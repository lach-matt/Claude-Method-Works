# PREDICTION — T7c-HFSR: scalar-relativistic Hartree-Fock (exact exchange) entrant object (bridge-20 s3(3); ruled s22). Written BEFORE the build.
Object: t7b_hf.HF (average-of-configuration Fock exchange, s18) with the local operator replaced by the banked KH form (t7c_kernel.qlog, verbatim)
built from the LOCAL part of the Fock potential (nuclear + Hartree + within-shell local exchange), the nonlocal exchange X entering as source
-2 M r^{3/2} X (kinetic operator -(1/2M)d^2 moved to the right; Cowan-Griffin 1976 form uses source unmodified: sensitivity to be reported).
No constant beyond c = 137.035999. Attribution: Fock 1930; Koelling-Harmon 1977; Cowan-Griffin JOSA 66, 1010 (1976).
Gates (must pass before any row is read):
 G1  c = 1e6 reproduces banked t7b hf_ts on Sc (-0.2681) to 1e-4;  He 1s eps -0.91796.
 G2  mode='hfs' with SR reproduces banked t7c_ts (spin-averaged local SR TS): La -0.2017, Sc -0.2686 to 2e-4.
Predictions (thresholds chosen now), rows La/Gd/Lu 5d and Dy/Er/Tm/Yb 4f, plus Sc/Fe/Cu 3d controls; quantity hf_ts_sr (Janak-consistent TS):
 PH1  5d: hf_ts_sr - hf_ts (nonrel) = +0.020..+0.045 (SR destabilisation, same as local: t7c_ts - hfs_ts = +0.027/+0.032/+0.039).
      Consequence: SR-HF 5d edge vs meas remains shallow by >= 0.015 on all three -> HF is not the 5d closure. (FINDING-T7C-SHELL on record.)
 PH2  4f: SR-HF TS is SHALLOWER than meas by 0.06-0.14 Ha on all four (nonrel HF already +0.10-0.12 above HFS; SR adds +0.15-0.19 shallow on 4f
      per srdec-4f) -> HF is not a closure for f; the local kernel is closer to measurement on 4f than exact exchange is.
 PH3  3d controls: |hf_ts_sr - hf_ts| <= 0.010 (SR small at 3d).
 PH4  Source-form sensitivity (M vs 1 on the exchange source): |delta eps| <= 0.001 on La 5d.
No measured input; meas comparison only.