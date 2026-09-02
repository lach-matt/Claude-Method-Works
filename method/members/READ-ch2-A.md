# READ-ch2 — Phase R2, main volume Chapter 2 "The protocols" (chat 69)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L568–L1002 (435 lines, 4,325 words; §2.1–§2.20), read in full against (i) each cited source, (ii) the cited Register entries (165, 219–222, 232, 270, 275, 277, 278, 286, 343, 407, 432), (iii) the rebuilt tower (r2-ch2.py beside tower-2.py). Labels as in READ-ch1. Nothing in any volume was changed.

## A. Deviations (both texts)

**2-01 · Chapter extent against §5 and Chapter 28.** Chapter 2 ends at §2.20 (L973–1002). §5 L1491 "§2.16 through §2.22"; L1500 `§2.21 a withdrawn figure's data · a number deleted rather than replaced · reg. 374`; L1501 `§2.22 a corroborable entry · a defect that cannot be traced to its proof · reg. 415`; L7809 "The withdrawals register closes through §2.22". No §2.21 or §2.22 heading exists (`^#+ *2\.2[12]`: 0). MEASURED. READING: two protocols named by the book are not in the chapter; the census (C1, 8 unresolved) did not report these four pointers.

**2-02 · L598 (§2.6) against §23.11.** PRINTED: "Four causes have been identified — dilution, depth, coupling-scheme change, and core-excited interleaving — and §23.11 gives a worked case of each." SOURCE: §23.11 L6519 "The refusal pattern carries four verdicts, not one" — its four are refusal patterns (none/infinite V; none/finite; one; regularly spaced; dense and irregular) and L6519–6570 contain none of the four causes' names. MEASURED (read + grep). READING: pointer does not resolve to the claim.

**2-03 · L641 (§2.11).** PRINTED: "Appendix B carries this at channel level for all 153 channels." SOURCE: Appendix B L10204–10206: "a twenty-channel gap disclosed against a total of 153. That was true at registers 630–631 and was overtaken by the parent-term wall (register 1578) and the J-resolved rows of T8-J (registers 1699–1700); the table drifted from…"; L10277 also prints "across all 153 channels". MEASURED. READING: a total Appendix B says was overtaken survives at L641 and L10277 (C7 class).

**2-04 · L701 (§2.15.2) against its own table L683–699.** PRINTED: "Two lower bounds, two upper, two negatives, five structural, one methodological" (= 12) over "Ten consecutive failures". The kind column of the ten rows reads upper, lower, negative, structural, upper, method, negative, lower, structural, structural — 2 / 2 / 2 / 3 / 1 = 10. MEASURED (page). READING: "five structural" contradicts the table.

**2-05 · L705–706, L711–714 against §30.3.** PRINTED: "X is ℛ-closed iff X = {(r,c) : c ≤ M(r) and r ≤ N(c)}, with M, N the running maxima of its own row and column maxima". SOURCE: `M\(r\)|N\(c\)|running maxima` in L8316–8608 (Chapter 30): 0 hits. MEASURED (grep). READING: the d = 2 characterisation is not printed in §30.3 in this form — not located; INFERRED open.

**2-06 · L695–696 (§2.15.2 rows).** PRINTED: "occupancy sort succeeds 53%"; "'row chain or column chain' holds at 68%". SOURCE: 68% is not in Chapter 30 (the only 68 sites are −0.68 at L8352 and 8.68 at L8389); the 53% at L8209 is "Fifty-four of one hundred and two is 53%" (checkable designations, L8199), a different quantity. MEASURED (grep). READING: both percentages unsourced as printed.

**2-07 · L731–734, L746 (§2.16.1) against the grid L736–744.** PRINTED: "eight unfilled requirements … the grid shows that four of them are one"; "Worked on §30.3: eight empty cells, four rows deep, at d ≥ 3"; "Three rows are full at every d". The printed grid has eight rows and four empty cells (·) in the d ≥ 3 column (characterisation, decision procedure, hardness, data structure); four rows are full at both d (YES certificate, NO certificate, obstruction family, construction rules). MEASURED (page). READING: "eight empty cells" prints where the table shows four; "three rows full" where it shows four (the NO-certificate row reads "Tucker — unbounded / unbounded" and may be the one meant as not full — INFERRED).

**2-08 · L754–772 (§2.16.2) against Appendix E.** PRINTED: "it classifies the whole of Q" — six items; "|Q| from six to five". SOURCE: Appendix E L10899–10900 "fourteen items, ten of them open"; E.1.1 L10922–10925 keeps eight, fifteen, thirteen as history. MEASURED. READING: the section presents a six-item Q as the whole; the current index is fourteen — the lineage class of READ-ch1 1-14.

**2-09 · L765.** PRINTED: "§32.2 previously read 'four external, one construction, one mathematical'". SOURCE: the phrase occurs only at L765. MEASURED (grep). READING: a superseded reading quoted with no site — record-carried; not checked against §32.2's current text (deferred to Chapter 32).

**2-10 · L791–792.** PRINTED: "this reduces to a CSP whose ternary constraints are 94% of Λ's pairs". SOURCE: 94% occurs elsewhere only at L2049 (Chapter 10, "Satisfied individually 67–94%"), a different quantity. MEASURED (grep). READING: unsourced.

**2-11 · L824 (§2.17.2).** PRINTED: "Measured: 39% at d = 3 and 49.5% at d = 4, rising." SOURCE: `49\.5%|\b39%`: no other site. MEASURED (grep). READING: unsourced measurement.

**2-12 · L841 (§2.18).** PRINTED: "§3.8 ends by saying a coordinate system answers to two masters and only one of them is computable." SOURCE: §3.8 = L1366 "How the set grew, and the two things that held"; `master` in L1366–1397: 0. MEASURED (grep). READING: attribution to §3.8 unresolved as worded.

**2-13 · L858 (§2.18).** PRINTED: "E(audits) at 11, 0 and 19". SOURCE: §3.8's table L1370–1380 gives the sequence 11 (at 3 coords) · — · 0 (at 3 coords) · 19 (at 4 coords) · 18 (SEQUENCE added) · 17 (PROJECTION added); L1344 "E(audits), then 17"; Register 275 "takes it to 19". MEASURED. READING: the list stops at the third state of five printed — a partial survival (census C7 rows 675). "the tripwire's 150 of 216" is current at §16.3.1 L4396 ("150 of 216 offered assignments are rejected — 69.4%"); "fifty-four of one hundred and two" is current at L8199/L8208.

**2-14 · L852–859 counted.** PRINTED: "Nineteen quantities … are computable" followed by a list; counted as printed the list has 18 items unless "every tower cell count and every density" is two. INFERRED (page count); no deviation asserted. Tower-measurable items all reproduce (r2-ch2.py): E(Λ8) = 0; |J(Λ8)| = 17 with 20 covering relations; 976 down-sets of J(Λ8) out of 2¹⁷ = 131,072; alphabet Σ(|Aᵢ| − 1) = 17 from |Aᵢ| = (3,2,3,4,3,2,4,4); the Λ13 ambient box 47,775,744 (= 6,912²); 475,800 pairs; lemma 4's 2,354 interval sets at L8467. 499,246 at §32.1.2 L8900. MEASURED.

**2-15 · L879–881.** PRINTED: "the seventeenth through twentieth entries of the register are corrections of computation and the twentieth through fortieth are reversals of judgement". MEASURED (page): the two ranges overlap at the twentieth. Entry kinds 17–40 not read this segment (genesis block).

**2-16 · L913–914 (§2.18.1).** PRINTED: "The tight K has two parents and costs the cylinder 2,475 cells." SOURCE: L3477 (§12.11.5) "45,450 at Λ₁₃, 21.4% and 22.8% of the product — recomputed; the 2,475 previously…"; 2,475 survives at L914 and L3434. MEASURED (grep; the census C7 row for 2,475 names these two sites). READING: survival of a recomputed figure — the class Sweep B found (W-102).

**2-17 · L960–966 (§2.19.1) against the current headings.** PRINTED: "§28.7.6 was titled 'Three from the tower session' and contained eighty-six entries, 199 to 284 … It is now four — the tower's three, which repairs their numbering — and §28.7.7 the eighty-seven written afterwards." SOURCE: §28.7.6 = L7677 "Two from the tower session and its repair, in the collaborator's hand"; §28.7.7 = L7678 "The results of the sessions after the tower — 119, printed individually"; `86|87|eighty-six|eighty-seven` near §28.7: 0. MEASURED. READING: the repaired state the section describes (four; eighty-seven) is not the state printed (two; 119).

**2-18 · L971 "Register 286"; L1498 "reg. 286, 287".** SOURCE: 286 is inside the grouped fault heading L1319 `### 203, 215, 218, 259, 280, 283, 284, 286, 291` (§4.2 — wrote into a structure without reading it), whose body lists other instances and not the §28.7.6 count. MEASURED. READING: the citation resolves to a mechanism group, not to a record of this repair — INFERRED. (219–221 resolve to the group at L1323, whose body names "the element count argued into three successive positions" — L936–937 agrees.)

**2-19 · L994–995 (§2.20).** PRINTED: "§2.20's requirement that the audits run on every output now runs under it: the twenty write their state". SOURCE: the requirement is §3.9 L1398 "The audits are run on every output, and the requirement is executable"; §2.20 cites itself. "the twenty" (L995; L1112; L1400 "audited by all twenty") against "The twenty-two prime audits" (L1003, L116) and L79 "twenty-two audits". MEASURED. READING: self-pointer; audit count printed as twenty and twenty-two (Chapter 3's segment decides which).

**2-20 · L620 (§2.9).** PRINTED: "A guard returning a null that a caller coerces to a Boolean produced three false conclusions in this work". SOURCE: the case is at L4463 (§16.6, `None` guard) and §5 L1478 ("the cap discard"); the count "three false conclusions" occurs nowhere else. MEASURED (grep). READING: count unsourced.

**2-21 · L588 (§2.4).** PRINTED: "Ne II fails at D = 5 with two shells; Ar II succeeds at D = 5 with three; Bi I succeeds at D = 5 with five." SOURCE: not located by grep (`(Ne II|Ar II|Bi I)` within 120 characters of `D ?= ?5`, L1003–end: 0). READING: unverified — INFERRED open (Appendix B's declines table may state it in another form).

**2-22 · L602 (§2.7).** PRINTED: "bounds the failure rate at ρ ≤ 3/n at 95% confidence". Prior art (the rule of three; Hanley & Lippman-Hand 1983) — References carry no Hanley. MEASURED (grep). READING: attribution owed (R-ATTR) — INFERRED as to the work.

**2-23 · Layout.** Column dumps with words split across lines: L672–674; L683–699 ("negati/ve", "struct/ural", "metho/d"); L736–744; L756–762; L780–785; L802–813 ("what they / measured"); L923–929; escaped bars at L705 ("M\\", "N\\") and L772 ("\\|Q\\|"). MEASURED (page).

## B. Verified, no deviation
§2.1 Si I 4 / P II 1 (L6833); §2.2 formula (L6170); §2.3 ν_V (L6235); §2.5 27 · 12 · 5 (L6848); §2.8 antiprotonic helium 0.09σ (§16.4 L4426; Ch. 19 L5401–5412); §2.10 Chapter 19, §30.4's five enumerations (L8575, L8597); §2.12 extent worded; §2.13 §28.8 (L7721), §25.6 (L6991); §2.14 Chapter 28 (§5 L1483); §2.16.1 36 (Chapter 6), Tucker 1972 and Schaefer 1978 in References (L11691, L11719); §2.16.2 Λ₉: 1,654 cells, E = 0, projects exactly onto Λ₈, F(−1) = 2 unchanged (r2-ch2.py, rank = Σxᵢ; the graded convention gives −2 for both), constraint graph a tree through Λ₉ (tower-2.py adds one bound per stage until v at Λ₁₀ — agrees with Register L6603's triangle "from Λ₁₀ onward"), item H (L10952); §2.17.1 step 2^(d−2), three quarters (L8488–8496); §2.18 Register 277 (text agrees), 275, 270 (agrees), item H; §2.18.1 Registers 278, 407, 232 (agree), 219–221 (group L1323); §2.19.1 165–204 / 120 entries (arithmetic), audit 15 ENUMERATION (L1131); §2.20 Registers 343, 432 (agree), 475,800, 47,775,744, 499,246 (§32.1.2 L8900).

## C. Outside the chapter, found incidentally
§5 and L7809 cite §2.21–§2.22 (2-01); Appendix B L10205 disclosure against L10277 (2-03); the audit count twenty / twenty-two (2-19); §28.7.6–7 headings (2-17).

## D. Instruments and commands
r2-ch2.py (beside tower-2.py). Pointer and phrase checks: Python `re.search` over the two members with the patterns quoted in each item. DEFECT-CENSUS.tsv rows 675–677 and 1027–1032 closed in CENSUS-CLOSURES.tsv.
