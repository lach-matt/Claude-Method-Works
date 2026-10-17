# `tables/nist-levels/` — the neutral energy levels behind 25 rows of the spectra index

Nine listings from the NIST Atomic Spectra Database (ASD), cut to the rows `tools/seriesdefect.py`
needs to recompute the 25 rows of COORDINATES-2.13 whose `B` column is not an integer. Those rows
come from one NIST fetch (2026-08-14). Each prints a median quantum defect, a float in place of the
Pauli bound, and a series limit with no unit. Recomputed from these levels, all 25 resolve exactly:
the limit is NIST's neutral ionisation energy in cm⁻¹, `delta` is the median of the series' quantum
defects, and `B` is their **range** (max − min). See `docs/CAVEATS.md`.

| file | spectrum | rows kept | md5 |
| --- | --- | --- | --- |
| `BI_levels.csv` | B I | 81 + limit | `7717942cc640c6d30f74496a18344a58` |
| `NaI_levels.csv` | Na I | 139 + limit | `6ad4febdb938533c84e15cd8b8763aac` |
| `AlI_levels.csv` | Al I | 22 + limit | `801e0a6a8d546929bbe9115fbca73cf2` |
| `GaI_levels.csv` | Ga I | 60 + limit | `a06819cd53bb9c0507acb77f093e3b41` |
| `InI_levels.csv` | In I | 16 + limit | `93438efc1af42b05b9deb601009319c9` |
| `CsI_levels.csv` | Cs I | 174 + limit | `a7cf208ea3068ef65ac78fe41e2233e1` |
| `LuI_levels.csv` | Lu I | 61 + limit | `9cab8c1893589723168b3b5ad437b766` |
| `TlI_levels.csv` | Tl I | 42 + limit | `8c65923776228901aa18e1e26525db45` |
| `FrI_levels.csv` | Fr I | 72 + limit | `261b4204c6971fdedc86b1f9930f602c` |

The first line of each file is NIST's CSV header and the second a `#` comment saying which rows were
kept. The levels are in cm⁻¹, and the prefixes, suffixes and uncertainties are as NIST printed them.

**Route.** This environment's proxy refuses physics.nist.gov, so the listings were fetched on
2026-10-17 through a web-fetch connector from ASD's energy-levels service in CSV form, one spectrum at
a time:

```
https://physics.nist.gov/cgi-bin/ASD/energy1.pl?de=0&spectrum=Na+I&units=0&format=2&output=0
  &page_size=15&multiplet_ordered=0&conf_out=on&term_out=on&level_out=on&unc_out=1&j_out=on
  &biblio=on&temp=
```

`units=0` is cm⁻¹. NIST's CSV wraps every field as `="…"`; that wrapping is removed and nothing else
is changed. Each file keeps the single-valence rows below the first limit (no parenthesised parent
term), which are the only rows a one-electron series can be drawn from, and that limit row. The nine
limit rows are the ionisation energies NIST's ionisation-energy service (`ie.pl`) returned the same
day; `tools/seriesdefect.py` holds those as `NIST_IE_CM1`, and its selftest checks each against the
limit COORDINATES-2.13 prints.

**Status.** `READ`. The capture is not regenerable here, because the proxy refuses the host. Never
hand-edit these files: re-fetch through a route that reaches NIST, and record the new md5s above.
`python3 tools/seriesdefect.py --selftest` checks the identity on all 25 rows. It also runs a negative
control: boron's ²P° row fails when ¹¹B's mass replaces the standard atomic weight, the mass convention
the source evidently used.
