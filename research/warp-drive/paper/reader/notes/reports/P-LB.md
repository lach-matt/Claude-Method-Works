# P-LB: the lower bounds on d, moved onto the proved set

Output: `research/warp-drive/paper/reader/proofs/P-LB.md` (the only file written in the repository). No chapter or
crosswalk was edited, nothing was committed, `assemble.py` was run only with `--check`, and only inside a scratch copy.

## 1. The lemmas

**lem:ec-lb-gauge** (gauge half). For every z ∈ (0, ½]:

- (a) ι^Υ_(sl,l+1) = l + 1 + d₂(l), ι^Υ_(sl,l+2) = l + 2 + d₁(l), with the closed forms of prop:np-10-52 (i) at this z.
- (b) 7z/240 − z²/960 − 49z²/864000 ≤ d₂(7) ≤ 7z/240, and 5z/171 − z²/21600 < d₁(8) ≤ 5z/171 + z²/1368.
- (c) z/13680 − z²/21600 < d₁(8) − d₂(7) ≤ z/13680 + z²/544, so d₁(8) > d₂(7) on the whole range.
- (d) 𝔡_ℳ ≤ d₁(8) − d₂(7), hence ε_Υ < ½𝔡_ℳ ≤ g(z) := z/27360 + z²/1088.

So **c = 1/544, valid on (0, ½]**. The exact coefficient is 30031/16416000 = 0.0018294. Using eq:s14-theta's rounder
θ₂ bound gives 7541/4104000 = 0.0018375; both are below 1/544 = 0.0018382.

Why the lemma re-derives the bounds: ch. 33 states prop:np-10-52 (i) and eq:s14-theta at z = 4·10⁻⁶ only. Their proof
uses nothing beyond z > 0, but the lemma does not lean on that remark. It derives the four one-sided bounds at u = 8 and
u = 9 for general z from eq:ec-sqrt. The lower bound in (c) is needed only to show that the two points are distinct.
Equality 𝔡_ℳ = d₁(8) − d₂(7) is not claimed for general z, and an upper bound does not need it.

**lem:ec-lb-ind** (damping half). For every h ∈ (0, 10⁻⁶], P_2 has a real root ι₂(h) with

    (40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < (40/13)h.

So **c′ = 0 on all of (0, 10⁻⁶]**: ε_ind(h) < (40/13)h. The constant ε_ind of eq:iii-f1-2-2 also satisfies
ε_ind < (40/13)h, given z ∈ (0, ½] and (C1).

- **Proof.** It needs no new determinant expansion. ch. 33's eq:s14-f-two already gives P(2 + w; κ, h) for general
  (κ, h, e). Put w = hξ at κ = 8. This gives P_2(2 + hξ) = Σ_{j=1}^9 p_j(ξ)h^j, with all nine p_j printed. Then
  bound the tail |Σ_{j≥3}| < 0.0017 by majorants, and check two signs:
  - at ξ = 40/13 the h² coefficient is −(9280 + 59920e)/169 < −54.9;
  - at ξ₋ = (40/13)(1 − 5·10⁴h) the value exceeds 1875/32 − 55.07 − 0.0017 > 3.5.
- **Two-sided.** The enclosure shows that 40/13 is sharp.
- **Consistent with lem:s14-sextic-small (b).** At h = 10⁻⁶ the interval is (2 + 2.923h, 2 + 3.077h), which contains
  (2.93h, 2.94h).
- **Improves on δ_50** for h ≤ 6.309·10⁻⁹.

**lem:ec-lb-rounds** re-runs the count of prop:ec-rounds with abstract bounds. Given
ε_g ≤ δ̂, ε_K < δ̂, ε_K < δ̄, η_2 < δ̄ and 5δ̂ + δ̄ < 1, it gives
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) > (1 − 5δ̂ − δ̄)/δ̂². The proof is written out in full.

## 2. The general lower bound (thm:ec-lb-proved, cor:ec-lb-delta)

At every point of the proved set, with z = 4e_Υγ_Υ², h = γ_C⁻¹, δ̂ = min(g(z), 40h/13) and δ̄ = 40h/13:

    d_NM ≥ d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²),   N_NM > 63(1 − 2·10⁻⁵) max(…),

that is:

- **d_acc**: > 2.2456·10⁹ z⁻²(1 + 25.15z)⁻² and > 0.3168 γ_C².
- **N_NM**: > 4.7158·10¹⁰ z⁻²(1 + 25.15z)⁻² and > 6.654 γ_C².
- **In the gauge parameters**: d_acc > 1.4035·10⁸ e_Υ⁻²γ_Υ⁻⁴(1 + 100.6e_Υγ_Υ²)⁻².
- **The threshold δ**: log₁₀ δ < −2.163·10¹⁰ z⁻²(1 + 25.15z)⁻² and log₁₀ δ < −3.052 γ_C², from prop:ec-delta-cap,
  which holds at every point.

**Conditions used** (listed in rem:ec-lb-conditions), each holding on the proved set:

- c1: (v_C, e_C);
- c2: h ≤ 10⁻⁶, since h_* ≤ 10⁻⁶;
- c3: (C1) only, which holds at every h ∈ (0, 10⁻⁶] by lem:iv4-1-3 (a);
- u5: z ∈ (0, ½];
- the definitions of ε_Υ, ε_ind and ε_g;
- w1: ε_K < ε_+ < ε_ind and ε_K < ε_Υ;
- w2: α ∈ (4, 4 + ε_K];
- the choices made inside the proofs: the levels, η_2 ∈ (ε_K, ε_+), 0 < ε < ½ε_g and ε′ ≤ ε.

**Conditions not used:**

- h_0, h_tf and 𝖹;
- ε_0, ε_1, ε_L, γ_1 and 𝖹_exc;
- (C2)–(C5), except that ε_ind exists;
- (G) beyond ε_K < ε_Υ, and (G⁺), (Ex1)–(Ex4), (A_J);
- rows d1–d2, b1–b4 and n1.

So no threshold is evaluated, and the theorem is a statement about the proved set as it stands.

The step d_acc ≥ Σ(2 + ℓ_tf) ≥ 3R and the step d_NM ≥ d_acc are the arguments of thm:loss-d. They are point-free:
lem:ec-closed-forms (d) needs only β_sctf < 3/2 and ϑ_in ≥ 0, which lem:ec-theta-in (b) proves for L_b at every value
of the parameters.

rem:ec-lb-unbounded draws the consequence:

- d is unbounded on the proved set, because 𝖧 reaches 0 and z can be taken small.
- d exceeds 1.57157·10⁵⁰ wherever h ≤ 4.48·10⁻²⁶.
- If (1/100, 1/100) is admissible at some h ∈ 𝖧, then d > 1.4032·10²⁰ there, and d > 0.3168γ_C² when h < 4.75·10⁻¹¹.
- 1.2497·10²⁴ stays a statement at the point.

Plan item (0), the new text of rem:ec-point-outside, says:

- The point is outside through h. h_* ≤ 10⁻⁶ whatever h_0 and h_tf are, and 𝖧 is open at h_*.
- The gauge half is undecided.
- def:ec-point does not fix γ_(Υ,H), on which ε_1 depends.
- No number of ch. 71 depends on γ_(Υ,H):
  - γ_(Υ,H) does not occur in ch. 71;
  - lem:iii-d-5-1 gives ϑ_ℋ(□^Υ) = 1 for every γ_(Υ,H);
  - lem:iii-f2-1-1 has y = 0 for c_(Υ,H) = −½χ dr, so ϑ_L = max(0, 2 − 2x);
  - the indicial roots behind ℳ and ε_Υ do not depend on the horizon modification.

## 3. Numbers recomputed

Exact rational arithmetic was used throughout, with an independent check at 60–80 digits.

**Gauge lemma:**

- 5/171 − 7/240 = 1/13680, and c₋ = 6561/142228224 = 4.613·10⁻⁵ < 1/21600.
- At z = 4·10⁻⁶:
  - 2.923969·10⁻¹⁰ < d₁(8) − d₂(7) < 2.924271·10⁻¹⁰, against the true value 2.924258·10⁻¹⁰;
  - this is consistent with eq:ec-gauge-gap's (2.9239, 2.92428)·10⁻¹⁰;
  - g = 1.4621354·10⁻¹⁰ < 1.46214·10⁻¹⁰, the paper's δ̂;
  - 3(1 − 2·10⁻⁵)/g² = 1.40326·10²⁰. This reproduces 1.403·10²⁰; the paper's own figure is 1.40325·10²⁰ with
    δ̄ = δ_50.
- The four one-sided bounds of (b), (c) and the bounds on w were checked on 4,000 grid points of (0, ½], and at
  z·10⁻⁶. No failure.

**P_2:**

- The p_j agree identically with eq:s14-f-two at κ = 8, and with the determinant of eq:s14-nl.
- p₂(40/13) = −11879149/216320 = −54.9147 and p₂(38/13) = −476495873/8652800 = −55.0684.
- The majorants of |p₃|…|p₉| at (40/13, 10⁻⁵) are 1635.5, 2645.1, 2855.1, 4141.0, 2358.0, 1654.8 and 848.6. The tail
  is 0.0016355 at h = 10⁻⁶.
- The signs were checked at 140 values of h from 10⁻⁶ to 10⁻²⁰. P/h² ≈ −54.91 at the upper end and +3.53…3.68 at the
  lower end. No failure.
- (ι₂ − 2)/h is 2.93235 at 10⁻⁶, 3.06250 at 10⁻⁷, 3.07548 at 10⁻⁸ and 3.0769087 at 10⁻¹⁰, tending to 40/13 = 3.0769231.
  This agrees with S-INSIDE's 3.0755 at 10⁻⁸.

**Theorem constants:**

- 3·27360²(1 − 2·10⁻⁵) = 2.24566·10⁹. S-INSIDE's 2.2457·10⁹ omits the factor.
- 3(13/40)²(1 − 2·10⁻⁵) = 0.316869, against S-INSIDE's 0.317.
- Times 21: 4.71589·10¹⁰ and 6.6542.
- Times 472/49: 2.16317·10¹⁰ and 3.0523.
- 6δ̄ ≤ 240/13·10⁻⁶ = 1.846·10⁻⁵ < 2·10⁻⁵.
- Crossovers:
  - 40h/13 = g(4·10⁻⁶) at h = 4.7519·10⁻¹¹;
  - (40/13)h = δ_50 at h = 6.309·10⁻⁹;
  - 0.31687/h² = 1.57157·10⁵⁰ at h = 4.490·10⁻²⁶, stated as h ≤ 4.48·10⁻²⁶ for margin.

**Trial merge.** In a scratch copy of the chapters:

- all nine old texts were found exactly once and replaced;
- the section was inserted after sec:ec-delta;
- lint --chapters gave 0 hits on 62 chapters;
- assemble --check gave 0 problems;
- no resolved line is over 121 characters;
- assembled-paper lint gave 0 hits.

The new labels resolve, at present numbering, to Section 49.8 and Lemma 49.34–Remark 49.41. Linted alone, the
proof part gives only undefined-label hits, and those labels are all defined in the chapters. Linting the whole of
P-LB.md gives expected hits in the Placement and crosswalk part: crosswalk paths, and rem:ec-point-outside appearing in
both the old and the new quotation.

## 4. Placement given (exact old and new texts in P-LB.md)

- **ch. 71:**
  - opening paragraph, lines 16–25;
  - rem:ec-point-outside, lines 49–57;
  - the paragraph after thm:loss-d, lines 1462–1464;
  - prop:ec-delta-cap, line 1512;
  - rem:ec-not-evaluated, lines 4693–4695;
  - the new section goes between line 1527 ("stop.") and the heading of sec:ec-upper.
- **ch. 00:** abstract, lines 32–37.
- **ch. 01:** sec:introduction-scope, lines 150–154.
- **ch. 03:** sec:further-results, the constants item, lines 351–357.
- **ch. 90:** sec:scope-constants, lines 66–67.

1.2497·10²⁴ is kept at the computational point everywhere. The intro and scope texts write γ_C rather than h, because
h also names the metric perturbation in "h + h_rem(q)". Crosswalk rows are given for the 16 new labels, with notes for
the existing rows. The front matter has no crosswalk rows.

## 5. Not closed, and coordination

1. **The raised bound 1.2497·10²⁴ is not moved.** It needs the least excess μ_G at general z.
   - A cheap partial route exists: an explicit upper bound for ε_K from the two-offset family λ_♯ + a𝔡₀ + b𝔡₁ by a
     Dirichlet / three-distance argument. It is probably O(z²), which would give R ≳ z⁻³.
   - Not attempted, as instructed.
2. **No upper bound for d on the proved set.** rem:ec-lb-unbounded proves that none can be uniform. A certified point
   still needs h_0, h_tf, ε_0 and ε_1.
3. **Dependence on ch. 33.** The proof cites eq:s14-f-two, lem:iv4-1-3, prop:np-10-52, sec:s14-simple,
   lem:s14-sextic-small and lem:s14-delta50. If the agents editing ch. 33 rename eq:s14-f-two or change the f_j,
   lem:ec-lb-ind must be rechecked. It cites nothing in chapters 20 or 63 or in Appendix A.
4. **Coordination with P-K.** There is no line overlap:
   - P-K changes ch. 71 lines 26–27, ch. 90 lines 72–73 and ch. 03 line 311;
   - P-LB changes ch. 71 lines 16–25, ch. 90 lines 66–67 and ch. 03 lines 351–357.

   P-K's phrases "d is not evaluated on the set where thm:settling is proved" and "d is bounded only at the
   computational point" (its texts 3, 6, 7) become accurate only for upper bounds once P-LB is placed. I suggest
   "bounded above only at the computational point".
5. **G-SWEEP row C7** (plan item 0) lies outside my write scope and was not edited. The suggested wording is: "known
   outside in h (by construction); undecided in (γ_Υ, e_Υ)".
6. **Weaker correction term.** δ̄ is taken as 40h/13 rather than min(40h/13, δ_50), for a uniform statement. This only
   weakens the correction term to (1 − 2·10⁻⁵).
