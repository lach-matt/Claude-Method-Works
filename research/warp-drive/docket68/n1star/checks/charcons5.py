#!/usr/bin/env python3
"""charcons5: the gauge-reduced null constraints of D440 as ODEs along the generators (FAMILIES5 4e, D448).

charprop5 (D440) showed that on N = {u = 0} the reduced operator's components E_vv, E_vA and gamma^(AB) E_AB are C_vv,
C_vA, C_tr plus transports of W, with C_vv, C_vA, C_tr free of the transverse jets: the null constraints in the gauge W
= 0. It left open whether they can be solved. Here they are computed modulo every W-jet at p (so E = C there), with the
first and second v-derivatives of g_uu, g_uv, g_uA and the second of g_AB along N made symbolic, and their dependence on
those derivatives is read off (exact, in Q[T, tangential symbols]; the other jets random rationals):

  K1  C_vv contains no second v-derivative of g_uu, g_uv, g_uA, and of g_AB only the trace: the coefficient of d_v^2 g_AB
      is -(1/2) gamma^(AB). With the conformal class of gamma along N and g_uv given it is a second-order ODE for the
      conformal factor (Raychaudhuri).
  K2  C_vA contains no second v-derivative of g_uu, and its coefficients on d_v^2 g_uB are g^(uv) delta_A^B: with the
      conformal factor known, a second-order ODE system for g_uA.
  K3  C_tr contains d_v^2 g_uu with the coefficient -2 (g^(uv))^2 (and d_v^2 of g_uv, g_uA, g_AB, and first derivatives);
      C_vv and C_vA contain no d_v^2 g_uu: with the conformal factor and g_uA known, a second-order ODE for g_uu.
  K4  the hierarchy closes (verifier 192): redrawing g_uu and g_uA and all their jets along N other than the symbolic
      v-jets leaves C_vv unchanged; redrawing g_uu's leaves C_vA unchanged; redrawing the angular jets of g_uA leaves
      C_vA unchanged (C_vA has no angular derivative of g_uB); redrawing the angular jets of g_uu leaves C_tr unchanged;
      control: redrawing g_uu and g_uA changes C_tr.

So given the conformal class of gamma and g_uv on N (free data and a gauge choice) and H, the gauge-reduced constraints
are ODEs along each generator for the conformal factor, then g_uA, then g_uu: the first (Raychaudhuri's) nonlinear,
holding while theta stays finite, the other two linear in their unknown's second derivative. Each later step uses angular
derivatives of the earlier unknowns, so each is solved on a neighbourhood of generators, smooth in x^A, with an existence
interval uniform over S (compact). The data at S: g_uu = g_uA = 0 there, as N' = {v = 0} is null; their first
v-derivatives and theta at S are what the corner conditions fix (the mirror of D440's N1 under u <-> v, not computed
here), and the conformal factor's value at S is free (D449). The corner conditions themselves are not computed.

Run: python3 checks/charcons5.py   (n = 4 and 5, two seeds each; exact)
"""
import random
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import charprop5 as CP  # noqa: E402

U, V = CP.U, CP.V


def make2(n, seed, perturb=()):
    """charprop5.make with the v-jets of g_u* (first and second) and of g_AB (second) along N symbolic. perturb: groups
    of jets redrawn from a second generator, the rest unchanged: "uu" (g_uu and its jets along N other than the
    symbolic v-jets), "uA" (likewise for g_uA), "uu_ang" and "uA_ang" (only their jets with an angular derivative)"""
    r = random.Random(seed)
    r2 = random.Random(seed + 1000)

    def which(a, b, ders):
        """the perturbation group a jet of g_ab with these derivative indices belongs to, if any"""
        a, b = min(a, b), max(a, b)
        ang = any(e >= 2 for e in ders)
        if (a, b) == (U, U):
            return "uu" in perturb or (ang and "uu_ang" in perturb)
        if a == U and b >= 2:
            return "uA" in perturb or (ang and "uA_ang" in perturb)
        return False

    def rnd(den=10, span=5):
        return Fr(r.randint(-span, span), den)
    comps = [(a, b) for a in range(n) for b in range(a, n)]
    names = []
    for a, b in comps:
        names.append("g%d%d_u" % (a, b))
        names += ["g%d%d_u%d" % (a, b, c) for c in range(n)]
    tang1 = [(U, b) for b in range(n) if b != V] + [(U, V)]
    tang1 = sorted(set((min(a, b), max(a, b)) for a, b in tang1))
    tang2 = tang1 + [(A, B) for A in range(2, n) for B in range(A, n)]
    names += ["t1_%d%d" % ab for ab in tang1] + ["t2_%d%d" % ab for ab in tang2]
    R, *gens = ring(",".join(names), QQ)
    sym = dict(zip(names, gens))

    def c(x):
        return R(sp.Rational(x.numerator, x.denominator))

    def zero_on_n(a, b):
        a, b = min(a, b), max(a, b)
        return a == V and b >= V

    while True:
        g0 = [[Fr(0)] * n for _ in range(n)]
        g0[U][U] = rnd()
        g0[U][V] = g0[V][U] = Fr(-1) + rnd(20, 3)
        for A in range(2, n):
            g0[U][A] = g0[A][U] = rnd()
            for B in range(A, n):
                g0[A][B] = g0[B][A] = Fr(int(A == B)) + rnd(20, 3)
        gam = sp.Matrix(n - 2, n - 2, lambda i, j: sp.Rational(g0[i + 2][j + 2].numerator, g0[i + 2][j + 2].denominator))
        full = sp.Matrix(n, n, lambda i, j: sp.Rational(g0[i][j].numerator, g0[i][j].denominator))
        if all(gam[:k, :k].det() > 0 for k in range(1, n - 1)) and full.det() != 0:
            break
    if "uu" in perturb:
        g0[U][U] = Fr(r2.randint(-5, 5), 10)
    if "uA" in perturb:
        for A in range(2, n):
            g0[U][A] = g0[A][U] = Fr(r2.randint(-5, 5), 10)
    full = sp.Matrix(n, n, lambda i, j: sp.Rational(g0[i][j].numerator, g0[i][j].denominator))
    d1, d2 = {}, {}
    for a, b in comps:
        for e in range(n):
            if e == U:
                d1[a, b, e] = sym["g%d%d_u" % (a, b)]
            elif zero_on_n(a, b):
                d1[a, b, e] = R(0)
            elif e == V and (a, b) in tang1:
                d1[a, b, e] = sym["t1_%d%d" % (a, b)]
            else:
                x = rnd()
                d1[a, b, e] = c(Fr(r2.randint(-5, 5), 10) if which(a, b, (e,)) else x)
        for e in range(n):
            for f in range(e, n):
                if e == U:
                    d2[a, b, e, f] = sym["g%d%d_u%d" % (a, b, f)]
                elif zero_on_n(a, b):
                    d2[a, b, e, f] = R(0)
                elif e == V and f == V and (a, b) in tang2:
                    d2[a, b, e, f] = sym["t2_%d%d" % (a, b)]
                else:
                    x = rnd()
                    d2[a, b, e, f] = c(Fr(r2.randint(-5, 5), 10) if which(a, b, (e, f)) else x)
    gi0 = full.inv()
    return dict(
        n=n, R=R, sym=sym, g0=[[c(g0[i][j]) for j in range(n)] for i in range(n)],
        gi=[[R(gi0[i, j]) for j in range(n)] for i in range(n)],
        gamI=[[R(x) for x in row] for row in gam.inv().tolist()],
        dg=lambda a, b, e: d1[min(a, b), max(a, b), e],
        d2g=lambda a, b, e, f: d2[min(a, b), max(a, b), min(e, f), max(e, f)],
        H0=[c(rnd()) for _ in range(n)], H1=[[c(rnd()) for _ in range(n)] for _ in range(n)])


def reduce_lin(polys, forms, pivots):
    """solve each form for its pivot (whose coefficient must be a constant) and substitute, in turn"""
    polys, forms = list(polys), list(forms)
    for k, x in enumerate(pivots):
        f = forms[k]
        coef = f.diff(x)
        assert coef.is_ground and coef != 0, "pivot coefficient not a nonzero constant"
        sol = -(f - coef * x) * f.ring(1 / coef.LC)
        assert sol.diff(x) == 0
        polys = [q.compose(x, sol) for q in polys]
        forms = [q.compose(x, sol) for q in forms]
    return polys


def transverse(R, sym, p):
    """True if the polynomial p involves a transverse generator"""
    tv = [i for i, nm in enumerate(R.symbols) if str(nm).startswith("g")]
    return any(any(m[i] for i in tv) for m in p.keys())


def constraints(j):
    """C_vv, [C_vA], C_tr: E_vv, E_vA and gamma^(AB) E_AB modulo every W-jet"""
    n, R, sym = j["n"], j["R"], j["sym"]
    geo = CP.geometry(j)
    W, dW, E = geo["W"], geo["dW"], geo["E"]
    S_ = list(range(2, n))
    piv = [sym["g%d%d_u" % (V, V)], sym["g%d%d_u%d" % (V, V, V)]] + [sym["g%d%d_u%d" % (V, V, A)] for A in S_]
    forms = [W[V], dW[V][V]] + [dW[A][V] for A in S_]
    piv += [sym["g%d%d_u" % (V, A)] for A in S_] + [sym["g%d%d_u%d" % (V, A, V)] for A in S_] \
        + [sym["g%d%d_u%d" % (V, A, C)] for A in S_ for C in S_]
    forms += [W[A] for A in S_] + [dW[V][A] for A in S_] + [dW[C][A] for A in S_ for C in S_]
    piv += [sym["g22_u"], sym["g22_u%d" % V]] + [sym["g22_u%d" % C] for C in S_]
    forms += [W[U], dW[V][U]] + [dW[C][U] for C in S_]
    trE = sum((j["gamI"][A - 2][B - 2] * E[A][B] for A in S_ for B in S_), R(0))
    red = reduce_lin([E[V][V]] + [E[V][A] for A in S_] + [trE], forms, piv)
    return red[0], red[1:-1], red[-1]


def run(n, seed):
    j = make2(n, seed)
    R, sym = j["R"], j["sym"]
    S = list(range(2, n))
    Cvv, CvA, Ctr = constraints(j)
    red = [Cvv] + CvA + [Ctr]
    ok = {"T-free": not any(transverse(R, sym, p) for p in red)}
    d = lambda p, nm: p.diff(sym[nm])
    half = R(sp.Rational(1, 2))
    # K1
    k1 = all(d(Cvv, "t2_%d%d" % ab) == 0 for ab in [(U, U), (U, V)] + [(U, A) for A in S])
    for A in S:
        for B in S:
            if A <= B:
                want = -half * j["gamI"][A - 2][B - 2] * (1 if A == B else 2)
                k1 &= d(Cvv, "t2_%d%d" % (A, B)) == want
    ok["K1"] = k1
    # K2
    k2 = all(d(c_, "t2_%d%d" % (U, U)) == 0 for c_ in CvA)
    Mt = [[d(CvA[i], "t2_%d%d" % (U, B)) for B in S] for i in range(len(S))]
    k2 &= all(m.is_ground for row in Mt for m in row)
    Mnum = sp.Matrix(len(S), len(S), lambda a, b: sp.Rational(str(Mt[a][b].LC)) if Mt[a][b] else 0)
    guv = sp.Rational(str(j["gi"][U][V].LC))
    k2 &= Mnum == guv * sp.eye(len(S))
    ok["K2"] = k2
    # K3
    cu = d(Ctr, "t2_%d%d" % (U, U))
    k3 = cu.is_ground and sp.Rational(str(cu.LC)) == -2 * guv**2
    k3 &= all(d(c_, "t2_%d%d" % (U, U)) == 0 for c_ in [Cvv] + CvA)
    ok["K3"] = k3
    # K4: the hierarchy closes (verifier 192, D449)
    same = lambda p, q: (p - q).as_expr() == 0 if p.ring != q.ring else p == q
    Pvv, _, _ = constraints(make2(n, seed, ("uu", "uA")))
    _, QvA, _ = constraints(make2(n, seed, ("uu",)))
    _, RvA, _ = constraints(make2(n, seed, ("uA_ang",)))
    _, _, Ttr = constraints(make2(n, seed, ("uu_ang",)))
    _, _, Utr = constraints(make2(n, seed, ("uu", "uA")))
    ok["K4"] = same(Cvv, Pvv) and all(same(x, y) for x, y in zip(CvA, QvA)) \
        and all(same(x, y) for x, y in zip(CvA, RvA)) and same(Ctr, Ttr) and not same(Ctr, Utr)
    return ok, Mnum, cu, j


def main():
    allok = {}
    for n in (4, 5):
        for seed in (1, 2):
            ok, Mnum, cu, j = run(n, seed)
            guv = sp.Rational(str(j["gi"][U][V].LC))
            print("  n = %d, seed %d: %s; C_vA's matrix on d_v^2 g_uB / g^uv = %s; C_tr's coefficient on d_v^2 g_uu,"
                  " over g^uv^2: %s" % (n, seed, ", ".join("%s %s" % (k, "ok" if v else "FAIL") for k, v in ok.items()),
                                       (Mnum / guv).tolist(), sp.Rational(str(cu.LC)) / guv**2 if cu.is_ground else cu),
                  flush=True)
            for k, v in ok.items():
                allok[k] = allok.get(k, True) and v
    for k, v in allok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(allok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
