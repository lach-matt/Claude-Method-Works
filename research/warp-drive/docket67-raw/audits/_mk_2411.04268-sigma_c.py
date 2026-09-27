import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "2411.04268-sigma_c",
 "name": "FLAG 2024 charm sigma term (ETM 19, sigma_c = 107(22) MeV)",
 "source": {
  "located": "FLAG Review 2024, arXiv:2411.04268 (v3 per the tree), Sec. 10.4.4, p.275 per massform.py:1339; the primary measurement is ETM 19 (FLAG ref. [983]); the tree also carries RQCD 16 (FLAG ref. [870]).",
  "read_status": "NAMED-NOT-READ",
  "via": "NOT read at source in this pass. alphaXiv answer_pdf_queries(2411.04268), get_paper_content(fullText=true) and discover_papers all returned 'alphaXiv assistant quota exceeded' (three attempts, 2026-09-26); arxiv.org, export.arxiv.org, www.alphaxiv.org and api.semanticscholar.org are refused by the egress proxy (curl CONNECT 403; WebFetch EGRESS_BLOCKED). No held copy of FLAG page text exists in the scratchpad (searched d67/, d65*/). The only text available is the tree's OWN held quote, massform.py:1339-1343 (DOCKET 65's read), which is the thing under audit and so is not independent evidence. ETM 19 itself (the primary measurement) was not read either."
 },
 "published_statement": "NOT READ THIS PASS. As held by the tree (massform.py:1339-1343, attributed to FLAG 2024 v3 Sec. 10.4.4 p.275): 'the RQCD 16 N_f = 2 analysis of Ref. [870] that reports f_Tc = 0.075(4) or sigma_c = 70(4) MeV, is consistent with the direct determinations of ETM 19 [983] for N_f = 2 + 1 + 1 of sigma_c = 107(22) MeV'. Definition as held (FLAG-def, massform.py:1352-1355, p.261): 'The sigma_piN,s,c give the shift in M_N due to nonzero light-, strange- and charm-quark masses.'",
 "published_hypotheses": [
  "As held (not re-read): sigma_c = m_c <N|c-bar c|N>, a Feynman-Hellmann first-order shift of M_N with m_c (FLAG-def, Eqs. (431)-(433) p.260 per the tree)",
  "As held: ETM 19 value is a direct lattice determination with N_f = 2 + 1 + 1 dynamical flavours",
  "As held: FLAG QUOTES the ETM 19 and RQCD 16 values in a consistency sentence; whether FLAG forms an average or estimate for sigma_c was not verified this pass (the held quote shows none)",
  "RQCD 16 is N_f = 2 (no dynamical strange or charm), so its sigma_c comes from a different sea content than ETM 19's",
  "Quoted uncertainty 22 MeV (20.6 %) on ETM 19; the lattice systematics behind it (lattice spacings, continuum extrapolation, excited states, disconnected-diagram treatment) were NOT read this pass"
 ],
 "hypothesis_drift": [
  "UNCERTAINTY DROPPED (acknowledged by the owner): the tree uses the central 107 only -- SIGMA_C_ETM19 = 107.0 (massform.py:1461) -- and says so for all C2 readings: 'It is a largest central value, not a bound: uncertainties are dropped' (massform.py:371-372). Not hidden; recorded as drift from '107(22)'.",
  "'UP TO' / 'largest printed' (massform.py:353, 1461): the tree selects the larger of the two values FLAG quotes (ETM 19 107 vs RQCD 16 70). The selection is disclosed; the docstring at massform.py:353-354 names 'ETM 19' but not its N_f = 2 + 1 + 1, and does not name the RQCD 16 N_f = 2 value it was chosen over (both are in the held quote at :1340-1343).",
  "'FLAG ... PRINTS a charm sigma term' (massform.py:353): per the held quote FLAG QUOTES individual determinations inside a consistency sentence; nothing held shows a FLAG average for sigma_c. The tree does not call it an average, so this is a wording note, not a mis-statement -- and whether FLAG averages sigma_c is itself unverified this pass.",
  "HETEROGENEOUS SUM ADDED: the CONTESTED row 'sigma_piN + sigma_s + sigma_c (ETM 19)' (massform.py:1859-1862) adds FLAG's N_f=2+1+1 AVERAGE sigma_piN = 60.9 (FLAG-447) and sigma_s = 41.0 (FLAG-449) to ETM 19's single-study sigma_c. The three are not one collaboration's consistent set; ETM 19's own sigma_piN was not read here. Row is labelled CONTESTED as mass and is never in the READ rows (massform.py:356, selftest :5015-5017).",
  "NO DRIFT in the direction of M: the tree labels heavy-quark terms 'CONTESTED' as mass the Higgs MAKES (massform.py:355-356) even though FLAG's own held definition (FLAG-def) reads sigma_c as the M_N shift from nonzero m_c -- the tree's label is the more conservative reading, not an over-representation."
 ],
 "data_at_publication": [
  {
   "quantity": "sigma_c (ETM 19, N_f = 2+1+1)",
   "value_then": "107(22) MeV (as held from FLAG 2024; primary: ETM 19, ~2019)",
   "value_now": "NOT READ this pass -- no later determination was retrievable (alphaXiv quota exhausted; arXiv egress-blocked)",
   "source_now": "none read",
   "moves_conclusion": "Computed: NO within any plausible move. The sigma_c row does not set any printed figure: HIGGS_SHARE_LARGEST_ALL = 0.3090 is set by the 'six-quark coupling, FLAG 2+1+1' row and HIGGS_SHARE_LARGEST_READ = 0.1719 excludes sigma_c. For the sigma_c row to set the all-rows figure sigma_c would need 186.0 MeV (3.6 sigma above ETM 19); to reach one half at first order, 364.1 MeV (11.7 sigma). Verdicts in S10 rest on C1/C3/C5 and on C2 over READ rows."
  },
  {
   "quantity": "sigma_c (RQCD 16, N_f = 2) / f_Tc",
   "value_then": "70(4) MeV, f_Tc = 0.075(4)",
   "value_now": "not read",
   "source_now": "none read",
   "moves_conclusion": "No: the tree uses the larger (107). Internal check: 0.075 x m_N(tree 938.919 MeV) = 70.42 MeV, consistent with the quoted 70(4)."
  },
  {
   "quantity": "m_N used to convert (tree M_N_MEV = mean of p and n)",
   "value_then": "938.9188 MeV (tree, from READ PDG masses)",
   "value_now": "unchanged at this precision",
   "source_now": "tree's own READ masses",
   "moves_conclusion": "No: f_Tc(ETM 19) = 107/938.919 = 0.1140(234)."
  },
  {
   "quantity": "SVZ leading-order heavy-quark expectation (cross-check, from the tree's own f_TQ = (2/27)(1 - f_l))",
   "value_then": "f_l(FLAG 2+1+1) = 0.10853 -> sigma_Q = 62.0 MeV; f_l(FLAG 2+1) -> 63.1 MeV",
   "value_now": "same (computed)",
   "source_now": "exact arithmetic here",
   "moves_conclusion": "No. ETM 19's 107(22) sits 2.05 sigma (ETM error only) above the LO heavy-quark value; RQCD 16's 70(4) is within ~2 sigma of it. A tension of this size is a discrepancy to record, not a refutation of either -- and the LO relation carries O(alpha_s) and 1/m_c corrections not computed here."
  }
 ],
 "rederivation": {
  "method": "numeric",
  "script_path": D + "/rederive/2411.04268-sigma_c.py",
  "outcome": "15/15 PASS. Checked: the tree's held quote carries ETM 19 107(22) N_f=2+1+1 and RQCD 16 70(4)/0.075(4); SIGMA_C_ETM19 = 107.0 is the larger of the two; RQCD's f_Tc x m_N = 70.42 MeV reproduces 70(4); sigma_fraction(60.9, 41.0, 107)/m_N = 0.222490 exactly; ETM 19 vs RQCD 16 differ by 37 MeV = 1.65 combined sigma (the held word 'consistent' is arithmetically fair at < 2 sigma); ETM 19 is 2.05 sigma above the SVZ-LO heavy-quark value 62.0 MeV the tree itself carries; the sigma_c row is the single CONTESTED row of its kind; it does not set HIGGS_SHARE_LARGEST_ALL (0.3090, set by the six-quark coupling row) nor enter HIGGS_SHARE_LARGEST_READ (0.1719); thresholds 186.0 MeV and 364.1 MeV computed. massform.py imported read-only with bytecode disabled; git status of research/ clean after the run. What is NOT checkable here: the measurement itself (a lattice result, not closed-form) and whether the held quote matches FLAG's page -- the source could not be opened.",
  "agrees_with_source": "partly"
 },
 "later_literature": [
  {
   "ref": "none retrieved",
   "effect": "contested",
   "what": "discover_papers for later lattice sigma_c determinations was attempted and refused (alphaXiv quota exceeded); no later work was read, so nothing is claimed to confirm, narrow or contradict ETM 19. The 'effect' field is forced by the schema; the true status is UNSEARCHED.",
   "read_status": "NOT-SEARCHED (tool quota exhausted)"
  }
 ],
 "lacked_data": "Not assessable at source this pass: neither FLAG 2024 nor ETM 19 could be opened, so what data ETM 19 had (ensembles, lattice spacings, continuum extrapolation, excited-state control) is NOT READ and is not asserted. What IS computed bears on M's hypothesis from the other side: the tree's conclusions are insensitive to this datum. sigma_c enters one row labelled CONTESTED as mass, never the READ rows; that row does not set any printed figure; a move to 186 MeV (+3.6 sigma) would be needed for it to set the all-rows display and 364 MeV (+11.7 sigma) to reach one half. So even if later data moved sigma_c by several sigma either way, no S10 verdict or printed figure would move. Evidence the other way: ETM 19's 107(22) is 2.05 sigma above the SVZ leading-order heavy-quark expectation the tree also carries (62 MeV), and 1.65 sigma above RQCD 16 -- a recorded discrepancy consistent with incomplete lattice systematics or with higher-order heavy-quark corrections; neither is shown here, and it is not a refutation.",
 "grade": "OPEN",
 "grade_evidence": "The measurement could not be read at source this pass (alphaXiv quota exceeded on all three tools; arxiv.org/alphaxiv.org/semanticscholar egress-blocked), and no later literature could be searched, so whether 107(22) is quoted correctly and whether it still stands cannot be established here -- it is not flattened to STANDS. What was checkable agrees with the tree (15/15): the arithmetic, the 'largest printed' selection, the RQCD f_Tc conversion, and -- decisively for the tree -- insensitivity: no sigma_c within 3 sigma moves any printed figure or verdict (thresholds 186.0 MeV and 364.1 MeV). Drifts recorded (dropped 22 MeV uncertainty, disclosed; 'up to' selection over RQCD 16, disclosed in SOURCES; heterogeneous FLAG-average + single-study sum in a CONTESTED row) are all conservative or disclosed; none is in M's favour.",
 "what_would_change_the_grade": "Reading FLAG 2024 (arXiv:2411.04268v3) Sec. 10.4.4 p.275 and confirming the held quote verbatim, plus reading ETM 19 for sigma_c = 107(22) MeV and its systematics, plus one discover_papers pass finding no superseding N_f=2+1+1 determination outside 186 MeV -> STANDS. A misquote in the held text -> a DISCREPANCY recorded (not WRONG; no conclusion rests on the value). A later determination >= 186 MeV would change which row sets the CONTESTED all-rows display (still not a verdict) -> DATA-DEPENDENT for that display only.",
 "reverify_command": "python3 " + D + "/rederive/2411.04268-sigma_c.py  # then, with alphaXiv quota: answer_pdf_queries(paper='2411.04268', queries=['Sec. 10.4.4 charm sigma term RQCD 16 70(4) ETM 19 107(22)', 'is there a FLAG average for sigma_c'])",
 "report_path": D + "/audits/2411.04268-sigma_c.json"
}
json.dump(R, open(D + "/audits/2411.04268-sigma_c.json", "w"), indent=1)
print("ok")
