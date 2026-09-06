# RESULT-S104-ITEM1-C -- identity closure, row 58. Prediction 4ff84b9b. Instrument
# pack104/w104c.py; receipt w104c-58.json. Scored vs sealed w103a-58.json law terms and
# in-run reconstruction (d_rec = 0.0 exact vs w104-58.json).

## SCORE:
PQ1.a HIT 4/4. The Derivation-1 identity reproduces every measured cross asymmetry to
      machine precision (worst d = 2.6e-15). THE ASYMMETRY IS DERIVED:
      asym = (Deps)S - <u|(DVloc)|v> + DX, a residual of large canceling terms
      (V ~ +-5e-2, X ~ -+5e-2, eps*S ~ +-2.4e-3 -> net 1.3e-4).
PQ1.b HIT 4/4. |Deps*S| >= 10|asym| everywhere -- structural, hence SCF-tol independent:
      PB.1's miss is now DERIVED, not just observed.
PQ2.a MISS 0/2 as filed. d_total = 6.3e-12 / 4.2e-12 vs the 1e-12 bound. Cause: the bound was
      drafted below the double-precision floor of quartic-coefficient extraction at the
      |E| ~ 1e4 Ha functional scale (1e-16 x 1e4 ~ 1e-12). Reconstruction d_rec = 0.0 exact;
      decomposition content is machine-clean at its achievable floor. FAULT F104.2 registered
      (severity: HYGIENE -- prediction tolerance drafted without the energy-scale floor;
      same species as F104.1). No result depends on the faulted bound.
PQ2.b HIT 2/2 by its inequality (remainder +1.6e-8 / -1.9e-9 <= 2e-7; sign(T2) = + both) --
      BUT THE CLAUSE'S GLOSS IS FALSIFIED BY ITS OWN NUMBERS: T2 (endpoint-Hessian difference)
      = +1.72e-7 (6s) and +6.1e-9 (5s), NOT the +3.3e-6 residual. The S103 D1 QUADRATIC
      HYPOTHESIS IS FALSIFIED: the Hessian term is real, derived, and 20-500x too small.
      The residual lives in T1, the TRUE linear gradient term itself.
PQ2.c MISS 0/2 on the 1.5e-6 clause -- and the miss is the discovery. The consistency clause
      holds 2/2 AND SATURATES:
        gap(6s) = T1 - law = +3.19e-6 vs reach 2|s|<|asym|>/dq2 = 3.26e-6  (ratio 0.98)
        gap(5s) = T1 - law = +3.19e-6 vs reach                 = 3.19e-6  (ratio 1.00)
      Magnitude identity: |T1 - law| = 2|s| * <|asym|> / dq2 at both shells. The residual is
      EXACTLY the derived cross-element content entering the linear term through the
      symmetrized M -- mechanism (ii), now closed-form via Derivation 1. Not an ambiguity:
      the (Deps, DV, DX) identity states the content.
CAN-FAIL deferred: with PQ2.a's bound already exceeded at machine floor the d_total lever is
      vacuous in the current state (S103 precedent); to be re-armed against a corrected bound.

## CLOSED DECOMPOSITION OF rot (row 58, valence basis) -- every term now a derived object:
  rot = T1 + T2 + (T3 + T4)
      T1 = filed linear law + 2 s <asym> / dq2   [magnitude identity 0.98/1.00; SIGNED
           orientation trace is the one remaining paper step -- no computation]
      T2 = (1/4)<Dr|(H_m - H_p)|Dr>/dq2 = +1.7e-7 / +6.1e-9  [exact quartic coefficients]
      T3 + T4 <= 1.6e-8  [exact; O(|Dr|^3) as predicted]
  with asym = (Deps)S - <u|DVloc|v> + DX  [machine-exact identity, 4/4].

## OPEN RESIDUE AFTER THIS RUN: the signed orientation trace of the gap formula (paper);
## F104.1, F104.2 (hygiene). G5b closes as DERIVED once the trace is written.
