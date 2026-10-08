{
  "title": "Fedeval: Defending Against Lazybone Attack via Multi-dimension Evaluation in Federated Learning",
  "date": "2025-01-31",
  "date_precision": 3,
  "authors": [
    "Hao Wang",
    "Haoran Zhang",
    "Lu Wang",
    "Shichang Xuan",
    "Qian Zhang"
  ],
  "publication": "ACM Transactions on Sensor Networks",
  "venue_short": "ACM TOSN",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "FedEval addresses lazybone attacks in federated learning, where participants contribute less useful work than expected. It evaluates contributions along multiple dimensions to help protect collaborative model training.",
  "doi": "10.1145/3703631",
  "volume": "21",
  "issue": "1",
  "pages": "1-23",
  "source_url": "https://doi.org/10.1145/3703631",
  "status": "Published",
  "slug": "fedeval",
  "short_title": "Fedeval",
  "featured": false,
  "overview_source": "https://doi.org/10.1145/3703631"
}

Federated learning relies on useful contributions from participating devices, but a participant may reduce its effort by supplying poor-quality data or performing too little local training. Fedeval frames this as a contribution-evaluation problem and combines multiple dimensions of evidence rather than treating every submitted update as equally informative.

The framework connects evaluation with the aggregation of client contributions, aiming to limit the effect of low-effort participants on collaborative training. The work concerns the reliability of participation in resource-constrained settings, complementing the usual focus on keeping raw training data decentralized.
