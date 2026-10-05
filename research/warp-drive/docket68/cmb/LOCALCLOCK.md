# A clock at each position (H-LOCAL-CLOCK; verified once; not seated; 2026-10-05)

## M's words and how they are carried

M, rulings item 52, verbatim: *"time is always relative, so the clock of the observer doesn't matter in the second
position, as time may move differently in the second position compared to the first. The clock is always present
relative to the position of measurement within its plane/dimension The clock is relative to the matter-based
observation. Consciousness observation is a perception of matter-observed time."*

This is carried as M's hypothesis **H-LOCAL-CLOCK**, never as a result.

M's order (item 53) was *"READ, then model"*. The READ was done on 2026-10-05, and `localclock.py` is the model. Every
number below is printed by it.

- **The selftest runs 6/6 checks, 3 of them controls**, with 3 STRUCTURAL lines printed and not counted.
- **What each check is.** One is an external fixture (IAU L_C) and one is lab data (Chou, Bothwell). One is a regression
  pin. The three controls each fail a wrong law: potential-only, ten times too large, and null.
- **Inputs.** It asks `cmbframe.py` (and through it `seat.py`) for its inputs. `unobserved.py` imports its Proxima
  velocity vector.
- **History.** The first build had 9 checks. The verifier found four of them true by construction or circular. They are
  replaced (see History).

## What the literature says (READ 2026-10-05; "verifier-READ" marks text the verifier read at source)

### For M's reading

- **Time is a clock's reading.** "time is not absolute but rather is defined by the reading of a clock moving along a
  specific world-line" (Castro-Ruiz, Giacomini, Belenchia & Brukner 1908.10165v2 p.2). And "the time localisability of
  events becomes relative, depending on the reference frame" (p.1).
- **Any clock can be the frame.** "each quantum clock constitutes a legitimate temporal (quantum) reference frame"
  (ibid. p.7).
- **Position and time only relative to physical systems.** "localization in both space and time is only meaningful in
  relation to other physical systems, and not relative to absolute or external structures" (Höhn, Smith & Lock
  1912.00033v3 p.3, verifier-READ). Also: "temporal locality is frame dependent" (p.31).
- **Observation is local.** Page (gr-qc/9303020v2) writes, verifier-READ:
  - "we cannot know the past except through its records in the present" (p.2);
  - "we cannot directly compare things at different locations either, so that all observations are really localized in
    space as well as in time" (p.3). This is close to M's "relative to the position of measurement".
- **The matter clock introduces time.** Page (same paper, pp.4–5, verifier-READ) writes that coordinate time "is
  completely unobservable". What is observable is "the reading of a physical clock", and the dependence of probabilities
  on that reading "is then the observable time evolution". This answers item 52's "what introduces the clock?": a
  physical clock, made of matter.
- **No quantity without its measurement.** "in quantum mechanics it makes no sense to speak about quantities without
  specifying how they are measured" (Zych et al. 1105.4531v2 p.7, verifier-READ). This supports "the clock is relative to
  the matter-based observation".
- **Consciousness perceives matter's records.** In Page's sensible quantum mechanics (gr-qc/9507024v1 pp.1–4),
  probabilities belong only to conscious perceptions. Their content includes memories, which are present records. A
  perception is not itself tied to a time or place; its time is read from the matter fields (p.10, verifier-READ).
  This supports "a perception of matter-observed time".
- **Clock rates differ with position, and this is measured** over 33 cm (Chou et al. 2010) and within a single
  millimetre (Bothwell et al. 2022).

### Scope and limits

- **Covariance supports "the clock of the observer doesn't matter".** No clock is privileged: changing clocks keeps the
  laws in the same form (1908.10165v2 p.7; 1912.00033v3 p.4). What changing clocks does change is the description, by a
  calculable amount.
- **The equivalence has a scope.** The three relational-time formalisms are shown equivalent only for a clock that does
  not interact with the system (1912.00033v3 p.3). The interacting case is open (p.37).
- **No relativistic clock-interference experiment was found in the READ.** The one READ, Margalit et al.
  (1505.05765v1 p.2), simulated the time lag. Their clock "is not accurate enough to be sensitive to special- or
  general-relativistic effects".

## The model, computed

### 1. The two local clocks

- **The law.** In the weak field, dτ/dt = 1 − Φ/c² − v²/(2c²) (H-WEAK-FIELD).
- **The frame.** Each clock is timed against a distant observer at rest with its *own* star (H-OWN-STAR-FRAME).
- **The orbits.** For any Keplerian orbit, ⟨1/r⟩ = 1/a and ⟨v²⟩ = GM/a. So the mean offset is exactly 1.5GM/(ac²), and
  the circular-orbit assumption costs nothing for the mean rate (H-CIRCULAR). Eccentricity adds only a periodic term.
- **A, on Earth's orbit,** runs slow by **1.481×10⁻⁸** (Φ/c² = 9.871×10⁻⁹, v = 29.78 km/s). GM_Sun is the IAU 2015
  B3 nominal value (1510.07674v1 p.3).
- **Checked against the IAU's L_C.** L_C = 1.48082686741×10⁻⁸ is the IAU's mean rate of a geocentre clock against
  barycentric coordinate time, with every body included. It was READ from search excerpts of the IAU 2000 resolutions
  (iers.org) and USNO Circular 179.
  - The law matches L_C to 2.3×10⁻¹², which is about the other planets' share.
  - **Control:** the potential term alone misses by 4.9×10⁻⁹, so the motion term is needed.
- **B, on Proxima b's orbit,** runs slow by **3.723×10⁻⁸** (Φ/c² = 2.482×10⁻⁸, v = 47.23 km/s). The stellar mass and
  orbit are Faria 2022's, via `seat.py`.
- **B's orbital offset exceeds A's by 2.242×10⁻⁸: 0.708 ± 0.014 s per year.**
  - The error is from Faria's stellar-mass uncertainty alone.
  - Faria's a follows from that mass by Kepler III (H-KEPLER-A), so the offset scales as M^(2/3).
- **Other terms are about the size of that error bar** (H-ORBIT-ONLY). They are printed and left out:

  | term | seconds per year |
  |---|---|
  | Earth's own potential and rotation (IAU L_G, READ) | 0.022 |
  | Proxima b's own surface (minimum mass 1.07 M⊕; radii 0.94–1.40 R⊕ from Brugger 2016, computed at 1.10–1.46 M⊕: H-B-SURFACE) | 0.017–0.025 |

- **Comparing the two clocks needs a frame or a signal exchange.** The size of the comparison depends on that choice. In
  the Sun's frame, Proxima's own motion at 32.38 km/s adds **0.184 s/yr**.

**Computed under H-WEAK-FIELD, H-OWN-STAR-FRAME and H-ORBIT-ONLY, M's "time may move differently in the second
position" holds: by about 0.7 seconds a year.**

### 2. The same law, against measurement

| experiment | the law predicts | measured | null law excluded at |
|---|---|---|---|
| Chou et al. 2010, 33 cm height (NIST open reprint, Fig. 3) | 3.60×10⁻¹⁷ | (4.1 ± 1.6)×10⁻¹⁷ | 2.6σ |
| Bothwell et al., per millimetre (2109.12238v1 p.6; prediction p.5) | −1.090×10⁻¹⁹ | (−9.8 ± 2.3)×10⁻²⁰ | 4.3σ |

- **Both agree within one sigma.** This tests the gradient term, gh/c², to roughly 20–40 %.
- **Chou et al. also measured time dilation from motion,** "from relative speeds of less than 10 meters per second"
  (abstract, verifier-READ). That bears on the v² term.
- **The corridor extrapolates.** It uses absolute potentials near 10⁻⁸ and the v²/2c² term, which is a third of each
  offset. That extrapolation stays under H-WEAK-FIELD. Bothwell p.2 cites redshift tests out to thousands of kilometres;
  those are candidates to READ.
- **Controls:** a law ten times too large misses Chou et al. by more than 3σ, and a null law misses Bothwell et al. by
  more than 3σ.

### 3. The CMB frame relating them (M's item 53)

- **The speeds.** In reading 1's frame (`cmbframe.py`), the Sun moves at 369.82 km/s and Proxima at 382.24 km/s. The
  latter uses Proxima's velocity relative to the Sun from Gaia, 32.38 km/s.
- **What that frame reckons.** It reckons Proxima's clock slower than the Sun's by **1.640 s per year** from motion
  alone.
- **The radial velocity matters at the 1 % level.** Gaia's radial velocity is not corrected for convective blueshift or
  gravitational redshift (H-GAIA-RV). With Kervella 2017's corrected value, the figure is **1.628 s/yr**.
- **Every comparison is a frame choice.** Section 1's own-star frames, the Sun's frame and the CMB frame each give a
  different figure. The CMB frame is the one M's item 53 names. No frame is privileged by the physics. Each is a
  lawful, calculable description.

### 4. What a local clock does to a quantum state spread across both positions

- **The phase.** A qubit with energy splitting ΔE, shared across A and B, picks up a relative phase ΔE·Δτ/ħ. The source
  is Zych et al. 1105.4531v2: eq. 12 is the phase, and eqs. 13–16 are their visibility law. Their setup excludes
  special-relativistic dilation (p.5). Moving it to the corridor's orbits is H-DELOCALISED-QUBIT.
- **The phase is large and fixed.**
  - An optical (Sr, 429 THz) qubit gains 1.91×10¹⁵ rad a year.
  - A caesium-hyperfine (9.19 GHz) qubit gains 4.09×10¹⁰ rad a year.
  - Δτ is a fixed number, so every run gets the same phase. Not knowing it shifts the fringe; it does not wash it out.
    A phase scan calibrates it.
- **Uncalibrated, the phase is a known unknown.** The stellar-mass error spreads it by 3.81×10¹³ rad (optical) or
  8.15×10⁸ rad (caesium). Averaged over that prior, the visibility is exp(−σ²/2) (H-GAUSSIAN-PHASE): log₁₀V = −3.1×10²⁶
  and −1.4×10¹⁷.
- **This loss is epistemic.** Castro-Ruiz et al. (1908.10165v2 p.2) note that clock-induced decoherence "is (quantum)
  reference frame dependent".
- **Without calibration, the spread stays under 1 rad (V = 0.61) only below 11.3 Hz,** and V stays above ½ only below
  13.3 Hz.

**So the two positions' clocks are not just bookkeeping.** A state spread across both carries their difference as a phase
that must be calibrated.

### 5. Two clocks for one system

- **Covariance (STRUCTURAL).** Relative to another clock, the system follows the same law, rescaled (1908.10165v2 p.7
  eqs. 10–11, "universal covariant form"). This is "the clock of the observer doesn't matter" in its precise form.
- **A spread clock (STRUCTURAL).** If B's clock is spread over readings τ ± Δ relative to A, the reduced state of S
  relative to B is an equal mixture of two branches (Höhn–Smith–Lock p.31, under their stated assumptions).
  - Its purity is (1 + |⟨a|b⟩|²)/2 by construction, which is 0.975 at illustrative inputs Δ = 0.6, τ = 5, w = 1,
    g = 0.4, |0⟩ (H-CLOCK-SPREAD).
  - The number shows the form, not a size.

### 6. Consciousness as a perception of matter-observed time (STRUCTURAL)

- **Page's sensible QM houses item 52's last clause.** A conscious perception is a perception of present matter records,
  including a clock's.
- **SQM leaves back-action out; it does not rule it out.** SQM "does not describe any action of the perceptions back on
  the state" (p.9). On the same page, Page argues that survival "does at least suggest that perceptions do have an action
  back on the quantum state". On p.12 he sketches how that could work.
- **So item 52 and H-CONSCIOUS-SELECTS (item 50) fit together.** Item 52 says what consciousness perceives (time, as
  recorded by matter). Item 50 says what conscious observation does (forces an outcome). That would sit where Page's
  suggested back-action sits.

## For M

- **Each position has its own clock, set by the matter there.** Proxima b's orbital clock runs 0.708 ± 0.014 s a year
  slower than Earth's orbital clock, each against its own star. The law that gives that number reproduces the IAU's L_C
  for Earth, and its gradient term is measured within a millimetre.
- **Comparing the two clocks needs a frame.** Each frame gives a lawful, calculable figure:
  - the CMB frame you named reckons 1.640 s/yr (1.628 with the corrected radial velocity);
  - the Sun's frame adds 0.184 s/yr to the own-star comparison.
- **"The clock of the observer doesn't matter" holds in its precise form.** Covariance makes no clock privileged.
  Changing clocks rescales the law and changes no physics.
- **The literature READ supports your reading more than the first draft said.**
  - Position and time are only meaningful relative to physical systems.
  - All observation is localised in space and time.
  - The observable time is a physical clock's reading.
- **The clocks' difference is real to a quantum state spread across both positions.** It is a fixed, calibratable phase
  of about 10¹⁵ rad a year for an optical qubit.
- **"Consciousness observation is a perception of matter-observed time" has a home** in Page's sensible QM. Page himself
  suggests perceptions act back, which is where item 50 would sit.

**Nothing here touches O9.** Local clocks change the phase and rate of what is sent. They do not open a channel.

## Named hypotheses

H-WEAK-FIELD, H-OWN-STAR-FRAME, H-CIRCULAR, H-KEPLER-A, H-ORBIT-ONLY, H-B-SURFACE, H-GAIA-RV, H-DELOCALISED-QUBIT,
H-GAUSSIAN-PHASE and H-CLOCK-SPREAD, with M's H-LOCAL-CLOCK.

## OPEN

1. Clocks that interact with the system they time. The relational-time equivalence is not shown there (1912.00033v3
   p.37).
2. Any experiment in which a clock's relativistic time lag is seen in interference (Zych et al.'s proposal).
3. Proxima b's radius at its own mass, and its true mass (inclination unknown): H-B-SURFACE.
4. The redshift tests out to thousands of kilometres (Galileo satellites, cited by Bothwell p.2): NAMED-NOT-READ.
5. How Page's suggested back-action (p.12) relates to H-CONSCIOUS-SELECTS reading (b).

## History (first-written claims kept)

### Before any report

- **The visibility of an unknown phase** was first printed as |cos(πfσ)|, giving 0.983 and 0.572. That is Zych's
  two-branch law applied to an uncertain phase. It was corrected to exp(−σ²/2).

### Verifier, 2026-10-05: what the first write-up said, and what replaced it

- **The error bar.** It said *"0.708 ± 0.021 seconds per year"*. That held a fixed and independent of M, but a follows
  from M by Kepler III, so the error is ± 0.014. The terms left out (0.022, 0.017–0.025 and a 0.184 frame term) were not
  all named.
- **The frames.** It said section 1's comparison is *"the physical one"* and the CMB frame's figure *"bookkeeping"*.
  Each is a frame choice, and M's item 53 names the CMB frame.
- **The coherence limit.** It said *"only a splitting below 7.5 Hz survives a year"*. That applied an unstated 1-rad
  criterion to ignorance of a fixed, calibratable phase. With the corrected error, the 1-rad figure is 11.3 Hz.
- **Earth's own potential** was computed from values labelled memory. It is now READ as the IAU's L_G.
- **The checks.** Four of the nine were not tests. They were replaced by the IAU L_C fixture, its potential-only control,
  and a null-law control on Bothwell.
  - The covariance check was true by construction: it set τ_B = rτ and evaluated U(τ_B/r), and its rate had the wrong
    sign.
  - The spread-clock check was near-vacuous.
  - The orbit-swap control was equivalent to the pin.
  - The 32.4 km/s check was circular: reading 2's 32.4 is this file's own vector.
- **The literature.**
  - The covariance argument was filed "against" M's reading. It supports it.
  - Page's, Höhn–Smith–Lock's and Zych's support for M's reading was not carried.
  - "No relativistic clock-interference experiment exists yet" was unsourced; it now reads "none found in the READ".
- **Page and back-action.** The first write-up said Page's perceptions *"do not act back"* and called back-action
  *"speculative"*. It concluded that items 50 and 52 *"pull in different directions"*. That misread Page: he omits
  back-action, argues that it is likely, and sketches it. The conflict between M's items was the write-up's invention.
- **Smaller fixes.**
  - The spread-clock state was called a "superposition"; it is the reduced, mixed state of S.
  - The "law measured on a lab bench" overstated what was tested: only the gradient term, to 20–40 %.
  - Gaia's radial velocity is uncorrected; Kervella's is printed beside it.
  - The visibility printed as 0.0 by underflow; it now prints log₁₀V.
  - Zych's phase is eq. 12, not eqs. 13–16.
