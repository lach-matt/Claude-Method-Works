# PREDICTION — CI-1..CI-7. Session 71, route C-b.
# FILED AND HASHED BEFORE ci2.py EXISTS AND BEFORE ANY ROW IS READ. R 1449.
# Clause-only. No numeric bands (s48 precedent, M accepted: four extrapolation bands failed
# in the same direction while the clauses held).

CI-1  The one-body coupling <ns|h|(n-1)d> is zero to machine precision (<= 1e-12 Ha) at
      every row tested. FALSIFIER: any value above 1e-12.

CI-2  With the spectator set spherically averaged -- the L4 field, exactly as the walk
      solves it -- the TOTAL coupling V is zero to machine precision.
      FALSIFIER: nonzero. If CI-2 fails, section 2(iii) of the spec is wrong and the whole
      design is withdrawn.

CI-3  Every direct two-body contribution to V is zero at every multipole; the coupling is
      carried by EXCHANGE alone. FALSIFIER: a nonzero direct term.

CI-4  THE SELECTION RULE. V is nonzero only where l_A + l_B is even. Specifically V is
      nonzero at the s<->d rows and IDENTICALLY ZERO at the d<->f rows.
      FALSIFIER: a nonzero V at Ce 58 or Th 90, or a zero V at both Cr 24 and Cu 29.

CI-5  THE ORDERING CLAUSE. At every FIRST-ENTRY row -- a row that opens a channel -- V is
      zero, because the partner channel is unoccupied and no open spectator shell of the
      required l exists. Tested at Sc 21, La 57, Ac 89.
      FALSIFIER: a nonzero V at any first-entry row.

CI-6  V at Cr 24 and Cu 29 clears the 0.05 mHa working floor.
      FALSIFIER: below floor. **If CI-6 fails the 2x2 object is DEAD as a repair for the
      configuration column, and that is a real result, not a null: it would close L3 as
      bounded at these rows by measurement rather than by declaration.**

CI-7  The lower root of the 2x2 lies at or below min(E_A, E_B) at every row where V =/= 0.
      This is variational and is a can-fail check on the diagonaliser, not a physics claim.
      FALSIFIER: a raised lower root.

## TIMING
No number bearing on any clause above has been read at the time of filing. `ci2.py` does
not exist. `pb4_terms.jsonl` holds E_A and E_B at Z=59 and Z=64 ONLY, both read at s71
before this filing -- neither Z appears in any clause above, and neither carries a V.