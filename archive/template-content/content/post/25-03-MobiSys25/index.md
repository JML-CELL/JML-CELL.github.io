---
title: "PIT: A Novel Toothbrush Providing Real-Time and Robust Plaque Indication During Brushing"
date: 2025-03-01
featured: false
tags: ["mobile sensing", "healthcare", "MobiSys"]
categories: ["paper"]
image:
  filename: featured.jpg
  focal_point: Smart
  preview_only: false
---

Congratulations to Kaixin Chen, Junfan Xiang, Wanying Tan, Keyu Chen, Yaqiong Luo, Chang Ma, Kaishun Wu, and Lu Wang for their paper accepted to MobiSys 2025!

<!--more-->

## ABSTRACT

The dental plaque disclosing agent helps guide plaque removal by revealing plaque on the teeth. However, existing toothbrushes cannot provide visualization of the stained plaque beneath the toothpaste foam during brushing. To fill this gap, this paper proposes PIT and uses smartphone to provide real-time plaque visualization during brushing. PIT introduces novel hardware, including a micro camera, four green LEDs, and a mechanical structure, offering a stable camera view of bristle position and bristle rotation. To address the challenge of toothpaste foam obstruction, we derived an optical channel model that guided the design of the light source to enhance plaque visibility. Furthermore, we designed a deep neural network specifically for plaque segmentation under thick foam. Finally, the trained distilled student model was run on a smartphone and evaluated on both denture models and human subjects. The results show that PIT achieved an IoU (Intersection over Union) of 75.22% and a latency of 29 ms, with robust performance across various conditions. Evaluation by 10 participants revealed that PIT helped reduce plaque coverage to 5.6% within two minutes of brushing, significantly outperforming existing advanced toothbrushes.

[PDF Download](/uploads/PiT_Mosiy2025.pdf)