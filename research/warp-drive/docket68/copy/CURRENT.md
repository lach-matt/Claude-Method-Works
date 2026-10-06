# The README corridor from a current state (M-RULINGS items 125–127; deduced and computed; verified once; not seated; 2026-10-06)

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
- **Selftest:** 6/6 checks, 1 control, with 6 STRUCTURAL lines printed and not counted. It takes about a minute and a
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

## What stays a coefficient

- **N:** item 108, and the board's value is illustrative.
- **m's current value.**
- **Δ and its side.**
- **E, and its normalization.**
- **The tension's sign:** H-OUR-TENSION; RS1 puts our atoms on the negative-tension sheet (BULK.md).
- **k and κ:** through the tension and the strength of gravity.
- **The coinciding junction.**

## Named hypotheses

- **Yours:** M-EXACT-VALUES (125); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
  H-SHORTEST-DISTANCE (126); H-HORIZON-NEEDS-OBJECT (109); H-README-AS-NEEDED (108); the horizon members' window.
- **The board's:**
  - H-CORE-README and H-GREY-VOLUME (illustrative);
  - H-CURRENT-IS-SCHWARZSCHILD (asked, and in conflict with item 109);
  - H-E-PER-BIT (asked);
  - PLANE.md's H-HORIZON-HOLDS and H-STRONG-BOUND.

## OPEN

1. What our current state is: empty space (alternative a), the candidate, or another.
2. N and m in our current universe.
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
