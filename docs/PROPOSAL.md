# `tools/proposal.py` — the complete proposal and the pitch, rendered from the instruments

> **Reviewed 2026-09-12** (`docs/PROPOSAL-REVIEW.md`): the closing plant now carries its O&M, the environmental and
> employment rows are at the adopted route, and the water's lift is priced at the route's one head. Whole-load price
> $172 / $279 per MWh, RA 3,616 / 3,537 MW, washing 872 / 1,486 AFY, land 45,361 / 66,339 acres, Title I jobs
> 1,901 / 1,214, Title II jobs 601 / 664, water with the lift $3,280 / $5,234 per acre-foot; a figure below computed
> before that pass is superseded by the instrument's current output.

**Why it exists.** The author (2026-09-12): *build the complete proposal, with every item fully
expanded, each location addressed in full, figures, tables, graphs, cited studies — as complete as
conceivably possible — and then a two- or three-page bullet-point pitch accompaniment.* The three
v0.2 Titles are the diff against v0.1, stated as documents; nothing rendered the whole program as
one document, drew its figures from the instruments, or set the pitch beside it under a check that
the short document cannot say what the long one does not.

**Run it.** `python3 tools/proposal.py` renders `proposals/California_Sovereign_Infrastructure_v0.2.md`
(the proposal), `proposals/Pitch_v0.2.md` (the pitch) and the twelve figures under
`proposals/figures/`; `--docx` also emits both as `.docx` from the same rendered text; `--no-figures`
renders the text only; `--selftest` asserts the invariants below. Rendering runs `hourly3.py` and
`both.py` at both cases and takes about ten minutes; the selftest re-gathers and takes as long again.
The figures need matplotlib; the text needs the stdlib only.

## What it renders

Twenty-one sections, A to U: the summary and the decision asked for; the requirement (F-17); what v0.1
submitted and what `helios.py` and `heliocost.py` found; the equipment question (`firmpower.py`);
the seven-link chain and the two plants on it (`cspchain.py`); Helios-3 link by link, sized and
costed by line, with the receiver's threshold and ladder (`receiver.py`); the hour-by-hour and the
month-by-month table (`hourly3.py`); the three routes, the ladder over the water's share, the
adopted point and its sensitivity to head and holding (`joinder.py`, `both.py`); the sixteen-row
register with every mitigation, carrier, source and price (`helios3.py`); the forty-nine study rows
grouped by technology with every source and recommendation (`studies.py`); the pilot aperture's
unit, measurements, pass mark and consequences (`pilot.py`); the studies and surveys row by row
(`predev.py`); the price, the household during and after the bonds, the securities, the mechanism,
the reserve, the downside, the schedule with both cases' years and the gen-tie (`titleone.py`,
`majors.py`); Title II's module, water, process decisions and schedule (`aquacost.py`,
`titletwo.py`); Title III's agreement, decision table, financial statement and severability
(`rebase3.py`'s constants); every Title I node and every coastal brownfield term by term, with its
first study (`sites.py`); the environmental and employment rows (`minors.py`, `majors.py`); what is
not settled; all forty flaws with claim, failure, what settles it and resolution (`FLAWS.tsv`);
the sources, deduplicated from the study register; and the instruments.

**The figures** are drawn from the gathered numbers and never typed: the built record against
Title I's $/W; every candidate's price; the chain link by link; the load by month and what is
served; the load shape on a July and a December day; the ladder over the water's share; modules
against head; the price step by step; the household today, during and after the bonds; the capital
stack; the schedule by tranche at both cases; the sites scored. Colours are the dataviz palette's
categorical slots: mid blue, critical orange, ink for today.

## What the selftest holds

- Both files on disk are byte-identical to a fresh render: never hand-edited.
- Every figure the proposal references exists; it places twelve.
- Every flaw, every study, every register row with its source, every node and every coastal site
  appears.
- **The pitch carries no number the proposal does not.** Every numeric token in the short document
  occurs in the long one, so a figure cannot appear in the pitch without a section, a case and a
  source behind it.
- Mid never exceeds critical on the whole-load price or the program total; the post-bond price is
  the adopted route's O&M (register plant and closing plant) over the energy and nothing else.

## What it does not do

It computes nothing of its own beyond sums, ratios and the post-bond price. `firmpower.py`'s bands
are low / mid / high rather than mid / critical, so its high column stands where critical stands
elsewhere and the table says so. The `.docx` is a plain rendering of the markdown (headings, tables,
bullets, pictures, bold and italic) and carries no layout beyond that.
