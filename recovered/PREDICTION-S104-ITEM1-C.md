# PREDICTION-S104-ITEM1-C -- closure of both Item-1 residues by DERIVED IDENTITY, row 58.
# Filed and hashed BEFORE any arithmetic. c the only number. No new SCF objects: the three
# standard solves (q = 0.4/0.5/0.6) are state reconstruction of sealed numbers (w103 cache-resume
# precedent); every scored quantity below is a closed-form function of those states.

## DERIVATION 1 (the cross-element asymmetry is an identity, not noise):
For u an eigenstate of h5's Fock operator and v of h(+/-)'s, the two eigen-relation extractions
of <u|T|v> differ EXACTLY by
    asym(u,v) = (eps_v - eps_u) S_uv - <u|(Vloc_v - Vloc_u)|v> + [<u|X_v> - <v|X_u>]
with (Vloc, X) = pot(state, shell) -- the state-dependent multiplier structure of HF (Lowdin's
non-orthogonality apparatus; multiplier matrices differ between Hamiltonians defined by
different orbitals). Every term evaluates from the existing states.

## DERIVATION 2 (the +3.3e-6 rot residual is the endpoint-Hessian difference):
Efun with only shell k's orbital varying is EXACTLY quartic in t along P + t*Dr (one-body
quadratic; two-body Coulomb/exchange quartic). Hence with exact polynomial coefficients
    F(Pm + t Dr) = F(Pm) + c1m t + c2m t^2 + c3m t^3 + c4m t^4   (and likewise at Pp with -t),
the sealed two-endpoint estimator decomposes EXACTLY as
    rot = [ (c1m + c1p)/2 + (c2m - c2p)/2 + (c3m + c3p)/2 + (c4m - c4p)/2 ] / dq2 .
Term 1 is the linear gradient (the S103 law's object); term 2 is the endpoint-Hessian
difference (1/4)<Dr|(H_m - H_p)|Dr>/dq2 -- the standard HF orbital-rotation Hessian content;
terms 3-4 are the cubic/quartic remainder, O(|Dr|^3), |Dr| ~ 2.4e-3.
Coefficients are extracted EXACTLY (no step-size truncation) from 5 F-evaluations per endpoint
at t in {0, +-1/2, +-1}, since a quartic is determined by 5 points. F-evaluations are cheap
functionals of existing states (no SCF).

RULE B LINE: PQ1.a / PQ2.a value-exact (bookkeeping identities, machine tolerance); PQ1.b
structural inequality; PQ2.b value-exact AND sign-exact; direction: differences BELOW bound.

PQ1.a: the Derivation-1 expression reproduces the measured cross asymmetry M[u,v] - M[v,u] to
  <= 1e-12 at all four cross elements (6s: m|5s, p|5s; 5s: m|6s, p|6s), basis as branch A.
PQ1.b: |(eps_v - eps_u) S_uv| >= 10 |asym| at all four -- the asymmetry is a small residual of
  large canceling Delta-eps x overlap and potential/exchange terms, hence SCF-tol independent
  (this DERIVES the PB.1 miss).
PQ2.a: the four-term decomposition total reproduces rot_val to <= 1e-12 at 6s and 5s
  (rot_val recomputed in-run with branch-A machinery at standard tol; must match w104-58.json
  to <= 1e-9 as reconstruction check).
PQ2.b: the identified residual IS the Hessian term: |rot_val - term1 - term2| <= 2e-7 at both
  shells (cubic+quartic remainder is O(|Dr|^3)-small), AND sign(term2) = + at both shells
  (matching the observed +3.2e-6 / +3.4e-6 residuals).
PQ2.c (informative, scored): |term1 - law| <= 1.5e-6 at both shells (law terms sealed in
  w103a-58.json: +4.0626e-6, -7.8432e-6); any term1-law gap is the symmetrized-M cross-element
  content now derived in PQ1 -- reported, and its scale must be <= the PQ1 reach
  2|s||asym|/dq2 <= 1.7e-6 (consistency clause between the two derivations).

CAN-FAIL (non-vacuous): --canfail adds 1e-6 to c2m at 6s after extraction; PQ2.a total at 6s
  must then MISS (>1e-12) -> rc=4 BREAK OK; else rc=5 VACUOUS.

If PQ1.a + PQ2.a + PQ2.b all HIT: G5b closes as DERIVED -- rot = linear valence law
+ endpoint-Hessian difference + (removed) core-M content, every term a closed-form object of
the sealed operators. Scored against sealed w103a-58.json and fresh-reconstruction receipts
only. No sealed file edited. All work in pack104/.
