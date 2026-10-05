# Step 1b — the balanced equation (verified once, corrected; 2026-10-05)

Five instruments, each importing its owners and READing outside results at source with the route recorded. They were
verified adversarially in both directions on 2026-10-05 and every finding was applied; first-written claims are kept
in each file's HISTORY block.

| file | selftest |
|---|---|
| `balance.py` | 17/17, 4 controls, 4 STRUCTURAL |
| `compensate.py` | 15/15, 2 controls, 2 STRUCTURAL |
| `openterms.py` | 11/11, 1 control, 2 STRUCTURAL |
| `bsupply.py` | 8/8, 1 control, 1 STRUCTURAL |
| `placement.py` | 9/9, 1 control, 3 STRUCTURAL |

## M's definition (docket68/M-RULINGS-2026-10-03.md items 29–33, verbatim)

> Balanced means that the value of the object at first position must equal the value of the object at the second
> position. And any variable input must be accounted for in output

- **Item 30**, on the value: "Information only".
- **Item 31**: "Be sure to account for compensation in the physics...".
- **Item 32**, on retiring the original: "I suspect so, to satisfy the no-cloning clause."
- **Item 33**: "Keep all four" (the four counts of I).

So: **I(A, before) = I(B, after)**. Every matter and energy term is an input or an output.

## `balance.py` — the equation

- **The value balances on the teleportation reading** (transit.teleport, 400 random states):
  - With the two bits, B's fidelity is 1.
  - A's four outcomes are equiprobable, so the record alone holds no information.
  - With the bits withheld, B's state is the maximally mixed 𝟙/2: **no information about the state**. Its fidelity of
    1/2 is what a blind guess gives. *(First written as "B holds I/2", which was wrong.)*
- **No-cloning, computed both ways.**
  - The Bužek–Hillery cloner gives each copy fidelity **5/6 < 1** for every input, so a quantum state cannot be copied
    perfectly. (The construction is computed here; its optimality is NAMED-NOT-READ.)
  - CNOT copies basis states perfectly, so a classical description copies freely.
  - M's H-RETIRE-A therefore reaches only the classical part. No-cloning requires only that the *state* not remain at
    A, which the Bell measurement already does without taking the matter apart. Retiring A's matter is what keeps the
    classical description at one position.
- **The accounting is a bookkeeping of declared links**, each input named by an output, **not a balance of
  quantities**. It is printed STRUCTURAL, with one control (IN-EBITS) that tests the bookkeeping function. Energy at A
  is now carried by two OPEN rows: IN-A-RETIRE-E (the energy to retire A, sign by H-STOCK-FORM) and OUT-A-HEAT (the
  read's excess, leaving A as heat). OPEN rows: IN-A-READ, IN-A-RETIRE-E, IN-B-ASSEMBLE, OUT-A-HEAT. **The energy
  total is refused.**
- **Conserved quantities close site by site** with zero transfer from A to B. This is STRUCTURAL. At B the closure is
  D25's stock gate: 749.1 kg of CI feedstock, binder P, which is unmeasured at Proxima.

## `compensate.py` — compensation (item 31)

- **(C1) Frame.** In the Sun's frame (H-SUN-FRAME), the 70 kg body's energy differs between Earth and Proxima b by
  −1.18e11 to +9.85e10 J. Built from B's stock this is **avoided, because nothing crosses**. That is avoidance rather
  than an opposite discrepancy, and it is STRUCTURAL. *(First written as "dissolved".)*
- **(C2) Negative energy at the seat: quantum interest** (Ford & Roman gr-qc/9901074v1, READ). The physics compensates
  a negative-energy defect, but **always overcompensates** (ε > 0), within T_max = 0.338(A/|E|)^(1/3).
  - Eq. 39 is re-derived numerically.
  - The 1 J over 1 m² example sits far outside the paper's causal-contact condition A < T² (fn. 34): cT_max = 1.07e-9 m
    against √A = 1 m.
- **(C3) Bit errors are dissolved by redundancy**, at I/(1 − h₂(p)) bits.
- **(C4) What can and cannot compensate what**, computed rather than declared:
  - **Energy and bits do compensate each other.** More power gives more bits (LNM 1D: 4.6e18 bits/s at 1 kW, 9.1e18 at
    4 kW), and a bit buys up to kT ln 2 of work (Szilard). *(First declared impossible, which understated against M.)*
  - Baryon number, lepton number and charge are compensated only by themselves. Making baryons from energy makes
    antibaryons too: 1.997 Mc².

## `openterms.py` — the OPEN energy terms

- **(T1) Reading at A.** The theorem floor is 0. The probe floors under H-PROBE are:

| probe at 1 Å | per quantum | total over the object |
|---|---|---|
| photon | 12.4 keV | 1.33e13 J |
| electron | 150 eV | 1.62e11 J |
| neutron | 82 meV | 8.8e7 J |

  Near-field reads (scanning-probe microscopy, about eV per quantum) evade the wavelength floor altogether
  (H-NEAR-FIELD).
- **(T2) Retiring A.** The chemistry is bounded by ±3.60e10 J. H-VALENCE is now stated per atom: atomisation energy at
  most (v_max/2)·D_max = 33.5 eV per atom, with D_max the CO bond (READ).
  - A photon or electron read exceeds that ceiling 4.5× to 3,700×. The retire cost is **subsumed by a larger cost, not
    cancelled**, and the excess leaves A as heat.
  - **Absorbed, the photon read at 1 Å deposits about 1.9e11 Gy: the object is destroyed while it is being read.** That
    needs H-READ-BEFORE-DAMAGE, and the plasma it leaves is stock in neither H-STOCK-FORM form.
  - *(First written as "the read dissolves the retire term", which overstated in M's favour.)*
- **(T3) Assembling at B.** The chemistry is within ±3.60e10 J, below the payback ceiling at every speed. Placement is
  in `placement.py`.

## `bsupply.py` — B's local supply against Proxima's light

- **The luminosity sources disagree.**
  - Faria et al. 2022 (READ) give L* = 0.0016 ± 0.0006 L☉, citing Boyajian et al. 2012. That gives a flux of 924 W/m²,
    with a range of 577–1270.
  - Boyajian 2012 itself (READ, Table 6 p.46) gives **0.00155 ± 0.00002 L☉**, a flux of 895 W/m² (883–906).
  - That is a **discrepancy, recorded, not adjudicated**: Faria's spread is 30× the primary source's.
- **The chemical ceiling on 100 m²** takes 4.51 days at Faria's central L*, 4.6–4.7 days on Boyajian's values, and
  **7.22 days at Faria's low L***. So "under a week" holds except at Faria's low end.

## `placement.py` — placement and the energy floor

- **(P1) One floor for the bits.** Bennett's floor, I k T ln 2, is paid once (OUT-B-HEAT). **Separately, B's stock is
  not a blank**: ordering thermal rock lowers the matter's own entropy. That export, T_B·ΔS (H-STOCK-ENTROPY), is
  **OPEN** and local to B. For ΔS of the order of the thermal count it is about 7e5 J at T_CMB or 8e7 J at 310 K.
  *(First written as "placement adds no second floor", which was wrong for the stock.)*
- **(P2) Holding an atom is a returned loan.** In a harmonic trap E0 = 3ħ²/(4mσ²); the general uncertainty floor is the
  kinetic part, 3ħ²/(8mσ²).
- **(P3) The floor of the energy column.** It holds under seat.py's channel hypotheses: H-EM-CARRIER, H-FEW-MODES and
  H-ONE-POL.
  - The channel dominates and falls with the schedule: 1.39e14 J for a classical send in 1 yr. **With two
    polarisations it is half that, 6.93e13 J**, and wider apertures lower it further.
  - The schedule-independent part runs from **2.5e5 J to 6.5e8 J** across counts and erasure.
  - The total stays refused.

## OPEN

1. H-WHICH-COUNT (M: keep all four).
2. H-STOCK-FORM.
3. H-STOCK-ENTROPY.
4. Any ceiling on placement.
5. The collector at B.
6. The Faria–Boyajian luminosity discrepancy.
7. H-READ-BEFORE-DAMAGE for an absorbed read.

## History

Every first-written claim the verification corrected is kept in its file's HISTORY block:
- "B holds I/2".
- The declared-link accounting counted as a balance.
- Two double-counted structural items.
- "No second floor".
- "Within one currency only".
- "The read dissolves the retire term".
- "Under a week".
- The 1e5–1e7 J range.
- Vacuous controls.

The earlier history is kept too: the 2/3 withheld-bits expectation, the 1e-4 ratio threshold, the "under a minute"
threshold, and the `terms.py` → `openterms.py` rename.
