# READ-reg1.md — the Register, unit 1: the front matter (L1–L74)

The first unit of the Register's source-order read, opened under M's compendia-scope ruling (the
Register in full under the chat-81 cadence; the other four compendia by class sweep). The front
matter is taken first because it is what every later entry is read against: it fixes the extent, the
block boundaries, the entry form, the kinds table and the load-bearing table.

**The standard this unit is scored against is the book's own.** The front matter states that its
figures are recomputed at every press — *"the citation counts and the load-bearing table
(`register_cites.py`, 1732), the kinds table below (`kinds.py`, 1756), and the entry form
(`build.py`, 1744)"*. A figure the book says is recomputed must equal the recomputation. Every
recomputation below was performed by the book's own instruments run against the seated member, never
by an operator of this reading's invention.

**Convention fixed before anything is scored (docket 30).** An entry is a heading line `### N` or
`### N, N, …`. On that convention the Register holds **1,635 entries — 1,628 bare and 7 grouped —
addressing 1,660 distinct numbers**. Counts are of headings unless stated. The distinction decides
1,635 against 1,660 and 1,470 against 1,495, and getting it wrong invents deviations where the book
is right.

Instrument: `r2-reg1a.py`, golden `r2-reg1a.out` (8,673 B · `723f0d08` · 110 lines). All instrument
checks OK; 12 deviations recorded. Nothing repaired — the chat-67 hold stands.

## A — deviations

**reg1-01 — the load-bearing table is stale in four ways at once, and it is a table the book says is
recomputed at every press.** MEASURED by `register_cites.py`:

| printed | measured |
|---|---:|
| 571 entries are cited by other entries | **593** |
| 1649 cited 9× | **10×** |
| "the 11 cited seven times or more" | **12** |
| — | **1526 at 8×, absent from the printed table** |

W-168 recorded 571/593, 1649 and 1526 as pre-existing states at BUILD90. They stand unchanged at
BUILD183 and are re-confirmed here, on the same operator. Docket 35 / 12.

**reg1-02 — the three citation figures are stale, and by a wide margin.** The closing paragraph
prints *"387 entries are cited in the main volume's chapters and appendices; 701 counting the four
compendia and the two papers; 970 counting citations by other entries."* MEASURED: **392**, **862**,
**1056**. The middle figure is out by 161. These three are new here — REGISTER_AUDIT R5 deferred
exactly this class ("load-bearing '376 cited' and per-entry cited-by counts not recomputed") to a
cross-volume citation pass, and R5's own quoted figure, 376, matches neither the page nor the
measurement. **R5's deferral is discharged: the numbers now exist.** Docket 35 / 12.

**reg1-03 — one paragraph contradicts itself on the grouped headings, seven against ten.** The kinds
paragraph says *"the 1,565 entry headings, seven of which hold the thirty-two grouped fault
entries"* and, twelve lines later in the same paragraph, *"the ten grouped headings count as
corrections and faults"*. MEASURED: **7** grouped headings, holding **32** numbers, 203 to 354. The
*seven* is right and the *ten* is wrong. Docket 33 / 28.

**reg1-04 — CORRECTED BELOW. The front matter's mature-record figures do not sum to its own total,
and it is the FRONT matter that is wrong, not the closing line.** L6 prints *"165 to 1791, 1,470 entries"*; L65 prints *"mature record
165–1792"*. MEASURED on the heading convention: 165–1791 holds **1,470** headings exactly, 165–1792
holds 1,471, and 1792 is itself an entry. So **1,470 is exact and it is the L65 range that is
wrong** — not, as the two-site reading in W-168 left it, an undecided disagreement between two
lines. Narrowed here. Docket 34 / 12.

> **CORRECTION, and the reading above is the half that was wrong.** `register_counts.py` — built by
> the cypher session and found on branch `claude/cypher-analysis-method-books-826x0x` — applies a
> constraint this reading did not: **the three blocks must sum to the total the front matter itself
> prints.** They do not. 94 + 70 + 1,470 = **1,634** against its own **1,635**, and only
> mature = **1,471** over **165–1792** sums correctly. So the defective half is the front matter's
> *"165 to 1791, 1,470 entries"* — **not** the closing line's range, which is right. Measured by
> running the tool against the seated member: it reports three drifted figures and exits 1.
>
> The tool reaches the same convention independently — *"AN ENTRY IS A HEADING, NOT A NUMBER …
> counting numbers instead gives 1,660 and disagrees with everything the volume prints"* — which is
> docket 30 and this unit's own fixed convention, arrived at twice.
>
> **It is also the repair, for this class only.** `--write` emits the Register with the extent
> figures corrected, matching each site's own numeral formatting rather than normalising it. It does
> **not** cover reg1-01 or reg1-02: `printed()` reads the total, the mature range and the back
> matter, and nothing else, so the load-bearing table and the three citation figures remain
> unrepaired and still need `register_cites.py` re-run into the page.

**reg1-05 — NEW, and the largest of the unit: the front matter's own provenance citations resolve to
nothing.** Four entries are cited by number for where this volume's own machinery is recorded —
**1725** (the settled entry form), **1732** (the citation counts and load-bearing table), **1744**
(the entry form), **1756** (the kinds table). MEASURED, directly and by the instrument: `### 1725`,
`### 1732`, `### 1744` and `### 1756` each have **0 heading lines**, while 1723, 1724 and 1726 have
one apiece. All four numbers lie inside the addressed span 1–1792.

**Why the existing sweep could not have caught them, which is the part that matters.** The
absent-and-cited class (docket 9(c) / 30, re-measured at warn-04) is enumerated by
`register_cites.py`, whose net is the phrase `register NNN` / `R NNN`. These four are printed as
bare numbers in parentheses after a script name — `` (`kinds.py`, 1756) `` — and fall outside that
net. They appear in no absent-and-cited list because no instrument has ever looked at citations in
this shape. **The front matter sits in the class sweep's blind spot.** Census row 3 flagged 1725
alone, from the one site written as *entry 1725*; the other three are unflagged and unrecorded.
Docket 9(c) / 2.

**reg1-06 — Ruling 46 and Ruling 38 in the front matter.** MEASURED: four script names visible to
the reader (`build.py`, `kinds.py`, `register_cites.py`, `register_gen.py`) and two build handles
(*Build 9*, *Build 16*), inside a block Ruling 38 makes a purpose statement only. Ruling 46 forbids
script names, build numbers and internal file references in a reader-facing volume. The generator
paragraph is entirely production narration. Docket 6 / 5.

## B — verified

- **The kinds table reproduces exactly, all eight rows.** `kinds.py` over 1,565 headings returns a
  finding 1,356 · a correction 149 · a measurement 499 · prior art 61 · a new protocol 23 · a
  withdrawal 33 · a fault of mine 16 · an open question 23 — every one as printed. The 1,565
  reconciles with the 1,635 of the population: 1,635 − 70 supersession stubs (95–164), dropped under
  the chat-52 ruling.
- **The extent and the block structure.** 1,635 headings; extent 1 to 1792; genesis 1–94 complete at
  94; superseded 95–164 complete at 70. All as printed.
- **The grouped fault entries.** Thirty-two, 203 to 354, and every one of the seven headings printed
  after entry 361 (361 at L1315; the headings at L1319–L1343). The front matter is right here and
  REGISTER_AUDIT R3's *"forty fault entries (203–358)"* is the stale statement, not this one.
- **Six of the ten front-matter pointers resolve to their claim** — 868 (R∞ → R_M, Bohr 1913), 1241
  (the sharpened attributions), 1139 (the multiplicity constraint proved), 1178 (carried into the
  operator), 1208 (the dependency cycle), 1225 (the three new prime audits, audit 24).

## Census

Three rows engaged, all in `CENSUS-CLOSURES-reg1.tsv`. Row **3** (C5-REGISTER-POINTER-UNRESOLVED,
*entry 1725*) closed **a defect** — the reading reached it independently and extends it to three more
numbers. Rows **1232** and **1233** (C9-OVERGENERALISATION-WORD, *never*) closed **not a defect**:
in both the flagged token is the section's own stated discipline or a bounded statement about this
file, which is the C9 regex-artefact precedent (678, 680–687, 1067, 1069).

## C — incidental

- The front matter carries no `§` pointer except two inside table cells (§2.9, §4); both resolve.
- *"the four compendia and the two papers"* is right on the count: five compendia exist and the
  Register is one of them, so four others.
- `register_cites.py` reports **31** numbers cited with no entry. That is docket 9(c) / 30's class
  and is not re-scored here; reg1-05 adds four the enumeration cannot see.
