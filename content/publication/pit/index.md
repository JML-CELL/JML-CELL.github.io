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
  "summary": "PIT provides real-time plaque indication during toothbrushing. Optical sensing helps users locate stained plaque even when toothpaste foam obscures the tooth surface.",
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
  "cover_alt": "Research illustration for PIT",
  "cover_caption": "Illustration from the authors’ research paper.",
  "featured": true,
  "feature_order": 1,
  "overview_source": "/papers/2025-pit.pdf"
}

Plaque-disclosing agents make dental plaque visible before brushing, but toothpaste foam can hide the stained areas during cleaning. PIT combines a miniature camera, four green LEDs, and a mechanical design that stabilizes the view around the bristles. An optical channel model guides illumination, and a dedicated neural network segments plaque through foam.

A distilled model runs on a smartphone to provide feedback during brushing. Tests on denture models and human participants report 75.22% segmentation IoU and 29 ms latency. In a study with 10 participants, plaque coverage fell to 5.6% after two minutes of brushing. These results describe the evaluated prototype and study conditions.
