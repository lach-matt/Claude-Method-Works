# SPEC — the third correlation form (candidate S): full RPA ring + SCREENED second-order exchange.  Written s31 for s32; nothing run.
## Object (all inputs derived; no constant)
eps_c^S(r_s,zeta) = eps_ring(r_s,zeta)/2 + eps_2x^scr(r_s,zeta)   [Ha]
 - eps_ring: the chain's own ring table (ring_table.json, BRM 2024 integrand, 41 r_s x 11 zeta) — unchanged.
 - eps_2x^scr: the second-order exchange diagram with ONE Coulomb line replaced by the coupling-constant-averaged statically screened line
   W(q) = v(q)/eps_L(q,0;lambda), eps_L the Lindhard static dielectric function of the SAME gas (the ring's own screening; Lindhard 1954), the average
   (1/1)∫_0^1 dlambda over the coupling constant as in the adiabatic connection (Gruneis-Kresse 2009 form; Ren et al 2013). No parameter enters: k_F, k_TF
   are functions of (r_s, zeta) alone. Spin: same-spin pairs only (the diagram); zeta enters through the two Fermi spheres and through eps_L(zeta).
 - Attribution: Onsager-Mittag-Stephen 1966 (bare constant, the kappa->0 limit); Ziesche 2006 (on-shell form); SOSEX: Gruneis-Kresse-Harl-Schimka 2009 /
   Ren-Rinke-Scheffler 2013; the reduction route (rescale frequency, factor denominators) 2603.23283 (2026, single-pole reference — NOT the physical screening).
## Gates (must fail if wrong)
 G-S1 kappa -> 0 (lambda-average off, bare v): reproduces E0B = 0.0241792 Ha to 1e-4 at zeta=0 AND zeta=1 (the ζ-independence of the bare diagram, FINDING-E0B).
 G-S2 r_s -> 0 (screening -> 0 in units of k_F): eps_c^S -> eps_c^R -> eps_c^Z (chain form) at r_s 1e-3 to 3e-5 Ha (gate 44 already fixes R = Z there).
 G-S3 the reduced integral agrees with a brute Monte-Carlo of the 9-D form to its statistical error at (r_s, zeta) = (2, 0) and (2, 1) — one point each, no scan.
## Predictions (write PREDICTION-SOSEX-SESSION-32.md BEFORE the first run; numbers below are the design's own expectation, entered there as PS-1..4)
 PS-1 eps_2x^scr(2,0)/E0B in [0.60, 0.80] (30 % reduction at r_s 2 needed to close R - bench +0.007);  PS-2 the reduction is monotone in r_s and larger at zeta=1
 than at zeta=0 at fixed r_s (a single Fermi sphere screens harder);  PS-3 form S against the RECALLED benchmark (comparison only): |S - bench| <= 0.003 Ha for
 r_s in [1,5] both spins — i.e. within the RPA+SOSEX literature accuracy;  PS-4 on the 15 chain rows (corr='S' hook, same interface as R): the nd>=4 rows deepen by
 0.004-0.006 relative to R and the 3d rows by <= 0.002, the 4f rows by <= 0.001 (rz_mech dR_loc as the bound) — the d-row object closes to <= 0.002; Sc goes to
 ~1.27 delivered and STAYS the anomaly (a 3d property, not a correlation-form property).
## Cost and order
 Build (reduced 3-4 dim quadrature) ~ one session's budget; batches; per-point cost must be measured before the 41 x 11 table is scheduled (a table of the SOX
 term at the ring grid; small-r_s below the table = E0B x reduction factor -> E0B). Then corr_sosex.py (E table + gradients as corr_ring), then t7c_corrz corr='S',
 15 rows both SUBCELL=1, COMPARE-RZS. Only after that: the walk test (SPEC-WALK) and the 4f/Yb item.