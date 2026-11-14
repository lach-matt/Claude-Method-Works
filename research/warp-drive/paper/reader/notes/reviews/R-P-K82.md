# R-P-K82: independent reading of proofs/P-K82.md (the radial pair in chapter 82)

Read line by line (578 lines, six blocks) against STYLE, the report reports/P-K82.md, R-82 (Major 2), R2-82 (M1),
F2-81, chapter 81 at its current text (mtime 2026-11-13 23:28, after F2-81), chapter 80, chapters 02, 03, 05, 07, 09,
and chapter 82 **as it stands while F3-82 runs** (HEAD 7af68ec plus working-tree edits, 1681 lines, read at
2026-11-14 00:14). P-K82 was written at 23:49 against the 1412-line text; F3-82 has since added
lem:vlasov-local-stability, eq:vlasov-localised, the item (v) *Localisation* of sec:vlasov-n, the new (O4), the
symbol 𝔫 for the unit normal and a new first paragraph. Line numbers below are those of proofs/P-K82.md.

**Verdict: NOT CONFIRMED — 1 Major, 11 minor, 9 nits.** The mathematics of the four pieces is right, and the R-82
Major 2 obstruction is genuinely overcome. The Major is R2-82's M1 entering P-K82 at three places; F3-82's localisation
repairs it once P-K82 routes the labels through lem:vlasov-local-stability and keeps the radial pair unlocalised. The
minors are mostly alignment with the revised chapter 82, plus three gaps of argument (mollifier invariance, the width
of Ω₂′, ι at the outer boundary) and the wording of the narrowing in the corollary.

## Re-derivations (private, sympy 1.x and mpmath at 40 digits)

- Template eq:vlasov-template: in the frame (e_ϑ, e1, e2), the entries λ_ϑ, λ_1, λ_2 equal the t-forms with t = π/2 −
  πζ/3 (difference 0 symbolically); λ_ϑ + λ_1 + λ_2 = 0 and λ_ϑ² + λ_1² + λ_2² = 2 symbolically; at ζ = 1 and ζ = −1 the
  entries are (−1, 2, −1)/√3 and (−1, −1, 2)/√3. On 30 random points of R⁴: 𝒯x = 0, Euclidean trace 0, |𝒯|² = 2,
  invariance under both plane rotations and x2 ↦ −x2, x4 ↦ −x4, worst defect 1.0 × 10⁻⁴⁰. At ρ2 = 10⁻⁸ the (x3, x4)
  block is −(1/√3) I: isotropic, finite. λ_ϑ = −(2/√3) cos(πζ/3) ≤ −1/√3 everywhere.
- Parallel transport (exact rationals, random 5D Lorentzian g, ∂g, 𝒫, Z, ℓ): with d𝒫_ab/dt = Z^c(Γ^d_ca 𝒫_db +
  Γ^d_cb 𝒫_ad), d|𝒫|²/dt = 0 and d tr 𝒫/dt = 0 exactly; with ℓ parallel along Z, ω := 𝒫(ℓ, ·) obeys the homogeneous
  parallel-transport system exactly, so ω ≡ 0 from zero data.
- λ⁻¹ cancellation (symbolic α, exact γ0 with orbit block and torus block, a radial-family wave vanishing on ν0 and
  trace-free, a torus label, second harmonics M): for both families the λ⁻¹ coefficients in ρ and J vanish at λ = 0
  identically in α, and their λ-derivative does not (so "of order one", not "zero", is the right claim). Controls: the
  same wave with a non-radial phase, and a radial phase with a wave not vanishing on ν0, leave a nonzero coefficient.
- Shear: flat R^(1,4), u = d_E − t for the ellipsoid (α1, α2) = (1/2, 1/3), parametrised by the foot angle t: σ2 is
  even in t with nonzero t² term, σ2/ρ2² is analytic and even, limit −0.0140332488 at d = 3/2 (three step sizes);
  σ1 = 5/((2d + 1)(9d + 2)) on axis 2, smooth and nonzero. So σ2 = ρ2²·(smooth), not identically 0.
- eq:vlasov-axis-commutator in full (both sides computed independently, flat 5D, generic invariant polynomial φ):
  u = (ρ1² + (ρ2 − 3/2)²)^(1/2) − t (σ1 = 0, σ2 = 2.213) and the same with the planes exchanged (σ1 = 2.115, σ2 = 0):
  difference 0 at 40 digits; ℓ̄ null with g(ℓ, ℓ̄) = −1. A non-eikonal control fails by 7.18.
- The data identity (2+1, polynomial lapse, shift, slice metric and phase, W with W(𝔫, ·) = 0 on {t = 0}, full
  two-scale computation): the oscillating λ⁰ part of κ equals ½ ν dφ(𝔫) ∂_θ W exactly, and the lapse has no oscillation
  at order λ.

## The seven checks

1. Read as a referee: findings below. 2. All four pieces hold as mathematics (re-derivations above;
lem:vlasov-axis-smooth (a)–(c) checked by hand, including the induction on 𝓔 and the Taylor factor t²). 3. R-82
Major 2 is overcome, not assumed away: its four items (waves, constraint term, commutator, domain) and the pair's
separation each have a proof; the non-roundness is met by choosing the pair's phase data radial on Σ_τ0, which are free
data, and by transporting the polarisation; the price is (V2′), stated as a hypothesis, and the narrowing to Ω₂′.
4. R2-82 M1 does break P-K82: Major 1. 5. Every [[…]] resolves; the chapter 81 statements (def:class-adapted with
T_(τ,U) and the additive normalisation, thm:class-stability (H2′), S^ax, Steps 9–10, cor:class-two-dust's boundaries
and packet hypothesis, prop:class-axis (a), (d), prop:class-structure (a), (b)) are used in their current form; one
wrong item of chapter 80 is cited (minor 10).
6. The narrowing is honest in the display, rem:vlasov-radial-scope and block 5; the statement's "there" is ambiguous
(minor 5), block 2 omits it (nit 7). 7. Block 5 is true and its old text matches chapter 03, lines 360–361.

Contract: no line over 121; the only "- " line after a non-blank line (331) is a list item; no file, program, code
or AI language; the 13 new labels are unique and none exists elsewhere.

## Major

### M1. Major — the labels are eikonals only near their tubes (R2-82 M1); P-K82 uses them as eikonals on Ω₂

Where it breaks. (a) Lines 428–431: "(H1) holds … for the labels by (V1)". (V1) makes each u_α an eikonal only on the
neighbourhood 𝒲 of 𝒟(S); (H1) of thm:class-stability-off-axes, which thm:class-stability keeps, asks every reference
family to be an eikonal on the whole domain. The current proof of prop:vlasov-uniform-n no longer runs those Steps: it
runs parts (ii)–(iii) of the proof of lem:vlasov-local-stability, whose (H2′) puts every tube 2δ off the axes, which the
radial pair violates. So neither route covers the n + 2 families as written. (b) Lines 417–419: g^(n) is called "a class
Einstein–null-dust solution with the n + 2 families"; after the localisation its labels are eikonals on their tubes only
(statement of prop:vlasov-uniform-n). (c) Lines 322–326: prop:vlasov-radial-step takes g0 "a smooth class
Einstein–null-dust solution on Ω with n + 2 families", which g^(n) is not; sec:vlasov-n now has its own set-up (S_A,
𝒱_A, 𝒯_A, item (v)). (d) Lines 529–530 then check (iii)–(iv) for a set-up that is no longer the chapter's.

What fixes it. Localise the labels only. The pair's transports are never cut off (ζ′_𝔨 = 1, P̃_𝔨 = P_𝔨), so its
equations are (Aug2)–(Aug4) on the whole adapted domain and Step 10 of thm:class-stability gives its phases as eikonals
there; the labels' localisation (cut-offs vanishing within δ of the axes) never meets the axis machinery, and the
adapted boundaries are spacelike, so dF(P̃_A) > 0 holds there as in part (ii) of lem:vlasov-local-stability. In
sec:vlasov-n the pair is a family with S_𝔨 := Σ_τ0 ∩ Ω, so 𝒱_𝔨 = Ω, and (v) (a) holds for it trivially.

- Lines 428–431, old: "(1) *The n-dust developments.* They are given by [[prop:vlasov-uniform-n]] with that reference
  and k = 2, whose proof runs Steps 1–10 of the proof of [[thm:class-stability]] on the adapted domain, in place of those
  of [[thm:class-stability-off-axes]] on Ω₂. (H1) holds for the radial pair by the proof of [[cor:class-two-dust]] and
  for the labels by (V1). (H2′) holds by the proof of [[cor:class-two-dust]]:"
  new: "(1) *The n-dust developments.* They are given by the proof of [[prop:vlasov-uniform-n]] with that reference and
  k = 2, run on the adapted domain: the n labels are localised as in parts (i)–(iii) of the proof of
  [[lem:vlasov-local-stability]], and the radial pair is not, ζ′_𝔨 := 1 and P̃_𝔨 := P_𝔨, so that its equations are
  (Aug2)–(Aug4) on the whole domain, with the changes of the proof of [[thm:class-stability]]. The labels satisfy (H1′)
  and (H2′) of [[lem:vlasov-local-stability]] by (V1) and (V2), and are eikonals of the developments on their tubes
  only; the radial pair satisfies (H1) of [[thm:class-stability-off-axes]], v and u being eikonals of g0 on the whole
  of Ω₂ (proof of [[cor:class-two-dust]]), and Step 10 of the proof of [[thm:class-stability]] gives its phases as
  eikonals on the whole adapted domain. (H2′) of [[thm:class-stability]] holds by the proof of [[cor:class-two-dust]]:"
- Lines 417–419, old: "For n ≥ n0 it has a smooth invariant development g^(n), a class Einstein–null-dust solution
  with the n + 2 families (u_A, q_A) and (ϕ_𝔨^(n), q_𝔨^(n)), in the gauge relative to g_ε, on an adapted domain that
  contains Ω₂′,"
  new: "For n ≥ n0 it has a smooth invariant development g^(n), in the gauge relative to g_ε, on an adapted domain that
  contains Ω₂′, with Ric(g^(n)) = Σ_A q_A du_A ⊗ du_A + Σ_𝔨 q_𝔨^(n) dϕ_𝔨^(n) ⊗ dϕ_𝔨^(n), each u_A an eikonal of g^(n)
  on its tube 𝒯_A as in [[prop:vlasov-uniform-n]] and each ϕ_𝔨^(n) an eikonal of g^(n) on the whole adapted domain,"
- Lines 322–326, old: "Let Ω be a domain of the type [[eq:omega]] and g0 a smooth class Einstein–null-dust solution
  on Ω with n + 2 families: n families (u_A, F_A²) and two families (ϕ_𝔨, F_𝔨²), 𝔨 ∈ {in, out}, the *radial pair*,
  each amplitude smooth and transported by [[eq:vlasov-amplitude]], each generator future directed (after the sign
  change of [[def:vlasov-label]] where needed)."
  new: "Let Ω be a domain of the type [[eq:omega]], let g0, u_A, F_A and S_A (A = 1, …, n) be as in the setting of
  [[sec:vlasov-n]], with Ric(g0) = Σ_A F_A² du_A ⊗ du_A + Σ_𝔨 F_𝔨² dϕ_𝔨 ⊗ dϕ_𝔨 in place of its equation, and let
  (ϕ_𝔨, F_𝔨), 𝔨 ∈ {in, out}, the *radial pair*, be two further families: ϕ_𝔨 an eikonal of g0 on the whole of Ω with
  g0⁻¹dϕ_𝔨 future directed (after the sign change of [[def:vlasov-label]] where needed), F_𝔨 ≥ 0 smooth and transported
  by [[eq:vlasov-amplitude]], and S_𝔨 := Σ_τ0 ∩ Ω, so that 𝒱_𝔨 = Ω."
- Lines 529–530, old: "The waves of the labels are those of the proof of [[thm:vlasov]], and their supports lie at
  distance at least δ from the axes for n large."
  new: "The setting of [[sec:vlasov-n]] holds for the labels of g^(n) as in the proof of [[thm:vlasov]], with the sets
  S_A of that proof and u_A extended off its tube by a cut-off; their waves are those of that proof, and their sets 𝒱_A
  lie at distance at least δ from the axes for n large. For the pair, ϕ_𝔨^(n) is an eikonal of g^(n) on the whole of
  Ω₂′ ([[prop:vlasov-radial-background]] (b))."

## minor

### m1. minor — block 3 reverts the narrowed (O4) now in chapter 82 (R2-82 m3)

Lines 62–63, old: "(O4) A non-radial wave with a component on the orbit block leaves a term of order λ⁻¹ in the
constraints" → new: "(O4) A non-radial wave whose orbit part is a nonzero multiple of q̂ ⊗ q̂, q̂ the unit covector
of the orbit slice orthogonal to the phase's gradient, leaves a term of order λ⁻¹ in the constraints". The rest of
(O4) stays; the pair's orbit part is a multiple of q̂ ⊗ q̂ (q̂ ⊥ dr), and its phase is radial, so it is consistent.

### m2. minor — block 1's old text no longer occurs in chapter 82

F3-82 rewrote lines 26–30 (", except the first two of the metric unknown" and a sentence on
lem:vlasov-local-stability). Re-anchor: old text "The last section shows that the hypotheses are open and that an
explicit family on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]])." → new text "A further
section adds to a small field the two radial dusts of [[thm:two-dusts]], which reach the axes, on domains of the type
[[eq:omega]] inside the adapted domain ([[cor:vlasov-two-dust]]), and the last shows that the hypotheses are open and
that an explicit family on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]])."

### m3. minor — n is both the unit normal and the number of labels

Chapter 82 writes 𝔫 for the unit normal (R2-82 n1); in prop:vlasov-radial-step "n + 2 families" and "both vanish on n"
stand side by side. Replace the unit normal n by 𝔫 at lines 223, 224, 234, 279, 280, 292, 293, 357, 358, 359; e.g.
lines 357–359, old "κ1_𝔨 = ½ ν_𝔨 dϕ_𝔨(n) ∂_(θ_𝔨) W_𝔨 on TΣ_τ0 to κ. By (iii′) both vanish on n and on ν0 = γ0⁻¹dr,
which is γ0-orthogonal to the spheres in Σ_τ0 and orthogonal to n, and both are γ0-trace-free, the γ0-trace of a form
that vanishes on n being its g0-trace." → new: the same with 𝔫 for n (four times).

### m4. minor — two item names collide with the revised chapter 82

(a) sec:vlasov-n now has an item (v) *Localisation*; prop:vlasov-radial-step's own (v) (line 331, used at 359 "By (v)"
and 531 "this is (v)") → rename (vi) at the three places. (b) lem:vlasov-local-stability has its own (H2′) (tubes 2δ
off the axes), the opposite of what the pair satisfies; at lines 426, 431, 473 and 497 write "(H2′) of
[[thm:class-stability]]" for "(H2′)".

### m5. minor — the corollary's statement can be read as claiming the limit on the adapted domain

Line 490, old: "on its adapted domain, which contains Ω₂′ ([[prop:vlasov-radial-background]]), and is a weak limit
there of class vacuum metrics:" → new: "on its adapted domain, which contains Ω₂′ ([[prop:vlasov-radial-background]]),
and on Ω₂′ it is a weak limit of class vacuum metrics:". ("There" follows "its adapted domain"; the display says Ω₂′.)

### m6. minor — lem:vlasov-axis-commutator needs an invariant φ, and the phase shift φ_𝔨 is invariant only if 𝒫 is

The lemma (like cor:vlasov-commutator) is for invariant φ: S(e_i, e_i) = g5⁻¹(dψ_i, dφ) fails otherwise, leaving
σ_i e^(−2ψ_i) ∂²_(φ_i) φ, a second-order term. φ_𝔨 solves ℓ_𝔨·dφ_𝔨 = ½ 𝒫 s_𝔨(h); h and ℓ_𝔨 are invariant, but
[[eq:mollifier]] fixes ρ ∈ C_c^∞(B_1) with no symmetry, and 𝒫 commutes with O(4) exactly when ρ is radial
([[lem:past-mollifier]] takes ρ radial for this reason). The same gap sits in thm:vlasov-n-uniform (4) for the labels.
Lines 348–349, old: "In step (4) the commutator of L_𝔨 is that of [[lem:vlasov-axis-commutator]], whose coefficients"
→ new: "In step (4) the commutator of L_𝔨 is that of [[lem:vlasov-axis-commutator]], which applies since φ_𝔨 is
invariant (h and ℓ_𝔨 are, and 𝒫 commutes with T² and both reflections when the kernel ρ of [[eq:mollifier]] is radial,
as in [[lem:past-mollifier]], which we take), and whose coefficients". For the coordinator: say "ρ radial" once where
chapter 82 introduces 𝒫 (before thm:vlasov-n-uniform), which covers the labels too.

### m7. minor — Ω₂′ is not of the type [[eq:omega]] in the sense the lemmas of chapter 05 use

With a′ − a < ½ and V − V′ < ½ the slices of Ω₂′ have width b(τ) − (V − V′) − a′ > δ0 only (lines 389–390 say so),
while lem:shift-map, hence lem:mollifier, uses b − a ≥ 1 + δ0 ("λ/(b − a) ≤ λ1/(1 + δ0) ≤ 1/20" and "r − a > (b − a)/3
≥ 1/3"). Line 385, old: "Fix a′ with a < a′ < √μ0 and a′ − a < ½, and V′ ∈ (V − ½, V), and put" → new: "Fix a′ with
a < a′ < √μ0 and a′ − a < δ0/4, and V′ ∈ (V − δ0/4, V), and put"; lines 389–390, old: "which exceeds a′ + δ0, as
b(τ) − a ≥ 1 + δ0 ([[lem:two-dust-domain]] (f))." → new: "which exceeds a′ + 1 + δ0/2, as b(τ) − a ≥ 1 + δ0
([[lem:two-dust-domain]] (f)): the slices satisfy the bound of [[eq:omega]] with δ0/2 in place of δ0." Also line 25 of
the comment ("a′ − a < ½ and V′ ∈ (V − ½, V)"). ι of (b) is unaffected.

### m8. minor — ι may be too large for the outer boundary of Ω₂^ι

Lines 464–468 claim v = V − ι + 1 + τ_end − τ > v_end + η on the outer boundary of Ω₂^ι; with V = v_end + T this needs
ι < T + 1 − η, which the choice of ι (≤ ¼) does not give for every T > 0 and η < 1. Line 464–465, old: "and decrease ι
so that 𝒯_out, a compact subset of Ω₂ disjoint from {R = a}, lies in {R ≥ a + 2ι}." → new: "and decrease ι so that
𝒯_out, a compact subset of Ω₂ disjoint from {R = a}, lies in {R ≥ a + 2ι}, and so that ι < V + 1 − v_end − η."

### m9. minor — the limit on varying adapted domains is asserted, not argued

Lines 449–454 pass from "the maps converge along a subsequence" to convergence "on every compact subset of the adapted
domain Ω_ε of the limit", which presupposes the limit's domain. Old: "So a subsequence converges in every C^j on every
compact subset of the adapted domain Ω_ε of the limit that avoids its lateral boundary, and the limit extends smoothly
to Ω_ε." → new: "Put Φ_n(τ, x) := (τ, T_(τ,U_n)(x)) on Ω₂. The Φ_n are bounded in C^k and the g^(n) ∘ Φ_n in C^k(Ω₂),
uniformly in n, so a subsequence of both converges in C^(k−1)(Ω₂); the limit of the Φ_n is (τ, x) ↦ (τ, T_(τ,U)(x))
for the limit U, whose axis values and leaves are the limits of those of the U_n ([[lem:class-leaf-differences]] (b)),
and Ω_ε is the image of Ω₂ under it. A compact subset of Ω_ε that avoids its lateral boundary lies in the adapted
domains of the U_n for n large, where they are bounded in every C^j, so the subsequence converges there in every C^j,
and the limit, bounded in every C^j, extends smoothly to Ω_ε."

### m10. minor — wrong item cited for du(∂_R) < 0

Line 531, old: "(proof of [[prop:two-dust-background]] (a))" → new: "(proof of [[cor:class-two-dust]]: du(∂_R) =
(1 − R_v)/R_u with R_v ≤ ½, and R_u < 0 by [[prop:two-dust-background]] (c))". Item (a) is the structure of the
background; R_u < 0 is (c).

### m11. minor — u is both the outgoing phase and the label field in one paragraph

The setting defines (ϕ_out, q_out) := (u, ℬ/R³) (line 369) and, three lines later, (V1), (V2) for "(g0, 0, u)", the
labels. Write ϕ_out for the outgoing phase where it means that: line 369 keep "(ϕ_out, q_out) := (u, ℬ/R³)" and add
"(u is the outgoing phase of [[sec:two-dust-phases]]; below it denotes the labels)"; and replace "{u1 ≤ u ≤ u2}" by
"{u1 ≤ ϕ_out ≤ u2}" at lines 371–372, 485–486 and 523, "{u1 − η ≤ u ≤ u2 + η}" by "{u1 − η ≤ ϕ_out ≤ u2 + η}" at line
373, "g0⁻¹(dv, du)" by "g0⁻¹(dv, dϕ_out)" at line 399, and "du(∂_R) < 0" by "dϕ_out(∂_R) < 0" at line 531.

## nits

1. Line 171: "In between it has an orbit part λ_ϑ ≠ 0" → "It has the orbit part λ_ϑ ≤ −1/√3 everywhere" (cos(πζ/3) ≥ ½
   for |ζ| ≤ 1; the axes included).
2. Line 201: "G := γ0 + α dr ⊗ dr" collides with the group G three lines up → "𝔊 := γ0 + α dr ⊗ dr" (and 𝔊⁻¹ twice).
3. Notation in sec:vlasov-radial: the template 𝒯 against the tubes 𝒯_A and the constraint stress 𝒯(x, α) of chapter
   82 (rename the template, e.g. 𝒵); κ1, κ2 (torus curvatures) against κ1_A, κ1_𝔨 (data) in the same section (write
   "the κ_i of [[prop:class-structure]]" once, or ϰ_i); Q1, Q2 against the symbols Q_j; E, s, H, σ each in two senses.
4. Line 451: "≤ C (sup 𝒩_k + ε) ≤ C ε" → "≤ C (sup 𝒩_k + ε) ≤ C (ε + n⁻²)".
5. Line 320: "and the identity is [[lem:two-dust-commutator]]" → "and the identity agrees with
   [[lem:two-dust-commutator]], a = 2Θ_h = 2 L(R)/R, up to the grouping of the terms of first order".
6. Line 343: "and is annihilated by its own generator" → "and is annihilated by its own generator and trace-free"
   (D^(0) = 0 uses tr W = 0).
7. Lines 50–51 (block 2): after "can be added to a small field" add "on domains of the type [[eq:omega]] inside the
   adapted domain".
8. Line 372: 𝒯_in, 𝒯_out (η-thickened) against chapter 82's 𝒯_A, the support of family A → write 𝒯̊_in, 𝒯̊_out, as
   cor:class-two-dust does (lines 372–373, 378, 395, 516, 521–523).
9. Line 472: "By [[lem:vlasov-open]], (g_ε, ε F^ε, u^ε) satisfies" → "By [[lem:vlasov-open]], after the replacement
   of the labels made there, (g_ε, ε F^ε, u^ε) satisfies"; line 513: "g_ε satisfies (Ω), (V1) and (V2) on Ω₂′ by
   [[lem:vlasov-open]]" → "g_ε, after the replacement of the labels made in [[lem:vlasov-open]], satisfies (Ω), (V1)
   and (V2) on Ω₂′ by that lemma" (the lemma now states (V1) after the replacement).

## For the coordinator

- P-K82 must be merged after F3-82 settles; M1, m1–m4 and nit 9 are alignments with F3-82's text and should be
  re-checked against its final version (it was being edited while this was read).
- m6 is shared with thm:vlasov-n-uniform (4): one sentence "ρ radial" where chapter 82 introduces 𝒫 closes both.
- Nothing in chapters 00, 01, 08 needs a change (block 6 confirmed); block 5's old text matches chapter 03.
