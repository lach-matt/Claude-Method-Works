# READ-32a.md — chat 152 (Cowork) — the origin of §32.1.4's three totals, under M's ruling (c)

Instrument `r2-32a.py` (22,360 B, md5 `15a9047af4a637eb7bdb05d0ea982878`, 306 lines), golden `r2-32a.out`
(16,587 B, md5 `0d5d75a2264ff50217db542a5baf28c6`, 179 lines). ALL INTEGRITY CHECKS OK, one deviation
recorded. Reads the six volumes and Prints & Proofs as members. Deterministic.

**WHAT WAS OWED.** 26c-02 recorded that three totals for §32.1.4 stand at once — the printed *fifty-five*,
§32.1.4.1's 48 with register 373, and register 375's 47 — and put to R3 the choice between the section
taking 375's change and 375 being corrected. **M ruled (c), a third state: find where each of the three
numbers came from.** This is that reading. It also corrects the finding that recorded it.

**CONVENTION ORIG, stated before anything was scored.** A total's ORIGIN is the object that computed it —
a printed component set whose sum reaches it, or an entry that states it as a readout. A total is
REPRODUCIBLE only if some assignment of PRINTED values to the four components §32.1.4's own table names
sums to it; a component value appearing nowhere in the six volumes or Prints & Proofs may not be supplied
to close an arithmetic. Where no printed assignment reaches a total, the entry stating it is its only
provenance — a fact about the record, not a defect in the arithmetic.

## The origins

**55 — §32.1.4's own table, and the only one of the three a reader can reconstruct.** The section's table
carries seven rows, four of them E-bearing (a *cells named and unoccupied* entry that is not an em dash):
Appendix D unfibred **4** (*four*), Appendix E (Q) unfibred **1** (*one*), Appendix F the numbers **33**
(*thirty-three*), the audit set at four coordinates **17** (*seventeen*). 4 + 1 + 33 + 17 = **55**, exact,
against L8978's *Fifty-five cells are named and nobody has put anything in them* — the only site, and the
total is printed as a word. **Measured: (4, 1, 33, 17) is the ONLY assignment of printed values reaching 55.**

**48 — §32.1.4.1 / register 373, and two of the four components are not restated.** The three-state table
moves two: E over the numbers index 33 → 21 → 23, E(Q) unfibred 1 → 1 → 4. Appendix D unfibred and the
audit set are carried at their §32.1.4 values and are not restated anywhere on the page. 4 + 4 + 23 + 17 =
**48**, exact, against L8998's *Recomputed now the total is 48*. Every figure about Λ (E(Λ), |Λ|, |J(Λ)|,
the surplus) is identical in all three states; every figure about the book moves — which is register 373's
own headline and reproduces here.

**47 — register 332's press readout, and 375 restates it rather than originating it.** §32.1.4's own
citation is *Register 332*, and it is missed by a line-wise pointer sweep because *Register* and *332.*
sit on either side of a line break: the line-wise sweep returns [278, 285, 294] and the
whitespace-normalised join returns [278, 285, 294, **332**]. Register 332 (Register L1231) states in terms:
*THE TOTAL IS A READOUT THE PRESS PRINTS AT EVERY BUILD — **47 AT THE TIME OF WRITING**, HAVING BEEN **55**
WHEN THIS SECTION WAS FIRST COMPUTED*, and carries the shape sentence. **So the 47 does not enter the
record at 375. It is there at 332, before 373 printed 48.**

## The chronology, and why three totals stand at once

Entry order is append-only, so the record's own sequence is:

| state | total | site |
|---|---|---|
| §32.1.4 as first computed (332's words) | **55** | Register L1231 |
| register 332, a press readout | **47** | Register L1231 |
| register 373 / §32.1.4.1 | **48** | Register L1379 |
| register 375, discharging §2.21 | **47** | Register L1387 |

**The total is not monotone: 55, 47, 48, 47.** The record has it at 47 *before* it has it at 48. Register
375's 47 is not a further movement down from 48 — it is 332's figure restated after 373 printed a higher
one. **That is the mechanism behind 26c-02**, and it is not the mechanism 26c-02 named.

## 32a-01 — 26c-02 IS CORRECTED (deviation)

26c-02 recorded that *the replacement shape sentence appears in no volume*. **Measured, case-folded over
all six volumes and Prints & Proofs: it has TWO sites, both in the Register — entries 332 and 375.**
Zero in the main volume's chapters, zero in the other four compendia, zero in Prints & Proofs. What is
true, and is what the finding meant, is narrower: **§32.1.4 does not carry it.** A claim about a volume is
not a claim about a section, and the recorded wording scored the wrong object. Recorded, not repaired.

## 32a-02 — the answer to the ruling: only 55 is reproducible, and the 47 mixes two states

Every printed value of each component, swept over the six volumes: Appendix D unfibred **{3, 4}**; E(Q)
unfibred **{1, 5}**; the numbers index **{21, 23, 33}**; the audit set **{0, 11, 16, 17}**. Over the
Cartesian product:

- **55 is reached by exactly ONE assignment** — (4, 1, 33, 17), §32.1.4's own table.
- **48 is reached by THREE** — (3, 1, 33, 11), (3, 5, 23, 17), (4, 5, 23, 16).
- **47 is reached by TWO** — (3, 5, 23, 16) and (4, 5, 21, 17).

Of the two reaching 47, only **(D 4, Q 5, numbers 21, audits 17)** agrees with the shape sentence that 332
and 375 both assert in the same breath (*the audit set seventeen*); the other takes the audits to 16. And
that one **mixes two states of the book**: the numbers index at **21** is §32.1.4.1's *before compression*
column (main L9010), while E(Q) unfibred at **5** is §32.6.1 / register 396's readout at *the build that
produced this page* (main L9270), which is after compression.

**32a-02a, the corollary that decides it.** A readout is reproducible only if its inputs are printed at ONE
state. §32.1.4.1's own rule is that a figure about the book *is true of a state, and the state is named*.
The 47 satisfies its own shape sentence only by drawing components from two states, so it is not a reading
taken at one moment. **Three totals stand at once because the record prints components from four states and
a total from three of them.**

## 32a-03 — the instrument that computes the largest component is not a member, and was itself a rebuild

Register 435 (Register L1615): ***densities.py* AND *numbers-index.py* WERE ABSENT AND ARE REBUILT FROM THE
PRINTED rules.** *Five of six densities reproduce exactly and the sixth to a rounding … All six build-time
readouts run for the first time.* Measured against BUILD184's members: **`numbers-index.py` is not a member.
Neither is `densities.py`, `indices.py`, `appendix_audit.py`, `mathreg.py`, `compendium.py`,
`register_gen.py` or `guard.py`.** `register_cites.py`, `kinds.py`, `build.py` and `close.py` are.

`build.py` **is** a member and computes none of it: it is a prose-substitution press — 919 lines of
markdown/pandoc repair and a substitution table whose job is to **strip the script names out of
reader-facing prose** (`'**densities.py* AND *numbers-index.py*'` → `'**the six densities* AND *the numbers
index*'`). It contains no arithmetic over the four components. **So the origin of the 47 is a reconstruction
of an absent instrument, the reconstruction is not held either, and the total cannot be re-derived from the
artefact as delivered. This is docket 38 — a figure whose instrument is not a member — not docket 12.**

## 32a-04 — register 332's own text is damaged where it would answer the question

Read entire, as docket 9(b) asks, 332's body reads: *Across its six indices**since** been confirmed by
occupants arriving.* **Two sentences collapsed with text lost between *indices* and *since*.** The entry
§32.1.4 cites for its total is damaged at exactly the point where it would say how many of the named cells
have since been filled — the figure §32.1.4's own *confirmed three times* paragraph depends on. Append-only:
a new entry citing 332 restores the sentence; 332 is not edited.

## Faults of mine, caught before banking and named

1. **`entry()` read the MAIN member for register entries.** The registers live in the Register member; main
   and register are separate members of separate bundles. Corrected; every entry line number here is a
   Register line.
2. **The pointer sweep was line-wise and missed *Register 332*** — the pointer wraps a line break. Corrected
   to the whitespace-normalised join, and both sweeps are printed so the difference is visible. This is the
   chat-125 convention (a list wrapping across two lines is read on the normalised join) applied to a
   citation, and it is why 26c-02 could record 375 as the 47's home.
3. **The shape sweep was first case-sensitive and over MAIN only**, which reproduced 26c-02's *no volume*
   verdict. Widened to all six volumes and PP, case-folded.
4. **§32.6.1's E(audits) = 16 was first admitted without asking whose readout it is.** §32.6.1's readout is
   a FIVE-term set over a different index family (Λ, audits, G, Q, D — sixty-five cells), not §32.1.4's
   four. The value is admitted as a printed value of the audits component, and the distinction is printed
   beside it, because a value is printed or it is not.
5. **The draft of §6 asserted that NO shape-consistent assignment reaches 47** and would have recorded the
   47 as flatly unreproducible. The scan found (4, 5, 21, 17). **The scan was right and the assertion was
   corrected to the measurement** — the same fault class chat 151-B recorded at 28a-06.

## Census

**Zero DEFECT-CENSUS.tsv rows fall in main L8963–L9029** under any class value. `CENSUS-CLOSURES-32a.tsv`
is header-only per the chat-70 R1 rule.

## Not measurable, recorded

Whether the press's own run at 332 used (4, 5, 21, 17) or a component set the book never printed. The
readout's inputs are not on the page and `numbers-index.py` is not a member; the assignment above is the
only shape-consistent one **available**, which is weaker than saying it is the one that was used.
