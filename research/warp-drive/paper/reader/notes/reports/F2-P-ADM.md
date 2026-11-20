# F2-P-ADM: round 2 of R-P-ADM applied

**File:** research/warp-drive/paper/reader/proofs/P-ADM.md, 1253 lines, longest line 121.

**md5:** 321077a8 → **bb8171d26e255d564043bda5ae5a75c5**.

No chapter was edited and nothing was committed.

## Findings

- **F1 (minor, notes only).** The P-TR paragraph has been replaced by the reader's six-line text, verbatim. The text defers to P-TR's form B. With it go this file's own versions of P-TR's texts 2–6 and the stale sentence on thm:tr-transfer at h ∈ 𝖧.
- **N1.** In the usage paragraph of def:vi-c-admissible, the reader's replacement line is applied: "s_C > 100 in (f) and (l), directly and …".
- **N2.** (AP3) now uses the reader's four lines, so "Im σ" is no longer split across a line.
- **N3.** Item 54's new text now uses the reader's three lines, so there is no line holding only "The".
- **N4.** The crosswalk row for prop:vi-c-adm-exist now carries the note "new: replaces rows c2–c4 and u2–u5". The reader's fuller note, "with def:vi-c-admissible, replaces rows c2–c4 and u2–u5", does not fit on the row: it would be 155 characters, against the limit of 121. So I dropped "with def:vi-c-admissible" and shortened the name field to "P-ADM, Proposition". The row is now 119 characters.

## Checks

- The chapters at HEAD (d65c494c) are identical to those at fb87f2fc, and the working tree has no chapter changes.
- All 58 old texts occur exactly once, and no two items overlap.
- Scratch merge of the chapters with all 58 items:
  - `lint.py --chapters`: 0 hits.
  - `assemble.py --check`: 4652 labels, 0 problems.
- Every line of the file is at most 121 characters, both raw and with labels resolved.
- No backslashes, and the only wrapped "- " lines are the bullets of item 39.
- The crosswalk pins are @PENDING:20, 64 and 106, the lines that carry the three labels.

## The repair of lem:iii-i11-2-1 in V-I11 (adding 1 + 𝒵 to the generators of Λ)

**The repair needs no parameter condition beyond (AP0)–(AP4).** Each property of 𝒵 it uses comes from a source already covered:

| Property of 𝒵 | Source | Condition needed |
|---|---|---|
| Its members (the list) | prop:iii-f1-2-3 | z ∈ (0, ½] and (C1); both are in (AP0) |
| Real parts in (1, 3) | (a)–(b) of prop:iii-f1-2-3 | same as above |
| Finite | lem:iii-f1-2-4, on the compact parameter set {𝗉} | none |
| Independent of b | (P2) of lem:iii-i15-1-1, through lem:iii-f-2-1 (3) | none; it is structural |
| Closed under conjugation | L̂_b(0) is real | none |
| Logarithmic orders | l_* | none; no simplicity, (C2), (C3) or Z_exc is needed |

**One place uses γ_C ≥ 10⁶ (h ≤ 10⁻⁶).** The proposed lem:s22-c-roots, together with the remark that cites it ("several of which lie in (1, 2) at every γ_C ≥ 10⁶"), says where the roots lie, and the repair does not need either. Both must keep their hypothesis γ_C ≥ 10⁶. V-I11's summary also says "at every admissible parameter point"; under the minimal definition that phrase should read "at every admissible point with h ≤ 10⁻⁶".
