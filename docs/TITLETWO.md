# `tools/titletwo.py` — Title II's process rows, settled; `tools/rebase2.py` — Title II re-based

**Why they exist.** After `aquacost.py` priced the module and its water, eleven rows of `FLAWS.tsv`
on Title II were process questions — minerals, brine, the desalination process, the schedule, the
energy price, on-site power, the intake, and two internal contradictions. `titletwo.py` settles
each the way the register asks, a decision where it asks for one and a computed figure where it
asks for one, at mid and at critical. `rebase2.py` then renders **`proposals/Title_II_Aqua-Sovereign_v0.2.md`**
from `aquacost.py`, `titletwo.py`, `joinder.py` and `hourly3.py`, byte-identical to a fresh render by
selftest, every number labelled with its case.

**Run them.** `python3 tools/titletwo.py` (`--selftest`), `python3 tools/rebase2.py` (`--selftest`).
Stdlib only.

## What is settled

- **F-03, F-11 — minerals.** No mineral revenue is in the water's price. One module's magnesium as
  hydroxide is **382 kt a year**, 0.76 of the US magnesium-compounds market at mid and
  1.27 of a smaller market at critical; the water route's thirty-odd modules would be twenty to
  forty markets. F-11's 79,600 t counted the product volume; the brine carries the *feed's*
  magnesium, twice that, and the correction runs against the revenue. Lithium is 22 t a year.
- **F-04, F-12 — brine.** ZLD dropped (author, 2026-09-11). At 50% recovery the brine is 67 ppt,
  33.5 above ambient, against the Ocean Plan's 2 ppt at the 100 m edge: **a diffuser dilution
  of 17 : 1**, which a retired plant's outfall must achieve with no cooling water — Carlsbad's
  post-2018 multiport configuration, priced in `aquacost.py`'s outfall share.
- **F-13 — process.** Seawater RO is the default and is what is priced; LT-MED only beside a named
  source of ≥ 500 MW_th per module, and none is named.
- **F-15 — schedule.** Carlsbad: 1998 proposed, 2006 permitted, 2015 water (17 years); Huntington
  Beach: 1998 to a 2022 denial. Permitting **5–8 years** (assumed from the record) and a
  3-year build put first water at **2034–2037** from 2026, beside the water route's need in
  Title I's ladder; each year of delay escalates a module by $57–87 M. A statutory
  consolidation shortens litigation, not the Coastal Commission.
- **F-26 — energy price.** Priced at Title I's contract price full-time. Title I's surplus is
  **589 hours a year, 7%** of them, not half; a membrane plant runs steadily. The surplus is
  the water route's lift, an upside the price does not count.
- **F-27 — on-site power.** A module draws 21–25 MW on average; the whole brownfield given
  to PV makes 2.8–1.5 MW, **13%–6%** of it. Islanding is a battery for the intake,
  pretreatment and controls (3.2–3.8 MW); full-load islanding is not claimed.
- **F-28 — intake.** screened open intake through the retired plant's channel, 1 mm wedge-wire at <= 0.5 ft/s (the Ocean Plan's alternative to subsurface intake), slant wells where per-site hydrogeology permits. Entrainment is non-zero and mitigated under the Ocean Plan;
  "eliminating 100 %" is withdrawn.
- **F-35, F-36.** Moot with ZLD and the mineral train gone; CIP waste neutralised and returned with
  the brine under the NPDES permit.

## Status

Eleven rows move to RESOLVED in the register's sense. What v0.2 does not settle is per-site — head,
hydrogeology, the diffuser, the entrainment — and the takers for a million acre-feet a year of winter
delivery, which is the joinder's question.
