{
  "title": "On Exploiting Concurrent Transmissions Through Discernible Interference Cancellation",
  "date": "2018-10-01",
  "date_precision": 2,
  "authors": [
    "Junmei Yao",
    "Wei Lou",
    "Lu Wang",
    "Kaishun Wu"
  ],
  "publication": "IEEE Transactions on Vehicular Technology",
  "venue_short": "IEEE TVT",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "ICMR 是一种利用干扰消除支持更多并发无线传输的跨层协议，研究活动链路两端附近节点的传输机会。",
  "doi": "10.1109/tvt.2018.2853716",
  "volume": "67",
  "issue": "10",
  "pages": "9370-9384",
  "source_url": "https://doi.org/10.1109/tvt.2018.2853716",
  "status": "Published",
  "slug": "concurrent-cancellation",
  "short_title": "On Exploiting Concurrent Transmissions Through Discernible Interference Cancellation",
  "url_pdf": "/papers/2018-concurrent-cancellation.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/On%20Exploiting%20Concurrent%20Transmissions%20through%20Discernible%20Interference%20Cancellation.pdf",
  "featured": false,
  "overview_source": "/papers/2018-concurrent-cancellation.pdf"
}

传统接入规则可能浪费活动链路两端附近的并发机会。ICMR 特别关注接收端，利用可辨识干扰消除，使数据帧与控制帧重叠时仍有机会正确解码；MAC 层据此允许更多并发传输。

论文建模分析发送与接收机会，在 USRP2 硬件上验证干扰消除，并通过 ns-2 仿真评估吞吐量。工作将具体的物理层干扰管理机制与跨层协议连接起来，避免简单地将所有重叠传输都视为失败。
