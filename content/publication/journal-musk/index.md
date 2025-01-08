---
title: "A Vision–language Foundation Model for Precision Oncology"
authors:
- Jinxi Xiang
- Xiyue wang
- Xiaoming Zhang  
- Yinghua Xi  
- Feyisope Eweje  
- Yijiang Chen  
- Yuchen Li  
- Colin Bergstrom  
- Matthew Gopaulchan  
- Ted Kim  
- Kun-Hsing Yu  
- Sierra Willens  
- Francesca Maria Olguin  
- Jeffrey J. Nirschl  
- Joel Neal  
- Maximilian Diehn  
- Sen Yang  
- Ruijiang Li  

author_notes:
- Equal contribution
- Equal contribution
- 
-   
-  
-   
- 
- 
- 
- 
- 
- 
- 
- 
-  
- 
- Corresponding author
- Corresponding author & Lead contact



date: "2025-01-08T00:00:00Z"
doi: "10.1038/s41586-024-08378-w"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-08T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Nature, 2025"
publication_short: "Nature"

abstract: Clinical decision-making is driven by multimodal data, including clinical notes and pathological characteristics. Artificial intelligence approaches that can effectively integrate multimodal data hold significant promise in advancing clinical care1,2. However, the scarcity of well-annotated multimodal datasets in clinical settings has hindered the development of useful models. In this study, we developed the Multimodal transformer with Unified maSKed modeling (MUSK), a vision–language foundation model designed to leverage large-scale, unlabelled, unpaired image and text data. MUSK was pretrained on 50 million pathology images from 11,577 patients and one billion pathology-related text tokens using unified masked modelling. It was further pretrained on one million pathology image–text pairs to efficiently align the vision and language features. With minimal or no further training, MUSK was tested in a wide range of applications and demonstrated superior performance across 23 patch-level and slide-level benchmarks, including image-to-text and text-to-image retrieval, visual question answering, image classification and molecular biomarker prediction. Furthermore, MUSK showed strong performance in outcome prediction, including melanoma relapse prediction, pan-cancer prognosis prediction and immunotherapy response prediction in lung and gastro-oesophageal cancers. MUSK effectively combined complementary information from pathology images and clinical reports and could potentially improve diagnosis and precision in cancer therapy.

1️⃣ Conceptual Advance: By leveraging the complementary information between images 🖼️ and clinical reports 📝, the hashtag#MultiModalAI approach achieved superior outcome prediction over either modality alone.

2️⃣ Translational Advance: We demonstrate that multi-modal hashtag#FoundationModels can achieve promising performance for predicting clinical outcomes, including relapse, prognosis, and immunotherapy response. 🔄📈

3️⃣ Technical Advance: We developed MUSK using unified masked modeling to harness unpaired data for pretraining and employed pathology-specific adaptations, including multiscale image processing, staining augmentation, bootstrap filtering, and fine-grained alignment.

# Summary. An optional shortened abstract.
summary: Nature, 2025


tags:
- Source Themes
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: 'https://www.nature.com/articles/s41586-024-08378-w'
url_code: 'https://github.com/lilab-stanford/MUSK'
# url_dataset: ''
# url_poster: ''
# url_project: ''
# url_slides: ''
url_source: 'https://huggingface.co/xiangjx/musk'
# url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Data curation, model development and evaluation.'
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
