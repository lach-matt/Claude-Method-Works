import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
S = D + "/rederive/modified-spherical-bessel-k_l.py"
R = D + "/audits/modified-spherical-bessel-k_l.json"
rep = {
 "key": "modified-spherical-bessel-k_l",
 "name": "Closed form of modified spherical Bessel functions of the second kind k_l(x) = e^{-x} sum_j (l+j)!/(j!(l-j)!) (2x)^{-j} / x",
 "kind": "theorem",
 "source": {
  "located": "Classical special-function identity. Standard references: DLMF 10.47.9 (k_n = sqrt(pi/(2z)) K_{n+1/2}) and 10.49.12 (k_n(z) = (pi/2) e^{-z} sum_{k=0}^{n} a_k(n+1/2) z^{-k-1}, a_k(n+1/2) = (n+k)!/(2^k k! (n-k)!)); Abramowitz & Stegun 10.2.15 -- not on arXiv, NAMED-NOT-READ. READ via exact restatement in arXiv:2207.00707v4 (D. R. Stoutemyer, 'Inverse spherical Bessel functions generalize Lambert W ...', 2022) Sec. 5 p.22-23: Table 6 rows n = 0..4, the recurrence (17), the Rayleigh-type formula k_n(x) = (-x)^n (1/x d/dx)^n e^{-x}/x, the asymptotic k_n ~ e^{-x}/x, and the explicit normalisation note 'the Digital Library of Mathematical Functions defines k_n(x) as pi/2 times these definitions' (MathWorld normalisation, adapted from Weisstein). The radial ODE and the exterior modified-multipole expansion (3D) READ in arXiv:2003.03370v1 (Hinzen, Di Napoli, Wortmann, Bluegel 2020) eq (14) (radial equation u'' + 2u'/r - (l(l+1)/r^2 + lambda^2) u = 0 with fundamental set i_l, k_l), eq (39) (Yukawa Green function = 4 pi lambda sum_L i_l(lambda r<) k_l(lambda r>) Y*_L Y_L) and eq (41) (exterior potential of a source localised in a sphere = sum_L coefficient * k_l(lambda r) Y_L).",
  "read_status": "READ-VIA-RESTATEMENT",
  "via": "alphaXiv answer_pdf_queries on 2207.00707 (pp.1,3,5-8,12-14,17-20,22-29) and 2003.03370 (pp.1-6,8-9). DLMF/A&S read only through Stoutemyer's restatement (which reproduces the coefficient table and names the DLMF pi/2 convention); the full-l closed form is additionally re-derived here from the ODE (C1). Owner re-read in the working tree: research/warp-drive/excite.py md5 a866f2f7745baca63aad910aeeb20a69 (last commit 524ccae), lines 66-83 (D15, H-a..H-e), 101, 708-743 (k_l_poly, multipole_residual, multipole_rate), 1075-1082 (TAIL_RATE_HYPOTHESES), 1201-1204, 1490-1497 (selftest rows), 1767-1776 (--verify V6)."
 },
 "published_statement": "Stoutemyer 2207.00707 p.22, Table 6 'Exact exponential expansions of spherical Bessel functions k_n(x)': n=0: (1/x) e^{-x}; n=1: (1/x^2 + 1/x) e^{-x}; n=2: (3/x^3 + 3/x^2 + 1/x) e^{-x}; n=3: (15/x^4 + 15/x^3 + 6/x^2 + 1/x) e^{-x}; n=4: (105/x^5 + 105/x^4 + 45/x^3 + 10/x^2 + 1/x) e^{-x}; 'Beware that the Digital Library of Mathematical Functions defines k_n(x) as pi/2 times these definitions.' p.23: 'k_n(x) ~ e^{-x}/x for large |x|, making k_n(x) -> 0 as x -> +infinity.' Hinzen et al. 2003.03370 p.4 eq (14): the radial part of (Delta - lambda^2)U = 0 is 'the modified spherical Bessel differential equation d^2u/dr^2 + (2/r) du/dr - (l(l+1)/r^2 + lambda^2) u = 0, and its fundamental set of solutions are for each l the two modified spherical Bessel functions i_l(lambda r) and k_l(lambda r)'; p.5 eq (41): outside a sphere containing the source, V = sum_L [4 pi lambda^{l+1}/(2l+1)!!] q_L k_l(lambda r) Y_L. DLMF 10.49.12 form (as restated/normalised by Stoutemyer): k_n(z) = (pi/2) e^{-z} sum_{k=0}^n (n+k)!/(2^k k!(n-k)!) z^{-k-1}.",
 "published_hypotheses": [
  "n (= l) a non-negative integer (the finite sum terminates only for half-integer Bessel order n + 1/2)",
  "z != 0 (pole of order n+1 at the origin)",
  "normalisation convention: MathWorld/Stoutemyer k_n = e^{-x} q_n(x); DLMF k_n = (pi/2) times that = sqrt(pi/(2z)) K_{n+1/2}(z)",
  "the ODE is the 3-dimensional radial modified Helmholtz equation (angular eigenvalue l(l+1) of the 2-sphere); k_l is the solution decaying at infinity",
  "multipole use (2003.03370): LINEAR equation (Delta - lambda^2)V = source, source compactly supported inside a sphere, expansion valid outside it; all l (a cutoff l_max is a numerical choice, not part of the identity)"
 ],
 "hypothesis_drift": [
  "NONE on the identity itself: the tree's p_l(y) = sum_j (l+j)!/(j!(l-j)!) (y/2)^j y (excite.py:710-712, 715-719) is exactly the MathWorld/Stoutemyer normalisation (Table 6 rows n=0..4 reproduced coefficient by coefficient, C4) and (2/pi) times DLMF 10.49.12 (C3, 40-digit agreement with K_{l+1/2}); the tree's words 'up to normalisation' (excite.py:712) are accurate.",
  "RESTRICTED, not dropped (excite.py:79, 1490-1492, 1767-1776): the tree seats l = 0..5 only; the source identity holds for every integer l >= 0. Re-derived here for general l symbolically (C1: coefficient recurrence a_k/a_{k-1} = (l(l+1) - k(k-1))/(2k) plus termination at k = l+1) and checked exactly for l <= 12 (C2). A non-spherical source's tail in general needs every l, so the tree's 'covered ... by the multipole witnesses k_l (l = 0..5)' (excite.py:78-79) is a claim about witnesses, and the l > 5 content the coverage needs is supplied by the source (and by C1), not by the tree's own check.",
  "UNNAMED in the tree (excite.py:77-79, 1082): H-e says the NONLINEAR proof is radial 'in any dimension d' and that non-spherical tails are 'covered ... by the multipole witnesses k_l'; k_l with eigenvalue l(l+1) is the d = 3 radial solution only. Shown here (C8a): the tree's k_l does NOT solve the d-dimensional radial equation f'' + (d-1) f'/x - l(l+d-2) f/x^2 - f = 0 for d = 2, 4, 5. The d-dimensional analogue x^{1-d/2} K_{l+d/2-1}(x) does solve it and its rate still -> 1 (C8b), and it is elementary only for odd d. So the non-spherical coverage as written carries an unnamed hypothesis d = 3; the conclusion (rate -> m) survives in other d by a different function, which the tree does not seat.",
  "ADDED by the tree and named (excite.py:78-79, 'where f is small ... LINEAR'): the use needs the tail to be governed by the linearisation of f'' + 2f'/x = (1/2) f(f+1)(f+2). The linear coefficient is exactly 1 = m^2 in x units (C7: (1/2)f(f+1)(f+2) = f + (3/2)f^2 + (1/2)f^3), so the linear operator is exactly the source's (Delta - 1). That the nonlinear remainder (O(f^2) ~ e^{-2x}) does not alter the non-spherical tail rate is NOT proved by the source (which is linear) nor by any row of the tree for l >= 1; the tree's nonlinear proof (i)-(iii) is radial. The tree names this as hypothesis 'linear tail (f small)', so it is a named limitation, not a silent drop.",
  "IMPLICIT (excite.py:78-79): summing infinitely many multipoles and carrying 'rate -> 1' through the sum needs an interchange of limit and series. Supplied here (C9): k_l(x) e^x x = 1 + (positive terms in 1/x), decreasing in x, so for x >= X > r_s the series is dominated termwise by its value at X and the per-l limit passes to the sum wherever the angular amplitude sum_lm c_lm Y_lm is nonzero. Neither the source restatement read nor the tree states this step; it is not a gap in the identity, only in the use."
 ],
 "data_at_publication": [
  {
   "quantity": "numerical inputs to the identity",
   "value_then": "none: a closed-form identity in the dimensionless x = m r with integer l",
   "value_now": "none",
   "source_now": "C1-C5 of the re-derivation script (exact rational/symbolic arithmetic)",
   "moves_conclusion": "no -- no datum enters"
  },
  {
   "quantity": "the scale m (Higgs mass m_h in D15's use, through x = m r)",
   "value_then": "enters only via the rescaling x = m r (excite.py: 'The Higgs mass enters only through (H-b)')",
   "value_now": "not consulted: the identity and the rate '-R'/R -> 1 in units of m' are independent of the numerical value of m",
   "source_now": "not needed (dimensionless statement)",
   "moves_conclusion": "no -- any m > 0 gives the same statement in units of m"
  },
  {
   "quantity": "tree's own datum: residual for l = 0..5; rate at x = 1e6",
   "value_then": "residual exactly [0]; |rate - 1| < 1e-5 (excite.py:1490-1497)",
   "value_now": "residual exactly 0 for l = 0..12 (C2); max |rate - 1| over l = 0..5 at x = 1e6 is 1.0000150e-6 (C5b), consistent with the expansion -R'/R = 1 + 1/x + l(l+1)/(2x^2) + O(x^-3) (C5a)",
   "source_now": "rederive/modified-spherical-bessel-k_l.py",
   "moves_conclusion": "no"
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": S,
  "outcome": "ALL PASS (14 rows). C1: for GENERAL l (symbolic), the single-term operator on e^{-x}x^{-n} gives 2(n-1)x^{-n-1} + (n(n-1)-l(l+1))x^{-n-2}, so the residual vanishes iff 2k a_k = (l(l+1) - k(k-1)) a_{k-1}; the tree's coefficients satisfy this identically (gammasimp) and the series closes at k = l+1 -- the identity is proved for every integer l >= 0, not just the tree's 0..5. C2: exact residual 0 for l = 0..12 by direct differentiation. C3: tree k_l equals (2/pi) sqrt(pi/(2x)) K_{l+1/2}(x) to rel. 2.3e-41 (mpmath, 40 digits, l <= 12, four x) and symbolically via sympy expand_func for l <= 5 -- i.e. tree = (2/pi) x DLMF k_l. C4: Stoutemyer Table 6 rows n = 0..4 reproduced exactly. C5: -R'/R = 1 + 1/x + l(l+1)/(2x^2) + O(x^-3), limit 1 for l = 0..12; tree's x = 1e6 datum max deviation 1.0000150e-6 < 1e-5. C6: control l^2 leaves a nonzero residual (l = 1..5). C7: linear coefficient of (1/2)f(f+1)(f+2) is exactly 1. C8: tree's k_l fails the radial equation for d = 2, 4, 5; x^{1-d/2}K_{l+d/2-1} solves it and its rate -> 1. C9: k_l(x) e^x x is 1 + positive powers of 1/x (monotone, dominated) for l <= 12.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "arXiv:2207.00707 (Stoutemyer 2022)",
   "effect": "confirms",
   "what": "Restates the finite exponential expansions of k_n (Table 6), the recurrence and Rayleigh formula, the large-x behaviour e^{-x}/x, and the pi/2 normalisation difference from DLMF; extends by constructing multi-branch inverses (generalising Lambert W). Nothing narrows or contradicts the identity.",
   "read_status": "READ (pp.1,3,5-8,12-14,17-20,22-29)"
  },
  {
   "ref": "arXiv:2003.03370 (Hinzen, Di Napoli, Wortmann, Bluegel 2020)",
   "effect": "confirms",
   "what": "Radial modified-Helmholtz equation (14) with fundamental set i_l, k_l; Yukawa Green function expansion (39); exterior modified-multipole expansion (41) for a source localised in a sphere -- the linear, 3D, all-l use that excite.py's H-e invokes. Linear equation only; says nothing about a nonlinear remainder.",
   "read_status": "READ (pp.1-6,8-9)"
  },
  {
   "ref": "arXiv:2105.09916 (mean value properties of solutions to the m-dimensional Helmholtz and modified Helmholtz equations, 2021)",
   "effect": "extends",
   "what": "Listed by discover_papers as treating the m-dimensional modified Helmholtz equation -- relevant to the d != 3 drift recorded above; not read, not relied on (the d-dimensional check here is C8, computed).",
   "read_status": "NAMED-NOT-READ (discover_papers abstract only)"
  }
 ],
 "lacked_data": "M's hypothesis tested: this result is a closed-form mathematical identity (half-integer-order Bessel functions reduce to elementary functions; known since the 19th century, tabulated in A&S 1964 and DLMF). It uses no measured datum, so there is no datum its authors could have lacked; the identity is re-derived here for every integer l from the ODE alone (C1) and matches K_{l+1/2} to 41 digits (C3). Evidence against 'lacked data' moving it: nothing numerical enters. Where the audit does find something, it is in the tree's USE, not in the outside result: (a) the witnesses are d = 3 only while H-e's text speaks of any d (C8, unnamed hypothesis); (b) the passage from the linear multipoles to the nonlinear non-spherical tail is a named hypothesis ('linear tail (f small)') that neither the source nor the tree proves for l >= 1; (c) l = 0..5 is the tree's check, the source covers all l. None of these is a defect of the published result.",
 "grade": "STANDS",
 "grade_evidence": "The identity as the tree states it (excite.py:710-712; normalisation 'up to normalisation') is exactly the published closed form: MathWorld/Stoutemyer normalisation, (2/pi) x DLMF 10.49.12. Re-derived symbolically for general integer l (C1) and exactly for l <= 12 (C2); numerically equal to (2/pi) sqrt(pi/2x) K_{l+1/2} to 2.3e-41 (C3); Stoutemyer's Table 6 reproduced (C4); the tree's own data (residual 0 for l = 0..5, rate within 1e-5 of 1 at x = 1e6) reproduced with margin (max 1.0000150e-6) (C5b); control fails as it should (C6). No datum enters, so none can move. The grade is for the external result. Recorded as drifts in the USE, not as defects of the result: the witnesses are d = 3 only while H-e's wording mentions 'any d' (C8, unnamed in the tree at excite.py:77-79/1082); the linear-to-nonlinear step for non-spherical tails is named by the tree as a hypothesis and is not proved by the source; the infinite-l interchange is supplied here (C9) but stated by neither.",
 "what_would_change_the_grade": "Nothing about the identity: it is proved for every integer l here. The USE would be graded NARROWED if D15/H-e were read as claiming non-spherical tail coverage in d != 3 with these k_l (C8 shows the tree's k_l are wrong there; the correct d-dim functions are x^{1-d/2}K_{l+d/2-1}), or if a later docket relied on the nonlinear non-spherical tail rate without a proof beyond linearisation. A misprinted coefficient in k_l_poly would show as a C2/C4 failure and would be a discrepancy, not a refutation of the source.",
 "reverify_command": "python3 " + S + "   # exits 0 with 'OVERALL: ALL PASS'; owner check: cd /home/user/Claude-Method-Works/research/warp-drive && python3 excite.py --verify (V6 rows) ",
 "report_path": R
}
json.dump(rep, open(R, "w"), indent=1)
print("wrote", R)
