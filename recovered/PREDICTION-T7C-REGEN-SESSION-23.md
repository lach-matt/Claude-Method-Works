# PREDICTION — item (1) regeneration of the 15-row chain under F22.1 repair (SIC_NOCLAMP=1), s23
Written BEFORE the run. Object: t7c_corr2.scf_sic_corr, SIC_NOCLAMP=1, GB_EXACT=0 (banked PZ constants, so the shift isolates F22.1 alone).
Runs: 15 rows x corr in {None, U, P}. Ruled: bridge-22 s3(1), M "continue in order".
PR1  Every row's SIC base (corr=None) moves POSITIVE (shallower) under NOCLAMP; no row moves negative. Threshold: all 15 shifts > 0.
PR2  5d rows Gd, Lu shift within +0.003..+0.006 (La measured +0.0041 in s22 and must reproduce to 1e-4).
PR3  Ordering of shift by channel: 6s (Cs) >= 5d > 4d > 3d, and 4f smaller than 5d. Threshold: 4f rows each < the smallest 5d shift; 3d rows each < 0.004.
PR4  The GB increments shiftU, shiftP (corr row minus its own base) are unchanged from banked to within 5e-4 on every row — the clamp sits on the SIC
     channel, not on the correlation functional.
PR5  Containment score 9 CONTAINED / 5 OVER / 1 SHORT is UNCHANGED after re-scoring with the regenerated bases (SO/Hund columns carried as banked,
     stated: t7c_so 5d Lande and 4f own-orbital Hund-II/level-SO are computed on TS/pol orbitals, not on the SIC channel). Cu remains SHORT and worsens.
Failure of PR5 by exactly one row (Ti crossing to CONTAINED, or a 4f row crossing to SHORT) is the pre-named alternative.