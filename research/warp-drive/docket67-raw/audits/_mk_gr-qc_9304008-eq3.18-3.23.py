import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "gr-qc/9304008-eq3.18-3.23",
 "name": "KF (3.18),(3.19),(3.22),(3.23): <:T00:> and <:T00^2:> for squeezed coherent and squeezed vacuum states",
 "source": {
  "located": "C.-I. Kuo & L. H. Ford, 'Semiclassical gravity theory and quantum fluctuations', arXiv gr-qc/9304008 v1 (1993), pp.7-9: Eqs. (3.9)-(3.17) (state and operator conventions), (3.18), (3.19), (3.20)-(3.21), (3.22), (3.23), and the p.9 conclusion; pp.5-6: (3.2)-(3.6) (definition of Delta, normal ordering). Journal version Phys. Rev. D 47, 4510 (1993) NAMED-NOT-READ.",
  "read_status": "READ",
  "via": "arXiv v1 PDF TEXT LAYER as returned by alphaXiv get_paper_content(fullText=true) earlier on 2026-09-26 in this docket (d67/src/gr-qc_9304008.note) and harvested verbatim to d67/src/casmag/all/gr-qc_9304008v1.txt (md5 f1a6628604751cf61b2a4bd411b00153), lines 975-1225 and 3060-3080 read in full for this key. A fresh fetch in THIS stage failed: answer_pdf_queries, get_paper_content and discover_papers each returned 'alphaXiv assistant quota exceeded'. Page image not viewed; journal version not read."
 },
 "published_statement": "v1 p.7-8, verbatim from the text layer: |alpha,zeta> = D(alpha)S(zeta)|0> (3.9); D(alpha) = exp(alpha a+ - alpha* a) (3.10); S(zeta) = exp[(1/2)zeta* a^2 - (1/2)zeta (a+)^2] (3.11); alpha = s e^{i gamma} (3.12); zeta = r e^{i delta} (3.13); S+ a S = a cosh r - a+ e^{i delta} sinh r (3.16). '<alpha,zeta|:T_ab(x):|alpha,zeta> = <0|S+D+(a^2 T_ab[f_k,f_k] + a+a(T_ab[f_k,f*_k] + T_ab[f*_k,f_k]) + (a+)^2 T_ab[f*_k,f*_k]) D S|0> = 2K_ab{sinh r cosh r cos(2theta+delta) + sinh^2 r + s^2[1 - cos 2(theta+gamma)]} (3.18)'. 'Simlarly, the expectation value of the squared stress tensor is <alpha,zeta|:T_ab(x)T_mn(x):|alpha,zeta> = 2K_ab K_mn ( s^4[cos 4(theta+gamma) - 4 cos 2(theta+gamma) + 3] + 3s^2{2 sinh r cosh r[2 cos(2theta+delta+2gamma) - cos(4theta+delta+2gamma)] + 4 sinh^2 r(cos 2gamma - cos 2theta) - cos(delta+2gamma)} + 3 sinh^2 r[cosh^2 r cos(4theta+2delta) + 3 - 4 cos 2theta] ). (3.19)'. 'In a squeezed vacuum, alpha = 0, we may also take delta = 0, as this is simply a choice of phase, and write <:T_ab(x):> = 2K_ab sinh r[cosh r cos(2theta) + sinh r]. (3.22)' 'For the case delta = 0 and alpha = 0, the expectation value of the squared stress tensor is <:T_ab T_mn:> = 2K_ab K_mn sinh^2 r[2 cosh^2 r cos 4theta - 8 sinh r cosh r cos 2theta + 3(sinh^2 r + cosh^2 r)]. (3.23) As required, for the vacuum state (r = 0) this quantity vanishes.' p.9: 'Our primary concern is whether or not Delta << 1, which is best determined by numerical evaluation of Delta using Eqs. (3.2), (3.18), and (3.19). ... By the point that the state is sufficiently squeezed to have rho = <:T00:> < 0, we always have that Delta is at least of order unity.'",
 "published_hypotheses": [
  "H1 massless minimally coupled free scalar in FLAT (Minkowski) spacetime, stress tensor bilinear (2.11); single plane-wave box mode k with (2.12)-(2.14): T[f,f] = -K e^{2i theta}, T[f,f*] = T[f*,f] = K, theta = k.x",
  "H2 single-mode squeezed coherent state D(alpha)S(zeta)|0> with KF's operator conventions (3.10)-(3.17): alpha = s e^{i gamma}, zeta = r e^{i delta}, S+ a S = a cosh r - a+ e^{i delta} sinh r",
  "H3 normal ordering with respect to the Minkowski vacuum for BOTH <:T:> and the quartic <:T T:> (KF p.5 after (3.2); (3.3)-(3.6): 'The effect of the normal ordering has been to remove the contribution of the n = 0 term from the diagonal part')",
  "H4 coincidence limit x -> y, purely temporal component for Delta (3.2)",
  "H5 squeezed vacuum = alpha = 0, and delta = 0 'as this is simply a choice of phase' ((3.22), (3.23))"
 ],
 "hypothesis_drift": [
  "NONE on the flags' substance: the tree's hypotheses ('single-mode squeezed coherent state, s = sinh r, c = cosh r, phases w, g'; 'squeezed vacuum = alpha 0, w = 1') are KF's H2 and H5 with w = e^{i delta}, g = e^{2i gamma}; fluctuation.py:241-260 transcribes (3.18), (3.19), (3.22), (3.23) term by term and this audit's independent transcription (rederive C1-C2) agrees with it (the tree's selftest and this script return the same four verdicts).",
  "DROPPED (harmless): H1 (massless, minimal, flat, box mode) and H3 (Minkowski normal ordering of the quartic) are not in the tree's hypothesis list for this key; they are carried by the operator at fluctuation.py:179-180 (sibling key gr-qc/9304008-t00-single-mode) and by fluctuation.py:13-18 ('normal-ordered against the Minkowski vacuum, flat spacetime, coincidence limit, massless minimally coupled scalar'). They are exactly KF's, so they move nothing; C7 shows the one plausible alternative reading of H3 (<:T::T:> minus its vacuum value) does not reproduce the print either.",
  "WIDENED (correctly, and proved): fluctuation.py:43-44 states '<:T00^2:> = 3 <:T00:>^2, IDENTICALLY' for the squeezed vacuum under the tree hypothesis w = 1; C4 proves it for every delta, so the claim holds on a larger class than the tree assumes. Not a drift against the tree.",
  "SCOPE (kept, correct): the verdicts are against the arXiv v1 TEXT LAYER only, journal NAMED-NOT-READ, page image not viewed (fluctuation.py:122-126, 135-136; status word 'READ (against arXiv v1 only)'). Named hypothesis of this audit too: the text layer is faithful. Evidence that the (3.19)/(3.23) discrepancy is not an extraction artefact: (a) (3.19) is structurally non-covariant under the exact U(1) phase symmetry (C6: depends on cos 2gamma, cos(delta+2gamma), cos(2theta+delta+2gamma), which no correct result can) -- a dropped glyph could cause this, but (b) (3.23) is short and differs from the exact 6K^2 s^2[c^2 cos4theta + 4sc cos2theta + 3s^2 + 1] in three independent coefficients (cos4theta: 4c^2 vs 6c^2; cos2theta: -16sc vs +24sc; constant), and (c) the print is inconsistent WITH ITSELF: (3.19) at alpha = 0, delta = 0 does not give (3.23) (C9). This is evidence, not proof; the page image would settle transcription.",
  "CROSS-KEY OVERREACH (named here, belongs to key gr-qc/9304008-qualitative-conclusion, not graded here): fluctuation.py:62-64 and :152 (KF_QUALITATIVE_CONCLUSION_SURVIVES = True) say KF's conclusion 'fluctuations of order unity wherever rho < 0 ... SURVIVES in every case they study'. The squeezed COHERENT state is a case they study (p.9, Figs. 1-4, built on (3.18),(3.19)), and the tree's theorem T1 (Delta >= 1/3) covers only ZERO-MEAN Gaussian states. With the exact <:T00^2:>, C8 exhibits, at KF's own Fig.1/2 parameters (gamma = delta = 0, theta = pi/2), a state with rho < 0 and Delta = 0 exactly: r = 1/2, s^2 = (1 - e^{-1})/8, rho/K = -0.316060, <:T00^2:> = rho^2 (Fock control agrees). KF's printed (3.19) gives Delta = 0.992 at the same point. Exact closed form (C5): rho = K(mu^2+v), <:T00^2:> = K^2(mu^4+6mu^2 v+3v^2), so Delta = 0 whenever v = -2mu^2, which lies inside rho < 0. Fair weight: on a grid r in (0,2], s in [0,2] the exact Delta < 0.1 on 81 of 8,615 rho<0 points (0.94%) -- order unity is typical, 'always' fails. Also, <:T00^2:> is not sign-definite (C3 point 1: -0.1498), so KF's Delta has poles inside the family."
 ],
 "data_at_publication": [
  {
   "quantity": "empirical inputs to (3.18)-(3.23)",
   "value_then": "none -- closed-form single-mode Fock/Gaussian expectation values; only the canonical commutator and KF's (2.12)-(2.14), (3.10)-(3.17)",
   "value_now": "none",
   "source_now": "re-derivation d67/rederive/gr-qc_9304008-eq3.18-3.23.py",
   "moves_conclusion": "No datum exists to move."
  },
  {
   "quantity": "tree check point r = 3/10, theta = 0.2 (squeezed vacuum, K = 1)",
   "value_then": "tree: Delta = 2/3 at a rho>0 point (fluctuation.py:405-416)",
   "value_now": "rho = +0.771862, exact <:T^2:> = 1.787313 = 3rho^2, KF (3.23) = 0.506957; Delta_exact = 0.666667, Delta from printed (3.23) = 0.175189",
   "source_now": "rederive C2 output (gr-qc_9304008-eq3.18-3.23.out)",
   "moves_conclusion": "No: reproduces the tree."
  },
  {
   "quantity": "tree check point r = 3/10, theta = 19pi/40 (squeezed vacuum, K = 1)",
   "value_then": "tree: Delta = 2/3 at a rho<0 point",
   "value_now": "rho = -0.443350, exact <:T^2:> = 0.589678 = 3rho^2, KF (3.23) = 1.511571; Delta_exact = 0.666667, Delta from printed (3.23) = 0.869964",
   "source_now": "rederive C2 output",
   "moves_conclusion": "No: reproduces the tree. Note both the exact and the printed Delta are order unity where rho < 0 in the squeezed vacuum, so for alpha = 0 the misprint does not move KF's qualitative reading."
  },
  {
   "quantity": "tree control r = 0.7, theta = 1.1 (Fock series vs Gaussian moments)",
   "value_then": "tree: Fock series agrees with Gaussian to 1e-12, printed (3.23) does not (fluctuation.py:418-446)",
   "value_now": "exact <:T^2:> = 0.0027388213 (Weyl route and 90-state Fock route agree to 1e-15; Fock tail 3.5e-19), KF (3.23) = 11.471068, KF (3.19) at alpha = 0, delta = 0 = 16.813995",
   "source_now": "rederive C2, C3 output",
   "moves_conclusion": "No: reproduces the tree."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/gr-qc_9304008-eq3.18-3.23.py",
  "outcome": "ALL CHECKS PASS, exit 0 (output rederive/gr-qc_9304008-eq3.18-3.23.out, md5 e412103d4025e485f05f2d8da3a0b87c; script md5 a6b337813f5cc45dc01d4c131503846b). Independent of fluctuation.py: no import, and a different method (explicit Weyl-algebra normal ordering of Heisenberg-transformed words, not the tree's generating function), controlled by a second independent route (state D(alpha)S(zeta)|0> built by 40-digit matrix exponentials of KF's own (3.10),(3.11) in a 90-state Fock space). C1: (3.18) and (3.22) are EXACT. C2: (3.19) and (3.23) are NOT exact; exact squeezed-vacuum <:T00^2:> = 6K^2 sinh^2 r[cosh^2 r cos4theta + 4 sinh r cosh r cos2theta + 3 sinh^2 r + 1]. C3: Fock and Weyl routes agree to 1e-15 at three generic points (incl. alpha != 0, gamma, delta != 0); KF (3.19) differs at all three. C4: squeezed vacuum <:T00^2:> = 3<:T00:>^2 identically for ANY delta, so Delta = 2/3 wherever rho != 0. C5: closed form rho = K(mu^2+v), <:T00^2:> = K^2(mu^4+6mu^2 v+3v^2), mu = <Q>, v = normal-ordered variance of the quadrature Q with :T00: = K:Q^2:. C6: exact rho and <:T^2:> and KF (3.18) are invariant under (theta+phi, gamma-phi, delta-2phi); KF (3.19) is not (difference 21.26 at a test point) -- a structural proof of non-exactness that does not depend on the algebra. C7: flipping the squeeze sign, the gamma sign or the theta sign, or replacing full normal ordering by <:T::T:> - <0|:T::T:|0>, reproduces neither (3.19) nor (3.23); (3.18) itself pins the squeeze convention. C8 (cross-key): exact Delta = 0 with rho < 0 at KF's Fig.1/2 parameters (see hypothesis_drift). C9: KF (3.19) at alpha = 0, delta = 0 gives 6K^2 sinh^2 r[cosh^2 r cos4theta + 3 - 4cos2theta], which disagrees with KF (3.23) and with 3rho^2 -- the v1 print is internally inconsistent. Tree side re-run: fluctuation.py --selftest returns (3.18) True, (3.19) False, (3.22) True, (3.23) False, 3rho^2 identity True, SELFTEST OK.",
  "agrees_with_source": "partly"
 },
 "later_literature": [
  {
   "ref": "B. L. Hu, A. Roura & E. Verdaguer, 'Induced quantum metric fluctuations and the validity of semiclassical gravity', arXiv:gr-qc/0402029",
   "effect": "narrows",
   "what": "'An earlier criterion put forth by Kuo and Ford [5] used the variance of the fluctuations of the stress tensor operator compared to the mean value as a measure of the validity of SCG. As pointed out by Hu and Phillips [27, 28] (see reply by Ford and Wu [7]) such a criterion should be refined by considering the back reaction of those fluctuations on the metric.' Narrows the use of Delta as a validity criterion; says nothing about the (3.19)/(3.23) coefficients.",
   "read_status": "READ from cached text d67/src/casmag/all/gr-qc_0402029v1.txt (~line 105), harvested earlier in this docket; Hu & Phillips and Ford & Wu NAMED-NOT-READ"
  },
  {
   "ref": "L. H. Ford & T. A. Roman, 'Averaged energy conditions and quantum inequalities', arXiv:gr-qc/9410043",
   "effect": "confirms",
   "what": "Restates KF's conclusion only qualitatively: 'recent work of Kuo and Ford [42, 43] indicates that in flat spacetime, negative energy densities are subject to large fluctuations'. No squeezed-state coefficients.",
   "read_status": "READ from cached text d67/src/casmag/all/gr-qc_9410043v1.txt (lines 2365-2368)"
  },
  {
   "ref": "M. J. Pfenning, PhD thesis 'Quantum Inequality Restrictions on Negative Energy Densities in Curved Spacetimes' (Ford's student), arXiv:gr-qc/9805037, section 2.1.2 'Squeezed States'",
   "effect": "contested",
   "what": "Would be the natural place for a restatement of (3.22)-(3.23) by Ford's group; the cached harvest holds only the table of contents for that section, so whether it restates (3.23) is unknown. Effect not determinable; listed so the gap is visible.",
   "read_status": "NAMED-NOT-READ (section body absent from cached text d67/src/casmag/all/gr-qc_9805037v1.txt)"
  }
 ],
 "lacked_data": "M's hypothesis does not bite on this result, and the evidence is the re-derivation: (3.18)-(3.23) are closed-form expectation values with no empirical input. Everything needed -- the commutator, KF's own (3.14)-(3.17), and the normal-ordering rule they state in (3.3)-(3.6) -- was in Kuo & Ford's hands in 1993, and their (3.18) and (3.22), derived from exactly those inputs, are exact (C1). The defect in (3.19)/(3.23) is algebraic (or typographical in v1), not a consequence of missing data: the print is non-covariant (C6) and inconsistent with itself (C9). Having more data would change nothing. Evidence either way on consequences: for the squeezed VACUUM the defect does not move KF's reading -- the exact Delta is 2/3 everywhere rho != 0 (C4), order unity on both sides of zero, so their statement survives there (and the tree's stronger reading, that Delta does not discriminate the sign, follows). For the squeezed COHERENT family the defect matters: KF's p.9 statement, built by 'numerical evaluation of Delta using Eqs. (3.2), (3.18), and (3.19)', says rho < 0 always carries Delta of order unity; with the exact (3.19) there is a curve inside rho < 0 where Delta = 0 exactly (C8), at the very parameters of their Figs. 1-2, where their printed formula gives 0.992. What KF lacked was a correct (3.19) and a closed-form check, not data. Whether PRD 47, 4510 prints corrected (3.19)/(3.23) is NAMED-NOT-READ.",
 "grade": "STANDS",
 "grade_evidence": "The tree's use of this key is four flags and one identity, scoped to arXiv v1: KF_318_IS_EXACT = True, KF_319_IS_EXACT = False, KF_322_IS_EXACT = True, KF_323_IS_EXACT = False (fluctuation.py:144-147), and 'For the squeezed vacuum the exact result is <:T00^2:> = 3 <:T00:>^2, IDENTICALLY' (fluctuation.py:43-44). All five are reproduced by an independent symbolic route (Weyl-algebra normal ordering) controlled by an independent 40-digit Fock-space route (C1-C4), agreeing with each other to 1e-15; the non-exactness of (3.19) is further shown structurally (U(1) non-covariance, C6) and the print is shown internally inconsistent ((3.19)|alpha=0 != (3.23), C9); four alternative conventions fail to rescue the print (C7), so the flags do not rest on a convention choice. The identity holds on a wider class than the tree assumes (any delta, C4). No hypothesis the tree drops moves a flag; no datum exists. The tree records these as discrepancies against v1, journal NAMED-NOT-READ -- the right weight under M's rule. Residual named hypotheses (bound, do not lower): (a) v1 text layer faithful (page image not viewed; this stage read the cached harvest because alphaXiv was over quota); (b) journal version unread; (c) the later-literature search did not run (quota). ONE FINDING ROUTED ELSEWHERE, not affecting this grade: the tree's KF_QUALITATIVE_CONCLUSION_SURVIVES = True with 'in every case they study' (fluctuation.py:62-64, 152) is contradicted for the squeezed coherent case by C8 (rho < 0, Delta = 0 exactly at r = 1/2, s^2 = (1-e^{-1})/8, theta = pi/2, gamma = delta = 0); that belongs to key gr-qc/9304008-qualitative-conclusion.",
 "what_would_change_the_grade": "To OPEN (for 3.19/3.23 only): the v1 page image or the journal version showing (3.19)/(3.23) in a form the text layer garbled -- but the fix would have to restore U(1) covariance to (3.19), change three coefficients of (3.23), and make the two consistent with each other, which no single glyph loss does. To a narrower scope (not a different grade): PRD 47, 4510 printing the exact forms -- the discrepancy would then be v1-only, as the tree already scopes it. Nothing computable moves the flags: (3.18)/(3.22) exactness and (3.19)/(3.23) non-exactness are identities checked two independent ways. A different definition of :T:, i.e. a change to (2.12)-(2.14), would move all four together, but (3.18) being exact under the tree's operator is itself evidence the operator matches KF's.",
 "reverify_command": "python3 " + D + "/rederive/gr-qc_9304008-eq3.18-3.23.py   # exits 0, 'ALL CHECKS PASS' (~2-4 min); source text: sed -n 975,1225p " + D + "/src/casmag/all/gr-qc_9304008v1.txt ; tree side: cd /home/user/Claude-Method-Works/research/warp-drive && python3 fluctuation.py --selftest | grep -E '\\(3\\.1[89]\\)|\\(3\\.2[23]\\)|3 rho'",
 "report_path": D + "/audits/gr-qc_9304008-eq3.18-3.23.json",
 "later_literature_search_note": "The one discover_papers call this stage made returned 'alphaXiv assistant quota exceeded'; later literature above is from texts cached earlier in this docket. No later paper restating KF (3.19) or (3.23) coefficients was found here, and absence of a finding is not a finding."
}
json.dump(R, open(D + "/audits/gr-qc_9304008-eq3.18-3.23.json", "w"), indent=1)
print("ok")
