import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "friedmann-equation-open-dust",
 "name": "Friedmann equations for k = -1 pressureless dust",
 "source": {
  "located": "Friedmann's open-space paper (Z. Phys. 21 (1924) 326, 'Ueber die Moeglichkeit einer Welt mit konstanter negativer Kruemmung des Raumes') has no arXiv copy. Read via exact restatement: K. Enqvist, 'Lemaitre-Tolman-Bondi model and accelerating expansion', arXiv 0709.2044 (2007): eq.(2.2) FRW limit X -> a/sqrt(1-kr^2), A -> a r; eq.(2.3) T^mu_nu = -rho_M delta^mu_0 delta^0_nu - rho_Lambda delta^mu_nu (dust + vacuum energy); eq.(2.11) Adot^2 + 2 A Addot + k(r) = 8 pi G rho_Lambda A^2 (the pressure equation, dust); eq.(2.12) first integral Adot^2/A^2 = F(r)/A^3 + (8 pi G/3) rho_Lambda - k(r)/A^2; eq.(2.13) F'/(A'A^2) = 8 pi G rho_M (layout of the extracted text; read as the standard LTB mass relation); eq.(2.15) H^2 = (8 pi G/3)(rho_M + rho_Lambda) - k/a^2; 'The FRW metric is the limit A -> a(t) r and k(r) -> k r^2' (p.4). Cross-read: Burwig & Easson arXiv 2510.13971v2 eq.(2) FRW with k in {0,+-1}, eq.(6) the k = -1 ANEC identity (independently re-derived here from rho + p = 2(-Hdot + k/a^2) in their 8 pi G = 1 units -- agrees).",
  "read_status": "READ-VIA-RESTATEMENT",
  "via": "alphaXiv answer_pdf_queries on 0709.2044v1 (pp.1-17, full), 2510.13971v2 (pp.1-6), 2511.07526v1 (pp.1-6), 1807.06209v4 (pp.1,13,16,40-42,71), 2503.14738v3 (pp.1,3-5,20-22,30). Friedmann 1922/1924 and Lemaitre 1927/1933: NAMED-NOT-READ (restated only). Owner file nonstatic.py re-read at HEAD b8b929b: lines 38-46, 85-107, 398-468, 640-666, 599-600."
 },
 "published_statement": "As restated in Enqvist 0709.2044 with the FRW limit A = a(t) r, k(r) = k r^2, F(r) = F0 r^3, G = c = 1: first integral adot^2 = F0/a + (8 pi/3) rho_Lambda a^2 - k (eq.2.12), with F0 = 8 pi rho_M a^3/3 (eq.2.13 in the FRW limit: 3F0/a^3 = 8 pi rho_M); pressure equation for dust adot^2 + 2 a addot + k = 8 pi rho_Lambda a^2 (eq.2.11). For k = -1, rho_Lambda = 0: adot^2 = C/a + 1 with C = F0 = 8 pi rho a^3/3, and addot = -C/(2a^2). This is exactly the tree's nonstatic.py:460-462.",
 "published_hypotheses": [
  "general relativity, G_mu_nu = 8 pi G T_mu_nu (Enqvist p.4, 'Plugging Eq. (2.1) into the Einstein equation')",
  "homogeneity and isotropy: the FRW metric as the limit A -> a r, k(r) -> k r^2 of LTB (Enqvist eq.2.2, p.4)",
  "comoving coordinates, t = proper time of the fluid, zero shift (Enqvist p.3: 'spatial coordinates to comove ... time coordinate to measure the proper time of the comoving fluid')",
  "source = pressureless dust plus (optionally) vacuum energy rho_Lambda (Enqvist eq.2.3); the tree's use sets rho_Lambda = 0",
  "F(r) non-negative (Enqvist p.5: 'F(r) is a non-negative function'), i.e. C >= 0; the strict witness needs C > 0",
  "k(r) < 1 (Enqvist p.4) -- satisfied by k(r) = -r^2",
  "a > 0: the relations hold on the solution's domain; the open-dust solution a = (C/2)(cosh eta - 1), t = (C/2)(sinh eta - eta) begins at a = 0, t = 0 with rho -> infinity (standard; checked here, C9), so the domain is t in (0, infinity)"
 ],
 "hypothesis_drift": [
  "NONE DROPPED from the Friedmann relations themselves: the tree's substitution (nonstatic.py:459-462) carries k = -1, dust, Lambda = 0 and C > 0, a > 0 (Symbol('C', positive=True), Function('a', positive=True)) -- each matches a source hypothesis, and C1-C3 re-derive the two relations from the Einstein tensor computed independently.",
  "LAMBDA = 0 -- load-bearing for the tree's IDENTITY, not for its SIGN (nonstatic.py:465-467, 664). With dust + Lambda the null contraction (adot^2 - 1 - a addot)/(4 pi a^2) is still exactly 3C/(8 pi a^3) = rho_matter (Lambda g_ab k^a k^b = 0), but the tree's rho = 3(adot^2 - 1)/(8 pi a^2), read off G_tt, becomes rho_m + Lambda/(8 pi), so the checked identity 'NEC - rho = 0' (nonstatic.py:663) would read -Lambda/(8 pi). C4 computes both. The tree states Lambda = 0 in the Friedmann comment (nonstatic.py:460 omits the Lambda term); recorded as a named hypothesis, not a drift.",
  "SCOPE WORDING 'for all time' (nonstatic.py:42 'the witnesses below hold it for all time with ... rho > 0 exactly'; nonstatic.py:92 'Two of them hold contraction for all time'; LEDGER.md:33 D10 'Witnesses hold it for all time'). nonstatic.py:92-101 names exactly two such witnesses, Minkowski in Milne slicing and open FRW k = -1, the latter with the dust NEC value. The open-dust spacetime exists for t in (0, infinity) and is past-singular: a -> 0, rho -> infinity, Ricci scalar 8 pi rho -> infinity as t -> 0+ (C9). 'For all time' is true of every t in the spacetime's domain; it is not 'for all t in R' and the spacetime is past-incomplete. Consistent with Burwig & Easson 2510.13971 Theorem (k = 0 or -1, non-static, bounded curvature, null-complete => I_ANEC < 0): open dust has rho + p = rho > 0 everywhere, so it must be null-incomplete, and it is. For open FRW with GENERAL a(t) (nonstatic.py:452) the tree does not claim NEC positivity; only for dust (open_dust_nec). Named qualifier: 'for all t > 0 of a past-singular solution'. Not a refutation of D10, whose claim is pointwise (at every event the witness has contraction, rho > 0, NEC strict).",
  "NULL DIRECTION -- the tree evaluates the radial outward contraction rho + p_r - 2j with k = e0 + e1 of the comoving frame (nonstatic.py:434). For a perfect fluid T_ab k^a k^b = (rho + p)(u.k)^2 for EVERY null k (C10), so 'SATISFIED, strictly' holds in every null direction and is independent of slicing. The tree's claim is therefore, if anything, stated more narrowly than it holds -- recorded so the widening is not over-read either: it is the NEC only, not the WEC/DEC/SEC (dust satisfies those too, but the tree neither claims nor needs them).",
  "SLICING -- the contraction variable W = cosh(chi) used alongside this result is a comoving-frame component; its slicing dependence is audited separately in audits/frw-open-contraction.json (C6 there). It does not touch the Friedmann relations or the NEC value audited here, both of which are scalars (C10)."
 ],
 "data_at_publication": [
  {
   "quantity": "numerical inputs to the conclusion 'T_ab k^a k^b = rho = 3C/(8 pi a^3) > 0'",
   "value_then": "none -- the result is an identity in the free parameters C > 0, a > 0 (canonical data_used = [])",
   "value_now": "none",
   "source_now": "n/a",
   "moves_conclusion": "no -- no datum enters; z3 C7 proves positivity for ALL reals a > 0, C > 0"
  },
  {
   "quantity": "spatial curvature Omega_K of the observed universe (context only; the tree uses open dust as an exact mathematical witness, not as a model of our universe)",
   "value_then": "Friedmann 1924: none measured (Hubble's expansion 1929 not yet published). Enqvist 2007 p.2: FRW fits then gave Omega_M ~ 1 (CMB), ~0.3 (galaxies), ~0 (SNe) absent Lambda.",
   "value_now": "Omega_K = 0.0007 +- 0.0019 (Planck 2018 TT,TE,EE+lowE+lensing+BAO, 1807.06209 eq.47b); 10^3 Omega_K = 2.3 +- 1.1 (DESI DR2 + CMB, LambdaCDM+Omega_K, 2503.14738 Table V)",
   "source_now": "arXiv 1807.06209v4 p.42 eq.(47b); arXiv 2503.14738v3 p.20 Table V",
   "moves_conclusion": "no -- the witness is a solution of the field equations for any C > 0 whatever the observed curvature; the observed universe is not claimed to be open dust"
  },
  {
   "quantity": "cosmological constant / dark energy fraction (context only)",
   "value_then": "Friedmann 1924 allowed Lambda; the tree sets Lambda = 0",
   "value_now": "Omega_Lambda = 0.6889 +- 0.0056 (Planck 2018 +lensing+BAO, Table 2); Omega_m = 0.3027 +- 0.0036 (DESI DR2+CMB, LambdaCDM); DESI DR2 prefers evolving dark energy at 2.8-4.2 sigma",
   "source_now": "arXiv 1807.06209v4 p.16 Table 2; arXiv 2503.14738v3 abstract, p.22 eq.(21)",
   "moves_conclusion": "no for the sign (C4: the null contraction equals rho_matter with or without Lambda); the tree's identity NEC = rho(G_tt) would acquire -Lambda/(8 pi) if Lambda were admitted, which the tree does not do"
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/friedmann-equation-open-dust.py",
  "outcome": "ALL CHECKS PASS (exit 0), 28 checks. C1: Einstein tensor of ds^2 = -dt^2 + a^2(dchi^2 + sinh^2 chi dOmega^2), computed with the script's own Christoffel/Ricci code, gives rho = 3(adot^2-1)/(8 pi a^2), p = -(2 a addot + adot^2 - 1)/(8 pi a^2), p_T = p_r, G_t chi = 0. C2: d/dt[a(adot^2-1)] = -8 pi a^2 adot p, so dust conserves C = a(adot^2-1) = 8 pi rho a^3/3, and p = 0 gives addot = -C/(2a^2) -- the tree's two substituted relations derived, not assumed. C3: rho + p = (adot^2 - 1 - a addot)/(4 pi a^2) (the tree's nonstatic.py:100 formula); for dust NEC = rho = 3C/(8 pi a^3). C4: with Lambda, NEC = 3C/(8 pi a^3) still, but NEC - rho(G_tt) = -Lambda/(8 pi). C5: parametric a = (C/2)(cosh eta - 1), t = (C/2)(sinh eta - eta) satisfies both relations exactly. C6: RK4 integration of adot = sqrt(C/a+1) matches the parametric a(eta=3) = 4.533830997889 to < 1e-10; NEC = rho = 1.280812073437e-03 there. C7 (z3 5.1.0, reals): for all a > 0, C > 0 the NEC numerator > 0 and = 3C/(2a) (negations unsat); C <= 0 admits a non-positive numerator (sat) -- C > 0 is load-bearing. C9: t, a -> 0 and rho, R = 8 pi rho -> infinity as eta -> 0+; adot = sinh eta/(cosh eta - 1) > 0 (no recollapse). C10: for a perfect fluid T_ab k^a k^b = (rho + p)(u.k)^2 for every null k. C8: the tree's own open_dust_nec() (imported read-only) returns rho = NEC = 3C/(8 pi a^3), NEC - rho = 0.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "N. L. Burwig & D. A. Easson, 'Open case for a closed universe', arXiv 2510.13971v2 (2025/2026)",
   "effect": "confirms",
   "what": "Theorem: non-static k = 0 or k = -1 FRW with a in C^2, a > 0, bounded curvature invariants, null-complete => I_ANEC < 0. Their eq.(6) k = -1 identity re-derived here from rho + p = 2(-Hdot + k/a^2) (8 pi G = 1) -- agrees with the tree's rho + p formula. Open dust (rho + p = rho > 0) is therefore necessarily null-incomplete, which C9 confirms directly (big-bang singularity). It does not contradict the tree's pointwise NEC claim; it sharpens the scope of 'for all time' (nonstatic.py:42, 92).",
   "read_status": "READ (alphaXiv pp.1-6)"
  },
  {
   "ref": "R. R. Caldwell & E. V. Linder, 'Null Impact of the Null Energy Condition in Current Cosmology', arXiv 2511.07526v1 (2025)",
   "effect": "confirms",
   "what": "States the FLRW NEC as rho_tot + P_tot >= 0 from R_mu_nu k^mu k^nu >= 0, a condition on the total fluid, not on components -- the same contraction the tree evaluates (for dust, rho). Its data discussion (w_tot > -0.53 for DESI best fit) concerns the real universe, not the tree's witness.",
   "read_status": "READ (alphaXiv pp.1-6)"
  },
  {
   "ref": "Planck Collaboration, 'Planck 2018 results. VI', arXiv 1807.06209v4; DESI Collaboration, 'DESI DR2 Results II', arXiv 2503.14738v3",
   "effect": "extends",
   "what": "Current curvature and Lambda measurements (see data_at_publication). They establish that the observed universe is near-flat and Lambda-dominated, i.e. not open Lambda = 0 dust; they neither test nor bear on the mathematical witness.",
   "read_status": "READ (alphaXiv, pages listed in source.via)"
  }
 ],
 "lacked_data": "Friedmann (1924) had no measurement of the expansion (Hubble 1929), of the curvature (Omega_K now 0.0007 +- 0.0019, Planck 2018+BAO; 0.0023 +- 0.0011, DESI DR2+CMB) or of Lambda (Omega_Lambda ~ 0.69 now). None of these enters the result as the tree uses it: the Friedmann relations for k = -1 dust are consequences of the Einstein equations for the stated metric and matter, re-derived here symbolically (C1-C3) and machine-checked over all reals a > 0, C > 0 (C7). Evidence against M's hypothesis for THIS result: nothing measured has moved and no measurement could move an identity in free parameters. Evidence that later data matter at all: only for the physical reading -- the real universe is not Lambda = 0 open dust -- which the tree does not assert. The one limitation later work sharpens is not data but a theorem (Burwig-Easson 2025): open dust with positive NEC must be past-incomplete, which the tree's 'for all time' wording (nonstatic.py:42, 92; LEDGER D10) should carry as a named qualifier.",
 "grade": "STANDS",
 "grade_evidence": "The two relations adot^2 = C/a + 1 and addot = -C/(2a^2) with C = 8 pi rho a^3/3 are derived here from the Einstein tensor of the open FRW metric for p = 0, Lambda = 0 (C1-C2), agree with the restated source (Enqvist 0709.2044 eqs.2.11-2.13, 2.15 in the FRW limit) and with the tree's own open_dust_nec() (C8); the NEC contraction equals rho = 3C/(8 pi a^3) > 0 for all a > 0, C > 0 (C3, z3 C7). Every hypothesis the tree uses (k = -1, dust, Lambda = 0, C > 0, a > 0) is a source hypothesis; none dropped. No datum enters. Named qualifiers recorded, none of which narrows the result as used: (i) Lambda = 0 is needed for the identity NEC = rho(G_tt), not for NEC > 0 (C4); (ii) 'for all time' means t in (0, infinity) of a past-singular spacetime (C9; Burwig-Easson 2510.13971); (iii) the NEC holds for every null direction, not only radial (C10).",
 "what_would_change_the_grade": "NARROWED if a downstream owner (LEDGER D10, nonstatic.py:42/92) is read as asserting the open-dust witness on a complete or past-eternal spacetime -- C9 shows it is past-singular. WRONG only if the Einstein tensor computation C1 failed on an independent CAS, or the z3 negation in C7 became sat for some a > 0, C > 0; neither is expected. The tree's identity check (nonstatic.py:663) would fail, by -Lambda/(8 pi), if a cosmological constant were admitted without redefining rho as rho_matter (C4).",
 "reverify_command": "PYTHONDONTWRITEBYTECODE=1 python3 " + D + "/rederive/friedmann-equation-open-dust.py   # expect 'ALL CHECKS PASS', exit 0 (needs sympy, z3-solver)",
 "report_path": D + "/audits/friedmann-equation-open-dust.json"
}
json.dump(R, open(R["report_path"], "w"), indent=1)
print("ok")
