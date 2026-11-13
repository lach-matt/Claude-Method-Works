# Outline S: the five-dimensional stability theory (map of `proof5/` for the reader's edition)

Scope: `research/warp-drive/docket68/n1star/proof5/` (78 Markdown files, 47,972 lines; 76 PART files, README,
BASEPOINT-LEDGER) and `proof5/checks/`. Paths below are relative to `proof5/` unless stated. "N1STAR" means
`../N1STAR-PROOF.md`; "R0P" means `../BEYOND5-R0-PROOF.md`. Line numbers are as of 2026-11-13.

Abbreviations used in this outline only (none may appear in the edition):
- Part labels: the files call each other by Part labels. Primes are written as digits here: III.I(k) = III.I with k
  primes. File map: I.A=I-SPECTRAL, I.B=I-B-HIGHENERGY, I.C=I-C-LOWENERGY; II.A=II-A-SETUP, II.A1=II-A2-STANDARD,
  II.B, II.C, II.C1=II-C2, II.D, II.D1=II-D2, II.E, II.F=II-F-IOTA, II.F1=II-F2-TAME, II.G=II-G-NASHMOSER,
  II.G1=II-G2-DECAY; III.A, III.A1=A2, III.B, III.C, III.C1=C2-POLYHOM, III.C2=C3-BOOSTDATA, III.D, III.D1..D3=D2..D4,
  III.E, III.E1=E2, III.F, III.F1..F4=F2..F5, III.G, III.G1..G4=G2..G5, III.H, III.H1=H2-ADMISS, III.H2=H3-UNIFORM,
  III.I=I-CONE, III.I(k)=PART-III-I(k+1)-* (so III.I(14)=I15-AUGMENT5, III.I(15)=I16-BASEPOINTS), III.J,
  III.J1..J3=J2..J4, III.K; IV=IV-EB, IV(1)..IV(6)=IV2-TAME..IV7-TFACE; V; VI.A=VI-DYN, VI.B=VI2, VI.B1=VI3,
  VI.C=VI4-PARAMS; VII; VIII; IX.
- "body a-b": from the first section heading to the line before the closing findings/sources section; the short
  intro between the status paragraph and the first heading is added in 1.8's "kept" range.
- BB = outside result cited as a black box (statement and page given in the file); W = outside proof written out at
  n = 4 in the file. Every [Hin26c]/[Hin26]/[Hin23a]/[Hin26a] section a file "proves at n = 4" is W.
- Programs: `p5c/x.py` = `proof5/checks/x.py`; `n1c/x.py` = `n1star/checks/x.py`; `n1/x.py` = `n1star/x.py` (the
  root); MISSING = cited but in no directory of the repository.

Sizes: the 76 parts have 46,029 lines, of which 39,927 are mathematical body (from the first section heading to the
closing findings) and about 6,100 are status paragraphs, short intros and closing findings/sources; README (1,483) and
BASEPOINT-LEDGER (460) are not mathematics.

## 1. Per-file map

Rows are written as records (one block per file) because the 121-character limit cannot hold a table row with these
fields. A one-line index of all 78 files, with the chapter each feeds, closes the section (1.8).

### 1.1 Part I: the spectral family on bundles ([Hin26c] section 9 at n = 4)

**I.A `PART-I-SPECTRAL.md`** (1,940 l.; body 30-1889; tail 1890-1940)
- Proves: Thm 7.2 = [Hin26c] Thm 9.5 at n = 4 on a trivial bundle of any rank (bounded nonzero frequencies; Fredholm,
  invertible, regularity, meromorphic) for constant regularity order; Thm 8.1 constants uniform in the operator.
  Tools: L3.1-3.2 (one regularised positive-commutator step, iteration), radial estimates P4.2 (horizon), P4.6
  (R_in), P4.9 (R_out), L4.8 = [Hin26c] L9.13 corrected (sign of (9.45)), P5.1 elliptic, P5.2 propagation, P6.3-6.4
  and C6.5 (artificial boundary: H^1 and all orders, energy method), L7.1 admissible orders.
  Hypotheses (H1)-(H5) of section 1 are the interface every later part instantiates.
- Status (l.3-15): Proved (D197). README row agrees.
- Uses: nothing earlier. Lit: [HJS] BB (L. notes on non-elliptic Fredholm theory: (2.1), Prop 2.3, Props 3.7, 3.11,
  3.13, 4.9-4.10, Def 7.2, Props 7.4-7.5, §7.5, §10.1-10.3, L12.5; pp. 9-95); [Hin26c] §9.1-9.2 W, its L5.12 W (L2.4).
  N1STAR: 10.84, 10.86 replaced (mentions 10-12, 1390, 1887, 1898 are provenance).
- Amended: only in place (D186-D197), inline tags on 30 body lines. External: R0P §2 re-reads it with the inner radius
  r_flat (Part I's r_0 put at III.B's radius; see VI.A).
- Programs: `n1/hthresh5.py` (l.708, the horizon threshold of the actual operators).

**I.B `PART-I-B-HIGHENERGY.md`** (2,133 l.; body 26-2055; tail 2056-2133)
- Proves: Thm 1.3 = [Hin26c] Thm 9.16 at n = 4 (high frequencies, semiclassical, trapping with loss), uniform in the
  operator (§9). §2 proves the semiclassical scattering calculus with matrix symbols and variable orders (Def 2.1,
  Thms 2.4 composition, 2.5 adjoints, 2.7 L^2 bound, P2.8, P2.10, L2.11-2.12); §3 commutator scheme (L3.1-3.4); §4
  elliptic and propagation (P4.2, P4.5, C4.6, C4.6'); §5 radial (L5.1, P5.2 horizon, P5.3, P5.5, P5.7 b-regularity);
  §6 trapping (L6.0 fibre inner product = [Hin26c] (5.9); P6.1, L6.2-6.3 defect measures, P6.4 loss one, P6.7, Thm
  6.8 = [Hin26c] Thm 9.28); §7 artificial boundary (P7.1-7.2, C7.3); §8 proof (P8.1-8.2). Hypotheses (H6)-(H8),
  (Gamma.1)-(Gamma.4) of §1.5.
- Status (l.3-13): Proved (D231). README agrees.
- Uses: I.A (73 cites: setting, L4.8, P4.2/4.6/4.9, C6.5). Lit: [HJS] BB via I.A; [Hin26c] §9.3 W; [HV16] Thm 4.7 and
  [Dya16] L2.3 followed through [Hin26c] (W); [Hin17] P3.12 (L6.0) W; [DZ19], [Hin25a], [VZ00], [Zwo12] replaced.
- Amended: in place (D189-D231; L6.0 added D226 at 1293; C4.6' added D189 at 924). External: R0P §0 (I.B's band
  |r-r_h|<delta_0 at 1067 holds in a smaller band).
- Programs: none.

**I.C `PART-I-C-LOWENERGY.md`** (1,512 l.; body 32-1434; tail 1435-1512)
- Proves: Thm 3.1 = [Hin26c] Thm 9.36 (zero energy operator, Fredholm on b-spaces); Thm 4.3 = Thm 9.38 (transition
  face normal operator); Def 5.1 tf-admissibility, C5.2 = Cor 9.39, P5.3 = Prop 9.40 (asymptotically Minkowski,
  weights (0,2), Hankel functions); Thm 6.4 = Thm 9.41 with Rmk 9.42 (uniform low-energy estimates, with an adjoint
  estimate the source lacks); C6.6 = Cor 9.43 (index 0); Thm 7.1 uniformity. §2: b-analysis at a conic end (Mellin,
  indicial family, model estimates, Def 1.1 indicial roots and gaps, Defs 2.1, 2.8, L2.2-2.9). R6.7: weaker than the
  source (smallness may depend on the b-order; no uniformity in the weight).
- Status (l.3-10): Proved (D194). README agrees.
- Uses: I.A (76), I.B (7). Lit: [HJS] BB via I.A; [DLMF] BB (10.2, 10.7.7, 10.17.2, 10.17.5-6; §5.2); [RS1] Thm VI.14
  BB (analytic Fredholm, L2.4); [Hin26c] §3.2.2-3.2.3, (3.72), Def 5.10, §9.4-9.6 W.
- Amended: in place (D191-D194). External: none.
- Programs: MISSING `checks_c.py` ("in the working notes", 455, 779, 830; sympy).

### 1.2 Part II: the e3b framework, forward problems, Nash-Moser, decay ([Hin26c] §§2-8, 10-13 at n = 4)

**II.A `PART-II-A-SETUP.md`** (1,595 l.; body 36-1497; tail 1498-1595)
- Proves: compactified spacetime and b-, 3b-, eb-, e3b-structures (§§1-2, Defs 1.1-1.3, 2.1, 2.4, 2.8; L2.2-2.11; C2.3
  = [Hin26c] C2.12, C2.7 = C2.16); e3b-calculus at n = 4 (§4); Fourier transform near K+ (§5), Mellin at iota+ (§6);
  supported/extendible spaces (§7, P7.4 = P3.18); finite regularity, multiplication, Sobolev embedding (§8, L8.2-8.8);
  elliptic and real principal type with b-regularity and tame versions (§9: P9.1 = P3.23, P9.2 = P3.24, P9.6, C9.7,
  P9.8-9.9). Standing inputs (L3)-(L4) = proved in II.A1.
- Status (l.3-18): proved (D197) at the end of the paragraph.
- Uses: I.A, I.C (15), II.A1 (11). Lit: [SBG] BB (scaled bounded geometry calculus; (S1)-(S11) listed in §3 =
  343-447, Defs 1.1-4.20, Props 3.19-4.22, Thms 3.21-3.52, pp. 43, 66, 73-74); [HJS] consulted; [Hin26c] §§2-3 W.
- Amended: in place (D194). R0P §2 (artificial boundary at r_0^A, l.38-39).
- Programs: none.

**II.A1 `PART-II-A2-STANDARD.md`** (839 l.; body 29-785; tail 786-839)
- Proves: (L3) = Thm 3.1 (elliptic estimate) and (L4) = Thm 5.4 (real principal type propagation), [Hin26c] Props
  3.23-3.24 at k = 0 for coefficients of finite regularity, variable orders, locally uniform constants; P2.4 (calculus
  of finite regularity by mollification), L4.1-4.2 commutator lemma, P5.3.
- Status (l.3-12): Proved (D197).
- Uses: II.A (37), I.A (9: L3.1-3.2, P5.2). Lit: [SBG] BB as in II.A; [Hin26c] pp. 55, 68-71 W; standard theorems by
  name (closed graph, Banach-Steinhaus, Hahn-Banach, Gronwall, IFT, ODE).
- Amended: in place (D195-D197; 13 tagged body lines). Programs: none.

**II.B `PART-II-B-DYNAMICS.md`** (746 l.; body 30-694; tail 695-746)
- Proves: null-bicharacteristic dynamics of the stationary model in e3b-phase space under (K1)-(K4) and Part I's
  hypotheses: P6.1 = [Hin26c] P4.21 (dynamics over the Kerr face via the map Phi_{z0} to I.B's phase space), P8.1 =
  P4.24 (global dynamics, (4.72)), P8.2 (curves over the interior; the form of [Hin26c] P6.1); closed-form flows near
  iota+, scri+ and the corner (§§3, 7); L1.1-7.3.
- Status (l.3-12): Proved (D326).
- Uses: II.A (24), I.B (23), I.A (11). Lit: [Hin26c] §4, pp. 77-99, 110-113 W; [HPS77] terminology only.
- Amended: in place (D197, D326 at 349). Programs: none.

**II.C `PART-II-C-OPERATORS.md`** (858 l.; body 30-795; tail 796-858)
- Proves: stationary wave-type operators = those whose spectral families satisfy (H1), (H2), (H6) (L1.2); tensor wave
  operators (L1.3); normal form at scri+ (L1.4); trapping and tf-admissibility, admissible orders, aleph-admissibility
  (Defs 2.1-2.7, L2.5-2.6); time function t_*^flat with an explicit gluing (L3.2), asymptotically stationary metrics
  and admissible operators (Defs 3.1-3.6, L3.4, L3.7); P4.2 = [Hin26c] P6.1 (incl. backward half); P5.1 = P6.4 (order
  functions, [Hin23c] App. C written out).
- Status (l.3-15): Proved (D327).
- Uses: II.B (40), II.A (18), I.A, I.B (17 each), I.C (9). Lit: [Hin26c] §§5-6 W; [Hin23c] App. C W (no input).
- Amended: in place (D200, D226, D326-D327). R0P §0 notes L3.2 (1) covers {r >= r_0^A} only (used by III.K, VIII).
- Programs: none.

**II.C1 `PART-II-C2-TRAPPING.md`** (435 l.; body 32-400; tail 401-435)
- Proves: Thm 1.1 (persistence of stable/unstable hypersurfaces of the trapped set for metrics decaying to the
  stationary model, by a graph transform, quantitative); P3.4 = [Hin26c] P6.3 at n = 4 (stable one in C^{d0-2}).
- Status (l.3-15): Proved (D328).
- Uses: II.B (10), II.C (8), I.B (6). Lit: [Hin21] Thm 2.6 replaced (not an input); [Hin26c] §6 W.
- Amended: in place; T_flat := 2/C' (D327-D328) at 296-299, 381-382. Programs: none.

**II.D `PART-II-D-REGULARITY.md`** (1,104 l.; body 37-1042; tail 1043-1104)
- Proves: Thm 1.2 = [Hin26c] P7.1 (global edge-3b regularity estimate, loss one at trapping); radial estimates P3.1-3.3,
  P3.5-3.6 (= P7.4, 7.6-7.9); P4.2 = P7.10 (trapped set, in place of [Hin21] Thm 3.9); commutator lemmas L2.1-2.5.
- Status (l.3-16): Proved (D326; D328 repair read D331).
- Uses: II.C (55), II.A1 (44), II.B (43), II.C1 (26), I.B (11). Lit: [Hin21] Thm 3.9 replaced; [Hin26c] §7.1 W.
- Amended: in place (D204, D326-D328; section 4 setting at T_flat, 550-579). Programs: none.

**II.D1 `PART-II-D2-BREGULARITY.md`** (682 l.; body 32-611; tail 612-682)
- Proves: Thm 1.1 = [Hin26c] P7.11 (estimates with b-regularity, tame); P3.2, P4.2 = P7.17, P5.2, P6.2 = P7.22.
- Status (l.3-16): Proved (D327). Uses: II.D (62), II.A (46). Lit: [Hin26c] §7.2 W.
- Amended: in place (D206, D326). Programs: none.

**II.E `PART-II-E-ENERGY.md`** (1,305 l.; body 37-1206; tail 1207-1305)
- Proves: energy estimates (P2.7 = [Hin26c] L8.1), localised radial estimates (P3.2), solvability on slabs (P3.4 =
  C8.2, P8.3), b-regularity on slabs and tame estimates (P4.3 = P8.6, P4.4 = P8.9), the black hole interior (P5.4 =
  P8.11, P5.6 = P8.12-8.13), Thm 6.1 = [Hin26c] Thm 8.14 (the global estimate).
- Status (l.3-17): Proved (D327). Uses: II.C (47), II.D (33), II.A (21), II.D1 (18). Lit: [Hin26c] §8 W.
- Amended: in place (D207, D212, D326). Programs: none.

**II.F `PART-II-F-IOTA.md`** (2,791 l.; body 39-2619; tail 2620-2791, incl. verifier sections 9.4-9.5)
- Proves: §1 setting incl. L1.3 (uniqueness of solutions supported to the future; [BGP]) and L1.4 (monotone functions
  along causal curves, giving the compact sets); §2 semiclassical calculus on iota+ and commutator scheme (P2.3-2.6);
  §§3-5 = [Hin26c] P10.6 (high frequencies without and with b-regularity: P3.1, P4.3; bounded frequencies: P5.1, L5.7 =
  Fourier bound in place of [Hin23d] L2.25, C5.9); §6 = P10.12 (forward solutions of the iota+-normal operator, P6.2); §7
  = P10.14 (modified operator P_+, P7.4); §8 Thm 8.1 = [Hin26c] Thm 10.1 (forward solutions of P_0 on e3b-spaces).
- Status (l.3-16): Proved (D216).
- Uses: II.C (67), II.A (45), I.B (43), I.C (40), II.E (23), II.B (22). Lit: [0C] BB (0-calculus with bounds: Def 1.2
  p.5, P2.7 p.9, C3.3 p.31, Thm 3.4, Rmk 3.5, C3.6 pp.33-34); [BGP] BB (pp. 18, 21-23, 68, 72, 174, 176: L1.3);
  [MM87] via [0C]; [Hin26c] §10 W.
- Amended: in place (D209, D212); L1.3's inner-boundary input named (D378, from R0P batch 4) and L1.4 (a) used at
  theta = 0 by VIII and III.K (D621). Programs: `n1/iplusnorm5.py` N1-N9 (21, 1380, 1702, 1716, 1792, 2505, 2625).

**II.F1 `PART-II-F2-TAME.md`** (851 l.; body 33-746; tail 747-851 incl. verifier §8.4)
- Proves: Thm 1.1 = [Hin26c] Thm 11.1 (forward solutions of wave-type operators, tame), C1.2 = (11.4); P3.1-3.2, P4.1-4.2
  (Steps 1-4); L2.1-2.9 preliminaries; R7.1-7.3 = Rmks 11.2-11.4.
- Status (l.3-12): Amended (D327: L2.1 (b) by enumeration), Proved (D216).
- Uses: II.E (64), II.C (47), II.A (34), II.F (17). Lit: [SBG] BB ((S3), (S5), (S8), (S10)); [Hin26c] §11 W.
- Amended: L2.1 (b), 174-179 (D327-D328): "Definition 3.3 (3) is not used" proved by enumerating 104 lines of II.C-II.E.
- Programs: `p5c/admiss5.py` (+ `admiss5.tsv`), l.177.

**II.G `PART-II-G-NASHMOSER.md`** (547 l.; body 28-453; tail 454-547 incl. verifier §6.3 at 529)
- Proves: Thm 2.1 = [Hin26c] Thm 12.4 (Nash-Moser with support classes; (iii) the support property at u in
  U cap B^infty_eta); R2.2; P3.1 = P12.6 (smoothing operators); L4.1 (tame bounds); §5 weights of §12.1 at n = 4.
- Status (l.3-12): Proved (D216); amended D304 (Thm 2.1 (iii), (H10)), amendment read (D621).
- Uses: II.F1 (22), II.C (12). Lit: [Hin26c] §12 W; [SR89], [Hin24a], [Hin23b] not used.
- Amended: Thm 2.1 (iii) at 78 and finding (H10) at 506 (D304); uses at III.K:330, 412 and III.J2:338.
- Programs: none.

**II.G1 `PART-II-G2-DECAY.md`** (1,330 l.; body 31-1198; tail 1199-1330 incl. verifier §7.3 at 1298)
- Proves: Fourier transform on the line and on resolved product spaces (§§2-3: Def 2.1, L2.2-2.6, P2.8 = [Hin26c] C13.7,
  P3.3 = P13.9, P3.5 = P13.11); resolvent bounds at n = 4 (§4: C4.2 = C13.14, P4.4 = P13.16, C4.5 = C13.17, P4.7 =
  P13.18); the radiation field (§5: P5.4 = P13.20).
- Status (l.3-13): Proved (D217). Uses: I.A (36), I.B (33), I.C (30), II.F1 (10). Lit: [Hin26c] §13 W; [Tay11a],
  [Li25], [Hin26b], [HV20], [LX24], [Tat13], [Hin22a] not used.
- Amended: in place (D216; 1302). Programs: none.

### 1.3 Part III, first half: the Einstein problem at n = 4 up to the low-energy resolvent ([Hin26] §§2-10)

Common to every Part III file: [Hin26] (Hintz, nonlinear stability of subextremal Kerr, arXiv:2606.28253v2) is W for
the sections named; each file closes with "Findings, labels and sources" (tail), which also names the N1STAR items the
part replaces ("the record's supplement 10.x") -- provenance only. Status lines all carry D-labels and verifier
numbers. Unless stated, amendments are in place and only the tags need stripping.

**III.A `PART-III-A-PREREQ.md`** (775 l.; body 23-723; tail 724-775)
- Proves: [Hin26] §§2.1-2.3 at n = 4: partial polyhomogeneity, integration along b-vector fields (L1.1-1.5, Defs
  2.1-2.3, L2.4, L3.1-3.3, L4.1); P4.2 = [Hin26] P2.25 with (L1) (pointwise bounds from partial polyhomogeneity).
- Status (l.3-11): Proved (D231). Uses: II.G1 (15: P3.3, P3.5, L3.1). Lit: [Mel93], [Mel96], [Hin25a], [Hin25c],
  [Hin23d], [HV20] replaced (proved here). Amended: III.J3 P4.1 makes P4.2 exact at K+ and zf (see III.J3).
- Programs: none.

**III.A1 `PART-III-A2-HARMONICS.md`** (553 l.; body 22-481; tail 482-553 incl. verifier §3.4 at 538)
- Proves: harmonics on S^3 (scalar, vector, tensor types; L1.1-1.6, Defs 1.3, 1.7); Minkowski operators in the null
  splittings; indicial roots by type (L2.1, Def 2.2, L2.3-2.4); general-N remark (316-318).
- Status (l.3-12): Proved (D324). Uses: none. Lit: [Hig87] (S^2 harmonics, comparison only); [Hin23b] §6.2 replaced.
- Programs: `n1/harm5.py` (18, 129, 388, 435, 478, 534, 545), `n1/lin5.py` (263, 487, 541).

**III.B `PART-III-B-FAMILY.md`** (560 l.; body 26-509; tail 510-560 incl. verifier §7.3 at 534)
- Proves: [Hin26] §§3-4 at n = 4: the compactified spacetime M (Def 2.1, L2.2); the Myers-Perry family in Kerr-Schild
  form (L3.1, Def 3.2, L3.3, P3.4 READ, L3.5, P3.6 = [Hin26] P3.10, L3.7); time functions and boosts (Def 3.8, L3.9,
  L4.1, L5.1-5.2); the gauge-fixed Einstein equation (Def 6.1, L6.2-6.3).
- Status (l.3-11): Proved (D221). Uses: II.A (3), II.C (2). Lit: [ER08] BB (formulas (14)-(16), (31)-(34), (42)-(44),
  pp. 10-19); [MP86] BB (the family); N1STAR 10.36 is Def 3.2's cited source.
- Amended: in place; R0P §3 (III.B at r_flat). Programs: MISSING `d215/chk3b.py` (107, 134, 187, 558),
  `d215/chkric.py` (154, 558), `d215/chkboost.py` (397, 558) -- sympy checks of L3.1, L3.3, P3.4 and the boosts.

**III.D `PART-III-D-GAUGEPOT.md`** (517 l.; body 26-466; tail 467-517)
- Proves: [Hin26] §6 to P6.9: the gauge potential operator (Box on 1-forms with modifications): structure (L2.1),
  Minkowski model (L3.1), indicial roots (L4.1), horizon threshold (L5.1-5.2), trapping, high energies (P6.1 = P6.5),
  P6.2 mode stability of Box on Tangherlini away from zero (replaces [AHW24] Thm 5.1), P6.3 = P6.9,
  tf-admissibility (L7.1). The hypotheses (Dyn) are named here and discharged in VI.
- Status (l.3-12): Proved (D229). Uses: III.B (20), III.A1 (19), I.B (17), I.A (13), I.C (9).
- Lit: [AHW24] Thm 5.1 replaced; [Hin17] P4.1 computed directly; N1STAR 10.15-10.20 (computed statements, 514).
- Programs: `n1/harm5.py`, `n1/trap5.py`, `n1/modes5.py`, `n1/lin5.py`, `n1/hienergy5.py`, `n1/thresh5.py`
  (43-337, 506).

**III.D1 `PART-III-D2-ZEROENERGY.md`** (389 l.; body 22-339; tail 340-389)
- Proves: [Hin26] §6.4 and L6.13: zero-energy kernel and cokernel of the gauge potential operator (L2.1), pairings
  (L3.1), mode stability at every frequency, the zero energy inverse via the augmented operator (P4.1), L5.1.
- Status (l.3-12): Proved (D231). Uses: I.C (26), III.D (24). Lit: [AHW24] Thm 5.1, [Hin24b] P3.7, P3.12, L3.8
  replaced; N1STAR 10.15 (386). Programs: `n1/modes5.py` (118, 379), `n1/gaugepot5.py` (79, 103, 193, 379).

**III.D2 `PART-III-D3-SYMSTATES.md`** (330 l.; body 20-287; tail 288-330)
- Proves: [Hin26] §6.5.1: zero energy states from the Minkowski symmetries (L2.1-2.2), Lemma 6.14's comparisons (P3.1).
- Status (l.3-11): Proved (D231). Uses: III.D1 (11), III.D (8), III.B (8). N1STAR 10.28 (329).
- Programs: `n1/zstates5.py` (44, 264, 280, 299, 320), `n1/genstates5.py` (44, 321).

**III.D3 `PART-III-D4-GENSTATES.md`** (309 l.; body 18-265; tail 266-309)
- Proves: [Hin26] §6.5.2: generalised zero energy states of the gauge potential operator (L2.1 solving; P3.1).
- Status (l.3-9): Proved (D235). Uses: III.D2 (14), III.D (5). N1STAR 10.29-10.30 (307).
- Programs: `n1/genstates5.py` (62-64, 179, 301), `n1/lin5.py` (259), `n1/puregauge5.py` (70, 72, 181, 301).

**III.E `PART-III-E-CONSTRAINT.md`** (243 l.; body 18-211; tail 212-243)
- Proves: Thm 1.1 = [Hin26] Thm 7.1 at n = 4 for the constraint propagation operator Box^C_b: (1) mode stability at
  sigma != 0, (2) invertible zero energy operator on the stated weights, (3) indicial roots with counts by type, (4)
  tf-admissibility for weights in [-C_0, 2). STATED here, PROVED in IV(4) [(1)-(3)] and IV(6) [(4)]. L2.1; P3.1 =
  P7.3 (the large dual states; invertibility of the adjoint).
- Status (l.3-10): Proved (D235). Uses: III.D2 (10), I.C (7), IV (5: forward). Lit: [Hin26a] W in IV(4)-IV(6).
  N1STAR 10.21, 10.31 (242).
- Amended: Thm 1.1 (3) widened D231 at 54 (count by type and last three clauses; used by III.F1 as (C1)-(C4), see
  III.F1:53, 506); 116, 123 (D231).
- Programs: `n1/cpmodes5.py` (63, 234), `n1/damping5.py` (56), `n1/dual5.py` (103, 169, 234).

**III.E1 `PART-III-E2-V1STATES.md`** (262 l.; body 18-216; tail 217-262)
- Proves: [Hin26] §7.2.1: the vector type 1 dual states; the deformation tensor of a rotation exact by equivariance
  (L2.1-2.3); the states' dependence on the bracket with the spin (P3.1).
- Status (l.3-7): Proved (D231). Uses: III.E (14), III.B (12). Programs: `n1/mp5.py` (81, 249), `n1/dualv1_5.py` (96,
  154, 248).

**III.F `PART-III-F-LINEARISED.md`** (258 l.; body 17-215; tail 216-258)
- Proves: [Hin26] §8 to end of 8.1: structure of the linearised gauge-fixed Einstein operator L_b (L2.1), the spectrum
  of the model's endomorphism (L3.1), the bound at the trapped set (P4.1).
- Status (l.3-8): Proved (D235). Uses: III.D (20), I.B (12), III.B (10), III.E (6). Lit: [Hin17] P4.1 (every dim.)
  as an identity. Programs: `n1/lgrade5.py`, `n1/cpmodes5.py`, `n1/sbar5.py`, `n1/lin5.py`, `n1/strap5.py`,
  `n1/thresh5.py` (124-245).

**III.F1 `PART-III-F2-INDICIAL.md`** (526 l.; body 14-492; tail 493-526)
- Proves: [Hin26] §§8.2-8.3: indicial roots of L_b (L2.1-2.2, P2.3 = L8.4, L2.4-2.5; the gap (2.2) giving eps_ind),
  indicial solutions at 0 (L3.1-3.2), tf-admissibility (P3.3 = P8.6), the inverse of the tf-normal operator on
  b-spaces (C3.4 = C8.7).
- Status (l.3-12): Proved (D238). Uses: I.C (36), III.D (11), III.F (10), III.E (9: Thm 1.1 (3) as (C1)-(C4)).
- N1STAR: 10.34 (iv), the numeral 1 + 2.93e-6 at 135 (eps_ind < 3e-6) -- a computed input from the main argument.
- Amended: none here; VI.C row w1 replaces the eps_ind bound it states (D390, D621: delta_50 = 1.94137e-8).
- Programs: `n1/damping5.py` (56), `n1/lin5.py` (11-75), `n1/linroots5.py` (12, 101, 261), `n1/eind5.py` (57).

**III.F2 `PART-III-F3-MODES.md`** (290 l.; body 17-270; tail 271-290)
- Proves: [Hin26] P8.8: horizon threshold (L1.1, C1.2, L1.3); mode stability of L at b_0 away from zero (T2.2, in place
  of [AHW24] Thm 6.1 (1), via Kodama-Ishibashi master equations; L2.1, L2.3; P3.1), P4.1 for |sigma| >= c_0 near b_0.
- Status (l.3-15): Proved (D238). Uses: I.A (13), III.D (11), III.F (8). Lit: [KI03] BB (formulas (5.3), (5.10),
  (5.15): master equations and potentials); [AHW24] Thm 6.1 (1) replaced. Low energy near b_0 closed by III.H C4.3-4.4.
- Programs: `n1/gmodes5.py` (15, 127), `n1/lhor5.py` (15, 37).

**III.F3 `PART-III-F4-ZERO.md`** (489 l.; body 17-457; tail 458-489)
- Proves: [Hin26] §8.4 P8.9-C8.13: zero energy kernel and cokernel of L (P2.2 = P8.9; L2.1, R2.3), stationary
  solutions on Tangherlini (T3.1 in place of [AHW24] Thm 6.1 (2); C3.2 stationary gauge invariants), P4.1 = P8.11,
  C4.2 = C8.13.
- Status (l.3-15): Proved (D238). Uses: III.D2 (17), III.F2 (13), I.C (12). Lit: [KI03] BB; [AHW24] replaced.
- Programs: `n1/zstates5.py`, `n1/gmodes5.py`, `n1/pairing5.py`, `n1/static5.py`, `n1/mp5.py` (15-478).

**III.F4 `PART-III-F5-PAIRINGS.md`** (366 l.; body 16-330; tail 331-366)
- Proves: [Hin26] L8.12, L8.15, P8.14: zero energy pairings reduced to infinity (L2.1-2.2, L3.1, L4.1); the physical
  states at -2 (P5.1 = P8.14 (1)).
- Status (l.3-14): Proved (D238). Uses: III.F3 (16), III.E, III.E1, III.D3 (6 each). Lit: [Hin24b] L3.17 replaced.
- Programs: `n1/pairing5.py` (8-187), `n1/physical5.py` (353), `n1/window5.py` (351).

**III.G `PART-III-G-SPECTRAL.md`** (970 l.; body 42-931; tail 932-970)
- Proves: [Hin26] P9.2: the spectral family at future timelike infinity (Mellin in the scaling): Fredholm across the
  light cone (P2.4), commuted equations (P2.6), b-regularity at the light cone (P2.7, in place of [HV15] Thm 6.3),
  injectivity (P3.2), invertibility for Re lambda < 2 and finite meromorphy (P4.6, T5.1 = P9.2).
- Status (l.3-13): Proved (D240). Uses: II.F (55), I.A (38), I.C (30), I.B (19), III.F1 (18).
- Lit: [Vas13], [Hin25a], [HV15] replaced by I.A-I.C. Programs: `n1/sf5.py` (13-662), `n1/iotasol5.py` (271, 938).

**III.G1 `PART-III-G2-IOTA.md`** (512 l.; body 15-472; tail 473-512)
- Proves: [Hin26] P9.4, Defs 9.3, 9.6, R9.7: the iota+-normal operator, its inverse (T3.1), asymptotics at scri+ and
  K+, finite regularity, the boundary spectrum (L1.1, Def 1.2, L1.3, L2.1 in place of [Hin26c] L13.4, L2.2, Def 4.1,
  L4.2-4.3).
- Status (l.3-13): Proved (D241). Uses: III.G (24), III.A (10), III.F1 (7).
- Programs: `n1/sbar5.py` (12, 66, 475), `n1/sf5.py` (12, 30, 464).

**III.G2 `PART-III-G3-GRAFT.md`** (447 l.; body 27-387; tail 388-447 incl. verifier §5.1 at 425)
- Proves: [Hin26] Defs 9.8, 9.10, P9.9, P9.11, C9.12: formal solutions at K+ from the zero energy states (T3.1; C3.2
  the index set at K+ precisely), the expansion at K+, grafting into spacetime (T4.2 = P9.11, C4.3 = C9.12); the
  window l_K < 3 (Table 1.1).
- Status (l.3-10): Proved (D244). Uses: III.D3 (20), III.G1 (18), III.F1 (9). N1STAR 10.35 (c) (23).
- Amended: III.J3 C3.2 restates C4.3 at the exact K+ weight. Programs: none.

**III.C `PART-III-C-EXTERIOR.md`** (578 l.; body 28-495; tail 496-578 incl. verifier §§6.4-6.5 at 558, 572)
- Proves: [Hin26] Defs 5.1-5.4, 5.13, R5.5, P5.11, P5.14, C5.15 at n = 4: metric perturbations near infinity (L1.1,
  Def 1.2, L1.3, L2.1, Defs 3.1-3.4, L3.2, L3.5); the linearised operator at null infinity: constant lower-triangular
  matrix A-bar (L4.2), perturbation half an order lower (L4.1, L4.3, P4.4 = P5.11 with (5.41a), R4.5); forward mapping
  (Def 5.1, P5.2 = P5.14, C5.3 = C5.15).
- Status (l.3-8): Proved (D245). Uses: III.B (24), III.F (13), III.C1 (8: forward), III.A (5). [Hin23a]: W in IV.
- N1STAR 10.38 (a), (c), 10.64 (314, 402, 505, 521, 556, 570: values; the scaling deduction now proved).
- Programs: `n1/ext5.py` (70-577), `n1/sbar5.py` (307, 556), `n1/exterior5.py` (401, 565, 576), `n1/scri5.py`
  (87-564).

**III.G3 `PART-III-G4-RESONANT.md`** (478 l.; body 22-407; tail 408-478 incl. verifier §4.4 at 464)
- Proves: [Hin26] §9.1.3 (L9.13-9.14, P9.15, C9.18, L9.21, P9.22): the iota+-normal operator on partially
  polyhomogeneous inputs; one exceptional exponent; least incoming pole 3/2 + (1 - e_Ups) gam_Ups (P2.4 = P9.15, C2.6
  = (9.49)); quasi-homogeneous solutions (C3.1 = C9.18); resonant states (P3.7 = P9.22); Defs 1.1, 2.5, 3.2, 3.6.
- Status (l.3-8): Proved (D247). Uses: III.G1 (41), III.C (22), III.G2 (11). N1STAR 10.35, 10.38 (d).
- Programs: `n1/ext5.py` (74-477), `n1/scri5.py` (75, 76, 451, 452).

**III.G4 `PART-III-G5-TF.md`** (805 l.; body 24-726; tail 727-805)
- Proves: [Hin26] §9.2: the tf-normal operator: formal solutions at ztf (L1.1-1.2, Defs 2.1, 2.3, L2.2, L2.4), the
  expansion of its inverse at r-hat = 0 over (-3, 0] (T3.1 = L9.26), grafting into the low-energy space (P4.4 = P9.30),
  conormal sources (P5.1 = P9.35, its first step repaired).
- Status (l.3-10): Proved (D249). Uses: III.G2 (21), III.F1 (15), III.A (8). Programs: `n1/tfgraft5.py` (79-805).
- Note: VI.C row w1 cites T3.1's (3.1) at 190 and P5.1 at 624-631 for eps_ind.

**III.H `PART-III-H-AUGMENT.md`** (608 l.; body 25-554; tail 555-608)
- Proves: [Hin26] §10.1: cut-off states (Def 2.1, L2.2-2.5, R2.6), the augmented zero energy operator (Def 3.1, P3.2
  = P10.6), uniform low-energy estimates with sigma-dependent columns (T4.1 = I.C Thm 6.4 with such columns), C4.2 =
  P10.7, C4.3-4.4 (mode stability near b_0 at low frequency; closes III.F2's P8.8 there), Def 5.1, L5.2, R5.3.
- Status (l.3-11): Proved (D252). Uses: I.C (35), III.F3 (18), II.G1 (14), III.F4 (8). Programs: none.

**III.H1 `PART-III-H2-ADMISS.md`** (534 l.; body 26-463; tail 464-534)
- Proves: T1.3 = [Hin26] Thm 10.1 at n = 4: 2-admissibility of L_b (contour representation; high and low frequencies;
  zero-energy contributions integrated twice in t_*; sf-loss 0); Def 1.1, L1.2, L2.1-L6.2.
- Status (l.3-12): Proved (D256). Uses: III.H (34), II.A (21), II.C (20), I.A (19), I.B (15). Lit: [Hin26c] L14.6
  and the proofs of Thms 12.2 W; [SBG] (3.26) BB.
- Amended: its restriction k <= K is superseded by III.H2 at PART-III-H3-UNIFORM.md:222 (every k).
- Programs: none.

### 1.4 Part III, second half: forward solutions, parameters, base points, the nonlinear theorem ([Hin26] §§11-13)

III.I to III.I(14) and III.J to III.J3 are written at b_0 = (mu_0, 0) (Tangherlini); III.I(15) carries all of them to
base points b near b_0. Every [Hin26] section named is W. None of these files cites a program except III.H2 and III.K.

**III.I `PART-III-I-CONE.md`** (497 l.; body 22-445; tail 446-497)
- Proves: [Hin26] §11 opening and §11.1: perturbation classes and the e3b class (Def 1.1, L2.1-2.2), structure in the
  forward cone (L3.1-3.2, P3.3-3.4 = P11.6, R3.5, L3.6), forward mapping (P4.1 = P11.8, C4.2 = C11.9, L4.3),
  admissibility with p_0 = p~_1 = 0 (L5.1, C5.2 = C11.10), T5.3 = [Hin26] Thm 11.12 at b_0 (forward solutions, sf-loss
  0); the orders of II.F1 in O_c (R5.4-5.5).
- Status (l.3-11): Proved (D258). Uses: III.C (42), II.C (21), II.F1 (18), III.H1 (16), III.B (16).
- N1STAR 10.39, 10.42, 10.44 (e) (63, 315, 495). Amended: T5.3 near b_0 with continuity in b = III.H2 C5.1.

**III.I(1) `PART-III-I2-SCRI.md`** (277 l.; body 20-239; tail 240-277)
- Proves: [Hin26] §11.2: partial polyhomogeneity at null infinity without loss at iota+ (L1.1, P2.1 = P11.14, L2.2);
  formal solutions at null infinity with one exceptional term (P3.1 = P11.16).
- Status (l.3-7): Proved (D258). Uses: III.C (20), III.A (20), III.I (13). N1STAR 10.44.

**III.I(2) `PART-III-I3-ALMOST.md`** (485 l.; body 22-441; tail 442-485)
- Proves: [Hin26] §11.3: almost linear bounds: integration of d_{t*} with a moment condition (L2.1, L3.1), the three
  frequency ranges (L4.1-4.3), forward solutions improved at K+ with the iota+-weight min(alpha_+, 3/2, min Re E_+)
  (P5.1 = P11.17).
- Status (l.3-7): Proved (D259). Uses: II.G1 (29), III.H (23), III.I (18), III.A (12), III.H1 (11). N1STAR 10.45.

**III.I(3) `PART-III-I4-BOOST.md`** (316 l.; body 24-276; tail 277-316)
- Proves: [Hin26] §11.4.1: the boost parameter (L1.1-1.3; P2.1 = P11.20: the forward solution is a cut-off generalised
  boost state plus a remainder of K+-weight alpha_K - 2; zero energy inverted by the augmented operator).
- Status (l.3-8): Proved (D261). Uses: III.H (20), III.I(2) (19), II.G1 (10). N1STAR 10.45 (b), 10.61 (b).

**III.I(4) `PART-III-I5-UNBOOST.md`** (457 l.; body 23-407; tail 408-457)
- Proves: [Hin26] §11.4.2: correction terms (Defs 1.1, 2.1, 2.3), the boost identity (11.78b) (L2.4), the augmented
  operator and its parameter derivative (L1.2, L2.2, L2.5, L3.1-3.2), the boost parameter map invertible (P4.1 =
  P11.30, L4.2), C4.3 = (11.95).
- Status (l.3-10): Proved (D263). Uses: III.I (28), III.B (24), III.I(3) (14), III.D2 (11).
- AMENDED at b != b_0: L2.4 exact only at b_0; P4.1 (2), C4.3 replaced at b by III.I(15) §2.6 (L2.7, P2.8;
  PART-III-I16-BASEPOINTS.md:375-455), Thm 3.1 item (ix) at 781.

**III.I(5) `PART-III-I6-ALMOSTBDD.md`** (271 l.; body 20-234; tail 235-271)
- Proves: [Hin26] §11.5: P2.1 = P11.32 (almost boundedness: K+-weight alpha_K - 2 for every alpha_K < 2, with a step at
  iota+ from 3/2 + (1 - e_Ups) gam_Ups); C2.2 (the remark after P11.32).
- Status (l.3-7): Proved (D266). Uses: III.I(4) (16), III.I(3) (15), III.I(1) (11), III.G2 (11), III.G1 (10).
- AMENDED at b: C2.2 by III.I(15) P2.8 (I16:415). VI.C row w1 cites 118-119 (the other eps_ind; see VI.C).

**III.I(6) `PART-III-I7-PARAMS.md`** (379 l.; body 21-333; tail 334-379)
- Proves: [Hin26] §11.6.1: P2.1 = P11.34 (extraction of the parameters: for sources of K+-weight alpha_K in (2, 5/2),
  u = chi_K g-dot(b-dot) + chi_K h(S^(0)_1) + remainder; no logarithmic centre-of-mass term at n = 4); L1.1-1.4.
- Status (l.3-7): Proved (D268). Uses: III.H (25), III.G4 (16: P5.1), III.I(2) (14), III.I(1) (13), III.I(5) (12).

**III.I(7) `PART-III-I8-UNPARAM.md`** (502 l.; body 23-455; tail 456-502)
- Proves: [Hin26] §11.6.2: undoing the parameter changes: corrections (L1.1, Defs 1.2, 2.1, 2.3, L1.3), the operator
  P_2 with parameters (S, b - b_0, S^(0)_1) (L2.2, L2.4 parameter identities, L2.5, L3.1), their elimination (L4.1,
  Def 4.2, L4.3, Def 4.4, L4.5, C4.6 = C11.46); the translated exterior background at n = 4.
- Status (l.3-10): Proved (D269). Uses: III.I(3) (48), III.I (27), III.I(6) (22), III.B (15).
- AMENDED at b: L2.4 exact only at (0, 0); L4.3, L4.5, C4.6 replaced at b by III.I(15) §2.8 (L2.11, P2.12;
  I16:532-642), item (x) at 784.

**III.I(8) `PART-III-I9-COMMOTION.md`** (470 l.; body 28-418; tail 419-470)
- Proves: [Hin26] §11.7: decaying centre-of-mass motions: the motion index set E_{++}, corrections #3 with generalised
  gauge 1-forms to order 4 (Defs 2.1, 2.3, L2.2, L2.4-2.6, L3.1-3.3), P4.1 = P11.51 (K+-weight alpha - 2 for alpha <
  min(a_K, 3)).
- Status (l.3-9): Proved (D271). Uses: III.I(7) (25), III.I(6) (18), III.G2 (11), III.I(3) (10).
- AMENDED at b: P4.1's base step by III.I(15) P2.12 (I16:580), Thm 3.1 list at 660-668.

**III.I(9) `PART-III-I10-CORR4.md`** (465 l.; body 31-408; tail 409-465)
- Proves: [Hin26] §11.8 to L11.57: hypotheses (H1)-(H3), corrections #4 for six row types (s1, v1, s0, s2, c0, c1;
  gauge towers of length 4, 3, 4, 3, 2, 2) (Defs 2.1, 2.3, L2.2, L2.4-2.6), the operator P_4 and its exact
  linearisation f^nu = L m_nu + r^nu (2.4).
- Status (l.3-9): Proved (D274). Uses: III.I(8) (27), III.I(7) (27), III.D3 (19), III.D2 (12).
- Note: (1.1) at 32-48 defines eps_ind (VI.C row w1); the paper cites 72-74 (the gap (G)).

**III.I(10) `PART-III-I11-SPACETIME.md`** (453 l.; body 28-408; tail 409-453)
- Proves: [Hin26] Thm 11.59 Parts 1-3, first half: (C5) and (H4) (Defs 1.1, 1.3 = the exponent set Lambda and the gap
  (G), L1.2), towers as delta*-images, uniqueness of row expansions (L2.1-2.2, C2.3, L2.4), forward Fourier tails, the
  spacetime phase (P3.1).
- Status (l.3-13): Proved (D275). Uses: III.I(9) (26), III.G2 (21), III.I(11) (13: forward; same theorem), III.I(8) (13).
- Interface: Def 1.3 is cited by the paper's Theorem 4.

**III.I(11) `PART-III-I12-SPECTRAL.md`** (572 l.; body 29-525; tail 526-572)
- Proves: Thm 11.59 Parts 1-3, second half, and (11.222): four zero-energy solves (L1.1, L2.1-2.5), III.G4 P4.4 at
  levels 1-2 and P5.1 at level 3, a physical decomposition, the spectral phase (P3.1), the expansion lemma and the
  elimination (L3.2-3.3); T4.1 = Thm 11.59 Parts 1-3 at n = 4.
- Status (l.3-12): Proved (D277; amended before verification D274: L1.1, eta_1, eta_2 < eps_+, L2.1-2.2).
- Uses: III.I(10) (30), III.I(8) (26), III.G4 (23), III.H (22), III.I(9) (17), III.I(6) (16).

**III.I(12) `PART-III-I13-EXPANSION.md`** (479 l.; body 28-445; tail 446-479)
- Proves: Thm 11.59 Part 4 ((11.196)) and the iota+ part of (11.222): T3.1 (the forward solution as towers of the
  zero-energy states with partially polyhomogeneous coefficients, modulo K+-order alpha); Def 1.1, L2.1-2.4.
- Status (l.3-11): Proved (D280). Uses: III.G2 (23), III.I(11) (20), III.I(10) (15), III.H (14).
- AMENDED at b: L2.3-2.4 use h_{b0,v1} = 0; replaced at a rotating b by III.I(15) §2.7 (L2.9, C2.10; I16:456-531),
  item (xi) at 787.

**III.I(13) `PART-III-I14-LEVELS.md`** (214 l.; body 26-187; tail 188-214)
- Proves: Thm 11.59 Parts 2-3 at every level: P2.1 (III.I(11) P3.1 at every level beta in (3, 4 + eps_K]), P2.4 (the
  enlarged sources Y^natural at the top level); Defs 1.1-1.2, L1.3, L2.2-2.3.
- Status (l.3-14): Proved (D324). Uses: III.I(11) (27), III.I(10) (20).

**III.I(14) `PART-III-I15-AUGMENT5.md`** (507 l.; body 34-458; tail 459-507)
- Proves: [Hin26] §11.8.3: augmentation #5 (Defs 1.1-1.3: the coefficients q, the rotation rows of Def 1.3 with
  coefficient space V_1), L2.1-2.5 (the b-derivative has K+-order alpha-), T3.1 = [Hin26] C11.66 (unique p' with the
  forward solution at h + h_rem(q) equal to h_rem(q') + h'), R3.2. Corollary 11.67 deferred (30-31, 489-491).
- Status (l.3-10): Proved (D287). Uses: III.I(9) (34), III.I(11) (27), III.I(10) (22), III.I(12) (16), III.I(8) (16).
- AMENDED: T3.1 at b is III.I(15) P2.5 (I16:276) and at exact weights III.J3 T5.3 (I16 item (viii)).

**III.J `PART-III-J-PARAM.md`** (422 l.; body 31-376; tail 377-422)
- Proves: [Hin26] §12 to R12.6: the data space (Def 1.1, L1.2: black hole parameters, boost, translation, iota+ data
  at the resonances in E_sharp, conormal remainders, a remainder tensor), L2.1-2.3, T2.4 = [Hin26] Thm 12.3 (data
  determine (h, p, q) with P_5 vanishing at iota+ to order 5 + eps_+ and of K+-order alpha), R2.5-2.6; (G+).
- Status (l.3-10): Proved (D287). Uses: III.I(13) (32), III.G3 (26), III.G2 (22), III.I(8) (14), III.I(9) (11).
- Interface: (G+) and 34, 48-51, 56 cited by VI.C row w1 and the paper's Theorem 4.

**III.J1 `PART-III-J2-LINEAR.md`** (194 l.; body 20-163; tail 164-194)
- Proves: [Hin26] Thm 12.8 at b_0: L1.1 (under (G+) the linear solutions have iota+-order (3 + eps_+)-), T2.1 (every
  linear forward solution of III.I(14) T3.1 for a source of class F is D_U Phi(U')), R2.2.
- Status (l.3-9): Proved (D287). Uses: III.I(13) (22), III.J (22), III.I(11) (10). Open items (J'3)-(J'4) closed by
  III.I(15) C3.2 and III.K.

**III.J2 `PART-III-J3-TAME.md`** (396 l.; body 27-344; tail 345-396)
- Proves: [Hin26] R11.13 and the tame estimates of C11.66 and Thm 12.8: a calculus of tame families (Def 1.1, L1.2,
  L2.1, R2.2, L2.3-2.4), the inventory of III.I-III.I(14) and III.J1 (table, incl. III.I(15) P2.5 at 271), T4.1-4.2
  (tame forms), P4.3 (the tame forward map), R4.4.
- Status (l.3-13): Proved (D295; (J''4) discharged by III.J3).
- AMENDED: (J''2) (neighbourhood shrinking with k) superseded at I16:759 by III.H2 P1.1 (H3:158-170, 222); noted at
  J3:355. Uses II.G Thm 2.1 (ii)-(iii) as amended D304 (338).

**III.J3 `PART-III-J4-EXACT.md`** (726 l.; body 40-672; tail 673-726)
- Proves: exact weights: the exact classes (Def 1.1, R1.2, Def 1.3, L1.4) and conditions (E1)-(E5); L2.1-2.2; the graft
  at the exact K+ weight (C3.2 = III.G2 C4.3 exact; L3.3, P3.4); III.A P4.2 exact at K+ and zf (P4.1); the pointwise
  bounds at the final weight re-proved in L^2 (L4.2, P4.3, L4.4-4.5, P4.6, L4.7); P5.2, T5.3 (III.I(14) T3.1 at exact
  weights), P5.4, T5.5 (III.J1 T2.1 at exact weights); C6.6 (III.J2 T4.1-4.2, P4.3 without loss).
- Status (l.3-12): Proved (D296). Uses: III.I(11) (24), III.J2 (20), III.J (20), III.I(13) (19), III.A (17).
- AMENDED at b: T5.3 stated at b by III.I(15) Thm 3.1 (ledger batch 5).

**III.H2 `PART-III-H3-UNIFORM.md`** (384 l.; body 27-339; tail 340-384)
- Proves: uniformity near b_0: P1.1 = [Hin26] P8.3 (strong trapping admissibility at every b on B_1, a frame from the
  null geometry), C1.2 (delta_Gamma uniformly small), T2.1 (2-admissibility on B_1 for every k; supersedes III.H1's
  k <= K at 222), T3.1 (II.F Thm 8.1 uniformly over 2L_b), T4.1 (II.F1 Thm 1.1 uniformly), C5.1 = [Hin26] Thm 11.12 near
  b_0 (III.I T5.3 with continuity in b).
- Status (l.4-12): Proved (D299). Uses: II.F (29), III.F (20), II.F1 (19), III.H (19), III.I (17), I.B (14).
- Programs: `n1/lgrade5.py` (127). Body carries 16 D-tagged lines.

**III.I(15) `PART-III-I16-BASEPOINTS.md`** (874 l.; body 35-805; tail 806-874)
- Proves: the linear theory at base points b near b_0: the model at b ((P1)-(P6) of L1.1 at 37; L1.2 joint
  injectivity by perturbation at 143); the rotation rows at b (§2, 169-374: L2.1, P2.2 v1 terms of exponent <= 2 as
  rotation rows with assigned coefficients, Def 2.3, L2.4, P2.5 = III.I(14) T3.1 at b, R2.6); §2.6 boost parameter at b
  (L2.7, P2.8 = III.I(4) P4.1 (2) at b; 375-455); §2.7 expansion at b (L2.9, C2.10 = III.I(12) T3.1 at b; 456-531);
  §2.8 parameter columns at b (L2.11, P2.12 = III.I(7) L4.3, 4.5, C4.6 at b; 532-642); §3 T3.1 (the parts at b, with a
  list of the forms in which each statement holds, 645-690) and its proof by items (i)-(xi) (692-799); C3.2 = (J'3).
- Status (l.4-21): Proved (D333); repairs from the ledger (D329-D332). Uses: nearly every III.I/III.J part.
- Note: the proof of T3.1 rests on BASEPOINT-LEDGER.md for completeness (692: "every use ... is a row of the ledger").
- Programs: none.

**III.C1 `PART-III-C2-POLYHOM.md`** (305 l.; body 28-275; tail 276-305)
- Proves: [Hin26] §§5.4-5.5: L1.1 the exterior domain (weights shifted; Omega_ext,r0; past slab); T2.1 = Thm 5.17 (the
  exterior solution and its linear estimate (5.52)-(5.53): DELIVERED by IV(2) T2.4, T3.1, L2.2), R2.2; T3.1 = Thm 5.21
  (partial polyhomogeneity at I_0 and null infinity without subtracting radiation fields; settles (C7)), R3.2.
- Status (l.3-8): Proved (D292). Uses: III.C (51), III.A (10), IV (9). Lit: [Hin23a] W in IV; [SR89] not used.
- N1STAR 10.57, 10.64 (117, 304). Programs: none.

**III.C2 `PART-III-C3-BOOSTDATA.md`** (270 l.; body 27-230; tail 231-270)
- Proves: [Hin26] §§5.6-5.7: L1.1 (the boosted metric in the class), L2.1, T3.1 = Thm 5.23 (pullback by boosts in the
  cut-off gauge; settles (C4)), R3.2, P4.1 = P5.25 (gauged Cauchy data), P4.2 (Boyer-Lindquist data carry no
  logarithm at n = 4), R4.3.
- Status (l.3-7): Proved (D292). Uses: III.C1 (24), III.C (22), III.B (16), IV (3). Lit: [COM81] (boost theorem)
  proved via III.C1 T2.1; [CD03] mentioned. Programs: none.

**III.K `PART-III-K-NONLINEAR.md`** (775 l.; body 21-504 and 620-763; tail 505-583, the amendment preambles 584-619
and the program remark and sources 764-774)
- Proves: [Hin26] §13.1 at n = 4 near b_0: §0 setting (constants, weights, (K1)-(K2)); §1 the initial family in a
  cut-off gauge equal to the cone's on Omega_* (L1.1, P1.2 = (13.5)); §2 the map Psi and its right inverses, support
  classes and smoothing on D_ex (Def 2.1, L2.2-2.3); §3 the Nash-Moser iteration by II.G (L3.1, T3.2); §4 constraint
  propagation and the theorem (L4.1, P4.2, T4.3 = [Hin26] Thm 13.1 at n = 4, R4.4); §6 L6.1 (the radius near scri+
  along past causal curves of every metric of the class; 620-692) and L6.2 (P1.2's uniqueness near infinity; 693-768).
- Status (l.3-12): Proved (D312), conditional on Part IV (closed by IV(2), IV(3)). README adds: amended D378 (P4.2),
  D611 (P1.2 (1) and its proof), D621 (L6.1), D626 (L6.2; L2.3's level), D628 (L6.2's compact-set clause narrowed),
  D629 (nits); all read.
- Amendments to fold in: inline brackets at 34, 57, 124, 151, 189, 194, 201, 327, 330, 412, 464, 466 (D304-D626);
  §6 L6.1-6.2 with their inline brackets at 646, 679, 696, 698, 708, 720, 726, 754, 761 (D626-D629). The text amended
  (P1.2 at 96-212, P4.2 at 437-470, L2.3 at 277-331) cites them.
- Uses: III.C2 (29), II.C (29), II.F (29), III.B (24), II.G (23), III.C (20), III.I(13) (12), III.J (12), IV(2)-(3).
- Programs: `n1c/scrirad5.py` R1-R5 (595, 609, 616, 658, 710, 747, 766, 770, 772: L6.1-6.2 checks);
  `n1c/vii5census.py` (589, 610, 617) and `n1c/r0census5.py` (590): census programs, provenance only.

### 1.5 Part IV: exterior estimates ([Hin23a] §3) and constraint damping ([Hin26a]) at n = 4

**IV `PART-IV-EB.md`** (353 l.; body 13-328; tail 329-353)
- Proves: [Hin23a] §§3.1-3.2 for [Hin26]'s gauge-fixed operator on III.C's exterior region: the edge-b calculus (§0);
  the frame as edge-b covectors (L1.1 = [Hin23a] L3.13, C1.2 = L3.12 + C3.14, R1.3); the scalar operator
  rho_I rho^(-7/2) Box rho^(3/2) with Delta + 3/4 (L2.1-2.2 = L3.16); the basic energy estimate near scri+ (P3.1 =
  P3.17, R3.2); the b-energy estimate near I_0 (P4.1, R4.2: new at n = 4, in place of [HV20] P4.3).
- Status (l.3-11): Proved (D309). Uses: III.C (16), III.C1 L1.1 (191-193, 320-325), III.B (6), II.F L1.3.
- N1STAR 10.64 X6 (l.39: "s = 3 serves at n = 4") is a cited input; 10.64 X1-X3, X8 via `n1/exterior5.py` (352).
- Amended: in place (D304-D309). Programs: `n1/exterior5.py` (352).

**IV(1) `PART-IV2-TAME.md`** (231 l.; body 13-210; tail 211-231)
- Proves: [Hin23a] §§3.3-3.5 at n = 4: L1.1 (Cartesian derivatives in rho_0 V_eb), P1.2 = P3.29 (edge-b form
  -2(X_I - Abar)(X_0 - X_I) + ..., the constant first-order matrix Abar of III.C L4.2); L2.1, P2.2 = P3.32 (energy
  estimate for the system at alpha_I < min(alpha_0, 0), and its tame form), L2.3 (Moser products), L2.4 = L3.34.
- Status (l.4-11): Proved (D311). Uses: III.C (33), IV (17), III.C1 T3.1 (l.26: l_I > 3/2; see risks).
- Lit: [Tay11] ch. 13 Props 3.6-3.7 BB (Moser estimates). N1STAR 10.64 (e), (X6), (X7), (g) (230).
- Amended: 23 (D309). Programs: none.

**IV(2) `PART-IV3-NM.md`** (441 l.; body 17-400; tail 401-441)
- Proves: [Hin23a] §3.6 at n = 4 on III.C1's Omega_ext,r0: integration along the two families of curves (L1.1-1.2),
  the Cauchy problem near I_0 in both directions (L2.1-2.3; L2.2 the backward solution on the past slab), T2.4 =
  [Hin23a] Thm 3.35 (the linear exterior estimate and its tame form), T3.1 = III.C1 T2.1's nonlinear part (by II.G),
  C4.1 (the cut-off gauge and the backgrounds; III.C2 (C''2)). DELIVERS III.C1 T2.1.
- Status (l.4-15): Proved (D311). Uses: III.C1 (25), IV(1) (20), III.C (16), IV (14), II.G (9), III.K (6: setting).
- Amended: in place (7 tagged lines). Programs: none.

**IV(3) `PART-IV4-SLAB.md`** (180 l.; body 17-159; tail 160-180)
- Proves: the slab near scri+ for III.K (K2) (b): posed on the exterior domain with the slab, from Sigma_IVP and the
  compact Sigma_c, in the chart translated in t (L0.1, L1.1); T2.1 (linear estimate on Omega^natural), T2.2 (the
  nonlinear solution there = III.K (K2) (b)), C2.3 (orders at scri+); boosted background in the translated class.
- Status (l.3-15): Proved (D312). Uses: III.K (19: setting of P1.2's proof), IV(2) (18), III.C (14), III.B (8).
- Amended: 75 (D311), 103 (D309). Programs: none.

**IV(4) `PART-IV5-CDMODES.md`** (275 l.; body 17-232; tail 233-275)
- Proves: III.E Thm 1.1 (1)-(3) at n = 4 at (v_C, e_C, C_0) = (1/2, 1/102400, <= 100), gamma_C = 1/h, h < h_* outside
  a countable set: §0 setting (constants at 30-38); §1 inputs (L1.1-1.6: fibre algebra, structure at infinity,
  indicial roots for every h <= 1e-6, the 1-form c_C, horizon threshold, (H1)-(H4) and (G)); §2 T2.1 = [Hin26a] Thm 6.2
  (mode stability at sigma != 0 and invertibility of the zero energy operator by the adjoint route), using IV(5) T7.3
  and IV(6) T3.1.
- Status (l.4-15): Proved (D312); amended D308 (L1.4, T2.1 (1)'s data surface).
- Uses: III.E (17), I.C (10), IV(5) (9), III.B (7). Lit: [Hin26a] §§3-4, 5.1, 6, App. A W.
- N1STAR inputs (272): 10.12-10.14, 10.18, 10.21-10.22, 10.52, 10.54, 10.79 (computed items of the main argument).
- Amended: 34, 103, 113, 187, 194, 225 (D308-D311). Programs: `n1/cpmodes5.py` (63), `n1/hthresh5.py` (131),
  `n1/cform5.py` (105, 108), `n1/uniform5.py` (82), `n1/solv5.py` (111), `n1/semiclass5.py` (49).

**IV(5) `PART-IV6-SOLV.md`** (922 l.; body 19-843; tail 844-922)
- Proves: T7.3 = [Hin26a] Thm 5.2 at n = 4, uniformly for b near b_0 (forward and initial value problems for Box^C_b
  on weighted semiclassical 3b-Sobolev spaces; a priori estimate (5.79), adjoint estimate (5.81) = P7.2): §0
  compactification with S^3 fibres in Kerr-Schild time, causal facts, fibre algebra, the 1-form (Def 0.1, L0.2-0.5);
  §1 elliptic and fibre infinity (L1.1, P1.2 = P5.5, P1.3 = P5.6); §2 saddle at r = r_c (P2.1 = P5.8); §3 corner saddle
  (P3.1 = P5.9); §4 sink (P4.1 = P5.11); §5 propagation (P5.1 = P5.12, P5.2-5.3 filling what the source leaves); §6
  energy (P6.1 = P5.16); §7 combination (P7.1 = P5.17, P7.2, T7.3, R7.4); §8 uniformity in b (L8.1).
- Status (l.3-17): Proved (D312). Uses: III.B (22), IV(4) (19: §0, L1.1, L1.4, (0.1), (2.1)).
- Lit: [Hin26a] §5.2 W, its P5.1 (pp. 37-39) READ; [Hin26d] bounded geometry (READ, record 10.65 (a)); N1STAR 10.13
  (i), 10.14, 10.22, 10.65 (a) as inputs.
- Amended: 679, 811, 819 (D311). Programs: none.

**IV(6) `PART-IV7-TFACE.md`** (486 l.; body 24-427; tail 428-486)
- Proves: III.E Thm 1.1 (4) (tf-admissibility for every weight in [-C_0, 2)): §0 the tf model on 4+1 Minkowski (L0.1,
  Def 0.2); P1.1 = [Hin26a] P B.2 (Fredholm, index 0: radial estimates, relative index per S^3 sector); T2.1 = Thm B.4
  (edge-b solvability); T3.1 = Thm B.1 (invertibility of the model's spectral family); T4.1 = III.E Thm 1.1 (4).
- Status (l.4-9): Proved (D315). Uses: I.C (25), IV(5) (17), IV(4) (14). Lit: [Mel93] Thm 6.5 BB (relative index
  theorem); [Hin26a] App. B W.
- Amended: 155, 323 (D312). Programs: `n1/cpmodes5.py` (65), `n1/cform5.py` (253, 274), `n1/tface5.py` (20, 63, 192),
  `n1/gaugepot5.py` (192).

### 1.6 Parts V-IX: gluing, dynamics, parameters, assembly, linear statement, gauge

**V `PART-V-GLUING.md`** (476 l.; body 20-413; tail 414-476)
- Proves: [CD03] Thm 8.1 at n = 4 for data with charges near Tangherlini's: §1 KIDs (L1.1), a linear flux identity
  (L1.2), the charges without a parity condition (P1.3), L1.4; §2 the Myers-Perry family and its charge map near
  Tangherlini (Def 2.1, L2.2, P2.3 = [CD03] P F.1's equivalent, C2.4); §3 the gluing (T3.1 = [CD03] Thm 8.1 + R8.4 at
  n = 4; L3.2 continuity in the parameter, L3.3 = L3.18, R3.4).
- Status (l.3-18): Proved (D317).
- Uses: III.B §3 (L3.1, Def 3.2, P3.4), VII (7: forward, in R3.4 and its amendment).
- Lit: [CD03] BB (Thms 3.6, 3.7, 3.9, 5.4, 5.6, 5.9, P5.10, C5.11, L3.18, T3.19, P G.1, App. E-F; pp. 4-78; valid for
  every n); [ER08] (34) and [CD03] (E.14) replaced by P2.3; [HHV21] not used. N1STAR 10.47, 10.63, 10.66, 10.68.
- Amended: 103 (D315), 291 (D315); R3.4's last two sentences superseded by the bracket at 404-412 (from
  `../GLUEDECAY5.md` R2.0, R3.0: VII uses only T3.1's proof in class form, with Tangherlini members on Sigma_IVP).
- Programs: `p5c/jac5.py` (427; 225 entries of the charge Jacobian), `n1/general5.py` (423).

**VI.A `PART-VI-DYN.md`** (363 l.; body 19-309; tail 310-363)
- Proves: the dynamical hypotheses (Dyn) at Tangherlini b_0: §0 coordinates and spectral symbols (L0.1); L1.1 ((H6),
  (K1) for every b); P2.1 ((H3), (H4) at b_0); P3.1 ((Gamma.1)-(Gamma.3) with exact separatrices); P4.1 ((K3)
  r-normal hyperbolicity); P5.1, L5.2 ((H8) global dynamics); T6.1 ((Dyn) at b_0).
- Status (l.3-17): Proved (D318); amended D373 (radii: Part I's r_0 at III.B's radius R_1/2, collar to 3R_1/8).
- Uses: III.B (24), I.B (8), I.A (7), II.B (5); IV(5) §0 (l.83: III.B's estimate at |x| >= R_1/4).
- Main argument: N1STAR 10.17 (P10.14 (ii)) and 10.19 (P10.16 (ii), (iv)) as computed inputs; R0P §0 and its F1
  (Lorentzian argument, l.84) as inputs; finding (VI.A7) at 339-351 records the D373 amendment.
- Programs: `p5c/dyn5.py` (164, 294), `n1/cform5.py` (347).

**VI.B `PART-VI2-HORIZON.md`** (165 l.; body 14-137; tail 138-165)
- Proves: the horizon near b_0: {r_A = r_+} an exact null hypersurface (L1.1-1.2), a diffeomorphism Psi_b fixing it
  (L2.1), P2.2 ((H3)-(H4) uniformly in b).
- Status (l.3-12): Proved (D323); amended D373 (read on {|x| >= 3R_1/8}). Uses: III.B (13), VI.A (10).
- Lit: [ER08] (horizon formula). Programs: `p5c/horizon5.py` (34).

**VI.B1 `PART-VI3-TRAPPING.md`** (512 l.; body 22-475; tail 476-512)
- Proves: by separability: spheroidal coordinates and separation (L0.1), the radial function (L1.1, C1.2), the trapped
  set ((Gamma.1)-(Gamma.3) near b_0: L2.1, P2.2 with closed-form separatrices), r-normal hyperbolicity ((K3), (K4):
  L3.1-3.3, P3.4 with the tangential bound from the integrable flow), global dynamics ((H8): P4.1), T5.1 ((Dyn) near
  b_0 with (H5)).
- Status (l.3-14): Proved (D323); amended D373 (finding (VI.B'6) at 500). Uses: VI.A (23), VI.B (17), III.B (15).
- Lit: [Hin26c] §4.2.3 W. Programs: `p5c/trap5.py` (14, 81, 125, 511).

**VI.C `PART-VI4-PARAMS.md`** (165 l.; body 16-134; tail 135-165)
- Proves: T2.1: the parameters the parts leave open can be chosen together, in an order with no circular threshold
  (steps (0)-(n) at 44-100); §1 the table of conditions (rows c1-c4 damping, u1-u5 gauge, d1-d2, b*, w1-w2 decay,
  n1 nonlinear, ...; each row keyed by file:line); §3 two quantifier checks (III.E Thm 1.1's proved range is all the
  parts use, by enumeration of lines; III.F2 §5 closed by III.H C4.3).
- Status (l.3-14): Proved (D332); amended D322 (rows d1-d2), D327-D328 and D331 (§3), D390 and D621 (row w1's eps_ind,
  delta_50 = 1.94137e-8; row n1's pointer).
- Amended in place: row w1 at 38 (brackets D390, D621), row n1 at 42 (D621).
- Programs: `n1c/epsind5.py` E3 (38), `p5c/gammac5.py` G1-G5 + `gammac5.tsv` (113, 118), `p5c/damping5.tsv` (116).
- Interface: rows w1, w2 and §3 are cited by the paper (8.4-8.8).

**VII `PART-VII-ASSEMBLY.md`** (565 l.; body 22-467; tail 468-539; amendment record 540-565)
- Proves: Thm 0.2 = the paper's Theorem 4: §0 setting in the main argument's coordinates (tau, x), Vaidya background,
  domain Omega and solution g_lambda of its Theorem E; L0.1 (what lies in the data class); §1 the solution after the
  shell (L1.1-1.2: g_lambda as III.B's Kerr-Schild Tangherlini, Sigma_IVP in the chart); §2 gluing in the class (L2.1,
  P2.2 = [CD03] Thm 8.1 with G-equivariance, C2.3 the data of (i)); §3 III.K in the class (O(4) action, L3.1
  naturality (C1)-(C4), P3.2 = III.K T4.3 in the class); §4 proof of T0.2 (incl. R4.1).
- Status (l.3-20): Proved (D324); amended D326-D328 (eps_t), D608-D609 (L3.1 (C3)), D621, D626, D628.
- Uses: III.K (39), Part V (proof of T3.1), VI.C (14), III.B (14), II.G (11), IV (8). Main argument: N1STAR §0.1,
  (1.1), Theorem E (24-30; L1.1-1.2); R0P §9 (re-proof at r_flat).
- Lit: [CD03] Thm 8.1 (via V), [DS23] Thm 2.4 BB (Step 8 of L1.1's proof, 116), [Hin26] §13.
- Amended in place: 277, 285, 302, 305, 309, 311, 316, 319, 340, 341, 414 (D621 brackets; L3.1 (C3) and its uses).
- Programs: `n1c/vii5read.py` Q1-Q4 (324, 344; Q3 checks delta* pointwise -- mathematical), `n1c/vii5census.py`
  V1-V2 (509-561; census of the document's spellings -- provenance), `n1c/VII5-READING.tsv`.

**VIII `PART-VIII-LINEAR.md`** (407 l.; body 24-353; tail 354-407)
- Proves: linear stability of 5D Tangherlini in the gauge of the nonlinear problem: §0 setting (III.K §0 kept;
  linearised operators L, L^natural); L1.1, P1.2 (the linear initial solution = III.K P1.2 linearised); L2.1; T2.2
  (every linearised data set in III.K's class has a linearised vacuum development settling to a linearised Myers-Perry
  metric at t_*^(-(alpha-2)+eps)); C2.3 (in the class: a change of mass alone); R2.4 (what is not claimed).
- Status (l.3-4): Proved (D336); amended D378 (Step 4), D621 (Step 4's compact sets: II.F L1.4 (a) at theta = 0, 286),
  D626 (sources). Uses: III.K (44), VII (21: §0, L3.1, P3.2, T0.2's eps_t, §4), II.F (11), III.C2 (10), IV(1)-(2).
- Lit: [KI03], [HKW18] (other routes, mentioned only). Amended in place: 286 (D378, D621); record 400-407.
- Programs: `n1c/scrirad5.py` (406).

**IX `PART-IX-GAUGE.md`** (407 l.; body 23-337; tail 338-407)
- Proves: §0 setting; §1 the Cauchy problem and the domain (L1.1, L1.2: the future half of a Cauchy development past
  Sigma_IVP); §2 T2.2 (linearised vacuum solutions with gauge-equivalent Cauchy data differ by L_X g, X unique up to
  Killing fields), L2.1, C2.3 (Part VIII's solution in any gauge), R2.4 (nothing on the decay of X).
- Status (l.3-8): Proved (D617); repaired D610 (domain), repair read D611.
- Uses: VIII (30), III.K (11: §0, P1.2), III.B (10), II.F (6: §1.4, L1.3). Lit: [BGP] BB (Def 1.3.8 p.23, C1.3.12,
  T1.3.13 p.24, §1.5 p.33, C3.2.4 p.76, P3.2.5 p.81, T3.2.11 pp.85-86, C A.5.4 p.174, L A.5.9 p.176); [See64] BB.
- Amended in place: 52 (D610, D617), 348. Programs: `n1c/ix5.py` X1-X8 (21, 193-386, 392).

### 1.7 The two non-part files

**`README.md`** (1,483 l.) -- the index and status log. 1-14 purpose (D184); 15-98 the plan table (Part, source,
content, status; the "content" column is a good one-line gist per part); 100-1483 one section per part: a first
paragraph naming the file and its results (usable as a gist), then verifier and repair history. No mathematics that is
not in the parts. Programs mentioned: as the parts. Status: none of its own. DROP entirely; mine the plan table's
content column and the first paragraph of each section for chapter introductions.

**`BASEPOINT-LEDGER.md`** (460 l.) -- "the census of III.I16 Theorem 3.1 by reading": 8-50 what the file is and the
categories (a)-(h) of base-point uses; 51-62 batch table; 63-460 five batches (one summary paragraph each, then a table
part | line | category | property used | supplied by | uniform | note; 324 rows in all) over III.I(1)-III.I(14),
III.J-III.J3. Status (3-6): read, all repairs folded into III.I(15) (D328-D333). It is the completeness argument of
III.I(15) T3.1 (see risks). Not mathematics as written (rows keyed by file:line); its "supplied by" column is.

### 1.8 One-line index (file, part, lines, kept range = intro + body, status, chapter of section 3)

"Kept" runs from the end of the status paragraph to the end of the body; the tail and the status paragraph are dropped.

| file (PART-) | part | lines | kept | status (own line) | ch. |
|---|---|---|---|---|---|
| I-SPECTRAL | I.A | 1940 | 17-1889 | Proved D197 | S1 |
| I-B-HIGHENERGY | I.B | 2133 | 15-2055 | Proved D231 | S2 |
| I-C-LOWENERGY | I.C | 1512 | 12-1434 | Proved D194 | S3 |
| II-A-SETUP | II.A | 1595 | 20-1497 | proved D197 | S4 |
| II-A2-STANDARD | II.A1 | 839 | 14-785 | Proved D197 | S4 |
| II-B-DYNAMICS | II.B | 746 | 14-694 | Proved D326 | S5 |
| II-C-OPERATORS | II.C | 858 | 17-795 | Proved D327 | S5 |
| II-C2-TRAPPING | II.C1 | 435 | 17-400 | Proved D328 | S5 |
| II-D-REGULARITY | II.D | 1104 | 18-1042 | Proved D326/D331 | S6 |
| II-D2-BREGULARITY | II.D1 | 682 | 18-611 | Proved D327 | S6 |
| II-E-ENERGY | II.E | 1305 | 19-1206 | Proved D327 | S7 |
| II-F-IOTA | II.F | 2791 | 18-1775 / 1776-2619 | Proved D216 | S8 / S9 |
| II-F2-TAME | II.F1 | 851 | 14-746 | Amended D327; Proved D216 | S9 |
| II-G-NASHMOSER | II.G | 547 | 14-453 | Proved D216; amended D304 | S10 |
| II-G2-DECAY | II.G1 | 1330 | 15-1198 | Proved D217 | S10 |
| III-A-PREREQ | III.A | 775 | 13-723 | Proved D231 | S11 |
| III-A2-HARMONICS | III.A1 | 553 | 14-481 | Proved D324 | S11 |
| III-B-FAMILY | III.B | 560 | 13-509 | Proved D221 | S11 |
| III-C-EXTERIOR | III.C | 578 | 10-495 | Proved D245 | S17 |
| III-C2-POLYHOM | III.C1 | 305 | 10-275 | Proved D292 | S26 |
| III-C3-BOOSTDATA | III.C2 | 270 | 9-230 | Proved D292 | S26 |
| III-D-GAUGEPOT | III.D | 517 | 14-466 | Proved D229 | S13 |
| III-D2-ZEROENERGY | III.D1 | 389 | 14-339 | Proved D231 | S13 |
| III-D3-SYMSTATES | III.D2 | 330 | 13-287 | Proved D231 | S13 |
| III-D4-GENSTATES | III.D3 | 309 | 11-265 | Proved D235 | S13 |
| III-E-CONSTRAINT | III.E | 243 | 12-211 | Proved D235 | S14 |
| III-E2-V1STATES | III.E1 | 262 | 9-216 | Proved D231 | S14 |
| III-F-LINEARISED | III.F | 258 | 10-215 | Proved D235 | S15 |
| III-F2-INDICIAL | III.F1 | 526 | 14-492 | Proved D238 | S15 |
| III-F3-MODES | III.F2 | 290 | 17-270 | Proved D238 | S15 |
| III-F4-ZERO | III.F3 | 489 | 17-457 | Proved D238 | S15 |
| III-F5-PAIRINGS | III.F4 | 366 | 16-330 | Proved D238 | S15 |
| III-G-SPECTRAL | III.G | 970 | 15-931 | Proved D240 | S16 |
| III-G2-IOTA | III.G1 | 512 | 15-472 | Proved D241 | S16 |
| III-G3-GRAFT | III.G2 | 447 | 12-387 | Proved D244 | S16 |
| III-G4-RESONANT | III.G3 | 478 | 10-407 | Proved D247 | S17 |
| III-G5-TF | III.G4 | 805 | 12-726 | Proved D249 | S17 |
| III-H-AUGMENT | III.H | 608 | 13-554 | Proved D252 | S18 |
| III-H2-ADMISS | III.H1 | 534 | 14-463 | Proved D256 | S18 |
| III-H3-UNIFORM | III.H2 | 384 | 14-339 | Proved D299 | S19 |
| III-I-CONE | III.I | 497 | 13-445 | Proved D258 | S19 |
| III-I2-SCRI | III.I(1) | 277 | 9-239 | Proved D258 | S19 |
| III-I3-ALMOST | III.I(2) | 485 | 9-441 | Proved D259 | S19 |
| III-I4-BOOST | III.I(3) | 316 | 10-276 | Proved D261 | S20 |
| III-I5-UNBOOST | III.I(4) | 457 | 12-407 | Proved D263 | S20 |
| III-I6-ALMOSTBDD | III.I(5) | 271 | 9-234 | Proved D266 | S20 |
| III-I7-PARAMS | III.I(6) | 379 | 9-333 | Proved D268 | S20 |
| III-I8-UNPARAM | III.I(7) | 502 | 12-455 | Proved D269 | S21 |
| III-I9-COMMOTION | III.I(8) | 470 | 11-418 | Proved D271 | S21 |
| III-I10-CORR4 | III.I(9) | 465 | 11-408 | Proved D274 | S21 |
| III-I11-SPACETIME | III.I(10) | 453 | 15-408 | Proved D275 | S22 |
| III-I12-SPECTRAL | III.I(11) | 572 | 14-525 | Proved D277 | S22 |
| III-I13-EXPANSION | III.I(12) | 479 | 13-445 | Proved D280 | S22 |
| III-I14-LEVELS | III.I(13) | 214 | 16-187 | Proved D324 | S22 |
| III-I15-AUGMENT5 | III.I(14) | 507 | 12-458 | Proved D287 | S23 |
| III-I16-BASEPOINTS | III.I(15) | 874 | 23-805 | Proved D333 | S25 |
| III-J-PARAM | III.J | 422 | 12-376 | Proved D287 | S23 |
| III-J2-LINEAR | III.J1 | 194 | 11-163 | Proved D287 | S23 |
| III-J3-TAME | III.J2 | 396 | 15-344 | Proved D295 | S24 |
| III-J4-EXACT | III.J3 | 726 | 14-672 | Proved D296 | S24 |
| III-K-NONLINEAR | III.K | 775 | 14-504, 620-763 | Proved D312 (+ D378-D629) | S27 |
| IV-EB | IV | 353 | 13-328 | Proved D309 | S26 |
| IV2-TAME | IV(1) | 231 | 13-210 | Proved D311 | S26 |
| IV3-NM | IV(2) | 441 | 17-400 | Proved D311 | S26 |
| IV4-SLAB | IV(3) | 180 | 17-159 | Proved D312 | S27 |
| IV5-CDMODES | IV(4) | 275 | 17-232 | Proved D312 | S14 |
| IV6-SOLV | IV(5) | 922 | 19-843 | Proved D312 | S14 |
| IV7-TFACE | IV(6) | 486 | 11-427 | Proved D315 | S14 |
| V-GLUING | V | 476 | 20-413 | Proved D317 | S28 |
| VI-DYN | VI.A | 363 | 19-309 | Proved D318; amended D373 | S12 |
| VI2-HORIZON | VI.B | 165 | 14-137 | Proved D323; amended D373 | S12 |
| VI3-TRAPPING | VI.B1 | 512 | 16-475 | Proved D323; amended D373 | S12 |
| VI4-PARAMS | VI.C | 165 | 16-134 | Proved D332; amended D390, D621 | S27 |
| VII-ASSEMBLY | VII | 565 | 22-467 | Proved D324; amended D326-D628 | S27, S28, S30 |
| VIII-LINEAR | VIII | 407 | 6-353 | Proved D336; amended D378-D626 | S29 |
| IX-GAUGE | IX | 407 | 10-337 | Proved D617 | S29 |
| README | -- | 1483 | none | -- | dropped |
| BASEPOINT-LEDGER | -- | 460 | supply column only | read D328-D333 | S25 |

## 2. Material to drop

Nothing listed here is mathematics the edition needs, except where marked "fold" or "mine". Line ranges are inclusive.

### 2.1 Whole files
- `README.md` 1-1483: index, plan table and per-part verification history. Mine only the plan table's "content"
  column (19-98) and each part section's first paragraph for chapter introductions; drop everything else.
- `BASEPOINT-LEDGER.md` 1-460: a line-keyed reading census (provenance of III.I(15) T3.1's completeness). Mine the
  "supplied by" column of its 324 rows (63-460) for chapter S25 (see risk R1); drop the rest.
- `checks/admiss5.tsv`, `checks/gammac5.tsv`, `checks/damping5.tsv`: enumerations of document lines; not mathematics.

### 2.2 Status paragraphs (every file; D-labels, verifier numbers, "written/verified/proved", "replaces 10.x")
I.A 3-15; I.B 3-13; I.C 3-10; II.A 3-18; II.A1 3-12; II.B 3-12; II.C 3-15; II.C1 3-15; II.D 3-16; II.D1 3-16;
II.E 3-17; II.F 3-16; II.F1 3-12; II.G 3-12; II.G1 3-13; III.A 3-11; III.A1 3-12; III.B 3-11; III.C 3-8; III.C1 3-8;
III.C2 3-7; III.D 3-12; III.D1 3-12; III.D2 3-11; III.D3 3-9; III.E 3-10; III.E1 3-7; III.F 3-8; III.F1 3-12;
III.F2 3-15; III.F3 3-15; III.F4 3-14; III.G 3-13; III.G1 3-13; III.G2 3-10; III.G3 3-8; III.G4 3-10; III.H 3-11;
III.H1 3-12; III.H2 4-12; III.I 3-11; III.I(1)-(15): I2 3-7, I3 3-7, I4 3-8, I5 3-10, I6 3-7, I7 3-7, I8 3-10, I9 3-9,
I10 3-9, I11 3-13, I12 3-12, I13 3-11, I14 3-14, I15 3-10, I16 4-21; III.J 3-10; III.J1 3-9; III.J2 3-13; III.J3 3-12;
III.K 3-12; IV 3-11; IV(1) 4-11; IV(2) 4-15; IV(3) 3-15; IV(4) 4-15; IV(5) 3-17; IV(6) 4-9; V 3-18; VI.A 3-17;
VI.B 3-12; VI.B1 3-14; VI.C 3-14; VII 3-20; VIII 3-4; IX 3-8.
Exception: from III.C onward the status paragraph also holds the one-sentence statement "This part proves, at spatial
dimension n = 4, ..."; keep that sentence's mathematical content for the chapter introduction.
In the intros that follow (1.8 "kept" ranges), drop the sentences "This part replaces ... the deductions of
N1STAR-PROOF.md 10.x" (I.A 10-12, I.B 10-12, I.C 6-9 and similar) and every "labels as in the record" convention line.

### 2.3 Closing sections ("What this part found", "Findings, labels and sources", "Sources")
Drop: I.A 1890-1940; I.B 2056-2133; I.C 1435-1512; II.A 1498-1595; II.A1 786-839; II.B 695-746; II.C 796-858;
II.C1 401-435; II.D 1043-1104; II.D1 612-682; II.E 1207-1305; II.F 2620-2791 (incl. verifier sections 9.4 at 2750,
9.5 at 2777); II.F1 747-851 (incl. 8.4 at 839); II.G 454-547 (incl. 6.3 at 529); II.G1 1199-1330 (incl. 7.3 at 1298);
III.A 724-775; III.A1 482-553 (incl. 3.4 at 538); III.B 510-560 (incl. 7.3 at 534); III.C 496-578 (incl. 6.4-6.5 at
558, 572); III.C1 276-305; III.C2 231-270; III.D 467-517; III.D1 340-389; III.D2 288-330; III.D3 266-309; III.E 212-243;
III.E1 217-262; III.F 216-258; III.F1 493-526; III.F2 271-290; III.F3 458-489; III.F4 331-366; III.G 932-970;
III.G1 473-512; III.G2 388-447 (incl. 5.1 at 425); III.G3 408-478 (incl. 4.4 at 464); III.G4 727-805; III.H 555-608;
III.H1 464-534; III.H2 340-384; III.I 446-497; I2 240-277; I3 442-485; I4 277-316; I5 408-457; I6 235-271; I7 334-379;
I8 456-502; I9 419-470; I10 409-465; I11 409-453; I12 526-572; I13 446-479; I14 188-214; I15 459-507; I16 806-874;
III.J 377-422; III.J1 164-194; III.J2 345-396; III.J3 673-726; III.K 505-583; IV 329-353; IV(1) 211-231; IV(2) 401-441;
IV(3) 160-180; IV(4) 233-275; IV(5) 844-922; IV(6) 428-486; V 414-476; VI.A 310-363; VI.B 138-165; VI.B1 476-512;
VI.C 135-165; VII 468-539; VIII 354-407; IX 338-407.
Optional "mine": the findings "against the source" (sign slips and gaps in [Hin26c], [Hin26], [Hin23a], [Hin26a],
[CD03]; e.g. I.A 1890-1925 (F1)-(F4), I.B 2056-2120, I.C 1435-1495 (F1)-(F7), II.A 1498-1574 (G1)-(G7), V 414-454
(V1)-(V8)) may be condensed into one "Remarks on the sources" paragraph per chapter, in neutral words and without labels;
the "Labels" tables (concordance with the source's numbering) may be kept as a correspondence table.

### 2.4 Amendment records and history inside the mathematics
- III.K 584-619 (section 6 heading and its *Record.*, D626, D628, D629 paragraphs): drop. Keep L6.1 (620-692) and L6.2
  (693-763) with their bracketed amendments folded into the text (see S27); drop 764-774 (the remark citing a program
  and the "Sources for this section" with its three bracketed amendments).
- VII 540-565 (section 6, "Amendment record"): drop (census widenings, reader findings).
- VIII 400-407 (amendment record inside the tail): dropped with the tail; the math it describes is already at 286.
- V 404-412: FOLD, not drop: it replaces the last two sentences of Remark 3.4 (400-402).
- VI.C 101-134 (section 3, "Two quantifier checks"): drop the enumeration argument (it proves a property of the
  document's own lines with `gammac5.py`); replace by the convention that (v_C, e_C, C_0, gamma_C) are fixed
  once, in S14.
  Keep 128-134 (III.F2 §5 closed by III.H C4.3) as one sentence.
- II.F1 174-179 (the "by enumeration" sentences of L2.1 (b), `admiss5.py`): drop; state L2.1 (b) with the explicit
  hypothesis "Definition 3.3 (3) is not assumed" and cite where (3) is used (risk R6).
- III.I(15) 692-698 (the ledger paragraph of T3.1's proof) and the verifier attributions in 645-690 ("verifier 145's
  M1, m1" etc.): drop the attributions, keep the list of forms.

### 2.5 In-body tags (edit, do not delete the sentence)
768 lines inside the kept ranges carry a D-label, a verifier/reader attribution, "the record"/N1STAR/BEYOND5
pointers, a READ/computed/deduced label, a program name or a PART file name. Heaviest: III.I(15) 100, VII 70, I.A 40,
VI.C 37, III.K 28, I.B 26, IV(4) 20, VIII 20. Files with none: III.H, III.J1, III.I(1)-(9), III.I(11)-(13). The full
list (file, kept body, count, line ranges) is Appendix A. Rule: delete the parenthetical; turn "(computed, `x.py` G1)"
into "(computation C_k)"; turn "READ at source" into a plain citation with theorem and page; turn "the record's 10.x"
into a citation of the main argument's numbered result (other mappers' numbering).

## 3. Chapter plan for the stability theory

Thirty chapters, S1-S30, in dependency order: every result a chapter uses is proved in an earlier chapter, in the same
chapter before its use, or is an outside black box (BB) or an input from the main argument (named "MAIN"). Each chapter
reads at most about 2,300 source lines (the largest, S4, reads 2,219 body lines). "Source" ranges are the kept ranges of
1.8, in reading order; the status paragraph and the tail of each file are always excluded (section 2) and are not
repeated below. Estimated cleaned lengths are in Markdown lines of the source's width (about 110 characters); the
factor is about 0.92 of body lines, lower where the process content is heavy.

Grouping into parts of the edition (suggested): A. Spectral theory on bundles (S1-S3); B. Analysis on the compactified
spacetime (S4-S10); C. The Myers-Perry family and its dynamics (S11-S12); D. Linear theory at zero and low energy
(S13-S18); E. Forward solutions and their asymptotics (S19-S25); F. Exterior, nonlinear theorem, gluing, linear
statement (S26-S29); G. Assembly (S30).

A note for every writer: the parts are labelled by the companion paper they write out ("[Hin26c] Theorem 9.5 at
n = 4"). In the edition each result gets its own number and a sentence "This is [Hin26c, Theorem 9.5] in dimension
4 + 1, with ..."; the dimensional changes (3/2 for 1, 5/2 for 2, rho^4 for rho^3, S^3 harmonics) are mathematics and
stay.

### S1. The spectral family at bounded nonzero frequencies
- Purpose: Fredholm theory and invertibility of the stationary spectral family on bundles at real sigma != 0 (and
  Im sigma >= 0), with constants uniform in the operator; fixes the hypotheses (H1)-(H5) that every later chapter
  instantiates.
- Source: I.A 17-1889 (§1 setting 30-191; §2 calculus 192-326; §3 commutator lemma 327-556; §4 radial 557-1145; §5
  elliptic/propagation 1146-1279; §6 artificial boundary 1280-1462; §7 Thm 7.2 1463-1866; §8 Thm 8.1 1867-1889).
- Fold: none beyond in-place text (D195-D197 repairs already in). Keep 1386-1391 only as mathematics (drop its
  "corrected form of N1STAR 10.86 (r)" clause).
- Depends on: nothing earlier. MAIN: the threshold of the actual operators is a computation of the main argument
  (I.A:708, `hthresh5.py`) -- state as a hypothesis here, verified in S12-S14.
- Programs: `n1/hthresh5.py` (one mention). Outside: [HJS] BB (list in 1.1); [Hin26c] §§9.1-9.2 and L5.12 (cited
  for comparison; proofs written).
- Est.: 1,700 lines.

### S2. The spectral family at high frequencies
- Purpose: semiclassical scattering calculus with matrix symbols and variable orders; high-frequency estimates incl.
  normally hyperbolic trapping with loss; [Hin26c] Thm 9.16 at n = 4 uniformly in the operator.
- Source: I.B 15-2055 (§1 26-234; §2 calculus 235-515; §3 516-653; §4 654-944; §5 945-1276; §6 trapping 1277-1754;
  §7 1755-1859; §8 proof 1860-2037; §9 uniformity 2038-2055).
- Fold: L6.0 (1293-1350) and C4.6' (924-944) are already in place; strip "(D189)", "(D226)" from their titles.
- Depends on: S1. Programs: none. Outside: [HJS] via S1; [HV16], [Dya16] arguments written out; [Hin17] P3.12 (L6.0).
- Est.: 1,850 lines.

### S3. The spectral family at zero and low frequencies
- Purpose: b-analysis at conic ends; zero energy operator, transition face normal operator, tf-admissibility, the
  asymptotically Minkowski case, uniform low-energy estimates (with an adjoint estimate), index 0.
- Source: I.C 12-1434 (§1 32-88; §2 89-364; §3 365-503; §4 504-703; §5 704-875; §6 876-1386; §7 1387-1434).
- Fold: none. Depends on: S1, S2.
- Programs: MISSING `checks_c.py` (455, 779, 830: sympy checks of a scalar formula, the Hankel ODE and spec_b
  = {-l, l+2}); re-create as computations or replace by hand verification (risk R8).
- Outside: [DLMF] BB (10.2, 10.7.7, 10.17.2, 10.17.5-6); [RS1] Thm VI.14 BB.
- Est.: 1,300 lines.

### S4. The compactified spacetime, its calculi and the standard estimates
- Purpose: the compactification M with faces iota+, scri+, K+, I_0; b-, 3b-, eb-, e3b-structures; the e3b-calculus;
  Fourier/Mellin transforms with n = 4 weights; supported/extendible spaces; finite regularity; elliptic and real
  principal type estimates with b-regularity, tame.
- Source, in this order: II.A 20-1082 (§§1-8; §3 at 343-447 is the quoted [SBG] black box (S1)-(S11): keep as a
  numbered list of cited statements); II.A1 14-785 (proves (L3) = Thm 3.1 and (L4) = Thm 5.4); II.A 1083-1497 (§9,
  which uses (L3)-(L4)).
- Fold: none. Exclude: II.A 1498-1595, II.A1 786-839.
- Depends on: S1 (L3.1-3.2, P5.2), S3 (b-spaces). Programs: none.
- Outside: [SBG] BB (Defs 1.1-4.20, Props 3.19-4.22, Thms 3.21-3.52; pp. 43, 66, 73-74); [HJS] consulted.
- Est.: 2,050 lines (the largest; may be split after II.A §8 if a writer prefers: S4a 1,063 + S4b 1,187 source lines).

### S5. Null-bicharacteristic dynamics, operator classes, and trapping of perturbed metrics
- Purpose: e3b-phase-space dynamics of the stationary model under (K1)-(K4); stationary and asymptotically stationary
  wave-type operators, admissibility, the time function t_*^flat, order functions; persistence of the stable and
  unstable hypersurfaces of the trapped set.
- Source: II.B 14-694; II.C 17-795; II.C1 17-400.
- Fold: II.C1's T_flat := 2/C' (296-299, 381-382) is already in place; strip the D-tags.
- Depends on: S1-S4. Programs: none. Outside: [Hin23c] App. C (construction written out); [Hin21] (replaced).
- Est.: 1,650 lines.

### S6. Global microlocal regularity
- Purpose: the global edge-3b regularity estimate with loss one at the trapped set; radial estimates; the estimates
  with b-regularity and their tame forms.
- Source: II.D 18-1042; II.D1 18-611.
- Fold: II.D §4's setting at T_flat (550-579) in place. Depends on: S2, S4, S5. Programs: none.
- Outside: [Hin21] Thm 3.9 replaced by II.D §4.
- Est.: 1,460 lines.

### S7. Energy estimates, solvability on slabs, the black hole interior, the global estimate
- Source: II.E 19-1206. Depends on: S4-S6. Programs: none. Outside: none beyond [Hin26c] §8 (written).
- Note: II.E cites II.F1 three times (tame bounds under an integer-order hypothesis): forward remarks; state the
  hypothesis locally.
- Est.: 1,080 lines.

### S8. The normal operator at future timelike infinity
- Purpose: the iota+-model: setting with the causal theory (L1.3 uniqueness to the future, L1.4 monotone functions along
  causal curves), the semiclassical calculus on iota+, high frequencies without and with b-regularity, bounded
  frequencies via the 0-calculus, the Fourier transform bound (L5.7).
- Source: II.F 18-1775 (§1 39-315; §2 316-671; §3 672-1171; §4 1172-1352; §5 1353-1775).
- Fold: L1.3's inner-boundary input and L1.4 (a) at theta = 0 are cited by S27 and S29 (D378, D621); make sure L1.4 (a)
  is stated with the compact sets it gives (risk R4).
- Depends on: S1-S7. Programs: `n1/iplusnorm5.py` N1-N9 (numerals at n = 4; 21, 1380, 1702, 1716, 1792).
- Outside: [0C] BB (Def 1.2, P2.7, C3.3, Thm 3.4, R3.5, C3.6; pp. 5-34); [BGP] BB (pp. 18, 21-23, 68, 72, 174, 176);
  [MM87] via [0C].
- Est.: 1,600 lines.

### S9. Forward solutions on e3b-spaces and their tame estimates
- Source: II.F 1776-2619 (§6 forward solutions of the iota+-normal operator; §7 the modified operator P_+; §8 Thm 8.1 =
  [Hin26c] Thm 10.1); II.F1 14-746 (Thm 1.1 = [Hin26c] Thm 11.1, C1.2; R7.1-7.3).
- Fold: II.F1 L2.1 (b) (around 174-179): replace the enumeration by an explicit hypothesis (2.4). Depends on: S4-S8.
- Programs: `n1/iplusnorm5.py` N4-N5 (2505); `p5c/admiss5.py` (dropped with the enumeration).
- Outside: [SBG] (S3), (S5), (S8), (S10) BB.
- Est.: 1,430 lines.

### S10. The Nash-Moser theorem; Fourier transforms, resolvent bounds and the radiation field
- Source, in this order: II.G 14-453 (Thm 2.1 with (iii) as amended, P3.1 smoothing operators, L4.1 tame bounds, §5
  weights); II.G1 15-1198.
- Fold: II.G (H10) justification (tail 506-511, first three sentences) as a remark after Thm 2.1 (the weaker support
  hypothesis (iii) is all the proof uses). Depends on: S1-S3 (II.G1), S7-S9 (II.G). Programs: none.
- Outside: [SR89], [Hin24a], [Hin23b], [Tay11a], [Li25], [Hin26b], [HV20] cited by the source only; none used.
- Est.: 1,470 lines.

### S11. Harmonics on S^3, the Myers-Perry family, the gauge-fixed Einstein equation, partial polyhomogeneity
- Source, in this order: III.A1 14-481; III.B 13-509; III.A 13-723.
- Fold: none. Add from IV(5) §0 the extension of III.B §3.1's estimate to |x| >= R_1/4 (IV(5) 19-210, the part used by
  VI.A Lemma 1.1 at VI.A:83); and fix the inner radius as a parameter (risk R3).
- Depends on: S4, S5 (III.B uses II.A, II.C), S10 (III.A uses II.G1 P3.3, P3.5, L3.1).
- Programs: `n1/harm5.py` K-list (III.A1: 18-545), `n1/lin5.py` (263, 487, 541); MISSING `d215/chk3b.py`,
  `chkric.py`, `chkboost.py` (III.B 107, 134, 154, 187, 397) -- sympy checks of the Kerr-Schild identities, the Ricci
  flatness and the boosts; must be re-created (risk R8).
- Outside: [ER08] BB ((14)-(16), (31)-(34), (42)-(44), pp. 10-19); [MP86] BB; [Hig87] comparison only.
- Est.: 1,500 lines.

### S12. The dynamics of the Myers-Perry metrics near Tangherlini
- Purpose: verify the metric hypotheses (H3)-(H8), (Gamma.1)-(Gamma.3), (K1)-(K4) of S1-S5 for g_b, b near b_0:
  Tangherlini first (VI.A), the horizon near b_0 (VI.B), trapping and global dynamics by separability (VI.B1).
- Source: VI.A 19-309; VI.B 14-137; VI.B1 16-475.
- Fold: the radii of D373 (VI.A finding (VI.A7), tail 339-351; R0P §0): Part I's r_0 at III.B's radius R_1/2 with the
  collar to 3R_1/8 -- the body already uses them (VI.A 73-91); write the choice once, in S11/S12, as a definition.
  VI.A:84 cites R0P F1 (a Lorentzian argument) -- MAIN; bring the argument in (a few lines) or cite the main chapter.
- Depends on: S1, S2 (hypotheses), S5 (II.B), S11. Forward mentions of III.D, III.F, IV(4) (VI.A 11-13, 346-348) state
  which operator hypotheses are left to S13-S15; keep as forward pointers.
- MAIN: N1STAR 10.17 (P10.14 (ii)) and 10.19 (P10.16 (ii), (iv)) computed inputs.
- Programs: `p5c/dyn5.py` (164, 294), `p5c/horizon5.py` (VI.B 34), `p5c/trap5.py` (VI.B1 14, 81, 125), `n1/cform5.py`.
- Outside: [ER08] (horizon formula) BB; [Hin26c] §4.2.3 written.
- Est.: 830 lines.

### S13. The gauge potential operator
- Source: III.D 14-466; III.D1 14-339; III.D2 13-287; III.D3 11-265.
- Fold: none. Depends on: S1-S3, S11, S12 ((Dyn)). MAIN: N1STAR 10.15-10.20, 10.28-10.30 computed statements.
- Programs: `n1/harm5.py`, `trap5.py`, `modes5.py`, `lin5.py`, `hienergy5.py`, `thresh5.py`, `gaugepot5.py`,
  `zstates5.py`, `genstates5.py`, `puregauge5.py` (all n1/).
- Outside: [AHW24] Thm 5.1 replaced by III.D P6.2 (no citation needed); [Hin24b] replaced.
- Est.: 1,170 lines.

### S14. Constraint propagation and constraint damping
- Purpose: state and prove the theorem on the constraint propagation operator Box^C_b (mode stability, zero energy,
  indicial roots, tf-admissibility) and derive its dual states.
- Source, in this order: III.E 12-73 (§1: setting and the statement of Thm 1.1); IV(4) 17-151 (§0 constants,
  (v_C, e_C, C_0) = (1/2, 1/102400, <= 100), gamma_C = 1/h; §1 inputs L1.1-1.6); IV(5) 19-843 ([Hin26a] Thm 5.2
  at n = 4 = T7.3, uniform in b); IV(6) 11-384 (§§0-3: the tf model, Fredholm index 0, edge-b solvability, Thm 3.1);
  IV(4) 152-232 (§2: T2.1 = Thm 1.1 (1)-(3)); IV(6) 385-427 (§4: T4.1 = Thm 1.1 (4)); III.E 74-211 (§§2-3: the adjoint,
  the dual states); III.E1 9-216 (the vector type 1 dual states).
- Fold: III.E Thm 1.1 (3) as widened (54: counts by type, simple roots, the clauses (C1)-(C4) used by III.F1); fix the
  damping constants once here (replaces VI.C §3's enumeration and VI.C rows c1-c4); IV(4) 34, 103, 113, 187, 194, 225
  and IV(5) 679, 811, 819 and IV(6) 155, 323 (amended clauses already in the text; strip tags).
- Depends on: S1, S3, S11, S12, S13 (III.D2 for III.E). MAIN: N1STAR 10.12-10.14, 10.18, 10.21-10.22, 10.31, 10.52,
  10.54, 10.65 (a), 10.79 (IV(4):272, IV(5) tail) -- computed inputs.
- Programs: `n1/cpmodes5.py`, `damping5.py`, `dual5.py` (III.E); `mp5.py`, `dualv1_5.py` (III.E1); `cpmodes5.py`,
  `hthresh5.py`, `cform5.py`, `uniform5.py`, `solv5.py`, `semiclass5.py` (IV(4)); `cform5.py`, `tface5.py`,
  `gaugepot5.py` (IV(6)).
- Outside: [Hin26a] §§2-6, App. A-B written out; [Hin26a] P5.1 (pp. 37-39) and [Hin26d] bounded geometry cited
  (BB); [Mel93] Thm 6.5 BB (relative index theorem, IV(6) §1).
- Est.: 1,690 lines.

### S15. The linearised gauge-fixed Einstein operator: structure, indicial roots, modes, zero energy
- Source: III.F 10-215; III.F1 14-492; III.F2 17-270; III.F3 17-457; III.F4 16-330.
- Fold: III.F1's numeral eps_ind < 3e-6 (130-136, from N1STAR 10.34 (iv)) is superseded by VI.C row w1 (38):
  eps_ind <= delta_50 = 1.94137e-8 computed (`n1c/epsind5.py` E3); state the computed value here. III.F2 §5's open
  item (261-265) is closed by III.H C4.3 (S18): write a forward pointer.
- Depends on: S1-S3, S11-S14 (III.E Thm 1.1 (3) as (C1)-(C4)). MAIN: N1STAR 10.34 (iv).
- Programs: `n1/lgrade5.py`, `cpmodes5.py`, `sbar5.py`, `lin5.py`, `strap5.py`, `thresh5.py`, `damping5.py`,
  `linroots5.py`, `eind5.py`, `gmodes5.py`, `lhor5.py`, `zstates5.py`, `pairing5.py`, `static5.py`, `mp5.py`,
  `physical5.py`, `window5.py`; `n1c/epsind5.py`.
- Outside: [KI03] BB (master equations (5.3), (5.10), (5.15)); [Hin17] P4.1 identity; [AHW24], [Hin24b] replaced.
- Est.: 1,550 lines.

### S16. Future timelike infinity: the spectral family, the iota+-normal operator, grafting
- Source: III.G 15-931; III.G1 15-472; III.G2 12-387.
- Fold: none (III.J3 C3.2 later restates III.G2 C4.3 at the exact weight; keep that in S24). Depends on: S1-S3, S8,
  S11, S13, S15. Programs: `n1/sf5.py`, `iotasol5.py`, `sbar5.py`.
- Outside: [Vas13], [HV15], [Hin25a] replaced by S1-S3.
- Est.: 1,570 lines.

### S17. Null infinity, resonant states, and the transition face
- Source, in this order: III.C 10-495 (metric perturbations at infinity; the operator at null infinity; forward
  mapping); III.G3 10-407 (partially polyhomogeneous inputs, resonant states); III.G4 12-726 (tf-normal operator).
- Fold: III.C's forward statements about III.C1 (e.g. "the edge-b form is in III.C'", 8 cites) become pointers to S26.
- Depends on: S11, S15, S16. MAIN: N1STAR 10.38, 10.64 (values now proved here).
- Programs: `n1/ext5.py`, `sbar5.py`, `exterior5.py`, `scri5.py` (III.C, III.G3); `n1/tfgraft5.py` (III.G4).
- Outside: none beyond [Hin26] §§5.1-5.3, 9.1.3, 9.2 (written).
- Est.: 1,430 lines.

### S18. The augmented low-energy resolvent and 2-admissibility
- Source: III.H 13-554; III.H1 14-463. (III.H2 follows in S19: its setting uses III.I L5.1 and P3.4.)
- Fold: III.H C4.3-4.4 close III.F2 §5 (state it). Depends on: S1-S10, S15-S17.
- Programs: none. Outside: [SBG] (3.26); [Hin26c] L14.6 and the proofs of its Thms 12.2 (written).
- Est.: 890 lines.

### S19. Forward solutions in the cone, uniformly near b_0; null infinity; almost linear bounds
- Source, in this order: III.I 13-445 (setting, classes, structure, forward mapping, T5.3 at b_0); III.H2 14-339
  (strong trapping admissibility on B_1 (P1.1, C1.2), 2-admissibility for every k (T2.1), II.F Thm 8.1 and II.F1
  Thm 1.1 uniformly over 2L_b (T3.1, T4.1), C5.1 = III.I T5.3 near b_0); III.I(1) 9-239; III.I(2) 9-441.
- Fold: III.H2:222 supersedes III.H1 T1.3's restriction k <= K -- state T1.3 for every k (in S18) or here; III.I's
  restriction R5.4 and (I3) removed by III.H2 C5.1 (337).
- Depends on: S8-S10, S16-S18. Programs: `n1/lgrade5.py` (III.H2 127). MAIN: none.
- Est.: 1,260 lines.

### S20. The boost parameter, almost boundedness, and the extraction of parameters
- Source: III.I(3) 10-276; III.I(4) 12-407; III.I(5) 9-234; III.I(6) 9-333.
- Fold (if the chapter is written at general b, the recommended option; risk R1): III.I(15) §2.6 (375-455: L2.7 the
  boost identity at b with error E^S_b, P2.8 = III.I(4) P4.1 (2), C4.3 and III.I(5) C2.2 at b).
- Depends on: S16-S19. Programs: none.
- Est.: 1,070 lines (+80 with §2.6).

### S21. Undoing the parameter changes; centre-of-mass motions; corrections of the fourth kind
- Source: III.I(7) 12-455; III.I(8) 11-418; III.I(9) 11-408.
- Fold (general b): III.I(15) §2.8 (532-642: L2.11 the parameter identities at b with error E^mot_b, P2.12 = III.I(7)
  L4.3, L4.5, C4.6 and III.I(8) P4.1's base step at b). Note (1.1) of III.I(9) (32-48) defines eps_ind (cited by S27,
  VI.C row w1) and 72-74 (the gap (G)) is cited by the paper's Theorem 4.
- Depends on: S13 (III.D2-D3), S16, S17, S20. Programs: none.
- Est.: 1,100 lines (+110).

### S22. The expansion at the Kerr face (Theorem 11.59 of [Hin26] at n = 4)
- Source: III.I(10) 15-408; III.I(11) 14-525; III.I(12) 13-445; III.I(13) 16-187 (the two halves of Parts 1-3 refer
  to each other; keep them adjacent).
- Fold (general b): III.I(15) §2.7 (456-531: L2.9, C2.10 = III.I(12) L2.3-2.4 and T3.1 at a rotating b, with the
  rotation rows T_{v1,b} in place of the antiderivative). III.I(10) Def 1.3 is cited by the paper's Theorem 4.
- Depends on: S16-S18, S20-S21. Programs: none.
- Est.: 1,340 lines (+75).

### S23. Augmentation by the expansion's coefficients; efficient parameterisation
- Source: III.I(14) 12-458; III.J 12-376; III.J1 11-163.
- Fold: the deferral of [Hin26] C11.67 and Thm 12.8 for Psi "to after III.C'" (I15 30-31, 489-491; J 10, 408; J1 183):
  either drop (not used) or move to S26/S27. (G+) of III.J (34, 48-51, 56) is cited by VI.C and the paper.
- Depends on: S20-S22. Programs: none.
- Est.: 840 lines.

### S24. Tame estimates and exact weights
- Source: III.J2 15-344; III.J3 14-672.
- Fold: III.J2 (J''2) superseded by III.H2 P1.1 (I16:759; J3:355): drop (J''2)'s shrinking neighbourhood and cite
  S19; III.J2 table row for III.I(15) P2.5 (271) and III.J3 T5.3 at b (ledger batch 5) belong to S25 or are folded if
  S20-S23 are at general b. II.G Thm 2.1 (iii) as amended (J2:338) is S10's form.
- Depends on: S10, S11 (III.A P4.2), S16-S23. Programs: none.
- Est.: 870 lines.

### S25. Base points near b_0
- Purpose: the linear theory of S19-S24 at every base point b near b_0, uniformly: the model at b ((P1)-(P6)), joint
  injectivity by perturbation, v1 terms as rotation rows with assigned coefficients, III.I(14) T3.1 at b, and the list
  of forms in which each earlier statement holds at b.
- Source: III.I(15) 23-374 (§1 model, §2.1-2.5 rotation rows), 643-799 (§3 T3.1 and proof items (i)-(xi)), C3.2;
  §§2.6-2.8 (375-642) here only if S20-S22 stay at b_0. BASEPOINT-LEDGER 63-460: only the "supplied by" content,
  re-keyed from file:line to result numbers, as a table "result -- what supplies it at b -- uniform" (risk R1).
- Exclude: I16 4-21, 806-874; the ledger's paragraphs and categories.
- Depends on: S11-S24 (all of III). Programs: none.
- Est.: 700 lines with the re-keyed table (450 if §§2.6-2.8 are distributed and the table is reduced to the items
  (i)-(xi)).

### S26. The exterior region: estimates at null and spatial infinity, the exterior solution, polyhomogeneity, boosts
- Source, in this order: III.C1 10-86 (§1: L1.1 the exterior domain); IV 13-328 (edge-b calculus, energy estimates
  near scri+ and near I_0); IV(1) 13-210 (edge-b form with the constant matrix Abar; energy estimate for the system,
  tame); IV(2) 17-400 (integration along curves; Cauchy problem near I_0; T2.4 the linear exterior estimate; T3.1 the
  nonlinear exterior solution; C4.1 the cut-off gauge); III.C1 87-275 (§2: T2.1 = [Hin26] Thm 5.17 now proved by
  IV(2); §3: T3.1 polyhomogeneity); III.C2 9-230 (boosts T3.1, gauged data P4.1, P4.2).
- Fold: IV(1) (0.1) cites III.C1 T3.1 only for the admissible range l_I > 3/2 (IV(1) 25-26): state it as a parameter
  condition, not a dependence (risk R5); IV(2) 345 "as in III.K Lemma 3.1": cite II.G §3 Step 4 directly; III.C1:96
  (IV(2) T3.1, D309) in place. IV 23, IV(3)-related amendments in place.
- Depends on: S8 (II.F L1.3), S10 (II.G), S11, S15, S17. MAIN: N1STAR 10.64 X6 ("s = 3 serves at n = 4", IV:39) --
  a computed input; 10.57, 10.64 (pointers only).
- Programs: `n1/exterior5.py` X1-X3, X6, X8 (IV 352). Outside: [Hin23a] §3 written out; [Tay11] ch. 13 P3.6-3.7 BB
  (Moser estimates); [HV20] P4.3 replaced by IV P4.1; [COM81] proved via III.C1 T2.1.
- Est.: 1,240 lines.

### S27. The nonlinear stability theorem near Tangherlini, the parameters, and the symmetry class
- Purpose: [Hin26] Thm 13.1 at n = 4 (III.K T4.3) with every constant chosen consistently, and its G-invariant
  (O(4)) version.
- Source, in this order: III.K 14-69 (§0 setting); III.K 70-95 (L1.1) and P1.2's statement (96-134); IV(3) 17-159
  (the slab near scri+: T2.1-T2.2, C2.3); III.K 620-763 (L6.1 the radius near scri+ along past causal curves; L6.2
  P1.2's uniqueness near infinity), placed before P1.2's proof; III.K 135-212 (P1.2's proof); III.K 213-504 (§2 the
  map Psi, §3 Nash-Moser, §4 constraint propagation and T4.3); VI.C 16-100 (§§1-2: the table of conditions re-keyed
  to result numbers, T2.1 the order of choices); VII 31-68 (the group G = O(2) x O(2), its fixed spaces in R^4 and
  so(4); the data class (0.1) and the norm ||.||_{d_1}; L0.1 what lies in the class -- with mu_0 general, not
  mu_end); VII 271-424 (§3: the O(4) action, L3.1 naturality, P3.2 = T4.3 in the class); VII 427-437 and
  445-456 (the epsilon_m refinement of T4.3 via II.G's radius, and "the rate (0.2)": settling on compact sets at
  t_*^{-(alpha-2)+eps}) as a corollary.
- Fold: III.K brackets at 34, 57, 124, 151, 189, 194, 201, 327, 330, 412, 464, 466 (D304-D626: P1.2 (1) with h_0
  ending at Sigma_IVP on {r <= R_nu}; P4.2's compact sets from L6.1 (c); L2.3's level below the support; II.G Thm 2.1
  (iii) in its amended form); L6.2's brackets at 696, 698, 708, 720, 726, 754, 761 (D628-D629: the compact-set clause
  narrowed to the bound near infinity; dt past; the past-cone component); VII L3.1 (C3) as amended D608-D621 (277,
  285, 302-341: the 1-form towers of every type, V_1 by conjugation, conditions affine); VI.C row w1 (38: eps_ind <=
  delta_50 = 1.94137e-8) and row n1 (42: T4.3 at 471-477).
- Exclude: III.K 505-619, 764-774; VI.C 101-134 (keep one sentence of 128-134); VII 468-565.
- Depends on: S4-S10, S11, S14 (constraint damping), S19-S26; VI.C needs S12 (B_VI) and S14 (damping constants).
- Programs: `n1c/scrirad5.py` R1-R5 (L6.1-6.2: numerical confirmation of the radius bound and the future-curve case
  on g_{b0}); `n1c/vii5read.py` Q3 (delta* pointwise against (1/2) L_{w#} g; mathematical); `n1c/epsind5.py` E3;
  drop `vii5census.py`, `r0census5.py`, `gammac5.py`, `damping5.tsv` (censuses of the text).
- Outside: [Hin26] §13.1 (written); [Hin23a], [Hin24a] mentioned only.
- Est.: 950 lines.

### S28. Gluing to the Myers-Perry family, and gluing in the symmetry class
- Source: V 20-413 (KIDs, flux identity, charges without parity; the charge map near Tangherlini; T3.1 = [CD03] Thm 8.1
  at n = 4); VII 160-270 (§2: L2.1, P2.2 = [CD03] Thm 8.1 with G; C2.3 the data of (i)).
- Fold: V R3.4 (396-402) with its last two sentences replaced by the amendment 404-412 (only T3.1's proof in class form
  is used, with Tangherlini members on Sigma_IVP; Kerr-Schild slices' K differs by nabla^2 f + rho^4 C^infty; source
  `../GLUEDECAY5.md` R2.0, R3.0 and its L4.1, P4 -- MAIN); V 103, 291 (D315) in place. Mine VII's finding (VII6)
  (tail 525-528: the a priori bound |m - mu-bar| <= C eta; a bump of relative size R^-1 at radius R costs about
  R^(l_0-3) in the weighted norm) as a remark after P2.2; the paper and GLUEDECAY5 cite it.
- Depends on: S11 (III.B §3), S27 (the data class: III.K, VII L0.1). MAIN: N1STAR 10.47, 10.63, 10.66, 10.68
  (replaced); GLUEDECAY5 L4.1 (d), P4 for the amendment.
- Programs: `p5c/jac5.py` (225 entries of the charge Jacobian at large radius), `n1/general5.py` (V 423).
- Outside: [CD03] BB (Thms 3.6, 3.7, 3.9, 5.4, 5.6, 5.9, P5.10, C5.11, L3.18, T3.19, P G.1, App. E-F; pp. 4-78);
  [ER08] (34) replaced by V P2.3.
- Est.: 470 lines.

### S29. Linear stability of five-dimensional Tangherlini, and the comparison of gauges
- Source: VIII 6-353; IX 10-337.
- Fold: VIII 286 (Step 4's compact sets: II.F L1.4 (a) at theta = 0; for the perturbed metrics III.K L6.1; D378,
  D621); IX 52 (D610, D617: the comparison posed on the future half of a Cauchy development extending past
  Sigma_IVP), 348.
- Depends on: S8 (II.F §1.4, L1.3-1.4), S11, S26 (IV(1), IV(2), III.C2), S27 (III.K §0, P1.2; VII L3.1, P3.2, the
  epsilon_t choice and the rate argument). Not on S28.
- Programs: `n1c/scrirad5.py` (VIII 406), `n1c/ix5.py` X1-X8 (IX 193-386: pointwise identities, with controls).
- Outside: [BGP] BB (IX: Def 1.3.8 p.23, C1.3.12, T1.3.13 p.24, §1.5 p.33, C3.2.4 p.76, P3.2.5 p.81, T3.2.11
  pp.85-86, C A.5.4 p.174, L A.5.9 p.176); [See64] BB (Seeley extension); [KI03], [HKW18] mentioned only (VIII).
- Est.: 590 lines.

### S30. Assembly: settling of the high-frequency limit (the paper's Theorem 4)
- Source: VII 22-30 and 69-101 (§0: the main argument's coordinates, background and solution; T0.2 = Theorem 4;
  31-68 went to S27), VII 102-159 (§1: the
  solution after the shell, L1.1-1.2), VII 425-467 (§4 proof of T0.2: 427-444 choices and (i), 457-461 (ii), 462-467
  R4.1; 445-456 by S27's corollary).
- Fold: T0.2 with eps_t < eps_K (D326-D328, in place); Remark 4.1 kept; VII's finding (VII1) (tail 470-482: why
  (ii) takes the perturbation in the data class and not by gluing) as a remark, cited by GLUEDECAY5 and V's amendment.
- Depends on: S27, S28 and MAIN: the main argument's Theorem E/Theorem 1 (the solution g_lambda on Omega), its domain
  (1.1) and coordinates (§0.1), and BEYOND5/R0P (the lowered inner radius, re-proof of VII at r_flat, R0P §9).
- Programs: none of its own. Outside: [DS23] Thm 2.4 BB (L1.1's Step 8, VII:116); [CD03] via S28.
- Placement: this chapter is the bridge into the main argument; it may sit in the main body instead (risk R2).
- Est.: 170 lines.

Total estimated cleaned length: about 36,800 lines (S1-S30), against 39,927 body lines read.

## 4. Interfaces: what the rest of the paper uses from the stability theory

Consumers: the paper (`paper/RESPONSE-HL-5D.md`, tag P), `N1STAR-PROOF.md` (N), `GAUGEDECAY5.md` (GD),
`SETTLE-GLAM5.md` (SG), `GLUEDECAY5.md` (GL). Format: result @ line of its statement in the proof5 file [consumer and
count]. Theorems, propositions, corollaries, lemmas, definitions and sections were matched by label, by file name and
by GAUGEDECAY5's abbreviations (I2-I4, I8-I10, I15, K, J, J4, F2, C', C3, G, G2, H, H', IIC, VIA). The chapter is the
one of section 3 that will carry the result.

### 4.1 The headline results (what the main argument must be able to cite)
- Theorem 4 = VII T0.2 @69 (P 1239; GL, SG): S30. Its parts: VII L0.1 @56 (what lies in the data class; P 2528, GL 8,
  SG 5) -> S27; VII L2.1 (c) @168 (P 2536, GL 6) and P2.2 @192 (gluing in the class; P 1200, 1225; GL 10) -> S28;
  VII P3.2 @390 (III.K in the class; P 1200; SG 5) -> S27; VII L1.1 @104, L1.2 @140 (the solution after the shell;
  SG 8, 7) -> S30; VII §4's rate argument (SG, GL) -> S27 corollary.
- The nonlinear theorem: III.K T4.3 @471 (SG 13) -> S27; VI.C T2.1 @46, rows w1 (38), w2, n1 (42) and §3 @101 (P 1092,
  1104, 1244; SG) -> S27 (and S14 for the damping constants).
- The gap conditions in Theorem 4's statement: III.I(10) Def 1.3 @152 (P 1245) -> S22; III.I(9) 72-74, the gap (G)
  (P 1245) -> S21; III.J's (G+) (P 1245) -> S23.
- The linear statement: VIII T2.2 @211 (P 779, 3352; GD 6), C2.3 @321 (GD), L1.1 @66 (GD, SG 5) -> S29.
- The gauge comparison: IX T2.2 @223 (P 790, 3353), C2.3 @297 (GD 7), L1.1 @116 (GD 10), L1.2 @144, L2.1 @190
  (a), (b), (f), R2.4 @323, §0 @23 -> S29. N 1960-2034, 2243, 3393 use VIII and IX as a whole.
- The low-energy hypotheses of I.C (N 2239: "Part I.C's low-energy hypotheses hold there") -> S3: (H1)-(H4), (G),
  (Z_P), (TF) of I.C §1.2 and Def 5.1.
- Gluing: V T3.1 @268 (P 1225 via VII P2.2), V Def 2.1 @138, L2.2 @154, P2.3 @168 (the charge map), L1.2 @66, P1.3
  @97, L1.4 @124, L3.3 @376, and Steps 1, 3, 5 of T3.1's proof (GL) -> S28. Note GL also cites VII's finding (VII6)
  (VII 525-528, "a bump of relative size R^-1 at radius R costs about R^(l_0-3)") and (VII1) (VII 470-482): fold both
  as remarks (S28, S30); they sit in the dropped tail (risk R7).
- The parameter census of the write-out (P 1450-1452 cites `proof5/checks/gammac5.py`, `admiss5.py` and
  BASEPOINT-LEDGER.md as evidence): no mathematical result; see risks R1, R6.

### 4.2 Everything else GAUGEDECAY5, SETTLE-GLAM5 and GLUEDECAY5 cite, by chapter
GAUGEDECAY5 re-enters the machinery (the Box operator on 1-forms at zero energy, the forward problem, the iota+ step),
so it cites many lemmas. Besides the list below it cites the parts about 300 times by file:line ("I3:115-131",
"IX:253-277", "G2:917-950", "VIII:144-147", "I10:195-206", "K:42-47", "I4:209-241", "F2:65-80", ...); those must be
re-keyed to result numbers of these chapters when GAUGEDECAY5 is edited (risk R9).
- S1: I.A L2.4@310 [GD1]; I.A §6@1280 [GD1]; I.A L7.1@1465 [GD1]; I.A T7.2@1500 [GD3]
- S2: I.B T1.3@190 [GD2]
- S3: I.C Def1.1@63 [GD1]; I.C L2.2@154 [GD3]; I.C §2.3@207 [GD1]; I.C L2.4@250 [GD3]; I.C T3.1@376 [GD3]; I.C §3.1@402
  [GD1]; I.C §4.1@506 [GD1]; I.C §4.3@578 [GD1]; I.C T4.3@596 [GD3]; I.C Def5.1@708 [GD3]; I.C L5.4@765 [GD4]; I.C
  L5.5@790 [GD1]; I.C L5.6@811 [GD1]; I.C P5.3@822 [GD5]; I.C T6.4@1105 [GD5]; I.C C6.6@1356 [GD1]
- S5: II.C Def2.4@243 [GD2]; II.C Def2.7@337 [GD6]; II.C L3.2@380 [GD1]; II.C P5.1@581 [GD1]
- S7: II.E P3.4@648 [GD4]
- S8: II.F L1.3@234 [GD3]
- S9: II.F1 T1.1@65 [GD13]
- S10: II.G1 Def2.1@79 [GD1]; II.G1 Def2.7@233 [GD3]; II.G1 P2.8@246 [GD3]; II.G1 §3.1@313 [GD1]; II.G1 P3.3@422 [GD8];
  II.G1 P3.5@526 [GD3]; II.G1 L4.1@627 [GD1]; II.G1 C4.5@830 [GD2]; II.G1 L4.6@877 [GD1]; II.G1 P4.7@917 [GD4]
- S11: III.A L1.2@73 [GD1 SG2]; III.A L1.3@109 [SG2]; III.A §1.1@140 [GL2]; III.A L3.2@387 [GD2 SG4]; III.A1 L1.4@132
  [GD1]; III.A1 L1.6@210 [GD2]; III.B L3.5@172 [GD1 GL1]; III.B L3.7@228 [GD2]; III.B L3.9@267 [GD1]; III.B §4@291 [GD1];
  III.B L4.1@297 [GD1]; III.B §5@336 [GD1]; III.B Def6.1@430 [GD1]
- S12: VI.A T6.1@303 [GD17]
- S13: III.D L2.1@54 [GD2]; III.D L3.1@125 [GD1]; III.D L4.1@176 [GD1]; III.D L5.1@249 [GD2]; III.D L5.2@289 [GD3]; III.D
  §6@320 [GD2]; III.D P6.1@322 [GD2]; III.D P6.2@360 [GD5]; III.D L7.1@439 [GD3]; III.D1 §1@22 [GD6]; III.D1 L2.1@82
  [GD21]; III.D1 L3.1@171 [GD2]; III.D1 P4.1@198 [GD2]
- S14: III.E T1.1@37 [SG2]
- S15: III.F P4.1@141 [GD1]
- S17: III.C Def3.1@149 [GD1 SG8]; III.C L3.2@189 [SG1]; III.C L3.5@246 [GD1]; III.C L4.2@293 [GD1]
- S18: III.H §1@25 [GD1]; III.H L2.2@83 [GD1]; III.H L2.3@115 [GD1]; III.H L2.4@143 [GD2]; III.H L2.5@219 [GD4]; III.H
  P3.2@304 [GD3]; III.H T4.1@342 [GD9]; III.H C4.2@443 [GD2]; III.H C4.3@466 [GD1]; III.H1 Def1.1@54 [GD1]; III.H1
  T1.3@121 [GD1]; III.H1 L2.1@147 [GD1]; III.H1 L4.2@277 [GD1]; III.H1 §5@283 [GD1]; III.H1 L5.1@295 [GD2]
- S19: III.I L5.1@338 [GD4]; III.I T5.3@394 [GD1]; III.I1 L1.1@33 [GD1]; III.I1 P2.1@59 [GD1]; III.I1 L2.2@72 [GD1];
  III.I1 P3.1@165 [GD3]; III.I2 L3.1@115 [GD2]; III.I2 L4.1@216 [GD4]; III.I2 L4.2@244 [GD9]; III.I2 L4.3@271 [GD1];
  III.I2 P5.1@309 [GD4]
- S20: III.I3 L1.1@35 [GD1]; III.I3 L1.2@61 [GD1]; III.I3 L1.3@98 [GD1]; III.I3 P2.1@120 [GD5]
- S23: III.I14 L2.2@145 [GD1]
- S24: III.J3 P5.4@593 [GD1]
- S26: III.C1 T3.1@133 [GD3 SG3]; III.C2 T3.1@91 [SG3]; III.C2 P4.1@162 [SG3]; IV R1.3@? [GD1]; IV P3.1@196 [GD1]; IV
  P4.1@277 [GD1]; IV1 L1.1@34 [GD1]; IV1 L2.1@117 [GD1]; IV1 P2.2@128 [GD3]; IV2 L2.2@160 [GD3]; IV2 L2.3@202 [GD1]; IV2
  T2.4@229 [GD8]
- S27: III.K §0@21 [GD3]; III.K L1.1@72 [GD3]; III.K T4.3@471 [SG13]; IV3 L0.1@39 [GD1]; IV3 L1.1@58 [GD1]; IV3 T2.1@86
  [GD3]; IV3 C2.3@148 [GD1]; VI.C T2.1@46 [SG1]; VI.C §3@101 [P1]; VII L0.1@56 [GL8 P1 SG5]; VII P3.2@390 [SG5]; VII
  §4@425 [GL1 SG1]
- S28: V L1.2@66 [GL1]; V P1.3@97 [GL1]; V L1.4@124 [GL1]; V Def2.1@138 [GL2]; V L2.2@154 [GL1]; V P2.3@168 [GL3]; V
  L3.3@376 [GL1]; VII §2@160 [GL1]; VII L2.1@168 [GL8 P1 SG1]; VII P2.2@192 [GL10 P2]
- S29: IX §0@23 [GD4]; IX L1.1@116 [GD10]; IX L1.2@144 [GD3]; IX L2.1@190 [GD7]; IX T2.2@223 [GD2 P2]; IX C2.3@297 [GD7];
  VIII L1.1@66 [GD1 SG5]; VIII T2.2@211 [GD6 P2]; VIII C2.3@321 [GD1]
- S30: VII §0@22 [GD1]; VII T0.2@69 [GL4 P1 SG2]; VII L1.1@104 [SG8]; VII L1.2@140 [SG7]; VII §5@468 [GL5]

## 5. Risks

**R1. The theory at base points b != b_0 is spread over 17 files and a reading census.** III.I(1)-(14) and
III.J-III.J3 are written at b_0. III.I(15) T3.1 (I16:645-799) says they hold at every b near b_0 "in the following
forms", repairs four of them (§§2.6-2.8: III.I(4) L2.4, P4.1 (2), C4.3; III.I(5) C2.2; III.I(7) L2.4, L4.3, L4.5,
C4.6; III.I(8) P4.1's base step; III.I(12) L2.3-2.4 and T3.1; III.J3 T5.3 at b), and rests its completeness on
BASEPOINT-LEDGER.md (I16:692: "every use ... is a row of the ledger"; 324 rows keyed by file:line, read by five
readers). A reading census is not a proof a reader can check. Two options: (a) recommended: write S20-S24 at a general
b near b_0 from the start, folding III.I(15) §§1-2 (P1)-(P6), L1.2, P2.2, P2.5 and §§2.6-2.8 into the chapters they
repair, so that S25 shrinks to the uniformity statement; (b) keep S25 and reproduce the ledger's "supplied by" column
re-keyed to result numbers (about 324 entries, of which categories c, d, g need an argument each). Either way III.J2's
table row (J3:271) and III.H2 P1.1 superseding (J''2) (I16:759, J3:355) must be folded.

**R2. Part VII mixes the stability theory with the main argument.** VII §0 works in the main argument's coordinates,
with its Vaidya background and Theorem E; §1 is about its solution after the shell; §§2-3 and the rate argument of §4
are pure stability theory and are used by VIII, IX, GLUEDECAY5 and SETTLE-GLAM5. The plan splits VII over S27 (31-68,
271-424, 427-437, 445-456), S28 (160-270) and S30 (the rest). S30 needs the main argument's Theorem 1/Theorem E and
domain before it; it may belong in the main body.

**R3. The inner radius.** BEYOND5-R0-PROOF.md (main argument, outside proof5) re-reads every part with the inner radius
lowered to r_flat in (0, R_1/2] (the paper's "beyond the boundary", RESPONSE-HL-5D.md 1748-1757), and its §0 found and
repaired a mismatch (Part I's artificial boundary at 5R_1/8 against III.B's R_1/2; repaired in VI.A as D373, finding
(VI.A7) in the dropped tail VI.A 339-351). Recommended: state the inner radius as a parameter in S11/S12 (r_0 := r_flat,
delta_0 := min(R_1/16, r_flat/4), collar to r_flat - 2 delta_0, r_2 := 7R_1/8, r_e := 17R_1/16) and write every
chapter for it; then R0P is absorbed. If the edition keeps r_0 = R_1/2, its Theorem 4 does not cover the lowered
boundary that the paper's later section uses (status there: deduced).

**R4. The forward problem's compact sets and the nonlinear initial family: final form spread over five places.**
III.K P1.2, L2.3, P4.2 (body, with brackets D304-D626 at 124-466), III.K L6.1-6.2 (620-763, with brackets D626-D629;
L6.2's compact-set clause withdrawn at 761 -- use only the bound near infinity), II.F L1.3-L1.4 (the inputs named at
D378, D621), VIII Step 4 (286), IX (52, D610). Writers must treat each bracket as replacing the sentence it follows
(several brackets say "as written this cannot work" or "withdrawn"), and must take L1.4 (a) at theta = 0 from II.F.

**R5. Statements proved after their first use.** III.E T1.1 is stated in III.E and proved in IV(4)-IV(6); III.C1 T2.1
is stated in III.C1 and proved by IV(2); IV(4) and IV(5) use each other (IV(5) uses IV(4) §§0-1, IV(4) §2 uses IV(5)
T7.3); III.K P1.2's proof poses the slab that IV(3) solves, and its uniqueness uses L6.2, which uses IV(3) C2.3 and
III.C2; IV(1) (0.1) cites III.C1 T3.1 for the range l_I > 3/2; III.I(10)-(11) refer to each other. The reading orders
of S14, S26 and S27 resolve these; no genuine circle was found, but each writer must check the order inside a chapter.

**R6. Arguments about the text instead of the mathematics.** II.F1 L2.1 (b) (admiss5.py: Definition 3.3 (3) unused in
104 lines of II.C-II.E), VI.C §3 (gammac5.py: every line naming gamma_C, s_C or III.E T1.1; damping5.tsv),
VII (VII5) and §6 (vii5census.py, vii5read.py Q1-Q2, Q4: 713 uses of the 1-form towers, supporting L3.1's
naturality), III.K/VII's re-keyed censuses (r0census5.py), and the ledger (R1). The paper cites two of them
(RESPONSE-HL-5D.md 1450-1452, 2956). They cannot be published as computations. Replace by: the damping constants fixed
once in S14; L2.1 (b) with an explicit hypothesis; a structural proof that every choice in L3.1 (C1)-(C4) is natural
(the claim at VII 521-523, "every other ingredient is natural or the unique solution of a natural problem", needs to be
argued, not counted). Only vii5read.py Q3 (delta* checked pointwise) is a mathematical computation.

**R7. Mathematics that lives only in dropped tails.** Consumers cite VII (VII1) 470-482 and (VII6) 525-528; II.G
(H10) 506-511 justifies Thm 2.1 (iii); several statements were changed by findings whose reason is only in the tail
(I.B: gamma_pm as the exact thresholds and gamma_- < 0 assumed, tail 2056-2120; I.C (F6): Cor 9.43 needs the adjoint
estimate; II.A (G3): tame estimates per representation, (G6)-(G7): hypotheses of the propagation estimate; II.C1
(C'2): the stable hypersurface in C^(d0-2); II.D (D2)-(D3); V (V1), (V3): no parity at n = 4, [CD03]'s indices at
n = 4). The plan folds the cited ones and suggests one "Remarks on the sources" paragraph per chapter for the rest.

**R8. Programs.** Cited but absent from the repository: `checks_c.py` (I.C 455, 779, 830), `d215/chk3b.py`,
`chkric.py`, `chkboost.py` (III.B 107-558). About 40 programs are in `n1star/` (root), 6 in `n1star/checks/`, and only
7 (+3 tables) in `proof5/checks/` (Appendix B); the brief's "checks/*.py" covers the last group only. Every *computed*
step (e.g. III.A1's harmonic lists, III.F2's potentials, VI.B1's trapping, IV(4)'s thresholds) becomes a C_k and needs
its code in the appendix.

**R9. Line-keyed citations.** GAUGEDECAY5 cites the parts about 300 times by file:line; SETTLE-GLAM5 cites
`proof5/README.md:77-84` and PART-IV3-NM.md, PART-IV4-SLAB.md lines; the paper cites PART-III-I10-CORR4.md:72-74; VI.C's
whole table (25-42) and VII's L3.1 (C1)-(C3) list (284-312) are keyed by file:line; VII and VIII cite
PART-III-I15-AUGMENT5.md:61-65. All must be re-keyed to the edition's numbering; the README line pointers die with the
README.

**R10. Status lines disagree in form, not in verdict.** Every part ends "proved". But: III.K's own status (3-12) stops at
D312 while the README row lists amendments D378-D629 that were "read" (not re-proved); II.F1 is "amended (D327)" after
"proved (D216)"; II.G "proved (D216); amended D304", read only at D621; VI.C and VII were amended after "proved"
(D390, D608-D628) and the amendments "read, holds"; VI.A/VI.B/VI.B1 "amended (D373)" in a file outside proof5; II.A's
status opens "Written out in full (D192)" and closes "proved (D197)"; many say "status synchronised with the README at
D325". The edition states no statuses, so this matters only for choosing the authoritative text: always the amended one.

**R11. Inputs from the main argument inside the stability proofs.** The parts use computed items of N1STAR as
hypotheses: 10.12-10.22 (gauge potential and constraint damping operators: modes, thresholds), 10.28-10.31 (zero energy
states), 10.34 (iv) (eps_ind, superseded by VI.C w1's 1.94137e-8 from n1c/epsind5.py), 10.35, 10.38, 10.47, 10.52,
10.54, 10.64 (X6: "s = 3 serves at n = 4", IV:39), 10.65 (a) ([Hin26d] reading), 10.79 (horizon thresholds), and
Props 10.14 (ii), 10.16 (ii), (iv) (VI.A). Unless those computations are described before the stability part, the
part is not self-contained: list them as computations C_k in S12-S15 and S26, or order the main argument's chapters
that prove them first.

**R12. Black boxes.** Every "proved" status rests on outside results cited with theorem and page, valid in every
dimension: [HJS] (scattering calculus, S1-S3), [SBG] (eleven statements, S4), [0C] (S8), [BGP] (S8, S29), [CD03]
(Thms 3.6-5.11, App. E-G, S28), [Mel93] Thm 6.5 (S14), [Tay11] ch. 13 (S26), [DLMF], [RS1] (S3), [KI03] (master
equations, S15), [ER08]/[MP86] (formulas, S11-S12), [See64], [DS23], [Hin26a] P5.1, [Hin26d] (S14). None needs
reproduction, but two need care: [CD03]'s dimension-dependent indices, which V corrects at n = 4 (tail (V3)); and
[Hin26a] P5.1 and [Hin26d], cited as READ without proof in IV(5). [Hin26c], [Hin26], [Hin23a], [Hin26a] are written out
(the edition must say so: "we follow [Hin26, §11] and write out the changes at n = 4"). [AHW24] is not used (replaced).

**R13. Size.** About 36,800 cleaned lines in 30 chapters; S4 (2,219 source lines), S2 (2,030) and S1 (1,860) are the
largest. If a writer's limit is tighter, S4 splits after II.A §8 and S8 after II.F §3.

## Appendix A. In-body lines to edit (file, kept body, count, line ranges)

These lines inside the kept ranges carry a D-label, a verifier or reader attribution, a pointer to "the record",
N1STAR or a BEYOND5/GLUEDECAY5/GAUGEDECAY5 file, a READ/computed/deduced label, a program or table name, or a PART file
name. Edit the clause; keep the mathematics.
- I-SPECTRAL (body 30-1889; 40): 51, 99, 134-135, 184-185, 198, 244, 263, 355, 405, 412, 457, 507, 532, 577, 594, 655,
  708, 745, 816, 879, 916, 1062, 1068, 1085, 1198, 1208, 1235, 1255, 1390-1391, 1417, 1607, 1655, 1836, 1844, 1865, 1882,
  1887
- I-B-HIGHENERGY (body 26-2055; 26): 139, 165, 167, 171, 220, 239, 924, 1288-1289, 1293, 1346, 1424, 1438, 1459-1460,
  1546, 1548, 1732-1733, 1840, 1876-1877, 2018, 2052-2054
- I-C-LOWENERGY (body 32-1434; 18): 84-85, 110, 306, 318, 455, 625, 634, 756, 767, 779, 830, 835, 845, 874, 949, 1280,
  1433
- II-A-SETUP (body 36-1497; 11): 343, 345, 408, 411, 508, 518, 757, 953, 1127, 1132, 1470
- II-A2-STANDARD (body 29-785; 17): 36, 53, 55, 76-77, 80, 168, 296, 319, 322-323, 422, 527, 533, 632, 742, 774
- II-B-DYNAMICS (body 30-694; 4): 70, 236, 349-350
- II-C-OPERATORS (body 30-795; 10): 106, 113, 126, 212, 456, 566, 615, 690, 694, 700
- II-C2-TRAPPING (body 32-400; 13): 90, 113, 160, 170, 183, 199, 248, 277, 299, 301, 353, 382, 399
- II-D-REGULARITY (body 37-1042; 8): 332-333, 528, 551, 579, 887-888, 892
- II-D2-BREGULARITY (body 32-611; 4): 90, 132, 410, 605
- II-E-ENERGY (body 37-1206; 4): 173, 502, 637, 709
- II-F-IOTA (body 39-2619; 15): 240, 319-320, 462, 1380, 1529, 1677-1678, 1702, 1716, 1792, 1903, 1998, 2052, 2505
- II-F2-TAME (body 33-746; 6): 76, 174, 177, 179, 668, 670
- II-G-NASHMOSER (body 28-453; 4): 78-79, 91, 336
- II-G2-DECAY (body 31-1198; 2): 982, 1015
- III-A-PREREQ (body 23-723; 14): 131, 137-138, 192-193, 243, 394, 440, 481, 522, 587, 662-663, 697
- III-A2-HARMONICS (body 22-481; 8): 121, 129, 263, 368, 388, 435, 447, 478
- III-B-FAMILY (body 26-509; 9): 107, 121, 134, 145, 149, 154, 187, 397, 474
- III-C-EXTERIOR (body 28-495; 16): 70, 87, 163, 186, 224, 259, 290, 307, 310-311, 314, 401-402, 427, 472, 494
- III-C2-POLYHOM (body 28-275; 5): 83, 96, 117-118, 125
- III-C3-BOOSTDATA (body 27-230; 3): 89, 95, 124
- III-D-GAUGEPOT (body 26-466; 10): 43, 162, 164, 199, 230, 241, 245, 277, 312, 337
- III-D2-ZEROENERGY (body 22-339; 6): 43, 79, 103, 118, 139, 193
- III-D3-SYMSTATES (body 20-287; 5): 44, 141, 256, 264, 280
- III-D4-GENSTATES (body 18-265; 17): 45, 61-64, 70, 72, 179, 181, 193, 200, 220, 229, 245, 248, 258-259
- III-E-CONSTRAINT (body 18-211; 10): 54-56, 63, 66-67, 103, 116, 123, 169
- III-E2-V1STATES (body 18-216; 6): 79, 81, 96, 147, 154, 213
- III-F-LINEARISED (body 17-215; 6): 110, 124-125, 129, 163, 193
- III-F2-INDICIAL (body 14-492; 10): 53-57, 75, 101, 134-135, 261
- III-F3-MODES (body 17-270; 14): 37, 116, 118-119, 127, 131, 138, 145, 147, 160-161, 166, 198, 268
- III-F4-ZERO (body 17-457; 8): 28, 58, 134, 136, 183-184, 227, 257
- III-F5-PAIRINGS (body 16-330; 8): 134, 169, 187, 194, 247, 315, 319, 321
- III-G-SPECTRAL (body 42-931; 17): 73, 126-127, 204, 245, 252, 271, 502, 525, 532, 609, 641-642, 660, 662, 695-696
- III-G2-IOTA (body 15-472; 9): 30, 66, 175, 208, 229, 376, 406, 411, 464
- III-G3-GRAFT (body 27-387; 2): 37, 378
- III-G4-RESONANT (body 22-407; 4): 74-76, 160
- III-G5-TF (body 24-726; 14): 79, 122, 153, 190-191, 194, 260-261, 306, 446, 462, 513-514, 685
- III-H2-ADMISS (body 26-463; 3): 92, 222-223
- III-H3-UNIFORM (body 27-339; 17): 35, 43, 48, 58, 61, 65-67, 71, 127, 207, 210, 251, 253, 275, 277, 302
- III-J-PARAM (body 31-376; 1): 158
- III-J3-TAME (body 27-344; 5): 271, 326, 338, 341-342
- III-J4-EXACT (body 40-672; 8): 97, 460, 464, 475, 482, 657, 663, 669
- III-K-NONLINEAR (body 21-504; 28): 30, 33-34, 57, 68, 107, 115, 124, 139, 145, 151-152, 165, 189, 194, 201, 236, 238,
  269, 327, 329-330, 337, 383-384, 412, 464, 466
- IV-EB (body 13-328; 2): 39, 325
- IV2-TAME (body 13-210; 3): 16, 23, 208
- IV3-NM (body 17-400; 7): 54, 162, 199, 204, 234, 328, 387
- IV4-SLAB (body 17-159; 2): 75, 103
- IV5-CDMODES (body 17-232; 20): 34, 40, 49, 63, 82, 91, 101, 103, 105, 108, 111, 113, 122, 131, 136, 185, 187-188, 194,
  225
- IV6-SOLV (body 19-843; 11): 75, 126, 160, 195, 417, 442, 679, 736, 760, 811, 819
- IV7-TFACE (body 24-427; 11): 63, 65, 155, 169, 172, 192, 251, 253, 274, 304, 323
- V-GLUING (body 20-413; 13): 103, 175, 279, 291, 301, 310, 319, 395, 404, 406, 409-410, 412
- VI-DYN (body 19-309; 3): 84, 164, 294
- VI2-HORIZON (body 14-137; 1): 34
- VI3-TRAPPING (body 22-475; 2): 81, 125
- VI4-PARAMS (body 16-134; 37): 19, 25-42, 59, 70, 74, 80, 84, 104-106, 108, 113, 116-118, 123, 126-127, 131-132
- VII-ASSEMBLY (body 22-467; 70): 24, 33, 44, 49, 51, 70, 72, 84-85, 91, 102, 104, 115, 119, 121, 125, 135, 138, 141,
  157, 277-278, 284-285, 287, 292-293, 295-296, 300, 302-305, 307-312, 316-317, 319, 322-324, 328, 334, 340-341, 343-344,
  346-347, 349, 359, 363, 367, 369, 372-373, 375, 385, 414, 429, 432, 447, 449, 462, 466
- VIII-LINEAR (body 24-353; 20): 29, 57, 90, 98, 116, 164, 166, 168, 172, 199, 259, 261-262, 286, 292, 303, 306, 311,
  313, 352
- IX-GAUGE (body 23-337; 14): 51-52, 57, 88, 131, 193, 198, 204, 208, 214, 221, 281, 311, 336
- III-I-CONE (body 22-445; 5): 63, 139, 228, 315, 352
- III-I11-SPACETIME (body 28-408; 1): 142
- III-I15-AUGMENT5 (body 34-458; 1): 36
- III-I16-BASEPOINTS (body 35-805; 100): 40, 42-43, 54-55, 58-60, 62, 66, 69, 71-72, 81, 97-99, 104, 109-111, 114, 133,
  136-140, 165, 167, 200, 242, 245, 274, 329-330, 336-337, 355, 357, 364, 380, 408, 434, 447, 454, 460, 503, 527, 539,
  590, 599-600, 604, 606-607, 640, 650, 652, 657, 661, 663, 665, 669, 671, 678, 680, 683, 688, 690-692, 696, 705,
  714-715, 719, 724, 734-735, 740-741, 743-744, 753, 762, 767-768, 770, 773-774, 776, 779, 782, 785, 787-788, 795-796,
  798
- No tagged lines: III-H-AUGMENT, III-J2-LINEAR, III-I2-SCRI, III-I3-ALMOST, III-I4-BOOST, III-I5-UNBOOST,
  III-I6-ALMOSTBDD, III-I7-PARAMS, III-I8-UNPARAM, III-I9-COMMOTION, III-I10-CORR4, III-I12-SPECTRAL, III-I13-EXPANSION,
  III-I14-LEVELS.

## Appendix B. Programs the stability theory cites (for the code appendix)

Kind: M = a mathematical computation (becomes a numbered computation C_k); T = a check of the document's own text
(census or enumeration; not publishable as a computation, see R6).

`proof5/checks/` (7 programs, 3 tables):
- `dyn5.py` M -- VI.A 164, 294 (S12). `horizon5.py` M -- VI.B 34 (S12). `trap5.py` M -- VI.B1 14, 81, 125 (S12).
- `jac5.py` M -- V 427: the 225 entries of the charge Jacobian at large radius (S28).
- `admiss5.py` + `admiss5.tsv` T -- II.F1 177 (S9). `gammac5.py` + `gammac5.tsv` T, `damping5.tsv` T -- VI.C 113-118
  (S27); the paper cites gammac5.py and admiss5.py (RESPONSE-HL-5D.md 1450, 2956).

`n1star/checks/` (6):
- `scrirad5.py` M -- III.K L6.1-6.2 (R1-R5, 595-772), VIII 406 (S27, S29). `ix5.py` M -- IX X1-X8 (S29).
- `epsind5.py` M -- VI.C row w1, E3: eps_ind <= delta_50 = 1.94137e-8 (S15, S27).
- `vii5read.py` M (Q3: delta* pointwise) and T (Q1-Q2, Q4) -- VII 324, 344 (S27).
- `vii5census.py` T, `r0census5.py` T -- III.K 589-617, VII 509-561 (dropped).

`n1star/` root (40), all M, by chapter:
- S1 `hthresh5.py` (I.A 708; also IV(4) 131). S8-S9 `iplusnorm5.py` N1-N9 (II.F).
- S11 `harm5.py`, `lin5.py` (III.A1). S13 `harm5.py`, `trap5.py`, `modes5.py`, `lin5.py`, `hienergy5.py`, `thresh5.py`
  (III.D); `modes5.py`, `gaugepot5.py` (III.D1); `zstates5.py`, `genstates5.py` (III.D2); `genstates5.py`, `lin5.py`,
  `puregauge5.py` (III.D3).
- S14 `cpmodes5.py`, `damping5.py`, `dual5.py` (III.E); `mp5.py`, `dualv1_5.py` (III.E1); `cpmodes5.py`,
  `hthresh5.py`, `cform5.py`, `uniform5.py`, `solv5.py`, `semiclass5.py` (IV(4)); `cpmodes5.py`, `cform5.py`,
  `tface5.py`, `gaugepot5.py` (IV(6)). S12 also `cform5.py` (VI.A 347).
- S15 `lgrade5.py`, `cpmodes5.py`, `sbar5.py`, `lin5.py`, `strap5.py`, `thresh5.py` (III.F); `damping5.py`, `lin5.py`,
  `linroots5.py`, `eind5.py` (III.F1); `gmodes5.py`, `lhor5.py` (III.F2); `zstates5.py`, `gmodes5.py`, `pairing5.py`,
  `static5.py`, `mp5.py` (III.F3); `pairing5.py`, `physical5.py`, `window5.py` (III.F4).
- S16 `sf5.py`, `iotasol5.py` (III.G); `sbar5.py`, `sf5.py` (III.G1). S17 `ext5.py`, `sbar5.py`, `exterior5.py`,
  `scri5.py` (III.C); `ext5.py`, `scri5.py` (III.G3); `tfgraft5.py` (III.G4). S19 `lgrade5.py` (III.H2 127).
- S26 `exterior5.py` X1-X3, X6, X8 (IV 352). S28 `general5.py` (V 423).
- Note: `trap5.py` and `uniform5.py` exist both in `n1star/` and in a checks directory (`proof5/checks/trap5.py`,
  `n1star/checks/uniform5.py`); III.D and IV(4) cite them without a directory -- confirm which one.

MISSING (cited, in no directory of the repository): `checks_c.py` (I.C 455, 779, 830; S3), `d215/chk3b.py` (III.B
107, 134, 187, 558), `d215/chkric.py` (III.B 154, 558), `d215/chkboost.py` (III.B 397, 558) (S11).
