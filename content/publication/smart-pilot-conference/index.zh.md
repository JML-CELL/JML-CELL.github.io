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
  "summary": "Smart Pilot 利用更丰富的当前信道信息调整无线传输速率，应对快速变化及频率选择性信道对传统速率估计的影响。",
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

当信道变化时，仅凭少量已知符号获得的信道估计可能不再准确。Smart Pilot 从物理层解码器及上层协议头提取额外可靠信息，将这些比特用作参考，以较少额外信令校准 CSI。

贪心速率选择算法进一步利用校准后的子载波信息。GNU Radio 实验与轨迹驱动仿真考察信道跟踪和速率预测，贡献了跨层获取信道知识的方法，支持更快速、细粒度的无线自适应。
