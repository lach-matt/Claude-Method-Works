# Second reading of P-U71-IS (after F-P-U71-IS)

Reader: R2-P-U71-IS. Text: proofs/P-U71-IS.md as it stands (644 lines, md5 7899ad03d3eff37d629d426769461324; its diff
against 3036fb0 is byte-identical to f_is/fix.diff). Line numbers "l. n" are those of this text. Read against it:
reviews/R-P-U71-IS.md, reports/F-P-U71-IS.md, chapters 30 (lem:iii-a-1-4, -5, Spec_b), 33 (prop:np-10-12, -54), 34
(sec:iii-f1-1, prop:iii-f1-2-3, lem:iii-f-2-1), 40, 41 (def:iii-i10-1-1, def:iii-i10-1-3, lem:iii-i10-1-2), 71
(def:ec-point), P-A-indicial (lem:s14-sextic-split, -count, -small, -large, prop:s14-damping-distance,
lem:s14-vector-distance, lem:s14-delta50), P-U71-assembly (lem:ec-gauge-gap), P-U71-close (rem:uc-missing), P-U71-SP,
and, on the coordinator's request, reviews/R-P-U71-SP.md. Private checks in scratchpad/reader/r2_is/ (num1.py,
num2.py, orders.py, contract.py; outputs num1.out, num2.out).

## Verdict

**NOT CONFIRMED** — 1 Major, 1 minor, 5 nits.

The fix round did what it reports: all 24 findings of R-P-U71-IS are applied, every number stands (all recomputed
below), and the departures (F3, F10, F24) are right. The one Major is old, missed by both earlier passes: prop:is-mult
claims every root of real part in [−101, 5] at hκ ≤ 70 simple because the located roots of P_l "lie in disjoint sets",
but for 134 ≤ l ≤ 172 two of them share one disc (lem:s14-sextic-large (b)) and nothing shows they are distinct. This
is the same gap as F1 (Major) of R-P-U71-SP, found independently here, and the repair is the same, with the exact
constants re-derived. The minor: the "multiplicity at most 3" exception for hκ > 70 that F1 wrote into prop:is-mult is
too weak, since the conjugation symmetry with multiplicity counted makes those roots simple (R-P-U71-SP F3). With both
repairs prop:is-mult says: every root of real part in [−101, 5] is simple. No number moves: l_* stays 50.

## What I re-derived

All in exact rationals or in mpmath interval arithmetic at 120 digits (certified enclosures), with sympy for the
polynomials.

- **lem:is-offsets.** The six first squares and six second squares, each strictly on the claimed side; the bracket of
  I, I′, I₂ is the exact image of the bracket of D^(1/2), D₂^(1/2) (equality at the printed endpoints, strict for I).
  𝔡₀ = 1.33333274074126748912665825006…·10⁻⁶, 𝔡₁ = 3.33333046296485082219485898…·10⁻⁷,
  δ′₁ = 6.00000077999906280030651019…·10⁻⁷, δ₂ = 2.66666533925966422384840394…·10⁻⁷,
  ε₀ = 5.5555532716024871465626…·10⁻¹³: all five inside the printed enclosures. (c): 3 ∥ D, cofactor digit sum 55,
  562501 digit sum 19.
- **F23 (l. 66–68).** 4/21 < (3/10)(1 − z)/(1 + z) and (3z/20)(1 + z) < 6.1·10⁻⁷, exactly; d₂(l) < d₁(l) ≤ δ′₁ < 𝔡₀
  for l ≤ 11 by interval arithmetic; δ₂ < 𝔡₁ < δ′₁ < 2𝔡₁ < 𝔡₀.
- **F6 (l. 289).** (250002000009)^(1/2) − 499999 = 3.00000499998000005499997999913… (500002² = 250002000004), so
  "3.00000499998…" is right.
- **The orders (prop:is-logs (a), (b), F10, F16).** An independent implementation of eq:is-l1 for (c1)–(c4): (c1) and
  (c4) have order 2j at offset j and at most 4 = ⌊t⌋ at non-integer offsets t ≤ 5; (c2) has 3, 9, 17, 27, 39 at
  j = 1, …, 5 and at most 18 at non-integer offsets (attained at 4 + 𝔡₀, 4 + 𝔡₁), equal to
  (⌊t⌋ + 1)(⌊t⌋ + 2)/2 + ⌊t⌋ − 1 at ⌊t⌋ = 4; (c3) has j + (j − 1)₊ and at most 3 at non-integer offsets. The step bounds
  with the corrected p′: 2·5 + 2 − 1 = 11, 1·5 + 1 − 1 = 5, 4·7 + 4 − 1 = 31; u_b: 3·16 + 3 − 1 = 50.
- **The new prop:is-mult and its proof.** *The bound 7*: prop:iii-f1-2-3 (ch. 34 l. 422–447) assumes z ∈ (0, ½] and
  (C1) (ch. 34 l. 285–288). z = 4·10⁻⁶. (C1) at h = 10⁻⁶ follows from prop:np-10-54 (i), (ii) (ch. 33 l. 283–292):
  no root of p_(v), P_0, P_l in [−100, 19/10], none in (19/10, 2) and only ι = 2 (l = 0, 1, simple) at real part 2, so
  every root has real part ≥ 2 or < −100 = −C_0 (C_0 = 100, ch. 34 l. 279), with the counts 1/1, 2/2, 3/3 that (C1)
  lists (at v1 the roots 3 and −1000001 of lem:iii-f1-2-2 are those of p_(v), −499999 ± 500002). Then (a), (b) give
  n_L ≤ 7 roots on each side of (0, 1], counted with multiplicity, so every multiplicity is ≤ n_L ≤ 7. Right.
  *The poles*: on W_π the family is N_L(ι) ⊗ Id_π (ch. 34 l. 303–307, 519–521); N_L⁻¹ = adj N_L/det N_L, so the pole
  order at ι₁ is at most ord_(ι₁) det N_L, the multiplicity at that type; the Laurent coefficients below that order
  vanish on every W_π and so vanish, as in lem:is-roots (b). Right: **the pole order is at most the multiplicity**.
  *The strip*: right except the two points of F1 and F2 below.
- **The hκ > 70 exception and its bound 3.** The bound 3 is correct (three roots of real part above 19/10), but the
  conjugation argument gives 1 (F2).
- **The |ι + j − 1| ≤ 50 step (l. 270–278).** E(α) is "the smallest index set containing the (ι, k) ∈ Spec_b(A) with
  Re ι > α" (ch. 30 l. 1496), an ordinary union, so ℓ̂_(E(α)) at a point is the largest pole order of the roots below it
  on its ladder, not a sum; the roots of positive real part have real part > 1 and Re w ≤ 3, so only roots at w and
  w − 1 enter; ℓ̂ ≤ max(q(w), q(w − 1)) + q(w − 1). With the text's prop:is-mult this gives order ≤ 1 when w is real or
  |w| ≤ 50 (|w − 1| < |w| once Re w > ½) and ≤ 5 always. Correct as written; after F1 and F2 it is ≤ 1 always.
- **The μ_G chain (F7).** μ_G = 1.641602171971270779…·10⁻¹⁴; μ_G < 10⁻¹³ < 1.94·10⁻⁸ < 1.941370568463·10⁻⁸ < δ_50;
  μ_G < 1.4619·10⁻¹⁰. Right (see N1 on how ε_Υ is named).
- **thm:is-gap.** All 28 rows: n⁺, frac (to four digits; the closest call, y = 0.4602, has frac 0.18885024…), n⁻, the
  admissible n, p, q and the excess bounds, every one as printed; y/𝔡₁ and 4y/𝔡₀ at distance ≥ 0.1367 and ≥ 0.0132
  from ℤ; least p = 0 candidate 5.01914·10⁻⁸ > 5.01·10⁻⁸. The three full-digit lines: 1109655𝔡₀ =
  1.4795393424272511756468419604731…, 31682𝔡₁ = 0.010560657572765240374877752234649…, μ_G in [[eq:is-mu]] and in
  (1.6416021719700, 1.6416021719734)·10⁻¹⁴; excesses 2.31814807019761…·10⁻¹⁴ and 8.09593530867985…·10⁻¹⁴, with every
  printed partial product and y inside its printed interval.
- **prop:is-count.** Σ(3 − β)² = 720294717/50000000 = 14.40589434, Σ(3 − β) = 2229/125 = 17.832 over the 26 rational
  β; 1/(2𝔡₀𝔡₁) = 1125001468750.4053819…; ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶; N_Λ > 1.62066522912·10¹³ > 1.62066·10¹³ and
  N_Λ < 1.67471700528·10¹³ < 1.67472·10¹³. **k̄_0 = 3** (𝒢 at 3 = 2 + 1). **J_* = 15,000,015**: 5/𝔡₁ =
  15000012.9166693…; 1/𝔡₁ = 3000002.58333386….
- **cor:is-flat.** μ♭ = 5.0191362449…·10⁻⁸ ∈ (5.0190, 5.0193)·10⁻⁸; y/𝔡₁ = 1470297.2660903… and 1470293.2660886… at
  0.4901 − 𝔡₀, 0.4901 − 2𝔡₀; second least excess 1.38889·10⁻⁷ > 1.3888·10⁻⁷; counts 56,436,655 (28 bases),
  56,436,656 (with β = 3), 59,377,257 (all 31). F21's wording is right.
- **The window 134 ≤ l ≤ 172 (F1).** Exactly: Δ_𝒬 = 0.093562…, 0.035476… at l = 134, 135, −0.023037762176 at l = 136,
  −2.414919… at l = 172; x₋ ∈ (0.01866, 0.01867); U(a) = 0.0057943…, 0.0021967… at l = 134, 135; U(a − 0.45) <
  −0.0178, U(a + 0.45) < −0.37 there; −0.0425·Δ_𝒬(0.018768)/8 = 1.2239·10⁻⁴ > 9.4·10⁻⁵. Sanity only (sympy roots of the
  full determinant P_l at h = 10⁻⁶): at l = 134, 135 the pair is real (2.4376, 2.5899; 2.4673, 2.5605), at l = 136, …,
  172 a conjugate pair (2.51412 ± 0.03858i at 136), least separation 0.0772. The roots are distinct; the text does not
  show it.

## Findings

### Major

**F1 (Major) — l. 336–338 (prop:is-mult, the strip), and so l. 309–313, 268–269, 276–278: for 134 ≤ l ≤ 172 the two
roots of P_l near a(x) are not shown to be distinct.** The proof makes the roots ι ∈ Z of P_l with hκ ≤ 70 simple
"as the three roots in |ι| < 1000 lie in disjoint sets" (lem:s14-sextic-small, -large, -count (a)). For
0.018 ≤ x ≤ 0.03 (x = hκ; l = 134, …, 172, x = 0.018224, …, 0.029928), lem:s14-sextic-large (b) only counts the two
roots other than ι_B in one disc |ι − a(x)| < 0.45 (a Rouché count); part (c), with disjoint discs, starts at
x = 0.03, and prop:s14-damping-distance locates real parts only. So a real double root in (2.06, 2.98) is not
excluded, and with it the claims "simple at the real points of that strip and at its points of modulus at most 50"
(l. 312–313), "the real roots of L̂_b(0) of real part at most 3 are simple" (l. 268–269), and the order ≤ 1 at
ι + 1 + j (l. 276–278). No number depends on it (a double root would give orders ≤ 3, and M ≤ 7 either way), but the
proposition is stated beyond its proof. R-P-U71-IS did not report this; R-P-U71-SP F1 reports it for lem:sp-roots (c),
which cites the same lemmas. The fix below (with F2) is the SP fix, its constants re-derived exactly here (num2.py);
it is written with ξ_x for a(x), Δ for Δ_𝒬 and P_l − U for hW, because a := 99/10000, ε₀ := 𝔡₀ − 4𝔡₁ and W ∈ 𝔰𝔬(4) are
already taken in this section.

*Fix (F1 and F2 together).* l. 334–341, replace from "Such an ι is a simple root of its polynomial, except possibly"
to "counted with multiplicity ([[prop:np-10-54]] (i))." by:

    Such an ι is a simple root of its polynomial: of C, as the other two roots have real part below −100; of p_(v),
    as its two roots are real and of opposite signs; of P_l with hκ ≤ 70, as the three roots in |ι| < 1000 have real
    part at least 2, are all of them, counted with multiplicity ([[lem:s14-sextic-small]], [[lem:s14-sextic-large]],
    [[lem:s14-sextic-count]] (a)), and are distinct, so that they are the three roots of real part above 19/10, each
    simple. Those lemmas place the three in disjoint sets, except for 0.018 ≤ x ≤ 0.03, x := hκ (134 ≤ l ≤ 172),
    where two of them lie in one disc |ι − ξ_x| < 0.45, ξ_x := (3x + 10)/4 ([[lem:s14-sextic-large]] (b)); these two
    are distinct. Indeed P_l = U + (P_l − U) with U(ι) := (2 + x − ι)(2(ι − ξ_x)² − Δ(x)/8) and
    Δ(x) := x² − 1715x/8 + 4, whose smaller root x₋ lies in (0.01866, 0.01867) ([[lem:s14-sextic-split]] (i), (iii)).
    On the disc |P_l − U| < 9.4·10⁻⁵ (proof of [[lem:s14-sextic-large]] (b)), and on its real diameter
    2 + x − ι ≤ x/4 − 0.05 ≤ −0.0425. If x < x₋, that is l = 134 or 135, then 0 < Δ(x) < 0.1, so
    U(ξ_x) = (2 − x)Δ(x)/32 > 2·10⁻³ and U(ξ_x ± 0.45) < −0.0425·0.39 < −0.016: P_l is negative, positive and
    negative at ξ_x − 0.45, ξ_x and ξ_x + 0.45, and the two roots are real and separated by ξ_x. If x > x₋, that is
    l ≥ 136 and x ≥ 0.018768, then Δ(x) ≤ Δ(0.018768) < −0.023, Δ being decreasing on [0, 107], so
    U < −0.0425·0.0028 < −1.1·10⁻⁴ on the real diameter: P_l has no real root in the disc, and the two roots there
    are a non-real conjugate pair. If hκ > 70, P_l has no root with |ι − 1| ≤ 50 ([[lem:s14-sextic-count]] (b)); so
    a root ι ∈ Z of P_l with Re ι ≤ 6 is non-real, a real one having 19/10 < ι ≤ 6 and so |ι − 1| ≤ 5. It is simple:
    P_l has real coefficients, so ῑ ≠ ι is a root of the same multiplicity m and the same real part, and P_l has three
    roots of real part above 19/10, counted with multiplicity ([[prop:np-10-54]] (i)); so 2m ≤ 3.

(Constants, exactly: Δ(0.018224) = 0.093562114176, Δ(0.018495) = 0.035476440025, U(ξ_x) = 0.0057943…, 0.0021967…;
2(0.45)² − Δ/8 > 0.39; Δ(0.018768) = −0.023037762176, −Δ/8 = 0.0028797… > 0.0028, 0.0425·0.0028 = 1.19·10⁻⁴ >
1.1·10⁻⁴ > 9.4·10⁻⁵. The disc bound holds on the closed disc, the majorants of lem:s14-majorant increasing in S;
|ι| ≤ 2.9725 < 2.98 there. Wrap to 121 characters; no line of it then starts with a listed character.)

Then, l. 309–313, replace "Every one of real part in [−101, 5] is a simple root" through "and at its points of
modulus at most 50." by:

    Every one of real part in [−101, 5] is a simple root of each type and degree at which it occurs. So
    N(L̂_b(0), ·)⁻¹ has poles of order at most 7, and simple poles on the strip −101 ≤ Re ≤ 5. (Whether P_l has a
    root of real part at most 6 for some l with hκ > 70, κ = l(l + 2), is not decided here; such a root would be
    non-real and simple.)

l. 276–278, "These poles are simple when w is real or when |w| ≤ 50, since |w − 1| < |w| for Re w > 1, and of order
at most 3 otherwise ([[prop:is-mult]]). So the order at ι + 1 + j is at most 1 when ι is real or when
|ι + j − 1| ≤ 50, and at most 2·3 − 1 = 5 in every case." → "These poles are simple, w and w − 1 lying in the strip
−101 ≤ Re ≤ 5 ([[prop:is-mult]]). So the order at ι + 1 + j is at most 1."

l. 6–8, "which are simple on the strip −101 ≤ Re ≤ 5 except possibly at non-real roots of modulus greater than 50 that
come from the polynomials P_l of large l ([[prop:is-mult]])." → "which are simple on the strip −101 ≤ Re ≤ 5
([[prop:is-mult]])."

l. 633, "has multiplicity at most 7, and at most 3 on [−101, 5] ([[prop:is-mult]]);" → "has multiplicity at most 7,
and is simple on [−101, 5] ([[prop:is-mult]]);".

What changes: the statements of prop:is-mult (simple on the strip, poles simple there), of prop:is-logs (c) (order 1
at every ι + 1 + j), the intro and rem:is-summary. What does not: ℰ^ι_ind ≤ 50, L, the bound M ≤ 7 on the half-plane
(the roots below −101 stay undecided), the (IS) part of l_* (50), and every number of the section. The bound 7 of
prop:is-mult is still what def:iii-i10-1-1 needs below −101.

### Minor

**F2 (minor) — l. 310–312, 340–341: for hκ > 70 the multiplicity bound 3 can and should be 1.** Not false, but weaker
than one line proves, and inconsistent with the sibling: P-U71-SP lem:sp-roots (b) and cor:sp-lstar (a) assert every
root of real part in (1, 4] simple, including roots of P_l with hκ > 70, while this text leaves multiplicity 3 open
there. P_l has real coefficients; the three roots of real part above 19/10 (prop:np-10-54 (i)), counted with
multiplicity, are permuted by conjugation; a non-real root of multiplicity m brings its conjugate, a different root
with the same multiplicity and real part, so 2m ≤ 3 and m = 1. By lem:s14-sextic-count (b) every root ι ∈ Z of P_l with
hκ > 70 and Re ι ≤ 6 is non-real, hence simple. *Fix*: included in the replacement texts of F1 above (the last two
sentences of the proof replacement, the statement, l. 6–8, 276–278, 633). The existence question stays open and is
kept in the statement's parenthesis.

### Nits

**N1 — l. 417, 483–484: ε_Υ is a choice, not a value lem:ec-gauge-gap fixes.** The lemma says "ε_Υ = 1.4619·10⁻¹⁰ is
an admissible choice" (P-U71-assembly l. 16–17), and def:iii-i10-1-3 asks ε_K < ε_Υ; every ε_K < μ_G is available only
for a choice ε_Υ ≥ μ_G. l. 417, "and μ_G < ε_Υ = 1.4619·10⁻¹⁰ ([[lem:ec-gauge-gap]])," → "and μ_G < ε_Υ for the
admissible choice ε_Υ = 1.4619·10⁻¹⁰ of [[lem:ec-gauge-gap]],"; l. 483–484, "and μ_G < ε_Υ = 1.4619·10⁻¹⁰
([[lem:ec-gauge-gap]])," → "and μ_G < ε_Υ = 1.4619·10⁻¹⁰, the choice of [[lem:ec-gauge-gap]],".

**N2 — l. 16: the intro rounds N_Λ more coarsely than prop:is-count (a).** Both are true. "1.6206·10¹³ < N_Λ <
1.6748·10¹³" → "1.62066·10¹³ < N_Λ < 1.67472·10¹³".

**N3 — l. 317–320: the identification of the roots of □^C_b with those of the polynomials is not cited.** (C1) is
about the indicial roots of □^C_b; prop:np-10-54 is about C, P_0, P_l, p_(v). After "[[prop:iii-f1-2-3]] assumes
z ∈ (0, ½], true for z = 4·10⁻⁶, and (C1), which holds at h = 10⁻⁶:" insert "the indicial roots of □^C_b at scalar
type l ≥ 1, scalar type 0 and vector type l are the roots of P_l, P_0 and p_(v) ([[prop:np-10-12]] (ii), (iii), with
h = 1/γ_C), and".

**N4 — l. 324, 327 and throughout: N(L̂_b(0), ·) is not defined.** The proof says "the indicial family of
ρ⁻²L̂_b(0)" and then inverts "N(L̂_b(0), ·)"; lem:is-roots (b) writes N(ρ⁻²(□^Υ_b)^(0), ·). l. 324, "The indicial
family of ρ⁻²L̂_b(0) is that of the model" → "The indicial family N(L̂_b(0), ·) of ρ⁻²L̂_b(0), which we write so
throughout, is that of the model".

**N5 — notation clashes inside the section.** K is the class range (l. 163–165) and a logarithmic order bound in the
step bound (l. 238–244); κ₀ (l. 506–508) sits beside κ = l(l + 2) (l. 311, and in the F1 fix). l. 238–244, rename the
order bound K → k_R (seven occurrences: "of order at most K", "K + ⌊t⌋ + 1", "p(K + ⌊t⌋ + 2)", "K + ⌊t⌋ + 2 ≤ K + 7",
"(K = 0)"); l. 506–508, κ₀ → ν₀ (five occurrences). M* (l. 167, 171, 196, 200) is a set, not the reserved large order;
it may stay, or become 𝔐* if the integrator wants bare M free.

## R-P-U71-IS findings against the text

| Finding | Where now | Status |
|---|---|---|
| F1 (Major) | l. 308–345 | Applied, rewritten; correct except the new F1 and F2 above. Pole order ≤ multiplicity now proved (l. 324–328). |
| F2 (Major) | l. 317–322, 633–636, 6–10 | Applied: (C1) verified at h = 10⁻⁶, bound 7 read off (a), (b); (IS) part of l_* 50. |
| F3 | l. 181–184 | Applied with departure α ≥ 0: right (u₂ uses α just below ι^Υ_(s1,2) > 2). |
| F4 | l. 26–30 | Applied. |
| F5 | l. 284–285, 291–296 | Applied; the three dropped classes add nothing below 5 (checked: m = −2 − d₁(3) gives 5 + d₁(3), 4 + 𝔡_i + d₁(3)). |
| F6 | l. 289 | Applied; 3.00000499998000005… |
| F7 | l. 417–419, 483–485 | Applied; see N1. |
| F8 | l. 425 | Applied. |
| F9 | l. 365–367 | Applied. |
| F10 | l. 246–251 | Applied with departure (c1)/(c4) ≤ 4, (c3) ≤ 3: all three bounds attained exactly as stated. |
| F11 | l. 286–287 | Applied. |
| F12 | l. 17–23, 638–642 | Applied; "smaller index sets, with a larger ε_K" is the accurate wording. |
| F13 | l. 4–10, 630–633 | Applied. |
| F14 | l. 188–189 | Applied. |
| F15 | l. 199–201 | Applied. |
| F16 | l. 241–244 | Applied; 11, 5, 31 exact. |
| F17 | l. 251 | Applied. |
| F18 | l. 261–262 | Applied; Σ_(q≤3) ord(q) = 3 for the simple real roots 0, 2, 3. |
| F19 | l. 402 | Applied. |
| F20 | l. 504 | Applied. |
| F21 | l. 624–625 | Applied; counts 56,436,655 + 1 and 59,377,257. |
| F22 | l. 603–604 | Applied. |
| F23 | l. 67–68 | Applied; exact. |
| F24 | l. 581–584 | Applied with the no-logarithm clause, which the coefficient comparison needs: right. |

The renaming N, M → n⁺, n⁻ (lem:is-reduction, thm:is-gap, table) is complete; no bare N remains.

## L, M and l_* (consistency with P-U71-SP)

P-U71-SP cor:sp-lstar: l_* = max(1, L, M), K_ι ≤ l_* + 2, with L the largest logarithmic order of
ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I and M the largest multiplicity of an indicial root of L̂_b(0), both at real part ≤ 5.

- **L**: ℰ_ind ≤ 39, attained at (5, 39); ℰ^ι_ind ≤ 50 (a bound, from u_b at real exponents); least ℰ^C_I 0. So
  **39 ≤ L ≤ 50**.
- **M**: ≤ 7 on the whole half-plane Re ≤ 5 (prop:iii-f1-2-3 (b)); on [−101, 5], ≤ 3 as the text stands and **1**
  after F1 and F2 (agreeing with SP's lem:sp-roots (b) on (1, 4]); below −101 undecided, ≤ 7. So **M ≤ 7**.
- **l_* = 50** is admissible (the least admissible value is L, between 39 and 50), with the SP pole orders 1;
  K_ι ≤ 52. Unchanged by F1 and F2.
- Shared gap: SP's lem:sp-roots (c) and this prop:is-mult rest on the same unproved distinctness for 134 ≤ l ≤ 172;
  the F1 text above and R-P-U71-SP's F1 text are the same argument with the same constants, and should go into both.

## Contract

- Line length: 644 lines, maximum 121 (Python len). The F1 replacement must be wrapped to 121.
- Wrapped lines: none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|"; the lines beginning "|" are the table.
- Label keys: 32 defined, 202 references, all lowercase; every reference resolves in chapters/ or proofs/.
- Forbidden words: reader/lint.py's patterns give no hit in this file; no file, program, code or AI word ("computed"
  at l. 28 and "computational point" are mathematical uses the lint allows).
- Proofs: 16 opened, 16 ∎, each proof closed by ∎.
- Notation: no bare λ (λ_♯ is declared "not the wavelength"), no ϰ, no Θ, no bare N; K, κ₀ and M* are N5.
