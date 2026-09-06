# PREDICTION — item (2), s26: is the residual under DE_J the functional's over-binding of the compact entrant? Ruling: run (a) and (b), comparison decides.
Written BEFORE the run. No constant, no measured input (Cs, Y meas RECALLED-NOT-ENTERED).
(a) CANDIDATE: exchange over-binding is a FUNCTIONAL property: replace, at first order and at the standing f=1/2 orbitals, the entrant's LSD exchange
    treatment  <n_ent| v_x^LSD[n_sigma] − v_x^LSD[f n_ent] >  by EXACT (Fock) exchange with every other same-spin occupied electron,
    <psi_ent|K_sigma^others|psi_ent> = −Σ_b q_b Σ_k (3j(l_a k l_b;000))^2 G^k(ent,b)  (spherical average; own m excluded: exact self-exchange
    cancels self-Hartree, which the chain's SIC already does). Coefficient 1, derived. Delta_x = exact − LSD; candidate residual = resid_J + Delta_x.
    Correlation (chain Z, with its SIC) left in place on both sides: exchange-only replacement.
(b) NULL: the residual is the object's bound; no in-chain derived term reduces it.
COMPARISON RULE (stated now): (a) beats (b) iff PA2 holds AND spread(max−min) of resid_J+Delta_x over the 14 non-Cs rows < spread of resid_J (0.081).
Otherwise (b) stands and item (2) closes as "the object's bound", with Delta_x on record as a measured (computed) size of the exchange part.
Gate GA0: G^0(ent,ent) == <n_ent|v_H[n_ent]> to 1e-5 (Y^k pipeline against the chain's Hartree).
PA1 Delta_x > 0 on all 15 rows (SIC-LSD binds the entrant deeper than exact exchange).
PA2 |resid_J + Delta_x| < |resid_J| on >= 12 of 14 non-Cs rows.
PA3 resid_J + Delta_x > 0 on >= 8 of the 10 3d/4f rows (exact exchange over-corrects: what is left is missing correlation of the entrant, not exchange).
PA4 Delta_x is larger for the compact classes: 3d/4f Delta_x >= 2 x (Y La Gd Lu 4d/5d Delta_x) on average.
Files: xfock.py, xfock.jsonl, TABLE-XFOCK-SESSION-26.txt.
