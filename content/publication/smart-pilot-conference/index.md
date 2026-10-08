{
  "title": "Wireless Rate Adaptation via Smart Pilot",
  "date": "2014-10-01",
  "date_precision": 2,
  "authors": [
    "Lu Wang",
    "Xiaoke Qi",
    "Jiang Xiao",
    "Kaishun Wu",
    "Mounir Hamdi",
    "Qian Zhang"
  ],
  "publication": "2014 IEEE 22nd International Conference on Network Protocols",
  "venue_short": "ICNP",
  "publication_kind": "Conference",
  "topic": "wireless",
  "summary": "Smart Pilot adapts wireless transmission rates using richer information about the current channel. It addresses rapidly changing and frequency-selective conditions that can undermine conventional rate estimates.",
  "doi": "10.1109/icnp.2014.64",
  "volume": "",
  "issue": "",
  "pages": "409-420",
  "source_url": "https://doi.org/10.1109/icnp.2014.64",
  "status": "Published",
  "slug": "smart-pilot-conference",
  "short_title": "Wireless Rate Adaptation via Smart Pilot",
  "url_pdf": "/papers/2014-smart-pilot-conference.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Wireless_Rate_Adaptation_via_Smart_Pilot.pdf",
  "featured": false,
  "overview_source": "/papers/2014-smart-pilot-conference.pdf"
}

A channel estimate derived from a small set of known symbols may become inaccurate as the channel changes. Smart Pilot extracts additional reliable information from both the physical-layer decoder and upper-layer protocol headers, using those bits as extra references to calibrate CSI with little additional signaling.

A greedy rate-selection algorithm then uses the calibrated information across subcarriers. GNU Radio experiments and trace-driven simulations examine channel tracking and rate prediction. The contribution is a cross-layer source of channel knowledge for faster, finer-grained wireless adaptation.
