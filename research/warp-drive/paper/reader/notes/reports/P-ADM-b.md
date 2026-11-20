# P-ADM, revision b: the cap h ≤ 10⁻⁶ removed (author's decision)

File: research/warp-drive/paper/reader/proofs/P-ADM.md, 1299 lines, longest line 121.
md5 before 0fac203dc2b9b29c96012e7d2d0d1e4a (the version under review), after **06a69312c5d9336af7af86c5a3b336f9**.
Nothing committed and no chapter edited.

## 1. The definition (Block A1)

- (P0) is now: s_C > 100, e_Υ < 1, γ_Υ < ¼, and (C1) for the indicial roots of □^C_b, b near b₀. No cap on h.
- (P1)–(P4) are unchanged.
- A new paragraph says where each condition is used, by the items of the proof of thm:vi-c-adm-holds:
  - s_C > 100 in (f);
  - (C1) in (b), and in (j) as a hypothesis of prop:iii-f1-3-3;
  - e_Υ < 1 and γ_Υ < ¼ in (l) and (j);
  - (P1) in (a), (P2) in (c), (P3) in (i), (P4) in (e) and (j).
- The definition also states that s_C > 100 and (C1) hold whenever h ≤ 10⁻⁶ (lem:iv4-1-3 (a)), and that thm:ec-lb-proved assumes h ≤ 10⁻⁶ on top of admissibility.
- (C5) is now stated correctly: γ_Cv_C > 100 gives (C5), which is γ_Cv_C ≥ ½.
- Row a1, step (2), the sec:iii-k-0 paragraph, items (b), (f) and (h) of the theorem, and the existence proof are adjusted to match.

## 2. Every site that used the cap was re-checked

None of them needs a new hypothesis.

| Site | Result |
|---|---|
| (b), (C1) | Now asked by (P0). prop:iii-f1-2-3 assumes only z ∈ (0,½] and (C1). |
| (g) of prop:iii-f1-2-3 | Uses (b), (d), lem:iii-f1-2-2 and eq:iii-d-4-2. No h. |
| (P2)/(C4′) | Follows from (C1) and (C4) by an argument on the roots alone. (f) under (C4′) uses lem:iii-f1-2-4 on a compact parameter set. No h. |
| (P4), prop:iii-f1-3-3 as merged (P-T78) | Hypotheses are (C1), e < 1, γ > 0, z ≤ ½ and Λ_tf < 1. Step 4 uses thm:iii-e-1-1 (4) only at β_C = 1 + 2β ∈ (1,2). sec:tf-explicit and lem:tf-lin-reduction contain no bound on h or γ_C. |
| (f) | s_C > 100 is part of (P0); (C5) follows from it. |
| (g) of the theorem | lem:iii-f2-1-1 holds for every γ_C. |
| lem:iii-e-2-1 (2) | Uses thm:iii-e-1-1 (3) only through (C1). |
| Search of ch 34–48 | For 10⁻⁶, 10⁶, h_*, lem:iv4-1-3 and γ_C bounds: hits only rows c2–c4 and the two sentences that items 8 and 19 replace. |
| Computational-point remark | (P0) holds there: s_C = 499995.1171875, and (C1) holds by lem:iv4-1-3 (a), which is closed at 10⁻⁶. |
| prop:vi-c-adm-exist | h ∈ 𝖧 ⊂ (0,10⁻⁶) gives (P0). |

Consequence: the admissible set may now include points with 10⁻⁶ < h < (1−e_C)/200. No result of the paper certifies any of them.

## 3. Placement: 53 items, re-based on HEAD 7854b15c (P-LB, explicit K and P-T78 merged)

### Qualifier added where the cap kept a statement true

Items 31, 34–41, 43, 44, 47–51. The wording is "h ≤ 10⁻⁶" in ch 71 and "γ_C ≥ 10⁶" in ch 00, 01, 03 and 90; Part C also carries it.

- **ch 71:**
  - the opening;
  - the paragraph after thm:loss-d;
  - prop:ec-delta-cap;
  - the opening of sec:ec-lb-proved;
  - thm:ec-lb-proved: new title, and hypothesis "admissible, h ≤ 10⁻⁶";
  - its proof;
  - rem:ec-lb-conditions: h ≤ 10⁻⁶ is named as the one condition that an admissible point need not satisfy;
  - rem:ec-lb-unbounded;
  - rem:uc-data-order-limits;
  - rem:ec-not-evaluated.
- **ch 00:** the abstract.
- **ch 01:** sec:introduction-scope.
- **ch 03:** sec:settling-statement (K text) and sec:further-results.
- **ch 90:** the lower-bound sentence of sec:scope-constants.

### Texts left unchanged, and why

- lem:ec-lb-ind: it already assumes h ≤ 10⁻⁶.
- cor:ec-lb-delta: it is stated in the setting of the theorem.
- Statements at the computational point.
- ch 33.

### Explicit-K texts as direct old/new items

These replace the earlier phrase substitutions and the text-8 note:

- items 42 and 43 (ch 71);
- item 46 (ch 63);
- item 49 (ch 03);
- item 52 (ch 90).

### Former combined items

Items 22, 28, 33, 44 and 53 are now plain old/new texts against P-T78's merged texts. Only item 33 (rem:ec-point-outside) still contains P-T49's text 7.

### New item

Item 6 (ch 35:53–54, P-T78's merged sentence): (C1) "which thm:iii-e-1-1 (3) provides for h ∈ 𝖧 and (P0) at every admissible point".

## 4. Interactions

- **P-T49:** no change from the cap. thm:t49-uniform (h ≤ 10⁻⁶) is not used by the definition. Merge order: P-T49 before this file.
  - After P-T49 merges, item 33's old text is the remark as it then stands; its new text, Part C, is unchanged.
  - Checked against the in-progress P-T49 merge in the working tree: every other old text of this file still occurs once, and line numbers shift by at most 2.
  - The suggested replacements for rem:t49-sets (d) and rem:t49-scope are updated to the fix-round text.
- **P-T78 (merged):** no change from the cap, since none of its results bounds h or γ_C. Its labels are cited directly.
- **P-TR:** its mathematics does not change, because it works at h < 10⁻⁶.
  - Its hypothesis should read "(h, γ_(Υ,H), 1/100, 1/100) admissible".
  - Suggested wording is given for rem:tr-scope.
  - Its texts 2–6 overlap items 32, 33, 41, 50 and 52. The file gives P-TR's texts 2–6 rewritten against this file's new texts.
- **Explicit K (merged):** nothing else in its section uses the cap. Its ch 46 and ch 63/90 data-order texts stay.
- **P-F123:** its item 15 (abstract, lines 37–38) is avoided; item 47 stops at line 36.

## 5. Checks

- **Scratch merge:** chapters at 7854b15c, then P-T49 items 1–2, then all 53 items.
  - `lint.py --chapters`: 0 hits.
  - `assemble.py --check`: 4652 labels, 0 problems.
  - Every line ≤ 121 characters, raw and with labels resolved.
  - No bad line starts (the only flags are the bullet lines of item 39) and no backslashes.
- **P-ADM.md:** same width, start and label checks pass. Lint hits are of the same kinds as in the previous version: crosswalk rows, "lint.py" named in the notes, and verbatim old texts.
- **The wrapper:** it now keeps formulas, products and "label (a)" pairs on one line.

## 6. Open

When P-T49's merge is committed, I can re-base the line numbers and item 33's old text on it if you want.
