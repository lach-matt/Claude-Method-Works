#!/usr/bin/env python3
"""corridor_p1.py -- item 454, the corridor's first rung P1 (BOUNCE-RESEARCH section 21): the throat with the plane.
M chose position 2's mouth in a second universe ("1 - b") and approved the ladder ("2 - yes").  Under (b) the hole is
stage 1's, electrically charged (section 14), so the extremal throat each plane sees is Kaus and Reall's near-horizon
problem (0901.4236, READ): ds^2 = A(rho)^2 dSigma^2 + drho^2 + R(rho)^2 dOmega^2 with unit AdS2 slices (k = -1), the
horizon's bulk end a smooth cap at rho = 0 (R = 0, R' = 1, A' = 0) and the plane at rho0 under Israel's conditions at
the Randall-Sundrum tension (ell = 1).  Their field lives on the plane; ours is the bulk U(1) of 446 (1), F = c omega
(omega the unit AdS2 area form), for which the Maxwell equations hold identically and dF = 0 makes c constant.  Bulk
normalisation G + Lambda g = 2(F F - g F^2/4) (Biggs and Santos 2407.00151 (3a), READ); a field term on the plane,
-(lam/16 pi G5) F^2 (Dvali, Gabadadze and Shifman hep-th/0010071, READ), adds Kaus and Reall's stress with lam in
place of their ell.  Labels: READ (quoted), computed (numerical), deduced.  Worked in the conversation; not verified;
not seated.  2026-10-17.

  P0 (read) M's words: 454.
  P1 (computed) The equations: Einstein-Maxwell for the ansatz, derived from the metric (sympy), agree with the ODEs
     integrated here at random points, and the Maxwell equations hold identically.
  P2 (computed) Kaus and Reall's exact point: A0 = 1/2 gives AdS2 x H^3, A = 1/2 throughout, sinh(sqrt(2) rho0) = 1,
     Q = 1/sqrt(2), L1 = 1/2, L2 = 1/sqrt(2) (READ, their (2.18)-(2.21)), to 1e-9.
  P3 (computed) Their small holes: L1, L2, rho0 over (Q^2)^(1/3) and S5/S4 extrapolate to 0.244, 0.657, 0.558, 0.138;
     theirs "0.24", "0.66", "0.56", "0.14" (READ).
  P4 (computed) Their large holes: L1^2 - Q^2 -> -3/4, L2^2 - Q^2 -> -1/4, rho0 - log Q -> log 2 (READ, (1.1),
     (1.3)), and the entropy's constant term -0.443 pi = -1.39 against their "a constant ~ -1.4 ell^3/G5" (READ).
  P5 (deduced) With the bulk field alone the plane needs A'/A = R'/R = 1.  W = A'/A - R'/R obeys
     (A^2 R^2 W)' = 2c^2 R^2/A^2 - R^2 - A^2 and W -> -inf at the cap, so at the first zero of W (where W' >= 0) the
     constraint gives W' = 3c^2/L1^4 - 2/L1^2 >= 0 with 1/L2^2 = 1/L1^2 - c^2/L1^4 > 0: L2^2 >= 3 L1^2.  A plane
     there would see AdS2 x S^2 with the sphere at least sqrt(3) times the AdS2, far from four-dimensional GR's L1 = L2.
  P6 (computed) With the bulk field alone no throat meets the plane: over a scan in (A0, c), W < 0 wherever
     A'/A + R'/R >= 1.5; and from every bulk-only plane (A'/A = R'/R = 1, the constraint holding) the inward
     integration reaches R = 0 only singularly (R' there >> 1, where a smooth cap has R' = 1).
  P7 (computed) With a field term on the plane the extremal throat exists above lam_min, which grows steeply with the
     hole: lam_min/L1^2 = 2.6-2.7 for small holes (L2/L1 -> 2, five-dimensional Reissner-Nordstrom's AdS2 x S^3),
     1.1 at L1 = 0.76, and 3.4e3 at L1 = 10 (lam_min/L1^2 = 34); Kaus and Reall's field on the plane is the limit
     lam -> infinity with lam c^2 held.  Mutants: k_zero, no_lambda, israel_sign, src_sign, and plane_term (a field
     term slipped into P6's bulk-only test, which P6 must catch).
  P8 (deduced) The reading for (b): with the bulk U(1) alone the hole has no extremal throat on the plane, so it
     cannot approach extremality there; a field on the plane (Kaus and Reall; Chamblin, Reall, Shinkai and Shiromizu)
     or a strong enough field term for the bulk U(1) (Dvali, Gabadadze and Shifman) gives it one.

python3 corridor_p1.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ('"1 - b 2 - yes"',)
KR_SMALL = (0.24, 0.66, 0.56, 0.14)


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def k_slice():
    return 0.0 if "k_zero" in MUT else -1.0


def rhs(r, y, c):
    """A'' from the AdS2 equation, R'' from the sphere's (Kaus and Reall's (2.4), (2.6) with the bulk source)"""
    A, Ap, R, Rp = y
    k = k_slice()
    E = -c * c / A**4 if "src_sign" in MUT else c * c / A**4
    lam4 = 0.0 if "no_lambda" in MUT else 4.0
    App = A * (k / A**2 - Ap**2 / A**2 - 2 * Ap * Rp / (A * R) + lam4 + 4 * E / 3)
    Rpp = R * (1 / R**2 - Rp**2 / R**2 - 2 * Ap * Rp / (A * R) + lam4 - 2 * E / 3)
    return [Ap, App, Rp, Rpp]


def constraint(y, c):
    A, Ap, R, Rp = y
    return (k_slice() / A**2 + 1 / R**2) - (Ap**2 / A**2 + Rp**2 / R**2 + 4 * Ap * Rp / (A * R) - 6 - c * c / A**4)


def start(A0, c, eps):
    """the smooth cap's series: A = A0 + a2 rho^2, R = rho + r3 rho^3"""
    E0 = c * c / A0**4
    a2 = A0 * (k_slice() / A0**2 + 4 + 4 * E0 / 3) / 6
    r3 = (4 - 2 * E0 / 3 - 4 * a2 / A0) / 12
    return [A0 + a2 * eps**2, 2 * a2 * eps, eps + r3 * eps**3, 1 + 3 * r3 * eps**2]


def shoot(A0, c, rmax=40.0, rtol=1e-12):
    eps = 1e-4 * min(A0, 1.0)

    def ev(r, y, c):
        return y[1] / y[0] + y[3] / y[2] - 2.0
    ev.terminal, ev.direction = True, -1

    def blow(r, y, c):
        return min(y[0], y[2]) - 1e-9
    blow.terminal = True
    return solve_ivp(rhs, (eps, rmax), start(A0, c, eps), args=(c,), method="DOP853", rtol=rtol, atol=1e-15,
                     events=[ev, blow], dense_output=True)


def israel_brane(a, b, R):
    """Kaus and Reall's (2.16), ell = 1: A'/A = 1 - Q^2/(2R^4), R'/R = 1 + Q^2/(2R^4); returns Q^2"""
    if "israel_sign" in MUT:
        return 2 * R**4 * (a - 1)
    return 2 * R**4 * (b - 1)


def entropy(s, r0):
    """S5 G5 = 2 pi int_0^rho0 R^2 drho (both sides of the plane; Kaus and Reall's (2.22))"""
    return 2 * math.pi * solve_ivp(lambda r, y: [s.sol(r)[2]**2], (s.t[0], r0), [0.0], rtol=1e-12,
                                   atol=1e-15).y[0, -1]


def brane_field(A0, rmax=40.0, rtol=1e-12):
    s = shoot(A0, 0.0, rmax, rtol)
    if len(s.t_events[0]) == 0:
        return None
    r0 = s.t_events[0][0]
    A, Ap, R, Rp = s.y_events[0][0]
    Q2 = israel_brane(Ap / A, Rp / R, R)
    rs = np.linspace(s.t[0] + 0.05 * r0, r0, 200)
    con = max(abs(constraint(s.sol(r), 0.0)) * min(s.sol(r)[0], s.sol(r)[2])**2 for r in rs)
    return dict(rho0=r0, L1=A, L2=R, Q2=Q2, S5=entropy(s, r0), con=con, s=s)


def symbolic_check():
    """Einstein-Maxwell for the ansatz from the metric, against rhs() and constraint() at random points"""
    import sympy as sp
    t, x, rho, th, ph, c = sp.symbols("t x rho theta phi c")
    A, R = sp.Function("A")(rho), sp.Function("R")(rho)
    X = [t, x, rho, th, ph]
    g = sp.diag(-A**2 * (1 + x**2), A**2 / (1 + x**2), 1, R**2, R**2 * sp.sin(th)**2)
    gi = g.inv()
    n = 5
    G = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[e]) + sp.diff(g[d, e], X[b]) - sp.diff(g[b, e], X[d]))
               for d in range(n)) / 2 for e in range(n)] for b in range(n)] for a in range(n)]

    def ric(b, e):
        r = 0
        for a in range(n):
            r += sp.diff(G[a][b][e], X[a]) - sp.diff(G[a][b][a], X[e])
            for d in range(n):
                r += G[a][a][d] * G[d][b][e] - G[a][e][d] * G[d][b][a]
        return r
    Ric = sp.Matrix(n, n, lambda i, j: ric(i, j))
    F = sp.zeros(n)
    F[0, 1], F[1, 0] = c, -c
    Fup = gi * F * gi
    F2 = sum(F[i, j] * Fup[i, j] for i in range(n) for j in range(n))
    FF = F * gi * F.T
    E = Ric + 4 * g - 2 * (FF - g * F2 / 6)
    sq = sp.sqrt(-g.det())
    maxwell = [sp.simplify(sum(sp.diff(sq * Fup[a, b], X[a]) for a in range(n))) for b in range(n)]
    Rs = sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n))
    con = (Ric[2, 2] - Rs * g[2, 2] / 2) - 6 * g[2, 2] - 2 * (FF[2, 2] - g[2, 2] * F2 / 4)
    a0, a1, a2, r0_, r1, r2, cc = sp.symbols("a0 a1 a2 r0 r1 r2 cc")
    sub = {sp.Derivative(A, (rho, 2)): a2, sp.Derivative(R, (rho, 2)): r2, sp.Derivative(A, rho): a1,
           sp.Derivative(R, rho): r1}
    # the AdS2 pair, the sphere, two off-diagonal components, and the rho-rho constraint
    picks = (E[0, 0] / g[0, 0], E[1, 1] / g[1, 1], E[3, 3] / g[3, 3], E[0, 2], E[2, 3], con)
    exprs = [sp.lambdify((a0, a1, a2, r0_, r1, r2, cc, x, th), e.subs(sub).subs({A: a0, R: r0_, c: cc}), "math")
             for e in picks]
    rng = np.random.default_rng(454)
    worst = 0.0
    for _ in range(20):
        Av, Apv, Rv, Rpv = rng.uniform(0.3, 2.0), rng.uniform(-1, 1), rng.uniform(0.3, 2.0), rng.uniform(-1, 1)
        cv, xv, thv = rng.uniform(0, 1.5), rng.uniform(-1, 1), rng.uniform(0.3, 2.8)
        y = [Av, Apv, Rv, Rpv]
        _, App, _, Rpp = rhs(0.0, y, cv)
        v = [f(Av, Apv, App, Rv, Rpv, Rpp, cv, xv, thv) for f in exprs]
        worst = max([worst] + [abs(t) for t in v[:5]] + [abs(v[5] + constraint(y, cv))])
    return worst, all(m == 0 for m in maxwell)


def w_identities():
    """P5 on the ODEs integrated here (sympy): W' = -2W(a+b) + 2c^2/A^4 - 1/A^2 - 1/R^2,
    (A^2 R^2 W)' = 2c^2 R^2/A^2 - R^2 - A^2, and at a = b = 1 with the constraint W' = 3c^2/A^4 - 2/A^2"""
    import sympy as sp
    A, Ap, R, Rp, c, iR2 = sp.symbols("A Ap R Rp c iR2", positive=True)
    _, App, _, Rpp = rhs(0.0, [A, Ap, R, Rp], c)
    a, b = Ap / A, Rp / R
    W = a - b
    Wp = (App / A - a**2) - (Rpp / R - b**2)
    one = sp.simplify(Wp - (-2 * W * (a + b) + 2 * c**2 / A**4 - 1 / A**2 - 1 / R**2)) == 0
    two = sp.simplify(2 * A * Ap * R**2 * W + 2 * A**2 * R * Rp * W + A**2 * R**2 * Wp
                      - (2 * c**2 * R**2 / A**2 - R**2 - A**2)) == 0
    con = constraint([A, A, R, R], c)                 # at the plane A'/A = R'/R = 1
    sol = sp.solve(sp.Eq(con.subs(1 / R**2, iR2), 0), iR2)
    three = len(sol) == 1 and sp.simplify(sol[0] - (1 / A**2 - c**2 / A**4)) == 0
    Wp1 = Wp.subs({Ap: A, Rp: R}).subs(1 / R**2, sol[0] if sol else 0)
    four = sp.simplify(Wp1.subs(R, 1 / sp.sqrt(sol[0])) - (3 * c**2 / A**4 - 2 / A**2)) == 0 if sol else False
    return one and two and three and four


def bulk_W(A0, c, rmax=12.0):
    """W at the first downward crossing of A'/A + R'/R = 2, and max W where A'/A + R'/R >= 1.5"""
    eps = 1e-4 * min(A0, 1.0)

    def bl(r, y, c):
        return min(y[0], y[2]) - 1e-9
    bl.terminal = True

    def big(r, y, c):
        return max(y[0], y[2]) - 1e6
    big.terminal = True
    s = solve_ivp(rhs, (eps, rmax), start(A0, c, eps), args=(c,), method="DOP853", rtol=1e-11, atol=1e-14,
                  events=[bl, big], dense_output=True)
    r = np.linspace(s.t[0], s.t[-1], 3000)
    A, Ap, R, Rp = s.sol(r)
    a, b = Ap / A, Rp / R
    W, S = a - b, a + b
    if "plane_term" in MUT:                     # a field term lam = 1 on the plane: the plane needs W = -c^2/L1^4
        W = W + c * c / A**4
    m = S >= 1.5
    return (W[m].max() if m.any() else -np.inf)


def inward(L1, s2):
    """from a bulk-only plane (A'/A = R'/R = 1, constraint) toward the cap; R' where R reaches ~0"""
    c = math.sqrt(s2) * L1
    L2 = 1 / math.sqrt(1 / L1**2 - c**2 / L1**4)

    def stop(r, y, c):
        return y[2] - 1e-7 * L2
    stop.terminal = True

    def blowA(r, y, c):
        return y[0] - 1e-9 * L1
    blowA.terminal = True
    sol = solve_ivp(rhs, (0, -60 * L1 - 10), [L1, L1, L2, L2], args=(c,), method="DOP853", rtol=1e-11,
                    atol=1e-15, events=[stop, blowA])
    if len(sol.t_events[0]) == 0:
        return None
    return sol.y[3, -1]


def lam_needed(A0, c):
    """field term on the plane: A'/A = 1 - lam c^2/(2 L1^4), R'/R = 1 + lam c^2/(2 L1^4) at the sum root"""
    s = shoot(A0, c, rmax=12)
    if len(s.t_events[0]) == 0:
        return None
    A, Ap, R, Rp = s.y_events[0][0]
    W = Ap / A - Rp / R
    if A > 1e3 or -W < 1e-8:
        return None
    return -W * A**4 / c**2, A, R


def lam_min(A0, n=120):
    rows = [(v[0], f, v[1], v[2]) for f in np.geomspace(0.05, 30, n) for v in [lam_needed(A0, f * A0)] if v]
    return min(rows) if rows else None


def run(quiet=False, gate=None):
    say = (lambda *a: None) if quiet else print
    res = {}
    w, mx = symbolic_check()
    res["p1"] = (w, mx)
    if gate and not gate("p1", res):
        return res
    b = brane_field(0.5)
    res["p2"] = b
    if gate and not gate("p2", res):
        return res
    small = {}
    for A0 in (0.005, 0.0025):
        bb = brane_field(A0)
        u = bb["Q2"]**(1 / 3)
        small[A0] = (bb["L1"] / u, bb["L2"] / u, bb["rho0"] / u, bb["S5"] / (math.pi * bb["Q2"]))
    res["p3"] = tuple(2 * small[0.0025][i] - small[0.005][i] for i in range(4))
    if gate and not gate("p3", res):
        return res
    big = brane_field(0.9999, rmax=60)
    Q2 = big["Q2"]
    res["p4"] = dict(d1=big["L1"]**2 - Q2, d2=big["L2"]**2 - Q2, dr=big["rho0"] - 0.5 * math.log(Q2),
                     s0=big["S5"] - math.pi * Q2 + 0.5 * math.pi * math.log(Q2),
                     con=big["con"], rt=tuple(abs(brane_field(0.9999, rmax=60, rtol=t)["rho0"] - big["rho0"])
                                              for t in (1e-10, 1e-11)))
    if gate and not gate("p4", res):
        return res
    res["p5"] = w_identities()
    if gate and not gate("p5", res):
        return res
    worst = -np.inf
    for A0 in np.concatenate([np.geomspace(0.01, 0.5, 6), np.linspace(0.7, 2.0, 4)]):
        for f in np.concatenate([np.linspace(0.05, 3.0, 20), [5.0, 10.0, 30.0]]):
            worst = max(worst, bulk_W(A0, f * A0))
    rp = []
    for L1 in (0.02, 0.1, 0.5, 2.0, 10.0):
        for s2 in np.linspace(0.0, 0.99, 25):
            v = inward(L1, s2)
            if v is not None:
                rp.append(v)
    res["p6"] = dict(Wmax=worst, Rpmin=min(rp), n=len(rp))
    say("  bulk only: max W on a+b>=1.5 = %.2e; inward R' at R->0 >= %.1f over %d planes" %
        (worst, min(rp), len(rp)))
    if gate and not gate("p6", res):
        return res
    lm = {A0: lam_min(A0) for A0 in (0.02, 0.5, 0.99)}
    res["p7"] = lm
    for A0, v in lm.items():
        say("  field term on the plane: A0 = %.2f lam_min = %.4g at L1 = %.4g (lam/L1^2 = %.2f), L2/L1 = %.3f" %
            (A0, v[0], v[2], v[0] / v[2]**2, v[3] / v[2]))
    if gate:
        gate("p7", res)
    return res


def _check(stage, res):
    if stage == "p1":
        w, mx = res["p1"]
        r = w < 1e-9 and mx
        return r, "P1 the ODEs are Einstein-Maxwell for the ansatz (worst residual %.1e), Maxwell identical: %s" % (w, r)
    if stage == "p2":
        b = res["p2"]
        Avar = np.ptp(b["s"].sol(np.linspace(b["s"].t[0], b["rho0"], 200))[0])
        r = (b is not None and Avar < 1e-9 and abs(b["rho0"] - math.asinh(1) / math.sqrt(2)) < 1e-9
             and abs(b["L2"] - 1 / math.sqrt(2)) < 1e-9 and abs(b["Q2"] - 0.5) < 1e-9)
        return r, "P2 Kaus and Reall's exact point (AdS2 x H^3, Q = 1/sqrt 2): %s" % r
    if stage == "p3":
        v = res["p3"]
        r = all(abs(v[i] - KR_SMALL[i]) < 0.0065 for i in range(4))
        return r, "P3 their small holes: %s against 0.24, 0.66, 0.56, 0.14: %s" % (
            ", ".join("%.3f" % t for t in v), r)
    if stage == "p4":
        p = res["p4"]
        r = (abs(p["d1"] + 0.75) < 2e-3 and abs(p["d2"] + 0.25) < 2e-3 and abs(p["dr"] - math.log(2)) < 1e-3
             and abs(p["s0"] + 1.4) < 0.05 and p["con"] < 1e-8 and p["rt"][1] < p["rt"][0] and p["rt"][1] < 1e-6)
        return r, ("P4 their large holes: %.4f, %.4f, rho0 - log Q = %.5f, entropy constant %.3f: %s" %
                   (p["d1"], p["d2"], p["dr"], p["s0"], r))
    if stage == "p5":
        r = res["p5"]
        return r, ("P5 (deduced, identities machine-checked) a bulk-only plane at W's first zero needs "
                   "L2^2 >= 3 L1^2: %s" % r)
    if stage == "p6":
        p = res["p6"]
        r = p["Wmax"] < 0 and p["Rpmin"] > 10 and p["n"] >= 100
        return r, "P6 with the bulk field alone no throat meets the plane: %s" % r
    lm = res["p7"]
    s, m, g = lm[0.02], lm[0.5], lm[0.99]
    r = (2.2 < s[0] / s[2]**2 < 3.0 and 0.5 < m[0] < 4 and g[0] / g[2]**2 > 20 and g[2] > 5
         and s[3] / s[2] > 1.8 and g[3] / g[2] < 1.01)
    return r, "P7 a field term on the plane gives the throat above lam_min, steep in size: %s" % r


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("P0 words: %s" % r)

    def gate(stage, res):
        r, line = _check(stage, res)
        ok.append(r)
        say(line)
        return r or not quiet
    run(quiet, gate)
    ok.append(all(ok)); say("P8 (deduced) the reading for (b) follows from P5-P7: %s" % ok[-1])
    say("%d/%d" % (sum(ok), 9))
    return len(ok) == 9 and all(ok)


def mutants():
    caught = 0
    names = ("k_zero", "no_lambda", "israel_sign", "src_sign", "plane_term")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-11s %s" % (m, "caught" if bad else "MISSED"), flush=True)
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    run()
