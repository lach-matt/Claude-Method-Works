# PHASE 1 LEDGER — the mathematics leg, worked item by item

M, 7 September 2026: *"everything you just asked about finishing has already been ruled. it all must be
done."* Phase 1 of `PLAN-R4-PUBLICATION.md` is *"every computable claim still unproven or contradicted,
re-derived by a standard-library instrument and settled by entry before any prose moves"*, and
`PLAN-R4-ANNEX.tsv` holds **41 open rows** in it. `RULINGS-R4c` §3 fixes the order: **subject matter, then
prose, then pointers**, so this leg stands in front of the prose pass.

**One instrument per class, banked, each with a `--selftest` whose fixtures are the corpus's own recorded
numbers.** Nothing is repaired in a volume by this ledger; what each instrument settles is what the
Register entry for its class will record.

---

## Worked

### J-20 · §32.1.1's self-index — `bookindex2.py`, selftest 10 of 10

§32.1.1 prints its index as *"Recomputed at this build (2026-08-24, `bookindex.py`), over the thirty-five
chapters and six appendices the book now has"*. **The book has thirty-six chapters and seven appendices** —
measured from its own headings, 1 to 36 with no gap, and A to G.

**And the instrument is as stale as the sentence.** `bookindex.py` hard-codes `APP='ABCDEF'`, filters
references with `1<=r<=35`, and sets `n=41  # 35 chapters + 6 appendices`. **Three constants, not a
reading** — so no re-run of it can ever count Chapter 36 or Appendix G. The answer is a successor
instrument, which is what the store did twice before (`census` → `census2`, `r2-reg1a` → `r2-reg1a3`) and
never an edit to the seated original, which G0c forbids.

| | printed | at the seated bounds | at the true extent |
|---|---|---|---|
| claims | 1,021 | 1,014 | **1,021** |
| cells | 400 | 402 | **410** |
| box | 1,681 | 1,681 | **1,849** |
| E(book) | 1,265 | 1,302 | **1,407** |

**The claim count is current and the three box-dependent figures are not**, which is a sharper result than
"the sentence is stale": what has moved is the box, because the extent moved.

### D-60 · F-191 · H-23 · §10.2's range in cell count — `voidrange.py`, selftest 9 of 9

Two lines apart, of one measurement: §10.2 prints *"a **seventeenfold** range in cell count"* and Figure
10.1's caption prints *"a **hundredfold** range in cell count"*, with an appendix row at *"2.4 points over
a 100×"*. **Every cell-count ratio the record names is computed, and none is seventeen and none is a
hundred**: the tower Λ₈→Λ₁₃ is 204×, Λ₈→Λ₁₂ 72.6×, Λ₈→Λ₁₁ 13.9×, Λ₈→Λ₁₀ 2.6×, and register 1830's six
sampled settings reach 234,340 cells from 976, which is 240×.

**Register 1830 already recorded why it cannot be decided**: the base-cap pair population is 475,800, *"no
one-parameter cap family from the base sums to 776 million"*, and the figures are *"a measurement at a
population the record does not name"*. **So this is not a choice between a right number and a wrong one.
Both printed ranges are unsupported, and what the volume owes is the cap family**, after which the ratio is
arithmetic. Main L3538's *"2.17-fold spread"* is a different object and is named so it is not swept in.

### D-05 · G-01 · the σ collision — `sigmacollision.py`, selftest 7 of 7

**Rule 4 (§22.2)**: *"take σ = 2R Z_eff² · SE_pred / ν³ from the fit's prediction standard error"* — σ is an
**output**. **§22.5**: *"r = 2Z²R / (ν³σ) ≥ 5 … r falls as ν⁻³"* — σ is an **input**.

**Substitute one into the other and the ν³ cancels exactly**: r = Z²/(Z_eff²·SE_pred), a constant in ν. So
if §22.5's σ were Rule 4's σ, **§22.5's own next sentence would be false** — r would not fall as ν⁻³ and no
channel would ever leave the domain. **The two σ are necessarily different quantities**, and the chapter
corroborates it two lines above Rule 4: *"This book's tightest bracket is 1.398 cm⁻¹; limit uncertainties in
the collection run 0.001 to 0.4 cm⁻¹"* — measured level uncertainties in cm⁻¹, constants of the channel,
which is exactly what makes r fall as ν⁻³. **Which symbol is renamed and where is prose, and prose is M's.**

### F-147 · §34.6's eighteen resets — already settled, and against me

The row reads *"'resets eighteen times' (8+6+4) not reproduced"*. **`FINDING-R4-01` is the withdrawal of
that finding**: the entry's parenthetical *"(four of them also openings)"* makes the three classes disjoint,
8 + 6 + 4 = 18 reproduces exactly on the seated ground configurations, and every figure register 1333 prints
returns. **The book is right and the error was mine.** No instrument is owed.

### D-61 · the 1,585-fold — withdrawn at W-245

Ruling 10, executed as work matter: the interval the printed inputs allow is [1577.81, 1588.07) and 1,585
lies inside it. `method/proofs/precision.py`.

### E-033 · §14.3's bundling claim — `bundling.py`, selftest 7 of 7

§14.3: *"What fails is bundling … In tests, the same sets presented bundled and presented decomposed both
gave **80/80 agreement** — the theorem survives, but only when the presentation respects it."* **The
evidence cited is a test in which bundling changed nothing**, offered in support of a conclusion that
requires a case in which it changes something.

**The claim is true and the demonstration is three cells.** On the 2×2×2 box,
{(0,0,0), (0,1,1), (1,0,1)} has **E = 1 decomposed and E = 0 bundled**: the cell (0,0,1) that the
three-coordinate closure adds is invisible once two coordinates are folded. **And the reason is general** —
with two coordinates the only pairwise projection is the set itself, so ℛ(X) = X for every X, verified on
3,000 random sets. **The chapter is right about the mechanism and cites the wrong experiment for it**, and
the right one is now printed.

### J-12 · the Physics Compendium's 27 "objects rest on it" — `pcrest.py`, selftest 8 of 8

The volume states the rule (register 1740) and says the counts are *"counted from the Mathematical
Compendium **at this build**"*. **The compendium's 299 objects carry no dependency field** — title,
statement, construction, *Proved —*, *Prior art*, and no edge. Built the most natural way, an object
depending on another when its body names that object's title, the graph has **208 edges** and the closures
from the volume's own listed seeds come out **7 and 6 against the printed 66 and 72** — short by an order
of magnitude, so it is not the graph the volume used, and no other edge rule is printed anywhere.
**The counts stand as the record's; what cannot stand is "at this build"**, which tells a reader they can
re-derive a number no printed structure supports.

### E-042 · register 497 withdrawn and then cited — `withdrawncite.py`, selftest 8 of 8

The complement of `r2-warn`, which censuses the entries that **carry** a `WARNING:` and cannot see one that
does not. Every main-volume line that both uses a withdrawal word and names a register is collected: **three
registers**, and **exactly one is withdrawn and then re-cited as authority**.

**Register 497.** Withdrawn at main **L3883** — *"the counting/coupling split they were read as showing is
withdrawn with register 497"* — and rested on at **L3920** and **L3951**: *"the exact triangle costs cells,
it costs E, and it costs seed. Register 497."* **The entry carries no `WARNING`.** So the volume withdraws
an entry and then rests a conclusion on it, in one section, and nothing in the Register tells a reader
either thing. Which reading survives is subject matter.

---

## The triage of the rest, so that no row is unknown

`PLAN-R4-ANNEX.tsv` holds 41 open Phase 1 rows. **Eleven are disposed above** — J-20, D-60, F-191, H-23,
D-05, G-01, F-147, D-61, E-033, J-12, E-042. The remaining thirty are classified here by **what blocks
them**, which is the thing Phase 1 needs to know before it can be worked, and E-075 is the annex's own
ruling for one of the three classes: *"companion-side and single-witness figures … must be declared
unverifiable, not left open-looking."*

**A · COMPUTABLE FROM THE VOLUMES, and each is a census instrument still to be built (9 rows).**
D-12 and E-081 (the unprinted-input class: sixty-plus derived figures printed without the inputs that
reproduce them — a census of sites, not a re-derivation), D-14 and E-089 (truncation printed as equality:
V = 4ν/3 at twelve sites and §23.6's asymptotic `=` forms), D-16 (main-volume against compendium
contradictions), D-21 (the false-universal and superlative class, grown by fourteen new C9 rows), D-23
(end-rule overstatement at twenty-three sites), D-36 (some thirty printed counts with unnamed
conventions), I-021 (the iff/equivalence/exactly claims of Chapters 8–11 that hold one way).

**B · NEEDS DATA THE REPOSITORY DOES NOT HOLD, and the standing rule closes them (10 rows).**
`CLAUDE.md` §5: *never withdraw a recorded finding on reconstructed evidence without the original
instrument.* F-217 says so in its own words — *"UNREPRODUCIBLE without ASD captures"* — and the same holds
of E-094 (K I nd 45.7 against 12.7 and the collection-side claims), E-110 (rounded-table truncations from
the collection), F-196 (the muon paper's figures, one site and no instrument), F-238 (*"thirty-seven
objects"* record-carried), I-048 (the 153 / 1,105 / 1,442 / 763 collection family), I-089 (the Löwdin
deliveries, ten items never received), E-014 (12t-03's further sites, which need the variation runs),
D-27 (the inherited-estimate class, never swept and with no held estimates), D-39 (Chapter 34's walk
figures under no named convention — the convention is what is missing, not the arithmetic).
**Under E-075 these are declared unverifiable here rather than left open-looking**, and a figure so
declared is not a defect: it is a figure whose witness did not survive the chat era.

**C · SINGLE-WITNESS AND POINTER WORK THAT IS PROSE-CLASS (11 rows).**
D-19 and E-075 (the single-witness class itself), D-37 (withdrawn-figure-re-asserted — `r2-warn` is its
live instrument and `withdrawncite.py` is now its complement, so what remains is reading, not measuring),
F-175, F-176, F-179, F-251 (Appendix A and E's wording, single-witness counts and vocabulary), I-020
(Chapters 7–8 promise settings and do not print them), I-061 and I-063 (Appendix E item-state drift and
pointer defects), F-258 (the 1,585-fold's two sites, whose arithmetic ruling 10 already settled and whose
wording is prose).

**So Phase 1's shape is now known rather than counted**: nine rows want an instrument each, ten are closed
by a rule already in force, eleven are prose the pass ahead will carry, and eleven are done.

---

## Class A, first item worked

### D-14 · E-089 · V = 4ν/3 printed as an equality — `vprice.py`, selftest 11 of 11

**`4ν/3` occurs 24 times on 22 lines of the main volume and once in the Mathematical Compendium**, in
tables, summary rows, the chapter's thesis sentence and a section title — almost always with an equals sign.
**One site says otherwise**, §23: *"The exact V is rational at every ν — 32/11, 54/13, 256/47, 250/37,
4000/299 — and 4ν/3 + 4/(9ν) is its **asymptotic** form, low by 0.69% at ν = 2."*

| ν | exact V = 4ν³/(3ν²−1) | printed | 4ν/3 + 4/(9ν) | low by | bare 4ν/3 | low by |
|---|---|---|---|---|---|---|
| 2 | 32/11 | 32/11 | 2.888889 | **0.69 %** | 2.666667 | **8.33 %** |
| 3 | 54/13 | 54/13 | 4.148148 | 0.14 % | 4.000000 | 3.70 % |
| 4 | 256/47 | 256/47 | 5.444444 | 0.04 % | 5.333333 | 2.08 % |
| 5 | 250/37 | 250/37 | 6.755556 | 0.02 % | 6.666667 | 1.33 % |
| 10 | 4000/299 | 4000/299 | 13.377778 | 0.00 % | 13.333333 | 0.33 % |

**All five printed rationals reproduce exactly** from the closed form, so the object is identified beyond
doubt; the two-term asymptotic is low by **0.69 %** at ν = 2, which is the volume's own figure; and the
**bare form is low by 8.33 %**, twelve times that. **One site states the approximation and its error;
twenty-two state an identity**, and a reader who meets any of the twenty-two first has no way to know.
The defect is not that 4ν/3 is wrong — it is the equals sign. Which sites take a qualifier is prose.

---

## Phase 0 ruling 3's evidence — why the nine sections are empty

M, 7 September 2026: *"why are they empty?"* — `emptysections.py`, selftest 9 of 9.

**They were never written.** Measured against `PP_The_Method_1_6.md`, md5 `49900cf41f818ab789bb90fc596ac977`
— the Prints & Proofs original-input witness under Ruling 56 — **all nine are empty there too**, and empty in
every archived build from BUILD9 to BUILD90, and consecutive on one page of the pressed PDF's contents,
which is what consecutive empty headings look like when they are typeset.

**Six of the nine were already measured and recorded.** `recovered/DEF-95B.md` (chat 95B):
*"§14.5.2–§14.5.7 are an **authoring gap, not a production loss** … the text never existed at the input, so
no print carries it. **Do not re-derive this and do not search for an earlier print.**"* This extends that
reading to §2.22, §28.7.6 and §28.9.

| section | witness | body | live | body | citations |
|---|---|---|---|---|---|
| §2.22 | L1154 | 0 | L1148 | 0 | 5 — main 4, Register 1 |
| §14.5.2 | L3764 | 0 | L3803 | 0 | 4 — Register 3, Maths 1 |
| §14.5.3 | L3766 | 0 | L3805 | 0 | 1 — main |
| §14.5.4 | L3768 | 0 | L3807 | 0 | 4 — Register 1, Maths 3 |
| §14.5.5 | L3770 | 0 | L3809 | 0 | 4 — Maths 4 |
| §14.5.6 | L3772 | 0 | L3811 | 0 | 3 — main 2, IoI 1 |
| **§14.5.7** | L3774 | 0 | L3813 | 0 | **23 — main 11, Register 8, Maths 4** |
| §28.7.6 | L7600 | 0 | L7682 | 0 | 2 — main |
| §28.9 | L7694 | 0 | L7777 | 0 | 5 — main 2, Register 2, Maths 1 |

**Fifty-one citations across the volumes resolve to a heading with nothing under it**, and the surrounding
prose speaks of what they say: §14.5.8 opens *"§14.5.7 measures the seed on scattered shapes"* and §14.5.9
opens *"Everything §14.5.7 and §14.5.8 report about seed SIZES came from one heuristic"*. **§14.5.7 alone
carries 23 citations, eight of them from the Register** — and Register entries are append-only, so that
section has to be written to what those eight already say, not the other way round. That is chat 95B's
order-of-work point and it still holds.


### And M's second reading overturns the first answer's conclusion

M, on being told they were never written: *"this is because the citations moved but the pointers did
not."* **That is right, and it changes the repair from authoring to re-pointing.**

Being never-written is true and is measured above. It is not the whole answer, and by itself it produced
chat 95B's conclusion — *"the repair is authoring six sections, and it is R3's largest single item."*
**The material those fifty-one citations want is in the book, under other numbers.**

| what a citation says the empty section contains | where it actually is |
|---|---|
| *"§14.5.7 says G is a seed iff φ̂(G) = φ̂(X)"* — quoted by §14.5.9 itself | **§14.5.9** |
| *"§14.5.7 records that zero cells are forced"* | **§14.5.10, §14.5.11, §14.5.12** |
| the seed as a covering problem | **§14.5.8, §14.5.9, §21.5.4** |
| Λ's seed is seven cells for 976 | **§14.5.1, §14.5.9, §14.5.13, §14.6.1, §21.5.4** |
| §14.5.5's ℛ₄ and its four orientations | **§14.6.3, §21.5.3, §21.5.5** |
| §14.5.4's *"what E measures, exactly"* | **§9.2, §18.4.1, §21.2, §21.5.2** |

**§28.9 is not a gap at all** — it is a parent heading with a child, §28.9.1. **And §28.7.6's material was
moved by a repair the volume describes in its own words**: its eighty-six entries were prepended into it
over time, the repair sent them to §28.7.7, and the volume says §28.7.6 *"is now four — the tower's three,
which repairs their numbering"*. **It is zero.** The move happened; the four were never put back.

**Two attributions have no home in the main volume, and that is the exception that has to be said.**
*"anti-exchange"* and *"NP-hard"* occur **nowhere** in it, and both are cited to §14.5.7 from the
Mathematical Compendium. The NP-hardness is seated at register 2071.

**So Phase 0 ruling 3 is not the item only M can do.** Fifty-one citations name a heading with nothing
under it while the material they want sits in the book under other numbers — which is Phase 3's pointer
class, and the plan already names it exactly: *"targets that say nothing of the claim"*. **Chat 95B
measured the emptiness correctly and drew the wrong conclusion, because it asked where the TEXT was and
not where the MATERIAL was.** `emptysections.py`, selftest 17 of 17.

### D-23 · §24.13's end rule against its own table — `endrule.py`, selftest 11 of 11

§24.13 measures both ends of two isoelectronic sequences by holding each member out, and prints:

| held out | lithium-like | sodium-like |
|---|---|---|
| **neutral, Z = 1** | **11.1 %** | **23.4 %** |
| Z = 2 | 1.4 % | 2.4 % |
| Z = 3 | 0.8 % | 1.3 % |
| **Z = 4** — the other end | **1.8 %** | **2.5 %** |

Its prose is exact — *"Extrapolation **to the neutral** does not"* — and Figure 24.3's caption is
exact — *"**The neutral** is not."* **Its summary row and its closing blockquote are not**:
*"within a sequence, **at an end** | δ not determined"* and *"**The ends always must** [be fetched]"*.

**A sequence has two ends, the table measures both, and only one fails.** The neutral end is
**6.2× and 9.4×** worse than the upper end; the upper end sits **inside the interior's own worst
case** on the sodium-like sequence (1.04×) and within a quarter of it on the lithium-like (1.29×).
The correct statement and the overstatement sit on one page, neither superseding the other, and the
two that must not be touched are named.

### D-16 · "K I nd 45.7" — `nreached.py`, selftest 10 of 10

Docket 14's own instruction is *"Resolve K I nd 45.7 first"*, and the collection resolves it.

| channel | printed *"ν reached"* | Spectra Compendium n range | Spectra Compendium ν range |
|---|---|---|---|
| **K I nd** | **45.7** | 3–13 | 2.9–12.7 |
| Na I ns | 20.0 | 3–**20** | 1.6–18.7 |
| Al I nf | 55.0 | 4–**55** | 4.0–**55.0** |

**The other two rows fix the reading.** Al I nf matches both; **Na I ns matches the n range and not
the ν range**, so the column is the top of the principal-quantum-number range. **K I nd's own row
runs n = 3 to 13**, so the entry should be 13 — or 12.7 under the other reading. **Neither is 45.7,
which is 3.5× the larger of them.**

**And the claim the table supports survives, strengthened.** *"Curvature washes out before separation,
in every channel in this work"*: a channel reaching 13 is **further** from its ν_V of 160 than one
reaching 45.7. The figure is wrong, not the thesis.

### I-021 · §11.7 and §11.8's biconditional — `palindromic.py`, selftest 11 of 11

**Chapters 8–11 carry six biconditional claims.** Five are definitions, metric axioms or
characterisations the volume proves. **One is false in one direction, and it is stated twice** — in
Figure 11.2's caption and again as §11.8's opening line:

> *"A rank polynomial is palindromic **if and only if** the poset is self-dual."*

**Self-dual ⟹ palindromic is true** and immediate: an anti-automorphism sends rank r to rank M − r.
**Palindromic ⟹ self-dual is false**, and the counterexample is six elements, found by exhaustive
search over strictly graded posets and printed so it can be checked by hand: relations
0 < 1, 0 < 2, 0 < 3, 4 < 1, 5 < 2, level sizes **(3, 3)** — palindromic — and **not self-dual**,
because element 0 has three above it and nothing in the poset has three below it.

**And the book's argument is sound**, which is why this is a wording defect and not a result defect.
§11.8 uses the claim one way only: the rank sequence is asymmetric — 1, 5, 15, 34, 59, 87 forwards
against 1, 4, 10, 21, 37, 57 backwards — **therefore not self-dual**, which is the *contrapositive of
the direction that holds*. **What does not stand is "if and only if", and with it §11.8's "they are
the same statement"**: an asymmetric rank sequence *implies* non-self-duality and is not equivalent
to it.
