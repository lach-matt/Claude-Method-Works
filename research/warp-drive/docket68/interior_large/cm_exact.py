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

    def roots(self, gtt, gpp):
        """every (r, xc), 0 <= xc <= x1, with the given norms: g_tautau gives 1 + xc r = mu sqrt((1 - mu/r)/g_tautau),
        so xc is a function of r and one equation in r remains; scanned in log r on both sides of the horizon, each
        sign change refined by brentq"""
        from scipy.optimize import brentq
        def xcr(r):
            a = (1 - self.mu / r) / gtt
            return (self.mu * np.sqrt(a) - 1) / r if a > 0 else np.nan
        def res(r):
            xc = xcr(r)
            return 4 * r ** 2 * self.G(xc) / (self.P1 ** 2 * (1 + xc * r) ** 2) / gpp - 1 if np.isfinite(xc) else np.nan
        side = np.geomspace(1e-6, 1 - 1e-12, 4000) if gtt < 0 else np.geomspace(1 + 1e-12, 1e4, 4000)
        rs = self.mu * side; v = np.array([res(r) for r in rs]); out = []
        for i in range(len(rs) - 1):
            if np.isfinite(v[i]) and np.isfinite(v[i + 1]) and v[i] * v[i + 1] < 0:
                r = brentq(res, rs[i], rs[i + 1], xtol=1e-15, rtol=1e-14); xc = xcr(r)
                if -1e-9 <= xc <= self.x1 + 1e-9:
                    out.append((r, xc))
        return out

    def invert(self, gtt, gpp, r0, xc0, axis=False):
        """(r, xc) with the given norms; on the axis (gpp = 0) xc = x1 and r from g_tautau alone.  Outside the horizon
        the map is two-to-one in places (g_tautau is not monotonic in r for xc > 0): every root is found (roots) and
        the one nearest the guess, in (log r, xc), is taken, so a continuation from a known point stays on its branch;
        (nan, nan) when the norms have no exact preimage"""
        if not axis:
            rts = self.roots(gtt, gpp)
            if not rts:
                return float("nan"), float("nan")
            return min(rts, key=lambda q: (np.log(q[0] / r0)) ** 2 + (q[1] - xc0) ** 2)
        if axis:
            q = fsolve(lambda v: [self.norms(np.exp(v[0]), self.x1)[0] / gtt - 1], [np.log(r0)], xtol=1e-14)
            return float(np.exp(q[0])), self.x1

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
    r, xc = E.chart(0.519, 0.794); gt, gp = E.norms(r, xc); rts = E.roots(gt, gp)    # a two-root exterior point
    r2, xc2 = E.invert(gt, gp, r * 1.02, xc + 0.01); n += 1
    ok += len(rts) == 2 and abs(r2 / r - 1) < 1e-9 and abs(xc2 - xc) < 1e-9 and min(q[0] for q in rts) < 0.8 * r
    print("two preimages at (s 0.519, x 0.794): %s; the branch kept %.5f, %.5f" % (
        ", ".join("(%.5f, %.5f)" % q for q in rts), r2, xc2))
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
