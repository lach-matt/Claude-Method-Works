"""vac5.py -- SETTLE-GLAM5 round 4, (V): the limit of the truncations is vacuum.

Setting: Cartesian (t, x1..x4); g_b0 := eta + mu r^-2 k k (k = dt + xhat.dx, mu = 4/5); for any Lorentzian g,
D^rho := g^(ab)(Gamma[g] - Gamma[g_b0])^rho_ab, D_n := g_(n rho) D^rho, E := Ric^H(g; g_b0) = Ric(g) - (1/2)(g_(m rho)
Dh_n D^rho + g_(n rho) Dh_m D^rho) (N1STAR-PROOF.md (0.2)), Ein(X) := X - (1/2) g tr_g X, and
C_mn := (1/2)(g_(m rho) (Gamma[g_b0] - Gamma[g])^rho_(n s) + g_(n rho) (Gamma[g_b0] - Gamma[g])^rho_(m s)) D^s.

  V1 (computed, mpmath 60 digits, central differences) the contracted Bianchi identity in the form the vacuum
     argument uses, for an explicit g = g_b0 + h that solves nothing (h of size 0.3):
        (1/2)(box_g D_n + Ric(g)_n^d D_d) + nabla^m Ein(C)_mn + nabla^m Ein(E)_mn = 0,
     all five components, three points. So where E = 0 (every truncated solution g_T), D solves a homogeneous linear
     wave system whose principal part is (1/2) g^(ab) d_a d_b, whose first-order coefficients are built from
     Gamma[g] - Gamma[g_b0] and Gamma[g], and whose zero-order coefficients from d Gamma[g], d Gamma[g_b0] and Ric(g).
     Controls (the identity mutated): without the Ric(g) D term, and without the C term, it fails.
  V2 (exact) the D-energy at weight a_D on W, along the truncations of (b2): with |Gamma[g] - Gamma[g_b0]| <=
     C(lam + mu) r^-3 + C eps r^(-3/2-a) and the zero-order coefficients <= C(lam + mu) r^-4 + C eps r^(-3/2-a)
     (a in (5/2, 3) the weight of the bootstrap), the time kernels are (1 + |sigma|)^-q with q = 3, 3/2 + a
     (first order), 3, a + 1/2 (zero order through the four-dimensional Hardy inequality): all integrable, for every
     a_D > 0. The cap: D(g_b0 + Sigma) = O(lam r^-3), d D = O(lam r^-4) beyond the band (Sigma = O(lam r^-2), its
     derivatives gain r^-1), whose D-energy on the truncation slice is ~ |T|^(2 a_D - 4) -> 0 exactly for a_D < 2; on
     the band D = O(r^(-9/2)) with its derivative (there g_T = g_lam + chi (g_b0 + Sigma - g_lam), D(g_lam) = 0 and
     g_b0 + Sigma - g_lam = O(r^(-9/2)) with derivatives), D-energy ~ |T|^(2 a_D - 6); on N, D = 0. So for a_D in
     (0, 2) the D-energy of g_T on W_T is at most C |T|^(2 a_D - 4) -> 0, uniformly in sigma. Controls: a_D = 2 (the
     cap does not vanish); the zero-order kernel with a = 1/2 (not integrable).
Round 5 (SETTLE-GLAM5 R5.0, the round-4 verifier's reading): checks marked [arithmetic] (V2a-V2e) integrate kernels
and caps whose exponents are entered by hand; the exponents of the coefficients are measured on the operator in
r5op5.py O1, the caps' and tails' on explicit fields in r5settle5.py G.
Labels: computed (V1 numerical at 60 digits; V2 exact, sympy).

    python3 checks/vac5.py
"""
import sys

import mpmath as mp
import sympy as sp

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


t, x1, x2, x3, x4 = XS = sp.symbols("t x1 x2 x3 x4", real=True)
RR = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
MU = sp.Rational(4, 5)
R5 = range(5)


def gb0():
    k = [sp.Integer(1), x1/RR, x2/RR, x3/RR, x4/RR]
    return sp.diag(-1, 1, 1, 1, 1) + MU/RR**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j])


def h_explicit():
    q = ((t - sp.Rational(3, 10))**2 + (x1 - 1)**2 + (x2 + sp.Rational(1, 2))**2 + x3**2
         + (x4 - sp.Rational(7, 10))**2)/8
    cvals = [[3, -2, 1, 4, -1], [-2, 5, 2, -3, 1], [1, 2, -4, 1, 3], [4, -3, 1, 2, -2], [-1, 1, 3, -2, 6]]
    return sp.Matrix(5, 5, lambda i, j: sp.Rational(cvals[i][j], 20)*sp.exp(-q)*(1 + x1*t/5))


class Field:
    def __init__(self, G):
        self.f = {}
        for i in R5:
            for j in range(i, 5):
                e = G[i, j]
                self.f[(i, j)] = sp.lambdify([XS], e, "mpmath")
                for a in R5:
                    ea = sp.diff(e, XS[a])
                    self.f[(i, j, a)] = sp.lambdify([XS], ea, "mpmath")
                    for b in range(a, 5):
                        self.f[(i, j, a, b)] = sp.lambdify([XS], sp.diff(ea, XS[b]), "mpmath")

    def jets(self, X):
        g = mp.matrix(5, 5)
        dg = [[[mp.mpf(0)]*5 for _ in R5] for _ in R5]
        ddg = [[[[mp.mpf(0)]*5 for _ in R5] for _ in R5] for _ in R5]
        for i in R5:
            for j in range(i, 5):
                g[i, j] = g[j, i] = self.f[(i, j)](X)
                for a in R5:
                    dg[a][i][j] = dg[a][j][i] = self.f[(i, j, a)](X)
                    for b in range(a, 5):
                        v = self.f[(i, j, a, b)](X)
                        ddg[a][b][i][j] = ddg[a][b][j][i] = ddg[b][a][i][j] = ddg[b][a][j][i] = v
        return g, dg, ddg


def christoffel(g, dg, ddg):
    gi = g**-1
    dgi = [[[-sum(gi[r, al]*dg[c][al][be]*gi[be, s] for al in R5 for be in R5) for s in R5] for r in R5]
           for c in R5]
    low = [[[(dg[a][s][b] + dg[b][s][a] - dg[s][a][b])/2 for b in R5] for a in R5] for s in R5]
    Gam = [[[sum(gi[r, s]*low[s][a][b] for s in R5) for b in R5] for a in R5] for r in R5]
    dlow = [[[[(ddg[c][a][s][b] + ddg[c][b][s][a] - ddg[c][s][a][b])/2 for b in R5] for a in R5] for s in R5]
            for c in R5]
    dGam = [[[[sum(dgi[c][r][s]*low[s][a][b] + gi[r, s]*dlow[c][s][a][b] for s in R5) for b in R5]
              for a in R5] for r in R5] for c in R5]
    return gi, dgi, Gam, dGam


class Geo:
    """the quantities of V1 at a point X, as functions of X (for central differences)"""

    def __init__(self):
        G0 = gb0()
        self.Fg = Field(G0 + h_explicit())
        self.F0 = Field(G0)

    def base(self, X):
        J, J0 = self.Fg.jets(X), self.F0.jets(X)
        g = J[0]
        gi, dgi, G, dG = christoffel(*J)
        _, _, G0, dG0 = christoffel(*J0)
        return g, gi, dgi, G, dG, G0, dG0

    def Dup(self, X):
        g, gi, dgi, G, dG, G0, dG0 = self.base(X)
        return [sum(gi[a, b]*(G[r][a][b] - G0[r][a][b]) for a in R5 for b in R5) for r in R5]

    def Dlow(self, X):
        g = self.Fg.jets(X)[0]
        Du = self.Dup(X)
        return [sum(g[n, r]*Du[r] for r in R5) for n in R5]

    def ric(self, X):
        g, gi, dgi, G, dG, G0, dG0 = self.base(X)
        Ric = mp.matrix(5, 5)
        for a in R5:
            for b in R5:
                Ric[a, b] = (sum(dG[r][r][a][b] for r in R5) - sum(dG[b][r][a][r] for r in R5)
                             + sum(G[r][r][l]*G[l][a][b] for r in R5 for l in R5)
                             - sum(G[r][b][l]*G[l][a][r] for r in R5 for l in R5))
        return Ric

    def E(self, X):
        g, gi, dgi, G, dG, G0, dG0 = self.base(X)
        Ric = self.ric(X)
        dGam = [[[G[r][a][b] - G0[r][a][b] for b in R5] for a in R5] for r in R5]
        Dv = [sum(gi[a, b]*dGam[r][a][b] for a in R5 for b in R5) for r in R5]
        dD = [[sum(dgi[c][a][b]*dGam[r][a][b] + gi[a, b]*(dG[c][r][a][b] - dG0[c][r][a][b]) for a in R5 for b in R5)
               for r in R5] for c in R5]
        nab = [[dD[n][r] + sum(G0[r][n][l]*Dv[l] for l in R5) for r in R5] for n in R5]
        out = mp.matrix(5, 5)
        for m_ in R5:
            for n in R5:
                out[m_, n] = Ric[m_, n] - (sum(g[m_, r]*nab[n][r] for r in R5)
                                           + sum(g[n, r]*nab[m_][r] for r in R5))/2
        return out

    def C(self, X):
        g, gi, dgi, G, dG, G0, dG0 = self.base(X)
        Dv = [sum(gi[a, b]*(G[r][a][b] - G0[r][a][b]) for a in R5 for b in R5) for r in R5]
        out = mp.matrix(5, 5)
        for m_ in R5:
            for n in R5:
                out[m_, n] = (sum(g[m_, r]*(G0[r][n][s] - G[r][n][s])*Dv[s] for r in R5 for s in R5)
                              + sum(g[n, r]*(G0[r][m_][s] - G[r][m_][s])*Dv[s] for r in R5 for s in R5))/2
        return out

    def ein(self, X, which):
        Xm = self.E(X) if which == "E" else self.C(X)
        g = self.Fg.jets(X)[0]
        gi = g**-1
        tr = sum(gi[a, b]*Xm[a, b] for a in R5 for b in R5)
        return Xm - g*tr/2


def shift(X, a, s):
    Y = list(X)
    Y[a] = Y[a] + s
    return Y


def d1(f, X, a, h):
    """central first difference of a vector/matrix-valued f in direction a (fourth order)"""
    fp, fm = f(shift(X, a, h)), f(shift(X, a, -h))
    fp2, fm2 = f(shift(X, a, 2*h)), f(shift(X, a, -2*h))
    if isinstance(fp, list):
        return [(8*(fp[i] - fm[i]) - (fp2[i] - fm2[i]))/(12*h) for i in range(len(fp))]
    return (8*(fp - fm) - (fp2 - fm2))/(12*h)


PTS = [[mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("-0.6"), mp.mpf("0.9"), mp.mpf("1.1")],
       [mp.mpf("-0.8"), mp.mpf("0.7"), mp.mpf("1.4"), mp.mpf("-0.5"), mp.mpf("0.6")],
       [mp.mpf("1.2"), mp.mpf("-1.1"), mp.mpf("0.3"), mp.mpf("1.6"), mp.mpf("-0.4")]]


def v1():
    print("V1  the contracted Bianchi identity of the gauge-fixed operator (60 digits)")
    mp.mp.dps = 60
    geo = Geo()
    h = mp.mpf(10)**-10
    worst, size, ctl_ric, ctl_C = mp.mpf(0), mp.mpf(0), mp.mpf(10)**9, mp.mpf(10)**9
    for X in PTS:
        g, gi, dgi, G, dG, G0, dG0 = geo.base(X)
        Dl = geo.Dlow(X)
        dDl = [d1(geo.Dlow, X, a, h) for a in R5]                                  # dDl[a][n] = d_a D_n
        ddDl = [[d1(lambda Y: d1(geo.Dlow, Y, b, h), X, a, h) for b in R5] for a in R5]   # d_a d_b D_n
        # nabla_b D_n and d_a (nabla_b D_n)
        nD = [[dDl[b][n] - sum(G[c][b][n]*Dl[c] for c in R5) for n in R5] for b in R5]
        dnD = [[[ddDl[a][b][n] - sum(dG[a][c][b][n]*Dl[c] + G[c][b][n]*dDl[a][c] for c in R5) for n in R5]
                for b in R5] for a in R5]
        box = [sum(gi[a, b]*(dnD[a][b][n] - sum(G[c][a][b]*nD[c][n] for c in R5)
                             - sum(G[c][a][n]*nD[b][c] for c in R5)) for a in R5 for b in R5) for n in R5]
        Ric = geo.ric(X)
        RicD = [sum(Ric[n, m]*gi[m, d]*Dl[d] for m in R5 for d in R5) for n in R5]

        def divsym(which):
            Xm = geo.ein(X, which)
            dX = [d1(lambda Y: geo.ein(Y, which), X, a, h) for a in R5]
            return [sum(gi[m, a]*(dX[a][m, n] - sum(G[c][a][m]*Xm[c, n] for c in R5)
                                  - sum(G[c][a][n]*Xm[m, c] for c in R5)) for m in R5 for a in R5) for n in R5]
        dE = divsym("E")
        dC = divsym("C")
        lhs = [(box[n] + RicD[n])/2 + dC[n] + dE[n] for n in R5]
        worst = max(worst, max(abs(c) for c in lhs))
        size = max(size, max(abs(c) for c in box), max(abs(c) for c in dE))
        ctl_ric = min(ctl_ric, max(abs(box[n]/2 + dC[n] + dE[n]) for n in R5))
        ctl_C = min(ctl_C, max(abs((box[n] + RicD[n])/2 + dE[n]) for n in R5))
    check("V1a (1/2)(box_g D_n + Ric_n^d D_d) + nabla^m Ein(C)_mn + nabla^m Ein(E)_mn = 0, five components, three "
          "points (h of size 0.3, no equation solved)", worst < mp.mpf(10)**-25,
          "max |defect| " + mp.nstr(worst, 3) + " against terms up to " + mp.nstr(size, 3))
    check("V1b control: without the Ric(g) D term the identity fails at every point", ctl_ric > mp.mpf(10)**-6,
          "min defect " + mp.nstr(ctl_ric, 3))
    check("V1c control: without the C term (Gamma[g] - Gamma[g_b0]) D it fails at every point", ctl_C > mp.mpf(10)**-6,
          "min defect " + mp.nstr(ctl_C, 3))


def v2():
    print("V2  the D-energy on W along the truncations (exact)")
    a, aD, sg = sp.symbols("a a_D sigma", positive=True)

    def integrable(q):
        return sp.integrate(sg**(-q), (sg, 1, sp.oo)).is_finite

    av = sp.Rational(11, 4)
    kernels = {"first order, (lam + mu) r^-3": 3, "first order, eps r^(-3/2-a)": sp.Rational(3, 2) + av,
               "zero order with Hardy, (lam + mu) r^-4 * r": 3, "zero order with Hardy, eps r^(-3/2-a) * r":
               av + sp.Rational(1, 2), "deformation d_t g: eps r^(-3/2-a) and lam r^-3": sp.Rational(3, 2) + av}
    ok = all(integrable(q) for q in kernels.values())
    check("V2a [arithmetic] every kernel of the D-system's energy at weight a_D is integrable along W (a = 11/4; the "
          "exponents "
          "do not involve a_D)", ok, str({k: str(v) for k, v in kernels.items()}))
    r, T = sp.symbols("r T", positive=True)
    cap = sp.integrate(r**(2*aD)*(r**-4)**2*r**3, (r, T, sp.oo), conds="none")
    capv = [sp.limit(cap.subs(aD, av_), T, sp.oo) for av_ in (sp.Rational(1, 2), 1, sp.Rational(19, 10))]
    check("V2b [arithmetic] the cap beyond the band: int_(|T|)^oo r^(2 a_D) (r^-4)^2 r^3 dr = |T|^(2 a_D - 4)/(4 - 2 "
          "a_D) -> 0 for "
          "a_D = 1/2, 1, 19/10", sp.simplify(cap - T**(2*aD - 4)/(4 - 2*aD)) == 0 and all(c == 0 for c in capv),
          str(sp.simplify(cap)))
    band = sp.integrate(r**(2*aD)*(r**sp.Rational(-9, 2))**2*r**3, (r, T, T + 1))
    check("V2c [arithmetic] the band (unit width at r ~ |T|): D-energy ~ |T|^(2 a_D - 6) -> 0 for a_D < 3 (a_D = 1)",
          sp.limit(band.subs(aD, 1), T, sp.oo) == 0)
    capc = sp.integrate(r**(2*2)*(r**-4)**2*r**3, (r, T, sp.oo), conds="none")
    check("V2d [arithmetic] control: at a_D = 2 the cap's D-energy does not tend to 0 (it is "
          "infinite)", capc in (sp.oo, sp.zoo)
          or not capc.is_finite, str(capc))
    check("V2e [arithmetic] control: the zero-order kernel with Hardy at a = 1/2 (q = a + 1/2 = 1) is not integrable",
          not integrable(sp.Rational(1, 2) + sp.Rational(1, 2)))


def main():
    v2()
    v1()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
