# FINDING-B2 (s35) — candidate (b): the remainder after (a) is the RELAXATION DIFFERENCE between the paths measured from ONE frozen reference, and the
correlation difference is small (|b2| <= 0.002 Ha). With relaxation so measured, seam = -Delta_x + (relax_O - relax_E) is an IDENTITY; its only test is
whether the E-path DSCF recomputed independently reproduces the record E_DSCF: chk = Sc +0.0016 · Cs -0.0004 (CLOSED at <= 2 mHa, non-relativistic) ·
Y -0.008 · La -0.024 · Gd -0.035 · Lu -0.037 (the t5 reference is NON-RELATIVISTIC; the record E path is SR: the chk on nd/5d rows is the SR shift of the
E-path removal, stated as a bound, not closed). Run: xseam_relax.py, six rows, three tool calls; TABLE-B2-SESSION-35.txt.
Numbers (Ha, D = E_neu - E_ion): relax_E Sc +0.105 · Y +0.064 · La +0.062 · Gd +0.067 · Lu +0.064 · Cs -0.007; relax_O(t5-referenced) Sc +0.093 · Y +0.062 ·
La +0.075 · Gd +0.088 · Lu +0.095 · Cs -0.002; rem = relax_O - relax_E = Sc -0.0116 (target -0.0100) · Cs +0.0050 (target +0.0046) · Y -0.002 (target -0.011)
· La/Gd/Lu +0.013/+0.021/+0.031 (targets -0.011/-0.014/-0.006; rem - target == -chk exactly). Correlation split b2 = DEc_O - DEc_E: Sc -0.0017 · Y -0.0016 ·
La -0.0009 · Gd -0.0007 · Lu -0.0011 · Cs +0.0014 -> the remainder is RELAXATION, not correlation, on every row.
Also found: the O path relaxes MORE from the common frozen reference (0.093 Sc) than from its own Koopmans point (0.069 Sc, hfdscf.jsonl) by 0.024-0.066 —
the frozen reference is load-bearing and must be stated with every relaxation number (R 1578 seam of the "relaxation" object).
Predictions: PB2-1 sign HELD, size FAILED (b1 = +0.09..+0.12 on d rows, x8-12: exchange-only relaxation is virial-cancelled by kinetic+Hartree; F35.1);
PB2-2 FAILED (Cs b1 -0.021), the b2 sign on Cs (+) HELD; PB2-3 HELD on Sc/Cs (<= 2 mHa), FAILED on Y/5d for the stated mechanism (no SR in the reference);
PB2-4 FAILED (Sc/mean(nd) = 1.21 vs 1.5-3.0: relaxation is class-flat, unlike Delta_x); PB2-5 (post-result, F35.1) FAILED (2 of 6 within x0.5-2).
Reading (bound): the exchange seam O_DSCF - E_DSCF is (a) frozen entrant exchange LSD+SIC vs HF, minus (b) the excess relaxation of the local functional
over HF (Sc 0.012, Cs -0.005), and (b) is not correlation. NOT closed on Y/La/Gd/Lu until the frozen reference is built in the SR machinery (t7c_cuaudit_S
channels: total energy on the neutral SR-SIC-S orbitals with the entrant removed) — one build, no new physics; the SR shift of the removal (0.008/0.024-0.037)
is the number that build must recover. Nothing entered; no constant; no measured input (record seam and D_tot enter the comparison column only).
Owed to T4: R 1932 xseam_relax built · R 1933 exchange-only relaxation refused on size (F35.1) · R 1934 seam identity on one frozen reference; Sc/Cs closed
at 2 mHa · R 1935 correlation difference between paths <= 0.002 · R 1936 frozen reference is load-bearing (0.024-0.066) · R 1937 SR reference owed for nd/5d.
Files (pack35): PREDICTION-B2 · FAULT-F35.1 · xseam_relax.py · xseam_relax.jsonl · TABLE-B2-SESSION-35.txt · this finding.