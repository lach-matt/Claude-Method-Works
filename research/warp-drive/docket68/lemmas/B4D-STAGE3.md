# B4d stage 3: the opening at once (computed and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage3.py`, selftest 3/3. It builds on
`o3_atonce.py`, whose verifier is still out; this stage gets its own verifier once that one reports.

> **Under item 163 (2026-10-08): conditional on a withdrawn reading.** Everything below assumes "at once" is an instant.
> You chose *"All together, one whole"*, so the instant hold is set aside and so is H-ENERGY-CARRIED-INFO-TAKEN. Still
> standing, and used by stage 5: C2's Vaidya fact (the trapping radius is r = 2m(v)) and C3's inversion of the gas bound
> (an instant carries ~2.8 bits — which is why the instant reading could not hold the README). The verifier is deferred:
> this stage is off the live path.

## What you said

- **Item 162:** the object *"only every takes on the size that contains the README upon opening. It is and always will
  be only the size that is needed to hold the object once and at once"*.
- **Item 160:** the corridor and the opening are the same object.
- **Item 115 (c):** the opening's inflow is *"The README itself"*.
- **Item 136 G:** the README is the energy.
- **Item 122 (3):** position 2's side is the time-reverse of position 1's.

## What follows

**C1. Causality** (deduced).
- **The window.** The hold is h/(4E), about 10⁻¹⁴ clocks.
- **What that forces.** At the opening, the one energy E is already within (2 + 10⁻¹⁴)m of the throat, or it arrives
  there in a single instant of advanced time.

**C2. The energy can arrive at once, as a thin shell** (computed).
- **The setup.** Ingoing Vaidya with a step, m(v) = m·H(v) (opening.py's form; its energy conditions hold as m rises).
- **What happens.** Before v = 0 there is no horizon; at v = 0 a horizon appears at r = 2m. The Einstein tensor is a
  positive delta at the step.
- **What that matches.** The size is set at once and never grows, which is your 162. A null shell from any distance
  reaches the throat in one instant of v.

**C3. The README's information cannot ride with that energy** (computed, from `o3_write.py`'s gas bound).
- **The limit.** A carrier arriving within a hold of T clocks brings at most N ≤ 8Z(T + 2)³/(3645 ln2) bits.
- **At T ≈ 10⁻¹⁴ clocks** that is **about 2.8 bits**, at the Standard Model's particle count.
- **The control.** Inverting the bound at its own time gives back the example README exactly.
- **So, if "at once" is an instant, the README cannot be carried in.** For any README above a few bits, an instant
  and an inflow carrying the README (your 115 (c)) cannot both hold. *Regraded after the O3-ATONCE verifier:* this
  states the conflict; it does not force "taken". "Taken" runs against causality and no-signalling, and it was
  circular with `o3_atonce.py`.
- **How your words then read.**
  - 115 (c), "the inflow is the README", and 136 G, "the README is the energy", read as: the README's energy arrives at
    once, and its information is taken (R0).
  - The board names this H-ENERGY-CARRIED-INFO-TAKEN. It is the math's consequence for your words, not a new
    assumption.

**C4. The black string's instability has no time to act** (computed).
- **The growth.** Over the hold, the string's fastest growth (0.046 per clock) amounts to about 5×10⁻¹⁶ e-folds.
- **No band-crossing either.** With no growing mass (your 162), no mode sweeps through the unstable range.
- **So the instability that refuted the long opening does not arise.**

**C5. What stays open** (deduced).
- **After the shell, the plane is Schwarzschild.** opening.py O3 says so: *"The Vaidya pieces end in Schwarzschild …
  not in the corridor"*. The corridor is eq. (17).
- **Two regions to join.** Inside the hold's cone the bulk is eq. (17)'s static bulk (`o3_atonce.py` A6); beyond it is
  the prior state.
- **Stage 4 computes the join.** The two must meet across the cone's null boundary as a null shell carrying
  non-negative energy (Barrabès–Israel, not yet READ).
- **The closing,** by your 122 (3), is the opening run backwards: an outgoing shell at position 2.

## Verdict

- **Under 162 the opening is consistent with causality and escapes the instability.** The energy arrives at once as a
  thin shell; the information is taken, not carried.
- **B4d now turns on one junction.** Can eq. (17)'s static bulk inside the hold's cone meet the shell's spacetime
  outside it with non-negative energy on the null boundary between them?

## Named hypotheses

- **Yours:** 115 (c), 122 (3), 136 G, 160, 162; R0.
- **The board's:**
  - H-ENERGY-CARRIED-INFO-TAKEN (forced by C3 under 162);
  - H-TAKEN-NOT-CARRIED;
  - R-VAIDYA-HOLDS, now only as the energy's delivery;
  - the hypotheses of `o3_write.py`'s gas bound.
