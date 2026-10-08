{
  "title": "FAST: Realizing what your neighbors are doing",
  "date": "2012-06-01",
  "date_precision": 2,
  "authors": [
    "Lu Wang",
    "Kaishun Wu",
    "Pengfei Chang",
    "Mounir Hamdi"
  ],
  "publication": "2012 IEEE International Conference on Communications (ICC)",
  "venue_short": "ICC",
  "publication_kind": "Conference",
  "topic": "wireless",
  "summary": "FAST 帮助无线节点了解邻近节点的发送与接收状态，利用这些信道占用信息，更准确地判断何时可以进行并发传输。",
  "doi": "10.1109/icc.2012.6364544",
  "volume": "",
  "issue": "",
  "pages": "544-548",
  "source_url": "https://doi.org/10.1109/icc.2012.6364544",
  "status": "Published",
  "slug": "fast",
  "short_title": "FAST",
  "url_pdf": "/papers/2012-fast.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/FAST_Realizing_what_your_neighbors_are_doing.pdf",
  "featured": false,
  "overview_source": "/papers/2012-fast.pdf"
}

隐藏终端会导致碰撞，暴露终端则会不必要地延迟发送。FAST 针对两者共同的信息缺口：邻近节点需要知道谁在发送、谁在接收。Attachment Coding 在物理层传递相关信息，Attachment Sense 再在 MAC 层区分两种情况。

研究通过自组织网络仿真评估系统。核心贡献是用同一套信道占用信息机制处理这两类问题，使接入决策不再只依赖“忙或闲”的粗粒度指示。
