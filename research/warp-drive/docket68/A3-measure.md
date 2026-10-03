# DOCKET 68 · A3-measure: Q-1 (the substrate-free measure), H-INFO and R-INDEX

**Status: a docket work item. Nothing here is seated.** The instrument is `measure.py`, which sits beside this file.
`python3 measure.py --selftest` runs 58 checks, and all 58 pass in about 13 s. Sixteen of the checks are
**controls**: cases built to fail, and every one of them fails. The instrument imports everything it uses and
copies nothing:

- `tools/cypher.py` for Λ;
- `nopath`, `massform`, `stock`, `wormhole` and `transit` for every board figure;
- `nlcontrol.py` for the drift model.

It writes nothing outside `docket68/`.

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
finding. Inverted, the bound gives an **exchange-rate floor**: E ≥ I ħc ln 2/(2πR) is the least total gravitating
energy of a complete system that holds I bits.

**Control.** Taking R in centimetres moves the figure by a factor of 100, and the check flags it.

**The object.** A 70 kg body. stock.HUMAN gives 6.7117e27 atoms and 1.4168 species bits per atom. The counts carry
the named hypotheses H-LISTED, H-RHO, H-GRID and H-THERMO:

| count (named hypotheses) | bits | Landauer, 310 K | Landauer, T_CMB | Bekenstein floor, R = 1 m | classical bits to teleport (H-FAITHFUL) |
|---|---|---|---|---|---|
| species sequence (H-LISTED) | 9.509e27 | 2.82e7 J | 2.48e5 J | 33 J | 1.90e28 |
| grid at 1 Å (H-GRID, H-RHO; 9.6 % of sites filled) | 4.142e28 | 1.23e8 J | 1.08e6 J | 144 J | 8.28e28 |
| grid at 0.1 Å (H-GRID, H-RHO) | 1.088e29 | 3.23e8 J | 2.84e6 J | 379 J | 2.18e29 |
| thermal entropy as water (H-THERMO; the datum is NAMED-NOT-READ, so the figure is CONDITIONAL) | 2.840e28 | 8.43e7 J | 7.41e5 J | 99 J | 5.68e28 |

**Control.** A 3 Å grid cannot seat the atoms (fill > 1), and the check flags it.

The four counts span one decade, 9.5e27 to 1.1e29 bits. That spread **is H-ALT made visible**: the measure is
exact once the alternatives are fixed, and the alternatives for an object are a choice.

Against the board's geometric prices (imported, not re-graded):

| board price | joules |
|---|---|
| O-HOLD: `wormhole.throat_mass(1 m)·c²` | 4.8155e42 |
| O-MAKE: `nopath.coincidence_mass()·c²` (Proxima, contraction) | 4.8707e59 |
| O-MATTER: Mc² (`massform.rest_energy_j`) | 6.2913e18 |
| O-MATTER: the (B, L)-conserving floor (`massform.pair_floor_j`) | 1.2567e19 |

Every count lies below the Bekenstein ceiling of 1.80e45 bits and far below the light-sheet cap for a 1 m sphere,
1.735e70 bits (`nopath.holographic_bits`).

The largest erasure price at 310 K, 3.2e8 J, is **1.5e34 times smaller** than the 1 m throat. **This is the
"costs little" half of M's thesis, priced:** the information that defines the object is cheap at every exchange
rate. Two things keep that from being over-read:

- It prices the information, not the corridor.
- Under H-FAITHFUL it must still be *sent*, at 2 classical bits per qubit, through a channel no faster than light
  (`transit.BEATS_LIGHT` is False; imported).

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
- **O-LOOP** is left: the measure is silent, because it has no time variable.

Under "Holding it open" in the charter's corridor replies, M says *"This is simply a translation of information
only. No physics. The null energy doesn't exist here"*. That is true *of the measure*. It is not yet true of the
corridor.

### R-INDEX: **PARTIAL**

BFL's objects are finite probability spaces. Inside the measure there is no stress tensor, no metric and no
manifold, so neither Morris-Thorne's NEC nor Geroch's theorem can even be stated.

- **O-HOLD and O-MAKE are not expressible in the measure.** They are therefore removed *within the measure*. That
  becomes a *physical* removal only under H-IT. What happens to them is that they **move to the exchange rate**:
  - the holding price becomes the Bekenstein floor, 33-379 J for the counts above at R = 1 m, against the 4.8e42 J
    throat;
  - erasure moves to Landauer;
  - transfer moves to Holevo.
- **Energy and geometry re-enter at the exchange rate, not as an NEC.** Bekenstein's E is the *gravitating* energy
  and R is a radius in asymptotically flat spacetime (READ p.1-2). The exchange rate that prices holding is stated
  in geometric terms.
- **R-INDEX leaves O-BITS.** A cell's bits must still be sent: 2 log₂ d classical bits per qudit, and nothing at all
  without a sent system.
- **R-INDEX leaves O-MATTER.** A holder with at least 2^I distinguishable states must be at the destination, and
  Bekenstein's E counts its rest energy (pp.2, 8).
- **R-INDEX leaves O-LOOP.** The measure has no time coordinate, so it is silent on loops and decides nothing about
  them.

## Combinations, per the standing instruction

**H-SETTLE × H-INFO: complementary obstructions, and computed.** The O-BITS bound read above rests on causality
(BSST p.3). H-SETTLE breaks the linearity behind that premise. With `nlcontrol.py`'s model imported, Bob's two
ensembles carry the following Holevo information, under the named hypothesis H-BORN-AT-BOB (Bob's final measurement
follows the Born rule):

| ε | χ_Bob, bits per use | trace distance | uses needed for the 1 Å count |
|---|---|---|---|
| 1e-3 | 6.49e-6 | 3.00e-3 | 6.4e33 |
| 1e-2 | 6.48e-4 | 3.00e-2 | 6.4e31 |
| 1e-1 | 5.71e-2 | 0.269 | 7.3e29 |

- The linear control gives exactly 0 at every ε.
- For small ε, χ scales as ε²: the ratio between ε = 1e-2 and ε = 1e-3 is 99.9.
- Each use consumes one pre-shared pair, and the pairs had to cross the distance first (`transit.py`: the traversal
  is moved earlier, not removed).
- So in this model, H-SETTLE is the member that could remove O-BITS. Its capacity is priced by Q-1, and its supply
  of pairs reintroduces transit.

**H-INFO × H-ZERO: tested at the source, and narrowed.** Bekenstein p.1 takes E as the gravitating energy precisely
to "dispose of any ambiguity" about the zero, and p.8 includes the ground-state energy. So relabelling the zero
cannot lower the Bekenstein exchange rate within general relativity. Whether it can in the emergent paradigm
(H-IT; Padmanabhan & Padmanabhan, as the charter reads it) is **OPEN**.

**H-INFO × R-QUANTUM.** A memory entangled with the system lowers erasure below zero: the work cost is H(S|O) kT
ln 2, so a Bell pair yields kT ln 2 (del Rio). This is a real quantum discount on the Landauer exchange rate, but
the protocol acts on S and O jointly. Whether a spatially separated, LOCC version keeps the discount is **OPEN**
here. It carries no signalling: S(A|B) = −1 is a property of the joint state.

**H-NULL × H-INFO.** These are cross-referenced only. The counts (≤ 1.1e29 bits) sit about 41 orders below the
light-sheet cap of a 1 m sphere. That is not a test of the QNEC pricing in `nullinfo.py`.

## Testable predictions

1. **Any signalling channel shows up in the superdense test.** Any channel in which Bob's statistics depend on
   Alice's choice, with nothing sent, would give χ_Bob > 0 in that test. Linear QM gives 0, which is computed. In
   nlcontrol's drift, a measured χ_Bob per use would bound ε through χ ≈ 6.5 ε² bits (small ε, T = 3).
2. **Nothing satisfies Theorem 2's axioms except c·ΔH.** Any functional on FinProb that satisfies all three axioms
   and is not c·ΔH would refute the theorem. All four non-Shannon controls fail an axiom.
3. **Landauer has a measurable floor.** A measured mean erasure heat below kT[ln 2 + p ln p + (1−p) ln(1−p)], with no
   quantum side information, would refute Landauer. Bérut's 0.72 ± 0.15 kT is consistent with it.
4. **Under R-INDEX with H-IT, holding has a floor.** Holding the definition of a 70 kg body at R = 1 m needs a
   complete system of total gravitating energy at least 33-379 J, depending on the count. Bekenstein forbids any
   holder below that.

## What was not done

- **No z3 screen.** R-INDEX's "no energy term" claim is structural: BFL's objects are (X, p). Nothing in this work
  item needed a decision procedure, and the docket's 127-combination screen is not attempted here.
- **H-THERMO's datum is not read at source.** The entropy of water, 69.95 J/(mol·K), was not read, so that row is
  conditional on it.
- **H-RHO is a round assumption.**
- **The O-LOOP grade is "silent".** It is not a decision; `frame.py` (A2) owns it.
- **The task's file list named `docket68/undefined`.** That is a script fault in the computed task text. The
  instrument is named `measure.py`, as the body of the task asked.
