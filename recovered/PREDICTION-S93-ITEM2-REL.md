# PREDICTION S93 ITEM 2 -- DERIVE THE RELAXATION-ENERGY DIFFERENCES S-dN' AND P-dZ' BY NAMED RESPONDER. Hashed before any solve.
## Objects (item 1): Rel(Z,core) = D(c;Z,core) - eps_c[Z;core+c].  S-dN' = Rel(Z*,cfg1) - Rel(Z*,cfg2) = +0.005..+0.011 (5/5 > 0).
##   P-dZ' = Rel(Z*,cfg2) - Rel(Z*-1,cfg2), |.| <= 0.003, l-signed.  cfg1 = cfg2 + c (own shell partner) at all 5 rows.
## Instrument: frozen-orbital energy functional E[Q'; P] (same functional as hfc2.run2, I_a from the converged N+1 solve), so that
##   E_frozen(core) := E[core; P_{core+c}].  Koopmans: E(core+c) - E_frozen(core) = eps_c EXACTLY in this functional (ceff = Q-1 is linear),
##   so Rel = E_frozen(core) - E_SCF(core) >= 0 is the variational relaxation energy, nothing else.
##   Single-responder relaxation: Rel_b = E_frozen(core) - E[core; only shell b re-solved to self-consistency in the frozen field of the others].
## Derivation being tested: the responder set of core cfg1 is the responder set of cfg2 plus the own-shell partner c (at 91: one more 6d).
##   The partner occupies the region c vacates, so its response to the removal is the largest single response; the others' responses are
##   nearly the same in cfg1 and cfg2 (same orbitals, one more screening electron). Hence S-dN' ~ Rel_c(cfg1) [- Rel_c(cfg2) at 91] > 0.
##   P-dZ' is the Z-derivative of the same responder set at fixed core: no responder is added or removed, so it is second order (small);
##   its l-sign is not derived here (F93.2 stands); only its magnitude is.
## Rule B declarations:
R0 VALUE-exact (structural; can fail if the functional is wrong): |E(core+c) - E_frozen(core) - eps_c| < 1e-5 Ha on 15/15 (A,B,C);
   |E_frozen(core) - E_SCF(core) - Rel_item1| < 2e-5 on 15/15; Rel_true >= 0 on 15/15.
R1 VALUE, bound-direction UP (dominance): [Rel_c(Z*,cfg1) - Rel_c(Z*,cfg2)] / (S-dN') >= 0.5 on 5/5. (Rel_c(cfg2) = 0 where c is empty in cfg2.)
R2 VALUE: sum over non-c shells b of [Rel_b(Z*,cfg1) - Rel_b(Z*,cfg2)] has |.| <= 0.5 (S-dN') on 5/5 (the rest of the core is a common mode).
R3 VALUE: Rel_c(Z*,cfg1)/Rel(Z*,cfg1) >= 0.5 at the s rows (38,56) 2/2; at the d rows no value claim (outer s and the other d/f shells respond too): REPORT.
R4 VALUE: |P-dZ'| <= 0.3 (S-dN') on 5/5; the largest single responder (by Rel_b) at (Z*-1,cfg2) and at (Z*,cfg2) is the SAME shell on 5/5.
R5 HYGIENE: single-shell relaxation loops converge (dmax < 2e-6) on every responder; rung 0 on all SCF solves; Drep 5/5.
## Can-fails (outside the instrument): A lever-dead: single-shell loop returns frozen P unchanged (0 iterations) -> Rel_c = 0 -> R1 cannot
##   score -> rc=4 expected.  B control-validity: E_frozen perturbed by +1e-4 -> R0 Koopmans check fires -> rc=4 expected. CORR=False asserted.
## Mechanism if R1 fails: the partner is not the dominant responder; the lift is collective (outer s at d rows) and a different named
##   electron carries it -- then name it from the Rel_b table (that table is computed regardless) and file the failure.