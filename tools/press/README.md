# tools/press — the reading copy

Six readable PDFs of the seated volumes, in `out/reading/`. 933 pages.

    sh tools/press/press3.sh <member>.md <name> "<TITLE>" <toc-depth> "" [strip]

**How it works, and what it is not.** `build.py` (a seated member) is the press: it applies the
press-time substitution table — Rulings 42, 45, 46 and 60, "source files are never edited" — and every
typographic rule the volumes need. It targets pandoc → docx → LibreOffice, and LibreOffice's Word
filter is missing in this container, so the last two steps are replaced: pandoc renders HTML on
`book.html`, and WeasyPrint prints it with CSS paged media, which gives a title page, a contents with
real page numbers, running heads and numbered pages. `build.py` itself is untouched.

**`press2.py` declines dead anchors and names every one.** `sweep()` asserts each substitution anchor
occurs exactly once and stops the press otherwise, so a volume whose text has moved past an anchor
cannot be pressed at all. `press2.py` keeps every anchor that still matches, drops the ones that do
not, and prints each dropped anchor with its match count. **13 anchors are currently dead** — 6 in the
Register, 7 in the Mathematical Compendium — so those press repairs are missing from the reading
copy. Five of the seven in the Mathematical Compendium strip script names from object provenance
lines, so `twoheur.py`, `allcons.py`, `protindex.py`, `stat_lang.py` and `close_L.py` appear in
reader text. Repairing them needs a `build.py` successor, which is the edition's work, not this copy's.

This is a **reading copy of the seated volume**, not the edition. The edition additionally needs the
paged print index (`index_pages.py`, `appf.py`), the dead anchors repaired, and everything the
publication plan's phases 1 to 7 settle.
