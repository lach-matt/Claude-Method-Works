# FINDING — item (2)(i): eps0^a(zeta) DERIVED in-project from the RPA ring integral, s23. Object ring_zeta.py (Benites-Rosado-Manousakis 2024
Eqs 12-14 integrand; c_L Eq. 16 = Wang-Perdew Lambda_0). Numerics stated: log grids kappa 1e-4..60 (1400), x 1e-4..1e3 (1400), trapezoid;
c0 read as eps_r - c_L ln r_s at r_s = 0.02/0.01/0.005 (residual r_s ln r_s term halves per halving, as predicted).
zeta   c0(0.005) [Ha]  Table II [Ha]   | zeta 0: -0.07115 (-0.07115; LG/Hoffman -0.0710995) | 0.4: -0.06824 (-0.06825) | 0.6: -0.06436 (-0.06435)
0.8: -0.05828 (-0.05825) | 0.9: -0.05399 (-0.05395) | 0.99: -0.04915 (-0.04915) | 1.0: -0.04991 (-0.0499; LG/Hoffman -0.0499167).
Raw eps_r checks: (r_s=0.01, zeta=0) -0.42884 Ry vs Table VIII -429.0 mRy; (0.01, 1) -0.24305 vs -243.1.
PZ1 HELD (sequence -0.07141/-0.07124/-0.07115, monotone, halving). PZ2 HELD. PZ3 HELD (all within 5e-5 Ha, 10x inside threshold).
PZ4 HELD (Hoffman minimum inside (0.99,1): c0(0.99) = -0.04915 > c0(1) = -0.04991). PZ5 HELD (c_L(0) = 0.0621814 Ry = (1-ln2)/pi^2 Ha; c_L(1) = half).
STANDING: the ONLY undetermined piece of the high-density series named in s22 (eps0^a(zeta) between its endpoints) is now an in-project
integral with no fitted element, agreeing with two independent published evaluations (Hoffman 1992 via Loos-Gill; BRM 2024) at every tested zeta.
Hoffman 1992 remains unfetched and is no longer needed for the derivation; its priority is recorded. Attributions added: Benites, Rosado &
Manousakis, arXiv:2411.18371 (2024) -- integrand form, Table II/VIII comparison values. Gell-Mann & Brueckner 1957 owns the ring sum itself.
No constant, no measured input.