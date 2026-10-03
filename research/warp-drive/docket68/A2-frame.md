# DOCKET 68 · A2-frame — H-FRAME, alone and with the curvature pairing

**Status: a docket work item. Nothing here is seated.** The instrument is `frame.py`, which sits beside this file
and imports `corridors.py` (and through it `latticectc.py`), `frw_frame.py`, `nosig.py`, `nlcontrol.py` and
`../transit.py` rather than copying them. `python3 frame.py --selftest` runs 56 checks and passes all 56
(about 25 s, most of it spent importing the pre-docket scripts, which run their own computations when imported).
Fifteen of those checks are **controls**: cases built to fail, and they do. *Wave 1 first said* 47 checks, 13 controls.

## Wave 2 repair (2026-10-03): what changed, and why

Each verifier problem sited in this work item is listed with its resolution. Wave 1's first forms are kept below,
marked *wave 1 first said*.

| verifier problem | resolution |
|---|---|
| AGAINST #6: `antitelephone` hard-codes the cosmic-frame 0 | **Applied.** `reply_arrival(u)` solves the Lorentz transformation with sympy for any keying frame u. Both values are now computed: −3/5 keyed to the sender, 0 keyed to the cosmic frame. An independent value (u = ½, L = 2 gives −1) is checked. |
| AGAINST #5: the 0.0817 bits and "C2 needs a frame" come from the D-CTC, which needs a CTC at Bob, and clause 1 excludes every CTC | **Applied.** The D-CTC numbers are withdrawn as ground for H-FRAME + H-SETTLE. That row's channel is now nlcontrol's drift, and **the drift's own ordering dependence is computed** (`drift_ordering`): Bob's signal is tanh(2ε(T − t_A)), giving 0.537 with Alice first, 0.291 with Alice at mid-window, and 0 when Bob's window is over first (the drift is computed on his reduced state, not assumed). The D-CTC under C2 gets a row of its own, as a clause-2b world. |
| AGAINST #7: the H-FRAME + H-SETTLE (C2) row lists O-BITS as removed, with no ε condition and no timing | **Applied.** O-BITS is REMOVED-IF {N_EPS (A1: ε > ε_any(L, N)), H-C2, H-BORN-AT-BOB, A1's bound hypotheses}. On A2's own evidence alone it was OPEN. |
| AGAINST #8, REPRODUCE #2: "per BHW p.2 (READ, not computed here) ... 1 bit per pair" labels a derived figure READ | **Applied, and now computed.** BHW's own construction (p.2 Fig. 2 and the p.3 theorem, re-READ) is run through this file's Deutsch fixed point (`bb84_c2_table`). It reproduces the READ map for all four inputs with unique fixed points, and gives **1.000000 bit per pair under C2 and 0 under C1**. |
| FOR #2 (3): "the per-qubit budget under C2 is OPEN" when 1 bit per pair × 2 pairs is arithmetic | **Applied.** The D-CTC under C2 needs 2 pairs per teleported qubit. FOR #2 also reports a four-basis discriminator at 2 bits per pair; that figure is the verifier's computation and was not re-run here. BHW p.4 (READ): a CTC-assisted rate is unbounded. |
| FOR #6: "M's sentence contradicts itself" (B-combine) rests on the docket's keying, not M's words | **Applied here at the source.** Clause 1 is M's "a preferred frame exists". "Corridors keyed to it" is the docket's modelling addition, now named H-KEYING. M's sentence is satisfied without contradiction by clause 1 + 2a. Clause 2b is excluded only by H-KEYING (or, in exact FRW, by the geometry) and only if corridors are the sole route to the cosmic past (H-2B-VIA-CORRIDOR). |
| FOR #9: O-LOOP keying is forced by exact FRW | **Applied.** This file's own z3 lemma shows that under H-FRW-EXACT + H-NOT-DE-SITTER only equal-cosmic-time identifications are isometries. So for corridors, the keying is the geometry's, not clause 1's. H-FRAME's contribution reduces to N_SIGKEY (signals keyed to that slice) plus H-CMB-IS-COSMIC. |
| (rule: declared values in checks) the de Sitter tangent norm was typed as −1 | **Applied.** It is now computed from the metric. |
| A2-frame.json had no `grades` list | **Applied.** The JSON now carries one, in A1's schema, with the summary kept for combine's reader. |

The hypothesis is M's, quoted from the charter: *"A preferred frame - maybe messages can travel into the past, it
seems impossible because our lack of understanding about cosmic information"*. It is carried as two clauses, and
each is graded on its own:

- **clause 1**: a preferred frame exists. *Wave 1 first said* "a preferred frame exists, and corridors are keyed to
  it". The keying is the docket's modelling addition (**H-KEYING**), not M's words, except in exact flat FRW, where
  the geometry forces it (part (i));
- **clause 2**: messages may travel into the past.

## Sources (M-D67-2: arXiv is the object)

| source | status | what was taken, where |
|---|---|---|
| Deutsch, PRD 44, 3197 (1991) | NAMED-NOT-READ (not on arXiv); **READ-VIA-RESTATEMENT** | The consistency condition and the output map are BLSS arXiv:0908.3023v2 p.1, eqs (1)-(2). The phrase "because the fixed point is allowed to be a mixed state, it always exists" and the remark that the induced map "is nonlinear" are on the same page. BHW arXiv:0811.1209v2 p.1, eqs (1)-(2), adds that the solution "does not necessarily have to be unique". |
| Bennett, Leung, Smith & Smolin, arXiv:0908.3023v2 | READ | p.1: EPR half sent into a CTC gives ρ_CTC = I/2 and ρ'_AB = I/4. p.2, Fig. 2: the "linearity trap". p.4: the "Principle of Universal Inclusion", and the point that Deutsch's formalism reduces to standard QM far from a CTC. p.3: Weinberg-type FTL claims fall into the same trap. |
| Brun, Harrington & Wilde, arXiv:0811.1209v2 | READ | p.2, Fig. 1: SWAP then controlled-H. Input \|0⟩ gives ρ_CTC = \|0⟩⟨0\|, input \|−⟩ gives \|1⟩⟨1\|, and both are unique. p.2, Fig. 2: perfect discrimination of the four BB84 states. p.4: the Holevo bound is broken. |
| Novikov, PRD 45, 1989 (1992) | NAMED-NOT-READ; **READ-VIA-RESTATEMENT** | Carlini, Frolov, Mensky, Novikov & Soleng, arXiv:gr-qc/9506087v2, p.3: only "globally self-consistent" solutions occur locally. pp.13-14: Echeverria, Klinkhammer & Thorne found multiple (even infinitely many) self-consistent solutions and "no evidence for non self-consistent trajectories". Visser, gr-qc/0204022v2 p.5. |
| Hawking, PRD 46, 603 (1992) | NAMED-NOT-READ (not on arXiv: an alphaXiv title query resolved to 2607.22056 instead); **READ-VIA-RESTATEMENT** | Visser, gr-qc/0204022v2: p.2 states the conjecture. pp.6-9 cover the chronology horizon, the fountain, and the divergence of ⟨T_μν⟩ on the polarized hypersurfaces. pp.10-11: Kay, Radzikowski & Wald show the semiclassical equations fail on the horizon. p.14: "we do not know for certain". p.5: canonical gravity's universal foliation "forbids closed timelike curves at the kinematical level". Bermudez & Leonhardt, arXiv:2607.22056v1, p.11 and App. A, quote Hawking's sentences. |
| CMB dipole | the board's D67 grade, `cmb-dipole-370kms` **NARROWED** (`docket67-raw/GRADES.tsv:112`; audit json) | 369.82 ± 0.11 km/s, READ-VIA-RESTATEMENT of Planck 2018. Its H1 (the dipole is kinematic) and H2 (the reference point is the Solar-System barycentre; Earth moves at 340.65-399.08 km/s over a year) are carried here as hypotheses. |
| Geroch 1967, Tipler 1977 | not re-read; the board's D67 grades as the charter records them | used only for the O-MAKE row |

No host refused a request in this pass. Every alphaXiv call returned content.

## (i) Which corridor networks a preferred frame admits

**The model, and it is a choice.** A corridor is an identification of positions by a translation ξ, under
latticectc's H1-H3 (flat bulk, a translation lattice acting freely, test branes). A corridor is *keyed to the
cosmic frame* when ξ has no time component in the comoving frame u. Equating that frame with the CMB-dipole-free
frame is a further hypothesis, H-CMB-IS-COSMIC.

1. **Clause 1 removes O-LOOP, at any rank.** If every generator has ξ_t = 0, the Minkowski Gram matrix is the
   Euclidean Gram matrix of the spatial parts. That matrix is positive definite, so the span holds no nonzero
   causal vector, and by latticectc's THEOREM (a) no closed causal curve exists. The argument is proved by
   inspection. The exact Sylvester test confirms it on 300 rank-2 and 300 rank-3 lattices, with 0 failures. This
   extends `corridors.py`'s rank-2 sample: latticectc's own computations are rank 2 only, and at rank 3 it warns
   that pairwise tests are not enough.
2. **Control (`corridors.py`'s witness).** E1 = (9/10, 1, 0, 0) is keyed to the frame moving at v = 9/10. E2 is
   keyed to another frame. Their span is timelike, and the pair closes a causal curve.
3. **Clause 2, the strong form (2b): a message into the past of the cosmic clock.** A corridor traversed from
   p+ξ to p moves a message by −ξ_t in cosmic time. So "some message reaches the cosmic past" is the same
   condition as ξ_t ≠ 0, which is the same as "not keyed to the cosmic frame". When |ξ_t| < |ξ_x|, the corridor is
   keyed to the frame moving at v = ξ_t/ξ_x.
   - **Computed:** take one corridor (−1/10, 1, 0, 0) and one cosmic corridor (0, 1, 1/100, 0). Their span is
     timelike, and the lattice vector (−1, 1) has norm −99/10000, which is a closed causal curve.
   - **In general (sympy):** for ξ1 = (−T, L, 0, 0) and ξ2 = (0, a, b, 0), the Gram determinant is
     L²b² − T²a² − T²b². It is negative exactly when b²(L² − T²) < T²a². **Every T > 0 has such a b**, so a single
     past-directed corridor, however small the step, closes a causal curve once it sits beside one suitably
     oriented cosmic corridor.
4. **Clause 2, the weak form (2a): the coordinate past of a moving frame.** Clause 1 admits this, and it closes
   no loop. Take a cosmic-simultaneous corridor one light-year long along the dipole. In the barycentre's frame it
   delivers at dt' = −γ(v/c)·(1 yr) = **−38,929 s (−10.81 h)**. For Earth over a year, the figure runs from
   −35,858 s to −42,009 s. This is a "past" in that frame's coordinate time only.

**The tension with M's second clause, stated exactly (wave 2).**
- A clause-1 network *keyed to the frame* (H-KEYING) admits clause 2a and excludes clause 2b. Clause 2b added to such
  a network brings O-LOOP back in the model for every T > 0.
- **M's sentence itself does not contradict itself.** "A preferred frame exists" plus "messages may travel into the
  past" is satisfied by clause 1 + 2a: the coordinate past of moving frames, −38,929 s per light-year in the
  barycentre frame, with no loop.
- The exclusion of 2b comes from H-KEYING (or, in exact FRW, from the geometry), and it holds only if corridors are the
  only route to the cosmic past (H-2B-VIA-CORRIDOR).
- *Wave 1 first said* "the two clauses cannot both hold in their strong form unless something else (a consistency
  principle, part (ii)) handles the loop". That is true of the keyed network, not of M's sentence. M's
own ruling, M-S1A-P3 (`LEDGER.md:175`), already prices this: a closed causal curve disqualifies a device **at the
seat only**. So clause 2b is disqualifying when its loop passes through the seat, and is not disqualified
otherwise.

**The curvature pairing (`frw_frame.py`, re-run through its own `lie_g`).**

- For a generic a(t): ∂x is Killing, while ∂t and the Minkowski-form boost are not. The Minkowski control fires
  (the boost is Killing there).
- **The time-function lemma (z3).** In ds² = −dt² + a²|dx|² with a > 0, every nonzero causal vector has v_t ≠ 0.
  The proof comes back `unsat`. The vacuity guard returns `sat` (the hypothesis is satisfiable). The
  encoding-drift guard matches `frw_frame`'s metric to 2.8e-14. The control (allow a ≥ 0) returns `sat`, so the
  claim fails there as it must. Comoving translations preserve t, so cosmic time is a global time function on
  the quotient, and **no closed causal curve exists, at any rank, for any a(t) > 0**. This argument does not use
  the flat-space lattice theorem at all.
- **NARROWING of the charter's reading, both ways.** The Killing equation for the family ∂t − c x·∂x reduces
  to 2a(a' − ca) = 0, so that vector is Killing exactly when a'/a = c is constant: **exact de Sitter**. There the
  isometry (t, x) → (t + τ, e^{−Hτ}x) fixes the worldline x = 0 and shifts it forward by τ. Its quotient
  therefore has a closed timelike curve (an isometry: True; tangent norm −1).
  - For ΛCDM, a = sinh^{2/3}(t), that vector is **not** Killing while ∂x is. So the charter's statement, that
    the expanding universe admits only equal-cosmic-time identifications, holds for ΛCDM and fails in its de
    Sitter limit.
  - In that limit the cosmic frame is selected by the matter content (the CMB), not by the geometry.
  - The Killing search covered ∂x, ∂t, the boost and the dilation family. Killing vectors whose ξ^t depends on x
    were not exhausted; that limit is named as H-KILLING-SEARCH.

**What chronology protection says.** Clause 1 is the kinematic form Visser describes on p.5: a universal
foliation "forbids closed timelike curves at the kinematical level". Under clause 1 no chronology horizon forms,
so Hawking's divergence never arises, and H-FRAME and the conjecture agree. Clause 2b is what the conjecture
says the laws forbid. But the conjecture is unproven: the semiclassical treatment fails on the horizon
(Kay, Radzikowski & Wald, pp.10-11), and the matter is "deep into the guts of quantum gravity" (p.14). It
therefore refutes nothing: **clause 2b is OPEN as physics**, and its O-LOOP is computed inside the model.

## (ii) Deutsch's fixed point on a qubit CTC

`frame.py` implements σ = Tr_CR[U(ρ⊗σ)U†] (BLSS eq 1). Existence is constructive: σ → T(σ) is CPTP and linear in
σ for fixed ρ, so the Cesàro means of Tⁿ(I/2) converge to a fixed **state**. That estimate is then projected onto
the exact eigenvalue-1 eigenspace.

- **READ fixtures, all reproduced.** BHW: input \|0⟩ reads 0 and input \|−⟩ reads 1, each with a unique fixed
  point. BLSS: ρ_CTC = I/2 and ρ'_AB = I/4.
- **It always has a solution.** Across 400 random 2-qubit U with random mixed ρ there were 0 failures (maximum
  residual 5.6e-16, all fixed points positive). The selection rule is not unique, however. With U = I, the
  fixed-point space has dimension 4 (a control), so a selection rule is a further hypothesis, H-DCTC-SELECT.
- **It is nonlinear in the input (computed, exact to rounding).** P(A=0) is 1, 1/3, 2/3 and 0 for the inputs
  \|0⟩, \|1⟩, \|+⟩ and \|−⟩. For input I/2 it is **1/2**, where linear mixing of the \|0⟩ and \|1⟩ outputs would
  give **2/3**.
- **Does it signal? That depends on one named convention, H-DCTC-CONVENTION.** Bob feeds his half of a singlet
  into the BHW circuit, and Alice chooses none, z or x:

| convention | P(Bob=0): none / z / x | I(Alice's choice; Bob) |
|---|---|---|
| **C1**: Deutsch's rule on the whole system (BLSS "Universal Inclusion"; the fixed point depends only on ρ_B) | 1/2 / 1/2 / 1/2 | **0 bits** |
| **C2**: the rule applied branch by branch (the "linearity trap", BLSS p.2) | 1/2 / 2/3 / 1/3 | **1 − H(2/3) = 0.0817 bits** per use |

**Bearing on H-SETTLE.** Deutsch's map is a deterministic map in which the state's own value steers its
evolution, which is M's definition in form. The same convention that decides signalling for the CTC decides it
for the drift:

- Run `nlcontrol.py`'s drift H = ε⟨X⟩Z with ⟨X⟩ taken on Bob's reduced state (C1). Bob's state is then the same
  whatever Alice does (difference 2.2e-16).
- `nlcontrol.py`'s own result (0.537 at ε = 0.1) is the per-branch case, C2.

So "does H-SETTLE signal?" is not settled by the dynamics. It is settled by whether the nonlinearity acts on the
density matrix (it does not signal) or on the branch's state (it signals).

**C2 needs a preferred frame (computed for the CTC circuit and, in wave 2, for the drift).**
- **The CTC circuit.** When Alice and Bob are spacelike separated, some frame puts Bob's CTC interaction first. In that
  ordering no branch exists yet and C2 returns 1/2; with Alice first it returns 2/3 or 1/3.
- **The drift** (`drift_ordering`). Bob's drift window is [0, T]. Before Alice measures, C2 has only his reduced state
  I/2, so the drift (computed on that state) does nothing.
  - Alice first: tanh(2εT) = 0.537 at ε = 0.1, T = 3.
  - Alice at mid-window: tanh(εT) = 0.291.
  - Alice after Bob's window: 0.
  - The same events give different predictions in different frames, so **C2 is not well defined without a preferred
    slicing**.
- *Wave 1 first said* this only for the CTC circuit, and then cited the CTC numbers as ground for the drift pairing.
  The CTC needs a closed timelike curve at Bob, which clause 1 excludes, so those numbers cannot ground H-FRAME +
  H-SETTLE.

**The D-CTC's capacity under C2 (wave 2, computed from BHW's READ construction).** BHW p.2 (Fig. 2) and the p.3
theorem: swap the system with the CTC qubits, then apply Σ_k |k⟩⟨k| ⊗ U_k with eq.(3)'s U₀₀ … U₁₁. Through this file's
Deutsch fixed point:
- the READ map |00⟩→|00⟩, |10⟩→|01⟩, |+0⟩→|10⟩, |−0⟩→|11⟩ is reproduced with probability 1, and every fixed point is
  unique;
- Bob holds half a singlet and reads the first output bit a. P(a = 1) is 0 if Alice chose z and 1 if she chose x,
  under C2: **1.000000 bit per pair**;
- under C1 his input I/2 ⊗ |0⟩⟨0| is the same for both choices: **0 bits**.

## (iii) Does a preferred frame remove O-BITS?

**No.** This was computed directly; no theorem is declared.

- With `nosig.py`'s singlet, the sequential Lüders updates in the two orderings (Alice first, Bob first) give the
  same joint distribution to 1.1e-16. Bob's P(+1) is 1/2 for all seven of Alice's angles, to 2.2e-16.
- `transit.py`'s withheld-bits state is I/2 to 2.2e-16. No time coordinate enters that computation, so no frame
  can change it.
- **Control:** a non-local CNOT moves Bob's P(0) by 1.000, so the test does detect a signal when one is present.

A preferred frame chooses which ordering is "true". In linear QM both orderings give the same statistics, so
choosing one changes nothing.

## Combinations, as the standing instruction asks

| combination | removes | leaves | ground |
|---|---|---|---|
| H-FRAME clause 1 + curvature (FRW) | O-LOOP REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER}. For corridors this is the geometry's removal: the keying is forced. It fails in exact de Sitter. | O-BITS, O-MAKE, O-HOLD, O-MATTER | z3 lemma; the Killing table |
| **H-FRAME + H-SETTLE-W (the drift, under C2)** | **O-BITS REMOVED-IF {N_EPS, H-C2, H-BORN-AT-BOB, A1's H-MAP/H-TRANSFER/H-SPIN/H-COHERE}**; **O-LOOP REMOVED-IF {N_SIGKEY}** | O-MAKE, O-HOLD, O-MATTER | settle.py's drift tanh(2εT); `drift_ordering` (C2 undefined without a slicing, computed); antitelephone, both values computed: a reply keyed to the sender's frame arrives at t = −3/5 (a loop), keyed to the cosmic frame at t = 0 |
| D-CTC under C2 (a CTC at Bob, so not compatible with clause 1) | O-BITS as a channel: 0.0817 bits per use (BHW circuit), 1.000 bit per pair (BHW BB84), unbounded per BHW p.4 | O-LOOP REINTRODUCED (the channel is a CTC); O-MAKE, O-HOLD, O-MATTER | `signalling_table`, `bb84_c2_table` |
| H-SETTLE (under C1) or D-CTC (under C1), with or without H-FRAME | nothing | all five | C1 signalling: 0 bits; drift on the reduced state 2.2e-16 |

*Wave 1 first said* the H-FRAME + H-SETTLE (C2) row "removes O-BITS (0.0817 bits per pair with this circuit) and the
O-LOOP". The 0.0817 was the D-CTC's, the circuit is incompatible with clause 1, and the removal carried no ε and no
timing condition. The row is the one complementary pair found here, and it is **PARTIAL and conditional**.

- C2 is the convention BLSS argue is ill defined (p.4: it needs "additional degrees of freedom identifying the
  'correct' decomposition", which "does not reduce to standard quantum mechanics far from any CTC").
- It needs measurement to be a physical event placed in cosmic time.
- Experimental bounds on nonlinear QM are NAMED-NOT-READ in the charter.
- *Wave 1 first said* "Per BHW p.2 (READ, not computed here), their BB84 circuit would let C2 carry 1 bit per pair ...
  so the per-qubit budget under C2 is OPEN". The 1 bit per pair is now computed (`bb84_c2_table`, 1.000000), and 2
  pairs per teleported qubit follows by arithmetic. That is the D-CTC's budget, which needs a CTC.
- The drift's budget is A1's: ≥ 6.21 pairs on average for nlcontrol's Hamiltonian, and > 2 for the W2 class under
  H-BORN-AT-BOB. The general W2 capacity is OPEN without H-BORN-AT-BOB.

## Grades (H-FRAME)

| obstruction | clause 1 alone | clause 2a | clause 2b |
|---|---|---|---|
| O-BITS | LEAVES (computed) | LEAVES | LEAVES; a channel needs H-SETTLE under C2 |
| O-MAKE | LEAVES, and closes the "with a CTC" escape in Geroch's compact case (board grade, not re-read) | LEAVES | OPEN (a CTC reopens the Geroch clause) |
| O-HOLD | LEAVES | LEAVES | LEAVES |
| O-MATTER | LEAVES | LEAVES | LEAVES |
| O-LOOP | **REMOVED-IF** {H-CORRIDOR-MODEL, H-KEYING} in the model; in exact flat FRW REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER}, with the keying forced (not in exact de Sitter); for signals, + N_SIGKEY | no loop | **REINTRODUCES** in the model for every T > 0, if corridors are its route (H-2B-VIA-CORRIDOR). Deutsch/Novikov make the loop consistent, not absent; Hawking's conjecture would forbid it (OPEN); M-S1A-P3 disqualifies it at the seat. |

For M's thesis: **H-FRAME alone does not touch the two classical bits.** What it does is make a superluminal
channel chronology-safe, *if* such a channel exists. That is why it pairs with H-SETTLE: one supplies the
channel, the other removes the loop the channel would otherwise bring.

**Testable prediction.** Under clause 1, Bell-type statistics are frame-independent (computed). Under
H-FRAME + H-SETTLE (C2), Bob's statistics would depend on whether Alice's measurement precedes his in **cosmic**
time and not in either lab's time. Such a signal would therefore be keyed to the CMB dipole direction
(v/c = 1.2336e-3) rather than to any lab frame.

## Named hypotheses

The full list is `NAMED_HYPOTHESES` in `frame.py`. The ones every result above depends on:

- **H-CORRIDOR-MODEL**: a corridor is an identification of positions by a translation.
- **H-FRW-EXACT**: the universe is exactly spatially flat FRW. Real perturbations break even the translation
  symmetry, and then no identification is an exact isometry.
- **H-CMB-IS-COSMIC**: the comoving frame is the CMB-dipole-free frame (needs D67's H1 and H2).
- **H-NOT-DE-SITTER**: a(t) is not exactly exponential.
- **H-KILLING-SEARCH**: the Killing search did not exhaust x-dependent ξ^t.
- **H-DCTC**: Deutsch's model is one model among several (P-CTCs; Svetlichny).
- **H-DCTC-CONVENTION**: C1 versus C2.
- **H-DCTC-SELECT**: a selection rule where the fixed point is not unique.
- **H-LINEAR-QM**: assumed in part (iii).
- **H-KEYING** (wave 2): corridors are keyed to the preferred frame. This is the docket's addition, forced by geometry
  only under H-FRW-EXACT + H-NOT-DE-SITTER.
- **H-2B-VIA-CORRIDOR** (wave 2): corridors are the only route to the cosmic past.
- **N_SIGKEY** (wave 2): a superluminal signal is keyed to the same slice (A1's H-SIG-COR).
- **H-C2, H-BORN-AT-BOB** (wave 2): as in settle.py.

## Findings (recorded, not repaired)

1. **`frw_frame.py` rebinds its module-global `g` to Minkowski** for its final control. Any importer that calls
   `frw_frame.lie_g` after importing it gets the Minkowski Lie derivative unless it restores `g`. The script's
   own printed output is correct. `frame.py` restores `g` around its calls and then puts it back.
2. **The charter's FRW reading holds for ΛCDM but not in the exact de Sitter limit.** There a time-shifting
   dilation is an isometry, and its quotient has a closed timelike curve.
3. **The cosmic-keyed no-CTC result holds at every rank.** The positive-definite Gram argument does not depend on
   latticectc's rank-2 restriction.
