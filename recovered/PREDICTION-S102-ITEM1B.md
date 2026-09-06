# PREDICTION S102 ITEM 1B -- ONE-SHELL SPLIT IN THE R2_parts GAUGE (row 58). Filed BEFORE arithmetic.
# Supersedes the falsified P3 frame (F102.1) with the commensurate object: d101's E_one per-shell chord.
# RULE B: VALUE-exact throughout.
# METHOD: F_k(P) := Efun of the hybrid (shell k's orbital replaced, all else h5), with I_k[P] computed on
#   the exact span basis {P_k^-, P_k^+, same-l occupied P_k'} via eigen-relation T-action (T P = eps P
#   - Vloc P + X per each orbital's own equation; potentials from pot()) -- no kinetic quadrature.
#   Chord vector D_k = P_k^+ - P_k^-, split D_k = D_rot + D_perp with D_rot = sum_{k' same-l occ, k'!=k}
#   <D_k, P_k'> P_k'. Symmetrized exact telescoping:
#     rot_k  = (1/2)[F(P^- + Dr) - F(P^-) + F(P^+) - F(P^+ - Dr)]/0.2
#     perp_k = (1/2)[F(P^+) - F(P^- + Dr) + F(P^+ - Dr) - F(P^-)]/0.2
#     rot_k + perp_k == [F(P^+) - F(P^-)]/0.2  ALGEBRAICALLY EXACT.
#
# P4 (reproduction; |[F(P^+)-F(P^-)]/0.2 - R2_parts[k]| <= 1e-8, 13/13): the T-table F reproduces
#   d101's stored per-shell chord. Direction: match. VALUE-exact. Validates the eigen-relation I.
#   CAN-FAIL: skew one I_cross entry by 1e-7 -> P4 must break at that shell (rc=4), else rc=5 vacuous.
# P5 (identity; |rot_k + perp_k - chord_k| <= 1e-12, 13/13): exact telescoping. VALUE-exact.
# P6 (localization): at the R3-anomalous shells {5s, 5p, 5d, 6s}: |rot_k| >= 0.5|R2p[k]| AND
#   sign(rot_k) = sign(R2p[k]) (4/4). At the core shells {1s,2s,2p,3s,3p,3d}: |rot_k| <= 0.2|R2p[k]|
#   (6/6, perp dominates). Direction: the occupied-rotation (overlap-Pulay) content is what the
#   (sqrt(M)-1)X projection missed, and it lives at the same-l valence pairs. VALUE-exact.
# DIAGNOSTIC (not scored): I_cross hermiticity asymmetry per pair; > 1e-8 flagged.
# SCORING: vs pack101/d101-58.json R2_parts. No sealed file touched.
