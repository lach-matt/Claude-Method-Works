#!/usr/bin/env python3
"""charcons5: the gauge-reduced null constraints of D440 as ODEs along the generators (FAMILIES5 4e, D448).

charprop5 (D440) showed that on N = {u = 0} the reduced operator's components E_vv, E_vA and gamma^(AB) E_AB are
C_vv, C_vA, C_tr plus transports of W, with C_vv, C_vA, C_tr free of the transverse jets: the null constraints in the
gauge W = 0. It left open whether they can be solved. Here they are computed modulo every W-jet at p (so E = C there),
with the first and second v-derivatives of g_uu, g_uv, g_uA and the second of g_AB along N made symbolic, and their
dependence on those derivatives is read off (exact, in Q[T, tangential symbols]; the other jets random rationals):

  K1  C_vv contains no second v-derivative of g_uu, g_uv, g_uA, and of g_AB only the trace: the coefficient of
      d_v^2 g_AB is -(1/2) gamma^(AB). With the conformal class of gamma along N and g_uv given it is a second-order
      ODE for the conformal factor (Raychaudhuri).
  K2  C_vA contains no second v-derivative of g_uu, and its coefficients on d_v^2 g_uB are g^(uv) delta_A^B: with the
      conformal factor known, a second-order ODE system for g_uA.
  K3  C_tr contains d_v^2 g_uu with the coefficient -2 (g^(uv))^2 (and d_v^2 of g_uv, g_uA, g_AB, and first
      derivatives); C_vv and C_vA contain no d_v^2 g_uu: with the conformal factor and g_uA known, a second-order ODE
      for g_uu.

So given the conformal class of gamma and g_uv on N (free data and a gauge choice) and H, and the values at S of the
conformal factor, g_uA, g_uu and their first v-derivatives, the gauge-reduced constraints are solved along each
generator by ODEs in turn: the conformal factor's (Raychaudhuri's) is nonlinear and holds while theta stays finite, the
other two are linear in their unknown's second derivative (local existence for each; not computed beyond that). The
corner conditions (W = 0 at S, which fixes d_u g_vv, d_u g_vA and the trace of d_u g_AB there, D440's N1) are a
condition on the data at S from both N and N'; they are not computed here.

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


def make2(n, seed):
    """charprop5.make with the v-jets of g_u* (first and second) and of g_AB (second) along N symbolic"""
    r = random.Random(seed)

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
                d1[a, b, e] = c(rnd())
        for e in range(n):
            for f in range(e, n):
                if e == U:
                    d2[a, b, e, f] = sym["g%d%d_u%d" % (a, b, f)]
                elif zero_on_n(a, b):
                    d2[a, b, e, f] = R(0)
                elif e == V and f == V and (a, b) in tang2:
                    d2[a, b, e, f] = sym["t2_%d%d" % (a, b)]
                else:
                    d2[a, b, e, f] = c(rnd())
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


def run(n, seed):
    j = make2(n, seed)
    R, sym = j["R"], j["sym"]
    geo = CP.geometry(j)
    W, dW, E = geo["W"], geo["dW"], geo["E"]
    S = list(range(2, n))
    piv = [sym["g%d%d_u" % (V, V)], sym["g%d%d_u%d" % (V, V, V)]] + [sym["g%d%d_u%d" % (V, V, A)] for A in S]
    forms = [W[V], dW[V][V]] + [dW[A][V] for A in S]
    piv += [sym["g%d%d_u" % (V, A)] for A in S] + [sym["g%d%d_u%d" % (V, A, V)] for A in S] \
        + [sym["g%d%d_u%d" % (V, A, C)] for A in S for C in S]
    forms += [W[A] for A in S] + [dW[V][A] for A in S] + [dW[C][A] for A in S for C in S]
    piv += [sym["g22_u"], sym["g22_u%d" % V]] + [sym["g22_u%d" % C] for C in S]
    forms += [W[U], dW[V][U]] + [dW[C][U] for C in S]
    trE = sum((j["gamI"][A - 2][B - 2] * E[A][B] for A in S for B in S), R(0))
    red = reduce_lin([E[V][V]] + [E[V][A] for A in S] + [trE], forms, piv)
    Cvv, CvA, Ctr = red[0], red[1:-1], red[-1]
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
