# FINDING — eps(0) by a run at f=1e-3 (frachf_eps0.py, frachf_eps0.jsonl; frachf.jsonl untouched) on the six class rows.  s31, item (2).
row  eps0_lin   eps0_run  | corr gap lin -> run   | hf gap lin -> run     (Ha; gap = D - Simpson(0,1/2,1))
Sc   -0.238648  -0.246301 | -0.001188 -> +0.000087 | -0.000728 -> -0.000008
Y    -0.190160  -0.191929 | -0.000605 -> -0.000310 | -0.000392 -> -0.000019
La   -0.204052  -0.203621 | -0.000272 -> -0.000344 | -0.000240 -> +0.000042
Gd   -0.187661  -0.188503 | -0.000451 -> -0.000311 | -0.000215 -> +0.000098
Lu   -0.159628  -0.160511 | -0.000372 -> -0.000225 | -0.000201 -> +0.000113
Cs   -0.129525  -0.129498 | -0.000028 -> -0.000033 | -0.000027 -> -0.000025
PS1 HELD: Sc eps(1e-3) = -0.24630 in [-0.248,-0.241]; the linear extrapolation was too shallow by 0.0077 on the twice-steeper row.
PS2 HELD: Sc janak_gap_corr 1.2e-3 -> 8.7e-5. The s29 flag closes: it was quadrature, not Janak. Sc's Janak row is clean.
PS3 HELD: HF path same sign; Sc hf gap 7.3e-4 -> 8e-6.  Extended (not predicted; stated as run, cheap and bounded, same operation on the same six rows):
    the HF-path gap goes to <= 1.1e-4 on ALL six rows (Janak exact on the HF path to 1e-4 with a run eps(0)); the corr-path gap stays 2-3.5e-4 on Y Gd Lu La
    (unchanged in size, sign persists) — a residual of the CORRELATED path only, at 3e-4, ordered nd>=4 > 3d ~ 6s. Not opened; recorded as a bound.
Files: frachf_eps0.py, frachf_eps0.jsonl (6 rows). Gate: python3 frachf_eps0.py 21 -> must SKIP; if deleted reprints corr eps -0.246301 gap_run 8.7e-05 (12 s).
Timing flags: none for PS1-3; the five-row extension followed the Sc read (flagged as extension, no prediction attached).