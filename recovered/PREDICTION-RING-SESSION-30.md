# PREDICTION — candidate C: the truncation of the high-density expansion IS the d-row object (and Cs's cut). Written BEFORE any run. s30.
# Form R: eps_c(r_s,zeta) = eps_r(r_s,zeta)/2 + E0B  [Ha], eps_r = the full RPA ring sum (ring_zeta.py, s23, BRM 2024 integrand, the same object the chain
# took eps0(zeta) from), E0B = Onsager second-order exchange constant already in the chain. Everything else unchanged: SIC structure, SUBCELL, sc path, c.
# No constant chosen. Numerics CHOSEN and stated: ring_zeta grids (nk=nx=1400), nan-mask of the cancellation cell (K~1e-4, X~1e3), r_s table (log, 1e-3..100)
# x zeta table (0..1), linear interpolation in ln r_s and zeta; small-r_s limit gate: table(1e-3) vs lam0 ln r_s + eps0 + E0B within 2e-4 Ha.
# Literature carried: Nozieres-Pines 1958 (GB valid r_s <~ 1); RPA overbinding ~0.035 Ry nearly flat in r_s; RPA+SOX constant ~90 % of CA at r_s 1-2.
PR0 gate: form R reproduces form Z (chain) at r_s = 1e-3 to 2e-4 Ha, and eps_c(R) < 0 at every r_s (no cut anywhere: F_out == 0 by construction).
PR1 delivered fraction (as cutfrac: -DEc_sc / required) under R: Y La Lu in [0.85, 1.05] (from 0.61-0.65); Sc > 1.00 (overshoot, in [1.03, 1.20], from 0.93);
    Cs in [0.6, 0.9] (from 0.16). Order of the CHANGE: Cs > Y ~ La ~ Lu > Sc.
PR2 the d-row excess as defined (missing/req - F_out)*req becomes |excess| < 0.004 on Y La Lu under R (from 0.007-0.010).
PR3 the ns-pair relaxation piece R and the SIC piece B change by < 30 % in magnitude between forms (the object was the total-density term A, not the SIC pieces).
PR4 Sc/Y contrast: (delivered_R - delivered_Z) on Sc < 0.6 x that on Y (Sc's entrant sits at higher density where the truncation still holds).
Rule: PR1 (Y La Lu window) and PR2 held -> the d-row object is the truncation; ONE object with Cs's cut. Sc overshoot held -> the ring's own overbinding is
the next object (known, ~0.035 Ry flat) and it is a form property, statable with attribution. PR1 failed on Y La Lu -> C refused; the class object stands.
Runs: ring_table.py (table + gate), then frachf_ring.py Z one row per call, order Y Sc La Lu Cs (Gd only if budget). Comparison decides. Thresholds CHOSEN.