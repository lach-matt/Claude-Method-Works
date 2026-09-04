# PREDICTION-HFCORR (s37, item 3) — written BEFORE the run. Ruling: HF is the walk's field (M, s37); item 3 = read the record chain against the tables and add
the standing correlation form (S: SOSEX-screened GB-Z, frachf_S/FINDING-FRACHFS5, self-consistent via hfc2 CORR with eps_c=eps_S, v_gbz=v_S) to Stage 2 on the
13 d/s rows: D_rel(x) = (E_HF+E_c^SIC)(neu) - (E_HF+E_c^SIC)(neu-x). Same removals as nlwalk_hf; nlwalk_hfc.py -> nlwalk_hfc.jsonl. Nothing entered; no constant.
Record read (done): DEc_S on the O path = Sc 3d -0.0319 · Y 4d -0.0275 · La 5d -0.0262 · Lu 5d -0.0270 · Cs 6s -0.0068 (d entrant correlates ~4x an outer s).
PC1  Correlation deepens the d removal MORE than the s removal on every row: dgap := gapHFcorr - gapHF < 0 on all 13, size 0.010-0.030.
PC2  Th (+0.008) flips to s-first (record: s-first) and Gd (-0.0002) deepens negative: both HELD -> the two s-first exceptions of Stage 2 close.
PC3  The d-first rows at +0.024..+0.028 (Ac Pa U Hf) SURVIVE: the s partner correlates too (7s/6s beside a d/f core: -0.010..-0.018), so |dgap| < 0.024 on
     those rows; HF+corr scores 13/13 with margin >= 0.005 on every d-first row. (If it fails, it fails on Ac first — the smallest margin, 0.024.)
PC4  The local-minus-HF pair offset (+0.034 +- 0.007, Stage 3) shrinks to +0.015..+0.025 (the local walk already carries S-correlation; what remains is the
     exchange seam proper) and STAYS class-flat (sd <= 0.010 on n>=4 rows) with ~0 at Sc.
PC5  On the f frontier HF+corr keeps HF's order (La 4f shallower than 5d; Ce Pa U f entrant deepest): correlation on f removal is larger (-0.03..-0.05) but
     the HF gaps there are 0.10-0.16.
Read against R 1436/1439/beta_nl to be written AFTER the run in the finding, from the two-field tables (no design follows it).