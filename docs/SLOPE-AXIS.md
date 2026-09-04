# `tools/slopeaxis.py` — the occupation law of Chapter 34 as one object

## What it is

§34.4 states the rule as **ν = n − a·√r**, with r = p + q/2(2ℓ+1), and the incoming electron takes
the least ν. Minimising `n − a·√r` is minimising **y − a·x** at the point **(x, y) = (√r, n)**.

So every admissible subshell is a **point in a plane**, and `a` is a **slope**: a line of slope `a`
rising from below stops at one point, and **only vertices of the lower convex hull can ever be that
point**, for any `a` whatsoever.

An element's place on the axis is the interval between the **two hull-edge slopes flanking its
observed entrant** — which is §34.5's corridor `L(Z) < a < U(Z)`, arrived at from the other side.

That identity is not assumed. `--selftest` checks the corridor set against the hull-vertex set at
all 106 steps in **both** forms and fails on any mismatch. It currently reports 0 mismatches, and
La's printed corridor (0.7071068, 1.7071068) is checked to equal the slopes of hull edges 4f→5d and
5d→6p.

## Running it

    python3 tools/slopeaxis.py --selftest              # 21 fixtures, the corpus's own numbers
    python3 tools/slopeaxis.py --report                # the object, in text
    python3 tools/slopeaxis.py --json  out/axis.json   # the object, as data
    python3 tools/slopeaxis.py --html  out/slope-axis.html

The page is **generated, never hand-edited** — regenerate it rather than patching the HTML. It is a
single self-contained file: drag the vertical rule across the slope axis to see how many of the 106
elements one fixed `a` can cover, and click any element to see its point set, its lower hull, and
the tangent line at the current slope.

It **imports** the seated member `method/members/r2-ch16y.py` by path for the observed ground
configurations and the corridor machinery. It reimplements neither. Stdlib only, Python 3.9+.

## What the object shows

| | node-only ν = n − a√p | finished ν = n − a√(p+q/cap) |
|---|---|---|
| entrant corridor non-empty | 106 of 106 | 106 of 106 |
| distinct hull-edge slopes | 17 | 121 |
| best coverage by one fixed `a` | 86 of 106 at a = 0.5780 | 90 of 106 at a = 1.0010 |
| running intersection empties | 14× | 11× |
| walk resets (register 1328) | 10 | 15 |
| steps admitting exactly one subshell | **0** | **0** |

A single `a` is a single vertical rule, and it never crosses all 106 bars. That is what "the state is
necessary" establishes: necessary **to this rule**, so that `a` may be re-set and remain exact.

## Three things it refuses to do

1. **It never draws a row past Z = 108.** Register 1304: there are **four edges, not two** — optical
   spectroscopy ends at 102, the NIST ASD listing holds no neutral ground configuration past 108,
   synthesis ends at 118, and Janet's lattice counts 120 cells. A row beyond the listing would be an
   invented cell, which register 1288 already refused once. The four edges are printed as an
   annotation and never as data.

2. **It never reports a coverage figure without naming the form and the sign convention.** Coverage
   under `a ∈ ℝ` and under `a > 0` are different numbers; the corpus records both, and docket 20x is
   not closed by picking one.

3. **It never merges the two forms.** Node-only gives 17 distinct edge slopes and 14 forced
   emptyings; the finished form gives 121 and 11. Averaging them, or silently defaulting to
   whichever is prettier, would flatten docket 37. Both are computed, both emitted, neither
   preferred.

## Its own defect, recorded

The first draft computed "entrant corridor non-empty" as `... or True` — 106 by construction, in
both `--report` and `--selftest`. A test that could not fail, which is §4.6's own defect class,
written into the instrument that exists to illustrate §34.6. Repaired before first commit: the
non-emptiness is now stored per step and counted, and a second fixture asserts the observed entrant
is a hull vertex at every step. Recorded here rather than quietly fixed.

## What it does not settle

- **The sign of `a`.** The `a ∈ ℝ` reading makes "at least two subshells are ν-self-consistent" a
  theorem for every neutral atom below Z = 124. Under `a > 0` it is false in general: the unfilled
  set {3s, 4p, 4d, 4f, 5d, 5f, 6f} with everything else at capacity gives |A| = 1, and needs only
  **86 electrons**. That configuration is Pauli-admissible and not remotely reachable, but the bound
  is below Z = 118, so the restriction cannot be discharged by a bound on Z alone.
- **Φ, the class of admissible rules.** The theorem is about the ν-family. §34.6's sentence
  quantifies over all rules and is false as literally quantified — a lookup table is a memoryless
  function of one configuration.
