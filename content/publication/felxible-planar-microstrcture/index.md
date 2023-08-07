---
title: Computational Design of Flexible Planar Microstructures
publication_types:
  - "2"
authors:
  - zz 
  - Christopher Brandt
  - Jean Jouve
  - Yue Wang
  - Tian Chen
  - MarkPauly
  - Julian
date: 2023-08-04T00:00:00.000Z
# doi: 10.1109/TVCG.2021.3106433

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics 2023*
publication_short: In *SIGGRAPH Aisa 2023*

summary: We make an initial step on developing algorithms to accelerate homogenization and metamaterial design for nonlinear elasticity and building a complete framework for the optimal design of planar metamaterials.

abstract: "Mechanical metamaterials enable customizing the elastic properties of physical objects by altering their fine-scale structure. A broad gamut of effective material properties can be produced even from a single fabrication material by optimizing the geometry of a periodic microstructure tiling. Past work has extensively studied the capabilities of microstructures in the small-displacement regime, where periodic homogenization of linear elasticity yields computationally efficient optimal design algorithms. However, many applications involve flexible structures undergoing large deformations for which the accuracy of linear elasticity rapidly deteriorates due to geometric nonlinearities. Design of microstructures at finite strains involves a massive increase in computation and is much less explored; no computational tool yet exists to design metamaterials emulating target hyperelastic laws over finite regions of strain space. \n\nWe make an initial step in this direction, developing algorithms to accelerate homogenization and metamaterial design for nonlinear elasticity and building a complete framework for the optimal design of planar metamaterials. Our nonlinear homogenization method works by efficiently constructing an accurate interpolant of a microstructure’s deformation over a finite space of macroscopic strains likely to be endured by the metamaterial. From this interpolant, the homogenized energy density, stress, and tangent elasticity tensor describing the microstructure’s effective properties can be inexpensively computed at any strain. Our design tool then fits the effective material properties to a target constitutive law over a region of strain space using a parametric shape optimization approach, producing a directly manufacturable geometry. We systematically test our framework by designing a catalog of materials fitting isotropic Hooke’s laws as closely as possible. We demonstrate significantly improved accuracy over traditional linear metamaterial design techniques by fabricating and testing physical prototypes."

tags:
  - metamaterials
  - homogenization
  - physics-based simulation
  - computational design
  - fabrication


draft: false
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  filename: felxible-planar-microstrcture.png # specify for shortcut
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
---

<!-- {{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}} -->