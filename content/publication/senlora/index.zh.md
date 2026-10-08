{
  "title": "SenLoRa: Integrated Sensing and Communication with Ambient LoRa",
  "date": "2025-09-03",
  "date_precision": 3,
  "authors": [
    "Lu Wang",
    "Hao Wang",
    "Boliang Guo",
    "Xiaoshen Li",
    "Yongzhi Huang",
    "Junmei Yao",
    "Kaishun Wu"
  ],
  "publication": "Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies",
  "venue_short": "IMWUT / UbiComp",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "SenLoRa 将感知与环境 LoRa 通信相结合，复用日常网络流量中的信息，在保留标准通信能力的同时实现感知。",
  "doi": "10.1145/3749522",
  "volume": "9",
  "issue": "3",
  "pages": "1-26",
  "source_url": "https://doi.org/10.1145/3749522",
  "status": "Published",
  "slug": "senlora",
  "short_title": "SenLoRa",
  "cover": "/research/senlora.jpg",
  "cover_alt": "SenLoRa 研究示意图",
  "cover_caption": "SenLoRa 实验装置，图片来自共同作者 Yongzhi Huang 的项目主页。",
  "featured": true,
  "feature_order": 3,
  "overview_source": "https://doi.org/10.1145/3749522"
}

日常 LoRa 流量较稀疏、数据速率较低，仅使用数据包前导码进行感知时，可用信息有限。SenLoRa 引入感知通信比（SCR）和逐符号感知熵来描述这种权衡，并利用似然比准则筛选有效载荷中的高置信度符号，使普通通信数据包中的更多信息能够用于感知。

在流量不足时，系统通过激励策略补充感知信息。论文案例报告了最低 0.2 次/分钟的呼吸检测误差及超过 90% 的行走检测准确率，同时保持标准 LoRa 通信。这项研究展示了如何复用通信载荷开展感知，减少对独立专用感知信号的依赖。
