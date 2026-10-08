{
  "title": "InFit: Combination Movement Recognition For Intensive Fitness Assistant Via Wi-Fi",
  "date": "2023-12-01",
  "date_precision": 2,
  "authors": [
    "Huichuwu Li",
    "Jiang Xiao",
    "Wei Wang",
    "Lu Wang",
    "Dian Zhang",
    "Hai Jin"
  ],
  "publication": "IEEE Transactions on Mobile Computing",
  "venue_short": "TMC",
  "publication_kind": "Journal",
  "topic": "sensing",
  "summary": "InFit recognizes combinations of fitness movements from Wi-Fi signals. It addresses continuous exercises whose component movements are concatenated or interleaved, extending recognition beyond isolated repetitions.",
  "doi": "10.1109/tmc.2022.3209656",
  "volume": "22",
  "issue": "12",
  "pages": "7188-7202",
  "source_url": "https://doi.org/10.1109/tmc.2022.3209656",
  "status": "Published",
  "slug": "infit",
  "short_title": "InFit",
  "url_pdf": "/papers/2023-infit.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/InFit-%20Combination%20Movement%20Recognition%20For%20Intensive%20Fitness%20Assistant%20Via%20Wi-Fi.pdf",
  "featured": false,
  "overview_source": "/papers/2023-infit.pdf"
}

Combination exercises concatenate or interleave simpler movements, creating many more patterns than isolated repetitions. InFit uses Stitching-based Virtual Sample Generation to synthesize training examples and reduce the cost of collecting every combination. A two-stage recognition model learns temporal dependencies and decomposes a sequence into its component movements.

Experiments report 94% average recognition accuracy and examine the setting with no collected combination-training samples. The system contributes both a data-augmentation method and a recognition pipeline for assessing continuous exercise rather than merely counting repeated isolated actions.
