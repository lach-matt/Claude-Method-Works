#!/usr/bin/env python3
"""hierarchy5.py -- the first rungs' rapid decay on five-dimensional Tangherlini: [Hun19] Proposition A.5 with k = 1,
one commutation with r^2 nabla_L, for the homogeneous first rungs Sigma = tr h (V = 0) and the master field phi (V =
V_phi, (10.30)), and the l = 0 obstruction (N1STAR-PROOF.md section 10.9; D51).  Labels: computed (exact, sympy),
deduced, READ.

Section 10.7 bounds the sources of the barred rungs by the first rungs with a factor (1 + tau/sqrt mu)^2 on [b r_h,
2 b r_h], which the rungs' own rate tau^(-2+p) cannot pay; [Hun19] pays it with Proposition A.5 at k = 1 (his
Propositions 5.2 and 5.4, rate (1 + tau/M)^(-4+p+3 delta)), the r^p hierarchy of Angelopoulos-Aretakis-Gajic extended
past p = 2 by commuting once with f^-1 r^2 nabla_L, under the conditions (A.7)-(A.9) on the potential.  This instrument
computes the five-dimensional form of the commuted equation, of the p-current identity it enters, and of each condition,
for the radiation field Psi = r^(3/2) u of a scalar mode k^2 = l(l + 2) with L Lbar Psi = -f Vcal Psi, Vcal = k^2/r^2 +
V + (3/4 + 9 mu/(4 r^2))/r^2 (rungs5.py M4), L = d_t + f d_r, Lbar = d_t - f d_r, f = 1 - mu/r^2.

  H1 (computed, exact) The commuted equation.  Psi_1 := f^-1 r^2 L Psi ([Hun19] (2.4)'s Phi^(1) in five dimensions)
     satisfies, for a symbolic radial potential V,
         L Lbar Psi_1 = -(2/r)(1 - 2 mu/r^2) L Psi_1 - f Vcal_1 Psi_1 + f (9 mu/(2 r^3) - r^2 V' - 2 r V) Psi,
         Vcal_1 = Vcal - 2/r^2 + 12 mu/r^4,   V1_inf := lim r^2 Vcal_1 = k^2 - 5/4 = (l - 1/2)(l + 5/2),
     exactly: the shift of the angular coefficient is -2 as in four dimensions, the Psi term (his "bad term") is
     (9 mu f/(2 r^3)) Psi for V = 0 and free of k, and the first-order term is new.  In four dimensions the same
     computation on r psi gives Vcal_1 = l(l + 1)/r^2 + V^(1) exactly, his V^(1) := V + 2M/r^3 - 2/r^2 + 12 M/r^3 (his
     V^(j) is measured from V, and the 2M/r^3 is the radiation field's own, so his 14 M/r^3 is the 12 M/r^3 of Vcal_1 -
     Vcal with it), with the first-order term -(2/r)(1 - 3M/r) nabla_L Phi^(1), which his sentence on r^-1 (r^2 L)^k (r
     psi) does not print and which (H2) enters the current with a good sign, and the Psi term (2M/r^2 - r^2 V' - 2 r V)
     f Phi^(0) (READ).  Control: Psi_1 := r^2 L Psi without the f^-1, whose Psi term carries -2 k^2 mu f/r^5 and is not
     uniform in l.
  H2 (computed, exact) The p-current identity for Psi_1: with J^p of (10.7) built on Psi_1 and V1_inf, measure r^3,
         div J^p[Psi_1] = r^(p-4) f^-2 (p f/2 + 2 - 5 mu/r^2) |L Psi_1|^2 + ((2 - p)/2) r^(p-6) V1_inf Psi_1^2
                          + r^(p-3) f^-1 L Psi_1 ((Vcal_1 - V1_inf/r^2) Psi_1 - f^-1 C Psi),
     C := f (9 mu/(2 r^3) - r^2 V' - 2 r V) the coefficient of H1:
     the first-order term adds 2(1 - 2 mu/r^2) to the |L Psi_1|^2 coefficient, which is then positive for r^2 > (10 +
     p) mu/(4 + p) (at most 5 mu/2) and not only for p > 0; and the Psi_1 L Psi_1 term is a divergence plus the bulk
     -(1/2) Psi_1^2 r^-3 d_r(r^p (Vcal_1 - V1_inf/r^2)).  Control: the sign of the first-order term reversed.
  H3 (computed) [Hun19]'s (A.7)-(A.9) and (A.3), (A.5) in five dimensions.  The Psi_1^2 bulk of H2 after that
     integration by parts, times r^(6-p), is
         B_1 = ((2 - p)/2)(k^2 - 5/4) + (57/8)(4 - p) mu/r^2                                   for V = 0 (Sigma),
     positive on the whole exterior for p in [0, 2] and l >= 1 -- (A.7) with no R_null needed -- and for V = V_phi it
     is ((2 - p)/2)(k^2 - 5/4) + (mu/r^2) Q_1(k^2, mu/r^2, p)/H^3 with Q_1 a polynomial, so that B_1 >= (1/4)(2 -
     p)(k^2 - 5/4) for r >= R_1(k, p); R_1 is computed at k^2 = 8, 24, 48, 80 over p in [delta, 2 - delta], delta =
     1/10, as his Lemma 5.3 computes R_Z, on a grid of 21 values of p that is complete because B_1 - (1/4)(2 - p)(k^2 -
     5/4) is affine in p (checked), and the radii are pinned.  The base bulk B_0 = ((2 - p)/2)(k^2 + 3/4) + (9/8)(4 - p)
     mu/r^2 for V = 0 (positive everywhere; (A.5)) and its V_phi form with R_0 likewise.  (A.8): V1_inf = k^2 - 5/4 > 0
     for l >= 1.  (A.9): r^4 |V_phi|/mu <= 12 (k^2 + 3)/(k^2 - 3) and r^3 |d_r(r^2 V_phi)|/mu <= 24 (k^2 + 3)/(k^2 - 3)
     on the exterior, the suprema attained at infinity, exactly (Sturm), so bounded uniformly in k (V_phi -> -12
     mu/r^4 as k -> oo); (A.3): r^2 (k^2/r^2 + V_phi) decreases in mu/r^2, so its minimum is at the horizon, 4/11,
     124/9, 628/17, 5692/83 at the four modes, exactly.  Controls: V1_inf claimed k^2 - 2 (the four-dimensional shift);
     (A.3) claimed at k^2 = 3, where it fails.
  H4 (computed) The l = 0 obstruction.  At k = 0, V_inf = 3/4 and V1_inf = -5/4: the commuted potential violates (A.8),
     and the base bulk B_0 = ((2 - p)/2)(3/4) + (9/8)(4 - p) mu/r^2 is negative for every p > 2 once r^2 > 3(4 - p)
     mu/(p - 2), so the r^p hierarchy of S_W stops at p < 2 and his Proposition A.6 (1), which extends it to p < 4
     because V_inf = 0 at l = 0 in four dimensions, does not transcribe; V1_inf is computed from H1's equation at k =
     0.  Controls: the four-dimensional l = 0 bulk, (3 - p) M r^(p-6), is positive for p < 3, and asserting the
     five-dimensional sign of it fails; the radiation field's (3/4)/r^2 dropped, as in four dimensions, for which B_0
     has no such root.  (The Psi^2 bulk -(1/2) r^(3-p) d_r(r^p Vcal) does not depend on how V_inf is split off; V_inf's
     own role is the sign of the flux r^(p-5) V_inf Psi^2 at null infinity, which is (A.8).)

READ (alphaXiv, 2026-10-21).  [Hun19] Appendix A pp. 70-73 in full: (A.1)-(A.14), Definitions A.1-A.2, Remark A.3,
Propositions A.4-A.6, the account of [2] (Angelopoulos-Aretakis-Gajic) and of the Newman-Penrose constant; Lemma 5.3
with its proof (V^(1)_Z = V_Z - 2/r^2 + 14 M/r^3, lim r^2 V^(1) = -2, lim V_Z = -8 M/r^3), Propositions 5.2 and 5.4,
Lemma 5.5; (2.4) (Phi^(j)), (2.19)-(2.23); Proposition 8.2 and Lemma 8.3.  [HKW18] section 7 as for rungs5.py.

sympy.  python3 hierarchy5.py [--selftest | --mutants]   (about a minute; --verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

t = sp.Symbol("t", real=True)
r = sp.Symbol("r", positive=True)
mu, kk = sp.symbols("mu k", positive=True)
p = sp.Symbol("p", positive=True)
xv = sp.Symbol("x", positive=True)                                                    # x = mu/r^2
D = sp.diff
f5 = 1 - mu/r**2
f4 = 1 - 2*mu/r                                                                       # four dimensions, M = mu
DELTA = sp.Rational(1, 10)
MODES = (8, 24, 48, 80)                                                               # k^2 = l(l + 2), l = 2, 4, 6, 8


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


def v_phi(K2):
    """the master potential (10.30) on phi = r^(-3/2) Phi_KI"""
    H = K2 - 3 + 6*mu/r**2
    return -12*mu*(K2 + 3)*((K2 - 3)*r**2 + 2*mu)/(r**6*H**2)


def commuted(dim, a, Vf):
    """Psi = r^(n/2) psi for box_l psi = V psi in dim = n + 2 dimensions; Psi_1 := r^2 f^-a L Psi.  Returns Vcal and the
    coefficients (A, B, C) of L Lbar Psi_1 = A L Psi_1 + B Psi_1 + C Psi (no Lbar Psi term survives)"""
    n = dim - 2
    f = f5 if dim == 5 else f4
    Psi = sp.Function("Psi")(t, r)
    L = lambda e: D(e, t) + f*D(e, r)
    Lb = lambda e: D(e, t) - f*D(e, r)
    psi = Psi/r**sp.Rational(n, 2)
    boxl = -D(psi, t, 2)/f + D(r**n*f*D(psi, r), r)/r**n - kk**2/r**2*psi
    Ptt = sp.solve(sp.expand((boxl - Vf*psi)*r**sp.Rational(n, 2)*f), D(Psi, t, 2))[0]
    Vcal = sp.simplify(-sp.expand(D(Psi, t, 2) - f*D(f*D(Psi, r), r)).subs(D(Psi, t, 2), Ptt)/(f*Psi))

    def red(e):
        e = sp.expand(e.doit())
        for _ in range(6):
            rep = {}
            for d in e.atoms(sp.Derivative):
                if d.expr == Psi:
                    cnt = dict(d.variable_count)
                    if cnt.get(t, 0) >= 2:
                        extra = [t]*(cnt[t] - 2) + [r]*cnt.get(r, 0)
                        rep[d] = D(Ptt, *extra) if extra else Ptt
            if not rep:
                break
            e = sp.expand(e.xreplace(rep).doit())
        return e
    P1 = r**2/f**a*L(Psi)
    A, B, C, Dd = sp.symbols("A B C Dd")
    diff = sp.expand(red(L(Lb(P1))) - red(A*L(P1) + B*P1 + C*Psi + Dd*Lb(Psi)))
    basis = sorted({d for d in diff.atoms(sp.Derivative) if d.expr == Psi}, key=str) + [Psi]
    eqs = [sp.simplify(diff.coeff(b)) for b in basis]
    sol = sp.solve([e for e in eqs if e != 0], [A, B, C, Dd], dict=True)
    assert sol and sp.simplify(sol[0].get(Dd, 0)) == 0, "no Lbar-free form"
    s = sol[0]
    return Vcal, sp.simplify(s[A]), sp.simplify(s[B]), sp.simplify(s[C])


def h1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Vf = sp.Function("V")(r)
    a = 0 if control == 1 else 1
    Vcal, A, B, C = commuted(5, a, Vf)
    V1 = sp.simplify(-B/f5)
    chk("Vcal = k^2/r^2 + V + (3/4 + 9 mu/(4 r^2))/r^2 (rungs5 M4) and Vcal_1 := -B/f = Vcal - 2/r^2 + 12 mu/r^4",
        sp.simplify(Vcal - (kk**2/r**2 + Vf + (sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2)) == 0
        and sp.simplify(V1 - Vcal + 2/r**2 - 12*mu/r**4) == 0)
    chk("the first-order coefficient is -(2/r)(1 - 2 mu/r^2)", sp.simplify(A + 2*(1 - 2*mu/r**2)/r) == 0)
    chk("the Psi coefficient is f (9 mu/(2 r^3) - r^2 V' - 2 r V): (9 mu f/(2 r^3)) Psi for V = 0, free of k",
        sp.simplify(C - f5*(9*mu/(2*r**3) - r**2*D(Vf, r) - 2*r*Vf)) == 0 and kk not in C.free_symbols)
    l = sp.Symbol("l", positive=True)
    V1inf = sp.limit((V1*r**2).subs(Vf, 0), r, sp.oo)
    chk("V1_inf = k^2 - 5/4 = (l - 1/2)(l + 5/2) at k^2 = l(l + 2); V_inf = k^2 + 3/4 = (l + 1/2)(l + 3/2)",
        sp.simplify(V1inf - (kk**2 - sp.Rational(5, 4))) == 0
        and sp.expand(V1inf.subs(kk**2, l*(l + 2)) - (l - sp.Rational(1, 2))*(l + sp.Rational(5, 2))) == 0
        and sp.expand((kk**2 + sp.Rational(3, 4)).subs(kk**2, l*(l + 2))
                      - (l + sp.Rational(1, 2))*(l + sp.Rational(3, 2))) == 0)
    # four dimensions, READ against [Hun19] (2.4), Lemma 5.3 and the definition of V^(j)
    Vc4, A4, B4, C4 = commuted(4, a, Vf)
    V14 = sp.simplify(-B4/f4)
    chk("four dimensions: Vcal_1 = l(l + 1)/r^2 + V^(1) exactly, his V^(1) := V + 2M/r^3 - 2/r^2 + 12 M/r^3 = V - "
        "2/r^2 + 14 M/r^3; first-order term -(2/r)(1 - 3M/r), Psi term f (2M/r^2 - r^2 V' - 2 r V)",
        sp.simplify(V14 - (kk**2/r**2 + Vf + 2*mu/r**3 - 2/r**2 + 12*mu/r**3)) == 0
        and sp.simplify(V14 - Vc4 + 2/r**2 - 12*mu/r**3) == 0 and sp.simplify(A4 + 2*(1 - 3*mu/r)/r) == 0
        and sp.simplify(C4 - f4*(2*mu/r**2 - r**2*D(Vf, r) - 2*r*Vf)) == 0
        and sp.limit((V14 - Vc4)*r**2, r, sp.oo) == -2)
    return chk.ok


def _current_setup():
    """the p-current (10.7) for an abstract W with L Lbar W = -f Vcal_W W - f S_W, divergence with the measure r^3"""
    W, S, Vw = sp.Function("W")(t, r), sp.Function("S")(t, r), sp.Function("Vw")(r)
    vinf = sp.Symbol("v_inf")
    f = f5
    Wtt = sp.expand(f*(f*D(W, r)).diff(r) - f*Vw*W - f*S)
    g = sp.diag(-f, 1/f)
    gi = g.inv()
    grad = [D(W, t), D(W, r)]
    sq = sum(gi[a, b]*grad[a]*grad[b] for a in range(2) for b in range(2))
    T = sp.Matrix(2, 2, lambda a, b: grad[a]*grad[b] - g[a, b]*sq/2)
    Lv = sp.Matrix([1, f])
    Ll = g*Lv
    Jl = sp.Matrix([r**(p - 3)/f*(sum(T[a, b]*Lv[b] for b in range(2)) - vinf*W**2/r**2*Ll[a]/2) for a in range(2)])
    Ju = gi*Jl
    div = sp.expand(((D(r**3*Ju[0], t) + D(r**3*Ju[1], r))/r**3).subs(D(W, t, 2), Wtt).doit())
    return W, S, Vw, vinf, div


def h2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    W, S, Vw, vinf, div = _current_setup()
    f = f5
    LW = D(W, t) + f*D(W, r)
    Psi = sp.Function("Psi")(t, r)
    Cc = sp.Function("C")(r)
    sgn = -1 if control == 1 else 1
    A = sgn*(-2*(1 - 2*mu/r**2)/r)
    # L Lbar W = A L W - f Vcal_1 W + C Psi  <=>  S_W = -(A L W + C Psi)/f
    div1 = sp.expand(div.subs(S, -(A*LW + Cc*Psi)/f).doit())
    want = (r**(p - 4)/f**2*(p*f/2 + 2 - 5*mu/r**2)*LW**2 + (2 - p)/2*r**(p - 6)*vinf*W**2
            + r**(p - 3)/f*LW*((Vw - vinf/r**2)*W - Cc*Psi/f))
    chk("div J^p[Psi_1] = r^(p-4) f^-2 (p f/2 + 2 - 5 mu/r^2)|L Psi_1|^2 + ((2-p)/2) r^(p-6) V1_inf Psi_1^2 + r^(p-3) "
        "f^-1 L Psi_1 ((Vcal_1 - V1_inf/r^2) Psi_1 - f^-1 C Psi)", sp.simplify(sp.expand(div1 - want)) == 0)
    co = p*f/2 + 2 - 5*mu/r**2
    root = sp.solve(co, r**2)
    chk("the |L Psi_1|^2 coefficient vanishes at r^2 = (10 + p) mu/(4 + p), at most 5 mu/2 on p in [0, 2]",
        len(root) == 1 and sp.simplify(root[0] - (10 + p)*mu/(4 + p)) == 0
        and sp.simplify(((10 + p)/(4 + p)).subs(p, 0) - sp.Rational(5, 2)) == 0)
    # the Psi_1 L Psi_1 term as a divergence plus a bulk, with the measure r^3
    h = r**(p - 3)/f*(Vw - vinf/r**2)
    Lvec = [1, f]
    divergence = sp.expand(sum(D(r**3*h*W**2/2*Lvec[i], v) for i, v in enumerate((t, r)))/r**3)
    bulk = -W**2/2*D(r**p*(Vw - vinf/r**2), r)/r**3
    chk("r^(p-3) f^-1 L Psi_1 (Vcal_1 - V1_inf/r^2) Psi_1 = div((1/2) h Psi_1^2 L) - (1/2) Psi_1^2 r^-3 d_r(r^p "
        "(Vcal_1 - V1_inf/r^2))", sp.simplify(sp.expand(h*LW*W - divergence - bulk)) == 0)
    return chk.ok


def bulk_poly(V, vinf, shift, v0c=sp.Rational(3, 4)):
    """r^(6-p) times the Psi^2 bulk ((2-p)/2) r^(p-6) v_inf - (1/2) r^-3 d_r(r^p (Vcal - v_inf/r^2)), as a function of
    x = mu/r^2 and p; Vcal = k^2/r^2 + V + V0 + shift/r^2 (shift = 0 for the base, -2 for the commuted potential)"""
    V0 = (v0c + 9*mu/(4*r**2))/r**2
    Vc = kk**2/r**2 + V + V0 + shift/r**2 + (12*mu/r**4 if shift != 0 else 0)
    B = (2 - p)/2*vinf - r**(6 - p)/2*D(r**p*(Vc - vinf/r**2), r)/r**3
    B = sp.simplify(B.subs(r, sp.sqrt(mu/xv)))
    return sp.simplify(B)


def smallest_radius(Bx, lower, grid=21):
    """the smallest r/r_h beyond which Bx(x, p) >= lower(p) for every p in [delta, 2 - delta] (a grid), x = mu/r^2: for
    each p the first root in x of Bx - lower coming from x = 0 (large r), where the difference is positive"""
    worst = sp.Integer(1)
    for i in range(grid):
        pv = DELTA + (2 - 2*DELTA)*sp.Rational(i, grid - 1)
        expr = sp.together((Bx - lower).subs(p, pv))
        nu, de = sp.fraction(expr)
        assert expr.subs(xv, sp.Rational(1, 10**6)) > 0 and de.subs(xv, sp.Rational(1, 2)) > 0
        roots = sorted(sp.re(z) for z in sp.Poly(sp.expand(nu), xv).nroots(n=30) if abs(sp.im(z)) < 1e-20
                       and 0 < sp.re(z) <= 1)
        worst = min(worst, roots[0] if roots else sp.Integer(1))
    return sp.sqrt(1/worst)                                                            # r/r_h = (mu/x)^(1/2)/sqrt mu


PINNED = {8: (8.141, 10.563), 24: (1.0, 4.61), 48: (1.0, 3.041), 80: (1.0, 2.29)}          # R_1, R_0 in r_h
A3MIN = {8: sp.Rational(4, 11), 24: sp.Rational(124, 9), 48: sp.Rational(628, 17), 80: sp.Rational(5692, 83)}


def nonneg_01(e):
    """e (rational in x) >= 0 on [0, 1], exactly: its numerator, stripped of the powers of x, and its denominator have
    no root in [0, 1] and the quotient is positive at x = 1/2"""
    nu, de = sp.fraction(sp.together(sp.expand(e)))
    nu, de = sp.Poly(sp.expand(nu), xv), sp.Poly(sp.expand(de), xv)
    if nu.is_zero:
        return True
    while nu.eval(0) == 0:
        nu = sp.Poly(sp.cancel(nu.as_expr()/xv), xv)
    return (nu.count_roots(0, 1) == 0 and de.count_roots(0, 1) == 0
            and nu.eval(sp.Rational(1, 2))*de.eval(sp.Rational(1, 2)) > 0)


def h3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    shift1 = -2 if control != 1 else -sp.Rational(11, 4)                              # control: V1_inf = k^2 - 2
    v1inf = kk**2 - sp.Rational(5, 4) if control != 1 else kk**2 - 2
    B1 = bulk_poly(sp.Integer(0), v1inf, shift1)
    chk("Sigma (V = 0): B_1 = ((2-p)/2)(k^2 - 5/4) + (57/8)(4 - p) mu/r^2 exactly",
        sp.simplify(B1 - ((2 - p)/2*(kk**2 - sp.Rational(5, 4)) + sp.Rational(57, 8)*(4 - p)*xv)) == 0)
    B0 = bulk_poly(sp.Integer(0), kk**2 + sp.Rational(3, 4), 0)
    chk("Sigma: the base bulk B_0 = ((2-p)/2)(k^2 + 3/4) + (9/8)(4 - p) mu/r^2 exactly; both positive on the exterior "
        "for p in [0, 2], l >= 1",
        sp.simplify(B0 - ((2 - p)/2*(kk**2 + sp.Rational(3, 4)) + sp.Rational(9, 8)*(4 - p)*xv)) == 0)
    radii = {}
    for K2 in MODES:
        V = v_phi(K2)
        Bx1 = bulk_poly(V, sp.Integer(K2) - sp.Rational(5, 4), -2).subs(kk, sp.sqrt(K2))
        Bx0 = bulk_poly(V, sp.Integer(K2) + sp.Rational(3, 4), 0).subs(kk, sp.sqrt(K2))
        affine = all(sp.Poly(sp.fraction(sp.together(Bx - lo))[0], p).degree() <= 1
                     for Bx, lo in ((Bx1, (2 - p)/4*(K2 - sp.Rational(5, 4))),
                                    (Bx0, (2 - p)/4*(K2 + sp.Rational(3, 4)))))
        R1 = smallest_radius(Bx1, (2 - p)/4*(K2 - sp.Rational(5, 4)))
        R0 = smallest_radius(Bx0, (2 - p)/4*(K2 + sp.Rational(3, 4)))
        radii[K2] = (round(float(R1), 3), round(float(R0), 3))
        # (A.9): the suprema 12 (k^2 + 3)/(k^2 - 3) and 24 (k^2 + 3)/(k^2 - 3), attained at infinity, exactly
        a9 = sp.simplify(sp.simplify(r**4*V/mu).subs(r, sp.sqrt(mu/xv)))
        a9b = sp.simplify(sp.simplify(r**3*D(r**2*V, r)/mu).subs(r, sp.sqrt(mu/xv)))
        s9, s9b = sp.Rational(12*(K2 + 3), K2 - 3), sp.Rational(24*(K2 + 3), K2 - 3)
        exact9 = (sp.limit(a9, xv, 0) == -s9 and sp.limit(a9b, xv, 0) == s9b
                  and all(nonneg_01(e) for e in (s9 + a9, s9 - a9, s9b - a9b, s9b + a9b)))
        # (A.3): r^2 (k^2/r^2 + V_phi) decreases in x = mu/r^2, so its minimum is the horizon's value, exactly
        Kc = K2 if control != 2 else 3
        a3 = sp.simplify(sp.simplify(r**2*(Kc/r**2 + v_phi(Kc))).subs(r, sp.sqrt(mu/xv)))
        da3 = sp.fraction(sp.together(sp.diff(a3, xv)))
        decreasing = (not da3[0].is_zero and sp.Poly(da3[0], xv).count_roots(0, 1) == 0
                      and sp.Poly(da3[1], xv).count_roots(0, 1) == 0
                      and (da3[0]/da3[1]).subs(xv, sp.Rational(1, 2)) < 0)
        a3min = sp.nsimplify(a3.subs(xv, 1))
        chk("k^2 = %d: B_1 >= (1/4)(2-p)(k^2 - 5/4) for r >= %.3f r_h, B_0 >= (1/4)(2-p)(k^2 + 3/4) for r >= %.3f r_h "
            "(p in [1/10, 19/10], the grid complete: affine in p); (A.9): r^4|V_phi|/mu <= %s = %.3f, r^3|d_r(r^2 "
            "V_phi)|/mu <= %s = %.3f, at infinity; (A.3): min r^2 (k^2/r^2 + V_phi) = %s, at the horizon"
            % (K2, radii[K2][0], radii[K2][1], s9, float(s9), s9b, float(s9b), a3min),
            affine and radii[K2] == PINNED[K2] and exact9 and decreasing and a3min == A3MIN[K2])
    lim = sp.limit(v_phi(kk**2), kk, sp.oo)
    chk("V_phi -> -12 mu/r^4 as k -> oo (the uniformity in l, his lim V_Z = -8 M/r^3)",
        sp.simplify(lim + 12*mu/r**4) == 0)
    return chk.ok


def h4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    v0c = 0 if control == 2 else sp.Rational(3, 4)          # control 2: the radiation field's (3/4)/r^2 dropped
    B0 = bulk_poly(sp.Integer(0), kk**2 + sp.Rational(3, 4), 0, v0c).subs(kk, 0)
    Vf = sp.Function("V")(r)
    Vcal, A, B, C = commuted(5, 1, Vf)
    v0 = sp.limit((Vcal*r**2).subs(Vf, 0).subs(kk, 0), r, sp.oo)
    v1 = sp.limit((-B/f5*r**2).subs(Vf, 0).subs(kk, 0), r, sp.oo)
    chk("l = 0, from H1's equation: V_inf = 3/4 and V1_inf = -5/4 < 0, so (A.8) fails for the commuted potential",
        v0 == sp.Rational(3, 4) and v1 == -sp.Rational(5, 4))
    # B_0 at l = 0: ((2-p)/2)(3/4) + (9/8)(4-p) x; negative for p > 2 once x < 3(p - 2)/(4(4 - p))... in r: r^2 > 3(4-p)
    # mu/(4(p-2)) <=> x < 4(p-2)/(3(4-p))
    sols = sp.solve(B0, xv)
    x0 = sols[0] if len(sols) == 1 else sp.nan
    good = len(sols) == 1 and sp.simplify(x0 - (p - 2)/(3*(4 - p))) == 0
    for pv in (sp.Rational(5, 2), 3, sp.Rational(13, 4)) if good else ():           # x_0 = 1/9, 1/3, 5/9
        good &= B0.subs({p: pv, xv: x0.subs(p, pv)/2}) < 0 and B0.subs({p: pv, xv: 1}) > 0
    chk("l = 0, five dimensions: B_0 = (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 < 0 for p > 2 once r^2 > 3(4 - p) mu/(p - 2): "
        "the hierarchy stops at p < 2 and A.6 (1)'s p < 4 does not transcribe", good)
    # four dimensions at l = 0, the control: Vcal = 2M/r^3 (V = 0), v_inf = 0, measure r^2: the Psi^2 bulk is -(1/2)
    # r^-2 d_r(r^p 2M/r^3) = (3 - p) M r^(p-6), positive for p < 3
    Vc4 = 2*mu/r**3
    bulk4 = sp.simplify(-r**(6 - p)/2*D(r**p*Vc4, r)/r**2)
    want4 = (3 - p)*mu if control != 1 else -(3 - p)*mu
    chk("four dimensions, l = 0: the Psi^2 bulk is (3 - p) M r^(p-6), positive for p < 3 (V_inf = 0 there: why his "
        "Proposition A.6 (1) has room past p = 2)", sp.simplify(bulk4 - want4) == 0)
    return chk.ok


CHECKS = [("H1 the commuted equation: Psi_1 = f^-1 r^2 L Psi, Vcal_1 = Vcal - 2/r^2 + 12 mu/r^4, V1_inf = k^2 - 5/4", h1,
           1),
          ("H2 the p-current identity for Psi_1: the first-order term adds 2(1 - 2 mu/r^2) to the |L Psi_1|^2 bulk", h2,
           1),
          ("H3 (A.7)-(A.9), (A.3), (A.5) in five dimensions: B_1, B_0 and the radii R_1, R_0 at four modes", h3, 2),
          ("H4 the l = 0 obstruction: V1_inf = -5/4, and B_0 < 0 for p > 2 at large r", h4, 2)]


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
    print(f"hierarchy5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"hierarchy5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
