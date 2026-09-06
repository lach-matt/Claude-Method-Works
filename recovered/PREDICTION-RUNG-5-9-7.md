# PREDICTION — RUNGS 5, 9 AND THE MINIMAL RUNG-7 FLOOR
# SESSION 62. FILED BEFORE ANY CODE OF THESE TESTS WAS WRITTEN OR RUN. R 1449.
# Scope set by M's ruling of this session: EX-4 RETIRED; the F61.1 55-row re-walk
# DEFERRED; the Rung-7 floor reduced to ONE NUMBER, not a campaign. Everything here
# serves a numbered clause of the 1969 Löwdin Challenge and nothing else.

## RUNG 5 — CLASSIFY `_ceff` (t7b_hf.py:105). SERVES CRITERION 4 (NO EMPIRICAL HEURISTICS).
### The reading, filed as a claim so it can be falsified
`_ceff(a,Q)` has two branches:
    frac branch   (qc*(qc-1) + 2*f*qc)/(qc+f)     -- s28 F26.2 fractional-occupation lift
    default       Q[a] - 1.0
`self.frac` is set at exactly six sites in the whole archive — drow_p.py:28, frachf.py:34,
frachf_S.py:19, frachf_eps0.py:13, frachf_ring.py:19, nodesplit.py:13 — every one of them
a fractional-occupation probe driver. **NONE is on the walk path.** nlchain -> nlguard
constructs a fresh `HFC(Z,cfg,c=C0)` (nlguard.py:64) and never assigns `.frac`.

R5-1  THE FRAC BRANCH IS OFF ON THE RULING PATH, AND PROVEN OFF IN THE CORRCHECK MANNER
      (three directions, Rung 6's standard): on a real `NG.run_guarded` call the frac
      branch executes ZERO times; forced on, it executes and CHANGES the energy; released,
      the energy returns BIT-IDENTICAL. **If forcing it changes nothing, the control is
      vacuous and this reports VOID, not PASS (F59.3).**

R5-2  THE DEFAULT IS DERIVED, NOT CHOSEN. `Q[a]-1.0` is the average-of-configuration
      statement that an electron in shell a sees the other q_a-1 electrons of its own
      shell and all q_b of every other — the exact removal of self-interaction from the
      determinant (Slater; Froese Fischer 1977), carrying no coefficient to fit.
      **THE FALSIFIER, and it is sharp:** at q=1 the derived value is exactly ZERO, so a
      one-electron atom must carry NO Hartree self-repulsion at all. Predicted: the walk's
      own solver at Z=1 returns the hydrogenic total energy to better than 1 mHa
      (non-relativistically -0.5 Ha exactly; the SR field must sit slightly below it, by
      less than 1 mHa at Z=1). Had `_ceff` returned Q[a] or any fitted screening value,
      Z=1 would carry a spurious self-repulsion of order 0.3 Ha and this test would fail
      by hundreds of milli-Hartree. There is no parameter that could be tuned to hide it.

## RUNG 9 — THE CANDIDATE TRUNCATION. SERVES CRITERION 6 (THE RULE AS A CONSEQUENCE).
The walk searches occ(c) < 2(2l+1), n <= N+1, 0 <= l <= min(n-1,4) (nlchain.py:6). What is
owed is that **no excluded channel could have won.**

R9-1  Extending the space to n <= N+2 and l <= 5 at a test row adds only channels that
      bind MORE WEAKLY than the winner — every added channel's D lies above the winner's
      D, and by a wide margin, not a marginal one. Predicted: every added channel sits at
      least 0.05 Ha above the winner at Z=19 and at Z=39.
R9-2  The added channels are monotone in the expected direction: for fixed l, D rises with
      n; for fixed n, D rises with l. A NON-MONOTONE addition would mean the truncation
      cannot be defended by a boundary argument and would have to be defended row by row
      across all 107 — report it loudly if seen.
R9-3  **HONEST LIMIT, DECLARED NOW.** Two rows do not close a truncation over 107. What
      two rows can establish is the SIZE and SIGN of the gap at the boundary. If the gap
      is large and monotone the truncation is defensible as a boundary argument; the
      claim must then be worded as such and not as an exhaustive search.

## RUNG 7 — THE FLOOR, MINIMAL FORM. ONE NUMBER, BY M'S RULING.
What is needed is not a campaign but a demonstration that the numerics cannot manufacture
or destroy the orderings the solution claims.
R7-1  Halving the radial grid (npts 4000 -> 3000, the other value already present in the
      kernel at t7c_kernel.py:39) moves the channel differences D by less than 1 mHa at
      Z=19, against a tightest margin anywhere in the sealed chain of 32.33 mHa (Z=89).
R7-2  The entrant at the test row is unchanged under the grid change.
R7-3  The floor so measured must be consistent with s61's seed-memory floor of
      <= 0.05 mHa. It may legitimately be LARGER (grid is a coarser variable than seed
      memory); it may not be smaller without an explanation, and if it exceeds 5 mHa the
      margins in Deliverable 1 must carry it explicitly.
**EX-4 IS RETIRED BY RULING AND IS NOT SCORED HERE. This floor is NOT offered as an
explanation of anything at Z=19; it is offered as a bound on the solution's margins.**

## WHAT FAILURE WOULD MEAN
  R5-1 VOID or R5-2 fail -> a fitted or self-interacting quantity is on the live path and
       criterion 4 is breached. This is the single worst outcome available and would be
       reported first, before anything else in the session.
  R9-1 fail -> an excluded channel could have won; the derivation is incomplete and the
       candidate rule becomes an INPUT rather than a truncation.
  R7-1 fail -> margins are numerics, not physics, and every margin claim in Deliverables
       1 and 3 must be restated with the floor attached.
