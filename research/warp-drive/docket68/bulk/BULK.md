# Two planes joined through a higher dimension (H-HIGHER-CORRIDOR, H-NO-SPEED; not verified; not seated; 2026-10-05)

## M's words and how they are carried

- **Item 57, verbatim:** *"If two points, each on a different spacetime plane, are connected by a corridor through a
  higher dimension, then speed cannot exist in the dimension below the corridor as you are at position 1 then position
  2, with no in between, which means no travel, no speed"*.
- **Item 58:** *"3, then 2, then 1 please"*. So the case is fixed first as two separate planes, then the sources are
  READ, then the corridor is modelled.

These are carried as M's hypotheses **H-NO-SPEED** and **H-HIGHER-CORRIDOR**, never as results. O9 stays OPEN.

Every number below is printed by `bulk.py`. Its selftest runs 6/6 checks, 1 of them a control, with 3 STRUCTURAL lines
printed and not counted. It asks `branelink.py` for its constants and for the board's moving-brane figure (O7).

## Step 3: the case is two planes

**The case.** Two separate 4D worlds, each its own spacetime plane, joined only through a fifth dimension.

**The published model that is exactly this** is Randall & Sundrum's two-brane set-up (hep-ph/9905221v1, READ):
- **The geometry.** The metric is ds² = e^(−2kr_c|φ|) η dx dx + r_c² dφ² (eq. 12, p.4). It has two branes, "hidden" at
  φ = 0 and "visible" at φ = π, and the space between them is "a slice of an AdS5 geometry".
- **What lives where.** Ordinary fields live on a brane; gravity lives in the bulk between them. The bulk's gravitational
  modes couple to visible-brane matter at "Energy/TeV" (p.6), far more strongly than ordinary gravity.
- **The warp factor.** RS take e^(kπr_c) "of order 10^15" (p.6), which gives kr_c = 10.99.
  - **Discrepancy:** the same page, as extracted, reads "kr_c [symbol lost] 50". The board uses the warp factor the
    paper states (H-RS1-WARP).

## Step 2: what the sources say (READ via alphaXiv, 2026-10-05)

- **Chung & Freese (hep-ph/9906542v2 p.13).** Regions that seem causally disconnected "might in fact have talked to each
  other because of a geodesic between them that went off our brane, into the bulk, and then back onto our brane".
- **Caldwell & Langlois (gr-qc/0103070v1).**
  - A bulk graviton between two brane points can "appear quicker than a photon" (abstract).
  - For a static brane (strict Randall–Sundrum) or de Sitter, "the photon horizon and the bulk gravitational horizon
    would be exactly identical" (p.5).
  - "there is no shortcut for compact, flat extra dimensions" (p.8).
  - Today the advance is r_g/r_γ ≈ 1 + (1/10)(ℓH₀)²(1+z)^(5/2), with ℓH₀ ≲ 10⁻²⁹ (eq. 22).
- **The board's own one-plane case** (D13, O7, `branelink.py`). Bulk paths join brane points that the brane itself calls
  causally disconnected.

## Step 1: the model, computed, with no speed anywhere

### 1. The jump between the planes

- **The geometry makes it simple.** In conformal coordinates the bulk is conformal to flat 5D space, so null paths are
  straight lines.
- **The checks.** Integrating the null path numerically in the original coordinate reproduces the closed form to
  1.6×10⁻¹⁵, and to 2.8×10⁻¹⁵ with sideways motion.
- **What each end's own clock reads** (H-LOCAL-CLOCK) for the jump between bulk-paired points, at k = 2×10¹⁸ GeV
  (H-K-PLANCK):

  | clock | reads |
  |---|---|
  | the hidden plane's | 3.29×10⁻²⁸ s |
  | **the visible plane's (ours)** | **3.29×10⁻⁴³ s** |

  - The two readings differ by exactly the warp factor, 10¹⁵.
  - **Control:** with the warping nearly removed, the same functions give the two clocks equal (ratio 1.000000001). So
    the split is the warping's.
- **Speed is undefined here, as M said.** There is no path *in either plane* between the two events, so a speed (a
  length over a time along a path in the plane) is undefined there, not merely large (STRUCTURAL). What remains is each
  end's own clock reading, and on our side that reading is about the Planck time.

### 2. A jump that also lands somewhere else

- **What "the same place" means.** Which point on one plane counts as "the same place" as a point on the other is fixed
  by the bulk's shared coordinates, not by either plane (H-BULK-PAIRING).
- **Landing elsewhere costs the light time.** To land a lateral distance D away, the visible clock reads at least D's
  light time. For the Proxima span that is 4.246500 yr, equal to the light time.

### 3. One plane, two places (the board's present case)

- **Static case: no shortcut.** In static Randall–Sundrum, going into the bulk and back is never shorter than the brane
  path. The detour costs between +1.2×10⁻²⁰ and +3.1×10⁻³⁷ in coordinate units, at offsets from 1 m to the Proxima span.
  This agrees with Caldwell–Langlois p.5.
- **Expanding brane:** the advance is 1.0×10⁻⁵⁹ today, or 3.9×10⁻⁵² for signals from z = 1090.
- **Moving brane** (`branelink`, O7): **93.8 ns** saved over 4.2465 yr. This is conditional on the graviton being a bulk
  degree of freedom and on B = 0, as O7 records.

### 4. Loops (STRUCTURAL)

The static two-brane metric has a global time, so it has no closed causal loop. The board's theorem D21 covers the
moving-brane case.

### 5. Entering and leaving (STRUCTURAL; O6, OPEN)

In Randall–Sundrum ordinary matter is confined to its plane, and what crosses the bulk is gravitational. On M's ruling
(M-D68-1), what crosses is the defining information. No one has computed a rate for entering or leaving the corridor
(O6).

## For M

- **Your two-plane corridor exists as published physics** (Randall–Sundrum's two branes). Between bulk-paired points
  there is no path in either plane, so **speed does not exist there**, as you said.
- **Each end's own clock still reads something.** Ours reads about the Planck time (3.3×10⁻⁴³ s); the other plane's reads
  10¹⁵ times longer, from the warping. That is your local clock, with no speed involved.
- **The catch is where the corridor lands.** It joins a point of one plane to its bulk partner on the other. Landing
  somewhere *else* on our plane (Proxima, say) costs at least that place's light time on our clock. And on one plane
  alone, the published geometries give no shortcut (static), a negligible one (expanding), or 93.8 ns over 4.2 years
  (the board's moving brane).
- **So on this model the question becomes one of pairing.** Is the destination the bulk partner of the origin? That is,
  are Earth here and the arrival point there "the same place" through the higher dimension? That is H-BULK-PAIRING, and
  no source says what fixes it for two chosen places.

## Named hypotheses

- H-RS1, H-RS1-WARP and H-K-PLANCK.
- H-BULK-PAIRING.
- H-GRAVITATIONAL-CARRIER.
- M's H-NO-SPEED, H-HIGHER-CORRIDOR and H-LOCAL-CLOCK.

## OPEN

1. What makes two chosen places bulk partners (H-BULK-PAIRING): a geometry in which the origin and the destination are
   bulk-paired.
2. Entering and leaving the corridor (O6): a rate for coupling a carrier into the bulk and back out.
3. Whether the other plane exists and holds matter: Randall–Sundrum's hidden brane is a model, not an observation.
4. The extracted "kr_c ≈ 50" against e^(kπr_c) = 10¹⁵: a page reading at source.
