#!/usr/bin/env python3
"""harmonics5: Lemma 6.5''s self-similar reduction for every harmonic, and its transfers at gamma_C = 10^6 (D436).

The record's full flat operator L = D Ric + dstar_(E^C) delta_(E^Ups) G (coulombL5.py, genstates5.py) on
h = r^-2 F(s) (Cartesian weight), s = v/r, at the record's point (coulombL5.POINT). coulombL5 reduced l = 0 (Q1) and
the l = 1 scalar type (Q5) with explicit harmonics. Here the harmonic is kept abstract, so l enters as a parameter:

  S1 (exact) scalar type: Y(chi) zonal with Y'' = -2 cot chi Y' - kappa Y, kappa = l(l + 2); h = r^-2 Y (a dt^2 +
     2b dt dr + c dr^2) + d Y g_S3 + k (Hess Y + kappa Y g_S3/3) + 2 r^-1 (e dt + f dr) (x)_s dY. Every component of L h
     reduces, after Y'' is eliminated, to a multiple of Y, of dY or of Y g_S3 and the traceless Hessian; the off-sector
     components and the chi-dependence drop out. A 7 x 7 system in s, second-order part (s - s^2/2) I.
     Controls: at kappa = 3 with k = 0 it is coulombL5's l = 1 system (Q5); at kappa = 0 with e = f = k = 0 it is the
     l = 0 system (Q1).
  S2 (exact) vector type: V = U(chi) sin^2 theta dphi, divergence-free, with U'' fixed by the rough Laplacian
     Delta V = -lam V, lam = l(l + 2) - 1 (S2a checks that U = sin^2 chi, the Killing field, has lam = 2);
     h = r^-1 (p dt + q dr) (x)_s V + k (nabla V)_sym. A 3 x 3 system (2 x 2 at l = 1, where V is Killing).
  S3 (exact) tensor type: for any h with only angular components, traceless and divergence-free on S^3, the gauge
     1-form w = delta G h + E^Ups G h vanishes identically (checked on arbitrary component functions), so L h = D Ric h
     and the damping drops out: the tensor-type transfers do not depend on gamma_C or gamma_Ups.
  T  (computed, series at 30 digits, 400 against 600 terms) for l = 1 ... LMAX: the scalar- and vector-type transfers
     F(0) -> F(1) at gamma_C = 10^6 and at gamma_C = 10^5, the exponents at N besides 0, and the size of each transfer.
  G  the growth in l: the norms of the k-th derivative transfers F(0) -> F^(k)(1), k = 0 ... 3, in the basis
     normalised by each harmonic's own L^2(S^3) size (|Y|^2, |dY|^2 = kappa |Y|^2, |Hess^0 Y|^2 = (2/3) kappa
     (kappa - 3) |Y|^2, |(nabla V)_sym|^2 = 2 (kappa - 3) |V|^2), and the exponent p of a fit ~ l^p over the last l.
"""
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.core.function import AppliedUndef

sys.path.insert(0, __file__.rsplit("/", 1)[0])
sys.path.insert(0, __file__.rsplit("/", 2)[0])
import coulombL5 as C  # noqa: E402
import genstates5 as GS  # noqa: E402

t, r, ch, th = GS.t, GS.r, GS.ch, GS.th
S, gC, eC, vC, gU, eU = C.S, C.gC, C.eC, C.vC, C.gU, C.eU
kap, lam = sp.symbols("kappa lambda", positive=True)
y0, y1 = sp.symbols("y0 y1")
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6


def ec_term(w, G):
    X, g, gi, Gam, f_ = G
    N = len(X)
    cc = [1/r, -vC/r, 0, 0, 0]
    cw = sum(gi[p, q]*cc[p]*w[q] for p in range(N) for q in range(N))
    m = sp.Rational(2, 3)*(1 - eC)
    return sp.Matrix(N, N, lambda p, q: gC*(cc[p]*w[q] + cc[q]*w[p] - m*g[p, q]*cw))


def full_L(h, G):
    Gh = GS.Gop(h, G)
    w = [p + q for p, q in zip(GS.div(Gh, G), GS.Eups(Gh, G))]
    return GS.dric(h, G) + GS.dstar(w, G) + ec_term(w, G), w


def ode_rules(fun, second):
    """replace fun^(k), k = 5 ... 0, by expressions in y0 = fun, y1 = fun', using fun'' = second(y0, y1, chi)"""
    def dch(e):
        return sp.diff(e, ch) + sp.diff(e, y0)*y1 + sp.diff(e, y1)*second
    hi = {0: y0, 1: y1}
    for k in range(2, 6):
        hi[k] = sp.expand(dch(hi[k - 1]))

    def apply(e):
        e = e.doit()
        for k in range(5, 0, -1):
            e = e.subs(sp.Derivative(fun, (ch, k)), hi[k])
        return sp.expand(e.subs(fun, y0))
    return apply


def simp_lin(e):
    """e linear in the unknown functions and their derivatives: simplify each coefficient on its own, after writing
    tan and cot through sin and cos (sympy leaves tan(chi) cot(chi) standing inside large expressions)"""
    e = sp.expand(sp.sympify(e).subs({sp.tan(ch): sp.sin(ch)/sp.cos(ch), sp.cot(ch): sp.cos(ch)/sp.sin(ch)}))
    if e == 0:
        return sp.Integer(0)
    terms = sorted(e.atoms(sp.Derivative) | e.atoms(AppliedUndef), key=sp.default_sort_key)
    d = sp.collect(e, terms, evaluate=False)
    return sp.Add(*[k_*sp.simplify(sp.trigsimp(sp.cancel(v))) for k_, v in d.items()])


def coeffs(e):
    """e linear in y0, y1: (coefficient of y0, coefficient of y1), simplified"""
    e = sp.expand(e)
    return simp_lin(e.coeff(y0)), simp_lin(e.coeff(y1))


FS = [sp.Function(n) for n in ("a", "b", "c", "d", "e", "f", "k")]
FV = [sp.Function(n) for n in ("p", "q", "kv")]


def to_s(e):
    return simp_lin(sp.expand(e.subs(t, (S - 1)*r).doit()))


def reduce_scalar():
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    sx = (t + r)/r
    a, b, c, d, e, f, k = FS
    Y = sp.Function("Y")(ch)
    dY = sp.diff(Y, ch)
    h = sp.zeros(N)
    h[0, 0], h[1, 1] = Y*a(sx)/r**2, Y*c(sx)/r**2
    h[0, 1] = h[1, 0] = Y*b(sx)/r**2
    for i in (2, 3, 4):
        h[i, i] = g[i, i]*Y*d(sx)/r**2
    Hcc = sp.diff(Y, ch, 2) + kap*Y/3
    Htt = sp.sin(ch)*sp.cos(ch)*dY + kap*Y*sp.sin(ch)**2/3
    h[2, 2] += k(sx)*Hcc
    h[3, 3] += k(sx)*Htt
    h[4, 4] += k(sx)*Htt*sp.sin(th)**2
    h[0, 2] = h[2, 0] = dY*e(sx)/r
    h[1, 2] = h[2, 1] = dY*f(sx)/r
    L, _ = full_L(h, G)
    rule = ode_rules(Y, -2*sp.cot(ch)*y1 - kap*y0)
    R = {(i, j): rule(L[i, j]) for i in range(N) for j in range(i, N)}
    out, checks = {}, []
    for (i, j), wt in (((0, 0), 4), ((0, 1), 4), ((1, 1), 4)):
        c0, c1 = coeffs(R[(i, j)]*r**wt)
        checks.append(c1 == 0)
        out[(i, j)] = c0
    for (i, j), name in (((0, 2), "e"), ((1, 2), "f")):
        c0, c1 = coeffs(R[(i, j)]*r**3)
        checks.append(c0 == 0)
        out[name] = c1
    t0, t1 = coeffs(R[(3, 3)]*r**2/sp.sin(ch)**2)
    B = simp_lin(t1*sp.sin(ch)/sp.cos(ch))
    A = simp_lin(t0 - kap*B/3)
    x0, x1 = coeffs(R[(2, 2)]*r**2)
    checks.append(simp_lin(x0 - (A - 2*kap*B/3)) == 0)
    checks.append(simp_lin(x1 + 2*B*sp.cos(ch)/sp.sin(ch)) == 0)
    checks.append(simp_lin(R[(4, 4)] - sp.sin(th)**2*R[(3, 3)]) == 0)
    for (i, j) in ((0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)):
        checks.append(simp_lin(R[(i, j)]) == 0)
    eqs = [out[(0, 0)], out[(0, 1)], out[(1, 1)], A, out["e"], out["f"], B]
    eqs = [to_s(q) for q in eqs]
    free = all(q.free_symbols <= {S, gU, eU, gC, eC, vC, kap} for q in eqs)
    return eqs, all(checks) and free, checks


def vector_ode():
    """the rough Laplacian of V = U(chi) sin^2 theta dphi on the unit S^3, its phi component over sin^2 theta"""
    U = sp.Function("U")(ch)
    x = (ch, th, GS.ph)
    gm = sp.diag(1, sp.sin(ch)**2, sp.sin(ch)**2*sp.sin(th)**2)
    gmi = gm.inv()
    n = 3
    Gm = [[[sp.simplify(sum(gmi[l, m] * (sp.diff(gm[m, i], x[j]) + sp.diff(gm[m, j], x[i]) - sp.diff(gm[i, j], x[m]))
                            for m in range(n)) / 2) for j in range(n)] for i in range(n)] for l in range(n)]
    V = [0, 0, U*sp.sin(th)**2]
    dV = [[sp.diff(V[b], x[a]) - sum(Gm[c][a][b]*V[c] for c in range(n)) for b in range(n)] for a in range(n)]
    ddV = [[[sp.diff(dV[b][cc], x[a]) - sum(Gm[e][a][b]*dV[e][cc] + Gm[e][a][cc]*dV[b][e] for e in range(n))
             for cc in range(n)] for b in range(n)] for a in range(n)]
    lap = [sp.simplify(sum(gmi[a, b]*ddV[a][b][cc] for a in range(n) for b in range(n))) for cc in range(n)]
    divV = sp.simplify(sum(gmi[a, b]*dV[a][b] for a in range(n) for b in range(n)))
    sol = sp.solve(sp.Eq(lap[2]/sp.sin(th)**2, -lam*U), sp.diff(U, ch, 2))[0]
    kill = sp.simplify((lap[2] + lam*V[2]).subs(lam, 2).subs(U, sp.sin(ch)**2).doit())
    return U, sp.simplify(sol), divV == 0 and sp.simplify(lap[0]) == 0 and sp.simplify(lap[1]) == 0, kill == 0


def reduce_vector():
    U, second, ok_div, ok_kill = vector_ode()
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    sx = (t + r)/r
    p, q, k = FV
    dU = sp.diff(U, ch)
    h = sp.zeros(N)
    h[0, 4] = h[4, 0] = p(sx)*U*sp.sin(th)**2/r
    h[1, 4] = h[4, 1] = q(sx)*U*sp.sin(th)**2/r
    h[2, 4] = h[4, 2] = k(sx)*(dU - 2*sp.cot(ch)*U)*sp.sin(th)**2
    L, _ = full_L(h, G)
    rule = ode_rules(U, second.subs({sp.diff(U, ch): y1, U: y0}))
    R = {(i, j): rule(L[i, j]) for i in range(N) for j in range(i, N)}
    checks = [ok_div, ok_kill]
    eqs = []
    for (i, j), wt in (((0, 4), 3), ((1, 4), 3)):
        c0, c1 = coeffs(R[(i, j)]*r**wt/sp.sin(th)**2)
        checks.append(c1 == 0)
        eqs.append(c0)
    c0, c1 = coeffs(R[(2, 4)]*r**2/sp.sin(th)**2)
    checks.append(simp_lin(c0 + 2*sp.cos(ch)/sp.sin(ch)*c1) == 0)
    eqs.append(c1)
    for (i, j) in ((0, 0), (0, 1), (1, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (3, 3), (4, 4), (2, 3), (3, 4)):
        checks.append(simp_lin(R[(i, j)]) == 0)
    eqs = [to_s(e) for e in eqs]
    free = all(e.free_symbols <= {S, gU, eU, gC, eC, vC, lam} for e in eqs)
    return eqs, all(checks) and free, checks


def tensor_w():
    """S3: w for an angular, traceless, S^3-divergence-free h with arbitrary components"""
    G = GS.geo(4, True)
    X, g, gi, Gam, f_ = G
    N = 5
    names = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4)]
    H = {ij: sp.Function("H%d%d" % ij)(t, r, ch, th, GS.ph) for ij in names}
    h = sp.zeros(N)
    for (i, j), v in H.items():
        h[i, j] = h[j, i] = v
    h[4, 4] = -g[4, 4]*(gi[2, 2]*h[2, 2] + gi[3, 3]*h[3, 3])     # traceless
    w = [sp.simplify(q) for q in [p + e for p, e in zip(GS.div(GS.Gop(h, G), G), GS.Eups(GS.Gop(h, G), G))]]
    # the S^3 divergence of h_AB / r^2: w_A must be -(1/r^2) (div_S3 h)_A, which vanishes for divergence-free h
    xs = (ch, th, GS.ph)
    gm = sp.diag(1, sp.sin(ch)**2, sp.sin(ch)**2*sp.sin(th)**2)
    gmi = gm.inv()
    Gm = [[[sp.simplify(sum(gmi[l, m] * (sp.diff(gm[m, i], xs[j]) + sp.diff(gm[m, j], xs[i]) - sp.diff(gm[i, j], xs[m]))
                            for m in range(3)) / 2) for j in range(3)] for i in range(3)] for l in range(3)]
    hA = sp.Matrix(3, 3, lambda i, j: h[i + 2, j + 2])
    divS = [sum(gmi[a, c]*(sp.diff(hA[a, b], xs[c]) - sum(Gm[e][c][a]*hA[e, b] + Gm[e][c][b]*hA[a, e] for e in range(3)))
                for a in range(3) for c in range(3)) for b in range(3)]
    ok_tr = sp.simplify(w[0]) == 0 and sp.simplify(w[1]) == 0
    ok_ang = all(sp.simplify(w[b + 2] + divS[b]/r**2) == 0 for b in range(3))
    return ok_tr and ok_ang


def matrices_n(eqs, funs):
    n = len(funs)
    sym = {}
    for i, fn in enumerate(funs):
        sym[sp.Derivative(fn(S), (S, 2))] = sp.Symbol("q2_%d" % i)
        sym[sp.Derivative(fn(S), S)] = sp.Symbol("q1_%d" % i)
    out = []
    for e in eqs:
        e2 = e.subs(sym).subs({fn(S): sp.Symbol("q0_%d" % i) for i, fn in enumerate(funs)})
        out.append(sp.expand(e2))
    M = [sp.Matrix(n, n, lambda i, j: out[i].coeff(sp.Symbol("q%d_%d" % (o, j)))) for o in (2, 1, 0)]
    rest = [sp.expand(out[i] - sum(M[o][i, j]*sp.Symbol("q%d_%d" % (2 - o, j)) for o in range(3) for j in range(n)))
            for i in range(n)]
    return M, rest


def series_transfer_n(M, sub, nterms=400, dps=30, nder=0):
    mp.mp.dps = dps
    n = M[0].shape[0]
    Cs, deg = {}, 0
    for o in range(3):
        for i in range(n):
            for j in range(n):
                P = sp.Poly(sp.expand(M[o][i, j].subs(sub)), S)
                for (pw,), val in P.terms():
                    Cs.setdefault((o, pw), mp.matrix(n, n))
                    v = sp.Rational(val)
                    Cs[(o, pw)][i, j] = mp.mpf(v.p)/v.q
                    deg = max(deg, pw)
    T = mp.matrix(n, n)
    Td = [mp.matrix(n, n) for _ in range(nder + 1)]
    last = mp.mpf(0)
    for j0 in range(n):
        F = [mp.matrix(n, 1)]
        F[0][j0] = 1
        total = F[0]*1
        for m in range(1, nterms):
            A = mp.matrix(n, n)
            rhs = mp.matrix(n, 1)
            for (o, pw), Cm in Cs.items():
                kk = m - 1 - pw + (2 - o)
                if kk < 0 or kk > m:
                    continue
                fac = 1
                for qq in range(2 - o):
                    fac *= (kk - qq)
                if kk == m:
                    A += Cm*fac
                else:
                    rhs -= Cm*F[kk]*fac
            Fm = mp.lu_solve(A, rhs)
            F.append(Fm)
            total += Fm
        for i in range(n):
            T[i, j0] = total[i]
        for kd in range(nder + 1):
            tot = mp.matrix(n, 1)
            for m in range(kd, len(F)):
                fac = 1
                for qq in range(kd):
                    fac *= (m - qq)
                tot += F[m]*fac
            for i in range(n):
                Td[kd][i, j0] = tot[i]
        last = max(last, max(abs(x) for x in F[-1]))
    if nder:
        return T, last, Td
    return T, last


def transfers(M, sub, label):
    m10 = np.array(sp.Matrix(M[1].subs(S, 0).subs(sub)).evalf(), dtype=complex)
    expo = 1 - np.linalg.eigvals(m10)
    bad = [x for x in expo if abs(x.imag) < 1e-9 and x.real > 0.5 and abs(x.real - round(x.real)) < 1e-6]
    T4, _ = series_transfer_n(M, sub, 400)
    T6, last, Td = series_transfer_n(M, sub, 600, nder=3)
    n = M[0].shape[0]
    A = np.array([[float(T6[i, j]) for j in range(n)] for i in range(n)])
    Ad = [np.array([[float(X[i, j]) for j in range(n)] for i in range(n)]) for X in Td]
    d46 = float(max(abs(T4[i, j] - T6[i, j]) for i in range(n) for j in range(n)))
    return A, d46, float(last), sorted(expo.real), bad, Ad


def weights(typ, l, n):
    kv = l*(l + 2)
    if typ == "scalar":
        w = [1, 1, 1, 3**0.5, (2*kv)**0.5, (2*kv)**0.5, (2*kv*(kv - 3)/3)**0.5][:n]
    else:
        w = [2**0.5, 2**0.5, (2*(kv - 3))**0.5][:n]
    return np.diag(w)


def main():
    ok = {}
    eqsS, okS, chS = reduce_scalar()
    MS, restS = matrices_n(eqsS, FS)
    m2 = S - S**2/2
    okS2 = all(x == 0 for x in restS) and sp.expand(MS[0] - m2*sp.eye(7)) == sp.zeros(7) and \
        all(MS[o][i, j].is_polynomial(S) for o in (1, 2) for i in range(7) for j in range(7))
    # controls against coulombL5's explicit reductions
    e1 = C.reduce_l1()
    M1, _ = C.matrices6(e1[:6])
    sub3 = {kap: 3}
    MS1 = [sp.Matrix(6, 6, lambda i, j: MS[o][i, j].subs(sub3)) for o in range(3)]
    ctl1 = all(sp.expand(MS1[o] - M1[o]) == sp.zeros(6) for o in range(3))
    e0 = C.reduce()
    M0, _ = C.matrices(e0[:4])
    MS0 = [sp.Matrix(4, 4, lambda i, j: MS[o][i, j].subs(kap, 0)) for o in range(3)]
    ctl0 = all(sp.expand(MS0[o] - M0[o]) == sp.zeros(4) for o in range(3))
    ok["S1"] = okS and okS2 and ctl0 and ctl1
    print("  S1 scalar type, kappa symbolic: sector closes and chi drops out: %s (%d checks); second-order part "
          "(s - s^2/2) I, polynomial coefficients: %s; = coulombL5 l = 0 at kappa = 0: %s; = l = 1 (Q5) at kappa = 3: %s"
          % (okS, len(chS), okS2, ctl0, ctl1), flush=True)
    eqsV, okV, chV = reduce_vector()
    MV, restV = matrices_n(eqsV, FV)
    okV2 = all(x == 0 for x in restV) and sp.expand(MV[0] - m2*sp.eye(3)) == sp.zeros(3) and \
        all(MV[o][i, j].is_polynomial(S) for o in (1, 2) for i in range(3) for j in range(3))
    ok["S2"] = okV and okV2
    print("  S2 vector type, lambda symbolic: divergence-free, Killing at lambda = 2, sector closes: %s (%d checks); "
          "second-order part (s - s^2/2) I, polynomial coefficients: %s" % (okV, len(chV), okV2), flush=True)
    ok["S3"] = tensor_w()
    print("  S3 tensor type: w = delta G h + E^Ups G h vanishes for angular traceless h, its angular part being "
          "-(div_S3 h)/r^2: %s, so the damping drops out" % ok["S3"], flush=True)
    rows = []
    good = True
    for l in range(1, LMAX + 1):
        for typ, Mx, n, par in (("scalar", MS, 7 if l >= 2 else 6, {kap: l*(l + 2)}),
                                ("vector", MV, 3 if l >= 2 else 2, {lam: l*(l + 2) - 1})):
            Ml = [sp.Matrix(n, n, lambda i, j: Mx[o][i, j].subs(par)) for o in range(3)]
            out = {}
            for gc in (10**5, 10**6):
                sub = dict(C.POINT)
                sub[gC] = gc
                out[gc] = transfers(Ml, sub, typ)
            A6, d46, last, expo, bad, Ad = out[10**6]
            A5 = out[10**5][0]
            dlim = float(np.max(np.abs(A6 - A5)))
            nrm = float(np.linalg.norm(A6, 2))
            Wt = weights(typ, l, n)
            nn = [float(np.linalg.norm(Wt @ X @ np.linalg.inv(Wt), 2)) for X in Ad]
            rows.append((l, typ, n, nrm, d46, last, dlim, expo, bad, A6, nn))
            good = good and d46 < 1e-12 and not bad
            print("  T: l = %d %s (%d functions): ||T(1e6)||_2 = %.6g; series 400 vs 600 %.1e (last term %.1e); "
                  "|T(1e6) - T(1e5)| = %.2e; exponents at N besides 0: %s%s"
                  % (l, typ, n, nrm, d46, last, dlim, ", ".join("%.4g" % x for x in expo if abs(x) > 1e-9),
                     "; RESONANT %s" % bad if bad else ""), flush=True)
    ok["T"] = good
    for typ in ("scalar", "vector"):
        rr = [q for q in rows if q[1] == typ]
        print("  G: %s type, normalised norms of F(0) -> F^(k)(1), k = 0 ... 3:" % typ)
        for q in rr:
            print("      l = %2d: %s" % (q[0], "  ".join("%10.4g" % x for x in q[10])))
        if len(rr) >= 3:
            l1, l2 = rr[-3][0], rr[-1][0]
            ps = [np.log(rr[-1][10][k]/rr[-3][10][k])/np.log(l2/l1) for k in range(4)]
            print("      fitted exponent p in l^p from l = %d to %d: %s" % (l1, l2, ", ".join("%.2f" % x for x in ps)))
    for l, typ, n, nrm, d46, last, dlim, expo, bad, A6, nn in rows:
        if l <= 2:
            print("  T(1e6), l = %d %s:" % (l, typ))
            for i in range(n):
                print("      " + "  ".join("%+.6f" % A6[i, j] for j in range(n)))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
