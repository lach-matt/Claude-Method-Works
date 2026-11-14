# Outline M -- main argument and further results (source map for the reader's edition)

Edition: "Five-Dimensional Vaidya Black Holes as High-Frequency Limits of Vacuum Spacetimes".
Base paper: `research/warp-drive/paper/RESPONSE-HL-5D.md` (P below; 4,322 lines, read-only).
Every other path is under `research/warp-drive/docket68/n1star/` unless written out. NP = N1STAR-PROOF.md,
GD = GAUGEDECAY5.md, SG = SETTLE-GLAM5.md, EL = EQUALITY5-LAYER.md, CR = CERTIFY-10L5-RESULT.md, C5 = CONSTANTS5.md.
The stability theory (`proof5/`) and the programs are mapped by other agents: `proof5` results appear here only as
interfaces ("Part VII Thm 0.2"), and programs only by name, for the C-list.

Status words used in this map (for planners only; none enters the edition): PROVED = written-out proof, read and
repaired, labelled proved at source; DEDUCED = written-out argument from computed or cited inputs, read by verifiers
but never promoted to "proved" at source; COMPUTED = exact program identity; CERTIFIED = interval/ball/rational
arithmetic; NUMERIC = floating point; SUPERSEDED = replaced by a later text.

Sections: 0 the paper's own map; 1 per-file tables; 2 composition; 3 material to drop; 4 chapter plan; 5 risks.

## 0. The paper's own map (P lines 1-1907)

- 1-12 title, byline, status labels (5-10): new title; drop 5-10.
- 14-53 abstract: rewrite; drop 41-47 (how the write-out was read, the censuses it replaces).
- 55-148 s.1 introduction (1.1 Burnett, 1.2 HL's theorem READ, 1.3 what is proved, 1.4 why 5D): keep; 109-121
  (supplement, census, write-out history) -> one sentence without process words.
- 150-259 s.2 setting: Props 2.1 (161), 2.2 (187), 2.3 (232); domain 203-215; waves (2.5') 217-235; gauge (2.7)
  243-259.
- 261-466 s.3: Thm 1 (263-295), Prop 3.2 (297-309), Prop 3.3 (311) with proof (320-332), Prop 3.4 (334) with proof
  (340-357), "How Theorem 1 follows" (359-369), Thm 2 (371-394) and sketch (396-411), Thm 3 (413-441) and sketch
  (443-466).
- 468-503 s.4 the approximant (Thm A at 499).
- 505-649 s.5 uniform existence (5.1 512, Lemma 5.1 at 524; 5.2 535; 5.3 564; 5.4 587; 5.5 603).
- 651-703 s.6 the remaining parts (boundary, horizon, mean mass, mass law at past null infinity vs the solver).
- 705-751 s.7 relation to HL, Touati, LR.
- 753-1485 s.8 settling: 8.1 (753-776) -> Part VI; 8.2 (777-923) linear level -> Part VI (RW-type gauge 797-841,
  harmonic gauge 842-872, Hung route 872-910, QNM/tail numerics 912-923); 8.3-8.6 (924-1179) -> Part S interfaces;
  8.7 (1180-1236) -> Part VI; 8.8 (1237-1485): Thm 4 statement 1239-1259 kept, write-out history 1261-1485 dropped.
- 1486-1907 s.9 further results: Settling 1488-1603 (constants of Thm 4); Physical wavelengths 1604-1747; Beyond the
  boundary 1748-1787; More families 1788-1838; Boundary at equality 1839-1863; Review 1864-1870 (drop); Computational
  support 1871-1906 (drop; feeds the C-list).
- 1908-2108 s.10 references (needed by every chapter; not mapped here); 2109- appendices (programs agent).

## 1. Per-file tables

### 1.1 P = paper/RESPONSE-HL-5D.md, sections 1-9

- Prop 2.1 (161): T2-mirror reduction, Ric[h] = (3/2)dpsi^2 + 2domega^2 with two free waves. COMPUTED.
  Prog: response5 R1; lemmas/kn_gauge K1-K2.
- Prop 2.2 (187): 5D Vaidya; K = 72 mu^2/r^8; null geodesic ell; exact commutator (2.4). COMPUTED.
  Prog: response5 R2-R4; ks5 K1-K5. Lit: [Tou23a] Lem 3.1 p.21 (comparison only).
- Domain, Omega (203-215): D_T, tau0, Omega a domain of dependence. DEDUCED (= NP Lemma 1.1).
- Waves (2.5') (217-235): explicit W_TT, p1, p2. COMPUTED. Prog: ansatz5 A3; data5; response5 R12.
- Prop 2.3 (232): averaged stress is null dust, dmu/dv = (2/9) A^2 env^2. COMPUTED. Prog: lead5 L2;
  lemmas/hf_theorem5 F3 (with a Wolfram and a Lean cross-check); response5 R6.
- Gauge (2.7) (243-259): wave-map gauge relative to g0. Lit: [CBCM10] (2.7)-(2.9) p.8, black box.
- Thm 1 (263-295): items 1-7. = NP Thms A, D, E (+ 0.7) and Props 8.1, 8.2. Constants paragraph 289-295.
  Prog: checks/support3 D2, D4; lemmas/counterpart5 P1; response5 R13.
- Prop 3.2 (297-309): x_K = 1 spacelike; the equality case in one sentence. COMPUTED + DEDUCED. Prog: response5 R6,
  R13. Equality: EQUALITY5 Props E.2-E.4; EL Theorems L, L_P, L_E, L_1E''', Cor L.7.
- Prop 3.3 (311-332): one zero per column. PROVED (= NP Prop 8.1). Prog: horizon5 H1-H3, H2b; support3 D1.
- Prop 3.4 (334-357): Hawking mass = mu(v) + O(lam^2) off the shell. PROVED (= NP Prop 8.2). Prog: mass5 M1-M4;
  checks/stage5 S2, S4; support5c C13.
- How Thm 1 follows (359-369): D propagates; symmetry by uniqueness. Prog: response5 R14; support3 D3.
  Lit: [LR05] p.1; [CBCL06] s.3; [CBCM10] Thm 3.3, (3.10)-(3.11) p.14 (black boxes).
- Thm 2 (371-394), sketch (396-411): from past null infinity. PROVED (= NP Thm P). Prog: past5 P1-P8; ledger5 L1;
  gauge5 G3; horizon5 H2b; stage5 S4. 409-411 is verifier history: drop.
- Thm 3 (413-441), sketch (443-466): Bondi chart, Bondi law, mean mass. PROVED (= NP Thm M). Prog: bondi5 B1-B4;
  ledger5 L3; past5 P7. Lit: [TTS09] (28) box; [HL21] eikonal (method).
- s.4 (468-503): profiles, (4.1), stage 0, (E1)-(E3), Thm A. Summary of NP s.5. Prog: support9 S6; lead5 L1-L5;
  stage5 S1. 499's "read by independent verifiers" drop.
- s.5 (505-649): one large coefficient, phase shift, mollifier, energy, local theory, data. Summary of NP s.2-4, 6.
  Prog: support5 C1-C4, C6; support5b C10; support5c C11-C12; csolve5 C7c; gauge5 G1-G2; data5 S2-S4, S6.
  Lit: [Tou23a] pp.12, 20-21; [AO14] Thm 1.1 p.2; [DS23] (A1)-(A4), Thm 2.4; [LY22] Thm 26; [Tou23b] s.5.4.2 p.29;
  [Rac16] p.6; [CD03] (2.1) p.4; [AO14] s.4.1; [AG22] p.1 (black boxes).
- s.6 (651-703): boundary (support5 C8; hf_theorem5 F2 with Z3), horizon (hf_core5, hf_theorem5 F4), mean mass
  (ansatz5 A5), mass law vs solver (past5 P7, bondi5 B4, hf_anchor5). COMPUTED/NUMERIC.
- s.7 (705-751): comparison. Lit: [HL18], [Tou23a], [Tou23b], [LR20].
- s.8.2 (777-923): see Part VI. Lit: [IK03] p.16; [Hol08] Thm 1.1; [HKW18] Thms 1, 2, 16, 18, Lemma 11, (20),
  (115), (124), (127), (173); [KI03] (3.14); [KI03b]; [DR08] Thm 7.2 p.87; [Hun19]; [Sch13]; [CYDL03]; [CLY03b]
  Table 1 p.8. Prog: settle5 T1, T3, T5, T6; support8 K8; kirecon5 P1-P2; redshift5; rwgauge5u; wavegauge5 W1-W8;
  gdrepair5; gdscri5, gdext5, gdkplus5, gdrad5, gdtail5, gdlge2_5, gdr9_5; ix5 X8; hung4; rungs5; growing5; lzero5;
  hierarchy5; coupled5; lzerorate5; lemmas/seed_escape.
- s.8.7 (1180-1236): after the shell, equivariant gluing, extent of Thm 4(ii). = NP 10.50 + GLUEDECAY5 + Part VII.
  Prog: support8b M2, M3; ledger5 L2; flux5; mpdata5; gluedecay5 E1-E6. Lit: [CD03].
- Thm 4 (1239-1259): settling (i) in the class, glued, (ii) without symmetry. PROVED at source as proof5 Part VII
  Thm 0.2 (Part S).
- s.9: see 1.5-1.12.

### 1.2 NP = N1STAR-PROOF.md (11,401 lines)

Header 1-68 is status/history (drop). Every in-text "[amended Dnnn: ...]" or "[corrected Dnnn ...]" bracket (92 of
them) annotates an edit ALREADY made to the surrounding text: delete the bracket, keep the text. Headings carry "(Dnn)"
and "verified (Dnn ...)" tags: delete them.

- 0.1-0.3 (70-141): coordinates, (0.1), gauge (0.2), profiles, scaled norms, eps1, s0. DEDUCED. Lit: [CBCM10] box. Prog:
  ks5 K1-K5; ansatz5 A2; eps1hyp5 H1-H6; lzerotrace5 T6-T7.
- Thm E 0.4 (143-166): uniform existence given (E1)-(E4). PROVED in s.1-4.
- Thm A 0.5 (168-173); Thm D 0.6 (175-179): approximant; data. PROVED in s.5, s.6.
- 0.7 (181-194): Thm 1 from A, D, E; D = 0; symmetry. PROVED. Lit: [LR05], [CBCL06] s.3 box.
- Lemma 1.1 (207-228): Omega, its boundaries, (a)-(e). PROVED. Prog: foliation5 B1, B4; ks5 K2.
- Lemma 2.1 (233): Sobolev and products on annuli. PROVED. Lit: [BH17] Thm 7.26 box.
- mollifier (241), Lemma 2.2 (259): compact mollifier (M1)-(M6). PROVED. Prog: support5 C4, C14.
- Lemma 2.3 (280): energy inequality. PROVED. Prog: eps1hyp5 H6.
- Lemma 2.4 (298): transport estimate. PROVED. Prog: ks5 K4; gronwall5 G0-G1.
- 3.1-3.2, Lemma 3.1 (311-357): two-scale form; linearisation; phase-shift identity. PROVED. Lit: [Tou23a] s.3.2.2
  (comparison). Prog: support5 C1-C2.
- Lemmas 3.2 (358), 3.3 (388), 3.4 (402): decomposition; ell-ell component; commutator transport. PROVED. Prog: ks5 K3;
  support5 C3; support5b C10.
- s.4 Steps 1-8 (414-532): bootstrap; closing; local existence, continuation, uniqueness. PROVED. Lit: [DS23] Thms 2.4,
  2.6; [AO14] Thm 1.1, Rem 1.2; [LY22] Thm 26, Lem 27; [BH17] Thm 7.21 (box). Prog: support5 C6; support5c C11-C12.
- 5.1-5.4 (540-627), Lemmas 5.1-5.3: stage 0; ansatz; each stage linear hyperbolic; Thm A. PROVED. Prog: lead5 L1-L5;
  ansatz5 A2-A3; stage5 S1.
- 6.1 (646-683): identities (6.1)-(6.2); why Touati's data do not transfer. PROVED. Lit: [Tou23b] Thm 2.1 (comparison).
  Prog: response5 R14.
- Lemmas 6.1 (692), 6.2 (718): gauge hierarchy; stage data. PROVED. Prog: stagen5 S5; gauge5 G1-G2.
- Lemma 6.3 (776): constraints as an r-evolution, parabolic-hyperbolic. PROVED. Lit: [Rac16] p.6, [CD03] (2.1) box. Prog:
  data5 S2-S4, S6; indepcons5; symmshift5.
- Lemma 6.4 (814): linear evolution by Faedo-Galerkin; tame clause. PROVED. Lit: [GO13], [DS23] Rem 2.3(i) box. Prog:
  tame5.
- Prop 6.5 (887): exact correction O(lam^(N-2)); Kato-Majda scheme. PROVED. Lit: [AG22] s.9; [AO14] s.4.1 box. Prog:
  csolve5.
- 6.4 (947-961): proof of Thm D. PROVED.
- s.7 (962-1101): verification history; READ table; quotations. provenance. Lit: harvest 1044-1095 for an appendix of
  standard results.
- Prop 8.1 (1107-1163): one zero per column. PROVED. Prog: horizon5 H1-H3; support3 D1.
- Lemma 8.2 (1171), Prop 8.2 (1191-1214): quarter-turn symmetry; Hawking mass. PROVED. Prog: mass5 M1-M4; support5c C13;
  stage5 S2, S4.
- Thm P (1236-1256): construction from past null infinity. PROVED. Prog: past5 P1-P8.
- Lemmas 9.1-9.6 (1258-1401): past domain; seed region; Sobolev with rotations; mollifier; 9.4b commutator; energy;
  transport. PROVED. Lit: [BH17]. Prog: past5 P1, P8; redshift5 R9, R10, R14.
- Lemma 9.7, Thm A_P (1402-1526): decay calculus; approximant from scri-. PROVED. Prog: past5 P2-P5.
- Props 9.8 (1546), 9.9 (1568); proof of Thm P (1628-1658): far region; near region; assembly. PROVED. Prog: ledger5 L1;
  gauge5 G3.
- 9.5 (1659-1705): flux at scri-, (9.10) with the factor 1 - pi/2. PROVED. Prog: past5 P7.
- Prop 9.10 (1706-1751): Thm 1 items 6-7 for Thm P's solutions. PROVED. Prog: horizon5 H2b; stage5 S4; support5c C13.
- 10.1 (1757-1795): settling numerics on the barrier. NUMERIC. Lit: [HKW18], [Hol08]. Prog: settle5 T1-T4.
- 10.2 (1796-1901): 10 l5 by growth5's scheme. NUMERIC; superseded in part by CERTIFY-10L5*. Lit: [Wu26]. Prog: growth5;
  response5 R7.
- Prop 10.1 (1913-2062), Lemmas 10.1a (2063), 10.1b (2109-2188): RW-type gauge: every component settles; red-shift datum
  needed. PROVED ((iv-a) via GAUGEDECAY5 Thm 1.5). Lit: [KI03] (3.14), [HKW18] Thms 1-2, [DR08] Thm 7.2 (box). Prog:
  kirecon5 P1-P2; redshift5; rwgauge5; settle5 T5-T6.
- Prop 10.2 (2202-2314): harmonic-gauge structure in the class; W*, K*. COMPUTED + DEDUCED. Lit: [Hun19] (4.11)-(4.23),
  (8.1), (8.38). Prog: wavegauge5 W1-W7; gdrepair5; hung4.
- Props 10.3-10.8 (2315-3413): Hung's route in 5D. DEDUCED, not proved; used by no proved result. Lit: [Hun19], [HKW18],
  [Sch13]. Prog: wavegauge5 W8; rungs5; growing5; lzero5; hierarchy5; coupled5; lzerorate5.
- 10.12-10.49 (3414-7182): deduced route to Thm 4. SUPERSEDED by proof5 (Part S).
- 10.50 (7183-7230): g_lam after the shell: no oscillation; glue; Cauchy stability. DEDUCED ("nothing proved"). Lit:
  [CD03]. Prog: support8b M2.
- 10.51 (7231-7258): Thm E at every order k >= 6. DEDUCED. Lit: [DS23] Thm 2.4. Prog: ledger5 L2.
- 10.52-10.86 (7259-10935): readings, censuses, inventories, bundles. SUPERSEDED by proof5 / provenance.
- Thm M (10961-11002): Bondi chart; Bondi law; mean mass. PROVED. Lit: [TTS09] box. Prog: bondi5 B1-B4.
- Lemma 11.0 (11015-11087): every order at fixed lam, far region (SETTLE-GLAM5 R6-D seated). PROVED. Prog: f1lemma5
  F1a-F1d; cclass5 C1-C3; r5edits5 E2-E3.
- Lemmas 11.1-11.2, Prop 11.1 (11088-11189): equation for u; half-order gain; expansion in r^(-1/2). PROVED. Prog:
  ledger5 L3.
- Lemma 11.3, Prop 11.2 (11190-11317): ell-components; Bondi chart. PROVED. Lit: [HL21] (method). Prog: bondi5 B2.
- [TTS09] READ (11320-11342), Prop 11.3 (11343), proof (11366-11379): hierarchy at scri-; proof of Thm M. PROVED. Lit:
  [TTS09] box. Prog: bondi5 B1.
- 11.4 (11380-11401): numerics against the law. NUMERIC. Prog: bondi5 B4; past5 P7.

### 1.3 GAUGEDECAY5.md (7,303 lines; rounds 1-13) -- the gauge vector of the linear solution; RW-type and harmonic gauge

Round structure: round 1 = lines 1-441 (sections 0-3); round n = "## Round n" blocks (R2 442, R3 994, R4 1388,
R5 1945, R6 2348, R7 3067, R8 3835, R9 4694, R10 5481, R11 6036, R12 6595, R13 7178). Amendments are NOT seated in
place: they are numbered (A1)-(A132), listed in the amendment sections, and many are flagged at their site by inline
"[R10 (A109): read ...]" style notes (about 75). The writer applies each "read X as Y" by hand (fold list in 2.2).

Proved set (final labels "proved [R10]/[R11]/[R12]", R12.p 6727-6769, completed by R13.0 (A130) 7193):

- s.0 Setting (44-79), (0.1): Part VIII in the class, domains N, N+, Sigma-circle, t_IVP
- Def 1.1 (95): the RW-type gauge in the class (f_a = 0 = H_T)
- Lemmas 1.2 (99), 1.3 (126), 1.4 (143): sphere inversions; the gauge vector X_RW; l = 0 linearised mass and Birkhoff
- Thm 1.5 (163-232): Part VIII in the RW-type gauge: settles to mu-dot K at Part VIII's rate, two derivatives lost; (d)
  uniqueness
- Prop 2.1 (248), Lemma 2.2 (284), Thm 2.3 (304): harmonic-gauge solutions; horizon charge; forced linear growth
- Lemmas R2.2 (528), R2.6 (632), R2.9 (683), R2.10 (702), R2.11 (719): box's indicial data; Sobolev; l = 0; gauge
  identity; cone sources
- Prop R2.3 (544), Thms R2.4 (563), R2.5 (581), R2.7 (637): augmented zero-energy operator of box; 1-admissibility; decay
  modulo W*
- Prop R2.13 (b),(c) (852): spherically symmetric sector in harmonic gauge ((a) as input)
- Lemma R3.1 (1076), Prop R3.2 (1161), Lemma R3.5 (1204), Thm R3.4 (1239), Prop R3.6 (1301): extension; (S_K); source
  class; harmonic gauge on the late region; conditional on (Ext box)
- Lemma R4.1 (a),(b),(d),(e) (1449), Prop R4.2 (1494), Thm R4.3 (1549): operator near I0 u scri+; exterior estimate; (Ext
  box) holds
- Cor R4.4 (1599), Cor R4.6 (1613): harmonic gauge on all of N+; homogeneous solutions, compact data
- Thm R5.1 (2009), Thm R5.2 (2110): R2.5, R2.7 at positive K+-weight
- Lemmas R6.1-R6.3 (2401-2437), Thms R6.4 (2438), R6.5 (2541), Cor R6.6 (2556), Lemma R6.8 (2636): III.I''' at box; rate
  at weight alpha_K in (1,2); compact gauge data
- Thm R7.1 (3225), Lemma R7.2 (3322), Thm R7.3 (3379), Cor R7.4 (3393): past the window for zero total charge; explicit
  charge-4pi^2 solution; the t*^(-2) term
- Prop R7.5 (3417), Cors R7.6 (3444), R7.7 (3475): spherically symmetric part homogeneous; data of order p; the
  spherically symmetric rate
- Def R8.1 (4028), Lemmas R8.2-R8.4 (4049-4171), R8.8 (4264), Props R8.5-R8.6 (4172-4234), Thm R8.7 (4235), Cor R8.9
  (4294): projections onto l >= 2 / no l <= 1; (G), (Z), (TF), I.C on the subspace; (M)
- Thm R8.10 (4309), Cors R8.11 (4358), R8.12 (4377): R6.4 on the subspace, window in (-1, 0); R7.8 (a); the harmonic-
  gauge representative
- R9.a (4884-4910), R9.b (4911-4989, items (F1) onward): Lemma R8.8's index argument repaired; functional
  analysis written out (part of the proofs)

Not in the edition (labels kept, nothing proved rests on them, R12.p list 6748-6763): Remark 2.4, Prop 2.5 (frequency
pole; mention as remark at most), Cor 2.6 (withdrawn), Lemma R2.0, Cor R2.8 (read as Cor R4.6), Thm R2.12 and Cor R3.3
(except two proof steps now inside R3.4's proof, (A119) at 1278), Lemma R4.1 (c), Prop R4.5 (formal), Cors R5.3-R5.4
(superseded by R6.6 and R7.4), Props R6.7 (formal), R6.9 (deduced sharpness), R6.10-R6.13 (expansion at scri+),
Remark R7.1', Prop R7.8 (its (a) = Cor R8.11), Remark R8.13, R9.c deductions.

Dependencies. proof5 (black boxes from Part S, by part and result only): Part VIII Thm 2.2, Cor 2.3, Lemma 1.1;
Part IX Lemmas 1.1, 1.2, 2.1, Thm 2.2 (Steps 1, 3), Cor 2.3, Rem 2.4(c); Part VI.A Thm 6.1 ((Dyn)); I.A, I.C
(spaces; low-energy theorems); II.C Def 2.7; II.E; II.F' Thm 1.1; II.G' Prop 3.3; III.A, III.A'; III.B s.3-6,
(3.6), (4.1), (6.3); III.C; III.D Props 6.1-6.2; III.D' Lemma 2.1, Prop 4.1; III.H Lemmas 2.2-2.5, Prop 3.2, Thm 4.1,
Cors 4.2-4.3; III.H' Thm 1.3; III.I (1.2); III.I' Lemmas 1.1, 2.2, Props 2.1, 3.1; III.I'' Prop 5.1; III.I''' Lemmas
1.1-1.3, Prop 2.1; III.J'; IV Props 3.1, 4.1; IV' Prop 2.2; IV'' Lemmas 2.2-2.3; IV''' Thm 2.1 (i)-(iii).
NP Prop 10.1, Prop 10.2 (W*, K*, W**). Literature (box): [KI03] (READ, the gauge vector X_a); [BGP] Cor 3.2.4
(uniqueness); Riesz (the 4+1 Green function, T1); [Hun19] (structure). Programs: checks/ rwgauge5, gdrepair5, hgauge5,
gdsk5, gdix5, gdr3fix5, gdrate5, gdext5, gdkplus5, gdscri5, gdrad5, gdtail5, gdlge2_5, gdr9_5, admbox5, kirecon5.

### 1.4 RWGAUGE5.md (605) -- the RW-type gauge uniformly in r

Status: proved (header 10-15). Bracket notes "[R2.0 ...]", "[R3.0 ...]" in the body (11 in 45-298) are "read as"
instructions, not edits.
- Lemma 1 (98-116): (10.1) in the outgoing chart; components. COMPUTED U1, U2, U4.
- Theorem 1 (122-202): uniformly in r the RW-type statement fails; explicit single-mode counterexample
  h(e0,e0) = B r^(1/2) f^-1 S. PROVED.
- Theorem 2 (213-278): weighted uniform decay from [HKW18] Thms 2, 16, 18, Lemma 11 (box). PROVED.
- Lemma A (363-393) Sobolev on S^3 with rotations; Theorem 2' (394-416) pointwise form. PROVED.
- Remarks s.5 (279-298): region r <= R_1; reading of [HKW18]'s energies. Keep as remarks.
Depends: NP Prop 10.1 ((10.1), the gauge f_a = 0 = H_T), [KI03] (3.14), [HKW18] (READ quotes s.1, 45-82). No proof5.
Programs: checks/rwgauge5u (U1-U11), kirecon5.

### 1.5 GLUEDECAY5.md (2,106) -- which perturbations Theorem 4(ii) reaches

Status: proved (header 16-18, after four readings). Body = s.0-6 (22-576); s.8 (641-1764) replacement texts for the
paper (drop); R2.0-R5.0 (1765-2106) dispositions. Ten "[R2.0 ...]/[R3.0 ...]" notes in the body are "read as" folds.
- s.1 Setting (91-174) incl. Lemma 1.2 (147) uniqueness of the expansion.
- Prop 1 (177), Cor 1.1 (193): order a > l0 lies in the class; every l0 in (3,4). PROVED.
- Prop 2 (206), Cor 2.1 (224): agreeing on balls uniformly in R iff in the class. PROVED.
- Lemma 3.1 (234), Prop 3 (260): pure-gauge examples outside the class, lower bound c Xi R^(l0-a). PROVED.
- Lemmas 4.1 (348), 4.2 (422), Prop 4 (441), Cor 4.3 (506): gluing to the translated/rotated/boosted Myers-Perry
  data, upper bound C Xi (1 + R^(l0-a)). PROVED.
- Theorem 5 (544-576): the settlement. PROVED.
Depends: proof5 Part V Def 2.1 and the gluing estimates; Part VII Thm 0.2, Prop 2.2; Part III.K's data class.
[CD03] (box). Programs: checks/gluedecay5 E1-E6, support8b M3, mpdata5.

### 1.6 BEYOND5.md (942) and BEYOND5-R0-PROOF.md (482) -- the interior after the shell

BEYOND5 status: "deduced", read by verifiers 167-168; Prop 6.2 re-proved part by part in BEYOND5-R0-PROOF.
- s.1 Prop 6.1 (38-57): Thm 4's development reaches r_q(mu_end) once the inner radius is lowered. DEDUCED.
- s.2 (58-74): whose continuation it is. Lemma 6.3 (80-176): the two developments agree on the common domain of
  dependence (gauge change). DEDUCED.
- Lemma 6.4 (177-251): (b)'s first step; the half-integer class D517 (229-244) is defined here; (iv) is written out
  as SETTLE-GLAM5 Lemma R9.1 (3376) with R10.0's deletion of (iii)(b). DEDUCED.
- Lemma 6.5 (252-298), 6.5' (299-884): the Coulomb part and the full flat operator -- an accretion of D4xx-D5xx
  bracket notes that became SETTLE-GLAM5; SUPERSEDED (cite only what SETTLE-GLAM5 cites by line).
- Prop 6.2 (885-937): every Part holds with inner radius r_flat. Re-proved in BEYOND5-R0-PROOF s.0-11 (17-482).
BEYOND5-R0-PROOF: a re-proof of each proof5 Part at the lowered radius. It belongs to Part S (see 4, Part S).
Programs: checks/r0census5, census9 C27, coulombL5 Q1-Q4 (6.5', superseded).

### 1.7 SETTLE-GLAM5.md (3,943) -- Theorem 4(ii) on g_lam's own data, no gluing

Status: Theorem R5.1 PROVED, conditional only on NP s.11.1, itself proved (R10-E 3745). Rounds 1-10; every round
keeps earlier text and adds "[Rn ...]" notes (75 from R6 on) that the writer must apply.
- Final statement: Theorem R5.1 (1942-1971), with R6-R10 notes; status R10-E (3745-3760).
- Proof assembly: "As R4.10 (1446) with R5.1' for R4.6, R5.2 for R4.8, R5.4 for R3.1" (1973-1974).
- Components, final versions:
  - s.3 Prop 3.1 (84-142): the r^(-5/2) tail G_5^inf, nonzero off a discrete set; Remark 3.2 (beyond all orders).
  - s.4 Prop 4.1 (145), Cor 4.2 (168): the tail reaches the data at spatial infinity.
  - s.5 Lemma 5.1 (191): the operator on W.
  - R2.1: Lemma R2.1 (350), Prop R2.2 (354), Lemma R2.3 (374), Theorem R2.4 (402): Theorem 4 in the half class.
  - R2.3: Lemmas R2.7 (466), R2.8 (473): the scaling field; the weight window.
  - R3: Lemma R3.2 (748), R3.3 (765, "as amended"), Props R3.5 (836), R3.6 (873).
  - R4-A: Props R4.1 (989), R4.2 (1016), Cor R4.3 (1033): Theorem P at every order k.
  - R4-C: Lemma R4.4 (1149) means at past null infinity; Lemma R4.5 (1176) widened in R6-B (2389).
  - R4-D (1197-1372) bootstrap on W at weight a -> Thm R4.6 (1367) -> Thm R5.1' (1822) with R5-B (1773-1826),
    written out in R6-A (2286-2386), openness step R7-A (2779-2810) as amended by R8-A (3046-3072).
  - Prop R5.2 (1829; proof 2369-2388) uniqueness at weight a_0 (replaces R4.8); Prop R4.9 (1418) vacuum.
  - Prop R5.4 (1749) (Poly) on the far region (replaces R3.1).
  - Lemma R9.1 (3376-3483) = BEYOND5 Lemma 6.4(iv); R10.0 (3707-3744) deletes (iii)(b) and three sentences.
- Negative results kept as remarks: Prop R4.7 restated as R5.3 (1841): the weight-a_0 < 1/2 scheme does not close;
  Prop R2.6 (440). Superseded: Thms R2.10 (521), R3.7 (889), R4.10 (restated), Props R2.5, R3.1, R4.8; R5-D
  (1862-1939) and R6-D (2427-2534) are NP Lemma 11.0's replacement text, already seated (NP 11015-11087): drop here.
Depends: proof5 Part IV (seven outputs), III.C', III.K Thm 4.3, Part VII Lemma 1.1, Prop 3.2, VI.C rows d1-d2 (Part S
interfaces); NP Thm P, Props 9.8-9.9, s.11.1 (Lemmas 11.0-11.2, Prop 11.1); BEYOND5 D517 class.
Programs: checks/tail5 T1-T9, wedge5 W1-W6, r5op5, r6sigma5 (W window), r5settle5 G1-G6, r9beyond5 B1-B5''',
f1lemma5, cclass5, r5edits5, r6edits5 (texts only; drop).

### 1.8 Families: FAMILIES5 and FAMILIES5-* (eleven files, 4,746 lines)

Status throughout: DEDUCED, read by independent verifiers round by round (rounds 1-11), "proved" never promoted. Each
later file seats the previous round's findings as bracketed notes in the earlier files ("[R5 ...]", "[R6 ...]",
"[R7 ...]", "[R8 ...]") or in itself; the paper text is FAMILIES5-R11 s.R11.1 (= P 1827-1876).
- FAMILIES5 (841): scoping. Inputs used by FULL: s.4b Stage 0 with two phases (121-213), 4d large coefficients
  (214-255), 4e Stage 0 in the generalised wave gauge (256-459), 4f NP s.5.2 with two families (460-523), 4g NP s.3
  (524-582), 4h Thm A (583-633), 4c two-dust background (634-667), 4i NP Lemma 1.1 with two dusts (668-835).
  Drop 1-120 (scoping, plan).
- FAMILIES5-FULL (829), Part I: Thm 1_2 (66) two crossing dusts; Prop B (93) background; s.3 phases; Thm A_2 (196);
  Thm E_2 (239) written in full in s.8 (513-665: Lemma 3.3_2 at 574, Steps 4-7); Thm D_2 (282); items 6-7: Prop 8.1_2
  (668), Lemma 8.2_2 (714), Prop 8.2_2 (728), 739. Part II (346-400): permitted null phases; angular separation fails
  at the axes. Part III (401-503): Vlasov literature, Prop V (456) no torus stress. s.11-12 (743-815) dispositions:
  the corrections are in place, marked [R5]; drop the disposition prose.
- FAMILIES5-NONROUND (423): Prop C (82), Prop A (148), Thm N (169) the non-round background off the axes, Cors N1-N3
  (225-271); Prop X (272) the axes fail as stated. Amended by bracketed notes from AXIS.
- FAMILIES5-AXIS (550): s.2 band-localised data (75-211; Prop L 138, superseded by R6 Thm L'' and R8 s.R8.3);
  Lemma A (264) planar shear at an axis; Thm N' (306), Cor N'1 (346): Cauchy stability without smallness on the
  record's domains; s.4 restricted Vlasov (385-433).
- FAMILIES5-VLASOV (429): Thm V (115) restricted massless Vlasov limits; Cor V1 (143); Prop U (148), Lemmas S, C, P,
  Psi (169-222), Prop Ax (225); s.3 Racz split on the whole slice (243-267); s.4 exact compact support (268-295;
  Prop L' 270); s.6 standard results proved: Thm K (309) Kato iteration with a non-local source, Lemma E (331),
  Lemma A' (339).
- FAMILIES5-R6 (547): Thm Q (153), Cor Q (169), KID pairing (192), Thm Q' (201) charge sign; Lemma S1 (253),
  Thm L'' (260) deformed slice; Thm V restated (288), Lemma O (308), Prop NE (319) non-vacuity; s.4 N-family step,
  Thm D_2_N (372); Thm K' (415) Cauchy stability.
- FAMILIES5-R7 (286): Thm Q at the axes (95-128); charge and E defined (129-145); margins certified (146-175);
  Lemma O' (178); corrections applied as [R7] notes (194-208).
- FAMILIES5-R8 (493): certificates in interval arithmetic (93-126); the background itself (127-228); Thm L'' with the
  moved lobe (231); N-family ledger (243-281); Lemma O'' (284) supersedes O, O'; Thm Q at the axes, signs (319-340);
  E and the Hollands-Wald identification (341-359); M_b review seated (432-480).
- FAMILIES5-MB (447): Lemma H (102), Thm T (129) tensor sector, Lemma X1 (172), Thm X (189) M_b fails inside the
  horizon, Lemma TR (215), Lemma G (253), Lemmas K, V (280-310), Thm P (343) M_b holds outside.
- FAMILIES5-R10 (155), R11 (76): wording, labels and controls; one false sentence of the paper block (Major 1) fixed.
  Mathematical content: none beyond corrections listed in R10.0 (12-90) and R11.0 (14-48).
Depends: NP s.1-6, 8 (the one-family proof, mirrored); GAUGEDECAY5 Lemma 1.2 (MB's class harmonics); [Rac16] Lemma
4.1; [CS06] Thm 2; [CD03] Thm 5.6; [KI03] master equations; [HL18] angular separation; Vlasov literature READ at
FULL 403-453. No proof5. Programs (checks/): stage0two5, twophase5, twobg5, twoslice5, nonres5, twotransport5,
twoext5, twodecomp5, twoledger5, twohorizon5, twoparity5, h3proof5, axisphase5, torusstress5, classchi5, augment5,
axisloss5, axisellip5, bandconst5, vlasov5, vlasovhf5, twoscale5, racglobal5, racslice5, qsign5, nfamily5, katonl5,
vlasovex5, intcert5, truebg5, nledger5, mbsign5, mbslice5, twodomainx5.

### 1.9 Constants of Theorem 1: CONSTANTS5 s.1 and R1-R7 on lambda0; LAMBDA0-DATA5; M22CERT5

- CONSTANTS5 (4,372; 15 rounds; P's constants text = R15.7, seated). lambda0 chain: s.1 (42-148) lambda0 <=
  min(lam1, eps1/C_app); R2-R4 (357-1113): lambda0 < 0.0024433 certified (operator norm), eps1 < s0 (ties to NP
  0.3); R6.0 (1403-1449) largest entry < 0.0012228; R7.0 MAJOR 2 and R7.3 (1613-1692, 1756-1793) Frobenius
  < 0.0019079; R8.2 (2204-2241) stage-1 enclosure attempted. Status: COMPUTED (certified) + DEDUCED.
- LAMBDA0-DATA5 (904): S_1, B_1 second-order constraint expansion (84-131), stage-1 data mode by mode (154-222),
  envelope (223-249, proved E1), M_22 decided where (250-281), X*'s past (282-317), s.12 stage-1 evolution and
  M_22 = 2.207738 (388-683), readers' confirmations s.13-14 (684-904). COMPUTED (floating point) + PROVED (envelope).
- M22CERT5 (260): s.2 the a posteriori estimate (59-115, proved); s.3-5 what is certified and why m_lo is not
  (116-191). PROVED + CERTIFIED; outcome negative.
Programs: checks/lzeroaudit5, lzeroconst5, lzerotrace5 T2-T7, r6fixes5 F1, stage1cap5, classm5, envelope5,
lam0data5, m22evol5, m22cert5, response5 R7 (wavelength ratios).

### 1.10 Constants of Theorem 4: LOSS-D, CONSTANTS5 R5-R15, E2-PILOT, INVERSE5-SCALAR, INVERSE5-SIX, EFFECTIVE-CONSTANTS

All of these count or bound constants of the stability write-out and cite its parts by line (I.B:1513, I.C:497,
III.J'' Thm 4.1, II.D:686 ...): they are only writable after Part S fixes its numbering.
- LOSS-D (990): structure of d (25-41), six elementary losses (42-174), weights and counts (175-208); LD sections
  with corrections. DEDUCED.
- CONSTANTS5 R5-R15 (1114-4372): d as an integer, d <= 46,236,517,538,883,361 (R8.1 2104, R9.1 2469, R10.1 2659,
  R11.1 2873, R12.1-R12.2 3104-3214, R13.1-R13.2 3444-3533), Appendix R7.A quantitative calculus (1860-1972),
  log orders Lemma R12.1 (3104), floor 8.41e15. Final summary R14.5 (3857-3866). DEDUCED, counts COMPUTED.
- E2-PILOT (877): Lemmas E2.1-E2.3, Props E2.4-E2.5, Cor E2.6, Lemmas E2.7-E2.10, Cors E2.11-E2.12 (37-608),
  s.3j large sigma (609-773). Self-contained scalar resolvent theory on Tangherlini. PROVED/CERTIFIED.
- INVERSE5-SCALAR (661): A scalar-type zero-energy blocks, Lemma/Cor A.6 (191, 213); B root avoidances, Lemma B.1
  (320), Thms B.2-B.5 (347-466), B.9 every admissible point (527-565). PROVED + CERTIFIED; part C superseded.
- INVERSE5-SIX (919): Lemmas R1-R8 (111-214), microlocal constants (215-277), spectral bounds (278-328), per bound
  (329-400); Round 2 Lemma R9 (560) and where the computation stops (470-641); R3-R5 corrections (650-919).
- EFFECTIVE-CONSTANTS (441): methods READ (62-102); Props 2.1-2.2 the chain to lam1 and delta (103-297); where
  numbers are lost (298-357). DEDUCED.
Programs: checks/ dnumber5, x7indep5, modcount5, d0count5, ordcensus5, l2par5, logind5, iotaind5, rootavoid5,
level2loop5, lambdacount5, epsind5, thetain5, prop31loss5, charge5, deltacap5, inverse6_5, inverse6_5a, inverse6_5m,
zeroext5, tensorzero5, scalarblock5, e2pilot5, e2band5, e2morawetz5, e2certify5, e2lzero5, e2cplx5, e2h1_5, e2meas5,
e2lower5, e2trapband5_384.out, e2h1band5.out, census9 C29, support9 S3.

### 1.11 The boundary at equality: EQUALITY5 (237), EQUALITY5-LAYER (3,665)

- EQUALITY5: Lemma E.1 (47) g0 at equality; Prop E.2 (74) seed region exact; Prop E.3 (110) boundary; Prop E.4 (133)
  domain of dependence at equality; Prop E.5 (182) the spheres' horizon at equality. PROVED (verified, EQ6).
- EQUALITY5-LAYER: rounds 1-9; every round adds "[Rn ...]" notes at amended sites (26), earlier text kept. DEDUCED.
  - Theorem L (14) and Cor L.7 (35): the layer has timelike points; proof s.7 (211-244) with round-2 lemmas.
  - Lemma L.1 (72), Prop L.2 (81) with (a) written in full R2.4 (507), Cor L.11 (529), angular factor s.4 (140-150).
  - Lemmas L.3, L.4: round-1 sketches (153, 171) replaced by R2.3 (413-504) and R2.5 (545-600); L.4' (1474).
  - Tools L.5, L.6 (192, 203), L.8-L.10 (359-410).
  - Thm L_P (617), Prop E.2_P (629), Lemmas L.3_P (652), L.4_P (691): Theorem 2's solution.
  - Props L.12 (987, amended 1489), L.13 (1024), L.14 (1058): the layer region by region.
  - Lemmas L.15_P (1293; (b) in full 1844), L.16 (1316), L.17 (1864, replaces L.17_P 1345), L.18 (1903, replaces
    L.18_P 1361), Thm L_E (1373): the very edge for Theorem 2's solution.
  - Theorem 1's g_lam at the very edge: R4.2 (1410-1471) -> L_1E (R5.3 1937-2113) -> L_1E' (R6.1 2354-2478) ->
    L_1E'' (2838; R7.1-R7.3 2726-2882, Prop L.26 at 2788) -> L_1E''' (3236; R8.1 L.28 3101, R8.2 L.27 3165).
  - Thm L.24 (2116) one switch per column; Prop L.25 -> L.25' (2481) -> L.25'' (2885).
  - Constants: lambda_L (R3.3 1093, R4.5 1548, R5.6 2203); C_L11, C_L4 (R5.5 2170); lambda_25 (R8.3 3199, R9.1-R9.2
    3395-3549).
  - R4.4 (1507-1547): the amendment to NP Lemma 6.2's proof -- already seated in NP (D615): drop here.
Depends: NP s.0-6, 9 (Lemma 2.3, 2.4, Thm A_P, Lemma 9.3), EQUALITY5; no proof5. Programs: checks/eq5 E1-E6,
layerlin5, layerwin5, layerpast5, layernull5, layerledger5, layerband5, edgeP5, bandL4p5, degtwo5, constL5, edge1_5,
hyp5, eqlayer5, bfam5.

### 1.12 Physical wavelengths at 10 l5: CERTIFY-10L5 (769), CERTIFY-10L5-RESULT (5,512)

- CERTIFY-10L5: feasibility study; s.6b (178-761) the double-null prototype and its runs at both seeds. NUMERIC.
- CERTIFY-10L5-RESULT, rounds 1-10 (each "seated as amendments to section n-1"):
  - s.1.2 (72-126) two deductions: leaves inside the seed's horizon generator are outer trapped; marginal sections
    near 1.01-1.05 r_h. DEDUCED (identities computed, sectexp5).
  - s.1.3-1.6 (127-261), 13.2 (4798-4820) second zero, rebuild against growth5. NUMERIC.
  - s.2.1 (264-305) Raychaudhuri constraint on the data cone. CERTIFIED (cdata5).
  - Theorem 7.L (1049-1107; constants re-derived in 8.0 at 1511), Theorem 8.W (1788), Theorem 8.L1 (s.8.5,
    1891-2042): linear estimates in double-null gauge. PROVED.
  - s.8.2 axis charts (1658-1785); s.9.5 axis hierarchy (2646-2701). DEDUCED (identities at random jets).
  - Lemma 9.C (2550) existence by continuity; Lemmas 9.H (2605), 9.B (2615) the block route closed. PROVED.
  - s.6.3, 8.4, 9.2 certified residuals (rcert5, rcert5d, rich5). CERTIFIED.
  - Late region s.9.6, 11.1, 12.1, 13.1 (cp3grid5, cpaxis5, mtrunc5). NUMERIC.
  - Final "what holds": 14.1 (5477-5484) = 13.4 (4867-4880) with one change.
Depends: NP s.10.2; [Wu26] Thms 2.1-2.2; [CTG23] Thm 1.1; [AB26]; [Luk] characteristic IVP. No proof5.
Programs (checks/): secondzero5, szconv5, szrun5, g5angle5, sectexp5, cdata5, resid5, rcert5, rcert5b, rcert5d, rich5,
reduce5, null3, linest5, lev1_5, wgron5, axis5, axisbianchi5, axhier5, cont5, blocks5, blockw5, symbol5s, late5,
late5b, cpaxis5, cp3grid5, mtrunc5, g1curv5, excise5; dnsolve5, growth5 (n1star/).

### 1.13 docket68/lemmas/

Sections 1-9 of P cite six programs there (hf_theorem5, hf_core5, hf_anchor5, seed_escape, counterpart5, kn_gauge)
and no note. The only prose behind them is docket68/lemmas/BOUNCE-RESEARCH.md s.46-52 (2675-3060: the Bondi-form
solver, THM-HF5, the anchor, the KN gauge), a history: hand it to the programs agent for the description of the
numerical solver of s.6; it contributes no theorem to the edition.

## 2. Composition: the final mathematics, file by file

General rule. Every statement in P sections 1-9 is the latest seated text: each workstream's "final paper text"
was seated in P (C5 R15.7; EL R9.4; CR 14.3; families R11.1; SG R10-E; GD R12.h/R13.h; GLUEDECAY5 s.8.5; RWGAUGE5
s.6). Take STATEMENTS from P (stripped of labels and file names) and PROOFS from the supplements below. Where a
supplement's statement and P differ, P wins unless noted in 5 (risks).

Three amendment styles occur, and the writer must know which applies:
- (I) seated in place, bracket keeps the old text (NP: "[amended Dnnn: was ...]"; FAMILIES5-FULL "[R5]"): delete the
  bracket, keep the text.
- (R) "read as" notes at the site, old text NOT changed (GD "[R10 (A109): read ...]"; RWGAUGE5; GLUEDECAY5; EL
  "[Rn, ...]"; SG "[Rn ...]"; families "[R6 ...]" to "[R11 ...]"; NONROUND "[Amendment 2026-11-02 ...]"; C5
  "[Round n ...]", "[Rn: ...]"): apply the note to the text, then delete it.
- (L) listed only, in a later round's amendment block, with no note at the site (GD (A1)-(A132); CR "seated as
  amendments to section n"; EL, SG, C5 verifier blocks "Rn.0"): find the target from the block and apply it.

### 2.1 NP (N1STAR-PROOF.md)

- Style (I) throughout: delete the 92 "[amended ...]" / "[corrected ...]" brackets (lines e.g. 117-127 in 0.3,
  1117, 1129, 1139, 1160, 1173, 1186, 1200, 1206, 1224, 1231-1235, 1250, 1301, 1324, 1334, 1513, 1620, 1664, 1684,
  1717, 1720, 1731, 1743, 10938-10960, 11051-11054, 11071-11073, 11075, 11083). Keep the text around each.
- Cross-file amendments to NP are already seated: SG R6-D (SG 2427-2534) = NP Lemma 11.0 (11015-11087), seated
  D630; EL R4.4 (EL 1507-1547) = NP Lemma 6.2's proof, seated D615-D616; GD R12.h texts (1), (2), (9)-(12) = NP
  Prop 10.1 header and (iv-a), seated D631 (GD 7265-7267). Nothing pending: no fold from outside NP is needed.
- 9.5: the formula (9.10) as corrected (factor 1 - pi/2) is final; drop the bracketed history 1680-1693 and the
  paragraph "What this does not prove" 1695-1705 (superseded by s.11, Thm M).
- 10.51 (7231-7258): fold as a remark into Thm E (NP 0.4): "the theorem holds for every k >= 6 with K >= 6"; its
  argument (a)-(d) becomes the remark's proof. 10.50 (7183-7230) (a), (b), (d) are inputs of Part S's assembly
  (Part VII Prop 2.2); (c), (e), (f) are superseded by Part VII (do not reproduce).
- Superseded and not composed: 10.12-10.49 (3414-7182) by proof5; 10.52-10.86 (7259-10935) by proof5 (readings,
  censuses, inventories); Props 10.3-10.8 (2315-3413), Hung's route, used by no proved result (P 872-910 says so).

### 2.2 GD (GAUGEDECAY5.md), style (L) + (R)

Final proved set: 1.3. Rule: compose each result from its first statement, then apply every amendment below in
order; amendments not listed here are about programs, texts for P, status or citations and are dropped (3.3).
- s.0 (44-79): (A1) 1047 (smoothness up to Sigma-circle); (A16) 1773 (everything at b0; (Dyn) from Part VI.A
  Thm 6.1); (A27) 1849 (the range of gamma_Upsilon).
- Thm 1.5 (163-232): (A2) 1050-1065 (read on N+; (d) on Omega'_+, U in U-sharp); (A11) 1740 (N-circle -> N_{r0});
  (A57) 3113 (Part IX proved); (A109) 5622 and its notes at 166, 183, 196; (A112) 6091 and notes at 186, 409;
  (A129) 6718 and note at 33.
- Prop 2.1 (248-276): (A3) 1066, (A4) 1069-1075 with Lemma R3.1 (1076-1095, insert before Prop 2.1's proof), (A7)
  1102 (Part IX inputs), (A9) 1726, (A13) 1754, (A124) 6687. Lemma 2.2, Thm 2.3: (A5) 1096, unchanged.
- R2 results (511-781): (A17) 1783 (s > 5/2 in R2.1); (A18) 1787 (R2.5 (iii)); (A19) 1793 and (A123) 6679 (naming:
  rename the round-2 objects so no label collides); (A12) 1746 and (A20) 1799 (Thm R2.7's derivatives and window);
  (A40) 2760 (compact-support claims at lines 427-428, 437, 445, 655, 864-866).
- Cor R4.6 (1613; replaces Cor R2.8 at 671): (A10) 1732, (A23) 1816, (A34) 2220, (A54) 2832.
- Prop R2.13 (852): (A10) 1732, (A23) 1816, (A121) 6668; statement (b), (c) only, (a) as input.
- R3 (1161-1332): (A8) 1109 (the cut-off chi_K); (A23) 1816 (Thm R3.4 (iv) and proof); (A24) 1827 and (A58) 3119
  (cite Part IX by result, not line); (A25) 1834 (t-flat-star in Prop R3.6's proof); (A28) 1854 (citation at 1155);
  (A29) 1858 (at 1247); (A30) 1863 (b-density at 1091); (A33) 2213 and (A49) 2808 (the rate of Thm R3.4 (iii));
  (A119) 6649 with the written-out steps at 1278 (the two steps of Thm R2.12's proof, which R3.4 uses).
- R4 (1436-1662): (A118) 6640 (Lemma R4.1 (a)); (A42) 2772 (add to Cor R4.4: "and g-dot_H = ..."); (A44) 2788
  (Prop R4.2's heading: IV''' Thm 2.1 (i)-(iii) at box); (A45) 2791; (A33) 2213 (Cor R4.4's rate).
- R5 (1979-2127): (A52) 2822 (R5.1 (i)-(ii) depend on k).
- R6 (2393-2590, 2636-2649): (A60) 3147-3155 (Cor R6.6's proof re-derived, Major); (A62) 3165 (Thm R6.4's (2.25a)).
- R7 (3218-3554): (A76) 3936, (A77) 3942, (A78) 3947 (Lemma R7.2: display with H(t - r), (c), the corners); (A83)
  3975 (Thm R7.1's eps0); (A73) 3912 (the Killing part: Cors R7.6-R7.7); (A79) 3960 (Cor R7.7's c); (A82) 3972
  (delete the cone-localised clause of R7.c); notation (A75) 3928, (A88) 4742, (A89) 4748 (mu0, psi, varpi, m).
- R8-R9 (4007-4401, 4884-4989): (A94) 4791 with R9.a 4884-4910 (Lemma R8.8's index argument); (A80) 3963 and (A97)
  4823 (Cor R8.11 = Prop R7.8 (a), conclusion only); (A102) 5535 and (A106) 5596 ((F1) in R9.b); (A100) 4854 where an
  item states mathematics.
- The [R8: ...], [R9 ...] brackets inside R7-R8's text are style (R): apply.
- Statements for the edition: P 797-872 and P 1488-1503 (seated texts; RW-type gauge 797-841, harmonic 842-872).
  Prop 2.5 (337) may appear as a remark without proof (frequency-domain pole), or be omitted.

### 2.3 RWGAUGE5, GLUEDECAY5, BEYOND5

- RWGAUGE5: Thm 1 (122-202), Thm 2 (213-278), Lemma 1 (98-116) with the body's 11 "[R2.0 ...]/[R3.0 ...]" notes
  applied; add Lemma A and Thm 2' (363-416); apply R2.0.2 (417-424, the measure dr dsigma), R2.0.3 (425-453),
  R2.0.5 (476-500) with R3.0.1 (523-530), R3.0.2 (531-541, h -> h - cK), R3.0.3 (542-550), R3.0.4 (551-564).
- GLUEDECAY5: s.1-6 (91-576) with the ten notes at 35, 65, 75, 85, 256, 278, 329, 514, 559, 570 applied; R2.0-R5.0
  (1765-2106) contain no further change to s.1-6 beyond those notes (they say so: "bracketed notes at each place").
- BEYOND5: Prop 6.1 (38-57), s.2 (58-74), Lemma 6.3 (80-176), Lemma 6.4 (177-251) with the D3xx brackets applied;
  Lemma 6.4 (iv) replaced by SG Lemma R9.1 (3376-3483) minus (iii)(b) (SG R10.0, 3707-3744); Prop 6.2 (885-937)
  with its proof = BEYOND5-R0-PROOF (Part S); D517's class (229-244) is the definition SG uses.

### 2.4 SG (SETTLE-GLAM5.md)

- Statement: Thm R5.1 (1942-1971), with [R6]-[R10] notes; P 1757-1778 is the seated final wording.
- Proof: compose in this order -- Prop 3.1 + Remark 3.2 (84-142) -> Prop 4.1, Cor 4.2 (145-188) -> Lemma 5.1
  (191-232) -> R2.1 (336-420: Lemma R2.1, Prop R2.2, Lemma R2.3, Thm R2.4) -> R2.3 (464-487: Lemmas R2.7, R2.8) ->
  R3-B/C/D (653-886: Lemma R3.2, R3.3, Props R3.5, R3.6; drop Prop R3.1, superseded by Prop R5.4 at 1749) -> R4-A
  (981-1048) -> R4-C (1141-1196, Lemmas R4.4, R4.5 with R6-B's widening 2387-2426) -> R4-D bootstrap (1197-1372)
  amended into Thm R5.1' (1822-1828) by R5-B (1773-1826), R6-A (2286-2386), R7-A (2779-2810) as amended by R8-A
  (3046-3072) -> Prop R5.2 (1829-1840, proof 2369-2388) -> Prop R4.9 (1416-1443) -> Lemma R9.1 (3358-3483) ->
  assembly R4-G (1444-1509) read with R5-E's substitutions (1973-1974).
- Fold, besides the in-line notes: R3.0 (589-622), R5.0 (1539-1746), R5-A (1747-1772), R5-C (1827-1861), R6.0
  (2117-2285), R7.0 (2701-2778), R8.0 (2975-3045), R9.0 (3280-3357), R10.0 (3707-3744). Drop R5-D and R6-D
  (Lemma 11.0 texts, seated in NP), every R*-E paper text, every ledger (s.7 268-287, R2.6, R3-F, R4-G's ledger).

### 2.5 EL (EQUALITY5-LAYER.md) and EQUALITY5

- EQUALITY5 (237): take as is, minus the status (3-4) and s.4 findings (210-237).
- EL: style (R) notes (26) plus per-round blocks: R2.0 (285-311), R3.1 (919-980), R4.6 (1586-1651, amendments to
  rounds 1-3), R5.1 (1775-1837), R6.0 (2274-2353), R6.3 (2534-2569), R7.0 (2655-2725), R7.5 (2911-2931), R8.0
  (3010-3054), R8.6 (3312-3352), R9.0 (3363-3394), R9.5 (3624-3640).
- Final versions: Thm L (14-34) with proof s.7 (211-244) re-run with R2's lemmas (R2.6, 601-614): L.3 = R2.3
  (413-504), L.4 = R2.5 (545-600), L.2 (a) = R2.4 (505-542). Thm L_P = R2.7 (615-718). L.12 amended (1489-1506),
  L.13-L.14 (1024-1092). Thm L_E = R4.1 (1279-1409) with L.15_P (b) (1844-1863), L.17 (1864-1902), L.18
  (1903-1936) replacing L.17_P, L.18_P. Theorem 1's very edge: the final theorem is L_1E''' (3236-3255); its proof
  must be written as one argument from L_1E (R5.3, 1937-2113), L_1E' (R6.1, 2354-2478), R7.1-R7.3 (2726-2882, incl.
  Lemma W and Prop L.26 at 2788), L.28 (3101-3147), L.27 (3165-3198). Thm L.24 (2116-2141). Dips: L.25'' (2885-2910)
  for (a), L.25' (2481-2533) for (b). Constants: lambda_L (1093-1142 -> 1548-1585 -> 2203-2211), C_L11, C_L4
  (2170-2202), lambda_25 (3199-3233 -> 3395-3549).
- Superseded: round-1 sketches L.3, L.4 (153-190), L.17_P, L.18_P (1345-1372), L.25, L.25', L_1E, L_1E', L_1E''
  as statements; every "Proposed paper text" (R2.8, R3.6, R4.8, R5.8, R6.5, R7.6, R8.5, R9.4); R4.4 (seated in NP).

### 2.6 Families (FAMILIES5, -FULL, -NONROUND, -AXIS, -VLASOV, -MB, -R6, -R7, -R8, -R10, -R11)

Order of authority (latest first): R11 > R10 > R8 (and MB) > R7 > R6 > VLASOV > AXIS > NONROUND > FULL > FAMILIES5.
- Two dusts: FULL s.1-6 (44-319) with the [R5] corrections in place (style I) and [R6] pointers applied; Thm E_2 in
  full from s.8 (513-665); items 6-7 from s.9-10 (666-742); FULL s.11-12 (743-815) only for any correction not yet in
  place. Inputs from FAMILIES5 s.4b-4i (121-835).
- Non-round background and the axes: NONROUND s.2-4 (77-325) with its eight "[Amendment 2026-11-02 ...]" notes
  (7, 37, 74, 89, 108, 133, 163, 221) applied; Thm N' = AXIS s.3 (212-384) with AXIS's [R5]/[R6] notes; Lemma A'
  and Lemma E: VLASOV s.6 (331-347); Cauchy stability: Thm K (VLASOV 309) -> Thm K' (R6 s.5, 413-443).
- Vlasov: Thm V (VLASOV 115-147) restated in R6 s.3 (286-334), its N-family step R6 s.4 (335-412), its openness
  Lemma O -> O' (R7 176-193) -> O'' (R8 282-318; final), its ledger R8.4 (243-281); Props U, Ax, Lemmas S, C, P, Psi
  (VLASOV 148-242); Prop NE (R6 319). FULL Part III (401-503) for the literature and Prop V.
- Localised data and the charge: AXIS s.2 (75-211) with [R5] notes; VLASOV s.3-4 (243-295; Prop L superseded by
  R6 Thm L'' -> R8 s.R8.3 Thm L'' with the moved lobe, 229-242, final); R6 s.1 (130-243) Thms Q, Q' -> R7.1 Thm Q at
  the axes (95-128) -> R8.6 (319-340); R7.2 E defined (129-145); R7.3 -> R8.1-R8.2 certificates (93-228); MB
  (87-352, with its [R8]-[R11] notes) and R8.7 (341-359), R8.9 (432-480); R10.0 (12-90) and R11.0 (14-48), [R11-nits]
  (55-76) for the final wording. The paper's block (P 1788-1838) is R10.1/R11.1.

### 2.7 Constants and wavelengths (C5, LAMBDA0-DATA5, M22CERT5, LOSS-D, E2-PILOT, INVERSE5-*, EFFECTIVE-CONSTANTS, CR)

- C5: final paper text R15.7 (4140-4372) = P 1488-1621 (Settling item; first half of Physical wavelengths). lambda0
  chain: s.1 (42-148) amended by R2 (357-648), R3
  (649-884), R4 (885-1113), R6.0 (1403-1449), R7.0 (1613-1692), R7.3 (1756-1793), R8.2 (2204-2241), R14.0
  (3818-3856). d: s.2 (149-276) -> R5.2-R5.4 (1220-1290) -> R6.1 (1450-1499) -> R7.2 (1707-1755) and Appendix R7.A
  (1860-1972) -> R8.1 (2104-2203) -> R9.1 (2469-2506) -> R10.1 (2659-2700) -> R11.1 (2873-2908) -> R12.1-R12.2
  (3104-3214) -> R13.1-R13.2 (3444-3533); final figures R14.5 (3857-3866), unchanged in R15. lambda1, delta: s.3
  (277-326), R5.6 (1315-1335), R6.3 (1531-1558), R7.4 (1794-1829), R8.3-R8.4 (2242-2280). Its 201 "[Round n]"/"[Rn:]"
  notes are style (R).
- LAMBDA0-DATA5: s.1-9 (40-317) as the derivation; s.12 (388-683) amended by s.13 (684-841) and s.14 (842-904).
- M22CERT5: s.2 (59-115) the estimate; s.3-5 (116-191) what is and is not certified; s.7 (200-260) folds.
- LOSS-D: s.1-3 (25-208) with its LD brackets; superseded in its figures by C5 R8.1 onward (use C5's numbers).
- E2-PILOT: s.1-3j (20-773) as is (accretive, no amendments); s.4 (774-863) is the summary to rewrite.
- INVERSE5-SCALAR: A.1-A.7 (74-258), B.1-B.7c, B.9 (287-527, 527-565); part C (566-647) superseded; drop A.8, B.8.
- INVERSE5-SIX: s.1-5 (71-400) and Round 2 (470-641; Lemma R9 at 560) with R3-R5 (650-919) folded (44 notes).
- EFFECTIVE-CONSTANTS: s.1-4 (62-357); Props 2.1-2.2 as repaired (status 8-29 says repaired D342-D343).
- CR: what holds = 13.4 (4867-4880) with 14.1's change (5477-5484); P 1660-1747 is the final wording (14.3). Each
  section n is amended by n+1's ".0" block: 7.10 (1313-1428) -> s.6; 8.0 (1439-1592) -> s.7 (with Thm 7.L's
  constants re-derived at 1511); 9.0 (2258-2427) -> s.8; 10.0 (3026-3155) -> s.9; 11.0 (3459-3587) -> s.10; 12.0
  (4103-4207) -> s.11; 13.0 (4708-4754) -> s.12; 14.0 (5439-5476) -> s.13. Region-of-existence lists 6.5, 8.7, 9.7,
  10.2, 11.2, 12.2 are superseded by 13.4/14.1. P 1621-1747 (from "And a high-frequency theorem") is CR's text.


## 3. Material to drop (file:line, reason)

Everywhere, without listing: status labels in headings and statements ("(deduced; ...)", "computed, `x.py` K3",
"proved [R10]", "(D625)", "verified (D12)"), program names in parentheses (replace by "Computation Cn"), "the
record('s)", "the supplement", "READ", "seated", "verifier", "round n", "workstream", D-labels, md5s, ledgers.
Reason throughout: process language, banned by the author's ruling; the mathematics around it stays.

### 3.1 P (sections 1-9)
- 5-10: the computed/deduced/READ legend. 41-47 (abstract) and 109-121 (s.1.3): how the write-out was read and what
  it replaced (history). 409-411: the two verifiers of Thm 2's near region (history). 499: "read by independent
  verifiers". 869-872: GD's rounds and promotions (status). 1100-1142 (s.8.5 "readings taken up") and 1261-1485 (s.8.8
  after Thm 4): census, inventories, write-out history (Part S may salvage the parameter facts, 1100-1112).
- 1864-1870 Review; 1871-1906 Computational support: process; the program list feeds the C-list only.
- 912-923: QNM and tail observations: keep as a remark citing C-items, drop program names.

### 3.2 NP
- 1-68 status and history. 535-538, 631-645, 1104-1106, 1217-1235, 10938-10960: section status paragraphs.
- 962-1043 and 1096-1101 (s.7): verification history, retrieval table, "Fragile". Keep 1044-1095 (the standard results
  quoted with theorem numbers) for Appendix S1, minus "READ".
- 1680-1693 (bracketed history of the factor 1 - pi/2) and 1695-1705 ("What this does not prove", superseded by s.11).
- 1752-1756 (s.10 preamble, "how far each goes"); 1757-1901 (10.1-10.2 numerics; to C-items, prose rewritten).
- 2315-3413 (10.5-10.11, Hung's route): not proved and not used (P 872-910 says so); drop or one sentence.
- 3414-7182 and 7259-10935 (10.12-10.49, 10.52-10.86): superseded by proof5 (Part S); census and reading inventories.
- 7183-7230 (10.50) (c), (e), (f): superseded by Part VII's assembly. 11380-11401 (11.4): numerics -> C-item.

### 3.3 GD
- 1-17 status; 19-43 one-paragraph result (rewrite as the chapter's opening, no status words).
- 335-399 (Prop 2.5 frequency pole, Cor 2.6 withdrawn, s.2.5 "not proved"); 400-441 s.3 findings.
- 442-510 (round-2 preamble; R2.0 with Lemma R2.0, an example); 745-781 (Thm R2.12: not promoted, except the two
  steps already written into R3.4 at 1278); 782-851 (R2.V verifier's reading; but KEEP Prop R2.13, 852-887, which
  sits inside R2.V); 888-993 (R2.S texts, R2.5-R2.6); 1179-1190 (Cor R3.3, not promoted).
- 994-1028, 1333-1435, 1663-1705 (R4.b: Prop R4.5 formal), 1877-1978, 2128-2201 (R5.b: Cors R5.3-R5.4 superseded by
  R6.6 and R7.4), 2235-2392, 2591-2633 (R6.d formal), 2650-2734 (Prop R6.9, R6.f: not promoted), 2858-3108,
  3530-3554 (Prop R7.8; its (a) is Cor R8.11), 3577-3876, 4394-4725 (Remark R8.13, R8.g-h, round-9 preamble),
  4990-5520 (R9.c-h; keep R9.b), 5637-6069, 6159-6627, 6727-7190, 7224-7303: status, promotions, replacement texts,
  runs and mutations, files.
- The amendment blocks 1029-1126, 1706-1876, 2202-2234, 2735-2857, 3109-3217, 3877-4006, 4726-4883, 5521-5636,
  6070-6158, 6628-6726, 7191-7223 are folded (2.2) and then dropped.
- 3555-3576 (R7.c, expansion of Z_1 on the initial slab): keep only if R7.5-R7.7's proofs cite it; (A82) deletes a
  clause of it.

### 3.4 Other settling files
- RWGAUGE5: 1-44 status and decision summary (rewrite); 299-341 (s.6 replacement text, s.7 files); 342-356; 454-475
  (R2.0.4 old block); 501-522 (R2.0.6 mutants); 565-605 (R3.0.5-R3.0.6).
- GLUEDECAY5: 1-21 status; 577-640 (s.7 findings, labels); 641-1764 (s.8 five rounds of paper texts); 1765-2106.
- BEYOND5: 1-8 status; 252-884 (Lemmas 6.5, 6.5': D-bracket accretion superseded by SG); 938-942 sources.
- BEYOND5-R0-PROOF: whole file to Part S (status 1-16 drop).
- SG: 1-7; 233-335 (s.6-7, R2 preamble, R2.0); 421-463 (R2.2, outline scheme, Props R2.5-R2.6: keep R2.6 as a
  remark only); 519-652; 887-980; 1049-1140 (R4-B, seated in NP); 1373-1415 (R4-E: keep Prop R4.7's content as the
  remark "the weight below 1/2 does not close", via R5.3 at 1841); 1510-1538; 1862-1939 (R5-D); 1975-2116;
  2427-2700 (R6-D, R6-E, round-7 preamble); 2811-2974; 3073-3279; 3484-3706; 3745-3943 (R10-E texts).

### 3.5 Part VII files
- Families: FAMILIES5 1-120 (scoping, plan), 836-841; FULL 1-41, 743-829 (after folding s.11-12); NONROUND 1-52,
  381-423 (keep 359-380's literature as citations); AXIS 1-74, 453-550 (keep 434-452 literature); VLASOV 1-66,
  348-429; R6 1-129 (after folding R6.0), 444-547; R7 1-94, 194-286; R8 1-92, 360-431 (R8.8 paper block), 481-493;
  MB 1-86, 381-447; R10 and R11 whole files after folding.
- EQUALITY5 1-22 (status; keep the setting from 23), 210-237. EL: see 2.5 for the blocks folded then dropped; also
  1-11, 245-284, 719-886, 1143-1278, 1507-1547 (R4.4, seated in NP), 1586-1774, 2212-2353, 2570-2725, 2911-3054,
  3256-3394, 3550-3665 (R9.3's computations -> C-items).
- C5: 1-41 status and summary (rewrite as the chapter's own summary); 327-356; every Rn.0 verifier block after
  folding; every Rn.5, Rn.6, Rn.7 (status lists, sources, paper texts: e.g. 1336-1402, 1559-1612, 1830-1859,
  1973-2103, 2281-2468, 2507-2658, 2701-2872, 2909-3103, 3215-3443, 3574-3856 except 3818-3856's lambda0 finding,
  3857-4372 except R14.5's figures).
- LAMBDA0-DATA5 1-39, 318-387; M22CERT5 1-58, 192-199; LOSS-D 1-24 and s.5's verifier dispositions (224-990: keep
  LD3, LD5-LD7, LD10-LD11 content, superseded in figures by C5); E2-PILOT 1-19, 774-877 (rewrite s.4 as a summary);
  INVERSE5-SCALAR 1-73, 259-286, 513-526, 566-661; INVERSE5-SIX 1-70, 401-469, 577-649, 735-743, 854-864, 914-919;
  EFFECTIVE-CONSTANTS 1-61 (verifier list), 358-441 (programme, sources).
- CERTIFY-10L5 1-177 (feasibility, plan), 762-769; CR 1-55 and every "Answers" block (452-503, 923-999, 1593-1657,
  2428-2472), every "Files and outputs", every "The paper: ..." block (897-914, 1287-1312, 2181-2248, 2889-3015,
  3204-3448, 3725-4093, 4313-4699, 4821-4866, 4904-5423, 5496-5512), every region-of-existence list superseded by
  13.4/14.1 (817-847, 2076-2104, 2784-2852, 3168-3180, 3680-3693, 4272-4286), and the n.0 blocks after folding.

## 4. Chapter plan (dependency order)

Each entry: purpose; sources (file:lines, with the approximate number of source lines the writer reads); folds and
exclusions (by reference to 2 and 3); dependencies; C-items (programs) and outside citations; estimated cleaned
length. Estimates exclude the C-list and the code appendix. Shape changes from the suggestion, with reasons:
(a) Part VI's GAUGEDECAY5 material needs three chapters (one per gauge, the harmonic gauge in two), because its
final text must be composed from 13 rounds; (b) "Beyond the boundary" (BEYOND5, SG) moves to Part VI, since it is
settling of Theorem 1's own solution and depends on Part S exactly as Theorem 4 does; (c) the constants of Theorem 4
form their own two chapters after Part S, because every number in them is a constant of Part S's write-out cited by
its line; (d) the families material needs four chapters and the equality case two.

### Part I. Introduction and statements

Ch 1. Introduction. Burnett's problem; Huneau and Luk's theorem quoted with page; what is proved (Theorems 1-4 in
words); why five dimensions and a black hole; relation to HL, Touati, LR; a scope paragraph (from the opening
sentence of each item of P s.9).
- Sources: P 14-148 (135), P 705-751 (47), P 1488-1906 first sentences only (~40). ~220 source lines.
- Exclusions: P 5-10, 41-47, 109-121. Replace "supplement (`proof5/`)" by "Part S", "the record" by nothing.
- Deps: none. Lit: [HL18] Thm 4.2 p.10 (quoted), (1.3)-(1.4), Def 3.2, Thm 3.3, Def 4.1, Rem 4.3; [HL24] Problem 8.6
  p.28; [LR20] (1.3) p.3, Thm 1.9, Cor 1.14; [Tou23a] Thm 2.2 p.12, Prop 7.1 p.13; [Tou23b]; Burnett; Isaacson.
- Estimate: 220.

Ch 2. Setting. The T2-mirror class and the reduction; five-dimensional Vaidya, the commutator; the curvature
boundary, D_T and Omega, Omega a domain of dependence; the waves (2.5') and their average; the wave-map gauge;
profiles and scaled norms, eps1 and s0.
- Sources: P 150-259 (110); NP 70-141 (72), 196-228 (33, Lemma 1.1 with proof). ~215.
- Folds: NP 0.3's D623/D625 brackets (style I). Exclusions: program names in Props 2.1-2.3 -> C1-C6.
- Deps: none. C-items: response5 R1-R4, R6, R12; ks5 K1-K5; ansatz5 A2-A3; lead5 L2; lemmas/hf_theorem5 F3;
  lemmas/kn_gauge; foliation5 B1, B4; eps1hyp5 H1-H6; lzerotrace5 T6-T7. Lit: [CBCM10] (2.7)-(2.9) p.8.
- Estimate: 260.

Ch 3. The theorems. Theorems 1-3 with Props 3.2-3.4 stated (proofs in Ch 8-10), how Theorem 1 follows from Theorems
A, D, E (the gauge propagates; symmetry by uniqueness); Theorem 4 stated; a list of the further results of Parts VI-VII
with forward references.
- Sources: P 261-466 (206) minus proofs 320-332, 340-357 (to Ch 8); P 1239-1259 (21); P 777-796 (20, linear statement);
  NP 143-194 (52: Thms E, A, D as stated, 0.7). ~280.
- Folds: Thm 1 item 5's uniqueness class and Thm 2 (P-v)'s class as in NP (D625, in place). Exclusions: 409-411.
- Deps: Ch 2. C-items: response5 R13-R14; support3 D2-D4; lemmas/counterpart5 P1. Lit: [LR05] p.1; [CBCL06] s.3;
  [CBCM10] Thm 3.3, (3.10)-(3.11) p.14.
- Estimate: 220.

### Part II. The approximant

Ch 4. The two-scale expansion and the approximant (Theorem A). Profiles, (4.1) equivariance, stage 0 and the
second harmonic chi, the ansatz with phase corrections, where each unknown first enters (Lemma 5.1), each stage a
linear hyperbolic system (Lemma 5.3), the approximant in Theorem E's form, (E1)-(E3).
- Sources: P 468-503 (36); NP 107-141 (scaled norms, if not in Ch 2), 309-320 (3.1), 533-627 (95). ~180.
- Folds: none beyond style (I). Exclusions: NP 535-538.
- Deps: Ch 2. C-items: lead5 L1-L5; ansatz5 A2-A3; support9 S6; stage5 S1. Lit: none essential ([Tou23a] for the
  comparison of transport and polarization conditions).
- Estimate: 180.

### Part III. Uniform existence

Ch 5. Inequalities on the slices. Sobolev and products; the compactly supported mollifier adapted to the annuli
(M1)-(M6); the energy inequality on Omega; the transport estimate.
- Sources: NP 229-308 (80); P 535-563 (mollifier text, 29). ~110.
- Deps: Ch 2. C-items: support5 C4, C14; eps1hyp5 H6; ks5 K4; gronwall5 G0-G1. Lit: [BH17] Thms 7.21, 7.26, 9.14.
- Estimate: 130.

Ch 6. The linear structure and Theorem E. The linearisation and its one coefficient of size 1/lambda; the
phase-shift identity; the decomposition w = h + phi [d_theta g1]; the ell-ell component; the commutator transport;
the bootstrap (Steps 1-7); existence, continuation and uniqueness with time lines along Z (Step 8); Theorem E at every
order (remark).
- Sources: NP 321-532 (212); P 505-602 (98, for exposition); NP 7231-7258 (28). ~340.
- Folds: style (I) in Steps 3, 8 (D623, D625). Exclusions: none else.
- Deps: Ch 4, Ch 5. C-items: support5 C1-C3, C6; support5b C10; support5c C11-C12; ks5 K3; ledger5 L2. Lit:
  [DS23] Thms 2.4, 2.6, (A1)-(A4), Rem 2.3(i); [AO14] Thm 1.1, Rem 1.2; [LY22] Thms 1, 26, Lemma 27; [SY21];
  [Tou23a] pp.12, 20-21 (comparison).
- Estimate: 330.

Ch 7. The data: the constraints solved outward in r (Theorem D), and the proof of Theorem 1 items 1-5. The two
identities; why the conformal method does not transfer; the gauge hierarchy and the stage data; the constraints as a
parabolic-hyperbolic evolution in r (5.6); the linear evolution by Faedo-Galerkin with its tame clause; the exact
correction by the Kato-Majda scheme; proof of Theorem D; the assembly 0.7.
- Sources: NP 629-961 (333) minus 631-645; P 603-649 (47). ~370.
- Folds: style (I) (D615-D616 in Lemma 6.2; D619 in Lemma 6.4's tame clause). Exclusions: NP 631-645.
- Deps: Ch 4, Ch 6. C-items: data5 S0-S6; csolve5 C7, C7c; gauge5 G1-G2; stagen5 S2-S5; tame5; indepcons5;
  symmshift5; response5 R5, R14. Lit: [Rac16] p.6, (3.3); [CD03] (2.1) p.4; [GO13]; [AG22] s.9, p.1; [AO14] s.4.1;
  [Tou23b] Thm 2.1, s.5.4.2 p.29 (comparison).
- Estimate: 330.

Appendix S1 (with Part III). Standard results used, each with its source, theorem number and page.
- Sources: NP 1044-1095 (52); VLASOV s.6 statements (309-347) if Part VII keeps them here. Estimate: 70.

### Part IV. The remaining parts

Ch 8. The boundary, the spheres' horizon and the mean mass. Prop 3.2 (x_K = 1 spacelike, margin for g_lam);
Prop 3.3 (one zero per column); the five-dimensional Hawking mass; the quarter-turn symmetry; Prop 3.4.
- Sources: NP 1102-1214 (113); P 297-357 (61); P 651-686 (36, for the remarks). ~210.
- Folds: style (I) (D622, D625). Exclusions: NP 1104-1106; numerics of P 667-686 -> C-items.
- Deps: Ch 3, Ch 6, Ch 7. C-items: horizon5 H1-H3, H2b; mass5 M1-M4; support3 D1; support5 C8; support5c C13;
  stage5 S2, S4; lemmas/hf_theorem5 F2, F4; lemmas/hf_core5; ansatz5 A5. Lit: none.
- Estimate: 170.

Ch 9. The construction from past null infinity (Theorem 2). The past domain; Sobolev with rotations; the mollifier on
the past slices and its commutator with the wave operator; decay classes; the approximant from past null infinity
(Theorem A_P); the far and near regions; the proof; the flux at past null infinity (9.10); items 6-7 for these
solutions (Prop 9.10).
- Sources: NP 1236-1694 (459), 1706-1751 (46); P 371-411 (41). ~550.
- Folds: style (I) (D622, D625, D632). Exclusions: NP 1217-1235, 1680-1693, 1695-1705; P 409-411.
- Deps: Ch 4-8. C-items: past5 P1-P9; redshift5 R9, R10, R14; ledger5 L1; gauge5 G3; horizon5 H2b; stage5 S4.
  Lit: [BH17].
- Estimate: 470.

Ch 10. Bondi coordinates and the mass law at past null infinity (Theorem 3). Every order at fixed lambda (Lemma 11.0);
the equation for u and the half-order gain; the expansion in r^(-1/2); the Bondi chart; the hierarchy in the class
and the five-dimensional Bondi law; the mean mass; comparison with the numerical solver as a computation.
- Sources: NP 10961-11379 (419); P 413-466 (54); P 687-703 (17). ~490.
- Folds: style (I) (D630 = SG R6-D, D632, D633). Exclusions: NP 10938-10960, 11380-11401 (-> C-item).
- Deps: Ch 9. C-items: bondi5 B1-B4; f1lemma5 F1a-F1d; cclass5 C1-C3; r5edits5 E2-E3; ledger5 L3; past5 P7;
  lemmas/hf_anchor5; lemmas/hf_core5. Lit: [TTS09] (28) (quoted at NP 11320-11342); [HL21] eikonal function.
- Estimate: 420.

### Part S. The stability theory (placeholder; mapped by another agent)

Interfaces this map needs from Part S, by proof5 part and result:
- S.1 linear: Part VIII Thm 2.2, Cor 2.3, Lemma 1.1; Part IX Lemmas 1.1-1.2, 2.1, Thm 2.2 (Steps 1, 3), Cor 2.3,
  Rem 2.4(c).
- S.2 nonlinear: Part VII Thm 0.2 (= Thm 4), Lemma 1.1, Props 2.2, 3.2, Lemma 3.1; Part V Def 2.1 and the gluing
  estimates; III.K Thm 4.3 and its data class (E_0, l0, d_1); Part IV's seven outputs; VI.C / VI4-PARAMS rows d1, d2,
  w1, w2; Part VI.A Thm 6.1 ((Dyn)).
- S.3 the operators GD uses at the box on 1-forms: I.A and I.C (spaces, low-energy theorems); II.C Def 2.7; II.E;
  II.F' Thm 1.1; II.G' Prop 3.3; III.A, A'; III.B s.3-6, (3.6), (4.1), (6.3); III.C; III.D Props 6.1-6.2; III.D'
  Lemma 2.1, Prop 4.1; III.H Lemmas 2.2-2.5, Prop 3.2, Thm 4.1, Cors 4.2-4.3; III.H' Thm 1.3; III.I (1.2); III.I'
  Lemmas 1.1, 2.2, Props 2.1, 3.1; III.I'' Prop 5.1; III.I''' Lemmas 1.1-1.3, Prop 2.1; III.J'; IV Props 3.1, 4.1;
  IV' Prop 2.2; IV'' Lemmas 2.2-2.3; IV''' Thm 2.1 (i)-(iii).
- S.4 inner radius: state every part with a general inner radius r_flat in (0, R_1/2] (BEYOND5 Prop 6.2;
  BEYOND5-R0-PROOF s.0-11, 17-482); then Ch 12 needs no separate re-proof.
- S.5 Theorem 1's solution after the shell as the assembly's input: NP 10.50 (a), (b), (d) (7183-7230) and Theorem E
  at every order (Ch 6's remark).
- S.6 the names Ch 17-18 cite: I.B:1513, I.B:1685, I.B:1978, III.F'':223, III.D:365, II.F:1393, I.C:497 (inverse
  bounds), III.J'' Thm 4.1 (the loss d), II.D:686 (kappa), III.D Prop 6.2 (the scalar wave operator); keep a
  concordance from these to the edition's numbering.

### Part VI. Settling at late times

Ch 11. After the shell: the reach of Theorem 4. No oscillation after the shell; the data near the hole are small in
every norm; equivariant gluing with only the mass to match; which decaying perturbations Theorem 4(ii) reaches,
directly or through gluing (GLUEDECAY5's Props 1-4, Thm 5); the pure-gauge examples outside the class.
- Sources: P 753-776 (24), 1180-1236 (57); NP 7183-7230 (48); GLUEDECAY5 22-576 (555). ~690.
- Folds: GLUEDECAY5's ten notes (2.3). Exclusions: 3.4.
- Deps: Ch 3, Ch 6 (every order), Part S (S.2). C-items: support8 K1, K8; support8b M2, M3; ledger5 L2, L4; flux5;
  mpdata5; gluedecay5 E1-E6. Lit: [CD03] Rem 8.2 p.36; [Hol08] Thm 1.1; [IK03] p.16; [ER08] (34).
- Estimate: 450.

Ch 12. The interior after the shell. Theorem 4's development continues inside the black hole up to the curvature
boundary; it and g_lam are one spacetime on the common domain of dependence; the half-integer data class.
- Sources: BEYOND5 18-251 (234), 885-937 (53); P 1748-1756 (9). ~300.
- Folds: BEYOND5's D3xx brackets (style I/R); Lemma 6.4 (iv) from SG R9.1. Exclusions: BEYOND5 252-884.
- Deps: Ch 11, Part S (S.2, S.4). C-items: r0census5; census9 C27. Lit: none new.
- Estimate: 220.

Ch 13. The development of g_lam's own data settles (no gluing). The half-order tail at past null infinity; it reaches
the data at spatial infinity; Theorem 4 in the half-integer class; the continuation to the far part's past domain of
dependence by one weighted energy estimate; uniqueness at weight a_0; the limit is vacuum; the theorem.
- Sources: SG components listed in 2.4 (~1,360) and its fold blocks (~640). ~2,000.
- Folds: 2.4. Exclusions: 3.4.
- Deps: Ch 9, Ch 10 (Lemma 11.0, Prop 11.1), Ch 12, Part S (S.2). C-items: tail5 T1-T9; wedge5 W1-W6; r5op5;
  r6sigma5 (W window); r5settle5 G1-G6; r9beyond5 B1-B5'''; f1lemma5; cclass5. Lit: none new.
- Estimate: 700.

Ch 14. The linear solution in a Regge-Wheeler-type gauge. The class carries no vector type and no l = 1; Kodama and
Ishibashi's gauge and the gauge vector; Theorem 1.5 (settling at Part VIII's rate, two derivatives lost); the
red-shift datum; [HKW18]'s data: energy decay on r <= R; uniformly in r, the exact weights r^(+-1/2) (RWGAUGE5); the
QNM and late-tail observations as computations.
- Sources: P 777-841 (65), 912-923 (12); NP 1902-2188 (287); GD 44-232 (189) with its fold lines (~120); RWGAUGE5
  45-298 (254), 357-453 (97), 476-564 (89). ~1,110.
- Folds: 2.2 (s.0, Thm 1.5), 2.3 (RWGAUGE5). Exclusions: 3.3, 3.4.
- Deps: Ch 2, Part S (S.1). C-items: settle5 T1, T3, T5, T6; support8 K8; kirecon5 P1-P2; redshift5; rwgauge5 R1-R5;
  rwgauge5u U1-U11; lemmas/seed_escape. Lit: [HKW18] Thms 1, 2, 16, 18, Lemma 11, (20), (115), (124), (127), (169),
  (173); [KI03] (3.14); [DR08] Thm 7.2 p.87; [CYDL03]; [CLY03b] Table 1 p.8; [Hol08].
- Estimate: 650.

Ch 15. The linear solution in harmonic gauge, I: structure, the horizon charge and decay modulo W*. The harmonic-gauge
solutions; the conserved horizon charge; forced linear growth; the explicit W*, K*, W**; the augmented zero-energy
operator of the 1-form wave operator; its 1-admissibility; decay modulo W*; the spherically symmetric sector; the late
region (S_K), (Ext box) and the harmonic gauge on all of N+.
- Sources: P 842-872 (31); NP 2189-2314 (126); GD 233-334 (102), 511-744 (234), 852-887 (36), 1029-1332 (304),
  1436-1662 (227), 1979-2127 (149); fold blocks 1047-1126, 1706-1876, 2202-2234, 2735-2857 (~400). ~1,610.
- Folds: 2.2 (A1-A56 as listed). Exclusions: 3.3.
- Deps: Ch 14, Part S (S.1, S.3). C-items: wavegauge5 W1-W7; hung4 (control); gdrepair5; hgauge5; gdsk5; gdix5;
  gdr3fix5; gdrate5; gdext5; gdkplus5; admbox5. Lit: [Hun19] (4.11)-(4.23), (8.1), (8.38)-(8.39), Thms 1.1-1.4;
  [BGP] Cor 3.2.4; [KI03b].
- Estimate: 700.

Ch 16. The linear solution in harmonic gauge, II: the rate. The rate at K+-weight in (1,2); compactly supported gauge
data; past the window for sources of zero total charge; the explicit solution of charge 4 pi^2 and the t*^(-2) term;
the spherically symmetric part; the subspace l >= 2 (projections, (G), (Z), (TF), I.C, (M)); the representative and
its rate tau^(-min(p,3/2)+eps).
- Sources: GD 2393-2590 (198), 2636-2649 (14), 3218-3529 (312), 4007-4393 (387), 4884-4989 (106); fold blocks
  3109-3217, 3877-4006, 4726-4883, 5521-5636, 6070-6158, 6628-6726, 7191-7223 (~790). ~1,810.
- Folds: 2.2 (A57-A132 as listed). Exclusions: 3.3.
- Deps: Ch 15, Part S (S.3). C-items: gdscri5; gdrad5; gdtail5 T1-T13; gdlge2_5 L1-L10; gdr9_5 N1-N6. Lit: Riesz's
  Green function of the 4+1 wave equation (for Lemma R7.2's T1; supply a citation).
- Estimate: 650.

### Part S'. The constants of Theorem 4 (after Part S; may sit inside Part S)

Ch 17. Explicit resolvent bounds on five-dimensional Tangherlini. The scalar wave operator harmonic by harmonic:
off the real axis, the flux, growth through the barrier, uniformity in l, above the barrier, Morawetz bounds for
every l (certified), l = 0, one derivative, large sigma; the absorption, parametrix and Schur lemmas; the
scalar-type zero-energy blocks and the weight obstruction.
- Sources: E2-PILOT 20-773 (754); INVERSE5-SIX 109-214 (106), 560-576 (17); INVERSE5-SCALAR 74-258 (185). ~1,060.
- Folds: INVERSE5-SIX R3-R5 (650-919) where they touch Lemmas R1-R9; INVERSE5-SCALAR's in-place notes.
- Deps: Ch 2; Part S only for where the bounds are used (S.6). C-items: e2pilot5, e2band5, e2morawetz5, e2certify5,
  e2lzero5, e2cplx5, e2h1_5, e2meas5, e2lower5, e2trapband5_384, e2h1band5, scalarblock5, inverse6_5 (K6),
  inverse6_5m. Lit: none new.
- Estimate: 450.

Ch 18. What the proof of Theorem 4 makes explicit. The loss d and the regularity N = 21d + 6 (structure, the six
losses, weights and loops; the floor and the integer bound at the computational point, which lies outside the proved
set); the root avoidances; delta and lambda1: what is bounded, and where explicit evaluation stops (compactness,
contradiction and Fredholm arguments).
- Sources: P 1488-1603 (116); LOSS-D 25-223 (199) and LD3, LD5-LD7, LD10-LD11 (~250); C5 149-326 (178) and the
  d-chain of 2.7 (~900, read selectively, final figures 3857-3866); INVERSE5-SCALAR 287-565 (279); INVERSE5-SIX 71-108,
  215-400, 470-559 (~390); EFFECTIVE-CONSTANTS 62-357 (296). ~2,400 (the writer reads statements and summaries).
- Folds: 2.7. Exclusions: 3.5.
- Deps: Part S (S.6), Ch 17. C-items: census9 C29; level2loop5; lambdacount5; epsind5 E3; eind5 E2; eindcert5;
  thetain5; prop31loss5; charge5; dnumber5; x7indep5; modcount5; d0count5; ordcensus5; l2par5; logind5; iotaind5;
  rootavoid5; deltacap5; inverse6_5a; zeroext5; tensorzero5; support9 S3. Lit: [Hin26a] Thm 4.9 p.37.
- Estimate: 450.

### Part VII. Further results

Ch 19. Two crossing null dusts. The two-dust Vaidya-type background on the whole domain; the phases; the approximant
to every order with interactions and non-resonance; Theorem E_2 with Lemma 3.3_2 and Steps 4-7 in full; the data;
items 6-7 for two families.
- Sources: FULL 42-345 (304), 504-742 (239); FAMILIES5 121-835 (715, the inputs FULL cites). ~1,260.
- Folds: 2.6 (two dusts). Exclusions: 3.5.
- Deps: Ch 4-8 (mirrored proofs; the chapter states the changes, not a second copy). C-items: stage0two5; twophase5;
  twobg5; twoslice5; nonres5; twotransport5; twoext5; twodecomp5 J0-J9; twoledger5 T1-T2; twohorizon5 H1-H3;
  h3proof5; twoparity5 P1-P4; twodomainx5; twodomain5. Lit: [HL18] angular separation Def 4.1.
- Estimate: 600.

Ch 20. The class Einstein-null-dust system: non-round backgrounds, the axes and Cauchy stability. Permitted null
phases; angular separation fails at the axes; the class structure; the augmented system and its energy hierarchy
(Thm N); the axes (Prop X, Lemma A, Thm N'); Kato's iteration with a non-local source (Thm K -> K'); interior
regularity (Lemmas E, A').
- Sources: FULL 346-400 (55); NONROUND 53-358 (306); AXIS 212-384 (173); VLASOV 307-347 (41); R6 413-443 (31). ~610.
- Folds: 2.6 (NONROUND's eight dated notes; AXIS [R5]/[R6]). Deps: Ch 19. C-items: classchi5 C1-C4; augment5;
  axisloss5 X1-X3; axisellip5 E0-E2; axisphase5; katonl5 K2. Lit: [Rac16]; standard elliptic and Kato references.
- Estimate: 450.

Ch 21. Restricted massless Vlasov limits. Burnett limits in the class carry no torus stress; restricted fields at the
axes; Theorem V (N-dust approximants uniform in N, torus-polarised waves at frequencies 1, Lambda, ...,
Lambda^(N-1), data with overlapping families, the N-family estimate, the diagonal choice); openness (Lemma O'') and
non-vacuity (Prop NE).
- Sources: FULL 401-503 (103); AXIS 385-433 (49); VLASOV 67-242 (176); R6 286-412 (127); R7 176-193 (18); R8
  243-318 (76). ~550.
- Folds: 2.6 (Vlasov). Deps: Ch 19, Ch 20. C-items: torusstress5 V2; vlasov5; vlasovhf5 H1-H7; twoscale5 T1;
  nfamily5 N1-N5; nledger5; vlasovex5; axisphase5. Lit: the Vlasov literature READ at FULL 403-453 (as citations).
- Estimate: 450.

Ch 22. Localised data and the sign of the charge. Exact localisation on cones; Racz's split on Part I's slice and the
band where it fails, a slice bent by 0.0012 (certified); exact compact support; the charge of momentum seeds (Thms
Q, Q', at the axes); seeds that perturb the metric: M_b fails inside the horizon (Thms T, X), holds outside (Thm P,
renamed), via Kodama-Ishibashi energies.
- Sources: AXIS 75-211 (137); VLASOV 243-295 (53); R6 130-285 (156); R7 95-175 (81); R8 93-242 (150), 319-359 (41),
  432-480 (49); MB 87-380 (294); R10 12-90 (79); R11 14-76 (63). ~1,100.
- Folds: 2.6 (localised data). Deps: Ch 14 (GD Lemma 1.2, the class harmonics), Ch 7. C-items: bandconst5 B4, B6;
  racglobal5 R1-R4; racslice5 S1-S3; intcert5 C1-C3; truebg5 T1-T4; qsign5 Q1-Q7; mbsign5 E1-E9; mbslice5 S1-S5.
  Lit: [Rac16] Lemma 4.1; [CS06] Thm 2; [CD03] Thm 5.6; [KI03]; Hollands-Wald (R8.7).
- Estimate: 550.

Ch 23. The boundary at equality, I: the seed region and the layer. g0 at equality; the seed region is exact; the
boundary and a domain of dependence at equality; the spheres' horizon at equality; the layer: the term linear in the
wave, the angular factor, flat-edge bounds and the weighted remainder, Theorem L and Cor L.7; Theorem 2's solution
(L_P); the layer region by region (L.12-L.14); lambda_L.
- Sources: EQUALITY5 23-209 (187); EL 12-244 (233), 312-718 (407), 981-1142 (162), 1474-1506 (33), 1548-1585 (38);
  folds R2.0 285-311, R3.1 919-980, R4.6 1586-1651 (~150). ~1,210.
- Folds: 2.5. Deps: Ch 6-9. C-items: eq5 E1-E6; layerlin5 N0-N6; layerwin5 W1-W3; layerpast5 P1-P3; layernull5
  E1-E6; layerledger5 L2; layerband5 B1-B2; bandL4p5 H1-H4. Lit: none new.
- Estimate: 600.

Ch 24. The boundary at equality, II: the very edge and the dips. Exact re-summation and the kernel lemma; degree two
and localisation at every depth; Theorem L_E (Theorem 2's solution); Theorem 1's solution in the deep layer and at
the very edge, one theorem (L_1E''') with one proof; one switch per column (L.24); dips (L.25''); the hypotheses for
a C_c-infinity envelope (L.27); the constants C_L11, C_L4 and lambda_25.
- Sources: EL 1279-1473 (195), 1838-2211 (374), 2354-2533 (180), 2726-2910 (185), 3055-3255 (201), 3395-3549 (155);
  folds R5.1, R6.0, R6.3, R7.0, R7.5, R8.0, R8.6, R9.0, R9.5 (~500). ~1,790.
- Folds: 2.5 (the L_1E chain). Deps: Ch 23. C-items: edgeP5 Q1-Q4; degtwo5 T1-T6; constL5 K1-K4; edge1_5 X14-X17;
  hyp5 H0-H5; eqlayer5; bfam5. Lit: none new.
- Estimate: 600.

Ch 25. lambda0 at the numerical point. The threshold lambda0 traced term by term: eps1 and s0, C_app, the three
norms (operator 0.0024433, Frobenius 0.0019079, largest entry 0.0012228, certified); the first stage's mean
correction M_22 (2.207738, floating point) and why it is not certified (the a posteriori estimate's factor 1.8e14).
- Sources: P 1604-1621 (18); C5 42-148 (107), 885-1113 (229), 1403-1449 (47), 1613-1692 (80), 1756-1793 (38),
  2204-2241 (38), 3818-3856 (39), and R2-R3 where cited (357-884, read selectively); LAMBDA0-DATA5 40-317 (278),
  388-904 (517); M22CERT5 12-191 (180), 200-260 (61). ~1,650 (+ selective 530).
- Folds: 2.7. Deps: Ch 2, Ch 6, Ch 7. C-items: lzeroaudit5; lzeroconst5; lzerotrace5 T2-T7; r6fixes5 F1; r7fixes5;
  stage1cap5; stage1rate5; classm5; envelope5; lam0data5; m22evol5; m22cert5. Lit: none new.
- Estimate: 300.

Ch 26. At the prescribed wavelength 10 l5. No separation of scales at 10 l5 (the ratios); the solver's scheme and its
breakdown; the second zero belongs to the areal spheres (two deductions); the characteristic problem in double-null
gauge; certified constraint and residual bounds; the linear estimates (Theorems 7.L, 8.W, 8.L1) and the axis charts;
existence by continuity (Lemma 9.C) and why its closing condition fails at the computed constant; what holds: existence
where the solution is the seed.
- Sources: P 1621-1747 (127); NP 1796-1901 (106); CR 56-305 (250), 677-723 (47), 1000-1132 (133), 1511-1592 (82),
  1658-2042 (385), 2473-2701 (229), 4798-4820 (23), 4867-4880, 5477-5484 (22); CERTIFY-10L5 178-761 (read for C-items
  only). ~1,400 (+ fold blocks 1313-1428, 2258-2427, 3026-3155 ~420).
- Folds: 2.7 (CR). Deps: Ch 2, Ch 8. C-items: growth5; response5 R7; excise5; g5angle5 A1-A2; sectexp5; secondzero5;
  szconv5; cdata5; resid5; rcert5; rcert5b; rcert5d; rich5; reduce5; null3; linest5; lev1_5; wgron5; axis5;
  axisbianchi5; axhier5; cont5; blocks5; blockw5; symbol5s; cpaxis5; cp3grid5; late5; late5b; mtrunc5; g1curv5;
  dnsolve5; lemmas/seed_escape. Lit: [Wu26] Thms 2.1-2.2, s.2.3 p.6; [CTG23] Thm 1.1; [AB26] s.3.1 and its [4].
- Estimate: 450.

Ch 27. Scope. What is and is not claimed, collected: Theorems 1-3 on Omega only; below the inner boundary (l5 is
arbitrary; at r = 0 the limit is singular); no inner or Cauchy horizon; lambda0, lambda1, delta not evaluated; at
10 l5 existence only where the solution is the seed; Hung's route not needed; the decay of the components in other
gauges and its exact weights.
- Sources: P 1782-1787 (6), 1604-1621 and 1739-1747 (closing sentences), 1599-1603; the "what is not claimed"
  sentences of Ch 11-26. ~80. C-items: innerr5 I1-I2. Estimate: 80.

Totals: 27 chapters and Appendix S1 (Part S not counted). Estimated cleaned length about 11,150 lines: Part I 700,
Part II 180, Part III 860 (with S1), Part IV 1,060, Part VI 3,370, Part S' 900, Part VII 4,000 (families 2,050,
equality 1,200, lambda0 300, 10 l5 450), scope 80. If the edition must be shorter, Part VII's Ch 20-22 and Ch 24
compress best (deduced material with long hypotheses), then Ch 18.

## 5. Risks

### 5.1 Final form spread across files or rounds (highest risk first)
1. GD: 132 amendments listed apart from their sites (style L), about 75 "read as" notes (style R), 13 rounds. A writer
   who reads a result where it first appears composes a superseded text: e.g. Lemma R7.2's display still prints
   r^(-2)H(t) at 3330, which (A76) corrects to H(t - r); Cor R6.6's proof (A60) and Lemma R8.8's index argument (A94,
   R9.a) were re-derived elsewhere. Use 2.2 result by result; budget a checking pass for Ch 15-16.
2. EL: Theorem 1's very edge exists in five successive versions (L_1E, L_1E', L_1E'', L_1E''', with Prop L.26, L.27,
   L.28 added); the final proof must be written once from five places (2.5). Round-1 sketches (L.3, L.4, L.17_P,
   L.18_P) were replaced; do not cite them.
3. SG: the proof of Thm R5.1 is "R4.10 with three substitutions", across ten rounds and 75 later notes, and it uses NP
   s.9, s.11.1, BEYOND5 and Part S (2.4).
4. Families: eleven files, each amended by notes from later files (Prop L -> Thm L'' -> Thm L'' with the moved lobe;
   Lemma O -> O' -> O''; Thm V restated in R6; Thm Q at the axes R7 -> R8.6). Order of authority in 2.6.
5. C5 and LOSS-D: d's value and derivation moved in ten rounds (from 7.95e15 floors to the integer 46,236,517,538,
   883,361); LOSS-D's own figures are superseded by C5's. lambda0's three norms come from three rounds (R4, R6.0, R7.0).
6. CR: section n is amended only in section n+1's ".0" block (style L), never at the site.
7. Theorem 1 items 6-7 have five homes: P Props 3.3-3.4, NP Props 8.1-8.2, NP Prop 9.10 (Theorem 2's solutions),
   EQUALITY5 Prop E.5 (equality), FULL Props 8.1_2-8.2_2 (two dusts). Keep one proof and state the variants as
   corollaries.
8. Stale line citations: SG and BEYOND5 cite NP by old line numbers (e.g. "N1STAR-PROOF.md:10551-10579", "(1197)",
   "(10516-10560)"; SG 312 notes some as stale); GD cites proof5 parts by line ("IX:131-134", "B:345-352",
   "K:35-37"); (A24), (A58) say to read them by name. Resolve every such cite by content, and get a line-to-result
   concordance for proof5 from the Part S agent (S.6).

### 5.2 Conflicting or weak statuses
1. Never promoted to "proved" at source, though P states them: all of Part VII's families results (DEDUCED, read
   round by round), EQUALITY5-LAYER (DEDUCED; P: "deduced ... whose rounds 1-9 independent verifiers have read"),
   BEYOND5 Props 6.1-6.2 and Lemma 6.3 (DEDUCED), NP 10.50-10.51 (DEDUCED, "nothing proved"), CR's deductions (s.1.2;
   axis hierarchy s.8.2, 9.5 "identities verified at random jets"), LOSS-D, EFFECTIVE-CONSTANTS. The edition's rule
   "complete proofs" will present them as theorems: the author must accept that, or mark them as propositions with
   proofs in outline. Note that P labels Theorem 1 itself "deduced" while NP labels Theorems A, D, E "PROVED": in
   NP's usage "deduced" means "argued in full"; elsewhere it often means less.
2. Hung's route (NP 10.5-10.11, P 872-910) is "deduced below, not proved" and is used by nothing proved: drop it or
   keep one sentence; never state it as a theorem.
3. E2-PILOT's own status line (8): "sections 1-3, 3d, 3g, 3h and 3i to be read"; C5's round 15 and SG's round 10
   wording, and LAMBDA0-DATA5's s.13-14, were read by one reader each; INVERSE5-SIX round 1 was "not yet read" until
   rounds 3-5.
4. GLUEDECAY5: this map assumes, from its own header, that rounds 2-5 changed s.1-6 only through the ten notes at the
   sites; check R2.0-R5.0 (1765-2106) once before composing Ch 11.
5. Checks at sample points standing for identities: P's (6.2) and the Bianchi identity "at a point of a random 4+1
   metric" (response5 R14, gauge5 G1): both have hand proofs (NP 6.1, the contracted Bianchi identity); use those.
   NP Prop 10.2 (iii) is "checked at l = 2 and 4" (W4) for a statement about every even l: confirm that nothing in
   Ch 15-16 uses (iii) beyond l = 0 (GD uses (i), (iv), W*, K*, W**). GD Lemma 8.4-type root statements "for l <= 12,
   the rest deduced" belong to Part S.
6. Computational point outside the proved set: every constant in Ch 18 and parts of Ch 17 is computed at gamma_C =
   10^6, gamma_Upsilon = e_Upsilon = 1/100, which the write-out does not show to satisfy its own thresholds
   (P 1526-1531). The chapters must say so in the statement, not in a footnote.

### 5.3 "Proved" results resting on what the edition cannot include
1. Everything in Part VI and Ch 17-18 rests on Part S (proof5); Ch 13 also on Part IV's seven outputs, III.K Thm 4.3,
   Part VII Lemma 1.1 and Prop 3.2. If Part S is abridged, these chapters become conditional.
2. Part S's own reliance on readings of Hintz's papers at n = 4 (P 1100-1142, 1430-1446) is outside this map but
   inherited by every settling result.
3. Black-box literature with no five-dimensional or bundle form in print, used as stated: [HKW18] Thms 2, 16, 18
   (Ch 14, applied "as stated" in 4+1); [KI03] (3.14) (Ch 14, 22); [Wu26] Thm 2.2 is quoted only as structure, not
   used (Ch 26); [CTG23] Thm 1.1 (Lemma 9.C); [Rac16] Lemma 4.1 (Ch 22); [CS06] Thm 2 and [CD03] Thm 5.6 (Prop L');
   [DS23], [AO14] (local theory, Ch 6). Each needs its exact statement and page in the edition (NP 1044-1095 has most).
4. Riesz's Green function for the 4+1 wave equation (Lemma R7.2, computed T1) is cited by name only: supply a source.
   More generally P's bibliography (s.10, 47 keys) lacks what the supplements cite: [BGP] Cor 3.2.4 (GD), [CS06]
   Thm 2 (VLASOV Prop L'), Hollands-Wald (R8.7), Kato's iteration (VLASOV Thm K), the Vlasov literature READ at FULL
   403-453, Riesz; and Ch 1's "Burnett" and "Isaacson" if named. Add them with theorem and page.
5. Numerical support only (must stay C-items, never premises): the solver comparisons (P s.6), QNM and tails
   (settle5), growth5 and the double-null runs (Ch 26), M_22 = 2.207738 (floating point), C5's "computed, floating
   point" items.

### 5.4 Naming and notation collisions to settle before writing
- "Theorem P" is NP's construction from past null infinity and FAMILIES5-MB's positivity outside the horizon;
  "Lemma A" is AXIS's planar shear and RWGAUGE5's Sobolev lemma; "Proposition L" (AXIS, VLASOV) collides with EL's
  L-series; "Theorem K" (VLASOV) with GD's K-labelled checks; Props 3.3/3.4 (P) = Props 8.1/8.2 (NP); Theorems A,
  D, E, P, M (NP) vs Theorems 1-3 (P). One numbering for the edition.
- N is both the approximant's number of stages and the Nash-Moser regularity N = 21d + 6 (P 1508-1509); theta is the
  phase and also the polar angle (NP 8.1 renamed the angle vartheta at D622); mu0 is the seed mass and also GD's hole
  mass (A75, A88-A89: m, varpi_K); lambda is the wavelength and also the spectral parameter and the indicial root in Part
  S and Ch 16-18; K is the Kretschmann scalar, the approximant's order and GD's mass change (K = r^(-2) dv^2).

