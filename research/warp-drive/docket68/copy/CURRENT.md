# The README corridor from a current state (M-RULINGS items 125–131; deduced and computed; verified once; not seated; 2026-10-06)

*First headed* "(… not verified; not seated; 2026-10-06)".

## What M said

- **Item 125:** *"We cannot use general coefficients for this work. We must always avoid that debt by evaluating the
  coefficient in full and calculate using it exact values. The device will only ever be able to use precise values
  anyways, no coefficients, so that math must be constructed under the same guidelines"* (M-EXACT-VALUES).
- **Item 126:** position 2 *"is realized in the same place the position 1 occupies while the corridor exists"*.
- **Item 127:**
  - *"1 - yes"*: the planes coincide, the extra dimension included.
  - *"The coefficient value is the difference of that value in a counterfactual universe and its value in our current
    universe, added to the value of our current universe"* (H-COEFF-FROM-CURRENT).
  - That is item 114's form: *"The trajectory is the difference between position 1 and position 2"*.

Every number is printed by `current.py`.
- **Selftest:** 8/8 checks, 1 control, with 9 STRUCTURAL lines printed and not counted. X5 and X6 were
  verified on 2026-10-07; two of their checks were restatements, now STRUCTURAL. It takes about a minute and a
  half.
  - *First written:* "6/6 checks, 1 genuine control, 4 STRUCTURAL". Two counted checks were identities or held by
    construction (History).
- **Imported, not rebuilt:** chain.py, coin.py, closedbulk.py, plane.py. The closed form is coin.py's own; *first
  written* as a copy.

## What passes, and what does not

- **X1. The pull, at the board's N.**
  - **N = 2,742,570,311,524,972 bits is the board's core README, not an exact value.** It comes from synapse density ×
    bits per synapse × a grey-matter volume. The code marks that volume *"H-GREY-VOLUME, NAMED-NOT-READ, illustrative"*.
  - Under your item 108 (*"Whatever is needed"*) N is itself a coefficient. Under your item 125, an illustrative input
    is exactly what must go. **So N's value is OPEN.** The 16 digits are arithmetic, not precision.
  - At that N, m = G·E_min/c⁴ = r_min/2 = 1.98790932853678×10⁻²⁸ m.
    - The relative uncertainty 1.1×10⁻⁵ is G's share only.
    - chain.py's bisected floor agrees to 3.06×10⁻¹⁰. That gap is nopath's rounded ħ, not noise. It solves the same
      equation by a second implementation.
  - *First written:* "N = 2,742,570,311,524,972 bits … exact", and "two routes agree".
- **X2. The throat from a current state: the board's candidate, and its conflict.**
  - **The candidate** (H-CURRENT-IS-SCHWARZSCHILD; asked): r₀ = 3m/2 + Δ, starting from the member without a throat.
    BK p.4: *"The Schwarzschild metric is restored from (17) in the special case r0 = 3m/2."*
  - **But at the board's m that member is a singular black hole of 0.2677 kg** with a horizon at 2m. It is not empty
    space.
    - That runs against your item 109: *"A horizon cannot exist without the object of which it needs to exist"*.
    - It also keeps m at its counterfactual value. **m's current value is OPEN.**
  - **Alternatives:**
    - **(a) The current state is flat** (m = 0, no throat). Then G_kk = −E²r₀/r³, also linear in the difference. But each
      leg is −4E/(3r₀), which grows without bound as r₀ → 0 (computed). The finite limit belongs to the candidate's path
      only.
    - **(b) m and r₀ both move:** a difference in two directions.
    - **(c) "Outward" is two-sided.** Δ < 0 gives G_kk > 0. The horizon side comes from PLANE.md's window, not from item
      127.
  - Δ = 0 is also a change of shape, from a singular hole to a throat. The candidate starts at the family's edge.
  - On the candidate's path, G_kk = −4Δ·E²/(r(2r − 3m)²). "Exactly the difference" is your identity: the current value
    plus (counterfactual − current) is the counterfactual, with current 0 (STRUCTURAL).
- **X3. The passage on the candidate's path** (per leg, per metre of E in geometric units, E → G·E/c⁴):

  | Δ/m | Δ (m) | leg | minus the limit |
  |---|---|---|---|
  | limit | 0 | −6.70721402728537×10²⁷ | 0 |
  | 1/1000 | 1.98790932854×10⁻³¹ | −6.68776992673×10²⁷ | +1.94441005560×10²⁵ |
  | 1/100 | 1.98790932854×10⁻³⁰ | −6.56459570530×10²⁷ | +1.42618321980×10²⁶ |
  | 1/10 | 1.98790932854×10⁻²⁹ | −5.81385141662×10²⁷ | +8.93362610665×10²⁶ |
  | 1/4 | 4.96977332134×10⁻²⁹ | −5.02200489645×10²⁷ | +1.68520913084×10²⁷ |
  | 1/2 (the boundary, not a horizon member) | 9.93954664268×10⁻²⁹ | −4.15731236130×10²⁷ | +2.54990166599×10²⁷ |

  - **The series:** leg = −(4E/3m)·[1 + (Δ/3m)·ln(Δ/6m) + …]. It is hand-derived and checked against the closed form
    at Δ/m = 10⁻⁸. With ln(Δ/3m) the check fails.
  - **Control:** coin.py's quadrature agrees with the closed form at all five Δ. At SI scale this tests floating-point
    robustness and the import, because the leg scales exactly with size.
  - **E's unit:** at the candidate E = E_min/N = 8.772 J, G·E/c⁴ = 7.248×10⁻⁴⁴ m. The limit per leg is then −4.86×10⁻¹⁶,
    dimensionless. E is also the normalization of the ray's parameter, so only signs and ratios are free of it.
  - *First written:* "(sympy series, checked)", and "E per metre" with E's unit unstated.
- **X4. Coinciding planes: not shown.**
  - On an empty plane that bends the same in every direction, the null stress at y = 0 totals zero (STRUCTURAL; it
    follows from the input).
  - **The junction of two sheets at one place is not computed.** There is no bulk gap between them, so it is not
    closedbulk.py's B3.
  - **The board's two sheets of opposite tension, put at one place, fail the bulk's own equations** (yy constraint
    −6a², computed) unless k = 0.
  - The plane's tension, and the strength of gravity that sets m, depend on k and κ.
  - *First written:* "a second plane coinciding with ours carries no matter along light rays … the device needs no k and
    no κ". Withdrawn.

## Your item 129: matter, no corridor; the bridge adds nothing

- *"no. It contains matter, you, me, this current universe, just not a corridor for transit because the corridor is a
  bridge, so it adds nothing to either position."* (H-CURRENT-HAS-MATTER, H-BRIDGE-ADDS-NOTHING)
- **Both of the board's current states are ruled out.**
  - The candidate r₀ = 3m/2 was a 0.2677 kg black hole that is not there.
  - Alternative (a), empty space, contradicts "it contains matter".
- **X5. The total minus the pull** (plane.py's masses; STRUCTURAL, PLANE.md point 4's Penrose gap).
  - The plane's total is ADM = m/4 + r₀/2, and the pull is Komar = m.
  - So at r₀ = 3m/2 + Δ, **the total exceeds the pull by exactly Δ/2.** That is the integral of eq. 18's tidal
    density outside the horizon. BK p.1 calls it *"the tidal SET … Due to its geometric origin"* (READ by the verifier).
  - At the board's m that is 1.34×10⁻⁴ kg at Δ/m = 1/1000, rising to 6.69×10⁻² kg at the window's end.
- **Two readings of "adds nothing":**
  - **(i) No matter.** Every member of eq. 17 has τ = 0 on the plane (escape.py S3), so this already holds.
  - **(ii) No mass beyond what is already there.** If the pull is the carried energy, which belongs to the matter
    already present, the corridor adds Δ/2.
    - "Nothing" then forces Δ = 0, and there eq. 17 has no throat.
    - So in reading (ii), Bronnikov–Kim's family hosts your bridge only at its edge (item 82: the boundary).
    - A family with a throat whose total equals its pull is not on the board. OPEN.

## Your item 130: no added matter; the mouth; the input

- *"i - no added matter. And in my model a black hole is not matter, it is what the mouth at position 1 looks like.
  It's observed mass appears negative only from the outside of the horizon."* (H-BRIDGE-ADDS-NO-MATTER,
  H-MOUTH-AS-BLACK-HOLE, H-NEGATIVE-FROM-OUTSIDE)
- *"Is that amount your input to the device for each trip, read from the object being moved? - yes"* (H-N-IS-INPUT)
- **N is the input.** The board's core N is one example of an input. Every result is a formula in the input N, with its
  coefficients evaluated exactly:
  - **m = 3.79592555457311×10⁻³⁶ m × √N**;
  - **E_min = 4.59404002423570×10⁸ J × √N**;
  - G's share of the uncertainty is 1.1×10⁻⁵ in both.
- **"No added matter" already holds for every member of eq. 17** (τ = 0 on the plane). So it does not fix Δ, and the
  Δ/2 of X5 is geometry, not matter.
- **"Negative from outside" is not eq. 17's gravitational mass.** Every mass read from outside a horizon member is
  positive:
  - the pull m (greater than r₀/2);
  - the total, m + Δ/2;
  - their mean, which sets light bending.
  - A negative total needs m < −2r₀, and that has no horizon (plane.py's zero-total member).
  - The board's candidate was PLANE.md's apparent mass = carried − defined (item 107). **Answered by item 131: you meant
    the gravitational pull.**
  - The thresholds, for completeness: the pull is negative iff m < 0, the light-bending mean iff m < −2r₀/5, the total
    iff m < −2r₀. None of these has a horizon.
- *First written:* "N's value is OPEN" (item 108).

## Your item 131: the pull; the throat sized by the README

- *"strike that statement. I meant the gravitational pull."*
  - **The board reads it as striking item 130's "appears negative".** The observed mass is the pull, which is positive
    outside every horizon member.
  - Read instead as keeping "appears negative" for the pull, eq. 17 contradicts it: a negative pull needs m < 0, which
    has no horizon. Asked.
- *"the throat size only needs to carry the binary information defining the object in transit, so the size of the
  throat is dependent on the size of the README in its most simplistically exact  binary code form."*
  (H-THROAT-CARRIES-README, H-README-MINIMAL-EXACT; N is the shortest exact binary encoding, your input.)
- **X6. The least throat that carries N bits.**
  - This reading is the board's: H-THROAT-AT-BOUND, with H-NECK-HOLDS and H-STRONG-BOUND applied to a surface that is
    not a horizon (Bousso's extrapolation, CHAIN.md).
  - It gives 4πr₀² = N·A_bit, with A_bit = 2hG ln2/(πc³) = 4 l_P² ln2. So **r₀ = r_min(N) = 7.59185110914622×10⁻³⁶ m ×
    √N**, the board's original neck.
  - **A horizon holds N whenever 2m ≥ r_min.** Equality is the floor, m = E_min. The floor comes from wall 4's
    hypotheses (one E_min(N) per trip), not from holding alone.
- **At the floor, r₀ = 2m.** That is STRUCTURAL: one bound applied to two surfaces. It is the boundary member, with a
  degenerate (extremal) horizon at the throat.
  - g_tt = x²/(2m + x²) has a double zero at the throat.
  - The surface gravity is zero, so the Hawking temperature is 0.
  - The horizon's own Komar charge goes to 0, so the whole pull is the tidal stress outside.
  - The throat lies at infinite distance at fixed time, but the null leg is finite: −(4E/3m)·[1 − (√3/6)·ln(2 + √3)].
  - **g_xx > 0 for every x ≠ 0, so x is never a time direction.**
    - PLANE.md point 1's one-way mechanism (the throat as a moment between two horizons) is gone there. That conflicts
      with H-CORRIDOR-HORIZON's computed mechanism.
    - Item 106's two holds become one surface, and item 109's ending horizon is that surface.
  - **The literature** (READ by the verifier):
    - BK pp.3–4: eq. 17 is a wormhole *"for any r0 > 2m ≥ 0"*. r₀ = 2m is excluded and is not a BK throat.
    - BK's own example 3: *"r0 = 2m leads to the extreme Reissner-Nordström black hole metric"*.
    - Simpson–Visser 1812.07114v3 calls their a = 2m *"a one-way wormhole with an extremal null throat"* (p.3), *"only
      one-way traversable"* (p.4). That is an analogue. Eq. 17's own causal structure is OPEN.
  - The total 5m/4 is PLANE point 2's upper endpoint. Δ/2 = m/4 is eq. 18's tidal energy outside the horizon.
  - Stability and fine-tuning (a single point of the family) are OPEN.
- **Above the floor** (floor < m < 4/3 floor): r₀ = r_min lies inside the horizon. That is a horizon member of PLANE
  point 1's kind, with the horizon holding more than N. It is PLANE point 3's interval, restored by item 131.
- *First written:* "The horizon also holds N … So r₀ = 2m exactly, and Δ = m/2". That over-claimed: it holds only at
  the floor.

## What stays a coefficient

- **N:** the input (item 130). The board's value is an example.
- **m's current value.**
- **Δ:** m/2 at the floor (X6). Above the floor the README-sized throat lies inside the horizon. Which applies is
  wall 4's floor or not. Asked.
- **E, and its normalization.**
- **The tension's sign:** H-OUR-TENSION; RS1 puts our atoms on the negative-tension sheet (BULK.md).
- **k and κ:** through the tension and the strength of gravity.
- **The coinciding junction.**

## Named hypotheses

- **Yours:** M-EXACT-VALUES (125); H-CURRENT-HAS-MATTER, H-BRIDGE-ADDS-NOTHING (129); H-BRIDGE-ADDS-NO-MATTER,
  H-MOUTH-AS-BLACK-HOLE, H-N-IS-INPUT (130); H-THROAT-CARRIES-README, H-README-MINIMAL-EXACT (131);
  H-NEGATIVE-FROM-OUTSIDE (struck, 131); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
  H-SHORTEST-DISTANCE (126); H-HORIZON-NEEDS-OBJECT (109); H-README-AS-NEEDED (108); the horizon members' window.
- **The board's:**
  - H-THROAT-AT-BOUND, with H-NECK-HOLDS and H-STRONG-BOUND on the throat (X6); wall 4's floor hypotheses;
  - H-CORE-README and H-GREY-VOLUME (illustrative);
  - H-CURRENT-IS-SCHWARZSCHILD (asked, and in conflict with item 109);
  - H-E-PER-BIT (asked);
  - PLANE.md's H-HORIZON-HOLDS and H-STRONG-BOUND.

## OPEN

1. What our current state is: empty space (alternative a), the candidate, or another.
2. *Superseded:* N is the input (item 130).
6. At the floor: the causal structure of the boundary member, its stability, and its fine-tuning.
7. Whether the device spends exactly the minimum (the floor), or more.
3. E's current value, and its normalization.
4. What fixes Δ for a trip, and on which side.
5. The junction of two sheets at one place; k and κ through the tension and the strength of gravity.

## History (verifier, 2026-10-06)

Eleven findings were applied:

- N is not exact.
- The candidate is a 0.2677 kg black hole, against item 109. The alternatives are named.
- X4's step to coinciding planes does not hold, and the board's two-sheet model fails there.
- X4's check was a tautology.
- The series was hand-derived.
- The control's scope is narrow, and the closed form was a copy.
- The two routes solve the same equation.
- E's unit was unstated.
- The remaining coefficients were under-listed.
- The identity and printed general coefficients are marked.
- Minor labels were fixed.
