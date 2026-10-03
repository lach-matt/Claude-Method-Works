# DOCKET 68 · B-combine: the seven hypotheses in combination

**Status: a docket work item. Nothing here is seated.** The instrument is `combine.py`, which sits beside this file.
`python3 combine.py --selftest` runs **80 checks and passes all 80** in about 60 s. The checks include the two
PROOF-ASSISTANT.md guards, five named controls, two more controls inside the new computations, and a re-run of every
computed ground.

`combine.py` imports what it uses and copies nothing:

- from the four work items: `settle.py`, `frame.py`, `measure.py` and `geometry.py`;
- from before the docket: `nlcontrol.py`, `corridors.py`, `nosig.py` and the rest, through those instruments;
- from the board: `../transit.py` and `../emtension.py`, and `../LEDGER.md`, which is read and never written.

It writes nothing outside `docket68/`.

M's standing instruction, verbatim from the charter: *"Remember that some of the hypothesies lined up for docket 68
may turn out, after initial testing, to work better in combination."* M's hypotheses are carried as hypotheses. Each
grade says what a combination does, not whether it is true.

## 1. What was built: every combination, in every reading

**The combinations.** Seven hypotheses give **127 non-empty combinations**.

**The readings.** Three of the hypotheses were found by the work items to have more than one reading, and every
reading is screened:

- **H-SETTLE**
  - **W2**: deterministic drift acting per branch. This is M's definition, of Weinberg/Gisin type, and it is A2's
    convention C2.
  - **W1**: the same drift acting on the reduced state (A2's C1).
  - **KR**: the causal Kaplan-Rajendran form.
- **H-FRAME**
  - **F1**: clause 1. A preferred frame exists and corridors are keyed to it.
  - **F2b**: clause 2b. Messages reach the past of the cosmic clock.
  - **F1+F2b**: both clauses in their strong form, as M's sentence states them. This is screened, not assumed away.
- **H-IT**
  - **ITB**: the corridor lives in the information layer (the charter's reading).
  - **ITE**: ER=EPR with Maldacena-Susskind's own stated assumptions.

**The reading slots.** Each variant is run with each of four reading slots: none, R-INDEX, R-QUANTUM, or both. The
readings apply to M's reply on holding the corridor open, and every combination has to hold one.

**The count.** (4·4·3·2⁴ − 1)·4 = **3,068 variants**, plus the 3 variants with readings only, gives **3,071
screened**. None was skipped.

**Two splits the work items forced.**

- **O-MAKE** is carried in the two forms A4 found:
  - **O-MAKE-TOPO**: the Geroch/Tipler topology change that the work order names;
  - **O-MAKE-DIST**: making the entanglement the corridor runs on, which means distributing it at ≤ c.

  O-MAKE counts as removed only when both forms are.
- **A verdict per obstruction** takes one of five values:

| verdict | meaning |
|---|---|
| **REMOVED** | z3 shows that the variant's commitments force the removal |
| **REMOVED-IF** | the removal is forced once the named hypotheses in the unsat core are assumed. Each is listed, and its premises are checked to be satisfiable. |
| **OPEN** | the removal is possible only through a pathway the sources leave undecided |
| **LEFT** | the obstruction stands in every model |
| **SILENT** | nothing in the variant decides it |

## 2. The screen (z3), and what it is

**How the encoding is built.**

- Every board holding is a tracked constraint, and so is every hypothesis commitment. `_board`, `_defs` and
  `_commitments` in `combine.py` hold them.
- Each constraint carries its ground: the instrument and the number it computed, or the arXiv id and page that was
  READ.
- An inconsistent variant is named by its unsat core.

**What z3 adds and does not add.** This is bookkeeping over findings that other instruments own; it is not new
physics. z3 adds three things:

1. which sets of commitments contradict one another;
2. which members and which named hypotheses a removal actually rests on;
3. exhaustive coverage.

The new physics in this work item is in section 5.

**Guards (they run before any result is reported; the screen refuses if either fails).**

- **Vacuity.**
  - The board alone is satisfiable.
  - Each of the 13 single readings is satisfiable.
  - The named hypotheses are jointly satisfiable with the board, with and without the OPEN pathways.
  - Every REMOVED-IF rests on premises that are themselves satisfiable.
  - Every consistent variant stays satisfiable once all the named hypotheses are assumed, so no conditional removal
    is vacuous.
  - **Three known contradictions are caught:** F1 with F2b; a planted signal in linear QM; ITE with W2.
- **Non-triviality.**
  - The board alone admits both a loop and no loop.
  - **CONTROL:** with the holding B-RECV deleted, O-MATTER becomes removable. This shows that O-MATTER's survival
    comes from that holding, not from the encoding.
- **Encoding drift.**
  - 17 hand-checked variants agree with z3.
  - Each is tied to the grade text of the A-report that owns it, parsed from that report's JSON: 17 of 17 match.
    (A2's JSON on disk carries a summary rather than a grades list; A2's text is read from `frame.GRADES` and from
    that summary.)
  - The two OPEN branches show up as OPEN: R-QUANTUM through ξ > 0, and KR through ε_G.
  - **CONTROL:** a deliberately mutated encoding, in which clause 1 no longer keys corridors, is **caught**
    disagreeing.
- **Grounds re-run from their instruments.**
  - W2 signals: tanh(0.6) = 0.53705.
  - C1 does not signal: 2.2e-16.
  - C2 carries 0.0817 bits and depends on the frame: 1/2 against 2/3 or 1/3.
  - Antitelephone: −3/5 when keyed to the sender's frame, 0 when keyed to the cosmic frame.
  - Cosmic keying: 0 of 100 lattices fail at rank 2, and 0 of 100 at rank 3.
  - N < 7 is impossible.
  - Local unitaries change the entanglement entropy by 8.9e-16.
  - The QEI covers 2.08e-68 of the deficit.
  - The zero-shift NEC claim is `unsat`.
  - The board flags hold: transit `BEATS_LIGHT`, `TRAVERSAL_IS_REMOVED` and `CARRIES_SUBSTANCE` are False, and
    `emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE` is False.
  - LEDGER: S5 OPEN, S10 REFUSED, S13 OPEN.

### Contradictory combinations: three clashes, named

Of the 3,071 variants, **1,919 are consistent and 1,152 are not.** Every inconsistent variant falls into one of three
clashes. **Every one of the 127 combinations has at least one consistent variant**, so no combination is
contradictory in all of its readings.

| clash (unsat core) | variants | what collides | ground |
|---|---|---|---|
| **(a)** F1 + F2b + B-2B | 640 | H-FRAME's clause 1, every corridor keyed (ξ_t = 0), against clause 2b, a message into the cosmic past | `frame.py` part (i).3, computed: a message into the cosmic past ⇔ ξ_t ≠ 0 ⇔ not keyed. M's sentence, taken with both clauses strong, contradicts itself. Each clause alone is consistent. |
| **(b)** ITB + R-INDEX + R-QUANTUM + B-THROAT | 256 | Under H-IT, R-INDEX removes the geometric throat (A3's conditional). R-QUANTUM holds a geometric throat with negative energy. | A3 (the measure has no energy term; the removal is physical only under H-IT); A4 (R-QUANTUM). The two readings M said to "consider both" cannot both be physical for the same corridor under H-IT. Each is consistent alone, and with ITE. |
| **(c)** ITE + W2 | 256 | ER=EPR as Maldacena-Susskind state it, against a per-branch drift that signals through entanglement | **READ here**, arXiv:1306.0533v2: fn.1 p.2, "We will assume that wormholes remain un-traversable"; §3.1 p.16, no local operation on one member "can influence the other"; §5.4 pp.36-37, a geometric feature is a linear operator. Computed in section 5 (T-B): in Van Raamsdonk's eq.(1) state, which is the ER=EPR model A4 used, the drift makes Bob's ⟨σ_y⟩ depend on Alice's choice (0.537 at β = 0). **This clash is with H-ER=EPR's own assumptions, not with H-IT:** ITB + W2 is consistent. |

## 3. The answer

**No consistent variant removes all five obstructions.**

The most any consistent variant removes is four entries of the six-way split. The variant is
**{H-SETTLE W2, H-FRAME F1, H-IT ITB, R-INDEX}**, and it may carry any of H-12, H-INFO and H-ZERO, H-NULL, or none of
them. Its verdicts:

| obstruction | verdict | rests on (z3 unsat core) |
|---|---|---|
| O-BITS | **REMOVED-IF** | W2 and the named hypothesis N_EPS: ε ≥ ε_min(L, N) with N ≥ 7, not excluded by the Weinberg-family limit (NAMED-NOT-READ), together with A1's H-MAP, H-TRANSFER, H-SPIN and H-COHERE |
| O-MAKE-TOPO | **REMOVED-IF** | ITB and N_QTOPO: the corridor is not a classical Lorentzian topology change |
| O-HOLD | **REMOVED** | ITB **and** R-INDEX **together**, with no named hypothesis beyond A3's conditional reading |
| O-LOOP | **REMOVED-IF** | F1, with N_CORR (H-CORRIDOR-MODEL) and N_SIGKEY (the signal keyed to the preferred slicing, A1's H-SIG-COR) |
| **O-MAKE-DIST** | **OPEN**, through N_VAC only | not removed in any consistent variant |
| **O-MATTER** | **LEFT** | not removed in any consistent variant |

In the five-way terms of the work order this variant removes **O-BITS, O-HOLD and O-LOOP**. It removes O-MAKE in its
topology-change form only. **O-MATTER and the distribution form of O-MAKE survive every one of the 1,919 consistent
variants.**

**Why O-MATTER survives every consistent combination.**

- None of the seven hypotheses commits to anything about what is at the destination.
- The holding it meets is B-RECV:
  - `transit.CARRIES_SUBSTANCE` is False, so a receiver must be there.
  - Bekenstein (quant-ph/0404042v1 pp.2 and 8, READ by A3): a complete system with E > 0 holds the bits.
  - LEDGER.md: S10 is REFUSED as a supply. S13 and S5 are OPEN, and both need a prior arrival at ≤ c (D23).
- **The control shows the survival is that holding's doing.** Delete B-RECV and z3 can remove O-MATTER.
- H-INFO's clause (b), "matter cannot exist without it", makes information **necessary** for matter. It does not
  make it **sufficient**, and its status is OPEN (A3). A hypothesis that information suffices to form matter at the
  destination would be needed, and it is not among M's seven.
- The cost is small in energy: the holder's Bekenstein floor is 33-379 J (T-D). The obstruction is the prior
  arrival, not the energy.

**Why O-MAKE-DIST survives every consistent combination.**

- Every channel among the hypotheses runs on shared entanglement, and the work items and this item computed it:
  - the drift's signal falls with the pairs' entanglement, from 0.537 at S = 1 bit to 0 at S = 0 (T-B);
  - on product states it is exactly 0 (T-C, 2.9e-15, against 0.537 for the Bell control).
- LOCC cannot create entanglement. Maldacena-Susskind §3.2 pp.16-17 (READ here): "no bridge without preexisting
  bridges". Computed: local unitaries change the entropy by 8.9e-16, and the nonlocal control changes it by 1.965.
- So the pairs are distributed first, at ≤ c. That is `transit.TRAVERSAL_IS_REMOVED = False`, unchanged by any
  combination.
- **The one pathway that opens it is N_VAC**: pre-existing vacuum entanglement used as the pairs, which is the
  closest reading of M's *"because it already exists everywhere"*. It is **READ, Reznik quant-ph/0212044v2**:
  - Causally disconnected probes can end up entangled (p.1). So M's intuition has a real counterpart.
  - The entanglement "vanishes once the regions become sufficiently separated" (p.1).
  - For inertial probes it persists only while L/T < 1.1 (p.12, Fig. 2). The probes, which must already be at both
    ends, interact for T > 0.91 L/c.
  - Whether any setup supplies ≥ 7 pairs per qubit faster than distribution is **not computed**, so the pathway is
    **OPEN**.

**Synergy and interference.**

- **Synergy (the measured payoff of M's instruction):** O-HOLD is removed by **ITB and R-INDEX jointly**, and by
  neither alone. R-INDEX alone removes it only within the measure (A3); H-IT alone leaves it (A4). This shows in
  192 consistent variants: 96 with ITB and R-INDEX alone, 48 with F1 added, 32 with W2 added, and 16 with both.
- **Interference:** none. No member's removal is undone by another member in any consistent variant.

## 4. Complementary combinations, and the instrument tests

A consistent variant is **complementary** when more than one member contributes a removal. That means one member
removes an obstruction that another leaves. **640 variants** qualify, in **9 classes**:

| removed | contributors | variants | tested by |
|---|---|---|---|
| O-HOLD, O-MAKE-TOPO | ITB, RI | 96 | T-D |
| O-BITS, O-MAKE-TOPO | W2, ITB | 64 | T-B, T-C |
| O-BITS, O-HOLD, O-MAKE-TOPO | W2, ITB, RI | 32 | T-B, T-C, T-D |
| O-LOOP, O-MAKE-TOPO | F1, ITB | 96 | T-A |
| O-HOLD, O-LOOP, O-MAKE-TOPO | F1, ITB, RI | 48 | T-A, T-D |
| O-LOOP, O-MAKE-TOPO | F1, ITE | 192 | T-A |
| O-BITS, O-LOOP | W2, F1 | 64 | T-A, T-C |
| O-BITS, O-LOOP, O-MAKE-TOPO | W2, F1, ITB | 32 | T-A, T-B, T-C |
| O-BITS, O-HOLD, O-LOOP, O-MAKE-TOPO | W2, F1, ITB, RI | 16 | all of T-A through T-E |

**T-A: W2 × F1. The channel survives being keyed to the cosmic slice, and no loop forms.** All values come from
imported instruments:

- C2 carries 0.0817 bits per use (`frame.signalling_table`).
- The outcome depends on the ordering: Bob-first gives 1/2, Alice-first gives 2/3 or 1/3. So the cosmic ordering is
  what defines the channel.
- The reply arrives at −3/5 when keyed to the sender's frame, and at **0** when keyed to the cosmic frame
  (`frame.antitelephone`).
- Cosmic-keyed lattices: 0 failures at rank 2 and 0 at rank 3.
- Bob's shift is tanh(0.6) = 0.53705 (`settle`).
- H-IT's own model adds no signal that would need keying: 1.55e-15 (`geometry.it_no_signal`). This covers the
  F1 × IT classes.
- **PASS.**

**T-B: W2 inside H-IT's own READ model. A new computation, `tfd_drift`.**

- **The setup.** Two copies in Van Raamsdonk's eq.(1) state at d = 2 (`geometry.tfd`). Alice measures z or x. Each of
  Bob's branch states drifts under nlcontrol's H = ε⟨X⟩Z, with ε = 0.1 and T = 3, under C2.
- **Two independent routes.** The integrator (`nlcontrol.evolve`) and the exact closed form (`settle.bloch_exact`)
  agree to 1.2e-5.

| β | entanglement S (bits) | C2 signal ⟨Y⟩ₓ − ⟨Y⟩_z (exact) | linear control | C1 control |
|---|---|---|---|---|
| 0 | 1.000 | 0.53705 (= tanh 0.6) | 0 | 0 |
| 0.5 | 0.956 | 0.50796 | 0 | 0 |
| 1 | 0.840 | 0.43186 | 0 | 0 |
| 2 | 0.527 | 0.24001 | 0 | 0 |
| 4 | 0.130 | 0.04204 | 0 | 0 |
| 8 | 0.0044 | 0.00080 | 0 | 0 |
| 30 | 0.000 | 0.00000 | 0 | 0 |

- **What it shows.**
  - The channel's strength falls monotonically with the shared entanglement, which is the corridor's "bridge" in Van
    Raamsdonk's reading. The channel runs on the bridge. It does not replace the bridge.
  - Under ITB nothing forbids this signal, so ITB + W2 is consistent.
  - Under ITE it contradicts MS §3.1 and fn.1, which is clash (c), computed.
- **PASS.**

**T-C: the drift cannot make its own pairs. A new computation, `product_drift`.**

- On random **product** states, Bob's drifted ensembles coincide whatever Alice measures: largest difference
  2.9e-15.
- The Bell control gives 0.53706.
- `geometry.locc_entropy_change`: 8.9e-16 for local unitaries, 1.965 bits for the nonlocal control.
- **O-MAKE-DIST is untouched by H-SETTLE.** **PASS.**

**T-D: ITB × R-INDEX. O-HOLD is removed, and the holding reappears as a holder at the destination.**

- The NEC throat is gone. Under R-INDEX the price of holding becomes a holder with gravitating energy above the
  Bekenstein floor: **33-379 J** at R = 1 m for measure.py's four counts of a 70 kg body.
- The board's 1 m throat is 4.8155e42 J, so it exceeds the largest floor by a factor of **1.27e40**.
- The removal moves the cost into O-MATTER. It does not erase it. **PASS.**

**T-E: the most-removing variant, end to end. A new computation, `first_transit`, plus a z3 check over the reals.**

- **Is N_EPS consistent with the Weinberg-family limit?** That limit is NAMED-NOT-READ (Majumder, via settle.py).
  z3 checks ε_min(L, N) ≤ ε ≤ ε_max under both H-MAP readings:

  | distance | pairs per qubit, N | consistent? |
  |---|---|---|
  | 1 ly | 7 | consistent: ε_min = 7.29e-8 s⁻¹, against ε_max = 2.39e-5 (reading A) or 1.19e-5 (reading B) |
  | 4.24 ly | 7 | consistent: ε_min = 1.72e-8 s⁻¹ |
  | 1 AU | 7 | **inconsistent**: ε_min = 4.61e-3 s⁻¹ |
  | 1 AU | 1,000 | **inconsistent** |
  | 1 AU | 10⁶ | consistent: ε_min = 6.67e-6 s⁻¹ |

  The guard on this check: ε > 0 alone is satisfiable. This reproduces A1's table.
- **What one transit costs.** For a single teleported qubit, the channel needs at least 2/CMAX = **6.21** pre-shared
  pairs. Using N = 7 pairs per qubit and one qubit per bit of the count (A3's H-FAITHFUL):

  | count | drift pairs | teleportation ebits |
  |---|---|---|
  | species sequence | **6.66e28** | 9.51e27 |
  | grid at 1 Å | 2.90e29 | 4.14e28 |
  | grid at 0.1 Å | 7.61e29 | 1.09e29 |
  | thermal entropy | 1.99e29 | 2.84e28 |

  Every one of those pairs is distributed at ≤ c beforehand.
- **Timing at 1 ly.**
  - With the pairs and the holder already in place, Bob reads after T = L/2c, which is **0.5 yr before light**. This
    advantage holds for *later* transits, conditional on N_EPS.
  - The **first** transit waits for the pairs: at the earliest L/c + T = **1.5 yr** after the pairs leave.
  - This is the amortisation shape LEDGER.md already records for S5. The combination makes repeated transits beat
    light (conditionally); the first one cannot.
- **PASS.**

**T-F: R-QUANTUM × H-SETTLE-KR, both OPEN on O-HOLD.**

- Nothing decides this pair. In the bound's scope the QEI covers 2.08e-68 of the 1 m deficit.
- The ξ > 0 branch (no state-independent QEI) and the ε_G branch (no bound) are both OPEN at source.
- Two OPENs make an OPEN, not a removal. **PASS** (recorded, not decided).

## 5. Each hypothesis across every combination (the retirement rule)

Charter rule 2: *"A failure alone does not retire a hypothesis. It is retired only if it also fails in every
combination tested."*

**Literals that are load-bearing** for some removal, as found by the unsat cores over the 1,919 consistent variants:

- **W2** (H-SETTLE): O-BITS.
- **F1** (H-FRAME): O-LOOP.
- **ITB and ITE** (H-IT): O-MAKE-TOPO.
- **ITB with R-INDEX**: O-HOLD.

The named hypotheses that are ever load-bearing: N_EPS, N_QTOPO, N_CORR and N_SIGKEY.

| hypothesis | across all combinations | rule 2 |
|---|---|---|
| H-SETTLE | Removes O-BITS in reading W2 under N_EPS. W1 and KR remove nothing in any combination. | **kept, PARTIAL**; leaves O-MAKE-DIST and O-MATTER in every combination |
| H-FRAME | Removes O-LOOP in reading F1. F2b removes nothing in any combination. F1+F2b is inconsistent (clash a). | **kept, PARTIAL** |
| H-IT | Removes O-MAKE-TOPO in both readings, and O-HOLD with R-INDEX (ITB only). ITE contradicts W2 (clash c). | **kept, PARTIAL** |
| H-12 | Load-bearing for no removal in any of the 1,919 consistent variants. Under W2 it names the carriers (Z0 is the only one with a state-dependent bound; G and v are unbounded: A1), but W2 removes O-BITS without it. | **meets the retirement criterion as a remover of the five obstructions.** It is not refuted, and its carrier map stands as the test list for W2. |
| H-INFO | Load-bearing for no removal. It reprices the "costs little" half (A3), but that is not a removal. Clause (b) is OPEN. | **meets the criterion as a remover.** It is not refuted; clause (a) is supported (A3). |
| H-ZERO | Load-bearing for no removal. Under H-IT it frees the zero of energy (A4, Jacobson), but the NEC is invariant (z3). | **meets the criterion as a remover.** It is not refuted. |
| H-NULL | Load-bearing for no removal. It prices O-HOLD in bits (A4). | **meets the criterion as a remover.** It is not refuted. |

"Meets the criterion" is a measured statement: in every combination screened, and in every instrument test, these
four remove none of the five obstructions. Their other results stand, and what each does is listed beside it. The
retirement itself is M's to apply.

## 6. Every combination (127, plus readings only)

Abbreviations:

- **Hypotheses:** IT = H-IT, SET = H-SETTLE, FR = H-FRAME, 12 = H-12, INF = H-INFO, ZER = H-ZERO, NUL = H-NULL.
- **Clashes:** a/b/c as in section 2.
- **Reason codes for variants not tested by instrument:**
  - **single**: one member's removal set covers the variant's, so it is graded in that member's report;
  - **no-removal**: no member removes an obstruction, so nothing is complementary (only N_VAC is OPEN);
  - **open-only**: removal is possible only through a member's own OPEN branch (N_XI or N_EPSG), which nothing
    decides.

The most-removed set is z3's, in six-way terms: BITS, TOPO, DIST, HOLD, MATTER, LOOP.

| # | combination | variants | consistent | clash | most removed (best consistent variant) | complementary variants | tested by | other variants' reason |
|---|---|---|---|---|---|---|---|---|
| 1 | IT | 8 | 7 | b | HOLD,TOPO (ITB,RI) | 1 | T-D | single |
| 2 | SET | 12 | 12 | - | BITS (W2) | 0 | - | no-removal,open-only,single |
| 3 | FR | 12 | 8 | a | LOOP (F1) | 0 | - | no-removal,open-only,single |
| 4 | 12 | 4 | 4 | - | none (H12) | 0 | - | no-removal,open-only |
| 5 | INF | 4 | 4 | - | none (INFO) | 0 | - | no-removal,open-only |
| 6 | ZER | 4 | 4 | - | none (ZERO) | 0 | - | no-removal,open-only |
| 7 | NUL | 4 | 4 | - | none (NULL) | 0 | - | no-removal,open-only |
| 8 | IT+SET | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,RI) | 5 | T-B,T-C,T-D | single |
| 9 | IT+FR | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,RI) | 8 | T-A,T-D | single |
| 10 | IT+12 | 8 | 7 | b | HOLD,TOPO (ITB,H12,RI) | 1 | T-D | single |
| 11 | IT+INF | 8 | 7 | b | HOLD,TOPO (ITB,INFO,RI) | 1 | T-D | single |
| 12 | IT+ZER | 8 | 7 | b | HOLD,TOPO (ITB,ZERO,RI) | 1 | T-D | single |
| 13 | IT+NUL | 8 | 7 | b | HOLD,TOPO (ITB,NULL,RI) | 1 | T-D | single |
| 14 | SET+FR | 36 | 24 | a | BITS,LOOP (W2,F1) | 4 | T-A,T-C | no-removal,open-only,single |
| 15 | SET+12 | 12 | 12 | - | BITS (W2,H12) | 0 | - | no-removal,open-only,single |
| 16 | SET+INF | 12 | 12 | - | BITS (W2,INFO) | 0 | - | no-removal,open-only,single |
| 17 | SET+ZER | 12 | 12 | - | BITS (W2,ZERO) | 0 | - | no-removal,open-only,single |
| 18 | SET+NUL | 12 | 12 | - | BITS (W2,NULL) | 0 | - | no-removal,open-only,single |
| 19 | FR+12 | 12 | 8 | a | LOOP (F1,H12) | 0 | - | no-removal,open-only,single |
| 20 | FR+INF | 12 | 8 | a | LOOP (F1,INFO) | 0 | - | no-removal,open-only,single |
| 21 | FR+ZER | 12 | 8 | a | LOOP (F1,ZERO) | 0 | - | no-removal,open-only,single |
| 22 | FR+NUL | 12 | 8 | a | LOOP (F1,NULL) | 0 | - | no-removal,open-only,single |
| 23 | 12+INF | 4 | 4 | - | none (H12,INFO) | 0 | - | no-removal,open-only |
| 24 | 12+ZER | 4 | 4 | - | none (H12,ZERO) | 0 | - | no-removal,open-only |
| 25 | 12+NUL | 4 | 4 | - | none (H12,NULL) | 0 | - | no-removal,open-only |
| 26 | INF+ZER | 4 | 4 | - | none (INFO,ZERO) | 0 | - | no-removal,open-only |
| 27 | INF+NUL | 4 | 4 | - | none (INFO,NULL) | 0 | - | no-removal,open-only |
| 28 | ZER+NUL | 4 | 4 | - | none (ZERO,NULL) | 0 | - | no-removal,open-only |
| 29 | IT+SET+FR | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 30 | IT+SET+12 | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,RI) | 5 | T-B,T-C,T-D | single |
| 31 | IT+SET+INF | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,INFO,RI) | 5 | T-B,T-C,T-D | single |
| 32 | IT+SET+ZER | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,ZERO,RI) | 5 | T-B,T-C,T-D | single |
| 33 | IT+SET+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 34 | IT+FR+12 | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,RI) | 8 | T-A,T-D | single |
| 35 | IT+FR+INF | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,INFO,RI) | 8 | T-A,T-D | single |
| 36 | IT+FR+ZER | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,ZERO,RI) | 8 | T-A,T-D | single |
| 37 | IT+FR+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,NULL,RI) | 8 | T-A,T-D | single |
| 38 | IT+12+INF | 8 | 7 | b | HOLD,TOPO (ITB,H12,INFO,RI) | 1 | T-D | single |
| 39 | IT+12+ZER | 8 | 7 | b | HOLD,TOPO (ITB,H12,ZERO,RI) | 1 | T-D | single |
| 40 | IT+12+NUL | 8 | 7 | b | HOLD,TOPO (ITB,H12,NULL,RI) | 1 | T-D | single |
| 41 | IT+INF+ZER | 8 | 7 | b | HOLD,TOPO (ITB,INFO,ZERO,RI) | 1 | T-D | single |
| 42 | IT+INF+NUL | 8 | 7 | b | HOLD,TOPO (ITB,INFO,NULL,RI) | 1 | T-D | single |
| 43 | IT+ZER+NUL | 8 | 7 | b | HOLD,TOPO (ITB,ZERO,NULL,RI) | 1 | T-D | single |
| 44 | SET+FR+12 | 36 | 24 | a | BITS,LOOP (W2,F1,H12) | 4 | T-A,T-C | no-removal,open-only,single |
| 45 | SET+FR+INF | 36 | 24 | a | BITS,LOOP (W2,F1,INFO) | 4 | T-A,T-C | no-removal,open-only,single |
| 46 | SET+FR+ZER | 36 | 24 | a | BITS,LOOP (W2,F1,ZERO) | 4 | T-A,T-C | no-removal,open-only,single |
| 47 | SET+FR+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 48 | SET+12+INF | 12 | 12 | - | BITS (W2,H12,INFO) | 0 | - | no-removal,open-only,single |
| 49 | SET+12+ZER | 12 | 12 | - | BITS (W2,H12,ZERO) | 0 | - | no-removal,open-only,single |
| 50 | SET+12+NUL | 12 | 12 | - | BITS (W2,H12,NULL) | 0 | - | no-removal,open-only,single |
| 51 | SET+INF+ZER | 12 | 12 | - | BITS (W2,INFO,ZERO) | 0 | - | no-removal,open-only,single |
| 52 | SET+INF+NUL | 12 | 12 | - | BITS (W2,INFO,NULL) | 0 | - | no-removal,open-only,single |
| 53 | SET+ZER+NUL | 12 | 12 | - | BITS (W2,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 54 | FR+12+INF | 12 | 8 | a | LOOP (F1,H12,INFO) | 0 | - | no-removal,open-only,single |
| 55 | FR+12+ZER | 12 | 8 | a | LOOP (F1,H12,ZERO) | 0 | - | no-removal,open-only,single |
| 56 | FR+12+NUL | 12 | 8 | a | LOOP (F1,H12,NULL) | 0 | - | no-removal,open-only,single |
| 57 | FR+INF+ZER | 12 | 8 | a | LOOP (F1,INFO,ZERO) | 0 | - | no-removal,open-only,single |
| 58 | FR+INF+NUL | 12 | 8 | a | LOOP (F1,INFO,NULL) | 0 | - | no-removal,open-only,single |
| 59 | FR+ZER+NUL | 12 | 8 | a | LOOP (F1,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 60 | 12+INF+ZER | 4 | 4 | - | none (H12,INFO,ZERO) | 0 | - | no-removal,open-only |
| 61 | 12+INF+NUL | 4 | 4 | - | none (H12,INFO,NULL) | 0 | - | no-removal,open-only |
| 62 | 12+ZER+NUL | 4 | 4 | - | none (H12,ZERO,NULL) | 0 | - | no-removal,open-only |
| 63 | INF+ZER+NUL | 4 | 4 | - | none (INFO,ZERO,NULL) | 0 | - | no-removal,open-only |
| 64 | IT+SET+FR+12 | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 65 | IT+SET+FR+INF | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,INFO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 66 | IT+SET+FR+ZER | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,ZERO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 67 | IT+SET+FR+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 68 | IT+SET+12+INF | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,INFO,RI) | 5 | T-B,T-C,T-D | single |
| 69 | IT+SET+12+ZER | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,ZERO,RI) | 5 | T-B,T-C,T-D | single |
| 70 | IT+SET+12+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 71 | IT+SET+INF+ZER | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,INFO,ZERO,RI) | 5 | T-B,T-C,T-D | single |
| 72 | IT+SET+INF+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,INFO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 73 | IT+SET+ZER+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,ZERO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 74 | IT+FR+12+INF | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,INFO,RI) | 8 | T-A,T-D | single |
| 75 | IT+FR+12+ZER | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,ZERO,RI) | 8 | T-A,T-D | single |
| 76 | IT+FR+12+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,NULL,RI) | 8 | T-A,T-D | single |
| 77 | IT+FR+INF+ZER | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,INFO,ZERO,RI) | 8 | T-A,T-D | single |
| 78 | IT+FR+INF+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,INFO,NULL,RI) | 8 | T-A,T-D | single |
| 79 | IT+FR+ZER+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,ZERO,NULL,RI) | 8 | T-A,T-D | single |
| 80 | IT+12+INF+ZER | 8 | 7 | b | HOLD,TOPO (ITB,H12,INFO,ZERO,RI) | 1 | T-D | single |
| 81 | IT+12+INF+NUL | 8 | 7 | b | HOLD,TOPO (ITB,H12,INFO,NULL,RI) | 1 | T-D | single |
| 82 | IT+12+ZER+NUL | 8 | 7 | b | HOLD,TOPO (ITB,H12,ZERO,NULL,RI) | 1 | T-D | single |
| 83 | IT+INF+ZER+NUL | 8 | 7 | b | HOLD,TOPO (ITB,INFO,ZERO,NULL,RI) | 1 | T-D | single |
| 84 | SET+FR+12+INF | 36 | 24 | a | BITS,LOOP (W2,F1,H12,INFO) | 4 | T-A,T-C | no-removal,open-only,single |
| 85 | SET+FR+12+ZER | 36 | 24 | a | BITS,LOOP (W2,F1,H12,ZERO) | 4 | T-A,T-C | no-removal,open-only,single |
| 86 | SET+FR+12+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,H12,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 87 | SET+FR+INF+ZER | 36 | 24 | a | BITS,LOOP (W2,F1,INFO,ZERO) | 4 | T-A,T-C | no-removal,open-only,single |
| 88 | SET+FR+INF+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,INFO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 89 | SET+FR+ZER+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,ZERO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 90 | SET+12+INF+ZER | 12 | 12 | - | BITS (W2,H12,INFO,ZERO) | 0 | - | no-removal,open-only,single |
| 91 | SET+12+INF+NUL | 12 | 12 | - | BITS (W2,H12,INFO,NULL) | 0 | - | no-removal,open-only,single |
| 92 | SET+12+ZER+NUL | 12 | 12 | - | BITS (W2,H12,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 93 | SET+INF+ZER+NUL | 12 | 12 | - | BITS (W2,INFO,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 94 | FR+12+INF+ZER | 12 | 8 | a | LOOP (F1,H12,INFO,ZERO) | 0 | - | no-removal,open-only,single |
| 95 | FR+12+INF+NUL | 12 | 8 | a | LOOP (F1,H12,INFO,NULL) | 0 | - | no-removal,open-only,single |
| 96 | FR+12+ZER+NUL | 12 | 8 | a | LOOP (F1,H12,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 97 | FR+INF+ZER+NUL | 12 | 8 | a | LOOP (F1,INFO,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 98 | 12+INF+ZER+NUL | 4 | 4 | - | none (H12,INFO,ZERO,NULL) | 0 | - | no-removal,open-only |
| 99 | IT+SET+FR+12+INF | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,INFO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 100 | IT+SET+FR+12+ZER | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,ZERO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 101 | IT+SET+FR+12+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 102 | IT+SET+FR+INF+ZER | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,INFO,ZERO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 103 | IT+SET+FR+INF+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,INFO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 104 | IT+SET+FR+ZER+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,ZERO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 105 | IT+SET+12+INF+ZER | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,INFO,ZERO,RI) | 5 | T-B,T-C,T-D | single |
| 106 | IT+SET+12+INF+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,INFO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 107 | IT+SET+12+ZER+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,ZERO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 108 | IT+SET+INF+ZER+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,INFO,ZERO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 109 | IT+FR+12+INF+ZER | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,INFO,ZERO,RI) | 8 | T-A,T-D | single |
| 110 | IT+FR+12+INF+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,INFO,NULL,RI) | 8 | T-A,T-D | single |
| 111 | IT+FR+12+ZER+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,ZERO,NULL,RI) | 8 | T-A,T-D | single |
| 112 | IT+FR+INF+ZER+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,INFO,ZERO,NULL,RI) | 8 | T-A,T-D | single |
| 113 | IT+12+INF+ZER+NUL | 8 | 7 | b | HOLD,TOPO (ITB,H12,INFO,ZERO,NULL,RI) | 1 | T-D | single |
| 114 | SET+FR+12+INF+ZER | 36 | 24 | a | BITS,LOOP (W2,F1,H12,INFO,ZERO) | 4 | T-A,T-C | no-removal,open-only,single |
| 115 | SET+FR+12+INF+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,H12,INFO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 116 | SET+FR+12+ZER+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,H12,ZERO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 117 | SET+FR+INF+ZER+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,INFO,ZERO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 118 | SET+12+INF+ZER+NUL | 12 | 12 | - | BITS (W2,H12,INFO,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 119 | FR+12+INF+ZER+NUL | 12 | 8 | a | LOOP (F1,H12,INFO,ZERO,NULL) | 0 | - | no-removal,open-only,single |
| 120 | IT+SET+FR+12+INF+ZER | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,INFO,ZERO,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 121 | IT+SET+FR+12+INF+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,INFO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 122 | IT+SET+FR+12+ZER+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,ZERO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 123 | IT+SET+FR+INF+ZER+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,INFO,ZERO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 124 | IT+SET+12+INF+ZER+NUL | 24 | 17 | b,c | BITS,HOLD,TOPO (W2,ITB,H12,INFO,ZERO,NULL,RI) | 5 | T-B,T-C,T-D | single |
| 125 | IT+FR+12+INF+ZER+NUL | 24 | 14 | a,b | HOLD,LOOP,TOPO (F1,ITB,H12,INFO,ZERO,NULL,RI) | 8 | T-A,T-D | single |
| 126 | SET+FR+12+INF+ZER+NUL | 36 | 24 | a | BITS,LOOP (W2,F1,H12,INFO,ZERO,NULL) | 4 | T-A,T-C | no-removal,open-only,single |
| 127 | IT+SET+FR+12+INF+ZER+NUL | 72 | 34 | a,b,c | BITS,HOLD,LOOP,TOPO (W2,F1,ITB,H12,INFO,ZERO,NULL,RI) | 22 | T-A,T-B,T-C,T-D,T-E | single |
| 128 | (readings only) | 3 | 3 | - | none (RI) | 0 | - | no-removal,open-only |

## 7. Not tested by instrument, with the reason (no silent caps)

Every one of the 3,071 variants is screened in z3. The **640 complementary variants** are covered by tests T-A
through T-E. The other 2,431 are not tested by instrument, for these reasons:

| reason | variants |
|---|---|
| INCONSISTENT: a named clash (a, b or c); nothing to test | 1,152 |
| SINGLE CONTRIBUTOR: one member's removal set covers the variant's; graded in that member's A-report, and z3 confirms no other member is load-bearing | 896 |
| NO REMOVAL: no member removes any obstruction, so nothing is complementary | 127 |
| OPEN ONLY: removal is possible only through ξ > 0 (R-QUANTUM) or ε_G (KR), which no source decides | 256 |

To get the variant-by-variant list with each reason, run `python3 combine.py --json PATH`. Each row carries the
variant's literals, its consistency, its clash core, and its per-obstruction verdict with core.

## 8. Named hypotheses

Everything above rests on these, listed in `combine.py`.

**Conditional named hypotheses** (assumed only where an unsat core shows a removal needs them):

- **N_EPS**: ε is at least the strength needed, and the drift is not excluded by the unread bound. It brings in A1's
  H-MAP, H-TRANSFER, H-SPIN, H-COHERE and H-FRAME3b.
- **N_SIGKEY**: the signal is keyed to the preferred slicing. This is A1's H-SIG-COR.
- **N_CORR**: H-CORRIDOR-MODEL, the latticectc model H1-H3.
- **N_QTOPO**: the corridor is not a Lorentzian topology change. For ITE this is MS p.17; for ITB it is the charter's
  reading.

**OPEN pathways** (never assumed in a removal):

- **N_XI**: ξ > 0 (Fewster-Osterbrink, board NARROWED).
- **N_EPSG**: KR p.13-14.
- **N_VAC**: vacuum entanglement used as the pairs (Reznik, READ, above).

**Encoding choices, named:**

- The six-way split of O-MAKE.
- R-INDEX's physical removal applies only with ITB, not ITE. Under ER=EPR the bridge is geometry and MS fn.1
  applies.
- A corridor network is present in every variant, because M's device includes the corridor.
- An absent hypothesis is asserted false (closed world). A combination commits to its members and nothing more.
- A combination is "complementary" when no single member's removal set covers the variant's.
- The work items' own named hypotheses carry through unchanged: A1's §2 list; A2's H-CMB-IS-COSMIC, H-NOT-DE-SITTER,
  H-KILLING-SEARCH, H-DCTC-CONVENTION; A3's H-ALT, H-FAITHFUL, H-R; A4's H-QUDIT, H-ER=EPR, H-EQUIL, H-PATH, H_flat.

## 9. Sources

| source | status | used for |
|---|---|---|
| Maldacena & Susskind, arXiv:1306.0533v2 | **READ this pass** | fn.1 p.2 (non-traversability assumed: "If this were not true, the ER=EPR connection would be wrong"); §3.1 p.16 (no superluminal signals); §3.2 pp.16-17 (no creation by LOCC; "without preexisting bridges"; make, separate, merge); p.17 (non-trivial topologies "should be allowed as possible quantum states"); §5.4 pp.36-37 (a geometric feature is a linear operator). Clash (c), B-LOCC, N_QTOPO. |
| Reznik, arXiv:quant-ph/0212044v2 | **READ this pass** | p.1: causally disconnected probes end up entangled, and the entanglement vanishes with separation. p.10: accelerated probes, amplitudes exponentially small. p.12, Fig. 2: inertial probes, L/T < 1.1. N_VAC. |
| the four A-reports and their instruments | imported and re-run | every ground in `_board` and `_commitments`; each READ citation there is the A-report's |
| LEDGER.md (S5, S10, S13), transit.py, emtension.py | read from the board, never written | B-RECV, B-LOCC, C-ITE |

No host refused a request. Both alphaXiv calls returned page text.

## 10. Findings (recorded, not repaired)

1. **No combination removes all five.** O-MATTER survives every consistent combination, by a board holding none of
   the seven touches. O-MAKE-DIST survives every consistent combination unless N_VAC, which is OPEN.
2. **M's H-FRAME sentence contradicts itself when both clauses are taken strong** (clash a, 640 variants). Clause 1
   keeps the loops out. Clause 2b brings them back.
3. **H-IT read as ER=EPR cannot be combined with M's settling** (clash c). The collision is with Maldacena-Susskind's
   own stated assumptions, now READ. ITB carries no such assumption, and ITB + W2 is consistent.
4. **The two readings of "supplied by probability" cannot both be physical under H-IT** (clash b).
5. **The instruction's payoff is real and measured:** O-HOLD falls only to H-IT and R-INDEX together.
6. **The most-removing combination is an amortisation scheme.** Later transits beat light by L/2c, conditionally.
   The first cannot, because the pairs (6.21 or more per qubit) and the holder arrive at ≤ c. This is the shape
   LEDGER.md's S5 already records.
7. **A2-frame.json on disk carries a `summary`, not a `grades` list.** The drift guard reads A2's grades from
   `frame.GRADES` and that summary. Recorded; nothing outside docket68/ was edited.

## 11. Testable predictions

- **{W2, F1}.** Bob's mean σ_y shifts by tanh(2εT) when Alice switches from z to x. The arrival is keyed to CMB-frame
  simultaneity plus T. The same pairs read in the lab frame show the ordering dependence: 1/2 against 2/3 or 1/3.
- **W2 on partly entangled pairs (T-B).** The shift must follow the shared entanglement: 0.240 at S = 0.53 bits and
  0.042 at S = 0.13 bits (ε = 0.1, T = 3), and exactly 0 for product pairs. A local systematic would not track the
  partner's entanglement, so this separates a drift signal from an artefact.
- **{ITB, R-INDEX}.** No throat and no NEC test applies. The prediction moves to the holder: a gravitating energy of
  at least 33-379 J at R = 1 m for a 70 kg definition (A3's Bekenstein floor).
