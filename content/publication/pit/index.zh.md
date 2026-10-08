{
  "title": "PIT: A Novel Toothbrush Providing Real-Time and Robust Plaque Indication During Brushing",
  "date": "2025-06-23",
  "date_precision": 3,
  "authors": [
    "Kaixin Chen",
    "Junfan Xiang",
    "Wanying Tan",
    "Keyu Chen",
    "Yaqiong Luo",
    "Chang Ma",
    "Kaishun Wu",
    "Lu Wang"
  ],
  "publication": "Proceedings of the 23rd Annual International Conference on Mobile Systems, Applications and Services",
  "venue_short": "MobiSys",
  "publication_kind": "Conference",
  "topic": "sensing",
  "summary": "PIT 在刷牙过程中提供实时牙菌斑指示，通过光学感知帮助用户定位染色后的牙菌斑，即使牙膏泡沫遮挡牙齿表面也能提供反馈。",
  "doi": "10.1145/3711875.3729124",
  "volume": "",
  "issue": "",
  "pages": "15-27",
  "source_url": "https://doi.org/10.1145/3711875.3729124",
  "status": "Published",
  "slug": "pit",
  "short_title": "PIT",
  "url_pdf": "/papers/2025-pit.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "Original project: static/uploads/PiT_Mosiy2025.pdf",
  "cover": "/research/pit.jpg",
  "cover_alt": "PIT 研究示意图",
  "cover_caption": "论文中的研究示意图。",
  "featured": true,
  "feature_order": 1,
  "overview_source": "/papers/2025-pit.pdf"
}

牙菌斑染色剂可以在刷牙前显示菌斑，但清洁时产生的牙膏泡沫会遮挡染色区域。PIT 将微型摄像头、四颗绿色 LED 与稳定刷毛周围视野的机械结构结合，利用光学信道模型指导照明设计，并训练专用神经网络分割泡沫下的牙菌斑。

系统将蒸馏后的轻量模型部署在智能手机上，在刷牙过程中提供反馈。义齿模型与人体实验报告了 75.22% 的分割 IoU 和 29 ms 的处理时延；10 位参与者的实验中，两分钟刷牙后的菌斑覆盖率降至 5.6%。这些数值对应论文所评估的原型与实验条件。
