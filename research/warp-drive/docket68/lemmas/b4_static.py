#!/usr/bin/env python3
"""b4_static.py -- Warp Theorem lemma B4b: the static bulk of eq. (17) past its series, and how long a hold it carries.

M, item 153: "No. Finish B4 in full please".  b4_regular.py left B4b at a necessary condition the Taylor series could
not reach: during the hold the plane carries eq. (17), static, so (in a locally analytic class) the bulk inside the
hold's double cone is the static local bulk, and it must be regular there.  This instrument takes the static bulk past
the series and decides that condition.

  S1 THE EXACT SERIES TO HIGH ORDER (computed; checked).  The same equations as bulk/bulkseries.py solve() (imported
      by path for the check, not copied: the check is exact equality), carried as a two-variable Taylor series in
      (r - r_c, y) with exact rational arithmetic (python-flint fmpq_poly).  Order 60 in y takes about a minute at a
      point, against 30 min for order 12 symbolically.  Checks: equal to bulkseries.solve through y^6, flat and at
      ell = r0, coefficient by coefficient and in its r-derivatives; control: Schwarzschild data give the black string,
      e^{-y} exactly through y^20
  S2 THE STATIC BULK HAS A CURVATURE SINGULARITY ABOVE THE THROAT (computed; numerical evidence, not a bound).  In the
      flat limit (ell >> r0 -- the regime measurement leaves above r0), at r = 2.15m: the Padé approximants of A, B, C
      in s = y^2, at seven orders up to order 80, put an interlacing cut of poles and zeros on the real axis starting at
      the same point -- y_b = 2.507m (order 60), 2.5025m (order 80); Domb-Sykes and a D-log Padé, independent, give
      2.48-2.49m: a branch point at y_b = 2.49-2.50m.  A, B, C stay finite and positive there, and K -- agreeing between
      Padé orders to 1% up to 2.43m at order 60 and 2.46m at order 80 -- rises 224 (2.30m), 1,480 (2.40m), 3,892
      (2.43m), 1.9e4 (2.46m): K ~ (y_b - y)^-p with p ~ 2.5-3, divergent either way.  The metric is finite, the
      curvature diverges: a curvature singularity at finite proper depth.  (Order 80 is recorded; the
      selftest re-runs order 60, about a minute.)  Near the throat (r = 2.02-2.2m) every column shows K in the thousands
      to tens of thousands at 2.4-2.5m; from r = 2.35m out, K stays below 2 to the grid's verified depth.  At r = 2.02m
      A and B alternate in sign in y^2 through order 60 (singularities at imaginary y); at r = 2.15m only through s^7
      and s^12, the tails then of one sign (Pringsheim-consistent with the real branch point)
  S3 HOW LONG A HOLD THE BULK CARRIES (computed from the banked grid, b4_static.json).  The static bulk on 32 radii
      (2.005m to 32m), y to 12-16m, by Padé [15/15] in y^2; a point counts only where [14/15] and [15/15] agree (A, B, C
      to 1e-4, K to 1%) -- a convergence heuristic, not a bound.  The hold's double cone is computed in full -- light
      from the plane at any r, by Dijkstra in the optical metric (B dr^2 + dy^2)/A of the static bulk, far time -- on a
      refined graph (the columns interpolated linearly in r, long stencils), checked converged between two refinements;
      between two columns a point counts as verified only below the lower of their tops.  (First written on the 25 bare
      columns with a 16-move stencil, which cannot follow oblique paths and overstated the times: 13.0 clocks; the
      verifier's converged figure was 11.9 by column tops and 11.3 counting the strips.)
        * Holds below 11.28 clocks (11.32 at twice the resolution) keep their whole computed double cone inside the
          verified region, K at most 2.7 there against 1.29 on the plane at the throat -- REGULAR and Padé-stable there
          (not a certificate: a heuristic agreement of orders).  The binding point is r = 2.59m, y = 2.84m.  The strip r < 2.005m (the cone only
          0.28m deep at r = 2.005m, the static chart degenerating at the throat) and r > 32m (5.4m deep at r = 32m,
          inside its verified 16m; K falls as ~m^2/r^6, 6e-8 at r = 32m) are not computed
        * Between 11.3 clocks and the singular surface the bulk is undecided.  K >= 100, finite, is reached from 14.9
          clocks (a large curvature, not a failure); the verified layer just beneath the singular surface (K 10^2-10^3,
          r = 2.13-2.17m) from 15.3; the surface itself (y_b = 2.49-2.50m at r = 2.15m), continuing A past the verified
          tops, by about 18 clocks along oblique paths (the verifier's figure)
        * O3's per-bit 28.48 clocks reaches the singular surface
      Control: away from the throat, at r = 4m, the column is verified to 10.1m with K <= 0.014 throughout
  S4 WHAT THIS DOES TO THE THEOREM (deduced).  The bulk refutes a conjunction: H-ONE-STEP-PER-BIT (the per-bit write,
      which forces 28.48 clocks), eq. (17) held exactly and statically through the hold, the flat limit, the board's
      locally analytic class near the hold, and Padé continuation.  Of these the board withdraws H-ONE-STEP-PER-BIT, its
      own reading of the write; the others carry the rest of the theorem.  H-HOLD-AT-BOUND is not refuted by itself: kept
      against the bounds that remain, it would set the hold at about 1/(2 xi) clocks (below); the board withdraws it by
      choice, and O3 asks only that the hold lie in the window.  The READ bounds that remain: Margolus-Levitin on the
      whole register, h/(4E) = (2 pi^2/ln2)/N clocks; Bremermann's bound as Bekenstein gives it (quant-ph/0311049 eq.
      (26), p.10: "we shall take xi = 10 for illustration", "at some large value"), N bits need >= 1/(2 xi) clocks --
      0.05 clocks at xi = 10 -- applying a channel-rate bound to the register write being the board's mapping.  The
      window is [max(h/(4E), 1/(2 xi)), ~11.3 clocks).  M's 136 E, "instantaneous or near instantaneous", is consistent with it
      and does not choose between it and the per-bit figure
  NOT DECIDED HERE: whether the opening and closing themselves -- non-static, and so non-analytic somewhere -- evolve
      regularly in five dimensions (H-EVOLUTION), and whether data beyond the cone join the untouched exterior
      (H-GLUING).  At linear order around the static bulk, Holmgren's theorem (analytic coefficients, solutions of any
      regularity; standard, not READ) closes the non-analytic escape inside the cone -- uniqueness only, not existence
      or stability: the static y-problem is elliptic in (r, y) and Hadamard-ill-posed; the evolution itself is a
      nonlinear five-dimensional initial-boundary problem (B4d)
Needs python-flint (pip install python-flint), sympy, numpy, mpmath.  Imports bulk/bulkseries.py by path.
python3 b4_static.py [--selftest] [--regenerate]   (selftest ~4 min; regenerate ~40 min)
"""
import contextlib
import heapq
import importlib.util
import io
import json
import math
import os
import pickle
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
BANK = os.path.join(HERE, "b4_static.json")
HOLD_PER_BIT = 2 * math.pi**2 / math.log(2)          # O3's per-bit figure, 28.4777 clocks
RADII = ["401/200", "201/100", "101/50", "51/25", "103/50", "52/25", "21/10", "53/25", "107/50", "54/25", "109/50", "11/5", "111/50", "9/4",
         "23/10", "47/20", "12/5", "5/2", "13/5", "14/5", "3", "33/10", "18/5", "4", "5", "6", "8", "10", "12", "16", "24", "32"]


def _flint():
    import flint
    return flint


# ------------------------------------------------------------------------------------------------ S1 the exact series
def _eq17(r):
    return 1 - 2 / r, (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)


def _schwarzschild(r):
    return 1 - 2 / r, 1 - 2 / r


def solve(rc, N, e=Fr(0), h=None, data=_eq17):
    """Exact Taylor coefficients of A, B, C at r = rc through y^N: co[X][j] is a rho-polynomial (r = rc + h rho)."""
    fl = _flint()
    P, Q = fl.fmpq_poly, fl.fmpq

    def tr(p, R):
        return p.truncate(R) if p.length() > R else p

    def mul(a, b, R):
        return a.mul_low(b, R)

    def inv1(a, R):
        g = P([1 / a[0]])
        n = 1
        while n < R:
            n = min(2 * n, R)
            g = tr(g * (2 - tr(a, n) * g), n)
        return g

    def smul(a, b, R, K):
        return [sum((mul(a[i], b[j - i], R) for i in range(j + 1)), P()) for j in range(K + 1)]

    def sinv(a, R, K):
        g0 = inv1(a[0], R)
        g = [g0]
        for j in range(1, K + 1):
            s = sum((mul(a[i], g[j - i], R) for i in range(1, j + 1)), P())
            g.append(-mul(g0, s, R))
        return g

    rc = sp.Rational(rc)
    h = sp.Rational(h) if h is not None else (rc - 2) * sp.Rational(4, 5)
    hq = Q(int(h.p), int(h.q))
    eq = Q(e.numerator, e.denominator)
    M = 2 * N + 6
    rho = sp.Symbol("rho")
    F, H = data(rc + h * rho)
    co = {}
    for X, f in (("A", F), ("B", 1 / H), ("C", (rc + h * rho) ** 2)):
        ser = sp.series(f, rho, 0, M + 1).removeO()
        p = P([Q(int(sp.Rational(ser.coeff(rho, i)).p), int(sp.Rational(ser.coeff(rho, i)).q)) for i in range(M + 1)])
        co[X] = [p, -2 * eq * p]
    half, qtr = Q(1, 2), Q(1, 4)
    for k in range(N - 1):
        R = 2 * (N - k) + 4
        K = k
        T = {X: [tr(c, R) for c in co[X][:K + 2]] for X in "ABC"}
        hX = {"A": [-c for c in T["A"]], "B": T["B"], "C": T["C"]}
        hp = {X: ([hX[X][j + 1] * (j + 1) for j in range(K + 1)]) for X in "ABC"}
        hK = {X: hX[X][:K + 1] for X in "ABC"}
        inv = {X: sinv(hK[X], R, K) for X in "ABC"}
        m = lambda a, b: smul(a, b, R, K)
        add = lambda *xs: [sum(v, P()) for v in zip(*xs)]
        sc = lambda c, a: [v * c for v in a]
        dr = lambda a: [tr(p.derivative() / hq, R) for p in a]
        kk = {X: sc(half, m(hp[X], inv[X])) for X in "ABC"}
        Ktr = add(kk["A"], kk["B"], sc(2, kk["C"]))
        A, Bm, C = T["A"][:K + 1], T["B"][:K + 1], T["C"][:K + 1]
        iA, iB, iC = sc(-1, inv["A"]), inv["B"], inv["C"]
        A1, B1, C1 = dr(A), dr(Bm), dr(C)
        A2, C2 = dr(A1), dr(C1)
        iBB, iAB = m(iB, iB), m(iA, iB)
        Rtt = add(sc(half, m(A2, iB)), sc(-qtr, m(m(A1, B1), iBB)), sc(-qtr, m(m(A1, A1), iAB)),
                  sc(half, m(m(A1, C1), m(iB, iC))))
        Rrr = add(sc(-half, m(A2, iA)), sc(qtr, m(m(A1, A1), m(iA, iA))), sc(qtr, m(m(A1, B1), iAB)), sc(-1, m(C2, iC)),
                  sc(half, m(m(C1, C1), m(iC, iC))), sc(half, m(m(B1, C1), m(iB, iC))))
        Rth = add([P([1])] + [P()] * K, sc(-half, m(C2, iB)), sc(qtr, m(m(B1, C1), iBB)), sc(-qtr, m(m(A1, C1), iAB)))
        Rd = {"A": Rtt, "B": Rrr, "C": Rth}
        for X in "ABC":
            rhs = add(Rd[X], sc(half, m(m(hp[X], hp[X]), inv[X])), sc(-half, m(Ktr, hp[X])), sc(4 * eq * eq, hK[X]))
            val = rhs[k] * Q(2, (k + 2) * (k + 1))
            co[X].append(-val if X == "A" else val)
    return co, h


def coeff(co, X, i, j, h):
    """d^i/dr^i of the y^j coefficient at r_c, exactly."""
    p = co[X][j]
    c = p[i] if i < p.length() else 0
    f = Fr(int(c.p), int(c.q)) if c != 0 else Fr(0)
    return f * math.factorial(i) / Fr(int(h.p), int(h.q)) ** i


def series(rc, N, e=Fr(0), data=_eq17):
    co, h = solve(rc, N, e, data=data)
    return {X: {i: [coeff(co, X, i, j, h) for j in range(N + 1)] for i in range(3)} for X in "ABC"}


def _bulkseries():
    spec = importlib.util.spec_from_file_location("b4s_bulkseries", os.path.join(D68, "bulk", "bulkseries.py"))
    mod = importlib.util.module_from_spec(spec)
    saved = list(sys.argv)
    sys.argv = ["x"]
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    sys.argv = saved
    return mod


def check_against_owner(order=6):
    bs = _bulkseries()
    r = bs.r
    F, H = _eq17(r)
    worst = 0
    for e in (Fr(0), Fr(1, 2)):
        co = bs.solve(F, H, order, sp.Rational(e.numerator, e.denominator))
        S = series("41/20", order, e)
        for X in "ABC":
            for i in range(3):
                for j in range(order + 1):
                    ex = sp.Rational(sp.diff(sp.sympify(co[X][j]), r, i).subs(r, sp.Rational(41, 20)))
                    if Fr(int(ex.p), int(ex.q)) != S[X][i][j]:
                        worst += 1
    return worst


# ------------------------------------------------------------------------------------------------ Padé and K
def pade(c, L, M):
    A = sp.Matrix(M, M, lambda i, j: c[L + 1 + i - (j + 1)] if L + 1 + i - (j + 1) >= 0 else 0)
    b = sp.Matrix(M, 1, lambda i, _: -c[L + 1 + i])
    qv = A.LUsolve(b)
    q = [Fr(1)] + [Fr(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in qv]
    p = [sum(q[j] * c[k - j] for j in range(0, min(k, M) + 1)) for k in range(L + 1)]
    return p, q


def kretschmann():
    """The Kretschmann formula of b4_regular.py (imported by path)."""
    spec = importlib.util.spec_from_file_location("b4s_regular", os.path.join(HERE, "b4_regular.py"))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    K, _ = mod.kretschmann()
    return K


def branch_and_K(rc, N, ys, K=None):
    """Real-axis Padé pole-zero cut start (A and C) and K at the given y, two Padé orders, flat limit."""
    K = K if K is not None else kretschmann()
    names = sorted(K.free_symbols, key=str)
    Kf = sp.lambdify(names, K, "mpmath")
    S = series(rc, N)
    n = N // 2
    orders = [(n // 2 - 1, n // 2), (n // 2, n // 2)]
    starts = []
    for o in orders:
        for X in "AC":
            p, q = pade(S[X][0][0::2], *o)
            roots = np.roots([float(v) for v in reversed(q)])
            real = sorted(math.sqrt(z.real) for z in roots if abs(z.imag) < 1e-8 * abs(z) and z.real > 0)
            if real:
                starts.append(real[0])
    mp.mp.dps = 30
    vals = []
    for o in orders:
        F = {(X, i): pade(S[X][i][0::2], *o) for X in "ABC" for i in range(3)}

        def ev(pq, y2):
            pp, qq = pq
            return (mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(pp)], y2)
                    / mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(qq)], y2))
        row = []
        for y in ys:
            env = {}
            yy = mp.mpf(y)
            for X in "ABC":
                for i in range(3):
                    f = lambda t, X=X, i=i: ev(F[(X, i)], t * t)
                    env[X + ("_" + "r" * i if i else "")] = f(yy)
                    if i < 2:
                        env[X + "_" + "r" * i + "y"] = mp.diff(f, yy, 1)
                    if i == 0:
                        env[X + "_yy"] = mp.diff(f, yy, 2)
            row.append(float(Kf(*[env[str(nm)] for nm in names])))
        vals.append(row)
    return {"cut_start": min(starts) if starts else None, "starts": starts, "K": vals}


# ------------------------------------------------------------------------------------------------ S3 the hold's cone
def _fine(bank, nsub, ystep):
    """Columns interpolated linearly in r; between two columns a point is verified only below the lower top."""
    rs = sorted(bank["r"], key=lambda k: float(Fr(k)))
    rv = [float(Fr(k)) for k in rs]
    cols = [bank["cols"][k] for k in rs]
    dy = bank["dy"] * ystep
    R, A, B, K, top = [], [], [], [], []
    for i in range(len(rs)):
        last = i == len(rs) - 1
        for k in range(1 if last else nsub):
            if last:
                k = 0
            c0 = cols[i]
            c1 = cols[i] if last else cols[i + 1]
            t = 0.0 if (last or k == 0) else k / nsub
            n = len(c0["A"]) if t == 0.0 else min(len(c0["A"]), len(c1["A"]))
            n = (n - 1) // ystep + 1
            if t == 0.0:
                c1 = c0
            a0, a1 = np.array(c0["A"])[::ystep][:n], np.array(c1["A"])[::ystep][:n]
            b0, b1 = np.array(c0["B"])[::ystep][:n], np.array(c1["B"])[::ystep][:n]
            k0, k1 = np.array(c0["K"])[::ystep][:n], np.array(c1["K"])[::ystep][:n]
            R.append(rv[i] + (0 if last else (rv[i + 1] - rv[i]) * t))
            A.append((1 - t) * a0 + t * a1)
            B.append((1 - t) * b0 + t * b1)
            K.append((1 - t) * k0 + t * k1)
            top.append(n)
    return np.array(R), A, B, K, np.array(top), dy


def cone(bank, nsub=12, ystep=2, M=4):
    """Least far-time T from the plane (any r) to every verified point, by Dijkstra (scipy) on the refined graph."""
    from math import gcd
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import dijkstra
    R, A, B, K, top, dy = _fine(bank, nsub, ystep)
    nr = len(R)
    off = np.concatenate([[0], np.cumsum(top)])
    nn = int(off[-1]) + 1                                   # + one source node
    src = nn - 1
    rows, colsx, w = [], [], []
    moves = [(di, dj) for di in range(0, M + 1) for dj in range(-M, M + 1)
             if (di, dj) != (0, 0) and gcd(di, abs(dj)) == 1 and (di > 0 or dj > 0)]
    for i in range(nr):
        for di, dj in moves:
            a = i + di
            if a >= nr:
                continue
            na, ni = top[a], top[i]
            j = np.arange(ni)
            b = j + dj
            okm = (b >= 0) & (b < na)
            j, b = j[okm], b[okm]
            if len(j) == 0:
                continue
            Am = 0.5 * (A[i][j] + A[a][b])
            Bm = 0.5 * (B[i][j] + B[a][b])
            L = np.sqrt((Bm * (R[a] - R[i]) ** 2 + (dj * dy) ** 2) / Am)
            rows.append(off[i] + j)
            colsx.append(off[a] + b)
            w.append(L)
    rows = np.concatenate(rows + [np.full(nr, src)])
    colsx = np.concatenate(colsx + [off[:-1]])
    w = np.concatenate(w + [np.full(nr, 1e-300)])
    G = coo_matrix((w, (rows, colsx)), shape=(nn, nn)).tocsr()
    dist = dijkstra(G, directed=False, indices=src)
    T = [dist[off[i]:off[i + 1]] for i in range(nr)]
    ymax_idx = max(top)
    edge = [(T[i][top[i] - 1], i) for i in range(1, nr - 1) if top[i] < ymax_idx]
    tc, ic = min(edge)
    out = {"t_cert": 2 * tc, "cert_r": R[ic], "cert_y": (top[ic] - 1) * dy, "T": T, "R": R, "top": top, "K": K,
           "dy": dy}
    out["Kmax_in"] = lambda hold: max(float(np.max(np.where(T[i] <= hold / 2, K[i], -np.inf))) for i in range(nr))
    for Kc in (1e2, 1e3, 1e4):
        cand = [T[i][K[i] >= Kc].min() for i in range(nr) if (K[i] >= Kc).any()]
        out["t_fail_%d" % int(math.log10(Kc))] = 2 * min(cand) if cand else float("inf")
    near = [i for i in range(nr) if 2.13 <= R[i] <= 2.17]
    out["t_sing_est"] = 2 * min(T[i][top[i] - 1] for i in near) if near else float("nan")
    out["inner_depth"] = lambda hold: (np.sum(T[0] <= hold / 2) - 1) * dy
    out["outer_depth"] = lambda hold: (np.sum(T[-1] <= hold / 2) - 1) * dy
    return out


def regenerate():
    K = kretschmann()
    names = sorted(K.free_symbols, key=str)
    Kn = sp.lambdify(names, K, "numpy")
    ys = np.round(np.arange(0, 16.0001, 0.02), 4)
    y2 = np.poly1d([1, 0, 0])
    cols = {}
    for rc in RADII:
        S = series(rc, 60)
        per = []
        for o in [(14, 15), (15, 15)]:
            Fv = {}
            for X in "ABC":
                for i in range(3):
                    p, q = pade(S[X][i][0::2], *o)
                    Pp = np.poly1d([float(v) for v in reversed(p)])(y2)
                    Qq = np.poly1d([float(v) for v in reversed(q)])(y2)
                    Fv[X + ("_" + "r" * i if i else "")] = Pp(ys) / Qq(ys)
                    if i < 2:
                        n1 = Pp.deriv() * Qq - Pp * Qq.deriv()
                        Fv[X + "_" + "r" * i + "y"] = n1(ys) / Qq(ys) ** 2
                    if i == 0:
                        n1 = Pp.deriv() * Qq - Pp * Qq.deriv()
                        Fv[X + "_yy"] = (n1.deriv()(ys) * Qq(ys) - 2 * n1(ys) * Qq.deriv()(ys)) / Qq(ys) ** 3
            per.append({"A": Fv["A"], "B": Fv["B"], "C": Fv["C"], "K": Kn(*[Fv[str(nm)] for nm in names])})
        a, b = per
        rel = lambda u, v: np.abs(u - v) / np.maximum(np.abs(v), 1e-300)
        st = ((rel(a["A"], b["A"]) < 1e-4) & (rel(a["B"], b["B"]) < 1e-4) & (rel(a["C"], b["C"]) < 1e-4)
              & (rel(a["K"], b["K"]) < 1e-2) & (b["A"] > 0) & (b["B"] > 0) & (b["C"] > 0))
        top = int(np.argmax(~st)) if (~st).any() else len(ys)
        r8 = lambda v: [float("%.8g" % x) for x in v[:top]]
        cols[rc] = {"top": top, "A": r8(b["A"]), "B": r8(b["B"]), "K": r8(b["K"])}
    json.dump({"note": "regenerated by lemmas/b4_static.py --regenerate", "dy": 0.02, "N": 60, "r": RADII,
               "cols": cols}, open(BANK, "w"), separators=(",", ":"))


def compute(live=True, nsub=12, ystep=2):
    bank = json.load(open(BANK))
    cn = cone(bank, nsub=nsub, ystep=ystep)
    tc = cn["t_cert"]
    d = {"cone": cn, "Kmax_cert": cn["Kmax_in"](tc - 1e-9), "Kmax_o3": cn["Kmax_in"](HOLD_PER_BIT),
         "K_plane_throat": bank["cols"]["101/50"]["K"][0], "inner_depth": cn["inner_depth"](tc),
         "outer_depth": cn["outer_depth"](tc)}
    i4 = int(np.argmin(np.abs(cn["R"] - 4.0)))
    d["r4_top_y"] = (cn["top"][i4] - 1) * cn["dy"]
    d["r4_Kmax"] = float(np.max(cn["K"][i4]))
    if live:
        d["converged"] = compute(live=False, nsub=2 * nsub, ystep=1)["cone"]["t_cert"]
        d["owner_mismatches"] = check_against_owner(6)
        bs = series("3", 20, Fr(1, 2), data=_schwarzschild)
        d["black_string"] = all(abs(float(bs["A"][0][j]) - (1 / 3) * (-1) ** j / math.factorial(j)) < 1e-15
                                and abs(float(bs["C"][0][j]) - 9 * (-1) ** j / math.factorial(j)) < 1e-13
                                for j in range(21))
        d["sing"] = branch_and_K("43/20", 60, [2.30, 2.40, 2.43, 2.46])
    return d


def report(d):
    cn = d["cone"]
    print("b4_static.py -- Warp Theorem lemma B4b: the static bulk past its series\n")
    if "owner_mismatches" in d:
        print("S1 exact series against bulkseries.solve through y^6 (flat and ell = r0): %d mismatches; black string: %s"
              % (d["owner_mismatches"], d["black_string"]))
        s = d["sing"]
        print("S2 r = 2.15m, order 60: real-axis Padé cut starts at y = %.4f (%s); K at 2.30/2.40/2.43/2.46: %s / %s"
              % (s["cut_start"], ", ".join("%.4f" % v for v in s["starts"]),
                 ", ".join("%.5g" % v for v in s["K"][0]), ", ".join("%.5g" % v for v in s["K"][1])))
        print("S3 refinement check: t_cert %.2f (nsub 12, dy 0.04) against %.2f (nsub 24, dy 0.02)"
              % (cn["t_cert"], d["converged"]))
    print("S3 regular (Padé-stable): any hold < %.2f clocks (binding point r = %.3f m, y = %.2f m); max K in that cone "
          "%.3f (plane at the throat %.3f)" % (cn["t_cert"], cn["cert_r"], cn["cert_y"], d["Kmax_cert"],
                                              d["K_plane_throat"]))
    print("   K >= 1e2 from %.2f clocks, >= 1e3 from %.2f, >= 1e4 from %.2f; the layer beneath the singular surface "
          "from ~%.1f (the surface ~18); the "
          "per-bit 28.48: max K in its cone (verified region) %.4g" % (cn["t_fail_2"], cn["t_fail_3"], cn["t_fail_4"],
                                                                    cn["t_sing_est"], d["Kmax_o3"]))
    print("   uncomputed strips at t_cert: r < 2.005 (cone %.2f m deep at r = 2.005), r > 32 (%.2f m deep at r = 32)"
          % (d["inner_depth"], d["outer_depth"]))
    print("   control r = 4m: verified to %.2f m, max K %.4f" % (d["r4_top_y"], d["r4_Kmax"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute(live=True)
    cn = d["cone"]
    chk("S1: the exact solver equals bulkseries.solve through y^6, flat and ell = r0, with its r-derivatives",
        d["owner_mismatches"] == 0)
    chk("S1 control: Schwarzschild data give the black string, e^{-y} exactly through y^20", d["black_string"])
    s = d["sing"]
    k60a, k60b = s["K"]
    chk("S2: at r = 2.15m the Padé cut starts on the real axis at y_b ~ 2.50m (order 60; order 80 gives 2.5025m)",
        s["cut_start"] is not None and abs(s["cut_start"] - 2.505) < 0.01)
    fit = math.log(k60b[2] / k60b[0]) / math.log((s["cut_start"] - 2.30) / (s["cut_start"] - 2.43))
    chk("S2: K rises 224 -> 1,480 -> 3,892 (two orders within 1% to 2.43m at order 60), K ~ (y_b - y)^-p, p ~ 2.5-3.5",
        all(abs(a - b) < 0.01 * abs(b) for a, b in zip(k60a[:3], k60b[:3])) and abs(k60b[0] - 224.1) < 1
        and abs(k60b[1] - 1480.1) < 5 and 2.3 < fit < 3.6)
    chk("S3: the refined cone is converged -- t_cert within 3% between two refinements",
        abs(cn["t_cert"] - d["converged"]) < 0.03 * d["converged"])
    chk("S3: holds below t_cert keep their computed cone in the verified region, K <= 5 there; t_cert between 10 and 12",
        10 < cn["t_cert"] < 12 and d["Kmax_cert"] < 5)
    chk("S3: the per-bit hold (28.48 clocks) reaches K >= 1e4 inside the verified region, and the layer beneath the "
        "singular surface",
        d["Kmax_o3"] > 1e4 and cn["t_sing_est"] < HOLD_PER_BIT)
    chk("S3: the uncomputed strips are shallow at t_cert -- under 0.5m at r = 2.005; at r = 32 within its verified column",
        d["inner_depth"] < 0.5 and d["outer_depth"] < (cn["top"][-1] - 1) * cn["dy"])
    chk("S3 control: away from the throat (r = 4m) the column is verified to 10.1m with K <= 0.014 throughout",
        d["r4_top_y"] > 10 and d["r4_Kmax"] < 0.015)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report(compute(live="--quick" not in sys.argv))
