# FINDING — T7c: scalar-relativistic kernel (session 17). Owner Koelling & Harmon 1977 (Desclaux 1973 for the indirect 4f destabilisation).
Bank 2_13 (R 1700) untouched; findings only. Scored against PREDICTION-T7-SESSION-16.md (not rewritten). Table: RUN-T7C-SESSION-17.txt.

## Build (t7c_kernel.py, t7c_pol.py, shoot_sr.c)
KH equation P'' = [l(l+1)/r² + 2M(V−E)]P + (M'/M)(P' − P/r), M = 1 + (E−V)/2c². With P = M^{1/2}F the derivative term drops
(F'' = QF, Q = l(l+1)/r² + 2M(V−E) − M'/(rM) − M''/(2M) + 3M'²/(4M²)); F rides the banked C Numerov shoot and the banked bisection.
Coulomb limit checked on paper and numerically: P ~ r^γ, γ = √(1−(Z/c)²). c = 137.035999 (CODATA); no constant, no fit.
Gates PASSED: (i) c=1e6 regenerates t5 hfs_ts (Sc −0.2752, Yb −0.528) and t6 ts_pol (Fe −0.378, Dy −0.4137) exactly, same iteration
counts; (ii) H 1s at c=137.036 → −0.5000064 (Dirac −0.5000067). Instrument audit Au: 6s −0.050, 5d +0.037, 4f +0.48 — the known pattern.

## Score
PC1  direction (4f shallower) HOLDS; growth Dy→Yb HOLDS (+0.166 → +0.193); magnitude .02–.08 FAILS (0.19 at Yb); "≤ half the offset"
     FAILS — shift/offset = Dy 1.19, Er 0.83, Tm 0.87, Yb 1.00: the SR shift IS the shell-constant offset. "Relativity alone does not
     close" FAILS on the polarised object: SR-pol 4f = Dy +8.6 %, Er −15.1 %, Tm −9.8 %, Yb 0.0 % of measurement (all inside the ~15 % band
     that 3d/5d hold). SR-TS is Z-flat across 4f (−0.328…−0.336; measured −0.256…−0.327): the nonrel deepening trend is gone.
PC2  FAILS both clauses: 5d moves SHALLOWER (+0.027/+0.033/+0.040 La/Gd/Lu — the known relativistic 5d destabilisation; the prediction's
     physics was wrong, the kernel is not) and on the spin-averaged object leaves the band (15.5/21/18 %); on the polarised object it sits
     at the band edge (12.9/13.2/15.1 % shallow, growing La→Lu) against 1.7/0.3/4.9 % non-relativistically. 5d is degraded, not broken.
PC3  HOLDS: 3d shifts Sc 0.007, Fe 0.012, Cu 0.008 Ha; 3d SR-pol within 3.6–7.5 %.
Pol-step prediction (stated in-session after the spin-averaged run, before the polarised run — timing per R 1449): additivity
     SR-pol = TS_pol + shift ± 0.02 HOLDS (≤ 0.003 Ha on all ten); "5d stays outside the band" FAILS narrowly (band edge).

## Reading
1. Comparison rule of PREDICTION-T7: T7c moves ALL FOUR 4f toward measurement, uniformly (+0.163…+0.192), 3d intact, 5d not broken but
   pushed to the band edge. By the rule as written, T7c is the direction. PB4's exact-exchange branch cannot fire (PC1 gave the whole
   offset, not < half); T7a/T7b remain owed under M's ruling "all three, comparison decides" and are still informative (T7a: SIC exclusion;
   T7b: whether exchange language changes the 5d edge).
2. The residue after T7c is no longer shell-constant: 4f {+8.6, −15.1, −9.8, 0.0} %, 5d {+12.9, +13.2, +15.1} % — a per-species scatter
   on 4f and a small shallow systematic on 5d growing La→Lu. This is a new state of the record: the offset T5/T6 named is owned by
   relativity (Desclaux 1973 indirect destabilisation), and what remains is ~0.02–0.04 Ha, of mixed sign on 4f.
3. Ra II / Lr / Th (R 1578-class relativistic residues of the corridor law) now have a derivable kernel to be re-probed with; NOT run —
   out of T7 scope, owed as a candidate step.
## Faults
F17.1 shoot.c fixes the start exponent at l+½; the SR regular exponent differs (γ). Caught by gate (ii) (−0.5000092 vs −0.5000067) BEFORE
      any species result was read; repaired by shoot_sr.c (start slope √q₀, → l+½ non-relativistically to 1e-5); gate (i) unaffected.
F17.2 eigen mesh rmin = 1e-5/Z lies inside the relativistic core (M−1 = 2.66 Z² there); residual 3e-7 Ha on H 1s after F17.1; hydrogenic
      Z=70 1s within 6e-7 relative of Dirac; SR core shift through the interpolated SCF potential accurate to ~1e-5 relative. Accepted as
      a stated precision limit (≪ 1e-3 Ha on any TS value), not repaired.
