# R-P-ADM: independent reading of proofs/P-ADM.md

File read: `research/warp-drive/paper/reader/proofs/P-ADM.md`, md5 0fac203dc2b9b29c96012e7d2d0d1e4a, 1,050 lines.

An addendum at the end of the findings gives the state at 766723cc, after P-T49 was merged and revision b of this file
was committed.

The chapters changed three times while I read:
- P-ADM's base, 155f39c6.
- M-K (7e73223b): P-K merged into chapters 03, 46, 63, 71 and 90.
- M-T78 (7854b15c): P-T78 merged with its own items 6–11. The HEAD at the end of reading is c1021295, whose
  chapters are those of 7854b15c.

P-T49 was revised in the same window (F-P-T49; md5 d2cad288… at the end). Line numbers `NN:line` below are in the
chapters at c1021295 unless marked otherwise. I did not read `method/`, `drive/`, `extracted/` or `recovered/`, and I
edited nothing in the repository.

**Verdict: NOT CONFIRMED. 0 Major, 7 minor, 12 nits. The mathematics is correct.**

I checked the following in full, for every z ∈ (0, ½]:
- part (g);
- the implication (C1) + (C4) ⇒ (C4′), and (f) under (C4′);
- the lead;
- prop:vi-c-adm-exist;
- thm:vi-c-adm-holds, site by site.

I found no mathematical error and no use of simplicity, Z_exc, (C2), (C3), u5 or (C4) that the file misses. Every
finding is about placement, notation or wording. Three things make the file not mergeable as it stands:
- three crosswalk rows are spliced into the new text of item 13;
- item 19 deletes the blank line in front of the new definition;
- six old texts and the P-K and P-T49 interactions are out of date, because P-K and P-T78 were merged with their own
  items.

---

## Findings

### m1. minor (merge-blocking): crosswalk rows inside item 13; the crosswalk section still has its placeholder (lines 414–420, 881)

Current text, item 13 (lines 414–420):

    New, the three lines:
        def:vi-c-admissible	paper/reader/proofs/P-ADM.md:17	P-ADM, Definition (admissible points)	new: (P0)–(P4)
        prop:vi-c-adm-exist	paper/reader/proofs/P-ADM.md:52	P-ADM, Proposition (existence)	new: contains the former rows
        thm:vi-c-adm-holds	paper/reader/proofs/P-ADM.md:95	P-ADM, Theorem (admissible points)	new: thm:settling holds there
    continues ℳR meromorphically to {Re λ < b̃}. In the strip {b < Re λ < b̃}, of width at most 1, the poles are at the

And line 881: `CROSSWALK-PLACEHOLDER`.

What is wrong:
- Item 13 announces three lines and gives six. Applied as written, it puts three tab-separated rows with file paths
  into the proof of lem:iii-g4-3-4 in chapter 36; the edition's lint flags them as file names.
- The crosswalk section gives no rows at all.

The writer's scratch merge applied texts from its own table, not from this file, so its check could not see this.

Replacement:
- Delete lines 415–417.
- Replace line 881 by those three lines, unchanged (four-space indent, tabs between the columns, as P-T49 writes its
  rows).

### m2. minor (merge-blocking): item 19 removes the blank line before the definition (lines 482–492)

Current text: the header says "(lines 1703–1709)", then "Old, the seven lines:". The old block is the six text lines
"made. m₀ > 0 is fixed …" to "… data class of [[thm:iii-c1-3-1]]." plus the blank line 1709 (now 1712). The new block
is "the six lines", with no blank line. Item 20 then replaces rows c1–c4 by "Block A1 …, then a blank line, then …
row c1".

What is wrong: with the two items applied, "**Definition {#def:vi-c-admissible}**" follows the paragraph with no
blank line, so it starts in the middle of the paragraph. The writer's scratch tree shows exactly this, at its line 1712.

Replacement: in the header of item 19, replace "(lines 1703–1709).* Old, the seven lines:" by
"(lines 1706–1711).* Old, the six lines:", and delete the two blank lines 490–491 (the old block then ends at line
489). Equivalently, keep the header and write "New, the six lines, then a blank line:".

### m3. minor (merge-blocking): six old texts no longer occur, because P-T78 was merged with its own items (items 21, 27, 31, 32, 37, 44; lines 283–287, 902–936)

At P-ADM's base all 44 old texts occurred exactly once. They still did after the P-K merge, but at shifted lines:
- chapter 46: +3;
- chapter 71, items 31 and 33–38: +3; item 32: +320;
- chapter 03: +7;
- chapter 90: +2.

M-T78 then applied P-T78's items 6–11 itself, instead of P-ADM's combined items. Now 38 old texts occur once and
these six do not:

| item | P-T78 item that rewrote the place | current old text (each occurs exactly once at c1021295) |
|---|---|---|
| 21 | 6 (rows u3, u4) | 46:1730–1741, twelve lines, "**u2.** γ_(Υ,H) ∈ (0, ε_0] …" to "𝖹_exc on c1–c3; u3." (u3 now has three lines) |
| 27 | 7 (step (2)) | 46:1791–1801, eleven lines, "(1) (v_C, e_C, C_0) := …" to "every σ with Im σ ≥ 0; so it imposes no further condition." |
| 31 | 8 (rem:ec-point-outside) | 71:55–75, twenty-one lines, the whole remark as P-T78 item 8 gives it |
| 32 | 10 (rem:ec-not-evaluated) | 71:5285–5293, nine lines, "positive by the proof of [[thm:settling]]. …" to "([[rem:ec-lb-unbounded]]). Among the inputs" |
| 37 | 9 (rem:ec-lb-conditions) | 71:1786–1790, five lines, "It uses none of the thresholds …" to "… constructions of [[sec:ec-floor]] are run" |
| 44 | 11 (sec:scope-constants) | 90:85–88, four lines, "Explicit values stop upstream …" to "… give constants without a value; and the" |

The new texts of all six still fit these old texts: each ends where the new old text ends. Item 37 is the case P-ADM
did not foresee, because P-T78 gained that item after P-ADM was written.

Replacement:
- In each of the six items, replace the old block by the lines listed above, verbatim, and the count ("the twelve
  lines", "the nine lines", "the four lines").
- In items 21, 27, 31, 32 and 44, delete the words "(combined text: …)". In item 37, write nothing about P-T78.
- Lines 283–287: replace "Line numbers are those of the chapters after the merge of P-LB (commit a722cb42)" by "Line
  numbers are those of the chapters at c1021295 (P-LB, P-K and P-T78 merged)", and correct the remaining line numbers
  of the item headers (current values: items 19–20 at 46:1706 and 1713; 22–26 at 46:1745, 1751, 1767, 1774, 1780;
  28–29 at 46:1825, 1834; 33–36 and 38 at 71:1553, 1714, 1734, 1776, 1794; 42 at 03:361; 43 at 90:79).
- Lines 923–936 (the paragraph "P-T78"): replace the paragraph by one sentence: "P-T78 is merged (7854b15c); the old
  texts of items 21, 27, 31, 32, 37 and 44 are its merged texts, and the labels eq:tf-lambda, eq:tf-lambda-point,
  prop:tf-gauge-explicit, lem:tf-lin-reduction and the parts (a), (b) of lem:iii-d-7-1 are in the chapters."
- Lines 902–910 ("Merge order"): delete the clauses on P-T78 and the description of the scratch check. Keep that P-T49
  must be merged before this file or together with it (for thm:t49-point).

The paragraph's item numbers are also out of date. P-T78's final file has items 9 (rem:ec-lb-conditions),
10 (rem:ec-not-evaluated), 11 (sec:scope-constants) and 14 (the "unchanged" list). P-ADM still calls them 9, 10 and 11.

### m4. minor (merge-blocking): P-K is merged, and four of its merged sentences still say the point lies "outside" (lines 981–996)

Current text (lines 981–982): "*P-K (not merged; its file is still changing).* Its texts say that the computational
point lies outside the set on which [[thm:settling]] is proved; after this file each should say that it is not shown
to lie in it."

What is wrong: M-K (7e73223b) merged P-K, and proofs/P-K.md is retired. So the four substitutions must be placement
items on the chapters. Without them, after P-ADM the paper still says, in four places, that the point lies outside the
proved set, while def:vi-c-admissible no longer excludes it.

P-K's text 8 (chapter 90) is merged too, and item 43's old text still occurs once (90:79–81). So the paragraph on
text 8 is moot.

Replacement: delete lines 981–996 and add the four items below after item 44, renumbering item 45 ("Unchanged") to
49. Add the crosswalk note "point not shown to lie in the proved set (P-ADM items 45–48)" to these rows:
- chapter 03, thm:settling;
- chapter 63, thm:own-data;
- chapter 71, sec:uc-data-order and rem:uc-data-order-limits.

*45. [[ch:theorems]], the paragraph after [[thm:settling]] (lines 316–318).* Old, the three lines:

    point of [[def:ec-point]], which lies outside that set ([[rem:ec-point-outside]]), and at one admissible choice of the
    weights, orders and inner products, d is at most an integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]]), and K at most
    one below 3.45745 × 10⁵¹.

New, the three lines:

    point of [[def:ec-point]], which is not shown to lie in that set ([[rem:ec-point-outside]]), and at one admissible choice
    of the weights, orders and inner products, d is at most an integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]]), and K at
    most one below 3.45745 × 10⁵¹.

*46. [[ch:own-data]], the paragraph after [[thm:own-data]] (line 71).* Old, the line:

    which lies outside the set where the theorem is proved. The order k_P is what the subtracted

New, the line:

    which is not shown to lie in the set where the theorem is proved. The order k_P is what the subtracted

*47. [[ch:explicit-constants]], the opening paragraph of [[sec:uc-data-order]] (line 4925).* Old, the line:

    follow from it use the bounds for d at the computational point, which lies outside the set on which

New, the line:

    follow from it use the bounds for d at the computational point, which is not shown to lie in the set on which

*48. [[ch:explicit-constants]], [[rem:uc-data-order-limits]] (line 5226).* Old, the line:

    point, outside that set ([[rem:ec-point-outside]]). L_0 and J depend on ℓ_0 and ℓ_I, on the gauge parameters through

New, the two lines:

    point, which is not shown to lie in that set ([[rem:ec-point-outside]]). L_0 and J depend on ℓ_0 and ℓ_I, on the
    gauge parameters through

Widths are 121, 118, 30, 102, 109, 112 and 24 characters. Each old text occurs exactly once at c1021295.

### m5. minor: the P-T49 replacement for rem:t49-scope repeats two imprecisions R-P-T49 found, and no longer matches P-T49 (lines 966–978)

Current text (lines 973–976): "The computational point is not in 𝖧, because h_* ≤ 10⁻⁶ and 𝖧 is open at h_*, …
Away from the point, 𝖹₂ and Z_exc are empty and (C3) holds at every h ∈ (0, 10⁻⁶] ([[thm:t49-uniform]]), so
𝖹 = 𝖹₁ ∪ 𝖹₃ and the choice of [[prop:vi-c-adm-exist]] meets no exclusion in z."

What is wrong:
- R-P-T49 (m8) showed two problems:
  - "𝖧 is open at h_*" is not the reason. The reason is 𝖧 ⊂ (0, h_*) and h_* ≤ 10⁻⁶.
  - thm:t49-uniform (iii) makes Z_exc empty only where (C2) holds.
- P-T49 has been revised accordingly. Its anchor "… and the order of choices in [[thm:vi-c-2-1]] meets no exclusion
  in z." now reads ", and, as (C2) holds at every h ∈ 𝖧, the order of choices …".
- The clause "the choice of prop:vi-c-adm-exist meets no exclusion in z" is empty: that proposition asks none.
- P-T49's revised item 7 already says that P-ADM's item 31 replaces it when both merge together, which agrees with
  Part C.

Replacement: in lines 966–968, instead of "the first four sentences, from … through … meets no exclusion in z.", write
"replace the remark from its first line through '… meets no exclusion in z.' (P-T49 lines 323–329 as revised)". In
place of lines 970–976, use:

    **Remark {#rem:t49-scope}** (What this decides.) At the damping point the exclusions of [[eq:iv4-0-1]] and
    [[prop:iii-f1-2-3]] (e) are met, although [[def:vi-c-admissible]] does not ask them: h = 10⁻⁶ ∉ 𝖹, (C1)–(C4) hold,
    and Z_exc = ∅ at h = 10⁻⁶, so z = 4·10⁻⁶ ∉ Z_exc ([[thm:t49-point]]); every indicial root of L̂_b(0) at the
    computational point is simple. The computational point is not in 𝖧, because 𝖧 ⊂ (0, h_*) and h_* ≤ 10⁻⁶, and
    whether it is admissible is decided by the conditions that [[rem:ec-point-outside]] lists as open. Away from the
    point, 𝖹₂ is empty and (C3) holds at every h ∈ (0, 10⁻⁶], and Z_exc is empty at every h at which (C2) holds
    ([[thm:t49-uniform]]); so 𝖹 = 𝖹₁ ∪ 𝖹₃. The set 𝖹 meets I

Then keep the rest of the remark as it stands, from "([[prop:t49-six]]); whether 𝖹 ∩ I is finite …". The line
"(d) Z_exc …, written 𝖹_exc in row u5 …" (lines 958–966) still matches the revised P-T49 (its line 39); keep that
replacement.

Whichever of P-T49 and P-ADM merges second has to be rebased on the other's text.

### m6. minor: the names (P0)–(P4) are already taken by lem:iii-i15-1-1 (whole file)

Chapters 38a and 40–44 cite the properties (P1)–(P5) of lem:iii-i15-1-1 (38a:47) by their bare names, for example:
- 41:69–73;
- 41:586 ("The roots, which do not depend on b ((P2))");
- 43:68 ("[[lem:iii-i15-1-1]] (P2)").

Chapter 71 also uses (P1), (P2) locally, at 71:825–854.

The new texts use the same bare names for something else:
- item 22 (row b2): "b near b₀ as (P1), (P4) and [[sec:iii-j-1]] ask";
- item 36: "(C4′) … ((P2))";
- item 37: "not (P1), (P3) or (P4)";
- Part C and thm:vi-c-adm-holds throughout.

So "(P2)" means "the roots do not depend on b" in chapter 41 and "(C4′)" in chapters 46 and 71. "(P4)" means "the
augmented low-energy theory at b" in chapter 41 and "Λ_tf < 1 with tf-admissibility of □^C" in row b2.

Replacement: rename the clauses of def:vi-c-admissible to (AP0)–(AP4), a name no chapter uses, at all 55
occurrences in the file. These are lines 24, 26, 29, 32, 36, 40, 43, 48, 55, 59, 61–64, 73, 74, 85, 86, 88–90, 97,
110, 112, 113, 122, 125, 132, 135, 143, 203–206, 209, 210, 214, 218, 415, 547, 550, 717, 733, 736, 737, 750, 913,
914, 924, 933, 935, 956, 1014, 1025 and 1050. Then refill lines 113, 956 and 1014, which become 122 characters. Any
other free name serves as well.

### m7. minor: three sentences of chapter 33 become false at the merge, and the file only suggests them (lines 1003–1016)

Current text (line 1003): "*Chapter 33 (being edited in parallel; not changed here).* Three sentences there describe the
parameter set of the paper's theorems as h ∈ 𝖧 and go stale after this file. Suggested texts, …"

What is wrong: after P-ADM, three sentences of chapter 33 are false, because the theorems are stated at admissible
points, where h need not lie in 𝖧:
- 33:3129: "the set 𝖧 … on which the theorems of this paper are stated";
- 33:3531: "The theorems of this paper take h in 𝖧";
- 33:125: "… and so do all later chapters".

They are not stale wording but false statements, so P-ADM should not merge without them. Each of the three old
sentences occurs exactly once in chapter 33 at c1021295 (I checked them with line breaks removed). Chapter 33 was last
changed at 281f5587 and is confirmed (R2-F-G24); P-T49 items 3 and 4 touch other lines of the same paragraphs.

Replacement:
- Turn the three suggestions into placement items 49–51, each giving the lines as they stand.
- Fix the grammar of the first: "and so do all later chapters, which hold as well with γ_C = h⁻¹ at every admissible
  point" makes chapters "hold", and it leaves out chapter 33's own sec:iii-e-2 to sec:iii-e1-3, which
  thm:vi-c-adm-holds (1) also covers. Use instead: "Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses
  these values, and so do all later chapters; the results that [[thm:vi-c-adm-holds]] (1) lists hold as well with
  γ_C = h⁻¹ at every admissible point ([[def:vi-c-admissible]])."
- Keep the other two texts as suggested.

---

## nits

### n1. Block B2, line 176: the coverage sentence names two chapters

Current: "covers the roots with real part in (−3, 0] that [[ch:s16]] and [[ch:s17]] use."

Part (g) is also what sec:iii-f4-5 (chapter 34) and lem:iii-i12-2-3 (chapter 41, item 16) use.

Replacement: "covers the roots with real part in (−3, 0] that the later chapters use."

### n2. Block A1, line 48: (P1)–(P4) should be (P0)–(P4)

Current: "through (P1)–(P4), and the simplicity of indicial roots …"

The requirement h ∈ 𝖧 is also used through h < 10⁻⁶, that is through s_C > 100 and (C1), which come from (P0).

Replacement: "through (P0)–(P4), and the simplicity of indicial roots of L̂_b(0) only where (P0) gives it
([[prop:iii-f1-2-3]] (g))." (118 characters.)

### n3. Block A3, line 86: tf-admissibility of L_b needs (P0) as well

Current: "γ_Cv_C > 100, which is (C5), and (C1) holds; by (P4), L_b^(·) is tf-admissible with every weight in (0, 1]"

Replacement: "γ_Cv_C > 100, which is (C5), and (C1) holds; by (P0) and (P4), L_b^(·) is tf-admissible with every weight
in (0, 1]" (115 characters, one line). Block A1 (line 43) already says "By (P0) and (P4)".

### n4. Items 18 and 37: ε_0, ε_1 and 𝖹_exc lose their definitions with rows u2–u5 (lines 479–480, 751)

Rows u2–u4 defined ε_0 and ε_1 as "that of [[prop:iii-d1-4-1]]", and row u5 defined 𝖹_exc. All of them are removed.
Row b3 uses ε_0 for another constant, the one of (B5). Block A1 and Part C use prop:iii-d1-4-1's own ϵ_0 and ϵ_1.

Replacements:
- Line 479: "(0, ε_0], e_Υ ∈ (0, min(ε_1, ½)]" → "(0, ϵ_0], e_Υ ∈ (0, min(ϵ_1, ½)]".
- Line 480: "min(ε_1, ¼)" → "min(ϵ_1, ¼)".
- Line 751: "γ_(Υ,H) ≤ ε_0, e_Υ < ε_1, γ_Υ < ε_1 or z ∉ 𝖹_exc" → "γ_(Υ,H) ≤ ϵ_0, e_Υ ≤ ϵ_1, γ_Υ < ϵ_1 or z ∉ Z_exc".
  prop:vi-c-adm-exist takes e_Υ ≤ min(ϵ_1, ½), hence ≤.

Widths are unchanged.

### n5. prop:vi-c-adm-exist: the statement fixes the neighbourhood, but the proof may shrink it (lines 55, 64)

Line 55 says the point is admissible "with the neighbourhood ℬ(γ_(Υ,H)) of [[prop:iii-d1-4-1]] in (P3)". Line 64
says "for b ∈ ℬ(γ_(Υ,H)), shrunk if necessary so that (Dyn) holds on it".

Replacement for line 55: "neighbourhood ℬ(γ_(Υ,H)) of [[prop:iii-d1-4-1]], intersected with the ball ℬ_VI of
[[thm:vi-b1-5-1]], in (P3). …" (refill). Alternatively delete "shrunk if necessary …" if ℬ(γ_(Υ,H)) already lies in
the region where (Dyn) is assumed.

### n6. thm:vi-c-adm-holds, (f) and (l): the lists of sites are not complete (lines 123–125, 139–143)

The proof says "We list every way …". These sites use the same inequalities and are not named:
- 36:673 and 36:730 (2γ_Υ < s_C);
- 36:1090 and 45:1649 (0 < e_Υ < 1);
- 38:53 (s_C > 100) and 38:1274;
- 39:962, 39:1058 and 41:448 (ℓ_I < 3/2 + s_C);
- 46:1851–1852 (sec:s27-class).

All of them follow from (P0) or from row d2, so nothing is uncovered.

Replacement for line 143 (two lines, 116 and 118 characters):

    [[prop:iii-f1-2-3]] and in [[lem:iii-g1-1-3]]. These follow from (P0), as [[def:vi-c-admissible]] records; so do the
    other uses of these inequalities, of s_C > 100 and of the bound ℓ_I < 3/2 + s_C of row d2 in [[ch:s17]] to [[ch:s27]].

### n7. Item 41, line 819: the last line is the single word "A"

Replacement for lines 818–819:

    them, and d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products
    ([[thm:uc-integer]]). A

### n8. Part C, lines 223–224, and 71:153, 71:1413: still phrased for h ∈ 𝖧 (depends on the cap)

Current (Part C): "For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), …"

The sentence is true, but the theorems are now stated at admissible points. The same holds for:
- 71:153: "[[thm:settling]] takes ε_K < ε_ind(h) ≤ δ_50 < 5.019·10⁻⁸ for every h ∈ 𝖧";
- 71:1413: "The same bound holds at every h ∈ 𝖧". This one is true at every h.

Replacement (Part C, lines 223–224 become three lines of 108, 117 and 108 characters; line 225 is unchanged):

    hold. Every number of this chapter that depends on the point is stated at it. At every admissible point with
    (e_Υ, γ_Υ) = (1/100, 1/100) the theorems use only 0 < ε_ind(h) ≤ δ_50 ((P2) and [[prop:iii-f1-2-3]] (f) for the first
    inequality, [[prop:np-10-52]] (iii) for the second), and the lower bound of [[thm:loss-d]] uses besides only

prop:np-10-52 (iii) defines ε_ind(h) only for h ≤ 10⁻⁶. If the cap is removed, insert "and h ≤ 10⁻⁶" after
"(1/100, 1/100)". The two sites in chapter 71 can be left, or re-phrased the same way.

### n9. Item 39 (lines 790–793): the reason given is the old threshold, not the new condition

"(γ_Υ, e_Υ) = (1/100, 1/100) are not shown to lie below the thresholds of prop:iii-d1-4-1" is true. But under the new
definition the point is not shown admissible because (P3) is open there, together with the first two open items.

Optional replacement for the clause: "and the invertibility (P3) of [[def:vi-c-admissible]] is not shown at
(γ_Υ, e_Υ) = (1/100, 1/100)" (refill).

### n10. Notes of the lead (lines 256, 269)

- (U4) leaves out two citations of lem:iii-g4-1-1: 36:1118, which uses part (3), and 36:1375, which uses part (2)
  inside the proof of lem:iii-g4-3-4 at the roots of the strip. The second is covered, as at 36:1360.
- Line 269 lists cor:iii-g2-3-2 among the places that "use no simplicity". It uses simplicity, through
  thm:iii-g2-3-1, for μ ∈ 𝒲(ℓ_K) ⊂ (−3, 0]; this is covered by (g).

Notes only; no chapter text changes.

### n11. Crosswalk notes and interactions, lines 897–898 and 919–921

- The notes give none for item 40 (00-front, the abstract) and none for the new items of m4.
- Line 919 says items 30, 31, 32, 40, 41 and 42 change "outside". Items 33, 39 and 43 do too.

Add the notes, and write "Items 30–33 and 39–43".

### n12. (P3) names its neighbourhood ℬ(γ_(Υ,H)) although it depends on the whole point (line 32)

In prop:iii-d1-4-1, ℬ(γ_(Υ,H)) depends on γ_(Υ,H) alone. In (P3) it is existential at the point. Keeping the
symbol is harmless, as row b2 reads it, but "(depending on 𝗉)" after its first use would prevent a misreading.
Optional.

### Addendum: the state at the end of reading (HEAD 766723cc)

Two more things landed while I wrote this report:
- M-T49 (fb87f2fc) merged P-T49, and proofs/P-T49.md is retired.
- The writer committed "P-ADM revision b" (d264cbc4), which removes the cap; the file's md5 is now 06a69312….

This report is on 0fac203d, as asked. Against the chapters at 766723cc, the reviewed file's old texts stand as follows:
- *The six of m3 still do not occur.* Of their rebased texts, items 21, 27, 32, 37 and 44 still occur once, at
  46:1730, 46:1791, 71:5286, 71:1788 and 90:85.
- *Item 31 moved again.* rem:ec-point-outside is now 71:55–77, twenty-three lines, because P-T49's text 7 inserted its
  sentence ("Its damping and gauge parameters avoid the countable exclusions: h = 10⁻⁶ ∉ 𝖹, and the set 𝖹_exc … is
  empty at h = 10⁻⁶ ([[thm:t49-point]])."). Item 31's old text must be these 23 lines. Part C already contains the
  sentence.
- *The other 37 occur once,* at current lines:
  - 34: 76, 295, 443, 454, 498;
  - 35: 1423, 1435, 1493, 1636;
  - 36: 1138, 1154, 1162, 1359, 1423;
  - 41: 124, 1204; 42: 559;
  - 46: 89, 1706, 1713, 1745, 1751, 1767, 1774, 1780, 1825, 1834;
  - 71: 26, 1555, 1716, 1736, 1778, 1796;
  - 70: 1695; 00: 35; 01: 154; 03: 361; 90: 79.
- *m4.* The four P-K lines are now 03:316, 63:71, 71:4926 and 71:5227. Each still occurs once.
- *m5.* The P-T49 interaction texts are now placements on chapter 33. rem:t49-sets (d) is at 33:3582; its old line
  still matches P-ADM line 960. rem:t49-scope is at 33:3866–3875, in the revised wording quoted in m5. The replacement
  of m5 applies there, from line 3866 through "… meets no exclusion in z." (line 3872).
- *m7.* The three sentences of chapter 33 are now at 33:126, 33:3130 and 33:3532. Each occurs once.

---

## The open question on lem:iii-i11-2-1 (task item 2)

P-ADM's argument does not depend on that lemma's root list:
- Part (g), the definition, prop:vi-c-adm-exist and the site list of thm:vi-c-adm-holds never use it.
- The lead names the lemma only among places that allow multiplicity: its E′ carries log orders up to l_*, and l_*
  bounds the multiplicities at real part ≤ 5 by prop:iii-f1-2-3 (b).
- Side finding 4 (lines 1038–1046) reports the same gap. The list omits the roots ι^C_(·,+) − 1 with real part in
  (1, 3); for example ι₂(h) − 1 ∈ (1, 1 + 40h/13) at scalar type 2 (lem:ec-lb-ind, for h ≤ 10⁻⁶).

There is one indirect link. thm:vi-c-adm-holds (1) states that every result of ch:s22, this lemma included, holds at
every admissible point "with its proof". So a repair of the lemma may use only what an admissible point gives: (C1),
(C4′), z ∈ (0, ½], s_C > 100, (P1), (P3), (P4). It must not bring back (C2), (C3) or z ∉ Z_exc, which the definition
drops. A repair that only adds these roots to E′ with log orders up to l_* needs none of them.

## Every use of h ≤ 10⁻⁶ (for the revision that removes the cap)

### (a) In P-ADM.md

*The cap stated:*
- line 24, (P0);
- line 49, "uses h ≤ 10⁻⁶ only through s_C > 100 and (C1)";
- lines 73–74, row a1;
- line 476, item 18: "h ≤ 10⁻⁶, so that s_C … > 100".

*s_C > 100 derived from the cap (γ_C ≥ 10⁶).* These sites need only s_C > 100, which also gives (C5):
- line 40;
- lines 85–86, step (2);
- lines 123–125, (f);
- line 351, item 7;
- lines 436 and 459, items 15 and 17, which cite sec:iii-f-1 for s_C > 100.

*(C1) derived from the cap through lem:iv4-1-3 (a):*
- line 41;
- lines 43–44, prop:iii-f1-3-3 needs (C1);
- line 48 and line 218, "where (P0) gives it" / "beyond what (P0) gives", that is part (g), which needs (C1);
- line 86;
- lines 110–112, (b);
- line 119;
- lines 134–135, (j);
- line 340, item 6;
- line 719, item 35;
- line 734, item 36.

*Other uses:*
- Line 128: "The bound h ≤ 10⁻⁶ enters through s_C > 100 and (C1)."
- Line 59, the proof of prop:vi-c-adm-exist: "h ∈ 𝖧 gives h < 10⁻⁶". Under the minimal form it must give s_C > 100
  (γ_C > 10⁶) and (C1) (lem:iv4-1-3 (a)) instead.
- Lines 202–203, Part C: "it satisfies (P0), as h = 10⁻⁶ …". This stays true in the minimal form: s_C = 499995.1…
  and (C1) by lem:iv4-1-3 (a) at h = 10⁻⁶.

*Texts that need h ≤ 10⁻⁶ itself, because thm:ec-lb-proved uses lem:ec-lb-ind and 6Θ_η < 2·10⁻⁵:*
- lines 226–228, Part C, last sentence;
- lines 680–683, item 32;
- lines 703–706, item 34, the theorem restated at every admissible point;
- lines 717–720, item 35;
- lines 733–737, item 36;
- lines 750–755, item 37: "So the bound holds on the proved set …";
- lines 777–779, item 38: d_NM > 1.4032·10²⁰ at an admissible (h, γ_(Υ,H), 1/100, 1/100).
- n8's replacement (prop:np-10-52 (iii) is defined only for h ≤ 10⁻⁶).

*Notes:*
- lines 912–921, the rationale for keeping the cap;
- lines 1020–1025, side finding 1: (C1) gives only s_C > 49.49, so s_C > 100 must be stated separately;
- line 1042, side finding 4: the location of ι₂(h) − 1.

The P-T49 texts (lines 955, 971–975) and the chapter 33 texts (lines 1010–1013) mention 10⁻⁶ only as facts about
𝖹, 𝖹₂ and h_*. They are unaffected.

### (b) Chapter sites the file relies on

*(C1) for h ≤ 10⁻⁶.* lem:iv4-1-3 (a) (33:1122), resting on prop:np-10-54 and sec:s14-every-h. No result gives (C1)
for h > 10⁻⁶. In the minimal form (C1) must therefore be a clause of the definition. s_C > 100 does not imply it, and
it does not imply s_C > 100.

*(H1)–(H4) and ½ + ϑ_ℋ < −C_0 for h ≤ 10⁻⁶.* lem:iv4-1-5 and lem:iv4-1-6 (33:1188, 33:1202). These are inside (P1);
only Part C uses the lemmas, at h = 10⁻⁶.

*ε_ind(h) on (0, 10⁻⁶].* prop:np-10-52 (ii)–(iii) (33:3031), used in Part C and in 71:153.

*The lower bound, which needs h ≤ 10⁻⁶ itself.* lem:ec-lb-ind and the step 6Θ_η < 2·10⁻⁵ in the proof of
thm:ec-lb-proved. With them:
- thm:ec-lb-proved, cor:ec-lb-delta, rem:ec-lb-conditions (71:1773, "each of which holds at every point of the proved
  set", and the bullet 71:1776) and rem:ec-lb-unbounded;
- every sentence that states the lower bound at every point of the proved set: 71:17–19, 71:73–75, 71:1555,
  71:5291, 00:33–34, 01:152–153, 03:314–315, 03:359–361 and 90:66–67.

In the minimal form each needs "with h ≤ 10⁻⁶", unless lem:ec-lb-ind and 6Θ_η < 2·10⁻⁵ are proved on a larger range.

*Sites that need only s_C > 100,* that is h < (1 − e_C)/200 ≈ 4.99995·10⁻³:
- 34:76 (sec:iii-f-1);
- 38:53 and 38:1200–1202 (eq:iii-i1-1-1);
- 45:53 (sec:iii-c1-0) and 45:802 (eq:iv2-0-1);
- 46:89–93 (sec:iii-k-0, item 18) and 46:1852 (sec:s27-class);
- row d2;
- 41:124 and 42:559 (items 15 and 17);
- 35:1435 (item 7).

Findings m1–m7 and n1–n12 do not depend on the cap, except that n8's replacement needs the qualifier.

---

## What I checked and found correct

**Part (g) (Blocks B2–B3), for every z ∈ (0, ½].**
- *Roots from □^C.* By (d), the entries before the semicolons that come from □^C have real part < −101. The v1 entry
  −2 − 2γ_Cv_C carries no superscript C, but it equals ι^C_(v1,≪) − 1. By lem:iii-f1-2-2 the v1 roots of □^C are 3
  and −1 − 2γ_Cv_C, and (C1) puts the second below −C_0, since it is not ≥ 2.
- *Entries after the semicolons* have real part > 1 by (b).
- *The remaining entries,* checked type by type against the list:
  - s0: 2 − ι^Υ_(s0,2) and 0;
  - s1: 2 − ι^Υ_(s1,3), 2 − ι^Υ_(s1,2) and −1;
  - sl: −l, 2 − ι^Υ_(sl,l+2), 2 − ι^Υ_(sl,l+1) and 2 − l;
  - v1: −1; vl: −l and 1 − l; tl: −l.
  They are real by lem:iii-d-4-1.
- *Distinctness.* They are pairwise distinct by eq:iii-d-4-2. Its bounds are strict for z > 0, including the upper
  bound at z = ½, where z(1 + z/8)/3 = 0.177 < ¼. The chains at s1 and sl are exactly the intervals
  (2 − l − j − ¼, 2 − l − j).
- *Multiplicity.* The list gives the zeros of det N_L with multiplicity. The cancellation of D in the first paragraph of
  the proof uses only (C1) (ι = 2 is a simple root at s0 and s1) and lem:iii-d-4-1, not (C2), (C3) or Z_exc. So each
  such root is a simple zero of det N_L at each type and degree, which is the meaning of "simple" in lem:iii-d-4-1 and
  at every site that uses it.

**(C4′) and part (f).**
- Block B1: (C1) and (C4) imply (C4′). |Re ι − 1| ≤ 50 forces Re ι ≥ 2 by (C1), and Re ι = 2 only at the real root 2.
- Block B3: (f) under (C4′) is correct. A non-integer root ι = ι^C_(·,+) − 1 with |ι| ≤ 50 and integer real part
  gives a non-real □^C root ι + 1 with |ι + 1 − 1| ≤ 50 and integer real part.
- (C4) is used nowhere else in the chapters: only in (f) and in rem:ec-lb-conditions, which item 36 re-keys. So (C4′)
  suffices wherever (C4) was used.

**The lead.** I searched chapters 32–48 and 60–71 for:
- "simple", "simplicity", "multiplicit", "one-dimensional", "adj", "Π_μ", "simple pole" and "order of the pole";
- every citation of prop:iii-f1-2-3, lem:iii-g4-1-1, prop:iii-d1-4-1, lem:iii-d1-5-1, lem:iii-d-7-1 and
  thm:iii-e-1-1;
- (C2), (C3), (C4), Z_exc and 𝖹_exc in all chapters.

Every use of simplicity concerns roots with real part in (−3, 0], at the sites the file names:
- 34:532 and 35:1103 (root 0, through (c));
- 34:1811 (−2 at s2, v2, t2);
- 35:1422–1426 and 35:1493;
- 35:1636 (α ∈ (−1, 0) in thm:iii-g2-3-1, so −3 < Re μ ≤ 0 by (a));
- 36:1138, 36:1154–1166, 36:1360 and 36:1375 (−1 < b < b̃ ≤ w₀ < ℓ_K^max ≤ 3);
- 36:1423 and 36:1698 (𝒲(w₀), 𝒲(w));
- 41:1204–1206 (a > −3).

The places that meet roots outside the window allow multiplicity: ℰ_K, l_* and the index sets of lem:iii-a-1-4. The
(C1)–(C3) of def:iii-h1-1-1 and def:ii-c-2-4 in chapters 37, 38 and 65 are different clauses. Items 6 and 8–16 cite
(g) correctly in context; each bound they state checks.

**prop:vi-c-adm-exist.**
- (P0) holds because 𝖧 ⊂ (0, h_*), h_* ≤ 10⁻⁶.
- (P1), (P2) and the second half of (P4) hold by thm:iv4-2-1 and thm:iv6-4-1 at h ∈ 𝖧.
- (P3) is the conclusion of prop:iii-d1-4-1, exactly: the σ ≠ 0 and σ = 0 spaces and weights match.
- Λ_tf ≤ 41/64 for e_Υ ≤ ½, γ_Υ ≤ ¼. I recomputed this: (9/8)(4/9 + 1/8) = 41/64.
- Existence holds, and so does the exclusion of a countable set from an open interval.
- With the rows as P-T78 left them, the old set equals the proposition's set intersected with {z ∉ Z_exc}, so the new
  set contains the old one. (This is because ½s_C > 50 makes the caps ⅜ and ½s_C of row u4 inactive.)

**thm:vi-c-adm-holds, site by site.**
- thm:iii-e-1-1 (1)–(2): at 34:1079, 34:1431, 34:1868 and lem:iii-e-2-1 (33:2678), hence prop:iii-e-3-1 and
  prop:iii-e1-3-1.
- thm:iii-e-1-1 (4): only at 34:663, Step 4 of prop:iii-f1-3-3, at β_C = 1 + 2β ∈ (1, 2).
- (C1) sites; s_C > 100 and (C5) (complete up to n6); 𝖧, h_0, h_tf and 𝖹 enter only through thm:iii-e-1-1 and
  prop:np-10-52.
- Mode stability of □^Υ: at 32:1139, 32:1166–1172, 34:1069, 34:1086, 34:1127, 34:1232, 34:1453 and row b2.
  lem:iii-d1-5-1 (1) is (P3) at σ = 0.
- prop:iii-d-6-3 is used only in the proof of prop:iii-d1-4-1 and in step (2).
- lem:iii-d-7-1 (b) is used only inside prop:iii-d1-4-1 (32:827, 32:1064). Its other uses are at γ_Υ = 0
  (65:448, 66:911).
- prop:iii-f1-3-3 as merged has hypotheses (C1), 0 < e_Υ < 1, γ_Υ > 0, z ≤ ½ and Λ_tf < 1. Its proof uses
  thm:iii-e-1-1 (4) only in Step 4, and prop:tf-gauge-explicit (a) under the same hypotheses in Step 5.
- The continuity results apply on the compact set {𝗉}.
- Chapter 33's sections from sec:iii-e-2 to sec:iii-e1-3 use thm:iii-e-1-1 (2) and the first sentence of (3) only.
- Chapter 60 uses only steps (0)–(6), whose numbering is kept. Chapters 61–66 use the parameters only through explicit
  inequalities or at γ_Υ = 0.
- No result needs uniformity in the gauge parameters: the only homotopies in γ_Υ are of transition-face models
  (34:561, 34:642).

**(P0)–(P4) as properties of the point.**
- Each is a property of the point alone. The admissible set is the product of an h-set and a gauge set:
  - the h-set is cut out by h ≤ 10⁻⁶, (P1), (P2) and the second half of (P4);
  - the gauge set by e_Υ < 1, γ_Υ < ¼, (P3) and Λ_tf < 1. Here (P3) does not involve h, since □^Υ has no damping.
- No condition refers to a later choice.
- thm:vi-c-adm-holds (1) does not use thm:vi-c-2-1. Step (1) cites (1), and (2) applies thm:vi-c-2-1's proof, so
  nothing is circular.

**Part C at the computational point.**
- s_C = 500000·102399/102400 = 499995.1171875.
- (H1)–(H4) and ½ + ϑ_ℋ < −C_0 hold for every h ≤ 10⁻⁶.
- (P2) follows from prop:s14-damping-distance, which covers the non-integer roots of P_l, P_0 and p_(v) with
  |ι − 1| ≤ 50.
- Λ_tf < 1.0111·10⁻⁴.
- The three open items are stated correctly.
- The reduction of (P3) to b = b₀ is sound. It is the argument of Step 2 of prop:iii-d1-4-1 based at
  (b₀, 1/100, 1/100, γ_(Υ,H)): low energies by thm:i-c-7-1 and thm:i-c-6-4 with (TF) from lem:iii-d-7-1 (a) for
  every b; high energies by prop:iii-d-6-1; the compact middle by openness.
- thm:t49-point (revised P-T49) states exactly what Part C cites.

**Old and new texts.**
- All 44 old texts occur exactly once at 155f39c6 and after the P-K merge. 38 occur once at c1021295; m3 lists the
  six that do not.
- I read every new text in its chapter context, with the lines before and after. Each joins correctly, except items 13
  and 19.
- The combined texts (items 21, 27, 31, 32, 44) contain P-T78's results: Λ_tf < 1.0111·10⁻⁴, lem:iii-d-7-1 (a), and
  the parentheses of P-T78 items 10 and 11. They also contain P-T49's sentence (h = 10⁻⁶ ∉ 𝖹, Z_exc = ∅). They are
  consistent with both files.

**Typography.**
- Every line of the file is at most 121 characters.
- With labels resolved conservatively (sections as "Section 49.99.9", results as "Proposition 49.999"), no line of
  chapter text exceeds 121. Only the notes lines 12 and 1005 and the old text at line 653 do.
- The only wrapped lines that start with "- " are the list items of rem:ec-lb-conditions (item 36), as in the
  chapter.
- All labels are lowercase. Every label cited is defined in the chapters at c1021295, in P-T49 or in P-ADM.
- The edition's lint, run over Parts A–C and every new text, flags only the crosswalk rows inside item 13 (m1).

**Side findings.**
- 1 is true: (C1) gives γ_Cv_C > 49.5, so s_C > 49.4995 at v_C = ½.
- 2, 3 and 5 are true. For 5, z ≤ 4ϵ_1³ is needed.
- 4 is the open question above.
