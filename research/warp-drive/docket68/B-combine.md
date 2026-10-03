# DOCKET 68 · B-combine: the seven hypotheses in combination

**Status: a docket work item, wave 3 (repaired 2026-10-03 after the two re-verifications in
`wave1/REPAIR1-RESULT.json`, key `result.reverify`). Nothing here is seated.** The instrument is `combine.py`, beside
this file. `PYTHONDONTWRITEBYTECODE=1 python3 combine.py --selftest` runs **85 checks and passes all 85** in about
190 s (z3, numpy, sympy; the screen runs in four worker processes). Seventeen of the checks are controls. **Five items
cannot fail and are reported as STRUCTURAL, not counted:** the engine's premise-consistency of supports, three ground
values (the D-CTC under C1, a state-independent unitary in `w2_ancilla_flow`, the Bob-first row of `drift_ordering`),
and the INDEPENDENT classes, which carry no test by definition. Further STRUCTURAL labels sit beside the figures they
qualify (the ratio 2.000000 in T-E; the 1 AU, N = 1e6 board equality).

*Wave 2 first said:* "65 checks and passes all 65 ... One guard cannot fail by construction". Two of those 65 could not
fail and were counted (the coverage check, the T-E ratio): RV-0 #9, #10. *Wave 1 first said* "80 checks".

`combine.py` imports what it uses and copies nothing: `settle.py`, `frame.py`, `measure.py`, `geometry.py` (the four
work items, wave 3 as repaired by R2-alone); `nlcontrol.py`, `corridors.py`, `nosig.py` through them; `../transit.py`,
`../emtension.py`, and `../LEDGER.md` (read, never written). It writes nothing outside `docket68/` except output paths
the caller names. It compares itself with the A-reports' wave-3 JSON grades.

M's standing instruction, verbatim from the charter: *"Remember that some of the hypothesies lined up for docket 68
may turn out, after initial testing, to work better in combination."* M's hypotheses are carried as hypotheses. Each
grade says what a combination does, not whether it is true.

## The answer, first (section 3 has the detail)

**Member-attributed removals — what the hypotheses themselves remove — number at most ONE in any consistent variant,
counted inside one consistent premise set (an "account"), and it is always O-BITS:**

- **by H-SETTLE W2 × H-FRAME** (clause 1, or clause 2b's cosmic clock): O-BITS **REMOVED-IF {W2, F1; N_EPS}** — a
  JOINT result (a synergy: neither member removes it alone; 192 variants at 1 ly). N_EPS carries the removal set
  R_W2 = {ε > ε_any(L, N), H-C2 with its no-branch rule, H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB,
  H-BLOCK}. It holds at **1 ly, N = 7** and at **1 AU, N = 10⁶** (window computed open); at **1 AU, N = 7 and
  N = 10³** only with H-12 supplying an unbounded carrier (N_H12W, no READ source). Pair counts from N·C ≥ 2 are
  **floors** (zero-error capacity 0 at D < 1); reliable transfer is block-coded (H-BLOCK);
- **or by H-FRAME clause 2b alone**, through a CTC at Bob: O-BITS **REMOVED-IF {F2b; N_DCTC}** (the D-CTC, computed
  2.000000 bits per pair over four axes, zero-error, so 1 pair per teleported qubit), at **every distance**, with
  **O-LOOP reintroduced** (the channel is a CTC; M-S1A-P3: disqualifying at the seat only). A CTC is not shown to exist.

**NOT-BOUND-IF (not removals):** under H-IT as an information layer (ITB + N_QTOPO), O-MAKE-TOPO, O-HOLD's geometric
form **and the corridor form of O-LOOP** — their theorems do not bind a non-geometric corridor; what that corridor costs
is OPEN (N_ILFREE). In five-way terms at most 2 (O-HOLD, O-LOOP), because O-MAKE also needs its distribution form.

**Removed with no member (the geometry's, the board's or a premise's):** corridor O-LOOP by exact FRW {N_CORR, N_FRW}
— only in accounts without N_QTOPO, since the two corridor accounts clash (B-QCORR) — and signal O-LOOP by N_SIGKEY.

**Survivors of every consistent variant:** O-MATTER (LEFT; H-INFO's sufficiency reading clashes with B-RECV — clash
(d), M's to rule) and O-MAKE in its distribution form (OPEN via N_VAC only).

*Wave 2 first said:* "The most is **three of five** (O-BITS REMOVED-IF, O-HOLD NOT-BOUND-IF, O-LOOP REMOVED-IF),
attained by 64 consistent variants ... Every one of them contains {H-SETTLE W2, H-IT ITB}". That count added a
REMOVED-IF, a NOT-BOUND-IF and the geometry's removal, mixed two clashing corridor accounts (N_QTOPO and N_CORR), and
credited O-BITS to W2 alone through a premise (N_FRAME3b) that presupposes F1 (RV-0 #2, #8; RV-1 #2). The wave-2 figure
recomputed per account is still 3 (32 variants, smallest {W2, F1, ITB}), and it is reported below as history, not as
the answer.

## 0. Wave-3 repair: every item in both re-verifications, and what was done

**The principle, applied symmetrically, stated once.** *A theorem that does not bind a non-geometric corridor makes
the obstruction NOT-BOUND-IF (its premise named), never REMOVED.* Wave 3 applies it to the third theorem family it
had missed: the exact-FRW keying lemma and latticectc's loop theorem are theorems about Lorentzian quotients, so under
ITB + N_QTOPO they do not bind the corridor either. **O-LOOP is split** into a corridor form (O-LOOP-C, which can be
NOT-BOUND-IF) and a signal/CTC form (O-LOOP-S, unchanged). The two corridor accounts are a **premise clash**
{N_QTOPO, N_CORR} (constraint B-QCORR), and **every headline figure is counted inside one account**. O-LOOP's FRW
removal is credited to the geometry and to no hypothesis, uniformly (in combine and in the repaired A1-A4).

### RV-0 (AGAINST M) — unresolved items

| item | resolution |
|---|---|
| U0: FOR #2 applied twice, A1 credits O-LOOP to H-SETTLE-W alone; B whitelists it | **Applied.** A1 now grades O-LOOP "LEAVES (member); corridors: geometry column" (R2-alone). combine reports the corridor removal as `Rg` (no member) in every account where it holds. The EXPLAINED entries for A1 {W2} and {W2, H12} O-LOOP are **deleted, not kept**; the drift guard now agrees on them. |
| U1: FOR #3 half applied in A4 (H-ZERO + H-IT, H-IT + H-NULL not split by reading) | **Applied.** A4 splits both rows by ITE / ITB / ITJ (R2-alone). combine carries the new reading **ITJ** and compares all six split rows by parse rule P7 (the clause for the variant's reading). The A4 {ITE, ZERO} EXPLAINED entry is deleted; agreement is computed. |
| U2: AGAINST #4, the 7 disagreements pass through a hand-typed EXPLAINED dict | **Applied.** Five wave-2 causes are gone because their A-side was repaired, not whitelisted. **Two disagreements remain of 168 comparisons**, each with a computed or READ reason (section 2). A new check fails if any EXPLAINED key is not a live disagreement (no stale whitelist). |
| U3: AGAINST #13, N_FRAME3b never adds F1 back, so {W2} alone is credited O-BITS | **Applied.** N_FRAME3b is **withdrawn** (it presupposes F1: A1 wave 3, corroborated READ 2511.15935v1 p.2). {W2} alone: O-BITS **LEFT**. The removal is W2 × F1's (or W2 × F2b's). H-SLICE-INTRINSIC (a slicing the drift picks without a preferred frame) is named, not credited; a third mutated encoding, `wave2-SLICE-INTRINSIC`, re-credits it and **is caught** (163/168, unexplained on A1 {W2}, {W2, H12} and A3 {W2, INFO}). |
| U4: four-basis D-CTC figure cited, not computed; N_H12W, N_MEASPHYS, N_QTOPO, N_ILFREE no READ source; Weinberg bounds NAMED-NOT-READ | **Computed:** `frame.four_basis_c2_table` is re-run in combine's grounds and in T-J: 2.000000 bits per pair under C2, map reproduced with P = 1, BHW condition-2 minimum 0.1738; `bb84_c2_table` 1.000000. **Unchanged and stated:** N_H12W, N_MEASPHYS, N_QTOPO and N_ILFREE still have no READ source, and every verdict resting on them names it. The Weinberg-family values stay NAMED-NOT-READ (R2-alone's two further READs, 2509.04320v1 and 2511.15935v1, carry no numbers): **OPEN**. |

### RV-0 (AGAINST M) — problems

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

### RV-1 (FOR M) — unresolved items

| item | resolution |
|---|---|
| U0: four-basis figure answered by restricting to H-BORN-AT-BOB on the qubit alone | **Applied.** The figure is computed (U4 above). T-E names the qubit-only subclass (H-BORN-AT-BOB + **H-QUBIT-DRIFT**) and adds the computed W2 member without H-QUBIT-DRIFT (`settle.w2_ancilla_flow`: 2.000000 bits per pair, zero-error, P(b′\|b) = identity, curves separated by 0.395 rad against a 0.0037 rad grid; smooth extension H-EXTEND derived, not computed): **1 pair per teleported qubit**. Not evidence such a drift exists. |
| U1: T-D still assigned as a covering test | **Applied.** T-D is a record and covers nothing (RV-0 #9). |

### RV-1 (FOR M) — problems

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

### The task's own items

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

### Wave 2's section 0, kept as history

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
  - **H-INFO**: INFO is necessity; INFOS is sufficiency (A3's H-INFO-S).
- **Reading slots** none / R-INDEX / R-QUANTUM / both: (4·4·4·3·2·2·2 − 1)·4 + 3 = **6,143 variants**, none skipped.
  *Wave 2:* 4,607 (no ITJ). *Wave 1:* 3,071.
- **Distance cells.** **1 ly, N = 7** (window non-empty under both H-MAP readings), all variants. **1 AU, N = 7**
  (window empty under both), the **1,536 W2 variants** re-screened; complete, because N_EPS occurs only in B-CAP and
  B-EPSWIN and the board admits no CAP without W2 (z3), and the D-CTC route does not depend on distance. **1 AU,
  N = 10⁶**: window computed open, so it screens as 1 ly. N is always a floor.
- **Seven obstruction forms.** O-MAKE as O-MAKE-TOPO and O-MAKE-DIST; O-LOOP as O-LOOP-C (corridor loops) and O-LOOP-S
  (signal and CTC loops). In five-way terms a split obstruction counts only if both forms do.

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
  jointly SAT at 1 ly and jointly **UNSAT** at 1 AU, N = 7 (content); named and OPEN together SAT; the board admits a
  loop and no loop. **CONTROL:** with B-RECV deleted, O-MATTER becomes removable.
- **Contradictions that must be caught** (twelve, every one caught): ITE & W2; INFOS; a planted signal in linear QM;
  F1 & F2b under {N_KEYING, N_2BVIA}; F2b under {N_FRW, N_2BVIA}; ITB & RQ under {N_QTOPO}; W2 at 1 AU, N = 7 without
  H12 under {N_EPS}; and, new in wave 3: **W2 alone signals nothing**; **ITB under {N_QTOPO, N_CORR}**; **F2b under
  {N_FRW, N_DCTC}**; **ITE & F2b under {N_DCTC}**; **a planted D-CTC channel without clause 2b**.
- **Results that used to be clashes:** F1 & F2b, and ITB & RI & RQ, are consistent as commitments.
- **STRUCTURAL, not counted.** Supports are drawn only from premise sets consistent with the variant (engine
  construction); its content is the control that the wave-1 engine at 1 AU, N = 7 reports **3 of 3** vacuous REMOVED-IF.
- **Named-premise census** (can a premise fail at all?):

  | named premise | inadmissible in (1 ly) | in a support (1 ly) | at 1 AU, N = 7 (W2 variants) |
  |---|---|---|---|
  | N_EPS | 0 — **STRUCTURAL at 1 ly** | 576 | **inadmissible in 384** (empty window, no H12) |
  | N_DCTC | 1,920 ({N_FRW}: 1,536; ITE: 384) | 1,536 | 384 |
  | N_FRW | 1,920 | 1,919 | 384 |
  | N_2BVIA | 1,920 | 0 | 384 |
  | N_QTOPO | 1,024 (RQ; N_CORR) | 512 | 256 |
  | N_KEYING | 960 | 960 | 192 |
  | N_CORR | 512 (N_QTOPO / N_MEASPHYS) | 1,919 | 128 |
  | N_MEASPHYS | 512 | 256 | 128 |
  | N_SIGKEY, N_MS17, N_H12W | 0 — **STRUCTURAL: assuming them cannot fail** | 192 / 768 / 0 | N_H12W in a support in 288, never inadmissible |

  *Wave 2 first said* N_FRAME3b, N_SIGKEY, N_CORR, N_MS17 and N_H12W were never constrained; N_FRAME3b is withdrawn
  and N_CORR is now constrained by B-QCORR.
- **Encoding drift: z3 against the A-reports' own wave-3 grades.** 32 (variant, cell, grade) rows, parsed by stated
  rules (`parse_report_class`: P1 every parenthetical dropped; P2 aliases; P4 corridor clause; **P7** the clause for
  the variant's H-IT reading; **P8** the first clause outside braces; **P9** LEFT-IF reads OPEN; P3 precedence;
  `z3_class`: Z1 a removal or non-binding counts for a hypothesis only if a support contains it; Z2 OPEN via N_VAC is
  not carried; Z3 an NB returns its removal's OPEN; Z4 the five-way O-MAKE is the weaker form; **Z5** the five-way
  O-LOOP counts only if both forms are removed or not-bound). **166 of 168 comparisons agree.** The two that do not:

  | report, variant, obstruction | why z3 differs |
  |---|---|
  | A2, {F2b}, O-MAKE | **Vocabulary.** A2: "NOT-BOUND-IF {2b's CTC; Geroch-compact case only}; Tipler's non-compact case still binds". The screen's NOT-BOUND needs every theorem of the obstruction unbound, so with Tipler binding O-MAKE-TOPO stays bound (and five-way O-MAKE also needs O-MAKE-DIST, OPEN via N_VAC only). A2's own D-CTC row grades the same world's O-MAKE LEAVES. Both say O-MAKE is not lifted. |
  | A3, {ITB, RI}, O-LOOP | **A3 omission, open for A3's stage.** A3's R-INDEX grade carries the corridor NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} on O-MAKE and O-HOLD but writes O-LOOP "SILENT; corridors: geometry column". By the symmetric rule (applied in A4's ITB grade) the loop theorems do not bind a non-geometric corridor either: z3 gives O-LOOP-C NOT-BOUND-IF {ITB; N_QTOPO} \| {ITB, RI; N_MEASPHYS}, beside the geometry's REMOVED-IF {N_CORR, N_FRW} in the other account. Not repaired here (not this stage's file). |

  **CONTROLS:** three mutated encodings, each caught as an unexplained disagreement: `KR-unconditional` (A1 {KR} and
  {KR, H12} O-HOLD; 164/168), `wave1-THROAT` (A3 {ITB, RI}, A4 {ITB}, {ITB, ZERO}, {ITB, NULL} O-HOLD; 162/168),
  `wave2-SLICE-INTRINSIC` (A1 {W2}, {W2, H12}, A3 {W2, INFO} O-BITS; 163/168). **Ground row:**
  `settle.h12_carrier_case` at 1 AU, N = 7 says EXCLUDED under H-TRANSFER and NOT EXCLUDED under H-12-CARRIER; z3 gives
  {W2, F1} LEFT and {W2, F1, H12} REMOVED-IF. They agree.
- **Load-bearing guard** (new, RV-0 #6): 12 combination rows checked; every row crediting a removal or non-binding has
  every graded literal load-bearing, or says a member adds nothing (A1 W2 × H12 under H-TRANSFER; A3 H-SETTLE ×
  H-INFO; A4's six H-ZERO / H-NULL × H-IT rows, whose ZERO / NULL add nothing). All agree.
- **Grounds re-run, each against an independent computation or with content:** tanh(2εT); C1 2.2e-16; the drift
  ordering against tanh(2ε(T − t_A)) at t_A < T; the antitelephone against −uL; cosmic keying, 0 failures at ranks 2
  and 3; the FRW lemma (unsat; vacuity sat; control a ≥ 0 sat); nlcontrol N < 7 impossible, CMAX = log₂1.25; H-12
  carrier flips, 2; LOCC 8.9e-16; QEI fraction 2.08e-68 (under {H_flat, H-PATH, H-MIN-SCALAR}); zero shift `unsat`;
  EGJ β_crit = −r0²/2 = 1.91e69 l_P² at 1 m, r⁴T_kk → −2r0², β = 0 reproduces R_kk; INFOS support; and, new:
  **D-CTC** four axes 2.000000 bits per pair (C2), BB84 1.000000; **zero-error** 1 codeword at D < 1, control 2/4/8;
  **W2 member without H-QUBIT-DRIFT** χ = 2.000000, P(b′\|b) = identity; **windows** 1 ly N = 7 open, 1 AU N = 7 empty,
  1 AU N = 10⁶ open; the board flags and LEDGER S5/S10/S13.

### Contradictory combinations: every core, counted by inclusion-exclusion

Of the 6,143 variants, **3,839 are consistent and 2,304 are not.** Every one of the 127 combinations has a consistent
variant. 320 inconsistent variants have more than one core.

| clash | cores (variants) | present in | alone in | what collides | label |
|---|---|---|---|---|---|
| **(c) W2 + ITE** | C-ITE + C-W2, linearity (384); C-ITE + B-GISIN + C-F1 (192); C-ITE + B-GISIN + C-F2b (192) | 384 | 256 | ER=EPR as MS state it (fn.1 p.2; §3.1 p.16; §5.4 pp.36-37, READ) against a per-branch drift; T-B: the drift signals 0.537 at β = 0 in Van Raamsdonk's state | **INCONSISTENT-AS-ENCODED**: a test of ER=EPR, not a refutation of W2. *Wave 1 first said* REFUTED. |
| **(d) INFOS** | C-INFOS + B-RECV (2,048) | 2,048 | 1,920 | H-INFO-S against B-RECV | **CLASH, board versus M. M's to rule.** Not a retirement. |

Intersection 128; union 384 + 2,048 − 128 = **2,304**, the inconsistent count. (*Wave 2:* 1,792 over 4,607.)

**B-RECV's conditions, listed beside clash (d)** — what a ruling for H-INFO-S would have to overturn (A3 wave 3;
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
| {N_2BVIA, N_FRW} with F2b | 1,920 | 0 | exact FRW excludes clause 2b if corridors are the route to the cosmic past |
| {N_DCTC, N_FRW} with F2b | 1,536 | 0 | **new:** a global time function admits no CTC, so exact FRW excludes the D-CTC channel |
| {N_2BVIA, N_KEYING} with F1 + F2b | 960 | 0 | the docket's keying excludes clause 2b (wave 1's clash a; not in M's sentence) |
| {N_CORR, N_QTOPO} with ITB | 512 | 128 | **new (RV-1 #2):** one corridor, two accounts |
| {N_QTOPO} with ITB + RQ | 512 | 128 | ITB's no-geometric-throat premise against R-QUANTUM's throat |
| {N_DCTC} with F2b + ITE | 384 | 0 | **new:** MS linearity against the D-CTC's nonlinearity |
| {N_CORR, N_MEASPHYS} with ITB + RI | 256 | 0 | **new:** the same, through R-INDEX |
| {N_MEASPHYS} with ITB + RI + RQ | 256 | 0 | the same, through R-INDEX |

Union by inclusion-exclusion 2,432. At 1 AU, N = 7 (W2 variants) **{N_EPS} with "not H12"** is added: 384 variants
(128 alone), the empty window; union 640.

**Wave 1's clash census, recomputed** over wave 1's 3,071 variants: (a) F1+F2b present 768 (alone 640), (b) ITB+RI+RQ
256 (192), (c) ITE+W2 256 (192); union 768 + 256 + 256 − 64 − 64 = 1,152. *Wave 1 first said* "(a) 640, (b) 256,
(c) 256", the core z3 happened to return.

## 3. The answer, in detail

Computed by `headline()` over every consistent variant and every account at 1 ly, N = 7 (`headline_au` at 1 AU,
N = 7 agrees in shape):

| figure (per account, never across two) | maximum | variants attaining it | smallest |
|---|---|---|---|
| **member-attributed removals** (five-way) | **1** (always O-BITS) | 1,728 | {F2b} (D-CTC); {W2, F1} for the drift |
| NOT-BOUND-IF (five-way) | 2 (O-HOLD, O-LOOP) | 256 | {ITB} |
| removed with no member (five-way) | 1 (O-LOOP) | 1,919 | {F1} |
| removed only, member or not | 2 (O-BITS + the geometry's O-LOOP) | 192 | {W2, F1} |
| removed or not-bound (wave 2's figure, now per account) | 3 | 32 | {W2, F1, ITB} |

**The variant with the most member-attributed results, {W2, F1, ITB}, at 1 ly, N = 7, in its two accounts:**

| form | account A (N_CORR dropped; N_QTOPO assumed) | account B (N_QTOPO dropped; N_CORR assumed) | supports (all accounts) |
|---|---|---|---|
| O-BITS | **Rm** | **Rm** | {W2, F1; N_EPS} |
| O-MAKE-TOPO | **NBm** | — (LEFT) | NOT-BOUND-IF {ITB; N_QTOPO}; removal OPEN via N_ILFREE |
| O-MAKE-DIST | — | — | OPEN via N_VAC only |
| O-HOLD | **NBm** | — (LEFT) | NOT-BOUND-IF {ITB; N_QTOPO}; removal OPEN via N_ILFREE |
| O-MATTER | — | — | LEFT |
| O-LOOP-C | **NBm** | **Rg** | NOT-BOUND-IF {ITB; N_QTOPO}; REMOVED-IF {N_CORR, N_FRW} \| {F1; N_CORR, N_KEYING} |
| O-LOOP-S | **Rg** | **Rg** | REMOVED-IF {N_SIGKEY} |

So the same three hypotheses give **either** one member removal plus two non-bindings (account A) **or** one member
removal plus the geometry's loop removal (account B), never both. F1's keying route is an *alternative* to the
geometry's, and in every account that admits N_FRW the removal holds without F1 (`Rg`).

**What is never removed by a member:** O-MAKE (both forms), O-HOLD, O-MATTER and both forms of O-LOOP. O-MAKE-TOPO and
O-HOLD are at most NOT-BOUND-IF. **Survivors of every consistent variant (both screened cells):** O-MATTER (LEFT in
all 3,839 consistent variants and all 768 consistent W2 variants at 1 AU, N = 7) and O-MAKE-DIST (OPEN via N_VAC only).

**Synergy (JOINT) and interference.**

- **Synergy: W2 × F1 on O-BITS** — 160 variants at 1 ly ({W2, F1}), 16 + 16 with ITB (and RI); at 1 AU, N = 7 it needs
  H12: 80 variants ({W2, F1, H12}), 8 + 8 with ITB (and RI). *Wave 2 first said* "Synergy: one, and it is H-12's ...
  At 1 ly there is no synergy". That rested on N_FRAME3b.
- **Interference** (a member's result undone in combination), 1 ly: clause 2b undoes the corridor O-LOOP removal (512
  variants: a message into the cosmic past spoils the time function); R-QUANTUM undoes ITB's non-binding (256 + 128);
  **ITE undoes clause 2b's D-CTC O-BITS** (192, and 192 with F2b's own loop interference): MS linearity excludes the
  D-CTC. At 1 AU, N = 7 the same kinds (128, 64, 32, 32).

*Wave 1 first said:* the most is four entries of the six-way split, {W2, F1, ITB, R-INDEX}, with O-HOLD REMOVED.

## 4. JOINT and INDEPENDENT combinations, and the instrument tests

A consistent variant is **complementary** when more than one member contributes a member-attributed result and no
single member's result covers it. Wave 3 splits these (RV-0 #9, RV-1 #7): **JOINT** if some member-attributed result
belongs to no single member (a synergy); **INDEPENDENT** otherwise (every contribution is a single member's own).

- **JOINT: 192 variants at 1 ly in 3 classes, 96 at 1 AU, N = 7 in 3 classes** — all W2 × F1 (× H12 at 1 AU) on O-BITS.
  Each has a content-bearing test (T-A, T-B, T-E; T-G at 1 AU). This check can fail and is counted.
- **INDEPENDENT: 448 variants at 1 ly, 64 at 1 AU** — F1 × ITE (O-MAKE-TOPO non-binding beside F1's loop route), F2b ×
  ITB (the D-CTC's O-BITS beside ITB's non-bindings) and their supersets. **Not instrument-tested as pairs**: each part
  is graded in its member's report; no instrument computes the pair. Reported STRUCTURAL.
- Tests are assigned by a table fixed before the screen runs (`TEST_BEARS`); there is no fallback. **T-D, T-F, T-H and
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
  | 1 ly | 7 | 3.64e-8 | yes | 7.29e-8 |
  | 4.24 ly | 7 | 8.59e-9 | yes | 1.72e-8 |
  | 1 AU | 7 | 2.30e-3 | **no** | 4.61e-3 |
  | 1 AU | 1,000 | 1.06e-4 | **no** | 2.11e-4 |
  | 1 AU | 10⁶ | 3.34e-6 | **yes** | 6.67e-6 |

  None of the 18 entries flips between the two ε. The ratio 2.000000 is an identity of T = atanh(D_N)/(2ε)
  (**STRUCTURAL**, not counted; *wave 2 counted it*).
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
  | W2 member without H-QUBIT-DRIFT (`w2_ancilla_flow`, H-EXTEND) | 1, zero-error |
  | clause 2b's D-CTC, four axes (N_DCTC) | 1, zero-error |

  | count (A3's H-FAITHFUL) | teleportation ebits | nlcontrol, N = 7 (floor) | block-coded (floor) | qubit-only subclass (strictly above) | W2 member / D-CTC (zero-error) | holder FLOOR at R = 1 m |
  |---|---|---|---|---|---|---|
  | species sequence | 9.51e27 | 6.66e28 | 5.91e28 | 1.90e28 | 9.51e27 | 33.2 J |
  | grid 1 Å | 4.14e28 | 2.90e29 | 2.57e29 | 8.28e28 | 4.14e28 | 144 J |
  | grid 0.1 Å | 1.09e29 | 7.61e29 | 6.76e29 | 2.18e29 | 1.09e29 | 379 J |
  | thermal entropy | 2.84e28 | 1.99e29 | 1.76e29 | 5.68e28 | 2.84e28 | 99.1 J |

  *Wave 2 first said:* "nlcontrol pairs, N = 7 (upper figure, one Hamiltonian)" and "W2 class floor, H-BORN-AT-BOB".
- **PASS.**

**T-F (record): RQ × KR.** Two OPENs on O-HOLD. The QEI fraction 2.08e-68 holds under {H_flat, H-PATH,
H-MIN-SCALAR}; ξ > 0, curved-space QEIs (NAMED-NOT-READ) and ε_G are OPEN. *Wave 2 first said* "in-scope fraction".

**T-G: W2 × F1 × H12 at 1 AU, N = 7.** `settle.h12_carrier_case` flips 2 of 9 cells (1 AU at N = 7 and N = 10³); z3
gives {W2, F1} LEFT and {W2, F1, H12} REMOVED-IF at 1 AU, N = 7, and {W2, F1} REMOVED-IF at 1 ly. **PASS.** No READ
source gives a model of a Weinberg-form drift in G or v (N_H12W). At 1 AU, N = 10⁶ H-12 adds nothing.

**T-H (record): ITJ.** `geometry.egj_fR_throat`: T_kk(r0) = 2(−2β − r0²)/r0⁴, ≥ 0 iff β ≤ −r0²/2 (1.91e69 l_P² at
1 m, against EGJ's β ~ l_P²); r⁴T_kk → −2r0² for every β: for the computed shape and f the deficit is moved, not
removed. The pathway (N_EQUIL) is H-IT's in the Jacobson reading. *Wave 2 first called it "(ZERO | NULL) × IT".*

**T-I (record): INFOS vs B-RECV.** φ(1) = 0 bits, Bekenstein 0 bits at E = 0, CARRIES_SUBSTANCE False.

**T-J (new): clause 2b's D-CTC.** `frame.four_basis_c2_table` (BHW 0811.1209v2 pp.3-4 construction, READ by A2):
2.000000 bits per pair under C2, map reproduced with P = 1, condition-2 minimum 0.1738; `bb84_c2_table` 1.000000. C1
gives 0 (STRUCTURAL: the same input for every choice). z3 {F2b}: O-BITS REMOVED-IF {F2b; N_DCTC}. O-LOOP reintroduced.
**PASS.**

## 5. Each hypothesis across every combination (rule 2)

Charter rule 2: *"A failure alone does not retire a hypothesis. It is retired only if it also fails in every
combination tested."* Retirement is established only for an **exercised** literal; the difference census measures it.

| literal | exercised? (changed / with it) | what it contributes | rule 2 |
|---|---|---|---|
| W2 (H-SETTLE, C2) | yes: 576 / 1,536 | O-BITS REMOVED-IF {W2, F1; N_EPS} (or F2b for F1), JOINT; clash (c) with ITE | **kept** (load-bearing in W2 × F1). Alone: LEAVES-ALL |
| W1 (H-SETTLE, C1) | **no** (0) | its one commitment, no signal, is the board's | **UNTESTED-BY-SCREEN**; its grade (LEAVES-ALL, 2.2e-16) stands |
| KR (H-SETTLE) | yes: 768 | O-HOLD OPEN via N_EPSG; removes nothing | kept: OPEN pathway |
| F1 (clause 1) | yes: 1,344 / 3,072 | supplies W2's slicing (O-BITS, JOINT); O-LOOP-C REMOVED-IF {F1; N_CORR, N_KEYING}, an alternative to the geometry's | **kept** |
| F2b (clause 2b) | yes: 2,112 | O-BITS REMOVED-IF {F2b; N_DCTC} (D-CTC), O-LOOP reintroduced; supplies W2's slicing; undoes the corridor loop removal | **kept** |
| ITB (H-IT) | yes: 1,024 / 1,536 | O-MAKE-TOPO, O-HOLD, O-LOOP-C **NOT-BOUND-IF** {N_QTOPO}; removal OPEN via N_ILFREE | kept: NOT-BOUND-IF, no removal |
| ITE (H-IT) | yes: 1,152 | O-MAKE-TOPO NOT-BOUND-IF {N_MS17}; clash (c) with W2; excludes the D-CTC | kept: NOT-BOUND-IF |
| ITJ (H-IT, new) | yes: 1,024 | O-HOLD OPEN via N_EQUIL; removes nothing (moved, not removed, for the computed shape) | kept: OPEN pathway |
| H12 | yes, **at 1 AU, N = 7 only** (384 changed; in a support 288) | the window: O-BITS REMOVED-IF {W2, F1, H12; N_EPS, N_H12W} | **kept** (on the window only). Not retired |
| INFO (necessity) | **no** (0) | none | **UNTESTED-BY-SCREEN**; retirement neither established nor refuted |
| INFOS (sufficiency) | yes: all 2,048 inconsistent | clash (d) | **CLASH, board versus M, M's to rule** |
| ZERO (H-ZERO) | **no** (0 / 3,072) | none on any obstruction (its result, the zero is free, touches none) | **UNTESTED-BY-SCREEN**. *Wave 2 first said* "kept: OPEN pathway" via N_EQUIL |
| NULL (H-NULL) | **no** (0 / 3,072) | none (EGJ has no null-information term) | **UNTESTED-BY-SCREEN**. *Wave 2 first said* "kept: OPEN pathway" |
| RI (R-INDEX) | yes: 512 | with ITB an alternative NOT-BOUND-IF support {ITB, RI; N_MEASPHYS} | kept (never needed) |
| RQ (R-QUANTUM) | yes: 1,536 | O-HOLD OPEN via N_XI, N_QEIC; undoes ITB's non-binding | kept: OPEN pathway |

**Load-bearing** (in some support): W2, F1, F2b, ITB, ITE and RI at 1 ly; plus H12 at 1 AU, N = 7. **Named premises
ever used:** N_CORR, N_DCTC, N_EPS, N_FRW, N_KEYING, N_MEASPHYS, N_MS17, N_QTOPO, N_SIGKEY; plus N_H12W at 1 AU.

## 6. Every combination (127, plus readings only)

Generated by `python3 combine.py --table PATH` from the 1 ly, N = 7 screen. For each combination the best consistent
variant and **one account** (premises dropped named) are shown: first by member-attributed removals, then by
not-bound, then by removed-or-not-bound. Codes per form: **Rm** removed by a member; **Rg** removed with no member
(geometry / board / premise); **NBm** not-bound, member-attributed; OPEN; **S** silent; **L** left (S and L are read
off the union of accounts; in the D-CTC account the CTC is itself a loop). **"Adds nothing"** names members of the
best variant that are in no support of a member-attributed result — the row then adds nothing for them. The last
column is the 1 AU, N = 7 re-screen of the combination's W2 variants.

| # | combination | variants | consistent | clash (literals in core) | premise clashes | best variant (one account) | BITS/TOPO/DIST/HOLD/MATTER/LOOP-C/LOOP-S | member-attributed removals | NOT-BOUND-IF | removed with no member (geometry / board / premise) | load-bearing members; adds nothing | joint / independent variants | 1 AU, N = 7: W2 variants with O-BITS member-removed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IT | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB | 0 / 0 | - |
| 2 | SET | 12 | 12 | - | - | W2 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2 | 0 / 0 | 0/4 |
| 3 | FR | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b | 0 / 0 | - |
| 4 | 12 | 4 | 4 | - | - | H12 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12 | 0 / 0 | - |
| 5 | INF | 8 | 4 | INFOS | - | INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO | 0 / 0 | - |
| 6 | ZER | 4 | 4 | - | - | ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: ZERO | 0 / 0 | - |
| 7 | NUL | 4 | 4 | - | - | NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: NULL | 0 / 0 | - |
| 8 | IT+SET | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2 | 0 / 0 | 0/12 |
| 9 | IT+FR | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB | 0 / 8 | - |
| 10 | IT+12 | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12 (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12 | 0 / 0 | - |
| 11 | IT+INF | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO | 0 / 0 | - |
| 12 | IT+ZER | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: ZERO | 0 / 0 | - |
| 13 | IT+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: NULL | 0 / 0 | - |
| 14 | SET+FR | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1 | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1 | 4 / 0 | 8/12 |
| 15 | SET+12 | 12 | 12 | - | - | W2,H12 | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12 | 0 / 0 | 0/4 |
| 16 | SET+INF | 24 | 12 | INFOS | - | W2,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO | 0 / 0 | 0/8 |
| 17 | SET+ZER | 12 | 12 | - | - | W2,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,ZERO | 0 / 0 | 0/4 |
| 18 | SET+NUL | 12 | 12 | - | - | W2,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,NULL | 0 / 0 | 0/4 |
| 19 | FR+12 | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12 (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12 | 0 / 0 | - |
| 20 | FR+INF | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO | 0 / 0 | - |
| 21 | FR+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: ZERO | 0 / 0 | - |
| 22 | FR+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: NULL | 0 / 0 | - |
| 23 | 12+INF | 8 | 4 | INFOS | - | H12,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO | 0 / 0 | - |
| 24 | 12+ZER | 4 | 4 | - | - | H12,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,ZERO | 0 / 0 | - |
| 25 | 12+NUL | 4 | 4 | - | - | H12,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,NULL | 0 / 0 | - |
| 26 | INF+ZER | 8 | 4 | INFOS | - | INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,ZERO | 0 / 0 | - |
| 27 | INF+NUL | 8 | 4 | INFOS | - | INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,NULL | 0 / 0 | - |
| 28 | ZER+NUL | 4 | 4 | - | - | ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: ZERO,NULL | 0 / 0 | - |
| 29 | IT+SET+FR | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB | 8 / 20 | 16/36 |
| 30 | IT+SET+12 | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12 (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12 | 0 / 0 | 0/12 |
| 31 | IT+SET+INF | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO | 0 / 0 | 0/24 |
| 32 | IT+SET+ZER | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,ZERO | 0 / 0 | 0/12 |
| 33 | IT+SET+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,NULL | 0 / 0 | 0/12 |
| 34 | IT+FR+12 | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12 (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12 | 0 / 8 | - |
| 35 | IT+FR+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO | 0 / 8 | - |
| 36 | IT+FR+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: ZERO | 0 / 8 | - |
| 37 | IT+FR+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: NULL | 0 / 8 | - |
| 38 | IT+12+INF | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO | 0 / 0 | - |
| 39 | IT+12+ZER | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,ZERO | 0 / 0 | - |
| 40 | IT+12+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,NULL | 0 / 0 | - |
| 41 | IT+INF+ZER | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,ZERO | 0 / 0 | - |
| 42 | IT+INF+NUL | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,NULL | 0 / 0 | - |
| 43 | IT+ZER+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: ZERO,NULL | 0 / 0 | - |
| 44 | SET+FR+12 | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12 | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12 | 4 / 0 | 12/12 |
| 45 | SET+FR+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO | 4 / 0 | 8/24 |
| 46 | SET+FR+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: ZERO | 4 / 0 | 8/12 |
| 47 | SET+FR+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: NULL | 4 / 0 | 8/12 |
| 48 | SET+12+INF | 24 | 12 | INFOS | - | W2,H12,INFO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO | 0 / 0 | 0/8 |
| 49 | SET+12+ZER | 12 | 12 | - | - | W2,H12,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,ZERO | 0 / 0 | 0/4 |
| 50 | SET+12+NUL | 12 | 12 | - | - | W2,H12,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,NULL | 0 / 0 | 0/4 |
| 51 | SET+INF+ZER | 24 | 12 | INFOS | - | W2,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,ZERO | 0 / 0 | 0/8 |
| 52 | SET+INF+NUL | 24 | 12 | INFOS | - | W2,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,NULL | 0 / 0 | 0/8 |
| 53 | SET+ZER+NUL | 12 | 12 | - | - | W2,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,ZERO,NULL | 0 / 0 | 0/4 |
| 54 | FR+12+INF | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO | 0 / 0 | - |
| 55 | FR+12+ZER | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,ZERO | 0 / 0 | - |
| 56 | FR+12+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,NULL | 0 / 0 | - |
| 57 | FR+INF+ZER | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,ZERO | 0 / 0 | - |
| 58 | FR+INF+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,NULL | 0 / 0 | - |
| 59 | FR+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: ZERO,NULL | 0 / 0 | - |
| 60 | 12+INF+ZER | 8 | 4 | INFOS | - | H12,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 61 | 12+INF+NUL | 8 | 4 | INFOS | - | H12,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 62 | 12+ZER+NUL | 4 | 4 | - | - | H12,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 63 | INF+ZER+NUL | 8 | 4 | INFOS | - | INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 64 | IT+SET+FR+12 | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12 (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12 | 8 / 20 | 24/36 |
| 65 | IT+SET+FR+INF | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO | 8 / 20 | 16/72 |
| 66 | IT+SET+FR+ZER | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: ZERO | 8 / 20 | 16/36 |
| 67 | IT+SET+FR+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: NULL | 8 / 20 | 16/36 |
| 68 | IT+SET+12+INF | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO | 0 / 0 | 0/24 |
| 69 | IT+SET+12+ZER | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,ZERO | 0 / 0 | 0/12 |
| 70 | IT+SET+12+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,NULL | 0 / 0 | 0/12 |
| 71 | IT+SET+INF+ZER | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,ZERO | 0 / 0 | 0/24 |
| 72 | IT+SET+INF+NUL | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,NULL | 0 / 0 | 0/24 |
| 73 | IT+SET+ZER+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,ZERO,NULL | 0 / 0 | 0/12 |
| 74 | IT+FR+12+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO | 0 / 8 | - |
| 75 | IT+FR+12+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,ZERO | 0 / 8 | - |
| 76 | IT+FR+12+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,NULL | 0 / 8 | - |
| 77 | IT+FR+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,ZERO | 0 / 8 | - |
| 78 | IT+FR+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,NULL | 0 / 8 | - |
| 79 | IT+FR+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: ZERO,NULL | 0 / 8 | - |
| 80 | IT+12+INF+ZER | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 81 | IT+12+INF+NUL | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 82 | IT+12+ZER+NUL | 12 | 12 | - | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 83 | IT+INF+ZER+NUL | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 84 | SET+FR+12+INF | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO | 4 / 0 | 12/24 |
| 85 | SET+FR+12+ZER | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,ZERO | 4 / 0 | 12/12 |
| 86 | SET+FR+12+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,NULL | 4 / 0 | 12/12 |
| 87 | SET+FR+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,ZERO | 4 / 0 | 8/24 |
| 88 | SET+FR+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,NULL | 4 / 0 | 8/24 |
| 89 | SET+FR+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: ZERO,NULL | 4 / 0 | 8/12 |
| 90 | SET+12+INF+ZER | 24 | 12 | INFOS | - | W2,H12,INFO,ZERO | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,ZERO | 0 / 0 | 0/8 |
| 91 | SET+12+INF+NUL | 24 | 12 | INFOS | - | W2,H12,INFO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,NULL | 0 / 0 | 0/8 |
| 92 | SET+12+ZER+NUL | 12 | 12 | - | - | W2,H12,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,ZERO,NULL | 0 / 0 | 0/4 |
| 93 | SET+INF+ZER+NUL | 24 | 12 | INFOS | - | W2,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,INFO,ZERO,NULL | 0 / 0 | 0/8 |
| 94 | FR+12+INF+ZER | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,ZERO (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,ZERO | 0 / 0 | - |
| 95 | FR+12+INF+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,NULL | 0 / 0 | - |
| 96 | FR+12+ZER+NUL | 12 | 12 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,ZERO,NULL | 0 / 0 | - |
| 97 | FR+INF+ZER+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,INFO,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: INFO,ZERO,NULL | 0 / 0 | - |
| 98 | 12+INF+ZER+NUL | 8 | 4 | INFOS | - | H12,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 99 | IT+SET+FR+12+INF | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO | 8 / 20 | 24/72 |
| 100 | IT+SET+FR+12+ZER | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,ZERO | 8 / 20 | 24/36 |
| 101 | IT+SET+FR+12+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,NULL | 8 / 20 | 24/36 |
| 102 | IT+SET+FR+INF+ZER | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,ZERO | 8 / 20 | 16/72 |
| 103 | IT+SET+FR+INF+NUL | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,NULL | 8 / 20 | 16/72 |
| 104 | IT+SET+FR+ZER+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: ZERO,NULL | 8 / 20 | 16/36 |
| 105 | IT+SET+12+INF+ZER | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,ZERO (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,ZERO | 0 / 0 | 0/24 |
| 106 | IT+SET+12+INF+NUL | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,NULL | 0 / 0 | 0/24 |
| 107 | IT+SET+12+ZER+NUL | 36 | 32 | W2+ITE | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,ZERO,NULL | 0 / 0 | 0/12 |
| 108 | IT+SET+INF+ZER+NUL | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,INFO,ZERO,NULL | 0 / 0 | 0/24 |
| 109 | IT+FR+12+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,ZERO (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,ZERO | 0 / 8 | - |
| 110 | IT+FR+12+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,NULL | 0 / 8 | - |
| 111 | IT+FR+12+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,ZERO,NULL | 0 / 8 | - |
| 112 | IT+FR+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,INFO,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: INFO,ZERO,NULL | 0 / 8 | - |
| 113 | IT+12+INF+ZER+NUL | 24 | 12 | INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 114 | SET+FR+12+INF+ZER | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,ZERO | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,ZERO | 4 / 0 | 12/24 |
| 115 | SET+FR+12+INF+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,NULL | 4 / 0 | 12/24 |
| 116 | SET+FR+12+ZER+NUL | 36 | 36 | - | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,ZERO,NULL | 4 / 0 | 12/12 |
| 117 | SET+FR+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,INFO,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: INFO,ZERO,NULL | 4 / 0 | 8/24 |
| 118 | SET+12+INF+ZER+NUL | 24 | 12 | INFOS | - | W2,H12,INFO,ZERO,NULL | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: W2,H12,INFO,ZERO,NULL | 0 / 0 | 0/8 |
| 119 | FR+12+INF+ZER+NUL | 24 | 12 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | F2b,H12,INFO,ZERO,NULL (dropped N_FRW) | Rm/L/OPEN/L/L/S/S | BITS | - | - | F2b; adds nothing: H12,INFO,ZERO,NULL | 0 / 0 | - |
| 120 | IT+SET+FR+12+INF+ZER | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,ZERO (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,ZERO | 8 / 20 | 24/72 |
| 121 | IT+SET+FR+12+INF+NUL | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,NULL | 8 / 20 | 24/72 |
| 122 | IT+SET+FR+12+ZER+NUL | 108 | 96 | W2+F1+F2b+ITE; W2+F1+ITE; W2+F2b+ITE | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,ZERO,NULL | 8 / 20 | 24/36 |
| 123 | IT+SET+FR+INF+ZER+NUL | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,INFO,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: INFO,ZERO,NULL | 8 / 20 | 16/72 |
| 124 | IT+SET+12+INF+ZER+NUL | 72 | 32 | INFOS; W2+ITE; W2+ITE+INFOS | {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_MEASPHYS}; {N_QTOPO} | W2,ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | L/NBm/OPEN/NBm/L/NBm/Rg | none | HOLD,LOOP | - | ITB; adds nothing: W2,H12,INFO,ZERO,NULL | 0 / 0 | 0/24 |
| 125 | IT+FR+12+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | F2b,ITB,H12,INFO,ZERO,NULL (dropped N_CORR, N_FRW) | Rm/NBm/OPEN/NBm/L/NBm/S | BITS | HOLD | - | F2b,ITB; adds nothing: H12,INFO,ZERO,NULL | 0 / 8 | - |
| 126 | SET+FR+12+INF+ZER+NUL | 72 | 36 | INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_DCTC,N_FRW} | W2,F1,H12,INFO,ZERO,NULL | Rm/L/OPEN/L/L/Rg/Rg | BITS | - | LOOP | W2,F1; adds nothing: H12,INFO,ZERO,NULL | 4 / 0 | 12/24 |
| 127 | IT+SET+FR+12+INF+ZER+NUL | 216 | 96 | INFOS; W2+F1+F2b+ITE; W2+F1+F2b+ITE+INFOS; W2+F1+ITE; W2+F1+ITE+INFOS; W2+F2b+ITE; W2+F2b+ITE+INFOS | {N_2BVIA,N_FRW}; {N_2BVIA,N_KEYING}; {N_CORR,N_MEASPHYS}; {N_CORR,N_QTOPO}; {N_DCTC,N_FRW}; {N_DCTC}; {N_MEASPHYS}; {N_QTOPO} | W2,F1,ITB,H12,INFO,ZERO,NULL (dropped N_CORR) | Rm/NBm/OPEN/NBm/L/NBm/Rg | BITS | HOLD,LOOP | - | W2,F1,ITB; adds nothing: H12,INFO,ZERO,NULL | 8 / 20 | 24/72 |
| 128 | (readings only) | 3 | 3 | - | - | RI | L/L/OPEN/L/L/Rg/Rg | none | - | LOOP | none; adds nothing: RI | 0 / 0 | - |

## 7. Not tested by instrument, with the reason (no silent caps)

Every variant is screened. At 1 ly, N = 7, the **192 JOINT variants** are covered by T-A, T-B, T-E; the other 5,951 are
not tested by instrument:

| reason (1 ly, N = 7) | variants |
|---|---|
| INCONSISTENT: clash (c) or (d); nothing to test | 2,304 |
| SINGLE CONTRIBUTOR: one member's result covers the variant's; graded in that member's report | 2,560 |
| NO MEMBER CONTRIBUTION: anything removed is the geometry's, the board's or a premise's | 639 |
| INDEPENDENT: two or more single-member results, none joint; each graded in its member's report | 448 |

At 1 AU, N = 7 (1,536 W2 variants): 96 JOINT (T-G with T-A, T-B, T-E); 768 inconsistent, 448 single contributor, 160
no member contribution, 64 independent. The variant-by-variant list comes from `python3 combine.py --json PATH`.

## 8. Named hypotheses

**Conditional named premises** (assumed only inside a support; every support listed):

- **N_EPS** — removal premise ε > ε_any(L, N) for nlcontrol's Hamiltonian, carrying R_W2's H-COHERE,
  H-NLCONTROL-FORM, H-BORN-AT-BOB and H-BLOCK; tied to the cell by B-EPSWIN under the window set W_W2 (E-WIN).
- **N_DCTC** (new) — a CTC at Bob, H-DCTC, H-DCTC-CONVENTION C2, H-DCTC-SELECT. A CTC is not shown to exist.
- **N_SIGKEY** (H-SIG-COR); **N_CORR** (H-CORRIDOR-MODEL, a Lorentzian quotient); **N_KEYING** (H-KEYING, the
  docket's); **N_FRW** (H-FRW-EXACT + H-NOT-DE-SITTER; also excludes CTCs); **N_2BVIA** (H-2B-VIA-CORRIDOR).
- **N_QTOPO** — ITB's corridor is not a classical Lorentzian object. **No READ source.**
- **N_MS17** — MS p.17, READ; a non-traversable bridge only.
- **N_MEASPHYS** (H-MEASURE-PHYSICAL) — no source. **N_H12W** (H-12-CARRIER + H-12-W) — no READ model.
- *Withdrawn:* **N_FRAME3b** (presupposes F1); H-SLICE-INTRINSIC named, not credited.

**OPEN pathways** (never assumed in a removal): **N_XI** (ξ > 0); **N_QEIC** (new: outside {H_flat, H-PATH,
H-MIN-SCALAR}; curved-space QEIs NAMED-NOT-READ); **N_EPSG** (KR pp.13-14); **N_VAC** (Reznik READ; the window
0.91 L/c < T < L/c DERIVED-FROM-READ); **N_EQUIL** (EGJ out of equilibrium, ITJ's); **N_ILFREE** (no source).

**Encoding choices, named:** W2 is C2; without a preferred slicing C2 defines no channel. The window premises are held
fixed (**E-WIN**). O-MAKE and O-LOOP are each split in two. A CTC releases only Geroch's compact case (O-MAKE-TOPO stays
bound). Under ITE, MS fn.1 commits the bridge non-traversable; under ITJ the throat is geometric. R-INDEX releases
nothing without H-IT. A corridor network is present in every variant. Absences are part of the variant (closed world).
**Carried through unchanged:** A1's §2 list (incl. H-BLOCK, H-QUBIT-DRIFT, H-EXTEND); A2's H-CMB-IS-COSMIC and
H-KILLING-SEARCH; A3's H-ALT, H-FAITHFUL and H-R; A4's H-QUDIT, H-ER=EPR, H-PATH, H_flat and H-MIN-SCALAR.

## 9. Sources

| source | status | used for |
|---|---|---|
| Maldacena & Susskind, arXiv:1306.0533v2 | READ (wave 1) | fn.1 p.2; §3.1 p.16; §3.2 pp.16-17; p.17 (N_MS17); §5.4 pp.36-37 |
| Reznik, arXiv:quant-ph/0212044v2 | READ (wave 1) | p.1; p.10; p.12 Fig. 2; N_VAC |
| Eling-Guedens-Jacobson, gr-qc/0602001v1; Jacobson gr-qc/9504004v2 | READ by A4 | N_EQUIL, ITJ |
| Brun-Harrington-Wilde, arXiv:0811.1209v2 | READ by A2 (pp.1-4 re-READ in wave 3) | N_DCTC, via `frame.four_basis_c2_table` and `bb84_c2_table` |
| Hsu, arXiv:2511.15935v1 | READ by A1 (wave 3) | N_FRAME3b withdrawn: H-FRAME3b presupposes F1 |
| `LEDGER.md` lines 50, 67, 70, 181 | READ this pass, never written | B-RECV's conditions beside clash (d) |
| the four A-reports and their instruments (wave 3) | imported and re-run | every ground; each READ citation is the owning A-report's |
| `transit.py`, `emtension.py` | read, never written | B-RECV, B-LOCC, C-ITE |

No arXiv source was re-read in this stage (no alphaXiv call was needed: every figure cited is computed by an imported
instrument or READ by its owning A-report). No host refused a request.

## 10. Findings (recorded, not repaired)

1. **At most one obstruction is removed by the hypotheses themselves, in any consistent variant and account, and it is
   O-BITS** — by W2 × F1 (JOINT, conditional on R_W2, at 1 ly, N = 7 and at 1 AU, N = 10⁶; at 1 AU, N ≤ 10³ only with
   H12 + N_H12W) or by clause 2b's D-CTC (conditional on N_DCTC, at any distance, O-LOOP reintroduced). *Wave 2 first
   said* "the most is three"; *wave 1* "four of the six-way split, with O-HOLD REMOVED".
2. **H-SETTLE alone removes nothing**: the drift needs H-FRAME's slicing. *Wave 2 first said* {W2} alone O-BITS
   REMOVED-IF {W2; N_EPS, N_FRAME3b}.
3. **O-HOLD, O-MAKE-TOPO and the corridor form of O-LOOP are at most NOT-BOUND-IF**, under ITB + N_QTOPO (no READ
   source); what the non-geometric corridor costs is OPEN (N_ILFREE).
4. **O-LOOP's corridor removal is the geometry's** (exact FRW, N_CORR) and holds only in accounts without N_QTOPO; the
   two corridor accounts clash. Signal loops are removed by N_SIGKEY; the D-CTC reintroduces a loop.
5. **O-MATTER survives every consistent variant**: H-INFO's sufficiency reading would remove it and clashes with B-RECV
   in all 2,048 of its variants. B-RECV's conditions are listed beside the clash. M's to rule.
6. **O-MAKE-DIST survives every consistent variant** (OPEN via N_VAC only).
7. **H-ZERO, H-NULL and H-INFO's necessity reading are UNTESTED-BY-SCREEN** (they change nothing in 3,072, 3,072 and
   2,048 variants). *Wave 2 first said* ZERO and NULL were exercised through N_EQUIL.
8. **H-FRAME's two clauses do not contradict each other as M states them**; exact FRW excludes clause 2b's corridor
   route and its D-CTC (a global time function admits no CTC).
9. **ER=EPR with W2 is INCONSISTENT-AS-ENCODED**, and ER=EPR's linearity also excludes the D-CTC channel.
10. **The first transit can beat light with a midpoint source**, conditionally (N_EPS at the unread limit, H-C2, F1,
    H-BLOCK): 0.50153 yr after the source fires, against light's 1 yr. One-end distribution cannot.
11. **Interference exists**: clause 2b undoes the corridor loop removal; R-QUANTUM undoes ITB's non-binding; ITE undoes
    the D-CTC.
12. **Two disagreements with the A-reports remain, both explained**: A2's partial non-binding of O-MAKE (vocabulary)
    and A3's missing corridor NOT-BOUND-IF on O-LOOP (an A3 omission, open for A3's stage).

## 11. Testable predictions

- **{W2, F1}.** Bob's mean σ_y shifts by tanh(2ε(T − t_A)), t_A Alice's measurement time in the preferred slicing:
  0.537, 0.291 or 0 for t_A at the start, middle or end of his window (ε = 0.1, T = 3), under H-C2 and its no-branch
  rule. Frames that order the events differently disagree, so the slicing is measurable through the signal.
- **W2 on partly entangled pairs (T-B).** The shift follows the shared entanglement: 0.240 at S = 0.53 bits, 0.042 at
  S = 0.13 bits, exactly 0 for product pairs.
- **Clause 2b's D-CTC.** None physical: it needs a CTC at Bob, not shown to exist.
- **ITB.** None READ: ITB has no model that predicts anything beyond linear QM's no-signalling.
- **Any complete holder** of the 70 kg definition at R = 1 m has gravitating energy of at least 33-379 J,
  count-dependent: a floor on O-MATTER's holder, not a price.

## 12. Open

- A3's R-INDEX grade lacks the corridor NOT-BOUND-IF on O-LOOP (explained disagreement above; A3's stage).
- A1's H-SETTLE-KR × H-12 row: in the screen its O-HOLD OPEN is KR's alone (N_EPSG), H12 not load-bearing there.
- The W2 class capacity without H-BORN-AT-BOB: OPEN (A1). H-EXTEND: derived, not computed.
- The window premises (E-WIN) are not screened: refusing H-TRANSFER without H-12 would widen the window (A1 §4b).
- N_QTOPO, N_MEASPHYS, N_H12W, N_ILFREE: no READ source. The Weinberg-family values: NAMED-NOT-READ.
- Clash (d): M's to rule.
