# READ-ch16b.md — chat 116 — main L8347–L8450 (§30.2, §30.2.1, §30.2.2, §30.2.3, §30.3 head, §30.3.1, §30.3.2)

**Unit** 104 lines, cut by heading scan taken in this chat. §30.2 closed with all three subsections;
§30.3 entered at its own head with §30.3.1 and §30.3.2. Extent resolved under both resolvers:
**§30.2 (8347,8363) vs (8347,8399) DIFFER**; **§30.3 (8399,8405) vs (8399,8575) DIFFER**;
§30.2.1, §30.2.2, §30.2.3, §30.3.1, §30.3.2 **COINCIDE** under both.

**Instruments** `r2-ch15z` (computable), `r2-ch16a` (prose). **Five instrument faults self-caught and
rewritten in place, none trimmed** — see §D.

---

## A. Deviations

**16b-01 — a count word its own table refutes, and Prints & Proofs shows the rows never existed.**
L8367 introduces the re-run as *Re-run over 928 instances with **six invariants discovered since***.
The table it introduces (L8369–L8374) carries **four** data rows — overlap pairs, nesting pairs,
distinct row supports, log solution density — above a baseline row (*best of the original ten*) and a
header. Of the four, **three are structural invariants**; log solution density is the density itself,
not a structure. L8366–L8367 separately names **four** things discovered since (containment forest,
overlap components, C1P, interval structure). MEASURED against Prints & Proofs P8291–P8296: the same
four rows, no more. **Authoring gap, not production loss.** R3 prints four (or three structural), or
supplies the missing rows. Docket 21, 31.

**16b-02 — a second count word its own table refutes, same shape, same page.**
L8392 qualifies the fit as *on **five points***. The table at L8385–L8389 carries **four** rows,
d = 2, 3, 4, 5. PP P8307–P8311 prints the same four. Docket 21.

**16b-03 — a regression that cannot be reproduced from the table it is printed under.**
L8391–L8392: *the log–log slope is 2.29 … with R² between 0.37 and 0.42.* MEASURED on the four
printed points (ln mean steps against ln distinct rows, Decimal HALF_UP at 2 dp): **slope 2.33**,
**R² 1.00**. Neither figure reproduces, and an R² near 0.4 cannot belong to a four- or five-point fit
of these means at all — it belongs to a per-instance regression over the **1,480 instances** of
L8383, which are nowhere printed. Alternative fits measured for completeness: log max against log d
gives 1.95, log (max/d²) gives −0.05. **The regression's inputs are unstated.** Docket 10, 34.

**16b-04 — a pointer whose target carries none of the claim, under both resolvers.**
L8396: *§30.3.3 completes this reading*, where *this reading* is §30.2.3's landscape statement — E as
a potential on the space of orderings, adjacent transposition as a move, solution density as the size
of the basin. §30.3.3 was **read in full** (L8451–L8475), not token-probed: it is *What the interval
machinery was* — C1P, monotone endpoints, PQ-trees, the fourth lemma discharged, and a closing
blockquote that the apparatus is a representation of a 2-colouring. `body_range` and `section_span`
**COINCIDE** at (8451, 8476) and neither carries *landscape*, *basin*, *potential*, *descent* or
*stall* (0, 0, 0, 0, 0 against *interval* 9). **Where the claim does live**, measured across six
volumes: *basin* has two sites only, L8333 (§30.1) and L8396 itself; *landscape* main L693, L805,
L8394; *descent* main L686, L693, L8396, L8541; *stall* main L686, L8396; *transposition* main L693,
L3704, L8395. The completion the sentence promises is at **main L686–L693**, and *descent* recurs at
**L8541 (§30.3.7)**. R3 redirects the pointer or supplies the completion in §30.3.3. Docket 9(a).

**16b-05 — a caption denominator that matches no measurable population.**
L8446–L8447: *114 of 141 at arity 4*. At arity k the constraint is on k orientation variables and is
invariant under global complementation, so it is a relation on k−1 XOR-difference variables. MEASURED
at arity 4 (3 variables): **256** relations, **254** non-constant, **164** bijunctive (majority-closed),
**80** orbits under axis permutation. **141 is none of them**, and neither is 114. The arity-3 figure
by contrast is exact — see B. The population that *arises* is not printed in the unit. Docket 10.

**16b-06 — a sentence spliced into the middle of another sentence, and it is in Prints & Proofs too.**
L8400 ends *…given an index whose constraint graph has cycles, can*; L8402 begins *its coordinate
order be recovered?*. Between them L8401 prints a complete and unrelated sentence: ***Van Isacker**'s
survey gives the seniority reduction chains.* Joined, L8400 + L8402 read cleanly. MEASURED: the unit
is byte-identical to PP at offset −78 for L8347–L8443, so **the splice is original authoring**.
Docket 26.

**16b-07 — a paragraph broken by a blank line and mangled inter-word spacing, also original.**
L8419 ends *…every constraint is closed under reversing all of*; **L8420 is blank**; L8421 resumes
*its own orientations — 3,781 constraints checked, 100%.* and then runs a second sentence onto the
same line with **three runs of ≥3 consecutive spaces** (*A   function     invariant     under*),
continuing at L8422. Present in PP. Docket 28, and docket 26 one level down.

**16b-08 — six Ruling 45 process and past-state remarks in 104 lines, the densest cluster measured.**
L8363 *And that list was **enumerated once*** (heading), L8365 *An **earlier draft** concluded*,
L8366 *the list **predates** the containment forest*, L8379–L8380 *The **earlier reading** had the
second link and called it the whole chain*, L8411 *a **draft withdrew** them*, L8412 *The withdrawal
**is withdrawn***. All six are remarks about the book's own drafting history, not subject matter, so
chat 115's discriminator classes all six as sites. For scale: chat 115 found four in 109 lines and
nine plain self-references beside them; this unit has six in 104 and none of the plain kind.
L8365 is already one of docket 15's seven *an earlier draft* sites. Docket 5, 15.

---

## B. Verified — so R3 does not re-derive

1. **L8348's *Ten structural invariants* is exact.** The named list is dimension, alphabet size, cell
   count, occupancy, join-irreducibles, poset height, poset width, covers, antichain, rank range —
   **ten**.
2. **The density table (L8354–L8359) is internally sound and L8361 holds.** Backtrack-free rises
   24 → 47 → 82 → 100 % strictly; mean backtracks falls 2.9 → 1.0 → 0.2 → 0.0 strictly. The rarest
   solution bucket is the hardest and the always-solvable bucket is backtrack-free, so *the search is
   hard exactly when the solution is nearly unique* is carried by the table.
3. **Every cell of the max/d² column recomputes exactly**: 8/4 = 2.00, 10/9 = 1.11, 36/16 = 2.25,
   39/25 = 1.56 (Decimal, HALF_UP, 2 dp). **L8391's *the ratio does not climb* HOLDS** — the column is
   not monotone increasing.
4. **L8376's *by twofold* holds as a rounding.** Best structural correlation with steps is 0.606
   (distinct row supports); 0.606 / 0.31 = **1.95**, nearest integer **2**.
5. **L8376–L8377's two-link claim HOLDS.** The structural invariant predicts the density at |−0.883|
   and the density predicts the difficulty at |−0.628|; 0.883 > 0.628.
6. **475,800 is C(976, 2) under the UNORDERED convention** — named explicitly. Ordered would be
   952,576 (with the diagonal) or 951,600 (without). Over all 475,800 unordered pairs of Λ₈:
   **zero join leaks, zero meet leaks** — Λ₈ is a sublattice.
7. **L8406–L8408's identity holds on an independent population.** ℛ-closure (r2lib's `Rset`, the
   §6.1 L1540 definition) against closure under coordinatewise ∨ and ∧, swept exhaustively over
   every non-empty subset of 2×2, 3×2, 3×3 and 2×2×2 and sampled over 4×3 and 3×3×3:
   **2,128 instances, 0 disagreements.** The unit's own 1,487 instances are a different population;
   this corroborates rather than reproduces them.
8. **L8427's *all 14 constraints that arise are 2-SAT expressible* is EXACT.** At arity 3 the relation
   is on 2 XOR-difference variables: 16 relations, **14 non-constant, 14 bijunctive**. At arity 2:
   2 non-constant, 2 bijunctive. **L8433's *at arity ≤ 3 the language is entirely bijunctive* is
   therefore true and measured.**
9. **L8434's *contains 1-in-3-SAT and admits no Schaefer class* is EXACT.** Exactly-one-of-three fails
   all six tests: 0-valid, 1-valid, Horn (min-closed), dual-Horn (max-closed), affine (⊕-closed),
   bijunctive (majority-closed) — all False.
10. **Docket 36's second consecutive entirely clean unit.** All seven attributions — Van Isacker,
    Rival, Larson, Siggers, Stahl, Wille, Yannakakis — appear in `## References` resolved to its
    **BODY occurrence L11503** (the L173 hit is the contents entry), and **none** falls to R.7
    (L11806). Stahl & Wille at L11771 and Yannakakis at L11774 both name §30.3 in their own entries.
11. **Zero first-person pronouns**, four chats running. **Zero Ruling 46 sites** in the unit
    (BUILD, gate.py, close.py, r2lib, tower-2.py, MANIFEST, md5, commit, repo — all tested
    case-sensitively and word-bounded); chats 112–116 remain at zero.
12. **Zero register citations** in the unit, and **zero census rows in range**, witnessed against
    **1179 at L8303** and **1180 at L8553** — **contiguous ids either side, so none was missed.**
13. **Duplicated-section sweep 0 of 53 long lines** — the tenth consecutive clean unit.
14. **The unit is byte-identical to Prints & Proofs** for L8347–L8443 at offset −78. The only
    differences in the unit are at its tail, and they are a production **improvement**: the volume
    inserts `![Figure 30.1](figures/figure-30.1.png)` at L8444, which PP lacks, and **corrects the
    caption number from PP's *Figure 23.1* to *Figure 30.1***. Docket 23's executed case — record it,
    or the class looks worse than the book is.
15. **L8412's reversal is consistent across the volume.** No site anywhere in six volumes still
    asserts that reorderability is an interval problem (*interval problem* has exactly one site,
    L8412 itself), and L8096 in chapter 29 independently states the Stahl & Wille prior art. The
    withdrawal of the withdrawal leaves no stale sibling.

---

## C. Incidentals

1. **Two spellings of one correlation over two populations.** L8352 prints the density-in-log
   correlation as **−0.68** over the 211 instances; L8374 prints **−0.628** over the 928. Not a
   contradiction — different populations — but the two sit fourteen lines apart and a reader will
   read the second as a restatement of the first.
2. **Figure references are a production layer absent from PP.** The volume carries **33** inline
   `![Figure …]` references; **PP carries none**. No `.png` is a bundle member and no `members/figures`
   directory exists, so the unresolvable image path at L8444 is **not** a defect of the text.
3. **L8414's identification is single-witness.** *The recovered bound of Chapter 15 is Rival's closed
   family of irreducible intervals.* Chapter 15 spans L4270–L4332 and carries *recover\** 8 and
   *bound* 4, but **zero** *Rival*, *interval* or *irreducib\**. The identification is asserted here
   and nowhere else; it is an identification made at this site, not a claim about chapter 15's text.
4. **L8415's *Siggers' Lemma 3.5(ii) states φ_ij exactly*** is a lemma-number citation with a single
   site; unverifiable from the book alone and correctly attributed.
5. **Docket 17 additions, with chat 115's refinement applied.** Single-witness in six volumes:
   **3,781** (1 site), **0.883**, **0.628**, **1,487**, **928**, **211**, **1,480**, **396**.
   Of these the correlations and ratios were **recomputed or cross-checked** here; the five population
   counts are **not recomputable from the book** and are single-witness in the strict sense.
   **0.606 and 0.31 are corroborated** at main L7634–L7635, §30.4's own audit item.
6. **§30.4's magnet is visible from here.** PP P7556–P7564 and main L7634–L7635 print the *Five lists
   in one chapter* material that docket 21's 15h-12 tracks; it belongs to §30.4/§30.4.2 and is **not**
   in this unit. Chat 117 or 118 tests it.

---

## D. Instrument faults, self-caught and rewritten in place before banking

1. **`r2-ch15z` §5 counted *log solution density* as a structural invariant**, returning 0.628 as the
   best structural correlation and reporting *twofold* refuted. The density is not a structure; the
   correct figure is 0.606 and the claim holds. **The book was right and the instrument wrong.**
2. **`r2-ch15z` §7 anchored the Prints & Proofs context on the first hit**, which is §30.4's audit
   material at P7557, not §30.2's tables. Re-anchored on the table rows themselves.
3. **`q()` was fed a `Decimal` through `repr()`** and raised `InvalidOperation`. Typed.
4. **The orbit canonicalisation used `min` over frozensets** — a subset partial order, not a total one
   — returning 256 orbits where the true count is **80**. Canonicalised over sorted tuples.
5. **The digit-bounded numeral sweep's lookahead `(?![\d.,])` treated a sentence-ending period as a
   digit boundary**, so `2.29` scored **zero sites in a unit that prints it**. Corrected to
   `(?![\d,])(?!\.\d)`. **This is the class's fifth member and the costliest: it would have recorded a
   printed figure as absent from its own page.**

**The book was right and the instrument wrong in 1, 4 and 5.** Running tally of instrument-wrong
events: chat 110 five, 111 three, 112 zero, 113 once, 114 once, 115 twice, **116 three**.
