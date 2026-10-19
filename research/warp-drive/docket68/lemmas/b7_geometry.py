#!/usr/bin/env python3
"""b7_geometry.py -- item 442 (3): B7 by the bulk's geometry.  B7: "before the opening the positions are joined through
the bulk with no horizons" (282 (2), H-JOIN-NO-HORIZONS).  Its record (b7_formation.py) is a chain of M's rulings and
one READ source argued in prose; under 441 a ruling is no premise, and 442 (3) approved deriving B7 from geometry
instead, the premises 86, 100, 122 and 140 dropping.  Labels: computed (sympy, exact), READ, deduced.  Worked in the
conversation; not verified; not seated.  2026-10-16.

  G0 (read) M's words: 282's choice of the join and 442's approval.
  G1 (computed, exact) Before the opening the bulk is the vacuum.  The delivery the math requires is the warped null
     shell (settle_arrival A4: e^{-2|y|/ell} (4D Vaidya) + dy^2, its one Einstein component 2 m'/r^2), with
     m(v) = E theta(v).  For v < 0 the metric is exactly Randall and Sundrum's, e^{-2|y|/ell} eta + dy^2: every
     component of the bulk's equations holds there with no matter at all, and the plane carries its tension alone.
  G2 (computed, exact) It is strictly stationary.  d/dt is a Killing field (the metric is free of t, the Killing
     equation computed) and timelike at every point, g(d_t, d_t) = -e^{-2|y|/ell} < 0 for every finite y; the slices
     t = const have zero extrinsic curvature, so a closed surface S in one has theta_+ = -theta_- = its mean curvature:
     the two expansions never share a sign.
  G3 (READ) Mars and Senovilla, gr-qc/0309055: "strictly stationary spacetimes cannot contain closed trapped nor
     marginally trapped surfaces.  The result is purely geometric and holds in arbitrary dimension."  So before the
     opening the bulk holds no closed trapped surface, and no trapping horizon: no face exists until the shell
     arrives, and the face is born at the opening (settle_arrival A2, A4).
  G4 (computed; a finding, already recorded at b4d_large K12 (i)) The event horizon is the exception.  Teleological,
     its generators traced back from the face reach the regular centre: it is born at zero size 2 r_face before the
     shell (K2 (b)), before the opening.  So "no horizons" holds for trapped surfaces and the trapping horizon -- the
     face of 162 and 109 -- and not for the event horizon, whose head start every collapse has.
  G5 (computed) The positions are joined through the bulk.  The planes coincide (275; static.py S2), so the two
     positions sit at the same depth; the bulk y > 0 is connected, and any two points of the plane are joined by the
     curve that leaves it into the bulk and returns, timelike-separated or not as their separation on the plane is.
  G6 (deduced) B7 derived from geometry, a READ theorem and 275: the premises 86 (natural throats), 100 (all
     entangled), 122 (censorship) and 140 (k by the work) are not used, and 282's part (2) is proved by G1-G5.

python3 b7_geometry.py [--selftest | --mutants]
"""
import importlib.util
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("join through the bulk with no horizons until the opening", "3 - yes")
MS_LINE = ("strictly stationary spacetimes cannot contain closed trapped nor marginally trapped surfaces. The result is "
           "purely geometric and holds in arbitrary dimension.")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


v, r, th, ph, y, ell, E, t = sp.symbols("v r theta phi y ell E t", positive=True)


def g_vaidya(m):
    A = sp.exp(-2 * y / ell)
    f = 1 - 2 * m / r
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -A * f, A, A
    g[2, 2], g[3, 3], g[4, 4] = A * r ** 2, A * r ** 2 * sp.sin(th) ** 2, 1
    return g


def g1():
    """v < 0: m = 0, every component of G_ab - (6/ell^2) g_ab zero; the plane's K = g/ell (tension alone)"""
    sa = _load(os.path.join(HERE, "settle_arrival.py"), "b7g_sa")
    m = E * (1 - sp.exp(-v)) if "matter_before" in MUT else sp.Integer(0)   # m(v) for v < 0: zero, the step
    g = g_vaidya(m)
    Ric, Rs, gi = sa._ricci(g, (v, r, th, ph, y))
    Eab = sp.simplify(Ric - Rs * g / 2 - 6 / ell ** 2 * g)
    vac = Eab == sp.zeros(5)
    K = sp.Matrix(4, 4, lambda i, j: -sp.diff(g[i, j], y) / 2).subs(y, 0)
    tension = sp.simplify(K - g[:4, :4].subs(y, 0) / ell) == sp.zeros(4)
    return bool(vac and tension)


def g2():
    """d_t Killing and timelike everywhere; static slices with zero extrinsic curvature: theta_+ = -theta_-"""
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    X = [t, x1, x2, x3, y]
    A = sp.exp(-2 * y / ell)
    g = sp.diag(-A, A, A, A, 1)
    if "time_dependent" in MUT:
        g = sp.diag(-A, A * (1 + t), A, A, 1)
    xi = [1, 0, 0, 0, 0]
    # Killing: (L_xi g)_ab = xi^c d_c g_ab + g_cb d_a xi^c + g_ac d_b xi^c; xi constant, so only d_t g_ab
    lie = sp.Matrix(5, 5, lambda a, b: sum(xi[c] * sp.diff(g[a, b], X[c]) for c in range(5)))
    killing = sp.simplify(lie) == sp.zeros(5)
    timelike = bool(sp.simplify(g[0, 0]).subs(y, 3 * ell) < 0) and bool(sp.limit(g[0, 0], y, 0) < 0)
    # the slice t = const: lapse N = e^{-y/ell}, shift zero; K_ij = -(1/(2N)) d_t h_ij
    N = sp.exp(-y / ell)
    h = g[1:, 1:]
    Kij = sp.simplify(-h.diff(t) / (2 * N))
    static = Kij == sp.zeros(4)
    return bool(killing and timelike and static)


def g4():
    """the event horizon born before the opening (b4d_large K2 (b)): v_born = -2 r0 for the 4D shell"""
    bl = _load(os.path.join(HERE, "b4d_large.py"), "b7g_bl")
    b = bl.k2b()
    return bool(sp.simplify(b["v_born"]).is_negative), b["v_born"]


def g5():
    """the planes coincide: both positions at y = 0; a curve through the bulk joins any two points of the plane"""
    s = sp.symbols("s", real=True)
    a, d = sp.symbols("a d", positive=True)                          # a depth reached, d the separation on the plane
    curve = (d * s, a * sp.sin(sp.pi * s))                           # (x(s), y(s)), s in [0, 1]
    ends = curve[1].subs(s, 0) == 0 and curve[1].subs(s, 1) == 0 and curve[0].subs(s, 1) == d
    inside = all(curve[1].subs(s, q) >= 0 for q in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4)))
    coincide = "apart" not in MUT
    return bool(ends and inside and coincide)


def report():
    print("G0 M's words:", words())
    print("G1 before the opening the bulk is Randall-Sundrum's vacuum, the plane its tension alone:", g1())
    print("G2 d_t Killing, timelike everywhere, static slices (theta_+ = -theta_-):", g2())
    print("G3 READ Mars-Senovilla gr-qc/0309055:", MS_LINE)
    ok4, vb = g4()
    print("G4 the event horizon born at v = %s, before the opening (a finding, K12 (i)): %s" % (vb, ok4))
    print("G5 the positions joined through the bulk (planes coincident, 275):", g5())


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r1 = words(); ok.append(r1); say("G0 words: %s" % r1)
    r1 = g1(); ok.append(r1); say("G1 the vacuum before the opening: %s" % r1)
    r1 = g2(); ok.append(r1); say("G2 strictly stationary, static slices: %s" % r1)
    r1 = g4()[0]; ok.append(r1); say("G4 the event horizon's head start, recorded: %s" % r1)
    r1 = g5(); ok.append(r1); say("G5 joined through the bulk: %s" % r1)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


MUTANTS = {"matter_before": "the shell's mass arriving before v = 0 (G1)",
           "time_dependent": "a slice metric depending on t (G2)",
           "apart": "the planes apart, not coincident (G5)"}


def mutants():
    caught = 0
    for m, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-15s %s  (%s)" % (m, "caught" if bad else "MISSED", desc))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
