# PREDICTION-GDSEAM (s33) — the Gd 4f7(8S)5d 9D-vs-average exchange seam (FINDING-SEAM open item), written BEFORE the run.
Object: hfterm.py machinery (s27, PT0-gated) applied to Gd: neutral 4f7 5d1 6s2 Hund determinant (9D: all 4f up, 5d up) vs average of configuration; ion 4f7 6s2 (8S).
seam_Gd = D_term - D_avg = dE_term(ion) - dE_term(neu). Closed form (derived, no constant): the 4f-4f term energy cancels between neutral and ion up to orbital
relaxation, so seam_Gd ≈ +1/2 sum_k G^k(4f,5d) Q_k, Q_k = sum_m c^k(2 m_d; 3 m)^2 (k = 1,3,5): the average-of-configuration D_HF omits half the 8S-5d same-spin exchange.
  PG-1: seam_Gd in [+0.010, +0.025] Ha (Gd's O-path shortfall exceeds La's by ~0.016 in TABLE-SEAM); it moves Gd DEEPER (IE larger).
  PG-2: closed form and dE_term(ion) - dE_term(neu) agree to <= 0.001 (relaxation only). PG-3: applying it to Gd's O path leaves Gd within 0.004 of Y/La/Lu's residual, i.e.
  Gd joins the class row; if instead |resid| stays > 0.008 the Gd row carries a further term. Tool: gd_seam.py (imports hfterm). No timing flag.