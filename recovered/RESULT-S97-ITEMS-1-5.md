# RESULT S97 -- ITEM 1 (core-core term, row 89) and ITEM 5 (Dirac scope above 112). c the only number. No sealed row, gate, D1-D5 touched.
## ITEM 1 -- SEVERITY LINE: ESTIMATE for value; SIGN-EXACT for direction. Criterion 3 at row 89: "estimated to second order, all terms, with the near-degenerate s^2->d^2 block resummed exactly".
instrument pack97/cc97.py (reads only sealed pack96 jsons; can-fail --canfail poisons Delta -> resummation must equal PT: PASS rc 0). prediction pack97/PREDICTION-S97-CORECORE.md sha256 c7e6c34a (hashed before arithmetic).
PR1 HELD -- slot rule decided by an external can-fail: the core object's own 6p-7s pair (no 6d anywhere) is the reference; (1-f) returns ent/core = +9.4% (PASS); exclusion returns -50% (FAIL). The s95 exclusion rule is RETIRED for the differential; F96.3 CLOSED (the asymmetry is now measured, not argued).
PR2 HELD -- ent 7s^2 -> 6d^2 own-slot block: E_PT -0.04538, two-state exact -0.04169 (ratio 0.919 at Delta 0.47; 0.84-0.96 over Delta 0.2-1.0).
PR3 HELD, and sign-exact for ANY Delta > 0: resummation reduces |E_PT|, so dcc_resummed >= dcc_PT = +0.06616 (reproduces filed +0.066 independently). Core-core differential WIDENS the margin.
PR4 HELD -- dm2(89) total = +0.04121 (entrant pairs, filed) + 0.0699 (core-core, resummed) = +0.111 Ha = 3.4 x margin 0.03233. No flip.
Limitation (declared): Delta = 0.47 is the s96 filed gap, not re-read this session (sweep shows sign and +-0.004 Ha insensitivity). Rows 38/56/72/105 core-core: NOT resummed (same instrument applies; expected same sign since PR3 is structural).
RULING REQUEST: the core-core term is no longer a limitation; criterion 3 at row 89 is a complete second-order estimate. Rule A: no named residue from V5.
## ITEM 5 -- SEVERITY LINE: SCOPE decision, non-gating, above the Z=108 evidentiary boundary. First-order SO on the KH field (what Dirac adds beyond scalar), NOT a Dirac solve. prediction pack97/PREDICTION-S97-SO.md sha256 b67c7904.
instrument pack97/so97.py: xi_nl = (1/2c^2)<P|(1/(r M^2))dV/dr|P>, M Koelling-Harmon. Can-fail c=1e6 -> xi = 0.00000 (lever-dead) PASS. Each xi from one foreground solve (15-24 s, rung 0).
   Z  competition       margin   SO term (jj worst case)                       narrowing   verdict
  109 6d(5/2) vs 7p(1/2) 0.1705   xi(6d)=0.0322 up + xi(7p)<=0.037 down         <=0.069    HELD
  112 6d(5/2) vs 7p(1/2) 0.2642   xi(6d)=0.0458 + xi(7p)<=0.037                 <=0.083    HELD
  113 7p(1/2) vs 8s      0.0581   xi(7p)=0.0374 lowers the ENTRANT              widens     HELD (sign-exact)
  115-118 7p(3/2) vs 8s  0.117-0.210  xi(7p)/2 <= 0.066 (xi(7p,118)=0.1312)    <=0.066    HELD
  119 8s vs 7d(3/2)      0.0965   1.5 xi(7d)=0.0013                             0.0013     HELD (sign-exact direction NARROWS; negligible)
PS1 sign HELD, range FALSIFIED (F97.2: xi(7p,113)=0.037 below the predicted [0.05,0.12]; the 7p at 113 is shallow, eps -0.164). PS2 HELD (0.028 < 0.058). PS3 HELD. PS4 ordering HELD (xi(6p)=0.738 >> xi(7p)).
DECISION (math decides): no predicted row 109-120 has a worst-case first-order SO shift exceeding its margin; the 7p1/2-7p3/2 split reaches 0.20 Ha at Og but re-orders j-components within the 7p shell, never the n+l entrant. Dirac kernel: NON-GATING. Recommend: not built; Law B attribution sentence above 112 cites this scan. Declared limitation: first-order on scalar orbitals underestimates the 7p1/2 contraction; a factor 2 leaves every verdict unchanged (worst row 109: 2x0.069 = 0.138 < 0.1705).
## FAULTS S97
F97.1 SEVERITY instrument -- so97.py occupancy parser added q-1 electrons (first Z=113 run was 6d9 7p1); caught by reading the printed cfg, not the label; fixed, rerun, discarded result not used.
F97.2 SEVERITY prediction -- PS1 range falsified (above). Stands.
Carried: F93.6; F95.1-F95.6 (F95.4 residual open); F96.2; F96.4 declared. CLOSED this session: F96.3.