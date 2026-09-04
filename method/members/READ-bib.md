# READ-bib.md — R3 (chat 153-R) — the two census bodies carried open since chat 151-B, taken: mc 387–672 and mc 293

Instrument `r2-bib.py`, golden `r2-bib.out`. ALL INTEGRITY CHECKS OK, one deviation recorded. Reads the six volumes
and DEFECT-CENSUS.tsv as members. Line numbers are MEMBER line numbers, measured this session, never carried.
DEF-152 item 10 carried both bodies forward unchanged as *computable work needing no ruling*; this is the
computation.

## mc 387–672 — the bibliography table's `objects` column (286 C13-HANDLE-LEAK rows)

The Mathematical Compendium's bibliography (`| year | work | objects |`, 162 data rows, as the volume states)
prints beside each work the handles of the objects that rest on it. The census flags every handle in that column
as a leak; chat 151-B engaged the rows and did not close them, and the question no one had computed is whether a
handle printed there RESOLVES — to an object the compendium states under that name, or to any site in another
volume.

- **The column prints 265 handles; the census pattern admits 179 of them** (it takes 3–6 lowercase letters after
  the dot, so `A.E`, `A.R`, `L.E0` and `S.bounds` are outside it). Every one of the 286 census items is an object
  handle in one of eighteen families — none is a BUILD, chat, W or MC token.
- **The compendium states none of its handles as an object's own name anywhere outside the table.** Six appear
  elsewhere in it — `A.staircls`, `C.Aq`, `E.nuclide`, `L.F`, `M.C1`, `M.C2` — and each of those only as a
  reference inside another entry's text. No entry heading carries its handle; no glossary maps handle to object.
- **122 resolve only in another volume** — the Register (105 handles) and the main volume (57), Appendix G's
  *what rests on it* column among the sites — **and 137 resolve nowhere.** Of the census's 179, 86 resolve only
  outside the compendium and 93 nowhere; 133 of the 286 rows carry a handle that resolves nowhere.
- **The map from handle to object is `mathreg.py`'s, and `mathreg.py` is not a member.** The generator names the
  objects; the volume it generates prints the names and never says what they name.

**Verdict: DEFECT, one class at one site, closed on all 286 rows together** — deviation bib-01, *a reader can
follow every handle in the column to an object the volume states*, measured False. Docket 28 / ruling 46 with
precedent 1546 for the handle in a reader-facing volume; docket 38 for the instrument that is not held. Recorded,
not repaired: the repair is the generator's — each handle printed beside the object it names — and the generator
is not a member.

## mc 293 — the modular ledger's eleven numerals (C6-NUMBERS-NOT-IN-SOURCE)

Reproduced under census.py's own extraction rule (years and one- and two-digit figures excluded, a trailing comma
kept on `1019,`), the block carries eleven numerals and nine are absent from the six entries it cites. Read, the
nine are: **four Register pointers** — 1019, 1035, 1483, 1484, the block's own citations, which an entry does not
print inside its own body — and **five journal locators** of the block's prior-art line — Borchers, *Commun. Math.
Phys.* 143 (1992) 315–332; Wiesbrock, *Lett. Math. Phys.* 28 (1993) 107–114. The two *in source* are 1020 and
1022, because 1483 and 1484 name them. The class asks for a figure the block states about its object that its
sources do not carry, and there is none.

**Verdict: NOT A DEFECT.** Carried open from the 27a unit, which took the block's citation list and not its
numerals; closed here on the numerals.

## Census

`CENSUS-CLOSURES-d152.tsv` carries the 287 rows: 293 not a defect, 387–672 defect, each reason citing the
instrument's section.
