# `tools/final.py` — the final edition of the proposal and the pitch

**Why it exists.** The author's notes for a final draft (2026-09-12): no version numbers; the author
line *Matthew Lach, Independent Researcher*, with 2026 and no render date; numbered sections; an
abstract ahead of the summary that states the existential problem of energy and fresh water; a basic
table of contents; a full bibliography; and prose that is analytical and instructive — **subject
matter only, not workshop matter**. `proposal.py` renders the working edition, which names the
instruments, the flaw register and the drafting history on every page because that edition is the
record of how the numbers were made. A reader of the proposal is owed the numbers and their sources
and nothing about the making. This program renders that edition.

**Run it.** `python3 tools/final.py` renders `proposals/California_Sovereign_Infrastructure.md` and
`proposals/California_Sovereign_Infrastructure_Pitch.md`; `--docx` and `--pdf` emit both through
`proposal.py`'s emitters (`--export-only` does so from the files on disk); `--selftest` asserts the
invariants below. It gathers through `proposal.gather()` and so runs the hourly model and the
closing-route ladder at both cases, about ten minutes; the figures are the working edition's and are
not redrawn here.

## What it renders

Front matter: title, subtitle, author line, the abstract, a contents list and a note on how to read
the two cases. Nineteen numbered sections: the summary and the decision requested; the requirement;
what was submitted and what it makes and earns; the equipment question; the energy chain; Helios-3
by link, by line and by threshold; the plant hour by hour; the closing routes and the adopted point;
the register of risks; the studies; the pilot aperture; the studies and surveys; the price, the
household, the securities, the reserve, the downside and the schedule; water; the joinder; the sites;
impacts and employment; what is not settled; how the figures were produced. Then the bibliography.
The pitch is the same case in brief under its own headings.

## The scrub

Every string that reaches the page from a data table — a register row's mitigation, a study's
source, a site's note, a decision's record — passes through `scrub()`, which removes the
parentheticals that name a model, the dated author attributions, the flaw references and the
drafting vocabulary, and maps each model's file name to what it is (the receiver model, the hourly
model, the chain model, the study register, the acceptance protocol, the closing-route analysis, the
site screening, the study budget). *The author* becomes *this work*. Nothing numeric is touched.

## The bibliography

Numbered in order of first citation: every source the study register names (split on semicolons
outside parentheses, scrubbed, the work's own runs excluded), then the sources of the constants the
text cites — EIA, the ATB, the NSRDB, CAISO's market report, the SAM cost structure, the Ocean Plan,
the Carlsbad and Huntington Beach records, PPIC, ASCE 7, the CGS maps, SB 6X and the codes it names,
PRC §25524.2, the geothermal and SMR records, the LPO record, the staffing records and the reservoir
records. A study table cites its row's sources by number; the prose cites by key.

## What the selftest holds

- Both files on disk are byte-identical to a fresh render.
- **No workshop token survives** in the proposal's body or the pitch: no file name, no flaw
  reference, no version string, no render date, no *the author*, no *instrument*, no *selftest*,
  no *register price* (the register is a risk register in this edition; the price is the plant
  price). The bibliography is exempt only for the sources' own titles, and the check found none there.
- The author line is present and no render date is.
- The abstract precedes the summary; the contents list matches the section headings exactly; every
  section heading is numbered.
- Every citation in the text resolves to a bibliography entry and every entry is cited at least once.
- The pitch carries no number the proposal does not.
- Every figure the proposal places exists; the registers, the studies and the sites are all present;
  the program total is the closing-route analysis's own.

## What it does not do

It computes nothing: every number is the working edition's, gathered by the same call. It does not
redraw the figures; those are drawn by `proposal.py`, whose titles carry no model names since this
pass. The `.docx` and the `.pdf` are the same plain renderings the working edition uses.
