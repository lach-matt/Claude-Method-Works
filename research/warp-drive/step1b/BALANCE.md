# Step 1b — the balanced equation (first pass, 2026-10-05)

Instrument: `step1b/balance.py` (`--selftest`: 33/33 pass, 5 of them controls, 1 STRUCTURAL item printed and not
counted). It reads the research tree and writes nothing. Every figure is imported from its owner: `measure.py`,
`seat.py`, `transit.py`, `massform.py`, `stock.py`, `nopath.py`.

## M's definition (docket68/M-RULINGS-2026-10-03.md, items 29–30, verbatim)

> Balanced means that the value of the object at first position must equal the value of the object at the second
> position. And any variable input must be accounted for in output

On what the value is, M: "Information only".

So: **I(A, before) = I(B, after)**. Every matter and energy term is an input or an output, and every input must be
accounted for by some output.

## What it computes

**The value.** I is counted four ways, under the hypotheses `measure.py` names. M's words do not fix which count is the
object's information (H-WHICH-COUNT), so all four are carried: species sequence 9.509e27 bits, 1 Å grid 4.142e28,
0.1 Å grid 1.088e29, thermal entropy 2.84e28.

**Does the value balance?** Two readings are carried.
- R-QUANTUM (teleportation, `transit.teleport`, over 400 random states):
  - With the two bits sent, B's least fidelity is 1.000000000000.
  - A's four outcomes are equiprobable for every state, with largest deviation 2.2e-16. The record alone holds no I.
  - With the bits withheld, B's fidelity is 0.5 for every state, because B holds I/2. Without the channel the value
    does not balance.
- R-CLASSICAL: I bits are sent. A classical record can be copied, so I(A) does not fall to zero by sending it.

**A finding that holds on both readings.** Teleportation moves state, not species (`transit.CARRIES_SUBSTANCE =
False`). So the classical part of I, the species sequence, is still present at A after the transfer. The object at A
leaves only through an output term: OUT-A-RESIDUE, A's 70 kg retired as stock at A. If that term is left out, the
balance holds and the object is at both positions. M's condition, "either at the beginning or end position, never in
between", therefore needs that output term. The value equation does not supply it.

**Conserved quantities.** These are a consistency column, not the value. The object has 6.712e27 atoms,
2.313e28 electrons (Z read via `massform.Z_OF`), mass number ~4.215e28 (H-BARYON-BY-MASS) and charge 0. The column
closes site by site, and **the transfer of every conserved quantity from A to B is 0**: only I crosses. At B the closure
is D25's stock gate. The CI-chondrite feedstock is 749.1 kg, with phosphorus (P) as the binder and a residue of
679.1 kg. P is measured nowhere in the Proxima system (`seat.P_MEASURED_IN_PROXIMA_SYSTEM = False`), so the closure at
B is OPEN there. This column closes by construction, so it is printed as STRUCTURAL and not counted.

**The equation's terms.** For every count and reading, every input is accounted for by an output (checked). Two
controls guard the check: dropping the ebit output leaves IN-EBITS unaccounted and is caught, and filling the OPEN
energy terms with 0 makes the total computable.

**Not totalled.** Two energy terms are OPEN: reading I at A (IN-A-READ) and assembling at B (IN-B-ASSEMBLE, E_rec,
already OPEN in `seat.py`). The energy to retire A's instance is OPEN inside OUT-A-RESIDUE. No energy total is printed,
and none may be quoted. The channel is priced per schedule only (`seat.channel_floor`). Species-sequence count, 1D
one-polarisation floor:

| reading | in 1 yr | in 100 yr |
|---|---|---|
| R-CLASSICAL | 1.39e14 J | 1.39e12 J |
| R-QUANTUM | 5.55e14 J | 5.55e12 J |

There is no floor independent of the schedule. Erasure terms are floors that apply only if a record is erased; a kept
record is itself the output. These floors are B's register reset at 2.725 K (≥ 2.48e5 J, under H-RESET) and A's
record or copy at 310 K (≥ 2.82e7 J for I bits).

## Named hypotheses

H-WHICH-COUNT, H-INFO-SHAPE (M, items 1 and 5), H-SAME-COMPOSITION, H-SAME-ISOTOPES (a mass-energy difference, not
computed), H-BARYON-BY-MASS, H-RESET, H-ERASE-RECORD, and H-ONE-POSITION. H-ONE-POSITION is M's: "The two positions
technically exist as one". The board's channel reading, `transit.BEATS_LIGHT = False`, is recorded beside it and not
graded, because M has said "speed is not a question in my work".

## OPEN

1. Which count is the object's definable condition information (H-WHICH-COUNT).
2. Energy to read I at A, to retire A's instance, and to assemble at B (E_rec).
3. The D25 gate at Proxima: P is unmeasured.
4. Isotope ratios between A's object and B's stock (H-SAME-ISOTOPES).

## History

- First written expecting B's fidelity with the bits withheld to be 2/3. That is the best measure-and-prepare fidelity,
  a different quantity. The check failed, and the value is 1/2 for every state, since B holds I/2.

## Compensation (M, item 31) — `step1b/compensate.py`, 18/18 pass, 3 controls

M: "Be sure to account for compensation in the physics.... Let's say mass energy density is different at the seat, but
some other discrepancy makes up of that and dissolves the defect...". This is carried as H-COMPENSATION. The file tests
four places where the physics itself compensates, and the rule that limits them.

- **(C1) Frame: dissolved by B's stock.** The object's rest mass is the same at both ends, but its energy in the Sun's
  frame is not, so a defect appears between the two positions.
  - A, Earth's surface: ε_A = −5.061e8 J/kg.
  - B, Proxima b: ε_B ranges from −2.19e9 to +9.01e8 J/kg. The inputs are Proxima's space velocity of 32.51 km/s
    (Kervella et al. 2017, arXiv:1611.03495v3, Table B.1, READ), b's orbital speed of 47.2 km/s, and the potentials
    of Proxima, the Sun and α Cen AB. b's orbital phase is unknown, and its mass is a minimum.
  - The defect for 70 kg runs from −1.18e11 to +9.85e10 J.
  - When the object is built from B's stock, the defect is **dissolved**: the stock already moves with B and sits in
    B's potential, so the residual is 0. The control: the same object shipped from A leaves the whole defect standing.
- **(C2) Negative energy at the seat: quantum interest** (Ford & Roman, gr-qc/9901074v1, READ). Here the physics does
  what M describes, but never exactly. A negative-energy defect must be repaid by positive energy that overcompensates
  it by a fraction ε > 0. Exact compensation (ε = 0) admits no non-trivial pulse.
  - The repayment must arrive within T_max = 0.338 (A/|E|)^(1/3). For 1 J over 1 m², that is 3.56e-18 s.
  - At a separation of 1e-19 s, ε ≥ 6.0e-8, and ε grows as T⁶.
  - Eq. 39's limit is re-derived numerically from F(α).
  - This is proved for a massless scalar field in flat spacetime (H-QI-SCOPE). At the seat it is a hypothesis.
- **(C3) The value: redundancy.** A noisy channel's bit errors are a defect in I(B). Redundancy dissolves it, at
  I/(1 − h₂(p)) channel bits (Shannon's binary symmetric channel). The redundant bits are an input, and they are
  discarded at B as an output. At p = 0.11 the channel needs about 2× the bits. At p = ½ nothing compensates.
- **(C4) What cannot compensate what.** Compensation works only within one conserved currency: energy for energy,
  bits for bits. Energy cannot dissolve a baryon, lepton or charge defect. Making baryons from energy makes antibaryons
  too (`massform.pair_floor_j` = 1.99748 Mc²), so it creates an equal and opposite defect rather than dissolving one.
  At B such a defect is dissolved only by stock that carries that charge, which is D25's gate again.

## Retiring the original at A (M, item 32)

Asked whether the original at A is taken apart into stock, so the object exists only at B, M answered: "I suspect so,
to satisfy the no-cloning clause." This is carried as M's hypothesis **H-RETIRE-A** ("I suspect", so a hypothesis and
not a result). Its term is OUT-A-RESIDUE. The energy to retire the original is OPEN.

What `balance.py` computes beside it (`no_cloning`; 35/35 pass):
- **No-cloning binds the quantum part.** Over 400 random pairs of states, the overlap gap |⟨ψ|φ⟩| − |⟨ψ|φ⟩|² stays
  above 0, with least value 0.00208. So no single unitary can clone both states of a pair. Teleportation already
  satisfies this: A's outcomes are equiprobable, so no copy of the state is left at A.
- **No-cloning does not bind the classical part.** CNOT onto a blank copies both basis states exactly. A classical
  description, such as the species sequence, copies freely.

So no-cloning accounts for the quantum state, and teleportation already meets it. The classical description is a
different matter: what keeps it at one position is retiring A's matter, which is M's condition "either at the beginning
or end position, never in between". No-cloning does not require it. M's reason is right for the quantum part and does
not reach the classical part. The retirement is needed either way.

## Pricing the three OPEN energy terms — `step1b/openterms.py`, 13/13 pass, 2 controls

M: "Continue by necessity to the current place of work". The current place is Step 1b, and its energy column was
refused because three terms were OPEN. They are now bounded. None of them is a single value, so the total is still
refused.

- **(T1) Reading at A.**
  - Theorem floor: **0 J**. Measurement can be reversible; only erasing the record has a Landauer price, and that is
    already in the equation (Bennett, physics/0210005v2, READ by `measure.py`).
  - Probe floor, under H-PROBE and H-ONE-QUANTUM: one quantum per atom, at a wavelength no longer than the pitch,
    over 6.712e27 atoms. In the table, "> D_max" means each quantum carries more energy than the strongest chemical
    bond (11.16 eV).

| carrier | at 1 Å | at 0.1 Å | > D_max |
|---|---|---|---|
| photon | 12.4 keV per quantum, 1.33e13 J | 1.33e14 J | yes |
| electron | 150 eV per quantum, 1.62e11 J | 1.62e13 J | yes |
| neutron | 82 meV per quantum, 8.8e7 J | 8.8e9 J | no |

- **(T2) Retiring A (H-RETIRE-A).**
  - Chemistry is bounded by ±3.60e10 J. That is (v_max N/2) × D_max, where v_max = 6 is a hypothesis (H-VALENCE)
    and D_max is the CO bond (READ: 1077 kJ/mol and 1072 kJ/mol; the larger is used).
  - The sign depends on the stock's chemical form (H-STOCK-FORM).
  - **Compensation (M, item 31):** a photon or electron read at atomic pitch carries more than D_max per quantum. Its
    total is 4.5× to 3,700× the whole chemical ceiling. So, if those quanta are absorbed in the object (H-ABSORB),
    **the read itself supplies the energy to take A apart**, and the retire term is dissolved by the read term.
  - Control: a neutron read at 1 Å carries 82 meV per quantum, below D_max, so it does not dissolve the term.
- **(T3) Assembling at B (E_rec).**
  - Chemistry is bounded by ±3.60e10 J. B's register reset costs at least 2.48e5 J (H-RESET). Placement is OPEN:
    no floor is established.
  - The chemical ceiling lies below the payback ceiling from `seat.py` at every speed it lists. The ratio is 2.8e-7
    at β = 0.2 and 1.1e-4 at β = 0.01. The payback ceiling is the E_rec below which building from B's stock ever beats
    shipping the payload at that speed.
  - **Global compensation:** if A's residue and B's stock are in the same chemical form, the chemistry at A and at B
    is one rearrangement run in reverse. It cancels in the global column. Locally, though, B is left a deficit of up
    to 3.60e10 J, which B's surroundings must supply (OPEN).

History: the first selftest asserted that ratio was below 1e-4 at every speed. At β = 0.01 it is 1.14e-4, so the
guessed threshold failed while the finding held. The check now asserts what is shown: below 1 at every speed.

## B's local supply against Proxima's light — `step1b/bsupply.py`, 8/8 pass, 2 controls

M: "I agree, continue". `openterms.py` leaves B a local deficit: the chemistry, up to its ceiling, when A's residue and
B's stock share a form. Here it is set against Proxima's own light.

- **Flux at b's orbit:** 924 W/m², with a range of 577–1270 W/m². The inputs are L* = 0.0016 ± 0.0006 L☉ (READ: Faria
  et al. 2022, arXiv:2202.05188v1, Table 1 p.2, citing Boyajian et al. 2012) and a = 0.04856 au. The control: the
  same expression at 1 au gives the solar constant, 1361 W/m². b sits inside the READ habitable-zone range.
- **Time to gather each local term at B** (central L*, efficiency 1, so these are the shortest times; H-COLLECT):

| term | energy | 1 m² | 100 m² | 10⁴ m² |
|---|---|---|---|---|
| chemical deficit ceiling | 3.60e10 J | 1.24 yr | 4.5 days | 65 min |
| register reset floor | 2.48e5 J | 269 s | 2.7 s | 0.03 s |
| *scale only:* payload rest energy | 6.29e18 J | 2.2e8 yr | 2.2e6 yr | 2.2e4 yr |
| *scale only:* E_rec payback ceiling at β = 0.01 | 3.15e14 J | 1.1e4 yr | 108 yr | 1.08 yr |

- **The chemical deficit at B can be met by Proxima's light.** A 100 m² collector gathers it in under a week. The
  low and high L* cases scale every time by 1.60 and 0.73.
- **Not established here:** the energy of placement (still OPEN), and any collector at B. The fabricator, survey and
  receiver of D23 all arrive no earlier than light (seat.py).

History:
- `openterms.py` was first written as `step1b/terms.py` (d79aa3b). It was renamed because the board already holds a
  `terms.py`, which shadowed it when `bsupply.py` imported it. Its content did not change.
- `bsupply.py`'s first selftest asserted the reset floor is gathered "in under a minute". It takes 269 s, so the
  guessed threshold failed while the finding held. The check now compares the reset floor with the chemical term.
