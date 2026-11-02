#!/usr/bin/env python3
"""admbox5.py -- GAUGEDECAY5.md Round 2: the 1-form wave operator Box at b_0 -- the inputs of the augmented resolvent
(III.H at Box), the horizon charge of the singular part, the l = 0 reduction, the failure of round 1's (AdmBox) as
stated, and the weight bookkeeping of the source.  Computed.

Background and class as in rwgauge5.py / hgauge5.py.  Two charts of five-dimensional Tangherlini:
  * the ingoing chart (v, r, th, phi1, phi2), g = -f dv^2 + 2 dv dr + r^2 gamma, f = 1 - s^2/r^2 (GEO of hgauge5);
  * near infinity (|x| >= 3 R_1) the outgoing chart of III.B (3.4), (3.6): g = eta + (mu/r^2)(dt - dr)^2 with
    t = T + psi(r), psi' = 1 - 8 mu/r^2, T := t_*; the first coordinate symbol of rwgauge5 (named v) is reused for T.
Box := Theta(L_X g) (III.D (1.1)); hat P(sigma) U := e^{i sigma T} Box(e^{-i sigma T} U) = L0 U - i sigma L1 U
- sigma^2 L2 U on stationary U (III.H section 1).

  B1 (exact) Structure at infinity.  In the outgoing chart Box W* = 0, L1 W* = O(r^-3), L2 W* = O(r^-4), L0(r W*) =
     O(r^-3) and L2 = -g^{TT} = O(r^-2): the column hat f_*(0) = L1 W* + L0 w, w = -kappa(r) W*, kappa = kappa_0 r -
     kappa_1, lies in A^3 (III.H Lemma 2.3 at Box).  Control: in the static time (T = t) L2 W* is only O(r^-2).
  B2 (exact) The cone source.  For chi a function of r/T (homogeneous of degree 0; chi = (r/T)^2 and exp(r/T)),
     [Box, chi] W* = O(r^-4) uniformly on the cone {2r <= T <= 4r} (III.H Lemma 2.2 (b) at Box, weight 2 as the mass
     state).  Control: for the non-decaying Killing form (d_T)^flat it is not O(r^-3).
  B3 (exact) The Schur number at the horizon.  In the ingoing chart: ell(Box u) = 0 for stationary l = 0 u with general
     coefficients (III.D' Lemma 2.1 (1)); ell([Box, v + F(r)] W*) = 4 pi^2 for every F (any t_* with t_* - v a function
     of r near r_h); so ell(hat f_*(0)) = 4 pi^2 for every kappa.  Control: the stationary column L0(kappa W*) has
     ell = 0, so an augmentation by it is not invertible at zero energy.
  B4 (exact) The charge of the singular part.  For beta(v, r), Q[beta W*] = 4 pi^2 (beta - r_h d_r beta) at r_h.
     Control: without the d_r beta term the identity fails.
  B5 (exact) l = 0.  For Y = a dv + b dr (functions of v, r), with phi := delta Y and q := r^3 (dY)_{vr}:
         (Box Y)_v = d_v phi + r^-3 (d_v q + f d_r q),   (Box Y)_r = d_r phi - r^-3 d_r q,
     so Box Y = 0 iff d_r q = r^3 d_r phi, d_v q = -r^3 (d_v phi + f d_r phi), whose integrability is Box_0 phi = 0;
     Q[Y] = 2 pi^2 (r_h^3 phi + q)|_{r_h}.  The stationary solutions: W* (phi, q) = (0, 2), (d_v)^flat (0, 2 mu), and
     d psi, psi = v + F, F' = -(r^2 + r r_h + r_h^2)/(r (r + r_h)), Box_0 psi = 0, (0, 0); d psi = mu W* - (d_v)^flat.
     Control: q with r^2 in place of r^3 does not reduce the equation.
  B6 (exact) Round 1's (AdmBox) is false as stated.  phi_2 := (r^2 - mu/2) P_1(cos 2 th) and phi_4 := (r^4 - mu r^2 +
     mu^2/6) P_2(cos 2 th) (solved for) satisfy Box_0 phi = 0, are smooth at the horizon and G-invariant; Z := d phi has
     Box Z = 0, Q[Z] = 0, and L_Z g = 2 nabla d phi != 0 is stationary with l >= 2 angular dependence: a homogeneous,
     G-invariant solution that is not c W* + c' (d_t)^flat + o(1).  Control: r^2 P_1 (the mass term dropped) is not a
     solution.
  B7 (exact) Weights.  For a conormal source supported in the cone {1 <= r <= T/2} with |f| ~ r^-a (r/T)^b, the
     H^{0,(beta,0)}_{3b} norm (density dT dx, rho_sf = 1/r, rho_K = r/(T + r)) is finite iff b > 1/2 and a > beta +
     5/2.  Control: a = beta + 5/2 diverges.
  B8 (exact) The gauge.  The linearisation of Upsilon^0(g + eps k, g) (III.B (6.3)) at eps = 0 is -Theta(k) for
     every class tensor k on Tangherlini.  Control: without the -g^{-1} k Gamma term of dGamma it fails.

Labels: computed (exact, sympy).  Run: python3 checks/admbox5.py   (several minutes)
"""
import sys

import sympy as sp

from rwgauge5 import Geo, N, X, gam, legendre_S, mu, r, s, sqg, th, v, zero
from hgauge5 import GEO, S3, WSTAR, box, charge_density, delta1, dform, theta

T = v                                                            # the coordinate symbol, read as t_* in B1-B2
sig = sp.Symbol("sigma")


class GeoM(Geo):
    """a general metric matrix in the coordinates X of rwgauge5"""

    def __init__(self, gmat):
        self.f = None
        self.g = gmat
        self.gi = sp.simplify(gmat.inv())
        g, gi = gmat, self.gi
        self.Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                - sp.diff(g[b, c], X[d])) for d in range(N))/2)
                      for c in range(N)] for b in range(N)] for a in range(N)]


def outgoing_geo(static=False):
    """g = eta + (mu/r^2)(dt - dr)^2 in (T, r, th, phi1, phi2), t = T + psi(r) (or t = T if static)"""
    p = 0 if static else 1 - 8*mu/r**2                           # dt = dT + p dr
    q = p - 1                                                    # dt - dr = dT + q dr
    g = sp.zeros(5)
    g[0, 0] = -1 + mu/r**2
    g[0, 1] = g[1, 0] = -p + mu*q/r**2
    g[1, 1] = -p**2 + 1 + mu*q**2/r**2
    g[2, 2] = r**2
    g[3, 3] = r**2*sp.cos(th)**2
    g[4, 4] = r**2*sp.sin(th)**2
    return GeoM(g), p


def wstar_out(p):
    """W* = dv/r^2 - dr/(r (r + s)), dv = dt + (r^2 + mu)/(r^2 - mu) dr, dt = dT + p dr"""
    return [1/r**2, (p + (r**2 + mu)/(r**2 - mu))/r**2 - 1/(r*(r + s)), 0, 0, 0]


def lparts(G, U):
    """(L0 U, L1 U, L2 U) for stationary U: e^{i sig T} Box(e^{-i sig T} U) = L0 U - i sig L1 U - sig^2 L2 U"""
    E = sp.exp(-sp.I*sig*T)
    b = box(G, [E*c for c in U])
    out = [[], [], []]
    for comp in b:
        e = sp.expand(sp.powsimp(sp.expand(comp/E)))
        out[0].append(sp.simplify(e.coeff(sig, 0)))
        out[1].append(sp.simplify(sp.I*e.coeff(sig, 1)))
        out[2].append(sp.simplify(-e.coeff(sig, 2)))
    return out


def order_at_infinity(expr, k):
    """r^k expr has a finite limit as r -> oo"""
    lim = sp.limit(sp.simplify(r**k*expr), r, sp.oo)
    return lim.is_finite, lim


# --------------------------------------------------------------------------------------------------------------- B1
def b1(control=False):
    G, p = outgoing_geo(static=control)
    W = wstar_out(p)
    if control:
        L = lparts(G, W)
        fin, lim = order_at_infinity(L[2][0], 4)
        fin2, lim2 = order_at_infinity(L[2][0], 2)
        print("  B1 control (static time T = t): r^4 (L2 W*)_T -> %s (finite: %s); r^2 (L2 W*)_T -> %s"
              % (lim, fin, lim2), flush=True)
        return bool(fin)
    kern = all(zero(e) for e in box(G, W))
    L = lparts(G, W)
    Lw = lparts(G, [r*c for c in W])
    res = {}
    ok = kern
    for name, comps, k in (("L1 W*", L[1], 3), ("L2 W*", L[2], 4), ("L0 (r W*)", Lw[0], 3)):
        lims = [order_at_infinity(c, k) for c in comps[:2]]
        res[name] = [x[1] for x in lims]
        ok &= all(x[0] for x in lims) and all(zero(c) for c in comps[2:])
    g00 = sp.simplify(G.gi[0, 0])
    fin00, lim00 = order_at_infinity(g00, 2)
    ok &= bool(fin00) and lim00 != 0
    ok &= all(zero(c) for c in L[0])
    print("  B1: Box W* = 0 in the outgoing chart: %s; L0 W* = 0: %s; r^3 L1 W* -> %s; r^4 L2 W* -> %s; r^3 L0(r W*) -> "
          "%s; r^2 g^{TT} -> %s" % (kern, all(zero(c) for c in L[0]), res["L1 W*"], res["L2 W*"], res["L0 (r W*)"],
                                     lim00), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B2
def b2(control=False):
    G, p = outgoing_geo()
    qv = sp.Symbol("q", positive=True)                           # q = r/T on the cone, in [1/4, 1/2]
    state = [-G.g[0, 0]*(-1), 0, 0, 0, 0]                        # placeholder, replaced below
    if control:
        state = [G.g[0, 0], G.g[0, 1], 0, 0, 0]                   # (d_T)^flat, d_T Killing
    else:
        state = wstar_out(p)
    ok = True
    lims = []
    for chi in (lambda z: z**2, sp.exp):
        c = chi(r/T)
        comm = [sp.simplify(b1_ - c*b0) for b1_, b0 in zip(box(G, [c*e for e in state]), box(G, state))]
        for comp in comm[:3]:
            e = sp.simplify(comp.subs(T, r/qv))
            k = 3 if control else 4
            lim = sp.limit(r**k*e, r, sp.oo)
            lims.append(lim)
            ok &= bool(lim.is_finite)
            if not control:
                ok &= sp.limit(r**3*e, r, sp.oo) == 0
    if control:
        print("  B2 control ((d_T)^flat, Killing, weight 0): r^3 [Box, chi] state -> %s: O(r^-3): %s" % (lims, ok),
              flush=True)
        return ok
    print("  B2: [Box, chi(r/T)] W* on the cone T = r/q, chi = z^2, exp(z): r^4 x components -> %s (finite), r^3 x -> 0:"
          " %s" % (lims, ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B3
def ell(comp_v):
    return sp.simplify(S3*s**3*comp_v.subs(r, s).doit())


def b3(control=False):
    a, b, kap, F = [sp.Function(n)(r) for n in ("a", "b", "kappa", "F")]
    if control:
        col = box(GEO, [kap*WSTAR[0], kap*WSTAR[1], 0, 0, 0])
        val = ell(col[0])
        print("  B3 control: ell of the stationary column L0(kappa W*) = %s; nonzero: %s" % (val, not zero(val)),
              flush=True)
        return not zero(val)
    u = [a, b, 0, 0, 0]
    bu = box(GEO, u)
    sta = zero(bu[0].subs(r, s).doit())
    sta2 = not zero(bu[0].subs(r, 2*s).doit())
    tstar = v + F
    comm = [sp.simplify(e1 - tstar*e0) for e1, e0 in zip(box(GEO, [tstar*w for w in WSTAR]), box(GEO, WSTAR))]
    l1 = ell(comm[0])
    col = [comm[i] + box(GEO, [-kap*WSTAR[0], -kap*WSTAR[1], 0, 0, 0])[i] for i in range(2)]
    l2 = ell(col[0])
    ok = sta and sta2 and zero(l1 - 4*sp.pi**2) and zero(l2 - 4*sp.pi**2)
    print("  B3: ell(Box u) = 0 for stationary l = 0 u: %s (not at r = 2 r_h: %s); ell([Box, v + F(r)] W*) = %s; "
          "ell(L1 W* + L0(-kappa W*)) = %s" % (sta, sta2, l1, l2), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B4
def b4(control=False):
    be = sp.Function("beta")(v, r)
    cd = charge_density(GEO, [be*WSTAR[0], be*WSTAR[1], 0, 0, 0])
    target = 2*be - (0 if control else 2*r*sp.diff(be, r))
    ok = zero(sp.expand((cd - target).subs(r, s).doit()))
    print("  B4%s: r^3 (delta + d_vr)(beta W*) = 2 beta%s at r_h, so Q[beta W*] = 4 pi^2 (beta%s): %s"
          % (" control" if control else "", "" if control else " - 2 r d_r beta", "" if control else
             " - r_h d_r beta", ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B5
def b5(control=False):
    f = 1 - mu/r**2
    a, b = [sp.Function(n)(v, r) for n in ("a", "b")]
    Y = [a, b, 0, 0, 0]
    phi = delta1(GEO, Y)
    pw = 2 if control else 3
    q = r**pw*dform(Y)[0][1]
    bY = box(GEO, Y)
    e1 = bY[0] - (sp.diff(phi, v) + (sp.diff(q, v) + f*sp.diff(q, r))/r**3)
    e2 = bY[1] - (sp.diff(phi, r) - sp.diff(q, r)/r**3)
    ok = zero(e1) and zero(e2) and all(zero(e) for e in bY[2:])
    if control:
        print("  B5 control (q = r^2 (dY)_vr): the reduction holds: %s" % ok, flush=True)
        return ok
    integ = sp.simplify(sp.diff(r**3*sp.diff(phi, r), v) + sp.diff(r**3*(sp.diff(phi, v) + f*sp.diff(phi, r)), r))
    box0 = sp.simplify(-r**3*sp.diff(phi, v, r)*0 + delta1(GEO, [sp.diff(phi, x) for x in X]))
    integ_ok = zero(integ - (-r**3)*box0) or zero(integ + (-r**3)*box0)
    Fp = -(r**2 + r*s + s**2)/(r*(r + s))
    table = []
    for name, w in (("W*", WSTAR), ("(d_v)^flat", [-f, 1, 0, 0, 0]), ("d psi", [1, Fp, 0, 0, 0])):
        table.append((name, all(zero(e) for e in box(GEO, w)), sp.simplify(delta1(GEO, w)),
                      sp.simplify(r**3*dform(w)[0][1])))
    psi_ok = zero(delta1(GEO, [1, Fp, 0, 0, 0])) and all(zero([1, Fp][i] - (mu*WSTAR[i] - [-f, 1][i]))
                                                         for i in range(2))
    ok &= integ_ok and psi_ok and all(t[1] for t in table)
    ok &= [(t[2], sp.simplify(t[3])) for t in table] == [(0, 2), (0, 2*s**2), (0, 0)]
    print("  B5: (Box Y)_v = d_v phi + r^-3 (d_v q + f d_r q), (Box Y)_r = d_r phi - r^-3 d_r q: True; integrability "
          "of q is r^3 Box_0 phi (up to sign): %s; stationary (Box = 0, phi, q): %s; d psi = mu W* - (d_v)^flat, "
          "Box_0 psi = 0: %s" % (integ_ok, table, psi_ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B6
def scalar_box(G, ph):
    return delta1(G, [sp.diff(ph, x) for x in X])


def b6(control=False):
    if control:
        ph = r**2*legendre_S(1)
        ok = zero(scalar_box(GEO, ph))
        print("  B6 control: r^2 P_1(cos 2th) solves Box_0 phi = 0: %s" % ok, flush=True)
        return ok
    a1, a0 = sp.symbols("a1 a0")
    trial = (r**4 + a1*mu*r**2 + a0*mu**2)*legendre_S(2)
    eqs = sp.Poly(sp.expand(sp.simplify(scalar_box(GEO, trial)/legendre_S(2))*r**2), r).coeffs()
    sol = sp.solve(eqs, [a1, a0], dict=True)
    phi4 = trial.subs(sol[0]) if sol else None
    ok = bool(sol) and sol[0] == {a1: -1, a0: sp.Rational(1, 6)}
    rows = []
    for name, ph in (("phi_2", (r**2 - mu/2)*legendre_S(1)), ("phi_4", phi4)):
        Z = [sp.diff(ph, x) for x in X]
        b0 = zero(scalar_box(GEO, ph))
        bz = all(zero(e) for e in box(GEO, Z))
        L = GEO.lie(Z)
        nz = any(not zero(e) for row in L for e in row)
        angular = any(not zero(sp.diff(e, th)) for row in L for e in row)
        stat = all(zero(sp.diff(e, v)) for row in L for e in row)
        qz = zero(sp.integrate(sp.expand(charge_density(GEO, Z).subs(r, s)*sqg), (th, 0, sp.pi/2)))
        grows = sp.limit(sp.diff(ph, r).subs(th, 0)/r, r, sp.oo)
        rows.append((name, b0, bz, nz, angular, stat, qz, grows))
        ok &= b0 and bz and nz and angular and stat and qz
    print("  B6: phi_4 coefficients solved: %s; (name, Box_0 phi = 0, Box d phi = 0, L_{d phi} g != 0, theta-dependent,"
          " stationary, Q = 0, lim d_r phi/r at th = 0): %s" % (sol, rows), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B7
def b7(control=False):
    tt, rr = sp.symbols("t rr", positive=True)
    cases = [(sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2) + sp.Rational(1, 4) + sp.Rational(5, 2)
              + sp.Rational(1, 10))]
    if control:
        cases = [(sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 4) + sp.Rational(5, 2))]
    ok = True
    vals = []
    for beta, bK, aI in cases:
        integrand = rr**(2*beta)*rr**(-2*aI)*(rr/tt)**(2*bK)*rr**3
        inner = sp.integrate(integrand, (tt, 2*rr, sp.oo))
        outer = sp.integrate(sp.simplify(inner), (rr, 1, sp.oo))
        vals.append(outer)
        ok &= bool(outer.is_finite)
    exp_ = sp.Symbol("e")
    a_, b_, be_ = sp.symbols("a b beta", positive=True)
    rexp = sp.simplify(2*be_ - 2*a_ + 2*b_ + 3 + (1 - 2*b_))     # r-exponent after the T-integral
    print("  B7%s: weighted norms of r^-a (r/T)^b on the cone: %s (finite: %s); the r-exponent after the T-integral is "
          "%s, integrable iff a > beta + 5/2" % (" control (a = beta + 5/2)" if control else "", vals, ok, rexp),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- B8
def b8(control=False):
    names = ("kvv", "kvr", "krr", "kvt", "krt", "ktt", "k11", "k22")
    kvv, kvr, krr, kvt, krt, ktt, k11, k22 = [sp.Function(n)(v, r, th) for n in names]
    k = [[kvv, kvr, kvt, 0, 0], [kvr, krr, krt, 0, 0], [kvt, krt, ktt, 0, 0], [0, 0, 0, k11, 0], [0, 0, 0, 0, k22]]
    g, gi, Gm = GEO.g, GEO.gi, GEO.Gam

    def dGam(nu, ka, la):
        e = sum(gi[nu, rho]*(sp.diff(k[rho][la], X[ka]) + sp.diff(k[rho][ka], X[la]) - sp.diff(k[ka][la], X[rho]))
                for rho in range(N))/2
        if not control:
            e -= sum(gi[nu, rho]*k[rho][si]*Gm[si][ka][la] for rho in range(N) for si in range(N))
        return e
    dG = [[[dGam(nu, ka, la) for la in range(N)] for ka in range(N)] for nu in range(N)]
    ups = [sum(g[m, nu]*gi[ka, la]*dG[nu][ka][la] for nu in range(N) for ka in range(N) for la in range(N)
               if gi[ka, la] != 0 and g[m, nu] != 0) for m in range(N)]
    th_ = theta(GEO, k)
    ok = all(zero(ups[m] + th_[m]) for m in range(N))
    print("  B8%s: d/d eps Upsilon^0(g + eps k, g)|_0 = -Theta(k) for a general class tensor: %s"
          % (" control (dGamma without -g^-1 k Gamma)" if control else "", ok), flush=True)
    return ok


CHECKS = [("B1", b1), ("B2", b2), ("B3", b3), ("B4", b4), ("B5", b5), ("B6", b6), ("B7", b7), ("B8", b8)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
