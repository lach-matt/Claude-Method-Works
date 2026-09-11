# `tools/sites.py` — the site terms, scored

**Why it exists.** What survives the register is site-specific: reservoir head, seismic basis,
outfall and intake, permitting. None can be computed without a site. This file does the thing
that can be done without one: it states the term each Title needs of a site, grades the three
Title I nodes and eight retired or retiring coastal plants on each term from the public record —
**MET**, **CONDITIONAL** (clears on an assumption the site study confirms), **OPEN**, **FAIL** — and
ranks them. **The rank orders the site studies; it does not choose a site.** Every site value is
ASSUMED from the public record unless an instrument holds it, and the note beside each grade says
which. DNI comes from `helios.py`, the seismic margin from `minors.py`, the head band from
`joinder.py`, the brownfield band from `titletwo.py`.

**Run it.** `python3 tools/sites.py` (`--selftest`). Stdlib only.

## Title I: six terms

DNI at or above 2,500 kWh/m²/yr; a contiguous disturbed parcel; no federal nexus; a seismic margin of
1.5× design over mapped; a 500 kV substation within one gen-tie; 500 m of head within reach for the
water route.

| node | mid | critical | first study |
|---|---|---|---|
| Central Valley (Westside) | 5.0 | 4.5 | one year of on-site DNI |
| Mojave (Kramer Junction) | 5.0 | 5.0 | title search and fallowing agreement |
| Imperial (Desert Center) | 4.5 | 4.5 | title search and fallowing agreement |

At mid the Westside ties the Mojave for first: it meets land, nexus and grid outright and is
conditional on DNI and head, so the node the record doubted for its sun has the fewest open terms,
which is why `majors.py` kept it. At critical the Mojave leads alone, because the Westside's seismic
margin (0.75 g over a mapped 0.55 g, 1.36×) falls under the 1.5× a site study must confirm.

## Title II: seven terms

An outfall the brine can use at Ocean Plan dilution; an intake channel to reuse; 50–80 acres; takers
within reach; 500 m of head within reach; a Coastal Commission record that does not foreclose the
site; a stated seismic and tsunami basis.

| site | score | first study |
|---|---|---|
| Mandalay (Oxnard) | 6.0 | Coastal Development Permit pre-application |
| Ormond Beach (Oxnard) | 6.0 | Coastal Development Permit pre-application |
| Morro Bay | 5.5 | recharge district contract |
| Moss Landing (Monterey) | 5.5 | reservoir siting study |
| Alamitos / Long Beach | 5.0 | site survey and remediation scope |
| Scattergood / El Segundo | 5.0 | site survey and remediation scope |
| South Bay (Chula Vista) | 5.0 | outfall diffuser hydraulic study |
| Huntington Beach (AES) | 4.0 | Coastal Development Permit pre-application |

Encina (Carlsbad) is excluded rather than scored: it already hosts the plant `aquacost.py` prices
from. **Huntington Beach carries the 2022 denial as a FAIL** on its permit term and is not a first
site. The Oxnard plain and Moss Landing meet the taker and head terms the water route needs, because
each sits beside a critically overdrafted basin with mountains behind it.

## What it says and does not say

- The adopted route (`both.py`) needs 16–18 modules and this list holds eight sites: two to three
  modules per site, or sites the list does not name. The count is a finding, not a plan.
- No Title II site is MET on every term, and the selftest asserts it: a site study is always owed.
- Nothing here is a site decision. Each row's first study is what would make it one, and the
  ranking says which study to fund first.
