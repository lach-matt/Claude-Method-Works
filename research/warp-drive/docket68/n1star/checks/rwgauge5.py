#!/usr/bin/env python3
"""rwgauge5.py -- GAUGEDECAY5.md section 1: the gauge vector carrying Part VIII's solution to the Regge-Wheeler-type
gauge of [KI03] in the class, computed.

Background: five-dimensional Tangherlini in the ingoing chart, g = -f dv^2 + 2 dv dr + r^2 (dth^2 + cos^2 th dphi1^2
+ sin^2 th dphi2^2), f = 1 - s^2/r^2 (s = sqrt(mu) = r_h).  The class: components depending on (v, r, th), no phi
components (T^2 and both reflections).  Convention: a perturbation h is moved by h -> h + L_xi g, L_xi g = nabla xi +
(nabla xi)^T for a 1-form xi.

  R1 (exact) The gauge vector.  For arbitrary class functions beta_v, beta_r, tau of (v, r, th),
         xi = (-beta_a + (r^2/2) d_a(tau/r^2)) dy^a - (1/2) d_th tau dth
     has (L_xi g)_{a th} = -d_th beta_a, no phi components, and (L_xi g)_ij = -(D_i D_j - gamma_ij Lap/3) tau + (a
     multiple of gamma_ij): it removes from h the 1-form parts h_{a i} = D_i beta_a and the scalar-derived traceless
     angular part (D_i D_j - gamma Lap/3) tau.  Control: r^2 d_a(tau/r^2)/2 replaced by d_a tau/2 fails.
  R2 (exact; READ [KI03] (2.4)-(2.8), pp. 4-5) Mode by mode it is [KI03]'s vector.  For a scalar mode with harmonic
     S = P_j(cos 2 th), k^2 = l(l + 2), l = 2j (l = 2, 4), h_ab = f_ab S, h_ai = r f_a S_i, h_ij = 2 r^2 (H_L gamma_ij S
     + H_T S_ij), S_i = -k^-1 D_i S, S_ij = k^-2 D_i D_j S + gamma_ij S/3: beta_a = -(r/k) f_a S, tau = 2 r^2 H_T S/k^2,
     R1's xi has orbit part X_a S with X_a = (r/k)(f_a + (r/k) D_a H_T) ([KI03] (2.8)), and h + L_xi g = F_ab S dy^a dy^b
     + 2 r^2 F S gamma, with F, F_ab [KI03]'s invariants (2.7a)-(2.7b): in the gauge f_a = 0 = H_T the components ARE
     the invariants.  Control: (r/k)^2 replaced by r/k^2 in X_a fails.
  R3 (exact) The sphere.  (a) Lap P_j(cos 2 th) = -l(l + 2) P_j, l = 2j, j <= 5.  (b) D^i D^j (D_i D_j - gamma Lap/3) tau
     = (2/3) Lap (Lap + 3) tau for every class tau(th).  (c) A class 1-form a(th) dth with zero divergence is c/(sin th
     cos th) dth, smooth only for c = 0: class 1-forms on S^3 are exact (no vector type).  (d) The divergence of a class
     symmetric 2-tensor is a class 1-form (no phi components).  (e) For j = 1..4: ||D P_j||^2 = k^2 ||P_j||^2 and
     ||(D D - gamma Lap/3) P_j||^2 = (2/3) k^2 (k^2 - 3) ||P_j||^2 over S^3.  (f) The l-uniform constants:
     sup_{l >= 2} (1 + k^2)^2 / ((2/3) k^2 (k^2 - 3)) = 243/80 (at l = 2; the function decreases for k^2 >= 8) and
     sup (1 + k^2)/k^2 = 9/8.  Control: (b) with (Lap + 2) in place of (Lap + 3) fails.
  R4 (exact) The l = 0 sector (linearised Birkhoff with the linearised mass).  For h0 = A dv^2 + 2 B dv dr + C dr^2 +
     2 r^2 H gamma (functions of v, r): (a) the linearisation of m = R^2 (1 - |dR|^2), the five-dimensional Misner-
     Sharp mass (m(g) = mu), is dmu[h0] = 2 mu H + r^2 (A + 2 f B + f^2 C) - 2 r^2 (d_v + f d_r)(r H); (b) dmu[L_Y g]
     = 0 for every spherically symmetric Y; (c) d(dmu[h0]) is a linear combination, with coefficients in r, of the
     components of DRic(h0) (so dmu is constant for vacuum h0); (d) dmu[dv^2/r^2] = 1 and DRic(dv^2/r^2) = 0; (e) Y1 =
     -r H dv (the vector -r H d_r) removes H; (f) if H = 0: omega := (B + f C/2) dv + (C/2) dr has d omega in the span
     of DRic(h0), and for zeta with d zeta = omega, L_{zeta d_v} g = h0 - (dmu[h0]/r^2) dv^2; (g) a spherically
     symmetric Killing field is c d_v; (h) DRic is validated: DRic(L_Y g) = 0, DRic(dv^2/r^2) = 0.  Controls: dmu
     without its 2 mu H term is not gauge invariant; omega without f C/2 is not closed modulo DRic; DRic(dv^2/r^3) != 0.
  R5 (exact) The loss of one power in the l = 0 time component is attained by the implication 'L_Y g decays => Y
     decays': Y = (1 + v)^-q d_v has L_Y g = O(v^(-q-1)) with every derivative, and Y = O(v^-q).  Control: the claim
     that Y decays like L_Y g fails for it.

Labels: computed (exact, sympy).  Run: python3 checks/rwgauge5.py   (a few minutes)
"""
import sys

import sympy as sp

v, r, th, p1, p2, s = sp.symbols("v r theta phi1 phi2 s", positive=True)
mu = s**2
X = [v, r, th, p1, p2]
N = 5


class Geo:
    """a warped metric -F dv^2 + 2 dv dr + r^2 gamma in the ingoing chart, with tensor calculus"""

    def __init__(self, F):
        self.f = F
        g = sp.zeros(5)
        g[0, 0] = -F
        g[0, 1] = g[1, 0] = 1
        g[2, 2] = r**2
        g[3, 3] = r**2*sp.cos(th)**2
        g[4, 4] = r**2*sp.sin(th)**2
        self.g = g
        self.gi = sp.simplify(g.inv())
        gi = self.gi
        self.Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                - sp.diff(g[b, c], X[d])) for d in range(N))/2)
                      for c in range(N)] for b in range(N)] for a in range(N)]

    def cov1(self, w):
        G = self.Gam
        return [[sp.diff(w[b], X[a]) - sum(G[c][a][b]*w[c] for c in range(N)) for b in range(N)] for a in range(N)]

    def cov2(self, h):
        G = self.Gam
        return [[[sp.diff(h[a][b], X[c]) - sum(G[d][c][a]*h[d][b] + G[d][c][b]*h[a][d] for d in range(N))
                  for b in range(N)] for a in range(N)] for c in range(N)]

    def lie(self, w):
        D = self.cov1(w)
        return [[D[a][b] + D[b][a] for b in range(N)] for a in range(N)]

    def tr(self, h):
        return sum(self.gi[a, b]*h[a][b] for a in range(N) for b in range(N))

    def dric(self, h):
        """DRic(h)_ab = (1/2)(nabla^c nabla_a h_bc + nabla^c nabla_b h_ac - nabla^c nabla_c h_ab - nabla_a nabla_b tr h)"""
        G, gi = self.Gam, self.gi
        T = self.cov2(h)                                     # T[c][a][b] = nabla_c h_ab

        def DT(d, c, a, b):
            return (sp.diff(T[c][a][b], X[d]) - sum(G[e][d][c]*T[e][a][b] + G[e][d][a]*T[c][e][b]
                                                    + G[e][d][b]*T[c][a][e] for e in range(N)))
        t_ = self.tr(h)
        dt = [sp.diff(t_, x) for x in X]
        Ht = [[sp.diff(dt[b], X[a]) - sum(G[c][a][b]*dt[c] for c in range(N)) for b in range(N)] for a in range(N)]
        out = [[0]*N for _ in range(N)]
        for a in range(N):
            for b in range(a, N):
                e = 0
                for c in range(N):
                    for d in range(N):
                        if gi[c, d] != 0:
                            e += gi[c, d]*(DT(d, a, b, c) + DT(d, b, a, c) - DT(d, c, a, b))
                out[a][b] = out[b][a] = (e - Ht[a][b])/2
        return out


GEO = Geo(1 - mu/r**2)
gam = sp.diag(1, sp.cos(th)**2, sp.sin(th)**2)             # the round metric of S^3 in (th, phi1, phi2)
gami = gam.inv()
SPH = [th, p1, p2]
sqg = sp.sin(th)*sp.cos(th)                                  # sqrt det gamma


def sph_hess(tau):
    """D_i D_j tau on (S^3, gamma)"""
    Gs = [[[sum(gami[a, d]*(sp.diff(gam[d, b], SPH[c]) + sp.diff(gam[d, c], SPH[b]) - sp.diff(gam[b, c], SPH[d]))
                for d in range(3))/2 for c in range(3)] for b in range(3)] for a in range(3)]
    d1 = [sp.diff(tau, x) for x in SPH]
    return sp.Matrix(3, 3, lambda i, j: sp.diff(d1[j], SPH[i]) - sum(Gs[c][i][j]*d1[c] for c in range(3))), Gs


def sph_lap(u):
    return sp.diff(sqg*sp.diff(u, th), th)/sqg


def sph_div_tensor(Tm):
    """(D^i T_ij) for a symmetric 2-tensor on S^3"""
    _, Gs = sph_hess(sp.Integer(0))
    out = []
    for j in range(3):
        e = 0
        for i in range(3):
            for k in range(3):
                if gami[i, k] == 0:
                    continue
                DT = sp.diff(Tm[k, j], SPH[i]) - sum(Gs[c][i][k]*Tm[c, j] + Gs[c][i][j]*Tm[k, c] for c in range(3))
                e += gami[i, k]*DT
        out.append(e)
    return out


def sph_div_form(w):
    return sum(sp.diff(sqg*sum(gami[i, k]*w[k] for k in range(3)), SPH[i]) for i in range(3))/sqg


def zero(e):
    """exact test of e == 0: simplify, then (trigonometric polynomials of multiple angles) after expand_trig"""
    e = sp.expand(e)
    if sp.simplify(e) == 0:
        return True
    return sp.simplify(sp.expand_trig(e)) == 0


def legendre_S(j):
    return sp.legendre(j, sp.cos(2*th))


# --------------------------------------------------------------------------------------------------------------- R1
def xi_of(bv, br, tau, weight=True):
    if weight:
        xa = [-bv + r**2*sp.diff(tau/r**2, v)/2, -br + r**2*sp.diff(tau/r**2, r)/2]
    else:
        xa = [-bv + sp.diff(tau, v)/2, -br + sp.diff(tau, r)/2]
    return [xa[0], xa[1], -sp.diff(tau, th)/2, 0, 0]


def r1(control=False):
    bv, br, tau = [sp.Function(n)(v, r, th) for n in ("beta_v", "beta_r", "tau")]
    L = GEO.lie(xi_of(bv, br, tau, weight=not control))
    ok = zero(L[0][2] + sp.diff(bv, th)) and zero(L[1][2] + sp.diff(br, th))
    ok &= all(zero(L[a][b]) for a in range(N) for b in (3, 4) if a != b)
    Hs, _ = sph_hess(tau)
    M = sp.Matrix(3, 3, lambda i, j: L[2 + i][2 + j]) + r**0*(Hs - gam*sph_lap(tau)/3)
    trM = sum(gami[i, j]*M[i, j] for i in range(3) for j in range(3))
    MTF = M - gam*trM/3
    ok &= all(zero(MTF[i, j]) for i in range(3) for j in range(3))
    print("  R1%s: (L_xi g)_{a th} = -d_th beta_a, no phi components, traceless angular part -(DD - gamma Lap/3) tau: %s"
          % (" control (weight dropped)" if control else "", ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- R2
def r2(control=False):
    ok = True
    names = ("fvv", "fvr", "frr", "fv", "fr", "HL", "HT")
    fvv, fvr, frr, fv, fr, HL, HT = [sp.Function(n)(v, r) for n in names]
    g2 = sp.Matrix([[-(1 - mu/r**2), 1], [1, 0]])
    g2i = g2.inv()
    Y2 = [v, r]
    G2 = [[[sum(g2i[a, d]*(sp.diff(g2[d, b], Y2[c]) + sp.diff(g2[d, c], Y2[b]) - sp.diff(g2[b, c], Y2[d]))
                for d in range(2))/2 for c in range(2)] for b in range(2)] for a in range(2)]
    for j in (1, 2):
        l = 2*j
        k = sp.sqrt(l*(l + 2))
        S = legendre_S(j)
        Si = [-sp.diff(S, x)/k for x in SPH]
        Hs, _ = sph_hess(S)
        Sij = Hs/k**2 + gam*S/3
        fa = [fv, fr]
        fab = [[fvv, fvr], [fvr, frr]]
        h = [[0]*N for _ in range(N)]
        for a in range(2):
            for b in range(2):
                h[a][b] = fab[a][b]*S
            for i in range(3):
                h[a][2 + i] = h[2 + i][a] = r*fa[a]*Si[i]
        for i in range(3):
            for jj in range(3):
                h[2 + i][2 + jj] = 2*r**2*(HL*gam[i, jj]*S + HT*Sij[i, jj])
        if control:
            Xa = [(r/k)*(fa[a] + (r/k**2)*sp.diff(HT, Y2[a])) for a in range(2)]
        else:
            Xa = [(r/k)*(fa[a] + (r/k)*sp.diff(HT, Y2[a])) for a in range(2)]   # [KI03] (2.8)
        Lk = (r/k)*HT
        xi = [Xa[0]*S, Xa[1]*S] + [r*Lk*Si[i] for i in range(3)]
        # R1's formula with beta_a = -(r/k) f_a S, tau = 2 r^2 H_T S/k^2
        beta = [-(r/k)*fa[a]*S for a in range(2)]
        tau = 2*r**2*HT*S/k**2
        xi1 = xi_of(beta[0], beta[1], tau)
        same = all(zero(xi[a] - xi1[a]) for a in range(3))
        L = GEO.lie(xi)
        DrX = Xa[0] + (1 - mu/r**2)*Xa[1]                          # D^a r X_a
        F = HL + HT/3 + DrX/r                                       # (2.7a), n = 3
        DX = [[sp.diff(Xa[b], Y2[a]) - sum(G2[c][a][b]*Xa[c] for c in range(2)) for b in range(2)] for a in range(2)]
        Fab = [[fab[a][b] + DX[a][b] + DX[b][a] for b in range(2)] for a in range(2)]   # (2.7b)
        good = same
        for a in range(N):
            for b in range(a, N):
                target = 0
                if a < 2 and b < 2:
                    target = Fab[a][b]*S
                elif a >= 2 and b >= 2:
                    target = 2*r**2*F*S*gam[a - 2, b - 2]
                good &= zero(h[a][b] + L[a][b] - target)
        print("  R2%s l = %d: KI's X_a is R1's vector and h + L_xi g = F_ab S dy dy + 2 r^2 F S gamma: %s "
              "(R1's formula reproduced: %s)" % (" control" if control else "", l, good, same), flush=True)
        ok &= good
    return ok


# --------------------------------------------------------------------------------------------------------------- R3
def r3(control=False):
    ok = True
    if not control:
        for j in range(6):
            l = 2*j
            ok &= zero(sph_lap(legendre_S(j)) + l*(l + 2)*legendre_S(j))
        print("  R3 (a) Lap P_j(cos 2th) = -l(l+2) P_j, l = 2j <= 10: %s" % ok, flush=True)
    tau = sp.Function("tau")(th)
    Hs, _ = sph_hess(tau)
    T = Hs - gam*sph_lap(tau)/3
    div = sph_div_tensor(T)
    ddiv = sph_div_form(div)
    rhs = sp.Rational(2, 3)*sph_lap(sph_lap(tau) + (2 if control else 3)*tau)
    b = zero(ddiv - rhs)
    print("  R3 (b)%s D^i D^j (D_i D_j - gamma Lap/3) tau = (2/3) Lap(Lap + %d) tau: %s"
          % (" control" if control else "", 2 if control else 3, b), flush=True)
    if control:
        return b
    ok &= b
    a = sp.Function("a")(th)
    sol = sp.dsolve(sph_div_form([a, 0, 0]), a)
    c_ok = zero(sp.diff(sol.rhs*sqg, th)) and not zero(sol.rhs*sqg)        # a nonzero constant over sin th cos th
    print("  R3 (c) class 1-forms with zero divergence: %s (smooth on S^3 only for C1 = 0)" % sol, flush=True)
    ok &= c_ok
    A1, A2, A3 = [sp.Function(n)(th) for n in ("t1", "t2", "t3")]
    Tg = sp.diag(A1, A2, A3)
    dv_ = sph_div_tensor(Tg)
    d_ok = zero(dv_[1]) and zero(dv_[2])
    print("  R3 (d) the divergence of a class symmetric tensor has no phi components: %s" % d_ok, flush=True)
    ok &= d_ok
    import mpmath
    mpmath.mp.dps = 40
    meas = 4*sp.pi**2*sqg                                          # dw = sin th cos th dth dphi1 dphi2
    for j in range(1, 5):
        l = 2*j
        k2 = l*(l + 2)
        S = legendre_S(j)
        n0 = sp.Rational(1, 2*j + 1)*2*sp.pi**2                      # P_j(u)^2, dw = pi^2 du on u = cos 2th
        dS = [sp.diff(S, x) for x in SPH]
        HsS, _ = sph_hess(S)
        TS = HsS - gam*sph_lap(S)/3
        dens = [S**2*meas, sum(gami[i, i]*dS[i]**2 for i in range(3))*meas,
                sum(gami[i, i]*gami[jj, jj]*TS[i, jj]**2 for i in range(3) for jj in range(3))*meas]
        nums = [mpmath.quad(sp.lambdify(th, e, "mpmath"), [0, mpmath.pi/4, mpmath.pi/2]) for e in dens]
        tgt = [n0, k2*n0, sp.Rational(2, 3)*k2*(k2 - 3)*n0]
        errs = [abs(nums[i] - mpmath.mpf(sp.N(tgt[i], 40)))/abs(mpmath.mpf(sp.N(tgt[i], 40))) for i in range(3)]
        e_ok = max(errs) < mpmath.mpf("1e-30")
        ok &= e_ok
        print("  R3 (e) j = %d (l = %d): ||P||^2 = %s, ||DP||^2 = k^2 ||P||^2, ||(DD - gamma Lap/3)P||^2 = (2/3)k^2(k^2-3)"
              "||P||^2, quadrature to 40 digits, relative error %s: %s"
              % (j, l, n0, mpmath.nstr(max(errs), 3), e_ok), flush=True)
    x = sp.Symbol("x", positive=True)
    q = (1 + x)**2/(sp.Rational(2, 3)*x*(x - 3))
    dq = sp.factor(sp.diff(q, x))
    num, den = sp.fraction(dq)
    mono = all(c >= 0 for c in sp.Poly(sp.expand(-num.subs(x, x + 8)), x).all_coeffs()) and \
        all(c >= 0 for c in sp.Poly(sp.expand(den.subs(x, x + 8)), x).all_coeffs())
    sup1 = q.subs(x, 8)
    mono2 = sp.simplify(sp.diff((1 + x)/x, x) + 1/x**2) == 0       # (1 + x)/x decreases: derivative -1/x^2
    f_ok = mono and sup1 == sp.Rational(243, 80) and bool(mono2)
    print("  R3 (f) (1+k^2)^2/((2/3)k^2(k^2-3)) has derivative %s, negative for k^2 >= 8 (coefficients of -num(x+8) "
          "and den(x+8) >= 0: %s); sup at l = 2: %s; (1+k^2)/k^2 decreasing, sup 9/8 at l = 2" % (dq, mono, sup1),
          flush=True)
    ok &= f_ok
    return ok


# --------------------------------------------------------------------------------------------------------------- R4
def l0_tensor(A, B, C, H):
    h = [[0]*N for _ in range(N)]
    h[0][0], h[0][1], h[1][0], h[1][1] = A, B, B, C
    for i in range(3):
        h[2 + i][2 + i] = 2*r**2*H*gam[i, i]
    return h


def dmu_formula(A, B, C, H, with_H=True):
    f = 1 - mu/r**2
    e = r**2*(A + 2*f*B + f**2*C) - 2*r**2*(sp.diff(r*H, v) + f*sp.diff(r*H, r))
    return e + (2*mu*H if with_H else 0)


def r4(control=False):
    A, B, C, H = [sp.Function(n)(v, r) for n in ("A", "B", "C", "H")]
    f = 1 - mu/r**2
    ok = True
    if control:
        Yv, Yr = sp.Function("Yv")(v, r), sp.Function("Yr")(v, r)
        hY = GEO.lie([Yv, Yr, 0, 0, 0])
        HY = sp.simplify(hY[2][2]/(2*r**2))
        c1 = zero(dmu_formula(hY[0][0], hY[0][1], hY[1][1], HY, with_H=False))
        h0 = l0_tensor(A, B, C, 0)
        D = GEO.dric(h0)
        om_v, om_r = B, C/2                                       # without f C/2
        curl = sp.expand(sp.diff(om_v, r) - sp.diff(om_r, v))
        c2 = in_span(curl, [D[0][0], D[0][1], D[1][1], D[2][2]], [A, B, C])
        hc = l0_tensor(1/r**3, 0, 0, 0)
        c3 = all(zero(e) for row in GEO.dric(hc) for e in row)
        print("  R4 controls: dmu without 2 mu H gauge invariant: %s; omega without f C/2 closed mod DRic: %s; "
              "DRic(dv^2/r^3) = 0: %s" % (c1, c2, c3), flush=True)
        return c1 or c2 or c3
    # (a) the linearisation of m = R^2 (1 - g~^{-1}(dR, dR))
    eps = sp.Symbol("eps")
    gt = sp.Matrix([[-f + eps*A, 1 + eps*B], [1 + eps*B, eps*C]])
    R2_ = r**2*(1 + 2*eps*H)
    R_ = sp.sqrt(R2_)
    dR = [sp.diff(R_, v), sp.diff(R_, r)]
    m = R2_*(1 - sum(gt.inv()[a, b]*dR[a]*dR[b] for a in range(2) for b in range(2)))
    lin = sp.diff(m, eps).subs(eps, 0)
    a_ok = zero(lin - dmu_formula(A, B, C, H)) and zero(m.subs(eps, 0) - mu)
    print("  R4 (a) dmu[h0] = 2 mu H + r^2 (A + 2fB + f^2 C) - 2 r^2 (d_v + f d_r)(r H), m(g) = mu: %s" % a_ok,
          flush=True)
    ok &= a_ok
    Yv, Yr = sp.Function("Yv")(v, r), sp.Function("Yr")(v, r)
    hY = GEO.lie([Yv, Yr, 0, 0, 0])
    HY = sp.simplify(hY[2][2]/(2*r**2))
    b_ok = zero(dmu_formula(hY[0][0], hY[0][1], hY[1][1], HY))
    print("  R4 (b) dmu[L_Y g] = 0: %s" % b_ok, flush=True)
    ok &= b_ok
    h0 = l0_tensor(A, B, C, H)
    D = GEO.dric(h0)
    comps = [D[0][0], D[0][1], D[1][1], D[2][2]]
    dm = dmu_formula(A, B, C, H)
    c_ok = True
    for y in (v, r):
        c_ok &= in_span(sp.diff(dm, y), comps, [A, B, C, H])
        print("  R4 (c) d_%s dmu = sum c_i DRic_i over (vv, vr, rr, th th): %s, c = %s"
              % (y, c_ok, list(getattr(in_span, "last", {}).values())), flush=True)
    ok &= c_ok
    K = l0_tensor(1/r**2, 0, 0, 0)
    d_ok = zero(dmu_formula(1/r**2, 0, 0, 0) - 1) and all(zero(e) for row in GEO.dric(K) for e in row)
    print("  R4 (d) dmu[dv^2/r^2] = 1, DRic(dv^2/r^2) = 0: %s" % d_ok, flush=True)
    ok &= d_ok
    hY1 = GEO.lie([-r*H, 0, 0, 0, 0])
    e_ok = zero(hY1[2][2]/(2*r**2) + H)
    print("  R4 (e) Y1 = -r H dv (vector -r H d_r) has L_Y1 g angular part -2 r^2 H gamma: %s" % e_ok, flush=True)
    ok &= e_ok
    h0p = l0_tensor(A, B, C, 0)
    Dp = GEO.dric(h0p)
    compsp = [Dp[0][0], Dp[0][1], Dp[1][1], Dp[2][2]]
    om_v, om_r = B + f*C/2, C/2
    curl = sp.expand(sp.diff(om_v, r) - sp.diff(om_r, v))
    f1 = in_span(curl, compsp, [A, B, C])
    zv, zr = sp.symbols("zeta_v zeta_r")                          # d_v zeta, d_r zeta
    Lz = [[-2*f*zv, zv - f*zr], [zv - f*zr, 2*zr]]               # L_{zeta d_v} g, orbit block
    dmp = dmu_formula(A, B, C, 0)
    tgt = [[A - dmp/r**2, B], [B, C]]
    f2 = all(zero((Lz[a][b] - tgt[a][b]).subs({zv: om_v, zr: om_r})) for a in range(2) for b in range(2))
    zeta = sp.Function("zeta")(v, r)
    Lzg = GEO.lie([-f*zeta, zeta, 0, 0, 0])                       # the 1-form of the vector zeta d_v
    f3 = all(zero(Lzg[a][b] - Lz[a][b].subs({zv: sp.diff(zeta, v), zr: sp.diff(zeta, r)})) for a in range(2)
             for b in range(2)) and all(zero(Lzg[a][b]) for a in range(N) for b in range(N) if a >= 2 or b >= 2)
    print("  R4 (f) H = 0: d omega in span DRic: %s; L_{zeta d_v} g = h0 - (dmu/r^2) dv^2 when d zeta = omega: %s "
          "(L_{zeta d_v} g computed: %s)" % (f1, f2, f3), flush=True)
    ok &= f1 and f2 and f3
    Zv, Zr = sp.Function("Zv")(v, r), sp.Function("Zr")(v, r)
    LZ = GEO.lie([-f*Zv + Zr, Zv, 0, 0, 0])                       # the 1-form of Zv d_v + Zr d_r
    g_ok = zero(LZ[2][2] - 2*r*Zr) and zero(LZ[1][1].subs(Zr, 0) - 2*sp.diff(Zv, r)) and \
        zero(LZ[0][0].subs(Zr, 0) + 2*f*sp.diff(Zv, v))
    print("  R4 (g) L_Z g = 0 for spherically symmetric Z forces Z^r = 0 (angular), d_r Z^v = 0, d_v Z^v = 0: %s"
          % g_ok, flush=True)
    ok &= g_ok
    h_ok = all(zero(e) for row in GEO.dric(GEO.lie([Yv, Yr, 0, 0, 0])) for e in row)
    print("  R4 (h) DRic(L_Y g) = 0 for spherically symmetric Y: %s" % h_ok, flush=True)
    ok &= h_ok
    return ok


def in_span(target, comps, funcs):
    """is target = sum_i c_i(r) comps_i identically in the jets of funcs (functions of v, r)?"""
    import itertools
    syms = {}
    n = 0
    for F in funcs:
        for i in range(4):
            for j in range(4 - i):
                sym = sp.Symbol("J%d" % n)
                n += 1
                if not i + j:
                    syms[F] = sym
                    continue
                for order in set(itertools.permutations([v]*i + [r]*j)):    # mixed partials in any order
                    syms[sp.Derivative(F, *order)] = sym

    def sub(e):
        return sp.expand(sp.expand(sp.sympify(e).doit()).xreplace(syms))      # top-down: whole derivatives first
    cs = sp.symbols("c0:%d" % len(comps))
    expr = sp.expand(sub(target) - sum(c*sub(e) for c, e in zip(cs, comps)))
    from sympy.core.function import AppliedUndef
    assert not expr.atoms(AppliedUndef) and not expr.atoms(sp.Derivative), "a jet was not read"
    eqs = [sp.cancel(sp.together(e)) for e in sp.Poly(expr, *sorted(set(syms.values()), key=str)).coeffs()]
    eqs = [e for e in eqs if e != 0]
    for m in range(1, len(eqs) + 1):                               # solve a leading subset, then check all
        sol = sp.solve(eqs[:m], cs, dict=True)
        if not sol:
            return False
        if all(sp.simplify(e.subs(sol[0])) == 0 for e in eqs):
            in_span.last = {c: sp.factor(sol[0].get(c, c)) for c in cs}
            return True
    return False


# --------------------------------------------------------------------------------------------------------------- R5
def r5(control=False):
    q = sp.Rational(3, 2)
    f = 1 - mu/r**2
    zeta = (1 + v)**(-q)
    L = GEO.lie([-f*zeta, zeta, 0, 0, 0])
    rates = [sp.limit(sp.simplify(L[a][b]*v**(q + 1)), v, sp.oo) for a in range(2) for b in range(2)]
    bounded = all(x.is_finite for x in rates) and any(x != 0 for x in rates)
    lim_Y = sp.limit(zeta*v**(q + 1), v, sp.oo)
    if control:
        print("  R5 control: Y = O(v^-(q+1)) like L_Y g: %s" % lim_Y.is_finite, flush=True)
        return bool(lim_Y.is_finite)
    print("  R5: Y = (1+v)^-%s d_v: v^(q+1) L_Y g -> %s (finite, not all 0: %s); v^q Y -> %s"
          % (q, rates, bounded, sp.limit(zeta*v**q, v, sp.oo)), flush=True)
    return bounded and sp.limit(zeta*v**q, v, sp.oo) == 1


CHECKS = [("R1", r1), ("R2", r2), ("R3", r3), ("R4", r4), ("R5", r5)]


def main():
    ok = True
    for name, fn in CHECKS:
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
