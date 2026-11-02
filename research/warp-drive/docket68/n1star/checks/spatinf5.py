"""spatinf5.py -- SETTLE-GLAM5 round 2, R3 and R4: the expansion at spatial infinity with a conormal remainder (the
scaling field Z and the weight window), and the lam-dependence of the record's fixed-lam expansion (the Gronwall
factor on the far region, the interpolation that turns polynomial constants into smallness, and a linear model).

Tangherlini in the ingoing chart, g = -f dv^2 + 2 dv dr + r^2 dOmega_3^2, f = 1 - mu/r^2 (= eta + mu r^-2 dv^2, the
Kerr-Schild g_(b_0) with v = t + r); Z := (v - v1) d_v + r d_r = (t - v1) d_t + r d_r, the Euler field centred at
N's vertex (t, x) = (v1, 0).

  Z1 (exact) L_Z eta = 2 eta (Z homothetic for Minkowski) and L_Z g - 2 g = -2 mu r^-2 dv^2 (the defect decays like
     r^-2 relative to g). Control: r d_r alone is not homothetic for eta.
  Z2 (exact) on phi(v, r) Y_l, box_g computed from the metric is box_eta - mu r^-3 d_r(r d_r) (tail5.py's boxT), and
     [Z, box_eta] = -2 box_eta, [Z, box_g] + 2 box_g = 2 mu r^-3 d_r(r d_r): an operator of order r^-2 relative to
     box, with r-homogeneous coefficients. Control: [r d_r, box_eta] is not a multiple of box_eta.
  Z3 (exact) in (tau, rho) = (t/r, 1/r), Z = -rho d_rho - v1 rho d_tau: b-normal at I_0 (III.A's sense).
     Control: d_t = rho d_tau vanishes at I_0 (not b-normal).
  Z4 (exact) Z(r^-p F(s)) = -p r^-p F(s), s = (v - v1)/r: the self-similar terms of round 1's (b1) are Z-eigenfields,
     so prod_p (Z + p) annihilates the subtracted expansion (III.A Lemma 1.3 with V = -Z). Control: r^-p log r F(s)
     is not annihilated by Z + p, only by (Z + p)^2.
  Z5 (exact) the weight window for the remainder: a remainder O(r^-q), conormal, on N has weighted flux finite
     exactly for a < q - 1, and the weighted energy class gives it O(rho^(1/2 + a)) at S, which lies in
     rho^(l_0) L^2_b near rho = 0 exactly when a > l_0 - 1/2: a window exists iff l_0 < q - 1/2. q = 4 (the
     terms through r^(-7/2) subtracted) serves every l_0 in (3, 7/2). Control: q = 7/2 (through r^-3 only) serves
     no l_0 > 3.
  U1 (exact) the Gronwall factor of Lemma 9.5 with the kernel C lam^-1 t^(-3/2) of (9.8)'s 1/lam term, on
     t >= T = lam^-2 (the far region of Lemma 11.0): exp(2C), bounded in lam. Control: from t = lam^-1 it is
     exp(2C lam^(-1/2)), which exceeds every power lam^-M as lam -> 0.
  U2 (exact) interpolation: if the tangential derivatives of e's remainder on N obey both |.| <= A lam^(K-4) r^-2
     ((P-iii), every K, lam-uniform) and |.| <= B lam^-M r^(-(J+3)/2) ((11.7) with its ell-gain, fixed-lam constants
     at most polynomial), the weighted flux with weight a < (J - 1)/2 is at most C(lam^(2(K-4) - 2as) + lam) with
     s = (2M + 1)/(J - 1 - 2a): it tends to 0 once K - 4 > a s. Control: the lam-uniform bound alone gives an
     infinite flux at every a > 0.
  U3 (computed) the linear model of the expansion coefficients: a_j = c_j int a_(j-1) from the radiation field
     F = lam env(v) sin(v/lam) (tail5.py T1), env the C_c^oo bump: sup |I_j| / lam^(j+1) stays below 25 and does
     not grow over lam = 2^-3..2^-6 for the j-fold integrals I_j, j = 1, 2, 3 (no lam^-1 loss), and each
     d_v costs lam^-1. Control: a non-oscillating F = lam env gives sup |I_1| / lam^2 growing like lam^-1.
Labels: computed (exact, sympy; numpy for U3).

    python3 checks/spatinf5.py
"""
import sys

import numpy as np
import sympy as sp

FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


v, r, v1, mu, th, p1, p2, t = sp.symbols("v r v1 mu theta phi1 phi2 t", real=True)
X = [v, r, th, p1, p2]


def metric(m):
    f = 1 - m/r**2
    g = sp.zeros(5, 5)
    g[0, 0] = -f
    g[0, 1] = g[1, 0] = 1
    g[2, 2] = r**2
    g[3, 3] = r**2*sp.sin(th)**2
    g[4, 4] = r**2*sp.cos(th)**2
    return g


def lie(Zc, g):
    out = sp.zeros(5, 5)
    for a in range(5):
        for b in range(5):
            out[a, b] = sp.simplify(sum(Zc[c]*sp.diff(g[a, b], X[c]) + g[c, b]*sp.diff(Zc[c], X[a])
                                        + g[a, c]*sp.diff(Zc[c], X[b]) for c in range(5)))
    return out


def z1():
    print("Z1  Z is homothetic for eta, and nearly so for Tangherlini")
    Zc = [v - v1, r, 0, 0, 0]
    eta, g = metric(0), metric(mu)
    d0 = sp.simplify(lie(Zc, eta) - 2*eta)
    d1 = sp.simplify(lie(Zc, g) - 2*g)
    target = sp.zeros(5, 5)
    target[0, 0] = -2*mu/r**2
    check("Z1a L_Z eta = 2 eta", d0 == sp.zeros(5, 5))
    check("Z1b L_Z g - 2 g = -2 mu r^-2 dv^2", sp.simplify(d1 - target) == sp.zeros(5, 5), str(d1[0, 0]))
    d2 = sp.simplify(lie([0, r, 0, 0, 0], eta) - 2*eta)
    check("Z1c control: r d_r alone is not homothetic for eta", d2 != sp.zeros(5, 5))


def box_from_metric(phi, m, kappa):
    """box_g on phi(v, r) Y_l, Y_l an eigenfunction of the S^3 Laplacian with eigenvalue -kappa"""
    gi = sp.Matrix([[0, 1], [1, 1 - m/r**2]])
    vol = r**3
    co = [v, r]
    s = sum(sp.diff(vol*gi[a, b]*sp.diff(phi, co[b]), co[a]) for a in range(2) for b in range(2))/vol
    return sp.simplify(s - kappa*phi/r**2)


def z2():
    print("Z2  the commutator of Z with the wave operator")
    kap = sp.Symbol("kappa")
    F = sp.Function("F")(v, r)
    bT = box_from_metric(F, mu, kap)
    b0 = box_from_metric(F, 0, kap)
    D = sp.diff(r*sp.diff(F, r), r)/r**3
    check("Z2a box_g = box_eta - mu r^-3 d_r(r d_r) (from the metric)", sp.simplify(bT - b0 + mu*D) == 0)
    Z = lambda e: (v - v1)*sp.diff(e, v) + r*sp.diff(e, r)
    c0 = sp.simplify(Z(b0) - box_from_metric(Z(F), 0, kap) + 2*b0)
    check("Z2b [Z, box_eta] = -2 box_eta", c0 == 0)
    cT = sp.simplify(Z(bT) - box_from_metric(Z(F), mu, kap) + 2*bT)
    check("Z2c [Z, box_g] + 2 box_g = 2 mu r^-3 d_r(r d_r)", sp.simplify(cT - 2*mu*D) == 0, str(sp.factor(cT))[:70])
    Rr = lambda e: r*sp.diff(e, r)
    cr = sp.simplify(Rr(b0) - box_from_metric(Rr(F), 0, kap))
    q = sp.simplify(cr/b0)
    check("Z2d control: [r d_r, box_eta] is not a constant multiple of box_eta", not q.is_number, str(q)[:50])


def z3():
    print("Z3  Z at I_0")
    tau, rho = sp.symbols("tau rho", positive=True)
    tt, rr = tau/rho, 1/rho
    # a vector field a d_t + b d_r acts on (tau, rho) = (t/r, 1/r)
    Zt, Zr = tt - v1, rr
    tau_e, rho_e = t/r, 1/r
    Ztau = sp.simplify((Zt*sp.diff(tau_e, t) + Zr*sp.diff(tau_e, r)).subs({t: tt, r: rr}))
    Zrho = sp.simplify((Zt*sp.diff(rho_e, t) + Zr*sp.diff(rho_e, r)).subs({t: tt, r: rr}))
    check("Z3a Z = -rho d_rho - v1 rho d_tau (b-normal at rho = 0)",
          sp.simplify(Zrho + rho) == 0 and sp.simplify(Ztau + v1*rho) == 0, f"Z rho = {Zrho}, Z tau = {Ztau}")
    dtau = sp.simplify(sp.diff(tau_e, t).subs({t: tt, r: rr}))
    check("Z3b control: d_t = rho d_tau, which vanishes at I_0", sp.simplify(dtau - rho) == 0)


def z4():
    print("Z4  the self-similar terms are Z-eigenfields")
    F = sp.Function("F")
    Z = lambda e: (v - v1)*sp.diff(e, v) + r*sp.diff(e, r)
    ok = True
    for p in (2, sp.Rational(5, 2), 3, sp.Rational(7, 2)):
        e = r**(-p)*F((v - v1)/r)
        ok = ok and sp.simplify(Z(e) + p*e) == 0
    check("Z4a (Z + p)(r^-p F(s)) = 0 for p = 2, 5/2, 3, 7/2", ok)
    p = sp.Rational(5, 2)
    e = r**(-p)*sp.log(r)*F((v - v1)/r)
    once = sp.simplify(Z(e) + p*e)
    twice = sp.simplify(Z(once) + p*once)
    check("Z4b control: a log term is not annihilated by Z + p, but is by (Z + p)^2", once != 0 and twice == 0,
          str(once))


def z5():
    print("Z5  the weight window")
    rr, R = sp.symbols("rr R", positive=True)
    out = {}
    for q in (sp.Rational(7, 2), sp.Integer(4), sp.Rational(9, 2)):
        win = []
        for l0 in (sp.Rational(31, 10), sp.Rational(34, 10), sp.Rational(36, 10), sp.Rational(39, 10)):
            ok = False
            for a in [l0 - sp.Rational(1, 2) + sp.Rational(k, 100) for k in range(1, 100)]:
                flux = sp.integrate(rr**(2*a)*rr**(-2*q - 2)*rr**3, (rr, R, sp.oo))
                rho = sp.Symbol("rho", positive=True)
                cls = sp.integrate((rho**(-l0)*rho**(sp.Rational(1, 2) + a))**2/rho, (rho, 0, 1))
                if flux.is_finite and cls.is_finite:
                    ok = True
                    break
            win.append(ok)
        out[q] = win
    print("     l_0 = 3.1, 3.4, 3.6, 3.9: a window exists for q = 7/2, 4, 9/2:", {str(k): w for k, w in out.items()})
    check("Z5a q = 4 serves l_0 = 3.1, 3.4 and not 3.6, 3.9; q = 9/2 serves all four",
          out[sp.Integer(4)] == [True, True, False, False] and out[sp.Rational(9, 2)] == [True]*4)
    check("Z5b control: q = 7/2 (subtraction through r^-3 only) serves no l_0 > 3", out[sp.Rational(7, 2)] == [False]*4)


def u1():
    print("U1  the Gronwall factor on the far region")
    lam, C, tt = sp.symbols("lambda C tt", positive=True)
    k = sp.integrate(C/lam*tt**(-sp.Rational(3, 2)), (tt, lam**-2, sp.oo))
    check("U1a exp(int_(lam^-2)^oo C lam^-1 t^(-3/2) dt) = exp(2C)", sp.simplify(sp.exp(k) - sp.exp(2*C)) == 0, str(k))
    k2 = sp.integrate(C/lam*tt**(-sp.Rational(3, 2)), (tt, 1/lam, sp.oo))
    M = sp.Symbol("M", positive=True)
    lim = sp.limit(sp.exp(k2)*lam**M, lam, 0)
    check("U1b control: from t = lam^-1 the factor exp(2C lam^(-1/2)) beats every lam^-M", lim == sp.oo, str(k2))


def u2():
    print("U2  interpolation")
    lam, A, B, K, M, J, s = sp.symbols("lambda A B K M J s", positive=True)
    a = sp.Symbol("a", positive=True)
    R = sp.Symbol("R", positive=True)
    rr = sp.Symbol("rr", positive=True)
    ok = True
    for aa, JJ, MM, KK in ((sp.Rational(11, 4), 9, 5, 30), (sp.Rational(29, 10), 9, 12, 60),
                           (sp.Rational(11, 4), 12, 20, 40)):
        ss = (2*MM + 1)/sp.Integer(JJ - 1 - 2*aa)
        R0 = lam**(-ss)
        p1 = sp.integrate(rr**(2*aa)*(lam**(KK - 4)*rr**-2)**2*rr**3, (rr, 1, R0))
        p2 = sp.integrate(rr**(2*aa)*(lam**(-MM)*rr**(-sp.Rational(JJ + 3, 2)))**2*rr**3, (rr, R0, sp.oo))
        tot = sp.simplify(p1 + p2)
        good = KK - 4 > aa*ss
        lim = sp.limit(tot, lam, 0, "+")
        ok = ok and (lim == 0) == good
        print(f"     a = {aa}, J = {JJ}, M = {MM}, K = {KK}: s = {ss}, K - 4 > a s: {good}, flux -> {lim}")
    check("U2a the split flux tends to 0 exactly in the sampled cases with K - 4 > a s", ok)
    flux0 = sp.integrate(rr**(2*sp.Rational(1, 10))*(rr**-2)**2*rr**3, (rr, 1, sp.oo))
    check("U2b control: the lam-uniform bound alone gives an infinite flux at a = 1/10", flux0 == sp.oo)


def u3():
    print("U3  the linear model: iterated integrals of an oscillating radiation field")
    xs = np.linspace(0.5, 3.5, 2_000_001)
    y = (xs - 2)/1.5
    env = np.where(np.abs(y) < 1, np.exp(-1/np.maximum(1 - y*y, 1e-300)), 0.0)

    def cumint(f):
        dx = xs[1] - xs[0]
        return np.concatenate(([0.0], np.cumsum((f[1:] + f[:-1])*dx/2)))
    rows = []
    for k in (3, 4, 5, 6):
        lam = 2.0**-k
        F = lam*env*np.sin(xs/lam)
        I1 = cumint(F)
        I2 = cumint(I1)
        I3 = cumint(I2)
        dF = np.gradient(F, xs)
        rows.append((lam, [float(np.max(np.abs(I)))/lam**(j + 1) for j, I in ((1, I1), (2, I2), (3, I3))],
                     float(np.max(np.abs(dF))/np.max(np.abs(F)))*lam))
        G = lam*env
        rows[-1] = rows[-1] + (float(np.max(np.abs(cumint(G))))/lam**2,)
    for lam, rat, dcost, ctl in rows:
        print(f"     lam = {lam:.5f}: sup|I_j|/lam^(j+1) = {[round(x, 4) for x in rat]}, lam sup|F'|/sup|F| = "
              f"{dcost:.4f}, control sup|int lam env|/lam^2 = {ctl:.2f}")
    allr = [x for row in rows for x in row[1]]
    growth = max(rows[-1][1][j]/rows[0][1][j] for j in range(3))
    check("U3a sup|I_j| <= C lam^(j+1): the ratios stay below 25 and do not grow from lam = 1/8 to 1/64",
          max(allr) < 25 and growth <= 1, f"largest {max(allr):.3f}, growth {growth:.3f}")
    check("U3b each d_v costs lam^-1: lam sup|F'|/sup|F| -> 1", all(abs(row[2] - 1) < 0.2 for row in rows[1:]))
    ctl = [row[3] for row in rows]
    check("U3c control: non-oscillating F = lam env: sup|I_1|/lam^2 doubles as lam halves",
          all(ctl[i + 1]/ctl[i] > 1.9 for i in range(len(ctl) - 1)), str([round(x, 2) for x in ctl]))


def main():
    for f in (z1, z2, z3, z4, z5, u1, u2, u3):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
