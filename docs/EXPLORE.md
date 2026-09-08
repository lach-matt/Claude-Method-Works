# EXPLORE.md — the design space, searched rather than evaluated

`python3 tools/explore.py` · `--selftest` · stdlib only

## Why it exists

Every other instrument here takes a configuration and returns its balance. `powersource.py` inverts
that once — it sets the balance to unity and returns the configuration. **Neither of them searches**,
and until something did, "how many redesigns does this plant need before it is optimal" had no answer
here at all: not a hard one, an absent one.

## The objective, and why it is the right single one

**Beam MW to serve the baseline million households.** Lower is better.

- the households are **fixed** by the objective the project was given, so what varies is what it costs
  to serve them;
- the beam is what every criterion runs through — the accelerator is the capital, the recirculated
  electricity, the driver count, the standby, and the reason for the 8 GeV;
- `startcost.py`'s two dominant build items are the driver and its shield, so build energy follows the
  beam rather than opposing it.

Where an axis's cost does **not** run through the beam — the stopping window's tritium, the module
count's buildability — that is stated beside its row rather than folded into a score. **A single
number that hides a trade is worse than two numbers that show it.**

## The statuses, and they are not degrees of the same thing

| status | meaning |
|---|---|
| `PHYSICS` | closed by a fact about matter. Not an axis at all. |
| `DECIDED` | open in principle, closed by a recorded decision |
| `DESIGN` | a free engineering choice — **the only kind a redesign can move** |
| `ASSUMED` | a constant carrying that status in its own file |
| `UNMEASURED` | a band nothing in this work has measured |

## What one axis at a time says

| axis | status | swing | range of beam MW |
|---|---|---:|---|
| multiplication k | DECIDED | **10.48×** | 240 → 2,515 |
| accelerator efficiency | DESIGN | **2.00×** | 185 → 370 |
| driver power | ASSUMED | **1.81×** | 240 → 435 |
| muon channel | DECIDED | 1.15× | 240 → 275 |
| stopping window | DESIGN | 1.14× | 210 → 240 |
| driver standby | ~~UNMEASURED~~ **SOURCED** | 1.02× | 250 → 255 |
| module power | DESIGN | 1.02× | 236.3 → 240 |

**One axis dominates and it is closed** — not by physics, by a decision on the record. The next two are
an engineering choice and a constant nobody has measured, and **nothing else moves the answer by more
than fifteen percent.**

## And the ranking's own limit is the second reading

One axis at a time cannot see an interaction. Every pair is **scanned**, not asserted about — and the
ranking above is not merely incomplete, it is **optimistic**:

| pair | singles | both at once | vs product |
|---|---|---:|---:|
| k × accelerator efficiency | 10.48, 2.00 | **no closure** | unbounded |
| k × driver power | 10.48, 1.81 | **no closure** | unbounded |
| accelerator efficiency × driver power | 2.00, 1.81 | **no closure** | unbounded |
| driver power × driver standby | 1.81, 1.02 | **no closure** | unbounded |
| k × muon channel | 10.48, 1.15 | 27.90× | 2.32× |

**Three pairs take the plant to no closure at all**, each pairing one large axis with another. The
design point is not near one cliff — it is near several, and the one-at-a-time table understates every
one of them. (Pairs are also not a full search: a triple could be worse still, and the file says so.)

## The cliff in multiplication

Nothing here had stated it:

```
the plant closes only above   k = 0.777
the design runs at            k = 0.900
the whole design lives in the last 0.123 of multiplication
```

| k | beam MW |
|---:|---:|
| 0.780 | 20,420 |
| 0.800 | 2,515 |
| 0.850 | 600 |
| 0.875 | 370 |
| **0.900** | **240** |

**Elasticity at the point: −16.7.** A one percent fall in k costs about seventeen percent more beam,
and the curve steepens the whole way down. The closure floor is consistent with `--plant`'s loop
requirement, which is met at k = 0.756: the station criterion is stricter because it also carries the
standby, the dry cooling and a net delivery.

## Redesign against measurement

| | |
|---|---|
| **REDESIGN CEILING** | **165.4 MW** against 240 — a factor of **1.45** |
| | every DESIGN axis at its best at once: `eta_acc=0.5, module_mw=0.78, window=400` |
| **MEASUREMENT EXPOSURE** | **4,620 MW** — a factor of **19.2** the other way |
| | every ASSUMED and UNMEASURED axis at its worst: `linac_mw=1.4, standby_kw=2000` |

Redesigning everything open to redesign is worth **1.45×**. Being wrong about the constants nobody has
measured was worth **19.2×** when this file was written, and with the accelerator efficiency at the low
end of its own *sourced* band as well, **the plant does not close at all**.

**One of the three measurements has since been made.** `powersource --standby` takes two published
cryoplants and the driver standby moved from `UNMEASURED` to `SOURCED`; it is no longer counted as
exposure, because a measured term is not exposure. The one-at-a-time exposure fell from **19.2× to
1.81×**.

**But it did not vanish — it changed kind.** In the pair table, driver power against the *measured*
standby is now **no closure**: a station built out of drivers of the largest class ever operated does
not work — not "is expensive", does not work — and that is now a fact about cryoplants rather than a
fear about an assumption. **The soft unknown became a hard requirement**, which is what measuring
something does, and is why it is worth doing first.

**A design space is not explored by iterating over the first while the second is open.** That is not a
counsel of patience — it is that the iteration would be measuring the assumptions with a plant, which
is the most expensive instrument anyone has ever proposed for the job.

## The refusal, and what replaces it

**This file reports no optimum.** An optimum over a space whose largest free swing is an unmeasured
constant is a statement about the constant. What it reports is **the order to work in**, and the order
is not the designer's instinct:

1. ~~**The standby scaling law.**~~ **MADE** — see `docs/POWERSOURCE.md` `--standby`. It decided
   exactly what it was expected to decide: a station of machines that exist is **not** possible.
2. **The wall-plug-to-beam efficiency** at this power, measured rather than banded. Worth 2.0× on its
   own and the largest genuinely *open* axis in the table.
3. **The transport calculation** on the fissile fraction, which is what actually places k. The
   one-group model is worth about fifteen percent on an absolute k, and at an elasticity of −17 that
   fifteen percent is the plant.

**Only after those three is a redesign a design decision rather than a guess about a measurement.**

## What the selftest pins

That the design point reproduces `powersource`'s own re-scaled station; that k is the dominant axis
*and* is DECIDED, so its swing is not available; that module power, window and route are all under
1.2×; that the closure floor exists, sits close below the design point, and the objective diverges as
it is approached; that redesign buys less than 2× while the owed axes cost more than an order of
magnitude more; that every pair is scanned rather than asserted about and that the pairs reaching no
closure all pair two of the three largest axes; and that the report states it reports no optimum.
