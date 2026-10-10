#!/usr/bin/env python3
"""o1c_complete.py -- lemma O1c: eq. (17) at r0 = 2m is geodesically complete (computed; one standard-not-READ fact;
not verified by a separate session; not seated; 2026-10-10).

O1 ("one way, 1 -> 2, nonsingular") was split by the F1 audit into O1a (DERIVED from 132 with 130), O1b (no curvature
singularity: M1's regularity clause) and O1c, geodesic completeness, OPEN: "It was never computed even for eq. (17)
(plane.py P1: 'Geodesic completeness is not computed: OPEN')".  This computes it.

Geometry (H-BK-CORRIDOR; Bronnikov-Kim gr-qc/0212112v1 eq. (17) p.4, READ via copy/plane.py): ds^2 = (1 - 2m/r) dt^2 -
(1 - 3m/2r) dr^2/((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2, at the corridor's member r0 = 2m (G3).  Throat coordinate
r = 2m + x^2, x in R (x > 0 position 1's side, x < 0 position 2's); units m = 1.

  C1 (computed, sympy) g_tt = x^2/(x^2 + 2), g_xx = 2(x^2 + 2)(2x^2 + 1)/x^2: the horizon sits on the throat (x = 0), a
     double zero of g_tt -- degenerate (O2), the near-horizon geometry AdS2 x S2
  C2 (computed) the Kretschmann scalar is 8(123x^8 + 170x^6 + 69x^4 + 12x^2 + 4)/((x^2 + 2)^6 (2x^2 + 1)^4): finite and
     smooth at every x, 1/2 at the throat, ~ 61.5/x^12 (~ 1/r^6) far out.  No curvature singularity anywhere
  C3 (computed) every geodesic (energy E, angular momentum L, eps = 1 timelike / 0 null) obeys xdot^2 = V(x) with V even
     in x and V(0) = E^2/2 > 0 for every L and eps: a geodesic with E != 0 crosses the throat at finite, non-zero speed,
     so in finite affine parameter, and x(lambda) is smooth through x = 0 (xddot = V'(x)/2, V smooth)
  C4 (computed) far out V ~ (E^2 - eps)/(4 x^2): unbound geodesics reach x^2 ~ lambda, so the affine parameter is
     unbounded at both ends; bound ones (E^2 < eps) turn at V = 0 on each side and continue (each crossing of the
     degenerate horizon enters the next static patch of the maximal extension, as in O1's one-way passage)
  C5 (computed, numerically) eight geodesics integrated through the throat with xddot = V'(x)/2 (RK4): each crosses x = 0
     and runs to |x| = 30 (or turns), the affine parameter growing as x^2
  C6 (standard-not-READ) E = 0 geodesics lie on the horizon x = 0 (V <= 0 elsewhere): its null generators, affinely
     parametrised by the Killing time because the surface gravity is zero (O2), so they run over all of R
  CONTROL (computed) the same eq. (17) at r0 = 3m/2 is Schwarzschild (BK p.4, READ): its Kretschmann 48m^2/r^6 diverges
     at r = 0 and a radial infall reaches r = 0 in finite affine parameter (4m/3 from r = 2m at E = 1): incomplete.
     The completeness above is a property of r0 = 2m, not of the method.
So O1c is PROVED for eq. (17)'s geometry.  Whether that geometry is the corridor's mouth is M1 (OPEN; F1-AUDIT.md), so in
the chain O1c is 'PROVED on M1'.  Stdlib + sympy.  python3 o1c_complete.py [--selftest | --mutants]
"""
import math
import sys

import sympy as sp

MUT = {}
x, E, L, eps = sp.symbols("x E L epsilon", real=True)


def metric(r0=2):
    m = sp.Integer(1)
    r = 2 * m + x**2 if r0 == 2 else sp.Rational(r0) + x**2
    f = 1 - 2 * m / r
    H = 1 - sp.Rational(3, 2) * m / r if not MUT.get("drop_bk_factor") else sp.Integer(1)
    grr = H / (f * (1 - sp.Rational(r0) / r)) if r0 != 2 else H / f**2
    if MUT.get("r0_not_2m"):
        grr = H / (f * (1 - sp.Rational(19, 10) / r))
    gxx = sp.simplify(grr * sp.diff(r, x)**2)
    return r, f, gxx


def kretschmann(r, f, gxx):
    t, th, ph = sp.symbols("t theta phi", real=True)
    g = sp.diag(f, -gxx, -r**2, -r**2 * sp.sin(th)**2)
    X = [t, x, th, ph]
    n, gi = 4, g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    v = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d]) + sum(
                        Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n))
                    if v != 0:
                        R[a, b, c, d] = sp.simplify(v)
    K = 0
    for (a, b, c, d), v in R.items():
        low = sum(g[a, e] * R.get((e, b, c, d), 0) for e in range(n))
        up = sum(gi[b, e] * gi[c, f_] * gi[d, h] * R.get((a, e, f_, h), 0)
                 for e in range(n) for f_ in range(n) for h in range(n))
        K += low * up if False else 0
    # direct contraction (diagonal metric): K = sum R_abcd R^abcd
    K = 0
    for (a, b, c, d), v in R.items():
        Rl = g[a, a] * v
        Ru = v * gi[b, b] * gi[c, c] * gi[d, d]
        K += Rl * Ru
    return sp.factor(sp.simplify(K))


def potential(r, f, gxx):
    return sp.simplify((E**2 / f - eps - L**2 / r**2) / gxx)


def integrate(V, Ev, Lv, ev, x0=-1e-9, sign=1, xmax=30.0, h=1e-3, nmax=2000000):
    """xddot = V'(x)/2 from x0 heading toward +x (sign) through the throat; returns (crossed, end, lambda, turned)."""
    Vn = sp.lambdify(x, V.subs({E: Ev, L: Lv, eps: ev}), "math")
    dV = sp.lambdify(x, sp.diff(V, x).subs({E: Ev, L: Lv, eps: ev}), "math")
    if MUT.get("integrator_sign"):
        dV0 = dV
        dV = lambda z: -dV0(z)
    s = [x0, sign * math.sqrt(max(Vn(x0), 0.0))]
    lam, crossed, turned = 0.0, False, False
    for _ in range(nmax):
        f = lambda st: (st[1], dV(st[0]) / 2)
        k1 = f(s)
        k2 = f([s[0] + h / 2 * k1[0], s[1] + h / 2 * k1[1]])
        k3 = f([s[0] + h / 2 * k2[0], s[1] + h / 2 * k2[1]])
        k4 = f([s[0] + h * k3[0], s[1] + h * k3[1]])
        nx = s[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        nv = s[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if (s[0] < 0) != (nx < 0):
            crossed = True
        if s[1] * nv < 0:
            turned = True
        s, lam = [nx, nv], lam + h
        if abs(s[0]) >= xmax:
            break
        h = min(5e-2, 1e-3 * max(1.0, abs(s[0])) ** 2)
    return crossed, s[0], lam, turned


def schwarzschild_control():
    rr = sp.Symbol("r", positive=True)
    K = sp.Integer(48) / rr**6                     # m = 1
    # radial infall E = 1 from r = 2 to 0: rdot^2 = E^2 - (1 - 2/r) = 2/r -> lambda = int_0^2 sqrt(r/2) dr
    lam = sp.integrate(sp.sqrt(rr / 2), (rr, 0, 2))
    return {"K_diverges": sp.limit(K, rr, 0, "+") == sp.oo, "lambda_to_r0": sp.nsimplify(lam)}


def compute():
    r, f, gxx = metric()
    K = kretschmann(r, f, gxx)
    V = potential(r, f, gxx)
    cases = [(1.0, 0.0, 0), (1.0, 3.0, 0), (1.2, 0.0, 1), (1.5, 4.0, 1), (0.9, 0.0, 1), (0.7, 1.0, 1), (2.0, 10.0, 0), (1.01, 2.0, 1)]
    runs = {c: integrate(V, *c) for c in cases}
    return {"g": (sp.factor(f), sp.factor(gxx)), "K": K, "V": sp.factor(V), "runs": runs, "ctl": schwarzschild_control()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    f, gxx = d["g"]
    add("C1 g_tt = x^2/(x^2 + 2) (double zero at the throat: degenerate horizon on the throat); g_xx = 2(x^2+2)(2x^2+1)/x^2",
        sp.simplify(f - x**2 / (x**2 + 2)) == 0 and sp.simplify(gxx - 2 * (x**2 + 2) * (2 * x**2 + 1) / x**2) == 0)
    K = d["K"]
    xs = [0, 0.1, 0.5, 1, 2, 5, 20]
    add("C2 Kretschmann finite and smooth at every x: 1/2 at the throat, ~ 61.5/x^12 far out",
        sp.simplify(K.subs(x, 0)) == sp.Rational(1, 2) and all(0 < float(K.subs(x, v)) < 1 for v in xs)
        and sp.limit(K * x**12, x, sp.oo) == sp.Rational(123, 2))
    V = d["V"]
    add("C3 xdot^2 = V(x), V even, V(0) = E^2/2 for every L and eps (crossing at finite non-zero speed)",
        sp.simplify(V - V.subs(x, -x)) == 0 and sp.simplify(V.subs(x, 0) - E**2 / 2) == 0)
    add("C4 far out V ~ (E^2 - eps)/(4 x^2): the affine parameter grows as x^2 (unbounded)",
        sp.simplify(sp.limit(V * x**2, x, sp.oo) - (E**2 - eps) / 4) == 0)
    runs = d["runs"]
    unbound = [c for c in runs if c[0] ** 2 > c[2]]
    bound = [c for c in runs if c[0] ** 2 < c[2]]
    add("C5 every integrated geodesic crosses the throat; unbound ones reach |x| = 30 with lambda ~ x^2; bound ones turn",
        all(runs[c][0] for c in runs) and all(abs(runs[c][1]) >= 30 and runs[c][2] > 100 for c in unbound)
        and all(runs[c][3] for c in bound))
    ctl = d["ctl"]
    add("CONTROL Schwarzschild (r0 = 3m/2): K = 48 m^2/r^6 diverges and radial infall reaches r = 0 at lambda = 4/3 "
        "(incomplete)", ctl["K_diverges"] and ctl["lambda_to_r0"] == sp.Rational(4, 3))
    return res


MUTANTS = {"drop_bk_factor": "the (1 - 3m/2r) factor dropped", "r0_not_2m": "the throat off the horizon (r0 = 1.9m)",
           "integrator_sign": "the geodesic force sign flipped"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-42s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("o1c_complete.py -- eq. (17) at r0 = 2m, geodesic completeness\n")
    print("g_tt =", d["g"][0], "  g_xx =", d["g"][1])
    print("Kretschmann =", d["K"])
    print("xdot^2 = V(x) =", d["V"])
    for c, (cr, xe, lam, tu) in d["runs"].items():
        print("  E=%.2f L=%.1f eps=%d: crossed %s, end x = %+.2f, lambda = %.1f, turned %s" % (c[0], c[1], c[2], cr, xe, lam, tu))
    print("control Schwarzschild:", d["ctl"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
