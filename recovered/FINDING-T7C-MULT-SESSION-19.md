# FINDING — the mixed-sign 4f scatter IS the multiplet coordinate (session 19, bridge-18 s3(3), R 1665)
Bank restore-point-2_13 (R 1700) unchanged. Findings only. Instrument t7c_mult.py.
## Object
meas = −(IP + E_hole) is LEVEL-to-LEVEL (neutral ground level → lowest J level of the ion's 4f^{n−1}6s²). t7c_pol is the spin-polarised
configuration average, i.e. the average of the max-S manifold. The gap between them is Hund-II: stab(k) = E(lowest L term) − E(max-S manifold
average) for k same-spin f electrons (holes for n>7: Dy 4→5, Er 2→3, Tm 1→2, Yb 0→1), computed by exact CI over the C(7,k) all-parallel-spin
determinants with F^k (k=2,4,6) integrated from OUR 4f orbital. corr = t7c_pol + stab(neutral) − stab(ion). Nothing measured enters; no constant.
Gate: term degeneracies and Hund ordering (f² ³H<³F<³P 11/7/3; f³ ⁴I lowest 13; particle-hole exact). Predictions PM1/PM2 stated before the run.
## Result (RUN-T7C-MULT-SESSION-19.txt)
Dy dev +8.6 → −6.1 % (stab_n −0.071, stab_i −0.030) · Er −15.1 → +1.9 % · Tm −9.8 → +2.0 % · Yb 0.0 → 0.0 % (correction identically zero).
PM1 HOLDS 4/4 (sign). PM2 HOLDS (Er, Tm < 5 %; Dy 0.017 Ha over). F4/F2 = 0.62, F6/F2 = 0.45 on all four — the Racah ratios, from the derived orbital.
## Reading (after the run, flagged)
1. The scatter was never in the kernel: it is the coordinate the observable is read at (level) versus the coordinate the object computes (average).
   R 1665's question is answered YES. Residual after correction ≤ 0.017 Ha (Dy), the others ≤ 0.006 Ha.
2. Two candidates for the Dy 0.017 remain, both derivable, neither opened: (3b) the spin-orbit level term (lowest J vs term centre); F^k from a local
   orbital run ~25 % above empirical, so stab may be over-scaled uniformly (would shrink all three, not just Dy). Owner: M ruling.
3. Structural degeneracy of f³ ⁴F/⁴S found by the CI under all F^k tested; property of the operator, not verified against Nielson–Koster (no network).
## Files: t7c_mult.py t7c_mult.jsonl RUN-T7C-MULT-SESSION-19.txt FINDING-T7C-MULT-SESSION-19.md