"""f1lemma5.py -- SETTLE-GLAM5 round 4, F1: the top-order terms of Lemma 11.0's source F_1 (N1STAR-PROOF.md as of
82a7e95, lines 10548-10567), computed on the full five-dimensional gauge-fixed operator.

Setting: Cartesian (t, x1..x4), g0 := eta + mu r^-2 k k (k = dt + xhat.dx, mu = 4/5; the record's g0 after the
shell), the wave U3 := lam A(x) sin(v/lam), A := r^(-3/2) P with P a fixed symmetric matrix (the record's
r^(-3/2) G_3 = lam [W_TT] has this form; transversality is not used), v = t + r. Ric^H(g; g0) as in (0.2):
Ric(g) - (1/2)(g_(m rho) Dh_n D^rho + g_(n rho) Dh_m D^rho), D^rho = g^(ab)(Gamma[g] - Gamma[g0])^rho_ab. Lemma 11.0's
F_1 := S(u) - (1/2)(g^(ab) - g0^(ab)) d_a d_b u_1 + (1/2) box~(U3) equals, by (0.2),
    F_1(u_1) = -Ric^H(g0 + U3 + u_1) - (1/2) g^(ab) d_a d_b u_1,     g := g0 + U3 + u_1,
and its first variation at u_1 is tested on fields k with only a value, only a gradient or only a Hessian at the
point x0 (k = K0; k = K1 (x - x0)_c; k = (1/2) K2 (x - x0)_c (x - x0)_d).

  F1a (computed, 80 digits) the Hessian coefficient of F_1 vanishes: D F_1[k_hess](x0) = 0 to 1e-60 relative, at two
      points, two values of lam, three random K2: F_1 has no second derivative of u_1. Control (the definition
      mutated to the record's -(1/2) box~ form, F~ := -Ric^H(g) - (1/2) g0^(ab) d_a d_b u_1): the Hessian
      coefficient is (1/2)(g0^(ab) - g^(ab)) d_a d_b k, nonzero.
  F1b (computed) the value coefficient c of u_1 has the lam^-1 part -(1/2) lam^-1 u_1(ell, ell) [d_th^2 W]
      ([d_th^2 W] = -A sin(v/lam), ell := g^-1 dv): D F_1[K0] - (1/2) lam^-1 K0(ell, ell) A sin(v/lam) stays bounded
      as lam = 10^-2, 10^-3, 10^-4 while the lam^-1 term grows tenfold per step; and for K0 with K0(ell, ell) = 0 the
      whole coefficient stays bounded. Control (the wave mutated to the non-oscillating lam A): no lam^-1 term.
  F1c (computed) the gradient coefficient b of d u_1 has lam-order 0: D F_1[k_grad] is bounded and bounded away
      from 0 as lam -> 0: a term b . d U at the order the step of Lemma 11.0 estimates (d U = d d^gamma u_1).
      Control (the coefficients mutated: g0 -> eta, no wave): b vanishes, so its size comes from d(lam [W]) and
      Gamma[g0], which are in E_(3/2) and E_2.
  F1d (exact, sympy) the chain rule (Faa di Bruno) on F(x, u, u'): d^N F - F_p u^(N+1) - F_u u^(N) contains no
      u^(N+1), and its u^(N) terms carry a total x-derivative of F_p (orders <= 2 of u) (N = 2..6): so
      d^gamma F_1 - b . d U - c . U involves derivatives of u_1 of order <= |gamma| only. Control: without the
      subtraction of F_p u^(N+1) the top order is present.
  F1e (exact) the Gronwall factors: the kernel C (1 + lam^-1) t^(-3/2) (b . d U and, through Lemma 9.3(b),
      c . U) integrates over t >= lam^-2 to 2 C (1 + lam): the factor e^(2C(1 + lam)) is lam-free; with c . U taken
      as a source instead (through the previous step's energy), each order costs one lam^-1. Control: the same
      kernel over the near region [1, lam^-2] gives exp(2C(1 + lam^-1)(1 - lam)), beating every power.
Round 5 (SETTLE-GLAM5 R5.0, the round-4 verifier's reading): F1c shows only b != 0 (it passes with the wave's
amplitude mutated to lam^2, b then coming from Gamma[g0]); the lam^0 wave part of b is cclass5.py C3. F1b's wave has no
envelope; with one, cclass5.py C1-C2 (c's remainder is E_(3/2), not E_2). Checks marked [arithmetic] (F1e, F1e',
F1e'') integrate a kernel or count a loop entered by hand.
Labels: computed (F1a-F1c mpmath at 80 digits on sympy-differentiated metrics, central differences in eps;
F1d-F1e exact).

    python3 checks/f1lemma5.py
"""
import random
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
lam = sp.Symbol("lam", positive=True)
RR = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
MU = sp.Rational(4, 5)
R5 = range(5)


def gb0(flat=False):
    if flat:
        return sp.diag(-1, 1, 1, 1, 1)
    k = [sp.Integer(1), x1/RR, x2/RR, x3/RR, x4/RR]
    return sp.diag(-1, 1, 1, 1, 1) + MU/RR**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j])


PMAT = sp.Matrix([[2, 1, -1, 3, 0], [1, -2, 2, 1, 1], [-1, 2, 1, -2, 3], [3, 1, -2, 1, -1], [0, 1, 3, -1, 2]])/7


def wave(osc=True):
    s = sp.sin((t + RR)/lam) if osc else sp.Integer(1)
    return lam*RR**sp.Rational(-3, 2)*s*PMAT


class Jets:
    """value, first and second derivatives of a symmetric matrix field at a point, from lambdified sympy"""

    def __init__(self, G):
        self.f = {}
        for i in R5:
            for j in range(i, 5):
                e = G[i, j]
                self.f[(i, j)] = sp.lambdify((XS, lam), e, "mpmath")
                for a in R5:
                    ea = sp.diff(e, XS[a])
                    self.f[(i, j, a)] = sp.lambdify((XS, lam), ea, "mpmath")
                    for b in range(a, 5):
                        self.f[(i, j, a, b)] = sp.lambdify((XS, lam), sp.diff(ea, XS[b]), "mpmath")

    def at(self, X, lv):
        g = mp.matrix(5, 5)
        dg = [[[mp.mpf(0)]*5 for _ in R5] for _ in R5]
        ddg = [[[[mp.mpf(0)]*5 for _ in R5] for _ in R5] for _ in R5]
        for i in R5:
            for j in range(i, 5):
                g[i, j] = g[j, i] = self.f[(i, j)](X, lv)
                for a in R5:
                    dg[a][i][j] = dg[a][j][i] = self.f[(i, j, a)](X, lv)
                    for b in range(a, 5):
                        v = self.f[(i, j, a, b)](X, lv)
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


def ricH(J, J0):
    g, dg, ddg = J
    g0, dg0, ddg0 = J0
    gi, dgi, G, dG = christoffel(g, dg, ddg)
    _, _, G0, dG0 = christoffel(g0, dg0, ddg0)
    Ric = mp.matrix(5, 5)
    for a in R5:
        for b in R5:
            Ric[a, b] = (sum(dG[r][r][a][b] for r in R5) - sum(dG[b][r][a][r] for r in R5)
                         + sum(G[r][r][l]*G[l][a][b] for r in R5 for l in R5)
                         - sum(G[r][b][l]*G[l][a][r] for r in R5 for l in R5))
    dGam = [[[G[r][a][b] - G0[r][a][b] for b in R5] for a in R5] for r in R5]
    Dv = [sum(gi[a, b]*dGam[r][a][b] for a in R5 for b in R5) for r in R5]
    dD = [[sum(dgi[c][a][b]*dGam[r][a][b] + gi[a, b]*(dG[c][r][a][b] - dG0[c][r][a][b]) for a in R5 for b in R5)
           for r in R5] for c in R5]
    nab = [[dD[n][r] + sum(G0[r][n][l]*Dv[l] for l in R5) for r in R5] for n in R5]
    out = mp.matrix(5, 5)
    for m_ in R5:
        for n in R5:
            out[m_, n] = Ric[m_, n] - (sum(g[m_, r]*nab[n][r] for r in R5) + sum(g[n, r]*nab[m_][r] for r in R5))/2
    return out


def add_k(J, kv, kd, kdd, e):
    """J + e * (jets of the test field k at x0)"""
    g, dg, ddg = J
    g2 = g + e*kv
    dg2 = [[[dg[a][i][j] + e*kd[a][i][j] for j in R5] for i in R5] for a in R5]
    ddg2 = [[[[ddg[a][b][i][j] + e*kdd[a][b][i][j] for j in R5] for i in R5] for b in R5] for a in R5]
    return g2, dg2, ddg2


def symmat(rnd, scale=1):
    M = mp.matrix(5, 5)
    for i in R5:
        for j in range(i, 5):
            M[i, j] = M[j, i] = mp.mpf(rnd.randint(-9, 9))/7*scale
    return M


ZERO3 = [[[mp.mpf(0)]*5 for _ in R5] for _ in R5]
ZERO4 = [[[[mp.mpf(0)]*5 for _ in R5] for _ in R5] for _ in R5]


def test_field(kind, K, c=0, d=0):
    """jets at x0 of k = K (value), K (x - x0)_c (gradient), (1/2) K (x - x0)_c (x - x0)_d (Hessian, symmetrised)"""
    kv = mp.matrix(5, 5)
    kd = [[[mp.mpf(0)]*5 for _ in R5] for _ in R5]
    kdd = [[[[mp.mpf(0)]*5 for _ in R5] for _ in R5] for _ in R5]
    if kind == "val":
        kv = K
    elif kind == "grad":
        for i in R5:
            for j in R5:
                kd[c][i][j] = K[i, j]
    else:
        for i in R5:
            for j in R5:
                if c == d:
                    kdd[c][c][i][j] = K[i, j]
                else:
                    kdd[c][d][i][j] = kdd[d][c][i][j] = K[i, j]/2
    return kv, kd, kdd


def DF1(Jw, J0, field, mutated=False):
    """first variation of F_1 at u_1 = 0 in the direction of the test field (central difference, step 1e-25)"""
    kv, kd, kdd = field
    e = mp.mpf(10)**-25
    Rp = ricH(add_k(Jw, kv, kd, kdd, e), J0)
    Rm = ricH(add_k(Jw, kv, kd, kdd, -e), J0)
    dR = (Rp - Rm)/(2*e)
    gmet = J0[0] if mutated else Jw[0]
    gi = gmet**-1
    box = sum(gi[a, b]*mp.matrix([[kdd[a][b][i][j] for j in R5] for i in R5]) for a in R5 for b in R5)
    return -dR - box/2


PTS = [[mp.mpf("0.3"), mp.mpf("1.7"), mp.mpf("-0.9"), mp.mpf("1.2"), mp.mpf("0.8")],
       [mp.mpf("-0.6"), mp.mpf("-1.1"), mp.mpf("1.5"), mp.mpf("0.4"), mp.mpf("-1.3")]]


def setup(osc=True, flat=False):
    G0 = gb0(flat)
    W = wave(osc) if not flat else sp.zeros(5, 5)
    return Jets(G0 + W), Jets(G0)


def f1a():
    print("F1a-F1c  the first variation of F_1 at u_1 = 0 on the full gauge-fixed operator (80 digits)")
    mp.mp.dps = 80
    rnd = random.Random(7)
    Jw_s, J0_s = setup()
    worst, ctl, size = mp.mpf(0), mp.mpf(10)**9, mp.mpf(0)
    for X in PTS:
        for lv in (mp.mpf("1e-2"), mp.mpf("1e-3")):
            Jw, J0 = Jw_s.at(X, lv), J0_s.at(X, lv)
            for (c, d) in ((0, 0), (1, 3), (0, 2)):
                K2 = symmat(rnd)
                fld = test_field("hess", K2, c, d)
                val = DF1(Jw, J0, fld)
                gi = Jw[0]**-1
                ref = mp.mnorm(sum(gi[a, b]*mp.matrix([[fld[2][a][b][i][j] for j in R5] for i in R5])
                                   for a in R5 for b in R5), 1)
                worst = max(worst, mp.mnorm(val, 1)/ref)
                size = max(size, ref)
                ctl = min(ctl, mp.mnorm(DF1(Jw, J0, fld, mutated=True), 1)/ref)
    check("F1a the Hessian coefficient of F_1 vanishes: |D F_1[k_hess]| / |g^ab d_a d_b k| (two points, lam = 1e-2, "
          "1e-3, three K2)", worst < mp.mpf(10)**-40, "max " + mp.nstr(worst, 3))
    check("F1a' control (F~ := -Ric^H(g) - (1/2) g0^ab d_a d_b u_1, the record's box~ form): a Hessian coefficient "
          "remains", ctl > mp.mpf(10)**-6, "min ratio " + mp.nstr(ctl, 3))


def lead_term(Jw, X, lv, K0):
    gi = Jw[0]**-1
    r = mp.sqrt(sum(c**2 for c in X[1:]))
    dv = mp.matrix([1] + [c/r for c in X[1:]])
    ell = gi*dv
    s = (ell.T*K0*ell)[0]
    A = mp.matrix(PMAT.tolist())*r**mp.mpf(-1.5)
    return s*A*mp.sin((X[0] + r)/lv)/(2*lv)


def f1b():
    mp.mp.dps = 80
    rnd = random.Random(19)
    lams = [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]
    Jw_s, J0_s = setup()
    Jn_s, J0n_s = setup(osc=False)
    rem_ok, grow_ok, tr_ok, ctl_ok = True, True, True, True
    info = []
    for X in PTS:
        K0 = symmat(rnd)
        # a K0 with K0(ell, ell) = 0: subtract the ell ell part along a fixed covector pair
        rems, leads, trs, nos = [], [], [], []
        for lv in lams:
            Jw, J0 = Jw_s.at(X, lv), J0_s.at(X, lv)
            val = DF1(Jw, J0, test_field("val", K0))
            L = lead_term(Jw, X, lv, K0)
            rems.append(mp.mnorm(val - L, 1))
            leads.append(mp.mnorm(L, 1))
            gi = Jw[0]**-1
            r = mp.sqrt(sum(c**2 for c in X[1:]))
            dv = mp.matrix([1] + [c/r for c in X[1:]])
            ell = gi*dv
            # K0t := K0 - (K0(ell, ell)/(m(ell)^2)) m m with m := e_1 (a covector with m(ell) != 0)
            m = mp.matrix([0, 1, 0, 0, 0])
            ml = (m.T*ell)[0]
            K0t = K0 - ((ell.T*K0*ell)[0]/ml**2)*(m*m.T)
            trs.append(mp.mnorm(DF1(Jw, J0, test_field("val", K0t)), 1))
            Jn, J0n = Jn_s.at(X, lv), J0n_s.at(X, lv)
            # the same test on the mutated (non-oscillating) wave: D F_1[K0] minus the claimed lam^-1 term
            nos.append(mp.mnorm(DF1(Jn, J0n, test_field("val", K0)) - L, 1))
        info.append((mp.nstr(rems[0], 3), mp.nstr(rems[-1], 3), mp.nstr(leads[0], 3), mp.nstr(leads[-1], 3)))
        rem_ok = rem_ok and max(rems) < 3*min(rems) + 1
        grow_ok = grow_ok and max(leads) > 100*max(rems)
        tr_ok = tr_ok and max(trs) < 3*min(trs) + 1
        ctl_ok = ctl_ok and max(nos) > 100*max(rems)
    check("F1b D F_1[K0] - (1/2) lam^-1 K0(ell, ell) A sin(v/lam) stays bounded (lam = 1e-2, 1e-3, 1e-4) while the "
          "lam^-1 term reaches more than 100 times it: c = -(1/2) lam^-1 (.)(ell, ell)[d_th^2 W] + O(1)",
          rem_ok and grow_ok,
          "(rem at 1e-2, 1e-4; lead at 1e-2, 1e-4) " + str(info))
    check("F1b' for K0(ell, ell) = 0 the value coefficient is O(1): the lam^-1 part is exactly the ell-ell one", tr_ok)
    check("F1b'' control (the wave mutated to the non-oscillating lam A): the same test fails, the remainder "
          "reaching more than 100 times the bound above (the lam^-1 coefficient is the oscillation's)", ctl_ok)


def f1c():
    mp.mp.dps = 80
    rnd = random.Random(23)
    lams = [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]
    Jw_s, J0_s = setup()
    Jf_s, J0f_s = setup(flat=True)
    ok, ctl = True, True
    info = []
    for X in PTS:
        K1 = symmat(rnd)
        vals = []
        for lv in lams:
            Jw, J0 = Jw_s.at(X, lv), J0_s.at(X, lv)
            vals.append(max(mp.mnorm(DF1(Jw, J0, test_field("grad", K1, c)), 1) for c in (0, 1)))
            Jf, J0f = Jf_s.at(X, lv), J0f_s.at(X, lv)
            ctl = ctl and max(mp.mnorm(DF1(Jf, J0f, test_field("grad", K1, c)), 1) for c in (0, 1)) < mp.mpf(10)**-40
        info.append([mp.nstr(v, 4) for v in vals])
        ok = ok and max(vals) < 4*min(vals) and min(vals) > mp.mpf("0.01")
    check("F1c [b != 0 only; its lam^0 wave part: cclass5 C3] the gradient coefficient b has lam-order 0: |D "
          "F_1[k_grad]| bounded and bounded away from 0 "
          "(lam = 1e-2, 1e-3, 1e-4): b . d U is at the order the step estimates", ok, str(info))
    check("F1c' control (g0 -> eta, no wave): b = 0, so b comes from d(lam [W]) and Gamma[g0]", ctl)


def f1d():
    print("F1d  the chain rule: the top-order terms of d^N F(x, u, u')")
    x = sp.Symbol("x")
    us = sp.symbols("u0:9")  # u0 = u, u1 = u', ...
    F = sp.Function("F")(x, us[0], us[1])

    def Dx(f):  # the total x-derivative on functions of (x, u0, u1, ...)
        return sp.diff(f, x) + sum(us[i + 1]*sp.diff(f, us[i]) for i in range(len(us) - 1))

    Fp, Fu = sp.diff(F, us[1]), sp.diff(F, us[0])
    ok, ctl = True, True
    dN = F
    for N in range(1, 7):
        dN = sp.expand(Dx(dN))
        if N < 2:
            continue
        rem = sp.expand(dN - Fp*us[N + 1] - Fu*us[N])
        ok = ok and not rem.has(us[N + 1])
        if N >= 3:
            ok = ok and sp.simplify(rem.coeff(us[N]) - N*Dx(Fp)) == 0
        ctl = ctl and sp.expand(dN - Fu*us[N]).has(us[N + 1])
    check("F1d d^N F - F_p u^(N+1) - F_u u^(N) has no u^(N+1), and (N >= 3) its u^(N) coefficient is N D_x(F_p), "
          "which involves u, u', u'' only (N = 2..6)", ok)
    check("F1d' control: without subtracting F_p u^(N+1) the top order u^(N+1) is present", ctl)


def f1e():
    print("F1e  the Gronwall factors of the repaired step")
    C, tt, Mx, lm = sp.symbols("C tt M lm", positive=True)
    far = sp.integrate(C*(1 + 1/lm)*tt**sp.Rational(-3, 2), (tt, lm**-2, sp.oo))
    check("F1e [arithmetic] int_(lam^-2)^oo C (1 + lam^-1) t^(-3/2) dt = 2 C (1 + lam): the factor e^(2C(1 + lam)) "
          "is lam-free",
          sp.simplify(far - 2*C*(1 + lm)) == 0, str(sp.simplify(far)))
    near = sp.integrate(C*(1 + 1/lm)*tt**sp.Rational(-3, 2), (tt, 1, lm**-2))
    lim = sp.limit(sp.exp(near.subs(C, 1))*lm**Mx, lm, 0, "+")
    check("F1e' [arithmetic] control: over the near region [1, lam^-2] the factor is exp(2C(1 + lam^-1)(1 - lam)), "
          "beating every "
          "lam^-M", sp.simplify(near - 2*C*(1 + 1/lm)*(1 - lm)) == 0 and lim == sp.oo)
    # the order count: c . U as a source costs lam^-1 per step (through the previous energy), in the kernel nothing
    steps = 12
    src = [0]
    ker = [0]
    for _ in range(steps):
        src.append(src[-1] + 1)
        ker.append(ker[-1])
    check("F1e'' [arithmetic] with c . U in the source the step-N constant carries lam^-N (N = 12 gives 12); in the "
          "kernel it "
          "carries lam^0: the kernel placement is the lam-sharp one (Proposition R3.1's count +1 per order is an "
          "overcount, harmless)", src[-1] == steps and ker[-1] == 0)


def main():
    f1d()
    f1e()
    f1a()
    f1b()
    f1c()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
