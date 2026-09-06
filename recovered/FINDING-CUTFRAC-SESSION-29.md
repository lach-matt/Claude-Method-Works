# FINDING — mechanism B (the eps_c >= 0 cut) IS the class-row remainder on Cs and is NOT it on the d rows.  s29.
# Files: PREDICTION-CUTFRAC-SESSION-29.md (before any run), cutfrac.py, cutfrac.jsonl (six neutral SCFs, SUBCELL=1). No new form, no constant, no measured
# input beyond the banked meas/so columns already in the chain. Not a closure.
## Table (F_out = entrant charge beyond r_cut, the last radius where eps_c[total] < 0; F_self = entrant charge where its own SIC density has eps_c >= 0)
row  F_out  F_self  r_cut  <r>   | required delivered missing  missing/req | missing/req <= F_out ?
Cs   0.869  0.997   3.77   5.97  |  0.0153    0.159    0.0129    0.841     | yes
Sc   0.020  0.120   4.05   1.66  |  0.0280    0.930    0.0019    0.070     | NO
Y    0.076  0.224   4.23   2.45  |  0.0329    0.614    0.0127    0.386     | NO
La   0.096  0.268   4.42   2.83  |  0.0282    0.650    0.0099    0.350     | NO
Lu   0.112  0.268   4.20   2.64  |  0.0313    0.622    0.0118    0.378     | NO
Gd   0.092  0.250   4.30   2.65  |  0.0430    0.400    0.0258    0.600     | NO (4f-adjacent; set aside)
## Predictions
PB1 HELD: F_out orders Sc 0.02 < {Y, La, Lu 0.08-0.11} < Cs 0.87.   PB2 HELD: (1 - delivered) has the same three-group order (0.07 < 0.35-0.39 < 0.84).
PB3 HELD: F_self > F_out on every row; F_self(Cs) = 0.997.
PB4 HELD on Cs only: missing/req 0.84 <= F_out 0.87 — the 6s lives 87 % past the cut and 84 % of its correlation is missing; B accounts for Cs in full.
    FAILED on every d row: missing/req is 3-5x F_out (Y 0.39 vs 0.08; La 0.35 vs 0.10; Lu 0.38 vs 0.11; Sc 0.07 vs 0.02) — and still exceeds even
    the generous F_self bound on Y La Lu. Correlation is missing INSIDE the object's own domain on the d rows.
## What this splits
The remainder is two objects, by shell type. (i) 6s: the derived high-density correlation form leaves its domain where a diffuse entrant lives; the
min(eps_c,0) constraint is the honest treatment and it costs 0.013 Ha on Cs. That is a property of the object, on record since s28. (ii) 4d/5d: with
the entrant 90 % inside the domain, the local form still delivers only ~62 % of the required correlation; the excess over the cut, missing/req - F_out
= 0.31 (Y) · 0.25 (La) · 0.27 (Lu) · 0.05 (Sc), is ~0.008-0.010 Ha on Y La Lu and ~0.001 on Sc. Uniform on the three n>=4 d rows, absent on 3d.
That is the object to pursue: entrant-core correlation the local form under-counts when the entrant sits outside a large closed (n-1)s2p6 shell (mechanism A,
core-valence), against zero deficit for 3d inside the Ar-like core. Test A needs a build: alpha_core of the chain's own HF orbitals by a Sternheimer
equation on the shooter, and the second-order entrant-core correlation cutoff-free (no r_c parameter) — prediction first: the A term must be ~0.009 on
Y La Lu, ~0.001 on Sc, and must NOT be needed on Cs beyond what B already gives.
Failed predictions s29 (this item): PB4 on d rows — as designed, this is the discriminating result, not an error. Timing flag: a sign slip in the derived
"required" column of cutfrac.py (so column added with the wrong sign) was corrected before any prediction was scored; SCF fields untouched; on record.
Gate for HANDOFF-29: python3 cutfrac.py -> must SKIP all six.