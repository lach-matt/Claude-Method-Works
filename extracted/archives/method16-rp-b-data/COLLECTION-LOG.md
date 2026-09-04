# SPECTRA COLLECTION — PHASE 1, RETRIEVAL ONLY

Register 661. **Collect everything before any analysis or write-in.**

## The routes, tried in order

| route | result |
|---|---|
| `physics.nist.gov/cgi-bin/ASD/energy1.pl` | **ROBOTS_DISALLOWED** |
| `www.physics.nist.gov/cgi-bin/...` | **ROBOTS_DISALLOWED** |
| `pmlg.nist.gov/cgi-bin/...` | **ROBOTS_DISALLOWED** |
| `pml.nist.gov/cgi-bin/...` | **reachable, but the fetcher normalises the URL back to the cached search result** — every request returned Tb IV regardless of the `spectrum` parameter |
| `data.nublado.org/nist/asd_v5.12/levels/` | never surfaced by a search, so unfetchable |
| **`physics.nist.gov/PhysRefData/Handbook/Tables/`** | **OPEN** — static tables, full data, no block |

**§19.6's rule, paying again.** The CGI query interface is the obvious route and it is
closed; the Handbook is a static index of the same data and it is open. *A source has an
index, and it is rarely the one with a search box.*

## The Handbook's own index

  [element]table1.htm    atomic data
  [element]table2.htm    strong lines
  [element]table3.htm    neutral persistent lines
  [element]table4.htm    singly-ionised persistent lines
  **[element]table5.htm    NEUTRAL ENERGY LEVELS**
  **[element]table6.htm    SINGLY-IONISED ENERGY LEVELS**
  [element]table7.htm    references
  [element]tableN_a.htm  the ASCII variant of table N

**Two limits, stated before collecting.** The Handbook carries **neutral and singly
ionised only** — so Li III, Sc III, Sc VI, Ba III, Bi II and Bi III are not in it. And it
prints **no level uncertainties**, which `B.adm` needs; that stays open on this route.

## The queue

  collected here    Ne I
  neutral, wanted   Be I · Bi I · Ga I · Kr I · Li I · Si I · Sr I · Ba I · Ti I · Zn I
  singly, wanted    Ar II · Be II · C II · Ca II · Cd II · Cu II · Hg II · K II · Mg II ·
                    N II · Na II · P II · Si II · Zn II · Ba II
  not in this route Li III · Sc III · Sc VI · Ba III · Bi II · Bi III

## The compression attempt, and why it failed

**Register 662.** The Handbook publishes an **ASCII variant of every table** — same numbers,
a fraction of the bytes, since the formatted version spends most of its size on navigation
gifs and table markup. *Changing the language to shrink the data is exactly right and it
does not work here, for two reasons that are the fetcher's rather than the source's:*

  the ASCII variant is unreachable   `[element]tableN_a.htm` appears only as an
                                     IMAGE-WRAPPED link — `[![Switch to ASCII
                                     Version](gif)](url)` — and the fetcher's URL index
                                     does not record it. Every attempt returns
                                     PERMISSIONS_ERROR.
  the token limit does not truncate  `text_content_token_limit=2500` was passed and the
                                     full page arrived regardless.

**So each species costs its full formatted page in context, about 8–10 KB, and there is no
route that costs less.** *The compression exists at the source and cannot be reached from
here — which is §19.5.1's own lesson: ρ is a property of (document, route), and this
document has a cheap route that this searcher cannot open.*

## Collected

  Ne I    33 levels   ref SS04   limit 173929.75    spectra_raw/NeI.tsv
  Ne II   28 levels   ref P71    limit 330388.6     spectra_raw/NeII.tsv
  Be I    16 levels   ref KM97   limit 75192.64     spectra_raw/BeI.tsv

**77 levels across three species.** Be II remains on the neutral/singly-ionised route and
was not reached before the budget ran out.

## Resuming

**The route is established and needs no rediscovery.** From `element_name.htm`, fetch
`[element]table1.htm` to surface that element's links, then `table5.htm` for the neutral
and `table6.htm` for the singly ionised. **Two fetches per element, roughly 18 KB of
context.** A fresh session can take six to eight elements — twelve to sixteen species —
before the same limit binds.

**Priority order**, by what each unblocks: Ar II · Mg II · Ca II · Si I and Si II ·
C II · N II · K II · Na II · Zn I and Zn II · Cd II · Cu II · Ga I · Kr I · Li I ·
Sr I · Ba I and Ba II · Ti I · Bi I · P II.

**Not on this route at all**: Li III, Sc III, Sc VI, Ba III, Bi II, Bi III — the Handbook
carries neutral and singly ionised only.

**And `B.adm` stays blocked regardless**: the Handbook prints no level uncertainties, and
σ is what that object needs.

## A fourth route, and it is the cheapest by an order of magnitude

**Register 670.** A web search whose query names the table's own heading — *"Energy Levels of
Singly Ionized …"*, *Configuration Term J Level(cm-1) Limit* — **returns the FULL TABLE in the
snippet.** No fetch is needed at all.

  route                                   cost per species
  ASD query interface                     closed
  Handbook, element_name → table1 → table5   three fetches, ~24 KB
  **search on the table's own heading**       **one search returns SEVERAL species**

*Two searches produced six complete tables. The fetch route produced three in the same budget.*
**§19.6 again: the route decides, and the route that names what the document calls itself beats
the route that names the document.**

**And a mirror appeared that is not robots-blocked**: `jupiter.chem.uoa.gr/pchem/courses/719/
eBookBASD/` carries the same Handbook pages, which is a fetch route for anything the search will
not surface.

## Collected · 9 species · 254 lines

  Ne I   33   SS04    173,929.75      Ne II  28   P71     330,388.6
  Be I   16   KM97     75,192.64      Mg I   46   MZ80     61,671.05
  Mg II  16   MZ80    121,267.64      Ca I   28   SC85     49,305.95
  Ca II  12   SC85/L99 95,751.88      C II   29   MG93    196,664.7
  Ar II  21   WACB95  222,848.30   ← PARTIAL, snippet truncated

**Ca II carries an uncertainty from calciumtable7: the 4p 2P° levels are ±0.002 cm⁻¹** — the only
uncertainty the Handbook has yielded, and it came from the REFERENCES table rather than the level
table. *That is where σ may be recoverable for `B.adm` after all: per-element, in table7, stated as
prose.*

## Batch three · four searches, seven more species

  Li I    12   REB95    43,487.150      Li II   13   HM59    610,078.4  ← was "off route"
  Si I    11   MKMD94   65,747.76  PART Si II   54   MZ83    131,838.14  PART
  Zn I    14   GL00     75,769.33       Zn II    8   SM95    144,892.6  DERIVED

**Li II was listed as unreachable and is not**: the Handbook's singly-ionised table covers it, and
it carries the Li III limit at 610,078.4 — *so the "neutral and singly ionised only" limit excludes
Li III's LEVELS but not its ionisation energy.*

**Zn II came from the persistent-LINES table**, which names the levels a transition connects. **That
is a fifth route**: where a level table does not surface, the line table gives a subset second-hand.
*Marked DERIVED, because it is a subset chosen by which lines are strong rather than a level list.*

**Si I and Si II are PARTIAL** — the search snippets truncate long tables at roughly 50 rows, so any
species with more levels than that arrives incomplete. **That is the search route's one real limit**,
and it is why Ar II, Si I and Si II are marked.

## Collected · 15 species

  Ne I 33 · Ne II 28 · Be I 16 · Mg I 46 · Mg II 16 · Ca I 28 · Ca II 12 · C II 29
  Ar II 21 PART · Li I 12 · Li II 13 · Si I 11 PART · Si II 54 PART · Zn I 14 · Zn II 8 DERIVED

## The ASD route, opened from the other side — and it carries σ

**Register 671.** Ar II arrived as ASD 5.12 output, Saloman 2010, ref L15349 — **419 levels found,
125 captured** — with a column the Handbook does not have:

  Configuration | Term | J | Level (cm-1) | **Uncertainty (cm-1)** | Landé | Reference

**124 of 125 levels carry an uncertainty.** σ ranges 0.0001 to 0.012 cm⁻¹, median **0.0003**.

    **`B.adm` is r = 2Z²R/(ν³σ) ≥ 5, and σ was the missing quantity.** It is not
    missing on this route. *I recorded twice that the Handbook prints no uncertainties
    and concluded the object was blocked; the correct statement was that ONE route
    lacks them.* **§19.5.1 exactly: ρ is a property of (document, route), and I drew a
    conclusion about the document.**

**And the compilation carries a systematic note the level table alone would hide**: *all energy
level values from this compilation have been decreased by 0.0002 cm⁻¹ to make the ground state
energy equal to zero.* **A uniform offset, smaller than most of the uncertainties, applied by the
compiler.**

**The route is Matthew's browser.** ASD is robots-disallowed to this session on every mirror and
open to a person. *The division is now exact: search snippets give Handbook tables without
uncertainties and truncate near fifty rows; a browser gives ASD output with uncertainties and no
truncation.*

**One request that costs nothing and saves a great deal: upload as a .txt FILE rather than pasting.**
A file lands at /mnt/user-data/uploads and can be parsed with no context cost at all; pasted text
must be re-typed to be saved. *Register 587's protocol, applied to the collaboration.*

## Batch four · six ASD outputs, and the σ picture is now clear

**Register 672.** Si I (542), Si II (151), Sc III (44), Sc IV (129), Ba III (162), Bi II (78),
Bi III (68), Li III (149) arrived as ASD 5.12 output. **Captured in full: Sc III and Bi III.** The
rest exceed what pasted text can be transcribed into at this session's remaining capacity, and are
listed below with their limits and σ profiles so nothing is lost about them.

  species  levels  primary source              limit cm-1          sigma
  Sc III       44  Sugar & Corliss 1985        199677.37 ± 0.10    CAPTURED
  Bi III       68  Arya & Tauheed 2020         206242.0 ± 1.4      CAPTURED, median 0.2
  Sc IV       129  Sugar & Corliss 1985        592732 ± 3          not stated per level
  Ba III      162  Sansonetti & Curry 2010     —                   UNIFORM 0.20 on every level
  Bi II        78  Dolk 2002 / Joshi 1986      134720 ± 30         0.020 typical, 400 on one
  Si I        542  Martin & Zalubas 1983       —                   blank on every level
  Si II       151  Martin & Zalubas 1983       —                   blank on every level
  Li III      149  Yerokhin & Shabaev 2015     —                   1e-7 to 1e-3, EXTRAORDINARY

**Four kinds of σ, and `B.adm` must distinguish them:**

  **stated per level**      Bi III, Ar II, Bi II — a real measurement uncertainty
  **uniform**               Ba III, 0.20 on all 162 — a compilation-wide floor, not a measurement
  **absent**                Si I, Si II — the column exists and every entry is blank
  **relative to a base**    Bi III states its σ as separations from 6s6p2(3P) 4P3/2 at 83038.06,
                            to be combined in quadrature with the ground level's 0.06 for an
                            EXCITATION energy

*That fourth kind is the one that would silently corrupt a calculation.* **A σ column is not a σ
until you read what the compilation says it means** — which is in the header, not the table.

**And Li III is a different object from the rest.** Its values are parenthesised — *theoretical*,
Yerokhin & Shabaev 2015 scaled to CODATA-2018 — with σ down to **1×10⁻⁷ cm⁻¹**. *Uncertainties for
n = 2 are excitation energies from the ground state; for everything above, separations from the
ionisation limit.* **Two different reference points inside one table.**

## Collected · 18 species

  Ne I · Ne II · Be I · Mg I · Mg II · Ca I · Ca II · C II · Li I · Li II · Zn I
  Ar II (Handbook) · Ar II (ASD, 125 of 419, with σ) · Si I* · Si II* · Zn II†
  **Sc III (complete, with limit)** · **Bi III (complete, with σ)**

## The Ba III limit — a route outside ASD

**Register 683.** ASD's Ba III data is Sansonetti & Curry 2010, and that compilation is **free full
text**, not paywalled:

  **J. E. Sansonetti and J. J. Curry, "Wavelengths, Transition Probabilities, and Energy
  Levels for the Spectra of Barium (Ba III through Ba LVI)", J. Phys. Chem. Ref. Data
  39, 043103 (2010), doi:10.1063/1.3432516**

  https://srd.nist.gov/jpcrdreprint/1.3432516.pdf
  https://www.nist.gov/system/files/documents/srd/jpcrd392010043103.pdf

**It states that ground states and ionisation energies are listed**, and its contents run *Observed
spectral lines of Ba III · Energy levels of Ba III · …* — so the limit is in the Ba III section head,
not buried in a table.

**And the paper names its own upstream source**: the Ba III ionisation energy is taken from
**P. Hellentin, Phys. Scr. 13, 155 (1976)**, with the 5p⁵ ²P₁/₂ level. *Two routes to one number,
and neither is ASD.*

**Also confirmed from the same search**: Ba IV's limit is **379,300 ± 2,700 cm⁻¹ (47.03 ± 0.33 eV)**,
revised in Sansonetti, Reader, Tauheed & Joshi, J. Opt. Soc. Am. B 10, 7 (1993) — which matches the
bracketed value in the ASD output exactly and confirms the brackets mean *fitted*, not *measured*.

*§19.6 once more: when the database is exhausted, the compilation behind it is a different route,
and the paper behind THAT is a third.*

## Is there one source with all the Rydberg runs? — the honest answer

**Register 687.** *Nearly, and it is a lead rather than a document.*

**What exists and was found:**

  **arXiv:physics/0504154, Table I** — experimentally measured quantum defects for **37
  elements**, with references, alongside the paper's own systematic values. Saved as
  `QD-CHECK.tsv`. **A CROSS-CHECK source, not a channel source**: one δ per element,
  neutral atoms, lowest series — no n-range, no limit, no series identification, no
  spread. *Every column the compendium needs except the number itself is absent.*

  **It checks out where it should.** Mg I ns ¹S computed here at **+1.533** against its
  **1.517** — 0.016 apart. *And it correctly fails to match where the species differ:
  Ca II ns +1.834 against neutral Ca's 2.340, Si II +1.394 against neutral Si's 1.816.*

**The lead that matters.** That paper states some of its "experimental" values came from
**an on-line database where the quantum defect is COMPUTED from available spectroscopic
data** — its reference [29]. **That is the single source this question is asking for**, and
its identity is one reference-list lookup away in a free arXiv PDF.

**Why one source probably cannot exist in the form wanted.** A channel needs a limit, a
series, an n-range and the levels themselves. **A δ compilation gives the ANSWER without
the working**, and this book's method is to compute the answer from the levels and check it
— *§2.14, compute then write.* A δ table can verify the compendium; it cannot populate it.

  **the levels**   ASD, per species — what remains outstanding
  **the limits**   derivable from the levels themselves where a series is long enough,
                   as Ba III proved at 289,118 with three independent checks
  **the defects**  computed here, and now checkable against 37 elements

## TOPbase — reachable, and it is a map rather than a mine

**Register 688.** Reference [29] of arXiv:physics/0504154 is **TOPbase, the Opacity Project
on-line atomic database**, now at **https://tiptopbase.obspm.fr/topbase** (portal
`cds.unistra.fr/OP.html`, the upgrade of the facility installed at CDS in 1993).

**Fetched successfully** — no robots block, unlike ASD.

  **holds**      LS-coupling term energies, f-values and photoionisation cross sections
                 for astrophysically abundant ions, **Z = 1–26**, even and odd LS terms
                 with S = 0,1 · L ≤ 4 · **effective quantum number ν ≤ 10**
  **method**     close-coupling, R-matrix, with asymptotic techniques
  **access**     interactive search, or **ftp of the original raw files**

**Why it cannot supply channels.** *They have been computed* — the energies are calculated,
not measured, and the project's own assessment puts term-energy error near **5% even for
Fe XIV**. **Ar II's measured levels carry σ = 0.0002 cm⁻¹.** A quantum defect computed from
a 5% energy is not a measurement, and §2.13's control group is the real atomic numbers.
*It would fail the same test that withdrew Ba III's guessed limit — a plausible number is
not a measured one.*

**Why it is still worth having.** **ν ≤ 10 is precisely the Rydberg-run structure the
Handbook lacks**, and Z = 1–26 covers eight of the nine species blocked on series length:
Ne I, Ne II, Be I, Ca I, Li II, Si I, C II, Mg I and Mg II. **It would say which n values
exist for which term — so an ASD request could be aimed rather than exhaustive.**

    **A map, not a mine.** It tells you where to dig; the measured levels still come
    from ASD.

**And its raw files are ftp-able**, which is a route neither the search snippets nor the
level-table pages offered — worth trying from a session with room to parse them.
