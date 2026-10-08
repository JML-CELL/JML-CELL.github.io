# Lu Wang · Shenzhen University

王璐个人学术主页，使用 Hugo 0.150.0 Extended 构建。新版采用本地模板、CSS 与少量原生 JavaScript；运行和构建不需要 Node、数据库或下载 HugoBlox 主题。

## 本地预览

```powershell
hugo server --bind 127.0.0.1 --port 1313 --disableFastRender
```

浏览器打开 `http://localhost:1313/`。

## 构建与检查

```powershell
python scripts/export_bibtex.py
hugo --minify
python scripts/check_site.py --public public
```

Python 脚本仅使用标准库。检查包括重复 DOI/PDF、作者、必要字段、引用文件、站内链接、资源、锚点与模板占位内容，也检查双语页面对应关系、引用元数据一致性和新闻完整题名。

## 中英文内容维护

默认英文位于 `/`，简体中文位于 `/zh/`。页首语言按钮切换到当前页面的另一语言版本，并保留搜索、筛选与锚点；无需浏览器自动翻译或外部翻译服务。

- `index.md` / `_index.md` 是英文内容，目录内对应的 `index.zh.md` / `_index.zh.md` 是中文内容。
- `data/translations.json` 存放界面文字；英文短语作为键，简体中文作为值。`layouts/partials/t.html` 按当前语言输出。
- `data/research.json` 与 `data/research_zh.json` 分别维护两个语言的研究方向。
- 新增或修改论文时同步中文简介，保持题名、作者、发表时间、刊物、DOI、PDF 路径等元数据一致。英文题名、作者名、刊物名及 BibTeX 保留原文，以便准确检索与引用。
- 两种语言共享 PDF、研究图、头像与引用文件，无需复制资源。论文搜索同时索引两种语言的简介。
- 新闻标题使用对应论文的完整原题；中文正文提供简介和出版信息。团队姓名沿用原资料，仅翻译角色与页面说明。

## 内容位置

- `content/about/index.md`：简介、教学、奖励与学术服务。
- `data/research.json`：三个研究方向及介绍。
- `content/publication/<slug>/index.md`：论文元数据与原创简介。
- `content/post/`：按出版月份整理的新闻。
- `content/authors/`：团队姓名、角色与头像；学生原资料保持不变。
- `static/papers/`：67 份已核对的 PDF；旧 `static/uploads/` 保留兼容原链接。
- `assets/research/`：从已有材料与论文取得的研究图；构建时自动生成适合手机和桌面的 WebP 图像。
- `layouts/`、`assets/css/site.css`、`assets/js/site.js`：版式、样式与交互。
- `docs/publication-sources.csv`：每条已发表成果的来源、PDF 来源及校验值。
- `docs/review-notes.md`：本轮审查记录与缺少 PDF 的清单。

## 新增或修改论文

复制一个现有论文目录，修改 `index.md` 顶部的 JSON 信息。必须核实题名、完整作者顺序、发表状态、年份、刊物与 DOI，避免把投稿状态或同名作者的工作直接加入。

- `publication_kind` 可选 `Journal`、`Conference`、`Poster / Demo`、`Book chapter`、`Book`。不要使用 Hugo 保留字段 `kind`。
- `topic` 可选 `wireless`、`sensing`、`interaction`。
- `date_precision`：1 表示只核实年份，2 表示年月，3 表示完整日期。只有年月时 `date` 使用当月 01 日作为排序值，页面和学术元标签按实际精度输出。
- `url_pdf` 只填已经确认与该条目匹配的 PDF；没有文件时省略，页面会保留出版入口。
- `featured: true` 和 `feature_order` 控制首页六篇精选论文。
- 修改后运行 `python scripts/export_bibtex.py`，同步各论文引用和完整书目下载，再构建检查。

## 论文详细介绍与临时头像

- 论文 JSON 前置信息之后的正文为详细介绍，中英文各维护一份；概述、方法与已核实的实验结果应与对应论文版本一致。`overview_source` 指向所依据的论文或研究记录，来源与证据范围见 `docs/overview-sources.csv`。
- 学生当前统一使用 `assets/avatars/student-default.svg` 中的中性默认头像，`data/team_avatars.json` 将学生目录映射到该文件。此前的插画文件与生成记录保留，但已不用于页面。
- 日后换真实头像时，在对应 `content/authors/<学生目录>/` 中更新 `avatar.*`，并移除 `data/team_avatars.json` 中该学生的映射；团队页和个人页会同时使用真实头像。原姓名和学生资料未修改。

## 发布配置

默认正式域名为原主页 `https://luwang-szu.github.io/`，可在 `config/_default/hugo.yaml` 修改。GitHub Pages 工作流和 Netlify 配置都固定 Hugo 0.150.0。当前仅完成本地修改和预览，没有推送或发布。

原来面向 HugoBlox 的 BibTeX 自动导入工作流会产生不兼容的数据结构，已经移入 `archive/template-content/`；新版从论文前置信息统一生成引用。模板示例、演示活动和原新闻也归档在该目录，不参与 Hugo 发布。

原始项目的开源许可证保留。论文及研究图的版权属于原作者或出版机构，来源见核验记录。
