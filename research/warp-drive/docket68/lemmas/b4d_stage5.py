#!/usr/bin/env python3
"""b4d_stage5.py -- Warp Theorem lemma B4d, stage 5: the corridor of fixed size through the write (M-RULINGS items
161-163).  Computed and deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 163 "All together, one whole" (the README carried in, held as one whole;
the gas bound stands); item 162 "The throat doesn't change size"; item 161 "my inclination is yes" (the corridor stays
regular while the README passes); item 160 "the corridor and the opening are the same object"; item 115 (c) "The README
itself" (the inflow); item 136 G (the README is the energy); clause (B) (the plane carries no matter); items 117/120 ("the
NEC only ever appears to break, but never does").

  F1 A FIXED SIZE WITH AN INFLOW IS A THROUGH-FLOW (STRUCTURAL, deduced).  On the plane, in the Vaidya form the opening
     already uses (opening.py), the trapping radius is r = 2 m(v) (computed), so 162's fixed size is dm/dv = 0: no net
     flux.  By 115 (c) and 136 G the README's energy flows in, for at least the gas bound's T (o3_write.py, 2.0e5
     clocks, which 163 keeps); so an equal flux leaves -- the corridor is a steady through-flow from position 1 to
     position 2 (H-THROUGH-FLOW, the board's reading of 160, 162, 163).  Its flux is at most E/T: 1/T = 5.0e-6 per
     clock in units of the corridor's mass m.
  F2 AT EVERY ell TESTED THE STATIC BULK STILL HAS A SINGULAR SURFACE, NEARER THE PLANE AS ell FALLS (computed;
     numerical evidence, not a bound).  b4_static.py's exact series at r = 2.15m, order 32 in y, with ell = 1/e finite
     (Randall-Sundrum tension, e = 1/ell; the series is not even in y).  Factoring out the warp -- X~ = X e^(2y/ell),
     constant in y for the black string -- removes the spurious poles that a bare Padé in y shows.  For each ell:
       * the nearest positive real singularity y_s of C~, at three Padé orders;
       * Pringsheim (standard, not READ): C~'s coefficients keep one sign from order 24 to 32 (where nonzero), and a
         power series with coefficients of one sign is singular at the positive real point of its radius -- root test
         |c_k|^(-1/k) agrees with y_s from above (it converges slowly);
       * K along the column, three Padé orders, against the black string at the same ell, K_bs = 40/ell^4 +
         48 m^2 e^(4y/ell)/r^6 (Chamblin-Hawking-Reall's form, standard, not READ; checked below): the depth y_K at
         which K reaches 30 K_bs, order-stable.
     ell = infinity (control, b4_static.py's 2.49-2.50m at order 80), 2m, m, m/2: y_s ~ 2.58, 1.43, 1.0, 0.69m (the
     three orders spread 0.05%, 0.1%, 6%, 0.01%); at finite ell the singularity shows as a near-real cluster of poles
     and zeros, the cut b4_static.py S2 found in the flat limit.  Spurious pole-zero pairs (Froissart doublets) are
     divided out before any evaluation.
     Controls: (i) ell = infinity reproduces b4_static.py's surface to the accuracy of order 32 (3% high); (ii)
     Schwarzschild data at ell = m: the warp-factored series terminates -- the black string, no singular surface at any
     finite y -- and the instrument's K equals K_bs.
     STRUCTURAL reading: the surface closing on the plane as ell falls is KSCALE's closure seen in the bulk -- with r0 >>
     ell the plane's geometry is four-dimensional GR to O(ell^2/r0^2) (Figueras-Wiseman, READ in b4d_stage2.py), and eq.
     (17)'s deficit is an O(1) Weyl datum the bulk cannot carry far.
  F3 THE HOLD THAT REACHES IT (computed).  Light from the plane down the column at r = 2.15m, in the static bulk's far
     time: T = 2 * integral_0^y_K dy/sqrt(A) -- the double cone of b4_static.py S3, along one path, so an upper bound on
     the earliest hold that contains the point (the minimum over paths is no later).  To y_K: 16.6, 11.7, 10.2, 8.6
     clocks at ell = infinity, 2m, m, m/2; to 0.95 y_s, where K is 1e5 or more at finite ell: 21.7, 18.0, 14.9, 13.1 --
     three Padé orders within 1% (2% at m/2), the lapse A positive all the way (>= 4e-4).  The last 5% to the surface is not
     resolved (the orders part there); A shows no sign of closing to a horizon.  Against F1's 2.0e5.  Control: at ell = infinity the column's time to K = 100 is no earlier than b4_static.py's
     banked 14.9 clocks (its minimum over all paths).
  F4 THE THROUGH-FLOW IS QUASI-STATIC OVER THAT HOLD (deduced, H-QUASI-STATIC-CORRIDOR, the board's).  Over T the
     through-flow moves at most (1/T_gas) T ~ 1e-4 of the mass past any point; the plane's data are eq. (17) to that
     order, and the bulk in the cone is the static bulk to that order.  Caution: the y-problem is elliptic and
     Hadamard-ill-posed, so continuity in the data is a reading inside the locally analytic class, not a theorem.
  F5 A SECOND PLANE BELOW THE SURFACE CARRIES NEC-BREAKING MATTER AT FINITE ell TOO (computed; STRUCTURAL at small
     height).  A mirrored plane at y = y_w closing the bulk (b4d_stage1.py D3, now at finite ell): rho + p_r =
     -A_y/(2A) + B_y/(2B) -- the warp cancels, and so does any tension (139's negative one included).  Exactly,
     rho + p_r = R4_kk (y_w + 3 y_w^2/ell) + O(y_w^3), R4_kk = -2(r - 2m)/(r^2 (2r - 3m)^2) < 0 (computed at r = 3m,
     rational); numerically negative at every r from 2.15m to 32m at y_w up to y_s/2.  So the plane would carry real
     matter breaking the NEC, which 117/120 rule out (clause (B) already forbids matter on the plane).
  VERDICT (deduced).  On a conjunction the corridor of 161-163 does not stay regular through the write: its bulk meets a
     curvature of 1e5 or more, rising to a singular surface, within about 20 clocks at every ell tested, against 2.0e5.  The conjunction: eq. (17) on
     the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD), one mirrored plane with the Randall-Sundrum tension
     and no matter (clause (B), H-RS2-ONE-PLANE), B4b's locally analytic class (Holmgren at linear order), Padé and
     Pringsheim as evidence, H-QUASI-STATIC-CORRIDOR, H-THROUGH-FLOW.  F5 closes a closing plane under 117/120.  Open:
     a plane with bulk on both sides (H-TWO-SIDED), a curved closing wall, a through-flowing plane whose geometry is
     not eq. (17), a bulk outside the analytic class, and ell below m/2 (not computed; the trend is nearer).

Imports lemmas/b4_static.py and lemmas/o3_write.py by path.  Needs python-flint, sympy, numpy, mpmath.
python3 b4d_stage5.py [--selftest]   (selftest about 2 min)
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ORDER = 32
RC = "43/20"                                    # b4_static.py's singular column, r = 2.15m
ES = [Fr(0), Fr(1, 2), Fr(1), Fr(2)]            # e = m/ell: ell = infinity, 2m, m, m/2
K_FACTOR = 30                                   # y_K: K reaches 30 times the black string's
B4_YB = 2.50                                    # b4_static.py S2: y_b = 2.49-2.50m (order 80)
B4_K100 = 14.9                                  # b4_static.py S3: K >= 100 from 14.9 clocks (minimum over paths)
WALL_R = ["43/20", "3", "5", "10", "32"]


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


B4 = _load(os.path.join(HERE, "b4_static.py"), "b4d5_b4static")


# ------------------------------------------------------------------------------------------------ F1 the through-flow
def through_flow():
    """Vaidya on the plane, f = 1 - 2 m(v)/r: the trapping radius, and its rate."""
    r, v = sp.symbols("r v", positive=True)
    m = sp.Function("m")(v)
    rah = sp.solve(sp.Eq(1 - 2 * m / r, 0), r)
    return rah, sp.diff(rah[0], v) if len(rah) == 1 else None, m, v


# ------------------------------------------------------------------------------------------------ F2 the warp-factored bulk
def warped(S, e, N):
    """X~ = X e^(2 e y), coefficient by coefficient (exact)."""
    w = [(2 * e) ** k / math.factorial(k) for k in range(N + 1)]
    return {X: {i: [sum(S[X][i][j] * w[k - j] for j in range(k + 1)) for k in range(N + 1)] for i in range(3)}
            for X in "ABC"}


def orders(N):
    return [(N // 2 - 1, N // 2), (N // 2, N // 2), (N // 2 - 2, N // 2 + 1)]


def _approx(c, o):
    if all(v == 0 for v in c[1:]):
        return [c[0]], [Fr(1)]
    return B4.pade(c, *o)


def nearest_real(c, o):
    """Nearest positive real pole of the Padé of c (a near-real pair counts, by its real part -- a cut of poles and
    zeros, as in b4_static.py S2), Froissart doublets (a zero within 2e-3) dropped."""
    p, q = _approx(c, o)
    if len(q) == 1:
        return None
    poles = np.roots([float(v) for v in reversed(q)])
    zeros = np.roots([float(v) for v in reversed(p)]) if len(p) > 1 else np.array([])
    keep = [z for z in poles if not len(zeros) or min(abs(z - zz) for zz in zeros) > 2e-3 * max(1, abs(z))]
    real = sorted(z.real for z in keep if abs(z.imag) < 5e-2 * abs(z) and z.real > 0)   # a near-real pair: a cut's start
    return real[0] if real else None


def pringsheim(c, N):
    tail = [(k, c[k]) for k in range(3 * N // 4, N + 1) if c[k] != 0]
    signs = {v > 0 for _, v in tail}
    return len(signs) == 1, abs(float(tail[-1][1])) ** (-1.0 / tail[-1][0])


def _clean(p, q, tol=2e-3):
    """p/q with its Froissart doublets cancelled: each pole with a zero within tol is divided out with that zero
    (roots at 40 digits).  Returns mp coefficient lists (highest first) and the doublets."""
    pp = [mp.mpf(v.numerator) / v.denominator for v in reversed(p)]
    qq = [mp.mpf(v.numerator) / v.denominator for v in reversed(q)]
    while len(pp) > 1 and pp[0] == 0:
        pp = pp[1:]
    while len(qq) > 1 and qq[0] == 0:
        qq = qq[1:]
    if len(qq) == 1 or len(pp) == 1:
        return pp, qq, []
    zs = list(mp.polyroots(pp, maxsteps=200, extraprec=200))
    dz = []
    for zq in mp.polyroots(qq, maxsteps=200, extraprec=200):
        if zs:
            zp = min(zs, key=lambda z: abs(z - zq))
            if abs(zp - zq) < tol * max(1, abs(zq)):
                dz.append((zq, zp))
                zs.remove(zp)
    return pp, qq, dz


_KF = None


def _kf():
    global _KF
    if _KF is None:
        K = B4.kretschmann()
        names = sorted(K.free_symbols, key=str)
        _KF = (names, sp.lambdify(names, K, "mpmath"))
    return _KF


def evaluator(W, e, o):
    """A, B, C and their derivatives at depth y from the warp-factored Padé at order o; returns K(y) and A(y)."""
    names, Kf = _kf()
    F = {(X, i): _clean(*_approx(W[X][i], o)) for X in "ABC" for i in range(3)}
    ee = mp.mpf(e.numerator) / e.denominator

    def ev(pq, t):
        pp, qq, dz = pq
        val = mp.polyval(pp, t) / mp.polyval(qq, t)
        for zp, zq in dz:
            val *= (t - zq) / (t - zp)
        return mp.exp(-2 * ee * t) * mp.re(val)

    def env(y):
        yy, out = mp.mpf(y), {}
        for X in "ABC":
            for i in range(3):
                f = lambda t, X=X, i=i: ev(F[(X, i)], t)
                out[X + ("_" + "r" * i if i else "")] = f(yy)
                if i < 2:
                    out[X + "_" + "r" * i + "y"] = mp.diff(f, yy, 1)
                if i == 0:
                    out[X + "_yy"] = mp.diff(f, yy, 2)
        return out

    def K(y):
        en = env(y)
        return float(Kf(*[en[str(n)] for n in names]))

    def A(y):
        return ev(F[("A", 0)], y)

    def wall(y):
        yy = mp.mpf(y)
        a = lambda t: ev(F[("A", 0)], t)
        b = lambda t: ev(F[("B", 0)], t)
        return float(-mp.diff(a, yy) / (2 * a(yy)) + mp.diff(b, yy) / (2 * b(yy)))
    return K, A, wall


def k_bs(e, r, y):
    return 40 * float(e) ** 4 + 48 * math.exp(4 * float(e) * y) / r ** 6


def depth_at(K, target, lo, hi, it=40):
    """Bisection for K(y) = target(y) on [lo, hi] (K - target < 0 at lo, > 0 at hi)."""
    for _ in range(it):
        mid = (lo + hi) / 2
        if K(mid) - target(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def column(e, N=ORDER, rc=RC):
    mp.mp.dps = 40
    r = float(Fr(rc))
    S = B4.series(rc, N, e)
    W = warped(S, e, N)
    ys = [nearest_real(W["C"][0], o) for o in orders(N)]
    ys = [y for y in ys if y is not None]
    ok_sign, root = pringsheim(W["C"][0], N)
    ys_mid = float(np.median(ys))
    out = {"e": e, "ys": ys, "y_s": ys_mid, "sign": ok_sign, "root": root, "yK": [], "T": [], "T95": [], "Amin": [],
           "K95": [], "T100": None}
    for o in orders(N):
        K, A, _ = evaluator(W, e, o)
        y_k = depth_at(K, lambda y: K_FACTOR * k_bs(e, r, y), 0.0, 0.995 * min(ys))
        out["yK"].append(y_k)
        out["T"].append(float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, y_k])))
        y95 = 0.95 * ys_mid
        out["T95"].append(float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, y_k, y95])))
        out["Amin"].append(min(float(A(f * y95)) for f in np.linspace(0, 1, 41)))
        out["K95"].append(K(y95))
        if e == 0 and o == orders(N)[1]:
            y100 = depth_at(K, lambda y: 100.0, 0.0, 0.995 * min(ys))
            out["T100"] = float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, y100]))
            out["y100"] = y100
    K, A, wall = evaluator(W, e, orders(N)[1])
    out["K_profile"] = [(f, K(f * ys_mid), k_bs(e, r, f * ys_mid)) for f in (0.0, 0.5, 0.8)]
    out["wall_215"] = [wall(f * ys_mid) for f in (0.25, 0.5)]
    return out


def schwarzschild_control(e=Fr(1), N=16, rc=RC):
    mp.mp.dps = 40
    S = B4.series(rc, N, e, data=B4._schwarzschild)
    W = warped(S, e, N)
    terminates = all(W[X][i][k] == 0 for X in "ABC" for i in range(3) for k in range(1, N + 1))
    K, _, _ = evaluator(W, e, orders(N)[1])
    r = float(Fr(rc))
    worst = max(abs(K(y) / k_bs(e, r, y) - 1) for y in (0.5, 1.0, 1.5))
    return terminates, worst


# ------------------------------------------------------------------------------------------------ F5 a closing plane
def wall_exact(e, rc="3", N=6):
    """rho + p_r = -A_y/(2A) + B_y/(2B) as an exact series: its y and y^2 coefficients against R4_kk."""
    y = sp.Symbol("y")
    S = B4.series(rc, N, e)
    A = sum(sp.Rational(c.numerator, c.denominator) * y**k for k, c in enumerate(S["A"][0]))
    B = sum(sp.Rational(c.numerator, c.denominator) * y**k for k, c in enumerate(S["B"][0]))
    ser = sp.series(-sp.diff(A, y) / (2 * A) + sp.diff(B, y) / (2 * B), y, 0, 3).removeO()
    r = sp.Rational(rc)
    R4 = -2 * (r - 2) / (r**2 * (2 * r - 3) ** 2)
    ee = sp.Rational(e.numerator, e.denominator)
    return ser.coeff(y, 0), sp.simplify(ser.coeff(y, 1) - R4), sp.simplify(ser.coeff(y, 2) - 3 * ee * R4), R4


def wall_far(e, y_s, N=20):
    """rho + p_r at r = 3m-32m, y_w = y_s/4 and y_s/2, from the exact series truncated at two orders (inside the
    radius of convergence there)."""
    out = []
    for rc in WALL_R[1:]:
        S = B4.series(rc, N, e)
        for f in (0.25, 0.5):
            yw = f * y_s
            vals = []
            for n in (N - 4, N):
                a = sum(float(S["A"][0][k]) * yw**k for k in range(n + 1))
                ay = sum(k * float(S["A"][0][k]) * yw**(k - 1) for k in range(1, n + 1))
                b = sum(float(S["B"][0][k]) * yw**k for k in range(n + 1))
                by = sum(k * float(S["B"][0][k]) * yw**(k - 1) for k in range(1, n + 1))
                vals.append(-ay / (2 * a) + by / (2 * b))
            out.append((rc, f, vals[1], abs(vals[1] - vals[0]) <= 1e-3 * abs(vals[1])))
    return out


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d5_o3write")
    t_gas = ow._num(ow.t_min(3))
    rah, rate, m, v = through_flow()
    cols = [column(e) for e in ES]
    ctl = schwarzschild_control()
    walls = {e: wall_exact(e) for e in ES[1:]}
    far = {c["e"]: wall_far(c["e"], c["y_s"]) for c in cols[1:]}
    return {"t_gas": t_gas, "flux": 1 / t_gas, "rah": rah, "rate": rate, "m": m, "v": v, "cols": cols, "ctl": ctl,
            "walls": walls, "far": far}


def _ell(e):
    return "inf" if e == 0 else str(1 / e)


def report(d):
    print("b4d_stage5.py -- B4d stage 5: the corridor of fixed size through the write\n")
    print("F1 trapping radius r = %s, d/dv = %s: fixed size is m' = 0; through-flow over >= %.3g clocks, flux <= %.2g "
          "per clock (units of m)" % (d["rah"], d["rate"], d["t_gas"], d["flux"]))
    print("F2/F3 at r = 2.15m (y in units of m; T in clocks):")
    for c in d["cols"]:
        print("   ell = %-4s y_s %s  one sign %s, root test %.2f  y_K %s  T %s" % (
            _ell(c["e"]), "/".join("%.3f" % y for y in c["ys"]), c["sign"], c["root"],
            "/".join("%.3f" % y for y in c["yK"]), "/".join("%.1f" % t for t in c["T"])))
        print("        K/K_bs at 0, 0.5, 0.8 y_s: %s" % ", ".join("%.3g/%.3g" % (k, b) for _, k, b in c["K_profile"]))
        print("        to 0.95 y_s: T %s clocks, A >= %s, K there %s" % ("/".join("%.1f" % t for t in c["T95"]),
              "/".join("%.1e" % a for a in c["Amin"]), "/".join("%.2g" % k for k in c["K95"])))
    c0 = d["cols"][0]
    print("   control ell = inf: time to K = 100 down the column %.1f clocks (b4_static.py minimum over paths 14.9)"
          % c0["T100"])
    print("   control Schwarzschild at ell = m: series terminates %s, K vs K_bs worst %.1e" % d["ctl"])
    print("F5 rho + p_r on a closing plane at r = 3m: (y^0, y^1 - R4_kk, y^2 - 3 e R4_kk) =")
    for e, w in d["walls"].items():
        print("   ell = %s: %s, %s, %s (R4_kk = %s)" % (_ell(e), *w))
    for c in d["cols"][1:]:
        print("   ell = %s at r = 2.15m, y_w = y_s/4, y_s/2: %s; r = 3-32m: %s" % (
            _ell(c["e"]), ", ".join("%.3g" % x for x in c["wall_215"]),
            ", ".join("%.2g" % x[2] for x in d["far"][c["e"]])))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    cols = {c["e"]: c for c in d["cols"]}
    chk("F1 (STRUCTURAL): on the plane the trapping radius is r = 2 m(v), so a fixed size is dm/dv = 0; the gas bound's "
        "2.0e5 clocks bounds the through-flow's flux by 5.0e-6 per clock",
        len(d["rah"]) == 1 and sp.simplify(d["rah"][0] - 2 * d["m"]) == 0
        and sp.simplify(d["rate"] - 2 * sp.diff(d["m"], d["v"])) == 0 and 1.9e5 < d["t_gas"] < 2.1e5)
    chk("F2 control: Schwarzschild data at ell = m -- the warp-factored series terminates (the black string, no "
        "singular surface) and K equals 40/ell^4 + 48 m^2 e^(4y/ell)/r^6 to 1e-12", d["ctl"][0] and d["ctl"][1] < 1e-12)
    c0 = cols[Fr(0)]
    chk("F2 control: ell = infinity reproduces b4_static.py's singular surface (2.50m at order 80) within 5% at "
        "order 32", all(abs(y / B4_YB - 1) < 0.05 for y in c0["ys"]) and len(c0["ys"]) == 3)
    fin = [cols[e] for e in ES[1:]]
    chk("F2: at ell = 2m, m, m/2 the nearest positive real singularity of C~ is stable across three Padé orders "
        "(spread under 7%: 0.1%, 6%, 0.01%) and nears the plane as ell falls (1.43, 1.0, 0.69m)",
        all(len(c["ys"]) == 3 and (max(c["ys"]) - min(c["ys"])) / c["y_s"] < 0.07 for c in fin)
        and B4_YB > fin[0]["y_s"] > fin[1]["y_s"] > fin[2]["y_s"] and 0.67 < fin[2]["y_s"] < 0.71)
    chk("F2 Pringsheim: at every ell C~'s coefficients keep one sign from order 24 to 32 and the root test sits within "
        "12% above y_s", all(c["sign"] and 1.0 <= c["root"] / c["y_s"] < 1.12 for c in d["cols"]))
    chk("F2: K reaches 30 times the black string's at a depth y_K < y_s that three Padé orders fix to 2%",
        all(max(c["yK"]) < min(c["ys"]) and (max(c["yK"]) - min(c["yK"])) / min(c["yK"]) < 0.02 for c in d["cols"]))
    chk("F3: down the column the hold reaching y_K takes under 20 clocks (three orders within 1%), and reaching 0.95 y_s "
        "under 25 (within 3%, the lapse A positive all the way, K there 1e5 or more at finite ell), at every ell -- against the "
        "write's 2.0e5; control: at ell = infinity the column reaches K = 100 no earlier than b4_static.py's 14.9-clock "
        "minimum over paths",
        all(max(c["T"]) < 20 and (max(c["T"]) - min(c["T"])) / min(c["T"]) < 0.01
            and max(c["T95"]) < 25 and (max(c["T95"]) - min(c["T95"])) / min(c["T95"]) < 0.03
            and min(c["Amin"]) > 0 for c in d["cols"])
        and all(min(c["K95"]) > 1e5 for c in fin)
        and c0["T100"] >= B4_K100 and max(max(c["T95"]) for c in d["cols"]) < 1e-3 * d["t_gas"])
    chk("F5 (exact, r = 3m): on a closing plane rho + p_r = R4_kk (y_w + 3 y_w^2/ell) + O(y_w^3) at ell = 2m, m, m/2 "
        "-- the warp and any tension cancel; R4_kk < 0",
        all(w[0] == 0 and w[1] == 0 and w[2] == 0 and w[3] < 0 for w in d["walls"].values()))
    chk("F5: rho + p_r < 0 at r = 2.15m-32m for y_w = y_s/4 and y_s/2 at every finite ell (far columns: two "
        "truncations within 0.1%)",
        all(x < 0 for c in fin for x in c["wall_215"])
        and all(v < 0 and conv for e in d["far"] for (_, _, v, conv) in d["far"][e]))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
