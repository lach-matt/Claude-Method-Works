#!/usr/bin/env python3
"""lzerorate5.py -- the l = 0 sector's rapid decay on five-dimensional Tangherlini by another route: the commuted r^p
hierarchy at l = 0 with the negative commuted potential absorbed by a Hardy inequality along the null leaf, the base
hierarchy at l = 0 without an angular term to borrow, and the cut-off source of P-hat (N1STAR-PROOF.md section 10.11;
D53).  Labels: computed (exact, sympy), deduced, READ.

Section 10.9 found [Hun19] Proposition A.6(1) obstructed at l = 0 in five dimensions: the commuted potential has
V1_inf = -5/4 (H4), so his condition (A.8) fails, and with it 10.8's input for S_W.  (A.8) asks for more than the
hierarchy needs.  At p < 2 the flux of V1_inf at null infinity vanishes, and the only place V1_inf enters is the
Psi_1^2 bulk, -(5/8)(2 - p) r^(p-6) Psi_1^2 at leading order; the commuted current's own |nabla_L Psi_1|^2 bulk, (2 +
p/2) r^(p-4) at leading order, pays for it through the Hardy inequality on each outgoing leaf when (2 + p/2)(2 - p) >
5/2, that is for p < 1.  So the commuted hierarchy runs at l = 0 on p in [delta, 1 - delta], one step where [Hun19]
has two, and S_W decays at (1 + tau/sqrt mu)^(-3+p+3 delta): enough to pay the factor (1 + tau/sqrt mu)^2 that 10.8's
P-hat carries on [b r_h, 2 b r_h], with one power to spare where his has two.  Notation as hierarchy5.py: Psi = r^(3/2)
u the radiation field, L Lbar Psi = -f Vcal Psi, Psi_1 := f^-1 r^2 L Psi, L = d_t + f d_r, f = 1 - mu/r^2, x = mu/r^2.

  Y1 (computed, exact) The l = 0 currents.  hierarchy5.py's commuted equation at k = 0, V = 0: Vcal = (3/4 + 9 mu/(4
     r^2))/r^2, Vcal_1 = -5/(4 r^2) + 57 mu/(4 r^4), the first-order coefficient -(2/r)(1 - 2 mu/r^2) and the Psi term
     C = 9 mu f/(2 r^3); the base current of (10.7) on Psi (no first-order term),
         div J^p[Psi] = r^(p-4) f^-2 (p f/2 - mu/r^2) |L Psi|^2 + ((2 - p)/2) r^(p-6) V_inf Psi^2
                        + r^(p-3) f^-1 L Psi (Vcal - V_inf/r^2) Psi,
     which (10.35) extends by 2 (1 - 2 mu/r^2); and (10.35) at k = 0 on an outgoing leaf u = const of r >= R_null, where
     the measure r^3 dt dr is r^3 du dr and L = f d_r along the leaf, w := Psi_1 there: after H2's integration by
     parts the bulk density is
         r^(p-1) c w'^2 + r^(p-3) B_1 w^2 - (9 mu/2) r^(p-3) Psi w',
         c = p f/2 + 2 - 5 mu/r^2,   B_1 = -(5/8)(2 - p) + (57/8)(4 - p) mu/r^2,
     the f's cancelling exactly.  Controls: the base |L Psi|^2 coefficient claimed p f/2 (the - mu/r^2 dropped); V1_inf
     claimed +5/4.
  Y2 (computed, exact) The Hardy step.  d_r(r^(p-2) w^2) = (p - 2) r^(p-3) w^2 + 2 r^(p-2) w w', so for w vanishing at
     R and p < 2, A := int_R^oo r^(p-3) w^2 dr and B := int_R^oo r^(p-1) w'^2 dr obey (2 - p) A <= 2 (A B)^(1/2), A <=
     4 B/(2 - p)^2 (deduced; checked on w = 1 - R/r at p = 1/2, where A/B = 8/15 against 16/9, and 4/9, the
     control's constant, fails).  With c_R := 2 + p/2 - (5 + p/2) x_R and Q := c_R (2 - p) - 5/2, exactly
         c_R B - (5/8)(2 - p) A = (Q/(2 (2 - p))) B + (Q (2 - p)/8) A + kappa (4 B/(2 - p)^2 - A),
         kappa = (2 - p)(5 + Q)/8,
     so the bulk is at least (Q/(2 (2 - p))) B + (Q (2 - p)/8) A when Q > 0; and the bad term is a perfect square away:
     eps a^2 - (9/2) a b + (81/(16 eps)) b^2 = (eps^(1/2) a - (9/4) eps^(-1/2) b)^2.  Control: the Hardy constant
     claimed 1/(2 - p)^2, which w = 1 - R/r refutes.
  Y3 (computed, exact) The window.  Q(p, x) = (2 + p/2 - (5 + p/2) x)(2 - p) - 5/2 has Q(p, 0) = (1 - p)(3 + p)/2,
     decreases in x on p < 2, and is concave in p, so on p in [delta, 1 - delta] = [1/10, 9/10] and r >= R_null = 10
     r_h (x <= 1/100, the record's R_null of 10.9 (iii), where f >= 99/100) its minimum is at a corner: Q(1/10, 1/100)
     = 25981/20000 and Q(9/10, 1/100) = 2701/20000 > 0; c is least at R_null and B_1 >= -(5/8)(2 - p) on p <= 4.  The
     window closes at p = 0.9716 at x = 1/100 and at p = 1 at x = 0; for general delta in (0, 1/10], R_null >= 3
     r_h/delta^(1/2) (x_R <= delta/9) keeps Q > 0 at both corners, exactly (Q(1 - delta, delta/9) = delta (25 - 19
     delta + delta^2)/18, vanishing with delta).  At leading order the condition is (4 +
     p)(2 - p) > -4 V1_inf, which needs V1_inf > -2: open on p < 1 at the five-dimensional l = 0 value -5/4 and
     empty at the four-dimensional one, -2 (H1), so the window is the odd dimension's.  Controls: R_null = 5 r_h,
     where Q(9/10, 1/25) < 0; and p = 1 at x = 0, where Q = 0.
  Y4 (computed, exact) The base hierarchy at l = 0 needs no angular term.  B_0 = (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 >=
     (3/8)(2 - p) > 0 for p < 2 (hierarchy5.py's bulk at k = 0), and the T-energy density of u on the leaf, r^3 |L
     u|^2 = |L Psi - (3/2)(f/r) Psi|^2, is at most 12 times the p = 1 bulk density f^-2 ((1 - 3 x)/2) |L Psi|^2 +
     r^-2 B_0 Psi^2 on x <= 1/100, exactly (the 2 x 2 form positive definite, Sturm): the radiation field's own
     (3/4)/r^2 does at l = 0 what k^2 >= 8 does in Proposition 10.5 (iii).  Control: the (3/4)/r^2 dropped, which
     makes the form indefinite at large r.
  Y5 (computed, exact) The cut-off source of P-hat := P + eta (u + r) S_W/2 (10.8, his (8.6)), u = t - r_*, for box_s
     S_W = 0 at l = 0 and eta = eta(r):
         box_s (eta w S_W/2) = (w/2)(S_W box_s eta + 2 f eta' d_r S_W) + eta (S_W box_s w/2 + grad w . grad S_W)
                               + f eta' (d_r w) S_W,                       w := u + r,
     with box_s w = -mu/r^3 and grad w . grad S_W = -f^-1 d_t S_W - (mu/r^2) d_r S_W, so where eta = 1 the source is
     (10.26) (Z5 re-derived), and the terms carrying the growing w are S_W and d_r S_W only, on the support of eta':
     his Lemma 8.3's middle region, (1 + tau/sqrt mu) |(sqrt mu d)^{<= 1} S_W|, in five dimensions.  Control: w = u,
     whose eta = 1 source carries d_r S_W with weight 1 instead of mu/r^2.

READ (alphaXiv, 2026-10-21).  [Hun19] section 8 pp. 58-70 in full (Theorem 8.1, Propositions 8.2 and 8.4, Lemma 8.3,
(8.2)-(8.39), Lemmas 8.5-8.6 and the proof of Theorem 8.1, Theorem 8.7), Proposition A.6 (A.12)-(A.14) and Appendix B
pp. 73-75.  [Sch13] Theorem 1 (1.9)-(1.10) p. 5, Proposition 4.1 (4.4) pp. 19-20, Corollary 4.3, (4.64), (4.67), (4.71)
pp. 38-39 and Corollary 4.18 p. 43, the proof of Proposition 4.1 (4.76)-(4.92) pp. 44-52, Propositions 4.21-4.22 pp.
53-54, (5.8)-(5.22) pp. 57-62.

sympy.  python3 lzerorate5.py [--selftest | --mutants]   (about forty seconds; --verbose lists every sub-check)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hierarchy5 as HI                                                               # noqa: E402

t, r, mu, kk, p, xv = HI.t, HI.r, HI.mu, HI.kk, HI.p, HI.xv
f = HI.f5
D = sp.diff
Checklist = HI.Checklist
DELTA = HI.DELTA                                                                      # 1/10
XR = sp.Rational(1, 100)                                                              # R_null = 10 r_h
LAM = 12                                                                              # Y4's constant


def q_of(pv, xr):
    """Y3's Q(p, x_R) = c_R (2 - p) - 5/2"""
    return (2 + pv/2 - (5 + pv/2)*xr)*(2 - pv) - sp.Rational(5, 2)


# ------------------------------------------------------------------------------------------------- Y1
def y1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Vcal, A, B, C = HI.commuted(5, 1, sp.Integer(0))
    Vcal, A, B, C = [sp.simplify(e.subs(kk, 0)) for e in (Vcal, A, B, C)]
    Vcal1 = sp.simplify(-B/f)
    v1 = sp.limit(Vcal1*r**2, r, sp.oo)
    v1want = -sp.Rational(5, 4) if control != 2 else sp.Rational(5, 4)
    chk("k = 0: Vcal = (3/4 + 9 mu/(4 r^2))/r^2, Vcal_1 = -5/(4 r^2) + 57 mu/(4 r^4), V1_inf = -5/4",
        sp.simplify(Vcal - (sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2) == 0
        and sp.simplify(Vcal1 - (-sp.Rational(5, 4)/r**2 + sp.Rational(57, 4)*mu/r**4)) == 0 and v1 == v1want)
    chk("k = 0: first-order coefficient -(2/r)(1 - 2 mu/r^2), Psi term C = 9 mu f/(2 r^3)",
        sp.simplify(A + 2/r*(1 - 2*mu/r**2)) == 0 and sp.simplify(C - 9*mu*f/(2*r**3)) == 0)
    W, S, Vw, vinf, div = HI._current_setup()
    LW = D(W, t) + f*D(W, r)
    d0 = sp.expand(div.subs(S, 0).doit())
    co = p*f/2 - (mu/r**2 if control != 1 else 0)
    want = (r**(p - 4)/f**2*co*LW**2 + (2 - p)/2*r**(p - 6)*vinf*W**2
            + r**(p - 3)/f*LW*(Vw - vinf/r**2)*W)
    chk("the base current: div J^p[Psi] = r^(p-4) f^-2 (p f/2 - mu/r^2)|L Psi|^2 + ((2-p)/2) r^(p-6) V_inf Psi^2 + "
        "r^(p-3) f^-1 L Psi (Vcal - V_inf/r^2) Psi", sp.simplify(sp.expand(d0 - want)) == 0)
    # (10.35) at k = 0 on the leaf: L Psi_1 = f w', measure r^3
    B1 = HI.bulk_poly(sp.Integer(0), kk**2 - sp.Rational(5, 4), -2).subs(kk, 0)
    chk("B_1 at k = 0 = -(5/8)(2 - p) + (57/8)(4 - p) mu/r^2",
        sp.simplify(B1 - (-sp.Rational(5, 8)*(2 - p) + sp.Rational(57, 8)*(4 - p)*xv)) == 0)
    wp, w, Ps = sp.symbols("wp w Ps")
    c35 = p*f/2 + 2 - 5*mu/r**2
    dens = (r**(p - 4)/f**2*c35*(f*wp)**2 + r**(p - 6)*B1.subs(xv, mu/r**2)*w**2
            + r**(p - 3)/f*(f*wp)*(-C/f*Ps))*r**3
    leaf = (r**(p - 1)*c35*wp**2 + r**(p - 3)*(-sp.Rational(5, 8)*(2 - p)
                                                 + sp.Rational(57, 8)*(4 - p)*mu/r**2)*w**2
            - sp.Rational(9, 2)*mu*r**(p - 3)*Ps*wp)
    chk("(10.35) at k = 0 on an outgoing leaf: L Psi_1 = f w' and the measure r^3 du dr turn its density into "
        "r^(p-1) c w'^2 + r^(p-3) B_1 w^2 - (9 mu/2) r^(p-3) Psi w', the f's cancelling (c and B_1 as above)",
        sp.simplify(sp.expand(dens - leaf)) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y2
def y2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    wf = sp.Function("w")(r)
    chk("d_r(r^(p-2) w^2) = (p - 2) r^(p-3) w^2 + 2 r^(p-2) w w'",
        sp.simplify(D(r**(p - 2)*wf**2, r) - ((p - 2)*r**(p - 3)*wf**2 + 2*r**(p - 2)*wf*D(wf, r))) == 0)
    hc = 4 if control != 1 else 1                                                     # control 1: constant 1/(2-p)^2
    R = sp.Symbol("R", positive=True)
    wt = 1 - R/r
    pv = sp.Rational(1, 2)
    Aw = sp.integrate(r**(pv - 3)*wt**2, (r, R, sp.oo))
    Bw = sp.integrate(r**(pv - 1)*D(wt, r)**2, (r, R, sp.oo))
    ratio = sp.simplify(Aw/Bw)
    chk("Hardy on the leaf, A <= (%d/(2 - p)^2) B, on w = 1 - R/r at p = 1/2: A/B = 8/15" % hc,
        ratio == sp.Rational(8, 15) and ratio <= sp.Rational(hc)/(2 - pv)**2)
    Am, Bm, xr = sp.symbols("A B x_R", nonnegative=True)
    cR = 2 + p/2 - (5 + p/2)*xr
    Q = cR*(2 - p) - sp.Rational(5, 2)
    kap = (2 - p)*(5 + Q)/8
    lhs = cR*Bm - sp.Rational(5, 8)*(2 - p)*Am
    rhs = Q/(2*(2 - p))*Bm + Q*(2 - p)/8*Am + kap*(hc*Bm/(2 - p)**2 - Am)
    chk("c_R B - (5/8)(2-p) A = (Q/(2(2-p))) B + (Q(2-p)/8) A + kappa (4 B/(2-p)^2 - A), kappa = (2-p)(5+Q)/8",
        sp.simplify(sp.expand(lhs - rhs)) == 0)
    a, b, eps = sp.symbols("a b epsilon", positive=True)
    chk("eps a^2 - (9/2) a b + (81/(16 eps)) b^2 = (eps^(1/2) a - (9/4) eps^(-1/2) b)^2",
        sp.simplify(sp.expand(eps*a**2 - sp.Rational(9, 2)*a*b + 81/(16*eps)*b**2
                              - (sp.sqrt(eps)*a - sp.Rational(9, 4)/sp.sqrt(eps)*b)**2)) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y3
def y3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Q = q_of(p, xv)
    chk("Q(p, 0) = (1 - p)(3 + p)/2", sp.simplify(Q.subs(xv, 0) - (1 - p)*(3 + p)/2) == 0)
    chk("d_x Q = -(5 + p/2)(2 - p) < 0 on p < 2, d_p^2 Q = -(1 - x) < 0",
        sp.simplify(D(Q, xv) + (5 + p/2)*(2 - p)) == 0 and sp.simplify(D(Q, p, 2) + (1 - xv)) == 0)
    xr = XR if control != 1 else sp.Rational(1, 25)                                 # control 1: R_null = 5 r_h
    lo, hi = DELTA, 1 - DELTA
    qlo, qhi = q_of(lo, xr), q_of(hi, xr)
    chk("Q(1/10, 1/100) = 25981/20000, Q(9/10, 1/100) = 2701/20000, both > 0: the window [delta, 1 - delta] at R_null = "
        "10 r_h" if control != 1 else "the window at R_null = 5 r_h",
        qlo > 0 and qhi > 0 and (control == 1 or (qlo == sp.Rational(25981, 20000)
                                                   and qhi == sp.Rational(2701, 20000))))
    root = [z for z in sp.Poly(q_of(p, XR), p).nroots(n=20) if 0 < z < 2]
    chk("the window closes at p = 0.9716 at x = 1/100", len(root) == 1 and abs(root[0] - 0.9716) < 1e-4)
    pend = 1 if control == 2 else hi                                                  # control 2: p = 1 at x = 0
    chk("at x = 0 the window is open at p = 9/10 (Q = 39/200)",
        q_of(pend, 0) > 0 and (control == 2 or q_of(pend, 0) == sp.Rational(39, 200)))
    c = p*(1 - xv)/2 + 2 - 5*xv
    chk("c = p f/2 + 2 - 5 x decreases in x (least at R_null)", sp.simplify(D(c, xv) + (p/2 + 5)) == 0)
    B1 = HI.bulk_poly(sp.Integer(0), kk**2 - sp.Rational(5, 4), -2).subs(kk, 0)
    chk("B_1 + (5/8)(2 - p) = (57/8)(4 - p) x, so B_1 >= -(5/8)(2 - p) on p <= 4",
        sp.simplify(B1 + sp.Rational(5, 8)*(2 - p) - sp.Rational(57, 8)*(4 - p)*xv) == 0)
    dl = sp.Symbol("delta", positive=True)
    corners = [sp.Poly(sp.cancel(sp.expand(q_of(pc, dl/9)*20)/dl**k), dl) for pc, k in ((dl, 0), (1 - dl, 1))]
    chk("general delta in (0, 1/10]: Q(delta, delta/9) > 0 and Q(1 - delta, delta/9) > 0 (R_null >= 3 r_h/delta^(1/2))",
        all(P.count_roots(0, DELTA) == 0 and P.eval(DELTA) > 0 for P in corners)
        and sp.expand(q_of(1 - dl, dl/9)).subs(dl, 0) == 0)
    chk("Q(1 - delta, delta/9) = delta (25 - 19 delta + delta^2)/18",
        sp.simplify(q_of(1 - dl, dl/9) - dl*(25 - 19*dl + dl**2)/18) == 0)
    # the leading-order condition for a general V1_inf: (2 + p/2)(2 - p)^2/4 > -((2 - p)/2) V1  <=>  (4 + p)(2 - p) >
    # -4 V1; at the five-dimensional l = 0 value -5/4 it is p < 1, at the four-dimensional one, -2 (H1), empty
    V1 = sp.Symbol("V1")
    lead = sp.expand((4 + p)*(2 - p) + 4*V1)
    open5 = sp.solve_univariate_inequality(lead.subs(V1, -sp.Rational(5, 4)) > 0, p, relational=False)
    open4 = sp.solve_univariate_inequality(lead.subs(V1, -2) > 0, p, relational=False)
    chk("leading order: (4 + p)(2 - p) > -4 V1_inf; at -5/4 (five dimensions, l = 0) on p < 1, at -2 (four "
        "dimensions, l = 0) for no p > 0", open5.intersect(sp.Interval.open(0, 2)) == sp.Interval.open(0, 1)
        and open4.intersect(sp.Interval.open(0, 2)) == sp.EmptySet)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y4
def _interval_pos(e, a, b):
    """e (rational in x) > 0 on [a, b], exactly: no root of numerator or denominator there and positive at a"""
    nu, de = sp.fraction(sp.together(sp.expand(e)))
    ok = True
    for P in (nu, de):
        Pp = sp.Poly(sp.expand(P), xv)
        ok &= Pp.count_roots(a, b) == 0
    return bool(ok and e.subs(xv, a) > 0)


def y4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    v0c = 0 if control == 1 else sp.Rational(3, 4)                                    # control 1: (3/4)/r^2 dropped
    B0 = HI.bulk_poly(sp.Integer(0), kk**2 + v0c, 0, v0c).subs(kk, 0)
    if control != 1:
        chk("B_0 at k = 0 = (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 >= (3/8)(2 - p)",
            sp.simplify(B0 - (sp.Rational(3, 8)*(2 - p) + sp.Rational(9, 8)*(4 - p)*xv)) == 0)
    fx = 1 - xv
    m11 = LAM*(1 - 3*xv)/(2*fx**2) - 1
    m12 = 3*fx/2
    m22 = LAM*B0.subs(p, 1) - sp.Rational(9, 4)*fx**2
    det = sp.together(m11*m22 - m12**2)
    good = _interval_pos(m11, 0, XR) and _interval_pos(det, 0, XR) if control != 1 else \
        _interval_pos(m11, sp.Rational(1, 10**6), XR) and _interval_pos(det, sp.Rational(1, 10**6), XR)
    chk("r^3 |L u|^2 <= 12 (f^-2 ((1 - 3x)/2) |L Psi|^2 + r^-2 B_0 Psi^2) at p = 1 on x <= 1/100 (positive definite)",
        good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y5
def y5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    S = sp.Function("S")(t, r)
    eta = sp.Function("eta")(r)
    rstar = sp.Function("rs")(r)                                                      # r_*' = 1/f
    box = lambda e: -D(e, t, 2)/f + D(r**3*f*D(e, r), r)/r**3                        # noqa: E731
    w = t - rstar + (r if control != 1 else 0)                                        # control 1: w = u
    sub = {D(rstar, r): 1/f, D(rstar, r, 2): D(1/f, r)}

    def red(e):
        e = sp.expand(e.doit())
        e = e.subs(D(rstar, r, 2), D(1/f, r)).subs(D(rstar, r), 1/f)
        return sp.expand(e.subs(D(S, t, 2), f*D(r**3*f*D(S, r), r)/r**3).doit())  # box_s S = 0
    full = red(box(eta*w*S/2))
    gw = sp.expand(red(-D(w, t)*D(S, t)/f + f*D(w, r)*D(S, r)))
    boxw = sp.simplify(red(box(w)))
    want = (w/2*(S*box(eta) + 2*f*D(eta, r)*D(S, r)) + eta*(S*boxw/2 + gw) + f*D(eta, r)*D(w, r)*S)
    chk("box_s(eta w S/2) = (w/2)(S box_s eta + 2 f eta' d_r S) + eta (S box_s w/2 + grad w.grad S) + f eta' (d_r w) S",
        sp.simplify(full - red(want)) == 0)
    if control != 1:
        chk("box_s w = -mu/r^3, grad w.grad S = -f^-1 d_t S - (mu/r^2) d_r S",
            sp.simplify(boxw + mu/r**3) == 0 and sp.simplify(gw - (-D(S, t)/f - mu/r**2*D(S, r))) == 0)
    # where eta = 1: box_s P-hat = d_t S + box_s(w S/2) = (10.26)
    LS = D(S, t) + f*D(S, r)
    at1 = sp.expand(D(S, t) + S*boxw/2 + gw)
    chk("eta = 1: box_s P-hat = -(mu/(r^2 f)) L S - (mu/(2 r^3)) S, (10.26)",
        sp.simplify(at1 - (-mu/(r**2*f)*LS - mu/(2*r**3)*S)) == 0)
    grow = sp.expand(S*box(eta) + 2*f*D(eta, r)*D(S, r))
    chk("the coefficient of w carries S and d_r S only, on the support of eta' (no d_t S)",
        not grow.has(D(S, t)) and sp.simplify(grow.subs(eta, 1).doit()) == 0)
    return chk.ok


CHECKS = [("Y1 the l = 0 currents: Vcal_1 = -5/(4r^2) + 57 mu/(4r^4), the base current, (10.35) on the leaf", y1, 2),
          ("Y2 the Hardy step on the leaf and the absorption identity", y2, 1),
          ("Y3 the window: Q(p, x) > 0 on [1/10, 9/10] x [0, 1/100]; Q(p, 0) = (1 - p)(3 + p)/2", y3, 2),
          ("Y4 the base hierarchy at l = 0: B_0 > 0 and the T-energy density dominated at p = 1", y4, 1),
          ("Y5 P-hat's cut-off source: the growing terms carry S_W and d_r S_W only; (10.26) where eta = 1", y5, 1)]


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
    print(f"lzerorate5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"lzerorate5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
