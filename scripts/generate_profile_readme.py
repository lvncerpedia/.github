import os
import re
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

load_dotenv()

PROFILE_DIR = Path(__file__).resolve().parent.parent / "profile"
REPOS_YAML = PROFILE_DIR / "repos.yaml"
README = PROFILE_DIR / "README.md"

UNCATEGORIZED = "未分類"
MARKER_START = "<!-- REPOS:START -->"
MARKER_END = "<!-- REPOS:END -->"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)


def load_config():
    return yaml.load(REPOS_YAML.read_text(encoding="utf-8"))


def listed_names(config):
    names = set()
    for category in config["categories"]:
        for repo in category["repos"] or []:
            names.add(str(repo["name"]).lower())
    return names


def fetch_org_repos(org, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(repo["name"] for repo in data)
        page += 1
    return repos


def uncategorized_category(config):
    for category in config["categories"]:
        if category["name"] == UNCATEGORIZED:
            return category
    category = CommentedMap()
    category["name"] = UNCATEGORIZED
    category["repos"] = []
    config["categories"].append(category)
    return category


def add_repo(category, name):
    entry = CommentedMap()
    entry["name"] = name
    entry["memo"] = ""
    entry.fa.set_flow_style()
    category["repos"].append(entry)


def sync_with_org(config, org_repos):
    listed = listed_names(config)
    new_repos = sorted(name for name in org_repos if name.lower() not in listed)

    if new_repos:
        category = uncategorized_category(config)
        for name in new_repos:
            add_repo(category, name)
        print(f"Added {len(new_repos)} new repo(s) to {UNCATEGORIZED}: {', '.join(new_repos)}")

    org_lower = {name.lower() for name in org_repos}
    for category in config["categories"]:
        for repo in category["repos"] or []:
            if str(repo["name"]).lower() not in org_lower:
                print(f"WARNING: '{repo['name']}' is listed but not found in org (not removed)")

    return new_repos


def render_tables(config, org):
    blocks = []
    for category in config["categories"]:
        repos = category["repos"] or []
        if not repos:
            continue
        lines = [
            f"## {category['name']}",
            "",
            "| Repository | Repository URL | Memo |",
            "| --- | --- | --- |",
        ]
        for repo in repos:
            name = repo["name"]
            memo = repo.get("memo") or ""
            url = f"https://github.com/{org}/{name}"
            lines.append(f"| `{name}` | [GitHub]({url}) | {memo} |")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def replace_markers(readme_text, generated):
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    replacement = f"{MARKER_START}\n\n{generated}\n\n{MARKER_END}"
    if not pattern.search(readme_text):
        raise SystemExit(f"Markers {MARKER_START} / {MARKER_END} not found in README.md")
    return pattern.sub(replacement, readme_text)


def dump_yaml(config):
    from io import StringIO

    stream = StringIO()
    yaml.dump(config, stream)
    return stream.getvalue()


def main():
    check_only = "--check" in sys.argv

    config = load_config()
    org = config.get("org", "lvncerpedia")

    token = os.getenv("GITHUB_TOKEN")
    if token:
        org_repos = fetch_org_repos(org, token)
        print(f"Fetched {len(org_repos)} repos from org '{org}'")
        sync_with_org(config, org_repos)
    else:
        print("No GITHUB_TOKEN: skipping org sync, rendering from repos.yaml only")

    new_yaml = dump_yaml(config)
    generated = render_tables(config, org)
    new_readme = replace_markers(README.read_text(encoding="utf-8"), generated)

    current_yaml = REPOS_YAML.read_text(encoding="utf-8")
    current_readme = README.read_text(encoding="utf-8")
    changed = new_yaml != current_yaml or new_readme != current_readme

    if check_only:
        if changed:
            print("CHECK FAILED: repos.yaml or README.md is out of date. Run the generator.")
            sys.exit(1)
        print("CHECK OK: profile README is up to date")
        return

    if not changed:
        print("No changes")
        return

    REPOS_YAML.write_text(new_yaml, encoding="utf-8")
    README.write_text(new_readme, encoding="utf-8")
    print("Updated repos.yaml and README.md")


if __name__ == "__main__":
    main()
