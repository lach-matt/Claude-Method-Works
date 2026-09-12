# `tools/rebase.py` — Title I re-based on Helios-3, rendered from the instruments

> **Reviewed 2026-09-12** (`docs/PROPOSAL-REVIEW.md`): the closing plant now carries its O&M, the environmental and
> employment rows are at the adopted route, and the water's lift is priced at the route's one head. Whole-load price
> $172 / $279 per MWh, RA 3,616 / 3,537 MW, washing 872 / 1,486 AFY, land 45,361 / 66,339 acres, Title I jobs
> 1,901 / 1,214, Title II jobs 601 / 664, water with the lift $3,280 / $5,234 per acre-foot; a figure below computed
> before that pass is superseded by the instrument's current output.

> **Studies line, 2026-09-11.** `tools/predev.py` now carries every study and survey as the first line of the
> capital (`docs/PREDEV.md`); the register price is $126 / $205 per MWh, water $3,044 / $4,830 per acre-foot,
> and any figure below computed before that line is superseded by the instrument's current output.

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why it exists.** `proposals/California_Sovereign_Infrastructure_v0.1.md` is the as-submitted
merge and is never edited; every repair is a diff against it. After the second pass — Helios-3
chosen, the mitigation register adopted row by row, the plant run hour by hour, the water route
priced — the diff had grown past what a register can hold, and Title I needed stating as a
document again. This file renders **`proposals/Title_I_Helios-3_v0.2.md`** from the instruments
that computed it: `helios.py` (the requirement), `cspchain.py` (the plant), `helios3.py` (the
register and the price), `receiver.py` (the receiver threshold), `hourly3.py` (what it serves
and what closes it), `joinder.py` (the water route), `studies.py` (provenance, the ladder,
the cost of delay), `aquacost.py` and `titleone.py` (Title II's price beside the water route; the
rate table, the schedule and the gen-tie), and `minors.py` (the cycle label in §2, and §8 —
emissions, employment, seismic, procurement and the Authority).

**Run it.** `python3 tools/rebase.py` renders (several minutes: it runs `hourly3.py` and
`joinder.py`); `--selftest` checks. Stdlib only.

## What the discipline is

The document **carries no number this file did not read from an instrument**, and every number
is labelled **mid** or **critical**, under the author's standing rule that a number quoted
without its case is misquoted. The selftest asserts the file on disk is **byte-identical to a
fresh render** — so it cannot have been hand-edited — and that its key figures equal the
instruments': the register price, the served share hour by hour, today's household bill beside
the criterion, every register row, and the receiver's field factor against the chain's own link
(the first render divided it against itself and printed 1.00; the selftest now pins 1.2–1.4).

## What v0.2 says, in one table

| $/MWh (household $/yr, today 1,177) | mid | critical |
|---|---|---|
| Helios-3 as chained | 117 | 187 |
| with the mitigation register | 125 (756) | 202 (1,218) |
| serving the whole load, mirrors route | 185 (1,119) | 302 (1,824) |
| serving the whole load, water route | 192 (1,161) | 310 (1,868) |

The criterion stated exactly: the plant pays for itself after the bonds only at a price above
the contract band; at mid a household serving its whole load from the plant pays about what it
pays now, and at critical it pays more. The critical case is the threshold the design is held
to, and the document does not offer a mid-only design.

## What it does not settle

The route for the season (mirrors or water) is Title III's decision; the evening block factor
waits on a measured load profile; the receiver's critical figure waits on the pilot aperture;
and transmission, the tariff, the bond rate and the schedule (F-09, F-10, F-19, F-24) were open
in `FLAWS.tsv` at this pass and have since been settled by `titleone.py` and rendered here as
positions with a price. With the minors folded in (`minors.py`, `docs/MINORS.md`) every row of
`FLAWS.tsv` is resolved. F-06 — the solar multiple that did not match the aperture — is
**resolved** by this pass: the winter guarantee is not a label on the field but a route.
