# FINDING — T7c-DYAUDIT: Dy hole bookkeeping audited; one unforced choice found and tested (session 22). Bridge-20 s3(4).
Files: t7c_dyaudit.py, t7c_dyaudit.jsonl, PREDICTION-T7C-DYAUDIT-SESSION-22.md. Object: banked SR-pol TS chain (t7c_pol / t7c_mult).
Read (no run): split() removes the half electron from the MINORITY channel on every 4f row (Dy 7up/2.5dn); holes (4,5)/(2,3)/(1,2)/(0,1)
match 4f10/12/13/14 minority counts; particle-hole CI symmetry (s20 audit); sign corr = pol + stab_n - stab_i; Lande level term on
J=L+S of both inverted multiplets. ALL FORCED. The one unforced choice: t7c_mult uses ONE F^k set (TS half-occupied orbital) for
both stab_n and stab_i; Slater/Condon-Shortley bookkeeping uses each configuration's own orbital.
## Run (4 rows x 3 SCFs; F2 neutral / TS / ion; stab with own orbital; delta = corr_own - corr_ts)
Yb 0.555/0.574/0.592  stab 0/0          delta 0       · Tm 0.536/0.557/0.575  stab_i -0.0336 -> -0.0347  delta +0.0011
Er 0.517/0.539/0.558  stab_n -0.0326 -> -0.0312, stab_i -0.076 -> -0.0787  delta +0.0040
Dy 0.471/0.501/0.523  stab_n -0.0707 -> -0.0664, stab_i -0.0303 -> -0.0316  delta +0.0055
PY1 HELD (ion > TS > neutral; spread 7-11 %, Dy 1 % over the stated 8 % ceiling — noted). PY2 HELD (Dy shallower 0.0055, still
over-bound: after SO -0.2904 vs -0.2745, residual -0.016). PY3 HELD (Er/Tm shallower 0.004/0.001, away from meas; Yb 0). PY4 HELD.
## Reading (bound): the Dy over-binding is NOT a hole-bookkeeping fault. Every bookkeeping element is forced except the F^k orbital
choice, and that choice moves Dy by 0.0055 (right way) and Er/Tm by 0.004/0.001 (wrong way) — a uniform TS-vs-own-orbital effect,
not a Dy anomaly. Dy stands at -0.016 (own-orbital + SO), the sole over-bound row; every other term (SIC -0.010, GB deeper, SO -0.0047)
moves it further. Which F^k convention the law carries is M's ruling: TS-orbital (one object, banked) or own-orbital (Slater form).
Faults: none. Predictions failed: none. No constant, no measured input.