# READ-ch14t — Chapter 24 second read: §24.8 and §24.9, main L6741–L6816

Chat 100. Unit MEASURED by heading scan on `The_Method_1_6-2.md`: §24.8 opens L6741, §24.9 opens
L6752, §24.10 opens L6817. **76 lines, two headings.** HANDOFF-52's boundaries confirmed exact —
re-scanned, not carried. Instruments: `r2-ch14t` (computable, golden `36d7afbc`, 117 lines) and
`r2-ch14u` (prose, golden `3eaa668d`, 179 lines). Both read the six volume members by name.

The Spectra Compendium parse reproduces the compendium's own totals line at spectra L900 exactly:
**596 channel rows · 28 elements · 2,269 interior cells**, 119 two-member rows, 477 rows with three
or more levels, section II measured at spectra L293–L934.

---

## A — Deviations

### 14t-01 — the unit is built entirely on a basis the same chapter retires 109 lines above it

L6632, in §24 itself: *An earlier version of this chapter read "1,442 interior cells across 35
atomic systems, the bracket holds in every one." That figure matches neither Appendix B's totals
line (1,105) nor its table (869) nor the present tested count (930)… **Four numbers for one
collection is a disclosure, not a reconciliation**.*

MEASURED across Chapter 24 (L6623–L6883):

| figure | status at L6632 | sites in chapter 24 |
|---|---|---|
| 1,442 | **retired** | 13 — L6632 (the retirement) and **twelve in this unit** |
| thirty-five / 35 atomic systems | **retired** | 2 — L6632 and **L6792, in this unit** |
| *the bracket holds in every one* | **retired** | restated in the unit's own words at L6746, L6750 |
| 1,105 (Appendix B totals line) | current | 1 — L6632 only |
| 869 (Appendix B table) | current | 1 — L6632 only |
| 930 (present tested count) | current | 1 — L6632 only |

The twelve unit sites for 1,442: L6742, L6744, L6746, L6750, L6767, L6786, L6799, L6802, L6804,
L6805, L6810, L6811. **The current basis is named once each; the retired basis carries the
argument.** 1,442 has **30 main-volume sites** in total, so the repair surface is not local to
this chapter.

This is chat 99's 14r-01 arriving at its cause. 14r-01 read the headline totals as *stale, not
wrong*; the sharper statement is that the chapter **knows** they are retired, says so in print, and
then runs two whole sections on them. R3 cannot fix this with a corrected digit: §24.8 and §24.9
need recomputation on whichever basis the chapter settles, and L6632 says the twenty rows that
would reconcile the four numbers are owed.

### 14t-02 — "none produced a failure" contradicts the chapter's opening and the compendium

- L6746: *counting **one effective test per channel** — gets **190 rather than 1,442**, and the
  bracket holds in all 190.*
- L6750: *It is that 190 channels were examined, each exhaustively, and **none produced a failure**.*
- L6626, same chapter: *it passes 546 of 789 interior cells — 69.2%… It fails on 243 cells across
  62 channels.*

MEASURED at the Spectra Compendium: 392 channels carry an `m/k` bracket; **294 hold in every cell,
98 contain a failing cell**, 161 failing cells, **1,577 of 1,738 = 90.7 %** (HALF_UP, 1 dp). The
remaining rows read `no-triple` (78) or `untested` (126). No basis makes the no-failure claim true.

### 14t-03 — the He I provenance contradiction: three positions in one section, and Register 436 settles it against two

The section states its own rule and then violates it:

- L6760–L6762: *`[ ]` is "interpolation, extrapolation, or other semi-empirical procedure" and
  explicitly includes "fitting the Ritz-type formulas along series of levels"; `( )` is "determined
  from an ab-initio calculation". **This section reads `[ ]` as covering ab initio and it does not.***
- L6763: *every level in the table is bracketed* — 1s² through 1s16d without exception.
- L6767: ***Its 189 cells — the largest single block of the 1,442 — are not independent tests***.
- L6787: *He I's nine certainly* [contain no independent test].

against

- L6807–L6809: *He I's bracketed values are **ab initio** and are the sharpest tests in the
  collection, so the bracketed set is not uniformly dependent.*
- L6815: *He I's are **ab initio QED calculations** — variational, with relativistic and radiative
  corrections… **Those are genuine tests**, and at uncertainties of 10⁻⁹ cm⁻¹ they are sharper than
  any measurement here.*

**Register 436 sides with L6767**, verbatim: *He I HAS NO OBSERVED LEVEL VALUES IN THE ASD… §24.9
read `[ ]` as ab initio; NIST marks ab initio with `( )`.* **The collection's largest block — 189
cells — contains no independent test.** L6807–L6809 and L6815 are unretired text surviving their
own correction, and L6815 is the section's closing paragraph — the last thing a reader sees.

### 14t-04 — L6791 supersedes a phrase L6811 still prints as the honest form

- L6791: *That is the honest form and **it supersedes *an unknown proper subset***.*
- L6811–L6812, twenty lines later: *The honest form is **1,442 cells, an unknown proper subset of
  which are independent**, and it should be written that way wherever the figure carries weight.*

### 14t-05 — "The book has never counted the three" is refuted inside its own section

L6801: ***The book has never counted the three.*** L6781 counts H I (13 of 64); L6791: *two species
of thirty-five are done*. Census row 1142 flags the *never*; the row is a **defect**, and the reason
is co-located stale text, not the over-generalisation word.

### 14t-06 — L6809's "§18's exclusions" has no target — eleventh member of the pointer class

L6809: *§24.11's decline modes and **§18's exclusions** rest on measured levels.* MEASURED: §18
spans L4922–L5380 (459 lines) and carries *exclusion* 0, *exclusions* 0, *species* 0, *levels* 0.
Whole-main-volume sweep for *exclusions*: eight sites (L664, L3374, L6809, L6890, L6926, L8733,
L8781, L11070), **none in §18**. The target is §25.2, *Five exclusions, which are three mechanisms*
(L6890, restated L6926), which the book's own front matter at L62 already pairs with the decline
modes. §24.11 in the same sentence resolves correctly.

### 14t-07 — "Ne I's sixteen contribute 131" matches no species

L6746. MEASURED: **Ne I is 7 rows / 39 interior cells / 51 levels; Ne II is 37 rows / 69 interior /
138 levels.** Neither the channel count nor the cell count matches under either species. Second
witness for chat 99's finding, which recorded the same pair from §24.2 — the figure recurs here,
so the repair is a class and not a site.

### 14t-08 — "the largest single block" is false at the current basis

L6767 calls He I's 189 *the largest single block of the 1,442*. MEASURED, largest blocks by interior
cells: **Si I 290**, He I 189, Al I 94, Na I 80, Ne II 69, Li II 62. Under the 1,442's own retired
basis the claim cannot be checked at all; under the compendium's current rows it is false.

### 14t-09 — "thirty-five" is returned by no base swept

L6791: *two species of **thirty-five** are done*. Seven bases swept: all species **70**, all elements
**28**, species with an `m/k` bracket 65, species with ≥3 levels 68, species with a failing bracket
34, species with a two-member row 37, neutral species (X I) 18. None returns 35. The 35 is the
retired *35 atomic systems* of L6632 (14t-01).

### 14t-10 — "worse than scattered" runs against both computations available

L6783–L6784: *And the collection is worse than scattered, because the derived values are the high-n
ones, which is where the channels run.* Two measurements, both against it:

1. **The section's own model, on the section's own species.** (1−f)³ at H I's f = 0.62 predicts
   5.49 % of cells surviving as tests. L6781 measures 13 of 64 = **20.3125 %** — **3.70× better**
   than scattered, not worse.
2. **Clustering versus scattering at fixed derived count.** Over all C(10,4) = 210 arrangements of
   four derived levels among ten, clean triples range **0 to 4**: strict alternation (2,4,6,8) — the
   scattered case, and precisely the nd series L6782 calls *the sharpest case* — gives 0; clustering
   at high n (7,8,9,10) or low n (1,2,3,4) gives 4. **Scattering is the worst case; clustering is the
   best.**

The claim can only rest on derived values co-locating with the *tested* cells rather than on
clustering as such, and that is computed nowhere in the six volumes.

### 14t-11 — Ruling 45 exposure: seven sites in 76 lines

L6748 (*the one this book would defend*), L6756 (*the caveat is sharper than it was written*), L6791
(*it supersedes*), L6801, L6803 (*the classification was never carried into the collection*),
L6810–L6812 (*the book has occasionally come close to saying it… **it should be written that way
wherever the figure carries weight***), L6813 (*Recorded in Q as item P — obstacle retrievable, cost
hours*). **L6812 is an instruction to the author printed in a reader-facing volume**, the strongest
of the class so far. Joins the six-member Ruling 45 docket.

---

## B — Verified

- **B1.** L6746/L6767's He I block: **9 channels, 189 interior cells** — MEASURED 9 rows, 189. Exact.
- **B2.** L6781's percentage: 13/64 = **20.3125 %** → printed *20 %* holds at 0 dp.
- **B3.** **Register 437 corroborates L6771–L6784 in full** — the (1−f)³ law, H I at 38 % plain,
  **13 of 64 interior cells**, the nd series' *six plain levels of ten and not one clean triple*.
  This settles chat 99's **14r-06**: the Register carries the **64**, so §24.7's *H I gives 5 cells*
  (L6729) stands alone against both L6781 and the Register. R3 repairs L6729, not L6781.
- **B4.** Survival table rows 1–3: 0.9³ = 0.729 → 0.73; 0.8³ = 0.512 → 0.51; 0.7³ = 0.343 → 0.34,
  all HALF_UP-exact at 2 dp. The *cells surviving* column equals 1 − f at all four rows.
- **B5.** §24.11 resolves — *Four ways a species declines* (L6826–L6843), carrying *declines* and
  *exclusion*.
- **B6.** Registers 246, 436 and 437 all resolve and carry the claims cited at L6792 and L6813.
- **B7.** **Q item P resolves exactly.** L10958: *P — the 1,442 split into independent and
  Ritz-derived tests — one claim — retrievable — hours — physical.* All three attributes L6813
  prints (*obstacle retrievable, cost hours, blocks one stated claim*) match the table.
- **B8.** L6782's nd arithmetic is consistent: ten levels → eight triples; four derived alternating
  leaves zero clean triples, verified over all 210 arrangements.
- **B9.** Neither heading's sentence finishes in the body — the three-member class (L4407, L6582,
  L8659) does not grow.
- **B10.** Name forms uniform: NIST ×1, ASD ×6, Drake ×1, Kandula ×1, Ritz ×5, QED ×2, one form
  each. Drake and Kandula have exactly two main-volume sites apiece (L6765 and the bibliography at
  L11520/L11521).
- **B11.** Boundaries re-scanned: §24.8 L6741, §24.9 L6752, §24.10 L6817 — HANDOFF-52 exact.
- **B12.** Q's open set is internally consistent: E.1.2 lists 14 items of which K, M, N and O are
  CLOSED, leaving **ten open of 14**, exactly as its heading states.

---

## C — Incidentals

- **C1.** The survival table's fourth row is the table's only tie: 0.5³ = **0.125 exactly**, printed
  **0.12**. HALF_UP gives 0.13; HALF_EVEN and truncation give 0.12 — and 0.12 is what Python's
  `round()` returns. The convention is unstated. A boundary case, not a violation; it joins the
  *conventions unstated* half of the unprinted-input class.
- **C2.** 1,442 / 190 = 7.59 cells per channel. He I's 189/9 = **21 exactly**; Ne I's printed
  131/16 = 8.1875, not integral — the two printed pairs are not of the same kind.
- **C3.** **No volume records per-level provenance.** Spectra rows carrying a provenance column: 0.
  Lines carrying both *observed* and *derived*: main 4, register 5, math 1, physics 1, index 0,
  spectra 0. So L6753–L6754's Al I comparison (*derived levels bracket exactly as observed ones do —
  and slightly better*) and the three-way split of the 1,442 cannot be recomputed from the six
  volumes at all — an *inputs absent* member, and it is exactly what Q item P says is owed.
- **C4.** *10⁻⁹* has four sites across the volumes: main L6815 and L8625, math L3208, spectra L1122.
- **C5.** **Instrument fault, self-caught and rewritten.** The first channel-table parse was
  unbounded and captured Section V's capture-groups table — 600 rows, 2,317 interior cells, 32
  elements, against the compendium's own totals line of 596 / 2,269 / 28. The instrument was
  suspected first, as the standing rule requires; bounded to section II's measured span
  (spectra L293–L934) it reproduces 596 / 28 / 2,269 / 119 / 477 exactly. A second fault — a dead
  misspelled-constant branch in the rounding pass — was caught before first run. Neither was
  trimmed.
- **C6.** **HANDOFF-52 named the wrong Register entry, and the cause is diagnosable.** It sent this
  chat to *Register 1625* for *independence is a property of triples*. Register 1625 is **THE
  4D-IN-1D CLAIM IS REFUTED IN ITS STRONG FORM…** and carries *independence* zero times. The
  independence entry is **Register 437**, at Register-member L1623 — and *13 of 64* sits at
  Register-member **line 1625**, inside 437's body. A line number was carried forward as an entry
  number. §24.9 L6792's own citation, *Registers 436 and 437*, was correct all along.
- **C7.** L6756 promises the caveat is sharper *on two counts* and delivers both — *First* at L6759,
  *Second* at L6771.

---

## Census rows closed in range

Two rows fall in L6741–L6816; both are C9-OVERGENERALISATION-WORD on *never*.

- **1142** (L6801, *never*) — **defect.** The sentence *The book has never counted the three* is
  refuted by L6781 and L6791 inside its own section. Co-located stale text counts against its census
  row (chat 70 ruling).
- **1143** (L6803, *never*) — **not a defect.** *The classification was never carried into the
  collection* is the sentence's own accurate claim: MEASURED, no volume records per-level provenance
  (C3). Regex artefact, precedents 678, 680–687, 1067, 1069.
