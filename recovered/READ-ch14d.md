# READ-ch14d.md — chat 92 — main L5874–L5936, the close of Chapter 21

**Range** main L5874–L5936, 63 lines, three headings: §21.6 *E = 0 is relative to coordinates, and
the coordinates must be given* (L5874), §21.6.1 *The letter that defines rather than constrains*
(L5905), §21.6.2 *Two of the companion's five, read from three numbers each* (L5924). Every boundary
MEASURED by exact-token heading scan before a line was read; §22.1.2 at L6006 measured in the same
scan and recorded for the next range. PART V opens L5937, Chapter 22 at L5939.

**Instruments** `r2-ch14d.py` (computable, golden `r2-ch14d.out` 5,583 B · md5 5b139676 · 82 lines)
and `r2-ch14e.py` (prose, golden `r2-ch14e.out` 8,144 B · md5 1ee1da14 · 119 lines). Both
deterministic, both banked.

**Standing check run first.** The Register was grepped for a later entry naming §21.6 before any
figure was recorded as unreproducible (chat 91's method note). There is none: the only Register line
matching `21.6` is reg L5093, entry 1355, on an unrelated fit. The late corrective band 1780–1792
does not touch this section.

---

## A. Deviations of the volume

**14d-01 · Three of the six section pointers are the companion's, printed in the main volume's own
bare form, and all three numbers exist as main-volume sections with unrelated content.**
MEASURED, r2-ch14e [E1], [E2].

| site | prints | resolves in this volume to | the companion's section is about |
|---|---|---|---|
| L5928 | §10.4 | L2060 *10.4 The count, with no sieve* | THETA = 0 at 16, STAT = 0 at 8 |
| L5932 | §8.1 | L1813 *8.1 Distributive* | the charger relation, five chargers |
| L5933 | §10.1 | L2026 *10.1 What the void is made of* | the charger index, counted at six |

Tested case-exact and word-bounded: `\bTHETA\b` and `\bSTAT\b` are absent from main §10.4, and
`\bcharger` is absent from both main §8.1 and main §10.1. The other three pointers in the same
sixty-three lines — §21.1 at L5896, §12.11.8 at L5901, §21.5.5 at L5922 — all resolve to their
*claims*, so the failure is not a citation-hygiene problem in general but exactly the companion set.

The book already has a marked form for this and uses it elsewhere: `T §` occurs 2× in the main
volume, 8× in the Register and 3× in the Mathematical Compendium. The Mathematical Compendium entry
carrying **this same claim** prints it correctly at mc L2498: *Computed — T §10.1 (App. G), §10.4;
Coxeter 1948.* R3 has a target form to copy; this is not a pointer needing a section identified.

**14d-02 · L5917 states without scope what Register 547 states with it.** MEASURED, r2-ch14e [E4].
The volume: *And only that index carries one.* The entry: *Only that index **of the companion's
four** carries one; V6, V3 and the null surface use every letter in their boxes.* The volume's
sentence carries no qualifier — tested for `companion's (four|five)` at L5917, absent — while its own
next heading (L5924) names **five**. Three indices are actually compared at L5917–L5918 (V6, the null
surface, V3); the charger index that §21.6.2 goes on to treat is not among them. As printed the
sentence is a universal over five supported against three.

**14d-03 · L5911's five-part invariance is four-fifths true; the envelope-step count is not
invariant.** MEASURED, r2-ch14d [D6]. Λ₈'s 976 cells with a constant ninth coordinate appended:

| invariant | Λ₈ | Λ₈ + rung-1 letter | as printed |
|---|---|---|---|
| cells | 976 | 976 | same ✓ |
| box (realised grid) | 6,912 | 6,912 | same ✓ |
| E | 0 | 0 | same ✓ |
| seed | reduced model 27 elements, FULL equal, covers equal | identical | same ✓ |
| **envelope steps** | **77** (model 25 + 77 = **102**) | **93** (model 26 + 93 = 119) | **not same ✗** |

The book's own model rebuilds exactly: L3981 prints *87 of 102 elements*, and the instrument
recovers 102 as 25 value slots + 77 raising steps — an independent confirmation of that figure. The
sixteen added steps (eight as bound, eight as bounding coordinate) are **vacuous**: every cell
witnesses them, which is precisely why they vanish under reduction and leave the seed untouched.
seed(Λ₈) = 7 is chat 90's settled value and was not re-derived. R3's repair is to narrow the printed
list to the reduced model or to the seed, not to withdraw the sentence — four of its five terms hold.

**14d-04 · §21.6.1 uses a V-numbering the volume itself records as retired, with no pointer to that
record.** MEASURED, r2-ch14e [E5]. L5917–L5918 cite V6 and V3 by number. Main L4256–L4257 states
*V6 is not a vocabulary index; §10.1's table nonetheless reports V6 CLOSED at 14 cells in a box of
24, under the old V-numbering that §8.4 retired*, and Register 544 carries the same withdrawal.
Tested for any caveat inside L5874–L5936 (`retired`, `withdrawn`, `old V-numbering`, `§8.4`): none.
The arithmetic §21.6.1 draws from those numbers is sound (see B-3); it is the naming that is stale.

---

## B. Verified

1. **The theorem and every row of the L5880 table.** r2-ch14d [D2]. 9 × 10 = 90, 5 × 73 = 365,
   2 × 13 = 26, 5 × 5 = 25 — all four factorisations correct, and ℛ run on each full rectangle
   returns E = 0 in every case. [D2b]: over N ≤ 400 the existence of a factorisation with a, b > 1 is
   exactly compositeness, so the theorem's scope is stated exactly. 976 is composite, so it applies
   to Λ itself, which is what L5889 asserts.
2. **The operative E, established before any E arithmetic.** [D1]. The calendar was rebuilt cell by
   cell (12 months, February at 28): 365 cells, |ℛ| = 372, E = 7, and the seven absent cells are
   (2,29), (2,30), (2,31), (4,31), (6,31), (9,31), (11,31) — identical to the list printed at
   L1677. The book's definition at L1544 is E(X) = |ℛ(X)| − |X|.
3. **All three "uses every letter" claims are theorems of the printed pair, not observations.** [D5].
   With every rung ≥ 2 the multiset is forced and unique in each case: 24 over four letters is
   (2,2,2,3) only; 48 over five is (2,2,2,2,3) only; 64 over six is (2,2,2,2,2,2) only.
4. **The local null surface.** [D3]. Six letters in a box of 64 force every rung to 2 (unique
   multiset). 32 is exactly half. The face x₀ = 0 has 32 cells and E = 0; the even-parity class has
   32 cells and E = 32 — both printed values reproduced exactly, and both halves are 32 cells.
5. **The nesting.** [D3b]. Fixing two coordinates gives 16 cells, three gives 8, each E = 0;
   32 ⊃ 16 ⊃ 8, each half the last, as L5928–L5929 states.
6. **The ANEC-proofs deduction, as far as it goes.** [D4]. Four rungs each ≥ 2 need 2⁴ = 16 > 12, and
   no such assignment exists — so a rung-1 letter is forced. See C-1 for the strength of "one".
7. **The three main-volume pointers.** [E1]. §21.1's body does carry the two-naming table
   (`first naming` / `second naming` columns, eight rows). §12.11.8 does name the vacuous zero, in
   other words: *the image is the complete product — 2 × 4 here, full box for free … E = 0, and the
   zero is worth nothing.* §21.5.5 does carry a `role` axis.
8. **All three Register citations resolve and are on topic.** [E3]. 546 → reg L2043 (a·b, composite);
   547 → reg L2047 (rung-1, ANEC); 548 → reg L2051 (FACE, JUR). No lowercase `register NNN` in range.

---

## C. Incidental

1. **"One letter has rung 1" is asserted where the printed arithmetic gives "at least one".** [D4].
   All four rung multisets with product 12 contain a 1, but three of the four contain two or more;
   only (1,2,2,3) has exactly one. Exactness follows from L5919's *disagree by exactly one*, i.e.
   from 12 = 2·2·3 being the unique three-factor form — which the text asserts rather than derives.
   The two sentences are consistent when read together; the deduction at L5908 alone is weaker than
   its phrasing.
2. **"a random 26-cell set, E as given 38" has exactly one site in all six volumes.** [E7], [D8].
   E = 38 at 26 cells requires |ℛ| = 64, which is consistent, but the set is printed nowhere, so the
   38 is not verifiable from the record. The row's own claim (2 × 13 gives E = 0) is verified.
3. **"V3 geometry" has exactly two sites in all six volumes, both inside this section.** [E6]. It is
   the only row of the L5880 table with no second site anywhere — named, never defined. Its 25 cells
   against a box of 48 (L5918) is **not** a contradiction: under ℛ as defined, E is |ℛ(X)| − |X| and
   not |box| − |cells|, so a 25-cell ℛ-closed set inside a 48-grid is admissible.
4. **The periodic table carries two counts across sections.** [E8]. §21.6 L5881 and main L1613 give
   90 cells with E = 36; §21.1 L5604 names the same object *the 118 elements* with the same E = 36.
   7 × 18 = 126 and 126 − 90 = 36 holds; 126 − 118 = 8. E = 36 is consistent with the 90-cell reading
   only. §21.1 is chat 90's range and was not re-opened — carried to DEFERRED as a cross-chapter item.
5. **"one cell from where half-sided modular inclusion is proved"** (L5929–L5930) is a companion-side
   claim. The companion is not a member of either bundle, so it is recorded as unverified here rather
   than as a deviation.
6. **§21.6.2's title, "Two of the companion's five", and Register 547's "the companion's four"** are
   two different counts of the companion's indices. Both may be correct — 547's four are those with a
   printed (letters, box) pair — but no site enumerates the five. Related to 14d-02.
7. Three C9-OVERGENERALISATION-WORD census rows fall in range (1129, 1130, 1131) and are disposed in
   `CENSUS-CLOSURES-ch14d.tsv`.

---

## D. Instrument faults self-caught, all rewritten rather than trimmed

1. **The near-miss that the discipline exists to prevent.** V3's 25 cells against its box of 48 was
   about to be recorded as a hard contradiction. Reading ℛ's definition out of r2lib first — the
   realised-value grid cut by the monotone envelopes φ̂ᵢⱼ, not the bounding box — showed E is not
   |box| − |cells| in general, and the row is consistent. The same reading clears V6's 14 cells in a
   box of 24. Two false findings avoided by measuring the operator before the arithmetic.
2. **`cover_model` returns a 4-tuple, not a matrix** — the first draft called `.shape` on a list.
3. **The envelope-step count was measured on the wrong model twice**: first on the raw pairwise
   family (200 elements), then against 102 as if 102 were the *reduced* model (it is 27). The book's
   102 is value slots + raising steps, recovered exactly as 25 + 77. The discrepancy at 14d-03
   survived all three measurements and was never tuned away.
4. **Three keyword-design faults in the prose batch**, each of which would have produced a false
   entry in A: `two` tested against §21.1's *body* while the word is in its heading; `vacuous` tested
   against §12.11.8, which states the claim in other words; and bare `STAT` matching *state* in main
   §10.4. All three replaced with case-exact, word-bounded claim tokens. Uncorrected, these would
   have recorded two resolving pointers as failures — the exact error chat 91 recorded.
5. **`'four' in L5917` matched *uses all four letters*** and inverted 14d-02's verdict to its
   opposite on the first draft. Replaced with a test for the qualifier phrase itself. The instrument
   prints the trap it fell into so the golden carries it.
6. An off-by-one on the Register entry body (the line after `### NNN` is blank) printed an empty
   quotation; corrected to the body line.
