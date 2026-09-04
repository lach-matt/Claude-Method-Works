# F82.2 — THE TARGET-NODE SEARCH CANNOT REPRESENT A RYDBERG CHANNEL.
# THE REFUSAL AT 7d AND 8d IS A PROPERTY OF THE MATCHING CRITERION, NOT OF THE SPECTRUM.
# RAISED AGAINST refine79 / de80 / de81 / conf82 — THE WHOLE TARGET-NODE LINE, INCLUDING
# THIS SESSION'S OWN INSTRUMENT.

## WHAT IS ESTABLISHED, BY MEASUREMENT
1. The probe's field carries an exact Coulomb tail: **q_eff = −r·V = 1.000000** from
   r = 20 a₀ to r = 298 a₀. **A −1/r tail admits an infinite Rydberg series in every ℓ.**
2. The grid reaches **r_max = 300 a₀** with 4000 points and is not the limitation.
3. The node census over [−0.700, −0.0002] Ha is **monotone and skips no value**, climbing
   nd = 3 → 16. **The states are there.** The 4-node region spans 86 scan points and the
   5-node region 66.
4. **The matching function f = log(nrm) crosses zero EXACTLY ONCE in the entire l=2
   channel — at 6d — and is POSITIVE AND RISING at every energy above it**, +3.15 at the
   top of the nd=3 region climbing to +8.49 at threshold.

## THE FAULT
**THE SEARCH LOOKS FOR f = 0 INSIDE A TARGET-NODE WINDOW. ABOVE THE VALENCE STATE, f
NEVER RETURNS TO ZERO.** So every channel shallower than the valence eigenvalue is
invisible to this instrument by construction, no matter how wide the window, how fine the
scan, or how converged the field.
**s81 WIDENED THE WINDOW 80x AND RE-RAN BOTH BRANCHES. IT COULD NEVER HAVE WORKED**, and
the four refusals it recorded were four measurements of the same structural fact.
**THIS SESSION'S OWN conf82 INHERITS THE FAULT.** The census was built to be more
informative than a hit, and it was — it is what exposed the fault — but its zero-finder
is de80's `fine()` logic and is subject to the same limit.

## WHY IT WAS NOT SEEN FOR THREE SESSIONS
Because **the control always passed.** 6d is recovered exactly, to nine digits, at the
converged field and at the fallback iteration alike. **A control drawn from the valence
state cannot detect a fault that begins above the valence state.** Every can-fail in
refine79, de80, de81 and conf82 used a channel the instrument CAN see.
**THIS IS R82.1's LESSON ARRIVING FROM THE OTHER DIRECTION, ON THE SAME DAY.** R82.1 was
adopted this session for corpus scanners: a suite drawn from the instrument's own
assumptions shares its blind spots. **F82.2 is the physical version of exactly that.**

## THE SPECIES
F80.3 asked whether an instrument could see what it claimed. F82.1 asked whether the test
proving it could see was drawn from the same picture that made it blind.
**F82.2: THE CONTROL WAS DRAWN FROM THE REGION WHERE THE INSTRUMENT WORKS.**
Ninth appearance in five sessions.

## SEVERITY — BOUNDED, AND THE BOUND IS ARGUED NOT ASSERTED
**NO ORDERING, NO ENTRANT AND NO SEALED ROW IS DISTURBED.** The ranking currency is dE, a
total-energy difference. The channels this fault hides are, by construction, the LEAST
bound in their ℓ — Rydberg states converging on threshold. **A least-bound channel cannot
be an entrant at any Z.** The fault hides exactly the states that can never win.
**WHAT IT DOES COST:** every sentence of the form "channel X does not exist in this field"
that the project has written or might write. **There are no such sentences in the sealed
record** — s79 raised, s80 recovered three f channels, s81 refused to write absence and M
ruled CLASS B. **M's R81.6 ruling is what prevented this fault from entering the record,
and it was made before the fault was known.**

## WHAT IS OWED — FOR M's RULING, NOT ADOPTED HERE
1. **7d AND 8d STAY CLASS B PERMANENTLY UNDER THIS INSTRUMENT.** R81.6 cannot be
   discharged by widening, re-converging or re-branching. It needs a different criterion.
2. **A CANDIDATE REPAIR, UNTESTED:** a bound-state criterion that matches the log-derivative
   at a turning point against an inward-integrated solution from r_max, rather than
   requiring f = 0 outward. Whether t7e_probe can express that is unknown and unmeasured.
3. **PROPOSED, EXTENDING R82.1 TO PHYSICAL INSTRUMENTS:** *a control must be drawn from
   the region where the instrument is DOUBTED, not the region where it is trusted.* If no
   such control can be constructed, that fact is itself the finding and is recorded.
