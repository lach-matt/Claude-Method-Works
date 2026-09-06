# FINDING — T7C RELATIVISTIC EXCHANGE (candidate (a) of bridge-19 s6) — session 20, 2026-08-16
Object: MacDonald-Vosko 1979 factor Phi_V(beta) = -1/2 + (3/2) ln(beta+eta)/(beta eta) on the spin-polarised local Vx inside scf_pol_sr,
beta = (6 pi^2 rho_s)^(1/3)/c, c = 137.035999 only. Phi_V(0)=1 (unit check 0.999999 at 1e-3), Phi_V(1)=0.435. Max beta ~1 at the Lu nucleus.
Prediction PA1 (before run; 0.005 CHOSEN): |dE_5d| < 0.005, negative. PA2: Dy 4f gate row moves < 0.005.
Result (t7c_mv.jsonl):  La 5d d = -0.0008 (banked SR pol -0.2079 -> -0.2087)   Lu 5d d = -0.0008 (-0.1693 -> -0.1701)   Dy 4f d = -0.0060 (-0.2509 -> -0.2569)
PA1 HELD (sign and magnitude). PA2 FAILED (0.0060 > 0.005) — recorded as a fail; the compact 4f responds to the core exchange more than the 5d does.
Conclusion: (a) RULED OUT as a closure of the 5d edge: it removes 3 % of +0.026, uniformly La->Lu. Relativistic exchange is a core-density effect
and the edge is not at core density — consistent with (b2): the indirect term is carried by the 6s and 5s5p CONTRACTION, which MV barely alters.
Bound stated: relativistic exchange is worth <=0.001 Ha on 5d, ~0.006 on 4f, in this kernel. Faults: none. Gates: none moved.