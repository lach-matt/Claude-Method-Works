import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
R = {
 "key": "clock-accuracy-1e-18",
 "name": "Clock-comparison accuracy 1e-18 (address.py section 7 fixture; 'optical/optical ratio 3e-16 in Godun 2014 and heading below 1e-18')",
 "source": {
  "located": "Godun et al., PRL 113, 210801 (2014) = arXiv:1407.0164v2 (the one cited datum). The 1e-18 itself cites no source (excite.py:397-400 calls it an ORDER, not a measurement), so its external support was read in the current measurement papers: arXiv:2403.10664 (Sr, 8.1e-19), 2512.07346 (Lu+/Lu+, 1.1e-19 systematic, agreement 5.8e-19), 2512.21428 (BACON 2025 ratios <=3.2e-18), 2603.23446 (Sr+ multi-ion 5.3e-19; Sr+/Yb+ ratio 2.9e-18), 2406.18719 (Th-229/Sr ratio 1.06e-12)",
  "read_status": "READ",
  "via": "alphaXiv answer_pdf_queries, full page text of 1407.0164v2 pp.1-6 including Table I; full page text of the five later papers listed. 2507.14030, 2606.23151, 2606.10514 and 2608.01916 were seen only as abstract snippets in the discover_papers listing and are marked so wherever they are used."
 },
 "published_statement": "Godun et al. 2014 (1407.0164v2 p.1): 'we present the first direct measurement of the ratio between the E3 and E2 optical transition frequencies in 171Yb+, with fractional uncertainty 3 x 10^-16'; p.3: 'nu_E3/nu_E2 = 0.932 829 404 530 964 65(31)'; Table I TOTAL for the ratio 3.36e-16 (systematic subtotal 3.29e-16, statistical 0.68e-16, dominated by the residual quadrupole shift of E2, 2.97e-16). p.4: 'Dependence on mu-dot arises through the nuclear magnetic moment and is negligible for optical transitions (the sensitivity coefficient B_E3 = B_E2 = 0).' The tree's '1e-18' has no published source: address.py:37-39 says only 'heading below 1e-18'; excite.py:397-400 declares CLOCK_ACCURACY_FIXTURE = 1e-18 an ORDER.",
 "published_hypotheses": [
  "Godun: a single 171Yb+ ion, E3 and E2 interrogated interleaved on ~100 ms timescale, so gravitational redshift and time dilation are common-mode in the RATIO (p.2)",
  "Godun: ac Stark shift of E3 removed by extrapolation between two probe powers, assuming constant beam pointing over the ~3 s cycle and a known power ratio kappa (sigma_kappa/kappa = 2e-4) (p.2)",
  "Godun: quadrupole shift averaged out by three nominally orthogonal field directions; residual set by non-orthogonality, simulated (p.2)",
  "Godun: BBR shift from experimental differential polarizabilities at 294.5 +- 2 K (p.2)",
  "Godun: the constraints on alpha-dot and mu-dot assume local position invariance and linear time variation (p.4)",
  "Godun: B_E3 = B_E2 = 0 is 'negligible', not zero -- dependence on mu only through the nuclear magnetic moment (p.4)",
  "Current literature (2512.07346 p.8; 2512.21428 p.2): a stated systematic uncertainty is 'validated' only by a comparison; the roadmap criteria are <= 2e-18 evaluated and <= 5e-18 agreement; repeatability below 1e-17 'remains an outstanding issue for clock comparisons' (2512.21428 p.4)"
 ],
 "hypothesis_drift": [
  "ADDED by the tree, not in any source: a clock CARRIED INTO the displaced region and compared with a twin outside (address.py:249-255; excite.py:397-401). Every sub-1e-18 figure READ is a stationary in-lab clock or an in-lab same-species pair (Lu+/Lu+ 1.2 m apart, 2512.07346 Fig.1). A transported comparison is a different measurement; the best transportable figure seen is 2.1e-18 systematic (2507.14030, abstract snippet only). WEAKENS the fixture for the courier use by a factor ~2, which moves no verdict (computed, section C).",
  "ADDED, carried unflagged to a different kind of clock: address.py:1161-1178 and 1537-1551 apply the same 1e-18 to a Th-229 NUCLEAR clock (eps_detectable_th229(1e-18, ...)), giving eps_det = 2.86e-24 and 'EIGHT ORDERS BETTER' (address.py:286). The READ state of Th-229 (2406.18719 p.8) is nu_Th/nu_Sr = 4.707 072 615 078(5) = 1.06e-12, 'Systematic uncertainty of this frequency ratio will be explored in future studies.' The fixture sits six orders past the measured nuclear state; the tree labels Flambaum's COEFFICIENT an ORDER (address.py:292-293) but not the ACCURACY applied to it. At the READ precision eps_det(Th-229) = 3.04e-18, worse than the electronic courier at the fixture.",
  "WEAKENED qualifier: address.py:37-38 calls the optical/optical ratio 'the sharpest measurement in physics'; the nearest source wording (2512.21428 p.2) is 'the most precise measurements of any physical quantity (other than symmetry tests, e.g. [27])' -- the tree drops 'other than symmetry tests'.",
  "LITERAL SCOPE: address.py:37-39 says an optical-to-optical frequency RATIO is 'heading below 1e-18'. As of the READ literature no inter-species optical ratio is below 1e-18 (best 2.2e-18, Al+/Sr, 2512.21428; 2.9e-18 Sr+/Yb+, 2603.23446). 'Heading below' is a trend statement and is accurate as one; sub-1e-18 has been reached by single-clock systematic budgets (8.1e-19, 5.5e-19, 5.3e-19, 1.1e-19) and by one same-species agreement (5.8e-19), not by a ratio.",
  "PRESERVED, not drifted: address.py:41-43 reproduces Godun's B_E3 = B_E2 = 0 as 'negligible, not zero' and its W10 withdrawal of 'EXACTLY BLIND' matches Godun p.4.",
  "The tree's own (not external) 'coefficient exactly 1' (excite.py:397-401, address.py:252, 740-742) is exact only for an infinite-mass nucleus: with the reduced-mass Rydberg it is 1 - x(1-f)/(1+x), x = m_e/M (sympy, section G): 1 - 5.1e-4 (hydrogen, H2), 1 - 5.9e-6 (87Sr, H2). Recorded as a discrepancy in the tree's wording, not a refutation; it moves eps_det by at most 0.051%."
 ],
 "data_at_publication": [
  {"quantity": "Godun 2014 E3/E2 ratio fractional uncertainty (the cited datum)",
   "value_then": "3e-16 as printed; Table I TOTAL 3.36e-16; from the quoted digits (31)/0.93282940453096465 = 3.32e-16",
   "value_now": "unchanged as a historical measurement; the best optical/optical ratio now is 2.2e-18 (BACON Al+/Sr)",
   "source_now": "arXiv:1407.0164v2 Table I (READ); arXiv:2512.21428 eq.(1) (READ)",
   "moves_conclusion": "No. Godun's 3e-16 enters the tree only as the stationary optical/optical control; re-deriving it reproduces 3.36e-16 exactly."},
  {"quantity": "best single-clock evaluated systematic uncertainty (what 'heading below 1e-18' forecast)",
   "value_then": "1e-18 ORDER (fixture, uncited)",
   "value_now": "1.1e-19 (Lu+ NUS 2025), 5.3e-19 (Sr+ PTB 2026), 5.5e-19 (Al+ NIST 2025, via 2512.07346 Table 2), 8.1e-19 (Sr JILA 2024)",
   "source_now": "arXiv:2512.07346 Table 1-2; 2603.23446 Table I; 2403.10664 Table I (all READ)",
   "moves_conclusion": "No. The forecast is confirmed for single clocks; the courier source scales linearly with the accuracy and stays > 2e7 x osmium at every READ value."},
  {"quantity": "same-species clock agreement (the measurement the courier would actually be)",
   "value_then": "1e-18 ORDER",
   "value_now": "[-2.4 +- 5.7(stat) +- 1.0(sys)] x 1e-19, total 5.79e-19, in-lab, stationary",
   "source_now": "arXiv:2512.07346 p.2, Fig.2 (READ)",
   "moves_conclusion": "No. At 5.79e-19 the courier source is 4.74e11 kg/m^3 (H1) to 2.12e12 (H2), 2.1e7 to 9.4e7 x osmium; the verdict 'the medium that makes the signal destroys the instrument' is untouched."},
  {"quantity": "best inter-species optical/optical frequency ratio",
   "value_then": "'heading below 1e-18'",
   "value_now": "2.2e-18 (Al+/Sr), 3.1e-18 (Yb/Sr), 3.2e-18 (Al+/Yb) -- recomputed from the quoted digits as 2.22e-18, 3.06e-18, 3.24e-18; 2.89e-18 (Sr+/Yb+)",
   "source_now": "arXiv:2512.21428 eq.(1); 2603.23446 p.5 (READ)",
   "moves_conclusion": "No. At 2.22e-18 the courier source is 1.82e12 (H1) to 8.15e12 (H2) kg/m^3."},
  {"quantity": "repeatability of stated uncertainties between campaigns",
   "value_then": "not considered by the tree",
   "value_now": "BACON 2025 vs BACON 2021: 87Sr ratios differ by ~1e-16 (14 sigma), Al+/Yb by 1.6e-17 (2.4 sigma); 'repeatability below 1e-17 remains an outstanding issue'",
   "source_now": "arXiv:2512.21428 abstract, p.2, p.4 (READ)",
   "moves_conclusion": "No, and in the tree's disfavour only. A worse effective accuracy raises the source density the courier needs (at 1e-16: 8.2e13 H1), which strengthens rather than weakens the verdict it supports."},
  {"quantity": "Th-229 nuclear clock accuracy (the fixture as applied at address.py:1167, 1537)",
   "value_then": "1e-18 (the electronic fixture, applied to a nuclear clock)",
   "value_now": "nu_Th/nu_Sr = 4.707 072 615 078(5), 1.06e-12, statistical; systematics not yet evaluated",
   "source_now": "arXiv:2406.18719v2 p.8 (READ)",
   "moves_conclusion": "Moves a figure, not a verdict. eps_det(Th-229) goes 2.86e-24 -> 3.04e-18, and 'EIGHT ORDERS BETTER' (address.py:286) holds only for a hypothetical 1e-18 nuclear clock. Section 9's domination theorem survives at every eps_det tested (gravimeter ahead by > 1e22 at every density, ratio diverging), as address.py:292-293 claims."},
  {"quantity": "transportable optical clock systematic uncertainty",
   "value_then": "not considered (courier = carried clock)",
   "value_now": "2.1e-18 total systematic (Sr, PTB) -- ABSTRACT SNIPPET ONLY, full text not read",
   "source_now": "arXiv:2507.14030 (discover_papers listing only)",
   "moves_conclusion": "No. The factor ~2 over the fixture scales the courier source to ~1.7e12 (H1)."},
  {"quantity": "m_h, entering COURIER_SOURCE (the tree's own input, recorded for completeness)",
   "value_then": "125.20 pin (withdrawn) -> 8.19956e11 kg/m^3 (H1)",
   "value_now": "125.13 READ -> 8.19040e11 (H1), 3.67051e12 (H2); excite.py:1380 already rescales by MH^2",
   "source_now": "higgs.M_HIGGS (captures/PDG-2026.tsv, per LEDGER D20)",
   "moves_conclusion": "No. address.py:262's prose '8.20e11' is the pre-READ rounding (8.190e11 now) -- a 0.1% discrepancy in prose, recorded, not repaired."}
 ],
 "rederivation": {
  "method": "numeric",
  "script_path": D + "/rederive/clock-accuracy-1e-18.py",
  "outcome": "ALL PASS (31 checks, exit 0; output in rederive/clock-accuracy-1e-18.out). (A) Godun Table I: sqrt(3.29^2+0.68^2) = 3.3595e-16, printed 3.36; digits give 3.32e-16; '3e-16' is that figure to 1 s.f. (B) BACON 2025 fractional uncertainties recomputed from the quoted digits: 2.22e-18, 3.24e-18, 3.06e-18; Sr+/Yb+ 2.89e-18; no inter-species ratio below 1e-18; Lu+/Lu+ total 5.79e-19 with -2.4e-19 inside 1 sigma; Th/Sr 1.06e-12. (C) Importing the tree's own address.py read-only (sys.dont_write_bytecode): COURIER_SOURCE at 1e-18 equals excite.py's pins x MH^2 to 1e-5; the courier source stays > 1e7 x osmium at every READ accuracy from 5.79e-19 to 3.36e-16. (D) The courier source reaches osmium density only at a clock accuracy of 2.76e-26 (H1) / 6.15e-27 (H2), more than 6 orders below the best READ clock (1.1e-19). (E) Th-229: coefficient -3.4963e5, eps_det 2.860e-24 at the fixture, 3.038e-18 at the READ Th/Sr precision. (F) Section 9's domination ratio at eps_det in {1e-18, 2.86e-24, 3.04e-18, 5.79e-19}: minimum over rho in 1e12..1e30 > 2.5e22 and diverging in the tail (it dips just above threshold, minimum at rho = e^2 rho_th, as sqrt(rho)/ln(rho/rho_th) must). (G) sympy: d ln R_M/d eps = (1 + f x)/(1 + x) = 1 - x(1-f)/(1+x).",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {"ref": "arXiv:2512.07346 (Arnold, Lee et al., NUS 2025), Optical clocks with accuracy validated at the 19th digit", "effect": "confirms", "what": "Two 176Lu+ clocks at 1.1e-19 and 1.4e-19 systematic; same-species agreement [-2.4 +- 5.7 +- 1.0] x 1e-19 -- the first sub-1e-18 accuracy validated by comparison. Table 2 lists every report meeting either roadmap criterion.", "read_status": "READ (pp.1-8, 13, 16-21)"},
  {"ref": "arXiv:2403.10664 (Aeppli et al., JILA 2024), A clock with 8e-19 systematic uncertainty", "effect": "confirms", "what": "Sr lattice clock 8.1e-19 total systematic, BBR-limited (7.3e-19). A systematic evaluation only; no independent comparison at that level.", "read_status": "READ (pp.1-6, 8, 21)"},
  {"ref": "arXiv:2512.21428 (BACON 2025), Atomic clock frequency ratios with fractional uncertainty <= 3.2e-18", "effect": "narrows", "what": "The best inter-species ratios are 2.2-3.2e-18, so no ratio is yet below 1e-18. It also records 14-sigma and 2.4-sigma disagreements with its own 2021 campaign and says 'repeatability below 1e-17 remains an outstanding issue'.", "read_status": "READ (pp.1-5, 9-10, 12)"},
  {"ref": "arXiv:2603.23446 (Filzinger et al., PTB 2026), A multi-ion optical clock with 5e-19 uncertainty", "effect": "confirms", "what": "88Sr+ multi-ion clock at 5.3e-19; Sr+/Yb+ E3 ratio 0.6926711632159660405(20), 2.9e-18, limited by the single-ion Yb+ clock at 2.7e-18.", "read_status": "READ (pp.1, 3-6, 8, 10)"},
  {"ref": "arXiv:2406.18719 (Zhang et al., JILA 2024), Frequency ratio of the 229mTh nuclear isomeric transition and the 87Sr atomic clock", "effect": "narrows", "what": "The measured Th-229 state is 1.06e-12 (statistical), with a comb-limited ~300 kHz linewidth and systematics unevaluated. The tree's 1e-18 for a nuclear courier is six orders past it.", "read_status": "READ (pp.1-4, 6, 8-11, 13, 15, 18)"},
  {"ref": "arXiv:2507.14030 (PTB 2025), Transportable strontium lattice clock with 4e-19 BBR shift uncertainty", "effect": "narrows", "what": "Transportable clock total systematic 2.1e-18. Relevant because the courier is a carried clock.", "read_status": "ABSTRACT SNIPPET in discover_papers listing only; full text NOT read"},
  {"ref": "arXiv:2606.23151 (Al+ 1.6e-18 and its frequency ratios, 2026); arXiv:2606.10514 (Yb lattice 1.3e-18, 2026); arXiv:2608.01916 (interspecies comparison below 5e-18 with a transportable clock, 2026)", "effect": "extends", "what": "More clocks and ratios in the 1e-18 decade. None reports a ratio below 1e-18 in its title or abstract.", "read_status": "TITLE/ABSTRACT SNIPPET only; NOT read"}
 ],
 "lacked_data": "M's hypothesis, tested. Godun et al. (2014) lacked every sub-1e-17 clock that followed, and the tree's forecast 'heading below 1e-18' is what those clocks measured: four single-clock budgets now sit at 1.1e-19 to 8.1e-19, and one same-species pair agrees at 5.79e-19. For single clocks the forecast is CONFIRMED. It is NOT yet true for the object address.py:37-39 literally names, an inter-species optical/optical RATIO (best 2.2e-18). Evidence cutting the other way, which M's lens predicts: BACON 2025 finds its own 2021 ratios off by ~1e-16 (14 sigma) and says repeatability below 1e-17 is unresolved. That is a published case of an earlier 1e-18-class stated uncertainty that was INCOMPLETE. The tree itself lacked one datum: the measured Th-229 state (1.06e-12, 2406.18719), against which it applied 1e-18. Does having these data change any conclusion? Computed: no. The courier verdict (source > 1e7 x osmium) holds at every accuracy from 1.1e-19 to 3.4e-16 and fails only below 2.8e-26. Section 9's domination theorem holds at every eps_det tested, including the Th-229 value at the measured precision. The one thing that moves is a FIGURE: Th-229's 2.9e-24 and 'EIGHT ORDERS BETTER' become 3.0e-18 at the measured state, i.e. no better than the electronic courier. No datum moves in the tree's favour.",
 "grade": "NARROWED",
 "grade_evidence": "STANDS for what the fixture is declared to be (excite.py:397-400, 267): an ORDER for an electronic optical clock comparison, not a capability. Godun's 3e-16 re-derives from Table I (3.36e-16). Sub-1e-18 is now READ in four single-clock budgets and one same-species agreement (5.79e-19). No verdict resting on it (D20, S6, COURIER_SOURCE F5, section 9 / R5-C) moves anywhere from 1.1e-19 to 3.4e-16, and the courier would need 2.8e-26 to reach osmium density (script sections C, D, F). NARROWED because the tree uses the same 1e-18 on a larger class than the support covers: (i) a Th-229 nuclear clock, whose READ state is 1.06e-12 with systematics unevaluated (2406.18719 p.8), so eps_det(Th-229) = 2.86e-24 and 'EIGHT ORDERS BETTER' (address.py:286, 1161-1178, 1537-1551) hold only for a hypothetical clock six orders beyond measurement, and the tree labels the Th-229 coefficient an ORDER but not the accuracy; (ii) a clock carried across a boundary, while every sub-1e-18 figure READ is stationary and in-lab (transportable 2.1e-18, abstract only); (iii) address.py:37-39's literal object, an optical/optical RATIO, is not yet below 1e-18 (best 2.2e-18). Nothing here is WRONG: no counterexample exists, and the drifts are unflagged scope, not errors. A misprint-class discrepancy (the prose '8.20e11' against 8.190e11 computed at READ m_h) is recorded, not graded.",
 "what_would_change_the_grade": "To STANDS: address.py marks the 1e-18 applied to Th-229 as a projection, an ORDER for a nuclear clock that does not yet exist. It would cite a Th-229 accuracy projection read at source (e.g. Campbell et al. 2012, not read here) or carry the READ 1.06e-12 alongside it, and it would name the stationary-to-transported step as a hypothesis. A published inter-species optical ratio below 1e-18 would retire drift (iii). Toward DATA-DEPENDENT: only an accuracy datum below ~3e-26, which no measurement approaches, or a Th-229 section-9 verdict that turns out to depend on eps_det, which the script's section F finds it does not. Toward WRONG: nothing in this audit; it would take a shown contradiction in Godun's Table I or in the tree's linear courier scaling, and both re-derive.",
 "reverify_command": "python3 /tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/clock-accuracy-1e-18.py   # exits 0 on ALL PASS; imports research/warp-drive/address.py and higgs.py read-only with bytecode writing disabled",
 "report_path": D + "/audits/clock-accuracy-1e-18.json"
}
json.dump(R, open(R["report_path"], "w"), indent=1, ensure_ascii=False)
print("written", R["report_path"])
