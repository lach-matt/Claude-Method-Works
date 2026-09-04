# SCORE — RUNGS 5, 9 AND THE MINIMAL RUNG-7 FLOOR, SESSION 62
# Prediction `pack61/PREDICTION-RUNG-5-9-7.md`
# sha256 bdc1e7052de800735074ce7106a20b72a728d64dad9a21d1d1b652a2777a15c5
# filed 17:45:09Z. First result read 17:45:56Z. VERIFY THE SHA BEFORE READING BELOW.
# Scope by M's ruling: EX-4 RETIRED. F61.1 re-walk DEFERRED. Rung 7 reduced to one number.

## RUNG 5 — `_ceff` IS **DERIVED**. CRITERION 4 HOLDS. **RUNG 5 CLOSES.**

### R5-1 the fractional branch is OFF, can-failed in three directions — **PASS**
    PHASE 1  ruling path (nlguard.run_guarded)   E = -601.378794570
             frac-branch calls = 0    default-branch calls = 310
    PHASE 2  frac FORCED ON at the 3p shell      E = -600.411645837
             frac-branch calls = 62   dE = +0.967148733 Ha
    PHASE 3  released                            E = -601.378794570  BIT-IDENTICAL
The branch executes zero times where it must not, executes 62 times when forced, moves the
answer by nearly a whole Hartree when it does, and leaves no residue when released. It
cannot be silently live and it is not vacuous (F59.3's signature is excluded).
Set at six sites archive-wide — drow_p, frachf, frachf_S, frachf_eps0, frachf_ring,
nodesplit — every one a fractional-occupation probe driver, none on the walk path.

### R5-2 the q=1 falsifier — **PASS, AND SHARPER THAN PREDICTED**
`_ceff` at q=1 returns **exactly 0.0**: a one-electron shell sees no other electron of its
own shell, so the derived value removes the self-repulsion completely, with no coefficient.
The consequence is checkable against a known exact answer:

    Z=1, the walk's own solver:     E = -0.500008079 Ha
    exact non-relativistic hydrogen:    -0.5
    difference:                         -8.08 microhartree
    analytic leading SR correction  -alpha^2 Z^4 / 8 = **-6.66 microhartree**

**The walk reproduces the exact hydrogen ground state, and the entire 8 microhartree by
which it misses is accounted for by the relativistic correction the field is supposed to
carry, to within 1.4 microhartree of grid.** Had `_ceff` returned `Q[a]` or any screening
value, Z=1 would have carried a spurious self-repulsion of order 0.3 Ha — a failure of
hundreds of milli-Hartree, with no parameter available to hide it.
**`_ceff` is DERIVED. There is no fitted or empirical quantity at Rung 5.**

## RUNG 9 — THE TRUNCATION. **PASS AT BOTH ROWS, WITH ONE HONEST CAVEAT.**

### R9-1 no excluded channel comes near winning — **PASS**
    Z=19  winner 4s at -0.14774.  5 channels excluded by the truncation.
          closest excluded: 5s at -0.06110  ->  **0.08664 Ha above the winner**
    Z=39  winner 4d at -0.19561.  7 channels excluded by the truncation.
          closest excluded: 7s at -0.03887  ->  **0.15674 Ha above the winner**
Predicted at least 0.05 Ha; observed 0.087 and 0.157 Ha. The gap is not marginal, and it
is WIDER at the heavier row, not narrower.

### R9-2 monotone in the predicted direction — **PASS**
    Z=19  5s -0.0611  5p -0.0456  5d -0.0209  5f -0.0200      rises with l at fixed n
    Z=39  7s -0.0389  7p -0.0304  7f -0.0103  7g -0.0102      rises with l at fixed n
The excluded region is approached from above and recedes monotonically. The truncation is
therefore defensible as a BOUNDARY argument rather than a row-by-row search — which is the
only form in which two rows could ever have supported it (R9-3, declared in advance).

### THE CAVEAT, AND IT IS NOT COSMETIC
At Z=19 the excluded **5s binds at -0.06110, MORE STRONGLY than the in-space 3d at
-0.05807.** The truncation therefore omits a channel that would have ranked THIRD in the
reported order. **The entrant is untouched — 5s loses to 4s by 87 mHa — and every claim
this solution makes rests on the entrant.** But the `order` column of a walk row is NOT
the complete ordering of all channels, and no statement anywhere may be worded as if it
were. Deliverable 1 must say the walk resolves the WINNER within a bounded candidate
space, not that it ranks every conceivable channel.

### NO-DATA, recorded not swept
5g (Z=19); 6h, 7d, 7h (Z=39) did not converge and are NOT counted as passing. Each is
bracketed by CONVERGED neighbours lying 0.1-0.19 Ha above the winner (7d sits between 7p
at -0.030 and 7f at -0.010), so none is a plausible winner — a bracketing argument, stated
as such, not a measurement.
Incidental: the walk's own `tagof` (nlchain.py:21) cannot even NAME an l=5 channel. The
l<=4 truncation is baked into the naming, which is why the extension needed a local tag.

## RUNG 7 — THE FLOOR, ONE NUMBER. **PASS.**
Radial grid 4000 -> 3000 points, ruling solver, Z=19, all channels:
    **max |dD| over 5 channels = 0.0108 mHa.   Entrant 4s -> 4s, UNCHANGED.**
Against the tightest margin anywhere in the sealed chain (Z=89, 32.33 mHa) that is a
factor of **3000**. A 25% coarsening of the mesh cannot manufacture or destroy any
ordering this solution claims. **Margins are physics, not numerics.**

### R7-3 reconciliation with s61's seed floor — DECLARED, NOT GLOSSED
The grid floor (0.011 mHa) is SMALLER than s61's seed-memory floor (<= 0.05 mHa). The
prediction required an explanation if so, and there is one: **the two numbers are measured
through different constructions** (Standing 8). R7 varies the grid on a FIXED direct
`run2` path; the seed test ran through the guard's damping ladder, where a rescued channel
converges by a different route. The seed number is the larger and more inclusive of the
two. **Take 0.05 mHa as the working floor.** Both are three orders below every margin.

### INCIDENTAL — F61.1'S MECHANISM IS NOW PROVEN, NOT INFERRED
R7 at npts=4000 returns 4p = **-0.09363**, which is the SEALED Z=19 value exactly, while
the guarded path returns -0.09558. F61.1 diagnosed the 1.95 mHa as the guard's repair;
this confirms it by reproducing the sealed number the moment the guard is bypassed.
**Sealed rows at Z<=56 are unguarded `run2` output.** The deferred re-walk keeps its place
on the owed list with its cause now established rather than suspected.

## LADDER STATE AFTER THIS SCORE
    DONE: Rung 1, 3, 4, 5, 6, 7 (minimal), 8, 9, 10, and the CONSTANT LEDGER.
    **EVERY QUANTITY ON THE LIVE PATH IS NOW CLASSIFIED. Nothing is unclassified.**
    OWED: Rung 2 (single-configuration bound on the ordering) and **RUNG 0 ASSEMBLY —
    the written reverse chain from the many-electron Schrodinger equation. That document
    is the deliverable the Challenge actually asks for, and it has never been drafted.**
