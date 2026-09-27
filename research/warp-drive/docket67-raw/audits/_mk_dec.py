import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
rep = {
 "key": "dominant-energy-condition",
 "name": "Dominant energy condition (DEC), as the admissibility test in axial.py's two failed scans and as the hypothesis of the positive-mass-theorem rigidity clause in concentric.py",
 "source": {
  "located": "Hawking & Ellis, The Large Scale Structure of Space-Time (CUP 1973) sec. 4.3. No arXiv copy: NAMED-NOT-READ. Read through exact restatements in two arXiv papers: (i) Pisana, Shoshany, Antoniou, Kauffman, Lambropoulou, arXiv:2505.02210v4, Sec. II.A (covariant DEC plus the hierarchy); (ii) Santiago, Schuster, Visser, 'Generic warp drives violate the null energy condition', arXiv:2105.03079v2, pp.15-16, eqs. (5.6)-(5.9) (the Hawking-Ellis type-I forms) and p.20, eq. (5.35). The initial-data form 'mu >= |J|_g' that the positive mass theorem uses was read in Kunduri, Margalef-Bentabol, Muth, arXiv:2409.07639v1, p.1. The rigidity clause's statement (Eichmair-Huang-Lee-Schoen arXiv:1110.2087 Thm 1 and p.2; Huang-Lee arXiv:1706.03732) was READ by this docket's sibling audit positive-mass-theorem.json and is cited from that audit here, not re-read.",
  "read_status": "READ-VIA-RESTATEMENT",
  "via": "This pass's own alphaXiv calls (answer_pdf_queries on 1702.05915 and 1405.0403, get_paper_content on 1702.05915, discover_papers) all returned 'alphaXiv assistant quota exceeded'. arxiv.org is blocked by the egress proxy for curl and WebFetch (403 / EGRESS_BLOCKED). The texts actually read are alphaXiv full-text or page extractions that earlier stages of this workflow banked in the scratchpad: d67/2505.02210.txt lines 985-1125; d67/src/gklm_cached.txt (2105.03079v2) lines 108-135, 225-260 and 500-516; d67/src/hawk/Hawking_answer_pdf_queries.txt (2409.07639v1 p.1) lines 1-30. Each was read in full at those lines this pass. Hawking-Ellis 1973 itself was not read."
 },
 "published_statement": "Covariant form (2505.02210 Sec. II.A, restating the standard conditions with no cosmological constant, citing [5]=Hawking-Ellis): 'Dominant energy condition (DEC): T_mu nu t^mu t^nu >= 0, g^L_mu nu T^mu_alpha T^nu_beta t^alpha t^beta <= 0, for all t^mu : g^L_mu nu t^mu t^nu < 0.' Hierarchy (same page): 'If the NEC is violated, then all the other energy conditions are violated as well. If the WEC is violated, then the DEC is also violated.' Type-I form (2105.03079 p.16, eq. 5.9): 'in terms of the Lorentz-invariant eigenvalues of a type I stress-energy tensor one has the two-way implications ... DEC <=> |p_i| <= rho.' The same paper, p.15: 'FEC -- flux energy condition: for all timelike observers, V^a, the flux F^a = T^ab V^b is either timelike or null ... (FEC is a weakening of DEC; that is, DEC => FEC.)' Initial-data form (2409.07639 p.1): 'energy-momentum density mu, J ... are assumed to satisfy the dominant energy condition mu >= |J|_g.'",
 "published_hypotheses": [
  "Classical GR with T_ab defined through the Einstein equation and no cosmological constant (2505.02210 Sec. II.A).",
  "The condition must hold for every timelike t (and, by continuity, every causal t), at every point. It is pointwise and observer-universal.",
  "The eigenvalue form rho >= |p_i| holds only for Hawking-Ellis type I stress-energy (2105.03079 p.16: 'assume the stress-energy tensor is of Hawking-Ellis type I').",
  "The DEC is a hypothesis about matter, not a theorem and not a measurement. In the 3+1 initial-data setting it is mu >= |J|_g (2409.07639 p.1), which on a time-symmetric slice (k = 0, J = 0) reduces to mu >= 0, i.e. R_g >= 0 (EHLS 1110.2087 p.2, per sibling audit)."
 ],
 "hypothesis_drift": [
  "ADDED (strengthened), axial.py:78-80: scan 1 counts profiles with 'u > 0 with the DEC'. The DEC requires u >= 0 (check A5), not u > 0 (check A6 is sat). Minkowski has u = p_r = p_z = p_phi = 0, so it satisfies the DEC and fails the test (check C, last line). The test is strictly stronger than the DEC. The conclusion does not move: the theorem gives INT 8 pi u W < 0 strictly whenever Psi' is not identically 0, so u < 0 strictly somewhere, and the DEC's own energy clause fails.",
  "WORDING, axial.py:85-86 and :220: '3959 of 4000 failures were u <= 0 -- not the DEC' and SCAN_DIAGNOSTIC's two bins ('u <= 0 somewhere' vs 'DEC fails with u > 0'). u < 0 IS a DEC failure, through its energy clause T(t,t) >= 0 (checks A3, A5). Read literally, 'not the DEC' is wrong. Read as intended, the split is energy clause vs pressure clause (|p_i| <= u, check A2), and that split is sound. A second point: the 'u <= 0' bin also takes in points with u = 0, where the DEC can hold (u = p = 0). The scan code is not banked anywhere in research/warp-drive (grep for 20000/300000/3959 finds only axial.py's own quotations), so how u = 0 was binned cannot be re-run. This is a discrepancy, not a refutation, and the tree already says the scans are not evidence (axial.py:89, :197).",
  "STRENGTHENING THE TREE DID NOT STATE, axial.py:74-91 with HYPOTHESES at axial.py:186-187: under the file's own two boundary conditions, plus W > 0 on (0, inf), which the theorem's '<= 0' also needs implicitly, the identity gives INT 8 pi u W = -INT W Psi'^2 <= 0. So u >= 0 everywhere forces u == 0 and Psi' == 0. No non-vacuum matter satisfying even the DEC's energy clause exists in the class, contracting or not (check C: with Psi' == 0 and W != r, u still changes sign and INT 8 pi u W = 0 to 1e-10). Scan 2's zero control ('the search space contained no admissible matter at all', axial.py:82-84) is therefore entailed by the boundary conditions, if the scan imposed them (not checkable: code not banked). It was not an accident of sampling. This fits with axial.py:126-136: an ordinary cosmic string needs a conical defect, and W' -> 1 at infinity together with a regular axis leaves no room for one.",
  "WEAKENED CONCLUSION (hypothesis stronger than needed), concentric.py:126-131 and pair.py:307-308 (PMT_HYPOTHESES includes 'dominant energy condition'): for a static configuration the slice is time-symmetric (k = 0, J = 0), and rigidity needs only mu >= 0, i.e. R_g >= 0 (check D5: R_h - 16 pi mu = 0 on the general static spherical slice; D6). The DEC implies mu >= 0 (A5), so the tree's hypothesis is stronger than the theorem requires. Its conclusion 'its matter CANNOT satisfy the DEC' is implied by, and weaker than, what the theorem gives: 'mu < 0 somewhere on the static slice'. That is the content of concentric.py:122-124 ('Its local energy density is negative'), which the tree marks SUPERSEDED. That content is in fact also derived by rigidity. The drift runs against over-claiming, not in the tree's favour.",
  "DROPPED (exactness), concentric.py:51-53, 126-131 vs concentric.py:139-140: the PMT rigidity clause is a theorem about exact, complete, asymptotically flat initial data. concentric.py is a linearised weak-field construction with Phi_max ~ m/a = 0.25 (named 'NOT small' at :139-140), and its M_ADM = 0 is the cancellation of linear monopoles. Applying rigidity to it drops the exact-solution hypothesis. The conclusion survives without rigidity: the core is a Plummer sphere of mass -m, so rho = -3 m a^2 / (4 pi (r^2+a^2)^(5/2)) < 0 everywhere (D1, D2). At linear order the stresses vanish (D4: G_xx = G_xy = 0 at O(eps)), so the core is type I and the DEC fails through its energy clause directly.",
  "INTERNAL WORDING, concentric.py:365 vs :126-131: the VERDICT print still says 'Negative mass is still assumed' after the header marks 'ASSUMED' SUPERSEDED ('IT IS NOT ASSUMED, IT IS DERIVED'). Both readings are defensible. The -m core is an input of the construction (:44, :163-167), and rigidity shows it is forced. This is recorded as a wording discrepancy in the owner's rests_on_it site, not an error."
 ],
 "data_at_publication": [
  {
   "quantity": "Any numerical input to the DEC itself",
   "value_then": "none: the DEC is a definition (Hawking-Ellis 1973) with no datum",
   "value_now": "none",
   "source_now": "2505.02210 Sec. II.A; 2105.03079 eq. (5.9)",
   "moves_conclusion": "no: there is no datum to move"
  },
  {
   "quantity": "Scan counts the tree reports (0 of 20000; 0 of 300000; 3959 u<=0 and 41 DEC-fails-with-u>0 of 4000)",
   "value_then": "as quoted at axial.py:78-86, 215-220",
   "value_now": "not re-measurable: the scan code is not banked anywhere in research/warp-drive",
   "source_now": "tree-internal. grep -n -E '20000|300000|3959' research/warp-drive/*.py finds only axial.py's own quotations",
   "moves_conclusion": "no: the tree declares them non-evidence (SCANS_ARE_EVIDENCE = False, axial.py:197), and the theorem, re-derived here (B3, C), implies every non-flat profile of the class has u < 0 somewhere, so '0 admissible' is what any faithful scan must return"
  },
  {
   "quantity": "axial.py regular-axis fixtures used to cross-check the identity",
   "value_then": "(0.4,1,0,1) -> -0.0800000000; (1.3,0.7,0.8,1.4) -> -1.0776404390; (0.9,1.7,-0.15,2.5) -> -0.3109284490",
   "value_now": "-0.0800000000; -1.0776404390; -0.3109284490 (Simpson, 60001 nodes on [0,30], this pass)",
   "source_now": "rederive/dominant-energy-condition.out, section C",
   "moves_conclusion": "no: reproduced to 1e-10"
  },
  {
   "quantity": "Empirical status of the DEC for real matter",
   "value_then": "1973: posited for classical matter",
   "value_now": "all pointwise energy conditions are violated by quantum fields and by some simple classical fields (Kontou & Sanders, arXiv:2003.01815, CQG 37 (2020) 193001, per its abstract as returned by web search; NOT read at source this pass)",
   "source_now": "arXiv:2003.01815 (abstract only)",
   "moves_conclusion": "no for both owners: axial.py's theorem uses no energy condition (ENERGY_CONDITION_USED = None, :190), and concentric.py uses the DEC only contrapositively, to derive that its own matter violates it, never as a law that forbids anything"
  }
 ],
 "rederivation": {
  "method": "z3",
  "script_path": D + "/rederive/dominant-energy-condition.py",
  "outcome": "ALL CHECKS PASS (exit 0; output banked at rederive/dominant-energy-condition.out). A1-A6, z3 (all negations unsat, except A6, which is sat as intended): Hawking-Ellis DEC on diag(rho,p1,p2,p3) <=> rho >= |p_i|, both directions (converse by explicit witnesses t=(1,0,0,0) and t=(1,s,0,0) with s^2 = ((rho/p1)^2+1)/2). Energy >= 0 plus a causal flux forces a future-directed flux, so 2505.02210's two-clause form equals the four-clause one. DEC => rho >= 0, but not rho > 0. B1-B3, sympy on axial.py's metric: T^a_b is exactly diagonal (type I at every point, so the DEC in that class is exactly u >= |p_r|,|p_z|,|p_phi|); u is independent of Phi; the identity 8 pi u W = -(W Psi')' - W Psi'^2 - W'' holds with residual 0. C, numeric: the identity reproduced on five profiles, including axial.py's fixtures to 1e-10; u < 0 somewhere in every non-flat profile, including Psi' == 0 with W != r; Minkowski passes the DEC and fails 'u > 0'. D1-D6, sympy: the Plummer core has rho < 0 everywhere and integrates to -m; the linearised metric has G_00 = 2 eps lap f and G_ij = 0 at O(eps); on a static slice R_h = 16 pi mu with mu = M'/(4 pi r^2), so time-symmetric rigidity needs mu >= 0 only.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "Kontou & Sanders, 'Energy conditions in general relativity and quantum field theory', arXiv:2003.01815, Class. Quantum Grav. 37 (2020) 193001",
   "effect": "narrows",
   "what": "Per its abstract: all pointwise energy conditions, the DEC among them, are systematically violated by quantum fields and by some simple classical fields. Averaged conditions and quantum energy inequalities are the weaker replacements. This narrows the DEC's range as a physical law. It does not touch either owner's use, since neither uses the DEC as a law.",
   "read_status": "NAMED-NOT-READ (abstract via WebSearch only; alphaXiv quota exhausted and arxiv.org egress-blocked this pass)"
  },
  {
   "ref": "Santiago, Schuster, Visser, arXiv:2105.03079v2 (2022)",
   "effect": "confirms",
   "what": "Restates the Hawking-Ellis type-I forms (5.6)-(5.9) and DEC => FEC. It shows generic warp drives violate the WEC and hence the DEC (p.3; lines 77-88 of the cached text), which agrees with the board's refusals.",
   "read_status": "READ (cached alphaXiv extraction, d67/src/gklm_cached.txt)"
  },
  {
   "ref": "Huang & Lee, 'Equality in the spacetime positive mass theorem', arXiv:1706.03732 (CMP 2020); Eichmair-Huang-Lee-Schoen arXiv:1110.2087",
   "effect": "extends",
   "what": "Rigidity under the DEC in 3 <= n <= 7, including the E = |P| case. For the static data used here P = 0, so only the older E = 0 rigidity is needed. In the time-symmetric case the DEC reduces to R_g >= 0.",
   "read_status": "READ by sibling audit d67/audits/positive-mass-theorem.json; not re-read this pass"
  }
 ],
 "lacked_data": "The DEC is a definition that Hawking & Ellis (1973) posited as a property of physically reasonable classical matter. No numerical datum enters it, so there is no measured input that could have moved. What came later is evidence about whether real matter obeys it. Quantum fields violate every pointwise energy condition, the DEC included: Casimir-type configurations have negative local energy density. Kontou & Sanders 2020 (abstract, not read at source) report that some simple classical fields violate them too. So M's hypothesis holds in one sense: the 1973 authors lacked the QFT results that narrow the DEC as a law of nature. Having those results changes nothing in this tree, and the evidence for that runs both ways. (a) axial.py's theorem assumes no energy condition (ENERGY_CONDITION_USED = None, axial.py:190; confirmed by B3, since the identity is pure geometry). Its conclusion, u < 0 somewhere, is a statement about what the Einstein equation returns, and it stands whatever matter exists. (b) concentric.py uses the DEC only contrapositively, to show its own core cannot satisfy it. A weaker DEC as a law would make such matter less forbidden, but it would not make the core's energy density any less negative (D1). Nothing the authors lacked reverses the direction of any conclusion here. The narrowing of the DEC as a law is favourable to the board, and the tree does not over-claim it either way.",
 "grade": "STANDS",
 "grade_evidence": "The published definition was read via exact restatements (2505.02210 Sec. II.A, 2105.03079 eq. 5.9, 2409.07639 p.1). It matches the tree's use, and the type-I equivalence the scans' diagnostic relies on was machine-checked in both directions (z3 A1-A4). The class axial.py scanned is type I at every point (B1), so 'u >= |p_i|' is exactly the DEC there. The tree's two uses are each sound. (1) axial.py uses the DEC only as a scan filter it declares non-evidence (:89, :190, :197). The theorem it does rely on is re-derived with residual 0 and uses no energy condition (B2, B3, C). (2) concentric.py uses the DEC as the rigidity hypothesis in the correct, contrapositive direction. Its conclusion also follows independently of rigidity, from the core's negative density (D1, D4). No datum enters the DEC, so none has moved. Discrepancies are recorded, not repaired, and none is a refutation or moves a conclusion: the strict 'u > 0' test (axial.py:78-80) is stronger than the DEC; 'u <= 0 ... not the DEC' (axial.py:85-86) mislabels an energy-clause DEC failure; rigidity is applied to a linearised construction (concentric.py:139-140); the tree states the DEC where time-symmetric rigidity needs only mu >= 0, so 'cannot satisfy the DEC' is weaker than the theorem gives (D5, D6); and the VERDICT print at concentric.py:365 still says 'assumed'. One finding goes beyond the tree: under axial.py's two boundary conditions, no non-vacuum matter even satisfies the DEC's energy clause, so scan 2's zero control is entailed by the hypotheses, if the scan imposed them. Not WRONG, because nothing refutes the definition or its use. Not NARROWED, because no hypothesis of the DEC is dropped by a use that needs it: the dropped exactness in concentric belongs to the rigidity theorem (key positive-mass-theorem-rigidity), and the conclusion survives it. Caveats on the grade: Hawking-Ellis 1973 is NAMED-NOT-READ; this pass's alphaXiv calls hit quota, so the restatements were read from texts banked earlier in the workflow; the scan code is not banked, so the scan counts are not re-measurable.",
 "what_would_change_the_grade": "NARROWED if the banked scan code turned up and showed its DEC test used a non-type-I criterion, or omitted a pressure clause while being quoted as 'the DEC' (the diagnostic would then mislabel its 41), or if a use of the DEC elsewhere on the board were found to rely on the eigenvalue form for a stress tensor that is not type I. OPEN if the restatements are judged insufficient without Hawking-Ellis sec. 4.3 read directly. WRONG would need a type-I tensor where rho >= |p_i| and the covariant DEC disagree, which z3 A1-A4 excludes.",
 "reverify_command": "cd /tmp && python3 /tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/dominant-energy-condition.py   # expects 'ALL CHECKS PASS', exit 0 (sympy, z3-solver). Tree cross-check: cd /home/user/Claude-Method-Works/research/warp-drive && python3 axial.py --selftest && python3 concentric.py --selftest; sources: sed -n 1040,1075p .../d67/2505.02210.txt ; sed -n 225,260p .../d67/src/gklm_cached.txt",
 "report_path": D + "/audits/dominant-energy-condition.json"
}
json.dump(rep, open(rep["report_path"], "w"), indent=1)
print("written")
