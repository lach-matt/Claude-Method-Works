#!/usr/bin/env python3
"""
pathmetric.py -- the method equation asked what it is for: the distance between
two points of an index, and the cheapest path between them.  Run on spacetime.

THE EQUATION HAS TWO HALVES AND THE CORPUS NAMES BOTH.  Register 1206: "the two
halves of the method equation meet for the first time on this index" -- R places
cells and the channel equation values them.  Structurally, E(X) = |R(X)| - |X|;
metrically, E_W(X) = |W(X)| - |X|, W the reachable set under a step set with
accumulated cost, whose prior art the Mathematical Compendium gives as Dijkstra
1959 and Freuder 1978.  M states the partition outright: "the Method equation
partitions an index into three populations: interior captures, the working
overlap, and exterior predictions".

AND THE CORPUS ALSO NAMES WHICH HALF SPACETIME GETS.  Section 12.11.1.3: AN INDEX
HAS A TIME COLUMN EXACTLY WHEN ITS CELLS ARE MOVES.  Events are configurations,
not moves, so the time column goes and -- the corpus's own words, on L3 -- "the
flow becomes the geodesic flow of the Jacobi-Maupertuis metric.  Time returns as
a quadrature carrying the transcendental part."  Section 12.11.4's "precision is
path-dependent; physics is not" is named there as the geodesic equation itself.

So the answer to "spacetime is an index" is not an analogy this file has to
argue.  It is a selector the corpus already applies, and it sends you to a metric
that general relativity already has.  Which means the honest first job is not to
use the tool but to CHECK IT AGAINST WHAT WE KNOW, and then see what it measures.

-- PART 2 CHECKS OUT, EXACTLY -------------------------------------------------
For a static spacetime ds^2 = -V^2 dt^2 + g_ij dx^i dx^j the Jacobi metric of a
particle of mass m and energy E is

        J_ij  =  (E^2 - m^2 V^2)/V^2  ·  g_ij

and its geodesics are the spatial orbits.  Verified here against the Schwarzschild
orbit equation at 3,000 random (r, E, L): worst relative error 1.0e-13, with the
Jacobi conserved quantity equal to L exactly.  Its degeneracies are the two
surfaces physics already knows -- V = E/m, the turning point, which for the
three-body index is Hill's 1878 zero-velocity surface where the corpus says the
geodesic flow stops; and V = 0, the horizon, which is where the massless
(optical) metric E^2 g/V^2 blows up.

    THE HORIZON THIS PROJECT KEPT HITTING IS THE ZERO-VELOCITY SURFACE OF THE
    METHOD EQUATION'S OWN METRIC HALF.  Not a warp pathology; a degeneracy of
    the Jacobi metric, classical since Hill.

-- AND THEN IT MEASURES THE SHIFT, AND THE ANSWER IS NEGATIVE -----------------
twist.py proved the 1+1D warp metric is static, with V^2 = c^2 - v^2 and
g_xx = c^2/(c^2 - v^2).  So the metric half applies directly.  Light in the
original Painleve-Gullstrand time obeys dt = dx/(c + v) forward and dx/(c - v)
back, so:

        one-way, forward   SHORTER      5.20558 against 6.00000 flat  (-13.2%)
        one-way, backward  longer       8.66048
        ROUND TRIP         LONGER       13.86606 against 12.00000    (+15.6%)

and the round trip is exactly the optical length INTEGRAL 2c dx/(c^2 - v^2),
checked to 1e-6.  The excess has a closed form and it is a strict inequality:

        2c/(c^2 - v^2)  -  2/c   =   2 v^2 / (c (c^2 - v^2))   >   0

for every v != 0.  So on the gauge-invariant measure -- the only one the metric
half offers -- ANY 1+1D SHIFT MAKES THE PATH STRICTLY LONGER, and the one-way
saving is precisely the simultaneity convention twist.py already showed to be a
global gauge choice (T = t + INTEGRAL v dx/(c^2-v^2)).  Three instruments now
say the same thing about 1+1D by three unrelated routes: the shift is gauge
(twist.py), it carries no twist (twist.py), and it costs distance (here).

WHAT IS NOT SETTLED, AND IT IS THE SAME GAP AS BEFORE: in 3+1D the metric is not
static -- the twist is nonzero -- so there is no global T, no optical metric of
this form, and no round-trip theorem.  The measurement above is a 1+1D result and
this file does not extend it.  That is the third time the same dimensional
boundary has decided a question in this series, which is itself the finding.

-- A FAULT IN THE CORPUS, RECORDED AND NOT REPAIRED ---------------------------
Checking the lattice half against its own statement turned one up.  M's "The
lattice metric" (proved M section 9.2; Monjardet 1981) defines
d(x,y) = PRODUCT_i (|x_i - y_i| + 1) and writes:

  "Equality holds on an axis iff st = 0, i.e. y lies between x and z there, so
   global equality iff y in [x^z, xvz] -- y on a geodesic"

The first clause is right and the gloss after "i.e." is strictly weaker than it.
Per-axis equality needs (|a-c|+1) = (s+1)(t+1), i.e. |a-c| = st + s + t, and
|a-c| <= s + t always, so it forces st = 0 -- meaning y_i EQUALS x_i or z_i, not
merely that it lies between them.  Counterexample in one dimension:
x = 0, y = 1, z = 2 has y between, and d(x,z) = 3 against d(x,y)d(y,z) = 4.

    THE GEODESIC SET IS THE VERTEX SET OF THE BOX SPANNED BY x AND z, NOT THE
    INTERVAL.  On Lambda's eight axes two cells three apart on each have an
    interval of 65,536 cells and a geodesic set of 256 -- a factor of 256, and
    6,561 at five apart.

The corpus's own check could not have caught it: it reports "4,000 of 4,000
sampled triples satisfy the INEQUALITY", and the inequality is not in question --
0 violations here too, over all 2,744 triples of index3's cells and 4,000 random
8-tuples.  It is the equality condition that is misglossed, and nothing sampled
it.  Recorded under the chat-67 full hold; no member is edited.

The underlying reason is worth stating because it bears on the question asked.
log(|D| + 1) is STRICTLY CONCAVE in |D|, so the metric rewards one long step and
penalises subdivision: an index in this metric is NOT A LENGTH SPACE, and its
first step costs log 2 however fine you try to make it.  A continuum has no such
quantum.  That is the precise sense in which spacetime is not an index of the
lattice kind -- and exactly why section 12.11.1.3 routes it to the other half.

stdlib only.  index3 is imported for its cells rather than transcribed.
"""
import math, random, sys

C = 1.0

# ---------------------------------------------------------------- the lattice --

def d(x, y):
    """M section 9.2: d(x,y) = PRODUCT (|x_i - y_i| + 1).  d >= 1, = 1 iff x = y."""
    p = 1
    for a, b in zip(x, y):
        p *= abs(a - b) + 1
    return p

def log_d(x, y):
    return sum(math.log(abs(a - b) + 1) for a, b in zip(x, y))

def join(x, y):
    return tuple(max(a, b) for a, b in zip(x, y))

def meet(x, y):
    return tuple(min(a, b) for a, b in zip(x, y))

def in_interval(y, x, z):
    """y in [x^z, xvz] -- the corpus's PRINTED condition."""
    lo, hi = meet(x, z), join(x, z)
    return all(l <= w <= h for w, l, h in zip(y, lo, hi))

def is_vertex(y, x, z):
    """y_i in {x_i, z_i} for every i -- the CORRECT condition."""
    return all(w == a or w == b for w, a, b in zip(y, x, z))

def saturates(x, y, z):
    """Whether d(x,z) = d(x,y) d(y,z) -- measured, not predicted."""
    return d(x, z) == d(x, y) * d(y, z)

def interval_size(x, z):
    p = 1
    for a, b in zip(x, z):
        p *= abs(a - b) + 1
    return p

def vertex_count(x, z):
    return 2 ** sum(1 for a, b in zip(x, z) if a != b)

def first_step_cost():
    """The quantum: the first step on an axis costs log 2, the tenth log(11/10)."""
    return math.log(2.0), math.log(11.0 / 10.0)

# ------------------------------------------------------- the Jacobi metric --

def V2_schwarzschild(r, M=1.0):
    return 1.0 - 2.0 * M / r

def jacobi_factor(V2, E, m=1.0):
    """(E^2 - m^2 V^2)/V^2.  m = 0 gives the optical metric E^2/V^2."""
    return (E * E - m * m * V2) / V2

def orbit_schwarzschild(r, E, L, M=1.0):
    """(dr/dphi)^2 from the standard effective potential, m = 1."""
    V2 = V2_schwarzschild(r, M)
    return r ** 4 / (L * L) * (E * E - V2 * (1.0 + L * L / (r * r)))

def orbit_jacobi(r, E, L, M=1.0):
    """(dr/dphi)^2 from the Jacobi metric, with conserved quantity h = L.
    J_rr = (E^2-V^2)/V^4, J_pp = (E^2-V^2) r^2/V^2, and
    (dr/dphi)^2 = (J_pp/J_rr)(J_pp/h^2 - 1)."""
    V2 = V2_schwarzschild(r, M)
    J_rr = (E * E - V2) / (V2 * V2)
    J_pp = (E * E - V2) * r * r / V2
    return (J_pp / J_rr) * (J_pp / (L * L) - 1.0)

def turning_point(E, M=1.0):
    """V = E/m with m = 1: the Jacobi metric degenerates.  Hill's zero-velocity
    surface, where the corpus says the geodesic flow stops."""
    return 2.0 * M / (1.0 - E * E) if E < 1.0 else None

def horizon_radius(M=1.0):
    """V = 0: where the optical metric blows up."""
    return 2.0 * M

# --------------------------------------------------- the warp measurement --

def shift(x, v0=0.6, sigma=4.0, R=1.0):
    """A subluminal 1+1D bump, v(x), vanishing at infinity."""
    return v0 * (math.tanh(sigma * (x + R)) - math.tanh(sigma * (x - R))) \
        / (2.0 * math.tanh(sigma * R))

def one_way(a=-3.0, b=3.0, forward=True, n=400000, **kw):
    """Coordinate time in the ORIGINAL Painleve-Gullstrand t.  From ds^2 = 0,
    dx/dt = v +/- c, so dt = dx/(c + v) forward and dx/(c - v) back."""
    h = (b - a) / n
    t = 0.0
    for i in range(n):
        v = shift(a + (i + 0.5) * h, **kw)
        t += h / (C + v) if forward else h / (C - v)
    return t

def round_trip(a=-3.0, b=3.0, n=400000, **kw):
    return one_way(a, b, True, n, **kw) + one_way(a, b, False, n, **kw)

def optical_length(a=-3.0, b=3.0, n=400000, **kw):
    """INTEGRAL 2c dx/(c^2 - v^2), the gauge-invariant two-way measure."""
    h = (b - a) / n
    s = 0.0
    for i in range(n):
        v = shift(a + (i + 0.5) * h, **kw)
        s += 2.0 * C * h / (C * C - v * v)
    return s

def excess_density(v):
    """2c/(c^2-v^2) - 2/c = 2 v^2/(c(c^2-v^2)).  Strictly positive for v != 0."""
    return 2.0 * v * v / (C * (C * C - v * v))

# ------------------------------------------------------------------ selftest --

def _cells():
    import index3
    return sorted({index3.coords(f) for f in index3.FINDINGS})

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("THE LATTICE HALF -- d, and what saturates the triangle inequality")
    chk("d(x,x) = 1", d((1, 2, 3), (1, 2, 3)), 1)
    chk("d is symmetric", d((0, 5), (3, 1)), d((3, 1), (0, 5)))
    chk("log d is additive over axes", log_d((0, 0), (2, 3)),
        math.log(3) + math.log(4), 1e-14)
    lo, hi = first_step_cost()
    chk("the first step on an axis costs log 2", lo, math.log(2.0), 1e-15)
    chk("...and the tenth log(11/10) -- the metric has a quantum", hi,
        math.log(1.1), 1e-15)

    cells = _cells()
    trip = [(x, y, z) for x in cells for y in cells for z in cells]
    viol = sum(1 for x, y, z in trip if d(x, z) > d(x, y) * d(y, z))
    chk("triangle inequality over all %d triples of index3's cells" % len(trip), viol, 0)
    random.seed(7)
    rnd = [tuple(tuple(random.randint(-9, 9) for _ in range(8)) for _ in range(3))
           for _ in range(4000)]
    chk("...and the corpus's own 4,000 random 8-tuples",
        sum(1 for x, y, z in rnd if d(x, z) > d(x, y) * d(y, z)), 0)

    print("\n  THE FAULT: the printed equality condition is too weak")
    chk("x=0, y=1, z=2 has y between x and z", in_interval((1,), (0,), (2,)), True)
    chk("  d(x,z)", d((0,), (2,)), 3)
    chk("  d(x,y) d(y,z)", d((0,), (1,)) * d((1,), (2,)), 4)
    chk("  so betweenness does NOT give equality", saturates((0,), (1,), (2,)), False)
    chk("  and y is not a vertex", is_vertex((1,), (0,), (2,)), False)
    printed = sum(1 for x, y, z in trip if in_interval(y, x, z) != saturates(x, y, z))
    correct = sum(1 for x, y, z in trip if is_vertex(y, x, z) != saturates(x, y, z))
    # NOTE: this count tracks index3's live cells, which grew 14 -> 15 when
    # TYPE-IV opened (+1,-1,-1), and 15 -> 16 when overturn.py's
    # BALL-AND-CHORD-INDEPENDENT opened (0,+1,0).  14^3 = 2,744 triples became
    # 15^3 = 3,375 and then 16^3 = 4,096; the mismatches went 204 -> 252 -> 310.
    # The fixture moves with the index by design: it is measuring the corpus's
    # condition over THIS project's cells.  It is also the ONLY fixture outside
    # index3.py that does, which is why a seating pass must run the whole sweep
    # and not just the files it edited -- this one was caught that way.
    chk("printed condition mismatches on index3's cells", printed, 310)
    chk("VERTEX condition mismatches", correct, 0)
    pr = sum(1 for x, y, z in rnd if in_interval(y, x, z) != saturates(x, y, z))
    cr = sum(1 for x, y, z in rnd if is_vertex(y, x, z) != saturates(x, y, z))
    chk("printed condition mismatches on the 4,000", pr, 3)
    chk("VERTEX condition mismatches", cr, 0)
    print("      the corpus sampled the INEQUALITY only, so nothing tested this")

    print("\n  and the geodesic set is exponentially smaller than the interval")
    for w in (1, 3, 5):
        x = tuple([0] * 8)
        z = tuple([w] * 8)
        print("      8 axes, %d apart: interval %8d   geodesics %5d   factor %5d"
              % (w, interval_size(x, z), vertex_count(x, z),
                 interval_size(x, z) // vertex_count(x, z)))
    chk("at 5 apart the overcount is 6,561x",
        interval_size(tuple([0]*8), tuple([5]*8)) // vertex_count(tuple([0]*8), tuple([5]*8)),
        6561)

    print("\nTHE JACOBI HALF -- checked against a spacetime we already know")
    random.seed(11)
    # Compare against the NATURAL SCALE r^4 E^2/L^2, not against (dr/dphi)^2
    # itself: the two agree algebraically, so near a turning point where both
    # tend to zero a ratio measures cancellation, not disagreement.
    worst = 0.0
    for _ in range(3000):
        r = random.uniform(3.5, 60.0)
        E = random.uniform(0.95, 1.4)
        L = random.uniform(3.6, 12.0)
        a, b = orbit_schwarzschild(r, E, L), orbit_jacobi(r, E, L)
        scale = r ** 4 * E * E / (L * L)
        worst = max(worst, abs(a - b) / scale)
    chk("Jacobi orbit == Schwarzschild orbit, 3000 samples", worst, 0.0, 1e-14)
    chk("optical metric is the m -> 0 limit", jacobi_factor(0.5, 2.0, 0.0),
        4.0 / 0.5, 1e-14)
    chk("turning point at E = 0.99 is r = 2M/(1-E^2)", turning_point(0.99),
        2.0 / (1.0 - 0.99 ** 2), 1e-12)
    chk("no turning point for an unbound particle", turning_point(1.2), None)
    chk("the optical metric diverges at the horizon", horizon_radius(1.0), 2.0)
    print("      V = E/m is Hill's zero-velocity surface; V = 0 is the horizon.")

    print("\nTHE MEASUREMENT -- does the shift shorten the path?")
    fw, bk = one_way(forward=True), one_way(forward=False)
    rt, op, flat = round_trip(), optical_length(), 2.0 * 6.0
    print("      forward one-way   %.6f   (flat %.6f)" % (fw, 6.0))
    print("      backward one-way  %.6f" % bk)
    print("      round trip        %.6f   (flat %.6f)" % (rt, flat))
    chk("the forward one-way IS shorter", fw < 6.0, True)
    chk("  by 13.2%", (6.0 - fw) / 6.0, 0.13240, 1e-4)
    chk("the backward one-way is longer", bk > 6.0, True)
    chk("the ROUND TRIP is longer", rt > flat, True)
    chk("round trip == the optical length exactly", rt, op, 1e-6)
    chk("  the excess", rt - flat, 1.866057, 1e-4)
    print("\n      and the excess density is a strict inequality, pointwise:")
    for v in (0.0, 0.2, 0.5, 0.9):
        e = excess_density(v)
        print("        v = %.2f   2c/(c^2-v^2) - 2/c = %.8f" % (v, e))
        chk("        positive iff v != 0 at v=%.2f" % v, e > 0.0, v != 0.0)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("WHAT THE METHOD EQUATION SAYS ABOUT A WARP SHIFT\n")
    fw, bk = one_way(forward=True), one_way(forward=False)
    rt, flat = round_trip(), 12.0
    print("  %-24s %14s %14s %12s" % ("measure", "with shift", "flat", "verdict"))
    print("  %-24s %14.6f %14.6f %12s" % ("forward one-way", fw, 6.0, "shorter"))
    print("  %-24s %14.6f %14.6f %12s" % ("backward one-way", bk, 6.0, "longer"))
    print("  %-24s %14.6f %14.6f %12s" % ("round trip (invariant)", rt, flat, "LONGER"))
    print("\n  The one-way saving is the simultaneity gauge.  The invariant is worse.")
    print("\nTHE TWO DEGENERACIES OF THE METRIC HALF\n")
    print("  V = E/m   turning point   Hill 1878 zero-velocity surface; flow stops")
    print("  V = 0     horizon         optical metric E^2 g/V^2 blows up")
    print("\n  The horizon this project kept hitting is the second of these.")
    print("\nTHE LATTICE HALF, AND ITS FAULT\n")
    print("  d(x,y) = PRODUCT (|x_i - y_i| + 1); geodesic iff y is a VERTEX of the")
    print("  box spanned by x and z -- not, as printed, any point of the interval.")
    for w in (1, 3, 5):
        x, z = tuple([0] * 8), tuple([w] * 8)
        print("    8 axes %d apart: interval %8d  geodesics %5d  overcount %5dx"
              % (w, interval_size(x, z), vertex_count(x, z),
                 interval_size(x, z) // vertex_count(x, z)))
    print("\n  log(|D|+1) is strictly concave, so the metric penalises subdivision:")
    print("  an index of this kind is not a length space and its first step costs")
    print("  log 2 = %.6f however fine you make it.  A continuum has no quantum," % math.log(2))
    print("  which is why section 12.11.1.3 routes spacetime to the other half.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
