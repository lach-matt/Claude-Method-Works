import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
S = D + "/rederive/gr-qc_9805003.py"
r = {
 "key": "gr-qc/9805003",
 "name": "Olum, 'Superluminal travel requires negative energies' (gr-qc/9805003v2; PRL 81, 3567 (1998)): a causal path P satisfying Condition 1, with the generic condition on P, forces WEC violation at some point of P",
 "source": {
  "located": "arXiv gr-qc/9805003v2 (14 Oct 1998; dated August 1998), K.D. Olum, Institute of Cosmology, Tufts; journal ref PRL 81, 3567 as cited by Visser-Bassett-Liberati gr-qc/9810026 ref.[7]. PRL typeset version NOT read.",
  "read_status": "READ",
  "via": "alphaXiv get_paper_content(fullText=true) returned all 8 pages (abstract, text, Figs.1-5, Eqs.(1)-(11), note added in proof, refs [1]-[8]); a second answer_pdf_queries call returned the same page text. Every quotation below is from that text."
 },
 "published_statement": "Abstract: 'I propose a definition of superluminal travel which requires that the path to be traveled reach a destination surface at an earlier time than any neighboring path. With this definition (and assuming the generic condition) I prove that superluminal travel requires weak-energy-condition violation.' p.4 Condition 1: 'There exist 2-surfaces Sigma_A around A and Sigma_B around B such that (i) if p in Sigma_A then a spacelike geodesic lying in Sigma_A connects A to p, and similarly for Sigma_B, and (ii) if p in Sigma_A and q in Sigma_B then q is in the causal future of p only if p = A and q = B.' p.6: 'any spacetime that admits superluminal travel on some path P (and thus, according to our definition, that satisfies Condition 1) and that satisfies the generic condition on P, must also violate the weak energy condition at some point of P.' p.6: 'The present theorem rules out the existence, rather than construction, of superluminal travel, unless there is weak energy condition violation. Spacetime singularities do not provide an alternative ... and the WEC violation must occur along the path to be traveled.' p.6: 'Does this theorem mean that superluminal travel is impossible? No, because the weak energy condition is not obeyed by systems of quantum fields.' Separate earlier result, p.3 (Fig.2 case): S flat except a region t>t0, x in [x1,x2], y,z in boxes; causal P from (t1,x1) to (t2,x2) with t2-t1 < x2-x1; S has no singularities; modified region obeys the generic condition => by Tipler's and Hawking's theorems 'WEC must be violated somewhere in S' (location NOT on P).",
 "published_hypotheses": [
  "H1 Condition 1 (the DEFINITION of superluminal): 2-surfaces Sigma_A, Sigma_B each made of spacelike geodesics through A (resp. B), and no point of Sigma_B in the causal future of any point of Sigma_A except B from A -- a comparison with NEIGHBOURING paths in ONE spacetime, no reference geometry",
  "H2 the generic condition on P: K_[a R_b]cd[e K_f] K^c K^d != 0 somewhere on P ('holds whenever there is any normal matter or any transverse tidal force anywhere on P')",
  "H3 (unwritten in the paper, used at Eq.(3)) Einstein's equations: 'If the weak energy condition is satisfied, then R_ab K^a K^b >= 0' -- the step needs only T_ab K^a K^b >= 0 for null K, i.e. the NEC, so the proof in fact yields NEC violation on P (stronger than the stated WEC violation)",
  "H4 (implicit) classical smooth 4-dimensional Lorentzian geometry, C^2 enough for Raychaudhuri/Jacobi fields and Riemannian normal coordinates at B; T_ab classical (the paper names quantum fields as the escape)",
  "H5 P actually reaches B ('Spacetime singularities do not provide an alternative (other than by making the purported path not actually reach the destination)')",
  "NOT assumed (verified by reading the proof): staticity, any symmetry, sphericity, asymptotic flatness, a foliation, global hyperbolicity, a reference metric",
  "Author's own caveat (p.4): Condition 1 'might not be sufficient for what one would call superluminal travel' -- P may beat its neighbours yet be slower than a distant path. Harmless for a necessity claim.",
  "Proof-internal step argued informally (p.5): no point of P, including B, is conjugate (focal) to Sigma_A; the B case is argued in two sentences about tangent vectors. Not re-proved or machine-checked here; recorded, not graded."
 ],
 "hypothesis_drift": [
  "DROPPED Condition 1 AND the generic condition -- ledger.py:394-397 (row D5): 'Superluminal travel requires negative energies, with NO staticity, NO symmetry and NO sphericity, pointwise on the path travelled'. 'Superluminal' is left undefined; Olum's paper exists because it cannot be left undefined (abstract; the Eq.(1) flat-space example). The 'no staticity/symmetry/sphericity' part is accurate.",
  "CHANGED CLASS: from a Condition-1 path to a 'lead' (negative Shapiro delay against a reference geometry) -- spec.py:13-15 ('negative Shapiro lead -- and every theorem in the way (Olum, ...)'), spec.py:106-107 ('There is no lead, and by Olum there cannot be one without negative energy'), spec.py:198 DOES_NOT[1], specthm.py:1367-1371 (SR3 'a lead needs negative energy (D5 ...)'), specthm.py:2835-2837 (V1 'Olum (D5) concerns superluminal travel -- the lead'). Combined with D5's 'pointwise on the path travelled' this claims more than Olum proves: rederive C7 shows a lead with T_ab = 0 (WEC and NEC holding) at every point of the leading path. What does cover a lead: Olum's p.3 argument (flat outside a compact region, no singularities, generic condition in the modified region) giving WEC violation SOMEWHERE, not on P; VBL gr-qc/9810026 in the weak field (NEC violation weighted over the backward light cone, not on the path).",
  "CHANGED CLASS: reference-geometry criterion D4 -- foliation.py:235-241 and :614 ('D4 OPERATIONAL: a signal from mouth to mouth arrives EARLIER than in the reference geometry ... THE THEOREM IS REPLACED BY A STRONGER ONE ...: Olum gr-qc/9805003, Gao & Wald ..., VBL ... -- with the NEC, never an advance'). Olum's main theorem has no reference geometry; 'never an advance' is VBL's/Gao-Wald's form, not Olum's. The reference must also be Minkowski-like: VBL p.3 records voids giving a Shapiro ADVANCE relative to FRW with no NEC violation.",
  "DROPPED the energy-condition hypothesis in wording -- driven.py:334-336 ('IT DOES NOT PROVE that no dynamic spherically symmetric corridor exists ... The proof of that statement is Olum's'), driven.py:499 REFUSED ('no proof that dynamic corridors are impossible (that is Olum's ...)'), foliation.py:395-397 ('IT DOES NOT SHOW THAT NO DYNAMIC SPHERICAL CORRIDOR EXISTS. That is Olum's theorem'), foliation.py:877-879 REFUSED. Read literally these credit Olum with an unconditional impossibility proof; Olum p.6: 'Does this theorem mean that superluminal travel is impossible? No'. What he proves is conditional (Condition 1 + generic => WEC violated on P). foliation.py:74-76 ('the bill is still not lifted') states it correctly as a cost, not an impossibility.",
  "ADDED UNSTATED PREMISE -- driven.py:311-312 and :517-518 ('therefore the corridor may be buildable without negative energy' REFUTED by 'Hochberg & Visser 1998, Olum 1998'): applying Olum needs the corridor's transit to be a Condition-1 path; no owner shows the corridor criterion (Gamma > 1 / contraction / D1-D4) entails Condition 1. foliation.py:238 itself files Olum under D4, which is not Condition 1.",
  "CITED FOR A CONFIGURATION IT DOES NOT GOVERN -- composite.py:116-117 ('Olum ... for the requirement of negative energy, which this configuration supplies'): composite's early ray passes outside a point M<0 (T_ab = 0 on it); by spec.py:82-83 ('WEYL FOCUSING IS SIGN-BLIND ... the term that made a negative source focus while leading') the tree's own leading ray focuses, i.e. is not a Condition-1 path (rederive C7b). Olum's on-path requirement is therefore not the operative constraint there; the necessity reading is not contradicted, only mis-attributed.",
  "FAITHFUL, recorded for balance -- driven.py:109-114 states Condition 1 (as 'arriving earlier than every neighbouring path'), the generic condition, the on-path conclusion and the absent symmetry hypotheses; it omits Condition 1(i) (the geodesic 2-surfaces) and Olum's own insufficiency caveat, neither of which weakens a necessity claim. driven.py:46-50, :484, :896-898 and foliation.py:74-76 ('needs no staticity, no sphericity and no foliation') are accurate.",
  "UNWRITTEN in every owner: H3 Einstein equations and H4 classical smooth 4D geometry. Direction of that omission: the tree says 'WEC'; the proof gives NEC violation on P (stronger); foliation.py:240 ('with the NEC') is the accurate reading. The tree UNDER-states here, not over-states."
 ],
 "data_at_publication": [
  {
   "quantity": "numerical inputs to the theorem",
   "value_then": "none: the result is a statement of Lorentzian geometry + Einstein equations; no measured constant enters",
   "value_now": "none",
   "source_now": "the proof as READ (pp.4-6)",
   "moves_conclusion": "no -- nothing to move; only a hypothesis (H1-H4) can fail"
  },
  {
   "quantity": "Casimir stress tensor between ideal plates (illustrative example, Eq.9), and R_ab K^a K^b (Eq.10)",
   "value_then": "T_ab = pi^2/(720 d^4) diag(-1,1,1,-3); R_ab K^a K^b = -2 pi^3/(45 d^4) (hbar=c=G=1)",
   "value_now": "the ideal-plate formula is derived, not fitted; re-derived here (C5): traceless, R_KK = 8 pi T_KK = -2 pi^3/(45 d^4), T_00 < 0. No later measured value was looked up: the example is not a premise of the theorem",
   "source_now": "rederive C5 (sympy)",
   "moves_conclusion": "no -- and the example concerns only the converse (Condition 1 met with NEC violation), which Olum himself flags as incomplete (plate mass and supports not included)"
  },
  {
   "quantity": "Eq.(1) example arrival time at x = 1",
   "value_then": "text layer: '(1 + sqrt5)/2 ~ 0.618'",
   "value_now": "(sqrt5 - 1)/2 = 0.618034 (root of t^2+t-1=0); (1+sqrt5)/2 = 1.618",
   "source_now": "rederive C2c (sympy)",
   "moves_conclusion": "no -- a DISCREPANCY in the printed expression of the arXiv text layer (possibly a minus lost in extraction; PRL version not read), the numeral 0.618 is right, and nothing downstream uses it. Not an error in the theorem; MUST NOT be quoted as one."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": S,
  "outcome": "ALL PASS (17 checks, ~2.5 s). C1 Eq.(1) is flat space under x'=x(1-t^2) (sympy identity). C2 null slopes Eq.(2) and the null ray x=t/(1-t^2) re-derived; arrival (sqrt5-1)/2=0.618, printed '(1+sqrt5)/2' recorded as discrepancy. C3 polarisation: II(X,X)=0 for all X => II=0, so theta-hat(A)=0. C4 z3: the sign logic of Eqs.(4)-(8) (NEC on P + generic + Condition 1) is UNSAT; vacuity guard with NEC dropped is SAT. C5 Casimir Eq.(9)-(10) re-derived exactly. C6 linearised optical tidal matrix T_ij = 2 d_i d_j Phi + delta_ij d_x^2 Phi from the Riemann tensor (sympy). C7 THE NARROWING, SHOWN (numeric, Riccati B'=-B^2-T along straight rays, M=-1e-3, R=1, L=400): ray b=2 outside a negative-mass ball leads flat space by -2.397e-2 with rho=0 on the path (WEC/NEC hold pointwise) and theta-hat(B)=-9.50e-4<0 (focused, not Condition 1); ray b=0 through the ball leads most (-2.930e-2), has rho=-2.39e-4 on P and is defocused (theta-hat(B)=+3.53e-3) -- Olum's conclusion on the locally best path. Control M=+1e-3: same theta-hat(B) (Weyl focusing sign-blind), delay +2.397e-2. Limits named: linearised field, Born (straight-ray) approximation, the negative-density ball PRESCRIBED not a self-consistent solution; C4 checks the sign logic given its premises, not the informal no-focal-point-at-B step.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "Visser, Bassett, Liberati, 'Superluminal censorship', gr-qc/9810026v2 (1999)",
   "effect": "extends",
   "what": "Weak field around Minkowski: NEC => g_mn k^m k^n = 16 pi G INT T_mn k^m k^n/|x-y| >= 0, so the Shapiro time delay is 'always a delay relative to the Minkowski background, and never an advance'. Calls itself 'complementary' to Olum [7]. The NEC violation needed for an advance is weighted over the backward light cone -- NOT on the path; and 'voids ... can sometimes lead to a Shapiro time advance' relative to FRW without NEC violation. This is the result that governs a LEAD; it narrows the tree's use of Olum for one.",
   "read_status": "READ (all 4 pages via alphaXiv answer_pdf_queries)"
  },
  {
   "ref": "Celmaster & Rubin, 'Violations of the Weak Energy Condition for Lentz Warp Drives', arXiv:2511.18251 (Nov 2025)",
   "effect": "confirms",
   "what": "Lentz's 2020 positive-energy soliton is shown by direct computation to have negative Eulerian energy density (sign error; phi_L not a solution of Lentz's own equation); corrected variants also violate WEC. The one recent candidate counterexample to the WEC-violation family does not stand. Restates Santiago-Schuster-Visser: zero-vorticity Natario drives violate WEC given fast fall-off of S^i, NEC given an on-off condition; names differentiability as a further hypothesis.",
   "read_status": "READ (pp.1-6, 11-15, 20-27, 31-37 via alphaXiv)"
  },
  {
   "ref": "Santiago, Schuster & Visser, arXiv:2105.03079 (generic warp drives violate the NEC)",
   "effect": "extends",
   "what": "Time-dependent Natario warp drives violate the NEC under an on-off condition; complements Olum without Condition 1 (as restated in 2511.18251 p.34).",
   "read_status": "READ-VIA-RESTATEMENT (Celmaster-Rubin 2511.18251 sec.7); not read at source in this audit"
  },
  {
   "ref": "Lentz arXiv:2006.07125; Fell & Heisenberg arXiv:2104.06488; Bobrick & Martire; Lentz 'Hyper-Fast Positive Energy Warp Drives' arXiv:2201.00652",
   "effect": "contested",
   "what": "Claims of positive-energy superluminal solitons; none read here. 2511.18251 refutes Lentz's and reports a Fell-Heisenberg drive with positive Eulerian density that still violates WEC. None shown here to exhibit a Condition-1 path with WEC on P.",
   "read_status": "NAMED-NOT-READ (titles/abstract snippets from discover_papers only)"
  },
  {
   "ref": "Penrose, Sorkin & Woolgar, gr-qc/9301015 (note added in proof); arXiv:1904.12123 (Gao-Wald validity); arXiv:2004.12523 (apparent superluminal drives in generic gravity theories)",
   "effect": "extends",
   "what": "Related positive-mass / time-advance results and scope questions for Gao-Wald and beyond GR; relevant to H3 (Einstein equations) but not read.",
   "read_status": "NAMED-NOT-READ"
  }
 ],
 "lacked_data": "M's hypothesis tested for this result: the theorem uses NO measured datum -- it is Lorentzian geometry (Raychaudhuri, Jacobi fields, normal coordinates) plus the Einstein-equation step WEC => R_ab K^a K^b >= 0 -- so there is no datum the author lacked that could move it; only a hypothesis can fail. Evidence that nothing later has broken it: the sign logic re-derives (C4 UNSAT, vacuity guard SAT), the Casimir example re-derives exactly (C5), the one prominent later counterexample claim (Lentz 2020) is refuted by computation in 2511.18251, and no source read here exhibits a Condition-1 path with WEC holding on it. Evidence that its REACH is smaller than the tree uses: what Olum could not have and did not claim is a statement about leads against a reference geometry; the later weak-field result that does (VBL 1999) places the NEC violation off the path, and C7 exhibits a lead with WEC/NEC holding everywhere on the path. The escapes Olum names himself (quantum fields violate WEC) and the unwritten H3 (beyond-GR theories where NEC need not imply null convergence) are hypotheses, not data, and are not tested here.",
 "grade": "NARROWED",
 "grade_evidence": "The theorem itself STANDS as published: READ in full at source; no staticity/symmetry/sphericity/foliation hypothesis (confirmed); sign logic of Eqs.(4)-(8) machine-checked (z3 UNSAT, vacuity SAT); Eq.(1), Eq.(2), Eqs.(9)-(10) re-derived; the proof in fact gives NEC violation on P (stronger than stated). One printed-expression discrepancy '(1+sqrt5)/2 ~ 0.618' (value right) -- a discrepancy, not a refutation. NARROWED because the tree uses it on a larger class than it covers: (a) ledger D5 (ledger.py:394-397) drops Condition 1 and the generic condition; (b) spec.py:106-107/198, specthm.py:1367-1371, 2835-2837 and foliation.py:235-241 apply it to a LEAD / earlier-than-reference-geometry criterion, which Olum's main theorem does not address -- and together with D5's 'pointwise on the path travelled' the tree's reading is shown false for leads by C7 (lead with T_ab = 0 on the path, M=-1e-3 ball, b=2: delay -2.397e-2, theta-hat(B)=-9.50e-4); (c) driven.py:334-336/499 and foliation.py:395-397/877-879 credit Olum with an impossibility proof he explicitly disclaims (p.6 'No'); (d) driven.py:311-312/517-518 apply it to 'the corridor' without showing the corridor criterion entails Condition 1. What survives unchanged: every use that reads 'a Condition-1 path with the generic condition needs WEC (indeed NEC) violation on that path, with no symmetry assumed' -- driven.py:109-114, foliation.py:74-76. Nothing in the tree is repaired by this audit.",
 "what_would_change_the_grade": "To STANDS: the tree restates D5 with Condition 1 and the generic condition, and re-cites a lead / reference-geometry claim to Olum's p.3 compact-support argument (WEC somewhere, not on P), Gao-Wald or VBL with their hypotheses, and drops 'pointwise on the path' for leads; or an owner shows the corridor criterion entails a Condition-1 path. To WRONG: an explicit smooth classical solution of Einstein's equations with a Condition-1 path, the generic condition on it and T_ab K^a K^b >= 0 along it (none known; Lentz 2020 refuted in 2511.18251), or a demonstrated failure of the informal no-focal-point-at-B step that the proof cannot absorb. To OPEN: none -- the source is read and the finite content checked.",
 "reverify_command": "python3 " + S,
 "report_path": D + "/audits/gr-qc_9805003.json"
}
json.dump(r, open(r["report_path"], "w"), indent=1)
print("written", r["report_path"])
