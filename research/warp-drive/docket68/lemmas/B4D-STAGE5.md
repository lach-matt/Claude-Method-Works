# B4d stage 5: the corridor of fixed size through the write (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage5.py`, selftest 11/11, about 5 minutes.

The first draft found no way open on the board's models. Its verifier found one: on the negative-tension side (your
139), the bulk has no singular surface. That changes the verdict. The refutation now holds on one side only, and the
other side is the live route for your 161. All findings are applied (History).

## What you said

- **Item 163:** *"All together, one whole"*. The README is carried in and held as one whole, and the gas bound stands.
- **Item 162:** *"The throat doesn't change size"*.
- **Item 161:** *"my inclination is yes"*: the corridor stays regular while the README passes.
- **Item 160:** *"the corridor and the opening are the same object"*.
- **Items 115 (c) and 136 G:** the inflow is the README, and the README is the energy.
- **Item 139:** position 2's plane has negative tension.
- **Clause (B):** the plane carries no matter.
- **Items 117/120:** *"the NEC only ever appears to break, but never does"*.

## What follows

**F1. Where the inflow's energy goes is a reading** (arithmetic; the readings are the board's).
- **What is fixed.** The trapping radius is r = 2m(v), so your fixed size means dm/dv = 0.
- **What flows in.** By 115 (c) and 136 G the README's energy flows in, over at least 1.997×10⁵ clocks.
- **Three readings reconcile the two, and none is forced:**
  1. **An equal outflow to position 2** (H-THROUGH-FLOW). This sits against your 163's "held as a single whole" and
     against clause (E)'s release at the closing.
  2. **The mass is set at the opening** (H-MASS-AT-OPENING).
  3. **The energy is carried into the bulk.** Your 158 (4) left this to the math.
- **The verdict needs none of them.** The inflow averages at most 5.0×10⁻⁶ of m per clock. So some 20-clock window
  carries no more than that, which is all F4 uses.

**F2. On the positive-tension side, the static bulk still has a singular surface at every ℓ tested, nearer the plane as
ℓ falls** (computed; numerical evidence, not a bound).
- **How it was computed.** `b4_static.py`'s exact series at r = 2.15m, order 32. The warp is divided out first. That
  helps a little at ℓ = 2m and m/2, not at m. Spurious Padé pole–zero pairs are divided out before anything is
  evaluated.
- **The results** (y in units of m):

  | ℓ | nearest singularity | K at 0.9 y_s | × the black string's | hold to reach it |
  |---|---|---|---|---|
  | ∞ (control) | 2.58 (2.50 at order 80) | 330 | 660 | 20.2 clocks |
  | 2m | 1.41–1.43, **a pair just off the axis** (±0.05i) | 1.0×10⁴ | 1,100 | 16.0 |
  | m | 1.00–1.02 | 2.7×10⁴ | 470 | 13.0 |
  | m/2 | 0.67–0.69 | 4.8×10⁵ | 670 | 10.9 |
  | m/4 | 0.43 | 1.6×10⁶ | 150 | 7.8 |

  The singularity ranges come from orders 32 to 48 (the verifier's figures). K at 0.9 y_s and the hold agree across
  three Padé orders, within 10% and 1%. At 0.95 y_s, K is larger but depends on the order.
- **What the evidence says, and what it does not.**
  - **The coefficients.** They keep one sign from order 24 to 32, which is *consistent with* Pringsheim's theorem. The
    theorem itself needs all but finitely many. At ℓ = 2m they turn negative from order 36, as a pair just off the
    axis requires.
  - **Curvature, not a coordinate breakdown.** This is not the flat limit's kind of singularity: near it the metric
    function B falls toward zero, which a mere breakdown of the coordinates would also do. K decides. It rises as
    (y_s − y)^−4 to hundreds or thousands of times the black string's, which a coordinate effect does not do.
- **Controls.**
  - ℓ = ∞ reproduces `b4_static.py`'s surface, 3% high at this order.
  - Schwarzschild data give the black string. The series terminates, so there is no singular surface, and K matches the
    black string's to 2×10⁻¹⁶.
- **Why it moves inward** (a heuristic). This is KSCALE's closure seen in the bulk: eq. (17)'s deficit is a Weyl datum
  the bulk cannot carry far when ℓ is small. At the values tested r₀/ℓ ≤ 8, so this is a heuristic, not a derivation.

**F3. The hold that reaches it** (computed).
- **What is measured.** Light down the r = 2.15m column, in far time. One path gives an upper bound on the earliest hold
  whose cone contains the point.
- **The result.** Within 8–16 clocks at every finite ℓ tested, the cone contains curvature of 10⁴ or more, 100 to 1,100
  times the black string's. The write takes 2.0×10⁵ clocks.
- **Checked another way.** The verifier's partial sums of the series, at orders 32–40, give the same times without Padé.
- **Control.** At ℓ = ∞ the column reaches K = 100 at 19.2 clocks. That is no earlier than `b4_static.py`'s 14.9, its
  minimum over all paths, as an upper bound must be.

**F4. Over that hold the plane's data are eq. (17)'s** (a reading, H-QUASI-STATIC-CORRIDOR, the board's).
- **How much changes.** In the window F1 picks, the inflow moves at most about 10⁻⁴ of the mass.
- **What that gives.** Read inside the locally analytic class, the bulk in that window's cone is the static bulk.
- **Why it is a reading.** The bulk problem is Hadamard-ill-posed, so this continuity is the hypothesis, not a theorem.
- **No escape through the opening.** Only the first such window matters. The opening's own transient does not escape:
  any later window of eq. (17) data fixes its own cone.

**F5. A second plane below the surface would carry NEC-breaking matter at finite ℓ too** (computed; STRUCTURAL at small
height).
- **What it must carry.** ρ + p_r = R⁽⁴⁾_kk·(y_w + 3y_w²/ℓ) + O(y_w³), with R⁽⁴⁾_kk = −2m(r − 2m)/(r²(2r − 3m)²) < 0. The
  warp cancels identically, and any tension drops out, your 139's negative one included. Checked rationally, and derived
  analytically by the verifier.
- **Where it is negative.** Computed at r = 2.15, 3, 5, 10 and 32m for y_w = y_s/4 and y_s/2. The verifier found it
  negative for every y_w up to 0.99 y_s at r = 2.25–32m.
- **So such a plane would carry real matter breaking the NEC,** which your 117/120 rule out.

**F6. On the negative-tension side there is no singular surface, on the evidence** (computed; the symmetry is exact).
- **The symmetry.** The bulk equations do not change under y → −y with e → −e; the series alternate, exactly. So with
  eq. (17) on a plane of **negative** tension, which is your 139's position-2 plane, the bulk on its side has the
  positive side's singularities behind the plane, at negative y.
- **Computed at ℓ = 2m, m and m/2:**
  - K equals the black string's to 4% at y = 0.5–3m, and to 0.1% from y = m at ℓ = m and m/2, in three Padé orders;
  - the lapse stays positive and grows;
  - eq. (17)'s extra curvature dies away, and the bulk settles into plain anti-de Sitter.
- **Its costs, named.**
  - **Data at the edge of the bulk.** Light reaches the bulk's conformal boundary in a finite far time: 15.7, 7.6 and
    3.8 clocks. So the bulk needs data there (H-BOUNDARY-DATA).
  - **Gravity is not held to the plane.** On a lone negative-tension plane, gravity is not localized (standard
    Randall–Sundrum, not READ). That runs against the board's four-dimensional readings, unless a positive-tension plane
    also bounds the bulk: your 127's coinciding planes, your 162's one object.

## Verdict

- **The refutation narrows to one side.**
  - **With eq. (17) on a positive-tension plane,** the corridor of 161–163 does not stay regular through the write. Its
    bulk reaches curvature of 10⁴ or more within 8–16 clocks at every finite ℓ tested (2m down to m/4). The write takes
    2.0×10⁵ clocks.
  - **That rests on a conjunction:**
    - eq. (17) on the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD);
    - one mirrored plane of positive Randall–Sundrum tension with no matter (clause (B), H-RS2-ONE-PLANE);
    - a vacuum bulk;
    - B4b's locally analytic class;
    - Padé as evidence;
    - H-QUASI-STATIC-CORRIDOR;
    - the far-time frame (H-HOLD-FRAME);
    - the column r = 2.15m and the ℓ values tested;
    - any write longer than about 16 clocks. The gas bound enters only through that.
  - **F5 closes one way round it,** a closing plane, under your 117/120.
- **With eq. (17) on your 139's negative-tension plane, the bulk is regular on the evidence (F6).** This is the live
  route for your 161. Its open questions are the data at the bulk's edge, and how gravity stays four-dimensional, by a
  positive-tension plane bounding the bulk (127, 162).
- **Also still open:**
  - H-TWO-SIDED;
  - a curved wall;
  - a through-flowing plane whose geometry is not eq. (17);
  - a bulk outside the analytic class;
  - README energy carried into the bulk (158 (4));
  - ℓ between and below the values tested.
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## History (verifier, 2026-10-08)

**What the verifier confirmed independently.**
- With its own 5D Ricci code, the series solves the bulk equations exactly through y⁹.
- The Kretschmann formula and the black string's K, derived from scratch.
- The closing-plane formula, derived analytically, with the Israel sign calibrated on the Randall–Sundrum plane.
- The light times, from series partial sums without Padé.
- The double-cone bound's logic, the warp division, and every quote of yours.
- Selftest 9/9 at the time.

**Its findings, all applied:**

**MUST-FIX**
1. **The Padé pole–zero cancellation was inverted.** It squared each spurious pair instead of removing it. Fixed. The
   times moved by at most 0.03 clocks; K at 0.95 y_s moved a lot, which is why the measure is now 0.9 y_s.
2. **At ℓ = 2m the nearest singularity is a pair just off the axis,** and the coefficients' sign fails from order 36.
   Pringsheim is now "consistent" only, and the pair is reported.
3. **The negative-tension side was missing,** and it is regular. Now F6, the verdict's live route.
4. **Numbers contradicted the output.**
   - "10⁵ at every ℓ" is replaced by the order-stable figures at 0.9 y_s.
   - "≥ 4×10⁵" and "~10⁸" are withdrawn.
   - "10⁴ times" is corrected.
5. **F1 over-claimed, and H-THROUGH-FLOW conflicts with your 163 and clause (E).** F1 is now a reading with three
   options, and the verdict no longer uses it: the pigeonhole on the average flux suffices.

**SHOULD-FIX**
6. **The singularity's precision was overstated.** Cross-order ranges are now given.
7. **"The same cut" as the flat limit was not supported.** B falls toward zero here; K decides, and favours curvature.
8. **"The step that made the difference"** is now "a modest improvement".
9. **F5's coverage** now names the sampled points, plus the verifier's wider scan.
10. **The conjunction lacked members.** Added: vacuum bulk, positive tension, the far-time frame, the column, the ℓ
    values, and the write needing only to exceed about 16 clocks.
11. **"What stays open" lacked items.** Added: ℓ between the values, README energy in the bulk. Also why the opening's
    transient is not an escape.
12. **F4 is a reading,** not a deduction.
13. **The KSCALE explanation is a heuristic** at r₀/ℓ ≤ 8, with Figueras–Wiseman p.4.

**NOTE**
14. **R⁽⁴⁾_kk** now carries its factor of m.
15. **F1's check** is labelled arithmetic.
16. **The Schwarzschild control** checks K and the warp division, not the Padé path.
17. **The spread at m/2** is within 3%.
18. **The selftest time** is now stated correctly.
19. **The ℓ = ∞ control** agrees with order 48: 2.497.
20. **The flux bound** holds on average; steadiness belonged to H-THROUGH-FLOW.

**Added after the verifier (computed):** ℓ = m/4. Its singularity is at 0.43m and the hold reaching it is 7.8 clocks.
At ℓ = m/8, in a scratch run not seated in the instrument, it is 0.26m.

## Named hypotheses

- **Yours:** 115 (c), 117/120, 127, 136 G, 139, 158 (4), 160, 161 (an inclination), 162, 163; clause (B).
- **The board's:**
  - H-EQ17-ON-PLANE-THROUGH-HOLD;
  - H-RS2-ONE-PLANE (positive tension);
  - H-QUASI-STATIC-CORRIDOR;
  - H-HOLD-FRAME;
  - B4b's locally analytic class;
  - H-BOUNDARY-DATA (F6);
  - the F1 readings H-THROUGH-FLOW and H-MASS-AT-OPENING, which the verdict does not use.
