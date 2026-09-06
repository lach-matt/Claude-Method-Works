# Mathematical Compendium — Phase 2 audit (reader perspective)

| # | finding | status |
|---|---|---|
| M1 | 265 objects, 18 families, no duplicate ids; every family header count matches its contents. | Verified. |
| M2 | Every object carries bold statement, italic gloss, grade line; every `depends on` and chain id resolves. | Verified. |
| M3 | Eight source references pointed at main-volume sections that no longer exist (`M §20.5`, `§21.8.1`, `§21.8.2`, `§21.10.1`, `§21.10.4`, `§21.15`, `§22.9`, `§26.9`). All resolve at chapter + 2 — written before Part IV (Chapters 20–21) was inserted. | **Closed** — repointed (§22.5, §23.8.1, §23.8.2, §23.10.1, §23.10.4, §23.15, §24.9, §28.9). Same test to be run on every volume in Phase 3. |
| M4 | 27 objects carried two PRIOR ART callouts jammed into one line; in 10 the second was a verbatim repeat. | **Closed** — repeats removed; the 17 distinct pairs split into two callouts. |
| M5 | ASCII/Unicode drift in the same names: `Lambda-9`/`Λ₉`, `Lambda_spectra`/`Λ_spectra`, `<=`/`≤`, `phi(`/`φ(`, `--`/`—` (about 150 instances outside code spans). | **Closed** — normalised to the Unicode forms the volume otherwise uses; code spans untouched. |
| M6 | "1 objects depend on it" (74). | **Closed.** |
| M7 | `M.semi` was the one object absent from the bibliography (Murray & von Neumann 1936). | **Closed** — row added; 172 works. |
| M8 | LS-family depths (15–17) are the build's assignment, not the author's. | **Open — Phase 3 chain audit** to confirm or reassign. |
| M9 | `T §5.1`, `T §6.5` reference the tower companion, not this set; unverifiable here. | Noted; no action. |