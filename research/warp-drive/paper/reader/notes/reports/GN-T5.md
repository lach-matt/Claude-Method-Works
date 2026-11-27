# GN-T5: go/no-go checks for Route M of S-T5 (non-adapted crossing families at the face–axis set)

Nothing under `reader/` was edited, `assemble.py` was not run, and nothing was committed. All scripts and outputs are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt5/` (file list in §8).
**Nothing in this report counts as proved.** Numbers are labelled **computed** (by a script here), **deduced** (by an
argument written here) or **cited** (read in a chapter or report, with line or section).

**Read for this report.** notes/reports/S-T5.md (all) and its scratch scripts `st5/leafcross.py`, `st5/grazing_model.py`;
notes/reports/S-T3.md (all); S-T4.md 150–165 and 380–500. Chapter 81: 1–160, 381–680 (Kato), 877–1037, 1038–1671 (the
axes to rem:class-scope). Chapter 83: 334–600. Chapter 80: 380–420. proofs/P-CIVP.md: 1–150, 684–760. Two scratch reports
appeared while this work ran and were read where used: `scratchpad/reader/reports/GN-T3.md` (summary, §§2.3–2.5, 4–8)
and `GN-T4.md` (summary, §§1.2–1.3). Nothing under method/, drive/, extracted/ or recovered/ was read.

**Models.** The computations use flat models: Minkowski space for the times (GN-M1), the domain of dependence (W), and a
flat leaf equation on one slice (GN-M3, GN-M2). They confirm mechanisms, signs and exponents, not the constants of the
paper's background. No proof should cite them.

---

## Verdict: GO WITH CONDITIONS

| Check | Result | One line |
|---|---|---|
| **GN-M1** (the times) | **passed** | The closure times t_A and the bent evolution time τ exist with all of M1 (a)–(d); explicit in a flat model, where the face sections of t_A are A-sections to 30 digits, the bend needed is K > \|D\|/(4z0) (at most ≈ 0.006 for the paper's ellipse on 4 ≤ z0 ≤ 8), and every arc used runs into the past of its endpoint. The general construction needs only that each present family is crossing (∂_v U_A ≠ 0). Risk R2 of S-T5 is low. |
| **GN-M2** (multi-foliation energy) | **passed, with a correction to M4** | The energy inequality for the toy model closes: the non-local source enters only through its space-time H^k norm, which coarea along the t_A-slices bounds by slice-wise energies, and Fubini returns to τ-slices. **S-T5's step 3 (contraction in L²(Σ_τ) at each τ) is false**: a computed family with bounded L² norms on every slice of both foliations has a leaf average whose squared L²(Σ_τ) norm grows like log(1/λ_min). The fixed-time loss is real (logarithmic, and it persists at order k), so (F1)–(F2) of thm:class-kato must be replaced by integrated versions. With them nothing unbounded appears; the commutator [∂^α, leaf construction] is lower order. |
| **GN-M3** (residual smoothness per family) | **passed in the model; full check rides on Tier 3's GN3** | In a t_A-slice the residual at depth d below the face is O(d^N) when Û agrees to order N, with fitted exponents 2.00, 2.99, 4.00, and exactly 0 at the face. In Tier 3's slicing the same residual at the face is (−0.17)(c ρ²)^N ≠ 0, with c of S-T5 (2.1): the leak S-T5 §2.3 describes, measured. GN-T3 reports GO on Tier 3's GN3, whose proof transfers once the face section is a leaf. |
| **GN-M4** (localisation) | **passed for Tier 3's statements; restricted for interior faces** | Every use of Lemma R in Tier 3 is on rectangles whose past faces lie in 𝒞_out ∪ 𝒞_in, where (H×) makes every present family crossing. A rectangle with an interior past face {u = u0} (or {v = v0}) is admissible only if u0 (v0) avoids the axis supports of the outgoing-type (ingoing-type) further families: those families graze such a face and carry density along its axis generator. |
| **Statement W** | **provable, with four additions** | Cut-off, Tier 3 and a domain-of-dependence argument work, but (W1) the cut must be made on both faces near the corner axis circle, (W2) the grazing family's phase, not only its density, must be removed near the grazing set, (W3) the region must have a spacelike or null lateral face off the axes, and (W4) the true causal bound must be used, not Tier 1's C0. In the flat model with the paper's lengths W covers 61 % of the orbit-space rectangle with one grazing axis and 31 % with two (computed). |

**Conditions for GO.**
1. **(C1) Integrated forcing hypotheses in M4.** Replace (F1)–(F3) by the path-dependent, space-time versions of §2.6.
   S-T5 §4.3 M4 step 3 must not be written as stated.
2. **(C2) Slice-wise leaf estimates on truncated, arc-closed domains.** lem:class-leaf-differences (a) and (b) are needed
   in each t_A-slicing on the sets {t_A = t} ∩ {τ′ ≤ τ}, whose inner part shrinks to the axis as t → τ. Use the leaf-wise
   versions (GN-T3 T3-2(b), GN-T4 K-ax (b′)), extended as in §6.2; the extension operator of T3-2(a) is not uniform there.
3. **(C3) (H×) in the neighbourhood sense.** A crossing family's data must vanish on a neighbourhood of the corner axis
   circles, not only on them (§1.3). Otherwise its tube accumulates on the axis generator of the face where it grazes.
4. **(C4) Grazing phases decoupled.** A family must be carried (its p_A, Θ_A, q_A) only on a neighbourhood of the tube of
   its density, by a space-time cut-off on its transport equations (§6.1). This affects Tier 3's family clause too.
5. **(C5) Lemma R on rectangles with past faces in 𝒞_out ∪ 𝒞_in**, or with interior faces restricted as in §4.
6. **(C6) Tier 3 as amended by GN-T3.** Route M presupposes Tier 3: the Q1-adapted chart time Φ(u0, v0) (GN-T3 §4.3)
   becomes M1's τ0, the slice-triangle becomes the energy region of M5 (F), and GN3's τ-continuity step carries over.
7. **(C7) A one-sided leaf-wise estimate for M5 (P)** (§6.2), or the first-disagreement window argument with T3-2(a).

**Fallback.** Route S plus statement W are unaffected by anything found here and remain the fallback. Nothing found here
bears on grazing families, which stay out of reach (S-T5 §4.2).

---

## 1. GN-M1: the closure times and the evolution time (passed)

### 1.1 The construction (deduced)

Work near a face–axis segment J ⊂ 𝒞_out ∩ axis 2; the other three kinds of segment are the same with the roles of the
faces or the axes exchanged. Let τ0 be Tier 3's chart time, any time function whose restriction to 𝒞_out is an
increasing function T0(v) of v and to 𝒞_in an increasing function of u (GN-T3 §1.1: chapter 81's v̂ − R and the
Q1-adapted Φ(u0, v0) both qualify; cited). Let ρ be the distance to axis 2 and (z, ρ) the meridional coordinates of
lem:class-leaf.

- **Data.** By (H×) every non-adapted family A present near J is crossing there, so ∂_v U_A ≠ 0 and its face sections are
  graphs v = V_A(c, ϑ²), smooth in (c, ϑ²) (S-T5 §1.2; cited).
- **Closure times.** On 𝒞_out near J put
      g_A := T0(V_A(c, ϑ²)) − T0(V_A(c, 0)) = Ĝ_A ρ² + O(ρ⁴),      Ĝ_A = T0′ ∂_(ϑ²)V_A / R² on the face,
  c being the label of the A-section through the point. Extend g_A off the face as a smooth G-invariant function
  Ĝ_A(p) ρ(p)², with Ĝ_A smooth, and put
      t_A := τ0 − χ(ρ/δ_*) g_A,      τ := τ0 + K ρ² χ(ρ/δ_*),
  χ a smooth step (1 on [0, 1/2], 0 on [1, ∞)), summed over both axes. For the adapted families t_v := t_u := τ0.
- **(b) Face sections.** For ρ < δ_*/2, t_A restricted to 𝒞_out is T0(V_A(c, 0)), constant on each A-section. So the face
  sections of t_A are exactly the A-sections. For v on 𝒞_out and u on 𝒞_in they are τ0's, the double-null spheres; every
  section of 𝒞_out is a u-leaf and every section of 𝒞_in a v-leaf.
- **(a) Time functions.** |d(t_A − τ0)| ≤ C(sup|Ĝ_A| + δ_* sup|dĜ_A|) δ_* and |d(τ − τ0)| ≤ C K δ_*. Since dτ0 is
  timelike with a margin on the compact region, all are time functions for δ_* ≤ δ_1(K, Ĝ). Away from the axes all equal
  τ0.
- **(c) Causality.** On a level set {t_A = c}, τ = c + f_A with f_A := g_A + Kρ² = (Ĝ_A + K)ρ² near the axis. Let
  z = h(ρ) be any arc in the slice with |h′(ρ)| ≤ C_L ρ. That includes the leaves of every state in the balls of
  lem:class-leaf-differences (lem:class-volterra gives |h′| ≤ C ρ; cited 81:1236). Then
      d/dρ f_A(h(ρ), ρ) = 2(Ĝ_A + K) ρ + ρ² ∂_z Ĝ_A h′ + ρ² ∂_ρ Ĝ_A ≥ 2(K − sup|Ĝ_A|) ρ − C ρ³,
  using ∂_ρ Ĝ_A = O(ρ) (Ĝ_A is even in ρ). With K > sup_A sup_J |Ĝ_A| and δ_* small, τ increases along every such arc from
  the axis. Every arc used at a point x with ρ(x) < δ_*/2 lies in {τ′ ≤ τ(x)}. The memory depth is m := sup f_A ≤
  (K + sup|Ĝ_A|) δ_*².
- **(d) The corner.** τ is one function, so it agrees from both faces. Under (C3) no non-adapted family is present near
  the corner axis circles, so g_A can be cut off there and t_A = τ0 near the corner.
- **Order of choices.** K is fixed by the data (the slopes of the present families' sections), then δ_*. There is no
  trade-off: K does not depend on δ_*. Where Φ's slices are nearly null (GN-T3 R2) δ_* must be smaller, by a fixed
  factor.
- **Nesting of cut-offs.** S^ax for A is used only where ρ < δ_*/4. The arcs used there stay in ρ < δ_*/4, where χ = 1.

### 1.2 Check in a flat model (computed: `gn_m1_times.py`, 30-digit arithmetic)

**Model.**
- Minkowski ℝ⁴⁺¹, chart time t (the flat analogue of τ0).
- Corner sphere at t = 0, |x| = R0 = 5.1, with 𝒞_out = {t = |x| − R0} and 𝒞_in = {t = R0 − |x|}. With u1 = 7.2, 𝒞_in then
  reaches R = 1.5, as on the paper's background (P-CIVP 74–76; cited).
- Families A: w₊ = t + d_E (ingoing type: crossing on 𝒞_out, grazing on 𝒞_in) and B: w₋ = t − d_E (outgoing type:
  crossing on 𝒞_in), with E the ellipsoid of lem:class-ellipse-phase.
- Exact times: t_A := t − g, t_B := t + g, g := (|x| − α∥ − d_E)/2, α∥ the semi-axis along the axis.
- **Deduced in this model.** On 𝒞_out, t_A = (w₊ − R0 + α∥)/2, and on 𝒞_in, t_B = (R0 − α∥ + w₋)/2, exactly. In the
  t_A-slices (and the t_B-slices) the A-leaves (B-leaves) are the level sets of |x| + d_E. So the face section of a
  t_A-slice is the A-leaf through its axis point (Lemma A), and τ − t_A along the leaf from the axis point z0 is
  (K + D/(4z0)) ρ² + O(ρ⁴), with D := (α⊥² − α∥²)/(α⊥² + α∥(z0 − α∥)). For B it is (K − D/(4z0)) ρ².

**Results.**
- (b) and Lemma A: residuals ≤ 8 × 10⁻³¹ at all tested points, for both ellipses and both axes.
- (c), smallest normalised slope d(τ − t_A)/d(ρ²) along the A-arcs (d(τ − t_B)/d(ρ²) along the B-arcs), 0 < ρ ≤ 0.5,
  z0 ∈ {4 (4.5 for the 3:1 ellipse), 5.1, 6.5, 8}:

| ellipse (α1, α2), axis | K | A-leaves | B-leaves | prediction ∓D/(4z0) at z0 = 5.1 | memory at ρ = 0.5 |
|---|---|---|---|---|---|
| (1/2, 1/3), axis 2 | 0 | −0.00468 (all < 0) | +0.00112 | −0.002824 (measured −0.002831…−0.002824) | — |
| (1/2, 1/3), axis 1 | 0 | +0.00154 | −0.00590 (all < 0) | | — |
| (3, 1), axis 2 | 0 | −0.0812 (all < 0) | +0.0156 | | — |
| (3, 1), axis 1 | 0 | +0.0156 | −0.0417 (all < 0) | | — |
| (1/2, 1/3), both axes | 0.01 | +0.00532 | +0.00410 | | ≤ 3.97 × 10⁻³ |
| (3, 1), both axes | 0.1 | +0.0188 | +0.0583 | | ≤ 4.53 × 10⁻² |

- (a): with the bend, η⁻¹(dτ, dτ) ≤ −0.99 and η⁻¹(dt_A, dt_A) ≤ −0.90 on ρ < 0.5 (|∇g| ≤ 0.0097 for the paper's
  ellipse, ≤ 0.315 for the 3:1 one).
- **Reading.** Without a bend, at each axis one of the two orientations has arcs running into the future of their
  endpoints: the sign of S-T5's c changes between the axes (S-T5 §2.2), and A and B take opposite signs. One K serves all
  families at both axes. On 4 ≤ z0 ≤ 8, K > 0.006 suffices for the paper's ellipse and K > 0.082 for a 3:1 ellipse
  (0.01 and 0.1 were used); neither constrains δ_*.

### 1.3 Remarks

- **(H×) must hold on a neighbourhood (deduced).** Suppose a crossing family's data on 𝒞_out vanish only on the corner
  axis circle but not near it.
  - Its rays from points (v0, ϑ0) of 𝒞_out with v0, ϑ0 → 0 run along u at v ≈ v0 + O(ϑ0² u). For w₊ in the flat model,
    dv/dt = 1 − cos β along a future ray.
  - So its tube accumulates on the whole axis generator of 𝒞_in, where the family grazes. There ζ_A must be 1 (density
    present nearby) and no slicing closes 𝒞_in under its leaves (S-T5 §2.4 (ii)).
  - Hence (C3). With (C3) the tube stays a fixed distance from Γ ∩ 𝒞_in, the axis being invariant under the flow
    (as in Step 10 of thm:class-stability; cited 81:1619–1622).
- **Only the face geometry enters M1.** The curved background changes Ĝ_A and the margins, not the structure.

---

## 2. GN-M2: the multi-foliation energy inequality (passed, with a correction)

### 2.1 The toy model

- **Variables.** Orbit-space variables (τ, z, y), y ∈ ℝ² the planar variable with the axis {y = 0} and ρ = |y|;
  functions radial in y. This is "2+1" after the symmetry reduction, the dimension count of chapter 81's leaves.
- **Foliations.** The evolution time τ and two closure times t_A := τ − a_A ρ² χ, A = 1, 2, a_1 ≠ a_2 > 0. These are bent
  to the past, as M1 (c) requires.
- **Unknowns.** One wave field φ and two transported scalars θ_1, θ_2:
      □φ = N_0(φ, ∂φ, θ),      X_A θ_A = N_A(φ, ∂φ, θ) + Φ_A,      X_A = ∂_τ + b_A ρ ∂_ρ + c_A ∂_z,
  where X_A vanishes in ρ on the axis (rays at an axis run along it, lem:class-phase-axis; cited).
- **Non-local term.** Φ_A := Q_A(ℓ_A, Av_A ℓ_A), with ℓ_A a local function of (φ, ∂φ, θ) and
      Av_A f(x) := r⁻² ∫_0^r 2ρ f(γ_x^A(ρ)) dρ,      r := ρ(x),
  where γ_x^A is the arc of x in the slice {t_A = t_A(x)}, from the axis to x. In the flat, linearised case
  eq:class-leaf-volterra is exactly this average (prop:class-flat-model (b): σ_pl = ℓ − 2𝒜ℓ, with 𝒜 half of Av; cited).
  Arcs are straight in the coordinates (t_A, z, y), or curved, z = z_x + κ_A(ρ² − r²), as for real leaves.
- **Energies.** E_k(H) := Σ_(|α|≤k) ∫_H (|∂^α ∂φ|² + Σ_A |∂^α θ_A|²), with spacetime derivatives ∂^α, on a τ-slice or on a
  t_A-slice.

### 2.2 The inequality and its proof (deduced)

**The exact structure of the leaf average.**
- The map Ψ_A : (t, z, y) ↦ (τ = t + a_A|y|² χ, z, y) is a diffeomorphism with Jacobian 1.
- In the coordinates (t, z, y), Av_A is the dilation average D f(t, z, y) = ∫_0^1 2s f(t, z, s y) ds at fixed (t, z).
  For curved arcs, compose with the per-slice map z ↦ z − κ_A(ρ² − r²).
- ∂_t and ∂_z commute with D, and ∂_y^γ D f = ∫_0^1 2s s^|γ| (∂_y^γ f)(t, z, s y) ds. With ‖g(s·)‖_(L²(ℝ²)) = s⁻¹ ‖g‖,
  Minkowski's inequality gives
      ‖∂_t^j ∂_z^i ∂_y^γ D f‖_(L²) ≤ (2/(|γ| + 1)) ‖∂_t^j ∂_z^i ∂_y^γ f‖_(L²).
- Spacetime derivatives in (τ, z, y) are (t, z, y)-derivatives with polynomial coefficients: ∂_y|_τ = ∂_y|_t − 2a_A y χ
  ∂_t + …. Hence, with slab_m := [τ1 − m, τ2] × (the support) and m = max_A a_A δ_*²,

      ‖Av_A f‖_(H^k([τ1, τ2] × ·)) ≤ C_k(a_A, δ_*) ‖f‖_(H^k(slab_m)).                                          (2.1)

**The inequality.** For a solution on [τ1, τ2] with history on [τ1 − m, τ1]:

    E_k(τ) ≤ C (E_k(τ1) + ∫_(τ1−m)^(τ1) E_k) + C ∫_(τ1)^τ E_k(τ′) dτ′,      τ1 ≤ τ ≤ τ2,                     (2.2)

with C depending on sup-norms of (φ, ∂φ, θ) and their derivatives of order ≤ k/2 + 2.

**Proof.**
1. **The energy identity.** For ∂^α of the system on Σ_τ:
       d/dτ E_k ≤ C E_k + 2 Σ_A Σ_α |⟨∂^α Φ_A, ∂^α θ_A⟩_(L²(Σ_τ))|.
   It holds for almost every τ: by Fubini, ∂^α Φ_A ∈ L²(Σ_τ) for a.e. τ whenever Φ_A ∈ H^k of space-time. The local
   terms and commutators are standard (Moser on Σ_τ).
2. **Integrate and use Cauchy–Schwarz in τ.** ∫_(τ1)^τ ‖∂^α Φ_A‖_(L²(Σ_τ′)) E_k^(1/2) ≤ sup E_k^(1/2) (τ − τ1)^(1/2)
   ‖∂^α Φ_A‖_(L²(slab)).
3. **Bound the source in space-time.** By Moser and (2.1), ‖Φ_A‖_(H^k(slab)) ≤ C ‖ℓ_A‖_(H^k(slab_m)). By Fubini,
   ‖ℓ_A‖²_(H^k(slab_m)) ≤ C ∫_(τ1−m)^τ E_k. Av_A is bounded on L^∞.
4. **Gronwall with memory.** Steps 1–3 give E_k(τ) ≤ E_k(τ1) + C∫_(τ1)^τ E_k + C (τ − τ1)^(1/2) sup_[τ1,τ] E_k^(1/2)
   (∫_(τ1−m)^τ E_k)^(1/2), and Young's inequality and Gronwall's inequality give (2.2).
   No restriction of Φ_A to a τ-slice in H^k is used, so no trace is taken. ∎

**In the real problem**, (2.1) is replaced by lem:class-leaf-differences (a) in each t_A-slicing (M3), and the coarea
formula along the t_A-foliation:

    ∫∫_slab |∂^α Φ_A|² = ∫ dt ∫_({t_A = t}) |∂^α Φ_A|² |∇t_A|⁻¹ dS ≤ C ∫ dt 𝒩_k(U on {t_A = t} ∩ {τ′ ≤ τ})²
                       = C ∫∫_(slab_m) |∂^(≤k) U|² ≤ C ∫_(τ1−m)^τ E_k(τ′) dτ′,

the last two steps by coarea for U itself and by Fubini over τ-slices. Two forms of the slice estimate are available:
- **Conservative.** (a) as stated, which needs each slice state in the ball 𝔅 (an 𝒩_k ball). This is supplied by
  energies on the composite hypersurfaces H_(t,τ) := ∂({t_A ≤ t} ∩ {τ′ ≤ τ}). These are Lipschitz and spacelike, and the
  divergence identity holds on them. This is the 𝔑_k of S-T5 M4, with 𝓕(τ) enlarged by the H_(t,τ).
- **Lighter.** A tame form of (a), bound linear in 𝒩_k with constants depending on an 𝒩_(k−1) ball, which needs only
  τ-slice energies (the slice 𝒩_(k−1) norm follows from the τ-slice 𝒩_k norm by the trace theorem in a slab).
  Not checked line by line.

Either way the estimate must be local in time: on {t_A = t} ∩ {τ′ ≤ τ}, not the whole slice, since the outer part of a
slice t ∈ [τ − m, τ] lies in the future of Σ_τ. That domain is closed under arcs by M1 (c) and under P/F by M2, but its
inner part is a disc of radius ((τ − t)/(K + Ĝ))^(1/2) → 0. The flat estimate (2.1) is uniform there: the dilation
average maps every disc about the axis into itself with the same constant. The curved version needs the per-leaf
(Volterra) form of lem:class-leaf-differences, condition (C2).

### 2.3 The commutator [∂^α, leaf construction] on tilted slices (deduced)

- **Choice of coordinates.** Take coordinates (t, ξ) adapted to the t_A-foliation. Φ_A on {t_A = t} is Λ_t(U(t, ·)):
  Λ_t solves the leaf equation on the slice and reads the planar shear.
- **Tangential derivatives** commute with Λ_t up to lower order. This is lem:class-leaf-differences (a) on the slice
  (interior regularity, or the Hardy structure in the radial form).
- **The transverse derivative** is ∂_t Λ_t(U(t)) = DΛ_t[∂_t U] + (∂_t Λ_t)(U).
  - The first term is DΛ_t, bounded on L² of the slice, applied to a spacetime derivative of U on the slice.
  - The second is the variation of the slice geometry (induced γ3, K_Σ of the fixed foliation), with coefficients
    smooth in t. That is step (4) of lem:class-planar-shear with t in place of τ (cited 81:1314–1317).
- **Spacetime derivatives** in the τ-chart are combinations of these with smooth coefficients (the foliation's
  Jacobian).
- **Conclusion.** ∂^α Φ_A = DΛ_t[∂^α U] + (terms with at most k − 1 derivatives of U, and products), with the top-order
  term bounded in L² of each t_A-slice by that slice's 𝒩_k.
- **Kill criterion.** S-T5's criterion, "a term that 𝔑_k does not bound", is not met. The only thing that is not
  bounded is the restriction of ∂^α Φ_A to a τ-slice (§2.4), and the scheme never uses it.

### 2.4 The trace question: fixed-time norms lose, space-time norms do not (computed: `gn_m2_trace.py`; deduced)

**The family.**
- Flat model of §2.1 with a = 1 and straight arcs.
- On each t-slice, f(t, y) = V(t, ρ) := ψ(t) φ(ρ/λ(t))/λ(t), with λ(t) = max(θ ((τ* − t)/a)^(1/2), λ_min), φ(s) =
  (1 − s²)³ on [0, 1), θ = 1/2, and ψ switching on smoothly over t ∈ [τ* − 1/4, τ* − 1/8] and off over [τ*, τ* + λ_min²/θ²].
- **Deduced.** On Σ_τ*, the arc of the point at radius r lies on the slice t = τ* − a r², where λ = θ r. So
  Av f(τ*, r) = (θ/r) Φ_∞ (Φ_∞ = ∫_0^1 2sφ = 1/4) for r ≥ λ_min/θ, and

      ‖Av f‖²_(L²(Σ_τ*)) = 2π θ² Φ_∞² log(θ r_max/λ_min) + O(1).

**Results.**

| λ_min | ‖Av f‖²_(L²(Σ_τ*)) | sup over τ-slices of ‖f‖² | ‖f‖² on every t_A-slice |
|---|---|---|---|
| 10⁻² | 1.4412 | 0.4637 | 0.4488 |
| 10⁻⁴ | 1.8933 | 0.4637 | 0.4488 |
| 10⁻⁶ | 2.3454 | 0.4637 | 0.4488 |

The increment per decade is 0.2261, against 2πθ²Φ_∞² ln 10 = 0.2261 predicted. The space-time norm stays bounded: on
every t_A-slice ‖Av V(t)‖²/‖V(t)‖² ≤ 2.66 < 4 (L² constant 2 for the normalised average), so ‖Av f‖²_(L²(slab)) ≤ 0.298,
independent of λ_min.

**Order one.**
- Put U_N := N⁻¹ cos(Nz) V with λ_min = N^(−1/2).
- Its first derivatives are bounded on the slices of both families, uniformly in N = 10², 10⁴, 10⁶, 10⁸ (computed):
  - N⁻¹ sup ‖∂_ρ V‖ = 0.194 → 0.0002;
  - N⁻¹ sup ‖∂_t V‖ on t_A-slices = 0.107, 0.091, 0.096, 0.086;
  - the same on τ-slices = 0.105, 0.078, 0.085, 0.092.
- Yet ‖Av V‖²_(Σ_τ*) = 1.215, 1.441, 1.667, 1.893: it rises by 0.226 for each factor 100 in N, linearly in log N, and
  ‖∂_z Av U_N‖² on Σ_τ* is half of it.
- **Order k (deduced).** U_N := N^(−k) cos(Nz) V with λ_min = N^(−1/2) has every spacetime derivative of order ≤ k
  bounded in L² on every slice of both families (∂_t^j V ~ N^j V, ∂_ρ^j V ~ N^(j/2) V). But ‖∂_z^k Av U_N‖_(L²(Σ_τ*)) ~
  (log N)^(1/2).

**Consequences.**
- **(i)** The fixed-time hypotheses (F1) and (F2) of thm:class-kato fail for a forcing that is non-local along tilted
  slices, even on 𝔑_k-bounded states. The loss is logarithmic at the axis, where the Jacobian of (r, z) ↦ (τ′, z′) on an
  arc vanishes like λ r.
- **(ii)** S-T5 §4.3 M4 step 3, "‖Φ_A[U] − Φ_A[V]‖_(L²(Σ_τ)) ≤ C sup_[τ−Kδ_*², τ] ‖U − V‖_(L²)", is false. U − V can
  be any small smooth function, and f above is one.
- **(iii)** The space-time versions hold (2.1). They are all the Kato scheme needs (§2.6).
- **(iv)** S-T5's idea, space-time L² norms of the source plus energies on hypersurfaces, does avoid the loss. It only has
  to be applied to the contraction as well, not just to the top-order bound.

### 2.5 The toy model evolved (computed: `gn_m2_toy.py`)

**Set-up.** z suppressed, ρ ∈ [0, 2.5], with
- φ_ττ = Δ_ρ φ − φ + (θ_1 + θ_2)/2;
- ∂_τ θ_A + b_A ρ ∂_ρ θ_A = −σ_A²/4 + φ_τ, with σ_A := θ_A − Av_A θ_A;
- (a_1, a_2) = (0.5, 1.5) and (b_1, b_2) = (0.3, −0.2).

Arcs reach back into the history, taken as the data for τ < 0. The scheme is Heun's method, with the history interpolated
in time and the current step interpolated between the last stored slice and the stage values.

| N | E_0(1) | E_1(1) | max_τ ‖σ‖_(L²(Σ_τ)) |
|---|---|---|---|
| 50 | 0.94061 | 27.519 | 0.20897 |
| 100 | 0.94715 | 28.106 | 0.20910 |
| 200 | 0.94887 | 28.260 | 0.20914 |

**Convergence.** L² self-convergence of θ_1, θ_2 and φ is second order (θ_1: 9.6 × 10⁻⁴ → 2.4 × 10⁻⁴). The max-norm error
of θ_1 is first order in the axis cell only, from the half-cell quadrature there.

**What this shows.** The memory term is causal and the scheme is stable. Nothing beyond the past is used. For smooth data
this was not in doubt; the run shows that the causal-memory system is as well behaved as (2.2) says.

### 2.6 What M4 must state (draft; deduced)

The forcing is path-dependent, F(τ, U|_[τ−m, τ]), with m the memory depth of §1.1. Replace (F1)–(F3) by:

- **(F1_int)** ‖F(U)‖_(H^s([τ1,τ2] × ℝ⁴)) ≤ C_F(𝔐) (1 + ‖U‖_(H^s([τ1−m, τ2] × ℝ⁴))) for paths with sup_τ ‖U(τ)‖ ≤ 𝔐
  in the norm used (𝒩_s on τ-slices, plus the H_(t,τ) energies in the conservative form);
- **(F2_int)** ∫_(τ1)^(τ2) ‖F(U) − F(V)‖²_(L²(Σ_τ)) dτ ≤ L(𝔐)² ∫_(τ1−m)^(τ2) ‖U − V‖²_(L²(Σ_τ)) dτ;
- **(F3)** τ ↦ F(U)(τ) is continuous into L². This holds since F(U) ∈ H¹(slab) ⊂ C(L²) by the trace theorem.

**The linear step.** lem:class-kato-linear with f ∈ H^s(slab) in place of sup_t ‖f(t)‖_(H^s) < ∞. Energies of spacetime
derivatives on τ-slices follow from the divergence identity; the solution lies in C(H^s), by approximation of f in
L¹(H^s). A routine extension.

**Iteration.**
- **Boundedness.** E_s(u^(n+1))^(1/2)(τ) ≤ e^(Cτ)(E_s(0)^(1/2) + C T^(1/2) ‖F(u^n)‖_(H^s(slab))), and (F1_int) closes
  for T small.
- **Contraction in sup_τ ‖·‖_(L²(Σ_τ)).** e^(1/2)(τ) ≤ C T^(1/2) ‖F(u^n) − F(u^(n−1))‖_(L²(slab)) + … ≤ C T sup ‖δ^n‖,
  with δ^n = 0 before τ1.
- **Uniqueness and the domain versions** by the integrated Gronwall argument: e(τ) ≤ C ∫_(τ1)^τ e.

**History.** For continuation from τ1, the history is the solution on [τ1 − m, τ1]. From Σ_init, Rendall's ξ vanishes
on {τ ≤ τ_init + m} near the axes (S-T3 §4.2 (ii)), so the memory is first used where the solution is the reference.

**Where M5 enters.** The domain-of-dependence statements of M5 run the same integrated Gronwall argument on P ∩ {τ′ ≤ τ}
and on the slice-triangle F ∩ {τ′ ≤ τ}. They need the slice estimates on the truncated domains {t_A = t} ∩ P (or F)
∩ {τ′ ≤ τ}, which is (C2) and (C7).

**Size.** M4 grows from 250–400 to about 300–450 lines (integrated hypotheses, path-dependence, linear lemma with
space-time forcing).

---

## 3. GN-M3: residual smoothness per family, in the tilted slicing (passed in the model)

### 3.1 Statement

The claim to check is S-T3 T3-3 / S-T5 M6. Let x ∈ P lie at depth d below a face, within δ_*/4 of an axis, and let A be
a family whose S^ax is used there. Then σ_A[Û](x) − σ_A^formal(x) = O(d^N) for every N, with all derivatives, where
the leaf of Û through x is taken in the t_A-slice of x.

### 3.2 Derivation (deduced)

1. **The arc stays near the face.**
   - By M2, the face section of the t_A-slice is Û's A-leaf: Û carries the formal 1-jets, and (b) of §1.1 makes the
     section a level set of the formal phase.
   - Û's A-leaves foliate a neighbourhood of the axis, so the arc of x lies between x's leaf and the face section.
   - The transverse derivative of the foliation, ∂_(z0) h, lies in [1/C, C], so the arc stays within C d of the face
     (the sandwich).
2. **The source is flat along the arc.** There H_L[Θ̂_A] − H_L[formal] = O(d^N) for every N, since Û matches the jets to
   infinite order.
3. **Volterra stability.** Gronwall for (r h′)′ = r H/a_L − E_L (lem:class-volterra; cited 81:1240–1253) gives a leaf
   difference, and a σ difference at x, of O(d^N).
4. **Derivatives.** Differentiating in x, in the axis point and in t (step (4) of lem:class-planar-shear) gives the
   same for all derivatives.

So F̃ = 1_P 𝔄_ξ(Û) is smooth across the faces, per family. GN-T3's τ-continuity step at the corner (GN-T3 §3.2; cited)
applies unchanged; near the corner only the adapted families are present, by (C3).

### 3.3 Computation (computed: `gn_m3_residual.py`, `gn_m3_residual_b.py`)

**Model.**
- One flat slice M3 = ℝ³, leaves z = h(ρ). With q := ρ h′/(1 + h′²)^(1/2) the leaf equation is q(r) = −∫_0^r ρ H dρ and
  σ_L = H/2 + q(r)/r².
- Family w₊: its leaves are the level sets of |x| + d_E in the t_A-slicing (§1.2) and of d_E in Tier 3's slicing.
- The face section is a level set of |x| + d_E (t_A-slicing), respectively the round circle |x| = R_F (Tier 3's
  slicing).
- Û has H_Û = H_true + η s^N, with s the face's defining function (s > 0 in P) and η = 1 + 3ρ² + (z − 5.6)/5. A constant
  η would hide the effect, since a constant change of H lies in the kernel of the planar shear (GN-T3 §2.4 noted the
  same).
- The leaf of Û through x is found by shooting from the axis (DOP853, rtol 10⁻¹³).
- Validation: the ODE with H_true reproduces the level set's σ to 8 × 10⁻¹⁷.

**t_A-slicing, Res(d) = σ[Û](x) − σ_true(x)**, for the 3:1 ellipse with N = 4 and the paper's ellipse with N = 2:

| ρ_x | d = 0 | 10⁻⁴ | 10⁻³ | 10⁻² | local slopes |
|---|---|---|---|---|---|
| 0.1 (paper, N = 2) | −1.7 × 10⁻¹⁶ | 3.00 × 10⁻¹⁰ | 3.00 × 10⁻⁸ | 2.98 × 10⁻⁶ | 2.00 2.00 2.00 2.00 |
| 0.3 (paper, N = 2) | 8 × 10⁻¹⁷ | 2.69 × 10⁻⁹ | 2.69 × 10⁻⁷ | 2.67 × 10⁻⁵ | 2.00 2.00 2.00 2.00 |
| 0.3 (3:1, N = 4) | 4 × 10⁻¹⁶ | roundoff | 1.07 × 10⁻¹² | 1.07 × 10⁻⁸ | 4.01 4.00 4.00 |

With constant η and N = 3 the slope is 2.99.

**Tier 3's slicing, residual at the face (d = 0)**, Res/(cρ²)^N with c of S-T5 (2.1):

| ρ_x | paper, N = 2 | 3:1, N = 2 | 3:1, N = 4 |
|---|---|---|---|
| 0.05 | −0.1670 | −0.1670 | (roundoff) |
| 0.10 | −0.1679 | −0.1678 | −0.1004 |
| 0.20 | −0.1716 | −0.1714 | −0.1017 |
| 0.30 | −0.1778 | −0.1772 | −0.1039 |

**Reading.**
- In the t_A-slicing the residual vanishes at the face to machine precision and to exactly the order of the mismatch.
- In the chart slicing the residual at the face is a fixed multiple of (cρ²)^N: flat at the axis, nonzero for ρ > 0, as
  S-T5 §2.3 states.
- The constant ratio confirms S-T5's formula (2.1) for c quantitatively, which GN-T3 did not re-derive.

### 3.4 Status

- **Passed in the model.** The full statement is Tier 3's GN3 with the slicing changed. GN-T3 reports GO on it, with a
  proof that uses only that the face section is a leaf of Û (GN-T3 §3; cited).
- **What remains is writing**, not a check: M6 = GN-T3's GN3 proof in the t_A-slicing, plus the remark that the sandwich
  in a t_A-slice is M2.

---

## 4. GN-M4: localisation on sub-rectangles (passed for Tier 3; restricted for interior faces)

**What Tier 3 uses Lemma R for** (S-T3 T3-8, GN-T3 §§4.3, 6; cited):
- (i) independence of the extension of the data beyond u1 and v1, now also carrying existence on Q1 (GN-T3 §4.3);
- (ii) localisation (d): g = g0 on corner rectangles [0, u′] × [0, v′];
- (iii) uniqueness on Q1 and on corner rectangles.

All three are rectangles whose past faces lie in 𝒞_out ∪ 𝒞_in. There (H×) makes every present family crossing, and M1
applies to the rectangle's own faces unchanged: the faces are pieces of the same cones, so the same t_A serve.

**Interior faces (deduced).** A rectangle R′ = [u0, u′] × [v0, v′] with u0 > 0 or v0 > 0 has an interior past face.
1. At an axis point in F the gradient of every class phase is a multiple of dv or du (lem:class-phase-axis; cited). A
   family's type is constant along connected pieces of the axis. b is odd, so b = 0 on the axis and g⁻¹dv ∝ ∂_u there.
2. Hence the rays of an ingoing-type family at the axis are the curves {v = const, ϑ = 0}. Its axis density, transported
   by P_A(q_A) = −Θ_A q_A, is nonzero at (u, v) exactly when it is nonzero at (0, v) on 𝒞_out. Likewise outgoing-type
   families along {u = const} from 𝒞_in.
3. On {v = v0} an ingoing-type family grazes: it is the face's orientation. On {u = u0} an outgoing-type family grazes.
4. So, with V_A the axis v-support on 𝒞_out of an ingoing-type further family and I_B the axis u-support on 𝒞_in of an
   outgoing-type one, the face {v = v0} carries a grazing family with density on its axis generator exactly when
   v0 ∈ V_A, and the face {u = u0} exactly when u0 ∈ I_B. That is S-T5's obstruction (ii), and Lemma R on R′ is then
   not available.

**Statement for M7.**
- Lemma R per family on rectangles with past faces in 𝒞_out ∪ 𝒞_in, as stated.
- On a rectangle with an interior past face only if that face's axis generator avoids the closure of the axis supports
  of the families grazing it.
- Tier 3's theorem needs nothing more.
- Any later use of interior faces must carry this restriction: Route E's gluing, or Tier 4's corners S_(a−η, b−η)
  (S-T4 T4-6; cited). This is consistent with S-T4 (H3), which already asks further families to vanish near the axes.

---

## 5. Statement W

### 5.1 Is it provable? Yes, with four additions (deduced)

S-T5 §4.4's outline (cut the uncovered densities off near Γ ∩ N̄, re-solve the cone constraints, apply Tier 3, finite
speed) is sound in structure. Four points must be added.

- **(W1) The corner.**
  - A grazing family's density on its grazing face's axis generator is carried from the corner (S-T5 §1.2; cited), and
    the corner values are shared by both faces.
  - So the cut must vanish near the corner axis circle on both faces. On the crossing face it must vanish on a
    neighbourhood of that circle, not only on it, for the reason of §1.3.
  - N must contain those neighbourhoods. S-T5 says "together with the corner axis circles if they are involved"; it
    should say "on both faces".
- **(W2) The phase, not only the density.**
  - A family with zero density near its grazing segment still has phase data there.
  - Its face jets divide by ∂U_A = O(ϑ²): the first jet is smooth when a1′ ≠ 0, and the higher ones need the
    compatibility conditions of S-T5 §2.4.
  - For generic smooth phase data Rendall's Û is not smooth there, whatever the density.
  - The cut problem must therefore carry the family only on a neighbourhood of the tube of its cut density (§6.1).
- **(W3) The region.**
  - The exact D := {p : J⁻(p) ∩ faces ⊂ faces ∖ N} has the achronal lateral boundary ∂J⁺(N), which need not be smooth.
  - What is provable directly is the development on every region D′ ⊂ D bounded by the faces off N and a G-invariant
    spacelike face {ϑ = Θ(u, v)} off the axes, with g⁻¹(dϑ − dΘ, dϑ − dΘ) < 0, i.e. Θ_u Θ_v > e^(2σ)/(2R²) on the
    round background.
  - On D′, two developments are compared by the energy identity with the faces and the lateral face as boundary.
    - Near the excluded axis, D′ stays at distance ≥ R sin w from the axis. There the local closure S_A is a valid
      identity for genuine solutions, and no leaves are needed (constants ~ (Rw)^(−1−j), prop:class-axis (c); cited).
    - Near the other axis and at face–axis points outside N, the leaves stay in D′ by M1–M2 (or Tier 3's Lemma A).
      In the flat model below, the lateral face stays ≥ 0.1 rad from the other axis.
  - The union of such D′ should exhaust the interior of D. That is plausible but not checked.
- **(W4) The causal bound.**
  - S-T5's remark uses Tier 1's angular speed C0 (uv)^(1/2), with C0 = 2√2/R_min. On the paper's lengths this
    excludes everything with uv ≳ 0.65.
  - The true reach is far smaller (computed below). W should be stated with J⁻ (or a Θ adapted to it), not with L7's
    constant.

**What W gives.** A smooth class development on D′, in the gauge eq:loc-double-null, unique among developments on D′ near
the background. It does not depend on the cut-off. It induces the original data on D′ ∩ faces, since those lie outside
N.
- **Gauge caveat.** The gauge reference W̊ on D′ must depend only on the data outside N. A local (Borel-type) extension
  does this after shrinking D′ by O(ε) (S-T3 R5; cited).
- **Size.** About 90–160 lines, against S-T5's 60–120.

### 5.2 How large is D? (computed: `gn_w_domain.py`, flat model)

**Set-up.** Corner sphere R0 = 5.1, u1 = 7.2, v1 = 4.5, N = (𝒞_in ∩ {ϑ < 0.05}) ∪ (𝒞_out ∩ {ϑ < 0.05, v ≤ 0.05}), for a
grazing family on the axis-2 generator of 𝒞_in. A point p belongs to D iff ϑ(p) > w + Δ(p), with Δ(p) the largest
angle of J⁻(p) on the faces.

| u \ v | 0.9 | 1.8 | 2.7 | 3.6 | 4.5 |
|---|---|---|---|---|---|
| 0.8 | 0.166 | 0.225 | 0.265 | 0.296 | 0.320 |
| 2.4 | 0.313 | 0.423 | 0.497 | 0.552 | 0.596 |
| 4.0 | 0.450 | 0.603 | 0.704 | 0.779 | 0.836 |
| 5.6 | 0.609 | 0.808 | 0.935 | 1.026 | 1.096 |
| 7.2 | 0.831 | 1.081 | 1.233 | 1.339 | 1.417 |

(Δ in radians.)

**Reading.**
- With one grazing axis, D covers **0.608** of the orbit-space rectangle [0, 7.2] × [0, 4.5] × [0, π/2]. The excluded
  set is a cone about that axis, opening from 0 at the faces to 1.42 rad at the far corner, and never reaching the other
  axis.
- With grazing families at both axes (symmetric case) D covers **0.310**, and at 31 % of the (u, v) points no angle is
  left.
- Tier 1's bound C0 (uv)^(1/2), C0 = 1.886, gives 1.886 at (u, v) = (1, 1), where the true Δ is 0.196, and 10.7 at the
  far corner, where it is 1.417.

On the paper's background the numbers differ (R varies, and the background is not flat). The shape (a widening cone
about each grazing axis, no loss near the faces off it) is what W gives.

---

## 6. Two further findings

### 6.1 Grazing phases (deduced; affects Route M, statement W and Tier 3's family clause)

- **The problem.** Every further family is grazing on one face at the corner axis circle: its gradient there is a
  multiple of dv or of du. So its phase data on that face near the axis generator are grazing data, even where its
  density vanishes.
  - The face jets of p_A there are obtained by dividing by ∂U_A = O(ϑ²) and must satisfy the compatibility conditions of
    S-T5 §2.4.
  - Tier 3 (S-T3 §4.2 (i)) and Route M carry every family's unknowns (p_A, Θ_A, q_A) on all of ℝ⁴ (chapter 81's system
    does). So Rendall's Û needs these jets everywhere, and for generic phase data it is not smooth near the grazing
    generator.
- **The remedy (C4).** Multiply family A's transport equations (Aug2)–(Aug4) by a space-time cut-off ξ_A, replacing them
  by ∂_τ(· − reference) where ξ_A = 0, as 𝔄_ξ does for the whole system. Take ξ_A = 1 on a neighbourhood of the A-rays
  from a neighbourhood of supp q_A on the faces, and 0 near the face–axis segments where A grazes.
- **Why this is legitimate.**
  - A enters the other equations only through q_A: (Aug1) through q_A p_A ⊗ p_A, the closures of other families through
    Σ q_A g⁻¹(p_B, p_A)².
  - The constraints for A (ν_A, dp_A, Δ_A) are needed only on the tube.
  - The leaf discs for S^ax of A at tube points near an axis stay inside {ξ_A = 1} once δ_* is small.
- **How large an issue.** Small to write (20–40 lines), but S-T3's family clause, S-T5's M0 and W must all say it.
  GN-T3 R4's recommendation (exclude further families near the axes) does not remove it, since the phase is present at
  the corner whatever the density.

### 6.2 A one-sided leaf-wise Lipschitz estimate (deduced; serves M5 (P), condition C7)

- **What is already available.** GN-T3 T3-2(b) and GN-T4 K-ax (b′) give ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D))
  for D closed under the leaves of **both** states (cited).
- **What M5 (P) needs.** In Route M it needs D = P ∩ {t_A = t} ∩ {τ′ ≤ τ}, closed under the arcs of V = Û (M2 and M1 (c)),
  while U's face sections are not yet known to be leaves.
- **The one-sided bound.** It holds with D closed under V's arcs only.
  1. Let ẑ0 be V's axis point for x, L̂ V's leaf and L′ U's leaf from ẑ0. Subtract the Volterra equations and split
         G_U(h_L′, p_L′) − G_V(h_L̂, p_L̂) = [G_U(h_L′, p_L′) − G_U(h_L̂, p_L̂)] + [G_U − G_V](h_L̂, p_L̂).
     The second bracket is evaluated on L̂ ⊂ D and is O(ρ|U − V|). The first is bounded by U's Lipschitz constants,
     |∂_p G| ≤ C(ρ + |p|) and |∂_z G| ≤ C(ρ + |p|). The second bound is finer than lem:class-volterra's C_1, since
     E_L(0, z, p) = A3p³/B3 (cited 81:1242–1243).
  2. Gronwall gives |δp(r)|/r ≤ C 𝒜_x|U − V| + C r² M|U − V|, with 𝒜_x the Hardy average along L̂ and M bounded on L².
  3. U's leaf L through x and L′ are both U-leaves, with axis points within |δh(r_x)| of each other. Comparing them uses
     only U's smoothness.
  4. So |σ[U](x) − σ[V](x)| ≤ C(|U − V|(x) + 𝒜_x|U − V|), C depending on C² bounds of g and C¹ bounds of (p, Θ) for both
     states. Integrating over V's axis points gives the L²(D) bound.
- **Uniformity.** The bound is uniform in D's shape, so in the thin inner discs and near the corner time.
- **The alternative.** GN-T3's first-disagreement argument with T3-2(a), run on a window [τ*, τ* + η], with the
  extension taken from the uniform domain P ∩ {t_A = t} ∩ {τ′ ≤ τ* + 2η}, also closes: the L² extension constant is
  scale-invariant and U − Û is flat on {τ′ ≤ τ*}.
- **Route M and GN-T3 R4.** A further family whose tube approaches an axis inside F needs ζ_A = 1 on an axis
  neighbourhood traced back to the face where it crosses. Route M's t_A makes S^ax usable there. This removes GN-T3's
  R4 conflict for families whose approach lies away from the face they graze.

---

## 7. What changes in S-T5's plan

- **M0.** Add (C4): each further family is carried only near the tube of its density (§6.1). Add (C3): the neighbourhood
  form of (H×).
- **M1.** Use the construction of §1.1: t_A := τ0 − χ g_A, τ := τ0 + Kρ²χ, t_v = t_u = τ0, with τ0 the Q1-adapted chart
  time of GN-T3 §4.3. Risk R2 drops from moderate to low. Size 60–100 lines, against 80–120.
- **M2.** Unchanged (GN-T3's criterion of §1.2 there, in the t_A-slicing).
- **M3.**
  - lem:class-leaf-differences (a) and (b) are needed on the truncated, arc-closed domains {t_A = t} ∩ {τ′ ≤ τ}, in
    per-leaf form (C2): (b′) of GN-T4 and the one-sided form of §6.2.
  - S-T3's GN2 concern (uniformity near the corner) disappears with the per-leaf forms.
  - Size unchanged, 80–120.
- **M4.**
  - Step 3 is false as written; use (F2_int).
  - Step 1 needs f ∈ H^s(slab) for energies of spacetime derivatives, which (2.1) and coarea supply.
  - Add path-dependence and the history.
  - 𝓕(τ) gains the composite hypersurfaces H_(t,τ) if the conservative form of (a) is used.
  - Size 300–450 lines.
  - Risk R1 drops from moderate–high to moderate: the mechanism is settled; the text is longer than planned.
- **M5.**
  - (P) uses the one-sided estimate or the window argument (C7).
  - (F) runs on the slice-triangle of GN-T3 §4.2, with Δ_A's region the tube of A from the faces plus an axis
    neighbourhood inside {ζ_A = 1}.
  - The integrated Gronwall argument replaces the pointwise one.
- **M6.** GN-T3's GN3 proof in the t_A-slicing (§3); unchanged in size.
- **M7.** Lemma R on rectangles with past faces in 𝒞_out ∪ 𝒞_in; interior faces restricted (§4). This is S-T5's GN-M4
  answered: no restriction of Tier 3's statements is needed.
- **M8.** Name (C3) and (C4) in the statement. In the remark on the grazing case, state W with (W1)–(W4).
- **Statement W.** 90–160 lines (§5.1).
- **S-T5 §4.4's remark** on D's width should use J⁻, not C0 (uv)^(1/2).
- **Total Route M.** About 950–1,450 lines on top of Tier 3 as amended by GN-T3, against S-T5's 900–1,400.

**Order of work** (S-T5 §4.3, revised).
1. GN-M1 and GN-M2 are done.
2. M0 (with C3, C4) and M1.
3. M2, and M3 with the per-leaf forms.
4. M4 in the integrated form.
5. M5–M6.
6. M7.
7. M8 and W.

Route S can still be written first, as an add-on to Tier 3 (S-T5 §4.3; cited); it needs (C4) as well.

---

## 8. Files

All in `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt5/`:

| File | What it does | Output |
|---|---|---|
| `ellipse.py` | distance to the ellipse, foot point, normal (mpmath) | — |
| `gn_m1_times.py` | GN-M1: t_A, t_B, τ in the flat model; face sections, Lemma A, monotonicity along arcs, timelike checks | `gn_m1_times.out` |
| `gn_m2_trace.py` | GN-M2: fixed-time versus space-time norms of the leaf average across tilted slices; order-zero and order-one families | `gn_m2_trace.out` |
| `gn_m2_toy.py` | GN-M2: the toy model (one wave, two transports, two foliations) evolved with memory; energies and self-convergence | `gn_m2_toy.out` |
| `gn_m3_residual.py` | GN-M3: residual at depth d, t_A-slicing against the chart slicing (constant η) | `gn_m3_residual.out` |
| `gn_m3_residual_b.py` | GN-M3: the same with non-constant η, smaller d, and Res(0)/(cρ²)^N | `gn_m3_residual_b.out` |
| `gn_w_domain.py` | statement W: the domain of dependence in the flat model with the paper's lengths | `gn_w_domain.out` |
