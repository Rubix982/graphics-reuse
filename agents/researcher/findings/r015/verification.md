# R-015 · What was checked against primary sources, and where the source files are

_2026-11-14, by the orchestrator, after the four agents finished. The agents read many pages through WebFetch, which returns a model's extract rather than the raw text, so the claims the card's result rests on were re-checked here: in the raw arXiv HTML, the raw GitHub files, or the papers' own text (pdftotext extracts of the PDFs the agents downloaded). Two-column PDFs interleave their columns in the extracts, so a quote can appear split by text from the other column; it was counted as found when both halves were present in order._

## Checked, and found as quoted

| Claim | Source checked | How |
|---|---|---|
| GarmentCodeData: "If a small enough percentage of mesh vertices (1.5%) change their location between the frames by a magnitude greater than a specified threshold (0.04 cm), the mesh is considered static." | arxiv.org/html/2405.17609v3 | raw HTML, maths alt-text restored |
| Dress-1-to-3: "To make the simulation as path-independent as possible, we avoid adding friction during the process." | arxiv.org/html/2502.03449 | raw HTML |
| Dress-1-to-3: "The garment optimization process can be finished within 2 hours on a single RTX 3090 with 24GB device memory." | arxiv.org/html/2502.03449 | raw HTML |
| Dress-1-to-3: "Since the static equilibrium does not locally depend on the initial state, meaning that the Jacobian matrix of the simulated state with respect to the initial state is zero …" | the paper's text (li2025-dress-1-to-3.txt) | interleaved, both halves present |
| HOOD is MIT-licensed | raw.githubusercontent.com/dolorousrtur/hood/main/LICENSE | "MIT License, Copyright (c) 2023 Artur Grigorev" |
| Newton: "OS: Linux (x86-64, aarch64), Windows (x86-64), or macOS (CPU only)" | raw README, newton-physics/newton | raw file |
| Warp: "Currently, kernels launched on CPU devices will be executed in serial." | nvidia.github.io/warp, runtime guide (v1.13–v1.19, stable, latest) | web search of the exact phrase |
| Wang 2018: "after M inexact outer iterations, e.g., M = 32, we run one exact outer iteration with sufficient simulation accuracy" | wang2018-rule-free-sewing-pattern-adjustment.txt | interleaved |
| Wang 2018: "…to ignore cloth-body friction and self collision of cloth. We believe it is a reasonable assumption … to drape naturally and relaxedly into a unique configuration"; "ignoring self collision does not prevent the system from handling multi-layered garments … as long as self collision does not greatly affect the draped garment shape" | same | interleaved |
| Wang 2018: "While we prefer the quasistatic state to be unique, it is often not" | same | found |
| Sensitive Couture: "Buckling, wrinkling, and static friction all make for a nonlinear relation between the 2D design and the 3D drape" | umetani2011-sensitive-couture.txt | interleaved |
| DiffCloth: "adding or deleting nodes in the contact set creates frequent and the most severe discontinuities" | li2022-diffcloth.txt | interleaved |
| DiffAvatar: "14-core i7 CPU with 32GB RAM"; "Optimization takes about one minute per iteration and total times vary between 20 to 200 minutes" | li2024-diffavatar.txt | interleaved |
| OGC: "…but cloth-cloth penetration is prevented" (body-cloth penetration may occur with a skeleton-driven body) | chen2025-offset-geometric-contact.txt | found |
| Tang et al. 2024: transmission "can no longer be estimated from a single image; both the reflection and transmission images are needed" | tang2024-woven-fabric-capture.txt | interleaved |

## Not checked here

Every other number in the four area files: speedups, timings, candidate counts, licence and CUDA verdicts for the remaining candidates, and HOOD's third-party CPU timing (an Arm blog post). Re-check each against its source before it goes into an entry, as R-013's rule asks for a full reading anyway.

## A change made to the agents' files

One phrase describing the test bed's photos was made generic ("reference photo") in five places (d-rendering.md four, c-differentiable-fitting.md one). The test bed is private, and the phrase said more about it than the library needs. Nothing else in the agents' files was edited.

## Where the downloaded sources are (git-ignored)

The agents downloaded papers and pages into the session's scratchpad. They were moved into `sources/` (git-ignored, like `sources/brouet2012.pdf`), so they survive the session and stay out of the public repo:

- `sources/r015/papers/`: 18 papers, each as PDF and as a pdftotext extract: chang2023-parameter-space-restir, chen2025-offset-geometric-contact, chinchuthakun2025-diffusionlight-turbo, careaga2024-colorful-diffuse-intrinsic, korosteleva2024-garmentcodedata, li2022-diffcloth, li2024-diffavatar, li2025-dress-1-to-3, lu2025-domain-decomposed-projective-dynamics, lu2025-fast-galerkin-multigrid, soh2024-neural-appearance-model-cloth, tang2024-woven-fabric-capture, umetani2011-sensitive-couture, wang2018-rule-free-sewing-pattern-adjustment, xu2024-residual-path-integrals, yang2026-periodic-anderson-acceleration, yu2024-inverse-garment-pattern-modeling, zhang2022-progressive-cloth-quasistatics.
- `sources/r015/pages/`: the pages behind specific claims. `blender-manual/` (Blender 4.5 manual pages: Light Groups and passes, performance and sampling settings, glTF exporter, sheen and translucent BSDFs, a release note), `newton-src/` (Newton's VBD and Style3D solver sources and cloth examples), `ppf-docs/` (ppf-contact-solver's README and docs on performance, penetration and criticism), `genesis-src/` (Genesis's PBD solver), `github-repo-metadata/` (GitHub API metadata and READMEs for the learned-cloth repos), `arxiv-queries/` (area A's raw arXiv API results and the script that parsed them).
- `sources/tamstorf2015.pdf`: Tamstorf, Jones and McCormick 2015, downloaded earlier for the coarse-to-fine entry.

## Left out, on purpose

- The source code the agents downloaded to read (HOOD, ContourCraft, ClothTransformer, as zip archives). It is third-party code, and the area files cite each repository and the files read; fetch it again from GitHub to re-check.
- One PDF that downloaded corrupt (`sig23cloth.pdf`, unreadable).
- The agents' full transcripts. They are large, and the briefs inside them describe the private test bed. Their final replies are in `agent-reports.md`, and the briefs in `private/r015-briefs.md`.
