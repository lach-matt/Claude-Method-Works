# Item 159: both readings of where the write sits, tested (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `o3_readings.py`, selftest 7/7.

The first draft called both readings refuted. Its verifier showed three things:
- **Reading (i), as first tested, contradicts your own rulings.** Its coherent form had not been tested.
- **Reading (ii)'s refutation rested on a step the draft never named.**
- **The "nearby wall" escape does not work** once the mass rises from zero.

All of this is corrected below (History).

## What you said

- **Item 159:** *"test both options"*. The two options are:
  - **(i)** the write happens in a hold after the corridor stands;
  - **(ii)** the write is the opening itself, the README flowing in.
- **Also bearing on the test:**
  - item 158 (2), *"Exactly as long as the write needs  I should think"*;
  - item 115 (c), *"The README itself"*;
  - item 127 (1), *"yes"* (the planes coincide *"while the corridor exists"*);
  - item 138 (the bulk is multi-universal).

## Reading (i): a hold after the corridor stands (R1)

- **As first tested, it contradicts your rulings.** The first test took the write to be the README arriving at the
  throat. But under your 115 (c), with H-PULL-IS-COST, the corridor's mass *is* the README's energy. So a corridor
  already standing means the README has already arrived.
- **Its coherent form is (i′), a write after arrival.** That is an internal encoding of what has already come in.
- **(i′) has no gas bound.** The gas bound limits arrival, not internal encoding, so it doesn't apply.
- **(i′) keeps O3's static window.** O3's static window, from max(h/4E, 1/(2ξ)) up to about 11.3 clocks, applies to it
  as before.
- **(i′) is not refuted.** Within that window it stands where O3 stood before item 158.
- **What it does not avoid.** The arrival itself, the opening, still lasts at least 2.0×10⁵ clocks (630 under the most
  generous assumption). That is true on either reading, so what the bulk does during the opening is B4d's on (i′) too.

## The black string's instability, computed (R2)

**The equation.**
- GL's eq. (10) (hep-th/9301052, p.7) is transcribed at D = 4. One sign, as extracted from the PDF, contradicts GL's
  own stated horizon exponents.
- Restored, the equation is **identical, term by term, to Emparan–Suzuki–Tanabe's eqs. (7.3)–(7.6)** (1302.6382, p.31,
  READ) at n = 1. That is a second printed source fixing every term. The extracted form is not identical.

**How it is solved.**
- Shooting from the horizon's regular branch, steered round the point where the equation's leading coefficient
  vanishes. The leftover imaginary part is tiny, so that point is only an apparent singularity.

**Results:**
- Unstable for 0 < μ·r₊ < 0.876.
- The fastest mode is Ω·r₊ = 0.0923 at μ·r₊ ≈ 0.35.

**Controls:**
- Lehner–Pretorius's critical *L/R* ≈ 7.2 is μ·r₊ = 0.873. Ours is 0.876.
- Gregory's GM = 1 range and favoured mode are consistent with ours.
- Camps–Emparan–Haddad's small-k form, eq. (1.5) (READ), agrees with ours within 3–6% for k·r₊ = 0.02–0.1. Their
  next-order term does not match ours cleanly at n = 1. CEH themselves note that n = 1 falls off more slowly (p.7).
- A second integration setting agrees.

## Reading (ii): the write as the opening (R3) — refuted in the board's quasi-static model

**The steps it rests on, now named:**
- **H-QUASI-STATIC-STRING** (the board's). Near the plane, and within its causal reach, the Vaidya opening's bulk is
  the black string of mass m(v). This lies outside B4b's static scope; whether it holds is B4d's to decide.
- **H-MASS-RISES.** A horizon is present through the write, so the README does not arrive as one late shell.

**The growth.**
- Ω(x)/x falls monotonically (computed). So one fixed mode (μ = 0.35/r₊ final) grows at least 0.046 per clock for any
  mass history.
- That is **at least 9.2×10³ e-folds over 2.0×10⁵ clocks**, whatever the shape of the ramp.
- At the 630-clock floor it is 29 e-folds. That needs a seed above e⁻²⁹ (H-SEED). Quantum noise is about e⁻¹⁶, so it
  qualifies.

**The endpoint.**
- Lehner–Pretorius's extrapolated endpoint (READ, *"the simulation results imply"*) follows about 107 clocks after the
  nonlinear stage. Classically it is a naked curvature singularity; in practice, Planck curvature.

## The escapes (R4; deduced)

**Still open:**
- **(d)** The opening's bulk is not the black string, i.e. H-QUASI-STATIC-STRING fails. That is B4d's to decide.
- **(e)** The README arrives as a late shell, so H-MASS-RISES fails.
- **(f)** The short write (630 clocks) with seeds below e⁻²⁹.
- **(i′)** above.
- **(a)** An extremal opening. This rests on the board's own mapping of Gregory's extremal exception onto eq. (17)'s
  degenerate horizon. It collapses into (i)'s static problem only under the same step as H-QUASI-STATIC-STRING.

**Closed:**
- **(b) A nearby wall.**
  - Gregory's eq. (11) reduces to sin(m·z_c) = 0 in the flat limit (deduced). So a wall closer than 3.59 r₊ does stop
    the *final* string.
  - But the mass rises from zero, so every allowed mode crosses the whole unstable band on the way. It grows by
    (T/2)·∫Ω/x dx = (T/2)·0.216 (computed). That is **2.2×10⁴ e-folds, or 68 at 630 clocks, whatever the spacing.**
  - A wall within 7.2 m also leaves no room for B4c's far surface.
  - Your 127's coinciding planes act as one wall (multiplane.py M4), with the bulk semi-infinite beyond it. That is
    Gregory's single-wall case, which is unstable. 127's scope is also only "while the corridor exists".
- **Charge and rotation.** A non-extremal charge does not help (Gregory p.2), and neither does rotation
  (Lehner–Pretorius p.4).
- **Leaving the flat limit, for (ii).** The Randall–Sundrum string is itself singular at the AdS horizon (Gregory p.4).

## Verdict

- **(i) as first tested contradicts your rulings.** Its coherent form (i′), a write after arrival, stands in O3's
  static window. It is untested beyond that window.
- **(ii) is refuted in the board's quasi-static model.** That holds under H-QUASI-STATIC-STRING, H-MASS-RISES and
  either H-README-ALONE or H-SEED.
- **On both readings,** the opening lasts at least 2.0×10⁵ clocks, and its bulk is B4d's to settle.

## Named hypotheses

- **Yours:** 115 (c), 127, 138, 158 (2), 159.
- **The board's:**
  - H-WRITE-IS-ARRIVAL (the first test of (i), and (ii));
  - H-QUASI-STATIC-STRING;
  - H-MASS-RISES;
  - H-SEED (at 630 clocks);
  - H-README-ALONE;
  - H-PULL-IS-COST;
  - R-VAIDYA-HOLDS;
  - the flat limit;
  - the board's mapping in escape (a).

## History (verifier, 2026-10-08)

**What the verifier confirmed.** It ran the selftest (7/7), READ the sources, and confirmed R2 independently:
- the same equation from EST, compared in sympy;
- its own solver, integrating inward along the opposite detour, which agreed to better than 10⁻⁴;
- the published small-k behaviour.

**Its findings, all applied:**

**MUST-FIX**
1. **(ii) rested on an unnamed step outside B4b.** It is now named H-QUASI-STATIC-STRING, and (d) is added as an
   escape.
2. **Escape (b) was over-claimed, and its source mislabelled.** `e^{kz_c} ≥ 2kGM` is Gregory's large-mass estimate,
   not eq. (11). The flat-limit wall condition is now deduced from eq. (11). Every mode crosses the band from m = 0:
   2.2×10⁴ e-folds, computed. (b) is now closed, and 127 is restated with multiplane.py M4 and its scope.
3. **(i) as tested was inconsistent with 115 (c) and H-PULL-IS-COST.** It is restated, and the coherent (i′) is named
   and left open.

**SHOULD-FIX**
4. **The 630-clock case.** Its seed requirement is now stated (H-SEED).
5. **The e-fold count used the fastest mode at each moment.** It now follows one fixed mode, which holds for any ramp
   shape (9.2×10³ e-folds). H-MASS-RISES is named and the late-shell escape added.
6. **Lehner–Pretorius's endpoint was stated too firmly.** It is now labelled an extrapolation, Planck-scale in
   practice.
7. **The EST identity** is added as a READ control, and CEH's small-k form is now compared.
8. **Escape (a)** is now labelled the board's mapping.
9. **Whether the instability mode fits the plane's boundary conditions was never stated.** It does: at the plane, in
   the flat limit, the data is a Neumann condition, and the mode cos(μy) satisfies it with no plane bending (Gregory
   p.4, footnote 1). Deduced.
10. **The escapes list is completed:** (d), (e), (f) and (i′) open; charge and rotation closed by READ.

**NOTE**
11. **R1's numbers** are imported from O3-WRITE.
12. **Selftest.** Arithmetic pins are now marked STRUCTURAL, the Gregory comparison is now "consistent with", and an
    imaginary-residue check is added.
13. **Vaidya from m = 0.** Its central naked point and the early non-adiabatic stretch belong to opening.py and the
    ramp. They are noted here, not computed.
14. **Units** were confirmed. The 632/630 slip is fixed in o3_write.py.
