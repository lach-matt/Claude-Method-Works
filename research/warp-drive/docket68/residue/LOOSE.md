# The loose ends the board can compute (M-RULINGS item 135, step 3; computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you asked

- **Item 135:** *"computable loose ends next"*.
- **The instrument:** `loose.py` computes six loose ends on the corridor fixed by your input N (eq. 17 at r₀ = 2m;
  current.py).
  - Selftest: 19/19.
  - E per √bit is imported from exactE.py, never retyped.
  - Every section but L1's identity checks has a control that can fail on its own.

## What passes

- **Two flat sheets at one place make a consistent junction (C8P-O2, L4).** Israel's condition is linear in the surface
  stress, so coinciding sheets act as one surface carrying both stresses.
  - With mirror symmetry (Z2), the two tensions must sum to 6k/κ₅², the Randall–Sundrum value.
  - Through a smooth bulk they must sum to 0.
  - **Control:** Israel's condition without its trace term gives −2k/κ₅², which is not the RS value.
  - The board's earlier failure (CURRENT.md X4) set K = 0. The junction needs the bulk's own K = −k·g.
  - **Premise H-FLAT-SHEET.** This is for flat, pure-tension sheets. Whether a bulk carries the corridor's own geometry
    on coinciding sheets is C8P-O1, not checked here.
  - **A reading, not a computation.** Sheets at one place share one induced metric, so the corridor read on each is one
    geometry. That fits your *"different views of the same object"* (item 132).
- **No mode instability for a test scalar (C8P-O5, L3).**
  - The scalar potential at r₀ = 2m is V₀ = 3m(3r − 4m)(r − 2m)²/(r⁴(2r − 3m)²) ≥ 0 for r ≥ 2m.
  - The l-part, (1 − 2m/r)·l(l+1)/r², is ≥ 0 too.
  - So a linear, massless, minimally coupled test scalar on the fixed static background has no growing mode
    (ω² < 0).
  - V has a double zero at the throat, against Schwarzschild's simple zero. That is the signature of power-law tails, as
    Bronnikov–Konoplya report for this member.
  - **What this does not cover.** It is not the Aretakis growth of transverse derivatives *on* the horizon, which stays
    open. It is not gravitational perturbations either.
- **Rays that leave the plane never return (C8P-O7, L5).** In the vacuum bulk off our plane, a ray leaving at angle θ,
  with its own energy ε:
  - crosses each layer y_s once, at conformal time (e^{k·y_s} − 1)/(k·sin θ);
  - reaches the Poincaré horizon at affine parameter 1/(k·ε·sin θ);
  - never comes back.
  - **Control:** with the bending the other way, the boundary is reached in time 1/(k·sin θ).
  - **Premise H-VACUUM-BULK:** the corridor's own local bulk correction is left out.
- **The opening's energy density on the shell is positive (C8O-O1, L6).** As a null shell it is [m_MS]/(4πr²), where
  m_MS(r) = m(5r − 8m)/(2(2r − 3m)) rises from m at the throat to 5m/4 at infinity.

## What does not close: four findings that need you or a wall

### L1 (RES-N1): the energy at position 2

- **The board's identification.** H-EXACT-ENERGY-AT-BOUND, the board's, identifies your one exact energy (item 133) with
  E(N).
- **Your rulings on the build.** Item 111 says the build uses *"that and only that"* energy.
- **The numbers:**
  - At the example N, E = 2.405878×10¹⁶ J.
  - A 70 kg body has 6.7117×10²⁷ atoms. Assembly needs at most 1.1947×10¹⁰ J at 11.11 eV per atom (H-BOND-CEILING,
    a generous ceiling: real atomisation energies run 5–7 eV per atom).
  - Writing the bits (Landauer, 300 K) costs 7.87×10⁻⁶ J.
- **The difference is 2.405877×10¹⁶ J, or 5.750 megatons of TNT.** E(N) falls to the assembly ceiling only at
  N = 676 bits.
- **Your item 108 already has an accounting.** You confirmed (*"Yes, that's it"*) that the README carries E/c²
  (0.2677 kg here) and position 2's stock fills the rest of the 70 kg. That holds while N is below N* = 1.8754×10²⁰
  bits.
- **Where does E go, then?** balance.py keeps the stock's composition fixed (stock in = object out). So the 0.2677 kg
  can only be **energy held inside the copy**: 2.4×10¹⁶ J beyond what its chemistry needs, not added matter.
- **So the readings are:**
  - (b) **kept inside the copy as internal energy**, your item 108's accounting;
  - (a) **released at position 2**, as heat into the site or stock, or as radiation (the closing shell is not
    computed here);
  - (c) **the one exact energy is not E(N)** (C8P-O9), or the build is not all of it.
- **Checked two ways.** N* agrees to 10⁻¹² from the coefficient and from 8π²GM²/(hc·ln2). The two are algebraically
  one expression, so this tests exactE's arithmetic, not anything independent.

### L2 (C8O-O7): where the trajectories' length could live

- **At fixed time the throat lies at infinite distance.** √g_rr has a simple pole at r = 2m with residue m.
  - **Control:** at r₀ = 2.2m the singularity is only of square-root order, and the distance is finite.
  - An infalling path reaches the throat in finite affine parameter (X7). A length depends on the slicing and on where
    its endpoints are.
- **Eq. (17)'s two parameters are both set by your rulings.** The holds fix r₀ = 2m; the input fixes m. This is
  STRUCTURAL: the check is a 2×2 system written to have one solution.
- **So the trajectories cannot lengthen the corridor through eq. (17)'s parameters.** Items 116 and 117 say they set
  its length.
- **Where else the length could live:**
  - where the endpoints sit;
  - the bulk scale k, which is free and only bounded (L5, OUTSIDE.md);
  - the range of values item 127 gives each coefficient;
  - or something eq. (17) does not hold.
- **Not ruled out:** a length that depends on the README's content. Item 117 fixes the width to the README alone; that
  does not stop the content from setting a length.

### L3 (C8P-O5): r₀ = 2m is exact, or it is a different object

- **Off the floor, the horizon is hot or gone.**
  - At r₀ = 2m(1 + δ) with δ < 0, the surface gravity is √(−δ)/(2m). The temperature is 9.167×10²³ K × √(−δ) at the
    example N, so δ = −10⁻⁴⁰ gives 9,167 K.
  - With δ > 0 the member is the two-way wormhole, with no horizon. Item 132 rules that out.
- **So the holds and the one exact energy select δ = 0 exactly.** The tuning required is exactness, which your
  M-EXACT-VALUES carries.
- **Open:**
  - the Aretakis instability on the extremal horizon;
  - gravitational perturbations, which need the bulk (C8P-O1).

### L6 (C8O-O1, C8O-O2): the opening as a null shell

- **The shell's surface pressure is negative.**
  - With the corridor to the future of the shell, p = ψ'/(8π) = −m/(16π(2r − 3m)(r − 2m)).
  - That is negative everywhere outside the throat, and it diverges there: (r − 2m)·p → −1/(16π).
  - The null condition on a null shell needs μ ≥ 0 *and* p ≥ 0. So it fails on the shell.
  - Putting the corridor to the shell's past flips both signs, so one of the two is negative either way.
  - **On your items 117 and 120** this is one more place where the null condition appears to break.
- **One shell cannot join the eternal corridor.**
  - Along a radial null ray, dx/dλ = ε/h, with h² = g_tt·g_xx = 2(m + 2x²), finite and nonzero at x = 0. So
    r = 2m + x² has a minimum along the generator.
  - Flat space's generator falls to r = 0.
  - So no single spherical shell at v = const joins a place with no corridor to the eternal, maximally extended
    corridor.
  - **Control:** for Schwarzschild, g_tt·g_rr = 1, r is affine and monotone on both sides, and the shell joins.
- **But the mouth may form by collapse, with no change of topology.**
  - Kehle–Unger, arXiv:2211.15742v2 p.3, Theorem 1 (READ, alphaXiv): *"there exist regular one-ended Cauchy data for
    the Einstein–Maxwell-charged scalar field system which undergo gravitational collapse and form an exactly
    Schwarzschild apparent horizon, only for the spacetime to form an exactly extremal Reissner–Nordström event horizon
    at a later advanced time."*
  - Their matter model *"satisfies the dominant energy condition"*.
  - The corridor's floor member has the same extremal structure (X7).
  - So the mouth at position 1 is the kind of object known to form from ordinary collapse.
  - **What collapse leaves open is the throat.** Behind the horizon the collapse decides what lies there. In their
    example a regular centre extends into the black hole. Whether the throat through to position 2 forms is the open
    part of the formation wall.
  - **This is on our plane's 4D equations.** The corridor is a brane solution carried by the bulk's Weyl part, and
    collapse on the brane needs the bulk.
- **The inflow seen from far away carries the ADM total, 5m/4** (X6: ADM − Komar = Δ/2 = m/4 at the floor). That is
  5E/4 against the one exact energy E.

## Named hypotheses

- **The board's:**
  - H-EXACT-ENERGY-AT-BOUND;
  - H-BOND-CEILING (NOT READ; generous);
  - H-SITE-T (300 K);
  - H-FLAT-SHEET, and H-Z2 or a smooth bulk (L4);
  - H-VACUUM-BULK (L5);
  - H-LOCAL-FLAT and H-SPHERICAL-SHELL (L6).
- **Yours, used:** items 108, 111, 117, 120, 125, 127, 129, 131–133.

## OPEN

1. **RES-N1:** where E goes. On your item 108 it stays inside the copy. Confirm, or rule otherwise.
2. **L2:** where the trajectories' length lives.
3. **Formation:**
   - the throat behind a collapse-formed mouth;
   - the shell's negative pressure, an appearance on your items 117 and 120;
   - collapse on the brane needs the bulk.
4. **The Aretakis instability, and gravitational stability**, which needs the bulk.
5. **The ADM 5E/4 at the opening against the one exact E.** It goes with C8P-O9.

## History (verifier, 2026-10-07)

Thirteen findings were applied:

- **The shell's surface pressure was left out.** It is negative and divergent, so "the opening respects the null
  condition on its shell" is withdrawn.
- **"Needs a change of topology" was withdrawn.** The obstruction holds only for one shell onto the eternal extension.
  Kehle–Unger (READ) form an extremal horizon from collapse.
- **The generator check was by construction.** It is now derived from h.
- **L4 was computed for flat sheets only.** H-FLAT-SHEET is named, and a control is added.
- **Item 108's accounting is now engaged.** H-EXACT-ENERGY-AT-BOUND is attributed to the board, and local heating is
  added to (a).
- **L5's affine parameter lacked 1/sin θ.** Its control was by construction.
- **L3** states the premises of "no mode instability", and l ≥ 1 is checked.
- **L2's conclusions** are narrowed.
- **The L1 control and the two N* paths** are marked as one expression.
