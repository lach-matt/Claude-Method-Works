# The class sweep — `tools/sweep.py`

Chat 152 (RUL-152) settles how the compendia close. Item 1 sends the Register to a full source-order
read under the chat-81 cadence. **Item 2 sends the other four — the Mathematical Compendium, the
Physics Compendium, the Index of Indices and the Spectra Compendium — to a class sweep against the
docket's classes, under chat 127 item 2. They are not read line by line.** This program is that sweep.

    python3 tools/sweep.py                     # the four compendia, every class
    python3 tools/sweep.py --selftest          # the calibration, asserted
    python3 tools/sweep.py --volume reg --class C2-THEOREM-POINTER-UNPRINTED
    python3 tools/sweep.py --class C9-OVERGENERALISATION-WORD --tsv

Stdlib only. It reads the seated members and writes nothing.

## The classes are not invented here

They are the thirteen already in `drive/The Method Materials/CORPUS/DEFECT-CENSUS.tsv`, and every
detector is calibrated against the rows that census already records. **A detector that cannot
reproduce the census's own rows on a volume the census swept is not the census's detector, and is
not run on the volumes it did not sweep.** `--selftest` asserts eleven such reproductions, all exact:

| class | volume | rows |
|---|---|---:|
| C1-SECTION-POINTER-UNRESOLVED | ioi | 1 |
| C2-THEOREM-POINTER-UNPRINTED | mc / main / reg | 4 / 1 / 6 |
| C6a-ENTRY-NO-SOURCE-POINTER | mc | 35 |
| C9-OVERGENERALISATION-WORD | main / ioi / pc / sc | 219 / 13 / 10 / 1 |
| C10-PROVED-WITHOUT-REGISTER | mc | 86 |
| C11-R-FORM-INCOMPLETE | mc | 55 |

## Three verdicts, and the third is the point

**RUN** — the detector reproduces the census where the census swept, so its count elsewhere is the
sweep's own reading.

**NOT-APPLICABLE** — the class is defined against a form the volume does not use. C6a, C10 and C11
read the Mathematical Compendium's **R-form** entry: `### name`, a bold statement, a scope, a grade
(`Proved`, `Measured`, `Computed` — `Cited`, `Definitional`, `Conditional` and `Asserted` are not
grades, which is why the census flags the entries carrying them), then `> **Prior art: …**`. The
Index of Indices and the Spectra Compendium open no `###` block at all. The Physics Compendium opens
27, and they are a different form — a status line, `**What it is.**`, `**Where it comes from.**`,
`> **Where it fails.**`, and none of the R-form's fields. Read with the R-form detector all 27 report
as missing a grade they were never asked for, which is a false population, not a finding.

**NOT-RUN** — the census records rows this program cannot reproduce, so the census's own predicate is
not recovered and no detector is guessed. `cypher.py` keeps the same rule under the name REFUSED: a
resource or definition limit is not a silence, and it is not a finding either. Six classes stand
here, each with its reason printed.

## What the sweep found

**Nothing new.** On the four compendia, every runnable class returns either zero or exactly the rows
the census already carries. The apparent under-sweep — 10 census rows on the Physics Compendium and
1 on the Spectra Compendium against 691 on the Mathematical Compendium — is not a gap: five of the
thirteen classes are Mathematical-Compendium-form classes with nothing to read in the other three
volumes, and of the classes that do apply, C9 was already complete on all four.

## Two faults found in the reader, not in the books

Both were mine, and both are the same fault: **a scan that reads only headings misses what the book
tabulates.**

1. **§4.1 to §4.10 are a tabulated list, not headings.** Chapter 4's ten mechanisms are written
   `  4.1   **attributed outward before checking inward** — …`. A heading-only inventory reports
   them unresolved at 42 sites across main, the Register and the Mathematical Compendium. The
   chapter says as much about its own history: *an earlier form was a heading with no body at all,
   carrying the word SEVEN while the register held ten — cited as §4.1 and §4.2 throughout a book
   that never defined them. Register 655.* It has a body now, and the body is the list.

2. **`Theorem 7.1 is absent — withdrawn` is not Theorem 7.1 being printed.** A loose anchor read
   that sentence as the theorem's own statement and silenced the census's row on it. A printed
   theorem opens its line and is followed at once by its statement or its tag. Separately, a
   prior-art blockquote cites *other people's* theorems — `Cover & Thomas … Thm 2.8.1` — and those
   are not the book's to print.

## What the sweep does not do

It does not adjudicate. A row is a class and a site, and what to do about it is the docket's. It
also does not touch `DEFECT-CENSUS.tsv`, which is a mirrored Drive record: `--tsv` emits rows in
that file's own schema so they can be carried across by the sync, never by this program.
