# `tables/ciaaw/` — standard atomic weights and isotopic compositions

The IUPAC Commission on Isotopic Abundances and Atomic Weights' (CIAAW) two tables, captured by
`tools/atomicweights.py` so that the site's builder and gravity modes can give a mass when no
isotope is typed. Before this, the repository held only AME2020 Table I, which gives every nuclide's
mass and nothing about which nuclides nature mixes, so water and iron had no mass at all.

| file | what it holds |
| --- | --- |
| `STANDARD-ATOMIC-WEIGHTS.tsv` | 84 elements: a value with its uncertainty, or, for the 14 elements whose terrestrial composition varies, CIAAW's interval [low, high] beside its abridged value |
| `ISOTOPIC-COMPOSITIONS.tsv` | 289 isotopes: the representative composition CIAAW prints, or its interval; an interval's midpoint is the `representative`, marked `DERIVED` |
| `CAPTURE.tsv` | the route: the PyPI wheel and its sha256, the member file's md5, the citations, the revisions applied |

**Edition.** These are the Atomic Weights 2021 report's tables (T. Prohaska et al., Pure Appl. Chem. 94,
573 (2022), doi:10.1515/pac-2019-0603), with CIAAW's 2024 revisions of zirconium, gadolinium and
lutetium. That is what ciaaw.org prints today.

**Route.** ciaaw.org, iupac.org and the publisher are refused by this environment's proxy, and PyPI
is not. The `periodictable` 2.1.0 wheel carries both 2021 tables as text, taken from ciaaw.org on
2023-07-06. The instrument downloads it, checks the sha256 PyPI publishes, and reads the text without
importing it. The three 2024 rows are quoted from ciaaw.org as read on 2026-10-17. Every other row
checked against the live pages agrees with the wheel's text: H, Li, B, C, N, O, Mg, Si, S, Cl, Ar, Fe,
Br, Tl, Pb, Th, Pa, U, and Fe's composition.

**Where the wheel's text departs from CIAAW, it is not followed.** For nitrogen, argon and lead, the
text adds a composition of its own beside CIAAW's interval: air for nitrogen and argon, the 2013 table
for lead. CIAAW prints the interval only, so the interval is what is captured.

**Status.** Every figure is `READ`, except a representative value derived from an interval, which is
`DERIVED`. The tables are generated: regenerate with `python3 tools/atomicweights.py`, never hand-edit.
`--verify` checks the files against the wheel, and `--selftest` checks them against CIAAW's own
printed figures and against AME2020. See `docs/ATOMIC-WEIGHTS.md`.
