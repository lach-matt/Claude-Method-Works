"""
typefour.py -- the objection that survives, and it is not about how much.

nullbound.py removed the standing objection: the 10^62 kg came from a timelike
quantum inequality bounding a null quantity, and on the null-smeared condition
the wall thickness cancels.  designpoint.py spent that -- 1.5e9 universes became
18.8 Earth masses.  The obvious question is what objection replaces it.

    IT IS HAWKING-ELLIS TYPE IV, AND IT IS UNTOUCHED BY EVERY WORD OF THAT,
    BECAUSE IT IS NOT A CLAIM ABOUT THE MAGNITUDE OF T_mu_nu.  IT IS A CLAIM
    ABOUT ITS ALGEBRA.

A stress-energy tensor is classified by the eigenvalue structure of T^mu_nu.
Type I is diagonalisable with a timelike eigenvector: it has a REST FRAME, and
every substance anyone has ever handled is Type I -- ordinary matter, fields,
and the Casimir vacuum included.  Type II is the defective null case: radiation,
null dust, Le's photon-rocket exterior.  Type IV has a COMPLEX EIGENVALUE PAIR,
which means there is no observer, anywhere, for whom it has a rest frame.

    NOTHING KNOWN IS TYPE IV.

-- THE MEASUREMENT ------------------------------------------------------------
The Alcubierre stress-energy is computed here from scratch: the metric on a grid,
finite-differenced to Christoffels, differenced again to Riemann, contracted to
Ricci and Einstein, divided by 8 pi.  Then the characteristic polynomial by
Faddeev-LeVerrier and its roots by Durand-Kerner, in complex arithmetic.  No
linear-algebra library and no classification assumed.

VALIDATED TWICE, because a doubly-differenced metric is exactly the kind of
pipeline that returns confident nonsense:

  * VACUUM.  ||T|| is 2.2e-6 at the bubble centre, 2.5e-8 at r = 2, and exactly
    0 at r = 3, where the metric is flat.  That is the noise floor, and it is
    six orders below every signal below.
  * THE CLOSED FORM.  T^00 for the Eulerian observer must equal BBV Eq (3.48),
    which twist.py holds independently as -Omega^2/(8 pi G).  It does, to 1e-6
    relative at five off-axis points, and returns 5e-9 on the axis where the
    closed form is exactly zero.

-- THE RESULT -----------------------------------------------------------------
At v_s = 0.5 c, every point tested in and around the wall:

        (x, y)        ||T||      |Im| / ||T||     type
        (0.60, 0.00)  0.00612       0.1435        IV
        (0.90, 0.00)  0.22317       0.2215        IV
        (0.90, 0.30)  0.15909       0.6425        IV
        (1.00, 0.00)  0.25482       0.3123        IV
        (1.00, 0.20)  0.28861       0.2585        IV
        (1.05, 0.40)  0.12612       0.5398        IV
        (1.20, 0.30)  0.01897       0.6937        IV

The imaginary parts are not marginal -- they are fourteen to sixty-nine per cent
of the tensor's own norm -- and they are STABLE TO SIX FIGURES as h changes by a
factor of four, which noise is not.  Seven of seven.  This reproduces the
classification Le's Table 1 states for the Alcubierre class, by an independent
route.

-- WHY nullbound.py DOES NOT REACH IT -----------------------------------------
Every energy condition -- NEC, WEC, DEC, ANEC, the quantum inequalities, the
SNEC, the QNEC -- is an inequality on a CONTRACTION of T_mu_nu with some vector.
Type IV is a statement about the tensor's eigenvectors.  You can make the
contractions as small as you like and the eigenvalues stay complex.  The two
questions are orthogonal, and this project spent its whole history on the first.

    THE OLD OBJECTION WAS "YOU NEED MORE ENERGY THAN EXISTS".  THAT IS GONE.
    THE OBJECTION THAT REPLACES IT IS "THE THING YOU NEED HAS NO REST FRAME",
    AND IT IS THE HARDER OF THE TWO.

-- AND IT EXPOSES THE REAL SHAPE OF THE PROBLEM, WHICH IS A TRADE -------------
Two architectures, and each has exactly one of the two properties:

        ALCUBIERRE CLASS   budget now tractable (18.8 Earth masses)
                           matter is TYPE IV -- no rest frame, unknown to physics
        WARPSHELL          matter is TYPE I, dominant-energy, observer-robust
                           l >= 2 unstable while self-gravitating (wall.py)

    NEITHER HAS BOTH, AND THE TWO OBSTRUCTIONS ARE UNRELATED.  That is a cleaner
    statement of where warp drive stands than "it needs 10^62 kg", and it is the
    first time this project has been able to say what the actual choice is.

The route out of Type IV is known and is not free: stop prescribing the metric.
Le's worldtube-first construction installs interpretable matter region by region
and gets Type I -- and lands squarely on the other obstruction.  BBV make the
same point as methodology: reading off whatever stress-energy a chosen metric
returns "can manufacture sources with no interpretation as physical matter".
Type IV is what that sentence looks like when it is measured.

-- WHAT IS NOT CLAIMED --------------------------------------------------------
That Type IV is impossible.  It is unknown, which is a weaker statement and an
honest one; no theorem forbids it, and the Hawking-Ellis classification is a
taxonomy rather than a law.  What is claimed is that it is the objection now
standing, that it is untouched by the energy-condition work, and that no
substance in the catalogue answers to it.

stdlib only.  twist.py supplies the independent closed form for validation.
"""
import cmath, math, sys

VS = 0.5
SIGMA = 8.0
RADIUS = 1.0
H = 2.0e-4

def shape(rs):
    return ((math.tanh(SIGMA * (rs + RADIUS)) - math.tanh(SIGMA * (rs - RADIUS)))
            / (2.0 * math.tanh(SIGMA * RADIUS)))

def metric(p, vs=VS):
    x, y, z = p
    v = vs * shape(math.sqrt(x * x + y * y + z * z))
    m = [[0.0] * 4 for _ in range(4)]
    m[0][0] = -1.0 + v * v
    m[0][1] = m[1][0] = -v
    m[1][1] = m[2][2] = m[3][3] = 1.0
    return m

def inverse(m):
    n = len(m)
    a = [r[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, r in enumerate(m)]
    for c in range(n):
        pr = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[pr] = a[pr], a[c]
        d = a[c][c]
        a[c] = [v / d for v in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                fa = a[r][c]
                a[r] = [u - fa * w for u, w in zip(a[r], a[c])]
    return [r[n:] for r in a]

def _shift(p, i, d):
    q = list(p)
    if i > 0:
        q[i - 1] += d
    return tuple(q)

def d_metric(p, mu, vs=VS, h=H):
    """The configuration is static in these coordinates, so d_t g = 0."""
    if mu == 0:
        return [[0.0] * 4 for _ in range(4)]
    a, b = metric(_shift(p, mu, h), vs), metric(_shift(p, mu, -h), vs)
    return [[(a[i][j] - b[i][j]) / (2.0 * h) for j in range(4)] for i in range(4)]

def christoffel(p, vs=VS, h=H):
    gi = inverse(metric(p, vs))
    d = [d_metric(p, m, vs, h) for m in range(4)]
    G = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                G[a][b][c] = 0.5 * sum(gi[a][e] * (d[b][e][c] + d[c][b][e] - d[e][b][c])
                                       for e in range(4))
    return G

def d_christoffel(p, mu, vs=VS, h=H):
    if mu == 0:
        return [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    A, B = christoffel(_shift(p, mu, h), vs, h), christoffel(_shift(p, mu, -h), vs, h)
    return [[[(A[a][b][c] - B[a][b][c]) / (2.0 * h) for c in range(4)]
             for b in range(4)] for a in range(4)]

def stress_mixed(p, vs=VS, h=H):
    """T^mu_nu = G^mu_nu/(8 pi), all the way from the metric."""
    G = christoffel(p, vs, h)
    dG = [d_christoffel(p, m, vs, h) for m in range(4)]
    Ric = [[0.0] * 4 for _ in range(4)]
    for b in range(4):
        for d in range(4):
            s = 0.0
            for a in range(4):
                s += dG[a][a][d][b] - dG[d][a][a][b]
                for e in range(4):
                    s += G[a][a][e] * G[e][d][b] - G[a][d][e] * G[e][a][b]
            Ric[b][d] = s
    gm = metric(p, vs)
    gi = inverse(gm)
    Rs = sum(gi[b][d] * Ric[b][d] for b in range(4) for d in range(4))
    Gd = [[Ric[b][d] - 0.5 * gm[b][d] * Rs for d in range(4)] for b in range(4)]
    return [[sum(gi[m][a] * Gd[a][n] for a in range(4)) / (8.0 * math.pi)
             for n in range(4)] for m in range(4)], gi

def eulerian_density(p, vs=VS, h=H):
    """T^00 for the unit normal.  Must equal BBV Eq (3.48)."""
    T, gi = stress_mixed(p, vs, h)
    return sum(gi[0][n] * T[0][n] for n in range(4))

def char_poly(A):
    """Faddeev-LeVerrier."""
    n = 4
    c = [1.0]
    Mk = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        if k > 1:
            Mk = [[sum(A[i][t] * Mk[t][j] for t in range(n)) + (c[-1] if i == j else 0.0)
                   for j in range(n)] for i in range(n)]
        AM = [[sum(A[i][t] * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        c.append(-sum(AM[i][i] for i in range(n)) / k)
    return c

def roots(c, iters=600):
    """Durand-Kerner, quartic."""
    a = [complex(x) for x in c]
    rs = [complex(0.4, 0.9) ** k for k in range(4)]
    for _ in range(iters):
        new = []
        for i, r in enumerate(rs):
            num = ((a[0] * r + a[1]) * r + a[2]) * r * r + a[3] * r + a[4]
            den = a[0]
            for j, s in enumerate(rs):
                if i != j:
                    den *= (r - s)
            new.append(r - num / den)
        rs = new
    return rs

def frobenius(T):
    return math.sqrt(sum(T[i][j] ** 2 for i in range(4) for j in range(4)))

def classify(p, vs=VS, h=H, thresh=1e-3):
    """Returns (||T||, max|Im|, ratio, type).  Type IV iff a complex pair
    survives against the tensor's own norm."""
    T, _gi = stress_mixed(p, vs, h)
    n = frobenius(T)
    im = max(abs(r.imag) for r in roots(char_poly(T)))
    ratio = im / n if n > 1e-12 else 0.0
    return n, im, ratio, ("IV" if ratio > thresh else "I/II")

def is_type_iv(p, vs=VS, h=H):
    return classify(p, vs, h)[3] == "IV"

WALL_POINTS = [(0.60, 0.00), (0.90, 0.00), (0.90, 0.30), (1.00, 0.00),
               (1.00, 0.20), (1.05, 0.40), (1.20, 0.30)]
VACUUM_POINTS = [(0.0, 0.0), (2.0, 0.0), (3.0, 0.0)]

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("VALIDATION 1 -- vacuum, where T must vanish: the noise floor")
    for p in VACUUM_POINTS:
        n = frobenius(stress_mixed((p[0], p[1], 0.0))[0])
        print("      %-12s ||T|| = %.3e" % (str(p), n))
        chk("  below 1e-5 at %s" % str(p), n < 1e-5, True)

    print("\nVALIDATION 2 -- against twist.py's independent closed form")
    import twist
    for (x, y) in ((0.9, 0.3), (1.0, 0.2), (1.2, 0.3)):
        a = eulerian_density((x, y, 0.0))
        b = twist.energy_density_bbv(x, y, 0.0, VS)
        chk("  T^00 vs BBV Eq (3.48) at (%.1f,%.1f)" % (x, y), abs(a / b - 1.0), 0.0, 2e-5)
    chk("  and it is zero on the axis", abs(eulerian_density((0.9, 0.0, 0.0))), 0.0, 1e-7)

    print("\nTHE RESULT -- every wall point is Type IV")
    print("      %-14s %10s %14s %8s" % ("(x,y)", "||T||", "|Im|/||T||", "type"))
    ivs = 0
    for (x, y) in WALL_POINTS:
        n, _im, r, t = classify((x, y, 0.0))
        print("      (%5.2f,%5.2f) %10.5f %14.4f %8s" % (x, y, n, r, t))
        ivs += (t == "IV")
    chk("wall points classified Type IV", ivs, len(WALL_POINTS))
    chk("  and none is marginal: worst ratio",
        min(classify((x, y, 0.0))[2] for x, y in WALL_POINTS) > 0.1, True)

    print("\nAnd the complex pair is stable in h, which noise is not")
    for (x, y) in ((0.9, 0.3), (1.0, 0.2)):
        vals = [classify((x, y, 0.0), h=hh)[1] for hh in (4e-4, 2e-4, 1e-4)]
        spread = (max(vals) - min(vals)) / max(vals)
        print("      (%.1f,%.1f) |Im| = %s" % (x, y, ", ".join("%.6e" % v for v in vals)))
        chk("  stable to six figures at (%.1f,%.1f)" % (x, y), spread, 0.0, 1e-5)

    print("\nWhy the energy-condition work does not reach it")
    import nullbound
    chk("nullbound bounds a CONTRACTION, and it passes", nullbound.ratio_closed(0.1) < 1.0, True)
    chk("  while the eigenvalues stay complex regardless",
        is_type_iv((0.9, 0.3, 0.0)), True)
    print("""      every energy condition is an inequality on T_mu_nu contracted with
      some vector; Type IV is a statement about its eigenvectors.  Orthogonal.""")

    print("\nThe trade this exposes")
    import wall
    chk("Alcubierre: budget tractable, matter Type IV",
        is_type_iv((1.0, 0.2, 0.0)), True)
    chk("warpshell: matter Type I, but l>=2 unstable while self-gravitating",
        wall.efoldings(1.0e6, 10.0, 0.2, 9.80665) > 100.0, True)
    print("      neither architecture has both, and the obstructions are unrelated.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE MEASUREMENT (v_s = %.1f c)\n" % VS)
    print("  %-14s %12s %14s %8s" % ("(x,y)", "||T||", "|Im|/||T||", "type"))
    for (x, y) in WALL_POINTS:
        n, _i, r, t = classify((x, y, 0.0))
        print("  (%5.2f,%5.2f) %12.5f %14.4f %8s" % (x, y, n, r, t))
    print("\n  noise floor, at vacuum points:")
    for p in VACUUM_POINTS:
        print("    %-12s ||T|| = %.3e" % (str(p), frobenius(stress_mixed((p[0], p[1], 0.0))[0])))
    print("\nVERDICT")
    print("  The objection that replaces 'more energy than exists' is 'no rest")
    print("  frame'.  It is untouched by every energy condition, because those")
    print("  bound contractions and this is about eigenvectors.  And it splits")
    print("  the field cleanly: the Alcubierre class has a tractable budget and")
    print("  impossible matter; the warpshell has possible matter and an l >= 2")
    print("  instability.  Neither has both.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
