# R2-DINT-b: confirming reading of F-DINT-b (chapter 71) and of PR-1 (Appendix A and references)

Reader R2-DINT-b. I changed nothing in the repository. Tree read at HEAD 392770f4.
- Chapter 71 is as e915e3e4 left it: md5 1978de0008ae2995c1fac8cd80ec3b76, 4,381 newline-terminated lines,
  203 labels. 28459334 adds only the report.
- Chapters 95 and 98 are as 724edab6 left them. The pre-round copies in scratch/f_dint_b and scratch/pr1 have the
  md5s of the parent commits.
- Scratch work, including the proposed replacement file used to check line lengths, is in
  `.../scratchpad/reader/scratch/r2_dint_b/`.

## Verdicts

- **Part 1, chapter 71 after F-DINT-b: CONFIRMED, with nits only: 0 Major, 0 minor, 3 nits (N1–N3 below).**
  - All eight R-DINT-b findings, its observation 1, and R-DINT-a's O1–O3 are resolved.
  - The new text is true where it stands, and the round moved no number.
  - thm:uc-integer's bounds and hypotheses still follow.
  - Nothing in chapter 71 contradicts P-46-R1.
- **Part 2, PR-1: CONFIRMED: 0 Major, 0 minor, 0 nits.**

## The original findings

| item | site now | resolved | note |
|---|---|---|---|
| R-DINT-b 1 (minor) | 71:386–388 | yes | Reviewer's text verbatim. lem:ec-round-loss (a), prop:ec-rounds and thm:loss-d (ii) together give d_acc ≥ Σ_rounds(2 + ℓ_tf) ≥ 3R over the rounds of the two iterations. |
| R-DINT-b 2 (minor) | 71:1556–1560 | yes | Reviewer's text, with "At h̃ = …", which defines h̃. See check (b) below. |
| R-DINT-b 3 (nit) | 71:1252, 1298 | yes | Headings as proposed. The four [[sec:ec-floor]] uses still fit. |
| R-DINT-b 4 (nit) | 71:380–382 | yes | Verbatim. |
| R-DINT-b 5 (nit) | 71:510–511 | yes | Verbatim. Chapter 23 l. 1082, 1139, 1417, 1509–1513 do use the closed graph theorem. N2 is a wording point that comes from keeping "We prove them again". |
| R-DINT-b 6 (nit) | 71:1477–1478 | yes | Verbatim, and true: N_NM = 21d_NM + 6 ≥ 21d_acc + 6 > any lower bound for d_acc. |
| R-DINT-b 7 (nit) | 71:4367–4369 | yes | Verbatim. def:ec-point, def:uc-choice and def:cs-choices all sit at the computational point. |
| R-DINT-b 8 (nit) | crosswalk/71 l. 20 | yes | Both replacements are made. The departure (minor 1's citation in place of "'the next section' written [[sec:ec-floor]]") is right. |
| R-DINT-b obs. 1 (R2-DB-b nit 2) | 71:3855–3856, 3875–3877, 3938 | yes | def:cs-choices (h) and its justification, cited in lem:cs-elem (e). See check (c). |
| R-DINT-b obs. 2 (chapter 43) | — | not in scope | lem:iii-j2-2-1 (a) still ends "and [[eq:iii-i-5-2]] with ‖β‖ in place of ‖h‖" (43:175–176). Chapter 71 now states the q-background case correctly. See the observations. |
| R-DINT-b obs. 3 | — | no action asked | — |
| R-DINT-a O1, first half (s_P) | 71:1488–1490 | yes | s_P is lem:iii-k-2-2 (d)'s (46:1247). ω_k and s_k are prop:iii-k-1-2 (3)'s (46:240–246). |
| R-DINT-a O1, second half (strict) | 71:1487, 1500 | yes | See check (d). |
| R-DINT-a O2 (line 27, = B5) | 71:28–30 | yes | True. N1 is a wording point about its list. |
| R-DINT-a O3 (def:cs-choices) | 71:20–21, 2450–2452 | yes | The opening and thm:uc-integer both name def:uc-choice and def:cs-choices. |

## New findings

### N1 (nit) — 71:28–30: the list of values that rest on the chapter is incomplete

*What is wrong.* "Other chapters state explicit values that rest on it, the indices of … and the value N′ = 13 …;
these values are used only in this chapter." The appositive reads as the complete list, but other chapters also
state values that rest on chapter 71:
- 00:34, 01:153–154, 03:353–354 and 90:64–70 restate d > 1.2497 × 10²⁴ and d < 1.57157 × 10⁵⁰.

The statement about proofs is true: outside chapter 71, its labels occur only in remarks (33:3236, 62:577), in these
summaries, and in the explicit clauses of 23:1071–1072, 23:1466–1471 and 25:29–30. The values 200Θ + 98, 200Θ + 100
and N′ = 13 occur nowhere else.

*Replacement* (l. 28–30 become four lines; the lengths after resolution are 116, 108, 105 and 64):

> No result of this chapter is used in the proof of any theorem of this paper outside it. Apart from the chapters that
> restate its bounds, two chapters state explicit values that rest on it: the indices of [[prop:ii-a1-2-4]] and
> [[lem:ii-a-8-5]], which [[prop:fwd-calculus]] proves, and the value N′ = 13 of [[ch:s06]], which rests on
> [[lem:fwd-orders]]; these values are used only in this chapter.

### N2 (nit) — 71:511: "them" now reads as "the values"

*What is wrong.* After R-DINT-b 5 the line reads "the values stated there are proved here. We prove them again,
every derivative counted." "them" now points back to "the values", so the text says they are proved here and also
proved "again". The two statements, prop:ii-a1-2-4 and lem:ii-a-8-5, are what is proved again.

*Replacement* (the same length, so nothing is rewrapped): "We prove them again, every derivative counted." → "We prove
both again, every derivative counted."

### N3 (nit) — 71:6: "asks smallness in the regularity N_NM" does not match thm:ii-g-2-1, and can be read as a data order

*What is wrong.*
- thm:ii-g-2-1 (29:78–79) asks ‖Φ(0)‖_(2d) < ε, with ε depending on the constants up to the order N_NM. It does not
  ask smallness at the order N_NM.
- Since P-46-R1, the data are asked small up to N_NM + k″ (46:1251–1253, 1555–1561). A reader could take "smallness
  in the regularity N_NM" as the data order, which it is not.
- thm:loss-d's own wording, "applied at the regularity N_NM", is exact.

This sentence predates the round. It is not contradicted by P-46-R1, but it is the one place in chapter 71 where the
order of a smallness condition is named.

*Replacement* (l. 6–8 become four lines, 6–9; the lengths after resolution are 108, 116, 109 and 32; no wrapped line
starts with a forbidden prefix):

> [[thm:loss-d]]), and [[thm:ii-g-2-1]] is then applied at the regularity N_NM = 21d + 6, the order up to which its
> smallness threshold reads the constants of its hypotheses. The threshold λ1 on the wavelength and the threshold δ on
> the data in [[thm:settling]] are produced by the proof, and are positive. This chapter states what the proof makes
> explicit about d, N_NM, δ and λ1.

## What I checked and found to hold

### Part 1: every hunk of F-DINT-b

I ran a word-level diff (difflib, no junk heuristic) of 71.orig.md against the current file.
- It has 30 change sites, and every one is an item of the F-DINT-b report. There are no others.
- Only one site touches no word: rem:is-summary, l. 3168–3169, where "taken" is only rewrapped.
- Every crosswalk change is in the note column. 13 rows changed, as the report says.

**(a) No number moved.**
- Every digit-bearing change is new text: N′ = 13, d_F + 3, 𝗌 with s_in = 11 and s_out = −10, and the strict "<".
- The removed sentence of nit 4 took with it "d_ℵ = 1", "raises by 5" and the eq:fwd-split terms, which sec:fwd
  states at l. 391–395.
- Recomputed exactly with fractions:
  - D_e + M_cC_* = 1,258,700·10¹⁸ + 244,153·64,368·10⁴⁰
    = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰. The margin is 5.97·10⁴⁴.
  - 21D_acc + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.
  - 244,153 · 64,368 = 15,715,640,304.
  - (1 − 5δ̂ − δ̄)/δ̂² = 4.67758916…·10¹⁹ (δ̂ = 1.46214·10⁻¹⁰, δ̄ = 1.94137057·10⁻⁸). So 3R > 3 · 4.6775·10¹⁹
    = 1.40325·10²⁰, and 21 · 1.403·10²⁰ = 2.9463·10²¹.
  - At ε_K = 1.6417·10⁻¹⁴: R > 4.16598·10²³ and 3R > 1.24979·10²⁴.
  - At ε_K = 1.6416·10⁻¹⁴: 3ε_K + 2δ̂ + δ̄ = 1.97062·10⁻⁸ < 1.98·10⁻⁸, ε_Kδ̂ = 2.400249024·10⁻²⁴ exactly, and
    3(1 − 1.98·10⁻⁸)/2.40025·10⁻²⁴ = 1.24987·10²⁴ > 1.2498·10²⁴. Also 1.0072 · 1.2498 = 1.25880 > 1.2587.
  - 1 + 19x + 171x² + 969x³ = 1.567891 at x = 0.024, and this is > 1.5678 > 100/64. 2¹⁹⁶ > 10⁵⁹ (checked as
    integers). (59/196) · 32 · 1.403·10²⁰ = 1.351461·10²¹.

**(b) Minor 2, the split losses (l. 1556–1571).**
- eq:iii-i-5-2 has the form ‖u‖_k ≤ C_k(‖f‖_(k+d) + ‖h̃‖_(𝒳^(k+d))‖f‖_d).
- At h, h + h^(−1)(S) and h + h_tot(p⃗), ‖h̃‖_(𝒳^m) ≤ C_m(‖h‖_(𝒳^m) + |S| + |p⃗|) (lem:cs-elem (e) proof, l. 3941).
  A term |S|‖f‖_d is absorbed in ‖f‖_(k+d), as in the proof of thm:iii-i-5-3 (38:650). So the split loss is
  (d_F; d_F, d_F).
- At h + h_rem(q) + h_tot(p⃗), the bound carries ‖q‖_(𝒬^(m+3)), which gives (d_F; d_F + 3, d_F). Since the norms are
  non-decreasing, this is also (d_F + 3; d_F + 3, d_F + 3), and d_F + 3 ≤ 20,183 is lem:cs-elem (e)'s charge.
- With that form, "every family other than the background terms has c, b ≤ a" holds. lem:ec-split-loss (d) then
  applies as before, and its family is charged its loss d_F + 3, as in cstar.
- No other statement of the chapter gives the forward operators the split loss (d_F; d_F, d_F) at the q-backgrounds.
  l. 14, 1436 and 1922 speak of the loss d_F of eq:iii-i-5-2, which is consistent with this paragraph.

**(c) def:cs-choices (h) (l. 3855–3856, 3875–3877).**
- lem:fwd-orders runs the construction of sec:ii-c-5-2 (the proof of prop:ii-c-5-1, 24:1245–1260) with s_in = 11 and
  s_out = −10.
- At those numbers its inequalities hold: ½ + 9/4 + 7 + 1 = 10.75 < 11, and −½ − 2 + 7 − α_+ + 1 < 7.5 < 11 for
  α_+ ∈ (−2, −1). They give inf 𝗌 = −10, inf 𝗌_0 = −13, and so N′ = 13 (25:29–30).
- thm:iii-i-5-3's proof uses "the orders of ch:s09, which lie in 𝒪_c by lem:iii-i-5-1". That is the order 𝗌 of
  prop:ii-c-5-1 (38:523), as (h) says.
- (B4) (38:749–753) is a condition on B_1 for "the order 𝗌 of prop:ii-c-5-1, built for 2L_(b₀)", and B_1 is fixed
  with (B1)–(B4) (38:696–697). So "B_1 is chosen after the order, so (B4) holds for it on B̄_1" is true.
- The citation in lem:cs-elem (e) (l. 3938) is right. thm:uc-integer and prop:cs-cstar now name every free choice
  that their proofs make.

**(d) prop:ec-delta-cap, the strict "<".**
- The proof of thm:iii-k-3-2 (46:1559–1560) asks ‖P_5(Ψ(0))‖_(ℱ^(2d)) < ε_NM, and chooses ε with
  C_(2d)ω_(2d+3)(ε) < ε_NM. The chapter-71 choice now matches.
- The proof's chain still holds: with C_(2d) ≥ 1 and ε_NM ≤ 2^(−(32d+8)) we get
  ω̃(ε) < ε_NM/C_(2d) ≤ 2^(−(32d+8)); and ε ≤ ω̃(ε), from ω̃(t) ≥ t on [0, s̃], gives δ ≤ 2^(−(32d+9)).
- Such an ε exists after the enlargement, since max(ω̃(t), t) → 0.
- The conclusions are unchanged, and the displayed "≤" is now weaker than what is proved.

**(e) The other hunks.**
- The O3 wording is true: def:uc-choice fixes the weights and def:cs-choices the free orders and inner products.
- rem:ec-not-evaluated's new colon list is true. Its scope ("on which d depends") excludes the cut-offs, which no
  definition fixes with numbers.
- The two headings now match the contents: the lower bound, prop:ec-rounds and thm:loss-d (ii), is in
  sec:ec-gauge-gap.

**(f) Contract, chapter 71.**
- Every line has at most 121 characters, both in the source and after assembly's label resolution (assemble.py's own
  REF_RX and numbering).
- No CR, tab or trailing blank. The file ends in one newline, with no double blank lines.
- Every line starting with "- " or "|" after a non-blank line is a list item or a table row (l. 105–118, 362–378,
  1261–1264, 1341–1359, 1965–1977, 2964–2993). The two new headings follow blank lines.
- Labels are lowercase. crosswalk/71: 203 rows of 4 fields, equal to the label sequence in order.
- No file names, program names, code or assistant language.

### Part 1: chapter 46 after P-46-R1, against chapter 71

- I grepped chapter 71 for d_1, k′, k″, Θ, ε_0, "data", "smallness", "regularity N_NM" and lem:iii-k-2-3. It has no
  d_1, no k′ or k″ of chapter 46, no N_NM + 3, and no data order. (The only "d_1" hits, l. 476, 1102, 1119, 1171
  and 1228, are the calculus index of sec:fwd.)
- lem:iii-k-2-3 is described at:
  - l. 161–163 and 1459–1466 (the loss of ℛ(U) is that of eq:iii-j2-4-2, now in the form eq:s27-rinv, with the same
    loss);
  - l. 2223 and 2235 (d_NM is the largest of the three losses);
  - l. 2432–2448 (lem:uc-dr: ℛ(U) is the construction at the base point Ψ(U), with e_S and e_(S⁰) as forcing
    summands);
  - l. 3883 and 3901, and lem:cs-elem (d) (e_S and e_(S⁰) are charged 11);
  - l. 4116, 4169 and 4272–4276 (U ↦ Ψ(U) has the loss of U ↦ Φ(U)).
- Each of these agrees with the repaired chapter 46:
  - 46:1378–1410 gives ‖Ψ(U)‖_j ≤ C_j‖β^Ψ‖_(j+d_Φ), with the loss d_Φ of Φ.
  - e_S has the loss d_BG + d_Φ in U, which the defects f^S already had.
  - Only the constants read the data, through Θ_(k+d).
  - So no loss moves, and d_acc, d_NM and N_NM are unchanged.
- prop:ec-delta-cap is consistent with the new Smallness paragraph:
  - ε ≤ s_1 ≤ s_♭ ≤ min(s_(2d+3), s_P) = s̃;
  - C_(2d)ω_(2d+3)(ε) < ε_NM;
  - C_(2d) is lem:iii-k-2-2 (d)'s, and (d) is unchanged;
  - "all that the proof uses of the modulus is that it tends to 0" is still true, since s_1 is fixed through
    ω_♭(s) → 0.
- l. 383–384 ("the constants of the smallness conditions are used at those orders only", k ≤ N_NM) agrees with
  46:1264 ("The smallness constants use orders k ≤ N_NM only"). The trapping data there are those of
  cor:iii-h2-1-2, not the initial data.
- Only l. 6 names a smallness order loosely: N3.

### Part 2: PR-1

- **Appendix A labels.** [[label]] occurrences in chapters/*.md:
  - thm:std-bgp-riesz 0, thm:std-cbcl-harmonicity 0, thm:std-lr-propagation 0, rem:std-racz 0,
    thm:std-wu-characteristic 0, thm:std-bh-extension 0;
  - no bare mention of the six keys in any chapter or other crosswalk.
  - No literature citation of their results remains: no [BGP, …1.2.…], no [BH17, Theorem 7.21], no
    [Rac16, (3.3)] or [Rac16, (4.7)], and no Riesz distribution or flat fundamental solution in use. The
    [BGP, p. 18], [BGP, p. 24], 07:196 and 83:10 citations are covered by kept entries
    (thm:std-bgp-causal, rem:std-racz-characteristic).
  - The removed entries defined no equation label.
- **Bibliography.**
  - 131 → 90 keys. The 41 removed are exactly the report's 37 plus CBCL06, LR05, Rie49 and Wu26.
  - The remaining 90 keep their order, and their entry texts are unchanged.
  - No alias ("See […]") remains, and no remaining entry refers to another key.
  - Whole-key search, with no alphanumeric on either side, finds none of the 41 in any chapter in any form. This
    also catches "[KEY, …]" and keys inside multi-key or multi-line brackets.
- **Nothing still cited was removed.**
  - Every citation key in chapters/*.md has an entry. The only non-matching bracket tokens are "AB" in the
    commutators [AB, X] (25:1438) and the subscript F_𝔨 W_𝔨,AB (80:1184).
  - All 90 entries are cited. BVW15 is cited in a bracket that spans a line break, at 35:1396.
  - Every [[kind:key]] in the 62 chapters resolves (0 unresolved, no uppercase key). That includes all 45 distinct
    [[…:std-…]] references.
- **Chapter 95.**
  - crosswalk/95 has 62 rows of 4 fields, equal to the chapter's 62 labels in order.
  - The diff only deletes lines. No section is left empty: sec:std-characteristic keeps
    thm:std-ctg-neighbourhood.
  - The opening's list of paging conventions names only kept keys: [BGP], [See64], [MM87], [Mel93], [Hö90], [RS1],
    [Tre19] and [DLMF], all in chapter 98.
  - The [BH17] convention sentence (95:589) still serves the three remaining [BH17] entries.
  - thm:std-racz-hyperbolic and rem:std-racz-characteristic define their notation themselves, without the removed
    remark.
  - 01:193, 47:15 and 87:1190 describe the appendix only in general terms.
  - No dangling sentence remains.
- **Contract.**
  - Chapters 95 and 98 have at most 121 and 120 characters per line, also after resolution.
  - Every "- " start in chapter 98 is an entry; continuation lines start with two spaces.
  - Chapter 95's "- " starts are its list items (95:215–218, 290–300, 1025–1027).
  - No double blank lines; each file ends in one newline.

### Tools

- `python3 lint.py --chapters`, last line: `chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)`
- `python3 assemble.py --check`, last line: `labels 4570, computations cited 0, problems 0`

The label count is consistent: F-DINT-b leaves 4,573, PR-1 removes 6, and P-46-R1 adds 3.

## Observations outside the count

1. Chapter 43, lem:iii-j2-2-1 (a), still ends "and [[eq:iii-i-5-2]] with ‖β‖ in place of ‖h‖" (43:175–176). At the
   q-backgrounds this holds only with the order k + d + 3 in ‖β‖, as chapter 71 now says. This is R-DINT-b's
   observation 2, and it belongs to the reader of chapter 43.
2. 03:354 and 90:69 still say "at one admissible choice of the weights". This is true as an existence statement;
   01:154 already says "of the weights, orders and inner products". 90:72–73 names the indices of chapter 23 but not
   N′ = 13. That is not false.
3. sec:ec-floor's heading keeps the old "Two long iterations", while the section lists three constructions and
   thm:loss-d (i) says "the three of [[sec:ec-floor]]". The two kinds of rounds are the two iterations the lower
   bound uses, so the heading is defensible. The phrase predates the round.
4. The F-DINT-b report gives the file as 4,382 lines. It has 4,381 newline-terminated lines; 4,382 is assembly's
   count of the split text.
5. crosswalk/95's heading rows sec:std-gauge and sec:std-characteristic still name [CBCL06], [LR05] and [Wu26] in
   source_name. That column describes the source record, not the chapter, so nothing dangles in the paper.
