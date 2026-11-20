# F-P-ADM: fix round on R-P-ADM, combined with the rebase on fb87f2fc

File: research/warp-drive/paper/reader/proofs/P-ADM.md, 1335 lines, longest 121.
md5: 0fac203d (the version read) → 06a69312 (revision b) → **321077a8168dd1940db23a33397ee7fa**.
I edited no chapter and committed nothing.

## Base

Every old text was rebased on commit fb87f2fc, where P-LB, the explicit K, P-T78 and P-T49 are all merged. The current HEAD, 19ebe3ef, has the same chapters.

All 58 old texts occur exactly once. No two items overlap.

Item numbering:
- Items 1–53 keep revision b's numbers. This matters because P-TR takes items 32, 33, 41, 50 and 52 as its basis.
- Items 54–58 are new, all in chapter 33.
- "Unchanged" is now item 59.

## Findings

**m1, fixed.** In revision b the crosswalk rows still landed inside an item, and the placeholder stayed. The cause was a bug in the generator: it computed the insertion index in the wrong list. The rows now sit only in the crosswalk section. Their sources are pinned as `paper/reader/proofs/P-ADM.md@PENDING:N`, with N = 20, 63 and 105.

**m2, fixed.** Item 20 now covers lines 1706–1711 and keeps blank line 1712. The definition starts after a blank line.

**m3, fixed.** Items 22, 28, 33, 40, 44 and 53 are plain old/new pairs against the merged texts; none is a combination any more.
- Item 33 (rem:ec-point-outside) takes the whole 23-line remark at 71:55–77, including P-T49's sentence.
- The P-T78 paragraph is now the reader's sentence, plus a remark that the cap changes nothing for P-T78.

**m4, already resolved in revision b.** It is carried by items 42, 43, 46 and 49 (71:4925, 71:5225–5227, 63:70–71, 03:314–316).
- Items 43 and 49 also carry the h ≤ 10⁻⁶ (or γ_C ≥ 10⁶) qualifier.
- Item 49 covers 03:314–316; the reader proposed 03:316–318. My range also contains the "bounded below" clause that the cap qualifier needs, so it stays.

**m5, fixed.** Item 58 uses the reader's text against 33:3866–3872, ending "…so 𝖹 = 𝖹₁ ∪ 𝖹₃. The set 𝖹 meets I". This drops the empty clause about prop:vi-c-adm-exist.

**m6, fixed.** The definition's clauses are now (AP0)–(AP4) throughout the file, which has no (P0)–(P4) left. Paragraphs that overflowed after the rename were rewrapped.

**m7, fixed.** The three chapter 33 sentences are now items 54–56.
- Item 54 uses the reader's grammar fix.
- Item 55 is as suggested.
- Item 56 does not use the suggested "used in the proof of no theorem", because that is false. cor:s14-eps-ind-point and prop:s14-damping-distance are used in chapter 71: at 71:52, 1406, 3114–3116 and 3862. It reads instead "are used by no step of the proof of [[thm:settling]]". It also names [[prop:vi-c-adm-exist]] beside [[thm:iii-e-1-1]] as taking h ∈ 𝖧.

## Nits

| Nit | Status | Change |
|---|---|---|
| n1 | Applied | Block B2: "that the later chapters use". |
| n2 | Resolved in revision b | Already "(AP0)–(AP4)". |
| n3 | Resolved in revision b | Step (2) already says "by (AP0) and (AP4)". |
| n4 | Applied | ϵ_0, ϵ_1 in item 19; "≤ ϵ_1 … Z_exc" in item 40. |
| n5 | Applied | The statement intersects ℬ(γ_(Υ,H)) with ℬ_VI; the proof says (Dyn) holds on that intersection. |
| n6 | Applied | The reader's closing sentence for item (l). |
| n7 | Resolved in revision b | No lone "A" line. |
| n8 | Applied | The reader's text in Part C, with "and h ≤ 10⁻⁶" because the cap is gone. 71:153 and 71:1413 left as they are. |
| n9 | Applied | Item 45 extended to line 1697; it now names the open (AP3) at (1/100, 1/100) and keeps the threshold clause as a reason. |
| n10 | Applied | The lead adds 36:1375. cor:iii-g2-3-2 is moved out of the list of places that use no simplicity: it uses simplicity, and (g) covers it. |
| n11 | Resolved in revision b | The P-LB paragraph's item list is computed, and the crosswalk notes cover the abstract and the K items. |
| n12 | Applied | "(depending on 𝗉)" added in (AP3). |

## Cap coverage

Every sentence the reader lists now carries the h ≤ 10⁻⁶ or γ_C ≥ 10⁶ qualifier:

| Chapter sites | Item |
|---|---|
| 71:17–19 | 31 |
| 71:73–75 | Part C, item 33 |
| 71:1555 | 36 |
| 71:5291 | 44 |
| 71:1773 | 39 |
| 00:33 | 47 |
| 01:152 | 48 |
| 03:314 | 49 |
| 03:359–361 | 50 |
| 90:66 | 51 |

Items 34, 35, 37, 38, 40, 41 and 43 also carry it.

(C1) is stated explicitly in (AP0).

## Checks

The scratch merge was run on the chapters at fb87f2fc with all 58 items applied:
- `lint.py --chapters`: 0 hits.
- `assemble.py --check`: 4652 labels, 0 problems.
- Every new line is at most 121 characters, both raw and with labels resolved to "Proposition 49.999".
- The only wrapped "- " starts are the list items of item 39.
- No backslashes; all labels are lowercase.

In P-ADM.md itself, the remaining lint hits are only in the notes: the crosswalk rows, "lint.py" named once, and quoted old texts.
