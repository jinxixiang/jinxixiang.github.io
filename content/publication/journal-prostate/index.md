---
title: "Automatic Diagnosis and Grading of Prostate Cancer with Weakly Supervised Learning on Whole Slide Images"

authors:
- admin
- Xiyue Wang
- Xinran Wang
- Jun Zhang
- Sen Yang
- Wei Yang
- Xiao Han
- Yueping Liu

author_notes:
- "Equal contribution"
- "Equal contribution"

date: "2023-01-01T00:00:00Z"
doi: "10.1016/j.compbiomed.2022.106340"

# Schedule page publish date (NOT publication's date).
publishDate: "2023-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Computers in Biology and Medicine, 2023"
publication_short: "CIBM"

abstract: Background. Prostate cancer diagnosis and grading workflow is cumbersome, and the results suffer from substantial inter-observer variability.  Recent trials have shown potential in using machine learning to develop automated systems to address this challenge. Most automated deep learning systems for prostate cancer Gleason grading focused on supervised learning requiring demanding fine-grained pixel-level annotations. Methods  A weakly supervised deep learning model with slide-level labels is presented in this study for diagnosing and grading prostate cancer with whole slide images (WSI). WSIs are first cropped into small patches and then processed with a deep-learning model to extract patch-level features. A graph convolution network (GCN) aggregates the features for classifications. The noisy labels are progressively filtered out throughout the training process to reduce inter-observer variations in clinical reports. Finally, multi-center independent test cohorts \textcolor{red}{with 6,174 slides are collected to evaluate the prostate cancer diagnosis and grading performance of our model.  Results  The cancer diagnosis (2-level classification) results on two external test sets (n=4,675, n=844) show an area under the receiver operating characteristic curve (AUC) of 0.985 and 0.986. The results of the Gleason grading (6-level classification) reach 0.931 quadratic weighted kappa on the internal test set (n=531). It generalizes well} on the external test dataset (n=844) with an independent 0.801 quadratic weighted kappa with the reference standard set. The model enables pathological meaningful interpretability by visualizing the most attended lesions, which are highly consistent with expert annotations. Conclusion The proposed model incorporates a graph network in weakly supervised learning with only slide-level reports. A robust learning strategy is also employed to correct the label noise. It is highly accurate $>0.985$ AUC for diagnosis) and also interpretable with intuitive heatmap visualization. It can be unified with a digital pathology pipeline to deliver prostate cancer metrics for a pathology report.

# Summary. An optional shortened abstract.
summary: Computers in Biology and Medicine, 2023


tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/pii/S0010482522010484
# url_code: 'https://github.com/jinxixiang/FISTA-Net'
# url_dataset: ''
# url_poster: ''
# url_project: ''
# url_slides: ''
# url_source: ''
# url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'The workflow of automated prostate cancer diagnosis and grading system'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

<!-- Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
