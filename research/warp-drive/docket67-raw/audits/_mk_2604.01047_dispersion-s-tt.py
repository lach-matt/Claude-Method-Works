import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "2604.01047#dispersion-s-tt",
 "name": "GMMPS dispersion functions F_S (5.3), Q (4.30), F_TT (5.4) with b_0, b_1, b_2, a",
 "source": {
  "located": "arXiv:2604.01047v1 [math-ph], 1 Apr 2026 (Galanda, Meda, Murro, Pinamonti, Schmid): Prop. 3.3 eqs (3.9)-(3.11) p.27, (3.16) p.29, prototype (4.9) p.43-44, Q (4.30) p.57-58, Thm 4.16 p.58, sec. 5.1 eqs (5.1)-(5.3) pp.59-60, sec. 5.2 TT display and (5.4) p.60, 5.2 text p.62, 5.2.1 p.62",
  "read_status": "READ",
  "via": "GMMPS v1 text layer (header line 'arXiv:2604.01047v1 [math-ph] 1 Apr 2026') as dumped from alphaXiv get_paper_content(fullText) during DOCKET 64 and held at scratchpad/d64/L4/galanda.txt (222,842 bytes, md5 4bac4a9400afceac615c5aa3b9f83c6e) and galanda_raw.txt (line layout, md5 7ec7c254a7412734f1aec9d54e1fe966; used to resolve the stacked fractions in (5.1), (5.2), (3.11)). In THIS stage every live alphaXiv call (answer_pdf_queries, get_paper_content, discover_papers) returned 'quota exceeded' and arxiv.org / alphaxiv.org are refused by the egress proxy (403), so the text was not re-fetched; whether a v2 exists was NOT checkable here."
 },
 "published_statement": "(4.9) p.44: 'iota_M G~_ret(Box(Box - a_1)(Box - a_2) phi (x) rho-check) + sum_{j=0}^2 b_j Box^j phi = S'. (4.30) p.57: 'Q(w^2) L_F phi(s,p) = L_F S(s,p), w^2 = s^2 + p^2, where Q(w^2) = w^2 (w^2 + a_1)(w^2 + a_2) J(-w^2) + b_0 - b_1 w^2 + b_2 w^4 (4.30) with J(-w^2) = INT_{4m^2}^inf rho(M) 1/(w^2 + M) dM.' 5.1 p.59: 'a_1 = a_2 = a = 2m^2/(6 xi - 1) ... [(5.1)] 6(1/6 - xi)^2/4 iota_M G~_ret(Box(Box - 2m^2/(6xi-1))^2 h^S (x) rho-check) - alpha~^S_1 m^4 h^S - 1/2 (1/kappa - alpha~^S_2 m^2) Box h^S - alpha~^S_3 Box Box h^S = S^S ... assuming that alpha~^S_2 = 0 ... and considering the result of Proposition 3.1 and Theorem 3.6 to fix alpha~^S_1 = (64 pi)^-1, we have by comparing term by term (5.1) with (4.9) that the parameters in the S case become: a_1 = a_2 = a = 2m^2/(6xi - 1), b_0 = -alpha~^S_1 4m^4/(6(1/6 - xi)^2), b_1 = -(2/kappa) 1/(6(1/6 - xi)^2) (5.2) and b_2 is a free parameter which depends on the renormalisation constant alpha~^S_3. Recall that kappa = 8 pi G. ... F^S(gamma) = gamma(a - gamma)^2 J(gamma) - (b_0 + b_1 gamma + b_2 gamma^2). (5.3) Notice that this function equals Q(-w) given in (4.30) for xi = -w^2 and for the set of parameters studied in this section.' 5.2 p.60: 'a_1 = a_2 = a = 4m^2 ... -1/120 iota_M G~_ret(Box(Box - 4m^2)^2 h^TT (x) rho-check) - alpha~^TT_1 m^4 h^TT - 1/2(1/kappa - alpha~^TT_2 m^2) Box h^TT - alpha~^TT_4 Box Box h^TT = S^TT ... Assuming again that alpha~^TT_2 = 0 ... and setting alpha~^TT_1 = 0 following Theorem 3.6, we have that a = 4m^2, b_0 = 0, b_1 = 60/kappa, while b_2 is a free parameter proportional to alpha~^TT_4 ... F^TT(gamma) = gamma(a - gamma)^2 J(gamma) - gamma(b_1 + b_2 gamma). (5.4)'",
 "published_hypotheses": [
  "one real Klein-Gordon field, m > 0, coupling xi; S sector needs 2/(6xi - 1) < 4 'to fulfil the hypotheses of Proposition 4.5' (5.1)",
  "Minkowski background, Poincare vacuum, past-compact perturbations, de Donder gauge; S/TT decoupling of (3.16) (Prop. 2.5, 3.3)",
  "the nonlocal kernel K_0 of Prop. 3.3 (3.10)-(3.13) with S = (2/3)(m^2 + (1/2)(1-6xi)Box)^2, T = (1/60)(Box - 4m^2)^2 (3.11), rewritten by Cor. 4.4 as iota_M G~_ret(Box . (x) rho-check)",
  "S: alpha~^S_2 = 0 assumed ('no renormalisation of the Newton constant'); alpha~^S_1 fixed by Prop. 3.1 + Thm 3.6 (printed (64 pi)^-1 in 5.1, 1/(64 pi^2) in Thm 3.6 -- sibling entry); alpha~^S_3 free -> b_2 free",
  "TT: alpha~^TT_2 = 0 assumed; alpha~^TT_1 = 0 by Thm 3.6; alpha~^TT_4 free -> b_2 free",
  "a_1 = a_2 = a read off the operators S and T (3.11)",
  "Fourier-Laplace convention Box -> -w^2 with G_ret of (Box - M) proportional to 1/(-w^2 - M) (p.58, 'with our sign conventions')",
  "Prop. 4.12 (the route to the normal form (4.23) and Thm 4.14 existence) requires a_1, a_2 in (-inf, 4m^2) -- satisfied in S iff 2/(6xi-1) < 4; in TT a = 4m^2 sits on the excluded endpoint"
 ],
 "hypothesis_drift": [
  "NONE DROPPED in the formulas: linstab.py:573-576 (c = 6(1/6 - xi)^2, b0 = -alpha 4 m^4/c, b1 = -(2/kappa)/c, a = 2m^2/(6xi - 1)) is (5.2) verbatim; linstab.py:605 Q is (4.30) at a_1 = a_2 = a; linstab.py:607 and :761 F_S is (5.3); linstab.py:763-764 (a = 4, b_1 = 60/kappa, F = g(a-g)^2 J - g(b_1 + b_2 g)) is 5.2/(5.4) at m = 1 -- all text-matched and re-derived in the script (D1, R2).",
  "a_1 = a_2 = a (linstab.py:601): the source's own statement for both sectors (5.1, 5.2), derived here from (3.11) (R1). Not drift.",
  "m = 1 units, kappa = eps (linstab.py:636-646, 747-763): a unit choice, eps = kappa m^2 = (m/M_P)^2 with M_P^2 = 1/kappa (5.3); (5.2) at m = 1 reproduces linstab.py:646 exactly (D1). Not drift.",
  "alpha~^S_2 = alpha~^TT_2 = 0: CARRIED at linstab.py:140 and :311 (GMMPS_HYPOTHESES), not restated at the dispersion lines 570-608/747-778. Computed here that it is load-bearing for b_1 (with alpha~^S_2 != 0, b_1 = -(2/kappa - 2 alpha~^S_2 m^2)/(6(1/6-xi)^2), R2). Carried, so not drift.",
  "xi constraint 2/(6xi - 1) < 4: CARRIED at linstab.py:133, :305; the tree's xi = 0 and xi = 1/3 (linstab.py:970-976) give 2/(6xi-1) = -2 and 2, both < 4, and a = -2m^2, 2m^2 < 4m^2 (H). Satisfied.",
  "UNNAMED (source-level, not a tree drop): TT's a = 4m^2 lies on the boundary Prop. 4.12 excludes (a_i in (-inf, 4m^2)); GMMPS nonetheless cite Thm 4.14 for TT existence (5.2 p.62). The tree uses F_TT only to BRACKET a zero (linstab.py:747-778, b2_root_bracket), which needs no existence theorem, so no computed result of the tree rests on it; the sibling spectral-j audit (C9) shows Lemma 4.13's endpoint limit is finite at a = 4m^2. Recorded, not repaired.",
  "linstab.py:955 'F_S(-w^2) = -Q(w^2) identically ((5.3) vs (4.30))' states the CORRECT identity (R4) but does not record that GMMPS's own sentence under (5.3) says 'equals Q(-w) ... for xi = -w^2' (sign dropped; variable misnamed, colliding with the coupling xi). Printed discrepancy, immaterial to the zeros (the two differ by the factor -1 exactly, R4). Recorded, not an error of the tree.",
  "b_2's relation to alpha~^S_3 is left as 'free' by both GMMPS and the tree; computed here b_2^S = -4 alpha~^S_3/(6(1/6-xi)^2) (sign(b_2) = -sign(alpha~^S_3)) and b_2^TT = 120 alpha~^TT_4. The tree brackets both signs of b_2 (|b_2| <= 1e100; S at -1e100, TT at +1e100, S +1e100 as control), so the unstated map moves nothing it uses."
 ],
 "data_at_publication": [
  {
   "quantity": "none measured: F_S, Q, F_TT and (a, b_0, b_1, b_2) are theory-level definitions; the only numbers are exact rationals (6(1/6-xi)^2/4, 1/120, 60) re-derived here",
   "value_then": "as printed",
   "value_now": "as printed (re-derived from (3.11), (3.16), (4.9))",
   "source_now": "this audit's script R1-R3",
   "moves_conclusion": "no"
  },
  {
   "quantity": "kappa = 8 pi G (enters b_1 and, via eps = kappa m^2, the tree's evaluation point)",
   "value_then": "G not printed numerically in 5.1-5.2",
   "value_now": "CODATA 2018 G = 6.67430(15)e-11 (rel 2.2e-5), as used by the sibling sec5.3-mass audit",
   "source_now": "sibling audit 2604.01047_sec5.3-mass.json (CODATA 2018)",
   "moves_conclusion": "no -- b_1 ~ 1/kappa sets only the scale; the tree's brackets are sign tests with margins of many orders"
  },
  {
   "quantity": "alpha~^S_1 (sets b_0)",
   "value_then": "1/(64 pi^2) (Thm 3.6); printed (64 pi)^-1 in 5.1",
   "value_now": "theory input, no measurement; the discrepancy belongs to sibling entries thm3.6 / attribution-and-printed-discrepancies",
   "source_now": "2604.01047 v1 5.1 and Thm 3.6 (READ via the cached text layer)",
   "moves_conclusion": "no for this entry: (5.2) is linear in alpha~^S_1 and the tree carries it as a symbol (linstab.py:574) or at 1/(64 pi^2) (linstab.py:644)"
  },
  {
   "quantity": "alpha~^S_2 = alpha~^TT_2 = 0 (assumption)",
   "value_then": "0 assumed",
   "value_now": "0 assumed (no datum exists)",
   "source_now": "GMMPS 5.1, 5.2",
   "moves_conclusion": "would shift b_1 by +2 alpha~_2 m^2/(6(1/6-xi)^2) (S) or -60 alpha~^TT_2 m^2 (TT); negligible against 1/kappa for sub-Planckian m unless alpha~_2 ~ (M_P/m)^2 -- an assumption, named, not a moved datum"
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/2604.01047_dispersion-s-tt.py",
  "outcome": "ALL PASS (exit 0), 45 assertions, nothing imported from the tree. R1: from printed (3.11) S, T and (3.16), (1/4)S = [6(1/6-xi)^2/4](Box - 2m^2/(6xi-1))^2 and -(1/2)T = -(1/120)(Box - 4m^2)^2, i.e. (5.1) and the 5.2 TT display, including the stacked fraction 6(1/6-xi)^2/4. R2: dividing by those prefactors and comparing with (4.9) reproduces printed (5.2) b_0, b_1 exactly and TT b_0 = 0, b_1 = 60/kappa, a = 4m^2; computes the unprinted b_2^S = -4 alpha~^S_3/(6(1/6-xi)^2), b_2^TT = 120 alpha~^TT_4. R3: the retarded Green function of (Box - M) is -theta sin(omega t)/omega; its Laplace transform is 1/(-w^2 - M), and the symbol of (4.9) is exactly printed Q (4.30). R4: F_S(-w^2) = -Q(w^2) and F_TT(-w^2) = -Q(w^2)|_{b0=0} identically; (5.4) is (5.3) at b_0 = 0; GMMPS's sentence 'equals Q(-w) for xi = -w^2' is literally false but only by the factor -1 / variable name (zeros unaffected). D1: linstab.py lines 573-576, 605, 607, 646, 761, 763-764 carry exactly these expressions (text match at those line numbers, md5 of linstab.py cf62b3bc4e9535283111b21ffcd24d41, commit 30d2f46). N1 (J from the (4.5) integral, 40 digits): TT at m = 1, kappa = 1, b_2 = 1e3, 1e4, 1e6 has a negative zero at -b_1/b_2 x (1 - 2.8e-4) (the offset is 16 J(0)/b_1), shrinking with b_2 -- GMMPS 5.2's sentence confirmed; gamma = 0 always a zero. N2 scope note at the test point m = 1, kappa = 1, xi = 0, alpha~^S_1 = 1/(64 pi^2), grid gamma in [-1e6, -1e-6] (8 pts/decade), J included: b_2 = +100 one negative zero; b_2 = -100 TWO negative zeros (gamma_0 and ~ -b_1/b_2); b_2 = -1000 none (discriminant of b_0 + b_1 g + b_2 g^2 negative, -7.98).",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "Meda & Pinamonti, 'Linear stability of semiclassical theories of gravity', Ann. Henri Poincare 24 (2023) 1211 = arXiv:2201.10288 (GMMPS ref. [79])",
   "effect": "extends",
   "what": "EARLIER, not later: the source of the decay-at-large-time method GMMPS apply to Q ('can be analysed as in [79]', p.58). Named because the only web search available returned it; it does not address GMMPS's S/TT coefficients",
   "read_status": "NAMED-NOT-READ (title/venue from GMMPS's bibliography in the cached text; arXiv blocked, alphaXiv quota exceeded)"
  },
  {
   "ref": "discover_papers for later work on 2604.01047 (attempted)",
   "effect": "contested",
   "what": "NOT RUN: alphaXiv discover_papers returned 'quota exceeded'. A WebSearch (fallback) found no paper after 2604.01047 (Apr 2026) that re-derives, narrows or contradicts its dispersion functions; the sibling sec5.3-mass audit's discover_papers call (same docket) likewise found none. Absence of a found paper is not evidence of absence",
   "read_status": "NAMED-NOT-READ (search result titles only)"
  },
  {
   "ref": "gr-qc/0209075 (Anderson, Molina-Paris, Mottola, AMM)",
   "effect": "contested",
   "what": "AMM's k^2 = 0 subtraction leaves no k-independent term in the scalar sector (the b_0 = 0 case of (5.2)); this contests which VALUE of alpha~^S_1 enters b_0, not the form of F_S/Q/F_TT audited here. Adjudicated in sibling entries (gr-qc/0209075 renorm-4.4, thm3.6), not here",
   "read_status": "NOT re-read in this stage; sibling audit gr-qc_0209075_renorm-4.4.json"
  }
 ],
 "lacked_data": "M's hypothesis tested for this result. The dispersion functions are exact consequences of GMMPS's own (3.11), (3.16) and (4.9) under a stated Fourier-Laplace convention; no measured datum enters them, so no later datum can move them -- evidence: every coefficient re-derives from the printed operators (R1-R3), and the only numbers are exact rationals. What the authors did NOT have is not data but two free renormalisation constants (alpha~^S_3, alpha~^TT_4 -> b_2) with no principle or measurement fixing them, and alpha~^S_2 = alpha~^TT_2 = 0 as an assumption; these are named hypotheses, not missing measurements. Where the conclusions DRAWN from these functions are sensitive: (i) the zero count depends on the sign and size of b_2 -- computed here, at a test point, b_2 < 0 gives a second negative zero and, beyond the discriminant threshold b_2 < -b_1^2/(4|b_0|) (~ 8.6e120 in m = 1 units at GMMPS's eps, far outside the tree's |b_2| <= 1e100), no negative real zero at all, which is at variance with GMMPS 5.1's prose 'For sufficiently large -b_2, this is the only negative zero' and consistent with their Fig. 1 (b_2 > 0) and 5.2.1 ('alpha~^S_3 sufficiently large and negative', i.e. b_2 > 0 by R2) -- a sign discrepancy in the prose, recorded, not a refutation, and it belongs to the sibling sec5.1-5.3-mode entry; it SUPPORTS the tree's own withdrawn-'only if' scoping (linstab.py:171-186); (ii) whether alpha~^S_1 is 1/(64 pi^2) or 0 (GMMPS vs AMM) sets b_0 -- a renormalisation-condition dispute, not a data gap. Having more data would not change the functions audited here.",
 "grade": "STANDS",
 "grade_evidence": "As the tree uses it -- GMMPS's F_S (5.3), Q (4.30) and F_TT (5.4) with (5.2)'s b_0, b_1, a and 5.2's a = 4m^2, b_0 = 0, b_1 = 60/kappa, READ -- every formula matches the source text verbatim at linstab.py:573-576, 605, 607, 646, 761, 763-764 (text-matched at those lines), and every coefficient re-derives in sympy from GMMPS's own operators (3.11) and equation (3.16) by the term comparison with (4.9) that GMMPS describe; the (4.9) -> (4.30) symbol re-derives with the retarded Green function's sign checked; F_S(-w^2) = -Q(w^2) holds identically (the tree's stated identity, linstab.py:955). The tree's hypotheses a_1 = a_2 = a and m = 1, kappa = eps are the source's and a unit choice; alpha~_2 = 0 and the xi constraint are carried at linstab.py:133, 140, 305, 311, and the tree's xi = 0, 1/3 satisfy the constraint. No datum enters. Discrepancies RECORDED in the source, none repaired and none a refutation: (a) the sentence under (5.3) 'equals Q(-w) ... for xi = -w^2' (true relation -Q(w^2), gamma = -w^2); (b) 5.1's 'large -b_2' against 5.2.1/Fig. 1 and the computed zero count; (c) TT's a = 4m^2 on Prop. 4.12's excluded endpoint while Thm 4.14 is cited -- none enters a computed result of the tree, which brackets zeros only. The live source could not be re-fetched in this stage (quota/egress); the READ rests on the verbatim v1 text layer cached in DOCKET 64.",
 "what_would_change_the_grade": "WRONG only if a v2 of 2604.01047 changed (3.11), (3.16), (4.9)/(4.30) or (5.2)/(5.4) so that the tree's lines no longer match (the tree would then be quoting a superseded version) -- a v2 could not be checked here. NARROWED if the tree began using F_TT for an existence or growth statement at a = 4m^2 (Prop. 4.12's endpoint, hypothesis (c)) or used F_S's zero count for b_2 beyond -b_1^2/(4|b_0|) without naming it. OPEN if the cached text layer were shown to differ from the arXiv v1 PDF at any of the quoted equations (re-read with answer_pdf_queries once the alphaXiv quota resets).",
 "reverify_command": "python3 " + D + "/rederive/2604.01047_dispersion-s-tt.py && cd /home/user/Claude-Method-Works/research/warp-drive && python3 linstab.py --selftest 2>&1 | grep -n 'F_S(-w^2) = -Q\\|b_2 = \\|BRANCH ROOT'",
 "report_path": D + "/audits/2604.01047_dispersion-s-tt.json"
}
json.dump(R, open(R["report_path"], "w"), indent=1)
print("ok")
