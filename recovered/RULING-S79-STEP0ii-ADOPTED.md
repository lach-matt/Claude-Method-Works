# RULING S79 — STEP 0(ii) SELECTION RULE: ADOPTED, WITH THE OBLIGATION REGISTERED TO ROUTE C.
# M ruled at s79 open. This closes item 6 of SESSION-78-COMBINED §5.
# NO SEALED FILE EDITED. c = 137.035999 remains the only number ever entered.

## THE RULE, NOW ADOPTED (text as drafted at pack76/POSITION-S76-SELECTION-RULE.md §3)
> For each Z and each candidate channel, the field is DEFINED to be a GLOBAL MINIMISER of
> the restricted Hartree-Fock functional E^RHF at the fixed shell occupancies of that
> candidate, over the relaxed set of Hantsch (8). Existence: Hantsch Theorem 2.1.
> Every scored row satisfies Z > N-1, so the minimiser is normalised with all shell
> eigenvalues strictly bound.

## WHAT ADOPTION CHANGES, EFFECTIVE IMMEDIATELY
1. Phi is defined by a VARIATIONAL PROPERTY, not by a trajectory.
2. **(beta, maxit) LEAVES THE DEFINITION.** The convergence ladder (R 47, rungs 0/1/2) is
   hereby a NUMERICAL SCHEME for approaching an independently defined object, and is no
   longer any part of what the derivation asserts. F47.3's mixed-rung resolution limit
   (~1e-5) is a statement about the SCHEME, not about the field.
3. The rule is stated on the ENERGY, never on the spectrum. Lions' simplicity assertion
   for radial Fock eigenvalues is NOT imported and must not be imported later by stealth.

## THE OBLIGATION, REGISTERED — OWNER: ROUTE C. LOAD-BEARING.
**O-C1. THE PROGRAM MUST BE SHOWN TO REACH THE GLOBAL MINIMISER, NOT A SADDLE AND NOT A
LOCAL ONE.** Cances & Le Bris (M2AN 34 (2000) 749) and Levitt (M2AN 46 (2012) 1321)
deliver A CRITICAL POINT ONLY. Adoption transfers this burden from the mathematics to the
code, where before adoption it was unnamed.
**EVIDENCE HELD AND ITS EXACT WEIGHT:** seeds A/B/C/D agree to 0.005 mHa from 52 Ha away,
and at s78 seed D held at Z=89 from 517 Ha away. **THAT IS A FOUR-START BASIN TEST. IT IS
NOT A PROOF OF A GLOBAL MINIMUM AND IS NEVER TO BE QUOTED AS ONE.**
**THE FALSIFIER IS CHEAP AND IS NOT YET RUN:** perturb a CONVERGED solution and
re-converge. A second basin at lower energy kills the rule as stated.