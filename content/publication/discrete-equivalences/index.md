---
title: Modeling and Fabrication with Specified Discrete Equivalence Classes
publication_types:
  - "2"
# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Zhongyuan Liu
  - zz
  - Di Zhang
  - ChunyangYe
  - LigangLiu
  - XiaomingFu

# Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'

# # Schedule page publish date (NOT publication's date).
# publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
# publication_types: ['2']

doi: 10.1145/3450626.3459843

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics 2021*
publication_short: In *SIGGRAPH 2021*

# Summary. An optional shortened abstract.
summary: We propose a novel method to model and fabricate shapes using a small set of specified discrete equivalence classes of triangles. The core of our modeling technique is a fabrication-error-driven remeshing algorithm.

abstract: 'We propose a novel method to model and fabricate shapes using a small set of specified discrete equivalence classes of triangles. The core of our modeling technique is a fabrication-error-driven remeshing algorithm. Given a triangle and a template triangle, which are coplanar and have one-to-one corresponding vertices, we define their similarity error from a manufacturing point of view as follows: the minimizer of the maximum of the three distances between the corresponding pair of vertices concerning a rigid transformation. To compute the similarity error, we convert it into an easy-to-compute form. Then, a greedy remeshing method is developed to optimize the topology and geometry of the input mesh to minimize the fabrication error defined as the maximum similarity error of all triangles. Besides, constraints are enforced to ensure the similarity between input and output shapes and the smoothness of the resulting shapes. Since the fabrication error has been considered during the modeling process, the fabrication process is easy to proceed. To assist users in performing fabrication using common materials and tools manually, we present a straightforward manufacturing solution. The feasibility and practicability of our method are demonstrated over various examples, including seven physical manufacturing models with only nine template triangles.'

tags:
  - computational design
  - fabrication
  - discrete equivalence classes
  - constrained remeshing

# Display this page in the Featured widget?
featured: false
draft: false

# Custom links (uncomment lines below)
links:
- name: Supplements
  url: discrete-equivalences-Supp.pdf
  
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://www.bilibili.com/video/BV1MP4y1a7t5/'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  filename: discrete-equivalences.png # specify for shortcut
  focal_point: Smart
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

date: 2021-07-19T07:00:00.000Z
---

<!-- {{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}} -->
