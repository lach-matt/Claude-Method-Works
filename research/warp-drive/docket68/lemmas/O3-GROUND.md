# O3 under item 164: what oscillates in a ground state (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `o3_ground.py`, selftest 7/7.

## What you said

- **Item 164:** *"The ground state of any atom is an oscillating state. Thus its energy oscillates as well"*. That
  answers the board's line *"Achievability conflicts with your rulings. Margolus–Levitin's achieving state needs an
  energy spread, a level at 2E, and it oscillates back."*
- **Item 133:** *"There is only one exact energy needed for any given README"*.
- **Item 162:** *"The throat doesn't change size"*.
- **Item 163:** *"All together, one whole"*.

## The source, re-read in full

Margolus & Levitin, quant-ph/9710043 (READ 2026-10-08):
- §2.1 sets the zero of energy at the ground state: *"we will choose our zero of energy so that E₀ = 0"*.
- **Eq. (4)**, τ ≥ h/(4E), with E the average energy above the ground state. **Eq. (5)** is the earlier
  Mandelstam–Tamm bound, τ ≥ h/(4ΔE). Both are on p.4.
- **Eqs. (6)–(7):** each energy component only turns its phase, and the survival amplitude is
  S(t) = Σ|cₙ|²e^{−iEₙt/ħ}.
- **Eqs. (10)–(11):** the achieving state, for which *"ΔE = E"*.
- **p.9:** *"an isolated stationary atom in an exact energy eigenstate never transitions to an orthogonal state"*.

## What follows

**G1. In a ground state, two things do oscillate** (computed).
- **The test cases.** Hydrogen's 1s and the oscillator's ground state solve Hψ = E₀ψ exactly.
- **The phase rotates.** Evolved, each becomes e^{−iE₀t/ħ}ψ, so the phase turns at the rate E₀/h.
- **Position keeps a spread** that never goes away: Δr = (√3/2)a₀ for 1s, Δx = 1/√2 for the oscillator.
- **So in that sense your statement holds:** a ground state is an oscillating state.

**G2. Its energy does not oscillate** (computed).
- **No spread.** In the same states the energy's spread is exactly zero, and ⟨r⟩, ⟨r²⟩ and ⟨H⟩ do not change with time.
- **Never orthogonal.** |S(t)| = 1 at every t, so the state never turns orthogonal. That is ML's p.9.
- **The rotation's rate is not even fixed.** Move the zero of energy by c, as ML themselves do, and the phase turns at a
  different rate. Nothing observable changes: |S|, every expectation value and the density matrix are all the same. So
  the phase is real but has no fixed rate, and it never shows up in the energy.

**G3. No isolated state's energy oscillates** (computed).
- **ML's own state.** Evolve their achieving state (eq. (10)) by eq. (6): ⟨H⟩ is E at every moment, and nothing
  depending on time is left in it.
- **What does oscillate** is S, between 1 and 0. This is Ehrenfest's d⟨H⟩/dt = 0 for a fixed H (standard, not READ).

**G4. What the write needs under your 163** (computed, from ML eqs. (4)–(5)).
- **The time.** The write lasts at least 2.0×10⁵ clocks (`o3_write.py`, which 163 keeps).
- **The spread that time needs.** Eq. (5) needs ΔE ≥ h/(4T). With h/(4E) = (2π²/ln2)/N clocks, that gives

  **ΔE / E ≥ 5.2×10⁻²⁰ at the example README.**

- **Reachable exactly.** The state (|E − d⟩ + |E + d⟩)/√2 with d = h/(4T) has an average of exactly E and turns
  orthogonal at exactly T (computed).
- **What that does to the size.** Its two branches differ in radius by **1.3×10⁻¹² Planck lengths**.
- **Inside the physics used.** The write lasts 1.3×10⁻³¹ s, about 2.5×10¹² Planck times. The instant hold, 6.9×10⁻⁵¹ s,
  was below one Planck time.

## Verdict

- **On your 164:**
  - A ground state oscillates in its phase and in the spread of its position. That is what "oscillating state" can mean.
  - Its energy does not oscillate (G2), and no isolated state's energy does (G3).
  - ML's p.9 stands.
- **But the conflict the board reported belonged to the instant reading.** An orthogonal step within h/(4E) needs
  ΔE = E: a spread as large as the energy itself.
- **Under 163 that conflict is withdrawn.** The write lasts at least 2.0×10⁵ clocks and needs a spread of only
  5.2×10⁻²⁰ of E (G4). So your 133's one exact energy holds to 5.2×10⁻²⁰, and your 162's fixed size holds to
  1.3×10⁻¹² Planck lengths. What withdraws it is the whole write needing almost no spread. Reading the energy as
  oscillating is not needed.
- **How the board reads your "oscillating state" for the corridor:** a near-eigenstate whose energy is exact to
  5.2×10⁻²⁰ and whose phase turns. This is the board's reading, H-NEAR-EIGENSTATE.
- **No status moves.** O3 stays OPEN as B4d's: the open question is the bulk through the write (`B4D-STAGE5.md`), not
  the write's energy.

## Named hypotheses

- **Yours:** 133, 162, 163, 164 (H-GROUND-OSCILLATES).
- **The board's:**
  - H-NEAR-EIGENSTATE;
  - the hypotheses of `o3_write.py`'s gas bound;
  - E taken as the average above the register's ground (as in `o3_atonce.py`);
  - ML's non-relativistic, fixed-background setting, now inside its domain.
