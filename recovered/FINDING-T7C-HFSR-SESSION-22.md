# FINDING — T7c-HFSR: scalar-relativistic exact-exchange (HF) entrant object; SR-HF is not a closure on 5d or 4f (session 22). Bridge-20 s3(3).
Files: t7c_hfsr.py (HFSR subclass of banked t7b_hf.HF; local operator = banked t7c_kernel.qlog on the LOCAL part of the Fock potential;
nonlocal exchange as source -2 M r^1.5 X), t7c_hfsr_run.py, t7c_hfsr.jsonl (12 rows: 10 species + Sc c=1e6 gate + La srcM=0), PREDICTION-T7C-HFSR-SESSION-22.md.
Attribution: Fock 1930; Koelling-Harmon 1977; Cowan-Griffin JOSA 66, 1010 (1976) (relativistic operator on the local potential, exchange added
unmodified). c = 137.035999 only. Gates: G1 He 1s c=1e6 -0.91796; Sc HF-TS c=1e6 -0.2681 == banked t7b (exact); G2 hfs-mode SR: Sc -0.2686,
La -0.2017 == banked t7c_ts (exact). All passed before any row was read.
## Rows (hf_ts_sr = SR Fock eps(N-1/2) + J~/2, Janak-consistent as t7b; shift_sr = hf_ts_sr - hf_ts(nonrel); local = t7c_ts - hfs_ts; dev = hf_ts_sr - meas)
 3d  Sc  hf_ts -0.2681 -> sr -0.2610  shift +0.0071 (local +0.0066)  dev +0.034 · Fe -0.4413 -> -0.4282 +0.0131 (+0.0118) dev -0.032 ·
     Cu -0.2806 -> -0.2698 +0.0108 (+0.0084) dev +0.114
 5d  La  -0.2329 -> -0.2036  +0.0293 (+0.0265)  dev +0.035 · Gd -0.2262 -> -0.1886 +0.0376 (+0.0323) dev +0.053 · Lu -0.2038 -> -0.1563 +0.0475 (+0.0394) dev +0.043
 4f  Dy  -0.3889 -> -0.2021  +0.1868 (+0.1657)  dev +0.072 · Er -0.3997 -> -0.1965 +0.2032 (+0.1789) dev +0.059 · Tm -0.4030 -> -0.1911 +0.2119 (+0.1858) dev +0.093 ·
     Yb -0.4048 -> -0.1841 +0.2207 (+0.1927) dev +0.143
 PH4 La srcM=False (Cowan-Griffin source): -0.2038 vs -0.2036 -> 0.0002.
## Score
PH1 HELD (5d shift +0.029/+0.038/+0.048, Lu 0.0025 over the 0.045 ceiling; edge vs meas +0.035/+0.053/+0.043, all >= 0.015). SR-HF is not the 5d closure.
PH2 HELD (4f shallow +0.06..+0.14; Yb 0.003 over the 0.14 ceiling). HF is not a closure for f; the local kernel is closer to measurement on 4f.
PH3 FAILED on magnitude (Fe +0.013, Cu +0.011 > 0.010; Sc held); sign held.
PH4 HELD (0.0002): the exchange-source form is immaterial at the 5d entrant.
## Observed, not predicted (offered, not claimed): the SR destabilisation of the entrant is LARGER under exact exchange than under local exchange
on every row, ratio shift_sr(HF)/shift(local) = 3d 1.08/1.11/1.29 · 5d 1.11/1.16/1.21 · 4f 1.13/1.14/1.14/1.15 -- ~+14 % on 5d/4f, i.e. the
indirect SR term (6s/core contraction, s20 (b2)) is 14 % stronger when the core is HF. Consistent with (b2), no bearing on the residual sign.
## Reading (bound): SR-HF CONFIRMS bridge-20's prediction -- exact exchange does not close the 5d edge (it widens it: HF 5d edge +0.035..+0.053
vs local-chain residual +0.011..+0.014 after SIC/SO) and over-shoots 4f by 0.06-0.14. The one-chain standing (bridge-21 s2) is unchanged.
Faults: none. Predictions failed: PH3 (magnitude). No constant, no measured input; meas comparison only.