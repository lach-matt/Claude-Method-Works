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
| then | liquefied **on site** (nitrogen is 78 % of the air here) at **8.1 kW**, 0.00071 % of net. That closed the gate line by **adding a plant**. |
| now | **DELETED.** The shields run on the helium cryoplant at **45 K**, as the reference machine's do. One fewer fluid, one fewer plant, one fewer inventory. **A supply line is better removed than fed.** |

**Two things had to be computed before that was a design change rather than a preference.**

**The row was never a cooling duty.** Run 200 t/yr back through nitrogen's latent heat and it is
**1,261 W**. The reference machine's shield load is **10.8 kW**. A figure three orders below the duty
it names could only ever have been **makeup on a loop already closed** — so *"the one utility feed"*
was leakage top-up, and **the shield heat itself had never been in the inventory at all**. It is in
the cryoplant, and the cryoplant is in `powersource --standby`, **which had to be corrected for it**.

**And 77 K loses to 45 K, which is not obvious.** Nitrogen is the cheaper refrigerant per watt — about
half what 45 K costs — but a hotter shield radiates at the cold mass, radiation goes as T⁴, and a watt
at 2 K costs some fifty times a watt at 45 K. The two trade exactly when **0.88 %** of the 2 K load is
shield radiation, and in any real cryomodule it is more than that. **The answer is a break-even rather
than a preference**, and helium wins.

**Salt-processing reagents, for fission-product removal.**

| | |
|---|---|
| was | *"the reagents the salt's fission-product removal consumes"* — named, never specified, and therefore never priced |
| now | specified **electrical**: helium sparge on the recirculating inventory, noble metals plated out, **vacuum distillation** for the alkali and alkaline-earth chlorides, **electrowinning** for the lanthanides, any chemical reductant regenerated electrolytically on site |
| cost | **bounded at 0.15 MW — 0.013 % of net** — and the bound is deliberately absurd: it distils the *whole* 505 t inventory three times a year, where a real cleanup takes a slipstream |

**A bound is computed because the process is not this file's to choose**, and if the bound is
negligible the choice does not have to be made to proceed.

**One line was deleted and the other became electricity, which the plant makes.** What is left of the
two is **0.15 MW against 1,141 MW net — 0.013 %** — so nothing else in the plant moves. The nitrogen's
own cost is not in that figure **because there is no nitrogen**: the shield heat it was carrying is
inside the cryoplant, where it always was and where it is now counted.

### What remains, read from the inventory rather than remembered

| class | zone | item |
|---|---|---|
| REPLACED | blanket | fission-product removal, salt side |
| REPLACED | conversion | krypton-85 capture, cryogenic charcoal |

**Two rows, and both are parts.** No material stream arrives at the gate any more — not fuel, not
fertile, not tritium, not lithium, not coolant, not reagent, not cryogen. **The criterion now holds on
every material stream and fails only on replacement parts.**

### And "fails on parts" was itself wrong — a category error, corrected

**A part is designed to spec and built to meet the mathematics.** It is the *output* of the
engineering phase, not an input the plant needs, and the criterion asks whether the thing needs
**feeding**. A specification is not a feed. Calling it a failure treated the next phase's deliverable
as this phase's shortfall.

**What the question survives as is sharper and answerable: a part is made of something.** So the test
is not *"is it a part"* — it is **what materials does the parts stream consume, and are they
ordinary?**

| | item | materials |
|---|---|---|
| ordinary | fission-product removal | nickel alloy vessel, graphite and refractory-metal electrodes, ordinary vacuum plant |
| **NOT ordinary** | fission-product removal | **Cl-37** leaving with the removed products, unless the waste form returns it |
| ordinary | krypton-85 capture | activated charcoal, **regenerated by warming rather than consumed**; steel cylinders for the gas |

Steel, nickel alloy, graphite and electrode stock are **ordinary**, and no criterion about a plant's
self-sufficiency was written to exclude the existence of industry.

### The one material that is not ordinary hides in the process, not the part

Fission products live in the salt as chlorides and leave as chlorides, and **every atom of that
chlorine is Cl-37 enriched** — the second long-lead purchase in the whole plant.

| | |
|---|---:|
| bound on Cl-37 leaving | **592 kg/yr** |
| against an inventory of | 184 t |
| which is | **0.322 % a year, 12.9 % over the life** |

The inventory is the row as it stands, which `fuelchoice.py` found **understates** it — the row counts
the NaCl portion and misses the three Cl per U in UCl₃, so the true holding is nearer 219 t. Using the
smaller figure makes the share an **over-estimate**, which is the direction a bound should err in.

**That is a bound and not a process figure**, and the difference is the whole of its honesty. Each
fission destroys one PuCl₃ and frees three chlorines; charge conservation caps what the two fission
products can carry out near what the parent held. The actual figure needs their valence distribution
and the process holdup, and this file computes neither.

**And the electrical route already returns it**, which is the second reason to have specified it.
Electrowinning deposits the lanthanide as *metal* at the cathode and evolves chlorine at the anode,
which goes back to the salt; distillation returns the salt with its chlorine in it. **A chloride waste
form carries the chlorine out of the building. An oxide waste form, or metal, leaves it behind.**

> **REQUIREMENT 4** — the waste form shall return chlorine to the salt. Unmet, it is a **592 kg/yr**
> Cl-37 line and **13 %** of the inventory over the life. Met, criterion 3 closes on materials with
> nothing left over.

**That is exactly the kind of thing the engineering-materials phase settles**, and stating it as a
requirement is what this phase owes that one. The residue is not a gap in the design; it is a line in
the next specification.

### Where criterion 3 stands

| | |
|---|---|
| **material input** | none. Closed. |
| **energy input** | none after start-up. Closed. |
| **parts** | ordinary materials, specified downstream |
| **the one condition** | Requirement 4, on the waste form |

Read literally — *no input of anything* — the criterion still cannot be met by any physical object,
because a machine that never needs a spare part is not a machine. Read as it was plainly meant — no
fuel, no feedstock, no consumable — **it is met, conditional on Requirement 4.** That is a stronger
statement than this file made a pass ago, and it is earned by arithmetic rather than by wording: the
criterion was not reworded, **the design was changed and then the residue was computed instead of
shrugged at.**

### A numbering error corrected in the same pass

This file adjudicated **"criterion 4"** throughout — the number it carried before 'cold' was dropped
as criterion 1 and everything below moved up. `OBJECTIVE.md`'s table is authoritative and the file now
agrees with it. **The verdict never changed, only the label on it**, and the mismatch is recorded
rather than silently corrected because *a criterion referenced by a number nobody can check* is
exactly what `OBJECTIVE.md` exists to stop. The selftest now asserts the file says "criterion 3" and
nowhere says "criterion 4".
