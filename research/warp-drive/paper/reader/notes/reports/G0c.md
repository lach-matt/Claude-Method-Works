# G0c: the closing of thm:tl5-hf at levels 3–7, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing; I read nothing under method/, drive/, extracted/ or
recovered/. Read: G0.md and G0b.md (whole), proofs/P-HF.md (md5 f5d9cd38…, whole) and its report, S-APP.md,
N-APP1.md (§§0–3, 8), DECISIONS.md, and chapter 87 where cited (the data, and the merged sec:tl5-hf: def:tl5-hf-constants,
eq:tl5-hf-smallness, thm:tl5-hf). Every number carries one of three labels:
- **computed**: floating point, mine; scripts and outputs under `scratchpad/g0c/` (§G0c.8);
- **deduced**: an argument or a bookkeeping choice given here;
- **record**: G0, G0b, S-APP, N-APP1, P-HF or chapter 87, cited.

All figures are at the **merged** closing condition 8(√2δ_w + 2ε_w)S_F < 1 (chapter 87, eq:tl5-hf-closing), with the
conventions M_w := 8√2 S_F (so the closing reads M_w(δ_w + √2 ε_w) < 1, G0b's form), G_N := 2S_F with e^(φ/2) → 1 (so
4F²G_N is the single-domain multiplier, G0b's M₁), and targets with G0b's margin of 10 and δ_w ≤ ε_w. The background is
G0/G0b's provisional approximant (the record's solver runs, `appC_R528_264_40_48.npz` seed 1, `appC2_…` seed 2) on G0b's
48 × 37 × 15 grid.

---

## G0c.0 Answer

1. **Level 6 as written does not close, on either domain at either seed: its residual targets lie 98–117 decades below
   quad-double precision (10^−35)** (computed).
   log₁₀M_w = 126.5 (seed 1, D_A), 127.8 (seed 2, D_A), 145.0 (seed 1, D\*), 139.2 (seed 2, D\*). The closing needs a
   residual f ≲ 10^−133 … 10^−152, the unweighted C⁵ residual bound ϱ ≲ 10^−189 … 10^−212, and the N₀ mismatch
   η₀ ≲ 10^−110 … 10^−122. G0b's gate quantity is F²G = 134–161 against its STOP line 35: NO-GO everywhere. The formal
   evaluations at N = 3, 4, 5 (outside P-HF's N ≥ 6) are NO-GO too: log₁₀M_w = 51–66 at N = 3 and 72–87 at N = 4.
2. **Most of this is not the level. It is P-HF's explicit constants:** 89–99 decades over a constant of G0b's form at the
   same level, rates and μ (computed). Within that:
   - about 47 decades are the single bound Λ, which P-HF uses for every background factor up to order N + 2. It enters
     𝔠_n as (Λ + 1)^k and C₁ as (1 + 6Λ); Λ ≈ 10⁹–10¹⁰ at level 6, set by the eighth derivatives of π at the wave's peak;
   - 14–22 decades are 𝔤_N against G0's c_NL after that grading;
   - 17–20 decades are k₁, which enters twice (in 𝔞 and in C_∞);
   - 13–17 decades are C₁ against G0's C_S;
   - about 1.5 decades are √(2𝔐).
   These maxima sit at different points, so the parts overlap by a few decades and do not add exactly.
   P-HF's second factor μ^(−N/2) in S_F costs another 11.6–16.3 decades.
3. **What the level itself costs is 9.5–13.6 decades in M_w and 11.6–16.2 in f.** With G0b-type constants at level 6 and the
   minimal power μ^(−N/2), log₁₀M_w = 24.3, 21.3, 31.6 and 26.3 (computed), against G0b's level-3 record of 12.6, 11.8,
   18.0 and 15.3. Of this:
   - 6.7–8.3 decades are the μ power of the level weights;
   - 0.5–1.5 decades are the cross-level coupling;
   - 1–2.4 decades are the growth of the same-level couplings and the Leibniz count;
   - 1.2–2.0 decades are P-HF's level-3 operator structure.
   The residual's higher derivatives cost a further 1.3 decades in f.
4. **The figures for level 4** (the author's second version) are in §G0c.3, together with the list of factors that
   change from level 6. With G0b-type constants level 4 gives log₁₀M_w = 17.8, 15.7, 23.4 and 19.8, and f = 10^−22.9,
   10^−20.9, 10^−29.0 and 10^−25.4 (computed); that is 5.6–8.2 decades in M_w less than level 6 and 3.9–5.4 decades more
   than G0b's level 3. P-HF's formulas evaluated at N = 4 give 72–87, still NO-GO.
5. **The approximant (§G0c.5).**
   - At the level-6 targets with G0b-type constants, S-APP's size model at level-6 weights gives 1,961, 1,643, 8,034 and
     4,117 pages (worst-case rule; computed). Against these, S-APP has 451, 425, 1,740 and 1,158 at level 3, and N-APP1
     has 577, 558, 1,982 and 1,588 at level 6 at G0b's targets (record).
   - At P-HF's targets as written the model extrapolates to about 3 × 10⁵ pages for f alone, and to 10⁶ or more with the
     ϱ requirement. That cannot be printed.
   - Hypothesis (a), now η₀ < 𝔰₁ in the merged text, needs η₀ ≲ 10^−110 … 10^−122 as written. With graded Λ it needs
     10^−64 … 10^−72 (𝔰₁ itself rises to 10^−23 … 10^−30), and with G0b-type constants only 𝔰₁ ≈ 4 × 10⁻⁶.
6. **Reach and levers (§G0c.6).**
   - As written, level 6 closes for no u\* ≥ −9: even [−10, −9] × [½, 7/2] needs f ≲ 10^−115 (computed).
   - The best levers are both rigorous restatements:
     - order-graded background bounds in Lemma G and C₁ (and, not computed, in k₁), worth about 47 decades (computed
       variant);
     - level-matched μ powers (one μ^(−N/2) in S_F removed), worth 12–18 decades.
   - With both, log₁₀M_w is 65–80, still far off. The remaining distance to the G0b-type figures (41–49 decades) is P-HF's
     chain of constants: k₁ twice, C₁ against C_S, 𝔤_N against c_NL, and 𝔐.
   - With G0b-type constants, level 6 reaches u\* ≈ −1.19 at seed 1 (quad-double) and all of D\* at seed 2 (f = 10^−32.8).
     The gate's GO line falls at u\* ≈ −5 (seed 1) and ≈ −3 (seed 2), against ≈ −1.17 at G0b's level 3.

## G0c.1 Side by side: G0b's level 3 and level 6 (merged closing)

**The figures** (log₁₀M_w; residual target f; computed except G0b's columns, which are record):

| | G0b L3: M_w | G0b L3: f | L6 as written: M_w | L6 as written: f | L6 as written: ϱ, η₀ | L6, G0b-type constants, μ^(−N/2): M_w | its f |
|---|---|---|---|---|---|---|---|
| seed 1, D_A | 12.63 | 10^−16.5 | **126.5** | **10^−132.8** | 10^−189, 10^−110 | 24.3 | 10^−30.3 |
| seed 2, D_A | 11.76 | 10^−15.6 | **127.8** | **10^−134.1** | 10^−199, 10^−112 | 21.3 | 10^−27.2 |
| seed 1, D\* | 17.99 | 10^−21.9 | **145.0** | **10^−151.8** | 10^−212, 10^−122 | 31.6 | 10^−38.1 |
| seed 2, D\* | 15.27 | 10^−19.1 | **139.2** | **10^−146.0** | 10^−212, 10^−120 | 26.3 | 10^−32.8 |

**Where the decades go in log₁₀M_w** (computed figures; the order of the replacements is a bookkeeping choice, deduced;
each step re-optimises μ over 10⁻³ … 10⁻⁶):

| step | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| G0b level 3 (record) | 12.63 | 11.76 | 17.99 | 15.27 |
| (i) P-HF's level-3 operators: per-component couplings 𝔒 with exact per-letter norms, a 4-block bulk per level, cross-level couplings from ℒ^sπ (growth model), 21 rays | +1.9 | +1.2 | +0.9 | +1.2 |
| (ii) the j-fold same-level count at level 3 | +0.05 | +0.01 | +0.5 | +0.1 |
| (iii) **the μ power of the level weights**: μ^(−N/2) at level 6 against μ^(−3/2) | **+8.2** | **+6.7** | **+8.3** | **+8.2** |
| (iv) **the cross-level coupling**, level 3 → 6 | +0.5 | +0.7 | +1.5 | +0.5 |
| (v) same-level growth (up to 6‖m‖) and the Leibniz count 9·2^N | +1.0 | +0.9 | +2.4 | +1.1 |
| = **level 6, G0b-type constants** | 24.3 | 21.3 | 31.6 | 26.3 |
| (vi) P-HF's second μ^(−N/2) in S_F | +13.7 | +11.6 | +16.3 | +13.8 |
| (vii) P-HF's constants (𝔤_N, k₁ twice, C₁/C_∞, 𝔐) | +88.6 | +95.0 | +97.1 | +99.1 |
| = **level 6 as written** | 126.5 | 127.8 | 145.0 | 139.2 |
| of (vii): the uniform Λ (removed by grading, §G0c.6) | 46.2 | 47.9 | 47.9 | 47.7 |

**The other two factors the coordinator named:**

- **Data order.** It costs nothing in M_w.
  - In the targets: δ_w now carries N₁ and N₀ faces at level 6 (merged text). A data mismatch converts into δ_w like
    the residual into ε_w: 7^(N/2) words, so +1.3 decades relative to level 3 (deduced).
  - Splitting δ_w's budget between the two faces costs 0.15 decades.
  - The binding new requirement is hypothesis (a), η₀ < 𝔰₁, together with η₀'s terms in 𝔯_w and 𝔰_\*. It asks
    η₀ ≲ 10^−110 … 10^−122 as written (deduced from computed constants with C_(∞,0) ≈ C_∞).
- **The residual's higher derivatives.**
  - The conversion ε_w/f grows by 7^(3/2) = 18.5 from level 3 to level 6: −1.27 decades in f (computed; the 𝔮-terms
    add < 0.01 at the optimal μ).
  - G0b's 2.5 × 10² did not count the 7^j words at level 3 either: a further −0.9 (D_A) to −1.5 (D\*) decades against
    G0b's convention.
  - As written, ε_w also contains (1/4)𝔤_N k₂ ϱ, and 𝔯_w ≤ 1/4 contains ϱ. That is the separate target ϱ above (an
    unweighted sup, so no allocation), and it dominates the printing (§G0c.5).

**f in one line per case** (G0b-type constants): f(L6) − f(L3, G0b) = −13.8, −11.6, −16.2 and −13.7 decades. Of this:
- −ΔM_w accounts for −11.7, −9.5, −13.6 and −11.0;
- the residual-derivative conversion and the closing constant account for −2.1, −2.1, −2.6 and −2.7.

## G0c.2 The level table: P-HF as written (merged closing; computed)

Decision as G0b: GO if F²G ≤ 10²⁵, NO-GO above 10³⁵. "Floor" means μ = 1 with all cross-level terms (ℭ_(jj′), 𝔮_(jj′),
j′ < j) removed. μ is the value giving the loosest f (grid 10⁻³ … 10⁻⁶). N = 3, 4, 5 are formal (P-HF needs N ≥ 5 for
Lemma G and N ≥ 6 for persistence).

| N | | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|---|
| 3 | F²G (floor) | 57.5 (48.2) | 59.8 (51.4) | 74.9 (64.7) | 70.7 (61.3) |
| | M_w; f; μ | 51.2; 10^−56.2; 3e−5 | 54.6; 10^−59.6; 3e−4 | 65.5; 10^−71.1; 3e−6 | 62.9; 10^−68.4; 3e−5 |
| 4 | F²G (floor) | 79.9 (67.1) | 79.6 (69.1) | 102.9 (86.5) | 92.6 (79.6) |
| | M_w; f; μ | 72.2; 10^−77.7; 3e−5 | 74.7; 10^−80.2; 1e−4 | 87.2; 10^−93.2; 1e−5 | 84.0; 10^−90.0; 3e−5 |
| 5 | F²G (floor) | 107.7 (91.2) | 104.3 (90.9) | 133.4 (112.3) | 120.2 (103.4) |
| | M_w; f; μ | 99.0; 10^−104.8; 3e−5 | 98.9; 10^−104.8; 1e−4 | 115.4; 10^−121.8; 1e−5 | 109.3; 10^−115.7; 3e−5 |
| **6** | F²G (floor) | **136.4** (116.1) | **133.9** (117.3) | **161.2** (139.5) | **151.5** (130.8) |
| | M_w; f; μ | **126.5; 10^−132.8**; 3e−5 | **127.8; 10^−134.1**; 1e−4 | **145.0; 10^−151.8**; 3e−6 | **139.2; 10^−146.0**; 3e−5 |
| | ϱ; 𝔰₁ | 10^−189; 3e−62 | 10^−199; 6e−67 | 10^−212; 9e−70 | 10^−212; 9e−70 |
| 7 | F²G (floor) | 168.9 (144.6) | 167.9 (148.1) | 196.1 (170.4) | 184.3 (162.2) |
| | M_w; f; μ | 157.8; 10^−164.5; 3e−5 | 161.1; 10^−167.8; 1e−4 | 178.2; 10^−185.4; 3e−6 | 173.3; 10^−180.5; 1e−5 |

Every entry is **NO-GO**. In every case the binding condition is the closing condition, not 𝔰_\* < 𝔰₁.

**The pieces at level 6** (computed, maxima over the grid at the optimal μ; seed 1, D_A, with the others in brackets in
the order seed 2 D_A, seed 1 D\*, seed 2 D\*):
- log₁₀F² = 14.3 (10.9, 23.5, 19.2), and 7.5 (6.3, 18.4, 12.1) without cross-level terms. The rates are not the problem
  at level 6: they sit 2.8–6.5 decades above G0b's level 3 (F₃² = 8.1, 8.1, 18.4, 12.7, record).
- log₁₀G_N = 122.1 (123.0, 137.7, 132.3), made of:
  - μ^(−6): 27.1 (24.0, 33.1, 27.1) decades;
  - 𝔤_N: 60.1 (67.1, 65.8, 68.8). 𝔠₆ is about 10⁷¹–10⁸⁰ because Λ = 9 × 10⁸ (5 × 10⁹, 1.6 × 10¹⁰, 1.6 × 10¹⁰);
  - 2k₁ + 4: 8.6 (8.0, 10.0, 8.7);
  - C_∞ = 2k₁(2𝔐)^(1/2)C₁: 26.1 (25.7, 30.0, 28.7), with C₁ at 16.0 (16.8, 18.5, 18.5) against C_S = 4.2–4.6.
- e^(φ/2) adds 4.4–7.2 decades between G and M_w.
- 𝔰₁ = 𝔰₀/2 with 𝔰₀ = 1/(2 sup k₃), and k₃ ∝ 𝔠_N, gives 𝔰₁ ≈ 10^−62 … 10^−70.

## G0c.3 What level 4 changes (for the level-4 version being written)

**Factors that differ from level 6** (deduced, with the computed values for this background in brackets; level-6
values second):
1. **μ power.** S_F carries μ^(−N): μ^(−4) as P-HF is written, or μ^(−2) with level-matched powers. At the optimal μ
   (3 × 10⁻⁶ … 10⁻⁴) that is 8–11 decades less than μ^(−6), and 4–5.5 less than μ^(−3).
2. **Rates.** 𝔅₄ is 20 × 20. Its same-level couplings go up to 4‖m‖ and its cross-level couplings involve ℒ^sπ for
   s ≤ 3 only (log₁₀F² = 11.1, 8.7, 22.5, 15.8, against 14.3, 10.9, 23.5, 19.2 at level 6).
3. **Background bounds.** P-HF's Λ bounds derivatives of π to order N + 2 = 6 (Λ = 8 × 10⁵ … 1.4 × 10⁷, against
   9 × 10⁸ … 1.6 × 10¹⁰), so 𝔠₄ ≈ 10³⁵–10⁴¹ against 𝔠₆ ≈ 10⁷¹–10⁸⁰. A level-4 product estimate with its own constants
   replaces Lemma G, and these figures will move with it.
4. **k₁**, through α_𝔄 over couplings to level N − 1 = 3: 10⁴–10⁶, against 5 × 10⁷–6 × 10⁹.
5. **𝔐** = Σ_(j≤1) 7^j = 8 against 400, so (2𝔐)^(1/2) = 4 against 28: −0.85 decades.
6. **Residual.** σ_N contains 7^(N/2) = 49 words against 343: −0.85 decades in f. ϱ becomes a C³ sup of the residual
   instead of a C⁵ sup.
7. **Data.** δ_w needs 4 transversal derivatives on N₁ instead of 6. η₀ involves derivatives of G^♯ − ĝ of order ≤ 4 on
   N₀, that is only the **fourth** v-derivatives, the first order at which the solution leaves the seed (N-APP1 §8),
   against orders 4–6 at level 6.

**Level-4 figures available now** (computed; merged closing):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| G0b-type constants, μ^(−N/2): M_w; f; μ | 17.8; 10^−22.9; 3e−5 | 15.7; 10^−20.9; 1e−4 | 23.4; 10^−29.0; 3e−6 | 19.8; 10^−25.4; 3e−5 |
| the same with μ^(−N) | 26.6; 10^−31.7 | 22.9; 10^−28.0 | 34.0; 10^−39.6 | 28.8; 10^−34.4 |
| P-HF's formulas at N = 4, graded Λ and μ^(−N/2) (both levers) | 43.4; 10^−48.8 | 46.7; 10^−52.1 | 57.3; 10^−63.3 | 55.3; 10^−61.2 |
| P-HF's formulas at N = 4 as written | 72.2; 10^−77.7 | 74.7; 10^−80.2 | 87.2; 10^−93.2 | 84.0; 10^−90.0 |
| pages at the first row's target (S-APP model, level-4 weights) | 876 | 753 | 3,594 | 1,986 |

The first row is a floor for any level-4 proof that uses these rates: it has the sharp nonlinear constant of G0
(c_NL C_S, which G0 itself calls a conservative product) and the minimal μ power. Once the level-4 constants exist, the
figure is that row plus the excess of their nonlinear constant over G0's c_NL C_S, plus their μ power beyond μ^(−2).

## G0c.4 How the numbers were made

**Operators and constants exactly as in P-HF/chapter 87** (deduced from the text; evaluated pointwise, computed):
- **Bulk.** 𝔅 (4 blocks +, −, ∥, 0) is merged from G0's 5-block bulk on Sym², with exact block norms given the
  sub-blocks. Level 0 agrees with the 5-block form to 0.01 decade.
- **Level-N matrix.** 𝔅_N := diag(𝔅) + 𝔒 + 𝔒ᵀ with 𝔒_((j,±),(j′,ϰ)) = √cΩ̂³μ^((j−j′)/2)ℭ_(jj′ϰ), then (1 − ϑ)⁻¹𝔅_N
  with ϑ = 10⁻². The rates come from G0's ray LP (21 rays; at level 0 these cost 0.12 decades against G0's 49).
- **Couplings ℭ, 𝔮, α_𝔄, q₁.** These come from a recursion over levels that follows eq:tl5-hf-system and
  lem:tl5-hf-recovery: C(j, s+1) terms per subset; the principal coefficient ℒ^Sπ is recovered to level j − s; P₁, P₀ act
  on level j − 1 − s; the 𝔷, 𝒞, 𝓡 pieces of the recovery go to level j − 1 − s; and the (1,1) slot feeds L̂Ψ_J back in.
  - **Same-level coupling.** It is the exact per-letter map m[W, Z, A′] (direction-resolved recovery), split by the
    components +, −, ∥.
  - Computed check (`multnorm.py`): the exact operator norm of the j-term same-level map equals j‖m‖ to 1 % for
    j = 1…5 at every node tested, so the j-fold count is real.
  - ‖m‖ is 2.5–3× below G0b's column bound cs. With cs in place of m, seed 1's D\* level-3 figure (G0b-type constants)
    rises by 9.8 decades in M_w and 22 in log F² (computed; files `*_cs.json`).
  - P₁, P₀ are G0b's exact spectral norms.
  - Couplings of order s ≥ 1 are these times γ(s), from the growth model below (an estimate).
- **Derivative growth** (`dgrowth.py`, computed; `growthmodel.py`, estimate).
  - The exact ℒ_T^sπ^Z (jets of order 9) and the proxy ∂_ϑ^s for the rotations were measured up to s = 8.
  - The T-sequence is trusted to s = 3 and the rotation sequence to s = 5. Beyond those orders the T-sequence peaks at
    the chart's edges, the signature of the fit's endpoint growth.
  - Higher orders are continued factorially (the ratio r_S·s/S, capped at twice the median ratio). Words are built from
    7 letters with Cartan letters ×2.
  - Λ = max(1, |R̂|, 1.5 X_(N+2) r_D², 1.5 X_(N+1) r_D), the sup over words of the order-(N + 2) and (N + 1) derivatives.
- **The rest, literally:** C_S, C₁, C_(1,ϱ), C_∞, C_(∞,ϱ) with the face suprema; k₁, k₂, k₃; 𝔠_n (Fubini numbers); 𝔤_N;
  𝔞_o, 𝔞_i, ϰ₀ with 𝔡 = 4‖ω‖ (computed: ρ(Σw_iD_i) = 4|w|); S_F; 𝔯_w; 𝔰₀, 𝔰_θ, 𝔰₁, 𝔰_\*; κ = κ′ = 10⁻²; C_(S³)² = 1/12
  exactly.
  - max_Z|D̂Z| is G0b's record (2.19 and 1.78).
  - max|D̂²Z| uses the Killing identity |R̂||Z| (an estimate).
- **Targets.**
  - The closing (margin 10, δ_w ≤ ε_w) and 𝔰_\* < 𝔰₁ give the ε_w budget.
  - f bounds max over |I| ≤ N of μ^(|I|/2)|ℒ^I f_ab| (S-APP's certified quantity extended to level N). ε_w's s_N-part
    gets half the budget, and ϱ gets the other half and 𝔯_w ≤ 1/40.
  - The conversion 𝒮[σ_N · 2√15 √72/R⁴] is taken with φ = 0, the uniform target, as G0b did.
- **"G0b-type constants".** These are G0's M_w = 4√2 c_NL S_F^NL μ^(−pw) with c_NL = 9 · 2^N and G0's C_S, evaluated with
  the level-N rates.
  - pw = N/2 is the minimal power: the low quantities need the level-N energies. It is the comparison for "what the
    level costs".
  - pw = N is P-HF's power.
- **Graded variant.** This is a lever estimate, deduced and not part of P-HF: each factor with k letters is bounded by
  Λ_(k−1) instead of Λ in 𝔠_n, and Λ₃ is used in C₁.

**Growth sensitivity** (computed, `levelN_*_sc0.5.json`). Every continued ratio was halved, that is every order beyond
the trusted 3 (T) and 5 (rotations).
- P-HF's level-6 log₁₀M_w falls by 12.3, 12.5, 4.1 and 12.4 decades (seed 1 D_A, seed 2 D_A, seed 1 D\*, seed 2 D\*),
  and Λ by 14–30×.
- The graded variant falls by 1.3–3.3.
- The G0b-type figures do not change (to 0.01): at the optimal μ the continued orders do not reach the rates.
- No verdict moves. The growth model is the largest single uncertainty of the "as written" column, at roughly ±12
  decades, and is negligible for the level's own cost.

## G0c.5 What level 6 does to the approximant

1. **The residual must be certified in the level-N norm.** The certified quantity becomes max over |I| ≤ N of
   μ^(|I|/2)|ℒ^I f_ab|, S-APP's B_e with l ≤ N; N-APP1's certificate order K is the parameter. As written there are two
   further pieces:
   - ϱ, the **unweighted** sup of |ℒ^J 2R̂ic| for |J| ≤ N − 1. It allows no e^(−φ/2) allocation and carries no μ
     weight, so it pays the full Markov/Bernstein growth of the residual over five derivatives;
   - η₀ (the N₀ mismatch, order ≤ N).
2. **Hypothesis (a) and the data.** I agree with N-APP1 §8.
   - The envelope sin⁴ is C³ and not C⁴ at v = ½ (chapter 87, record). So the solution's fourth v-derivatives on N₀ are
     nonzero, and no seed form (v − ½)^κ G meets the old (a).
   - The merged text replaces (a) by η₀ < 𝔰₁ and puts the N₀ face into δ_w. M_w is unchanged by this. The N₀ data take
     a share of δ_w's budget (−0.15 decades in the targets).
   - The real cost is η₀ itself. It is bounded by min(𝔰₁, its share of 𝔯_w, 𝔰₁/C_(∞,0)):
     - as written: ≈ 10^−110 (seed 1, D_A), 10^−112 (seed 2, D_A), 10^−122 (seed 1, D\*) and 10^−120 (seed 2, D\*);
     - with graded Λ: 10^−64 … 10^−72;
     - with G0b-type constants: 𝔰₁ ≈ 4 × 10⁻⁶, from 𝔰_θ.
     (Deduced from computed constants, with C_(∞,0) taken equal to C_∞.)
   - So the transported jets of orders 4–6 on N₀ must be enclosed to that accuracy (N-APP1's option (ii)).
3. **Pages** (S-APP's size model, imported unchanged except W_Γ to l ≤ N; V2 levers; φ allocation with the level-N rates'
   total; worst-case rule; dense format; computed).

| target | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| level 3 at G0b's targets (S-APP, record) | 451 | 425 | 1,740 | 1,158 |
| level 6 at G0b's targets, μ = 10⁻³ (N-APP1, record) | 577 | 558 | 1,982 | 1,588 |
| level 6 at G0b's target, μ = 10⁻⁵ (computed) | 367 | — | — | — |
| **level 6, G0b-type targets** (f = 10^−30.3, −27.2, −38.1, −32.8) | **1,961** | **1,643** | **8,034** | **4,117** |
| level 4, G0b-type targets (f = 10^−22.9, −20.9, −29.0, −25.4) | 876 | 753 | 3,594 | 1,986 |
| level 6 as written (f ≈ 10^−133 … −152; ϱ ≈ 10^−189 … −212) | ≈ 3 × 10⁵ for f alone; ≳ 10⁶ with ϱ (extrapolated) | | | |

- **Calibration of the extrapolation** (computed, seed 2 D_A, level 6, μ = 10⁻⁴): f = 10^−45 gives 7,959 pages, 10^−60
  gives 20,513, and 10^−80 gives 54,451. The local slope is pages ∝ (−log f)^3.4.
- **The ϱ requirement** at an equal nominal target f_ρ = f = 10^−30 multiplies the pages by 2.7 (5,833 against about
  2,200), and f_ρ = 10^−45 gives 15,927.
- The level-6 weights themselves cost little at small μ: the derivative loss is μ^(l/2)(growth)^l. At μ = 10⁻⁵, level 6
  at G0b's target is cheaper than S-APP's level 3 at μ = 10⁻³.
- The page figures move with the target (12–17 % per decade near 10^−20, falling to about 5 % per decade near 10^−80,
  computed). They carry S-APP's risk 1: ×3.3 if the decay is 30 % slower.

## G0c.6 Reach and levers

**Reach** (computed, D\*'s grid restricted to u ≤ u\*):
- **As written, level 6 closes nowhere.** log₁₀M_w = 110.9 and f = 10^−115.5 already at u\* = −9 (seed 1), and 114.2
  and 10^−118.8 (seed 2).
  - The cause is that the full v-range carries the wave from the data on N₁ onward: Λ, 𝔠_n and k₁ are pointwise and do
    not shrink with u\*.
  - Formal level 4 as written: 10^−64.5 at u\* = −9.
- **With both levers (graded Λ, level-matched μ) it still closes nowhere:** f = 10^−64.9 (seed 1) and 10^−64.3
  (seed 2) at u\* = −9.
- **G0b-type constants at level 6** (log₁₀M_w; f; F²G):

| u\* | −9 | −7 | −5 | −3 | −2 | −1.5 | −1.3 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|---|---|
| seed 1 | 16.3; −20.6; 19.5 | 18.8; −23.7; 23.0 | 20.4; −25.7; 25.0 | 22.4; −28.0; 27.6 | 24.3; −30.3; 30.4 | 25.7; −31.9; 33.8 | 27.4; −33.7; 35.8 | 28.5; −34.9; 38.1 | 31.6; −38.1; 44.7 |
| seed 2 | 14.8; −19.1; 16.1 | 16.8; −21.7; 20.5 | 18.2; −23.5; 21.7 | 19.9; −25.6; 25.8 | 21.3; −27.2; 27.3 | 22.6; −28.8; 30.4 | 23.6; −29.9; 31.0 | 24.4; −30.8; 32.7 | 26.3; −32.8; 35.3 |

  Reach at level 6 with these constants:
  - **seed 1:** u\* ≈ −1.19 for a quad-double target (f ≥ 10^−35). The gate's GO line is at u\* ≈ −5. No u\* ≥ −9 is
    reachable in double-double (f ≥ 10^−20).
  - **seed 2:** D\* itself is within quad-double (f = 10^−32.8). The gate's GO line is at u\* ≈ −3 (F²G = 25.3–25.8 on
    [−3, −2.5]), and double-double reaches u\* ≈ −8.4.
  - The level costs seed 1 its D\* even with sharp constants: compare G0b's level-3 reach, where the GO line was at
    u\* ≈ −1.17 (record).

**Levers, in order of measured gain at level 6** (computed variants, unless marked):
1. **Order-graded background bounds** in Lemma G, in C₁ and (not done here) in k₁: −46 to −48 decades. This is a
   restatement of lem:tl5-hf-quadratic with Λ_k for factors carrying k letters (deduced; not in P-HF). It also lifts 𝔰₁
   from 10^−62 to 10^−23 and η₀'s target to about 10^−64.
2. **Level-matched μ powers.** The high factor of a monomial in the equation for Ψ_I has level ≤ |I|, so the
   μ^(−N/2) inside 𝔞 can go (deduced). Worth 11.6–16.3 decades at G0b-type constants and 13.8–17.6 after lever 1.
3. **G0's sharper chain.** The remaining distance to G0b-type constants, after levers 1–2, is 41–49 decades (computed).
   At seed 1's D_A it is made of:
   - k₁ twice: 17;
   - C₁ and the 𝔳⁶𝔴⁶, 𝔭₃, 𝔨₂ chain against C_S: 13.5;
   - 𝔤_N against c_NL: 14;
   - (2𝔐)^(1/2): 1.5.
   The other cases are similar, with 𝔤_N up to 22. Each is a separate restatement.
4. **Exact operator norms where P-HF says exact.** These are already used here: the same-level ℭ uses ‖m‖, which is
   2.5–3× below G0b's cs (9.8 decades in M_w at level 3, seed 1 D\*).
5. Smaller domains in u\* do not help (above). A smaller v\* is the domain lever that would, but it changes D_A and D\*.
6. **Not levers here.**
   - Staging: G0 §8, chains lose to the weighted norm.
   - The tilt κ′: C₁ ∝ max(1/c, 1/κ′)^(1/2), and κ′ = c_\* buys ≤ 0.5 decades.
   - Per-level weights μ_j: deduced, untested. They could trade the factorial growth of ℒ^sπ against the μ power, with
     an expected gain of a few decades at the G0b-type level.

## G0c.7 Caveats

1. **The provisional approximants** are G0/G0b's scoping objects. Their derivatives beyond order 3 (T) and 5
   (rotations) are modelled, not measured; Λ and the cross-level couplings rest on that model.
2. **Sup over φ** uses three phases, as G0b did with two; L7 must use φ-boxes. **Sampling:** grid nodes; the rays are
   21 rather than 49, conservative by about 0.1–0.3 decades in log F².
3. **max|D̂²Z|** uses the Killing identity, an estimate. **C_(∞,0)** is taken equal to C_∞ in η₀'s target.
4. **Upper bounds.** Several couplings are upper bounds: the triangle inequality over subsets and orders, and the
   (1,1)-recursion. P-HF's ℭ, 𝔮 are exact norms and could be smaller for s ≥ 1. The same-level count is exact (checked).
5. **The decade attribution** depends on the order of the replacements. Steps (iii)–(v) are taken at each step's own
   optimal μ.

## G0c.8 Files (all under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0c/`)

| file | what |
|---|---|
| `dgrowth.py`, `growth_s{1,2}.npz`, `growth_s{1,2}.out` | ℒ_T^sπ^Z (exact, jets of order 9) and ∂_ϑ^s (proxy) up to s = 8, on 24 × 19 × 9 nodes |
| `growthmodel.py` | word model, trusted orders, factorial continuation, interpolation to G0b's grid |
| `pointx.py` | P, Q, ζ, b; \|D̂∂_v\|, \|D̂∂_u\|, \|D̂T\|, div T, ‖ω‖, 𝔡, ‖𝒞_(·0)‖, ‖𝒞_(·1)‖, ‖𝓡̂‖, \|R̂\| |
| `multnorm.py` | exact level-j norm of the same-level map against j‖m‖ |
| `exactm.py`, `exactm_s{1,2}.npz` | exact per-letter, per-component same-level norms on the grid; \|π₁₁\| |
| `levelN.py` | the whole evaluation: 𝔅_N, couplings, LP, all constants of def:tl5-hf-constants, targets, G0b-type and graded variants |
| `levelN_s{1,2}_34567_{-2.0,-1.1}.json`, `run_*.out` | main results (exact norms); `*_cs.json` with G0b's cs |
| `levelN_s{1,2}_36_…_m1.json` | one same-level term per word (the attribution) |
| `levelN_s{1,2}_{4,6}_-9.0_….json`, `reach_*.out` | reach sweeps (level 6 complete; the level-4 sweep was stopped after u\* = −5 to free the processors) |
| `levelN_*_sc0.5.json`, `sens_*.out` | growth-model sensitivity |
| `summarize.py`, `tables.py`, `tables.md`, `chain.py`, `chain.json` | tables and the attribution chain (merged closing) |
| `pages.py`, `pages_*.out` | S-APP's size model at level N, with the ϱ requirement |
