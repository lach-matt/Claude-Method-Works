# FINDING-CAND (s33) — (a) tested against candidates (i) (ii) (iii): all three refused; the comparison decides for (a). Nothing entered.
Ruling (M, s33): test (a) [local trunk closed at S; the d-row 0.005 a stated non-local residual] against the three candidate homes named in FINDING-DZETA.
Criteria fixed first (PREDICTION-CAND): a candidate beats (a) only if c1 it deepens Y/La/Gd/Lu by 0.002-0.007, c2 it does not deepen Sc by > 0.002 (Sc is OVER by
0.004 under R/S), c3 it is class-flat on the nd rows within 0.003. Tool cand_i.py, 15 rows on the corr='S' SCF densities; TABLE-CAND-SESSION-33.txt.
CORRECTION CARRIED (before re-use of the D-table): the chain SICs f*n_i, f = 1/2 on the entrant (t7c_corrz l.124), so the one-orbital line is (n_ent/2, zeta=1),
r_s(ent/2) ~ 6.3 on nd rows (anchored). A_half = -0.0008 on every nd row (A was -0.0009): |A_half - A| <= 0.0002 HELD; D_half = -0.0028 (lin) / -0.0015 (fx),
FINDING-DZETA unchanged in every clause. On Sc/Ti/Cr A_half is now anchored (r_s 4.5) and reads -0.0009/-0.0007/-0.0004; on Fe..Yb it stays a held-end bound.
CANDIDATE (i) inhomogeneity — REFUSED, and by sign: Delta_i = +0.014 (Y) +0.014 (La) +0.015 (Gd) +0.016 (Lu); 3d +0.012..+0.014; 4f +0.012; Cs +0.010.
  P-i-1 FAILED (sign and x3 magnitude): the gradient term SHALLOWS every row. Mechanism read from the table: on the total line the entrant window is the atom's
  valence tail, t^2 large, and H_tot cancels 38-55 % of |eps_S| there (0.017-0.032); on the one-orbital line H_ent cancels 70-80 % of the whole SIC line
  (0.007-0.021); the DIFFERENCE is +0.010..+0.016 and CLASS-FLAT — a uniform shift, not the object. P-i-2 FAILED narrowly (Sc 0.0139 vs Y 0.0144: t^2_ent grows
  with diffuseness, La 15 > Y 5.6 > 3d 2.3-3.8, and H saturates), P-i-3 FAILED (4f 0.012 < nd 0.015). Fails c1 (wrong sign) and c2 (Sc +0.014). Caveat stated:
  eps-level proxy through the cancellation law (validated to ~10 % in s32 for a form change); a potential-level GGA would differ in detail, not in sign at this size.
CANDIDATE (ii) the SIC one-orbital line's own defect — REFUSED by three bounds: |A_half| <= 0.0009 (bench-vs-S on that line, anchored, nd rows); M_csic = -0.0007
  (s26 midpoint defect, Y, chain Z); and its only non-UEG content is the inhomogeneity of n_ent/2, which is candidate (i)'s H_ent and carries the wrong sign.
  Fails c1 by >= 4x. (The whole line is -0.014 on nd rows; the object would need a 35 % defect of it that no bound admits.)
CANDIDATE (iii) "same object as the 5d 0.013 flat" — RESOLVED FROM RECORD, prediction held: the 0.013 (chain Z, FINDING-RING: Y/La/Lu/Cs, delivered 0.61 of
  required) and the 0.005 (chain R/S, delivered 0.85; resid_R Y +0.0054 Lu +0.0043 La +0.0019 Cs +0.0086) are the SAME row-set, one sign, the ring gain having taken
  0.008 of it. Not a separate home; it is the object's history. Note carried: FINDING-RING's parenthesised resid_Z is in the opposite sign convention (- = short).
DECISION (comparison decides): (a) stands — the local-correlation trunk is closed at S; the d-row object (Y/Lu ~0.005, La ~0.002, Cs ~0.009 short; Sc ~0.004
over) is not repaired by the trunk's zeta-dependence (D < 0), its inhomogeneity (Delta_i > 0, x3), or its SIC line (<= 0.001), and it is not a second object.
NEW BOUND (register-worthy): at the eps level a gradient (GGA-form) correction of the local trunk shifts EVERY class shallower by 0.010-0.016, uniformly —
so no inhomogeneity correction can be the class-resolved object either; the same fact bars it from the 5d/6s side. What remains for the object, stated as the
next candidates (not opened): the term/hole-state seam (the eigenvalue/observable object of R 1578), and the frachf-path convention itself (its D_HF, hfdscf).
Files (pack33): PREDICTION-CAND · cand_i.py · cand_i.jsonl · TABLE-CAND · this finding. Failed predictions s33 (this file): P-i-1, P-i-2, P-i-3 (all three
are the finding). Timing flags: none. Prior art: PBE 1996 (H form; gamma = (1-ln2)/pi^2), Ma-Brueckner 1968 (beta), Perdew-Zunger 1981.
Owed to T4: R 1898 D-table (FINDING-DZETA) · R 1899 candidate comparison, (a) stands · R 1900 the uniform GGA-shift bound · R 1901 A_half correction (f = 1/2 SIC line).