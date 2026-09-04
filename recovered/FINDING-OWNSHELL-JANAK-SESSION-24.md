# FINDING — bridge-23 s3(2) own-shell class and s3(3) Dy, session 24. Files: t7c_cuaudit.py (env FENT, FOCC), t7c_ownshell_run.py,
t7c_ownshell.jsonl (test C: mode none/ent/all on Sc, Fe; test D: eps(f) on all 15 rows), janak_table.py, TABLE-JANAK-SESSION-24.txt,
exent.py, exent.jsonl, ratio.txt, PREDICTION-OWNSHELL-SC-SESSION-24.md (five prediction blocks, each written before its run).
No constant, no measured input; Cs/Y comparison values RECALLED-NOT-ENTERED; so/hund column carried from TABLE-CHAIN-15 (stated).
## Test C (Z chain SIC decomposition): Sc none -0.3061 / ent -0.3226 / all -0.3211 -> direct -0.0166, indirect +0.0015 (N_sib 0).
Fe none -0.4164 / ent -0.4363 / all -0.4126 -> direct -0.0199, indirect +0.0237. PO1 HELD, PO5 HELD, PO2 FAILED (Z direct is 0.59 x the
pol-chain direct: the correlation SIC opposes the exchange SIC on the entrant). Sc is over-bound -0.0115 with NO SIC at all.
## Test D (Janak): eps(f) of the entrant channel at f in {0.001,0.05,0.15,0.25,0.5,0.75,1.0} with f in both the density and the PZ SIC
weight; DE_J = int_0^1 eps(f) df (interpolated in f^(1/3)) is the functional's own DSCF removal energy. On EVERY row eps(f) is deep at
f->0 (the empty orbital, no self-repulsion), SHALLOWEST at f = 1/2..3/4, deeper again at f = 1 (PZ SIC flattens the LDA slope only
partly). PO4 FAILED (monotone). The Slater TS point eps(1/2) sits at the least-bound point of the curve on all 15 rows.
TABLE-JANAK-SESSION-24 (resid = chain - meas): DE_J - eps(1/2) and resid_TS -> resid_J:
  Cs 6s -0.0022 (+0.0003 -> -0.0019) · Y 4d -0.0112 (-0.0012 -> -0.0124) · La -0.0097 (+0.0010 -> -0.0087) · Gd -0.0106 (+0.0022 ->
  -0.0084) · Lu -0.0101 (-0.0012 -> -0.0113) · Sc -0.0170 (-0.0265 -> -0.0435) · Ti -0.0200 (-0.0159 -> -0.0359) · Cr -0.0230
  (-0.0155 -> -0.0385) · Fe -0.0272 (-0.0159 -> -0.0430) · Ni -0.0321 (-0.0120 -> -0.0440) · Cu -0.0340 (+0.0146 -> -0.0194, SO in)
  · Dy -0.0372 (-0.0524 -> -0.0897) · Er -0.0400 (-0.0118 -> -0.0519) · Tm -0.0414 (-0.0018 -> -0.0431) · Yb -0.0426 (+0.0041 -> -0.0385).
PO3 HELD (Sc), PO6-PO7 HELD (Fe), PO8 HELD (Ti Cr Ni in [-0.055,-0.031]), PO9 HELD (La control), PO10 HELD (Er), PO11 HELD (Cu joins the
3d class; the "short" shape is gone), PO12 HELD (Tm Yb Dy; Dy persists at -0.090), PO13 HELD (closed class within -0.016).
RESULT (class statement, predicted at PO11-13 and held): under the functional's own DSCF the residual is ONE monotone function of the
entrant's compactness -- 6s -0.002 · 4d/5d -0.008..-0.012 · 3d -0.019..-0.044 · 4f -0.039..-0.052 -- plus Dy at -0.090. The 3d class
tightens from spread 0.015 (TS) to 0.008 (Janak); the three TS shapes (own-shell over-binding; Cu short; Dy) reduce to TWO (compact-shell
over-binding; Dy). The TS half-point is a shell-dependent MASK, not the origin: it hides 0.002 (6s), 0.010 (5d), 0.017-0.034 (3d),
0.037-0.043 (4f) of the functional's over-binding.
## PO14 (closed-form mask from PZ-81 scaling, -0.0583|E_x[n_ent]|): FAILED as stated (ratio in [0.7,1.3] on 5/15) -- with structure:
ratio 1.40-1.51 on all eight compact rows (Cr Fe Ni Cu Dy Er Tm Yb; mean 1.44), 1.19-1.31 on Sc Ti Y La Gd Lu, 0.52 on Cs (ratio.txt;
|E_x[n_ent]| 0.073 (Cs) .. 0.507 (Yb), r_mean 5.47 .. 0.82). The exchange scaling carries ~70 % of the mask; the remainder is a
shell-dependent residue (correlation-SIC and total-density LSD curvature; candidate, not run). Not a fit: read off the run.
## Interpretation (formed after the runs, R 1449): eps(f) is not flat -> the functional violates piecewise linearity of E(N) (the exact
condition under which TS = DSCF = removal energy). The class deviation is that curvature integrated; it is a property of the LSD-x +
GB-Z + PZ-SIC functional on compact nodeless shells, not of the entrant bookkeeping (item (1)B, tests C-D) and not of the TS weight.
Item (2) CLOSED: the named candidate (entrant SIC self-term vs siblings) is EXCLUDED as the origin; the origin is named and quantified.
## Item (3) Dy: per the ruling, stated as the OBJECT'S BOUND. Under Janak Dy sits 0.04-0.05 outside a 4f class that is itself uniform to
+-0.007 (Er Tm Yb -0.052/-0.043/-0.039). Observation, not a claim: Dy is the one 4f row whose own-orbital Hund-II term is negative
(-0.0395, the neutral f^10 term dominating the ion f^9 term) and its excess over the class (~ -0.045) is of that size; Er (+0.053) and
Tm (+0.048) show no matching excess vs Yb (Hund 0), so the F^k scale is not the cause at the 0.01 level. No candidate; M may name one.
STANDING AFTER (2)-(3): the chain of s23 with two estimators recorded side by side (TS eps(1/2); Janak DE_J). NOT a closure. Failure has
two shapes under DE_J. Candidate for M's ruling (not run): the next link is a piecewise-linearity (Koopmans) condition on E(f) --
attribution to be searched (Perdew-Parr-Levy-Balduz 1982; Janak 1978; Slater 1972 TS) -- with the derivability rule deciding whether
any such construction enters.
Faults: none new. Predictions failed: PO2, PO4, PO14 (each with its reason above).
