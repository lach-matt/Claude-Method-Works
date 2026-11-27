# Review R-M-LL: the merge M-LL (commit b6258b74) of the confirmed proof P-LL

## Verdict

**CONFIRMED — 0 Major, 0 minor, 1 nit.**

All three nits of R-P-LL are in the proof text in the reviewer's own words. Nothing else in the proof text changed. Each
of the six placed blocks is byte-identical to its block in notes/reports/M-LL.P-LL.md and occurs exactly once. Each old
text is gone completely, and every join reads on. In place, the new lem:layer-interpolation and rem:layer-threshold-size
read correctly, and every reference resolves to what is meant. Every use of the lemma in chapter 84 holds with the new
lemma. No sentence in chapters/ contradicts the new remark. Crosswalks 84 and 95 match their chapters row for row. The
contract holds: all three commands are clean.

The one nit is in the merger's report, not in the paper. Report §6 says a crosswalk row has an empty note, but the
commit gives that row a note.

**The tree moved while I read.** HEAD went from b6258b74 to d773cba7 (four commits). Those commits touch only chapter 63
and notes/reports/S-G1.md. The working tree also has uncommitted edits to chapter 63 and crosswalk 63. All seven files
of this merge are byte-identical at HEAD and at b6258b74 (checked with cmp): chapters 84, 90, 95 and 98, crosswalks 84
and 95, and M-LL.P-LL.md. I ran the checks both on the live tree and on an exported copy of b6258b74.

## Checks

| # | check | result |
|---|---|---|
| 1a | n1 applied in the reviewer's words | R-P-LL lines 41–51, with the review's 6-space indent removed, equal M-LL.P-LL.md lines 115–125 byte for byte. The merger used the replacement because no page image was available. That is the condition R-P-LL states. |
| 1b | n2 applied in the reviewer's words | R-P-LL lines 65–66, indent removed, equal M-LL.P-LL.md lines 53–54 byte for byte. |
| 1c | n3 applied in the reviewer's words | The reviewer's replacement phrase occurs verbatim in placement item 7 (lines 205–207), rewrapped. Against 392f69f4 the only word changes are "[[lem:layer-levels]] and" → "[[lem:layer-levels]]," and the inserted "[[thm:layer-past]] and [[prop:layer-regions]],". |
| 1d | nothing else changed | The diff from 392f69f4:proofs/P-LL.md to M-LL.P-LL.md has exactly three hunks (old lines 53, 114–122 and 202–206): 206 lines become 210. The md5 4d2208fa6f4a70749fda80f0842ab2fd matches M-LL.md §5. proofs/P-LL.md is no longer tracked. |
| 2a | item 1 byte-identical | Proof lines 7–42 (36 lines, 3136 bytes) are chapter 84 lines 844–879. 1 occurrence. |
| 2b | item 2 byte-identical | Proof lines 44–108 (65 lines, 4939 bytes) are chapter 84 lines 1371–1435. 1 occurrence. |
| 2c | item 3 byte-identical | Proof lines 182–183, 4-space indent removed (171 bytes), are chapter 90 lines 97–98. 1 occurrence. |
| 2d | item 4 byte-identical | Proof lines 189–193, indent removed (513 bytes), are chapter 95 lines 8–12. 1 occurrence. Normalised, they equal the old lines 8–12 with "[See64] and [MM87] are" changed to "[See64], [MM87] and [DS41] are", and nothing else. |
| 2e | item 5 byte-identical | Proof lines 115–125 (883 bytes) are chapter 95 lines 1255–1265. 1 occurrence. |
| 2f | item 6 byte-identical | Proof lines 202–203, indent removed (182 bytes), are chapter 98 lines 52–53. 1 occurrence. |
| 2g | old texts fully replaced | At b6258b74^, chapter 84 lines 844–862 and 1354–1365 equal the placement's quoted old texts after whitespace normalisation, with the label markers restored and "(its equation label)" read as {#eq:layer-interpolation}. In the merged file, nothing of either survives between the new block and its neighbours. Old 863 (blank) and 864 (cor:layer-interpolation-band) are now 880 and 881. The remark was and is the end of the file. Chapter 90's old 97–98 ("at most 10^(−430)") is gone. In chapter 95, the old last line "…". Here log is the natural logarithm." is kept, and the theorem follows it after a blank line. |
| 2h | joins, 3 lines either side | Item 1: "### The window {#sec:layer-window}", blank, lemma, blank, cor:layer-interpolation-band. Item 2: "… ν_* = \|ν(v_s − τ0)\|.", blank, remark, end of file with one newline. Item 3: "… λ_L is the" / "threshold that the proof delivers, …, and for the envelope env_C it is" / "below 2.71·10⁻¹² ([[rem:layer-threshold-size]]).", then blank and "### After the shell". Item 4: "… listed in the references;" / "the arXiv text of [BGP] …" / … / "Inside each item the letters are the source's.", then blank and the next heading. Item 5: "…". Here log is the natural logarithm.", blank, theorem, end of file with one newline. Item 6: [DS23] / [DS41] / [Dya16], with a 2-space continuation indent, in alphabetical order. Every join reads as one sentence or as the next item. |
| 3a | lem:layer-interpolation in place | It is correct, and it reads as the confirmed text. It cites [[thm:std-duffin-schaeffer]] (A.49) for the formula for T_n^(i)(1) and for the bound at the nodes. That theorem quotes (19) and the sentence identifying T_n^(p)(1) with its right side, for degree n and \|f(cos(νπ/n))\| ≤ 1, so it gives both. n = m − 1 ≥ 1, as m ≥ 2. The definitions of T_n agree: T_n(cos θ) = cos nθ here and T_n(x) = cos(n cos⁻¹ x) in A.49. The points cos(kπ/n) are A.49's cos(νπ/n). The minimisation variable κ is local, as it was in the old lemma, so κ := 64 in thm:layer and C_κ in lem:layer-levels do not clash with it. |
| 3b | rem:layer-threshold-size in place | Every reference resolves to what is meant. [[eq:layer-threshold]]: λ_L is the minimum, and Λ_4 is the term in it, so Λ_4 = [(1 + C1Δτ/(2π)) B_m]^(−m/(m−p)) exactly. [[lem:layer-interpolation]] gives the closed form of C_(1,m). [[eq:envelope]] defines β and env, and the argument (2v − 4)/3 at v = 1/2 + x is t − 1. [[lem:envelope-constant]] (a) gives support [1/2, 7/2], and (b) gives c_e > 1.3240867 > 1. [[thm:layer]] fixes p = 14, M = 2N + 8 and N = K + 3, so m = 112K + 784. C1 ≥ 0 by [[eq:eq-c1]]. The step τ_end ≥ v_start − q0 > τ0 holds by chapter 2: τ_end = max_(v≤V)(v − r_q(v)) ≥ v_start − q0, and v_start − τ0 > √μ0 + 1 > q0. The four eq:layer-size-* keys are cited only inside the remark. I recomputed every printed number in double precision, each in its stated direction. The remark's own inputs give Λ_4(0) ≤ 2.708684·10⁻¹² for K = 6. The other values are β(1568) = 26.598164, β(1680) = 26.809016, e^(−26.837) = 2.2123·10⁻¹² and e^(−26.809) = 2.2751·10⁻¹². |
| 3c | the uses of the lemma in chapter 84 | Every use holds. cor:layer-interpolation-band (881–908) uses the lemma for i ≤ c < m, with C_(0,m) := 1 for the term i = 0, and global M_m ≥ M_m(v). eq:layer-margin-lower (901–905) uses it at i = 1. lem:layer-levels (910–926) uses it at i = 1 on (−∞, v_+]. prop:layer-regions (1210 ff.) takes m := max(56M, 4PM, ⌈4M/δ⌉) and uses it through "the argument of lem:layer-levels" and eq:layer-cost-level. thm:layer-past (1185–1201) takes m := 56 M_P and uses it through C_ε. In the proof of thm:layer, line 962 gives Λ_4 (i = 1), 963–967 give C_ε (i ≤ M < m), and Λ_5′ uses i ≤ 4. Each takes only the inequality, with finite C_(i,m), so every argument stands as written. |
| 3d | the constants of eq:layer-threshold | Λ_4, Λ_5′ (min over i ≤ 4) and C_ε (sum over i ≤ M) all read with the new C_(i,m), and the term i = 0 with C_(0,m) := 1 of the corollary. Λ_8b–Λ_8d use C_ε. No form changes. The sentence after the display, "Λ_4 is the hypothesis of [[lem:layer-levels]] …", is still exact. |
| 4a | "10^(−430)" in chapters/*.md | 0 occurrences. Variants checked: 10⁻⁴³⁰, 10^(-430), 10^430 and 10^600, all 0. |
| 4b | "Λ_(i,m)" in chapters/*.md | 0 occurrences. Also 0 for Λ_(1,m), l_k^(i) and l_k′. |
| 4c | "λ_L" in chapters/*.md | 13 lines, none contradicting the remark. 84:17 says λ_L is written as an explicit formula, which is true. 84:936, 938, 944 and 956 are thm:layer and its proof. 84:1339 and 1346 are the threshold section. 84:1371, 1377 and 1379 are the new remark. 85:2058 says C_L11 and C_L4 are not evaluated, which the remark still says. 90:95–98 say "not evaluated … below 2.71·10⁻¹²", which is the remark's uniform bound. Also 86:11, "whose lower end c_e > 1 is also what [[rem:layer-threshold-size]] uses": true, since the remark uses only c_e > 1. No chapter describes the old equidistant nodes, and none cites the old numbers 357 or 10^600. |
| 5a | crosswalk 84 | 92 labels in the chapter and 92 rows, the same keys in the same order, 4 fields in every row. The header is label, source, source_name, note. There are no blank rows, no CR, and a final newline. The four eq:layer-size-* rows follow rem:layer-threshold-size, in order of definition. The cited lines of 392f69f4:proofs/P-LL.md are right: 7–42 is the lemma, 44–107 the remark, and 56, 62, 71 and 77 the four equation-label lines. |
| 5b | crosswalk 95 | 63 labels and 63 rows, the same order, 4 fields in every row. thm:std-duffin-schaeffer is the last row, after thm:std-chebyshev. Its source line, 392f69f4:114, is the theorem heading. |
| 6a | line length, source | The maximum is 121 in chapters 84, 90 and 95, 120 in chapter 98, and 121 in M-LL.P-LL.md. No line exceeds 121. The 112 added lines have a maximum of 121. |
| 6b | line length, resolved | In the assembled text (b6258b74) the maximum is 121. Resolved, the lemma block's longest line is 119 characters and the remark block's 118. The added lines resolve to at most 121. The resolved headings are Lemma 54.23, Remark 54.39 and Theorem A.49. |
| 6c | wrapped-line starts | No added paragraph line starts with "+ ", "- ", "* ", "> ", "#", "=" or "\|". The only such starts are the 4-space-indented displays and the bibliography item "- [DS41] …", which is the list form of every entry in chapter 98. |
| 6d | no backslash, no file, program, code or AI language | 0 backslashes in the four chapters and in M-LL.P-LL.md. Searching the 112 added lines for file, script, program, code, comput, software, numeric, machine, algorithm, tool, AI, model, agent and similar words gives 0 hits. |
| 6e | `python3 lint.py --chapters` | HEAD (live tree): "chapters: 62 file(s), 4585 label(s) defined, 0 hit(s)". b6258b74 (export): 4584 labels, 0 hits, as in M-LL.md §4. The extra label comes from the later chapter 63 work. |
| 6f | `python3 assemble.py --check` | HEAD: "labels 4585, computations cited 0, problems 0". b6258b74: "labels 4584, computations cited 0, problems 0". |
| 6g | the in-memory assembled lint | It prints `[] 0` on HEAD and on b6258b74. |

## Findings

### n1 (nit, record only) — M-LL.md §6 says a crosswalk row still has an empty note; the commit gives it one

- **Location:** notes/reports/M-LL.md lines 157–159. §3, lines 87–95, also lists only two amended rows.
- **What is wrong.** At b6258b74, crosswalk/84-equality-layer.tsv line 60, the row for eq:layer-interpolation, carries
  the note "P-LL: the constant C_(i,m) is now that of Chebyshev-point interpolation (Duffin-Schaeffer), closed form in
  lem:layer-interpolation". That note is accurate. So the coordinator took up the report's suggestion at commit, but
  the report still describes the state before the commit. No paper text is affected.
- **Replacement** for lines 157–159:

      - **eq:layer-interpolation's crosswalk row** (84) had an empty note when this report was written. Its source name
        is "EL L.5, A15", though the equation now defines C_(i,m) with 2^i T_(m−1)^(i)(1). The commit gives it the note
        "P-LL: the constant C_(i,m) is now that of Chebyshev-point interpolation (Duffin-Schaeffer), closed form in
        lem:layer-interpolation", so this item is closed.

## Observations (not findings)

- **Unchanged source names.** The rows for lem:layer-interpolation and eq:layer-interpolation keep their source names,
  "EL Lemma L.5 with A15's constant" and "EL L.5, A15". The edition now carries R4.5's C^DS at every i. A15 introduced
  only the Chebyshev–Lobatto constant at i = 1. The notes record the change, and the merge was notes-only by design. The
  coordinator may wish to add "R4.5" to source_name.
- **Stale 10^(−430) outside chapters/.** These were already flagged by R-P-LL:
  - INTEGRATION.md:960 and 1196 are log entries, historical as written;
  - PAPER.md (lines 76615, 76623 and 80454) is generated and stays stale until the next full assembly;
  - STATUS.md:57 now ends by recording the supersession.
- **The figures of M-LL.md §2 and §4 reproduce.** The byte counts, line ranges and check outputs all match at
  b6258b74.
