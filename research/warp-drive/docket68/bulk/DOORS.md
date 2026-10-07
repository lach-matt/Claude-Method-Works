# Wall D, worked: which door the corridor must pass (M-RULINGS items 139–149; READ, deduced and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## Where this starts

- **censor.py (verified once) found that the bulk censorship theorems depended on two choices:**
  - the sign of our plane's tension (H-OUR-TENSION);
  - where the bulk ends (H-POINCARE-PATCH).
- **Your rulings since then settle the first.**
  - Ours is positive (item 139).
  - The planes are static and face to face (item 141). static.py: their summed surface is +1.
- **Item 149:** *"work the math now"*.
- **The instrument:** `doors.py`. Selftest 4/4.
  - **Genuine checks:** two.
  - **Marked STRUCTURAL:** two.

## READ

- **Friedman, Schleich and Witt**, gr-qc/9305017v2 ("FSW").
  - **p.3, Theorem 1:** *"If an asymptotically flat, globally hyperbolic spacetime (M, g_ab) satisfies the averaged null
    energy condition, then every causal curve from J⁻ to J⁺ is deformable to γ₀ rel J"*.
  - **p.6:** such a curve, if not deformable, *"will join J⁺₀(M) to another copy of the asymptotic region"*, through
    surfaces *"outer trapped as seen from the first asymptotic region"*. Their Lemma 2 forbids those.
  - **p.7:** *"one can passively observe that topology by detecting light that originates at a past singularity … one
    must see a signal that originates in a white hole rather than J⁻"*.

## What the mathematics gives

### 1. Every energy premise of the five-dimensional theorems now holds (K1, K2)

- **On the summed surface the null energy is λ_RS·k_y², never negative.** In the bulk it is 0 (static.py S4 and
  censor.py C1, both imported).
- **Along the passage itself it is exactly zero.** A ray running along the plane has k_y = 0, so the surface term
  vanishes, and the bulk term is 0 (STRUCTURAL).
  - So in five dimensions the averaged null energy along the passage holds, at exactly zero.
  - The plane reads it as −0.826 E/m (coin.py).
- **That is your items 117 and 120 in the mathematics:** the null energy condition is never violated in five
  dimensions; it only appears violated on the plane.

### 2. So the corridor's passage meets censorship at a global premise, not an energy one (K3)

- **FSW's mechanism:** a causal curve from one region's past infinity to another region's future infinity passes
  through surfaces that look trapped. Under the averaged null energy condition and global hyperbolicity those cannot
  be reached.
- **The corridor is such a curve** (plane.py P1). It enters position 1's horizon and leaves through position 2's
  white-hole horizon.
- **With every energy premise holding in five dimensions,** any five-dimensional censorship theorem whose global
  premises also hold forbids the passage.
- **The premises still open are global:**
  - global hyperbolicity;
  - the bulk's asymptotic structure: where it ends, H-POINCARE-PATCH.
- **That is wall C.** The corridor stands or falls on the bulk's global structure.

### 3. Entanglement does not provide a way around it (K4)

- **The no-signalling bound** (standard, not READ): with any amount of shared entanglement, one qubit sent carries at
  most 2 bits (superdense coding; Holevo).
- **So an N-bit README needs at least N/2 qubits sent along a causal channel between the two positions.** That is
  1.37×10¹⁵ qubits at the board's example README; without entanglement, 2.74×10¹⁵ (STRUCTURAL).
- **That causal channel is exactly what censorship governs.** Your passage as entanglement (H-PASSAGE-IS-ENTANGLEMENT,
  item 136) still needs it.

### 4. What censorship allows: light from a white hole

- **FSW p.7:** a signal that *"originates in a white hole"* can be seen. Your corridor's exit at position 2 is a
  white-hole horizon (plane.py P1).
- **So what arrives at position 2 is allowed to be seen there.** What censorship governs is whether it can be traced
  back, causally, to position 1's past infinity.

## Named hypotheses

- **Yours:**
  - H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139);
  - H-STATIC-PLANES (141);
  - H-PASSAGE-IS-ENTANGLEMENT (136);
  - H-NEC-NEVER-VIOLATED (117, 120);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-FACE-TO-FACE;
  - H-COMPOSITE-SURFACE;
  - H-BK-CORRIDOR;
  - H-POINCARE-PATCH (open: wall C).

## OPEN

1. **Wall C: the bulk's global structure.** Does a five-dimensional censorship theorem's global premise hold for the
   corridor's bulk?
