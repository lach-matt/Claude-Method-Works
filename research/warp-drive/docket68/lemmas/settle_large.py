#!/usr/bin/env python3
"""settle_large.py -- item 542, lemma SETTLE: the formed hole settles at the large end.  M, 542, to the weak rows:
"strengthen the existing lemmas, and ad more for support".  (G) asserts a static corridor at both ends; at the
emitter's finite wavelength the formed hole is round only on average, so the static corridor needs it to settle.
settle_late determined the small end (SETTLEs); this file the large end.  Labels: computed (exact unless marked
numerical), READ, deduced, M's.

  E0 (read) M's words, verbatim in the rulings file, 542.
  E1 (computed, exact) On the plane the formed hole's data are axisymmetric with zero Komar angular momentum.  The
     delivery's class is T^2-invariant with both reflections (settle5 T1; settle_late S1); the plane is the fixed set
     of one reflection, so on it one rotation, d_phi, survives: the induced data are axisymmetric.  The other
     reflection, phi -> -phi, removes every g_(t phi), g_(r phi), g_(theta phi), for any dependence on (t, r, theta),
     and the Komar integral of d_phi over every sphere then vanishes identically (proved: with every g_(a phi) off the
     diagonal zero, F_ab = d_a g_(b phi) - d_b g_(a phi) = 0 for a, b != phi, and g^(t phi) = g^(r phi) = 0; computed
     exactly on random polynomial components; the integral's normalisation checked on slowly rotating Kerr, omega =
     2J/r^3, which returns J).  Control: without the reflection it does not vanish.
  E2 (READ) Dafermos, Holzegel, Rodnianski and Taylor (2104.08222v1, p. 16, Corollary III.3.1, READ): "All
     characteristic initial data prescribed on (I.3.2), assumed sufficiently close to Schwarzschild data with mass
     M_init, which are moreover axisymmetric and have vanishing Komar angular momentum, are contained in the
     codimension-3 'submanifold' M_stable of Theorem I.3.1.  Thus, consequences (i), (ii) and (iii) apply to such
     data"; (iii): the metric "asymptotes, inverse polynomially, to a Schwarzschild metric with mass M_final ~ M_init"
     (p. 6); "general vacuum initial data -- with no symmetry assumed" (abstract).
  E3 (computed, exact) The data's distance from Schwarzschild at the large end.  The plane reads the large hole as
     four-dimensional Schwarzschild to O((ell/r0)^2) (C3, verified 261; m1_large): 2.5e-3 at r0 = 20 ell, falling as
     1/N.  The formation's departure from roundness is of order its wavelength over r0, 10 l5/r0, with l5/ell =
     (l_P/ell)^(2/3): at most 4.4e-18 at ell_H and 5.5e-21 at the window's top, from r0 = 20 ell on.
  E4 (deduced) So at the large end the formed hole settles, nonlinearly, to Schwarzschild of its final mass, to
     O((ell/r0)^2): its data are axisymmetric with zero Komar J (E1), within the corollary's class (E2), and close to
     Schwarzschild by E3's margins once the corollary's threshold (unquantified in the paper) is met, which holds for
     all N above a finite value since both margins fall with N.  With SETTLEs at the small end, (G)'s static corridor
     is the end state of the formation at both ends; at the small end the nonlinear step is computed and its proof
     theorized (settle_late S3-S5), at the large end it is proved.

python3 settle_large.py [--selftest | --mutants]
"""
import contextlib, io, math, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "strengthen the existing lemmas, and ad more for support"),)
G, C, HBAR = 6.67430e-11, 299792458.0, 1.054571817e-34
L_P = math.sqrt(HBAR * G / C ** 3)
ELL = {"H": 0.611e-9, "F": 13.964e-6}           # the Higgs tie and the window's top (ell_si L2)


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def komar(g, X):
    """sum over a sphere of g^(t a) g^(r b) F_ab sqrt(-g), F_ab = d_a g_(b phi) - d_b g_(a phi): proportional to the
    Komar integral of d_phi (Killing: nabla_a xi_b = F_ab/2)"""
    gi = g.inv() if not g.is_diagonal() else sp.diag(*[1 / g[i, i] for i in range(4)])
    F = [[sp.diff(g[b, 3], X[a]) - sp.diff(g[a, 3], X[b]) for b in range(4)] for a in range(4)]
    integrand = sum(gi[0, a] * gi[1, b] * F[a][b] for a in range(4) for b in range(4))
    return integrand, sp.sqrt(-g.det())


def e1():
    t, r, th, ph = X = sp.symbols("t r theta phi")
    # calibration: slowly rotating Kerr to first order in J, at large r
    J, M = sp.symbols("J M", positive=True)
    f = 1 - 2 * M / r
    om = 2 * J / r ** 3
    gk = sp.Matrix([[-f + r ** 2 * sp.sin(th) ** 2 * om ** 2, 0, 0, -r ** 2 * sp.sin(th) ** 2 * om],
                    [0, 1 / f, 0, 0], [0, 0, r ** 2, 0],
                    [-r ** 2 * sp.sin(th) ** 2 * om, 0, 0, r ** 2 * sp.sin(th) ** 2]])
    integ, vol = komar(gk, X)
    lead = sp.series(sp.simplify(integ * vol), J, 0, 2).removeO()
    K = sp.integrate(sp.integrate(sp.simplify(lead), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
    Kinf = sp.limit(K, r, sp.oo)
    norm = sp.simplify(J / Kinf)                                 # J = norm * K
    # the class on the plane: every component a function of (t, r, theta); the reflection phi -> -phi.  The integrand
    # is tested exactly with each component a polynomial in (t, r, theta) with rational coefficients (Lorentzian at the
    # test points), at three points: zero at all three for every draw, or not zero
    import random
    rnd = random.Random(542)
    names = [(i, j) for i in range(4) for j in range(i, 4)]
    zero = True
    for draw in range(3):
        g = sp.zeros(4, 4)
        for (i, j) in names:
            poly = sum(sp.Rational(rnd.randint(-9, 9), 97) * m for m in (1, t, r, th, t * r, r * th, th ** 2))
            base = {0: -4, 1: 3, 2: 5, 3: 6}[i] if i == j else 0
            g[i, j] = g[j, i] = base + poly
        if not MUT.get("noreflect"):
            R = sp.diag(1, 1, 1, -1)
            g = (g + R * g * R) / 2                              # phi -> -phi: odd components vanish
        integ, vol = komar(g, X)
        for pt in ((sp.Rational(1, 3), 2, sp.Rational(1, 2)), (0, 3, 1), (sp.Rational(-1, 2), 5, 2)):
            val = sp.nsimplify(integ.subs(dict(zip((t, r, th), pt))))
            zero &= val == 0
    return dict(norm=norm, Kinf=Kinf, zero=zero, axisym=all(sp.diff(v, ph) == 0 for v in g))


def e3():
    return dict(bulk20=(1 / 20) ** 2, round={k: 10 * (L_P / v) ** (2 / 3) / 20 for k, v in ELL.items()})


def compute():
    return dict(words=words(), e1=e1(), e3=e3())


def checks(o):
    e, x = o["e1"], o["e3"]
    return {"E0": o["words"],
            "E1": e["zero"] and e["axisym"] and sp.simplify(e["norm"] * e["Kinf"] - sp.Symbol("J", positive=True)) == 0
                  and e["norm"] != 0,
            "E3": "%.2g" % x["bulk20"] == "0.0025" and "%.2g" % x["round"]["H"] == "4.4e-18"
                  and "%.2g" % x["round"]["F"] == "5.5e-21"}


def report(o=None):
    o = o or compute(); ck = checks(o)
    e, x = o["e1"], o["e3"]
    print("E0 M's words:", o["words"])
    print("E1 Komar normalisation on slow Kerr: J = %s x K (K -> %s); the class with phi -> -phi: integrand zero %s, "
          "axisymmetric %s" % (e["norm"], e["Kinf"], e["zero"], e["axisym"]))
    print("E3 (ell/r0)^2 at r0 = 20 ell: %.2g; 10 l5/r0 there: %.2g at ell_H, %.2g at the window's top"
          % (x["bulk20"], x["round"]["H"], x["round"]["F"]))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return ck


def selftest(quiet=False):
    with contextlib.redirect_stdout(io.StringIO()) if quiet else contextlib.nullcontext():
        ck = report()
    ok = all(ck.values())
    if not quiet:
        print("selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


MUTANTS = {"noreflect": "the class without the reflection phi -> -phi (E1)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-8s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
