import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/reaudit/"
FI = "1BZAg4Dncc5sTu00aTRPr7uBUvtT5awH-"
FL = "1dxtorrPjr43Bu7Jaq3TdGI8t0ADCd22N"
SI = D + "icrp23_reaudit.py"
SL = D + "lodders2003_reaudit.py"
IDENT = ("Drive file 'P_023_1975_Report_on_the_Task_Group_on_Reference_Man_rev0.pdf' (26,505,556 bytes). Its title page reads: "
         "'INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION No. 23 Report of the Task Group on Reference Man A REPORT PREPARED BY A TASK GROUP OF COMMITTEE 2 ... "
         "ADOPTED BY THE COMMISSION IN OCTOBER, 1974 W. S. Snyder Chairman M. J. Cook E.S. Nasset L. R. Karhausen G. Parry Howells I. H. Tipton ... PERGAMON PRESS ... "
         "First edition 1975 Reprinted 1992'. It is the cited work (a 1992 reprint of the 1975 first edition).")
PAGES = ("PARTIAL. mcp__Google_Drive__read_file_content returned 151,684 characters that END at report p.61; mcp__Google_Drive__download_file_content refused "
         "('File too large for download, over limit of 10 MB'); the file is private, so no other route was tried. READ: title page and imprint; Contents pp.v-xix "
         "(including the Chapter 2 entry 'GROSS AND ELEMENTAL CONTENT OF REFERENCE MAN I. Introduction 273 II. Physical Properties, Blood Content, and Gross and Elemental "
         "Content of Reference Man 274 Addendum I. Weights of Organs and Tissues of Reference Man 325 Addendum II. Variation of Elemental Concentration with Age 329 References 331'); "
         "Introduction pp.1-7 (definition of Reference Man, p.4; chapter responsibilities, p.6); Chapter 1 pp.8-61 (total-body weight p.13; adult gross composition p.24; "
         "figure and table pages from ~p.56 on are OCR-garbled). NOT READ: pp.62-480 -- in particular ALL of Chapter 2 (pp.273-334), which holds the whole-body elemental "
         "content the tree cites (P, N, K, Li, O, C and every other gram value), Chapter 3 (pp.335-420, intake/excretion incl. 'Summary of Model Values for Daily Balance "
         "of Elements'), and the appendices. No elemental mass in the tree is checked against ICRP 23 in this re-audit.")
Q = {
 "def": "p.4: 'Reference Man is defined as being between 20-30 years of age, weighing 70 kg, is 170 cm in height, and lives in a climate with an average temperature of from 10° to 20° He is a Caucasian and is a Western European or North American in habitat and custom.' (OCR renders '170 cn-i' and the degree signs as '\\~')",
 "sigfig": "p.4: 'Because of the wide range of individual variation and the fact that characteristics of Reference Man are chosen within those limits with some degree of arbitrariness and because estimates of intake to produce a specified dose commitment, or equivalent MPAIs, are often only specified to one significant figure, it is clear that minor changes in the definition to bring it into precise agreement with national or regional averages are not warranted.'",
 "notavg": "p.4: '(c) The Task Group agreed that it was not feasible to define Reference Man as an \"average\" or a \"median\" individual of a specified population group ... The available data certainly do not represent a random sample of any specified population. ... Only a very few individuals of any population will have characteristics which approximate closely those of Reference Man, however he is defined.'",
 "ch2": "p.6: 'Chapter 2: data relating to elemental composition of tissues and the whole body' ... 'Chapter 2, I. H. Tipton'",
 "mass": "p.13: 'The data of Stoudt et al. ... for the adult are as follows: Male: mean = 71.7 kg; SD = ±10 kg. Female: mean = 56.7 kg; SD = ±8.6 kg.' ... 'Weight of total body for reference adult male: 70 kg female: 58 kg'",
 "gross": "p.24 '(2) Adult. Water: Protein: Fat: Carbohydrate: Ash: Mineral: Blood: 60 % W (see pp. 27-29). 15-20% W (...). 19 % W (see pp. 40-42). 0.6% W (ref. 857, p. 381). 4.8-5.8 % W (...). 5.8 % W (ref. 129, p. 122). 7.9 % W (see p. 33).' (OCR separates labels from values; paired in printed order)",
}
REPORT = ("First-audit context kept where not contradicted: ICRP's own web page says P23 'is supplemented and amended by ICRP Publication 89' (READ by the first audit); "
          "ICRP 110 whole-body bulk from Kanematsu arXiv:1508.00226 Table I (READ by the first audit); Emsley via the Wikipedia restatement (tertiary, READ by the first audit).")

def write(key, obj):
    json.dump(obj, open(D + key.replace('/', '_').replace('#', '_') + ".json", "w"), indent=1, ensure_ascii=False)
    print("wrote", key)

icrp = {
 "key": "icrp-23-reference-man",
 "name": "ICRP Publication 23 (Reference Man) / Emsley, Nature's Building Blocks -- elemental composition of a 70 kg reference adult",
 "source": {
  "located": "ICRP Publication 23 (1975), Report of the Task Group on Reference Man, Pergamon; M-retrieved scan on Google Drive " + FI + ". " + IDENT + " Emsley, Nature's Building Blocks (2011) p.83: not supplied, not read.",
  "read_status": "PARTIAL -- READ (M-retrieved, Google Drive " + FI + ") for front matter, Introduction and Chapter 1 pp.1-61 only; the elemental-content chapter (pp.273-334) was NOT returned by the Drive text tool and is NAMED-NOT-READ. Emsley NAMED-NOT-READ.",
  "via": "mcp__Google_Drive__read_file_content (truncated at p.61, 151,684 chars; saved to scratchpad reaudit/icrp23.txt). download_file_content refused over 10 MB. " + REPORT
 },
 "pages_read": PAGES,
 "published_statement": " | ".join([Q["def"], Q["mass"], Q["sigfig"], Q["notavg"], Q["ch2"], Q["gross"]]) + " | ICRP 23's own whole-body gram table (Chapter 2) NOT READ; no gram value is quoted from it.",
 "published_hypotheses": [
  "H1 (READ p.4) Reference Man is one DEFINED individual: 20-30 y, 70 kg, 170 cm, Caucasian, Western European / North American habitat, 10-20 °C climate.",
  "H2 (READ p.13) 70 kg is the reference adult MALE; ICRP 23 defines a reference adult FEMALE at 58 kg. The 70 kg was chosen against data 'Male: mean = 71.7 kg; SD = ±10 kg'.",
  "H3 (READ p.4) Reference Man is NOT an average or median of any population; the data 'do not represent a random sample'; characteristics are chosen 'with some degree of arbitrariness'; derived intakes are 'often only specified to one significant figure'.",
  "H4 (READ p.24) adult gross composition: water 60 % W, fat 19 % W, protein 15-20 % W, ash 4.8-5.8 % W -- the elemental masses in Chapter 2 belong to this body.",
  "H5 (NOT READ) whatever uncertainty, age dependence (Chapter 2 Addendum II 'Variation of Elemental Concentration with Age', p.329) or per-element provenance Chapter 2 attaches to each element."
 ],
 "hypothesis_drift": [
  "DROPPED 'male', now CONFIRMED AT SOURCE. stockgate.py:288-289 and :345 say 'reference 70 kg adult'; stock.py:196-197 'reference adult'; ledger.py:674 'A reference adult (ICRP)'. ICRP 23 p.13 prints 'Weight of total body for reference adult male: 70 kg female: 58 kg', so the 70 kg body is the male; 'adult' is a wider class than the source's 70 kg object.",
  "DROPPED the source's precision statement (H3, READ). stockgate.py:53-55 reports Li at '91.758 %' of P's factor and calls it 'Nine per cent from flipping the answer'; the computed flip margins are +8.98 % (Li) and -8.24 % (P). The source says Reference Man's characteristics are chosen 'with some degree of arbitrariness' from a population with SD ±10 kg in body mass alone, and are not an average of anyone. A 9 % margin is finer than the definition claims to be.",
  "WEAKENED: 'measured' (stockgate.py:36 'a reference adult has measured quantities of 59'). The source says its values are selected, not averaged or median, from non-random data (p.4). Whether Chapter 2 prints all 59 elements, and which, is NOT READ.",
  "WEAKENED: attribution. stockgate.py:288/:345 and stock.py:196 cite 'ICRP 23 / Emsley' as one table; per-element provenance is not given. Still uncheckable: Chapter 2 not read, Emsley not supplied.",
  "CORRECTION to the first audit's citation: the definition it quoted as 'ICRP 23 p.335' (via Wikipedia) is on p.4 of the report itself; p.335 is the start of Chapter 3 ('PHYSIOLOGICAL DATA FOR REFERENCE MAN ... 335' in Contents).",
  "DROPPED currency (carried, not re-read): ICRP's page says P23 'is supplemented and amended by ICRP Publication 89'; no owner names it.",
  "TRIVIAL: stock.HUMAN is normalised over 70,085.9 g, so K at 70 kg is 139.83 g, not exactly 140 (stock.py:472-473)."
 ],
 "data_at_publication": [
  {"quantity": "Reference body mass", "value_then": "70 kg, reference adult MALE (p.13, READ); female 58 kg (p.13, READ)", "value_now": "ICRP 89 revises the reference male (per the first audit, via restatement: +3 kg); ICRP 89 NOT READ", "source_now": "icrp.org page (first audit)", "moves_conclusion": "No for per-kg processing factors. The tree's 59-row total 70,085.9 g matches the male. A 58 kg female payload would need 620.7 kg at the tree's CI factor (not a tree figure)."},
  {"quantity": "Total-body P, N, K, Li, O, C (the binder and runners-up)", "value_then": "NOT READ in ICRP 23 (Chapter 2 not returned). The tree carries P 780 g, N 1800 g, K 140 g, Li 0.007 g.", "value_now": "first audit: ICRP 110 whole body P 0.813 %, N 2.40 %, C 31.6 % (Kanematsu arXiv:1508.00226, READ there); Emsley restatement's fraction column P 0.5-0.7 %, Li 2.17 mg (tertiary)", "source_now": "CARRIED from the first audit", "moves_conclusion": "YES (first audit, reproduced here): the photosphere binder passes P -> Li below P 715.7 g or above Li 7.629 mg; the CI binder passes P -> N below P 588.7 g. ICRP 110 bulk makes Li (photosphere) and C (CI) bind."},
  {"quantity": "Adult gross composition", "value_then": "water 60 % W, fat 19 % W, protein 15-20 % W, ash 4.8-5.8 % W (p.24, READ)", "value_now": "not re-read", "source_now": "n/a", "moves_conclusion": "Context only: states the body whose elements Chapter 2 tabulates; the first audit's note that ICRP 110 prices a different (50/50 M/F) body stands."}
 ],
 "rederivation": {
  "method": "numeric", "script_path": SI,
  "outcome": "exit 0, 4/4 checks pass (reaudit/icrp23_reaudit.out). The tree's 59-row total 70,085.9 g equals ICRP 23's reference adult MALE mass (p.13) to 0.12 %; stock.HUMAN equals the 59-row fractions to 6 dp; CI binds P 10.701 (N 8.0763), photosphere P 1910.9 (Li 1753.4); flip thresholds reproduce: Li > 7.6288 mg (x1.0898), photosphere P < 715.7 g (x0.9176), CI P < 588.7 g (x0.7547). No ICRP 23 elemental value could be compared (Chapter 2 not read).",
  "agrees_with_source": "partly (body-mass hypothesis matches the male; elemental values unchecked)"
 },
 "later_literature": [
  {"ref": "ICRP Publication 89 (2002)", "effect": "narrows", "what": "Supplements and amends P23 (ICRP page, first audit). A WebSearch this session found that it gives body content of 13 elements, but no numeric value was read.", "read_status": "NAMED-NOT-READ"},
  {"ref": "Kanematsu 2015, arXiv:1508.00226 (ICRP 110 tissues)", "effect": "contested", "what": "Whole-body P 0.813 %, N 2.40 %, C 31.6 % (computed by the first audit); a different reference population.", "read_status": "CARRIED from the first audit (READ there)"},
  {"ref": "Emsley 2011 via Wikipedia 'Composition of the human body'", "effect": "contested", "what": "Mass column matches the tree in 54/56 rows; its fraction column gives P 0.5-0.7 % and Li 2.17 mg.", "read_status": "CARRIED from the first audit (tertiary)"}
 ],
 "lacked_data": "Read at source, ICRP 23 states its own limits: a single defined male chosen 'with some degree of arbitrariness' from non-random, Western data, 'not ... an average or median', to about one significant figure for derived intakes (p.4), with a separate 58 kg female (p.13). What it lacked (per the first audit, not re-read): in vivo data for women and other populations (Ellis 1990), the ICRP 89 revision, ICRP 110 tissues. FOR the hypothesis that later data move the tree: ICRP 110 bulk and the Emsley fraction column each flip a binder. AGAINST: magnitudes move by at most ~1.2x, and part of the move is a change of reference body, not a correction of ICRP 23. The elemental values themselves could not be checked against ICRP 23.",
 "grade": "DATA-DEPENDENT",
 "grade_evidence": "(1) New at source: the 70 kg body is ICRP 23's reference adult MALE (p.13), defined, not averaged, and selected with 'some degree of arbitrariness' (p.4). The tree drops 'male' and treats a defined individual's element masses as fixed to better than 9 %. (2) The tree's arithmetic reproduces exactly; the binder at the photosphere sits +8.98 % (Li) / -8.24 % (P) from a flip, at CI -24.5 % (P). (3) Data that have moved or are contested (ICRP 110 bulk; Emsley's own fraction column; carried from the first audit) cross those margins. A tree conclusion (the printed binder) rests on values that are contested: DATA-DEPENDENT, unchanged. (4) Not WRONG: nothing read contradicts ICRP 23. (5) The ICRP 23 component that would settle the P and Li values -- Chapter 2 -- remains NAMED-NOT-READ; this re-audit could not move the grade toward STANDS or NARROWED on the elemental values.",
 "what_would_change_the_grade": "Read ICRP 23 Chapter 2 (pp.273-334; the text tool truncated at p.61 and the 10 MB download cap blocked the file -- M could split the PDF or place pp.273-334 as a separate file) and Emsley p.83. If ICRP 23 prints P >= 716 g and Li < 7.63 mg for the 70 kg male, the photosphere binder holds for Reference Man and the grade becomes NARROWED (true for the defined male, not for 'an adult'). If ICRP 23 prints P < 716 g or Li > 7.63 mg, D25's printed photosphere binder is contradicted for the tree's own cited source (recorded, not repaired).",
 "reverify_command": "PYTHONDONTWRITEBYTECODE=1 python3 " + SI,
 "report_path": D + "icrp-23-reference-man.json",
 "supersedes_grade": "DATA-DEPENDENT"
}
write(icrp["key"], icrp)

comp = {
 "key": "icrp-reference-adult-and-ci-chondrite",
 "name": "ICRP reference adult composition; CI chondrite and stellar photosphere abundances (composite, as D25 uses them)",
 "source": {
  "located": "(a) ICRP Publication 23 (1975), Drive " + FI + " -- " + IDENT + " (b) Lodders 2003, ApJ 591, 1220, Drive " + FL + " -- title page 'SOLAR SYSTEM ABUNDANCES AND CONDENSATION TEMPERATURES OF THE ELEMENTS', 'Katharina Lodders', 'The Astrophysical Journal, 591:1220–1247, 2003 July 10'. (c) Asplund et al. 2009 (photosphere): not supplied by M; carried from audits/0909.0948.json.",
  "read_status": "MIXED: L03 READ (M-retrieved, Google Drive " + FL + "), Table 3 in full; ICRP 23 PARTIAL -- READ (M-retrieved, Google Drive " + FI + ") pp.1-61 only, elemental Chapter 2 NAMED-NOT-READ; A09 CARRIED from sibling audit (READ there); LBP25 READ this session (alphaXiv).",
  "via": "Drive read_file_content on both files; alphaXiv answer_pdf_queries on 2502.10575. The first audit of this key read none of the three primaries."
 },
 "pages_read": "L03: full extraction, closely pp.1220-1226, 1231, 1234, 1236-1245 (Tables 3 and 8 complete). ICRP 23: " + PAGES + " LBP25: pp.1, 22-23, 29, 33, 70, 73, 75.",
 "published_statement": " | ".join([
   "L03 Table 3 (pp.1225-1226): 'P (1200 ) (1) (760) (1) 924 100 8 ... (480) (1) 920 100 1'; 'N 2900 1 ... 2948 535 5 ... ... 2940 20 2' (group mean, 1 sigma, N_met)",
   "L03 p.1234: 'the meteoritic value is only based on the P abundance in the Orgueil meteorite, for which a concentration of 920 ± 100 ppm is derived ... P analyses of other CI chondrites ... range from 500 to 1800 ppm'",
   Q["def"], Q["mass"], Q["sigfig"],
   "A09 (carried): photospheric log eps(P) 5.41 +- 0.03, log eps(Li) 1.05 +- 0.10",
   "TREE (ledger.py:674-677): 'A reference adult (ICRP) against a CI chondrite binds on %s at %.4g kg of feedstock per kg; the same payload against a stellar photosphere binds on %s at %.4g kg per kg' -> P 10.70, P 1911"]),
 "published_hypotheses": [
  "ICRP 23 (READ p.4, p.13): a defined reference adult MALE, 70 kg, 20-30 y, 170 cm; a separate reference adult female of 58 kg; characteristics chosen 'with some degree of arbitrariness', not an average or median.",
  "ICRP 23 elemental content: Chapter 2 NOT READ; no hypothesis attached to the gram values can be quoted.",
  "L03 (READ): CI group means weighted by analyses over five falls; P from Orgueil alone (N_met 1), other CI P 500-1800 ppm; N from two meteorites (Orgueil 1 sigma 535 ppm); CI 'severely altered mineralogically' (p.1221).",
  "A09 (carried): present-day solar photosphere; Li depleted 2.21 dex vs meteorites; Li +-0.10, P +-0.03."
 ],
 "hypothesis_drift": [
  "DROPPED 'male', CONFIRMED AT SOURCE: ledger.py:674 'A reference adult (ICRP)'; ICRP 23 p.13 assigns 70 kg to the reference adult male and 58 kg to the female.",
  "DROPPED the source's own precision caveat (ICRP 23 p.4) while printing the binder identity to 4 figures (ledger.py:675-677) at an 8-9 % flip margin.",
  "ATTRIBUTION DISCREPANCY, CONFIRMED AT SOURCE: stockgate.py:284/:395 attribute the CI table to L03; the full L03 Table 3 matches it within 0.5 % for 9 of 60 elements; P 1040 vs 920 +- 100, N 3180 vs 2940 +- 20, As x10.69, Ta x0.694.",
  "DROPPED UNCERTAINTIES on all three tables; newly read: L03's P is a one-meteorite value with older CI analyses spanning 500-1800 ppm (a range that contains a CI binder flip: N binds at P 1800), and L03's N +-20 hides Orgueil's +-535.",
  "WIDENED ATTRIBUTION: '(ICRP)' covers the 34 incidental elements incl. Li 7 mg; whether ICRP 23 prints Li at all is NOT READ (Chapter 2).",
  "ADDED: destination = bulk CI, all accessible (tree names this open at ledger.py:706-709); 'a stellar photosphere' generalises A09's present-day Sun (carried)."
 ],
 "data_at_publication": [
  {"quantity": "CI N (decides CI binder N vs P)", "value_then": "tree 3180; L03 2940 +- 20, Orgueil 2948 +- 535 (READ)", "value_now": "LBP25 1965, SD 970, quality D (Table 4) / +-447 (text p.29) (READ)", "source_now": "arXiv:2502.10575", "moves_conclusion": "YES for the label: crossover 2282 ppm at LBP25 P; N binds at 13.070. Contested (band spans the crossover)."},
  {"quantity": "CI P", "value_then": "tree 1040; L03 920 +- 100, N_met 1 (READ)", "value_now": "LBP25 989, SD 89 / +-63 (READ)", "source_now": "arXiv:2502.10575", "moves_conclusion": "Figure only: P binds at 10.70 (tree), 12.10 (L03), 11.25 (LBP25 P with tree N)."},
  {"quantity": "photospheric Li (decides photosphere binder)", "value_then": "A09 1.05 +- 0.10 (carried)", "value_now": "AAG21 0.96 +- 0.06 (carried; exojax data file in the first audit)", "source_now": "CARRIED", "moves_conclusion": "YES (first audit): Li binds at 2138.5 under AAG21."},
  {"quantity": "payload P and Li", "value_then": "780 g, 7 mg (tree; ICRP 23 value NOT READ)", "value_now": "ICRP 110 bulk P 0.813 %; Emsley fraction column Li 2.17 mg (carried)", "source_now": "CARRIED from icrp-23-reference-man first audit", "moves_conclusion": "YES: flips at P < 715.7 g / Li > 7.629 mg (photosphere), P < 588.7 g (CI) -- reproduced here."},
  {"quantity": "payload body mass", "value_then": "70 kg reference adult male (ICRP 23 p.13, READ)", "value_now": "n/a", "source_now": "n/a", "moves_conclusion": "No for per-kg factors; confirms the object is the male."}
 ],
 "rederivation": {
  "method": "numeric", "script_path": SL + " ; " + SI,
  "outcome": "Both exit 0. From L03 read at source: tree CI binder P 10.70115 (749.08 kg); L03 rows P 12.097 (846.79 kg); crossover 2123 (L03 P) / 2282 (LBP25 P) / 2400 (tree P); LBP25 N+P -> N 13.070; P at 1800 ppm (L03's older CI range) -> N 8.736. From the tree payload: photosphere P 1910.9 (Li 1753.4, 91.76 %); flips Li > 7.6288 mg, P < 715.7 g (photosphere), P < 588.7 g (CI); 59-row total 70,085.9 g = ICRP 23 male 70 kg. The first audit's AAG21 and ICRP 110 substitutions and its z3 principal-ideal check are not re-run.",
  "agrees_with_source": "partly"
 },
 "later_literature": [
  {"ref": "Lodders, Bergemann & Palme 2025, arXiv:2502.10575", "effect": "contested", "what": "CI N 1965 (SD 970 in Table 4; +-447 in text p.29; quality D, -33 %), P 989. Moves the CI binder to N.", "read_status": "READ this session (alphaXiv; Table 4 p.70, pp.29, 33)"},
  {"ref": "Asplund, Amarsi & Grevesse 2021, arXiv:2105.01661", "effect": "narrows", "what": "Photospheric Li 0.96 +- 0.06; moves the photosphere binder to Li.", "read_status": "CARRIED from the first audit (package data file)"},
  {"ref": "ICRP 89 (2002); ICRP 110 via arXiv:1508.00226", "effect": "contested", "what": "Amends P23; ICRP 110 bulk moves both binders (different population).", "read_status": "CARRIED from icrp-23-reference-man first audit; ICRP 89 NAMED-NOT-READ"}
 ],
 "lacked_data": "Each source, read at source where possible, already states the looseness the tree dropped: ICRP 23 that Reference Man is a defined, arbitrary-within-limits male not an average (p.4, p.13); L03 that CI P is one meteorite with others at 500-1800 ppm and that halogens and Hg are uncertain. What they lacked: ICRP 89/110 and in vivo female data; LBP25's CI N; AAG21's Li. FOR: each later datum, substituted alone, flips a binder D25 prints. AGAINST: no datum refutes a measurement as defined; magnitudes stay within 1752-2157 (photosphere) and 9.0-13.1 (CI) kg/kg; D25's OPEN verdict and R11 do not depend on the binder identity.",
 "grade": "DATA-DEPENDENT",
 "grade_evidence": "(1) L03 now read at source confirms the carried CI values (P 920 +- 100, N 2940 +- 20) and adds that P rests on Orgueil alone; the tree's CI table is not L03's. (2) ICRP 23 read at source confirms the payload is a defined 70 kg MALE and states its own arbitrariness; its elemental chapter was not returned, so P 780 g / Li 7 mg remain unverified against it. (3) The binder identities D25 prints sit 8-9 % (photosphere) and 24.5 % / the N crossover (CI) from a flip, and data that have moved or are contested (LBP25 N, read; AAG21 Li and ICRP 110, carried) cross them. DATA-DEPENDENT, unchanged. Not WRONG; not STANDS; OPEN only for the unread ICRP 23 Chapter 2 and the carried A09/AAG21 leg.",
 "what_would_change_the_grade": "To STANDS for the labels: settled photospheric Li with eps_Li - eps_P >= -4.397, settled CI N >= ~2280 ppm at P 989, and ICRP 23 Chapter 2 (pp.273-334) read showing P >= 716 g and Li < 7.63 mg for the 70 kg male; or the tree printing 'P or Li / P or N within the data's spread'. To WRONG: a computed contradiction of a measurement as defined; none approached.",
 "reverify_command": "PYTHONDONTWRITEBYTECODE=1 python3 " + SL + " && PYTHONDONTWRITEBYTECODE=1 python3 " + SI,
 "report_path": D + "icrp-reference-adult-and-ci-chondrite.json",
 "supersedes_grade": "DATA-DEPENDENT"
}
write(comp["key"], comp)
