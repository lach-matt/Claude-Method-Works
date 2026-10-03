# DOCKET 68 · A4-geometry — H-IT, H-ZERO, H-NULL and R-QUANTUM

**Status: a docket work item. Nothing here is seated.** The instrument is `geometry.py`, which sits beside this file.
It imports `zero.py`, `nullinfo.py` and `cosmin.py` from beside it, and `../achievable.py` (`duration_bound`,
`hold_time`, the Fewster constant, the CODATA constants) and `../transit.py`. It copies none of them.
`python3 geometry.py --selftest` runs **42 checks and passes all 42**, in about 20 s, most of it sympy. **Ten** of the
checks are **controls**: cases built to fail, and they do fail.

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
   - **The topology-change form.** Geroch and Tipler are theorems about classical Lorentzian manifolds. Under
     ER = EPR (MS, a conjecture), a bridge belongs to an entangled state, and non-trivial topologies "should be
     allowed as possible quantum states" (p.17). Within H-IT, this form does not bind. **That half goes to M.**
   - **The distribution form remains.** MS §3.2 (pp.16-17): no bridge is made "without preexisting bridges". The
     READ route is to make pairs together, separate them, then merge them. The separation runs at ≤ c, as
     `transit.py` has it (`TRAVERSAL_IS_REMOVED = False`). LOCC cannot create entanglement.
   - **Computed:** local unitaries change the cut entropy by **8.9e-16** bits. **CONTROL:** a nonlocal unitary takes a
     product state to **1.965** bits.
4. **O-HOLD: not removed.**
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
  - **Grade: LEAVES-ALL.** The pairing removes an objection to H-ZERO itself. It removes none of the five
    obstructions.

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
| H-ZERO + H-IT | Pairing named in the charter. The zero becomes free, and the five obstructions stand (ii). |
| H-NULL + R-QUANTUM | Both bear on O-HOLD. At 1 m the throat needs \|ΔS\|/A = 0.5 of the light-sheet cap (QNEC outside scope) **and** a deficit lasting 3.3e-9 s, against 4.0e-26 s allowed. O-HOLD stays. |
| H-IT + H-NULL | Jacobson's NEC ⇔ focusing ⇔ the area/entropy bookkeeping (computed in (ii)). Under H-IT the throat's NEC deficit becomes an entropy decrease on local horizons, which H-EQUIL leaves OPEN. Nothing is removed. |
| the other 8 subsets of {H-IT, H-ZERO, H-NULL, R-QUANTUM} | **Not tested, for a stated reason.** The only removal in this set is H-IT's topology-change form of O-MAKE. No other member removes an obstruction that H-IT leaves, so these subsets offer no complementary pairing to test. |

## Grades

| hypothesis | verdict | removes | leaves |
|---|---|---|---|
| H-IT | **PARTIAL** | O-MAKE, the Geroch/Tipler topology-change form, under H-ER=EPR | O-BITS (computed); O-MAKE, the distribution form (MS §3.2; LOCC computed); O-HOLD (Gao-Wald, MS fn.1); O-MATTER; O-LOOP |
| H-ZERO | LEAVES-ALL | — | all five (z3: NEC invariant) |
| H-ZERO + H-IT | LEAVES-ALL | (only GR's objection to H-ZERO) | all five |
| H-NULL | LEAVES-ALL | — | all five; O-HOLD is priced at 0.5 of the light-sheet cap per m² at 1 m |
| R-QUANTUM | LEAVES-ALL (in scope) / OPEN (ξ > 0) | — | all five; the bound covers 2.1e-68 of O-HOLD's deficit |

## Named hypotheses

H-QUDIT (a finite TFD stands in for the CFT pair). H-ER=EPR (MS's conjecture, with non-traversability assumed: their
footnote 1). H-QNEC-OUT-OF-SCOPE. H-CONST (S″ constant over the null run). H-EQUIL (Jacobson's local equilibrium at a
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
