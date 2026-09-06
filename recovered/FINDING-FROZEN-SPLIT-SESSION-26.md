# FINDING — item (1), s26: is the frozen ratio 1.15 derivable? Files: frozen_split.py, frozen_split.jsonl (30 rows: 15 chain Z, 15 x-only),
frozen_resp.py, frozen_resp.jsonl (15, chain Z), frozen_split_table.py, TABLE-FROZEN-SPLIT-SESSION-26.txt, PREDICTION-FROZEN-SPLIT-SESSION-26.md
(P26.0–P26.9 written before each run); frozen_scan_corrnone.jsonl extended from 2 to 15 rows (frozen_scan3.py, unchanged). No constant, no measured input.
## Method. On the f=1/2 frozen reference every f-dependent term T of the potential has the exact frozen-orbital derivative <n_ent|v_T(f)>, hence an
exact MIDPOINT DEFECT M_T = int_0^1 <n_ent|v_T(f)>df − <n_ent|v_T(1/2)>. Hartree (total and SIC) are linear in f: M = 0 exactly. Remaining: M_xtot,
M_ctot, M_xsic (closed form 0.0583 E_x[n_ent]), M_csic. The scan's mask_fr differs from their sum only by the entrant orbital's own response: M_resp.
## Result 1 — the s25 attribution of the +0.15 was WRONG in name, right in size. M_xtot: |r| <= 0.011 on all 14 non-Cs rows (both chains). M_ctot:
|r| <= 0.013. So s25 PF8's "LSD total-density exchange curvature ~+0.07–0.09" is NOT exchange curvature — it is M_resp; and its "correlation
~+0.05–0.08" is almost purely the SIC-CORRELATION defect M_csic (r 0.050–0.080). Correction owed to the s25 record (FINDING-FROZEN-SCAN Result 4).
## Result 2 — the frozen mask is three derived pieces, none a chosen constant:
   mask_fr = 0.0583 E_x[n_ent]  (law, r = 1.000, P26.0 HELD to 1e-6)  +  M_csic (E_c^SIC midpoint defect of f n_ent; r 0.050–0.080, decreasing 4d/5d ->
   3d -> 4f; P26.3 HELD)  +  M_resp (entrant orbital's own second-order response to dV_f = V_fr(f) − V_fr(1/2); negative on all 30 rows, r 0.067–0.117;
   P26.1, P26.4 HELD: |M_resp/mask_fr| 0.06–0.10). x-only chain reproduces PF8's Sc 1.09 / Yb 1.07 (1.093/1.071, P26.2 HELD).
## Result 3 — M_resp is linear response, computed WITHOUT any f-scan: M_resp^(2) = int e2(f) df with e2 the finite-difference curvature of the eigenvalue
along dV_f (d = 0.1 and 0.05 agree to <1e-4 rel, P26.9 HELD). M_resp^(2)/M_resp = 1.07–1.15 (P26.7 FAILED narrowly: bound was 1.15, Dy 1.151, and
the whole class sits ABOVE 1 — third-order terms are +7..15% and one-signed, not noise). The SIC-x shape alone, M_x^(2) = −K chi_x with the derived
K = 3/5 − (3/2)2^(−1/3) + 2^(−2/3) = 0.03941, gives 0.88–1.14 of M_resp (P26.8 HELD): the response is the orbital polarising in its own PZ exchange
potential — the same object as the KIPZ/Koopmans screening alpha of ruling (c) (folded there in s25), here obtained by derivation, no alpha chosen.
   Remainder after law + M_csic + M_resp^(2): −0.028 .. +0.005 in law units on the 14 non-Cs rows.
## Result 4 — the "1.15" is NOT a constant to derive. It is 1 + r_csic + r_resp, both row-dependent and both derived; the s25 plateau (1.12–1.19) is
a near-cancellation of r_csic FALLING with compactness (0.08 -> 0.05) against r_resp varying (0.07–0.12). P26.5 FAILED (spread 0.026 <= 0.05 held,
but the CV-vs-rmean clause did not: r_csic scales with neither |E_x| nor 1/rmean, CV 0.135 vs 0.124 — it is log-like, as GB eps_c ~ ln r_s).
P26.6 FAILED on its premise: there is no monotone 3d Sc->Cu trend in r_total (1.173 -> 1.157, s25's "1.14–1.19" was a range not a trend); the
delta is carried by r_csic (−0.011) at least as much as r_resp (−0.009). Cs: r_xtot = −0.48 (6s diffuse: total-x nonlinearity of the same size
as the law, opposite sign) explains its 0.60; Cs stays the stated exception.
## Standing for item (2). Under DE_J the TS mask is now closed-form-derivable at the 3% level: eps(1/2) + 0.0583 E_x[n_ent] + M_csic[n_ent] + M_resp^(2)
[+ SO/Hund]. What remains of resid_J is the functional's over-binding of the compact entrant (s24 test C) — item (2)'s scope question, ruling needed.
Not a closure. Failed: P26.5 P26.6 P26.7 (reasons above). Held: P26.0 P26.1 P26.2 P26.3 P26.4 P26.8 P26.9. Cs, Y meas RECALLED-NOT-ENTERED unchanged.
No faults. Reference SCFs: Ti, Cu at maxit=100 (F25.1) as in s25; eps_half matched to 1e-5.
