{
  "title": "Pilot: Passive Device-Free Indoor Localization Using Channel State Information",
  "date": "2013-07-01",
  "date_precision": 2,
  "authors": [
    "Jiang Xiao",
    "Kaishun Wu",
    "Youwen Yi",
    "Lu Wang",
    "Lionel M. Ni"
  ],
  "publication": "2013 IEEE 33rd International Conference on Distributed Computing Systems",
  "venue_short": "ICDCS",
  "publication_kind": "Conference",
  "topic": "sensing",
  "summary": "Pilot 利用信道状态信息实现被动、无设备的室内定位，研究人体出现时引起的无线传播变化，以及如何从这些变化中提取位置信息。",
  "doi": "10.1109/icdcs.2013.49",
  "volume": "",
  "issue": "",
  "pages": "236-245",
  "source_url": "https://doi.org/10.1109/icdcs.2013.49",
  "status": "Published",
  "slug": "pilot-localization",
  "short_title": "Pilot",
  "url_pdf": "/papers/2013-pilot-localization.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Pilot_Passive_Device-Free_Indoor_Localization_Using_Channel_State_Information.pdf",
  "featured": false,
  "overview_source": "/papers/2013-pilot-localization.pdf"
}

Pilot 首先建立被动无线指纹图，记录空场景及人员位于参考位置时的 CSI 模式。异常检测器判断是否有人进入，再通过概率匹配将变化后的信号与指纹图比较以估计位置，并利用数据融合处理多人情况。

原型采用商用 IEEE 802.11n 网卡，在两类室内场景中测试。贡献是形成从人员出现检测到定位的完整流程，无需人员携带发射器，并利用信道结构而不只依赖接收功率。
