# `tools/materials.py` — the bill of materials, and criterion 4 adjudicated

Phase 2 of the build. Every material the reference plant needs, how much of it, how it is
stored, and — the column that decides the project's fourth criterion — whether it has to be
delivered to the site.

## What it refuses to do

It never restates a quantity another instrument holds. The solenoid's cold mass and conductor
grading, the cell's radius, depth, pressure and temperature, the tritium holding, the neutron
budget and the burnup are **imported** from `machine.py`, `collector.py` and `powersource.py`.
Its selftest asserts the imports match to the last digit, so the bill cannot drift from the
design while still looking finished.

## Two columns, and neither is ever flattened

Each row carries a **status** — `DERIVED`, `IMPORTED`, `SOURCED`, `SCALED`, `ASSUMED`,
`REQUIREMENT` — and a **supply class**: `FIRST-CHARGE`, `BRED`, `STOCKPILED`, `REPLACED`,
`CIRCULATING`, `PRODUCED`. A `REQUIREMENT` is a number the plant needs that this work does not
compute; it is stated so a measurement can refuse it, not so a reader can trust it. The selftest
fails any row carrying neither column.

## The blanket is forced, not chosen

`powersource.py`'s neutron budget is not neutral about chemistry, and three of its own numbers
each exclude a family of designs:

- **ν = 2.9 is Pu-239 *fast***. A thermal spectrum does not reach the required `f_b = 0.4872`
  on the U–Pu cycle. No graphite, no FLiBe.
- **L = 0.20 covers leakage, structure, coolant *and fission products*, for forty years.** A
  solid-fuel core accumulates fission-product capture monotonically and would eat that budget,
  so the fuel must be **liquid** and the products must leave continuously.
- **A liquid fast fuel salt is a chloride**, and Cl-35(n,p)S-35 is both a parasitic absorption
  the budget cannot afford and a sulphur source that attacks the loop. The design therefore
  specifies **Cl-37**, on sourced chloride-reactor practice; this work does not compute the
  penalty of not doing so, and that is a `REQUIREMENT`.

So: **NaCl–UCl₃** fuel salt with a **Pb–15.7Li** breeding and reflecting zone at 90 % ⁶Li — Pb–Li
over a lithium salt because it *multiplies* as it breeds and returns part of `L` as a reflector.

## The distinction the inventory hides

The first charge holds **17.9 t** of heavy metal (at 7 MW; it scales with the plant) and the
plant fissions a quarter of it in forty years. **On mass the charge outlasts the plant and
breeding looks optional.** What runs out is not mass but **reactivity**: at first order `k` falls
with the fissile density, and with it the gain — from 42.70 to 6.4. **Breeding holds `k`, not the
inventory**, and that is the whole of why `f_b` is a requirement. The selftest asserts both halves,
because either alone is misleading.

## Criterion 4, as it actually resolves

`--supply` groups every row by supply class and adjudicates. Fissile and tritium are both `BRED`,
by independent arguments. **⁶Li is the only material genuinely consumed** — a few hundred grams a
year against a holding of over a tonne, so a couple of percent over the life: a first charge and
not a delivery. What does arrive at the gate for ever is nitrogen, one beryllium window a year,
and the salt-processing reagents; what leaves is fission products.

**The criterion holds on fuel and fails on consumables and parts.** That is stated rather than
flattened. The theorem's own floor — `P·t ≤ Mc²` — puts the mass actually converted at a few
kilogrammes over the life, and every other row is bookkeeping around it.

## Running it

```
python3 tools/materials.py            the bill of materials
python3 tools/materials.py --storage  the storage schedule
python3 tools/materials.py --supply   criterion 4, row by row
python3 tools/materials.py --selftest
```

Stdlib only. It imports `powersource.py`, `machine.py` and `collector.py` by path, and the
acceptance integrals behind those are memoised — without that the report takes minutes.

## `--fertile` — the ladder below the tails, and the rung that does not substitute

`--uranium` asks whether there is enough. This asks what comes after, and then the question that is
usually skipped: **a resource is not a fuel until the neutron budget says so.**

| resource | tonnes | station-lifetimes |
|---|---:|---:|
| enrichment tails (DU), world | 1.6 × 10⁶ | 31,365 |
| spent LWR fuel, heavy metal | 4.0 × 10⁵ | 7,841 |
| identified natural uranium | 8.0 × 10⁶ | 156,825 |
| thorium, identified resources | 6.4 × 10⁶ | 125,460 |
| uranium in seawater | 4.5 × 10⁹ | 88,213,811 |

**The first three rungs are the same fuel.** Tails, spent fuel and natural uranium are all U-238
with different amounts of U-235 attached, and the design does not care which — it burns the U-238.
Nothing changes but the provenance, and the first two are *wastes*, so the environmental case
survives them.

**The fourth rung is a different fuel and it does not simply substitute.** Thorium breeds U-233,
which fissions at ν = 2.50 against Pu-239's 2.90, and the whole neutron budget is built on that
number. It costs twice over — fission takes more of the budget *and* `f_b = k/(ν−k)` rises from
0.4872 to 0.6129 — so what is left for ⁶Li shrinks from 2.897 to **0.800** per source neutron at the
loose leakage allowance, against a tritium demand of 1.373. **Thorium closes at L = 0.10 with 1.427
to spare and fails at L = 0.20 by 0.573.**

So the thorium fallback is **conditional**, and the condition is the one term this work has never
measured. On uranium the leakage band decides nothing; **on thorium it decides whether the fuel
works.**

And one route makes the question go away: a cell that makes its own tritium from deuterium
(`window.py --fuels`) demands essentially no ⁶Li, and thorium then closes on both budgets. **The fuel
question and the fertile question turn out to be the same question.**

## `--criterion3` — closing it, by changing the plant rather than the sentence

Criterion 3 asks for **no input of anything beyond the initial ignition**. `--supply`'s verdict was
that it *"holds on fuel and fails on consumables and parts"*. **The consumables half was a design
choice rather than a law**, and this is the pass that changed the design.

### What arrived at the gate before, and what replaces it

**Liquid nitrogen, for the cryogenic shields.**

| | |
|---|---|
| was | **200 t/yr** in a tanker — the file called it *"the one utility feed"* |
| now | liquefied **on site**. Nitrogen is 78 % of the air here, so the shield circuit runs **closed** and the feedstock is the atmosphere, which is not a delivery. |
| cost | **8.1 kW** at a sourced **0.357 kWh/kg** — **0.00071 %** of net output. At the pessimistic 2.56 kWh/kg, 0.0051 %. |

**Salt-processing reagents, for fission-product removal.**

| | |
|---|---|
| was | *"the reagents the salt's fission-product removal consumes"* — named, never specified, and therefore never priced |
| now | specified **electrical**: helium sparge on the recirculating inventory, noble metals plated out, **vacuum distillation** for the alkali and alkaline-earth chlorides, **electrowinning** for the lanthanides, any chemical reductant regenerated electrolytically on site |
| cost | **bounded at 0.15 MW — 0.013 % of net** — and the bound is deliberately absurd: it distils the *whole* 505 t inventory three times a year, where a real cleanup takes a slipstream |

**A bound is computed because the process is not this file's to choose**, and if the bound is
negligible the choice does not have to be made to proceed.

**A chemical line becomes an electricity line, and the plant makes electricity.** Together the two
draw **0.16 MW against 1,141 MW net — 0.0137 %** — so nothing else in the plant moves.

### What remains, read from the inventory rather than remembered

| class | zone | item |
|---|---|---|
| REPLACED | blanket | fission-product removal, salt side |
| REPLACED | conversion | krypton-85 capture, cryogenic charcoal |

**Two rows, and both are parts.** No material stream arrives at the gate any more — not fuel, not
fertile, not tritium, not lithium, not coolant, not reagent, not cryogen. **The criterion now holds on
every material stream and fails only on replacement parts.**

### The pass is not claimed complete, and the difference matters

What was *"fails on consumables and parts"* is now *"fails on parts"*. The consumables were a design
choice and were designed out. **The parts are not a design choice**: pumps have seals, heat exchangers
foul, electrodes erode, and the fission-product removal system — still the single most demanding
unbuilt item here — will have a service life.

| | |
|---|---|
| **material input** | none. Closed. |
| **energy input** | none after start-up. Closed. |
| **parts** | a supply line inward, for ever, and no machine ever built has escaped one |

**A decision is owed and it is not this file's to take.** Read literally — *no input of anything* —
the criterion cannot be met by any physical object, because parts wear. Read as it was plainly meant —
no fuel, no feedstock, no consumable — **it is now met**. Which reading governs is the author's, and
rewording a criterion so a design passes it is the one move this project forbids. **The design was
changed; the criterion was not**, and both readings are stated so the choice is visible rather than
assumed.

### A numbering error corrected in the same pass

This file adjudicated **"criterion 4"** throughout — the number it carried before 'cold' was dropped
as criterion 1 and everything below moved up. `OBJECTIVE.md`'s table is authoritative and the file now
agrees with it. **The verdict never changed, only the label on it**, and the mismatch is recorded
rather than silently corrected because *a criterion referenced by a number nobody can check* is
exactly what `OBJECTIVE.md` exists to stop. The selftest now asserts the file says "criterion 3" and
nowhere says "criterion 4".
