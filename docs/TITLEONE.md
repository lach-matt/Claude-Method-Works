# `tools/titleone.py` — the four Title I flaws no instrument had touched

**Why it exists.** After the second pass, four rows of `FLAWS.tsv` on Title I had been touched by
nothing numerical: the bond rate (F-19), the schedule (F-24), transmission (F-09) and the tariff
(F-10). Each names what settles it, and each is settled here the way the register asks — as a
position with a price, at mid and at critical — rather than as a witness. Every number is imported
from `helios3.py`, `cspchain.py`, `hourly3.py` and `heliocost.py`; the file states four positions.

**Run it.** `python3 tools/titleone.py`, `--selftest` for the checks. Stdlib only.

## F-19 — the bond rate

The 3.85 % Title I assumes is an investment-grade municipal rate on a contracted revenue stream,
and a first-of-kind plant has no such rating on its own. **The security**: contracted in-state
offtake at the required price — the same load-serving entities who pay $80–120/MWh for firm clean
energy today — with a **state general-obligation backstop for the first-of-kind rungs**, which is
the state's to give. Priced to each security, with the mitigation register:

| security | rate | mid, $/MWh ($/household) | critical, $/MWh ($/household) |
|---|---|---|---|
| GO-backed, state general obligation | 3.85 % | 125 (756) | 202 (1,218) |
| revenue bond, contracted in-state offtake | 5.00 % | 140 (846) | 227 (1,369) |
| unrated first-of-kind | 6.50 % | 161 (970) | 262 (1,579) |

Today a household pays $1,177. Each point of rate is worth about $13/MWh at mid.

## F-24 — the schedule

v0.1 built 5.25 GW in two construction years where the record is four years for a tenth of that.
The schedule is now the ladder of R-12, dated from the author's 2028–2030 groundbreaking, **each
bond tranche following a rung that has been passed at its critical figure**; the pilot aperture and
the first node's field run in parallel. Direct cost by rung:

| rung | years | mid, $B | critical, $B |
|---|---|---|---|
| field, towers and PV at the first node | 2029–2031 | 3.02 | 4.68 |
| pilot aperture on one tower | 2031–2033 | 0.07 | 0.07 |
| first 100 MWe module | 2033–2036 | 0.63 | 0.94 |
| fleet, by tower group | 2036–2041 | 12.68 | 18.86 |

The first module's COD is the third rung; the fleet's last tower group is a decade from
groundbreaking. The durations are ASSUMED and say so; the tranche split is `cspchain.py`'s own lines.

## F-09 — transmission

The 1,515 MW export needed firm rights that do not exist. F-01 found the export is **negative**, so
the export need is zero and no right has to be bought. What remains is the in-state gen-tie per
node at the closed sizing (block ×1.5), from the hour-by-hour peak injection: **1,196 MW per node
at mid, 1,179 at critical** — 0.60 / 0.79 of one 500 kV circuit (rated 2,000 / 1,500 MW,
SOURCED band) — priced in `heliocost.py`'s switchyard line at $600 / $900 M. PV and the
block are anti-coincident, so the peak is below their sum, and the selftest asserts it. The
interconnection study and the CAISO cluster application are the Authority's to file; no sovereign
authority shortens them.

## F-10 — the tariff

$0.00/kWh is not the Authority's to give: retail generation charges are set in IOU tariffs under
the CPUC. The tariff is replaced by the household bill at cost recovery, an **output** of the
balance — $756 at mid and $1,218 at critical with the register, against $1,177 today, and
the whole-load prices of the re-base move it further. **The mechanism**: the Authority registered as a load-serving entity in the community-choice form (PUC section 366.2), IOU delivery, generation sold at cost recovery. A free tariff
is a subsidy paid by someone, and this program names no one to pay it.

## Status

F-09, F-10, F-19 and F-24 move to RESOLVED in `FLAWS.tsv` in the register's sense: the claim is
replaced by a position with a computed figure and its case. None of the four is a witness, and the
re-base carries all four.
