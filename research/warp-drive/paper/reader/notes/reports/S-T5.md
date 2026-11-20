# S-T5: non-adapted dust families crossing a face of the characteristic problem where it meets an axis

This is a scoping report for the writer. Nothing under `reader/` was edited, and `assemble.py` was not run.

**Read for this report.**
- notes/reports/S-CIVP.md (all of it); notes/reports/S-T3.md (all of it).
- proofs/P-CIVP.md (Block A: lem:loc-cone-in, thm:loc-cone-development, rem:loc-cone-scope) and the scope lines of
  proofs/P-CIVP2.md. Both now exist; both have N_f = 2.
- Chapter 81: lines 1–380, 540–700, 848–1671 (the phases, prop:class-separation, the augmented system, Kato's theorem
  with (F1)–(F5), thm:class-stability-off-axes, the axes, lem:class-leaf, lem:class-volterra, lem:class-leaf-differences,
  def:class-adapted, thm:class-stability, cor:class-two-dust, rem:class-scope).
- Chapter 83: 334–372, 440–475 (lem:loc-lens-dependence and its step (6)) and 525–601 (sec:loc-cones).
- Chapter 82: 1–40 and 180–250 (lem:vlasov-axis-stress, rem:vlasov-axis-density, lem:vlasov-axis-phases,
  prop:vlasov-axis-focus). Chapter 80: 380–420 (lem:two-dust-domain).
- The openings of chapters 29 and 43 (the Nash–Moser theorem thm:ii-g-2-1 and the tame estimates).

**The Tier 3 go/no-go report.** `reports/GN-T3.md` did not exist when this report was written (checked 2026-11-20).
This report therefore cites the Tier 3 plan by the lemma names of S-T3 §4 (T3-0 … T3-9, Lemma A, Lemma R).

**Scratch.** Two checks are in `scratchpad/st5/`. `leafcross.py` measures how far a non-radial leaf departs from a round
face section. `grazing_model.py` is the model transport behind §2.4. Both are quoted below.

---

## Summary

- **The problem splits into two cases, and the earlier reports did not separate them.** Take a point p where a face
  meets an axis, say p on 𝒞_out = {u = 0} with ϑ = 0. By lem:class-phase-axis, the gradient of every class phase at p
  is a multiple of dv or of du. So a further family present at p is one of two kinds.
  - **Crossing** (opposite orientation to the face: an ingoing family at 𝒞_out, an outgoing one at 𝒞_in). It is
    transverse to the face along the face's axis generator.
  - **Grazing** (same orientation as the face, and not resonant with it). Its null hypersurface is tangent to the face
    along the axis generator. Its speed across the face is −g⁻¹(du, du_A) = O(ϑ²), which is the separation defect of
    prop:class-separation (a). Its density on the axis generator is carried there from the corner, so a grazing family
    is present at a face–axis segment exactly when it is present at the corner's axis circle. On the other face it is a
    crossing family.
- **Why Tier 3 fails, in one sentence.** Lemma A (T3-1) needs each face section to be a leaf of every family whose axis
  closure S^ax is used there. A face section is such a leaf exactly when the family's phase, restricted to the face,
  is constant on it.
  - For a non-adapted family the leaf through a face point leaves the face at depth c r², where r is the distance to
    the axis.
  - For the paper's own non-radial family (lem:class-ellipse-phase), c = (α2² − α1²)/(2(α1 + d)(α2² + dα1)). This is of
    order one, not O(ε), and its sign changes between the two axes. The value was checked numerically to four digits.
  - The leak breaks all three Rendall steps: the forcing F̃ = 1_P 𝔄(Û) jumps across the face, U = Û on P (T3-5) fails,
    and constraint propagation in F (T3-6) fails. It also breaks Lemma R.
- **Crossing families: feasible.**
  - **Route S** works when, at each face–axis point, the crossing families present have functionally dependent
    restricted phases. Bend the chart time τ so that its face sections are their sections. This is S-T3's partial remedy.
  - **Route M** covers any number of crossing families. Give each family its own closure time t_A, whose face sections
    are that family's sections. Choose the evolution time τ bent towards the past near the axes, so that every leaf arc
    lies in the past of its endpoint. The non-local term is then a causal memory term.
  - Route M needs one new analytic theorem: Kato's iteration and energy estimates with forcing that is non-local along
    the leaves of several foliations. It avoids taking traces of σ_A on Σ_τ by using only spacetime L² norms of the
    source together with energies on every hypersurface of the family.
  - This corrects S-T3 §5.2: two functionally independent crossing phases at one point is **not** the open case.
- **Grazing families: a genuinely new difficulty, not provable with the paper's tools.** There are two independent
  obstructions.
  - (i) The face is characteristic for the family along its axis generator, a glancing set. The face jets of the phase
    and the density are obtained by dividing by ∂_v U_A and by the transverse speed, both O(ϑ²). Smooth developments
    exist only for compatible data: along the generator, the ϑ^(2j) coefficients of the data are fixed by their corner
    values (for the phase, the first is a Riccati equation). Free smooth face data give densities that are functions
    of u/ϑ² near the generator.
  - (ii) In **every** slicing the family's leaves through face points leave the face on a fixed side. That side is set
    by the relative planar curvature along the generator, which obeys a Riccati equation. So no slicing, and no
    per-family slicing, closes Rendall's argument.
  - No caustic is involved. The phase is smooth, and caustics are excluded by hypothesis as usual.
- **What is provable for grazing families now (statement W).** A development, unique in the gauge, exists on the
  domain of dependence of the faces minus a neighbourhood N of the grazing face–axis set. Cut the grazing densities off
  in N, re-solve the cone constraints on those generators (localisation by generators), apply Tier 3, and use finite
  speed. This region avoids the axes near the grazing segments. About 60–120 lines.
- **Size.**
  - Route S: 150–250 lines on top of Tier 3.
  - Route M: 900–1,400 lines on top of Tier 3 (18–28 PDF pages), with four go/no-go checks.
  - Statement W: 60–120 lines.
  - Grazing families in full: a research problem; no responsible estimate is possible, but at least 2,000 lines, with
    high risk.

---

## 1. The problem, precisely

### 1.1 The data

- **Faces.** Chapter 83's characteristic data on 𝒞_out^(v1) = {u = 0, 0 ≤ v ≤ v1} and 𝒞_in^(u1) = {v = 0, 0 ≤ u ≤ u1}
  (sec:loc-cones), in the gauge eq:loc-double-null, with corner S (P-CIVP, Block A).
- **The two adapted families** (thm:loc-cone-development).
  - Ingoing: phase v, density q_in, free on 𝒞_out.
  - Outgoing: phase u, density q_out, free on 𝒞_in.
- **Further families** A = 3, …, N_f.
  - Each is a G-invariant phase u_A, an eikonal without caustics on a neighbourhood of Q1 × S³, as allowed in
    cor:class-two-dust.
  - On each face where it is transverse, its data are the restricted phase U_A and its density.
  - Its transverse derivative on the face follows from g⁻¹(du_A, du_A) = 0 and the inverse metric of the proof of
    lem:loc-cone-equations:

        ∂_u u_A = Ω² (∂_ϑ U_A)² / (γ_ϑ ∂_v U_A) − b ∂_ϑ U_A      on 𝒞_out.                          (1.1)

  - The cone constraints take further sources. On 𝒞_out:
    - T(∂_v, ∂_v) = q_in + Σ_A q_A (∂_v U_A)²;
    - T(∂_v, ∂_ϑ) = Σ_A q_A ∂_v U_A ∂_ϑ U_A. This term is nonzero, unlike for adapted dust, but it only adds a source
      to the linear ODE for ∂_v b in prop:loc-cones.
- **Already covered elsewhere.**
  - Off the axes any number of families is local in chapter 81 and fits Tier 1; P-CIVP states only N_f = 2.
  - Tier 3 (S-T3 §4.1) allows further families whose densities vanish near the points where a face meets an axis.

### 1.2 The face–axis set and the dichotomy

- **The face–axis set.** Let Γ := (𝒞_out ∪ 𝒞_in) ∩ (axis 1 ∪ axis 2). In the orbit space it is four segments:
  {u = 0, ϑ ∈ {0, π/2}, 0 ≤ v ≤ v1} and {v = 0, ϑ ∈ {0, π/2}, 0 ≤ u ≤ u1}. In space-time each segment is a
  two-dimensional null surface ruled by **axis generators**. Γ meets the corner in the two **corner axis circles**.
- **A family present at p ∈ Γ** is one whose density is nonzero in every neighbourhood of p. Only such families need
  S^ax near p. Others are cut off by ζ_A, as in Step 6 of thm:class-stability.
- **Lemma (dichotomy).** Let A be a further family and J a connected piece of Γ ∩ 𝒞_out. Then on J either
  - (C) du_A is a multiple of dv: A is **crossing** at J; or
  - (G) du_A is a multiple of du: A is **grazing** at J.

  The same holds on 𝒞_in with u and v exchanged.

  *Proof.* By lem:class-phase-axis, at each axis point du_A lies on one of the two null lines of span(dτ, dr). It is
  nonzero (no caustic) and continuous, so it stays on one line along the connected J. ∎
- **Properties of the two kinds.**
  - **(C) Crossing families.** ∂_v U_A ≠ 0 on J. The level sets of U_A are sections of the face, v = V_A(c, ϑ²). The
    family is **adapted** at J if V_A does not depend on ϑ² near J, that is, if its sections are the double-null
    spheres used by Tier 3.
    - The family's ray at J runs along the axis and leaves the face transversally into F. Its transverse speed is
      −g⁻¹(du, du_A) ≠ 0 (compare prop:class-separation (b)).
    - Its density at J is free data on 𝒞_out.
  - **(G) Grazing families.** At J, P_A is parallel to the face generator, and both are geodesic. So u_A is constant
    along the axis generator, and P_A = λ g⁻¹du with λ constant on it.
    - On the face, U_A = α0 + a1(v) ϑ² + O(ϑ⁴).
    - The family is non-adapted unless U_A ≡ α0 near J, in which case it is resonant with the face's own family, as in
      prop:class-separation (d).
    - The transverse speed is −g⁻¹(du, du_A) = O(ϑ²). In Minkowski space, for the radial phase and the ellipse phase
      of the same orientation, it is exactly 1 − cos β ≈ β²/2 with β/ϑ → |α1² − α2²|/(α2² + dα1)
      (prop:class-separation (a)).
    - The density on the axis generator obeys P_A(q_A) = −Θ_A q_A along the generator. So it is carried from the corner
      and is not free.
    - Hence **a family is grazing and present at J if and only if it is present at the corner's axis circle with that
      orientation.** On the other face it is crossing.
    - In the terms of prop:class-separation (c): grazing families are exactly the families that are not angularly
      separated, at the axis, from the face's own family.
- **Concrete examples.** For lem:class-ellipse-phase's ellipsoid E, w₊ = τ + d_E is ingoing: crossing on 𝒞_out and
  grazing on 𝒞_in. w₋ = τ − d_E is outgoing: grazing on 𝒞_out and crossing on 𝒞_in. On the two-dust background the
  analogous non-radial eikonals of cor:class-two-dust behave the same way.

### 1.3 The question

"Non-adapted families crossing a face at an axis" means data with a further family A present at a point p ∈ Γ and
non-adapted there. It is either crossing with V_A depending on ϑ² near p, or grazing and not resonant. The theorem
wanted is Tier 3's theorem (S-T3 §4.1: small data near the background, whole rectangle Q1 × S³, gauge
eq:loc-double-null, uniqueness and localisation) **without** the hypothesis that further families vanish near Γ.

---

## 2. Why Tier 3 fails

### 2.1 What Lemma A uses

- **Leaves.** The closure S^ax of family A at x uses σ_A[Θ_A](x), the planar shear of A's leaf through x in the slice.
  The leaf is computed by the Volterra equation eq:class-leaf-volterra from the axis to x (lem:class-leaf-differences).
- **Lemma A (S-T3 T3-1).** For every state carrying the formal 1-jets on the faces, a face section is that state's leaf
  for family A if and only if u_A restricted to the face is constant on that section.
  - *Proof.* H_L depends only on the 1-jet. If U_A is constant on the section, the section is a level set of the formal
    phase, so it solves the Volterra equation, and lem:class-volterra gives uniqueness. Conversely, a leaf is a level
    set of u_A for the formal jet. ∎
- **The adapted families.** On 𝒞_out, u ≡ 0 is constant on every section, in **any** slicing. v is constant on the
  sections {v = c}, which are the face sections of Tier 3's chart time τ = v − R (80:399, lem:two-dust-domain).
  Symmetrically on 𝒞_in. This is the whole content of S-T3's "observation".

### 2.2 How far a non-adapted leaf leaves the face

- **Set-up.** In a slice, near a face–axis point, write the face section and the leaf of A through the same axis point
  as graphs z = h_F(y) and z = h_A(y) over the disc (lem:class-leaf). F is the side z < h_F for 𝒞_out.
- **Size.** Both graphs are even with the same value at y = 0. So h_A − h_F = c |y|² + O(|y|⁴), and c is the
  difference of their planar curvatures.
- **The paper's own example.** Take a round face section and the ellipse family. A's leaf is the outer parallel surface
  of E at distance d. Then

      c = (α2² − α1²) / (2 (α1 + d)(α2² + dα1))      near axis 2 (α1 ↔ α2 near axis 1).               (2.1)

  `leafcross.py` checks this:

  | α1, α2 | measured (h_A − h_F)/y² at y = 0.2, 0.1, 0.05, 0.025 | formula (2.1) |
  |---|---|---|
  | 1/2, 1/3 | −0.040609, −0.040394, −0.040340, −0.040327 | −0.040323 |
  | 1/3, 1/2 | +0.043238, +0.043137, +0.043112, +0.043106 | +0.043103 |

- **Consequences.**
  - c is of order one for a genuinely non-round family. S-T3 §1.5 quotes "O(ε)|y|²", which is right only for the
    adapted families after perturbation.
  - The sign of c is opposite at the two axes. The same factor |α1² − α2²| controls β/ϑ in prop:class-separation (a).

### 2.3 What the crossing breaks

Bending sets which side is closed under leaves:
- If the leaves bend towards P (h_A − h_F increasing along arcs from the axis), F is closed under the arcs from the
  axis and P is not.
- If they bend towards F, P is closed and F is not.
- Only c ≡ 0, that is exact adaptation, closes both. Only exact adaptation also gives the **sandwich**: the arc of a
  point at depth d from the face stays within O(d) of the face.

Each Tier 3 step then fails for a stated reason.

- **T3-3, the forcing.**
  - The non-local residual of the extension Û at x ∈ P is controlled by Û on x's arc. That arc reaches depth d + |c|r²,
    not O(d).
  - Û agrees with a formal solution only to O(dist^∞), so the residual is O((d + r²)^∞).
  - At face points it is O(r^∞): flat at the axis but **nonzero** for r > 0.
  - So F̃ = 1_P 𝔄_ξ(Û) has a jump across the face. It is not in H¹, and thm:class-kato does not apply.
  - The same holds for crossing families in Tier 3's slicing. This is why S-T3's GN3 needs Lemma A.
- **T3-5, U = Û on P.** When leaves bend towards F, the arcs of P-points enter F, where z = U − Û is not controlled by
  the energy on P. The Gronwall argument gets a source that is not bounded by e(τ).
  - A continuity argument does not save it. If z = 0 on P up to time τ, then z = O(d^N) in F near the face, which
    bounds the leak by C_N r^(2N) ‖z‖_(C^N). That bound is small, but it is not zero.
- **T3-6, constraints in F.** When leaves bend towards P, the arcs of F-points enter P, where the defects of Û do not
  vanish. Tier 3 deliberately does not extend D and Δ_A by zero, and that step is still needed here.
- **T3-8, Lemma R.** The slices of t = u + v are the double-null spheres. They are leaves of u and v only.

For the ellipse family both T3-5 and T3-6 fail somewhere, because c changes sign between the two axes.

### 2.4 Why no single slicing works, and why grazing families resist every slicing

- **Crossing families, one at a time.** The face sections of τ are free. Bending them to v = V_A(c, ϑ²) makes A adapted.
  This is S-T3 §5.2's partial remedy, Route S below.
- **Two crossing families.** If two crossing families present at one point have functionally independent restricted
  phases, no single section is a level set of both. The adapted ingoing family v counts here wherever the shell is
  present, on 𝒞_out ∩ {3 < v < 4.5}.
- **Grazing families: no slicing helps.**
  - U_A = α0 + a1(v)ϑ² + … is constant only on the axis generator. Its other level sets are tubes about the generator,
    not sections. So **no** section of the face lies in a level set of u_A, and Lemma A fails in **every** slicing.
  - The side is also fixed. On a face section, u_A − α0 ≈ a1 ϑ². So A's leaf through the axis point lies on the side
    where u_A − α0 = 0, displaced by about −a1 ϑ²/∂_n u_A. This holds whatever the slicing.
  - The planar curvature difference δ along the shared generator obeys δ′ = −δ² − 2κ2^face δ. Both κ2's satisfy
    eq:class-torus-riccati with the same P up to a constant factor and the same curvature term, and prop:class-axis (d)
    gives κ2 at the axis.
  - So δ vanishes identically or nowhere, until a caustic. Generically one of P, F is not closed under leaves in any
    slicing, and the forcing is never smooth.
- **Grazing families also break the data.**
  - For a grazing family, ∂_v U_A = a1′ϑ² + …, so (1.1) divides by O(ϑ²). The first jet is still smooth when a1′ ≠ 0:
    ∂_u u_A → 4Ω²a1²/(R² a1′) on the axis.
  - That value must be carried along the generator by (Aug2). This turns into a Riccati equation for a1. In the flat
    model w = t − |x − x0|, a1 = −1/(2(v − z0)) and a1′ = 2a1².
  - The density is worse. Its transverse jet ∂_u q_A comes from P_A(q_A) = −Θ_A q_A divided by the transverse speed,
    which is O(ϑ²).
  - In the model w ∂_u q + ∂_v q = 0 with w = ϑ² (`grazing_model.py`), the solution is q = F(u − wv, w), and on the
    side fed through the face q = Q(−s/w, w) with s = u − wv. It is smooth at the generator **if and only if** the
    coefficient of w^j in the face data Q(v, w) is a polynomial in v of degree at most j.
    - Q = v w and Q = v² w² give q = −s and q = s², which are smooth.
    - Q = v and Q = v² w give q = −s/w and q = s²/w, which are not.
  - The conditions at j = 0 are the transport along the generator. The higher ones are new and are not satisfied by
    generic smooth data.
  - The rays through the corner form a seam 𝒮_A that meets 𝒞_out tangentially along the generator: a cusp u ≈ c ϑ² v.
    So the corner compatibility couples data near the corner on 𝒞_in to data along the whole axis generator of 𝒞_out.
- **This is a glancing characteristic boundary, not a caustic.** The phase is smooth. A blow-up of a1 along the
  generator would be a focal point on the face, which the caustic-free hypothesis excludes.

---

## 3. Literature, verified

Search route: the Firecrawl research index, alphaXiv full text, and arXiv. Each source was opened at the pages cited
unless marked "abstract only". The sources of S-CIVP §2 and S-T3 §2 are not repeated except where something new was
checked.

| Source | Setting | Families / momenta relative to the faces | At an axis | Use here |
|---|---|---|---|---|
| Taylor, arXiv:1602.02611 (Ann. PDE 2017) | 3+1, no symmetry, massless Vlasov, characteristic semi-global | f smooth on the mass shell; f = 0 on {u = u0}; on {v = v0} the support obeys r²p³ ≤ C p⁴ and r²\|p^A\| ≤ C p⁴, so p⁴ = 0 forces p = 0 | none | non-adapted momenta are harmless for smooth f; data tangent to a face are excluded |
| Athanasiou–Mondal–Yau, arXiv:2510.12429 | 3+1, no symmetry, massless Vlasov, large-data semi-global | f smooth; support on H_(u∞) with 0 < p³ ≤ C, \|u\|²p⁴ ≤ C p³, \|u\|²\|p^A\| ≤ C p³; f = 0 on the other face | none | the same exclusion of momenta tangent to a face |
| Tadmon, arXiv:1109.6844 | 3+1, massive Vlasov, harmonic gauge, Goursat constraints only | the extra gauge assumption (3.2) turns the Vlasov data into integral equations (IS), (IE) | none | Vlasov data on null faces need not be free |
| Dossa–Patenou, arXiv:1608.01135 | Einstein–Vlasov–scalar, temporal gauge, two characteristic hypersurfaces | — | none | abstract only; not used |
| Luk–Rodnianski [LR20], arXiv:2009.08968 | 3+1, two null dusts, measures | **adapted** to the double-null foliation (abstract: "adapted to a double null coordinate system") | none (S²) | no non-adapted dust in the only general dust theorem |
| Moschidis, arXiv:1704.08685 | spherical Einstein–null dust, Λ < 0 | ingoing and outgoing radial dust | at the centre: "at the first point where the ingoing dust reaches the axis of symmetry, solutions become C⁰ inextendible" (abstract) | contrast: in the class, rays at a T² axis run along it (lem:class-phase-axis), and transversal arrival focuses (prop:vlasov-axis-focus) |
| Guo–Kim–Tonon–Trescases, arXiv:1212.1694 | kinetic transport and Boltzmann in convex domains | the grazing set γ₀ = {n·v = 0} | — | the closest analogue of grazing families (below) |
| Siebel–Font–Müller–Papadopoulos, gr-qc/0111093, gr-qc/0301127; Gómez–Papadopoulos–Winicour, gr-qc/0006081 | axisymmetric characteristic numerical relativity, perfect fluid or vacuum | fluid characteristics are timelike, never tangent to the cones | regular axis in the code | abstract only; no grazing matter, no theorem |
| Mädler–Müller, arXiv:1211.4980; Barbosa, arXiv:2611.08958 | Bondi–Sachs at a cone vertex and the polar axis | — | regularity forces "a very rigid angular structure" of the data (1211.4980, abstract) | abstract only; an analogue of the compatibility of §2.4 |

The entries in detail:

1. **Taylor**, Theorem 5.1 (pp. 34–35).
   - The data on {v = v0} satisfy "0 ≤ p⁴ ≤ C_(p4), 0 ≤ r²p³ ≤ C_(p3) p⁴, |r² p^A| ≤ C_(pA) p⁴", and "f|_(π⁻¹({u=u0})) = 0".
   - So momenta tangent to {v = v0} (p⁴ = 0) carry no f, and the other face carries none at all.
   - The local characteristic theorem used in the last-slice argument, Theorem 12.2 (p. 119), is quoted, not proved:
     "The analogue … for the vacuum Einstein equations is a result of Rendall [28]. For the Einstein–Vlasov system see
     also [11], [5]."
   - What it shows: with f smooth in momentum, velocity averaging removes the derivative loss, and momenta in every
     direction are allowed. The exclusion of momenta tangent to the data surfaces is part of the hypotheses. That
     exclusion is the Vlasov counterpart of excluding grazing families.
2. **Athanasiou–Mondal–Yau**, Theorem 1.2 (pp. 5–6).
   - 3+1, "without any symmetry assumptions", f smooth.
   - Momentum support (1.5): "0 < p³ ≤ C_(p3), 0 ≤ |u|²p⁴ ≤ C_(p4) p³, |u|²|p^A| ≤ C_(pA) p³" on H_(u∞), and "f|_(u=0) = 0".
   - p³ > 0 is the same exclusion. The authors call (1.5) "precisely the focusing condition for the Vlasov matter".
3. **Tadmon** (pp. 2–3, 11–13, Theorem 1). The Goursat constraints for Einstein–Vlasov in harmonic gauge.
   - "As a consequence of the additional assumption on the gravitational potentials, the distribution function can not
     be given as free data, it must satisfy some integral equations."
   - The evolution is "out of the scope of the present work".
   - No relevance to axes. Cited only as a second instance of matter data on null faces that are not free.
4. **Luk–Rodnianski.** Read in S-CIVP (Theorem 4.6, p. 29). The abstract confirms the scope: "all sufficiently regular
   solutions to the Einstein-null dust system … adapted to a double null coordinate system". Non-adapted families are
   outside the only general characteristic theorem for null dust, even in 3+1 without axes.
5. **Moschidis.** Abstract only, re-read. The breakdown is at the centre r = 0 of spherical symmetry, where radial dust
   arrives transversally. Chapter 82 shows the class analogue (prop:vlasov-axis-focus): restricted particles reaching an
   axis transversally make Ric unbounded. Smooth class phases avoid this because their rays at the axis run along it.
   So focusing at the axis is excluded by smoothness of the phase, and it is not the obstruction here.
6. **Guo–Kim–Tonon–Trescases** (pp. 1–5, 96–99).
   - The boundary splits into incoming, outgoing and grazing sets, "γ₀ = {(x, v) ∈ ∂Ω × R³ : n(x)·v = 0} (the grazing
     set)" (p. 2).
   - The normal derivative is obtained by dividing by n·v, eq. (20), p. 5: "Unfortunately, this standard approach
     encounters a severe difficulty: 1/(n(x)·v) ∉ L¹_loc".
   - They construct weighted C¹ solutions "away from the grazing set" with the kinetic distance α of Definition 2. The
     Appendix (p. 96) shows that "some second order spatial derivative does not exist up to the boundary in general".
   - The analogy is exact at the level of the mechanism. A grazing family's transverse jets on the face are obtained by
     dividing by the transverse speed g⁻¹(du, du_A) = O(ϑ²), and smoothness up to the face fails without conditions.
   - Their setting has collisions and a fixed geometry, so nothing transfers as a lemma. The model of §2.4 is the
     in-house statement.
7. **Numerical characteristic relativity in axisymmetry.** Abstracts only. The matter used there (perfect fluid, scalar
   field) has characteristics strictly inside the light cone, so it never grazes a null slice. Axis regularity there
   concerns the metric and the vertex. Mädler–Müller's "rigid angular structure" at a cone vertex is the nearest
   published counterpart of the compatibility conditions of §2.4, but at a point rather than along a generator.
8. **[CCTW16]**, as read in S-CIVP.
   - The doubly-null form (2.7)–(2.8) has A^u nonzero only on the ϕ block and A^v only on the ψ block. A transport along
     P_A = a∂_u + b∂_v + c∂_ϑ with a, b ≠ 0 lies in neither block.
   - So **Tier 2's engine excludes non-adapted families even off the axes**. Large-data versions with further families
     would need another engine.
9. **Chapter 82** (lem:vlasov-axis-stress, rem:vlasov-axis-density, prop:vlasov-axis-focus).
   - At an axis point, a restricted field with smooth stress has momenta in span(dτ, dr). Densities that do not
     concentrate on the axial directions give a stress that is not smooth.
   - This is the momentum-space form of lem:class-phase-axis, and it is what makes the crossing/grazing dichotomy
     exhaustive.

**Conclusion.**
- No source treats null dust that is not adapted to the data surfaces, with or without axes.
- The Vlasov characteristic theorems avoid the issue in two ways. Smooth f removes the closure problem, and the
  momentum-support hypotheses exclude momenta tangent to the data hypersurfaces.
- The kinetic theory of the grazing set confirms that the grazing case is a genuine loss of regularity, not an artefact
  of the method.
- No outside result is needed for Route S or Route M. Every step has a template in chapters 81 and 83 or in Tier 3.

---

## 4. Routes, verdict and plan

### 4.1 Routes considered

| Route | Idea | Crossing | Grazing | Length (on top of Tier 3) | Risk | Verdict |
|---|---|---|---|---|---|---|
| **S** | one evolution time; near each face–axis segment bend its face sections to the sections of the one crossing class present | yes, if at each point the crossing families are functionally dependent, with gaps between segments of different classes | no | 150–250 | low | **do first** |
| **M** | per-family closure times t_A adapted to that family's face sections; an evolution time τ bent to the past, so that every leaf arc is causal; Kato with several foliations | yes, any number | no | 900–1,400 | moderate to high | **recommended** for crossing families |
| F | "face-started" leaves: integrate the leaf ODE from where the arc meets the face, with face data there | — | — | — | — | rejected: the boundary term is h′(ρ₁)ρ₁/r² with ρ₁² ≈ r² − d/\|a\|. It is a degree-0 function of d/r², and ∫\|∇·\|² ~ ∫dρ/ρ, so it is not in H¹ |
| X | make Û an exact solution near the faces, so that leaks see no defect | — | — | — | — | circular: this is the backward characteristic problem with the same face–axis set |
| L | Luk/[LR20]-type double-null theory | non-adapted dust still loses a derivative; [LR20] is adapted only | — | 3,000+ | high | not a route for dust |
| NM | a local lossy closure −\|∇²u_A\|² for the grazing families near Γ, with the loss absorbed by thm:ii-g-2-1 (Nash–Moser with support classes) | — | conceivably | ? | very high | needs tame estimates for a linearised characteristic problem with a glancing transport; none exist |
| W | cut the grazing (or untreated crossing) data off near Γ; solve; use finite speed | partial | partial | 60–120 | low | **do**: it is the honest weaker statement |

### 4.2 Verdict

1. **Crossing families: provable.**
   - Route S gives at once the case of one crossing class per face–axis point. This covers a single added ingoing family
     on 𝒞_out away from the shell's v-range, or resonant families f_A(v).
   - Route M gives the general case, including families crossing the shell at the axes.
   - Hypothesis (H×): near each point of Γ ∩ 𝒞_out, every non-adapted family with nonzero density is ingoing-type, and
     near each point of Γ ∩ 𝒞_in every such family is outgoing-type.
   - For families whose density does not vanish on the axis generators, (H×) is equivalent to: no non-adapted family is
     present at the corner's axis circles.
2. **Grazing families: not provable with the tools of the paper.** Exactly why:
   - (i) The face is characteristic for the family along its axis generator. Data must lie in a compatible class
     (§2.4), which the theorem would first have to describe and prove sufficient for smoothness up to the face.
   - (ii) No slicing makes the face sections leaves of the family (§2.4). So the closure is not causal relative to the
     face, Rendall's forcing is not in H¹, and neither U = Û on P nor constraint propagation in F closes.
   - These are two independent new problems.
   - What is provable is statement W (§4.4). Off the axes nothing changes: Tier 1 with further families.

### 4.3 Plan for Route M

**Notation.**
- The further crossing families present near Γ are A ∈ 𝒜×. The adapted families are v and u.
- For each A present at a face–axis segment J ⊂ 𝒞 (𝒞 ∈ {𝒞_out, 𝒞_in}) on which A is crossing, write the A-sections of
  𝒞 near J as v = V_A(c, ϑ²) (respectively u = U^A(c, ϑ²)).
- Families present near Γ on a face where they are grazing are excluded by (H×).

**M0. Cone data with further families through the axes.** Extends T3-0 and P-CIVP's lem:loc-cone-in. 60–100 lines.
- *Statement.* prop:loc-cones and lem:loc-cone-in hold with further crossing families. The restricted phase U_A is free
  with ∂_v U_A ≠ 0, the density is free, the transverse derivative is given by (1.1), and the two constraint sources are
  those of §1.1. Everything is smooth on S³ with the parity and conical conditions. Localisation is by generators.
- *Proof.* As T3-0. The source Σ_A q_A ∂_v U_A ∂_ϑ U_A is tensorial ((Ric − T)(∂_v, ·) on the sections), and
  ∂_ϑ U_A = O(ϑ) is odd.
- *Check.* The jets of (1.1) are smooth because ∂_v U_A ≠ 0 on J. This is exactly where grazing families fail.

**M1. Times.** New. 80–120 lines.
- *Statement.* For δ_* small there are smooth G-invariant functions τ and t_A (A ∈ 𝒜× ∪ {u, v}) on a neighbourhood of
  Q1 × S³ and the collar such that:
  - (a) all are time functions, equal to Tier 3's chart time τ₀ = v − R outside {dist(·, axes) < 2δ_*};
  - (b) on each face near each segment J where A is present, the face sections of t_A are A-sections. For v on 𝒞_out
    and u on 𝒞_in these are the double-null spheres;
  - (c) **causality**: on every level set of t_A, within δ_* of the axes, τ increases with |y|. So every t_A-arc from the
    axis to x lies in {τ ≤ τ(x)};
  - (d) τ agrees at the corner from both faces.
- *Construction.*
  - Take τ = τ₀ + K ρ_ax² χ near the axes, ρ_ax the distance to the axis. On 𝒞_out this gives
    τ|_𝒞out = v + K ϑ² + O(ϑ⁴), whose face sections bend to the past.
  - Choose K > sup_A sup |∂_(ϑ²) V_A| on the δ_*-neighbourhood. Then along each A-section τ increases with ϑ².
  - Put t_A := τ − f_A, where f_A on the face is τ restricted to A-sections minus the section's value, and f_A is
    extended off the face, even in y and nondecreasing in |y|².
  - Spacelikeness needs |∇(K ρ_ax²)| ≤ 2Kδ_* small, which fixes δ_* after K.
- *Go/no-go GN-M1.* Construct τ and t_A explicitly on the background with the families w₊ = τ + d_E on 𝒞_out and the
  shell's v, and check (a)–(d) by computer algebra and numerics. The same machinery as `leafcross.py` will do.

**M2. Lemma A per family.** Replaces T3-1. 30–50 lines.
- *Statement.* For every G-invariant state in the ball 𝔅′ of lem:class-leaf-differences (in the t_A-slicing) carrying
  the formal 1-jets on the faces, each t_A-face section near J is that state's A-leaf.
- Consequence: P ∩ {t_A = c} and F ∩ {t_A = c} are closed under A-leaves, with the sandwich property.
- *Proof.* §2.1, in the t_A-slicing.

**M3. Leaf differences on tilted slices, and non-local terms on sets closed under leaves.** Replaces T3-2. 80–120
lines.
- *Statement.* lem:class-leaf-differences (a), (b) hold in each t_A-slicing with constants uniform in t. T3-2's estimate
  holds on each t_A-slice with D = P ∩ {t_A = c} or F ∩ {t_A = c}, through Ŭ := U − 𝔼(U − V).
- *Proof.* The proofs are intrinsic to a slice and use only its 1-jet geometry. Check uniformity as the two face
  sections approach each other near the corner (S-T3's GN2).

**M4. Kato's iteration with forcing non-local along several foliations.** New; the main analytic piece. 250–400 lines.
- *Statement.*
  - Let the forcing be F(τ, U) = F_loc(τ, x, U) + Σ_A 1_(supp ζ_A) Φ_A[U], where Φ_A[U](x) is computed on the level set
    {t_A = t_A(x)} from U there, by the leaf construction.
  - With M1 (c), Φ_A at time τ depends on U only on the slab {τ − Kδ_*² ≤ τ′ ≤ τ}: a causal memory.
  - Then thm:class-kato (a) and thm:class-kato-stability (a) hold in the norm
    𝔑_k(τ) := sup over the hypersurfaces H ∈ 𝓕(τ) of ‖U‖_(H^k(H)). Here 𝓕(τ) is the family of all Σ_τ′ and all
    t_A-level sets that lie in {τ′ ≤ τ}, on a ball about the reference path.
  - The conclusions are existence, continuation, uniqueness, smoothness and G-invariance.
- *Proof outline.*
  1. **Linear step.** For the symmetric hyperbolic system with coefficients at the previous iterate and forcing in
     L²_τ H^k, energy identities hold on every spacelike hypersurface between Σ_init and H. The forcing only needs to
     be in L² of space-time at top order. So bound ‖U^(n+1)‖ in 𝔑_k by data plus ∫∫ |∂^α f|².
  2. **The non-local source** is never restricted to Σ_τ. ∫∫_(region) |∂^α Φ_A|² = ∫ dt ‖∂^α Φ_A‖²_(L²({t_A = t})) by
     the coarea formula, and each slice term is bounded by M3 and lem:class-planar-shear from ‖U‖_(H^k({t_A = t})) ≤ 𝔑_k.
     This avoids the half-derivative loss of a trace on a tilted hypersurface.
  3. **Contraction** in L²: ‖Φ_A[U] − Φ_A[V]‖_(L²(Σ_τ)) ≤ C sup_([τ−Kδ_*², τ]) ‖U − V‖_(L²). This is (F2) with memory.
     It follows from Hardy averages along the arcs and the coarea change of variables (r, z) ↦ (τ′, z′), whose Jacobian
     on a t_A-arc is of order λr.
  4. **Smoothness and G-invariance** as in thm:class-stability ("Smoothness") and Step 9.
- *Go/no-go GN-M2.* Write the energy inequality for a toy model first: one wave field, two transports, and a Volterra
  leaf term on two foliations in 2+1. Check that the Gronwall closes with 𝔑_k and that no trace of Φ_A on Σ_τ is
  needed. Kill the route if the commutators [∂^α, leaf construction] on tilted slices produce a term that 𝔑_k does not
  bound.

**M5. The past region and the constraints.** Replaces T3-5 and T3-6. 150–220 lines.
- **(P) U = Û on P.**
  - The difference equation has coefficients at Û. The faces are null for Û, so the boundary form is ≥ 0, as in T3-5.
  - Local terms are ≤ C|z|. The non-local term of family A at x is bounded through M3 on the t_A-slice of x, with
    D = P ∩ {t_A = t_A(x)}. That slice lies in {τ′ ≤ τ(x)} by M1 (c), where z = 0 by induction.
  - Gronwall with memory gives z = 0.
- **(F) Constraints.**
  - ν_A and dp_A vanish along P_A from the transverse face, as in T3-6.
  - D and Δ_A: use the energy on F, or on F ∩ 𝒯′_A for Δ_A. There is zero flux through the faces, by infinite-order
    vanishing.
  - The non-local term ½(σ_A[Θ_A]² − σ_A[div_g P_A]²) is bounded on t_A-slices with V := U, whose face sections are
    A-leaves by (P) and M2.
  - The multi-foliation Gronwall of M4 then gives Δ_A = 0.

**M6. Jets and smoothness of the forcing.** Extends T3-3. 60–90 lines.
- Infinite-order vanishing of each family's non-local residual at the faces. Use the sandwich property in the t_A-slicing
  and the smooth dependence of the Volterra leaves.
- *Go/no-go GN-M3.* This is S-T3's GN3, per family, in the tilted slicing.

**M7. Lemma R per family; uniqueness; localisation.** Replaces T3-8. 100–150 lines.
- Two genuine solutions near g0 in the same wave gauge, agreeing to infinite order on the past faces of a double-null
  rectangle R′, agree on R′.
- Each family's closure is taken on slices adapted to R′'s faces (M1 for R′). For genuine solutions σ_A is intrinsic, so
  any slicing is admissible.
- *Go/no-go GN-M4.* The localisation statement on sub-rectangles {u ≥ u0} meets interior null hypersurfaces. Check that
  no family is grazing there with nonzero density, or restrict the statement.

**M8. Statement, corollary, remarks.** 80–120 lines.
- The theorem is S-T3 §4.1 with "further families vanishing near Γ" replaced by (H×).
- Add a remark naming the grazing case and statement W, and one sentence on Tier 2 (CCTW16 excludes non-adapted
  families).

**Order of work.**
1. GN-M1 and GN-M2 first, in parallel. They decide the route.
2. M0 and M1.
3. M2 and M3.
4. M4.
5. M5 and M6.
6. M7.
7. M8.

Route S can be written before any of this, as an add-on to Tier 3. It is M0, M1 with a single family per segment and
t_A = τ, and M2 with Tier 3's proofs unchanged.

**Placement.**
- Chapter 81: Route M's M4 belongs after thm:class-kato-stability, as a general tool.
- Chapter 83 or the Tier 3 section: M1–M3 and M5–M8.
- rem:class-scope: one sentence. The orientation dichotomy at Γ is the separation geometry of prop:class-separation (c),
  not the high-frequency construction.

### 4.4 Statement W (grazing families, or crossing families not yet treated)

- *Statement.* Let N be a neighbourhood, in the faces, of the face–axis segments where a family not covered (grazing, or
  crossing when Route M is not written) is present, together with the corner axis circles if they are involved. Let
  D := {p ∈ Q1 × S³ : J⁻(p) ∩ (𝒞_out ∪ 𝒞_in) ⊂ (𝒞_out ∪ 𝒞_in) ∖ N}. Then for small data there is a smooth class
  development on D in the gauge eq:loc-double-null, unique there.
- *Proof outline.*
  1. Multiply the uncovered densities by a G-invariant cut-off vanishing near Γ ∩ N̄ and equal to 1 outside N.
  2. Re-solve the cone constraints on the affected generators. They lie in N by localisation by generators
     (prop:loc-cones, lem:loc-cone-in).
  3. Apply Tier 3, which allows further families vanishing near Γ.
  4. Points of D see only uncut data, by finite speed (Tier 1's L7, in the form |Δϑ| ≤ C₀(ΔuΔv)^(1/2)), so the solution
     on D does not depend on the cut-off.
- *Remark.* When a grazing family is present along a whole axis generator (always the case once it is present at the
  corner), D stays at angular distance ≥ width(N) + C₀(uv)^(1/2) from that axis near the faces.
- 60–120 lines.

---

## 5. What stays open

### 5.1 Grazing families

There are two sub-problems.

- **(a) The glancing characteristic problem.**
  - Describe the face data of a grazing null dust that are traces of smooth solutions, and prove existence for them.
  - In the model, the coefficient of ϑ^(2j) along the axis generator must be a polynomial in v of degree at most j,
    after transport. For the full problem, the ϑ^(2j) coefficients of U_A and q_A must obey ODEs along the generator,
    the first a Riccati equation for a1.
  - The corner seam 𝒮_A is tangent to the face along the generator, so the corner compatibility is a cusp condition.
  - A finite-regularity or weighted version, in the style of Guo–Kim–Tonon–Trescases's kinetic distance, is a separate
    question.
- **(b) A causal, lossless closure near a grazing face–axis segment.**
  - Every slicing leaves the face on a fixed side (§2.4). So the planar shear would have to be recovered either from data
    on the face plus F, without the axis-started Volterra integral, or by accepting a loss and absorbing it (Route NM).
  - The obvious face-started variant fails to be in H¹ (Route F).

### 5.2 Unchanged from S-T3 §5

- Large data reaching the axes.
- Low regularity: measure-valued shells and C³ data.
- General 4+1 without symmetry.
- For further families there is one more restriction: Tier 2 cannot host non-adapted transports even off the axes
  (§3, item 8). A large-data theorem with further families needs another engine.

### 5.3 Corrections to the earlier reports

- **S-CIVP §3.7** cites rem:class-scope. S-T3 corrected this: rem:class-scope concerns the high-frequency
  construction. The instinct was nevertheless half right. Grazing families are exactly those not separated, at the
  axis, from the face's own family (prop:class-separation (c)), and their speed across the face is the separation
  defect of prop:class-separation (a).
- **S-T3 §5.2.** Its condition ("the face section must be a leaf of every family present") is right for one common
  slicing. With per-family slicings it weakens to "the face sections are among each family's own leaves". That holds for
  every crossing family and for no grazing family. So:
  - "two functionally independent transverse phases at one face-axis point" is **not** genuinely open (Route M);
  - the genuinely open case is the grazing family, which S-T3 does not single out. Its partial remedy (bending the
    slicing) is impossible for a grazing family.
- **S-T3 §1.5** says the crossing is "at distance O(ε)|y|²". That is true for the adapted families after perturbation.
  For a non-radial further family it is O(1)|y|², as (2.1) shows.

---

## 6. Estimate and risks

**Size** (about 49.5 chapter lines per PDF page):

| Piece | Lines |
|---|---|
| Route S (on top of Tier 3) | 150–250 |
| M0 | 60–100 |
| M1 | 80–120 |
| M2 | 30–50 |
| M3 | 80–120 |
| M4 | 250–400 |
| M5 | 150–220 |
| M6 | 60–90 |
| M7 | 100–150 |
| M8 | 80–120 |
| **Route M total** | **≈ 900–1,400 (18–28 PDF pages)** |
| Statement W | 60–120 |
| Grazing families in full | research problem; at least 2,000; not estimated |

- Route M presupposes Tier 3. P-CIVP (Tier 1) exists; the Tier 3 proof file does not yet exist.
- If Tier 3 is still to be written, writing it directly in Route M's form costs about 1,400–2,100 lines for both,
  instead of 1,550–2,400 for the two separately.
- Expect a writer and two to four confirming readings, as for Tier 1.

**Go/no-go checks for Route M:**
- GN-M1: the times of M1 on a concrete example.
- GN-M2: the multi-foliation energy inequality on a toy model.
- GN-M3: residual smoothness per family.
- GN-M4: localisation on interior null hypersurfaces.

**Risks.**
- **R1 (moderate to high): M4.** Kato's iteration with forcing non-local along several foliations. The danger is the
  top-order commutator of ∂^α with the leaf construction on tilted slices. GN-M2 decides it. If it fails, fall back to
  Route S plus statement W.
- **R2 (moderate): M1.** The trade-off between the bend K, which must exceed the sections' ϑ²-slopes, and δ_*, which
  must be small for spacelikeness. Also the compatibility of the bent τ with Tier 1's chart, Σ_init and the corner.
- **R3 (moderate): M3 and M5.** The constants of lem:class-leaf-differences must be uniform on tilted slices and near the
  corner, where the two face sections approach each other (S-T3's GN2).
- **R4 (low to moderate): M6.** The infinite-order vanishing of each family's residual.
- **R5 (structural): grazing families are excluded.** The theorem must say so, and chapter 83's loss sentence must keep
  them, together with large data and low regularity. Statement W is what can be added.
- **R6 (literature).**
  - Tadmon and Dossa–Patenou: Tadmon was read at the pages cited, Dossa–Patenou in abstract only.
  - Moschidis and the numerical-relativity papers were read in abstract only.
  - Guo–Kim–Tonon–Trescases is an analogy, not a source for any step.
  - Athanasiou–Mondal–Yau and Shen–Song–Wan are preprints.
  - No outside result is used in any step of Route S, Route M or statement W.
