{
  "title": "Parameter-Transfer Learning for Low-Resource Individualization of Head-Related Transfer Functions",
  "date": "2019-09-15",
  "date_precision": 3,
  "authors": [
    "Xiaoke Qi",
    "Lu Wang"
  ],
  "publication": "Interspeech 2019",
  "venue_short": "Interspeech",
  "publication_kind": "Conference",
  "topic": "interaction",
  "summary": "利用参数迁移，在有限个体数据下实现头相关传递函数（HRTF）的个性化，降低大量测量难以开展时的空间音频适配门槛。",
  "doi": "10.21437/interspeech.2019-2558",
  "volume": "",
  "issue": "",
  "pages": "3865-3869",
  "source_url": "https://doi.org/10.21437/interspeech.2019-2558",
  "status": "Published",
  "slug": "hrtf-transfer",
  "short_title": "Parameter-Transfer Learning for Low-Resource Individualization of Head-Related Transfer Functions",
  "url_pdf": "/papers/2019-hrtf-transfer.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/Parameter-Transfer.pdf",
  "featured": false,
  "overview_source": "/papers/2019-hrtf-transfer.pdf"
}

完整测量个体头相关传递函数需要较高成本。参数迁移学习先在已有 HRTF 数据库上训练通用神经模型，利用声学知识设计输入特征和损失函数，再用目标听者的少量测量调整指定模型参数。

研究通过客观频谱距离及主观声源定位实验评估个性化结果。其贡献是结合物理声学知识与学习方法，在有限个体校准数据下实现跨听者模型迁移，服务于空间音频个性化。
