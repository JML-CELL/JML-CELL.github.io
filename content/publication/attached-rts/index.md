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
  "summary": "Attached-RTS carries control information alongside data transmissions to address exposed terminals. The approach helps wireless nodes identify safe opportunities for concurrent access.",
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

A node that senses a busy channel may still be able to transmit safely if the ongoing receiver would not be disturbed. Attached-RTS uses Attachment Coding to carry control information alongside data, giving neighboring nodes a more precise view of who is transmitting and receiving. AR-MAC uses that information to identify exposed terminals and schedule concurrent access.

The paper analyzes the coding mechanism, validates its feasibility on a GNU Radio testbed, and evaluates MAC performance through simulation. The contribution is a low-overhead link between physical-layer signaling and medium-access decisions, recovering opportunities that coarse busy-or-idle sensing can miss.
