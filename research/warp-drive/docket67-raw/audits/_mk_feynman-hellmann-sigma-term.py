import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "feynman-hellmann-sigma-term",
 "name": "Feynman-Hellmann theorem and dimensional homogeneity m_p = Lambda f(m_q/Lambda) giving d ln m_p/d ln Lambda = 1 - S (and its H1/H2 compositions 2/9 + 7S/9, S; K_mu = f - 1)",
 "source": {
  "located": "The tree cites no paper for this step (address.py:99-104: 'by dimensional homogeneity ... the Feynman-Hellmann light-quark fraction'). Located: (i) the QCD form of Feynman-Hellmann, FLAG Review 2024, arXiv:2411.04268v3, Sec.10.4, eqs.(431)-(433) p.260, p.261, eq.(446) p.270; (ii) the published form of the homogeneity step with a numerical S, Coc, Nunes, Olive, Uzan, Vangioni, astro-ph/0610733v2 (PRD 76, 023511, 2007) eq.(11) and the remark 'we have repaired the mass dimension by adding the appropriate powers of Delta Lambda/Lambda' (before eq.(12)), with eqs.(13)-(14) for the heavy thresholds; (iii) the H1 combination in print, Hoferichter, Ruiz de Elvira, Kubis, Meissner, arXiv:1506.04142v2 eq.(24); (iv) the beyond-LO heavy-quark series, Hill & Solon arXiv:1409.8290v1 eq.(39), (61), (62); (v) the H2 limit, Flambaum arXiv:0705.3704v2 p.4 'M_p ~ 3 Lambda_QCD'; (vi) current full-theory breakdown, Hoferichter & Ruiz de Elvira arXiv:2506.23902v2 eq.(35). Hellmann (1937) and Feynman (Phys. Rev. 56, 340, 1939): NAMED-NOT-READ, READ-VIA-RESTATEMENT through FLAG p.260 ('This relationship is given by the Feynman-Hellmann theorem') and machine-checked here (check B). SVZ 1978: NAMED-NOT-READ (restated by Hill-Solon eq.(101), sibling audit svz-1978).",
  "read_status": "READ",
  "via": "Live alphaXiv refused in THIS stage (answer_pdf_queries x2, get_paper_content, discover_papers: 'alphaXiv assistant quota exceeded', 2026-09-26) and arxiv.org / export.arxiv.org / alphaxiv.org return CONNECT 403 from the proxy (curl probe this stage). The sources were therefore READ from verbatim arXiv full-text extractions harvested earlier in this docket into scratchpad/d67/src/casmag/all/ (1506.04142v2.txt, 2411.04268v3.txt, astro-ph_0610733v2.txt, 0705.3704v2.txt, 1409.8290v1.txt, 2506.23902v2.txt; each carries its arXiv stamp line). The passages quoted below were read from those files in this stage; the classics are READ-VIA-RESTATEMENT only."
 },
 "published_statement": "FLAG 2024 (2411.04268v3 p.260): 'The matrix elements of the scalar operator qq with flavour q give the rate of change in the nucleon mass due to nonzero values of the corresponding quark mass. This relationship is given by the Feynman-Hellmann theorem ... sigma_piN = m_ud <N|uu + dd|N> (431), sigma_s = m_s <N|ss|N> (432), sigma_c = m_c <N|cc|N> (433)'; p.261: 'The sigma_piN,s,c give the shift in M_N due to nonzero light-, strange- and charm-quark masses'; eq.(446): sigma_piN = m_ud dM_N/dm_ud ~ M_pi^2 dM_N/dM_pi^2, sigma_s = m_s dM_N/dm_s. Coc et al. 2007 (astro-ph/0610733v2 p.4): with the strange content from B_s = 1.5 (Sigma ~ 51 MeV) 'Delta m_N/m_N = (m_s B_s/m_N) Delta m_s/m_s ~ 0.19 Delta m_s/m_s' and 'for the light quark (u and d) contributions ... Delta m_N/m_N ~ 0.052 Delta m_q/m_q. This implies that Delta m_p/m_p ~ 0.76 Delta Lambda/Lambda + 0.24 (Delta h/h + Delta v/v) (11)' -- i.e. d ln m_p/d ln Lambda = 1 - S with S = 0.24; eq.(13) 'Lambda = mu (m_c m_b m_t/mu^3)^(2/27) exp(-2 pi/(9 alpha_s(mu))) for mu > m_t up to some unification scale in the standard model', eq.(14) 'Delta Lambda/Lambda = R Delta alpha/alpha + (2/27)(3 Delta v/v + Delta h_c/h_c + Delta h_b/h_b + Delta h_t/h_t)'. Hoferichter et al. 2015 (1506.04142v2 eq.(24)): 'sum_{q=u,...,t} f_q^N = 2/9 + 7/9 (f_u^N + f_d^N + f_s^N) = 0.305 +- 0.009', with m_N f_q^N = <N|m_q qq|N> (eq.(22)) and f_s from lattice. Flambaum 2007 (0705.3704v2 p.4): 'The proton mass is proportional to Lambda_QCD (M_p ~ 3 Lambda_QCD)'. Hill-Solon (1409.8290v1 eq.(39)): the heavy-quark matrix element is a series in alpha_s^(nf+1)(mu_Q)/pi whose O(alpha_s^0) term is (1/(3 beta_0))(2 - 2 lambda), 'lambda = sum_{q=u,d,s,...} <O_q>/m_N ... the sum of light quark scalar matrix elements in the n_f-flavor theory'; p.15: 'Due to the lightness of the charm quark, and correspondingly poorly convergent alpha_s(m_c) expansion ...'.",
 "published_hypotheses": [
  "FH-1 (theorem): an isolated, non-degenerate eigenvalue of a Hermitian H(lambda) with a normalised eigenstate; the nucleon is the lowest state in its channel (FLAG's use; machine-checked here, check B).",
  "FH-2 (FLAG eq.(446)): sigma_q is a FIRST-ORDER derivative at the physical point, m_q dM_N/dm_q; renormalized operators ('all operators are assumed to be appropriately renormalized', FLAG p.260); m_q qq is RG invariant so sigma_q is scheme-independent.",
  "HOM-1 (Coc eq.(11)-(12)): QCD only -- the nucleon mass is a function of Lambda and the quark masses alone, the mass dimension 'repaired' by powers of Lambda; QED and weak contributions to m_p not included.",
  "HOM-2 (implicit in any homogeneity statement; derived here, check C): the quark masses held fixed while Lambda varies are RG-invariant masses (or MSbar masses at a scale proportional to Lambda); at fixed m_q(mu0) with mu0 fixed in GeV the coefficient is 1 - S(1 + gamma_m(mu0)).",
  "HOM-3 (Coc eq.(11), Hoferichter eq.(24), Hill-Solon's lambda): the light set is the flavours of the theory whose scale is Lambda -- u, d, s for Lambda_3 -- so S = (sigma_piN + sigma_s)/m_N.",
  "H1-1 (Coc eq.(13)-(14), Hoferichter eq.(24), SVZ via Hill-Solon eq.(39)): one-loop running with continuous LO matching at each heavy threshold; heavy-quark limit for c, b, t; Standard-Model coloured content between m_t and the high scale (Coc footnote 1: 'In supersymmetric models, additional thresholds ... would affect this relation').",
  "H1-2 (Coc eq.(14)): masses m_Q = h_Q v at fixed Yukawa; the tree's H1 is Coc's Delta alpha = 0, Delta h = 0 (no GUT R-term).",
  "H2 (Flambaum p.4): Lambda_QCD fixed and M_p proportional to it -- Flambaum states it with S -> 0 (M_p ~ 3 Lambda); the tree keeps S."
 ],
 "hypothesis_drift": [
  "NOT A DRIFT (checked, exact): the Euler/homogeneity step d ln m_p/d ln Lambda = 1 - S with S = sum sigma_q/m_p (address.py:99-101) is exactly Coc eq.(11)'s structure (coefficients sum to 1: 0.76 + 0.24) and follows for a generic f (sympy, check A); FH is FLAG's definition (eqs.(431)-(433),(446)) and is machine-checked for an isolated level (check B). The tree's code (address.py:504-515) implements exactly (2/9)(1 - S) + S and S (check D, address.py functions called).",
  "DROPPED (order of the H1 evaluation): address.py:99-104 and higgs_fraction (address.py:816-822) present 2/9 + (7/9) S as the value of d ln m_p/d ln v under H1 with no 'leading order' qualifier; the qualifier 'One-loop' appears only at address.py:88. The exact H1 statement is d ln m_p/d ln v = sum_{q=u..t} f_q (full-theory Euler with Lambda_6 fixed, every MSbar mass proportional to v; sympy check D) -- Hoferichter eq.(24)'s left side -- and 2/9 + 7S/9 is its SVZ-LO evaluation. Beyond LO (Hill-Solon through O(alpha_s^3), sibling transcription re-run here) f(S = 0.06) = 0.28177 not 0.26889 (+4.8%), and the (1 - S) factorisation fails at the 2% level. Shared with sibling audit dlnlambdaqcd-dlnv-2-9 (same drop at address.py:97, 498-500).",
  "DROPPED (HOM-2, unstated but satisfied): 'm_p = Lambda f(m_q/Lambda)' (address.py:100) does not say which quark mass is held fixed. Computed (sympy, check C): at fixed RG-invariant mass the coefficient is 1 - S; at fixed m_q(2 GeV) it is 1 - S(1 + gamma_m) = 0.9285 vs 0.9400 at S = 0.06 (LO gamma_m ~ 0.19 at alpha_s(2 GeV) ~ 0.30, NAMED-NOT-READ). The tree never holds m_q(2 GeV) fixed while moving Lambda -- in H1 every MSbar mass moves with v at fixed high-scale Yukawa, which is the full-theory identity above, and in H2 Lambda does not move -- so the hypothesis is satisfied in use; its O(S alpha_s) residue sits inside the beyond-LO correction already counted.",
  "DROPPED (HOM-1, QCD only): m_p = Lambda f(m_q/Lambda) (address.py:100) omits the electromagnetic part of m_p. Its size is O(1 MeV) ~ 1e-3 of m_p (NAMED-NOT-READ in this stage); its v-dependence enters only through K_alpha, which the tree carries separately (W11). Negligible against every number the tree prints (4 significant figures of K_mu move at most in the 4th).",
  "DRIFT IN USE (HOM-3, cross-reference, not re-litigated): the tree's own definition S = sum_q sigma_q/m_p over the light flavours of Lambda_3 requires u + d + s (HOM-3; Coc's 0.24 and Hoferichter's f_u + f_d + f_s both include strange), but the adopted S_MID = 0.06 is labelled 'sigma_piN ~ 56 MeV' (address.py:452) and is u + d only. Recorded in full by sibling audit sigma-term-scan; the definition at address.py:101, 505 is correct, the value fed to it is the drift.",
  "DISCREPANCY OF PRESENTATION (not an error): address.py:106 prints 'H1 gives 0.229 at S = 0.0096'; 2/9 + 7(0.0096)/9 = 0.22969, which rounds to 0.230 and truncates to 0.229 (check D). The same line's 'TWENTY-FOUR TIMES' (23.93 at 0.0096; 23.97 at the code's valence 0.009581) is correct to the figures printed.",
  "NOT A DRIFT (checked): the tree keeps H1 and H2 both and refuses to choose (address.py:108-110, H1_VS_H2_IS_REFUSED); H2 as the tree writes it (d ln m_p/d ln v = S) is strictly more complete than its cited source's form M_p ~ 3 Lambda (Flambaum p.4, which sets S -> 0). The status 'S is a SCAN, not a measurement' (address.py:336-338, 449-450) matches the sources' spread."
 ],
 "data_at_publication": [
  {
   "quantity": "S = light-quark sigma-term fraction as used by the published homogeneity statement (Coc 2007 eq.(11))",
   "value_then": "0.24 = 0.19 (strange, from B_s = 1.5, Sigma ~ 51 MeV and octet-mass sigma_0 = 36(7) MeV) + 0.052 (u, d); published coefficient of Delta Lambda/Lambda 0.76",
   "value_now": "S_uds = 0.0928 (FLAG 2024 Nf=2+1: 42.2 + 44.9 MeV), 0.1086 (Nf=2+1+1: 60.9 + 41.0), 0.1108 (pheno 59.1 + 44.9), 0.1064 (Hoferichter eq.(24) inverted); coefficient 0.89-0.91",
   "source_now": "FLAG 2024 arXiv:2411.04268v3 eqs.(447)-(450) (values as READ by sibling sigma-term-scan and in the cached text); Hoferichter 1506.04142v2 eq.(24); arithmetic in rederive check E",
   "moves_conclusion": "Moves Coc's NUMBER by a factor 2.2-2.6 in S (the 1990s-2000s strange content was large; lattice sigma_s is ~41-45 MeV), not the structure. For the tree: K_mu(H1) = -0.591 at Coc's 0.24 vs -0.693 at 0.1086; H2 -0.760 vs -0.891. Sign and O(1) unchanged; the tree does not use Coc's number."
  },
  {
   "quantity": "S fed to the tree's formula (address.py S_SCAN: 0.00958, 0.06, 0.09)",
   "value_then": "S_MID = 0.06 labelled 'sigma_piN ~ 56 MeV' (u + d only)",
   "value_now": "S_uds 0.093-0.111 (row above)",
   "source_now": "as above; full treatment in sibling audit sigma-term-scan",
   "moves_conclusion": "Numerics only (K_mu H1 -0.7311 -> -0.6916 at 0.1108); no sign or order conclusion moves, and the tree declares S a scan."
  },
  {
   "quantity": "Heavy-quark part of d ln m_p/d ln v under H1 (sum_{c,b,t} f_Q)",
   "value_then": "2/9 (1 - S) at LO (SVZ; one-loop matching): 0.20889 at S = 0.06",
   "value_now": "0.22177 at S = 0.06 through O(alpha_s^3) (Hill-Solon eq.(39) series, alpha_s(M_Z) = 0.1180 and PDG masses NAMED-NOT-READ), stable +6.04..+6.29% over the input scan; independent current breakdown Hoferichter & Ruiz de Elvira 2506.23902v2 eq.(35) sigma_c,b,t = 68 + 65 + 63 MeV (21% of m_N, 'perturbative input for sigma_c')",
   "source_now": "arXiv:1409.8290v1 eq.(39),(61); arXiv:2506.23902v2 eq.(35) p.7 (read from cached text this stage); sibling rederive/dlnlambdaqcd-dlnv-2-9.py re-run inside this stage's script",
   "moves_conclusion": "Computed with address.py's own functions: higgs_fraction H1 x1.048 (0.2689 -> 0.2818), K_mu H1 x0.982 (-0.7311 -> -0.7182), eps_det_stationary H1 x1.018, EPS_NUCLEAR H1 x1.048, EPS_NUCLEAR_OVER_DET H1 398 -> 410, COURIER_SOURCE_KG_M3 H1 x0.954, NAIVE_CORRECTION_FACTOR 23.97 -> 25.60 / 4.48 -> 4.70 / 3.25 -> 3.37. No sign flips; no conclusion moves."
  },
  {
   "quantity": "gamma_m(2 GeV) (enters only if a fixed-scale MSbar mass were held fixed; check C)",
   "value_then": "not used by the tree",
   "value_now": "LO 2 alpha_s/pi ~ 0.19 at alpha_s(2 GeV) ~ 0.30 (NAMED-NOT-READ)",
   "source_now": "textbook LO anomalous dimension; not read at source in this stage",
   "moves_conclusion": "No: the tree's use holds RG-invariant / high-scale-Yukawa masses; the coefficient shift 0.0115 at S = 0.06 would be absorbed into the beyond-LO correction."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/feynman-hellmann-sigma-term.py",
  "outcome": "0 failures, exit 0 (output rederive/feynman-hellmann-sigma-term.out). A: Euler residual Lambda dm_p/dLambda + sum m_q dm_p/dm_q - m_p = 0 for generic f of three ratios, so d ln m_p/d ln Lambda = 1 - S exactly. B: FH dE0/dlambda = <psi0|dH/dlambda|psi0> exact for an isolated level of a 2x2 Hermitian family. C: at fixed m_q(mu0) the coefficient is 1 - S(1 + gamma_m(mu0)) (sympy, generic f and running) -- the unstated which-mass hypothesis; 0.9285 vs 0.9400 at S = 0.06. D: one-loop matching Lambda_3 = Lambda_6^(7/9)(m_c m_b m_t)^(2/27), d ln Lambda_3/d ln v = 2/9, (2/9)(1-S) + S = 2/9 + 7S/9; SVZ-LO route gives the same; full-theory Euler gives d ln m_p/d ln v = sum_{u..t} sigma_q/m_p exactly; Hoferichter's 0.305 inverts to S_uds = 0.1064; every printed tree number reproduced (0.26889, K_mu -0.7703/-0.9904/-0.7311/-0.9400, F6 4.48/3.25, 'twenty-four') except '0.229', which is the truncation of 0.22969 (rounds to 0.230); address.py's dln_lambda_dln_v, dln_mp_dln_v and K_mu called and agree to 1e-15. E: Coc eq.(11) 0.76 + 0.24 = 1; 0.19 + 0.052 = 0.242; today's S_uds 0.093-0.111 gives 0.89-0.91. F: K_mu < 0 under H1 and H2 exactly on S < 1; |K_H2/K_H1| = 9/7 identically. G: beyond LO, every rests_on_it quantity moves < 5% (NAIVE at the valence row 6.8%), no sign flip, EPS_NUCLEAR_OVER_DET H1 = 410 > 100.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "R.J. Hill, M.P. Solon, arXiv:1409.8290 (PRD 91, 043505, 2015), eqs.(39), (61), (62), (101)",
   "effect": "narrows",
   "what": "Heavy-quark scalar matrix elements through O(alpha_s^3): the H1 value 2/9 + 7S/9 is the O(alpha_s^0) term; the full series gives +6.2% on the heavy sum and +4.8% on f at S = 0.06, breaks the (1 - S) factorisation, and flags charm as 'poorly convergent' with O(1/m_c) not estimated.",
   "read_status": "READ from cached arXiv text (eq.(39) p.18 and p.15 in this stage); series transcription from sibling audit dlnlambdaqcd-dlnv-2-9, re-run and checked against eqs.(120),(61)"
  },
  {
   "ref": "M. Hoferichter, J. Ruiz de Elvira, arXiv:2506.23902v2 (2025), eq.(35) p.7",
   "effect": "confirms",
   "what": "Full six-flavour decomposition m_N ~ (69 + 43 + 68 + 65 + 63 + 630) MeV; 'about 21% can be identified with the heavy quarks'; heavy sigma terms from 'perturbative input'. LO SVZ gives 3 x (2/27)(1 - S) = 19.8% at S = 0.109; the Hill-Solon series ~21% -- consistent, and the quark total 0.33 keeps sum f < 1, so K_mu < 0 beyond LO.",
   "read_status": "READ (cached arXiv text, this stage)"
  },
  {
   "ref": "FLAG Review 2024, Y. Aoki et al., arXiv:2411.04268v3, Sec.10.4.4",
   "effect": "contested",
   "what": "Lattice sigma_piN averages 42.2(2.4) (2+1) and 60.9(6.5) (2+1+1) MeV in 2.7 sigma tension with each other and ~3 sigma with phenomenology; sigma_s 41.0-44.9 MeV. The theorem is untouched; the datum S it feeds is contested (moves numbers, not conclusions).",
   "read_status": "READ (cached arXiv text: definitions pp.260-261, 270 in this stage; averages as READ by sibling sigma-term-scan)"
  },
  {
   "ref": "A. Coc et al., astro-ph/0610733 (2007), eq.(11)",
   "effect": "confirms",
   "what": "The published form of the homogeneity step (0.76 Delta Lambda/Lambda + 0.24 Delta m_q/m_q); its 0.24 predates lattice sigma_s and is 2.2-2.6x today's S_uds -- the structure stands, the number moved.",
   "read_status": "READ (cached arXiv text, this stage)"
  },
  {
   "ref": "Hoferichter et al., PLB 843 (2023) 138001, arXiv:2305.07045 (isospin-convention shift of sigma_piN by 3.1(5) MeV)",
   "effect": "narrows",
   "what": "Convention for sigma_piN (charged vs neutral pion isospin limit); moves S by 0.0033.",
   "read_status": "NAMED-NOT-READ (restated by 2609.05989 per sibling sigma-term-scan). The one discover_papers call of this stage was refused on quota, so no new later literature was surfaced here."
  }
 ],
 "lacked_data": "The theorem itself (Feynman-Hellmann) and the homogeneity identity lack no data: they are exact identities (checks A, B, D) and no datum can move them. What the authors of the PUBLISHED numerical forms lacked: Coc et al. (2007) lacked lattice strange sigma terms and used B_s = 1.5 (strange 0.19 of m_N), giving S = 0.24; today's S_uds is 0.093-0.111 (FLAG 2024), so their coefficient 0.76 becomes 0.89-0.91 -- the datum moved by a factor 2.2-2.6, confirming M's hypothesis in its weak form for this published number. SVZ (1978) and the one-loop matching behind 2/9 lacked the O(alpha_s^1..3) decoupling coefficients (Chetyrkin-Kniehl-Steinhauser 1997, NAMED-NOT-READ) and the Hill-Solon series (2014): having them moves the H1 value by +4.8% at S = 0.06. Flambaum's M_p ~ 3 Lambda (H2 limit) lacked nothing the tree needs; the tree already carries S. EVIDENCE EITHER WAY on whether the new data change the conclusion: computed with address.py's own functions, no rests_on_it quantity changes sign, every one moves < 5% (NAIVE at the valence row 6.8%), and K_mu < 0 holds exactly for S < 1 at LO and for sum_{u..t} f_q < 1 beyond LO (current value ~0.32-0.33). So the new data NARROW the H1 formula's exactness (LO) and move the published S, but refute nothing and move no conclusion. M's hypothesis in its strong form (an established result is wrong because data were lacking) is NOT supported for this result.",
 "grade": "NARROWED",
 "grade_evidence": "The core -- Feynman-Hellmann plus dimensional homogeneity, d ln m_p/d ln Lambda = 1 - S -- is an exact identity under its hypotheses (QCD only, isolated level, RG-invariant masses held fixed) and is machine-checked here (sympy A, B), matching FLAG 2024's definition (eqs.(431)-(433),(446)) and Coc et al. 2007 eq.(11) read at source (cached arXiv text). The tree's H1/H2 compositions and every printed number are reproduced, and address.py's own functions agree (D). It is graded NARROWED, not STANDS, because the statement as used carries hypotheses the tree does not name: (1) the H1 value 2/9 + 7S/9 is the leading-order evaluation of the exact d ln m_p/d ln v = sum_{u..t} f_q (Hoferichter eq.(24)'s left side); beyond LO it is 0.28177 vs 0.26889 at S = 0.06 and the (1 - S) factorisation fails at 2% (address.py:99-104, 816-822 carry no LO qualifier; shared with sibling dlnlambdaqcd-dlnv-2-9); (2) QCD-only (EM part of m_p, ~1e-3, dropped at address.py:100); (3) which quark mass is held fixed (at fixed m_q(2 GeV) the coefficient is 1 - S(1+gamma_m), check C) -- unstated but satisfied in the tree's use. It is not WRONG: no counterexample exists; the LO value is correct LO. It is not DATA-DEPENDENT: the identity uses no datum, and the contested datum S (and the beyond-LO shift) moves numbers only -- K_mu < 0 exactly for S < 1 under both hypotheses, |K_H2/K_H1| = 9/7 identically, and no rests_on_it quantity changes sign or moves > 7%. Discrepancies recorded, not repaired: '0.229' at address.py:106 is the truncation of 0.22969; the adopted S_MID = 0.06 omits sigma_s against the tree's own u+d+s definition (sibling sigma-term-scan).",
 "what_would_change_the_grade": "To STANDS: the tree names the LO qualifier on 2/9 + 7S/9 (or carries the beyond-LO sum_{u..t} f_q) and the QCD-only / RG-invariant-mass hypotheses beside 'm_p = Lambda f(m_q/Lambda)'. To DATA-DEPENDENT: a conclusion that turned on S or on the beyond-LO shift -- none does over S in [0, 1) at LO or at any sum f_q < 1. To WRONG: a sum_{u..t} f_q >= 1 (would flip K_mu's sign) or a failure of Feynman-Hellmann for the nucleon (a degenerate or non-isolated level) -- neither exists in any source read. To OPEN: none; every step is closed-form and checked here.",
 "reverify_command": "python3 -B " + D + "/rederive/feynman-hellmann-sigma-term.py; grep -n 'This implies that' -A3 " + D + "/src/casmag/all/astro-ph_0610733v2.txt; grep -n '(24)' -B12 " + D + "/src/casmag/all/1506.04142v2.txt; sed -n 1215,1245p " + D + "/src/casmag/all/2411.04268v3.txt",
 "report_path": D + "/audits/feynman-hellmann-sigma-term.json"
}
json.dump(R, open(R["report_path"], "w"), indent=1)
print("ok", len(json.dumps(R)))
