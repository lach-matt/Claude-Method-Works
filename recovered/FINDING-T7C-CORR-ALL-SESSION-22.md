# FINDING — T7c-CORR-ALL: GB bracket on all 15 rows; the one-table chain restatement (session 22). Bridge-21 s3(1)+(2).
Files: t7c_corr_all.py, t7c_corr_all.jsonl (15 rows: 4 carried from t7c_corr s21, 11 run s22 = 33 SCFs), t7c_pol_s22.jsonl (SR-pol TS Ti/Cr/Ni,
3 SCFs, for the table), TABLE-CHAIN-15-SESSION-22.txt, PREDICTION-T7C-CORR-ALL-SESSION-22.md, COMPARE-FK-CONVENTION-SESSION-22.md.
## GB shifts (U / P): Cs 6s -0.0038/-0.0022 · 3d Sc -0.0262/-0.0098 Ti -0.0273/-0.0106 Cr -0.0271/-0.0126 Fe -0.0311/-0.0100 Ni -0.0330/-0.0114
Cu -0.0313/-0.0118 · Y 4d -0.0202/-0.0084 · 5d La/Gd/Lu -0.0186/-0.0082, -0.0201/-0.0089, -0.0191/-0.0083 · 4f Dy/Er/Tm/Yb -0.0365/-0.0141,
-0.0372/-0.0148, -0.0374/-0.0151, -0.0378/-0.0154. Compactness-ordered 4f > 3d > 4d/5d > 6s; flat within a shell (4f U spread 0.0013).
## Chain per row (SR-pol TS -> +SIC on the SR object -> +SO/Hund -> residual vs recalled/measured -> GB bracket), see TABLE file:
CONTAINED (9): Fe +0.023, Ni +0.021, Y +0.0125, La +0.0138, Gd +0.0141, Lu +0.0112, Er +0.023, Tm +0.032, Yb +0.037.
OVER-SHOT (5): Cs -0.002, Sc -0.008, Ti +0.001, Cr -0.000 (residual already <= |P| before GB), Dy -0.015 (GB deepens to -0.029..-0.051).
SHORT (1): Cu +0.038 > |U| 0.031.
## Score: PG2 HELD (Fe/Ni in, Sc/Ti/Cr over, Cu short). PG3 HELD (Dy worsens; Er/Tm/Yb 3/3 in). PG4 direction HELD, magnitude FAILED (Cs U -0.0038 not
-0.007..-0.014). PG1 magnitudes HELD on 3d/4f/P-6s; FAILED on 6s U (0.0038 < 0.005) and on the U/P ratio clause (2.2-2.5 predicted; observed
6s 1.7, 5d 2.3, 4f 2.5, 3d 2.2-3.1, Fe 3.1). Whole-picture prediction HELD: the GB bracket is NOT a closure on 15 rows -- it brackets the
d/f rows whose residual after SIC is +0.011..+0.037 and over-shoots every row SIC has already closed (Cs, Sc, Ti, Cr) and Dy.
## NEW, unpredicted, and it QUALIFIES bridge-21 (C): "SIC commutes with SR to 0.0015" was read on 4d/5d only. On 4f it FAILS: SIC shift on
the SR object is +0.0012/+0.0084/+0.0119/+0.0157 (Dy/Er/Tm/Yb) vs nonrel t7a_all -0.0096/-0.0040/-0.0012/+0.0016 -- SR adds +0.011..+0.014
to the 4f SIC shift on every row (SR contracts 4f, each sibling's V_SIC on the entrant grows -> beta_4f grows; the direct term is unchanged in
sign). PC1's reach: HELD on 4d/5d, FAILS on 4f by 0.011-0.014. Entered per R 1449 (claim qualified, not silently dropped). Consequence for
the 4f residual: after SR-SIC + own-orbital Hund + level SO, Er/Tm/Yb are +0.023/+0.032/+0.037 shallow (not +0.015/+0.020/+0.021 as in the
COMPARE file, which was on the pre-SIC object). Same sign as 5d, ~2x size; the GB bracket contains all three.
## Reading (bound): one attributed chain, no constant, brackets 9 of 15 rows within U/P and over-shoots the 5 rows on which SIC alone
already lands, with Cu (late-3d, SIC destabilises +0.024) the one row the chain cannot reach. The residue is not shell-uniform: it is where SIC's
indirect term (beta*N_sib) is largest. Dy: every term deepens it. Not a closure; the shape of the failure is now the same on all 15 rows.
Faults: none. Predictions failed: PG1 (6s U magnitude; U/P ratio), PG4 (magnitude). No constant, no measured input; recalled values comparison only.