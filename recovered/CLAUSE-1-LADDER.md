# CLAUSE 1 — THE APPROXIMATION LADDER, v1
# Session 60. The reverse chain from the EXACT many-electron Schrodinger equation to the
# field `nlchain.step` actually solves. Every rung carries a CODE RECEIPT (file:line) and
# a CLASS. Nothing here is bounded yet except where it says BOUNDED. This is the naming
# pass; the bounding pass is the work that follows.
#
# CLASSES
#   DERIVED   -- follows from the equation above it with no free choice
#   NUMERIC   -- a discretisation or convergence parameter; must be shown CONVERGED,
#                which is a different obligation from being bounded
#   APPROX    -- a genuine physical approximation; its effect ON THE ORDERING must be bounded
#   INPUT     -- something taken from outside the equation. MUST be named and quarantined.
#   OFF       -- present in the code, PROVEN not to execute on the ruling path

## RUNG 0 — THE STARTING POINT (Löwdin's clause 3)
    H = sum_i [ -1/2 nabla_i^2 - Z/r_i ] + sum_{i<j} 1/r_ij
Exact, non-relativistic, clamped point nucleus, infinite nuclear mass, no spin-orbit.
Atomic units. **This is the object the solution must be traceable to.**

## RUNG 1 — RELATIVITY: AN ADDITION ABOVE RUNG 0, AND THE ONE RUNG ALREADY DISCHARGED
    receipt  t7c_kernel.py:25  C0 = 137.035999
             t7c_hfsr.py:8,39  scalar-relativistic (Koelling-Harmon), c passed positionally
    class    APPROX -- and it points the WRONG WAY: the ruling field is MORE than Rung 0,
             not less. A derivation from the non-relativistic equation may not rest on it.
    **STATUS: DISCHARGED, s60.** `pack60/SCORE-EXPOSED-13.md`: at c -> 1e6 the field
    reduces to the non-relativistic one, and the entrant is UNCHANGED at all 13 rows that
    could possibly have been affected; the other 94 are immune combinatorially (F55.2).
    **The ordering clause is a Rung-0 statement, not a relativistic one.** This is the
    single largest thing Clause 1 needed from the walk, and it is now in hand.
    RESIDUAL OWED: EX-4's failure at Z=19 (see the score) — a shift ordering, not an
    entrant, so it does not touch this status.

## RUNG 2 — SINGLE CONFIGURATION / CENTRAL FIELD
    receipt  hfc2.py:38-58  one radial P(n,l) per subshell, spherically averaged Y^k
    class    APPROX. The exact eigenstate is a CI superposition; the walk carries one
             determinantal configuration with a spherically averaged density.
    OWED     A bound on the ordering. The known failure mode is already named elsewhere in
             the solution: the s->d promotion anomalies (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag)
             are configurations the one-electron walk format cannot express. That is a
             FORMAT limitation of this rung, and Deliverable 1 says so.

## RUNG 3 — EXCHANGE IS EXACT HF ON THE CONVERGED ANSWER. THE KS FORM IS SEED-ONLY.
    receipt  hfc2.py:53   X += 0.5*Q[b]*_c3j0sq(l,k,lb)*Yk(P[a],P[b],k)/r*P[b]
                          -- Slater Y^k integrals with exact 3j coefficients: true nonlocal
                             Fock exchange, no functional
             t7c_kernel.py:105  Vx = -(3*rho/pi)**(1/3)   <-- Gaspar-Kohn-Sham, alpha=2/3
             t7b_hf.py:33-34    def seed(...): scf_occ(...)   <-- and it is used HERE
    class    DERIVED on the converged answer. The alpha=2/3 form appears only in the SCF
             STARTING GUESS.
    OWED     **THE SEED-INDEPENDENCE BOUND.** "Seed-only" is worth nothing until a
             converged SCF is shown to forget its seed. s53 named the warm-start test;
             it has not been run against the ordering. Until it is, Rung 3 is NOT closed.
             This is the highest-value single measurement left on this ladder.

## RUNG 4 — THOMAS-FERMI-DIRAC AND THE LATTER TAIL
    receipt  t7c_kernel.py:90   Vt,_ = tfd.potential(Z, ...)  -- SCF starting potential
             t7b_hf.py:10,119   Latter tail  Vall = min(V, -qtail/r)
    class    APPROX, seed-side. The Latter clamp enforces the exact asymptotic -q/r, which
             is a THEOREM about Rung 0, not a fit.
    OWED     Confirm whether `run2` (the walk's own solver, hfc2.py:40-59) applies the
             Latter clamp at all, or only `run` does. **UNVERIFIED. Do not assert either
             way.** Folds into the Rung-3 seed-independence bound.

## RUNG 5 — SELF-INTERACTION IN THE SAME-SHELL HARTREE TERM
    receipt  t7b_hf.py:105 _ceff ; used hfc2.py:45,49
    class    APPROX/DERIVED, undetermined. An occupation-effective charge removing a
             shell's self-repulsion.
    OWED     Classify it. If it carries any chosen coefficient it is INPUT and must be
             quarantined; if it follows from the determinant it is DERIVED. NOT YET READ.

## RUNG 6 — CORRELATION. **OFF, AND NOW PROVEN OFF.**
    receipt  hfc2.py:11   CORR = os.environ.get("CORR","1")=="1"   <-- DEFAULTS TRUE
             nlchain.py:17  H.CORR = False                          <-- ONE LINE, load-bearing
             hfc2.py:42,75  Vc = corr_pot(P) if CORR else 0 ; Ec = E_c(P) if CORR else 0
    class    OFF. This matters more than any other rung: the correlation branch is a
             Gell-Mann-Brueckner high-density functional (hfc2.py:14-19) whose
             coefficients are NOT derived anywhere in this chain. **If it executed, the
             no-fitted-constants claim would be dead.**
    **CAN-FAILED 2026-08-20T17:15Z — `pack60/corrcheck.py`, three directions, on the
    walk's own path (nlguard.run_guarded -> HFC.run2), not a hand-built call:**

        PHASE 0  import nlchain  ->  hfc2.CORR = False ; nlguard.H IS hfc2  (same global)
        PHASE 1  CORR=False   Z=4  E= -14.575879   corr_pot calls=0   E_c calls=0
                              Z=12 E=-199.935373   corr_pot calls=0   E_c calls=0
        PHASE 2  CORR=True    Z=4  E= -14.575616   calls=27/1   dE=+0.000263 Ha
                              Z=12 E=-199.934938   calls=30/1   dE=+0.000434 Ha
        PHASE 3  CORR=False   both return BIT-IDENTICAL to PHASE 1, calls=0
        CORRCHECK: PASS

    The script REFUSES to pass if the branch executes when off, if it fails to execute
    when on, or if turning it on changes nothing — that last being F59.3's exact signature
    and the half s52-s59 never checked on `c`. **The control is proven to vary the thing
    it controls for.**
    NOTED, NOT CLAIMED: dE is 0.26-0.43 mHa at Z=4,12 against margins of 50-100 mHa. That
    is a total-energy shift for one configuration, NOT the channel DIFFERENCE the walk
    reads, and it is measured at two light atoms only. **It is not a bound and is not
    offered as one.** A bound would need the difference, across Z.

## RUNG 7 — NUMERICS
    receipt  t7c_kernel.py:39,89  rmin=1e-5/Z, rmax=max(80, 4n^2/zeta), npts=3000/4000,
                                  log mesh ; tol=1e-9 / 2e-5 / 2e-6 ; beta mixing 0.3/0.4
             nlguard.py LADDER    beta/maxit rungs; rung 0 IS the ruling field
    class    NUMERIC. These cannot bias the ORDER, only the precision of a margin —
             PROVIDED convergence is demonstrated. It is not, yet.
    OWED     A convergence floor for the restart walk. **This is now doubly owed: EX-4's
             failure at Z=19 sits at 0.6-2.5 mHa and "numerical" is the obvious excuse for
             it, which is exactly why the floor must be measured before anyone offers it.**

## RUNG 8 — THE REFERENCE CONFIGURATION. **NAMED, PER M'S RULING OF s60.**
    receipt  nlchain.py:29  cfg_from_chain(Z-1, rows)   -- CHAINED mode
             nlchain.py:8   restart Z: one step from the OBSERVED config(Z-1)
             cinf2.py:73    NC.step(Z, G.expand(Z-1), rows, 'cinf2')   <-- RESTART
             pack53/induct.py:32  NC.step(Z, NC.cfg_from_chain(Z-1, rows), ...)  <-- CHAINED
    **THE TWO MODES ARE NOT THE SAME OBJECT AND MUST NEVER BE CONFLATED:**

      CHAINED  cfg(Z-1) is built from the walk's OWN previous choices, seeded once at Z=1.
               **class DERIVED. Empirics-free. This is the mode in which the solution is
               claimed.** `ground.py` supplies only the seed and the comparison column
               (nlchain.py:3, and G.expand appears at nlchain.py:86-88 in the RECORD
               fields `rec`/`recent`, downstream of `win` at line 83 — it cannot reach the
               entrant).

      RESTART  cfg(Z-1) is `G.expand(Z-1)`: the OBSERVED, MEASURED ground configuration.
               **class INPUT. This mode reads experimental data into the reference.**

    **WHY THE RESTART MODE IS NEVERTHELESS LEGITIMATE WHERE IT IS USED, AND WHERE IT IS
    NOT.** It is a per-element probe, not a derivation. Its results are admissible for
    statements OF THE FORM "holding the reference fixed, X changes the answer / does not"
    — a controlled comparison in which the empirical input appears IDENTICALLY on both
    sides and cancels. It is INADMISSIBLE as evidence that the walk derives anything,
    because at those rows the walk was handed the answer to Z-1.

    This is exactly why s60 checked, rather than assumed, that the two constructions
    coincide at the 13 exposed rows (F60.3: 13/13 identical, zero solve cost). Because
    they coincide there, today's c-experiment is BOTH a clean c-comparison AND free of
    empirical contamination at those rows. **That coincidence was verified, not hoped
    for, and it does not extend to any other row without the same check.**
    STANDING CONSEQUENCE: any future statement built on `restart` rows must state which
    of the two it is, and if it claims derivation, must show the configs coincide.

## RUNG 9 — THE CANDIDATE RULE
    receipt  nlchain.py:6  occ(c) < 2(2l+1), n <= N+1, 0 <= l <= min(n-1,4), N = max n occ
    class    APPROX (a search-space truncation), SPEC-CHAIN-SESSION-40 §4, chosen.
    OWED     Show no excluded channel could have won. The l <= 4 and n <= N+1 cuts are the
             ones that must be defended. NOT YET DONE.

## RUNG 10 — THE ENTRANT CRITERION
    receipt  nlchain.py:5  D_chain(c) = E_HF(cfg+c) - E_HF(cfg); entrant = argmin
    class    DERIVED. **The entrant is a Delta-SCF TOTAL-ENERGY difference, not an orbital
             eigenvalue.** This is the rung that answers Löwdin's "filling ambiguity"
             clause: the walk governs the DIFFERENTIATING electron, by total energy.
             No Koopmans, no eigenvalue ordering, no screening constant.

## THE CONSTANT LEDGER — EVERY NUMBER ON THE LIVE PATH
    c = 137.035999    DECLARED. The one entered number. Rung 1 shows the answer is
                      unchanged as c -> infinity, so it is not load-bearing for ORDER.
    alpha = 2/3       Gaspar-Kohn-Sham exchange coefficient. DERIVED, and SEED-ONLY.
    GB correlation    NOT ON THE PATH — Rung 6, can-failed.
    grid / tol / beta NUMERIC, Rung 7, convergence owed.
    NO screening constant, NO ionization energy, NO fitted parameter appears at any rung.

## WHAT CLAUSE 1 STILL OWES, IN PRIORITY ORDER
    1. Rung 3/4  seed-independence (warm-start) against the ORDERING. Highest value.
    2. Rung 7    the convergence floor — and it must be measured BEFORE it is used to
                 explain EX-4's Z=19.
    3. Rung 5    classify _ceff: DERIVED or INPUT.
    4. Rung 9    defend the candidate-space truncation.
    5. Rung 2    bound the single-configuration approximation on the ordering.
    Rungs 1, 6, 8, 10 and the constant ledger are DONE as of s60.
