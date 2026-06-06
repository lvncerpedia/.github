# lvncerpedia

lvncerpeida is lvncers knowledge base.

<img width=200 src="../images/l.png" >

## License

このOrganization配下の全リポジトリは、特に明記されていない限り [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) のもとで公開されています。

- 個人利用・学習目的での使用・改変・再配布は自由です
- 商用利用は禁止です
- 利用の際はこのリポジトリへのクレジット表記をお願いします

## カテゴリの考え方

lvncerpedia のリポジトリは **トピック1リポ**（`react`, `architecture` など）。
カテゴリは索引用のメタデータで、トピックの細分化は各 repo 内の Markdown で行う。

分類は **2段** で管理する。

- **大箱（グループ）**: 大学の学部に近い10分類。AI と人間が同じ名称で認識できる単位
- **小箱（カテゴリ）**: 大箱の中をさらに分ける専攻・講義群

### 10の大箱

| 大箱 | 一言説明 |
| --- | --- |
| 理学 | 数学・計算の原理 |
| コンピュータ科学 | 計算機・OSの原理 |
| ソフトウェア工学 | システム開発（設計・実装・品質・運用） |
| 情報・知能 | AI・データ |
| デザイン | 見た目・表現・メディア |
| 人文・言語 | 言語を学ぶ |
| 教養・文化 | 知識・ゲーム・時事 |
| 経営学 | PM・組織・戦略 |
| 環境・ツール | 開発環境・ガジェット |
| 管理 | Org 運用・未分類 |

### 新しいリポジトリを作る基準

新規 repo は次の3つを **すべて満たすとき** だけ作る。満たさないなら既存 repo に Markdown を足す。

1. 既存 repo に Markdown 1ファイルで足せないか？
2. 半年以上触り続けそうか？
3. 10ファイル以上になりそうか？

迷ったら新規作成し、`未分類` に置いて後で正しいカテゴリへ移動する。
同じスタックの細分化（例: React → hooks）では repo を増やさず、中身のファイルで分ける。

### 境界の優先ルール

分類に迷ったときは上から順に判定する。

1. README の目的行で「主たる知識」を1つに決める
2. 言語・文学 → 人文・言語
3. 開発環境・ガジェット・デスク → 環境・ツール
4. PM・組織・戦略 → 経営学
5. 時事・探究・文化 → 教養・文化
6. それでも迷う → 未分類（CI が自動で拾う）

例外的な配置:

- **ゲーム** — 制作 repo（`game-making`, `godot` など）も **教養・文化** に置く。ゲームは文化・趣味として扱う特例
- **`ai-positions`** — 経営学ではなく **情報・知能**。AI 領域の人物・動向として扱う
- **`mermaid`** — ソフトウェア工学・設計（設計ドキュメント用途が中心）
- **`claude-code`** — 情報・知能・AI・LLM（AI 開発ツール）
- **`tailwindcss`** — ソフトウェア工学・実装（スタイルも実装の一部として扱う）

# Repository Categories

<!-- REPOS:START -->

## 理学

数学・計算の原理。

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `math` | [GitHub](https://github.com/lvncerpedia/math) | 数学 |
| `algorithm-and-data-structure` | [GitHub](https://github.com/lvncerpedia/algorithm-and-data-structure) | アルゴリズム・データ構造 |

## コンピュータ科学

計算機・OSの原理。

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `computer-science` | [GitHub](https://github.com/lvncerpedia/computer-science) | コンピュータサイエンス |
| `os` | [GitHub](https://github.com/lvncerpedia/os) | オペレーティングシステム |

## ソフトウェア工学

システム開発（設計・実装・品質・運用）。

### 設計

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `architecture` | [GitHub](https://github.com/lvncerpedia/architecture) | ソフトウェアアーキテクチャ |
| `development-principles` | [GitHub](https://github.com/lvncerpedia/development-principles) | 開発原則 |
| `uml` | [GitHub](https://github.com/lvncerpedia/uml) | UML |
| `mermaid` | [GitHub](https://github.com/lvncerpedia/mermaid) | Mermaid図 |

### 実装

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `programming` | [GitHub](https://github.com/lvncerpedia/programming) | プログラミング全般 |
| `programming-lang` | [GitHub](https://github.com/lvncerpedia/programming-lang) | プログラミング言語全般 |
| `go` | [GitHub](https://github.com/lvncerpedia/go) | Go |
| `rust` | [GitHub](https://github.com/lvncerpedia/rust) | Rust |
| `java` | [GitHub](https://github.com/lvncerpedia/java) | Java |
| `react` | [GitHub](https://github.com/lvncerpedia/react) | React |
| `react-native` | [GitHub](https://github.com/lvncerpedia/react-native) | React Native |
| `nextjs` | [GitHub](https://github.com/lvncerpedia/nextjs) | Next.js |
| `rails` | [GitHub](https://github.com/lvncerpedia/rails) | Rails |
| `web-saas` | [GitHub](https://github.com/lvncerpedia/web-saas) | Web/SaaS関連 |
| `js-libraries` | [GitHub](https://github.com/lvncerpedia/js-libraries) | JavaScriptライブラリ |
| `tailwindcss` | [GitHub](https://github.com/lvncerpedia/tailwindcss) | Tailwind CSS |

### 品質

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `software-test` | [GitHub](https://github.com/lvncerpedia/software-test) | ソフトウェアテスト |
| `debug` | [GitHub](https://github.com/lvncerpedia/debug) | デバッグ |

### 運用

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `aws` | [GitHub](https://github.com/lvncerpedia/aws) | AWS |
| `docker` | [GitHub](https://github.com/lvncerpedia/docker) | Docker |
| `kubernetes` | [GitHub](https://github.com/lvncerpedia/kubernetes) | Kubernetes関連 |
| `iac` | [GitHub](https://github.com/lvncerpedia/iac) | Infrastructure as Code |
| `network` | [GitHub](https://github.com/lvncerpedia/network) | ネットワーク |
| `monitoring` | [GitHub](https://github.com/lvncerpedia/monitoring) | 監視 |
| `git` | [GitHub](https://github.com/lvncerpedia/git) | Git |
| `workflows` | [GitHub](https://github.com/lvncerpedia/workflows) | ワークフロー自動化 |

## 情報・知能

AI・データ。

### AI・LLM

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `llm` | [GitHub](https://github.com/lvncerpedia/llm) | LLMの基礎・仕組み |
| `ml` | [GitHub](https://github.com/lvncerpedia/ml) | 機械学習 |
| `ai-agents` | [GitHub](https://github.com/lvncerpedia/ai-agents) | AIエージェント関連 |
| `local-llm` | [GitHub](https://github.com/lvncerpedia/local-llm) | ローカルLLM |
| `mcp` | [GitHub](https://github.com/lvncerpedia/mcp) | MCP・AIツール連携 |
| `claude-code` | [GitHub](https://github.com/lvncerpedia/claude-code) | Claude Code |
| `humanoid-robots` | [GitHub](https://github.com/lvncerpedia/humanoid-robots) | ヒューマノイドロボット |
| `ai-positions` | [GitHub](https://github.com/lvncerpedia/ai-positions) | AI領域の人物・ポジション |

### データ

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `database` | [GitHub](https://github.com/lvncerpedia/database) | データベース |
| `sql` | [GitHub](https://github.com/lvncerpedia/sql) | SQL |
| `orm` | [GitHub](https://github.com/lvncerpedia/orm) | ORM |

## デザイン

見た目・表現・メディア。

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `design` | [GitHub](https://github.com/lvncerpedia/design) | デザイン |
| `figma` | [GitHub](https://github.com/lvncerpedia/figma) | Figma |
| `fonts` | [GitHub](https://github.com/lvncerpedia/fonts) | フォント |
| `sound` | [GitHub](https://github.com/lvncerpedia/sound) | サウンド |
| `audio` | [GitHub](https://github.com/lvncerpedia/audio) | オーディオ機器・音響 |
| `presentation` | [GitHub](https://github.com/lvncerpedia/presentation) | プレゼンテーション |
| `modeling` | [GitHub](https://github.com/lvncerpedia/modeling) | 3D モデリング |

## 人文・言語

言語を学ぶ。

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `english` | [GitHub](https://github.com/lvncerpedia/english) | 英語 |

## 教養・文化

知識・ゲーム・時事。

### 文化・ゲーム

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `game-making` | [GitHub](https://github.com/lvncerpedia/game-making) | ゲーム制作全般（技術面） |
| `game-knowhow` | [GitHub](https://github.com/lvncerpedia/game-knowhow) | ゲーム制作ノウハウ |
| `godot` | [GitHub](https://github.com/lvncerpedia/godot) | Godot |
| `game-list` | [GitHub](https://github.com/lvncerpedia/game-list) | ゲーム一覧 |

### 知識・探究

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `universe` | [GitHub](https://github.com/lvncerpedia/universe) | 宇宙 |
| `military` | [GitHub](https://github.com/lvncerpedia/military) | 軍事・装備 |
| `exams` | [GitHub](https://github.com/lvncerpedia/exams) | 試験・学習メモ |

### 時事・記録

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `news` | [GitHub](https://github.com/lvncerpedia/news) | ニュースメモ |
| `news-source` | [GitHub](https://github.com/lvncerpedia/news-source) | ニュース情報源 |
| `events` | [GitHub](https://github.com/lvncerpedia/events) | イベント |

## 経営学

PM・組織・戦略。

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `project-management` | [GitHub](https://github.com/lvncerpedia/project-management) | プロジェクト管理 |

## 環境・ツール

開発環境・ガジェット。

### 開発環境

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `nvim` | [GitHub](https://github.com/lvncerpedia/nvim) | Neovim |
| `obsidian` | [GitHub](https://github.com/lvncerpedia/obsidian) | Obsidian |
| `toolchain` | [GitHub](https://github.com/lvncerpedia/toolchain) | 開発ツールチェーン |

### ハードウェア

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `gadget` | [GitHub](https://github.com/lvncerpedia/gadget) | ガジェット |
| `custom-built-PC` | [GitHub](https://github.com/lvncerpedia/custom-built-PC) | 自作PC |
| `custom-keyboard` | [GitHub](https://github.com/lvncerpedia/custom-keyboard) | 自作キーボード |

### デスク・操作

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `unixporn` | [GitHub](https://github.com/lvncerpedia/unixporn) | デスクトップカスタマイズ |
| `setup` | [GitHub](https://github.com/lvncerpedia/setup) | 環境構築・セットアップ |
| `shortcut` | [GitHub](https://github.com/lvncerpedia/shortcut) | ショートカット |

## 管理

Org 運用・未分類。

### Org

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `.github` | [GitHub](https://github.com/lvncerpedia/.github) | Organizationプロフィール・同期スクリプト |

<!-- REPOS:END -->
