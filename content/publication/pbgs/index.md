---
title: Position-Based Nonlinear Gauss-Seidel for Quasistatic Hyperelasticity

authors:
  - Yizhou Chen
  - YushanHan
  - JingyuChen
  - zz 
  - Alex Mcadams
  - Joey

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types:
  - "2"
date: 2024-07-19T00:00:00.000Z
doi: 10.1145/3658154

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics 2024*
publication_short: In *SIGGRAPH 2024*

summary: We show that a position-based, rather than constraint-based nonlinear Gauss-Seidel approach resolves a number of issues with PBD, particularly in the quasistatic setting. Our approach retains the essential PBD feature of stable behavior with constrained computational budgets, but also allows for convergent behavior with expanded budgets.

abstract: "Position based dynamics is a powerful technique for simulating a variety of materials. Its primary strength is its robustness when run with limited computational budget. Even though PBD is based on the projection of static constraints, it does not work well for quasistatic problems. This is particularly relevant since the efficient creation of large data sets of plausible, but not necessarily accurate elastic equilibria is of increasing importance with the emergence of quasistatic neural networks. Recent work has shown that PBD can be related to the Gauss-Seidel approximation of a Lagrange multiplier formulation of backward Euler time stepping, where each constraint is solved/projected independently of the others in an iterative fashion. We show that a position-based, rather than constraint-based nonlinear Gauss-Seidel approach resolves a number of issues with PBD, particularly in the quasistatic setting. Our approach retains the essential PBD feature of stable behavior with constrained computational budgets, but also allows for convergent behavior with expanded budgets. We demonstrate the efficacy of our method on a variety of representative hyperelastic problems and show that both successive over relaxation (SOR), Chebyshev and multiresolution-based acceleration can be easily applied."

tags:
  - elasticity 
  - physics-based simulation

draft: false
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Supplements
#   url: flexible_planar_microstructures_supplement.pdf

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
  filename: pbgs.png # specify for shortcut
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