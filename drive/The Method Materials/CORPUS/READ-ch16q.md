# READ-ch16q.md — main L9030–L9156 (§32.2, §32.3, §32.4, §32.4.1, §32.4.2)

Chat 122. Unit cut by own heading scan: **L9030–L9156, 127 lines**, §32.2 through §32.4.2 — the
movement-closing cut, ending where §32.5 opens at L9157. Instruments: `r2-ch16o` (computable,
146 lines, md5 146b46f2) and `r2-ch16p` (prose, 405 lines, md5 6944ac1f). Main volume read to
**L9156 of 11,855 = 77.2 %**.

Conventions fixed before any figure was scored: surplus = |J| − log₂(cells), derived from L2149's
*976 of the 131,072 available seventeen-bit words* and checked against §11.1.1's printed 7.07;
fill = cells / ambient box (∏|Aᵢ| over the eight coordinates); rank = coordinate sum, confirmed
against L2474's *eighteen antichains, the largest 122 at rank 11* before use; E(X) = |ℛ(X)| − |X|.

---

## A. Deviations

**16q-01 — two count words that neither the table nor the Register reaches, and the Register
repeats them.** L9135 prints *Nine of nine move.* over a table of **seven** rows (cells,
generators, fill, rank levels, widest level, surplus, reflection survivors — L9127–L9133). L9147
prints *Six of six identities hold; nine of nine values move.* over a table of **five** rows
(L9141–L9145). Register **394** (reg L1465) carries the same headline — *SIX OF SIX IDENTITIES
HOLD UNDER CAP VARIATION; NINE OF NINE VALUES MOVE* — and its own body enumerates *E(Λ) = 0,
|J(Λ)| = Σ(|Aᵢ| − 1), closure under join and meet, rank modularity and the cylinder's
factorisation* (**five**) against *cells, generators, fill, rank levels, the widest level, the bit
surplus and both reflection counts* (**eight**). MEASURED: six is reached only by reading *closed
under join and meet* as two identities; **nine is reached by no reading of either volume** — the
table gives seven, the Register's own enumeration eight. Cross-volume, main + Register.

**16q-02 — 1,635 attributed to Chapter 28 with the wrong referent, and Chapter 28 does not list
them.** L9055: *The book's physical claims are checked against measured levels from named
compilations, and Chapter 28 lists one thousand six hundred and thirty-five that failed.* MEASURED
at the target: Chapter 28's own head, L7367, reads *one thousand six hundred and thirty-five claims
made in the course of this work were wrong* — the figure counts **the book's own withdrawn claims**,
not measured levels that failed a check. L7372 states *The entries themselves are not printed
here*, and L7373–L7375 send them to the Register volume, so *lists* fails too. The word form has
**fifteen main-volume sites**; fourteen are the Register's size (entries, corrections, withdrawn
claims, failures the book caught in itself) and **L9055 alone makes it a count of external
measurements**. Docket 30 and docket 14.

**16q-03 — three unreachable documents attributed to the wrong chapter.** L9057: *Chapter 28 names
three documents and one section that could not be reached.* MEASURED: an eleven-token sweep
(*could not be, not obtained, unobtained, not reached, could not reach, inaccessible, unavailable,
not consulted, not seen, paywall, not read*) over Chapter 28's whole span L7364–L7856 returns
**zero** hits. The same sweep over Chapter 29 returns five, including the heading **§29.6 *The three
documents we could not reach*** at L8029. The claim is true of Chapter 29 and false of Chapter 28.
Docket 9(a).

**16q-04 — *the single open item* has no home.** L9057: *Chapter 29 names the single open item.*
MEASURED at the target: Chapter 29 names **six** items that remain open — L7911–L7914, *six of the
eleven items in Q had novelty as their only stake — B, C, F, G, K and N … They remain open* — and
L8105 adds one more (*grows by one item: whether anyone has lattice-ordered the seniority scheme*).
*single open* has **one site in the whole volume, L9057 itself**, the citing line. Same shape as
16m-05, 16j-02 and chat 121's 16o-06; docket 9(b).

**16q-05 — §18 cited for a triple whose home is §12.11.2.** L9116: *§18 already prices it: no
differences, no sums, no symmetric bounds.* MEASURED under both resolvers — §18 `section_span`
(4922, 5381), `body_range` (4922, 4931), DIFFER, swept over the span: *symmetric bounds* has
**zero** sites inside §18 and two in the volume, L3365 and the citing line. The triple's home is
**§12.11.2 L3364**: *Chapter 17 excluded two constraint forms — sums and differences. The tower
requires a third: SYMMETRIC BOUNDS.* §18 does carry sums and differences as the triangle's two
inequalities (L4926, L4971), so two of three prices are at the cited section and the third is not.
Mitigation recorded: the next clause cites §12.11, and §12.11.2 is inside that span. Docket 9(b).

**16q-06 — Knaster and Tarski invoked as authority, unbibliographed.** L9107–L9108: *A monotone
operator on a complete lattice has fixed points — Knaster and Tarski.* MEASURED against the
**body** occurrence of `## References` (L11503, the second of two; the contents hit is L173):
**Knaster 0, Tarski 0**. Gödel is bibliographed (1). Russell and Heaviside appear as eponymous
terms rather than citations and are recorded here without being scored as attributions. Register
279's headline also names Knaster, so the Register carries the attribution the volume does not
bibliograph. Docket 36.

**16q-07 — Ruling 46 site: `rclose.py` at L9107**, inside the corroboration clause of §32.4.1's
proof. Swept case-sensitively for `.py`, `BUILD<n>`, `MANIFEST`, `.tsv`, `.md` across the 127 lines:
**one site**. **Absent from Prints & Proofs** — the second Ruling 46 site added since chat 111, and
the second in a row that is not original (chat 120's `bookindex.py` at L8816 was also absent).

---

## B. Verified findings

1. **The cap-variation table is exact in all twenty-eight figures.** Rebuilt at four settings —
   (3,3,1,3,1), (4,4,1,6,1), (4,4,2,6,2), (5,5,2,6,2): **cells 976 / 8,853 / 19,109 / 35,789**;
   **generators 17 / 31 / 33 / 35**; **fill 14.12 % / 6.72 % / 6.45 % / 7.73 %** (Decimal.quantize,
   2 dp, HALF_UP); **rank levels 18 / 32 / 34 / 36**; **widest level 122 / 704 / 1,497 / 2,742**;
   **surplus 7.07 / 17.89 / 18.78 / 19.87**; **reflection survivors 8 / 16 / 17 / 68**. Every figure
   reproduces at the source's precision. Register 394's *fill alone … not even monotone* is exact.
2. **All five printed identities hold at all four settings.** E(Λ) = 0 everywhere; |J| = Σ(|Aᵢ| − 1)
   at 17, 31, 33, 35; join/meet closure with **zero leaks** — exhaustive over all 475,800 pairs at
   976 and by a stated **200,000-pair budget** (seed 122) at 8,853, 19,109 and 35,789; rank
   modularity zero failures; the cylinder factorises over the transfer, factor = 0 at every setting.
3. **The join-irreducible count is exact and independently derived**, not read off the identity it
   would otherwise assume: J(Λ) ⊆ {minimum of {y : yᵢ ≥ v}} by meet-closure, each candidate then
   tested against the join of everything strictly below it.
4. **χ is a product of seven Heaviside factors, exactly as L9093 states.** MEASURED from the
   construction: ℓ ≤ n−1, k ≤ 4ℓ+2, q ≤ k, f ≤ e−1, g ≤ 4f+2, g ≤ q, 2S ≤ k — **seven**, every one
   binding (relaxing them admits 308, 564, 575, 200, 24, 673 and 300 further cells), and the seven
   with the five caps cut the 6,912-cell ambient box to exactly **976**. Every factor is an upper
   bound of one coordinate by a monotone function of another: **no negation, no complement, no
   implication**. L9093–L9098 is exact.
5. **The recursion table's occupancy column is exact at all four levels** — 10/16 = 0.625,
   10/70 = 0.143, 10/100 = 0.100, 0.100.
6. **The closure-operator proof corroborates.** 3,000 random subsets of the (3,3,1,3,1) ambient box,
   seed 122: **extensive 0 failures, monotone 0, idempotent 0**. Meets of fixed points: **zero
   closure failures**, as printed.
7. **§32.2 carries nothing bibliographic — 16m-08 confirmed from the cited side.** Printed whole
   (eight lines, `section_span` = `body_range` = (9030, 9038), COINCIDE): S1 alphabet, S2 order, S3
   bounds. *unobtained* 0, *works* 0, *listing* 0, *cited* 0, *compilation* 0. L11555 (*not obtained;
   §32.2 lists them as open*) and L11799 (*was not read in this work (§32.2)*) both send the reader
   to a section with no list in it.
8. **Registers 279, 388, 391, 392 and 394 all exist and are on point.** 279's headline is literally
   §32.4.1's argument — *the language is negation-free, and ℛ is a closure operator*; 388, 391 and
   392 are the three findings L9150 cites them for.
9. **Every pointer in the unit resolves.** §32.4 span (9059, 9157) / body (9059, 9085) DIFFER;
   §32.1.4.1, §12.11.3.1, §32.4.1 and §32.4.2 **COINCIDE**; §D.5.2 resolves through
   `lettered_heading` to L10562. Nine of eleven pointers carry their claims; the two that do not
   are 16q-04 and 16q-05.
10. **Prints & Proofs anchors at a uniform −94** across every witness taken in this unit, re-anchored
    per witness on its own text. The unit is original throughout except `rclose.py`.
11. **Docket 27 clean for a sixteenth consecutive unit:** 45 long lines swept, **none** recur.
12. **Census: three rows in range**, ids 710–712, all `C7-WITHDRAWAL-LINE-NUMBER-SURVIVES` at L9150
    on registers 388, 391 and 392 — the flagged tokens are the section's own live citations.
    Regex artefacts, disposed *not a defect* (precedents 678, 680–687).

---

## C. Incidentals

1. **L9079 understates its own table.** *Closure, dimension and E are invariant from level 1* — the
   table shows closed = yes, E = 0 and dimension 2 at level **0** as well. What changes at level 1
   is occupancy and the alphabets, which the same paragraph correctly says stabilise by level 2.
2. **The fourth identity is entailed by the third.** Under the rank convention the book's own §11
   fixes (coordinate sum), componentwise max + min = a + b in every coordinate, so rank modularity
   cannot fail wherever join and meet stay inside the lattice. It is printed in the same voice and
   with the same *tested by pairs* qualifier as the independent tests.
3. **2,873 is single-witness and draw-dependent.** One site in six volumes (L9107). Reproduced in
   kind, not exactly: the same experiment at seed 122 gives **2,955 / 3,000 (98.5 %)** against the
   printed 2,873 (95.8 %), with zero closure failures either way. It is a population count that
   cannot be recomputed without the original sampler — docket 17's strict class.
4. **Ruling 45 grows by twelve candidate sites** — L9036, L9041, L9045, L9050, L9057, L9065, L9083,
   L9108, L9120, L9136, L9147, L9148 — **all present in PP at −94**. Chat 115's discriminator must
   be applied to the standing list before any of them is repaired. L9065 (*an earlier draft of this
   section got it wrong*) is also a docket 15 narrated-past-state member.
5. **Table formatting (docket 28).** The recursion table's level-3 row carries no label where levels
   0–2 are named; neither table in §32.4.2 carries a rule between header and body.
6. **19,109, 35,789 and 2,742 each have one site in six volumes**, but all three were recomputed
   exactly here, so under chat 115's refinement they are not single-witness.

---

## Instrument faults, self-caught and rewritten in place (three)

1. `r2lib.factor_q` is a **Λ≉** function — its `tgt()` reads tuple index 8, which an 8-tuple does not
   have. Rewritten for L8's halves (source 0,1,2,7; transfer 3; target 4,5,6) with provenance.
2. The first form of the seven-factors test counted **binding φ̂ pairs** (16) and scored the book's
   *seven factors* against them. Wrong measurement: φ̂ pairs belong to the reconstruction operator,
   not to χ. Rewritten to read the construction's own inter-coordinate bounds.
3. `numsites` matched only unseparated digits, so **8,853 / 19,109 / 35,789 scored zero sites
   including their own table line**. Every four- and five-digit figure the book prints was invisible
   to it. Rewritten to sweep the comma-grouped form as well.

The book was right and the instrument wrong in all three. A fourth near-fault was avoided by
reading §12.11.2 in full rather than accepting the token probe's verdict on §18.
