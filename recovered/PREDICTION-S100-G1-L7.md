# PREDICTION S100 -- G1 LOCUS 7 (DERIVED exchange weight). Hashed BEFORE the run. Derivation (this session, from sealed source, no fitted number):
# solve_one: (-d2/dx2 + q) y = s, s = -2 M r^{3/2} X_vec, X_vec_i = sum_j S_ij P_a(j) r_j h, and P = r^{1/2} M^{1/2} y (t7c_kernel line 76).
# => y-space exchange kernel K_y[i,j] = 2 M_i r_i^{3/2} S_ij r_j^{3/2} sqrt(M_j) h. Symmetrising with Bi = (2 r^2 M)^{-1/2}:
# Bi K_y Bi = sqrt(M_i) * [r^{1/2} S r^{1/2} h] = sqrt(M_i) * X_tilde. The sealed kernel's exchange block carries a ROW-SIDE sqrt(M);
# the v5a-class dense build uses weight 1. Total M-power 1/2 -- consistent with the measured linear zero at alpha ~ 0.467.
## Rule B:
PR-L7 VALUE: dense build with exchange block sqrt(M_i)*X (general eig; sym twin qm*X*qm, qm = M^{1/4}) gives |dE| < 0.15 * 1.8351e-4 at npts=4000/7s. Direction: from + toward 0, not through to -2e-4.
PR-L8 DERIVED-SIZE: first-order integral <y|(sqrt(M)-1)_row X|y> on the baseline eigenvector reproduces the baseline dE to 30 percent.
CF-L7 lever: sqrt(M)->1 in the reweighted build reproduces baseline to 1e-9.