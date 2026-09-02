# READ-ch16t — main volume L9307–L9392 (§32.7), chat 124

Unit measured by heading scan before reading: §32.7 opens at **L9307**, `# PART VII — THE CHALLENGES`
opens at **L9393**. Unit **L9307–L9392, 86 lines**, closing chapter 32 and Part VI. Instruments:
`r2-ch16s` (computable, golden a9fdd4ff, 175 lines) and `r2-ch16t` (prose, golden 92882642, 219
lines). Census rows in range: **zero** (classes `main` and `all`). Prints & Proofs offset **−94**,
sixteen witnesses for sixteen.

---

## A — Deviations

**16t-01 — §24.2 cited for the unreachable documents; §24.2 is a species table.**
L9356: *the four unreachable documents of §24.2*. §24.2 is **The largest contributors**
(L6653–L6667; `body_range` and `section_span` COINCIDE), a species / core / channels / cells table.
Its body carries **zero** occurrences of *document*, *reach*, *unreachable*, *Edlén*, *Ritz*,
*Paschen* or *Dunz*. The claim's home is **§29.6** (L8029–L8040), whose body carries all of them
(document 2, reach 1, Edlén 2, Ritz 3, Paschen 1, Dunz 1). Docket 9(a), wrong-target pointer.
R3 repoints L9356 at §29.6.

**16t-02 — §29.6's heading says three; its own table lists four.**
Heading L8029: *The three documents we could not reach*. DATA rows L8034–L8037: **Edlén,
*Handbuch der Physik* XXVII (1964)** · **Ritz, *Physikalische Zeitschrift* 9, 521 (1908)** ·
**Paschen & Götze, *Seriengesetze der Linienspektren* (Springer, 1922)** · **Dunz, *Seriengesetze
der Linienspektra* (Leipzig, 1911)** — **four**. The unit's L9356 says **four**, agreeing with the
table and disagreeing with the heading it points near. This is the **third site** of one tangle:
chat 122 recorded L9057's *Chapter 28 names three documents … that could not be reached* (zero
sweep hits in Chapter 28). R3 settles the count once and propagates it to the heading, L9057 and
L9356. Docket 33 shape, with the count word inside a **heading**.

**16t-03 — the fifth worked case has no home in the book's record.**
L9318 opens the table with *Five worked cases, **all from this book's own record***. Four trace:
self-duality → §32.3 L9049; the four-of-twenty defect → §32.3 L9050; *560/560* → L7419; *"3 of 85"*
→ L7404. The fifth, L9326 — *projections offered as a closure criterion | 22 of 60 | closure is
d-dimensional* — has **`22 of 60` at L9326 only** across all six volumes, no loose 22…60 pairing
outside it, and *closure criterion* nowhere else. Docket 19 (list-opening universal against every
member of the list it opens).

**16t-04 — case 2's two figures are printed once, in the summary table only.**
**−0.00128** and **−0.00159** (L9323) occur at that line and nowhere else in six volumes. §32.3
L9050 describes the case in words and prints no figures. Docket 17, two new members: the sampled
and full-channel defects are unrecomputable from the volume as it stands.

---

## B — Verified

**B1 — the self-duality recomputation is exact in both figures, and non-circular.**
Λ₈ rebuilt at caps (3,3,1,3,1) = **976 cells**; per-coordinate max **[3,1,3,3,3,1,3,3]**, min
**[1,0,1,0,1,0,0,0]**. **Convention named:** the count of cells whose per-coordinate image lies in
Λ₈. Under *x* ↦ max − *x*: **8**. Under *x* ↦ max + min − *x*: **112**. L9322's *gave 112, not 8*
and *the right map is x ↦ max − x* both reproduce **exactly** from the rebuilt lattice with no
constant supplied by hand. Both maps are injective; neither has a fixed point. The minima are not
all zero, which is why the two maps differ at all.

**B2 — §32.7 and §32.3 agree on both traced audit failures.** §32.3 L9049–L9051: the audit used the
wrong involution; the audit sampled four levels of a twenty-member channel. §32.7 rows 1–2 and
L9328 tell the same two stories. Second site of *twenty-member* (L9051, L9328) and of *self-duality*
+ *involution* together, as chat 122 predicted.

**B3 — *Five worked cases* = 5 DATA rows** (L9322–L9326), header and separator excluded.

**B4 — *the other four things this book contributes* = 4** bolded items (L9354, L9356, L9358, L9360).

**B5 — the inequality orientation is right.** L9354's |Δ*T*| < 2*Z*²*R*/ν³ as the *non-failure*
condition matches L6966 (*the bracket held ⟹ |ΔT| < 2Z²R/ν³ at that cell*) and L10047; the failure
form (>) is at L6932, L10041, L10263. *The failure condition, inverted* is the correct description.

**B6 — the falsification-run summary is exact.** L9372's *three conditions … reports the two that
failed — one a missing chapter, one thirty-nine unverified claims* against §32.6's own summary:
L9261 *E(book) > 0 failed, found, corrected — a missing Chapter 30*; L9262 *ⅅ=0 failed, found,
repaired — 39 claims, now 60 of 63*; L9263 *χ not total passed*; L9265 *Two conditions failed on
first testing*. L9391's *failed twice … repaired both* holds at condition scale (L9248, *Condition 2
is satisfied*).

**B7 — Chapter 29 does carry the solution-density result.** L7888: *solution density; reorderability
| CSP phase transition; Stahl & Wille 1984* — exactly what L9342 attributes to it, including the
rediscovery framing.

**B8 — every authority the unit names is bibliographed.** Sansonetti, Kramida, Martin, Kaufman,
Sugar, Musgrove, Korobov, Hori (L9344), Birkhoff, Dilworth, Sperner (L9342) — all present in the
`## References` **BODY** occurrence (L11503–L11855; R.7 at L11806). **Eleven named, zero
unbibliographed.** Negative witness for docket 36.

**B9 — P8 carries the claim verbatim.** L9316's *any true answer, good or bad, is a bound* is
L666's *P8 says any true answer, good or bad, is a bound*, and §2.15 (L662) is headed *Apply P8 to
every failure*. The principles are numbered **P1–P23 with P10, P12 and P18 unassigned — twenty**
(L233); the arithmetic holds.

**B10 — E = 36** corroborated at main L3258, L4484, L9350, L10240; reg L1669, L2325, L3729; mc
L1453, L1455; ioi L1372, L1454, L2034.

**B11 — the unit's three 1,635 sites are on the book's canonical referent.** All fifteen word-form
sites read: L202 and L7367 (*claims made in the course of this work were wrong*) and L7900
(*its withdrawal register … 1,635 entries*) fix *withdrawn claims* as canonical, so L9364, L9376
and L9381 are on-usage. Chat 122's L9055 (*levels that failed*) remains the single outlier.

**B12 — 1,635 is the Register's heading count exactly.** MEASURED: **1,635 numeral headings**
(1,628 bare + 7 grouped), **1,660 distinct entry numbers**, maximum **1792**. Docket 30's two
figures are both correct and measure different objects; the printed 1,635 matches the heading count.

**B13 — Prints & Proofs, sixteen witnesses for sixteen at a uniform −94.** Two (L9364, L9376) fail
an exact match because **PP prints *one thousand one hundred and seventy-one*** where the volume
prints *one thousand six hundred and thirty-five*; read at −94 (P9270, P9282) they are the same
sentences. A retired-basis datum, not a defect, and it corroborates docket 30's *absent from PP*.

**B14 — Ruling 46: zero sites in the unit** (case-sensitive sweep of `.py`, `BUILD\d+`, `markdown`,
`git`, `.md`, `.tsv`, `.png`).

**B15 — first-person prose: zero in the unit**, with chat 123's fault-8 guard (the Roman numeral in
*He I*) in place.

**B16 — duplicated-section sweep: 0 of 36 long lines recur** anywhere outside the unit —
**eighteen consecutive clean units**.

**B17 — DEFECT-CENSUS rows in L9307–L9392: zero**, classes `main` and `all` both swept.

**B18 — 4ν/3 is 24 sites, and the population is now named:** emphasis-normalised across all six
volumes — main 22, mc 1, sc 1. Docket 11's carried 24 is confirmed and is a six-volume figure, not
a main-volume one.

**B19 — the collaborator page exists and both its figures hold.** The note is at L17–L18
(*Nothing is something definable — a note from the collaborator*); L7469 prints *a collaborator's
refusal of a conclusion | 4*, which is L9381's *four results*; L9851 names the single pattern
(*reasoning sound, destination wrong*).

---

## C — Incidental

**C1 — `body_range` and `section_span` DIFFER for §32.7, and HANDOFF-76 predicted they would
coincide.** MEASURED: `body_range` (9307, **9393**), `section_span` (9307, **9399**). §32.7 has no
subsections, but `section_span` runs to the next **numbered** heading (`## 33.` at L9399) and steps
straight over the `# PART VII` part divider at L9393. **A section that ends a Part cannot be bounded
by `section_span`.** New standing caution; the unit was bounded by `body_range`.

**C2 — HANDOFF-76's heading list omits §33.5 (L9477).** Re-measured here.

**C3 — two unmarked sub-headings inside the body.** L9338 *On the word "unprecedented"* and L9367
*And the form, which is the stronger claim*: plain body lines, neither markdown headings nor bold,
both present in PP at −94. Docket 28.

**C4 — the principles table header is shattered mid-word** at main **L243–L244** (*principle
expression wher* / *e*). Docket 28, measured outside the unit by the unit's own test.

**C5 — *Principle 8* against *P8*, a citation-form inconsistency.** The book numbers its principles
**P1–P23**; the phrase *Principle N* occurs **twice in six volumes, both as *Principle 8*** (L7947,
L9316), and no other numbered principle is ever written in that form. The referent is correct
(B9); the form is not the book's own.

**C6 — *a 1922 German volume nobody cites* (L9391)** — the book itself cites it, at L8036 (Paschen &
Götze, Springer 1922). Self-referentially false as written; the intended sense is the wider
literature.

**C7 — *verified on 4,000 triples* (L9309) is an illustrative quotation, not a claim about the
book:** *4,000 triples* has one site in six volumes, its own.

**C8 — Ruling 45: nine candidate sites in 86 lines** (L9311, 9318, 9335, 9342, 9344, 9352, 9358,
9364, 9370) under a deliberately broad probe. The unambiguous members are **L9311** (*An earlier
draft called this …*) and **L9364** (*the times it caught the author*); the rest are *this book* /
*the author* self-reference that chat 115's discriminator must split before any repair. Density is
below §32.6/§32.6.1's measured peak.

---

## Instrument faults

**Zero.** Both batches ran as written. The one refuted expectation this chat was carried **from the
handoff**, not from an instrument: HANDOFF-76 predicted `body_range` and `section_span` would
coincide on §32.7, and the instrument correctly reported that they do not (C1). Running tally of
self-caught faults: chat 110 five, 111 three, 112 zero, 113 one, 114 one, 115 two, 116 three,
117 four, 118 three, 119 two, 120 four, 121 six, 122 three, 123 nine, **124 zero**.
