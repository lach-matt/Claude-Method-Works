# F-P-U71-small: report

Base: proofs/P-U71-small.md as reviewed (85bcfe80, 409 lines). Final: 438 lines. Only that file was edited. Nothing was
committed by me. Note: the coordinator's snapshot commits a903f977, c60dca6c and 6fe263d9 already hold most of this
work, so `git diff` against HEAD shows only the last one-line change. The full diff against the reviewed text
(`git diff 85bcfe80 -- …/proofs/P-U71-small.md`) is at the end.

## Outcome

- **The headline bounds stand unchanged:** d_NM ≤ D_NM := D_acc < 1.57157·10⁵⁰ and N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹.
  So do D_*, D′_*, D_♭, the fine bound d_NM < 2.6193·10⁴⁹ (N_NM < 5.5005·10⁵⁰), the reading-free bound
  d_NM < 5.2386·10⁴⁹ (N_NM < 1.10009·10⁵¹) and every lower bound. No integer in the text changed.
- All 6 minors and 7 nits are applied. Five depart from the reviewer's text: m3, m5, m6, n5 and n7. Each is explained
  below.
- **Chapter 40 check.** (c) did not name the new second seminorms. It now does, with the regularity bound and the uses
  that the repaired chapters 40 and 44 add. No order moves.
- **Placement.** There are now 14 replacement texts with 20 old texts, and each old text occurs exactly once in the
  current chapter 71. Two errors in the instructions are fixed: text 2 spans four lines, not three, and text 10's first
  line becomes longer (121 characters), not shorter.

## Findings

**m1 (applied, reworded).** prop:uc-d-small now defines d_* as the largest of the orders of the smallness conditions
named in the proof of lem:iii-j2-2-3, "the fixed seminorms being those of lem:uc-small-orders (d) or those of
rem:uc-small-reading". (b) opens "for the fixed seminorms of lem:uc-small-orders (d)" and (c) opens "for those of
rem:uc-small-reading". (a), (d), the proof and the closing paragraph stand as written. Deviation: I did not use the
reviewer's "…(d) in (b) and for those of … in (c)". (a) also uses d_* and holds under both readings, so the definition
should not depend on the item.

**m2 (applied).** In (e): of the conditions of (d), one read at a reference point (0, p⃗_b) with b ≠ b₀ occurs only at a
level. The reason: Step 4′ is a step of thm:iii-i14-3-1, which is stated at b = b₀, and at a rotating b
prop:iii-i15-2-5 has no Step 4′. I verified this against chapter 42 (thm:iii-i14-3-1 "(b = b₀)") and chapter 44, and
added the pointer [[sec:s23-base-points]], whose item (2) says "Step 4′ of the proof of thm:iii-i14-3-1 is not used at
b". Step 4 at b is the bound cor:iii-i15-2-10 and makes no comparison.

**m3 (applied, with a correction to the reviewer's analysis).**
- The conventions are now treated in (e). "h small" (sec:iii-i7-1, kept in sec:iii-i8-1, in sec:iii-i9-1, and so at
  the base points of ch:s22) and "q small" (sec:iii-i14-1) each fix one order for all their uses: the largest of the
  orders those uses ask. The uses lie in the bases, at the levels and in Steps 4′ and 4, and each asks an order that
  (a)–(d) bound.
- **Correction.** The reviewer bounds the convention by max(2R_base + 16, C_lev + I_lev + 3). That is too low. The base
  points of ch:s22 are those of sec:iii-i9-2 (sec:s22-setting), where "h small" is as in sec:iii-i8-1. So the same
  convention also covers:
  - the level reads at reference points (C_lev + I_lev + R_base + 5);
  - the reads of thm:iii-i11-4-1 and thm:iii-i12-3-1 in Steps 4′ and 4, charged at most T_12 − 11, so of order at most
    T_12 + 3.
- **The bound that holds** is T_12 + 3 = D_* − 11, for both conventions; "q small" covers R_q and Δ_q in the same
  seminorms.
- So the order of each convention is at most D_*, and D_*, D′_* and the bounds on d_NM are unchanged. Under
  rem:uc-small-reading the conventions are at most D′_*. The remark now cites "the proofs of (c)–(e)".
- The proof text has no table. The writer's report table (notes/reports/P-U71-small.md) wrongly gives the rows
  "ch:s21 'h small'" and "ch:s23 'q small'" as ≤ 2R_base + 16; the right entry is ≤ T_12 + 3 < D_*. I did not edit that
  file.

**m4 (applied as text 14).** One sentence is appended to rem:uc-missing: "The bound for d_NM rests in addition on the
orders of the smallness conditions, which lem:uc-small-orders bounds for the fixed seminorms of its (d), and
rem:uc-small-reading for the larger ones that sec:iii-i8-1 describes (prop:uc-d-small)." The old line occurs once. The
Placement paragraph now mentions text 14.

**m5 (applied, last clause changed).**
- The pointer is fixed. The line now reads: at ℐ⁺ through cor:iii-i-4-2 for Φ(U) (thm:iii-j-2-4), which asks the order 3
  of h + h_rem(q) + h_tot(p⃗), and through cor:iii-c-5-3 for Ψ(U) (lem:iii-k-2-2 (c)), "whose smallness is read at an
  order at most 5 (prop:iii-c-4-4)". I checked lem:iii-k-2-2 (c): it applies cor:iii-c-5-3 near ℐ⁺ ∩ {t^♭_* ≤ T̂ + 2},
  and cor:iii-i-4-2 through cor:iii-j3-6-6 for t^♭_* > T̂ + 2.
- Deviation: I did not use "read at its order 5". This is the reviewer's observation O1, which the text depends on:
  - committed chapter 36 asks smallness in H^(k,a₀,a_I) at the order k of each membership, with ε₀ depending on k;
  - read literally, d := d_Φ + 8 in prop:uc-d-small (a) then needs the low-order form for lem:iii-k-2-2.
- Chapter 36 is being repaired in the working tree right now (uncommitted, another worker). That repair makes
  prop:iii-c-4-4 ask smallness in H^(3,a₀,a_I) only, with ε₀ independent of k. My wording is true under that repair
  (order 3 ≤ 5). Under the committed text it is an explicit reading at k = 5.
- In U the order is 5: h̃ is the tail of U, and the H^5 norm of h̃ is part of ‖U‖_(𝒟^5_ex). That is below d_Φ + 8, so
  no number moves.
- **Flag for the coordinator:** prop:uc-d-small (a) relies on O1 being resolved in the low-order form.

**m6 (applied, list completed).**
- A base is now prop:iii-i8-4-1, with its forward solution, at a level in (2, 3) reached from α_0 by one level step
  without transition face round, for a background of K⁺-order at least a♭_K. The bases used are:
  - that of Step 1 of thm:iii-i14-3-1 at α_1 (at b also in prop:iii-i15-2-5);
  - that of thm:iii-i11-4-1 at the α′ of def:cs-choices (f);
  - those of lem:iii-i11-3-3 **and lem:iii-i13-2-3**. For these, α′ is taken below 2 + ε_g − 2ε, with one level step
    from an admissible α_0 ∈ (2, α′).
- Each level is below τ_0 = 2 + ε_g − 2ε, so it has no transition face round, by (6) of Step 1 of lem:cs-rest.
- Deviations:
  - **lem:iii-i13-2-3 is added.** Its proof fixes its own admissible α′ ∈ (2, min(3, 2 + w_0)), and (d) uses its
    reference-point term. The reviewer listed only three bases.
  - α_0 is fixed explicitly for the two lemma bases, since def:cs-choices (f) fixes it only for thm:iii-i11-4-1.
  - The generic "α′" of the reviewer's text is dropped. It clashed with the specific α′ of thm:iii-i11-4-1.
- Checked: at the base point (0, p⃗_b) the background is 0, so every K⁺-order is allowed, and α_0 < α′ < 2 + ε_g < 5/2.
  So prop:iii-i8-4-1's proof allows the single step.

**n1 (applied).** (c) now says "have order 2R_base + 16", and (d) says "has order ρ + 14, or ρ + R_base + 16". The Orders
paragraph now states the upward closure the nit relies on: "a condition of order j has order j′ for every j′ ≥ j".

**n2 (applied as given).** Checked: the difference h_(b,rem)(q) − h_(b′,rem)(q′) has the part
(h_(b,rem) − h_(b′,rem))(q′) = O(|b − b′|)‖q′‖_(j+5), and ‖q′‖_(k+8) ≤ ‖β′‖_(k+14), as the final constant allows.

**n3 (applied as given).** Checked: L_(h,p⃗) − L_b = (L_(h,p⃗) − L_(b₀)) + (L_(b₀) − L_b). The first term is (F1) with
β′ = 0 (F3). The second has fixed coefficients of size O(|b − b₀|).

**n4 (applied).** I used the reviewer's text with "as" added: "is such a bound, as |p⃗| ≤ ‖β‖_0, its component
|b − b₀| being also made small by the choice of ℬ_*".

**n5 (applied, text 6 reworded).**
- Text 3 is applied as given.
- In text 6 I wrote "[[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at which these results ask U
  small, and with them d_NM". The reviewer had "lem:uc-small-orders bounds the orders at which these results ask U
  small". That lemma bounds the background orders (d_*); prop:uc-d-small (a) turns them into the orders in U.

**n6 (applied as given)** for texts 1, 2 and 13. Checked: the three lemmas are existential, and prop:uc-d-small (a)
fixes their d's.

**n7 (applied, final clause corrected).** m is now "the largest regularity ρ of the seminorms in which the proof of
lem:iii-j2-2-3 asks R_j → 0". The reviewer added "and those conditions have the orders ρ + 14 by (d)". I wrote instead:
"the condition asked in that seminorm has an order at least m + 14 by (c) and (d)".
- The largest seminorm need not be a level one.
- At the base, (c) assigns 2R_base + 16 ≥ ρ + 14.
- At a reference point, (d) assigns ρ + R_base + 16, the seminorm there being ‖·‖^+ at ρ + 2 + R_base.

This also settles the chapter 46 point of P-40-sem and R-P-40-sem: reg ‖·‖^+_(𝒴(α_1)) ≤ 2R_base + 2 is far below d − 5.

## Chapter 40 (14817ece, 85bcfe80, and 06988e45, which landed during this run)

- **The claim "regularity at most 2R_base + 2" is right for the base norms under the fine reading.**
  - ‖·‖^+_(𝒴(α_0)) bounds the α_0 base map into ‖·‖_(α_0), whose regularity is that of ‖·‖_(𝒴(α_1)) plus 2 (at most
    R_base + 2). The map adds at most R_base. So the regularity is at most 2R_base + 2.
  - ‖·‖^+_(𝒴(α_1)) is taken at the larger of the two.
  - ‖·‖^+_𝒴 of prop:iii-i15-2-12 (2) has regularity at most reg ‖·‖_𝒴 + 2 + 20,183.
  - Each of these has order at most 2R_base + 16.
- **The claim is not true everywhere.**
  - At a reference point inside a level comparison (lem:iii-i11-3-3, lem:iii-i13-2-3), the second seminorm of (i) at
    α′ has regularity up to ρ + 2 + R_base. (d)'s ρ + R_base + 16 already counts it.
  - In Step 4′, thm:iii-i11-4-1 applies (i) at α′ with a target at least the w_0 seminorm. That seminorm has regularity
    at most C_lev − 11 + I_lev + 2 + R_base ≤ T_11, within (d)'s ρ < T_12.
  - Under the cumulative reading the base norms are at most ρ_1 + 2 + R_base, and ρ_1 + 2R_base + 4 with the reference
    terms, as rem:uc-small-reading already states.
- **What changed in the text.**
  - The repaired sec:iii-i8-1 asks d large for the bounds by ‖h‖ "in these seminorms", the second ones included, and
    (i) now carries "d being large for ‖·‖_(α)". prop:iii-i15-2-5 now bounds e_rows in ‖·‖^+_(𝒴(α_1)), "d and the
    order of the seminorm of q being large".
  - These are smallness uses that (c) did not mention. (c) now:
    - names the second norms ‖·‖^+_(𝒴(α)) and ‖·‖^+_𝒴, whose regularity exceeds that of a fixed norm by at most
      2 + R_base, so they are at most 2R_base + 2;
    - lists them among "these norms";
    - adds lem:iii-i8-2-6 (c), which the repaired sec:iii-i8-1 now cites;
    - adds the bound behind eq:s25-motions-small, with ‖q‖.
- No order, D_*, D′_* or d_NM bound moves.

## Numbers recomputed (exact integers and fractions; all assertions pass)

All printed integers are unchanged. Each was recomputed from N_ι, N̄_Λ, R_b, ε_K, Δβ_0, Δτ_0, D_e, C_* and M_c:
- C_lev, k̄_max, I_lev, I_base, D_acc, 21D_acc + 6 and d_Φ ≤ 1,038,326,399,999,940;
- (2 + ε_K)/Δβ_0 = 62,500,000,000,000,513,000,000/511,974,513 = 122,076,389,376,829.22…, so K ≤ K̄;
- the two products 16,383,184,416·K̄ and 16,383,184,416·(K̄ + 1), and 16,383,184,416·61,038,194,688,415 > 10²⁴;
- K̄C_lev, 469R_b + 466(R_b + 1) = 57,070,717,000,000,466, and D_♭ (< 2.6193·10⁴⁹);
- k̄_0 = 28,443,801,200,020,602 = 12 + 20,590 + 466R_b;
- R_base = 1,435,970,471,299,470,597,059, 2R_base, and 2R_base + 16 = 2,871,940,942,598,941,194,134;
- X_12, T_11 < T_12 − 11, T_12, and D_* = 214,558,790,360,104,032,305,147,901,608,827,158 < 2.14559·10³⁵;
- C_lev − 11 + I_lev + R_base + 16 = C_lev + I_lev + R_base + 5 < D_*, and 23,524,832 + 20,541,783,006 < I_lev;
- K̄(C_lev + I_lev − 9) and D′_*. The recursion ρ_1 = T_12 + K̄(C_lev + I_lev − 9) and ρ_1 + 2R_base + 18 = D′_* were
  checked exactly;
- the fine and cumulative sums, 21x + 6 for each, and D_acc minus the cumulative bound
  (104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307).

New checks for this round:
- **m3, the largest use of a convention.** It is T_12 + 3 = D_* − 11. The reviewer's
  max(2R_base + 16, C_lev + I_lev + 3) = C_lev + I_lev + 3 omits the ch:s22 uses.
- **The second seminorms at the base.** R_base + 2 + R_base = 2R_base + 2, and plus 14 this is 2R_base + 16.
- **m6.** 3(1/Δτ_0 + 1) = 20,541,781,267.1… < 2.06·10¹⁰. The slack in (e) is X_12 − R_base − 2 ≈ 4.98·10²². The review
  writes ≈ 5.1·10²², which is X_12 itself; the conclusion is unaffected.

## Headline bounds

They stand: d_NM ≤ D_acc < 1.57157·10⁵⁰, N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹, and every lower bound. No correction forced
a change.

## Contract

- **Old texts.** Each of the 20 old texts of texts 1–14 was matched in an in-memory copy of chapter 71 (unchanged since
  85bcfe80) and occurs exactly once.
- **Merge.** After applying all 14 texts and inserting the subsection before sec:ec-linear, the edition's own
  numbering gives Lemma 49.107, Lemma 49.108, Remark 49.109 and Proposition 49.110, Section 49.12.7 and equations
  (49.51)–(49.54). Problems: 0.
- **Line lengths.** Every line of the proof file, and of the merged chapter 71, is at most 121 characters in source and
  after resolution. The maximum is 121, reached by text 10's line, which the Placement now states.
- **Wrapped lines.** No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". I also kept operators and the
  tuples (0, p⃗_b, 0) and (0, 0, 0) off line breaks.
- **Labels and text.** No backslash. Label keys are lowercase. No file, program, code or AI language.
- **Lint.**
  - `python3 lint.py proofs/P-U71-small.md` gives 325 hits, all "undefined label": cross-chapter references, the
    single-file limitation.
  - On a scratch tree with the merged chapter 71 (and the working-tree chapters 36, 38, 40, 41, 45),
    `lint.py --chapters` gives 0 hits over 62 files and 4579 labels, and `assemble.py --check` gives problems 0.
  - On the real tree, `assemble.py --check` gives labels 4570, problems 0.

## Diff (against the reviewed text, 85bcfe80)

```diff
diff --git a/research/warp-drive/paper/reader/proofs/P-U71-small.md b/research/warp-drive/paper/reader/proofs/P-U71-small.md
index f292c0f4..e394e4dd 100644
--- a/research/warp-drive/paper/reader/proofs/P-U71-small.md
+++ b/research/warp-drive/paper/reader/proofs/P-U71-small.md
@@ -16,9 +16,15 @@ every b ∈ ℬ̄_* ([[thm:fwd-loss]], [[cor:fwd-near-b0]]); ‖β‖_j = ‖h
 
     K̄ := 122,076,389,376,829,     R_base := 20,183 + 1,914 + I_base = 1,435,970,471,299,470,597,059.
 
-A *base* is [[prop:iii-i8-4-1]] at a level in (2, 3) for a background of K⁺-order at least a♭_K, with its forward
-solution. By [[lem:cs-iterations]] (b), with the count of Step 1 in the proof of [[lem:cs-rest]], a base with all its
-rounds, steps and windows charged is charged at most R_base along every chain.
+A *base* is [[prop:iii-i8-4-1]], with its forward solution, at a level in (2, 3) that it reaches from its α_0 by one
+level step without transition face round, for a background of K⁺-order at least a♭_K. The bases used are that of
+Step 1 of the proof of [[thm:iii-i14-3-1]] at α_1, at b also in [[prop:iii-i15-2-5]]; that of the proof of
+[[thm:iii-i11-4-1]] at the α′ of [[def:cs-choices]] (f); and those of the proofs of [[lem:iii-i11-3-3]] and
+[[lem:iii-i13-2-3]], whose admissible α′ we take below 2 + ε_g − 2ε, with one level step from an admissible
+α_0 ∈ (2, α′), as those proofs and that of [[prop:iii-i8-4-1]] allow. Each of these levels is below
+τ_0 = 2 + ε_g − 2ε, so its level step has no transition face round ((6) of Step 1 in the proof of [[lem:cs-rest]]). By
+[[lem:cs-iterations]] (b), with the count of Step 1 in the proof of [[lem:cs-rest]], a base with all its rounds, steps
+and windows charged is charged at most R_base along every chain.
 
 **Lemma {#lem:cs-sharp}** (The single-step losses summed level by level.) The number K of the levels β_1, …, β_K of
 [[thm:iii-i14-3-1]] satisfies K ≤ K̄, and
@@ -53,11 +59,12 @@ c_0; these satisfy the same bounds ([[lem:cs-levels]], [[lem:cs-base]], [[lem:cs
 D_e = 1,258,700,000,000,000,000,000,000 and C_* = 643,680,000,000,000,000,000,000,000,000,000,000 gives the integer of
 [[eq:cs-sharp]], whose leading digits are 2.619256. ∎
 
-*Orders.* We say that a condition on the background β = (h, p⃗, q) has *order j* if it holds whenever ‖β‖_j is less
-than one positive number and ‖β‖_(j+D) is less than another, D being the d of [[thm:iii-j2-4-1]]. As the norms are
-non-decreasing in the order and d_0 = d_* + D ([[lem:iii-j2-2-3]]), every condition of order at most d_* holds on the
-ball ‖β‖_(d_0) < δ_𝔹 of [[thm:iii-j2-4-1]] once δ_𝔹 is small. The bound at the order j + D is the one that the proof of
-[[lem:iii-j2-2-3]] uses when it asks the solutions u_j entering a comparison to be bounded at a fixed order.
+*Orders.* We say that a condition on the background β = (h, p⃗, q) has *order j* if it holds whenever ‖β‖_j is less than
+one positive number and ‖β‖_(j+D) is less than another, D being the d of [[thm:iii-j2-4-1]]. As the norms are
+non-decreasing in the order, a condition of order j has order j′ for every j′ ≥ j; and as d_0 = d_* + D
+([[lem:iii-j2-2-3]]), every condition of order at most d_* holds on the ball ‖β‖_(d_0) < δ_𝔹 of [[thm:iii-j2-4-1]] once
+δ_𝔹 is small. The bound at the order j + D is the one that the proof of [[lem:iii-j2-2-3]] uses when it asks the
+solutions u_j entering a comparison to be bounded at a fixed order.
 
 **Lemma {#lem:uc-small-orders}** (The orders of the smallness conditions.) At the computational point, with the index
 sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]]:
@@ -70,16 +77,15 @@ order d_T + 3 = 20,183;
 h + h_rem(q) + h_tot(p⃗);
 
 (c) the conditions that [[ch:s20]], [[ch:s21]] and [[prop:iii-i8-4-1]] place on the background of a base, at a base
-point with parameter b ∈ ℬ̄_* included ([[prop:iii-i15-2-8]], [[prop:iii-i15-2-12]]), have order at most
-2R_base + 16;
+point with parameter b ∈ ℬ̄_* included ([[prop:iii-i15-2-8]], [[prop:iii-i15-2-12]]), have order 2R_base + 16;
 
 (d) let the fixed seminorm of the forcing class of a level β of [[thm:iii-i14-3-1]] (in [[lem:iii-i8-3-2]],
 [[lem:iii-i11-3-2]], [[lem:iii-i13-2-2]], [[def:iii-i15-2-3]], [[lem:iii-i15-2-4]] and Step 3 of the proof of
 [[prop:iii-i15-2-5]]), and the seminorm in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0, be taken at the
 regularity ρ at which the maps that read the coefficients from the forcing of the step are bounded. Then
 ρ ≤ C_lev − 11 + I_lev at the levels, and ρ < T_12 in Steps 4′ and 4; and every condition of Steps 2–4′ of the proofs
-of [[thm:iii-i14-3-1]] and [[prop:iii-i15-2-5]] has order at most ρ + 14, or ρ + R_base + 16 when it is read at a
-reference point (0, p⃗_b) with b ≠ b₀;
+of [[thm:iii-i14-3-1]] and [[prop:iii-i15-2-5]] has order ρ + 14, or ρ + R_base + 16 when it is read at a reference
+point (0, p⃗_b) with b ≠ b₀;
 
 (e) hence every condition named in the proof of [[lem:iii-j2-2-3]] has order at most
 
@@ -102,16 +108,17 @@ the integral over the segment of ∂_(p⃗)Φ_γ·(p⃗ − p⃗′) + ∂_wΦ_
 a function smooth in (x, p⃗) plus one vanishing at w = 0; so [[lem:ii-g-4-1]] (2)–(3) with d = 3 bound the difference at
 the order j by C_j(‖w − w′‖_j + |p⃗ − p⃗′| + ‖w_s‖_(j+6)(‖w − w′‖_0 + |p⃗ − p⃗′|)), w_s on the segment. The product with
 D^γ_bu is bounded by [[lem:ii-g-4-1]] (2), which reads the coefficient at the orders 3 and k + 3. As
-‖w − w′‖_j ≤ C_j‖β − β′‖_(j+5), h_tot(p⃗) being smooth in p⃗ and h_(b,rem)(q) linear in q and smooth in b, and
-‖w_s‖_j ≤ C_j(‖β‖_(j+5) + ‖β′‖_(j+5)), this gives [[eq:uc-small-diff]]. The weights and the coefficients at the faces
-are treated as in the proof of [[prop:uc-dbg]].
+‖w − w′‖_j ≤ C_j‖β − β′‖_(j+5), with C_j depending on a bound for ‖q′‖_(𝒬^(j+5)), as h_(b,rem)(q) is linear in q and
+smooth in b and h_tot(p⃗) is smooth in p⃗, and ‖w_s‖_j ≤ C_j(‖β‖_(j+5) + ‖β′‖_(j+5)), this gives [[eq:uc-small-diff]].
+The weights and the coefficients at the faces are treated as in the proof of [[prop:uc-dbg]].
 
 (F2) In each comparison below, a solution u of an earlier entry of [[sec:iii-j2-3]] enters only through terms
-(A_β − A_β′)u, and is needed at the order ρ + 2, ρ the regularity of the seminorm. By the induction in the proof of
-[[thm:iii-j2-4-1]], over the entries of [[sec:iii-j2-3]] in their order and, in [[thm:iii-i14-3-1]], over its levels,
-the solution maps of the earlier entries are tame with losses at most D. Their forcings are F, which lies in every
-order, and background sources times finite-dimensional coordinates, of order-j norm at most C_j(1 + ‖β‖_(j+11)) per
-unit coordinate ([[prop:uc-dbg]]). So ‖u‖_(ρ+2) is bounded by the data of the step once ‖β‖_(ρ+13+D) is bounded.
+(A_β − A_β′)u, at a rotating b also through (L_(b₀) − L_b)u, whose coefficients are O(|b − b₀|), and is needed at the
+order ρ + 2, ρ the regularity of the seminorm. By the induction in the proof of [[thm:iii-j2-4-1]], over the entries of
+[[sec:iii-j2-3]] in their order and, in [[thm:iii-i14-3-1]], over its levels, the solution maps of the earlier entries
+are tame with losses at most D. Their forcings are F, which lies in every order, and background sources times
+finite-dimensional coordinates, of order-j norm at most C_j(1 + ‖β‖_(j+11)) per unit coordinate ([[prop:uc-dbg]]). So
+‖u‖_(ρ+2) is bounded by the data of the step once ‖β‖_(ρ+13+D) is bounded.
 
 (F3) At b₀ and the background 0, L_(0,0) = L_(b₀) ([[lem:iii-i7-2-5]] (a), [[lem:iii-i11-3-2]]), so the forcing
 f′ = G − (L − L_b)u of Step 0 of the proofs of [[lem:iii-i8-3-2]], [[lem:iii-i11-3-2]] and [[lem:iii-i13-2-2]] is G
@@ -150,15 +157,20 @@ is bounded from the order R_base into its finite-dimensional target, the coeffic
 order 0 ([[lem:cs-elem]] (a)). At a reference point (0, p⃗_b) with b ≠ b₀ the read carries also a term
 C|p⃗_b|‖u_j − u‖, which the proof of [[lem:iii-i11-3-3]] bounds by (i) of [[prop:iii-i8-4-1]] at a level below 3, a
 base map, from the forcing at the order of the seminorm plus 2 + R_base. So these norms are needed at regularities at
-most 2R_base + 2. The bounds of (i) of [[prop:iii-i8-4-1]] and of [[lem:iii-i7-2-5]] (c) enter the conditions only as
-bounds of solutions and parameters by the data of the step, which (F2) supplies. In these norms the proofs ask: bounds
-of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), as in [[lem:iii-i8-2-6]] (b), [[lem:s21-motions-at-b]],
-[[lem:iii-i15-2-7]] and (1) of the proof of [[prop:iii-i15-2-12]]; the counts ‖(L − L′)u‖ ≤ C(‖h‖ + |p⃗ − p⃗′|)‖u‖ of
-Step 0 of the proof of [[lem:iii-i8-3-2]], of the proofs of [[lem:iii-i7-4-1]] and [[prop:iii-i15-2-8]], and of (2) of
-the proof of [[prop:iii-i15-2-12]], with u bounded; and the conditions of (a) and (b). By (F1) at a regularity
-ρ ≤ 2R_base + 2, the first two kinds are bounds by ‖β − β′‖_(ρ+11), β′ being (0, p⃗_b, 0) or (0, 0, 0), so that
-‖β − β′‖_j ≤ 2‖β‖_j; their constants and the bounds of u need ‖β‖_(ρ+14+D) bounded ((F2)). So they have order at most
-2R_base + 16, as have those of (a) and (b), since 20,183 and k̄_0 + 5 are less than R_base.
+most 2R_base + 2. The bounds of (i) of [[prop:iii-i8-4-1]] and of (2) of the proof of [[prop:iii-i15-2-12]] are taken in
+second norms, ‖·‖^+_(𝒴(α)) of [[sec:iii-i8-1]] and ‖·‖^+_𝒴, whose regularity exceeds that of a norm above by at most
+2 + R_base: 2 for the count of Step 0, and R_base for the base map that bounds the solution. So they too are needed at
+regularities at most 2R_base + 2. These bounds, and those of [[lem:iii-i7-2-5]] (c), enter the conditions only as bounds
+of solutions and parameters by the data of the step, which (F2) supplies. In these norms, the second ones included, the
+proofs ask: bounds of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), as in [[lem:iii-i8-2-6]] (b)–(c),
+[[lem:s21-motions-at-b]], [[lem:iii-i15-2-7]] and (1) of the proof of [[prop:iii-i15-2-12]], and with ‖q‖ added in the
+bound by which the proof of [[prop:iii-i15-2-5]] obtains [[eq:s25-motions-small]]; the counts
+‖(L − L′)u‖ ≤ C(‖h‖ + |p⃗ − p⃗′|)‖u‖ of Step 0 of the proof of [[lem:iii-i8-3-2]], of the proofs of [[lem:iii-i7-4-1]]
+and [[prop:iii-i15-2-8]], and of (2) of the proof of [[prop:iii-i15-2-12]], with u bounded; and the conditions of (a)
+and (b). By (F1) at a regularity ρ ≤ 2R_base + 2, the first two kinds are bounds by ‖β − β′‖_(ρ+11), β′ being
+(0, p⃗_b, 0) or (0, 0, 0), so that ‖β − β′‖_j ≤ 2‖β‖_j; their constants and the bounds of u need ‖β‖_(ρ+14+D) bounded
+((F2)). So they have order at most 2R_base + 16, as have those of (a) and (b), since 20,183 and k̄_0 + 5 are less than
+R_base.
 
 *(d)* *The reads.* At a level β ∈ (3, α], [[lem:iii-i11-3-2]] and [[lem:iii-i13-2-2]] read the coefficients S_ν and
 u^rot (at b also A_b, [[def:iii-i15-2-3]]) from the forcing f′ of Step 0 of their proofs by maps fixed by L_b. These
@@ -184,8 +196,8 @@ the lower levels and at the base, which tend to their values at β_r by the same
 over the levels that ends at the base, (c). A_k is the coefficient of the new coordinates in such an expression, and
 the derivative of C^rot is read in the same way. By (F1) at the order ρ, every background contribution is bounded by
 ‖β − β_r‖_(ρ+11) times the coordinates or times ‖u‖_(ρ+2), which (F2) bounds once ‖β‖_(ρ+13+D) is bounded. The factor
-‖h‖ + |p⃗| of the direct bounds is such a bound, |p⃗| ≥ |b − b₀| being made small by the choice of ℬ_*, a condition on a
-component of p⃗; R_q and Δ_q are bounded by C‖q‖ in this way ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]), q being a
+‖h‖ + |p⃗| of the direct bounds is such a bound, as |p⃗| ≤ ‖β‖_0, its component |b − b₀| being also made small by the
+choice of ℬ_*; R_q and Δ_q are bounded by C‖q‖ in this way ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]), q being a
 component of β; and the bounds of [[lem:iii-i9-2-6]] are of this kind, its continuity asking h ∈ 𝒳^k with k ≥ 5 only.
 At b₀ the reference read is bounded on the order ρ by (F3), so the condition has order at most ρ + 14. At a reference
 point (0, p⃗_b) with b ≠ b₀ the read carries also C|p⃗_b|‖u_j − u‖_(w), which the proof of [[lem:iii-i11-3-3]] bounds by
@@ -193,10 +205,17 @@ point (0, p⃗_b) with b ≠ b₀ the read carries also C|p⃗_b|‖u_j − u‖
 order at most ρ + R_base + 16.
 
 *(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,871,940,942,598,941,194,134, which is less than T_12. Those of
-(d) are at most ρ + 14 < T_12 + 14, and ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as
-X_12 = 51,246,486,662,857,739,996,772 exceeds R_base. So every order is at most D_*, and so is their largest, d_*. The
-order m of the proof of [[lem:iii-k-2-3]] is the regularity ρ of the seminorm in which the proof of [[lem:iii-j2-2-3]]
-asks R_j → 0, and that condition has the order m + 14 by (d); so m + 14 ≤ d_*. The integer:
+(d) are at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point
+(0, p⃗_b) with b ≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]],
+at b₀, and at a rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates
+being the A_b read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as
+X_12 = 51,246,486,662,857,739,996,772 exceeds R_base. The convention "h small" of [[sec:iii-i7-1]], kept in
+[[sec:iii-i8-1]], in [[sec:iii-i9-1]] and so at the base points of [[ch:s22]], and the convention "q small" of
+[[sec:iii-i14-1]] each fix one order for all their uses: the largest of the orders that those uses ask. The uses lie
+in the bases, at the levels and in Steps 4′ and 4, and each asks an order that (a)–(d) bound, by (F1) at the
+regularity of its seminorm. So every order is at most D_*, and so is their largest, d_*. The order m of the proof of
+[[lem:iii-k-2-3]] is the largest regularity ρ of the seminorms in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0,
+and the condition asked in that seminorm has an order at least m + 14 by (c) and (d); so m + 14 ≤ d_*. The integer:
 T_12 = C_lev + I_lev + X_12 = 214,558,790,360,104,032,305,147,901,608,827,144, and D_* = T_12 + 14. ∎
 
 **Remark {#rem:uc-small-reading}** (Fixed seminorms that also bound the remainders.) [[sec:iii-i8-1]] takes the
@@ -211,7 +230,7 @@ in the seminorm of the next forcing class, two orders lower. The remainder map i
 Step 4′ reading the solution at α at an order below T_12 + 2. So ρ_k ≤ T_12 + K̄(C_lev + I_lev − 9) for every k, by
 [[lem:cs-sharp]]. The norms of the base must bound its maps into the seminorm of the hypothesis of the first step, so
 they are needed at regularities at most ρ_1 + 2 + R_base, and at most ρ_1 + 2R_base + 4 with the terms at a reference
-point (0, p⃗_b). By (F1)–(F3) and the proof of (c) and (d), every order is then at most
+point (0, p⃗_b). By (F1)–(F3) and the proofs of (c)–(e), every order is then at most
 
     D′_* := T_12 + 18 + K̄(C_lev + I_lev − 9) + 2R_base
          = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207 < 2.6193·10⁴⁹,
@@ -222,19 +241,20 @@ T_12 + 18 and 2R_base = 2,871,940,942,598,941,194,118 are added.
 **Proposition {#prop:uc-d-small}** (The loss with which the Nash–Moser theorem is applied.) At the computational point,
 with the index sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]], let d_F be the number
 that [[def:ec-accounted-loss]] assigns to the construction of [[thm:iii-j2-4-1]] at the base point Ψ(U) of the proof of
-[[lem:iii-k-2-3]], with which that proof obtains [[eq:iii-j2-4-1]], and let d_* be the largest of the orders of
-[[lem:uc-small-orders]]. Then:
+[[lem:iii-k-2-3]], with which that proof obtains [[eq:iii-j2-4-1]], and let d_* be the largest of the orders of the
+smallness conditions named in the proof of [[lem:iii-j2-2-3]], the fixed seminorms being those of
+[[lem:uc-small-orders]] (d) or those of [[rem:uc-small-reading]]. Then:
 
 (a) [[lem:iii-k-2-3]] holds with d := max(d_R, d_* + d_F + d_Φ), and [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] hold
 with d := d_Φ + 8. So the proof of [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] with
 
     d_NM = max(d_R, d_* + d_F + d_Φ),     d_F ≤ d_R,     d_acc ≤ d_R ≤ d_NM;                          {#eq:uc-d-small}
 
-(b) d_NM ≤ D_♭ + D_* + 1,038,326,399,999,940 = 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644,
-so d_NM < 2.6193·10⁴⁹, and N_NM = 21d_NM + 6 ≤ 550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530
-< 5.5005·10⁵⁰;
+(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + 1,038,326,399,999,940 =
+26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644, so d_NM < 2.6193·10⁴⁹, and N_NM = 21d_NM + 6 ≤
+550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 < 5.5005·10⁵⁰;
 
-(c) with D′_* of [[rem:uc-small-reading]] in place of D_*, d_NM ≤ D_♭ + D′_* + 1,038,326,399,999,940 =
+(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + 1,038,326,399,999,940 =
 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693 < 5.2386·10⁴⁹, and N_NM < 1.10009·10⁵¹;
 
 (d) in either case d_NM < D_acc and N_NM < 21D_acc + 6, with D_acc of [[thm:uc-integer]]; and every lower bound for
@@ -252,12 +272,13 @@ as it holds with d_R and the norms are non-decreasing in the order. *The other t
 most d_Φ + 8 ([[lem:uc-phi-loss]]). Their proofs ask U small through |U_0| ([[thm:iii-j-2-4]]); through the smallness in
 H³ of w = (h″, D_bh″, D²_bh″) that [[lem:ii-g-4-1]] (3) asks, and through [[lem:iii-j2-2-4]] at the faces, whose d_1 = 3
 serves, its proof using [[lem:ii-g-4-1]] with d = 3 only, both of which ‖Φ(U)‖_8 ≤ C‖U‖_(𝒟^(8+d_Φ)) controls (the proof
-of [[lem:uc-phi-loss]]); and through [[cor:iii-i-4-2]] at ℐ⁺, which asks the order 3 of h + h_rem(q) + h_tot(p⃗).
-Besides, [[prop:iii-j2-4-3]] states its bounds for ‖U‖_(𝒟^(3d)) < ε_0, which the domain |U|_(3d) < δ of the proof of
-[[thm:iii-k-3-2]] provides. So d := d_Φ + 8 serves for both. The largest of the three d's is max(d_R, d_* + d_F + d_Φ),
-as d_* ≥ 8. Finally, the construction of ℛ(U) applies that of [[thm:iii-j2-4-1]] at Ψ(U) and assembles U′ from its
-output by maps of non-negative charge (the proof of [[lem:iii-k-2-3]]), so d_F ≤ d_R; and d_acc ≤ d_R by the proof of
-[[thm:loss-d]].
+of [[lem:uc-phi-loss]]); and at ℐ⁺ through [[cor:iii-i-4-2]] for Φ(U) ([[thm:iii-j-2-4]]), which asks the order 3 of
+h + h_rem(q) + h_tot(p⃗), and through [[cor:iii-c-5-3]] for Ψ(U) ([[lem:iii-k-2-2]] (c)), whose smallness is read at an
+order at most 5 ([[prop:iii-c-4-4]]). Besides, [[prop:iii-j2-4-3]] states its bounds for ‖U‖_(𝒟^(3d)) < ε_0, which the
+domain |U|_(3d) < δ of the proof of [[thm:iii-k-3-2]] provides. So d := d_Φ + 8 serves for both. The largest of the
+three d's is max(d_R, d_* + d_F + d_Φ), as d_* ≥ 8. Finally, the construction of ℛ(U) applies that of [[thm:iii-j2-4-1]]
+at Ψ(U) and assembles U′ from its output by maps of non-negative charge (the proof of [[lem:iii-k-2-3]]), so d_F ≤ d_R;
+and d_acc ≤ d_R by the proof of [[thm:loss-d]].
 
 (b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ 1,038,326,399,999,940
 ([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + 1,038,326,399,999,940, the
@@ -287,37 +308,37 @@ under both.
 eq:uc-small-diff, rem:uc-small-reading, prop:uc-d-small and eq:uc-d-small, none of which is defined elsewhere. Every
 number of [[ch:explicit-constants]] stands, among them D_acc, 21D_acc + 6 and the lower bounds. The definition of d_NM
 changes from the largest of the losses of the three results to the largest of their d's, which [[prop:uc-d-small]]
-bounds, and the following sentences of [[ch:explicit-constants]] change with it. No sentence of the title page,
-[[ch:introduction]], [[ch:theorems]], [[ch:s27]] or [[ch:scope]] needs to change: each states its bounds for the loss d
-with which the settling proof applies the Nash–Moser theorem, which is d_NM, and they hold for it by
-[[prop:uc-d-small]] (d).
+bounds, and the following sentences of [[ch:explicit-constants]] change with it; [[rem:uc-missing]] gains one sentence
+(text 14). No sentence of the title page, [[ch:introduction]], [[ch:theorems]], [[ch:s27]] or [[ch:scope]] needs to
+change: each states its bounds for the loss d with which the settling proof applies the Nash–Moser theorem, which is
+d_NM, and they hold for it by [[prop:uc-d-small]] (d).
 
 *1. In [[sec:ec-accounted]],* replace the paragraph that begins "[[thm:ii-g-2-1]] is applied in the proof of" and ends
 "([[thm:loss-d]])." by:
 
 [[thm:ii-g-2-1]] is applied in the proof of [[thm:iii-k-3-2]] with N_NM = 21d_NM + 6, where d_NM is the largest of
-the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]]. Each of these is at least the loss of the
-estimate of its result, that of [[lem:iii-k-2-3]], a construction, accounted by [[def:ec-accounted-loss]] and the other
-two as their proofs fix them, and at least the orders at which its proof asks U small; for [[lem:iii-k-2-3]] these
-contain d_* + D + d_Φ, with d_* of [[lem:iii-j2-2-3]], D the d of [[thm:iii-j2-4-1]] and d_Φ the loss of U ↦ Φ(U)
-([[prop:uc-d-small]]). As (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]] of the right inverse of [[lem:iii-k-2-3]],
-whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc ([[thm:loss-d]]).
-
-*2. In [[thm:loss-d]],* replace the three lines from "[[def:ec-accounted-loss]], and d_NM the loss with which" through
+the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], as [[prop:uc-d-small]] fixes them. Each of
+these is at least the loss of the estimate of its result, that of [[lem:iii-k-2-3]], a construction, accounted by
+[[def:ec-accounted-loss]] and the other two as their proofs fix them, and at least the orders at which its proof asks U
+small; for [[lem:iii-k-2-3]] these include the order d′_0 ≥ d_* + D + d_Φ of its proof, with d_* of [[lem:iii-j2-2-3]],
+D the d of [[thm:iii-j2-4-1]] and d_Φ the loss of U ↦ Φ(U). As (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]] of the
+right inverse of [[lem:iii-k-2-3]], whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc ([[thm:loss-d]]).
+
+*2. In [[thm:loss-d]],* replace the four lines from "[[def:ec-accounted-loss]], and d_NM the loss with which" through
 "d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:" by:
 
 [[def:ec-accounted-loss]], and d_NM the loss with which the proof of [[thm:iii-k-3-2]] applies the Nash–Moser theorem
-[[thm:ii-g-2-1]]: the largest of the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], each at least
-the loss of its estimate, that of [[lem:iii-k-2-3]] accounted by [[def:ec-accounted-loss]], and the orders at which its
-proof asks U small ([[prop:uc-d-small]]). Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d = d_acc,
-[[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:
+[[thm:ii-g-2-1]]: the largest of the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]] that
+[[prop:uc-d-small]] fixes, each at least the loss of its estimate, that of [[lem:iii-k-2-3]] accounted by
+[[def:ec-accounted-loss]], and the orders at which its proof asks U small. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]
+hold with d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:
 
 *3. In the paragraph after (iii) of [[thm:loss-d]],* replace the two lines from "the index sets. At the computational
 point [[thm:uc-integer]] evaluates" through "at most one below 3.30029 × 10⁵¹." by:
 
 the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
-[[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc and d_NM are at most an
-integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.
+[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc
+and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.
 
 *4. In the proof of [[thm:loss-d]],* replace the three lines from "([[eq:ii-g-2-5]]). *d_NM ≥ d_acc.* Hypothesis (iii)"
 through "is one of the three whose largest is d_NM. By" by:
@@ -340,8 +361,8 @@ for N_NM," through "so that d_NM equals it ([[thm:uc-integer]]). Given ε_K, the
 
 through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are
 at most 62N_Λ + 10 < 1.04·10¹⁵ ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of [[lem:iii-k-2-3]] satisfies
-[[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[prop:uc-d-small]] bounds the orders at which these results ask U
-small, and with them d_NM ([[thm:uc-integer]]). Given ε_K, the explicit part
+[[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at
+which these results ask U small, and with them d_NM ([[thm:uc-integer]]). Given ε_K, the explicit part
 
 *7. In the opening of [[sec:uc-close]],* replace the line "loss of the map Φ of [[thm:iii-j-2-4]], which governs the
 two other components of d_NM ([[lem:uc-phi-loss]]). Memberships" by:
@@ -372,9 +393,9 @@ accounted by [[def:ec-accounted-loss]] and at least d_acc ([[thm:loss-d]]), and
 *9. In (ii) of [[thm:uc-reduction]],* replace "(ii) d_NM = max(d_R, d_FM, d_Ψ) with" by "(ii) d_NM ≥ max(d_R, d_FM,
 d_Ψ) with"; the line keeps its length.
 
-*10. In [[lem:uc-dr]],* replace "If d_R > 62N_Λ + 10, then d_NM = d_R." by "If d_R > 62N_Λ + 10, then
-d_R = max(d_R, d_FM, d_Ψ)."; and in the last sentence of its proof replace "d_NM = max(d_R, d_FM, d_Ψ) with
-d_FM, d_Ψ ≤ 62N_Λ + 10." by "d_FM, d_Ψ ≤ 62N_Λ + 10." Both lines become shorter.
+*10. In [[lem:uc-dr]],* replace "If d_R > 62N_Λ + 10, then d_NM = d_R." by "If d_R > 62N_Λ + 10, then d_R = max(d_R,
+d_FM, d_Ψ)."; and in the last sentence of its proof replace "d_NM = max(d_R, d_FM, d_Ψ) with d_FM, d_Ψ ≤ 62N_Λ + 10." by
+"d_FM, d_Ψ ≤ 62N_Λ + 10." The first line becomes 121 characters long, the second shorter.
 
 *11. In [[thm:uc-integer]],* replace the display line of [[eq:uc-integer]] by:
 
@@ -404,6 +425,14 @@ orders that the constructions produce are bounded in this paper only by k̄(λ).
 d_acc and d_NM are at most" through "most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies
 outside the set on which [[thm:settling]]" by:
 
-products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]] with the orders
-at which it asks U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below
-3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
+products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
+orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
+most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
+
+*14. In [[rem:uc-missing]],* replace its last line, "the logarithmic orders that the level steps produce, which this
+paper bounds only by k̄(λ) ([[rem:cs-sharpness]]).", by:
+
+the logarithmic orders that the level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]). The
+bound for d_NM rests in addition on the orders of the smallness conditions, which [[lem:uc-small-orders]] bounds for
+the fixed seminorms of its (d), and [[rem:uc-small-reading]] for the larger ones that [[sec:iii-i8-1]] describes
+([[prop:uc-d-small]]).
```
