import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
rep = {
 "key": "1801.08358-eq10",
 "name": "Herrera 2018, eq. (10): the static field equation nu' = 2(m + 4 pi P_r r^3)/(r(r - 2m))",
 "source": {
  "located": "arXiv:1801.08358v2 [gr-qc], 7 Feb 2018, L. Herrera (Salamanca), 'New definition of complexity for self-gravitating fluid distributions: The spherically symmetric, static case'; journal ref Phys. Rev. D 97, 044010 (2018) as cited by Abbas & Nazar arXiv:1806.05042 ref [1]. Eq. (10) is on p.3, Sec. II.A.",
  "read_status": "READ",
  "via": "alphaXiv answer_pdf_queries(paper='1801.08358') returned pp.1-10 (the whole paper incl. references) as the PDF text layer; eqs (1)-(13), (19)-(22), (31)-(33) read there. Equation typography READ through the text layer only; eq. (12)'s garbled 'R^3_232' reading was confirmed by computing R^3_{232} = 1 - e^{-lambda} from metric (1) (rederive script, check A1 = 0)."
 },
 "published_statement": "p.3: 'Alternatively, using nu' = 2 (m + 4 pi P_r r^3)/(r (r - 2m)),  (10)  which follows from the field equations, we may write P_r' = -(m + 4 pi P_r r^3)/(r(r - 2m)) (mu + P_r) + 2(P_perp - P_r)/r,  (11)  where m is the mass function defined by: R^3_232 = 1 - e^{-lambda} = 2m/r, (12) or, equivalently as m = 4 pi INT_0^r r~^2 mu dr~. (13)'  Context: 'The metric (1) has to satisfy Einstein field equations G^nu_mu = 8 pi T^nu_mu, (2)'; eq. (7) 'P_r = -(1/8 pi)[1/r^2 - e^{-lambda}(1/r^2 + nu'/r)]' is the field equation (10) is solved from.",
 "published_hypotheses": [
  "Static: nu(r), lambda(r) functions of r only; fluid at rest, u^mu = (e^{-nu/2},0,0,0) (eqs 1, 14)",
  "Spherically symmetric, Schwarzschild-like (areal) coordinates, line element ds^2 = e^nu dt^2 - e^lambda dr^2 - r^2 dOmega^2, signature (+,-,-,-) (eq 1)",
  "Locally anisotropic fluid: T^0_0 = mu, T^1_1 = -P_r, T^2_2 = T^3_3 = -P_perp (eqs 3-5), physical meaning via Bondi's local Minkowski frame",
  "General relativity with NO cosmological constant: G^nu_mu = 8 pi T^nu_mu (eq 2); G = c = 1 (implicit in the 8 pi)",
  "m defined geometrically by e^{-lambda} = 1 - 2m/r (eq 12); eq (13) m = 4 pi INT mu is stated as 'equivalent', which presumes m(0) = 0 (regular centre) -- NOT used by eq (10)",
  "Implicit, never stated: r != 0 and r != 2m (division), and 1 - 2m/r > 0 so that lambda is real and metric (1) Lorentzian",
  "Distribution bounded by Sigma and matched to Schwarzschild (eqs 19-22) -- a global hypothesis of the paper, NOT used by the local eq (10)"
 ],
 "hypothesis_drift": [
  "CONVENTION CHANGE, verified equivalent (not a drift in content): tolman.py:1704-1708 (V9) and tolman.py:1400-1404 (dPhi_sourced) use signature (-,+,+,+), e^{2 Phi} = e^nu, T^r_r = +p_r and state Phi' = (m + 4 pi r^3 p_r)/(r(r-2m)); rederive B shows this is exactly nu'/2 of Herrera eq (10) (residual 0). The tree's own statement at tolman.py:94-95 quotes eq (10) in Herrera's nu form verbatim; the quote matches the source.",
  "ADDED by the tree: r - 2m > 0 encoded in EINSTEINg (tolman.py:2337-2339). The source leaves it implicit (division by r - 2m; e^{-lambda} = 1 - 2m/r > 0 for a real lambda). The addition is consistent with the source and NOT load-bearing for the uses: z3 re-encoding shows I7 is still unsat with r - 2m > 0 removed (rederive E).",
  "BROADER THAN NEEDED, in neither direction harmful: the tree's hypothesis list carries 'anisotropic fluid T = diag(-u,p_r,p_t,p_t)'. Rederive A shows eq (10) uses only G^1_1 = 8 pi T^1_1 and eq (12): mu, P_perp and m' never enter. So eq (10) holds for any static spherically symmetric source with T^r_r = p_r, fluid or not -- which is the class the tree also applies it to (Morris-Thorne throat, V18a, tolman.py:1782-1787).",
  "EXTENDED BEYOND THE SOURCE'S DOMAIN at one site, not a rests_on_it site: V18/V18a (tolman.py:1782-1792) evaluate the Phi' = 0 G^r_r relation at the Morris-Thorne throat, substituting m = r/2, i.e. AT r = 2m, where Herrera's chart is degenerate (e^{-lambda} = 0) and the divided form of eq (10) is undefined. The tree solves the undivided relation for p_r, which is the r -> 2m limit of the regular mixed component; the undivided form nu' r(r-2m) = 2(m + 4 pi P_r r^3) is an identity with no division (rederive C). A corollary the tree does not state: at r = 2m the undivided form gives 4 pi r^3 p_r = -m for ANY finite Phi', so at the throat itself the result does not depend on Phi' = 0. THEOREM X, I7/I8 and X1-X3 (the rests_on_it) all carry r - 2m > 0 and so stay inside the source's domain.",
  "CARRIED BY BOTH, NAMED BY NEITHER'S LEDGER: Lambda = 0. Source eq (2) is G = 8 pi T; the tree's canonical hypothesis is 'the Einstein equations' and V8/V9 are computed without Lambda; tolman.py's HYPOTHESIS LEDGER (tolman.py:204-219) does not name it. Rederive C/E show it is LOAD-BEARING for the tree's use: with MTW's G + Lambda g = 8 pi T and geometric m, Phi' = (m + 4 pi r^3 p_r - Lambda r^3/2)/(r(r-2m)), and Phi' = 0 plus the identity m = 4 pi r^3 p_r then solves to m = Lambda r^3/4, p_r = Lambda/(16 pi) -- NOT the vacuum. Not a drift (the tree does not drop it), but a limitation that is not yet a NAMED hypothesis in the owner file."
 ],
 "data_at_publication": [
  {
   "quantity": "unit convention G = c = 1 (the only 'datum' the canonical entry lists)",
   "value_then": "G = c = 1 (the 8 pi in eq (2))",
   "value_now": "G = c = 1 (a convention, not a measurement)",
   "source_now": "none needed: a unit choice has no current value",
   "moves_conclusion": "no -- eq (10) is a closed-form consequence of G^1_1 = 8 pi T^1_1 and contains no measured input; rederive D confirms it on the constant-density Schwarzschild interior at arbitrary M = 1, R = 3 (max rel. residual 3.1e-10, finite-difference limited)"
  },
  {
   "quantity": "cosmological constant Lambda (enters only if the Lambda = 0 hypothesis is relaxed)",
   "value_then": "0 by hypothesis (eq 2); a nonzero Lambda had been measured since 1998, so it was known to the author in 2018 and excluded by choice of field equation",
   "value_now": "0 by hypothesis in both source and tree; the measured value was NOT read in this audit, so its size is not quoted",
   "source_now": "not read (no measurement paper opened); the structural consequence was computed instead",
   "moves_conclusion": "structurally yes, numerically not assessed here: with Lambda != 0 the Phi' = 0 branch plus the identity gives m = Lambda r^3/4 != 0 (rederive E), so THEOREM X's I7/I8 emptiness is a Lambda = 0 statement. Whether the magnitude matters at any warp-board scale needs a READ value of Lambda and is left OPEN."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/1801.08358-eq10.py",
  "outcome": "0 checks not as expected (output saved beside the script as 1801.08358-eq10.out). A: from scratch in the source's conventions (Christoffel -> Ricci -> mixed Einstein for metric (1)): eq (12) R^3_232 = 1 - e^{-lambda}; eqs (6),(7),(8) as printed; eq (10) nu' solved from computed G^1_1 = -8 pi P_r with e^{-lambda} = 1 - 2m/r, residual 0; eq (10) free of mu, P_perp, m'; eq (13) m' = 4 pi r^2 mu from G^0_0; eq (9) from T^mu_{1;mu} = 0; eq (11) = (9)+(10); eq (33)->(32) via (10). B: tree conventions (-,+,+,+), Phi' = (m + 4 pi r^3 p_r)/(r(r-2m)) = nu'/2, residual 0 (independently reproduces tolman.py V9). C: Lambda probe -- eq (10) acquires -Lambda r^3/2 in the bracket (geometric m), equivalently the textbook (m_M + 4 pi r^3 p_r - Lambda r^3/3)/(r(r - 2m_M - Lambda r^3/3)) with matter mass; the undivided form is division-free. D: numeric witness, constant-density Schwarzschild interior (M=1, R=3), eq (10) vs finite-difference nu' at 6 radii, max rel. residual 3.10e-10; boundary eqs (20),(22) hold to 1.7e-16. E: the tree's use -- sympy {Phi'=0 under (10), m = 4 pi r^3 p_r} -> {m:0, p:0}; z3 independent re-encoding: I7 unsat, I8 unsat, I7 still unsat with r - 2m > 0 removed, vacuity guards sat; with Lambda the same system solves to m = Lambda r^3/4. Also run, read-only: python3 tolman.py --prove -> I2s sat, I7/I8 unsat (hyp sat), X0 sat, X1-X3 unsat, 0 obligations not as expected; no file under research/ modified.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "G. Abbas & H. Nazar, arXiv:1806.05042 (2018), 'Complexity Factor For Static Anisotropic Self-Gravitating Source in f(R) Gravity'",
   "effect": "extends",
   "what": "Eq. (15) gives the f(R) analogue nu' = 2(m + 4 pi P_r r^3/F)/(r(r-2m)) - r^3/(r(r-2m)F){(f - RF)/2 + nu'F'/(2e^lambda) + 2F'/(r e^lambda)} and states it reduces to Herrera's eq (10) at f(R) = R (their conclusion list). Confirms eq (10) as the GR limit and shows it is field-equation-specific: a modified-gravity source term enters exactly where the tree's I7/I8 use it, so 'the Einstein equations' is load-bearing in the same way Lambda = 0 is.",
   "read_status": "READ (pp.1-16 via alphaXiv answer_pdf_queries)"
  },
  {
   "ref": "discover_papers hits on Herrera's complexity factor 2022-2026 (e.g. 2203.16704, 2410.03095, 2501.14282, 2505.17424, 2609.03393)",
   "effect": "confirms",
   "what": "Titles/abstracts only: follow-up work builds on Herrera 2018's Sec. II equations or generalises them to modified gravity; no hit reports an erratum or contradiction of eq (10). Not read beyond the discovery abstracts, so this is absence-of-contrary-signal, not a reading.",
   "read_status": "NAMED-NOT-READ (abstracts from discover_papers only)"
  },
  {
   "ref": "Tolman, Phys. Rev. 55, 364 (1939); Oppenheimer & Volkoff, Phys. Rev. 55, 374 (1939); Bowers & Liang, ApJ 188, 657 (1974) -- the isotropic/anisotropic TOV lineage eq (10) belongs to",
   "effect": "confirms",
   "what": "Herrera presents eq (10) as following from the field equations, not as new; it is the standard TOV potential equation. Named for attribution only; the audit's confirmation is the from-scratch re-derivation, not these papers.",
   "read_status": "NAMED-NOT-READ"
  }
 ],
 "lacked_data": "M's hypothesis tested for this result: eq (10) has NO measured input. It is an algebraic consequence of one component of G^mu_nu = 8 pi T^mu_nu for the static spherical metric plus the definition e^{-lambda} = 1 - 2m/r, re-derived here from scratch in both sign conventions with residual 0 and checked numerically on an exact interior solution. There is no datum the author could have lacked that would change it; newer data cannot move a closed-form identity. What CAN move the conclusion is theory, not data: (i) a nonzero cosmological constant (measured since 1998, so known in 2018 and excluded by the choice of eq (2)) adds -Lambda r^3/2 and makes THEOREM X's Phi' = 0 branch non-empty (m = Lambda r^3/4); (ii) modified gravity (f(R), 1806.05042 eq 15) adds curvature source terms. Neither is a flaw in Herrera's GR statement; both mean the tree's I7/I8/THEOREM X conclusions are statements about GR with Lambda = 0, which is what the tree says it uses. Evidence against M's hypothesis for this result: the from-scratch computation (rederive A, B, D). Evidence that would support it: none found; no erratum or contradiction surfaced in the later literature checked.",
 "grade": "STANDS",
 "grade_evidence": "Statement READ verbatim at arXiv:1801.08358v2 p.3 and matches the tree's quote (tolman.py:94-95, 2511-2513). Re-derived from scratch with sympy in Herrera's (+,-,-,-) conventions and in the tree's (-,+,+,+) conventions (residual 0 both), together with eqs (6)-(9), (11)-(13), (32)-(33); numeric witness on the constant-density Schwarzschild interior agrees to 3e-10. The tree's hypotheses match the source's: the added r - 2m > 0 is implicit in the source and shown not load-bearing; the fluid hypothesis is shown unnecessary (eq (10) needs only T^r_r). The tree's use (Phi' = 0 plus the identity forces m = p_r = 0; I7/I8) is independently re-checked by sympy and z3 with vacuity guards. No datum enters. Two notes that do not change the grade: Lambda = 0 is carried by both source and tree but not named in tolman.py's hypothesis ledger, and it is load-bearing for I7/I8 (computed); V18/V18a use the undivided relation at r = 2m, outside the source's chart, which is a valid limit and not a rests_on_it site.",
 "what_would_change_the_grade": "NARROWED if a rests_on_it site (THEOREM X, I7/I8, X1-X3, W4, D9, specthm:R2) were shown to apply eq (10) with Lambda != 0, in a modified-gravity setting, or at r <= 2m in the divided form; WRONG only on a computed counterexample to eq (10) under its own hypotheses (none exists: rederive A is an identity); OPEN would apply only if the source became unreadable. A misprint in a later version of the paper would be a discrepancy, not a refutation.",
 "reverify_command": "python3 " + D + "/rederive/1801.08358-eq10.py && (cd /home/user/Claude-Method-Works/research/warp-drive && python3 tolman.py --prove | grep -E 'I2s|I7|I8|X0|X1|X2|X3|obligation')",
 "report_path": D + "/audits/1801.08358-eq10.json"
}
json.dump(rep, open(rep["report_path"], "w"), indent=1)
print("ok", len(json.dumps(rep)))
