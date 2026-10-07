#!/usr/bin/env python3
"""bulkseries.py -- wall C, second piece: the local bulk off the corridor, computed order by order.

localbulk.py L4 proved that a local vacuum bulk exists in which the corridor (Bronnikov-Kim eq. (17) at r0 = 2m) is a
Randall-Sundrum plane with K = -g/ell, unique among analytic solutions.  This computes it.  Gaussian normal gauge,
ds^2 = dy^2 - A dt^2 + B dr^2 + C dOmega^2 (staticity and spherical symmetry are inherited, L4), with the evolution
equations, for each diagonal component h of the induced metric,

    (1/2) d^2h/dy^2 = R_mumu[h] + (dh/dy)^2/(2h) - (K/2) dh/dy + (4/ell^2) h,   K = sum of (1/2) d ln|h|/dy,

from R_mu nu(5) = R_mu nu[h] - dK_mu nu/dy + 2 K_mu a K^a_nu - K K_mu nu = -(4/ell^2) h_mu nu (checked on RS itself and
on the dS slicing of AdS5).  Data at y = 0: h = eq. (17), dh/dy = -2h/ell.  Each order is explicit.

  owner: closedbulk.py's seated build() (imported, never copied) builds the same series for any member; the fast solver
      here must agree with it through y^4 on the corridor (r0 = 2m), and does
  B1  control: Schwarzschild data give the black string, C = r^2 e^{-2y/ell} exactly, at every computed order
  B2  the corridor's series reproduces Maartens-Koyama eq. (148) at the throat: in g~ = e^{2y/ell} g,
      C~ = 4m^2 + y^2 + 2y^3/ell (throatbulk.py T6, imported)
  B3  the constraints propagate: the Gauss (yy) and Codazzi (yr) constraints vanish order by order off the plane -- the
      Bianchi lemma of localbulk L4, checked rather than cited (through y^7 at ell = r0, y^8 in the flat limit)
  B4  the next orders at the throat (m = 1, r0 = 2): C~ = 4 + y^2 + 2y^3/ell + (ell^2 + 28) y^4/(12 ell^2)
      + (ell^2 + 6) y^5/(3 ell^3) + (3 ell^4 + 260 ell^2 + 496) y^6/(360 ell^4) + ...   (--order 6, ~8 min)
      ell = r0:   4 + y^2 + y^3 + 2y^4/3 + 5y^5/12 + 11y^6/40 + 79y^7/420 + 2603y^8/20160   (--inv-ell 1/2 --order 8, ~16 min)
      flat limit: 4 + y^2 + y^4/12 + y^6/120 + 23y^8/20160 + 37y^10/259200   (--flat --order 10, ~13 min)
  B5  the radius of convergence at the throat, by the ratio test (an estimate from the last terms, not a bound; and a
      radius of this representation, not where the bulk ends): at ell = r0 the ratios settle at 0.684, 0.686 per order,
      a radius of ~1.46m = 0.73 r0; in the flat limit the ratios in (y/r0)^2 run 0.33, 0.40, 0.55, 0.50, a radius of
      ~1.4 r0.  So the reach is of order r0 and, at ell = r0, below it
Imports closedbulk.py and throatbulk.py by path.  Stdlib + sympy.
python3 bulkseries.py [--selftest] [--order N] [--flat | --inv-ell 1/2]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)

r, ell, y = sp.symbols("r ell y", positive=True)
M1 = sp.Integer(1)                                                  # units m = 1, so r0 = 2


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def _cz(e):
    return sp.cancel(sp.together(e))


class Series:
    """A power series in y truncated at order N, coefficients rational in r and ell."""

    def __init__(self, c, N):
        self.N = N
        c = [_cz(x) for x in c][:N + 1]
        self.c = c + [sp.Integer(0)] * (N + 1 - len(c))

    def _lift(self, o):
        return o if isinstance(o, Series) else Series([o], self.N)

    def __add__(self, o):
        o = self._lift(o)
        return Series([a + b for a, b in zip(self.c, o.c)], self.N)

    __radd__ = __add__

    def __neg__(self):
        return Series([-a for a in self.c], self.N)

    def __sub__(self, o):
        return self + (-self._lift(o))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, Series):
            return Series([a * o for a in self.c], self.N)
        return Series([sum(self.c[i] * o.c[k - i] for i in range(k + 1)) for k in range(self.N + 1)], self.N)

    __rmul__ = __mul__

    def inv(self):
        a0 = self.c[0]
        out = [1 / a0]
        for k in range(1, self.N + 1):
            out.append(_cz(-sum(self.c[i] * out[k - i] for i in range(1, k + 1)) / a0))
        return Series(out, self.N)

    def __truediv__(self, o):
        return self * (o.inv() if isinstance(o, Series) else 1 / sp.sympify(o))

    def dr(self):
        return Series([sp.diff(a, r) for a in self.c], self.N)

    def dy(self):
        return Series([(k + 1) * self.c[k + 1] for k in range(self.N)] + [0], self.N)


def ricci(A, B, C):
    """R_tt, R_rr, R_thth of -A dt^2 + B dr^2 + C dOmega^2 (r-derivatives only; y is a parameter)."""
    A1, B1, C1, A2, C2 = A.dr(), B.dr(), C.dr(), A.dr().dr(), C.dr().dr()
    Rtt = A2 / (B * 2) - A1 * B1 / (B * B * 4) - A1 * A1 / (A * B * 4) + A1 * C1 / (B * C * 2)
    Rrr = (-A2 / (A * 2) + A1 * A1 / (A * A * 4) + A1 * B1 / (A * B * 4) - C2 / C + C1 * C1 / (C * C * 2)
           + B1 * C1 / (B * C * 2))
    Rth = 1 - C2 / (B * 2) + B1 * C1 / (B * B * 4) - A1 * C1 / (A * B * 4)
    return {"A": Rtt, "B": Rrr, "C": Rth}


def ricci_check():
    """The closed forms above against a direct computation from the metric."""
    t, th, ph = sp.symbols("t theta phi")
    Af, Bf, Cf = [sp.Function(n)(r) for n in "ABC"]
    g = sp.diag(-Af, Bf, Cf, Cf * sp.sin(th) ** 2)
    X = [t, r, th, ph]
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = [sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) - sp.diff(Gam[a][b][a], X[b])
                           + sum(Gam[a][a][d] * Gam[d][b][b] - Gam[a][b][d] * Gam[d][b][a] for d in range(4))
                           for a in range(4))) for b in range(3)]
    A1, B1, C1, A2, C2 = [sp.diff(f, r, k) for f, k in ((Af, 1), (Bf, 1), (Cf, 1), (Af, 2), (Cf, 2))]
    closed = [A2 / (2 * Bf) - A1 * B1 / (4 * Bf**2) - A1**2 / (4 * Af * Bf) + A1 * C1 / (2 * Bf * Cf),
              -A2 / (2 * Af) + A1**2 / (4 * Af**2) + A1 * B1 / (4 * Af * Bf) - C2 / Cf + C1**2 / (2 * Cf**2)
              + B1 * C1 / (2 * Bf * Cf),
              1 - C2 / (2 * Bf) + B1 * C1 / (4 * Bf**2) - A1 * C1 / (4 * Af * Bf)]
    return all(sp.simplify(a - b) == 0 for a, b in zip(Ric, closed))


def solve(F0, H0, N, e=None):
    """The series through y^N; e = 1/ell (default symbolic; 0 is the flat-bulk limit, K = 0, Lambda5 = 0)."""
    e = 1 / ell if e is None else e
    co = {"A": [F0, -2 * F0 * e], "B": [1 / H0, -2 * e / H0], "C": [r**2, -2 * r**2 * e]}
    for k in range(N - 1):
        S = {X: Series(co[X], N) for X in "ABC"}
        h = {"A": -S["A"], "B": S["B"], "C": S["C"]}
        kk = {X: h[X].dy() / (h[X] * 2) for X in "ABC"}
        Ktr = kk["A"] + kk["B"] + kk["C"] * 2
        R = ricci(S["A"], S["B"], S["C"])
        for X in "ABC":
            hp = h[X].dy()
            rhs = R[X] + hp * hp / (h[X] * 2) - Ktr * hp * sp.Rational(1, 2) + h[X] * (4 * e**2)
            val = _cz(2 * rhs.c[k] / ((k + 2) * (k + 1)))
            co[X].append(_cz(-val) if X == "A" else val)
    return co


def constraints(co, N, e=None):
    e = 1 / ell if e is None else e
    S = {X: Series(co[X], N) for X in "ABC"}
    h = {"A": -S["A"], "B": S["B"], "C": S["C"]}
    kk = {X: h[X].dy() / (h[X] * 2) for X in "ABC"}
    Ktr = kk["A"] + kk["B"] + kk["C"] * 2
    KK = kk["A"] * kk["A"] + kk["B"] * kk["B"] + kk["C"] * kk["C"] * 2
    R = ricci(S["A"], S["B"], S["C"])
    R4 = R["A"] / h["A"] + R["B"] / h["B"] + R["C"] / h["C"] * 2
    gauss = R4 - (Ktr * Ktr - KK - 12 * e**2)
    codazzi = (S["A"].dr() / (S["A"] * 2) * (kk["B"] - kk["A"]) + S["C"].dr() / S["C"] * (kk["B"] - kk["C"])
               - kk["A"].dr() - kk["C"].dr() * 2)
    # the evolution at order k fixes h_{k+2}; the constraints are then exact through order N - 2
    return [sp.simplify(x) == 0 for x in gauss.c[:N - 1]], [sp.simplify(x) == 0 for x in codazzi.c[:N - 1]]


def throat(co, N, e=None):
    e = 1 / ell if e is None else e
    Ct = sp.series(sp.exp(2 * y * e) * sum(c * y**k for k, c in enumerate(co["C"])), y, 0, N + 1).removeO()
    return [sp.factor(sp.limit(Ct.coeff(y, k), r, 2 * M1)) for k in range(N + 1)]


def owner_build(order=4):
    """closedbulk.py's seated build() (imported, never copied) on the corridor, m = 1, r0 = 2: the series through y^order
    and its constraints, the second path the fast solver must agree with."""
    cb = _load(os.path.join(HERE, "closedbulk.py"), "bs_closedbulk")
    E = cb.field_equations()
    x, a = E["x"], E["a"]
    F = 1 - 2 / x
    res = cb.build(F, (1 - sp.Rational(3, 2) / x) / F**2, x**2, order=order)
    coeffs = [[sp.sympify(c).subs({x: r, a: 1 / ell}) for c in cl] for cl in res["coeffs"]]
    return coeffs, res["constraints"]


def compute(N=4, flat=False, inv_ell=None):
    """inv_ell: a fixed rational 1/ell (m = 1), e.g. 1/2 for ell = r0; flat: ell -> infinity.  Either skips the
    symbolic-ell checks."""
    F = 1 - 2 * M1 / r
    H = (1 - 2 * M1 / r) ** 2 / (1 - sp.Rational(3, 2) * M1 / r)
    e = sp.Integer(0) if flat else (sp.Rational(inv_ell) if inv_ell is not None else None)
    corr = solve(F, H, N, e)
    g_ok, c_ok = constraints(corr, N, e)
    d = {"N": N, "flat": flat, "inv_ell": e, "gauss_ok": g_ok, "codazzi_ok": c_ok, "throat": throat(corr, N, e)}
    if e is not None:
        return d
    schw = solve(F, F, N)
    own, own_con = owner_build(min(N, 4))
    tb = _load(os.path.join(HERE, "throatbulk.py"), "bs_throatbulk")
    gt0 = tb.t6()["g_tilde"]
    yt = [s for s in gt0.free_symbols if s.name == "y"][0]
    d.update({"ricci_ok": ricci_check(),
              "schw_ok": all(sp.simplify(schw["C"][k] - r**2 * (-2 / ell) ** k / sp.factorial(k)) == 0
                             for k in range(N + 1)),
              "owner_agrees": all(sp.simplify(own[i][k] - corr[X][k]) == 0 for i, X in enumerate("ABC")
                                  for k in range(min(N, 4) + 1)),
              "owner_constraints": own_con,
              "mk148": sp.expand(gt0.subs({yt: y, tb.m: M1, tb.ell: ell}))})
    return d


def report(d):
    tag = (" -- flat-bulk limit, ell -> infinity" if d["flat"] else
           (" -- 1/ell = %s" % d["inv_ell"] if d["inv_ell"] is not None else ""))
    print("bulkseries.py -- wall C: the local bulk off the corridor, order by order (m = 1, r0 = 2)%s\n" % tag)
    if d["inv_ell"] is None:
        print("closed-form 4D Ricci checked against a direct computation: %s" % d["ricci_ok"])
        print("agrees with closedbulk.py's seated build() through y^%d: %s (owner's constraints %s)"
              % (min(d["N"], 4), d["owner_agrees"], d["owner_constraints"]))
        print("B1 control, Schwarzschild data -> black string C = r^2 e^{-2y/ell} through order %d: %s"
              % (d["N"], d["schw_ok"]))
        print("B2 MK eq. 148 at the throat (throatbulk T6): C~ = %s" % d["mk148"])
    print("B3 constraints vanish order by order: Gauss %s, Codazzi %s" % (d["gauss_ok"], d["codazzi_ok"]))
    print("B4 C~ at the throat, coefficients of y^0..y^%d: %s" % (d["N"], d["throat"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute(4)
    th = d["throat"]
    chk("the closed-form 4D Ricci components agree with a direct computation", d["ricci_ok"])
    chk("the fast solver agrees with closedbulk.py's seated build() through y^4, and the owner's constraints vanish",
        d["owner_agrees"] and all(v == 0 for vl in d["owner_constraints"].values() for v in vl))
    chk("B1 control: Schwarzschild data give the black string, C = r^2 e^{-2y/ell}, through y^4", d["schw_ok"])
    chk("B2: the corridor's series reproduces MK eq. 148 at the throat, C~ = 4 + y^2 + 2y^3/ell",
        sp.expand(sum(th[k] * y**k for k in range(4)) - d["mk148"]) == 0)
    chk("B3: the Gauss and Codazzi constraints vanish order by order off the plane (through y^2)",
        all(d["gauss_ok"]) and all(d["codazzi_ok"]))
    chk("B4: the y^4 coefficient at the throat is (ell^2 + 28)/(12 ell^2)",
        sp.simplify(th[4] - (ell**2 + 28) / (12 * ell**2)) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    order = int(sys.argv[sys.argv.index("--order") + 1]) if "--order" in sys.argv else 4
    inv = sys.argv[sys.argv.index("--inv-ell") + 1] if "--inv-ell" in sys.argv else None
    report(compute(order, flat="--flat" in sys.argv, inv_ell=inv))
