# PREDICTION — T7c-CORR: Gell-Mann-Brueckner local correlation on the SR-pol-SIC chain, 5d rows (session 21). Ruled "Go" by M.
Attribution: Gell-Mann & Brueckner PR 106, 364 (1957) high-density limit eps_c = A ln r_s + B; A = (1-ln2)/pi^2 = 0.0311 Ha analytic,
B = -0.048 Ha (unpolarised) / A_P = 0.01555, B_P = -0.0269 (fully polarised), as quoted in Perdew-Zunger PRB 23, 5048 (1981) as EXACT
limits; Gombas 1949/1956 (local correlation in TFD); PZ-81 orbital SIC applied to correlation as to exchange. Constraint eps_c <= 0
(derived: correlation energy is non-positive; the high-density form is not valid where it turns positive, r_s > e^{-B/A}). Object:
t7c_sic.scf_sic_sr with v_c added per spin channel; v_c = eps_c - (r_s/3) d eps_c/d r_s = A ln r_s + B - A/3 (zero where eps_c >= 0);
orbital SIC subtracts v_c[n_i] for each orbital as PZ does. Bracket: unpolarised constants on total density (U) and fully polarised
constants on the channel density (P). No chosen constant. Measured 5d rows comparison only.
PX1  Gates: v_c off reproduces t7c_sic (La sr_all -0.2202); the correlation self-term of a one-orbital density is removed (H-like check:
     entrant-only SIC on H 1s leaves eps unchanged by v_c to 1e-4).
PX2  On the SR-pol-SIC-SO chain the correlation shift on the 5d entrant is DEEPENING, 0.008-0.020 Ha, and FLAT (spread <= 0.005) La/Gd/Lu,
     for both U and P; the residual +0.0138/+0.0141/+0.0112 lies INSIDE the U-P bracket on all three rows.
PX3  On Y 4d the same bracket contains its +0.013 (nonrel chain).
Reading rule: PX2 held -> the 5d edge closes on an attributed chain; write the residual once and hand the object-class question to
chapter 34. PX2 failed -> the GB form's reach (r_s <~ 1) is the stated limitation and the correlation term is bounded, not fitted.