# Wall E, worked: the corridor's horizon and its instability (M-RULINGS item 149; READ, derived and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft quoted a theorem proved for extremal Kerr as
if it were general, and used an asymptotic bound to speak of early times. Both are withdrawn, and an exact horizon
identity replaces them (History).

## What you said

- **Item 149:** *"I have given you everything I can. You have to work the math now"*.
- **On how long the corridor lasts:**
  - item 86, answer 5 (H-BRIEF-HOLD): the hold is *"incredibly short, maybe even immeasurable but not zero"*, and
    *"this answer is also a relative one"*;
  - item 136 E: *"Instantaneous or near instantaneous"*.
- **The instrument:** `stability.py`. Selftest 7/7.
  - **Controls:** two. One is a horizon off the corridor; one is READ (extremal Reissner–Nordström).

## READ

- **Aretakis**, "Horizon instability of extremal black holes", arXiv:1206.6598v2.
  - **Abstract:** derivatives of generic waves *"do not decay along such horizons as advanced time tends to infinity,
    and in fact, higher order derivatives blow up"*.
  - **p.10, eqs. (6)–(8):** g = −D dv² + 2 dv dr + K⁻¹ g_S², with extremality D = D′ = 0.
  - **p.10, Prop. 3.2:** a conservation law for every angular mode, *"provided"* that D″ = 2K (eq. 10). *"Extremal
    Reissner–Nordström satisfies the condition (10)"* (p.11).
  - **p.11, Theorem 1 (non-decay):** needs only his assumptions A1–A4.
  - **p.12, Theorem 2 (blow-up):** conditional. It holds *"unless ψ and the tangential to H⁺ derivatives of ψ do not
    decay and H[ψ] = 0"*, and gives no rate.
  - **p.15, Theorem 3:** the τ^(k−1) rate is for extremal Kerr only.

## What the mathematics gives

### 1. The corridor's horizon is extremal (S1), and meets Aretakis's condition exactly (S2)

- **D′ = 0 at the horizon**, so the surface gravity is zero.
  - **Control:** the r₀ = 1.8m member has D′ = √10/(10m).
- **D″ = 1/(2m²) = 2K.** His eq. (10) holds exactly, so his hierarchy of conservation laws applies.
  - **Control (READ):** extremal Reissner–Nordström meets (10).
- **The verifier adds a computation:** at r₀ = 2m the two horizons of the family merge at the throat. D is even and
  non-negative on both sides, like extremal Reissner–Nordström's r = M, with no timelike region between.

### 2. What Aretakis's theorems give the corridor

- **Theorem 1 applies without condition:** first derivatives along the horizon generically do not decay.
- **Theorem 2's blow-up of higher derivatives is conditional.** It needs waves to decay along the horizon on this
  background, which has not been shown. The wall's own record says the same: *"proven for extreme Reissner–Nordström,
  not yet for this metric"* (residue/STATUS.md).

### 3. An exact identity on the horizon fixes how fast the change goes (S4)

- **Derived here from the wave operator,** for a spherical wave, with generic D and r.
- **The first derivative along the horizon is conserved exactly:** ∂_v(∂_ρψ) = 0, so H₀ = ∂_ρψ.
  - The extra term Aretakis's law usually carries vanishes here, because the throat sits on the horizon (r′ = 0).
- **The second derivative changes at an exact rate:** ∂_v(∂²_ρψ) = −H₀/(4m²) − (1/(2m²))·∂_vψ, using r″ = 1/m at the
  horizon.
- **So over an advanced time v, the second derivative changes by −H₀v/(4m²) − (ψ(v) − ψ(0))/(2m²).** That is linear
  growth with an exact coefficient, and no unknown constant.
- **Over one of the corridor's clocks (v = m), its linear part is H₀/(4m),** a quarter of the second derivative's natural
  size, H₀/m.

### 4. The corridor's clock (S3)

- **m/c = r_min(N)/(2c):** 6.6×10⁻³⁷ s at the board's example README; 1.27×10⁻⁴⁴ s × √N in general.
- **So a hold of a few clocks changes the second derivative by a quarter per clock, at most a few times its natural
  size.**
  - That is a finite, computed change, not a blow-up.
  - Aretakis's blow-up is a statement as advanced time goes to infinity.
- **Caution:** your *"relative"* (item 86) matters here. The clock is measured in the horizon's own advanced time.

## What is not settled

- **The white-hole half of wall E.** The wall's record notes that large white holes are unstable. The corridor's exit
  is a white-hole horizon (plane.py P1). That is not worked here.
- **The hold's length,** in the corridor's clocks.

## Named hypotheses

- **Yours:**
  - H-BRIEF-HOLD (item 86, answer 5), with its *"relative"*;
  - item 136 E;
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-TEST-FIELD (a scalar wave stands in for perturbations).

## OPEN

1. The white-hole instability at the corridor's exit.
2. The hold's length in the corridor's clocks.
3. Whether waves decay along this horizon, which Theorem 2's blow-up needs.

## History (verifier, 2026-10-07)

Eight findings, all applied:

1. **Theorem 3 is for extremal Kerr.** The τ^(k−1) law is withdrawn. Theorems 1 and 2 are now stated for the corridor.
2. **"The instability is real for this horizon" over-stated.** Non-decay holds; blow-up is conditional.
3. **An asymptotic bound was used for early times.** Replaced by the exact horizon identity (S4).
4. **The white-hole half of the wall** was missing. It is now OPEN.
5. **The hypothesis was mislabelled.** It is H-BRIEF-HOLD (86.5), with its "relative".
6. **The quote is now verbatim** ("asympotically", sic).
7. **The degenerate member's structure** is now stated.
8. **Under-claims taken up:** H₀ = ∂_ρψ exactly, Theorem 1 cited, and the finite-time statement.
