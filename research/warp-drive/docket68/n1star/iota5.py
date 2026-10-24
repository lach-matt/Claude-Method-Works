#!/usr/bin/env python3
"""iota5.py -- [Hin26] section 9.1 in five dimensions: the pure iota+ resonances of the linearized gauge-fixed Einstein
operator, by harmonic type, on 4+1 Minkowski (N1STAR-PROOF.md section 10.37; ROUTES-OPEN.md 4.38; D97).  Labels:
computed (exact, sympy; numerical, mpmath, where said), deduced, READ.

[Hin26] (arXiv:2606.28253v2) (9.11): N_iota+(L-bar, lam) = -2 v (v d_v - lam)(v d_v - 1 - S-bar) + v^2 L~(0)(omega,
v d_v, d_omega), v = t*/r; Definition 9.6: spec_iota+(L-bar) is "the set of poles of N_iota+(L-bar, lam)^-1 acting on
C-dot^oo(iota+; S^2 T*)", the "pure" resonances (p. 172); Proposition 9.2(2): the spectral family is invertible "For all
lam in C with Re lam < 1 + eps_ind" (p. 165); and "u_3(v, omega) := (v/(v+2))^(3/2) in ker N_iota+(box-bar_4+1, 3)
... Since u_3 has vanishing incoming data (no v^3-term), it is thus what we call a 'pure' resonant state" (p. 16).
Here the five-dimensional model by type, from lin5.py's operators, and its pure resonances.

  I1 (computed, exact) The model by type.  With t* = t - r and fields T^a r^-x u (T = t*, u of degree 0 and one
     harmonic type: lin5.py's bases and point), L-bar, box^C and box^Ups return T^(a-1) r^(-x-1) [a L1(x) u] + T^a
     r^(-x-2) [N(x) u] and no T^(a-2) term (dt* is null).  So with a = x - lam and G = sum s^x, s = t*/r, the iota+
     model is M0(D) G + s M1(D) G = 0, D = s d/ds, M0(x) = (x - lam) L1(x), M1 = N: [Hin26] (9.11) at n = 4.  M1 is
     lin5.py's own indicial matrix (Nmat, the same basis) at s0 and v1, and at gam_Ups = gam_C = 0 L1(x) = (3 - 2x) Id
     for box^C and box^Ups (s0, s1, v1) and (3 - 2x)/2 Id for L-bar (s0, s1, v1, v2, t2), 2 L-bar being box there (his
     (8.5)): the transport of the free wave.
     Control: the powers of T split with z = x1 + i x2 symbolic -- sympy's expand then moves T into denominators T x1 +
     I T x2 and the transport of the degree-p harmonics is lost, which the free-wave check catches at s1.
  I2 (computed, numerical) The connection.  z = s/(s + 2) sends the singular points s = 0, -2, oo to 0, oo, 1, so the
     Frobenius series at s = 0 (the roots of det L1: the outgoing exponents, lam itself, the stationary r^-lam, left
     out) and at s = oo (the K lowest roots of det N: [Hin26]'s E_K "from -1 times the indicial roots in Lemma 8.4 with
     non-positive real parts", p. 170) both converge at s = 2; a pure resonance is a zero of the 2K x 2K determinant of
     the two families there.  On the free 4+1 wave its zeros are lam = 3 + l + k (l, k = 0, 1, 2) to 10^-25, and at lam
     = 3, l = 0 the outgoing series is z^(3/2) = (v/(v + 2))^(3/2), his u_3; on box^C at s0, gam_C = 1 (the record's v
     and e_C) it vanishes at 1 + mu = 3.6457654215... and 2 + mu, mu = 2.6457654215... the upper root of det N other
     than the Coulomb 2 (whose 3 and 4 lie within 5 x 10^-6 of poles mu' + 1, mu' + 2 of this unnormalized determinant,
     mu' = 1.99999511... the outgoing exponent; I3 has them where no pole is near).  Control: the outgoing exponent
     moved by 1/10, which loses lam = 3.
  I3 (computed, numerical) The descent of N1STAR-PROOF.md 10.37(b) at work, on box^C s0 at gam_C = 10: (i) the
     argument principle over [6/5, 9/2] x [-3, 3] counts 4 zeros, the points 1 + mu + k (mu = 2, 2.1355877934..., k = 0,
     1), each located to 10^-25, so none complex; (ii) the resonant state's moment m = int_0^oo s^-lam G ds is nonzero
     with N(lam - 1) m = 0 at lam = 1 + mu, and vanishes at lam = 2 + mu.  Controls: a count of 3 claimed; N(lam - 2) m
     = 0 claimed.
  I4 (computed, exact and numerical) The candidates at the record's point (lin5.py's POINT: gam_C = 10^6, e_C =
     1/102400, v = 1/2, gam_Ups = e_Ups = 1/100).  (i) The roots of det N_L with real part in (0, 3/2], from I1's M1 at
     50 digits: s0 1.0000747438..., s1 1.0001201950..., none at v1 -- each 1 less than a root of det N_C of the same
     type; none in (0, 1].  (ii) For every l = 0, ..., 400, from damping5.py's polynomials (U3): box^C's roots with real
     part in [-100, 5/2] are the Coulomb root 2 at l = 0 and 1 and, at every scalar type, roots in (2, 5/2) -- 2 +
     7.474e-5 at l = 0, 2 + 1.202e-4 at l = 1, two of them for 2 <= l <= 135, the lowest 2 + 2.93e-6 at l = 2 -- and
     none at a vector type (the lowest 3, at l = 1); the e_C-root against the h = 0 root 2 + e_C ((1 - v^2) kappa + 3
     (1 + v^2))/(2 v^2) of U3's Q_5, within 5 h.  (iii) At s0 box^C's root above 2 stays in (2, 5/2), decreasing, as
     gam_C runs over 10^2, 10^2.5, ..., 10^6.  Control: L-bar's root 1 at s0, which lin5.py's denominator
     (lam - 1)^2 removes, counted.
  I5 (computed, numerical) The s0 candidate is a resonance at moderate gam_C, the record's other parameters: at gam_C =
     10 (50 digits, 260 terms) and 100 (100 digits, 700 terms) the determinant of L-bar's s0 connection changes sign once
     on a grid of [1.2, 2.3] with the candidate +- 10^-3, 10^-5 added, at the candidate lam^C = 2.1355877934... and
     2.0149221090..., where it is below 10^-4 of its value at +- 10^-5.  The record's gam_C = 10^6 is beyond this
     method: the outgoing exponents near 10^6 need some 5 x 10^6 terms at s = 2 (at gam_C = 100, 400 do and 200 do not).
     Control: the zero claimed 10^-3 above the candidate.

Deduced from these (N1STAR-PROOF.md 10.37): the tower lam -> lam + 1 (d/dt*), the descent lam -> lam - 1 (the moment),
[Hin26] Proposition 9.2(2)'s injectivity below 1 + eps_ind in five dimensions on 10.25's readings, and hence: at the
record's point every pure iota+ resonance of L-bar with real part below 5/2 is a root of box^C's det N_C in (2, 5/2),
and none has real part at most 2.

sympy, mpmath.  python3 iota5.py [--selftest | --mutants | --only k]   (about twenty and fifteen minutes)
"""
import sys
import time

import mpmath as mp
import sympy as sp

import damping5 as DP
import lin5 as L5
from damping5 import Checklist

T, a, Lam = sp.symbols("T a Lam")
X = L5.lam                                                  # lin5.py's lam: the r-exponent of the field, x here


# ------------------------------------------------------------------------------------------------- I1 the model
class TCtx(L5.Ctx):
    """lin5.py's context with t* dependence: d_0 = d_T, d_i = (lin5.py's d_i) - (x_i / r) d_T"""

    def d(self, f, i):
        if i == 0:
            return sp.diff(f, T)
        return L5.Ctx.d(self, f, i) - self.x[i - 1] / self.r * sp.diff(f, T)


def tctx(n, typ):
    C0 = L5.ctx_of(n, typ)
    return TCtx(n, C0.p, C0.deg)


_M = {}


def mats(n, typ, op, zsym=False):
    """(M0, M1, closure): M0 = (x - Lam) L1(x) and M1 = N(x) in the type's basis, symbolic in x, Lam, the parameters"""
    key = (n, typ, op.__name__, zsym)
    if key in _M:
        return _M[key]
    C = tctx(n, typ)
    B1, B2 = L5.bases(C, typ)
    B = B2 if op is L5.Lbar else B1
    outs = [op(C, T**a * b if isinstance(b, sp.MatrixBase) else [T**a * q for q in b]) for b in B]
    P = L5.point(C, 0)
    ev = lambda q: sp.expand(sp.sympify(q).subs(P))
    E = sp.Matrix([[ev(q) for q in L5.flat(C, b)] for b in B]).T
    parts = {}
    for k, sc in ((0, C.r**2), (-1, C.r), (-2, sp.Integer(1))):
        cols = []
        for o in outs:
            col = []
            for q in L5.flat(C, o):
                if zsym:                                    # the control: z left symbolic while T is split off
                    e = sp.expand(sp.powsimp(sp.expand(sp.sympify(q) * sc / T**a), force=True))
                    col.append(ev(e.coeff(T, k)))
                else:                                       # the point first, then the powers of T
                    e = sp.expand(sp.powsimp(sp.expand(sp.sympify(q).subs(P) * sc.subs(P) / T**a), force=True))
                    col.append(e.coeff(T, k))
            cols.append(col)
        parts[k] = sp.Matrix(cols).T
    nonull = all(sp.simplify(q) == 0 for q in parts[-2])
    Eh = E.H
    Gi = (Eh * E).applyfunc(sp.cancel).inv()
    res, ok = {}, nonull
    for k in (0, -1):
        Nk = (Gi * (Eh * parts[k])).applyfunc(lambda q: sp.cancel(sp.expand(q)))
        ok &= all(sp.cancel(sp.expand(q)) == 0 for q in (E * Nk - parts[k]))
        res[k] = Nk
    M0 = res[-1].subs(a, X - Lam).applyfunc(sp.expand)
    M1 = res[0].applyfunc(sp.expand)
    _M[key] = (M0, M1, ok)
    return _M[key]


def numeric(M0, M1, subs):
    """Lam -> ((P2, P1, P0), (Q2, Q1, Q0)) in mpmath, M0(x) = P2 x^2 + P1 x + P0, M1(x) = Q2 x^2 + Q1 x + Q0"""
    K = M0.shape[0]

    def coeffs(M, withLam):
        out = []
        for k in (2, 1, 0):
            rows = []
            for i in range(K):
                row = []
                for j in range(K):
                    q = sp.Poly(sp.expand(M[i, j].subs(subs)), X).coeff_monomial(X**k)
                    pl = sp.Poly(q, Lam).all_coeffs() if withLam else [q]
                    row.append([mp.mpmathify(sp.N(c, mp.mp.dps + 20)) for c in pl])
                rows.append(row)
            out.append(rows)
        return out
    c0, c1 = coeffs(M0, True), coeffs(M1, False)

    def F(L):
        mk = lambda E: mp.matrix([[mp.polyval(E[i][j], L) for j in range(K)] for i in range(K)])
        return tuple(mk(E) for E in c0), tuple(mk(E) for E in c1)
    return F


# ------------------------------------------------------------------------------------------------- I2 the connection
def coeffR(Af, Bf, c):
    """(1 - z) A(D) + 2 c z B(D) = sum_j z^j R_j(theta), D = (1 - z) theta, theta = z d/dz"""
    A2, A1, A0 = Af
    B2, B1, B0 = Bf
    return [(A2, A1, A0), (-3 * A2 + 2 * c * B2, -A2 - 2 * A1 + 2 * c * B1, -A0 + 2 * c * B0),
            (3 * A2 - 4 * c * B2, 2 * A2 + A1 - 2 * c * B2 - 2 * c * B1, A0 * 0),
            (-A2 + 2 * c * B2, -A2 + 2 * c * B2, A0 * 0)]


def ev(R, x):
    return R[0] * x**2 + R[1] * x + R[2]


def kernel(M):
    """a null vector by inverse iteration, its first component of modulus > 10^-8 set to 1 (analytic in parameters)"""
    K = M.rows
    y = mp.matrix([mp.mpf(1) + mp.mpf(j) / 10 for j in range(K)])
    Mp = M + mp.eye(K) * mp.mpf(10)**(-mp.mp.dps // 2)
    for _ in range(8):
        y = mp.lu_solve(Mp, y)
        y = y / mp.norm(y)
    for i in range(K):
        if abs(y[i]) > mp.mpf(10)**-8:
            return y / y[i]
    return y


def frob(Rs, mu, z, N, coeffs=False):
    """sum g_n z^(mu + n), g_0 in ker R_0(mu): (value, theta value) at z divided by z^mu, or the coefficients"""
    g0 = kernel(ev(Rs[0], mu))
    gs = [g0]
    val, th, zn = g0 * 1, g0 * mu, mp.mpf(1)
    for n in range(1, N):
        rhs = sum((ev(Rs[j], mu + n - j) * gs[n - j] for j in range(1, 4) if n - j >= 0), mp.matrix(g0.rows, 1))
        g = -mp.lu_solve(ev(Rs[0], mu + n), rhs)
        gs.append(g)
        zn *= z
        val += g * zn
        th += g * (mu + n) * zn
    return gs if coeffs else (val, th)


def quad_eigs(Q):
    """the 2K roots of det(Q2 x^2 + Q1 x + Q0) by the companion linearization"""
    Q2, Q1, Q0 = Q
    K = Q2.rows
    A = mp.matrix(2 * K, 2 * K)
    i2 = mp.inverse(Q2)
    B0, B1 = -i2 * Q0, -i2 * Q1
    for i in range(K):
        A[i, K + i] = 1
        for j in range(K):
            A[K + i, j], A[K + i, K + j] = B0[i, j], B1[i, j]
    return [realify(q) for q in eigvals(A)]


def eigvals(M):
    if M.rows == 1:
        return [M[0, 0]]
    return list(mp.eig(M, left=False, right=False))


def realify(q):
    return mp.re(q) if abs(mp.im(q)) < mp.mpf(10)**(-mp.mp.dps // 2) * (1 + abs(q)) else q


def out_exps(P, lam):
    """M0(x) = (x - lam)(P2 x + P1 + lam P2): the outgoing exponents, the roots of det(P2 x + P1 + lam P2)"""
    P2, P1, P0 = P
    C = P1 + lam * P2
    assert mp.norm(P0 + lam * C) < mp.mpf(10)**(-mp.mp.dps // 2) * (1 + mp.norm(P0)), "M0 does not factor"
    e = [realify(q) for q in eigvals(-mp.inverse(P2) * C)]
    return sorted(e, key=lambda q: (mp.nint(mp.re(q) * 10**8), mp.nint(mp.im(q) * 10**8)))


def neg(Tr):
    return (Tr[0], -Tr[1], Tr[2])                           # x -> -x


def connection(P, Q, lam, N=260, shift=0, colnorm=False):
    """(det, matrix, out exponents, allowed exponents) at s = 2 in rows (G, D_s G); shift moves the outgoing exponents
    (a control)"""
    K = P[0].rows
    out = [q + shift for q in out_exps(P, lam)]
    allow = sorted(quad_eigs(Q), key=mp.re)[:K]
    z = mp.mpf(1) / 2
    R0s, Rinf = coeffR(P, Q, 1), coeffR(neg(Q), neg(P), mp.mpf(1) / 4)
    cols = []
    for mu in out:
        v, th = frob(R0s, mu, z, N)
        cols.append([q for q in v] + [q * (1 - z) for q in th])        # D_s = (1 - z) theta_z
    for nu in allow:
        v, th = frob(Rinf, -nu, z, N)
        cols.append([q for q in v] + [-q * (1 - z) for q in th])       # D_s = -(1 - z') theta_z', z' = 1 - z
    C = mp.matrix(2 * K, 2 * K)
    for j, c in enumerate(cols):
        nrm = max(abs(q) for q in c) if colnorm else 1                   # positive rescaling: the zeros stay
        for i in range(2 * K):
            C[i, j] = c[i] / nrm
    return mp.det(C), C, out, allow


def free_wave(l):
    """the scalar 4+1 wave, type l, in the normalization of I1: M0 = -(x - lam)(2x - 3), N = -x^2 + 2x + l(l + 2)"""
    one = lambda q: mp.matrix([[q]])
    return lambda L: ((one(-2), one(2 * L + 3), one(-3 * L)), (one(-1), one(2), one(l * (l + 2))))


def i1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    zsym = control == 1
    free = {L5.gU: 0, L5.gC: 0}
    ok = True
    for typ, ops in (("s0", (L5.Lbar, L5.box_C, L5.box_U)), ("s1", (L5.Lbar, L5.box_C, L5.box_U)),
                     ("v1", (L5.Lbar, L5.box_C, L5.box_U)), ("v2", (L5.Lbar,)), ("t2", (L5.Lbar,))):
        for op in ops:
            if zsym and typ != "s1":
                continue
            M0, M1, closed = mats(4, typ, op, zsym=zsym)
            K = M0.shape[0]
            half = sp.Rational(1, 2) if op is L5.Lbar else 1          # 2 L-bar = box at gam = 0 ([Hin26] (8.5))
            fr = (M0.subs(free) - half * (X - Lam) * (3 - 2 * X) * sp.eye(K)).applyfunc(sp.expand)
            lin = all(sp.Poly(sp.expand(sp.cancel(q / (X - Lam))), X).degree() <= 1 for q in M0 if q != 0) and \
                all(sp.rem(sp.Poly(q, X), sp.Poly(X - Lam, X)) == 0 for q in M0 if q != 0)
            good = closed and lin and fr == sp.zeros(K, K)
            chk(f"{typ} {op.__name__}: no T^(a-2) term, closed in the type, M0 = (x - lam) L1 with L1 affine, at gam = 0"
                f" L1 = {half} (3 - 2x) Id ({K} x {K})", good)
            ok &= good
    if not zsym:
        for typ in ("s0", "v1"):
            M0, M1, _ = mats(4, typ, L5.Lbar)
            C0 = L5.ctx_of(4, typ)
            _, B2 = L5.bases(C0, typ)
            NL, _ = L5.Nmat(C0, B2, [L5.Lbar(C0, b) for b in B2], scale=C0.r**2)
            same = (M1 - NL).applyfunc(lambda q: sp.cancel(sp.expand(q))) == sp.zeros(*M1.shape)
            chk(f"{typ}: M1 is lin5.py's N_L itself", same)
            ok &= same
    return ok


def i2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mp.mp.dps = 40
    shift = mp.mpf(1) / 10 if control == 1 else 0
    ok = True
    for l in (0, 1, 2):
        F = free_wave(l)
        f = lambda L: connection(*F(L), L, N=200, shift=shift)[0]
        for k in (0, 1, 2):
            st = mp.mpf(3 + l + k)
            try:
                r = mp.findroot(f, (st + mp.mpf(1) / 1000, st + mp.mpf(1) / 500), solver="secant", tol=mp.mpf(10)**-30)
                good = abs(r - st) < mp.mpf(10)**-25
            except Exception:
                r, good = None, False
            chk(f"free wave l = {l}: a zero at 3 + l + k = {st}" + ("" if r is None else f" ({mp.nstr(r - st, 3)})"),
                good)
            ok &= good
    P, Q = free_wave(0)(mp.mpf(3))
    gs = frob(coeffR(P, Q, 1), mp.mpf(3) / 2 + shift, mp.mpf(1) / 2, 12, coeffs=True)
    term = all(mp.norm(g) < mp.mpf(10)**-30 for g in gs[1:])
    chk("lam = 3, l = 0: the outgoing series is z^(3/2) = (v/(v + 2))^(3/2) exactly (g_n = 0, n >= 1), his u_3", term)
    ok &= term
    M0, M1, _ = mats(4, "s0", L5.box_C)
    subs = dict(L5.POINT)
    subs[L5.gC] = 1
    F = numeric(M0, M1, subs)
    ups = sorted(quad_eigs(F(mp.mpf(3))[1]), key=mp.re)[2:]
    want = [1 + ups[1], 2 + ups[1]]
    f = lambda L: connection(*F(L), L, N=200, shift=shift)[0]
    for w in want:
        try:
            r = mp.findroot(f, (w + mp.mpf(1) / 1000, w + mp.mpf(1) / 500), solver="secant", tol=mp.mpf(10)**-30)
            good = abs(r - w) < mp.mpf(10)**-25
        except Exception:
            r, good = None, False
        chk(f"box^C s0, gam_C = 1: a zero at 1 + mu + k = {mp.nstr(w, 12)}, mu an upper root of det N "
            f"({[mp.nstr(u, 12) for u in ups]})", good)
        ok &= good
    return ok


def winding(f, x0, x1, y0, y1, n0=24, maxdepth=14):
    """zeros of f inside the rectangle by the argument principle, each step's change of arg below pi/6"""
    corners = [mp.mpc(x0, y0), mp.mpc(x1, y0), mp.mpc(x1, y1), mp.mpc(x0, y1)]
    total = mp.mpf(0)
    for k in range(4):
        A, B = corners[k], corners[(k + 1) % 4]
        pts = [A + (B - A) * j / n0 for j in range(n0 + 1)]
        vals = [f(z) for z in pts]
        stack = list(zip(zip(pts, pts[1:]), zip(vals, vals[1:]), [0] * n0))
        while stack:
            (za, zb), (fa, fb), dep = stack.pop()
            dphi = mp.im(mp.log(fb / fa))
            if abs(dphi) > mp.pi / 6 and dep < maxdepth:
                zm = (za + zb) / 2
                fm = f(zm)
                stack += [((zm, zb), (fm, fb), dep + 1), ((za, zm), (fa, fm), dep + 1)]
            else:
                total += dphi
    return total / (2 * mp.pi)


def moment(P, Q, lam, N=200):
    """the resonant state's moment m = int_0^oo s^-lam G(s) ds, G from the null vector of the connection matrix, and
    the scale int_0^oo |s^-lam G| ds"""
    _, C, out, allow = connection(P, Q, lam, N=N)
    K = P[0].rows
    U, S, V = mp.svd_c(C)
    c = [V[2 * K - 1, j].conjugate() for j in range(2 * K)]
    R0s, Rinf = coeffR(P, Q, 1), coeffR(neg(Q), neg(P), mp.mpf(1) / 4)
    s0 = [(c[j], mu, frob(R0s, mu, 0, N, coeffs=True)) for j, mu in enumerate(out)]
    si = [(-c[K + j], -nu, frob(Rinf, -nu, 0, N, coeffs=True)) for j, nu in enumerate(allow)]

    def G(z, fam):
        tot = mp.matrix(K, 1)
        for cj, mu, gs in fam:
            acc, zn = mp.matrix(K, 1), mp.mpf(1)
            for g in gs:
                acc += g * zn
                zn *= z
            tot += cj * acc * (2 * z)**mu                  # the columns were taken at z = 1/2 over z^mu
        return tot
    m, sc = mp.matrix(K, 1), mp.mpf(0)
    for fam, jac in ((s0, lambda z: (2 * z / (1 - z))**(-lam) * 2 / (1 - z)**2),
                     (si, lambda z: (2 * (1 - z) / z)**(-lam) * 2 / z**2)):
        for i in range(K):
            m[i] += mp.quad(lambda z: jac(z) * G(z, fam)[i], [0, mp.mpf(1) / 4, mp.mpf(1) / 2])
        sc += mp.quad(lambda z: abs(jac(z)) * mp.norm(G(z, fam)), [0, mp.mpf(1) / 4, mp.mpf(1) / 2])
    return m, sc


def i3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mp.mp.dps = 30
    M0, M1, _ = mats(4, "s0", L5.box_C)
    subs = dict(L5.POINT)
    subs[L5.gC] = 10
    F = numeric(M0, M1, subs)
    ups = sorted(quad_eigs(F(mp.mpf(3))[1]), key=mp.re)[2:]
    pts = [1 + u + k for u in ups for k in (0, 1)]
    f = lambda L: connection(*F(L), L, N=160)[0]
    w = winding(f, mp.mpf(6) / 5, mp.mpf(9) / 2, -3, 3)
    want = 3 if control == 1 else 4
    good = abs(w - want) < mp.mpf(1) / 100
    chk(f"argument principle over [6/5, 9/2] x [-3, 3]: {mp.nstr(w, 6)} zeros; claimed {want}", good)
    ok = good
    for p in pts:
        try:
            r = mp.findroot(f, (p + mp.mpf(1) / 1000, p + mp.mpf(1) / 500), solver="secant", tol=mp.mpf(10)**-28)
            good = abs(r - p) < mp.mpf(10)**-22
        except Exception:
            good = False
        chk(f"a zero at 1 + mu + k = {mp.nstr(p, 14)}", good)
        ok &= good
    sh = 2 if control == 2 else 1
    for u in ups:
        lam = 1 + u
        P, Q = F(lam)
        m, sc = moment(P, Q, lam)
        Nm = ev(Q, lam - sh) * m
        good = mp.norm(m) > mp.mpf(10)**-6 * sc and mp.norm(Nm) < mp.mpf(10)**-12 * sc * mp.norm(ev(Q, lam - sh))
        chk(f"lam = 1 + mu = {mp.nstr(lam, 12)}: |m| / scale = {mp.nstr(mp.norm(m) / sc, 4)}, N(lam - {sh}) m: "
            f"{mp.nstr(mp.norm(Nm) / sc, 3)}", good)
        ok &= good
        lam = 2 + u
        P, Q = F(lam)
        m, sc = moment(P, Q, lam)
        good = mp.norm(m) < mp.mpf(10)**-12 * sc
        chk(f"lam = 2 + mu = {mp.nstr(lam, 12)}: the moment vanishes, |m| / scale = {mp.nstr(mp.norm(m) / sc, 3)}",
            good)
        ok &= good
    return ok


def i4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mp.mp.dps = 50
    ok = True
    want = {"s0": [mp.mpf("1.0000747438204")], "s1": [mp.mpf("1.0001201950372")], "v1": []}
    for typ in ("s0", "s1", "v1"):
        ML0, ML1, _ = mats(4, typ, L5.Lbar)
        MC0, MC1, _ = mats(4, typ, L5.box_C)
        rL = quad_eigs(numeric(ML0, ML1, dict(L5.POINT))(mp.mpf(2))[1])
        rC = quad_eigs(numeric(MC0, MC1, dict(L5.POINT))(mp.mpf(2))[1])
        inb = sorted([mp.re(q) for q in rL if 0 < mp.re(q) <= mp.mpf(3) / 2 + mp.mpf(10)**-40], key=float)
        if control == 1 and typ == "s0":
            inb = sorted(inb + [mp.mpf(1)], key=float)
        fromC = all(min(abs(q + 1 - c) for c in rC) < mp.mpf(10)**-30 for q in inb)
        none01 = all(q > 1 for q in inb)
        good = len(inb) == len(want[typ]) and all(abs(q - w) < mp.mpf(10)**-12 for q, w in zip(inb, want[typ])) and \
            fromC and none01
        chk(f"{typ}: the roots of det N_L with real part in (0, 3/2]: {[mp.nstr(q, 14) for q in inb]}, each 1 less "
            f"than a root of det N_C, none in (0, 1]", good)
        ok &= good
    pk, p0, pv = DP.polys(4, sp.Rational(2, 3))
    E, V, H = mp.mpf(1) / 102400, mp.mpf(1) / 2, mp.mpf(10)**-6
    lo, exc, vlo, inband, two = mp.inf, [], mp.inf, set(), []
    for name, P, ls in (("s0", p0, [0]), ("sl", pk, range(1, 401)), ("vl", pv, range(1, 401))):
        co = [sp.lambdify((DP.e, DP.v, DP.h, DP.K), c, "mpmath") for c in sp.Poly(P, DP.lam).all_coeffs()]
        for lv in ls:
            kap = lv * (lv + 2)                             # damping5.py's kappa, scalar and vector types alike
            rts = mp.polyroots([c(E, V, H, kap) for c in co], maxsteps=500, extraprec=300)
            band = [z for z in rts if abs(z - 2) >= mp.mpf(10)**-30 and -100 <= mp.re(z) <= mp.mpf(5) / 2]
            exc += [(name, lv)] * sum(1 for z in rts if abs(z - 2) < mp.mpf(10)**-30)
            if name == "vl":
                vlo = min([vlo] + [mp.re(z) for z in rts if mp.re(z) > -100])
            elif band:
                lo = min([lo] + [mp.re(z) for z in band])
                inband.add(lv)
                if len(band) == 2:
                    two.append(lv)
            if name != "vl" and lv <= 2:
                eroot = max([z for z in rts if 2 + mp.mpf(10)**-30 < mp.re(z) < mp.mpf(5) / 2], key=mp.re)
                h0 = 2 + E * ((1 - V**2) * kap + 3 * (1 + V**2)) / (2 * V**2)
                good = abs(eroot - h0) < 5 * H
                chk(f"l = {lv}: the e_C-root {mp.nstr(eroot, 12)} against the h = 0 root {mp.nstr(h0, 12)}", good)
                ok &= good
    l2 = max(two) if two else None
    good = exc == [("s0", 0), ("sl", 1)] and lo > 2 and abs(lo - 2 - mp.mpf("2.93235e-6")) < mp.mpf(10)**-10 and \
        vlo == 3 and inband == set(range(0, 401)) and two == list(range(2, l2 + 1))
    chk(f"l <= 400: box^C's roots in [-100, 5/2] are 2 at {exc} and others in (2, 5/2), the lowest 2 + "
        f"{mp.nstr(lo - 2, 6)}, at every scalar l, two of them for 2 <= l <= {l2}; at the vector types none (the lowest "
        f"{mp.nstr(vlo, 8)})", good)
    ok &= good
    co = [sp.lambdify((DP.e, DP.v, DP.h, DP.K), c, "mpmath") for c in sp.Poly(p0, DP.lam).all_coeffs()]
    path = []
    for k in range(4, 13):                                  # gam_C = 10^(k/2), 10^2 to 10^6
        hv = mp.mpf(10)**(-mp.mpf(k) / 2)
        rts = mp.polyroots([c(E, V, hv, 0) for c in co], maxsteps=500, extraprec=300)
        path.append(min([mp.re(z) for z in rts if mp.re(z) > 2 + mp.mpf(10)**-30]))
    good = all(2 < q < mp.mpf(5) / 2 for q in path) and all(p > q for p, q in zip(path, path[1:]))
    chk(f"s0 along gam_C = 10^2, ..., 10^6: box^C's root above 2 {[mp.nstr(q, 8) for q in path]}, in (2, 5/2) and "
        f"decreasing", good)
    return ok and good


def i5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    M0, M1, _ = mats(4, "s0", L5.Lbar)
    ok = True
    for g, dps, N in ((10, 50, 260), (100, 100, 700)):
        mp.mp.dps = dps
        subs = dict(L5.POINT)
        subs[L5.gC] = g
        F = numeric(M0, M1, subs)
        f = lambda L: mp.re(connection(*F(L), L, N=N, colnorm=True)[0])
        ups = sorted(quad_eigs(F(mp.mpf(2))[1]), key=mp.re)[4:]
        cands = [1 + u for u in ups if 0 < u < mp.mpf(3) / 2]
        c = cands[0]
        tgt = c + (mp.mpf(10)**-3 if control == 1 else 0)
        grid = sorted([mp.mpf(q) + mp.mpf(1) / 997 for q in ("1.2", "1.5", "1.8", "1.95", "2.3")] +
                      [c + d for d in (-mp.mpf(10)**-3, -mp.mpf(10)**-5, mp.mpf(10)**-5, mp.mpf(10)**-3)])
        vals = [f(L) for L in grid]
        flips = [(grid[i], grid[i + 1]) for i in range(len(grid) - 1) if mp.sign(vals[i]) != mp.sign(vals[i + 1])]
        side = max(abs(f(tgt - mp.mpf(10)**-5)), abs(f(tgt + mp.mpf(10)**-5)))
        at = abs(f(tgt))
        good = len(cands) == 1 and len(flips) == 1 and flips[0][0] < c < flips[0][1] and at < mp.mpf(10)**-4 * side
        fl = [(mp.nstr(p, 8), mp.nstr(q, 8)) for p, q in flips]
        chk(f"gam_C = {g}: one candidate {mp.nstr(c, 12)}; sign changes {fl}; |det| at {mp.nstr(tgt, 10)} / at +- "
            f"10^-5: {mp.nstr(at / side, 3)}", good)
        ok &= good
    return ok


CHECKS = [("I1 the iota+ model by type from lin5.py's operators: M0 = (x - lam) L1, M1 = N_L, the free transport", i1,
           1),
          ("I2 the connection through z = s/(s + 2): the free wave's 3 + l + k and his u_3; box^C at gam_C = 1", i2, 1),
          ("I3 the descent: 4 zeros in [6/5, 9/2] x [-3, 3] at 1 + mu + k; the moment at 1 + mu and 2 + mu", i3, 2),
          ("I4 the record's point: det N_L's roots in (0, 3/2] are box^C's minus 1; box^C over l <= 400 in (2, 5/2)",
           i4, 1),
          ("I5 the s0 candidate is a pure resonance of L-bar at gam_C = 10 and 100", i5, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"iota5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"iota5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, _ = CHECKS[k - 1]
        print(name, fn(verbose=True))
        sys.exit(0)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
