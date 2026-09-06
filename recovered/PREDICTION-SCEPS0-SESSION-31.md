# PREDICTION — Sc eps(0) by a run at f=1e-3 in place of the linear extrapolation eps(0):=2 eps(1/4)-eps(1/2) (bridge s30 §3 (2); s29 flag).  s31, before the run.
Standing Sc corr-path eps(f): 0.25 -0.263465 · 0.5 -0.288282 · 0.75 -0.318801 · 1.0 -0.355230 (convex; second difference +0.0057). Linear extrapolation gave
eps(0) = -0.238648; a quadratic through 1/4,1/2,3/4 gives -0.2444.
PS1: eps(f=1e-3), corr path, lies in [-0.248, -0.241] (i.e. the linear extrapolation is too shallow by 0.003-0.009 on this twice-steeper row).
PS2: with the run eps(0), Sc's janak_gap_corr falls from 1.2e-3 to |gap| <= 6e-4, joining the other class rows (the s29 statement "quadrature, not Janak").
PS3: the HF path behaves the same way (its gap moves by the same sign, magnitude within a factor 2 of the corr path's).
Numerics: HFCf as frachf.path with f=1e-3 (frac hook), corr and hf, one SCF each; nothing else changes; the standing frachf.jsonl row is not overwritten (a
side file frachf_eps0.jsonl). No constant.