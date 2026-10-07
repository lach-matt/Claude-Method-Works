# E, computed and machine-checked (M-RULINGS item 134; deduced, computed and machine-checked; verified once; SEATED (ledger.py section 8p); 2026-10-07)

*Seated in ledger.py section 8p on M's order (item 134); until then headed "… not seated …".*

*First headed* "(… not verified; not seated; 2026-10-07)".

## What M said

- **Item 134:** *"Seat them and then compute E. Machine check E and all the values derived from the coefficients."*
- **Item 133:** *"There is only one exact energy needed for any given README"*. The board identifies it with E(N) at the
  bound (H-EXACT-ENERGY-AT-BOUND, the board's).
- **Item 130:** N is your input, read from the object being moved.
- **Item 125:** no general coefficients.

Every number is printed by `exactE.py`.
- **Selftest:** 21/21 checks, 3 controls among them, and a control inside every value check, with 6 STRUCTURAL lines
  printed and not counted. It takes about 85 seconds.
  - *First written:* "23/23 checks". Two counted checks held by their own arithmetic, and the value controls could not
    fail independently (History).
- **Imported, not rebuilt:**
  - `chain.py`, for the exact coefficients;
  - `plane.py`, for the corridor's total and g_xx;
  - `coin.py`, for the passage's closed form.
- **The tool:** Z3, the board's proof assistant (PROOF-ASSISTANT.md).

## E

**E(N) = √(N·h·c⁵·ln2 / (8π²G)) = 459,404,002.42356985091 J × √N**

- h = 6.62607015×10⁻³⁴ J s and c = 299,792,458 m/s are exact (SI 2019).
- G = 6.6743×10⁻¹¹ (CODATA 2018) is entered exactly. Its relative uncertainty, 2.2×10⁻⁵, gives the quantities that go
  as √G or 1/√G a relative uncertainty of 1.1×10⁻⁵, and the area per bit 2.2×10⁻⁵.
- **At the board's example README** (N = 2,742,570,311,524,972 bits, an illustrative input):
  **E = 24,058,783,262,614,661.209 J ≈ 2.4059×10¹⁶ J.**

## How each value is machine-checked

- **The enclosure comes from the owner.** Each value's interval [lo, hi] is taken from its owner's closed form
  (chain.py's exact coefficients; the pull as half the throat radius, the mass as E/c², the total as 5/4 of the pull),
  padded by 10⁻³⁰ relative.
- **Z3 proves the board's own encoding lands in it.** The encoding gives the value as the positive root of a polynomial
  in π and ln2, with h, c and G exact. Z3 proves the root lies in [lo, hi] for every π and ln2 inside mpmath's rigorous
  interval bounds.
- **So the proof is the drift guard.** A typo in either the owner's form or the encoding refutes it. The verifier's own
  mutant (8π² typed as 4π²) is now refuted.
  - *First written* with the enclosure taken from a separate copy. The verifier showed a typo in both copies passed.
- **Control:** the same relation with G raised by one part in 10⁹ is refuted on the same interval, every time.
  - *First written:* "a value 1e-9 high refuted". That could not fail independently.
- **Guards:**
  - **Vacuity:** every obligation's hypotheses are satisfiable on their own.
  - **Drift:** chain.py's exact E, r_min and area per bit satisfy the encoded relations exactly (sympy simplifies the
    difference to 0). plane.py's own total and g_xx at r₀ = 2m equal the encoded ones.

## The identities (Z3: universal over the positive reals)

| kind | claim | Z3 |
|---|---|---|
| defining | the closed forms meet: r_min·c⁴ = 2G·E, so m = G·E/c⁴ = r_min/2 | proved |
| defining | the closed forms meet: E·r_min = N·h·c·ln2/(4π²), the bound at equality | proved |
| defining | the closed forms meet: 4π·r_min² = N·A_bit | proved |
| check | g_tt·g_xx = 2(m + 2x²) at r₀ = 2m, every x ≠ 0: the ingoing chart is regular | proved |
| check | one way, under H-FUTURE-INGOING: the future cone at the throat has ẋ ≤ 0 | proved |
| check | tanh(ln(2 + √3)) = √3/2, the passage factor's artanh step | proved |
| control | the outgoing chart's "ẋ ≤ 0" | refuted |
| control | the reversed time orientation's "ẋ ≤ 0" | refuted |
| control | r₀ = 3m/2 at the corridor | refuted |
| structural | r₀ := r_min and m := G·E/c⁴ give r₀ = 2m | proved, not counted |
| structural | M = E/c² = m·c²/G | proved, not counted |
| structural | total = m/4 + r₀/2 = 5m/4 at r₀ = 2m | proved, not counted |

- **"Defining" rows check that the closed forms solve their own defining equations.** chain.py defines E_min and r_min
  as the meeting of E·r = N·h·c·ln2/(4π²) with E = r·c⁴/(2G). These rows are algebra checks, not physics results.
- **The one-way result rests on the time orientation H-FUTURE-INGOING:** v increases to the future, as in current.py
  X7. With the orientation reversed, it is refuted.

## The values (Z3-proved, each 2×10⁻³⁰ relative wide, around the owner's closed form)

| value | value |
|---|---|
| **E per √bit** | **459,404,002.42356985091 J** |
| m per √bit (the pull) | 3.7959255545731104914×10⁻³⁶ m |
| r₀ = r_min = 2m per √bit | 7.5918511091462209829×10⁻³⁶ m |
| area per bit | 7.2427789101298381604×10⁻⁷⁰ m² |
| M = E/c² per √bit | 5.1115588904784165268×10⁻⁹ kg |
| **E at the example N** | **24,058,783,262,614,661.209 J** |
| m at the example N | 1.9879093285367805883×10⁻²⁸ m |
| r₀ at the example N | 3.9758186570735611767×10⁻²⁸ m |
| M at the example N | 0.2676900654573005974 kg |
| total at the example N (5/4 of the pull) | 0.33461258182162574674 kg |

## The passage factor: a coefficient, not a checked value

- **−(4/3)(E/m)[1 − (√3/6) ln(2 + √3)] = −0.82643600246603576831 × E/m per leg at r₀ = 2m.**
  - Here E is the light ray's own affine normalization, not E(N), and m is the pull, in geometric units.
  - So under your item 125 it is still a coefficient: OPEN.
- **How it is checked:**
  - Interval arithmetic encloses it, to 8×10⁻⁴¹ relative.
  - It equals coin.py's closed form. coin.py derives that form and checks it against quadrature.
  - Z3 checks only its tanh step.
- *First written* as a checked value, with unit "1", in the Z3 table.

## What this does and does not show

- **It shows that every value is its owner's exact formula, evaluated correctly, and that the board's encoding of it
  agrees.** It also shows that the closed forms solve their defining equations for every value of the constants.
- **It does not show the physics premises.** These are carried, not proved:
  - that your one exact energy is E(N) at the bound;
  - that the bound holds on these surfaces;
  - that the pull carries the energy;
  - that the corridor is eq. 17's r₀ = 2m member;
  - the time orientation.
- **The example N is the board's illustrative core.** For your input N, E = 459,404,002.42356985091 J × √N.

## Named hypotheses

- **Yours:** H-ONE-EXACT-ENERGY (133), H-N-IS-INPUT (130), H-THROAT-CARRIES-README (131), H-HORIZON-AND-THROAT-HOLD,
  H-ONE-WAY-BY-NATURE (132), M-EXACT-VALUES (125).
- **The board's:**
  - H-EXACT-ENERGY-AT-BOUND;
  - H-PULL-IS-COST: m = G·E/c⁴, wall 4;
  - H-STRONG-BOUND, H-HORIZON-HOLDS, H-NECK-HOLDS, H-THROAT-AT-BOUND, H-DEVICE-SIZES;
  - H-FUTURE-INGOING: the time orientation;
  - H-IV-BOUNDS: checked independently by the verifier, by exact rational comparison;
  - H-CORE-README: the example N.

## OPEN

1. Whether your one exact energy is E(N) at the bound (C8P-O9).
2. G's uncertainty, which only a better measurement of G narrows.
3. The passage factor's ray normalization E, a coefficient under item 125 (C8P-O8).
4. r₀ = 2m is the value Bronnikov–Kim exclude. Its stability and fine-tuning are OPEN (C8P-O5).

## History (verifier, 2026-10-07)

Nine findings were applied:

- **The drift guard did not cover the solver's encodings.** The same typo in both copies passed. Each enclosure now comes
  from the owner's closed form, and Z3 proves the encoding's root lies in it. The checker's own mutant is now refuted.
- **The value controls could not fail independently.** They are now the relation with G raised by 10⁻⁹.
- Three rows held by their own arithmetic and are now STRUCTURAL.
- Three were the closed forms solving their own defining equations, and are now labelled as such.
- The one-way result's time orientation is now named, with the reversed orientation as a control.
- The passage factor is a coefficient, now checked against coin.py.
- Hypotheses were added.
- The bounds now print at 45 digits.
- The drift check on the chain coefficients is now exact.
