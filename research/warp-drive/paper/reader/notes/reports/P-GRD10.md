# P-GRD10 report

File: proofs/P-GRD10.md (not committed), md5 871190e2fcc85ccaf1fcff32a454f7a3, 459 lines.
Lines 1–283 are the chapter text and lines 285–459 hold Placement, Comparison and Crosswalk.
Source tree: HEAD 3a6a1ee0, chapters/87-ten-l5.md md5 29a18cc0…, 6599 lines.

## What is proved

The new section is sec:tl5-hfp ("The leaf constant, the weights of the words and the seven fields"), printed as
Section 57.25. It goes after rem:tl5-hfz-what, and adds a pointer sentence to that remark. It defines 15 labels:

- **Lemma 57.215, lem:tl5-hfp-leaf.** On each SO(4)-isotypic piece V_π the sum over the 43 words is exactly
  (𝔶₀ + 𝔶₁c_π + c_π²)‖A_π‖². This gives the leaf Sobolev inequality with
  C_(E,r)(𝔶)² = (1/2π²) Σ d/(𝔶₀ + 𝔶₁c + c²), where 𝔶₂ = 1.
  - C^♯ := C(1, 1) satisfies C^♯² ≤ (4/3)C_(E,r)² = (2/9)·6C_(E,r)².
  - The sum gives a ratio of 0.418–0.422 for ranks 0–4, which is −0.375 decades.
- **Definition 57.216, def:tl5-hfp-constants.** Weights 𝔶₀ ≤ μ⁻² and 𝔶₁ ≤ μ⁻¹, and the following constants:
  - 𝔷′;
  - k₁^(j,ν′,p) and k₁^D;
  - 𝔨₂′ = 𝔨₂ − 1/(2Ω̂²z̲) and 𝒟_g;
  - the family coupling norm 𝔞_𝔄(𝔚);
  - 𝔩_D and 𝔩_J;
  - C₁(𝔚) = min(C₁^U, C₁^D + C₁^J);
  - C₁^p and C₁^Γ;
  - 𝔗(𝔶), with one form for each lemma in use;
  - C_S^p and 𝔐_p^(m);
  - 𝔨_rec^(·,p).
- **Lemmas 57.217–57.221.**
  - lem:tl5-hfp-abs: the weighted face lemma; k₁ with 𝔷′; the 𝒟_g-refined per-word bound; the zeroth-order bound
    over a family.
  - lem:tl5-hfp-words: second derivatives over a family of n words. The leading term counts once, the nonlinear part
    carries (43n)^(1/2), and the factors 𝔢_k keep the parts with ϱ and η₀ from growing.
  - lem:tl5-hfp-c1: the first-order bound over a family.
  - lem:tl5-hfp-rec: the seven fields in 𝔨_rec taken as one family. This is G0l's √301 lever (target 1).
  - lem:tl5-hfp-low: 𝔐_p^(m) at the low levels, N ≥ 6.
- **Theorem 57.222, thm:tl5-hfp.** The closing condition is
  `4 η_p^(−3/2) (δ_w + η_p^(−1/2) (ε^z + ε_M^p)) (S_F^p + S_M^p) < 1`, with 𝔰_*^p < 𝔰₁^v and η₀ < 𝔰₁^v.
  - At 𝔶₀ = 𝔶₁ = 1 every constant is at most the one in thm:tl5-hfz, so the earlier closing conditions stay valid.
  - It is stated with the intrinsic Sobolev choice of def:tl5-hft-constants.
- **Remark 57.223, rem:tl5-hfp-what.**

Target 2: K_rec is sharp for its step. It is the operator norm of the block-diagonal map, because CCᵀ = M⁻¹. The
lever proved in its place is the split, which puts 𝔨₂′ in front of k₁^D only. z̲ is not changed, so the rates are
not changed either.

## Levers, deduced from G0l's tables, not evaluated

**Level 4** (lem:tl5-hfq-theta, 𝔶 = (μ⁻², μ⁻¹)):

| Lever | Acts on | Seed 1 D_A | Seed 2 D_A | Seed 1 D* | Seed 2 D* |
|---|---|---|---|---|---|
| C^♯ | every face-Sobolev constant | −0.375 | −0.375 | −0.375 | −0.375 |
| Weights (q₃) | ℰ_g parts | −1.17 | −0.92 | −1.31 | −1.17 |
| Weights (q₃𝔗) | parts with ϱ and η₀ | −0.39 | −0.73 | −0.68 | −1.04 |
| Split | C₁ | −0.23 | −0.18 | −0.19 | −0.19 |
| Γ family + split | 𝔨_rec | −0.45 | −0.45 | −0.30 | −0.28 |
| Total | C_P^v | ≈ 2.0 | ≈ 1.75 | ≈ 2.0 | ≈ 1.8 |

𝔨_rec still leads C_P^v. At G0l's 1:1 rate this is worth up to about 1.75–2.0 decades on min(f, ϱ). It is capped by:
- S_M, which takes only the C^♯ factor (cost up to about 0.15);
- the parts with ϱ and η₀, which fall less;
- the 𝔰_* slack, which also moves.

**Level 6** (option (b), 𝔗 = 1):
- Sobolev constants: −0.375 − (0.92 to 1.31).
- 𝔐_p^(m): −0.57 to −0.73 at m = 1 and −0.69 to −1.01 at m = 2, against √114 and √800.
- Split: about −0.2.
- ϱ could move by up to 2.2–2.9 decades.

## Not done

- Target 4: not attempted.
- The other Sobolev choice (6C_(S³)²𝔭_r) with weights.
- The nonlinear absorption over the words.
- The 1/κ′ part of 𝔨₂, and z̲ in the rates.
- The 𝒟_g refinement inside S_F.

Under lem:tl5-hfs-linfty and lem:tl5-hft-small (a), 𝔗 grows. There the weights are a trade-off, and 𝔶 = 1 is still
available.

## Checks (scratch tree: git archive 3a6a1ee0, plus merge)

- `lint.py --chapters`: 62 files, 5281 labels, 0 hits.
- `assemble.py --check`: labels 5281, problems 0.
- In-memory check: `[] 0`.
- Numbering: of the 5,266 old labels, 0 changed, and 15 were added.
- Crosswalk: 430 rows for 430 chapter labels, in the same order.
- The Placement quotes match lines 6598–6599 of the old and new files, and the inserted section equals the chapter text.
