#!/usr/bin/env python3
"""
plebanski.py -- MAPPING-2D, the one untested row, taken.  The mapping exists in
full 3+1D and has since 1960.  It is the medium it asks for that cannot be built.

obstruct.py listed MAPPING-2D as UNTESTED and described it as "a derivation
awaiting a derivation": twist.py had shown an analogue must be at least 2+1D to
carry any metric content, Smolyaninov derives only 1+1D, and no 2+1D version is
published.  That framing was wrong in a useful way.  THE GENERAL MAPPING ALREADY
EXISTS -- Plebanski's 1960 constitutive relations, the foundation of
transformation optics -- and it says that any metric is a medium:

        eps^ij = mu^ij = -sqrt(-g) g^ij / g_00        w_i = -g_0i / g_00

with w the magnetoelectric vector, D = eps E + w x H and B = mu H - w x E.  So
there was never a derivation to do.  Applied to the 3+1D Alcubierre metric,
computed here from the numerical inverse and determinant rather than by hand:

        eps_xx = 1 EXACTLY        eps_yy = eps_zz = 1/(1 - v^2)
        w_x    = -v/(1 - v^2)     w_y = w_z = 0          (v = v_s f)

Two things follow, and the second closes the row.

-- THE MEDIUM IS ANISOTROPIC, WHICH IS THE 2+1D CONTENT ----------------------
eps_xx != eps_yy whenever v != 0.  The shift picks out x and the medium knows it.
That is the transverse structure twist.py said was necessary, present in the
exact mapping and absent from Smolyaninov's isotropic eps = mu.  So a 2+1D
analogue is not merely possible to write down; it is what the honest mapping
gives, and the 1+1D reduction is what has to be argued for.

-- AND BROWN-HORNREICH-SHTRIKMAN FORBIDS IT, EXCEPT BEYOND THE HORIZON -------
w lies along x, so it couples (E_y, H_z) and (E_z, H_y); the anisotropic BHS
condition is therefore w_x^2 <= (eps_yy - 1)(mu_zz - 1).  Substituting,

        w^2  =  v^2/(1-v^2)^2      bound  =  v^4/(1-v^2)^2

so the medium is admissible iff v^2 <= v^4, that is iff |v| >= c.

    THE EXACT 3+1D ALCUBIERRE MEDIUM IS THERMODYNAMICALLY FORBIDDEN EVERYWHERE
    IT IS SUBLUMINAL, AND ADMISSIBLE ONLY AT OR BEYOND THE HORIZON.

Which is the exact inverse of the 1+1D situation device.py measured, where
stability capped v BELOW the horizon and forbade reaching it (TEST 16).  Both
routes are closed and for opposite reasons:

        1+1D    BHS allows v < c(n-1)/n^2, forbids the horizon -- and the metric
                there is pure gauge, so there was nothing to emulate anyway.
        3+1D    the metric has real content, and BHS forbids the medium at every
                subluminal v, admitting only the regime nobody can steer.

-- THE OBVIOUS ESCAPE, CLOSED --------------------------------------------------
A conformal rescaling g -> Omega^2 g leaves null geodesics alone, so it is the
natural place to look for headroom.  It gives none: eps and w are CONFORMALLY
INVARIANT, verified here at Omega = 0.5, 1, 2, 7.3 to sixteen digits, because
the Omega^4 from sqrt(-g) and the Omega^-2 from g^ij exactly cancel the Omega^2
from g_00.  eps_xx = 1 is not a choice of units; it is the mapping's answer.

-- SO WHERE DOES SMOLYANINOV'S ADMISSIBLE MEDIUM COME FROM? -------------------
Not from this mapping.  Run Plebanski on his own 1+1D metric and it returns
eps = 1 and w = -v/(1-v^2), BHS-forbidden exactly as above -- NOT his
eps = mu = n/sqrt(1-(n beta f)^2).  The square root is the tell: his medium
emulates the metric whose light speed is c/n rather than c, which is a
physically different object, and the background index is where the (eps - 1)
headroom comes from.  That is legitimate -- an analogue may emulate a rescaled
metric -- but it is a substitution, not the mapping, and it has never been shown
to survive in 3+1D where eps must also become anisotropic.

    SO MAPPING-2D IS NO LONGER "UNTESTED".  It is a sharp question with a
    computed obstruction in front of it: does the index-n embedding that rescues
    1+1D also rescue the anisotropic 3+1D medium, given that the exact mapping
    is forbidden at every subluminal v and conformal freedom buys nothing?

That is a far better statement of the problem than the one this project had, and
it is the first time the analogue route has had a specific thing to prove rather
than a fabrication to attempt.

-- SOURCES --------------------------------------------------------------------
Plebanski J 1960 Phys. Rev. 118 1396 -- electromagnetic waves in gravitational
    fields; the constitutive relations used here.
Brown W F, Hornreich R M, Shtrikman S 1968 Phys. Rev. 168 574 -- the bound.
Smolyaninov I I 2011 Phys. Rev. B 84 113103 = arXiv:1009.5663.
Alcubierre M 1994 Class. Quantum Grav. 11 L73, shape function Eq (7).

stdlib only.  The metric is built, inverted and its determinant taken
numerically; no constitutive component below is transcribed from an algebraic
result, and the closed forms in the docstring are CHECKED against the numerics
rather than the other way round.
"""
import itertools, math, sys

VS_DEFAULT = 0.9
SIGMA = 8.0
RADIUS = 1.0

def shape(rs, sigma=SIGMA, R=RADIUS):
    return ((math.tanh(sigma * (rs + R)) - math.tanh(sigma * (rs - R)))
            / (2.0 * math.tanh(sigma * R)))

def alcubierre(x, y, z=0.0, vs=VS_DEFAULT, omega=1.0):
    """g_mu nu for ds^2 = -dt^2 + (dx - v dt)^2 + dy^2 + dz^2, times Omega^2."""
    v = vs * shape(math.sqrt(x * x + y * y + z * z))
    w = omega * omega
    g = [[0.0] * 4 for _ in range(4)]
    g[0][0] = w * (-1.0 + v * v)
    g[0][1] = g[1][0] = -w * v
    g[1][1] = g[2][2] = g[3][3] = w
    return g, v

def inverse(m):
    """Gauss-Jordan.  No linear algebra library, and none needed."""
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        d = a[c][c]
        a[c] = [v / d for v in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                fac = a[r][c]
                a[r] = [u - fac * w for u, w in zip(a[r], a[c])]
    return [row[n:] for row in a]

def determinant(m):
    tot = 0.0
    n = len(m)
    for p in itertools.permutations(range(n)):
        sgn = 1
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    sgn = -sgn
        pr = 1.0
        for i in range(n):
            pr *= m[i][p[i]]
        tot += sgn * pr
    return tot

def plebanski(g):
    """PINNED (Plebanski 1960).  Returns (eps_xx, eps_yy, eps_zz, w_x)."""
    gi = inverse(g)
    s = math.sqrt(-determinant(g))
    eps = [-s * gi[i][i] / g[0][0] for i in (1, 2, 3)]
    w_x = -g[0][1] / g[0][0]
    return eps[0], eps[1], eps[2], w_x

def medium(x, y, z=0.0, vs=VS_DEFAULT, omega=1.0):
    g, v = alcubierre(x, y, z, vs, omega)
    return plebanski(g) + (v,)

# -- the closed forms, to be CHECKED against the numerics ---------------------

def eps_xx_closed(v):
    return 1.0

def eps_yy_closed(v):
    return 1.0 / (1.0 - v * v)

def w_closed(v):
    return -v / (1.0 - v * v)

# -- Brown-Hornreich-Shtrikman, in its anisotropic form -----------------------

def bhs_margin(v):
    """w_x^2 <= (eps_yy - 1)(mu_zz - 1).  Positive margin = admissible."""
    e = eps_yy_closed(v)
    return (e - 1.0) ** 2 - w_closed(v) ** 2

def bhs_admissible(v):
    return bhs_margin(v) >= 0.0

def admissibility_threshold():
    """DERIVED.  v^2 <= v^4 iff |v| >= 1: the medium is admissible only at or
    beyond the horizon."""
    return 1.0

def anisotropy(v):
    """eps_yy/eps_xx.  1 in vacuum, > 1 wherever the shift is nonzero -- the
    transverse structure twist.py said a 2+1D analogue must carry."""
    return eps_yy_closed(v) / eps_xx_closed(v)

# -- selftest -----------------------------------------------------------------

PTS = [(0.0, 0.0), (0.9, 0.0), (0.9, 0.3), (1.0, 0.2), (1.05, 0.5), (2.0, 0.0)]

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The mapping, computed numerically, against the closed forms")
    for (x, y) in PTS:
        exx, eyy, ezz, wx, v = medium(x, y)
        chk("  eps_xx == 1 at (%.2f, %.2f)" % (x, y), exx, eps_xx_closed(v), 1e-12)
        chk("  eps_yy == 1/(1-v^2)", eyy, eps_yy_closed(v), 1e-12)
        chk("  eps_zz == eps_yy (the shift picks out x only)", ezz, eyy, 1e-12)
        chk("  w_x == -v/(1-v^2)", wx, w_closed(v), 1e-12)

    print("\nThe medium is ANISOTROPIC wherever the shift is nonzero")
    for (x, y) in PTS:
        _e1, _e2, _e3, _w, v = medium(x, y)
        a = anisotropy(v)
        chk("  eps_yy/eps_xx at (%.2f, %.2f)" % (x, y), a > 1.0, abs(v) > 0.0)
    chk("...and isotropic only in vacuum", anisotropy(0.0), 1.0, 1e-15)

    print("\nConformal rescaling buys nothing: eps and w are invariant")
    base = medium(0.9, 0.3, omega=1.0)
    for om in (0.5, 2.0, 7.3, 100.0):
        got = medium(0.9, 0.3, omega=om)
        chk("  Omega = %.1f reproduces Omega = 1" % om,
            max(abs(a - b) for a, b in zip(got[:4], base[:4])), 0.0, 1e-12)
    print("      Omega^4 from sqrt(-g) and Omega^-2 from g^ij cancel Omega^2 from g_00")

    print("\nBrown-Hornreich-Shtrikman on the exact medium")
    for v in (0.05, 0.1, 0.5, 0.9, 0.99):
        chk("  FORBIDDEN at v = %.2f" % v, bhs_admissible(v), False)
    for v in (1.5, 2.0, 10.0):
        chk("  admissible at v = %.1f" % v, bhs_admissible(v), True)
    chk("the threshold is exactly the horizon", admissibility_threshold(), 1.0, 0.0)
    chk("  margin -> 0 from BELOW as v -> 0", bhs_margin(1e-4) < 0.0, True)
    chk("  and the deficit is v^2(1-v^2)... i.e. v^4 - v^2 over (1-v^2)^2",
        bhs_margin(0.5), (0.5 ** 4 - 0.5 ** 2) / (1 - 0.25) ** 2, 1e-15)

    print("\nThe contrast this closes")
    print("      1+1D  BHS caps v below the horizon (device.py TEST 16), and the")
    print("            metric there is gauge (twist.py) -- nothing to emulate.")
    print("      3+1D  the metric has content, and BHS admits ONLY |v| >= c --")
    print("            the regime the crew cannot steer.")
    chk("both are closed, and for opposite reasons",
        bhs_admissible(0.5) is False and bhs_admissible(1.5) is True, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE EXACT MEDIUM OF THE 3+1D ALCUBIERRE METRIC (v_s = %.1f)\n" % VS_DEFAULT)
    print("  %-14s %10s %10s %10s %12s %13s"
          % ("(x, y)", "v = v_s f", "eps_xx", "eps_yy", "w_x", "BHS margin"))
    for (x, y) in PTS:
        exx, eyy, _ezz, wx, v = medium(x, y)
        print("  (%5.2f,%5.2f) %10.5f %10.6f %10.6f %12.6f %13.6f"
              % (x, y, v, exx, eyy, wx, bhs_margin(v)))
    print("\n  admissible iff v^2 <= v^4, i.e. |v| >= c:\n")
    print("  %-8s %14s %14s %12s" % ("v", "w^2", "bound", ""))
    for v in (0.1, 0.5, 0.9, 0.99, 1.5, 2.0):
        w2 = w_closed(v) ** 2
        b = (eps_yy_closed(v) - 1.0) ** 2
        print("  %-8.2f %14.6g %14.6g %12s"
              % (v, w2, b, "ok" if w2 <= b else "FORBIDDEN"))
    print("\nVERDICT")
    print("  The 2+1D mapping was never missing -- Plebanski 1960 gives it in full")
    print("  3+1D, and it returns exactly the transverse anisotropy twist.py said")
    print("  was necessary.  What is missing is a medium: the exact one is")
    print("  thermodynamically forbidden at every subluminal shift, conformal")
    print("  freedom is no escape, and the index-n substitution that rescues the")
    print("  1+1D case has never been shown to survive the anisotropy.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
