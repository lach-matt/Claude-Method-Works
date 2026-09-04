# PREDICTION — item (2)(i): eps0^a(zeta) from the RPA ring integral built in-project, s23. Written BEFORE the run.
Source of integrand: Benites, Rosado & Manousakis, arXiv:2411.18371 (2024) Eqs. 12-14 (ring sum, imaginary-frequency Lindhard, spin-resolved
k_F,sigma = k_F (1+sigma zeta)^{1/3}); c_L(zeta) their Eq. 16 (= Wang-Perdew 1991 Lambda_0). Comparison targets (recalled, not entered):
their Table II c0(zeta) [Ry] at 16 zeta values; Loos-Gill/Hoffman endpoints eps0^a(0) = -0.0710995 Ha, eps0^a(1) = -0.0499167 Ha.
Object: ring_zeta.py -- eps_r(r_s,zeta) = gamma Int dkappa kappa^3 Int dx [ln(1+Pi) - Pi]; c0 extracted as eps_r - c_L ln r_s at r_s -> 0
(evaluated at r_s = 0.02, 0.01, 0.005; the residual r_s ln r_s term must shrink ~2x per halving).
PZ1  zeta = 0: c0 reproduces -0.0711 Ha within 5e-4 Ha; the r_s -> 0 sequence is monotone and shrinks.
PZ2  zeta = 1: c0 reproduces -0.0499 Ha within 5e-4 Ha (Misawa scaling then holds by construction of the integrand).
PZ3  Intermediate zeta (0.4, 0.6, 0.8, 0.9): agrees with Table II c0(zeta)/2 [Ha] within 1 mRy = 5e-4 Ha.
PZ4  Non-monotone near zeta = 1: c0(0.99) > c0(1.00) (Hoffman minimum inside (0.99,1)) reproduced in-project.
PZ5  c_L(zeta) evaluated from Eq. 16 equals Wang-Perdew Lambda_0(zeta) as coded in s22 READ-GB-ZETA to 1e-6 at zeta = 0, 0.5, 1.
No constant chosen; the r_s sequence and grids are numerics and are stated.