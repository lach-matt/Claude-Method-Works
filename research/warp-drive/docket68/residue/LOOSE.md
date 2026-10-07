# The loose ends the board can compute (M-RULINGS item 135, step 3; computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you asked

- **Item 135:** *"computable loose ends next"*.
- **The instrument:** `loose.py` computes six of them on the corridor fixed by your input N (eq. 17 at r₀ = 2m;
  current.py).
  - Selftest: 15/15, a control inside every section.
  - E per √bit is imported from exactE.py, never retyped.

## What passes

- **The coinciding junction exists (C8P-O2, L4).** Israel's condition is linear in the surface stress, so two sheets
  at one place act as one surface carrying both sheets' stress.
  - With mirror symmetry (Z2), the two tensions must sum to 6k/κ₅², the Randall–Sundrum value.
  - Through a smooth bulk they must sum to 0.
  - The board's earlier failure (CURRENT.md X4) was the extra-dimension bending set to K = 0. The coinciding junction
    needs the bulk's own K = −k·g instead.
  - **One more thing follows.** Sheets at one place share one induced metric. So the corridor read on plane 1 and on
    plane 2 is literally one geometry. That fits your item 132: *"different views of the same object"*.
- **The opening respects the null condition on its shell (C8O-O1, L6).** As a null shell, the opening's energy density
  is the jump in the Misner–Sharp mass, [m_MS]/(4πr²).
  - m_MS(r) = m(5r − 8m)/(2(2r − 3m)). It rises monotonically, from m at the throat to 5m/4 at infinity.
  - Positive everywhere: the shell carries positive energy. The violation the plane reads stays inside the corridor's
    Weyl part, as before. On your items 117 and 120 that is an appearance.
- **Test fields do not grow (C8P-O5, L3).**
  - The scalar potential at r₀ = 2m is V = 3m(3r − 4m)(r − 2m)²/(r⁴(2r − 3m)²) ≥ 0 for every r ≥ 2m, on both sides. So
    there are no bound states.
  - V has a double zero at the throat, against Schwarzschild's simple zero. That is the signature of power-law tails,
    and it agrees with Bronnikov–Konoplya's READ result for this member (OUTSIDE.md).
- **Rays that leave the plane never return (C8P-O7, L5).** In the vacuum bulk off our plane, a ray leaving at angle θ:
  - crosses each layer y_s once, at conformal time (e^{k·y_s} − 1)/(k·sin θ);
  - reaches the Poincaré horizon at finite affine parameter;
  - never comes back.
  - With the measured bound k > 1.25×10⁴ m⁻¹ (OUTSIDE.md), 1/k < 80 μm.
  - **Control:** with the bending the other way, the ray reaches the boundary in time 1/(k·sin θ).

## What does not close: four findings that need you or a wall

### L1 (RES-N1): the energy at position 2 does not balance by building alone

- **Items 111 and 133 make the build's energy equal to E(N).**
  - Item 111: *"that and only that which is provided by the closing of the horizon"*.
  - Item 133: *"There is only one exact energy needed for any given README"*.
- **The assembly's energy is far smaller.** A 70 kg body has 6.7117×10²⁷ atoms (step1b/balance.py). At most 11.11 eV per
  atom (H-BOND-CEILING, the strongest chemical bond, NOT READ), assembly needs at most **1.1947×10¹⁰ J**.
- **Writing the bits costs almost nothing.** Landauer's N·k_B·T·ln2 at 300 K is 7.87×10⁻⁶ J at the example N.
- **E(N) at the example N is 2.405878×10¹⁶ J.** The difference is **2.405877×10¹⁶ J, which is 5.750 megatons of TNT**.
- **At the atomic snapshot** (N = 1.09×10²⁹), E = 1.517×10²³ J, which is 1.69×10⁶ kg × c².
- **E(N) falls to the assembly ceiling only at N = 676 bits.** No README of a body is that small.
- **So the energy at position 2 does not close by building alone.** Three readings, each with what it costs:
  - (a) **Released at position 2.** L6's closing as an outgoing null shell would carry it out at light speed:
    5.75 Mt for the core README.
  - (b) **Kept in the built object as mass.** The core copy would weigh 0.2677 kg more than the stock it was built from;
    the snapshot copy, 1.69×10⁶ kg more.
  - (c) **The one exact energy is not E(N) at the bound** (C8P-O9), or the build is not all of it.
- **Recorded in two ways** (both agree to 10⁻¹²): item 108's crossover, N* = 1.8754×10²⁰ bits for 70 kg, from the
  coefficient and from 8π²GM²/(hc·ln2).

### L2 (C8O-O7): the corridor has no free length for the trajectories to set

- **At fixed time the throat lies at infinite distance.** √g_rr has a simple pole at r = 2m with residue m, so the
  distance grows as m·ln.
  - **Control:** at r₀ = 2.2m the pole is only of square-root order, and the distance is finite.
  - Maldacena–Susskind say the same of extremal bridges (OUTSIDE.md).
- **Eq. (17) has two parameters, m and r₀. Your two rulings fix both.** The holds fix r₀ = 2m; the input fixes m.
  Nothing is left free.
- **So the trajectories have nowhere to set a length in this geometry.** Items 116 and 117 say the length depends on
  the trajectories needed, and that trajectories change length, never width.
- **Where could it live?**
  - In the README: but item 117 keeps the width the README's alone.
  - In the extra dimension: but item 127 has the planes coincide, at zero distance.
  - Or in something eq. (17) does not hold.

### L3 (C8P-O5): r₀ = 2m is exact, or it is a different object

- **Off the floor, the horizon is hot or gone.**
  - At r₀ = 2m(1 + δ) with δ < 0, the horizon's temperature is **9.167×10²³ K × √(−δ)** at the example N. Even
    δ = −10⁻⁴⁰ gives about 9,200 K.
  - With δ > 0 the member is the two-way wormhole, with no horizon to hold the README. Your item 132 rules that out.
- **So the holds and the one exact energy select δ = 0 exactly.** The tuning required is exactness, which your
  M-EXACT-VALUES (item 125) carries.
- **What stays open is the dynamics.**
  - An extremal horizon is expected to carry the Aretakis instability (OUTSIDE.md: proven for extreme
    Reissner–Nordström, shown in a 3D black bounce, not for this metric).
  - Gravitational perturbations need the bulk (C8P-O1).

### L6 (C8O-O1, C8O-O2): the opening cannot be a single shell; it needs a change of topology

- **The shell does not join along whole generators.**
  - On the corridor's side the shell's generators have areal radius r = 2m + x², with a minimum at the throat.
  - On the side with no corridor (your item 129: our current state, no corridor) they fall to r = 0.
- **Control:** for a Schwarzschild exterior both sides are monotone, and the shell joins.
- **So no spherical null shell at v = const turns a place with no corridor into the corridor.** The step needs a change
  of topology.
- **The sources say the same of every traversable wormhole.** Maldacena–Milekhin, arXiv:2008.06618v2 p.14: *"Since they
  require topology change, this seems difficult."* (OUTSIDE.md)
- **NOT READ:** the theorems on topology change (Geroch 1967; Tipler 1977).
- **This is the formation wall.** Your item 86 answer 3 (*"likely made"*) and item 101 answer 1 carry it as yours.
- **The inflow seen from far away carries 5m/4, the ADM total, not the pull m.** In energy that is 5E/4 against your one
  exact E. The extra quarter is the Weyl part outside the throat (ADM − Komar = Δ/2 = m/4 at the floor, X6).

## Named hypotheses

- **The board's:**
  - H-BOND-CEILING (at most 11.11 eV per atom to assemble, NOT READ);
  - H-SITE-T (300 K, illustrative);
  - H-Z2 or a smooth bulk (L4, both computed);
  - H-VACUUM-BULK (L5: the leading-order AdS bulk, without the corridor's local correction);
  - H-LOCAL-FLAT (L6: the side with no corridor taken locally flat; your item 129's matter ignored at this scale);
  - H-SPHERICAL-SHELL (L6: one spherical null shell).
- **Yours, used:** items 111, 117, 120, 125, 127, 129, 131–133.

## OPEN

1. **RES-N1:** where E(N) minus the build goes, (a), (b) or (c). Yours.
2. **L2:** where the trajectories' length lives. Yours.
3. **The formation step: a change of topology.** It is a wall. NOT READ: Geroch, Tipler.
4. **The Aretakis instability, and gravitational stability**, which needs the bulk. A wall.
5. **The ADM 5E/4 against the one exact E at the opening.** It goes with C8P-O9.
