# `tools/aquacost.py` — Title II priced: the module and its water, at mid and at critical

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why it exists.** F-16 says Title II's capital is understated three- to four-fold and names no
source for it; F-14 says $400 per acre-foot rests on a mineral offset that F-03, F-11 and F-12
dissolved. Both name what settles them: a bottom-up cost build per module with the energy at the
Title I contract price, and a stated financing structure. This is that, under the author's
standing rule, and the energy line is the joinder: the water's electricity is bought from Title I
at the price `helios3.py` requires at each case, so the water carries Title I's case.

**Run it.** `python3 tools/aquacost.py`, `--selftest` for the checks. Stdlib only; imports the
energy price from `helios3.py`, the financing form from `helios.py` and `heliocost.py`, the module
count and the lift from `joinder.py`, and restates none.

## The module

50,000 AFY seawater reverse osmosis on a coastal brownfield (F-13: RO is the default), brine
returned through the retired plant's permitted outfall (F-12: ZLD dropped), state-owned on Title
I's own form. **The unit capital is derived from the built record and never typed**: mid is
Carlsbad (56,000 AFY, Encina brownfield, ~$1.0 B in 2015) escalated to the groundbreaking dollar
at 3 %/yr, **$27,011 per AFY**; critical is Huntington Beach as designed and denied
(50,000 AFY, ~$1.4 B in 2020), **$36,534 per AFY**. Title II submitted $5,000–6,400.

| | mid | critical |
|---|---|---|
| overnight per module, $M | 1,391 | 1,881 |
| financed (contingency, EPC, IDC), $M | **1,883** | **2,886** |
| against Title II's $250–320 M | 6.6× | 10.1× |
| debt service, $M/yr | 107 | 164 |
| electricity at Title I's price, $M/yr | 23 at $125/MWh | 45 at $202/MWh |
| non-energy O&M, $M/yr | 22 | 31 |

**F-16's three- to four-fold was itself understated: the record is 6.6× at mid and
10.1× at critical**, financed.

## The water

At cost recovery — debt service plus operations, no mineral revenue —

| | mid | critical |
|---|---|---|
| $ per acre-foot | **3,034** | **4,790** |
| $ per m³ | 2.46 | 3.88 |
| of which energy | 15% | 19% |
| per household per year at 0.28 AF | 850 | 1,341 |

Against Title II's $400, Carlsbad's delivered $2,700–2,900 and a wholesale price today of about
$1,300: **the claim was 7.6× below the cost at mid and 12.0× at critical**, and the cost sits where
the built record sits. Capital dominates, not energy; desalinated water is not cheap water, it is
firm water, and it is priced as such.

## The water route's side of the parity

`joinder.py` priced the reservoir and the pump-turbines to Title I and left the modules to Title
II. Here they are, with the lift on the water's own bill:

| | mid | critical |
|---|---|---|
| modules at 500 m of head | 32.8 | 35.3 |
| water, M acre-feet/yr | 1.64 | 1.76 |
| modules' capital, financed, $B | **61.8** | **101.7** |
| lift, kWh/m³ | 1.51 | 0.96 |
| water with the lift, $/acre-foot | 3,268 | 5,030 |
| per household per year | 915 | 1,408 |

The parity on the power side stands. What the water route adds is a water program of 62 to
102 billion dollars making 1.6 to 1.8 million acre-feet a year at what firm water costs. Whether
California wants that much firm water at that price is the joinder's question, now with a number.

## What it does not do

It counts no mineral revenue (F-03, F-11), prices no site, and takes the unit capital from two
plants, one built and one designed and denied. The energy price is Title I's register price at
each case; a plant serving its whole load would charge more (`rebase.py` §5) and the water would
follow it. F-14 and F-16 are **resolved** by this file, in the sense the register uses: the claim
is replaced by a computed figure with its case on it.
