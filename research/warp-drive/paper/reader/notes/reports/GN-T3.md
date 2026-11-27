# GN-T3: go/no-go checks for Tier 3 (perturbations that reach the axes)

Nothing under `reader/` was edited. `assemble.py` was not run. All computations are in the scratch directory
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt3/` (file list in §8).

**Read for this report.** notes/reports/S-T3.md (all); notes/reports/S-CIVP.md §§1, 3 (all of §3.3); chapter 81:
1–380, 540–710, 848–1671; chapter 80: 150–244, 350–424; chapter 83: 1–80, 330–600. On the coordinator's notes:
S-T5.md §2 and §5.3, S-T4.md lines 150–165 and 512–570. proofs/P-CIVP.md does not exist (checked 2026-11-20), so
Tier 1 is cited by the lemma names L0–L11 of S-CIVP §3.3.

---

## Summary

| Check | Verdict | One line |
|---|---|---|
| **GN1** (Lemma A in the actual chart) | **GO** | Proved, with an exact "if and only if" criterion. Verified by computer algebra for the general class metric of eq:loc-double-null and a general face-adapted slicing, with positive and negative controls. It holds for **every** chart time whose restriction to each face is an increasing function of that face's data coordinate. That includes τ = v − R and the data's t = u + v (S-T4's request). |
| **GN2** (uniform constants near the corner time) | **GO, with a change to T3-2** | The extension Û and the extension from each component of P are uniform. The extension from F ∩ Σ_τ is **not**: near the corner time that set is a thin shell, and no extension operator from it is uniformly bounded (capacity bound, §2.3). S-T3's remedy, "components one at a time", does not help there, because F ∩ Σ_τ is one component. The fix is a leaf-wise version of lem:class-leaf-differences (b) that needs no extension. It applies in T3-6 and in Lemma R, and it is uniform in the width (checked numerically, §2.4). |
| **GN3** (the forcing F̃ is smooth) | **GO** | Proved. The non-local residual inherits the order of vanishing of the local mismatch, because the face section is a leaf of Û. The proof adds a τ-continuity step at the corner that S-T3 omits. Numerically, a mismatch vanishing to order m gives a residual vanishing to order m, the fitted exponent within 0.012 of m for m = 1, …, 4. A negative control shows the plateau that appears when the face section is not a leaf. |

**One new obstruction affects the plan, though no GN check fails.** It concerns T3-6 and the claim "the whole rectangle
Q1" (§4).
- **The problem.** Inside F the two adapted families' leaves in a slice separate at second order, O(ε)|y|² (S-T3 §1.1).
  So a boundary of the energy region that is a leaf of only one family is not closed under the other family's leaves.
  An example is the future face {u_out = u1} ∩ Σ_τ.
- **What T3-6 therefore needs.** The constraint propagation must run on a region whose slice sections are bounded by
  face sections only: a "slice-triangle" F ∩ {τ ≤ s}.
- **Why chapter 81's τ falls short.** On chapter 83's background, the τ-slice through the far corner of
  Q1 = [0, 7.2] × [0, 4.5] has τ = 1.54. But τ ≤ −1.52 on 𝒞_in^(7.2), and τ ≤ −0.70 at the inner radius a. So the
  τ-triangles reach only a neighbourhood of the faces.
- **The remedy.** The whole-rectangle claim survives in three steps:
  1. Use a chart time adapted to Q1: any function of the background's (u, v) that increases in both (example in §4.3).
  2. Extend the data a little beyond u1 and v1, inside L0's neighbourhood 𝒩.
  3. Use Lemma R for independence of the extension.
- **Size of the change.** This adds about 40–70 lines and changes T3-3, T3-6 and T3-8.

**The coordinator's O(ε) note (S-T5 §2.2).** No conclusion of this report relies on the size of the crossing depth.
- GN1 is an exact identity.
- GN2's leaf-wise lemma needs only exact closure.
- GN3's negative control uses an order-one curvature mismatch, Δκ = 0.3, which is consistent with S-T5's correction.
- The obstruction of §4 uses only that the in-family and out-family leaves in the interior of F separate at all. For
  the two adapted families that separation is O(ε)|y|², as S-T5 §5.3 agrees, and it is generically nonzero.

I did not re-derive S-T5's formula (2.1).

---

## 1. GN1: the faces are leaves of both families

### 1.1 The chart: face sections are the data's double-null spheres

**Claim (i).** Let τ′ be a chart time that is a smooth function Φ(u0, v0) of the background's double-null coordinates
on 𝒩, with Φ_u, Φ_v > 0. Then:
- Σ_τ′ ∩ 𝒞_out = {u = 0, v = c(τ′)} and Σ_τ′ ∩ 𝒞_in = {u = c′(τ′), v = 0}, with c and c′ strictly increasing;
- these are the data's double-null spheres, provided Tier 1's L1 places the data by the background's coordinate map.

**Proof.**
- **The face restrictions.** On 𝒞_out, τ′ = Φ(0, v), which is strictly increasing in v. On 𝒞_in, τ′ = Φ(u, 0), which
  is strictly increasing in u.
- **Only the faces matter.** The proof uses only the restriction of τ′ to each face. So (i) holds for any chart time
  whose restriction to 𝒞_out is an increasing function of v and whose restriction to 𝒞_in is an increasing function
  of u.
- **Identification with the data.** L1 transports the data metric, given in the double-null form eq:loc-double-null on
  {u = 0}, to the chart X = (τ, x) by the background's map (u, v, ϑ, φ) ↦ (τ, x). So the data sphere {u = 0, v = c} is
  carried to the background sphere {u0 = 0, v0 = c}.
- **Two conditions this needs of L1 (it already does both).**
  - The data's v on 𝒞_out is identified with the background's v. prop:loc-cones keeps Ω the background's on 𝒞_out,
    so the normalisation of v is the background's.
  - The data's u on 𝒞_in is identified with the background's u, with the gauge b = 0 on 𝒞_in.
  ∎

**Instances.**
- **Chapter 81's τ = v̂ − R.**
  - Φ_u = −R_u > 0 by prop:two-dust-background (c).
  - Φ_v = v̂′ (1 − e^ψ f/2) > 0, since e^ψ f ≤ 1 (lem:class-speeds; cor:class-two-dust proof, 81:1647–1651).
  - On the faces this is 80:399: dR/dv̂ = f/2 ≤ 1/2 on 𝒞_out, and τ = −R(u, 0) on 𝒞_in.
- **The data's t = u + v (S-T4).** Φ = u + v.
- **The solution's own t = u_out + v_in (Lemma R).** On the faces u_out and v_in equal the data's coordinates (L9). So
  the same conclusion holds, with the solution's map in place of the background's.

**Numerical confirmation on chapter 83's background** (`gn1_chart.py`, the cone ODEs of sec:bg-data integrated at
rtol 10⁻¹¹):
- **On 𝒞_out.** R_u ∈ [−0.5003, −0.4700] on v ∈ [0, 8], and dτ/dv ≥ 0.5224 there. The identity dR/dv̂ = f/2 holds to
  5.6 × 10⁻¹⁷.
- **On 𝒞_in.** R_u ≤ −0.47 up to R = a = 0.7, which is reached at u = 8.55.
- **Width of F ∩ Σ_τ near the corner time τ_c = −5.** It grows linearly:
  - R_out − R_in = (0.8868 + 1)(τ − τ_c) = 1.887 (τ − τ_c);
  - here 0.8868 = R_v/(v̂′ − R_v) at S, with v̂′ = 0.5/0.47.

### 1.2 The leaf criterion (exact, if and only if)

**Lemma (criterion).** Let V = (g, p_A, Θ_A, q_A) lie in the ball 𝔅′ of lem:class-leaf-differences, so that its A-leaves
exist and foliate a neighbourhood of the axis. Let S ⊂ Σ_τ′ be a G-invariant 3-sphere that meets axis 2 near p, with
S ∩ M3 a graph z = h_S(y) over the disc and p_A(∂_z) ≠ 0 there. Then S ∩ M3 is V's A-leaf through its axis point if
and only if, along S near the axis:
- **(a)** p_A annihilates TS (its spatial part is conormal to S in Σ_τ′), and
- **(b)** Θ_A = θ_S[p_A; g] := −tr_TS p_A(∇^g_X Y), the expansion of S along g⁻¹p_A, computed with V's own metric.

**Proof.**
1. **Decompose ∇_X Y.** For X, Y tangent to S, write ∇_X Y = ∇^S_X Y − k(X, Y) ν + K_Σ(X, Y) n. Here ν is the unit
   normal of S in Σ_τ′, k(X, Y) = g(∇_X ν, Y), and K_Σ is as in lem:class-gauss; the last term is the Gauss formula of
   that lemma's proof.
2. **Contract with p_A.** By (a), −p_A(∇_X Y) = p_A(ν) k(X, Y) − p_A(n) K_Σ(X, Y).
3. **Trace.** Take the trace over TS = TΣ_L ⊕ ℝ e1. By invariance (prop:class-structure (a)), −p_A(∇_(e1) e1) = κ_A1. M3
   is totally geodesic and ν is tangent to it, so k restricted to TΣ_L is the second fundamental form of Σ_L in M3.
   With p_A(ν) = |p_A^Σ| this gives
   |p_A^Σ| H_geom(Σ_L ⊂ M3) = θ_S[p_A] − κ_A1 + p_A(n) tr K_Σ|_(TΣ_L).
4. **Compare with the leaf equation.** H_L[V] := (Θ_A − κ_A1 + p_A(n) tr K_Σ|_(TΣ_L))/|p_A^Σ| is step (1) of
   lem:class-planar-shear with Θ_A in place of Θ. So H_geom = H_L[V] on S exactly when (b) holds.
5. **Pass to eq:class-leaf-volterra.** For any graph, lem:class-leaf (c) is an identity, H_geom = a_L h″ + (terms free
   of h″). So H_geom = H_L[V] says that h_S solves (r h′)′ = r H_L/a_L − E_L. Since h_S′(0) = 0 (h_S is smooth and
   invariant), h_S solves eq:class-leaf-volterra.
6. **Uniqueness.** lem:class-volterra (uniqueness on [0, r0], then Picard–Lindelöf) makes h_S the leaf.
7. **Converse.** If h_S is the leaf, then H_geom = H_L[V] along it. If moreover (a) holds, (b) follows from step 3.
   Without (a), the leaf's normal is not the conormal p_A uses, so it is not S.
∎

**A point of definition for the writer.** In lem:class-leaf-differences, H_L[Θ_A] must be a function of position, as
lem:class-volterra takes H(z, r).
- So its "TΣ_L" must be fixed by the state: the γ3-orthogonal complement in TM3 of the spatial part of p_A. It cannot be
  the unknown leaf's tangent.
- On a section satisfying (a) the two agree.
- The text leaves this implicit (81:1326–1328). One clause fixes it.

### 1.3 The faces are common leaves

**Corollary (T3-1 (ii)).** Let V ∈ 𝔅′ carry on a face section S the formal values of (p_A, Θ_A) and the formal 1-jet of
g. Then S is V's leaf of **both** adapted families near each of its axis points.

**Proof.**
- **(a).** The formal phases are constant on S: ũ_out ≡ 0 on 𝒞_out, and ṽ_in = v_data is constant on the double-null
  sphere S by §1.1. So p̃_A = dũ_A annihilates TS.
- **(b).** The formal ũ_A is eikonal to infinite order on the faces (L2). So ∇²ũ_A(P, ·) = 0 there, and
  Θ̃_A = □ũ_A = tr_TS ∇²ũ_A = θ_S[dũ_A] by prop:class-structure (b), TS being a screen.
- Both quantities in (b) depend only on (p_A, Θ_A) at S and on the 1-jet of g at S.
∎

**Exactly what is needed of the state.**
1. (a) and (b) along each face section near its axis points.
2. For the family **tangent** to the face (out on 𝒞_out, in on 𝒞_in), θ_S uses only g along the face: χ along
   P_out ∝ ∂_v is half the v-derivative of the section metric (lem:loc-cone-equations proof).
3. For the **transverse** family, θ_S uses the first transverse jet: ∂_u g on 𝒞_out, ∂_v g on 𝒞_in.
4. Sufficient for both: the formal 0-jet of (p_A, Θ_A) and the formal 1-jet of g. No jet of p_A or Θ_A beyond order
   0 is used, and none of g beyond order 1.
5. Where the criterion is used:
   - in T3-5 by Û (all jets);
   - in T3-6 by U (formal jets after T3-5) and by U′ (Θ′ = div_g P_A, equal to the formal Θ on the faces because
     Δ_A vanishes to infinite order there);
   - in Lemma R by genuine solutions.

### 1.4 Computer algebra

**Setup** (`gn1_jets.py`, sympy 1.14, exact).
- **Metric.** The class metric eq:loc-double-null with **general jets**: Ω², γ_ϑ, b, e^(2A_c), e^(2A_s) and their u-, v-
  and ϑ-derivatives at the point are independent symbols. u and v are then exact null phases. No Einstein equation is
  needed, so this metric plays the formal solution.
- **Slice.** T = v − F(u, ϑ) with F = u(f1 + f2 ϑ) + f3 u²/2 and f1 < 0. It is face-adapted (T|_(u=0) = v) and tilted in
  a non-round way off the face. It covers t = u + v (F = −u).
- **Why this is exact.** Every quantity needs only the 1-jet of the metric and the 2-jet of T. So replacing the metric
  functions by first-order Taylor polynomials with symbolic coefficients loses nothing.
- **What is compared.** H_geom is computed **by brute force** from the induced metric of M3 in the coordinates
  (u, ϑ, φ2), with v = F(u, ϑ). H_L is computed from the formula with Θ = □u (respectively □v), κ1, n and K_Σ.

**Results, all simplifying to 0 identically.**

    H_geom − H_L[out, Θ = □u]                        = 0
    H_geom + H_L[in,  Θ = □v]  (dv^Σ = f1 du^Σ, f1 < 0) = 0
    θ_S[du] − □u = 0,    θ_S[dv] − □v = 0
    □u|_S = −G_v/(4 G0 W0) − E_v/(4 E0 W0) − C_v/(4 C0 W0)

**Controls** (`gn1_controls.py`, three trials with exact random rational jets).

| state on S | out-family | in-family |
|---|---|---|
| formal | 0 | 0 |
| g + u²G (formal 1-jet kept), Θ formal | 0 | 0 |
| g + uG (transverse jet changed), Θ formal | 0 | **0.048, −0.035, −0.090** |
| g + uG, Θ := θ_S[p; g + uG] (the criterion) | 0 | 0 |
| Θ + 0.01 | **−0.011, −0.012, −0.016** | **0.021, 0.020, 0.016** |

So the transverse family needs the transverse jet, the tangent family does not, and (b) is exactly the condition.

**Non-adapted slicing** (analytic). If T|_(u=0) = v − ε ϑ², then
- Σ ∩ 𝒞_out = {v = τ + εϑ²}, and dv restricted to it is 2εϑ dϑ ≠ 0, so (a) fails for the in-family;
- its in-leaf through the axis point is the level set {v = const} ∩ Σ, which crosses the face section.

### 1.5 Remarks

- **Agreement with S-T5 §2.1.** S-T5 states Lemma A as "a leaf iff u_A restricted to the face is constant on the
  section". For states with the formal jets that is (a), and (b) then holds automatically. The two agree.
- **The coordinator's O(ε) note.** Not used. The criterion is exact. A non-adapted family fails (a) at order one or at
  order ε alike.

**GN1 verdict: GO.**

---

## 2. GN2: uniform constants near the corner time

There are four places where a constant could degenerate as the face sections S_out(τ) and S_in(τ) approach each other.

### 2.1 The extension Û (L3, used in L4–L6): uniform

- **Why there is no slice-wise degeneration.** Û is built in spacetime: Borel's lemma along 𝒞_out with the jets a_j
  extended smoothly past S, then Borel along 𝒞_in with the residual jets. That the two face sections approach each
  other inside a slice is an artefact of slicing.
- **Why the corner correction is clean.** The residual jets vanish to infinite order at S by L2's corner compatibility,
  so the second sum is flat on {u = 0}.
- **What the constants depend on.**
  - The angle between the two transversal null hypersurfaces at S (g0⁻¹(du, dv) = −e^(−2σ)/2 ≠ 0), which is fixed.
  - Bounds on the jets of order ≤ k + 2.
- **The flatness estimates use two-sided spacetime distance**, so they are uniform near S as well.

### 2.2 The past region (T3-5): uniform, one component at a time

- **The components.** For τ > τ_c, P ∩ Σ_τ has two components, inside S_in(τ) and outside S_out(τ).
- **Why each is uniform.**
  - In the chart x = ρ x̂ (ρ a background radial function), each component is a ball or the complement of a ball,
    bounded by one round sphere |x| = ρ_±(τ), ρ_± ∈ [ρ_min, ρ_max].
  - Stein's operator for these, transported by the dilation x ↦ (ρ_0/ρ_±) x and averaged over G, is bounded on L² and
    H^(k−1) uniformly in τ.
- **How T3-2(a) is applied.** With V = Û, separately on each component. lem:class-leaf-differences (b) is applied on
  the whole 𝒰_2δ to U and Ŭ_± := U − 𝔼_±(U − Û).
- **Union versus components.** Extending from the union of the two components would need the extension to fill the thin
  gap F ∩ Σ_τ, and the constants would blow up (§2.3).
- **Assessment of S-T3's claim.** For P, the remedy "components one at a time" is correct and sufficient.
- **For τ ≤ τ_c** there is nothing to extend: P ∩ Σ_τ is the whole slice near the faces.

### 2.3 F ∩ Σ_τ (T3-6): Stein is not uniform, and no extension can be

**Why the problem arises.** F ∩ Σ_τ is a single shell of width w = 1.887 (τ − τ_c). S-T3's T3-2 extends from D = F ∩ Σ_τ.
"Components one at a time" does not apply, since there is one component.

**A uniform bound is impossible for any extension operator.**
- **The test function.** Take f ≡ 1 on the shell {5 ≤ |x| ≤ 5 + w} ⊂ ℝ⁴.
  - Every H¹(ℝ⁴) extension of f costs at least the H¹-capacity of the shell, which is positive uniformly in w.
  - But ‖f‖_(H¹(shell)) ~ w^(1/2).
- **The exact least ratio.** Computed with Bessel functions in `gn2_uniform.py` (b): the radial solutions I_1(r)/r inside
  and K_1(r)/r outside.

| w | 1 | 0.1 | 0.01 | 10⁻³ | 10⁻⁴ |
|---|---|---|---|---|---|
| least ‖Ef‖_(H¹(ℝ⁴))/‖f‖_(H¹(shell)) | 1.777 | 4.630 | 14.29 | 45.09 | 142.6 |

  The ratio grows like w^(−1/2) (ratio · √w → 1.4255). At order k − 1 the obstruction can only be worse (test functions
  polynomial in the normal variable); that was not computed.
- **Consequence.** As written, T3-2 cannot place Ŭ in 𝔅′ with a constant uniform in τ near τ_c. And the L² bound feeds
  a Gronwall argument that must start at τ_c.

**The fix: a leaf-wise version of lem:class-leaf-differences (b), T3-2(b).**
- **Why it applies in T3-6.** Both states, U and U′ (Θ_A replaced by div_g P_A), have the face sections as leaves:
  - (a) holds because p_A = du_A in F with u_A formal on the faces;
  - (b) holds because U = Û on the closure of P, and Δ_A vanishes to infinite order on the faces.
- **What follows.** The leaves of both states through points of F ∩ Σ_τ stay in F ∩ Σ_τ, as graphs over the whole disc
  𝔻_2δ. So nothing needs extending.
- **The statement.**

    ‖σ_A[U] − σ_A[U′]‖_(L²(D ∩ 𝒰_δ)) ≤ C ‖U − U′‖_(L²(D ∩ 𝒰_2δ))  whenever D is closed under the leaves of both,

  with C the constant of lem:class-leaf-differences (b), independent of D.
- **Proof.**
  - The proof of (b) is per leaf. The difference of the two leaves issued from one axis point solves the linearised
    leaf equation on the disc. lem:class-interior-regularity with j = 0 applies on that disc, and its right side
    evaluates U − U′ on the leaf, which lies in D.
  - The L² norm of the leaf difference on 𝔻_2δ, which that lemma needs on its right side, comes from the integrated
    form: the same axis point and the Hardy average of prop:class-flat-model (b).
  - The "shift of the foliation" term at x uses U′-leaves whose axis points lie between those of the U-leaf and the
    U′-leaf through x. Those axis points lie in D ∩ axis, an interval, so those leaves lie in D.
  - Integrating over the axis point, with ∂_(z0) h ∈ [1/C, C], gives the L²(D) norms.
- **Uniformity.** The width of D never enters: the estimate runs along the leaves, which span the full disc whatever
  the width, and the non-local operator acts only along leaves.

### 2.4 Numerical check of the leaf-wise estimate

**Model** (`leafmodel.py`, `gn2_uniform.py` (a)).
- **Metric.** γ3 of the form eq:class-m3-metric with non-constant A3, B3, C3, D3. H-fields as in
  lem:class-leaf-differences. Leaves integrated from the axis with the series start and DOP853 at rtol 10⁻¹².
- **The shell.** The region between the base leaves from z0 = 1.5 and z0 = 1.5 + w.
- **The perturbation.** δH = ε φ(s) cos(3r/(2δ)), where s is the normalised label (0 on the inner leaf, 1 on the outer)
  and φ is a bump on (0.15, 0.85). So both boundary leaves are leaves of both states.
- **Why the cosine factor.** A δH that is constant along leaves lies, to first order, in the kernel of the planar shear
  (σ_pl = ℓ − 2𝒜ℓ = 0 for constant ℓ). The first run used such a δH and gave ratios ≈ 6 × 10⁻⁵, which test nothing. It
  was replaced.

| w | ‖δσ‖_(L²(D, r<δ))/‖δH‖_(L²(D, r<2δ)) | boundary leaves moved | perturbed leaves stay in D |
|---|---|---|---|
| 0.2 | 0.10000 | 0.0 | yes |
| 0.05 | 0.09999 | 0.0 | yes |
| 0.0125 | 0.09999 | 0.0 | yes |
| 0.003125 | 0.09999 | 0.0 | yes |

sup |δσ|/ε = 0.2166 at every w, and ε = 10⁻⁵ keeps the response linear.

The ratio is flat in w: the leaf-wise constant does not see the width.

### 2.5 Lemma R (T3-8): uniform

- **Slicing.** Lemma R slices by t = u + v of the first solution.
- **Near the past corner.** D_t = R′ ∩ {t} is bounded by past-face sections, which are leaves of both solutions: the
  two agree to infinite order on the past faces, and genuine phases have their level sets as leaves. So T3-2(b) applies
  uniformly.
- **Elsewhere.** D_t has future-face sections, which are double-null spheres of solution 1 and hence common leaves of
  solution 1 only.
  - Use T3-2(a) with V = solution 1 and a first-disagreement argument: if the solutions agree up to t*, then
    ‖U2 − U1‖_(H^(k−1)(D_t)) → 0 as t ↓ t*, since U2 − U1 is smooth and flat on D_(t*).
  - So Ŭ ∈ 𝔅′ near t* whatever Stein's constant at the positive width w(t*).
  - The Gronwall step on [t*, t* + η] needs only a finite constant.
- **Near the future corner.** The width tends to 0 there. Stop at t_end − η and let η → 0.
- **Smallness.** None of this uses the size of either solution beyond membership of 𝔅′. That suits S-T4's request
  for a continuity argument.

**GN2 verdict: GO, provided T3-2 is split into (a) (extension, single-sphere components) and (b) (leaf-wise, both states
closed).**
- T3-6 uses (b).
- T3-5 uses (a).
- Lemma R uses (b) near the past corner and (a) elsewhere.
- S-T3's sentence "Taking the components one at a time keeps the constants uniform near the corner time, where the
  annulus F ∩ Σ_τ is thin" is wrong for F and must not be carried into the text.

---

## 3. GN3: the forcing is smooth

### 3.1 Statement

Let Û be the extension of T3-3. It is smooth on 𝒩, in 𝔅, and carries the formal jets on the faces
∂F := 𝒞_out⁺ ∪ 𝒞_in⁺, with the data extended past u1 and v1 (§4). Let û_A be a smooth function with the formal jets of
the phase (Borel). Put

    E_A := σ_A[Û] − σ(û_A; ĝ),

where σ(û_A; ĝ) is eq:class-shear-leaf for the level sets of û_A in the slices.

Then **E_A vanishes to infinite order on ∂F near the axes.** Hence 𝔄(Û) does too, and F̃ := 1_P 𝔄_ξ(Û) ∈ C^∞, with
‖F̃‖_(H^k) ≤ Cε.

### 3.2 Proof

Fix N. Write d(x) := dist(x, ∂F).

1. **Sandwich.** For x near the axes, Û's A-leaf through x lies over the disc within C d(x) of ∂F.
   - The Û-leaves form a smooth foliation in (τ′, z0, y): lem:class-leaf-differences, with smooth dependence on
     parameters as in step (4) of lem:class-planar-shear.
   - The face sections are Û-leaves (§1.3).
   - If τ′(x) ≥ τ′_c, compare with the face section in Σ_(τ′(x)). The labels differ by ≤ C d(x).
   - If τ′(x) < τ′_c, compare with S = leaf(τ′_c, z_S). The distance is ≤ C(|τ′(x) − τ′_c| + |z0(x) − z_S|)
     ≤ C d(x). S-T3 omits this case: a slice before the corner time contains no face section, and only τ-continuity
     of the leaves helps.
   - The same holds for the level set Λ_x of û_A through x.
2. **The level set nearly solves Û's leaf equation.** By §1.2,
   |dû^Σ| H_geom(Λ_x) = θ_Λ[dû_A] − κ1 + dû_A(n) tr K_Σ|.
   - θ_Λ[dû_A] − □û_A is a smooth function of (g, dg, dû, ∇dû) that vanishes where g⁻¹(dû, dû) and its gradient
     vanish, so it is O(d^N) on Λ_x.
   - p̂_A − dû_A and Θ̂_A − □_ĝ û_A are O(d^N) there.
   - So the graph of Λ_x solves Û's eq:class-leaf-volterra up to an O(d(x)^N) error in H.
3. **Volterra stability.** The contraction in lem:class-volterra is Lipschitz in H, and for r > 0 Gronwall applies.
   - So Û's leaf from the axis point of Λ_x is within C d^N of Λ_x in C¹, and in h″ through the equation.
   - The foliation's transverse derivative is bounded below. So the Û-leaf through x has its axis point within C d^N.
4. **Conclusion at x.** σ at x is fixed by h, h′, H_L and the 1-jet of g (eq:class-shear-leaf). So |E_A(x)| ≤ C_N d(x)^N.
5. **From pointwise bounds to flatness.** E_A is C^∞ on a two-sided neighbourhood of ∂F, since Û and û_A are smooth and
   the leaves are smooth in their parameters. A smooth function that is O(d^N) for every N has all derivatives zero on
   ∂F, by Taylor's formula in the normal direction. This replaces S-T3's "smooth dependence … with all derivatives",
   which is true but not needed.
6. **The residual of (Aug3).** It is a local part (flat) plus ½ χ_ax (σ(û_A)² − σ_A[Û]²) (flat by 5), plus differences
   of the local parts of S^ax and the Raychaudhuri right side of û_A (flat).
   - The formal jets satisfy the general Raychaudhuri equation identically: P(□u) = −|∇²u|² − Ric(P, P) for an eikonal,
     with |∇²u|² = κ1² + ½(Θ − κ1)² + ½σ² (eq:class-x).
   - Hence L2's jets may be computed "with the local equations", as S-T3 says, with Θ̃_A := □ũ_A on the axis
     generators.
7. **F̃.** It is C^∞ once ξ ≡ 1 on a neighbourhood of ∂F ∩ supp(Û − Ů) up to the final time, or once F̃ is cut off in
   spacetime where it is not used. Without this, (1 − ξ) A^0(Ů) ∂_τ(Û − Ů) jumps across ∂F where 0 < ξ < 1. That is a
   writer's detail, and Tier 1 has it too.
   - The bound: ‖F̃‖_(H^k) = ‖𝔄_ξ(Û)‖_(H^k(P)) ≤ Cε. The local part is O(ε) in C^(k+1). Both σ terms are within Cε of
     σ̊ in H^k, by lem:class-leaf-differences (a) for Û and for (ĝ, dû_A, □û_A) ∈ 𝔅.
∎

### 3.3 Numerical check

**Setup** (`gn3_order.py`). Same 2D model as §2.4. The "true" state is H0. The face is its leaf from z_f = 1.5. The
mismatch is δH = 0.5 sgn(Φ)|Φ|^m with Φ = z − h_face(r). δσ is computed at the point at depth d on the base leaf with
r = 0.3.

| m | δσ at d = 0.08, 0.04, 0.02, 0.01, 0.005 | successive slopes |
|---|---|---|
| 1 | −1.664e−4, −8.350e−5, −4.183e−5, −2.094e−5, −1.047e−5 | 0.995 0.997 0.999 0.999 |
| 2 | −1.130e−5, −2.655e−6, −6.425e−7, −1.579e−7, −3.915e−8 | 2.089 2.047 2.024 2.012 |
| 3 | −1.250e−6, −1.558e−7, −1.950e−8, −2.440e−9, −3.052e−10 | 3.003 2.999 2.999 2.999 |
| 4 | −1.345e−7, −8.455e−9, −5.301e−10, −3.319e−11, −2.075e−12 | 3.991 3.995 3.998 3.999 |

**Negative control.** The mismatch is flat on a curve z = z_f + κr² that is not a leaf (Δκ = +0.3).

| m | δσ at d = 0.08 … 0.0025 |
|---|---|
| 2 | −6.2e−4, −3.4e−4, −2.0e−4, −1.3e−4, −9.6e−5, −7.9e−5 (plateau ~ (Δκ r²)^m) |
| 3 | −8.4e−5, −2.5e−5, −9.2e−6, −4.2e−6, −2.5e−6, −1.8e−6 (plateau) |

So without Lemma A the residual has a jump across the face. This is S-T5 §2.3's mechanism.

**GN3 verdict: GO.**

---

## 4. A further obstruction found: future boundaries in F, and the reach of Tier 3

### 4.1 The obstruction

- **Interior separation.** In the interior of F the two adapted families' leaves in a slice through a point x do not
  coincide. Both are flat to first order at their axis points, but they separate like c(x)|y|² with c = O(ε) and
  generically nonzero.
  - That is S-T3 §1.1; for adapted families the O(ε) is right (S-T5 §5.3).
  - On the background they coincide: every slice of a chart time Φ(u0, v0) is a union of round spheres. The
    perturbation makes τ′ a non-function of the solution's (u_out, v_in).
- **Consequence for a boundary leaf of one family only.** Let D ⊂ Σ_τ′ ∩ F have a boundary piece B that is a leaf of
  one family only. An example is the future face {u_out = u1} ∩ Σ_τ′. Unless c has the favourable sign at every axis
  point of B, which nothing provides, points of D within |c| r² of B have other-family arcs that leave D.
- **What breaks.** The non-local term of (Aug3), and of the defect equation in T3-6, then reads the state outside D, and
  neither T3-2(a) nor T3-2(b) applies.
- **Changing the slicing does not help.** In the solution's own t-slicing the future faces are common leaves. But U's
  closure uses the leaves of the chart slicing, not U's own t-leaves, and before T3-6 U is not known to be genuine.

### 4.2 Consequence for T3-6

- **What the energy region must look like.** The energy region for (D, Δ_A) must have slice sections bounded **only by
  face sections**: the slice-triangle T(s) := F ∩ {τ′ ≤ s}, with Σ_s meeting both faces inside the (extended) data and
  ξ ≡ 1 on T(s).
- **This is S-T3's "energy on F itself", made precise.** S-T3's alternative "F ∩ 𝒯′_A" is not needed for the two
  adapted families, which carry no ζ_A, so the defect equation holds on all of T(s). And it is not usable: the tube's
  lateral boundary is a leaf of U′ but not of U.
- **Chapter 81's τ on chapter 83's background** (`gn1_rect.py`, a second-order characteristic scheme, h = 0.005).

| point | R | τ = v̂ − R |
|---|---|---|
| (u, v) = (7.2, 4.5), far corner of a dust-carrying Q1 | 3.153 | **+1.540** |
| (7.2, 0) on 𝒞_in | 1.519 | −1.519 |
| (0, 4.5) on 𝒞_out | — | −2.540 |
| R = a = 0.7 on 𝒞_in (u = 8.55) | 0.7 | −0.700 |

- **Reading the table.**
  - No τ-slice through the far corner of Q1 meets 𝒞_in at all: that would need R = −1.54.
  - Even the largest τ-triangle inside G, with τ ≤ −0.70, misses the corner.
  - So with chapter 81's τ, T3-6 propagates the constraints only on a neighbourhood of the faces (compare Tier 1's G_*),
    **not on Q1**.

### 4.3 Remedy (keeps S-T3's "whole rectangle")

1. **Chart time adapted to Q1.** Take τ′ := Φ(u0, v0) with Φ_u, Φ_v > 0 on Q1^η := [0, u1 + η] × [0, v1 + η] ⊂ 𝒩 (L0
   gives such η), chosen so that Q1 ⊂ T(s*) ⊂ Q1^η. For example:
   - Φ = (u/a)^N + (v/b)^N + κ(u + v), with a = u1 + η, b = v1 + η, s* = 1, N large and κ > 0 small.
   - The level set {Φ = 1} meets the faces at u_* ∈ (u1, a) and v_* ∈ (v1, b), and passes beyond (u1, v1).
   - Spatial chart x := ρ x̂ with ρ := c0 + u0 − v0, which decreases strictly along the slices.
   - dΦ is timelike for g0 automatically. The constants depend on η, which is fixed.
2. **Extend the data.** Extend the free data and densities smoothly past u1 and v1 to u_* and v_*, with smallness kept,
   and solve the cone constraints along the extension (T3-0).
3. **Lemma R.** It shows that the solution on Q1 does not depend on the extension. S-T3 already lists this use. It must
   now carry the existence claim.
4. **Is chapter 81 usable in another chart?**
   - Every result used (lem:class-leaf-differences, lem:class-planar-shear, thm:class-kato, the Steps of
     thm:class-stability-off-axes) is stated for slices of a chart with spacelike slices. Only constants change (S-T3
     R5).
   - GN1 holds in this chart by §1.1.
5. **On t = u + v (S-T4).**
   - GN1 holds at no cost.
   - But its triangle {u + v ≤ s} reaches Q1 only with data on faces of length u1 + v1.
   - On chapter 83's background that is 11.7 on 𝒞_in, past R = a at u = 8.55. So t = u + v cannot carry a dust-carrying
     Q1 inside G, while the adapted Φ can.
   - Tier 4 should note this.

---

## 5. Verdict

| Check | Verdict | Condition |
|---|---|---|
| GN1 | GO | State T3-1 as the criterion (a)–(b) for any face-adapted chart time. Fix H_L[Θ_A]'s TΣ_L by p_A. |
| GN2 | GO | Split T3-2 into (a) extension (P components) and (b) leaf-wise (F, Lemma R near the past corner). Drop "components one at a time" for F. |
| GN3 | GO | Add the τ-continuity case at the corner. Make ξ ≡ 1 near ∂F ∩ supp(Û − Ů), or cut F̃ off. |
| §4 (new) | GO with change | Use a chart time adapted to Q1 and extended data. T3-6 runs on the slice-triangle. Lemma R carries the existence on Q1. |

**Route B stands.** The refined outline follows.

---

## 6. Refined lemma outline (T3-0 to T3-9)

Notation as in S-T3 §4:
- **Unknowns.** U = (g, p_A, Θ_A, q_A), A ∈ {in, out}, with D̃ = D(g) − W̊.
- **Faces.** ∂F = 𝒞_out⁺ ∪ 𝒞_in⁺ (extended data), F = {u ≥ 0, v ≥ 0} and P its complement.
- **Slices.** Σ_τ′ are the slices of the chart time τ′ = Φ(u0, v0) of T3-3.

Sizes are chapter lines.

**T3-0. Cone data through the axes. (60–90; unchanged from S-T3.)**
- prop:loc-cones and its 𝒞_in analogue hold on every generator, axis generators included.
- Variables ϕ̃, ℓ̃_i and the shift b ∂_ϑ (b odd).
- Per S-T4 §4.5 (4), cover the transverse jets of L2 on the axis generators as well.
- Add one sentence: the data extend past u1 and v1 inside 𝒩, with the constraints solved along the extension (needed by
  T3-3).

**T3-1. Lemma A. (50–70.)**
- **(i) Face sections.** For every chart time Φ(u0, v0) with Φ_u, Φ_v > 0, Σ_τ′ ∩ 𝒞_out = S_(0, c(τ′)) and
  Σ_τ′ ∩ 𝒞_in = S_(c′(τ′), 0), with c and c′ increasing. These are the data's spheres via L1. The proof is §1.1.
- **(ii) Criterion.** For V ∈ 𝔅′ and a G-invariant sphere S ⊂ Σ_τ′ meeting an axis transversally, S is V's A-leaf near
  that point iff (a) p_A(TS) = 0 and (b) Θ_A = −tr_TS p_A(∇_X Y). The proof is §1.2: the Gauss formula, prop:class-structure
  (a), lem:class-leaf (c), lem:class-volterra.
- **(iii) Common leaves.** If V carries on the face sections the formal (p_A, Θ_A) and the formal 1-jet of g, every face
  section is V's leaf of both adapted families.
- **Definitional sentence.** In lem:class-leaf-differences, TΣ_L in H_L[Θ_A] is the orthogonal complement of the spatial
  part of p_A.
- **Remark.** A further family satisfies (a) on a face only if its phase restricted to the face is constant on the face
  sections (S-T5 §2).

**T3-2. Non-local terms on sets closed under leaves. (100–150.)**
- **(a) Extension version.**
  - *Hypothesis.* D ⊂ Σ_τ′ is a component bounded near the axes by one sphere that is a V-leaf of every family whose
    S^ax is used there.
  - *Conclusion.* For U ∈ 𝔅′, ‖σ_A[U] − σ_A[V]‖_(L²(D ∩ 𝒰_δ)) ≤ C ‖U − V‖_(L²(D)), provided Ŭ := U − 𝔼(U − V) ∈ 𝔅′.
  - *Uniformity.* Uniform when the component is a ball or a ball's complement, of radius in a compact interval, after a
    dilation.
  - *Proof.* As in S-T3 and in the proof of lem:loc-lens-dependence step (6).
- **(b) Leaf-wise version.**
  - *Hypothesis.* D ⊂ Σ_τ′ is closed under the leaves of both U and U′: each leaf through a point of D ∩ 𝒰_δ lies, as a
    graph over 𝔻_2δ, in D.
  - *Conclusion.* ‖σ_A[U] − σ_A[U′]‖_(L²(D ∩ 𝒰_δ)) ≤ C ‖U − U′‖_(L²(D ∩ 𝒰_2δ)), with C that of lem:class-leaf-differences
    (b). C is independent of D, and in particular of its width.
  - *Proof.* The proof of (b), written per leaf (§2.3), with the L² bound on the leaf difference over 𝔻_2δ from the
    integrated Volterra form and the shift term handled as in §2.3.
- **(c) Remark.** No extension operator from a shell of width w is bounded uniformly in w (capacity; §2.3), so (a)
  cannot replace (b) near the corner time.

**T3-3. Chart, system, jets, forcing. (90–140; modifies L1, L2 and L4.)**
- **Chart.** τ′ = Φ(u0, v0) adapted to Q1 (§4.3), x = ρ x̂, with Q1 ⊂ T(s*) ⊂ Q1^η.
- **System.** As in S-T3 §4.2, with ξ ≡ 1 on a neighbourhood of T(s*), of the strip of P along ∂F ∩ {τ′ ≤ s*}, and of
  ∂F ∩ supp(Û − Ů) ∩ {τ′ ≤ τ′_fin}. Alternatively, multiply F̃ by a spacetime cut-off that equals 1 where T3-5 and T3-6
  use it.
- **Jets.** As in L2, with the local equations. On the axis generators take Θ̃_A := □ũ_A.
- **Forcing.** The non-local residual vanishes to infinite order (§3.2, including the τ-continuity step at the corner).
  So F̃ := 1_P 𝔄_ξ(Û) ∈ C^∞ and ‖F̃‖_(H^k) ≤ Cε.

**T3-4. Existence on ℝ⁴. (60–100; as S-T3.)**
- thm:class-kato (a) on 𝒟_ρ, with the bootstrap of Steps 4–8 of thm:class-stability-off-axes plus Step 6 of
  thm:class-stability, on ℝ⁴, with no lateral boundaries and no restarts. thm:class-kato-stability (a) is not usable,
  since ρ < ∞.
- Smoothness and G-invariance as in thm:class-stability.
- Constants are those of the chart of T3-3.

**T3-5. The past region. (60–90.)**
- **Statement.** U = Û on the closure of P ∩ {τ′ ≤ s*}.
- **Energy.** With coefficients at Û on all of P ∩ {τ′ ≤ s*}. U and Û solve 𝔄_ξ(·) = F̃ on all of P, F̃ being
  1_P 𝔄_ξ(Û), and U − Û has compact support in each slice. The faces are null for Û, so the flux through them is ≥ 0.
  Far from the faces Û = Ů, whose leaves are round spheres, so the exterior component is closed under Û-leaves.
- **Non-local part.** T3-2(a) with V = Û, separately on the two components for τ′ > τ′_c.
- **Close.** Gronwall from Σ_init.
- **Consequence.** U carries the formal jets on ∂F, so T3-1 (iii) applies to U.

**T3-6. Constraints on the slice-triangle. (90–130.)**
- **Region.** T(s*) = F ∩ {τ′ ≤ s*}. Its slice sections are bounded by face sections only.
- **ν_A and dp_A.** Every point of T(s*) lies on an integral curve of P_A back to the face transverse to it (P_in to
  𝒞_out, P_out to 𝒞_in). The curve stays in T(s*), since τ′ decreases and P_A is tangent to the other face. So ν_A ≡ 0
  and dp_A ≡ 0, and p_A = du_A.
- **D and Δ_A.** The energy for (D, Δ_A) runs on all of T(s*), with no tubes: no ζ_A for the adapted families.
  - Zero flux through the faces, by infinite-order vanishing.
  - The non-local term ½(σ_A[Θ_A]² − σ_A[div_g P_A]²) is bounded by T3-2(b) with U and U′: both have the face sections
    as leaves, by T3-5 and T3-1. The bound is uniform near τ′_c.
- **Do not use.** No region with a future face inside F (§4.1), and no extension by zero into P.

**T3-7. Double-null gauge through the axes. (30–50; as S-T3.)**

**T3-8. Lemma R; uniqueness, independence, localisation. (130–190.)**
- **Statement.** Two smooth class solutions in the same wave gauge, with W̊ on R′ depending only on R′'s face data (L1
  local), that agree to infinite order on the past faces of a double-null rectangle R′, agree on R′.
- **Proof.**
  - Use the first solution's t = u + v. Genuine solutions satisfy the axis closure in any slicing, σ being intrinsic.
  - Near the past corner use T3-2(b). Elsewhere use T3-2(a) with V = the first solution, and a first-disagreement
    argument in t (§2.5; this also meets S-T4's request that the argument not use the size of either solution).
  - Stop at t_end − η and let η → 0.
- **Uses.**
  - **Existence on Q1** (new weight). The solution of T3-4–T3-6 on T(s*) ⊃ Q1 does not depend on the extension of the
    data past u1 and v1.
  - Uniqueness on Q1 (L10's conversion to wave gauge, then Lemma R).
  - Localisation in (u, v), with the background as the first solution.
  - Angular localisation near an axis that the supports do not reach.

**T3-9. Statement, chapter-83 corollary, remarks. (60–100.)**
- Theorem on Q1, for Q1 with Q1^η ⊂ 𝒩.
- **Remark on the chart.** Chapter 81's own τ = v̂ − R reaches only a neighbourhood of the faces (the numbers of §4.2).
- **Remark on families** (S-T3 §5.2 as corrected by S-T5).
- **Recommendation.** State Tier 3 for the two adapted families plus further families whose densities vanish near the
  axes on T(s*); refer to S-T5 for the rest.
  - The reason: a further family that reaches an axis inside F needs a Step-10 energy region containing a full axis
    neighbourhood inside {ζ = 1}, which conflicts with ζ = 0 near the face–axis points.
  - This was not resolved here.

**Size.** About 730–1,110 lines in all: T3-1 +10, T3-2 +30, T3-3 +20, T3-6 +10 and T3-8 +10 over S-T3's estimate.

---

## 7. Risks that remain

1. **R1 (moderate): T3-2(b) is a re-proof.** lem:class-leaf-differences (b) is a sketch (81:1348–1353). The per-leaf
   version must be written out: the L² bound on the leaf difference over 𝔻_2δ (Volterra or Hardy), the shift term, and
   the integration over axis points. Without it T3-6 has no uniform constant at τ′_c.
2. **R2 (moderate): the adapted chart.** Chapter 81 is applied in a chart other than sec:background's. The constants of
   lem:class-planar-shear, lem:class-leaf-differences and the Sobolev steps must be re-taken in it (S-T3 R5). The slices
   of the example Φ are nearly null near the ends of the level set Φ = s*. Constants are finite for fixed η but
   unquantified.
3. **R3 (low to moderate): ξ near the far ends of the faces.** F̃ must be cut off consistently (§3.2 step 7). Otherwise
   F̃ ∉ H¹ where 0 < ξ < 1 on ∂F. Tier 1 has the same issue.
4. **R4 (moderate): further families reaching the axes inside F.** Not resolved (§6, T3-9). The recommendation is to
   exclude them.
5. **R5 (low): the H_L definition.** TΣ_L must be fixed by p_A (§1.2). This is one clause in chapter 81, but it
   touches confirmed text.
6. **R6 (low): the 2D model numerics** are a model of the leaf equation with chosen coefficients, not chapter 81's
   metric at a solution. They confirm mechanisms (exponents, uniformity in the width), not constants. No proof should
   cite them.
7. **R7 (carried from S-T3): T3-4.** Ball-restricted Cauchy stability on ℝ⁴. Unchanged.

---

## 8. Scratch files

All in `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/gnt3/`:

| File | What it does | Output |
|---|---|---|
| `gn1_jets.py` | GN1 identity for general jets (exact) | `gn1_jets.out` |
| `gn1_controls.py` | positive and negative controls (exact rational jets) | `gn1_controls.out` |
| `gn1_chart.py` | chapter-83 cone ODEs, τ on the faces, widths | `gn1_chart.out` |
| `gn1_rect.py` | background on the rectangle, τ at Q1's corner | `gn1_rect.out` |
| `leafmodel.py` | 2D leaf-equation model | — |
| `gn2_uniform.py` | leaf-wise uniformity and capacity bound | `gn2_uniform.out` |
| `gn3_order.py` | order of vanishing and negative control | `gn3_order.out` |

`gn1_leaf.py` is an earlier, too slow, fully symbolic attempt; it was superseded by `gn1_jets.py`.
