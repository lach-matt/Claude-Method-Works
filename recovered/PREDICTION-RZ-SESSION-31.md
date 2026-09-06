# PREDICTION — the 15 chain rows under form R vs form Z (bridge s30 §3 (1)(iii)); written BEFORE the hook is run.  s31.
Design (before any run): t7c_corrz gains corr='R' = corr_ring.v_R with the identical interface (total-density Vc AND per-orbital SIC vci); everything else
verbatim. Both forms are rerun under the STANDING convention SIC_NOCLAMP=1 SUBCELL=1 into NEW files (t7c_corrz_sc.jsonl, t7c_corrR.jsonl); the s23 Z rows
(t7c_corrz.jsonl, SUBCELL unset) are the reference for PZ0. Batches <= 3 species per call. Rows: Cs Sc Ti Cr Fe Ni Cu Y La Gd Lu Dy Er Tm Yb.
PZ0  Z under SUBCELL=1 reproduces the s23 Z rows to |dE| <= 0.001 Ha on all 15 (cellcut: default byte-identical; Ti gate 32 -0.38064 vs -0.3806).
PZ1  shiftR (= ER - base) is DEEPER than shiftZ on every row (R delivers more correlation than the truncated Z on the class rows: gain +0.22..0.29 of required).
PZ2  the ratio shiftR/shiftZ is UNIFORM across the 3d rows Sc..Cu: within +-10 % of its Sc value (FINDING-RING: the gain is uniform, Sc/Y 0.95).
PZ3  4f rows (Dy Er Tm Yb) move deeper under R by a ratio in the SAME band as 3d (form R changes 4f rows too, bridge (3)); prediction: 4f resid +0.09 is
     reduced by <= 0.01 Ha — R does NOT close the 4f object.
PZ4  Cs: shiftR/shiftZ ~ 2.5-3.0 (frachf_ring 0.45/0.16 = 2.8) — the outlier ratio, the zeta~1 cut half-lifted, not lifted.
PZ5  the 'inside' [U,P] bracket count: R puts MORE rows below U (over) than Z (Z: Fe Ni already outside); predicted >= 4 rows below U under R.
COMPARE-RZ criterion (stated before the run): the winner is the form whose residual against the RECALLED (not entered) measured IEs on the 15 rows has the
smaller spread across the three shell classes (3d, nd>=4, 4f) — a uniform residual is a form property; a class-dependent one is the object under study.
Not a criterion: smaller mean residual (Cs/Y RECALLED-NOT-ENTERED; no fitting to measured values).