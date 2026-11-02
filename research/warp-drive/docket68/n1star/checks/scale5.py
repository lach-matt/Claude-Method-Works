"""scale5.py -- SETTLE-GLAM5 round 3, (b2): the Z-commuted nonlinear equation on the wedge W and the identities its
weighted estimate uses.

Setting: Cartesian (t, x1..x4); g_b0(mu) := eta + mu r^-2 k k, k = dt + xhat.dx (5D Tangherlini, Kerr-Schild,
det = -1); the record's gauge-fixed operator relative to g_b0 (N1STAR-PROOF.md (0.2)),
    P_mu(h) := Ric^H(g_b0(mu) + h; g_b0(mu)) = Ric(g) - (1/2)(g_(m rho) Dh_n D^rho + g_(n rho) Dh_m D^rho),
    D^rho := g^(ab) (Gamma[g]^rho_ab - Gamma[g_b0]^rho_ab),  Dh the covariant derivative of g_b0,
in Cartesian components; Z := (t - v1) d_t + x.d_x, acting on components (the dilation about N's vertex).

  Z1 (computed, mpmath 40 digits) the exact scaling identity, for an explicit h that is not small:
        (Z + 2) P_mu(h) = DP_mu(h)[Z h] - 2 mu d_mu P_mu(h),
     at three points (all 15 components), with DP by d/d eps, Z P by d/ds along the dilation, d_mu by d/d mu.
     It follows from Ric^H(s^2 G; s^2 G0) = Ric^H(G; G0), naturality, and D_s^* g_b0(mu) = s^2 g_b0(mu s^-2)
     (Z1d, exact); for a solution P_mu(h) = 0 it says that Z h solves the linearised equation at h with source
     2 mu d_mu P_mu(h), the mu-derivative at fixed h, whose coefficients carry mu r^-2. Controls: without the
     mu d_mu term, and with the non-uniform dilation (t - v1) d_t + 2 x.d_x, the identity fails.
  Z2 (computed) the other commutators: d_t P(h) = DP(h)[d_t h] (static) and L_Omega P(h) = DP(h)[L_Omega h] for the
     rotation Omega = x1 d_2 - x2 d_1 with its index terms. Controls: the rotation without its index terms, and the
     translation d_1 (not an isometry), fail.
  Z3 (exact) the scalar case: for box_g of g_b0, (Z + 2) box_g phi - box_g(Z phi) = -2 mu d_mu(box_g) phi
     = 2 mu r^-3 d_r(r d_r) phi on phi(v, r) Y_l, round 2's Z2c read as Z1's identity.
  Z4 (exact) the Hessian from the commuted fields: d_i = r^-1 xhat_i (Z - (t - v1) d_t) - r^-2 x_j Omega_ij on
     every function, so every second derivative of h is a combination of first derivatives of h, Z h, d_t h and
     Omega_ij h with coefficients bounded by 1 + 4/r on W, where |t - v1| <= r (W lies in {v >= v1, t <= v1}).
     Control: with |t - v1| > r (outside W) the coefficient of d d_t h is unbounded along t -> -oo at fixed r.
  Z5 (exact; an explicit h(t, r), f generic) on S = {t = f(r)}: r d/dr (h|_S) = (Z h)|_S + (v1 - f + r f')
     (d_t h)|_S, so the b-derivative rho d_rho = -r d/dr of the data on S is a combination of the restrictions
     of Z h and d_t h with a coefficient smooth in rho (f' in |x|^-2 C^oo, Part VII 162-177). Control:
     (r d_r h)|_S is not r d/dr (h|_S).
  Z6 (exact) on N = {v = v1}: Z(v - v1) = v - v1, so Z is tangent to N, Z = r (d_r - d_t) there, and Z^j of a
     datum r^-q F(xhat) + (ell-gaining remainder) keeps the order r^-q (Z(r^-q F) = -q r^-q F). Control: d_t is
     transverse to N (d_t v = 1).
  Z7 (exact) the kernel table of the Z-commuted energy at weight a for the remainder h_R := h - Sigma
     (Sigma = sum_(p in {2,5/2,3,7/2,4}) r^-p F_p(s)), with |d Gamma^alpha h_R| <= eps r^(-3/2-a) (S1 of round 2):
     every error term's time kernel along W (r >= v1 - t) is integrable at a in (5/2, 3): mu d_mu P (r^-3), the
     quasilinear (Z H) d d h (r^-3 from Sigma, r^(-1/2-a) from h_R), Q's terms (r^-3, r^(-3/2-a)), Sigma's residual
     P(Sigma) = O(r^-6) (L^2 kernel (v1 - t)^(a-4), integrable exactly for a < 3). Controls: the residual kernel at
     a = 3 diverges; the quasilinear h_R-kernel at a = 1/2 diverges.
  Z8 (exact) the class on S: the S-flux at weight a, int_S r^(2a) |d phi|^2 r^3, with the Hardy inequality puts
     phi|_S in rho^(a+1) L^2_b(drho/rho) and d phi|_S in rho^(a+2) L^2_b: for phi = rho^beta exactly when
     beta > a + 1; so a in (l0 - 1, 3) puts h_R|_S in rho^(l0) H_b and d h_R|_S in rho^(l0+1) H_b for every
     l0 in (3, 4). Sigma|_S has the exponents p + j, p in {2, 5/2, 3, 7/2, 4}, all in E_0^(1/2). Control: a
     pointwise reading O(rho^(1/2+a)) gives only a > l0 - 1/2 (round 2's R2.8), which fails at l0 = 3.8, a = 2.9.
Labels: computed (Z1-Z2 mpmath at 40 digits on sympy-differentiated metrics; Z3-Z8 exact, sympy).

    python3 checks/scale5.py
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
mu, eps = sp.symbols("mu epsilon", real=True)
V1 = sp.Rational(7, 10)
RR = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)


def gb0(m):
    k = [sp.Integer(1), x1/RR, x2/RR, x3/RR, x4/RR]
    eta = sp.diag(-1, 1, 1, 1, 1)
    return eta + m/RR**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j])


def h_explicit():
    q = ((t - sp.Rational(3, 10))**2 + (x1 - 1)**2 + (x2 + sp.Rational(1, 2))**2 + x3**2
         + (x4 - sp.Rational(7, 10))**2)/8
    cvals = [[3, -2, 1, 4, -1], [-2, 5, 2, -3, 1], [1, 2, -4, 1, 3], [4, -3, 1, 2, -2], [-1, 1, 3, -2, 6]]
    return sp.Matrix(5, 5, lambda i, j: sp.Rational(cvals[i][j], 20)*sp.exp(-q)*(1 + x1*t/5))


class Op:
    """P(h) = Ric^H(g0 + h; g0) at a point, from lambdified derivatives of g = g0 + h + eps k and of g0."""

    def __init__(self, g0sym, hsym, ksym):
        gs = g0sym + hsym + eps*ksym
        self.f = {}
        for name, G in (("g", gs), ("g0", g0sym)):
            comp = {}
            for i in range(5):
                for j in range(i, 5):
                    e = G[i, j]
                    comp[(i, j)] = sp.lambdify((XS, mu, eps), e, "mpmath")
                    for a in range(5):
                        ea = sp.diff(e, XS[a])
                        comp[(i, j, a)] = sp.lambdify((XS, mu, eps), ea, "mpmath")
                        for b in range(a, 5):
                            comp[(i, j, a, b)] = sp.lambdify((XS, mu, eps), sp.diff(ea, XS[b]), "mpmath")
            self.f[name] = comp

    def jets(self, name, X, m, e):
        c = self.f[name]
        g = mp.matrix(5, 5)
        dg = [[[0]*5 for _ in range(5)] for _ in range(5)]  # dg[a][i][j]
        ddg = [[[[0]*5 for _ in range(5)] for _ in range(5)] for _ in range(5)]  # ddg[a][b][i][j]
        for i in range(5):
            for j in range(i, 5):
                g[i, j] = g[j, i] = c[(i, j)](X, m, e)
                for a in range(5):
                    dg[a][i][j] = dg[a][j][i] = c[(i, j, a)](X, m, e)
                    for b in range(a, 5):
                        v = c[(i, j, a, b)](X, m, e)
                        ddg[a][b][i][j] = ddg[a][b][j][i] = ddg[b][a][i][j] = ddg[b][a][j][i] = v
        return g, dg, ddg

    @staticmethod
    def christoffel(g, dg, ddg):
        gi = g**-1
        R5 = range(5)
        dgi = [[[-sum(gi[r, al]*dg[c][al][be]*gi[be, s] for al in R5 for be in R5) for s in R5] for r in R5]
               for c in R5]  # dgi[c][r][s]
        low = [[[(dg[a][s][b] + dg[b][s][a] - dg[s][a][b])/2 for b in R5] for a in R5] for s in R5]  # low[s][a][b]
        Gam = [[[sum(gi[r, s]*low[s][a][b] for s in R5) for b in R5] for a in R5] for r in R5]
        dlow = [[[[(ddg[c][a][s][b] + ddg[c][b][s][a] - ddg[c][s][a][b])/2 for b in R5] for a in R5] for s in R5]
                for c in R5]
        dGam = [[[[sum(dgi[c][r][s]*low[s][a][b] + gi[r, s]*dlow[c][s][a][b] for s in R5) for b in R5]
                  for a in R5] for r in R5] for c in R5]  # dGam[c][r][a][b]
        return gi, dgi, Gam, dGam

    def P(self, X, m, e=0):
        X = [mp.mpf(c) for c in X]
        key = (tuple(str(c) for c in X), str(m), str(e))
        if not hasattr(self, "cache"):
            self.cache = {}
        if key in self.cache:
            return self.cache[key]
        self.cache[key] = self._P(X, mp.mpf(m), mp.mpf(e))
        return self.cache[key]

    def _P(self, X, m, e):
        g, dg, ddg = self.jets("g", X, m, e)
        g0, dg0, ddg0 = self.jets("g0", X, m, 0)
        gi, dgi, G, dG = self.christoffel(g, dg, ddg)
        _, _, G0, dG0 = self.christoffel(g0, dg0, ddg0)
        R5 = range(5)
        Ric = mp.matrix(5, 5)
        for a in R5:
            for b in R5:
                Ric[a, b] = (sum(dG[r][r][a][b] for r in R5) - sum(dG[b][r][a][r] for r in R5)
                             + sum(G[r][r][l]*G[l][a][b] for r in R5 for l in R5)
                             - sum(G[r][b][l]*G[l][a][r] for r in R5 for l in R5))
        dGam = [[[G[r][a][b] - G0[r][a][b] for b in R5] for a in R5] for r in R5]
        Dv = [sum(gi[a, b]*dGam[r][a][b] for a in R5 for b in R5) for r in R5]
        dD = [[sum(dgi[c][a][b]*dGam[r][a][b] + gi[a, b]*(dG[c][r][a][b] - dG0[c][r][a][b]) for a in R5 for b in R5)
               for r in R5] for c in R5]  # dD[c][r]
        nab = [[dD[n][r] + sum(G0[r][n][l]*Dv[l] for l in R5) for r in R5] for n in R5]  # nab[n][r] = Dh_n D^r
        out = mp.matrix(5, 5)
        for m_ in R5:
            for n in R5:
                out[m_, n] = Ric[m_, n] - (sum(g[m_, r]*nab[n][r] for r in R5) + sum(g[n, r]*nab[m_][r] for r in R5))/2
        return out


PTS = [[mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("-0.6"), mp.mpf("0.9"), mp.mpf("1.1")],
       [mp.mpf("-0.8"), mp.mpf("0.7"), mp.mpf("1.4"), mp.mpf("-0.5"), mp.mpf("0.6")],
       [mp.mpf("1.2"), mp.mpf("-1.1"), mp.mpf("0.3"), mp.mpf("1.6"), mp.mpf("-0.4")]]
MU = mp.mpf("0.8")


def zop(H, cx=1):
    return sp.Matrix(5, 5, lambda i, j: (t - V1)*sp.diff(H[i, j], t)
                     + cx*sum(XS[a]*sp.diff(H[i, j], XS[a]) for a in range(1, 5)))


def z1():
    print("Z1  the exact scaling identity of the gauge-fixed operator (mpmath, 40 digits)")
    mp.mp.dps = 40
    h = h_explicit()
    Zh = zop(h)
    op = Op(gb0(mu), h, Zh)
    worst, ctl1, ctl2, size = mp.mpf(0), mp.mpf(10)**9, mp.mpf(10)**9, mp.mpf(0)
    Zh2 = zop(h, cx=2)
    op2 = Op(gb0(mu), h, Zh2)
    for X in PTS:
        c = [V1, 0, 0, 0, 0]
        Pv = op.P(X, MU)
        ZP = mp.matrix(5, 5)
        Z2P = mp.matrix(5, 5)
        for i in range(5):
            for j in range(i, 5):
                ZP[i, j] = ZP[j, i] = mp.diff(lambda s: op.P([mp.mpf(c[a]) + s*(X[a] - c[a]) for a in range(5)],
                                                             MU)[i, j], 1)
        DPZ = mp.matrix(5, 5)
        DPZ2 = mp.matrix(5, 5)
        dmu = mp.matrix(5, 5)
        for i in range(5):
            for j in range(i, 5):
                DPZ[i, j] = DPZ[j, i] = mp.diff(lambda e: op.P(X, MU, e)[i, j], 0)
                DPZ2[i, j] = DPZ2[j, i] = mp.diff(lambda e: op2.P(X, MU, e)[i, j], 0)
                dmu[i, j] = dmu[j, i] = mp.diff(lambda m: op.P(X, m)[i, j], MU)
                # the non-uniform dilation (t - v1) d_t + 2 x.d_x applied to P, for the control
                Z2P[i, j] = Z2P[j, i] = mp.diff(lambda s: op.P([X[0] + s*(X[0] - mp.mpf(c[0]))]
                                                               + [X[a]*(1 + 2*s) for a in range(1, 5)], MU)[i, j], 0)
        lhs = ZP + 2*Pv
        rhs = DPZ - 2*MU*dmu
        worst = max(worst, mp.mnorm(lhs - rhs, 1))
        size = max(size, mp.mnorm(lhs, 1), mp.mnorm(dmu, 1))
        ctl1 = min(ctl1, mp.mnorm(lhs - DPZ, 1))
        ctl2 = min(ctl2, mp.mnorm(Z2P + 2*Pv - (DPZ2 - 2*MU*dmu), 1))
    check("Z1a (Z + 2) P(h) = DP(h)[Z h] - 2 mu d_mu P(h), all components, three points", worst < mp.mpf(10)**-18,
          "max |defect| " + mp.nstr(worst, 3) + " against sizes up to " + mp.nstr(size, 3))
    check("Z1b control: without - 2 mu d_mu P the identity fails at every point", ctl1 > mp.mpf(10)**-4,
          "min defect " + mp.nstr(ctl1, 3))
    check("Z1c control: the non-uniform dilation (t - v1) d_t + 2 x.d_x fails at every point", ctl2 > mp.mpf(10)**-4,
          "min defect " + mp.nstr(ctl2, 3))
    s = sp.Symbol("s", positive=True)
    pull = sp.simplify(s**2*gb0(mu).subs({x1: s*x1, x2: s*x2, x3: s*x3, x4: s*x4}) - s**2*gb0(mu/s**2))
    check("Z1d the scaling behind it, exact: D_s^* g_b0(mu) = s^2 g_b0(mu s^-2) (components s^2 g(s x))",
          pull == sp.zeros(5, 5))


def lie_rot(H):
    """L_Omega H for Omega = x1 d_2 - x2 d_1 (components): Omega^c d_c H_ab + H_cb d_a Omega^c + H_ac d_b Omega^c"""
    Om = [0, -x2, x1, 0, 0]
    dOm = sp.Matrix(5, 5, lambda a, c: sp.diff(Om[c], XS[a]))
    return sp.Matrix(5, 5, lambda a, b: sum(Om[c]*sp.diff(H[a, b], XS[c]) for c in range(5))
                     + sum(H[c, b]*dOm[a, c] for c in range(5)) + sum(H[a, c]*dOm[b, c] for c in range(5))), Om, dOm


def z2():
    print("Z2  the time translation and the rotations commute with the operator")
    mp.mp.dps = 40
    h = h_explicit()
    LO, Om, dOm = lie_rot(h)
    comp_only = sp.Matrix(5, 5, lambda a, b: sum(Om[c]*sp.diff(h[a, b], XS[c]) for c in range(5)))
    cases = {"dt": sp.Matrix(5, 5, lambda a, b: sp.diff(h[a, b], t)), "rot": LO, "rot-comp": comp_only,
             "d1": sp.Matrix(5, 5, lambda a, b: sp.diff(h[a, b], x1))}
    res = {}
    for nm, K in cases.items():
        op = Op(gb0(mu), h, K)
        worst = mp.mpf(0)
        for X in PTS[:2]:
            Pv = op.P(X, MU)
            DPK = mp.matrix(5, 5)
            for i in range(5):
                for j in range(i, 5):
                    DPK[i, j] = DPK[j, i] = mp.diff(lambda e: op.P(X, MU, e)[i, j], 0)
            if nm == "dt":
                vec = [1, 0, 0, 0, 0]
            elif nm == "d1":
                vec = [0, 1, 0, 0, 0]
            else:
                vec = [0, -X[2], X[1], 0, 0]
            dirP = mp.matrix(5, 5)
            for i in range(5):
                for j in range(i, 5):
                    dirP[i, j] = dirP[j, i] = mp.diff(lambda s: op.P([X[a] + s*vec[a] for a in range(5)], MU)[i, j], 0)
            if nm in ("rot", "rot-comp"):
                dO = [[float(dOm[a, c]) for c in range(5)] for a in range(5)]
                if nm == "rot":
                    for a in range(5):
                        for b in range(5):
                            dirP[a, b] += sum(Pv[c, b]*dO[a][c] + Pv[a, c]*dO[b][c] for c in range(5))
            worst = max(worst, mp.mnorm(dirP - DPK, 1))
        res[nm] = worst
    check("Z2a d_t P(h) = DP(h)[d_t h] (g_b0 static)", res["dt"] < mp.mpf(10)**-18, mp.nstr(res["dt"], 3))
    check("Z2b L_Omega P(h) = DP(h)[L_Omega h], Omega = x1 d_2 - x2 d_1 with its index terms",
          res["rot"] < mp.mpf(10)**-18, mp.nstr(res["rot"], 3))
    check("Z2c control: the rotation acting on components alone fails", res["rot-comp"] > mp.mpf(10)**-4,
          mp.nstr(res["rot-comp"], 3))
    check("Z2d control: the translation d_1 (not an isometry of g_b0) fails", res["d1"] > mp.mpf(10)**-4,
          mp.nstr(res["d1"], 3))


def z3():
    print("Z3  the scalar case: round 2's Z2c is Z1's identity")
    v, r, kap = sp.symbols("v r kappa", positive=True)
    F = sp.Function("F")(v, r)

    def box(phi, m):
        gi = sp.Matrix([[0, 1], [1, 1 - m/r**2]])
        co = [v, r]
        return sp.simplify(sum(sp.diff(r**3*gi[a, b]*sp.diff(phi, co[b]), co[a]) for a in range(2)
                               for b in range(2))/r**3 - kap*phi/r**2)
    Z = lambda e: (v - V1)*sp.diff(e, v) + r*sp.diff(e, r)
    lhs = sp.simplify(Z(box(F, mu)) + 2*box(F, mu) - box(Z(F), mu))
    dmu = sp.simplify(-2*mu*sp.diff(box(F, mu), mu))
    target = 2*mu/r**3*sp.diff(r*sp.diff(F, r), r)
    check("Z3a (Z + 2) box_g phi - box_g(Z phi) = -2 mu d_mu(box_g) phi = 2 mu r^-3 d_r(r d_r) phi",
          sp.simplify(lhs - dmu) == 0 and sp.simplify(dmu - target) == 0)


def z4():
    print("Z4  the Hessian from the commuted fields")
    phi = sp.Function("phi")(*XS)
    r = RR
    ok = True
    Om = lambda i, j, f: XS[i]*sp.diff(f, XS[j]) - XS[j]*sp.diff(f, XS[i])
    Zf = (t - V1)*sp.diff(phi, t) + sum(XS[a]*sp.diff(phi, XS[a]) for a in range(1, 5))
    for i in range(1, 5):
        rhs = XS[i]/r**2*(Zf - (t - V1)*sp.diff(phi, t)) - sum(XS[j]*Om(i, j, phi) for j in range(1, 5))/r**2
        ok = ok and sp.simplify(rhs - sp.diff(phi, XS[i])) == 0
    check("Z4a d_i = r^-1 xhat_i (Z - (t - v1) d_t) - r^-2 x_j Omega_ij on every function", ok)
    tt, rr = sp.symbols("tt rr", real=True)
    th_ = sp.Symbol("theta", nonnegative=True)
    # on W: v = t + r >= v1 and t <= v1 (S at t ~ c_IVP < v1 = c_IVP + 4R + O(1)): t = v1 - theta r, 0 <= theta <= 1
    coef = sp.simplify(((V1 - tt)/rr).subs(tt, V1 - th_*rr))
    check("Z4b on W, t = v1 - theta r with 0 <= theta <= 1 (v >= v1, t <= v1): |t - v1|/r = theta <= 1",
          coef == th_)
    coeff = (V1 - tt)/rr
    lim = sp.limit(coeff.subs(rr, 2), tt, -sp.oo)
    check("Z4c control: outside W (fixed r, t -> -oo) the coefficient (v1 - t)/r is unbounded", lim == sp.oo)


def z5():
    print("Z5  the b-derivative on S")
    r = sp.Symbol("r", positive=True)
    f = sp.Function("f")(r)
    tt, rr = sp.symbols("tt rr")
    H = tt**2*rr**3 + sp.sin(tt*rr) + sp.exp(tt)/rr  # an explicit h(t, r); f stays generic
    onS = lambda e: e.subs(tt, f).subs(rr, r)
    lhs = r*sp.diff(onS(H), r)
    Zh = (tt - V1)*sp.diff(H, tt) + rr*sp.diff(H, rr)
    rhs = onS(Zh) + (V1 - f + r*sp.diff(f, r))*onS(sp.diff(H, tt))
    check("Z5a r d/dr (h|_S) = (Z h)|_S + (v1 - f + r f')(d_t h)|_S", sp.simplify(sp.expand(lhs - rhs)) == 0)
    rdr = onS(rr*sp.diff(H, rr))
    check("Z5b control: (r d_r h)|_S is not r d/dr (h|_S) (the slice is not t = const)",
          sp.simplify(lhs - rdr) != 0)


def z6():
    print("Z6  Z on N")
    r, tt = sp.symbols("r tt", positive=True)
    v = tt + r
    Zt, Zr = tt - V1, r
    Zv = sp.simplify(Zt*sp.diff(v, tt) + Zr*sp.diff(v, r))
    check("Z6a Z(v - v1) = v - v1: Z is tangent to N = {v = v1}", sp.simplify(Zv - (v - V1)) == 0)
    on = {tt: V1 - r}
    check("Z6b on N, Z = r d_r - r d_t (coefficients (t - v1, r) = (-r, r))", sp.simplify(Zt.subs(on) + r) == 0)
    q = sp.Symbol("q", positive=True)
    Fx = sp.Function("F")(sp.Symbol("w"))
    e = r**(-q)*Fx
    check("Z6c Z (r^-q F(xhat)) = -q r^-q F along N", sp.simplify(r*sp.diff(e, r) + q*e) == 0)
    check("Z6d control: d_t v = 1, d_t is transverse to N", sp.diff(v, tt) == 1)


def z7():
    print("Z7  the kernels of the Z-commuted energy at weight a")
    a, tt, rr = sp.symbols("a tt rr", positive=True)
    L = sp.Symbol("L", positive=True)  # v1 - t_S
    kern = {"mu d_mu P: mu r^-2 d d -> mu r^-3 d(Gamma h)": 3,
            "(Z Sigma) d d h_R and (d d Sigma) Z h_R: r^-3": 3,
            "Q(d Z h, d Sigma): r^-3": 3}
    ok = True
    for aa in (sp.Rational(51, 20), sp.Rational(11, 4), sp.Rational(59, 20)):
        for nm, p in kern.items():
            I = sp.integrate((tt)**(-p), (tt, L, sp.oo))  # tt := v1 - t >= L
            ok = ok and I.is_finite
        I1 = sp.integrate(tt**(-sp.Rational(1, 2) - aa), (tt, L, sp.oo))  # (Z h_R) d d h_R, sup r |d d h_R|
        I2 = sp.integrate(tt**(-sp.Rational(3, 2) - aa), (tt, L, sp.oo))  # Q(d Z h_R, d h_R)
        res = sp.sqrt(sp.integrate(rr**(2*aa - 12)*rr**3, (rr, tt, sp.oo)))  # ||r^a P(Sigma)||, P(Sigma) ~ r^-6
        I3 = sp.integrate(sp.simplify(res), (tt, L, sp.oo))
        ok = ok and I1.is_finite and I2.is_finite and I3.is_finite
    check("Z7a every kernel is integrable for a = 51/20, 11/4, 59/20 (in (5/2, 3))", ok)
    res3 = sp.sqrt(sp.integrate(rr**(2*3 - 12)*rr**3, (rr, tt, sp.oo)))
    I3 = sp.integrate(sp.simplify(res3), (tt, L, sp.oo))
    check("Z7b control: at a = 3 the residual's kernel (v1 - t)^(a-4) is not integrable", I3 == sp.oo, str(res3))
    I1 = sp.integrate(tt**(-1), (tt, L, sp.oo))
    check("Z7c control: at a = 1/2 the quasilinear h_R-kernel (v1 - t)^(-1/2-a) is not integrable", I1 == sp.oo)


def z8():
    print("Z8  the class on S from the S-flux")
    a, beta, rho, r = sp.symbols("a beta rho r", positive=True)
    ok = True
    for aa, bb in ((sp.Rational(11, 4), sp.Rational(19, 5)), (sp.Rational(11, 4), sp.Rational(7, 2))):
        # phi = rho^beta = r^-beta: Hardy side int r^(2a-2) phi^2 r^3 dr, and the b-norm int |rho^-(a+1) phi|^2 drho/rho
        hardy = sp.integrate(r**(2*aa - 2)*r**(-2*bb)*r**3, (r, 1, sp.oo))
        bnorm = sp.integrate((rho**(-(aa + 1))*rho**bb)**2/rho, (rho, 0, 1))
        ok = ok and (hardy.is_finite == bnorm.is_finite) and (bnorm.is_finite == (bb > aa + 1))
    check("Z8a the S-energy (Hardy) and rho^(a+1) L^2_b(drho/rho) agree on rho^beta, finite exactly for beta > a + 1",
          ok)
    l0, aa = sp.Rational(19, 5), sp.Rational(29, 10)
    inclass = sp.integrate((rho**(-l0)*rho**(aa + 1 - sp.Rational(1, 100)))**2/rho, (rho, 0, 1)).is_finite
    check("Z8b l0 = 3.8, a = 2.9 in (l0 - 1, 3): rho^(a + 1 - 0.01) lies in rho^(l0) L^2_b", inclass)
    exps = sorted({p + sp.Rational(j, 1) for p in (2, sp.Rational(5, 2), 3, sp.Rational(7, 2), 4) for j in range(3)})
    half = all((2*e).is_integer and e >= 2 for e in exps)
    check("Z8c Sigma|_S: rho^p F_p(1 - (v1 - f) rho) has exponents p + j, all in E_0^(1/2) = {2 + j/2}", half,
          str([str(e) for e in exps[:8]]))
    ptw = (aa + sp.Rational(1, 2)) > l0
    check("Z8d control: the pointwise reading O(rho^(1/2 + a)) (round 2 R2.8) fails at l0 = 3.8, a = 2.9", not ptw)


def main():
    for f in (z3, z4, z5, z6, z7, z8, z1, z2):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
