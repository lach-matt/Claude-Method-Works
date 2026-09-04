# WHAT IS LEFT — the spectra collection

## Collected · 3 species · 77 levels

  Ne I    33 levels   ref SS04   limit 173,929.75 cm-1
  Ne II   28 levels   ref P71    limit 330,388.6
  Be I    16 levels   ref KM97   limit 75,192.64   (ionization 9.32270 eV)

---

## Reachable on this route · 26 species · 15 elements

**Two per element where both stages are wanted. Fetch cost: three requests per element —
`element_name.htm`, then `[element]table1.htm`, then `table5.htm` and/or `table6.htm`.**

  element      wanted           pages
  Argon        Ar II            argontable6
  Beryllium    Be II            berylliumtable6          ← element already opened once
  Carbon       C II             carbontable6
  Calcium      Ca II            calciumtable6
  Cadmium      Cd II            cadmiumtable6
  Copper       Cu II            coppertable6
  Gallium      Ga I             galliumtable5
  Mercury      Hg II            mercurytable6
  Potassium    K II             potassiumtable6
  Krypton      Kr I             kryptontable5
  Lithium      Li I             lithiumtable5
  Magnesium    Mg II            magnesiumtable6
  Nitrogen     N II             nitrogentable6
  Sodium       Na II            sodiumtable6
  Phosphorus   P II             phosphorustable6
  Silicon      Si I, Si II      silicontable5, silicontable6
  Strontium    Sr I             strontiumtable5
  Barium       Ba I, Ba II      bariumtable5, bariumtable6
  Titanium     Ti I             titaniumtable5
  Bismuth      Bi I             bismuthtable5
  Zinc         Zn I, Zn II      zinctable5, zinctable6

**26 species across 21 elements.** At three fetches per element and roughly 8 KB each,
**about 500 KB of context** — six to eight elements per session, so **three sessions.**

---

## NOT reachable on this route · 6 species

  Li III · Sc III · Sc VI · Ba III · Bi II · Bi III

**The Handbook carries neutral and singly ionised only.** These need the ASD query
interface, which is robots-disallowed on every mirror tried, or a compilation paper per
species.

---

## What no amount of collecting will supply

**`B.adm` needs σ — level uncertainties — and the Handbook prints none.** Every species
above can be collected and that object stays open. *It needs the ASD levels output with
`Level Uncertainty` ticked, which is the interface that is closed.*

---

## Three findings from the retrieval, which are the durable part

**1 · The obvious route is the closed one.** The ASD query interface is disallowed on
`physics.nist.gov`, `www.physics.nist.gov` and `pmlg.nist.gov`; on `pml.nist.gov` it
answers but the fetcher normalises every request back to whichever URL a search returned,
so the `spectrum` parameter cannot be varied. **The Handbook — a static index of the same
data, with no search box — is open.**

**2 · The cheap language exists and cannot be reached.** Every table has an ASCII variant
at a fraction of the size, linked as `[![Switch to ASCII Version](gif)](url)`. **The
fetcher does not record image-wrapped links**, so the variant returns PERMISSIONS_ERROR.
And `text_content_token_limit` did not truncate when passed. *§19.5.1's law, turned on the
searcher: this document has a cheap route that this reader cannot open.*

**3 · The URL index is recency-limited.** `element_name.htm` surfaces all 100 elements'
`table1` links, and they expire within a few fetches. **So the index page must be
re-fetched immediately before each element** — which is why the cost is three requests per
element rather than two, and why a batch cannot be planned ahead.
