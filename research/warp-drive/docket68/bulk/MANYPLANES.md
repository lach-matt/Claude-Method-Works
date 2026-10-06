# Infinitely many planes, as layers and as sheets (M-RULINGS items 123–127; deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS items 123–124; deduced and computed; not verified; not seated; 2026-10-06)".

## What M said

- **Item 123:**
  - *"by closed I mean every plausibility, possibility, eventuality, every position infinitely possible as a closed
    dimension."*
  - *"A second plane exists. In a closed infinite multiverse dimension, there are infinite spacetime planes"*
- **Item 124:** *"Both A and B"*. (A) is the planes as the bulk's own layers; (B) is the planes as separate sheets with
  their own matter.
- **Item 125:** no general coefficients. Every value is evaluated with the exact values the device would use.
- **Item 126:**
  - *"The corridor will always entangle separate plane position using the shortest distance needed."*
  - *"The second position isn't built far away, it is realized in the same place the position 1 occupies while the
    corridor exists"*
- **Item 127:**
  - *"1 - yes"*: the planes coincide, the extra dimension included.
  - *"The coefficient value is the difference of that value in a counterfactual universe and its value in our current
    universe, added to the value of our current universe"*

Every number is printed by `manyplanes.py`.
- **Selftest:** 6/6 checks, 2 genuine controls and 1 contrast, with 6 STRUCTURAL lines printed and not counted. It takes
  about three minutes.
  - *First written:* "6/6 checks, 1 genuine control and 1 contrast, with 4 STRUCTURAL", at an illustrative member.
- **Imported, not rebuilt:**
  - `closedbulk.py`;
  - `pairing.py`;
  - `coin.py`;
  - `current.py`, for the README's exact m.

## The tool: one exact identity

- **R⁽⁵⁾_μν = R⁽⁴⁾_μν − ∂_yK_μν + 2K_μαK^α_ν − K K_μν**, in coordinates running straight out from a layer
  (K = ½∂_y g, lower indices).
- It is checked exactly for any metric −A dt² + B dr² + C dΩ² + dy². The control: with the quadratic sign flipped, it
  fails.
- It is Maartens' eq. 3.9 (gr-qc/0312059v2 p.9, READ by the verifiers).
- **In a bulk of vacuum energy, R⁽⁵⁾_kk = 0 along each layer's own light rays.** So each layer reads its own spacetime as
  R⁽⁴⁾_kk = ∂_yK_kk − 2(KK)_kk + K K_kk.

## (A) The layers

- **A1. Throat and horizon on nearby layers (STRUCTURAL).**
  - Every coefficient of A/A₀, B/B₀ and C/C₀ through y⁴ has poles only at r = 0 and r = 3m/2.
  - So on each nearby layer the horizon stays where A vanishes, at 2m. The throat also stays, at r₀: B keeps its
    1/(r − r₀) pole while C stays regular, which puts the minimum areal radius there.
  - The check cannot fail for any r₀ ≠ 3m/2, and it has no control.
  - *First written* as a counted check, on A and B only.
- **A2. What each nearby layer reads, exactly.**
  - Along its own radial light ray, each layer reads

    **L(y) = G_kk·(1 + 4a y) + [8a²·G_kk + R₂]·y² + …**

    - The 4a and 8a² are the warp rescaling each layer's light cone.
    - **R₂ is free of a and zero for a Schwarzschild plane.** It is the layers' own departure from the warp: Maartens'
      −E y², the bulk responding to the plane's Weyl curvature.
  - **Integrated along each layer's whole passage:** I₀ + I₁y + I₂y², with I₁ = 2a·I₀ and I₂ = 2a²·I₀ + J₂.
  - **At the README's exact m** (m = 1.98790932853678×10⁻²⁸ m, current.py), with r₀ = 3m/2 + Δ, from the current state
    outward:

    | Δ/m | I₀ (E per metre) | J₂ (E per metre³) |
    |---|---|---|
    | 1/1000 | −1.3376×10²⁸ | **+2.0082×10⁸⁵** |
    | 1/100 | −1.3129×10²⁸ | +1.9794×10⁸⁴ |
    | 1/10 | −1.1628×10²⁸ | +1.7444×10⁸³ |
    | 1/4 | −1.0044×10²⁸ | +5.8345×10⁸² |
    | 1/2 | −8.3146×10²⁷ | +2.2585×10⁸² |

    - I₀ matches current.py's exact closed form at all five Δ. That is the control.
    - **J₂ is positive at every Δ.** It is the first computed sign of the layers turning toward positive.
    - J₂ grows about tenfold per decade as Δ shrinks toward the current state. So the series reaches less far the closer
      the corridor is to the no-corridor state (H-NEAR-PLANE).
    - **The bulk's scale a = k stays a coefficient off our plane.** Its current-state value is asked.
  - *First written* at the illustrative member m = 1, r₀ = 1.8, a = 1: −1.914712 − 3.829424y − 3.467761y² E/m, "each
    term negative".
    - Those were general coefficients, which item 125 rules out.
    - "Each term negative" held only for a·m > 0.3073.
  - **Contrast:** a Schwarzschild plane's layers read 0. That is exact at every order, because the black string is an
    exact solution (Maartens p.19, after eq. 4.3).
- **A3. Light along a nearby layer is drawn toward our plane** (STRUCTURAL; first order, G_kk < 0, near the plane).

## (B) The sheets

- **The junction at a sheet:** Maartens eq. 3.17 p.9, *"K+ − K− = −κ5²(T^brane − (1/3) T^brane g)"* (READ by the
  verifier).
  - *First written:* "Israel; standard, NOT READ here".
- **For a fixed coordinate direction k, the identity gives how K_kk changes between sheets:** ∂_y(K_kk) = R⁽⁴⁾_kk −
  R⁽⁵⁾_kk + 2(KK)_kk − K K_kk.
- **The sum rule holds only if the extra dimension is a loop.** That means h and K return single-valued and one
  coordinate system covers the whole loop (H-CLOSED-AS-LOOP, H-GN-GLOBAL). Then (STRUCTURAL):

  **κ² Σ_sheets (τ − (τ/3)h)_kk = ∮ ∂_y(K_kk) dy** (the smooth part)

  - **This loop is the board's reading, and it is the compact sense.** GKL (hep-th/0011225v2 p.4) calls that *"closed,
    i.e. compact without boundary"*. It is not your item 123's "every position".
  - On an infinite line, a boundary term K_kk(+∞) − K_kk(−∞) survives instead.
- **What the rule says, and what it does not.**
  - The integrand is ∂_yK_kk for the fixed k. It equals the corridor's G_kk only at our plane. Off our plane, the
    fixed k is no longer light-like.
  - Our plane's null jump is zero, tension included. Another sheet's tension enters, through h_kk at that sheet.
  - **With no sheet carrying anything along k, ∂_yK_kk is negative at our plane and must be positive somewhere** for
    K_kk to return. Nothing more follows.
  - **A sheet keeping the NEC (τ_kk ≥ 0) makes K_kk jump down.** That adds to the rise the rest of the loop must
    supply. Only τ_kk < 0 lowers it (closedbulk.py B3).
  - GKL eqs. 2.14, 2.26–2.28 pp.4–6 (READ by the verifier) are the literature's trace and tension sum rules on a
    compact space. This null-null form is the board's.
- **The mirror H-Z2 is dropped for (B).** On a loop it forces a second fixed point, which is closedbulk.py's B3 again.
- *First written:*
  - "every sheet's matter … is fixed by every layer's reading";
  - "what our plane reads as negative, the rest of the closed dimension reads as positive, in total exactly".
  - Our plane is one layer, of zero width in the integral.

## With your items 126–127

- **The planes coincide, so the second plane occupies our plane's place.** Its matter along light rays is exactly zero
  (current.py X4). The corridor's readings on our plane need no k.
- The layers off our plane still exist in picture (A), and what they read depends on k.

## Named hypotheses

- **Yours:**
  - H-CLOSED-AS-TOTALITY, H-SECOND-PLANE-EXISTS, H-INFINITE-PLANES, H-NEC-NEVER-VIOLATED (123);
  - H-PLANES-AS-LAYERS, H-PLANES-AS-SHEETS (124);
  - M-EXACT-VALUES (125);
  - H-SHORTEST-DISTANCE, H-COLOCATED-REALIZATION (126);
  - H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127);
  - H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120).
- **The board's:**
  - closedbulk.py's H-VACUUM-BULK, H-NEAR-PLANE, H-OUR-TENSION, and H-Z2 for (A) only;
  - H-BK-CORRIDOR;
  - H-CLOSED-AS-LOOP and H-GN-GLOBAL, for (B);
  - current.py's H-CURRENT-IS-SCHWARZSCHILD.

## OPEN

1. The current-state value of the bulk's scale k, which the layers off our plane need.
2. Every layer beyond the near-plane series.
3. Whether your closed dimension is a loop (B's sum rule) or not (a boundary term instead).

## History (verifier, 2026-10-06)

Thirteen findings were applied:

- "Closed" had turned back into "compact". The loop is now named as the board's.
- Our plane cannot be one side of a zero-sum.
- The integrand is ∂_yK_kk, not "every layer's reading".
- Other sheets' tensions enter.
- The mirror forces a second fixed point.
- The NEC-sign consequence was added.
- "Each term negative" needed a·m > 0.3073.
- The remainder is positive and free of a.
- A1 was weak (C added, no control).
- One check repeated another.
- The junction is READ.
- The Schwarzschild contrast is exact at every order.
- Over-claims were scoped.

With your item 125 applied, the illustrative member was replaced by the README's exact m.
