"""sf5.py -- checks behind Part III.G (proof5/PART-III-G-SPECTRAL.md, D236): [Hin26] section 9.1 at n = 4, the
spectral family N_sf(lam) of the model at future timelike infinity.  Labels: computed (exact, sympy).

The model.  On 4+1 Minkowski space, rho = 1/r, t_* = t - r, v := rho t_*, and 2 rho^-2 Lbar acts on rho^lam u(v, w) as
rho^lam N_sf(lam) u with ([Hin26] (9.2) at n = 4)
    N_sf(lam) = -2 d_v (v d_v + lam - 3/2 - S) + Lt(v d_v + lam),   Lt(x) = -x^2 + a x + kappa + b,
S the endomorphism of III.F (2.2), Lt the dilation-invariant b-operator rho^-2 hat(2 Lbar)(0) (III.F Lemma 2.1 (2)).  For
the scalar wave operator S = 0, a = 2, b = 0 and kappa = l(l+2) on harmonics of degree l.  Below S, a, b are constant
symbols (the identities are pointwise in the fibre, and the S^3-operators are spectators unless named).

  S1  The scalar model: rho^(-2-lam) Box (rho^lam u(v)) = N_sf(lam) u with c = 3/2 and Lt(x) = -x^2 + 2x + kappa, for
      Box = d_t^2 - d_r^2 - (3/r) d_r + kappa/r^2.  Control: c = 1 (the four-dimensional value) fails.
  S2  The dilation-reduced metric: in (T = log r, v, omega), rhat := r^-2 (-dt^2 + dr^2 + r^2 domega^2) has inverse
      d_T^2 - 2(v+1) d_T d_v + v(v+2) d_v^2 + gslash^-1; so dT is spacelike (ghat^-1(dT,dT) = 1), dv is timelike exactly
      on -2 < v < 0, and the principal symbol of N_sf(lam), as a spectral family in T at sigma = -i lam, is
      ghat^-1(-sigma dT + xi dv + eta).  Control: ghat^-1(dT, dT) = -1 fails.
  S3  The radial set N*{v = 0}: for p2 = v(v+2) xi^2 + |eta|^2 and rho_inf = 1/xi (xi > 0), H := rho_inf H_p2 has
      H rho_inf = 2(1+v) rho_inf and H q = 4(v+2) v^2 + 4(1+v) etahat^2 for q := v^2 + etahat^2, etahat := eta rho_inf
      (eta a flat fibre coordinate; {p2, |eta|^2} = 0 on S^3 too).  Control: H rho_inf = 2(1+2v) rho_inf fails.
  S4  The threshold: for the density dv/(2+v) and complex constants lam, S, the first-order coefficient of
      (N - N*)/(2i) at v = 0 is c1 d_v with i c1(0) = 3 + 2 Re S - 2 Re lam, i.e. sigma_1(Im N_sf) = xi(3 + 2 Re S - 2 Re
      lam) at N*{v = 0}, and the coefficient of d_v^2 in N - N* vanishes.  Control: c = 1 gives 2 + 2 Re S - 2 Re lam.
  S5  The commutator and the tower: [v d_v, N_sf(lam)] = -N_sf(lam) + Lt(v d_v + lam), and N_sf(lam+1) d_v = d_v
      N_sf(lam) ([Hin26] p. 16's u_3 tower; the record's 10.37 (a)).  Control: N_sf(lam) d_v != d_v N_sf(lam).
  S6  The semiclassical family at lam = i z/h: the principal symbol of h^2 N_sf is p = (v xi + z)((v+2) xi + z) +
      |eta|^2; for z = 1 and xit := -(v+2)(v xi + 1), H_p xit = 2(v+1)(|eta|^2 - p), so xit is non-decreasing along the
      flow on {p = 0} over v > -1; and H_p |eta|^2 = 0.  Control: xit' := -(v+1)(v xi + 1) is not monotone.
  S7  The cone point: with R = 1/v, xi_c := -v(v xi + 1), eta_c := v eta, G := 2(1 + R xi_c) xi_c + xi_c^2 + |eta_c|^2
      (II.F (1.13) at z = 1) equals v^2 p, and (1 + 2R) xi_c = xit; with II.F (3.12)'s field
      H = (2(1+2R)xi_c + 2)(R d_R - eta_c d_eta_c) + 2(|eta_c|^2 - R xi_c^2) d_xi_c,
      H xit = -2(1+R) xi_c (xit + 2) on {G = 0}.  Control: H xi_c is not of one sign on {G = 0}.
  S8  The Fourier reduction: under u -> uhat(rhat) = int e^(i rhat v) u dv and the conjugation by rhat^(1-lam),
      N_sf(lam) becomes rhat^2 N_tf(+1) with N_tf(sh) = 2 i sh rhohat (rhohat d_rhohat - 3/2 - S) + rhohat^2 Lt(rhohat
      d_rhohat), rhohat = 1/rhat (I.C (4.1); II.F (5.11)-(5.13) with i sigma = lam).  Control: the conjugation by
      rhat^(-lam) fails.
  S9  The iota+ normal operator: N_iota(lam) := v^(2+lam) N_sf(lam) v^(-lam) (R = 1/v) equals
      -2 v (v d_v - lam)(v d_v - 3/2 - S) + v^2 Lt(v d_v) on a general u(v) (III.G' (1.1)).  Control: v^(2-lam)
      N_sf(lam) v^lam fails.
  S10 Kernels supported at the light cone: by the transpose, N_sf(lam) delta^(j) = -2 (lam - j - 5/2 - S)
      delta^(j+1) + Lt(lam - j - 1) delta^(j), j = 0..4, tested on a general polynomial (III.G' Lemma 4.3).
      Control: the top factor lam - j - 3/2 - S fails.
  S11 The turning point of Lemma 4.1 (d): with p = (v xi + 1)((v + 2) xi + 1) + q (z = 1, q = |eta|^2 conserved), at a
      critical point of v on {p = 0} (H_p v = d_xi p = 0), H_p^2 v = -4(v + 1)/(v(v + 2)), negative for v > 0, so every
      critical point over v > 0 is a strict maximum (III.G Lemma 4.1 (d), D238).  Control: the opposite sign fails.
"""
import sys
import sympy as sp

v, r, t, T = sp.symbols('v r t T', real=True)
lam, S, a, b, kap, z = sp.symbols('lam S a b kappa z')
xi, eta, h = sp.symbols('xi eta h', real=True)
f = sp.Function('f')
c32 = sp.Rational(3, 2)


def Lt(x_op, u, aa=a, bb=b, kk=kap):
    """Lt(X) u for X a linear operator (callable), Lt(x) = -x^2 + aa x + kk + bb."""
    Xu = x_op(u)
    return -x_op(Xu) + aa * Xu + (kk + bb) * u


def N_sf(L, u, c=c32, SS=S, aa=a, bb=b, kk=kap):
    X = lambda w: v * sp.diff(w, v) + (L - c - SS) * w
    Y = lambda w: v * sp.diff(w, v) + L * w
    return -2 * sp.diff(X(u), v) + Lt(Y, u, aa, bb, kk)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


def s1():
    # on monomials v^m, m symbolic: a second-order operator in v is determined by its action on them; r, v > 0
    m = sp.symbols('m', integer=True)
    rp, vp = sp.symbols('rpos vpos', positive=True)
    U = rp**(-lam) * ((t - rp) / rp)**m
    box = sp.diff(U, t, 2) - sp.diff(U, rp, 2) - 3 / rp * sp.diff(U, rp) + kap / rp**2 * U
    lhs = sp.simplify(sp.powsimp(sp.expand_power_base((box * rp**(2 + lam)).subs(t, rp * (vp + 1)), force=True),
                                 force=True) / vp**m)

    def rhs(c):
        g = sp.Function('g')
        e = N_sf(lam, g(v), c=c, SS=0, aa=2, bb=0).subs(g(v), v**m).doit()
        return sp.simplify((e / v**m).subs(v, vp))
    ok = zero(lhs - rhs(c32))
    ctrl = not zero(lhs - rhs(1))
    print('S1 scalar model, c = 3/2:', 'PASS' if ok else 'FAIL', '(control c = 1:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s2():
    # metric r^-2 (-dt^2 + dr^2) in (T, v): r = e^T, t = r (v + 1)
    rr = sp.exp(T)
    tt = rr * (v + 1)
    J = sp.Matrix([[sp.diff(tt, T), sp.diff(tt, v)], [sp.diff(rr, T), sp.diff(rr, v)]])
    g = sp.diag(-1, 1)
    gh = sp.simplify(J.T * g * J / rr**2)
    ginv = sp.simplify(gh.inv())
    sigma = sp.symbols('sigma')
    sym = sp.expand((sp.Matrix([[-sigma, xi]]) * ginv * sp.Matrix([[-sigma], [xi]]))[0] + eta**2)
    p = sp.expand((v * xi + sigma) * ((v + 2) * xi + sigma) + eta**2)
    ok = (zero(ginv[0, 0] - 1) and zero(ginv[0, 1] + (v + 1)) and zero(ginv[1, 1] - v * (v + 2)) and zero(sym - p))
    ctrl = not zero(ginv[0, 0] + 1)
    print('S2 dilation-reduced metric, dT spacelike, dv timelike on (-2,0):', 'PASS' if ok else 'FAIL',
          '(control g^TT = -1:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def hamilton(p, g, q=(v,), pq=(xi,)):
    return sum(sp.diff(p, pp) * sp.diff(g, qq) - sp.diff(p, qq) * sp.diff(g, pp) for qq, pp in zip(q, pq))


def s3():
    y = sp.symbols('y', real=True)
    p2 = v * (v + 2) * xi**2 + eta**2
    H = lambda g: (1 / xi) * hamilton(p2, g, (v, y), (xi, eta))
    rinf = 1 / xi
    q = v**2 + (eta / xi)**2
    ok = zero(H(rinf) - 2 * (1 + v) * rinf) and zero(H(q) - (4 * (v + 2) * v**2 + 4 * (1 + v) * (eta / xi)**2))
    ok = ok and zero(hamilton(p2, eta**2, (v, y), (xi, eta)))
    ctrl = not zero(H(rinf) - 2 * (1 + 2 * v) * rinf)
    print('S3 radial set: H rho_inf = 2(1+v) rho_inf, H q >= 2q near v = 0:', 'PASS' if ok else 'FAIL',
          '(control:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s4():
    l1, l2, s_1, s_2 = sp.symbols('l1 l2 s1 s2', real=True)
    L = l1 + sp.I * l2
    SS = s_1 + sp.I * s_2
    m = 1 / (2 + v)

    def coeffs(c):
        # N = sum_k A_k(v) d_v^k on functions of v (kappa etc. constants)
        u = f(v)
        e = sp.expand(N_sf(L, u, c=c, SS=SS))
        A = [sp.simplify(e.coeff(sp.diff(f(v), v, k))) if k > 0 else None for k in range(3)]
        A[0] = sp.simplify(e.subs({sp.diff(f(v), v, 2): 0}).subs({sp.diff(f(v), v): 0}).subs(f(v), 1))
        return A

    def adj(A):
        # formal adjoint for <u,w> = int u wbar m dv: N* w = m^-1 sum (-d)^k (conj(A_k) m w)
        w = f(v)
        e = 0
        for k, Ak in enumerate(A):
            e += (-1)**k * sp.diff(sp.conjugate(Ak) * m * w, v, k)
        e = sp.expand(sp.simplify(e / m))
        B = [None] * 3
        for k in (2, 1):
            B[k] = sp.simplify(e.coeff(sp.diff(f(v), v, k)))
        B[0] = sp.simplify(e.subs({sp.diff(f(v), v, 2): 0}).subs({sp.diff(f(v), v): 0}).subs(f(v), 1))
        return B

    def check(c):
        A = coeffs(c)
        B = adj(A)
        c2 = sp.simplify(A[2] - B[2])
        c1 = sp.simplify(((A[1] - B[1]) / (2 * sp.I)).subs(v, 0))
        return c2, sp.simplify(sp.expand(sp.I * c1))
    c2, ic1 = check(c32)
    ok = zero(c2) and zero(ic1 - (3 + 2 * s_1 - 2 * l1))
    _, ic1b = check(1)
    ctrl = not zero(ic1b - (3 + 2 * s_1 - 2 * l1))
    print('S4 threshold at N*{v=0}: sigma_1(Im N_sf) = xi(3 + 2 Re S - 2 Re lam):', 'PASS' if ok else 'FAIL',
          '(control c = 1:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s5():
    u = f(v)
    vd = lambda w: v * sp.diff(w, v)
    Y = lambda w: v * sp.diff(w, v) + lam * w
    comm = vd(N_sf(lam, u)) - N_sf(lam, vd(u))
    ok1 = zero(comm - (-N_sf(lam, u) + Lt(Y, u)))
    ok2 = zero(N_sf(lam + 1, sp.diff(u, v)) - sp.diff(N_sf(lam, u), v))
    ctrl = not zero(N_sf(lam, sp.diff(u, v)) - sp.diff(N_sf(lam, u), v))
    ok = ok1 and ok2
    print('S5 [v d_v, N] = -N + Lt(v d_v + lam); N(lam+1) d_v = d_v N(lam):', 'PASS' if ok else 'FAIL',
          '(control:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s6():
    # principal symbol of h^2 N_sf(i z / h): replace d_v -> i xi / h, lam -> i z / h, kappa -> eta^2 / h^2, keep h^0
    D = sp.I * xi / h
    L = sp.I * z / h
    Xs = v * D + L - c32 - S
    Ys = v * D + L
    sym = sp.expand(h**2 * (-2 * D * Xs + (-Ys**2 + a * Ys + eta**2 / h**2 + b)))
    prin = sp.limit(sym, h, 0)
    p = sp.expand((v * xi + z) * ((v + 2) * xi + z) + eta**2)
    ok = zero(prin - p)
    p1 = p.subs(z, 1)
    xit = -(v + 2) * (v * xi + 1)
    y = sp.symbols('y', real=True)
    Hx = hamilton(p1, xit, (v, y), (xi, eta))
    ok = ok and zero(Hx - 2 * (v + 1) * (eta**2 - p1)) and zero(hamilton(p1, eta**2, (v, y), (xi, eta)))
    bad = -(v + 1) * (v * xi + 1)
    Hb = sp.expand(hamilton(p1, bad, (v, y), (xi, eta)))
    # on {p1 = 0} at eta = 0 the bad candidate changes sign: take v = 1/2, the incoming ray xi = -1/(v+2) and the
    # outgoing ray xi = -1/v (both with eta = 0), and a point with eta != 0
    vals = []
    for vv, xx, ee in [(sp.Rational(1, 2), -sp.Rational(2, 5), 0), (sp.Rational(1, 2), -2, 0)]:
        vals.append(Hb.subs({v: vv, xi: xx, eta: ee}))
    ctrl = any(sp.sign(x) < 0 for x in vals)     # decreases somewhere on the characteristic set
    print('S6 semiclassical symbol; H_p xit = 2(v+1)(|eta|^2 - p):', 'PASS' if ok else 'FAIL',
          '(control xit\':', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s7():
    R = 1 / v
    xc = -v * (v * xi + 1)
    ec = v * eta
    G = 2 * (1 + R * xc) * xc + xc**2 + ec**2
    p = (v * xi + 1) * ((v + 2) * xi + 1) + eta**2
    xit = -(v + 2) * (v * xi + 1)
    ok = zero(G - v**2 * p) and zero((1 + 2 * R) * xc - xit)
    # II.F (3.12) in its own variables
    Rr, X, E = sp.symbols('R X E', real=True)
    def Hf(g):
        return ((2 * (1 + 2 * Rr) * X + 2) * (Rr * sp.diff(g, Rr) - E * sp.diff(g, E))
                + 2 * (E**2 - Rr * X**2) * sp.diff(g, X))
    XT = (1 + 2 * Rr) * X
    HXT = sp.expand(Hf(XT)).subs(E**2, -2 * X - (1 + 2 * Rr) * X**2)
    ok = ok and zero(HXT - (-2 * (1 + Rr) * X * (XT + 2)))
    HX = sp.expand(Hf(X)).subs(E**2, -2 * X - (1 + 2 * Rr) * X**2)
    # control: H xi_c changes sign on the characteristic set (R = 1, X near the incoming end)
    a1 = HX.subs({Rr: 1, X: -sp.Rational(2, 3) + sp.Rational(1, 100)})
    a2 = HX.subs({Rr: 1, X: -sp.Rational(1, 10)})
    ctrl = sp.sign(a1) != sp.sign(a2)
    print('S7 cone point: G = v^2 p, (1+2R) xi_c = xit, H xit = -2(1+R) xi_c (xit+2) on {G = 0}:',
          'PASS' if ok else 'FAIL', '(control H xi_c:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s8():
    # on monomials: u = v^m (formal Fourier transform of homogeneous functions); use the operator calculus:
    # F d_v = -i rhat F, F v = -i d_rhat F; so F (v d_v) = -(rhat d_rhat + 1) F.
    rh = sp.symbols('rhat', positive=True)
    g = sp.Function('g')
    w = g(rh)
    Dv = lambda W: -sp.I * rh * W                       # image of d_v
    VDv = lambda W: -(rh * sp.diff(W, rh) + W)          # image of v d_v

    def NF(W, L):
        X = lambda U: VDv(U) + (L - c32 - S) * U
        Y = lambda U: VDv(U) + L * U
        return -2 * Dv(X(W)) + Lt(Y, W)
    # conjugation: w = rhat^(lam - 1) wflat
    wf = sp.Function('k')(rh)
    conj = sp.simplify(rh**(1 - lam) * NF(rh**(lam - 1) * wf, lam))
    rhoh = sp.symbols('rhohat', positive=True)
    # target: rhat^2 N_tf(+1) wflat, with rhohat d_rhohat = -rhat d_rhat
    RD = lambda U: -rh * sp.diff(U, rh)
    target = rh**2 * (2 * sp.I * (1 / rh) * (RD(wf) - (c32 + S) * wf) + (1 / rh)**2 * Lt(RD, wf))
    ok = zero(conj - target)
    conjb = sp.simplify(rh**(-lam) * NF(rh**(lam) * wf, lam))
    ctrl = not zero(conjb - target)
    print('S8 Fourier reduction to rhat^2 N_tf(+1):', 'PASS' if ok else 'FAIL',
          '(control rhat^-lam:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s9():
    u = f(v)
    lhs = v**(2 + lam) * N_sf(lam, v**(-lam) * u)
    Y = lambda w: v * sp.diff(w, v)
    W1 = v * sp.diff(u, v) - (c32 + S) * u
    target = -2 * v * (v * sp.diff(W1, v) - lam * W1) + v**2 * Lt(Y, u)
    vp = sp.Symbol('vp', positive=True)
    z9 = lambda e: sp.simplify(sp.expand(sp.powsimp(sp.expand(e.subs(v, vp)), force=True))) == 0
    ok = z9(lhs - target)
    ctrl = not z9(v**(2 - lam) * N_sf(lam, v**lam * u) - target)
    print('S9 iota+ normal operator -2v(v d_v - lam)(v d_v - 3/2 - S) + v^2 Lt(v d_v):', 'PASS' if ok else 'FAIL',
          '(control v^(2-lam) N v^lam:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s10():
    p = sp.symbols('p0:8')
    phi = sum(p[k] * v**k for k in range(8))
    # transpose of N_sf: d_v^t = -d_v, (v d_v)^t = -1 - v d_v
    Xt = lambda w: -w - v * sp.diff(w, v) + (lam - c32 - S) * w
    Yt = lambda w: -w - v * sp.diff(w, v) + lam * w
    Nt = Xt(2 * sp.diff(phi, v)) + Lt(Yt, phi)
    pair = lambda j, g: (-1)**j * sp.diff(g, v, j).subs(v, 0)        # <delta^(j), g>
    ok, ctrl = True, True
    for j in range(5):
        lhs = pair(j, Nt)
        L1 = lam - j - 1
        want = (-2 * (lam - j - sp.Rational(5, 2) - S) * pair(j + 1, phi)
                + (-L1**2 + a * L1 + kap + b) * pair(j, phi))
        bad = (-2 * (lam - j - c32 - S) * pair(j + 1, phi) + (-L1**2 + a * L1 + kap + b) * pair(j, phi))
        ok &= zero(lhs - want)
        ctrl &= not zero(lhs - bad)
    print('S10 N_sf delta^(j) = -2(lam - j - 5/2 - S) delta^(j+1) + Lt(lam - j - 1) delta^(j):',
          'PASS' if ok else 'FAIL', '(control lam - j - 3/2 - S:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def s11():
    vv, x, q = sp.symbols('v xi q', real=True)
    p = (vv * x + 1) * ((vv + 2) * x + 1) + q
    H = lambda F: sp.diff(p, x) * sp.diff(F, vv) - sp.diff(p, vv) * sp.diff(F, x) + 0 * q
    Hv = H(vv)
    xs = sp.solve(sp.Eq(Hv, 0), x)[0]
    qs = sp.solve(sp.Eq(p.subs(x, xs), 0), q)[0]
    H2 = sp.simplify(H(Hv).subs(x, xs).subs(q, qs))
    want = -4 * (vv + 1) / (vv * (vv + 2))
    ok = sp.simplify(H2 - want) == 0
    ctrl = sp.simplify(H2 + want) != 0
    print('S11 H_p^2 v = -4(v+1)/(v(v+2)) at critical points of v on Sigma:', 'PASS' if ok else 'FAIL',
          '(control opposite sign:', 'fails' if ctrl else 'PASSES', ')')
    return ok and ctrl


def run():
    ok = True
    for fn in (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11):
        ok &= fn()
    print('sf5.py:', 'all checks pass' if ok else 'FAILURES')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
