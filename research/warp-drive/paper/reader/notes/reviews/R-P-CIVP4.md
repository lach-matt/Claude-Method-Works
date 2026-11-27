# R-P-CIVP4: independent line-by-line reading of proofs/P-CIVP4.md (Tier 4)

File read: `research/warp-drive/paper/reader/proofs/P-CIVP4.md`, md5 436d17be962a9c34358832bfce3c00b9, 1155 lines
(`wc -l`; the brief's 1154 counts without the final newline). Every line was read. Also read: STYLE.md,
READER-BRIEF.md, the writer's report, notes/reports/S-T4.md and GN-T4.md (the parts on K-ax, the jets and the
continuation), chapter 81 lines 540–870 and 1139–1625 (thm:class-kato, rem:class-kato-local, sec:class-planar-shear,
lem:class-leaf-differences, thm:class-stability), the merged Tier 1 and Tier 2 sections of chapter 83 (and
proofs/P-CIVP.md, P-CIVP2.md), all of proofs/P-CIVP3.md (the statements, def:loc-axis-data, lem:loc-axis-constraints,
lem:loc-axis-jets, lem:loc-axis-dependence, the remarks and the placement), Appendix A's entries
thm:std-ly-extension and thm:std-sy-extension, prop:two-dust-background. Nothing under method/, drive/, extracted/ or
recovered/ was read; no repository file was edited.

**The base moved while I read.** When I started, HEAD was 78843c34 and Tiers 1–2 were proof files in a fix round. HEAD
is now 5de1a56b: Tiers 1–2 are CONFIRMED and merged into chapters 01, 03, 83, 90, 95 and 98 (Tier 1's Block B is
byte-identical to proofs/P-CIVP.md's), chapter 81 is unchanged, and P-CIVP4.md is unchanged. My scratch merge
(scratchpad/reader/scratch/rpcivp4/, scripts in scratchpad/reader/scratch/rpcivp4-tools/) is HEAD 5de1a56b plus this
file. I also built HEAD 78843c34 plus Tiers 1–2 as their placements state (Tier 1's items 3–7 being the merged texts
that replace Tier 2's items 2, 3, 5, 6 and the second pair of 4): the result for this file's placement is the same.

## Verdict: NOT CONFIRMED

**5 Major, 13 minor, 16 nits.** The Major findings are four missing steps in Block B (the first transverse derivative
of the shift along N_i; the time chart of the uniqueness proof; the ball argument of its case (ii); the gluing in the
continuation criterion) and one against chapter 81 that Tier 4 inherits (the zero-order bound in the proof of
lem:class-leaf-differences). Each has a short repair, written out below; none changes a statement of the theorem.
Everything else in the mathematics checked out, including the hand computation of the principal parts (confirmed by
my own computer algebra), K-ax (o) and (b′) up to minor 1–2, the corner proof Steps 0–7 and the continuation along the
generators.

---------------------------------------------------------------------------------------------------------------------

## Major findings

### Major 1 — the shift's first derivative across N_i is never determined (lem:civp-axes-jets, lines 305–375; prop:civp-axes-formal (d), lines 469–472)

On N_i the lemma works in the form with u and v exchanged (lines 305–310), whose zeroth jet is J̃_0 = (Ω̃, b̃, γ̃) at
v = 0. But b̃ at v = 0 is not a datum of N_i. With ψ the flow in u of b(·, v, ·) and b = 0 on N_i, ψ = id at v = 0 and
∂_u ∂_v ψ = Db ∂_v ψ + ∂_v b = ∂_v b there, so

    b̃|_(v=0) = −Dψ⁻¹ ∂_v ψ|_(v=0) = −∫_0^u ∂_v b(u′, 0, ·) du′,

which is the first derivative of b across N_i. The hierarchy on N_i (𝔏̃_k J̃_k = −𝔖̃_k for k ≥ 1, lines 321–326 and
353–355) takes J̃_0 as given; its second row determines ∂_v^k b̃ for k ≥ 1 only. So ∂_v b on N_i is fixed by nothing in
the lemma. The exchanged evolution components ℰ̃ are, in the original frame, (E(L̲, ∂_v), E(∂_v, ·), E(·, ·)). They do not
contain E(L̲, ·), the transport equation for ∂_v b along N_i (Tier 1's lem:loc-cone-in, last sentence). Consequences:

- the uniqueness of the b_k in the statement (line 313) fails: every choice of ∂_v b on N_i with the right derivatives
  at the corner gives a hierarchy with ℰ̃ = 0 to infinite order;
- so does (iv);
- the Bianchi argument cited in prop:civp-axes-formal (d) (that of prop:loc-cone-formal (c)) assumes that E′, which
  contains E(L̲, ∂_ϑ), vanishes to infinite order on N_i, and that is not established. Its exchanged form on N_i needs
  E(L̲, ·) = 0 on N_i as a constraint, and the data do not supply it;
- (ii), which identifies the a_j and b_k off the axes with Tier 1's, inherits this.

Repair (three texts).

(1) lem:civp-axes-jets, lines 318–319. Current: "… the corresponding components with u and v exchanged on N_i, and the
conservation laws vanish to infinite order on N. Moreover:". Replacement:

```
[[lem:civp-axes-principal]] on N_o, the corresponding components with u and v exchanged on N_i, and the conservation laws
vanish to infinite order on N, and E(L̲, ·) vanishes on N_i. Moreover:
```

(2) Its proof, lines 353–355. Current: the paragraph "*On N_i* the same, … ψ commuting with G." Replacement:

```
*On N_i* the same, in the form with u and v exchanged given before the lemma, with the generators of N_i, the integral
curves of ∂_u (b = 0 there), and the initial values at u = 0 the v-derivatives of the data of N_o at the corner, after
one step that has no analogue on N_o. In that form the shift b̃ at v = 0 is not a datum of N_i: there ψ = id and
∂_u∂_vψ = ∂_v b, so b̃ = −∫_0^u ∂_v b du′ at v = 0, the first derivative of b across N_i. It is fixed by E(L̲, ·) = 0 on
N_i, which in that form is the constraint E(∂_u, X) = 0 of the edge: as for Ric(∂_v, X) = 0 on N_o (the paragraph
after [[def:civp-axes-data]]), a linear first-order equation for ∂_u b̃ along the generators, with coefficients built
from Ω and γ on N_i, which we solve with b̃ = 0 and ∂_u b̃ = −∂_v b at the corner, the latter a derivative along N_o of
the data of N_o. The induction for k ≥ 1 then runs with this b̃ in the zeroth jet. The change of form is smooth through
the axes, ψ commuting with G, and the v-derivatives of (Ω, b, γ) and of (Ω̃, b̃, γ̃) at v = 0 determine one another,
those of order k of the first through those of order at most k of Ω̃, γ̃ and k − 1 of b̃ and their derivatives along
N_i, so the bounds of (iii) pass from one to the other with the loss counted there.
```

(3) prop:civp-axes-formal (d), lines 469–472. Current: "The other components of E vanish to infinite order on N by
the proof of [[prop:loc-cone-formal]] (c), … E being a smooth tensor field. ∎". Replacement:

```
the conservation laws vanish to infinite order on N by [[lem:civp-axes-jets]]. The other components of E vanish to
infinite order on N by the proof of [[prop:loc-cone-formal]] (c), which uses the contracted Bianchi identity in the form
[[eq:loc-cone-bianchi]] and the constraints and is local in ϑ: on N_o as written there, with the constraints
Ric(∂_v, ∂_v) = q_in and Ric(∂_v, X) = 0 of the data and E(L̲, L̲) = 0 on N_i; on N_i in the form with u and v
exchanged, the evolution components being those of [[lem:civp-axes-jets]] on N_i and the constraints E(L̲, L̲) = 0 of
the data and E(L̲, ·) = 0 of that lemma, with E(∂_v, ∂_v) = 0 on N_o. It applies off the axes, and at the axes by
continuity, E being a smooth tensor field. ∎
```

### Major 2 — the time chart of the uniqueness proof need not be timelike (prop:civp-axes-unique, Steps 3–4, lines 698–736)

Step 3 uses y := e^(v−u) ω and checks only that dt is timelike. The first-order form in which [[thm:class-kato]] (a)
solves the wave-map system, and in which Step 4's energy is taken, has A^0 = diag(1, −g^(tt), g^(ab), P^t). Its block
g^(ab) on the dy^a, which annihilate ∂_t, is positive definite only when ∂_t is timelike (the argument of the paragraph
on the reference metric in case (II)). Here ∂_t = ½(∂_u + ∂_v) at fixed y, and g(∂_t, ∂_t) = ¼(γ(b, b) − 4Ω²). Step 1
makes b = 0 on N_i only; on N_o and inside, b is of any size. So A^0 can fail to be positive, and neither the Cauchy
problem of Step 3 nor the energy of Step 4 is justified. (The corner proof proves the corresponding property, for ∂_τ
and Ĝ, in its Step 1; Tier 3's lem:loc-axis-dependence chooses a factor μ for this reason.) Repair, line 698–700:

Current: "*Step 3 (A wave map near D_(t*)).* Use the coordinates (t, y), y := e^(v−u) ω, ω ∈ S³ ⊂ ℝ⁴, a G-equivariant
chart on which metrics in natural double-null form are smooth through the axes, with dt timelike for every such metric,
as g⁻¹(dt, dt) = 2 g^(uv) < 0." Replacement:

```
*Step 3 (A wave map near D_(t*)).* Fix μ ≥ 1 with 4μΩ² > γ(b, b) on [0, a + 2ε] × [0, b + 2ε] for both solutions, and
use the coordinates (t, y), y := e^(v−μu) ω, ω ∈ S³ ⊂ ℝ⁴, a G-equivariant chart on which metrics in natural double-null
form are smooth through the axes. Its slices are the sets {u + v = t}; dt is timelike for every such metric, as
g⁻¹(dt, dt) = 2 g^(uv) < 0; and ∂_t, a positive multiple of ∂_u + μ∂_v, is timelike for both solutions, as
g(∂_u + μ∂_v, ∂_u + μ∂_v) = γ(b, b) − 4μΩ² < 0, so that the first-order forms below have A^0 positive definite, as in
the paragraph on the reference metric in case (II) of [[sec:loc-cone-reduced]].
```

The extension g_e and g′_e keep this property on a neighbourhood, after decreasing ε_1. The level sets of u in a slice
are still the spheres {|y| = e^(t−(1+μ)u)}, so Step 4's description of D_t is unchanged.

### Major 3 — case (ii) of the non-local term: Ũ is not in the ball about U (prop:civp-axes-unique, Step 4, lines 738–752)

Lines 749–750 assert that, for t near t*, "both Ũ and Ŭ lie in the ball 𝔅′ of [[lem:class-leaf-differences]] (b) about
… ů := U". The proof gives only ‖Ũ − U‖_(H^(k−1)(D_t)) → 0.

- The ball 𝔅′ is a ball of states on the fixed sets 𝒰_(2δ) about the axis points.
- About an axis point of D_t near a future face, 𝒰_(2δ) reaches past that face, outside R′.
- There Ũ is G̃ (on R_ε) or not defined at all, and Ũ − U need not be small: the two solutions are known to agree only
  on R′ ∩ {t ≤ t*}, not on R_ε ∖ R′.

So Ũ ∉ 𝔅′ in general, and lem:class-leaf-differences (b) cannot be applied to (Ũ, Ŭ). The trick of Step 5 of the
corner proof does not transfer: there the extended state was the global solution, here the global state is U.

Repair: localise Ũ by a cut-off, as Tier 3's lem:loc-axis-dependence does, and use (b′), which needs only the leaves of
the first state to stay in D_t. This covers case (i) as well. Replace lines 738–752, from "*The non-local term.*" to
the display, by:

```
*The non-local term.* D_t is bounded by at most two double-null spheres of g, each on N or on a future face; each is a
level set of u or of v within Σ_t, hence a leaf of U of both families, and the leaves of U foliate a neighbourhood of
each axis point, so D_t is closed under the leaves of U. Ũ − U is smooth and vanishes with all its derivatives on R′ ∩
{t ≤ t*}, so for every ϵ′ > 0 there is θ_1 ∈ (0, θ] such that its derivatives of order at most k are at most ϵ′ on the
set 𝒩 of the points whose coordinates (u, v) lie within θ_1 of R′ ∩ {t ≤ t*}. Let χ_𝒩 be a G-invariant cut-off in
(u, v), equal to 1 within θ_1/2 of R′ ∩ {t ≤ t*} and supported in 𝒩, and W := U + χ_𝒩(Ũ − U), a state on the slices
near R′ which for ϵ′ small has the bounds 𝔐 of [[lem:class-leaf-reference]] (b′) of U. R′ is star-shaped about (0, 0),
so for t* ≤ t ≤ t* + θ_1/8 the set D_t lies within θ_1/4 of R′ ∩ {t ≤ t*}. Let x ∈ D_t lie near an axis. The leaf of U
through x lies in D_t; the leaf of W through x is C¹-close to it, so it lies where W = Ũ, and by the uniqueness in
[[lem:class-volterra]] it is the leaf of Ũ; so σ_A[W] = σ_A[Ũ] on D_t. [[lem:class-leaf-reference]] (b′) with
(U, U′) := (U, W) and D := D_t gives

    ‖σ_A[Ũ] − σ_A[U]‖_(L²(D_t∩𝒰_δ)) ≤ C ‖W − U‖_(L²(D_t∩𝒰_(2δ))) ≤ C ‖z‖_(L²(D_t)),

C depending only on the bounds of U, and not on the width of D_t.
```

and in the next paragraph (line 754) replace "In both cases e(s)" by "So e(s)", with θ′ ∈ (0, θ_1/8]. Here δ and
χ_ax must be fixed for U in the t-slicing (minor 13).

### Major 4 — the continuation criterion glues beyond R_(a,b) without justification (prop:civp-axes-criterion, lines 870–880)

The corner solution lives on the square [a − η, a − η + σ″]² with σ″ ≥ 2η, which reaches past u = a and v = b.

- Its edge data equal the maximal development's only on [a − η, a] × {b − η} and {a − η} × [b − η, b]. Beyond, they
  are the extensions of lem:civp-axes-extension (b), (c).
- Wherever D_max contains points with u > a or v > b, it does when a < λ_u or b < λ_v, being relatively open, the two
  solutions need not agree. prop:civp-axes-unique applies only on [a − η, a] × [b − η, b], where the data coincide.
- The union of the domains is not a past set either. The past of a point (u, v) of the square with v > b contains
  {u′ ≤ a − η, b < v′ ≤ v}, which is not known to lie in D_max.

So "the union of their domains is a relatively open past set carrying a class solution" (lines 878–879) is unproved,
and with it (a, b) ∈ D_max with a relative neighbourhood. Repair: take the edges a little past a and b inside D_max,
where its data exist and, by continuity, obey the same bounds. Replacement for lines 870–880:

```
*Proof.* Let K_1 bound the derivatives named, m := 6k + 19, L := 2C K_1, and let ℓ″, Λ″, κ″ be the numbers below and
σ″ := σ(k, Λ″, κ″, ℓ″); put η := min(a, b, σ″/2, 1/(4(1 + L))). The sets [0, a] × [0, b − η] and [0, a − η] × [0, b]
are compact subsets of D_max, which is a relatively open past set; so there is ε ∈ (0, η] such that [0, a + ε] ×
[0, b − η/2] and [0, a − η/2] × [0, b + ε], intersected with Q, lie in D_max, and, by continuity, the derivatives named
are at most 2K_1 and γ ≥ (κ/2)γ̊ there. The edges {a − η} × [b − η, b + ε] and [a − η, a + ε] × {b − η}, each cut at the
edge of Q, lie in D_max, and the maximal development induces cone data on them. Normalise b on the second by
[[lem:civp-axes-extension]] (d), and extend both by its parts (b) and (c), at the order m + 3, with L and the corner
derivatives bounded by C K_1, which is possible as their lengths are at most 2η ≤ 1/(2(1 + L)): this gives cone data on
edges of length at least ℓ″ > 0, of size at most Λ″ in C^m and κ″-nondegenerate, ℓ″, Λ″, κ″ depending only on k, K_1
and κ, equal to the induced data on the given edges. [[prop:civp-axes-corner]] gives a class solution in the gauge on
[a − η, a − η + σ″] × [b − η, b − η + σ″] × S³. By [[prop:civp-axes-unique]], with the corner (a − η, b − η) and the
edges just named, it agrees with the maximal development on D_max ∩ ([a − η, a + ε] × [b − η, b + ε]), a past set
relative to that corner. Put 𝒬 := ([a − η, a + ε) × [b − η, b + ε)) ∩ Q, which lies in the square as σ″ ≥ 2η. Then
D_max ∪ 𝒬 is a past set: for (u, v) ∈ 𝒬, [0, u] × [0, b − η] ⊂ [0, a + ε] × [0, b − η/2], [0, a − η] × [0, v] ⊂
[0, a − η/2] × [0, b + ε], and [a − η, u] × [b − η, v] ⊂ 𝒬. It is relatively open in Q and carries a class solution in
the gauge that induces the data, so it lies in D_max; and it contains (a, b). D_max is relatively open, so it contains
a relative neighbourhood of the compact R_(a,b). ∎
```

(The order of derivatives 6k + 26 in the hypothesis still suffices: (b) at the order m + 3 after the change of angle
uses derivatives of order m + 5 = 6k + 24.)

### Major 5 — against chapter 81, inherited: the proof of lem:class-leaf-differences lacks its zero-order bound (81:1340–1353)

The writer calls this proof sketch-level, and I agree: as written it is incomplete. Block A's (a), (b) are "the proof
of lem:class-leaf-differences with the following changes" (lines 85–102). Tier 4 uses them in three places: the
forcing (F1), (F2) of the corner proof (Step 3), its smoothness (Step 4), and the uniqueness proof.

- (a): [[lem:class-interior-regularity]] bounds ‖δh‖_(H^(k+2)(𝔻_δ)) by ‖f‖_(H^k(𝔻_(2δ))) plus ‖δh‖_(L²(𝔻_(2δ))).
  Nothing in the proof bounds the second term. The leaves have no boundary condition on the disc. The term is fixed by
  δh(0) = 0 and the radial form, through the Volterra estimate, which the proof never mentions. The same gap affects
  the shift δc, which needs |δc| ≤ C|δh|.
- (a) and (b): the passage from the estimates along each disc to the L²(𝒰_δ) norms in three variables (integration
  over the axis points with the Jacobian of (c, y) ↦ (z, y)) is not written.
- (b) has the same zero-order gap. It is in fact proved, completely and more simply, by Block A's (b′) with D the whole
  slice.

Repair (a placement item of this file, chapter 81).

Old (81:1343–1344):

```
coefficients. [[lem:class-interior-regularity]] with j = k, the quadratic terms absorbed on 𝔅, bounds δh in
H^(k+2) along the disc. Derivatives transverse to the disc commute with L_ů up to operators of lower order with smooth
```

New (the rest of the paragraph rewrapped):

```
coefficients. [[lem:class-interior-regularity]] with j = k, the quadratic terms absorbed on 𝔅, bounds δh in
H^(k+2) along the disc. The term ‖δh‖_(L²(𝔻_(2δ))) on the right of that lemma is bounded by the radial form: the two
leaves have the same axis point, so δh(0) = 0, and subtracting the two equations [[eq:class-leaf-volterra]] gives the
bound |δh(r)| ≤ C r ‖F‖_(L²(r dr; [0,2δ])), F the difference of H_L and of the 1-jets of γ3 along the leaf of U, as in
the step *One leaf* of the proof of [[lem:class-leaf-reference]] (b′); the same bound controls the shift δc below. The
bounds along the leaves are integrated over their axis points, as in the step *All leaves* there. Derivatives
transverse to the disc commute with L_ů up to operators of lower order with smooth
```

Old (81:1348–1353, from "(b) The same with" to the end mark). New:

```
(b) This is [[lem:class-leaf-reference]] (b′) with D := Σ_τ: on 𝔅′ the C³ norms of g and the C¹ norms of p_A and Θ_A
are bounded by the Sobolev inequality of [[lem:sobolev]] at the order k − 4 ≥ 2, and |p_A^Σ|, |p_A(∂_z)| and the lower
bounds for A3, B3 and det₂ are those of ů up to a factor 2. The bound needs the first derivatives of g among the
components of U. ∎
```

The forward reference is within one section. (b′) uses no part of lem:class-leaf-differences, so there is no
circularity.

---------------------------------------------------------------------------------------------------------------------

## minor findings

### minor 1 — the operator T_1 of the Volterra/Hardy estimate has the wrong weight (lines 120, 125, 129)

|θ_1 δh| ≤ C_4 ρ |δh(ρ)| ≤ C_4 ρ ∫_0^ρ t ω dt, so after division by r² the operator is r⁻² ∫_0^r ρ ∫_0^ρ t ω dt dρ, with
ρ to the power one, not ρ². With ρ² ≤ ρ the written inequality claims more than the subtraction gives. The correct
operator gives |T_1ω(r)| ≤ (r/(3√2))‖ω‖ and ‖T_1ω‖ ≤ (R²/(6√2))‖ω‖ ≤ R²‖ω‖. The conclusion ‖ω‖ ≤ 2‖F‖ stands, with R²
in place of R³ in the smallness. Replacements:

- line 120: "T_1 ω(r) := r⁻² ∫_0^r ρ² ∫_0^ρ t ω dt dρ," → "T_1 ω(r) := r⁻² ∫_0^r ρ ∫_0^ρ t ω dt dρ,"
- line 125: "inequality, so |T_1 ω(r)| ≤ (r²/(3√2)) ‖ω‖ and ‖T_1 ω‖ ≤ R³ ‖ω‖. With C_4 (R/2 + R³) ≤ 1/2," → "inequality,
  so |T_1 ω(r)| ≤ (r/(3√2)) ‖ω‖ and ‖T_1 ω‖ ≤ R² ‖ω‖. With C_4 (R/2 + R²) ≤ 1/2,"
- line 129: "C_4 (R_0/2 + R_0³) ≤ 1/2" → "C_4 (R_0/2 + R_0²) ≤ 1/2".

### minor 2 — the reason given for |∂_z G| ≤ C_3 (r + |q|³) is wrong (lines 105–107)

"∂_r ∂_z G is bounded by the C³ norms of g and the C¹ norms of p_A, Θ_A" is false. ∂_r∂_z G contains r ∂_r∂_z(H/a_L),
and H holds Θ_A and p_A, so this needs their second derivatives. The bound itself holds, by splitting off the term in H.
Replace lines 105–107 by:

```
both, depending only on 𝔐 and c. In addition |∂_z G(r, z, q)| ≤ C_3 (r + |q|³) for |q| ≤ δ_p, for G built from either
state: ∂_z G = r ∂_z(H/a_L) − ∂_z E_L, where ∂_z(H/a_L) is bounded by the C² norms of g and the C¹ norms of p_A, Θ_A;
E_L(0, z, q) = A3 q³/B3 by the proof of [[lem:class-volterra]], so ∂_z E_L(0, z, q) = ∂_z(A3/B3) q³; and ∂_r∂_z E_L,
which holds derivatives of the metric of order at most three, is bounded by its C³ norms. Along a leaf |q| = |h′| ≤
C_0 r, so there |∂_z G| ≤ C_4 r
```

(This is where the C³ bound of g in (b′) is needed, as the writer says; for E_L the same fact gives the bound of F at
line 117–118, which I checked: E_L is a smooth function of (r, q) and the 1-jet of γ3 at the point, equal to A3q³/B3 at
r = 0 for every jet.)

### minor 3 — placement items 4, 6 and 7 do not apply; item 5 is not given as lines (lines 1037–1080)

Their old texts are Tier 2's item texts. At HEAD those sites carry Tier 1's merged texts (Tier 1's placement items 3, 4,
6, 7, which replace Tier 2's), so items 4, 6 and 7 have no occurrence at all (count 0 at 5de1a56b, and at 78843c34 with
Tiers 1–2 placed). Item 5 inserts a sentence mid-line and gives no Old/New lines. Rebased on HEAD, all four apply
exactly once (checked in the scratch merge; every line ≤ 121, assembled too):

Item 4, ch:localised-data. Old:

```
([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. No development is
asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
that are not smooth, and no other result of this paper uses these developments.
```

New:

```
([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. Cone data of any size
that reach the axes, with or without dust, have a development in the gauge on a neighbourhood of the two cones, unique
in the gauge, and a maximal development with a continuation criterion, provided the cones do not focus
([[thm:civp-axes]], [[cor:civp-axes-cones]]); the neighbourhood is not explicit, and a development of the whole
rectangle is not asserted ([[rem:civp-axes-scope]]). No development is asserted for data of finite regularity or for
densities that are not smooth, and no other result of this paper uses these developments.
```

Item 5, ch:localised-data, opening paragraph. Old:

```
background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). On Σ_τ0 the
constraints split, after Rácz
```

New:

```
background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). Data of any size that
reach the axes have a development on a neighbourhood of the two cones, unique in the gauge, and a maximal development,
provided the cones do not focus ([[thm:civp-axes]]). On Σ_τ0 the constraints split, after Rácz
```

Item 6, ch:scope. Old:

```
estimate ([[thm:loc-cone-development]]). Developments of cone data that differ from the background's near an axis are
not established ([[rem:loc-cone-scope]]).
```

New:

```
estimate ([[thm:loc-cone-development]]). For data of any size that reach the axes, a development on a neighbourhood of
the two cones, unique in the gauge, and a maximal development with a continuation criterion exist when the cones do not
focus; that neighbourhood is not explicit, and a development of the whole rectangle is not asserted
([[thm:civp-axes]], [[rem:civp-axes-scope]]).
```

Item 7, ch:theorems. Old:

```
  estimate ([[thm:loc-cone-development]]); and exactly localised vacuum data
```

New:

```
  estimate ([[thm:loc-cone-development]]); for such data of any size and reaching the axes, a development near the
  two cones, unique in the gauge, with a maximal development and a continuation criterion ([[thm:civp-axes]]); and
  exactly localised vacuum data
```

Tier 3 is placed before this section, and its items 2, 3, 9, 10 replace these same four sites again (its old texts are
Tier 1's new texts). Once Tier 3 is rebased and placed, items 4–7 must be rebased once more on Tier 3's new texts. I
built that variant too (scratch rpcivp4b): the four sentences fit after Tier 3's last sentences in the same way.
Tier 3's item 3 ends "…not near the background's at an axis, for data of finite regularity or for densities that are
not smooth ([[rem:loc-axis-scope]]), and no other result of this paper uses these developments."; Tier 4's sentence
replaces its first clause. The preamble's line 999–1000 ("where that section, Tier 1 or Tier 2 changes a text listed
below, the coordinator merges the new texts") should name Tier 3's items 2, 3, 9, 10 explicitly. The line numbers in
items 3 and 6 (602, 694–695, 720–721, 744) are stale (sec:loc-kid is at 83:2391 at HEAD).

### minor 4 — two remarks of Tier 1 and Tier 2 become false and are not amended

- rem:loc-cone-local-scope (83:1629–1631 at HEAD) ends "A statement with no background, the data being prescribed up
  to the axes, needs a local theory of the augmented system at the axes, with a domain of dependence for null
  boundaries there, and is not given in this paper." prop:civp-axes-corner is that statement. Tier 3's item 6 rewrites
  the sentence and keeps "is not given in this paper".
- rem:civp-large-domain (83:2370–2372) ends "cone data that differ from the background's at the axes are not treated".

New placement items (against HEAD; against Tier 3's item 6 text once that is placed):

Old:

```
terms of the C^(m_1 + 1) norms of the old ones. A statement with no background, the data being prescribed up to the axes,
needs a local theory of the augmented system at the axes, with a domain of dependence for null boundaries there, and is
not given in this paper.
```

New:

```
terms of the C^(m_1 + 1) norms of the old ones. A statement with no background, the data being prescribed up to the axes,
is [[prop:civp-axes-corner]]: it carries out the reduction about the formal solution, with the closure of the
Raychaudhuri equation at the axes in place of the angular cut-off, and its σ depends only on norms of the data near the
corner sphere.
```

Old:

```
are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
or measure-valued.
```

New:

```
are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated here, nor are data of finite regularity or densities that are only
bounded or measure-valued; [[thm:civp-axes]] develops data of any size that reach the axes near the two cones.
```

(The second is the sentence to which Tier 3's item 7 appends its own; one rewrapped paragraph should carry both.)

### minor 5 — placement item 2 does not make H_L[U] a function of the state; Tier 3's item 8 does (lines 1009–1023)

Step (1) of lem:class-planar-shear holds n(u) and the sign of ∂_z u as well as TΣ_L. Item 2 replaces only TΣ_L, so for a
state whose p_A is not closed, n(u) and the sign stay undefined. Block A needs H_L[U] for every state (its definition,
line 9, and (b′)). Tier 3's item 8 replaces the same three lines with all four readings (p_A^Σ for ∇_Σ u, p_A(n) for
n(u), the sign of p_A(∂_z), the γ3-orthogonal complement of p_A^Σ for TΣ_L). Replacement: drop item 2. Keep Tier 3's
item 8 as the one copy, and change line 9 to "Its function H_L[U] is that of [[lem:class-leaf-differences]] (with p_A(n)
in place of n(u) and the sign of p_A(∂_z))" until Tier 3 is placed. Line 1011 should say which copy is kept.

### minor 6 — "chapter 81" in the text of the paper (lines 169, 486, 726)

Source file numbers are not chapter numbers. Chapter 81 assembles as Chapter 51, and the paper has 58 chapters. Each
"chapter 81's closure" must be "the closure of [[ch:class-system]]". Replacements (wrapped, ≤ 121 characters):

- lines 169–170: "whole of each cone. Second, near a corner sphere, Rendall's reduction is carried out with the closure of
  [[ch:class-system]] at the axes, about the formal solution Û rather than about a background, for a short time; this
  needs the planar" (rewrap to the end of the paragraph);
- line 486: "with the closure of [[ch:class-system]] at the axes in place of the angular cut-off, and with
  [[thm:class-kato]] (a) about Û" (rewrap to line 487);
- line 726: "augmented system relative to g with ζ_A := 1 and the closure of [[ch:class-system]] at the axes, in the
  slicing by t: the closure" (rewrap to line 729).

### minor 7 — "class solution in the gauge" is given a second meaning in the same chapter (line 226 and passim)

Line 226 defines a class solution in the gauge "as in [[sec:civp-large]]" as any smooth class solution in natural
double-null form. The chapter already defines the term (sec:loc-cone-setting, 83:741–744, used by sec:civp-large),
with the condition that the functions equal the background's near the axes. The text needs the broader sense
throughout, so "as in [[sec:civp-large]]" is not true, and one term would carry two meanings in one chapter. HEAD's
P-SHELL introduces "class solution in double-null form" for exactly this broader sense. Replace lines 226–228 by

```
A *class solution in double-null form* on D × S³, for a set D of the (u, v)-plane, is a smooth class solution (g, v, u,
q_in, q_out) of [[eq:class-system]] with N_f = 2, v the phase of the density q_in and u that of q_out, whose metric is
in natural double-null form: a class solution in the gauge of [[sec:loc-cone-setting]] without the condition that it
equal the background near the axes. It *induces* cone data on edges contained in D if its functions Ω, b, γ and
```

and read "class solution in double-null form" for "class solution in the gauge" in every later occurrence in Block B
(21 occurrences from line 230 to line 969, two of them broken across lines; rewrap). If P-SHELL's definition is
placed first, this sentence reduces to a reference to it. Lines 190–192 then say "the metric of a class solution in the gauge of [[sec:loc-cone-setting]] is in this form",
which is what they show.

### minor 8 — a renamed parameter of Tier 1 (line 459)

"ε_0 := δ_e" names the cut-off scale of lem:loc-cone-borel by its old name. At HEAD it is ε_B (83:944). Replace by
"ε_B := δ_e".

### minor 9 — smallness of ρ imposed after T* is fixed (corner Steps 5–7, lines 607, 636, 653–660)

Line 659 says "The smallness of ρ is imposed in Step 3, before T* is fixed in Step 4". But Steps 5, 6 and 7 impose
further conditions:

- Ŭ ∈ 𝔅′, "(1 + C)ρ … for ρ small", line 607–608;
- the bound 𝔐 of (b′) for U and U′, line 636;
- C ρ ≤ 1/4 and C ρ ≤ 1/8, lines 654 and 657.

Step 3 does not list them. Their constants do not depend on T* (the annuli and the transport are uniform for
τ ∈ [τ_c − 1/2, τ_c + 1/2]), so no circularity arises, but the text must say so. Add at the end of (iii) of Step 3 (after
"ρ depends only on k, Λ, κ, l."): "We take ρ also so small that the conditions on ρ of Steps 5, 6 and 7 hold; their
constants depend only on k, Λ, κ and l, through bounds that are uniform for τ ∈ [τ_c − 1/2, τ_c + 1/2], and not on
T*."

### minor 10 — prop:civp-axes-formal (c) does not follow from (b) as written (lines 466–468)

(b) bounds |X̂ − X_0| by C_b(|u| + |v|). That is not small at points near N far from the corner, for instance at
(d/2, λ_v). So "with (b) this gives (c)" covers only the square |u|, |v| ≤ d, not the points within d of N. The needed
bound holds, by the same form of the Borel sums. Replace "(c) X_0 equals the data on N, so … of min(1, κ, e^(−Λ))." by

```
(c) Every term of the two sums vanishes at u = 0 and at v = 0: those of f_1 as ã_j(0) = c_(j0) = 0, those of the second
as d_k = 0 for u ≤ 0 and d_0 = 0; and their first derivatives are bounded by the same suprema, without δ_e. So |X̂ −
X_0| ≤ C_b min(|u|, |v|) on 𝒮_e. X_0 equals the data on N, so |X_0 − X| ≤ Λ′ dist(·, N), X the data at the nearest point
of N and Λ′ the bound of the extended a_0 and b_0 in C¹, and Ω ≥ e^(−Λ), γ ≥ κ γ̊ there; this gives (c) for d a small
multiple, depending only on these bounds, of min(1, κ, e^(−Λ)).
```

### minor 11 — lem:civp-axes-jets (iv) is stated for D ⊃ N but used on partial domains (lines 333–335)

The uniqueness proof (Step 1, on R_ε) and the continuation (Step 3, on [0, w] × [0, V − η/2]) apply (iv) to past sets
that do not contain N. The proof of (iv) is local and covers them. Replace "on D × S³, D ⊃ N a past set relative to
(0, 0) containing a neighbourhood of N in it, that induces the data has ∂_u^j (Ω, b, γ) = a_j on N_o and ∂_v^k
(Ω, b, γ) = b_k on N_i" by "on D × S³, D a past set relative to (0, 0) whose interior is dense in it, smooth up to
N ∩ D, that induces the data on N ∩ D has ∂_u^j (Ω, b, γ) = a_j on N_o ∩ D and ∂_v^k (Ω, b, γ) = b_k on N_i ∩ D", as
in Tier 1's lem:loc-cone-jets (iv).

### minor 12 — Corollary P: hypotheses do not match the theorem that supplies it (lines 965–976)

The marker [[pending:tier3-theorem-general]] is supplied by Tier 3's thm:loc-axis (see the marker section). But that
theorem needs:

- a background on Q_0 with margin δ_1, a solution of eq:two-dust-limit on [0, λ_u + 2δ_1] × [0, λ_v + 2δ_1], with σ
  and R smooth across the cones;
- data in the normalised gauge, with nonnegative densities, of size ≤ ε_0 in C^(12k+42), and k ≥ 9.

"Given … on a neighbourhood of a rectangle Q_0 contained in its set G" does not give the margin when Q_0 touches the
boundary of G in Q. Likewise "develop on every rectangle contained in G" (line 971) must be "every rectangle at
positive distance from that boundary". Also "Q_0 := [0, a] × [0, b]" reuses a, the inner radius in the definition of G
in the same sentence. Replace lines 965–976 by

```
**Corollary {#cor:civp-axes-perturbations}** (Small perturbations of a background that is round.) Let k ≥ 9 and let g_0
be a two-dust background of [[prop:two-dust-background]], which is round, with the corner of its two cones at (0, 0).
Let Q_0 := [0, λ_u] × [0, λ_v] lie in its set G at positive distance from the boundary of G in the set Q of that
proposition, and let δ_1 > 0 be so small that g_0, with σ and R extended across the two cones as in the proof of
[[lem:loc-cone-strips]] (b), is a background on Q_0 with margin δ_1 ([[sec:loc-axis]]). Let ε_0 be the number of
[[thm:loc-axis]] for it. Then for cone data through the axes on the edges of Q_0, in the normalised gauge, with
nonnegative densities and of size at most ε_0 in C^(12k+42), D_max = Q_0, and the maximal development of
[[thm:civp-axes]] (c) is the solution of [[thm:loc-axis]] (a). So small non-round perturbations of the cone data of
g_0, reaching the axes, develop on every such rectangle, ε_0 depending on the rectangle, and on every finite union of
such rectangles.

*Proof.* Q_0 is a past set relatively open in itself, so the solution of [[thm:loc-axis]] (a) is a development in the
sense of [[cor:civp-axes-maximal]], and D_max = Q_0; for a finite union of rectangles take the data on the longest
edges and apply [[thm:civp-axes]] (c) to the developments on each rectangle. ∎
```

(If the data are not in the normalised gauge, lem:civp-axes-extension (d) normalises them first; the size bound is then
for the new functions.) Crosswalk row B27's note changes accordingly ("Corollary P, from thm:loc-axis about a general
round background with margin").

### minor 13 — δ and χ_ax are not fixed for the uniqueness proof (line 734)

"χ_ax as in Step 2 of the proof of [[prop:civp-axes-corner]]" refers to a cut-off built from δ, which was chosen there
from the constants of K-ax for Û in the τ-chart. Here the relevant state is U = g in the t-slicing. Replace by "χ_ax
built as in Step 2 of the proof of [[prop:civp-axes-corner]] from a number δ ∈ (0, δ_𝔐] fixed for U in the slicing by
t, δ_𝔐 that of [[lem:class-leaf-reference]] (b′) for the bounds of U and of the states W of the next paragraph on R′ ∩
{t* ≤ t ≤ t* + θ}".

---------------------------------------------------------------------------------------------------------------------

## nits

1. Line 102: "foliate 𝒰_(r_V/8) by (o) for U". (o) is stated for a smooth state and U ∈ 𝔅′ is not smooth. Read "by
   Steps 1–3 of the proof of (o) for U, which use only its C² and C¹ bounds".
2. Line 131: "σ = 2 |p_A^Σ| σ_L − …" holds when p_A(∂_z) > 0; otherwise the first term changes sign. Add "for
   p_A(∂_z) > 0, and with the factor −1 on the first term otherwise". The bounds are unaffected.
3. Line 524: "for τ ≤ τ_c, Σ_τ ∩ 𝒰 ⊂ P". At τ = τ_c the corner sphere lies in F. Read "for τ < τ_c".
4. Line 657: "every point of [0, σ]² is … at distance at most 2σ from N". What the degree argument uses is that every
   point of 𝒯 ∩ Σ_(τ_end) lies within 2σ of N (there min(u, v) ≤ 2σ). Read "and every point of 𝒯 ∩ Σ_(τ_end) lies
   within distance 2σ of N, so moves by at most 2Cρσ".
5. Line 703: "Seek Φ = id + φ with id : (g′_e) → (g_e) a wave map". Read "with Φ : (g′_e) → (g_e) a wave map".
6. Line 563: without the term −(1 − ξ)B_♭Z of case (II), the first and third wave rows give g_τ = ∂_τ g and g_a =
   ∂_a g only where ξ = 1, which is all that is used (on 𝒰_1). Say "on 𝒰_1", or restore −(1 − ξ)B_♭Z in
   [[eq:civp-axes-modified]].
7. Line 547: χ_♭ must be supported in 𝒮′, where ∂_τ is timelike for Ĝ (in case (II) it was supported in 𝒮). Add "and
   χ_♭ supported in 𝒮′".
8. Lines 532–534: δ is fixed with reference to "the support of ξ below". ξ does not depend on δ, so fix ξ first (move
   its definition to Step 2) or say "ξ of Step 3, which does not depend on δ".
9. Line 496: "every point of which lies within δ_1 of N" is false at (−δ_1, −δ_1). It is not needed: |u|, |v| ≤ 3δ_1 ≤
   d suffices. Delete the clause.
10. Lines 465–466: "so b_0 = 0" reads as the whole edge sequence; read "so the shift component of b_0 vanishes". The
    bound |a_0^b(v)| ≤ Λ|v| holds for v ≥ 0; for v < 0 the constant is the C¹ bound of the extension.
11. Notation: κ (nondegeneracy) and the κ of [[eq:loc-cone-region]], used in Step 2 through 𝒰; b, the side of R_(a,b),
    and the shift b in prop:civp-axes-criterion and thm:civp-axes (d); θ, the angle and the time step, in uniqueness
    Step 5. Rename the time step θ ↦ ϑ_1, say, and the rectangle sides (a, b) ↦ (a_R, b_R).
12. Line 194: "the plane of the K2-directions" → "the plane normal to the axis".
13. Line 900: "its part quadratic in b" → "its part nonlinear in b".
14. Line 428: "|∂ ln ỹ| ≤ C(Λ)" needs κ (γ⁻¹ ≤ κ⁻¹γ̊⁻¹): C(Λ, κ). Also γ̂ ≥ Λ⁻²γ̊ follows directly from μ_γ̂ = μ_γ̊ and
    γ̂ ≤ Λγ̊, without decreasing ℓ.
15. Line 855: "In Step 3" → "In Step 3 of the proof of [[prop:civp-axes-faces]]".
16. Crosswalk: the second field elsewhere has the form "paper/reader/proofs/P-CIVP4.md@PENDING:6"; use it. Row B27's
    note: see minor 12. Faces Step 4 (line 827): after the change of angle of Step 3, b on the piece of N_o^+ becomes
    b − b(0, v_η, ·), of C^m norm up to 2Λ_0. Put Λ_c := max(2Λ_0, C, 1) at line 804 (the corner proposition also asks
    Λ ≥ 1).

---------------------------------------------------------------------------------------------------------------------

## The pending markers against Tier 3 (proofs/P-CIVP3.md, md5 1d196fae6ed5c92557721eb8dadfd294)

- **[[pending:tier3-section]]** (lines 159, 999): supplied, as **[[sec:loc-axis]]** ("Developments of cone data through
  the axes"). Nothing is missing. Tier 3's item 1 places it after the Tier 2 section, before sec:loc-kid, as this file
  assumes.
- **[[pending:tier3-theorem]]** (lines 929, 943, 981): supplied, as **[[thm:loc-axis]]** (a). It gives, for cone data
  through the axes (def:loc-axis-data: def:loc-cone-data with fields smooth through the axes, so cone data of
  def:civp-axes-data) in the normalised gauge, with nonnegative densities and small in C^(12k+42), k ≥ 9, a class
  solution in the gauge through the axes on Q1 × S³, whose metric is smooth on Q1 × S³, the axes included. That is a
  class solution of this file's (broader) kind on Q1, a relatively open past set of Q = Q1. So (c) "D_max contains the
  set on which that development is defined, whenever the data satisfy its hypotheses" holds, here with D_max = Q, and
  the proof's "or are those of [[pending:tier3-theorem]]" and rem:civp-axes-scope (i)'s "explicit domains" (the whole
  rectangle) are correct. Nothing is missing from Tier 3; Tier 4 should state the hypotheses as "whenever the data
  satisfy its hypotheses" (as it does).
- **[[pending:tier3-theorem-general]]** (lines 967, 974): supplied by **[[thm:loc-axis]]** (a), which is already written
  for a general background on Q1 with margin δ_1 (a round two-dust metric on [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 + 2δ_1]
  solving eq:two-dust-limit on its part in F), not only for chapter 83's background; ε_0 depends only on k, u_1, v_1,
  δ_1 and the background. What is missing is on Tier 4's side: Corollary P's hypotheses must provide that background
  (Q_0 at positive distance from the boundary of G, σ and R extended across the cones) and the theorem's data
  conditions (normalised gauge, nonnegative densities, k ≥ 9, the size in C^(12k+42)); minor 12 gives the text. With
  that, the corollary is no longer conditional and the marker becomes [[thm:loc-axis]].

Interplay with Tier 3's placement:

- Tier 3's item 8 and this file's item 2 replace the same three lines of lem:class-leaf-differences; keep Tier 3's
  (minor 5).
- Tier 3's items 2, 3, 9, 10 rewrite the four sites of this file's items 4–7 (minor 3).
- Tier 3's item 6 keeps "is not given in this paper" in rem:loc-cone-local-scope (minor 4).
- Tier 3's rem:loc-axis-scope (i) says that "for cone data that are not near the background's at the axes nothing is
  asserted there". That is right for thm:loc-axis. A pointer to [[thm:civp-axes]] for the neighbourhood of the cones
  would help the reader; it is optional.

---------------------------------------------------------------------------------------------------------------------

## Placement, lint and assembly (scratch only)

Scratch: HEAD 5de1a56b (Tiers 1–2 merged) copied to scratchpad/reader/scratch/rpcivp4/; Block A inserted after
rem:class-leaf-numerics, Block B before sec:loc-kid (each anchor found once), item 2 applied (count 1). Items 4, 6, 7:
count 0 (minor 3). With items 4–7 rebased as in minor 3 and the two items of minor 4 added (each count 1):

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4766 label(s) defined, 6 hit(s)", all six Tier 4's own
  pending markers (three tier3-theorem, two tier3-theorem-general, one tier3-section); no other hit.
- `python3 assemble.py --check`: "labels 4766, computations cited 0, problems 0". `python3 assemble.py`: 0 problems; the
  section is Section 53.6, and lem:class-leaf-reference is Lemma 51.30.
- `python3 lint.py --paper`: 12 hits, each a pending marker counted twice (pending, unresolved label); nothing else.
- Line lengths: no line of the file over 121 characters; no assembled line of Block A, Block B or the placed texts over
  121; no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=" or "|". The replacement texts in this review were
  checked the same way.
- Every label in the Placement list is defined once and nowhere else; all 31 crosswalk rows give the right line of
  their label (checked by script); sec:class-axes-stability and sec:loc-kid, the two other headings in the file, are
  existing labels quoted in the placement.
- `python3 lint.py proofs/P-CIVP4.md` alone: besides the pending markers and the cross-file labels, only file names in
  the Placement and Crosswalk sections, which are not merged.

Self-containedness of the merged text: no file or program names, no code, no process language in Blocks A and B. The
only problems are the three "chapter 81" references (minor 6), which lint does not catch.

---------------------------------------------------------------------------------------------------------------------

## What I checked and found correct

- **lem:civp-axes-principal.** I redid it by hand from the formula for Ricci with the inverse metric of lines 257–260.
  I then confirmed it with my own sympy computation of the second-derivative part in a general chart of S³ (scratch
  rpcivp4-cas/principal.py):
  - no ∂_u² in any component of ℰ;
  - E(L̲, ∂_v) has −(2/Ω)∂_u∂_vΩ − ½γ^(CD)∂_u∂_vγ_CD and no ∂_u∂_C;
  - E(L̲, ∂_A) has −(1/(4Ω²))γ_AC ∂_u∂_v b^C + ½γ^(CD)(∂_D∂_uγ_CA − ∂_A∂_uγ_CD) − (1/Ω)∂_u∂_AΩ. The ∂_u∂_vγ-terms
    cancel, and there is no ∂_u∂_C b;
  - E(∂_A, ∂_B) has (1/(2Ω²))∂_u∂_vγ_AB alone.

  So the ∂_v-principal part is block-triangular, with the invertible (ω, h)-block ((−2/Ω, −½tr_γ), (0, (2Ω²)⁻¹ id)) and
  the b-row −(4Ω²)⁻¹γ(∂_v β, ·). Its coefficients are regular at every point, axes included. Affinity in J_j for
  j ≥ 2, and the coefficient structure of 𝔏′, are as stated. For (c) I checked every monomial of eq:loc-cone-frame-ricci
  (at most one factor among the L̲-quantities listed at line 296; no ∂_u b in E(L̲, ∂_v), E(∂_ϑ, ∂_ϑ), E(K_i, K_i); no
  ∂_u ln Ω in the last two). The two continuity arguments are sound: 𝔔(J_1, J_1) is a continuous function vanishing
  off the axes, and invariant β vanishes at the axes with no derivative on S³ in the first and third rows. So no Riccati
  term occurs at any order.
- eq:civp-axes-raychaudhuri, from Raychaudhuri's equation with χ = (ỹ′/ỹ)id + ½γ̂⁻¹∂_vγ̂ and tr(γ̂⁻¹∂_vγ̂) = 0. It agrees
  with Tier 3's lem:loc-axis-constraints (a) and with the paragraph after lem:civp-axes-free-data (ỹ = e^ϕ(sin ϑ cos
  ϑ)^(−1/3), ¼|∂_vγ̂|² = Σ(∂_vℓ_i)²).
- The conservation laws ∂_uρ_in + ℒ_bρ_in = 0 and ∂_vρ_out = 0 (√|g| = 2Ω²√γ, g⁻¹dv = −L̲/(2Ω²), g⁻¹du = −∂_v/(2Ω²)).
- The invariance statements: invariant vector fields vanish at the axes, and the parity of the coordinate functions.
- The N_o half of lem:civp-axes-jets: the reduction to (ω, h) first and then β, with invariance by equivariance of the
  reduced system, and (v).
- **lem:class-leaf-reference (o).** Steps 1–4 line by line:
  - the constants of lem:class-volterra, uniform in z0;
  - the contraction estimate giving sup|Δw| ≤ 4C_1|Δz| and the quotients in [1/2, 3/2];
  - the image of z0 ↦ h_V(r; z0), with C_0r²/2 ≤ r_V/32;
  - the regularity: C^(1,1) at the axis, the removable point;
  - the implicit function theorem in C([0, r_V]) with differential of norm ≤ 3/4.
- **(b′).** The rest is correct after minors 1–2:
  - F with |F| ≤ C|U − U′|, from E_L(0, z, q) = A3q³/B3 for every jet;
  - θ_1, θ_2 ≤ C_4ρ, the intermediate q being bounded by C_0ρ;
  - 𝒜 of norm 1 and T_2 of norm R/2 on L²(r dr);
  - |δh| ≤ √2 r‖F‖;
  - the Lipschitz dependence of σ[U′] on the axis point, C_4(3/2 + 4C_1);
  - the change of variables over axis points with weight 2πρ1, ρ1 ∈ [ρ1(p)/2, 2ρ1(p)] on 𝒰_(2δ);
  - the containment |h − z(p)| ≤ δ + 3C_0δ² ≤ 2δ.

  (a), (b) about V: the five changes are right, the zero-order term −(∂_zH_L[V])δh included. They inherit Major 5.
- **lem:civp-axes-extension.**
  - (a) against Appendix A's thm:std-ly-extension: Σ_j a_j(−b_j)^k = 1 and Σ 2^(δ_k|j|)|a_j|b_j^k < ∞ give A_i < ∞,
    uniform convergence of all derivatives, the matching at s = 0, the w^(−m) bound, linearity and invariance.
  - (b): the Taylor remainder L s^(m+1−i), the bound C_m L a^(m+1−i) after the cut-offs, the C^m norm ≤ C_m(Λ + 1).
  - (c) as an adaptation of lem:loc-cone-extension (nit 14).
  - (d): dθ − b du = Dψ_u(dθ′ − b′du) with b′ = ψ_u^*(b − b(u, 0, ·)); the constraints are unchanged because ∂_v at
    fixed θ′ is ∂_v and ∂_u at fixed θ′ is L̲ on N_i.
- **prop:civp-axes-formal** (a) and (b): the compatibility of a_j − ∂_u^jX_0 and b_k − ∂_v^kX_0 at the corner; m − 4(k +
  3) ≥ 2(k + 3); C_b independent of δ_e from the form of the Borel sums.
- **prop:civp-axes-corner**, Steps 0–7. Checked:
  - Step 1's two estimates of |b̂|²(u + δ_c)/(v + δ_c): 32eC_b²δ_1² + 32C_b²δ_1² and 8eC_b²(δ_c² + 16δ_1²), with
    (u + δ_c)(v + δ_c) ≥ δ_c²e^(−1) on 𝒮′;
  - 4Ĝ(∂_τ, ∂_τ);
  - the face sections |y| = e^τ/δ_c² and δ_c²e^(−τ), and du(∂_r), dv(∂_r);
  - the residual of (Aug3) at Û, −E(P̂_A, P̂_A) by eq:class-raychaudhuri, eq:class-identity and eq:class-x, and so the
    smoothness of F̃;
  - (F1)–(F3), with T* from the proof of thm:class-kato (a): with u_* = 0 and u0 = 0, 𝔐 = 1, C_u and C_A on
    {|Z| ≤ C_S(1 + ρ)}, uniform in τ_init ∈ [τ_c − 1/2, τ_c];
  - σ = δ_c(e^(T*/4) − 1)/2, with [0, 2σ]² ⊂ F ∩ {τ ≤ τ_end};
  - Step 5: the annuli bounded by face sections and far cuts, radii in a compact subinterval of (0, ∞), ratio ≈ 81²
    near τ_c, so Stein's constant is uniform (the writer's point 3);
  - Step 6 with (b′) on the shells, the face sections being leaves of U and U′;
  - Step 7: the inversion to natural double-null form; injectivity on the down-set; the degree argument, with moves
    ≤ 2Cρσ < σ/2 on the top boundary.
- **prop:civp-axes-unique.** The reduction to compact rectangles, the closedness of the set of agreement times, the
  wave-map energy region (conormals du + 2dv and 2du + dv timelike, the null faces), and the vanishing of Φ − id to
  infinite order on D_(t*) are correct. Step 5 is correct. Majors 2 and 3 cover Steps 3–4.
- cor:civp-axes-maximal.
- **prop:civp-axes-faces**, all steps:
  - K′ finite by smoothness on compact edges;
  - the uniform σ_c, independent of η;
  - η ≤ σ_c/4 with v_η + σ_c ≥ V + 3σ_c/4;
  - the gluing on 𝒬 ⊂ [0, ā), where the data of both edges coincide;
  - D_new a past set, and both cases of the contradiction.

  The ingoing edge by symmetry, b on the outgoing piece being solved by (c). It stands once Major 1 repairs the b_k it
  uses on N_i.
- rem:civp-axes-riccati: w = w_0/(1 + w_0v/4), blowing up at v = 4/|w_0| for w_0 < 0.
- lem:civp-axes-free-data and the paragraph after it. thm:civp-axes (a), (b), (e) as consequences. cor:civp-axes-cones.
  rem:civp-axes-scope.
- Every cited result says what is used at the hypotheses used, apart from the findings above:
  - Tier 1: lem:loc-cone-borel, lem:loc-cone-jets, prop:loc-cone-formal, the reference-metric paragraph,
    lem:loc-cone-system, lem:loc-cone-energy, lem:loc-cone-past, lem:loc-cone-constraints, lem:loc-cone-gauge,
    lem:loc-cone-extension;
  - Tier 2: sec:civp-large, thm:civp-large, thm:std-cctw-strips in a remark;
  - chapter 81: thm:class-kato, rem:class-kato-local, lem:class-volterra, lem:class-leaf, lem:class-planar-shear step
    (3), prop:class-augmented, Steps 6, 9, 10 of thm:class-stability;
  - Appendix A: thm:std-ly-extension, thm:std-sy-extension, cor:std-moser-product.

---------------------------------------------------------------------------------------------------------------------

## Confirmation

File read: proofs/P-CIVP4.md after its fix round, md5 0e0ef24b527d9ae78536e0208f86b9b5, 1292 lines; every line
re-read. Also read: the writer's fix-round report (notes/reports/P-CIVP4.md). HEAD is now 0c913792. Its chapters and
crosswalk are identical to 481f86a1's, on which the placement is based (`git diff --stat 481f86a1 HEAD` shows only
proof files).

Scratch merge: `git archive` of HEAD into scratchpad/reader/scratch/rpcivp4c/, script rpcivp4-tools/apply_fix.py.

- Block A follows rem:class-leaf-numerics, and Block B goes before "### Null shells along the leaves
  {#sec:loc-shells}". Each anchor occurs once.
- Items 4–11 each occur once, as whole lines.
- `python3 lint.py --chapters`: "62 file(s), 4864 label(s) defined, 0 hit(s)".
- `python3 assemble.py --check`: "labels 4864, computations cited 0, problems 0".
- `python3 assemble.py` (scratch only): 0 problems. No assembled line is over 121 characters. The section is 53.7 and
  lem:class-leaf-reference is Lemma 51.30.
- `python3 lint.py --paper`: 0 hits.
- In the file: no line before the Crosswalk section is over 121 characters, and no wrapped line has a forbidden start.
  There are 14 proofs and 14 end marks, and no pending marker remains.
- "chapter 81" no longer appears in paper text. "class solution in the gauge" is left only where it names Tier 1's or
  Tier 3's terms (lines 208, 248, 251, 1020).
- All 31 crosswalk rows are tab-separated, have four fields, and give the right line of their label.

### Verdict on the findings: all resolved

**Major 1 (the shift across N_i): resolved.**

- The statement now says that E(L̲, ·) vanishes on N_i.
- (i) records the extra ODE.
- The "On N_i" paragraph fixes b̃ at v = 0 by the exchanged constraint, with b̃ = 0 and ∂_u b̃ = −∂_v b at the
  corner.
- "Vanishing to infinite order" now says why E(L̲, ·) = 0 on N_i.
- prop:civp-axes-formal (d) runs the Bianchi argument on N_i in the exchanged form, with the right constraints. It uses
  E(L̲, L̲) and E(L̲, ·) on N_i and E(∂_v, ∂_v) on N_o.

**Major 2 (the time chart): resolved.**

- The chart is y = e^(v−μu)ω with 4μΩ² > γ(b, b) on R_ε for both solutions; ∂_t is a positive multiple of
  ∂_u + μ∂_v.
- The writer's changes are right:
  - the densities are extended with the metric, which is needed, as U and Ũ carry them;
  - ε_1 ≤ ε is chosen so that the inequality persists on the extension, by continuity from R_ε where g_e = g;
  - g′_e inherits the inequality.
- The set 𝒲 is what Major 3 needs. One small overstatement remains (nit A below).

**Major 3 (the non-local term in uniqueness): resolved.**

- The writer is right that my replacement did not close. There ϵ′ was fixed before the scale θ_1 of the cut-off, so the
  derivatives of χ_𝒩, of size θ_1^(−i), are not compensated.
- The Taylor version works:
  - Ũ − U vanishes to infinite order on the closed set R′ ∩ {t ≤ t*}, so its derivatives of order j ≤ k + 2 are
    ≤ C′ s^(k+2−j) at distance s, along the segment to the nearest point, which stays in 𝒲 as η_2 ≤ ε_1/4;
  - with |∂^i χ_𝒩| ≤ C η_2^(−i) on supp χ_𝒩 ⊂ {s ≤ η_2}, every derivative of order ≤ k of W − U = χ_𝒩(Ũ − U) is
    ≤ C C′ η_2^(k+2−j) ≤ C C′ η_2²;
  - so W has the bounds of (b′), and *One leaf* (sup |F| ≤ C C′ η_2²) with eq:class-leaf-lipschitz puts the leaf of W
    through a point within C″ η_2² of the leaf of U through it.
- With C″ η_2² ≤ η_2/4 and D_t within η_2/8 of R′ ∩ {t ≤ t*} (R′ star-shaped, |(u, v)| ≤ t), the W-leaf lies within
  3η_2/8 < η_2/2, where W = Ũ.
- (b′) with (U, W) on D_t, which is closed under the round U-leaves, then gives the estimate, for t ≤ t* + η_2/8.
- η′ := η_2/8 is consistent. r_*, δ ≤ δ_𝔐 (for 2𝔐_U and c_U/2) and χ_ax are now fixed for U in the t-slicing, which
  closes minor 13.

**Major 4 (the criterion): resolved, and the writer's correction of my parenthesis is right.**

- lem:civp-axes-extension (b) needs Λ ≥ |∇̊^i ∂_s^j f(0)| with i, j ≤ m separately: the C^m norm of the Taylor
  polynomial P holds ∇̊^α ∂_s^l f(0) with |α| ≤ m − j′ and l ≤ m. It also needs L ≥ |∇̊^i ∂_s^(m+1) f| with i ≤ m.
- That is total order 2m + 1 at the order m, hence 2m + 7 at the order m + 3. Part (d) raises it to 2m + 8 =
  12k + 46. My 6k + 26 was too few.
- The new hypotheses of prop:civp-axes-criterion and thm:civp-axes (d), the sentence after the criterion, and faces
  Steps 0 and 3 (K′ over i + j ≤ 2m + 8, K″ over i, j ≤ m + 3, L(η) for ∇̊^i ∂_u^(m+4)) are consistent with each
  other.
- The gluing is right:
  - uniqueness on D_max ∩ 𝒬 ∩ {u < λ_u, v < λ_v}, which is relatively open in the rectangle of the extended edges
    even where those pass the far sides of Q;
  - then continuity;
  - D_max ∪ 𝒬 is a past set, by the three inclusions, and relatively open in Q.

**Major 5 (the zero-order bound of lem:class-leaf-differences): resolved for Tier 4.**

- Block A (a) now adds (vi), the zero-order term ‖δh‖_(L²(𝔻_(2δ))) and the shift z0^U − z0^V, bounded by *One leaf*
  of (b′) with (U, V), using δh(0) = 0.
- It also adds (vii), the integration over axis points, with the Jacobian ∂_(z0) h_V ∈ [1/2, 3/2] and the weight 2πρ1.
- (b) is proved as (b′) with D := Σ_τ.
- The bounds are taken on 𝒰_(r_*). I checked:
  - r_V ≤ r_*/2, and the leaves over [0, r_V] stay in 𝒰_(r_*), since |h_V − z(p)| ≤ 3r_V/2;
  - δ_𝔐 ≤ r_V/8 ≤ r_*/16, with ρ1 ∈ [ρ1(p)/2, 2ρ1(p)] on 𝒰_(2δ) still holding;
  - δ_V := min(r_V/8, δ_𝔐(2𝔐_V, c/2)), and the bounds of (b′) hold for states in 𝔅′ by (v).
- The corner (Step 2: r_*, δ_Û, ξ fixed first) and the uniqueness proof (Step 4: r_* with 𝒰_(r_*) ⊂ 𝒲) choose r_* and
  δ consistently.
- Block A no longer needs any further step of chapter 81's base proof beyond those I accepted in the first reading: the
  elliptic estimate with the quadratic terms absorbed, and the induction on transverse derivatives. So it stands on its
  own until proofs/P-CLD.md lands; (vi) and (vii) can then cite it.

**minor 1–13: all resolved.** Where the writer changed my replacement, I agree:

- minor 3 and 4: rebased on HEAD. Item 4 drops only the false clause and keeps the Tier 3 citation and the null-shell
  exception with its closing clause. Item 6 keeps the sentences of Tier 3 and the null shells. Items 8 and 9 are right
  in context.
- minor 5: item 2 is "no change". The merged Tier 3 clause in lem:class-leaf-differences (p_A^Σ, p_A(n), the sign of
  p_A(∂_z), the γ3-orthogonal complement) is at HEAD, and Block A reads H_L[U] from it.
- minor 7: the term is defined once, at line 246.
  - The new paragraph after eq:civp-axes-form proves the equivalence of the two forms. I checked the step at the axes:
    det g = −4Ω⁴ det γ, so nondegeneracy with γ ≥ 0 and Ω² ≥ 0 as limits gives γ > 0 and Ω² > 0.
  - Item 10 turns the null-shells definition (83:3282–3286) into a reference with the same content. The section's
    later uses (83:3318, 3421, 3988, 4007 at HEAD: "a class solution in double-null form" on cells, with "round", on
    each closed cell) read correctly with it. Tier 4's section precedes sec:loc-shells, so the definition comes before
    every use.
  - Chapter 57's "metrics in double-null form" (sec:tl5-cip-form) is a different, explicitly defined notion in another
    chapter, and does not conflict.
- minor 10: the constant 2Λ′ (for points with u, v < 0 the nearest point is the corner, |u| + |v| ≤ √2 dist) and
  √2 d are right; min(|u|, |v|) ≤ dist(·, N) holds on 𝒮_e.
- minor 12: "Q_0 has a neighbourhood in F contained in G" is the right hypothesis; the writer's point about the side
  v = V1 of Q is correct. Corollary P is now unconditional: it cites thm:loc-axis with k ≥ 9, cone data through the
  axes in the normalised gauge, nonnegative densities, size ≤ ε_0 in C^(12k+42), and a background with margin δ_1. The
  finite-union part is proved correctly: the slightly larger Q_0″, Q_0′ := Q_0″ ∩ Q′, its interior relative to Q′,
  and the least ε_0.
- nit 14: κ′ := κ/(4Λ²) is right (ỹ² ≥ κ/4, γ̂ ≥ Λ⁻² γ̊). Extension (c) on [λ, λ + 1/2] with ℓ ≤ 1/2 matches what (a)
  (to [−w, 1] in v − λ_v) and (b) (to [0, 1]) supply.
- The other minors and nits 1–16 are applied as written: lines 102, 136, 141, 145, 120–124, 148, 185–186, 215, 463–465,
  494, 500–507, 527, 537, 565, 591, 608, 611–613, 703, 754, 779, 864, 887–888, 916, 975, and the crosswalk format.

### Remaining nits (none blocks confirmation)

A. Line 771–773: "the image under Φ of the points … with t ≤ t* + η_1 contains the set 𝒲 of the points of
   {t* ≤ t ≤ t* + η_1} …". Φ moves points by O(η_1²) (φ = ∂φ = 0 at t*), so near the top slice t = t* + η_1 the
   claim is not exact. Only slices with t ≤ t* + η_2/8 ≤ t* + η_1/8 are used, so nothing depends on it.
   - Fix: at line 773 read "{t* ≤ t ≤ t* + η_1/2}", and at line 784 read "t* ≤ t ≤ t* + η_1/2".

B. Lines 1130 and 1158: the new texts of items 4 and 6 end in the short lines "except finitely many null" and "with
   densities smooth", followed by the unchanged chapter lines. This is legal, but ragged. The paragraph can be rewrapped
   at merge.

C. Line 948–950: prop:civp-axes-unique is applied to the corner solution, whose domain is the closed square. Take its
   relatively open part [a_R − η, a_R − η + σ″)² (∩ Q), as cor:civp-axes-maximal does.

D. Lines 3–4 (not merged): "the Placement section below gives the position and one clause added to
   [[lem:class-leaf-differences]]" is stale, since item 2 is now "no change". Read "gives the position".

**Verdict: CONFIRMED.** There is no open Major or minor finding; nits A–D are optional.
