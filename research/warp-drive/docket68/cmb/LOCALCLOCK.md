# A clock at each position (H-LOCAL-CLOCK; not verified; not seated; 2026-10-05)

## M's words and how they are carried

M, rulings item 52, verbatim: *"time is always relative, so the clock of the observer doesn't matter in the second
position, as time may move differently in the second position compared to the first. The clock is always present
relative to the position of measurement within its plane/dimension The clock is relative to the matter-based
observation. Consciousness observation is a perception of matter-observed time."*

This is carried as M's hypothesis **H-LOCAL-CLOCK**, never as a result.

M's order (item 53) was *"READ, then model"*. The READ was done on 2026-10-05, and `localclock.py` is the model. Every
number below is printed by it. Its selftest runs **9/9 checks, 2 of them controls**, with 2 STRUCTURAL lines printed
and not counted. It asks `cmbframe.py` (and through it `seat.py`) for its inputs, and `unobserved.py` imports its
Proxima velocity vector.

## What the literature says (READ 2026-10-05)

### For M's reading

- **Time is a clock reading tied to a worldline** (Castro-Ruiz, Giacomini, Belenchia & Brukner 1908.10165v2 p.2).
- **Any clock can be the frame.** "each quantum clock constitutes a legitimate temporal (quantum) reference frame"
  (ibid. p.7).
- **What counts as "the same moment" depends on the clock.** "temporal locality is frame dependent" (Höhn, Smith & Lock
  1912.00033v3 p.31).
- **Clock rates differ with position, and this is measured** over 33 cm (Chou et al. 2010) and within a single
  millimetre (Bothwell et al. 2022).
- **Consciousness as perception of records.** In Page's sensible quantum mechanics (gr-qc/9507024v1 pp.1–4),
  probabilities belong only to conscious perceptions. Their content includes memories, which are present records. Page
  also writes: "we cannot know the past except through its records in the present" (gr-qc/9303020v2 p.2).

### Against the letter of "the clock of the observer doesn't matter"

- **Clock relations are lawful.** Changing clocks changes the description by a calculable amount, and the laws keep
  their form (1908.10165v2 p.7; 1912.00033v3 p.4). So the clock "matters" in that it fixes the description. It does not
  matter in that no clock is privileged.
- **The equivalence has a scope.** The three relational-time formalisms are shown equivalent only for a clock that does
  not interact with the system (1912.00033v3 p.3). The interacting case is open (p.37).
- **No relativistic clock-interference experiment exists yet.** The one clock-interference experiment simulated the
  time lag and was not sensitive to relativity (Margalit et al. 1505.05765v1 p.2).
- **Perceptions do not act back.** In Page's scheme they leave the quantum state alone (gr-qc/9507024v1 p.9). Back-action
  appears only in his speculative "Sensational" extension (p.12).

## The model, computed

### 1. The two local clocks

- **The law.** In the weak field, dτ/dt = 1 − Φ/c² − v²/(2c²), each clock taken in its own star's rest frame
  (H-WEAK-FIELD), on a circular orbit (H-CIRCULAR).
- **A, on Earth's orbit,** runs slow by **1.481×10⁻⁸** (Φ/c² = 9.871×10⁻⁹, v = 29.78 km/s). GM_Sun is the IAU 2015
  B3 nominal value (1510.07674v1 p.3).
- **B, on Proxima b's orbit,** runs slow by **3.723×10⁻⁸** (Φ/c² = 2.482×10⁻⁸, v = 47.23 km/s). The stellar mass and
  orbit are Faria 2022's, via `seat.py`.
- **So B runs slower than A by 2.242×10⁻⁸: 0.708 ± 0.021 seconds per year.** The error comes from Faria's stellar-mass
  uncertainty.
- **What is left out (H-ORBIT-ONLY).** Earth's own potential, 7.0×10⁻¹⁰, is 3 % of the difference. Its inputs are from
  memory and are printed for size only. Rotation and b's eccentricity are also left out.
- **Control:** swapping the two orbits flips the sign.

**M's "time may move differently in the second position" is true and computed**: about 0.7 seconds a year.

### 2. The same law, against measurement

| experiment | the law predicts | measured |
|---|---|---|
| Chou et al. 2010, 33 cm height (NIST open reprint, Fig. 3) | 3.60×10⁻¹⁷ | (4.1 ± 1.6)×10⁻¹⁷ |
| Bothwell et al., per millimetre (2109.12238v1 p.6) | −1.090×10⁻¹⁹ | (−9.8 ± 2.3)×10⁻²⁰ |

- **Both agree within one sigma.** The law that sets the corridor's 0.708 s/yr is the law measured on a lab bench.
- **Control:** a law ten times too large misses Chou et al. by more than 3 sigma.

### 3. The CMB frame's reckoning

- **The speeds.** In reading 1's frame (`cmbframe.py`), the Sun moves at 369.82 km/s and Proxima at 382.24 km/s. That
  uses Proxima's velocity relative to the Sun from Gaia: 32.38 km/s, against 32.4 in reading 2.
- **What that frame reckons.** It reckons Proxima's clock slower than the Sun's by **1.640 s per year** from motion
  alone.
- **This figure depends on the frame.** Another frame reckons another, as relativity requires. Only section 1's local
  comparison, with each clock in its own star's rest frame, is a statement about the two positions. Section 3 is a
  statement about one frame's bookkeeping.

### 4. What a local clock costs a delocalised quantum state

- **The phase.** A qubit with energy splitting ΔE, shared across A and B, picks up a relative phase ΔE·Δτ/ħ. This is
  Zych et al.'s proper-time phase (1105.4531v2 eqs. 13–16), applied to the corridor's span.
- **The phase can be corrected if it is known.** It is deterministic.
  - An optical (Sr, 429 THz) qubit gains 1.91×10¹⁵ rad a year.
  - A caesium-hyperfine (9.19 GHz) qubit gains 4.09×10¹⁰ rad a year.
- **An unknown phase is not correctable.** The READ uncertainty in Δτ spreads the phase by 5.71×10¹³ rad (optical) or
  1.22×10⁹ rad (caesium). A Gaussian spread σ leaves visibility exp(−σ²/2) (H-GAUSSIAN-PHASE), which is **below
  10⁻¹⁰⁰** for both.
- **At today's knowledge of Δτ, a qubit stays coherent across A and B for a year only if its splitting is below
  7.5 Hz** (H-DELOCALISED-QUBIT).
- **What this means for M's reading.** The local clocks are not just bookkeeping. A state spread across both positions
  carries their difference as a measurable phase.

### 5. Two clocks for one system

- **Covariance.** Relative to B's clock, which ticks at rate r against A's, the system evolves as exp(−iHτ_B/r). That is
  the same law rescaled (infidelity −8.9×10⁻¹⁶, zero to machine precision). This is M's "the clock of the observer
  doesn't matter", in its precise form.
- **A spread clock.** If B's clock is spread over readings τ ± Δ relative to A, the system relative to B is a
  superposition U(τ − Δ) + U(τ + Δ). It becomes "temporally nonlocal": purity 0.975, against 1.000 with no spread
  (H-CLOCK-SPREAD).

### 6. Consciousness as a perception of matter-observed time (STRUCTURAL)

- **Page's sensible QM matches M's last clause directly.** A conscious perception is a perception of a present matter
  record, including the record of a clock.
- **It does not give H-CONSCIOUS-SELECTS reading (b).** In Page's scheme perceptions do not act back on the state.
  Reading (b)'s "forces a specific and measurable behaviour" needs his speculative extension.
- **So M's items 50 and 52 pull in different directions here.** Item 52's "perception of matter-observed time" is
  passive. Item 50's "forces" is active. Both are carried. The model does not choose between them.

## For M

- **Each position has its own clock, set by the matter there.** It is computed: Proxima b's clock runs 0.708 ± 0.021 s
  a year slower than Earth's orbit. The law that gives that number is measured within a millimetre on Earth.
- **"The clock of the observer doesn't matter" holds in its precise form.** Changing clocks rescales the law and
  changes no physics. But the change is calculable and lawful, not arbitrary.
- **A frame-wide figure, such as the CMB frame's 1.640 s/yr, is bookkeeping.** The local comparison is the physical one.
- **The clocks' difference is real to a quantum state spread across both positions.** It shows as a phase that destroys
  coherence unless it is known. At today's knowledge, only a splitting below 7.5 Hz survives a year.
- **"Consciousness observation is a perception of matter-observed time" has a home** in Page's sensible QM. There,
  perception is passive, which sits beside item 50's "forces" rather than with it.

**Nothing here touches O9.** Local clocks change the phase and rate of what is sent. They do not open a channel.

## Named hypotheses

H-WEAK-FIELD, H-ORBIT-ONLY, H-CIRCULAR, H-DELOCALISED-QUBIT, H-GAUSSIAN-PHASE and H-CLOCK-SPREAD, with M's H-LOCAL-CLOCK.

## OPEN

1. Clocks that interact with the system they time. The relational-time equivalence is not shown there (1912.00033v3
   p.37).
2. Any experiment in which a clock's relativistic time lag is seen in interference (Zych et al.'s proposal; Margalit et
   al. simulated only).
3. Earth's own potential and rotation, and b's eccentricity, from READ values rather than memory (H-ORBIT-ONLY).
4. How item 52's passive perception and item 50's forcing are to be reconciled. This is M's to say.

## History (first-written claims kept)

- **The visibility of an unknown phase** was first printed as |cos(πfσ)|, giving 0.983 and 0.572. That is Zych's
  two-branch law applied to an uncertain phase, and it is meaningless at spreads of 10⁹–10¹³ rad. It was corrected to
  exp(−σ²/2) before any report (H-GAUSSIAN-PHASE). The check now requires visibility below 10⁻¹⁰⁰.
