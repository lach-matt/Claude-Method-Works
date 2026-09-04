# F82.1 — THE FAULT DETECTOR COULD NOT SEE THE FAULT. THREE DRAFTS.
# RAISED AGAINST MY OWN INSTRUMENT, IN THE SESSION THAT WROTE IT, BEFORE ANY CLAUSE WAS
# SCORED. **THE THIRD DRAFT WAS NOT CAUGHT BY A GATE, AND THAT IS THE SERIOUS PART.**

## DRAFT 1 — THE TERMINATION-TEST DETECTOR COULD NOT PARSE A PAREN
`DIFFTEST` read `E2?\s*-\s*E\b`. Real source reads `done = float(E2) - E < 1e-10`: the
closing paren sits BETWEEN the operands. **CF1 — the synthetic file that COMMITS the
one-sided break — scored clean.** The can-fail halted the run at rc=4 before any tree
scan existed. **Caught by a gate. Working as designed.**

## DRAFT 2 — THE REPAIR CLAIMED BOTH OPERAND ORDERS AND HAD ONLY TESTED ONE
The paren-tolerant patch was written and, in the same breath, asserted that it also
caught the reversed form. **CF4 was added to demonstrate that claim rather than accept
it, and CF4 FALSIFIED IT**: `E - float(E2) > -1e-10` hides the operands behind a CALL,
not merely a paren. Patching the pattern a third time would have been guessing at the
next disguise, so the line is now NORMALISED — call wrappers and parens stripped — and
the test made on bare tokens. `abs(` is read on the ORIGINAL line, because the normaliser
would otherwise erase the very thing that makes a line innocent.
**Caught by a gate written specifically to attack my own repair.**

## DRAFT 3 — THE STRUCTURAL DETECTOR MISSED perturb80, AND NO GATE CAUGHT IT
`RESEED` read `\.P0\s*=`. perturb80 re-seeds ONLY as a tuple target —
`Perturbed.P0, Perturbed.EPS0 = h.P, h.eps` — where a comma sits between the attribute
and the `=`. **perturb80 was scored as carrying NO restart ladder.**
**AND perturb81 AND fixed81 WERE CAUGHT FOR THE WRONG REASON**: both happen to contain an
unrelated `Cls.P0 = None` reset line. The detector returned two of the three right
answers by accident.
**CONSEQUENCE, MEASURED.** X1 read **2** instead of 3, and X4 — the clause that decides
whether F81.1 is a naming fault or a numerical one — read **1 external consumer** instead
of 0, because the missing S3 file was reclassified as external to itself. **The headline
finding of the item was wrong in both directions at once.**

**HOW IT SURFACED, AND THIS IS WHY IT IS REGISTERED AT FULL SEVERITY.** Not by a gate.
By reading the count **2** against a file I had read by inspection an hour earlier and
knew carried a ladder. **The five can-fails as first written all passed on the broken
detector.** CF5 — the tuple-target re-seed as the SOLE re-seed — was written AFTER the
failure, to make the repair demonstrable and to make the next such miss catchable.
**A can-fail suite that passes a detector which misses a third of its targets is not a
can-fail suite; it is a set of examples the detector happened to be written against.**

## THE SPECIES, AND IT IS A NEW MEMBER OF IT
F78.1 read the raise, not the sentence. F79.1 read the instrument, not its column label.
F79.2 read the units. F80.1 read which zero it picked. F80.3 read whether the instrument
could see what it claimed. F81.1 read whether a direction was measured or assumed.
F81.4 read what the patch actually replaced.
**F82.1: THE INSTRUMENT'S CAN-FAILS WERE WRITTEN FROM THE INSTRUMENT'S OWN ASSUMPTIONS.**
F80.3 asked whether an instrument can see what it claims. **F82.1 asks the next question
down: whether the test that proves it can see was drawn from the same picture that made
it blind.** Eighth appearance in five sessions, and the first where the gate itself was
the thing at fault.

## WHAT IT CHANGES GOING FORWARD — PROPOSED, FOR M's RULING
**A CAN-FAIL MUST BE BUILT FROM A REAL SITE, NOT A SYNTHETIC ONE.** Every synthetic
can-fail in this instrument was written by me, from my own idea of what the fault looks
like, and my idea was wrong three times. The one thing that caught draft 3 was a REAL
file whose answer was known independently.
**PROPOSED STANDING RULE: any detector that scans the corpus must include, among its
can-fails, at least one REAL file whose verdict is established by inspection before the
detector runs — a positive control drawn from the corpus itself.**
This is not yet law. It is proposed to M.

## WHAT SURVIVES
The scored result stands: five can-fails pass against the repaired detector, both lint
directions are demonstrated, and X1/X2/X4 were re-measured after the repair. **No clause
in RESULT-S82-ITEM5 was scored against a broken detector**; the prediction sha gate held
across all three drafts and the prediction file was never touched.
