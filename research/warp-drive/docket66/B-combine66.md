# DOCKET 66 · B-combine66: the three D66 hypotheses in combination, with D68's members that bear

**Status: a docket work item, step 3 of the DOCKET 66 charter's order of work (2026-10-04), corrected at D66-fix the
same day.** Nothing here is seated. `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` are
untouched. The instrument is `combine66.py`, beside this file.

`PYTHONDONTWRITEBYTECODE=1 python3 combine66.py --selftest` runs **68 counted checks and passes all 68** (rc 0; z3,
sympy, numpy; four worker processes; about 16 min). **24 of them are controls.** **6 items cannot fail and are printed
STRUCTURAL, not counted** (section 2). The D66-fix run's first pass failed one check: the expectation written for the
reading `singok-board` (that it moves only variants holding a D68 throat) was wrong -- it also moves variants holding
no throat at all, where a throat is merely possible. The check now says what the reading does (O-MAKE-TOPO to OPEN via
N_WNCC, never in a variant holding a D66 throat); the screen was not changed. Wave 1 ran 58 checks with 20 controls.
`--json PATH` writes every variant; the D66-fix run's JSON is in the scratchpad (`d66/B-combine66-run-fix2.json`).

The encoding changed (section 0), so **`--conservative-full` was re-run: 8,192 compared (all 8,191 of
`combine.variants()` plus the empty board context), 0 differ** -- see the end of section 2 for its record.

M's standing instruction, verbatim from docket68/CHARTER.md: *"Remember that some of the hypothesies lined up for
docket 68 may turn out, after initial testing, to work better in combination."* The DOCKET 66 charter's step 3 reads:
"Combinations screened with D68's hypotheses, where one member removes an obstruction another leaves". M's hypotheses
are carried as hypotheses. Each grade says what a combination does, not whether it is true.

## 0. D66-fix: what the three verifier reports found, and what changed here

Every problem in the three wave-1 verifier reports (V66-0 against M, V66-1 for M, V66-2 reproduce) was applied or
answered with a computed or READ reason, in the A-report it belongs to (A1-defects.md, A2-throatbits.md, A3-qet.md,
each with its own table). The ones that touch this screen:

| verifier item | wave 1 encoded | D66-fix encodes | effect on the screen |
|---|---|---|---|
| V66-1 #1 (grade-moving): M **has** ruled on the singular throat (ledger M-S1A-P3: "APPLIED at the seat; a singular throat is not disqualified"; "the throat-creation classes stay OPEN") | E-SINGOK: the creation route N_WNCC credited to TBHOLO / TBTSH only; the board reading `singok-board` shown beside it as an open question "for M" | **the ruling applied to every D66 geometric throat** (DEF-TOPO/66 with DTHR, TBHOLO, TBTSH, TBTEL; N_WNCC's owners). A board ruling, applied -- not a question for M. Wave 1's encoding kept as the reading `singok-a2`, and the drift guard refuses it (mutation control) | O-MAKE-TOPO LEFT → OPEN via N_WNCC in the 48 single-reading variants with DTHR or TBTEL (`singok-a2` moves exactly those back) |
| V66-1 #1, second half | — | the ruling read as reaching **D68's own O-MAKE-TOPO** is the reading `singok-board`: it moves 174 single-reading/context variants, **20 of them D68-only** (RQ, ITJ, SHAPE, W2 x F1 and the empty board, where a throat is merely possible or D68's) | combine66 cannot change D68 rows under its conservative-extension rule (E-EXTEND). **Recorded for the D68 board, not repaired:** if M-S1A-P3 is a board ruling, D68's combine.py grades O-MAKE-TOPO LEFT where it would read OPEN via W-create-ncc |
| V66-0 #1 (grade-moving): GJW alone gives a brief opening, not a hold | TBTEL's AdS removal carried as A2's leading clause, one space OPEN via N_GJWAMB | A2 now grades **LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone**; the held AdS throat is Maldacena & Qi 1804.00491 (READ), outside the board's setting (E-ADS) | the drift row reads A2's new leading clause (OPEN by P9 = z3's OPEN via N_GJWPAY) |
| V66-1 #2 (grade-moving): the one-space GJW realisation exists | N_GJWAMB, "GJW p.14, stated, not computed" | **N_GJWPAY**: what Maldacena-Milekhin-Popov 1807.04726 (READ) shows -- a held one-space throat at sub-electroweak scale, REMOVED-IF its premises outside the board's setting by scale -- and does not show: a throat that admits the payload (binding energy = payload rest energy only below l_P; at r_fit N_f ≳ 1.4-1.8e14 massless charged species; `throatbits.mmp_scales`) | TBTEL's hold route renamed and re-grounded; tie, census and vacuity unchanged in shape |
| V66-1 #3 (grade-moving): the wall's causal structure is READ | N_WALLLOOP, a DEFEATING pathway: O-LOOP-S and the seat defeasible wherever DWALL appears | **N_WALLLOOP retired**: Minkowski T is a global time function of the M4-M4 wall (`defects.vis_time_function`, CGS p.15, Fig.4) | no wall-defeasible removal or seat remains (0 of 2,492; wave 1 had them in 28 / 120 / 40 / 172 variants by combination); mutation `wall-clean` replaced by `wall-loop` (a loop asserted at the wall), which the drift guard catches |
| V66-0 #7: N_XI, N_QEIC are the board's | B-HELD widened with QET ∧ (N_XI ∨ N_QEIC ∨ N_QETHAD); N_XI / N_QEIC counted among "every D66 pathway" | **QET ∧ N_QETHAD only**; N_XI and N_QEIC stay where the board puts them, with RQ. Wave 1's gating kept as the reading `qet-board-paths` | QET alone: O-HOLD OPEN via exactly [N_QETHAD] (GROUND check); `qet-board-paths` moves 8 variants, O-HOLD's via list only, never its verdict |
| V66-1 #7: R-LIT is not "M's sentence alone" | QLIT labelled "R-LIT: M's sentence alone" | **R-LIT is the question's parenthetical read as arrival alone**; M's sentence read operationally is R-QET | labels only; no verdict changes |
| A1's corrections (V66-0 #2, #3; V66-1 #4, #5; V66-2 #1-#3, #7) | — | N_DEFB's READ direction (wash-out, HK eq.(4.33); a supply only IF {CP violation, departure from equilibrium}, HK p.65) carried in its text; the global monopole's TURN, the gauge monopole's S-1 seat and the exact deficit are A1's (outside the screen's atoms) | B66-DEFB text; grounds re-run from defects.py |
| (robustness) | the drift guard read stored scratchpad JSON (A1's written by hand) | **`report_grades()` asks the instruments at run time** (`defects.a1_grades()`, `throatbits.grades()`, `qet.grades()`) | a corrected instrument is what the guard reads; 85 rows, all anchored |

## The answer, first

**Member-attributed removals: at most ONE per account, in any consistent variant, and it is always O-BITS, by D68's
{W2, F1}.** No D66 hypothesis is load-bearing in any support. Counted inside one consistent premise set (an account),
at both screened cells:

- at **1 ly, N = 7**: 1,332 of 2,492 consistent D66 variants;
- at **1 AU, N = 7**: 1,332 of 1,332 consistent W2 × F1 variants. Only support 2 (N_W2ANC) reaches here, because N_EPS
  is a premise clash in all 1,332, the window being empty.

Seven combinations of H-DEFECT-SEAT, H-THROAT-BITS and H-QET-EXOTIC were screened. Each hypothesis was carried in every
reading its A-report graded (6 + 5 + 2 readings), and each reading-combination was screened with every context of the
D68 members that bear: H-IT none / ITB / ITE / ITJ × H-INFO-SHAPE × H-SETTLE W2 × H-FRAME F1 × R-QUANTUM. That is
3,496 D66 variants at 1 ly plus 32 context-only references, and 1,748 + 16 at 1 AU. Over all of them:

- **No D66 literal is load-bearing in any support of any removal or any non-binding.** The count is 0 in 2,492
  consistent variants at 1 ly and 0 in 1,332 at 1 AU (z3: each support's D66 members freed, the goal re-asked). One
  D66 literal does appear inside supports. R-LIT is in an O-BITS support in 448 variants at each cell, but only because
  R-LIT entails W2 under the closed world (B66-LIN: R-LIT needs a non-linear member, and W2 is the only one present).
  With R-LIT freed, the support's own {W2, F1} still removes O-BITS. A naive "member in a support" count would credit
  R-LIT with W2 × F1's removal. The load-bearing test refuses that credit, and a control shows the test can fail: a
  planted D66 removal is credited.
- **No combination removes or makes NOT-BOUND an obstruction that a member leaves.** The lifts that occur are D68's:
  - O-BITS, by W2 × F1 (its two supports, unchanged from docket68/B-combine.md);
  - O-MAKE-TOPO and O-HOLD, NOT-BOUND-IF {ITB; N_QTOPO}, or O-MAKE-TOPO by ITE + N_MS17;
  - both forms of O-LOOP, by the geometry or the board (REMOVED-IF {N_CORR, N_FRW}; REMOVED, or REMOVED-IF
    {N_SIGKEY}).
- **What the D66 hypotheses do in combination is three things, none of them a removal:**
  1. **They add OPEN pathways.** On O-SEAT: N_DEFB, for every string, wall or monopole seat (its READ direction is
     wash-out; a supply needs CP violation and a departure from equilibrium). On O-HOLD: N_NEGT (string-supported
     throat), N_GJWPAY (a payload-admitting one-space throat beyond MMP's SM-field family), N_PINCH (a singular throat
     outside the thin-shell / static set) and N_QETHAD (QET outside the Hadamard class) -- QET contributes only
     N_QETHAD; N_XI and N_QEIC are the board's, appearing only with RQ. On O-MAKE-TOPO: N_WNCC (specthm's W-create-ncc,
     OPEN at its owner), now for **every** D66 geometric throat under M's ruling. **A union of OPEN pathways is not a
     removal**, and in no combination does one member's pathway close another member's gap.
  2. **They interfere.** Every geometric-throat reading (DTHR, TBHOLO, TBTSH, TBTEL) makes N_QTOPO a premise clash
     beside ITB, so ITB's two non-bindings (O-MAKE-TOPO, O-HOLD) fall. This is exactly what R-QUANTUM's throat does in
     D68. It appears in every one of the seven combinations that holds a throat reading together with ITB.
  3. **They make removals defeasible -- through a held throat only.** Signal O-LOOP-S and the seat condition
     M-S1A-P3 (i) become defeasible only where the string-supported throat DTHR is present: once held (by any pathway
     that can hold a throat), it is a time machine unless the mouths balance. The FKZ conditional is CONTENT: with the
     throat held, the seat is free given N_MBAL, and a seat loop is FORCED without it. *Wave 1 also made every wall seat
     defeasible through N_WALLLOOP; the wall's time function is now computed and that pathway is retired.*
- **Survivors of every consistent variant, both cells:**
  - **O-SEAT** is lifted in none. It is OPEN via {N_S5, N_DEFB} in exactly the consistent variants holding a string,
    wall or monopole: 1,440 at 1 ly and 768 at 1 AU. It is OPEN via N_S5 alone in every other: 1,052 and 564. Under
    the named reading H-SEAT-ROUTES it is LEFT, in all 356 consistent single-reading and context variants re-screened.
  - **O-MAKE-DIST** is lifted in none. It is OPEN via N_VACNP alone (1,160 at 1 ly), or via N_NLDIST, N_W2WEAK and
    N_VACNP with W2 × F1 (1,332 at 1 ly; all 1,332 at 1 AU).
- **R-LIT (the question's parenthetical, arrival alone) is inconsistent wherever no non-linear member is present.** Its
  clash core is C-QLIT + B66-ARR + B66-LIN (+ B-DCTC), in 588 variants at 1 ly, and with ITE (C-ITE's linearity) in 280
  more. With W2 the encoding no longer refutes it. That is consistency by the absence of a refutation (STRUCTURAL),
  because nothing computes arrival-alone energy under a non-linear dynamics. It moves no obstruction: R-LIT is SILENT
  on all six, and is load-bearing nowhere. M's own sentence, read operationally, is R-QET (TRUE-IF its four named
  hypotheses); *wave 1 labelled R-LIT "M's sentence alone".*

**What this says about M's standing instruction for DOCKET 66.** It was tested, and on every obstruction the D66
hypotheses do not work better in combination, either among themselves or with D68's bearing members. The nearest
approaches are named in section 5 (A1's F8 defect core × TEMPLATE; R-TELEPORT × QET; R-LIT × W2). Each is computed,
and each leaves the grade where it was. The D66-fix moved no headline: 0 D66 load-bearing removals and non-bindings,
at most one member-attributed removal per account, the same two survivors.

## 1. What was built

| item | value |
|---|---|
| D66 readings | H-DEFECT-SEAT: DSTR (static straight string), DWALL (thin VIS wall, Lambda = 0 both sides), DGMON (global monopole), DMON (gauge monopole exterior), DTEX (texture), DTHR (a defect as the throat's support). H-THROAT-BITS: TBHOLO, TBTSH, TBTEL, TBISL, TBITB (R-HOLO, R-THINSHELL, R-TELEPORT, R-ISLAND, R-ITB). H-QET-EXOTIC: QET (R-QET), QLIT (R-LIT, the parenthetical's arrival-alone reading) |
| reading-combinations | 125 over the 7 combinations (6 + 5 + 2 + 30 + 12 + 10 + 60) |
| D68 contexts (members that bear) | H-IT {none, ITB, ITE, ITJ} × H-INFO-SHAPE {−, +} × W2 × F1 {−, +} × R-QUANTUM {−, +} = 32. The S5 seat route is the board's OPEN pathway N_S5, present in every variant |
| R-ITB | screened WITH D68's ITB (A2: "adds the location only"). With ITE / ITJ it would be two readings of H-IT at once, which D68 never forms: 336 NOT TESTED (section 6). The none / ITB contexts coincide and are deduplicated |
| variants | 1 ly, N = 7: 3,496 D66 + 32 context-only = 3,528. 1 AU, N = 7: every W2 × F1 variant, 1,748 + 16 = 1,764 |
| per variant | combine's verdict per obstruction (7 forms) with every minimal support, accounts, premise clashes, OPEN status; plus, new here: the vacuity flag, D66 load-bearing, defeasibility of every removal, and the seat condition |

**The encoding: DOCKET 66's commitments as tracked constraints with grounds.** Each holding below is a tracked
constraint carrying its ground. Every ground is re-run in the selftest from its owner (section 2, GROUNDS).

| name | constraint | ground |
|---|---|---|
| C-DTHR, C-TBHOLO, C-TBTSH, C-TBTEL | the reading ⇒ THROAT (a geometric throat) | A1: every string-supported throat read is a Lorentzian wormhole. A2: R-HOLO's sphere is geometry; PV gr-qc/9506083v1 p.1, distributional curvature on a complete manifold; GJW/MSY's bridge is geometry (encoding E-THROAT) |
| C-DTEX | DTEX ⇒ ¬N_SEATPERSIST | `defects.derrick(3)`: no stationary point (control: d = 1 admits one). DURRER Table 1, as READ by A1 |
| C-QLIT | QLIT ⇒ ARRNEG (arrival-alone negative energy) | A3 R-LIT, the parenthetical's arrival-alone reading |
| B66-ARR | ARRNEG ⇒ ¬LIN | A3 / `qet.post_alice`: after the bit arrives and before Bob acts, the local energy at B is 0 (re-run: \|.\| < 1e-12). Hotta 0803.2272v3 p.14 as READ by A3 |
| B66-LIN | ¬LIN ⇒ W2 ∨ W1 ∨ KR ∨ CAPD | encoding E-LIN: QM is linear unless a member commits a non-linear dynamics. combine left LIN free where nothing named it, while R-LIT's FALSE-IF is scoped to linear QM (A3) |
| B66-DEFB | DEFBSUP ⇒ (DSTR ∨ DWALL ∨ DGMON ∨ DMON) ∧ N_DEFB | A1 / `defects.grades`: "O-SEAT, defect at the seat: OPEN via N_S5 \| N_DEFB". HK pp.63-65 as READ by A1 (the direction READ is wash-out) |
| B66-FKZ | CTCW ⇔ DTHR ∧ HELD ∧ ¬N_MBAL | FKZ 2305.03887 as READ by A1. `defects.figures`: T ≈ 1.44e9 yr for an Earth-mass shell, L = 1 ly |
| B66-CTCW | CTCW ⇒ LOOPS | a wormhole time machine is a closed causal curve |
| B66-WALL | (empty; the control `wall-loop` asserts DWALL ⇒ LOOPS) | `defects.vis_time_function`: Minkowski T a global time function. *Wave 1: DWALL ∧ N_WALLLOOP ⇒ LOOPS* |
| B66-SEAT | SEATLOOP ⇒ CTC ∨ CTCW ∨ (TB ∧ ¬N_SEATOFF) ∨ ((QET ∨ QLIT) ∧ ¬N_FLATQFT); and CTC ∨ CTCW ⇒ SEATLOOP | M-S1A-P3 (i) at the seat. `defects.static_is_stably_causal` (g^tt < 0 for the static seats), `defects.vis_time_function` (the wall seat). A2's H-SEAT-OFF-THROAT; A3's H-FLAT-QFT. combine's CTC is at Bob (B-DCTC) |
| B-HELD/66 (widened) | HELD ⇒ combine's held ∨ DTHR ∧ N_NEGT ∨ TBTEL ∧ N_GJWPAY ∨ (TBHOLO ∨ TBTSH) ∧ N_PINCH ∨ QET ∧ N_QETHAD | `defects.canonical_nec` (T_kk a sum of squares; phantom control). `throatbits.pv_static` (σ0 < 0 at every a0 > 2M). `throatbits.mmp_scales` (MMP's binding energy against the payload). `geometry.r_quantum` (2.0811e-68 of the 1 m deficit). A2 E-ADS. *Wave 1: TBTEL ∧ N_GJWAMB; QET ∧ (N_XI ∨ N_QEIC ∨ N_QETHAD)* |
| B-SIGLOOP/66 (widened) | combine's antecedent ∧ ¬CTCW ⇒ ¬LOOPS | as above. *Wave 1 also required ¬(DWALL ∧ N_WALLLOOP)* |
| DEF-SEAT/66 (widened) | rm(O-SEAT) ⇔ combine's rhs ∨ DEFBSUP (unchanged under H-SEAT-ROUTES) | A1 |
| DEF-TOPO/66 (widened) | rm(O-MAKE-TOPO) ⇔ combine's rhs ∨ (DTHR ∨ TBHOLO ∨ TBTSH ∨ TBTEL) ∧ N_WNCC | ledger M-S1A-P3 (read at run time); A1's and A2's grades; specthm W-create-ncc = OPEN, asked at run time. *Wave 1: (TBHOLO ∨ TBTSH) ∧ N_WNCC* |

The four widened items are built from **combine's own terms**. Each term is read out of combine's expression
(Implies(HELD, held) → held, and so on), its shape is asserted, and the original's indicator is dropped from the
assumptions. Nothing of combine is retyped.

**Named premises** (assumed only inside a support): N_MBAL (H-MASS-BALANCE), N_SEATOFF (H-SEAT-OFF-THROAT), N_FLATQFT
(H-FLAT-QFT), N_SEATPERSIST (H-SEAT-PERSISTS).

**OPEN pathways** (held false in every support and account): N_DEFB, N_NEGT, N_GJWPAY, N_PINCH, N_QETHAD, N_WNCC, all
opening. Each is tied to its owner literal (section 2, ties). **Retired** (`combine66.RETIRED`, with the reason):
N_WALLLOOP (computed) and N_GJWAMB (replaced by N_GJWPAY).

**Encoding choices, each named:**

- **E-EXTEND.** combine's vocabulary is extended in process only, with no file edited. It is guarded by the
  conservative-extension check.
- **E-THROAT.** As in the table above.
- **E-ADS.** Held throats outside the board's one-space setting (Maldacena-Qi's nearly-AdS2; MMP's sub-electroweak
  scale) are carried as A2's text; the payload-admitting one-space clause is screened as N_GJWPAY.
- **E-SINGOK-RULED** (D66-fix). M's singular-throat ruling is applied to every D66 geometric throat. Readings on
  record: `singok-a2` (wave 1's E-SINGOK) and `singok-board` (the ruling reaching D68's throats as well).
- **E-FKZ.** For DTHR only, as A1 graded it. Reading `fkz-generic` applies it to every held throat.
- **E-LIN.** As in the table above.
- **E-SEATOFF-ALL.** H-SEAT-OFF-THROAT is applied to all five TB readings. A2's seat text names R-HOLO and R-THINSHELL
  and says R-TELEPORT "adds GJW p.13 (no CTC)". It says nothing for R-ISLAND or R-ITB, where the closure only adds a
  condition.
- **E-DEFB.** N_DEFB is given to the four classes A1 grades "OPEN via N_S5 | N_DEFB" (READ for strings and gauge
  monopoles; for walls and global monopoles OPEN as unchecked). The texture and the throat-support row grade no supply.

## 2. Guards (the screen refuses to report if any fails)

- **Vacuity** (PROOF-ASSISTANT.md):
  - the board is SAT;
  - 12 of 13 D66 readings are SAT alone, R-LIT not (content);
  - D66's named premises are jointly SAT with the board and with DTHR / TBHOLO / QET, OPEN pathways false;
  - each D66 pathway is SAT with its owner;
  - **every consistent variant at both cells is SAT with every OPEN pathway false.** The engine computes supports with
    OPEN pathways false, so a variant consistent only through one would report vacuous removals.
  - CONTROL: the planted `open-forced` (QET forced to need N_QETHAD) trips the flag, and the engine then does report a
    vacuous REMOVED. The guard is what stops it.
- **Conservative extension.** In the selftest, 368 D68 variants (every 24th of `combine.variants()` plus the 32
  contexts) were screened by combine under its own vocabulary and by D66Screen under the extended one. 0 differ in
  signature (verdict, OPEN via, NB beside, premise-clash sets) or in the supports of any lift. The full run over all
  8,191 is recorded at the end of this section.
- **Encoding drift.** 85 rows compare z3's class with the D66 A-reports' own grade text, **asked of the instruments at
  run time** (`defects.a1_grades()`, `throatbits.grades()`, `qet.grades()`; wave 1 read stored scratchpad JSON).
  - **All 85 fragments are anchored verbatim** in the instruments' text. Each is parsed by
    `combine.parse_report_class` (P1, P8, P9) or by SEAT_PARSE.
  - **83 agree**, and the 2 disagreements are explained:
    - (A2, R-ISLAND, O-BITS) is vocabulary. "LEFT-IF {H-ISLAND-COUNTERPART}" reads OPEN by combine's P9, but the
      condition is the reading's own identification, with no pathway outside it, so z3 gives LEFT. Both sides say O-BITS
      is not removed.
    - (A1, throat support, seat) is a presupposition. A1's "M-S1A-P3 (i) disqualifies it unless the masses balance" is
      about the held throat its own O-HOLD grade makes OPEN. The conditional itself is the CONTENT check above.
  - New or changed rows at D66-fix: the wall's O-LOOP ("none") and seat ("PASSES under H-VIS-MINKOWSKI"); DTHR's
    O-MAKE-TOPO ("OPEN via N_WNCC"); R-TELEPORT's two O-HOLD clauses (GJW alone; the payload-admitting one-space throat)
    and its O-MAKE-TOPO without ITE. Wave 1's Z7 rule (a removal defeasible via the graded literal's own pathway reads
    {N, OPEN}) is kept in the code; after N_WALLLOOP's retirement no drift row needs it.
  - **Seven mutated encodings, each caught** as an unexplained disagreement: `defb-asserted` (10 rows),
    `negt-asserted` (1), `gjw-ads` (the AdS hold imported to one space, 2), `qet-holds` (1), `wall-loop` (a loop
    asserted at the wall, 1; replaces wave 1's `wall-clean`), `qlit-free` (1) and `singok-a2` (wave 1's E-SINGOK
    against the corrected reports, 2).
  - `defects.grades()`, A1's own z3, agrees on O-HOLD (OPEN via exactly [N_NEGT]), on O-SEAT (OPEN via exactly
    {N_DEFB, N_S5}), on the static seat (PASSES = SATISFIED, not defeasible) and on the made throat's O-MAKE-TOPO (OPEN
    via exactly [N_WNCC]).
- **Pathway ties (6 controls).** Each D66 pathway opens only with its owner. N_DEFB opens O-SEAT with DSTR and not with
  QET. N_NEGT opens O-HOLD with DTHR, not DSTR. N_GJWPAY opens it with TBTEL, not TBISL. N_PINCH opens it with TBTSH,
  not TBTEL. N_QETHAD opens it with QET, not TBISL. N_WNCC opens O-MAKE-TOPO with DTHR (the reading M's ruling newly
  covers), not QET. *Wave 1 had a seventh tie, N_WALLLOOP; that pathway is retired.*
- **Load-bearing.** A D66 literal counts only if the goal fails when the D66 members of the support are freed. CONTROL:
  under `defb-asserted`, DSTR's O-SEAT reads REMOVED and is credited to DSTR.
- **GROUNDS, re-run from their owners:**
  - `defects.canonical_nec` (+ phantom control); `defects.static_is_stably_causal`; `defects.derrick` (+ d = 1 control);
  - D66-fix: `defects.vis_time_function` (+ the R control; and the screen's DWALL seat SATISFIED with no defeat),
    `defects.monopole_conjugate` (+ halved-curvature control), `defects.gauge_monopole_lens` (+ 1e-27 kg control),
    ledger M-S1A-P3's ruling text with `defects.grades` and the screen's DTHR O-MAKE-TOPO (OPEN via [N_WNCC]),
    `throatbits.mmp_scales` (+ the (5.31)-without-π^(3/2) control), and QET alone OPEN via exactly [N_QETHAD];
  - `throatbits.pv_static` and `pv_conservation` (+ flipped control);
  - specthm's verdicts via `throatbits.specthm_verdicts` (S-1 NONEMPTY; S-2, S-3, Rec, W-create-cc, W-create-ncc,
    W-enlarge OPEN);
  - qet's arrival-alone 0, E_B = 0.14252 (control; raw model units) and no-signalling < 1e-14;
  - `geometry.r_quantum` 2.0811e-68;
  - `massform.derive_readings` (TEMPLATE REFUSED on C1 alone; STANDS with C1's link holding), `READING_REASONS`
    (TEMPLATE makes no new baryon number) and HELD_SEAT_ROUTE (forms no baryons);
  - `seat.grade_o_seat` = OPEN.
- **STRUCTURAL, printed and not counted:**
  - the widened terms are combine's own;
  - TBISL and TBITB are inert on every obstruction atom (seat closure only);
  - R-LIT with W2 is consistent by absence of a refutation;
  - OPEN pathways are held false in supports (combine's engine), and every D66 pathway is tied to an owner;
  - the 1 AU N = 1e3 / 1e6 and 4.2465 ly cells are board equalities that no D66 commitment touches;
  - (D66-fix) the wall supplies no loop by encoding; its CONTENT is `defects.vis_time_function`, re-run in the grounds.

**Full conservative-extension run** (`python3 combine66.py --conservative-full`, D66-fix encoding): **8,192 compared
(all 8,191 of `combine.variants()` plus the empty board context), 0 differ.** With every D66 literal absent, the
extended screen is combine's screen. (Wave 1's encoding: the same 8,192, 0 differ, 1,750 s.)

## 3. Results in detail (1 ly, N = 7; the 1 AU figures follow each)

**Consistency.** 2,492 of 3,496 consistent; 1,332 of 1,748 at 1 AU (unchanged from wave 1).

Clash cores, counted by variant (a variant may carry more than one):

| core | 1 ly | 1 AU | reading |
|---|---|---|---|
| C-QLIT + B66-ARR + B66-LIN + B-DCTC | 588 | — | R-LIT with no non-linear member: FALSE-IF in linear QM (A3) |
| C-QLIT + B66-ARR + C-ITE | 280 | 140 | R-LIT against ER=EPR's linearity (MS sec.5.4, as D68 encodes it) |
| C-ITE + C-W2 (linearity) | 416 | 416 | D68's clash (c), inherited |
| C-ITE + B-GISIN + C-F1 | 416 | 416 | D68's clash (c), second core, inherited |

Premise clashes in consistent variants:

| premise clash | 1 ly | 1 AU | reading |
|---|---|---|---|
| {N_QTOPO} | 656 | 394 | geometric-throat readings (or RQ) beside ITB |
| {N_CORR, N_QTOPO} | 176 | 106 | D68's own |
| {N_SEATPERSIST} | 360 | 192 | the texture: "EMPTY IF {H-SEAT-PERSISTS}" |
| {N_EPS} | — | 1,332 | the empty window |

**Lifts, by what** (consistent variants). The final column is the D66 literal in a support but not load-bearing.

| form | lifted | D66 load-bearing | D68 member only | no member | entailment only |
|---|---|---|---|---|---|
| O-BITS | 1,332 | **0** | 884 | 0 | 448 |
| O-MAKE-TOPO | 452 | **0** | 452 | 0 | 0 |
| O-HOLD | 176 | **0** | 176 | 0 | 0 |
| O-LOOP-C | 2,492 | **0** | 1,402 | 1,090 | 0 |
| O-LOOP-S | 2,492 | **0** | 0 | 2,492 | 0 |

At 1 AU: O-BITS 1,332 (0 / 884 / 448), O-MAKE-TOPO and O-HOLD 106 each, O-LOOP-C and O-LOOP-S 1,332. O-MAKE-DIST and
O-SEAT are lifted in none.

**Headline maxima** (per account, never across two):

| figure | maximum | variants | smallest |
|---|---|---|---|
| member-attributed removals | 1, always O-BITS by {W2, F1} | 1,332 | {DSTR, W2, F1} |
| not-bound | 2 | 176 at 1 ly; 106 at 1 AU | {DSTR, ITB} |
| D66-attributed removals | 0 | — | — |
| D66-attributed non-bindings | 0 | — | — |

The not-bound pair is O-MAKE-TOPO and O-HOLD, from ITB with a D66 reading that commits no throat.

**Per combination** (1 ly). "Interference" lists D68 lifts that the D66 literal undoes; "new OPEN" lists pathways not
present in the same variant without its D66 literals.

| combination | variants / consistent | D66 load-bearing lifts | interference | new OPEN | removals made defeasible | seat |
|---|---|---|---|---|---|---|
| H-DEFECT-SEAT | 192 / 168 | 0 | ITB's TOPO + HOLD by DTHR (4) | O-SEAT N_DEFB (112); O-MAKE-TOPO N_WNCC (28); O-HOLD N_NEGT (24) | O-LOOP-S via N_NEGT (24), N_XI / N_QEIC (12), N_EQUIL (8) -- all with DTHR | SATISFIED 144; SATISFIED but defeasible 24 |
| H-THROAT-BITS | 136 / 120 | 0 | ITB's TOPO + HOLD by TBHOLO, TBTSH, TBTEL (4 each) | O-MAKE-TOPO N_WNCC (84); O-HOLD N_PINCH (48), N_GJWPAY (24) | none | SATISFIED-IF {N_SEATOFF} 120 |
| H-QET-EXOTIC | 64 / 40 | 0 | none | O-HOLD N_QETHAD (24) | none | SATISFIED-IF {N_FLATQFT} 40 |
| DS × TB | 816 / 720 | 0 | by TBHOLO / TBTSH / TBTEL (20 each), DTHR (8), jointly (12) | N_WNCC 540, N_DEFB 480, N_PINCH 288, N_GJWPAY 144, N_NEGT 104 | O-LOOP-S via N_NEGT 104, N_XI / N_QEIC 52, N_PINCH 48, N_EQUIL 32, N_GJWPAY 24 | SATISFIED-IF 616; defeasible 104 |
| DS × QE | 384 / 240 | 0 | by DTHR (6) | N_DEFB 160, N_QETHAD 144, N_WNCC 40, N_NEGT 36 | O-LOOP-S via N_NEGT 36, N_QETHAD 24, N_XI / N_QEIC 18, N_EQUIL 12 | SATISFIED-IF 204; defeasible 36 |
| TB × QE | 272 / 172 | 0 | by TBHOLO / TBTSH / TBTEL (6 each) | N_WNCC 120, N_QETHAD 104, N_PINCH 72, N_GJWPAY 36 | none | SATISFIED-IF 172 |
| DS × TB × QE | 1,632 / 1,032 | 0 | by TBHOLO / TBTSH / TBTEL (30 each), DTHR (12), jointly (18) | N_WNCC 772, N_DEFB 688, N_QETHAD 624, N_PINCH 432, N_GJWPAY 216, N_NEGT 156 | O-LOOP-S via N_NEGT 156, N_QETHAD 104, N_XI / N_QEIC 78, N_PINCH 72, N_EQUIL 48, N_GJWPAY 36 | SATISFIED-IF 876; defeasible 156 |

The number after each pathway is the count of variants. "Jointly" means two throat readings are present, each
sufficient, so no single D66 literal restores the lift. N_XI and N_QEIC appear among the defeating pathways only where
RQ (the board's R-QUANTUM) is in the context, beside DTHR; they are not new OPEN pathways of any D66 reading. The TB × QE
row has no defeasible removal because the FKZ loop is encoded for DTHR only (E-FKZ); reading `fkz-generic` adds them
(section 4).

*Wave 1's figures, for the record:* new OPEN N_WNCC 56 / 336 / 80 / 480 in the TB / DS × TB / TB × QE / triple rows
(TBHOLO, TBTSH only); N_XI / N_QEIC counted among the D66 pathways (12 / 72 / 52 / 312); seats defeasible 52 / 224 / 76
/ 328 in the DS / DS × TB / DS × QE / triple rows, the wall's N_WALLLOOP included.

**The seat condition M-S1A-P3 (i).** It is VIOLATED in no consistent variant. F2b, the only D68 member with a CTC at
Bob, is not among the bearing members (section 6). Every variant reads SATISFIED, or SATISFIED-IF {N_SEATOFF} and/or
{N_FLATQFT}. 320 of the 2,492 at 1 ly (192 of 1,332 at 1 AU) are defeasible, every one through a pathway that can hold
the throat (N_NEGT, N_GJWPAY, N_PINCH, N_QETHAD, and the board's N_XI, N_QEIC, N_EQUIL), and **every one holds DTHR**
(FKZ, E-FKZ; checked over the run JSON: 0 defeasible seats without DTHR). No wall seat is defeasible. The full census
is in the JSON (key `1 ly.seat`).

**Pathway census** (consistent variants at 1 ly, on which form): N_DEFB on O-SEAT 1,440; N_WNCC on O-MAKE-TOPO 1,584;
on O-HOLD N_QETHAD 896, N_PINCH 840, N_GJWPAY 420, N_NEGT 320, each defeating O-LOOP-S and the seat only beside DTHR
(N_NEGT 320, N_QETHAD 128, N_PINCH 120, N_GJWPAY 60). At 1 AU: 768; 840; 448, 504, 252, 192.

## 4. Readings under the guard (alternatives on record, not mutations)

Each was run on the 424 single-reading and context-only variants.

| reading | rows moved | what it moves |
|---|---|---|
| **H-SEAT-ROUTES** (supply restricted to S10 and S13) | 356 consistent variants: 28 context-only and 328 with a D66 reading | O-SEAT OPEN → **LEFT** in every one, the N_DEFB route included (DEF-SEAT unwidened). A defect seat does not reopen S10 or S13 (see section 5) |
| **singok-a2** (wave 1's E-SINGOK: the creation route for TBHOLO / TBTSH only) | 48, none context-only | O-MAKE-TOPO OPEN via N_WNCC → **LEFT** for DTHR and TBTEL variants: what the ruling, now applied, changed. Also a drift mutation, caught |
| **singok-board** (M's ruling reaching every geometric throat, D68's included) | 174, of which 20 context-only | O-MAKE-TOPO LEFT → OPEN via N_WNCC, only in variants holding **no** D66 throat (where a throat is merely possible, or is D68's RQ / ITJ). combine66 does not adopt it: it would change D68's own rows (E-EXTEND). Recorded for the D68 board. *Wave 1: 222, of which 20 context-only; the other 48 are now the adopted encoding* |
| **fkz-generic** (FKZ for every held throat) | 440 moves in 220 distinct variants, of which 16 context-only (RQ, ITJ) | only defeasibility: O-LOOP-S and the seat become defeasible via the hold's pathways. No verdict word moves |
| **qet-board-paths** (wave 1's gating of N_XI / N_QEIC through QET) | 8 | O-HOLD's via list gains N_XI, N_QEIC in QET variants without RQ; the verdict (OPEN) never moves |
| **H-SM-ONLY** | all 2,520 variants holding a string, wall, monopole or string-supported throat become inconsistent | A1: S^3 has π0 = π1 = π2 = 0 (HK p.36, DURRER p.4, as READ by A1) |

## 5. The combinations the A-reports named for this step, each answered from the screen

| candidate (named by) | what the screen computes |
|---|---|
| defect seat × H-THROAT-BITS: "M-S1A-P3 (i) allows a singular ring throat, but it still needs N_NEGT" (A1) | {DTHR, TBHOLO}: O-HOLD OPEN via {N_NEGT, N_PINCH}, a union of two pathways, neither closing the other. O-MAKE-TOPO OPEN via N_WNCC (both readings' under M's ruling). O-LOOP-S defeasible via both (FKZ). Seat SATISFIED-IF {N_SEATOFF}. No removal |
| defect core × S13, topological hold vs H-RELEASE (A1 F8) | GROUND (massform imported): TEMPLATE is refused on C1 alone, and with C1's link holding it STANDS. At a defect core \|φ\| = 0 is held with no local source, so C1's P-UNIFORM ground fails there. Restoration still fails by topology: only annihilation ends it, releasing μc² (A1 F8). TEMPLATE also "makes no new baryon number" and the held-seat route forms no baryons, so a defect-core TEMPLATE is not a supply of substance. **The ground of the refusal moves (P-UNIFORM → topology); the screen grade does not** (B-S10, B-S13 bare) |
| defect seat × H-QET-EXOTIC (A1) | {DTHR, QET}: O-HOLD OPEN via {N_NEGT, N_QETHAD} (and the board's N_XI, N_QEIC with RQ). Two pathways side by side. QET covers at most 2.08e-68 of the 1 m throat's deficit (`geometry.r_quantum`, re-run), and N_NEGT stays as A1 left it (no mechanism known). No ratio between the two is computed here. With DS4: O-SEAT OPEN via {N_S5, N_DEFB}; QET adds no supply (LEFT-IF {H-QET-BUDGET}) |
| R-TELEPORT × W2 × F1 on O-BITS (A2) | {TBTEL, W2, F1}: O-BITS REMOVED-IF by W2 × F1's two supports; TBTEL is in no support. GJW's coupling is O-BITS's channel at ≤ c; with W2 × F1 the channel is W2 × F1's, not TBTEL's |
| R-ITB × D68 ITB (A2) | R-ITB carries ITB. NOT-BOUND-IF {ITB; N_QTOPO} on O-MAKE-TOPO, O-HOLD and O-LOOP-C, credited to ITB; TBITB is inert (location only). Agrees with A2's "every non-binding here is H-IT's" |
| R-TELEPORT × H-QET-EXOTIC: can arriving-information negative energy be the throat's ANEC deficit? (A2, A3) | {TBTEL, QET}: O-HOLD OPEN via {N_GJWPAY, N_QETHAD}. QET's states are QEI-bound (LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}); QET's negative density is local and offset (FMM p.3), not an averaged violation (A3, V66-0 #6). GJW alone gives an opening, not a hold; held throats (MQ, MMP) lie outside the board's setting (E-ADS), and MMP's does not admit the payload. No pathway of one closes the other's. Whether GJW's negative ANEC is itself QET-like is not read here: OPEN |
| R-QET × H-THROAT-BITS / H-INFO-SHAPE: bits pushed to the seat and used there (A3) | {QET, SHAPE}, {QET, TBTEL, SHAPE}: O-SEAT OPEN via N_S5 only; QET relocates at most E_A, gated by a bit at ≤ c (A3). No supply, no grade moved |
| R-LIT × a non-linear member (found here) | R-LIT's FALSE-IF is scoped to linear QM. With W2 it is no longer refuted, by absence of a refutation, and it is load-bearing nowhere. Named: **N_QLITNL** (in a non-linear dynamics the arrival alone creates negative energy), computed nowhere, candidate only |

## 6. Not tested, with the reason (no silent caps)

- **R-ITB with ITE or ITJ: 336 variants.** These would be two readings of H-IT at once, which D68's screen never forms.
- **D68 members outside the task's bearing list:**
  - W1 and KR: W1 signals nothing; KR's open branch N_EPSG would add a hold pathway beside RQ's.
  - F2b: its D-CTC is at Bob, so the seat condition would read VIOLATED-IF {N_DCTC}; not in the list.
  - F1 alone and W2 alone: the pair is the listed member. W2 alone appears only as R-LIT's companion in the drift rows.
  - H12: bears only on the ε window (N_EPS), which no D66 commitment touches.
  - INFO, ZERO, NULL: inert in combine.
  - INFOS: clashes with B-RECV in every variant (clash (d); M ruled for SHAPE).
  - R-INDEX: its NONGEO route ITB + RI + N_MEASPHYS would meet the same premise clash as N_QTOPO beside a throat
    reading.
- **Two readings of one D66 hypothesis at once** (two defects at one seat; two throat readings): not generated, as in
  D68.
- **The 1 AU N = 1e3 / 1e6 and 4.2465 ly cells:** board equalities (STRUCTURAL).
- **specthm's classes and the Sturm condition** are not re-derived per combination. No D66 reading enters specthm's
  axioms; A1, A2 and A3 each found them unmoved except A1's gauge-monopole S-1 placement (named hypotheses; outside the
  screen's atoms), and the grounds re-ask specthm once.
- **H-SEAT-S12** (QET's energy fed to the pair route): adopted nowhere.
- **H-SINGULAR-IS-PINCH** is carried only as the OPEN pathway N_PINCH, because A2 did not model it.
- **Walls with an AdS side** (CGS's identification CTCs): outside DWALL's reading (H-VIS-MINKOWSKI).

## 7. Named hypotheses (every limitation)

- **D66's own:**
  - H-CANONICAL, H-THIN, H-STATIC-STRING, H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION, H-SM-ONLY, H-SEAT-PERSISTS
    (N_SEATPERSIST), H-VIS-MINKOWSKI, H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM;
  - H-SINGULAR-IS-THINSHELL, H-PV-STATIC, H-SEAT-OFF-THROAT (N_SEATOFF);
  - H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED; H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, H-MQ-LARGE-N; H-MMP, H-SM-FIELDS,
    H-MMP-G, H-MMP-OOM;
  - H-GROUND, H-CORR, H-ACT, H-INSTANT, H-QET-BUDGET, H-QET-HADAMARD, H-FLAT-QFT (N_FLATQFT), H-LINEAR-QM;
  - H-MASS-BALANCE (N_MBAL).
- **OPEN pathways:** N_DEFB, N_NEGT, N_GJWPAY (N_GJW-PAYLOAD), N_PINCH, N_QETHAD, N_WNCC, and the candidate N_QLITNL.
  Retired: N_WALLLOOP, N_GJWAMB.
- **D68's, carried unchanged:** W_W2R, H-SAME-EPS, R_W2, H-NEARMAX, N_EPS, N_W2ANC, N_QTOPO, N_CORR, N_S5, H-SEAT-S5 /
  H-SEAT-ROUTES, the nine of H-VAC-LEFTIF, and N_XI / N_QEIC (with RQ).
- **Encoding choices:** E-EXTEND, E-THROAT, E-ADS, E-SINGOK-RULED, E-FKZ, E-LIN, E-SEATOFF-ALL, E-DEFB, plus drift rules
  Z7 and the seat rule.

## 8. Sources

**No outside source was read at this stage.** Every outside reading is the A-reports', with its route recorded there:

- A1: alphaXiv full text (HK, DURRER, CGS, VISSER89, GV17, FKZ23, CFG94, DLM04, PLANCK13, FSW93, FGM19, ETO25) and
  Firecrawl abstracts; at D66-fix HK pp.63-65, CGS pp.14-15 / Fig.4 and GV pp.20-22 re-read;
- A2: alphaXiv (PV, GJW, MSY, AHMST); at D66-fix GJW pp.12-15, Maldacena & Qi 1804.00491 and Maldacena-Milekhin-Popov
  1807.04726;
- A3: alphaXiv (Hotta 2008 / 2010, FMM, Ikeda, review, Zachary, Flanagan); at D66-fix Hotta 1002.0200v2's page numbers.

No host refused a request, no paywall or login wall was met, and no copyrighted text is quoted here.

## 9. Findings (recorded, not repaired)

1. No D66 hypothesis, in any reading or combination, is load-bearing in any removal or non-binding. Every lift is D68's
   or the board's.
2. A naive "member in a support" attribution would credit R-LIT with W2 × F1's O-BITS removal in 448 variants per
   cell, because R-LIT entails W2 under E-LIN. The load-bearing test is needed, and it is controlled.
3. The geometric-throat readings undo ITB's non-bindings by a premise clash, as RQ does in D68. Anyone wanting ITB's
   NOT-BOUND-IF and a D66 throat in one account cannot have both.
4. A1's FKZ sentence holds as a conditional: once the string-supported throat is held, the seat loop is FORCED unless
   N_MBAL. After D66-fix it is the only source of a defeasible seat.
5. The defect core moves the GROUND of massform's TEMPLATE refusal (P-UNIFORM → topology), not the refusal, and not
   O-SEAT.
6. A3's minimal-model figures are raw model values at (h, k) = (1.5, 1) (E_B = 0.14252, E_B/h = 0.0950); A3 now prints
   them so (V66-2 #5). *Wave 1 recorded this here as a unit note on A3's "0.1425 h".*
7. A2's seat text names R-HOLO and R-THINSHELL (and R-TELEPORT "adds" GJW), not R-ISLAND or R-ITB. E-SEATOFF-ALL is
   stated.
8. (D66-fix) **For the D68 board:** M's ruling M-S1A-P3, read as a board ruling, reaches D68's own O-MAKE-TOPO in 20
   context-only variants (`singok-board`), where D68's combine.py grades LEFT. combine66 applies the ruling to every
   D66 throat and leaves D68's encoding alone (E-EXTEND); whether D68 re-grades is the D68 board's.

## 10. Open

- N_DEFB: a B-violating core supplying baryons needs CP violation and a departure from equilibrium (HK p.65); its READ
  direction is wash-out; rate and feedstock (leptons) uncomputed.
- N_NEGT, N_GJWPAY, N_PINCH, N_QETHAD, N_WNCC: each computed nowhere as a realisation (N_GJWPAY's MMP family is computed
  and does not admit the payload; N_QETHAD's check is short and not run).
- N_QLITNL: arrival-alone energy under any non-linear dynamics.
- Whether GJW's negative ANEC is QET-like (R-TELEPORT × QET), not read.
- H-FKZ-GENERIC (`fkz-generic`): whether FKZ's time machine is generic to every held throat with mouths in one space.
  Shown beside the screen, adopted nowhere.
- *Closed at D66-fix:* whether M's singular-throat admission is a board ruling -- it is (ledger M-S1A-P3), and it is
  applied; the wall's causal structure (computed; N_WALLLOOP retired).
