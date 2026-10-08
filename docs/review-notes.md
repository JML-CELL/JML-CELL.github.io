# 论文核验与交接记录

核验日期：2026-10-07。

已整理 83 项已发表成果（含专著、会议短文/演示），其中 67 项提供本地 PDF。范围为 Lu Wang 旧主页发表记录、Excel 中能由正式记录证实的成果，以及检索中进一步确认的合作论文。没有宣称穷尽她的全部职业生涯发表记录。

## 核验原则

- 身份以深圳大学王璐、旧主页、机构与合作者信息交叉确认，避免其他同名作者。
- 题名、完整作者顺序、DOI、卷期和日期优先采用出版者登记到 Crossref 的记录；对不完整记录用正式会议页面、机构仓储和原 PDF 补足。
- 67 份 PDF 均能解析，已比较题名、作者或 DOI；两份字体编码影响文字提取的 PDF 另外做了首页目视检查。
- 年份按当前正式出版记录整理；少数仅有年份或年月的记录没有在页面冒充精确发布日期。
- 会议版与期刊版分开；海报/演示单独标注。正文简介重新撰写，没有整段照搬摘要。
- Excel 中未确认录用/发表的记录没有加入公开页面；原 Excel 和投稿备注没有复制进网站。

## 已纠正的问题

- 旧主页 hJam 的 INFOCOM 链接指向 TMC 扩展版，会议条目已去掉错误 PDF。
- ISMIR 与 ICPADS 新闻目录名和内容不一致；保留原链接，校正标题、简介和配图对应。
- MeetSumAid 作者补齐 Kaixin Chen；LiT 使用项目中的正式版本，作者顺序与出版记录一致。
- FedEval 归入 ACM Transactions on Sensor Networks。
- InFit 按正式卷期归入 2023 年；Attached-RTS 按 2013 年；WiHumidity 区分 2016 年会议与 2017 年章节出版。
- 保留全部 14 个团队姓名；13 个学生资料文件未改动。教师职称、学历与联系方式改为可核实信息。

## 尚未取得匹配 PDF 的成果

这些条目有已发表记录，页面提供 DOI/出版页面，不用相似论文或其他版本充当 PDF。受限下载没有绕过验证或付费墙。

- [HJam: Attachment transmission in WLANs](https://doi.org/10.1109/infcom.2012.6195510)
- [ContractMind: Trust-calibration interaction design for AI contract review tools](https://doi.org/10.1016/j.ijhcs.2024.103411)
- [Optical Sensing-Based Intelligent Toothbrushing Monitoring System](https://doi.org/10.1109/tmc.2024.3479455)
- [Fedeval: Defending Against Lazybone Attack via Multi-dimension Evaluation in Federated Learning](https://doi.org/10.1145/3703631)
- [A lightweight group-based SDN-driven encryption protocol for smart home IoT devices](https://doi.org/10.1016/j.comnet.2024.110537)
- [CCM: Cooperative Cross-Boundary Multimodal Communication Leveraging Swarms of UAVs via Multiagent Reinforcement Learning](https://doi.org/10.1109/jiot.2026.3670433)
- [Collaborative Observation Imputation and Trajectory Prediction via Consistency Evaluation](https://doi.org/10.1109/tmc.2026.3664639)
- [TagEcho: Empowering Ambient LoRa Backscatter Tags With Adaptive Modulation](https://doi.org/10.1109/TMC.2026.3683550)
- [VNiScan-Fruit: A Non-Invasive Visible-Near Infrared Sensing System for Soluble Solids Content Estimation in Fruits](https://doi.org/10.1109/tmc.2026.3667385)
- [SenLoRa: Integrated Sensing and Communication with Ambient LoRa](https://doi.org/10.1145/3749522)
- [FELT: Federated Ensemble Learning for Long-Tailed IoT Data via Communication-Efficient Private Voting](https://doi.org/10.1109/jiot.2026.3690483)
- [COCO+: A Behavior-Aware Cause Identification Framework for Order Cancellation in Logistics Service](https://doi.org/10.1109/tmc.2026.3652201)
- [MTxLSTM: Multi-Task Learning for Gesture Recognition and Person Identification Using a Miniature Radar Sensor](https://doi.org/10.1109/tmc.2026.3653448)
- [RadarAttn: Efficient Radar-Based Human Activity Recognition by Integrating Visual Attention and Self-Attention](https://researchportal.northumbria.ac.uk/en/publications/radarattn-efficient-radar-based-human-activity-recognition-by-int/)
- [Study on MAC Protocol of LoRa Network Hidden Terminal Based on BTMA](https://www.jsjkx.com/EN/10.11896/jsjkx.240700203)
- [Attachment Transmission in Wireless Networks](https://doi.org/10.1007/978-3-319-04909-0)

## 验证

- Hugo 0.150.0 Extended 构建通过。
- 全站本地链接、资源、锚点及论文重复 DOI/PDF 检查见 `scripts/check_site.py`。
- 浏览器检查：1440px 桌面、390px 手机；检索、年份筛选、重置、无结果状态、手机菜单与 Escape、BibTeX 复制。
- 7 个主要页面及论文详情无横向溢出；团队 14 张照片均能加载；浏览器未记录 JavaScript 错误。
- 改动前的源代码备份保存在本机审查目录；模板示例和旧导入工作流保存在 `archive/template-content/`，不会被 Hugo 发布。

第三轮优化：原图保存在 `assets/research/`，Hugo 自动输出两种尺寸的 WebP，保留图中文字与完整比例。额外验证 320px 窄屏和 GitHub Pages 子路径构建，BibTeX 复制内容与目标 DOI 一致。学生资料文件逐字节与备份比较，全部未改变。

## 2026-10-08：职称、首页和双语修订

- 按用户提供的最新任职信息统一为 Professor / 教授；保留 Associate Editor 的期刊编委含义。
- 首页主介绍改为人工智能、移动与可穿戴计算、LoRa、智能感知、物联网、人机交互与协作标签，其他首页介绍改为客观表述。
- 简介页面的 Selected recognition 改为 Awards / 获奖。
- 使用 Hugo 双语页面：英文默认、中文 `/zh/`。已翻译主要页面、83 项成果简介、8 篇扩展研究介绍、14 篇新闻、教学、获奖和学术服务。论文原题、作者、期刊会议名、DOI 及引用保留原文。
- 14 条新闻全部使用论文完整题名；中英文保留同一论文、来源和下载关系。
- 语言切换保留当前页面、搜索条件与锚点；搜索同时索引中英简介。中文页面的菜单、日期、筛选状态、空结果提示和引用复制反馈均已翻译。
- 英文学生资料未修改；增加配对中文页面，姓名沿用原资料，角色由页面统一翻译。
- 生产压缩构建通过；243 个 HTML 页面站内链接和锚点检查通过，83 组双语论文的题名、作者、DOI、日期与学术引用元标签一致，67 份 PDF 保持原有对应关系。
- 浏览器实测中文关键词“牙菌斑”定位 PIT，切换英文后搜索结果仍保留；中文论文页 PDF 地址正确，BibTeX 复制反馈正常。手机中文首页、简介及完整新闻题名无横向溢出，手机菜单可正常使用。
- 复查并修复两个边界问题：320px 英文导航宽度溢出，以及子目录部署时中文导航路径/语言关联。1440px、390px 和 320px 视口复查通过；子目录生产构建及导航语言一致性检查通过；浏览器无 JavaScript 错误。

## 2026-10-08：详细介绍与团队头像

- 83 项成果的中英文详情均补充两段正文，说明研究问题、方法、应用与有依据的实验结果；列表保留简短摘要。每项详情附来源入口，核查范围见 `overview-sources.csv`。
- 67 项依据已匹配的本地论文，9 项依据出版社、作者或高校研究记录；其余 7 项仅展开已确认的研究范围，不补写未核实的技术机制或实验数字。会议版与期刊版的结果分别核对。
- 修正 FLoc 原简介中将地板振动定位误写成无线信号定位的问题，并修订 Taprint、低功耗输入系统和反向散射综述的概述，使其与论文一致。
- 13 位博士生及研究生使用不同的临时插画头像；原姓名、英文资料和原照片文件保留，教师继续使用真实照片。团队页与个人页共用头像映射；生成工具、提示词和文件关系见 `generated-avatar-prompts.json`。
- 语言按钮增加浅色背景和图标，中文界面以 English 标识返回英文。按钮继续对应当前页面。已实测 TagEcho 中英互切及 320px 窄屏。
- 修复 Windows 下头像目录反斜杠导致映射失效的问题，确认团队页 13 张插画及教师照片均正常加载。生产构建及 243 页资源、链接、双语对应关系检查通过。
