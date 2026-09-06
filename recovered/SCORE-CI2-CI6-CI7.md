# SCORE — CI-2, CI-6 (ALL TEN s<->d ROWS), CI-7. Session 73, M's ruling "test it all". R 1970.
# Prediction pack71/PREDICTION-CI2x2.md sha256 bb04e6c2...5fb1429, filed at s71 before any
# instrument existed. Determinant sector: pack73/DERIVATION-CI6-SECTOR.md, filed before any
# radial integral. Instrument pack73/ci2b.py · rows pack73/ci2b.jsonl.
# Scalar-relativistic HF, c = 137.035999. No other constant. No CG recoupling — still R-C(a).

## REPRESENTATIVE FREEDOM REMOVED BY ENUMERATION
ci2.py chose ONE determinant pair per row. For N =/= 5 that choice is not unique and would
have been the assistant's design decision. ci2b enumerates EVERY pair sharing (M_L,M_S) and
differing by exactly one spin-orbital. The constraint solves itself: the replaced orbital is
forced to be d(m=0) with spin opposite the s electron. Reported statistic is max|V| — "is the
coupling alive anywhere in the shared sector". Cross-check: at Cr the enumeration contains
ci2.py's pair (4.0711 mHa) and finds a stronger member at 8.1422 mHa. Instruments agree.

## THE TEN ROWS
    Z  el  kind    pairs   |V|max mHa   spherically-averaged spectator   floor 0.05 mHa
    24 Cr  single    252      8.1422        8.67e-16 mHa                 CLEARS
    29 Cu  single      2      0.0000        4.34e-16                     ZERO
    41 Nb  single    168     18.8513        4.34e-16                     CLEARS
    42 Mo  single    252     17.7535        8.67e-16                     CLEARS
    44 Ru  single    168     15.8185        8.67e-16                     CLEARS
    45 Rh  single     72     14.9719        0.00e+00                     CLEARS
    46 Pd  DOUBLE      5      9.9418        n/a                          CLEARS
    47 Ag  single      2      0.0000        1.73e-15                     ZERO
    78 Pt  single     18     12.8700        1.73e-15                     CLEARS
    79 Au  single      2      0.0000        1.73e-15                     ZERO
Pd is NOT a single replacement: 4d10 vs 4d8 5s2 differ by TWO spin-orbitals. Scored under the
double-replacement clause of Slater-Condon, and flagged as such. Pd is also the one row whose
A configuration holds no s orbital at all, so its common set is taken on the B field.

## SCORING
**CI-2  HELD.** With the open spectator spherically averaged — the L4 field exactly as the
walk solves it — V is machine zero at every single-replacement row (worst 1.7e-15 mHa).
**SPEC §2(iii) SURVIVES. The design is NOT withdrawn.** This was the clause whose failure
would have taken the whole 2x2 object with it. It was NOT TESTED from s71 to now.

**CI-6  FAILED AS FILED, and the failure is a selection rule.** The clause is conjunctive
over Cr and Cu. Cu is exactly zero. Extended over all ten rows: CLEARS at seven, EXACTLY
ZERO at three. **The three zeros are Cu 29, Ag 47, Au 79 — and nothing else.**

**CI-7  HELD.** Lower root at or below min(E_A,E_B) at all ten rows. S = I as derived, so the
generalised problem is an ordinary symmetric 2x2 and the check is on the diagonaliser.

**CI-1, CI-3, CI-5 unchanged. CI-4 stands** (its falsifier needs zero at BOTH Cr and Cu).

## THE RESULT WORTH THE SESSION — GROUP 11 IS A DIFFERENT OBJECT FROM THE OTHER ANOMALIES
The ten s<->d anomalies partition by ANGULAR MOMENTUM ALONE into two classes:
  (i)  **d10 s1 rows — Cu, Ag, Au.** A is closed d10 + s, hence PURE 2S. B is d9 s2 and d9
       carries only 2D, hence PURE 2D. H is a scalar: <2S|H|2D> = 0 EXACTLY. Measured at
       4e-19 Ha on both fields, at all three rows, and the shared sector is only 2 pairs wide
       so there is no freedom anywhere in it. **Configuration mixing between the observed and
       the Madelung configuration is RIGOROUSLY FORBIDDEN at every coinage metal.**
  (ii) **every other s<->d anomaly — Cr, Nb, Mo, Ru, Rh, Pd, Pt.** V = 8 to 19 mHa, alive,
       clearing the working floor by two to three orders.
**This partition was DERIVED at Cu before any number (DERIVATION-CI6-SECTOR §3a) and then
found to hold at Ag and Au, which were not part of that derivation.** A prediction made on
one row and confirmed on two rows it did not cover.

**CONSEQUENCE, AT ITS PROPER STRENGTH.** The Cu/Ag/Au anomalies are not "too small to repair
by the 2x2". They are UNREACHABLE by it. Whatever produces the d10 s1 ground state at the
coinage metals, it is NOT configuration mixing with the Madelung configuration. That closes
one candidate mechanism for three of the Challenge's exceptions BY DERIVATION, not by bound.
And per DERIVATION §3b the same is true of Cr for a different reason: 7S has no partner of
the same (L,S) in 3d4 4s2, so the mixing that IS alive at Cr cannot reach Cr's ground term.

## WHAT IS NOT CLOSED — SEE F73.2
The 2x2's diagonal here is the AVERAGE-OF-CONFIGURATION HF energy while its off-diagonal is a
DETERMINANT-level element. That is a resolution mismatch. No conclusion about which
configuration wins, and no claim about the configuration column, is drawn from it in this
score. The term-resolved 2x2 is a NEW object and requires a FRESH hashed prediction.