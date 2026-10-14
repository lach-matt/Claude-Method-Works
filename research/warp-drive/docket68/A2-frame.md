# DOCKET 68 · A2-frame — H-FRAME, alone and with the curvature pairing

**Status: a docket work item. Nothing here is seated.** The instrument is `frame.py`, which sits beside this file
and imports `corridors.py` (and through it `latticectc.py`), `frw_frame.py`, `nosig.py`, `nlcontrol.py` and
`../transit.py` rather than copying them. `python3 frame.py --selftest` runs 61 checks and passes all 61
(about 30 s, most of it spent importing the pre-docket scripts, which run their own computations when imported;
re-run in wave 4, whose edits to `frame.py` are grade text only).
Sixteen of those checks are **controls**: cases built to fail, and they do. One more row is printed **STRUCTURAL**
(it cannot fail) and is neither counted nor cited. *Wave 2 first said* 56 checks, 15 controls, and counted that row as
a control. *Wave 1 first said* 47 checks, 13 controls.

**Headline, member-attributed first (wave 3).**
- **H-FRAME alone removes no obstruction a member can claim.** Clause 1 removes O-LOOP only for a keyed network
  (H-KEYING). In exact FRW the corridor removal is the geometry's, credited to no hypothesis.
- **H-FRAME × H-SETTLE-W is PARTIAL, and both members are load-bearing:** O-BITS has **two supports** (wave 4):
  REMOVED-IF {N_EPS, H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK}, window premises
  separate; or REMOVED-IF {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2}, A1's zero-error
  ancilla member, whose window is unevaluated (H-MAP is not established for its field). Signal O-LOOP REMOVED-IF
  {N_SIGKEY}. *Wave 3 first said* the first support only.
- **Clause 2b's D-CTC channel is REMOVED-IF {a CTC at Bob, H-DCTC, C2, H-DCTC-SELECT}**: four axes give 1 pair per
  teleported qubit (zero-error, computed); BHW 0811.1209v2 p.4 (READ) makes the rate unbounded if CTC qubits are a
  free resource, so the route's figure is **≤ 1 pair per teleported qubit, with its minimum OPEN**. O-LOOP is
  reintroduced. *Wave 3 first said* "at 1 pair per teleported qubit (four axes ...)", which read as the route's count.

## M-apply (2026-10-03): M's rulings, and V3's residuals sited here

M's answers (`M-RULINGS-2026-10-03.md`, carried verbatim into CHARTER.md's last section) are rulings and are applied as
worded.

| item | resolution |
|---|---|
| M item 5: O-MATTER is relocated to **O-SEAT, "supply at the seat"** ("Yes, from the seat") | **Applied as a relabel, no grade moves.** Every O-MATTER entry in this file was LEAVES ("says nothing about the seat"), and it stays LEAVES read as O-SEAT: H-FRAME supplies nothing at the seat. What the seat must supply, and the board's prices for it (S13 OPEN, priced; S10 REFUSED), are stated once, in A3-measure.md § (viii), not repeated here. `frame.py` is unchanged: its keys still read "O-MATTER" so that `combine.py`'s imports stay comparable. |
| V3 problem 1 (support 2's field figure, 1.465 vs 1.4306) | Not sited here: this file carries no /s field figure. A2's support-2 premise H-FIELD-W2 already gives the computed range max‖H‖T ≈ 1.43-1.56, and A1 § 1b names which construction gives 1.465 (the four-axis `w2_ancilla_flow`). |
| V3 problem 2 (numbering) | The item numbers in this file's re-verification tables are **1-based**; `V2-0.json` and `V2-1.json` store 0-based arrays, so "V2-0 problem 7" here is `V2-0.json` `problems[6]` (the D-CTC "exact" item). Each row also cites its item by site text. |
| V3 problem 3 (M's rule both ways) | The window is A1's (support 1); `settle.window_given` now flags every open window ADMISSIBLE GIVEN W_W2. In this file's W2 × F1 row the window column already names "the NAMED-NOT-READ values"; read it as: an open window there is **admissible given** those values, flagged, not settled. |

## Wave 4 repair (R3-alone, 2026-10-03): the second pair of re-verifications

V2-0 (AGAINST M) and V2-1 (FOR M), `wave1/REPAIR2-Q1S-RESULT.json` key `result.verify`. Wave 3's forms are kept,
marked *wave 3 first said*.

| re-verification item | resolution |
|---|---|
| V2-0 problem 7: "The D-CTC route is zero-error, so its counts are exact rather than floors" presents one construction's figure (four axes, 2 bits per pair) as the route's count; the clause 2b O-BITS cell likewise | **Applied.** "Exact" holds **for the four-axis construction only**. BHW p.4 (READ): 2ⁿ states carry n bits per qubit, unbounded "if CTC qubits are treated as a free resource"; the W2 ceiling is log₂d per pair. So the class figure is ≤ 1 pair per teleported qubit and its minimum is OPEN. The clause-2b cell now reads "four axes: 1 pair per qubit; unbounded per BHW p.4 if CTC qubits are free". This also *understated* for M (it fixed 1 pair as if it were the route's best), so it is recorded both ways. A k-axis D-CTC table was not computed: `deutsch_fixed_point`'s Cesàro loop on a 16-dimensional CTC (256 × 256 superoperator, 4,000 iterations, 16 branches) was judged too slow for the selftest; the "≤ 1, minimum OPEN" statement rests on the four-axis computation plus BHW p.4 as READ. |
| V2-1 problem 1: "1 pair per teleported qubit" given as what the W2 class does without H-QUBIT-DRIFT (A2:258) | **Applied** (computed in A1 §1b, `settle.w2_ancilla_flow_k`): k = 4, 8, 16, 32 axes give 1, 2/3, 1/2, 0.4 pairs per teleported qubit, zero-error. No positive floor in the computed range. |
| V2-1 problem 2: H-FRAME × H-SETTLE-W's O-BITS removal given one support (headline, Combinations row) | **Applied.** Two supports, as in A1 §5 (R_W2 and R_W2′); grade word unchanged. `frame.py`'s grade text carries both. |
| V2-0 unresolved 3 / V2-1 unresolved 4 | **Answered: OPEN by design, unchanged** (N_QTOPO in the ITB row; the NAMED-NOT-READ values in the window column). |

## Wave 3 repair (2026-10-03): the two re-verifications

| re-verification item | resolution |
|---|---|
| RV-1 #1: clause 2b's O-BITS column reads LEAVES, though its own D-CTC row grades the channel | **Applied.** Clause 2b, O-BITS: **REMOVED-IF {a CTC at Bob, H-DCTC, H-DCTC-CONVENTION C2, H-DCTC-SELECT}**. The BB84 route gives 1.000000 bit per pair (2 pairs per teleported qubit). Four axes give 2.000000 bits per pair (1 pair). Both are zero-error, since every fixed point is unique and P = 1. **O-LOOP is REINTRODUCED.** Under M-S1A-P3 that loop disqualifies the device at the seat only. A CTC is not shown to exist, and Hawking's conjecture stays OPEN. Whether combine carries it is combine's to decide. |
| RV-0 unresolved #4, RV-1 unresolved #0: the four-basis 2 bits/pair figure was cited, not computed | **Applied: computed.** `four_basis_c2_table` runs BHW's general construction (0811.1209v2 pp.3-4, re-READ this pass) on four axes. Bob holds his qubit plus a two-qubit ancilla, so the 8 branch states sit in C⁸, with an 8-dimensional CTC. The map ψ_j → \|j⟩ is reproduced with probability 1 and BHW's condition 2 holds (minimum 0.174). Every fixed point is unique. **I = 2.000000 bits per pair under C2, 0 under C1.** Control: four "choices" naming one axis give 0. |
| RV-0 #7: clause 2b × O-MAKE graded OPEN | **Applied.** It is **NOT-BOUND-IF {clause 2b's CTC; Geroch's compact case only}**. Geroch's "no CTC" hypothesis fails, so the theorem does not bind, and its conclusion is not shown false. Tipler's non-compact case still binds. The release is bought with O-LOOP, which 2b reintroduces. |
| RV-0 #11: the drift-ordering "control" cannot be nonzero | **Applied.** That row integrates the drift on I/2, where H = 0, so it is printed STRUCTURAL. "C2 is undefined without a slicing" is **derived given H-C2's rule**: no branch exists before t_A, so the drift acts on the reduced state. The rule is now named as part of H-C2. |
| RV-0 #12: "Clause 1 removes O-LOOP, at any rank" stated unconditionally | **Applied.** It now reads: "A keyed network (H-KEYING, under H-CORRIDOR-MODEL) closes no causal curve at any rank." Wave 1's form is kept as history. |
| RV-0 #3, RV-1 #9: the FRW removal attributed to hypotheses | **Applied, uniformly.** In exact FRW, corridor O-LOOP is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}. It is the geometry's removal and credited to no hypothesis, so clause 1 adds nothing for corridors there. |
| RV-1 #2: {N_QTOPO, N_CORR} | **Applied.** Under ITB + N_QTOPO, neither the lemma nor latticectc's theorem binds an ITB corridor, so corridor O-LOOP is NOT-BOUND-IF {N_QTOPO}. Signal loops are unchanged. The pair is a premise clash. |
| RV-0 #2: H-FRAME3b is clause 1's substance | **Applied.** In the H-FRAME + H-SETTLE-W row clause 1 is load-bearing: it supplies the drift's slicing. H-SETTLE-W alone leaves O-BITS (A1). |
| RV-1 #3, RV-0 #0: premise sets differ across reports; pair counts read as sufficient | **Applied.** One removal set is used, with window premises in a separate column. Pair counts from N·C ≥ 2 are floors (H-BLOCK). The D-CTC route is zero-error, so its counts are exact rather than floors. *Wave 4: exact for the four-axis construction only; the route's figure is ≤ 1 pair per teleported qubit with its minimum OPEN (BHW p.4; V2-0 problem 7).* |
| RV-1 #0: the W2 "class floor" assumed the drift acts on Bob's qubit only | **Applied** (A1 §1b). That floor is the qubit-only subclass's (H-QUBIT-DRIFT). Without it, A1 computes a W2 member at 1 pair per teleported qubit, zero-error, under H-EXTEND. *Wave 4: that is the four-axis member; with k axes the class reaches 2/(log₂d − 1) pairs, no positive floor computed (A1 §1b).* |

## Wave 2 repair (2026-10-03): what changed, and why

Each verifier problem sited in this work item is listed with its resolution. Wave 1's first forms are kept below,
marked *wave 1 first said*.

| verifier problem | resolution |
|---|---|
| AGAINST #6: `antitelephone` hard-codes the cosmic-frame 0 | **Applied.** `reply_arrival(u)` solves the Lorentz transformation with sympy for any keying frame u. Both values are now computed: −3/5 keyed to the sender, 0 keyed to the cosmic frame. An independent value (u = ½, L = 2 gives −1) is checked. |
| AGAINST #5: the 0.0817 bits and "C2 needs a frame" come from the D-CTC, which needs a CTC at Bob, and clause 1 excludes every CTC | **Applied.** The D-CTC numbers are withdrawn as ground for H-FRAME + H-SETTLE. That row's channel is now nlcontrol's drift, and **the drift's own ordering dependence is computed** (`drift_ordering`): Bob's signal is tanh(2ε(T − t_A)), giving 0.537 with Alice first, 0.291 with Alice at mid-window, and 0 when Bob's window is over first (the drift is computed on his reduced state, not assumed). The D-CTC under C2 gets a row of its own, as a clause-2b world. |
| AGAINST #7: the H-FRAME + H-SETTLE (C2) row lists O-BITS as removed, with no ε condition and no timing | **Applied.** O-BITS is REMOVED-IF {N_EPS (A1: ε > ε_any(L, N)), H-C2, H-BORN-AT-BOB, A1's bound hypotheses}. On A2's own evidence alone it was OPEN. |
| AGAINST #8, REPRODUCE #2: "per BHW p.2 (READ, not computed here) ... 1 bit per pair" labels a derived figure READ | **Applied, and now computed.** BHW's own construction (p.2 Fig. 2 and the p.3 theorem, re-READ) is run through this file's Deutsch fixed point (`bb84_c2_table`). It reproduces the READ map for all four inputs with unique fixed points, and gives **1.000000 bit per pair under C2 and 0 under C1**. |
| FOR #2 (3): "the per-qubit budget under C2 is OPEN" when 1 bit per pair × 2 pairs is arithmetic | **Applied.** The D-CTC under C2 needs 2 pairs per teleported qubit. FOR #2 also reports a four-basis discriminator at 2 bits per pair; that figure is the verifier's computation and was not re-run here. BHW p.4 (READ): a CTC-assisted rate is unbounded. *Wave 3: now computed* (`four_basis_c2_table`, 2.000000 bits per pair). |
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
| Brun, Harrington & Wilde, arXiv:0811.1209v2 | READ (pp.1-4 re-READ in wave 3) | p.2, Fig. 1: SWAP then controlled-H. Input \|0⟩ gives ρ_CTC = \|0⟩⟨0\|, input \|−⟩ gives \|1⟩⟨1\|, and both are unique. p.2, Fig. 2: perfect discrimination of the four BB84 states. pp.3-4: the Theorem for N distinct states in dimension N, and its construction (conditions 1 and 2, the b/c bases), run in `four_basis_c2_table`. p.4: the Holevo bound is broken; unbounded "if CTC qubits are treated as a free resource". |
| Hsu, arXiv:2511.15935v1 | READ, pp.1-3, 5 (wave 3) | Foliation independence of a Weinberg-type term holds only under microcausality, which "cannot be consistently maintained" under state-dependent evolution (p.2). This corroborates that C2 and the drift need a preferred slicing. |
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

1. **A keyed network (H-KEYING, under H-CORRIDOR-MODEL) closes no causal curve at any rank.** *Wave 1 first said*
   "Clause 1 removes O-LOOP, at any rank". The keying is H-KEYING's, not clause 1's (RV-0 #12). If every generator has
   ξ_t = 0, the Minkowski Gram matrix is the
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
  - Alice after Bob's window: 0. This value is the output of H-C2's rule: the drift is integrated on I/2, where
    ⟨X⟩ = 0 and H = 0. It cannot be anything else, so it is printed STRUCTURAL. *Wave 2 first labelled it a CONTROL.*
  - The same events give different predictions in different frames, so **C2 is not well defined without a preferred
    slicing**. This is derived *given* H-C2's rule, that no branch exists before t_A in the chosen frame. The rule is
    a definition inside H-C2, not an output (RV-0 #11). Corroboration, READ in wave 3: 2511.15935v1 pp.1-3. A
    Weinberg-type term is foliation-independent only under microcausality, which "cannot be consistently maintained"
    under state-dependent evolution (p.2).
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

**Four axes (wave 3, computed from BHW's general construction, 0811.1209v2 pp.3-4, READ).** BHW's Theorem builds,
for N distinct states in dimension N, unitaries U_k with U_k ψ_k = \|k⟩ and ⟨j\|U_k\|ψ_j⟩ ≠ 0. This makes the
fixed point unique and the map ψ_j → \|j⟩ exact. `four_basis_c2_table` applies it to Alice's four axes (z, x, y and
(1,1,1)/√3). Bob's qubit with a two-qubit ancilla \|00⟩ carries the 8 branch states in C⁸, and the CTC is
8-dimensional.
- The map is reproduced with probability 1 for all 8 states.
- Condition 2's minimum is 0.174, and every fixed point is unique.
- **I(axis; Bob) = 2.000000 bits per pair under C2**, with zero error. So this four-axis D-CTC construction needs 1
  pair per teleported qubit (wave 4: *this construction*; the route's minimum is OPEN, see the next bullet).
- Under C1: 0 bits. Control: four "choices" naming one axis give 0.
- BHW p.4: 2ⁿ states carry n bits per qubit, unbounded "if CTC qubits are treated as a free resource".

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
| H-FRAME clause 1 + curvature (FRW) | **adds nothing for corridors**: corridor O-LOOP REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL} is the geometry's removal, credited to no hypothesis (the keying is forced; it fails in exact de Sitter, where the matter content, not the geometry, selects the frame) | O-BITS, O-MAKE, O-HOLD, O-MATTER | z3 lemma; the Killing table |
| **H-FRAME + H-SETTLE-W (the drift, under C2)**: both load-bearing | **O-BITS REMOVED-IF {N_EPS, H-C2 (with its no-branch rule), H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK}**; window, separate: {H-MAP, H-TRANSFER, H-SPIN, H-DILUTION, the NAMED-NOT-READ values}; **or (wave 4) REMOVED-IF {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2}**, zero-error, window unevaluated; **signal O-LOOP REMOVED-IF {N_SIGKEY}** | O-MAKE, O-HOLD, O-MATTER (corridor O-LOOP: the geometry's) | settle.py's drift tanh(2εT); `drift_ordering` (C2 undefined without a slicing, derived given H-C2's rule); antitelephone, both values computed: a reply keyed to the sender's frame arrives at t = −3/5 (a loop), keyed to the cosmic frame at t = 0 |
| D-CTC under C2 (a CTC at Bob, so not compatible with clause 1: a clause-2b world) | **O-BITS REMOVED-IF {a CTC at Bob, H-DCTC, C2, H-DCTC-SELECT}**: 0.0817 bits per use (BHW circuit), 1.000 bit per pair (BHW BB84), **2.000 bits per pair (four axes)**, all zero-error, unbounded per BHW p.4 if CTC qubits are free | **O-LOOP REINTRODUCED** (the channel is a CTC; M-S1A-P3: disqualifying at the seat only); O-MAKE NOT-BOUND-IF {its CTC; Geroch-compact only}; O-HOLD, O-MATTER | `signalling_table`, `bb84_c2_table`, `four_basis_c2_table` |
| any of the above × H-IT read as ITB, under N_QTOPO | corridor O-LOOP **NOT-BOUND-IF {N_QTOPO}** (the lemma and latticectc's theorem do not bind an ITB corridor); premise clash {N_QTOPO, N_CORR} | signal loops unchanged | wave 3, RV-1 #2 |
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
- The drift's budget is A1's, and every figure from N·C ≥ 2 is a floor with reliable transfer block-coded (H-BLOCK).
  - nlcontrol's Hamiltonian: ≥ 6.21 pairs on average, ≥ 7 per qubit, never zero-error.
  - The qubit-only subclass (H-BORN-AT-BOB + H-QUBIT-DRIFT): > 2 on average.
  - Without H-QUBIT-DRIFT, computed W2 members need 2/(log₂d − 1) pairs per teleported qubit, zero-error: 1, 2/3,
    1/2, 0.4 at d = 8, 16, 32, 64 (A1 §1b, H-EXTEND) -- no positive floor in the computed range. *Wave 3 first said*
    "a computed W2 member needs 1 pair per teleported qubit".
  - The general W2 capacity is OPEN without H-BORN-AT-BOB.
  - *Wave 2 first said* "> 2 for the W2 class under H-BORN-AT-BOB".
- *Wave 2 first cited* "FOR #2 ... a four-basis discriminator at 2 bits per pair; that figure is the verifier's computation
  and was not re-run here". It is now computed (`four_basis_c2_table`).

## Grades (H-FRAME)

| obstruction | clause 1 alone | clause 2a | clause 2b |
|---|---|---|---|
| O-BITS | LEAVES (computed) | LEAVES | **REMOVED-IF {a CTC at Bob, H-DCTC, C2, H-DCTC-SELECT}**: four axes, 1 pair per qubit (zero-error, computed); unbounded per BHW p.4 if CTC qubits are free -- route figure ≤ 1, minimum OPEN; O-LOOP reintroduced. *Wave 3 first said* "1 pair per teleported qubit (four axes ...)"; *wave 2 first said* "LEAVES; a channel needs H-SETTLE under C2" |
| O-MAKE | LEAVES, and closes the "with a CTC" escape in Geroch's compact case (board grade, not re-read) | LEAVES | **NOT-BOUND-IF {2b's CTC; Geroch-compact case only}**; Tipler's non-compact case still binds; traded for O-LOOP. *Wave 2 first said* "OPEN (a CTC reopens the Geroch clause)" |
| O-HOLD | LEAVES | LEAVES | LEAVES |
| O-MATTER (read as O-SEAT, M item 5) | LEAVES | LEAVES | LEAVES |
| O-LOOP | **REMOVED-IF** {H-CORRIDOR-MODEL, H-KEYING} in the model (a keyed network); in exact flat FRW the corridor removal is the **geometry's**, REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}, credited to no hypothesis (not in exact de Sitter); for signals, REMOVED-IF {N_SIGKEY}; under ITB + N_QTOPO, corridor O-LOOP NOT-BOUND-IF {N_QTOPO} | no loop | **REINTRODUCES** in the model for every T > 0, if corridors are its route (H-2B-VIA-CORRIDOR). Deutsch/Novikov make the loop consistent, not absent; Hawking's conjecture would forbid it (OPEN); M-S1A-P3 disqualifies it at the seat. |

For M's thesis:
- **Clause 1 alone does not touch the two classical bits.** What it does is supply the slicing a drift channel needs,
  and make such a channel chronology-safe, *if* the channel exists. That is why it pairs with H-SETTLE: one supplies
  the channel, the other the slicing and the keying that removes the signal loop.
- **Clause 2b touches the two bits only through a CTC at Bob** (the D-CTC under C2, REMOVED-IF {a CTC at Bob, H-DCTC,
  C2, H-DCTC-SELECT}), and it pays for this by reintroducing O-LOOP.
- *Wave 2 first said* "H-FRAME alone does not touch the two classical bits", which left clause 2b's D-CTC route out.

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
- **H-C2's rule** (wave 3): before Alice measures in the chosen slicing there is no branch, so the drift acts on Bob's
  reduced state.
- **H-BLOCK** (wave 3): reliable transfer is block-coded; pair counts from N·C ≥ 2 are floors.
- **H-FRAME3b ⇐ F1** (wave 3): the drift's preferred slicing is clause 1's substance.
- **a CTC at Bob** (wave 3): clause 2b's D-CTC channel needs one, and none is shown to exist.
- **{N_QTOPO, N_CORR}** (wave 3): a premise clash. An ITB corridor that is not a Lorentzian object cannot also be a
  Lorentzian quotient by translation.
- **H-EXTEND, H-FIELD-W2** (wave 4): the second support of H-FRAME × H-SETTLE-W's O-BITS removal (A1 §5): the field
  computed on the ancilla member's disjoint curves extends smoothly (derived, not computed), and its strength
  max‖H‖T ≈ 1.43-1.56 is available within the drift time (no bound maps onto it; H-MAP not established).

## Findings (recorded, not repaired)

1. **`frw_frame.py` rebinds its module-global `g` to Minkowski** for its final control. Any importer that calls
   `frw_frame.lie_g` after importing it gets the Minkowski Lie derivative unless it restores `g`. The script's
   own printed output is correct. `frame.py` restores `g` around its calls and then puts it back.
2. **The charter's FRW reading holds for ΛCDM but not in the exact de Sitter limit.** There a time-shifting
   dilation is an isometry, and its quotient has a closed timelike curve.
3. **The cosmic-keyed no-CTC result holds at every rank.** The positive-definite Gram argument does not depend on
   latticectc's rank-2 restriction.
