# FINDING — T0(b) Scott / Englert–Schwinger K-shell correction (session 16, 2026-08-16)
Ruled by M: run as specified (PREDICTION-T0B-SESSION-13.md). Predictions PB1–PB6 stood unaltered before the run.
Nothing written to register/index/store. Bank restore-point-2_13 (R 1700) unchanged.

## Method (derivable, no constant)
rho_TFD taken from tfd.py's own equation, rho = Z/(4πb³)(√(φ/x)+β)³; integrates to N exactly (checked, all six ions).
rho_K = 2|ψ_1s(Z)|² = 2Z³/π e^{−2Zr}. r_s = inner crossing (selected by the densities): Z·r_s = 0.51–0.61, inside the
K-shell peak. TFD overcounts within r_s by δN = −0.10 … −0.12 e (the cusp overshoot Scott 1952 corrects).
"Same N" is not mechanised in the prediction, so both readings were run and the comparison decides:
 (u) unscaled — outer TFD untouched, N′ = N+δN, tail −(Z−N′)/r;
 (c) conserved — outer TFD scaled by (N−N_in,K)/(N−N_in,TFD) ≈ 1.006, fixed by the constraint.
V_T0b = V_base(tfd.potential) + [V_H+V_x](rho_new) − [V_H+V_x](rho_TFD). Machinery gate: the reconstruction regenerates
the RUN-12 TFD column to ≤1e−4 Ha (t0b_pot.py). Probe = eigen_fix on the RUN-12 pairs.

## Result (RUN-T0B-SESSION-16.txt; d = E(second)−E(first), Ha)
             meas     TFD      (u)      (c)
 Ca II       hold   +.0453   +.0218   +.0445   holds (both)
 Sr II      +.070   −.0022   −.0241   −.0039   AWAY (both)
 Ra II      +.055   −.0018   −.0152   −.0025   (c) unchanged (Δ .0007); (u) away
 Ce IV      −.227   +.1634   +.1221   +.1592   toward, sign still wrong (both)
 Pr V       −.524   +.0034   −.0510   −.0030   toward, sign flips correct (both); |d| ≪ .524
 Th IV       hold   −.0436   −.0851   −.0484   holds (both)
Direction agrees on every ion between (u) and (c). Magnitudes in (u) are dominated by the 0.11 e net-charge deficit
(all levels deepen ~.03–.06 Ha, inner d/f more); (c) isolates the shape effect, which is small (≤ .004 Ha except Ce IV .004,
Pr V .006). The pattern is the λ=1 pattern of RUN-12: f-onset toward, d-onset away.

## Score
PB1 HOLDS (Ce IV, Pr V toward). PB2 HOLDS (Sr II away). PB3 HOLDS under (c) — under (u) Ra II moves away by .013, which is
the charge-deficit artefact, not the cusp; noted. PB4 HOLDS (Ca II, Th IV). PB5 HOLDS by construction (eigenvalue-only object;
no hole state built). PB6 HOLDS: no derived cusp correction closes all four — Sr II and Ra II move away, Ce IV keeps the wrong
sign, Pr V reaches the right sign at 1–10 % of the measured gap.  6/6 held. No timing flag: nothing was formulated after the run.

## Reading (stated, not decided)
Per the prediction file's own clause: T0's question is answered jointly by T0(a) + T0(b) + T3b′. The one-electron potential —
gradient-corrected (a) or cusp-corrected (b) — moves f-onset and d-onset in opposite senses, and neither reaches measurement.
T3b′ located the residue at the observable (measured entrant binding flat, kernels deepening with occupancy). The next derived
candidate must act on the hole-state DIFFERENCE, not the eigenvalue. Candidate owners to be named before any run:
Slater transition state (Slater 1972; Slater & Wood 1971) — half-occupation eigenvalue as the ΔE estimator; ΔSCF (Bagus 1965)
on the same TFD/HFS object; Janak 1978 (dE/dn_i = ε_i) as the theorem tying the two. RULING OWED from M before opening.

## Fault registered this session
F16.1 — MEAS sign in first t0b_run.py output carried the opposite convention to RUN-12; caught on reading, corrected before the
run file was sealed. Computed columns unaffected. Registered before the result was scored (fault-before-result convention).