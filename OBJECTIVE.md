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
| 8 | **Restartable quickly after shutdown** | `restart.py` — **being built** |
| 9 | **Cheap to start**, and a tremendous output making it long-term sustainable | `startcost.py` — **being built** |

**Two decisions taken by the author, recorded here so that neither is re-argued and neither is
forgotten:** 'cold' is dropped from the objective (above), and **criteria 8 and 9 are adjudicated by
new instruments before phase 4 is drafted** rather than carried into the paper as open items. A paper
that states a criterion it cannot support is the failure mode this whole harness exists to prevent.

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
