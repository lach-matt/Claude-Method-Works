#!/usr/bin/env python3
"""dual5.py -- [Hin26] section 7.2 in five dimensions: the zero energy dual states of the constraint propagation
operator (N1STAR-PROOF.md section 10.31; ROUTES-OPEN.md 4.32; D86).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 7.2 records the large zero energy states of the adjoint (box^C)* = 2 (delta*_(g,
E^C))* G delta* ((7.11)) of the constraint propagation operator box^C = 2 delta G (delta* + E^C): Lemma 7.2 (its zero
energy operator invertible on the weights (0, C_0 + 1], its indicial roots 1 - conj(lam), (7.10)), Proposition 7.3 (the
dual states from the Minkowskian Killing 1-forms, their trace-reversed symmetric gradients h* in (7.15) decaying at
rho^2) and section 7.2.1 (the v1 dual states near a = 0: Lemma 7.5's -2 m rho^2 (dt* + dr) (x)_s rho V(S'), (7.20), and
Proposition 7.4's (7.18), from N_v1(rho^-2 box*(0), 1) = 2 + 4 gam_C v_C).  Here box^C with C omega = h^-1 (2 c (x)_s
omega - m (1 - e) g iota_c omega), c = r^-1 (dt - v dr), m = 2/(D - 2) and h = 1/gam_C (10.12), its formal adjoint 2
(delta + C*) G delta*, C* k = h^-1 (2 iota_(g^-1 c) k - m (1 - e) c tr k); on 4+1 Minkowski and Tangherlini, f = 1 -
mu/r^2, and on the one-spin Myers-Perry metric at first order in its rotation, g_T - a h_A (10.28(vi)); 3+1 Minkowski,
Schwarzschild and Kerr at first order in a are the control.

  A1 (computed, exact) The adjoint's indicial families.  For s0, sl (l <= 3) and vl (l <= 3), det N*(lam) = det N(2 -
     lam) exactly, N the indicial family of box^C (four dimensions det N(1 - lam): his (7.10)); box^C's polynomials are
     10.12's (damping5.py) at kappa = l (l + 2); the v1 roots of box^C are 3 and -1 - 2 v gam_C, so the adjoint's are -1
     and 3 + 2 v gam_C (four dimensions his (7.8), 2 and -1 - 2 v gam_C); and N*_v1(1) = 2 + 4 gam_C v_C in four
     dimensions (his p. 143), N*_v1(2) = 3 + 6 gam_C v_C in five.  Control: the shift 1 claimed in five dimensions.
  A2 (computed, exact) The translations' dual state.  On Tangherlini, with dx = d(r S), S = cos chi, the source
     box^C*(dx) vanishes to order rho^3 and has its leading term at rho^4 (four dimensions: rho^3, his proof of
     Proposition 7.3); the correction omega' = rho^2 (a S d xbar^0 + b S d xbar^1 + c r dS) cancelling it is unique (2
     no root of the adjoint's s1 polynomial; four dimensions rho^1); and h*_s1 = G delta*(dx + omega') vanishes to order
     rho^2 with a nonzero leading term at rho^3 (four dimensions rho^2, his (7.15)).  Control: the four-dimensional order
     rho^2 claimed in five dimensions.
  A3 (computed, exact) The rotations' dual states near a = 0.  At first order in a, with V a rotation 1-form and V_a =
     g_a gbar^-1 V: delta*_(g_a) V_a = (a/2) L_R k is -(mu/r^4) a dt (x)_s V' on Myers-Perry, k = -h_A (four dimensions,
     Kerr: -(2M/r^3) a dt (x)_s V', his (7.20)'s -2 m rho^2 (dt* + dr) (x)_s rho V(S')), V' = L_R w the rotation 1-form
     of the bracket of V's plane with the spin plane 12 -- zero for the planes 12 and 34, so two of the six rotations
     stay Killing (four dimensions one of three); the correction omega_0 = c_0 r^-3 V' (four dimensions r^-2 V') is
     unique, c_0 = -2 mu/(3 (h + 2v)) (four dimensions -2M/(h + 2v), his (7.31)); and the leading term of h-sharp, at
     rho^3 (four dimensions rho^2), is that of delta*_(g_a) V_a times (h + 2v - 2)/(h + 2v) on d xbar^0 and (h + 2v +
     2)/(h + 2v) on d xbar^1, in five dimensions as in four -- his (7.18), the same for each of the four non-Killing
     rotations.  Control: his c_0 claimed in five dimensions.

Deduced, not computed here (N1STAR-PROOF.md 10.31): his Lemma 7.2 in five dimensions on 10.21(e) (the weights (0, C_0 +
2]) with A1 and Proposition 10.9; his Proposition 7.3 there on Tangherlini, h*_s1 at rho^3 and the time translation's
and the six rotations' h* rapidly decaying; section 7.2.1's structure at first order in the rotation.

READ.  [Hin26] pp. 134-144 (section 7: (7.1)-(7.8), Theorem 7.1; section 7.2: Lemma 7.2, (7.9)-(7.11), Proposition 7.3
and its proof, (7.12)-(7.15); section 7.2.1: (7.16), Proposition 7.4, (7.17)-(7.19), Lemma 7.5 and its proof,
(7.20)-(7.28), the proof of Proposition 7.4, (7.29)-(7.35)), 126 ((6.30)-(6.32), Remarks 6.16-6.17); alphaXiv,
2026-10-23.

sympy.  python3 dual5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time
from functools import lru_cache

import sympy as sp

from damping5 import Checklist
import damping5 as D5
from genstates5 import geo, dstar, div, trace, Gop, TRIG, t, r, ch, th, ph, mu, M
from puregauge5 import basis, decompose

v, e, h = D5.v, D5.e, D5.h
lam = sp.Symbol("lam")
a = sp.Symbol("a")
rho = sp.Symbol("rho", positive=True)
LM = 3


def cvec(N):
    return [1 / r, -v / r] + [0] * (N - 2)


def Cop(w, G):
    """C omega = h^-1 (2 c (x)_s omega - m (1 - e) g iota_c omega), m = 2/(D - 2)"""
    X, g, gi, Gam, f = G
    N = len(X)
    m, c = sp.Rational(2, N - 2), cvec(N)
    cw = sum(gi[i, j] * c[i] * w[j] for i in range(N) for j in range(N))
    return sp.Matrix(N, N, lambda i, j: (c[i] * w[j] + c[j] * w[i] - m * (1 - e) * g[i, j] * cw) / h)


def Cstar(k, G):
    """its adjoint on 2-tensors: C* k = h^-1 (2 iota_(g^-1 c) k - m (1 - e) c tr k)"""
    X, g, gi, Gam, f = G
    N = len(X)
    m, c = sp.Rational(2, N - 2), cvec(N)
    cs = [sum(gi[i, j] * c[j] for j in range(N)) for i in range(N)]
    tr = trace(k, G)
    return [(2 * sum(cs[i] * k[i, j] for i in range(N)) - m * (1 - e) * c[j] * tr) / h for j in range(N)]


def boxC(w, G):
    return [2 * q for q in div(Gop(dstar(w, G) + Cop(w, G), G), G)]


def boxCs(w, G):
    Gh = Gop(dstar(w, G), G)
    return [2 * (x + y) for x, y in zip(div(Gh, G), Cstar(Gh, G))]


@lru_cache(maxsize=None)
def fam(n, typ, l, adj):
    """N(lam) of box^C (adj False) or of its adjoint (adj True) on rho^lam times the basis of puregauge5.py"""
    G = geo(n, True)
    op = boxCs if adj else boxC
    cols = []
    for E in basis(n, typ, l):
        col, ok = decompose(op([r**(-lam) * q for q in E], G), n, typ, l, TRIG)
        assert ok
        cols.append(col)
    return sp.Matrix(cols).T.applyfunc(sp.expand)


def ser(q, k):
    return sp.series(sp.cancel(q).subs(r, 1 / rho), rho, 0, k + 1).removeO()


def frame1(F):
    return [F[0], F[1]] + [F[k] / r for k in range(2, len(F))]


def frame2(H):
    N = H.shape[0]
    return sp.Matrix(N, N, lambda i, j: H[int(i), int(j)] / r**((1 if int(i) >= 2 else 0) + (1 if int(j) >= 2 else 0)))


# ------------------------------------------------------------------------------------------------- A1
def a1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for n in (4, 3):
        shift = (2 if n == 4 else 1) if control == 0 else 1
        for typ, ls in (("s0", [0]), ("s", range(1, LM + 1)), ("v", range(1, LM + 1))):
            for l in ls:
                A, B = fam(n, typ, l, False).det(), fam(n, typ, l, True).det()
                good = sp.expand(B - A.subs(lam, shift - lam)) == 0
                ok &= good
                chk(f"n + 1 = {n + 1}, {typ}{l}: det N*(lam) = det N({shift} - lam)", good)
    if control:
        return chk.ok
    pk, p0, pv = D5.polys(4, sp.Rational(2, 3))
    okp = True
    for typ, l in (("s0", 0), ("s", 1), ("s", 2), ("s", 3), ("v", 1), ("v", 2), ("v", 3)):
        A = fam(4, typ, l, False).det().subs(lam, D5.lam)
        ref = {"s0": p0, "s": pk, "v": pv}[typ].subs(D5.K, l * (l + 2))
        ratio = sp.cancel(A / ref)
        okp &= ratio.free_symbols <= {h} and ratio != 0
    chk("n + 1 = 5: box^C's polynomials are 10.12's (damping5.py) at kappa = l (l + 2), up to powers of h", okp)
    g_ = 1 / h
    r5, r4 = sp.solve(fam(4, "v", 1, False)[0], lam), sp.solve(fam(3, "v", 1, False)[0], lam)
    s5, s4 = sp.solve(fam(4, "v", 1, True)[0], lam), sp.solve(fam(3, "v", 1, True)[0], lam)
    okr = set(map(sp.simplify, r4)) == {2, sp.simplify(-1 - 2 * v * g_)}
    okr &= set(map(sp.simplify, s4)) == {-1, sp.simplify(2 + 2 * v * g_)}
    okr &= set(map(sp.simplify, r5)) == {3, sp.simplify(-1 - 2 * v * g_)}
    okr &= set(map(sp.simplify, s5)) == {-1, sp.simplify(3 + 2 * v * g_)}
    chk(f"v1: box^C roots {r5} (four dimensions {r4}, his (7.8)); the adjoint's {s5} ({s4})", okr)
    n4, n5 = fam(3, "v", 1, True)[0].subs(lam, 1), fam(4, "v", 1, True)[0].subs(lam, 2)
    okn = sp.simplify(n4 - (2 + 4 * g_ * v)) == 0 and sp.simplify(n5 - (3 + 6 * g_ * v)) == 0
    chk(f"N*_v1(1) = {sp.simplify(n4)} in four dimensions (his p. 143: 2 + 4 gam v); N*_v1(2) = {sp.simplify(n5)} in "
        f"five", okn)
    return chk.ok and ok


# ------------------------------------------------------------------------------------------------- A2
@lru_cache(maxsize=None)
def s1_dual(n):
    """the translation dx = d(r S), S = cos(zonal angle), on Tangherlini (n = 4) / Schwarzschild (n = 3)"""
    G = geo(n, False)
    X = G[0]
    N = len(X)
    S = sp.cos(X[2])
    dx = [sp.diff(r * S, q) for q in X]
    A_, B_, C_ = sp.symbols("A B C")
    p = 2 if n == 4 else 1
    wp = [r**(-p) * (A_ + B_) * S, r**(-p) * (A_ - B_) * S, r**(-p) * C_ * r * sp.diff(S, X[2])] + [0] * (N - 3)
    kf = p + 2
    F0 = [ser(q, kf) for q in frame1(boxCs(dx, G))]
    low = all(sp.simplify(q.coeff(rho, j)) == 0 for q in F0 for j in range(kf))
    lead = [sp.factor(q.coeff(rho, kf)) for q in F0]
    F = [ser(q, kf) for q in frame1(boxCs([x + y for x, y in zip(dx, wp)], G))]
    pt = {sp.cos(X[2]): sp.Rational(4, 5), sp.sin(X[2]): sp.Rational(3, 5)}
    sol = sp.solve([sp.expand(q.coeff(rho, kf).subs(pt)) for q in F], [A_, B_, C_], dict=True)
    if len(sol) != 1:
        return low, lead, None, None, None
    w = [sp.sympify(x + y).subs(sol[0]) for x, y in zip(dx, wp)]
    H = frame2(Gop(dstar(w, G), G)).applyfunc(lambda q: ser(q, p + 1))
    hlow = all(sp.simplify(H[i, j].coeff(rho, k)) == 0 for i in range(N) for j in range(N) for k in range(p + 1))
    lead_h = H.applyfunc(lambda q: sp.factor(q.coeff(rho, p + 1)))
    return low, lead, {k: sp.factor(x) for k, x in sol[0].items()}, hlow, lead_h


def a2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4, 3) if control == 0 else (4,)):
        low, lead, sol, hlow, H = s1_dual(n)
        p = 2 if n == 4 else 1
        if control:                                                     # control: rho^2 claimed in five dimensions
            nz = H is not None and any(sp.simplify(q) != 0 for q in H)
            chk("n + 1 = 5: h*_s1 has its leading term at rho^2", not hlow and nz)
            return chk.ok
        okf = low and any(q != 0 for q in lead)
        chk(f"n + 1 = {n + 1}: box^C*(dx) = O(rho^{p + 2}), leading term (frame) {lead}", okf)
        chk(f"n + 1 = {n + 1}: the correction rho^{p} (a, b, c) unique: {sol}", sol is not None)
        nz = H is not None and any(sp.simplify(q) != 0 for q in H)
        chk(f"n + 1 = {n + 1}: h*_s1 = O(rho^{p + 1}) with a nonzero leading term", bool(hlow) and nz)
    return chk.ok


# ------------------------------------------------------------------------------------------------- A3
def cart(n, X):
    rr = X[1]
    if n == 4:
        c, ta, p_ = X[2], X[3], X[4]
        return [rr * sp.sin(c) * sp.sin(ta) * sp.cos(p_), rr * sp.sin(c) * sp.sin(ta) * sp.sin(p_),
                rr * sp.sin(c) * sp.cos(ta), rr * sp.cos(c)]
    ta, p_ = X[2], X[3]
    return [rr * sp.sin(ta) * sp.cos(p_), rr * sp.sin(ta) * sp.sin(p_), rr * sp.cos(ta)]


def rot1(n, X, i, j):
    """the rotation 1-form x^i dx^j - x^j dx^i in the coordinates X"""
    x = cart(n, X)
    return [sp.expand(x[i] * sp.diff(x[j], q) - x[j] * sp.diff(x[i], q)) for q in X]


def at(x):
    """the value at the generic angles, the trig expanded first so that no combined angle escapes"""
    return sp.cancel(sp.expand_trig(sp.sympify(x)).subs(TRIG))


def geo_lin(g, gi, X):
    N = len(X)
    Gam = [[[sum(gi[l, k] * (sp.diff(g[k, m], X[nn]) + sp.diff(g[k, nn], X[m]) - sp.diff(g[m, nn], X[k]))
                 for k in range(N)) / 2 for nn in range(N)] for m in range(N)] for l in range(N)]
    return X, g, gi, Gam, None


def d0(q):
    """the first-order coefficient in a"""
    return sp.diff(sp.sympify(q), a).subs(a, 0)


@lru_cache(maxsize=None)
def rot_dual(n, plane):
    """at first order in a: delta*_(g_a) V_a, its bracket V', the correction omega_0 and h-sharp's leading term"""
    X, gT, gTi, GamT, fT = geo(n, False)
    G = (X, gT, gTi, GamT, fT)
    N = len(X)
    w = rot1(n, X, 0, 1)                                                  # the spin plane 12
    cm, nn = (mu, 4) if n == 4 else (2 * M, 3)
    dt = [1] + [0] * (N - 1)
    k = sp.Matrix(N, N, lambda i, j: -(cm / r**nn) * (dt[int(i)] * w[int(j)] + w[int(i)] * dt[int(j)]))
    ga = gT + a * k
    gai = gTi - a * gTi * k * gTi
    Ga = geo_lin(ga, gai, X)
    gbi = sp.diag(-1, 1, *[gTi[i, i] for i in range(2, N)])               # Minkowski's inverse, same angles
    V = rot1(n, X, *plane)
    Va = list(ga * gbi * sp.Matrix(V))
    hV = dstar(Va, Ga).applyfunc(lambda q: sp.simplify(d0(q)))
    # V' from the dt (x)_s components: hV_tj = -(cm/r^nn) V'_j / 2
    Vp = [sp.expand(sp.expand_trig(sp.cancel(-2 * r**nn * hV[0, j] / cm))) for j in range(N)]
    pure = all(sp.simplify(hV[i, j]) == 0 for i in range(1, N) for j in range(1, N)) and hV[0, 0] == 0
    form = all(sp.simplify(hV[0, j] + (cm / r**nn) * Vp[j] / 2) == 0 for j in range(N))
    if all(q == 0 for q in Vp):
        return dict(Vp=Vp, pure=pure, form=form, zero=True)
    q = 3 if n == 4 else 2
    c0 = sp.Symbol("c0")
    om = [c0 * r**(-q) * x for x in Vp]
    kf = q + 1
    f1 = [2 * (x + y) for x, y in zip(div(Gop(hV, G), G), Cstar(Gop(hV, G), G))]
    F = [ser(x, kf) for x in frame1([u + s for u, s in zip(f1, boxCs(om, G))])]
    low = all(sp.simplify(x.coeff(rho, j)) == 0 for x in F for j in range(kf))
    eqs = [sp.expand(at(x.coeff(rho, kf))) for x in F]
    eqs = [x for x in eqs if x != 0]
    sol = sp.solve(eqs, [c0], dict=True)
    if len(sol) != 1:
        return dict(Vp=Vp, pure=pure, form=form, zero=False, sol=None)
    hs = (Gop(hV, G) + Gop(dstar([sp.sympify(x).subs(sol[0]) for x in om], G), G))
    hL = frame2(Gop(hV, G)).applyfunc(lambda x: ser(x, q))
    hS = frame2(hs).applyfunc(lambda x: ser(x, q))
    e0, e1 = (sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(1, 2), -sp.Rational(1, 2))

    def proj(H, u):                                                       # H(u, .) on the angular directions
        return [sum(u[i] * H[i, j] for i in range(2)) for j in range(2, N)]
    ratios = []
    for u in (e0, e1):
        num = [at(x.coeff(rho, q)) for x in proj(hS, u)]
        den = [at(x.coeff(rho, q)) for x in proj(hL, u)]
        rs = {sp.factor(x / y) for x, y in zip(num, den) if y != 0}
        ratios.append(rs.pop() if len(rs) == 1 else None)
    lowL = all(sp.simplify(hL[i, j].coeff(rho, s)) == 0 for i in range(N) for j in range(N) for s in range(q))
    lowS = all(sp.simplify(hS[i, j].coeff(rho, s)) == 0 for i in range(N) for j in range(N) for s in range(q))
    return dict(Vp=Vp, pure=pure, form=form, zero=False, sol=sp.factor(sol[0][c0]), low=low and lowL and lowS,
                ratios=ratios)


def a3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    want = [(h + 2 * (v - 1)) / (h + 2 * v), (h + 2 * (v + 1)) / (h + 2 * v)]
    c05 = -2 * mu / (h + 2 * v) if control else -2 * mu / (3 * (h + 2 * v))   # control 1: his c_0 in five dimensions
    X5 = geo(4, False)[0]
    R5 = rot_dual(4, (0, 2))
    good5 = R5["pure"] and R5["form"] and not R5["zero"] and R5.get("sol") is not None and R5["low"]
    good5 &= sp.simplify(R5.get("sol", 0) - c05) == 0
    good5 &= all(sp.simplify(x - y) == 0 for x, y in zip(R5["Vp"], rot1(4, X5, 1, 2)))
    good5 &= all(x is not None and sp.simplify(x - y) == 0 for x, y in zip(R5.get("ratios", [None, None]), want))
    chk(f"n + 1 = 5 (Myers-Perry at first order, V = x^1 dx^3 - x^3 dx^1): delta* V_a = -(mu/r^4) a dt (x)_s V', V' = "
        f"x^2 dx^3 - x^3 dx^2; c_0 = {R5.get('sol')}; h-sharp / delta* V_a on d xbar^0, d xbar^1: {R5.get('ratios')}",
        good5)
    if control:
        return chk.ok
    okz = True
    for pl in ((0, 1), (2, 3)):
        R = rot_dual(4, pl)
        okz &= R["zero"] and R["pure"]
    for pl in ((0, 3), (1, 2), (1, 3)):
        R = rot_dual(4, pl)
        okz &= not R["zero"] and sp.simplify(R["sol"] - c05) == 0 and all(sp.simplify(x - y) == 0
                                                                          for x, y in zip(R["ratios"], want))
    chk("n + 1 = 5: the rotations in the planes 12 and 34 stay Killing (V' = 0); those in 13, 14, 23, 24 give the same "
        "c_0 and ratios", okz)
    R4 = rot_dual(3, (0, 2))
    good4 = R4["pure"] and R4["form"] and not R4["zero"] and R4.get("sol") is not None and R4["low"]
    good4 &= sp.simplify(R4["sol"] + 2 * M / (h + 2 * v)) == 0
    good4 &= all(x is not None and sp.simplify(x - y) == 0 for x, y in zip(R4["ratios"], want))
    V23 = rot1(3, geo(3, False)[0], 1, 2)
    good4 &= all(sp.simplify(x - y) == 0 for x, y in zip(R4["Vp"], V23))
    chk(f"n + 1 = 4 (Kerr at first order): delta* V_a = -(2M/r^3) a dt (x)_s V', his (7.20); c_0 = {R4.get('sol')}, his "
        f"(7.31) -2 m gam/(1 + 2 v gam); ratios {R4.get('ratios')}, his (7.18)", good4)
    R12 = rot_dual(3, (0, 1))
    chk("n + 1 = 4: the spin axis's rotation stays Killing (V' = 0)", R12["zero"] and R12["pure"])
    return chk.ok


CHECKS = [("A1 the adjoint's indicial roots 2 - lam (four dimensions 1 - lam, his (7.10)); his (7.8) and p. 143", a1, 1),
          ("A2 translations' dual state: source rho^4, correction rho^2, h*_s1 at rho^3 (four dimensions rho^2)", a2, 1),
          ("A3 rotations near a = 0: Lemma 7.5's term at rho^3, h-sharp's ratios; his (7.18) in four dimensions", a3, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state_ = "PASS" if good and not control else "FAIL"
        ok_all &= state_ == "PASS"
        print(f"{name:<112} {state_}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"dual5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"dual5.py mutants: {caught}/{total}")
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
