---
title: "Automatic Diagnosis and Grading of Prostate Cancer with Weakly Supervised Learning on Whole Slide Images"

authors:
- Jinxi Xiang
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
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://pdf.sciencedirectassets.com/271150/1-s2.0-S0010482522X00127/1-s2.0-S0010482522010484/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJGMEQCIBntjL2Xk54QzlRkk7NS5BkJ32%2BFDaQ6aBRUenL5GHpcAiAbI0ys8q4muejbkL5XSPjeoZ0VbpPo772ZHE5zIdSydCqyBQhsEAUaDDA1OTAwMzU0Njg2NSIM8oV9mfAaTIroa1s6Ko8F9%2BQY2LKJTDMMErftvycYd78dIJGLJuYDOAzkkEVjWqjatAcc8UL%2BnC2Jess0DIBGGwJbi%2F6XYkhbyZNZJm9gzD5mbJcsECQHY2Ju0nm77aLcxzu%2FCuSOFYGu83VGUkxvGOH8kotNlrI0hbiWrOh4nGT%2BN3fF61ZHtP%2FTx8x4k16aSeyfFsDKvuCHXZDiCUs1dPE4XTNFVsiXY9ScwqVGOQ0Xbb0eUiPzJzuykCYxwmMdaoLrX9%2BVjgnj776RWDzUm2O6%2B2klG2W0iXWY8ncLNXaObrVGAIq%2BZiCNuOsdF1XQvQOvDq9krPePjYKd69cGEP6VranW%2BVCCEk1d5jzPXjal29wRsRboFH%2BNHH0xWDZUenuvXC1S9i9Fam5mL6sAfK%2B1FL32iJvo0F%2F8Ys%2BsTHtgYpDalmEzxp%2Bo3c12lYCMP%2FDUlI4o7JuTM4nBvHqYKwGSudGfOXWZJvn3pGwJ6ILcIdsXyOmQjh9P7O4X3Kfd9JHQBdpAL14IffmRyThJoZJQfAqgx%2Bk4TpOPa6MX8xGFUcEqtG6wr0xUvLYtABOVxDbEHGY5BAXjR%2BhBM%2BruED30oytRDEM5mFAowkHRyxLKkIE7fmC4CuZb6EYh0NbRdiMU%2FB7b%2BxvSrzosyoIuYtP4XChRQwXThMHOAexTpl4ztJZ%2BXmUFoaE0KeBVRd3tVw8a5p8VN2RiO8Cpmaij5WqYSD80RctoFJ6Eu12k9sEQA9uULK09zYBS2uecGq4Pow1Pf3zMn6KTogeGEJ6S%2F8kopx%2FlT44fWvFUIuGCaVg%2FdmTZOCtVhtZe0O%2BhuWhue0E5dtEjpVAwZIdF%2FU4Oy%2F6M6ZhwrjFDvwWknZMEslUeHB8SCMAh2aT0tGyrMTDw2%2BewBjqyAYQBUC1CkfW3bSC%2FeuYSL42%2BO2%2Fujj5Q2%2FD5yh6GEmDxyrIccjz8s9UWcCNvnTRd7K65zX6z2w6FmyEqDINBXCArcisheKWWS52b56LtH36AP4kW6%2BRs9Fv65HZQoqNUBQK7uzsTqqHco7S%2BT8xgV2xUEL43%2FlrlSqrPzd0yrUn2HL0UV%2FMKNISFS2afNnHnEiI9Fp3zH98m7jMWPfMYXAgGEe9RIlNUOo6qoWHtWYkCAcc%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240413T033603Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSYLRG4UA%2F20240413%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=260cf7ccabf8c0988a91222e8554dc4a65dd683f98531e0cad17af0e4e035fbc&hash=ad09717d47da7aee57df93e1868ee912c090466a8c8003f610598175132e67b4&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0010482522010484&tid=spdf-629c49e1-1e6b-42f7-8dba-6ba530196762&sid=38ea6a8e6ada2542a88bd0e0b59c35d4adb0gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=13155856525959560001&rr=873868ded883ce50&cc=us
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

<!-- {{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}} -->

<!-- Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
