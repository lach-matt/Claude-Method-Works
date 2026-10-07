# E, computed and machine-checked (M-RULINGS item 134; deduced, computed and machine-checked; not verified; not seated; 2026-10-07)

## What M said

- **Item 134:** *"Seat them and then compute E. Machine check E and all the values derived from the coefficients."*
- **Item 133:** *"There is only one exact energy needed for any given README"*. The board identifies it with E(N) at the
  bound (H-EXACT-ENERGY-AT-BOUND, the board's).
- **Item 130:** N is your input, read from the object being moved.
- **Item 125:** no general coefficients.

Every number is printed by `exactE.py`.
- **Selftest:** 23/23 checks, 2 controls in the identities, and a control inside every value check, with 3 STRUCTURAL
  lines printed and not counted. It takes about 80 seconds.
- **Imported, not rebuilt:**
  - `chain.py`, for the exact coefficients;
  - `plane.py`, for the corridor's masses and g_xx.
- **The tool:** Z3, the board's proof assistant (PROOF-ASSISTANT.md).

## E

**E(N) = √(N·h·c⁵·ln2 / (8π²G)) = 459,404,002.42356985091 J × √N**

- h = 6.62607015×10⁻³⁴ J s and c = 299,792,458 m/s are exact (SI 2019).
- G = 6.6743×10⁻¹¹ (CODATA 2018) is entered exactly. Its relative uncertainty, 2.2×10⁻⁵, gives E and every quantity
  in √N a relative uncertainty of 1.1×10⁻⁵, and the area per bit 2.2×10⁻⁵.
- **At the board's example README** (N = 2,742,570,311,524,972 bits, an illustrative input):
  **E = 24,058,783,262,614,661.209 J ≈ 2.4059×10¹⁶ J.**

## What a machine check means here

- **Identities: proved for every positive value of the constants, not at one point.**
  - Z3 is given the hypotheses and the claim's negation. "unsat" means no counterexample exists anywhere.
  - Square roots enter as positive roots of their squares (E > 0, E² = …), so every claim is polynomial and Z3 decides
    it.
- **Values: rigorous enclosures.**
  - π and ln2 are bounded by mpmath's interval arithmetic, which rounds outward.
  - Z3 then proves that the value lies in [lo, hi] for *every* π and ln2 inside those bounds. That is far tighter than
    G's own uncertainty.
  - **Control:** a value claimed one part in 10⁹ too high is refuted, every time.
- **Guards** (PROOF-ASSISTANT.md's two):
  - **Vacuity:** each obligation's hypotheses are satisfiable on their own, so an "unsat" is never empty.
  - **Encoding drift:** the encoded E, r_min and area per bit match chain.py's exact coefficients (zero difference at 30
    digits). The encoded total and g_xx at r₀ = 2m match plane.py's.

## Machine-checked identities (Z3: proved for every positive h, c, G, π, ln2, N)

| claim | Z3 |
|---|---|
| m = G·E/c⁴ = r_min/2 (the pull) | proved |
| E·r_min = N·h·c·ln2/(4π²) (Bekenstein's bound saturated) | proved |
| 4π·r_min² = N·A_bit, with A_bit = 2hG ln2/(πc³) (each surface holds N bits) | proved |
| r₀ = r_min and m = G·E/c⁴ give r₀ = 2m (the throat on the horizon) | proved |
| M = E/c² = m·c²/G (the pull as a mass) | proved |
| total = m/4 + r₀/2 = 5m/4 at r₀ = 2m; total − pull = m/4 | proved |
| g_tt·g_xx = 2(m + 2x²) at r₀ = 2m (the ingoing chart is regular) | proved |
| one way: the future cone at the throat has ẋ ≤ 0 | proved |
| tanh(ln(2 + √3)) = √3/2 (the passage factor's algebraic core) | proved |
| **control:** the outgoing chart's "ẋ ≤ 0" | refuted, as it must be |
| **control:** r₀ = 3m/2 at the corridor | refuted, as it must be |

## Machine-checked values (Z3-proved enclosures, each 2×10⁻³⁰ relative wide)

| value | exact form | value |
|---|---|---|
| E per √bit | √(h c⁵ ln2/(8π²G)) | **459,404,002.42356985091 J** |
| m per √bit | √(hG ln2/(2π²c³))/2 | 3.7959255545731104914×10⁻³⁶ m |
| r₀ = r_min = 2m per √bit | √(hG ln2/(2π²c³)) | 7.5918511091462209829×10⁻³⁶ m |
| area per bit | 2hG ln2/(πc³) | 7.2427789101298381604×10⁻⁷⁰ m² |
| M = E/c² per √bit | | 5.1115588904784165268×10⁻⁹ kg |
| **E at the example N** | | **24,058,783,262,614,661.209 J** |
| m at the example N | | 1.9879093285367805883×10⁻²⁸ m |
| r₀ at the example N | | 3.9758186570735611767×10⁻²⁸ m |
| M at the example N | | 0.2676900654573005974 kg |
| total at the example N (5/4 of the pull) | | 0.33461258182162574674 kg |
| passage factor per leg at r₀ = 2m | −(4/3)[1 − (√3/6) ln(2 + √3)] | −0.82643600246603576831 (× E/m) |

- The passage factor is transcendental. Interval arithmetic encloses it, to a width of 8×10⁻⁴¹ relative. Its algebraic
  core is the Z3 identity above.
- The enclosures are exact for G as entered. G's own uncertainty is the real limit on these digits.

## What this does and does not show

- **It shows that every value is the stated exact formula, evaluated correctly.** It also shows that the formulas are
  consistent with one another for every value of the constants: the pull, the throat, the horizon, the bits, the masses,
  the regular chart and the one-way cone.
- **It does not show the physics premises.** These are carried, not proved:
  - that your one exact energy is E(N) at the bound (H-EXACT-ENERGY-AT-BOUND, the board's);
  - that the bound holds on these surfaces (H-STRONG-BOUND, H-HORIZON-HOLDS, H-THROAT-AT-BOUND);
  - that the corridor is eq. 17's r₀ = 2m member.
- **The example N is the board's illustrative core.** For your input N, E = 459,404,002.42356985091 J × √N.
- **Trusted, named:** mpmath's interval π and ln2 (H-IV-BOUNDS), and Z3's nonlinear real arithmetic.

## Named hypotheses

- **Yours:** H-ONE-EXACT-ENERGY (133), H-N-IS-INPUT (130), H-THROAT-CARRIES-README (131), H-HORIZON-AND-THROAT-HOLD,
  H-ONE-WAY-BY-NATURE (132), M-EXACT-VALUES (125).
- **The board's:**
  - H-EXACT-ENERGY-AT-BOUND;
  - H-STRONG-BOUND, H-HORIZON-HOLDS, H-THROAT-AT-BOUND;
  - H-CORE-README (the example N);
  - H-IV-BOUNDS.

## OPEN

1. Whether your one exact energy is E(N) at the bound (C8P-O9).
2. G's uncertainty, which only a better measurement of G narrows.
