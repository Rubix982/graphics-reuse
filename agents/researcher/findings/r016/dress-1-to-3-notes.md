# R-016 · Dress-1-to-3, read in full: notes against the ticket's questions

_Xuan Li, Chang Yu, Wenxin Du, Ying Jiang, Tianyi Xie, Yunuo Chen, Yin Yang, Chenfanfu Jiang. "Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics." ACM TOG / SIGGRAPH 2025; arXiv 2502.03449v2 (21 May 2025). Read 2026-11-14 in full except the reference list, from the arXiv HTML converted to text (`sources/r016/li2025-dress-1-to-3.txt`, git-ignored). Section numbers are the paper's._

**What it does.** One photo of a clothed person → an initial sewing pattern from SewFormer (quadratic Bézier panels) → multi-view RGB and normal images from a multi-view diffusion model (MagicMan) → an SMPL-X body fitted to those views → the pattern sewn and draped on the body → the pattern's curve vertices and control points, with global stretching and bending stiffness, optimised so the static drape matches the generated views (§4–6). The simulator is Codimensional IPC (intersection-free, log-barrier contact with CCD), made differentiable by the adjoint method plus autodiff, written in NVIDIA Warp (§3, §8).

## Q1 · Why each iteration's drape may start from the previous one, and what breaks it

- "For each optimization iteration, we use CIPC simulation to statically drape the garment onto the fixed-posed human body mesh. Leveraging the robustness of CIPC, we simulate one step of 1 second to directly reach near-static equilibrium. Since the static equilibrium does not locally depend on the initial state, meaning that the Jacobian matrix of the simulated state with respect to the initial state is zero, we update the initial state of iteration n … to the previously simulated state" (§6.1, Eq. 17).
- The argument is made for their gradients: the zero Jacobian means the start can change without entering the gradient. It is the same condition a finite-difference fit needs: the response measured between two warm drapes is the equilibrium's response only if the equilibrium doesn't depend on where the drape started.
- "Locally" is the limit they state. Nothing in the paper measures it: there is no warm-against-fresh comparison, no ablation of the warm start, and no report of time saved.
- What breaks it, in their text: friction (Q2), and a change of mesh (Q4), where the chain is deliberately broken.
- Their initial state x₀⁰ comes from the initial fit (§5.4): panels placed around a T-posed body, sewn and fitted bottom to top, one connected component at a time, then the body interpolated from the T-pose to the target pose as a moving boundary.

## Q2 · What removing friction buys and doesn't, and how slip is prevented

- "To make the simulation as path-independent as possible, we avoid adding friction during the process. To prevent the bottom garments from slipping down, the boundary loop of the bottom component near the waist area is fixed." (§6.1)
- In the initial fit, friction is used the opposite way: "To secure the bottom garments and prevent them from slipping during pose interpolation, we shrink the rest shape of the triangles near the waist to generate sufficient friction." (§5.4)
- What it buys is stated only as intent, "as path-independent as possible". Contact stays on (IPC barrier, self-contact included); only friction goes. The paper doesn't measure how path-independent the result is, nor whether folds still depend on the start.
- The final assets are animated with their CIPC simulator under motion (§7.2). The paper doesn't say whether friction is restored there.

## Q3 · How many iterations, and what each costs

- Not reported: no iteration count, no per-iteration time. Training is in two stages, with the Bézier control points (curvatures) frozen in the first because "edge curvatures K are more sensitive than vertex positions P" (§6.1).
- "The pre-optimization steps require about 10 minutes. The garment optimization process can be finished within 2 hours on a single RTX 3090 with 24GB device memory." (§8)

## Q4 · Flipped triangles, remeshing and penetration

- Flips: two Bézier curves that come close (a thin strip) may cross after an update, which "can lead to flipped triangles, causing the simulation to fail in the next iteration". The safeguard minimises negative triangle areas by least squares after the update, in place, only when triangles are close to flipping (§6.4, Eq. 30).
- Correspondence across iterations is kept by construction: the triangulation is fixed and its interior moved by fixed harmonic coordinates of the boundary samples, with the boundary sampling parameters also fixed. Both are updated only when the pattern is remeshed (§5.1.2, §6.5).
- Remeshing, triggered when mesh quality drops below a threshold: "directly remeshing the fitted garment state on the human body can lead to penetrations. This occurs because the underlying smoothly interpolated surface may intersect after re-triangulation, as the collision handling relies on the previous discretization." Instead, the new triangulation is pulled back to the initial pattern, the initial fit (§5.4) is re-run with it as the rest shape, then the garment is relaxed with the new triangulation as rest shape, and that becomes the next iteration's start (§6.5, Fig. 3). So a change of mesh costs a fresh drape.

## Q5 · What the method can't recover

- New pattern pieces not in SewFormer's estimate; layered garments (SewFormer predicts single layers, so layers fuse); patterns that may not follow design conventions; surfaces over-smoothed by the Laplacian and seam losses and by inconsistent generated normals (§10).
- Non-static targets: "Our method optimizes garments in static fitting states under gravity and body supporting forces. For non-static states, such as a snapshot of flowing … our garment optimization process attempts to approximate the non-static states by finding nearby static configurations … these static approximations may not reflect the garment's true geometry." (§9.4, Fig. 10)

## Other things in the paper worth keeping

- Physical parameters are fitted with the pattern: global stretching and bending stiffness are optimisation variables (§6.1), and the authors attribute part of their gain over SewFormer to that (§9.1).
- Results (Table 1): Chamfer distance 1.623 on CloSe and 2.441 on 4D-Dress against SewFormer's 2.233 and 2.926; mask IoU 0.862 and 0.808 against 0.748 and 0.720.
- Regularisers needed because "for the same sewn 3D garment mesh, there are infinitely many ways to decompose the mesh into flattened patches" (§6.3): area ratio, corner angles, comfort (ARAP stretch, against over-tight fits), Laplacian, seam length and curvature.
