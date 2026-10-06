# The coin test (M-RULINGS items 117–118, 120; deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS items 117–118; deduced and computed; not verified; not seated; 2026-10-06)".

## What M said

- **Item 117:** *"An NEC is never violated, between two entangled positions the NEC is like a coin, each position sits on
  a separate side. That action is that the coin flips. The NEC appears broken, but is not"* (H-NEC-COIN).
- **Item 118:** *"Yes, run it"*. The test is the null energy condition averaged along a whole path through the one-way
  corridor, from position 1's side to position 2's.
- **Item 120:** *"it was an methaphor to describe that the NEC only ever appears to break, but never does"*, and on the
  bulk *"yes. Science has already taught us that matter is neither created nor destroyed, it only changes geometric
  state."* (section below).

Every number is printed by `coin.py`.
- **Selftest:** 9/9 checks, 3 genuine controls, with 5 STRUCTURAL lines printed and not counted.
  *First written* "6/6 checks, 1 genuine control and 1 contrast". That control could not fail when check 1 passed, and
  the contrast restated a definition (History).
- **Imported:** `opening.py` (the corridor's radial combination, computed from eq. 17, and its Einstein pipeline) and
  `escape.py` (R = 0, and its seated text).

## What the test finds

**In our plane's reading the condition fails along the whole passage, not only point by point: averaging does not
remove the appearance. In the bulk near the plane it is kept.** That is your "appears broken, but is not", shown on
both faces (item 82).
*First written:* "In our plane's reading the test goes against the coin. In the bulk it agrees with the coin." That
bent your hypothesis. You said the NEC *appears* broken, and the plane's reading is that appearance. What the test
refutes is the board's own first-written expectation (OPENING): *"If it holds, the pointwise violation is an appearance
along the whole passage too."*

- **1. G_kk has one sign through the horizon.**
  - For a radial light-like path, **G_kk = −2E²(2r₀ − 3m)/(r(2r − 3m)²)** (sympy). This is the null-contracted Einstein
    tensor; under H-PLANE-READING it is 8π times the plane's effective T_kk.
  - It is finite at the horizon, where it is E²(3m − 2r₀)/m³ (−0.6 E² for m = 1, r₀ = 1.8).
  - It is negative at every radius for **every member with 2r₀ > 3m**, not only the horizon members: −1.32 just outside
    the throat, −0.60 at the horizon, −0.044 at r = 3 (m = 1, r₀ = 1.8).
  - **The sign change I offered as a candidate coin flip was an artifact.** The static-frame combination (−0.0148
    outside, +0.0519 inside) changes sign only because of the frame's factor 1/(1 − 2m/r).
    - `opening.py`'s O3 already said so when the candidate was offered: *"inside it (where the inequality reverses)"*.
    - The candidate is withdrawn (OPENING.md).
  - The same artifact made O3 say the condition holds at the horizon itself. It fails there too (OPENING.md, corrected).
- **2. The ANEC integral along the whole passage is negative, in closed form.**
  - Each leg, from infinity to the throat or from the throat to infinity, gives
    **∫G_kk dλ = −(4E/3m)·[1 − ((c² − 1)/c)·artanh(1/c)], with c = √(2r₀/3m)**.
    - The closed form was derived by the verifier. coin.py checks it against the quadrature at six members, two of
      them two-way; they agree to every printed digit.
  - For m = 1, r₀ = 1.8 (units E/m, G = c = 1):
    | | ∫G_kk dλ | ∫T_kk dλ (÷8π) |
    |---|---|---|
    | per leg | −0.957356 | −0.0380920 |
    | whole passage | **−1.914712** | −0.0761840 |
  - *First written:* "−0.957356 E … (geometric units)", calling it "the energy along the path" and "the average".
    Those values are the integral of G_kk, in units of E/m.
  - **The bounds, for every member: −4E/(3m) < leg < 0.** The bracket lies between 0 and 1 because
    0 < artanh x < x/(1 − x²) on (0, 1), term by term. coin.py also checks it on a sweep from r₀ = 1.5001 to 1000.
    - The two-way members r₀ > 2m are included (r₀ = 3: −0.502366). m = 0 gives exactly −4E/(3r₀).
    - **So the horizon plays no part in the sign.** This test cannot tell the one-way corridor from a two-way member of
      the same family.
    - The most negative value is at the Schwarzschild edge: as r₀ approaches 3m/2 from above, each leg tends to
      −4E/(3m), not 0. The negative energy gathers at the throat.
  - *First written:* "Control: an ordinary black hole (r₀ = 3m/2) meets no energy at all". That case has no throat and no
    passage. Its zero is check 1's factor (2r₀ − 3m), so it is now STRUCTURAL.
- **3. The bulk near the plane keeps the condition.**
  - `escape.py` (section 8m, seated, S3): *"With tau = 0: K = -a q exactly, the scalar Gauss equation reads R = 0
    (met), Codazzi holds, the NEC holds -- on either sign of the tension. The bulk keeps only its vacuum energy (the NEC,
    saturated); E = -G carries the whole reading"*.
  - In plain terms: the plane carries no matter (τ = 0, so its own NEC holds trivially), and the bulk carries only vacuum
    (the NEC, saturated).
  - The scope: locally, under H-RS1, with Anderson's objection carrying. The global bulk is BULK5-O1. Its existence is
    carried on your path (item 120); building it is OPEN.
  - *First written:* the quote began at *"the NEC holds"*, under "The bulk keeps the condition". That clause is about
    the plane's matter, so read alone it changed subject. Also *first written:* "is not broken in the full spacetime the
    plane sits in". That dropped "locally".
- **4. A published theorem forces the appearance (READ).**
  - **Friedman, Schleich & Witt**, gr-qc/9305017v2, Thm 1 p.3: *"If an asymptotically flat, globally hyperbolic
    spacetime (M, g_ab) satisfies the averaged null energy condition, then every causal curve from J− to J+ is
    deformable to γ0 rel J"*.
    - The condition is defined on p.3 along *"every inextendible null geodesic"*.
    - Lemma 2, p.5: no strongly outer trapped surface meets the causal past of J+_α. The proof runs on null focusing,
      so on the plane the binding quantity is G_kk.
  - PLANE point 1 gives a causal curve from P1's past infinity to P2's future infinity, and both ends are flat.
  - So in any four-dimensional reading, **a one-way passage between two flat ends must break the averaged condition
    somewhere**, unless global hyperbolicity fails (H-GLOBAL-HYPERBOLIC, OPEN; PLANE: completeness OPEN).
  - Point 2 is what the theorem requires. It is not a contingent fact about this family.
  - The same paper, p.8: *"Wald and Yurtsever show that ANEC is violated by the renormalized stress tensor of free
    fields in generic spacetimes"*.
  - **Whether a five-dimensional censorship theorem binds the bulk is NOT READ, OPEN.** This is your coin's sharpest
    open question. If one did bind it, with the bulk keeping the condition, the passage itself would be forbidden.
- **5. One curve, both faces: a candidate, OPEN.**
  - S3 has K = −a q. If that makes the plane umbilic, then K_μν k^μ k^ν = 0, and the passage's light ray is also a light
    ray of the bulk (standard, NOT READ here).
  - Along it, a bulk of vacuum energy alone gives R⁽⁵⁾_kk = 0. The same curve would then read −1.914712 E/m in the
    plane and exactly 0 in the bulk.
  - Carried as **H-UMBILIC-GEODESIC**, the board's candidate. OPEN until it is computed and READ.
- **6. What the board already holds.**
  - **Maldacena–Susskind fn.1 p.2** (READ in geometry.py): non-traversability *"can be shown using the integrated null
    energy condition"*; *"If this were not true, the ER=EPR connection would be wrong"*.
    - The horizon member is one-way traversable, and point 2 has the integrated condition failing in the plane's reading.
    - So under H-ER=EPR, the corridor between two entangled positions lies outside Maldacena–Susskind's ER=EPR in that
      reading.
    - This bears on geometry.py's O-HOLD grading, which is not re-graded here.
  - **Gao–Wald fn.3 p.12** (READ in geometry.py): Borde's averaged condition may replace the NEC. Its premise fails on
    the plane, and holds, saturated, in the bulk.
- **7. Your two sides.**
  - You put *"each position"* on a separate side. The board's map of the sides onto plane and bulk is its own reading of
    "appears / is not". It does not test your sides-as-positions.
  - What the work shows about the positions:
    - In the plane both read alike: G_kk depends on r only, and the two legs are equal.
    - The asymmetry that exists is causal. P1 has a future (black-hole) horizon and P2 a past (white-hole) one
      (PLANE point 1). They are time-reversed images.
  - That pair is the board's candidate for your two sides, with the passage as the coin turning. OPEN.
    - Each side of the maximal extension has two exteriors. Which one a given ray reaches is not computed; the integral
      is the same either way.
  - *First written:* "That is the part of your coin the board can show."

## Your item 120

- *"it was an methaphor to describe that the NEC only ever appears to break, but never does"*. So there is no flip to
  compute. What the board can show is exactly that appearance: broken in our plane's reading along the whole passage
  (and forced there, point 4), kept in the bulk near the plane (point 3).
- On the bulk: *"yes. Science has already taught us that matter is neither created nor destroyed, it only changes
  geometric state."* (H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY).
  - On your path a complete bulk exists, so point 3's local statement extends to it.
  - The board reads "matter" as mass-energy, which general relativity conserves locally (H-MATTER-IS-MASS-ENERGY). Rest
    mass alone is not conserved, for example in pair creation (standard, NOT READ here).
  - Constructing the bulk is still a computation no one has done (BULK5-O1).

## Named hypotheses

- **Yours:** H-NEC-COIN (117; a metaphor, 120), H-COMPLETE-BULK and H-CONSERVATION-AS-GEOMETRY (120), H-READING-ONLY
  (86.1), H-CORRIDOR-HORIZON (104).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-AVERAGED-NEC: the test you approved;
  - H-PLANE-READING: the four-dimensional reading of the brane's projected stress;
  - H-RS1: the scope of the bulk statement;
  - H-GLOBAL-HYPERBOLIC and H-ASYMPTOTIC-FLAT-ENDS: point 4's premises;
  - H-UMBILIC-GEODESIC: point 5;
  - H-ER=EPR: point 6;
  - H-MATTER-IS-MASS-ENERGY: the board's reading of item 120.

## Sources READ

| source | route | used |
|---|---|---|
| Friedman, Schleich & Witt, gr-qc/9305017v2 | alphaXiv full text (verifier, then re-read for this write-up) | Thm 1 p.3; ANEC defined p.3; Lemma 2 p.5 and the proof p.6; Wald–Yurtsever p.8 |
| Maldacena & Susskind fn.1; Gao & Wald fn.3 | geometry.py (READ there) | point 6 |
| Bronnikov & Kim, gr-qc/0212112 | plane.py, escape.py (READ there) | eq. 17 p.4; p.6 |

## OPEN

1. The flip. *Closed by your item 120: a metaphor; the NEC only appears to break.*
2. Constructing the complete bulk (BULK5-O1). Its existence is carried on your path (item 120).
3. Whether a five-dimensional censorship theorem binds the bulk (point 4). NOT READ.
4. H-UMBILIC-GEODESIC: one curve reading −1.914712 E/m in the plane and 0 in the bulk (point 5).
5. Whether the corridor's spacetime is globally hyperbolic (point 4's escape clause).
6. Your two sides as the time-reversed horizon pair (point 7).

## History (verifier, 2026-10-06)

Thirteen findings were applied:

- "Against the coin" bent H-NEC-COIN: it refuted the board's expectation, not your statement.
- The exact closed form was missing. With it: the bounds, every member negative, and the horizon playing no part.
- Units were not stated: the values are ∫G_kk dλ in E/m, and ÷8π gives the plane's effective T_kk.
- The Schwarzschild control was tautological. The integrator had no control. Both are now controlled by the closed form,
  the m = 0 value, and the Einstein pipeline on an independent Schwarzschild metric.
- The contrast restated a definition.
- O3's horizon exception was the same artifact.
- The S3 quote was elided, which changed its subject.
- The scope dropped "locally".
- The candidate both-faces curve was added.
- Friedman–Schleich–Witt was added.
- Maldacena–Susskind fn.1 and Gao–Wald fn.3 were added.
- The sides were re-read.
- Wording: "average" became "ANEC integral"; the READ part of check C3 is labelled as such.
