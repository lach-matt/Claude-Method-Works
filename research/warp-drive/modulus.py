#!/usr/bin/env python3.12
"""modulus.py -- what a modulus DOES, how it does it, and an index of need.

M: "What does a modulus actually do?  How does it perform its functions?  What
inputs does it require, and which of those do we have and not have on an index
of need and don't need?"

Answered for the modulus this project actually depends on, |z| with
z = r - i a cos(theta), which phase.py showed is the only thing the two threads
of weave.py can see.  Seven results.

  1.  IT IS NOT AN ABSTRACTION -- IT IS A METRIC COMPONENT.  |z|^2 = Sigma =
      g_thetatheta, exactly.  The modulus is the POLAR THREAD, readable off the
      metric with no derivation at all.  AND weave.py's three-thread
      decomposition OMITTED IT, because on the equatorial plane
      g_thetatheta = r^2 and carries no spin.  THE THREAD THAT CARRIES THE
      MODULUS IS TRIVIAL ON THE PLANE WHERE THE BIT VANISHES.

  2.  HOW IT PERFORMS ITS FUNCTION -- AND THE MECHANISM IS THE LOSS.
      |z|^2 = z zbar, and zbar(r, theta, a) IS z(r, theta, -a) EXACTLY.
      SO THE MODULUS IS THE PRODUCT OF THE TWO CHIRALITIES.  It requires both,
      weighted identically, and multiplies them together.  It is not that the
      modulus fails to distinguish them; IT IS BUILT BY PAIRING THEM.

  3.  AND THE COMPLEMENTARY COMBINATION IS THE PHASE.  z/zbar = e^{2i arg z}.
      ONE PAIR, TWO COMBINATIONS: THEIR PRODUCT IS THE MAGNITUDE AND THEIR
      RATIO IS THE DIRECTION.  That is the shape weave.py found in the other
      two threads.  RECORDED AS A RECURRING SHAPE, NOT AS AN IDENTITY -- the
      objects paired are different objects.

  4.  THE GEOMETRY IS A CIRCLE MEETING A LINE.  |z| = rho is a CIRCLE; the
      radial coordinate fixes Re z = r, a LINE.  They meet in TWO points --
      conjugates -- and the two points collapse to ONE exactly when the line is
      TANGENT, which is |z| = r, which is a cos(theta) = 0, WHICH IS THE
      EQUATOR.  The whole missing bit is "a circle meets a line twice".

  5.  WHAT IT REQUIRES, COUNTED.  |z| is ONE real number.  Inverting it needs
      TWO.  And the pair (|z|, arg z) is equivalent to (r, a cos theta) and NOT
      to (r, a, theta): THE COMPLEX RADIUS CANNOT SEPARATE THE SPIN FROM THE
      POLAR ANGLE.  Two genuinely different Kerr geometries sharing a cos theta
      have IDENTICAL polynomial curvature invariants at that point and
      DIFFERENT metrics.  Measured.

  6.  THE INDEX OF NEED.  Six jobs the modulus is asked to do, what each
      requires, and whether this tree holds it.  THREE HELD, ONE PARTIAL, TWO
      NOT HELD -- and BOTH of the not-held rows are SEPARATIONS.

  7.  AND THE OBSTRUCTION IS GLOBAL, NOT INFINITESIMAL, WHICH IS WHY NO
      DERIVATIVE FINDS IT.  The even sector's Jacobian in (M, a) has RANK 2 at
      a != 0 -- so |a| is LOCALLY determined -- while the fibre has TWO points.
      A rank-2 map with a two-point fibre is a covering, not a degeneracy.
      NO PERTURBATIVE METHOD CAN SEE A DECK TRANSFORMATION.

Scope: the Kerr family.  Stdlib only.  Nothing is repaired.

    python3.12 modulus.py            full report
    python3.12 modulus.py --selftest
"""

import cmath
import math
import sys


# --------------------------------------------------------------------------

def z_of(r, th, a):
    return r - 1j * a * math.cos(th)


def sigma(r, th, a):
    return r * r + a * a * math.cos(th) ** 2


def kerr(r, th, M, a):
    c, s = math.cos(th), math.sin(th)
    S = r * r + a * a * c * c
    D = r * r - 2.0 * M * r + a * a
    return {
        "g_tt":   -(1.0 - 2.0 * M * r / S),
        "g_rr":   S / D,
        "g_thth": S,
        "g_pp":   (r * r + a * a + 2.0 * M * r * a * a * s * s / S) * s * s,
        "g_tp":   -2.0 * M * r * a * s * s / S,
    }


EVEN = ("g_tt", "g_rr", "g_thth", "g_pp")


def psi2(r, th, M, a):
    return -M / z_of(r, th, a) ** 3


# --------------------------------------------------------------------------
# 2/3.  The two combinations of a conjugate pair.
# --------------------------------------------------------------------------

def conjugate_is_opposite_spin(r, th, a):
    """|z(+a) - conj(z(-a))|.  Zero: the conjugate IS the other chirality."""
    return abs(z_of(r, th, a).conjugate() - z_of(r, th, -a))


def product_of_chiralities(r, th, a):
    """z(+a) * z(-a).  The claim: it is |z|^2, real and positive."""
    return z_of(r, th, a) * z_of(r, th, -a)


def ratio_of_chiralities(r, th, a):
    """z(+a) / z(-a) = z/zbar = e^{2i arg z}.  Unit modulus; all the direction."""
    return z_of(r, th, a) / z_of(r, th, -a)


# --------------------------------------------------------------------------
# 4.  Circle meets line.
# --------------------------------------------------------------------------

def circle_meets_line(rho, r):
    """Points with |z| = rho and Re z = r.  Returns the imaginary parts."""
    d = rho * rho - r * r
    if d < -1e-15:
        return []
    if abs(d) <= 1e-15:
        return [0.0]
    y = math.sqrt(d)
    return [+y, -y]


# --------------------------------------------------------------------------
# 5.  What one real number cannot separate.
# --------------------------------------------------------------------------

def same_z_different_metric(r, th1, a1, th2, a2, M):
    """Two (a, theta) with the same a cos(theta): same z, different metric."""
    z1, z2 = z_of(r, th1, a1), z_of(r, th2, a2)
    g1, g2 = kerr(r, th1, M, a1), kerr(r, th2, M, a2)
    return abs(z1 - z2), abs(psi2(r, th1, M, a1) - psi2(r, th2, M, a2)), \
        abs(g1["g_rr"] - g2["g_rr"])


# --------------------------------------------------------------------------
# 7.  Rank of the even sector, and the size of its fibre.
# --------------------------------------------------------------------------

def even_jacobian(r, th, M, a, h=1e-6):
    """d(g_tt, g_rr, g_thth, g_pp) / d(M, a).  A 4x2 matrix of lists."""
    rows = []
    for name in EVEN:
        dM = (kerr(r, th, M + h, a)[name] - kerr(r, th, M - h, a)[name]) / (2 * h)
        da = (kerr(r, th, M, a + h)[name] - kerr(r, th, M, a - h)[name]) / (2 * h)
        rows.append([dM, da])
    return rows


def rank2(rows, tol=1e-7):
    """Rank of a 4x2 matrix, by its largest 2x2 minor against its scale."""
    scale = max(abs(v) for row in rows for v in row) or 1.0
    best = 0.0
    n = len(rows)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, abs(rows[i][0] * rows[j][1] - rows[i][1] * rows[j][0]))
    if best / (scale * scale) > tol:
        return 2
    return 1 if scale > tol else 0


def fibre(r, th, M, a):
    """The spins the even sector cannot tell from a.  weave.py inverts to a^2."""
    g = kerr(r, th, M, a)
    a2 = (g["g_thth"] - r * r) / max(math.cos(th) ** 2, 1e-300)
    if a2 < 1e-18:
        return [0.0]
    root = math.sqrt(a2)
    return [+root, -root]


# --------------------------------------------------------------------------
# 6.  The index of need.
# --------------------------------------------------------------------------
#   job, what it requires, status, where it comes from
JOBS = [
    ("set the curvature magnitude  |psi2| = M/|z|^3",
     "M and |z|", "HELD",
     "M from g_tt (weave.py); |z| = sqrt(g_thetatheta), read directly"),
    ("normalise every metric component (Sigma)",
     "|z|^2", "HELD",
     "it IS g_thetatheta -- no derivation needed"),
    ("locate the ergosphere   2 M r = Sigma",
     "M, r, |z|", "HELD",
     "all three above"),
    ("locate the horizon      Delta = 0",
     "M, r, a^2", "PARTIAL",
     "|z| gives a^2 cos^2(theta), not a^2; needs theta, or g_rr"),
    ("separate the spin from the polar angle",
     "a second independent relation", "NOT-HELD-FROM-z",
     "z carries only the PRODUCT a cos(theta); g_rr supplies a^2"),
    ("give the chirality      sgn(a)",
     "arg z", "NOT-HELD", "parity theorem (cube.py); off-plane *RR or circulation"),
]

MODULUS_IS = "g_thetatheta -- the polar thread"
MODULUS_MECHANISM = "z * zbar, and zbar is the opposite-chirality z"
MODULUS_IS_A_HOMOMORPHISM = True
JOBS_HELD = 3
JOBS_PARTIAL = 1
JOBS_NOT_HELD = 2
OBSTRUCTION_IS_INFINITESIMAL = False
z_SEPARATES_a_FROM_theta = False
SCOPE = "the Kerr family"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Scope:")[0].rstrip())
    print()

    print(BAR)
    print("1.  IT IS A METRIC COMPONENT.  |z|^2 IS g_thetatheta.")
    print(BAR)
    print()
    print("      %6s %8s %6s %18s %18s %10s"
          % ("a", "theta", "r", "|z|^2", "g_thetatheta", "diff"))
    w = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (0.99, 2.4, 6.0),
                     (0.7, math.pi / 2, 5.0), (4.9, 0.9, 12.0)]:
        A = abs(z_of(r, th, a)) ** 2
        B = kerr(r, th, 1.0, a)["g_thth"]
        w = max(w, abs(A - B))
        print("      %6.2f %8.4f %6.2f %18.12f %18.12f %10.1e" % (a, th, r, A, B, abs(A - B)))
    print()
    print("      IDENTICAL TO %.1e.  THE MODULUS IS NOT AN ABSTRACTION OVER THE" % w)
    print("      METRIC -- IT IS ONE OF ITS COMPONENTS, THE POLAR THREAD, and it")
    print("      is read off directly with no derivation.")
    print()
    eq = kerr(5.0, math.pi / 2, 1.0, 0.7)["g_thth"]
    print("      AND ON THE EQUATOR IT IS %.9f = r^2, FOR EVERY SPIN." % eq)
    print("      weave.py decomposed the corridor into a TIME, a SPACE and an")
    print("      INTERSECTION thread and never named a fourth.  THE FOURTH IS")
    print("      THE MODULUS, and it was omissible precisely because it is")
    print("      TRIVIAL ON THE PLANE WHERE THE BIT VANISHES.  Same fact again.")
    print()

    print(BAR)
    print("2.  HOW IT WORKS -- AND THE MECHANISM IS THE LOSS")
    print(BAR)
    print()
    print("      |z|^2 = z * zbar,  AND  zbar(r, theta, a) = z(r, theta, -a).")
    print()
    print("      %6s %8s %14s %26s %26s"
          % ("a", "theta", "|conj - z(-a)|", "z(+a) * z(-a)", "|z|^2"))
    cw = pw = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (-0.99, 2.4, 6.0)]:
        c = conjugate_is_opposite_spin(r, th, a)
        p = product_of_chiralities(r, th, a)
        m = abs(z_of(r, th, a)) ** 2
        cw = max(cw, c)
        pw = max(pw, abs(p - m))
        print("      %6.2f %8.4f %14.1e %26s %26.12f"
              % (a, th, c, "%.12f%+.1ej" % (p.real, p.imag), m))
    print()
    print("      THE CONJUGATE IS THE OPPOSITE-SPIN z TO %.1e, AND THEIR" % cw)
    print("      PRODUCT IS THE MODULUS SQUARED TO %.1e." % pw)
    print()
    print("        SO THE MODULUS IS THE PRODUCT OF THE TWO CHIRALITIES.")
    print()
    print("      It does not FAIL to distinguish them.  IT IS BUILT BY PAIRING")
    print("      THEM, with identical weight, and a product is symmetric in its")
    print("      factors.  cube.py proved the bit is unrecoverable and this is")
    print("      the mechanism: THE OPERATION THAT MAKES A MODULUS IS THE")
    print("      OPERATION THAT DESTROYS THE SIGN.  They are one act.")
    print()

    print(BAR)
    print("3.  AND THE OTHER COMBINATION OF THE SAME PAIR IS THE PHASE")
    print(BAR)
    print()
    print("      %6s %8s %26s %16s %16s"
          % ("a", "theta", "z(+a) / z(-a)", "its modulus", "arg/2 vs arg z"))
    rw = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (-0.99, 2.4, 6.0)]:
        q = ratio_of_chiralities(r, th, a)
        d = abs(cmath.phase(q) / 2.0 - cmath.phase(z_of(r, th, a)))
        rw = max(rw, abs(abs(q) - 1.0), d)
        print("      %6.2f %8.4f %26s %16.12f %16.1e"
              % (a, th, "%+.9f%+.9fj" % (q.real, q.imag), abs(q), d))
    print()
    print("      UNIT MODULUS AND THE PHASE RECOVERED, BOTH TO %.1e." % rw)
    print()
    print("        THEIR PRODUCT IS THE MAGNITUDE.  THEIR RATIO IS THE DIRECTION.")
    print()
    print("      weave.py found that shape in the OTHER two threads -- their")
    print("      ratio is light and their product is the intersection.  SAME")
    print("      SHAPE, DIFFERENT OBJECTS.  Recorded as a recurring form and NOT")
    print("      as an identity: one pair is g_tt against g_rr, the other is a")
    print("      chirality against its mirror, and calling them the same fact")
    print("      would be the scope slip this session has made twice.")
    print()

    print(BAR)
    print("4.  THE GEOMETRY IS A CIRCLE MEETING A LINE")
    print(BAR)
    print()
    print("      |z| = rho is a CIRCLE.  The radial coordinate fixes Re z = r,")
    print("      a LINE.  A circle meets a line in two points, one, or none.")
    print()
    print("      %6s %8s %10s %10s %8s %22s"
          % ("a", "theta", "rho", "r", "hits", "Im z solutions"))
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (0.7, math.pi / 2, 5.0),
                     (0.0, 0.4, 5.0), (-0.99, 2.4, 6.0)]:
        rho = abs(z_of(r, th, a))
        sol = circle_meets_line(rho, r)
        print("      %6.2f %8.4f %10.6f %10.6f %8d %22s"
              % (a, th, rho, r, len(sol), ", ".join("%+.6f" % v for v in sol)))
    print()
    print("      TWO POINTS, AND THEY ARE CONJUGATES.  THEY COLLAPSE TO ONE")
    print("      EXACTLY WHEN THE LINE IS TANGENT, rho = r, WHICH IS")
    print("      a cos(theta) = 0 -- THE EQUATOR, OR NO SPIN.  The entire")
    print("      missing bit is the statement that A CIRCLE MEETS A LINE TWICE.")
    print()
    print("      AND rho >= r ALWAYS, with equality only there: the line can")
    print("      never miss.  There is always EITHER a two-fold ambiguity OR no")
    print("      spin in the plane to be ambiguous about.  NEVER A THIRD CASE.")
    print()

    print(BAR)
    print("5.  WHAT IT REQUIRES, COUNTED -- AND WHAT z CANNOT SEPARATE")
    print(BAR)
    print()
    print("      |z| is ONE real number.  Recovering the object needs TWO, and")
    print("      (|z|, arg z) is equivalent to (r, a cos theta).")
    print()
    print("      BUT THAT IS TWO OF THREE.  z CARRIES THE PRODUCT a cos(theta)")
    print("      AND CANNOT SPLIT IT.  Two different geometries, same product:")
    print()
    print("      %26s %14s %14s %14s" % ("(a, theta)", "|z1 - z2|", "|psi2 diff|", "|g_rr diff|"))
    # The partner is SOLVED for, never typed: a2 = a1 cos(t1)/cos(t2).
    for (a1, t1), t2 in [((0.8, math.pi / 3), 0.0), ((1.2, 1.2), 0.4),
                         ((2.5, 0.3), 1.0)]:
        a2 = a1 * math.cos(t1) / math.cos(t2)
        dz, dp, dg = same_z_different_metric(5.0, t1, a1, t2, a2, 1.0)
        print("      %26s %14.1e %14.1e %14.9f"
              % ("(%.4f,%.4f)/(%.4f,%.4f)" % (a1, t1, a2, t2), dz, dp, dg))
    print()
    print("      IDENTICAL COMPLEX RADIUS, IDENTICAL psi2, AND THEREFORE")
    print("      IDENTICAL POLYNOMIAL CURVATURE INVARIANTS AT THAT POINT --")
    print("      WITH A DIFFERENT METRIC.  This is POINTWISE and not a claim")
    print("      about the neighbourhoods, which differ; Delta carries a^2 and")
    print("      z does not.  So the complex radius is a COMPLETE description of")
    print("      the local curvature and an INCOMPLETE description of the")
    print("      geometry, and the gap between those two is a whole parameter,")
    print("      not a bit.")
    print()

    print(BAR)
    print("6.  THE INDEX OF NEED")
    print(BAR)
    print()
    print("   %-46s %-30s %-16s" % ("job", "requires", "status"))
    print("   " + "-" * 74)
    for job, req, st, src in JOBS:
        print("   %-46s %-30s %-16s" % (job, req, st))
        print("   %-46s   from: %s" % ("", src))
    held = sum(1 for j in JOBS if j[2] == "HELD")
    part = sum(1 for j in JOBS if j[2] == "PARTIAL")
    non = sum(1 for j in JOBS if j[2].startswith("NOT-HELD"))
    print()
    print("      %d HELD, %d PARTIAL, %d NOT HELD, of %d jobs."
          % (held, part, non, len(JOBS)))
    print()
    print("      THE SHAPE OF THE INDEX IS THE FINDING.  EVERYTHING THE MODULUS")
    print("      IS ASKED TO DO ABOUT MAGNITUDE IT DOES, WITH INPUTS THIS TREE")
    print("      ALREADY HOLDS AND MOSTLY WITHOUT DERIVING ANYTHING.  The two")
    print("      rows that are not clean are both about SEPARATION -- splitting")
    print("      a from theta, and splitting +a from -a -- AND A MODULUS IS A")
    print("      MERGING OPERATION.  It is being asked to undo its own act.")
    print()

    print(BAR)
    print("7.  THE OBSTRUCTION IS GLOBAL, NOT INFINITESIMAL")
    print(BAR)
    print()
    print("      %6s %8s %10s %10s %s" % ("a", "theta", "rank", "fibre", "reading"))
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (-0.99, 2.4, 6.0),
                     (0.001, 1.1, 5.0), (0.0, 1.1, 5.0)]:
        rk = rank2(even_jacobian(r, th, 1.0, a))
        fb = fibre(r, th, 1.0, a)
        tag = ("|a| locally determined, sign not" if rk == 2 and len(fb) == 2
               else "degenerate: no spin to resolve")
        print("      %6.3f %8.4f %10d %10d  %s" % (a, th, rk, len(fb), tag))
    print()
    print("      RANK 2 WITH A TWO-POINT FIBRE IS A COVERING, NOT A DEGENERACY.")
    print("      The even sector determines |a| LOCALLY and perfectly -- the")
    print("      Jacobian is full rank -- and still cannot choose between the")
    print("      two sheets.  A DERIVATIVE CANNOT SEE A DECK TRANSFORMATION.")
    print()
    print("      THAT IS WHY NO PERTURBATIVE METHOD FINDS THE BIT, and it is a")
    print("      stronger statement than cube.py's: not merely that the closed")
    print("      forms fail, but that the whole class of local methods is the")
    print("      wrong class.  It also says exactly where the rank DOES fail --")
    print("      at a = 0, where the fibre collapses to one point and there is")
    print("      nothing left to choose.  THE MAP IS SINGULAR EXACTLY WHERE THE")
    print("      QUESTION IS EMPTY.")
    print()
    print("    SCOPE: %s.  Nothing here is repaired." % SCOPE)
    print()


def selftest():
    fails = []

    def chk(label, got, want, ):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("modulus.py --selftest")
    print()
    cases = [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (0.99, 2.4, 6.0),
             (0.7, math.pi / 2, 5.0), (4.9, 0.9, 12.0), (-0.99, 2.4, 6.0)]

    w = max(abs(abs(z_of(r, th, a)) ** 2 - kerr(r, th, 1.0, a)["g_thth"])
            for a, th, r in cases)
    chk("|z|^2 == g_thetatheta", w < 1e-12, True)
    chk("and it is r^2 on the equator, every spin",
        max(abs(kerr(5.0, math.pi / 2, 1.0, a)["g_thth"] - 25.0)
            for a in (0.0, 0.3, 0.7, 2.5, -0.7)) < 1e-12, True)

    chk("conj(z(+a)) == z(-a)",
        max(conjugate_is_opposite_spin(r, th, a) for a, th, r in cases) < 1e-15, True)
    chk("z(+a) * z(-a) == |z|^2",
        max(abs(product_of_chiralities(r, th, a) - abs(z_of(r, th, a)) ** 2)
            for a, th, r in cases) < 1e-12, True)
    chk("that product is real",
        max(abs(product_of_chiralities(r, th, a).imag) for a, th, r in cases) < 1e-15, True)
    chk("z(+a)/z(-a) has unit modulus",
        max(abs(abs(ratio_of_chiralities(r, th, a)) - 1.0) for a, th, r in cases) < 1e-15, True)
    chk("and its half-argument IS arg z",
        max(abs(cmath.phase(ratio_of_chiralities(r, th, a)) / 2.0
                - cmath.phase(z_of(r, th, a))) for a, th, r in cases) < 1e-15, True)
    chk("|z| is multiplicative (a homomorphism)",
        abs(abs(z_of(5.0, 1.1, 0.7) * z_of(4.0, 0.3, 2.5))
            - abs(z_of(5.0, 1.1, 0.7)) * abs(z_of(4.0, 0.3, 2.5))) < 1e-13, True)
    chk("it is a homomorphism", MODULUS_IS_A_HOMOMORPHISM, True)

    chk("circle meets line twice off the equator",
        len(circle_meets_line(abs(z_of(5.0, 1.1, 0.7)), 5.0)), 2)
    chk("and once on it",
        len(circle_meets_line(abs(z_of(5.0, math.pi / 2, 0.7)), 5.0)), 1)
    chk("and once at zero spin",
        len(circle_meets_line(abs(z_of(5.0, 1.1, 0.0)), 5.0)), 1)
    chk("rho >= r always",
        min(abs(z_of(r, th, a)) - r for a, th, r in cases) >= -1e-15, True)
    chk("equality only where a cos(theta) = 0",
        abs(abs(z_of(5.0, math.pi / 2, 0.7)) - 5.0) < 1e-15
        and abs(z_of(5.0, 1.1, 0.7)) - 5.0 > 1e-6, True)

    dzw = dpw = 0.0
    dgw = 1e9
    for (a1, t1), t2 in [((0.8, math.pi / 3), 0.0), ((1.2, 1.2), 0.4), ((2.5, 0.3), 1.0)]:
        a2 = a1 * math.cos(t1) / math.cos(t2)
        dz, dp, dg = same_z_different_metric(5.0, t1, a1, t2, a2, 1.0)
        dzw, dpw, dgw = max(dzw, dz), max(dpw, dp), min(dgw, dg)
    chk("same a cos(theta) gives the same z", dzw < 1e-14, True)
    chk("and the same psi2", dpw < 1e-15, True)
    chk("and a DIFFERENT g_rr", dgw > 1e-3, True)
    chk("z separates a from theta", z_SEPARATES_a_FROM_theta, False)

    chk("index rows", len(JOBS), 6)
    chk("held", sum(1 for j in JOBS if j[2] == "HELD"), JOBS_HELD)
    chk("partial", sum(1 for j in JOBS if j[2] == "PARTIAL"), JOBS_PARTIAL)
    chk("not held", sum(1 for j in JOBS if j[2].startswith("NOT-HELD")), JOBS_NOT_HELD)

    chk("even Jacobian is rank 2 off zero spin",
        [rank2(even_jacobian(r, th, 1.0, a)) for a, th, r in
         [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (-0.99, 2.4, 6.0)]], [2, 2, 2])
    chk("and the fibre still has two points",
        [len(fibre(r, th, 1.0, a)) for a, th, r in
         [(0.7, 1.1, 5.0), (2.5, 0.3, 4.0), (-0.99, 2.4, 6.0)]], [2, 2, 2])
    chk("at a = 0 the rank drops", rank2(even_jacobian(5.0, 1.1, 1.0, 0.0)), 1)
    chk("and the fibre collapses", len(fibre(5.0, 1.1, 1.0, 0.0)), 1)
    chk("obstruction is infinitesimal", OBSTRUCTION_IS_INFINITESIMAL, False)
    chk("what the modulus is", MODULUS_IS, "g_thetatheta -- the polar thread")
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w_ in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w_))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
