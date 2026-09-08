# DRAFT-R4-PHASE4 — the compendia repairs, one item at a time

**M RULED ON ALL THREE QUESTIONS ON 7 SEPTEMBER AND SIX OF THESE ITEMS ARE NOW SEATED.** The file is kept as
it was written, and what has since happened is recorded here rather than edited into the items:

| item | disposition |
|---|---|
| **C1** Spectra L562, `41–5` → `41–55` | **SEATED**, BUILD278, `W-283` |
| **C2** Index of Indices L2021, the truncated row restored | **SEATED**, BUILD278, `W-283` — and `r2-ch27a4` had banked this defect as a golden before the census found it; the repair takes it from *29 of 30* to *30 of 30* |
| **D1** Ruling 46, script names, stamps, the rebuild command | **SEATED**, BUILD279 and BUILD281, `W-284` and `W-286` — thirty substitutions, then one more the pass missed |
| **D2** Ruling 45, six interface disclosures | **SEATED with D1**; three are refused with their reason, being a verbatim quotation of a stored row and two descriptions of the column it comes from |
| **D3** the handle vocabulary | **THE MAP IS REBUILT AND THE SOURCE IS FOUND** — M ruled the handle map stale and the map mine to build (`W-289`). `proofs/bibindex.py` derives the objects column from the objects' own attributions: **127 of 162 rows**, each object by its descriptive title, in `method/BIBLIOGRAPHY-OBJECTS.tsv`. 35 rows cannot be derived and get no column. `method/HANDLE-MAP.tsv` is superseded as a proposal and kept as the evidence for the cross-check |
| **D4** the 285-of-431 channel sentence | **OPEN** — deliberately untouched by the Ruling 46 pass, which does not license fixing a figure in passing |
| **D5** seven files named to a reader and held nowhere | **THREE SEATED with D1** (the two `MECHANISMS.md` sites and `LITERATURE.md` repointed at the volume that answers); the rest went with their sentences |
| **E1** the three register counts | **RESOLVED AS A MEASUREMENT** (`W-290`): all three are correct counts of three different things. **299** is the objects the compendium holds, family by family; **265** is the handles its bibliography prints; **248** is the `R()` entries in `mathreg.py`, which is **held** at `extracted/archives/restore-point-2-13/` — so E1's "corroborated by nothing here" is corrected. What is left is not a count but a **labelling** question, and it is M's. The *false universal* beside it is corrected too: `W-281` said false by 34; `W-289` measures **12** |
| **E2** the bracket-system object | **OPEN**; writing it is an editorial act |

**One finding is owed a ruling and is new**: family L prints *Three excluded forms* and family T *The three
excluded forms*, so under the handle ruling a descriptive title alone does not identify those two objects.
They need their family printed with them, or one needs renaming (`W-290`).

**Seventeen Ruling 46 sites remain and are refused, not owed**: they are figure image paths, and removing them
would remove the figures. `W-286` records that.

**NOTHING ELSE IN THIS FILE HAS BEEN DONE.** The chat-67 hold stands and a plan is not a repair. Every
figure below is measured by `method/proofs/compendia.py` (25/25, BUILD275) or its successor
`method/proofs/compendia2.py` (57/57, BUILD276), and `W-280` and `W-281` are their closes. Each item
names its site, what stands there, what a repair would put there, and a grade. **A `MEDIUM` names
what would settle it. Two items are marked `RULING` and cannot be graded at all, because the choice
between two repairs is M's and not a matter of evidence.**

The items split on where the repair lands, exactly as `docs/R3-REPAIR-PLAN.md` splits Batch A from
Batch B:

* **Batch C — a determinate correction inside one reader-facing volume.** Two items. Each has a
  single right answer that two independent columns of the volume agree on.
* **Batch D — a class across volumes.** Five items. Each spans more than one file, so the store's own
  rule applies: state the files and the change, and wait.
* **Batch E — an editorial act.** Two items. Nothing is wrong; something is owed.

---

## Batch C — determinate, one volume, one line

### C1 — Spectra Compendium L562: an n-range that runs backwards · **HIGH**

**Site.** `The_Method_1_6___Spectra_Compendium-2.md` L562, the Ga I `4s²np ²P° high` row.

**What stands.** `| Ga I | 4s²np ²P° high | 41–5 | 15 | 13 | 13/13 | 38.8–52.7 | +2.2107 | … |`

**What a repair would put there.** `41–55`.

**Why it is determinate.** Two other columns of the same row fix it independently. The *levels*
column reads **15**, and 41…55 is the only range opening at 41 with fifteen members. The *n\* range*
column reads **38.8–52.7**, and at this row's mean defect of 2.2107 an upper n of 55 gives 52.79
where 54 gives 51.79 and 53 gives 50.79 — only 55 reaches the printed value. **This is the one row in
596 whose range runs backwards**; every other parses, and the twelve rows the detector first called
unparsable carry the volume's dagger marker and are not faults.

### C2 — Index of Indices L2021: a row truncated where an escaped pipe lost what it escaped · **HIGH**

**Site.** `The_Method_1_6___The_Index_of_Indices-2.md` L2021, row 1.7 of the *Transitions* table.

**What stands.** `…the box grows by that coordinate's value count while \ | **rests on it** — Appendix G |`

**What a repair would put there.** `…the box grows by that coordinate's value count while \|X\| stays fixed. | **rests on it** — Appendix G |`

**Why it is determinate.** **The main volume prints the same row whole** — `The_Method_1_6-2.md`
L11425 carries `while \|X\| stays fixed.` — so the repair is a restoration from a source held here
and not a reconstruction. **This is the one such row in the four volumes**; the 22 others a
pipe-splitting read reports are the compendia writing mathematics as `\|X\|` and are not faults.

---

## Batch D — a class across volumes: the files and the change, stated, and waiting

### D1 — Ruling 46: script names, stamps and a rebuild command printed to a reader · **RULING scope, mechanical repair**

**Files.** All four compendia. **23 sites naming 18 distinct scripts** — `mathreg.py`, `mathverify.py`,
`check_audit.py`, `compendium.py`, `twoheur.py`, `allcons.py`, `protindex.py`, `stat_lang.py`,
`close_L.py`, `tower.py`, `tower3.py`, `factor.py`, `ground.py`, `channels.py`, `indices.py`,
`domain_protocol.py`, `coords.py`, `spectra.py`, `spectra_count.py` — plus **seven "generated from …
on" stamps** and **one printed rebuild command**, *"Rebuild with `python3 compendium.py >
COMPENDIUM.md`"*.

**The change.** Each site either loses the name or gains a descriptive substitute. **Which of the two
is a content decision and is not made here.** Ruling 45 governs the same class for build remarks.

**Why it waits.** A pass spanning four reader-facing volumes states its files and its change and
waits — that is the store's own rule, and this is the file that states them.

### D2 — Ruling 45: six interface disclosures · **as D1**

**Files.** Physics Compendium (a session count), Index of Indices (*"claims per session"*), Spectra
Compendium (four, among them *"session 1.8 queue"* and *"the session that fetched it"*).

**The change.** The same choice as D1, and it should be ruled with it: these name the machinery of how
the work was done rather than the work.

### D3 — the handle vocabulary · **RULING — two different repairs, and the choice is M's**

**Files.** Mathematical Compendium (**265 distinct handles at 417 sites**, of which **407 are one
column of one table** — the bibliography's *objects* column, 162 rows) and the main volume (**76
more**: 29 in Appendix G's third column, and **47 printed BARE in running prose**, *"L.c8 is k ≥ 1"*).
**No key resolving one of them is printed anywhere; the word "handle" occurs zero times in the four
volumes.**

**The two repairs.** `PLAN-R4-PUBLICATION.md` proposes **printing a key**. The standing content
standard says the opposite — *"no object handles or workshop jargon in reader-facing volumes;
cross-references name the object by its descriptive title"* — which would **remove them in favour of
the titles**. Both are coherent and they are incompatible.

**What each costs.** A key is one new table and leaves 493 sites where they are. Descriptive titles
rewrite the bibliography's objects column and Appendix G's third column, and the 47 bare prose sites
in the main volume fall in the prose pass rather than here. **The census sizes the class and stops.**

### D4 — the Physics Compendium's 285-of-431 channel sentence · **HIGH, but it spans two volumes**

**Site.** `The_Method_1_6___The_Physics_Compendium-2.md` L186: *"285 of 431 channels are unverified on
the compendium's central claim"*.

**What is true now.** The Spectra Compendium's table holds **126 rows reading `untested`, over 596**.

**Why it is not Batch C.** The sentence is in one volume and its evidence is in another, and the
Spectra Compendium **records the move against itself in the same paragraph as its own count** — the
parent-term wall (register 1578) and the J-resolved rows (registers 1699–1700). A repair to the
Physics Compendium should be taken with that record in view, and 126 is a standing open item the
corpus already publishes as open.

### D5 — seven files named to a reader, none of them held · **HIGH, and MEASURED BY HAND**

**Files.** All four compendia, **8 sites naming 7 distinct non-`.py` files**: `COMPENDIUM.md`,
`INDICES.md` and `vi_best.json` in the Mathematical Compendium; **`MECHANISMS.md` twice** and
`SPECTRA-DATA.tsv` in the Physics Compendium; `LITERATURE.md` and `MEASUREMENTS.tsv` in the Spectra
Compendium.

**What is measured.** **None of the seven is held** — not as a bundle member, not as a row in
`drive/MANIFEST.tsv`. The Physics Compendium's second `MECHANISMS.md` site is the worse of the two:
it is the sentence that tells a reader **where the mechanisms are** — *"those are in `MECHANISMS.md`
and the Mathematical Compendium"* — so the volume answers a reader's question with an address that
resolves nowhere.

**Why this row says MEASURED BY HAND.** `compendia.py`'s Ruling 46 sweep matches `.py` names only,
and `compendia2.py` corrected two of its figures without re-taking that class. **This class was found
by hand after both were seated, and no instrument in the store measures it.** It is owed an
instrument, and until one exists the eight sites above are a floor and not a census. **Recording that
is the point of the row**: a class no instrument holds is exactly the class that goes stale unseen.

---

## Batch E — nothing is wrong; something is owed

### E1 — the Mathematical Compendium's three register counts · **MEDIUM**

**What stands.** Three counts of one register in reader-facing front matter: **299 objects** (MC front
matter, *"Generated from `mathreg.py` on 2026-08-12"*), **265** (the cycle table, *closure — objects
the register holds*), **248 registered objects** (PC front matter, same generator, same date). *And
the eighteen roots table is printed against a seed of seventeen.*

**What is measured.** **299 is corroborated**: the eighteen family headings sum to 299 and every
family holds exactly what it states. **265 is the bibliography's coverage** — exactly the number of
distinct handles its objects column names — and is therefore mislabelled rather than wrong. **248 is
corroborated by nothing here**, because `mathreg.py` is not held.

**And a false universal falls out of it.** The bibliography opens *"Every object of this compendium
names a work."* **299 objects, 265 named in the bibliography: false by 34.**

**What would settle it.** `mathreg.py`, or a ruling that the volumes' front matter states only counts
the volumes themselves can be checked against. **The second is cheaper and is the one this file
recommends**, because it removes the dependence rather than dating it.

### E2 — the bracket-system object · **owed, per register 1880**

**What stands.** Register 1880 records that *"the Mathematical Compendium prints no object for the
bracket system — an expansion owed there and not written here."* **Measured: families B and T name
none.** Family B is the numerical bracket — price V, the four-thirds law, monotone interpolation —
and family T is the tower's bounds; the composition-is-a-bracket-not-a-map result of registers 334
and 1880 is in neither.

**The change.** A new object in the Mathematical Compendium, in the family M rules it into, stating
the bracket system and citing 334 and 1880. **Writing it is an editorial act and is not drafted
here.**

---

## What is NOT in this file

The **nine duplicated (species, series) keys** in the Spectra Compendium — Ba III ×1, Ca II ×1, Si I
×7, every one a pair and none a triple. They are measured and located to the line, and **no repair is
proposed**, because which of each pair survives is a question about the spectroscopic data and not
about the text. That is a data adjudication and it is M's, or the Spectra project's.

The **pointer audit** and the **retraction audit**, which are other instruments' contracts and are not
re-done here. The **twenty-seven "objects rest on it" counts**, which measure 28 in the Physics
Compendium and 1 in the Index of Indices and are not a defect. **Appendix G**, which is clean —
30 rows, 29 handles all printed in the compendium, 12 Register citations all seated, one § pointer
resolving — so the plan's *three pointers to entries that do not exist* do not reproduce. **The Index
of Indices' tower rows**, all six cell counts reproducing against the seated `tower.py` and
`tower3.py` and all six fractions exact to four places.
