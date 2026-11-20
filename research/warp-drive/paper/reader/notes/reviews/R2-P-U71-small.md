# R2-P-U71-small: confirming reading of the fix round F-P-U71-small

## Scope

**Tree read.** HEAD a3877611. The proof file, proofs/P-U71-small.md (438 lines), is unchanged since 0d3c10c4. Chapter 71 is
unchanged since 85bcfe80.

**Commits that landed during the reading.** Both were checked, and neither changes a conclusion below:
- 75bcfa65 (R2-P-40-sem nit): sec:iii-i8-1 now says "the bounds and the continuity" and adds one sentence on F_j → F.
- a3877611 (R-P-36-c44 applied): the statement of prop:iii-c-4-4 names the domain and target of the smooth dependence.
  It still asks smallness in H^(3,a₀,a_I)_b, with ε₀ independent of k.

**Diff checked.** `git diff 85bcfe80 HEAD` of the proof file agrees line for line with the diff at the end of the report
notes/reports/F-P-U71-small.md.

**Edits.** Nothing in the repository was edited. This file is the only one written.

## Verdict

**CONFIRMED** — Major 0, minor 0, nit 1.

**All 6 minors and 7 nits of R-P-U71-small are resolved.**
- Every new text is true where it stands.
- Every cited label was checked against its target.
- The six departures from the reviewer's texts (m1, m3, m5, m6, n5, n7) are justified. Two of them correct the reviewer
  (m3, n7).

**The headline bounds stand**, under both readings of the fixed seminorms:
- d_acc ≤ d_R ≤ d_NM ≤ D_NM := D_acc < 1.57157·10⁵⁰;
- N_NM = 21d_NM + 6 ≤ 21D_acc + 6 < 3.30029·10⁵¹;
- the finer bounds:
  - d_acc, d_R ≤ D_♭ < 2.6193·10⁴⁹;
  - d_NM < 2.6193·10⁴⁹ under the fine reading, with N_NM < 5.5005·10⁵⁰;
  - d_NM < 5.2386·10⁴⁹ under either reading, with N_NM < 1.10009·10⁵¹;
- every lower bound (thm:loss-d (ii), cor:uc-two-offsets, eq:uc-lower), carried to d_NM by d_NM ≥ d_R ≥ d_acc.

**No integer moved.** Every integer was recomputed exactly.

**Placement.** The 14 replacement texts have 20 old texts, and each occurs exactly once in the current chapter 71. The
merged chapter numbers with 0 problems.

**`python3 assemble.py --check`**, last line: `labels 4570, computations cited 0, problems 0`.

## The original findings

| Finding | Resolved | New text true; labels checked | Departure from the reviewer's text |
|---|---|---|---|
| m1 | yes | yes | justified |
| m2 | yes | yes | none |
| m3 | yes | yes; bound T_12 + 3 ≤ D_* | justified; corrects the reviewer |
| m4 | yes | yes | none (applied as text 14) |
| m5 | yes | yes; now literally true (order 3 ≤ 5) | justified |
| m6 | yes | yes | justified |
| n1 | yes | yes | none |
| n2 | yes | yes | none |
| n3 | yes | yes | none |
| n4 | yes | yes | "as" added; fine |
| n5 | yes | yes | text 6 reworded; justified |
| n6 | yes | yes | none |
| n7 | yes | yes | justified; corrects the reviewer |

### m1. prop:uc-d-small, lines 241–258

**The text.** d_* is now "the largest of the orders of the smallness conditions named in the proof of
[[lem:iii-j2-2-3]], the fixed seminorms being those of [[lem:uc-small-orders]] (d) or those of
[[rem:uc-small-reading]]". Item (b) opens "for the fixed seminorms of [[lem:uc-small-orders]] (d)". Item (c) opens "for
those of [[rem:uc-small-reading]]". Item (d) says "in either case".

**Resolved.** The fine bound 2.6193·10⁴⁹ is no longer stated unconditionally.

**Departure.** The reviewer tied the definition of d_* to the item. The fixer keeps it independent of the item. That is
right: (a) and (d) use d_* and hold under both readings.

**Further checks.**
- thm:uc-integer's new sentence "d_NM < 5.2386·10⁴⁹" holds under both readings, since D_* < D′_*.
- The sentence after the proof states which bound rests on which reading.

### m2. Proof of (e), lines 208–212

**The text.** "Of the conditions of (d), one read at a reference point (0, p⃗_b) with b ≠ b₀ occurs only at a level".

**Checked.**
- thm:iii-i14-3-1 is stated with "(b = b₀)" (42:377).
- Item (2) of [[sec:s23-base-points]] says "Step 4′ of the proof of [[thm:iii-i14-3-1]] is not used at b" (42:1036–1038).
- prop:iii-i15-2-5 reads A_b at the levels (eq:iii-i15-2-2).
- Step 4 at b is cor:iii-i15-2-10 (41:1706), a bound with no comparison.

**Order.** ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14 holds exactly, as X_12 > R_base. True.

### m3. The conventions "h small" and "q small", (e), lines 212–216

**Each citation checked.**
- [[sec:iii-i7-1]] fixes "h small" as small in 𝒳^d, with d at least the d of eq:s20-d (40:166).
- [[sec:iii-i8-1]] keeps it (40:744).
- [[sec:iii-i9-1]] keeps it "in this and the next section, and in [[ch:s22]]" (40:1373–1375).
- The base points of [[ch:s22]] are "as in [[sec:iii-i9-2]]" (41:63).
- [[sec:iii-i14-1]] fixes "q small" as one fixed seminorm of large order (42:143).
- The proof of lem:iii-j2-2-3 names both (43:302–306).

**The uses and their orders.**

| Where the use lies | Bound on its order | Source |
|---|---|---|
| The bases | 2R_base + 16 | (c) |
| The level reads | C_lev + I_lev + 3 | (d) |
| Reference-point reads at the levels | C_lev + I_lev + R_base + 5 | (d) |
| Step 4′: C^rot read through thm:iii-i12-3-1 | (T_12 − 11) + 14 = T_12 + 3 | read charged at most C_lev − 11 + I_lev + X_12 = T_12 − 11 |
| Step 4′: p⃗′_0 read through thm:iii-i11-4-1 | below T_12 + 3 | read charged at most T_11 < T_12 − 11 |
| Step 4′: the second seminorm of the base inside thm:iii-i11-4-1, at α′ | below T_12 + 3 | regularity at most C_lev − 11 + I_lev + 2 + R_base = T_11 − 31 |
| Step 4 | as Step 4′ | applies thm:iii-i12-3-1 again |

The largest is T_12 + 3 = D_* − 11 ≤ D_*.

**The fixer's correction is right.** The reviewer's max(2R_base + 16, C_lev + I_lev + 3) = C_lev + I_lev + 3 omits the
ch:s22 uses in Steps 4′ and 4.

**The departure is justified.** The text says each use "asks an order that (a)–(d) bound, by (F1) at the regularity of
its seminorm". The reviewer had "each of which is a condition of (a)–(d)". The fixer's wording is the more accurate:
these uses are bounded by conditions of (a)–(d), not literally such conditions.

**The cumulative reading.** All these uses are at most D′_*. rem:uc-small-reading now cites "the proofs of (c)–(e)".

### m4. Text 14, rem:uc-missing

**Placement.** The old last line occurs once (71:2519).

**The new sentence is true.** sec:iii-i8-1 as repaired still takes its seminorm so large that the maps "to the
coefficients and to the remainder" are bounded (40:747–750). These are "the larger ones" of rem:uc-small-reading.

**Pointer.** The pointer "[[rem:uc-missing]] states what the bound rests on" of text 7 is now complete.

### m5. Proof of prop:uc-d-small (a), lines 275–277

The pointer is fixed: cor:iii-c-5-3 for Ψ(U), through lem:iii-k-2-2 (c). Point 3 below checks the clause against
chapter 36.

### m6. The definition of a base, lines 19–27

**The general shape.** The proof of prop:iii-i8-4-1 takes α_0 ∈ (2, min(a_K, 2 + ε_g, 5/2)) and steps shorter than
a_K − 2 (40:1151–1152). So a single level step to α′ < τ_0 is allowed once α′ − α_0 < a_K − 2.

**The four bases.**

| Base | One level step | Level below τ_0 |
|---|---|---|
| Step 1 of thm:iii-i14-3-1 at α_1 | α_1 − α_0 < a♭_K − 2 (71:4239) | α_1 − 2 < ε_K < ε_g − 2ε (71:4241–4242) |
| thm:iii-i11-4-1 at the α′ of def:cs-choices (f) | its background has a_K ≥ 4 + ε_K (41:967) | α′ ∈ (2, 2 + ε_g − 2ε) (71:3858) |
| lem:iii-i11-3-3 | background 0 at (0, p⃗_b), so every K⁺-order | α′ fixed in (2, min(3, 2 + w_0)) (41:918), may be taken below τ_0 |
| lem:iii-i13-2-3 | background 0 at (0, p⃗_b), so every K⁺-order | α′ fixed in (2, min(3, 2 + w_0)) (41:1617), may be taken below τ_0 |

Each level is below τ_0, so it has no transition face round by (6) of Step 1 of lem:cs-rest.

**The departures are justified.**
- lem:iii-i13-2-3 is added: (d) uses its reference-point term.
- α_0 is fixed for the lemma bases, since def:cs-choices (f) fixes it only for thm:iii-i11-4-1.
- The generic α′ is dropped, as it clashed with the specific α′ of thm:iii-i11-4-1.

### n1. Definite orders

**The text.**
- (c) says "have order 2R_base + 16".
- (d) says "has order ρ + 14, or ρ + R_base + 16".
- The *Orders* paragraph states the upward closure.

**Why it is true.** If ‖β‖_(j′) and ‖β‖_(j′+D) are small, then so are ‖β‖_j and ‖β‖_(j+D), for j′ ≥ j. So "the largest of
these orders" is now a definite number.

### n2. Line 111

**The text.** C_j now depends on a bound for ‖q′‖_(𝒬^(j+5)).

**Checked.** This is within the final constant of eq:uc-small-diff, which depends on bounds for ‖β‖_(k+14) and
‖β′‖_(k+14): the coefficient difference is read at the order k + 3, so the order needed is k + 8 ≤ k + 14.

### n3. Line 116

The term (L_(b₀) − L_b)u at a rotating b, with coefficients O(|b − b₀|), is added, as the reviewer proposed. Correct.

### n4. Lines 199–200

"as |p⃗| ≤ ‖β‖_0" is true, since ‖β‖_j = ‖h‖_(𝒳^j) + |p⃗| + ‖q‖_(𝒬^j).

### n5. Texts 3 and 6

**Text 3** is applied as given.

**Text 6.** It reads "[[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at which these results ask U small,
and with them d_NM". The rewording is justified: lem:uc-small-orders bounds orders in the background β, and
prop:uc-d-small (a) converts them into orders in U (d_* + d_F + d_Φ, d_Φ + 8).

### n6. Texts 1, 2 and 13

Applied as given. They match the proof of thm:iii-k-3-2, which takes "d the largest of the d's of [[lem:iii-k-2-2]],
[[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]]" (46:1550–1551).

### n7. The order m, lines 216–218

**The text.** "the largest regularity ρ of the seminorms … and the condition asked in that seminorm has an order at least
m + 14 by (c) and (d)".

**The departure is justified.** The largest seminorm may lie in two places other than a level:
- at a base, where (c) assigns 2R_base + 16 ≥ ρ + 14, as ρ ≤ 2R_base + 2;
- at a reference point, where the seminorm is ‖·‖^+ at regularity ρ + 2 + R_base, and (d) assigns
  ρ + R_base + 16 = (ρ + 2 + R_base) + 14.

**Agreement with chapter 46.** Chapter 46 reads m as the order of the seminorm in which the e_S terms must be small
(46:1386–1390, 1449–1452). Those terms enter every level and the base, so the largest regularity is the right reading.

## Point 2: m3, the bound T_12 + 3

**Exact values.**
- T_12 + 3 = 214,558,790,360,104,032,305,147,901,608,827,147.
- T_12 + 3 = D_* − 11 < D_*.

**The bound is right for both conventions.** Their uses lie in the bases, at the levels and in Steps 4′ and 4 (table under
m3 above). The largest use is the C^rot read of Step 4′ and Step 4, charged T_12 − 11.

**Why "q small" fits under it.** It enters through R_q and Δ_q, bounded by C‖q‖ in the same seminorms (lem:iii-i14-2-3,
lem:iii-i14-2-4). It also enters through e_rows in ‖·‖^+_(𝒴(α_1)) (eq:s25-motions-small).

**The printed text** uses only "at most D_*". That holds.

## Point 3: m5 against chapter 36 as it stands

**The three results.**
- prop:iii-c-4-4 asks ‖h‖_(H^(3,a₀,a_I)_b) < ε₀ "with ε₀ depending on a₀, a_I and g₁, and not on k" (36:422–425,
  unchanged by a3877611 in this respect).
- prop:iii-c-5-2 asks h "small as in [[prop:iii-c-4-4]]", and away from U "small in H³" (36:542–553).
- cor:iii-c-5-3 asks h "small as in [[prop:iii-c-4-4]]" (36:581–582).

**Their use.** lem:iii-k-2-2 (c) applies cor:iii-c-5-3 with g_0 = ĝ and h = χ_−h_(−S,−S⁰) + h̃ (46:1287). So the
smallness it asks is the order 3 of h, which in U is the order 3 of the tail h̃, together with |U_0|.

**The sentence is literally true.** "whose smallness is read at an order at most 5 ([[prop:iii-c-4-4]])" holds, since
3 ≤ 5. So d := d_Φ + 8 serves, as 3 < 1,038,326,399,999,948.

**The other order in the sentence.** cor:iii-i-4-2 asks small H^(3,(1,0,0))_b-norm (38:500–501), which is order 3, as
stated.

**The fixer's flag is resolved.** It said prop:uc-d-small (a) relies on the low-order form. P-36-c44 (14a9a082) provides
that form, and R-P-36-c44 (a3877611) confirmed it.

## Point 4: lem:uc-small-orders (c) against chapters 40 and 44 as repaired

### The two second seminorms

**‖·‖^+_(𝒴(α)) of sec:iii-i8-1.** It is fixed in the proof of prop:iii-i8-4-1 (40:1165–1170). It is the quotient norm at
a regularity at least those of ‖·‖_(𝒴(α″)) and ‖·‖^+_(𝒴(α′)), the latter the seminorm of (i) at α′ for ‖·‖_(α′), whose
regularity is that of ‖·‖_(𝒴(α″)) plus 2.

For a base (one step α_0 → α_1), under the fine reading:

| Seminorm | Regularity at most | Why |
|---|---|---|
| ‖·‖_(𝒴(α_1)) | R_base | read by a base map, bounded from the order R_base |
| ‖·‖_(α_0) | R_base + 2 | regularity of ‖·‖_(𝒴(α_1)) plus 2 |
| ‖·‖^+_(𝒴(α_0)) | 2R_base + 2 | ‖·‖_(α_0) plus at most R_base for the α_0 base map |
| ‖·‖^+_(𝒴(α_1)) | 2R_base + 2 | the larger of the above |

This is (c)'s "exceeds that of a norm above by at most 2 + R_base", reading "a norm above" as a fixed norm at its read
regularity R_base.

prop:iii-i15-2-5 also takes ‖·‖^+_(𝒴(α_1)) as the seminorm of (i) at α_1 for its induction bound at k = 0 (44:319–331).
That bound measures the solution in the hypothesis seminorm of level 1.
- β_1 − α_1 < α − 4 ≤ ε_K, so β_1 < 3.
- The level-1 read regularity is therefore at most 486 + 20,565,307,838 < I_lev.
- This adds at most R_base + I_lev + 2 < 2R_base + 2.
- So the bound holds even if that literal choice is kept. Under the fine reading (F2) supplies it anyway.

**‖·‖^+_𝒴 of (2) of the proof of prop:iii-i15-2-12** (40:589–592). Its regularity is that of ‖·‖_𝒴 plus 2 plus the
forward-solution loss of lem:iii-i7-2-5 (c), which is within R_base. So it too is at most 2R_base + 2.

### The added uses

- **lem:iii-i8-2-6 (c).** It is cited by the repaired sec:iii-i8-1 (40:755–757).
- **The bound behind eq:s25-motions-small.** It is ‖e_rows(W⃗)‖^+_(𝒴(α_1)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|W⃗|, "d
  and the order of the seminorm of q being large" (44:357–386).
- The text now lists both, with ‖q‖ added. Both are of the kinds that (F1) turns into ‖β − β′‖_(ρ+11).

**No order moves.** (c) stays at 2R_base + 16; D_* and D′_* are unchanged.

### Where the base bound does not apply

These seminorms are covered elsewhere, as the fix report says.

**The reference point inside a level comparison** (lem:iii-i11-3-3, lem:iii-i13-2-3):
- The second seminorm of (i) at α′ has regularity up to ρ + 2 + R_base.
- (d) counts it, at ρ + R_base + 16.
- Under rem:uc-small-reading it is at most ρ_1 + 2 + R_base. The remark's base bound ρ_1 + 2R_base + 4 covers this.

**Step 4′:**
- thm:iii-i11-4-1 applies (i) at α′ with regularity at most C_lev − 11 + I_lev + 2 + R_base = T_11 − 31.
- This lies within (d)'s ρ < T_12.
- Under rem:uc-small-reading it is within ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev.

### One wording point, from the newest chapter 40

Since 75bcfa65, sec:iii-i8-1 distinguishes "the bounds and the continuity" of lem:iii-i8-2-6 (b)–(c). Item (c) of that
lemma states continuity, not a bound. The text lists it under "bounds of background terms by ‖h‖ + |p⃗ − p⃗_b|". That is
covered by (F1), which turns the continuity into such a bound, but it should say so. This is nit N1 below.

## New finding

### N1 (nit). lem:uc-small-orders (c) proof, lines 165–167: lem:iii-i8-2-6 (c) is a continuity statement, not a bound

**The problem.** The proof of (c) lists "bounds of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), as in
[[lem:iii-i8-2-6]] (b)–(c)". lem:iii-i8-2-6 (c) states continuity in (h, p⃗) (40:865). The repaired sec:iii-i8-1 now
names "the bounds and the continuity used below" (75bcfa65).

**Effect.** None on any order: by (F1) the continuity is a bound by ‖β − β′‖_(ρ+11), as the next sentence of the proof
says for "the first two kinds".

**Replacement.** Replace lines 165–167:

```
proofs ask: bounds of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), as in [[lem:iii-i8-2-6]] (b)–(c),
[[lem:s21-motions-at-b]], [[lem:iii-i15-2-7]] and (1) of the proof of [[prop:iii-i15-2-12]], and with ‖q‖ added in the
bound by which the proof of [[prop:iii-i15-2-5]] obtains [[eq:s25-motions-small]]; the counts
```

by:

```
proofs ask: bounds of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), and their continuity, as in [[lem:iii-i8-2-6]]
(b)–(c), [[lem:s21-motions-at-b]], [[lem:iii-i15-2-7]] and (1) of the proof of [[prop:iii-i15-2-12]], and with ‖q‖
added in the bound by which the proof of [[prop:iii-i15-2-5]] obtains [[eq:s25-motions-small]]; the counts
```

**Checked.**
- The old block occurs once.
- Lengths are 119, 114 and 106 characters in source, and 112, 89 and 84 after resolution with the merged numbering.
- No line starts with a forbidden marker.

## Point 5: numbers recomputed

All were computed exactly in Python integers and fractions. Each agrees with the printed value.

**From chapter 71's inputs** (N_ι, N̄_Λ = 16,747,199,999,999, R_b = 61,038,200,000,000, ε_K, ε_Υ, D_e, M_c, C_*):

| Quantity | Exact value |
|---|---|
| C_lev | 214,558,790,360,052,785,818,485,009,600,000,520 |
| k̄_max | 12,811,621,665,714,434,999,187 |
| I_lev | 34,268,829,852 |
| I_base | 1,435,970,471,299,470,574,962 |
| X_12 | 51,246,486,662,857,739,996,772 |
| T_11 | 214,558,790,360,054,221,788,956,343,339,427,453 (< T_12 − 11) |
| T_12 | 214,558,790,360,104,032,305,147,901,608,827,144 |
| D_acc | 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 (< 1.57157·10⁵⁰) |
| 21D_acc + 6 | 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 (< 3.30029·10⁵¹) |
| d_Φ ≤ 62N̄_Λ + 2 | 1,038,326,399,999,940 |
| d_Φ + 8 | 1,038,326,399,999,948 |
| Bound of eq:cs-cstar | 643,676,388,469,322,172,480,826,383,357,103,759 (< C_*) |

**lem:cs-sharp.**
- Δβ_0 = 0.999²ε_K = 16,383,184,416·10⁻²⁴, and Δτ_0 = 0.999ε_Υ = 1.4604381·10⁻¹⁰.
- (2 + ε_K)/Δβ_0 = 62,500,000,000,000,513,000,000/511,974,513 = 122,076,389,376,829.22…
- 16,383,184,416·K̄ = 2,000,000,000,000,012,824,296,864.
- 16,383,184,416·(K̄ + 1) = 2,000,000,000,000,029,207,481,280.
- So K ≤ K̄ = 122,076,389,376,829 < 1.22077·10¹⁴.
- 16,383,184,416·61,038,194,688,415 = 1,000,000,000,000,014,603,740,640 > 10²⁴.
- N_b ≤ 1/Δβ_0 + 1 = 61,038,194,688,415.11… < R_b.
- K̄C_lev = 26,192,562,436,215,228,354,699,390,649,792,285,562,280,875,951,080.
- 469R_b = 28,626,915,800,000,000, and 466(R_b + 1) = 28,443,801,200,000,466; their sum is 57,070,717,000,000,466.
- **D_♭ = 26,192,562,436,215,872,034,699,391,908,492,342,632,997,875,951,546** < 2.6193·10⁴⁹ (also < 2.62·10⁴⁹, as text 12
  states).

**lem:uc-small-orders.**
- k̄_0 = 20,602 + 466R_b = 12 + 20,590 + 466R_b = 28,443,801,200,020,602.
- max(20,180, k̄_0 + 2, 20,197) = k̄_0 + 2.
- 1/(2Δβ_0) + 1 = 30,519,097,344,208.06 < R_b.
- R_base = 1,435,970,471,299,470,597,059.
- 2R_base = 2,871,940,942,598,941,194,118, and 2R_base + 16 = 2,871,940,942,598,941,194,134 < T_12.
- 20,183 and k̄_0 + 5 are less than R_base.
- 16·1,470,302 + 3·6,847,261,002 = 23,524,832 + 20,541,783,006 = 20,565,307,838 < I_lev, and with 497 added still below.
- 1/Δτ_0 + 1 = 6,847,260,422.38 < 6,847,261,002.
- C_lev − 11 + I_lev + X_12 = T_12 − 11.
- C_lev − 11 + I_lev + R_base + 16 = C_lev + I_lev + R_base + 5 < D_*.
- X_12 > R_base, and X_12 − R_base − 2 = 4.981·10²².
- **D_* = T_12 + 14 = 214,558,790,360,104,032,305,147,901,608,827,158** < 2.14559·10³⁵.
- **m3:** T_12 + 3 = D_* − 11.
- The reviewer's max(2R_base + 16, C_lev + I_lev + 3) equals C_lev + I_lev + 3, which is less than T_12 + 3.

**rem:uc-small-reading.**
- K̄(C_lev + I_lev − 9) = 26,192,562,436,215,228,354,699,394,833,207,300,964,646,683,858,927.
- The step 2 + C_lev − 11 + I_lev equals C_lev + I_lev − 9.
- ρ_1 = T_12 + K̄(C_lev + I_lev − 9), and ρ_1 + 2R_base + 18 = D′_*.
- **D′_* = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207** < 2.6193·10⁴⁹.

**prop:uc-d-small, fine reading.**
- D_♭ + D_* = 26,192,562,436,216,086,593,489,752,012,524,647,780,899,484,778,704.
- Adding d_Φ gives **26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644** < 2.6193·10⁴⁹ (leading digits
  2.619256).
- 21 times that plus 6 is 550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 < 5.5005·10⁵⁰ (5.500438).

**prop:uc-d-small, cumulative reading.**
- D_♭ + D′_* = 52,385,124,872,431,314,948,189,146,848,603,889,688,145,109,831,753.
- Adding d_Φ gives **52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693** < 5.2386·10⁴⁹ (5.238512).
- 21 times that plus 6 is 1,100,087,622,321,057,613,911,972,083,820,681,705,255,901,706,465,559 < 1.10009·10⁵¹
  (1.100087).
- D_acc minus the cumulative bound is 104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307 > 0.
- So d_NM < D_acc and N_NM < 21D_acc + 6 under either reading.

**m6.** 3(1/Δτ_0 + 1) = 20,541,781,267.1 < 2.06·10¹⁰.

**Whether the headline bounds stand.** They do:
- d_NM < 5.2386·10⁴⁹ < D_acc < 1.57157·10⁵⁰ under every reading the text allows;
- N_NM < 1.10009·10⁵¹ < 21D_acc + 6 < 3.30029·10⁵¹;
- every lower bound holds for d_NM, since d_NM ≥ d_R ≥ d_acc.

## Point 6: placement

### The old texts

All 20 old texts of texts 1–14 were located in the current chapter 71 with whitespace-insensitive matching. Each occurs
exactly once:
1, 2, 3, 4, 5, 6, 7a, 7b, the title of 8, its line, its proof, 9, 10a, 10b, the display of 11, its line, its proof, 12, 13
and 14.

- The end text of 8 ("21d_NM + 6 is the regularity of") occurs twice in the chapter, but only once after the unique start
  text, so the span is unambiguous.
- Every "lines" and "paragraph" span begins and ends on line boundaries.
- The stated line counts are right: text 2 has four lines, texts 3, 7b and 13 two, and texts 4, 6, 8 (proof), 11 (proof)
  and 12 three.

### The merge

All 14 texts were applied in memory, and the subsection (proof lines 1–301) was inserted before the heading of
sec:ec-linear. `assemble.number` and `assemble.resolve` were then run with the merged chapter swapped in:
- problems 0 and 0;
- labels 4579, that is 4570 + 9;
- new labels:
  - sec:cs-small = Section 49.12.7;
  - lem:cs-sharp = Lemma 49.107, lem:uc-small-orders = Lemma 49.108;
  - rem:uc-small-reading = Remark 49.109, prop:uc-d-small = Proposition 49.110;
  - eq:cs-sharp, eq:uc-small, eq:uc-small-diff and eq:uc-d-small = (49.51)–(49.54).

Five labels after the insertion renumber, as they must: lem:ec-test-function, eq:ec-test-function,
rem:ec-lower-bounds-observed, rem:ec-linear-observed and rem:ec-not-evaluated. No chapter cites a result by a hard-coded
number.

**Lint.** `lint.py --chapters` on a scratch tree with the merged chapter gives 0 hits over 62 files and 4579 labels.

### Each new text read in place, all true

- **Texts 1, 2 and 4.** thm:loss-d's definition and its proof read correctly. d_NM ≥ d_acc still follows. (ii) and (iii)
  speak of d_acc only.
- **Text 5.** "d ≥ d_R ≥ d_acc" holds by eq:uc-d-small and the proof of thm:loss-d. The proof of prop:ec-delta-cap uses
  d ≥ d_acc only.
- **Texts 3 and 6.** See n5 above.
- **Texts 7, 8, 9 and 10.** These are true, and lem:uc-dr (10a) is now trivially true.
- **Text 11.**
  - d_R ≤ D_acc is lem:uc-dr with the same first line.
  - d_NM ≤ D_NM is prop:uc-d-small (d).
  - The finer bounds are lem:cs-sharp and (b), (c) there. d_NM < 5.2386·10⁴⁹ holds under both readings.
- **Text 12.** d_acc, d_R < 2.62·10⁴⁹ is lem:cs-sharp.
- **Text 13.** "the d of [[thm:iii-k-3-2]]" matches 46:1550.
- **Text 14.** See m4 above.

### Sentences elsewhere: none becomes false

**Chapter 71.** The untouched sentences on d_NM stay true:
- the order of choices (71:390);
- the sentence that thm:uc-integer bounds d_NM from above (396);
- cor:uc-two-offsets (2080–2081, 2091);
- eq:uc-lower (2487);
- thm:uc-reduction, whose (ii) now reads "≥" and whose closing sentence rests on thm:uc-integer.

**Chapters 00 (line 34), 01 (151–154), 03 (351–354) and 90 (60–72).** Each speaks of "the loss d with which the
settling proof applies the Nash–Moser theorem", that is, the d of thm:iii-k-3-2. That d is d_NM. Each statement holds:
- the upper bounds by prop:uc-d-small (d);
- the lower bounds by d_NM ≥ d_acc;
- 03's "at least the loss that the proof assigns to the tame estimates" by d_NM ≥ d_acc.

**Chapter 46.** It takes d as "the d of [[thm:iii-k-3-2]]", the largest of the three d's (1251, 1550). Its
*The constants* asks the d of lem:iii-k-2-3 at least d_R, d′_0, d_BG and m + 5. This agrees with prop:uc-d-small (a).

No chapter other than 71 uses the symbol d_NM.

## Point 7: contract

**Line lengths.**
- The proof file: at most 121 characters in source, and 121 after resolution with the merged numbering.
- The merged chapter 71: at most 121 in source and after resolution. The only 121-character new line is text 10's, as the
  Placement states.

**Wrapped lines.** No wrapped line of the proof file, or of any new or changed line of the merged chapter, starts with
"+ ", "- ", "* ", "> ", "#", "=" or "|". The two lines starting "#" are the headings. No wrapped line starts with a
numeral and ". ".

**Text.** No backslash. Every label key is lowercase. No file, program, code or AI language.

**`python3 lint.py proofs/P-U71-small.md`.** 325 hits, all "reference to undefined label": the single-file limitation.
Every reference resolves in the merge.

**`python3 assemble.py --check`.** Run at a3877611 from the paper directory. Last line:
`labels 4570, computations cited 0, problems 0`.

## Observations outside the text (not counted)

**O1. m5's clause can be made exact.** With prop:iii-c-4-4 now asking the order 3, "whose smallness is read at an order
at most 5" could read "at the order 3". The text as written is true and robust to further changes in chapter 36.

**O2. Chapter 62 (rem:half-class-changes, 62:577).** It cites "the loss d ([[thm:loss-d]])" as the same in the
half-integer class.
- The next sentence says the logarithmic orders may rise and enter l_* and k̄(λ). These already enter d_acc, through the
  counts n(E, β).
- The redefinition of d_NM neither adds to this tension nor removes it.
- It predates the fix round and lies outside the six chapters checked. It is noted only because it cites thm:loss-d.

**O3. Short source lines.** Texts 4 and 5 leave short source lines inside their paragraphs ("[[eq:iii-j2-4-2]] for it.
By" and "and let the Nash–Moser"). This is within the contract and invisible after assembly.
