# R-012 · Every paper looked at, in shuffled order

_Sorted 2026-11-14 by the orchestrator from each abstract, by `procedure.md`. Abstract sources: `abstracts.jsonl`. "Reason" quotes the abstract. Axis abbreviations: time, space, runs, res (resolutions), shapes, many (many instances). `changes` is `reuse_changes`: cost (cost only), answer (the answer), depends._

## A decision made during sorting

The procedure didn't say whether one kind of saving counts as reuse: **an identical intermediate term computed once and shared within one evaluation** (common subexpressions). Rank 1 shares edge terms between the tetrahedra around each edge "to avoid redundant computation"; rank 52 (D*) eliminates common subexpressions in derivative graphs. The library's premise calls exact repeats and memoization reuse ("the easy case"), but none of the six axes has a place for them: the axes all describe near-repeats along some dimension. Rank 1 fits "across space" only by the letter of procedure step 6 ("neighbouring … elements"); rank 52 has no neighbours at all. Rather than settle it after seeing the data, both readings are reported:

- **strict:** they are reuse, and misfits (no axis);
- **lenient:** they are outside the library's scope (not reuse), and the sample runs on until 20 other reuse papers are found.

Also decided during sorting, from the axes' own examples in README.md: hierarchical approximation (Barnes–Hut, fast multipole) is a faster algorithm, not reuse (procedure step 7). A precomputation per scene or asset that is reused across changing inputs is "across many instances", as precomputed radiance transfer is in the README. "Across runs" is reserved for reusing the result of an earlier run, not a dedicated precomputation. Multigrid is "across resolutions", cost only, as in `entries/coarse-to-fine-cloth.md` (T-006).

## The list

| # | year | title | verdict | axis per mechanism · changes | reason (the abstract's words) |
|---|---|---|---|---|---|
| 1 | 2009 | An edge-based computationally efficient formulation of Saint Venant-Kirchhoff tetrahedral finite elements | **reuse, borderline** (strict: misfit; lenient: not reuse) | shared identical sub-terms within one evaluation · cost | "the data is associated with edges and tetrahedron-sharing edge-pairs … as opposed to tetrahedra, to avoid redundant computation" |
| 2 | 2016 | Position-normal distributions for efficient rendering of specular microstructure | not reuse | — | a new representation: "fit this distribution using millions of 4D Gaussians … closed-form solutions" |
| 3 | 2015 | Efficient and Accurate Spherical Kernel Integrals Using Isotropic Decomposition | not reuse | — | "decomposing spherical filters into a linear combination of simpler isotropic kernels" |
| 4 | 2019 | Blockwise Multi-Order Feature Regression for Real-Time Path-Tracing Reconstruction | not reuse | — | "The high speed is achieved with a fast implementation of augmented QR factorization and by using stochastic regularization" |
| 5 | 2017 | Real-time global illumination by precomputed local reconstruction from sparse radiance probes | **reuse, clean** | many · depends (exact while geometry is static); space · answer | "our precomputed local reconstruction operator" for "mostly static scenes"; "every receiver depends only on a small, constant number of nearby radiance probes" |
| 6 | 2025 | Artifact-Resilient Real-Time Holography | **reuse, clean** | many · answer | "train a real-time neural network-based phase generator" |
| 7 | 2009 | An efficient GPU-based approach for interactive global illumination | **reuse, clean** | space · answer | "The sampled irradiance values are then interpolated at all shading points … exploits the spatial coherence of illumination" |
| 8 | 2023 | MERF: Memory-Efficient Radiance Fields for Real-time View Synthesis in Unbounded Scenes | **reuse, clean** | many · cost | "a lossless procedure for baking the parameterization used during training into a model that achieves real-time rendering" |
| 9 | 2025 | Real-Time Knit Deformation and Rendering | not reuse | — | "solved through a GPU-based Gauss-Newton scheme for real-time performance"; "decomposition strategies" |
| 10 | 2025 | WATER: Watertight Tessellation for Real-Time Pixel-Accurate Rendering of Large-Scale Surfaces | not reuse | — | "a fully GPU-driven pipeline with cache-friendly design and novel algorithms" |
| 11 | 2006 | Efficient simulation of large bodies of water by coupling two and three dimensional techniques | not reuse | — | less work, nothing carried over: "coarsen the mesh away from the interface for efficiency" |
| 12 | 2020 | Fast and scalable turbulent flow simulation with two-way coupling | not reuse | — | a new kinetic solver, "highly parallelizable by nature" |
| 13 | 2025 | A Fast, Efficient, and Robust Feature Protected Denoising Method | not reuse | — | "solved by an explicit Euler method … requires no training samples" |
| 14 | 2016 | Sphere-meshes for real-time hand modeling and tracking | not reuse | — | "the limited number of primitives in the tracking template allows us to retain excellent computational performance" |
| 15 | 2024 | MiNNIE: a Mixed Multigrid Method for Real-time Simulation of Nonlinear Near-Incompressible Elastics | **reuse, clean** | res · cost | "a specially tailored GPU multigrid solver" |
| 16 | 2022 | Fast GPU-based Two-way Continuous Collision Handling | not reuse | — | a new algorithm that avoids "repetitive collision testing"; the previous intersection-free state is the usual anchor of collision handling, not a stated saving |
| 17 | 2021 | Fast linking numbers for topology verification of loopy structures | not reuse | — | "Barnes-Hut or fast multipole methods" (hierarchical approximation) |
| 18 | 2021 | Real-time deep dynamic characters | **reuse, clean** | many · answer | dynamics "in an efficient data-driven way, without requiring complex physics simulation" |
| 19 | 2021 | Fast evaluation of smooth distance constraints on co-dimensional geometry | not reuse | — | "a modified Barnes-Hut acceleration approach" |
| 20 | 2010 | Stable spaces for real-time clothing | **reuse, clean** | many · answer | "learning clothing models that enables the simultaneous animation of thousands of detailed garments in real-time" |
| 21 | 2014 | Continuous projection for fast L1 reconstruction | not reuse | — | "a novel continuous formulation … based on a Gaussian mixture describing the input point density" |
| 22 | 2008 | Real-time control of physically based simulations using gentle forces | not reuse | — | "made tractable in real-time by linearizing the system dynamics around the input trajectory"; the LQR gains are presumably computed ahead of time, but the abstract credits linearisation |
| 23 | 2024 | CharacterGen: Efficient 3D Character Generation from Single Images with Multi-View Pose Canonicalization | unclear (skipped) | — | the abstract doesn't say what makes it efficient beyond "a streamlined generation pipeline" |
| 24 | 2014 | The natural-constraint representation of the path space for efficient light transport simulation | not reuse | — | a new path representation and mutation strategy for better exploration |
| 25 | 2006 | Real-time GPU rendering of piecewise algebraic surfaces | no abstract (skipped) | — | — |
| 26 | 2008 | Efficient multiple scattering in hair using spherical harmonics | **reuse, clean** | space · answer | light paths contribute "power to a 3D grid of spherical harmonic coefficients that store the directional distribution of scattered radiance", then visible fibres integrate "the stored radiance" |
| 27 | 2023 | Adaptive Shells for Efficient Neural Radiance Field Rendering | not reuse | — | fewer samples: "In solid regions, the envelope … can often be rendered with a single sample" |
| 28 | 2006 | Fast Separation of Direct and Global Components of a Scene Using High Frequency Illumination | not reuse | — | fewer captured images, by a measurement method |
| 29 | 2025 | IMLS-Splatting: Efficient Mesh Reconstruction from Multi-view Images via Point Representation | not reuse | — | an efficient representation and pipeline |
| 30 | 2025 | A Highly-Efficient Hybrid Simulation System for Flight Controller Design and Evaluation of Unmanned Aerial Vehicles | not reuse | — | "hybrid modeling that … combines our novel far-field adaptive block-based fluid simulator with parametric empirical models" (model simplification) |
| 31 | 2011 | Physically-based real-time lens flare rendering | unclear (skipped) | — | "Various acceleration strategies", not described |
| 32 | 2025 | Creating Fluid-Interactive Virtual Agents by an Efficient Simulator with Local-domain Control | not reuse | — | less work: "improves efficiency by employing a slender domain" |
| 33 | 2023 | BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis | **reuse, clean** | many · answer | appearances "baked into static textures for efficient rasterization" |
| 34 | 2015 | Real-time pixel luminance optimization for dynamic multi-projection mapping | not reuse | — | "a real-time solution to this optimization problem using off-the-shelf graphics hardware" |
| 35 | 2009 | Real-time hand-tracking with a color glove | no abstract (skipped) | — | — |
| 36 | 2003 | Efficient synthesis of physically valid human motion | not reuse | — | "objective functions and constraints that lead to linear time analytical first derivatives" |
| 37 | 2019 | A scalable galerkin multigrid method for real-time simulation of deformable objects | **reuse, clean** | res · cost | "a simple yet efficient multigrid scheme" |
| 38 | 2009 | Real-time parallel hashing on the GPU | not reuse | — | "an efficient data-parallel algorithm for building large hash tables" |
| 39 | 2018 | Real-time High-accuracy Three-Dimensional Reconstruction with Consumer RGB-D Cameras | not reuse | — | GPU implementation; submap-based optimisation for scalability (decomposition, nothing carried over as a stated saving) |
| 40 | 2004 | Fast hierarchical importance sampling with blue noise properties | **reuse, clean** | many · answer | "Pre-computed correction vectors, obtained using relaxation, are used to improve the spectral characteristics of the sampling pattern" |
| 41 | 2016 | Real-time rendering on a power budget | **reuse, clean** | many · answer | "efficiently explore the vast power-error space and leverage optimal Pareto frontiers at runtime" |
| 42 | 2011 | GPU-efficient recursive filtering and summed-area tables | not reuse | — | memory traffic: "the image data is read only twice and written just once" |
| 43 | 2006 | Statistical acceleration for animated global illumination | **reuse, clean** | time · answer | "The variation of these noisy solutions over time is then used to create a smooth basis" |
| 44 | 2022 | Fast Octree Neighborhood Search for SPH Simulations | not reuse | — | "By permitting more comparisons than strictly necessary, the time spent on preparing and searching the acceleration structure can be reduced" |
| 45 | 2019 | Real-time pose and shape reconstruction of two interacting hands with a single depth camera | not reuse | — | "To achieve real-time rates … a highly efficient GPU-based Gauss-Newton optimizer" |
| 46 | 2024 | Area ReSTIR: Resampling for Real-Time Defocus and Antialiasing | **reuse, clean** | space · depends; time · depends | "sample reuse from neighbors"; "subpixel-tracking temporal reuse" |
| 47 | 2010 | PantaRay: fast ray-traced occlusion caching of massive scenes | **reuse, clean** | many · answer | "precomputing sparse directional occlusion caches … used for accelerating a fast cinematic lighting pipeline" |
| 48 | 2011 | Real-time large-deformation substructuring | **reuse, clean** | many · answer | "build a reduced deformable model for each domain … parts can be re-used and precomputation times shortened" |
| 49 | 2018 | Fast depth densification for occlusion-aware augmented reality | not reuse | — | propagates measured sparse depth; no computed result carried over |
| 50 | 2016 | Efficient GPU rendering of subdivision surfaces using adaptive quadtrees | **reuse, clean** | many · cost | "subdivide the u, v domain of each face ahead of time, generating a quadtree structure"; "accurately and efficiently evaluate the limit surface" |
| 51 | 2007 | Active learning for real-time motion controllers | not reuse | — | the contribution is fewer captured clips; the controller being real-time isn't the paper's saving |
| 52 | 2007 | Efficient symbolic differentiation for graphics applications | **reuse, borderline** (strict: misfit; lenient: not reuse) | shared identical sub-terms within one evaluation · cost | "symbolically executing the expression graph at compile time to eliminate common subexpressions" |
| 53 | 2004 | An intuitive framework for real-time freeform modeling | **reuse, clean** | many · cost | "real-time response … by precomputing a set of scalar-valued basis functions that correspond to the degrees of freedom of the manipulator" |
| 54 | 2008 | Fast animation of turbulence using energy transport and procedural synthesis | **reuse, clean** (lenient sample only) | res · answer | a coarse solve plus synthesised "subgrid-scale flow detail … an order of magnitude faster than full numerical simulation of equivalent resolution" |
| 55 | 2018 | Efficient palette-based decomposition and recoloring of images via RGBXY-space geometry | **reuse, clean** (lenient sample only) | many · answer | "After preprocessing, our algorithm can decompose 6 MP images into layers in 20 milliseconds" while the palette is edited; the main saving is a new geometric method (not reuse) |

The strict sample stops at rank 53, the 20th reuse paper counting ranks 1 and 52. The lenient sample stops at rank 55, the 20th without them. Ranks 56–60 were read in the same batch, but they come after both stopping points and are not counted.

## Counts

| | strict (ranks 1–53) | lenient (ranks 1–55) |
|---|---|---|
| papers looked at | 53 | 55 |
| no abstract / unclear (skipped) | 2 / 2 | 2 / 2 |
| judged | 49 | 51 |
| reuse | 20 (41 %) | 20 (39 %) |
| clean | **18** | **20** |
| misfit | 2 (ranks 1, 52: shared sub-terms, no axis) | 0 |

**Papers per axis** (a paper with two mechanisms counts on both):

| axis | strict | lenient |
|---|---|---|
| across many instances | 12 | 13 |
| across space | 4 | 4 |
| across resolutions | 2 | 3 |
| across time | 2 | 2 |
| across shapes | 0 | 0 |
| across runs | 0 | 0 |

**reuse_changes by mechanism** (22 mechanisms in 20 papers): strict, cost only 7 (including both borderline cases), the answer 12, depends 3; lenient, cost only 5, the answer 14, depends 3.
