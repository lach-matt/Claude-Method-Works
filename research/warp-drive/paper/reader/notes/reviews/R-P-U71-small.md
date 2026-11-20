# R-P-U71-small: independent reading of proofs/P-U71-small.md

Tree read at HEAD 6a65bbad (chapter 71 unchanged since ed41ea95, so the report's line numbers hold). Nothing in the
repository was edited. This file is the only one written.

## Verdict

**CONFIRMED** — Major 0, minor 6, nit 7.

**The printed bounds stand**, the integers included, under both readings of the fixed seminorms:
- d_acc ≤ d_R ≤ d_NM ≤ D_NM := D_acc < 1.57157·10⁵⁰;
- N_NM = 21d_NM + 6 ≤ 21D_acc + 6 < 3.30029·10⁵¹;
- every lower bound (1.403·10²⁰, 2.946·10²¹, 1.2497·10²⁴, 2.624·10²⁵, log₁₀ δ < −1.351·10²¹).

Every integer in the text and the report was recomputed in exact integer and rational arithmetic, and every one is
right. All 19 old texts of the 13 replacements occur exactly once in the current chapter 71. No sentence of chapters
00, 01, 03, 46 or 90 becomes false. Every proof step checks: (F1) against prop:uc-dbg and lem:ii-g-4-1 (2)–(3), each
order against the cited chapter, and prop:uc-d-small against thm:iii-k-3-2. The minors are about precision:
- one statement has to name the reading it holds under;
- two justifications are missing;
- a definition is too broad;
- a remark becomes incomplete;
- one pointer is wrong.

## Findings

### m1 (minor). prop:uc-d-small (b), lines 222–238: the fine bound d_NM < 2.6193·10⁴⁹ is stated unconditionally, but it holds only for the seminorms of lem:uc-small-orders (d)

**What is wrong.** d_NM := max(d_R, d_* + d_F + d_Φ), and d_* is "the largest of the orders of lem:uc-small-orders".
lem:uc-small-orders (d) is a conditional: it *chooses* each fixed seminorm at the regularity of the coefficient reads.
Chapter 40 prescribes something else. sec:iii-i8-1 asks the seminorm to bound the maps to the remainder too, and
lem:iii-i11-3-2 copies that convention. Under that prescription d_* is only bounded by D′_* (rem:uc-small-reading).
So (b) and (c) are bounds for two different numbers d_NM. Yet the statement reads as if one d_NM satisfied both. Only
the paragraph after the proof says (b) depends on the reading.

**Why it matters.** Nothing printed in chapter 71 rests on (b): thm:uc-integer's replacement correctly uses
d_NM < 5.2386·10⁴⁹, which holds under both readings. But a reader quoting prop:uc-d-small (b) would take the fine bound
for the paper's construction as chapter 40 writes it.

**Replacement.** In lines 225–226 replace "[[lem:iii-k-2-3]], with which that proof obtains [[eq:iii-j2-4-1]], and let
d_* be the largest of the orders of\n[[lem:uc-small-orders]]. Then:" by:

```
[[lem:iii-k-2-3]], with which that proof obtains [[eq:iii-j2-4-1]], and let d_* be the largest of the orders of the
smallness conditions named in the proof of [[lem:iii-j2-2-3]], for the fixed seminorms of [[lem:uc-small-orders]] (d)
in (b) and for those of [[rem:uc-small-reading]] in (c). Then:
```

and replace lines 233–238, (b) and (c) of the statement, by:

```
(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + 1,038,326,399,999,940 =
26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644, so d_NM < 2.6193·10⁴⁹, and N_NM = 21d_NM + 6 ≤
550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 < 5.5005·10⁵⁰;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + 1,038,326,399,999,940 =
52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693 < 5.2386·10⁴⁹, and N_NM < 1.10009·10⁵¹;
```

(d), the proof and the closing paragraph stand as written.

### m2 (minor). Proof of lem:uc-small-orders (e), lines 195–197: the bound for the reference-point conditions uses the level value of ρ without saying that such reads occur only at the levels

**What is wrong.** (d) gives a condition read at (0, p⃗_b), b ≠ b₀, the order ρ + R_base + 16. Then (e) bounds it by
C_lev + I_lev + R_base + 5, so it uses ρ ≤ C_lev − 11 + I_lev. But (d) also allows ρ < T_12 in Steps 4′ and 4. If
Step 4′ had a reference-point read at b ≠ b₀, its order could reach T_12 + R_base + 5, which exceeds D_* = T_12 + 14.

**Why it is true but unproved.** Step 4′ belongs to thm:iii-i14-3-1, which is stated at b = b₀. At a rotating b,
prop:iii-i15-2-5 has no Step 4′:
- its rotation coordinates are the A_b read at the levels (eq:iii-i15-2-2);
- it bounds A_k directly.

Step 4 asks no comparison (cor:iii-i15-2-10 is a bound). One sentence closes the gap. The replacement is combined with
m3's below.

### m3 (minor). lem:uc-small-orders (c)–(e): the conventions "h small" (ch:s21) and "q small" (ch:s23) are named in the proof of lem:iii-j2-2-3 but not treated

**What is wrong.** lem:iii-j2-2-3 names "q small", one fixed seminorm of large order, so that h + h_rem(q) is small
in that 𝒳^d. It also names "h small" in 𝒳^d, with one d for all of ch:s21. Each convention fixes one order for all of
its uses. Those uses include the levels of thm:iii-i14-3-1 below 3, where the seminorm of 𝒴(β_k) has regularity up to
C_lev − 11 + I_lev, not only the base. (c) treats only "the conditions … on the background of a base". The report's
table entry for these conventions, "≤ 2R_base + 16", is therefore too low for the convention as one order. The bound
that holds is max(2R_base + 16, C_lev + I_lev + 3) < D_*, so D_* is unaffected. But (e) claims "every condition named in
the proof of lem:iii-j2-2-3", and these two are named there without any treatment.

**Replacement for m2 and m3.** Replace lines 195–197, from "*(e)* The orders of (a)–(c)" through "exceeds R_base.
So every order is at most D_*, and so is their largest, d_*. The", by:

```
*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,871,940,942,598,941,194,134, which is less than T_12. Those of
(d) are at most ρ + 14 < T_12 + 14. A read at a reference point (0, p⃗_b) with b ≠ b₀ occurs only at a level, where
ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]], at b₀, and at a rotating b [[prop:iii-i15-2-5]] has no
Step 4′, its rotation coordinates being the A_b read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 <
T_12 + 14, as X_12 = 51,246,486,662,857,739,996,772 exceeds R_base. The conventions "h small" of [[sec:iii-i7-1]] and
[[sec:iii-i8-1]] and "q small" of [[sec:iii-i14-1]] fix one order for all their uses, the largest of the orders that
those uses ask, each of which is a condition of (a)–(d). So every order is at most D_*, and so is their largest, d_*. The
```

(Lengths checked: at most 120 characters in source, 117 after resolution.)

### m4 (minor). Replacement 7 (lines 351–357) and rem:uc-missing (71:2497–2519): "rem:uc-missing states what the bound rests on" becomes incomplete for d_NM

**What is wrong.** After the redefinition, the integer bound for d_NM rests on more than (IS), (SP) and the counts
of sec:cs, which rem:uc-missing lists. It also rests on lem:uc-small-orders and on the reading of the fixed seminorms
(lem:uc-small-orders (d) or rem:uc-small-reading). The new sentence of sec:uc-close keeps the pointer "[[rem:uc-missing]]
states what the bound rests on", so the pointer now promises more than the remark gives.

**Replacement.** In rem:uc-missing replace its last line, "the logarithmic orders that the level steps produce,
which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]).", by:

```
the logarithmic orders that the level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]). The
bound for d_NM rests besides on the orders of the smallness conditions, which [[lem:uc-small-orders]] bounds for the
fixed seminorms of its (d) and [[rem:uc-small-reading]] for the larger ones that [[sec:iii-i8-1]] describes
([[prop:uc-d-small]]).
```

This would be a fourteenth replacement text in the section *Placement*.

### m5 (minor). Proof of prop:uc-d-small (a), line 255: wrong pointer for lem:iii-k-2-2

**What is wrong.** "and through [[cor:iii-i-4-2]] at ℐ⁺, which asks the order 3 of h + h_rem(q) + h_tot(p⃗)" is right
for prop:iii-j2-4-3, through eq:iii-j-2-5 of thm:iii-j-2-4. The proof of lem:iii-k-2-2 (c) instead applies
cor:iii-c-5-3 near ℐ⁺ ∩ {t^♭_* ≤ T̂ + 2}, with h = χ_−h_(−S,−S⁰) + h̃. That corollary asks smallness "as in
prop:iii-c-4-4" at an order k ≥ 5. Read at k = 5, the order is at most 5 + 3, below d_Φ + 8, so the conclusion stands.

**Replacement.** Replace line 255 by:

```
of [[lem:uc-phi-loss]]); and at ℐ⁺ through [[cor:iii-i-4-2]] for Φ(U) ([[thm:iii-j-2-4]]), which asks the order 3 of
h + h_rem(q) + h_tot(p⃗), and through [[cor:iii-c-5-3]] for Ψ(U) ([[lem:iii-k-2-2]] (c)), read at its order 5.
```

See also observation O1 below.

### m6 (minor). Lines 19–21 (with 150–152 and 190–192): "a base" is defined too broadly for the bound R_base

**What is wrong.** "A *base* is [[prop:iii-i8-4-1]] at a level in (2, 3) for a background of K⁺-order at least a♭_K"
is followed by "a base … is charged at most R_base along every chain". R_base = 20,183 + 1,914 + I_base uses the count
of Step 1 of the proof of lem:cs-rest. That count holds for a base with one level step α_0 → α and no transition face
round. Its item (6) charges that step 497 because τ_0 = 2 + ε_g − 2ε exceeds α_1 − ε′. Two cases break the bound:
- **A level near 3, with a background of K⁺-order near a♭_K.** prop:iii-i8-4-1 then needs level steps shorter than
  a♭_K − 2 < ε_K, about 6·10¹³ of them, each with up to about 6.8·10⁹ transition face rounds. That exceeds R_base.
- **The base of lem:iii-i11-3-3.** It is used in (c) and (d) for the term C|p⃗_b|‖u_j − u‖. That proof fixes "an
  admissible α′ ∈ (2, min(3, 2 + w_0))", and for α′ above τ_0 + ε′ the level step has transition face rounds,
  at most 3(1/Δτ_0 + 1) < 2.06·10¹⁰ more.

**Why it is harmless.** The three bases actually used are fine once that α′ is chosen: Step 1 at α_1, thm:iii-i11-4-1
at the α′ of def:cs-choices (f), and lem:iii-i11-3-3. Even unchosen, 2.06·10¹⁰ is far inside the slack
X_12 − R_base ≈ 5.1·10²² of (e). But the general claim as written is false, and the orders "2R_base + 16" and
"ρ + R_base + 16" need the choice.

**Replacement.** Replace lines 19–21 by:

```
A *base* is [[prop:iii-i8-4-1]], with its forward solution, at a level α′ ∈ (2, 3) that it reaches from its α_0 by one
level step without transition face round, for a background of K⁺-order at least a♭_K: the base of Step 1 of the proof of
[[thm:iii-i14-3-1]] at α_1, that of the proof of [[thm:iii-i11-4-1]] at the α′ of [[def:cs-choices]] (f), and that of
the proof of [[lem:iii-i11-3-3]], whose admissible α′ we take below 2 + ε_g − 2ε, as that proof allows. By
[[lem:cs-iterations]] (b), with the count of Step 1 in the proof of [[lem:cs-rest]], a base with all its rounds, steps
and windows charged is charged at most R_base along every chain.
```

(At most 120 characters in source, 117 after resolution. lem:iii-i11-3-3's w < α′ − 2 can still be taken, and its
seminorm ‖·‖_(α′) still dominates ‖·‖_(w).)

### n1 (nit). lem:uc-small-orders (c)–(e), lines 72–74, 80–82, 88: "the largest of these orders" is not a definite number

A condition "of order j" is of order j′ for every j′ ≥ j, and (c), (d) give only "order at most". So "the largest of
these orders, d_*" is not well defined, and d_NM is now defined through it. The fix is to give each condition a
definite order:
- in line 73 replace "have order at most" by "have order";
- in line 81 replace "has order at most ρ + 14, or ρ + R_base + 16" by "has order ρ + 14, or ρ + R_base + 16".

Both are true because order is upward closed. "The largest of these orders" in (e) is then definite, and
m + 14 ≤ d_* holds because the R_j condition is given ρ + 14.

### n2 (nit). (F1), line 105: the constant of ‖w − w′‖_j ≤ C_j‖β − β′‖_(j+5) depends on β′

h_(b,rem)(q) − h_(b′,rem)(q′) contains (h_(b,rem) − h_(b′,rem))(q′) = O(|b − b′|)‖q′‖. So C_j depends on a bound for
‖q′‖_(𝒬^(j+5)). The final statement allows that ("C_k depending only on upper bounds for ‖β‖_(k+14), ‖β′‖_(k+14)"), but
the intermediate claim does not say it. Replace line 105 by:

```
‖w − w′‖_j ≤ C_j‖β − β′‖_(j+5), with C_j depending on a bound for ‖q′‖_(𝒬^(j+5)), as h_(b,rem)(q) is linear in q and
smooth in b and h_tot(p⃗) is smooth in p⃗, and
```

The rest of (F1) checks. Spelled out, the bound is:

    ‖(A_β − A_β′)u‖_k ≤ C_k(‖β − β′‖_8 ‖u‖_(k+2) + [‖β − β′‖_(k+8) + (‖β‖_(k+14) + ‖β′‖_(k+14))‖β − β′‖_5] ‖u‖_2).

So k + 8 suffices, as the report says, and k + 11 is safe.

### n3 (nit). (F2), lines 109–110: the direct bounds at a rotating b are not literally (A_β − A_β′)u

The direct bound's last term is ‖(L_(h,p⃗) − L_b)u‖_ρ. Its reference L_b is not L_(0,p⃗_b), which differs from L_b by
O(|b − b₀|) on supp(1 − χ_K) (proof of lem:iii-i8-3-2). It is (L_β − L_(b₀))u, to which (F1) applies, plus
(L_(b₀) − L_b)u, of size O(|b − b₀|)‖u‖_(ρ+2). Replace "(A_β − A_β′)u, and is needed at the order ρ + 2, ρ the
regularity of the seminorm. By the induction in the proof of" (line 110) by:

```
(A_β − A_β′)u, at a rotating b also through (L_(b₀) − L_b)u, whose coefficients are O(|b − b₀|), and is needed at the
order ρ + 2, ρ the regularity of the seminorm. By the induction in the proof of
```

### n4 (nit). Lines 187–188: "|p⃗| ≥ |b − b₀| being made small by the choice of ℬ_*" is garbled

Replace lines 187–188 by:

```
‖h‖ + |p⃗| of the direct bounds is such a bound, |p⃗| ≤ ‖β‖_0, its component |b − b₀| being also made small by the
choice of ℬ_*; R_q and Δ_q are bounded by C‖q‖ in this way ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]), q being a
```

### n5 (nit). Replacements 3 and 6: the orders are evaluated by lem:uc-small-orders, not by prop:uc-d-small

Replacement 3 says "[[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small". Use
instead:

```
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc
and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.
```

Replacement 6 says "[[prop:uc-d-small]] bounds the orders …, and with them d_NM". Use instead:

```
through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are
at most 62N_Λ + 10 < 1.04·10¹⁵ ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of [[lem:iii-k-2-3]] satisfies
[[eq:ec-upper]] in the form of [[lem:uc-dr]], [[lem:uc-small-orders]] bounds the orders at which these results ask U
small, and [[prop:uc-d-small]] bounds d_NM ([[thm:uc-integer]]). Given ε_K, the explicit part
```

### n6 (nit). Replacements 1, 2 and 13: "the largest of the d's" names existential numbers

The three d's exist only as "There are d and ε_0". The definition of d_NM is definite once it says the d's are those
that prop:uc-d-small (a) fixes. Replacement 1 also says "these contain d_* + D + d_Φ" where it means the order
d′_0 ≥ d_* + D + d_Φ. Proposed texts, all checked for length:

Replacement 1:

```
[[thm:ii-g-2-1]] is applied in the proof of [[thm:iii-k-3-2]] with N_NM = 21d_NM + 6, where d_NM is the largest of
the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], as [[prop:uc-d-small]] fixes them. Each of these
is at least the loss of the estimate of its result, that of [[lem:iii-k-2-3]], a construction, accounted by
[[def:ec-accounted-loss]] and the other two as their proofs fix them, and at least the orders at which its proof asks U
small; for [[lem:iii-k-2-3]] these include the order d′_0 ≥ d_* + D + d_Φ of its proof, with d_* of [[lem:iii-j2-2-3]],
D the d of [[thm:iii-j2-4-1]] and d_Φ the loss of U ↦ Φ(U). As (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]] of the
right inverse of [[lem:iii-k-2-3]], whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc ([[thm:loss-d]]).
```

Replacement 2:

```
[[def:ec-accounted-loss]], and d_NM the loss with which the proof of [[thm:iii-k-3-2]] applies the Nash–Moser theorem
[[thm:ii-g-2-1]]: the largest of the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]] that
[[prop:uc-d-small]] fixes, each at least the loss of its estimate, that of [[lem:iii-k-2-3]] accounted by
[[def:ec-accounted-loss]], and the orders at which its proof asks U small. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]
hold with d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:
```

Replacement 13 ("with the orders" reads oddly):

```
products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
```

### n7 (nit). Lines 198–199: there are several seminorms in which R_j → 0 is asked

e_S and e_(S⁰) enter the forcings of the base, of every level and of thm:iii-i11-4-1, each read in its own fixed
seminorm. So m, the order of ch. 46, is their largest regularity. Replace lines 198–199, from "order m of the proof of
[[lem:iii-k-2-3]] is the regularity ρ" through "so m + 14 ≤ d_*. The integer:", by:

```
order m of the proof of [[lem:iii-k-2-3]] is the largest regularity ρ of the seminorms in which the proof of
[[lem:iii-j2-2-3]] asks R_j → 0, and those conditions have the orders ρ + 14 by (d); so m + 14 ≤ d_*. The integer:
```

## What was checked and holds

### lem:cs-sharp

**The levels.**
- At the choice of def:uc-choice every spacing is at least Δβ_0 (lem:uc-admissible), and α − α_1 < 2 + ε_K.
- (2 + ε_K)/Δβ_0 = 2,000,000,000,000,016,416,000,000/16,383,184,416 = 122,076,389,376,829.22…
- So K ≤ K̄ = 122,076,389,376,829 < 1.22077·10¹⁴, in agreement with rem:ec-upper-point.

**The second line of eq:ec-upper.** It is Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0 (prop:ec-upper).
- c(β_k) ≤ max(497, C_lev) = C_lev (lem:cs-levels, eq:cs-clev).
- c_b ≤ 469 and c′_b ≤ 466 (lem:cs-base).
- c_0 is at most the integer of eq:cs-cstar, which is less than C_* (lem:cs-rest, prop:cs-cstar).
- N_b ≤ 1/Δβ_0 + 1 = 61,038,194,688,415.11… < 61,038,194,688,416 < R_b.
- The first line is less than D_e (prop:uc-explicit, with lem:uc-gaps).

**d_R.** lem:uc-dr has the same first line, and lem:cs-levels, lem:cs-base and lem:cs-rest state the same bounds for
the c^Ψ. So d_R ≤ D_♭ as well.

### lem:uc-small-orders, condition by condition

- **(a), d_T + 3 = 20,183.**
  - thm:iii-i-5-3 asks ‖h‖_(𝒳^(d_T)) < ε_0. Its (iii) asks ‖P − P_0‖_((0;d_T−5)) small through C(|S| + ‖h‖_(𝒳^(d_T))).
  - eq:s19-time-hyp asks |S| + ‖h‖_(𝒳³) small, and cor:iii-h2-5-1 asks |b − b₀| small.
  - lem:iii-j2-2-1 (a) gives +3 at the q-backgrounds.
- **(b), k_1 = 10.** In lem:iii-i4-4-2, Π_b is the 𝒮_1-component of L̃_b(0)⁻¹(f̂^♭(0), 0, 0), where
  f^♭ = f′ − L_b u_I. Its charge is 6 + 2 for f^♭, 1 for prop:ii-g1-3-3 (1), 1 for prop:iii-h-3-2 and 0 for the
  component, so Π_b is bounded from the order 10.
- **(b), k_0 = k_1 + 2 + L_u.**
  - Proof of lem:iii-i4-4-2 (a): ‖f′‖ ≤ ‖f‖ + C‖u‖_(k_1+2), with u in eq:iii-i2-5-2.
  - L_u ≤ 20,183 + 407 + 466·(steps of prop:iii-i2-5-1).
  - steps ≤ (α_K − ½)/(a_K − 2) + 1 < 1/(2Δβ_0) + 1 ≈ 3.05·10¹³ < R_b.
  - eq:s20-d: max(20,180, k̄_0 + 2, 20,197) = k̄_0 + 2 = 28,443,801,200,020,604.
- **(c), the base.**
  - The base's fixed norms are read by base maps, charged at most R_base (subject to m6).
  - The reference-point term adds R_base + 2, so the norms are needed at regularity 2R_base + 2.
  - (F1) gives 2R_base + 13 for smallness and 2R_base + 16 for the constants.
  - k̄_0 + 5 and 20,183 are below R_base.
  - prop:iii-i15-2-8 and prop:iii-i15-2-12 are direct bounds of the same form.
- **(d), the level reads.**
  - Levels above 3: the reads are after Step 0, at most C_lev − 11 + I_lev (lem:cs-iterations (a)), in fact at most
    C_lev − 22 + I_lev.
  - Levels below 3: 497 + 16·1,470,302 + 3·6,847,261,002 = 497 + 20,565,307,838, far below I_lev. The windows come
    from lem:ec-counts (e) and lem:uc-gaps; the rounds are fewer than 1/Δτ_0 + 1 = 6,847,260,422.4…; each round is
    charged ℓ⁺_tf + 2 (lem:ec-round-charges (a)).
- **(d), Step 4′.** C^rot is read by thm:iii-i12-3-1 at (0, 0), charged at most C_lev − 11 + I_lev + X_12 = T_12 − 11.
  p⃗′_0 is read by thm:iii-i11-4-1, charged at most T_11. Both are below T_12. Step 4′ is at b₀ (m2).
- **(d), the comparisons.** They are those of the proof of lem:iii-j2-2-3, the proofs of lem:iii-i8-3-3,
  lem:iii-i11-3-3 and lem:iii-i13-2-3, and the direct bounds of Step 3 of prop:iii-i15-2-5 (A_k, A_b). The extra term
  at (0, p⃗_b) is bounded through (i) of prop:iii-i8-4-1 at α′, a base map, as the proof of lem:iii-i11-3-3 does. That
  gives ρ + R_base + 16.
- **lem:iii-i9-2-6 and lem:iii-i14-2-3/4.**
  - lem:iii-i9-2-6 (c), (e) bound r^ν in H^(k−2) by ‖h‖_(𝒳^k) + |p⃗|, so ρ + 11 is safe; its continuity needs k ≥ 5.
  - R_q and Δ_q are O(‖q‖), which F1 covers.
- **(e).** The largest order is T_12 + 14 = D_*. Since ρ ≤ T_12 − 11 in Step 4′, the true maximum is at most
  T_12 + 3. m + 14 ≤ d_* holds (n7).

### The difference bound (F1)

Checked in full against prop:uc-dbg and against lem:ii-g-4-1 (2)–(3), with d = 3:
- **The p⃗-part.** ∂_(p⃗)Φ_γ vanishes at w = 0, so (3) applies to it.
- **The w-part.** ∂_wΦ_γ(·, p⃗_s, w_s) = ∂_wΦ_γ(·, p⃗_s, 0) + G(w_s) with G(0) = 0. So (2), and (3) on G, give
  ‖G(w_s)(w − w′)‖_j ≤ C(‖w_s‖_6 ‖w − w′‖_j + ‖w_s‖_(j+6) ‖w − w′‖_0).
- **The product with D^γ_b u.** It is read at the orders 3 and k + 3.
- **The orders.** ‖w‖_j ≤ C‖β‖_(j+5) and ‖w_s‖_(k+9) ≤ C(‖β‖_(k+14) + ‖β′‖_(k+14)).
- **Smallness.** ‖β‖_14 small gives the smallness of ‖w_s‖_3 that (3) asks.

The display of eq:uc-small-diff follows, with k + 8 in place of k + 11. The one omission is n2.

### The meaning of "order j"

The condition must hold when ‖β‖_j is small and ‖β‖_(j+D) is bounded. On the ball ‖β‖_(d_0) < δ_𝔹 of thm:iii-j2-4-1,
with d_0 = d_* + D (lem:iii-j2-2-3), both hold for every j ≤ d_*. So the convention is consistent with
thm:iii-j2-4-1. It makes explicit the "u_j bounded at a fixed order" of the proof of lem:iii-j2-2-3.

There is no circularity: by the induction of the proof of thm:iii-j2-4-1, an entry's conditions use only the tame
bounds of earlier entries and earlier levels.

For lem:iii-k-2-3 the conditions are read in β̂, with D = d_F:
- ‖β̂‖_(d_0) ≤ C‖β^Ψ‖_(d_0+d_Φ) ((i) of *The constants*);
- this is at most C(‖U‖_(𝒟^d) + Θ_d) < 2Cε_0 for d ≥ d_0 + d_Φ;
- in thm:iii-k-3-2, |U|_(3d) < δ ≤ ε_0 supplies ‖U‖_(𝒟^d).

The e_S terms are bounded in β̂ at the order ρ + 14 by F1, with Ψ(U) − Φ(U) = (χ_−h_(−S,−S⁰), 0, 0), whose norm is at
most CΘ. That is consistent with ch. 46's own m + 5.

### prop:uc-d-small

**(a)** checks against *The constants* of the proof of lem:iii-k-2-3. That d must be at least d_R, d′_0, d_BG and
m + 5. The proof of thm:iii-j2-4-2 asks U small in three ways:
- through ‖Φ(U)‖_(d_0) small;
- through lem:iii-j2-1-2 (b), (e) at the composed loss d_R;
- through |U_0| alone for D_UΦ (rem:iii-j-2-5; the proof of thm:iii-j-2-4 uses only |U_0| < ε_0).

So d′_0 = max(d_* + d_F + d_Φ, d_R). The other conditions are smaller: d_BG = 11 < d_*, m + 5 < d_*, and
d_Φ + 8 ≤ d_* + d_F + d_Φ. lem:iii-j2-2-4's d_1 = 3 serves, its proof using lem:ii-g-4-1 with d = 3 only. For
prop:iii-j2-4-3, the domain |U|_(3d_NM) < δ covers its 𝒟^(3d) condition. d_F ≤ d_R because the construction of ℛ(U)
composes that of thm:iii-j2-4-1 at Ψ(U) with maps of non-negative charge. d_acc ≤ d_R by the proof of thm:loss-d.

**Fit with thm:iii-k-3-2.** The d of thm:iii-k-3-2 is the largest of the three d's that (a) fixes, so d_NM is exactly
what thm:iii-k-3-2 uses (n6 for the wording). N_NM = 21d_NM + 6 is unchanged (ch. 29, ch. 46).

**The lower bounds.** Every lower bound of ch. 71 needs only d ≥ d_acc. That covers thm:loss-d (ii),
cor:uc-two-offsets, eq:uc-lower and prop:ec-delta-cap, whose proof uses only d ≥ d_acc.

### The replacement texts

All 19 old strings were matched in a scratch copy of chapter 71 and each occurs exactly once:
1, 2, 3, 4, 5, 6, 7a, 7b, the title of 8, its statement and its proof, 9, 10a, 10b, the display of 11, its statement
and its proof, 12 and 13. The subsection was then inserted before the heading of sec:ec-linear. The edition's
numbering and resolution, run in memory, gave:
- **problems:** 0;
- **new labels:**
  - Lemma 49.107, Lemma 49.108, Remark 49.109, Proposition 49.110;
  - Section 49.12.7;
  - equations (49.51)–(49.54);
- **line lengths:** at most 121 characters in source and after resolution;
- **wrapped lines:** none of the new or replaced lines starts with a forbidden marker. The only flags were the
  existing lists and tables of chapter 71.

Every new text is true. Every other occurrence of d_NM in chapter 71 stays true, for example lines 387, 393, 2071–2072
and 2082. So do the headline sentences of chapters 00 (line 34), 01 (154), 03 (351–354) and 90 (64–72). Each speaks of
"the loss d with which the settling proof applies the Nash–Moser theorem", now d_NM, and holds by prop:uc-d-small (d).
Chapter 46 needs no change. The one sentence that becomes incomplete is the pointer to rem:uc-missing (m4).

## The seminorm reading (open point 1)

**What the chapters say.**
- sec:iii-i8-1 states it outright: the fixed seminorm of 𝒴(α) is taken "so large … that the linear maps used below
  … (in the proof of lem:iii-i8-3-2, the maps from the forcing f′ of its Step 0 to the coefficients **and to the
  remainder**; and those of prop:iii-i8-4-1 (i)) are bounded in this seminorm".
- ‖·‖_(α′) is chosen "in the same way".
- lem:iii-i11-3-2 takes its seminorms "chosen as in sec:iii-i8-1".
- prop:iii-i8-4-1 (i) and the induction bound of prop:iii-i15-2-5 pass the remainder of one level, measured in these
  seminorms, to the next.

So the regularities have to chain through the levels. **The chapters' text supports the cumulative reading of
rem:uc-small-reading.** The fine reading is supported only by the proof of lem:iii-j2-2-3, whose comparisons need
R_j → 0 in the read seminorm and the u_j only "bounded at a fixed order". The fine reading is a valid re-derivation,
not a reading of chapter 40: every bound of a solution by data that chapters 40–44 take from the chained seminorms is
replaced by the tame bound (F2). The text says so in one sentence of (c). It is legitimate because those bounds are
needed only at earlier entries or earlier levels, where thm:iii-j2-4-1's induction already provides them. The text
cannot exclude the cumulative reading. It is the literal one. So both readings must be covered, and the text does
cover both.

**How my reading depends on the chapter 40 question.** Read literally, with one seminorm per class for all levels,
prop:iii-i8-4-1 (i) asks ‖F‖_(𝒴(α′)) ≤ C‖F‖_(𝒴(α″)) together with the remainder chain. No single finite regularity
satisfies both. That reading is therefore available to neither side.
- **Fine reading.** The fine bound does not depend on how chapter 40 is repaired, since (F2) replaces (i)'s seminorm
  bounds.
- **Cumulative reading.** The cumulative bound presupposes the natural repair: ‖F‖ in (i) of larger regularity, as
  prop:iii-i15-2-5 already states its induction bound. With that repair the per-level ρ_k of rem:uc-small-reading are
  consistent. The recursion is ρ_k ≤ ρ_(k+1) + 2 + C_lev − 11 + I_lev, with ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev. So
  ρ_1 ≤ T_12 + K̄(C_lev + I_lev − 9).
- **Iterations inside a level step.** Within a step the window loops and rounds are already inside the step's charge.
  Each applies (L − L_b) at charge 11 ≥ 2, so chaining seminorms through them adds nothing beyond the charges.

**Every reading the text cannot exclude** gives d_* ≤ D′_* < 2.6193·10⁴⁹. Then:
- d_NM ≤ D_♭ + D′_* + d̄_Φ < 5.2386·10⁴⁹ < D_acc;
- N_NM < 1.10009·10⁵¹ < 21D_acc + 6.

So the printed 1.57157·10⁵⁰ and 3.30029·10⁵¹ hold, and lem:cs-sharp is what makes them hold. Without it,
d_* + d_F + d_Φ could exceed D_acc. **The fine 2.6193·10⁴⁹ for d_NM is reading-dependent (m1).** thm:uc-integer's
replacement rightly prints the reading-independent 5.2386·10⁴⁹.

## Numbers recomputed (exact integers and fractions)

All agree with the text and the report.

**Chapter 71's own numbers.**
- N_ι = 107,279,395,180,026,392,909,234,131,199,999,996.
- C_lev = 214,558,790,360,052,785,818,485,009,600,000,520.
- k̄_max = 12,811,621,665,714,434,999,187.
- I_lev = 34,268,829,852.
- I_base = 1,435,970,471,299,470,574,962.
- The seven summands of eq:cs-cstar add to 17,389,163,815,025,371,354,557,103,786.
- 6N_ι + 3N̄_Λ + that sum = 643,676,388,469,322,172,480,826,383,357,103,759 < C_*.
- D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000.
- 21D_acc + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006.
- d_Φ ≤ 62·16,747,199,999,999 + 2 = 1,038,326,399,999,940, and d_Φ + 8 ≤ 1,038,326,399,999,948.

**New numbers.**
- X_12 = 51,246,486,662,857,739,996,772.
- T_11 = 214,558,790,360,054,221,788,956,343,339,427,453.
- T_12 = 214,558,790,360,104,032,305,147,901,608,827,144, so T_11 < T_12.
- C_lev − 11 + I_lev + X_12 = T_12 − 11.
- (2 + ε_K)/Δβ_0 = 62,500,000,000,000,513,000,000/511,974,513 = 122,076,389,376,829.22…
- 16,383,184,416 · 122,076,389,376,829 = 2,000,000,000,000,012,824,296,864.
- 16,383,184,416 · 122,076,389,376,830 = 2,000,000,000,000,029,207,481,280.
- (2·10¹⁸ + 16,416)·10⁶ = 2,000,000,000,000,016,416,000,000 lies between them, so K ≤ K̄.
- 16,383,184,416 · 61,038,194,688,415 = 1,000,000,000,000,014,603,740,640 > 10²⁴.
- 1/Δβ_0 + 1 = 61,038,194,688,415.11… < R_b = 61,038,200,000,000.
- K̄C_lev = 26,192,562,436,215,228,354,699,390,649,792,285,562,280,875,951,080.
- 469R_b = 28,626,915,800,000,000 and 466(R_b + 1) = 28,443,801,200,000,466; their sum is 57,070,717,000,000,466.
- D_♭ = 26,192,562,436,215,872,034,699,391,908,492,342,632,997,875,951,546 = 2.6192562…·10⁴⁹ < 2.6193·10⁴⁹.
- k̄_0 = 20,602 + 466R_b = 28,443,801,200,020,602, and 12 + 20,590 + 466R_b gives the same.
- R_base = 1,435,970,471,299,470,597,059.
- 2R_base = 2,871,940,942,598,941,194,118, and 2R_base + 16 = 2,871,940,942,598,941,194,134 < T_12.
- C_lev − 11 + I_lev = 214,558,790,360,052,785,818,485,043,868,830,361.
- ρ + R_base + 16 at that ρ = 214,558,790,360,054,221,788,956,343,339,427,436, which is C_lev + I_lev + R_base + 5 and
  is below T_12 + 14.
- D_* = T_12 + 14 = 214,558,790,360,104,032,305,147,901,608,827,158 = 2.1455879…·10³⁵ < 2.14559·10³⁵.
- K̄(C_lev + I_lev − 9) = 26,192,562,436,215,228,354,699,394,833,207,300,964,646,683,858,927.
- D′_* = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207 < 2.6193·10⁴⁹.

**The fine reading.**
- D_♭ + D_* = 26,192,562,436,216,086,593,489,752,012,524,647,780,899,484,778,704.
- Adding d̄_Φ gives 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644 = 2.6192562…·10⁴⁹.
- 21 times that plus 6 = 550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 = 5.5004381…·10⁵⁰
  < 5.5005·10⁵⁰.

**The cumulative reading.**
- D_♭ + D′_* = 52,385,124,872,431,314,948,189,146,848,603,889,688,145,109,831,753.
- Adding d̄_Φ gives 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693 = 5.2385124…·10⁴⁹
  < 5.2386·10⁴⁹.
- 21 times that plus 6 = 1,100,087,622,321,057,613,911,972,083,820,681,705,255,901,706,465,559 = 1.1000876…·10⁵¹
  < 1.10009·10⁵¹.
- D_acc minus the cumulative bound = 104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307 > 0.

**Levels below 3.**
- 16·1,470,302 = 23,524,832 and 3·6,847,261,002 = 20,541,783,006; their sum is 20,565,307,838 < I_lev.
- 1/Δτ_0 = 10¹⁷/14,604,381 = 6,847,260,421.37…

**rem:cs-sharpness.**
- C_* − 6N_ι = 3,628,919,841,642,544,595,212,800,000,024 < 3.63·10³⁰.
- c̄_0 − 6N_ι = 17,389,163,815,025,421,596,157,103,783 < 1.74·10²⁸.
- (N̄_Λ + 2)(d_Φ + 30) = 17,389,059,886,080,535,910,399,999,970 < 1.739·10²⁸.
- K̄ < 1.22077·10¹⁴, and D_♭ < 2.62·10⁴⁹.

## Contract

- **`python3 assemble.py --check`**, last line: `labels 4570, computations cited 0, problems 0`.
- **`python3 lint.py proofs/P-U71-small.md`**: 296 hits, every one "reference to undefined label", the single-file
  limitation. Every referenced label resolves in the in-memory merge.
- **`python3 lint.py --chapters`**: 0 hits on the unmodified tree.
- **Lint on the merged scratch chapter**: no hit other than "reference to undefined label" (212 labels against 203,
  that is 9 new).
- **Line lengths**: at most 121 characters in the proof file and after resolution. Every replacement text proposed in
  this review was checked the same way.
- **Wrapped lines**: none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The two lines beginning "#" are headings.
- **Text**: no backslash, every label key lowercase, no file, program, code or AI language. The integers are presented
  as derivations, as chapter 71 does.

## Observations outside the text (not counted)

- **O1 (chapters 36/46).** prop:iii-c-4-4 asks ‖h‖_(H^(k,a₀,a_I)) < ε₀ with ε₀ depending on k, through a Neumann
  series that uses an algebra constant at the order k. cor:iii-c-5-3, and with it the membership claim of
  lem:iii-k-2-2 (c), then reads smallness at the order of the membership. Taken literally, membership in ℱ^∞_ex would
  need smallness at every order. A tame product bound (lem:ii-g-4-1 (2)) needs smallness at a fixed low order only.
  This predates the text and does not involve d_NM, but the owner of chapter 36 may want to state the low-order form.
- **O2 (the report, not merged).** The table row for ch:s21 "h small" (≤ 2R_base + 16) is right for the base only.
  As one convention for all of ch:s21 the bound is max(2R_base + 16, C_lev + I_lev + 3) (m3). D_* is unaffected.
- **O3 (chapter 40).** The circularity in prop:iii-i8-4-1 (i) is real as written; see the seminorm section. Neither
  bound of the text depends on how it is repaired, as long as the repair is the natural one, a larger regularity for
  ‖F‖.
