---
title: "FISTA-Net: Learning a Fast Iterative Shrinkage Thresholding Network for Inverse Problems in Imaging"
authors:
- <strong>Jinxi Xiang<strong>
- Yonggui Dong
- Yunjie Yang
# author_notes:
# - "Equal contribution"
# - "Equal contribution"
date: "2021-05-01T00:00:00Z"
doi: "10.1109/TMI.2021.3054167"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-05-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Medical Imaging, 2021"
publication_short: "TMI"

abstract: Inverse problems are essential to imaging applications. In this paper, we propose a model-based deep learning network, named FISTA-Net, by combining the merits of interpretability and generality of the model-based Fast Iterative Shrinkage/Thresholding Algorithm (FISTA) and strong regularization and tuning-free advantages of the data-driven neural network. By unfolding the FISTA into a deep network, the architecture of FISTA-Net consists of multiple gradient descent, proximal mapping, and {momentum modules} in cascade. Different from FISTA, the gradient matrix in FISTA-Net can be updated during iteration, and a proximal operator network is developed for nonlinear thresholding, which can be learned through end-to-end training. Key parameters of FISTA-Net, including the gradient step size, thresholding value, and momentum scalar, are tuning-free and learned from training data rather than hand-crafted. We further impose positive and monotonous constraints on these parameters to ensure they converge properly. The experimental results, evaluated both visually and quantitatively, show that the FISTA-Net can optimize parameters for different imaging tasks, i.e. Electromagnetic Tomography (EMT) and X-ray Computational Tomography (X-ray CT). It outperforms the state-of-the-art model-based and deep learning methods and exhibits good generalization ability over other competitive learning-based approaches under different noise levels.

# Summary. An optional shortened abstract.
summary: IEEE Transactions on Medical Imaging, 2021


tags:
- Source Themes
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9335299
url_code: 'https://github.com/jinxixiang/FISTA-Net'
# url_dataset: ''
# url_poster: ''
# url_project: ''
# url_slides: ''
# url_source: ''
# url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'The overall architecture of the proposed FISTA-Net.'
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
