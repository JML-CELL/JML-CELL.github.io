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
  "summary": "ICMR is a cross-layer protocol for enabling more concurrent wireless transmissions through interference cancellation. It examines transmission opportunities around both ends of an active wireless link.",
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

Conventional access rules can waste transmission opportunities around both ends of an active wireless link. ICMR examines the receiver side in particular, using discernible interference cancellation so that a data frame can remain decodable when it overlaps a control frame. The MAC design uses this physical-layer capability to permit additional concurrency.

The paper formulates transmission and reception opportunities, verifies cancellation on USRP2 hardware, and evaluates throughput with ns-2 simulations. The work links a specific interference-management mechanism to a cross-layer protocol rather than assuming that every overlapping transmission must fail.
