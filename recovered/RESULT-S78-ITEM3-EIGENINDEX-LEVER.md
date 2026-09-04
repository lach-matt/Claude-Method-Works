# RESULT S78 — ITEM 3. THE EIGENINDEX LEVER IS LIVE, AND THE BRACKET SEARCH IS BRITTLE.
# Prediction sha256 fad25b628a1d92fea64b3c8364c80dc103a9fc49e614f53ed11cf3ff6ada4c73, filed first.

## WHERE k LIVES — READ FROM SOURCE BEFORE ANYTHING WAS RUN
t7c_hfsr.solve_one selects NO eigenvalue by index. With exchange present it seeds a
bracket from `eh = eigen_sr(Vf, l, n, 1.0, self.Z, c, ...)` and then **BISECTS TO A ZERO OF
log(nrm)**. The node count is computed, returned, and checked by the CALLER at hfc2.py:55.
**The eigenindex is therefore implicit and post hoc: the solver hunts a zero, and the node
count VERIFIES afterwards which state it found.** `n` is passed POSITIONALLY, so a default
patch is dead — F54.2 exactly — and the poison wraps the module-level name.

## LEVER 1 — INTEGER POISON, n -> n±1.  VERDICT: LIVE
| run | result | eigen_sr calls |
|---|---|---|
| clean | E = **-601.378794570 Ha**, it=30 | 150 |
| n -> n+1 | **RAISED `RuntimeError: Z=19 10 nodes 1`** | 1 |
| n -> n-1 | RAISED `TypeError: 'NoneType' object is not subscriptable` | 1 |
**K1 CORRECT** — the wrapper is reached, 150 times in a clean run.
**K2 CORRECT, AND IN ITS EXACT PREDICTED MECHANISM** — the raise is a node-count raise
from hfc2.py:55, `1s` returning ONE node because the bracket was seeded at n=2.
**K3 CORRECT IN VERDICT, DEGENERATE IN MECHANISM, AND RECORDED AS SUCH** — n-1 sends the
1s solve to n=0, which is unphysical; eigen_sr returns None. That the output moved is true
and uninformative.

## LEVER 2 — CONTINUOUS PERTURBATION OF THE BRACKET SEED, eh -> eh*(1+d)
| d | E (Ha) | dE vs d=0 |
|---|---|---|
| 0 | -601.378794569654 | — |
| 1e-3 | -601.378794569659 | **-5.57e-12 Ha** |
| **1e-2** | **RAISED `TypeError`** | **—** |
| 5e-2 | -601.378794569620 | **+3.39e-11 Ha** |
**THE CONVERGED ENERGY IS INDEPENDENT OF THE BRACKET SEED TO ~1e-11 Ha.** A 5% displacement
of the seed moves the answer by 34 picohartree. **The converged answer is a function of the
ZERO, not of the seed that found it.** That is the robustness statement Rung B needs, and
it is the first time it has been measured rather than assumed.

## F78.2 RAISED — THE BRACKET SEARCH FAILS NON-MONOTONICALLY. SEVERITY: STRUCTURAL LEAD.
**d = 0.01 RAISES WHERE d = 0.001 AND d = 0.05 BOTH SUCCEED.** The failure is not a
threshold; it is a hole. Its mechanism is visible in solve_one: when the expansion loop
never finds a sign change in log(nrm), `g()` returns None, `best` stays None, and the last
line executes `best=(mid,rm[1])` on `rm = None`. **`TypeError: 'NoneType' object is not
subscriptable` IS THE SIGNATURE OF A FAILED BRACKET EXPANSION, and it is the same
exception the n-1 poison produced.**
**WHY THIS MATTERS MORE THAN THE LEVER TEST DID.** s77 classified the five non-converging
channels at Z=89 as CLASS B — *the target node count IS attained in the field; the shooting
fails to find it* — and observed that the three f channels return minlog -6.53/-6.01/-5.45,
within e^-6 of a findable zero. **F78.2 supplies a MECHANISM for exactly that: the zero is
there and the bracket expansion does not reach it.** A hole that opens at d=0.01 and closes
again at d=0.05 is a search failure, not a spectral fact.
**THIS IS A LEAD AND NOT A RESULT. It has been demonstrated at Z=19 under a deliberate
perturbation. It has NOT been shown to be the mechanism at Z=89, and showing that is work.**

## WHAT ITEM 3 HAS AND HAS NOT DELIVERED
**HAS: the lever is LIVE and is now verified in F54.2's shape before anything is built on
it.** The quantity Rung B would vary is a live input, and the converged answer does not
depend on how the zero was located.
**HAS NOT: Rung B IS NOT BUILT.** A PASS on a lever test is permission to build, not a build.