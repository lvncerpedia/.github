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

- 大箱（グループ）: 知識の役割で分ける5つの大分類
- 小箱（カテゴリ）: 大箱の中をさらに分けるレイヤー

### 5つの大箱

| 大箱 | 役割 |
| --- | --- |
| コア — ソフトウェア工学 | 仕事の技術の土台（基礎 → 設計 → 実装 → 運用） |
| 応用 — 専門領域 | 特定ドメインへの応用（AI・データ・ゲーム） |
| 方法論 — ツールと生産性 | 全領域を横断するやり方・環境 |
| 教養 — インプットと趣味 | 仕事外の知的好奇心・情報収集 |
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
2. 横断ツール（Git, Neovim など）→ 方法論
3. 時事・趣味・教養 → 教養
4. それでも迷う → 未分類（CI が自動で拾う）

例外的な配置（運用で迷いやすいもの）:

- `mermaid` → 設計（図はツールだが設計ドキュメント用途が中心）
- `claude-code` → AI・知能（AI 開発ツールとして応用側に置く）
- `web-saas` → 実装（SaaS も実装の一形態）
- `game-list` → 教養（制作ではなく消費・記録のため）

# Repository Categories

<!-- REPOS:START -->

## コア — ソフトウェア工学

仕事の技術の土台。基礎→設計→実装→運用のレイヤー。

### 基礎

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `math` | [GitHub](https://github.com/lvncerpedia/math) | 数学 |
| `computer-science` | [GitHub](https://github.com/lvncerpedia/computer-science) | コンピュータサイエンス |
| `algorithm-and-data-structure` | [GitHub](https://github.com/lvncerpedia/algorithm-and-data-structure) | アルゴリズム・データ構造 |
| `os` | [GitHub](https://github.com/lvncerpedia/os) | オペレーティングシステム |

### 設計

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `architecture` | [GitHub](https://github.com/lvncerpedia/architecture) | ソフトウェアアーキテクチャ |
| `development-principles` | [GitHub](https://github.com/lvncerpedia/development-principles) | 開発原則 |
| `uml` | [GitHub](https://github.com/lvncerpedia/uml) | UML |
| `software-test` | [GitHub](https://github.com/lvncerpedia/software-test) | ソフトウェアテスト |
| `mermaid` | [GitHub](https://github.com/lvncerpedia/mermaid) | Mermaid図 |

### 実装

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `programming` | [GitHub](https://github.com/lvncerpedia/programming) | プログラミング全般 |
| `programming-lang` | [GitHub](https://github.com/lvncerpedia/programming-lang) | プログラミング言語全般 |
| `java` | [GitHub](https://github.com/lvncerpedia/java) | Java |
| `go` | [GitHub](https://github.com/lvncerpedia/go) | Go |
| `rust` | [GitHub](https://github.com/lvncerpedia/rust) | Rust |
| `rails` | [GitHub](https://github.com/lvncerpedia/rails) | Rails |
| `react` | [GitHub](https://github.com/lvncerpedia/react) | React |
| `react-native` | [GitHub](https://github.com/lvncerpedia/react-native) | React Native |
| `nextjs` | [GitHub](https://github.com/lvncerpedia/nextjs) | Next.js |
| `js-libraries` | [GitHub](https://github.com/lvncerpedia/js-libraries) | JavaScriptライブラリ |
| `tailwindcss` | [GitHub](https://github.com/lvncerpedia/tailwindcss) | Tailwind CSS |
| `web-saas` | [GitHub](https://github.com/lvncerpedia/web-saas) | Web/SaaS関連 |

### 運用

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `aws` | [GitHub](https://github.com/lvncerpedia/aws) | AWS |
| `docker` | [GitHub](https://github.com/lvncerpedia/docker) | Docker |
| `kubernetes` | [GitHub](https://github.com/lvncerpedia/kubernetes) | Kubernetes関連 |
| `iac` | [GitHub](https://github.com/lvncerpedia/iac) | Infrastructure as Code |
| `network` | [GitHub](https://github.com/lvncerpedia/network) | ネットワーク |
| `monitoring` | [GitHub](https://github.com/lvncerpedia/monitoring) | 監視 |
| `workflows` | [GitHub](https://github.com/lvncerpedia/workflows) | ワークフロー自動化 |

## 応用 — 専門領域

特定ドメインへの応用（AI・データ・ゲーム）。

### AI・知能

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

### ゲーム制作

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `game-making` | [GitHub](https://github.com/lvncerpedia/game-making) | ゲーム制作全般（技術面） |
| `game-knowhow` | [GitHub](https://github.com/lvncerpedia/game-knowhow) | ゲーム制作ノウハウ |
| `godot` | [GitHub](https://github.com/lvncerpedia/godot) | Godot |

## 方法論 — ツールと生産性

全領域を横断するやり方・環境。

### 開発環境

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `setup` | [GitHub](https://github.com/lvncerpedia/setup) | 環境構築・セットアップ |
| `nvim` | [GitHub](https://github.com/lvncerpedia/nvim) | Neovim |
| `obsidian` | [GitHub](https://github.com/lvncerpedia/obsidian) | Obsidian |
| `shortcut` | [GitHub](https://github.com/lvncerpedia/shortcut) | ショートカット |
| `unixporn` | [GitHub](https://github.com/lvncerpedia/unixporn) | デスクトップカスタマイズ |

### ワークフロー

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `git` | [GitHub](https://github.com/lvncerpedia/git) | Git |
| `debug` | [GitHub](https://github.com/lvncerpedia/debug) | デバッグ |
| `toolchain` | [GitHub](https://github.com/lvncerpedia/toolchain) | 開発ツールチェーン |
| `project-management` | [GitHub](https://github.com/lvncerpedia/project-management) | プロジェクト管理 |

## 教養 — インプットと趣味

仕事外の知的好奇心・情報収集。

### 情報・時事

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `news` | [GitHub](https://github.com/lvncerpedia/news) | ニュースメモ |
| `news-source` | [GitHub](https://github.com/lvncerpedia/news-source) | ニュース情報源 |
| `events` | [GitHub](https://github.com/lvncerpedia/events) | イベント |

### 探究・学習

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `universe` | [GitHub](https://github.com/lvncerpedia/universe) | 宇宙 |
| `military` | [GitHub](https://github.com/lvncerpedia/military) | 軍事・装備 |
| `exams` | [GitHub](https://github.com/lvncerpedia/exams) | 試験・学習メモ |

### クリエイティブ・趣味

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `design` | [GitHub](https://github.com/lvncerpedia/design) | デザイン |
| `figma` | [GitHub](https://github.com/lvncerpedia/figma) | Figma |
| `fonts` | [GitHub](https://github.com/lvncerpedia/fonts) | フォント |
| `modeling` | [GitHub](https://github.com/lvncerpedia/modeling) | 3D モデリング |
| `sound` | [GitHub](https://github.com/lvncerpedia/sound) | サウンド |
| `audio` | [GitHub](https://github.com/lvncerpedia/audio) | オーディオ機器・音響 |
| `presentation` | [GitHub](https://github.com/lvncerpedia/presentation) | プレゼンテーション |
| `custom-built-PC` | [GitHub](https://github.com/lvncerpedia/custom-built-PC) | 自作PC |
| `custom-keyboard` | [GitHub](https://github.com/lvncerpedia/custom-keyboard) | 自作キーボード |
| `gadget` | [GitHub](https://github.com/lvncerpedia/gadget) | ガジェット |
| `game-list` | [GitHub](https://github.com/lvncerpedia/game-list) | ゲーム一覧 |

## 管理

Org運用・未分類。

### 管理

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `.github` | [GitHub](https://github.com/lvncerpedia/.github) | Organizationプロフィール・同期スクリプト |

### 未分類

| Repository | Repository URL | Memo |
| --- | --- | --- |
| `english` | [GitHub](https://github.com/lvncerpedia/english) |  |

<!-- REPOS:END -->
