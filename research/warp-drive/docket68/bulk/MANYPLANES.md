# Infinitely many planes, as layers and as sheets (M-RULINGS items 123–124; deduced and computed; not verified; not seated; 2026-10-06)

## What M said

- **Item 123:**
  - *"by closed I mean every plausibility, possibility, eventuality, every position infinitely possible as a closed
    dimension."*
  - *"A second plane exists. In a closed infinite multiverse dimension, there are infinite spacetime planes"*
- **Item 124:** *"Both A and B"*.
  - (A) Every position of the extra dimension is a spacetime plane: the planes are the bulk's own layers.
  - (B) There are also separate sheets at distinct positions, each with its own matter.

Every number is printed by `manyplanes.py`.
- **Selftest:** 6/6 checks, 1 genuine control and 1 contrast, with 4 STRUCTURAL lines printed and not counted. It takes
  about two minutes.
- **Imported, not rebuilt:**
  - `closedbulk.py`, for the bulk, built through y⁴;
  - `pairing.py`, for the five-dimensional Ricci tensor;
  - `coin.py`, for the passage integral.

## The tool: one exact identity

- In coordinates running straight out from any layer (K = ½∂_y g):

  **R⁽⁵⁾_μν = R⁽⁴⁾_μν − ∂_yK_μν + 2K_μαK^α_ν − K K_μν**

- **This is checked exactly here,** for any metric −A dt² + B dr² + C dΩ² + dy² with A, B and C arbitrary functions of
  r and y. The control: with the quadratic sign flipped, it fails.
- It is Maartens' eq. 3.9 (gr-qc/0312059v2 p.9, READ by closedbulk.py's verifier).
- **In a bulk of vacuum energy, R⁽⁵⁾_kk = 0 along each layer's own light rays.** So the layer at y reads its own
  spacetime as R⁽⁴⁾_kk = ∂_yK_kk − 2(KK)_kk + K K_kk, computed from the bulk alone.

## (A) The layers: what passes

- **A1. The corridor is on every nearby layer.**
  - Every coefficient of A/A₀ and B/B₀ through y⁴ is finite at the throat r = r₀ and at the horizon r = 2m.
  - So each layer near ours has its own throat at r₀ and its own horizon at 2m, to this order.
- **A2. Every nearby layer reads its own passage negative.**
  - Each layer's own reading along its own radial light ray is L(y) = G_kk·(1 + 4a y) + O(y²). The 4a is the warp's
    rescaling of the layer's light cone.
  - Integrated along each layer's whole passage (m = 1, r₀ = 1.8, a = 1, in units of E/m):

    | | y⁰ | y¹ | y² |
    |---|---|---|---|
    | the layer at distance y | **−1.914712** | −3.829424 | −3.467761 |
    | the warp alone would give | −1.914712 | −3.829424 | −3.829424 |

    - Every term is negative.
    - The y⁰ term is our plane's own −1.914712.
    - The difference at y² is the plane's curvature.
  - **Contrast:** a Schwarzschild plane's layers read 0 at every order computed.
- **A3. Only our layer bends evenly in every direction (STRUCTURAL).** This is from closedbulk.py B1 and umbilic.py U3.
  - On the layer at y, K_kk = y G_kk + …
  - So a light ray running along a nearby layer is drawn toward our plane, from either side under the mirror (H-Z2).

**So in picture (A), the corridor is not alone on our plane.** Every layer near ours carries a corridor with the same
throat and horizon, and reads the same kind of passage. Our plane is the one that light along the neighbouring layers
is drawn toward.

## (B) The sheets: the totality's one ledger

- **At a sheet, the bulk's K jumps by the sheet's own matter.** This is the standard Israel junction (H-ISRAEL; NOT READ
  here), with no mirror at a generic sheet:

  [K_μν] = −κ²(τ_μν − (τ/3)h_μν)

- **Around a closed dimension, the jumps and the smooth change of K add up to zero.** So for any fixed direction k the
  identity gives an exact sum rule (STRUCTURAL; H-CONVERGES if the closed dimension is infinite):

  **κ² Σ_sheets (τ − (τ/3)h)_kk = ∮ dy [R⁽⁴⁾_kk − R⁽⁵⁾_kk + 2(KK)_kk − K K_kk]**

  - **Left side:** every sheet's matter, summed over all of them.
  - **Right side:** every layer's own reading, plus terms from how each layer bends, summed over the whole closed
    dimension.
  - **At our plane the right side's integrand is the corridor's reading, G_kk** (R⁽⁵⁾_kk = 0 by construction; K = −a q
    and q_kk = 0 there).
- **If our plane is the only sheet with anything along k, the right side integrates to exactly zero.** Our plane's
  tension drops out, because k is light-like there.
  - So what our plane reads as negative, the rest of the closed dimension must read as positive, in total, exactly
    (derived).
  - This is the board's reading of your item 120 (*"matter is neither created nor destroyed, it only changes geometric
    state"*) in this setting, not your words.
- **If other sheets carry matter along k,** the ledger fixes their total and not where it sits.

## The boundary (item 82)

- **A1 and A2 are the near-plane series** (closedbulk.py's H-NEAR-PLANE: y ≪ r₀ and e^{2ay} ≪ 2a r₀). Whether every
  layer, out to every position, carries the corridor is not computed.
- **The sum rule is exact** given the identity, the junction and a closed dimension. It does not say which sheets exist,
  where they are, or what each carries.
- **On a closed dimension with only our plane, the balance needs layers that read positive somewhere.** Those layers are
  not computed: they lie beyond the series.
- **The layers' readings are geometry, not matter.** In a vacuum bulk no layer except a sheet carries matter, and R⁽⁵⁾_kk
  = 0 off the sheets (umbilic.py). So the averaged condition can fail only at a sheet.

## Named hypotheses

- **Yours:**
  - H-CLOSED-AS-TOTALITY, H-SECOND-PLANE-EXISTS, H-INFINITE-PLANES, H-NEC-NEVER-VIOLATED (123);
  - H-PLANES-AS-LAYERS, H-PLANES-AS-SHEETS (124);
  - H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120).
- **The board's:**
  - closedbulk.py's H-VACUUM-BULK, H-Z2, H-NEAR-PLANE, H-OUR-TENSION;
  - H-BK-CORRIDOR;
  - H-ISRAEL: the junction at a sheet;
  - H-CONVERGES: the closed integral exists in an infinite dimension.

## OPEN

1. Every layer beyond the near-plane series: whether the corridor persists, and where the layers read positive.
2. The sheets: which exist, where, and what they carry. The ledger fixes only their total.
3. Whether a sheet is position 2's plane. It is not asked; your item 123 says a second plane exists.
