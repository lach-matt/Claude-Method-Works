import json
D="/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "0708.2450-conclusion",
 "name": "Fewster-Osterbrink conclusion: an absolute QEI for non-minimal coupling 'can also be adapted' (expected, not done), with a literature search returning none",
 "source": {
  "located": "C.J. Fewster & L.W. Osterbrink, 'Quantum Energy Inequalities for the Non-Minimally Coupled Scalar Field', arXiv:0708.2450v2 [gr-qc], 23 Oct 2007 (J. Phys. A 41 (2008) 025402); Sec. 6 Conclusion, pp.20-21, last paragraph; ref. [31] = C.J. Fewster & C.J. Smith, gr-qc/0702056 (2007).",
  "read_status": "READ",
  "via": "Full extracted text of 0708.2450v2 obtained earlier this docket through alphaXiv get_paper_content(fullText=true), cached at scratchpad/d67/src/0708.2450.txt (md5 5ef2edeec5aa48e27368f476cb65da2a); Sec. 6 read in full (lines 3809-3847). A fresh alphaXiv call this stage returned 'assistant quota exceeded' and arxiv.org returns 403 at the proxy, so the cached full text is what was read; the quotes are string-matched against it by the rederive script."
 },
 "published_statement": "FO Sec. 6, final paragraph: 'Finally, our general QEI is of the so-called ‘difference’ type: it constrains the normal ordered energy density rather than the (Hadamard) renormalised version. This restriction has recently been removed for the minimally coupled field in [31] to obtain an ‘absolute’ QEI; one would expect that this can also be adapted to the non-minimally coupled field.' ([31] = Fewster-Smith gr-qc/0702056.) Context in the same section: the QEI being referred to is FO's STATE-DEPENDENT QEI 'for couplings in the range (0, 1/4] in general globally hyperbolic spacetimes' (Thm 4.2 states xi in [0,1/4]); state-independent QEIs are excluded for xi > 0 'at least for massless fields in four-dimensional Minkowski space'.",
 "published_hypotheses": [
  "P1 it is an EXPECTATION ('one would expect'), not a theorem: no absolute NMC QEI is derived or sketched in 0708.2450",
  "P2 the object expected is the Hadamard-renormalised ('absolute') counterpart of FO's own state-dependent difference QEI -- a state-DEPENDENT absolute bound (FO Sec. 3 already excludes a state-independent one for xi > 0, massless, 4D Minkowski)",
  "P3 the route expected is adaptation of the Fewster-Smith (gr-qc/0702056) method, which was then (2007) new and proved for the minimally coupled field only",
  "P4 implicit scope of the difference QEI being upgraded: xi in (0,1/4] (Thm 4.2: [0,1/4]), globally hyperbolic spacetime, timelike geodesic, Hadamard states"
 ],
 "hypothesis_drift": [
  "KEPT, no drift on the FO sentence: qeihps.py:89-90 'an absolute version for non-minimal coupling \"can also be adapted\" -- expected, NOT DONE' -- 'can also be adapted' is FO verbatim (string-matched), 'expected' renders 'one would expect', 'NOT DONE' is accurate (FO: 'our general QEI is of the so-called difference type').",
  "KEPT: the owner's own hypothesis 'the NOT-FOUND is a search result over alphaXiv, not a non-existence proof' (qeihps.py:90-92, 511-512 'alphaXiv search returned none') -- the tree does not flatten the search to 'does not exist'.",
  "DROPPED (minor, a precision not a change of claim) P2 at qeihps.py:511-512: ABSOLUTE_QEI_FOR_NMC does not say the expected object is a state-DEPENDENT absolute bound; specthm.py:2159-2164 (H_M0) supplies it by context ('state-dependent NMC bounds exist ... and an absolute one is NOT-FOUND'), specthm.py:1049-1053 (R6) does not ('An absolute QEI for NMC is NOT-FOUND'). Read literally, R6's sentence could be taken as 'no absolute state-independent QEI found' -- which is not a search result but FO Sec. 3's theorem (massless, 4D Minkowski).",
  "UNSTATED (named here): the NOT-FOUND carries no search date and no coverage statement at qeihps.py:90-92, 511-512; a search result is dated by nature. Recorded, not repaired.",
  "MISSED SOURCE (a discrepancy of the search, not of FO): Fewster-Kontou 1809.05047v2 p.3 states the contrary -- 'as shown in Ref. [28] [math-ph/0611058], nonminimally coupled fields obey state dependent QWEIs of both absolute and difference types' -- and the qeihps search did not record it. The pages of math-ph/0611058 read (1-2, 6-9, 22, 24-27) show only the FO difference QEI for NMC (App. B) and a broadened definition of state-dependent absolute QIs; Sec. 3.2-4 (Props 4.5, 4.6, the DQI/AQI relations) was not readable this stage. Conversely the tree could have cited a POSITIVE statement for its NOT-FOUND: Kontou-Sanders 2003.01815 'To date no absolute QEIs have been derived for the non-minimally coupled scalar field.'"
 ],
 "data_at_publication": [
  {
   "quantity": "state of the literature on absolute (Hadamard-renormalised, local and covariant) QEIs -- the only 'input' an expectation depends on (no numerical datum enters)",
   "value_then": "2007: first curved-spacetime absolute QEI just proved for the MINIMALLY coupled massive scalar (Fewster-Smith gr-qc/0702056v3, 'the first absolute QEI applicable to the scalar field'); NMC: difference QEI only (FO), state-independent QEI excluded for xi > 0 (FO Sec. 3)",
   "value_now": "2020: Kontou-Sanders review: 'To date no absolute QEIs have been derived for the non-minimally coupled scalar field. The root cause is that the operator T^split_ab is not of positive type or symmetric.' 2023: FFKP 2309.10848 Sec. IV: 'the derivation is for a difference QEIs unlike the absolute one that was possible for the minimally coupled field.' 2024: Kontou 2405.05963: T^split of NMC fields is not positive type 'so these inequalities cannot be used in this case. State-dependent bounds have been derived [17,29,30].' Contrary (2018): 1809.05047 p.3 'obey state dependent QWEIs of both absolute and difference types' citing math-ph/0611058, not substantiated in the pages of that paper read. Post-mid-2024 literature: NOT SEARCHED this stage (alphaXiv quota exhausted).",
   "source_now": "scratchpad/d67/src/casmag/all/2003.01815v2.txt (md5 a647c534...), src/2309.10848.txt (md5 4f318768...), src/casmag/all/2405.05963v2.txt (md5 7b8e441a...), src/casmag/all/1809.05047v2.txt (md5 aa6f78fe...), src/casmag/all/math-ph_0611058v2.txt (md5 bdc1fee5..., partial) -- all alphaXiv extractions cached earlier in this docket; every sentence quoted here is string-matched by the rederive script",
   "moves_conclusion": "No. FO's expectation remained an expectation through 2024 by the field's own reviews (one of them co-authored by the author of the contrary 2018 sentence); the tree's NOT-FOUND is corroborated, not overturned. The one contrary published sentence is a contest, recorded, not a refutation."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/0708.2450-conclusion.py",
  "outcome": "ALL PASS (32 checks; output at rederive/0708.2450-conclusion.out). (A) FO's Sec. 6 sentence and ref. [31], and the five later-literature sentences the grade rests on (including the contrary 1809.05047 one), string-matched in md5-pinned cached texts; the tree's 'can also be adapted' is FO verbatim. (B) The obstruction the later reviews name -- T^split not of positive type for NMC -- machine-checked on the Minkowski NMC energy density, kernel on one-particle wavefunctions K(k,k') = [w w' + k.k' + m^2 + 2 xi |k-k'|^2]/(2 sqrt(w w')) (from rho = rho_min - xi Lap phi^2, signature (+,-,-,-)): sympy gives the massless s-wave 2x2 minor det = -xi (k1-k2)^2 (k1 k2 + xi (k1+k2)^2)/(k1 k2), negative for EVERY xi > 0 and k1 != k2, zero at xi = 0 (e.g. xi = 1/6, (k1,k2) = (1,2): det = -7/24); (C) numerically, 40 random 3-momenta: min eigenvalue ~ -6e-15 at xi = 0 (positive type), -1.81e-2 at xi = 1e-3, -3.05 at xi = 1/6, -4.60 at xi = 1/4, -1.40 at m = 1, xi = 1/6. So the Fewster-Smith route FO expected to adapt loses its positivity hypothesis for every xi > 0 -- which corroborates WHY nothing was 'adapted' directly; it is NOT a proof that no absolute NMC QEI exists (FO's own difference QEI evades the same non-positivity by splitting off a Wick-square term, and an absolute analogue by that route is neither proved nor excluded here).",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "E.-A. Kontou & K. Sanders, 'Energy conditions in general relativity and quantum field theory', arXiv:2003.01815v2 (Class. Quantum Grav. 37 (2020) 193001)",
   "effect": "confirms",
   "what": "'To date no absolute QEIs have been derived for the non-minimally coupled scalar field. The root cause is that the operator T^split_ab (see (50)) is not of positive type or symmetric.' Also defines 'absolute' as a lower bound local and covariant in metric and test function, and shows the trivial rearrangement of a difference QEI 'only yields an absolute QEI when the lower bound is local and covariant' -- which excludes the reference-state shortcut as a way to claim FO's expectation met.",
   "read_status": "READ (cached alphaXiv extraction, the absolute/difference passage and the NMC paragraph; string-matched)"
  },
  {
   "ref": "J.R. Fliss, B. Freivogel, E.-A. Kontou & D. Pardo Santos, 'Non-minimal coupling, negative null energy, and effective field theory', arXiv:2309.10848 (2023)",
   "effect": "confirms",
   "what": "Sec. IV: the curved-spacetime NMC null QEI (Thm IV.1) is 'for a difference QEIs unlike the absolute one that was possible for the minimally coupled field'; absolute QEIs via the Hadamard parametrix are 'not used here'.",
   "read_status": "READ (cached full text, Sec. IV opening and the Hadamard-parametrix paragraph)"
  },
  {
   "ref": "E.-A. Kontou, 'Wormhole Restrictions from Quantum Energy Inequalities', arXiv:2405.05963v2 (Universe 10 (2024) 291)",
   "effect": "confirms",
   "what": "Positivity of T^split is what makes the general (difference and absolute) worldline QEI work; 'This is not true ... for the T split operator of nonminimally coupled fields, so these inequalities cannot be used in this case. State-dependent bounds have been derived for the nonminimally coupled field [17,29,30].' No absolute NMC QEI cited as of mid-2024.",
   "read_status": "READ (cached extraction, Sec. on general QEIs)"
  },
  {
   "ref": "C.J. Fewster & E.-A. Kontou, 'Quantum strong energy inequalities', arXiv:1809.05047v2 (Phys. Rev. D 99 (2019) 045001)",
   "effect": "contested",
   "what": "p.3: 'as shown in Ref. [28] [math-ph/0611058], nonminimally coupled fields obey state dependent QWEIs of both absolute and difference types' -- the one published sentence contrary to the tree's NOT-FOUND; the same paper derives only a difference QSEI and says an absolute QSEI 'is the objective of a future work'. Its co-author's 2020 review states none has been derived. Unresolved here: which result in math-ph/0611058 is meant.",
   "read_status": "READ (cached full text, p.3 introduction)"
  },
  {
   "ref": "C.J. Fewster, 'Quantum energy inequalities and local covariance II: categorical formulation', arXiv:math-ph/0611058v2 (Gen. Rel. Grav. 39 (2007) 1855)",
   "effect": "contested",
   "what": "Broadens 'absolute QI' to state-dependent bounds omega(T(f)) >= -omega(Q(f)) with Q(f) in the algebra, explicitly to encompass NMC (p.7-8); App. B illustrates only 'the difference QEI obtained in [22] [FO] ... for the case 0 <= xi <= 1/4'; App. A: the DQI 'obeys the continuity hypotheses required in Propositions 4.5 and 4.6(b)'. Those propositions (the DQI/AQI relations, pp.10-21) were NOT readable this stage, so whether an abstract state-dependent AQI for NMC follows there is OPEN.",
   "read_status": "READ in part (cached pages 1-2, 6-9, 22, 24-27); Sec. 3.2-5 NAMED-NOT-READ"
  },
  {
   "ref": "discover_papers for post-2024 work on an absolute NMC QEI",
   "effect": "contested",
   "what": "NOT RUN: alphaXiv returned 'assistant quota exceeded' on discover_papers, get_paper_content and answer_pdf_queries this stage; arxiv.org and export.arxiv.org return 403 at the proxy. Literature after Kontou 2405.05963 (July 2024) is therefore unsearched here; 2503.24068 (2025, non-commutative QFT QEI) is in the cache and cites FO and Fewster-Smith but gives no NMC absolute QEI.",
   "read_status": "NOT-READ (tool quota); cached 2503.24068v2 grepped only"
  }
 ],
 "lacked_data": "FO's sentence is an expectation about a method, not a conclusion from data; no measured quantity enters, so M's hypothesis ('previous physicists may have lacked certain data') has no datum to act on here. What FO lacked in 2007 was the outcome of the attempt: Fewster-Smith's absolute QEI (gr-qc/0702056) was months old and minimal-coupling only. Evidence since: (for the tree) the 2020 Kontou-Sanders review, FFKP 2023 and Kontou 2024 all record that no absolute NMC QEI has been derived and name the obstruction -- T^split is not of positive type -- which the rederive script machine-checks: the NMC point-split energy-density kernel has a negative 2x2 minor for every xi > 0 (det = -xi(k1-k2)^2(k1k2 + xi(k1+k2)^2)/(k1k2)), so the Fewster-Smith route cannot be carried over verbatim; (against the tree) Fewster-Kontou 2018 asserts absolute state-dependent NMC QWEIs were shown in math-ph/0611058, whose readable pages do not show one. Having the later information does not change the tree's use: FO's 'expected, not done' is still accurate as a description of FO, and NOT-FOUND is still the state of the literature as far as it could be read here (through mid-2024). It does sharpen it: the NOT-FOUND can rest on a published review sentence rather than on a search alone, and the contrary 2018 sentence should be recorded beside it.",
 "grade": "STANDS",
 "grade_evidence": "(1) The FO sentence is quoted accurately: 'can also be adapted' is verbatim, 'expected'/'NOT DONE' render 'one would expect' and FO's own statement that their QEI is difference type (string-matched in the md5-pinned full text, rederive (A)). (2) The tree keeps FO's status (an expectation) and its own hypothesis (a search result, not a non-existence proof); nothing is promoted to a theorem. (3) The NOT-FOUND is corroborated by three later sources read here -- Kontou-Sanders 2020 ('To date no absolute QEIs have been derived for the non-minimally coupled scalar field'), FFKP 2023 (difference only), Kontou 2024 (T^split not positive type; state-dependent bounds only) -- and the obstruction they name is machine-checked (rederive (B),(C): negative minor for every xi > 0, positive type at xi = 0). (4) No datum enters. Limits carried with the grade, not hidden in it: one contrary published sentence (1809.05047 p.3, citing math-ph/0611058) stands unresolved because math-ph/0611058 Sec. 3.2-4 could not be read this stage -- a CONTEST, recorded, not a refutation of either side; post-mid-2024 literature was not searched (alphaXiv quota exhausted); R6 (specthm.py:1049-1053) omits 'state-dependent', a precision the H_M0 text supplies. Not NARROWED: the tree uses the sentence exactly as FO wrote it and qualifies its search itself. Not WRONG: nothing refutes it. Not DATA-DEPENDENT: no datum.",
 "what_would_change_the_grade": "To NARROWED or WRONG: a paper deriving a local and covariant (Hadamard-renormalised) QEI for the NMC scalar -- state-dependent is enough -- published at any date (then NOT-FOUND is a missed result; if it predates the qeihps search, the search was incomplete); or math-ph/0611058 Props 4.5/4.6 read and shown to yield such an AQI for FO's DQI, which would substantiate 1809.05047's sentence. To OPEN: if the math-ph/0611058 reading is held to decide the matter and cannot be done. Stays STANDS if a post-2024 discover_papers search and the unread 0611058 pages both return no absolute NMC energy-density QEI.",
 "reverify_command": "python3 /tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/0708.2450-conclusion.py  # expects ALL PASS; then grep -n 'can also be adapted' /home/user/Claude-Method-Works/research/warp-drive/qeihps.py; and (when quota allows) alphaXiv answer_pdf_queries(paper='math-ph/0611058', queries=['Propositions 4.5 and 4.6: DQI to AQI', 'absolute QEI for the non-minimally coupled field']) plus discover_papers(['absolute quantum energy inequality','non-minimally coupled scalar'], prioritize='recency')",
 "report_path": D + "/audits/0708.2450-conclusion.json"
}
R["published_hypotheses"]=R["published_hypotheses"]
json.dump(R, open(R["report_path"],"w"), indent=1, ensure_ascii=False)
print("written", R["report_path"])
