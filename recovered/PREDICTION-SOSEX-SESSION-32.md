# PREDICTION-SOSEX (s32) — filed BEFORE the first run of the build (R 1449). Object: SPEC-SOSEX-SESSION-32 (pack32).
Design of the reduction (stated here so timing flags can be assessed): the bare SOX integrand depends on (k1,k2) only through P = k1+k2, so
eps_2b = ∫ dq g_2b(q) with g_2b(q) built from the pair density rho_q(P) = |L_q ∩ (P - L_q)| (L_q the lens k<1, |k+q|>1; k_F units), and rho_q(P)
is a 2-D integral (z, rho) with the azimuthal measure analytic. g_2b(q) is r_s- and zeta-INDEPENDENT (k_F units); zeta enters only through the
per-spin scaling q = s q~ and weight s^3/2, and r_s/zeta only through the coupling-averaged static screening factor
S(Pi) = ∫_0^1 2 lam dlam /(1 + lam Pi) = 2[Pi - ln(1+Pi)]/Pi^2 applied on the q line. Hence the whole 41x11 table costs ONE g_2b(q~) tabulation.
PS-0a  G-S4 f-sum coefficient 4 al rs/(3 pi), zeta-independent (certified at open, FINDING-SUMRULES).   PS-0b  G-S5 2 al rs (x_up+x_dn)/pi (certified).
PS-G1  ∫ g_2b dq (screening off) = E0B = 0.0241792 Ha within 1e-4 Ha at zeta 0 and, through the s^3/2 bookkeeping, identically at zeta 1.
PS-G2  at r_s -> 0 (Pi -> 0 at every q~ except a shrinking window k_TF/k_F ~ sqrt(rs)): eps_2x^scr -> E0B; |eps_2x^scr(1e-3,z) - E0B| < 3e-5 Ha.
PS-G3  the reduced ∫ g_2b agrees with a brute Monte Carlo of the bare 9-D form within 2 sigma of the MC at one point (bare, k_F units); the screened
       value at (2,0) and (2,1) likewise (weight S applied to the same samples).
PS-1   eps_2x^scr(2,0)/E0B in [0.60, 0.80]  (s31's number).  Design note entered before the run: at r_s 2 the static Pi at q~ = 1 is ~1.2 so S ~ 0.57
       there; the outcome depends on where g_2b(q) is concentrated. If g_2b peaks at q~ >~ 1.5 the ratio lands in range; if at q~ <~ 1 it lands BELOW 0.60.
       PS-1 stands as written; the run decides.
PS-2   the reduction (1 - ratio) is monotone increasing in r_s and, at fixed r_s, LARGER at zeta = 1 than at zeta = 0.
PS-3   |S_form - RECALLED benchmark| <= 0.003 Ha for r_s in [1,5], both spins (comparison only; nothing entered).
PS-4   15 chain rows, corr='S': nd>=4 rows deepen 0.004-0.006 Ha vs R; 3d <= 0.002; 4f <= 0.001; Sc ~1.27 delivered and stays the anomaly.
Grid/threshold choices (CHOSEN, §H.6): q~ log grid 1e-3..40 (~120 pts); (P_par,P_perp) 96x96; (z,rho) 160x160; MC 4e6 samples/point.