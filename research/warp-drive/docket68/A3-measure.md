# DOCKET 68 · A3-measure: Q-1 (the substrate-free measure), H-INFO and R-INDEX

**Status: a docket work item. Nothing here is seated.** The instrument is `measure.py`, which sits beside this file.
`python3 measure.py --selftest` runs 86 checks. Thirteen are printed **STRUCTURAL**: they cannot fail by construction
(a literal, a comparison of typed values, or two runs of one expression), so they are **not counted** and are not cited
as evidence. **The 73 counted checks all pass** (about 30 s); nineteen of them are **controls**: cases built to fail,
and every one of them fails. *Wave 4 first-said record:* the summary printed "85/85 pass" with six STRUCTURAL inside
the 85; wave 4 relabels six checks of § (vii) STRUCTURAL (V2-0 problem 5), adds one STRUCTURAL guard for the
symmetric rule, and prints the counted total.
*Wave 1 first said* "58 checks ... Sixteen of the checks are controls", and four of those sixteen were structural.
*Wave 3 first said* "65 checks ... Fifteen ... controls ... Five ... STRUCTURAL"; the Q-1s integration (§ (vii)) added
20 checks, 4 controls and 1 structural.
The instrument imports everything it uses and copies nothing:

- `tools/cypher.py` for Λ;
- `nopath`, `massform`, `stock`, `wormhole` and `transit` for every board figure;
- `nlcontrol.py` for the drift model;
- `signed.py` (Q-1s, `Q1s-signed.md`) for the signed measure, imported lazily inside the functions that use it,
  because `signed.py` itself imports this file inside two of its functions.

It writes nothing outside `docket68/`.

**Headline, member-attributed first (wave 3).**
- Nothing in this work item removes an obstruction that a member can claim. Q-1, H-INFO and R-INDEX are each
  LEAVES-ALL.
- **H-SETTLE × H-INFO adds nothing to H-SETTLE-W.** The drift's O-BITS removal is H-SETTLE-W × H-FRAME's (A1, A2).
- H-INFO-S is a **CLASH** with B-RECV, and it stays M's to rule.
- R-INDEX's NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} is in a column of its own -- on O-MAKE, O-HOLD **and (wave 4)
  corridor O-LOOP** -- and so is the geometry's corridor O-LOOP removal, which is credited to no hypothesis.
- **Q-1s is now in use (§ (vii)).** Q-1 takes signed cell weights under H-SIGNED-CELLS, and returns Shannon exactly
  when no weight is negative. **No grade moves**; each was re-examined, and the reason it does not move is recorded.

## Wave 4 repair (R3-alone, 2026-10-03): the second pair of re-verifications

V2-0 (AGAINST M) and V2-1 (FOR M), `wave1/REPAIR2-Q1S-RESULT.json` key `result.verify`. Earlier forms are kept,
marked *wave 3 first said* or *Q1s-integrate first said*.

| re-verification item | resolution |
|---|---|
| V2-0 unresolved 2 / V2-1 unresolved 1 and problem 4: the symmetric corridor rule (RV-1 #2) is applied in A1, A2, A4 but not to A3's R-INDEX, which writes O-LOOP "SILENT; corridors: geometry column" while granting O-MAKE and O-HOLD NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} | **Applied.** For a physical corridor under R-INDEX: **O-LOOP-C NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL}**. The loop theorems (the exact-FRW keying lemma, latticectc) are statements about Lorentzian quotients, so the reason that unbinds the NEC and Geroch unbinds them too: one reason, one verdict. It is not a removal, and the conclusion is not shown false. It sits beside the geometry's REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL} in the other account, with the premise clash **{N_MEASPHYS, N_CORR}** as combine already encodes it (z3: O-LOOP-C NOT-BOUND-IF {ITB, RI; N_MEASPHYS}). Signal loops are unchanged. Within the measure O-LOOP stays SILENT. Carried in § (iv), § (vii)'s table, `measure.GRADES`, `Q1S_GRADE_REVIEW` and `A3-measure.json`. **For combine's stage:** `combine.EXPLAINED[("A3-measure", "ITB+RI", "O-LOOP")]` now names a disagreement that no longer exists, so combine's "no stale whitelist entry" check will report it until that stage removes the entry; this stage does not edit `combine.py`. |
| V2-0 problem 1: Kontsevich's appendix (math/0008089v1 pp.43-44) already claims the unique continuous solution on all of R; prior art list too narrow | **READ at source this pass, and applied** (Q1s-signed.md § 4c). Uniqueness of Re H under signed-weight recursivity (Kontsevich's (A), (B), symmetry, continuity on R) is **CLAIMED-IN-LITERATURE**, as a cohomological sketch; under BFL's convex-linear axioms it is derived here for separable functionals and OPEN otherwise. § (vii) and `Q1S_GRADE_REVIEW` say so. |
| V2-1 problem 5: the lawful-family result is confined to a 12-functional dictionary; the separable extension was sketched but not done | **Done in `signed.py` § (4b)**, every step shown, the algebraic steps machine-checked by z3 with vacuity and encoding guards, the solution identity by sympy. Over every continuous separable functional the lawful family is span{Re H, N}. **H-INFO clause (a) on signed weights moves from OPEN to SUPPORTED-IF {H-SEPARABLE, BFL's codomain dropped, product additivity}**, and is impossible inside H-SEPARABLE if the codomain is kept; OPEN over non-separable functionals. No obstruction grade moves; one clause status does. |
| V2-0 problem 5: § (vii)'s recovery checks counted as passes and cited as evidence ("recovered exactly"), though none can fail | **Applied.** Five checks (SHANNON routing, Re H == H, M == 0, signed loss == F_shannon, uniform Λ == log₂976) and the n = 1 check are printed STRUCTURAL and not counted. **That Re H = H on non-negative p is definitional** (the same float expression). The checks that carry content are boundary continuity, the clip-and-renormalise control, the H-NORM refusal and the closed-form agreement. 73 counted, 13 STRUCTURAL. |
| V2-0 unresolved 3 / V2-1 unresolved 4: N_MEASPHYS has no READ source | **Answered: OPEN by design, unchanged.** It is named in every R-INDEX non-binding, never cited as evidence. |

## Q-1s integration (2026-10-03): what changed, and why

M, in the charter: *"Let's create the instrument and implement its use."* `signed.py` was built in Q1s-build; this
pass puts it to use in Q-1. What was added to `measure.py`, all of it in section (vii):

| added | what it does | what checks it |
|---|---|---|
| `q1(p)` | Q-1 on a cell weighting. If no weight is negative, the case is **SHANNON** and the value is H(p), with the signed quantities alongside. If some weight is negative, the case is **SIGNED**: (Re H, Im H = πN, N, M) from `signed.py`, under H-SIGNED-CELLS, and no Shannon value is offered. A total other than 1 is refused (H-NORM). | On 301 vectors with no negative weight Re H equals H bit for bit, Im H = 0, N = 0, \|M\| ≤ 1.1e-14 nats -- **definitional, printed STRUCTURAL in wave 4** (*Q1s-integrate first said* "recovered **exactly**" as a result). Two controls carry the content: a weighting with one negative entry is routed SIGNED and differs from the clip-and-renormalise value; a total of 2 is refused. |
| `signed_loss` | Re H(p) − Re H(f₊p), the signed analogue of the BFL loss | equal to `F_shannon` bit for bit on 300 random FinProb morphisms (STRUCTURAL in wave 4: the same expression). Control: it leaves Theorem 2's codomain [0, ∞) on signed morphisms. |
| `boundary_continuity` | a weight crossing zero from below | the signed case joins the Shannon case: the Re H gap falls 4.9e-2 → 2.3e-9 over e = 1e-2 … 1e-10, and Im H and M → 0 |
| `holder_ceiling` | whether Re H keeps Shannon's ceiling ln n | computed on `signed.py`'s extremal vectors, each evaluated by `q1` |
| `rindex_signed` | R-INDEX on Λ with signed cell weights (H-MOBIUS-WEIGHT, `signed.lambda_mobius`) | reproduces Q1s-build's recorded figures; control: a full box gives a one-point weight, case SHANNON |
| `Q1S_GRADE_REVIEW` | each A3 grade, re-examined | every grade is covered and every verdict is unchanged (STRUCTURAL: a comparison of typed values) |

`signed.py` gained one keyword, `lambda_mobius(..., vectors=True)`, which returns the two normalised weightings so that
`q1` evaluates them itself. Nothing else in `signed.py` changed.

## Wave 3 repair (2026-10-03): the two re-verifications

| re-verification item | resolution |
|---|---|
| RV-0 #6: H-SETTLE × H-INFO graded PARTIAL, "complementary obstructions", but H-INFO contributes nothing | **Applied.** The verdict is now **LEAVES-ALL, adding nothing to H-SETTLE-W**. The χ in this file is nlcontrol's Holevo information, which is H-SETTLE-W's alone, counted in Q-1's unit, so H-INFO is not load-bearing. The drift's removal needs a preferred slicing (H-FRAME3b ⇐ F1) and so belongs to H-SETTLE-W × H-FRAME, with one removal set: {N_EPS, H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM, H-BORN-AT-BOB, H-BLOCK}. The window premises {H-MAP, H-TRANSFER, H-SPIN} are kept separate. |
| RV-0 #13: "a measured 6.4920"; prediction 1 omits H-C2 | **Applied.** The value now reads "integrated (nlcontrol)", in the text and in `measure.py`'s check. Prediction 1 now reads: under H-C2 and H-NLCONTROL-FORM, χ_Bob bounds ε through χ ≈ 6.5ε²; under C1 a null result does not bound ε. |
| RV-1 #6: clash (d) carries conditions named nowhere beside it | **Applied** (§ H-INFO-S). B-RECV's conditions are listed beside the clash: C3, P-UNIFORM and H-UNSOURCED-SEAT (LEDGER S10 and D27, READ); Bekenstein's scope; and what φ(1) = 0 does and does not require. **The clash stays a CLASH for M to rule.** Encoding B-RECV with a premise would let H-INFO-S remove O-MATTER by assertion, which would over-represent in the other direction. |
| RV-1 #9: LEAVES-ALL rows do not carry the geometry's O-LOOP | **Applied.** Each LEAVES-ALL row's O-LOOP is SILENT within the measure. For a physical corridor in exact FRW it is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}, by the geometry, credited to no hypothesis. |
| RV-0 unresolved #4: N_MEASPHYS has no READ source | **Answered.** That is correct, and it is what the grade says. H-MEASURE-PHYSICAL is a named hypothesis carried so the grade can state what a removal would take. It is never cited as evidence, and the obstruction stays NOT-BOUND-IF, not REMOVED. |

## Wave 2 repair (2026-10-03): what changed, and why

| verifier problem | resolution |
|---|---|
| AGAINST #1: R-INDEX "removes" O-HOLD and O-MAKE within the measure because they are not expressible, while O-LOOP's inexpressibility is called silence | **Applied.** One reason gets one verdict: within the measure, O-HOLD, O-MAKE and O-LOOP are all **SILENT**. For a physical corridor, the NEC and Geroch are **NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL}**, never REMOVED: showing a theorem cannot be stated in a formalism is not showing its conclusion false. R-INDEX alone is **LEAVES-ALL**. The Bekenstein floor belongs to the destination holder (O-MATTER). |
| AGAINST #0 (sited in combine; it cites this file): B-THROAT reads "physical only under H-IT" as sufficiency | **Answered at the source.** Here H-IT is *necessary*. Sufficiency would need H-MEASURE-PHYSICAL ("under H-IT, the measure-level absence of an NEC is physical"), which no instrument or READ source supplies. It is named so the grade can say what it would take. |
| AGAINST #9: lower bounds read as costs ("the 'costs little' half, priced") | **Applied.** Every joule figure is a **floor**. Landauer prices *erasure*, which teleportation does not require. Bekenstein floors a holder's gravitating energy. No upper bound on any cost is computed. The one READ-backed holder, the body, has Mc² = 6.29e18 J. "Costs little" is **floored, not priced**. |
| AGAINST #14: H-SETTLE × H-INFO "removes O-BITS in nlcontrol's model only", with no distance in the model and C2 unnamed | **Applied.** The model shows a channel **exists**: χ = (2T)²ε²/(8 ln 2) per use for small ε, coefficient 6.49 at T = 3 (computed, and it matches χ(1e-3)/1e-6 = 6.4920). This holds under H-C2; under C1 there is none. O-BITS is REMOVED-IF {N_EPS (A1's timing), H-C2, H-BORN-AT-BOB, H-FRAME3b}. *Superseded in wave 3:* the pair adds nothing to H-SETTLE-W, and the removal is H-SETTLE-W × H-FRAME's (RV-0 #6). |
| FOR #8: H-INFO's sufficiency reading was never screened, so "O-MATTER survives because none of the seven touches it" is not established | **Applied.** H-INFO-S is graded: a **CLASH** with B-RECV, not a removal (`info_s_clash`). |
| FOR #0 (sited in combine): rule-2 retirement of H-INFO rests on an inert encoding | **Recorded here.** H-INFO is exercised in this file (it reprices nothing and removes nothing). Combine's verdict that it is "not load-bearing" is UNTESTED-BY-SCREEN, because its MEASURE atom is in no constraint. Retirement is not established. |
| (rule: vacuous controls) four wave-1 controls could not fail | **Applied.** They are now printed STRUCTURAL. One of them (the mis-stated identity) was given content: a mis-stated line, parsed by `read_identity`'s own pattern, must fail the comparison with cypher's computation. |

M's request, quoted from the charter: *"We need to quantify information, unambiguously and independently of all
cosmic/quantum physicalities"*. H-INFO and both readings are carried as M's hypotheses. Each is graded on what it
does, and none is treated as a result.

## Sources (M-D67-2: arXiv is the object)

| source | status | what was taken, where |
|---|---|---|
| Baez, Fritz & Leinster, arXiv:1106.1791v3 | READ (re-read this pass) | **Thm 2, p.4.** Three axioms: functoriality (1), convex linearity (2) and continuity. Continuity is defined on p.4: fixed sets, a fixed function, and p(n)→p pointwise. Conclusion: F(f) = c(H(p) − H(q)), c ≥ 0, with a converse. **Def 1, p.3:** FinProb, whose morphisms are measure-preserving *functions*. **Eq. (5), p.6:** the loss is a conditional entropy. **Thms 5-6, pp.7-8:** Faddeev and the grouping rule. **p.8:** φ(nm) = φ(n) + φ(m), so φ(n) = c ln n. **Thm 7, p.10:** Tsallis entropy at homogeneity degree α. Shannon 1948 and Faddeev 1956 are NAMED-NOT-READ (both are restated here). |
| Parzygnat, arXiv:2009.07125v3 | READ | **Thm 1.4 = Thm 4.26 (pp.3, 24):** the von Neumann entropy difference is the unique continuous, orthogonally affine fibred functor on NCFinProb with H_A ≥ 0 and H_A = 0 on pure states. **p.2:** the quantum entropy difference "need not have a fixed sign", and Landauer "could fail for quantum systems". |
| Holevo, arXiv:quant-ph/9611023v1 | READ | **p.2:** the entropy bound C ≤ max ΔH. **p.3, Theorem:** C = max_π [H(Σπ_i S_i) − Σπ_i H(S_i)]. Holevo 1973 itself is NAMED-NOT-READ (it is this paper's ref. [7]). |
| Bennett, Shor, Smolin & Thapliyal, arXiv:quant-ph/9904023v5 | READ | **p.1:** prior entanglement "by itself ... confers no ability to transmit classical information", and C_E = 2C for any noiseless channel. **p.2:** C₁ ≤ log₂ d − S̄. **p.3:** "the FCCC of simulating a quantum channel cannot be less than its classical capacity; otherwise a violation of causality would occur". Bennett & Wiesner 1992 is NAMED-NOT-READ and READ-VIA-RESTATEMENT (p.1). |
| Bennett, arXiv:physics/0210005v2 | READ | **p.1:** Landauer's principle covers logically irreversible manipulation; logically reversible steps "can in principle" be thermodynamically reversible. **p.4:** a merge costs k ln 2. Landauer 1961 is NAMED-NOT-READ and READ-VIA-RESTATEMENT. |
| Bérut, Petrosyan & Ciliberto, arXiv:1503.06537v1 | READ (the measured test; the Nature 2012 letter is its ref. [3], NAMED-NOT-READ) | **p.2:** at least k_BT ln 2 per bit, "∼ 3 × 10⁻²¹ J at room temperature". **p.3, eq. (1):** the generalised bound. **p.13:** "≈ 0.19 k_BT" at P = 80 %. **p.14:** the fitted asymptote A = 0.72 k_BT. **p.13:** error bars ±0.15 k_BT. |
| del Rio, Åberg, Renner, Dahlsten & Vedral, arXiv:1009.1630v2 | READ | **pp.2-4:** W(S\|O) = H(S\|O) kT ln 2. A Bell-pair memory gives H(S\|Q) = −1 and a net work *gain* of kT ln 2. The observer acts on S and O jointly, "not restricted to LOCC" (p.3). |
| Bekenstein, arXiv:quant-ph/0404042v1 | READ (the board grade is D67 **NARROWED**, `docket67-raw/GRADES.tsv:96`) | **Eq. (1), p.1:** S ≤ 2πER/ħc. E is "the gravitating energy", which "disposes of any ambiguity" about the zero of energy (p.1). **p.2:** valid "for complete, weakly self-gravitating, isolated objects". **p.8:** E "must include the ground state energy". |
| The Method, `method/members/The_Method_1_6-2.md` line 4 | READ (targeted, not scanned) | "6,912 = 976 + 0 + 5,936". Register 833 per the Physics Compendium (line 22). |

No host refused a request in this pass. Every alphaXiv call returned content.

## (i) Q-1: the measure exists, and it is substrate-free

Theorem 2's characterisation is verified computationally on random finite spaces, with a fixed seed.

- **Functoriality.** Maximum error 4.4e-16.
- **Convex linearity.** Maximum error 7.8e-16. It is also checked **symbolically** (sympy, exact) on a generic map
  `3→2 ⊕ 2→1`, with an encoding-drift guard against the operator the report uses.
- **Continuity.** It is probed where it is hardest: a point whose mass goes to 0. The gap falls from 4.9e-2 to
  2.3e-9 over ε = 1e-2 … 1e-10.
- **Non-negativity.**
- **The uniform case.** φ(nm) = φ(n) + φ(m) holds for all n, m ≤ 30 (error 1.5e-13). φ(n) = ln n, and
  φ(n+1) − φ(n) → 0.
- **Other identities.** Faddeev's grouping rule, eq. (5), and uniqueness: c fitted on one morphism predicts every
  other (c = 1/ln 2 = 1.442695 in bits).

**Controls.** Each must fail, and each does:

- squared loss fails functoriality;
- Rényi-2 fails convex linearity, and its one-morphism fit fails elsewhere (error 0.277);
- Tsallis-2 fails degree-1 convex linearity, and its symbolic identity does not vanish;
- Hartley-of-support fails continuity (a jump of ln(3/2) = 0.405) and convex linearity.

There is also one **positive control**: Tsallis-2 passes Theorem 7's degree-2 rule, as BFL say it must.

**Theorem 2's hypotheses, re-checked.** These are what Q-1 inherits, stated exactly.

- **H-FINITE.** The theorem covers finite sets and measure-preserving *functions*, which are deterministic. It does
  not cover continuous spaces or stochastic maps.
- **H-UNIT.** The constant c is not fixed by the theorem; choosing bits is choosing a unit.
- **H-ALT.** The theorem names no physical quantity, so it is substrate-free (p.3-4). It also does not say **which
  alternatives count as distinguishable, nor with what probabilities.** This is where physics re-enters.
- **The quantum case** is a different theorem (Parzygnat). There, BFL's non-negativity fails: an entropy
  difference can be negative.

So M's request is met up to the unit and the choice of alternatives, and no further. The charter already named
this boundary.

## (ii) The Method's closed index: where H-ALT is settled

`cypher._lambda()` is imported, not copied, and it **computes** |Λ| = 976 and box = 6,912. Its order operator gives
E(Λ) = 0, so refused = 5,936. The identity read from the live volume matches this computation exactly.

Under **H-UNIFORM** (every admitted cell equiprobable):

| quantity | value |
|---|---|
| log₂ 976, bits per cell of Λ | 9.930737 |
| log₂ 6,912, bits per cell of the box | 12.754888 |
| log₂(6,912/976), the bits the envelopes' closure supplies | 2.824150 |
| strong additivity on the corpus's own partition | H(box) = H₂(976/6912) + (976/6912)·log₂ 976 + (5936/6912)·log₂ 5936 = 12.754887502163, exact |

**Bound.** Any non-uniform measure on the 976 cells gives fewer bits. The largest of 50 random measures gave 9.68.
On this index the alternatives are fixed by the coordinate list, so the count is unambiguous. For a physical object
they are a choice, which (iii) makes visible.

## (iii) The exchange rates, and the price of an object

**Holevo.**

- χ ≤ log₂ d − S̄ holds on 200 random ensembles at d = 2, 4 and 8.
- **Control: counting labels.** The four BB84 states on one qubit carry 2 bits of labels but χ = 1 bit = log₂ 2.
  Counting labels instead of distinguishable states breaches the bound, and the check catches it.
- **Superdense coding.** χ of the four joint states, after Alice *sends* her qubit, is 2.000000 bits, which is
  C_E = 2 log₂ 2.
- **Prior entanglement alone.** χ of Bob's qubit when nothing is sent is 0, exactly as BSST p.1 states.
- **Control: a channel.** When Alice's choice *is* delivered to Bob, χ_Bob = 1, so the test does detect a channel.
  (An earlier version of this control applied the Pauli to Bob's own half of the Bell pair. It wrongly gave 0: a
  local unitary leaves a maximally mixed marginal unchanged. That version was replaced and is recorded here.)
- **transit.py's 2 bits per qubit.** transit.py records CLASSICAL_BITS_PER_QUBIT = 2 as DECLARED. It now has a READ
  lower bound behind it: FCCC ≥ C_E = 2 log₂ d (BSST p.3). The bound is argued *from causality*.

**Landauer.** kT ln 2 is:

- 2.9667e-21 J at 310 K (H-TBODY);
- 2.8710e-21 J at 300 K (Bérut: "∼ 3 × 10⁻²¹ J");
- 2.6083e-23 J at T_CMB (`nopath.T_CMB`).

Bérut's generalised bound at P = 0.80 recomputes as 0.1927 kT (the paper gives ≈ 0.19). Their asymptote, 0.72 kT,
lies within ±0.15 kT of ln 2.

**Control.** A "measured" 0.5 kT at full efficiency is flagged as below the bound.

**H-ERASE.** Landauer prices only *erasure*; copying and holding can be reversible (Bennett p.1).

**Quantum side information.** With an entangled memory, erasure can *yield* work: S(A|B) of a Bell pair is −1 bit
(computed). This requires joint operations on S and O.

**Bekenstein.** `massform.bekenstein_bits()` gives 1.8038e45 bits for 70 kg at R = 1 m, matching the board's READ
finding. Inverted, the bound gives a **floor**: E ≥ I ħc ln 2/(2πR) is the least total gravitating energy of a complete
system that holds I bits. It is a property of the holder, which bears on O-MATTER. It is not a price paid, and it is
not the cost of holding a corridor open.

**Control.** Taking R in centimetres moves the figure by a factor of 100, and the check flags it.

**The object.** A 70 kg body. stock.HUMAN gives 6.7117e27 atoms and 1.4168 species bits per atom. The counts carry
the named hypotheses H-LISTED, H-RHO, H-GRID and H-THERMO:

Every joule column is a floor:

| count (named hypotheses) | bits | Landauer floor, 310 K | Landauer floor, T_CMB | Bekenstein floor, R = 1 m | classical bits to teleport (H-FAITHFUL) |
|---|---|---|---|---|---|
| species sequence (H-LISTED) | 9.509e27 | 2.82e7 J | 2.48e5 J | 33 J | 1.90e28 |
| grid at 1 Å (H-GRID, H-RHO; 9.6 % of sites filled) | 4.142e28 | 1.23e8 J | 1.08e6 J | 144 J | 8.28e28 |
| grid at 0.1 Å (H-GRID, H-RHO) | 1.088e29 | 3.23e8 J | 2.84e6 J | 379 J | 2.18e29 |
| thermal entropy as water (H-THERMO; the datum is NAMED-NOT-READ, so the figure is CONDITIONAL) | 2.840e28 | 8.43e7 J | 7.41e5 J | 99 J | 5.68e28 |

**Control.** A 3 Å grid cannot seat the atoms (fill > 1), and the check flags it.

The four counts span one decade, 9.5e27 to 1.1e29 bits. That spread **is H-ALT made visible**: the measure is
exact once the alternatives are fixed, and the alternatives for an object are a choice.

Against the board's geometric figures (imported, not re-graded):

| board figure | joules |
|---|---|
| O-HOLD: `wormhole.throat_mass(1 m)·c²` | 4.8155e42 |
| O-MAKE: `nopath.coincidence_mass()·c²` (Proxima, contraction) | 4.8707e59 |
| O-MATTER: Mc² (`massform.rest_energy_j`) | 6.2913e18 |
| O-MATTER: the (B, L)-conserving floor (`massform.pair_floor_j`) | 1.2567e19 |

Every count lies below the Bekenstein ceiling of 1.80e45 bits and far below the light-sheet cap for a 1 m sphere,
1.735e70 bits (`nopath.holographic_bits`).

**Floors, not prices (wave 2).** *Wave 1 first said:* "The largest erasure price at 310 K, 3.2e8 J, is 1.5e34 times
smaller than the 1 m throat. This is the 'costs little' half of M's thesis, priced: the information that defines the
object is cheap at every exchange rate." That treated lower bounds as costs. What the computation shows:

- **Landauer.** Erasing the count would cost **at least** 2.8e7-3.2e8 J at 310 K, and teleportation need not erase at
  all (H-ERASE).
- **Bekenstein.** A holder at R = 1 m must have **at least** 33-379 J of gravitating energy.
- **No upper bound on any cost is computed here.** No instrument exhibits a holder near its floor. The one READ-backed
  holder, the body itself, has Mc² = 6.29e18 J (`massform`).
- **So "costs little" is floored, not priced.** The floors sit 1.5e34 (Landauer) and 1.3e40 (Bekenstein) below the
  board's 1 m throat figure. That is a comparison of floors with a board figure, not of cost with cost.
- Under H-FAITHFUL the information must still be *sent*, at 2 classical bits per qubit, through a channel no faster
  than light (`transit.BEATS_LIGHT` is False; imported).

## (vii) Q-1s in use: R-INDEX with signed cell weights

**The hypothesis.** H-SIGNED-CELLS: a cell weighting on R-INDEX may be a quasi-probability. Its weights are real,
total exactly 1 (H-NORM, enforced), and some may be negative. Its Q-1 value is then `signed.py`'s (Re H, Im H = πN,
N, M = ln Σ|p|) on the principal branch (H-PRINCIPAL). *Which* signed weighting is meant is a further choice; here
it is `signed.py`'s H-MOBIUS-WEIGHT. **Λ itself carries no negative probability.** A signed weighting is a
decomposition of Λ, not a measurement of it.

**The ordinary case: definitional, not a result (wave 4).** When no weight is negative, `q1` reports case SHANNON,
and on p ≥ 0 Re H **is** H: `signed.re_h` runs the same float expression as this file's H, Im H is π times an empty
sum and N is 0. So "Re H equals H bit for bit on 301 vectors", "M = 0 up to the rounding of Σp" and "the signed loss
equals `F_shannon` bit for bit on 300 morphisms" cannot fail, and are printed STRUCTURAL and not counted. *Q1s-integrate
first said* "Control: the ordinary case is recovered exactly ... These checks can fail" (V2-0 problem 5). **What can
fail, and carries the content:** a weight crossing zero from below joins the Shannon case continuously (the Re H gap
falls 4.9e-2 → 2.3e-9); a weighting with one negative entry, (0.5, 0.6, −0.1), is routed SIGNED with Im H > 0 and M > 0,
and its Re H (0.422810 nats) differs from the clip-and-renormalise Shannon value (0.918428 nats), which is what a
dispatcher that ignored the sign would have returned; a total of 2 is refused (H-NORM); and the extremal vectors
evaluated by `q1` agree with `signed.reh_bounds`' closed form.

**On Λ (COMPUTED).**

| weighting (hypothesis) | case | cells | Re H, bits | Im H | N | M, bits |
|---|---|---|---|---|---|---|
| uniform (H-UNIFORM) | SHANNON | 976 | 9.930737 | 0 | 0 | 0 |
| Möbius p (H-MOBIUS-WEIGHT) | SIGNED | 317 | 0 (every \|p\| = 1) | 496.3716 = 158π | 158 | 8.3083 = log₂ 317 |
| box mixture q (H-MOBIUS-WEIGHT) | SIGNED | 317 | −3.033176 | 256.6643 | 81.6988 | 7.3610 |
| full box (control) | SHANNON | 1 | 0 | 0 | 0 | 0 |

The figures match Q1s-build's (N = 158, Re H = 0, M = 8.308 bits; Re H = −3.033 bits, N = 81.70). The uniform row is
§ (ii)'s log₂ 976.

**What does not carry from § (i). It is computed, not asserted.**
- **Theorem 2's codomain fails.** Crushing (1.5, −0.5) to a point has signed loss **−0.954771 nats**. Merging
  (1.6, −0.3, −0.3) to (1.6, −0.6) has loss −0.6 ln 2 = −0.415888 nats, with N unchanged. A measure-preserving map can
  *raise* Re H, so Q-1's uniqueness (Theorem 2) is **not inherited** by signed weights (H-FINSIGNED). What replaces it
  (Q1s-signed.md § 4, 4b, 4c; wave 4):
  - **over every continuous separable functional** X = Σ g(p_i) (H-SEPARABLE), BFL's functoriality, convex linearity
    and continuity force **X = c Re H + b N** (derived step by step; the algebraic steps machine-checked by z3, the
    solution identity by sympy). Product additivity then leaves **Re H alone**; keeping BFL's codomain leaves only
    b N (b ≥ 0), which vanishes on probabilities;
  - **under signed-weight recursivity** (Kontsevich's (A), (B), symmetry, continuity on all of R) the uniqueness of
    Re H on two entries is **CLAIMED-IN-LITERATURE**: math/0008089v1 p.43, READ, a cohomological sketch;
  - **over non-separable functionals under BFL's axioms, uniqueness is OPEN**: convex linearity does not reach a
    signed atom such as (1.5, −0.5), and about half of random three-entry signed measures are such atoms.
  *Wave 3 first said* "Within a 12-functional dictionary the lawful family is span{Re H, N} ... Over all continuous
  functionals, uniqueness is **OPEN**."
- **Re H has no ceiling ln n.** These values come from `signed.py`'s extremal vectors, each evaluated by `q1` and
  agreeing with the closed form to 1e-9:
  - **n = 1:** the only weighting with total 1 is (1), so Re H = 0 = φ(1), signed or not.
  - **n = 2:** Re H < 0 at every N tested (−0.9548, −1.9095, −3.3510, −5.6102 nats at N = 0.5, 2, 10, 100).
  - **n = 3:** the extremal (P/2, P/2, −N) has Re H = 0.1699, 4.2736 and 64.3977 nats at N = 2, 10 and 100, against
    ln 3 = 1.0986. Re H grows without bound in N.
  - **n = 5:** Re H already exceeds ln 5 at N = 2 (2.2493 nats).
  So "I bits at the destination need at least 2^I states" holds for Shannon only. Read as information, Re H would bound
  no holder's size. But Re H's operational meaning is **OPEN** (Q1s-signed.md, OPEN 6). The finding therefore neither
  weakens B-RECV nor supports H-INFO-S; it is not to be read either way.

**Grades re-examined (`Q1S_GRADE_REVIEW`). None moves.**

| grade | verdict | why it does not move |
|---|---|---|
| Q-1 | LEAVES-ALL | The signed measure counts, as Q-1 does. It sends no bit, holds no throat, forms no matter, closes no loop. Only its scope changes: Theorem 2's uniqueness covers the SHANNON case only; for signed weights uniqueness holds over separable functionals (Re H with product additivity), is CLAIMED-IN-LITERATURE under signed recursivity (Kontsevich), and is OPEN otherwise. |
| H-INFO | LEAVES-ALL | Clause (a) was already scoped to probability measures (BFL's hypotheses, READ pp.3-4). For signed weights (wave 4): **SUPPORTED-IF {H-SEPARABLE, BFL's codomain dropped, product additivity}** -- Re H is then the unique measure, and those hypotheses name only finite sets, signed measures and functions; **impossible** inside H-SEPARABLE (and inside H-DICTIONARY) if the codomain is kept; OPEN over non-separable functionals. *Wave 3 first said* "SUPPORTED for probability weights and OPEN for signed ones". One clause status moves; the verdict does not. Clause (b) is untouched: Re H gives no lower bound per unit matter either. |
| H-INFO-S | CLASH | φ(1) = 0 survives signed weights (n = 1 above). The 2^I leg is Shannon's (n = 3 above), and Re H's meaning is OPEN. The clash stays M's to rule. |
| R-INDEX | LEAVES-ALL | Its values are (Re H, Im H, N, M). None is an energy density: a negative weight is not a negative T_ab k^a k^b. So O-HOLD stays SILENT within the measure, and NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} for a corridor. To read a negative weight as the throat's null deficit (one reading of M's "supplied by probability in the citation/seating") is **H-NEGWEIGHT-NEC**: named, with no instrument and no source, and not credited. O-BITS: a signed weighting sends nothing. O-MATTER: unchanged. O-LOOP: SILENT within the measure; for a physical corridor O-LOOP-C NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL}, as O-MAKE and O-HOLD (wave 4; *wave 3 first said* "O-LOOP: SILENT"). |
| H-SETTLE × H-INFO | LEAVES-ALL | Its χ is a Holevo quantity of density matrices, whose spectra are non-negative. No signed weight enters it. |

## (iv) Grades

### Q-1 (the measure), alone: **LEAVES-ALL**

The measure is delivered, but a measure counts; it moves nothing. It sends no bit, holds no throat, forms no matter,
and neither closes nor opens a loop.

### H-INFO, alone: **LEAVES-ALL**

H-INFO has two clauses.

- **Clause (a)**, that information can be quantified independently of physicalities, is **supported** by the
  theorem, up to H-UNIT and H-ALT.
- **Clause (b)**, that matter cannot exist without information, is **OPEN**. The measure assigns 0 bits to a
  one-point space. Nothing read here gives a *lower* bound on information per unit matter; Bekenstein's is an upper
  bound.

Per obstruction, alone:

- **O-BITS** is left. BSST p.1 says prior entanglement alone carries no classical information, and χ_Bob = 0 is
  computed.
- **O-MAKE** and **O-HOLD** are left: a premise about primacy is not a mechanism.
- **O-MATTER** is left. Bekenstein's bound applies to a complete system with E > 0, which must hold the bits.
- **O-LOOP** is SILENT: the measure has no time variable. It is left, not decided. In the geometry column, credited to
  no hypothesis: for a corridor in exact FRW it is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}.

H-INFO is exercised here and removes nothing. That is not a retirement under rule 2: combine's screen encodes it
inertly, so its result there is UNTESTED-BY-SCREEN.

### H-INFO-S, the sufficiency reading (wave 2): **CLASH with B-RECV**

M's premise read as sufficiency: information at the destination **suffices** to constitute the matter. The charter
gives the textual ground: "only the information defining it is necessary"; "the only multi-universal currency".
Against the board holding B-RECV (a holder must be at the destination), computed in `info_s_clash`:

- Q-1 gives a one-state destination **0 bits** (φ(1) = 0). Control: a two-state destination holds 1 bit. So I > 0 bits
  at the destination needs a holder with at least 2^I distinguishable states already there.
- Bekenstein admits **0 bits at E = 0** (`nopath.bekenstein_bits`). Within its scope (READ p.2), information
  presupposes gravitating energy at the destination.
- `transit.CARRIES_SUBSTANCE` is False: the protocol moves a state into a receiver that is already there.

H-INFO-S says the arriving information suffices; B-RECV says a holder must already be there. As commitments they
clash. Nothing computed here shows information constituting its own holder. So O-MATTER is **CLASH**: REMOVED-IF
{H-INFO-S} holds only on a board without B-RECV. O-MATTER's survival is therefore a board-versus-M clash, not
something "none of the seven touches". The z3 screen of that clash (combine's clash (d)) belongs to combine and is not
run here.

**B-RECV's conditions, listed beside the clash (wave 3, RV-1 #6).** The clash stays a **CLASH, for M to rule**. These
are what a ruling for H-INFO-S would have to overturn. O-MATTER's survival is unchanged.

| B-RECV rests on | its condition | where |
|---|---|---|
| S10 (atomic mass formed at the seat: REFUSED) | **C3**: holds for renormalisable couplings, dimension ≤ 4. "a higher-dimension operator carrying B or L would reverse it". | `LEDGER.md:67` (READ) |
| | **P-UNIFORM**: the vev takes one value wherever nothing sources it. A named premise, M-D65-4. | `LEDGER.md:50` (D27), `:181` (READ) |
| | **H-UNSOURCED-SEAT**: nothing holds a source at the seat before arrival. Where it fails, what remains is the held-seat release route S13, OPEN, priced, and forming no baryons. | `LEDGER.md:67`, `:70` (READ) |
| Bekenstein's bound (0 bits at E = 0) | scope: "complete, weakly self-gravitating, isolated objects" (p.2); E is the **gravitating** energy (p.1), a geometric quantity | quant-ph/0404042v1 (READ) |
| Q-1, φ(1) = 0 | needs **2^I distinguishable states at the destination**. It does not by itself require that those states be matter already there; "the holder's states are material" is a further premise of B-RECV. *(Q-1s:)* φ(1) = 0 holds for signed weights too; the 2^I leg is Shannon's, because signed Re H on 3 cells has no ceiling (§ (vii)) | BFL 1106.1791v3 pp.3-4 (READ); computed here |
| transit.py | `CARRIES_SUBSTANCE = False`: the protocol moves a state into a receiver that is already there (a property of linear-QM teleportation) | imported |

Under "Holding it open" in the charter's corridor replies, M says *"This is simply a translation of information
only. No physics. The null energy doesn't exist here"*. That is true *of the measure*. It is not yet true of the
corridor.

### R-INDEX: **LEAVES-ALL** (wave 1 first said PARTIAL)

BFL's objects are finite probability spaces. Inside the measure there is no stress tensor, no metric and no
manifold, so neither Morris-Thorne's NEC nor Geroch's theorem can even be stated.

- **O-HOLD and O-MAKE are SILENT within the measure, exactly as O-LOOP is.** A formalism that cannot state a theorem
  is silent on it.
  - *Wave 1 first said* they "are therefore removed *within the measure*. That becomes a *physical* removal only under
    H-IT ... the holding price becomes the Bekenstein floor". One reason gave two verdicts (AGAINST #1).
- **For a physical corridor: NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL}.** H-IT is necessary but not sufficient. The
  second premise, that the measure-level absence of an NEC is a fact about the corridor, is supplied by no instrument
  and no READ source. Not bound is not removed.
- **The exchange rates are floors.** Erasure goes to Landauer and transfer to Holevo. The Bekenstein floor (33-379 J
  at R = 1 m) bounds the **destination holder**, so it bears on O-MATTER, not on holding a corridor open. Nothing here
  prices holding a corridor open.
- **Energy and geometry re-enter at the exchange rate, not as an NEC.** Bekenstein's E is the *gravitating* energy
  and R is a radius in asymptotically flat spacetime (READ p.1-2). The exchange rate that prices holding is stated
  in geometric terms.
- **R-INDEX leaves O-BITS.** A cell's bits must still be sent: 2 log₂ d classical bits per qudit, and nothing at all
  without a sent system.
- **R-INDEX leaves O-MATTER.** A holder with at least 2^I distinguishable states must be at the destination, and
  Bekenstein's E counts its rest energy (pp.2, 8).
- **O-LOOP is SILENT within the measure; for a physical corridor, O-LOOP-C is NOT-BOUND-IF {H-IT,
  H-MEASURE-PHYSICAL}** (wave 4, the symmetric rule). The measure has no time coordinate, so it is silent on loops. The
  corridor loop theorems -- the exact-FRW keying lemma and latticectc's theorem -- are statements about Lorentzian
  quotients, so the same reason that unbinds the NEC and Geroch for an R-INDEX corridor unbinds them: one reason, one
  verdict. Not a removal; the conclusion is not shown false. Signal loops are unchanged. In the other account,
  credited to no hypothesis: for a physical corridor in exact FRW it is REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER,
  H-CORRIDOR-MODEL}; the two accounts rest on clashing premises, **{N_MEASPHYS, N_CORR}** (combine's z3: O-LOOP-C
  NOT-BOUND-IF {ITB, RI; N_MEASPHYS}). Combined with H-IT read as ITB under N_QTOPO it is NOT-BOUND-IF {N_QTOPO}, and
  {N_QTOPO, N_CORR} is a premise clash.
  - *Wave 3 first said* "**R-INDEX leaves O-LOOP.** The measure has no time coordinate, so it is silent on loops and
    decides nothing about them", granting O-MAKE and O-HOLD the non-binding but not O-LOOP (V2-0 / V2-1).

## Combinations, per the standing instruction

**H-SETTLE × H-INFO: computed, and it adds nothing to H-SETTLE-W. Verdict LEAVES-ALL (wave 3).** The O-BITS bound read
above rests on causality (BSST p.3), and H-SETTLE breaks the linearity behind that premise. With `nlcontrol.py`'s model
imported, Bob's two ensembles carry the Holevo information in the table below. That information is H-SETTLE-W's,
counted in Q-1's unit. H-INFO changes nothing in it, so H-INFO is not load-bearing and this is not a complementary
pair.
- The drift's O-BITS removal needs a preferred slicing (H-FRAME3b ⇐ F1). It is therefore H-SETTLE-W × H-FRAME's
  (A1 §5, A2), with two supports (wave 4): REMOVED-IF {N_EPS, H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-NLCONTROL-FORM,
  H-BORN-AT-BOB, H-BLOCK}, or REMOVED-IF {H-C2, H-FRAME3b ⇐ F1, H-COHERE, H-BORN-AT-BOB, H-EXTEND, H-FIELD-W2} (A1's
  zero-error ancilla member; window unevaluated). *Wave 3 first said* the first support only (V2-1 problem 2).
- The window premises {H-MAP, H-TRANSFER, H-SPIN} are separate.
- *Wave 2 first said* "complementary obstructions, and computed. Verdict PARTIAL: O-BITS REMOVED-IF {N_EPS, H-C2,
  H-BORN-AT-BOB, H-FRAME3b}" (RV-0 #6).

The named hypotheses of the computation are:
- H-BORN-AT-BOB: Bob's final measurement follows the Born rule;
- **H-C2**: the drift acts on the branch state. *Wave 1 first omitted it.* Under C1 χ = 0.

| ε | χ_Bob, bits per use | trace distance | uses needed for the 1 Å count |
|---|---|---|---|
| 1e-3 | 6.49e-6 | 3.00e-3 | 6.4e33 |
| 1e-2 | 6.48e-4 | 3.00e-2 | 6.4e31 |
| 1e-1 | 5.71e-2 | 0.269 | 7.3e29 |

- The linear control gives exactly 0 at every ε.
- For small ε, χ scales as ε²: the ratio between ε = 1e-2 and ε = 1e-3 is 99.9.
- Each use consumes one pre-shared pair, and the pairs had to cross the distance first (`transit.py`: the traversal
  is moved earlier, not removed).
- For small ε the law is χ = (2T)²ε²/(8 ln 2). The computed coefficient is 6.4921 at T = 3, against 6.4920 integrated
  by nlcontrol. *Wave 2 first wrote* "against a measured 6.4920", which read as experimental (RV-0 #13).
- **What the model shows is that a channel exists.** nlcontrol has no distance, so "before light" is not defined
  inside it. The O-BITS removal needs A1's timing condition (N_EPS: ε > ε_any(L, N)) and H-C2.
  - *Wave 1 first said* "removes O-BITS, in nlcontrol's model only, at a priced capacity".
  - The capacity figures are nlcontrol's single Hamiltonian's (H-NLCONTROL-FORM). A1 §1b computes the W2 class.
- Its supply of pairs reintroduces transit.

**H-INFO × H-ZERO: tested at the source, and narrowed. On obstructions it adds nothing: neither member removes one,
and the pair removes none.** Bekenstein p.1 takes E as the gravitating energy precisely
to "dispose of any ambiguity" about the zero, and p.8 includes the ground-state energy. So relabelling the zero
cannot lower the Bekenstein exchange rate within general relativity. Whether it can in the emergent paradigm
(H-IT; Padmanabhan & Padmanabhan, as the charter reads it) is **OPEN**.

**H-INFO × R-QUANTUM.** A memory entangled with the system lowers erasure below zero: the work cost is H(S|O) kT
ln 2, so a Bell pair yields kT ln 2 (del Rio). This is a real quantum discount on the Landauer exchange rate, but
the protocol acts on S and O jointly. Whether a spatially separated, LOCC version keeps the discount is **OPEN**
here. It carries no signalling: S(A|B) = −1 is a property of the joint state. On obstructions the pair adds nothing.

**H-NULL × H-INFO.** These are cross-referenced only. The counts (≤ 1.1e29 bits) sit about 41 orders below the
light-sheet cap of a 1 m sphere. That is not a test of the QNEC pricing in `nullinfo.py`. The pair adds nothing on
obstructions.

## Testable predictions

1. **Any signalling channel shows up in the superdense test.** Any channel in which Bob's statistics depend on
   Alice's choice, with nothing sent, would give χ_Bob > 0 in that test. Linear QM gives 0, which is computed.
   **Under H-C2 and H-NLCONTROL-FORM**, a measured χ_Bob per use would bound ε through χ ≈ 6.5 ε² bits (small ε,
   T = 3). **Under C1, χ = 0 for every ε, so a null result does not bound ε.** *Wave 2 first said* "In nlcontrol's
   drift, a measured χ_Bob per use would bound ε", without naming H-C2.
2. **Nothing satisfies Theorem 2's axioms except c·ΔH.** Any functional on FinProb that satisfies all three axioms
   and is not c·ΔH would refute the theorem. All four non-Shannon controls fail an axiom.
3. **Landauer has a measurable floor.** A measured mean erasure heat below kT[ln 2 + p ln p + (1−p) ln(1−p)], with no
   quantum side information, would refute Landauer. Bérut's 0.72 ± 0.15 kT is consistent with it.
4. **Any holder has a floor.** Holding the definition of a 70 kg body at R = 1 m needs a complete system of total
   gravitating energy at least 33-379 J, depending on the count; Bekenstein forbids any holder below that. This is a
   floor on the destination holder (O-MATTER). It is not a price, and it does not need R-INDEX or H-IT. *Wave 1 first
   said* "Under R-INDEX with H-IT, holding has a floor".

## What was not done

- **No z3 screen.** R-INDEX's "no energy term" claim is structural: BFL's objects are (X, p). Nothing in this work
  item needed a decision procedure, and the docket's 127-combination screen is not attempted here.
- **H-THERMO's datum is not read at source.** The entropy of water, 69.95 J/(mol·K), was not read, so that row is
  conditional on it.
- **H-RHO is a round assumption.**
- **The O-LOOP grade is "silent" within the measure.** It is not a decision; `frame.py` (A2) owns it. In wave 2,
  O-HOLD and O-MAKE take the same word within the measure; in wave 4, corridor O-LOOP takes the same NOT-BOUND-IF as
  they do for a physical corridor.
- **H-INFO-S's clash is not z3-screened here.** It is graded from computed facts (φ(1) = 0, Bekenstein at E = 0,
  `transit.CARRIES_SUBSTANCE`); the screen is combine's.
- **Q-1s: what stays OPEN.** Uniqueness of a signed measure over all continuous NON-separable functionals under BFL's
  axioms (*wave 3 first said* "over all continuous functionals"; the separable case is now derived, and the
  recursive case is claimed by Kontsevich). The operational meaning
  of Re H when some weight is negative. Which signed weighting of Λ, if any, The Method means (H-MOBIUS-WEIGHT is one
  choice among many). H-NEGWEIGHT-NEC has no source. None of `signed.py`'s literature was re-read in this pass; it is
  cited as Q1s-build READ it (Q1s-signed.md § 6).
- **The task's file list named `docket68/undefined`.** That is a script fault in the computed task text. The
  instrument is named `measure.py`, as the body of the task asked.
