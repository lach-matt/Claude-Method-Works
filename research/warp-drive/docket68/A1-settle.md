# DOCKET 68 / A1-settle: H-SETTLE alone, H-12's carriers, and the collapse control

**Status: a work-item write-up, not seated.** Instrument: `settle.py` (`python3 settle.py --selftest`: 62/62 checks
pass, about 2 min; six of the 62 are printed STRUCTURAL -- they cannot fail by construction and are not counted -- so
**56/56 counted**, ten of them controls built to fail; *wave 3 first said* 57/57 with six STRUCTURAL and eight controls;
*wave 2 first said* 47/47 with two STRUCTURAL). It imports
`nlcontrol.py`, `corridors.py` and (wave 2) `frame.py`, and copies none of them. Every number here is computed in
`settle.py`, READ at the locator given, DERIVED-FROM-READ, or labelled NAMED-NOT-READ or OPEN. Short quotations only,
each with its page.

**Headline, member-attributed first (wave 3).** Alone, H-SETTLE-W removes nothing: the channel it supplies needs a
preferred slicing, which is H-FRAME clause 1's substance. The one member-attributed removal in this work item is
**O-BITS by H-SETTLE-W × H-FRAME**, with **two supports** (wave 4): (1) REMOVED-IF {N_EPS, H-C2, H-FRAME3b ⇐ F1,
H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK} -- nlcontrol's form, block-coded, every pair count a floor; or
(2) REMOVED-IF {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2} -- the computed zero-error ancilla
member, with neither H-BLOCK nor H-NLCONTROL-FORM. For support (1), whether ε lies in the window is a separate
question, settled by window premises (H-MAP, H-TRANSFER, H-SPIN, H-DILUTION and the NAMED-NOT-READ bound values). For
support (2) no window is computed: H-MAP is not established for its field, so the window is **unevaluated** -- neither
open nor excluded, and "not excluded" is not evidence. No NOT-BOUND-IF arises here. *Wave 3 first said* the removal
had the single support (1), which read as if block coding were necessary (V2-1 problem 2). In a separate geometry
column, corridor O-LOOP is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}, credited to no hypothesis.

## Wave 4 repair (R3-alone, 2026-10-03): the second pair of re-verifications

Two re-verifications (V2-0, AGAINST M; V2-1, FOR M; `wave1/REPAIR2-Q1S-RESULT.json`, key `result.verify`) left items
sited here. Each is applied, or answered with a computed or READ reason. Wave 3's forms are kept, marked *wave 3 first
said*.

| re-verification item | resolution |
|---|---|
| V2-0 problem 2 / V2-1 unresolved 2: the row "H-SETTLE-KR × H-12, with G as the carrier" credits O-HOLD OPEN via G to the pair; H-SETTLE-KR alone already carries it | **Applied.** The row now reads **adds nothing to H-SETTLE-KR alone**. The pathway (KR p.13; ε_G unconstrained, KR p.14) is KR's; naming G as a carrier adds no premise the pathway uses. The header's rule (every combination row says load-bearing or adds-nothing) now holds. |
| V2-1 problem 1: "1 pair per teleported qubit" presented as the W2 class's figure without H-QUBIT-DRIFT | **Applied, and computed.** `w2_ancilla_flow_k` (G21-G25) is the same construction with k axes (none antipodal) and an m-qubit ancilla, d = 2^(1+m). k = 4, 8, 16, 32 give χ = 2, 3, 4, 5 = log₂d − 1 bits per pair with zero error, i.e. **1, 2/3, 1/2 and 0.4 pairs per teleported qubit**. Curves stay disjoint (0.391, 0.337, 0.180, 0.117 rad against grid steps ≈ 0.0075); end fidelity 1 − O(1e-15). Controls fail as built to: antipodal axes give χ = 2, not 3, at k = 8 (curves collide, separation 0); a state-independent unitary gives 0. These reproduce the FOR verifier's scratch figures. **The class has no positive floor on pairs per qubit in the computed range**; the Holevo ceiling under H-BORN-AT-BOB is log₂d per pair (READ in A3). Two cautions keep this from over-reading: the separation shrinks with k, so H-EXTEND asks for a field that varies on ever finer scales (max‖H‖T stays 1.43-1.56); and none of it is evidence that such a drift exists. |
| V2-1 problem 2: W2 × F1's O-BITS removal given one support, R_W2, containing H-NLCONTROL-FORM and H-BLOCK | **Applied.** Two supports (headline, §5): R_W2, and **R_W2′ = {H-C2 (no-branch rule), H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2}**, where H-FIELD-W2 (the field strength max‖H‖T ≈ 1.43-1.56 is available within the drift time) replaces N_EPS. Support 2 is zero-error. No published bound maps onto it, because H-MAP is not established for this field, so its window is **unevaluated**. The grade word (PARTIAL; O-BITS REMOVED-IF) does not change. |
| V2-1 problem 3 / unresolved 3: at 1 AU with N ≤ 1e3, O-BITS without H-12 carried as LEFT, as if the window exclusion were settled | **Applied.** Those cells are **LEFT-IF W_W2**, and W_W2 contains an unread value (the NAMED-NOT-READ Majumder figure; §2: "Everything below therefore rests on the Majumder figure"). By M's rule an unread value makes the cell **OPEN**, pending a READ of the Weinberg-family values. The exclusion also holds only for nlcontrol's ε mapping; for support 2 no window is computed. The "H-12 synergy at 1 AU" now reads: H-12-CARRIER + H-12-W replaces H-TRANSFER in an exclusion that rests on an unread value. `settle.h12_carrier_case` still prints EXCLUDED for those cells: that label is the computation *given* W_W2, and it is kept so `combine.py`'s ground rows stay comparable. |
| V2-0 unresolved 4 (outside its lens, for the FOR side): 2511.15935v1 p.4 says the KR model fails Tomonaga-Schwinger integrability; A1 READ pp.1-3, 5 only | **READ this pass, p.4, and recorded.** "The TS integrability condition fails for generic states even though the KR model enforces retarded (causal) dependence": the overlap J⁻(x) ∩ J⁻(y) of two spacelike points is generically non-empty. That is foliation dependence. The paper shows no signal from it, and it is a single-author 2025 preprint deriving a necessary condition. Named **H-KR-TS**; whether the foliation dependence is operational (a signal, or a preferred slicing) is OPEN. KR alone still LEAVES O-BITS on its own §2.3 factorisation (DERIVED-FROM-READ); no grade moves. |
| V2-0 unresolved 3 / V2-1 unresolved 4: N_QTOPO, N_MEASPHYS, N_H12W, N_ILFREE have no READ source; the Weinberg-family values stay NAMED-NOT-READ; H-EXTEND is derived; the W2 capacity without H-BORN-AT-BOB is OPEN | **Answered: OPEN by design, unchanged.** Each verdict that rests on one of them names it (here: N_H12W in §4b, the Majumder value in §2 and §5, H-EXTEND in §1b and support 2). No READ source was found this pass either. |
| V2-0 problem 7 (D-CTC "exact") and the clause-2b cell | Sited in A2 and B. A1 §1b's D-CTC sentence already carries BHW 0811.1209v2 p.4, "unbounded if CTC qubits are treated as a free resource". |

## Wave 3 repair (2026-10-03): the two re-verifications

Two re-verifications (RV-0, AGAINST M; RV-1, FOR M; `wave1/REPAIR1-RESULT.json`, key `result.reverify`) left items
sited here. Each is applied, or answered with a computed or READ reason. Wave 2's forms are kept below, marked *wave 2
first said*.

| re-verification item | resolution |
|---|---|
| RV-0 #0: ε > ε_any and "7 per qubit" presented as the removal condition; they come from N·C ≥ 2, Shannon's converse | **Applied.** Every pair count from N·C ≥ 2 is a **floor**. `zero_error_table` (checks G14, G15, G15b) finds the zero-error capacity is 0 at D < 1 for both nlcontrol's Z-channel and H₂'s BSC: one codeword at block lengths 1-3. For the Z-channel it is 0 even at D = 1, since both inputs give '+'. Control: the BSC at D = 1 has 2, 4 and 8 words. So no finite N per qubit delivers the 2 bits with certainty. Reliable transfer is block-coded over many qubits at a rate below C, with error going to 0 only as the block length goes to infinity. That is named **H-BLOCK** and sits in the removal's support. "7 per qubit" now reads "≥ 7 (floor)". One premise set is used in A1, A2 and A3. |
| RV-0 #2 / RV-0 unresolved #3: H-FRAME3b is "clause 1's substance", yet {W2} alone was credited O-BITS | **Applied: H-FRAME3b presupposes F1.** A preferred slicing *is* "a preferred frame exists". Corroboration READ this pass: 2511.15935v1 (Hsu) pp.1-3. A Weinberg-type term keeps foliation independence only under microcausality, and microcausality "cannot be consistently maintained" under state-dependent evolution (p.2). So H-SETTLE-W alone **leaves** O-BITS, and the removal is W2 × F1's (or W2 × clause 2b's cosmic clock). No READ source or computation gives a slicing that a drift selects for itself without a preferred frame. If one did (name it H-SLICE-INTRINSIC), W2 alone would carry the channel. It is named so the grade says what it would take, and nothing is credited to it. |
| RV-0 #3, RV-1 #9 / RV-0 unresolved #0: O-LOOP credited to H-SETTLE-W alone, against A1's own H-12 row and against B | **Applied, uniformly.** Corridor O-LOOP is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}. The removal is **the geometry's, credited to no hypothesis**, and every row carries it in a separate column. W2 × F1 adds only signal keying: N_SIGKEY under H-SIG-COR. |
| RV-1 #2: {N_QTOPO, N_CORR} never named | **Applied.** In a combination with H-IT read as ITB under N_QTOPO, neither the FRW lemma nor latticectc's theorem binds an ITB corridor. Corridor O-LOOP is then **NOT-BOUND-IF {N_QTOPO}**, and loops made by signals are unchanged. {N_QTOPO, N_CORR} is a premise clash: one corridor, two accounts. |
| RV-0 #4, RV-1 #9: W2 × H-12 credits "O-HOLD (OPEN via G in KR form)" against its own H-12-W premise | **Applied.** In that row O-HOLD is LEFT. "OPEN via G" is re-sited to a new row, H-SETTLE-KR × H-12 with G as the carrier. |
| RV-0 #10: G6, G7, G8 and G12 cannot fail | **Applied.** G6a, G7, G8 and G12b are printed STRUCTURAL. G6b (3 pairs reach 2 bits) and G12a (the H-TRANSFER comparison) keep the content. The factor 2 and the distance-independence are stated as analytic consequences of T = atanh(D_N)/(2ε), not as checks. |
| RV-1 #0 / RV-1 unresolved #0: the W2 "class floor" rests on an unnamed premise, that the drift acts on Bob's qubit alone | **Applied, and computed.** The premise is named **H-QUBIT-DRIFT**. Under H-BORN-AT-BOB + H-QUBIT-DRIFT the floors stand: > 2 on average, ≥ 3 per qubit at finite T. Without H-QUBIT-DRIFT, `w2_ancilla_flow` (G18-G20) gives a W2 member that carries **2.000000 bits per pair with zero error at finite T**. The setup is the qubit plus a two-qubit ancilla in \|00⟩, four axes, and a field that depends only on the current state, built from H = i(vψ† − ψv†) (G16, control G17). That makes **1 pair per teleported qubit**. Smoothness of the global field is H-EXTEND, derived and not computed. This is not evidence that such a drift exists. *Wave 4: "1 pair" is the four-axis instance's figure, not the class's; with more axes and a larger ancilla the class has no positive floor (§1b, V2-1 problem 1).* |
| RV-1 #3: H-MAP, H-TRANSFER and H-SPIN listed as removal premises; four premise sets across reports | **Applied.** Removal premises and window premises are now separate columns, and one removal set is used everywhere. |
| RV-1 #8: 1 AU statements without their N | **Applied.** Each 1 AU statement now carries its N. At 1 AU with N = 1e6, ε_any = 3.34e-6 /s is not excluded even under H-TRANSFER. The H-12 flips are specific to N = 7 and N = 1000. |
| RV-0 unresolved #4: the Weinberg-family bounds remain NAMED-NOT-READ | **Answered.** Two further arXiv papers were READ this pass for a restatement carrying the 1989-90 numbers: 2509.04320v1 pp.1-2, 12, 16 and 2511.15935v1 pp.1-3, 5. Neither carries them. The PRLs predate arXiv, so the values stay NAMED-NOT-READ and every number derived from them stays conditional. |

## Wave 2 repair (2026-10-03): what changed, and why

Three adversarial verifications (AGAINST M, FOR M, REPRODUCE; `wave1/WAVE1-RESULT.json`) raised problems sited in this
work item. Each is resolved below, either applied or answered with the computed or READ reason it does not hold.
Wave 1's first forms are kept in place, marked *wave 1 first said*.

| verifier problem | resolution |
|---|---|
| REPRODUCE #0: the O-BITS removal names no hypothesis about WHICH state the drift acts on | **Applied.** H-C2 (the drift acts on Bob's per-branch pure state) is named on every signal. Under C1 (his reduced state) the signal is 2.2e-16 (`frame.settle_under_C1`, re-run in check G1): no channel. 2412.20854v1 pp.4, 7 (re-READ this pass): Gisin's theorem covers local maps on pure states only, and nonlinear maps defined on mixed states can be non-signalling (their refs [40, 41]). |
| REPRODUCE #3: 'might be premature' cited at p.25 | **Applied.** It is on p.26 (re-READ this pass). |
| AGAINST #15: D6 is vacuous | **Applied.** D6 now runs the drift through `sde_ensemble` with λ = 0 and must reproduce tanh(2εT) (0.94698 against 0.94681). Wave 1's D6 fed a hand-typed vector to the detector. |
| AGAINST #16 / FOR #7: H-SETTLE × H-12 adds no removal / H-12 is load-bearing with an unbounded carrier | **Both hold, under different hypotheses, and both are computed** (§4b). Under H-TRANSFER, H-12 adds nothing. Under H-12-CARRIER + H-12-W (the carrier is α_s, G or v, with no state-dependent bound READ anywhere), 2 of the 9 tabulated (L, N) cells flip from EXCLUDED to NOT EXCLUDED, both at 1 AU (N = 7 and N = 1000; wave 3 adds the N). "Not excluded" is still not evidence. |
| FOR #9: O-LOOP keying is forced by exact FRW | **Applied.** H-SETTLE-W alone now has O-LOOP REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, N_SIGKEY}. The ground is `frame.frw_time_function_lemma` (z3 unsat, re-run in check G13). Wave 1 first said it *leaves* O-LOOP. *Superseded in wave 3:* the removal is the geometry's, credited to no hypothesis (RV-0 #3). |
| FOR #2: 6.21 pairs and Holevo's 1 bit are carried as properties of W2 | **Applied, and computed further** (§1b). 6.21 belongs to nlcontrol's single Hamiltonian (H-NLCONTROL-FORM). A second W2 Hamiltonian reaches 1 bit per pair. Under H-BORN-AT-BOB no per-branch drift on a qubit exceeds 1 bit per pair, and none reaches it at finite T. So the class needs more than 2 pairs per teleported qubit (at least 3 at finite T). Without H-BORN-AT-BOB the class capacity is OPEN. *Corrected in wave 3:* that floor holds for the qubit-only subclass (H-QUBIT-DRIFT), not for the class (RV-1 #0). |
| FOR #3: the T = L/2c table is an arbitrary choice; drift time is distance-independent | **Applied** (§2). The drift time is T = atanh(D_N)/(2ε). The ε needed for *any* advantage is exactly half the wave-1 figure, at every row. No excluded/not-excluded entry flips. |
| FOR #4: first transit with a midpoint source | **Applied** (§2, first transit), using LEDGER D23 as corrected in DOCKET 67. |
| AGAINST #13 (sited in combine): W2's O-BITS removal silently includes a preferred slicing | **Applied here too.** H-SETTLE-W's O-BITS removal carries H-FRAME3b, which is H-FRAME clause 1's substance (a preferred slicing). "H-SETTLE alone removes O-BITS" means "with a preferred slicing built in". *Superseded in wave 3:* H-FRAME3b presupposes F1, so the removal is W2 × F1's (RV-0 #2). |

M's hypothesis, carried as M stated it: **quantum easing / quantum settling is deterministic drift**, "the state's own
value steers its evolution, smoothly and the same every time" (CHARTER). It is graded on what it does. Whether it is
fashionable does not enter the grade.

## 1. The signal at Bob: an exact law

For nlcontrol's drift H = ε⟨X⟩Z, the Bloch vector rotates about z at a rate set by its own x component:
ẋ = −2εxy, ẏ = 2εx². The perpendicular length ρ⊥ is conserved, and φ̇ = 2ερ⊥cos φ. Its solution is
φ = gd(2ερ⊥t + gd⁻¹φ₀), checked symbolically with sympy (residual 0). This gives

* **Bob's ⟨σ_y⟩ = tanh(2εT) when Alice measures x, and exactly 0 when she measures z.** In general,
  y(T) = ρ⊥ tanh(atanh(y₀/ρ⊥) + 2ερ⊥T). x keeps its sign and z is constant. Against nlcontrol's own integrator the
  closed form agrees to 1.6e-5 on 12 random states.
* nlcontrol's printed numbers are its integrator's output: 0.00600, 0.05993, 0.53706. The exact values are 0.0059999,
  0.0599281 and 0.5370496. The 0.53706 sits +1.0e-5 above the exact value. That comes from the first-order
  frozen-H step, so it is a discrepancy in the last digit and changes no conclusion. A wrong law, tanh(εT), is caught
  by the same comparison (control A4). The linear control H = εZ gives exactly 0.
* Searching every measurement axis Alice could use finds the largest Bob-side displacement on the **x axis**, equal to
  tanh(2εT). The z and y axes give 0. Bob's mean y is ≥ 0 for every axis, because
  tanh u + tanh v = sinh(u+v)/(cosh u cosh v). So this drift offers no antipodal letter.

**What it is worth, for THIS Hamiltonian (H-NLCONTROL-FORM).** The channel is: Alice picks x or z, Bob measures
σ_y. It carries I = D²/(8 ln 2) bits per pair for small D, with D = tanh(2εT). The capacity tends to log₂1.25 =
**0.3219 bits/pair** as D → 1 (a Z-channel with crossover ½). The Holevo χ equals the measured mutual information,
because the two states commute. One teleported qubit needs 2 bits, so by Shannon's converse it needs **at least 6.21
pairs on average** and **at least 7** if each qubit is coded alone. **Both are floors.** This Z-channel's zero-error
capacity is 0 at every D, because both of Alice's inputs give Bob a '+' with positive probability (`zero_error_table`,
G15b). So no finite number of pairs per qubit delivers the 2 bits with certainty. Reliable transfer is block-coded over
many teleported qubits at a rate below C, with error, and so teleportation infidelity, going to 0 only as the block
length goes to infinity (**H-BLOCK**). All of this is conditional on H-C2. *Wave 2 first said* "at least 6.21 pairs on
average (block coding over many qubits), or 7 if each qubit is coded alone", which read the floor as sufficient.

*Wave 1 first said:* "at least 6.21 pairs with this protocol. Holevo's bound caps any qubit protocol at 1 bit per pair,
so any protocol needs at least 2 pairs (Holevo is NAMED-NOT-READ here)". Three things in that sentence were wrong:
- 6.21 was carried downstream (by B-combine) as H-SETTLE's figure, and it is not;
- Holevo's bound is READ in A3 (quant-ph/9611023v1 pp.2-3);
- Holevo is a theorem of *linear* QM, so it binds only Bob's final Born-rule readout (H-BORN-AT-BOB), not the drift.

### 1b. The W2 class, not one Hamiltonian (wave 2, computed)

- **A second member of the class.** H₂ = ε(⟨X⟩Z + ⟨Z⟩X) is deterministic, acts per branch, and is steered by the
  state's own value. Its Z term pulls Alice's x-branch states ±x to +y, which is nlcontrol's law. Its X term pulls
  her z-branch states ±z to −y.
  - Bob's σ_y difference is 2 tanh(2εT). The integrator gives 1.074111 at ε = 0.1, T = 3, against the exact 1.074099.
  - The channel is binary symmetric. Its capacity is 1 − h₂((1 − D)/2): 0.7136 at D = 0.9, 0.9546 at D = 0.99, and
    0.99999 at D = 0.999999.
- **The ceiling under H-BORN-AT-BOB + H-QUBIT-DRIFT (the qubit-only subclass).** If the drift acts on Bob's received
  qubit alone, his readout is a Born measurement of one qubit, so χ ≤ log₂2 = 1 bit. This holds however many
  settings Alice has. The arithmetic was checked on 300 random ensembles of up to 8 choices: the largest χ was 0.812.
  *Wave 2 first said* "Under H-BORN-AT-BOB ... one qubit", silently adding H-QUBIT-DRIFT (RV-1 #0).
- **The ceiling is never reached at finite T.** A drift is a flow, and a flow is injective. Alice's two outcomes in
  one basis therefore stay distinct pure states, and their mixture has rank 2. Computed for H₂ at ε = 0.3, T = 3: the
  smallest eigenvalue is 2.7e-2 and the trace distance is 0.947, below 1.
- **Pairs per teleported qubit:**

| hypothesis | pairs per teleported qubit (all floors unless zero-error) |
|---|---|
| nlcontrol (H-NLCONTROL-FORM) | ≥ 6.21 on average (block-coded, H-BLOCK); ≥ 7 per qubit (floor; never zero-error) |
| qubit-only subclass (H-BORN-AT-BOB + H-QUBIT-DRIFT) | > 2 on average (2 is the infimum and is never attained); ≥ 3 per qubit at finite T (floor) |
| W2 under H-BORN-AT-BOB, without H-QUBIT-DRIFT, four axes (qubit + two-qubit ancilla; `w2_ancilla_flow`, H-EXTEND) | 1, zero-error at finite T (χ = 2.000000 bits per pair; P(b′\|b) = identity) -- **this instance only** |
| W2 under H-BORN-AT-BOB, without H-QUBIT-DRIFT, k axes and an m-qubit ancilla, d = 2^(1+m) (`w2_ancilla_flow_k`, H-EXTEND; wave 4) | **2/(log₂d − 1), zero-error**: 1, 2/3, 1/2, 0.4 at d = 8, 16, 32, 64 (χ = 2, 3, 4, 5). **No positive floor** in the computed range |
| W2 without H-BORN-AT-BOB | **OPEN** |

- **The member without H-QUBIT-DRIFT (wave 3, computed).** Bob's received qubit sits beside a two-qubit ancilla in
  \|00⟩, which does not depend on Alice. Alice measures along one of four axes, giving eight distinct branch states in
  C⁸. Each branch is carried along a Fubini-Study geodesic to one vector of an orthonormal basis.
  - The eight curves are disjoint as sets: minimum separation 0.395 rad, against a grid step of 0.0037. So one
    autonomous field, a function of the state alone, is single-valued on them.
  - On the curves the field is H(ψ) = i(vψ† − ψv†). It is Hermitian and generates v (checked on 50 random states in
    C⁸, residual 1.1e-15). Control: a v not orthogonal to ψ leaves a residual of 0.51.
  - Integrating each branch under H of its own current state reaches the targets with fidelity 1 − 1e-12.
  - Bob's Born readout identifies Alice's axis with certainty: 2 bits per pair, zero error, at max‖H‖·T = 1.465.
  - Control: one state-independent unitary for every branch gives χ = 0.
  - A smooth global field is **H-EXTEND**, derived from the curves' separation and not computed. H-MAP is not
    established for this field.
  - **This shows what the class admits. It is not evidence that such a drift exists.**
- *Wave 3 first said* the row above as "W2 under H-BORN-AT-BOB, without H-QUBIT-DRIFT ... **1, zero-error at finite
  T**", reading as the class's figure (V2-1 problem 1). The k-axis member is the same construction: 2k branch states
  carried to 2k orthonormal vectors in C^d, so Bob's Born readout identifies the axis (log₂k bits) and Alice's random
  outcome costs the remaining bit of the log₂d ceiling.
- Without H-BORN-AT-BOB, the D-CTC analogue under C2 carries 1.000 bit per pair through BHW's BB84 construction
  (`frame.bb84_c2_table`) and **2.000000 bits per pair over four axes** (`frame.four_basis_c2_table`, wave 3). Both
  are computed and zero-error. BHW 0811.1209v2 p.4 (READ): unbounded "if CTC qubits are treated as a free resource".
  **W2's general capacity is OPEN.** *Wave 2 first said* "the four-basis figure ... not re-run".
- H₂ at 1 ly with N = 3 needs ε > 2.16e-8 /s for any advantage. That figure assumes H-MAP carries over to H₂, which
  has not been established, so it is illustration only.

## 2. The published bounds, by family, and what each permits at Bob

**The KR family: causal by construction.** All entries are READ. Kaplan and Rajendran (2106.10576v2) shift a bosonic
field by ε times its expectation value (eq. 4). For separated systems the evolution factorises into a unitary on x
times a unitary on y (§2.3, pp.7–8). A local operation on Alice's side therefore reaches Bob only through retarded
Green's functions. The bounds on |ε_γ|:

| bound | source |
|---|---|
| 1.15e-12 at 90% CL | 2411.09611v1 p.1, p.7 |
| 5.4e-12 (1 s.d.) | 2206.12976v1 p.1, p.5 |
| 4.7e-11 at 90% CL | 2204.11875v1 p.1, p.3 |
| ≲1e-5 from ion traps, ε > 0 only | 2106.10576v2 p.14 |

**Inverting these bounds into the largest superluminal signal at Bob gives 0, at every ε.** This is DERIVED-FROM-READ
(from KR's factorisation, §2.3). The experiments bound an inter-branch effect, the "Everett phone"
(2411.09611v1 p.2), which is not a channel from Alice to Bob. This family removes nothing from O-BITS.
Two discrepancies are recorded and neither is a refutation:
* 2411.09611 calls its result an improvement "by nearly a factor of 50" (p.1). The computed ratio
  4.7e-11/1.15e-12 is 40.87.
* KR v2 p.14 prints its Lamb-shift estimate as |ε_γ| ≲ 1e-4. Brož et al. restate it as ≲ 1e-2 (2206.12976v1 p.2, p.5).

**The Weinberg family: deterministic, local on pure states.** This is the family Gisin's theorem covers. It contains
nlcontrol's drift, and M's definition **read per branch (H-C2)**.

*Wave 1 first said* "It contains nlcontrol's drift and M's definition", naming no convention. M's words ("the state's
own value steers its evolution") do not say whether the state is Bob's branch pure state (C2) or his reduced density
matrix (C1). The two readings give different answers:
- Under C1 the drift gives 2.2e-16: no channel.
- 2412.20854v1 p.7 (re-READ): Gisin's argument is "limited to local dynamical maps acting on pure states only. It does
  not apply" to dynamics defined directly on mixed states, and refs [40, 41] give explicit nonlinear maps on mixed
  states that "bypass" it. p.4 says the same.
- 0908.3023v2 pp.3-4 (READ by A2) calls the per-branch argument the "linearity trap".

So every signal in this report is conditional on H-C2.

The 1989–90 spin experiments are PRLs that are not on arXiv:
* Majumder et al.: |ε|/2π ≤ 3.8 µHz.
* Walsworth et al.: 3.7e-20 eV, equal to 8.9 µHz. The check h × 8.9 µHz = 3.68e-20 eV is consistent. The abstract's
  text layer prints the exponent as "10^{20}", which is a discrepancy, not a refutation.

Both figures come from abstract metadata seen through a search index (PubMed ids 10042736 and 10041761). I found no
READ arXiv restatement that carries the numbers, so both are **NAMED-NOT-READ**. Bollinger et al. 1989 (⁹Be⁺) and
Chupp & Hoare 1990 (²¹Ne): **the values are OPEN**. Two further arXiv papers were READ in wave 3 for a restatement:
2509.04320v1 pp.1-2, 12, 16 and 2511.15935v1 pp.1-3, 5. Neither carries the numbers. Everything below therefore rests on
the Majumder figure and on two separate sets of named hypotheses (wave 3, RV-1 #3).

**Removal premises** (if these hold and ε exceeds ε_any(L, N), O-BITS is removed):
* N_EPS: ε > ε_any(L, N).
* H-C2: the drift acts on the branch state. Its rule, named in wave 3: before Alice measures in the chosen slicing
  there is no branch, so the drift acts on the reduced state. Under C1 there is no signal.
* H-FRAME3b ⇐ F1: the remote preparation happens on a fixed spacelike hypersurface. 2412.20854v1 p.6 calls this a
  "rather strong assumption" that needs "some preferred time-slicing". A preferred slicing is H-FRAME clause 1's
  substance, so this premise is supplied by F1 (wave 3, RV-0 #2).
* H-COHERE: Bob keeps coherence for the drift time.
* H-NLCONTROL-FORM: the drift is ε⟨X⟩Z. The capacity figures and ε_any below are this Hamiltonian's.
* H-BORN-AT-BOB: Bob's final readout is a Born measurement.
* H-BLOCK: the 2 bits are block-coded over many qubits. N·C ≥ 2 is a floor, and the zero-error capacity is 0.

**Window premises** (whether the unread bound excludes that ε; they bear on exclusion, not on the removal):
* H-MAP: the bounded shift is nlcontrol's 2ε. Reading A takes ε = 2πf, reading B takes ε = πf. Both are given.
* H-TRANSFER: a bound measured on a ²⁰¹Hg or H spin applies to Bob's carrier. When it fails the window *widens*
  (§4b: 2 of 9 cells flip). Listing it as a condition of the removal pointed it the wrong way, and *wave 2 first did*.
* H-SPIN: Weinberg's experiments used spins above ½. nlcontrol's term is not rotation-invariant; it belongs to the
  torsion class (2112.09005v3 eq. 99, and p.23: "frequency 2J₁x").
* H-DILUTION: KR p.13 says nonlinear effects can be diluted by cosmic history.
* **The bound values are NAMED-NOT-READ, and the bound is an upper limit measured consistent with zero.**

Conditional numbers. The table uses reading A, ε_max = 2.39e-5 s⁻¹; reading B halves ε.

| quantity | reading A | reading B |
|---|---|---|
| drift time to D = 0.5 | 3.20 h | 6.39 h |
| D at T = 1 s | 4.8e-5 | — |
| D at T = 1 h | 0.170 (5.3e-3 bits/pair) | — |
| D at T = 1 day | 0.9995 (0.320 bits/pair) | — |
| best rate per pair | 6.7e-6 bits/s, at T = 8.6 h | 3.4e-6 bits/s, at T = 17.2 h |

* Pairs for a 3σ detection at the limit, reading A: 3.9e9 at T = 1 s, 310 at T = 1 h.
* **The ε that removes O-BITS (wave 2; floors since wave 3).** One teleported qubit needs N·C ≥ 2 bits. That is
  Shannon's converse: necessary, not sufficient. With nlcontrol's Hamiltonian, N < 7 is impossible at any ε when each
  qubit is coded alone, and no N ≥ 7 is zero-error. So ε_any(L, N) is the floor on ε for block-coded transfer at
  average rate N pairs per qubit (H-BLOCK).
  - The drift time needed is **T = atanh(D_N)/(2ε), independent of distance**. The read precedes light whenever
    T < L/c.
  - So the condition is ε > ε_any(L, N), which is the ε at which T reaches L/c.
  - *Wave 1 first said* "Bob holds each pair for T = L/2c" and tabulated ε at that T. T = L/2c was a declared choice,
    and its ε is exactly twice ε_any at every row. That follows analytically from T = atanh(D_N)/(2ε). Check G7
    prints it as STRUCTURAL and it is not evidence; *wave 2 first cited* "check G7: ratio 2.000000" as evidence.

| distance | N = 7: ε_any (wave 1, at T = L/2c) | N = 1e3 | N = 1e6 | under H-TRANSFER, reading A |
|---|---|---|---|---|
| 1 AU | 2.30e-3 (4.6e-3) s⁻¹ | 1.06e-4 (2.1e-4) | 3.34e-6 (6.7e-6) | excluded, excluded, not excluded |
| 1 ly | 3.64e-8 (7.3e-8) s⁻¹ | 1.67e-9 (3.3e-9) | 5.28e-11 (1.1e-10) | not excluded ×3 |
| 4.24 ly (illustrative) | 8.60e-9 (1.7e-8) s⁻¹ | 3.94e-10 (7.9e-10) | 1.24e-11 (2.5e-11) | not excluded ×3 |

  No excluded/not-excluded entry flips between the two columns.
* **Timing at the NAMED-NOT-READ limit.** The drift times are:

| reading | N = 7 | N = 1000 |
|---|---|---|
| A | T = 13.38 h | T = 0.61 h |
| B | T = 26.76 h | T = 1.23 h |

  Once the pairs are in place, a transit at 1 ly with N = 7 reads 0.99847 L/c early under reading A (0.99695 under
  reading B).
* **The first transit (LEDGER D23, as corrected in DOCKET 67: "a midpoint source spans D at D/(2c)").** Times are
  counted from when the source fires. The pairs move at c, which is setup, not message latency.
  - **One-end source:** Bob holds his half from L/c, so the read comes at L/c + T, after light launched from Alice at
    the firing. It never beats light.
  - **Midpoint source:** both parties hold their halves from L/2c, so the read comes at L/2c + T (0.501526 yr at 1 ly,
    reading A, N = 7). That beats light launched from Alice's end at the firing whenever T < L/2c (check G10; control
    G11 with T > L/2c does not). Against light launched when Alice measures, the advantage is L/c − T, the same as for
    later transits.
  - *Wave 1 (via B-combine) first said* "the first cannot [beat light]". That holds only for one-end distribution.
  - The source, the pairs and the holder still arrive at ≤ c.
  - Every timing here is conditional on N_EPS, H-C2, H-FRAME3b ⇐ F1, H-NLCONTROL-FORM, H-BLOCK and the unread
    limit. N = 7 is a floor (block-coded).

  Read this table as: at interstellar distances **the unread upper limit does not exclude** a Weinberg-type drift strong
  enough to carry the two bits. It is **not** evidence that such a drift exists. A measurement consistent with zero
  says nothing in M's favour. A bound that does not exclude says nothing against.

## 3. The collapse-type (stochastic) control: it must not signal, and it does not

The model is the QMUPL-form stochastic Schrödinger equation (1204.4325v3 eq. 23, READ), with A = σ_x, H = 0.7σ_y,
λ = 1 and T = 2. Each trajectory is nonlinear and changes a great deal: |0⟩ ends with a per-trajectory ⟨|x|⟩ of 0.82,
against a Lindblad |x| of 0.18. This is the vacuity guard. The **ensemble** follows the linear Lindblad equation
(1204.4325v3 p.89, READ): Monte Carlo matches it within 2.5σ for all four initial states.
* The exact difference between Alice's two ensembles is 1.1e-16.
* The Monte Carlo detector reads 0.0042 ± 0.0077 (0.54σ): **no signal.**

**The control that must signal does, with the same detector.** Deterministic drift plus collapse noise (ε = 0.3,
λ = 0.2, T = 3) reads 0.259 ± 0.003, which is 93σ. Noise does not wash out a deterministic nonlinearity. What protects
causality is a linear ensemble map. Weinberg makes the same point (1109.6462v4 p.11): if the density matrix's evolution
depends on the ensemble, then "instantaneous communication between isolated systems would be possible".

*Recorded fault (wave 2), kept like fields12's.* Wave 1's D6 ("CONTROL (must signal): pure deterministic drift, same
detector") passed the detector a hand-typed vector (0, tanh 0.6, 0) with zero error. It returned ∞ whatever the drift
code did, so it tested the detector's arithmetic, not a drift (AGAINST #15). D5 (93σ) was always the real must-signal
control.
- D6 now runs the drift through `sde_ensemble` with λ = 0 and must reproduce tanh(2εT).
- Wave 1's C3 (two typed READ values differ) and E2 (counting the H-12 table's own labels) cannot fail by
  construction. They are now printed STRUCTURAL and are not cited as evidence.

*Recorded fault, kept like fields12's:* in a scratch prototype (not in settle.py) I tried a "non-martingale"
stochastic control: wrong drift coefficient, explicit renormalisation. It showed no signal. The likely cause is that
renormalising every step restores the norm-preserving structure, which makes that control **VACUOUS**. It was not
used. The claim that no-signalling requires the martingale structure (1204.4325v3 p.17) stays READ, not computed.

## 4. H-12: which of the twelve could carry a state-dependent drift

The definitions were READ from M's `multiverse_12_vector_taxonomy_v2.pdf` through the Drive connector.

| class | members | what that means for a drift |
|---|---|---|
| **Cannot carry a drift of their own** (4) | M (Madelung ordering), R (relativistic contraction) | readouts of α and v; they inherit those bounds |
| | K (Kondo T_K), T (Grüneisen γ_TA) | material properties, not constants of nature; no variation-of-a-constant bound applies |
| **Can carry one in KR form** (5 field carriers) | Z0, α_s, G, G_F, v | see the list below |
| **Can carry one only conditionally** (3) | CP (if the Yukawa matrix is a field), Λ (if dark energy is dynamical), G_θ (if an axion exists, 2001.11966v1 p.1) | no READ variation bound |

The five field carriers:

* **Z0**: Z0 = 2αh/e² = 376.730313410 Ω, computed, against CODATA 376.730313412. So Z0's variation is α's. The
  carrier is the photon field. **Z0 is the only one of the twelve with a measured state-dependent bound**,
  |ε_γ| < 1.15e-12, and that bound belongs to the causal family. Time variation: α̇/α = 1.0(1.1)e-18 /yr; coupling
  to gravity (c²/α)dα/dΦ = 14(11)e-9 (2010.06620v2 p.1, Table II).
* **α_s**: carried by the gluon field. KR fn. 5 says no non-trivial bounds can be placed on ε_S. The available proxy
  is Oklo, |Ẋ_s/X_s| < 1e-18 /yr (0705.3704v2 p.1, p.4).
* **G**: carried by the metric. KR p.14 says they are "not aware of any current experimental data" constraining ε_G.
  Ġ/G = (4 ± 9)e-13 /yr from lunar laser ranging (1009.5514v1 p.71 eq. 133, READ-VIA-RESTATEMENT of
  Williams–Turyshev–Boggs 2004).
* **G_F**: carried by the W and Z fields. No numeric bound READ; at tree level it is tied to v (named).
* **v**: the expectation value of a bosonic field, so KR's construction applies to it literally. From
  μ̇/μ = −8(36)e-18 /yr, with m_e ∝ v (fixed Yukawa, named) and the board's H1/H2 with S = 0.047–0.094:
  v̇/v = +8(38)e-18 to +11(51)e-18 /yr.

G_θ static bound: |d_n| < 1.8e-26 e·cm at 90% CL (2001.11966v1 p.6). The conversion to θ̄ is OPEN.

**Named limit: a time-variation bound bounds a drift common to all states. It does not bound state-dependence.**
Among the twelve, only Z0 has a state-dependent bound.

### 4b. H-SETTLE × H-12 with an unbounded carrier (wave 2, computed: `h12_carrier_case`)

*Wave 1 first graded* H-SETTLE × H-12 PARTIAL, "removing O-BITS only through a Weinberg-type carrier drift". AGAINST
#16 answered that the removal is entirely H-SETTLE-W's. FOR #7 answered that H-12's carrier map is the alternative to
H-TRANSFER. Both are right, under different hypotheses:

- **Under H-TRANSFER** (the ²⁰¹Hg bound applies to Bob's carrier), H-12 adds no removal. It contributes a test list.
- **Under H-12-CARRIER + H-12-W**, Bob's carrier is α_s, G or v, which have no state-dependent bound of any kind:
  - α_s: KR fn.5 says "no non-trivial bounds can be placed";
  - G: KR p.14, no data;
  - v: no bound located.
  The carrier is also assumed to drift in Weinberg (per-branch) rather than KR (causal) form. **No READ source gives
  a model of that**, and H-12-CARRIER + H-12-W (combine's N_H12W) has no READ source: it is a named hypothesis,
  carried so the case can be computed. With no bound capping ε, a cell is excluded only if N·C < 2. **At 1 AU, N = 7
  (ε > 2.3e-3 /s) and N = 1000 (ε > 1.06e-4 /s)** flip from EXCLUDED to NOT EXCLUDED: **2 of 9 cells** (check G12a for
  the H-TRANSFER side; the flip itself, G12b, is STRUCTURAL). **At 1 AU, N = 1e6** (ε > 3.34e-6 /s) the cell is
  already NOT EXCLUDED under H-TRANSFER, so there H-12 adds nothing.
- **Wave 4 qualifier (V2-1 problem 3).** "EXCLUDED under H-TRANSFER" is LEFT-IF W_W2, and W_W2 holds the unread
  Majumder value, so the two 1 AU cells (N = 7, N = 1000) **without** H-12 are **OPEN** pending a READ, not settled
  LEFT. Read the next bullet as: H-12-CARRIER + H-12-W replaces H-TRANSFER in an exclusion that rests on an unread
  value. The exclusion is also nlcontrol's ε mapping only; for the ancilla member (support 2) no window is computed.
- **So W2 × F1 × H-12 removes O-BITS in strictly more cells than W2 × F1 under H-TRANSFER.** The removal premises are
  W2 × F1's. H-12-CARRIER + H-12-W replaces H-TRANSFER among the *window* premises. H-12 is load-bearing on the
  window, not on the removal. An absent bound is not a measurement, so this is not evidence that such a drift exists.
  *Wave 2 first said* "SET × 12 removes O-BITS REMOVED-IF {N_EPS, H-C2, H-FRAME3b, H-12-CARRIER, H-12-W}", without
  F1 and with the window premise inside the removal set.
- **Rule 2.** H-12 was exercised here and is load-bearing under H-12-CARRIER. It is not retired. B-combine's
  "H-12 load-bearing for nothing" came from an encoding in which H-12's atoms sit in no constraint, so that result is
  UNTESTED-BY-SCREEN.

**Discrepancy (recorded, not repaired).** `warpfolder.py` §4 calls the 12-vector "a list of COUPLING CONSTANTS AND ONE
VACUUM EXPECTATION VALUE". The PDF defines M, R, K and T as emergent atomic and condensed-matter properties, and Z0 as an
impedance. warpfolder's category conclusion, that none of the twelve carries a quantum number, is unaffected.

## 5. Grades, alone and in the combinations the charter names

Verdict words (wave 2): REMOVED-IF {premises} is a removal that holds if the named premises hold. NOT-BOUND-IF {premise}
means a theorem does not bind; its conclusion is not shown false, so it is not a removal. SILENT means the formalism
cannot state it. OPEN means a pathway exists that is neither excluded nor shown.

**Wave 3 layout.** The verdict is the member-attributed one. The geometry column is credited to no hypothesis. For every
row except those that reintroduce a loop (clause 2b, a D-CTC) it reads: corridor O-LOOP REMOVED-IF {H-FRW-EXACT,
H-NOT-DE-SITTER, H-CORRIDOR-MODEL}. Under ITB + N_QTOPO it reads NOT-BOUND-IF {N_QTOPO}, and {N_QTOPO, N_CORR} is a
premise clash. Removal premises and window premises are kept apart. The canonical sets are:

- **R_W2** (removal) = {N_EPS, H-C2 (with its no-branch rule), H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM,
  H-BORN-AT-BOB, H-BLOCK}.
- **W_W2** (window) = {H-MAP, H-TRANSFER, H-SPIN, H-DILUTION, the NAMED-NOT-READ bound values}.
- **R_W2′** (removal, support 2; wave 4) = {H-C2 (with its no-branch rule), H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB,
  H-EXTEND, H-FIELD-W2}. Zero-error; no H-BLOCK, no H-NLCONTROL-FORM; H-FIELD-W2 (max‖H‖T ≈ 1.43-1.56 within the
  drift time) replaces N_EPS. Its window is **unevaluated** (H-MAP not established for its field).

| hypothesis | verdict | member-attributed removes | NOT-BOUND-IF / OPEN | geometry (credited to no hypothesis) | leaves |
|---|---|---|---|---|---|
| H-SETTLE-W, M's definition read per branch, alone | **LEAVES-ALL** (not retired: load-bearing in W2 × F1) | none. It supplies a channel under H-C2 that is undefined without a preferred slicing (`frame.drift_ordering`, given H-C2's rule), and that slicing is F1's substance | — | corridor O-LOOP | O-BITS, O-MAKE, O-HOLD, O-MATTER |
| H-SETTLE-W read on the reduced state (C1), alone | LEAVES-ALL | none (2.2e-16) | — | corridor O-LOOP | O-BITS, O-MAKE, O-HOLD, O-MATTER |
| H-SETTLE-KR (causal field-expectation form), alone | OPEN | none (H-KR-TS, wave 4: KR fails Tomonaga-Schwinger integrability, 2511.15935v1 p.4 READ; no signal shown, so O-BITS stays left) | **O-HOLD OPEN** via ε_G (KR p.13, speculation in the source) | corridor O-LOOP | O-BITS, O-MAKE, O-MATTER |
| Collapse-type stochastic drift | LEAVES-ALL | none (control: no signal) | — | corridor O-LOOP | O-BITS, O-MAKE, O-HOLD, O-MATTER |
| H-12 alone, linear QM | LEAVES-ALL | none (fields12.py: 1.44e-15) | — | corridor O-LOOP | O-BITS, O-MAKE, O-HOLD, O-MATTER |
| **H-SETTLE-W × H-FRAME (clause 1)**: both load-bearing (W2 supplies the channel; F1 the slicing and the signal keying) | **PARTIAL** | **O-BITS REMOVED-IF R_W2** (window W_W2; ε_any(1 ly, N = 7) = 3.64e-8 /s, a floor) **or REMOVED-IF R_W2′** (zero-error; window unevaluated); **signal O-LOOP REMOVED-IF {N_SIGKEY}** under H-SIG-COR | — | corridor O-LOOP | O-MAKE, O-HOLD, O-MATTER |
| H-SETTLE-W × H-12 under H-TRANSFER | adds nothing (to W2 alone or to W2 × F1) | as without H-12 | — | corridor O-LOOP | as without H-12 |
| H-SETTLE-W × H-FRAME × H-12 under H-12-CARRIER + H-12-W | PARTIAL; H-12 load-bearing **on the window only** | O-BITS REMOVED-IF R_W2, with H-12-CARRIER + H-12-W replacing H-TRANSFER in the window: 2 more of 9 cells (**1 AU, N = 7 and N = 1000**; at 1 AU, N = 1e6 H-12 adds nothing). Wave 4: without H-12 those two cells are LEFT-IF W_W2, hence **OPEN** (W_W2 holds the unread Majumder value) | — | corridor O-LOOP | O-MAKE, **O-HOLD LEFT** (H-12-W is Weinberg form), O-MATTER |
| H-SETTLE-KR × H-12, with G as the carrier | **adds nothing to H-SETTLE-KR alone** (wave 4) | none (KR is causal: O-BITS untouched) | O-HOLD OPEN via ε_G -- **H-SETTLE-KR's alone**; naming G adds no premise the pathway uses | corridor O-LOOP | O-BITS, O-MAKE, O-MATTER |
| any row above × H-IT read as ITB, under N_QTOPO | as the row | as the row | corridor O-LOOP **NOT-BOUND-IF {N_QTOPO}**; premise clash {N_QTOPO, N_CORR} | does not bind an ITB corridor | signal loops unchanged |

*Wave 3 first said* (kept as history): "H-SETTLE-KR × H-12, with G as the carrier | OPEN | ... | **O-HOLD OPEN via G**",
crediting KR alone's pathway to the pair (V2-0 problem 2); W2 × F1's O-BITS with the single support R_W2 (V2-1
problem 2); and the 1 AU, N ≤ 1e3 cells without H-12 as settled LEFT (V2-1 problem 3).

*Wave 2 first said* (kept as history; the table above supersedes it):
- H-SETTLE-W alone: PARTIAL, "O-BITS REMOVED-IF {N_EPS (ε > ε_any(L, N)), H-C2, H-FRAME3b (a preferred slicing,
  H-FRAME clause 1's substance), H-MAP, H-TRANSFER, H-SPIN, H-COHERE}; O-LOOP REMOVED-IF {H-FRW-EXACT,
  H-NOT-DE-SITTER, N_SIGKEY}". Three faults: F1 was presupposed and not added back (RV-0 #2); the window premises
  were mixed into the removal set (RV-1 #3); and the geometry's O-LOOP removal was credited to a hypothesis, which
  contradicted the H-12 row (RV-0 #3).
- H-SETTLE-W × H-12 under H-12-CARRIER + H-12-W: "O-HOLD (OPEN via G in KR form)". That pathway belongs to the KR
  reading, not to H-12-W (RV-0 #4).

*Wave 1 first said:*
- H-SETTLE-W alone "leaves O-LOOP (without a fixed slicing, signals faster than light reopen loops)". Wave 2 then
  credited O-LOOP to H-SETTLE alone via exact FRW. Wave 3 credits the corridor removal to the geometry and the signal
  removal to W2 × F1 (N_SIGKEY).
- H-SETTLE × H-12 "PARTIAL: O-BITS only through a Weinberg-type carrier drift". See §4b.

Why H-SETTLE-KR's O-HOLD is OPEN: KR p.13 reads a gravitational nonlinearity as positive-energy matter in another
branch appearing here as a null-energy-violating source ("may cause it to undergo a bounce"). That is speculation in
the source, and ε_G is unconstrained.

Why the H-SETTLE-W × H-FRAME pairing removes signal loops: Gisin's protocol already needs a fixed slicing
(2412.20854v1 p.6, assumption 3b). corridors.py, imported, shows that identifications keyed to one frame close no causal
curve (0 of 2,000 pairs), while two frames do (E1, E2). Treating a signal as such an identification is the model choice
H-SIG-COR.

The record on the theory itself is contested, and the grades above carry no verdict on it:
* Gisin's theorem (READ-VIA-RESTATEMENT: 2412.20854v1 pp.5–7; quant-ph/0012041v3 p.1, p.5; 1109.6462v4 p.11) makes
  signalling generic for local deterministic nonlinearity.
* Polchinski's causal restriction (READ-VIA-RESTATEMENT: 2206.12976v1 p.1; quant-ph/0012041v3 p.1) is disputed by
  Mielnik (quant-ph/0012041v3 p.5). Mielnik argues that an observable satisfying the criterion must be quadratic.
* Bielińska–Eckstein–Horodecki find that a categorical rejection "might be premature" (2412.20854v1 p.26; *wave 1
  first said p.25*, a page misprint, now re-READ).

## 6. Testable predictions

* **H-SETTLE-W (under H-C2)**: Bob's mean σ_y shifts by tanh(2εT) when Alice switches from z to x; the shift is 2εT
  for small εT.
  - At the Majumder limit (reading A), about 310 pairs held for 1 h detect it at 3σ.
  - The arrival time is Alice's time in the preferred slicing plus T, whatever the distance. That slicing is F1's.
  - The signal falls to tanh(2ε(T − t_A)) if Alice measures partway through Bob's window, and to 0 if she measures
    after it (`frame.drift_ordering`, computed). So the effect is keyed to the slicing.
  - The candidate frame is the CMB rest frame (`cmb-dipole-370kms`, D67 NARROWED).
  - **Under C1 there is no shift.** A null result therefore does not separate "no drift" from "drift on the reduced
    state".
* **H-SETTLE-KR × G**: a gravity gradient from a test mass positioned according to a qubit outcome, read by an atom
  interferometer, as proposed in 2204.11875v1 p.4. It would bound ε_G, which is the parameter that bears on O-HOLD.

## Sources

READ means read at source through alphaXiv.

| source | status | what it was used for |
|---|---|---|
| 2411.09611v1 | READ, pp.1–8 | |
| 2204.11875v1 | READ, pp.1–4 | |
| 2206.12976v1 | READ, pp.1–5 | |
| 2106.10576v2 | READ, pp.1–3, 7–8, 13–14, 22 | |
| quant-ph/0012041v3 | READ, pp.1–6 | |
| 2412.20854v1 | READ, pp.1–10, 17–26; pp.4, 7, 26 re-READ in wave 2 | Gisin limited to pure-state maps (pp.4, 7); "might be premature" (p.26) |
| 0811.1209v2 | READ by A2; p.4 re-READ in wave 2 | Holevo broken by a CTC-assisted party (relevant only without H-BORN-AT-BOB) |
| quant-ph/9611023v1 | READ in A3 | Holevo's bound (wave 1 first labelled it NAMED-NOT-READ here) |
| 1204.4325v3 | READ, pp.1–2, 15–17, 31, 34, 53, 87, 89, 111–112, 131 | |
| 1109.6462v4 | READ, pp.1–14 | |
| 2112.09005v3 | READ, pp.1–11, 23–24 | |
| 2203.10269v3 | READ, pp.1–4 | Weinberg 2016's three-clock test; no 1989 bounds in it |
| 1909.01608v2 | READ | no Weinberg bounds in it |
| 0705.3704v2 | READ, pp.1–7 | |
| 2010.06620v2 | READ, pp.1–4 | |
| 1009.5514v1 | READ, pp.1, 71–79 | |
| 2001.11966v1 | READ, pp.1–6 | |
| 2511.15935v1 (Hsu) | READ, pp.1–3, 5 (wave 3); p.4 (wave 4) | a Weinberg-type term is foliation-independent only under microcausality, which "cannot be consistently maintained" under state-dependent evolution (p.2): corroborates H-FRAME3b ⇐ F1; carries no 1989-90 bound values. p.4: the KR model "does not satisfy the TS conditions"; the integrability condition "fails for generic states even though the KR model enforces retarded (causal) dependence" (H-KR-TS; no signal shown) |
| 2509.04320v1 (Chodos & Cooper) | READ, pp.1–2, 12, 16 (wave 3) | searched for the 1989-90 bound values; none present |
| Weinberg 1989 | READ-VIA-RESTATEMENT | qualitative structure only |
| Gisin 1989, 1990; Polchinski 1991; Simon–Bužek–Gisin 2001 | READ-VIA-RESTATEMENT | |
| Bollinger 1989; Chupp & Hoare 1990; Walsworth 1990; Majumder 1990 | NAMED-NOT-READ | PRLs that predate arXiv; no READ arXiv restatement carries the numbers (searched again in wave 3) |
| Shannon 1956 (zero-error capacity) | NAMED-NOT-READ | the zero-error step is DERIVED in `zero_error_words` (two words are confusable iff every coordinate pair is equal or confusable) |

No host refused (no 403), in wave 4 either. The D67 audit `fermion-mass-constancy` named 2010.06620 and 1009.5514 "for a future read"; the
pages cited here are now READ. That note is for the board; nothing outside docket68/ was edited.
