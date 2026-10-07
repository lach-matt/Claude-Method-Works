# Wall E, worked: the corridor's horizon and its instability (M-RULINGS item 149; READ and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 149:** *"I have given you everything I can. You have to work the math now"*.
- **On how long the corridor lasts** (items 86, 136 E): *"Instantaneous or near instantaneous"*.
- **The instrument:** `stability.py`. Selftest 5/5.
  - **Controls:** two. One is a horizon off the corridor; one is READ (extremal Reissner–Nordström).

## READ

- **Aretakis**, "Horizon instability of extremal black holes", arXiv:1206.6598v2.
  - **Abstract:** derivatives of generic waves *"do not decay along such horizons as advanced time tends to infinity,
    and in fact, higher order derivatives blow up"*.
  - **p.10, eqs. (6)–(8):** the setting is g = −D dv² + 2 dv dr + K⁻¹ g_S², and an extremal horizon is one where D and
    D′ vanish.
  - **p.10, Prop. 3.2:** every angular mode carries a conservation law, *"provided"* that D″(r_H) = 2K(r_H) (his eq.
    10). *"Extremal Reissner–Nordström satisfies the condition (10)"* (p.11).
  - **p.15, Theorem 3:** *"sup |Yᵏψ| ≥ c|H₀[ψ]| τ^(k−1), asymptotically along H⁺ for all k ≥ 2"*.

## What the mathematics gives

### 1. The corridor's horizon is extremal (S1)

- **Written in Aretakis's form,** D has a double zero at the horizon, so D′ = 0. The surface gravity is zero.
- **Control:** a horizon member of eq. (17) off the corridor (r₀ = 1.8m) has D′ = √10/(10m), not zero.

### 2. It meets Aretakis's condition exactly (S2)

- **D″ at the horizon is 1/(2m²), and 2K is 1/(2m²).** His eq. (10) holds exactly.
- **So his whole hierarchy of conservation laws applies to the corridor,** as it does to extremal Reissner–Nordström.
  - **Control (READ):** extremal Reissner–Nordström meets (10). The board's arithmetic reproduces his statement.
- **This is not a growing mode.** It agrees with the board's earlier finding that a test scalar has no growing mode on
  this member. Aretakis's instability is non-decay on the horizon, with power-law growth of higher derivatives.

### 3. It acts only at late times, and the corridor's clock is short (S3)

- **The growth is asymptotic in advanced time,** measured in the horizon's own scale m. After a time T, the k-th
  derivative grows by about (cT/m)^(k−1). That is Theorem 3's power; its constant is not known.
- **The corridor's own clock, m/c = r_min(N)/(2c):**
  - **6.6×10⁻³⁷ s** at the board's example README;
  - in general, 1.27×10⁻⁴⁴ s × √N.
- **A hold no longer than that clock leaves the growth of order one.**
  - The second derivative grows by about 1 over one clock, 10 over ten clocks and 1,000 over a thousand.
  - The third derivative grows by the square of those figures.
- **So the instability is real for this horizon, and cannot act within your near-instantaneous hold** if the hold is a
  few of the corridor's clocks or less.
  - What sets the hold's length is not computed here: it is part of the opening and closing.

## Named hypotheses

- **Yours:**
  - H-INSTANT-REBUILD and the hold near-instantaneous (items 86, 136 E);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR (the corridor is eq. 17 at r₀ = 2m);
  - H-TEST-FIELD (a scalar wave stands in for perturbations; Aretakis's own setting).
    - Gravitational perturbations carry the same conservation laws in extremal Kerr (Lucietti–Reall, cited in his
      addendum, not READ here).

## OPEN

1. The hold's length in the corridor's clocks, from the opening and closing dynamics.
