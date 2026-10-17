# `tools/atomicweights.py` — standard atomic weights and isotopic compositions

The site's builder and gravity modes refused a mass whenever no isotope was typed: "water", "iron"
and "glucose" all came back `mass: refused`. The repository held one nuclear table, AME2020 Table I,
which gives every nuclide's mass and says nothing about which nuclides nature mixes. This instrument
captures the two tables that do, both from the IUPAC Commission on Isotopic Abundances and Atomic
Weights (CIAAW), into `tables/ciaaw/`:

| file | rows | what |
| --- | --- | --- |
| `STANDARD-ATOMIC-WEIGHTS.tsv` | 84 | the standard atomic weights: a value with its uncertainty, or, for the 14 elements whose terrestrial composition varies, an interval beside its abridged value |
| `ISOTOPIC-COMPOSITIONS.tsv` | 289 | the representative isotopic compositions, or the interval where CIAAW prints only that |
| `CAPTURE.tsv` | — | the route, the hashes, the citations and the revisions applied |

```
python3 tools/atomicweights.py               # download the pinned wheel, write tables/ciaaw/
python3 tools/atomicweights.py --wheel PATH  # the same from a wheel already on disk
python3 tools/atomicweights.py --verify      # the tables on disk are what the wheel gives
python3 tools/atomicweights.py --selftest    # the tables against CIAAW's own figures (15 checks)
```

## Edition and route

**Edition.** These are the Atomic Weights 2021 report's tables (T. Prohaska et al., Pure Appl. Chem.
94, 573 (2022), doi:10.1515/pac-2019-0603), with the Commission's 2024 revisions of zirconium,
gadolinium and lutetium. That is what ciaaw.org prints today; the page says so, and names those three
as the 2024 revisions.

**Route.** ciaaw.org, iupac.org, the publisher and NIST's equivalent table (SRD 144) are all refused
by this environment's proxy. PyPI is not. The `periodictable` 2.1.0 wheel carries both 2021 tables as
text in its `mass.py`, taken from ciaaw.org on 2023-07-06. The instrument downloads the wheel, checks
it against the sha256 PyPI publishes (`e9155d2b…`), and reads the two tables as text without importing
anything from the package. The three 2024 rows are quoted in the instrument from ciaaw.org as read on
2026-10-17 through an outside fetch.

Rows checked against the live pages agree with the wheel's text, digit for digit: the weights of H,
Li, B, C, N, O, Mg, Si, S, Cl, Ar, Fe, Br, Tl, Pb, Th, Pa and U, and the compositions of Fe, He, Li,
B, C, N and Ar. The only differences are the three 2024 revisions.

**Where the wheel's text departs from CIAAW, it is not followed.** For nitrogen, argon and lead, the
text adds a composition of its own beside CIAAW's interval: air for nitrogen and argon, the 2013 table
for lead. CIAAW prints the interval only, so the interval is what is captured, and `CAPTURE.tsv` names
the three.

## What the site does with them

`tools/webindex.py` carries both tables in `data/nuclides.js`, with each file's md5, the route and the
citations, and records the fixtures the browser selftest holds them to.

- **An element written without its isotope is its most abundant one.** The isotope is chosen by the
  representative composition; where CIAAW prints only an interval, its midpoint is used, marked
  `DERIVED`. The exact mass then comes from AME2020. The row says the isotope was chosen, gives its
  share, and the mass carries `DERIVED`, because the choice is a rule and not a reading. "Fe" is
  ⁵⁶Fe, 91.754 %. "Water" is ¹H₂¹⁶O, 18.010565 u.
- **The molar mass of the natural substance** is the sum of the standard atomic weights, kept to the
  decimals of the least precise of them, with the sum of their uncertainties. Water is
  18.015 g/mol. Glucose is 180.156 g/mol. An ion has q·mₑ subtracted, so Fe³⁺ is 55.843.
- **An element with no standard atomic weight is refused, not invented.** These have no stable isotope
  and no characteristic terrestrial composition: Tc, Pm, Po to Ac, Np and beyond (Bi, Th, Pa and U
  carry one). Such an element has neither a molar mass nor a chosen isotope; typing one (Tc-99) gives
  its exact mass.

## What it refuses

- It never imports the package. The wheel is read as a zip and its `mass.py` as text.
- It never follows the transcription where it departs from CIAAW (N, Ar, Pb).
- It writes no value CIAAW does not print, except the midpoint of an interval, which carries
  `DERIVED` in its own column.
- The tables are generated: regenerate them, never hand-edit. `--verify` exits 1 if a file on disk is
  not what the pinned wheel and the quoted revisions give.
