# DOCKET 68 · B-combine: the seven hypotheses in combination

**Status: a docket work item, wave 5 (2026-10-03, M-combine).** This stage applies M's rulings
(`M-RULINGS-2026-10-03.md`, verbatim in CHARTER.md) to the screen, after M-apply. It also resolves the three V3
residuals of `wave1/REPAIR3-RESULT.json` (key `result.v`) whose sites are here. **Nothing here is seated.** The
instrument is `combine.py`, beside this file.

`PYTHONDONTWRITEBYTECODE=1 python3 combine.py --selftest` runs **97 counted checks and passes all 97** in about 350 s
(z3, numpy, sympy; four worker processes). Twenty of the checks are controls. **Ten items cannot fail and are printed
STRUCTURAL, not counted:**

- the engine's premise-consistency of supports;
- three ground values: the D-CTC under C1, a state-independent unitary in `w2_ancilla_flow`, and the Bob-first row of
  `drift_ordering`;
- the INDEPENDENT classes, which carry no test by definition;
- the COVERAGE partition identity (7,903 + 288 = 8,191);
- **new in wave 5**, O-SEAT's survival in every consistent variant, and the two O-SEAT encoding comparisons (the
  H-SEAT-S12 alternative, and wave 4's DEF-MATTER under the O-SEAT atom). These cannot fail because B-S10 and B-S13 are
  bare refusals and no commitment names a supply. *Wave 4 counted the analogous O-MATTER survivor check*, which the bare
  B-RECV made equally unfailable; it is now STRUCTURAL.

*Wave 4 first said:* "90 counted checks and passes all 90 ... Eighteen of the checks are controls. Six items cannot
fail". *Wave 3:* 85; *wave 2:* 65; *wave 1:* 80.

`combine.py` imports what it uses and copies nothing: `settle.py`, `frame.py`, `measure.py`, `geometry.py` (the four
work items, as repaired by R3-alone and then by M-apply); `../massform.py` through `measure.seat_supply` (wave 5); `nlcontrol.py`, `corridors.py`, `nosig.py` through them; `../transit.py`,
`../emtension.py`, and `../LEDGER.md` (read, never written). It writes nothing outside `docket68/` except output paths
the caller names. It compares itself with the A-reports' JSON grades. A3's H-INFO-SHAPE grade is not in A3's JSON, so
it is read from `measure.GRADES`, tagged with that source.

M's standing instruction, verbatim from the charter: *"Remember that some of the hypothesies lined up for docket 68
may turn out, after initial testing, to work better in combination."* M's hypotheses are carried as hypotheses. Each
grade says what a combination does, not whether it is true.

## The answer, first (section 3 has the detail)

**Member-attributed removals (what the hypotheses themselves remove) number at most ONE in any consistent variant,
counted inside one consistent premise set (an "account"). It is always O-BITS:** 2,592 variants at 1 ly, N = 7, and 864
of the 1,152 consistent W2 variants at 1 AU, N = 7 (the re-screen with H-INFO-SHAPE; *wave 4 first said* 1,728, and
576 of 768, over 6,143 variants). There are two ways it happens.

**1. By H-SETTLE W2 × H-FRAME** (clause 1, or clause 2b's cosmic clock). This is a JOINT result: neither member
removes O-BITS alone. It has **two supports**:

- **Support 1: REMOVED-IF {W2, F1; N_EPS}.** R_W2 = {ε > ε_any(L, N), H-C2 with its no-branch rule, H-FRAME3b ⇐ F1,
  H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK}. This is nlcontrol's form: every pair count is a **floor**, and
  reliable transfer is block-coded. Its window W_W2 is computed from the NAMED-NOT-READ Weinberg-family value:
  - at **1 ly, N = 7** and **1 AU, N = 10⁶** the window is open, so support 1 is **admissible given W_W2 (flagged, not
    settled)**. Majumder and Walsworth are unread; Bollinger 1989 and Chupp-Hoare 1990 are OPEN and were never
    checked. A bound 655× (reading A) / 328× (B) tighter than the unread figure would close it at 1 ly, and 7.16× /
    3.58× tighter at 1 AU, N = 10⁶ (context, not evidence; V3 problem 3, against M);
  - at **1 AU, N = 7 and N = 10³** the window computed from that value is empty, so support 1 is **OPEN via N_WREAD**,
    not LEFT;
  - with H-12 (N_H12W, no READ source), support 1 is REMOVED-IF.
- **Support 2: REMOVED-IF {W2, F1; N_W2ANC}.** R_W2′ = {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND,
  H-FIELD-W2}. This is the computed **zero-error** ancilla member, with neither H-BLOCK nor H-NLCONTROL-FORM. It carries
  χ = log₂d − 1 bits per pair, so it needs **2/(log₂d − 1) pairs per teleported qubit: 1, 2/3 and 1/2** at d = 8, 16,
  32. The class has no positive floor in the computed range. Its window is **unevaluated**: no READ bound maps onto its
  field. It holds in both cells only because nothing bounds the field, and "not excluded" is not evidence. The other
  direction, per member (V3 problem 1): the field it needs is ‖H‖ ≥ max‖H‖T · c/L, where max‖H‖T is 1.465 for the
  four-axis member (4.64e-8 s⁻¹ at 1 ly, **2.94e-3 s⁻¹ at 1 AU**) and spans 1.43–1.56 across the computed members
  (2.87e-3 to 3.12e-3 s⁻¹ at 1 AU). IF the unread precession bound were read onto this field (H-MAP-W2, adopted
  nowhere), that would sit **120–131× above ε_max under reading A and 240–261× under reading B** at 1 AU (123× / 246×
  for the four-axis member). No verdict moves.

**2. By H-FRAME clause 2b alone**, through a CTC at Bob: O-BITS **REMOVED-IF {F2b; N_DCTC}**, at every distance, with
**O-LOOP reintroduced**. The D-CTC carries 2.000000 bits per pair over four axes, zero-error, so it needs 1 pair per
teleported qubit **for that construction only**. The route needs ≤ 1, and its minimum is OPEN (BHW 0811.1209v2 p.4).
A CTC is not shown to exist.

**NOT-BOUND-IF (not removals).** Under H-IT as an information layer (ITB + N_QTOPO, or ITB + R-INDEX + N_MEASPHYS),
the theorems behind O-MAKE-TOPO, O-HOLD's geometric form and the corridor form of O-LOOP do not bind a non-geometric
corridor. What such a corridor costs is OPEN (N_ILFREE). In five-way terms that is at most 2.

**Removed with no member** (by the geometry, the board or a premise):

- corridor O-LOOP, by exact FRW {N_CORR, N_FRW}, only in accounts without N_QTOPO;
- signal O-LOOP, by N_SIGKEY.

**Survivors of every consistent variant:**

- **O-SEAT, "supply at the seat"**, which replaces O-MATTER by M's ruling (item 5: *"Yes, from the seat"*). It is
  **LEFT**. S10 is REFUSED as a supply on all six readings. S13 is OPEN and priced, but it forms no baryons: it
  restores 3.010e-6 (electrons) + ~1.716e-3 (nucleons, first order) of the payload to templates already there, so
  ≥ 0.998 of the payload must already be at the seat. Both refusals rest on H-C3.
- **O-MAKE in its distribution form**, OPEN via N_VAC only.

**Clash (d) under M's ruling.** M ruled on 2026-10-03, items 1 and 5: *"Teleportation carries no physical substance,
but does carry information (non physical properties/bounds that give shape to the geometry at the seat)"*. Read as
H-INFO-SHAPE, this is **consistent with B-RECV in every variant**, and it enters no clash core. The clash is
**dissolved by relocation, not removed by assertion**: the substance question moves to O-SEAT, which stays an
obstruction until the seat's supply is shown. H-INFO-SHAPE removes nothing (A3: LEAVES-ALL; difference census: inert).
H-INFO-S is **kept as the alternative reading**. Its clash with B-RECV stands in all 2,048 of its variants and is
recorded as history (*wave 4 first said* "clash (d), M's to rule").

**Q-1s (signed / complex entropy) moves no grade here, and the reason is computed, not declared.** Every bit count the
screen uses is taken over non-negative probabilities, where Re H = H by definition: nlcontrol's capacity, the Holevo χ
of the ancilla member and of the D-CTC, and log₂ 976. No board holding or commitment names the measure's functional
form. H-INFO's necessity reading is inert (difference census: 0 of 2,048 variants change). M's rulings 2, 3 and 6 (the
weightings, the inverses and reflections, the ground-state calibration) are applied in signed.py and measure.py by
M-apply. The screen encodes no obstruction that turns on them.

*Wave 4's form of this section is kept verbatim as history at the head of wave 4's section 0, below.*

## 0. Wave-5 work: M's rulings applied in the screen, and the three V3 residuals sited here

M answered the open questions on 2026-10-03 (`M-RULINGS-2026-10-03.md`, carried verbatim into CHARTER.md by M-apply).
These are **rulings**, and they are applied as M worded them. M-apply graded H-INFO-SHAPE and O-SEAT in A3 and
`measure.py`. This stage re-screened every combination under them and resolved the three V3 residuals
(`wave1/REPAIR3-RESULT.json`, key `result.v`) whose sites are in `combine.py` and this file. Wave 4's section 0 follows
unchanged as history; wave 4's forms elsewhere are marked *wave 4 first said*.

**Numbering (V3 problem 2).** In this file, outside the history tables, V2-0, V2-1 and V3 items are cited **1-based**:
"problem n" is the n-th entry, which is JSON index n − 1. M-apply stated the same convention in A1, A2, A3 and Q1s, and
`combine.py`'s comments were already 1-based. **Wave 4's section-0 tables print the JSON index** (0-based) in their "#"
column and in their U labels. Each of those rows also carries its site text, and that text is the reference to use. To
convert, add 1: wave 4's "1:" under *V2-1 — problems* is V2-1 problem 2, the two supports.

### M's rulings, as screened

| ruling (verbatim in CHARTER.md) | what this stage did | computed result |
|---|---|---|
| **1 and 5.** Clash (d), H-INFO-S against B-RECV. M: *"Teleportation carries no physical substance, but does carry information (non physical properties/bounds that give shape to the geometry at the seat)"*; asked whether the substance is supplied by the seat itself, *"Yes, from the seat"* | **H-INFO-SHAPE added as a fourth H-INFO option (`SHAPE`)**, screened in every combination beside INFO and INFOS. Its one commitment is C-SHAPE (SHAPE ⇒ RECV, measure.py's H-SHAPE-ENCODING). **INFOS is kept as the alternative reading.** Its clash with B-RECV is recorded as history: "M ruled 2026-10-03". | SHAPE ∧ B-RECV is **SAT**, and INFOS ∧ B-RECV stays **UNSAT**. CONTROL: drop B-RECV and INFOS becomes consistent. SHAPE enters **no** clash core. The difference census finds SHAPE **inert**: its commitment is already the board's. Variants: (4·4·4·4·2·2·2 − 1)·4 + 3 = **8,191** (wave 4: 6,143). The clash is **dissolved by relocation, not removed by assertion**. |
| **5.** The matter obstruction becomes **supply at the seat** | **O-MATTER is replaced by O-SEAT** in every variant (H-SEAT-GLOBAL: M's ruling concerns the obstruction itself, not one reading). DEF-SEAT: O-SEAT is removed iff the seat's supply of the substance is shown, by S10 or S13. **B-S10**: S10 REFUSED as a supply (`massform.MECHANISM_VERDICT`, all six readings; LEDGER S10 READ). **B-S13**: S13 is OPEN and priced, but *"It forms no baryons (C3: the elements were already there)"* (LEDGER S13, READ; `massform.HELD_SEAT_ROUTE['forms baryons']` False). Both refusals rest on **H-C3**, which is named. Drift rule **P10**: an A-report's "O-MATTER" text is compared with O-SEAT. | O-SEAT is **LEFT in every consistent variant**. That cannot fail, because both refusals are bare, so it is printed **STRUCTURAL** and not counted. *Wave 4 counted the same check on O-MATTER, which was equally unfailable.* The content sits in two **CONTROLS**: dropping B-S10 frees O-SEAT, and so does dropping B-S13. **ALTERNATIVE H-SEAT-S12** (adopted nowhere): read the pair route S12 (OPEN, priced) as a supply and O-SEAT reads OPEN via N_S12. The energy that route needs, ≥ 1.2567e19 J for 70 kg, would itself have to be at the seat (D23). M-apply places S12 beside O-SEAT and does not credit it. No obstruction is removed by assertion. |
| 2, 3, 4, 6 (weightings, inverses and reflections, D67's held rows, the calibration of the origin) | Not sited in the screen. M-apply applied them in signed.py, measure.py, Q1s and A3. | No board holding or commitment of the screen names a weighting, a branch or a calibration. The Q-1s note in "The answer, first" still holds, so no grade moves. |

### V3 residuals sited here (`REPAIR3-RESULT.json` `result.v.problems`, 1-based)

| V3 item (site) | resolution |
|---|---|
| **problem 1**: B-combine.md:48, :598, :880 and R3-combine.json printed "1.465 c/L, i.e. 4.5e-8 s⁻¹ at 1 ly, 2.9e-3 s⁻¹ at 1 AU, 120× ε_max". Those figures came from `w2_ancilla_flow_k(4, 2)` (max‖H‖T = 1.4306), not from 1.465 | **Applied.** `support2_members()` collects every computed support-2 member with its own max‖H‖T, and `support2_field_rows` gives one row per member, naming its construction, under **both** H-MAP-W2 readings. A new GROUND check recomputes needed ‖H‖ = max‖H‖T · c/L from independent constants. The computed members span max‖H‖T 1.43–1.56. The per-member figures are in the table after this one, and **no verdict moves**. |
| **problem 2**: one item-numbering convention | **Applied** (the note above). Current text is 1-based, wave 4's tables are marked 0-based, and every row cites its site. |
| **problem 3**: M's rule was applied in one direction only. A support-1 removal at a cell whose window is OPEN from the unread value was listed as settled | **Applied, as a flag and not a premise.** Every support naming N_EPS at an open-window cell now carries **"ADMISSIBLE GIVEN W_W2 (flagged, not settled)"**. Majumder and Walsworth are NAMED-NOT-READ; Bollinger 1989 and Chupp-Hoare 1990 are OPEN and were never checked. Support 2 carries "UNEVALUATED". The verdicts are unchanged: {W2, F1} is still **REMOVED-IF {W2, F1; N_EPS} [admissible given W_W2] \| {W2, F1; N_W2ANC} [unevaluated]** at 1 ly, N = 7 and at 1 AU, N = 10⁶ (checked). `settle.window_given` (imported) agrees with combine's z3 window (exact rationals) in all 12 (cell, reading) rows. Tightening that would close the window (context, not evidence): **655× (A) / 328× (B)** at 1 ly, N = 7; **7.16× / 3.58×** at 1 AU, N = 10⁶. AGAINST M, and it moves no grade. |

**Support 2's field figure per member (V3 problem 1).** Each member's figure uses that member's own max‖H‖T, and IF
H-MAP-W2 held (adopted nowhere) the figure is shown against both readings:

| member (construction) | max‖H‖T | needed ‖H‖ at 1 ly (s⁻¹) | needed ‖H‖ at 1 AU (s⁻¹) | IF H-MAP-W2: × ε_max at 1 AU, reading A / B |
|---|---|---|---|---|
| `w2_ancilla_flow` (four-axis member, d = 8) | 1.4654 | 4.643e-8 | 2.937e-3 | 123.0 / 246.0 |
| `w2_ancilla_flow_k(4, 2)` (k = 4, d = 8) | 1.4306 | 4.533e-8 | 2.867e-3 | 120.1 / 240.1 |
| `w2_ancilla_flow_k(8, 3)` (k = 8, d = 16) | 1.4843 | 4.703e-8 | 2.974e-3 | 124.6 / 249.2 |
| `w2_ancilla_flow_k(16, 4)` (k = 16, d = 32) | 1.5556 | 4.929e-8 | 3.118e-3 | 130.6 / 261.1 |

At 1 ly every member needs 0.0019–0.0021× ε_max (A) and 0.0038–0.0041× (B). The window is unevaluated and H-MAP-W2 is
adopted nowhere. *Wave 4 first said* "1.465 c/L, i.e. 4.5e-8 s⁻¹ at 1 ly, 2.9e-3 s⁻¹ at 1 AU, 120×". That paired the
four-axis member's 1.465 with k = 4's figures and gave one reading only.

### V3's unresolved list, as it bears here

- **H-CORES-AS-SCREENED.** The clash cores are still not re-derived from the board holdings, which is unchanged. The
  re-screen re-enumerates them under SHAPE: the cores are C-ITE + C-W2 linearity, C-ITE + B-GISIN + C-F1/F2b, and
  C-INFOS + B-RECV. No new core appears.
- **No source was re-read this stage, and no 403 was met.** Every new figure is imported: LEDGER S10, S12 and S13 rows
  (READ through `measure.ledger_row` and `board_flags`), massform and `settle.window_given`.
- **The OPEN items stand** as both R3 reports carry them (section 12). The one change is clash (d), which M has ruled.

### The task's own items (M-combine)

| item | where |
|---|---|
| re-screen with H-INFO-SHAPE; carry it as a reading | `SHAPE` in SUBREADINGS / LIT_NAMES, C-SHAPE; 8,191 variants; drift row for A3's H-INFO-SHAPE grade (P10); checks "CONTENT clash (d) under M's ruling", "RESULT clash census under SHAPE", "RESULT INFO, SHAPE, ZERO and NULL are UNTESTED-BY-SCREEN" |
| replace O-MATTER by O-SEAT, encoded from S13 / S10 as M-apply graded them; no obstruction removed by assertion | OBST / FIVE, DEF-SEAT, B-S10, B-S13 (H-C3 named); CONTROLS dropping each refusal; GROUND "O-SEAT as encoded"; H-SEAT-S12 alternative and wave 4's DEF-MATTER printed STRUCTURAL |
| keep INFO-S as the alternative, its clash recorded as history ("M ruled 2026-10-03") | SUBREADINGS["H-INFO"]["INFOS"], C-INFOS, B-RECV text, rule 2, the clash table, findings 5, section 12 |
| V3 residuals 1-3 | the table above: `support2_members` / `support2_field_rows` per member; the numbering note; the support flag `_window_flag` with the GROUND against `settle.window_given` |
| re-run the screen and selftest; restate the answer, member-attributed first | `--selftest` 97/97 (20 controls, 10 STRUCTURAL); `--json`, `--table` re-run (section 6 regenerated); "The answer, first" |

**Counted checks, 90 → 97.** Two of wave 4's checks left the count:

- "CONTROL without B-RECV, O-MATTER becomes removable" went with DEF-MATTER;
- "RESULT O-MATTER removed or not-bound in no consistent variant", whose O-SEAT form cannot fail, is now STRUCTURAL.

Nine checks are new:

- CONTENT: clash (d) under M's ruling;
- three CONTROLS: B-RECV dropped, so INFOS is consistent; B-S10 dropped, so O-SEAT is removable; B-S13 dropped, so
  O-SEAT is removable;
- two RESULTS: the clash census under SHAPE (8,191 = 5,759 + 2,432; INFOS 2,048; W2+ITE 512; SHAPE in no core), and
  the support-1 flag at 1 ly, N = 7 and 1 AU, N = 10⁶;
- three GROUNDS: O-SEAT as encoded, the support-2 field figure per member, and the window both ways.

The INFO/ZERO/NULL inertness check now includes SHAPE. Controls go 18 → 20 and STRUCTURAL items 6 → 10.

## 0 (wave 4). Wave-4 repair: every item in both re-verifications of REPAIR2, and what was done — kept as history

**Numbering in this wave-4 section (V3 problem 2):** the "#" column and the U labels print the **JSON index (0-based)**.
Everywhere else in this file the items are cited 1-based, so add 1 to convert (row "1:" under *V2-1 — problems* is V2-1
problem 2). Each row's site text is the unambiguous reference.

### Wave 4's "The answer, first", kept verbatim

*(wave 4)* The answer, first

**Member-attributed removals — what the hypotheses themselves remove — number at most ONE in any consistent variant,
counted inside one consistent premise set (an "account"), and it is always O-BITS** (1,728 variants at 1 ly, N = 7;
576 of the 768 consistent W2 variants at 1 AU, N = 7):

- **by H-SETTLE W2 × H-FRAME** (clause 1, or clause 2b's cosmic clock), a JOINT result (neither member removes it
  alone), with **two supports** (wave 4, V2-1 problem 2; A1 wave 4):
  1. **REMOVED-IF {W2, F1; N_EPS}** — R_W2 = {ε > ε_any(L, N), H-C2 with its no-branch rule, H-FRAME3b ⇐ F1, H-COHERE,
     H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK}: nlcontrol's form, every pair count a **floor**, reliable transfer
     block-coded. Its window W_W2 = {H-MAP, H-TRANSFER, H-SPIN, H-DILUTION, the NAMED-NOT-READ values} is computed open
     at **1 ly, N = 7** and **1 AU, N = 10⁶**. At **1 AU, N = 7 and N = 10³** the window computed from the unread value
     is empty, so the exclusion is LEFT-IF W_W2 and, by M's rule, **OPEN via N_WREAD pending a READ of the
     Weinberg-family values (E-WIN), not LEFT**; with H-12 (N_H12W, no READ source) support 1 is REMOVED-IF there —
     H-12 replaces H-TRANSFER in an exclusion that rests on an unread value;
  2. **REMOVED-IF {W2, F1; N_W2ANC}** — R_W2′ = {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2}:
     the computed **zero-error** ancilla member, with neither H-BLOCK nor H-NLCONTROL-FORM. χ = log₂d − 1 bits per pair
     (2, 3, 4 at d = 8, 16, 32: T-K), so **2/(log₂d − 1) pairs per teleported qubit — 1, 2/3, 1/2 — and the class has
     no positive floor** in the computed range (V2-1 problem 1). Its window is **unevaluated**: no READ bound maps onto
     its field (H-MAP not established), so the screen never excludes it and it holds in both cells — **distance-free
     only because nothing bounds the field**; "not excluded" is not evidence. Shown the other way: it needs
     ‖H‖ ≥ 1.465 c/L, i.e. 4.5e-8 s⁻¹ at 1 ly but **2.9e-3 s⁻¹ at 1 AU**, which IF the unread precession bound were read
     onto this field (H-MAP-W2, adopted nowhere) would sit 120× above ε_max = 2.39e-5 s⁻¹;
- **or by H-FRAME clause 2b alone**, through a CTC at Bob: O-BITS **REMOVED-IF {F2b; N_DCTC}** (the D-CTC: 2.000000
  bits per pair over four axes, zero-error, so 1 pair per teleported qubit **for that construction only**; the route is
  ≤ 1 pair per qubit and its minimum is OPEN, since BHW 0811.1209v2 p.4 makes the rate unbounded if CTC qubits are
  free — V2-0 problem 7, which understates for M as well), at **every distance**, with **O-LOOP reintroduced** (the
  channel is a CTC; M-S1A-P3: disqualifying at the seat only). A CTC is not shown to exist.

**NOT-BOUND-IF (not removals):** under H-IT as an information layer (ITB + N_QTOPO, or ITB + R-INDEX + N_MEASPHYS),
O-MAKE-TOPO, O-HOLD's geometric form **and the corridor form of O-LOOP** — their theorems do not bind a non-geometric
corridor; what that corridor costs is OPEN (N_ILFREE). In five-way terms at most 2 (O-HOLD, O-LOOP). The A-reports now
grade this symmetrically too (A3's R-INDEX grade was repaired by R3-alone, so the drift guard agrees on it: 167 of 168).

**Removed with no member (the geometry's, the board's or a premise's):** corridor O-LOOP by exact FRW {N_CORR, N_FRW}
— only in accounts without N_QTOPO, since the two corridor accounts clash (B-QCORR) — and signal O-LOOP by N_SIGKEY.

**Survivors of every consistent variant:** O-MATTER (LEFT; H-INFO's sufficiency reading clashes with B-RECV — clash
(d), M's to rule) and O-MAKE in its distribution form (OPEN via N_VAC only).

**Q-1s (signed / complex entropy) moves no grade here, and the reason is computed, not declared.** Every bit count the
screen uses — nlcontrol's capacity, the Holevo χ of the ancilla member and the D-CTC, log₂ 976 — is taken over
non-negative probabilities, where Re H = H by definition (STRUCTURAL: R3-alone's measure.py labels the same identity),
and no board holding or commitment names the measure's functional form; H-INFO's necessity reading is inert (difference
census: 0 of 2,048 variants change). Where Q-1s does bear — H-INFO clause (a) for signed weights, now SUPPORTED-IF
{H-SEPARABLE, BFL codomain dropped, product additivity} and impossible with the codomain kept (R3-alone, signed.py
§4b) — the screen encodes no obstruction that turns on it.

*Wave 3 first said:* "by H-SETTLE W2 × H-FRAME ... O-BITS REMOVED-IF {W2, F1; N_EPS} ... at 1 AU, N = 7 and N = 10³ only
with H-12 supplying an unbounded carrier" and "computed 2.000000 bits per pair over four axes, zero-error, so 1 pair per
teleported qubit" — one support (reading as if block coding were necessary), the 1 AU exclusion as settled though it
rests on an unread value, and the four-axis figures as the classes' (V2-1 problems 1-3; V2-0 problem 7).
*Wave 2 first said:* "The most is **three of five** ... Every one of them contains {H-SETTLE W2, H-IT ITB}" — that count
mixed a REMOVED-IF, a NOT-BOUND-IF and the geometry's removal across two clashing corridor accounts; recomputed per
account it is still 3 (32 variants, smallest {W2, F1, ITB}), reported below as history, not as the answer.


### Wave 4's repair items

Two re-verifications (V2-0, AGAINST M; V2-1, FOR M) left items in repaired wave 1 and in Q-1s. R3-alone repaired the
A-reports, the four instruments, Q1s-signed.md and the charter note; this stage repaired `combine.py` and this file and
re-ran the screen. Every item is listed, including those sited elsewhere, with what this stage checked. Wave 3's forms are
kept below, marked *wave 3 first said*; wave 3's section 0 follows unchanged as history.

### V2-0 (AGAINST M) — unresolved items

| item | resolution |
|---|---|
| U0: A1-settle.md:373, "H-SETTLE-KR × H-12, with G as the carrier ... O-HOLD OPEN via G" duplicates KR alone and does not say H-12 adds nothing | **Applied in A1 by R3-alone** (row now "adds nothing to H-SETTLE-KR alone"). **Checked here:** the load-bearing guard reads A1's wave-4 row, which says "adds nothing", so rule L1 requires the z3 load-bearing set to be a proper subset of {KR, H12}: it is empty (KR's O-HOLD is OPEN via N_EPSG, no removal or non-binding), and the row agrees. 13 rows checked, all agree. The wave-3 open item ("A1's KR × H-12 row ... H12 not load-bearing") is closed. |
| U1: RV-1 #2's symmetric corridor rule not carried to A3's R-INDEX O-LOOP; one of the two live `combine.EXPLAINED` entries | **Applied in A3 by R3-alone** (O-LOOP-C NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} for a physical corridor; SILENT within the measure). **Applied here:** the entry ('A3-measure', 'ITB+RI', 'O-LOOP') is **deleted** from `EXPLAINED` (its wave-3 text kept in `EXPLAINED_HISTORY`, never consulted), and the drift guard now agrees on that row: **167 of 168** comparisons agree (*wave 3:* 166 of 168). R3-alone's read-only run had shown the stale entry failing the "no stale whitelist" check (84/85); that check now passes. |
| U2: N_QTOPO, N_MEASPHYS, N_H12W, N_ILFREE have no READ source; the Weinberg-family values stay NAMED-NOT-READ; H-EXTEND derived; W2 capacity without H-BORN-AT-BOB OPEN | **Answered: OPEN by design, each verdict naming its premise** (section 8). One more READ for the Weinberg-family values this pass: arXiv:2411.09611v1 pp.1-8 (alphaXiv) carries none of the 1989-90 numbers; its \|ε\| ≲ 1.15e-12 (90% CL) bounds the Kaplan-Rajendran causal electromagnetic nonlinearity, dimensionless, so no H-MAP carries it onto ε_max. **What changed is how the unread values enter:** they are now the OPEN pathway **N_WREAD**, so the 1 AU, N ≤ 10³ cells are OPEN, not LEFT (FOR problem 2 below). H-EXTEND sits in N_W2ANC as derived, not computed. |
| U3 (outside its lens, for the FOR side): 2511.15935v1 p.4 — KR fails Tomonaga-Schwinger integrability (foliation dependence); A1 READ pp.1-3, 5 only | **READ by R3-alone (p.4) and named H-KR-TS in A1.** **Here:** C-KR's ground now records it; no signal is shown from the foliation dependence, so the commitment (KR: no signal at Bob, KR §2.3, DERIVED-FROM-READ) stands and no verdict moves. Whether the dependence is operational is OPEN (section 12). |
| U4: every other RV-0 / RV-1 item found applied | No action; recorded. |

### V2-0 (AGAINST M) — problems

| # (site) | resolution |
|---|---|
| 0: Q1s s.6 / s.4 (d)-(e) / OPEN 1: uniqueness of Re H reported OPEN; Kontsevich (math/0008089v1 p.43) claims it under signed recursivity | **Applied by R3-alone** (Kontsevich READ pp.1-2, 10-11, 42-44; OPEN 1 restated CLAIMED-IN-LITERATURE / DERIVED (separable) / OPEN (non-separable); positioning list extended). **Bearing here:** none on a grade — the Q-1s paragraph in "The answer, first" gives the computed reason. |
| 1: A1:373 KR × H-12 credits O-HOLD OPEN via G to the pair | As U0. |
| 2: Q1s s.4 "Extending Shannon to signed measures forces dropping non-negativity" unqualified | **Applied by R3-alone** ("Inside H-DICTIONARY, and inside H-SEPARABLE, ..."; general case OPEN). Not sited here. |
| 3: Q1s s.4 (c) "M is the product-additive member" (uniqueness) | **Applied by R3-alone** (qualified; g₃ counterexample recomputed). Not sited here. |
| 4: measure.py / signed.py checks that cannot fail counted as evidence | **Applied by R3-alone** (measure 73 counted, 13 STRUCTURAL; signed 77 counted, 9 STRUCTURAL). combine imports none of those checks; it uses no Q-1s figure as evidence (above). |
| 5: combine.py:2334 "COVERAGE untested + joint = all variants" counted in 85/85 | **Applied.** Printed STRUCTURAL and not counted (the identity is shown in the header). The JOINT content-bearing check (TEST_BEARS) can fail and stays counted. Counted checks: 84 of wave 3's 85 survive as counted; six new counted checks are listed below. |
| 6: A2:32 "the D-CTC route is zero-error, so its counts are exact"; B's T-E rows "1, zero-error" for the W2 ancilla member and the four-axis D-CTC | **Applied** (A2 by R3-alone). **Here:** T-E's pairs table, the count table, `N_DCTC`'s text, `first_transit`'s labels and T-J now read "four-axis construction: 1, zero-error; the route ≤ 1 pair per teleported qubit, minimum OPEN (BHW 0811.1209v2 p.4)"; the W2 row reads "four-axis instance 1; the class 2/(log₂d − 1), no positive floor". Recorded both ways: the class figures are lower (better for M) than "1". |
| 7: Q1s s.6 (iv) per-entry branch accounting listed as not found | **Applied by R3-alone** (marked elementary; basis of D1). Not sited here. |

### V2-1 (FOR M) — unresolved items

| item | resolution |
|---|---|
| U0: RV-1 #2 not carried to A3's R-INDEX grade (`combine.py:1332`, EXPLAINED) | As V2-0 U1: repaired in A3, entry deleted here, agreement computed. |
| U1: RV-0 #4 not followed through (A1:374 KR × H-12) | As V2-0 U0. |
| U2: RV-1 #3's window premises named (E-WIN) but not screened; B-combine.md:32 states the 1 AU result categorically | **Applied.** The NAMED-NOT-READ values now enter the screen as the OPEN pathway **N_WREAD** in B-EPSWIN (N_EPS ⇒ window open ∨ (H12 ∧ N_H12W) ∨ N_WREAD). OPEN pathways are held false whenever premise sets, supports and accounts are computed (they are never assumed in a removal), so N_EPS stays **inadmissible** at 1 AU without H-12 (the premise clash {N_EPS}, 384 variants, unchanged) while the support-1 route reads **OPEN via N_WREAD** (computed: `support1-only` screen of {W2, F1}). CONTROL: wave 3's encoding (no N_WREAD) gives LEFT. The rest of E-WIN — refusing H-TRANSFER without H-12 — is still not screened, and is named. |
| U3: RV-0 unresolved #4 stands in part | As V2-0 U2. |

### V2-1 (FOR M) — problems

| # (site) | resolution |
|---|---|
| 0: "1 pair per teleported qubit" presented as the W2 class's figure without H-QUBIT-DRIFT (A1 s.1b, A2:258, B:426, B:36-37) | **Applied and computed here.** `settle.w2_ancilla_flow_k` (R3-alone's generalisation, imported) is re-run in combine's grounds and in the new test **T-K**: k = 4, 8, 16 axes with d = 8, 16, 32 give χ = 2.000000, 3.000000, 4.000000 = log₂d − 1, Bob's error 0, curves disjoint (0.391, 0.337, 0.180 rad against grid steps 0.0072-0.0078) → **1, 2/3, 1/2 pairs per teleported qubit**. CONTROLS fail as built to: a state-independent unitary gives χ = 0 (k = 16); antipodal axes give χ < log₂k with colliding curves (k = 8). The class has no positive floor in the computed range; H-EXTEND is still derived, and none of this is evidence such a drift exists. T-E's tables relabelled (section 4). |
| 1: W2 × F1's removal given a single support R_W2, reading as if H-BLOCK and H-NLCONTROL-FORM were necessary | **Applied in the encoding**, not only in prose: the named premise **N_W2ANC** (R_W2′) enters B-CAP (CAP ⇔ SIG ∧ (N_EPS ∨ N_W2ANC)). z3 now gives {W2, F1}: O-BITS **REMOVED-IF {W2, F1; N_EPS} \| {W2, F1; N_W2ANC}** (checked). The grade word does not change; the support set gains an alternative with fewer premises. The named census reports N_W2ANC **STRUCTURAL: never inadmissible, assuming it cannot fail**, exactly as N_H12W — no bound reaches its field. |
| 2: at 1 AU with N ≤ 10³, O-BITS without H-12 carried as LEFT | **Applied**, as U2: support 1 there is **OPEN via N_WREAD**, pending a READ of the Weinberg-family values; the N = 10³ cell has the same computed window as N = 7 (empty under both H-MAP readings), so it screens identically (board equality STRUCTURAL; the window is the content). Support 2 has no window at all and gives **REMOVED-IF {W2, F1; N_W2ANC}** in both cells; so the full 1 AU verdict on {W2, F1} is REMOVED-IF through support 2 alone (96 variants rest only on it), and the support-1 OPEN is reported per support (drift ground row, T-G). "The H-12 synergy at 1 AU" now reads: H-12 replaces H-TRANSFER in support 1's exclusion, which rests on an unread value; it changes no verdict once support 2 is counted (difference census: H-12 changes only the premise clash {N_EPS}, 384 variants) and stays in an alternative support (288 variants). |
| 3: A3's R-INDEX grade gives O-MAKE and O-HOLD NOT-BOUND-IF for a physical corridor but not O-LOOP | As V2-0 U1. z3's encoding already gave O-LOOP-C NOT-BOUND-IF {ITB; N_QTOPO} \| {ITB, RI; N_MEASPHYS} beside the geometry's REMOVED-IF in the other account (premise clash {N_CORR, N_MEASPHYS}); the A-report now agrees. |
| 4: Q1s s.4 / A3 (vii): uniqueness confined to H-DICTIONARY where a short proof reaches every continuous separable functional | **Applied by R3-alone** (signed.py §4b: X = c Re H + b N; z3 obligations with vacuity and encoding guards). Bearing here: as the Q-1s paragraph — one H-INFO clause status moves, no obstruction grade, and the screen encodes none that turns on it. |

### The task's own items (R3-combine)

| item | where |
|---|---|
| the COVERAGE partition identity STRUCTURAL | header; selftest prints it, does not count it |
| the 1 AU, N ≤ 10³ cell OPEN pending a READ of the Weinberg-family values (E-WIN), not LEFT | N_WREAD (B-EPSWIN); drift ground row; T-G; checks "RESULT 1 AU ... OPEN via N_WREAD", "CONTROL wave 3's settled window ... LEFT", "CONTENT ... only through N_WREAD"; N = 10³ window computed |
| W2 × F1's two supports | N_W2ANC in B-CAP; check "RESULT {W2, F1} ... TWO supports"; T-K; the answer above |
| align with every repaired A-report; no EXPLAINED entry left if its cause is repaired | A3 entry deleted (167/168); the A2 entry kept because its cause is vocabulary, not a fault (re-read in A2's wave-4 JSON: unchanged), so no repair exists to make; the KR × H-12 row agrees under rule L1 |
| Q-1s where it bears; it moves no grade, with the reason | "The answer, first"; selftest STRUCTURAL note; section 10 |
| re-run the screen and selftest; restate the answer, member-attributed removals first | `--selftest` 90/90 (6 STRUCTURAL); `--json`, `--table` re-run (section 6 regenerated); "The answer, first" |

**Counted checks, 85 → 90:** the COVERAGE identity leaves the count (84); wave 3's "{W2, F1}: one support" check is
rewritten as "two supports"; six are new — RESULT support 1 at 1 AU OPEN via N_WREAD; CONTROL settled window gives LEFT;
CONTENT N_EPS admissible at 1 AU only through N_WREAD; GROUND w2_ancilla_flow_k χ = log₂d − 1; GROUND its two CONTROLS
(linear, antipodal); TEST T-K. Controls 17 → 18. The vacuity guard gains the N_WREAD content line; the
"W2 at 1 AU without H12 under N_EPS" contradiction is now checked with OPEN pathways held false.

### Wave 3's section 0, kept as history

The wave-3 repair table follows unchanged; its figures are wave 3's (85 checks, 166/168, one support, the 1 AU cells
LEFT). Where wave 4 changed one, the tables above say so.

#### 0 (wave 3). Wave-3 repair: every item in both re-verifications, and what was done

**The principle, applied symmetrically, stated once.** *A theorem that does not bind a non-geometric corridor makes
the obstruction NOT-BOUND-IF (its premise named), never REMOVED.* Wave 3 applies it to the third theorem family it
had missed: the exact-FRW keying lemma and latticectc's loop theorem are theorems about Lorentzian quotients, so under
ITB + N_QTOPO they do not bind the corridor either. **O-LOOP is split** into a corridor form (O-LOOP-C, which can be
NOT-BOUND-IF) and a signal/CTC form (O-LOOP-S, unchanged). The two corridor accounts are a **premise clash**
{N_QTOPO, N_CORR} (constraint B-QCORR), and **every headline figure is counted inside one account**. O-LOOP's FRW
removal is credited to the geometry and to no hypothesis, uniformly (in combine and in the repaired A1-A4).

#### RV-0 (AGAINST M) — unresolved items

| item | resolution |
|---|---|
| U0: FOR #2 applied twice, A1 credits O-LOOP to H-SETTLE-W alone; B whitelists it | **Applied.** A1 now grades O-LOOP "LEAVES (member); corridors: geometry column" (R2-alone). combine reports the corridor removal as `Rg` (no member) in every account where it holds. The EXPLAINED entries for A1 {W2} and {W2, H12} O-LOOP are **deleted, not kept**; the drift guard now agrees on them. |
| U1: FOR #3 half applied in A4 (H-ZERO + H-IT, H-IT + H-NULL not split by reading) | **Applied.** A4 splits both rows by ITE / ITB / ITJ (R2-alone). combine carries the new reading **ITJ** and compares all six split rows by parse rule P7 (the clause for the variant's reading). The A4 {ITE, ZERO} EXPLAINED entry is deleted; agreement is computed. |
| U2: AGAINST #4, the 7 disagreements pass through a hand-typed EXPLAINED dict | **Applied.** Five wave-2 causes are gone because their A-side was repaired, not whitelisted. **Two disagreements remain of 168 comparisons**, each with a computed or READ reason (section 2). A new check fails if any EXPLAINED key is not a live disagreement (no stale whitelist). |
| U3: AGAINST #13, N_FRAME3b never adds F1 back, so {W2} alone is credited O-BITS | **Applied.** N_FRAME3b is **withdrawn** (it presupposes F1: A1 wave 3, corroborated READ 2511.15935v1 p.2). {W2} alone: O-BITS **LEFT**. The removal is W2 × F1's (or W2 × F2b's). H-SLICE-INTRINSIC (a slicing the drift picks without a preferred frame) is named, not credited; a third mutated encoding, `wave2-SLICE-INTRINSIC`, re-credits it and **is caught** (163/168, unexplained on A1 {W2}, {W2, H12} and A3 {W2, INFO}). |
| U4: four-basis D-CTC figure cited, not computed; N_H12W, N_MEASPHYS, N_QTOPO, N_ILFREE no READ source; Weinberg bounds NAMED-NOT-READ | **Computed:** `frame.four_basis_c2_table` is re-run in combine's grounds and in T-J: 2.000000 bits per pair under C2, map reproduced with P = 1, BHW condition-2 minimum 0.1738; `bb84_c2_table` 1.000000. **Unchanged and stated:** N_H12W, N_MEASPHYS, N_QTOPO and N_ILFREE still have no READ source, and every verdict resting on them names it. The Weinberg-family values stay NAMED-NOT-READ (R2-alone's two further READs, 2509.04320v1 and 2511.15935v1, carry no numbers): **OPEN**. |

#### RV-0 (AGAINST M) — problems

| # (site) | resolution |
|---|---|
| 0: ε > ε_any and N ≥ 7 presented as sufficient; "upper figure" | **Applied.** Every pair count from N·C ≥ 2 is a **floor**. Ground check (content-bearing): `settle.zero_error_table` gives one codeword at block lengths 1-3 for the Z-channel (every D) and the BSC at D < 1; control: the BSC at D = 1 gives 2, 4, 8. Reliable transfer is block-coded (**H-BLOCK**, in N_EPS's removal set). T-E's columns now read "floor, coded alone", "floor, block-coded", and the drift time T is labelled a floor. One removal set R_W2 everywhere. *Wave 2 first said* "nlcontrol pairs, N = 7 (upper figure, one Hamiltonian)". |
| 1: N_EQUIL encoded as needing H-ZERO or H-NULL | **Applied.** N_EQUIL belongs to H-IT read as Jacobson emergent gravity (**ITJ**, new reading). H-ZERO and H-NULL have no obstruction content: **UNTESTED-BY-SCREEN** (difference census: 0 of 3,072 variants changed by either), retirement neither established nor refuted. H-ZERO's own computed result (the zero is free under emergent gravity) touches no obstruction. |
| 2: N_FRAME3b presupposes F1 | **Applied**, as U3. Best member-attributed variants contain F1 (or F2b). |
| 3: A1 credits H-SETTLE-W alone with O-LOOP | **Applied** (A1 by R2-alone; combine uniform, as U0). |
| 4: A1's W2 × H12 row credits "OPEN via G in KR form" | **Applied** in A1 (re-sited to H-SETTLE-KR × H-12). combine now compares A1's KR × H12 row (agrees: O-HOLD OPEN via N_EPSG). **Recorded:** in the screen that OPEN is KR's alone; H12 is not load-bearing there. |
| 5: A4's H-ZERO + H-IT grades not split by reading | **Applied**, as U1. |
| 6: A3's H-SETTLE × H-INFO "complementary", H-INFO adds nothing | **Applied** in A3 (now "LEAVES-ALL, adds nothing"). combine adds a **load-bearing guard**: a combination row whose grade credits a removal or a non-binding must have every graded literal in a member-attributed support, unless the row says a member adds nothing. 12 rows checked, all agree. Parse rule P1 is generalised (every parenthetical dropped), so "LEFT by this pair (... REMOVED-IF ...)" no longer reads as R. |
| 7: A2 grades clause 2b × O-MAKE OPEN | **Applied** in A2 (NOT-BOUND-IF {2b's CTC; Geroch-compact only}, Tipler binds). combine keeps O-MAKE-TOPO **bound** under a CTC (B-TOPO: Tipler's non-compact case still binds). The one remaining difference is vocabulary, explained (section 2). |
| 8: headline "three of five" mixes REMOVED-IF, NOT-BOUND-IF and the geometry | **Applied.** The headline is computed per account by `headline()`, led by member-attributed removals, with NOT-BOUND-IF and no-member removals in separate columns (top of this file; section 3; section 6 table). |
| 9: coverage by fallback cannot fail | **Applied.** The fallback is deleted. A test covers a class only if its declared members are among the class's contributors and it bears on the class's synergy (`TEST_BEARS`, fixed before the screen runs). Classes are split: **JOINT** (a synergy) must have a test (a check that can fail); **INDEPENDENT** (only single-member results) are listed and **not tested as pairs** — reported STRUCTURAL. F1 × ITE, F2b × ITB and their supersets are INDEPENDENT. T-D covers nothing. |
| 10: settle's G7/G8/G6a/G12b cannot fail | **Applied** in settle (R2-alone). In combine the same identity — the ratio ε(T = L/2c)/ε_any = 2.000000 — is removed from T-E's pass condition and printed STRUCTURAL. |
| 11: drift_ordering's Bob-first "control" cannot be nonzero | **Applied.** It is excluded from T-A's pass and from the ground check, and reported STRUCTURAL; the content is the closed-form agreement at t_A < T. B-C2-SLICE's ground says the frame-dependence is derived *given* H-C2's no-branch-before-t_A rule. |
| 12: A2 item 1 "Clause 1 removes O-LOOP" | Sited in A2, applied there by R2-alone. combine's F1 reading already says keying is N_KEYING; F1's route {F1; N_CORR, N_KEYING} is reported as an **alternative** support beside the geometry's. |
| 13: A3 "measured 6.4920"; prediction 1 unconditional | Sited in A3, applied there by R2-alone. combine uses no "measured" for an integrated value (checked by grep). |

#### RV-1 (FOR M) — unresolved items

| item | resolution |
|---|---|
| U0: four-basis figure answered by restricting to H-BORN-AT-BOB on the qubit alone | **Applied.** The figure is computed (U4 above). T-E names the qubit-only subclass (H-BORN-AT-BOB + **H-QUBIT-DRIFT**) and adds the computed W2 member without H-QUBIT-DRIFT (`settle.w2_ancilla_flow`: 2.000000 bits per pair, zero-error, P(b′\|b) = identity, curves separated by 0.395 rad against a 0.0037 rad grid; smooth extension H-EXTEND derived, not computed): **1 pair per teleported qubit**. Not evidence such a drift exists. |
| U1: T-D still assigned as a covering test | **Applied.** T-D is a record and covers nothing (RV-0 #9). |

#### RV-1 (FOR M) — problems

| # (site) | resolution |
|---|---|
| 0: the W2 class floor rests on unnamed H-QUBIT-DRIFT | **Applied**, as U0. B-CAP's ground and T-E's table relabelled. |
| 1: clause 2b's D-CTC route absent from combine | **Applied.** B-DCTC: (F2b ∧ N_DCTC) ⇒ CTC ∧ CAPD ∧ ¬LIN; CAPD ⇒ F2b ∧ N_DCTC; CTC ⇒ O-LOOP-S not removed. DEF-BITS: O-BITS removed iff CAP ∨ CAPD. **{F2b}: O-BITS REMOVED-IF {F2b; N_DCTC}** (no N_EPS, distance-free), with premise clashes {N_DCTC, N_FRW} (a global time function admits no CTC, derived from `frw_time_function_lemma`) and {N_DCTC} with ITE (MS linearity against the D-CTC's nonlinearity). The F2b variants at 1 AU therefore keep O-BITS (480 of the 1,536 W2 variants re-screened there are member-removed). |
| 2: {N_QTOPO, N_CORR} never named; O-LOOP REMOVED-IF beside NOT-BOUND-IF | **Applied**, as stated in the principle above. Premise clash {N_CORR, N_QTOPO} with ITB in 512 variants (128 alone), {N_CORR, N_MEASPHYS} with ITB + RI in 256. In the N_QTOPO account corridor O-LOOP is **NBm**; signal loops stay `Rg`. In ITB variants the removed-only maximum per account is unchanged at 2 only in the N_CORR account (O-BITS and the geometry's O-LOOP); in the N_QTOPO account it is 1. |
| 3: H-MAP, H-TRANSFER, H-SPIN listed as removal premises | **Applied.** N_EPS's text separates the **removal set R_W2** from the **window set W_W2** = {H-MAP, H-TRANSFER, H-SPIN, H-DILUTION, the NAMED-NOT-READ values}. The window premises are held fixed by B-EPSWIN and named as encoding choice **E-WIN**: refusing H-TRANSFER widens the window (A1 §4b) and is not screened; N_H12W replaces H-TRANSFER. |
| 4: A4 rows not split by reading | **Applied**, as RV-0 U1. RV-1's "OPEN via N_EQUIL / N_ILFREE under ITB" is not applied, for A4's computed reason (EGJ acts on a metric; under N_QTOPO there is none). combine agrees: under ITB, O-HOLD is NOT-BOUND-IF with removal OPEN via N_ILFREE only. |
| 5: R-QUANTUM "in scope" | **Applied.** B-HELD's ground reads "LEFT only IF {H_flat, H-PATH, H-MIN-SCALAR}"; a new OPEN pathway **N_QEIC** (curved-space QEIs NAMED-NOT-READ) carries the outside of that IF. {RQ}: O-HOLD OPEN via N_XI and N_QEIC. *Wave 2 first said* "(minimal scalar, in scope)". |
| 6: B-RECV's conditions named nowhere beside clash (d) | **Applied.** B-RECV stays bare (a premise would let INFOS remove O-MATTER by assertion). Its conditions are in its ground and beside clash (d) in section 2. **Clash (d) stays a CLASH for M to rule.** |
| 7: coverage check cannot fail; F1 × ITB has no test | **Applied**, as RV-0 #9. F1 × ITB is not even complementary now (F1's loop route and ITB's non-binding are alternatives in different accounts); F1 × ITE and F2b × ITB are INDEPENDENT, untested as pairs. |
| 8: 1 AU statements without N | **Applied.** Every 1 AU statement carries N. A third cell, **1 AU, N = 10⁶**, has its window computed (open under both H-MAP readings: ε_any = 3.34e-6 s⁻¹ against 2.39e-5 and 1.19e-5), so it screens as 1 ly does (the board takes the cell only through that boolean: STRUCTURAL): there W2 × F1 removes O-BITS **without** H-12. The H-12 synergy is specific to 1 AU with N ≤ 10³. |
| 9: A1 rows treat O-LOOP unevenly; "OPEN via G" mis-sited | **Applied** in A1 (R2-alone); combine uniform, as RV-0 U0 and #4. |

#### The task's own items

| item | where |
|---|---|
| NOT-BOUND-IF, never REMOVED, applied symmetrically (incl. FRW lemma and loop theorem; {N_QTOPO, N_CORR} named) | principle above; B-NONGEO, B-QCORR, DEF-NB-LOOP-C |
| O-LOOP's FRW removal credited to the geometry uniformly | `Rg` in every account; column "removed with no member" |
| Shannon pair counts are floors; zero-error 0 at D < 1; block-coded | N_EPS, B-CAP, T-E, ground check |
| D-CTC: REMOVED-IF {CTC at Bob, H-DCTC, C2, select}, O-LOOP reintroduced; four-basis figure computed | N_DCTC, B-DCTC, T-J, ground check |
| removal vs window premises separated | N_EPS; E-WIN |
| R-QUANTUM LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR} | B-HELD, N_QEIC, parse rule P9 |
| combination rows load-bearing or "adds nothing" | load-bearing guard; section 6 column |
| headline leads with member-attributed removals; NB and geometry separate | top of file, section 3, section 6 |
| coverage by fallback STRUCTURAL | section 4 |
| 1 AU statements carry N | cells 1 AU N = 7 (re-screened) and N = 10⁶ (window) |
| B-RECV's conditions beside clash (d), which stays a CLASH | section 2 |

#### Wave 2's section 0, kept as history

The wave-2 repair table follows unchanged. Its figures are wave 2's (4,607 variants, 127/134 agreement, "three of
five"); where wave 3 changed one, the table above says so.

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
  - **H-SETTLE**: W2 is the drift on Bob's per-branch pure state (convention C2 = H-C2, with its no-branch rule). It
    signals only with a preferred slicing, which is H-FRAME's (H-FRAME3b ⇐ F1). W1 is the same drift on the reduced
    state (C1). KR is the causal Kaplan-Rajendran form.
  - **H-FRAME**: F1 is clause 1, "a preferred frame exists" (keying corridors to it is N_KEYING). F2b is clause 2b,
    "messages reach the past of the cosmic clock"; with N_DCTC it carries the D-CTC channel. F1+F2b is both together.
  - **H-IT**: ITB, the information-layer reading (no READ realisation); ITE, ER=EPR with MS's own assumptions; **ITJ**
    (new in wave 3), Jacobson / thermodynamic emergent gravity, whose one pathway is N_EQUIL on O-HOLD.
  - **H-INFO**: INFO is necessity; INFOS is sufficiency (A3's H-INFO-S), now kept as the alternative reading; and,
    **new in wave 5, SHAPE**: H-INFO-SHAPE, M's ruled reading (*"Teleportation carries no physical substance, but does
    carry information (non physical properties/bounds that give shape to the geometry at the seat)"*; the substance
    comes *"from the seat"*).
- **Reading slots** none / R-INDEX / R-QUANTUM / both: (4·4·4·4·2·2·2 − 1)·4 + 3 = **8,191 variants**, none skipped.
  *Wave 4:* 6,143 (no SHAPE). *Wave 2:* 4,607 (no ITJ). *Wave 1:* 3,071.
- **Distance cells.** **1 ly, N = 7** (window non-empty under both H-MAP readings), all variants. **1 AU, N = 7**
  (window empty under both), the **2,048 W2 variants** re-screened (*wave 4:* 1,536); complete, because N_EPS occurs only in B-CAP and
  B-EPSWIN and the board admits no CAP without W2 (z3), and neither the D-CTC route nor support 2 (N_W2ANC) depends on
  distance. **1 AU, N = 10³** (wave 4: window computed, empty under both readings) screens as 1 AU, N = 7, and **1 AU,
  N = 10⁶** (window computed open) as 1 ly — board equalities, STRUCTURAL; the windows are the content. Every window is
  computed from the NAMED-NOT-READ value. An empty one makes support 1 OPEN via N_WREAD, not LEFT. An open one makes
  support 1 admissible **given** W_W2, flagged and not settled (wave 5, V3 problem 3). N is always a floor.
- **Seven obstruction forms.** O-MAKE splits into O-MAKE-TOPO and O-MAKE-DIST; O-LOOP into O-LOOP-C (corridor loops)
  and O-LOOP-S (signal and CTC loops). In five-way terms a split obstruction counts only if both forms do. **Wave 5:**
  O-MATTER is replaced by **O-SEAT**, "supply at the seat", by M's ruling item 5. It is removed iff the seat's supply of
  the substance is shown, by S10 (REFUSED as a supply) or S13 (forms no baryons); both refusals rest on H-C3.

**Verdicts per obstruction:**

| verdict | meaning |
|---|---|
| **REMOVED** | forced by the variant's commitments, with no named premise |
| **REMOVED-IF** | forced once the named premises of a **support** are assumed; **every** minimal support is listed, drawn from a premise set consistent with the variant; absences are fixed (closed world); a member a premise presupposes is added back |
| **NOT-BOUND-IF** | the obstruction's theorem is forced not to bind because its geometric premise fails. **Not a removal.** For O-MAKE-TOPO, O-HOLD and O-LOOP-C it is computed even beside a REMOVED-IF (field `nb`), because the two can rest on clashing premises |
| **OPEN** | possible only through an OPEN pathway the sources leave undecided |
| **SILENT** | not forced either way, without any OPEN pathway |
| **LEFT** | the obstruction stands in every model |

**Per account** (one maximal consistent premise set), each form is **Rm** (removed, and the removal fails when the
present members are freed: member-attributed), **Rg** (removed with no member needed: geometry, board or premise),
**NBm** (not-bound, member-attributed), or not lifted. Headline counts are taken inside one account.

## 2. The screen (z3), and its guards

**What it is.** Bookkeeping over findings that other instruments own. Every board holding (`_board`) and commitment
(`_commitments`) is a tracked constraint with its ground (a computation or a READ page). z3 adds which commitments
contradict one another, which members and premises each verdict rests on (all supports), and exhaustive coverage. It
is not new physics, and its results are only as good as the encoding.

**Guards (the screen refuses to report if any fails).**

- **Vacuity.** The board alone is SAT; each single reading is SAT except INFOS (a clash); the named premises are
  jointly SAT at 1 ly and jointly **UNSAT** at 1 AU, N = 7 with OPEN pathways held false (content); named and OPEN
  together SAT; the board admits a loop and no loop; **wave 4:** at 1 AU, N_EPS with {W2, F1} is SAT with N_WREAD and
  UNSAT without it (the OPEN pathway carries the cell). **Wave 5:** SHAPE alone is SAT, so clash (d) is dissolved under
  M's reading, while INFOS stays UNSAT. Three CONTROLS: with B-RECV deleted, INFOS becomes consistent; with B-S10
  deleted, O-SEAT becomes removable; with B-S13 deleted, O-SEAT becomes removable. *Wave 4's* control ("with B-RECV
  deleted, O-MATTER becomes removable") went with DEF-MATTER.
- **Contradictions that must be caught** (twelve, every one caught): ITE & W2; INFOS; a planted signal in linear QM;
  F1 & F2b under {N_KEYING, N_2BVIA}; F2b under {N_FRW, N_2BVIA}; ITB & RQ under {N_QTOPO}; W2 at 1 AU, N = 7 without
  H12 under {N_EPS} (wave 4: with OPEN pathways held false); and, new in wave 3: **W2 alone signals nothing**; **ITB under {N_QTOPO, N_CORR}**; **F2b under
  {N_FRW, N_DCTC}**; **ITE & F2b under {N_DCTC}**; **a planted D-CTC channel without clause 2b**.
- **Results that used to be clashes:** F1 & F2b, and ITB & RI & RQ, are consistent as commitments.
- **STRUCTURAL, not counted.** Supports are drawn only from premise sets consistent with the variant (engine
  construction); its content is the control that the wave-1 engine at 1 AU, N = 7 reports **3 of 3** vacuous REMOVED-IF.
- **Named-premise census** (can a premise fail at all?):

  | named premise | inadmissible in (1 ly) | in a support (1 ly) | at 1 AU, N = 7 (W2 variants) |
  |---|---|---|---|
  | N_EPS | 0 — **STRUCTURAL at 1 ly**; every such support flagged **admissible given W_W2** (wave 5) | 864 | **inadmissible in 576** (empty window, no H12) |
  | N_DCTC | 2,880 ({N_FRW}: 2,304; ITE: 576) | 2,304 | 576 |
  | N_FRW | 2,880 | 2,879 | 576 |
  | N_2BVIA | 2,880 | 0 | 576 |
  | N_QTOPO | 1,536 (RQ; N_CORR) | 768 | 384 |
  | N_KEYING | 1,440 | 1,440 | 288 |
  | N_CORR | 768 (N_QTOPO / N_MEASPHYS) | 2,879 | 192 |
  | N_MEASPHYS | 768 | 384 | 192 |
  | N_SIGKEY, N_MS17, N_H12W | 0 — **STRUCTURAL: assuming them cannot fail** | 288 / 1,152 / 0 | N_H12W in a support in 432, never inadmissible |
  | **N_W2ANC** (wave 4) | 0 — **STRUCTURAL: assuming it cannot fail** (no READ bound reaches its field) | 864 | in a support in 864, never inadmissible |

  At 1 AU, N = 7, N_EPS is in a support in 432 variants (all with H12 + N_H12W). Without H12 it is inadmissible (576
  variants) and support 1 reads OPEN via N_WREAD. Every count is wave 4's × 3/2 (*wave 4 first said* 576, 384, 1,920
  ...), because SHAPE adds a third consistent H-INFO option and changes no verdict.

  *Wave 2 first said* N_FRAME3b, N_SIGKEY, N_CORR, N_MS17 and N_H12W were never constrained; N_FRAME3b is withdrawn
  and N_CORR is now constrained by B-QCORR.
- **Encoding drift: z3 against the A-reports' own wave-4 grades.** 32 (variant, cell, grade) rows, parsed by stated
  rules (`parse_report_class`: P1 every parenthetical dropped; P2 aliases; P4 corridor clause; **P7** the clause for
  the variant's H-IT reading; **P8** the first clause outside braces; **P9** LEFT-IF reads OPEN; P3 precedence;
  `z3_class`: Z1 a removal or non-binding counts for a hypothesis only if a support contains it; Z2 OPEN via N_VAC is
  not carried; Z3 an NB returns its removal's OPEN; Z4 the five-way O-MAKE is the weaker form; **Z5** the five-way
  O-LOOP counts only if both forms are removed or not-bound; **P10**, wave 5: an A-report's "O-MATTER" text is compared
  with z3's O-SEAT). There are now **33 rows**, adding A3's H-INFO-SHAPE grade, read from `measure.GRADES` because A3's
  JSON has no such row. **172 of 173 comparisons agree.** All five SHAPE comparisons agree: O-SEAT reads "RELOCATED to
  O-SEAT, LEFT there" → N, and z3 gives LEFT. *Wave 4 first said* 167 of 168; *wave 3* 166 of 168. The one that does
  not:

  | report, variant, obstruction | why z3 differs |
  |---|---|
  | A2, {F2b}, O-MAKE | **Vocabulary.** A2: "NOT-BOUND-IF {2b's CTC; Geroch-compact case only}; Tipler's non-compact case still binds". The screen's NOT-BOUND needs every theorem of the obstruction unbound, so with Tipler binding O-MAKE-TOPO stays bound (and five-way O-MAKE also needs O-MAKE-DIST, OPEN via N_VAC only). A2's own D-CTC row grades the same world's O-MAKE LEAVES. Both say O-MAKE is not lifted. |

  The A2 entry stays because its cause is a difference of vocabulary, not a fault on either side: there is nothing to
  repair, and a parse rule that read A2's partial non-binding as "not lifted" would only rename the difference.
  *Wave 3 first said* a second row: "A3, {ITB, RI}, O-LOOP | **A3 omission, open for A3's stage** ..." — repaired by
  R3-alone (A3 wave 4); the entry is deleted from `EXPLAINED` and kept in `EXPLAINED_HISTORY`, and the guard agrees.

  **CONTROLS:** three mutated encodings, each caught as an unexplained disagreement: `KR-unconditional` (170/173),
  `wave1-THROAT` (168/173), `wave2-SLICE-INTRINSIC` (169/173) (*wave 4:* 165, 163, 164 of 168). **Ground rows (wave 4, per support):**
  `settle.h12_carrier_case` at 1 AU, N = 7 says EXCLUDED under H-TRANSFER — the computation *given* W_W2, as A1 wave 4
  states — and NOT EXCLUDED under H-12-CARRIER; z3's support-1 route (`support1-only`) gives {W2, F1} **OPEN via
  N_WREAD** and {W2, F1, H12} REMOVED-IF; A1's wave-4 field for those cells reads "LEFT-IF W_W2 -> OPEN". They agree.
  With both supports z3 gives {W2, F1} REMOVED-IF {W2, F1; N_W2ANC} at 1 AU. CONTROL: wave 3's settled window gives
  LEFT. *Wave 3 first said* "z3 gives {W2, F1} LEFT ... They agree."
- **Load-bearing guard** (RV-0 #6): 13 combination rows checked (*wave 3:* 12); every row crediting a removal or
  non-binding has every graded literal load-bearing, or says a member adds nothing (A1 W2 × H12 under H-TRANSFER;
  **A1 KR × H12, wave 4**; A3 H-SETTLE × H-INFO; A4's six H-ZERO / H-NULL × H-IT rows, whose ZERO / NULL add nothing).
  All agree.
- **Grounds re-run, each against an independent computation or with content:** tanh(2εT); C1 2.2e-16; the drift
  ordering against tanh(2ε(T − t_A)) at t_A < T; the antitelephone against −uL; cosmic keying, 0 failures at ranks 2
  and 3; the FRW lemma (unsat; vacuity sat; control a ≥ 0 sat); nlcontrol N < 7 impossible, CMAX = log₂1.25; H-12
  carrier flips, 2; LOCC 8.9e-16; QEI fraction 2.08e-68 (under {H_flat, H-PATH, H-MIN-SCALAR}); zero shift `unsat`;
  EGJ β_crit = −r0²/2 = 1.91e69 l_P² at 1 m, r⁴T_kk → −2r0², β = 0 reproduces R_kk; INFOS support; and, new:
  **D-CTC** four axes 2.000000 bits per pair (C2), BB84 1.000000; **zero-error** 1 codeword at D < 1, control 2/4/8;
  **W2 member without H-QUBIT-DRIFT** χ = 2.000000, P(b′\|b) = identity; **wave 4:** `w2_ancilla_flow_k` χ = 2, 3, 4
  at d = 8, 16, 32 with zero error (controls: linear 0, antipodal collides); **windows** 1 ly N = 7 open, 1 AU N = 7 and
  N = 10³ empty, 1 AU N = 10⁶ open; the board flags and LEDGER S5/S10/S13; and, **new in wave 5**, three more:
  - **O-SEAT as encoded**: `massform.MECHANISM_VERDICT` is REFUSED on six readings; S13 forms no baryons;
    HIGGS_COUPLING_CARRIES_B_OR_L is False; `measure.info_shape_screen` reproduces clash (d) for INFOS and dissolves it
    for SHAPE; LEDGER S12 OPEN; the S13 price figures are imported;
  - **the support-2 field figure per member**, against independent constants;
  - **`settle.window_given` against combine's z3 window** in all 12 (cell, reading) rows.

### Contradictory combinations: every core, counted by inclusion-exclusion

Of the 8,191 variants, **5,759 are consistent and 2,432 are not** (*wave 4:* 3,839 and 2,304 of 6,143). Every one of
the 127 combinations has a consistent variant. 416 inconsistent variants have more than one core. **SHAPE enters no
core.**

| clash | cores (variants) | present in | alone in | what collides | label |
|---|---|---|---|---|---|
| **(c) W2 + ITE** | C-ITE + C-W2, linearity (512); C-ITE + B-GISIN + C-F1 (256); C-ITE + B-GISIN + C-F2b (256) | 512 | 384 | ER=EPR as MS state it (fn.1 p.2; §3.1 p.16; §5.4 pp.36-37, READ) against a per-branch drift; T-B: the drift signals 0.537 at β = 0 in Van Raamsdonk's state | **INCONSISTENT-AS-ENCODED**: a test of ER=EPR, not a refutation of W2. *Wave 1 first said* REFUTED. |
| **(d) INFOS** | C-INFOS + B-RECV (2,048) | 2,048 | 1,920 | H-INFO-S against B-RECV | **CLASH, board versus M. M ruled 2026-10-03 for H-INFO-SHAPE** (items 1 and 5). INFOS is kept as the alternative reading, and its clash stands under it as history. SHAPE ∧ B-RECV is SAT: dissolved by relocation. Not a retirement. *Wave 4 first said* "M's to rule". |

Intersection 128; union 512 + 2,048 − 128 = **2,432**, the inconsistent count. (*Wave 4:* 384 + 2,048 − 128 = 2,304;
*wave 2:* 1,792 over 4,607.)

**B-RECV's conditions, listed beside clash (d).** M ruled for H-INFO-SHAPE, under which B-RECV holds. These are what
the alternative reading H-INFO-S would still have to overturn (A3 wave 3;
`LEDGER.md` lines 50, 67, 70, 181, READ this pass):

- **S10 rests on C3**: it holds for renormalisable couplings, dimension ≤ 4; LEDGER: "a higher-dimension operator
  carrying B or L would reverse it";
- **P-UNIFORM**: the vev takes one value wherever nothing sources it (a named premise, M-D65-4);
- **H-UNSOURCED-SEAT**: nothing holds a source at the seat before arrival; where it fails, what remains is the
  held-seat release route S13 (OPEN, priced, forming no baryons);
- **Bekenstein's scope**: "complete, weakly self-gravitating, isolated objects" (quant-ph/0404042v1 p.2), with E the
  gravitating energy;
- **φ(1) = 0** needs 2^I distinguishable states at the destination, not that they be matter already there: the
  condition is "the holder's states are material";
- **transit.CARRIES_SUBSTANCE False**: a receiver must be there.

**Premise clashes** (consistent variants that cannot carry a named premise), at 1 ly, N = 7:

| premise clash | present in | alone in | reading |
|---|---|---|---|
| {N_2BVIA, N_FRW} with F2b | 2,880 | 0 | exact FRW excludes clause 2b if corridors are the route to the cosmic past |
| {N_DCTC, N_FRW} with F2b | 2,304 | 0 | **new:** a global time function admits no CTC, so exact FRW excludes the D-CTC channel |
| {N_2BVIA, N_KEYING} with F1 + F2b | 1,440 | 0 | the docket's keying excludes clause 2b (wave 1's clash a; not in M's sentence) |
| {N_CORR, N_QTOPO} with ITB | 768 | 192 | **new (RV-1 #2):** one corridor, two accounts |
| {N_QTOPO} with ITB + RQ | 768 | 192 | ITB's no-geometric-throat premise against R-QUANTUM's throat |
| {N_DCTC} with F2b + ITE | 576 | 0 | **new:** MS linearity against the D-CTC's nonlinearity |
| {N_CORR, N_MEASPHYS} with ITB + RI | 384 | 0 | **new:** the same, through R-INDEX |
| {N_MEASPHYS} with ITB + RI + RQ | 384 | 0 | the same, through R-INDEX |

Union by inclusion-exclusion 3,648 (*wave 4:* 2,432). At 1 AU, N = 7 (W2 variants), **{N_EPS} with "not H12"** is
added: 576 variants (192 alone), the empty window; union 960 (*wave 4:* 384, 128, 640).

**Wave 1's clash census, recomputed** over wave 1's 3,071 variants: (a) F1+F2b present 768 (alone 640), (b) ITB+RI+RQ
256 (192), (c) ITE+W2 256 (192); union 768 + 256 + 256 − 64 − 64 = 1,152. *Wave 1 first said* "(a) 640, (b) 256,
(c) 256", the core z3 happened to return.

## 3. The answer, in detail

Computed by `headline()` over every consistent variant and every account at 1 ly, N = 7 (wave-5 re-run with SHAPE).
Every maximum and every smallest variant is unchanged from wave 4; every variant count is wave 4's × 3/2, because SHAPE
is a third consistent H-INFO option that changes no verdict. `headline_au` at 1 AU, N = 7: member-attributed removals
max 1 (always O-BITS), in 864 variants, smallest {W2, F1}, through support 2 or, with H12, support 1. The D-CTC is the
other route. *Wave 4 first said* 576 there; *wave 3* 480.

| figure (per account, never across two) | maximum | variants attaining it | smallest |
|---|---|---|---|
| **member-attributed removals** (five-way) | **1** (always O-BITS) | 2,592 (*wave 4:* 1,728) | {F2b} (D-CTC); {W2, F1} for the drift |
| NOT-BOUND-IF (five-way) | 2 (O-HOLD, O-LOOP) | 384 (256) | {ITB} |
| removed with no member (five-way) | 1 (O-LOOP) | 2,879 (1,919) | {F1} |
| removed only, member or not | 2 (O-BITS + the geometry's O-LOOP) | 288 (192) | {W2, F1} |
| removed or not-bound (wave 2's figure, now per account) | 3 | 48 (32) | {W2, F1, ITB} |

**The variant with the most member-attributed results, {W2, F1, ITB}, at 1 ly, N = 7, in its two accounts:**

| form | account A (N_CORR dropped; N_QTOPO assumed) | account B (N_QTOPO dropped; N_CORR assumed) | supports (all accounts) |
|---|---|---|---|
| O-BITS | **Rm** | **Rm** | {W2, F1; N_EPS} [admissible given W_W2] \| {W2, F1; N_W2ANC} [unevaluated] (wave 4: two supports; wave 5: flags) |
| O-MAKE-TOPO | **NBm** | — (LEFT) | NOT-BOUND-IF {ITB; N_QTOPO}; removal OPEN via N_ILFREE |
| O-MAKE-DIST | — | — | OPEN via N_VAC only |
| O-HOLD | **NBm** | — (LEFT) | NOT-BOUND-IF {ITB; N_QTOPO}; removal OPEN via N_ILFREE |
| O-SEAT (wave 4: O-MATTER) | — | — | LEFT (S10 refused as a supply; S13 forms no baryons) |
| O-LOOP-C | **NBm** | **Rg** | NOT-BOUND-IF {ITB; N_QTOPO}; REMOVED-IF {N_CORR, N_FRW} \| {F1; N_CORR, N_KEYING} |
| O-LOOP-S | **Rg** | **Rg** | REMOVED-IF {N_SIGKEY} |

So the same three hypotheses give **either** one member removal plus two non-bindings (account A) **or** one member
removal plus the geometry's loop removal (account B), never both. F1's keying route is an *alternative* to the
geometry's, and in every account that admits N_FRW the removal holds without F1 (`Rg`).

**What is never removed by a member:** O-MAKE (both forms), O-HOLD, O-SEAT and both forms of O-LOOP. O-MAKE-TOPO and
O-HOLD are at most NOT-BOUND-IF. **Survivors of every consistent variant (both screened cells):**

- **O-SEAT**, LEFT in all 5,759 consistent variants and all 1,152 consistent W2 variants at 1 AU, N = 7. This is
  STRUCTURAL, because the refusals are bare; the controls carry the content.
- **O-MAKE-DIST**, OPEN via N_VAC only.

*Wave 4 first said* "O-MATTER (LEFT in all 3,839 consistent variants and all 768 ...)".

**Synergy (JOINT) and interference.**

- **Synergy: W2 × F1 on O-BITS.** At 1 ly: 240 variants ({W2, F1}), plus 24 + 24 with ITB (and RI). At 1 AU, N = 7:
  120 ({W2, F1}, through support 2) + 12 + 12, and 120 ({W2, F1, H12}, through either support) + 12 + 12. *Wave 4
  first said* 160 / 16 / 16 and 80 / 8 / 8, over 6,143 variants. *Wave 3 first said*
  "at 1 AU, N = 7 it needs H12: 80 variants" — support 2 was not encoded and support 1's exclusion was taken as settled.
  *Wave 2 first said* "Synergy: one, and it is H-12's ... At 1 ly there is no synergy". That rested on N_FRAME3b.
- **Interference** (a member's result undone in combination), at 1 ly:
  - clause 2b undoes the corridor O-LOOP removal (768 variants): a message into the cosmic past spoils the time
    function;
  - R-QUANTUM undoes ITB's non-binding (384 + 192);
  - **ITE undoes clause 2b's D-CTC O-BITS** (288, and 288 with F2b's own loop interference): MS linearity excludes
    the D-CTC.

  At 1 AU, N = 7 the same kinds appear (192, 96, 48, 48). *Wave 4:* 512; 256 + 128; 192; and 128, 64, 32, 32.

*Wave 1 first said:* the most is four entries of the six-way split, {W2, F1, ITB, R-INDEX}, with O-HOLD REMOVED.

## 4. JOINT and INDEPENDENT combinations, and the instrument tests

A consistent variant is **complementary** when more than one member contributes a member-attributed result and no
single member's result covers it. Wave 3 splits these (RV-0 #9, RV-1 #7): **JOINT** if some member-attributed result
belongs to no single member (a synergy); **INDEPENDENT** otherwise (every contribution is a single member's own).

- **JOINT: 288 variants at 1 ly in 3 classes, and 288 at 1 AU, N = 7 in 6 classes**, all W2 × F1 (× H12 at 1 AU) on
  O-BITS. Each has a content-bearing test (T-A, T-B, T-E, T-K; T-G for the H12 classes). This check can fail and is
  counted. *Wave 4 first said* 192 and 192; *wave 3* 96 at 1 AU in 3 classes.
- **INDEPENDENT: 672 variants at 1 ly, 96 at 1 AU** (*wave 4:* 448, 64) — F1 × ITE (O-MAKE-TOPO non-binding beside F1's loop route), F2b ×
  ITB (the D-CTC's O-BITS beside ITB's non-bindings) and their supersets. **Not instrument-tested as pairs**: each part
  is graded in its member's report; no instrument computes the pair. Reported STRUCTURAL.
- Tests are assigned by a table fixed before the screen runs (`TEST_BEARS`, wave 4 adding T-K); there is no fallback. **T-D, T-F, T-H and
  T-I are records**, cover nothing, and say so.

**T-A: W2 × F1.** `frame.drift_ordering`: 0.5371 / 0.4219 / 0.2913 / 0.1489 as Alice measures at 0, ¼, ½, ¾ of Bob's
window, against tanh(2ε(T − t_A)) to 1.2e-5 (the Bob-first 0 is STRUCTURAL). Reply keyed to the sender's frame −3/5,
to the cosmic frame 0. Cosmic keying 0 failures at ranks 2, 3. H-IT's model adds no signal: 1.55e-15. **PASS.**

**T-B: W2 inside H-IT's own READ model** (`tfd_drift`; ε = 0.1, T = 3 illustrative; the slicing is F1's):

| β | S (bits) | C2 signal (exact) | linear | C1 |
|---|---|---|---|---|
| 0 | 1.000 | 0.53705 (= tanh 0.6) | 0 | 0 |
| 0.5 | 0.956 | 0.50796 | 0 | 0 |
| 1 | 0.840 | 0.43186 | 0 | 0 |
| 2 | 0.527 | 0.24001 | 0 | 0 |
| 4 | 0.130 | 0.04204 | 0 | 0 |
| 8 | 0.0044 | 0.00080 | 0 | 0 |
| 30 | 0.000 | 0.00000 | 0 | 0 |

The channel runs on the bridge and does not replace it. **PASS.**

**T-C: the drift cannot make its own pairs.** Product states 2.9e-15 against the Bell control's 0.53706; local
unitaries change entropy by 8.9e-16, the nonlocal control by 1.965 bits. **PASS.**

**T-D (record): the holder floors.** 33.2 / 144 / 379 / 99.1 J at R = 1 m (measure's four counts of a 70 kg body),
matching the CODATA cross-check exactly. Floors, not prices; the one READ-backed holder is the body, Mc² = 6.29e18 J.
*Wave 2 still assigned it as a covering test.*

**T-E: W2 × F1 end to end.**

- **The ε window** (z3 over the reals; ε_max from the NAMED-NOT-READ Majumder figure, 2.39e-5 s⁻¹ reading A,
  1.19e-5 s⁻¹ reading B; both readings agree in every row):

  | distance | N (floor) | ε_any (s⁻¹) | consistent? | wave 1's ε at T = L/2c |
  |---|---|---|---|---|
  | 1 ly | 7 | 3.64e-8 | yes → **admissible given W_W2** (wave 5; would close at a bound 655× (A) / 328× (B) tighter) | 7.29e-8 |
  | 4.24 ly | 7 | 8.59e-9 | yes → admissible given W_W2 | 1.72e-8 |
  | 1 AU | 7 | 2.30e-3 | **no** → support 1 OPEN via N_WREAD (wave 4) | 4.61e-3 |
  | 1 AU | 1,000 | 1.06e-4 | **no** → support 1 OPEN via N_WREAD (wave 4) | 2.11e-4 |
  | 1 AU | 10⁶ | 3.34e-6 | **yes** → **admissible given W_W2** (wave 5; 7.16× / 3.58×) | 6.67e-6 |

  None of the 18 entries flips between the two ε. The ratio 2.000000 is an identity of T = atanh(D_N)/(2ε)
  (**STRUCTURAL**, not counted; *wave 2 counted it*). Every "consistent?" is computed against the NAMED-NOT-READ value:
  a "no" is LEFT-IF W_W2, hence OPEN pending a READ (wave 4; *wave 3 first said* the 1 AU rows settled the cells), and
  a "yes" is admissible GIVEN W_W2, flagged and not settled (wave 5, V3 problem 3: M's rule both ways; *wave 4 first
  said* "computed open" with no flag). The flag is carried on each z3 support and checked against
  `settle.window_given` in all 12 rows. This
  window is support 1's only; support 2 has none (T-K).
- **Timing.** The drift time does not depend on distance and is a **floor** (D_N is the least D with N·C(D) ≥ 2).
  At the unread limit, reading A, N = 7: T = **13.38 h**; once pairs and holder are in place the read is 0.99847 L/c
  early at 1 ly. Not a measured time; an upper limit consistent with zero is not evidence of a drift.
- **First transit** (`settle.first_transit_times`): midpoint source (LEDGER D23 as corrected in DOCKET 67), read at
  L/2c + T = **0.50153 yr** after the source fires, beating light launched from Alice at that moment (1 yr) —
  conditional on N_EPS, H-C2, F1 (H-FRAME3b ⇐ F1) and H-BLOCK. One-end distribution never beats light. Control: at
  1 AU, T = 13.38 h > L/2c = 250 s, and the midpoint case fails.
- **Pairs per teleported qubit:**

  | hypothesis | pairs per qubit |
  |---|---|
  | nlcontrol (H-NLCONTROL-FORM), coded alone | ≥ 7 (floor; never zero-error) |
  | nlcontrol, block-coded (H-BLOCK) | ≥ 6.21 on average (floor) |
  | qubit-only subclass (H-BORN-AT-BOB + H-QUBIT-DRIFT) | > 2 on average; ≥ 3 at finite T |
  | W2 member without H-QUBIT-DRIFT, four-axis instance (`w2_ancilla_flow`, H-EXTEND) | 1, zero-error |
  | W2 class without H-QUBIT-DRIFT (`w2_ancilla_flow_k`, k = 8, 16; T-K) | 2/3, 1/2, zero-error: 2/(log₂d − 1), **no positive floor** in the computed range |
  | clause 2b's D-CTC, four-axis construction (N_DCTC) | 1, zero-error — **that construction only**; the route ≤ 1, minimum OPEN (BHW 0811.1209v2 p.4: unbounded if CTC qubits are free) |

  | count (A3's H-FAITHFUL) | teleportation ebits | nlcontrol, N = 7 (floor) | block-coded (floor) | qubit-only subclass (strictly above) | four-axis W2 member / D-CTC (zero-error; the classes go lower) | holder FLOOR at R = 1 m |
  |---|---|---|---|---|---|---|
  | species sequence | 9.51e27 | 6.66e28 | 5.91e28 | 1.90e28 | 9.51e27 | 33.2 J |
  | grid 1 Å | 4.14e28 | 2.90e29 | 2.57e29 | 8.28e28 | 4.14e28 | 144 J |
  | grid 0.1 Å | 1.09e29 | 7.61e29 | 6.76e29 | 2.18e29 | 1.09e29 | 379 J |
  | thermal entropy | 2.84e28 | 1.99e29 | 1.76e29 | 5.68e28 | 2.84e28 | 99.1 J |

  The four-axis column is one construction's figure: the W2 class at k = 16 needs half of it (species sequence
  4.75e27), and the D-CTC route's minimum is OPEN. *Wave 3 first said* "W2 member without H-QUBIT-DRIFT ... | 1,
  zero-error" and "clause 2b's D-CTC, four axes | 1, zero-error", read as the classes' figures (V2-1 problem 1, V2-0
  problem 7). *Wave 2 first said:* "nlcontrol pairs, N = 7 (upper figure, one Hamiltonian)" and "W2 class floor,
  H-BORN-AT-BOB".
- **PASS.**

**T-F (record): RQ × KR.** Two OPENs on O-HOLD. The QEI fraction 2.08e-68 holds under {H_flat, H-PATH,
H-MIN-SCALAR}; ξ > 0, curved-space QEIs (NAMED-NOT-READ) and ε_G are OPEN. *Wave 2 first said* "in-scope fraction".

**T-G: W2 × F1 × H12 at 1 AU, N = 7 — per support (wave 4).** `settle.h12_carrier_case` flips 2 of 9 cells (1 AU at
N = 7 and N = 10³; "EXCLUDED" there is the computation given W_W2). z3: support 1 alone gives {W2, F1} **OPEN via
N_WREAD** at 1 AU, N = 7; with both supports {W2, F1} is REMOVED-IF {W2, F1; N_W2ANC} and {W2, F1, H12} is REMOVED-IF
{W2, F1; N_W2ANC} \| {W2, F1, H12; N_EPS, N_H12W}; at 1 ly {W2, F1} is REMOVED-IF {W2, F1; N_EPS} \| {W2, F1; N_W2ANC}.
**PASS.** No READ source gives a model of a Weinberg-form drift in G or v (N_H12W). At 1 AU, N = 10⁶ H-12 adds nothing.
*Wave 3 first said* "z3 gives {W2, F1} LEFT ... at 1 AU, N = 7".

**T-H (record): ITJ.** `geometry.egj_fR_throat`: T_kk(r0) = 2(−2β − r0²)/r0⁴, ≥ 0 iff β ≤ −r0²/2 (1.91e69 l_P² at
1 m, against EGJ's β ~ l_P²); r⁴T_kk → −2r0² for every β: for the computed shape and f the deficit is moved, not
removed. The pathway (N_EQUIL) is H-IT's in the Jacobson reading. *Wave 2 first called it "(ZERO | NULL) × IT".*

**T-I (record): INFOS vs B-RECV.** φ(1) = 0 bits, Bekenstein 0 bits at E = 0, CARRIES_SUBSTANCE False. **Wave 5:**
`measure.info_shape_screen` (H-SHAPE-ENCODING, M-apply's) is recorded beside it. INFOS ∧ RECV is unsat (clash (d)
reproduced) and SHAPE ∧ RECV is sat (dissolved). Under SHAPE, O-SEAT removed and O-SEAT left are both sat in that
seven-atom screen, because its S13 atom is free. Combine encodes LEDGER S13's "forms no baryons", so in combine O-SEAT
is LEFT, which is M-apply's grade. The two screens differ in how much of the board they encode, not in the verdict.

**T-J: clause 2b's D-CTC.** `frame.four_basis_c2_table` (BHW 0811.1209v2 pp.3-4 construction, READ by A2):
2.000000 bits per pair under C2, map reproduced with P = 1, condition-2 minimum 0.1738; `bb84_c2_table` 1.000000. C1
gives 0 (STRUCTURAL: the same input for every choice). z3 {F2b}: O-BITS REMOVED-IF {F2b; N_DCTC}. O-LOOP reintroduced.
Pairs per teleported qubit: four axes 1, BB84 2 — those constructions'; the route ≤ 1 with its minimum OPEN (BHW p.4).
A k-axis D-CTC table is not computed (R3-alone: the Cesàro fixed point at CTC dimension 16 is too slow). **PASS.**

**T-K (wave 4): W2 × F1, support 2.** `settle.w2_ancilla_flow_k` (imported; same construction as `w2_ancilla_flow`,
k axes on one hemisphere, an m-qubit ancilla, the field read from each branch's own state):

| k axes | d | χ (bits per pair) | Bob's error | pairs per teleported qubit | min curve separation (rad) | grid step (rad) | max‖H‖T |
|---|---|---|---|---|---|---|---|
| 4 | 8 | 2.000000 | 0 | 1 | 0.391 | 0.0072 | 1.431 |
| 8 | 16 | 3.000000 | 0 | 0.667 | 0.337 | 0.0074 | 1.484 |
| 16 | 32 | 4.000000 | 0 | 0.5 | 0.180 | 0.0078 | 1.556 |

CONTROLS: one state-independent unitary gives χ = 0 (k = 16); antipodal axes give χ below log₂k with colliding curves
(k = 8). z3 {W2, F1} lists {W2, F1; N_W2ANC} as a support. **Field figure, both ways, per member (wave 5, V3
problem 1):** support 2 needs ‖H‖ ≥ max‖H‖T · c/L, and each member's figure uses that member's own max‖H‖T:

| member (construction) | max‖H‖T | needed ‖H‖ at 1 ly (s⁻¹) | needed ‖H‖ at 1 AU (s⁻¹) | IF H-MAP-W2: × ε_max at 1 AU, reading A / B |
|---|---|---|---|---|
| `w2_ancilla_flow` (four-axis member, d = 8) | 1.4654 | 4.643e-8 | 2.937e-3 | 123.0 / 246.0 |
| `w2_ancilla_flow_k(4, 2)` (k = 4, d = 8) | 1.4306 | 4.533e-8 | 2.867e-3 | 120.1 / 240.1 |
| `w2_ancilla_flow_k(8, 3)` (k = 8, d = 16) | 1.4843 | 4.703e-8 | 2.974e-3 | 124.6 / 249.2 |
| `w2_ancilla_flow_k(16, 4)` (k = 16, d = 32) | 1.5556 | 4.929e-8 | 3.118e-3 | 130.6 / 261.1 |

No READ bound maps onto that field, so the screen leaves the window unevaluated. IF H-MAP-W2 held (the unread
Majumder precession figure read as a bound on ‖H‖, which is adopted nowhere), the 1 AU cell would be excluded for
every member under both readings (ε_max 2.39e-5 / 1.19e-5 s⁻¹) and the 1 ly cell would not. *Wave 4 first said*
"4.53e-8 s⁻¹ at 1 ly and 2.87e-3 s⁻¹ at 1 AU (four-axis max‖H‖T = 1.465 from `w2_ancilla_flow`)". Those two figures
are k = 4's (1.4306); 1.465 gives 4.64e-8 and 2.94e-3. The separation shrinks with k, so H-EXTEND asks for ever
finer field variation; nothing here is evidence such a drift exists. **PASS.**

## 5. Each hypothesis across every combination (rule 2)

Charter rule 2: *"A failure alone does not retire a hypothesis. It is retired only if it also fails in every
combination tested."* Retirement is established only for an **exercised** literal; the difference census measures it.

| literal | exercised? (changed / with it) | what it contributes | rule 2 |
|---|---|---|---|
| W2 (H-SETTLE, C2) | yes: 800 / 2,048 | O-BITS REMOVED-IF {W2, F1; N_EPS} \| {W2, F1; N_W2ANC} (or F2b for F1), JOINT; clash (c) with ITE | **kept** (load-bearing in W2 × F1, both supports). Alone: LEAVES-ALL |
| W1 (H-SETTLE, C1) | **no** (0) | its one commitment, no signal, is the board's | **UNTESTED-BY-SCREEN**; its grade (LEAVES-ALL, 2.2e-16) stands |
| KR (H-SETTLE) | yes: 1,152 | O-HOLD OPEN via N_EPSG; removes nothing | kept: OPEN pathway |
| F1 (clause 1) | yes: 1,984 / 4,096 | supplies W2's slicing (O-BITS, JOINT); O-LOOP-C REMOVED-IF {F1; N_CORR, N_KEYING}, an alternative to the geometry's | **kept** |
| F2b (clause 2b) | yes: 3,136 | O-BITS REMOVED-IF {F2b; N_DCTC} (D-CTC), O-LOOP reintroduced; supplies W2's slicing; undoes the corridor loop removal | **kept** |
| ITB (H-IT) | yes: 1,536 / 2,048 | O-MAKE-TOPO, O-HOLD, O-LOOP-C **NOT-BOUND-IF** {N_QTOPO}; removal OPEN via N_ILFREE | kept: NOT-BOUND-IF, no removal |
| ITE (H-IT) | yes: 1,664 | O-MAKE-TOPO NOT-BOUND-IF {N_MS17}; clash (c) with W2; excludes the D-CTC | kept: NOT-BOUND-IF |
| ITJ (H-IT, new) | yes: 1,536 | O-HOLD OPEN via N_EQUIL; removes nothing (moved, not removed, for the computed shape) | kept: OPEN pathway |
| H12 | yes, **at 1 AU, N = 7 only** (576 changed — only the premise clash {N_EPS} changes; in a support 432; *wave 4:* 384, 288) | support 1's window: O-BITS REMOVED-IF {W2, F1, H12; N_EPS, N_H12W}, an **alternative** to support 2's {W2, F1; N_W2ANC}; without H12, support 1 is OPEN via N_WREAD | **kept** (on support 1's window only; it changes no verdict once support 2 is counted). Not retired. *Wave 3 first said* it flipped O-BITS LEFT → REMOVED-IF |
| INFO (necessity) | **no** (0) | none | **UNTESTED-BY-SCREEN**; retirement neither established nor refuted |
| INFOS (sufficiency; the alternative reading) | yes: all 2,048 inconsistent | clash (d) | **CLASH, board versus M; M ruled 2026-10-03 for H-INFO-SHAPE.** INFOS is kept as the alternative, and its clash stands as history. *Wave 4 first said* "M's to rule" |
| **SHAPE (H-INFO-SHAPE, M's ruling; wave 5)** | **no** (0 / 2,048) | none: its one commitment (the substance is at the seat ⇒ RECV) is the board's B-RECV; it enters no clash core | **UNTESTED-BY-SCREEN** (inert). It is consistent with B-RECV (clash (d) dissolved by relocation) and removes nothing (A3: LEAVES-ALL). O-MATTER is relocated to O-SEAT, which stays LEFT until the seat's supply is shown |
| ZERO (H-ZERO) | **no** (0 / 4,096) | none on any obstruction (its result, the zero is free, touches none) | **UNTESTED-BY-SCREEN**. *Wave 2 first said* "kept: OPEN pathway" via N_EQUIL |
| NULL (H-NULL) | **no** (0 / 4,096) | none (EGJ has no null-information term) | **UNTESTED-BY-SCREEN**. *Wave 2 first said* "kept: OPEN pathway" |
| RI (R-INDEX) | yes: 768 | with ITB an alternative NOT-BOUND-IF support {ITB, RI; N_MEASPHYS} | kept (never needed) |
| RQ (R-QUANTUM) | yes: 2,304 | O-HOLD OPEN via N_XI, N_QEIC; undoes ITB's non-binding | kept: OPEN pathway |

**Load-bearing** (in some support): W2, F1, F2b, ITB, ITE and RI at 1 ly; plus H12 at 1 AU, N = 7. **Named premises
ever used:** N_CORR, N_DCTC, N_EPS, N_FRW, N_KEYING, N_MEASPHYS, N_MS17, N_QTOPO, N_SIGKEY, **N_W2ANC** (wave 4); plus
N_H12W at 1 AU. OPEN pathways: N_WREAD (wave 4) appears at 1 AU only, in support 1's route.

## 6. Every combination (127, plus readings only)

Generated by `python3 combine.py --table PATH` from the 1 ly, N = 7 screen. For each combination the best consistent
variant and **one account** (premises dropped named) are shown: first by member-attributed removals, then by
not-bound, then by removed-or-not-bound. Codes per form: **Rm** removed by a member; **Rg** removed with no member
(geometry / board / premise); **NBm** not-bound, member-attributed; OPEN; **S** silent; **L** left (S and L are read
off the union of accounts; in the D-CTC account the CTC is itself a loop). **"Adds nothing"** names members of the
best variant that are in no support of a member-attributed result — the row then adds nothing for them. The last
column is the 1 AU, N = 7 re-screen of the combination's W2 variants (wave 4: both supports counted, so W2 × F1
variants without H12 now count there through support 2; only this column changed from wave 3, which said e.g. "8/12"
for SET+FR and "16/36" for IT+SET+FR, now 12/12 and 24/36). **Wave 5:** regenerated from the re-screen with SHAPE. H-INFO now has three readings,
so every combination containing H-INFO has 4/3 as many variants; the obstruction column reads SEAT where it read MATTER
(O-SEAT, LEFT in every row); and no best variant, account or code changed.

| # | combination | variants | consistent | clash (literals in core) | premise clashes | best variant (one account) | BITS/TOPO/DIST/HOLD/SEAT/LOOP-C/LOOP-S | member-attributed removals | NOT-BOUND-IF | removed with no member (geometry / board / premise) | load-bearing members; adds nothing | joint / independent variants | 1 AU, N = 7: W2 variants with O-BITS member-removed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IT | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB | 0 / 0 | - |
| 2 | SET | 12 | 12 | - | - | W2 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2 | 0 / 0 | 0/4 |
| 3 | FR | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b | 0 / 0 | - |
| 4 | 12 | 4 | 4 | - | - | H12 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12 | 0 / 0 | - |
| 5 | INF | 12 | 8 | INFOS | - | INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO | 0 / 0 | - |
| 6 | ZER | 4 | 4 | - | - | ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: ZERO | 0 / 0 | - |
| 7 | NUL | 4 | 4 | - | - | NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: NULL | 0 / 0 | - |
| 8 | IT+SET | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2 | 0 / 0 | 0/12 |
| 9 | IT+FR | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB | 0 / 8 | - |
| 10 | IT+12 | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12 (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12 | 0 / 0 | - |
| 11 | IT+INF | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO | 0 / 0 | - |
| 12 | IT+ZER | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: ZERO | 0 / 0 | - |
| 13 | IT+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: NULL | 0 / 0 | - |
| 14 | SET+FR | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1 | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1 | 4 / 0 | 12/12 |
| 15 | SET+12 | 12 | 12 | - | - | W2,H12 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12 | 0 / 0 | 0/4 |
| 16 | SET+INF | 36 | 24 | INFOS | - | W2,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO | 0 / 0 | 0/12 |
| 17 | SET+ZER | 12 | 12 | - | - | W2,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,ZERO | 0 / 0 | 0/4 |
| 18 | SET+NUL | 12 | 12 | - | - | W2,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,NULL | 0 / 0 | 0/4 |
| 19 | FR+12 | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12 (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12 | 0 / 0 | - |
| 20 | FR+INF | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO | 0 / 0 | - |
| 21 | FR+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: ZERO | 0 / 0 | - |
| 22 | FR+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: NULL | 0 / 0 | - |
| 23 | 12+INF | 12 | 8 | INFOS | - | H12,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO | 0 / 0 | - |
| 24 | 12+ZER | 4 | 4 | - | - | H12,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,ZERO | 0 / 0 | - |
| 25 | 12+NUL | 4 | 4 | - | - | H12,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,NULL | 0 / 0 | - |
| 26 | INF+ZER | 12 | 8 | INFOS | - | INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,ZERO | 0 / 0 | - |
| 27 | INF+NUL | 12 | 8 | INFOS | - | INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,NULL | 0 / 0 | - |
| 28 | ZER+NUL | 4 | 4 | - | - | ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: ZERO,NULL | 0 / 0 | - |
| 29 | IT+SET+FR | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB | 8 / 20 | 24/36 |
| 30 | IT+SET+12 | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12 (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12 | 0 / 0 | 0/12 |
| 31 | IT+SET+INF | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO | 0 / 0 | 0/36 |
| 32 | IT+SET+ZER | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,ZERO | 0 / 0 | 0/12 |
| 33 | IT+SET+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,NULL | 0 / 0 | 0/12 |
| 34 | IT+FR+12 | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12 (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12 | 0 / 8 | - |
| 35 | IT+FR+INF | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO | 0 / 16 | - |
| 36 | IT+FR+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: ZERO | 0 / 8 | - |
| 37 | IT+FR+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: NULL | 0 / 8 | - |
| 38 | IT+12+INF | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO | 0 / 0 | - |
| 39 | IT+12+ZER | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,ZERO | 0 / 0 | - |
| 40 | IT+12+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,NULL | 0 / 0 | - |
| 41 | IT+INF+ZER | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,ZERO | 0 / 0 | - |
| 42 | IT+INF+NUL | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,NULL | 0 / 0 | - |
| 43 | IT+ZER+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: ZERO,NULL | 0 / 0 | - |
| 44 | SET+FR+12 | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12 | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12 | 4 / 0 | 12/12 |
| 45 | SET+FR+INF | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO | 8 / 0 | 24/36 |
| 46 | SET+FR+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: ZERO | 4 / 0 | 12/12 |
| 47 | SET+FR+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: NULL | 4 / 0 | 12/12 |
| 48 | SET+12+INF | 36 | 24 | INFOS | - | W2,H12,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO | 0 / 0 | 0/12 |
| 49 | SET+12+ZER | 12 | 12 | - | - | W2,H12,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,ZERO | 0 / 0 | 0/4 |
| 50 | SET+12+NUL | 12 | 12 | - | - | W2,H12,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,NULL | 0 / 0 | 0/4 |
| 51 | SET+INF+ZER | 36 | 24 | INFOS | - | W2,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,ZERO | 0 / 0 | 0/12 |
| 52 | SET+INF+NUL | 36 | 24 | INFOS | - | W2,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,NULL | 0 / 0 | 0/12 |
| 53 | SET+ZER+NUL | 12 | 12 | - | - | W2,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,ZERO,NULL | 0 / 0 | 0/4 |
| 54 | FR+12+INF | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO | 0 / 0 | - |
| 55 | FR+12+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,ZERO | 0 / 0 | - |
| 56 | FR+12+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,NULL | 0 / 0 | - |
| 57 | FR+INF+ZER | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,ZERO | 0 / 0 | - |
| 58 | FR+INF+NUL | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,NULL | 0 / 0 | - |
| 59 | FR+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: ZERO,NULL | 0 / 0 | - |
| 60 | 12+INF+ZER | 12 | 8 | INFOS | - | H12,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 61 | 12+INF+NUL | 12 | 8 | INFOS | - | H12,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 62 | 12+ZER+NUL | 4 | 4 | - | - | H12,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 63 | INF+ZER+NUL | 12 | 8 | INFOS | - | INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 64 | IT+SET+FR+12 | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12 (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12 | 8 / 20 | 24/36 |
| 65 | IT+SET+FR+INF | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO | 16 / 40 | 48/108 |
| 66 | IT+SET+FR+ZER | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: ZERO | 8 / 20 | 24/36 |
| 67 | IT+SET+FR+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: NULL | 8 / 20 | 24/36 |
| 68 | IT+SET+12+INF | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO | 0 / 0 | 0/36 |
| 69 | IT+SET+12+ZER | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,ZERO | 0 / 0 | 0/12 |
| 70 | IT+SET+12+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,NULL | 0 / 0 | 0/12 |
| 71 | IT+SET+INF+ZER | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,ZERO | 0 / 0 | 0/36 |
| 72 | IT+SET+INF+NUL | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,NULL | 0 / 0 | 0/36 |
| 73 | IT+SET+ZER+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,ZERO,NULL | 0 / 0 | 0/12 |
| 74 | IT+FR+12+INF | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO | 0 / 16 | - |
| 75 | IT+FR+12+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,ZERO | 0 / 8 | - |
| 76 | IT+FR+12+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,NULL | 0 / 8 | - |
| 77 | IT+FR+INF+ZER | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,ZERO | 0 / 16 | - |
| 78 | IT+FR+INF+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,NULL | 0 / 16 | - |
| 79 | IT+FR+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: ZERO,NULL | 0 / 8 | - |
| 80 | IT+12+INF+ZER | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 81 | IT+12+INF+NUL | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 82 | IT+12+ZER+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 83 | IT+INF+ZER+NUL | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 84 | SET+FR+12+INF | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO | 8 / 0 | 24/36 |
| 85 | SET+FR+12+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,ZERO | 4 / 0 | 12/12 |
| 86 | SET+FR+12+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,NULL | 4 / 0 | 12/12 |
| 87 | SET+FR+INF+ZER | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,ZERO | 8 / 0 | 24/36 |
| 88 | SET+FR+INF+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,NULL | 8 / 0 | 24/36 |
| 89 | SET+FR+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: ZERO,NULL | 4 / 0 | 12/12 |
| 90 | SET+12+INF+ZER | 36 | 24 | INFOS | - | W2,H12,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,ZERO | 0 / 0 | 0/12 |
| 91 | SET+12+INF+NUL | 36 | 24 | INFOS | - | W2,H12,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,NULL | 0 / 0 | 0/12 |
| 92 | SET+12+ZER+NUL | 12 | 12 | - | - | W2,H12,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,ZERO,NULL | 0 / 0 | 0/4 |
| 93 | SET+INF+ZER+NUL | 36 | 24 | INFOS | - | W2,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,ZERO,NULL | 0 / 0 | 0/12 |
| 94 | FR+12+INF+ZER | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 95 | FR+12+INF+NUL | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 96 | FR+12+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 97 | FR+INF+ZER+NUL | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 98 | 12+INF+ZER+NUL | 12 | 8 | INFOS | - | H12,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 99 | IT+SET+FR+12+INF | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO | 16 / 40 | 48/108 |
| 100 | IT+SET+FR+12+ZER | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,ZERO | 8 / 20 | 24/36 |
| 101 | IT+SET+FR+12+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,NULL | 8 / 20 | 24/36 |
| 102 | IT+SET+FR+INF+ZER | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,ZERO | 16 / 40 | 48/108 |
| 103 | IT+SET+FR+INF+NUL | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,NULL | 16 / 40 | 48/108 |
| 104 | IT+SET+FR+ZER+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: ZERO,NULL | 8 / 20 | 24/36 |
| 105 | IT+SET+12+INF+ZER | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,ZERO | 0 / 0 | 0/36 |
| 106 | IT+SET+12+INF+NUL | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,NULL | 0 / 0 | 0/36 |
| 107 | IT+SET+12+ZER+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,ZERO,NULL | 0 / 0 | 0/12 |
| 108 | IT+SET+INF+ZER+NUL | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,ZERO,NULL | 0 / 0 | 0/36 |
| 109 | IT+FR+12+INF+ZER | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,ZERO | 0 / 16 | - |
| 110 | IT+FR+12+INF+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,NULL | 0 / 16 | - |
| 111 | IT+FR+12+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,ZERO,NULL | 0 / 8 | - |
| 112 | IT+FR+INF+ZER+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,ZERO,NULL | 0 / 16 | - |
| 113 | IT+12+INF+ZER+NUL | 36 | 24 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 114 | SET+FR+12+INF+ZER | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,ZERO | 8 / 0 | 24/36 |
| 115 | SET+FR+12+INF+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,NULL | 8 / 0 | 24/36 |
| 116 | SET+FR+12+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,ZERO,NULL | 4 / 0 | 12/12 |
| 117 | SET+FR+INF+ZER+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,ZERO,NULL | 8 / 0 | 24/36 |
| 118 | SET+12+INF+ZER+NUL | 36 | 24 | INFOS | - | W2,H12,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,ZERO,NULL | 0 / 0 | 0/12 |
| 119 | FR+12+INF+ZER+NUL | 36 | 24 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 120 | IT+SET+FR+12+INF+ZER | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,ZERO | 16 / 40 | 48/108 |
| 121 | IT+SET+FR+12+INF+NUL | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,NULL | 16 / 40 | 48/108 |
| 122 | IT+SET+FR+12+ZER+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,ZERO,NULL | 8 / 20 | 24/36 |
| 123 | IT+SET+FR+INF+ZER+NUL | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,ZERO,NULL | 16 / 40 | 48/108 |
| 124 | IT+SET+12+INF+ZER+NUL | 108 | 64 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,ZERO,NULL | 0 / 0 | 0/36 |
| 125 | IT+FR+12+INF+ZER+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,ZERO,NULL | 0 / 16 | - |
| 126 | SET+FR+12+INF+ZER+NUL | 108 | 72 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,ZERO,NULL | 8 / 0 | 24/36 |
| 127 | IT+SET+FR+12+INF+ZER+NUL | 324 | 192 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,ZERO,NULL | 16 / 40 | 48/108 |
| 128 | (readings only) | 3 | 3 | - | - | RI | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: RI | 0 / 0 | - |

## 7. Not tested by instrument, with the reason (no silent caps)

Every variant is screened. At 1 ly, N = 7, the **288 JOINT variants** are covered by T-A, T-B, T-E and T-K. The other
7,903 are not tested by instrument. That 7,903 + 288 = 8,191 is a partition identity, STRUCTURAL (*wave 4:* 5,951 +
192 = 6,143):

| reason (1 ly, N = 7) | variants |
|---|---|
| INCONSISTENT: clash (c) or (d); nothing to test | 2,432 |
| SINGLE CONTRIBUTOR: one member's result covers the variant's; graded in that member's report | 3,840 |
| NO MEMBER CONTRIBUTION: anything removed is the geometry's, the board's or a premise's | 959 |
| INDEPENDENT: two or more single-member results, none joint; each graded in its member's report | 672 |

At 1 AU, N = 7 (2,048 W2 variants): 288 JOINT (T-A, T-B, T-E, T-K; T-G for the H12 classes), 896 inconsistent, 528
single contributor, 240 no member contribution, 96 independent. *Wave 4 first said* 1,536 W2 variants: 192, 768, 352,
160, 64 (*wave 3 first said* 96 JOINT and 448 single
contributor: the 96 {W2, F1}-type variants without H12 are now JOINT through support 2). The variant-by-variant list comes from `python3 combine.py --json PATH`.

## 8. Named hypotheses

**Conditional named premises** (assumed only inside a support; every support listed):

- **N_EPS** — support 1 of W2 × F1: removal premise ε > ε_any(L, N) for nlcontrol's Hamiltonian, carrying R_W2's
  H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB and H-BLOCK; tied to the cell by B-EPSWIN under the window set W_W2 (E-WIN).
  Wave 4: where the window computed from the unread value is empty, N_EPS stays possible through the OPEN pathway
  N_WREAD.
- **N_W2ANC** (wave 4) — support 2 of W2 × F1, R_W2′: H-COHERE, H-BORN-AT-BOB, H-EXTEND (derived, not computed) and
  H-FIELD-W2 (max‖H‖T ≈ 1.43-1.56 within the drift time). Zero-error; no H-BLOCK, no H-NLCONTROL-FORM. Window
  **unevaluated**: no READ bound maps onto its field (H-MAP not established), so the screen never makes it
  inadmissible — **assuming it cannot fail (STRUCTURAL in the named census)**, as for N_H12W. Not evidence a drift
  exists.
- **N_DCTC** — a CTC at Bob, H-DCTC, H-DCTC-CONVENTION C2, H-DCTC-SELECT. A CTC is not shown to exist. Its four-axis
  figure, 1 pair per teleported qubit, is that construction's; the route is ≤ 1 with its minimum OPEN (BHW 0811.1209v2
  p.4: unbounded if CTC qubits are free).
- **N_SIGKEY** (H-SIG-COR); **N_CORR** (H-CORRIDOR-MODEL, a Lorentzian quotient); **N_KEYING** (H-KEYING, the
  docket's); **N_FRW** (H-FRW-EXACT + H-NOT-DE-SITTER; also excludes CTCs); **N_2BVIA** (H-2B-VIA-CORRIDOR).
- **N_QTOPO** — ITB's corridor is not a classical Lorentzian object. **No READ source.**
- **N_MS17** — MS p.17, READ; a non-traversable bridge only.
- **N_MEASPHYS** (H-MEASURE-PHYSICAL) — no source. **N_H12W** (H-12-CARRIER + H-12-W) — no READ model.
- *Withdrawn:* **N_FRAME3b** (presupposes F1); H-SLICE-INTRINSIC named, not credited.

**Wave 5 (M's rulings; named, each carried as a hypothesis, none seated):**

- **H-INFO-SHAPE** (literal `SHAPE`), M's ruling, verbatim: *"Teleportation carries no physical substance, but does
  carry information (non physical properties/bounds that give shape to the geometry at the seat)"*; the substance
  comes *"from the seat"*. Commitment C-SHAPE: SHAPE ⇒ RECV.
- **H-SHAPE-ENCODING** (measure.py's, carried here): H-INFO-SHAPE is encoded as "a holder / the substance is at the
  seat". An encoding is a choice, and it is named so the verdict says what it rests on.
- **H-INFO-S** (literal `INFOS`): kept as the **alternative reading**. Its clash with B-RECV stands and is history
  (M ruled 2026-10-03).
- **H-SEAT-GLOBAL**: the relocation O-MATTER → O-SEAT is applied in every variant, because M's ruling concerns the
  obstruction itself. It is not credited to the SHAPE literal.
- **H-C3**: renormalisable couplings carry no net B or L (`massform.HIGGS_COUPLING_CARRIES_B_OR_L` False). S10's
  refusal as a supply and S13's "forms no baryons" both rest on it. LEDGER: a higher-dimension operator carrying B or L
  would reverse it. S10's other conditions are C1/P-UNIFORM, C4 (D29's bridge), C5 and H-UNSOURCED-SEAT.
- **H-SEAT-S12** (ALTERNATIVE, adopted nowhere): the pair route S12 read as a supply at the seat, through the OPEN
  pathway N_S12 used only in that alternative. M-apply places S12 beside O-SEAT and does not credit it; its energy
  would itself have to be at the seat (D23).
- **E-SEAT** (encoding choice): O-SEAT's removal is tested only against S10 and S13, the two routes M-apply grades it
  against. S5 (reconstruction from stock) needs the stock already at the seat (D23), so it is not a supply.

**OPEN pathways** (never assumed in a removal; wave 4: held **false** whenever premise sets, supports and accounts are
computed, and set one at a time only by the OPEN test): **N_WREAD** (wave 4: a READ of the Weinberg-family values could
open support 1's window where the unread value closes it); **N_XI** (ξ > 0); **N_QEIC** (new: outside {H_flat, H-PATH,
H-MIN-SCALAR}; curved-space QEIs NAMED-NOT-READ); **N_EPSG** (KR pp.13-14); **N_VAC** (Reznik READ; the window
0.91 L/c < T < L/c DERIVED-FROM-READ); **N_EQUIL** (EGJ out of equilibrium, ITJ's); **N_ILFREE** (no source).

**Encoding choices, named:** W2 is C2; without a preferred slicing C2 defines no channel. The window premises are held
fixed (**E-WIN**), except that their NAMED-NOT-READ values enter as the OPEN pathway N_WREAD (wave 4); refusing
H-TRANSFER without H-12 is still not screened. Support 2's window is unevaluated and not screened at all (**E-WIN2**,
wave 4): `support2_field_rows` reports what it would need (‖H‖ ≥ max‖H‖T · c/L) beside the unread bound only as if
H-MAP-W2 held, which is adopted nowhere. O-MAKE and O-LOOP are each split in two. A CTC releases only Geroch's compact case (O-MAKE-TOPO stays
bound). Under ITE, MS fn.1 commits the bridge non-traversable; under ITJ the throat is geometric. R-INDEX releases
nothing without H-IT. A corridor network is present in every variant. Absences are part of the variant (closed world).
**Carried through unchanged:** A1's §2 list (incl. H-BLOCK, H-QUBIT-DRIFT, H-EXTEND); A2's H-CMB-IS-COSMIC and
H-KILLING-SEARCH; A3's H-ALT, H-FAITHFUL and H-R; A4's H-QUDIT, H-ER=EPR, H-PATH, H_flat and H-MIN-SCALAR. Wave 4: A1's H-FIELD-W2
(in N_W2ANC) and H-KR-TS (beside C-KR: KR's foliation dependence, 2511.15935v1 p.4, not shown to be a signal).
**Wave 5:** the support-1 window flag "ADMISSIBLE GIVEN W_W2" (a flag, not a premise; `settle.window_given`), and
**H-MAP-W2** (support 2's field read against the unread precession bound), still adopted nowhere and now reported per
member.

## 9. Sources

| source | status | used for |
|---|---|---|
| Maldacena & Susskind, arXiv:1306.0533v2 | READ (wave 1) | fn.1 p.2; §3.1 p.16; §3.2 pp.16-17; p.17 (N_MS17); §5.4 pp.36-37 |
| Reznik, arXiv:quant-ph/0212044v2 | READ (wave 1) | p.1; p.10; p.12 Fig. 2; N_VAC |
| Eling-Guedens-Jacobson, gr-qc/0602001v1; Jacobson gr-qc/9504004v2 | READ by A4 | N_EQUIL, ITJ |
| Brun-Harrington-Wilde, arXiv:0811.1209v2 | READ by A2 (pp.1-4 re-READ in wave 3) | N_DCTC, via `frame.four_basis_c2_table` and `bb84_c2_table` |
| Hsu, arXiv:2511.15935v1 | READ by A1 (wave 3; p.4 in wave 4) | N_FRAME3b withdrawn: H-FRAME3b presupposes F1; H-KR-TS beside C-KR |
| Melnychuk et al., arXiv:2411.09611v1 | **READ this pass** (alphaXiv, pp.1-8) | searched for a restatement of the 1989-90 Weinberg-family values: none. Its bound, \|ε\| ≲ 1.15e-12 (90% CL, p.1, p.7), is on the Kaplan-Rajendran causal electromagnetic nonlinearity (dimensionless; "(A^μ + ε⟨Ψ\|A^μ\|Ψ⟩)J^μ", p.1), not on a Weinberg-form precession rate in s⁻¹, so no H-MAP carries it onto ε_max: N_WREAD stays OPEN |
| `LEDGER.md` lines 50, 67, 70, 181 | READ (wave 4), never written | B-RECV's conditions beside clash (d) |
| `LEDGER.md` rows S10, S12, S13 | **READ this pass** (`measure.ledger_row`, `board_flags`), never written | B-S10 (REFUSED), B-S13 ("It forms no baryons (C3: the elements were already there)"), the H-SEAT-S12 alternative (OPEN, priced) |
| `M-RULINGS-2026-10-03.md` / CHARTER.md (M's rulings, verbatim) | READ this pass | H-INFO-SHAPE, O-SEAT |
| `../massform.py` (DOCKET 65), via `measure.seat_supply` | imported, never copied | MECHANISM_VERDICT, HELD_SEAT_ROUTE, HIGGS_COUPLING_CARRIES_B_OR_L, the S13 price figures |
| the four A-reports and their instruments (wave 3) | imported and re-run | every ground; each READ citation is the owning A-report's |
| `transit.py`, `emtension.py` | read, never written | B-RECV, B-LOCC, C-ITE |

Wave 5: no arXiv source was read this stage, and no host refused a request. The new figures are imported or READ from
the board (LEDGER rows, M-RULINGS). Wave 4: one source READ (2411.09611v1, above); every other figure is computed by an imported instrument or READ by its
owning A-report. No host refused a request (no 403). *Wave 3 first said* "No arXiv source was re-read in this stage".

## 10. Findings (recorded, not repaired)

1. **At most one obstruction is removed by the hypotheses themselves, in any consistent variant and account, and it is
   O-BITS** — by W2 × F1 (JOINT) with two supports: R_W2 (N_EPS; at 1 ly, N = 7 and 1 AU, N = 10⁶ **admissible given
   W_W2, flagged, not settled** (wave 5); at 1 AU, N ≤ 10³
   OPEN via N_WREAD without H12, REMOVED-IF with H12 + N_H12W) and R_W2′ (N_W2ANC; zero-error, window unevaluated, so
   in both cells); or by clause 2b's D-CTC (conditional on N_DCTC, at any distance, O-LOOP reintroduced). *Wave 3 first
   said* one support, and "at 1 AU, N ≤ 10³ only with H12 + N_H12W". *Wave 2 first said* "the most is three"; *wave 1*
   "four of the six-way split, with O-HOLD REMOVED".
2. **H-SETTLE alone removes nothing**: the drift needs H-FRAME's slicing. *Wave 2 first said* {W2} alone O-BITS
   REMOVED-IF {W2; N_EPS, N_FRAME3b}.
3. **O-HOLD, O-MAKE-TOPO and the corridor form of O-LOOP are at most NOT-BOUND-IF**, under ITB + N_QTOPO (no READ
   source); what the non-geometric corridor costs is OPEN (N_ILFREE).
4. **O-LOOP's corridor removal is the geometry's** (exact FRW, N_CORR) and holds only in accounts without N_QTOPO; the
   two corridor accounts clash. Signal loops are removed by N_SIGKEY; the D-CTC reintroduces a loop.
5. **O-SEAT ("supply at the seat", which replaces O-MATTER by M's ruling) survives every consistent variant**: S10 is
   REFUSED as a supply and S13 forms no baryons, both resting on H-C3, so ≥ 0.998 of the payload must already be at
   the seat. **Clash (d) is ruled**: under H-INFO-SHAPE it is dissolved by relocation (SHAPE ∧ B-RECV SAT; SHAPE in
   no core), not removed by assertion. H-INFO-S, kept as the alternative, still clashes with B-RECV in all 2,048 of its
   variants. *Wave 4 first said* "O-MATTER survives every consistent variant ... M's to rule".
6. **O-MAKE-DIST survives every consistent variant** (OPEN via N_VAC only).
7. **H-ZERO, H-NULL, H-INFO's necessity reading and (wave 5) H-INFO-SHAPE are UNTESTED-BY-SCREEN** (they change
   nothing in 4,096, 4,096, 2,048 and 2,048 variants; *wave 4:* 3,072, 3,072, 2,048). *Wave 2 first said* ZERO and NULL were exercised through N_EQUIL.
8. **H-FRAME's two clauses do not contradict each other as M states them**; exact FRW excludes clause 2b's corridor
   route and its D-CTC (a global time function admits no CTC).
9. **ER=EPR with W2 is INCONSISTENT-AS-ENCODED**, and ER=EPR's linearity also excludes the D-CTC channel.
10. **The first transit can beat light with a midpoint source**, conditionally (N_EPS at the unread limit, H-C2, F1,
    H-BLOCK): 0.50153 yr after the source fires, against light's 1 yr. One-end distribution cannot.
11. **Interference exists**: clause 2b undoes the corridor loop removal; R-QUANTUM undoes ITB's non-binding; ITE undoes
    the D-CTC.
12. **One disagreement with the A-reports remains, explained**: A2's partial non-binding of O-MAKE (vocabulary, not a
    fault). *Wave 3 first said* two, the second A3's missing corridor NOT-BOUND-IF on O-LOOP — repaired by R3-alone.
13. **The pairs-per-qubit figures "1, zero-error" are constructions', not classes'** (wave 4): the W2 class without
    H-QUBIT-DRIFT reaches 2/(log₂d − 1) — 1, 2/3, 1/2 at d = 8, 16, 32 — with no positive floor in the computed range;
    the D-CTC route is ≤ 1 with its minimum OPEN (BHW p.4).
14. **Support 1's 1 AU, N ≤ 10³ exclusion rests on an unread value** (wave 4): OPEN via N_WREAD, not LEFT. **And its
    open windows rest on the same value** (wave 5, V3 problem 3): at 1 ly, N = 7 and 1 AU, N = 10⁶ it is admissible
    given W_W2, flagged, not settled. Support 2 is distance-free in the screen only because no READ bound reaches its
    field. Under H-MAP-W2 (adopted nowhere) it would need 120–131× the unread ε_max at 1 AU under reading A, and
    240–261× under B, across the computed members (123× / 246× for the four-axis member). *Wave 4 first said* "120×",
    with the four-axis member's max‖H‖T beside k = 4's figures (V3 problem 1).
15. **Q-1s moves no grade here** (wave 4): every bit count the screen uses is over non-negative probabilities, where
    Re H = H by definition, and no board holding names the measure's form; H-INFO necessity is inert.

## 11. Testable predictions

- **{W2, F1}.** Bob's mean σ_y shifts by tanh(2ε(T − t_A)), t_A Alice's measurement time in the preferred slicing:
  0.537, 0.291 or 0 for t_A at the start, middle or end of his window (ε = 0.1, T = 3), under H-C2 and its no-branch
  rule. Frames that order the events differently disagree, so the slicing is measurable through the signal.
- **W2 on partly entangled pairs (T-B).** The shift follows the shared entanglement: 0.240 at S = 0.53 bits, 0.042 at
  S = 0.13 bits, exactly 0 for product pairs.
- **Clause 2b's D-CTC.** None physical: it needs a CTC at Bob, not shown to exist.
- **ITB.** None READ: ITB has no model that predicts anything beyond linear QM's no-signalling.
- **Any complete holder** of the 70 kg definition at R = 1 m has gravitating energy of at least 33-379 J,
  count-dependent: a floor on O-SEAT's holder, not a price (*wave 4 first said* "O-MATTER's holder").

## 12. Open

- **The Weinberg-family values** (Majumder+ 1990 and kin): NAMED-NOT-READ; pre-arXiv; 2509.04320v1, 2511.15935v1 and
  (this pass) 2411.09611v1 carry none. A READ would settle N_WREAD: support 1 at 1 AU, N ≤ 10³ stays OPEN until then.
- Support 2's window: unevaluated (no H-MAP for its field; H-FIELD-W2 unbounded by any READ source); H-EXTEND derived,
  not computed. The W2 class capacity without H-BORN-AT-BOB: OPEN (A1).
- The rest of E-WIN is not screened: refusing H-TRANSFER without H-12 would widen support 1's window (A1 §4b).
- The D-CTC route's minimum pairs per qubit: OPEN (k-axis table not computed, cost).
- Whether KR's foliation dependence (H-KR-TS, 2511.15935v1 p.4) is operational: OPEN.
- N_QTOPO, N_MEASPHYS, N_H12W, N_ILFREE: no READ source.
- **O-SEAT**: an obstruction until the seat's supply is shown. S13's finite nucleon response and its source's fate
  (H-RELEASE) are OPEN on the board; they bear on how much mass returns to templates already at the seat, not on
  baryon number (H-C3). Whether S12 counts as a supply at the seat (H-SEAT-S12) is not ruled.
- Whether any H-IT reading turns H-INFO-SHAPE's "shape" into geometry at the seat: not computed, and no READ source.
- Support 1 wherever its window is open (1 ly, N = 7; 1 AU, N = 10⁶): **admissible given W_W2, not settled**.
  Bollinger 1989 and Chupp-Hoare 1990 have never been checked.
- *Closed in wave 5* (kept as history): "Clash (d): M's to rule". M ruled on 2026-10-03 for H-INFO-SHAPE, under
  which the clash is dissolved by relocation. INFOS is kept as the alternative, and its clash stands.
- *Closed in wave 4* (kept as history): "A3's R-INDEX grade lacks the corridor NOT-BOUND-IF on O-LOOP" and "A1's
  H-SETTLE-KR × H-12 row ... H12 not load-bearing there" — both repaired by R3-alone and checked here (drift 167/168;
  load-bearing guard 13/13).
