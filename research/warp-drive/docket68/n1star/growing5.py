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

READ (alphaXiv, 2026-10-21).  [KI03] H. Kodama, A. Ishibashi, A master equation for gravitational perturbations of
maximally symmetric black holes in higher dimensions, hep-th/0305147v3: sections 2-3 ((2.4)-(2.8), (2.11)-(2.13),
(2.20)-(2.21), (3.1)-(3.7), (3.9)-(3.14)), section 6 (6.1), Appendix A ((A.1b)).  [Hun19] section 4.2 pp. 26-32
((4.10)-(4.42), Lemmas 4.8-4.10), section 5 (Propositions 5.1-5.9, Lemma 5.5), section 6 (6.1)-(6.11).

sympy.  python3 growing5.py [--selftest | --mutants]   (about four minutes; --verbose lists every sub-check)
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


CHECKS = [("G1 the transcription of [KI03] at n = 3: the trace, the Einstein equations E_a = 0, Zerilli at n = 2", g1,
           1),
          ("G2 J = -Gamma[h_RW] in h_RW's components, (10.28), and tr h_RW = F^a_a + 6F = 4F", g2, 1),
          ("G3 the direct system (10.29): Hung's (4.21)-(4.23) in five dimensions", g3, 1)]


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
