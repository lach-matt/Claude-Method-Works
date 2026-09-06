# FINDING — second-order (self-consistent, integer-occupation) chain correlation on Cs/Gd: POSITIVE, and it moves the s26 class rows too.  s27, bridge-26 §3(4)
Files: hfc2.py hfc2.jsonl PREDICTION-HFC2-SESSION-27.md (written before any run). No constant beyond c; meas RECALLED-NOT-ENTERED. Not a closure.
## Gate PC1 HELD: CORR=0 reproduces s26 D_HF Cs 0.12779 and E_neu/E_ion to 1e-5.
## Result (second-order piece := obj_2 − obj_s26, obj_2 = −[(E_HF+E_c^SIC)_ion − (E_HF+E_c^SIC)_neu] with the chain-Z correlation potential in the SCF):
   Cs +0.0008 · Gd +0.0083 · Y (control) +0.0082.   E_HF itself moves < 0.0005 (orbital relaxation under v_c is negligible); the whole piece is
   E_c^SIC(ion) − E_c^SIC(neu) at INTEGER occupation vs s26's Δ_c = TS-midpoint slope: Y 0.0202 vs 0.0280, Gd 0.0172 vs 0.0251, Cs 0.0024 vs 0.0032.
   PC2 FAILED (positive on all three) · PC3 FAILED (Cs +0.012 -> +0.0128) · PC4 FAILED (Gd +0.018 -> +0.026) · PC5 FAILED (Y shifts 0.008 > 0.005).
## Reading. The Cs/Gd shortfall is NOT second-order local correlation: making the correlation self-consistent makes every row SHALLOWER, uniformly
   ~0.008 on d rows and 0.001 on Cs. Stop rule fired; no scan.
   THE LARGER FINDING, not predicted (R 1449 timing flag): two derivable forms of the same correlation term disagree by 0.008 Ha on the like-for-like
   class rows — the TS-midpoint first-order Δ_c (s26; the chain's own convention, entrant SIC at weight 1/2) and the integer-occupation E_c^SIC
   difference (this file). s26's "(a') closes to <= 0.008 on Y La Lu Sc" was computed with the former; with the latter it reads ~+0.013 on Y/Gd.
   The gap is the f-nonlinearity of the correlation SIC term (f·E_c[f n_ent] is not linear in f) — the correlation analogue of the s24/s25 frozen-mask
   f^(4/3) exchange nonlinearity — plus whatever the midpoint slope misses at second order in E_c[n_TS]. Which form is admissible in the law is a
   RULING (both are parameter-free; the chain uses the midpoint form throughout, so consistency argues for it), and the s26 (a') margin must be
   restated with the gap on record either way.
## Open, stated: La, Lu, Sc, and the 3d/4f rows under obj_2 (not run — outside this item's ruling); the size of the pure f-nonlinearity of E_c^SIC
   separated from the midpoint-vs-integer difference (a 3-point f evaluation would split it; not opened).
