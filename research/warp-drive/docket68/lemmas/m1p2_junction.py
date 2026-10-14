#!/usr/bin/env python3
"""m1p2_junction.py -- position 2's mass where its bulk meets ours at the corridor (203), in the flat-limit static
class: the near-horizon invariants both sides must share (Israel's first condition) fix m2 = m.  Item 211: the between
analyst's pass, strengthened by its critic (the near-horizon Ricci-flat ODE proves what the analyst sampled at 50
depths); seated under 206 with the critic's limits; 2026-10-10.

  J1 (computed, sympy) the static flat-limit bulk near the corridor's horizon, ds^2 = -a(y) x dt^2 + b(y) dx^2/x^2 +
     c(y) dOmega^2 + dy^2 (x = r - 2m -> 0), is Ricci-flat only if R_xy = 0, which forces a/b constant; then R_xx = 0
     and R_thth = 0 are exactly (c b')' = -c/2 and (b c')' = 2b, with the constraint (G_yy = 0)
     -4 b^2 c + b^2 c'^2 + b c^2 + 4 b c b' c' + c^2 b'^2 = 0
  J2 (computed) on our plane (y = 0) eq. (17) gives a = 1/2, b = 1, c = 4 (m = 1): the AdS2 radius L = 2 sqrt(b) and the
     S2 radius R = sqrt(c) are both 2m there, and the bank is even in y (b' = c' = 0); the constraint holds at y = 0
  J3 (deduced from J1, J2) for y > 0, (c b')' < 0 from b'(0) = 0 gives b' < 0, and (b c')' > 0 from c'(0) = 0 gives
     c' > 0, while b, c > 0.  So lambda = L/R = 2 sqrt(b/c) is STRICTLY decreasing in depth and R strictly increasing --
     proved, not sampled
  J4 (computed) the ODE integrated from J2's data reproduces the bank's near-horizon L and R (extrapolated to x = 0
     from its first three columns) at every depth checked up to 2.45m, keeps the constraint, and lambda falls from 1 to
     about 0.07 there
  J5 (deduced from J3; the board's reading H-OWN-BULK-SAME-FASHION) if position 2's side of the corridor is the same
     family scaled by m2 = mu m (202's record: each plane grows its own bulk from its own data), a junction crossing
     the horizon at finite depths s1 (ours, in units of m) and s2 (its, in units of m2) must match
     L: L(s1) = mu L(s2), and R: R(s1) = mu R(s2).  Their ratio gives lambda(s1) = lambda(s2), so s1 = s2 by J3 and
     mu = 1.  Every mass ratio but 1 is excluded in the class, 2 among them.  Control: mu = 1 matches at any s1 = s2,
     corridor_shape's symmetric junction
[ITEM 215 (M: 'they exist within the everything bulk index'): J5 glues our bulk to position 2's by Israel's first
condition at the corridor.  M places the two bulks as cells of the everything bulk index, not glued, so J5 stands as
computed for glued bulks and does not bind M's configuration: there the per-sheet conjunction is not refuted.  J1-J4
stand as computed.]
So the per-sheet m2 = 2m is refuted in the flat-limit static class, on H-OWN-BULK-SAME-FASHION and a finite-depth
crossing.  What it refutes is a CONJUNCTION -- H-ONE-G5's per-sheet G2 = 2 G1 read as position 2's pull and Planck-area
G (g2_between G3-G4, m1p2_cypher X3), H-PULL-PER-SIDE, 203's one E, H-OWN-BULK-SAME-FASHION and the class -- and which
member gives way is the board's call under 149, not deduced; it is not made here.  M1P2x stays OPEN: position 2's
tension still acts on crossing rays (m1x X2: a ray crossing P2 at -sigma/4 gains -(sigma/4) sin a, which needs
pairing) and in the rim's balance, and its matter is B5px's unknown -- only the mouth's bulk reading is fixed.
What this does not show: the flat limit (ell -> infinity), static, thin junction meeting the horizon at a finite depth;
the near-horizon limit taken uniform in depth (J4's agreement supports it).
Imports corridor_shape.py by path (read only).  Stdlib + sympy.  python3 m1p2_junction.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = {}
_C = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


# ================================================================================================================ J1
def ricci(g, X):
    import sympy as sp
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                      + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                                      for a in range(n)))
    return R


def j1():
    import sympy as sp
    t, x, th, ph, y = sp.symbols("t x theta phi y", positive=True)
    a, b, c = [sp.Function(nm)(y) for nm in "abc"]
    g = sp.diag(-a * x, b / x ** 2, c, c * sp.sin(th) ** 2, 1)
    R = ricci(g, [t, x, th, ph, y])
    k = sp.Symbol("k", positive=True)
    # R_xy vanishes iff (a/b)' = 0
    rxy = sp.simplify(R[1, 4])
    rxy_is_ratio = sp.simplify(rxy.subs(a, k * b).doit()) == 0
    rxy_nonzero = sp.simplify(rxy) != 0
    sub = {a: k * b}
    Rxx = sp.simplify(R[1, 1].subs(sub).doit())
    Rth = sp.simplify(R[2, 2].subs(sub).doit())
    d = sp.diff
    shift = sp.Rational(1, 2) if not MUT.get("wrong_source") else -sp.Rational(1, 2)
    e_xx = d(c * d(b, y), y) + shift * c
    e_th = d(b * d(c, y), y) - 2 * b
    # each Ricci component is a nonzero multiple of its equation
    q_xx = sp.simplify(Rxx / e_xx)
    q_th = sp.simplify(Rth / e_th)
    # constraint from G_yy (Einstein tensor) with a = k b
    Rs = sp.simplify(sum((g.inv()[i, i] * R[i, i]) for i in range(5)).subs(sub).doit())
    Gyy = sp.simplify(R[4, 4].subs(sub).doit() - Rs / 2)
    con = -4 * b ** 2 * c + b ** 2 * d(c, y) ** 2 + b * c ** 2 + 4 * b * c * d(b, y) * d(c, y) + c ** 2 * d(b, y) ** 2
    q_con = sp.simplify(Gyy / con)
    return {"rxy_ratio": rxy_is_ratio, "rxy_nonzero": rxy_nonzero, "q_xx": q_xx, "q_th": q_th,
            "xx_ok": (not q_xx.has(sp.Derivative)) and q_xx != 0, "th_ok": (not q_th.has(sp.Derivative)) and q_th != 0,
            "con_ok": (not q_con.has(sp.Derivative)) and q_con != 0}


# ============================================================================================================ J2, J4
def bank():
    if "bulk" not in _C:
        cs = _load(os.path.join(HERE, "corridor_shape.py"), "mj_cs")
        _C["bulk"] = cs.Bulk(cs.load_bank())
    return _C["bulk"]


def near_horizon(y):
    """b = lim B x^2, c = lim C, a = lim A/x, extrapolated to x = 0 from the bank's first three columns (Lagrange)"""
    bulk = bank()
    xs = [bulk.rv[i] - 2 for i in range(3)]
    vals = {"a": [], "b": [], "c": []}
    for i in range(3):
        col = bulk.col(i, y)
        vals["a"].append(col["A"][0] / xs[i])
        vals["b"].append(col["B"][0] * xs[i] ** 2)
        vals["c"].append(col["C"][0])
    out = {}
    for key, f in vals.items():
        tot = 0.0
        for i in range(3):
            w = 1.0
            for j in range(3):
                if j != i:
                    w *= (0 - xs[j]) / (xs[i] - xs[j])
            tot += w * f[i]
        out[key] = tot
    return out


def ode(ymax=2.45, h=1e-3):
    """RK4 for (c b')' = -c/2, (b c')' = 2b from b = 1, c = 4, b' = c' = 0"""
    src = 0.5 if not MUT.get("wrong_source") else -0.5

    def F(u):
        b, c, bp, cp = u
        return (bp, cp, (-src * c - bp * cp) / c, (2 * b - bp * cp) / b)
    u, y, rows = (1.0, 4.0, 0.0, 0.0), 0.0, []
    while y < ymax - 1e-12:
        k1 = F(u)
        k2 = F(tuple(u[i] + h / 2 * k1[i] for i in range(4)))
        k3 = F(tuple(u[i] + h / 2 * k2[i] for i in range(4)))
        k4 = F(tuple(u[i] + h * k3[i] for i in range(4)))
        u = tuple(u[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))
        y += h
        b, c, bp, cp = u
        rows.append((y, b, c, bp, cp, -4 * b * b * c + b * b * cp * cp + b * c * c + 4 * b * c * bp * cp + c * c * bp * bp))
    return rows


def compute():
    nh0 = near_horizon(0.0)
    rows = ode()
    checks_at = (0.25, 0.5, 1.0, 1.5, 2.0, 2.3, 2.45)
    cmp = []
    for yc in checks_at:
        r = min(rows, key=lambda q: abs(q[0] - yc))
        nb = near_horizon(yc)
        cmp.append((yc, 2 * math.sqrt(r[1]), 2 * math.sqrt(nb["b"]), math.sqrt(r[2]), math.sqrt(nb["c"])))
    return {"j1": j1(), "nh0": nh0, "rows": rows, "cmp": cmp}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    a = d["j1"]
    add("J1 the near-horizon static bulk is Ricci-flat only with a/b constant (R_xy); then R_xx and R_thth are nonzero "
        "multiples of (c b')' + c/2 and (b c')' - 2b, and G_yy of the constraint",
        a["rxy_ratio"] and a["rxy_nonzero"] and a["xx_ok"] and a["th_ok"] and a["con_ok"])
    n0 = d["nh0"]
    add("J2 on our plane the bank gives a = 1/2, b = 1, c = 4 (L = R = 2m), and the constraint holds there",
        abs(n0["a"] - 0.5) < 1e-3 and abs(n0["b"] - 1) < 1e-3 and abs(n0["c"] - 4) < 1e-3 and abs(-4 * 1 * 4 + 1 * 16) < 1e-12)
    rows = d["rows"]
    mono = all(r[3] < 0 and r[4] > 0 for r in rows) and all(r[1] > 0 for r in rows)
    lam = [2 * math.sqrt(r[1] / r[2]) for r in rows]
    add("J3 for y > 0, b' < 0 and c' > 0 (from (c b')' < 0, (b c')' > 0 and b'(0) = c'(0) = 0): lambda = L/R strictly "
        "decreasing, R strictly increasing", mono and all(l2 < l1 for l1, l2 in zip(lam, lam[1:])))
    cmp = d["cmp"]
    add("J4 the ODE reproduces the bank's near-horizon L and R to 1e-3 at y = 0.25-2.45m, keeps the constraint, and "
        "lambda falls from 1 to about 0.07",
        all(abs(c[1] - c[2]) < 1e-3 and abs(c[3] - c[4]) < 1e-3 for c in cmp) and max(abs(r[5]) for r in rows) < 1e-6
        and 0.05 < lam[-1] < 0.09)
    # J5: matching L and R at mass ratio mu needs lambda(s1) = lambda(s2); injective, so s1 = s2, mu = 1
    ys = [r[0] for r in rows]
    Lf = [2 * math.sqrt(r[1]) for r in rows]
    Rf = [math.sqrt(r[2]) for r in rows]
    found = []
    for mu in (2.0, 1.5, 0.5):
        for i in range(0, len(rows), 25):
            for j in range(0, len(rows), 25):
                if abs(Lf[i] - mu * Lf[j]) < 1e-2 and abs(Rf[i] - mu * Rf[j]) < 1e-2:
                    found.append((mu, ys[i], ys[j]))
    same = [(ys[i], ys[j]) for i in range(0, len(rows), 25) for j in range(0, len(rows), 25)
            if abs(Lf[i] - Lf[j]) < 1e-2 and abs(Rf[i] - Rf[j]) < 1e-2]
    ctrl = bool(same) and all(abs(p - q) < 0.2 for p, q in same)     # mu = 1: the search finds matches, all near s1 = s2 (L, R stationary at y = 0)
    add("J5 matching L and R with position 2's side scaled by mu: no pair of depths matches both for mu = 2, 1.5 or 0.5 "
        "(lambda injective: s1 = s2, mu = 1); control: mu = 1 matches at s1 = s2", not found and ctrl)
    return res


MUTANTS = {"wrong_source": "the source term of (c b')' entered with the wrong sign"}


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
        print("  mutant %-14s %-55s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("m1p2_junction.py -- position 2's mass at the corridor's junction (item 211)\n")
    print("J1", {k: v for k, v in d["j1"].items()})
    print("J2 near-horizon data on our plane:", d["nh0"])
    for c in d["cmp"]:
        print("J4 y %.2f  L ode %.6f bank %.6f   R ode %.6f bank %.6f   lambda %.4f" % (c[0], c[1], c[2], c[3], c[4], c[1] / c[3]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
