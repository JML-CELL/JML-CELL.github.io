{
  "title": "Exploring Partially Overlapping Channels for Low-power Wide Area Networks",
  "date": "2022-11-30",
  "date_precision": 3,
  "authors": [
    "Lu Wang",
    "Xiaoke Qi",
    "Ruifeng Huang",
    "Kaishun Wu",
    "Qian Zhang"
  ],
  "publication": "ACM Transactions on Sensor Networks",
  "venue_short": "ACM TOSN",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "This work explores partially overlapping channels for LoRa-based low-power wide-area networks. A learning-based spectrum-sharing design uses coding redundancy to support more concurrent spectrum access.",
  "doi": "10.1145/3546075",
  "volume": "18",
  "issue": "4",
  "pages": "1-20",
  "source_url": "https://doi.org/10.1145/3546075",
  "status": "Published",
  "slug": "overlapping-lpwan",
  "short_title": "Exploring Partially Overlapping Channels for Low-power Wide Area Networks",
  "url_pdf": "/papers/2022-overlapping-lpwan.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Exploring%20Partially%20Overlapping%20Channels%20for%20Low-power%20Wide%20Area%20Networks.pdf",
  "featured": false,
  "overview_source": "/papers/2022-overlapping-lpwan.pdf"
}

Strictly separating LoRa channels limits how many devices can transmit concurrently. Intelligent Overlapping uses a deep-Q-learning design to estimate available coding redundancy and choose a suitable overlap between channels. Information from the non-overlapping portion helps recover data affected by interference.

At the MAC layer, the method predicts channel conditions and assigns overlap; at the physical layer, interleaving spreads interference to preserve decodability. Simulations assess spectrum efficiency and convergence. The work connects learning-based access control with the error-correction properties of the transmitted signal.
