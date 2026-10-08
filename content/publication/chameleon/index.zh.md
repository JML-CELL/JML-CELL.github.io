{
  "title": "Chameleon: An Adaptive System for Overlapping Keystroke Signal Separation and Identification",
  "date": "2024-10-10",
  "date_precision": 3,
  "authors": [
    "Jiayi Zhao",
    "Yongzhi Huang",
    "Qipeng Xie",
    "Weizheng Wang",
    "Lu Wang",
    "Kaishun Wu"
  ],
  "publication": "2024 IEEE 30th International Conference on Parallel and Distributed Systems (ICPADS)",
  "venue_short": "ICPADS",
  "publication_kind": "Conference",
  "topic": "interaction",
  "summary": "Chameleon 分离并识别相互叠加的击键信号，通过自适应设计处理同时输入，解决基于单次独立击键建立的模型难以识别重叠输入的问题。",
  "doi": "10.1109/icpads63350.2024.00018",
  "volume": "",
  "issue": "",
  "pages": "60-67",
  "source_url": "https://doi.org/10.1109/icpads63350.2024.00018",
  "status": "Published",
  "slug": "chameleon",
  "short_title": "Chameleon",
  "url_pdf": "/papers/2024-chameleon.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "Original project: static/uploads/Chameleon.pdf",
  "cover": "/research/chameleon.png",
  "cover_alt": "Chameleon 研究示意图",
  "cover_caption": "论文中的研究示意图。",
  "featured": false,
  "overview_source": "/papers/2024-chameleon.pdf"
}

能够识别独立击键，并不意味着能够处理两次击键重叠或采集环境改变的情况。Chameleon 使用低计算开销的 Ranking Model 分离重叠信号，再利用 Fréchet Inception Distance 衡量分布变化，通过 Inductive Vector 调整识别模型，以适应不同手机位置、用户及环境。

论文分别评估信号分离与模型适配，报告分离信号的平均识别准确率为 92.69%。这项工作的重点是将分离与适配连接为完整流程，同时应对并发输入和信号采集条件变化。
