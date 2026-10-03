# DOCKET 68 · B-combine: the seven hypotheses in combination

**Status: a docket work item, wave 2 (repaired 2026-10-03 after three adversarial verifications). Nothing here is
seated.** The instrument is `combine.py`, beside this file. `python3 combine.py --selftest` runs **65 checks and
passes all 65** in about 95 s (z3, numpy, sympy; the screen runs in four worker processes). Eleven of the checks are
controls. One guard cannot fail by construction and is **reported as STRUCTURAL, not counted** (section 2).

*Wave 1 first said:* "80 checks and passes all 80". Several of those 80 could not fail (section 0, AGAINST #2, #3, #4);
they are gone or relabelled, which is why the count fell.

`combine.py` imports what it uses and copies nothing: `settle.py`, `frame.py`, `measure.py`, `geometry.py` (the four
work items, wave 2); `nlcontrol.py`, `corridors.py`, `nosig.py` through them; `../transit.py`, `../emtension.py`, and
`../LEDGER.md` (read, never written). It writes nothing outside `docket68/` except output paths the caller names.

M's standing instruction, verbatim from the charter: *"Remember that some of the hypothesies lined up for docket 68
may turn out, after initial testing, to work better in combination."* M's hypotheses are carried as hypotheses. Each
grade says what a combination does, not whether it is true.

## 0. Wave-2 repair: every verifier problem sited here, and what was done

**The principle the repair runs on, stated once.** *A theorem that does not bind a non-geometric corridor makes the
obstruction NOT-BOUND-IF (its premise named), never REMOVED. Showing a theorem does not apply is not showing its
conclusion false.* It is applied symmetrically:

- to **O-MAKE-TOPO** (Geroch/Tipler bind a corridor made by a classical Lorentzian topology change);
- to **O-HOLD's geometric form** (Morris-Thorne binds a geometric throat);
- under **ITB** (premise N_QTOPO), under **ITE** (premise N_MS17, for O-MAKE-TOPO only; MS fn.1 assumes the bridge's
  throat), and under **R-INDEX with H-IT** (premise N_MEASPHYS). A3's only-if direction is kept: R-INDEX without H-IT
  releases nothing.

**NOT-BOUND-IF is a verdict of its own**, distinct from REMOVED and REMOVED-IF. A not-bound obstruction is not
removed. What the non-geometric corridor costs to make or hold is a separate question, and it is carried beside the
verdict as the removal's own status. For ITB that status is **OPEN via N_ILFREE**: "the information layer charges
nothing", which no source supplies. When an AGAINST finding (the removal rests on an out-of-scope argument) and a FOR
finding (the encoding treats H-IT unevenly) pulled opposite ways, both were resolved by this one rule. B-THROAT and
B-TOPO now have the same form, and neither yields a removal.

| verifier problem (site) | resolution |
|---|---|
| AGAINST #0 (B-THROAT made H-IT sufficient; O-HOLD "REMOVED" on ITB+RI) | **Applied.** B-THROAT is re-encoded: the throat fails to be geometric only under ITB+N_QTOPO or ITB+RI+N_MEASPHYS, and DEF-HOLD no longer counts "no throat" as removal. O-HOLD is **never REMOVED** in any consistent variant. Under ITB+RI it is NOT-BOUND-IF with two supports, {ITB, N_QTOPO} and {ITB, RI, N_MEASPHYS}. The wave-1 encoding is kept as a mutated-encoding control (`wave1-THROAT`), and the drift guard catches it disagreeing with A3 and A4 (123/134 agree under the mutation). |
| FOR #1 (asymmetric B-THROAT vs B-TOPO) | **Applied, symmetrically.** ITB alone: O-MAKE-TOPO and O-HOLD are both NOT-BOUND-IF {N_QTOPO}, with the removal OPEN via N_ILFREE. R-INDEX adds an alternative support. It is not needed. The 192-variant "synergy" of wave 1 is gone. FOR #1's caution holds: ITB+RQ is a **premise clash** on N_QTOPO (512 variants), not a removal. |
| AGAINST #11 (O-MAKE-TOPO removal rests on an out-of-scope argument) | **Applied.** It is NOT-BOUND-IF {N_QTOPO} under ITB (no READ source) and NOT-BOUND-IF {N_MS17} under ITE. N_MS17 is MS p.17, READ, and covers a non-traversable bridge only. The verdict is never REMOVED. |
| AGAINST #2 (T-D cannot fail; "the holding reappears as a holder" not computed) | **Applied.** T-D is renamed a **record** of the holder floors, which belong to O-MATTER. It states that it does not test O-HOLD. Its one check now has content: measure's floor against an independent ħc ln2·bits/(2πR) with CODATA constants. |
| AGAINST #3 (the premise-satisfiability guard cannot fail; N_EPS is a free boolean, true at 1 AU) | **Applied.** N_EPS is tied to the distance cell by B-EPSWIN. That constraint is computed by `eps_window` in z3 over the reals, from `settle.eps_any_advantage` and the NAMED-NOT-READ limit. At 1 AU, N = 7, N_EPS is inconsistent unless H-12 supplies an unbounded carrier. In the new engine the guard holds by construction, so it is **reported STRUCTURAL**. Its content is shown by a control: the wave-1 engine at 1 AU reports **3 of 3** vacuous REMOVED-IF on O-BITS. A census of named premises says which ones can fail at all: N_EPS (at 1 AU), N_KEYING, N_FRW, N_2BVIA, N_QTOPO, N_MEASPHYS. N_FRAME3b, N_SIGKEY, N_CORR, N_MS17 and N_H12W are never constrained, so **assuming them cannot fail**, and that is stated beside every support that uses them. |
| AGAINST #4 (drift guard never compared z3 with the reports; 12 of 17 agree) | **Applied.** The guard now compares z3's per-obstruction verdict with **the A-reports' own wave-2 grade text**, parsed from their JSON by stated rules. Result: **127 of 134** (variant, obstruction) comparisons agree. The 7 that disagree come from 5 causes, each listed with its reason (section 2). Two mutated encodings must each produce an *unexplained* disagreement, and both do. ITB now has its own grade (A4 wave 2). It is no longer tied to the ITE grade. |
| AGAINST #5 (D-CTC numbers cited as the ground of W2×F1) | **Applied.** The D-CTC C2 ground (0.0817 bits; 1/2 vs 2/3) is withdrawn from B-C2-SLICE and from T-A. The ground is now `frame.drift_ordering`, which computes the drift's own ordering dependence: tanh(2ε(T − t_A)) = 0.537 / 0.291 / 0 as Alice measures before, during or after Bob's window. T-A checks it against the closed form. |
| AGAINST #6 (the antitelephone's cosmic 0 was typed) | **Applied** (frame.py, R-alone). T-A and the ground check now use `frame.reply_arrival`. It is compared with the independent Lorentz formula t_A = −uL, including u = 1/2, L = 2 → −1. |
| AGAINST #9 (floors read as costs) | **Applied.** "The cost is small in energy: 33-379 J" is withdrawn. These are **floors** on the holder's energy. They are not prices. No instrument computes a holder near the floor. The one READ-backed holder is the body, Mc² = 6.29e18 J. |
| AGAINST #10 ("removes O-BITS, O-HOLD and O-LOOP" drops the conditions) | **Applied.** Every verdict now carries its supports, and section 3 states them all. |
| AGAINST #12 (ITB commits to nothing, so ITB+W2 is consistent by construction) | **Applied, stated.** ITB has no unconditional commitment. Its content comes only through N_QTOPO / N_MEASPHYS. Its consistency with W2 holds by construction and is not evidence. The READ realisations of H-IT (MS ER=EPR) assume linearity and clash with W2, which is clash (c). |
| AGAINST #13 (W2 ⇒ SLICE builds a preferred frame into H-SETTLE; N_EPS omits H-FRAME3b) | **Applied.** The slicing is now a named premise. W2 signals only with a preferred frame (`B-GISIN`: W2 ∧ FRAME ⇒ SIG; `B-C2-SLICE`: SIG ⇒ FRAME). The frame comes from H-FRAME (F1 or F2b) or from **N_FRAME3b** (H-FRAME3b). "H-SETTLE alone" therefore reads O-BITS REMOVED-IF {W2, N_EPS, N_FRAME3b}. |
| FOR #0 (H-12, H-INFO, H-ZERO, H-NULL inert; retirement "measured") | **Applied.** Each was given the content the A-reports supply. **H-12**: an unbounded carrier frees N_EPS from the transferred bound at 1 AU (N_H12W). **H-INFO-S**: no holder needed, which clashes with B-RECV. **H-ZERO, H-NULL**: with H-IT they open O-HOLD via N_EQUIL (EGJ). Whether each literal does anything is then **measured** by a difference census (section 5). INFO (necessity) and W1 change nothing anywhere, so both are **UNTESTED-BY-SCREEN**, and no retirement is claimed for them. *Wave 1 first said* the four "meet the retirement criterion", and called that "a measured statement". |
| FOR #2 (the FRW keying lemma; O-LOOP attributed to H-FRAME) | **Applied.** B-FRW: N_FRW (H-FRW-EXACT + H-NOT-DE-SITTER) forces keying, from `frame.frw_time_function_lemma`. Result: O-LOOP is REMOVED-IF {N_FRW, N_CORR} in **every** consistent variant without clause 2b, with no member in the support. N_SIGKEY is added when W2 signals. This goes further than FOR #2 itself, which put the removal on H-SETTLE alone. The removal belongs to the geometry, and W2 only adds the need for N_SIGKEY. H-FRAME clause 1's own route is {F1, N_KEYING, N_CORR}. |
| FOR #3 (H-EQUIL not carried; O-HOLD LEFT instead of OPEN) | **Applied.** N_EQUIL is an OPEN pathway (B-HELD) for H-IT with H-ZERO or H-NULL, from `geometry.egj_fR_throat`. Under ITB+ZERO, O-HOLD's removal status is OPEN via N_EQUIL and N_ILFREE. Under ITE+ZERO, MS fn.1 closes the route, and the drift guard records that as a disagreement with A4. |
| FOR #4 (H-12 load-bearing where H-TRANSFER excludes N_EPS) | **Applied and computed.** At 1 AU, N = 7: {W2} gives O-BITS **LEFT**, and {W2, H12} gives **REMOVED-IF** {W2, H12, N_EPS, N_FRAME3b, N_H12W}. That is the screen's one synergy, in 256 W2 variants. It ties to `settle.h12_carrier_case` (2 of 9 cells flip). "Not excluded" is not evidence of a drift. |
| FOR #5 (H-INFO-S never screened) | **Applied.** H-INFO is screened in two readings. INFOS (sufficiency) is inconsistent with B-RECV in all 1,536 of its variants. So O-MATTER's survival is a **board-versus-M clash**. *Wave 1 first said* it survived "by a board holding none of the seven touches". |
| FOR #6 ("M's sentence contradicts itself") | **Applied.** F1 now commits only to "a preferred frame exists" (M's words). Keying is the named premise N_KEYING (the docket's H-KEYING). F1+F2b is **consistent as commitments**. It is excluded only by the premise clashes {N_KEYING, N_2BVIA} and {N_FRW, N_2BVIA}, the latter for F2b alone. *Wave 1 first said* "M's H-FRAME sentence contradicts itself when both clauses are taken strong (clash a, 640 variants)". |
| FOR #7 (6.21, N ≥ 7 and Holevo are nlcontrol's, not W2's) | **Applied.** B-CAP and N_EPS name H-NLCONTROL-FORM. T-E reports the pairs per qubit separately for nlcontrol (7, or 6.21 block-coded) and for the W2 class under H-BORN-AT-BOB (> 2 on average, ≥ 3 per qubit, the 1 bit/pair ceiling not attained at finite T: A1). Without H-BORN-AT-BOB the class capacity is **OPEN**. The drift-pair totals are labelled upper figures for one Hamiltonian. |
| FOR #8 (T = L/2c is a choice) | **Applied.** The drift time T = atanh(D_N)/(2ε) does not depend on distance (`settle.drift_time_needed`). At the unread limit, reading A, N = 7, it is 13.38 h, and the read is 0.99847 L/c early at 1 ly. The ε for any advantage is `eps_any_advantage`, exactly half of wave 1's figure (ratio 2.000000), and no window entry flips (computed: 0 of 18). |
| FOR #9 (first transit assumed one-end distribution) | **Applied.** `settle.first_transit_times` is used for the **midpoint source** (LEDGER D23 as corrected in DOCKET 67). The first read comes L/2c + T = 0.50153 yr after the source fires at 1 ly, and it beats light launched from Alice at that moment. One-end distribution never does. Control: at 1 AU, T > L/2c, and it fails. |
| FOR #10 (ITE×W2 graded REFUTED) | **Applied.** It is now **INCONSISTENT-AS-ENCODED**, clash (c). It is a test of ER=EPR as MS state it, and it does not refute W2. |
| REPRODUCE #0 (no convention named on the best row) | **Applied.** W2 *is* convention C2 (H-C2), stated in its reading and on every signal. Under C1 (W1) there is no signal (2.2e-16). |
| REPRODUCE #1 (clash counts were z3's returned core) | **Applied.** Every minimal core of every inconsistent variant is enumerated (`all_mus`), and the counts are by inclusion-exclusion. The wave-1 census is recomputed for the record: (a) present in **768** (640 alone), (b) 256, (c) 256, union 1,152 = 768 + 256 + 256 − 64 − 64. |
| REPRODUCE #4 (Reznik window) | **Applied.** It is now 0.91 L/c < T < L/c. p.10 gives T < L/c (READ). p.12 Fig. 2 gives L/T < 1.1 for that window and gap (READ). The window itself is labelled DERIVED-FROM-READ. |
| AGAINST #1, #14; R-alone's grades | Not sited here. combine.py now reads the repaired grades: R-INDEX alone LEAVES-ALL, H-SETTLE×H-INFO REMOVED-IF. |

## 1. What was built: every combination, in every reading

- **127 non-empty combinations** of the seven hypotheses.
- **Readings** (every one screened):
  - **H-SETTLE**: W2 is the drift on Bob's per-branch pure state, which is convention C2 = H-C2. The definition does not say which state the drift acts on, so C2 is a named hypothesis, not M's words. W1 is the same drift on the reduced state (C1). KR is the causal Kaplan-Rajendran form.
  - **H-FRAME**: F1 is clause 1, "a preferred frame exists". Keying corridors to it is N_KEYING, not F1. F2b is clause 2b, "messages reach the past of the cosmic clock". F1+F2b is both together.
  - **H-IT**: ITB is the information-layer reading, with no READ realisation. ITE is ER=EPR with MS's own assumptions.
  - **H-INFO** (new in wave 2): INFO is necessity. **INFOS** is sufficiency, A3's H-INFO-S.
- **Reading slots** none / R-INDEX / R-QUANTUM / both: (4·4·3·3·2·2·2 − 1)·4 + 3 = **4,607 variants**, none
  skipped. *Wave 1:* 3,071 (H-INFO in one reading).
- **Distance cells.** The screen runs at **1 ly, N = 7**, where the transferred-bound window is non-empty under both
  H-MAP readings. It is repeated at **1 AU, N = 7**, where the window is empty under both, for the **1,152 W2
  variants**. Re-screening only those is complete, and z3 proves it: N_EPS occurs only in B-CAP and B-EPSWIN, and the
  board admits no CAP without W2.
- **O-MAKE** is carried as O-MAKE-TOPO and O-MAKE-DIST. In five-way terms O-MAKE counts only if both forms do.

**Verdicts per obstruction:**

| verdict | meaning |
|---|---|
| **REMOVED** | forced by the variant's commitments, with no named premise |
| **REMOVED-IF** | forced once the named premises of a **support** are assumed. **Every** minimal support is listed: the present members plus named premises drawn from a premise set that is consistent with the variant. Absences are fixed (closed world), and a member that a premise presupposes is added back. |
| **NOT-BOUND-IF** | the obstruction's theorem is forced not to bind once a support's premises are assumed, because its geometric premise fails. **Not a removal.** The removal's own status (OPEN via …, SILENT, LEFT) is reported beside it. |
| **OPEN** | possible only through an OPEN pathway that the sources leave undecided |
| **SILENT** | not forced either way, without any OPEN pathway |
| **LEFT** | the obstruction stands in every model |

A variant can also be **INCONSISTENT** (an unconditional clash, with every minimal core named). A consistent variant
can carry a **PREMISE CLASH**: a minimal set of named premises it cannot carry. The premise is then dropped from that
variant's supports, never assumed, so no conditional verdict rests on a premise the variant contradicts.

## 2. The screen (z3), and its guards

**What it is.** Bookkeeping over findings that other instruments own. Every board holding (`_board`) and every
commitment (`_commitments`) is a tracked constraint with its ground, which is a computation or a READ page. z3 adds
which commitments contradict one another, which members and premises each verdict rests on (all supports, not one),
and exhaustive coverage. It is not new physics.

**Guards (the screen refuses to report if any fails).**

- **Vacuity.**
  - The board alone is SAT.
  - Each single reading is SAT, except INFOS, which is caught as a clash.
  - The named premises are jointly SAT with the board at 1 ly. They are jointly **UNSAT** at 1 AU, because the window is empty there. This has content.
  - The named premises and the OPEN pathways together are SAT with the board.
  - The board admits both a loop and no loop.
  - **CONTROL:** with B-RECV deleted, O-MATTER becomes removable.
- **Contradictions that must be caught** (seven, every one caught):
  - ITE & W2;
  - INFOS;
  - a planted signal in linear QM;
  - F1 & F2b under {N_KEYING, N_2BVIA};
  - F2b under {N_FRW, N_2BVIA};
  - ITB & RQ under {N_QTOPO};
  - W2 at 1 AU without H12 under {N_EPS}.
- **Results that used to be clashes:** F1 & F2b is consistent as commitments, and so is ITB & RI & RQ. *Wave 1 called the first "M's sentence contradicting itself", and the second came from B-THROAT's slip.*
- **STRUCTURAL, not counted as evidence.** "Every REMOVED-IF / NOT-BOUND-IF support is drawn from a premise set
  consistent with the variant" holds by construction of the engine. Its content is the control: the **wave-1 engine at
  1 AU reports 3 of 3 vacuous REMOVED-IF** on O-BITS ({W2}, {W2, F1}, {W2, ITB}). The named-premise census says which
  premises can fail at all:

  | named premise | can it fail? | variants where it is inadmissible |
  |---|---|---|
  | N_EPS | **yes**, at 1 AU | 256 W2 variants without H12 (1 AU) |
  | N_KEYING | yes | 704 (with F1 + F2b, under N_2BVIA) |
  | N_FRW | yes | 1,408 (with F2b, under N_2BVIA) |
  | N_2BVIA | yes | 1,408 |
  | N_QTOPO | yes | 512 (ITB + RQ) |
  | N_MEASPHYS | yes | 256 (ITB + RI + RQ) |
  | N_FRAME3b, N_SIGKEY, N_CORR, N_MS17, N_H12W | **no**: STRUCTURAL, assuming them cannot fail | 0 |

- **Encoding drift: z3 against the A-reports' own grades.** There are 26 (variant, cell, grade) rows, tied to A1–A4
  wave-2 grade text parsed from their JSON. The parse rules are stated in `parse_report_class` and `z3_class`. A
  removal counts for a hypothesis only if some support contains it. O-MAKE-DIST "OPEN via N_VAC only" compares as not
  removed, because the reports do not carry N_VAC. A NOT-BOUND verdict matches a report's OPEN when its removal status
  is OPEN. **127 of 134 comparisons agree.** The 7 that disagree come from 5 causes, each explained:

  | report, variant, obstruction | why z3 differs |
  |---|---|
  | A1, {W2} and {W2, H12} (both cells), O-LOOP | A1 attributes O-LOOP to H-SETTLE-W. z3 finds it rests on **no member**: the exact-FRW geometry (N_FRW) with N_CORR, in every variant without clause 2b. W2 only adds the need for N_SIGKEY. A1's own H-12-alone grade (O-LOOP LEAVES) leaves the same geometry unattributed, so the two A1 grades disagree with each other. |
  | A1, {W2, H12} (both cells), O-HOLD | A1's "OPEN (G in KR form)" is H-SETTLE's KR reading. In a W2 variant that branch is absent (one reading per variant). |
  | A2, {F2b}, O-MAKE | A2's "a CTC reopens Geroch's clause" is not carried as a pathway. It would trade O-MAKE-TOPO for O-LOOP (encoding choice, named). |
  | A4, {ITE, ZERO}, O-HOLD | A4's H-ZERO + H-IT grade does not split H-IT's readings. Under ITE, MS fn.1 assumes non-traversability (C-ITE: not HELD), which closes the EGJ route. Under ITB the verdicts agree. |

  **CONTROLS:** the mutated encodings are each caught as unexplained disagreements. `KR-unconditional` gives A1
  {KR} O-HOLD OPEN → not removed (126/134). `wave1-THROAT` gives A3 {ITB, RI}, A4 {ITB} and A4 {ITB, ZERO} O-HOLD
  NB/OPEN → REMOVED (123/134). There is also a ground row: `settle.h12_carrier_case` at 1 AU, N = 7 says EXCLUDED
  under H-TRANSFER and NOT EXCLUDED under H-12-CARRIER, and z3 gives {W2} LEFT and {W2, H12} REMOVED-IF. They agree.
- **Grounds re-run, each against an independent computation:**
  - tanh(2εT) (math.tanh);
  - C1 2.2e-16;
  - the drift ordering against tanh(2ε(T − t_A)), to 1.2e-5;
  - the antitelephone against −uL;
  - cosmic keying, 0 failures at ranks 2 and 3;
  - the FRW lemma (unsat; vacuity sat; control a ≥ 0 sat);
  - nlcontrol N < 7 impossible, CMAX = log₂1.25;
  - H-12 carrier flips, 2;
  - LOCC 8.9e-16;
  - QEI 2.08e-68;
  - zero shift `unsat`;
  - EGJ: β_crit = −r0²/2 = 1.91e69 l_P² at 1 m, r⁴T_kk → −2r0², and β = 0 reproduces R_kk;
  - INFOS support: φ(1) = 0, Bekenstein 0 bits at E = 0, CARRIES_SUBSTANCE False;
  - the board flags and LEDGER S5/S10/S13.

### Contradictory combinations: every core, counted by inclusion-exclusion

Of the 4,607 variants, **2,815 are consistent and 1,792 are not.** Every one of the 127 combinations has a consistent
variant. Every minimal core was enumerated. 320 inconsistent variants have more than one core. Grouped by the minimal
literal set the cores contain:

| clash | cores (variants) | present in | alone in | what collides | label |
|---|---|---|---|---|---|
| **(c) W2 + ITE** | C-ITE + C-W2, linearity (384); C-ITE + B-GISIN + C-F1, no-signal with a frame (192); C-ITE + B-GISIN + C-F2b (192) | 384 | 256 | ER=EPR as MS state it (fn.1 p.2 non-traversability; §3.1 p.16; §5.4 pp.36-37 linearity, READ) against a per-branch drift. Computed (T-B): in Van Raamsdonk's eq.(1) state the drift signals 0.537 at β = 0. | **INCONSISTENT-AS-ENCODED**: a test of ER=EPR (MS fn.1: if traversable, "the ER=EPR connection would be wrong"), not a refutation of W2. *Wave 1 first said* REFUTED. |
| **(d) INFOS** | C-INFOS + B-RECV (1,536) | 1,536 | 1,408 | H-INFO-S (information at the destination suffices) against B-RECV (transit.CARRIES_SUBSTANCE False; Bekenstein: a complete system with E > 0 holds the bits; φ(1) = 0) | **CLASH, board versus M.** M's to rule. Not a retirement. |

Intersection 128; union by inclusion-exclusion 384 + 1,536 − 128 = **1,792**. That equals the inconsistent count.

**Premise clashes** (consistent variants that cannot carry a named premise), at 1 ly:

| premise clash | present in | alone in | reading |
|---|---|---|---|
| {N_2BVIA, N_FRW} with F2b | 1,408 | 576 | exact FRW excludes clause 2b if corridors are the route to the cosmic past (A2) |
| {N_2BVIA, N_KEYING} with F1 + F2b | 704 | 0 | **the docket's keying excludes clause 2b.** This is wave 1's clash (a), and it is not in M's sentence. |
| {N_QTOPO} with ITB + RQ | 512 | 128 | one corridor, two accounts: ITB's no-geometric-throat premise against R-QUANTUM's throat (A4) |
| {N_MEASPHYS} with ITB + RI + RQ | 256 | 0 | the same, through R-INDEX |

The union by inclusion-exclusion is 1,664. At 1 AU (W2 variants) **{N_EPS} with "not H12"** is added: 256 variants, the empty window.

**Wave 1's clash census, recomputed** (`wave1_clash_census`, over wave 1's 3,071 variants):

| clash | present | alone |
|---|---|---|
| (a) F1+F2b | 768 | 640 |
| (b) ITB+RI+RQ | 256 | 192 |
| (c) ITE+W2 | 256 | 192 |

Union 768 + 256 + 256 − 64 − 64 = 1,152. *Wave 1 first said* "(a) 640, (b) 256, (c) 256", which was the core z3
happened to return. Wave 2 removes (a) and (b) as unconditional clashes: (a) becomes a premise clash, and (b) came
from B-THROAT's slip.

## 3. The answer

**No consistent variant removes all five obstructions or makes them all NOT-BOUND.** The most is **three of five**,
attained by 64 consistent variants at 1 ly. Every one of them contains **{H-SETTLE W2, H-IT ITB}**, and any of F1,
R-INDEX, H-12, H-INFO (necessity), H-ZERO and H-NULL may be added. At 1 AU the most is again three, in 32 variants,
all of which also contain H12. The verdicts for the smallest such variant, {W2, ITB}, at 1 ly:

| obstruction | verdict | every support (members + named premises) | removal status |
|---|---|---|---|
| O-BITS | **REMOVED-IF** | {W2; N_EPS, N_FRAME3b}. With F1 added there is also {W2, F1; N_EPS}. W2 is H-C2; N_EPS is nlcontrol's Hamiltonian, with ε > ε_any(L, N) not excluded by the NAMED-NOT-READ limit. | — |
| O-MAKE-TOPO | **NOT-BOUND-IF** | {ITB; N_QTOPO}, no READ source. With RI there is also {ITB, RI; N_MEASPHYS}. | OPEN via N_ILFREE |
| O-MAKE-DIST | **OPEN** | — | via N_VAC only |
| O-HOLD | **NOT-BOUND-IF** (geometric NEC/throat form) | {ITB; N_QTOPO}; with RI also {ITB, RI; N_MEASPHYS} | OPEN via N_ILFREE (with H-ZERO or H-NULL, also N_EQUIL) |
| O-MATTER | **LEFT** | — | — |
| O-LOOP | **REMOVED-IF**, by the geometry, no member | {N_CORR, N_FRW, N_SIGKEY}; with F1 also {F1; N_CORR, N_KEYING, N_SIGKEY} | — |

In removed-only terms, which exclude NOT-BOUND, the most any consistent variant removes is **two of five**: O-BITS
and O-LOOP, both conditional.

**Which obstructions survive every consistent variant (both cells):**

- **O-MATTER**: LEFT in all 2,815 consistent variants and in all 512 consistent W2 variants at 1 AU. The one
  reading that would remove it, INFOS, is inconsistent with B-RECV in every variant (clash d). So O-MATTER's survival
  is a clash between the board and M's sufficiency reading. Nothing the screen settles removes it.
- **O-MAKE in its distribution form (O-MAKE-DIST)**: OPEN via N_VAC only in every consistent variant, and never
  removed or not-bound. Every channel runs on pre-distributed entanglement (T-B, T-C), and LOCC cannot make it (MS
  §3.2, READ; 8.9e-16 computed). O-MAKE in five-way terms therefore never falls, even where its topology form is
  NOT-BOUND-IF.

**What is never REMOVED:** O-MAKE-TOPO and O-HOLD are at most NOT-BOUND-IF. Their removal status is OPEN via N_ILFREE,
and no source prices the non-geometric corridor.

*Wave 1 first said:* "the most any consistent variant removes is four entries of the six-way split, {W2, F1, ITB,
R-INDEX}: O-BITS REMOVED-IF, O-MAKE-TOPO REMOVED-IF, **O-HOLD REMOVED**, O-LOOP REMOVED-IF", and "in five-way terms
this variant removes O-BITS, O-HOLD and O-LOOP". The same variant now reads O-BITS REMOVED-IF, O-MAKE-TOPO
NOT-BOUND-IF, O-HOLD NOT-BOUND-IF, O-LOOP REMOVED-IF. F1 and R-INDEX are each only an alternative support, and
neither is needed.

**Synergy and interference.**

- **Synergy: one, and it is H-12's.** At 1 AU, N = 7, {W2} leaves O-BITS and {W2, H12} removes it, REMOVED-IF {W2, H12;
  N_EPS, N_FRAME3b, N_H12W}. This holds in 256 variants. Neither member does it alone. At 1 ly there is no synergy:
  every member-attributed result is already a single member's. *Wave 1 first said:* "Synergy (the measured payoff of
  M's instruction): O-HOLD is removed by ITB and R-INDEX jointly … 192 consistent variants". That came from B-THROAT's
  slip.
- **Interference: 1,088 variants at 1 ly** (224 at 1 AU), in two kinds. In 576 variants clause 2b undoes the O-LOOP
  removal, because a message into the cosmic past spoils the time function. In 384 variants R-QUANTUM undoes ITB's
  non-binding of O-MAKE-TOPO and O-HOLD, because a geometric throat is asserted. 128 variants have both. *Wave 1 first
  said:* "Interference: none".

## 4. Complementary combinations, and the instrument tests

A consistent variant is **complementary** when more than one member contributes a member-attributed result and no
single member's own result covers it. **512 variants at 1 ly in 12 classes, and 272 at 1 AU in 14 classes.** Every
class has a test (`combine.py --json` lists the classes).

**T-A: W2 × F1** (and F1 with any member). It now rests on the drift, not the D-CTC.

- `frame.drift_ordering`: Bob's signal is 0.5371 / 0.4219 / 0.2913 / 0.1489 / 0 as Alice measures at 0, ¼, ½, ¾ or
  all of Bob's window. The closed form tanh(2ε(T − t_A)) agrees to 1.2e-5. A C2 signal is defined only relative to a
  slicing, which is computed for the drift itself.
- The reply keyed to the sender's frame arrives at −3/5, and keyed to the cosmic frame at 0, both computed.
- Cosmic keying: 0 failures at ranks 2 and 3.
- H-IT's model adds no signal: 1.55e-15.
- **PASS.** *Wave 1 first said:* "C2 carries 0.0817 bits per use … Bob-first 1/2, Alice-first 2/3 or 1/3". That is
  the D-CTC circuit, which needs a CTC at Bob, and it is withdrawn as a ground.

**T-B: W2 inside H-IT's own READ model** (`tfd_drift`; ε = 0.1, T = 3 are nlcontrol's illustrative parameters):

| β | S (bits) | C2 signal (exact) | linear | C1 |
|---|---|---|---|---|
| 0 | 1.000 | 0.53705 (= tanh 0.6) | 0 | 0 |
| 0.5 | 0.956 | 0.50796 | 0 | 0 |
| 1 | 0.840 | 0.43186 | 0 | 0 |
| 2 | 0.527 | 0.24001 | 0 | 0 |
| 4 | 0.130 | 0.04204 | 0 | 0 |
| 8 | 0.0044 | 0.00080 | 0 | 0 |
| 30 | 0.000 | 0.00000 | 0 | 0 |

The channel runs on the bridge, and it does not replace the bridge. ITB + W2 is consistent **because ITB is encoded
with no unconditional content** (AGAINST #12). Under ITE the signal contradicts MS §3.1 and fn.1, which is clash (c),
INCONSISTENT-AS-ENCODED. **PASS.**

**T-C: the drift cannot make its own pairs.**

- Product states give 2.9e-15, against the Bell control's 0.53706.
- Local unitaries change the entropy by 8.9e-16, and the nonlocal control by 1.965 bits.
- **PASS.**

**T-D: ITB × R-INDEX. A record of the holder floors, not a test of O-HOLD.**

- The Bekenstein **floors** on O-MATTER's holder are 33.2 / 144 / 379 / 99.1 J at R = 1 m (measure's four counts of a
  70 kg body), matching the CODATA cross-check exactly.
- These are floors. They are not prices. The one READ-backed holder is the body, Mc² = 6.29e18 J.
- The O-HOLD verdict is NOT-BOUND-IF and comes from B-THROAT, not from here. *Wave 1 first said:* "O-HOLD is removed,
  and the holding reappears as a holder … The removal moves the cost into O-MATTER."

**T-E: the most-removing variant, end to end.**

- **The ε window**, z3 over the reals. ε_any is the ε for any advantage, from `settle.eps_any_advantage`. ε_max is
  2.39e-5 s⁻¹ (reading A) or 1.19e-5 s⁻¹ (reading B), from the NAMED-NOT-READ Majumder figure.

  | distance | N | ε_any (s⁻¹) | consistent? | wave 1's ε at T = L/2c (DECLARED-FRAC) |
  |---|---|---|---|---|
  | 1 ly | 7 | 3.64e-8 | yes | 7.29e-8 |
  | 4.24 ly | 7 | 8.59e-9 | yes | 1.72e-8 |
  | 1 AU | 7 | 2.30e-3 | **no** | 4.61e-3 |
  | 1 AU | 1,000 | 1.06e-4 | **no** | 2.11e-4 |
  | 1 AU | 10⁶ | 3.34e-6 | yes | 6.67e-6 |

  The ratio is exactly 2.000000 in every row, and none of the 18 entries flips. Vacuity: ε > 0 alone is SAT.
- **Timing.**
  - The drift time does not depend on distance. At the unread limit, reading A, N = 7, it is T = **13.38 h**. Once
    the pairs and the holder are in place, the read is 0.99847 L/c early at 1 ly.
  - These are floors at an unread upper limit, not measured times. An upper limit consistent with zero is not
    evidence of a drift.
- **First transit** (`settle.first_transit_times`):
  - **Midpoint source** (LEDGER D23 as corrected in DOCKET 67): the read comes at L/2c + T = **0.50153 yr** after the
    source fires. Light launched from Alice at that moment arrives at 1 yr, so the first message **beats it**,
    conditional on N_EPS, H-C2 and N_FRAME3b.
  - **One-end distribution**: L/c + T, which never beats light.
  - **Control:** at 1 AU, T = 13.38 h > L/2c = 250 s, and the midpoint case fails.
  - The source and the holder still arrive at ≤ c. That is setup cost, not message latency.
- **Pairs per teleported qubit:**
  - nlcontrol's Hamiltonian (H-NLCONTROL-FORM): 7 without block coding, 6.21 on average with it.
  - The W2 class under H-BORN-AT-BOB: strictly more than 2 on average, and at least 3 per qubit (A1). The class
    capacity is OPEN without H-BORN-AT-BOB.

  | count (A3's H-FAITHFUL: one qubit per bit) | teleportation ebits | nlcontrol pairs, N = 7 (upper figure, one Hamiltonian) | block-coded | W2 class floor, H-BORN-AT-BOB (strictly above) | holder FLOOR at R = 1 m |
  |---|---|---|---|---|---|
  | species sequence | 9.51e27 | 6.66e28 | 5.91e28 | 1.90e28 | 33.2 J |
  | grid 1 Å | 4.14e28 | 2.90e29 | 2.57e29 | 8.28e28 | 144 J |
  | grid 0.1 Å | 1.09e29 | 7.61e29 | 6.76e29 | 2.18e29 | 379 J |
  | thermal entropy | 2.84e28 | 1.99e29 | 1.76e29 | 5.68e28 | 99.1 J |

- **PASS.** *Wave 1 first said:*
  - "Bob reads after T = L/2c, which is 0.5 yr before light";
  - "The first transit waits for the pairs: at the earliest L/c + T = 1.5 yr … the first one cannot";
  - "the channel needs at least 2/CMAX = 6.21 pre-shared pairs".

  The first two were a declared T and one-end distribution. The third is nlcontrol's figure, not the class's.

**T-F: RQ × KR.** Two OPENs on O-HOLD. The in-scope QEI fraction 2.08e-68 is re-run. **PASS** (recorded, not
decided).

**T-G (new): W2 × H12 at 1 AU.** `settle.h12_carrier_case` flips 2 of 9 cells (1 AU at N = 7 and N = 1,000). z3 gives
{W2} LEFT and {W2, H12} REMOVED-IF. **PASS.** No READ source gives a model of a Weinberg-form drift in G or v
(N_H12W). "Not excluded" is not evidence.

**T-H (new): (ZERO | NULL) × IT.** `geometry.egj_fR_throat`:

- T_kk(r0) = 2(−2β − r0²)/r0⁴, which is ≥ 0 iff β ≤ −r0²/2, that is 1.91e69 l_P² at 1 m (EGJ's β ~ l_P²).
- At 1.05 r0, T_kk = −1.68 at β = −r0²/2 (−1.65 at β = 0).
- r⁴T_kk → −2r0² for every β (b = r0²/r, f = 1 + βR).
- The pathway is OPEN (N_EQUIL). It is never a removal. **PASS.**

**T-I (new): INFOS vs B-RECV.** `measure.info_s_clash`: φ(1) = 0 bits, Bekenstein 0 bits at E = 0, and
CARRIES_SUBSTANCE False. These are the computed support of clash (d). **PASS.**

## 5. Each hypothesis across every combination (rule 2)

Charter rule 2: *"A failure alone does not retire a hypothesis. It is retired only if it also fails in every
combination tested."* Wave 2 establishes retirement only for a hypothesis that was **exercised**. The **difference
census** (`exercised`) measures it: drop the literal from each variant and count the variants whose result changes
(consistency, any verdict, any OPEN pathway, any premise clash).

| literal | exercised? (variants changed by it) | what it contributes, from the supports | rule 2 |
|---|---|---|---|
| W2 (H-SETTLE, C2) | yes: 896 of 1,152 | O-BITS REMOVED-IF {W2; N_EPS, N_FRAME3b} (or F1 in place of N_FRAME3b); clash (c) with ITE | **kept, PARTIAL** |
| W1 (H-SETTLE, C1) | **no** (0) | its one commitment, no signal, is what the board gives without it | **UNTESTED-BY-SCREEN.** Its single-hypothesis grade (LEAVES-ALL, computed 2.2e-16) stands. |
| KR (H-SETTLE) | yes: 512 | O-HOLD OPEN via N_EPSG; removes nothing | kept: OPEN pathway |
| F1 (H-FRAME clause 1) | yes: 896 | O-LOOP REMOVED-IF {F1; N_KEYING, N_CORR}, an alternative to the geometry's {N_FRW, N_CORR}; supplies W2's frame | **kept, PARTIAL** |
| F2b (H-FRAME clause 2b) | yes: 1,600 | supplies W2's frame (O-BITS REMOVED-IF with W2); undoes O-LOOP's removal in 1,408 variants; premise clashes with N_FRW / N_KEYING | kept |
| ITB (H-IT) | yes: 1,024 | O-MAKE-TOPO and O-HOLD **NOT-BOUND-IF** {N_QTOPO}; removal OPEN via N_ILFREE | **kept: NOT-BOUND-IF**, no removal |
| ITE (H-IT) | yes: 1,152 | O-MAKE-TOPO NOT-BOUND-IF {N_MS17}; clash (c) with W2 | **kept: NOT-BOUND-IF** |
| H12 | yes, **at 1 AU only** (256 of the W2 variants) | O-BITS REMOVED-IF {W2, H12; N_EPS, N_FRAME3b, N_H12W} where the transferred bound excludes W2 alone | **kept, PARTIAL** (A1). Not retired. |
| INFO (H-INFO, necessity) | **no** (0) | none: consistent with B-RECV and decides nothing encoded | **UNTESTED-BY-SCREEN.** Retirement not established. |
| INFOS (H-INFO, sufficiency) | yes: all 1,536 inconsistent | clash (d) with B-RECV | **CLASH, board versus M.** M's to rule. |
| ZERO (H-ZERO) | yes: 256 | with H-IT, O-HOLD OPEN via N_EQUIL; removes nothing (the NEC is invariant, z3) | kept: OPEN pathway |
| NULL (H-NULL) | yes: 256 | the same | kept: OPEN pathway |
| RI (R-INDEX) | yes: 256 | with ITB, an alternative NOT-BOUND-IF support {ITB, RI; N_MEASPHYS}; premise clash with RQ | kept (an alternative premise, never needed) |
| RQ (R-QUANTUM) | yes: 1,024 | O-HOLD OPEN via N_XI; undoes ITB's non-binding (premise clash on N_QTOPO) | kept: OPEN pathway |

**Load-bearing** (in some support): W2, F1, F2b, ITB, ITE and RI at 1 ly; plus H12 at 1 AU. **Named premises ever
used:** N_CORR, N_EPS, N_FRAME3b, N_FRW, N_KEYING, N_MEASPHYS, N_MS17, N_QTOPO and N_SIGKEY; plus N_H12W at 1 AU.

*Wave 1 first said:* H-12, H-INFO, H-ZERO and H-NULL each "meets the retirement criterion as a remover … a measured
statement". That was the inert encoding. Of the four, only INFO's necessity reading is still inert, and it is
reported UNTESTED-BY-SCREEN.

## 6. Every combination (127, plus readings only)

The table is generated by `python3 combine.py --table PATH` from the 1 ly screen.

- **Abbreviations:** IT, SET, FR, 12, INF, ZER and NUL stand for the seven hypotheses.
- **Verdict codes:** R-IF = REMOVED-IF; NB-IF = NOT-BOUND-IF; L = LEFT; S = SILENT.
- **The O-LOOP column is the board's geometry** under {N_FRW, N_CORR}, wherever clause 2b is absent. No member is in
  that support, so it does not credit the combination.
- **The last column** gives the 1 AU re-screen of the combination's W2 variants.

| # | combination | variants | consistent | clash (literals in core) | premise clashes | best consistent variant: BITS/TOPO/DIST/HOLD/MATTER/LOOP | five-way removed or not-bound | complementary | 1 AU: W2 variants with O-BITS removed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IT | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB) | HOLD,LOOP | 0 | - |
| 2 | SET | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2) | BITS,LOOP | 0 | 0/4 |
| 3 | FR | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1) | LOOP | 0 | - |
| 4 | 12 | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (H12) | LOOP | 0 | - |
| 5 | INF | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (INFO) | LOOP | 0 | - |
| 6 | ZER | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (ZERO) | LOOP | 0 | - |
| 7 | NUL | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (NULL) | LOOP | 0 | - |
| 8 | IT+SET | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB) | BITS,HOLD,LOOP | 2 | 0/8 |
| 9 | IT+FR | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB) | HOLD,LOOP | 6 | - |
| 10 | IT+12 | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12) | HOLD,LOOP | 0 | - |
| 11 | IT+INF | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,INFO) | HOLD,LOOP | 0 | - |
| 12 | IT+ZER | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,ZERO) | HOLD,LOOP | 0 | - |
| 13 | IT+NUL | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,NULL) | HOLD,LOOP | 0 | - |
| 14 | SET+FR | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1) | BITS,LOOP | 4 | 0/12 |
| 15 | SET+12 | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,H12) | BITS,LOOP | 0 | 4/4 |
| 16 | SET+INF | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,INFO) | BITS,LOOP | 0 | 0/8 |
| 17 | SET+ZER | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,ZERO) | BITS,LOOP | 0 | 0/4 |
| 18 | SET+NUL | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,NULL) | BITS,LOOP | 0 | 0/4 |
| 19 | FR+12 | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12) | LOOP | 0 | - |
| 20 | FR+INF | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,INFO) | LOOP | 0 | - |
| 21 | FR+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,ZERO) | LOOP | 0 | - |
| 22 | FR+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,NULL) | LOOP | 0 | - |
| 23 | 12+INF | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (H12,INFO) | LOOP | 0 | - |
| 24 | 12+ZER | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (H12,ZERO) | LOOP | 0 | - |
| 25 | 12+NUL | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (H12,NULL) | LOOP | 0 | - |
| 26 | INF+ZER | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (INFO,ZERO) | LOOP | 0 | - |
| 27 | INF+NUL | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (INFO,NULL) | LOOP | 0 | - |
| 28 | ZER+NUL | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (ZERO,NULL) | LOOP | 0 | - |
| 29 | IT+SET+FR | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB) | BITS,HOLD,LOOP | 20 | 0/24 |
| 30 | IT+SET+12 | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12) | BITS,HOLD,LOOP | 2 | 4/8 |
| 31 | IT+SET+INF | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,INFO) | BITS,HOLD,LOOP | 2 | 0/16 |
| 32 | IT+SET+ZER | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,ZERO) | BITS,HOLD,LOOP | 2 | 0/8 |
| 33 | IT+SET+NUL | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,NULL) | BITS,HOLD,LOOP | 2 | 0/8 |
| 34 | IT+FR+12 | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12) | HOLD,LOOP | 6 | - |
| 35 | IT+FR+INF | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,INFO) | HOLD,LOOP | 6 | - |
| 36 | IT+FR+ZER | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,ZERO) | HOLD,LOOP | 6 | - |
| 37 | IT+FR+NUL | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,NULL) | HOLD,LOOP | 6 | - |
| 38 | IT+12+INF | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,INFO) | HOLD,LOOP | 0 | - |
| 39 | IT+12+ZER | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,ZERO) | HOLD,LOOP | 0 | - |
| 40 | IT+12+NUL | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,NULL) | HOLD,LOOP | 0 | - |
| 41 | IT+INF+ZER | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,INFO,ZERO) | HOLD,LOOP | 0 | - |
| 42 | IT+INF+NUL | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,INFO,NULL) | HOLD,LOOP | 0 | - |
| 43 | IT+ZER+NUL | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,ZERO,NULL) | HOLD,LOOP | 0 | - |
| 44 | SET+FR+12 | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12) | BITS,LOOP | 4 | 12/12 |
| 45 | SET+FR+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,INFO) | BITS,LOOP | 4 | 0/24 |
| 46 | SET+FR+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,ZERO) | BITS,LOOP | 4 | 0/12 |
| 47 | SET+FR+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,NULL) | BITS,LOOP | 4 | 0/12 |
| 48 | SET+12+INF | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,INFO) | BITS,LOOP | 0 | 4/8 |
| 49 | SET+12+ZER | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,ZERO) | BITS,LOOP | 0 | 4/4 |
| 50 | SET+12+NUL | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,NULL) | BITS,LOOP | 0 | 4/4 |
| 51 | SET+INF+ZER | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,INFO,ZERO) | BITS,LOOP | 0 | 0/8 |
| 52 | SET+INF+NUL | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,INFO,NULL) | BITS,LOOP | 0 | 0/8 |
| 53 | SET+ZER+NUL | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,ZERO,NULL) | BITS,LOOP | 0 | 0/4 |
| 54 | FR+12+INF | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,INFO) | LOOP | 0 | - |
| 55 | FR+12+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,ZERO) | LOOP | 0 | - |
| 56 | FR+12+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,NULL) | LOOP | 0 | - |
| 57 | FR+INF+ZER | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,INFO,ZERO) | LOOP | 0 | - |
| 58 | FR+INF+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,INFO,NULL) | LOOP | 0 | - |
| 59 | FR+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,ZERO,NULL) | LOOP | 0 | - |
| 60 | 12+INF+ZER | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (H12,INFO,ZERO) | LOOP | 0 | - |
| 61 | 12+INF+NUL | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (H12,INFO,NULL) | LOOP | 0 | - |
| 62 | 12+ZER+NUL | 4 | 4 | - | - | L/L/OPEN/L/L/R-IF (H12,ZERO,NULL) | LOOP | 0 | - |
| 63 | INF+ZER+NUL | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (INFO,ZERO,NULL) | LOOP | 0 | - |
| 64 | IT+SET+FR+12 | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12) | BITS,HOLD,LOOP | 20 | 12/24 |
| 65 | IT+SET+FR+INF | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,INFO) | BITS,HOLD,LOOP | 20 | 0/48 |
| 66 | IT+SET+FR+ZER | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,ZERO) | BITS,HOLD,LOOP | 20 | 0/24 |
| 67 | IT+SET+FR+NUL | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,NULL) | BITS,HOLD,LOOP | 20 | 0/24 |
| 68 | IT+SET+12+INF | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,INFO) | BITS,HOLD,LOOP | 2 | 4/16 |
| 69 | IT+SET+12+ZER | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,ZERO) | BITS,HOLD,LOOP | 2 | 4/8 |
| 70 | IT+SET+12+NUL | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,NULL) | BITS,HOLD,LOOP | 2 | 4/8 |
| 71 | IT+SET+INF+ZER | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,INFO,ZERO) | BITS,HOLD,LOOP | 2 | 0/16 |
| 72 | IT+SET+INF+NUL | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,INFO,NULL) | BITS,HOLD,LOOP | 2 | 0/16 |
| 73 | IT+SET+ZER+NUL | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,ZERO,NULL) | BITS,HOLD,LOOP | 2 | 0/8 |
| 74 | IT+FR+12+INF | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,INFO) | HOLD,LOOP | 6 | - |
| 75 | IT+FR+12+ZER | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,ZERO) | HOLD,LOOP | 6 | - |
| 76 | IT+FR+12+NUL | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,NULL) | HOLD,LOOP | 6 | - |
| 77 | IT+FR+INF+ZER | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,INFO,ZERO) | HOLD,LOOP | 6 | - |
| 78 | IT+FR+INF+NUL | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,INFO,NULL) | HOLD,LOOP | 6 | - |
| 79 | IT+FR+ZER+NUL | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,ZERO,NULL) | HOLD,LOOP | 6 | - |
| 80 | IT+12+INF+ZER | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,INFO,ZERO) | HOLD,LOOP | 0 | - |
| 81 | IT+12+INF+NUL | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,INFO,NULL) | HOLD,LOOP | 0 | - |
| 82 | IT+12+ZER+NUL | 8 | 8 | - | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,ZERO,NULL) | HOLD,LOOP | 0 | - |
| 83 | IT+INF+ZER+NUL | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,INFO,ZERO,NULL) | HOLD,LOOP | 0 | - |
| 84 | SET+FR+12+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,INFO) | BITS,LOOP | 4 | 12/24 |
| 85 | SET+FR+12+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,ZERO) | BITS,LOOP | 4 | 12/12 |
| 86 | SET+FR+12+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,NULL) | BITS,LOOP | 4 | 12/12 |
| 87 | SET+FR+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,INFO,ZERO) | BITS,LOOP | 4 | 0/24 |
| 88 | SET+FR+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,INFO,NULL) | BITS,LOOP | 4 | 0/24 |
| 89 | SET+FR+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,ZERO,NULL) | BITS,LOOP | 4 | 0/12 |
| 90 | SET+12+INF+ZER | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,INFO,ZERO) | BITS,LOOP | 0 | 4/8 |
| 91 | SET+12+INF+NUL | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,INFO,NULL) | BITS,LOOP | 0 | 4/8 |
| 92 | SET+12+ZER+NUL | 12 | 12 | - | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,ZERO,NULL) | BITS,LOOP | 0 | 4/4 |
| 93 | SET+INF+ZER+NUL | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,INFO,ZERO,NULL) | BITS,LOOP | 0 | 0/8 |
| 94 | FR+12+INF+ZER | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,INFO,ZERO) | LOOP | 0 | - |
| 95 | FR+12+INF+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,INFO,NULL) | LOOP | 0 | - |
| 96 | FR+12+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,ZERO,NULL) | LOOP | 0 | - |
| 97 | FR+INF+ZER+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,INFO,ZERO,NULL) | LOOP | 0 | - |
| 98 | 12+INF+ZER+NUL | 8 | 4 | INFOS | - | L/L/OPEN/L/L/R-IF (H12,INFO,ZERO,NULL) | LOOP | 0 | - |
| 99 | IT+SET+FR+12+INF | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,INFO) | BITS,HOLD,LOOP | 20 | 12/48 |
| 100 | IT+SET+FR+12+ZER | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,ZERO) | BITS,HOLD,LOOP | 20 | 12/24 |
| 101 | IT+SET+FR+12+NUL | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,NULL) | BITS,HOLD,LOOP | 20 | 12/24 |
| 102 | IT+SET+FR+INF+ZER | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,INFO,ZERO) | BITS,HOLD,LOOP | 20 | 0/48 |
| 103 | IT+SET+FR+INF+NUL | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,INFO,NULL) | BITS,HOLD,LOOP | 20 | 0/48 |
| 104 | IT+SET+FR+ZER+NUL | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,ZERO,NULL) | BITS,HOLD,LOOP | 20 | 0/24 |
| 105 | IT+SET+12+INF+ZER | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,INFO,ZERO) | BITS,HOLD,LOOP | 2 | 4/16 |
| 106 | IT+SET+12+INF+NUL | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,INFO,NULL) | BITS,HOLD,LOOP | 2 | 4/16 |
| 107 | IT+SET+12+ZER+NUL | 24 | 20 | W2+ITE | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,ZERO,NULL) | BITS,HOLD,LOOP | 2 | 4/8 |
| 108 | IT+SET+INF+ZER+NUL | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,INFO,ZERO,NULL) | BITS,HOLD,LOOP | 2 | 0/16 |
| 109 | IT+FR+12+INF+ZER | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,INFO,ZERO) | HOLD,LOOP | 6 | - |
| 110 | IT+FR+12+INF+NUL | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,INFO,NULL) | HOLD,LOOP | 6 | - |
| 111 | IT+FR+12+ZER+NUL | 24 | 24 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,ZERO,NULL) | HOLD,LOOP | 6 | - |
| 112 | IT+FR+INF+ZER+NUL | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,INFO,ZERO,NULL) | HOLD,LOOP | 6 | - |
| 113 | IT+12+INF+ZER+NUL | 16 | 8 | INFOS | {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (ITB,H12,INFO,ZERO,NULL) | HOLD,LOOP | 0 | - |
| 114 | SET+FR+12+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,INFO,ZERO) | BITS,LOOP | 4 | 12/24 |
| 115 | SET+FR+12+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,INFO,NULL) | BITS,LOOP | 4 | 12/24 |
| 116 | SET+FR+12+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,ZERO,NULL) | BITS,LOOP | 4 | 12/12 |
| 117 | SET+FR+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,INFO,ZERO,NULL) | BITS,LOOP | 4 | 0/24 |
| 118 | SET+12+INF+ZER+NUL | 24 | 12 | INFOS | - | R-IF/L/OPEN/L/L/R-IF (W2,H12,INFO,ZERO,NULL) | BITS,LOOP | 0 | 4/8 |
| 119 | FR+12+INF+ZER+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | L/L/OPEN/L/L/R-IF (F1,H12,INFO,ZERO,NULL) | LOOP | 0 | - |
| 120 | IT+SET+FR+12+INF+ZER | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,INFO,ZERO) | BITS,HOLD,LOOP | 20 | 12/48 |
| 121 | IT+SET+FR+12+INF+NUL | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,INFO,NULL) | BITS,HOLD,LOOP | 20 | 12/48 |
| 122 | IT+SET+FR+12+ZER+NUL | 72 | 60 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,ZERO,NULL) | BITS,HOLD,LOOP | 20 | 12/24 |
| 123 | IT+SET+FR+INF+ZER+NUL | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,INFO,ZERO,NULL) | BITS,HOLD,LOOP | 20 | 0/48 |
| 124 | IT+SET+12+INF+ZER+NUL | 48 | 20 | INFOS; W2+ITE; W2+ITE+INFOS | {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,ITB,H12,INFO,ZERO,NULL) | BITS,HOLD,LOOP | 2 | 4/16 |
| 125 | IT+FR+12+INF+ZER+NUL | 48 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | L/NB-IF/OPEN/NB-IF/L/R-IF (F1,ITB,H12,INFO,ZERO,NULL) | HOLD,LOOP | 6 | - |
| 126 | SET+FR+12+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING} | R-IF/L/OPEN/L/L/R-IF (W2,F1,H12,INFO,ZERO,NULL) | BITS,LOOP | 4 | 12/24 |
| 127 | IT+SET+FR+12+INF+ZER+NUL | 144 | 60 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_MEASPHYS}; {N_QTOPO} | R-IF/NB-IF/OPEN/NB-IF/L/R-IF (W2,F1,ITB,H12,INFO,ZERO,NULL) | BITS,HOLD,LOOP | 20 | 12/48 |
| 128 | (readings only) | 3 | 3 | - | - | L/L/OPEN/L/L/R-IF (RI) | LOOP | 0 | - |

## 7. Not tested by instrument, with the reason (no silent caps)

Every variant is screened. At 1 ly, the **512 complementary variants** are covered by T-A through T-I, and the other
4,095 are not tested by instrument:

| reason (1 ly) | variants |
|---|---|
| INCONSISTENT: clash (c) or (d); nothing to test | 1,792 |
| SINGLE CONTRIBUTOR: one member's result covers the variant's; graded in that member's A-report | 1,440 |
| NO MEMBER CONTRIBUTION: nothing removed or not-bound by a member. Any removal is the board's under named premises, such as O-LOOP by the geometry. | 863 |

At 1 AU (1,152 W2 variants): 272 are complementary; the rest are 640 inconsistent, 96 single contributor and 144 with
no member contribution. The variant-by-variant list, with each reason, supports and premise clashes, comes from
`python3 combine.py --json PATH`.

## 8. Named hypotheses

**Conditional named premises** (assumed only inside a support; every support listed):

- **N_EPS**: ε > ε_any(L, N) for nlcontrol's Hamiltonian, not excluded by the Weinberg-family limit (NAMED-NOT-READ;
  an upper limit consistent with zero). It brings in A1's H-MAP, H-TRANSFER, H-SPIN and H-COHERE, and it is **tied to
  the distance cell**.
- **N_FRAME3b** (H-FRAME3b): a preferred slicing orders the drift's branching.
- **N_SIGKEY** (H-SIG-COR): the signal is keyed to that slicing.
- **N_CORR** (H-CORRIDOR-MODEL).
- **N_KEYING** (H-KEYING): the docket's addition to clause 1.
- **N_FRW**: H-FRW-EXACT + H-NOT-DE-SITTER. Perturbations break even the translations.
- **N_2BVIA** (H-2B-VIA-CORRIDOR).
- **N_QTOPO**: ITB's corridor is not a classical Lorentzian object. **No READ source.**
- **N_MS17**: MS p.17, READ. A non-traversable bridge only, Planckian for particle pairs.
- **N_MEASPHYS** (H-MEASURE-PHYSICAL): no instrument or source supplies it.
- **N_H12W** (H-12-CARRIER + H-12-W): no READ model.

**OPEN pathways** (never assumed in a removal):

- **N_XI**: ξ > 0.
- **N_EPSG**: KR p.13-14.
- **N_VAC**: vacuum entanglement as the pairs. Reznik READ; the window 0.91 L/c < T < L/c is DERIVED-FROM-READ.
- **N_EQUIL**: EGJ out of equilibrium, with H-IT and H-ZERO or H-NULL.
- **N_ILFREE**: the non-geometric corridor is made or held for free. No source.

**Encoding choices, named:**

- **Conventions.** W2 is C2 (H-C2): the drift acts on the branch pure state; under C1 there is no signal. Without a
  preferred slicing, C2 defines no channel.
- **O-MAKE and O-HOLD.**
  - The six-way O-MAKE split.
  - Geroch's with-a-CTC clause is not carried as an O-MAKE-TOPO pathway.
  - Under ITE, MS fn.1 commits the bridge to be non-traversable (not HELD).
  - R-INDEX releases nothing without H-IT.
- **Variants.**
  - A corridor network is present in every variant.
  - Absences are part of the variant (closed world). A support lists present members and named premises, with any
    member a premise presupposes added back.
  - A variant is complementary when no single member's own result covers it.
- **Carried through unchanged.** The work items' own named hypotheses: A1's §2 list; A2's H-CMB-IS-COSMIC and
  H-KILLING-SEARCH; A3's H-ALT, H-FAITHFUL and H-R; A4's H-QUDIT, H-ER=EPR, H-PATH and H_flat.

## 9. Sources

| source | status | used for |
|---|---|---|
| Maldacena & Susskind, arXiv:1306.0533v2 | READ (wave 1) | fn.1 p.2; §3.1 p.16; §3.2 pp.16-17; p.17 (N_MS17); §5.4 pp.36-37. Clash (c), B-LOCC, N_MS17. |
| Reznik, arXiv:quant-ph/0212044v2 | READ (wave 1) | p.1; p.10 (T < L/c); p.12 Fig. 2 (L/T < 1.1, T = 1, Ω = 9.5, one window). N_VAC; the window is DERIVED-FROM-READ. |
| Eling-Guedens-Jacobson, gr-qc/0602001v1 | READ by A4 (wave 2) | N_EQUIL, via `geometry.egj_fR_throat` |
| the four A-reports and their instruments (wave 2) | imported and re-run | every ground; each READ citation is the owning A-report's |
| LEDGER.md (S5, S10, S13; D23 as corrected in DOCKET 67), transit.py, emtension.py | read from the board, never written | B-RECV, B-LOCC, C-ITE, the midpoint first transit |

No source was re-read in this pass. No host refused a request.

## 10. Findings (recorded, not repaired)

1. **No consistent combination removes all five or makes them all NOT-BOUND.** The most is three (O-BITS REMOVED-IF,
   O-HOLD NOT-BOUND-IF, O-LOOP REMOVED-IF), in variants containing W2 and ITB. In removed-only terms the most is two.
   *Wave 1 first said* four of the six-way split, with O-HOLD REMOVED.
2. **O-MATTER survives every consistent variant, and the reason is a clash between the board and M.** H-INFO's
   sufficiency reading would remove it and is inconsistent with B-RECV in all 1,536 of its variants. *Wave 1 first
   said* "by a board holding none of the seven touches".
3. **O-MAKE-DIST survives every consistent variant.** It is OPEN via N_VAC only.
4. **O-HOLD and O-MAKE-TOPO are never removed.** Under H-IT they are NOT-BOUND-IF, and what the non-geometric corridor
   costs is OPEN (N_ILFREE). *Wave 1 first said* "The instruction's payoff is real and measured: O-HOLD falls only to
   H-IT and R-INDEX together". That came from B-THROAT's slip.
5. **O-LOOP's removal belongs to the exact-FRW geometry, not to any hypothesis.** It is REMOVED-IF {N_FRW, N_CORR} in
   every consistent variant without clause 2b. Clause 1 offers an alternative route only through the docket's keying.
   A1's attribution to H-SETTLE-W is a disagreement, explained above.
6. **H-FRAME's two clauses do not contradict each other as M states them.** The docket's keying (N_KEYING), or exact
   FRW, excludes clause 2b, and only if corridors are the route to the cosmic past. *Wave 1 first said* "M's H-FRAME
   sentence contradicts itself when both clauses are taken strong".
7. **ER=EPR with W2 is INCONSISTENT-AS-ENCODED.** A measured W2 signal on entangled pairs would test ER=EPR as MS
   state it. *Wave 1 first said* REFUTED.
8. **H-12 is the screen's only synergy.** At 1 AU it supplies the carrier that W2 alone lacks.
9. **The first transit can beat light with a midpoint source**, conditionally (N_EPS at the unread limit, H-C2,
   N_FRAME3b): 0.50153 yr after the source fires, against light's 1 yr. One-end distribution cannot. *Wave 1 first
   said* "The first cannot".
10. **Interference exists.** Clause 2b undoes the O-LOOP removal, and R-QUANTUM undoes ITB's non-binding. *Wave 1
    first said* none.

## 11. Testable predictions

- **{W2} with a preferred slicing.** Bob's mean σ_y shifts by tanh(2ε(T − t_A)), with t_A Alice's measurement time in
  the preferred slicing. The value is 0.537, 0.291 or 0 for t_A at the start, middle or end of his window (ε = 0.1,
  T = 3). Frames that order the events differently disagree, so the slicing is measurable through the signal.
- **W2 on partly entangled pairs (T-B).** The shift follows the shared entanglement: 0.240 at S = 0.53 bits, 0.042 at
  S = 0.13 bits, and exactly 0 for product pairs.
- **ITB.** None READ. ITB has no model that predicts anything beyond linear QM's no-signalling.
- **Any complete holder** of the 70 kg definition at R = 1 m has gravitating energy of at least 33-379 J,
  count-dependent. This is a floor on O-MATTER's holder, not a price.
