{
  "title": "Pilot: Passive Device-Free Indoor Localization Using Channel State Information",
  "date": "2013-07-01",
  "date_precision": 2,
  "authors": [
    "Jiang Xiao",
    "Kaishun Wu",
    "Youwen Yi",
    "Lu Wang",
    "Lionel M. Ni"
  ],
  "publication": "2013 IEEE 33rd International Conference on Distributed Computing Systems",
  "venue_short": "ICDCS",
  "publication_kind": "Conference",
  "topic": "sensing",
  "summary": "Pilot uses channel state information for passive, device-free indoor localization. The system studies how a person's presence changes wireless propagation and how those changes can reveal location.",
  "doi": "10.1109/icdcs.2013.49",
  "volume": "",
  "issue": "",
  "pages": "236-245",
  "source_url": "https://doi.org/10.1109/icdcs.2013.49",
  "status": "Published",
  "slug": "pilot-localization",
  "short_title": "Pilot",
  "url_pdf": "/papers/2013-pilot-localization.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Pilot_Passive_Device-Free_Indoor_Localization_Using_Channel_State_Information.pdf",
  "featured": false,
  "overview_source": "/papers/2013-pilot-localization.pdf"
}

Pilot first builds a passive radio map containing CSI patterns for an empty space and for people at reference positions. An anomaly detector identifies when a person enters the monitored area, then a probabilistic matcher compares the changed signal with the map to estimate location. Data fusion addresses the presence of multiple people.

The prototype uses commercial IEEE 802.11n network cards and is tested in two indoor settings. The contribution is a complete workflow from detecting a person’s presence to localizing that person without requiring a carried transmitter, using channel structure rather than received power alone.
