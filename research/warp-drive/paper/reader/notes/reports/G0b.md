# G0b: the D\* decision with a careful level-3 count, and seed 2

This follows G0.md (same directory) and uses its notation and section numbers. Report only: nothing in the repository was
edited or committed. Every number carries one of three labels:
- **computed**: floating point, mine; scripts under `scratchpad/g0/`;
- **deduced**: an argument given here;
- **record**: G0, S-H123 or chapter 87, cited.

The grid is 48 × 37 × 15 (G0 used 64 × 49 × 21). Level 0 agrees with G0 to 0.2 decades at every u\* (computed).

## G0b.1 Decision, restated

| | seed 1 | seed 2 |
|---|---|---|
| **D\* = [−10, −1.1] × [½, 7/2]**: log₁₀F₃²G | **28.05: in between** (G0: 32.66) | **22.33: GO** |
| floor without cross-level terms | 20.17 | 15.28 |
| log₁₀M₁ (single), log₁₀M_w (weighted) | 28.65, 17.99 | 22.93, 15.27 |
| **D_A = [−10, −2] × [½, 7/2]**: log₁₀F₃²G | **17.62: GO** (G0: 20.55) | **16.10: GO** |
| log₁₀M₁, log₁₀M_w | 18.22, 12.63 | 16.70, 11.76 |
| u\* where F₃²G crosses 10^{25} | **≈ −1.17** (G0: −1.38) | not crossed for u\* ≤ −1.1 |

**What was found.**
- The careful count lowers seed 1's D\* figure by 4.6 decades.
  - Exact commutator maps and the computed ∇π^E, ∇²π^E bring the same-level term from 20.04 to 16.50.
  - With the cross-level terms they bring the full figure from 32.66 to 28.05.
- The remaining cross-level surcharge (7.9 decades) is now mostly the polynomial factor μ^{−3/2} of the level weights
  (6.0 decades at μ = 10⁻⁴). Only 1.9 decades of it is exponential.
- Changing the angular commutation fields can target only the orbit–leaf block of π^E. Removing that block entirely
  would lower the same-level term by at most 0.02–0.7 decades (a computed diagnostic). The obvious co-moving
  alternative is 3× worse (§G0b.2).

**Residual needed** (computed from M; conversion ε ≈ 2.5 × 10² f under the μ-weights, §G0b.6; Ξ < 1 needs
f < 10^{−(log₁₀M + 2.9)}; precision tiers as in S-H123 §4: double-double 10⁻¹⁶–10⁻²⁰, quad-double 10⁻³⁰–10⁻³⁵).

| target | single domain (Ξ₁ < 1) | weighted (Ξ_w < 1) |
|---|---|---|
| seed 1, D\* | f < 10^{−31.5}: **quad-double, upper end** (10⁻³⁵ gives Ξ₁ ≈ 10^{−3.5}) | f < 10^{−20.9}: **quad-double** (10⁻²⁰ gives Ξ_w ≈ 8; 10⁻³⁰ gives 10^{−9.1}) |
| seed 1, D_A | f < 10^{−21.1}: quad-double | f < 10^{−15.5}: **double-double** (10⁻²⁰ gives 10^{−4.5}) |
| seed 2, D\* | f < 10^{−25.8}: quad-double | f < 10^{−18.2}: **double-double at its upper end** (10⁻²⁰ gives 10^{−1.8}) |
| seed 2, D_A | f < 10^{−19.6}: double-double at its upper end | f < 10^{−14.6}: double-double |

**Recommendation.**
- **Seed 2: GO for D\*.** With the weighted norm (G0 §8) a double-double approximant at f ≈ 10⁻²⁰ closes, with margin
  10^{−1.8}. Quad-double gives margin 10^{−11.8}.
- **Seed 1:** D\* stays in the intermediate band by the gate's rule, 3 decades above the GO line. With the weighted
  norm it needs a quad-double approximant (f ≲ 10⁻²²). The GO line is crossed at u\* ≈ −1.17.
  - A seed-1 target of u\* = −1.2 (F₃²G = 10^{23.4}, log₁₀M_w = 15.8, f < 10^{−18.7}) is reachable in double-double
    with the weighted norm.
- **D_A: GO at both seeds,** in double-double with the weighted norm.

**What would still move seed 1's D\*** (not done; §G0b.7):
- an interpolation (Gagliardo–Nirenberg) bound for |∇²h|_∞ using levels 2 and 3, which lowers the μ^{−3/2} cost
  (about 1–3 decades, deduced);
- a re-optimised weight family at level 3.
Together, plausibly 2–4 decades: enough to reach the GO line, but not shown.

## G0b.2 Lever 1: better angular commutation fields

**What dominates π^E (computed, `piblocks.py`, D\* approximant, seed 1).**
- The maximum of (Σ_E|π^E|²)^{1/2} is 3.04, at (u\*, v = 2.39, x = −0.993), near the axis x = −1 at the envelope's peak.
  - Orbit–leaf block: 2.53. Leaf–leaf: 1.59. Orbit–orbit: 0.54.
  - Medians: 0.11 in total; 90 % quantile 1.10.
- π^T (the seed's static field) peaks at 2.15 at the same place, dominated by the leaf–leaf block (1.89): the wave's
  strain of the leaves.
- The shift is large there (computed): |s| reaches 6.1 and |b|e^ζ 2.1, against max |s| = 0.57 on Π. At seed 2 the shift
  is much smaller (max |s| = 0.74).

**The orbit–leaf block is the commutator with the null pair (deduced).**
- For a field Z tangent to the leaves, π^Z(L, e_A) = ĝ([L, Z], e_A) and π^Z(L̲, e_A) = ĝ([L̲, Z], e_A). The null second
  fundamental forms are symmetric, so their contributions cancel.
- With the double-null angle (x constant along L = ∂_v), [L, E_ab] = 0 and [L̲, E_ab] = b[∂_x, E] − E(b)∂_x.
  The whole orbit–leaf block sits in the L̲-row and is proportional to the shift b and its x-derivative.

**Co-moving with L̲ is worse, not better (deduced; computed estimate).**
- Take an angle y transported along L̲ from N₁ (L̲y = 0, y = x on N₁). Then [L̲, Ẽ] = 0, but [L, Ẽ] ∝ β̃ := ∂_vy/∂_xy,
  the integrated twist, ≈ ∫_{−10}^u ∂_vb du′ along the generators. The deformation moves to the L-row.
- In the X-adapted frame, L = √cΩ(e₀ + e₁) and L̲ = (Ω/√c)(e₀ − e₁). So the L̲-row is weighted by √c/Ω and the L-row by
  1/(√cΩ): moving the deformation costs |β̃|/(c|b|), with c = f(1.1)/2 = 0.087 at u\*.
- On the approximant (`comoving.py`), the frame-weighted orbit–leaf size is 0.445 (current) against 1.354 (co-moving
  with L̲) at the maximum, and 0.30 against 0.78 on u ≤ −1.3. That is 3× worse.
- **The double-null angle is the better co-moving choice near u\*.** Transport the angle along L + θ(L̲ − L)-type
  combinations, so a fraction θ of the twist moves to the L-row. The two rows then scale as (1 − θ)·0.445 and θ·1.354,
  and their Frobenius combination is least at θ ≈ 0.10, where it is 0.42: **a 5 % gain** (computed from the two
  endpoint estimates, assuming the linear dependence on θ that holds to first order).

**Conformal-Killing approximants of the leaf metric (examined; not constructed).**
- The leaf–leaf block, where such fields would help, is not the dominant block at the maxima of π^E (1.59 of 3.04).
- Making E_ab approximately conformal Killing for each leaf's metric means a correction δE = Σ_k c_k(u, v)W_k, fitted
  leaf by leaf. Its (u, v)-derivatives feed back into the orbit–leaf block.
- An upper bound on what any change of the angular fields could buy in the same-level term is the computed
  "orbit–leaf block removed" row of §G0b.3 (diagnostic only, not a construction).

**Conclusion.** Keep E_ab in the double-null angle. No better rigorous choice was found, and the obvious alternative is
worse by a factor of 3 where it matters.

## G0b.3 Lever 2: careful commutator counts (rigorous replacements, computed)

The crude level-3 coupling of G0 is replaced as follows; each item says why it is rigorous.

1. **Exact first-order commutator map.** P₁^Z : ∇Ψ ↦ −ĝ^{αβ}Γ′^ρ_{αβ}∇_ρΨ − 2ĝ^{αβ}(Γ′^ρ_{αμ}∇_βΨ_{ρν} + Γ′^ρ_{αν}∇_βΨ_{μρ}),
   with Γ′ = ½ĝ⁻¹(∇π^Z + ∇π^Z − ∇π^Z). This is the first-order part of −DL_ĝ[π^Z] (§3.2 of G0), written as a 15 × 75
   matrix in the frame; its exact spectral norm is used.
   *Rigorous:* |P₁∇Ψ| ≤ ‖P₁‖|∇Ψ| is the definition of the norm. L7 certifies an upper bound.
2. **Exact zeroth-order commutator map.** P₀^Z : Ψ ↦ −ĝ^{αβ}(∇_αΓ′^ρ_{βμ}Ψ_{ρν} + ∇_αΓ′^ρ_{βν}Ψ_{μρ}) + 2(D𝓡[π^Z])Ψ,
   with D𝓡[δ] the exact variation of 𝓡 = Riem·Ψ − ½(Ric∘Ψ + Ψ∘Ric). It includes the variation of the index raising,
   δRiem = ∇Γ′ − ∇Γ′, and δRic = ∇Γ′ − ∇(tr Γ′). It is a 15 × 15 matrix with exact spectral norm.
   - It pairs |Ψ_{j−1}| with ∇₀Ψ_j, so it is paid by the zeroth-order fluxes and not by gradients, as G0's isotropic
     bound assumed.
3. **∇π^E and ∇²π^E computed, not estimated (G0 used 3|π^E|).**
   - In coordinates, the components of E_ab and of π^E lie in span{cos φ1, sin φ1} ⊗ span{cos φ2, sin φ2}. Hence
     ∂_{φ1}π^E(φ) = π^E(φ1 + π/2, φ2), ∂²_{φ1}π^E = −π^E and ∂_{φ1}∂_{φ2}π^E = π^E(φ1 + π/2, φ2 + π/2), exactly.
   - The (u, v, x)-derivatives come from exact jets of order 3.
   - Controls (computed, `t_l3b.py`):
     - on the seed every π, ∇π, ∇²π, P₁ and P₀ vanishes to 10⁻¹²;
     - on the approximant, |π^T|, |∇π^T| and Σ|π^E|² agree to rounding with G0's independent code.
4. **Second-commutator principal terms.** At level j ≥ 2, ℒ_{Z₁}(DL[π^{Z₂}]Ψ) contains −(ℒ_{Z₁}π^{Z₂})·∇²Ψ, an
   adjacent-level coupling after recovery.
   - Bound: |ℒ_Zπ| ≤ |Z||∇π| + 2|∇Z||π|, since ℒ_Zπ = ∇_Zπ + π(∇·Z, ·) + π(·, ∇·Z).
   - |∇Z|_k is measured: ≤ 1.41 (T) and ≤ 2.19 (E_ab) at seed 1; 0.93 and 1.78 at seed 2 (computed, `gradZ.py`).
     The global maximum is used, with multiplicity 2 (at most two such terms per field at level 3).
5. **Direction-resolved recovery for the same-level term.** Replace K_rec π_tot by
   c^Z := |X|^{−1}(|π_{·0}| + |π_{01}| + |π_{11}|) + λ_M^{−1/2}(|π_{·J}| + |π_{J1}| + √3|π_{11}|),
   summed in quadrature over Γ.
   *Rigorous:* this is Lemma F3.1 applied direction by direction to Σ_{AB}π^{AB}∇_A∇_BΨ with Cauchy–Schwarz on each
   column. Column 0 is recovered from ℒ_T; columns 2–4 from the E's; column 1 by commutation (A ≠ 1) or by the
   equation (11).
6. **Two items are not computed.**
   - (a) The terms coupling non-adjacent levels: two derivatives on π, ∇R̂iem·π. They come with a factor μ (not √μ) in
     the level-weighted Young inequality, and are covered by a 50 % margin on ‖P₀‖ (deduced, not computed).
   - (b) The sup over φ of the non-T²-invariant operator norms is taken over two phases. The quadratic sums
     Σ_E|π^E|² and Σ_E|∇π^E|² are T²-invariant exactly. L7 must take the sup on φ-boxes, or use the T²-invariant
     Frobenius sums, which lose ≤ √15.

**What the careful count changes (computed, small test grid, seed 1 D\*).**
- Same-level coefficient: median 0.06, max 5.4, against 0.24 and 6.7 (K_rec π_tot).
- First-order cross coefficient ‖P₁‖: median 1.0, max 29.
- Zeroth-order ‖P₀‖: median 2.7, max 79.
- G0's isotropic cross coefficient was 9.4·2·(|∇π^T| + 3|π^E|): median 13, max 268.
- The computed |∇π^E| reaches 12.1, larger than G0's estimate 3|π^E| at the maximum, but smaller in the median.

## G0b.4 Seed 2 (λ = 10^{−1/2}; computed)

**The provisional approximant.** It is built exactly as for seed 1 (G0 §6.3): the record's dnsolve5.py with the
record's data at λ = 10^{−1/2}, A = 1, on u ∈ [−10, −1.05], v ∈ [0, 3.6], with M = 16 at 132/264/528 rows and M = 24 at
264. It is the Richardson combination, Chebyshev-interpolated at degrees 40 × 48 (`fit_seed2.py`, `appC2_*.npz`).

**How far it can be trusted.**
- *Convergence.* Second order: difference ratios 3.7–4.0 in every field and region, including [−1.3, −1.1] × [2, 3.5].
- *Angular.* M = 24 against M = 16: ≤ 1.6 × 10⁻⁵ in m and ≤ 3 × 10⁻⁶ in s over D\*. This is much better than seed 1
  (5 × 10⁻³ in s). It agrees with rem:tl5-runs: the two coarser angular resolutions agree to v ≈ 3.5 (record).
- *Ricci residual of the fit.* Median 6 × 10⁻⁷, max 8.5 × 10⁻⁵ (at (u\*, ½)). The plain 528 run reaches 1.1 × 10⁻³.

**The geometry.**
- The wave's peak curvature is higher than at seed 1 (|Riem| ≤ 22.1 against 18.3; seed 4.8).
- But it is narrower in v, and the field amplitudes and the shift are much smaller: max |m| 0.12 against 0.47, and
  max |s| 0.76 against 6.07.
- The median curvature excess on the strip u ≥ −1.3 is 1.84 against 3.27 (all computed, `curvcmp.py`).
- The level-0 rates integrate these extended quantities, so seed 2's constants are lower:
  log₁₀F₀²(D\*) = 10.98 against 12.67.
- Same-level level 3: 11.61 against 16.50. This follows from seed 2's smaller deformation of the seed's Killing fields.

**The zeroth-order weights are seed 1's** (like for like, not re-optimised). Re-optimising for seed 2 could only lower
its numbers.

## G0b.5 The sweep with the careful count (computed; both seeds; D\* approximants restricted to u ≤ u\*)

| u\* | seed | L0 | L3 same: G0 count | L3 same: careful | the same, orbit–leaf removed (diagnostic) | L3 full (μ\*) | μ\* | log₁₀F₃²G | floor log₁₀F₃²G | log₁₀M₁ | log₁₀M_w (μ) | G0 log₁₀F₃²G |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| −2.00 | 1 | 6.72 | 9.29 | 7.33 | 7.24 | 8.08 | 10^-4 | **17.62** | 10.87 | 18.22 | 12.63 (10^-3) | 20.55 |
| −2.00 | 2 | 6.02 | 6.76 | 6.17 | 6.15 | 8.06 | 10^-3 | **16.10** | 9.71 | 16.70 | 11.76 (10^-3) | — |
| −1.50 | 1 | 8.07 | 11.51 | 9.07 | 8.91 | 10.03 | 10^-4 | **19.60** | 12.64 | 20.20 | 13.72 (10^-3) | 23.64 |
| −1.50 | 2 | 7.11 | 8.08 | 7.35 | 7.33 | 7.96 | 10^-4 | **17.53** | 10.92 | 18.13 | 12.46 (10^-3) | — |
| −1.30 | 1 | 9.42 | 13.85 | 10.99 | 10.72 | 12.19 | 10^-4 | **21.77** | 14.58 | 22.38 | 14.96 (10^-3) | 25.99 |
| −1.30 | 2 | 8.23 | 9.45 | 8.57 | 8.54 | 9.30 | 10^-4 | **18.88** | 12.15 | 19.48 | 13.22 (10^-3) | — |
| −1.20 | 1 | 10.38 | 15.54 | 12.45 | 12.08 | 13.82 | 10^-4 | **23.42** | 16.04 | 24.02 | 15.80 (10^-4) | 27.82 |
| −1.20 | 2 | 9.04 | 10.46 | 9.45 | 9.41 | 10.27 | 10^-4 | **19.86** | 13.05 | 20.46 | 13.79 (10^-3) | — |
| −1.10 | 1 | 12.67 | 20.04 | 16.50 | 15.83 | 18.37 | 10^-4 | **28.05** | 20.17 | 28.65 | 17.99 (10^-4) | 32.66 |
| −1.10 | 2 | 10.98 | 12.99 | 11.61 | 11.56 | 12.66 | 10^-4 | **22.33** | 15.28 | 22.93 | 15.27 (10^-3) | — |


Reading the table:
- **The same-level term.** The careful count lowers it by 0.6–1.4 decades at seed 2 and by 2.0–3.5 at seed 1.
  Removing the orbit–leaf block of π^E entirely would lower it by only 0.02–0.67 more (diagnostic upper bound for
  lever 1).
- **The cross-level part.** Full minus floor is 6.4–7.9 decades at every u\*. Of this, 4.5–6.0 is μ^{−3/2}
  (μ\* = 10⁻³–10⁻⁴) and 0.6–1.9 is exponential.
  - The careful coefficients are an order of magnitude smaller than G0's in the median (test grid: ‖P₁‖ 1.0 and ‖P₀‖ 2.7
    against 13), and comparable at the maxima once the second-commutator terms are added.
  - They move μ\* at D\* from 10⁻⁵ to 10⁻⁴, which saves 1.5 decades of the polynomial factor.
- **M_w sits 4.9–10.7 decades below M₁**, the factor F of G0 §8, as before.


## G0b.6 What L1, L6 and L7 must certify, with target accuracies (deduced; targets from the computed multipliers)

**The closing structure fixes the targets.**
- Weighted: Ξ_w = M_w(δ_w + 2ε_w) < 1, with A_w = δ_w + 2ε_w and B_w = c_NL S_F^{NL}μ^{−3/2}.
- Single domain: Ξ₁ = M₁(δ + 2ε_r) < 1.
- Ask for **a margin of 10** (Ξ ≤ 0.1), and split the budget as δ ≤ ε, so δ + 2ε ≤ 3ε.
- Then **ε ≤ 1/(30M)**, where M is M_w (weighted) or M₁ (single), taken from §G0b.5 at the chosen μ.

**The residual conversion under the μ-weights.**
- The level-3 norms weight Γ^I-derivatives by μ^{|I|/2} in amplitude. At μ ≈ 10⁻⁴–10⁻⁵, the residual's derivatives,
  which vary on the wave's scale with |Γ| ≲ 10, contribute (10μ^{1/2})^j ≤ 0.1^j.
- So ε at level 3 is the level-0 norm within 10 %: **ε ≈ 2.5 × 10² f over D\*** (231 f at level 0, computed, plus 10 %),
  where f is the pointwise residual bound in units of the curvature scale (eq:tl5-residual).
- This replaces G0's factor 2 × 10³, which ignored the μ-weights; the μ^{−3/2} is already in G.
- **Hence f ≤ 1/(7.5 × 10³ M)**: log₁₀f_target = −log₁₀M − 3.9.

### L1: data on N₀ ∪ N₁ (certified ODE enclosures)

1. **N₀ (v = 1/2): the seed.**
   - The approximant must agree with the seed on N₀ together with its v-jets of order ≤ 3, which is possible since the
     solution is C³ across v = 1/2. Then every Ψ_I = Γ^I h vanishes on N₀.
   - This is a construction (the affine/polynomial correction of eq:cone-approximant extended to the 3-jet), not an
     enclosure.
   - Target: exact. Any mismatch is added to δ at the same budget as N₁.
2. **N₁ (u = −10).**
   - (a) The free data: W, P, Q of eq:cone-data and R of prop:cone-exact, as Chebyshev enclosures in r. The chapter's
     method gives 10⁻³⁰ at degree 80.
   - (b) The shift β from Ric_vx = 0 along each generator: a linear ODE with zero data at v = 1/2.
   - (c) The wave-gauge components g_{uu}, g_{uv}, g_{ux} on N₁ from Υ = 0 restricted to N₁ (transport ODEs along v).
   - (d) **The transversal derivatives ∂_u^k g_{μν} on N₁ for k ≤ 3.** These come from the reduced equation and its
     u-derivatives restricted to N₁ (a triangular hierarchy of linear transport ODEs along the generators), together
     with the x-derivatives they require (≤ 3 + 3).
   - (e) The T²×reflection symmetry of all of these, by construction.
3. **Output: δ_w** := the level-3, μ-weighted flux of ĝ − g on N₁, with weight e^{−B(v)}, enclosed.
   - **Target: δ_w ≤ 1/(30M)**:
     - D\* (weighted): ≈ 10^{−(log₁₀M_w + 1.5)};
     - D_A (weighted): ≈ 10^{−(log₁₀M_w(D_A) + 1.5)};
     - the numbers are in §G0b.5.
   - Since δ is built from transversal derivatives up to order 3, the Chebyshev degree in r for (d) must carry about
     three orders more accuracy than (a).
   - Cost: minutes of interval arithmetic per generator family (S-H123 §7).

### L6: the approximant's residual in the level-3 norm

1. **The approximant.**
   - A spectral-element approximant on D (D\* or D_A), equal to the seed's 3-jet on N₀ and to the L1 data (with
     transversal jets to order 3) on N₁ up to δ.
   - Precision as required below: double-double for D_A weighted; quad-double for D\* weighted.
   - Its coefficients are shipped by md5 (Appendix B prints the procedure, not the coefficients).
2. **The certified quantity.**
   - ε_w := ‖2Ric(ĝ)‖_{𝒩,φ}, i.e. ∫du ‖Ω²e^{−φ/2}·2Ric‖_{L²(C_u)} + ∫dv ‖√cΩ²e^{−φ/2}·2Ric‖_{L²(C̲_v)}, at level 3 with the
     μ-weights.
   - Equivalently, and more simply for the certificate, a pointwise bound f on |Γ^I Ric(ĝ)|·μ^{|I|/2}·R⁴/√72 over D,
     times the computed conversion 2.5 × 10².
   - Method (S-H123 §4.3): Chebyshev interpolation of the residual at (2n)³ nodes per element, ball arithmetic at the
     nodes, a polyellipse analyticity bound (the chapter's lem:cone-ellipse extended to three tensor factors), and
     coefficient sums for the Γ-derivatives (lem:tl5-chebyshev).
3. **Target: f ≤ 1/(7.5 × 10³ M)**. See §G0b.5 for the numbers; on G0b's figures this means double-double for D_A
   (weighted) and quad-double for D\* (weighted).
4. **The corner (u\*, 7/2) is the hardest place.**
   - It is where the provisional approximant's residual is largest (4 × 10⁻³ at seed 1, 5 × 10⁻⁵ at seed 2).
   - It is where the angular truncation dominates (seed 1).
   - The element map should refine there, and in x near x = −1 at seed 1, where the shift is large.

### L7: the rates, on boxes, with margin

1. **The objects.**
   - Piecewise-linear a_o(u), a_i(v) on a partition (the LP's output, inflated by the margin).
   - The zeroth-order weights z_L, z_L̲: explicit, 6 parameters, fixed at the LP's values.
   - The multiplier X = T.
   - The level weight μ.
2. **The inequality to certify on every box Q of a partition of D (sup over x ∈ [−1, 1], and over φ where the
   commutator norms are not T²-invariant):**
   a_o E_o + a_i E_i − (𝔅_{Sym²} + 𝔅_same + √μ 𝔅_cross) ⪰ 0, by an LDLᵀ test on interval enclosures of the entries.
   - The entries involve the 2-jet of ĝ (𝔅), the 3-jet (π^Z, ∇π^Z, Γ′, ∇Γ′, hence ‖P₁‖ and ‖P₀‖) and the 1-jet of the
     weights.
   - ‖P₁‖ and ‖P₀‖ need certified upper bounds for spectral norms: Frobenius norms are certified directly and lose at
     most √15. Gershgorin/LDLᵀ on PᵀP is the cheaper certified route.
3. **Margin and its cost.**
   - The rates enter F² as e^{A+B}, and the weighted closing as e^{(A+B)/2}.
   - A uniform slack of 5 % in the rates costs 0.05(A + B)/ln 10 decades: about 0.9 decades in F₃² at seed 1's D\*
     (A + B ≈ 42 at level 3, computed), and 0.45 in the weighted closing.
   - **Target: certify the rates to within 5 %.**
4. **Box count.** The rates vary on the wave's scale (λ = 1 at seed 1, 10^{−1/2} at seed 2) and on the near-horizon
   scale (≈ 0.03 in u near u\*: the 2-piece chain's second strip).
   - With order-1 Taylor models, about 10⁴–10⁵ boxes per seed for D\*, as S-H123 estimated. Hours of ball arithmetic.
   - The x-direction needs boxes down to the axes; the entries are smooth there.
5. **The other constants to certify.**
   - C_S (§5 of G0): the sup of an explicit product, including C_{S³}(R) as a convergent Legendre sum with an explicit
     tail.
   - S^{NL} and S_F^{NL}: integrals of explicit functions with the certified a_o, a_i.
   - The term counts c_Q, c₁, c₀, c_R: written out in L4–L5, no numerics.
   - Target 10 % each (they enter linearly).

### The targets in numbers (computed from §G0b.5; margin 10; ε ≈ 2.5 × 10² f; δ ≤ ε)

| target | weighted: δ_w ≤ | weighted: f ≤ | single domain: f ≤ |
|---|---|---|---|
| seed 1, D\* | 10^{−19.5} | **10^{−21.9}** (quad-double) | 10^{−32.5} |
| seed 1, D_A | 10^{−14.1} | **10^{−16.5}** (double-double) | 10^{−22.1} |
| seed 1, u\* = −1.2 | 10^{−17.3} | **10^{−19.7}** (double-double, upper end) | 10^{−27.9} |
| seed 2, D\* | 10^{−16.8} | **10^{−19.1}** (double-double, upper end) | 10^{−26.8} |
| seed 2, D_A | 10^{−13.2} | **10^{−15.6}** (double-double) | 10^{−20.6} |

The rates (L7) are to be certified to 5 %, and C_S, S^{NL} and S_F^{NL} to 10 %.

## G0b.7 Caveats, and what would still move seed 1's D\*

1. **Two items are estimates, not computations** (§G0b.3 item 6): the non-adjacent-level terms (a 50 % margin on ‖P₀‖)
   and the sup over φ (two phases). A factor 2 in the cross-level coefficients moves the result by about 0.9 decades
   through the μ-optimum (deduced: cost ≈ 3 log₁₀R_x + O(1)).
2. **The second-commutator term uses the global maxima of |∇Z|** (2.2 and 1.8). A pointwise |∇Z| would lower it. The
   version with |∇Z| ≤ 1 gives seed 1 D\* within 0.1 decade of the stated figure (computed: final2_s1.out against
   final3_s1.out at u\* = −2, −1.5).
3. **G0's caveats stand.** The provisional approximants are scoping objects. G (C_S) is a conservative product. Floating
   point and sampled grids are used throughout. Seed 2's weights are seed 1's.
4. **Next levers for seed 1's D\*, in order** (deduced, untested):
   - (i) bound |∇²h|_∞ by Gagliardo–Nirenberg interpolation between levels 2 and 3 on the cones. This replaces
     μ^{−3/2} by about μ^{−5/4} or less, worth about 1–3 decades;
   - (ii) re-optimise the zeroth-order weights with the level-3 bulk form (they were optimised at level 0);
   - (iii) a pointwise |∇Z|;
   - (iv) level-dependent μ_j.
   - Together, plausibly 2–4 decades. That would bring seed 1's D\* to or below the GO line, but it has not been shown.

## G0b.8 Files (all under `scratchpad/g0/`)

| file | what |
|---|---|
| `lvl3b.py` | careful level-3 data: π^Z, ∇π^Z, ∇²π^Z for T and E₁₃…E₂₄ (φ-derivatives by exact phase shifts); Γ′, ∇Γ′; exact spectral norms of P₁ (15 × 75) and P₀ (15 × 15, with the exact variation D𝓡); direction-resolved same-level coefficient; orbit–leaf diagnostic |
| `t_l3b.py` | controls: everything vanishes on the seed; agreement with lvl3.py on π^T, ∇π^T, Σ\|π^E\|² |
| `piblocks.py` | block structure of π^E and π^T; the shift |
| `comoving.py` | the co-moving-with-L̲ estimate |
| `gradZ.py` | \|∇T\|_k, \|∇E_ab\|_k |
| `final2.py`, `final3.py`, `final2_s*.out`, `final3_s*.out`, `final3_s*.json`, `cdb_s*.npz` | the re-evaluation (final2 with \|∇Z\| ≤ 1; final3 with the measured \|∇Z\|), both seeds, the u\* sweep, the μ-trade, M₁, M_w |
| `runs/d2_*.npz`, `runs/d2_*.log`, `fit_seed2.py`, `appC2_*.npz` | seed 2's provisional approximant |
| `curvcmp.py` | curvature, field and shift magnitudes, seed 1 against seed 2 |
| `b_*.md` | this report's parts |
