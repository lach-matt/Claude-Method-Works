"""coulombL5.py -- BEYOND5 Lemma 6.5' (D417): the Coulomb part at I_0 under the record's full flat operator.

Lemma 6.5 carried the means' leading term r^-2 M Y_l from N = {v = v1} to I_0 under the flat wave operator. The record's
operator is L = D Ric + delta*_(E^C) delta_(E^Ups) G (lin5.py's Lbar; [Hin26] (8.1)), with
E^Ups h = -gam_U (2 iota_(c_U#) h - (2/3)(1 - e_U) c_U tr h), c_U = r^-1 dt, and
E^C w = gam_C (2 c (x)_s w - (2/3)(1 - e_C) g <c, w>), c = r^-1 (dt - v dr). On 4+1 Minkowski both c's are
homogeneous of degree -1, so L is homogeneous of degree -2: data r^-2 F(0) on N (taking v1 = 0) give, by
uniqueness, the self-similar solution r^-2 F(s), s := (t + r)/r = v/r. On a slice t = const, s = 1 + t rho, so
r^2 h = F(1 + t rho): the expansion at I_0 is F's Taylor series at s = 1.

The spherically symmetric sector, h = r^-2 (a dt^2 + 2b dt dr + c dr^2 + d r^2 g_S3), F = (a, b, c, d), with
genstates5.py's polar machinery:

  Q1 (exact) r^4 (L h)_(tt, tr, rr) and r^2 (L h)_(chi chi) depend on s and the parameters only (no t, r), and the
     other angular components agree with chi chi (phi phi = sin^2 theta theta theta) and the off-diagonal ones outside
     (t, r) vanish (all checked since D429): L reduces to a 4 x 4 ODE system in s.
  Q2 (exact) its second-order part is (s - s^2/2) F'' = -(1/2) s (s - 2) F'' in every row, diagonal: the principal
     symbol at ds. The other coefficients are polynomials in s. So the only singular points are s = 0 (N) and s = 2
     (the cone u = 0), and s = 1 (I_0) is an ordinary point: F is analytic there for every value of gam_U, e_U, gam_C,
     e_C, v, and r^2 h is smooth in rho at I_0, with no logarithm.
  Q3 (exact, control) with the damping off (gam_U = gam_C = 0) Lemma 6.5's polynomials solve the system: a = a0,
     b = b0 (1 - s), c - d = e0 U_2(1 - s)/3, (c + 3d)/4 = p0, the Cartesian harmonics l = 0, 1, 2, 0; so the transfer
     F(0) -> F(1) multiplies them by 1, 0, -1/3, 1 (cos(pi l/2)/(l + 1)). Control: c - d with U_1 for U_2 fails.
  Q4 (computed) the Frobenius exponents at s = 0 are 0 (the regular branch, which the data fix) and 1 - eig(m1_0),
     m1_0 the coefficient of F' at s = 0; at the record's point (e_U = gam_U = 1/100, e_C = 1/102400, gam_C = 10^6,
     v = 1/2; lin5.POINT) none is a positive integer, so the regular branch exists for every F(0). The transfer
     F(0) -> F(1) at gam_C = 1 by the regular series (convergent for |s| < 2) and by a stiff integrator agree.
  Q5 (exact, D421) the l = 1 scalar-type sector (six functions; the traceless Hessian of an l = 1 harmonic on S^3
     vanishes): the same reduction, second-order part (s - s^2/2) I, polynomial coefficients, exponents at s = 0
     besides 0 all negative at the record's point. The seven components outside the sector, (t, r, chi) x (theta, phi)
     and (theta, phi), vanish, and phi phi = sin^2 theta theta theta (all checked; verifier 184, D427).
  Q6 (exact, D426) Tangherlini to first order in mu (static t, f = 1 - mu/r^2, c_U and c built on that t), the l = 0
     sector, h = r^-2 F(s) + mu r^-4 G(s): the mu^0 part is Q1's system; the mu^1 part is an ODE system for G with a
     source in F, depending on s only, with second-order part (s - s^2/2) I and polynomial coefficients and source;
     G's exponents at s = 0 besides 0 are all negative at the record's point.
Labels: computed (exact, sympy; floating point where said); the smoothness at I_0 deduced from Q2 (an ODE with analytic
coefficients at an ordinary point). Harmonics beyond l = 1, the vector and tensor types, and Tangherlini beyond O(mu)
are not computed here.

    python3 checks/coulombL5.py [--selftest]
"""
import os
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import genstates5 as GS   # noqa: E402

t, r, ch = GS.t, GS.r, GS.ch
S = sp.Symbol("s")
gC, eC, vC = sp.symbols("gamma_C e_C v_C", positive=True)
gU, eU = GS.gU, GS.eU
FN = [sp.Function(n) for n in "abcd"]
POINT = {gU: sp.Rational(1, 100), eU: sp.Rational(1, 100), gC: 10**6, eC: sp.Rational(1, 102400), vC: sp.Rational(1, 2)}


def reduce():
    G = GS.geo(4, True)
    X, g, gi, Gam, f = G
    N = 5
    sx = (t + r)/r
    a, b, c, d = FN
    h = sp.zeros(N)
    h[0, 0], h[1, 1] = a(sx)/r**2, c(sx)/r**2
    h[0, 1] = h[1, 0] = b(sx)/r**2
    for k in (2, 3, 4):
        h[k, k] = g[k, k]*d(sx)/r**2

    def E_C(w):
        cc = [1/r, -vC/r, 0, 0, 0]
        cw = sum(gi[p, q]*cc[p]*w[q] for p in range(N) for q in range(N))
        m = sp.Rational(2, 3)*(1 - eC)
        return sp.Matrix(N, N, lambda p, q: gC*(cc[p]*w[q] + cc[q]*w[p] - m*g[p, q]*cw))

    Gh = GS.Gop(h, G)
    w = [p + q for p, q in zip(GS.div(Gh, G), GS.Eups(Gh, G))]
    L = GS.dric(h, G) + GS.dstar(w, G) + E_C(w)
    comps = [L[0, 0]*r**4, L[0, 1]*r**4, L[1, 1]*r**4, L[2, 2]*r**2, L[3, 3]*r**2/sp.sin(ch)**2,
             L[4, 4] - sp.sin(GS.th)**2*L[3, 3]]
    comps += [L[p, q] for p in range(N) for q in range(p + 1, N) if (p, q) != (0, 1)]
    return [sp.expand(sp.simplify(e.subs(t, (S - 1)*r).doit())) for e in comps]


FN1 = [sp.Function(n) for n in ("a1", "b1", "c1", "d1", "e1", "f1")]


def reduce_l1():
    """the l = 1 scalar-type sector, Y = cos chi: h = r^-2 Y (a dt^2 + 2b dt dr + c dr^2 + d r^2 g_S3)
    + 2 r^-1 (e dt + f dr) (x)_s dY (the traceless Hessian of an l = 1 harmonic on S^3 vanishes)"""
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    sx = (t + r)/r
    a, b, c, d, e, f = FN1
    Y, dY = sp.cos(ch), -sp.sin(ch)
    h = sp.zeros(N)
    h[0, 0], h[1, 1] = Y*a(sx)/r**2, Y*c(sx)/r**2
    h[0, 1] = h[1, 0] = Y*b(sx)/r**2
    for k in (2, 3, 4):
        h[k, k] = g[k, k]*Y*d(sx)/r**2
    h[0, 2] = h[2, 0] = dY*e(sx)/r
    h[1, 2] = h[2, 1] = dY*f(sx)/r

    def E_C(w):
        cc = [1/r, -vC/r, 0, 0, 0]
        cw = sum(gi[p, q]*cc[p]*w[q] for p in range(N) for q in range(N))
        m = sp.Rational(2, 3)*(1 - eC)
        return sp.Matrix(N, N, lambda p, q: gC*(cc[p]*w[q] + cc[q]*w[p] - m*g[p, q]*cw))

    Gh = GS.Gop(h, G)
    w = [p + q for p, q in zip(GS.div(Gh, G), GS.Eups(Gh, G))]
    L = GS.dric(h, G) + GS.dstar(w, G) + E_C(w)
    comps = [L[0, 0]*r**4/Y, L[0, 1]*r**4/Y, L[1, 1]*r**4/Y, L[2, 2]*r**2/Y, L[0, 2]*r**3/dY, L[1, 2]*r**3/dY,
             L[3, 3]*r**2/(Y*sp.sin(ch)**2), L[0, 3], L[0, 4], L[1, 3], L[1, 4], L[2, 3], L[2, 4], L[3, 4],
             L[4, 4] - sp.sin(GS.th)**2*L[3, 3]]
    return [sp.expand(sp.simplify(q.subs(t, (S - 1)*r).doit())) for q in comps]


GN = [sp.Function(n) for n in ("ga", "gb", "gc", "gd")]


def reduce_tang():
    """Q6 (D426): Tangherlini (static t, f = 1 - mu/r^2; c_U = r^-1 dt and c = r^-1 (dt - v dr) in that t), the l = 0
    sector, h = r^-2 F(s) + mu r^-4 G(s): the lam-free operator's mu^0 part (Q1's system for F) and its mu^1 part,
    r^6 (tt, tr, rr) and r^4 (chi chi), an ODE system for G with a source in F"""
    G_ = GS.geo(4, False)
    X, g, gi, Gam, f_ = G_
    N = 5
    sx = (t + r)/r
    h = sp.zeros(N)
    F, Gf = FN, GN
    h[0, 0] = F[0](sx)/r**2 + GS.mu*Gf[0](sx)/r**4
    h[1, 1] = F[2](sx)/r**2 + GS.mu*Gf[2](sx)/r**4
    h[0, 1] = h[1, 0] = F[1](sx)/r**2 + GS.mu*Gf[1](sx)/r**4
    for k in (2, 3, 4):
        h[k, k] = g[k, k]*(F[3](sx)/r**2 + GS.mu*Gf[3](sx)/r**4)

    def E_C(w):
        cc = [1/r, -vC/r, 0, 0, 0]
        cw = sum(gi[p, q]*cc[p]*w[q] for p in range(N) for q in range(N))
        m = sp.Rational(2, 3)*(1 - eC)
        return sp.Matrix(N, N, lambda p, q: gC*(cc[p]*w[q] + cc[q]*w[p] - m*g[p, q]*cw))

    Gh = GS.Gop(h, G_)
    w = [p + q for p, q in zip(GS.div(Gh, G_), GS.Eups(Gh, G_))]
    L = GS.dric(h, G_) + GS.dstar(w, G_) + E_C(w)
    out0, out1 = [], []
    for e, p in ((L[0, 0], 4), (L[0, 1], 4), (L[1, 1], 4), (L[2, 2], 2)):
        e0 = e.subs(GS.mu, 0)
        e1 = sp.diff(e, GS.mu).subs(GS.mu, 0)
        out0.append(sp.expand(sp.simplify((e0*r**p).subs(t, (S - 1)*r).doit())))
        out1.append(sp.expand(sp.simplify((e1*r**(p + 2)).subs(t, (S - 1)*r).doit())))
    return out0, out1


def matrices6(eqs):
    syms = {}
    for k, q in enumerate(FN1):
        syms[sp.Derivative(q(S), (S, 2))] = sp.Symbol("q2_%d" % k)
        syms[sp.Derivative(q(S), S)] = sp.Symbol("q1_%d" % k)
    out = []
    for e in eqs:
        e2 = e.subs(syms).subs({q(S): sp.Symbol("q0_%d" % k) for k, q in enumerate(FN1)})
        out.append(sp.expand(e2))
    M = [sp.Matrix(6, 6, lambda i, j: out[i].coeff(sp.Symbol("q%d_%d" % (o, j)))) for o in (2, 1, 0)]
    rest = [sp.expand(out[i] - sum(M[o][i, j]*sp.Symbol("q%d_%d" % (2 - o, j)) for o in range(3) for j in range(6)))
            for i in range(6)]
    return M, rest


def matrices(eqs):
    """(M2, M1, M0) with eqs = M2 F'' + M1 F' + M0 F, entries polynomials in s"""
    syms = {}
    for k, q in enumerate(FN):
        syms[sp.Derivative(q(S), (S, 2))] = sp.Symbol("q2_%d" % k)
        syms[sp.Derivative(q(S), S)] = sp.Symbol("q1_%d" % k)
    out = []
    for e in eqs:
        e2 = e.subs(syms)
        e2 = e2.subs({q(S): sp.Symbol("q0_%d" % k) for k, q in enumerate(FN)})
        out.append(sp.expand(e2))
    M = [sp.Matrix(4, 4, lambda i, j: out[i].coeff(sp.Symbol("q%d_%d" % (o, j)))) for o in (2, 1, 0)]
    rest = [sp.expand(out[i] - sum(M[o][i, j]*sp.Symbol("q%d_%d" % (2 - o, j)) for o in range(3) for j in range(4)))
            for i in range(4)]
    return M, rest


def series_transfer(M, sub, nterms=400, s1=1, dps=40):
    """F(s1) for the regular Frobenius solutions at s = 0, F(0) = e_j, by the series (radius 2)"""
    mp.mp.dps = dps
    deg = 3
    C = {(o, p): mp.matrix(4, 4) for o in range(3) for p in range(deg + 1)}
    for o in range(3):
        for i in range(4):
            for j in range(4):
                P = sp.Poly(sp.expand(M[o][i, j].subs(sub)), S)
                for (p,), val in P.terms():
                    C[(o, p)][i, j] = mp.mpf(sp.Rational(val).p)/sp.Rational(val).q
    T = mp.matrix(4, 4)
    for j0 in range(4):
        F = [mp.matrix(4, 1)]
        F[0][j0] = 1
        total = F[0]*1
        for n in range(1, nterms):
            # coefficient of s^(n-1): sum over o, p of C[o,p] * k(k-1).. with k = n - 1 + 2 - o - p ... shifted index
            A = mp.matrix(4, 4)
            rhs = mp.matrix(4, 1)
            for o in range(3):
                for p in range(deg + 1):
                    # C[o,p] s^p D^(2-o) (F_k s^k) contributes at s^(p + k - (2 - o)); match s^(n - 1)
                    k = n - 1 - p + (2 - o)
                    if k < 0 or k > n:
                        continue
                    fac = 1
                    for q in range(2 - o):
                        fac *= (k - q)
                    if k == n:
                        A += C[(o, p)]*fac
                    else:
                        rhs -= C[(o, p)]*F[k]*fac
            Fn = mp.lu_solve(A, rhs) if mp.mnorm(A, 1) != 0 else mp.matrix(4, 1)
            F.append(Fn)
            total += Fn*mp.mpf(s1)**n
        for i in range(4):
            T[i, j0] = total[i]
    return T, max(abs(x) for x in F[-1])


def ode_transfer(M, sub, s0=1e-3, s1=1.0, nser=40):
    Ms = [sp.lambdify(S, M[o].subs(sub), "numpy") for o in range(3)]
    Ts, _ = series_transfer(M, sub, nterms=nser, s1=s0, dps=30)
    T = np.zeros((4, 4))
    for j0 in range(4):
        F0 = np.array([float(Ts[i, j0]) for i in range(4)])
        h = 1e-6
        Tp, _ = series_transfer(M, sub, nterms=nser, s1=s0 + h, dps=30)
        Tm, _ = series_transfer(M, sub, nterms=nser, s1=s0 - h, dps=30)
        dF0 = np.array([float((Tp[i, j0] - Tm[i, j0])/(2*h)) for i in range(4)])

        def rhs(s, y):
            M2, M1, M0 = (np.array(m(s), dtype=float) for m in Ms)
            return np.concatenate([y[4:], -np.linalg.solve(M2, M1 @ y[4:] + M0 @ y[:4])])
        sol = solve_ivp(rhs, (s0, s1), np.concatenate([F0, dF0]), method="Radau", rtol=1e-11, atol=1e-13)
        T[:, j0] = sol.y[:4, -1]
    return T


def main():
    ok = {}
    eqs = reduce()
    ok["Q1"] = all(e.free_symbols <= {S, gU, eU, gC, eC, vC} for e in eqs[:5]) and sp.expand(eqs[3] - eqs[4]) == 0 \
        and all(sp.expand(e) == 0 for e in eqs[5:])
    M, rest = matrices(eqs[:4])
    print("  Q1: r and t drop out, chi chi = theta theta, phi phi = sin^2 theta theta theta, the nine off-diagonal "
          "components outside (t, r) vanish: %s" % ok["Q1"], flush=True)
    m2 = S - S**2/2
    ok["Q2"] = all(r_ == 0 for r_ in rest) and sp.expand(M[0] - m2*sp.eye(4)) == sp.zeros(4) and \
        all(M[o][i, j].is_polynomial(S) for o in (1, 2) for i in range(4) for j in range(4))
    print("  Q2: F'' coefficient (s - s^2/2) I, other coefficients polynomial in s: %s" % ok["Q2"], flush=True)
    a0, b0, e0, p0 = sp.symbols("a0 b0 e0 p0")
    U2 = lambda x: 4*x**2 - 1   # noqa: E731
    ee, pp = e0*U2(1 - S)/3, p0
    cs, ds = pp + 3*ee/4, pp - ee/4            # c - d = ee, (c + 3d)/4 = pp
    Fq = sp.Matrix([a0, b0*(1 - S), cs, ds])
    off = {gU: 0, gC: 0}

    def resid(Mx, Fv):
        return (Mx[0]*Fv.diff(S, 2) + Mx[1]*Fv.diff(S) + Mx[2]*Fv).applyfunc(sp.expand)
    q3 = resid([m.subs(off) for m in M], Fq) == sp.zeros(4, 1)
    Fbad = sp.Matrix([a0, b0*(1 - S), pp + 3*e0*(1 - S)/4, pp - e0*(1 - S)/4])
    q3c = resid([m.subs(off) for m in M], Fbad) != sp.zeros(4, 1)
    ok["Q3"] = q3 and q3c
    print("  Q3: damping off, Lemma 6.5's polynomials solve it (transfer 1, 0, -1/3, 1): %s; U_1 for U_2 fails: %s"
          % (q3, q3c), flush=True)
    m10 = sp.Matrix(M[1].subs(S, 0).subs(POINT))
    lam = sp.Symbol("lam")
    ev = [complex(x) for x in sp.Poly(m10.charpoly(lam).as_expr(), lam).nroots(n=30, maxsteps=200)]
    expo = [1 - x for x in ev]
    bad = [x for x in expo if abs(x.imag) < 1e-9 and x.real > 0.5 and abs(x.real - round(x.real)) < 1e-9]
    ok["Q4 exponents"] = not bad
    print("  Q4: exponents at s = 0 at the record's point besides 0: %s; positive integers: %s"
          % (", ".join("%.6g%+.3gi" % (x.real, x.imag) for x in expo), bad or "none"), flush=True)
    mod = dict(POINT)
    mod[gC] = 1
    Tser, last = series_transfer(M, mod)
    Tode = ode_transfer(M, mod)
    diff = max(abs(float(Tser[i, j]) - Tode[i, j]) for i in range(4) for j in range(4))
    ok["Q4 transfer"] = diff < 1e-7 and last < 1e-30
    print("  Q4: transfer F(0) -> F(1) at gam_C = 1 (series, 400 terms; last term %.1e):" % float(last))
    for i in range(4):
        print("      " + "  ".join("%+.10f" % float(Tser[i, j]) for j in range(4)))
    print("      series against Radau: max difference %.2e" % diff)
    e1 = reduce_l1()
    sym = {S, gU, eU, gC, eC, vC}
    q5a = all(q.free_symbols <= sym for q in e1[:7]) and sp.expand(e1[3] - e1[6]) == 0 and \
        all(sp.expand(q) == 0 for q in e1[7:])
    M1, rest1 = matrices6(e1[:6])
    q5b = all(r_ == 0 for r_ in rest1) and sp.expand(M1[0] - m2*sp.eye(6)) == sp.zeros(6) and \
        all(M1[o][i, j].is_polynomial(S) for o in (1, 2) for i in range(6) for j in range(6))
    m10b = sp.Matrix(M1[1].subs(S, 0).subs(POINT))
    lam = sp.Symbol("lam")
    ev1 = [complex(x) for x in sp.Poly(m10b.charpoly(lam).as_expr(), lam).nroots(n=30, maxsteps=200)]
    expo1 = [1 - x for x in ev1]
    bad1 = [x for x in expo1 if abs(x.imag) < 1e-9 and x.real > 0.5 and abs(x.real - round(x.real)) < 1e-9]
    ok["Q5 l = 1"] = q5a and q5b and not bad1
    print("  Q5 (D421): l = 1 scalar-type sector, six functions: r, t and the angles drop out, the other components "
          "vanish: %s; F'' coefficient (s - s^2/2) I, polynomial coefficients: %s; exponents at s = 0 besides 0: %s"
          % (q5a, q5b, ", ".join("%.6g" % x.real if abs(x.imag) < 1e-9 else "%.4g%+.3gi" % (x.real, x.imag)
                                 for x in expo1)))
    o0, o1 = reduce_tang()
    q6a = all(sp.expand(o0[i] - eqs[i]) == 0 for i in range(4))
    q6b = all(q.free_symbols <= sym for q in o1)
    syms = {}
    for k, q in enumerate(GN):
        syms[sp.Derivative(q(S), (S, 2))] = sp.Symbol("q2_%d" % k)
        syms[sp.Derivative(q(S), S)] = sp.Symbol("q1_%d" % k)
    o1s = [sp.expand(q.subs(syms).subs({qq(S): sp.Symbol("q0_%d" % k) for k, qq in enumerate(GN)})) for q in o1]
    MG = [sp.Matrix(4, 4, lambda i, j: o1s[i].coeff(sp.Symbol("q%d_%d" % (o, j)))) for o in (2, 1, 0)]
    src = [sp.expand(o1s[i] - sum(MG[o][i, j]*sp.Symbol("q%d_%d" % (2 - o, j)) for o in range(3) for j in range(4)))
           for i in range(4)]
    fsym = {}
    for k, ff in enumerate(FN):
        fsym[sp.Derivative(ff(S), (S, 2))] = sp.Symbol("F2_%d" % k)
        fsym[sp.Derivative(ff(S), S)] = sp.Symbol("F1_%d" % k)
    fsym0 = {ff(S): sp.Symbol("F0_%d" % k) for k, ff in enumerate(FN)}
    src_poly = all(sp.expand(q.subs(fsym).subs(fsym0)).is_polynomial(S) for q in src)
    q6c = sp.expand(MG[0] - m2*sp.eye(4)) == sp.zeros(4) and \
        all(MG[o][i, j].is_polynomial(S) for o in (1, 2) for i in range(4) for j in range(4)) and src_poly
    m10g = sp.Matrix(MG[1].subs(S, 0).subs(POINT))
    lam = sp.Symbol("lam")
    evg = [complex(x) for x in sp.Poly(m10g.charpoly(lam).as_expr(), lam).nroots(n=30, maxsteps=200)]
    expog = [1 - x for x in evg]
    badg = [x for x in expog if abs(x.imag) < 1e-9 and x.real > 0.5 and abs(x.real - round(x.real)) < 1e-9]
    ok["Q6 Tangherlini, O(mu)"] = q6a and q6b and q6c and not badg
    print("  Q6 (D426): Tangherlini to O(mu), l = 0: the mu^0 part is Q1's system: %s; the mu^1 part, an ODE for G with "
          "a source in F, depends on s only: %s; second-order part (s - s^2/2) I, polynomial coefficients and source: "
          "%s; G's exponents at s = 0 besides 0: %s" % (q6a, q6b, q6c, ", ".join(
              "%.6g" % x.real if abs(x.imag) < 1e-9 else "%.4g%+.3gi" % (x.real, x.imag) for x in expog)))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
