# PREDICTION S79 — ITEM 1. THE FIXED-FIELD CROSS-CHANNEL COMPARISON AT Z=89.
# FILED BEFORE THE BUILD AND BEFORE THE RUN. Nothing below has been executed.

## THE OBJECT, AS CLOSE-S78 §3 DEFINES IT
Freeze the core at the converged 6d solution, Phi_d*. Build F_core = h + sum_{i in core}
(J_i - K_i) from those frozen core orbitals. The residual clause-1 claim is
      **eps_3^{l=3}(F_core[Phi_d*])  >  eps_4^{l=2}(F_core[Phi_d*])**
i.e. 6f above 6d in ONE field. This is NOT what item 2 measured — item 2 gave three
DIFFERENT self-consistent fields. THIS IS THE FIRST TIME THE FIXED-FIELD OBJECT IS COMPUTED.

## A FACT READ FROM SOURCE BEFORE PREDICTING (t7b_hf.py:105, hfc2.py:45)
`_ceff(a,Q) = Q[a] - 1.0`. At single occupancy this is ZERO, so the valence orbital's own
Hartree term and its exchange self-term BOTH DROP. **The sealed walk already solves a
single valence electron in F_core plus the correlation potential Vc.** The fixed-field
object is therefore adjacent to what is already computed, not remote from it.

## DECLARED CHOICE, APPLIED IDENTICALLY TO BOTH CHANNELS
Vc = 0 for the probe orbital, because the probe is not in `occ` and corr_pot is defined
per occupied shell. Applied to l=2 and l=3 alike, so the COMPARISON is like-for-like.
The sealed 6d eigenvalue is reported alongside as a cross-check, not as the comparand.

## THE PREDICTIONS
W1  **eps_3^{l=3} > eps_4^{l=2} IN THE FROZEN FIELD. The Madelung ordering HOLDS at Z=89
    at fixed field.** Predicted TRUE.
W2  **THE FROZEN GAP EXCEEDS THE RELAXED GAP OF 126.020 mHa**, and the frozen 6f lies
    ABOVE (less bound than) the relaxed -0.031600 Ha. Rationale filed: the core is
    optimised for 6d, so denying 6f its own core relaxation can only cost 6f. Flagged:
    this reasoning is exact for total energies and is being applied to EIGENVALUES.
W3  The l=2 probe reproduces the sealed 6d value -0.15762 to within a few mHa, the
    residue being Vc. This is the MACHINERY CROSS-CHECK. A large discrepancy voids the run.
W4  The l=3 probe requires the refined scan at least once: the standard bracket
    misidentifies the state in the frozen field as it did in the SCF.
W5  The frozen gap lies between 126 and 250 mHa.

## CAN-FAIL, DECLARED IN ADVANCE
The comparator must be able to return ORDERING FAILS. Control: probe (4,3) — 4f, which
lies DEEP INSIDE the [Rn] core and far BELOW 6d. **The control MUST return eps(4f) <
eps(6d), i.e. the f-above-d comparison FAILING.** If the control returns the ordering
holding, the instrument is broken and the run is void. **THE CONTROL RUNS FIRST.**

## THE FALSIFIERS
W1 is falsified by eps_3^{l=3} <= eps_4^{l=2}, which would be a counterexample to the
derivation at its tightest row and would be reported as one, unrewritten.
W2 is falsified by a frozen gap below 126.020 mHa.