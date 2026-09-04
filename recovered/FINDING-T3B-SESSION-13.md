# FINDING — T3b bracket/geometric-mean test, session 13 (2026-08-16). 6 of 6 required points SERVED.
Source: NIST Handbook of Basic Atomic Spectroscopic Data, <el>table1_a.htm (IP, ref) + <el>table6_a.htm (ion levels, ref).
Definition (session 11, before lookup): E_bind = IP(M I) + E(M II hole state), hole state = ion with one electron removed from
the entrant shell, all else fixed. Kernels: T0b_pairs.json (PACK-9), TFD (repaired floor) and SCF one-electron eigenvalues.
Served (served.tsv): Sc, Ti, Cr, Fe, Cu (3d), Yb (4f). NULL (hole state not in Handbook = gap, not negative): V, Mn.
Not attempted (budget): Co, Ni, La–Tm, Lu.  Scoring script fault registered before reading: kernel key by Z only merged 3d/4f rows;
repaired to (Z,shell); Sc regenerated to the session-11 figures exactly.
  el   meas     TFD     SCF     geo    arith  between  geo%   arith%
  Sc  -0.2946 -0.0878 -0.4866 -0.2067 -0.2872   Y     29.8    2.5
  Ti  -0.3647 -0.1176 -0.5485 -0.2540 -0.3330   Y     30.4    8.7
  Cr  -0.3032 -0.2453 -0.6592 -0.4021 -0.4522   Y     32.6   49.2
  Fe  -0.3967 -0.4928 -0.7590 -0.6116 -0.6259   N     54.2   57.8
  Cu  -0.3839 -1.1403 -0.8961 -1.0109 -1.0182   N    163.3  165.3
  Yb  -0.3274 -1.7105 -0.8447 -1.2021 -1.2776   N    267.1  290.2
PB-11.1 (between kernels where |TFD-SCF|>0.1): 3/6 — HOLDS at the onset (Sc,Ti,Cr), FAILS from Fe on: BOTH kernels deeper than measured.
PB-11.2 (>=4/6 within 30% of geometric mean): 1/6 — FALSIFIED (Ti 30.4, Cr 32.6 just outside; Fe on far outside).
PB-11.3 (geo fails past mid-row where kernels cross): HELD as stated — but the failure is a monotone drift already visible at Cr,
        not an artefact of the crossing. The mean is not the object (session-9 'no mean' stands, now at 6 points).
FINDING (the number the test actually returned): the MEASURED entrant-shell binding is nearly flat across the row,
  3d: -0.29..-0.40 Ha over Sc->Cu (slope ~0.012 Ha/Z); Yb 4f -0.33 Ha — while both one-electron kernels deepen steeply
  (TFD -0.09 -> -1.14, ~0.13 Ha/Z; SCF -0.49 -> -0.90, ~0.05 Ha/Z). Two languages, one direction, one fault: an eigenvalue is
  compared to a hole-state DIFFERENCE. The gap that grows with occupancy is orbital relaxation on removal (Koopmans' theorem is
  the object being measured, not either kernel). Object/observer distinction (R 1578 type) at the level of the OBSERVABLE:
  the kernel eigenvalue and the served E_bind are different objects; the test's 'bracket' question was posed across that seam.
BEARING ON T0 (stated, not decided): a collapse-curve correction to the one-electron TFD potential — uniform or region-split —
  acts on the eigenvalue and cannot produce a Z-flat hole-state binding; the residue seen here is many-electron relaxation.
  T0(a)/(b) remain to be run as ruled; this finding predicts they move the eigenvalue, not this flatness. Chosen constants: none.
  Timing flag: none (PB-11.1/2/3 stated in session 11; scorer fault registered before result read). Nothing written to bank.