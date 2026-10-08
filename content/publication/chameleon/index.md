{
  "title": "Chameleon: An Adaptive System for Overlapping Keystroke Signal Separation and Identification",
  "date": "2024-10-10",
  "date_precision": 3,
  "authors": [
    "Jiayi Zhao",
    "Yongzhi Huang",
    "Qipeng Xie",
    "Weizheng Wang",
    "Lu Wang",
    "Kaishun Wu"
  ],
  "publication": "2024 IEEE 30th International Conference on Parallel and Distributed Systems (ICPADS)",
  "venue_short": "ICPADS",
  "publication_kind": "Conference",
  "topic": "interaction",
  "summary": "Chameleon separates and identifies overlapping keystroke signals. Its adaptive design addresses simultaneous inputs that are difficult to recognize using models built for isolated keystrokes.",
  "doi": "10.1109/icpads63350.2024.00018",
  "volume": "",
  "issue": "",
  "pages": "60-67",
  "source_url": "https://doi.org/10.1109/icpads63350.2024.00018",
  "status": "Published",
  "slug": "chameleon",
  "short_title": "Chameleon",
  "url_pdf": "/papers/2024-chameleon.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "Original project: static/uploads/Chameleon.pdf",
  "cover": "/research/chameleon.png",
  "cover_alt": "Research illustration for Chameleon",
  "cover_caption": "Illustration from the authors’ research paper.",
  "featured": false,
  "overview_source": "/papers/2024-chameleon.pdf"
}

Recognizing isolated keystrokes does not directly solve the harder case in which two signals overlap or the recording environment changes. Chameleon uses a lightweight Ranking Model to separate overlapping inputs. It also uses Fréchet Inception Distance to measure distribution changes and an Inductive Vector to adapt the recognition model to different phone positions, users, and environments.

The paper evaluates signal separation and adaptation separately, reporting 92.69% average recognition accuracy on separated signals. Its broader contribution is to connect separation and model adaptation in one workflow, addressing both simultaneous inputs and shifts in the conditions under which keystrokes are recorded.
