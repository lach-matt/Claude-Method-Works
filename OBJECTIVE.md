# The objective, and the criteria it sets

**This file is the authoritative statement of what the project is for.** It was
stated by the author and is recorded here verbatim. Before it existed, four
criteria were referenced *by number* in three instruments — `materials.py`
adjudicates "criterion 4", `powersource.py` calls stability "the project's third
criterion", `buildpackage.py` quotes the fourth as speaking of "an initial
ignition" — and **no file stated them.** That is how a paper comes to be graded
against criteria nobody can read. Nothing here is inferred; where the work does
not meet a criterion, that is recorded below rather than softened.

## The objective, verbatim

> Identify a 'cold' self sustaining power source that requires no input of
> anything beyond the initial ignition. Must be scaled for civilization,
> baseline 1 million households. Should also supply the power to ignite further
> stations. Be entirely environmentally friendly — mitigations to environmental
> problems are addressed upfront before design. Contain built in fail-safes and
> have the ability to be restarted quickly after a shutdown. Must be cheap to
> start but put out a tremendous amount of energy, which will make this a long
> term sustainable power source.

## The criteria, as that objective sets them

| # | criterion | where it is adjudicated |
|---|---|---|
| ~~1~~ | ~~**'Cold'**~~ — **DROPPED by the author, and the reason is recorded rather than the word quietly removed.** 'Cold' is *proved* in `Cold_Fusion_Proof_v1.0` for muon-catalysed fusion, where the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy. The plant this project now builds carries **no fusion channel**, so the word had nothing left to attach to, and redefining it at plant level would have been a second and different definition wearing the first one's name. The word retires to the proof paper where it is earned. **The criterion is now: clean, efficient, self-sustaining.** | *retired — see the proof paper* |
| 2 | **Self-sustaining** — runs its own drive from its own output | `powersource.py --plant` |
| 3 | **No input beyond the initial ignition** | `materials.py --supply` |
| 4 | **Scaled for civilization**, baseline 1,000,000 households | `powersource.py --station` |
| 5 | **Ignites further stations** from its own output | `powersource.py --ignition` |
| 6 | **Entirely environmentally friendly**, mitigated before design | `environment.py` |
| 7 | **Built-in fail-safes** | `powersource.py --stability` |
| 8 | **Restartable quickly after shutdown** | `restart.py` — **minutes held molten, 6 h drained**; the clock is thermal, not neutronic |
| 9 | **Cheap to start**, and a tremendous output making it long-term sustainable | `startcost.py` — **32-day energy payback, EROI 460:1**; measured in energy, not money |

**Two decisions taken by the author, recorded here so that neither is re-argued and neither is
forgotten:** 'cold' is dropped from the objective (above), and **criteria 8 and 9 are adjudicated by
new instruments before phase 4 is drafted** rather than carried into the paper as open items. A paper
that states a criterion it cannot support is the failure mode this whole harness exists to prevent.

## Decisions taken, with their reasons

A refused or adopted option with its reason is a decision; one without is a gap.

**The operating point is k = 0.900, not the field's 0.95, and it is adopted for
intrinsic criticality safety.** Below **7.93 %** fissile the fuel salt's `k_inf`
falls under one, and an assembly whose `k_inf` is under one cannot be made
critical by any amount in any shape. Holding the design there means **no
accumulation of fuel salt anywhere on site can ever be critical when dry** — the
hazard class stops existing rather than being managed by procedure, and the
property is a fact about the material rather than about the operator. The
subcritical margin doubles to 10,000 pcm. There is no intermediate: `k_eff` is
capped at 0.900 by the property itself.

**The price is 2.76× the driver** — 84 MW to 230 MW for the same million
households — because at lower multiplication more of the plant's own electricity
recirculates into its accelerators. It was quoted at 2.05× when the decision was
put, **corrected to 2.76× before implementation**, and re-confirmed at the true
figure. The reason given for paying it: *"it's what sells a new plant to a
community, in an age when plants and data centers are being rejected."*

**Re-scaling the station does not recover that cost, and the re-scale was
undertaken to test whether it could.** The module size was set by a *pion*
production target, which route C does not have; of the four constraints that
fixed it at 4 MW, three vanish with the muon channel and only the **spallation
target's power** survives. Re-scaling to an ESS-class 5 MW target takes the
module count from 58 to 46, and to 23 at a 10 MW target — but **the beam is
230 MW at every row**, because it is set by the multiplication and the module
size only decides how it is divided. Re-scaling buys buildability, not energy.

## The phases

1. Define the math in full and prove it.
2. Design concepts, material identification, storage requirements.
3. Facility build package.
4. Draft the proposal/paper.
5. Adversarial audits.

## Two rules this file inherits, and they govern everything above

**A status is never flattened.** Where a criterion is met on one term and failed
on another, both are stated. `materials.py` already says of criterion 3 that it
"holds ON FUEL and fails ON CONSUMABLES AND PARTS … and it is not what was asked
for" — that sentence stands, and no paper may quote the first half alone.

**A finding is recorded, never repaired.** A criterion that is not met is written
down as not met. It is the author's decision whether to relax the criterion,
change the design, or publish the shortfall; it is never the writer's to make by
choosing a kinder word.
