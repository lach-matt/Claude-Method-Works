#!/usr/bin/env python3
"""rungs5.py -- the rungs of the gauge-vector system on five-dimensional Tangherlini: the scalar wave equation with the
Maxwell potential -4 mu/r^4 and the free one, at the modes l >= 2 of the class (N1STAR-PROOF.md section 10.6,
Propositions 10.4-10.5; D49).  Labels: computed (exact, sympy), deduced, READ.

The gauge-vector system of Proposition 10.2(v) is triangular, every rung a scalar wave equation box u - V u = G on the
exterior of g = -f dt^2 + dr^2/f + r^2 gamma_{S^3}, f = 1 - mu/r^2, at a scalar mode k^2 = l(l + 2) >= 8: V = 0 for
S = div X, X_t and r X_L, and V = -4 mu/r^4 for r P (P = F_tr/S_l; the Maxwell master equation of [KI03b] (5.20) at
n = 3).  The estimates for such an equation are those of [HKW18] section 7 (T-energy comparison, red-shift, Morawetz,
the r^p hierarchy, the dyadic argument) and of [Hun19] Appendix A, and the one thing in them that depends on the
potential is the Morawetz multiplier.  This instrument computes what the proofs use:

  M1 (computed, exact) The Morawetz identity [HKW18] (123) at n = 3 for a scalar u(t, r) at mode k with a radial
     potential V and a source G, on the quotient with the measure r^3: for X = F d_r*, omega = F' + 3 f F/r (' = d_r* = f
     d_r), and the current J_a = T_ab X^b + (1/4) omega d_a(u^2) - (1/4) (d_a omega) u^2 + F' beta u^2 (dr*)_a with T_ab
     = d_a u d_b u - (1/2) g_ab (du.du + (k^2/r^2 + V) u^2), div J = (F'/f) |d_r* u + beta u|^2 + (F/r^3)(1 - 2 mu/r^2)
     k^2 u^2 + W0(F, beta) u^2 + G (F d_r* u + omega u/2), W0 = -(1/4) box omega - (1/2) V' F + (1/2) (mu/r^2)' V F + F''
     beta/f + F' (beta'/f + 3 beta/r - beta^2/f), box omega = r^-3 d_r (r^3 f d_r omega).  Control: the sign of the beta
     term reversed.
  M2 (computed, exact) The positivity for the Maxwell rung V = -4 mu/r^4 and the free rung V = 0 at k^2 = 8 with
     [HKW18]'s n = 3 choice read in mu = 2M, F = (1 - 2 mu/r^2)(1 - mu/(2 r^2) + mu^2/(5 r^4)) and beta = 1/(2 sqrt mu)
     (their 1/2 in units M = 1): with the angular term borrowed through k^2 u^2 >= 8 u^2, W := W0 + 8 F (1 - 2
     mu/r^2)/r^3 is mu^(-3/2) (-y^3/40) Q(y), y = sqrt(mu)/r in (0, 1], with Q a polynomial of degree ten having no root
     in [0, 1] and Q(0) = -300: so W > 0 on the exterior, W >= c r^-3 with c = 1/4 (Maxwell) and 1/5 (free), W(r_h) =
     17/(4 mu^(3/2)) and 141/(20 mu^(3/2)); F'/f = dF/dr = mu (25 r^4 - 24 mu r^2 + 12 mu^2)/(5 r^7) > 0 on the closed
     exterior, 13/(5 sqrt mu) at r_h; the angular coefficient F (1 - 2 mu/r^2)/r^3 = (r^2 - 2 mu)^2 (10 r^4 - 5 mu r^2 +
     2 mu^2)/(10 r^11) >= 0 with its double zero at the photon sphere r^2 = 2 mu; F bounded, from -7/10 at r_h to 1.
     Control: beta = 2/sqrt mu, for which W is negative on part of the exterior.
  M3 (computed, exact) Hung's (A.3) and the T-energy comparison pointwise: k^2/r^2 - 4 mu/r^4 >= k^2/(2 r^2) on the
     exterior for every k^2 >= 8 (equality at the horizon when k^2 = 8), so the T-energy density of the Maxwell rung is
     at least half the virtual one and no Hardy inequality is needed; |V| <= 4/mu, the bound the red-shift step needs.
     Control: k^2 = 4, which fails near the horizon.
  M4 (computed, exact) The r^p piece in the radiation variable Psi = r^(3/2) u: d_u d_v Psi = -f Vcal Psi - f r^(3/2) G
     with Vcal = k^2/r^2 + V + V0, V0 = (3/4 + 9 mu/(4 r^2))/r^2, V_inf := lim r^2 Vcal = k^2 + 3/4 >= 35/4, and Vcal -
     V_inf/r^2 = -7 mu/(4 r^4) (Maxwell), 9 mu/(4 r^4) (free): the p-current identity (10.7) of Proposition 10.3 with the
     source in the place of Uhat Psi, re-derived for one component.  Control: V_inf claimed k^2 + 1.
  M5 (computed, exact) The g-current of [HKW18] p. 55: div((1/4)(d_a g) u^2 - (1/4) g d_a(u^2)) = (1/4)(box g) u^2 +
     (1/2) g f^-1 |d_t u|^2 - (1/2) g (f |d_r u|^2 + (k^2/r^2 + V) u^2) - (1/2) g u G, the term that supplies |d_t u|^2
     to the Morawetz bulk.  Control: the sign of the second current term reversed.

READ (alphaXiv, 2026-10-21). [HKW18] P.-K. Hung, J. Keller, M.-T. Wang, arXiv:1809.05144v1: section 7 pp. 28-48
(Definition 8, (88), the decay foliation 7.3, the Poincare inequality (98) with lambda = 2 for scalar potentials, Lemma
9, Lemma 10, the T-energy comparison (111), the red-shift section 7.8 with Lemma 11 "for any bounded radial potential",
Theorem 12, Lemma 13, Theorem 14, the Morawetz currents (119)-(123), the r^p current (125), Proposition 15 with its proof
(a_0 bar = a_0 + (n^2 - 2n)/4), Theorem 16, Lemma 17, Theorem 18 with its proof); 9.3.2 pp. 54-57 (the n = 3 choice f,
beta = 1/2, the epsilon_0, epsilon_1 splits, g(r), the red-shift addition, the boundary terms, the remark on n >= 5);
10.4.2 and 10.5 pp. 66-67. [Hun19] Appendix A pp. 70-72 ((A.1)-(A.11)), as for W8. [KI03b] (5.17)-(5.20).

sympy.  python3 rungs5.py [--selftest | --mutants]   (about half a minute; --verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

t, r = sp.symbols("t r", real=True)
mu, kk = sp.symbols("mu k", positive=True)
yv = sp.symbols("y", positive=True)
f = 1 - mu/r**2
fp = sp.diff(f, r)
D = sp.diff


def drs(e):
    """d/dr* = f d/dr"""
    return f*D(e, r)


def boxrad(w):
    """the wave operator on a radial function"""
    return D(r**3*f*D(w, r), r)/r**3


def boxhat(w):
    """the quotient wave operator on u(t, r): -f^-1 d_t^2 + f d_r^2 + (f' + 3f/r) d_r"""
    return -D(w, t, 2)/f + f*D(w, r, 2) + (fp + 3*f/r)*D(w, r)


F_HKW = (1 - 2*mu/r**2)*(1 - mu/(2*r**2) + mu**2/(5*r**4))
BETA_HKW = sp.Rational(1, 2)/sp.sqrt(mu)
V_MAX = -4*mu/r**4


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


def _quotient_setup(u, V, G):
    """u_tt from box u = (k^2/r^2 + V) u + G, the metric and energy-momentum tensor on the quotient"""
    utt = sp.expand(f*(f*D(u, r, 2) + (fp + 3*f/r)*D(u, r) - (kk**2/r**2 + V)*u - G))
    g = sp.diag(-f, 1/f)
    gi = g.inv()
    grad = [D(u, t), D(u, r)]
    sq = sum(gi[a, b]*grad[a]*grad[b] for a in range(2) for b in range(2)) + (kk**2/r**2 + V)*u**2
    T = sp.Matrix(2, 2, lambda a, b: grad[a]*grad[b] - g[a, b]*sq/2)
    return utt, g, gi, T


def _divergence(Jl, gi, u, utt):
    Ju = gi*Jl
    div = (D(r**3*Ju[0], t) + D(r**3*Ju[1], r))/r**3
    return sp.expand(div.subs(D(u, t, 2), utt).doit())


def W_of(F, beta, V, k2):
    """W0(F, beta) of M1 and W = W0 + k2 F (1 - 2 mu/r^2)/r^3, the angular term borrowed"""
    omega = drs(F) + 3*f*F/r
    W0 = ((-boxrad(omega)/4 - drs(V)*F/2 + D(mu/r**2, r)*V*F/2)
          + (drs(drs(F))*beta/f + drs(F)*(drs(beta)/f + 3*beta/r - beta**2/f)))
    return W0, sp.simplify(W0 + k2*F*(1 - 2*mu/r**2)/r**3)


def m1(control=0, verbose=False):
    """M1: the Morawetz identity, HKW18 (123) at n = 3 for a scalar with potential and source"""
    chk = Checklist(verbose, quiet=control != 0)
    u, V, F, beta, G = (sp.Function("u")(t, r), sp.Function("V")(r), sp.Function("F")(r), sp.Function("beta")(r),
                        sp.Function("G")(t, r))
    utt, g, gi, T = _quotient_setup(u, V, G)
    X = sp.Matrix([0, F*f])
    omega = drs(F) + 3*f*F/r
    sgn = -1 if control == 1 else 1
    Jl = sp.Matrix([sum(T[a, b]*X[b] for b in range(2)) + omega*D(u**2, [t, r][a])/4 - D(omega, [t, r][a])*u**2/4
                    + sgn*drs(F)*beta*u**2*sp.Matrix([0, 1/f])[a] for a in range(2)])
    div = _divergence(Jl, gi, u, utt)
    W0, _ = W_of(F, beta, V, 0)
    want = (drs(F)/f*(drs(u) + beta*u)**2 + F/r**3*(1 - 2*mu/r**2)*kk**2*u**2 + W0*u**2
            + G*(F*drs(u) + omega*u/2))
    chk("div J = (F'/f)|d_r* u + beta u|^2 + (F/r^3)(1 - 2 mu/r^2) k^2 u^2 + W0 u^2 + G (F d_r* u + omega u/2), W0 = "
        "-(1/4) box omega - (1/2) V' F + (1/2)(mu/r^2)' V F + F'' beta/f + F'(beta'/f + 3 beta/r - beta^2/f) ([HKW18] "
        "(123), n = 3)", sp.simplify(sp.expand(div - want)) == 0)
    return chk.ok


def m2(control=0, verbose=False):
    """M2: positivity of the Morawetz bulk for the Maxwell and the free rung with HKW18's F and beta = 1/(2 sqrt mu)"""
    chk = Checklist(verbose, quiet=control != 0)
    beta = 2/sp.sqrt(mu) if control == 1 else BETA_HKW
    Fp = sp.factor(sp.simplify(drs(F_HKW)/f))
    chk("F'/f = dF/dr = mu (25 r^4 - 24 mu r^2 + 12 mu^2)/(5 r^7) > 0 on the closed exterior, 13/(5 sqrt mu) at r_h; F "
        "from -7/10 at r_h to 1",
        sp.simplify(Fp - mu*(25*r**4 - 24*mu*r**2 + 12*mu**2)/(5*r**7)) == 0
        and sp.Poly(25*yv**4 - 24*yv**2 + 12, yv).count_roots(0, 1) == 0
        and sp.simplify(Fp.subs(r, sp.sqrt(mu)) - sp.Rational(13, 5)/sp.sqrt(mu)) == 0
        and F_HKW.subs(r, sp.sqrt(mu)) == sp.Rational(-7, 10) and sp.limit(F_HKW, r, sp.oo) == 1)
    ang = sp.factor(F_HKW*(1 - 2*mu/r**2)/r**3)
    chk("the angular coefficient F (1 - 2 mu/r^2)/r^3 = (r^2 - 2 mu)^2 (10 r^4 - 5 mu r^2 + 2 mu^2)/(10 r^11) >= 0, a "
        "double zero at the photon sphere",
        sp.simplify(ang - (r**2 - 2*mu)**2*(10*r**4 - 5*mu*r**2 + 2*mu**2)/(10*r**11)) == 0
        and sp.Poly(10 - 5*yv**2 + 2*yv**4, yv).count_roots(0, 1) == 0)
    for name, V, c, Wh in (("Maxwell V = -4 mu/r^4", V_MAX, sp.Rational(1, 4), sp.Rational(17, 4)),
                           ("free V = 0", sp.Integer(0), sp.Rational(1, 5), sp.Rational(141, 20))):
        W0, W = W_of(F_HKW, beta, V, 8)
        P = sp.simplify((W*mu**sp.Rational(3, 2)).subs(r, sp.sqrt(mu)/yv))
        Q = sp.Poly(sp.cancel(-40*P/yv**3), yv)
        good = Q.degree() == 10 and Q.count_roots(0, 1) == 0 and Q.eval(0) < 0 and Q.eval(1) < 0
        # W >= c r^-3 on the exterior: -Q(y)/40 >= c on [0, 1], tested on a fine grid after the root count
        good &= all(-Q.eval(sp.Rational(i, 200))/40 >= c for i in range(201))
        good &= sp.simplify(W.subs(r, sp.sqrt(mu)) - Wh/mu**sp.Rational(3, 2)) == 0
        chk("%s, k^2 = 8, beta = 1/(2 sqrt mu): mu^(3/2) W = -(y^3/40) Q(y) with Q of degree ten, no root in [0, 1], "
            "Q(0) = -300: W > 0 on the exterior, W >= %s r^-3, W(r_h) = %s/mu^(3/2)" % (name, c, Wh), good)
    return chk.ok


def m3(control=0, verbose=False):
    """M3: (A.3) pointwise with room, and the bound on the potential"""
    chk = Checklist(verbose, quiet=control != 0)
    k2 = 4 if control == 1 else 8
    x = sp.symbols("x", positive=True)                        # x = mu/r^2 in (0, 1]
    e = sp.expand(((k2/r**2 + V_MAX - sp.Rational(k2, 2)/r**2)*r**2).subs(mu, x*r**2))
    chk("k^2/r^2 - 4 mu/r^4 >= k^2/(2 r^2) on the exterior at k^2 = %d (and so for every k^2 >= 8): the T-energy "
        "density "
        "of the Maxwell rung is at least half the virtual one" % k2,
        sp.Poly(e, x).count_roots(0, 1) == (1 if k2 == 8 else 0) and e.subs(x, sp.Rational(1, 2)) > 0
        and e.subs(x, 1) >= 0
        and all(e.subs(x, sp.Rational(i, 50)) >= 0 for i in range(1, 51)))
    chk("|V| <= 4/mu on the exterior", sp.simplify(sp.Abs(V_MAX).subs(r, sp.sqrt(mu)) - 4/mu) == 0)
    return chk.ok


def m4(control=0, verbose=False):
    """M4: the radiation variable's potential and the p-current identity with the source, one component"""
    chk = Checklist(verbose, quiet=control != 0)
    V0 = (sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2
    shift = 1 if control == 1 else sp.Rational(3, 4)
    for name, V, rem in (("Maxwell", V_MAX, -7*mu/(4*r**4)), ("free", sp.Integer(0), 9*mu/(4*r**4))):
        Vc = kk**2/r**2 + V + V0
        Vinf = sp.limit(Vc*r**2, r, sp.oo)
        chk("%s: V_inf = lim r^2 (k^2/r^2 + V + V0) = k^2 + 3/4 and Vcal - V_inf/r^2 = %s" % (name, rem),
            sp.simplify(Vinf - (kk**2 + shift)) == 0 and sp.simplify(Vc - Vinf/r**2 - rem) == 0)
    # the p-current identity for one component with the source: d_u d_v Psi = -f Vcal Psi - f S, S = r^(3/2) G
    p = sp.Symbol("p", positive=True)
    Psi, S, Vf = sp.Function("Psi")(t, r), sp.Function("S")(t, r), sp.Function("Vf")(r)
    vinf = sp.Symbol("v_inf")
    Ptt = sp.expand(f*(f*D(Psi, r)).diff(r) - f*Vf*Psi - f*S)
    g = sp.diag(-f, 1/f)
    gi = g.inv()
    grad = [D(Psi, t), D(Psi, r)]
    sq = sum(gi[a, b]*grad[a]*grad[b] for a in range(2) for b in range(2))
    T = sp.Matrix(2, 2, lambda a, b: grad[a]*grad[b] - g[a, b]*sq/2)
    Lv = sp.Matrix([1, f])
    Ll = g*Lv
    Jl = sp.Matrix([r**(p - 3)/f*(sum(T[a, b]*Lv[b] for b in range(2)) - vinf*Psi**2/r**2*Ll[a]/2) for a in range(2)])
    Ju = gi*Jl
    div = sp.expand(((D(r**3*Ju[0], t) + D(r**3*Ju[1], r))/r**3).subs(D(Psi, t, 2), Ptt).doit())
    LP = D(Psi, t) + f*D(Psi, r)
    want = (r**(p - 4)*(p*f/2 - mu/r**2)/f**2*LP**2 + (2 - p)*r**(p - 6)/2*vinf*Psi**2
            + r**(p - 3)/f*LP*((Vf - vinf/r**2)*Psi + S))
    chk("div J^p = r^(p-4) f^-2 (p f/2 - mu/r^2)|nabla_L Psi|^2 + (2 - p)/2 r^(p-6) V_inf Psi^2 + r^(p-3) f^-1 "
        "nabla_L Psi "
        "((Vcal - V_inf/r^2) Psi + r^(3/2) G): (10.7) for one component, the source in the place of Uhat Psi",
        sp.simplify(sp.expand(div - want)) == 0)
    return chk.ok


def m5(control=0, verbose=False):
    """M5: the g-current identity, HKW18 p. 55"""
    chk = Checklist(verbose, quiet=control != 0)
    u, V, gfun, G = sp.Function("u")(t, r), sp.Function("V")(r), sp.Function("g")(r), sp.Function("G")(t, r)
    utt, g, gi, T = _quotient_setup(u, V, G)
    sgn = -1 if control == 1 else 1
    Jl = sp.Matrix([D(gfun, [t, r][a])*u**2/4 - sgn*gfun*D(u**2, [t, r][a])/4 for a in range(2)])
    div = _divergence(Jl, gi, u, utt)
    want = (boxrad(gfun)*u**2/4 + gfun/f*D(u, t)**2/2 - gfun*(f*D(u, r)**2 + (kk**2/r**2 + V)*u**2)/2 - gfun*u*G/2)
    chk("div((1/4)(d g) u^2 - (1/4) g d(u^2)) = (1/4)(box g) u^2 + (1/2) g f^-1 |d_t u|^2 - (1/2) g (f |d_r u|^2 "
        "+ (k^2/r^2 + "
        "V) u^2) - (1/2) g u G", sp.simplify(sp.expand(div - want)) == 0)
    return chk.ok


CHECKS = [("M1 the Morawetz identity, HKW18 (123) at n = 3, scalar with potential and source", m1, 1),
          ("M2 the Morawetz bulk is positive for the Maxwell and the free rung: F' > 0, W > 0, W >= c r^-3", m2, 1),
          ("M3 Hung's (A.3) with room: the T-energy density at least half the virtual one; |V| <= 4/mu", m3, 1),
          ("M4 the radiation variable: V_inf = k^2 + 3/4, the remainder O(mu/r^4), the p-current with the source", m4,
           1),
          ("M5 the g-current identity that supplies |d_t u|^2 to the Morawetz bulk", m5, 1)]


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
    print(f"rungs5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"rungs5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
