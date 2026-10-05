# H-CMB-CORRIDOR, reading 1: the cosmic background as the corridor's frame (not verified, not seated; 2026-10-05)

**M's question** (rulings item 41, verbatim): *"Have we considered the universe's own background radiation as the
means by which the corridor is constructed? As it is likely that background only multi-spacetime/multiversal
constant?"*

It is carried as two of M's hypotheses, never as results:
- **H-CMB-CORRIDOR:** the cosmic background builds the corridor.
- **H-CMB-UNIVERSAL:** the background is a multi-spacetime constant.

M's order (item 42, "3, then 1") took the Q-1s gate first, then this reading. This reading is **the background's rest
frame as H-FRAME's preferred frame**, to which every corridor coupling is keyed. It does not cover whether the
background's photons or entropy could carry or build the corridor; that is another reading, not taken up here.

Every number is printed by `cmbframe.py` (`--selftest`: 20/20, 6 controls, 2 STRUCTURAL). The owners it asks at run
time are `frame.py`, `step1c/nonlocal.py`, `seat.py` and `cosmo.py`.

## What the board already held

- A corridor network keyed to one frame closes no causal curve at any rank (`frame.py`, A2-frame.md (i)1).
- In exact FRW, cosmic time is a global time function on the comoving quotient (z3 lemma).
- An instantaneous coupling is loop-free iff all couplings share one simultaneity frame (`nonlocal.py`).
- So **any** single frame satisfies H-FRAME's loop requirement. The CMB frame was named as the natural candidate, but
  only from a dipole READ-VIA-RESTATEMENT (D67) and under H-CMB-IS-COSMIC.

## What this reading adds

1. **The frame, READ at source.** Planck 2018 I (1807.06205v2, Table 2 p.6 and its footnote e):
   - the barycentre moves at **369.82 ± 0.11 km/s**, β = (1.23357 ± 0.00036)×10⁻³;
   - toward (l, b) = (264.021°, 48.253°), RA/Dec (167.942°, −6.944°).

   This upgrades `frame.py`'s restatement, and the two agree within Planck's error. The Hipparcos Galactic rotation
   used for the other directions reproduces Planck's printed RA/Dec to 0.0003°.
2. **Earth–Proxima under CMB keying.**
   - Proxima lies **66.19°** from the dipole apex.
   - A link simultaneous in the CMB frame reaches Proxima at barycentre coordinate time **−66,725 s (−18.5 h)**. That is
     the coordinate past of the barycentre's frame (clause 2a), and it closes no loop.
   - Earth's orbit modulates this by **±9,453 s (±2.6 h)** over a year.
   - Realising the frame from the dipole's own precision leaves **σ = 35 s** across the span.
3. **One frame spans Earth–Proxima.**
   - Comoving frames at the two ends differ by the Hubble flow: Δβ = 2.9×10⁻¹⁰, a 0.04 s tilt in the flat lattice
     model.
   - In FRW the keying is to cosmic time, which is exactly a time function, so the tilt is the flat model's artefact.
   - The keyed lattices asked of `frame.py` gave 0 of 100 failures at rank 2 and 0 of 100 at rank 3.
4. **H-LAB-FRAME becomes a computation.** `nonlocal.py`'s J bounds needed the preferred frame to move slower than
   c²t/r relative to the lab.
   - With the frame named as the CMB's, Earth's largest speed in it is 400.8 km/s (β = 1.34×10⁻³). Every test needs
     β < 0.80–0.98, so **H-LAB-FRAME holds for all six**.
   - The bounds weaken by at most 0.17 %. The tightest is 6.61×10³ rad/s (NIST, 5-pulse margin).
   - So under H-CMB-AS-FRAME, the present no-signalling tests bound a CMB-keyed instantaneous coupling exactly as
     `nonlocal.py` priced it. H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING and H-J-DISTANCE-FREE still stand.
5. **The speed of influence in the CMB frame.**
   - Only one paper prints a CMB-frame figure: Scarani, Tittel, Zbinden and Gisin 2000 (quant-ph/0007008v1, p.1 and
     p.5), v ≥ 1.5×10⁴ c. Their detections were simultaneous in the CMB frame near 3h UTC, with τ interpolated, an
     assumption they state.
   - Salart 2008's headline condition is β = 10⁻³. The CMB's 1.234×10⁻³ lies just outside it, and that paper prints no
     CMB figure.
   - These are lower bounds, so **v = ∞ in the CMB frame is not excluded** (as in `nonlocal.py`, and per Bancal).
6. **H-CMB-IS-COSMIC is contested by READ data.** The matter dipole exceeds its kinematic expectation:
   - 4.9σ: Secrest 2021, 2009.14826v2 p.5;
   - 5.1σ joint: Secrest 2022, 2206.05624v2 p.5;
   - "now exceeds 5σ", ~6.4σ combined: the 2025 colloquium, 2505.23526v2 pp.1, 14.

   So the CMB's rest frame and the frame matter defines may differ, and H-FRAME must say which frame it means.
   - At Proxima, keying to the quasar dipole read kinematically (H-QUASAR-KINEMATIC, 750 km/s) shifts the lead by
     0.74 h at the central values. **Over the READ errors the shift is 0.28–13.3 h.** The near-agreement at the
     central values is a geometric coincidence, not a constraint.
   - The Local Group's frame (Planck Table 3 p.7, 620 km/s) shifts the lead by 30 h.
7. **H-CMB-UNIVERSAL, its measurable part.**
   - T(z) = T₀(1+z)^(1−β) with β consistent with 0 in every fit READ: Avgoustidis 2016, 0.0076 ± 0.0080; Riechers
     2022, 0.0034 (+0.0081/−0.0073).
   - The standard 20.0 K at HFLS3 (z = 6.34) lies inside its measured 16.4–30.2 K.
   - **The background is not constant in time: it cools as 1/a.** What all comoving observers share is its rest frame
     and its blackbody form.
   - Its temperature is a cosmic clock, but with T₀ = 2.72548 ± 0.00057 K (Fixsen 2009) it resolves cosmic time only
     to **3.0 Myr**. It can name the frame, but it cannot synchronise the corridor's ends.
   - The "multi-spacetime / multiversal" clause has no measurement on the board: **OPEN, carried**.

## The answer to M, as the board holds it

**The background's rest frame is a lawful choice of H-FRAME's frame, and it is measurable.**
- It is loop-free, being one frame keyed to cosmic time.
- It is fixed to ±0.11 km/s, which leaves a 35 s realisation spread over 4.25 ly.
- Present no-signalling and speed-of-influence tests constrain a coupling keyed to it but do not exclude it.

Two limits are named:
- whether "the frame" is the CMB's or matter's is contested at more than 5σ (H-CMB-IS-COSMIC);
- the background cools, so it is constant in frame and form, not in temperature.

Nothing here shows the coupling exists. **O9 stays OPEN.** Naming the frame does not touch the two classical bits; it
fixes which slicing a channel would use if one exists.

## Named hypotheses

- **This reading's own:** H-CMB-AS-FRAME, H-CMB-IS-COSMIC (contested), H-BARYCENTRE, H-FIRST-ORDER, H-CIRCULAR-ORBIT,
  H-OBLIQUITY, H-ROTATION-BOUND, H-GAL-MATRIX, H-QUASAR-KINEMATIC.
- **Carried from the owners:** `frame.py`'s H-CORRIDOR-MODEL, H-FRW-EXACT and H-NOT-DE-SITTER; `nonlocal.py`'s
  H-CORRIDOR-MAP, H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING and H-J-DISTANCE-FREE.

## OPEN

1. Which frame H-FRAME means if the CMB and matter dipoles disagree (the matter-dipole anomaly is unresolved in the
   sources read).
2. H-CMB-UNIVERSAL's multi-spacetime clause.
3. The other readings of H-CMB-CORRIDOR: the background as the medium, as the register, as the coupling's carrier.
4. A CMB-frame bound from Salart 2008 or Yin 2013 at the CMB's own β. None is printed; a reader's evaluation, about
   4.6×10⁴ c, is not used.

## Sources (READ 2026-10-05; routes)

All arXiv reads went through alphaXiv; the Gaia row came from VizieR via Firecrawl. No 403 was met.

| source | pages |
|---|---|
| Planck 2018 I, 1807.06205v2 | Table 2 p.6 (fn. e), Table 3 p.7 |
| Planck 2018 III, 1807.06207v1 | eq. (10) p.25 |
| Fixsen 2009, 0911.1955v2 | abstract p.1; Table 2 p.5 |
| Avgoustidis 2016, 1511.04335v1 | Table II p.4; Table III p.6 |
| Riechers 2022, 2202.00693v1 | pp.1, 3, 5, 7 |
| Secrest 2021, 2009.14826v2 | pp.2, 5 |
| Secrest 2022, 2206.05624v2 | pp.5–6 |
| Secrest et al. 2025 colloquium, 2505.23526v2 | pp.1, 12, 14 |
| Scarani et al. 2000, quant-ph/0007008v1 | pp.1–6 |
| Salart 2008, 0808.3316v1 | pp.1–5 |
| Yin 2013, 1303.0614v2 | pp.6–7 |
| Bancal 2012, 1110.3795v2 | pp.1–2 |
| Gaia DR3, VizieR I/355/gaiadr3 | source 5853498713190525696 |
| Kervella 2017, 1611.03495v3 | Table 2 p.4 |

**NOT READ:** Planck 2018 II (LFI) directly; Luzzi; Gelo 2022; Wagenveld 2023; the Cocciaro 2018 paper.
