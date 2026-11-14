# R-018 · The orchestrator's classification (the comparison, not the test)

_Written 2026-11-14 while the blind agent was running, before its result was seen. The orchestrator had read these abstracts in R-012 and wrote the classes and the bar after that, so this classification can't be the test; the blind one is. Classes as in CARD.md: (A) computed for this problem, (B) fitted to examples, (C) neither, both, unclear._

| # | class | what is reused | what makes it go stale | the abstract's words |
|---|---|---|---|---|
| 5 | A | a precomputed local reconstruction operator | the scene's geometry changing (lights, cameras and diffuse materials may vary) | "mostly static scenes … while supporting fully dynamic lights, cameras and diffuse surface materials" |
| 6 | B | a trained phase-generating network | inputs unlike its training | "train a real-time neural network-based phase generator" |
| 8 | A | a model baked from the scene's trained radiance field, rendered for every new view | the scene changing. The radiance field under it is itself fitted to the scene's photos, which is B-like for views far from them, but the baking is "lossless" | "a lossless procedure for baking the parameterization used during training into a model" |
| 18 | B | a character model learned from one person's multi-view video | motions unlike those it was trained on | "by merely providing new skeletal motions, our model creates motion-dependent surface deformations" |
| 20 | B | a clothing model learned from data | motions unlike the training data | "treats training data as a 'black box'" |
| 33 | B | textures baked from a learned head avatar | expressions and poses unlike the training video. It could be argued A (baked for this avatar); what goes stale is the expressions | appearances "expression-, pose-, and view-dependent … baked into static textures" |
| 40 | C | correction vectors from a relaxation, the same for every importance density | nothing in the problem: a table about the method, not about any instance | "Pre-computed correction vectors, obtained using relaxation" |
| 41 | unclear | Pareto frontiers of rendering settings | not said what they are computed from | "explore the vast power-error space and leverage optimal Pareto frontiers at runtime" |
| 47 | A | directional occlusion caches of a scene | the scene's geometry changing (the lighting is what varies) | "precomputing sparse directional occlusion caches … used for accelerating a fast cinematic lighting pipeline" |
| 48 | both | a reduced deformable model per domain of this mesh | the mesh changing (A), and deformations leaving the reduced space (B) | "build a reduced deformable model for each domain" |
| 50 | A | a quadtree over each face's parameter domain | the base mesh's faces changing | "subdivide the u, v domain of each face ahead of time, generating a quadtree structure" |
| 53 | A | basis functions, one per degree of freedom of the manipulator | the support region and boundary constraints changing (the manipulator moves) | "precomputing a set of scalar-valued basis functions that correspond to the degrees of freedom of the manipulator" |
| 55 | A | per-image preprocessing | the image changing (the palette is edited) | "After preprocessing, our algorithm can decompose 6 MP images into layers in 20 milliseconds" |
| 56 | B | a personalised face model and an image-to-avatar regression trained on a short video | new environments, handled by few-shot fine-tuning | "we learn a regression for real-time inference … fine-tune the real-time regression model with a few-shot learning strategy" |
| 58 | B | a user-specific regressor from images of the user's poses and expressions | inputs unlike its training images | "learns an accurate, user-specific face alignment model from an easily acquired set of training data" |

Counts: A 6, B 6, C 1, both 1, unclear 1. Clearly A or B: 12 of 15, exactly the bar, so by this classification the two-kinds branch is taken with no room to spare.
