import json, os
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/reaudit/"
SCRIPT = D + "lodders2003_reaudit.py"
REV = "PYTHONDONTWRITEBYTECODE=1 python3 " + SCRIPT
FID = "1dxtorrPjr43Bu7Jaq3TdGI8t0ADCd22N"
IDENT = ("Drive file title 'SOLAR SYSTEM ABUNDANCES AND CONDENSATION TEMPERATURES OF THE ELEMENTS.pdf' (280,145 bytes). "
         "Its own p.1 prints 'SOLAR SYSTEM ABUNDANCES AND CONDENSATION TEMPERATURES OF THE ELEMENTS', 'Katharina Lodders', "
         "'Received 2003 January 22; accepted 2003 March 21', and the running line 'The Astrophysical Journal, 591:1220–1247, 2003 July 10'. "
         "It is the cited work. PDF page n = journal page 1219+n (PDF p.2 footer '1221').")
PAGES_COMMON = ("Whole Drive text extraction (168,561 chars, 28 PDF pages = journal pp.1220-1247) received; read closely: "
                "p.1220 (abstract), p.1221 (sec.2.2 CI chondrites), p.1224 (CI group-mean method), pp.1225-1226 (Table 3, all rows H..U), "
                "p.1231 (sec.2.3.2.1 Be), p.1234 (sec.2.3.3 P), p.1236 (sec.3, pressure choice), p.1238 (sec.3.1-3.2 equilibrium, host phases, 10 K composition offset), "
                "pp.1239-1240 (Table 8, complete), p.1241 (Table 9 head), p.1242 (sec.3.3.3 Be 1421 K), p.1243 (pressure dependence Te/Pb; Hg; sec.3.3.8 halogens), "
                "pp.1244-1245 (sec.3.4 O, C, N condensation). Table 3 and Table 8 are rotated tables whose extraction splits digits with spaces "
                "(e.g. '2101 5' = 21015) and renders some decimal points as ':'; each value used was reconstructed from the row and is quoted as extracted. "
                "Ambiguous in extraction: Be group sigma/N_met, Ti group sigma/N_met, Th and U group sigma.")

T3_QUOTES = [
 "Table 3 title: 'TABLE 3 Elemental Abundances in CI Chondrites' ; columns 'Alais Ivuna Orgueil Revelstoke Tonk CI Chondrite Group ... Weighted Mean 1σ N met'",
 "Table 3 note: 'Note.—ppm by mass = μg g−1 ... N = number of analyses included in mean; N met = number of meteorites included in weighted group mean. Elemental abundances given in parentheses are excluded in the group mean. a Oxygen abundance by difference to 100%.'",
 "N row: 'N 2900 1 ... 2948 535 5 ... ... 2940 20 2' -> Alais 2900 (1 analysis), Orgueil 2948 +- 535 (5), group 2940 +- 20, N_met 2",
 "P row: 'P (1200 ) (1) (760) (1) 924 100 8 ... (480) (1) 920 100 1' -> Orgueil 924 +- 100 (8), group 920 +- 100, N_met 1 (Alais, Ivuna, Tonk excluded)",
 "As row: 'As 1.82 0.04 2 1.77 0.21 3 1.70 0.23 18 ... 1.95 1 1 .73 0.06 4' -> group 1.73 +- 0.06, N_met 4",
 "Ta row: 'Ta ... 0.014 3 1 0.014 5 0.0010 2 ... ... 0.014 4 0.000 1 2' -> group 0.0144 +- 0.0001, N_met 2",
 "Rb row: 'Rb (1.55 0.04) (2) 2.16 0.32 15 2.12 0.31 30 ... (< 4) (1) 2.13 0.02 2'",
 "Se row: 'Se 20.5 0.9 4 20.0 1.1 8 19.5 1.9 2 6 ... 21 1 19.7 0.4 4'",
 "H row: 'H 21800 1 20900 1 1973 0 2270 3 ... 2420 0 1 2101 5 1770 4' -> group 21015 +- 1770",
 "C row: '... 3518 0 4810 5' -> group 35180 +- 4810, N_met 5",
 "O row: 'O (4717 0) a 454,130 a 462,2 5 0 a (4 13,400) a (488,7 00) a 458,2 0 0 5750 2' -> group 458200 +- 5750 (by difference)",
 "K row: 'K 524 57 2 475 18 3 543 35 17 (800) (1 ) 510 1 530 24 4'",
 "Li row: 'Li ... 1.52 1 1 :45 0 :21 6 ... ... 1 :46 0 :03 2' -> group 1.46 +- 0.03",
 "S row: '... 5410 0 3650 5' -> group 54100 +- 3650",
]
T8_QUOTES = [
 "Table 8 title: 'TABLE 8 Equilibrium Condensation Temperatures for a Solar-System Composition Gas Element (1) TC (K) (2) Initial Phase {Dissolving Species} (3) 50% TC (K) (4) Major Phase(s) or Host(s) (5)'",
 "Table 8 note (p.1240): 'Note.—At 10 4 bar total pressure. Solar system abundances from Table 2. a 22.75% of oxygen is condensed into rock before water ice condensation. b Major condensed reservoir of element.' ('10 4' is the extraction of 10^-4)",
 "'P 1248 Fe3P 1229 Schreibersite' ; 'N 131 NH3H2O 123 NH3H2O' ; 'H 182 H2O ice ... ...' ; 'He <3 He ice ... ...' ; 'O 182 Water icea 180 rock + water ice'",
 "'Mg 1397 Spinel 1354 Forsteriteb 1336 Forsterite' ; 'Si 1529 Gehlenite 1354 Forsteriteb 1310 Forsterite + enstatite' ; 'Zr 1764 ZrO2 1741 ZrO2' ; 'Ne 9.3 Ne ice 9.1 Ne ice'",
 "'Li {Li4SiO4, Li2SiO3} 1142 Forsterite + enstatite' ; 'Cl 954 Na4[Al3Si3O12]Cl 948 Sodalite' ; 'Br {CaBr2} 546 Cl apatite' ; 'I {CaI2} 535 Cl apatite' ; 'Ta {Ta2O5} 1573 Hibonite + titanate' ; 'Au {Au} 1060 Fe alloy' ; 'Hg {HgS, HgSe, HgTe} 252 Troilite' ; 'Ar 48 Ar·6H2O 47 Ar·6H2O'",
]
HYP_QUOTES = {
 "pressure": "p.1236: 'The condensation temperatures and the 50% condensation temperatures are calculated for all elements at a total pressure of 10-4 bar. This pressure was chosen because it is characteristic for the total pressure near 1 AU in the solar nebula (see Fegley 2000).'",
 "photo": "p.1236: 'Condensation temperatures for the photospheric abundance set are not directly applicable to the solar nebula because of the slightly lower metallicity caused by gravitational settling'",
 "equil": "p.1238: 'For calculating standard condensation temperatures, condensates remain in equilibrium with the gas as temperature drops. ... This scenario applies to physical settings such as the solar nebula, protostellar and protoplanetary disks, and stellar outflows ... However, this condensation sequence does not apply to giant planetary, brown dwarf, or cool stellar atmospheres, in which gravitational settling removes primary condensates into cloud layers'",
 "host": "p.1238: 'the 50% condensation temperatures of trace elements are independent of their total solar system abundance but are dependent on the availability and amount of the major host phase, which do depend on the relative abundances of the major elements.'",
 "tenK": "p.1238: 'The condensation temperatures for the solar system composition with higher metallicity are generally somewhat larger (about 10 K) than those calculated for the photospheric composition.'",
 "Pdep": "p.1243: 'the troilite condensation temperature is independent of total pressure (for total pressures <10-2 bar), whereas the condensation temperature of metal decreases with decreasing total pressure. ... At 10-6 bar, their 50% condensation temperatures are 694 K (Te) and 634 K (Pb).'",
 "halo": "p.1243: 'Halogen condensation temperatures are among the more uncertain ones, and previously there were no or only uncertain condensation temperatures available for I and Br.' p.1244: 'In the absence of thermodynamic data for Br- and I-apatite, the Br and I condensation is modeled by assuming substitutions ... This leads to 50% condensation temperatures of ~546 K (Br) and ~535 K (I).'",
 "Be": "p.1242: 'Melilite ... serves as host phase for initial Be condensation ..., into which 50% of Be is condensed at 1421 K.' (Table 8 prints 'Be {BeCa2Si2O7} 1452 Melilite')",
 "O": "p.1244: 'About 23% of all oxygen is bound to rocky elements (Al, Ca, Mg, Si, and Ti) before water ice condenses at 182 K.'",
 "N": "p.1245: 'Under equilibrium conditions, ammonia hydrate (NH3H2O) condenses at 131 K by the reaction of ammonia gas and water ice, and 50% of all nitrogen is in this hydrate by 123 K. The kinetic inhibition of molecular nitrogen to ammonia gas formation ... is the other end-member case ... 50% of nitrogen is condensed by 52 K.'",
 "CIprim": "p.1221: 'CI chondrites are the most primitive chondrites in the sense that they are not chemically fractionated when relative abundances are compared to the photosphere. However, it should be noted that they are severely altered mineralogically from the \"pristine\" mineralogy expected for solar nebular condensates.'",
 "CIalt": "p.1224: 'aqueous alteration likely has led to redistribution of some elements such as S, Ca, and Mn within the CI chondrite parent body, and abundance determinations for some elements may have statistically larger uncertainties, which simply reflect sample heterogeneity introduced by parent body alterations. Here it should be noted that chondritic meteorites in their present form are not unaltered equilibrium condensates from the solar nebula.'",
 "CImethod": "p.1224: 'The CI chondrite group-mean composition (last columns in Table 3) was obtained by taking the weighted average of the compositions from the individual meteorites, using the number of analyses (N) as statistical weight. The uncertainties given are the square root of the weighted variance of the weighted average. Values in parenthesis in Table 3 are not included in the computation of the group mean.'",
 "P": "p.1234: 'the meteoritic value is only based on the P abundance in the Orgueil meteorite, for which a concentration of 920 ± 100 ppm is derived (mainly from data by Wolf & Palme 2001). The P abundances of other CI chondrites are much more uncertain; for Ivuna, one reliable P analysis of 760 ppm exists (Wolf & Palme 2001), whereas P analyses of other CI chondrites date back several decades to almost a century, and range from 500 to 1800 ppm (see Mason 1963).'",
 "falls": "p.1221: 'Only five CI meteorite falls are known, and of these, only four are massive enough for multiple chemical analyses.'",
}
LBP25 = ("Lodders, Bergemann & Palme 2025, arXiv:2502.10575 (Space Sci. Rev., accepted 7 Feb 2025), READ this session via alphaXiv answer_pdf_queries "
         "(pp.1, 22-23, 29, 33, 35, 70, 73, 75). Table 4 p.70: 'N 1965 970 49 22 206 10.5 428 37000 18200 D -33 ...' (1 SD 970, %SD 49, n 22, SE 206, quality D, -33% vs P14); "
         "'P 989 89 9.1 32 16 1.6 32 8410 760 B 0.4 ...'. Text p.29: 'All selected values provide the grand average N = 1965 ± 447 ppm for CI-chondrites.' "
         "Text p.33: 'The recommended concentration of P = 989 ± 63 ppm from 24 analyses'. Abstract: 'the CI-abundances of Hg and N are now significantly lower.' "
         "Both N uncertainties (970 and 447) are printed in the paper itself: Table 4's SD against the text's; this settles the relay disagreement recorded by the first audits.")
LFME24 = ("Lodders, Fegley, Mezger & Ebel 2024, arXiv:2411.01362, READ this session via alphaXiv (pp.1-2, 4-5, 28-29, 34-35, 39). Table 1 p.5 at log P = -2/-4/-6/-8: "
          "'P 1421 1273 1142 1029', 'N 139 124 111 101', 'Cl 460 418 383 354', 'Br 466 423 387 357', 'Li 1319 1152 1003 891', 'H 10.6 7.4 5.7 4.6', 'O 210 182 160 143'. "
          "p.28: '(3) Although widely assumed, a total pressure of 10-4 bar is model specific. Temperature and pressure varied with radial distance from the proto-Sun, height above the nebular midplane, and with temporal evolution'. "
          "p.29: 'There is no fundamental reason to expect a relationship between 50% condensation temperatures at any single total pressure and elemental abundances in the BSE or any meteorite parent body.' "
          "Abstract (5): 'volatility trends ... are qualitative indicators'. p.2: 'At 10-4 bar total pressure, refractory elements condense at T > 1300 – 1360 K, moderately volatile elements condense between 1300 and 660 K, and highly volatile elements condense below 660 K.'")

def write(key, obj):
    fn = D + key.replace("/", "_").replace("#", "_") + ".json"
    json.dump(obj, open(fn, "w"), indent=1, ensure_ascii=False)
    print("wrote", fn)

# ------------------------------------------------------------------ CI chondrite
ci = {
 "key": "lodders-2003-ci-chondrite",
 "name": "Lodders (2003), ApJ 591, 1220 -- CI chondrite bulk composition (as used by stockgate.py CHONDRITE and stock.py CHONDRITE)",
 "source": {
  "located": "K. Lodders, 'Solar System Abundances and Condensation Temperatures of the Elements', ApJ 591, 1220-1247 (2003); M-retrieved PDF on Google Drive " + FID + ". " + IDENT,
  "read_status": "READ (M-retrieved, Google Drive " + FID + ")",
  "via": "mcp__Google_Drive__read_file_content on " + FID + " (full text returned, saved to scratchpad reaudit/lodders2003.txt). Table 3 read in full (all rows H..U) for the first time in this docket; the first audit of this key had it CARRIED-FROM-SIBLING. LBP25 read directly this session (alphaXiv).",
  "read_status_detail": "Table 3 extraction is a rotated table; values reconstructed row by row. Ambiguous cells (Be, Ti, Th, U sigma/N_met) are flagged and no conclusion rests on them."
 },
 "pages_read": PAGES_COMMON,
 "published_statement": " | ".join([HYP_QUOTES["falls"], HYP_QUOTES["CIprim"], HYP_QUOTES["CImethod"], HYP_QUOTES["P"]] + T3_QUOTES),
 "published_hypotheses": [
  "H1 (READ) The CI composition is a group mean over five falls weighted by number of analyses, with parenthesised values excluded; its uncertainty is 'the square root of the weighted variance of the weighted average' (p.1224) -- i.e. a spread of meteorite means, not the analytical scatter within a meteorite.",
  "H2 (READ) Per-element support differs: P rests on ONE meteorite (Table 3 'N met' = 1; p.1234 'only based on the P abundance in the Orgueil meteorite'; other CI P analyses 'range from 500 to 1800 ppm'); N rests on TWO (Alais, a single analysis 2900; Orgueil 2948 +- 535 over 5 analyses), giving the group 2940 +- 20. The +-20 is far tighter than Orgueil's own 535.",
  "H3 (READ) CI chondrites are 'not chemically fractionated' relative to the photosphere for the rock-forming elements, but 'severely altered mineralogically' (p.1221); aqueous alteration redistributed S, Ca, Mn; they 'are not unaltered equilibrium condensates' (p.1224).",
  "H4 (READ) Values are mass concentrations of bulk meteorite ('ppm by mass = μg g−1', Table 3 note; O 'by difference to 100%'). The table describes five meteorites; it says nothing about any asteroid's accessible stock.",
 ],
 "hypothesis_drift": [
  "ATTRIBUTION DISCREPANCY, now CONFIRMED AT SOURCE (in the tree, not in Lodders). stockgate.py:284-285 and stock.py:195 credit CHONDRITE (stockgate.py:395-414; stock.py:216-219) to L03, but it is not L03 Table 3. Over the 60 elements both carry: 9 within 0.5%, 33 within L03's 1 sigma, 5 beyond 3 sigma: As 18.5 vs 1.73 +- 0.06 ppm (x10.69), Ta 0.01 vs 0.0144 +- 0.0001 ppm (x0.694), N 3180 vs 2940 +- 20 (x1.082), Rb 2.3 vs 2.13 +- 0.02 (x1.080), Se 21.2 vs 19.7 +- 0.4 (x1.076). P 1040 vs 920 +- 100 (x1.130, +1.2 sigma). Recorded, not repaired.",
  "DROPPED: the per-element support. The tree carries P at a point value with no note that L03's P is one meteorite (Orgueil) and that other CI P analyses span 500-1800 ppm (p.1234). Computed: with L03's other rows and P at 1800 ppm the CI binder would be N (8.736); at 500 ppm P (22.26).",
  "DROPPED: the uncertainties. 'Binds on PHOSPHORUS, not nitrogen' (stock.py:107-110; D25 via ledger.py:671-683) turns on CI N against the crossover N = P_CI x (payload N/P = 2.3077): 2400 ppm at the tree's P, 2123 at L03's. L03's group N (2940 +- 20) clears 2123 by 40.8 group sigma, but Orgueil's own scatter (2948 +- 535, 5 analyses) clears it by only 1.54 sigma.",
  "WEAKENED: stockgate.py:175-177 'A CI chondrite retained its volatiles'. The source calls CI 'not chemically fractionated' relative to the photosphere for rock-forming elements and 'severely altered mineralogically' (p.1221); its Table 3 H, C, N are bulk concentrations of hydrated, altered meteorites. The tree needs only CI N/P > 2.3077: L03 gives 2940/920 = 3.20; LBP25 gives 1965/989 = 1.99, which fails.",
  "ADDED by the tree (not in L03): that the CI group mean is the accessible stock of an asteroid destination (stock.py:112, 131-133). L03 averages five meteorite falls; LBP25 p.23 notes Ryugu and Bennu returned samples 'are similar to CI-chondrites in bulk chemical and isotopic composition' but does not discuss them. OPEN here.",
  "NORMALISATION (tree): stockgate.CHONDRITE sums to 1.006899 and is not renormalised; effect on the factor below 0.7%.",
  "SUBSET: stock.CHONDRITE's 16 entries equal stockgate's (checked by import)."
 ],
 "data_at_publication": [
  {"quantity": "CI P (sets the CI processing factor and the 749.08 kg figure)",
   "value_then": "L03 Table 3 group 920 +- 100 ppm, N_met 1 (Orgueil only) -- READ: 'P (1200 ) (1) (760) (1) 924 100 8 ... (480) (1) 920 100 1'. The tree uses 1040 attributed to L03.",
   "value_now": "989 +- 89 (LBP25 Table 4, 1 SD, quality B) / 989 +- 63 (LBP25 text p.33) -- READ",
   "source_now": "arXiv:2502.10575 Table 4 p.70, text p.33",
   "moves_conclusion": "The figure, not the binder: 749.08 kg (tree) -> 846.79 kg (L03 920) -> 787.7 kg (LBP25 989); L03 +-1 sigma spans 763.8-950.1 kg. The binder stays P under every L03 value."},
  {"quantity": "CI N (decides P vs N as binder)",
   "value_then": "L03 group 2940 +- 20 ppm (N_met 2; Orgueil 2948 +- 535, n 5) -- READ: 'N 2900 1 ... 2948 535 5 ... ... 2940 20 2'. The tree uses 3180.",
   "value_now": "1965 ppm, 1 SD 970 (Table 4, quality D, '-33' vs P14) or +- 447 (text p.29) -- READ",
   "source_now": "arXiv:2502.10575 Table 4 p.70, p.29, abstract",
   "moves_conclusion": "YES for the binder label. Crossover at LBP25 P is 2282 ppm; LBP25 N is below it by 0.33 SD (970), 0.71 (447) or 1.54 SE (206). With LBP25 N and P the binder is N at 13.070 (914.9 kg) and stockgate's regime label becomes VOLATILITY-LIMITED. The datum is quality D and its own band spans the crossover: contested."},
  {"quantity": "CI Ta (the DECLARED craft's binder)",
   "value_then": "L03 0.0144 +- 0.0001 ppm -- READ: 'Ta ... 0.014 4 0.000 1 2'. The tree uses 0.01 ppm (1 significant figure).",
   "value_now": "not re-read here",
   "source_now": "n/a",
   "moves_conclusion": "The figure only: craft factor 90,082 -> 62,557 (x0.694) under L03; binder stays Ta (computed)."},
  {"quantity": "CI As",
   "value_then": "L03 1.73 +- 0.06 ppm (READ); the tree 18.5",
   "value_now": "not needed",
   "source_now": "n/a",
   "moves_conclusion": "No conclusion rests on it; a factor-10 transcription discrepancy against the cited source."}
 ],
 "rederivation": {
  "method": "numeric",
  "script_path": SCRIPT,
  "outcome": "exit 0, all checks pass; output reaudit/lodders2003_reaudit.out. (1) stockgate.CHONDRITE vs L03 Table 3 (60 elements, read at source): 9 within 0.5%, 33 within 1 sigma, 5 beyond 3 sigma (N +12.0, Se +3.8, As +279.5, Rb +8.5, Ta -44.0 sigma). (2) Tree binder reproduced: P 10.701153, 749.08 kg per 70 kg. (3) With L03's P only or all L03 rows: P 12.0970, 846.79 kg; P at 920 +- 100: 10.911-13.572. (4) Crossover N = P_CI x 2.3077: 2400.0 (tree P), 2123.1 (L03), 2282.3 (LBP25). (5) L03 rows with P at 1800 ppm (L03's quoted older CI range): binder N 8.736. (6) LBP25 N 1965 + P 989: binder N 13.070 (914.9 kg). (7) Craft: Ta 90,082 -> 62,557 under L03.",
  "agrees_with_source": "partly (the tree's arithmetic is exact; its table is not the cited source's)"
 },
 "later_literature": [
  {"ref": "Lodders, Bergemann & Palme 2025, arXiv:2502.10575", "effect": "contested",
   "what": "Revised CI N 1965 ppm (SD 970, quality D, -33%) and P 989. Under it the tree's CI binder flips from P to N. Its N analyses of Orgueil 'vary from 800 to 8200 ppm in 20 analyses' (p.29).",
   "read_status": "READ this session (alphaXiv; pp.1, 22-23, 29, 33, 70, 73, 75). " + LBP25},
  {"ref": "Palme & O'Neill 2014; McDonough & Sun 1995 (CI columns)", "effect": "contested",
   "what": "As recorded by the first audit (package transcriptions): PON14 N 2950 +- 885 (2 sigma), MS95 N 3180 flagged factor-2. Not re-read here.",
   "read_status": "CARRIED from the first audit (pyrolite 0.3.7 data files)"},
  {"ref": "Ryugu (Hayabusa2) and Bennu (OSIRIS-REx) returned samples", "effect": "extends",
   "what": "LBP25 p.23: 'similar to CI-chondrites in bulk chemical and isotopic composition. These pristine samples are not discussed here'. Bearing on the tree's 'asteroid = CI stock' hypothesis; no values read.",
   "read_status": "NAMED (quoted from LBP25 p.23); values NOT READ"}
 ],
 "lacked_data": "Read at source, L03's own text already carries the fragility: P from one meteorite with other CI analyses spanning 500-1800 ppm (p.1234), and N from two meteorites with Orgueil's own 1 sigma at 535 ppm. What L03 lacked: the modern CI N compilation (LBP25: 20 Orgueil analyses from 800 to 8200 ppm, grand mean 1965) and ICP data for P (LBP25: 24 analyses, 989). FOR the hypothesis that later data move the tree: LBP25 N crosses the 2123-2400 ppm crossover and flips the binder to N at 13.07, VOLATILITY-LIMITED. AGAINST: LBP25 N is quality D with a band spanning the crossover; P moved only 920 -> 989; the major elements are within ~3%. No datum refutes L03's table as a 2003 group mean. Net: the binder label is sensitive to N; the tree's table is not L03's.",
 "grade": "DATA-DEPENDENT",
 "grade_evidence": "(i) L03 now READ at source: Table 3 prints P 920 +- 100 (N_met 1), N 2940 +- 20 (N_met 2), As 1.73 +- 0.06, Ta 0.0144 +- 0.0001. The tree's CHONDRITE is not this table (9/60 within 0.5%; five elements beyond 3 sigma; As x10.69). That is an attribution/transcription discrepancy in the tree, not an error in Lodders. (ii) The tree's result 'CI binder = P at 10.70' moves with CI N: the crossover is 2123 ppm at L03's own P. L03's group N clears it, but only by 1.54 sigma of Orgueil's own scatter, and L03's own statement that CI P spans 500-1800 ppm contains a flip at the high end. LBP25 (read) puts N at 1965 (quality D), below the crossover, making N the binder at 13.07. A tree label rests on a measured value that has changed and is contested: DATA-DEPENDENT. (iii) Not WRONG: nothing contradicts L03 at its hypotheses. (iv) Not NARROWED as primary: the verdicts built on the factor (asteroid beats cosmic/crust; stock need not travel) hold at 10.7-13.1.",
 "what_would_change_the_grade": "To STANDS: a settled CI N whose band clears ~2400 ppm (e.g. the announced Lodders et al. 2025b CI composition, or Ryugu/Bennu bulk N), plus the tree citing the composition it actually uses (it is not L03 Table 3) with its uncertainties. To WRONG: only a demonstrated error in L03 at its hypotheses; none found.",
 "reverify_command": REV,
 "report_path": D + "lodders-2003-ci-chondrite.json",
 "supersedes_grade": "DATA-DEPENDENT"
}
write(ci["key"], ci)

# ------------------------------------------------------------- condensation temps
tc = {
 "key": "lodders-2003-condensation-temperatures",
 "name": "Lodders (2003) 50% condensation temperatures at 1e-4 bar",
 "source": {
  "located": "K. Lodders, ApJ 591, 1220-1247 (2003), Table 8 (pp.1239-1240); M-retrieved PDF on Google Drive " + FID + ". " + IDENT,
  "read_status": "READ (M-retrieved, Google Drive " + FID + ")",
  "via": "mcp__Google_Drive__read_file_content on " + FID + ". Supersedes the first audit's READ-VIA-RESTATEMENT (0901.1149, 2301.03674, 1810.12741). LFME 2024 re-read this session via alphaXiv for the later values."
 },
 "pages_read": PAGES_COMMON,
 "published_statement": " | ".join([HYP_QUOTES["pressure"], HYP_QUOTES["equil"], HYP_QUOTES["host"]] + T8_QUOTES),
 "published_hypotheses": [
  "H1 (READ p.1236) total pressure fixed at 1e-4 bar, chosen as 'characteristic for the total pressure near 1 AU in the solar nebula'.",
  "H2 (READ, Table 8 note, p.1236, p.1238) a gas of solar-SYSTEM (protosolar, Table 2) composition; Table 9 is the photospheric set, 'about 10 K' lower; photospheric T_c 'not directly applicable to the solar nebula'.",
  "H3 (READ p.1238) full equilibrium: 'condensates remain in equilibrium with the gas as temperature drops'; applies to 'the solar nebula, protostellar and protoplanetary disks, and stellar outflows'; 'does not apply to giant planetary, brown dwarf, or cool stellar atmospheres'.",
  "H4 (READ p.1238) trace-element T50 depends on host-phase availability, not the element's own abundance; hosts chosen from meteorite mineral analyses; activity coefficients from earlier studies.",
  "H5 (READ pp.1243-1245) thermodynamic data of 2003; halogens 'among the more uncertain'; Br and I by assumed apatite substitution; Rb/Cs by assumed K-feldspar exchange (p.1243: 'Previously, the condensation temperatures of the heavy alkali elements Rb and Cs were uncertain or unknown').",
  "H6 (READ Table 8, p.1244-1245) H and He carry NO 50% value ('...'): H 182 K is the appearance T of H2O ice, He '<3'. O 180 K is 50% into 'rock + water ice' with 23% of O in rock. N 123 K assumes NH3 equilibrium; under kinetic inhibition N is 50% condensed by 52 K.",
  "H7 (READ p.1243) pressure dependence: metal condensation T falls with falling P; troilite T independent of P below 1e-2 bar; Te, Pb change host by 1e-6 bar."
 ],
 "hypothesis_drift": [
  "KEPT: H1. stockgate.py:330 header 'Lodders (2003) 50% condensation temperatures, K, at 1e-4 bar' and formation.py:501 LODDERS_PRESSURE_BAR = 1.0e-4.",
  "TRANSCRIPTION CONFIRMED AT SOURCE: 61 of the 63 element entries of stockgate.TCOND (:331-343) equal Table 8's 50% T_C exactly (Ne 9.1 -> 9). The first audit's unresolved restatement disagreements are resolved by the primary: Mg 1336, Si 1310 and Zr 1741 are Table 8's 50% values; the restatements' 1354 (Mg, Si) and 1764 (Zr) are the appearance temperatures of forsterite and ZrO2 printed in column (2).",
  "DROPPED H6 (label): stockgate.py:330 calls every entry a '50% condensation temperature', but Table 8 prints no 50% value for H ('H 182 H2O ice ... ...') or He ('He <3 He ice ... ...'); 182 is H2O-ice appearance and 3 is an upper bound written as a value. Plus a sentinel key 'Ni_': 0. No conclusion uses H, He or O via TCOND.",
  "EXTENDED BEYOND H1/H3 at stockgate.py:182-184: 'Retaining volatiles is a statement about formation temperature, hence orbital radius' and 'THE SNOW LINE IS THEREFORE THE SELECTOR'. The source fixes P at the value 'characteristic ... near 1 AU' (p.1236) and supplies no T(a), P(a); the snow-line step is the owner's. formation.py:271-279 already concedes this ('REFUSED to compute a radius: it would use a nebular T_c outside its pressure hypothesis').",
  "EXTENDED BEYOND H3: stockgate.volatility_regime() (:738-751) labels 'Jupiter (3x solar)' from T_c; the source says its condensation sequence 'does not apply to giant planetary ... atmospheres' (p.1238). The label uses T_c only as a volatility index of the binder element, so it is a rank use, which LFME 2024 calls qualitative.",
  "WEAKENED (proxy): Earth's continental crust labelled VOLATILITY-LIMITED from N's nebular 123 K. LFME 2024 p.29: 'no fundamental reason to expect a relationship between 50% condensation temperatures at any single total pressure and elemental abundances in the BSE or any meteorite parent body.' The owner states the label is from 'T_c alone' (:180).",
  "ADDED (owner's): VOLATILE_CUT = 500 K (:735) is not a Lodders boundary. L03 uses troilite (664 K) to separate moderately volatile from volatile (p.1239: 'elements condensing below troilite are \"volatile\" or \"highly volatile\"'); LFME 2024 p.2 puts highly volatile below 660 K. OXIDE_O and 'all leftover O -> water ice' in Finding G are also the owner's; L03 counts 23% of O in rock at water-ice condensation (p.1244).",
  "DROPPED H5 (currency): the table is the 2003 edition, transcribed exactly, not flagged as revised by LFME 2024 / LF 2023.",
  "INTERNAL TO THE SOURCE (recorded): p.1242 gives Be 50% at 1421 K; Table 8 prints 1452 K. The tree uses the table value."
 ],
 "data_at_publication": [
  {"quantity": "T_c(P), binder of photosphere / Jupiter / CI chondrite", "value_then": "1229 K -- READ: 'P 1248 Fe3P 1229 Schreibersite'",
   "value_now": "1273 K at 1e-4 bar; 1421/1142/1029 K at 1e-2/1e-6/1e-8 -- READ: 'P 1421 1273 1142 1029'", "source_now": "arXiv:2411.01362 Table 1 p.5",
   "moves_conclusion": "No. ABUNDANCE-LIMITED at every value; lowest 1029 K is 529 K above the 500 K cut."},
  {"quantity": "T_c(N), binder of Earth's continental crust", "value_then": "123 K (equilibrium NH3.H2O); 52 K under kinetic inhibition (p.1245) -- READ",
   "value_now": "124 K at 1e-4 bar; 139/111/101 K -- READ: 'N 139 124 111 101'", "source_now": "arXiv:2411.01362 Table 1 p.5",
   "moves_conclusion": "No. VOLATILITY-LIMITED at every value and under either kinetic end-member."},
  {"quantity": "T_c(Cl), T_c(Br)", "value_then": "948 K (sodalite), 546 K (assumed apatite) -- READ",
   "value_now": "418 K, 423 K at 1e-4 bar -- READ: 'Cl 460 418 383 354', 'Br 466 423 387 357'", "source_now": "arXiv:2411.01362 Table 1 p.5",
   "moves_conclusion": "Both cross the 500 K cut and leave Finding G's refractory sum; the first audit computed -0.253% (refractory) with I, In, Tl included (I, In, Tl 2024 values CARRIED, not re-read: p.6 not returned)."},
  {"quantity": "T_c(Li), photosphere co-binder", "value_then": "1142 K -- READ", "value_now": "1152 K -- READ: 'Li 1319 1152 1003 891'", "source_now": "arXiv:2411.01362 Table 1", "moves_conclusion": "No."},
  {"quantity": "T_c(H)", "value_then": "no 50% value; 182 K appearance of H2O ice -- READ", "value_now": "7.4 K fictive H2 ice -- READ: 'H 10.6 7.4 5.7 4.6'", "source_now": "arXiv:2411.01362 Table 1, p.4", "moves_conclusion": "No; a definition, not a measurement; no conclusion uses it."},
  {"quantity": "nebular total pressure", "value_then": "1e-4 bar, 'near 1 AU' (p.1236)", "value_now": "'model specific' (LFME 2024 p.28)", "source_now": "arXiv:2411.01362 p.28",
   "moves_conclusion": "Not the regime labels (checked at all four pressures by the first audit; P and N re-read here). It is why the source does not carry the snow-line/radius step."}
 ],
 "rederivation": {
  "method": "numeric", "script_path": SCRIPT,
  "outcome": "exit 0. (1) TCOND vs Table 8 read at source: 61/63 exact; H and He have no 50% value in Table 8; sentinel 'Ni_'. (2) Regime labels reproduced: photosphere, Jupiter, CI on P (Table 8: 1229 K) ABUNDANCE-LIMITED; crust on N (123 K) VOLATILITY-LIMITED. (3) condensed_budget reproduced: refractory 3.2498e-3, rock 4.9690e-3, rock+ice 9.4877e-3, gas 0.990512 (stockgate.py:200 prints '99.06 %', a rounding discrepancy carried from the first audit). The 2024-table and cut-window sensitivities of the first audit (cut anywhere in (139, 1029] K) are not re-run; their P and N inputs are confirmed above.",
  "agrees_with_source": "yes (transcription); the snow-line/orbital-radius step and the Jupiter label go beyond the source's stated scope"
 },
 "later_literature": [
  {"ref": "Lodders, Fegley, Mezger & Ebel 2024, arXiv:2411.01362", "effect": "narrows", "what": "Updated T50 at 1e-2..1e-8 bar; 1e-4 bar 'model specific'; volatility plots 'qualitative'; no fundamental T50-abundance relation for any parent body.", "read_status": "READ this session. " + LFME24},
  {"ref": "Lodders & Fegley 2023, arXiv:2301.03674", "effect": "narrows", "what": "Halogen revision (Cl 427 K, Br 392 K, I 312 K per the first audit).", "read_status": "CARRIED from the first audit (READ there, pp.1-2, 40-47)"},
  {"ref": "Spaargaren et al. 2025, arXiv:2509.03724", "effect": "narrows", "what": "T_c shifts of 40-200 K with disc composition and pressure (first audit).", "read_status": "CARRIED from the first audit"}
 ],
 "lacked_data": "L03 itself names what it lacked: reliable halogen data ('among the more uncertain'; Br, I by assumed apatite substitution), Rb/Cs feldspar data (modelled by analogy to K), and kinetics for C and N (two end-members given). The later same-group revisions moved exactly those (Cl -530 K, Br -123 K; H redefined). FOR the hypothesis: five elements the tree counts refractory now fall below its 500 K cut. AGAINST it mattering: the two binders moved +44 K (P) and +1 K (N); every regime label survives every revision and pressure. The gap that bears on the tree is not a Lodders datum: the disc T(a), P(a) needed for 'snow line = selector', which L03 never supplies and formation.py refuses to invent.",
 "grade": "NARROWED",
 "grade_evidence": "READ at source: the tree transcribes Table 8 exactly (61/63; H and He mislabelled as 50% values), and every regime label holds under the 2003 and 2024 values. But the tree uses the T_c beyond the source's stated scope in two places: stockgate.py:182-184 turns a 1e-4 bar ('near 1 AU') equilibrium T_c ranking into 'formation temperature, hence orbital radius ... THE SNOW LINE IS THEREFORE THE SELECTOR', for which the source supplies no T(a), P(a); and volatility_regime() labels a giant planet although the source says the sequence 'does not apply to giant planetary ... atmospheres'. The labels themselves are a rank use the authors call qualitative. True at a weaker strength than the tree states: NARROWED. Not WRONG (no error in L03 at its hypotheses); not DATA-DEPENDENT (no revision crosses the cut for a binder).",
 "what_would_change_the_grade": "To STANDS: restate stockgate.py:182-184 as conditional on a formation-epoch disc model (as formation.py does) and name the regime labels as qualitative ranks. To DATA-DEPENDENT: a revision dropping T_c(P) by >529 K below its 1e-8 bar value, or raising T_c(N) above 500 K; none read.",
 "reverify_command": REV,
 "report_path": D + "lodders-2003-condensation-temperatures.json",
 "supersedes_grade": "NARROWED"
}
write(tc["key"], tc)

# ---------------------------------------------------------------- composite apj
apj = {
 "key": "lodders-2003-apj-591-1220",
 "name": "Lodders 2003: CI chondrite abundances and 50% condensation temperatures at 1e-4 bar",
 "source": {
  "located": "Lodders K. (2003) ApJ 591, 1220-1247, doi:10.1086/375492; M-retrieved PDF on Google Drive " + FID + ". " + IDENT,
  "read_status": "READ (M-retrieved, Google Drive " + FID + ")",
  "via": "mcp__Google_Drive__read_file_content on " + FID + ". The first audit read the IOP PDF through alphaXiv; every value it quoted from Tables 3 and 8 and from pp.1236, 1238, 1242-1243 is confirmed against this copy, and Table 3 is now read in full (rows after Ag were not read before)."
 },
 "pages_read": PAGES_COMMON,
 "published_statement": " | ".join([HYP_QUOTES["pressure"], HYP_QUOTES["equil"], HYP_QUOTES["P"], T3_QUOTES[2], T3_QUOTES[3], T3_QUOTES[4], T8_QUOTES[1], T8_QUOTES[2]]),
 "published_hypotheses": [
  "H1 total pressure 1e-4 bar, 'characteristic for the total pressure near 1 AU in the solar nebula' (p.1236, READ)",
  "H2 solar-system (protosolar, Table 2) composition for Table 8; photospheric Table 9 'about 10 K' lower (p.1238, READ)",
  "H3 full equilibrium; 'does not apply to giant planetary, brown dwarf, or cool stellar atmospheres' (p.1238, READ)",
  "H4 trace elements in chosen host phases; T50 'independent of their total solar system abundance' (p.1238, READ)",
  "H5 2003 thermodynamic data; halogens 'among the more uncertain' (p.1243, READ); Hg 'problematic' (p.1243)",
  "H6 pressure dependence of metal vs troilite hosts (p.1243, READ)",
  "H7 CI values are N-weighted means of meteorite means over the five falls; parenthesised values excluded; P from Orgueil alone (N_met 1), N from two meteorites (p.1224, p.1234, Table 3, READ)"
 ],
 "hypothesis_drift": [
  "KEPT, exact: H1. formation.py:501 LODDERS_PRESSURE_BAR = 1.0e-4 and stockgate.py:284-285 SOURCES['L03'] '... 50% condensation temperatures at 1e-4 bar'. formation.py:271-274 calls them 'nebular'; the source's reason (p.1236) supports that, and ties the pressure to ~1 AU.",
  "DROPPED H2: stockgate.py:330 does not name the solar-system composition; the values are Table 8, not Table 9 (checked: 61/63 equal Table 8). No effect on D25, since formation refuses T_c at the destination.",
  "DROPPED H3/H4 at stockgate.py:166-184 and :735-751 (labels, snow-line selector, Jupiter labelled despite H3's exclusion of giant-planet atmospheres). See lodders-2003-condensation-temperatures.",
  "DISCREPANCY (label): TCOND H = 182 and He = 3 are appearance values; Table 8 prints '...' in the 50% column for both.",
  "DISCREPANCY (attribution), confirmed on the full Table 3: stockgate.CHONDRITE is not L03 Table 3 -- 9 of 60 within 0.5%; As x10.69, Ta x0.694, N x1.082, Rb x1.080, Se x1.076 all beyond 3 sigma; P x1.130 (+1.2 sigma). Sum 1.006899, not renormalised.",
  "DROPPED H7: L03's P is one meteorite, and L03 says other CI P analyses 'range from 500 to 1800 ppm' (p.1234); N's +-20 is the spread of two meteorite means while Orgueil's own 1 sigma is 535 (Table 3).",
  "ADDED by the tree: formation.py:271-277 requires the formation-epoch disc T(a), P(a) to turn 'primitive' into a radius -- consistent with H1/H6 and LFME 2024 p.28.",
  "INTERNAL to the source: p.1242 Be 50% 'at 1421 K' vs Table 8 1452 K (confirmed on this copy)."
 ],
 "data_at_publication": [
  {"quantity": "total pressure", "value_then": "1e-4 bar (p.1236, READ)", "value_now": "'model specific'; tabulated 1e-2..1e-8 bar (LFME 2024 p.28, Table 1, READ)", "source_now": "arXiv:2411.01362", "moves_conclusion": "No. A hypothesis carried correctly; its dependence (P 1421/1273/1142/1029 K) strengthens formation's refusal."},
  {"quantity": "50% T_c of P", "value_then": "1229 K (READ)", "value_now": "1273 K (READ)", "source_now": "arXiv:2411.01362 Table 1", "moves_conclusion": "No; far above 500 K."},
  {"quantity": "50% T_c of Cl, Br", "value_then": "948, 546 K (READ)", "value_now": "418, 423 K (READ)", "source_now": "arXiv:2411.01362 Table 1", "moves_conclusion": "Cross the cut; no regime label changes; Finding G moves in the 4th figure."},
  {"quantity": "50% T_c of N", "value_then": "123 K (READ)", "value_now": "124 K (READ)", "source_now": "arXiv:2411.01362 Table 1", "moves_conclusion": "No."},
  {"quantity": "CI P (sets 749.08 kg)", "value_then": "L03 920 +- 100 ppm, N_met 1 (READ). Tree uses 1040, attributed to L03.", "value_now": "989, SD 89 (Table 4) / +-63 (p.33) (READ)", "source_now": "arXiv:2502.10575", "moves_conclusion": "The figure, not a verdict: 749.08 (tree) / 846.79 (L03) / 787.7 kg (LBP25)."},
  {"quantity": "CI N", "value_then": "L03 2940 +- 20 (N_met 2; Orgueil 2948 +- 535) (READ). Tree uses 3180.", "value_now": "1965, SD 970, quality D (Table 4) / +-447 (p.29) (READ)", "source_now": "arXiv:2502.10575", "moves_conclusion": "YES for stockgate's CI label: binder N at 13.07 (914.9 kg), VOLATILITY-LIMITED; the datum is contested (its band spans the 2282 ppm crossover). D25's OPEN verdict does not move."}
 ],
 "rederivation": {
  "method": "numeric", "script_path": SCRIPT,
  "outcome": "exit 0, all checks pass (reaudit/lodders2003_reaudit.out). Pressure constant and SOURCES as p.1236; TCOND 61/63 = Table 8; CHONDRITE vs full Table 3 9/60 within 0.5%, 5 beyond 3 sigma; tree binder P 10.70115 (749.08 kg); L03 rows P 12.097 (846.79 kg); crossover 2123/2282/2400 ppm; LBP25 N binder 13.070; regime labels and condensed_budget reproduced; craft Ta 90,082 -> 62,557 under L03.",
  "agrees_with_source": "partly"
 },
 "later_literature": [
  {"ref": "Lodders, Fegley, Mezger & Ebel 2024, arXiv:2411.01362", "effect": "extends", "what": "Updated T50 at four pressures; 1e-4 bar model specific.", "read_status": "READ this session. " + LFME24},
  {"ref": "Lodders, Bergemann & Palme 2025, arXiv:2502.10575", "effect": "narrows", "what": "Revised CI: N 1965 (quality D), P 989.", "read_status": "READ this session. " + LBP25},
  {"ref": "Lodders & Fegley 2023, arXiv:2301.03674", "effect": "narrows", "what": "Halogen T_c revision.", "read_status": "NAMED-NOT-READ here (values via LFME 2024 Table 1)"}
 ],
 "lacked_data": "As the first audit: post-2003 CI analyses (LBP25's N and P), revised halogen thermodynamics, returned samples. Read at source, L03 already flags the weak points it lacked data for: one-meteorite P, 'much more uncertain' other CI P values, halogens 'among the more uncertain', kinetics of C/N. FOR: CI N moved enough to flip the tree's CI binder (contested, quality D); Cl/Br T50 fell by 530/123 K. AGAINST: rock-forming T50 moved <= 44 K; every regime label holds; CI P moved 920 -> 989. No datum refutes the 2003 result; one tree label rests on a moved, contested datum.",
 "grade": "DATA-DEPENDENT",
 "grade_evidence": "Confirmed on the primary. CONDENSATION TEMPERATURES: Table 8 transcribed 61/63; 1e-4 bar carried exactly; D25's refusal (formation.py:271-279) is consistent with p.1236 ('near 1 AU') and p.1243 (pressure dependence). That half STANDS for D25 (see lodders-2003-condensation-temperatures, NARROWED, for stockgate's snow-line prose). CI CHONDRITE: the tree's table is not L03's (full Table 3 now read); under L03's own values the CI factor is 12.10 not 10.70, binder unchanged. The CI binder label moves with CI N, which LBP25 (read) places below the crossover at quality D. A tree conclusion moves with a datum that has moved and is contested: DATA-DEPENDENT. Not WRONG.",
 "what_would_change_the_grade": "To STANDS: a settled CI N above ~2400 ppm, and the tree citing the composition it actually uses. To WRONG: a demonstrated error in L03 under its hypotheses; none found.",
 "reverify_command": REV,
 "report_path": D + "lodders-2003-apj-591-1220.json",
 "supersedes_grade": "DATA-DEPENDENT"
}
write(apj["key"], apj)
