---
title: "Chameleon: An Adaptive System for Overlapping Keystroke Signal Separation and Identification"
date: 2024-12-01
featured: false
tags: ["keystroke dynamics", "signal separation", "adaptive system", "ICPADS"]
categories: ["paper"]
image:
  filename: image.png
  focal_point: Smart
  preview_only: false
---

Congratulations to Jiayi Zhao, Yongzhi Huang, Qipeng Xie, Weizheng Wang, Lu Wang, and Kaishun Wu for their paper accepted to ICPADS 2024!

<!--more-->

## ABSTRACT

Keystroke dynamics has proven to be highly effective, with its applications expanding significantly over the years in areas such as preventing transaction fraud, account takeovers, and identity theft. Key-positioning and feature-learning methods are commonly used to identify keystroke signals. However, the existing methods face challenges in detecting overlapping keystrokes and environmentally changed signals. We propose a solution called Chameleon to address these limitations. Unlike previous signal separation and deep learning methods that are ineffective in keystroke signals and computationally demanding, Chameleon employs a low-computation Ranking Model to separate overlapping keystroke signals. Moreover, our experiments demonstrate that Chameleon separated signals can be recognized with an average accuracy of 92.69%, surpassing the commonly used FastICA method, which only reaches 25% accuracy. To account for environmental changes, we utilize the Fréchet Inception Distance (FID) as a guiding metric for model migration. Additionally, we introduce the Inductive Vector, which enables our key-identifying model to adapt to altered environmental conditions such as environment, phone location, and user variety. The Inductive Vector adjusts the model parameters based on the shift in FID. In scenarios with various phone locations, the Inductive Vector significantly improves recognition accuracy from 61% to 98%, outperforming the best existing keystroke recognition algorithm. In other dynamic environmental conditions, our approach achieves an average accuracy rate of 81.7%, which is at least 1.6 times better than the current state-of-the-art keystroke recognition algorithm.

[PDF Download](/uploads/Chameleon.pdf)