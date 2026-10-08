{
  "title": "SenLoRa: Integrated Sensing and Communication with Ambient LoRa",
  "date": "2025-09-03",
  "date_precision": 3,
  "authors": [
    "Lu Wang",
    "Hao Wang",
    "Boliang Guo",
    "Xiaoshen Li",
    "Yongzhi Huang",
    "Junmei Yao",
    "Kaishun Wu"
  ],
  "publication": "Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies",
  "venue_short": "IMWUT / UbiComp",
  "publication_kind": "Journal",
  "topic": "wireless",
  "summary": "SenLoRa integrates sensing with ambient LoRa communication. It reuses information in ordinary network traffic to enable sensing while retaining standard communication capabilities.",
  "doi": "10.1145/3749522",
  "volume": "9",
  "issue": "3",
  "pages": "1-26",
  "source_url": "https://doi.org/10.1145/3749522",
  "status": "Published",
  "slug": "senlora",
  "short_title": "SenLoRa",
  "cover": "/research/senlora.jpg",
  "cover_alt": "Research illustration for SenLoRa",
  "cover_caption": "SenLoRa experimental setup, from coauthor Yongzhi Huang’s project page.",
  "featured": true,
  "feature_order": 3,
  "overview_source": "https://doi.org/10.1145/3749522"
}

Ambient LoRa traffic is sparse and has a low data rate, so using only packet preambles leaves little information for sensing. SenLoRa introduces the Sensing–Communication Ratio and per-symbol sensing entropy to characterize this trade-off. It then uses a likelihood-ratio criterion to select high-confidence payload symbols, making more of an ordinary packet useful for sensing.

An incentive strategy supplies additional sensing information when traffic is insufficient. The reported case studies include respiration monitoring with an error as low as 0.2 breaths per minute and walking detection above 90% accuracy, while maintaining standard LoRa communication. The work illustrates how communication payloads can support sensing without a separate dedicated signal stream.
