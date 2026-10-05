# H-CMB-CORRIDOR, reading 1: the cosmic background as the corridor's frame (verified once and corrected; not seated; 2026-10-05)

## M's question and how it is carried

M asked, verbatim (rulings item 41): *"Have we considered the universe's own background radiation as the means by
which the corridor is constructed? As it is likely that background only multi-spacetime/multiversal constant?"*

The question is carried as two of M's hypotheses, never as results:
- **H-CMB-CORRIDOR**: the background builds the corridor.
- **H-CMB-UNIVERSAL**: the background is a multi-spacetime constant.

M ordered the work in item 42 ("3, then 1"): the Q-1s gate first, then this reading. After the first build M added:
*"The physics as it applies to the frame is what matters."*

**This reading covers one thing only.** It takes the background's rest frame as H-FRAME's preferred frame, to which
every corridor coupling is keyed. It does not take up whether the background's photons or entropy could carry or build
the corridor. That is another reading.

**Where the numbers come from.** Every number is printed by `cmbframe.py`. Its selftest passes 21/21, 5 of them
controls, with 4 STRUCTURAL lines printed and not counted. It asks its owners at run time: `frame.py`,
`step1c/nonlocal.py`, `seat.py` and `cosmo.py`. One verifier checked it in both directions. Its findings are applied,
and the first-written claims are kept in the file's HISTORY and in the History section below.

## The physics of the frame

1. **The background is a gas of light, and a gas has one rest frame.** The CMB is a thermal photon gas that has
   streamed freely since last scattering.
   - Exactly one frame has zero net momentum density, and only in that frame is the gas isotropic.
   - That frame is a property of the universe's *state*, not of its laws. Lorentz invariance is untouched.
2. **Each observer measures its velocity against the gas locally, with no signal exchanged.**
   - An observer moving at β sees T(θ) = T₀/[γ(1 − β cos θ)]: 2.72884 K ahead, 2.72548 K across, 2.72212 K behind.
   - The dipole amplitude over T₀ *is* β. With Planck's 3362.08 μK and Fixsen's 2.72548 K, that is 1.233574×10⁻³.
     It matches Planck's printed β (1.23357 ± 0.00036)×10⁻³, a cross-check between two READ papers.
3. **Equal temperature means equal cosmic time.** In FRW the gas cools as 1/a, so the surfaces of equal CMB
   temperature are the surfaces of equal cosmic time. The background therefore defines a simultaneity as well as a
   direction, and keying to it is keying to cosmic time. By `frame.py`'s z3 lemma that is a global time function:
   no closed causal curve exists, at any rank.

## Results

1. **The frame, READ at source.** Planck 2018 I (1807.06205v2) gives it in Table 2 p.6 and its footnote e:
   - barycentre speed 369.82 ± 0.11 km/s;
   - direction (l, b) = (264.021°, 48.253°), which is RA/Dec (167.942°, −6.944°).

   This upgrades `frame.py`'s figure from READ-VIA-RESTATEMENT (D67) to READ. The Hipparcos Galactic rotation
   reproduces Planck's printed RA/Dec to 0.0003°. The control, the untransposed matrix, misses by 96°.
2. **Earth–Proxima under CMB keying.** Proxima lies **66.19°** from the dipole apex.
   - **The lead.** A link simultaneous in the CMB frame reaches Proxima at barycentre coordinate time
     **−66,725 s (−18.5 h)**. This is clause 2a: the coordinate past, spacelike, no loop. In barycentre time the lead
     is fixed; Earth's offset from the barycentre adds at most 0.6 s.
   - **In Earth's momentary rest frame** the lead moves by **±9,453 s (±2.6 h) over a year**, from the orbit, and by up
     to ±95 s over a day at the equator.
   - **The dipole-precision term alone is σ ≈ 27 s.** The speed contributes 19.8 s. The direction error in the
     apex–Proxima plane contributes 17.7 s. Planck's errors are linear sums of statistical and systematic parts, here
     treated as 1σ (H-LINEAR-ERRORS).
   - **Other terms of the same size sit beside it** (H-EPOCH):
     - Proxima's proper motion from 2016 to 2026 moves the lead by −26 s;
     - the light-time position correction by −11 s;
     - the radial velocity by +11.5 s per decade;
     - the parallax error by 4 s.
3. **One frame spans Earth–Proxima.**
   - Comoving frames at the two ends differ by the Hubble flow, Δβ = 2.9×10⁻¹⁰. In the flat model that is a 0.04 s
     tilt.
   - In FRW the keying is to cosmic time, so the tilt is the flat model's artefact.
   - That a network keyed to one frame closes no loop is a theorem, true of *any* single frame. It is shown, not
     sampled, and it is not evidence for the CMB's frame in particular.
4. **H-LAB-FRAME is now a computation, not an assumption.**
   - Earth's speed relative to the CMB frame is at most 400.8 km/s (β 1.34×10⁻³). The D67 range is 340.65–399.08 km/s.
   - All six of `nonlocal.py`'s spacelike tests need β < 0.80–0.98, so **H-LAB-FRAME holds for all six**.
   - Their J bounds then apply to a CMB-keyed instantaneous coupling **to within 0.17 %**. The tightest is
     6.61×10³ rad/s (NIST, 5-pulse margin).
   - This holds given H-CMB-AS-FRAME, H-BARYCENTRE, H-INSTANTANEOUS-IN-FRAME and H-J-PER-FRAME-TIME, together with
     `nonlocal.py`'s H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING and H-J-DISTANCE-FREE.
5. **Speed-of-influence bounds in the CMB frame.**
   - Only one paper prints a figure for the CMB frame: Scarani, Tittel, Zbinden and Gisin 2000 (quant-ph/0007008v1,
     p.1 and p.5), v ≥ 1.5×10⁴ c. Its detections were simultaneous in the CMB frame near 3h UTC, with τ interpolated;
     the paper states that as an assumption.
   - Earth's β relative to the CMB frame, 1.13–1.34×10⁻³, lies just outside Salart 2008's headline condition
     (β = 10⁻³).
   - These are lower bounds. **v = ∞ in the CMB frame is not excluded.**
6. **H-CMB-IS-COSMIC and the matter dipole: two readings, both carried.** Matter's isotropy in the CMB frame is
   rejected:
   - at 4.9σ (Secrest 2021, 2009.14826v2 p.5);
   - at 5.1σ jointly (Secrest 2022, 2206.05624v2 p.5);
   - at "now exceeds 5σ", ~6.4σ combined, in the 2025 colloquium (2505.23526v2 pp.1, 14).

   The two readings:
   - **(a) Intrinsic matter anisotropy.** This is the source's own preferred reading (Secrest 2022: consistency
     improves on boosting to the CMB frame, "suggesting … intrinsic anisotropy in this frame"; abstract p.1, p.6, p.7).
     **The CMB frame stays the kinematic frame. This supports M.**
   - **(b) Kinematic.** The frames differ (H-QUASAR-KINEMATIC: the whole excess kinematic, its axis the velocity
     axis). At Proxima:
     - the quasar frame shifts the lead by 0.74 h at the central values, and by **0 to 13.3 h** over a ±1σ box in
       (D, l, b), whose corners sit at √3σ. The central near-agreement is a geometric coincidence, not a constraint;
     - keying to the Local Group puts Proxima at **+29.9 h**, in the barycentre's coordinate *future*. That is a
       **48.4 h** shift. The relative velocity, 298.6 km/s toward (98.4°, −5.8°), reproduces Planck Table 3's Sun–LG
       row;
     - keying to the Galactic centre gives +21.5 h, a 40.0 h shift.

   Under (b), H-FRAME must say which frame it means.
7. **H-CMB-UNIVERSAL: what can be measured.**
   - T(z) = T₀(1+z)^(1−β), with β consistent with 0 in every fit READ:
     - Avgoustidis 2016: 0.0076 ± 0.0080;
     - Riechers 2022: 0.0034 (+0.0081/−0.0073).
   - The standard 20.0 K at HFLS3 (z = 6.34) lies inside the measured 16.4–30.2 K.
   - **The background is not constant in time: it cools as 1/a.** What all comoving observers share is its rest frame
     and its blackbody form.
   - **Its temperature cannot synchronise the corridor's ends.**
     - One second of cosmic time moves T by 2.2×10⁻¹⁸ of itself. T₀ is known to 2.1×10⁻⁴, which is 14 orders short.
     - Resolving the 18.5 h lead by temperature would take δT/T ~ 1.5×10⁻¹³.
     - The absolute calibration, 3.0 Myr, is shared by both ends, so it is not the limiting figure.
   - **The dipole plus light signals can synchronise the ends**, to the dipole term (~27 s) plus the epoch terms.
   - The "multi-spacetime / multiversal" clause has no measurement on the board: **OPEN, carried**.

## What the CMB frame does that an arbitrary frame cannot (for M)

- **Local, independent realisation.** Each end of a corridor can find the frame by itself, with a thermometer and a
  telescope, exchanging no signal. No other candidate frame offers this, and a corridor's two ends need it.
- **It does work the geometry cannot.** In the de Sitter limit the geometry stops selecting a frame. There, "the cosmic
  frame is selected by the matter content (the CMB)" (A2-frame.md (i)).
- **It turns a prediction into an experiment.** Under H-FRAME + H-SETTLE, Bob's statistics would follow *cosmic*-time
  ordering (A2-frame.md). Naming the CMB gives that a concrete signature: β = 1.2336×10⁻³, a known apex, and annual
  and diurnal modulation. Scarani-style Bell runs, simultaneous in the CMB frame, are that experiment.
- **Paired with H-SETTLE it names the slicing the channel needs.** On its own, clause 1 does not touch the two classical
  bits (A2-frame.md). But under H-SETTLE × H-FRAME, O-BITS is REMOVED-IF {W2, F1} (CLOSE.md §1). The CMB frame names
  the slicing that route would use.

## The answer to M, as the board holds it

**The background's rest frame is a lawful, physical and measurable choice of H-FRAME's frame.**
- Every observer reads it locally.
- It is keyed to cosmic time, so it closes no loop.
- It is realised across Earth–Proxima to about half a minute.
- Present no-signalling tests and speed-of-influence bounds constrain a coupling keyed to it, but do not exclude it.

Two limits are named:
- Matter's dipole disagrees with the CMB's at more than 5σ. The source reads that as intrinsic anisotropy, which
  leaves the CMB frame standing, but the kinematic reading would make the two frames differ.
- The background is constant in frame and form, not in temperature.

**O9 stays OPEN.** Nothing here shows a coupling exists. The frame decides which slicing a channel would use, if one
exists.

## Named hypotheses

- **This reading's own:** H-CMB-AS-FRAME, H-CMB-IS-COSMIC, H-BARYCENTRE, H-AT-REST-ENDPOINT, H-EPOCH, H-CIRCULAR-ORBIT,
  H-OBLIQUITY, H-ROTATION, H-GAL-MATRIX, H-LINEAR-ERRORS, H-QUASAR-KINEMATIC, H-INSTANTANEOUS-IN-FRAME and
  H-J-PER-FRAME-TIME.
- **From the owners:** `frame.py`'s H-CORRIDOR-MODEL, H-FRW-EXACT and H-NOT-DE-SITTER; `nonlocal.py`'s H-CORRIDOR-MAP,
  H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING and H-J-DISTANCE-FREE.

## OPEN

1. Which frame H-FRAME means under reading (b) of the matter dipole.
2. H-CMB-UNIVERSAL's multi-spacetime clause.
3. The other readings of H-CMB-CORRIDOR: the background as the medium, as the register, or as the coupling's carrier.
4. A CMB-frame figure from Salart 2008 or Yin 2013 at the CMB's own β. None is printed. A reader's own evaluation,
   about 4.6×10⁴ c, is not used.

## History (verifier, 2026-10-05; first-written claims kept)

- **The Local Group lead.**
  - First said: "the Local Group's frame … shifts the lead by 30 h".
  - What was wrong: the velocity was wrong. The correct one is v_Sun−CMB − v_LG−CMB.
  - Corrected: +29.9 h, a 48.4 h shift.
- **The annual modulation.**
  - First said: "Earth's orbit modulates this by ±9,453 s", of the barycentre-time lead.
  - What was wrong: the frame. That modulation belongs to Earth's momentary rest frame.
- **The quasar shift.**
  - First said: "0.28–13.3 h".
  - What was wrong: a grid artefact. The range is 0–13.3 h.
- **The realisation error.**
  - First said: "σ = 35 s".
  - What was wrong: the T₀ term does not apply to the velocity, and the direction error was not projected onto the
    apex–Proxima plane.
  - Corrected: about 27 s, and it is the dipole term only.
- **Synchronisation.**
  - First said: "It can name the frame, but it cannot synchronise the corridor's ends".
  - What was wrong: this mixed up the temperature clock with the frame.
- **The matter dipole.**
  - First said: "H-CMB-IS-COSMIC is contested by READ data".
  - What was wrong: it was overstated. Both readings are now carried.

The keyed-lattice sample was first presented as evidence. It is a theorem for any frame.

## Sources (READ 2026-10-05; routes)

All arXiv reads went through alphaXiv; the Gaia row came from VizieR via Firecrawl. No 403 was met.

| source | pages |
|---|---|
| Planck 2018 I, 1807.06205v2 | Table 2 p.6 (fn. e); Table 3 p.7. Re-read by the verifier |
| Planck 2018 III, 1807.06207v1 | eq. (10) p.25 |
| Fixsen 2009, 0911.1955v2 | abstract p.1; Table 2 p.5 |
| Avgoustidis 2016, 1511.04335v1 | Table II p.4; Table III p.6 |
| Riechers 2022, 2202.00693v1 | pp.1, 3, 5, 7 |
| Secrest 2021, 2009.14826v2 | pp.2, 5 |
| Secrest 2022, 2206.05624v2 | pp.1, 5–7 |
| Secrest et al. 2025 colloquium, 2505.23526v2 | pp.1, 12, 14 |
| Scarani et al. 2000, quant-ph/0007008v1 | pp.1–6 |
| Salart 2008, 0808.3316v1 | pp.1–5 |
| Yin 2013, 1303.0614v2 | pp.6–7 |
| Bancal 2012, 1110.3795v2 | pp.1–2 |
| Gaia DR3, VizieR I/355/gaiadr3 | source 5853498713190525696 |
| Kervella 2017, 1611.03495v3 | Table 2 p.4 |

**NOT READ:** Planck 2018 II (LFI) directly; Luzzi; Gelo 2022; Wagenveld 2023; the Cocciaro 2018 paper.
