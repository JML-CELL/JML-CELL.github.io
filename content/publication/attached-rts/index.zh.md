{
  "title": "Attached-RTS: Eliminating an Exposed Terminal Problem in Wireless Networks",
  "date": "2013-07-01",
  "date_precision": 2,
  "authors": [
    "Lu Wang",
    "Kaishun Wu",
    "Mounir Hamdi"
  ],
  "publication": "IEEE Transactions on Parallel and Distributed Systems",
  "venue_short": "IEEE TPDS",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "Attached-RTS 在数据传输的同时携带控制信息，以缓解暴露终端问题，帮助无线节点识别可安全并发接入的机会。",
  "doi": "10.1109/tpds.2012.228",
  "volume": "24",
  "issue": "7",
  "pages": "1289-1299",
  "source_url": "https://doi.org/10.1109/tpds.2012.228",
  "status": "Published",
  "slug": "attached-rts",
  "short_title": "Attached-RTS",
  "url_pdf": "/papers/2013-attached-rts.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Attached-RTS-%20Eliminating%20an%20Exposed%20Terminal%20Problem%20in%20Wireless%20Networks.pdf",
  "featured": false,
  "overview_source": "/papers/2013-attached-rts.pdf"
}

节点检测到信道忙，并不一定意味着它的发送会干扰正在接收的节点。Attached-RTS 利用 Attachment Coding 在数据传输的同时携带控制信息，使邻近节点更准确地了解发送与接收状态；AR-MAC 再利用这些信息识别暴露终端并安排并发接入。

论文对编码机制进行理论分析，在 GNU Radio 平台验证其可行性，并通过仿真评估 MAC 性能。贡献在于以较低开销连接物理层信令与介质访问决策，找回仅凭“忙或闲”判断容易错过的传输机会。
