# READ-ch13f.md — Phase R2, chat 80, segment 2: main §13.1–§13.4 (L3626–3676)

Range: `### 13.1 Why that ordering and not the other` (L3626) to L3676, the line before `# PART III — THE LAW` (L3677) — the whole of §13.1, §13.2, §13.3 and §13.4, closing Chapter 13. Instrument: `r2-ch13f.py` (banked, r2-ch13f.out 2,700 B · md5 2dc8c9d8… · ≈ 3 s). Clerical: `r2-tools.py lines|pointers|figures|census|layout 3626 3676` — census rows in range: 1 (row 1076); manual grep for lowercase `register NNN` and `A.N`: none. Five pointers resolved to heading **and** claim; no Register entry is cited anywhere in these fifty-one lines. `sections(X, w)` written here as the width-general fibre split (r2-ch13b's, owed to r2lib). Findings are recorded, never repaired (chat 67 hold).

## A — deviations

**13f-01 · L3662 (with L2472) — "the most active constraint" is refuted on the book's own measure, and the printed binding rates do not reproduce.** PRINTED L3662: `g ≤ q is the most active constraint   it is the coupling itself`; L2472: `**The most active constraint is the coupling; the least is the Pauli bound** … Two independent measures, one answer`; the table at L2467–2470 prints `g≤q 35.6 %`, `q≤k 33.0 %`, `g ≤ 4f+2 4.9 %`. MEASURED (r2-ch13f §3) on §12.9's own Box test — `y_i ≤ φ(x_j)` for every constraint — over every comparable pair of Λ₈. The population reproduces the record exactly, which is the control: **115,162** comparable pairs (recorded interval census 115,162) of which **31,604 = 27.4 %** are boxes (recorded 31,604 = 27.4 %). On that population the seven rates are

| constraint | binds | rate | printed |
|---|---|---|---|
| q ≤ k | 39,296 | **34.1 %** | 33.0 % |
| g ≤ q | 37,516 | **32.6 %** | 35.6 % |
| k ≤ 4ℓ+2 | 35,200 | 30.6 % | — |
| 2S ≤ k | 28,688 | 24.9 % | — |
| n ≥ ℓ+1 | 19,904 | 17.3 % | — |
| e ≥ f+1 | 17,324 | 15.0 % | — |
| g ≤ 4f+2 | 4,350 | **3.8 %** | 4.9 % |

so **q ≤ k is the most active constraint, not g ≤ q**, and the three printed rates are each off by 1–3 points. The 24.9 % for 2S ≤ k reproduces 12c-04's recorded figure exactly, so the measure is the one used in chat 74. The second measure named at L2472 does not separate them either: by tightness over the 976 cells, q ≤ k and g ≤ q are **tied at 461 cells (47.2 %)** each. Two further sites inherit: "the least is the Pauli bound" is true of `g ≤ 4f+2` (3.8 %) but §7.1 gives the Pauli origin to **two** constraints, and the other, `k ≤ 4ℓ+2`, binds in 30.6 % — third of seven; and L3662's `it is the coupling itself` is 12c-04's naming, under which §7.1 L1760 gives "vector coupling" to 2S ≤ k and "counting" to g ≤ q. **Closes 12c-04's L3662 site** and enlarges it: in Chapter 13 the gloss is not a passing one but a claim in a findings table. For R3: the ranking sentence at L2472, the three rates at L2467–2470 and L3662's row all rest on one measurement, and the measurement inverts the claim.

**13f-02 · L3627–3629 — the Kreuzer–Skarke frontier is listed among the indexes that close, and the book measures E(X) = 540 there.** PRINTED: `Λ closes, and so does the nucleon index, and the string partition function, and the Kreuzer–Skarke frontier, and Appendix D's index of this book's own mathematics.` SOURCE: §31.3.4 L8728–8736 — `E(X) on a specifiable slice, and 540 predictions … E(X) = 540. 498 join failures and 498 meet failures of 21,528 pairs`; §12.11.7 L3492 — `The 540 of the Kreuzer–Skarke slice are proposals of the same kind, and are stated as such`; §32 L8885 — `**7. The 540 remain unverified.**` The KS slice is the book's flagship *non*-closure, and E(X) = 540 is the whole point of §31.3.4. The nucleon index does close (L8653, `the shell model is closed under join and meet with E(X) = 0`) and Appendix D does (L10322, `elements, twenty-four fibres, E = 0`); for `the string partition function` no closure figure was found — the nearest site, L8686, reports `Λ closes at every dimension 2–8 with E = 0`, which is Λ's closure at various dimensions, not the partition function's. For R3: two of the four listed companions carry a measured E = 0, one carries E = 540, and one carries no figure.

**13f-03 · L3647 — "Chapter 7 … never says the pair is the object" is contradicted by Chapter 7's second sentence.** PRINTED: `**Chapter 7 introduces both ends and never says the pair is the object.**` SOURCE L1725–1726: `Λ is a set of eight-tuples. Each is a transition cell: a source configuration, a target configuration, and the electron count moved between them.` That is the pair with its transfer, named as what a cell *is*, in Chapter 7's opening lines; §7.1's coordinate table then labels the coordinates `source shell / source subshell / source occupancy / electrons removed / target shell / target subshell / target occupancy`. The rest of L3647 stands and is measured (below). Census row 1076 is closed **as a defect** on this line. For R3: the negative claim, not the positive one.

**13f-04 · L3657–3660 — a table row of §13.3 is corrupted and unreadable as printed.** PRINTED, in the `finding / where it comes from` table:

```
  \                                     A_q\                                 falls as   B   ris   the transfer is conserved between
                                                                             \          _   es    them
                                                                                        q
                                                                                        \
```

Four lines of interleaved fragments where the other three rows are single lines. The intended content is recoverable — *A_q falls as q rises, B_q rises; the transfer is conserved between them* — and MEASURED (r2-ch13f §2) on Λ₈: |A_q| = **33, 33, 23, 8** and |B_q| = **5, 10, 15, 17** for q = 0, 1, 2, 3. So B rises strictly, and A **does not fall strictly** — it is flat from q = 0 to q = 1 and falls thereafter. For R3: the row needs setting again, and the claim about A needs "does not rise" rather than "falls" (or a note of the tie), which cannot be judged from the corrupted text as it stands.

**13f-05 · L3672–3673 — "Chapter 17's measured levels" points at the wrong chapter.** PRINTED: `Structure does not choose; energy does, and energy enters only through Chapter 17's measured levels.` SOURCE: Chapter 17 is `Extension — cells, axes, constraints` (L4789; §17.1 E1, §17.2 E2, §17.3 E3, §17.4 a worked extension, §17.5 E is derived) and contains no measured levels. The book's measured levels are **Chapter 24's 1,442** — L564, `the regress terminates outside … at Chapter 24's 1,442 measured levels`, and L6799. For R3: the pointer is Chapter 24 (and §24.11 for the decline modes at L6809).

## B — verified

- **L3632–3634 the four self-applications.** Chapter 32 → L8790 `The law applied to this book`; §28.8 → L7721 `A dependent choice is indexable`; Part I indexes the rules; Appendix D → L10320 `The mathematics, indexed`, which closes at E = 0 (L10322, `elements, twenty-four fibres, E = 0`). Four, as `four times over` states.
- **L3641–3645 the fibration and the two ends.** Λ is fibred over q, and the ends as printed — a parent (n, ℓ, k) with 2S, a target (e, f) with g — are exactly the tower's two sides: A at indices 0, 1, 2, 7 (and 10, 11, 12 above Λ₁₀) and B at 4, 5, 6 (and 8, 9), meeting at the base q at index 3.
- **L3647 the product identity.** |Λ| = Σ_q |A_q|·|B_q| measured with defect **0 at all six stages** — Λ₈ 976, Λ₉ 1,654, Λ₁₀ 2,535, Λ₁₁ 13,585, Λ₁₂ 70,905, Λ₁₃ 199,130 — reproducing chat 79's measurement (READ-ch13b B) from the width-general fibre split. `there is no factorisation that does not pass through the transfer` is the same statement as the bridge census of READ-ch13b (no edge crosses the two sides).
- **L3655 the fibres are two-body products**, and §12.8.5's local form holds on them: E(A_q) = E(B_q) = 0 at every q on both sides of Λ₈, no join or meet failure anywhere.
- **L3664 rank is modular.** r(x∨y) + r(x∧y) = r(x) + r(y) with both x∨y and x∧y in Λ₈, over all **475,800** unordered pairs, 0 failures. The identity is automatic for a coordinate-sum rank (max + min = a + b); what is not automatic, and is what the row is really reporting, is that the join and the meet stay inside Λ₈ — E(Λ₈) = 0.
- **L3671 the maximal chains.** Recounted by rank-graded path counting on the cover graph: ranks 3 … 20, so 17 steps and 18 cells on a maximal chain, unique 0̂ = (1,0,1,0,1,0,0,0) and 1̂ = (3,1,3,3,3,1,3,3), and **1,113,045,672** maximal chains — the figure printed at L2478 and at L3671, reproduced exactly. §12.9's identification (a distributive lattice's maximal chains are the linear extensions of its poset of join-irreducibles) is what makes L2478's `e(P)` and L3671's `maximal chains` the same object.
- **L3668–3669 kinematics without dynamics** is a restatement, not a new claim; §12.9 (L2460) resolves and prints the chain count the sentence uses.
- **L3650–3651** `This one fibres over a difference` is the q of L3641, and every row of the table below it that is legible resolves to a measured result above.

## C — incidental

- L3637–3638, L3644–3645, L3658–3660, L3665 and L3671–3673 are four-space-indented paragraphs that render as code blocks; L3657 is a column dump. Same production class as earlier segments; noted, not a concern (M's priorities) — except L3657–3660, which is 13f-04 because the text itself is destroyed, not merely mis-set.
- §13.3's table has a header row (`finding / where it comes from`) and four content rows, one of which is the corrupted one; the other three are one line each.
- L3628's `Appendix D's index of this book's own mathematics` and L3633's `Appendix D indexes the mathematics and closes it at E = 0` are the same claim twice in seven lines; wording only.
- No Register entry is cited in §13.1–§13.4. Every figure in the segment has its home elsewhere (§12.9, §12.8.5, Chapter 7), so nothing here is unsourced, but the chapter that names the book's title carries no register pointer of its own.
