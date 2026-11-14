# R-015 · The four agents' final reports, verbatim

_Each area was searched by a fresh agent (claude-opus-5-5, with web tools) on 2026-11-14. These are their final replies, copied from their hand-back messages without edits, in the order they arrived. Their full notes are the four area files beside this one. The briefs they were given describe the private test bed, so they are kept in `private/r015-briefs.md` (git-ignored). The only change to the area files after the agents finished: one phrase describing the test bed's photos was made generic ("reference photo") in five places (see `verification.md`)._

## Area C: differentiable cloth and inverse garment fitting

The Area C file is written: /Users/saifulislam/code/graphics-reuse/agents/researcher/findings/r015/c-differentiable-fitting.md. It lists 46 queries, a 44-row candidate table with rejects, six picks in depth and a gaps paragraph. Numbers marked (verbatim) were checked in the PDF text. Those marked (extracted) came through WebFetch summaries and were not re-checked word for word.

**The picks:**
1. **Dress-1-to-3 (TOG/SIGGRAPH 2025).** The closest analogue to the test bed: one photo, a SewFormer pattern, then a differentiable C-IPC refinement. Each iteration starts from the previous drape, and friction is left out "to make the simulation as path-independent as possible." It took 2 h on an RTX 3090, has no code and uses Warp with CUDA, so it can't run here. Both conditions can be rebuilt in Blender.
2. **Wang 2018, rule-free pattern adjustment (background, cited by DiffAvatar and Yu et al.).** Same loop shape as the test bed's fit. It runs the inner drape short ("inexact") and does a full drape every M=32 steps, backing off if the cost hasn't dropped. It switches off friction and self-collision to get "a unique configuration," and states that drapes are "often not" unique. No code, but the strategy needs no gradients from the solver.
3. **Sensitive Couture (2011, background).** Caches drapes and their sensitivities and blends them by moving least squares. It is a more careful version of the test bed's pooled model, buildable in NumPy on CPU. It states that "buckling, wrinkling, and static friction" break linear prediction, which matches where the widths failed.
4. **DiffCloth (2022, background; MIT, CPU C++, tested on Mac OS 12, Apple Silicon not stated).** It measured that adding or removing contact nodes is the worst source of gradient jumps. On a bumpy one-parameter problem, evolution strategies beat L-BFGS-B. For the test bed that suggests sampling for the widths and Gauss–Newton for the lengths.
5. **PhysAvatar (ECCV 2024) and MPMAvatar (NeurIPS 2025).** Both fit 3 parameters by finite differences, as the test bed does. Neither reports noise or how stable the sign is.
6. **DiffAvatar (CVPR 2024).** A differentiable garment fit on a CPU: 14-core i7, about 1 min per iteration, 20–200 min total. No code is released.

**Surprising:**
- Two groups seven years apart (Wang 2018, Dress-1-to-3 2025) each turned friction off during the fit to make the drape depend only on the cut. That is a cheap test to run on the sign-unstable widths.
- Newton, the successor to `warp.sim` (which was removed in Warp 1.10), runs only on CPU on macOS. Its only differentiable cloth paths have no self-collision.
- No paper measures whether a sensitivity keeps its sign across runs.
- NGL-Prompter (2026) states that "VLMs struggle to reason about numeric garment parameters." None of the image-to-pattern models refines its estimate against the photo.

## Area A: learned and neural cloth

I wrote /Users/saifulislam/code/graphics-reuse/agents/researcher/findings/r015/a-learned-cloth.md. It covers 47 candidates, including rejects, with every query listed (26 web searches, 6 arXiv API queries, plus GitHub checks). That is the only file I wrote. Full-text reads went through WebFetch, which returns a model's extract of the page, not the raw text, so spot-check the numbers against the PDFs before they go into an entry.

**Best picks**
1. **HOOD** (Grigorev et al., CVPR 2023): the only pretrained neural cloth simulator I found that is MIT-licensed and works on garments it wasn't trained on. Verdict: probably runs on CPU, slowly. It is plain PyTorch, PyG and pytorch3d, I found no custom CUDA kernels, and the device is a config setting. Its mesh-sequence input path doesn't need SMPL, which requires an account. Its most plausible use is as a warm start that Blender then finishes. None of this was run.
2. **ContourCraft** (SIGGRAPH 2024): it handles cloth lying on cloth, which the scarf case needs. Verdict: does not run as shipped. Inference imports CUDA collision code (CCCollisions) and the install pulls in NVIDIA-only libraries (cudf, cugraph, cupy).
3. **GDSR** (SIGGRAPH Asia 2024): takes a coarse simulation and adds fine wrinkles, and it was tested on garments it hadn't seen. It is aimed at the smooth-folds problem. Verdict: plausibly runs on CPU. It is AGPL with a released checkpoint, but it was trained on Marvelous Designer output in a single fabric, so a Blender drape may be out of its range, and its preprocessing has to be rebuilt for macOS.
4. **ClothTransformer** (2026; the repo says NeurIPS 2026, unverified): MIT, plain PyTorch, checkpoint on Hugging Face. But it was trained on one fabric, its fabric can't be set, and its mean error is 6.92 cm, so it is useless as a stand-in inside the fitting loop.
5. **PhysGraph** (2023, no code found): worth having for the technique and one finding. A model trained only on small patches of cloth works on any garment because cloth physics is local. The technique itself, subdividing a coarse drape and relaxing it, can be rebuilt in Blender.

**Surprises**
- On CPU, HOOD may not beat Blender by much. An Arm blog measured it at 0.75–1.0 s per frame on phone CPUs for a 4,424-vertex garment. The large speedups in the papers are GPU numbers.
- No neural simulator takes the flat sewing pattern as its rest shape. HOOD's code uses a 3D mesh as the rest shape, so a cut change can't be fed in directly. None of them models sewing the seams closed either.
- ContourCraft says it can't handle a mesh edge passing through another surface. A scarf's free edges hitting the tunic is exactly that case.
- Nothing from 2023–2026 uses a network's drape as the starting point for a physical solver. The only example is from 2020, which I list as background. That is also the one design where reuse would change only the cost, not the answer.

## Area D: model rendering

I wrote the Area D file at `/Users/saifulislam/code/graphics-reuse/agents/researcher/findings/r015/d-rendering.md`. It lists 40 queries and about 60 candidates, rejects included, and covers six picks in depth. Nothing published fixes the dupatta density or the dark-backdrop light. The reuse that runs on the Mac today is Cycles' own settings, and nobody has measured them.

**Best picks:**
1. **Cycles Light Groups, Persistent Data and a fixed Seed** (Blender 4.5 manual). Light Groups change light colour and strength without re-rendering, so light weights could be fitted to the photo by least squares (my idea, untested). Persistent Data keeps render data between frames, though bug reports show stale data changing the image. A fixed seed makes ΔE between looks less noisy. Runs on CPU and Metal; no published timings.
2. **DiffusionLight-Turbo** (arXiv 2025). 31.9 min down to 0.54 min per estimate on an RTX 3090 Ti, with slightly worse scores. Its stated failures include low-key images with solid backgrounds, which matches the dark-backdrop case. MIT licence, built on SDXL; MPS in 16 GB is tight and untested.
3. **Woven Fabric Capture with a Reflection-Transmission Photo Pair** (SIGGRAPH 2024). It needs a physical swatch, so the test bed can't use it directly. What transfers is its argument that a reflection-only view can't fix how much light passes through. GPL-3.0, plain PyTorch that falls back to CPU.
4. **Colorful Diffuse Intrinsic Decomposition** (TOG 2024). An update to the ordinal-shading method the test bed already uses, about 1 s per image. Licence is academic use only; Marigold-IID gives the same three outputs under Apache-2.0 code and openrail++ weights. Aimed at the shading baked into projected prints.
5. **Parameter-space ReSTIR** (SIGGRAPH 2023). Reuses gradient samples across iterations of a fitting loop: over 4× lower gradient error on one scene (RTX 2080 Ti, compile overhead excluded). Its code needs an NVIDIA GPU, so it doesn't run on the Mac.
6. **Residual path integrals** (EGSR 2024). Renders only the difference between near-identical scenes, 4–16× faster than correlated path tracing for material edits, on a CPU. No code found; only its baseline (a fixed seed) is usable.

**Surprises:**
- The Blender 4.5 glTF exporter writes sheen and transmission but nothing for Cycles' Translucent BSDF; the glTF extension for that is still a Release Candidate. The manual says glTF alpha is meant for "medical gauze wrap", which suggests the dupatta's see-through coverage belongs in alpha (untested).
- The recent neural cloth model renders on CPU in Mitsuba 3 but can't handle printed or dyed cloth.
- Gaussian splatting gives nothing useful from one photo, though Metal trainers exist (msplat, OpenSplat, Brush).

The ticket, plan, card and `.gitignore` already show local edits; I didn't make those.

## Area B: fast cloth solvers and GPU simulation

I've written the area B survey to `/Users/saifulislam/code/graphics-reuse/agents/researcher/findings/r015/b-fast-solvers.md`. It covers 34 candidates, rejects included, with the 30 web searches and every page I fetched listed. Nothing was run or timed; all numbers are quoted from the papers or official repos with their hardware.

**Verified:** the cubic-barrier paper is Ando, ACM TOG 43(6), article 224, SIGGRAPH Asia 2024 (from the repo and OGC's reference list; I didn't open the paper PDF). Vertex Block Descent is Chen, Liu, Yang, Yuksel, ACM TOG 43(4), SIGGRAPH 2024. GIPC is Huang, Chitalu, Lin, Komura, ACM TOG 2024. StiffGIPC is ACM TOG 2025 according to the libuipc README.

**Best picks:**
1. **Offset Geometric Contact running inside Vertex Block Descent (SIGGRAPH 2025).** Cloth layers can't pass through each other, and it skips repeat collision checks while nothing has moved far. It runs on the CPU: a 15.7K-vertex dress takes 30 ms per step on the authors' C++ build (Ryzen 7950X). Mac verdict: the free Newton library (Apache-2.0) implements it and installs on macOS, CPU only. But its underlying Warp kernels run on one core on the CPU, so the speed here is unknown until a 5,000-vertex piece is timed.
2. **Domain-decomposed projective dynamics (SIGGRAPH 2025).** The only recent paper built for multicore CPUs, tested on garments. It is 10–100× faster than multithreaded CPU solvers, and a multi-layer dress takes 351 ms per frame on a 32-core Threadripper. Mac verdict: no code. The paper assumes all cores are equal, which Apple's performance-plus-efficiency chips are not.
3. **Progressive quasistatics (2022, background; unstructured-mesh follow-up 2023).** Solves for the resting drape directly, coarse to fine, without crossings. On a MacBook M1 Max a 370K-triangle drape took 122 s against 1,248 s for C-IPC. Mac verdict: no code, and the authors say seams are not handled.
4. **GarmentCodeData's settling rule (ECCV 2024).** A drape counts as static when at most 1.5% of vertices move more than 0.04 cm between frames; their cap was 2,400 frames, and about 72% of samples passed overall. Mac verdict: can be rebuilt in Blender Python now.
5. **Subspace reuse in Lan et al. (SIGGRAPH Asia 2024).** A garment-wide correction built once from the rest pose and reused every step cut later iterations by 70%. Worth a library entry; GPU only, no code.

**Surprises:**
- ppf's own documentation says cloth pinched by an animated character can stop with "Newton solve made no progress (over-constrained configuration)". That bears directly on the wide trousers caught between the legs.
- OGC names few contacts at high speed as its weak case, which describes the free-hanging scarf.
- Blender 5.2's experimental Geometry Nodes cloth has no self-collision, so it can't do layers.
- Most fast solvers spend minutes of setup per mesh (up to 77 min for one, JGS2). None measures what happens when the cut changes each run.
- Nothing from 2023–2026 addresses cloth pinched between legs.
