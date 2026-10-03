# DOCKET 68 · A4-geometry — H-IT, H-ZERO, H-NULL and R-QUANTUM

**Status: a docket work item. Nothing here is seated.** The instrument is `geometry.py`, which sits beside this file.
It imports `zero.py`, `nullinfo.py` and `cosmin.py` from beside it, and `../achievable.py` (`duration_bound`,
`hold_time`, the Fewster constant, the CODATA constants) and `../transit.py`. It copies none of them.
`python3 geometry.py --selftest` runs **48 checks and passes all 48**, in about 30 s, most of it sympy. **Eleven** of the
checks are **controls**: cases built to fail, and they do fail. One more check is printed STRUCTURAL (it checks the typed
grades and cannot fail unless they are edited), and it is not cited as evidence. *Wave 1 first said* 42 checks, 10
controls.

## Wave 2 repair (2026-10-03): what changed, and why

**The principle, stated once and applied both ways.** A theorem that does not bind a non-geometric corridor makes the
obstruction **NOT-BOUND-IF** (its premise named), never REMOVED. Showing a theorem does not apply is not showing its
conclusion false. Where an AGAINST finding and a FOR finding pulled opposite ways, they are resolved on this principle.

| verifier problem | resolution |
|---|---|
| AGAINST #11: O-MAKE-TOPO "removed" rests on an out-of-scope argument | **Applied.** It is now NOT-BOUND-IF. For **ITE** the premise is {H-ER=EPR}, and what is made is a *non-traversable* bridge only (MS fn.1), Planckian for pairs (p.17). For **ITB** the premise is {N_QTOPO}, with no READ source. |
| FOR #1: under ITB, O-HOLD's NEC form is graded LEFT on Gao-Wald and MS fn.1, whose hypotheses an ITB corridor does not meet | **Applied, symmetrically.** Under ITB, O-HOLD's geometric (NEC/throat) form is NOT-BOUND-IF {N_QTOPO}, on the same footing as O-MAKE-TOPO, and the information layer's own holding cost is OPEN. Under ITE, O-HOLD stays LEFT, because MS fn.1 *assumes* non-traversability. FOR #1 also cautioned that ITB + R-QUANTUM becomes a clash; that is named below. |
| AGAINST #4: ITB has no owning READ grade, and the H-IT grade was made under H-ER=EPR | **Applied.** H-IT is graded in two readings, ITE and ITB. ITB's grade says plainly that it has no READ realisation. |
| AGAINST #12 (sited in combine): ITB commits to nothing, so its consistency with W2 is by construction | **Recorded in ITB's grade.** The READ realisations of H-IT (MS, Van Raamsdonk) assume linear QM. |
| FOR #5: H-ZERO + H-IT graded LEAVES-ALL with O-HOLD LEFT, while H-EQUIL is named OPEN | **Applied, and computed.** EGJ gr-qc/0602001v1 was re-READ this pass (eq.(21) p.3; remark 5 p.4). `egj_fR_throat` reproduces the verifier's T_kk(r0) = 2(−2β − r0²)/r0⁴ and adds a further result: for b = r0²/r, r⁴T_kk → −2r0² for **every** β. O-HOLD is **OPEN via N_EQUIL**, neither LEFT nor removed. The same holds for H-IT + H-NULL. |
| FOR #10 (sited in combine): ITE × W2 labelled REFUTED | **Recorded here.** It is INCONSISTENT-AS-ENCODED: a clash of commitments with MS's stated linearity and non-traversability. A W2 signal on entangled pairs would test ER=EPR as MS state it; it would not refute W2. |
| FOR #0 (sited in combine): rule-2 retirement of H-ZERO and H-NULL rests on inert encodings | **Recorded in their grades.** Combine's result for both is UNTESTED-BY-SCREEN, so retirement is not established. |
| (rule: declared values in checks) the Minkowski light-sheet control typed θ = −2 | **Applied.** θ = (1/√−g)∂_a(√−g k^a) is now computed for the ingoing k in spherical coordinates. |


The work order named my files as `docket68/undefined` and `A4-geometry.md`. "undefined" is a fault in the script
that produced the order. The instrument goes by the name the order's text gives it, `geometry.py`.

M's hypotheses are carried as hypotheses throughout. **Each grade states what a hypothesis does. It never says whether
the hypothesis is true.**

## Sources (M-D67-2: arXiv is the object)

| source | status | what was taken, where |
|---|---|---|
| Gao & Wald, arXiv:gr-qc/0007021v2 | READ, all 15 pp. | Thm 1 p.6; Thm 2 pp.12-13. Hypotheses: the NEC (eq. 2) and the null generic condition (eq. 9), p.4; strong causality and compactness of J⁺(p)∩J⁻(q), p.12. Footnote 3, p.12: Borde's averaged condition may replace the NEC. p.14: pure AdS fails the null generic condition. |
| — the holographic reading ("bulk causality respects boundary causality") | **NAMED-NOT-READ** | The paper reads Thm 2 as a "time delay" relative to AdS (pp.6, 14). **It never mentions a CFT.** The charter's gloss is a later reading, and its source was not read here. |
| Van Raamsdonk, arXiv:1005.3035v2 | READ, all 8 pp. | Eq.(1), p.2. The horizons that forbid communication go with "the absence of interactions" between the CFTs, p.2. Eq.(2), mutual information bounds correlations, p.4. Pinch-off, pp.3-5. Footnote 1, p.4: geometry likely fails before the entanglement reaches zero. |
| Jacobson, arXiv:gr-qc/9504004v2 | READ, all 8 pp. | Eqs.(1)-(6), pp.4-5. Λ appears "for some constant", p.5. G = (4ħη)⁻¹, p.6. Λ "remains as enigmatic as ever", p.6. The derivation presumes local equilibrium, p.6. |
| Bousso, Fisher, **Koeller**, Leichenauer & Wall, arXiv:1509.02542v2 | READ (pp.1-13, 24-27, 29-31) | Abstract. pp.1-2: ⟨T_kk⟩ at a point can be negative "with magnitude as large as we wish". p.2: the right-hand side "can have any sign". p.4: "fixed background spacetimes with no dynamical gravity". p.4: the quantum expansion reduces to the classical one as ħ→0. Eq.(2.2), p.7. Eq.(5.3), p.25. |
| Maldacena & Susskind, arXiv:1306.0533v2 | READ (pp.1-4, 7-9, 11, 14-22, 31, 42, 47) | Footnote 1, p.2: non-traversability "can be shown using the integrated null energy condition", and "If this were not true, the ER=EPR connection would be wrong". §3.1, p.16. §3.2, pp.16-17: a bridge between distant black holes is not made "without preexisting bridges"; making pairs, separating them and then merging them does make one. p.17: non-trivial topologies "should be allowed as possible quantum states". |
| Padmanabhan & Padmanabhan, arXiv:1703.06144v1 | READ, pp.1-9 | pp.6-7: emergent gravity's field equations are invariant under adding a constant to the matter Lagrangian, and Λ is "an integration constant". |
| Eling, Guedens & Jacobson, arXiv:gr-qc/0602001v1 | READ, all 4 pp. (wave 2; first READ by the FOR verifier, re-read here) | Eq.(11), p.3: dS = δQ/T + d_iS. Eq.(21), p.3: f R_ab − f_;ab + (f − L/2) g_ab = (2π/ħα) T_ab, with f = dL/dR. p.3: the equilibrium (Clausius) version (14) "is inconsistent with energy conservation", and the internal entropy production d_iS resolves it. p.4, remark 5: "dimensional analysis suggests that in nature we have β₁ ∼ ε² ∼ L²_Planck". |
| Bousso hep-th/9905177; QNEC; 1208.5399; Fewster-Osterbrink; gr-qc/0209036; kontou-fo-ffkp; gr-qc/9510071 | the board's D67 grades (all NARROWED; `docket67-raw/GRADES.tsv`, `audits/`) | Bousso's hypotheses: Einstein's equation, plus the dominant (or the null + causal) energy condition. 1208.5399: duration bound eq.(4), C ≈ 3.17. Fewster-Osterbrink: a ξ > 0 field has no state-independent QEI. gr-qc/0209036: no QI along null geodesics, for a free massless minimally coupled scalar in 4D Minkowski. |

No host refused a request. Every alphaXiv call returned page text.

## (i) H-IT — spacetime from information

**The model is a choice, named H-QUDIT.** A d = 4 system with energies E_i = i stands in for one CFT, and two copies
are prepared in Van Raamsdonk's eq.(1) state. The instrument computes only the quantum-information statements the
essay makes. It does not compute a bulk.

1. **O-BITS: not removed.** Over 900 of Alice's choices, Bob's reduced state moves by at most **1.55e-15**: 150
   random unitaries and 150 unread measurements, at each of three temperatures. That state is Van Raamsdonk's
   thermal ρ_T (p.2) to rounding.
   - **CONTROL:** add an interaction exp(−i g Z⊗X). Bob's state then moves by **0.302**, so the detector is not blind.
   - This is the essay's own statement in numbers: connection comes from entanglement, and communication needs
     interaction. MS §3.1 says the same, and so does `transit.py` (`BEATS_LIGHT = False`).
2. **Eq.(2) holds, and the bridge pinches off.** Eq.(2) holds on all 1000 random operator pairs. **CONTROL:** with
   its right-hand side ×50 it fails somewhere.
   - As β rises, the mutual information falls: I = 3.996, 3.844, 2.734, 0.601, 0.009 bits. This is the direction in
     which the bridge pinches off.
   - **Correlation is not signal.** The bridge is built from correlations, and correlations leave Bob's marginal at
     ρ_T.
3. **O-MAKE comes in two forms, and H-IT splits them.**
   - **The topology-change form: NOT-BOUND-IF, not removed (wave 2).** Geroch and Tipler are theorems about
     classical Lorentzian manifolds.
     - Under ER = EPR (ITE; MS, a conjecture), a bridge belongs to an entangled state, and non-trivial topologies
       "should be allowed as possible quantum states" (p.17). But what is then "made" is a **non-traversable**
       bridge (MS fn.1, an assumption of the conjecture), Planckian for particle pairs (p.17). It is not a crossable
       corridor.
     - Under ITB (an information layer), the theorems do not apply, on the charter's reading and with no READ source.
     - Either way, the theorem is shown not to bind, and its conclusion is not shown false: **NOT-BOUND-IF
       {H-ER=EPR} / {N_QTOPO}**.
     - *Wave 1 first said* "Within H-IT, this form does not bind. **That half goes to M.**" and graded it a removal.
   - **The distribution form remains.** MS §3.2 (pp.16-17): no bridge is made "without preexisting bridges". The
     READ route is to make pairs together, separate them, then merge them. The separation runs at ≤ c, as
     `transit.py` has it (`TRAVERSAL_IS_REMOVED = False`). LOCC cannot create entanglement.
   - **Computed:** local unitaries change the cut entropy by **8.9e-16** bits. **CONTROL:** a nonlocal unitary takes a
     product state to **1.965** bits.
4. **O-HOLD: not removed. Under ITE it is LEFT; under ITB its geometric form is NOT-BOUND-IF {N_QTOPO} (wave 2).**
   The readings in this item (Gao-Wald, MS fn.1) are about geometric throats in Lorentzian spacetimes, or about
   ER=EPR. An information-layer corridor (ITB) meets none of their hypotheses. The same principle that makes
   O-MAKE-TOPO NOT-BOUND-IF therefore applies, and what the information layer charges to hold a corridor is OPEN.
   *Wave 1 first said* "O-HOLD: not removed" for H-IT in general, on these grounds.
   - **Gao-Wald Thm 2, encoded as logic in z3.** A bulk shortcut is UNSAT when every hypothesis holds. It is SAT when
     only the NEC (with Borde's averaged form) fails, and SAT when any single hypothesis is dropped.
   - **The guards hold:** the hypotheses are jointly satisfiable, and the encoding drifts on 0 of 64 assignments.
   - So Gao-Wald forbids nothing outright. A shortcut must break one of the theorem's hypotheses, and the obvious
     candidate is the NEC, which is O-HOLD. The theorem gives **no ranking** among its hypotheses.
   - MS footnote 1 rests non-traversability on the integrated NEC.
5. **O-MATTER, O-LOOP: not removed.** No READ result on H-IT addresses either one.

## (ii) H-ZERO, alone and with H-IT

- **Alone.** Shifting the zero is T_ab → T_ab + λg_ab. `zero.py` shows it moves the NEC combination by 0, the WEC
  density by −λ and the SEC combination by +λ.
  - **z3 proves the NEC part over every symmetric T, every λ and every null k:** the negation is UNSAT.
  - **The guards hold:** the premise is satisfiable, and the encoding differs from numpy by at most 1.4e-15 at 20
    points.
  - **CONTROL:** the same claim for a timelike u is SAT.
  - The throat's ρ + p_r depends on b(r), not on where zero sits. **H-ZERO alone leaves all five obstructions.**
- **With H-IT (Jacobson; Padmanabhan pp.6-7).** Jacobson's δQ = TdS uses only T_kk.
  - **Computed:** contracting his eq.(6) with a null k cancels both Λ and R, leaving R_kk = (2π/ħη)T_kk. A zero shift
    is invisible to that equation. **CONTROL:** contracted with a timelike u, Λ stays.
  - So under emergent gravity **the zero is free**, and that answers GR's objection to H-ZERO: in GR, moving the zero
    adds a cosmological constant, which gravitates.
  - Padmanabhan fixes the integration constant separately, through CosmIn. `cosmin.py`'s check A round-trips:
    Ic(ν = 6144) = 4π to 1.8e-15.
  - **The deficit is untouched.** In this framework the throat still needs R_kk < 0, so T_kk < 0. That is exactly
    the part of T_ab the free zero cannot reach.
  - Computed from his eqs.(2) and (5): T_kk < 0 gives δQ < 0 and δA < 0. The local Rindler horizon's entropy would
    fall. Jacobson presumes local equilibrium (p.6), and whether it can hold at a throat is **OPEN**. That
    assumption is named H-EQUIL.
  - **Relaxing H-EQUIL (wave 2, computed; EGJ READ).** Out of equilibrium, EGJ's eq.(21) contracted with a null k
    gives (2π/ħα)T_kk = f R_kk − d²f/dλ². This uses the affine k, and the g_ab term drops, as Λ did. For b = r0²/r
    (R = −2r0²/r⁴) and f = 1 + βR, `egj_fR_throat` gives:
    - **T_kk ∝ −2r0²(r⁴ − 20βr² + 22βr0²)/r⁸**;
    - at the throat, T_kk(r0) = 2(−2β − r0²)/r0⁴, which is ≥ 0 iff **β ≤ −r0²/2**. At r0 = 1 m that is 1.9e69 l_P²,
      against EGJ's own dimensional expectation β ~ l_P² (p.4). There f(r0) = 2 > 0;
    - just outside the throat it stays negative: −1.68 at 1.05 r0 with β = −r0²/2;
    - **r⁴T_kk → −2r0² for every β**, so for this shape T_kk < 0 somewhere whatever β is;
    - control: β = 0 returns Jacobson's R_kk.
    So relaxing H-EQUIL opens a pathway, neither excluded nor shown: it can move the deficit off the throat point,
    but not out of this shape, and only at a β 69 orders above the dimensional estimate. Other shapes and other f
    are not computed.
  - **Grade: OPEN** (O-HOLD OPEN via N_EQUIL; O-MAKE-TOPO NOT-BOUND-IF, inherited from the H-IT reading). The pairing
    also removes an objection to H-ZERO itself. *Wave 1 first said* "Grade: LEAVES-ALL ... It removes none of the
    five obstructions", which left H-EQUIL named but not carried.

## (iii) H-NULL — "Null (NEC) is a containment"

- **Computed with sympy, for the Morris-Thorne metric with Φ = 0 and an arbitrary b(r).**
  - R_kk = 8π(ρ + p_r), which is `zero.py`'s own expression, and **R_kk(r0) = (b′ − 1)/r0²**.
  - The radial null congruence has θ = 0 at the throat and dθ/dλ = (1 − b′)/r0² > 0 there. That is Raychaudhuri with
    θ = σ = 0.
  - For three flare-out shapes, θ > 0 just outside the throat on either sheet.
- **So no congruence leaving the throat sphere has θ ≤ 0. No light-sheet leaves the throat.**
  - **CONTROLS:** the ingoing congruence of a sphere in Minkowski space has θ = −2/R, so a light-sheet exists there.
    With b′(r0) = 1 (no flare-out), dθ/dλ = 0 and R_kk = 0.
- **The reading, both ways.**
  - *For M:* the computation supports the first clause in a precise sense. The NEC is what makes null congruences
    focus, which is what closes a light-sheet. That is a containment, and Bousso's bound counts information on it.
  - *Against the corridor:* the throat is exactly where that containment fails. Bousso's hypotheses (Einstein's
    equation, plus the dominant or null + causal energy condition; board, NARROWED) exclude the throat, and the
    bound is silent there.
- **The price in bits.** This carries the QNEC outside its scope, as the named hypothesis H-QNEC-OUT-OF-SCOPE: BFKLW
  p.4 covers fixed backgrounds with no dynamical gravity.
  - `nullinfo.py` gives S″/A ≤ **−1.3807e69 bits per m⁴** at r0 = 1 m and b′ = 0. Symbolically, that is exactly the
    light-sheet density 1/(4l_P² ln 2) divided by r0².
  - Under H-CONST (S″ held constant over a null run of length r0, starting from S′ = 0), |ΔS|/A = **6.90e68 bits/m²,
    or 0.500 of the light-sheet cap**. Over the throat sphere that is **8.68e69 bits**.
  - BFKLW eq.(5.3) puts a uniform deformation's second variation at or below the sum of the diagonal ones, so the
    uniform reading does not weaken the requirement.
- **Can any READ state reach it? OPEN.**
  - In the QNEC's own scope, nothing forbids it pointwise: ⟨T_kk⟩ can be negative "with magnitude as large as we
    wish" (pp.1-2). Any state that has the throat's T_kk automatically meets the QNEC.
  - No READ paper exhibits a state with the throat's profile, and the duration limit is part (iv).
  - The QNEC prices O-HOLD. It does not remove it, and it is not a channel.
- **Grade: LEAVES-ALL.** The price is H-NULL with H-INFO in computable form, as the charter pairs them. H-INFO is
  A3's item.

## (iv) R-QUANTUM — holding a 1 m throat with QEI-bounded negative energy

- **Making the bound speak to the deficit.** At b′(r0) = 0 the energy density is ρ = 0, and the whole deficit is
  radial tension.
  - A radial observer at v² = 1/2 has γv = 1. That observer sees T₀′₀′ = γ²(ρ + v²p_r) = p_r = ρ + p_r, so the NEC
    combination becomes an energy density, and the T₀₀ bound applies to it (computed).
  - At γv = 1, the observer's proper time to cross a radial extent r0 is r0/c, which is `achievable.hold_time(r0)`.
  - Named hypotheses: H-PATH (the path is taken over the static frame's radial coordinate) and H_flat (the board's
    own).
- **Numbers at r0 = 1 m.**
  - Required: |ρ + p_r| = c⁴/(8πG r0²) = **4.8155e42 Pa**.
  - Allowed: `duration_bound(3.3356e-9 s)` = **1.0022e-25 Pa**.
  - **Fraction covered: 2.08e-68.**
  - At the required magnitude, the bound lets the negative energy last T* = **4.0e-26 s**. That is 1.2e-17 of the
    hold time, or 7.4e17 Planck times.
  - The bound stops refusing at r* = √(8πC)·l_P = **8.93 l_P**. That is the board's own dimensional identity, l_P
    times an O(1) number by construction (`achievable.persistence_crossing`). **It is not evidence of a throat at that
    size.**
  - **CONTROLS:** at r0 = r*, the fraction is 1. At r0 = r*/2, the bound does not refuse.
- **Scope.** The bound covers a massless minimally coupled scalar in Hadamard states in flat space.
  - For a ξ > 0 nonminimally coupled scalar there is **no state-independent QEI** (Fewster-Osterbrink; Fewster 1208.5399
    §5.1, board NARROWED). On that branch R-QUANTUM is **OPEN, not refused**.
  - gr-qc/0209036 (board NARROWED) finds no QI along null geodesics for the free massless minimal scalar in 4D
    Minkowski. A timelike-worldline QNEI does exist there, and that is the form used above.
- **Grade: LEAVES-ALL** in the bound's proven scope, with the ξ > 0 branch OPEN.

## Combinations (standing instruction)

| combination | result |
|---|---|
| H-ZERO + H-IT | Pairing named in the charter. The zero becomes free (ii). O-HOLD is **OPEN via N_EQUIL** (EGJ computed in (ii)). O-MAKE-TOPO is NOT-BOUND-IF (inherited). The rest stand. *Wave 1 first said* "the five obstructions stand". |
| H-NULL + R-QUANTUM | Both bear on O-HOLD. At 1 m the throat needs \|ΔS\|/A = 0.5 of the light-sheet cap (QNEC outside scope) **and** a deficit lasting 3.3e-9 s, against 4.0e-26 s allowed. These are requirements (floors), not supplies. O-HOLD stays. |
| H-IT + H-NULL | Jacobson's NEC ⇔ focusing ⇔ the area/entropy bookkeeping (computed in (ii)). Under H-EQUIL the throat's NEC deficit becomes an entropy decrease on local horizons. With H-EQUIL relaxed, O-HOLD is **OPEN via N_EQUIL**, as above. Nothing is removed. *Wave 1 first said* "Nothing is removed" and left O-HOLD standing. |
| ITB + R-QUANTUM | **A named clash for one corridor.** R-QUANTUM's premise is a geometric throat held by QEI-bounded negative energy. ITB's non-binding premise (N_QTOPO) is that there is no geometric throat. They are alternative accounts of the same corridor and cannot both be asserted of it (FOR #1's caution). |
| ITE + H-SETTLE W2 (sited in combine) | INCONSISTENT-AS-ENCODED, not REFUTED. MS assume linearity (§5.4) and non-traversability (fn.1, via the integrated NEC), and W2 drops linearity. A W2 signal on entangled pairs would be a test of ER=EPR as stated, not a refutation of W2. |
| the other subsets of {H-IT, H-ZERO, H-NULL, R-QUANTUM} | **Not tested, for a stated reason.** There is no removal in this set: wave 2 grades every former removal NOT-BOUND-IF or OPEN. No member removes an obstruction that another leaves, so these subsets offer no complementary pairing to test. |

## Grades

Verdict words: **NOT-BOUND-IF** means nothing is removed, but a theorem is shown not to bind under the named premise.
**OPEN** means a pathway is neither excluded nor shown.

| hypothesis | verdict | removes | not bound / open | leaves |
|---|---|---|---|---|
| H-IT read as ER=EPR (ITE) | **NOT-BOUND-IF** | — | O-MAKE-TOPO NOT-BOUND-IF {H-ER=EPR}, non-traversable bridge only (MS fn.1; Planckian for pairs, p.17) | O-BITS (computed); O-MAKE-DIST (MS §3.2; LOCC computed); O-HOLD (MS fn.1 assumes it; Gao-Wald); O-MATTER; O-LOOP |
| H-IT read as an information layer (ITB) | **NOT-BOUND-IF** | — | O-MAKE-TOPO and O-HOLD's geometric form NOT-BOUND-IF {N_QTOPO}, no READ source; the layer's own holding cost OPEN | O-BITS; O-MAKE-DIST (linear QM, computed); O-MATTER; O-LOOP |
| H-ZERO | LEAVES-ALL | — | — | all five (z3: NEC invariant). Rule 2: UNTESTED-BY-SCREEN in combine |
| H-ZERO + H-IT | **OPEN** | (only GR's objection to H-ZERO) | O-HOLD OPEN via N_EQUIL (EGJ, computed); O-MAKE-TOPO NOT-BOUND-IF (inherited) | O-BITS, O-MAKE-DIST, O-MATTER, O-LOOP |
| H-IT + H-NULL | **OPEN** | — | O-HOLD OPEN via N_EQUIL; O-MAKE-TOPO NOT-BOUND-IF (inherited) | O-BITS, O-MAKE-DIST, O-MATTER, O-LOOP |
| H-NULL | LEAVES-ALL | — | — | all five; O-HOLD's requirement is 0.5 of the light-sheet cap per m² at 1 m (a floor, not a supply). Rule 2: UNTESTED-BY-SCREEN in combine |
| R-QUANTUM | LEAVES-ALL (in scope) / OPEN (ξ > 0) | — | — | all five; the bound covers 2.1e-68 of O-HOLD's deficit |

*Wave 1 first said:* H-IT **PARTIAL**, removing "O-MAKE, the Geroch/Tipler topology-change form, under H-ER=EPR"; H-ZERO
+ H-IT **LEAVES-ALL**. Both changed on the principle stated at the top.

## Named hypotheses

H-QUDIT (a finite TFD stands in for the CFT pair). H-ER=EPR (MS's conjecture, with non-traversability assumed: their
footnote 1). N_QTOPO (wave 2: an information-layer corridor is not a Lorentzian topology change and has no geometric
throat; the charter's reading, no READ source). N_EQUIL (wave 2: Jacobson's local equilibrium relaxed, EGJ's
non-equilibrium equation of state in its place). H-QNEC-OUT-OF-SCOPE. H-CONST (S″ constant over the null run). H-EQUIL (Jacobson's local equilibrium at a
throat). H-PATH (the boosted observer's crossing). H_flat (a flat-space QEI applied at a curved throat; the board's).
H-MIN-SCALAR (the QEI's field class). The reading of eq.(2) in nats: the stricter of the two readings.

## Testable predictions

- **H-IT:** Bob's marginals do not depend on Alice's setting, whatever the entanglement. A deviation would refute
  linear QM. It would not single out H-IT, since Van Raamsdonk's model predicts no deviation. The rate at which
  corridors are made is bounded by entanglement distribution at ≤ c.
- **H-ZERO + H-IT:** no local experiment sees an absolute zero of energy. The value of Λ is set by a separate
  principle: in `cosmin.py`, ν = 6144 from Λ.
- **H-NULL:** in any laboratory NEC violation inside the QNEC's scope, S″_out ≤ (2π/ħ)A⟨T_kk⟩ is satisfied. A state
  with T_kk < 0 and S″ > (2π/ħ)A T_kk would refute the QNEC.
- **R-QUANTUM:** at one point, a negative energy density held for a duration T has magnitude at most Cħ/(c³T⁴) for
  the minimal scalar. The ξ > 0 scalar is the place to look for an exception.

## Findings (recorded, not repaired)

1. The charter lists **gr-qc/9506083 (STANDS)** among the QEI holdings. In the board's audit
   (`audits/gr-qc_9506083.json`), that id is **Poisson & Visser, thin-shell wormhole linearised stability**, not a
   quantum energy inequality. This is a discrepancy in the charter.
2. The charter cites 1509.02542 as "Bousso-Fisher-Leichenauer-Wall". Its authors are **Bousso, Fisher, Koeller,
   Leichenauer and Wall**. BFLW is the QFC paper, 1506.02669 (their ref. [23]). The board's audit already writes
   BFKLW.
3. Gao-Wald's paper does not state the holographic "bulk respects boundary causality" reading that the work order
   ascribes to it. It proves a time delay relative to AdS **under the NEC (or Borde's averaged condition)**, which
   is exactly the condition a throat violates.
4. Not a discrepancy, only a note: `achievable.py`'s typed `L_PLANCK = 1.616255e-35` differs from √(ħG/c³),
   computed from the same file's constants, by 1.5e-8 relative. That is rounding, well inside CODATA's own
   uncertainty on G. `geometry.py` computes r* from the constants so that its round-trip check can hold to 1e-9.
