# FINDING — item (3): F^k convention on SIC-noclamp and Z 4f orbitals, s23 (t7c_fkdens.py, t7c_fkdens_SIC.jsonl, t7c_fkdens_Z.jsonl). Rows Dy Er Tm Yb.
resid_Z0 with the banked (pol,own) Hund shift replaced:      Z0(pol,own) | SIC ts / own | Z ts / own
 Dy -0.0524 | -0.0546 -0.0551 | -0.0551 -0.0554     Er -0.0118 | -0.0192 -0.0114 | -0.0189 -0.0113
 Tm -0.0018 | -0.0054 -0.0012 | -0.0052 -0.0011     Yb +0.0041 | +0.0041 +0.0041 | +0.0041 +0.0041 (Hund-II = 0 for f^14)
 rms(4): SIC ts 0.0291 own 0.0282 | Z ts 0.0293 own 0.0283.  rms(Er Tm Yb): SIC 0.0118 / 0.0070 | Z 0.0116 / 0.0070.
RESULT: own-orbital better on BOTH densities; tie broken by 0.0048 on the three non-zero rows (> 0.001 pre-named alternative). Densities agree to 3e-4.
PF1 FAILED: F^2 moves 5-9 %, and on the SIC/Z chains the TS-orbital F^2 falls BELOW the neutral's (Dy 0.4584 < 0.4950 < 0.5346): the half-occupied
  entrant channel carries a half-weighted PZ-SIC (f_i = 1/2) and is more diffuse than its integer siblings -- the TS convention inherits an
  object-dependence the own-orbital form does not. (Formed after the run, R 1449.) PF2 FAILED (tie broken, pre-named direction). PF3 HELD.
RULING APPLIED (M, s23): own-orbital F^k Hund-II is STANDING, marked NEW, BASED ON THE SLATER FORM (Slater 1960; Condon-Shortley 1935: each
configuration's multiplet splitting from its own radial function), until a better attribution is found; if none is found it is PROPOSED,
REQUIRING VERIFICATION BY OTHERS IN THE FIELD. Attribution candidates flagged, NOT entered: Ziegler, Rauk & Baerends TCA 43, 261 (1977)
(multiplet Delta-SCF in the Xalpha/DFT frame); von Barth PRA 20, 1693 (1979). The TS-orbital form is recorded as the tested alternative.
Owed: the banked 4f SO/Hund column of TABLE-CHAIN-15 is on the pol chain; regenerated own-orbital Hund on SIC/Z shifts Er by +0.0004 only -- carried.