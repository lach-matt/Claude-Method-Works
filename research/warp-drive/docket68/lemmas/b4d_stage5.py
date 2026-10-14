#!/usr/bin/env python3
"""b4d_stage5.py -- Warp Theorem lemma B4d, stage 5: the corridor of fixed size through the write (M-RULINGS items
161-163).  Computed, READ and deduced; verified once (findings applied, B4D-STAGE5.md History); not seated.  First
headed "... not verified; not seated" -- and first finding no way open on the board's models, before its verifier found
that on the negative-tension side (139) the bulk has no singular surface.

M's words (verbatim in the rulings file): item 163 "All together, one whole" (the README carried in, held as one whole;
the gas bound stands); item 162 "The throat doesn't change size"; item 161 "my inclination is yes" (the corridor stays
regular while the README passes); item 160 "the corridor and the opening are the same object"; item 115 (c) "The README
itself" (the inflow); item 136 G (the README is the energy); item 139 (position 2's plane has negative tension); clause
(B) (the plane carries no matter); items 117/120 ("the NEC only ever appears to break, but never does").

  F1 WHERE THE INFLOW'S ENERGY GOES IS A READING (arithmetic; the readings are the board's).  On the plane, in the
     Vaidya form of opening.py, the trapping radius is r = 2 m(v), so 162's fixed size is dm/dv = 0.  By 115 (c) and
     136 G the README's energy flows in, over at least 1.997e5 clocks (o3_write.py, which 163 keeps).  Three readings
     reconcile them, none forced: an equal outflow to position 2 (H-THROUGH-FLOW -- against 163's "held as a single
     whole" and clause (E)'s release at the closing); the mass set at the opening (H-MASS-AT-OPENING); the energy carried
     into the bulk (158 (4), left to the math).  The verdict needs none of them: the inflow's average is at most E/T =
     5.0e-6 of m per clock, so some ~20-clock window carries no more than that (pigeonhole), which is all F4 uses.
  F2 ON THE POSITIVE-TENSION SIDE THE STATIC BULK STILL HAS A SINGULAR SURFACE AT EVERY ell TESTED, NEARER THE PLANE AS
     ell FALLS (computed; numerical evidence, not a bound).  b4_static.py's exact series at r = 2.15m, order 32 in y,
     with ell = 1/e finite (the Randall-Sundrum tension; the series is not even in y).  The warp is divided out, X~ = X
     e^(2y/ell) (entire and never zero, so X~ has X's singularities; constant for the black string) -- a modest
     improvement in the Padé spread at ell = 2m and m/2, none at m.  Spurious pole-zero pairs (Froissart doublets) are
     divided out before evaluation.  For each ell:
       * the nearest singularity of C~ by the positive axis, three Padé orders -- a scale for the depth.  At ell = m, m/2,
         m/4 a real pole; at ell = 2m a conjugate pair at 1.43 +- 0.05i (its verifier, at order 48: 1.4136 +- 0.053i,
         with a real pole near 1.49 suggested, not resolved).  Across orders 32-48 (the verifier's): 1.41-1.43, 1.00-1.02,
         0.67-0.69m at ell = 2m, m, m/2; 0.43m at m/4 (order 32);
       * C~'s coefficients keep one sign from order 24 to 32: Pringsheim-consistent (Pringsheim's theorem, standard, not
         READ, needs all but finitely many) -- at ell = 2m they turn negative from order 36 (the verifier's), as the
         complex pair requires;
       * K along the column against the black string at the same ell, K_bs = 40/ell^4 + 48 m^2 e^(4y/ell)/r^6
         (Chamblin-Hawking-Reall's form, standard, not READ; derived by the verifier; checked below): the depth y_K at
         which K reaches 30 K_bs, and K at 0.9 y_s, both order-stable.  At 0.9 y_s K is 1.0e4, 2.7e4, 4.8e5, 1.6e6 at
         ell = 2m, m, m/2, m/4 -- 1,100, 470, 670, 150 times K_bs.  At 0.95 y_s K is larger but order-dependent.
     Not the flat limit's cut: at finite ell B (g_rr) falls toward 0 near y_s, which a Gaussian-normal caustic would
     also show -- K arbitrates, and it rises as (y_s - y)^-p with p ~ 4 to hundreds-to-thousands of K_bs, which a smooth
     caustic does not do (the verifier's fit).
     Controls: (i) ell = infinity reproduces b4_static.py's surface, 2.58 at order 32 against 2.50 at order 80 (3% high);
     (ii) Schwarzschild data at ell = m: the warp-divided series terminates -- the black string, no singular surface --
     and the instrument's K equals K_bs to 2e-16.
     STRUCTURAL heuristic: the surface nearing the plane as ell falls is KSCALE's closure seen in the bulk -- for r0 >>
     ell the plane is four-dimensional GR to O(ell^2/r0^2) (Figueras-Wiseman p.4, READ in b4d_stage2.py), and eq. (17)'s
     deficit is an O(1) Weyl datum; at the values tested r0/ell <= 8, so this is a heuristic, not a derivation.
  F3 THE HOLD THAT REACHES IT (computed).  Light from the plane down the column at r = 2.15m, in the static bulk's far
     time: T = 2 int dy/sqrt(A) -- the double cone of b4_static.py S3 along one path, an upper bound on the earliest hold
     containing the point (the minimum over paths is no later).  To 0.9 y_s: 16.0, 13.0, 10.9, 7.8 clocks at ell = 2m,
     m, m/2, m/4 (20.2 at ell = infinity, where K is 330 there); three orders within 1%, the lapse positive (>= 3e-4),
     the series still convergent there (the verifier's partial sums at orders 32-40 agree).  Control: at ell = infinity
     the column reaches K = 100 at 19.2 clocks, no earlier than b4_static.py's 14.9 (its minimum over paths).
  F4 OVER THAT HOLD THE PLANE'S DATA ARE EQ. (17)'S (a reading, H-QUASI-STATIC-CORRIDOR, the board's).  In a 20-clock
     window chosen by F1's pigeonhole the inflow moves at most ~1e-4 of the mass; read inside the locally analytic class,
     the bulk in that window's cone is the static bulk to that order.  The y-problem is elliptic and Hadamard-ill-posed,
     so this continuity -- a bound on the 1e-4 perturbation in an analytic norm, since a mode of wavenumber k grows like
     e^(ky) -- is the hypothesis, not a theorem.  Only the first such window matters; secular effects over
     2e5 clocks do not enter.  The opening's own transient is no escape: any later 20-clock window of eq. (17) data fixes
     its own cone.
  F5 A SECOND PLANE BELOW THE SURFACE CARRIES NEC-BREAKING MATTER AT FINITE ell TOO (computed; STRUCTURAL at small
     height).  A mirrored plane at y = y_w closing the bulk (b4d_stage1.py D3, at finite ell): rho + p_r = -A_y/(2A) +
     B_y/(2B) -- the warp cancels identically and any tension drops out (it is proportional to h_ab), 139's negative one
     included.  Exactly, rho + p_r = R4_kk (y_w + 3 y_w^2/ell) + O(y_w^3), R4_kk = -2m(r - 2m)/(r^2 (2r - 3m)^2) < 0
     (rational at r = 3m; derived analytically by the verifier: D'' = 6e D').  Computed negative at r = 2.15, 3, 5, 10,
     32m for y_w = y_s/4 and y_s/2 (the verifier: at r = 2.25-32m for every y_w up to 0.99 y_s).  So the plane would carry
     real matter breaking the NEC, which 117/120 rule out.
  F6 ON THE NEGATIVE-TENSION SIDE THERE IS NO SINGULAR SURFACE, ON THE EVIDENCE (computed; STRUCTURAL symmetry).  The bulk
     equations are invariant under y -> -y with e -> -e (exact: the series alternate).  So eq. (17) on a plane of
     negative tension -- 139's position-2 plane -- with the bulk on its growing-warp side has the positive side's
     singularities at negative y, behind the plane.  Computed at ell = 2m, m, m/2: K = K_bs to 4% at y = 0.5-3m (to 0.1%
     from y = m at ell = m, m/2) in three Padé orders, the lapse positive and growing: eq. (17)'s Weyl excess dies away
     and the bulk relaxes to AdS.  Its costs, named: light reaches the bulk's conformal boundary in finite far time --
     15.7, 7.6, 3.8 clocks -- so the bulk needs data there (H-BOUNDARY-DATA); and on a lone negative-tension plane
     gravity is not localized (standard Randall-Sundrum, not READ) -- against the board's four-dimensional readings
     unless a positive-tension plane bounds the bulk (127's coinciding planes, 162's one object).
  VERDICT (deduced).  The refutation narrows to one side.  With eq. (17) on a positive-tension plane, the corridor of
     161-163 does not stay regular through the write: its bulk reaches K of 1e4 or more, 100-1,100 times the black
     string's, within 8-16 clocks at every finite ell tested (2m to m/4), against 2.0e5.  The conjunction: eq. (17) on
     the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD); one mirrored plane of positive Randall-Sundrum tension
     and no matter (clause (B), H-RS2-ONE-PLANE); a vacuum bulk; B4b's locally analytic class (Holmgren at linear
     order); Padé as evidence; H-QUASI-STATIC-CORRIDOR; the far-time frame (H-HOLD-FRAME); the column r = 2.15m; the ell
     values tested; and any write longer than ~16 clocks (the gas bound's hypotheses only through that).  F5 closes a
     closing plane under 117/120.  F6 opens the other side: with eq. (17) on 139's negative-tension plane the bulk is
     regular on the evidence, at the cost of boundary data and of localized gravity -- the live route for 161.  Also
     open: H-TWO-SIDED, a curved wall, a through-flowing plane not eq. (17), a bulk outside the analytic class, README
     energy in the bulk (158 (4)), ell between and below the values tested.

Imports lemmas/b4_static.py and lemmas/o3_write.py by path.  Needs python-flint, sympy, numpy, mpmath.
python3 b4d_stage5.py [--selftest]   (selftest about 5 min)
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
ES = [Fr(0), Fr(1, 2), Fr(1), Fr(2), Fr(4)]     # e = m/ell: ell = infinity, 2m, m, m/2, m/4
ES_NEG = [Fr(-1, 2), Fr(-1), Fr(-2)]            # 139's negative tension: the growing-warp side
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
    """The nearest singularity of the Padé of c on or near the positive real axis, by its real part: a real pole, or a
    near-real conjugate pair (|Im| < 5% |z|) -- whose imaginary part is reported -- Froissart doublets (a zero within
    2e-3) dropped.  A scale for the depth, not a claim that the singular point is real."""
    p, q = _approx(c, o)
    if len(q) == 1:
        return None
    poles = np.roots([float(v) for v in reversed(q)])
    zeros = np.roots([float(v) for v in reversed(p)]) if len(p) > 1 else np.array([])
    keep = [z for z in poles if not len(zeros) or min(abs(z - zz) for zz in zeros) > 2e-3 * max(1, abs(z))]
    near = sorted((z for z in keep if abs(z.imag) < 5e-2 * abs(z) and z.real > 0), key=lambda z: z.real)
    return (near[0].real, abs(near[0].imag)) if near else None


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
        for pole, zero in dz:                     # p/q has the zero, q the pole: divide both out
            val *= (t - pole) / (t - zero)
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
    sing = [nearest_real(W["C"][0], o) for o in orders(N)]
    sing = [s for s in sing if s is not None]
    ys = [s[0] for s in sing]
    ok_sign, root = pringsheim(W["C"][0], N)
    ys_mid = float(np.median(ys))
    out = {"e": e, "ys": ys, "im": [s[1] for s in sing], "y_s": ys_mid, "sign": ok_sign, "root": root, "yK": [],
           "T": [], "T95": [], "Amin": [], "K95": [], "K90": [], "T90": [], "T100": None,
           "kbs90": k_bs(e, r, 0.9 * ys_mid)}
    for o in orders(N):
        K, A, _ = evaluator(W, e, o)
        y_k = depth_at(K, lambda y: K_FACTOR * k_bs(e, r, y), 0.0, 0.995 * min(ys))
        out["yK"].append(y_k)
        out["T"].append(float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, y_k])))
        y95 = 0.95 * ys_mid
        out["T95"].append(float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, y_k, y95])))
        out["Amin"].append(min(float(A(f * y95)) for f in np.linspace(0, 1, 41)))
        out["K95"].append(K(y95))
        y90 = 0.9 * ys_mid
        out["K90"].append(K(y90))
        out["T90"].append(float(2 * mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, min(y_k, y90), y90])))
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


# ------------------------------------------------------------------------------------------------ F6 the negative side
def mirror(e=Fr(1), N=16, rc=RC):
    """The bulk equations are invariant under y -> -y with e -> -e: C~(e) and C~(-e) coefficients alternate in sign."""
    a = warped(B4.series(rc, N, e), e, N)
    b = warped(B4.series(rc, N, -e), -e, N)
    return all(b[X][i][k] == (-1) ** k * a[X][i][k] for X in "ABC" for i in range(3) for k in range(N + 1))


def negative_side(e, N=ORDER, rc=RC, ys=(0.5, 1.0, 2.0, 3.0), Y=3.0):
    """Eq. (17) on a plane of negative tension (e < 0), bulk on its growing-warp side: K/K_bs and A down the column at
    three Padé orders, and the far time for light to the conformal boundary, 2 (int_0^Y dy/sqrt A + 1/(|e| sqrt A(Y)))
    (the tail with A ~ A(Y) e^(2|e|(y - Y)))."""
    mp.mp.dps = 40
    r = float(Fr(rc))
    W = warped(B4.series(rc, N, e), e, N)
    out = {"e": e, "ratio": [], "Amin": [], "Tb": []}
    for o in orders(N):
        K, A, _ = evaluator(W, e, o)
        out["ratio"].append([K(y) / k_bs(e, r, y) for y in ys])
        out["Amin"].append(min(float(A(y)) for y in np.linspace(0, Y, 31)))
        ae = abs(float(e))
        out["Tb"].append(float(2 * (mp.quad(lambda t: 1 / mp.sqrt(A(t)), [0, Y]) + 1 / (ae * mp.sqrt(A(Y))))))
    return out


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d5_o3write")
    t_gas = ow._num(ow.t_min(3))
    rah, rate, m, v = through_flow()
    cols = [column(e) for e in ES]
    ctl = schwarzschild_control()
    walls = {e: wall_exact(e) for e in ES[1:4]}
    far = {c["e"]: wall_far(c["e"], c["y_s"]) for c in cols[1:4]}
    neg = [negative_side(e) for e in ES_NEG]
    return {"t_gas": t_gas, "flux": 1 / t_gas, "rah": rah, "rate": rate, "m": m, "v": v, "cols": cols, "ctl": ctl,
            "walls": walls, "far": far, "neg": neg, "mirror": mirror()}


def _ell(e):
    return "inf" if e == 0 else str(1 / e)


def report(d):
    print("b4d_stage5.py -- B4d stage 5: the corridor of fixed size through the write\n")
    print("F1 trapping radius r = %s, d/dv = %s; the write >= %.4g clocks, average inflow <= %.2g of m per clock" % (
        d["rah"], d["rate"], d["t_gas"], d["flux"]))
    print("F2/F3 at r = 2.15m, positive tension (y in units of m; T in clocks):")
    for c in d["cols"]:
        print("   ell = %-4s y_s %s (|Im| %s)  one sign 24-32 %s, root test %.2f  y_K %s  T %s" % (
            _ell(c["e"]), "/".join("%.3f" % y for y in c["ys"]), "/".join("%.2f" % v for v in c["im"]), c["sign"],
            c["root"], "/".join("%.3f" % y for y in c["yK"]), "/".join("%.1f" % t for t in c["T"])))
        print("        at 0.9 y_s: K %s (K_bs %.3g), T %s;  at 0.95 y_s (order-dependent): K %s, T %s, A >= %s" % (
            "/".join("%.3g" % k for k in c["K90"]), c["kbs90"], "/".join("%.1f" % t for t in c["T90"]),
            "/".join("%.2g" % k for k in c["K95"]), "/".join("%.1f" % t for t in c["T95"]),
            "/".join("%.1e" % a for a in c["Amin"])))
    c0 = d["cols"][0]
    print("   control ell = inf: time to K = 100 down the column %.1f clocks (b4_static.py minimum over paths 14.9)"
          % c0["T100"])
    print("   control Schwarzschild at ell = m: series terminates %s, K vs K_bs worst %.1e" % d["ctl"])
    print("F5 rho + p_r on a closing plane at r = 3m: (y^0, y^1 - R4_kk, y^2 - 3 e R4_kk) =")
    for e, w in d["walls"].items():
        print("   ell = %s: %s, %s, %s (R4_kk = %s)" % (_ell(e), *w))
    for c in d["cols"][1:4]:
        print("   ell = %s at r = 2.15m, y_w = y_s/4, y_s/2: %s; r = 3, 5, 10, 32m: %s" % (
            _ell(c["e"]), ", ".join("%.3g" % x for x in c["wall_215"]),
            ", ".join("%.2g" % x[2] for x in d["far"][c["e"]])))
    print("F6 mirror y -> -y, e -> -e exact: %s" % d["mirror"])
    for g in d["neg"]:
        print("   negative tension, ell = %s: K/K_bs at y = 0.5, 1, 2, 3: %s; A >= %s; light to the boundary %s clocks" % (
            str(-1 / g["e"]), " | ".join("/".join("%.4f" % x for x in row) for row in zip(*g["ratio"])),
            "/".join("%.3g" % a for a in g["Amin"]), "/".join("%.2f" % t for t in g["Tb"])))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    cols = {c["e"]: c for c in d["cols"]}
    chk("F1 (arithmetic; the reading is the board's): the trapping radius is r = 2 m(v), so a fixed size is dm/dv = 0; "
        "the write's 1.997e5 clocks bound the inflow's average by 5.0e-6 of m per clock",
        len(d["rah"]) == 1 and sp.simplify(d["rah"][0] - 2 * d["m"]) == 0
        and sp.simplify(d["rate"] - 2 * sp.diff(d["m"], d["v"])) == 0 and 1.99e5 < d["t_gas"] < 2.0e5)
    chk("F2 control: Schwarzschild data at ell = m -- the warp-divided series terminates (the black string, no "
        "singular surface) and K equals 40/ell^4 + 48 m^2 e^(4y/ell)/r^6 to 1e-12", d["ctl"][0] and d["ctl"][1] < 1e-12)
    c0 = cols[Fr(0)]
    chk("F2 control: ell = infinity reproduces b4_static.py's singular surface (2.50m at order 80) within 5% at "
        "order 32", all(abs(y / B4_YB - 1) < 0.05 for y in c0["ys"]) and len(c0["ys"]) == 3)
    fin = [cols[e] for e in ES[1:]]
    chk("F2: at ell = 2m, m, m/2, m/4 the nearest singularity of C~ by the positive axis is found at all three Padé "
        "orders (spread under 7%) and nears the plane as ell falls (~1.43, ~1.0, ~0.69, ~0.43m); at 2m it is a "
        "conjugate pair off the axis (|Im| ~ 0.05)",
        all(len(c["ys"]) == 3 and (max(c["ys"]) - min(c["ys"])) / c["y_s"] < 0.07 for c in fin)
        and B4_YB > fin[0]["y_s"] > fin[1]["y_s"] > fin[2]["y_s"] > fin[3]["y_s"] and 0.40 < fin[3]["y_s"] < 0.45
        and min(cols[Fr(1, 2)]["im"]) > 0.02)
    chk("F2: K reaches 30 times the black string's at a depth y_K < y_s that three Padé orders fix to 2%",
        all(max(c["yK"]) < min(c["ys"]) and (max(c["yK"]) - min(c["yK"])) / min(c["yK"]) < 0.02 for c in d["cols"]))
    chk("F2/F3: at 0.9 y_s K is 1e4 or more and 100 or more times K_bs at every finite ell, three Padé orders within "
        "10%; the hold reaching it takes under 17 clocks (orders within 1%), the lapse positive throughout -- against "
        "the write's 2.0e5",
        all(min(c["K90"]) > 1e4 and min(c["K90"]) / c["kbs90"] > 100
            and (max(c["K90"]) - min(c["K90"])) / min(c["K90"]) < 0.10 and max(c["T90"]) < 17
            and (max(c["T90"]) - min(c["T90"])) / min(c["T90"]) < 0.01 and min(c["Amin"]) > 0 for c in fin)
        and max(max(c["T90"]) for c in d["cols"]) < 1e-3 * d["t_gas"])
    chk("F3 control: at ell = infinity the column reaches K = 100 no earlier than b4_static.py's 14.9-clock minimum "
        "over paths (one path bounds the minimum from above)", c0["T100"] >= B4_K100)
    chk("F5 (exact, r = 3m): on a closing plane rho + p_r = R4_kk (y_w + 3 y_w^2/ell) + O(y_w^3) at ell = 2m, m, m/2 "
        "-- the warp and any tension cancel; R4_kk < 0",
        all(w[0] == 0 and w[1] == 0 and w[2] == 0 and w[3] < 0 for w in d["walls"].values()))
    chk("F5: rho + p_r < 0 at r = 2.15, 3, 5, 10, 32m for y_w = y_s/4 and y_s/2 at ell = 2m, m, m/2 (far columns: two "
        "truncations within 0.1%)",
        all(x < 0 for c in fin[:3] for x in c["wall_215"])
        and all(v < 0 and conv for e in d["far"] for (_, _, v, conv) in d["far"][e]))
    chk("F6 (STRUCTURAL, exact): the bulk equations are invariant under y -> -y with e -> -e -- the negative-tension "
        "side's series is the positive side's with alternating signs", d["mirror"])
    chk("F6: eq. (17) on a negative-tension plane (139), bulk on the growing-warp side: K = K_bs to 4% at y = 0.5-3m "
        "(to 0.1% from y = m at ell = m, m/2), three Padé orders, lapse positive -- no singular surface on the evidence; "
        "light reaches the conformal boundary in finite far time (under 16 clocks)",
        all(abs(x - 1) < 0.04 for g in d["neg"] for row in g["ratio"] for x in row)
        and all(abs(x - 1) < 1e-3 for g in d["neg"][1:] for row in g["ratio"] for x in row[1:])
        and all(min(g["Amin"]) > 0 and max(g["Tb"]) < 16 for g in d["neg"]))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
