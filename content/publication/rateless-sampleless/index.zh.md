{
  "title": "From rateless to sampleless: Wi-Fi connectivity made energy efficient",
  "date": "2016-04-01",
  "date_precision": 2,
  "authors": [
    "Wei Wang",
    "Yingjie Chen",
    "Lu Wang",
    "Qian Zhang"
  ],
  "publication": "IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications",
  "venue_short": "INFOCOM",
  "publication_kind": "Conference",
  "topic": "wireless",
  "summary": "通过降低采样率减少 Wi-Fi 接收机的能耗，利用多次重传之间的冗余，恢复单次欠采样接收时无法解码的数据包。",
  "doi": "10.1109/infocom.2016.7524424",
  "volume": "",
  "issue": "",
  "pages": "1-9",
  "source_url": "https://doi.org/10.1109/infocom.2016.7524424",
  "status": "Published",
  "slug": "rateless-sampleless",
  "short_title": "From rateless to sampleless",
  "url_pdf": "/papers/2016-rateless-sampleless.pdf",
  "pdf_label": "Read PDF",
  "pdf_source": "https://luwang-szu.github.io/paper/From_rateless_to_sampleless_Wi-Fi_connectivity_made_energy_efficient.pdf",
  "featured": false,
  "overview_source": "/papers/2016-rateless-sampleless.pdf"
}

对于通信负载较轻的设备，高 Wi-Fi 采样率可能浪费能量。Sampleless Wi-Fi 借鉴无速率编码思想，跨多次重传累积信息以恢复低采样率接收的数据包，并利用接收端时间偏移产生星座分集，无需改变标准数据包格式。

研究通过 GNU Radio/USRP 实验和真实 Wi-Fi 轨迹，与降频方法比较解码表现和能耗效率。这篇会议论文展示如何把重传冗余转化为低能耗接收资源，同时保持数据包兼容性。
