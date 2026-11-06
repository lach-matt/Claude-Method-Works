"""r6settle5.py -- SETTLE-GLAM5 round 6: computational support for the round-5 reader's minors m1-m3 and m5 and for
the claims its list says no check exercises (the window and F_4 are in r6sigma5.py, R6-D's mathematics in
r6edits5.py, the flux sign in r5settle5.py F1-F1x).

  X (m1: the exterior energy identity on a bounded region)
    X1 (exact, sympy) the energy identity on the bounded exterior region D = {t1 <= t <= t2, r >= R + 2(t - t1),
       t + r + 1/r <= V_*} of the flat radial model (measure r^3 dr; t1 = 0, t2 = 11/12, R = 1/2, V_* = 17/4, so the
       corners are rational): E(t2) + F_in + F_out = E(t1) - int int phi_t box phi r^3 for a polynomial phi, with
       F_in = int r^3 (phi_t^2 + phi_r^2 + phi_t phi_r) dt on the inner boundary (speed 2) and F_out = int r^3
       ((c/2)(phi_t^2 + phi_r^2) - phi_t phi_r) dt on {t + r + 1/r = V_*}, c := (1 - r^-2)^-1; the flux forms have the
       eigenvalues 1/2, 3/2 and (c - 1)/2, (c + 1)/2, all > 0 (exact): both lateral boundaries are future boundaries
       whose flux can be dropped. Control (the code mutated: the inner boundary at speed 1/2, timelike): the identity
       holds with that boundary but its flux form has the eigenvalue -1/4: no sign, nothing can be dropped.
    X2 (exact and sampled) on W the inner boundary {r - 2 t~ = c} of R5-B's exterior region: for |f'| <= 1/4,
       g_b0^-1(alpha, alpha) <= -7/4 for alpha = d(r - 2 t~) = (1 + 2 f') dr - 2 dt (exact, every mu >= 0), |alpha|_E^2
       <= 25/4, so (g_b0^-1 + delta)(alpha, alpha) < 0 for |delta|_op <= r^-2/2, r >= 2; alpha(d_t) = -2 < 0, so r - 2 t~
       decreases along future causal curves and the region lies to the past of that boundary. Sampled at 2000 points
       (r in [8, 800], random delta and f'). Control: with |f'| = 1 allowed the bound fails (alpha null at f' = 1/2,
       spacelike beyond).
    X3 (exact) V_* -> oo: for an explicit field with finite exterior energy the energy of the slice cut at
       {Phi <= V_*} increases with V_* to the full value (sympy limit), the monotone convergence of R5-B.
    X4 (exact) the uniform dyadic tail: with the exterior bound E(r >= rho) <= C lam^2 rho^-q at every sigma of
       [T, sigma_1] (q = 9 from the source degree 13/2: 2(13/2) - 4), the weighted tail is at most
       sum_j (2^(j+1) rho)^(2a) C lam^2 (2^(j-1) rho)^-q = C lam^2 2^(2a+q) rho^(2a-q) / (1 - 2^(2a-q)) (exact sum),
       finite exactly for a < q/2 and -> 0 as rho -> oo uniformly in sigma: the weighted energy is a uniform limit of
       continuous functions. [arithmetic: q entered from the degree count.] Control: q = 8 (F_4 with no source)
       gives a < 4, still above the window.
  Y (m2: the a priori decay behind Hardy, and Proposition R5.2's uniformity in sigma)
    Y1 (exact, sympy) S1 needs no Hardy: along a ray of Sigma~_sigma, d/dr (d_c psi) for any psi equals
       r^-1 d_c(Z psi) - r^-1 (t - v1) d_c(d_t psi) + f' d_c(d_t psi) plus first derivatives of psi with
       coefficients bounded by C/r on W (|t - v1| <= r): no undifferentiated psi and no other second derivative
       (generic psi; f generic). Control (the term r^-1 d_c(Z psi) dropped): second derivatives remain.
    Y2 (sampled, mpmath) for phi -> 0 at infinity with int r^(2a+3) phi'^2 < oo: r^(2a+2) phi(r)^2 <=
       (2a + 2)^-1 int_r^oo s^(2a+3) phi'^2 ds (Cauchy-Schwarz on phi = -int phi'), so the Hardy boundary term
       vanishes at every R' -> oo, and Hardy holds on [R, oo): 24 random fields with log-periodic oscillation (not
       power laws), a in (0, 4), R in {2, 20}, R' in {10, 100, 1000}. Control (exact): phi = c + r^-(a+2), c != 0
       (finite derivative energy, nonzero limit): int r^(2a+1) phi^2 = oo and R'^(2a+2) phi^2 -> oo: Hardy fails,
       which is why the limit must be shown to vanish first.
    Y3 (exact, sympy) Proposition R5.2's argument on a model family on {v >= v1, t <= 0} (f = 0, t~ = t): h'(t, r) =
       B(v) r^-2 + D r^(-1/2-a0) cos(t/r), B(v) = (3/10)/(1 + v^2), D = 1/100, a0 = 1/4, with |d h'| <= C r^(-3/2-a0)
       uniformly in t and h'|_N -> 0; the limit c(sigma) = lim_(r -> oo) h'(sigma, r) is the same for sigma = 0, -3,
       -100 and equals 0, and |h'(sigma, r)| <= C r^(-1/2-a0) with C independent of sigma (exact at the three sigma).
       Controls: h' + c0 (c0 = 1/60: derivatives unchanged, |h'| <= 1/50 kept) violates h'|_N -> 0 and has c = c0 !=
       0; h' + c0 t/(1 + t^2) has a sigma-dependent limit, and its |d_t h'| does not decay in r (the uniform bound
       fails).
  M (m3, exact) Lemma R4.5 at every a in (0, 7/2): w_a = (u* - u)^(2a) <= w_a' for a <= a' since u* - u >= 1
     (r5settle5 E1), so its fluxes are monotone in a; and its proof's three inputs hold on (0, 7/2) (r6sigma5 W2, W7).
     Control: with u* - u allowed below 1 the monotonicity fails.
  L ("+2 for Lemma 9.3", exact) Lemma 9.3(a) bounds sup |f| by sum_(i <= 3) ||d_r^i f||; on an oscillating field
     f = A(r) sin(v/lam) the ratio ||d_r^3 f||^2/||d_r f||^2 -> lam^-4 (the limit of lam^4 times it is 1): the sup
     bound costs lam^-2 beyond the energy level ||d f||, which is Proposition R5.4's "+2"; with it the stage recursion
     of r5settle5 A gives B_J = 3J - 9. Control: a cost of 3 (Sobolev to order 4) gives a different B_J.
  A0 (computed, 40 digits) the coefficient list of r5settle5 A from g_b0: the decay degrees of g_b0^-1 - eta,
     d g_b0, Gamma[g_b0], d d g_b0, d Gamma[g_b0] and Gamma Gamma along a ray are 2, 3, 3, 4, 4, 6, which with (0.2)'s
     derivative counts (two on u through g^ab, one through Gamma[g0], none through d d g0 and (d g0)^2) is
     r5settle5.COEFS = [(0, 2), (2, 2), (3, 1), (4, 0), (6, 0)]. Control: the flat metric gives no coefficients.
  T (m5, exact and sampled) Theorem P's use of Lemmas 1.1(e) and 2.3 after D623 (N1STAR-PROOF.md 0.3: eps1 <
     min(s0, mu0/a^2 - 1)): on P the margin of Lemma 9.1(f) is |g^-1 - g0^-1| <= eps_P t^(-5/4), a bound on the
     inverse. g0^-1(dtau, dtau) = -1 - m (m := mu/r^2), so (g0^-1 + delta)(dtau, dtau) <= -1 + eps_P; the least
     absolute eigenvalue of g0^-1 is sqrt(1 + m^2) - m =: s(m) (exact), so for eps_P < s(m*) every such g^-1 is
     invertible with |g| <= (s(m*) - eps_P)^-1 (Weyl); and {r = a} stays spacelike for eps_P < mu0/a^2 - 1. Lemma 9.5's
     constants therefore come from the inverse margin with eps_P below those two numbers, which "there is eps_P > 0"
     allows; D623's s0 is the same mechanism on Omega. Sampled (2000 points, |delta|_op = 0.99 of the threshold).
     Control: |delta|_op = s(m) makes g^-1 singular (exact).
Labels: computed (exact sympy; X2, Y2, T sampled in floating point or mpmath).

    python3 checks/r6settle5.py     (4 minutes alone, 27 beside five other programs, on this loaded machine)
"""
import os
import random
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r5settle5 as R5  # noqa: E402

FAIL = []
print = R5.print
Q = sp.Rational


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


# ================================================================ X

def flux_identity(speed):
    t, r = sp.symbols("t r", positive=True)
    t1, t2, R, Vs = Q(0), Q(11, 12), Q(1, 2), Q(17, 4)
    phi = 1 + t*r - r**2/7 + t**2*r/3 + r**3/40 - t**3/5
    pt, pr = sp.diff(phi, t), sp.diff(phi, r)
    box = -sp.diff(phi, t, 2) + sp.diff(phi, r, 2) + 3*pr/r
    e = (pt**2 + pr**2)/2
    rin = lambda tt: R + speed*(tt - t1)
    rout1, rout2 = Q(4), Q(3)          # r + 1/r = V_* - t at t1 and t2
    assert rout1 + 1/rout1 == Vs - t1 and rout2 + 1/rout2 == Vs - t2
    E1 = sp.integrate((e*r**3).subs(t, t1), (r, rin(t1), rout1))
    E2 = sp.integrate((e*r**3).subs(t, t2), (r, rin(t2), rout2))
    fin_dens = r**3*(e*speed + pt*pr)
    F_in = sp.integrate(fin_dens.subs(r, rin(t)), (t, t1, t2))
    # the outer boundary parametrised by r: t = V_* - r - 1/r, dt = -(1 - r^-2) dr; there r_out' = -c
    c = 1/(1 - r**-2)
    fout_dens = r**3*(c*e - pt*pr)
    F_out = sp.integrate((fout_dens*(1 - r**-2)).subs(t, Vs - r - 1/r), (r, rout2, rout1))
    # the bulk over D: for each t, r from rin(t) to rout(t); rout is algebraic, so integrate in t at fixed r instead:
    # D = {r in [R, 4]} x {t in [t1, min(t2, (r - R)/speed + t1, V_* - r - 1/r)]}
    tb = sp.Symbol("tb")
    inner = sp.integrate(sp.expand(pt*box*r**3), (t, t1, tb))
    rc_in = rin(t2)                       # inner boundary's r at t2
    # pieces in r: [R, rc_in]: t up to (r - R)/speed; [rc_in, 3]: t up to t2; [3, 4]: t up to V_* - r - 1/r
    b1 = sp.integrate(inner.subs(tb, (r - R)/speed + t1), (r, R, rc_in))
    b2 = sp.integrate(inner.subs(tb, t2), (r, rc_in, rout2))
    b3 = sp.integrate(sp.expand(inner.subs(tb, Vs - r - 1/r)), (r, rout2, rout1))
    bulk = b1 + b2 + b3
    lhs, rhs = E2 + F_in + F_out, E1 - bulk
    form_in = sp.Matrix([[speed/2, Q(1, 2)], [Q(1, 2), speed/2]])
    return sp.simplify(lhs - rhs) == 0, form_in.eigenvals(), sp.N(lhs, 15)


def part_x():
    print("X  the exterior energy identity on a bounded region, and the continuity of the energy (m1)")
    ok, ev_in, val = flux_identity(Q(2))
    r = sp.Symbol("r", positive=True)
    c = 1/(1 - r**-2)
    ev_out = sp.Matrix([[c/2, -Q(1, 2)], [-Q(1, 2), c/2]]).eigenvals()
    pos_out = all(sp.simplify(k - (c - 1)/2) == 0 or sp.simplify(k - (c + 1)/2) == 0 for k in ev_out) and \
        sp.simplify((c - 1)/2 - 1/(2*(r**2 - 1))) == 0
    check("X1 E(t2) + F_in + F_out = E(t1) - int int phi_t box phi r^3 on the bounded exterior region (exact); flux "
          "forms: inner eigenvalues 1/2, 3/2, outer (c - 1)/2 = 1/(2(r^2 - 1)) > 0 and (c + 1)/2", ok
          and set(ev_in) == {Q(1, 2), Q(3, 2)} and pos_out, f"E(t2) + fluxes = {val}; inner {list(ev_in)}")
    okc, ev_c, _ = flux_identity(Q(1, 2))
    check("X1' control (inner boundary at speed 1/2, timelike): the identity holds with it, but its flux form has the "
          "eigenvalue -1/4", okc and Q(-1, 4) in ev_c, str(list(ev_c)))
    # X2
    fp, m = sp.symbols("fp m", real=True)
    # the (t, r) block suffices: alpha has no angular part; g_b0^-1 = eta^-1 - m l l, l = (-1, xhat)
    alpha = sp.Matrix([-2, 1 + 2*fp])
    lvec = sp.Matrix([-1, 1])
    gform = (alpha.T*sp.diag(-1, 1)*alpha)[0] - m*((lvec.T*alpha)[0])**2
    from sympy.calculus.util import maximum
    mx = maximum(gform.subs(m, 0), fp, sp.Interval(-Q(1, 4), Q(1, 4)))
    mono = sp.diff(gform, m)
    okx2 = mx == -Q(7, 4) and sp.simplify(mono + (3 + 2*fp)**2) == 0
    rng = random.Random(61)
    worst, ctl = -1e9, -1e9
    for _ in range(2000):
        r_ = rng.uniform(8, 800)
        mu_ = rng.uniform(0.2, 2)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = x/np.linalg.norm(x)
        kv = np.concatenate(([1.0], xh))
        E = np.diag([-1.0, 1, 1, 1, 1])
        g0i = E - mu_/r_**2*np.outer(E@kv, E@kv)
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        D = (A + A.T)/2
        D /= max(abs(np.linalg.eigvalsh(D)))
        f1 = rng.uniform(-0.25, 0.25)
        al = np.concatenate(([-2.0], (1 + 2*f1)*xh))
        worst = max(worst, al@(g0i + 0.5/r_**2*D)@al)
        f2 = rng.uniform(0.5, 1.0)
        al2 = np.concatenate(([-2.0], (1 + 2*f2)*xh))
        ctl = max(ctl, al2@(g0i + 0.5/r_**2*D)@al2)
    check("X2 alpha = d(r - 2 t~): g_b0^-1(alpha, alpha) <= -7/4 for |f'| <= 1/4, decreasing in mu (exact), < 0 with "
          "|delta|_op <= r^-2/2 at 2000 points; alpha(d_t) = -2: a future boundary", okx2 and worst < -1.5,
          f"max {worst:.4f}")
    check("X2' control (f' in [1/2, 1]): alpha null or spacelike somewhere", ctl >= 0, f"max {ctl:.4f}")
    # X3
    a = sp.Symbol("a", positive=True)
    Vs = sp.Symbol("V", positive=True)
    phi_r = r**-4          # an explicit slice field, |d phi| ~ r^-5
    dens = (2*r)**(2*Q(11, 4))*sp.diff(phi_r, r)**2*r**3
    Ecut = sp.integrate(dens, (r, 10, Vs))
    full = sp.integrate(dens, (r, 10, sp.oo))
    check("X3 the energy cut at Phi <= V_* increases with V_* (positive integrand) to the full slice energy as "
          "V_* -> oo (exact, a = 11/4)", sp.limit(Ecut, Vs, sp.oo) == full and full.is_finite
          and sp.diff(Ecut, Vs).subs(Vs, 20) > 0, str(full))
    # X4
    j, rho = sp.symbols("j rho", positive=True)
    res = {}
    for q in (9, 8):
        term = (2**(j + 1)*rho)**(2*a)*(2**(j - 1)*rho)**(-q)
        res[q] = []
        for av in (Q(11, 4), Q(q, 2) - Q(1, 10), Q(q, 2)):
            ssum = sp.summation(term.subs(a, av), (j, 0, sp.oo))
            res[q].append(ssum.is_finite)
        closed = sp.summation(term.subs(a, Q(11, 4)), (j, 0, sp.oo))
        ok4 = sp.simplify(closed - 2**(2*Q(11, 4) + q)*rho**(2*Q(11, 4) - q)/(1 - 2**(2*Q(11, 4) - q))) == 0
        res[q].append(ok4)
    check("X4 [arithmetic: q entered from the degree count] the weighted tail sum_j (2^(j+1) rho)^(2a) (2^(j-1) "
          "rho)^-q = 2^(2a+q) rho^(2a-q)/(1 - 2^(2a-q)) (exact at a = 11/4), finite at a = q/2 - 1/10, infinite at "
          "q/2: for q = 9 the tail -> 0 uniformly in sigma, so the energy is continuous", res[9] == [True, True, False,
                                                                                                    True], str(res[9]))
    check("X4' control (q = 8, F_4 with no source): finite exactly for a < 4, still above the window",
          res[8] == [True, True, False, True], str(res[8]))


# ================================================================ Y

def part_y():
    print("Y  the a priori decay behind Hardy; Proposition R5.2's uniformity in sigma (m2)")
    t, x1, x2, x3, x4 = X = sp.symbols("t x1 x2 x3 x4", real=True)
    v1 = Q(7, 10)
    r = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    psi = sp.Function("psi")(*X)
    fp = sp.Symbol("fp")  # f'(r) at the point
    ok, ctl = True, True
    for c in (0, 1, 3):
        Fc = sp.diff(psi, X[c])
        ray = sum(X[i]/r*sp.diff(Fc, X[i]) for i in (1, 2, 3, 4)) + fp*sp.diff(Fc, t)   # d/dr along Sigma~
        Zpsi = (t - v1)*sp.diff(psi, t) + sum(X[i]*sp.diff(psi, X[i]) for i in (1, 2, 3, 4))
        main = sp.diff(Zpsi, X[c])/r - (t - v1)/r*sp.diff(sp.diff(psi, t), X[c]) + fp*sp.diff(sp.diff(psi, t), X[c])
        rem = sp.expand(ray - main)
        rem_c = sp.expand(ray - main + sp.diff(Zpsi, X[c])/r)
        ders = list(rem.atoms(sp.Derivative))
        first_only = all(len(d.variables) == 1 for d in ders)
        no_value = sp.expand(rem.xreplace({d: 0 for d in ders})) == 0        # no undifferentiated psi
        coefs = [sp.simplify(rem.coeff(d)*r) for d in ders]                 # r x coefficient: bounded on W
        bounded = all(cf.is_number and abs(cf) <= 1 for cf in coefs)
        ok = ok and ders and first_only and no_value and bounded
        ctl = ctl and any(len(d.variables) == 2 for d in rem_c.atoms(sp.Derivative))
    check("Y1 d/dr along a ray of d_c psi = r^-1 d_c(Z psi) - r^-1 (t - v1) d_c d_t psi + f' d_c d_t psi + first "
          "derivatives of psi with coefficients O(1/r): S1 for d h' uses first derivatives of Gamma h' only, no Hardy "
          "(c = t, x1, x3; generic psi)", ok)
    check("Y1' control (r^-1 d_c(Z psi) dropped): second derivatives of psi remain", ctl)
    mp.mp.dps = 30
    rng = random.Random(71)
    worst_b, worst_h, n = 0.0, 0.0, 0
    for _ in range(24):
        av = mp.mpf(rng.uniform(0.1, 3.9))
        ps = [av + 1 + mp.mpf(rng.uniform(0.05, 2)) for _ in range(3)]
        cs = [mp.mpf(rng.uniform(-2, 2)) for _ in range(3)]
        om = mp.mpf(rng.uniform(0.5, 3))
        phi = lambda x: sum(c*x**(-p)*(1 + mp.sin(om*mp.log(x))/2) for c, p in zip(cs, ps))
        dphi = lambda x: mp.diff(phi, x)
        for R in (mp.mpf(2), mp.mpf(20)):
            lhs = mp.quad(lambda x: x**(2*av + 1)*phi(x)**2, [R, 10*R, mp.inf])
            rhs = mp.quad(lambda x: x**(2*av + 3)*dphi(x)**2, [R, 10*R, mp.inf])/(av + 1)**2
            worst_h = max(worst_h, float(lhs/rhs))
        for Rp in (10, 100, 1000):
            Rp = mp.mpf(Rp)
            bt = Rp**(2*av + 2)*phi(Rp)**2
            tail = mp.quad(lambda x: x**(2*av + 3)*dphi(x)**2, [Rp, 10*Rp, mp.inf])/(2*av + 2)
            worst_b = max(worst_b, float(bt/tail))
            n += 1
    check("Y2 for phi -> 0 with finite derivative energy: R'^(2a+2) phi(R')^2 <= (2a+2)^-1 int_R'^oo s^(2a+3) phi'^2 "
          "(so the Hardy boundary term vanishes at every R' -> oo) and Hardy on [R, oo) (24 random non-power-law "
          "fields)", worst_b <= 1 + 1e-12 and worst_h <= 1 + 1e-12,
          f"max boundary/tail {worst_b:.4f}, max Hardy lhs/rhs {worst_h:.4f}")
    a, rr, c0 = sp.symbols("a r c0", positive=True)
    phic = c0 + rr**(-a - 2)
    Rv = sp.Symbol("Rv", positive=True)   # the integrals up to Rv, then Rv -> oo (sympy's improper form is slow here)
    I_lhs = sp.limit(sp.integrate(sp.expand((rr**(2*a + 1)*phic**2).subs({a: Q(11, 4), c0: Q(1, 60)})), (rr, 1, Rv)),
                     Rv, sp.oo)
    I_rhs = sp.limit(sp.integrate(sp.expand((rr**(2*a + 3)*sp.diff(phic, rr)**2).subs({a: Q(11, 4), c0: Q(1, 60)})),
                                  (rr, 1, Rv)), Rv, sp.oo)
    bt_c = sp.limit((rr**(2*a + 2)*phic**2).subs({a: Q(11, 4), c0: Q(1, 60)}), rr, sp.oo)
    check("Y2' control (phi = c + r^-(a+2), c = 1/60: finite derivative energy, limit c): int r^(2a+1) phi^2 = oo, the "
          "boundary term -> oo: Hardy fails without the decay", I_lhs == sp.oo and I_rhs.is_finite and bt_c == sp.oo)
    # Y3: the model family
    tt, rs = sp.symbols("t r", real=True)
    a0 = Q(1, 4)
    v = tt + rs
    B = lambda vv: sp.Rational(3, 10)/(1 + vv**2)
    D = Q(1, 100)

    def family(kind):
        h = B(v)*rs**-2 + D*rs**(-Q(1, 2) - a0)*sp.cos(tt/rs)
        if kind == "const":
            h = h + Q(1, 60)
        if kind == "sigma":
            h = h + Q(1, 60)*tt/(1 + tt**2)
        return h
    res = {}
    for kind in ("model", "const", "sigma"):
        h = family(kind)
        lims = [sp.limit(h.subs(tt, sg), rs, sp.oo) for sg in (0, -3, -100)]
        onN = sp.limit(h.subs(tt, Q(7, 10) - rs), rs, sp.oo)
        dt_dec = sp.limit(sp.diff(h, tt).subs(tt, -3)*rs**(Q(3, 2) + a0), rs, sp.oo)  # at fixed t = -3 in W
        res[kind] = (lims, onN, dt_dec)
    lims, onN, dtd = res["model"]
    sup_ok = True
    for sg in (0, -3, -100):
        expr = sp.Abs(family("model").subs(tt, sg))*rs**(Q(1, 2) + a0)
        vals = [sp.N(expr.subs(rs, rv), 20) for rv in (200, 2000, 20000, 200000)]
        sup_ok = sup_ok and max(vals) <= D + Q(3, 10) + 1e-12
    check("Y3 model family (a0 = 1/4): c(sigma) = lim h'(sigma, r) is the same at sigma = 0, -3, -100 and equals "
          "lim h'|_N = 0; |d_t h'| r^(3/2 + a0) bounded; |h'| <= C r^(-1/2-a0) with C independent of sigma",
          len(set(lims)) == 1 and lims[0] == 0 and onN == 0 and dtd.is_finite and sup_ok, str(lims))
    lc, nc, _ = res["const"]
    ls_, ns_, dts = res["sigma"]
    check("Y3' controls: h' + 1/60 has c = 1/60 != 0 and violates h'|_N -> 0; h' + t/(60(1 + t^2)) has a "
          "sigma-dependent limit and |d_t h'| r^(3/2+a0) unbounded", lc == [Q(1, 60)]*3 and nc == Q(1, 60)
          and len(set(ls_)) == 3 and dts in (sp.oo, -sp.oo), f"{lc}; {ls_}")


# ================================================================ M, L, A0, T

def part_m():
    print("M  Lemma R4.5 at every a in (0, 7/2): monotone in the weight (m3)")
    a, ap, d = sp.symbols("a ap d", positive=True)
    u = 1 + d    # u* - u >= 1 (r5settle5 E1: r + 1 <= u* - u)
    ratio = u**(2*a)/u**(2*(a + ap))
    ok = sp.simplify(sp.log(ratio).expand(force=True)) == -2*ap*sp.log(1 + d) and all(
        ratio.subs({a: Q(1, 2), ap: Q(9, 4), d: dv}) <= 1 for dv in (0, Q(1, 10), 5, 1000))
    ctl = (u**(2*a)/u**(2*(a + ap))).subs({a: Q(1, 2), ap: Q(9, 4), d: -Q(1, 2)}) > 1
    check("M1 w_a/w_(a') = (u* - u)^(-2(a' - a)) <= 1 for a <= a' since u* - u >= 1: R4.5's fluxes are monotone in a",
          ok)
    check("M1' control (u* - u = 1/2 allowed): the ratio exceeds 1", ctl)


def part_l():
    print("L  the '+2 for Lemma 9.3' of Proposition R5.4")
    r, lam = sp.symbols("r lam", positive=True)
    A = 1 + r
    f = A*sp.sin(r/lam)
    N = {i: sp.integrate(sp.expand(r**3*sp.diff(f, r, i)**2), (r, 1, 2)) for i in (1, 3, 4)}  # exact in lam
    rat3 = [sp.N((lam**4*N[3]/N[1]).subs(lam, sp.Rational(1, 10**k)), 40) for k in (2, 3, 4)]
    rat4 = [sp.N((lam**6*N[4]/N[1]).subs(lam, sp.Rational(1, 10**k)), 40) for k in (2, 3, 4)]
    l31 = all(abs(x - 1) <= 40*sp.Rational(1, 10**k) for x, k in zip(rat3, (2, 3, 4)))
    l41 = all(abs(x - 1) <= 40*sp.Rational(1, 10**k) for x, k in zip(rat4, (2, 3, 4)))
    e, B = R5.stages(12, 6)

    def stages_cost(cost):
        e_ = {3: -1}
        for kk in range(4, 13):
            e_[kk] = R5.explicit_orders(kk - 1, 6, True, e_)[1]
        B_ = {3: -1}
        for J in range(3, 12):
            tail, _ = R5.explicit_orders(J, 6, True, e_)
            rem = R5.remainder_orders(J, B_[J], 6, e_)
            B_[J + 1] = max(tail, rem, e_[J + 1] + 1, e_[J + 1]) + cost
        return B_
    b2, b3 = stages_cost(2), stages_cost(3)
    check("L ||d_r^3 f||^2/||d_r f||^2 ~ lam^-4 on f = (1 + r) sin(v/lam) (lam^4 times it is 1 + O(lam): the exact "
          "integrals at lam = 1e-2, 1e-3, 1e-4): Lemma 9.3(a)'s sup bound costs lam^-2 beyond ||d f||; with that cost "
          "the recursion is B_J = 3J - 9 (= r5settle5 A2)",
          l31 and all(b2[J] == 3*J - 9 for J in range(4, 13)) and all(b2[J] == B[J] for J in range(4, 13)),
          f"{[sp.N(x, 8) for x in rat3]}; B_J {[b2[J] for J in range(4, 13)]}")
    check("L' control (Sobolev to order 4, cost 3): lam^6 ||d_r^4 f||^2/||d_r f||^2 -> 1 and B_J changes",
          l41 and any(b3[J] != 3*J - 9 for J in range(4, 13)), str([b3[J] for J in range(4, 13)]))


def part_a0():
    print("A0  the coefficient list of r5settle5 A, from g_b0")
    import f1lemma5 as F1
    mp.mp.dps = 40

    def degrees(flat):
        J = F1.Jets(F1.gb0(flat=flat))
        vals = {}
        for R_ in (10**6, 10**7):
            X = [mp.mpf("0.3")] + [mp.mpf(R_)/2]*4
            g, dg, ddg = J.at(X, 0)
            gi, dgi, G, dG = F1.christoffel(g, dg, ddg)
            eta = mp.diag([-1, 1, 1, 1, 1])
            R5_ = range(5)
            vals[R_] = {
                "g^-1 - eta": max(abs(gi[i, j] - eta[i, j]) for i in R5_ for j in R5_),
                "d g": max(abs(dg[c][i][j]) for c in R5_ for i in R5_ for j in R5_),
                "Gamma": max(abs(G[q][a_][b_]) for q in R5_ for a_ in R5_ for b_ in R5_),
                "d d g": max(abs(ddg[c][d][i][j]) for c in R5_ for d in R5_ for i in R5_ for j in R5_),
                "d Gamma": max(abs(dG[c][q][a_][b_]) for c in R5_ for q in R5_ for a_ in R5_ for b_ in R5_),
                "Gamma Gamma": max(abs(sum(G[c][c][d]*G[d][a_][b_] - G[c][b_][d]*G[d][a_][c] for c in R5_
                                           for d in R5_)) for a_ in R5_ for b_ in R5_)}
        out = {}
        for k_ in vals[10**6]:
            v6, v7 = vals[10**6][k_], vals[10**7][k_]
            out[k_] = None if v6 == 0 else int(mp.nint(mp.log10(v6/v7)))   # flat: exact zeros
        return out
    d = degrees(False)
    coefs = sorted({(0, 2), (d["g^-1 - eta"], 2), (d["Gamma"], 1), (d["d d g"], 0), (d["Gamma Gamma"], 0)})
    check("A0 decay degrees along a ray (R = 1e6, 1e7, 40 digits, f1lemma5's jets of g_b0): g^-1 - eta 2, d g 3, "
          "Gamma 3, d d g 4, d Gamma 4, Gamma Gamma 6; with (0.2)'s derivative counts this is r5settle5.COEFS",
          d == {"g^-1 - eta": 2, "d g": 3, "Gamma": 3, "d d g": 4, "d Gamma": 4, "Gamma Gamma": 6}
          and coefs == sorted(R5.COEFS), f"{d}; COEFS = {R5.COEFS}")
    dfl = degrees(True)
    check("A0' control (the flat metric): no coefficient beyond eta", all(v is None for v in dfl.values()), str(dfl))


def part_t():
    print("T  Theorem P's use of Lemmas 1.1(e) and 2.3 after D623 (m5)")
    m, lam = sp.symbols("m lambda", real=True)
    G = sp.Matrix([[-1 - m, m], [m, 1 - m]])   # g0^-1 on the (tau, r) plane: eta^-1 - m L0 L0, L0 = (1, -1)
    evs = list(G.eigenvals())
    s_of_m = sp.sqrt(1 + m**2) - m
    ok_ev = any(sp.simplify(e_ - (-m + sp.sqrt(1 + m**2))) == 0 for e_ in evs) and \
        any(sp.simplify(e_ - (-m - sp.sqrt(1 + m**2))) == 0 for e_ in evs)
    ok_tt = sp.simplify(G[0, 0] + 1 + m) == 0
    rng = random.Random(81)
    worst_tt, worst_inv, worst_ra, n = -1e9, 0.0, -1e9, 0
    for _ in range(2000):
        mv = rng.uniform(0.0, 0.9)
        mu0a2 = rng.uniform(1.05, 3.0)          # mu0/a^2 > 1
        sP = float(s_of_m.subs(m, mv))
        epsP = 0.99*min(sP, mu0a2 - 1, 1.0)
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        D = (A + A.T)/2
        D *= epsP/max(abs(np.linalg.eigvalsh(D)))
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = x/np.linalg.norm(x)
        L0 = np.concatenate(([1.0], -xh))
        g0i = np.diag([-1.0, 1, 1, 1, 1]) - mv*np.outer(L0, L0)
        gi = g0i + D
        worst_tt = max(worst_tt, gi[0, 0] - (-1 + epsP))
        worst_inv = max(worst_inv, max(abs(np.linalg.eigvalsh(np.linalg.inv(gi))))*(sP - epsP))
        dr = np.concatenate(([0.0], xh))
        g0i_a = np.diag([-1.0, 1, 1, 1, 1]) - mu0a2*np.outer(L0, L0)   # at r = a with mu = mu0
        worst_ra = max(worst_ra, dr@(g0i_a + D)@dr)
        n += 1
    check("T g0^-1(dtau, dtau) = -1 - m and the least |eigenvalue| of g0^-1 is sqrt(1 + m^2) - m (exact); for "
          "|delta|_op <= eps_P < min(s(m), mu0/a^2 - 1): (g0^-1 + delta)(dtau, dtau) <= -1 + eps_P, "
          "|g| <= (s - eps_P)^-1 (Weyl) and {r = a} spacelike (2000 samples at 0.99 of the threshold)",
          ok_ev and ok_tt and worst_tt <= 1e-12 and worst_inv <= 1 + 1e-9 and worst_ra < 0,
          f"max excess {worst_tt:.2e}, max |g| (s - eps_P) {worst_inv:.4f}, max g^-1(dr, dr) at r = a {worst_ra:.4f}")
    mv = Q(1, 3)
    Gn = G.subs(m, mv)
    P_, Dg = Gn.diagonalize()
    smin = sp.simplify(s_of_m.subs(m, mv))
    idx = [i for i in range(2) if sp.simplify(Dg[i, i] - smin) == 0][0]
    pert = sp.zeros(2, 2)
    pert[idx, idx] = -smin
    sing = sp.simplify((P_*(Dg + pert)*P_.inv()).det()) == 0
    check("T' control: |delta|_op = s(m) (m = 1/3) makes g^-1 singular (exact)", sing)


def main():
    for f in (part_x, part_y, part_m, part_l, part_a0, part_t):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
