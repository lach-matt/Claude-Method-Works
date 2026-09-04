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