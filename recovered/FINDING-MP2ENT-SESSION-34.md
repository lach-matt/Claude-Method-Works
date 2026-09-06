# FINDING-MP2ENT (s34) — the second-order entrant-core pair correlation is BUILT (mp2_ent.py, one file, no constant) and run on the six class rows and Yb.
The undelivered FRACTION of the entrant's pair correlation under the local chain form ranks with the O-path residual (PN-2 HELD); the absolute
second-order numbers are class-FLAT on the d rows (PN-1 FAILED on magnitude); Yb's sibling term is 63 % of its entrant correlation (PN-4 HELD).
Nothing entered; not a closure — a class-shape fact and a bound.
Build: radial eigenproblem on the log mesh (u = r^{1/2} y; -1/2 y'' + [(l+1/2)^2/2 + r^2 V] y = E r^2 y, symmetric via y = y'/r), spin-averaged HFS neutral
potential (t5_scf.scf_occ, qtail=1), r_min = 1e-3/Z (conditioning: eps_mach/(h^2 r_min^2)), r_max 60, 700 pts, virtuals = all box states below 300 Ha,
l <= 3; LS-coupled pair matrix elements with 6j/3j from sympy (cached), R^k via Y_k; open core shell weighted N_b/(2(2l_b+1)) (average of configuration);
negative-denominator pairs EXCLUDED and counted (La: 175 — the local 4f collapses to -0.29 below 5d/6s, a genuine near-degeneracy of the local HFS,
stated as a bound on La). Occupied eigenvalues reproduce the SCF to <= 2e-4 (Sc 3d -0.13966/-0.13964, Cs 6s -0.12023/-0.12033, Yb 4f -0.27456/-0.27434).
Gate He 1s^2, k<=3: -0.0490 (k<=0 -0.0207, k<=1 -0.0445, k<=2 -0.0481) against the RECALLED HF-orbital second order -0.0374: outside my stated window
[-0.045,-0.028] by 0.004 — REPORTED, not tuned: the local HFS 1s (-0.743 vs HF -0.918) is shallower, denominators smaller, the k-series shape is the
known one (s < p dominant, d/f small). Faults: two solver forms tried and refused before the r_min bound (generalized eigh and tridiagonal select both
lose the valence eigenvalues to conditioning on Z >= 55: recorded as the reason for RMIN, F34.4, closed).
Results (TABLE-MP2ENT-SESSION-34.txt), E2_ent = sum_b E2closed(a,b)/(2(2l_a+1)) [+ (2/N_a) E2closed(a,a)]:
  Sc 3d -0.0652 · Y 4d -0.0631 · Gd 5d -0.0554 · La 5d -0.0626 (175 pairs excluded) · Lu 5d -0.0666 · Cs 6s -0.0240 · Yb 4f -0.1786 (core -0.0667, siblings -0.1119).
PN-1 FAILED on magnitude/order: the d rows are flat at 0.055-0.067 (predicted 3d > 4d > 5d, 5d 0.02-0.04); Cs smallest and Yb largest held.
PN-2 HELD: 1 - |DEc_chain|/|E2_ent| = Sc 0.51 · Y 0.56 · Gd 0.56 · La 0.58 · Lu 0.59 · Cs 0.71 — Sc smallest, Cs largest, monotone in rs_w with Y/Gd tied,
  the same shape as resid_O (Sc<Gd<La<Lu<Y<Cs) and as the post-UEG residual of FINDING-A. Read as: the local chain form delivers ~half of the entrant's
  frozen-orbital second-order pair correlation on the compact rows and less on the diffuse ones; the DIFFERENCE is not the residual in size (frozen
  second order on local orbitals overestimates — He x1.3 — and the ion's own correlation relaxation, which reduces the removal correlation, is absent),
  but its class SHAPE is the residual's shape. Bound, not closure.
PN-3 NOT RUN (radial partition of the pair density not implemented in this build; owed).
PN-4 HELD (Yb): sibling term 0.112 of 0.179 (63 %). The 4f +0.09 shortfall's candidate is the same-shell pair correlation the SIC-corrected local form
  handles as self-correlation subtraction while the 13-sibling correlation is real: horizon item (3) now has a derivable object and a number to test
  against (0.09 vs 0.11 lower-bound frozen second order, before the ion's relaxation is subtracted).
Flag F34.3 (record, stated not fixed): the "class row under S" of FINDING-GDS is S on Gd only; Sc/Y/La/Lu/Cs O-path DEc are the R form (frachf_ring). The
  spread statement is across two correlation forms differing by <= 0.001 on those rows (s32 PS-4). frachf_S on the other five rows is OWED before the
  law statement (5 runs, ~25 s each).
Owed to T4: R 1920 mp2_ent built (form, gates, bounds) · R 1921 PN-1 failed: d rows flat at second order · R 1922 PN-2 held: undelivered fraction ranks with
  the residual · R 1923 PN-4 held: Yb sibling 63 % · R 1924 F34.3 · R 1925 F34.4 · R 1926 La 4f collapse bound.
Files (pack34): PREDICTION-MP2ENT · mp2_ent.py · mp2_ent.jsonl · TABLE-MP2ENT-SESSION-34.txt · this finding.