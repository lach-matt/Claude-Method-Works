# PREDICTION-B (s34) — bridge-33 §3(1)(B): the eigenvalue seam. Written BEFORE any run. Ruling (M, s34): "B first, then A".
Object: E path = local-exchange (Slater/Gaspar) + PZ-SIC + chain-S TS eigenvalue at f=1/2, over T on every row (Sc -0.032, Y -0.009, La -0.007,
Gd -0.005, Lu -0.009, Cs -0.0035; FINDING-SEAM s33). Candidate named in bridge-33: the TS eigenvalue's MISSING ORBITAL RELAXATION vs the
DSCF on the SAME functional, i.e. kappa_S = eps_S(1/2) - DE_J^S with DE_J^S = int_0^1 eps_S(f) df (Janak; identity vs Etot held untailed to
<= 0.0003 on 15 rows, s21 P2d; janak_gap_corr <= 0.0012 on the O path, s33). If the E-path over-delivery is "TS lacks relaxation" then the DSCF
on the same functional must be SHALLOWER than eps(1/2) by the seam: kappa_S < 0 in Ha (eps negative; DE_J less negative), of size 0.005-0.009 nd, ~0.03 Sc.
Record consulted before predicting (timing flag F34.1, stated): TABLE-JANAK-SESSION-24 (chain Z, same machinery): DE_J - eps(1/2) = Sc -0.0170 ·
Y -0.0112 · La -0.0097 · Gd -0.0106 · Lu -0.0101 · Cs -0.0022 — the Janak integral is DEEPER than the TS eigenvalue on chain Z; s21 untailed
local functional (no SIC): kappa = +0.006 Sc, +0.004 Y, +0.002-0.004 5d, -0.0001 Cs (same sign: DSCF deeper). Not on record: the same under S.
Run: t7c_cuaudit_S.py (= t7c_cuaudit.py verbatim + the corr="S" hook of t7c_corrz.py, nothing else) via janak_S.py, f in {0.001,0.02,0.05,0.1,
0.15,0.25,0.5,0.75,1.0}, FOCC=FENT=f, SIC_NOCLAMP=1 SUBCELL=1, mode=all, rows Sc Y La Gd Lu Cs; DE_J by trapezoid in f^(1/3) as janak_table.py.
Gate: the f=0.5 row must reproduce t7c_corrS.jsonl EF (Sc -0.327 · Y? · La? … whatever is banked there) to 1e-4.
PB-1: DE_J^S - eps_S(1/2) is NEGATIVE on all six rows (Janak deeper than TS), within 0.0015 of the chain-Z record: Sc -0.017 · Y -0.011 ·
      La -0.010 · Gd -0.011 · Lu -0.010 · Cs -0.002. Mechanism: the correlation form (Z->S) shifts eps(f) nearly uniformly in f (g_v <= 0.001 s33);
      the curvature of eps(f) is the SIC one-orbital term (f^(1/3) at small f) and the local-exchange f-dependence, both unchanged.
PB-2: consequence — the candidate is REFUSED ON SIGN: replacing TS by the same-functional DSCF moves the E path FURTHER over T (to -0.015..-0.020 nd,
      ~-0.049 Sc), not toward it. Missing relaxation is not the eigenvalue seam's home.
PB-3: class ratio 3d/nd of the curvature = 1.5-1.8, against the seam's 2.0-3.1 (Sc 0.028 vs nd 0.009-0.014): not proportional; the seam is not
      the curvature scaled.
PB-4 (structural, no run needed if PB-1 holds): the E-path over-delivery is a property of the FUNCTIONAL (local exchange + PZ-SIC on the entrant),
      as s21 read for the pre-SIC object; the seam E-O = local+SIC minus exact-exchange (O path) on the SAME correlation S is then the next object:
      it lives in the exchange treatment of the entrant, and the sign (SIC-LSD over-binds the compact entrant, Sc most) is the standing
      "bracketed from opposite sides" finding. If PB-1 FAILS (kappa_S sign flips or magnitude >= seam) then relaxation IS in play and the
      test is repeated at f-grid density 2x before reading.
Failure criteria: PB-1 fails if any row's sign is positive or |delta vs Z record| > 0.0015. PB-3 fails if ratio within 10 % of the seam ratio.
Nothing entered; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED (T comparison only). Files: this file · t7c_cuaudit_S.py · janak_S.py · janak_S.jsonl · TABLE-B.