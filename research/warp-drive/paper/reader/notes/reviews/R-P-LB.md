# Review of proofs/P-LB.md (md5 c2b4ef1da757cd54c18364b535c839e2)

Verdict: NOT CONFIRMED. 0 Major, 5 minor, 10 nits. The mathematics is correct. Every proof step traces to a statement
that holds at every point of the proved set, and every number recomputes exactly. The minor findings are four
misstatements in the text (the direction of the bound for δ, "γ_C tends to 0", a general-z sentence inside a section that
fixes z = 4·10⁻⁶, and the reuse of the chapter's fixed symbol δ̄) and one missing placement in chapter 33.

Line numbers are those of P-LB.md unless a chapter is named. Chapter line numbers are those of the tree at 003371f6.

## Minor

**m1. Line 5 (section opening): δ gets an upper bound, not a lower bound.**
Current text (lines 4–5): "This section proves a lower bound for d_acc, and so for / d_NM, N_NM and δ, at every
point of that set, as an explicit function of the gauge parameter z = 4e_Υγ_Υ² and of".
What is wrong: [[cor:ec-lb-delta]] bounds log₁₀ δ from above. The sentence says it bounds δ from below.
Replacement for line 5 only (117 characters; line 6 is unchanged):

    d_NM and N_NM, and an upper bound for δ, at every point of that set, in terms of the gauge parameter z = 4e_Υγ_Υ² and

Line 6 continues "h = γ_C⁻¹, γ_C being the damping parameter. ...", which still reads correctly.

**m2. Line 371 (Placement text 6, rem:ec-not-evaluated): "as they tend to 0" is wrong for γ_C.**
Current text: "of the gauge and damping parameters, and it tends to infinity as they tend to 0, so that no upper bound for d holds
on / all of that set ([[rem:ec-lb-unbounded]]). Among the inputs".
What is wrong: the bound grows as z → 0 or as γ_C → ∞ (h → 0). The damping parameter γ_C is above 10⁶ and never tends
to 0. Text 10 (line 442) gets this right: "as z or γ_C⁻¹ tends to 0".
Replacement for lines 371–372 (still two lines, 114 and 80 characters; text 6 stays six lines):

    of the gauge and damping parameters, and it tends to infinity as z tends to 0 or γ_C to infinity, so that no upper
    bound for d holds on all of that set ([[rem:ec-lb-unbounded]]). Among the inputs

**m3. Lines 346–348 (Placement text 4): a general-z statement inside a section that fixes z = 4·10⁻⁶.**
Current text: "bound rises to 3R > 1.2497 × 10²⁴ ([[cor:uc-two-offsets]]). At every point of the set on which [[thm:settling]]
is / proved, d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²), an explicit function of the gauge and damping
parameters / ([[thm:ec-lb-proved]]). The bound (iii) is explicit in the numbers of steps, which".
What is wrong: the paragraph after [[thm:loss-d]] lies in [[sec:ec-gauge-gap]]. Chapter 71 line 1314 fixes the
convention for that section: "Throughout, z = 4·10⁻⁶". Read under that convention, the sentence says
d_acc > 3(1 − 2·10⁻⁵)g(4·10⁻⁶)⁻² at every point of the proved set, which is not proved at points with larger z. Also, g
is used here before its definition in [[eq:ec-lb-g]], which comes in a later section, and the text gives no reference to
it. (Text 2 defines g inline, so it has no such problem.)
Replacement for lines 346–348, four lines (116 characters or fewer; text 4 becomes "the six lines"):

    bound rises to 3R > 1.2497 × 10²⁴ ([[cor:uc-two-offsets]]). At every point of the set on which [[thm:settling]] is
    proved, d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²), where z = 4e_Υγ_Υ² is that point's gauge parameter, not
    4·10⁻⁶, and g is the function of [[eq:ec-lb-g]] ([[thm:ec-lb-proved]]). The bound (iii) is explicit in the numbers of
    steps, which

Line 342 then reads "New, the six lines:".

**m4. Lines 125, 169, 189–190: δ̄ already has a fixed meaning throughout chapter 71.**
Current text: line 125 "Let δ̂ > 0 and δ̄ > 0 with"; line 169 "δ̂ := min(g(z), 40h/13)."; lines 189–190 "Put / δ̄ :=
40h/13."
What is wrong: [[def:ec-point]] (chapter 71 line 47) fixes the notation for the whole chapter: "We write δ̄ :=
1.94137057·10⁻⁸, so that δ_50 < δ̄". The chapter uses this δ̄ after the insertion point at lines 2091, 2506, 2560, 2930,
3037 ("every ε_+ ∈ (0, δ̄)") and 3786. [[prop:ec-rounds]] gives δ̂ the value 1.46214·10⁻¹⁰, and lines 2091 and 2506 use
that value. The new section rebinds both symbols without saying so; thm:ec-lb-proved even redefines δ̄ := 40h/13 in a
proof. Lemma-local variables are standard, but a reader of lines 3037 or 3786 cannot tell which δ̄ is meant without
checking the scope. The least invasive repair is to say so once, at the end of the opening paragraph.
Replacement for line 10, two lines (117 and 109 characters):

    proof uses. Throughout, (v_C, e_C) = (1/2, 1/102400) as in [[eq:iv4-0-1]], and e := e_C; and δ̂, δ̄ denote the bounds
    of [[lem:ec-lb-rounds]] and [[thm:ec-lb-proved]], not the numbers of [[prop:ec-rounds]] and [[def:ec-point]].

(Renaming them, say δ_g and δ_C in lem:ec-lb-rounds and thm:ec-lb-proved, would also work, but it touches about 25 lines.)

**m5. A missing placement: chapter 33, [[rem:s14-eps-ind-scope]], becomes false. Line 451 (item 11) claims otherwise.**
Current text, chapter 33 lines 3534–3535 (this text occurs exactly once):

    every constant, and this paper does not determine ε_ind(h) for h ∈ 𝖧 beyond 0 < ε_ind(h) ≤ δ_50.
    [[cor:s14-eps-ind-point]] shows that this upper bound is attained at the end h = 10⁻⁶ of the interval on which ε_ind is

What is wrong: [[lem:ec-lb-ind]] proves ε_ind(h) < 40h/13 for every h ∈ (0, 10⁻⁶]. That is smaller than δ_50 for
h ≤ 6.309·10⁻⁹, as [[rem:ec-lb-ind]] itself notes. So once P-LB is merged, "this paper does not determine ε_ind(h) for
h ∈ 𝖧 beyond 0 < ε_ind(h) ≤ δ_50" is false. Line 451 says "every statement of [[ch:s14]] keep their texts". (The
sentence of [[rem:ec-point-outside]] that P-LB keeps, "For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50", is still
true.)
Proposed new placement item, "*12. [[ch:s14]], [[rem:s14-eps-ind-scope]] (lines 3534–3535).* Old, the two lines:" as
above, and "New, the three lines:" (109, 117 and 86 characters; after resolution at most 109):

    every constant, and this paper does not determine ε_ind(h) for h ∈ 𝖧 beyond 0 < ε_ind(h) ≤ δ_50 and the bound
    ε_ind(h) < 40h/13 of [[lem:ec-lb-ind]], which is the smaller for h ≤ 6.309·10⁻⁹. [[cor:s14-eps-ind-point]] shows that
    the upper bound δ_50 is attained at the end h = 10⁻⁶ of the interval on which ε_ind is

The next line, "defined.", is unchanged. ("this upper bound" becomes "the upper bound δ_50", because two upper bounds are
now named.) Item 11, line 451: replace "and / every statement of [[ch:s14]] keep their texts" with "and every statement of
[[ch:s14]] except [[rem:s14-eps-ind-scope]] (text 12) keep their texts". The crosswalk of [[ch:s14]] then needs a note on
row rem:s14-eps-ind-scope: "cites lem:ec-lb-ind for ε_ind(h) < 40h/13 (P-LB text 12)". Chapter 33 has changed recently,
so the old text should be re-checked at merge. I checked it at 003371f6.

## Nits

**n1. Lines 92–93: the justification of the majorants.** Current text: "For 0 ≤ ξ ≤ 40/13 and 0 < e < 10⁻⁵, each p_j is
bounded by the sum of the moduli of its / terms, taken at ξ = 40/13 and e = 10⁻⁵:". As a function of e, the sum of the
moduli does not increase. For p₃–p₇ it is larger at e = 0 than at e = 10⁻⁵: for p₃ it is 1635.5394 at e = 0 against
1635.5346 at e = 10⁻⁵. The printed bounds still hold at the worst e in [0, 10⁻⁵]: 1635.54, 2645.10, 2855.08, 4141.03,
2358.03, 1654.76, 848.59. Replacement for line 93 (line 92 unchanged):

    terms, each coefficient taken at its largest modulus for 0 ≤ e ≤ 10⁻⁵ and each power of ξ at ξ = 40/13:

**n2. Lines 319–320 (text 3): "𝖧 is open at h_*" is not standard.** Read literally, "open at h_*" says that h_* is an
interior point, the opposite of what is meant. Replacement for line 320 (112 characters; line 319 still ends "and 𝖧"):

    ⊂ (0, h_*); so h = 10⁻⁶ is not in 𝖧 ([[rem:s14-eps-ind-scope]]). Whether the gauge half of the point lies in the

**n3. Lines 322–323 (text 3): "is not decided" twice in one sentence.** Replacement for line 322 (120 characters; line
323 begins "[[def:ec-point]] does not fix …" and is otherwise unchanged):

    existence is proved and whose values are not determined, and (γ_Υ, e_Υ) = (1/100, 1/100) is not shown to lie below them.

with "not decided. " deleted from the start of line 323.

**n4. Line 224: v also enters.** "through e in P_2". The expansion [[eq:s14-f-two]] is taken at v = 1/2. Replacement:
"- (v_C, e_C) = (1/2, 1/102400) (row c1 of [[sec:vi-c-1]]), through v = 1/2 and e in P_2 and [[eq:s14-f-two]];"
(109 characters).

**n5. Lines 221–232: "uses exactly the following conditions", yet (C4) is missing from the list.** The existence of
ε_ind comes from (C4) ([[prop:iii-f1-2-3]] (f)), and only the next paragraph says so. Add after line 227: "- (C4)
(row c3), only through the existence of the constant ε_ind ([[prop:iii-f1-2-3]] (f));" (92 characters).

**n6. Line 237: the row groups are mixed up.** "the data classes, the parameter set ℬ_* or the smallness of rows d1–d2, b1–b4
and n1". Rows d1–d2 and b1–b4 are not smallness conditions. Replacement for line 237: "classes (rows d1–d2), the
parameter set ℬ_* (rows b1–b4) or the smallness of row n1. So the bound" (97 characters).

**n7. Lines 240–241: "which is the bound of [[thm:loss-d]] (ii)".** 1.4032·10²⁰ is slightly stronger than the printed 1.403 × 10²⁰,
so it implies that bound. Replacement: "conditions listed. At the computational point it gives d_acc > 3(1 −
2·10⁻⁵)g(4·10⁻⁶)⁻² > 1.4032·10²⁰, which implies / the bound 1.403 × 10²⁰ of [[thm:loss-d]] (ii)." (116 and 46
characters).

**n8. Line 449 (item 11): "is the case z = 4·10⁻⁶ of [[thm:ec-lb-proved]]".** [[prop:ec-rounds]]'s last sentence (R > 4.6775·10¹⁹)
follows from the theorem at z = 4·10⁻⁶ (R > (1 − 2·10⁻⁵)/g(4·10⁻⁶)² = 4.6776·10¹⁹), but it is not literally that case:
its δ̄ is 1.94137057·10⁻⁸, not 40h/13. Replacement: "on every h ∈ 𝖧 with the same (γ_Υ, e_Υ), stays true and follows
from [[thm:ec-lb-proved]] at z = 4·10⁻⁶), the statement" (119 characters).

**n9. Line 68: an empty sentence.** "The leading coefficient 1/13680 = 5/171 − 7/240 does not depend on z." It is a constant,
so the sentence says nothing. Suggest deleting it, so that the paragraph ends "… the number δ̂ of [[prop:ec-rounds]]."

**n10. Crosswalk coordination with P-K.** Both proposals append notes to the same existing rows: ch:explicit-constants
in the crosswalk of chapter 71 (P-LB text 2, P-K text 2) and sec:scope-constants in the crosswalk of chapter 90 (P-LB
text 10, P-K text 8). The merge must keep both notes on each row; neither proposal says this.

## Interaction with proofs/P-K.md (md5 6c7eb17393ce45f0f67b0d52cbd36773)

No P-LB old text is the same as, or overlaps, a P-K old text. The pairs that share a chapter:

- Chapter 71: P-LB 16–25, 49–57, 1462–1464, 1512, 4693–4695 and the insertion after line 1527; P-K 26–27 and its
  insertion before [[sec:ec-linear]]. P-LB text 2 and P-K text 2 are adjacent. Merged in either order they read
  correctly: P-K's "at that point K is at most …" still refers to the computational point named in P-LB's last sentence.
- Chapter 03: P-LB 351–357; P-K 311.
- Chapter 90: P-LB 66–67; P-K 72–73 and 130–131. The merged section reads correctly.

Statements in P-K that P-LB makes false or incomplete (they are P-K's to change):

- P-K text 6 (P-K line 377), text 7 (P-K line 391) and the merge note of item 10 (P-K line 420) say "d is bounded only at
  the computational point". After P-LB, d is bounded below at every point of the proved set, so these become false. The
  writer's suggestion "bounded above only at the computational point" is correct. Adding "above" keeps line 377 at 120
  characters, but lines 391 and 420 need rewrapping.
- P-K text 3 (P-K line 346, chapter 03 line 311): "d is not evaluated on the set where [[thm:settling]] is proved". This is still
  true, but it sits about 40 lines above P-LB text 9, which states explicit lower bounds on that set. Suggested: "On the
  set where [[thm:settling]] is proved d is not evaluated and is bounded only from below ([[thm:ec-lb-proved]]); at the …".
- P-K item 10 (P-K line 420) says "[[rem:ec-not-evaluated]] stands", while P-LB text 6 rewrites three of its lines. There is no
  textual conflict, because P-K does not edit that remark, but the note is inaccurate once both are merged.
- P-K [[rem:uc-data-order-limits]] (P-K line 305), "on which d is not evaluated", stays true.

## What I checked and found correct

- **Typography.** Every line of P-LB.md is at most 121 characters. In a trial merge in a scratch copy of the chapters,
  with all nine texts placed and the section inserted, the assembled paper has no line over 121 characters (code points)
  after label resolution. No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The only such lines are
  the two headings and the intended list items at lines 224–231, 413 and 423. All labels are lowercase. In the trial
  merge, lint --chapters gives 0 hits on 62 files with 4609 labels, assemble --check gives 0 problems, and lint --paper
  gives 0 hits. No new label is defined anywhere else. The proof part names no file or program.
- **[[lem:ec-lb-gauge]] (a).** The discriminant of Q_l is (z + 2)² + 4κ = 4(u + w)², s_± = u² + z/2 ± (u + w), and
  1 + 4s_± = (2u ± 1)² + 2z ± 4w. The roots of type sl come from [[eq:s13-dets]] (chapter 32). The labelling of the two
  roots uses [[eq:iii-d-4-2]] (ι^Υ_(sl,l+j) ∈ (l + j, l + j + ¼)), which [[lem:iii-d-4-1]] proves for every z ∈ (0, ½].
- **(b).** w = (z + z²/4)/(√(u² + z + z²/4) + u). [[eq:ec-sqrt]] applies, since y = z + z²/4 ≤ 8u². The identity
  (z + z²/4)2u − z(2u + (z + z²/4)/(2u)) = (z²/(2u))(u² − 1 − z/4) holds, and it is positive for u ≥ 2, z ≤ ½. The ranges
  of y = 2z ∓ 4w lie in [0, 8A²]. Then 2uA = 240, 4u²A³ = 864000 (u = 8, A = 15); 342, 2222316 (u = 9, A = 19);
  (81/8)² = 6561/64; and 6561·21600 = 141717600 < 142228224 = 64·2222316.
- **(c).** 5/171 − 7/240 = 1/13680 exactly. c = 1/1368 + 1/960 + 49/864000 = 30031/16416000, and
  30031·544 = 16336864 < 16416000. The lower bound z/13680 − z²/21600 is positive for z < 21600/13680.
- **(d).** −7 − d₂(7) = 1 − ι^Υ_(s7,8) and −9 − d₁(8) = 1 − ι^Υ_(s8,10) are roots with |Re| ≤ 10. The roots 8 + d₂(7)
  and 10 + d₁(8) would not serve, since the second has |Re| > 10. The shifts −d₂(7), −d₁(8) lie in ℳ of
  [[sec:iii-d2-1]], which says the roots do not depend on b or on the horizon modification. g(z) = z/27360 + z²/1088.
- **(a)–(d) on the whole range.** Every step is an analytic inequality valid on all of (0, ½]. As a cross-check,
  mpmath at 200 digits verified (b), (c) and the w-bounds on 2,000 grid points of (0, ½] and at z = 10⁻¹, …, 10⁻²⁹, with
  no failure. At z = 4·10⁻⁶: 2.9239692·10⁻¹⁰ < d₁(8) − d₂(7) = 2.9242581·10⁻¹⁰ < 2.9242707·10⁻¹⁰, consistent with
  [[eq:ec-gauge-gap]]. g(4·10⁻⁶) = 1.4621354·10⁻¹⁰ < 1.46214·10⁻¹⁰.
- **[[lem:ec-lb-ind]], the expansion.** The f_j of [[eq:s14-f-two]] agree identically with det(hN_2) of [[eq:s14-nl]]
  at v = 1/2 for general (κ, e, h), checked symbolically. With w = hξ and κ = 8, the nine p_j agree identically with
  P-LB lines 85–88. f₀ and f₁ at κ = 8 are as printed.
- **The majorants and the tail.** At ξ = 40/13 the majorants are 1635.5, 2645.1, 2855.1, 4141.0, 2358.0, 1654.8 and 848.6,
  all below the printed bounds for every e ∈ [0, 10⁻⁵] (but see n1). The tail is 0.001636 < 0.0017 for h ≤ 10⁻⁶. Each
  term |c|ξ^k increases in ξ ≥ 0.
- **The two signs.** p₂(40/13) = −(9280 + 59920e)/169 = −11879149/216320 = −54.9147. p₂(38/13) = −(9306 + 57346e)/169 =
  −476495873/8652800 = −55.0684. p₂′ ≥ 152/13 − 11 − 159e = 0.69075 > 0.69. 13ξ₋ − 40 = −2·10⁶h, hp₁(ξ₋) = 6·10⁶eh² =
  (1875/32)h², and ξ₋ ≥ 38/13 for h ≤ 10⁻⁶. The lower margin is 1875/32 − 55.07 − 0.0017 = 3.522 > 3.5. The signs hold
  for every h in (0, 10⁻⁶] by these estimates. As a cross-check, P_2/h² at the two ends at 200 values of h from 10⁻⁶ to
  10⁻²⁰ gave −54.9147 and +3.525…3.679, with no failure. (ι₂ − 2)/h is 2.932350 at h = 10⁻⁶ and tends to 40/13.
- **The consequences.** ι₂(h) − 1 is an entry of ℛ^sc_2 ([[sec:s14-simple]]). The roots of □^C_b of scalar type 2 are
  those of P_2 ([[lem:iv4-1-3]] and its proof). (C1) is chapter 34 line 285, which [[lem:iv4-1-3]] (a) gives at every
  h ∈ (0, 10⁻⁶] with C_0 = 100. ι₂(h) is then one of the ι^C_(s2,+,j). [[prop:iii-f1-2-3]] lists ι^C_(sl,+,j) − 1 among
  the roots of L_b^(0), and D removes nothing at l ≥ 2. [[eq:iii-f1-2-2]] gives ε_ind ≤ ι₂(h) − 2.
- **[[rem:ec-lb-ind]].** (38/13, 40/13) ⊃ (2.93, 2.94). [[lem:s14-sextic-small]] (b) puts the three roots of P_2 with
  |ι| < 1000 in three disjoint intervals, the other two above 2 + 8h, so ι₂(10⁻⁶) is the root it locates.
  (40/13)·6.309·10⁻⁹ = 1.941231·10⁻⁸ < δ_50, and the crossover is at h = 6.30945·10⁻⁹.
- **[[lem:ec-lb-rounds]].** It reproduces the proof of [[prop:ec-rounds]] line by line with δ̂ and δ̄ abstract. The
  uses of ε_g ≤ δ̂, ε_K < δ̂, ε_K < δ̄ and η_2 < δ̄ are exactly where stated. [[lem:ec-level-sum]] applies with
  c = ε_K: g_1, g_2 are non-decreasing and 1-Lipschitz, b_1 < 2 + 2δ̂, b_m > 3 − ε_K, c_1 < 3 + δ̄, c_p > 4 − ε_K, and
  both spans are below 1. Both integrals are correct, and (1 − a)²/2 > ½ − a. The monotonicity in ε_K on (0, δ̂] needs
  1 − 2δ̂ − δ̄ > 0, which holds. Admissible α ≥ 3 satisfies α > 4 + ε_K/2 > 4 ([[def:iii-i10-1-3]], with
  ε′_0 ≤ ε_K/2), so α ∈ (4, 4 + ε_K].
- **[[thm:ec-lb-proved]], the hypotheses.** Rows c1, c2, c3, u5, w1 and w2 of [[sec:vi-c-1]] say what P-LB says they
  say. ε_K < ε_+ < ε_ind ([[eq:iii-i9-1-1]]) and ε_K < ε_Υ ([[def:iii-i10-1-3]]) hold, and η_2 ∈ (ε_K, ε_+)
  ([[sec:iii-i11-1]], chapter 41). ε_g = min(ε_Υ, ε_ind) ([[def:s21-eps-g]]), with ε_ind the constant of
  [[eq:iii-f1-2-2]]. No hypothesis used holds only at the computational point. h < h_* ≤ 10⁻⁶ comes from
  [[eq:iv4-0-1]], and z ∈ (0, ½] from row u5.
- **The loss step.** It is point-free: [[lem:ec-round-loss]] (a) holds in the accounting at every point,
  [[lem:ec-closed-forms]] (d) needs only β_sctf < 3/2 and ϑ_in ≥ 0, and [[lem:ec-theta-in]] (b) gives ϑ_in ≥ 0 for L_b
  at every value of the parameters. d_NM ≥ d_acc and N_NM = 21d_NM + 6 come from [[thm:loss-d]].
- **The constants.** 27360/1088 = 25.1471 < 25.15. 3·27360² = 2245708800, and with the factor (1 − 2·10⁻⁵) it is
  2.2456639·10⁹. 3(13/40)²(1 − 2·10⁻⁵) = 0.3168687. Times 21 these are 4.715894·10¹⁰ and 6.65424. 2.24566·10⁹/16 =
  1.40354·10⁸, and 25.15·4 = 100.6. 6δ̄ ≤ (240/13)·10⁻⁶ = 1.846·10⁻⁵. Every printed constant is a valid floor.
- **[[cor:ec-lb-delta]].** (59/196)·32 = 472/49. (472/49)·2.24566·10⁹ = 2.16317·10¹⁰ > 2.1631·10¹⁰, and (472/49)·0.31686 =
  3.052202 > 3.0522. [[prop:ec-delta-cap]] uses no property of the point.
- **[[rem:ec-lb-conditions]] and [[rem:ec-lb-unbounded]].** 3(1 − 2·10⁻⁵)g(4·10⁻⁶)⁻² = 1.4032576·10²⁰ > 1.4032·10²⁰.
  0.3168/(4.48·10⁻²⁶)² = 1.5784·10⁵⁰ > 1.57157·10⁵⁰, with the exact crossover at 4.4903·10⁻²⁶. 0.3168/h² exceeds
  1.4032·10²⁰ for h < 4.7515·10⁻¹¹, so 4.75·10⁻¹¹ is right. At a fixed h, every condition on (e_Υ, γ_Υ) is an upper bound
  or the exclusion of a countable set, so z can be taken arbitrarily small.
- **The placements.** All nine old texts occur exactly once in the current chapters, at the lines stated (71: 16, 49,
  1462, 1512, 4693; 00: 32; 01: 150; 03: 351; 90: 66). The anchor "stop." is at line 1527 and the heading of
  [[sec:ec-upper]] at line 1529. The stated line counts of all old and new texts are right. Each new text reads
  correctly in context, apart from m2, m3 and n2–n3. In particular, text 3's claims about γ_(Υ,H) check out:
  γ_(Υ,H) does not occur in chapter 71, [[lem:iii-d-5-1]] gives ϑ_ℋ = 1 for every γ_(Υ,H), [[lem:iii-f2-1-1]] has y = 0
  for c_(Υ,H) = −½χ dr, and row u3 makes ε_1 depend on u2.
- **The rest of the paper.** I searched the other chapters for statements that P-LB makes false. I found only chapter 33
  line 3534 (m5). Chapter 34 [[prop:iii-f1-2-3]] (f), row w1, chapter 70 line 1695 and chapter 90 lines 79–84 stay true.
