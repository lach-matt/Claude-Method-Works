# `tools/pilot.py` — the pilot aperture as an acceptance protocol

**Why it exists.** Of the items left open after the register closed, the receiver's real efficiency
is the one no instrument can compute: `receiver.py` holds the design to a critical open-aperture
figure of 0.690 (nominal 0.882) and hands the chain a field factor of 1.30, and no falling-particle
receiver above 2 MW_th has run. The ladder puts a ~30 MW_th pilot aperture before the first module.
A test whose pass mark is chosen after it runs is not a test, so this file fixes the mark now, from
the instruments' own figures, and prices every outcome upstream.

**Run it.** `python3 tools/pilot.py` (`--selftest`). Stdlib only; imports `receiver.py`,
`cspchain.py`, `hourly3.py` and `titleone.py` and defines no receiver constant of its own.

## The unit under test

| | nominal | critical |
|---|---|---|
| curtain width × drop, m | 10 × 3 | 60 × 1 |
| aperture area, m² | 30 | 60 |
| particle flow, kg/s | 125 | 150 |
| aperture-average flux, MW/m² | 1.0 | 0.5 |
| ambient, °C | 25 | 45 |

The critical unit is the design basis: wider, shallower, hotter, at half the flux. Both carry 30 MW_th.

## The five measurements

1. **Thermal efficiency**, by calorimetry: weigh-cell mass flow, inlet and outlet temperature,
   incident flux by calibrated heliostat field and flux gauge. Graded at critical conditions.
2. **Edge losses**: the same measurement at half and full curtain width on one aperture. The loss
   per m² must fall as perimeter over area, which is the scaling law the fleet tower rests on.
3. **Dome beside open**: one compound quartz dome (R-02) and one open aperture on one tower. The
   model says the dome loses and the record says it pays; the pilot decides.
4. **Particle ageing**: absorptance, attrition and oxide state sampled quarterly (R-01, R-08).
5. **Wind**: the graded figure must hold across the site envelope, 0–12 m/s, not at calm.

## The pass mark

Calorimetric uncertainty in quadrature is **3.3 %** (flow 1 %, ΔT 1 %, flux 3 %), and the mark must
be cleared by it.

| result, averaged over the graded window | grade |
|---|---|
| ≥ 0.930 | PASS-CHAIN: the chain's own 0.90 is witnessed, mid holds |
| ≥ 0.713 | PASS-DESIGN: the critical design basis holds |
| 0.667–0.713 | UNDECIDED: inside the uncertainty band, neither a pass nor a fail; the pilot runs on |
| < 0.667 | FAIL: the salt-block fallback (Helios-2) is the route; the first module is not ordered |

1,000 on-sun hours before grading, the last 500 graded. The record is G3P3-USA's >250 h.

## What each result costs upstream

Each measured figure is turned into a field factor against each case's **own** rec link, since
mid carries the chain's 0.90 and critical already carries 0.690, and priced through `hourly3.py`:

| measured η | grade | mid field × | +$/MWh | critical field × | +$/MWh |
|---|---|---|---|---|---|
| 0.90 | PASS-DESIGN | 1.00 | 0 | 0.77 | −15 |
| 0.80 | PASS-DESIGN | 1.12 | 4 | 0.86 | −9 |
| 0.75 | PASS-DESIGN | 1.20 | 7 | 0.92 | −5 |
| 0.70 | UNDECIDED | 1.29 | 10 | 0.99 | −1 |
| 0.65 | FAIL | 1.38 | 13 | 1.06 | 4 |
| 0.60 | FAIL | 1.50 | 17 | 1.15 | 10 |

A pass at the design basis costs the critical design nothing, and anything above it is a saving the
design was held pessimistic against. That is what holding the design to critical buys: the pilot can
only relieve it.

## Cost and time

The pilot tranche in `titleone.py`: **2031–2033, $71 M**, run in parallel with the first node's
field; the first module waits on measurement 1.

## What is assumed

The hours, the uncertainty budget, the wind envelope and the two widths are protocol constants,
marked ASSUMED in the source. The pass mark is not assumed: it is `receiver.py`'s critical figure
and the chain's link, which the design already rests on. Two stale figures were corrected in passing:
`studies.py`'s receiver row carried the pre-review 0.795 and a 30 m critical curtain, and `CLAUDE.md`'s
critical-chain sentence the same 0.795; both now read 0.690 and 60 m.
