# C, first part: the corridor on one static plane, and k from the corridor (M-RULINGS items 127, 140, 141; READ and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## Where this starts

- **Item 141:** the planes are static, and a stable throat forms between them.
- **static.py:** static and face to face, the two planes are one Randall–Sundrum II plane at long range.
- **Item 140:** *"Our math is not dependent on k, k is dependent on our work."*
- **Item 127:** r₀, E and k are coefficients, *"a variable solution"*.
- **So this reads the corridor on one static plane, with its throat stable.** The corridor is Bronnikov–Kim eq. (17)
  at r₀ = 2m. Reading "a stable throat" as a static corridor during the hold is the board's (H-STABLE-THROAT).
- **The instrument:** `throatbulk.py`. Selftest 12/12, with two controls and one contrast.
- **READ:** Maartens–Koyama, *Living Rev. Rel.* 13 (2010) 5, arXiv:1004.3962v2 ("MK"), pp.10, 26–28.

## What passes

### 1. Your corridor is a plane with no matter on it, shaped by the bulk (T1)

- **MK eq. (143), p.26:** a plane with no matter on it obeys R_μν = −E_μν, where E is the bulk's Weyl curvature read on
  the plane. Its curvature scalar must vanish.
- **Eq. (17) has R = 0 exactly.** So it is a solution of that kind: no matter, and every bit of its curvature read from
  the bulk.
- **The board's check:** E computed by MK's eqs. (150) and (152), with tracelessness, equals −R_μν component by
  component. That is a transcription check: it confirms the formulas were copied right.
- **Control:** the member of eq. (17) with no throat (r₀ = 3m/2, Schwarzschild, Bronnikov–Kim p.4) has E = 0.
- **MK's eq. (151) as read does not reproduce R_rr for eq. (17).** It is not used; E_rr comes from tracelessness
  instead. Recorded, not repaired.

### 2. How far the corridor's own field can reach (T2)

- **On the plane, the corridor's departure from Schwarzschild is ψ = m(2m − r)/(r(2r − 3m)).**
  - It falls as −m/(2r) far away. That is γ = 5/4, restated (STRUCTURAL).
- **One static plane supplies ψ = −4mℓ²/(3r³)** for a large object (MK eq. 155, READ). That is γ = 1.
- **The ratio is 3r²/(8ℓ²).** The two meet at **r_× = √(8/3)·ℓ = 1.633ℓ**.
- **Beyond r_×, eq. (17) asks for more of the bulk's field than one plane gives, and the shortfall grows as r².**
  - So eq. (17) can describe the plane only out to a few ℓ from the throat. Beyond that, the field is Schwarzschild's,
    with γ = 1.
  - That is the γ = 1 that static.py found at long range, now seen from the corridor's side.
- **Control:** the Schwarzschild member asks for no such field.

### 3. Where the field turns five-dimensional (T3)

- MK give V = GMℓ/r² for r ≪ ℓ (eq. 40) and V = (GM/r)(1 + 2ℓ²/3r²) for r ≫ ℓ (eq. 41). Their leading terms meet at
  **r = ℓ**.
- Inside that, the field is five-dimensional and cannot take eq. (17)'s four-dimensional 1/r form.

### 4. k from the work (T4)

- **For your corridor to exist, two conditions must both hold:**
  - its throat must lie inside its own zone: r₀ ≤ r_×;
  - its throat must lie on the four-dimensional side: r₀ ≥ ℓ.
- **Together: √(3/8) ≤ ℓ/r₀ ≤ 1.** Since k = 1/ℓ and r₀ = r_min(N):

  **k = c / r_min(N), with c between 1 and √(8/3) = 1.633.**

- **This is k depending on your work, as item 140 says.** It is fixed by the README's bit count N, through the
  corridor's throat.
  - It varies with N, as a coefficient does in your item 127.
  - Each corridor's bulk is curved on the scale of that corridor's own throat.
- **At the board's example README:** r_min = 3.976×10⁻²⁸ m, so k is between **2.5×10²⁷ and 4.1×10²⁷ m⁻¹**. That is
  far above every measured bound (the strongest read, 1.25×10⁴ m⁻¹, OUTSIDE.md).
- **The window is indicative, not exact.** Both edges come from leading-order forms, used at the crossover where they
  are least reliable.
  - That c is of order one is the result.
  - The exact c needs the full bulk solved off the plane. MK p.27 say of such integrations that they are *"plagued with
    difficulties"*. That is OPEN.

### 5. That bulk is classical for any README of many bits (T5)

- **The bulk's curvature length against the 5D Planck length is ℓ/l₅ = (ℓ/l_P)^(2/3).**
  - At the example README it is 6.1×10⁴ to 8.5×10⁴, comfortably classical.
  - At one bit it is 0.44 to 0.60, not classical. That is kderive.py's K2 and K4 again: the chain holds for many bits
    (H-MANY-BITS).

### 6. Just off the plane, the throat widens (T6)

- **MK eq. (154)** gives the plane's spheres a little way into the bulk, from ψ.
- **At your throat, ψ′(r₀) = −1/(2m)**, so the throat's sphere *grows* away from the plane:
  g_θθ(r₀, y) = 4m² + y²/(2m) + y³/(mℓ) + …
- **Contrast (READ):** a large black hole's sphere shrinks away from the plane, which MK call "pancake-like".
- **So your throat is narrowest on the plane itself.** The corridor's neck is a feature of the plane, not of the bulk
  around it.
- **Caution:** at r₀ = 2m the throat sits on the horizon (H = 0 there). The expansion is at second order and short
  distance only.

## What this does and does not show

- **It shows:**
  - eq. (17) is a no-matter plane solution whose curvature is entirely the bulk's;
  - one static plane can carry its field only within a few ℓ of the throat;
  - the corridor can exist only if ℓ is of the order of its throat, which ties k to N;
  - that bulk is classical for many bits;
  - the throat is narrowest on the plane.
- **It does not show:**
  - **the exact c, or that the bulk exists.** No bulk solution carrying eq. (17) is known (MK p.27, for every such brane
    metric), and the window's edges are estimates;
  - **the transition** from eq. (17) near the throat to Schwarzschild beyond r_×;
  - **the time the corridor exists.** A stable throat during the hold is the board's reading of item 141;
  - **the sheets' inner structure.** At long range it is invisible (static.py S2b);
  - **the contained dimensions of the surfaces** (item 141), which may also carry a length.
- **Earlier claims this corrects:**
  - KSCALE.md's way out (c) said *"k is one constant, so that could hold for one README only"*. Under your item 127, k
    is a coefficient, and (c) holds for each README with its own k.
  - kderive.py said the work fixed only the ratio of k_R to k_L. The corridor now fixes the scale, to within a factor
    of order one.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES, H-FACING-MATCH (141);
  - M-K-FROM-THE-WORK (140);
  - H-COEFF-FROM-CURRENT (127);
  - H-BK-CORRIDOR (the corridor is eq. 17).
- **The board's:**
  - H-STABLE-THROAT (the corridor static during the hold);
  - H-FACE-TO-FACE (static.py);
  - H-MANY-BITS;
  - H-LEADING-WINDOW (the window's edges from MK's leading-order forms).

## OPEN

1. **The exact c:** the full static bulk off the plane, carrying eq. (17) near the throat and Schwarzschild beyond.
2. Whether the surfaces' contained dimensions add a length of their own.
3. The transition between eq. (17) and Schwarzschild, around r_× ≈ 1.6ℓ.
