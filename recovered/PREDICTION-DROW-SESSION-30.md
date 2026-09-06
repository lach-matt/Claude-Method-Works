# PREDICTION — the d-row excess (SPEC-DROW-EXCESS-SESSION-30). Written BEFORE any run. s30, 2026-08-17.
# Object: excess = missing/req - F_out on the class rows: Y 0.31 · La 0.25 · Lu 0.27 · Sc 0.05 (of req) = ~0.0102 Y · 0.0071 La · 0.0085 Lu · 0.0014 Sc Ha.
# (from FINDING-CUTFRAC: required Y 0.0329 La 0.0282 Lu 0.0313 Sc 0.0280; F_out Y 0.076 La 0.096 Lu 0.112 Sc 0.020). Cs settled (B). Gd set aside (4f-adjacent).
# Rulings in force: SUBCELL=1; SIC_NOCLAMP=1; correlation = one function I on the sc path; adiabatic A closed. No scan, no constant, no new measured input.

## Route P (object property of the local form). Extend cutfrac.py -> drow_p.py: SCF at f=1 (neutral) and f=0 (ion) on the s28 sc path, then
##   DEc_sc = [A] + [B] + [R] with  A = Δ ∫ n_tot eps_c(n_tot) dr  (total-density GB term; by construction zero for r > r_cut),
##   B = -Δ Σ_shells q ∫ P² eps_c(P²/w,0) dr restricted to the ENTRANT shell (its PZ self-correlation), R = the same sum over the non-entrant shells (relaxation).
##   Also A_in = A restricted to r < r_cut(f=1) (== A) and A_out = 0 (the cut). C = the s29 F_out column, carried.
PP0 (gate): A + B + R reproduces frachf DEc_sc on every row to 1e-5 (same orbitals, same integrals). Failure = build error, not physics.
PP1 sign: B > 0 on ALL six rows (the entrant's own eps_c is negative over 73-88 % of its charge on d rows, F_self 0.12-0.27; the SIC subtraction
    over-counts correlation removal). Committed magnitudes: B on d rows in [0.003, 0.010] Ha; B(Cs) < 0.001 (F_self 0.997, entrant sits where eps_c >= 0).
PP2 shape: B does NOT track the excess. Committed: B(Sc) >= 0.7 * B(Y) (a compact 3d entrant has smaller r_s hence larger |eps_c|; the excess ratio
    Sc/Y is 0.14). So P1's condition ("comparable AND same shape") is predicted to FAIL on shape: the deficit is not the entrant self-correlation term.
    If instead B(Sc) < 0.4 * B(Y) AND B on Y La Lu within factor 2 of the excess, P1 HOLDS and the deficit is an object property — record either way.
PP3 relaxation: |R| < 0.003 on every row (core shells barely change along the path).
PP4 (P2 ratio): g = excess / Q_mid, Q_mid = entrant charge with r < r_cut AND r > r_peak((n-1)p). Committed: Q_mid in [0.6, 0.9] on all four rows,
    so g(Sc) < 0.4 * g(Y): the ratio is NOT a single number to 20 % -> P2 FAILS -> the deficit is not geometric -> Route N decides.
Prediction summary Route P: PP0 HELD, PP1 HELD, PP2 FAILS-as-explanation (recorded as HELD if B(Sc) >= 0.7 B(Y)), PP3 HELD, PP4 P2-ratio not constant.

## Route N (non-adiabatic entrant-core second order; the honest A). drow_n.py on the shooter (t7c_kernel eigen_sr / numerov_wf_sr):
##   N1 spectrum in the ion HFS-SR local potential: bound l=0..3, plus box continuum on the log mesh (banded eigenproblem, keep eps < +3 Ha; box = mesh end).
##   N2 E2 = - Σ_{i in closed core} Σ_{a,b} |<i e|1/r12|a b>|² / (eps_a+eps_b-eps_i-eps_e), k=1 dipole term only, direct only; e = HFS entrant orbital;
##      i over (n-1)s2p6 and inward; ns2 reported separately.
PN0 (gate, adiabatic limit): dropping (eps_b - eps_e) from the denominator and closing the b-sum reproduces s29 corepol E_A on Cs to within 10 %.
    (corepol.jsonl: Cs E_A_closed -0.02985 uncoupled; A_ns for Sc -0.13953). If it does not, the basis is incomplete -> report basis size, no physics read.
PN1 E2(closed core, non-adiabatic) on Y La Lu in [0.005, 0.015] Ha (attractive, magnitude), Sc <= 0.003, Cs in [0.008, 0.020] (one object with B, s29 PC3).
PN2 ratio E2(Sc)/E2(Y) < 0.3.
PN3 ordering: |E2| Sc < La ~ Lu ~ Y (within 40 % of each other on the three n>=4 rows).
PN4 non-adiabatic << adiabatic on d rows: |E2_nonadiabatic| / |E_A_adiabatic(corepol)| < 0.1 on Sc (adiabatic was 20-200x too large, s29 PC2).
PN5 ns2 (outer s pair) contribution on Y La Lu is NOT negligible: |E2(ns2)| >= 0.3 |E2(closed)|. Reported separately, not added.
Failure of PN1 with the mechanism named: if E2(Y La Lu) < 0.005 the exchange term or higher k is required (build next); if > 0.015 the box continuum
    is too dense/too high (state box, cut at eps < +3, no retune).

## Comparison rule (SPEC): P1/P2 hold -> "domain of the form"; N holds (PN1-PN3) -> "missing physics"; both -> the same 0.009 twice-named (as Cs);
##   neither -> new object, stated. Predicted outcome: P fails, N holds -> Route N names the object: entrant-core second-order correlation.
Thresholds above are CHOSEN (§H.6). Nothing else is. Runs: drow_p.py (six SCF pairs, ~1 min/row, batches <= 3), drow_n.py (batches <= 2, drow_n.jsonl).
