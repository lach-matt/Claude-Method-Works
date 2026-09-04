# FINDING-B (s34) — the eigenvalue seam is NOT missing orbital relaxation: the same-functional DSCF (Janak) is DEEPER than the TS eigenvalue on every
row, so it moves the E path FURTHER over T. Candidate REFUSED ON SIGN. PB-1/2/3 held; PB-4 stands as the reading. Nothing entered.
Run: janak_S.py (t7c_cuaudit_S.py = cuaudit + corr="S" hook of t7c_corrz, two hunks), 9 f-points per row, Sc Y La Gd Lu Cs, SIC_NOCLAMP=1 SUBCELL=1,
54 SCFs; gate: f=1/2 reproduces t7c_corrS.jsonl EF (Sc -0.32698 vs -0.327). TABLE-B-SESSION-34.txt.
DE_J^S - eps_S(1/2) [Ha]: Sc -0.0166 · Y -0.0109 · La -0.0095 · Gd -0.0104 · Lu -0.0099 · Cs -0.0030 (chain-Z record -0.0170/-0.0112/-0.0097/
-0.0106/-0.0101/-0.0022: S-Z <= 0.0004 on d rows, -0.0007 Cs). PB-1 HELD (sign, and within 0.0015 of record on all six). The curvature of eps(f)
is a property of the SIC one-orbital term + local exchange, invariant to the correlation form (as g_v <= 0.001 said from the other side).
PB-2 HELD: E path if carried at DSCF instead of TS: Sc -0.049 · Y -0.020 · La -0.017 · Gd -0.016 · Lu -0.019 · Cs -0.007 against T — further over.
PB-3 HELD: curvature ratio 3d/nd 1.5-1.7 vs seam ratio (E-O) 2.0-3.1 / (E resid) 3.6-6.2: not proportional.
NEW FACT (derived, comparison of like with like): the O path is a DSCF (frachf D_tot, HF exchange + S) and the E path was a TS eigenvalue; put both
at DSCF the exchange-treatment seam under ONE correlation S is O_DSCF - E_DSCF = Sc +0.045 · Y +0.025 · La +0.018 · Gd +0.015 (Gd seam applied) ·
Lu +0.023 · Cs +0.015 — local-exchange+PZ-SIC binds the removed entrant MORE than exact exchange by 0.015-0.025 on nd/6s and 0.045 on 3d, and T sits
inside that interval on every row but Sc (T below both on Sc, by 0.004 O and 0.049 E). This is the "bracketed from opposite sides" finding
stated on one correlation form and one observable, and it names the seam's home by elimination: the entrant EXCHANGE (LSD+PZ-SIC vs HF), not
the TS step, not relaxation, not correlation.
Reading (bound): the half-occupation TS approximation owns -0.010 (nd) / -0.017 (3d) / -0.003 (6s) of the E path in the shallow direction —
i.e. TS HIDES part of the local-exchange over-binding; the E path's true functional residual is the DSCF column. RULING (6) applies: this closes
candidate B as a home; the object (exchange seam O_DSCF - E_DSCF, class-resolved) is now stated in one number per row and is the thing to close.
Timing flag F34.1: the chain-Z Janak table and s21 kappa were read before PB-1..3 were written (stated in the prediction). Failed predictions: none.
Owed to T4: R 1912 B refused on sign · R 1913 exchange seam at DSCF, one correlation form · R 1914 F34.1.
Files (pack34): PREDICTION-B · t7c_cuaudit_S.py · janak_S.py · janak_S.jsonl · table_B.py · TABLE-B-SESSION-34.txt · this finding.