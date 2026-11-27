# Review R2-P-TR: proofs/P-TR.md (md5 48074b35225dbe6f5b7652efb534d15a, 924 lines), second reading

**Verdict: NOT CONFIRMED. 0 Major, 8 minor, 9 nits.**

The repaired transfer is sound in substance. Everything below holds as stated:

- the lower bound d_NM ≥ d_acc > 2.0517·10¹⁰/μ(h) at every admissible h ∈ (0, 10⁻⁶], and its floor 1.2498·10²⁴;
- the intermediate-value argument of prop:tr-mu-small;
- lem:tr-z3 and prop:tr-lambda;
- the new b ≥ 56 parts of lem:tr-large (c) and lem:tr-slopes (b);
- the n = 3 clause of 𝖩 and the measure bound 1.698·10⁻¹¹.

I recomputed every new number independently (section "Recomputation"). All are correct.

What blocks confirmation is eight minor findings:
- one false proof step in prop:tr-fail, introduced in this round by moving its hypothesis to the end (m1);
- two wrong justifications in the proof of thm:tr-transfer (iii), one created by the merge of P-UB1 (m2, m3);
- five overclaims or undefined notation in the section's own text and in the placement texts (m4–m8), one of which
  undoes the first reading's m10.

Every replacement below was applied to a scratch copy and checked in the scratch merge.

Base used, as the coordinator asked. HEAD edafc288 has the same chapters as ebc73adf, where P-I11, P-UB1 and P-UB2
are merged together with J1–J3. The chapter md5s at HEAD are:
- 71-explicit-constants.md ef1085259abb5d8008f7300656235055;
- 03-theorems.md e0648449a1d880dfc81286159380cdb6;
- 90-scope.md b01d87820565a9e3ccffd03689a63038;
- 33-s14-constraint-damping.md 3c9903830291c7d9b1030e40e6ba85b6.

Chapter 71 at HEAD is identical, line for line, to my own earlier merge of HEAD a03de14d + P-UB1 (all 14 blocks) +
P-UB2 (all 43 blocks of its section 5), apart from the three lines J1–J3 add.

Line numbers below are those of P-TR.md as it stands.

---

## Placement at HEAD, and J1–J3

**Old texts.** Every old text occurs exactly once at HEAD as whole lines:

| item | file | line at HEAD | line P-TR states |
|---|---|---|---|
| 1 | 71, heading of sec:ec-linear | 5499 | 5496 |
| 2 | 71 | 30 | 30 |
| 3 | 71 | 85–86 | 85–86 |
| 4 | 71 | 1820–1821 | 1820–1821 |
| 5 | 03 | 364 | 364 |
| 6 | 90 | 81 | 81 |
| 7 | 33 | 4535–4537 | 4535–4537 |
| 8 | 71 | 5491 | 5488 |

Items 1 and 8 are three lines later because J1, J2 and J3 each add one line before them; see nit 7.

**Scratch merge** (HEAD + P-TR) in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rptr2/merged3a:
- `lint.py --chapters`: 62 files, 4956 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- The in-memory check prints `[] 0`.
- No line exceeds 121 characters after labels resolve. The longest lines from P-TR are exactly 121.
- In the assembled paper sec:tr is Section 49.15, thm:tr-transfer Theorem 49.128, eq:tr-split (49.67) and
  prop:tr-mu-small Proposition 49.142.

With all the replacements of this review applied, the same checks give the same result: 0 hits, 0 problems, `[] 0`,
longest line 121. That merge is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rptr2/merged3c, and the
patched copy of P-TR is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rptr2/P-TR-fixed2.md
(928 lines).

**J1–J3.** None overlaps or touches any P-TR old text. Their contents hold at every h that P-TR treats:
- **J1** (sec:uc-index-sets) lists 1 + 𝒵 among the generators, as P-TR's input (e) assumes.
- **J2** (proof of lem:cs-fourier (b)) adds the exponents (μ, ·), μ ∈ 𝒵 with Re μ < 2 + ε_+ − ε, and uses 𝒵 ⊂ {Re > 1}.
  This holds at every h ∈ (0, 10⁻⁶], by (C1) and prop:iii-f1-2-3 (a). P-TR's list of what that proof uses at h could
  name it (nit 9, optional).
- **J3** (cor:sp-lstar (d)) puts the poles on {2 ≤ Re ≤ 3 + ε_+} in Λ through 1 + 𝒵. At h this follows from
  prop:tr-lambda (a). It enters no bound, as J3 itself says, so the sentence "[[cor:sp-lstar]] hold at h" in the proof
  of (iii) stays true.

**Crosswalk.** The 28 rows are complete: one per label defined in the section, in the order the labels are defined.
Each PENDING line number matches the line of its label. The edits below change the line count, so the rows must be
re-pinned after them; nit 8 also changes three notes.

---

## The first reading

| finding | status |
|---|---|
| M1 | Resolved. The b ≥ 56 disc lies in {Re ι > −1/(2h)} (lines 322–327). It is now strengthened: the root lies in the ϱ-disc when h ≥ h_m (lines 328–335), which I verified (below). |
| m1 | Resolved: 4.751175·10⁻¹¹ (lines 34, 96) and 9.98011…·10⁻⁷ (line 663). |
| m2 | Resolved (lines 406–408). |
| m3 | Resolved at lines 28–29 and 691–692 and in text 7. Texts 2, 4 and 6 no longer make the claim. |
| m4 | Resolved for prop:is-ci-pp. thm:is-gap is now handled through prop:tr-lambda (b). But see m3 below: cor:is-flat has become h-dependent. |
| m5–m8 | Resolved. |
| m9 | Resolved for 𝖧, h_* and ε_Υ. The new texts bring in undefined κ and Λ (m8 below). |
| m10 | **Regressed.** Text 6 was rewritten and lost "for d and N_NM". It again reads "upper bounds there" next to the K sentence of chapter 90 (m7 below). |
| nits 1–10, 12–15 | Resolved, or moot after the rewrite: nit 12's sentence is replaced by the new proof of (ii). |
| nit 11 | **Not applied.** Line 363 still says "A, B from above at the right end" (nit 5 below). |

---

## Major

None.

---

## minor

**m1. prop:tr-fail: the first clause is stated for every ε_ind(h), but the proof covers only ε_ind(h) < 3.17·10⁻¹⁰
(lines 660–669).**

- **What the text does.** The statement now reads: "Every admissible choice … gives d_NM ≥ d_acc >
  3(1 − 2.1·10⁻⁸)/ε_ind(h)², which exceeds 7.5755·10⁵⁵, and so the bounds …, when ε_ind(h) < 1.99·10⁻²⁸." The proof
  asserts "5Θ_g + Θ_η < 2.1·10⁻⁸" with Θ_g = ε_ind(h), Θ_η = δ̄, under no condition on ε_ind(h).
- **Why the step fails.** δ̄ = 1.94137057·10⁻⁸, so the inequality needs ε_ind(h) < (2.1·10⁻⁸ − δ̄)/5 = 3.1726·10⁻¹⁰.
  Off 𝖩, ε_ind(h) can be as large as δ_50 ≈ 1.94·10⁻⁸ (thm:tr-transfer (i)). Crosswalk row 27 reads the first clause
  as unconditional.
- **How it arose.** At e8d94b36 the hypothesis stood first ("If ε_ind(h) < 1.38·10⁻²⁵, every admissible choice …").
  This round moved it to the end of the sentence.
- **Why it is minor.** The clause is true for large ε_ind(h) by another route: (ii) gives d_acc > 1.2498·10²⁴, which
  exceeds 3/ε² once ε > 1.55·10⁻¹². But the proof as written is wrong.

Replace lines 660–664 by:

```
**Proposition {#prop:tr-fail}** (The bound fails near a crossing.) Let 0 < h < 10⁻⁶, and suppose that the parameter point
(h, 1/100, 1/100) is admissible and that ε_ind(h) < 1.99·10⁻²⁸. Every admissible choice of the weights at (h, 1/100,
1/100) gives d_NM ≥ d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)², which exceeds 7.5755·10⁵⁵, and so the bounds for d_acc and d_NM of
[[thm:uc-integer]]. Let h_c := 1/1001992 = 9.98011…·10⁻⁷; then h_c ∈ 𝖩, ι_v(1000, h_c) = 4, and ε_ind(h) < 1.99·10⁻²⁸ for
0 < |h − h_c| < 1.986·10⁻³⁴.
```

and lines 666–669 by:

```
*Proof.* [[lem:ec-lb-rounds]] applies with Θ_g := ε_ind(h) and Θ_η := δ̄: ε_g ≤ ε_ind ≤ ε_ind(h), ε_K < ε_+ < ε_ind,
η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄, and 5Θ_g + Θ_η < 10⁻²⁷ + δ̄ < 2.1·10⁻⁸. It gives R > (1 − 2.1·10⁻⁸)/ε_ind(h)²; so by the
argument of [[thm:loss-d]] (ii), which does not use the computational point (proof of [[thm:ec-lb-proved]]),
d_NM ≥ d_acc ≥ 3R > 3(1 − 2.1·10⁻⁸)/ε_ind(h)² > 3(1 − 2.1·10⁻⁸)/(1.99·10⁻²⁸)² > 7.5755·10⁵⁵. At l = 1000,
```

**m2. Proof of thm:tr-transfer (iii), lines 600–602: the rows that 1 + 𝒵 adds are misdescribed.**

- **Current text.** "the rows of type s1 that the generator 1 + 𝒵 adds have real part equal to that of a root ι ≠ 2 of
  P_1, which exceeds 2 + 3e ([[lem:tr-small]] (a))".
- **What the added rows are.** By eq:iii-i10-1-1 and the definition of ℰ_rows, the rows that 1 + 𝒵 adds are the rows
  (τ, λ, k) with λ ∈ Λ ∖ Λ_ℬ and Re(λ + d_τ) ≤ 2. Their λ run over all ι + p𝔡₀ + q𝔡₁ with ι ∈ Z₃(h), not only over
  the roots of P_1.
- **Why the stated bound is false.** The least such real part is that of ι₂(h), and
  ι₂(h) − 2 < 40h/13 ≤ 3.08·10⁻⁶ < 3e = 2.93·10⁻⁵ (lem:tr-small (b)). So "exceeds 2 + 3e" is false for these rows.
- **The conclusion still holds**, by prop:tr-lambda (a): every element of Λ ∖ Λ_ℬ of real part at most 3 + ε_+ has
  real part greater than 2 + 1.4646·10⁻¹⁰. So ℰ_rows ∩ {Re < 2} is unchanged.

Replace lines 600–602 by:

```
orders and multiplicities of (i) ([[prop:tr-inputs]] (a), (d)), and the rows that the generator 1 + 𝒵 adds have exponents
λ ∈ Λ ∖ Λ_ℬ, of real part greater than 2 + 1.4646·10⁻¹⁰ ([[prop:tr-lambda]] (a)), so that the part of real part below 2
is unchanged. The proof of [[lem:uc-admissible]] applies at h with these ε_K and ε_+: (G) and (G⁺)
```

**m3. Proof of (iii), line 611: cor:is-flat is no longer "fixed by (γ_Υ, e_Υ)", and that proof does not use it.**

- **What changed.** At HEAD, cor:is-flat is P-UB1's T12. Its least excess μ♭_Z = (n + 1)𝔡₁ − y is taken at the
  non-real root of P_700 at h = 10⁻⁶ ([[lem:is-z3]]). It is a statement about Z₃ at the computational point.
- **Why it can be dropped.** It is cited only in rem:gap-sums, the opening of sec:is and rem:is-summary. No step of
  thm:uc-integer or prop:uc-dependence uses it.
- **History.** At the first reading cor:is-flat was gauge-only, so the list was right then. The merge of P-UB1 made it
  false.

Replace on line 611 "[[thm:is-d0]], [[cor:is-flat]] and [[lem:uc-two-offsets]] concern" by "[[thm:is-d0]] and
[[lem:uc-two-offsets]] concern". The line becomes:

```
[[thm:is-d0]] and [[lem:uc-two-offsets]] concern numbers fixed by (γ_Υ, e_Υ); [[prop:is-ci-pp]] uses
```

**m4. "(a)–(d) … with their values at the computational point" is stronger than what is proved (line 20, rem:tr-scope
line 94, placement text 3).**

- **What does not carry over.** At h, ε_ind(h) is only shown to lie in [ε_Υ, min(δ_50, ι₂(h) − 2)]. It is not its
  value δ_50 at the computational point, and it is below δ_50 for h ≤ 6.309·10⁻⁹. The exponents ι + 1 + j of
  ℰ^ι_ind and the singular roots of (d) move with h.
- **What carries over** is the form the proof uses: ε_g = ε_Υ, ε_Υ ≤ ε_ind ≤ δ_50, real part above 3 and not an integer,
  simplicity, and orders at most 1, 3 or 50 (thm:tr-transfer (i), prop:tr-inputs).
- **Why it matters.** Text 3 tells the reader of rem:ec-point-outside that the inputs "keep their values", which is
  false as written.

The fixes are under m5 (opening paragraph), nit 1 (rem:tr-scope) and m8 (text 3), where the same lines carry other
changes:
- line 20: "with their values at the computational point" → "in the form in which the proof uses them at the
  computational point";
- line 94: "carry over with their values at h = 10⁻⁶" → "carry over in the form the proof uses at h = 10⁻⁶";
- text 3: "keep their values at the computational point" → "enter its proof as at the computational point".

**m5. Unboundedness near h_μ is stated as if admissible points there were known to exist (lines 26–27, placement
text 4, crosswalk row 28).**

- **What is proved.** prop:tr-mu-small proves: for every D there is δ with d_NM > D at every admissible
  h ∈ (h_μ, h_μ + δ). That is vacuous if no admissible point lies near h_μ, and rem:tr-scope says this paper does not
  decide whether any h ∈ [h_m, 10⁻⁶) is admissible.
- **What the texts say.**
  - Line 26–27 says "so no upper bound for d holds uniformly in h near h_μ". If there are no admissible points there,
    every bound holds vacuously.
  - Text 4 says the bound "is unbounded at the admissible points near a point h_μ". That presupposes such points
    accumulate at h_μ.
- **What is true without that presupposition:** μ(h) → 0 as h ↓ h_μ, and the bound 2.0517·10¹⁰/μ(h) → ∞.

Replace lines 20–35, which carry m4's change at line 20, this change and m6's, by:

```
10⁻⁶) outside a set 𝖩 ([[def:tr-exceptional]]), in the form in which the proof uses them at the computational point.
Input (e) moves with h: the gap of (G) becomes the least excess μ(h) above 3 that the roots of real part below 3 give
([[def:tr-excess]]), and the count has a bound that grows like h^(−1/2) ([[sec:tr-lambda]]). So the lower bound becomes
d_NM > 2.0517·10¹⁰/μ(h), at every h ∈ (0, 10⁻⁶] at which the parameter point (h, 1/100, 1/100) is admissible, and the
upper bound becomes the bound of [[prop:uc-dependence]] at that gap and that count, at the h ∈ [h_m, 10⁻⁶) ∖ 𝖩 at which,
besides, the degrees with hκ > 70 have no root of real part in [2, 3 + ε_Υ) ([[thm:tr-transfer]]). This paper decides
that condition, and evaluates μ(h), only at h = 10⁻⁶. As h decreases to a point h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and
the lower bound tends to infinity ([[prop:tr-mu-small]]). The set 𝖩 is the price of moving h for (a)–(d): as h varies,
the roots of real part at least 5/2 cross the integers, at finitely many values of h for each degree, and near such a
value, when the root has |ι − 1| ≤ 50, ε_ind(h) tends to 0; 𝖩 holds as well the finitely many h at which two roots of P_l
near 5/2 meet, and the h at which a non-real root has real part within ε_Υ of 3. 𝖩 is a finite union of intervals and
points of total length below 1.7·10⁻¹¹ ([[prop:tr-measure]]), and it cannot be dropped: near such a crossing, at every h
at which the parameter point is admissible, every admissible choice of the weights gives d_acc above the bounds of
[[thm:uc-integer]] ([[prop:tr-fail]]). The lower end h_m is fixed by the root ι₂(h) of P_2 near 2, with
(40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < 40h/13 ([[lem:ec-lb-ind]]): below 13ε_Υ/40 = 4.751175·10⁻¹¹ no h satisfies (H_ε)
([[prop:tr-eps]] (b)).
```

Replace text 4's New block (lines 760–763), which also carries the μ(h) change of m8, by:

```
([[lem:uc-two-offsets]]), and the second also at h = 10⁻⁶ ([[thm:is-gap]]); they are stated at the computational point
only. At the admissible points with (e_Υ, γ_Υ) = (1/100, 1/100) and other h ≤ 10⁻⁶ the second is replaced by
d_NM > 2.0517·10¹⁰/μ(h), with the least excess μ(h) of [[def:tr-excess]] ([[thm:tr-transfer]]); as h decreases to a point
h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and this bound to infinity ([[prop:tr-mu-small]]).
```

Crosswalk row 28: "d_NM unbounded there" → "the lower bound tends to infinity there".

**m6. "the count grows like h^(−1/2)" (line 22, placement text 2, crosswalk row 4).**

- **What is proved.** Only an upper bound: N_Λ ≤ N̄(h) < 4.961·10¹⁴ + 1.0155·10¹²h^(−1/2), from lem:tr-z3 (b) and
  prop:tr-lambda (c).
- **What is not proved.** No lower bound for N̄(h) or N_Λ in h is proved, so "grows like" is not established. A lower
  bound for N̄(h) would be easy (y_ι > 1 − 3x/2 for ι_B with x ≤ 1/2), but the paper does not state it.

The fixes:
- line 22: in the m5 block above, "and the count has a bound that grows like h^(−1/2)";
- text 2: in the m8 block below, "a count bounded by a multiple of h^(−1/2)";
- crosswalk row 4: "N̄(h) grows like h^(−1/2)" → "N̄(h) is bounded by a multiple of h^(−1/2)".

**m7. Texts 5 and 6 claim upper bounds at all the other h. Text 6 again leaves the reach of "upper bounds" open (m10
of the first reading).**

- **Text 5** (chapter 3) says "at the other damping parameters h = 1/γ_C ∈ (0, 10⁻⁶) … upper bounds under a condition
  decided only at γ_C = 10⁶".
- **Text 6** (chapter 90) says "upper bounds there are explicit in μ(h) and h only under a condition …".
- **Why both overstate.** thm:tr-transfer (iii) needs h ≥ 4.76·10⁻¹¹ and h ∉ 𝖩 besides (R_h). No upper bound is
  proved for h < h_m even under (R_h).
- **Two further defects in text 6.**
  - "only under a condition" also reads as asserting that the condition is necessary, which is not proved.
  - Text 6 sits right after chapter 90's sentence on K. As m10 found, "upper bounds" there can be read as including K,
    which thm:tr-transfer does not bound. The fix of the last round ("for d and N_NM") was lost in the rewrite.

Replace text 5's New block (lines 771–774) by:

```
  weights, orders and inner products ([[thm:uc-integer]]), and at the other damping parameters h = 1/γ_C ∈ (0, 10⁻⁶) with
  the same gauge parameters lower bounds that are unbounded near some γ_C ∈ (10⁶, 2 × 10⁶), and, for γ_C ≤ 2.1 × 10¹⁰
  outside a set of h of total length below 1.7 × 10⁻¹¹, upper bounds under a condition decided only at γ_C = 10⁶
  ([[thm:tr-transfer]], [[prop:tr-mu-small]]); through the lower bounds, upper bounds for δ and for the
```

Here γ_C ≤ 2.1 × 10¹⁰ gives h ≥ 4.7619·10⁻¹¹ > h_m.

Replace text 6's New block (lines 783–788), which also carries the μ(h) change of m8, by:

```
set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]). At the admissible parameter points with the same
gauge values and other values h ∈ (0, 10⁻⁶) of the damping parameter, d > 2.0517 × 10¹⁰/μ(h), μ(h) the least excess above
3 that the roots of real part below 3 of the damping polynomials give to the exponents of the construction, which tends
to 0 as h decreases to some h_μ ∈ (5 × 10⁻⁷, 10⁻⁶); this paper proves upper bounds for d and N_NM there, explicit in μ(h)
and h, only for h ≥ 4.76 × 10⁻¹¹ outside a set of total length below 1.7 × 10⁻¹¹ and under a condition on the roots of
the damping polynomials of large degree that is decided only at h = 10⁻⁶, and whether such points are admissible is not
decided ([[thm:tr-transfer]], [[prop:tr-mu-small]], [[rem:tr-scope]]). No result of [[ch:explicit-constants]] is used in
```

**m8. Placement texts 2, 3, 4 and 6: notation not defined where they land, and μ(h) described as the least excess of
all of Λ.**

- **κ in texts 2 and 3.** Both use κ ("the degrees with hκ > 70"). Chapter 71 defines κ = l(l + 2) only later, in
  sec:is-z and sec:tr. Before these texts, κ in chapter 71 denotes a chart map (lem:fwd-transport). This is the same
  kind of finding as m9 of the first reading.
- **Λ and N_Λ.** Text 2 uses Λ in the chapter's opening without a reference. Text 3 uses N_Λ before lem:uc-lambda
  defines it.
- **μ(h) in texts 4 and 6.** They call μ(h) "the least excess above 3 of the elements of Λ at h", or "of the exponents
  of the construction". That is not the μ(h) of def:tr-excess.
  - A root ι of real part in [3, 3 + ε_Υ) at h ∈ 𝖩, or a large-degree root where (R_h) fails, gives Λ an element with
    excess Re ι − 3, which μ(h) does not count.
  - So the least excess of Λ can be below μ(h), and the bound the texts then state is stronger than thm:tr-transfer
    (ii). It follows from the same argument, but it is not what the cited theorem says.
  - Text 2's description ("that the roots of real part below 3 … give") is the right one.

Replace text 2's New block (lines 729–734), which also carries m6, by:

```
it bound what this proof's choices produce, not the optimal loss. At the admissible parameter points with the same gauge
values and other values h ∈ (0, 10⁻⁶) of the damping parameter, d_acc and d_NM exceed 2.0517 × 10¹⁰/μ(h), μ(h) the least
excess above 3 that the roots of real part below 3 of the damping polynomials give to the set Λ of [[def:iii-i10-1-1]],
which tends to 0 as h decreases to some h_μ ∈ (5 × 10⁻⁷, 10⁻⁶); upper bounds there are explicit functions of μ(h) and of
a count bounded by a multiple of h^(−1/2), for h ≥ 4.76 × 10⁻¹¹ outside a set of total length below 1.7 × 10⁻¹¹, under a
condition on the roots of the damping polynomials of large degree that is decided only at h = 10⁻⁶ ([[thm:tr-transfer]],
[[prop:tr-mu-small]]). The
```

Replace text 3's New block (lines 744–750), which also carries m4, by:

```
z = 4e_Υγ_Υ² and h, with no threshold evaluated, through bounds for ε_Υ and ε_ind(h) that hold at every such point
([[lem:ec-lb-gauge]], [[lem:ec-lb-ind]], [[thm:ec-lb-proved]]). With (e_Υ, γ_Υ) = (1/100, 1/100) and
4.76·10⁻¹¹ ≤ h < 10⁻⁶ outside a set of h of total length below 1.7·10⁻¹¹, the inputs of [[thm:uc-integer]] that depend on
h enter its proof as at the computational point, except the roots of real part below 3 of the damping polynomials,
through which the gap of (G) and the count N_Λ of [[lem:uc-lambda]] move with h; at the admissible points among these at
which the degrees l with hl(l + 2) > 70 have no root of real part in [2, 3 + ε_Υ), a condition decided only at h = 10⁻⁶,
the bounds of [[prop:uc-dependence]] hold with the gap and the count at h ([[thm:tr-transfer]]).
```

Texts 4 and 6 are given under m5 and m7.

---

## nits

1. **rem:tr-scope, lines 90–95.**
   - "elsewhere this paper proves 0 < μ(h) ≤ μ_G and nothing more" contradicts the next clause: prop:tr-mu-small
     proves an upper bound for μ(h) on (h_μ, 10⁻⁶].
   - "The count N̄(h) is explicit" overstates. N̄(h) is defined from Z₃(h), whose elements are enclosed only at
     h = 10⁻⁶; what is explicit is its bound.
   - Replace lines 90–95, which also carry m4's change at line 94, by:

   ```
   enclosed to within 10⁻²¹ ([[lem:is-z3]], [[lem:is-gap-z]]); elsewhere this paper proves only 0 < μ(h) ≤ μ_G and, on (h_μ,
   10⁻⁶], an upper bound for μ(h) that tends to 0 at h_μ, so that μ(h) has no positive lower bound there
   ([[prop:tr-mu-small]]). The count N̄(h) is bounded explicitly, and the bound of [[prop:uc-dependence]] is at least of the
   order N̄(h)²/ε_K; the bound of (iii) for N̄(h) is below 1.512·10¹⁵ at h = 10⁻⁶ and below 1.477·10¹⁷ at h = h_m, while the
   enclosures of [[lem:is-z3]] give N̄(10⁻⁶) ≤ 909,507,124,095,312. The restrictions h ≥ h_m and h ∉ 𝖩 are those under which
   (a)–(d) carry over in the form the proof uses at h = 10⁻⁶, and besides (R_h) the proof uses no other property of h than
   h < 10⁻⁶; admissibility is what makes the numbers bounds for the loss with
   ```

2. **Optional: Z₃(h) is finite at every h.**
   - prop:np-10-54 (iii) gives this at every h ∈ (0, 10⁻⁶]. Then μ(h) is a positive minimum at every h, and the
     parenthesis "(Z₃(h) finite)" on line 502 always holds.
   - This makes the bound of (ii) a number at every admissible h. It is not needed for correctness: if μ(h) were 0, no
     ε_K would satisfy (G).
   - Optionally add after the display: "Z₃(h) is finite at every such h ([[prop:np-10-54]] (iii)), so μ(h) is a positive
     minimum."

3. **Optional.** In (iii), min(μ(h), 10⁻¹³) = μ(h), since μ(h) ≤ μ_G < 1.65·10⁻¹⁴. The 10⁻¹³ can go.

4. **lem:tr-large (c), lines 330–335.**
   - Only 10⁻⁶ is said to be replaced by 3ex̄/(2b²). The F₃ term needs its square in place of 10⁻¹². With 10⁻¹² kept,
     the ϖ̄-term of F₃ grows like b⁴, and eΦ(4642) ≈ 41.
   - The printed values 0.0062, 0.1233, 0.0300 and 0.2337 are those with the square (my recomputation below).
   - Replace lines 330–335 by:

   ```
   ϖ̄, and 3ex̄/(2b²) for 10⁻⁶ and its square for 10⁻¹². The result is b²Φ(b), Φ a sum of non-negative multiples of b, 1,
   b⁻¹, b⁻², …, so Φ is convex on (0, ∞); and |U| ≥ 2ϱ(b − ϱ)(2b − ϱ) ≥ 2ϱ(1 − ϱ/56)(2 − ϱ/56)b². For x̄ = 20, eΦ is below
   0.0062 at b = 56 and below 0.1233 at b = 2481, against 2ϱ(1 − ϱ/56)(2 − ϱ/56) > 0.1997; for x̄ = 70, below 0.0300 at
   b = 56 and below 0.2337 at b = 4642, against more than 0.7957. So e|F| < |U| on |ι − ζ| = ϱ, and the root of the disc of
   radius b/10 lies in the smaller disc. Finally |ι_P − 1| ≥ Im ι_P > b − r, which exceeds 50 if b > 50.2 (r ≤ 1/5 for
   b ≤ 56, r = b/10 for b ≥ 56).
   ```

5. **First reading's nit 11, not applied (lines 362–365).**
   - The printed A values are upper bounds only with the factor 1/x of 10⁻⁶F̄^ϖ/x taken at the left end.
   - Replace lines 362–365 by:

   ```
   (𝒬 − A)/(𝒬 + B). On the intervals [0.98, 2], [2, 5], [5, 10], [10, 20], [20, 35], [35, 49.02], evaluating 𝒬 from below at
   the left end, and A, B from above with the majorants at the right end and the factor 1/x of 10⁻⁶F̄^ϖ/x at the left end,
   gives 𝒬 ≥ 25.76, 52.56, 131.4, 262.7, 525.6, 919.9, A ≤ 0.04152, 0.1004, 0.2386, 0.8528, 2.878, 5.997 and B ≤ 0.02129,
   0.06983, 0.231, 0.9253, 3.46, 8.242, so the quotient is at least 0.9975, 0.9967, 0.9964, 0.9932, 0.988, 0.9846.
   ```

6. **prop:tr-lambda proof (a), line 565.**
   - "has real part above 3 + ε_Υ" should read "at least 3 + ε_Υ": lem:tr-z3 (a) excludes only [3, 3 + ε_Υ).
   - Replace lines 565–567 by:

   ```
   real part at least 3 has real part at least 3 + ε_Υ > 3 + ε_+, and so has every sum with it; one of real part below 3 has
   real part above 2 + 1.4646·10⁻¹⁰, so that an increment of real part at least 1 takes it above 3 + ε_+. A non-real element
   of Λ ∖ Λ_ℬ below 3 + ε_+ is ι + p𝔡₀ + q𝔡₁ with ι ∈ Z₃(h) non-real, of real part above 2.1 by [[lem:tr-z3]] (a).
   ```

7. **Placement preamble and items 1, 3 and 8 are stale.** P-UB1 and P-UB2 are merged and retired, and every item now
   has the single base HEAD.
   - Replace lines 700–707 by:

   ```
   Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
   source, with the chapter's indentation, each preceded by a line ending "Old:" or "New:". All items are given against
   the chapters at HEAD edafc288, where chapter 71 carries the merged texts of P-I11, P-UB1 and P-UB2. Each old text
   occurs exactly once in its chapter in the form stated, and line numbers, which serve only to find the place, are those
   of that form.
   ```

   - In item 1: "(line 5496 of chapter 71 after P-UB1 and P-UB2)" → "(line 5499 of chapter 71)". Also "and the results of
     P-UB1 and P-UB2 named above, which stand earlier in the chapter" → "and [[lem:is-z3]], [[lem:is-gap-z]],
     [[cor:is-lower]], [[prop:is-lambda]], [[thm:is-gap]] and [[prop:is-count]], which stand earlier in the chapter".
   - In items 2–4: drop " after P-UB1 and P-UB2".
   - In item 3: drop the sentence "P-UB1 and P-UB2 leave these lines as they are at 8d583306."
   - In item 4: "The old text is that of P-UB2." → "The old text is the chapter's."
   - In item 8: "(line 5488 of chapter 71 after P-UB1 and P-UB2)" → "(line 5491 of chapter 71)", and drop "P-UB1 and P-UB2
     leave these lines as they are at 8d583306."
   - In items 5–7: "at 8d583306" → "at HEAD". The lines are 364, 81 and 4535–4537 there.
   - Crosswalk row 1: drop ", after the texts of P-UB1 and P-UB2".

8. **Crosswalk notes.**
   - Row 27: "d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)², above 7.57245·10⁵⁵ when ε_ind(h) < 1.99·10⁻²⁸" → "if
     ε_ind(h) < 1.99·10⁻²⁸, d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)² > 7.5755·10⁵⁵". This matches m1 and the text's number.
   - Rows 4 and 28: see m6 and m5.
   - After the edits, re-pin every PENDING:N.

9. **Optional (J2).**
   - In the proof of (iii), "the proof of [[lem:cs-fourier]] (b) uses ε_ind > ε_K and the reality …" could add "and
     𝒵 ⊂ {Re > 1}, which holds at every h ([[prop:iii-f1-2-3]] (a))".
   - J2 at HEAD makes this an input of that proof. It is h-independent.

---

## What I checked and found correct

**thm:tr-transfer (ii).**
- Z₃(h) ⊂ Z(h) has real parts in (2, 3), by prop:np-10-54 (ii). So ι − 1 is an indicial root of real part in (1, 2),
  and it is not removed by D. The roots of D at s0, s1 and v1 are h-independent (proof of prop:iii-f1-2-3).
- Hence ι + p𝔡₀ + q𝔡₁ ∈ Λ, with 𝔡₀ and 𝔡₁ gauge increments (prop:is-ind).
- m(y) of lem:is-reduction is defined for every y > 0 and is a positive minimum, since the p𝔡₀ + q𝔡₁ form a discrete
  set. So (G) gives ε_K < m(y_ι) and ε_K < μ_G, and ε_K ≤ μ(h).
- prop:ec-rounds uses only ε_g ≤ ε_Υ < δ̂ and η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄, which hold at every admissible h.
- The numbers:
  - 3ε_K + 2δ̂ + δ̄ ≤ 1.97062·10⁻⁸ < 1.98·10⁻⁸;
  - 3(1 − 1.98·10⁻⁸)/δ̂ = 2.0517870·10¹⁰ > 2.0517·10¹⁰;
  - 21 × 2.0517·10¹⁰ = 4.30857·10¹¹;
  - 2.0517·10¹⁰/1.64160217198·10⁻¹⁴ = 1.2498156·10²⁴;
  - 4.3085·10¹¹/1.64160217198·10⁻¹⁴ = 2.6245701·10²⁵.
- At h = 10⁻⁶: μ(10⁻⁶) = μ_Z, as μ_Z < μ_G and every other m(y_ι) ≥ 1.1076·10⁻¹⁵ (lem:is-gap-z). Also
  2.0517·10¹⁰/μ_Z > 1.22505·10²⁷ and 4.3085·10¹¹/μ_Z > 2.57256·10²⁸, the bounds of cor:is-lower.

**thm:tr-transfer (iii).**
- prop:uc-dependence at HEAD has exactly the hypotheses the proof supplies.
- I_base = 935R_b + 466 + 23,524,832(R_b + 3) depends on ε_K but not on N̄_Λ, so N₁ is well defined.
- 4 × 765,000,816 = 3,060,003,264 and 22,119 − 36 = 22,083, so N̄_Λ ≥ N₁ gives 4k̄_max + 24 > I_base + 22,119, with
  k̄_max = 3 + J′N̄_Λ.
- lem:uc-admissible's steps carry over:
  - α can be chosen in [4 + 0.999ε_K, 4 + ε_K] whatever ε′_0 is;
  - Λ ∩ {Re ≤ 4} is finite;
  - (Ex2) and (H4) are h-independent.
- "at least of the order N̄(h)²/ε_K" in rem:tr-scope is prop:uc-dependence's last sentence.

**lem:tr-z3.**
- Every case of (a) is right.
- The count is 1 + 2 + 3·141 = 426.
- y_ι is bounded by 1 − x/2, by 1.01 − x, and by (3/4)(11/15 − x), where a − 1/20 = 3 + 3(x − 11/15)/4.
- g_B and g_P are non-increasing. The integral comparison holds, and so does the count bound (c/h)^(1/2), as
  √(X + 1) − 1 < √X.
- The integrals, by mpmath and in closed form:
  - ½∫g_Bx^(−1/2) = 0.62624564 < 0.626246;
  - ½∫g_Px^(−1/2) = (3/10)(11/15)^(5/2) = 0.13815761 < 0.138158;
  - 0.62624564 + 2·0.13815761 = 0.90256086 < 0.90257;
  - √1.01 + 2√(11/15) = 2.71768524 < 2.7177.

**prop:tr-lambda.**
- (a): Λ_ℬ is unchanged, because the increments below 3/2 come from ℰ_ind only (prop:tr-inputs (a)). 1 + 𝒵 =
  {3} ∪ {ι ∈ Z(h) : Re ι < 4} by prop:iii-f1-2-3 under (C1).
- (b): the windows behave as in thm:is-gap, as ε_K < μ_G < 1.4646·10⁻¹⁰.
- (c): the numbers:
  - 2ν₀ + ν₀² = 3.3800029·10⁻⁶ < 3.39·10⁻⁶;
  - 426 + 426·3.39·10⁻⁶ = 426.00144 < 426.0015;
  - 0.90257 + 2.7177·3.39·10⁻⁶ = 0.9025792 < 0.90258;
  - 1.67472·10¹³ + 1,125,001,468,750.5·426.0015 = 4.9599951·10¹⁴ < 4.961·10¹⁴;
  - 1,125,001,468,750.5·0.90258 = 1.0154038·10¹² < 1.0155·10¹².
- So (G) holds iff ε_K < μ(h), and (G⁺) holds iff ε_+ < μ(h).
- The bound of rem:tr-scope is 1.5116·10¹⁵ < 1.512·10¹⁵ at h = 10⁻⁶ and 1.476855·10¹⁷ < 1.477·10¹⁷ at h_m.
- N̄(10⁻⁶) ≤ ⌊16,747,200,000,000 + 892,759,924,095,312.22⌋ = 909,507,124,095,312.

**prop:tr-mu-small.**
- κ = 152880, y = 1.49297 > 1.49, x ≤ 0.15288. At 5·10⁻⁷, x = 0.07644 and ι_B < 2 + 3x/2 = 2.11466, while
  w_* < 0.847129468486787284131724 < 0.84713, so the sum is below 2.9618 < 3.
- |ι_* − 2.15288| = 9.5·10⁻⁶ < 1/100, so ι_* = ι_B(390, 10⁻⁶).
- ι_B(390, ·) is continuous. It is the simple root in a disc whose centre moves continuously, a polynomial root in
  (ι, h).
- The intermediate-value argument is correct:
  - f(h) := ι_B(390, h) + w_* − 3 is continuous and real on [5·10⁻⁷, 10⁻⁶], with f(5·10⁻⁷) < 0 < f(10⁻⁶) = μ_Z.
  - {f ≤ 0} is closed and non-empty, and its supremum h_μ has f(h_μ) ≤ 0.
  - If f(h_μ) < 0, then f < 0 just to the right of h_μ, which contradicts maximality. So f(h_μ) = 0, and
    h_μ ∈ (5·10⁻⁷, 10⁻⁶).
  - f > 0 on (h_μ, 10⁻⁶].
- For such h, ι_B ∈ Z₃(h), and m(y_ι) ≤ f(h) with (p, q) = (356327, 1116082). The conclusion follows from (ii).
- As a sanity check by 60-digit root-finding (no claim rests on it): P_390's root at 10⁻⁶ agrees with r_*; my
  𝒫_390 = 64·10¹⁸P_390 equals the integer polynomial of lem:is-gap-z; and f(10⁻⁶ − 10⁻¹²) < 0, so h_μ lies within about
  10⁻²² of 10⁻⁶. This is consistent with the statement, which claims only h_μ ∈ (5·10⁻⁷, 10⁻⁶).

**lem:tr-large (c), b ≥ 56 and h ≥ h_m.**
- √(105e/h_m) = 4641.32 < 4642 and √(30e/h_m) = 2480.89 < 2481.
- Φ is a sum of non-negative multiples of b, 1, b⁻¹, …, hence convex.
- The endpoint values, by exact rationals from my own majorants (A_j, F₂ and F₃ with ϖ̄ = 3x̄/(2b²), h̄ = eϖ̄, h̄²,
  ā = (3x̄ + 10)/4):

  | x̄ | b | eΦ | printed |
  |---|---|---|---|
  | 20 | 56 | 0.0061161 | < 0.0062 |
  | 20 | 2481 | 0.1232506 | < 0.1233 |
  | 70 | 56 | 0.0299866 | < 0.0300 |
  | 70 | 4642 | 0.2336818 | < 0.2337 |

- A 400-point grid confirms that the maximum is at the endpoints.
- 2ϱ(1 − ϱ/56)(2 − ϱ/56) = 0.199732 for ϱ = 1/20 and 0.795719 for ϱ = 1/5.
- The ϱ-disc lies inside the b/10-disc. The step "b > 50.2 implies |ι_P − 1| > 50" is right.
- I also verified the coefficients A₀–A₄ of eq:tr-aj symbolically.

**lem:tr-slopes (b), b ≥ 56, 1/2 ≤ x ≤ 1.**
- √(1.5e/h_m) = 554.74 < 555.
- The deviation bound, with majorants at (ā + b_b + 1/20, 1), ϖ̄ = 3/(2b_a²) and h̄ = eϖ̄, and 1/x = 2, gives at most
  0.00956, 0.00514, 0.00295 and 0.00083 on the four b-intervals. These are below the printed 0.0138, 0.0073, 0.0041 and
  0.0010.
- 3/4 − 0.2923 > 2/5.

**𝖩, n = 3 clause, and prop:tr-measure.**
- The window for n = 3 is x ∈ (0.59999999981, 0.73333333353) ⊂ (1/2, 0.734). lem:tr-slopes (b) covers it for every b,
  and lem:tr-large (c) gives the ϱ-disc for every b when h ≥ h_m.
- The least l is 1000√0.3999 − 1 = 631.38.
- The sums:
  - Σ(4n/3 − 3.6001)^(−1/2) = 12.1096 ≤ 12.6702 < 12.671;
  - Σ(n − 2.0101)^(−1/2) = 12.6228 ≤ 13.0138 < 13.014;
  - Σ(n − 3)^(−1/2) = 12.4681 ≤ 12.8564 < 12.857.
- The factors are 1.001006, 1.001584 and 1.001001 (·10⁻³). The coefficients are 0.0265884, 0.0634564 and 0.0260023.
- 0.1161ε_Υ = 1.69727·10⁻¹¹ < 1.698·10⁻¹¹, and 1.698·10⁻¹¹/(10⁻⁶ − h_m) = 1.69808·10⁻⁵ < 1.7·10⁻⁵.

**h_m and prop:tr-fail.**
- (40/13)h_m(1 − 5·10⁴h_m) = 1.4646119·10⁻¹⁰ > 1.4646·10⁻¹⁰ > ε_Υ, and 3.1h_m = 1.4756·10⁻¹⁰.
- 13ε_Υ/40 = 4.751175·10⁻¹¹ exactly, and h_m/(13ε_Υ/40) = 1.0018574, within 0.19 %.
- h_c = 9.9801196…·10⁻⁷.
- 1.986·10⁻³⁴ × 1002001 = 1.98997·10⁻²⁸ < 1.99·10⁻²⁸.
- 3(1 − 2.1·10⁻⁸)/(1.99·10⁻²⁸)² = 7.5755661·10⁵⁵ > 7.5755·10⁵⁵ > D_NM > D_acc.
- √(0.3168/7.57245·10⁵⁵) = 6.4681·10⁻²⁹, as the remark after prop:tr-mu-small states.

**Overclaim pass.** I read every sentence of the section and of texts 2–8 against the proofs. Besides m4–m8 and nits 1
and 4:
- rem:tr-scope's three conditions are each stated correctly. In particular, the undecided conditions are listed by
  rem:ec-point-outside: (AP1)'s mode stability, (AP4)'s tf-admissibility and (AP3).
- Text 7's claim, that near every integer crossing of a root with |ι − 1| ≤ 50 ε_ind(h) is arbitrarily small, is the
  first reading's accepted wording.
- Text 8's "except at the points of [[thm:tr-transfer]] (iii), if there are any" is accurate.

**Format.**
- In the file and in all replacement texts, lines are at most 121 characters, also after the labels resolve.
- The only lines that start with "+ " or "|" are indented display continuations and the two tables.
- There are no file or program names in chapter text, and all labels are lowercase.

**Method.** My own scripts are in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rptr2/ (num/ for the
numbers, merge3.py and fix.py for the scratch merges). They use exact rationals from fractions and sympy for every
majorant and inequality, and mpmath at 30–60 digits for the integrals and sums. I did not use the writer's scripts.

Verdict: NOT CONFIRMED

---

## Confirmation (P-TR.md md5 20e494d7c5d171be7b1aa6b1ca3f9880, 920 lines; report F3-P-TR)

Base: HEAD 31ee2458. Its chapters are those of ebc73adf, and the working tree equals HEAD for the chapters and for
P-TR.md. I compared the new file with my P-TR-fixed2.md.

**The body** differs only by the three optional nits:
- the first line of (iii);
- the display and the next sentence of def:tr-excess;
- the proof of (iii), lines 601–621, which is rewrapped because of the two added clauses.

Every text of m1–m8 and of nits 1 and 4–6 is mine, word for word.

**The placement and crosswalk part** follows nit 7:
- the preamble is against HEAD;
- items 1 and 8 cite 5499 and 5491;
- item 1 names its sources, now including [[prop:np-10-54]] and [[prop:uc-dependence]];
- the notes about proof files are gone.

The crosswalk follows nit 8:
- rows 1, 4, 27 and 28 carry the new notes;
- all 28 pins are re-pinned, and each matches the line of its label, in order.

**The three optional changes.**
- **def:tr-excess.** "Z₃(h) is finite at every such h ([[prop:np-10-54]] (iii)), so μ(h) is a positive minimum and N̄(h)
  is defined."
  - prop:np-10-54 (iii) says that, for every h ∈ (0, 10⁻⁶] and every R > 0, only finitely many l have a root of P_l or
    p_(v) in {|Re ι| ≤ R}. So only finitely many roots lie in that strip.
  - Z₃(h) ⊂ {2 < Re ι < 3}, and the root of C is a root of P_0, so Z₃(h) is finite.
  - Each m(y) is a positive minimum, being the infimum of a discrete set of positive numbers p𝔡₀ + q𝔡₁ − y. So μ(h) is
    a positive minimum at every h, and N̄(h) is a finite sum.
  - Dropping "(Z₃(h) finite)" from the display is right.
- **(iii).** "0 < ε_K < ε_+ < μ(h)" replaces "< min(μ(h), 10⁻¹³)", and the proof's chain reads
  0 < ε_K < ε_+ < μ(h) ≤ μ_G < ε_Υ ≤ ε_ind. Link by link:
  - μ(h) ≤ μ_G holds at every h, since μ_G is in the set of which μ(h) is the infimum.
  - μ_G < 1.64160217198·10⁻¹⁴ < 1.4619·10⁻¹⁰ = ε_Υ, by eq:is-mu.
  - ε_Υ ≤ ε_ind := min(1, ε_ind(h)) needs h ∈ [h_m, 10⁻⁶] ∖ 𝖩 (prop:tr-eps (a)). That is the hypothesis of the theorem.
    At admissible h outside that set it can fail (prop:tr-eps (b)), but the chain is used only in (iii), under that
    hypothesis.
  - ε_+ < μ_G < 10⁻¹³, which is what prop:tr-lambda and prop:uc-dependence ask.
  - ε_K < ε_+ < ε_ind and δ_♯ = 0.0099 meet the constants of eq:iii-i9-1-1.
- **𝒵 ⊂ {Re > 1}, at every h ([[prop:iii-f1-2-3]] (a)).** prop:iii-f1-2-3 (a) says, for z ∈ (0, ½] and under (C1), that
  no indicial root of L̂_b(0) has real part in (0, 1].
  - z = 4·10⁻⁶ here.
  - (C1) holds at every h ∈ (0, 10⁻⁶], by lem:iv4-1-3 (a), which the same section cites.
  - So every μ ∈ 𝒵, that is every root with 0 < Re μ < 3, has Re μ > 1.

**Scratch merge** of HEAD + the new P-TR in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rptr2/merged4.

Every old text occurs exactly once at HEAD:

| item | file | line at HEAD |
|---|---|---|
| 1 | 71, heading of sec:ec-linear | 5499 |
| 2 | 71 | 30 |
| 3 | 71 | 85–86 |
| 4 | 71 | 1820–1821 |
| 5 | 03 | 364 |
| 6 | 90 | 81 |
| 7 | 33 | 4535–4537 |
| 8 | 71 | 5491 |

The checks:
- `lint.py --chapters`: 62 files, 4956 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- The in-memory check prints `[] 0`.
- No line exceeds 121 characters after labels resolve; the longest from P-TR is 121.
- sec:tr is Section 49.15, thm:tr-transfer Theorem 49.128 and prop:tr-mu-small Proposition 49.142.

**The file:**
- at most 121 characters per line;
- no wrapped prose line, in the section or in any New block, starts with "+ ", "- ", "* ", "> ", "#", "=" or "|";
- labels are lowercase;
- the chapter text carries no file, program or commit names.

J1–J3 still touch no P-TR text, and the J2 input is now named in the proof of (iii).

All findings of the second reading (m1–m8, nits 1–9) are resolved, and the resolutions are right. Nothing new is open.

Verdict: CONFIRMED
