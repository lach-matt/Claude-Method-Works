#!/usr/bin/env python3
"""g0_small.py -- item 542, lemma G0s: the small end's static corridor is unique, order by order in r_h/ell.  M, 542:
"add lemmas to close these gaps. nothing gets narrowed, only expanded to complete the statement" -- the gap (541, A2):
G1 and G3's "exactly one static corridor" rested on Gibbons, Ida and Shiromizu, whose theorem is for asymptotically
flat vacuum, not for the hole on our plane at finite ell.  Labels: computed (exact unless marked numerical), READ,
deduced, M's.

  Z0 (read) M's words, verbatim in the rulings file, 542.
  Z1 (computed, exact) Every static perturbation of five-dimensional Tangherlini with harmonic degree l >= 2 has a
     strictly positive master potential on the whole exterior.  The potentials are settle5's (Cardoso, Lemos and
     Yoshida, hep-th/0311260 (2.4), READ there; Kodama and Ishibashi's), V = f q/r^2, x = r_h^2/r^2, n = 3:
     - tensor: q = (2l + 3)(2l + 1)/4 + (9/4) x > 0;
     - vector: q = (2l + 3)(2l + 1)/4 - (27/4) x >= l^2 + 2l - 6 > 0 for l >= 2 (least at the horizon);
     - scalar: q = Q/(16 H^2) with H = m + 6x > 0 and Q >= 4m(4m^2 + 15m - 108) > 0, m = l(l + 2) - 3 >= 5.
  Z2 (computed, exact) So no static zero mode exists.  In the tortoise coordinate the static master equation is
     Phi'' = V Phi.  A perturbation regular at the horizon has Phi -> a, Phi' -> 0 there (the other solution grows
     linearly in r*, logarithmically in r - r_h), and with a = 1 and V > 0, Phi' = int V Phi > 0 keeps Phi >= 1 for
     ever: the regular solution never decays.  At infinity the two branches go as r^(l + 3/2) and r^-(l + 1/2)
     (computed: s(s - 1) = (2l + 3)(2l + 1)/4).  The regular solution is the growing one, so nothing is both regular
     and decaying: the static operator's kernel is trivial in every type and degree l >= 2.
  Z3 (computed, numerical) The same, integrated: for l = 2 to 8, every type, the horizon-regular solution grows as
     r^(l + 3/2) with a positive coefficient, steady to 1e-3 between 2e3 r_h and 4e3 r_h.
  Z4 (READ; deduced) Below l = 2 nothing is free.  Hung, Keller and Wang (1809.05144v1, Theorem 1, READ in settle5):
     "the l < 2 part is pure gauge plus a linearised Myers-Perry solution" -- a change of mass, fixed by N (H1), and
     rotations, excluded at J = 0 by both reflections (settle5 T1; settle_late S1).  The l = 1 translation normal to
     the plane is odd under the mirror; along it is where the hole sits, a choice of origin.
  Z5 (READ; deduced) Order by order.  The corridor at finite ell is the matched expansion in eps = r_h/ell: near the
     hole Tangherlini plus corrections, far from it the linearised field of a mass on the plane (Garriga and Tanaka,
     READ in far_large), matched where both hold.  Karasik, Sahabandu, Suranyi and Wijewardhana (gr-qc/0404015v2,
     READ) build the first order and find every free coefficient fixed: the junction conditions set a(lambda = 2n)
     (their (33)), constant surface gravity sets delta_0 and a(lambda = 2k + 1) ((38)-(39)), and the first law sets
     d_2 = 0 and delta_0 = 0 ((42), (47)); "the results for the eps solution and the discussion of regularity are
     equivalent" for one brane, with eps -> -eps (p. 9).  At every higher order the near-zone equation is the same
     static operator with a source: its solutions differ by homogeneous ones, which are either regular and growing
     (fixed by the matching, Z3) or decaying and singular at the horizon (excluded, Z2).  So no free parameter enters
     at any order beyond the mass and the position: the static corridor near Tangherlini is unique, order by order.
  Z6 (deduced) The hypotheses read.  Gibbons, Ida and Shiromizu's uniqueness (gr-qc/0203004) needs asymptotic
     flatness and a non-degenerate horizon: it holds exactly at eps = 0 (kappa = 1/r_h).  At eps > 0 the plane breaks
     asymptotic flatness, and Z1-Z5 carry the uniqueness instead.  The example README sits at eps = 8.0e-16 (the
     window's top) to 6.5e-13 (ell_H) (ell_si L2).  The nonlinear hole at finite eps is known numerically
     (Kudoh, Tanaka and Nakamura, gr-qc/0301089, READ at 254; Figueras and Wiseman's family, READ at 261, "no zero
     modes"), and gmid.py follows it from R4 = 0.2 ell up.  A proof that no static brane hole exists on a separate
     branch, away from Tangherlini, is not in the field.

Imports ../n1star/settle5.py (the potentials) by path.  numpy, scipy, sympy.
python3 g0_small.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, os, sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "add lemmas to close these gaps"),
         (542, "nothing gets narrowed, only expanded to complete the statement"))
_MOD = {}


def _settle5():
    if "s5" not in _MOD:
        spec = importlib.util.spec_from_file_location("g0_settle5", os.path.join(D68, "n1star", "settle5.py"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["g0_settle5"] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        _MOD["s5"] = mod
    return _MOD["s5"]


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def q_of(kind, l):
    """q(x) = r^2 V/f as a sympy expression in x, from settle5's potentials (the mutant: the vector type's horizon
    coefficient taken twice as large)"""
    S5 = _settle5()
    r, rh, V = S5.potentials(l, kind)
    x = sp.Symbol("x", positive=True)
    q = sp.simplify((V * r ** 2 / (1 - rh ** 2 / r ** 2)).subs(r, rh / sp.sqrt(x)))
    if MUT.get("vector") and kind == "vector":
        q = q - sp.Rational(27, 4) * x
    return x, q


def z1():
    """the potentials' positivity on 0 <= x <= 1: tensor and vector exactly, scalar by the bound on Q"""
    out = {}
    x = sp.Symbol("x", positive=True)
    l = sp.Symbol("l", positive=True)
    for kind in ("tensor", "vector"):
        mins = []
        for L in range(2, 9):
            xx, q = q_of(kind, L)
            q = q.subs(xx, x)
            mins.append(min(sp.nsimplify(q.subs(x, 0)), sp.nsimplify(q.subs(x, 1))))   # q is linear in x
            assert sp.degree(sp.expand(q), x) <= 1
        out[kind] = (all(m > 0 for m in mins), mins[0])
    # the vector type for every l: least at the horizon, l^2 + 2l - 6
    qv1 = sp.expand((2 * l + 3) * (2 * l + 1) / 4 - sp.Rational(27, 4))
    out["vector_all"] = sp.simplify(qv1 - (l ** 2 + 2 * l - 6)) == 0 and (qv1.subs(l, 2) > 0)
    # the scalar type for every m >= 5: Q's lower bound, and H > 0
    m = sp.Symbol("m", positive=True)
    Q = 1296 * x ** 3 + (624 * m - 144) * x ** 2 + 36 * (m - 12) * m * x + 16 * m ** 3 + 60 * m ** 2
    bound = 4 * m * (4 * m ** 2 + 15 * m - 108)
    # Q - bound = 1296 x^3 + (624 m - 144) x^2 + 36 m^2 x + 432 m (1 - x) >= 0 on 0 <= x <= 1, m >= 5
    gap = sp.expand(Q - bound - (1296 * x ** 3 + (624 * m - 144) * x ** 2 + 36 * m ** 2 * x + 432 * m * (1 - x)))
    xs, qs = q_of("scalar", 2)
    Qs = sp.simplify(qs.subs(xs, x) * 16 * (5 + 6 * x) ** 2)
    out["scalar"] = (gap == 0 and sp.expand(Qs - Q.subs(m, 5)) == 0
                     and bound.subs(m, 5) > 0 and sp.diff(4 * m ** 2 + 15 * m - 108, m).subs(m, 5) > 0,
                     int(bound.subs(m, 5)))
    return out


def z2():
    """the indicial exponents at infinity, s(s - 1) = (2l + 3)(2l + 1)/4"""
    s, l = sp.symbols("s l")
    roots = sp.solve(sp.Eq(s * (s - 1), (2 * l + 3) * (2 * l + 1) / 4), s)
    return set(sp.simplify(r_) for r_ in roots) == {l + sp.Rational(3, 2), -l - sp.Rational(1, 2)}


def regular_growth(kind, l, r_max=4000.0):
    """integrate the horizon-regular static solution (r_h = 1) outward; Phi / r^(l + 3/2) at 2e3 and 4e3"""
    xs, q = q_of(kind, l)
    qf = sp.lambdify(xs, q, "numpy")
    # with y = f dPhi/dr: dPhi/dr = y/f, dy/dr = q Phi / r^2; regular: Phi = 1, y = 0 at the horizon
    qh = float(q.subs(xs, 1))
    r0 = 1 + 1e-6
    f0 = 1 - 1 / r0 ** 2
    y0 = qh * (r0 - 1)
    ph0 = 1 + qh / 2 * (r0 - 1)

    def rhs(r, u):
        f = 1 - 1 / r ** 2
        return [u[1] / f, qf(1 / r ** 2) * u[0] / r ** 2]
    sol = solve_ivp(rhs, (r0, r_max), [ph0, y0], method="LSODA", rtol=1e-10, atol=1e-14, dense_output=True)
    a = sol.sol(r_max / 2)[0] / (r_max / 2) ** (l + 1.5)
    b = sol.sol(r_max)[0] / r_max ** (l + 1.5)
    return a, b, f0


def z3():
    rows = {}
    for kind in ("tensor", "vector", "scalar"):
        for l in range(2, 9):
            a, b, _ = regular_growth(kind, l)
            rows[(kind, l)] = (a, b)
    ok = all(b > 0 and abs(a / b - 1) < 1e-3 for a, b in rows.values())
    return ok, rows


def compute():
    return dict(words=words(), z1=z1(), z2=z2(), z3=z3())


def checks(o):
    z = o["z1"]
    return {"Z0": o["words"],
            "Z1": z["tensor"][0] and z["vector"][0] and z["vector_all"] and z["scalar"][0],
            "Z2": o["z2"],
            "Z3": o["z3"][0]}


def report(o=None):
    o = o or compute(); ck = checks(o)
    z = o["z1"]
    print("Z0 M's words:", o["words"])
    print("Z1 tensor q > 0 for l = 2-8 (least %s); vector q > 0 (least %s, l^2 + 2l - 6 for every l: %s); scalar Q >= "
          "4m(4m^2 + 15m - 108) = %s at m = 5: %s" % (z["tensor"][1], z["vector"][1], z["vector_all"],
                                                     z["scalar"][1], z["scalar"][0]))
    print("Z2 the branches at infinity r^(l + 3/2), r^-(l + 1/2): %s" % o["z2"])
    for (kind, l), (a, b) in sorted(o["z3"][1].items()):
        if l in (2, 4, 8):
            print("Z3 %-6s l = %d: Phi/r^(l+3/2) = %.6g at 2e3, %.6g at 4e3" % (kind, l, a, b))
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


MUTANTS = {"vector": "the vector type's horizon term doubled, so its potential turns negative near the horizon (Z1)"}


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
