import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
S = D + "/rederive/minkowski-plane-wave-mode-normalisation.py"
R = D + "/audits/minkowski-plane-wave-mode-normalisation.json"
rep = {
 "key": "minkowski-plane-wave-mode-normalisation",
 "name": "Minkowski scalar plane-wave modes U_k = e^{ik.x}/sqrt((2 pi)^n 2 w_k)",
 "source": {
  "located": "No single source: a textbook definition (canonical quantisation of the free Klein-Gordon field; e.g. Birrell & Davies, Quantum Fields in Curved Space, 1982, Sec. 2.1 -- book, no arXiv copy, NAMED-NOT-READ). The tree uses it as the Minkowski instance of Fewster & Teo, 'Bounds on negative energy densities in static space-times', arXiv:gr-qc/9812032v2 (Phys. Rev. D 59 (1999) 104016), eqs. (2.3) 'complete orthonormal set of positive-frequency solutions' and (3.1)/(3.2).",
  "read_status": "NAMED-NOT-READ",
  "via": "NOT READ AT SOURCE THIS STAGE. alphaXiv answer_pdf_queries(paper='gr-qc/9812032', 5 queries), get_paper_content(fullText) and discover_papers all returned 'alphaXiv assistant quota exceeded'; curl https://arxiv.org/abs/gr-qc/9812032 -> 'CONNECT tunnel failed, response 403' at the egress proxy. The only access to F&T's wording is the tree's OWN DOCKET 62 transcription (scratchpad/a1/o2.txt, keys 'bound_verbatim' and 'prefactor_rederived', which states it read gr-qc/9812032v2 at source and quotes (2.3), (2.10)-(2.13), (3.2) as '-(1/2) INT d^n k/(2 pi)^n w_k |fhat|^2' and U_k = e^{ik.x}/[(2pi)^n 2 w_k]^{1/2}). That is an internal transcription, not an independent read, so it is NOT counted as READ-VIA-RESTATEMENT. The grade below does NOT rest on it: the normalisation is fixed by computation (C1-C3), independent of any printed page."
 },
 "published_statement": "Not read at source this stage. Per the DOCKET 62 transcription (not re-read): F&T (2.3) 'f_lambda(t,x) = U_lambda(x) exp(-i omega_lambda t), a complete orthonormal set of positive-frequency solutions'; in Minkowski space (Sec. 3) U_k = e^{ik.x}/[(2pi)^n 2 w_k]^{1/2}, and (3.2) = -(1/2) INT d^n k/(2pi)^n w_k |fhat^{1/2}|^2 (dw measure as transcribed: INT_0^oo dw). Textbook content (computed here, not quoted): the unique normalisation making {U_k e^{-i w_k t}} Klein-Gordon-orthonormal to delta^n(k-k') and giving the canonical commutator [phi, pi] = i delta^n.",
 "published_hypotheses": [
  "flat Minkowski spacetime, n spatial dimensions, |g_tt| = 1 (ultrastatic)",
  "free real scalar, minimally coupled, mass mu >= 0, dispersion w_k = sqrt(k^2 + mu^2) > 0",
  "modes orthonormal in the Klein-Gordon inner product, continuum (delta^n(k-k')) normalisation with Lebesgue measure d^n k -- plane waves are not square-integrable, orthonormality is distributional",
  "completeness of the positive-frequency set; Fock vacuum built on it (static/Minkowski vacuum)",
  "IR: the Fock construction needs INT d^n k/(2 w_k) locally finite near k = 0, i.e. mu > 0 or n >= 2 (fails for massless n = 1)"
 ],
 "hypothesis_drift": [
  "NONE THAT MOVES A RESULT. Tree's 'standard Klein-Gordon normalisation with factor 2 w_k' (canonical.json; fewsterteo.py:27, 464) = the KG-orthonormal normalisation, computed here (C1).",
  "n: the tree's docstring and canonical hypotheses say n = 3 (fewsterteo.py:464 'n = 3 coordinates'), but prefactor_route2 carries n SYMBOLIC in the normalisation while differentiating in 3 coordinates (fewsterteo.py:467-472). Harmless: |U_k|^2 is x-independent for every n, and C1/C2/C4/C5 run with n symbolic. The IR hypothesis (mu > 0 or n >= 2) is not stated in the tree; it is satisfied at n = 3 and carries no weight there.",
  "Dispersion relation DROPPED in the tree's route 2: omega_k is a free positive symbol, w^2 = k^2 + mu^2 never imposed (fewsterteo.py:468). Harmless for route 2 (grad^2|U_k|^2 = 0 whatever w is), but the direct (2.10) -> (3.2) check (C4 here) needs it; with it, norm = 2 is forced independently of (2.12).",
  "Distributional (delta) normalisation is left implicit in the tree (fewsterteo.py:27-28, 464); F&T's 'orthonormal' (2.3, per transcription) is the same convention. Label-convention independence: SUM_lambda |U_lambda|^2 is the coincidence Wightman function, fixed by completeness + KG orthonormality whatever labelling F&T use (C3 matches the Hadamard coefficient 1/(4 pi^2 sigma)), so the combination route 2 feeds into (2.12) cannot depend on F&T's labelling convention.",
  "DISCREPANCY IN THE TRANSCRIPTION CHAIN (recorded, not repaired, and NOT a finding against F&T): the DOCKET 62 transcription of (2.10) reads '-(1/2) INT_0^inf dw ...' and of (5.6) '-(1/(16 pi^3)) INT u^4 |fhat^{1/2}|^2'. With these modes, the transcribed (3.2) reduces (massless, n = 3) to -(1/(16 pi^2)) INT u^4 |fhat^{1/2}|^2 (C6a) -- one factor pi from the transcribed (5.6). The 1/(16 pi^3) form is the one that gives the tree's 9/64 against Ford-Roman's -3/(32 pi^2 t0^4) (C6b); 1/(16 pi^2) would give 9 pi/64 (C6c). So a 1/pi (e.g. INT dw/pi, or an fhat convention) is missing from the transcribed (2.10)/(3.2), not from the modes. fewsterteo.py:30-31 prints (3.2) without its dw measure, so the tree file itself does not display the inconsistency. It is common to (2.12) and (3.2), so route 2's P (a ratio) is immune, and route 1 (ratio of (2.10) to (2.12) brackets) is immune. Must not be quoted as an error of F&T until (2.10)/(3.2) are read at source."
 ],
 "data_at_publication": [
  {"quantity": "none -- a definition in natural units (hbar = c = 1); no measured input enters the normalisation",
   "value_then": "n/a", "value_now": "n/a", "source_now": "n/a",
   "moves_conclusion": "no -- no datum exists to move"},
  {"quantity": "tree's control datum: route 2 with norm = 1 (drop the 2)",
   "value_then": "P = 1/2 (fewsterteo.py:33, 393-395)",
   "value_now": "P = 1/2 reproduced (C5); P = 1 at norm = 2 reproduced",
   "source_now": "rederive/minkowski-plane-wave-mode-normalisation.py C5",
   "moves_conclusion": "no -- and the control is a GENUINELY wrong normalisation, not merely another convention: at norm = 1 the KG norm is 2 delta (C1), the commutator 2i delta (C2), the Wightman coefficient 1/(2 pi^2 eps^2), twice Hadamard (C3)"}
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": S,
  "outcome": "14/14 PASS, exit 0. C1: KG inner product coefficient of delta^n(k-k') = 1 at norm 2, 2 at norm 1 (n symbolic). C2: [phi,pi] coefficient = i at norm 2, 2i at norm 1. C3: n=3 massless coincidence Wightman INT d^3k |U_k|^2 e^{-k eps} = 1/(4 pi^2 eps^2) (Hadamard) at norm 2, 1/(2 pi^2 eps^2) at norm 1. C4: F&T (2.10) bracket (as transcribed) on plane waves with w^2 = k^2 + mu^2 gives -(1/2) w/(2pi)^n = the transcribed (3.2) density at norm 2 WITHOUT using (2.12); norm 1 gives -w/(2pi)^n. C5: tree's route 2 reproduced, P = 1 (norm 2), 1/2 (norm 1). C6: transcription-chain constant probe -- (3.2) as transcribed -> 1/(16 pi^2) vs transcribed (5.6) 1/(16 pi^3); only the latter gives 9/64 vs Ford-Roman (exact rationals; INT v^4 K0^2 = 27 pi^2/512 confirmed by mpmath quadrature to 1e-15).",
  "agrees_with_source": "partly"
 },
 "later_literature": [
  {"ref": "discover_papers (keywords 'quantum inequalities', 'static spacetimes', 'mode functions')",
   "effect": "contested",
   "what": "NOT RUN: 'alphaXiv assistant quota exceeded'. No later literature was read this stage. 'contested' is the schema's nearest slot and here means ONLY 'not established either way'; no paper is known to contest the normalisation.",
   "read_status": "NOT-READ (tool refused)"},
  {"ref": "Birrell & Davies, Quantum Fields in Curved Space (CUP 1982), Sec. 2.1",
   "effect": "confirms",
   "what": "Standard statement of plane-wave KG normalisation u_k = [2 w (2pi)^{n}]^{-1/2} e^{i(k.x - w t)} for n spatial dimensions (their index convention counts spacetime dimensions). Named from knowledge, not read this stage; the grade does not rest on it -- C1-C3 compute the same thing.",
   "read_status": "NAMED-NOT-READ"},
  {"ref": "Ford & Roman, gr-qc/9410043 (flat massless QI, Lorentzian sampler, -3/(32 pi^2 t0^4))",
   "effect": "confirms",
   "what": "Used only as the external fixed point of C6: with the transcribed (5.6) constant 1/(16 pi^3), F&T's flat bound is 9/64 of it, as the tree states; this locates the transcription's missing 1/pi outside the mode normalisation. Value named from the tree's own usage, not re-read this stage.",
   "read_status": "NAMED-NOT-READ"}
 ],
 "lacked_data": "M's hypothesis does not bite here, by the nature of the result: the normalisation is a definition fixed by algebra (Klein-Gordon orthonormality and the canonical commutator), with no empirical input -- there is no datum F&T (1999) or the textbooks could have lacked. Evidence FOR its correctness is computed (C1-C3: the factor 2 w_k is forced; its absence doubles the KG norm, the commutator and the Wightman/Hadamard coefficient). Evidence that could have cut against it: a labelling-convention mismatch between the tree's plane waves and F&T's own modes -- excluded, because the combination entering (2.12) is the Wightman function, convention-independent (C3). The only live defect found is in the tree's DOCKET 62 TRANSCRIPTION of F&T's absolute constants (a missing 1/pi between transcribed (2.10)/(3.2) and (5.6)), which is not data, does not touch the modes, and cancels in both prefactor routes.",
 "grade": "STANDS",
 "grade_evidence": "As the tree uses it (fewsterteo.py:27-33, 456-477; hypotheses 'standard KG normalisation with factor 2 w_k', 'n = 3'), the definition is correct and was computed, not quoted: sympy shows U_k e^{-i w t} with 1/sqrt((2pi)^n 2 w_k) is KG-orthonormal to delta^n(k-k') for symbolic n (C1), reproduces [phi,pi] = i delta^n (C2), and gives the Hadamard coincidence coefficient 1/(4 pi^2 eps^2) at n = 3 (C3). The tree's use -- |U_k|^2 constant, grad^2|U_k|^2 = 0, route 2 P = 1, control norm = 1 -> P = 1/2 -- is reproduced (C5), and a third route not in the tree ((2.10) directly -> (3.2), C4) independently requires the factor 2. No datum enters. LIMITS, named: (i) F&T's printed (2.3)/(3.1)/(3.2) were NOT read at source this stage (alphaXiv quota, arXiv 403), so 'this is F&T's own normalisation' rests on the DOCKET 62 transcription -- but C3 makes the combination route 2 uses independent of F&T's labelling, so the grade does not need it; (ii) the transcription chain is internally off by one factor pi in its absolute constants (C6), recorded as a discrepancy in the tree's transcription, not as an error of F&T, immune for P; (iii) the IR hypothesis (mu > 0 or n >= 2) is unstated in the tree and satisfied at n = 3.",
 "what_would_change_the_grade": "To NARROWED: a reading of F&T gr-qc/9812032 showing their (2.3) 'orthonormal' is NOT Klein-Gordon/delta-normalised in a way that changes SUM_lambda |U_lambda|^2 (impossible for a complete KG-orthonormal set per C3, so this would mean F&T's modes are normalised to something else and their (2.10) prefactor compensates -- then route 2 would still be consistent but the tree's gloss would be the drift), or the tree applying these modes at n = 1 with mu = 0. To WRONG: none available for the definition itself -- C1-C3 are identities. The C6 pi discrepancy would move to a finding only if a source read shows F&T print (2.10)/(3.2) with INT_0^oo dw and no 1/pi AND (5.6) with 1/(16 pi^3) -- then it is F&T's internal misprint (a discrepancy, still not a refutation, and still immune for P).",
 "reverify_command": "python3 " + S + "   # expect 14/14 PASS, exit 0; tree side (read-only): cd /home/user/Claude-Method-Works/research/warp-drive && sed -n 456,477p fewsterteo.py && sed -n 388,396p fewsterteo.py; when alphaXiv quota returns: answer_pdf_queries(paper='gr-qc/9812032', queries=['exact (2.3) orthonormality convention', 'exact (2.10) prefactor and dw measure incl. any 1/pi', 'exact (3.1)/(3.2) Minkowski modes and bound', 'exact (5.6) constant'])",
 "report_path": R
}
json.dump(rep, open(R, "w"), indent=1)
print(R)
