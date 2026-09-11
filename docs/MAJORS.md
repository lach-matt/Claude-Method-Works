# `tools/majors.py` — the remaining majors, settled; `tools/rebase3.py` — Title III, the joinder

> **Studies line, 2026-09-11.** `tools/predev.py` now carries every study and survey as the first line of the
> capital (`docs/PREDEV.md`); the register price is $126 / $205 per MWh, water $3,044 / $4,830 per acre-foot,
> and any figure below computed before that line is superseded by the instrument's current output.

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why they exist.** After Title I and Title II were re-based, nine rows of `FLAWS.tsv` remained
that were neither minor nor touched: six Title I majors (F-18, F-20, F-21, F-22, F-23, F-25), the
two program-wide rows (F-29 sensitivity, F-30 contingency), and the joinder itself (F-31).
`majors.py` settles the first eight the way the register asks, at mid and at critical, from the
instruments; `rebase3.py` writes Title III — the power-supply agreement, the single financial
statement, the severability and the decision — as **`proposals/Title_III_Joinder_v0.2.md`**,
byte-identical to a fresh render by selftest.

**Run them.** `python3 tools/majors.py` (`--selftest`), `python3 tools/rebase3.py` (`--selftest`).
Stdlib only.

## What is settled

- **F-18 — resource adequacy.** The export is negative, so there is no export RA. In-state RA is
  the closed block's net capacity, **3,616 / 3,537 MW**, self-supplied by the Authority
  as the load-serving entity: a requirement met, not a revenue line.
- **F-20 — mirror washing.** Scaled per m² from Ivanpah's 100 AFY on 2.6 M m²: **1,394 / 2,378 AFY**
  on the mirrors route, 697 / 1,189 on the water route — under one module-year either way — and the
  source is the program's own water: Title II's desalinated water on the mirrors route, the water
  route's own delivery on the other.
- **F-21 — land.** `cspchain.py`'s own acreage: **62,160 / 94,980 acres** on the mirrors route
  (20,720 / 31,660 per node, 84 / 128 km²), 39,762 / 56,792 on the water route. Fallowed,
  drainage-impaired Westside San Joaquin farmland covers a node 4.8× / 1.9× on the mirrors route: the
  one contiguous disturbed parcel of this size in the state, which the document did not claim.
- **F-22 — the Central Valley node.** Its DNI is 0.78 of the Mojave's and `hourly3.py` runs it on
  its own series; its December is the model's kindest. Moving it to the desert lifts service from
  0.839 to 0.856 and does not change the closing sizing. Kept, at a larger field share, because
  its land is the program's best.
- **F-23 — the nitrate register.** Helios-3 holds no nitrate; the medium is sintered bauxite, so
  the oxidiser, the decomposition ceiling, the freezing point and the hot tank leave with the salt
  (helios3 R-13 to R-15). They return only with the salt-block fallback, whose hot tank is the
  record's own failure (Crescent Dunes four leaks, Noor III fourteen months).
- **F-25 — federal nexus.** NEPA is not shortened by any state statute; the first node is the one
  with no federal nexus (Westside), and the Mojave node budgets NEPA on the fleet rung: 2 / 4 years,
  **$647 / $2,184 M** of escalation while it waits.
- **F-29 — the downside case** is the critical case, by the author's standing rule. A revenue bond
  adds coverage: at 1.25× the price is **$151 / $245 per MWh** (909 / 1,477 per household).
- **F-30 — contingency, reserve, overrun.** Contingency **15% / 30%** and EPC 13% / 15% are
  carried in the capital; a debt-service reserve of one year, **$1,836 / $3,100 M**; the overrun backstop
  is the state GO of F-19. The critical case carries the 30 % first-of-kind figure the flaw asked for.

## Title III

The power-supply agreement (Title II buys at Title I's price for the bond term; energy is a sixth
of the water's cost), the one shared asset (the reservoir and pump-turbines are Title I's, the
modules Title II's, the lift energy the surplus), the decision table (mirrors against water at both
cases: parity on the power side, 1.6–1.8 million acre-feet a year and $62–102 B of Title II capital on the
other), the takers (SGMA recharge, a contract question), the single financial statement, and
severability both ways. **The decision is the author's** and the document says so.

## Status

Nine rows move to RESOLVED. Thirty-three of forty are resolved; the seven that remain are minors of
wording and citation. Those seven are settled in `tools/minors.py` (`docs/MINORS.md`), which brings the
register to forty of forty.
