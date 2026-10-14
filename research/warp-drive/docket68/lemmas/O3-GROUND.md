# O3 under item 164: what oscillates in a ground state (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `o3_ground.py`, selftest 9/9. Its first draft concluded
"the conflict is withdrawn" while one of the board's three objections, "it oscillates back", was still unanswered. The
verifier showed that was not earned. It is answered now (G5), and every finding is applied (History).

## What you said

- **Item 164:** *"The ground state of any atom is an oscillating state. Thus its energy oscillates as well"*. That
  answers the board's line *"Achievability conflicts with your rulings. Margolus–Levitin's achieving state needs an
  energy spread, a level at 2E, and it oscillates back."*
- **Item 133:** *"There is only one exact energy needed for any given README"*.
- **Item 162:** *"The throat doesn't change size"*.
- **Item 163:** *"All together, one whole"*. That is the option "held as a single whole, not bit by bit".
- **Item 115 (c):** *"The README itself"*: the inflow.

## The source, re-read in full

Margolus & Levitin, quant-ph/9710043 (READ 2026-10-08):
- **The zero of energy.** §2's opening paragraph, footnote 2 and §2.1: *"we will choose our zero of energy so that
  E₀ = 0"*.
- **The two bounds, p.4.** Eq. (4), τ ≥ h/(4E), with E the average energy above the ground state. Eq. (5), the earlier
  Mandelstam–Tamm bound τ ≥ h/(4ΔE).
- **How a state evolves.** Eq. (6): each energy component only turns its phase. Eq. (7): the survival amplitude
  S(t) = Σ|cₙ|²e^{−iEₙt/ħ}.
- **The achieving state.** Eqs. (10)–(11), with *"For these states, ∆E = E"*.
- **p.9** (page by the paper's order; the scan marks no page there): *"an isolated stationary atom in an exact energy
  eigenstate never transitions to an orthogonal state, but if we view this same atom from a moving frame we will see a
  sequence of distinct position states"*.

## What follows

**G1. In a ground state, three things oscillate or fluctuate** (computed).
- **The test cases.** Hydrogen's 1s and the oscillator's ground state solve Hψ = E₀ψ exactly.
- **The phase turns.** Each evolves to e^{−iE₀t/ħ}ψ.
- **Position keeps a spread:** Δr = (√3/2)a₀ for 1s, Δx = 1/√2 for the oscillator.
- **So do both halves of the energy.** The kinetic energy T and the potential energy V each fluctuate, and they move
  exactly against each other:

  | ground state | Var T | Var V | Cov(T, V) |
  |---|---|---|---|
  | oscillator | 1/8 | 1/8 | −1/8 |
  | hydrogen 1s | 1 hartree² (ΔT = 2\|E₀\|) | 1 hartree² | −1 |

- **This is the strongest reading of your words, and on it they hold literally:** the ground state's kinetic and
  potential energies fluctuate.
- **The same holds generally.** Every ground state does this (Heisenberg; standard, not READ). The QED vacuum's field
  energy fluctuates in any subregion too, while the full ground state is still an exact energy state (standard, not
  READ).

**G2. Its total energy does not** (computed; the time-independence is deduced).
- **No spread in the total.** Var(T + V) = Var H = 0 exactly, and for 1s this is computed two independent ways.
- **Never orthogonal.** |S(t)| = 1, so the state never turns orthogonal: ML's p.9.
- **The fluctuations are fixed in time.** The spreads of T, V and r come from |ψ|², which the turning phase leaves
  unchanged. So they *fluctuate*; they do not *oscillate*.
- **The phase's rate depends on the setting.**
  - Without gravity it moves with the zero of energy, and nothing observable moves with it.
  - With gravity the zero is fixed, because energy gravitates (ML's §3 uses the total relativistic energy). Then the
    corridor's phase turns at E/h = **2.4×10¹³ cycles per clock** (de Broglie/Compton; standard, not READ).
    Margolus–Levitin's h/(4E) is exactly a quarter of that period.
  - Either way it is only a phase. By itself it never produces a different state.

**G3. No isolated state's energy oscillates** (computed for ML's state; in general, Ehrenfest, standard, not READ).
- **ML's own state.** Evolved by eq. (6), its average energy is E at every moment.
- **What does oscillate** is S, between 1 and 0.

**G4. What the write needs under your 163** (computed, from ML eqs. (4)–(5)).
- **What 163 chose.** The write is one whole: one orthogonal step (H-WRITE-ONE-ORTHOGONAL-STEP). It is a step of the
  corridor together with its inflow (H-WRITE-CLOSED-SYSTEM). By 115 (c) the corridor alone is not isolated while the
  README flows in.
- **The time.** At least 1.997×10⁵ clocks (`o3_write.py`).
- **The spread that needs.** Eq. (5) asks for ΔE ≥ h/(4T). Eq. (4) asks for E ≥ h/(4T), which E exceeds about 2×10¹⁹
  times. So

  **ΔE / E ≥ 5.2×10⁻²⁰ at the example README.**

- **Reachable exactly.** The state (|E − d⟩ + |E + d⟩)/√2 has an average of exactly E and turns orthogonal at exactly
  h/(4d). Control: with d = E it is ML's own state.
- **What that does to the size.** If the size follows the energy (H-SIZE-TRACKS-ENERGY), the radius spreads by
  **1.3×10⁻¹² Planck lengths**. (The first draft called this the "split"; the two branches actually differ by twice
  that.)
- **If the write were bit by bit,** which 163 declined: N steps would need ΔE/E ≥ 1.4×10⁻⁴, a radius spread of 3.5×10³
  Planck lengths. So the tiny figure depends on the collective reading.
- **The setting.**
  - The write's duration, 1.3×10⁻³¹ s (2.5×10¹² Planck times), is above the Planck time.
  - The size figure is far below a Planck length.
  - ML's non-relativistic, fixed-background setting is still assumed for a horizon-sized object.

**G5. The held README does not oscillate back** (computed; deduced from your 133).
- **The register is degenerate.** By 133 and the board's E(N), the energy depends on N alone, never on what the README
  says. So all 2^N READMEs of N bits share the one energy E. The board names this H-DEGENERATE-REGISTER. It is also
  exactly what an entropy of N bits at one energy counts.
- **The write is a coupling.** The inflow couples the state before, |a⟩, to the README, |b⟩, at that one energy. It is
  on for T and then off (V = v(|a⟩⟨b| + |b⟩⟨a|), v = h/(4T)). Computed exactly:
  - the average energy is **exactly E at every moment**;
  - the spread is h/(4T) while the coupling is on, which reaches eq. (5), and **zero before and after**;
  - at T the state is the README, and once the coupling ends **it stays the README for good**;
  - **no level at 2E is used.** The levels are E ± v;
  - **control:** if the coupling were left on, the state would be back at |a⟩ at 2T. Swinging back belongs to the
    coupling, not to the held register.

## Verdict

- **On your 164:**
  - A ground state oscillates in its phase, and it fluctuates in its position and in its kinetic and potential energy
    (G1). On that reading your words hold.
  - Its total energy neither oscillates nor fluctuates (G2), and no isolated state's does (G3).
  - ML's p.9 stands.
- **The board's three objections were all the instant reading's,** and under 163 each is answered:

  | objection | answer under 163 |
  |---|---|
  | an energy spread | 5.2×10⁻²⁰ of E, only while the inflow's coupling is on; none in the held README |
  | a level at 2E | none; the levels are E ± h/(4T) |
  | it oscillates back | not once the coupling ends; the held README stays (G5) |

  These answers rest on H-WRITE-ONE-ORTHOGONAL-STEP, H-WRITE-CLOSED-SYSTEM and H-DEGENERATE-REGISTER.
- **Your 133 holds exactly in the held state,** and as the exact average throughout the write.
- **One reading of 133 cannot stand with your rulings:** that the energy has no spread at any moment. By eq. (5) a state
  with no spread never changes, so the README could never be written, against your 115 (c) and 163. The rulings
  themselves decide against that reading, so no question is put to you.
- **How the board reads your "oscillating state":** G1 and G5 together. The held corridor's phase turns and its parts
  fluctuate, and its energy is exact. This is the board's reading, H-HELD-EIGENSTATE.
- **No status moves.** O3 stays OPEN as B4d's.

## History (verifier, 2026-10-08)

**What the verifier confirmed.** The selftest (then 7/7). It recomputed every G4 number independently with mpmath, and
the figures matched. It checked every quote against the PDF; eq. (5) is Mandelstam–Tamm, the paper's ref. [10]. It
confirmed that the (|E − d⟩ + |E + d⟩)/√2 state reaches eq. (5).

**Its findings, all applied:**

**MUST-FIX**
1. **"The conflict is withdrawn" was not earned.** G4 answered the spread and the 2E level, but not oscillating back,
   and the eigenstate reading of 133 was left standing. G5 now answers oscillating back, from 133's degeneracy. The
   no-spread reading of 133 is shown to contradict 115 (c) and 163.
2. **The radius figure was off by a factor of 2.** 1.3×10⁻¹² Planck lengths is the radius's spread. The two branches
   differ by 2.6×10⁻¹².
3. **Put to you or decided?** The verifier proposed two questions. Both are now decided by the rulings:
   - whether 133 admits a spread: the average is exact, the held state is exact, and a zero spread at every moment
     would forbid the write;
   - what holds the README after T: the degenerate register, once the coupling ends.

**SHOULD-FIX**
4. **Eq. (4) was stated backwards.** It asks for E ≥ h/(4T), which E exceeds about 2×10¹⁹ times.
5. **Your strongest readings were missing.** Added: T and V fluctuate (computed); the Compton phase at a fixed zero;
   the QED vacuum; the rest of ML's p.9 sentence.
6. **The corridor is not isolated during the write.** H-WRITE-CLOSED-SYSTEM and H-WRITE-ONE-ORTHOGONAL-STEP are now
   named.
7. **Bit-by-bit sensitivity** is now given: 1.4×10⁻⁴.
8. **"Inside its domain" over-claimed.** Only the duration is above the Planck scale.
9. **Labels.** The time-independence is deduced, the general claims are standard, and G3 is computed only for ML's
   state.

**NOTE**
10. **Identity checks** (|S| = 1, the cancelling phase, T/T) are no longer tested as findings. G2 now computes Var H two
    independent ways.
11. **The write's time** is 1.997×10⁵ clocks, not a rounded-up 2.0×10⁵.
12. **Footnote 2** sits at §2's opening.

## Named hypotheses

- **Yours:** 115 (c), 133, 162, 163, 164 (H-GROUND-OSCILLATES).
- **The board's:**
  - H-WRITE-ONE-ORTHOGONAL-STEP (from 163's option);
  - H-WRITE-CLOSED-SYSTEM;
  - H-DEGENERATE-REGISTER (deduced from 133 and E(N));
  - H-SIZE-TRACKS-ENERGY;
  - H-HELD-EIGENSTATE;
  - E taken as the average above the register's ground (as in `o3_atonce.py`);
  - ML's non-relativistic, fixed-background setting;
  - the hypotheses of `o3_write.py`'s gas bound.
