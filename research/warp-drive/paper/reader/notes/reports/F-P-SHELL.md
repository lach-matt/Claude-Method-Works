# F-P-SHELL: fix round on proofs/P-SHELL.md after R-P-SHELL

File: research/warp-drive/paper/reader/proofs/P-SHELL.md
- before: md5 cc81a1ade67f193e898240dee404db85, 759 lines
- after: md5 f797a039d96cf7a2dd7a79a1062d829d, 829 lines
  - section: lines 1-676
  - Placement: lines 678-803 (items 1-9)
  - Crosswalk rows: lines 805-829

Only this file was edited. Not committed. A coordinator snapshot commit (30c6d238) captured an intermediate state of the
file mid-round (md5 aac86b34...). The final state is the md5 above.

Drafting base for the Tier-dependent items:
- P-CIVP.md: md5 4d8ea745d570bfb2e6f4aa588d747da2 (HEAD and working tree agree).
- P-CIVP2.md: md5 924a45ecfbef762ee34a500044e9414f.
- Chapters at HEAD. Chapter 83: opening at lines 21-22, the paragraph after prop:loc-cones at 593-600, sec:loc-kid at
  602. Chapter 90: the line is at 210. Chapter 98: [Rac16] at 157.

## The 19 findings

| Finding | Status | Where and what |
|---|---|---|
| minor 1 | applied with a change | The argument is written in full (see note 1). |
| minor 2 | applied | rem:loc-shell-poisson in the reader's words, with 𝔖 from nit 3. |
| minor 3 | applied with a change | Full argument in a new opening paragraph of the proof (see note 2). |
| minor 4 | applied | (a) now begins "If D contains a neighbourhood of (d_j, c_k), then at every point of Z, …". |
| minor 5 | applied with a change | "locally bounded along the curve" in place of the reader's "bounded" (see note 3). |
| minor 6 | applied, one addition | Both sites: metric functions by continuity, q_out and q_in by (J3) of prop:loc-shell-junction (d) (see note 4). |
| minor 7 | drafted, pending the Tier 1/2 round | Item 2 re-based on the current Block A, rem:loc-cone-scope (iii) (P-CIVP.md lines 88-89). The Old occurs exactly once there. |
| minor 8 | drafted, pending | Item 5 is the reader's replacement; see note 5. |
| minor 9 | drafted, pending | New item 8; see note 6. |
| minor 10 | applied | η → ϖ at all four sites; see note 7. |
| nit 1 | applied | Step 1 reflowed: "(i)–(iii)" on one line. |
| nit 2 | drafted, pending | Item 4 "(lines 21–22)"; item 5 "line 210". |
| nit 3 | applied | 𝒮_k → 𝔖_k and 𝒮′_j → 𝔖′_j at all 10 + 10 sites, the crosswalk note of eq:loc-shell-singular included. The domains 𝒮_0, 𝒮_k^out, 𝒮_j^in, 𝒮_δ and 𝒮_w are unchanged. |
| nit 4 | applied | "with Ω the background's there" added for 𝒞_in in prop:loc-shell-cones. |
| nit 5 | applied with a change | See note 8. |
| nit 6 | applied | "Put c_1 := v_1 if p = 0 and d_1 := u_1 if q = 0" dropped; see note 9. |
| nit 7 | applied now, against current Tier 2 | See note 10. |
| nit 8 | pending | Nothing done until the Tier 2 prefix decision; see note 11. |
| nit 9 | not applied (optional) | See note 12. |

### Notes on the findings

1. **minor 1.** The proof of (d) now has two paragraphs in place of one.
   - *Depth k ≥ 1 along 𝒞_out.*
     - It states the induction hypothesis: the solution of depth k − 1 is within Cε in C^(k_(k−1) − 4) in the
       original angle.
     - It identifies Φ_k(u, ·) as the inverse of the flow of b(u, c_k, ·) ∂_ϑ. So Φ_k − id and Φ_k⁻¹ − id are within
       Cε in C^(k_(k−1) − 4).
     - It derives the forward bound C^(k_(k−1) − 5) = C^(6k_k + 18) = m_0 by the argument of the next paragraph, with
       Φ_k⁻¹ in place of Φ_k.
   - *Changing the angle back loses no derivative.* This paragraph is new.
     - The change back composes with Φ_k, multiplies γ_ϑ by (∂_ϑΦ_k)², and replaces b by (b − ∂_uΦ_k)/∂_ϑΦ_k.
     - It uses the decomposition F ∘ Φ_k − F̊ = (F − F̊) ∘ Φ_k + (F̊ ∘ Φ_k − F̊).
     - The first term is bounded by the chain rule.
     - The second term is bounded by the mean value theorem. Φ_k is the identity off a compact K ⊂ (0, π/2) and maps
       K onto K.
     - The factors (∂_ϑΦ_k)², ∂_uΦ_k, 1/∂_ϑΦ_k and ln ∂_ϑΦ_k are within Cε in C^(k_(k−1) − 5), and
       k_(k−1) − 5 ≥ k_k − 4.
     - So order k_k − 4 holds in the original angle. Along 𝒞_in the N_o data have order
       k_(j−1) − 4 ≥ 6k_j + 18.
   - The closing line now reads "as k_i − 4 ≥ k_(N−1) − 4 = 2 at every depth i".
   - The cascade k_(i−1) = 6k_i + 23 is unchanged. The theorem's C¹ claim is unchanged; it is not strengthened to C².
2. **minor 3.**
   - *The statement* carries the reader's extension to sets D′ that meet every coordinate line in an interval. The
     exception is stated exactly: the last sentence of prop:loc-shell-junction (a) holds with any sphere
     {(u′, c_k)} × S³ ⊂ D′ × S³ in place of {(0, c_k)} × S³, and with the part u ≥ u′ of the leaf in place of the leaf.
   - *The proof* opens with a new paragraph, "*The sets D′.*". It names the steps that use the past-set property:
     - the integration by parts along v- and u-intervals in lem:loc-shell-ricci (a);
     - the ODEs along curves and generators over the leaf's interval in prop:loc-shell-junction;
     - the rule for derivatives on the leaf in (d), which with the rest uses only the interval property.
   - It then checks, line by line, that 𝔏, 𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s] and 𝔏 ∪ D″ (D″ a past set of 𝒬
     relative to its corner) meet every line {u = u′} and {v = v′} in an interval.
   - The proof of (c) now cites the exception: "by the last sentence of (a) with Z in place of {(0, c_k)} × S³".
   - Why the change: the reader's wording ("vanishes along each integral curve … that starts at a point where it
     vanishes") drops the "these curves fill the leaf" half, which (c) needs on the new part of the leaf.
3. **minor 5.** Near the axes the coefficient L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) is bounded only on compact pieces of
   the leaf. Local boundedness is what uniqueness for a linear ODE needs.
4. **minor 6.** At the first site (proof of (c) of thm:loc-shells), "In the same way" now also says that q_in on N_o
   comes from (J3) across {u = d_j}. The reader's text left this implicit.
5. **minor 8.** Item 5 is the reader's replacement:
   - Old: the last two lines of Tier 1 placement item 7's New, "estimate ([[thm:loc-cone-development]]). Developments …
     not established ([[rem:loc-cone-scope]]).".
   - New: those two lines followed by the shell sentence.
   - The Old occurs exactly once in the current P-CIVP.md, which is the text chapter 90 will carry.
6. **minor 9.**
   - New item 8: the last sentence of the paragraph after prop:loc-cones, against Tier 1 placement item 4's New (current
     P-CIVP.md lines 1110-1112, once). It adds "except finitely many null shells along leaves of the two cones and data
     that are smooth except across such leaves ([[thm:loc-shells]])".
   - It adds a sentence for the case where Tier 2's item 3 is used instead.
   - Old item 8 "No other change" is now item 9, and says that no text outside items 1–8 changes.
   - One point for the re-base. The closing clause "and no other result of this paper uses these developments" is kept
     as the reader wrote it. It is true when "these developments" means the developments of the cone data of
     prop:loc-cones; no result takes those as input. But thm:loc-shells applies thm:civp-large to restricted cone data
     (Step 1). If the final Tier 1 text makes that clause read more broadly, it should become "and no result of this
     paper outside this chapter uses these developments".
7. **minor 10.**
   - η → ϖ at all four sites: the quantities list of lem:loc-shell-identities, 𝔞, "r̲ is built from ϖ = ∂_ϑ ln Ω",
     "For a round metric ϖ = 0". A grep finds no other η := ∂_ϑ ln Ω.
   - The remaining η are angles: (T1), the proof of (d), and prop:loc-shell-crossing (c).
   - ε_0 → ε_B and a_0 → λ_e: no site in this file. Here ε_0 is the smallness threshold of thm:loc-cone-development,
     still ε_0 at P-CIVP.md line 47. The file uses no a_0. "a = 0.70" is unchanged in Tier 1.
8. **nit 5.** The extra smallness is fixed where δ_e is chosen: g0 is defined in the gauge near
   [0, 3δ_e] × [0, v_1 + δ_e] and near [0, u_1 + δ_e] × [0, 3δ_e], and R > a there. At depth k the text then says that
   the rectangle spanned by N_o and N_i lies in that set. This gives R > a on N_o and N_i and g0 near the rectangle,
   which (T1) needs, without shrinking δ_e after it is fixed. δ_e still depends only on g0.
9. **nit 6.** In (d), "w … and ε_0, C > 0, depending only on g0, u_1, v_1, the leaves and the band" replaces
   "depending also on N" (N is determined by the leaves).
10. **nit 7.** One sentence is inserted after "continuous and cellwise smooth.": "Here and below a class solution in the
    gauge is meant in the sense of [[sec:civp-large]]: its functions are smooth off the axes and the metric extends
    smoothly to them; it need not equal g0 near the axes." The paragraph is reflowed. When the Tier 1/2 round defines the
    term once, this sentence is to be re-pointed or dropped.
11. **nit 8.** If the Tier 2 prefix changes, these references follow:
    - in the section: civp-large ×9, def:civp-large-data ×4, eq:civp-large-band ×1;
    - in the Placement: civp-large ×2, civp-large-beyond, civp-large-domain and civp-large-data ×1 each.
    The pending key civp-large-at-a-corner is kept as it is, as instructed.
12. **nit 9.** The reader marks it optional. It needs a literature entry (for example the four-dimensional
    crossing-shell relation of Dray and 't Hooft or Barrabès and Israel), checked against its source and entered in the
    references. This round cannot check that source. An unchecked citation would break the edition's rule that the
    literature is cited exactly. No proof uses it.

## Labels

- No label was renamed or removed. The 19 defined labels are unchanged.
- Symbol renames, not labels: 𝒮_k → 𝔖_k and 𝒮′_j → 𝔖′_j (nit 3), η → ϖ (minor 10).
- Placement numbering: the new item is 8, and old item 8 became 9.

## Other edits

- **Crosswalk rows.**
  - All 19 line numbers are refreshed, and each row points at its label's line. Changed rows: def 46, eq-einstein 54,
    eq-dust 56, lem-ricci 69, eq-singular 76, lem-identities 127, eq-trace 135, prop-junction 167, eq-torsion 173,
    eq-conservation 181, rem-poisson 262, def-data 275, prop-cones 295, thm 355, eq-bands 360, prop-crossing 524,
    eq-crossing-rule 545, rem-scope 657.
  - Notes are extended for rem:loc-shell-poisson (S^αβ comes from the Einstein tensor; the 𝔖 are trace-free),
    thm:loc-shells (the derivative count) and prop:loc-shell-crossing (the D′ sets; a neighbourhood for the crossing
    rule).
- **Placement intro.** "every old text occurs exactly once … after the text of Tier 1 … and the section of Tier 2 … are in
  place and their placements applied". It also says that items 2, 5 and 8 are written against the current Tier 1 text
  and are to be re-based.

## Checks

- **Line length.** Every line of the file is at most 121 characters by Unicode count, except the tab-separated crosswalk
  rows, as before.
- **Line starts.** No wrapped line starts with a Markdown marker. The only hits are the reference-list item of item 6,
  which is meant, and three indented display continuation lines that were already there.
- **Scratch build** (scratch/fshell/build: Tier 1 Blocks A and B, Tier 2 and this section in chapter 83; Tier 1 items 3,
  4 and 7 and this file's items 2-6 and 8 applied).
  - Every Old text of this file occurs exactly once.
  - The section is 53.6, and its theorem is Theorem 53.46.
  - After label resolution, no line of the section or of the placed texts is longer than 121 characters.
  - `assemble.py`: the only problems are 9 undefined Tier 2 Appendix A labels (thm:std-cctw-*).
  - `lint.py --chapters`: the only hits in this section are the two pending markers (T2) and (T1), kept as they are.
- **Pending markers.** Both are unchanged.

## Incident (corrected)

Early in the round I ran `python3 assemble.py --help` in the real directory. The script ignores unknown flags, so it
assembled and rewrote PAPER.md.
- I restored PAPER.md from HEAD at once with `git checkout -- PAPER.md`.
- PAPER.md had no working-tree changes before; its last commit is 13:30.
- Nothing else was written. No computations/NUMBERS.tsv exists.
- PAPER.md is clean now.

## Still to do after the Tier 1/2 round

When the final texts arrive:
- Re-base items 2, 5 and 8, and nit 2's line numbers.
- Re-point or drop the nit 7 sentence once "class solution in the gauge" is defined once.
- Follow the Tier 2 label prefix if it changes (nit 8).
- Follow Tier 2's renaming of u1 and v1. The section has u_1 or v_1 on 31 lines (46 occurrences):
  - Q1 = [0, u_1] × [0, v_1] "as in [[sec:civp-large]]", the band and leaves conventions, Step 1's "d_1 and c_1 in
    place of u_1 and v_1", the extension paragraph and the widths of (d);
  - thm:loc-shells (d) takes u_1 and v_1 "as in [[thm:loc-cone-development]]", which is Tier 1's pair and is not
    renamed.
  - Which occurrences follow depends on the new names.

---------------------------------------------------------------------------------------------------------------------

# Re-base on the final Tier 1/2 texts (df9a4c35)

Base texts:
- P-CIVP.md: md5 f8a1e948a7f9c53831719f5d526cc3a8, 1319 lines.
- P-CIVP2.md: md5 e80ea7a4542d128253dccbb16a7dd408, 841 lines.
- Chapters at HEAD.

File: proofs/P-SHELL.md, md5 20b99739d608bbfe1f5c4ff963e331a1, 833 lines.
- Section: lines 1-682.
- Placement: lines 684-807.
- Crosswalk: lines 809-833.

Snapshot commit af953435 captured an intermediate state; the md5 above is final. Not committed by me. In the real
directory, nothing other than this file was touched; PAPER.md is clean.

## New finding: the section needs the old, broader sense of "class solution in the gauge"

Tier 1's definition (sec:loc-cone-setting, which Tier 2 now refers to) requires the functions to equal the background's
near the axes. Five sites in this section use the term for solutions that need not equal g0 near the axes:
1. The paragraph after def:loc-shell-solution: every solution with null shells is a class solution on each cell; and
   p = q = 0 gives a class solution.
2. The hypothesis of prop:loc-shell-junction. prop:loc-shell-crossing applies it to solutions that need not equal g0
   near the axes:
   - in (a), to general solutions and to round g;
   - in (b), to the round extension;
   - in (d), to every solution of def:loc-shell-solution.
3. The proof of prop:loc-shell-crossing (b), in two places: "a round class solution with the phases v and u …", and
   "each closed cell carries a class solution …" for the round extension.

Read in Tier 1's sense, these sites would be wrong. prop:loc-shell-crossing (b), and the general and round claims of (a)
and (d), would lose their footing.

**Resolution in the file, open to your decision.**
- In "Leaves and cells", nit 7's sentence now points to Tier 1: "A class solution in the gauge is one in the sense of
  [[sec:loc-cone-setting]], with the corner at S and g0 as the background, as in [[sec:civp-large]]; its functions equal
  g0's near the axes."
- It defines a *class solution in double-null form*: Tier 1's definition without the condition near the axes (the old
  Tier 2 sense), smooth on D × S³ with the axes included.
- The new term replaces the old one at exactly those five sites.
- Every other use keeps Tier 1's sense, and at each of them the solution equals g0 near the axes:
  - (T1) and (T2);
  - Steps 1–4 and (c) of thm:loc-shells;
  - prop:loc-shell-crossing (c).
- The alternative, if you prefer no new term: restrict def:loc-shell-solution to solutions equal to g0 near the axes.
  Then prop:loc-shell-crossing (b) and the round part of (a) must be dropped or restated, and rem:loc-shell-scope (iii)
  changes.

## The other Tier 2 changes, followed

- **𝒪 and Q1.** "Leaves and cells" now takes g0, Q1, the open set 𝒪 ⊃ Q1 and the band from sec:civp-large. g0 is
  given on 𝒪 × S³ and solves eq:two-dust-limit where u, v ≥ 0. The same 𝒪 is used in:
  - the choice of δ_e in (d);
  - prop:loc-shell-crossing (c), "the open set 𝒪 of [[sec:civp-large]]". prop:loc-cone-local's final hypothesis, a
    solution on 𝒪 ∩ {u ≥ u_Q, v ≥ v_Q}, holds there.
- **(T2)'s closing sentence.** It now reads: "uses of g0 only that it is round, with b = 0, given on 𝒪 × S³ and a
  solution of [[eq:two-dust-limit]] at the points of 𝒪 with u, v ≥ 0, and its corner step, [[prop:civp-large-corner]],
  already works at every corner of Q1". The pending marker and the statement are unchanged.
- **"Cone data on Q1".** The new term is used in (T2), Step 1 ("cone data on 𝒫_0 in the sense of [[def:civp-large-data]]")
  and the last sentence of def:loc-shell-data.
- **Renames from earlier rounds.** u1/v1 → u_1/v_1 and R → 𝒬: this section already used those forms. η → κ: the η here
  are Tier 1's, in (T1), the proof of (d) and prop:loc-cone-local in (c), so nothing changes. k → w: Tier 2's w(u, v)
  does not appear here. This section's w and w_i are widths, and the overlap is in name only.
- **No other Tier 2 change touches this section:** m := 114, the replaced markers, lem:civp-large-free and
  lem:civp-large-rectangle.
- **nit 8.** There is no prefix change, so nothing to do.

## Placement re-based

- **Intro.** Items 2, 3, 5 and 8 are now said to be written against the final Tier 1 and Tier 2 texts.
- **Item 1.** The section goes immediately before sec:loc-kid. It depends only on Tiers 1 and 2, so it follows any further
  section placed after Tier 2; Tiers 3–5 also place sections there.
- **Item 2.** The Old is now the single second line of rem:loc-cone-scope (iii): "that are only bounded, or measures
  (shells), are not covered. For the 3 + 1 problem …". Tier 3's item 4 rewrites the end of (ii) and its own Old includes
  the line "the background there. (iii) …". This item therefore no longer touches that line and composes in either order.
- **Item 3.** Re-based, because Tier 2 reflowed rem:civp-large-domain. The Old now begins "are defined. The data must
  equal …"; the New is the same words, reflowed.
- **Item 5.** The Old is unchanged and occurs once in Tier 1's final item 7 New, chapter 90 line 210. The heading now
  says that Tier 2's item 4 second pair defers to Tier 1's item 7.
- **Item 8.** Re-based on Tier 1's final item 4 New, its last two lines: "asserted for cone data that differ … no other
  result of this paper uses these developments." The fallback for Tier 2's item 3 is removed, since that item now defers.
- **nit 2.** "lines 21–22" and "line 210" are confirmed at HEAD; chapter 83 593–600 and 602, and chapter 98 157, are
  unchanged.

## The clause "no other result of this paper uses these developments"

Read literally, the clause is false once this section is placed:
- thm:loc-shells Step 1 applies thm:civp-large to restrictions of exactly these cone data;
- the proof of (d) applies thm:loc-cone-development at S to extended data.

Item 8's New therefore reads: "…, except finitely many null shells along leaves of the two cones and data that are smooth
except across such leaves, which [[thm:loc-shells]] develops slab by slab with [[thm:civp-large]] and
[[thm:loc-cone-development]]; no result of the other chapters uses these developments."

I checked that the narrowed clause holds for the texts placed so far:
- No chapter at HEAD outside ch:localised-data cites thm:civp-large, thm:loc-cone-development, prop:loc-cone-local or
  thm:loc-shells.
- The blocks of Tiers 4 and 5 for chapter 81 cite none of them either.
- The other placements touch descriptive text only (ch:scope, ch:theorems, ch:introduction).
- Tier 5's own placement uses the same wording, "No result of the other chapters uses these developments".

**For the merge.** The placements of Tiers 3, 4 and 5 also rewrite this sentence:
- Tier 3: item 3's merged paragraph.
- Tier 4: its item 4, against Tier 2's old item-3 text, which no longer exists.
- Tier 5: its item 4, whose New says "Densities that are only bounded, or are measures, are not covered".

The last is no longer true once null shells are covered; the merged sentence should carry item 8's exception. Item 8's
text says so.

## Scratch build with both final tiers

The build (…/scratchpad/reader/scratch/fshell/build, script build2.py) applied:
- Tier 1: Blocks A and B, items 3–7;
- Tier 2: the section, items 4, 7 (Appendix A) and 8;
- this file: the section and items 2–6 and 8.

Results:
- Every Old occurs exactly once.
- `assemble.py`, scratch copy only: 0 problems. The section is 53.6, and thm:loc-shells is Theorem 53.48.
- No line of the section or of the placed texts is longer than 121 characters after label resolution.
- `lint.py --chapters`: 2 hits in all chapters, the two pending markers (T2) and (T1) of this section.
- In the file itself: every line is at most 121 characters (Unicode count), apart from the tab-separated crosswalk rows.
  The only line starting with "- " is the reference-list item of item 6.
- All 19 crosswalk rows point at their labels.

Aside, outside my file: final Tier 1 prop:loc-cone-local has a short line "Λ, d and" (P-CIVP.md, statement of
prop:loc-cone-local). It is harmless in rendering, but it is a stray wrap.
