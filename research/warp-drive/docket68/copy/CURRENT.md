# The README corridor from our current state (M-RULINGS items 125–127; deduced and computed; not verified; not seated; 2026-10-06)

## What M said

- **Item 125:** *"We cannot use general coefficients for this work. We must always avoid that debt by evaluating the
  coefficient in full and calculate using it exact values. The device will only ever be able to use precise values
  anyways, no coefficients, so that math must be constructed under the same guidelines"* (M-EXACT-VALUES).
- **Item 126:** position 2 *"is realized in the same place the position 1 occupies while the corridor exists"*.
- **Item 127:**
  - *"1 - yes"*: the planes coincide, the extra dimension included.
  - *"these are coefficients. And because the are coefficients, they represent a variable solution. If we can calculate
    the individual value for our current state, we can evaluate the range of values moving out from out from our
    current state. The coefficient value is the difference of that value in a counterfactual universe and its value in
    our current universe, added to the value of our current universe"* (H-COEFF-FROM-CURRENT).
  - That is item 114's form: *"The trajectory is the difference between position 1 and position 2"*.

Every number is printed by `current.py`.
- **Selftest:** 6/6 checks, 1 genuine control, with 4 STRUCTURAL lines printed and not counted. It takes about a minute
  and a half.
- **Imported, not rebuilt:**
  - `chain.py`, for the exact coefficients, the core README's N and the floor;
  - `coin.py`, for G_kk and the passage;
  - `closedbulk.py`, for K_kk;
  - `plane.py`, for BK's text.

## What passes

- **X1. The pull, exact.**
  - N = **2,742,570,311,524,972** bits (the core README).
  - E_min = 2.40587832626147×10¹⁶ J.
  - **m = G·E_min/c⁴ = r_min/2 = 1.98790932853678×10⁻²⁸ m.**
  - The relative uncertainty is 1.1×10⁻⁵, from G. h and c are exact.
  - Two routes agree: chain.py's exact coefficient times √N, and chain.py's bisected floor halved.
- **X2. The throat, from our current state.**
  - **The board's candidate for r₀'s current value** (H-CURRENT-IS-SCHWARZSCHILD; asked):
    - Our current state has no corridor, and the member of eq. 17 with none is Schwarzschild. BK p.4: *"The
      Schwarzschild metric is restored from (17) in the special case r0 = 3m/2."*
    - So **r₀ = 3m/2 + Δ**. The current value is 2.98186399280517×10⁻²⁸ m.
    - Δ is the counterfactual difference, with 0 < Δ < m/2 = 9.93954664268×10⁻²⁹ m.
  - **The plane's reading is then exactly the difference: G_kk = −4Δ·E²/(r(2r − 3m)²).**
    - It is zero in our current state and linear in Δ.
    - The corridor's whole reading is the counterfactual difference.
- **X3. The passage, from the current state outward** (per leg, in units of E per metre):

  | Δ/m | Δ (m) | leg | leg minus current |
  |---|---|---|---|
  | current state (limit) | 0 | **−6.70721402728537×10²⁷** | 0 |
  | 1/1000 | 1.98790932854×10⁻³¹ | −6.68776992673×10²⁷ | +1.94441005560×10²⁵ |
  | 1/100 | 1.98790932854×10⁻³⁰ | −6.56459570530×10²⁷ | +1.42618321980×10²⁶ |
  | 1/10 | 1.98790932854×10⁻²⁹ | −5.81385141662×10²⁷ | +8.93362610665×10²⁶ |
  | 1/4 | 4.96977332134×10⁻²⁹ | −5.02200489645×10²⁷ | +1.68520913084×10²⁷ |
  | 1/2 (the window's end, r₀ = 2m) | 9.93954664268×10⁻²⁹ | −4.15731236130×10²⁷ | +2.54990166599×10²⁷ |

  - **Moving outward:** leg = −(4E/3m)·[1 + (Δ/3m)·ln(Δ/6m) + O((Δ/m)² ln(Δ/m))]. sympy derived the series and
    coin.py's quadrature checks it.
  - **At the current state itself there is no throat, so no passage, and G_kk = 0.**
    - The limit from the counterfactual side is −4E/(3m), not 0.
    - The passage's whole reading gathers at the throat as Δ → 0.
  - **Control:** the closed form at exact m in metres agrees with coin.py's quadrature at all five Δ.
- **X4. With the planes coinciding (item 127), k drops out.**
  - A second plane in our plane's place carries exactly zero matter along light rays: K_kk = 0 on our plane.
  - Every reading of the corridor on our plane is free of the bulk's scale a = k. That covers G_kk, the bulk's
    E_kk = −G_kk, and the passage.
  - So in the coinciding configuration the device needs no k and no κ.
  - The layers off our plane still need k (MANYPLANES.md).

## What stays a coefficient

- **E, the ray's energy.** Every passage reading is linear in it.
- **Its current-state value is asked.** The board's candidate is the floor's energy per bit, E_min/N =
  8.77234875675332 J (H-E-PER-BIT, the board's).
- **Δ itself:** your item 127 makes it the counterfactual difference. Its value for a given trip is not yet ruled.

## Named hypotheses

- **Yours:** M-EXACT-VALUES (125); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
  H-SHORTEST-DISTANCE (126); the horizon members' window (PLANE.md).
- **The board's:**
  - H-CURRENT-IS-SCHWARZSCHILD (asked);
  - H-E-PER-BIT (asked);
  - PLANE.md's H-HORIZON-HOLDS and H-STRONG-BOUND, which give m = r_min/2.

## OPEN

1. Whether r₀'s current value is the no-corridor member r₀ = 3m/2 (the board's candidate).
2. E's current-state value.
3. What fixes Δ for a trip.
4. k's current value, needed by the layers off our plane only.
