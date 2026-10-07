# The censorship theorems against your plane's bulk (M-RULINGS items 136-137, wall D; computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you asked

- **Item 136, wall D:** *"yes, or prove that a censorship theorem does not apply"*.
- **Item 137:** *"Yes, take them in order"*. D comes first.
- **The instrument:** `censor.py` takes the five censorship and time-delay theorems READ at source in step 2
  (OUTSIDE.md). It checks each one's premises against the board's bulk:
  - vacuum AdS₅ off the plane;
  - the plane an umbilic brane with no matter on it (the corridor is a vacuum brane solution);
  - the two sides mirror images (H-Z2).
  - Selftest: 13/13, with a control on every computed check. It runs in 3 seconds.

## What passes

- **None of the five theorems applies.** Each fails at least one premise the board checks:

| theorem | premise that fails | check |
|---|---|---|
| Friedman–Schleich–Witt Thm 1 (gr-qc/9305017v2 p.3), on the plane | ANEC: the plane reads the passage's averaged null energy as negative, −0.826436 E/m per leg | C6, coin.py |
| Gao–Wald Thm 1 (gr-qc/0007021v2 p.6), in the bulk | null generic condition (fails everywhere in vacuum AdS₅); null completeness (the Poincaré patch is incomplete); a smooth metric (the mirror-symmetric plane makes it only C⁰) | C3, C5, C7 |
| Gao–Wald Thm 2 (pp.12–13), in the bulk | a conformal boundary where Ω = 0: off the plane Ω = k·z ≥ 1; the generic condition | C4, C3 |
| Galloway–Schleich–Witt–Woolgar Thm 2.1 (gr-qc/9902061v2 p.8) | a boundary I with Ω = 0 | C4 |
| Galloway–Schleich–Witt–Woolgar Thm 1 (hep-th/9912119v2 p.8) | a timelike boundary I with Ω = 0 | C4 |

- **And the null energy condition holds in five dimensions.**
  - On the plane, the stress is pure tension λ with no matter. For every null vector, S_AB·k^A·k^B = λ·k_y², which is
    never negative when λ > 0. The mirror-symmetric junction gives λ = 6k/κ₅² > 0 (LOOSE.md L4).
  - In the bulk, the only stress is the cosmological constant's, and g_AB·k^A·k^B = 0 for null k.
  - **Control:** a negative-tension plane gives negative null energy.
- **So the plane's negative reading is not matter.** It is the bulk's Weyl curvature projected onto the plane:
  E_kk = −G_kk (umbilic.py, seated).
- **Your *"An NEC is never violated"* (item 117), *"it only ever appears to break"* (item 120), is a result of this
  model, under its named premises.**
  - **In five dimensions the null energy condition holds everywhere** (C1).
  - **The four-dimensional violation is how the plane reads the bulk's geometry** (C2).
  - **That is also why the plane's censorship theorem does not bind the passage** (C6).

## The checks

- **C1.** S_AB·k^A·k^B = λ·k_y² for the plane; 0 for the bulk.
- **C2.** E_kk = −G_kk. This is umbilic.py's seated result, cited, not recomputed.
- **C3.** The null generic condition fails in vacuum AdS₅.
  - Exactly: AdS₅'s Riemann tensor is maximally symmetric, R_abcd = −k²(g_ac·g_bd − g_ad·g_bc), identically (residual
    0). So k_[a R_b]cd[e k_f] k^c k^d = 0 for every null vector at every point.
  - **Control:** a non-radial light ray in Schwarzschild gives 20.25.
  - **Contrast:** a radial one gives 0, as it must, since it runs along a principal null direction.
- **C4.** In z = e^{k·y}/k the bulk is (1/(k·z)²)(η + dz²), so Ω = k·z. Off the plane, z ≥ 1/k and Ω ≥ 1: there is no
  boundary where Ω = 0.
  - **Control:** on the other side (bending growing away) Ω falls to 0, a conformal boundary.
- **C5.** A ray leaving the plane reaches the Poincaré horizon at affine parameter 1/(k·ε·sin θ) (loose.py L5).
- **C6.** The leg is −0.826436002466036 E/m at r₀ = 2m (coin.py).
- **C7.** [K] = −2k·g ≠ 0 across the plane (loose.py L4). The metric is continuous but not smooth there.

## What this does and does not show

- **It shows** that the theorems the board read do not forbid the corridor, because each has a premise this bulk does
  not meet.
- **It also shows that five-dimensional matter keeps the null energy condition everywhere**, under the named premises.
- **A theorem that does not apply forbids nothing; it also permits nothing.** The corridor is not shown allowed by
  this.
- **It does not cover theorems not read.** Maldacena–Milekhin's remark that in 5D *"the topological censorship should
  work"* (OUTSIDE.md) is a remark, not a theorem, and is not tested here.
- **Two premises rest on choices:**
  - **H-POINCARE-PATCH:** the bulk is the region between the plane and the Poincaré horizon, as in Randall–Sundrum II.
    On an extension past that horizon, completeness and the boundary question are open.
  - **The generic condition.** It fails in the vacuum bulk. Near the corridor the bulk's Weyl part can supply it; there
    the Poincaré incompleteness and the plane's non-smoothness still fail Gao–Wald Thm 1.
- **Not checked:** global hyperbolicity of the plane's geometry (FSW). That theorem is already out on ANEC.

## Named hypotheses

- **The board's:**
  - H-Z2 (positive total tension);
  - H-VACUUM-PLANE (no matter on the plane; Bronnikov–Kim);
  - H-VACUUM-BULK;
  - H-POINCARE-PATCH.
- **Yours:** items 117, 120, 122, 136 (wall D).

## OPEN

1. A theorem the board has not read that does bind a brane-bounded bulk. None was found in step 2.
2. The bulk past the Poincaré horizon (with C, the numerical bulk).
3. The corridor's own bulk correction near the plane: the generic condition there.
