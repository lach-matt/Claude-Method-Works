# S-T6: low regularity for the characteristic problems (C³ data, measure-valued null-dust shells)

This is a scoping report for the writer. I edited nothing under `reader/`, and I did not run `assemble.py`.
Scratch work and computer-algebra scripts are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/st6/`.

**What I read.**
- notes/reports/S-CIVP.md (all of it) and S-T3.md (the summary and §§5–6).
- Chapter 87: lines 1–20, 68–142, 429–440, 492–620 and 1148–1254. Chapter 03: 40–60. Chapter 01: 95–125.
  Chapter 90: 10–30 and 195–230. Chapter 95: 455–470. Chapter 83: 1–72. Chapter 81: 140–168, 540–600 and 895–905.
  Chapter 80: the label list.
- proofs/P-CIVP.md (Tier 1): lines 36–95, plus the label list.
- proofs/P-CIVP2.md (Tier 2): lines 1–52, 390–480 and 575–601.
- proofs/P-F123.md: lines 1–12, 150–330, 500–560, 660–800 and 870–904.
- The writer's report reader/reports/P-F123.md, all of it.
- reader/reports/S-H123.md: 1–120 and 300–346.

The three files P-CIVP, P-F123 and S-H123 did not exist when this work started. They appeared during it, and this
report takes them into account.

---

## Summary

- **C³ is not an obstruction for chapter 87, and no finite-regularity theory is needed.**
  - lem:tl5-continuation starts at v = 1/2: N₁ = {u = −10, 1/2 ≤ v ≤ v\*}.
  - The envelope sin⁴(π(v − 1/2)/3) is, on [1/2, 7/2], the restriction of an entire function. Chapter 87 already uses
    this fact in lem:cone-ellipse.
  - Hence, for u\* < u₀ and v\* ≤ 7/2, the data of def:tl5-problem restricted to N₀ ∪ N₁ are **smooth data in the gauge**:
    - P, Q and W are analytic up to the ends;
    - R solves an analytic linear ODE there;
    - the shift β is smooth by lem:tl5-cip-shift.
  - So P-F123's thm:tl5-cip, which proves (F1)–(F3), applies to them as it stands.
  - The C³ junction sits at the corner, between the seed's region D⁰ and D. There, a finite-order reading of P-F123's
    own lem:tl5-cip-jets (a) glues the two pieces into a solution of def:tl5-problem of class C^{3,1}. Its fourth
    v-derivative jumps across {v = 1/2}.
  - For v\* > 7/2 the problem is solved in two smooth stages, glued the same way at v = 7/2.
  - S-H123 §6 reached the "two smooth stages" conclusion independently. This report supplies the gluing proof, the
    regularity counts behind it, and the edits that follow.
- **Every literature route with isotropic regularity fails at C³, symmetry or not.**
  - [CCTW16, Theorem 3.9] needs ℓ > (n+9)/2 derivatives along the generators: ℓ ≥ 7 in 4+1, and ℓ ≥ 6 in the T²-reduced
    2+1 system. These are counted on first-order or curvature-level fields, so the metric data need C⁷ to C⁹. C¹
    solutions, the uniqueness class, need about C¹³ to C¹⁵.
  - [CTG23]'s "suitable Sobolev spaces" inherit these counts.
  - In wave gauge (Rendall plus Kato, s > 3 on ℝ⁴) the Cauchy part would accept the conormal C^{3,1} data, which lie in
    H^{9/2−}. But the passage back to double-null form loses one or two derivatives [CCTW16, p. 40; CTG23, p. 2].
  - The continuation criterion (F3) is known only for smooth data [CCTW16, Theorem 3.15 and p. 37].
  - The reduction to 2+1 lowers these thresholds by one derivative only, because the "+9" losses dominate.
  - Anisotropic double-null theories (Luk–Rodnianski) need only a Lipschitz metric along the generators. They exist in
    3+1 only.
- **Mollification is not needed.** It changes the problem, invalidates lem:cone-ellipse and all the certified tables
  for the sin⁴ envelope, and buys nothing for existence. It remains the author's call (§2).
- **Measure-valued shells.**
  - *Shells along leaves {v = c} or {u = c}, finitely many, with densities smooth in angle: GO.*
    - The same slab-gluing works, with a null-shell lemma in the class gauge, a Barrabès–Israel junction.
    - By computer algebra, the singular part of Ric is exactly −(3/R)[∂_vR] δ(v − c) dv ⊗ dv once the torsion jump
      [∂_vβ] vanishes.
    - That jump obeys a homogeneous transport equation along the shell.
    - The jump of R²∂_vR obeys exactly the null-dust conservation law. So a glued metric is a distributional
      Einstein–null-dust solution with a shell, plus possibly an impulsive gravitational wave.
    - Cost: 400–700 lines on top of Tier 1 or Tier 2.
  - *General angularly regular measures (the [LR20] class): NO-GO with the paper's tools.* They need a T²-reduced
    Luk–Rodnianski theory: a separate paper, 2,500–4,000 lines, high risk.
  - The round case (1+1) with measure-valued 𝒜 and ℬ is elementary. Its crossing rule, a five-dimensional
    Dray–'t Hooft–Redmount identity, follows in one line from f = −2e^{−2σ}R_uR_v.
- **Effect.**
  - *Chapter 87.* Three texts in P-F123's placement must change, because they name C³ as an obstruction it is not:
    rem:tl5-cip-regularity, the new rem:tl5-beyond, and the new chapter 90 paragraph. Also, P-F123's optional
    lem:tl5-continuation-ck is not needed, and the remaining obstruction is (H1)–(H3) alone.
  - *Chapter 83.* Nothing is needed for its smooth data. The optional shell theorem would refine
    rem:loc-cone-scope (iii) and rem:civp-large-domain.

---

## 1. C³: thresholds and route

### 1.1 What the data actually are

- env(v) = sin⁴(π(v − 1/2)/3) on [1/2, 7/2], and 0 outside. Its fourth derivative jumps by 4!(π/3)⁴ = 8π⁴/27 at
  each end, as rem:envelope-regularity says.
- Near each end env ≈ c(v − 1/2)₊⁴. So env ∈ C^{3,1} = W^{4,∞}, it is piecewise analytic, and it lies in H^s_loc
  exactly for s < 9/2. "C³" understates it.
- **Angular regularity.** P and Q of eq:cone-data are polynomial in x times h(x) = (2/(1 + x²))^{1/2}. They are
  analytic in x, axes included; the axis conditions 2P + Q = 0 at x = −1 and P + 2Q = 0 at x = 1 hold by construction.
  So the only roughness is in v, on the two leaves v = 1/2 and v = 7/2 of N.
- **Regularity in v on all of N.** This sharpens P-F123, which states C² for R and β.
  - A = (φ cos θ)′ and B = (φ sin θ)′ are C^{2,1}. So w of eq:cone-w is C^{2,1}, and by eq:cone-ode R ∈ C^{4,1}.
  - 𝔣 of eq:tl5-cip-shift is C^{2,1}. So R³e^{−2W}G_x∂_vβ ∈ C^{3,1}, and β ∈ C^{4,1}.
  - W is smooth.
  - So every datum is C³ (in fact C^{3,1}) in v across v = 1/2 and v = 7/2.
- **On each closed stage the data are analytic.**
  - On [1/2, 7/2], φ and θ are analytic in r, one-sided at r_s and r_e.
  - R solves eq:cone-ode with analytic coefficients, with R = r_s and ∂_rR = 1 at r_s.
  - β comes from lem:tl5-cip-shift with smooth γ and W, and b_S = ζ_S = 0 at the corner.
  - On [7/2, ∞), env = 0, so P = Q = 0, s = 0, R is affine in r, and β solves a smooth ODE.

### 1.2 Thresholds of the tools named in the brief (all read at the pages cited, §4)

| Route | Setting | Needed along the generators | Angular | Output | C³ data? |
|---|---|---|---|---|---|
| [CCTW16, Thm 3.9, pp. 32–33] (symmetric hyperbolic, doubly-null) | Y of dim n − 1; 4+1: n = 4 | data in ∩_{0≤j≤ℓ} C^j(H^{ℓ−j}(Y)), **ℓ > (n+9)/2**, so C^ℓ in the null parameter | H^{ℓ−j} | (3.102) ⊂ C^{ℓ₁−1,1} with ℓ − 3ℓ₁ > (n+9)/2; "unique within the class of C¹ solutions" | no |
| [CTG23] frame system in that theorem | fields (4.9)–(4.10), p. 10, include the Weyl components | ℓ ≥ 7 on Weyl-level fields, so metric data ≈ C⁹ for existence; C^{1,1} fields need ℓ ≥ 13, so ≈ C¹⁵ | as above | "suitable Sobolev spaces" (p. 3), no index | no |
| T²-reduced 2+1 system (P-CIVP2) in [CCTW16, Thm 3.9] | n = 2, Y = circle, off the axes only | ℓ ≥ 6 on connection-level fields, so metric data ≈ C⁷; C^{1,1} fields need ℓ ≥ 12, so ≈ C¹³ | as above | as above | no |
| Rendall's reduction plus Kato's theorem on ℝ⁴ (wave gauge) | 4+1 | Cauchy part s > 3; C^{3,1}-conormal data are H^{9/2−} | jets cost 2 angular derivatives per order | H^s in wave gauge, but double-null components lose 1–2 derivatives [CCTW16, p. 40; CTG23, p. 2]; C² double-null components need about H^{5+} or H^{6+} | no |
| Finite-regularity continuation (F3) | any | — | — | "it is not clear whether such a result can be established" [CCTW16, p. 37] | no |
| Luk–Rodnianski anisotropic double null [LR15, Thm 2; LR17, Thm 2; LR20, Def 4.5] | **3+1 only** | metric Lipschitz along the generators (χ̂ ∈ L^∞), or W^{1,2} (χ̂ ∈ L²); measures for the dust | 3–6 angular derivatives | Lipschitz or C⁰ ∩ W^{1,2} weak solutions | yes, with large margin, but no 4+1 theorem |
| Piecewise smooth, glued by finite-order jets (this report) | 4+1 class, any n | smooth on closed slabs, C^q (q ≥ 2) at finitely many break leaves | smooth | C^q, smooth on each slab | **yes: the data of def:tl5-problem** |

Notes on the table:
- The "metric data ≈ C^…" entries are counted from the stated theorems. They are not optimised. Each first-order field
  costs one metric derivative, and each Weyl field costs two.
- [CCTW16, Remark 3.7] allows real k in the linear estimates, but that does not change the losses.
- The 1+1 case (round data) is not relevant to chapter 87 beyond the seed: the data at v > 1/2 are not round.
- **Conclusion for the brief's question "is C³ enough?"**
  - Not for any finite-regularity route that is on the shelf, in 4+1 or in the 2+1 reduction.
  - Yes for the actual data, by the piecewise route, because they break only on leaves of N.
- **Why the leaves matter.**
  - In the gauge, v is constant on the ingoing null hypersurfaces through the leaves of N₁. The break at v = 1/2 or
    v = 7/2 therefore lies on a characteristic hypersurface {v = c} of the solution itself.
  - The region {v ≤ c} depends only on data with v ≤ c.
  - The region {v ≥ c} is a smooth characteristic problem with data on {v = c} and on N₁ ∩ {v ≥ c}.
  - This is the mechanism by which [LR15, Remark 9, p. 90] gets smoothness after an impulse, and [LR17, p. 7] notes
    that for "much weaker" conormal singularities classical theory applies.

### 1.3 The gluing lemma (finite-order jets)

P-F123's lem:tl5-cip-jets (a) already allows the two metrics to lie on opposite sides of H = {v = s₀}. Its induction on
the transverse order k uses at step k only the orders below k, and the values at order k on Z = {u = −10, v = s₀}.

**Lemma G (finite order).** In lem:tl5-cip-jets (a), if ∂_v^k g₁ = ∂_v^k g₂ on Z for every k ≤ q, then
∂_v^k g₁ = ∂_v^k g₂ on H for every k ≤ q.
- *Proof:* the induction of lem:tl5-cip-jets (a) stopped at q. One sentence.

**Corollary G′ (gluing).** Let g₋ be smooth on [−10, u\*] × [s₀ − ε, s₀] × S³ and g₊ smooth on
[−10, u\*] × [s₀, s₀ + ε] × S³. Let both be vacuum metrics in double-null form that agree on H. Suppose their
one-sided v-derivatives of order ≤ q agree on Z, which holds when both induce on N₁ data of class C^q at v = s₀. Then
the glued metric is C^q. It is a classical vacuum metric if q ≥ 2, and smooth on each side up to H.
- *Proof:* Lemma G gives agreement of ∂_v^k for k ≤ q on H. Derivatives along H of these functions agree. Together
  these give every mixed partial derivative of order ≤ q.

Independent check, by computer algebra in the class gauge (scripts `ricci_structure.py` and `jets_on_N0c.py`,
`jets_on_N0d.py`):
- Second v-derivatives occur only as ∂_v²R in Ric_vv, with coefficient −3/R.
- ∂_v²β occurs in Ric_vx, with coefficient R²e^{−2(P+Q+W)}/(16(1 − x²)), and in Ric_uv with the same coefficient
  times −β.
- On {v = c} with β = 0, Ric_ux = c₁∂_u∂_vβ + c₂∂_vβ + (tangential terms):
  - c₁ = −R²e^{−2(P+Q+W)}/(16(1 − x²)) ≠ 0;
  - c₂ is a function of the tangential data alone;
  - Ric_ux contains no ∂_v of R, P, Q or W.
- Ric_uv, Ric_11, Ric_22 and Ric_xx contain no x-derivative of a first v-jet of R, P, Q or W. Their ∂_u∂_v-matrix in
  (R, P, Q, W) is invertible, with determinant ∝ R².
- So the transverse jets satisfy a triangular system of ODEs along the generators, as P-F123's proof says.

### 1.4 The route for chapter 87, step by step

1. **Stage 1 (v\* ≤ 7/2).** For u\* < u₀ (lem:tl5-seed (a)), the data of def:tl5-problem restricted to N₀ ∪ N₁ are
   smooth data in the gauge satisfying eq:tl5-cip-constraints (§1.1). thm:tl5-cip gives (F1)–(F3).
   lem:tl5-continuation, in P-F123's smooth form, applies verbatim, with (H1)–(H3) as the only hypotheses.
2. **Junction with the seed.** g₋ = seed on D⁰, which is analytic, and g₊ = the stage-1 solution. On Z = S the
   one-sided v-derivatives agree to order 3 (in fact to order 4 for R, W and β, and to order 3 for P and Q). Corollary
   G′ with q = 3 gives a solution of def:tl5-problem on D⁰ ∪ D. It is C^{3,1}, smooth on D⁰ and on D, and ∂_v⁴(P, Q)
   jumps on N₀. def:tl5-problem asks for C².
3. **Stage 2 (v\* > 7/2).**
   - Data: on N₀′ = {v = 7/2}, those induced by the stage-1 solution, which are smooth from below; on
     N₁ ∩ {7/2 ≤ v ≤ v\*}, the smooth data of §1.1.
   - thm:tl5-cip applies after the translation v ↦ v − 3. The constraints on N₀′ hold because the stage-1 solution is
     vacuum, as in P-F123's proof of (F3).
   - Gluing at v = 7/2: Corollary G′ with q = 3, since the N₁ data are C^{3,1} there.
   - (H1)–(H3) for stage 2 are statements about stage-1's output. S-H123 §6 already notes δ₂ ≤ y₁.
4. **Uniqueness.**
   - Among solutions smooth on each closed stage (and on D⁰): by prop:tl5-cip-unique stage by stage. A stage's data on
     its ingoing face are those of the solution itself.
   - Among all C² solutions of def:tl5-problem: open. prop:tl5-cip-unique needs jets of all orders, and a C² vacuum
     metric is below the H^{3+} threshold at which persistence of regularity is standard. Not needed for existence.

### 1.5 How lem:tl5-continuation should be restated

Three options, in order of preference.

- **(A) No change to the lemma. Add a remark and a corollary.**
  - Keep P-F123's smooth lem:tl5-continuation.
  - Add a remark: for u\* < u₀ and v\* ≤ 7/2, the data of def:tl5-problem restricted to N₀ ∪ N₁ are smooth data in the
    gauge, with the computation of §1.1.
  - Add Lemma G and Corollary G′, with the junction statement of step 2 of §1.4.
  - This covers the whole wave (v ≤ 7/2), which is S-H123's natural target D\* = [−10, −11/10] × [1/2, 7/2].
  - About 60–100 lines.
- **(B) A piecewise-smooth form**, if one statement through v = 7/2 is wanted. Draft:
  - **Lemma (Existence by continuity, piecewise-smooth data).** Let u\* ∈ (−10, 0) and 1/2 = σ₀ < σ₁ < … < σ_m = v\*.
    Let T²-invariant data in the gauge (def:tl5-cip-data) be given on N₀ and N₁: smooth on N₀ and on each
    N₁ ∩ {σ_{i−1} ≤ v ≤ σ_i}, of class C^q on N₁ (q ≥ 2), and satisfying eq:tl5-cip-constraints.
  - A *solution on D_s* is a T²-invariant vacuum metric of the class in the gauge on D_s that induces the data and whose
    components are smooth on each D_s ∩ {σ_{i−1} ≤ v ≤ σ_i}.
  - Let y_σ, A and B satisfy (H1) and (H3) as before, together with:
    - **(H2_pw)** for every k there is C_k such that every solution g on a D_s with y_σ(g) ≤ 2A on [1/2, s] has, on
      each D_s ∩ {σ_{i−1} ≤ v ≤ σ_i}, its components, their one-sided derivatives of order ≤ k, and the components of
      g⁻¹ bounded by C_k in a fixed finite atlas.
  - Then there is a solution on D. It is of class C^q, and y_σ ≤ 2A on [1/2, v\*].
  - *Proof:* (F1)–(F3) for this notion of solution follow from thm:tl5-cip slab by slab.
    - (F1) is stage 1.
    - (F2) holds stage by stage.
    - (F3) inside a stage is thm:tl5-cip (F3). At s = σ_i it is thm:tl5-cip (F1) for stage i+1, glued by Corollary
      G′.
    - The continuity argument is unchanged, except that "I is closed" uses (H2_pw) on the stage containing s̄ from
      below.
  - About 40–60 lines on top of (A).
- **(C) A finite-regularity form (C^k or H^k): not recommended.**
  - P-F123's optional lem:tl5-continuation-ck is correct as an implication, but its C^k versions of (F1)–(F3) are
    established nowhere.
  - At C³ they cannot come from the shelf: §1.2, and [CCTW16, p. 37] for (F3).
  - A single-stage estimate across v = 7/2 can use at most four v-derivatives of the solution, since ∂_v⁵ env has a
    Dirac mass at the ends. Tangential derivatives (∂_u, ∂_x) are unrestricted, because the solution is conormal.
  - S-H123's level-3 norm respects this. But it would need (F1)–(F3) in H⁴, which nobody proves.
  - Recommend dropping item 15 of P-F123, or marking it "not needed: see the stage remark".

### 1.6 The dust problem for chapter 83

- Chapter 83's data are C^∞, so regularity costs nothing there.
- What the two existing tiers require:
  - *Tier 1 (thm:loc-cone-development in P-CIVP).* Smooth data, ε-close in C^m with m = 6k + 21 and k ≥ 6. The proof
    builds a formal solution to infinite order (Borel's lemma) and rests on chapter 81's Kato theory at k ≥ 6, that is,
    at least six derivatives in every direction, the generators included.
  - *Tier 2 (thm:civp-large in P-CIVP2).* [CCTW16, Theorem 3.9] with n = 2 and ℓ ≥ 6 on the 23 reduced fields, so
    metric data ≈ C⁷ along the generators, plus Tier 1's C^m at the corners (prop:civp-large-corner).
  - So **C³ dust data are not covered by either tier in finite-regularity form.**
- **Piecewise-smooth dust data are covered** if they break on leaves: {v = c} on 𝒞_out, {u = c} on 𝒞_in. The slab
  argument of §1.4 carries over, with three remarks.
  - (i) The jets lemma extends with dust. For adapted families T = q_in dv² + q_out du², so T(e₃, ∂_A) = T_AB =
    T(e₃, e₄) = 0, and the lines of eq:tl5-cip-ricci used on {v = c} carry no dust terms.
    - The v-jets of q_in on {v = c} solve ODEs along e₃.
    - Those of q_out are algebraic, since ∂_v q_out = −Θ q_out.
  - (ii) Tier 1 and Tier 2 assume b = 0 on the ingoing face. At a restart face {v = c}, b ≠ 0 in general, so re-gauge
    the angle on the next slab and transform back. prop:civp-large-corner already works with corners at arbitrary
    (u_c, v_c) and b = 0 on N_i.
  - (iii) Tier 1's region shrinks per restart, and so does Tier 2's δ. With finitely many breaks the union still
    contains a future neighbourhood of both cones.
- This is optional: no result of chapter 83 needs it. About 100–180 lines.

---

## 2. Mollification alternative

The alternative is to replace env by a smooth envelope.
- **Either:** a flat surgery near the ends, env_δ ∈ C_c^∞([1/2, 7/2]) with env_δ = env outside
  [1/2, 1/2 + δ] ∪ [7/2 − δ, 7/2] and ‖env_δ − env‖_{C^j} = O(δ^{4−j}).
- **Or:** the envelope env_C of def:lambda0-point and lem:envelope-constant, which has the same support and the same
  ∫env² = 105/128.

Consequences:
- **It changes the problem.** The solutions are different spacetimes for v > 1/2. Convergence as δ → 0 to the
  slab-glued solution is plausible but unproved. It would need a stability estimate in a norm that sees only about four
  v-derivatives, which the literature does not supply for 4+1.
- **It gains nothing for existence.** Existence is unconditional modulo (H1)–(H3) with the original data (§1.4).
  - With env_δ, lem:tl5-continuation applies in one stage for every v\*. That is the only gain.
  - (H1)–(H3) are as hard as before. S-H123's constants are driven by the lower-order coupling, not by the envelope's
    smoothness.
- **thm:main would apply to env_δ**, but only for λ ≤ λ₀(δ).
  - rem:envelope-regularity counts eight derivatives of env in the bounds, so ‖env_δ‖_{C⁸} ~ δ^{−4}, and λ₀(δ) → 0 as
    δ → 0.
  - At 10 l5 thm:main does not apply either way (prop:lambda0).
- **It breaks certified results.**
  - lem:cone-ellipse uses that env is entire on [r_s, r_e]. env_C has essential singularities at the ends (87:140), and
    a flat surgery is not analytic.
  - prop:cone-residual, cor:cone-compare, the tables of sec:cone-tables and the approximants and residual boxes of
    sec:tl5-residuals would have to be re-derived. The latter's region Π lies at v ∈ [0.55, 1.6], inside stage 1.
  - The numerical remarks rem:tl5-runs and rem:tl5-constants would have to be rerun.
  - P-F123's report gives the same cost list.
- **Recommendation:** keep the sin⁴ envelope. Mollification is the author's call only if he wants a single-stage
  statement or a link to thm:main's envelope class. Neither is needed.

---

## 3. Measure-valued shells: route

### 3.1 Which measures

- **[LR20]'s class**, Definition 2.36 (p. 19) and Definition 4.5 (5), pp. 28–29.
  - The class is non-negative Radon measures on each null hypersurface whose angular derivatives up to order six are
    again measures.
  - In T² symmetry this means measures in v whose ϑ-derivatives are measures. Examples: Σ m_i(ϑ) δ(v − v_i) with m_i
    smooth, or ν(dv) ⊗ m(ϑ).
- **A shell on a non-leaf section {v = f(ϑ)} is not angularly regular.** Its support is not a null hypersurface. Such
  shells are excluded here, as in [LR20].

### 3.2 Route M1: finitely many leaf-aligned shells (recommended; GO)

- **The structure, verified by computer algebra in the class gauge.** Scripts: `ricci_structure.py`,
  `shell_numeric2.py`, `density_numeric.py`, `density_out_numeric.py`, `control_*.py`.
  Take a metric of the class that is continuous across {v = c}, smooth on each side, and whose first v-derivatives
  jump. Then:
  - (a) **δ-parts.** Ric has a δ(v − c) part only in Ric_vv, Ric_vx and Ric_uv: −(3/R)[∂_vR]δ in vv, and terms ∝
    [∂_vβ]δ in vx and uv. Jumps of ∂_vP, ∂_vQ and ∂_vW produce no δ in Ric.
  - (b) **Current.** Ric(∂_u + β∂_x, ∂_x) = Ric_ux + βRic_xx contains no first v-derivative of R, P, Q or W. (Tested at
    random rational points, 30 digits.)
    - So for two solutions inducing the same metric on {v = c}, [∂_vβ] satisfies a homogeneous linear transport
      equation along the ingoing generators.
    - It therefore vanishes on the shell if it vanishes on one leaf. This is the no-current condition, j = 0 in
      [Poi02, (2.13)].
  - (c) **Density.** Solve the evolution equations (Ric_uv, Ric_11, Ric_22, Ric_xx) for (∂_u + β∂_x)∂_v(R, P, Q, W).
    Then (∂_u + β∂_x)(R²∂_vR) + (∂_xβ)R²∂_vR is free of first v-derivatives of R, P, Q and W.
    - Hence the jump obeys ∂_u(R²[∂_vR]) + ∂_x(βR²[∂_vR]) = 0.
    - This is exactly the conservation law div(q g⁻¹dv) = 0, that is ∂_u(R³q) + ∂_x(βR³q) = 0, for
      q = μ δ(v − c) with **μ := −(3/R)[∂_vR]**.
    - Negative control: without the compensating terms the expression depends on ∂_vR.
  - (d) **Outgoing shells across {u = c}.** The δ-part sits only in Ric_uu, as −(3/R)[∂_uR]δ. No current condition
    arises, because ∂_v is exactly the outgoing generator (g_vx = 0). ∂_v(R²∂_uR) is free of first u-derivatives, so
    ∂_v(R³μ_out) = 0.
  - These are the Barrabès–Israel quantities in the class gauge [BI91; Poi02, (2.12)–(2.14)]:
    - μ ∝ −σ^{AB}[C_AB];
    - p ∝ [C_λλ], which vanishes in this gauge;
    - j ∝ [C_λA] ∝ [∂_vβ].
    - The δ in the Weyl tensor from [∂_vP] and [∂_vQ] is the "independent impulsive tidal wave" of [Poi02, p. 1].
- **Lemmas.**
  - **MV-0 (round thin shells; extends chapter 80).** Allow the round two-dust system (lem:two-dust-equations) to have
    𝒜 and ℬ equal to a smooth part plus finitely many atoms.
    - R_v jumps by −(1/3)M_i/R² at v_i, by C_v, so R²[R_v] is constant along u, as (c) requires. R_u jumps
      analogously at u_j.
    - Crossing rule: f = −2e^{−2σ}R_uR_v (eq:two-dust-mass), with R_u continuous across ingoing shells and R_v across
      outgoing ones. So the four values of f around a crossing sphere satisfy f₊₊f₋₋ = f₊₋f₋₊.
    - The weak formulation follows [Mos17, Appendix A].
    - Keep the domain off R = 0: by [Mos17, Proposition 1], ingoing dust that reaches the centre breaks the system.
      The paper's inner radius 0.70 already does this.
    - About 60–100 lines.
  - **MV-1 (null shell lemma).** Let g± be smooth class solutions with adapted dusts on either side of {v = c}. Suppose
    they induce the same metric on {v = c}, and [∂_vβ] = 0 on one leaf of it.
    - Then the glued metric is Lipschitz, and [∂_vβ] ≡ 0 on the shell.
    - Ric(g) = (q_in + μ δ(v − c)) dv ⊗ dv + q_out du ⊗ du holds in the sense of distributions, with μ conserved and
      μ ≥ 0 if it is ≥ 0 on one leaf.
    - The same holds for {u = c}, without the condition on β.
    - Proof: (a)–(d), written symbolically. The private numerical checks become a symbolic identity, as P-F123 did for
      eq:tl5-cip-ricci.
    - Distributional curvature is well defined for continuous, piecewise smooth metrics, since Γ ∈ L^∞ and the
      coefficients of ∂² are continuous.
    - About 100–160 lines.
  - **MV-2 (cone data with atoms).** Extend prop:loc-cones and lem:loc-cone-in to q_in = q_reg + Σ m_i(ϑ)δ(v − v_i),
    and likewise on 𝒞_in, with m_i ≥ 0 smooth and supported in the band.
    - Raychaudhuri makes ∂_vϕ jump by a negative amount, so ϕ is Lipschitz. Positivity of e^ϕ is argued as before.
    - In the shift constraint ∂_v(R³e^{−2W}G_x∂_vβ) = 4R³𝔣 (eq:tl5-cip-shift; the second line of eq:loc-cone), 𝔣
      jumps but has no δ when m_i ∈ C¹(ϑ). So [∂_vβ] = 0 at every corner leaf, automatically, and MV-1's hypothesis
      holds.
    - About 60–100 lines.
  - **MV-3 (development on the checkerboard).** The rectangles [u_j, u_{j+1}] × [v_i, v_{i+1}] are smooth
    characteristic problems.
    - Their data are the previous rectangles' solutions on the ingoing and outgoing faces, plus the cone data.
    - Solve each by Tier 1 (small data, around the thin-shell background, which is smooth on each rectangle) or by
      Tier 2 (no smallness), after angular re-gauging (§1.6 (ii)).
    - Glue with MV-1. The perturbation stays in the band by each tier's localisation.
    - Uniqueness holds among solutions smooth on each rectangle.
    - The domain is a neighbourhood of both cones that shrinks with each crossing; it is finite.
    - About 150–250 lines.
  - **MV-4 (edits).** About 30–60 lines; see §6.
- **Go/no-go checks.**
  - **GM-1:** the δ-structure (a). Done here (symbolic, `ricci_structure.out`).
  - **GM-2:** (b)–(d) as symbolic identities. Done numerically here, with negative controls.
  - **GM-3:** Tier 1 and Tier 2 restated around any smooth round two-dust solution on a rectangle, with a corner at
    (u_c, v_c), instead of g0.
    - P-CIVP2's proof uses only that g0 is a smooth round solution in the gauge.
    - Tier 1's proof uses g0's collar (L0) and explicit bounds. Check those.
  - **GM-4:** corner data at a crossing sphere: ∂_uR and ∂_vR are taken from the adjacent rectangles. They are
    consistent by the crossing rule.

### 3.3 Route M2: general angularly regular measures (NO-GO now; separate paper)

Can [LR20], or a T²-reduction of it, give the 4+1 symmetric case?

- **Not directly.** [LR20] is 3+1-specific.
  - It uses Hodge systems and Sobolev on S², and the renormalised Bianchi pairs (β, ρ̌, σ̌, β̲) of 3+1 Weyl curvature.
  - Its existence proof (§9, pp. 73, 84) passes through the low-regularity vacuum theorem of [LR17] and an
    approximation of dust data by vacuum data. That approximation needs the dust to vanish on an open set of angles
    (Proposition 9.1; the hairy-ball restriction of Remark 4.9).
  - S-CIVP §2 already notes that the J terms of [CTG23] (B.6) carry angular derivatives of the densities.
- **A T²-reduced version is plausible and simpler.**
  - Off the axes, prop:reduction leaves 2+1 gravity with two scalar waves and the dusts.
  - In 2+1 the curvature is Ricci, hence matter, so there are no Weyl or Bianchi unknowns.
  - The leaves are curves, so there is no shear and no Hodge theory.
  - P-CIVP2's lem:civp-large-frame states that the connection coefficients obey transport equations "with no angular
    derivative of an unknown on the right".
  - The dust enters only Raychaudhuri, where trχ becomes BV in v. An impulsive wave makes ∂_vψ and ∂_vω bounded with
    jumps.
  - A Luk-type scheme would commute only with ∂_ϑ and estimate ∂_vψ in L² on outgoing cones. The low-regularity
    weak-transport formalism of [LR20, Definitions 2.30–2.31] and the BV traces of [LR20, Lemma 2.24] would be adapted.
- **Plan (separate paper).**
  - Weak formulation in the reduced gauge.
  - A priori estimates in angular H^N (N ≈ 4) with BV control in the null directions.
  - Existence by mollifying the data in v (as [LR20, Proposition 9.2]), Tier 2 for each mollified datum, a uniform
    domain from the estimates, then compactness and passage to the limit.
  - Uniqueness by a difference estimate in a weaker norm (as [LR20, §8]).
  - Localisation off the axes, glued to the explicit round thin-shell background.
- **Go/no-go checks.**
  - **GMV-1:** the reduced wave equations close at angular order N with only BV control of trχ.
  - **GMV-2:** a uniform domain. Tier 2's δ is not bounded by norms of the data (rem:civp-large-domain), so this is
    genuinely new.
  - **GMV-3:** the products in the weak formulation (BV coefficients times measures) are well defined.
  - **GMV-4:** the axes. Either non-round perturbations stay off them, or Tier 3 machinery at H^k, k ≥ 6, is used,
    which is incompatible with measures.
- The same theory would cover general C³ (or C^{0,1}) data that are not piecewise smooth. Chapter 87 does not need
  this.

---

## 4. Literature, verified

Each source was opened and read at the pages cited.

1. **[CCTW16]** Cabet, Chruściel, Tagne Wafo, arXiv:1406.3009v2 (Dissertationes Math. 515).
   - Proposition 3.6 (p. 28): k > (n+7)/2 for the linear iterates. Remark 3.7: real k possible.
   - **Theorem 3.9 (pp. 32–33).** Y is (n − 1)-dimensional; ℓ ∈ ℕ with ℓ > (n+9)/2; data in
     ∩_{0≤j≤ℓ} C^j([0, b₀]; H^{ℓ−j}(Y)); solution regularity (3.102) ⊂ C^{ℓ₁−1,1} with ℓ − 3ℓ₁ > (n+9)/2. "The
     solution f is unique within the class of C¹ solutions, and is smooth if" the data are.
   - Corollary 3.11 and Remark 3.12 (p. 35).
   - Theorem 3.13 (p. 36): ℓ ≥ (n+15)/2.
   - **Theorem 3.15 and p. 37:** a continuation criterion for smooth data only. "One would like to have a similar
     continuation criterion for solutions of finite differentiability class. However, due to the losses of
     differentiability occurring in our argument it is not clear whether such a result can be established."
   - **p. 40:** "after passing to a doubly-null coordinate system one loses one derivative of the metric … This is why
     we will restrict ourselves to dimension four."
   - Theorem 4.1 (pp. 40–41): ℓ > (n+6)/2.
   - Theorem 4.3 (**p. 49**, not p. 48, as P-F123 also notes): ℓ ≥ (n+11)/2. Remark 4.4: data in C^ℓ suffice.
   - p. 50: harmonic coordinates "lead to a loss of derivative of the coefficients".
2. **[CTG23]** Chruściel, Tagne Wafo, Gray, arXiv:2305.07306v1.
   - p. 2: "the transition to such coordinates from harmonic ones can lead to a loss of two derivatives … a tame
     version of these together with the Nash-Moser iteration scheme can be used … We will not provide any details".
   - p. 3: Theorem 1.1, and "the result remains true in suitable Sobolev spaces, as can be checked by chasing various
     losses of differentiability". No index is given.
   - (3.5), p. 7: the off-diagonal angular symbol.
   - (4.9)–(4.10), p. 10: the fields include the Weyl components.
3. **[LR20]** Luk–Rodnianski, *High-frequency limits and null dust shell solutions*, arXiv:2009.08968v1.
   - Abstract.
   - Theorem 1.13 and Corollary 1.14 (p. 6).
   - Definition 2.26 (p. 16); Definitions 2.30–2.31 (p. 18); Definition 2.36 (p. 19).
   - Footnote 20 (p. 23): the original theorems "allow the initial χ̂ and χ̲̂ to be discontinuous".
   - Definition 4.5 (pp. 28–29): Φ Lipschitz with ∂Φ ∈ BV, W^{6,∞} angular, six angular derivatives on the measures.
     "Consistent with the initial null dust being merely a measure, and initial metric being merely C⁰ ∩ W^{1,2}."
   - **Theorem 4.6 (p. 29):** u̲\* ≤ ε, unique angularly regular weak solution.
   - Remark 4.9 (p. 29): the hairy-ball restriction.
   - §9 (pp. 73, 84): the proof via vacuum approximation.
   - 3+1 throughout. Still a preprint.
4. **[LR15]** Luk–Rodnianski, *Local propagation of impulsive gravitational waves*, arXiv:1209.1130v2. It is a journal
   article (Princeton record), but I did not confirm the journal reference: cite it by arXiv number unless confirmed.
   - Theorem 1 (p. 4): a jump of χ̂ across a sphere. α has a δ on the incoming null hypersurface, "smooth away from" it.
   - Theorem 2 (p. 7): χ̂ with three angular derivatives bounded, no e₄-derivative of χ̂ needed. The spacetime is
     "Lipschitz and retains higher regularity in the angular directions".
   - Remark 5 (p. 7): Hughes–Kato–Marsden needs s > 5/2.
   - p. 11: about 2N data derivatives for N derivatives of curvature.
   - Theorem 3 (p. 17).
   - Remark 9 (p. 90): smoothness after the impulse wherever the data are smooth.
   - Propositions 78–79 (pp. 90–91).
5. **[LR17]** Luk–Rodnianski, *Nonlinear interaction of impulsive gravitational waves*, arXiv:1301.1072v2 (Camb. J.
   Math. 5 (2017); journal data as cited in [LR20]'s abstract).
   - Theorem 1 (pp. 6–7): smooth away from the two singular hypersurfaces.
   - p. 7: "Similar problems have been studied for general hyperbolic equations with a much weaker singularity such that
     classical well-posedness theorems can be applied [Beals, Alinhac] … no new singularities appear after the
     interaction of the weak conormal singularities".
   - Theorem 2 (p. 11): χ̂ in L² along the null directions; W^{1,2}.
   - Proposition 52 (p. 86).
   - pp. 3–4: Penrose's and Khan–Penrose's plane-symmetric impulsive solutions.
6. **[Luk18]** Luk, *Weak null singularities in general relativity*, arXiv:1311.4970v3 (journal version not checked).
   - Abstract, pp. 1–5 and 9–13: Theorems 1–4.
   - χ̂ ~ (u̲\* − u̲)^{−1} log^{−p}: Christoffel symbols not in L², metric C⁰ up to the boundary.
   - Relevant only as the far end of the anisotropic scale.
7. **[Mos17]** Moschidis, *The Einstein–null dust system in spherical symmetry with an inner mirror: structure of the
   maximal development and Cauchy stability*, arXiv:1704.08685v1.
   - Abstract; Theorem 1 and Proposition 1 (p. 4): C⁰-inextendibility when ingoing dust reaches the axis.
   - Theorem 2 and the rough norm (4.27) (pp. 20–21).
   - Appendix A (p. 68): the system (A.17)–(A.22) on C⁰ spherically symmetric spacetimes, with τ and τ̄ "regular (and
     non-negative) Borel measures", and Lemma A.1.
   - 3+1, spherical symmetry, Λ < 0, smooth data for the main theorems.
   - arXiv:1812.04274 (massless Vlasov) was not re-read.
8. **[BI91]** Barrabès, Israel, *Thin shells in general relativity and cosmology: the lightlike limit*, Phys. Rev. D 43
   (1991) 1129–1142.
   - **Abstract only** (OSTI record 5835627): it extends the extrinsic-curvature formalism to light-like shells, with
     coordinates chosen independently on the two sides. The full text was not read.
   - The formulas are taken from **[Poi02]** Poisson, *A reformulation of the Barrabès–Israel null-shell formalism*,
     arXiv:gr-qc/0207101, read at pp. 1–10:
     - μ = −(1/8π)σ^{AB}[C_AB], j^A = (1/8π)σ^{AB}[C_λB], p = −(1/8π)[C_λλ], (2.12)–(2.14);
     - S^{αβ} = μkk + j(ke + ek) + pσee, (2.15);
     - the singular Riemann tensor (3.3)–(3.6);
     - [κ] = −8πp, (4.2);
     - the singular Weyl part is "an independent impulsive tidal wave" (p. 1).
   - The derivation uses only the null basis (k, N, e_A), so it is dimension-independent. The class-gauge computation
     of §3.2 does not depend on it in any case.
9. **Internal sources.**
   - P-F123's lem:tl5-cip-jets (a) (opposite sides allowed), thm:tl5-cip, rem:tl5-cip-regularity and item 15.
   - P-CIVP's thm:loc-cone-development and rem:loc-cone-scope (iii).
   - P-CIVP2's thm:civp-large, prop:civp-large-corner and rem:civp-large-domain.
   - S-H123 §6.

**Not used:**
- Rendall 1990, which is paywalled; S-CIVP read it through secondary sources.
- Beals and Alinhac, cited only through [LR17].
- Christodoulou's BV solutions, not opened, so not cited.

---

## 5. Verdicts and plans

### 5.1 C³

**Verdict.**
- **GO for chapter 87, by the piecewise route.** There is no new analysis beyond P-F123.
- **NO-GO for any isotropic finite-regularity route at C³**, whether CCTW, CTG23 Sobolev or Rendall in wave gauge, in
  4+1 or in the 2+1 reduction.
- **Not needed:** a Luk–Rodnianski-type 4+1 theory. That would be necessary only for C³ data that are not piecewise
  smooth.

**Plan for chapter 87.**
1. **L-87.1 (data on the stages).**
   - On N₁ ∩ [1/2, 7/2] and on N₁ ∩ [7/2, v\*] the data are smooth up to the ends.
   - Across v = 7/2 they are C^{3,1}.
   - R and β are C^{4,1} on N, which sharpens P-F123's C².
   - About 25–40 lines.
2. **Lemma G and Corollary G′ (finite-order jets and gluing).** About 15–30 lines, since P-F123 has the induction.
3. **Cor-87 (the solution of def:tl5-problem on D⁰ ∪ D).** It holds under (H1)–(H3) for stage 1, and for stage 2 if
   v\* > 7/2. It is of class C^{3,1} and smooth on each stage. About 20–40 lines.
4. **Optional:** the piecewise lemma of §1.5 (B). About 40–60 lines.
5. **Edits.** About 20–40 lines (§6).

**Go/no-go checks.**
- **GN-87a:** P-F123's induction in lem:tl5-cip-jets (a) uses only lower orders. It does as written, and the
  structure was re-checked by computer algebra (§1.3).
- **GN-87b:** the regularity counts of L-87.1, one line each (§1.1).
- **GN-87c:** R > 0 on N₁ up to v\*: prop:cone-exact (a), and R affine with ∂_rR ≥ 0.967 beyond r_e.
- **GN-87d:** u\* < u₀, so that N₀ ⊂ D_seed (lem:tl5-seed (a)).

**What stays open.**
- (H1)–(H3). This is S-H123's subject, and its plan is unaffected; this report confirms its §6.
- Uniqueness among C² solutions that are not piecewise smooth.
- Data that are C³ but not piecewise smooth (Route M2's theory).

### 5.2 Measure-valued

**Verdict.**
- **GO for finitely many leaf-aligned shells** with angular densities smooth in ϑ, both families, crossings included.
  This covers band-localised perturbations (Tier 1 or Tier 2) and round thin-shell backgrounds.
- **NO-GO now for general angularly regular measures**, and for non-round shells at the axes.

**Plan.**
- MV-0, MV-1, MV-2, MV-3 and MV-4 of §3.2.
- Order: GM-2 symbolic, then MV-1, then MV-0 and MV-2, then GM-3, then MV-3.
- Go/no-go checks: GM-1 (done), GM-2 (done numerically), GM-3 and GM-4.

**What stays open.**
- General measures (Route M2: a separate paper).
- Accumulating shells.
- Uniqueness in a weak class: [LR20, §8]-type estimates are needed.
- Shells non-round at the axes. Tier 3 machinery is H^k, k ≥ 6, slab by slab; this was not checked against S-T3's
  face conditions.
- Thin shells as limits of the paper's smooth-envelope solutions. Tier 1's smallness in C^{6k+21} degenerates as the
  width tends to 0.

---

## 6. Effect on chapters 83 and 87

### Chapter 87 (and P-F123's placement texts)

- **P-F123 rem:tl5-cip-regularity.** "On the data of def:tl5-problem … So no result quoted … gives (F1) for those data,
  and thm:tl5-cip is not stated for them." This should become: for u\* < u₀ and v\* ≤ 7/2, the restriction of those
  data to N₀ ∪ N₁ is smooth and thm:tl5-cip applies. The C³ junctions at v = 1/2 and v = 7/2 are handled by
  finite-order gluing, not by a finite-regularity theory.
- **P-F123's new rem:tl5-beyond** ("[[thm:tl5-cip]] is proved for smooth data, and no result … gives (F1) for data of
  this regularity"). Replace it with a statement that the regularity is no obstruction (stages and gluing), and keep
  the (H1)–(H3) part unchanged.
- **P-F123 item 10 (chapter 90, 212–223):** "the data at 10 l5 are C³ and not smooth, and no result quoted here gives
  even local existence for them". This is incorrect as it stands: (F1) holds for the restricted data. Reword it to name
  (H1)–(H3) as the obstruction.
- **P-F123 item 15** (lem:tl5-continuation-ck): drop it, or mark it as not needed.
- **P-F123's report**, last line ("The obstacles are the C³ data and (H1)–(H3)"): the obstacle is (H1)–(H3).
- **P-F123, after lem:tl5-cip-shift:** "R is … of class C² in v" and "smooth in x and of class C² in v" are true, but C³
  is needed for C³ gluing at 7/2. Use C^{4,1}, or at least C³.
- **New:** L-87.1, Lemma G and Corollary G′, and Cor-87, placed after thm:tl5-cip. Optionally, the piecewise lemma.
- **thm:ten-l5 is unchanged**: existence beyond v = 1/2 still needs (H1)–(H3). If S-H123's plan succeeds, Cor-87 gives
  the new part.
- **(H1)–(H3), for S-H123.**
  - Within a stage, nothing changes.
  - In a piecewise statement, (H2) becomes per-stage (H2_pw).
  - A single estimate across v = 7/2 must use at most four v-derivatives. Tangential derivatives are free.
  - Stage 2's data error is stage 1's output.
- **No effect on** sec:cone-approximant (it lives on N), on sec:tl5-residuals (Π ⊂ stage 1), or on prop:tl5-leaves
  and cor:tl5-mots (they need C²).

### Chapter 83 (and the Tier 1 and Tier 2 texts)

- No change is needed for its smooth data.
- **If the shell theorem is added (MV-3):**
  - Refine rem:loc-cone-scope (iii) and rem:civp-large-domain ("densities that are … measures (shells) are not
    covered") to "finitely many shells along leaves, with angularly smooth densities, are covered
    ([[thm:loc-cone-shells]]); general measures are not".
  - Extend prop:loc-cones (MV-2).
  - Add one sentence to the chapter's opening.
- **Chapter 80 (optional):** MV-0, the round two-dust background with atomic profiles and the crossing rule. thm:main
  and thm:two-dusts are unaffected.
- **Chapter 90:** one sentence each for the stage remark (87) and, if added, the shells (83).
- **Chapters 95 and 98, if M1 is written:**
  - add [BI91] and [Poi02] (attribution of MV-1);
  - [Mos17] optional (MV-0);
  - [LR15] and [LR17] only if they are cited in remarks.
  - [LR20] is present.

---

## 7. Estimate and risks

Sizes are in chapter lines, at about 49.5 per PDF page.

| Piece | Lines | Pages | Risk |
|---|---|---|---|
| 87: L-87.1, Lemma G, G′, Cor-87 and edits | 110–190 | 2–4 | low |
| 87: optional piecewise lemma | 40–60 | ~1 | low |
| 83: piecewise-smooth dust data (optional) | 100–180 | 2–4 | low to moderate (re-gauging, shrinking regions) |
| Shells M1: MV-0 to MV-4 | 400–700 | 8–14 | moderate (GM-3) |
| General measures M2 | 2,500–4,000 | 50–80 | high; separate paper |
| Mollification (if chosen instead) | redo of sec:cone-approximant, the certified tables and sec:tl5-residuals | large | high cost, no gain |

**Risks.**
- **R1 (low): the finite-order jets.** P-F123's induction is order by order. The structure is confirmed by computer
  algebra.
- **R2 (low): the regularity counts on N** (C^{4,1} for R and β). Elementary.
- **R3 (moderate): GM-3.** Tier 1 is written around g0, with the explicit collar L0 and the bounds δ\* and C₀. It must
  be restated around a general smooth round solution on a rectangle with a corner at (u_c, v_c).
- **R4 (moderate): uniqueness classes.** Only "piecewise smooth" uniqueness is available. Uniqueness among C² or
  Lipschitz solutions is open, and the theorems must say so.
- **R5 (structural).** The piecewise route needs breaks on leaves of the data hypersurfaces. General low-regularity
  data, and shells on non-leaf sections, are out of scope.
- **R6 (literature).**
  - [CTG23], [LR20] and [LR15/17] in their arXiv versions; journal references not confirmed except as noted.
  - [BI91] was read in abstract only; its formulas come via [Poi02].
- **R7 (coordination).** P-F123's placement texts named in §6 should be corrected before merge. S-H123's stage-2 plan
  depends on Corollary G′.

**Computer-algebra artefacts** (private; no proof cites them). They are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/st6/`:
- `ricci_structure.py` and `.out`: the second-derivative structure of all eight Ricci components.
- `jets_on_N0c.py` and `jets_on_N0d.py`: the jets on {v = c} with β = 0.
- `shell_numeric2.py`: the current law for general β.
- `density_numeric.py` and `density_out_numeric.py`: the density laws.
- `control_in.py` and `control_out.py`: the negative controls.
