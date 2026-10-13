"""The exact AdS4 C-metric brane hole (gen_eqs_cm.py) as a yardstick: given the two Killing norms of a computed metric,
g_tautau = mu^2 (1 - mu/r)/(1 + xc r)^2 and g_psipsi = 4 r^2 G(xc)/(P1^2 (1 + xc r)^2) (tau of period 4 pi, psi of
period 2 pi, both fixed by regularity, so both norms are invariants), recover the exact point (r, xc) and the exact
Kretschmann scalar there, K = 24 + 12 mu^2 (1 + xc r)^6/r^6 (checked against the generated expression at the exact
chart by --selftest).  The singularity is r = 0, the horizon r = mu, the brane xc = 0, the axis xc = x1."""
import numpy as np, pickle, sys
from fractions import Fraction
from scipy.optimize import fsolve

class Exact:
    def __init__(self, tag):
        m = pickle.load(open("eqs_%s.pkl" % tag, "rb"))["meta"]
        self.x1, self.mu, self.P1 = (float(Fraction(m[k])) for k in ("x1", "mu", "P1"))
        self.ca, self.cb = float(Fraction(m.get("ca", "0"))), float(Fraction(m.get("cb", "0")))

    def G(self, xc):
        return 1 - xc ** 2 - self.mu * xc ** 3

    def norms(self, r, xc):
        u = 1 + xc * r
        return self.mu ** 2 * (1 - self.mu / r) / u ** 2, 4 * r ** 2 * self.G(xc) / (self.P1 ** 2 * u ** 2)

    def K(self, r, xc):
        return 24 + 12 * self.mu ** 2 * (1 + xc * r) ** 6 / r ** 6

    def invert(self, gtt, gpp, r0, xc0, axis=False):
        """(r, xc) with the given norms; on the axis (gpp = 0) xc = x1 and r from g_tautau alone.  Outside the horizon
        the map is two-to-one in places (g_tautau is not monotonic in r for xc > 0), so the guess must be near"""
        if axis:
            q = fsolve(lambda v: [self.norms(np.exp(v[0]), self.x1)[0] / gtt - 1], [np.log(r0)], xtol=1e-14)
            return float(np.exp(q[0])), self.x1
        def res(v):
            t, p = self.norms(np.exp(v[0]), v[1])
            return [t / gtt - 1, p / gpp - 1]
        q, info, ier, msg = fsolve(res, [np.log(r0), xc0], xtol=1e-14, full_output=True)
        return float(np.exp(q[0])), float(q[1])

    def chart(self, s, x):
        """the exact chart's point (a = b = 0): r = mu/(1 - s), xc = x1 (1 - x^2)"""
        return self.mu / (1 - s), self.x1 * (1 - x ** 2)

    def tau_total(self, xc, n=4000):
        """proper time from the horizon to r = 0 along the exact chart's normal at fixed xc (Gauss-Chebyshev in r)"""
        th = (np.arange(n) + 0.5) * np.pi / (2 * n); r = self.mu * np.sin(th) ** 2
        # integral of dr/((1 + xc r) sqrt(mu/r - 1)) with r = mu sin^2 th: 2 mu sin^2 th/(1 + xc r) dth
        return float(np.sum(2 * self.mu * np.sin(th) ** 2 / (1 + xc * r)) * np.pi / (2 * n))

def selftest():
    import os
    os.environ.setdefault("PROB", "cm23a0b0")
    import sympy as sp, core_fw as C
    E = Exact(os.environ["PROB"]); ok = 0; n = 0
    assert abs(E.mu - 15 / 8) < 1e-15 and abs(E.P1 - 23 / 6) < 1e-15 and abs(E.G(E.x1)) < 1e-15
    raw = pickle.load(open("kretsch_%s.pkl" % os.environ["PROB"], "rb"))
    Kx0 = sp.lambdify([C.s, C.x, C.bt] + C.VARS, C.ev(raw), "numpy")
    Kx = lambda s, x, *a: Kx0(s, x, 0.0, *a)                          # eps = 0: the exact chart
    ex = [1.0] + [0.0] * 5
    args = ex * 4 + [0.0] * 6                                          # T, S, A, B = 1, F = 0, no derivatives
    for s in (0.5, 0.2, -0.3, -1.0, -3.0):
        for x in (0.2, 0.5, 0.8, 1.0):
            r, xc = E.chart(s, x); k1 = float(Kx(s, x, *args)); k2 = E.K(r, xc); n += 1
            ok += abs(k1 / k2 - 1) < 1e-10
            gt, gp = E.norms(r, xc); r2, xc2 = E.invert(gt, gp, r * 1.1, xc + 0.03)
            n += 1; ok += abs(r2 / r - 1) < 1e-9 and abs(xc2 - xc) < 1e-9
    print("exact K against the generated Kretschmann, and the inversion: %d/%d" % (ok, n))
    if True:                                                           # at eps = 0 the exact chart solves every row
        fr, fb = C.lam(C.RES), C.lam(C.BCS); worst = 0.0
        for s in (0.7, 0.3, -0.5, -2.0, -6.0):
            for x in (0.1, 0.4, 0.9):
                worst = max(worst, max(abs(float(v)) for v in fr(s, x, 0.0, *args)))
            worst = max(worst, max(abs(float(v)) for v in fb(s, 1.0, 0.0, *args)))
        print("max |E_ab|, |brane rows| at the exact chart: %.1e" % worst); n += 1; ok += worst < 1e-10
        bad = list(args); bad[2 * 6] = 1.001                              # mutant: A = 1.001
        n += 1; ok += max(abs(float(v)) for v in fr(-0.5, 0.4, 0.0, *bad)) > 1e-5
        n += 1; ok += max(abs(float(v)) for v in fr(-0.5, 0.4, 0.3, *args)) > 1e-5 or E.ca == E.cb == 0
    t0 = E.tau_total(0.0); n += 1; ok += abs(t0 - np.pi * E.mu / 2) < 1e-9
    print("tau to r = 0 on the brane: %.6f (pi mu/2 = %.6f)" % (t0, np.pi * E.mu / 2))
    # mutants: a wrong mu in K, a wrong P1 in the norms
    E2 = Exact(os.environ["PROB"]); E2.mu *= 1.001
    r, xc = E.chart(-1.0, 0.5); n += 1; ok += abs(E2.K(r, xc) / float(Kx(-1.0, 0.5, *args)) - 1) > 1e-4
    E3 = Exact(os.environ["PROB"]); E3.P1 *= 1.001; gt, gp = E3.norms(r, xc); r3, xc3 = E.invert(gt, gp, r, xc)
    n += 1; ok += abs(xc3 - xc) > 1e-5
    print("selftest: %d/%d" % (ok, n)); return ok == n

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
