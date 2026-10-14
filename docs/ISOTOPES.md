# The isotope index — `tools/isotopes.py`

*Every nuclide of the one nuclear table the repository holds, charted on its proton number and its
neutron number. An index of this site, built and measured by its own instrument; not a row of the
research tree's register, and it says so wherever it is shown.*

## What it is

The repository holds exactly one nuclear table: AME2020 Table I, the published atomic mass table,
captured at `extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv` from the PDF and
md5-pinned in `extracted/LEDGER.tsv` (`9540ebcd…`). It holds no NUBASE table and no nuclide level
table, so no spin, parity or half-life is READ anywhere here. `tools/isotopes.py` charts what that
one table gives and nothing else:

| coordinate | meaning | status |
|---|---|---|
| Z | the proton number, the element | READ |
| N | the neutron number | READ |

Every row of the table is a member, the neutron (0, 1) included — **3,558 members on 3,558 cells**,
an injective chart. Everything else the table carries rides on the member and is refused as a
coordinate, each refusal against a measurement (below).

## The cell, measured twice

On two coordinates the containment order is the product order on (Z, N), so the instrument measures
the cell exactly, without the general machinery:

- **height 295** — the longest chain. Sorted by (Z, N), two members are comparable exactly when N
  does not fall, so a chain is a non-decreasing run of N and the height is the longest such run, by
  patience sorting. The witness runs from (1, 0) to (118, 177).
- **width 18** — the largest antichain. Two members are incomparable exactly when Z rises and N
  strictly falls, so an antichain takes one member per Z with N strictly decreasing. The witness is
  the eighteen nuclides (63, 107), (64, 106), …, (80, 90): one isotope each of europium through
  mercury along an anti-diagonal of the chart.
- **E = 0** — the join-closure deficit. For every two members the cell (max Z, max N) is held, so
  the chart of nuclides is join-closed, the index demands nothing and draws no ghost. Computed by
  two routes (a per-Z sweep and the pairwise closure) and asserted equal.

The channel is **not** computed by the instrument: it needs the five closure operators of the
hierarchy law, which are the research tree's instruments and are imported by the site build
(`tools/webindex.py`, `_isotopes`), never copied. At build they return **K4, cell (4, 295, 18)**,
closed by information and statistics, with closure sizes order 3,560, algebra 3,560, geometry 3,962,
information 3,558, statistics 3,558; the build asserts that their height and width equal the
instrument's and that the information closure's deficit equals the instrument's E. The
meet-closure (the other corner, (min Z, min N)) asks for two cells, the empty nucleus (0, 0) and the
diproton (2, 0) — which is exactly what the order and algebra closures add. That is recorded as a
measurement of the chart's shape, not as a language's closure.

## What rides on each member

All DERIVED from the table alone, with one named constant:

- **mass in u**: M = A + Δ / (u c²), with u c² = 931 494.10242 keV (CODATA 2018, the value the
  evaluation itself uses) — the one EMPIRICAL constant. Carbon 12 reconstructs to 12 u exactly.
- **binding energy**: B = Z Δ(¹H) + N Δ(n) − Δ(Z, N), in keV over atomic mass excesses, so the
  electrons cancel exactly. The neutron and the proton bind to zero; ⁶²Ni is the most bound at
  8,794.555 keV per nucleon on the rounded table's own rows (the evaluation's unrounded file gives
  8,794.553; the capture's header records that it is the published rounded table).
- **separation energies** S_n, S_p, S_2n, S_2p: differences of B with the neighbour where the
  table holds it, and None where it does not — S_n on 119 members, S_p on 179. A negative value is
  the table's own (27 and 211 of them) and not a finding.
- the mass excess with its uncertainty and its **quality flag**, 2,550 measured and 1,008 estimated,
  carried at the status the table gives it and never flattened.

## The refusals

| candidate | verdict | measurement |
|---|---|---|
| A, the mass number | REFUSED | A = Z + N on 3,558 of 3,558 rows; the chart on (Z, N, A) has the same height and width, 295 and 18 |
| T_z = (N − Z)/2 | REFUSED | a function of the two; charted anyway at height 178, width 31 — the order changes, but no two members are separated that (Z, N) does not already separate |
| the mass excess Δ | REFUSED | a signed magnitude in keV; 3,481 distinct values on 3,558 rows |
| the quality flag | REFUSED | provenance of the value, not a property of the nuclide; charted anyway at height 295, width 22 |
| B and B/A | REFUSED | derived from three of the table's own entries, a magnitude |
| S_n, S_p and their signs | REFUSED | magnitudes, and not total: undefined on 119 and 179 |
| spin, parity, half-life | NOT HELD | no NUBASE table in the repository; a seated one would be a new index beside this, not a coordinate added to it |

## On the site

`tools/webindex.py` carries the block as `isotopes` in `data/particles.js`: the rows with their
extras, the cell measured both ways, the closure sizes, the demand, the witnesses, the census, the
refusals, the formulas and the constant, and the source with its measured and recorded md5. The
explorer draws it as its eleventh index (N across, Z up, coloured by the quality flag); a member's
plate carries every derived figure and opens the same nuclide in the gravity index and in the
gravity mode. The Indexes dialog places it after the tenth index, labelled *an index of this site*.
The site's selftest pins every figure above, and `tools/docfigures.py` pins the summary against
`data/index.js` and the instrument's own `--json`.

## Running it

```
python3 tools/isotopes.py                 # the report (4 s)
python3 tools/isotopes.py --selftest      # the table's census, its ledger md5, the exact cell, the witnesses
python3 tools/isotopes.py --charts        # also the three refused charts, by the generic-arity functions (about 25 s)
python3 tools/isotopes.py --member 56Fe   # one record: 56Fe, Fe-56, Fe56 or ^56Fe
python3 tools/isotopes.py --json          # the whole block
```

The selftest also checks the generic height and width (the O(n²) chain and the Dilworth matching
used for the refused charts) against the exact 2-D functions on the Z ≤ 12 sub-chart, so a refusal
is measured by a checked tool.

## What it is not

It is not a nuclide chart with physics on it: no drip line, no magic number, no stability is
inferred from the table, and the valley of stability is not drawn, because the table carries masses
and their provenance and nothing else. It is not a register row: the research tree's registry seats
its own indexes by its own procedure, and this one was built here from the site's data. It does not
read the exact-forms export or any instrument of the research tree; it reads one TSV.
