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

---

## Final (round 2): proofs/P-ADM.md at md5 321077a8168dd1940db23a33397ee7fa, 1,335 lines

This round read:
- the whole file;
- the writer's reports P-ADM-b.md (the cap removed) and F-P-ADM.md (the fix round);
- the chapters at HEAD 2768bfb8. They are identical to those at fb87f2fc, where P-LB, the explicit K, P-T78 and P-T49
  are merged, and to the working tree.

**Verdict: NOT CONFIRMED, 0 Major, 1 minor, 4 nits.**
- All of m1–m7 and n1–n12 are resolved.
- The cap removal is complete, and no proof step at an admissible point uses h ≤ 10⁻⁶ silently.
- All 58 old texts occur exactly once at HEAD, at the lines the item headers give, and no two items overlap.
- My own scratch merge is clean: lint 0 hits, assemble 4652 labels and 0 problems.

The one minor finding is in the notes: the P-TR paragraph no longer matches P-TR, which now carries its own texts
against this file. Once that paragraph is replaced (text below), I would confirm the file; the 4 nits do not block it.

### The round-1 findings

| finding | status | where |
|---|---|---|
| m1 | resolved | The crosswalk rows are only in the crosswalk section (lines 1106–1108). They are pinned `@PENDING:20/63/105`, which are the label lines 20, 63 and 105, in P-T49's convention. Item 14's new text is clean. |
| m2 | resolved | Item 20 is 46:1706–1711. In the merge the blank line 1712 stays, and the definition starts a new paragraph (checked in the merged chapter). |
| m3 | resolved | Items 22, 28, 33, 40, 44 and 53 are rebased on the merged texts. Item 33 is the 23-line remark with P-T49's sentence. |
| m4 | resolved | Items 42, 43, 46, 49 and 52. |
| m5 | resolved | Items 57 and 58. Item 58 is my text, against 33:3866–3872. |
| m6 | resolved | Renamed (AP0)–(AP4). "(P1)–(P5)" remains only in the note on line 11, where it names lem:iii-i15-1-1. |
| m7 | resolved | Items 54–56. |
| n1–n12 | resolved | n1 (line 189), n2 (59), n3 (97), n4 (lines 504–505 and 813), n5 (66, 75), n6 (154–156), n7 (item 48), n8 (Part C, 236–238, with "and h ≤ 10⁻⁶"), n9 (item 45), n10 (268, 286–287), n11 (crosswalk notes), n12 (line 36). |

Two decisions of the writer:
- *m4, item 49.* The writer chose 03:314–316 instead of my 316–318, so that the "bounded below" clause can carry the cap
  qualifier. That is right. The new fourth line "admissible choice of the" joins 03:317 correctly.
- *m7, item 56.* The writer is right and my wording was wrong. cor:s14-eps-ind-point and prop:s14-damping-distance are
  used in chapter 71, at 71:52, 1406, 3114–3116 and 3862, so "used in the proof of no theorem" is false. "Used by no
  step of the proof of [[thm:settling]]" is true, since no result of chapter 71 is used outside it.

### The cap removal, against my list

**(AP0) states both conditions explicitly** (lines 27–28): s_C > 100 and (C1), the latter for □^C_b, b near b₀. It also
keeps e_Υ < 1 and γ_Υ < ¼. The consequences are derived correctly:
- γ_C = 2s_C/(1 − e_C) > 200, so γ_Cv_C > 100, which gives (C5);
- z_Υ ∈ (0, ¼);
- γ_Υ < min(½s_C, ⅜);
- δ_♯ ∈ (0, ¼).

(C1) is now asked by the definition, not derived. This is needed: (C1) gives only s_C > 49.49 (side finding 1), and no
result proves (C1) for h > 10⁻⁶.

**Where the cap was derived before, it is now read from (AP0):**
- (b) (line 122);
- (f) (line 135);
- (h) (lines 139–140);
- (j) (line 147);
- step (2) (line 96);
- row a1;
- item 19 (sec:iii-k-0);
- item 38 ("(C1) holds by (AP0)");
- item 39 ("(C1), part of (AP0)");
- Part C at the point ((C1) at h = 10⁻⁶ by lem:iv4-1-3 (a), closed at 10⁻⁶).

The proof of prop:vi-c-adm-exist (line 70) now shows s_C > 100 and (C1) from h < 10⁻⁶. The new item 6 gives the opening
of ch:s16 the clause "(AP0) … at every admissible point".

**Every lower-bound sentence carries the qualifier.**
- In chapter 71:
  - 71:18–21 (item 31);
  - 71:73–77 (Part C);
  - 71:1484–1487 (item 34, which also covers the "([[thm:ec-lb-proved]])" at 1487);
  - 71:1535–1536 (item 35);
  - 71:1555–1562 (item 36);
  - thm:ec-lb-proved: title and hypothesis (item 37);
  - its proof (item 38);
  - rem:ec-lb-conditions (items 39–40; "each of which, except h ≤ 10⁻⁶, holds at every point of the proved set");
  - rem:ec-lb-unbounded (item 41);
  - rem:uc-data-order-limits (item 43);
  - rem:ec-not-evaluated (item 44).
- 00:33–36 (item 47), 01:152–156 (item 48), 03:314–316 (item 49), 03:359–365 (item 50) and 90:66–70 (item 51).
- cor:ec-lb-delta is stated "in the setting of [[thm:ec-lb-proved]]", so it inherits the hypothesis. lem:ec-lb-ind
  already assumes 0 < h ≤ 10⁻⁶.
- I grepped the chapters at HEAD for every citation of thm:ec-lb-proved, cor:ec-lb-delta, lem:ec-lb-ind and
  lem:ec-lb-rounds, and for the numbers 0.3168, 2.2456, 4.7158, 6.654 and 3.052. Every hit is inside one of these items
  or is a proof step under the theorem's own hypothesis.
- "d is unbounded on the proved set" and "no upper bound holds on all of it" stay true without the qualifier, because
  prop:vi-c-adm-exist gives admissible points with h arbitrarily small, at which the bound holds.

**No silent use of h ≤ 10⁻⁶ at an admissible point.** I grepped the results that thm:vi-c-adm-holds (1) covers
(chapter 32 from sec:iii-d2-1, chapter 33 from sec:iii-e-2 to sec:iii-e1-3, chapters 34–48 and 60) for 10⁻⁶, 10⁶, h_*,
γ_C bounds and every citation of the h-dependent results of chapter 33: lem:iv4-1-*, thm:iv*, prop:np-10-5*,
sec:s14-every-h, *s14-* labels. The hits are:
- *Sites that items 1, 8 and 19–28 rewrite.*
- *Explicit s_C > 100 sites,* which (AP0) covers: 34:76, 38:53, 38:1200–1202, 45:53, 45:802, 45:1632, 46:1852.
- *Remarks on the gauge point that no proof step uses:*
  - 34:35 and 34:452–453 (δ_50 and prop:np-10-52);
  - row w1's remark at 46:1769–1771;
  - 34:492 (P-T49's sentence in the proof of (e), unused).
  The bound ε_ind ≤ δ_50 at (1/100, 1/100) holds at every h anyway, the entry −49 − δ_50 being independent of h.
- *33:2958 (prop:iii-e1-3-1).* It cites "the proof of [[lem:iv4-1-6]], (H2)" for the principal symbol of ρ⁻²P^C_b,
  which does not depend on h, and (H2) is part of (AP1) in any case.

The step-4 use of thm:iii-e-1-1 (4) is in (AP4), and (H1)–(H4) with ½ + ϑ_ℋ < −C_0 are in (AP1). lem:iii-f2-1-1 and
cor:iii-f2-1-2 hold at every γ_C. The 1-form c_C of sec:iv4-0 does not depend on h.

### Old texts and the scratch merge

- I parsed all 58 items:
  - every old text occurs exactly once in the chapters at HEAD 2768bfb8;
  - every header's line range is exactly where the old text sits;
  - no two items overlap;
  - every "Old/New, the N lines" count is correct.
- I built an independent scratch merge, with my own script and not the writer's: the chapters at HEAD, then all 58
  items, with Blocks A1–A4, B1–B3 and Part C substituted as the headers say. In the merged chapter 46, the rows read c1,
  u1, a1, b1–b4, w1–w2, d1–d2, n1, and thm:vi-c-adm-holds follows the paragraph after the proof of thm:vi-c-2-1.
  - `lint.py --chapters`: 62 files, 4652 labels, **0 hits**.
  - `assemble.py --check`: **labels 4652, problems 0**.
- In the file itself:
  - every line is at most 121 characters;
  - with labels resolved conservatively, only the notes line 15 exceeds 121;
  - the only wrapped "- " starts are the bullets of item 39, as in the chapter;
  - all labels are lowercase;
  - every label cited is defined in the chapters at HEAD or in P-ADM, except thm:tr-transfer, rem:tr-scope and
    prop:tr-fail, which appear only in the P-TR notes.
- Other proof files:
  - P-F123 (ebfba4ae): its item 15 (front matter 37–38) and item 13 (ch01 157–159) are compatible with items 47 and 48
    in the merge.
  - P-TR (35df0aaf): every old text of its form B occurs once in the merged tree, at 71:29, 71:84, 71:1815, 03:364,
    90:81, 71:5236 and 71:5244. Its item 7 is at 33:3541, not at the "3537 in form B" it states; that is P-TR's line
    number, not this file's.

### New findings

#### F1. minor (notes; a merge hazard): the P-TR paragraph conflicts with P-TR's own form B (lines 1200–1288)

Current text (lines 1200–1201, and the texts that follow down to line 1288): "*P-TR (not merged).* Nothing in P-TR's
mathematics changes. [[thm:tr-transfer]] is stated at h ∈ 𝖧 ∩ [h₁, 10⁻⁶), within the cap, … Its texts 2–6 change the
places of items 32, 33, 41, 50 and 52 of this file. If P-TR merges after this file, its texts 2–6 read as follows, …"

What is wrong:
- *Two sets of texts for the same lines.* P-TR (md5 35df0aaf) now gives its own form B against this file's new texts:
  - item 1b;
  - items 2, 3, 5, 6 and 8, against the new texts of items 32, 33, 50, 52 and 43;
  - item 4, after item 41;
  - item 7, after item 56.

  This paragraph gives different new texts for the same lines, with different line ranges. For example, its text 2
  replaces three lines where P-TR's form B replaces one.
- *Wrong overlaps.* The paragraph names items 32, 33, 41, 50 and 52. P-TR's item 4 lies after item 41 without
  overlapping it; its item 8 overlaps item 43, which the paragraph does not name; and item 1b is not mentioned.
- *Out of date.* thm:tr-transfer is now stated for h_m ≤ h < 10⁻⁶, h ∉ 𝖩, with (h, 1/100, 1/100) admissible. It no
  longer takes h ∈ 𝖧, so "is stated at h ∈ 𝖧 ∩ [h₁, 10⁻⁶)" no longer describes P-TR.

Replacement: lines 1200–1288 (from "*P-TR (not merged).*" through "Its text 7 ([[rem:s14-eps-ind-scope]] in
[[ch:s14]]) does not overlap this file.") become:

    *P-TR (not merged).* P-TR gives its own texts against this file (its form B): its item 1b states its notion of an
    admissible parameter point (h, 1/100, 1/100) through [[def:vi-c-admissible]], and its items 2, 3, 5, 6 and 8 change lines
    of the new texts of items 32, 33 (Part C), 50, 52 and 43 of this file. Its item 4 changes the two lines after item 41,
    and its item 7 lines of [[rem:s14-eps-ind-scope]] after item 56; neither overlaps this file. Each old text of P-TR's
    form B occurs exactly once in the chapters after this file is applied. This file gives no text of P-TR; if its new texts
    of items 32, 33, 43, 50 or 52 change again, P-TR's form B is to be checked against them.

(Widths 113, 121, 118, 116, 120 and 88.)

#### N1. nit: the usage paragraph credits γ_Υ < ½s_C to item (f) (line 50)

Current: "Each condition is used, and the proof of [[thm:vi-c-adm-holds]] says where: s_C > 100 in its item (f), directly
and / through γ_Cv_C > 100 and γ_Υ < ½s_C; …"

γ_Υ < min(½s_C, ⅜) is listed in item (l), not in (f).

Replacement for line 50 (114 characters; line 51 unchanged):

    Each condition is used, and the proof of [[thm:vi-c-adm-holds]] says where: s_C > 100 in (f) and (l), directly and

#### N2. nit: (AP3) splits "Im σ" across a line break (lines 36–38)

Replacement for lines 36–38 (four lines, widths 116, 118, 101 and 20):

    (AP3) there is a neighbourhood ℬ(γ_(Υ,H)) of b₀ (depending on 𝗉) such that for every b ∈ ℬ(γ_(Υ,H)) and every σ with
    Im σ ≥ 0, (□^Υ_b)^(σ) is invertible, as a map 𝒳_σ → 𝒴_σ when σ ≠ 0, and as a map 𝒳_0 → 𝒴_0 for every s > 3/2 and every
    α with α + 2 ∈ (0, ι^Υ_(s1,2)) when σ = 0 (the spaces of [[sec:iii-d1-1]]); this is the conclusion of
    [[prop:iii-d1-4-1]];

#### N3. nit (optional): item 54's new text ends with a line that holds only "The" (line 1034)

Replacement for the new text (three lines, the last no longer a single word):

    Every result of this chapter that names (v_C, e_C, C_0, γ_C) uses these values, and so do all later chapters; the
    results that [[thm:vi-c-adm-holds]] (1) lists hold as well with γ_C = h⁻¹ at every admissible point
    ([[def:vi-c-admissible]]). The

#### N4. nit (optional): crosswalk row note (line 1107)

"new: replaces rows c2–u5" reads as if row u1 were replaced too. Replace by "new: with def:vi-c-admissible, replaces
rows c2–c4 and u2–u5".

### Checked again and found correct in this revision

- Parts A–C read line by line against the chapters.
- The definition's new paragraph on where each condition is used matches the items of the proof.
- prop:vi-c-adm-exist with ℬ(γ_(Υ,H)) ∩ ℬ_VI.
- thm:vi-c-adm-holds (b), (f), (h) and (j) with the explicit (AP0).
- Part (g) and Blocks B1–B3, unchanged.
- Part C, with (AP0) at the point, the three open conditions, and the qualifier in its last two sentences.
- Items 6, 31, 34–41, 43, 44 and 47–58 read in context. Each joins the line after it in the merged tree.
- The interactions on P-LB, the explicit K, P-T78 and P-T49 agree with the merged texts.
- Side findings 1–5 are unchanged and true. Side finding 1 now also explains why (AP0) asks s_C > 100 and (C1)
  separately.
