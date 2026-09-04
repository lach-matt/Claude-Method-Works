# PREDICTION — SESSION 82, ITEM 4. R81.6: CONFIRM 7d AND 8d AT THE CONVERGED FIELD.
# FILED BEFORE THE INSTRUMENT EXISTS AND BEFORE ANY Z=89 CONVERGED-FIELD NUMBER IS READ.

## THE CONSTRUCTION, DECLARED BEFORE IT IS BUILT
R81.6 asks for the search repeated against the CONVERGED field rather than the field at
the iteration where de80's fallback fires. **For 7d and 8d no converged SCF exists** —
the channel the SCF would need is the one being searched for. So the converged field must
be borrowed from the row that DOES converge:
  1. converge Z=89 cfg88+6d, **restarted to stationarity (R81.2)**;
  2. freeze the core with the entrant occupancy reduced by one (fixed81's E6/E7), so the
     probe sees 88 electrons against Z=89 — **net tail −1/r**;
  3. scan the l=2 channel over the de81 window and take a **NODE CENSUS**, not merely a
     target-node hit: record nd at every scan energy.
A census answers a question a hit cannot: whether the d ladder TERMINATES at 3 nodes or
whether 4 exists and was missed.

## THE OBJECTION THAT MOTIVATES THIS FILE — STATED BEFORE MEASURING
**A −1/r TAIL ADMITS AN INFINITE RYDBERG SERIES IN EVERY ℓ.** With 88 electrons screening
Z=89 the probe's asymptotic potential is −1/r, so l=2 must carry 7d, 8d, 9d ... converging
on threshold. With a modest quantum defect 7d sits near **−1/(2·6.5²) ≈ −11.8 mHa** and 8d
near **−1/(2·7.5²) ≈ −8.9 mHa**. **BOTH LIE INSIDE de81's SEARCHED WINDOW [−1.99e−4,
−0.635] Ha, AND de81 FOUND NEITHER.** That is not a small discrepancy; it is a channel the
potential's own asymptotics require.
**THEREFORE ONE OF THREE THINGS IS TRUE, AND THE CENSUS DISTINGUISHES THEM:**
  H1 the field's tail is NOT −1/r for the probe (a convention — s79's E2 sets Vc = 0, and
     t7c_tail records that scf_pol_sr floors V at −q/r with q = 1);
  H2 the RADIAL GRID cannot represent the state: 7d has ⟨r⟩ of order 80 a₀, and if r_max
     is smaller the orbital is truncated and its outer node is never counted;
  H3 the physics genuinely terminates the d ladder at 6d in this field.
**H3 IS THE ONE de81's RESULT WAS WRITTEN AS THOUGH IT HAD ESTABLISHED, AND IT IS THE
LEAST LIKELY OF THE THREE.**

## CLAUSES

Y1 · **THE CAN-FAIL RECOVERS 6d AT THE CONVERGED FIELD.** The same census, target 3 nodes,
   returns a zero within **1 mHa** of the SCF's own eps(6d). Without this nothing else in
   the file is readable. (fixed81's analogous check at Z=90 was exact to nine digits, so
   1 mHa is a generous bound and I expect far better.)

Y2 · **THE NODE COUNT IS MONOTONE NON-DECREASING AS THE SCAN ENERGY RISES**, with no
   value skipped, until it saturates. A SKIPPED value is itself the finding: it would mean
   the counter, not the field, terminates the ladder.

Y3 · **THE CENSUS SATURATES AT nd = 3.** No energy in [−0.7, −2e−4] Ha returns nd = 4 or
   nd = 5. **de81's refusal is CONFIRMED at the converged field.** Predicted because the
   converged field differs from the fallback-iteration field by a small perturbation and
   de81's refusal was robust across two branches and an 80x window widening.

Y4 · **AND THE CAUSE IS H2, THE GRID — NOT H3, THE PHYSICS.** r_max is predicted to be
   **between 40 and 120 a₀**, too small to carry a state whose ⟨r⟩ is ~80 a₀. **THIS IS
   THE CLAUSE WITH THE CONTENT AND THE ONE I EXPECT TO BE ARGUED WITH.** If it holds, then
   "the d ladder terminates at 6d" is a statement about the grid and **MUST NOT** enter the
   Z=89 record as a statement about the spectrum.

Y5 · **THE 6d ORBITAL ITSELF IS COMFORTABLY INSIDE THE GRID** — its outer amplitude falls
   below 1e−6 of its peak well before r_max — so the grid is adequate for every SEALED
   quantity and this is a limitation of the SEARCH, not of the chain. Predicted, because
   if it failed the sealed rows would be in question and that is a far larger claim.

Y6 · **CONSEQUENCE FOR R81.6, EITHER WAY.** If Y3 and Y4 both hold, 7d and 8d are neither
   absent nor unreached but **OUTSIDE THE INSTRUMENT'S REPRESENTABLE SPACE**, which is a
   THIRD class and is not what CLASS B means. Predicted: **the honest verdict is that
   R81.6's confirmation CANNOT be completed by this construction**, and the Z=89 record
   gets a declared limitation rather than a result.

## WHAT IS NOT CLAIMED
This does not re-open the Z=89 entrant. 6d wins rank 1 by a total-energy margin of
m(89) = 32.332 mHa; a Rydberg 7d at ~−12 mHa in EIGENVALUE currency is not commensurable
with that and **must not be compared to it** (F79.2's species). **Nothing here can promote
7d to entrant.** What it can do is decide whether a sentence about absence is admissible.
