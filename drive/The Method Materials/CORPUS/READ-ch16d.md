# READ-ch16d — chat 117 — main L8451–L8574 (§30.3.3 – §30.3.9), 124 lines

**§30.3 IS CLOSED IN FULL.** Cut chosen over HANDOFF-69's two shorter offers because it closes a
movement rather than stopping mid-section. Extents re-measured by heading scan; every heading
resolved to its body occurrence. Instruments `r2-ch16b` (computable, md5 81670a57, 173 lines) and
`r2-ch16c` (prose, md5 25e135d6, 248 lines). Census rows in range: **2** (1180 at L8553, 1181 at
L8569), witnessed against 1178/1179 below and 1182/1183 above, ids contiguous 1178–1183.

---

## A. Deviations

**16d-01 — Rival's bound printed in the vacuous orientation, at two sites.** L8497 (caption) and
L8500 (body) both print `|K| ≤ (3/2)|L|` *for a maximal sublattice*. With K a sublattice of L,
|K| ≤ |L| ≤ (3/2)|L| holds always: the inequality bounds nothing. Rival's 1973 theorem is
|L| ≤ (3/2)|K|, i.e. |K| ≥ (2/3)|L|. The adjacent claim *the Boolean case is tighter* has content
only under the standard orientation — MEASURED 2/3 = 0.67 < 3/4 = 0.75 (Decimal, HALF_UP, 2 dp);
under the printed orientation 3/4 ≤ 3/2 is true and says nothing. The letters are never bound to
lattice and sublattice anywhere in the unit. R3 reverses the inequality or binds the letters.
Docket 12, 34.

**16d-02 — a total reachable only by rounding up (L8530).** *Three complete boxes, 267,000 subsets.*
MEASURED from the table's own rows: 2⁸ + 2¹² + 2¹⁸ = 256 + 4,096 + 262,144 = **266,496**. Nearest
thousand **266,000**; three significant figures **266,000**; ceiling to the thousand **267,000**.
The printed figure exceeds the measured total by 504 and is reachable only by rounding up. The
three row figures are each exact. R3 prints 266,496 or names the convention. Docket 34.

**16d-03 — Dilworth cited for a decomposition Dilworth does not produce (L8517–L8518).** *width 7 ≤ 8,
and by Dilworth and Larson the chain decomposition of J(Λ) IS the axis system.* MEASURED on the
rebuilt lattice: |J(Λ)| = **17**, width of J(Λ) = **7** (Dilworth, n − max matching), axes = **8**.
*width 7 ≤ 8* is exact. But Dilworth's theorem yields a MINIMUM chain decomposition, hence 7 chains,
not 8; an 8-chain decomposition exists and is not Dilworth's. The definite article is the defect.
R3 softens to *a chain decomposition* or names the merge that takes 8 to 7. Docket 19.

**16d-04 — a count word right about its rows and wrong about the class its own labels name
(L8559–L8560).** *Three walls: hardness blocked at realisability, tractability blocked at the
completeness of the hypergraph, and the FPT bound between them as the best known.* Items listed
**3**; items naming a wall **2**. The third is named as what lies BETWEEN the walls. Identical in
shape to chat 115's *five unlocated results* whose fourth marked itself LOCATED. R3 prints *two
walls and the bound between them*. Docket 21.

**16d-05 — a splice inside a sentence, and it is ORIGINAL.** L8563 ends *Every sublattice and*;
L8566 begins *interval of Λ has E = 0*; the two join cleanly. Between them L8564 and L8565 insert
two complete prior-art sentences (Anstee & Farber, Hoffman/Kolen/Sakarovitch; Lubiw and the Γ-free
literature). MEASURED against Prints & Proofs P8481–P8485: **the five-line block is byte-identical**
— authoring, not production. The clearest member of the class yet found; chat 116's L8401 inserted
one sentence, this inserts two into a shorter sentence. Docket 26.

**16d-06 — an unbibliographed attribution (L8510).** *NextClosure enumerates the sublattices with
polynomial delay.* MEASURED: `NextClosure` has **one site in six volumes**, is absent from
`## References` at its BODY occurrence L11503, and absent from R.7 L11806. `Ganter`, to whom the
algorithm belongs, has **zero sites in six volumes**. Every other attribution in the unit is
bibliographed. Docket 36.

**16d-07 — three count words standing on bodies that do not enumerate them.** L8510 *converging in
nine rounds* (no rounds printed); L8552 *Three reduction attempts* (the sentence states the shared
direction of all three and enumerates none); L8563 *Its nine recovered extra edges* (MEASURED: the
tree has 7 edges on 8 vertices, C(8,2) − 7 = 21 non-edges; 9 is not derivable from the tree, and
`nine recovered` / `extra edge` have **one site each in six volumes**, L8563 itself). Docket 10, 17.

**16d-08 — a figure whose inputs are printed nowhere (L8531).** *After the duality merge the 19
canonical forms reduce to 12 with no loss.* The table above prints 30, 210 and 4,168 classes; 19
appears once in the unit and only in this sentence. Docket 10.

**16d-09 — a unit left unstated on a two-figure comparison (L8509).** *in 47.8 s against 86.* The
47.8 carries `s`; the 86 carries nothing on the line. Docket 10 (15f-02's sub-class).

---

## B. Verified findings — MEASURED exact, R3 must not re-derive

1. **The fourth lemma reproduces in full, and so does the trap beside it.** Interval sets of two to
   four intervals on ground sets of two to five points: population MEASURED **2,354** (4 + 50 + 375
   + 1,925), matching the printed figure exactly. The nesting characterisation holds with **zero
   counterexamples** over all 2,354. Reading *strictly* as ordinary containment refutes the lemma on
   exactly **1,098** of them, as printed — 46.64 % of the population. Three printed figures, three
   exact, and *Strictly* is load-bearing exactly as the text says.
2. **Λ's arithmetic, all exact.** 976 cells, d = 8, axis alphabets [3,2,3,4,3,2,4,4]; ∏|A_i|! =
   **11,943,936** exact. |J(Λ)| = **17** = height **17**. Width of J(Λ) = **7**. And 17 = Σ(|A_i|−1)
   — this is where the figure comes from, recorded so R3 need not hunt it.
3. **The constraint graph is a tree, measured off the generator.** Edges n–ℓ, ℓ–k, k–q, e–f, f–g,
   q–g, k–S2: 8 vertices, 7 edges, `is_tree` **True**.
4. **The step law and the three-quarters subset.** Row labels sum 8 + 3 + 1 = **12**, matching
   *twelve boxes*; steps 1, 2, 4 match 2^(d−2) at d = 2, 3, 4, and the caption's 8 matches at d = 5.
   3·2^(d−2) over 2^d = **0.75 at every dimension**; the caption's 3, 6, 12, 24 are exact; the
   removed cells number 2^(d−2), a subcube, at all four.
5. **Three method classes over three classes.** §30.3.7's body carries one colon-terminated lead-in
   and **three** class paragraphs. The count word holds. (A lead-in is not a class — the instrument
   said otherwise until repaired.)
6. **Three preserving rules over three arrows.** *box → interval → sublattice → product* — four
   objects, three arrows. Exact.
7. **The hypergraph bound.** A complete hypergraph on d vertices has exactly 2^d − 1 non-empty
   hyperedges. Exact.
8. **E = 0 on the intervals.** 115,162 ordered strict comparable pairs (convention: ORDERED,
   strict); on a systematic 1-in-28 sample, **4,112 intervals tested, zero join or meet leaks**.
   Every interval of a lattice is join/meet-closed by construction, so the claim is structural.
9. **Register 247 is exact and on point.** L8471's *Register 247* resolves to an exact Register
   heading whose headline reads *§30.3.3's FOURTH LEMMA, LEFT ON A CITATION AND NOW PROVED IN FULL* —
   docket 9(b)'s cleanest counter-case in the run.
10. **Three of four pointers hold, and the fourth holds too.** §18.4 carries the projection claim
    under both resolvers (which DIFFER: (4980,4999) vs (4980,5294)); §E.5 carries Rival, sublattice,
    Chen and precedence; §E.6 carries Ryter, Schmid, Adams, Dwinger and complexity; **§2.15.2 holds**
    — its body at (680,716), COINCIDENT resolvers, is titled *Worked, on §30.3* and derives the exact
    ℛ-closed characterisation. The probe scored it zero only because the instrument tested the
    transliteration *Gamma* where the section prints the raw **Γ**.
11. **Nineteen of twenty-one attributions bibliographed.** Booth, Lueker, Rival, Chen, Koh, Tan,
    Dilworth, Larson, Tucker, Anstee, Farber, Hoffman, Kolen, Sakarovitch, Lubiw, Ryter, Schmid,
    Adams, Dwinger all in `## References` L11503. Only NextClosure and Ganter fail (16d-06).
12. **Zero Ruling 46 sites**; **zero duplicated-section recurrences over 65 long lines** — the
    eleventh consecutive clean unit.

---

## C. Incidentals

1. **Docket 23's executed case, second consecutive unit.** PP P8413 prints *Figure 23.2*; the volume
   prints **Figure 30.2** at L8495 and additionally carries the image reference
   `![Figure 30.2](figures/figure-30.2.png)` at L8493, which PP lacks. Chat 116 found the same at
   Figure 23.1 → 30.1. Stronger here: **Figure 23.2 is LIVE elsewhere in the volume at L6328 and
   L6330**, so the production renumbering resolved a real collision. Record the executed cases.
2. **The step-law table prints its header twice** — L8480 and L8483, identical, splitting three rows
   into 1 + 2. MEASURED in PP at P8400 and P8403: **authoring, not production**. Docket 28
   (15j-12's shape).
3. **Two first-person sites, and neither is prose.** L8516 and L8523 match the token `I` only inside
   the mathematical symbols on those lines. Chats 113–117 carry no first-person pronoun in prose.
4. **Ruling 45 candidates, four in 124 lines** — a much thinner cluster than chat 116's six in 104.
   L8459–L8460 *stood on Booth and Lueker's construction and on nothing of this book's own. It is now
   discharged*; L8470–L8471 *That reading was tried first here and was wrong, which is the whole
   reason the qualifier is in the statement*; L8545 *which is what reopened the question*. All are
   drafting history, none the plain self-reference kind. Docket 5.
5. **Census rows 1180 and 1181 are both C9-OVERGENERALISATION-WORD on `never`.** L8553 *never the
   reverse* is a statement about three reductions the body does not enumerate — it rides on 16d-07
   rather than standing alone. L8569 *This book never has one* is a universal over the book's own
   constructions; recorded **UNMEASURABLE** rather than refuted, since no printed inventory of
   constructions exists to sweep. Docket 19's discipline.
6. **§18.4's resolvers DIFFER** (body (4980,4999), span (4980,5294)) and the claim holds under both.
   Recorded because coincidence is not a reason to skip the second resolver and difference is not a
   reason to distrust the first.
7. **Chapter 7's span (1724,1796) is thin against L8516's *its structure is constructed in Chapter
   7*** — `structur` 1, `construct` 1, `axis` 0, `embedd` 0, `tight` 0. Not recorded as a defect: the
   sentence's later clauses (*embedding is tight*) are not pointed at Chapter 7. Flagged for R3's
   pointer sweep to read Chapter 7 in full before deciding.
8. **Figure references remain a production layer.** 33 inline `![Figure …]` references in the volume,
   **0** in PP, no `.png` member. Not a text defect; not recorded as one.

---

## D. Instrument faults, self-caught and rewritten in place — eight, none trimmed

1. **The digit boundary rejected a LIST comma as well as a thousands separator.** Chat 116 corrected
   the trailing-period half; this is the trailing-comma half. `(?![\d,])` scored **2,047** and **86**
   at zero sites in L8455 and L8510, the very lines that print them. Corrected form, owed to r2lib:
   **`(?<![\d.,])N(?!\d)(?!,\d)(?!\.\d)`** — only a comma FOLLOWED BY A DIGIT is a separator.
2. **A colon-terminated lead-in counted as a method class**, refuting a true count word (3 read as 4).
3. **A per-axis attribution of join-irreducibles silently dropped 10 of 17** and then reported a
   chain count from the remainder. Replaced with what is measurable: |J|, width, axes, and Σ(|A_i|−1).
4. **`Gamma` tested where the text prints `Γ`** — would have recorded the holding §2.15.2 pointer as
   a defect. A symbol is tested RAW. This is the fault the *a token probe is not a reading* rule
   exists to catch, and reading the target in full is what caught it.
5. **One global PP offset across a unit that inserts a line mid-way** — the offset shifts by one at
   L8493's image reference, so every witness after it was misaligned by one. Witnesses now anchor on
   their own text.
6. A `round()` self-check that matched its own source line and reported False on a clean instrument.
7. A rounding block that printed thousands-units as bare integers and computed one quantity under
   two labels.
8. Format arguments attached to the wrong `print`.

**The book was right and the instrument wrong four times** (faults 1, 2, 3, 4). Running count:
chat 110 five, 111 three, 112 zero, 113 one, 114 one, 115 two, 116 three, **117 four**.
