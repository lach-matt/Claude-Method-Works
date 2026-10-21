#!/usr/bin/env python3
"""growing5.py -- the growing source: [Hun19] section 4.2 in five dimensions (N1STAR-PROOF.md section 10.7; D50).  The
gauge vector X of a scalar mode l >= 2 in the class solves box X = J := -Gamma[h_RW] (Proposition 10.2(iii)); this
instrument computes J in the master field of [KI03], the direct system for (X_t, X_1, X_L) in Hung's form, the rung
sources with their weights in r, and the substitutions that remove the bad weights.  Labels: computed (exact, sympy),
READ.

Conventions.  g = -f dt^2 + dr^2/f + r^2 gamma_{S^3}, f = 1 - mu/r^2; a scalar harmonic S(th) with S'' = -2 cot 2th S' -
k^2 S, k^2 = l(l + 2); h_RW = F_ab S dy^a dy^b + 2 r^2 F S gamma_ij dz^i dz^j; X = X_t S dt + X_r S dr + X_L r S_i dz^i,
S_i = -k^-1 D_i S, X_1 := f X_r (Hung's W_1).  [KI03] at n = 3, K = 1, lambda = 0: x = mu/r^2 (their 2M = mu), m = k^2 -
3, H = m + 6x; the master field Phi solves box_2 Phi = (V_S/f) Phi on the orbit space, V_S = f Q/(16 r^2 H^2), Q = 1296
x^3 + (624 m - 144) x^2 + (36 m^2 - 432 m) x + 16 m^3 + 60 m^2 ((3.5)-(3.7)); Psi := r^(3/2) H Phi ((3.13)); r F =
(1/(12 r^2 H))[(2H - 3 r f') Psi + 6 r Dr.DPsi] and r F_ab + r F g_ab = (1/H)(D_a D_b Psi - (1/2) box_2 Psi g_ab)
((3.14), (10.1) here).  phi := Psi/(r^3 H) = r^(-3/2) Phi is the scalar-wave normalisation (his r^-1 psi_Z).  Sigma :=
tr h, with box Sigma = 0 in harmonic gauge; S = div X = (Sigma - 4F)/2.  u := t - r_* + const.

  G1 (computed, exact; READ check) The transcription of [KI03]: F^a_a = -2F ((2.11)); the Einstein equations E_a = 0,
     D^b(r F_ab) - 2 D_a(r F) = 0 ((2.12)), hold modulo the master equation, checked at three rational (mu, k) and three
     radii; and at n = 2 the same transcription of (3.7) is the Zerilli potential, Q = 128 lam^2 (lam + 1) + 192 lam^2 x
     + 288 lam x^2 + 144 x^3 with m = 2 lam.  Control: the master equation with V_S's sign reversed.
  G2 (computed, exact) J = -Gamma[h_RW] in h_RW's components, theta-free after division by S and r S_th (10.28), and
     tr h_RW = F^a_a + 6F = 4F by G1.  Control: a vector-type angular part.
  G3 (computed, exact) The direct system (10.29): box_l X_t + (2 mu/r^3)(d_t X_r - d_r X_t) = J_t; box_l X_1 - (3/r^2)(1
     - 3 mu/r^2) X_1 - (2k/r^2)(1 - 2 mu/r^2) X_L = (2 mu/r^3) S + f J_r; box_l X_L + (1/r^2)(1 + mu/r^2) X_L - (2k/r^2)
     X_1 = J_L -- [Hun19] (4.21)-(4.23) in five dimensions, d_t X_t eliminated through S = div X.  Control: the sign of
     the X_1-X_L coupling reversed.

  G4 (computed, exact at (k^2, mu) = (8, 2/3), (24, 5/4), (48, 3/2)) The rung sources in Hung's canonical form -- d_r^2
     eliminated by the wave equations, Psi = r^3 H phi (phi = r^(-3/2) Phi_KI the scalar-wave normalisation, box_l phi =
     V_phi phi with V_phi = -12 mu (k^2 + 3)((k^2 - 3) r^2 + 2 mu)/(r^6 H^2)) -- are (10.31): tr h_RW = 4F = 2 r f d_r
     phi + c_F phi; G_P := r dJ_tr + d_t Sigma - d_t(4F) - 2 J_t = 4 r f d_t d_r phi + c_2 d_t phi + d_t Sigma; J_t =
     -2 r f d_t d_r phi + c_t d_t phi; f J_r = -2 r d_t^2 phi + 2 mu f ((m + 12) r^2 - 6 mu)/(r^4 H) d_r phi - r f V_phi
     phi; J_L = 0 (every other term cancels modulo the master equation), with m = k^2 - 3, c_F = (12 mu + (2/3) m (k^2 +
     6) r^2)/(r^2 H), c_2 = 2 c_F, c_t = -2 (3 m r^4 - (4m - 6) mu r^2 - 12 mu^2)/(r^4 H): Hung's (4.21)-(4.25) in five
     dimensions, the bad terms O(r) d_t d_r phi, O(1) d_t phi, d_t Sigma and O(r) d_t^2 phi.  Control: the sign of 2 J_t
     in G_P.
  G5 (computed, exact at the four sample points) The substitutions (10.32), Hung's (4.27)-(4.30): r P-bar = r P -
     r^2 d_t phi + (u + r)((2 k^2/3) phi + Sigma/2), X_t-bar = X_t + (r^2/2) d_t phi - (u + r) phi, X_1-bar = X_1 +
     (r^2 f/2) d_r phi + (m r^4 + 6 mu^2)/(r^3 H) phi, X_L-bar = X_L + (k r/2) phi, with u + r carried as an abstract
     function (d_t(u + r) = 1, d_r(u + r) = 1 - 1/f).  The barred rungs' sources, modulo the wave equations of phi and
     Sigma, carry no d_t d_r phi and no d_t^2 phi, and every coefficient is O(r^-2) or better, the (u + r)-weighted ones
     O(r^-4): (10.33), his (4.31)-(4.34).  Control: the (u + r) phi coefficient of r P-bar halved, which leaves an O(1)
     d_t phi.

READ (alphaXiv, 2026-10-21).  [KI03] H. Kodama, A. Ishibashi, A master equation for gravitational perturbations of
maximally symmetric black holes in higher dimensions, hep-th/0305147v3: sections 2-3 ((2.4)-(2.8), (2.11)-(2.13),
(2.20)-(2.21), (3.1)-(3.7), (3.9)-(3.14)), section 6 (6.1), Appendix A ((A.1b)).  [Hun19] section 4.2 pp. 26-32
((4.10)-(4.42), Lemmas 4.8-4.10), section 5 (Propositions 5.1-5.9, Lemma 5.5), section 6 (6.1)-(6.11).

sympy.  python3 growing5.py [--selftest | --mutants]   (about twelve minutes; --verbose lists every sub-check)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wavegauge5 as WG                                       # the metric, Christoffels, box on one-forms, Gamma[h]

t, r, th, mu, kk, f, N = WG.t, WG.r, WG.th, WG.mu, WG.kk, WG.f, WG.N
D = sp.diff
fp = D(f, r)
x = mu/r**2
m = kk**2 - 3
H = m + 6*x
Q = 1296*x**3 + (624*m - 144)*x**2 + (36*m**2 - 432*m)*x + 16*m**3 + 60*m**2
V_S = f*Q/(16*r**2*H**2)
Psi = sp.Function("Psi")(t, r)
S = sp.Function("S")(th)
Sp = D(S, th)
S0, S1 = sp.symbols("S0 S1")
ANG = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13))]
PTS = [{mu: sp.Rational(2, 3), kk: sp.sqrt(8)}, {mu: sp.Rational(5, 4), kk: sp.sqrt(24)},
       {mu: sp.Rational(3, 2), kk: sp.sqrt(48)}]
RPTS = [sp.Rational(9, 4), sp.Rational(17, 5), sp.Rational(7, 2)]


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


# ---------------------------------------------------------------------------------------------- the orbit space
gq = sp.diag(-f, 1/f)
gqi = gq.inv()
Y2 = [t, r]
G2 = [[[sp.simplify(sum(gqi[a, d]*(D(gq[d, b], Y2[c]) + D(gq[d, c], Y2[b]) - D(gq[b, c], Y2[d])) for d in range(2))/2)
        for c in range(2)] for b in range(2)] for a in range(2)]


def DD(phi, a, b):
    return D(phi, Y2[a], Y2[b]) - sum(G2[c][a][b]*D(phi, Y2[c]) for c in range(2))


def box2(phi):
    return sum(gqi[a, b]*DD(phi, a, b) for a in range(2) for b in range(2))


def reconstruction():
    """F and F_ab from Psi by (10.1) ([KI03] (3.14) at n = 3)"""
    DrDPsi = sum(gqi[a, b]*D(r, Y2[a])*D(Psi, Y2[b]) for a in range(2) for b in range(2))
    F = ((2*H - 3*r*fp)*Psi + 6*r*DrDPsi)/(12*r**3*H)
    Fab = sp.Matrix(2, 2, lambda a, b: (DD(Psi, a, b) - box2(Psi)*gq[a, b]/2)/(r*H) - F*gq[a, b])
    return F, Fab


def master_tt(sign=1):
    """Psi_tt from the master equation, rational in r (Phi = Psi/(r^(3/2) H))"""
    PhiKI = Psi/(r**sp.Rational(3, 2)*H)
    me = sp.expand(sp.simplify((box2(PhiKI) - sign*V_S/f*PhiKI)*r**sp.Rational(3, 2)*H))
    return sp.expand(sp.cancel(sp.solve(me, D(Psi, t, 2))[0]))


def reduce_tt(e, mtt):
    """replace every d_t^2 (d_t^a d_r^b) Psi by the master equation"""
    e = sp.expand(e.doit())
    for _ in range(8):
        rep = {}
        for d in e.atoms(sp.Derivative):
            if d.expr == Psi and dict(d.variable_count).get(t, 0) >= 2:
                cnt = dict(d.variable_count)
                extra = [t]*(cnt[t] - 2) + [r]*cnt.get(r, 0)
                rep[d] = D(mtt, *extra) if extra else mtt
        if not rep:
            break
        e = sp.expand(e.xreplace(rep).doit())
    return e


def vanishes(e, mtt):
    """e, linear in Psi and its derivatives, is zero modulo the master equation at the sample points"""
    for pt in PTS:
        en = reduce_tt(e.subs(pt), sp.expand(mtt.subs(pt)))
        keys = sorted([d for d in en.atoms(sp.Derivative) if d.expr == Psi], key=str) + [Psi]
        for key in keys:
            c = sp.cancel(en.coeff(key))
            if any(sp.simplify(c.subs(r, rv)) != 0 for rv in RPTS):
                return False
    return True


# ---------------------------------------------------------------------------------------------- the harmonic
def red(e):
    """reduce every d_th^n S (n >= 2) by the harmonic ODE"""
    e = sp.expand(e.doit())
    for _ in range(8):
        ders = [d for d in e.atoms(sp.Derivative) if d.expr == S and d.variable_count[0][1] >= 2]
        if not ders:
            break
        e = sp.expand(e.xreplace({d: D(-2*sp.cot(2*th)*Sp - kk**2*S, th, d.variable_count[0][1] - 2)
                                  for d in ders}).doit())
    return e


def at_angle(q, c, s_):
    """the angle evaluated exactly at cos th = c, sin th = s_, with S -> S0 and S' -> S1"""
    q = q.xreplace({Sp: S1}).xreplace({S: S0})
    tab = {sp.cos: lambda a: c if a == th else (c**2 - s_**2 if a == 2*th else sp.cos(a)),
           sp.sin: lambda a: s_ if a == th else (2*c*s_ if a == 2*th else sp.sin(a)),
           sp.tan: lambda a: s_/c if a == th else (2*c*s_/(c**2 - s_**2) if a == 2*th else sp.tan(a)),
           sp.cot: lambda a: c/s_ if a == th else ((c**2 - s_**2)/(2*c*s_) if a == 2*th else sp.cot(a))}
    q = q.replace(lambda e: isinstance(e, (sp.cos, sp.sin, sp.tan, sp.cot)), lambda e: tab[type(e)](e.args[0]))
    return sp.expand(sp.cancel(q))


def lin_coeffs(e, basis, funcs):
    """e linear in funcs and their derivatives; {derivative or function: theta-free coefficient / basis}, or None"""
    e = sp.expand(e)
    ders = sorted([d for d in e.atoms(sp.Derivative) if d.expr in funcs], key=str)
    syms = {d: sp.Symbol("D%d" % i) for i, d in enumerate(ders)}
    syms.update({fn: sp.Symbol("F%d" % i) for i, fn in enumerate(funcs)})
    lin = sp.expand(e.xreplace(syms))
    if sp.expand(lin - sum(lin.coeff(sym)*sym for sym in syms.values())) != 0:
        return None
    out = {}
    for key, sym in syms.items():
        c = lin.coeff(sym)
        if c == 0:
            continue
        ca = [sp.cancel(at_angle(sp.expand(c/basis), *a)) for a in ANG]
        if sp.simplify(ca[0] - ca[1]) != 0 or ca[0].has(S0) or ca[0].has(S1):
            return None
        out[key] = sp.factor(ca[0])
    return out


Ftt, Ftr, Frr, Fs = [sp.Function(nm)(t, r) for nm in ("Ftt", "Ftr", "Frr", "F")]
FUNCS = (Ftt, Ftr, Frr, Fs)


def gauge_source(control=0):
    """J_t, J_r, J_L = -Gamma[h_RW] divided by S, S, -r S'/k, in the abstract components (G2)"""
    gam = sp.diag(1, sp.cos(th)**2, sp.sin(th)**2)
    h = sp.zeros(N)
    h[0, 0] = Ftt*S
    h[0, 1] = h[1, 0] = Ftr*S
    h[1, 1] = Frr*S
    for i in range(3):
        h[2 + i, 2 + i] = 2*r**2*Fs*S*gam[i, i]
    G = WG.gamma_of(h, simp=False)
    out = {}
    for name, idx, basis in (("t", 0, S), ("r", 1, S), ("L", 2, -r*Sp/kk)):
        if control == 1 and name == "L":
            idx, basis = 3, r*sp.cos(th)**2*sp.sin(th)        # a vector-type angular part: not of this form
        co = lin_coeffs(red(-G[idx]), basis, FUNCS)
        out[name] = None if co is None else sum(c*key for key, c in co.items())
    trh = sum(WG.gi[a, b]*h[a, b] for a in range(N) for b in range(N))
    return out, sp.simplify(trh/S)


# ---------------------------------------------------------------------------------------------- the checks
def g1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    F, Fab = reconstruction()
    mtt = master_tt(-1 if control == 1 else 1)
    chk("F^a_a = -2F ([KI03] (2.11))", vanishes(sum(gqi[a, b]*Fab[a, b] for a in range(2) for b in range(2)) + 2*F, mtt))

    def Db_upper(Tab, a):
        return sum(gqi[b, c]*(D(Tab[c, a], Y2[b]) - sum(G2[d][b][c]*Tab[d, a] + G2[d][b][a]*Tab[c, d]
                                                       for d in range(2))) for b in range(2) for c in range(2))
    Ft = r*Fab
    chk("the Einstein equations E_a = 0: D^b(r F_ab) - 2 D_a(r F) = 0 modulo the master equation ([KI03] (2.12))",
        all(vanishes(Db_upper(Ft, a) - 2*D(r*F, Y2[a]), mtt) for a in range(2)))
    n, K, lam, xx = sp.symbols("n K lambda x")
    mm = kk**2 - n*K
    Qn = (n**4*(n + 1)**2*xx**3 + n*(n + 1)*(4*(2*n**2 - 3*n + 4)*mm + n*(n - 2)*(n - 4)*(n + 1)*K)*xx**2
          - 12*n*((n - 4)*mm + n*(n + 1)*(n - 2)*K)*mm*xx + 16*mm**3 + 4*K*n*(n + 2)*mm**2)
    Q3 = sp.expand(Qn.subs({n: 3, K: 1}).subs(xx, x))
    Q2 = sp.expand(Qn.subs({n: 2, K: 1}).subs(kk**2, 2*lam + 2))
    chk("(3.7) at lambda = 0 reads at n = 3 as (10.27) and at n = 2 as the Zerilli potential's numerator",
        sp.expand(Q3 - Q) == 0
        and sp.expand(Q2 - (128*lam**2*(lam + 1) + 192*lam**2*xx + 288*lam*xx**2 + 144*xx**3)) == 0)
    return chk.ok


def g2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    J, trh = gauge_source(control)
    want = {"t": 3*D(Fs, t) + f/2*D(Frr, t) - f*D(Ftr, r) + D(Ftt, t)/(2*f) - (3*r**2 - mu)/r**3*Ftr,
            "r": 3*D(Fs, r) - f/2*D(Frr, r) + D(Ftr, t)/f - D(Ftt, r)/(2*f) - (3*r**2 - mu)/r**3*Frr + 6/r*Fs,
            "L": kk/(2*r*f)*Ftt - kk*f/(2*r)*Frr - kk/r*Fs}
    chk("J_t, J_r, J_L are theta-free after division by S, S, r S_th and are (10.28)",
        all(J[nm] is not None and sp.simplify(J[nm] - want[nm]) == 0 for nm in ("t", "r", "L")))
    chk("tr h_RW = F^a_a + 6F, which is 4F by G1's trace identity",
        sp.simplify(trh - (-Ftt/f + f*Frr + 6*Fs)) == 0)
    return chk.ok


def g3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Xt, Xr, XL, X1, Sdiv = [sp.Function(nm)(t, r) for nm in ("Xt", "Xr", "XL", "X1", "Sdiv")]
    bX = WG.box1([Xt*S, Xr*S, -r*XL*Sp/kk, 0, 0], simp=False)
    OP = {}
    for name, idx, basis in (("t", 0, S), ("r", 1, S), ("L", 2, -r*Sp/kk)):
        co = lin_coeffs(red(bX[idx]), basis, (Xt, Xr, XL))
        OP[name] = None if co is None else sum(c*key for key, c in co.items())
    boxl = lambda u: -D(u, t, 2)/f + f*D(u, r, 2) + (3*r**2 - mu)/r**3*D(u, r) - kk**2/r**2*u
    ok = all(OP[nm] is not None for nm in OP)
    chk("(box X)_t = box_l X_t + (2 mu/r^3)(d_t X_r - d_r X_t)",
        ok and sp.simplify(OP["t"] - (boxl(Xt) + 2*mu/r**3*(D(Xr, t) - D(Xt, r)))) == 0)
    sgn = -1 if control == 1 else 1
    dtXt = f*(-Sdiv + D(r**3*f*Xr, r)/r**3 + kk/r*XL)         # from S = div X
    er = sp.expand((f*OP["r"].xreplace({D(Xt, t): dtXt})).xreplace({Xr: X1/f}).doit()) if ok else None
    chk("f (box X)_r with d_t X_t -> S and X_1 = f X_r: box_l X_1 - (3/r^2)(1 - 3 mu/r^2) X_1 - (2k/r^2)(1 - 2 mu/r^2)"
        " X_L - (2 mu/r^3) S",
        ok and sp.simplify(er - (boxl(X1) - 3/r**2*(1 - 3*mu/r**2)*X1 - sgn*2*kk/r**2*(1 - 2*mu/r**2)*XL
                                 - 2*mu/r**3*Sdiv)) == 0)
    el = sp.expand(OP["L"].xreplace({Xr: X1/f}).doit()) if ok else None
    chk("(box X)_L with X_r = X_1/f: box_l X_L + (1/r^2)(1 + mu/r^2) X_L - (2k/r^2) X_1",
        ok and sp.simplify(el - (boxl(XL) + (1 + mu/r**2)/r**2*XL - sgn*2*kk/r**2*X1)) == 0)
    return chk.ok



# ---------------------------------------------------------------------------------------------- G4, G5: the sources
phi = sp.Function("phi")(t, r)                     # the scalar-wave normalisation, Psi = r^3 H phi
Sig = sp.Function("Sigma")(t, r)                   # tr h, box Sigma = 0
Uf = sp.Function("U")(t, r)                        # u + r as an abstract function: d_t U = 1, d_r U = 1 - 1/f
USYM = sp.Symbol("U")
SAMPLES = [(8, sp.Rational(2, 3)), (24, sp.Rational(5, 4)), (48, sp.Rational(3, 2)), (80, sp.Rational(7, 5))]  # k^2, mu


def boxl_k(u, K2):
    return -D(u, t, 2)/f + f*D(u, r, 2) + (3*r**2 - mu)/r**3*D(u, r) - K2/r**2*u


def v_phi(K2):
    """box_l phi = V_phi phi for phi = r^(-3/2) Phi_KI: the master potential read on phi, (10.30)"""
    mm = K2 - 3
    HH = mm + 6*mu/r**2
    return -12*mu*(K2 + 3)*(mm*r**2 + 2*mu)/(r**6*HH**2)


class Canon:
    """canonical forms at a sample point: d_r^2 eliminated by the wave equations of phi and Sigma; u + r resolved"""

    def __init__(self, K2, muv):
        self.K2, self.muv = K2, muv
        self.sub = {mu: muv}
        self.boxl = lambda u: boxl_k(u, K2).subs(self.sub)
        self.phi_rr = sp.expand(sp.solve(self.boxl(phi) - v_phi(K2).subs(self.sub)*phi, D(phi, r, 2))[0])
        self.Sig_rr = sp.expand(sp.solve(self.boxl(Sig), D(Sig, r, 2))[0])

    def resolve_U(self, e):
        e = sp.expand(e.doit())
        rep = {}
        for d in e.atoms(sp.Derivative):
            if d.expr == Uf:
                cnt = dict(d.variable_count)
                nt, nr = cnt.get(t, 0), cnt.get(r, 0)
                if nt >= 2 or (nt == 1 and nr >= 1):
                    rep[d] = 0
                elif nt == 1:
                    rep[d] = 1
                else:
                    rep[d] = D(1 - 1/f, r, nr - 1).subs(self.sub)
        return sp.expand(e.xreplace(rep).xreplace({Uf: USYM}))

    def reduce(self, e):
        e = self.resolve_U(e)
        for _ in range(12):
            rep = {}
            for d in e.atoms(sp.Derivative):
                if d.expr in (phi, Sig):
                    cnt = dict(d.variable_count)
                    nt, nr = cnt.get(t, 0), cnt.get(r, 0)
                    if nr >= 2:
                        base = self.phi_rr if d.expr == phi else self.Sig_rr
                        extra = [t]*nt + [r]*(nr - 2)
                        rep[d] = D(base, *extra) if extra else base
            if not rep:
                break
            e = sp.expand(e.xreplace(rep).doit())
        return e

    def coeffs(self, e):
        """{(U-power, derivative or function): coefficient}, cancelled"""
        e = self.reduce(e)
        out = {}
        for fn in (phi, Sig):
            keys = sorted([d for d in e.atoms(sp.Derivative) if d.expr == fn], key=str) + [fn]
            for key in keys:
                c = sp.expand(e.coeff(key))
                for pw in (0, 1, 2):
                    nu, de = _frac(c.coeff(USYM, pw))
                    if nu != 0:
                        out[(pw, key)] = nu/de
        return out


_DENS = {}


def _den_factors(de):
    """a term's denominator as {irreducible polynomial in r: exponent} with the multiplier that completes 1/de; the
    denominators the reduction leaves are products of r, f and H multiplied out, which sp.together does not see as
    common (cached)"""
    if de not in _DENS:
        const, poly = de.as_independent(r, as_Add=False)
        pn, pd = sp.fraction(sp.together(poly))                 # a Laurent polynomial in r: clear the negative powers
        co, fl = sp.factor_list(pn, r)
        facs = {}
        for base, ex in fl:
            facs[base] = facs.get(base, 0) + ex
        _DENS[de] = (pd/(const*co), facs)                        # 1/de = (pd/(const co)) / prod base^ex
    return _DENS[de]


def _frac(c):
    """c, a sum of rational functions of r, as one fraction over the factored common denominator, the numerator expanded;
    no gcd is taken (sp.cancel over the algebraic k took hours), since a common factor changes neither whether the
    numerator vanishes nor the difference of the degrees"""
    parts, dens = [], {}
    for term in sp.Add.make_args(sp.expand(c)):
        nu, de = sp.fraction(term)
        mult, facs = _den_factors(de)
        parts.append((nu*mult, facs))
        for base, ex in facs.items():
            dens[base] = max(dens.get(base, 0), ex)
    total = sum(nu*sp.Mul(*[base**(dens[base] - facs.get(base, 0)) for base in dens]) for nu, facs in parts)
    return sp.expand(total), sp.Mul(*[base**ex for base, ex in dens.items()])


def order_at_infinity(c):
    nu, de = _frac(c)
    if nu == 0:
        return None
    return sp.Poly(nu, r).degree() - sp.Poly(de, r).degree()


def leading(c):
    """(order at infinity, leading coefficient) of a rational function of r"""
    nu, de = _frac(c)
    pn, pd = sp.Poly(nu, r), sp.Poly(de, r)
    return pn.degree() - pd.degree(), sp.nsimplify(sp.simplify(pn.LC()/pd.LC()))


def psi_to_phi(e, K2, muv):
    """Psi = r^3 H phi"""
    HH = (K2 - 3 + 6*muv/r**2)
    e = sp.expand(e)
    rep = {d: D(r**3*HH*phi, *[v for v, c in d.variable_count for _ in range(c)]) for d in e.atoms(sp.Derivative)
           if d.expr == Psi}
    return sp.expand(e.xreplace(rep).xreplace({Psi: r**3*HH*phi}).doit())


_SOURCES = {}


def rung_sources(K2, muv, control=0):
    """the four rung sources of (10.31) and tr h_RW at a sample point, in canonical form, from G2's J and (10.1)"""
    if (K2, muv, control) in _SOURCES:
        return _SOURCES[(K2, muv, control)]
    C = Canon(K2, muv)
    F, Fab = reconstruction()
    J, _ = gauge_source()
    sub = {Ftt: Fab[0, 0], Ftr: Fab[0, 1], Frr: Fab[1, 1], Fs: F}
    sub = {k_: v.subs({kk: sp.sqrt(K2), mu: muv}) for k_, v in sub.items()}

    def in_phi(e):
        e = sp.expand(e.subs({kk: sp.sqrt(K2), mu: muv}))
        rep = {d: D(sub[d.expr], *[v for v, c in d.variable_count for _ in range(c)]) for d in e.atoms(sp.Derivative)
               if d.expr in sub}
        e = e.xreplace(rep).xreplace(sub)
        return C.reduce(psi_to_phi(e, K2, muv))
    Jt, Jr, JL = in_phi(J["t"]), in_phi(J["r"]), in_phi(J["L"])
    F4 = in_phi(4*Fs)
    ff = f.subs(mu, muv)
    GP = C.reduce(r*(D(Jr, t) - D(Jt, r)) - D(F4, t) - (1 if control != 1 else -1)*2*Jt) + D(Sig, t)
    _SOURCES[(K2, muv, control)] = (C, {"P": GP, "t": Jt, "1": C.reduce(ff*Jr), "L": JL, "F4": F4})
    return _SOURCES[(K2, muv, control)]


def closed_forms(K2, muv):
    """the coefficient functions of (10.31) as read off the three modes and fitted in k"""
    mm = K2 - 3
    HH = mm + 6*muv/r**2
    ff = f.subs(mu, muv)
    c2 = (24*muv + sp.Rational(4, 3)*mm*(K2 + 6)*r**2)/(r**2*HH)
    ct = -2*(3*mm*r**4 - (4*mm - 6)*muv*r**2 - 12*muv**2)/(r**4*HH)
    c1r = 2*muv*ff*((mm + 12)*r**2 - 6*muv)/(r**4*HH)
    cF = (12*muv + sp.Rational(2, 3)*mm*(K2 + 6)*r**2)/(r**2*HH)
    Vp = v_phi(K2).subs(mu, muv)
    return {"P": 4*r*ff*D(phi, r, t) + c2*D(phi, t) + D(Sig, t),
            "t": -2*r*ff*D(phi, r, t) + ct*D(phi, t),
            "1": -2*r*D(phi, t, 2) + c1r*D(phi, r) - r*ff*Vp*phi,
            "L": sp.Integer(0),
            "F4": 2*r*ff*D(phi, r) + cF*phi}


def g4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for K2, muv in SAMPLES:
        C, G = rung_sources(K2, muv, control)
        want = closed_forms(K2, muv)
        good = True
        for key in ("P", "t", "1", "L", "F4"):
            diff = C.coeffs(G[key] - want[key])
            good &= not diff
        chk("k^2 = %d, mu = %s: the sources in canonical form are (10.31) -- G_P = 4 r f d_t d_r phi + c_2 d_t phi + "
            "d_t Sigma, J_t = -2 r f d_t d_r phi + c_t d_t phi, f J_r = -2 r d_t^2 phi + O(r^-2) d_r phi - r f V_phi "
            "phi, J_L = 0, 4F = 2 r f d_r phi + c_F phi" % (K2, muv), good)
    return chk.ok


def substitutions(K2, muv):
    """the corrections (10.32): rP-bar, X_t-bar, X_1-bar, X_L-bar"""
    mm = K2 - 3
    HH = mm + 6*muv/r**2
    ff = f.subs(mu, muv)
    k = sp.sqrt(K2)
    corrP = -r**2*D(phi, t) + Uf*(sp.Rational(2, 3)*K2*phi + Sig/2)
    corrT = r**2/2*D(phi, t) - Uf*phi
    corr1 = r**2*ff/2*D(phi, r) + (mm*r**4 + 6*muv**2)/(r**3*HH)*phi
    corrL = k*r/2*phi
    return corrP, corrT, corr1, corrL


def g5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for K2, muv in SAMPLES:
        C, G = rung_sources(K2, muv)
        ff = f.subs(mu, muv)
        k = sp.sqrt(K2)
        corrP, corrT, corr1, corrL = substitutions(K2, muv)
        if control == 1:                                   # half the (u + r) phi coefficient: an O(1) d_t phi survives
            corrP = -r**2*D(phi, t) + Uf*(sp.Rational(1, 3)*K2*phi + Sig/2)
        NP = G["P"] + C.boxl(corrP) + 4*muv/r**4*corrP
        Nt = G["t"] + C.boxl(corrT)
        L1 = lambda X1, XL: C.boxl(X1) - 3/r**2*(1 - 3*muv/r**2)*X1 - 2*k/r**2*(1 - 2*muv/r**2)*XL
        LL = lambda X1, XL: C.boxl(XL) + (1 + muv/r**2)/r**2*XL - 2*k/r**2*X1
        N1 = G["1"] + L1(corr1, corrL)
        NL = G["L"] + LL(corr1, corrL)
        for name, N in (("rP-bar", NP), ("X_t-bar", Nt), ("X_1-bar", N1), ("X_L-bar", NL)):
            co = C.coeffs(N)
            bad = []
            for (pw, key), c in co.items():
                o = order_at_infinity(c)
                cnt = dict(key.variable_count) if isinstance(key, sp.Derivative) else {}
                nt, nr = cnt.get(t, 0), cnt.get(r, 0)
                if (nt >= 2 and nr == 0) or (nt >= 1 and nr >= 1):
                    bad.append(("second order", key))
                elif o is not None and o > (-2 if pw == 0 else -4):
                    bad.append((o, key))
            chk("k^2 = %d, mu = %s, %s: no d_t d_r or d_t^2 term, every coefficient O(r^-2) or better, the (u + r)-"
                "weighted ones O(r^-4)%s" % (K2, muv, name, "" if not bad else " -- FAILS: %s" % bad), not bad)
        co = C.coeffs(NP)                                     # (10.33)'s first line: Sigma exact, phi to leading order
        exact = {(0, D(Sig, t)): -muv/(r**2*ff), (0, D(Sig, r)): -muv/r**2, (0, Sig): -muv/(2*r**3),
                 (1, Sig): 2*muv/r**4}
        lead = {(0, D(phi, r)): (-2, -sp.Rational(4, 3)*K2*muv), (0, phi): (-3, -sp.Rational(2, 3)*K2*muv)}
        good = all(_frac(co.get(key, 0) - v)[0] == 0 for key, v in exact.items())
        good &= all(leading(co.get(key, 0)) == v for key, v in lead.items())
        chk("k^2 = %d, mu = %s, rP-bar's source: -(mu/(r^2 f)) nabla_L Sigma - (mu/(2 r^3)) Sigma + (2 mu/r^4) (u + r) "
            "Sigma exactly, -(4 k^2 mu/(3 r^2)) d_r phi - (2 k^2 mu/(3 r^3)) phi to leading order" % (K2, muv), good)
        co = C.coeffs(Nt)                                     # line 2: d_r phi, phi and the (u + r) phi term exact
        exact = {(0, D(phi, r)): 2*muv/r**2, (0, phi): muv/r**3, (1, phi): -v_phi(K2).subs(mu, muv)}
        good = all(_frac(co.get(key, 0) - v)[0] == 0 for key, v in exact.items())
        chk("k^2 = %d, mu = %s, X_t-bar's source: (2 mu/r^2) d_r phi + (mu/r^3) phi - (u + r) V_phi phi exactly" %
            (K2, muv), good)
        mm = K2 - 3                                           # lines 3-4: one phi term each, of order r^-3
        for name, N, lc in (("X_1-bar", N1, 2*muv*K2*(K2 + 1)/mm), ("X_L-bar", NL, -6*k*muv*(K2 + 1)/mm)):
            co = C.coeffs(N)
            good = set(co) == {(0, phi)} and leading(co[(0, phi)]) == (-3, lc)
            chk("k^2 = %d, mu = %s, %s's source is a single phi term, leading (%s)/r^3" % (K2, muv, name, lc), good)
    return chk.ok


CHECKS = [("G1 the transcription of [KI03] at n = 3: the trace, the Einstein equations E_a = 0, Zerilli at n = 2", g1,
           1),
          ("G2 J = -Gamma[h_RW] in h_RW's components, (10.28), and tr h_RW = F^a_a + 6F = 4F", g2, 1),
          ("G3 the direct system (10.29): Hung's (4.21)-(4.23) in five dimensions", g3, 1),
          ("G4 the rung sources in canonical form, (10.31), at four modes", g4, 1),
          ("G5 the substitutions (10.32) remove every bad weight: the sources of the barred rungs", g5, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"growing5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            mm = fn(control=k)
            caught += (not mm)
            print(f"mutant {k} of {name[:2]}: {'caught' if not mm else 'NOT caught'}", flush=True)
    print(f"growing5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
