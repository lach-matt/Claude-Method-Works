# FINDING-GDSEAM (s33) — the Gd 4f7(8S)5d exchange seam is +0.019 Ha; with it Gd joins the class row on the observable path. Nothing entered.
Run (gd_seam.py, hfterm machinery, PT0-gated; HFSR 'hf' c=C0): neutral 4f7 5d1 6s2 (open 4f7, 5d1), ion 4f7 6s2. D_avg = 0.19137 == frachf D_HF (gate).
dE_term(neu) = -0.50551, dE_term(ion) = -0.48642 -> seam = D_term - D_avg = +0.01908 Ha; D_term = 0.21046. PG-1 HELD (in [0.010,0.025], deepening).
Closed form on the neutral orbitals, +1/2 sum_k G^k(4f,5d) Q_k with G^1/G^3/G^5 = 0.04348/0.03446/0.02606 and Q_k = 7(2 k 3;000)^2 = 0.6/0.2667/0.303: 0.02159.
PG-2 FAILED (0.0025 > 0.001): the difference is the 4f-4f 8S term energy's orbital relaxation between neutral and ion (4f contracts in the ion), 12 % of the seam —
the closed form is the frozen-orbital limit, the run is the derived value. Both no-constant.
Applied to the O path (TABLE-SEAM, chain Z): Gd resid 0.0258 -> +0.0067, against Y +0.0127 · La +0.0099 · Lu +0.0118 (Z): Gd moves from +0.016 ABOVE the class
to 0.003-0.006 BELOW it; under R/S (ring gain ~0.008 as on the other rows) Gd's observable-path residual is ~ -0.001, on the class row with Sc -0.004 · La +0.002 ·
Lu +0.004 · Y +0.005. PG-3 HELD against La (0.003), marginal against Y/Lu (0.005-0.006). The seam does NOT apply to the E path: the spin-polarised local-exchange
TS eigenvalue already carries the same-spin 4f7-5d exchange (its Gd residual, -0.005, stays as read).
Consequence for FINDING-SEAM: the Gd open item is closed; the observable-path class row is Sc -0.004 · Gd ~-0.001 · La +0.002 · Lu +0.004 · Y +0.005 (Cs +0.008):
the "d-row object" is a spread of 0.009 across the class with Gd and Sc on the over side, not a flat +0.005 — the law statement should carry it as a spread with the
sign changing inside the class, as (a) already allowed. Files (pack33): PREDICTION-GDSEAM · gd_seam.py · gd_seam.json · this finding. Failed prediction: PG-2 (relaxation).
Owed to T4: R 1906 Gd exchange seam +0.019, closed form 0.0216, relaxation 12 % · R 1907 the class row is a spread of 0.009 with sign change (Sc, Gd over).