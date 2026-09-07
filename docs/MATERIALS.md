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
