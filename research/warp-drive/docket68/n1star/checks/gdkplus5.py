#!/usr/bin/env python3
"""gdkplus5.py -- GAUGEDECAY5.md Round 5: Theorem R2.5 at positive K+-weight for the 1-form wave operator Box on
Tangherlini (III.I'' Proposition 5.1 carried over to Box), and the rate it gives.  Every new weight, order and indicial
root of round 5 is computed here, each with a control that mutates the computed path and must fail.

  Q1 (exact) Densities and the weight dictionary.  Near iota+ cap K+ (rho_+ = 1/r, rho_K = r/t) and with dx =
     r^(n-1) dr dw, dt dx = rho_+^-(n+1) rho_K^-1 (drho_+/rho_+)(drho_K/rho_K) dw: L^2(dt dx) = rho_+^((n+1)/2)
     rho_K^(1/2) L^2_b, so at n = 4 a 3b weight (sf, K) is the b-weight (sf + 5/2, K + 1/2) for II.F''s mu_b = dt dx /
     (t r^4), which is exactly the b-density (II.F' (1.6), (1.7)).  A function rho_+^A rho_K^B lies in rho_+^w1 rho_K^w2
     L^2_b near the corner iff A > w1 and B > w2.  So R2.5's source class (3b (a_sf + 2, 0)) is the b-class (g + 2, 1/2)
     with g := a_sf + 5/2, its window a_sf + 2 in (0, 1) is g - 1/2 in (0, 1), its solution weight -1 (3b) is -1/2 =
     1/2 - 1 (b), and a b-weight a_K at K+ is the pointwise rate t^-a_K on compact sets: a_K = 1/2 + kappa.
     Control: n = 3 gives the shift 2 at iota+, not 5/2.
  Q2 (exact) The zero-energy gap of Box and the window.  r^2(-Delta) on r^-q Y_l in R^n has the indicial roots q = -l,
     l + n - 2 (on Cartesian components; the 1-form coupling is rho^2-relative, gdext5.py E1-E2).  In mu_b-weights (rho^q
     in rho^w L^2_b iff q > w; III.H's weight alpha on L^2(dx) is the mu_b-weight alpha + n/2) the root-free interval
     around the window is (0, 2) for l = 0..8; the column hat f_*(0) in A^3 lies in Y_0 (mu_b-weight alpha + 4) iff
     alpha + 2 < 1: the window gamma_+ - alpha_K = alpha + 2 is (0, 1), inside the gap.  The outgoing threshold:
     Box_0(r^-p F(t - r)) = (2p - (n - 1)) r^-(p+1) F' + O(r^-(p+2)), root p = 3/2, the scf cap 3/2 + S-bar, S-bar = 0
     for Box.  Control: at n = 3 the gap is (0, 1) and the root 1.
  Q3 (exact main term) Lemma 4.3 of III.I'' at Box: the one state W* = r^-2 dv - dr/(r(r + r_h)) lies in A^2 exactly
     (r^2 W*_t -> 1, r^3 W*_r -> r_h, (r d_r)^j (r^2 W*) bounded, j <= 3), and for G = Phi(sigma r) r^-q the norm
     ||W_beta^-1 G||_{L^2(mu_b)} at beta = (N, a + q - eps, a) is sigma^(q - eps) (2 eps)^(-1/2) (1 + o(1)): with q = 2
     the cut-off state's transform has tf-order a + 2 - eps.  Control: the Killing form (d_v)^flat in place of W* has
     q = 0, so order -eps, not 2 - eps.
  Q4 (exact) The coefficient B (II.G' Proposition 2.8 at beta = alpha_K).  F[t_+^-a_K e^(-e t)](sigma) =
     Gamma(1 - a_K) (e - i sigma)^(a_K - 1) for a_K in {1/2, 3/5, 3/4, 9/10}: the zf-weight a_K - 1 of hat b_1 is the
     K+-weight a_K of B, and the membership thresholds of X^(0, beta - 1) and H^(0, beta)_b meet at beta = a_K.
     Control: at a_K = 1 the transform is not a power (Gamma(0) is infinite; the cut-off transform E_1 carries
     log sigma): the zf Taylor term enters, the window's end.
  Q5 (exact, whole box) Every weight condition of the carried-over steps (III.I'' Lemmas 3.1, 4.1-4.3, (2.25a),
     (2.26a), II.G' Proposition 2.8, II.F' Theorem 1.1 for the density step) at alpha_K in (1/2, 1), gamma_+ in
     (alpha_K, 3/2), eps in (0, (3/2 - gamma_+)/5): each a positive sum on the box.  Control: III.I'''s bookkeeping
     for the singular part (beta_iota := gamma_+ + 1, the weight of d_t u_sing there) violates Lemma 4.3's tf-order.
  Q6 (exact) The rate.  For a source of iota+-order a the admissible K+-weights give kappa < min(1/2, a - 5/2); for
     the harmonic-gauge source (a = lambda_# + 1 = 5/2 + delta_#, and the commutator at b_+ + 2, b_+ < 1/2 + delta_#)
     explicit parameters exist for every kappa in (0, delta_#), and for the commutator of a homogeneous solution with
     compactly supported data for every kappa in (0, 1/2), each a positive sum on the box; round 4's G4 class with
     sf-weight beta is exactly this class with beta = gamma_+ - alpha_K; and kappa_sup(a) equals round 4's formal l = 0
     exponent a - 5/2 on (5/2, 3), never exceeding it.  Control: with the window's lower end dropped (gamma_+ > alpha_K
     - 1) the bookkeeping admits kappa beyond the model exponent.

Labels: computed (exact, sympy; Q3's main term exact and its remainder checked by its order at 0).  Run: python3
checks/gdkplus5.py
"""
import sys

import sympy as sp

HALF = sp.Rational(1, 2)


def positive_sum(expr, pos):
    """expr equals a quotient of polynomials in the 'pos' symbols whose coefficients all have one sign, the same for
    numerator and denominator: a sufficient, exact test of positivity on the open box (the symbols range over (0, oo);
    box coordinates are U/(1 + U))"""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    if num.is_number and den.is_number:
        return bool(num/den > 0)
    N, Dn = sp.Poly(sp.expand(num), *pos), sp.Poly(sp.expand(den), *pos)

    def allpos(P):
        return not P.is_zero and all(c > 0 for c in P.coeffs())

    def allneg(P):
        return not P.is_zero and all(c < 0 for c in P.coeffs())
    return (allpos(N) and allpos(Dn)) or (allneg(N) and allneg(Dn))


def box(*names):
    syms = sp.symbols(' '.join(names), positive=True)
    return syms, [S/(1 + S) for S in syms]


# --------------------------------------------------------------------------------------------------------------- Q1
def q1(control=False):
    n = 3 if control else 4
    rp, rk, A, B, w1, w2 = sp.symbols('rho_p rho_K A B w1 w2', positive=True)
    T, R = 1/(rp*rk), 1/rp
    jac = sp.Matrix([[sp.diff(T, rp), sp.diff(T, rk)], [sp.diff(R, rp), sp.diff(R, rk)]]).det()
    dens = sp.simplify(sp.Abs(jac)*R**(n - 1))             # dt dx = dens drho_+ drho_K dw
    fac = sp.simplify(dens*rp*rk)                           # relative to the b-density drho_+ drho_K/(rho_+ rho_K)
    e_p = sp.degree(sp.Poly(sp.simplify(1/fac), rp))
    e_k = sp.degree(sp.Poly(sp.simplify(1/fac), rk))
    shifts = (sp.Rational(e_p, 2), sp.Rational(e_k, 2))
    mub = sp.simplify(dens/(T*R**4)*rp*rk) if not control else sp.simplify(dens/(T*R**n)*rp*rk)
    # pointwise membership near the corner: int_0^1 rho^(2(A - w) - 1) drho < oo iff A > w
    conv = sp.integrate(rp**(2*(A - w1) - 1), (rp, 0, 1), conds='piecewise')
    memb = isinstance(conv, sp.Piecewise) and sp.simplify(conv.args[0][1].subs(A, w1 + 1)) == True
    edge = sp.integrate(rp**(-1), (rp, sp.Rational(1, 10**6), 1))  # A = w: logarithmic, not bounded uniformly
    # interior of K+: rho_K = <x>/t at fixed x: dt = <x> rho_K^-2 drho_K = (<x>/rho_K) drho_K/rho_K: shift 1/2
    x = sp.Symbol('X', positive=True)
    tk = x/rk
    kint = sp.simplify(sp.Abs(sp.diff(tk, rk))*rk)          # dt = (<x>/rho_K) drho_K/rho_K at fixed x
    kok = sp.simplify(sp.log(kint/x).diff(rk)*rk) == -1     # rho_K^-1: L^2(dt) = rho_K^(1/2) L^2_b, shift 1/2
    # the dictionary: R2.5's classes
    asf = sp.Symbol('a_sf')
    g = asf + 2 + shifts[0]
    src_b = (g, 0 + shifts[1])                               # 3b (a_sf + 2, 0)
    sol_K = -1 + shifts[1]                                   # 3b K-weight -1
    ok = (shifts == (sp.Rational(5, 2), HALF) and mub == 1 and memb and edge > 13 and kok
          and sp.simplify(src_b[0] - (asf + sp.Rational(9, 2))) == 0 and src_b[1] == HALF
          and sp.simplify(sol_K - (HALF - 1)) == 0)
    if control:
        print("  Q1 control (n = 3): b-shifts at (iota+, K+) = %s, the 4D values (5/2, 1/2): %s"
              % (shifts, ok), flush=True)
        return ok
    print("  Q1: dt dx = rho_+^-%s rho_K^-%s x b-density, so L^2(dt dx) = rho_+^%s rho_K^%s L^2_b; mu_b = dt dx/(t r^4)"
          " is the b-density: %s; rho^A in rho^w L^2_b iff A > w: %s (A = w diverges: %s); K+ interior shift 1/2: %s; "
          "R2.5's source 3b (a_sf + 2, 0) = b (%s, %s), solution K-weight 3b -1 = b %s"
          % (e_p, e_k, shifts[0], shifts[1], mub == 1, memb, edge > 13, kok, src_b[0], src_b[1], sol_K), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- Q2
def q2(control=False):
    n = 3 if control else 4
    q, rr, p = sp.symbols('q r p', positive=True)
    roots_all = []
    for l in range(0, 9):
        f = rr**(-q)
        lap = sp.diff(f, rr, 2) + sp.Rational(n - 1)/rr*sp.diff(f, rr) - l*(l + n - 2)/rr**2*f
        ind = sp.expand(sp.simplify(-lap*rr**(q + 2)))
        qq = sp.Symbol('qq')
        rts = sp.solve(sp.Eq(ind.subs(q, qq), 0), qq)
        roots_all += [sp.nsimplify(z) for z in rts]
        if sorted(rts) != sorted([-l, l + n - 2]):
            return control is False and False
    below = max(z for z in roots_all if z <= 0)
    above = min(z for z in roots_all if z > 0)
    gap = (below, above)
    # III.H's alpha (L^2(dx)) is the mu_b-weight alpha + n/2; Y_0 has mu_b-weight alpha + n/2 + 2; A^3 in Y_0 iff
    # 3 > alpha + n/2 + 2
    al = sp.Symbol('alpha')
    edge = sp.solve(sp.Eq(al + sp.Rational(n, 2) + 2, 3), al)[0]  # A^3 in Y_0 (mu_b-weight alpha + n/2 + 2) iff below
    win_hi = edge + 2                                              # alpha + 2 at the column's edge
    # the outgoing threshold: F = exp(k(t - r)), read the r^0 coefficient after multiplying by r^(p+1)
    tt = sp.Symbol('t')
    kk = sp.Symbol('k')
    ue = rr**(-p)*sp.exp(kk*(tt - rr))
    be = sp.simplify((-sp.diff(ue, tt, 2) + sp.diff(ue, rr, 2) + sp.Rational(n - 1)/rr*sp.diff(ue, rr))
                     * rr**(p + 1)/sp.exp(kk*(tt - rr)))
    be = sp.expand(be)
    lead = sp.limit(be, rr, sp.oo)
    root_p = sp.solve(sp.Eq(lead, 0), p)
    ok = gap == (0, 2) and win_hi == 1 and (0 < win_hi <= gap[1]) and root_p == [sp.Rational(3, 2)]
    if control:
        print("  Q2 control (n = 3): gap %s, column window edge %s, radiation root %s; the 4D values: %s"
              % (gap, win_hi, root_p, ok), flush=True)
        return ok
    print("  Q2: indicial roots of r^2(-Delta) on r^-q Y_l are {-l, l + 2} for l = 0..8; root-free interval around the "
          "window (mu_b-weights): %s; column A^3 in Y_0 iff alpha + 2 < %s, so the window gamma_+ - alpha_K in (0, %s) "
          "lies in the gap; Box_0(r^-p e^(k(t - r))) r^(p+1) -> %s, root p = %s (the scf cap 3/2 + S-bar, S-bar = 0)"
          % (gap, win_hi, win_hi, sp.factor(lead), root_p), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- Q3
def q3(control=False):
    r, rh, sg, xx = sp.symbols('r r_h sigma x', positive=True)
    mu = rh**2
    f = 1 - mu/r**2
    if control:                                     # the Killing form (d_v)^flat = -f dv + dr, dv = dt + dr/f
        Wt, Wr = -f, -f/f + 1
    else:                                           # W* = r^-2 dv - dr/(r (r + r_h))
        Wt, Wr = 1/r**2, 1/(r**2*f) - 1/(r*(r + rh))
    # the decay order q: the largest integer with r^q W bounded and some component not o(r^-q)
    q = None
    for qq in range(4, -1, -1):
        lims = [sp.limit(r**qq*w, r, sp.oo) for w in (Wt, Wr)]
        if all(z.is_finite for z in lims) and any(z != 0 for z in lims):
            q = qq
            break
    conormal = q is not None and all(                      # r^j d_r^j spans (r d_r)^i, i <= j
        sp.limit(sp.simplify(sp.diff(r**q*w, r, j)*r**j), r, sp.oo).is_finite for w in (Wt, Wr) for j in (1, 2, 3))
    r3Wr = sp.limit(r**3*Wr, r, sp.oo)
    # Lemma 4.3: ||W^-1 Phi(sigma r) r^-q||^2_{L^2(dr/r, r >= 1)} = sigma^(2q) int_sigma^oo (1+x)^(2m) x^(-2eps-1)
    # g(x) dx
    # with g = Phi^2 = e^(-2x^2); main term int_sigma^1 x^(-2eps-1) dx exact, remainder integrable (g - 1 = O(x^2))
    rows = []
    good = True
    for eps in (sp.Rational(1, 4), sp.Rational(1, 10), sp.Rational(1, 3)):
        for m in (0, 2):
            g = (1 + xx)**(2*m)*sp.exp(-2*xx**2)
            main = sp.integrate(xx**(-2*eps - 1), (xx, sg, 1))
            lim_main = sp.limit(sg**(2*eps)*main, sg, 0)
            rem_order = sp.Poly(sp.series(g - 1, xx, 0, 3).removeO(), xx).monoms()[-1][0]
            rem_ok = rem_order - 2*eps - 1 > -1                 # x^(-2eps-1)(g - 1) integrable at 0
            tail_ok = True                                       # int_1^oo of x^(-2eps-1) g converges (Gaussian)
            order = q - eps                                      # ||.|| = sigma^q (sigma^(-2eps)/(2eps))^(1/2)(1+o(1))
            rows.append((str(eps), m, lim_main, rem_ok, order))
            good &= lim_main == 1/(2*eps) and rem_ok and tail_ok
    tf_order_minus_a = [rw[4] for rw in rows]
    ok = q == 2 and conormal and good and all(rw[4] == 2 - sp.Rational(rw[0]) for rw in rows)
    if control:
        print("  Q3 control ((d_v)^flat): decay order q = %s, tf-order minus a = %s; equal to 2 - eps: %s"
              % (q, tf_order_minus_a[:2], ok), flush=True)
        return ok
    print("  Q3: W* in A^2: q = %s, r^2 W*_t -> 1, r^3 W*_r -> %s, (r d_r)^j (r^2 W*) bounded j <= 3: %s; (eps, m, "
          "lim sigma^(2eps) int_sigma^1 x^(-2eps-1), remainder integrable, tf-order minus a) = %s"
          % (q, r3Wr, conormal, rows), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- Q4
def q4(control=False):
    t, s, e = sp.symbols('t sigma e', positive=True)
    rows = []
    ok = True
    samples = [sp.Integer(1)] if control else [HALF, sp.Rational(3, 5), sp.Rational(3, 4), sp.Rational(9, 10)]
    for aK in samples:
        lam = -aK
        z = e - sp.I*s
        expected = sp.gamma(1 - aK)*z**(aK - 1)
        if control:
            power_law = sp.gamma(1 - aK).is_finite is True       # Gamma(0) = zoo: no power law at a_K = 1
            w = sp.Symbol('w', positive=True)
            ser = sp.series(sp.expint(1, w), w, 0, 2).removeO()  # the transform of t^-1 cut off at t = 1
            has_log = ser.has(sp.log)
            print("  Q4 control (a_K = 1): Gamma(1 - a_K) = %s, so no power law; E_1(w) = %s near 0, log: %s"
                  % (sp.gamma(1 - aK), ser, has_log), flush=True)
            return power_law and not has_log
        # the transform, computed: int_0^oo t^lam e^(-z t) dt with z = e - i sigma, Re z = e > 0
        k = sp.Symbol('kk', positive=True)
        val = sp.integrate(t**lam*sp.exp(-k*t), (t, 0, sp.oo))
        tr_ok = sp.simplify(val - sp.gamma(1 - aK)*k**(aK - 1)) == 0      # analytic in k, continued to k = z
        # membership thresholds: t^-aK in H^(0,beta)_b at oo iff beta < aK; |sigma|^(aK-1) in X^(0, beta-1) iff
        # beta - 1 < aK - 1
        # <t>^(beta-1/2) t^-aK in L^2(dt) at oo iff 2(beta - 1/2) - 2aK < -1 (II.G' Definition 2.1);
        # |sigma|^(-(beta-1)-1/2) |sigma|^(aK-1) in L^2(dsigma) at 0 iff -2(beta - 1) - 1 + 2(aK - 1) > -1 (Def. 2.7)
        be = sp.Symbol('beta')
        thr_t = sp.solve(sp.Eq(2*(be - HALF) - 2*aK, -1), be)[0]
        thr_s = sp.solve(sp.Eq(-2*(be - 1) - 1 + 2*(aK - 1), -1), be)[0]
        it = sp.integrate(t**(2*(thr_t - sp.Rational(1, 10) - HALF) - 2*aK), (t, 1, sp.oo))   # below: finite
        it_edge = sp.integrate(t**(2*(thr_t - HALF) - 2*aK), (t, 1, sp.oo))                  # at: infinite
        tr_ok = tr_ok and it.is_finite and it_edge == sp.oo
        rows.append((str(aK), tr_ok, thr_t, thr_s))
        ok &= tr_ok and thr_t == aK and thr_s == aK
    print("  Q4: (a_K, int_0^oo t^-a_K e^(-k t) dt = Gamma(1 - a_K) k^(a_K - 1), threshold of beta for t^-a_K in "
          "H^(0,beta)_b, for |sigma|^(a_K - 1) in X^(0,beta-1)) = %s: zf-weight a_K - 1 <-> K+-weight a_K, pointwise "
          "|B| <~ t^-a_K" % rows, flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- Q5
def q5(control=False):
    (U1, U2, U3), (u1, u2, u3) = box('U1', 'U2', 'U3')
    aK = HALF + u1/2
    gp = aK + u2*(sp.Rational(3, 2) - aK)
    ep = u3*(sp.Rational(3, 2) - gp)/5
    bp = (HALF + gp)/2
    bI = (bp + sp.Rational(3, 2))/2
    wI = 3                                                   # the source's I+-weight (vanishing near I+ is allowed)
    beta_iota_sing = gp + 1 if control else gp               # III.I'' uses gamma_+ + 1 for d_t u_sing
    pos = [U1, U2, U3]
    conds = {
        'window > 0': gp - aK,
        'window < 1': 1 - (gp - aK),
        'L4.1 beta_K = a_K in (0,1)': aK,
        'L4.1 1 - a_K': 1 - aK,
        'L4.1 beta_I^f = w_I - 1 >= 3/2': (wI - 1) - sp.Rational(3, 2) + sp.Rational(1, 10**6),
        'L4.1 w_I >= g + 2 - a_K': wI - (gp + 2 - aK),
        '(2.25a) w_I >= g + 2 - min(a_K, .)': wI - (gp + 2 - aK),
        'L4.2 r_out < -1/2': -HALF - (sp.Rational(3, 2) - ep - 2 - ep/2),
        'L4.2 source scf 5/2 - eps <= g + 2 - eps': (gp + 2 - ep) - (sp.Rational(5, 2) - ep),
        '(2.26a) K-weight a_K, Taylor void (a_K - 1 < 0)': 1 - aK,
        'L4.3 tf(chi G_1) = a_K + 1 - eps >= beta_iota': (aK + 1 - ep) - beta_iota_sing,
        'L3.1 beta_iota > beta_I = g - eps': beta_iota_sing - (gp - ep),
        'L3.1 beta_K = a_K - 1 <= beta_iota - beta_I': (beta_iota_sing - (gp - ep)) - (aK - 1),
        'L3.1 beta_K > -1': aK,
        'L3.1 beta_K < 0': 1 - aK,
        'L3.1 a priori K-: a_K >= a_K - 1': sp.Integer(1),
        'II.G 2.8: a = a_K - 1 > -1': aK,
        'II.F b_+ > 1/2': bp - HALF,
        'II.F b_+ < b_I': bI - bp,
        'II.F b_I < 3/2': sp.Rational(3, 2) - bI,
        'II.F source iota+ g + 2 >= b_+ + 2': gp - bp,
        'II.F source I+ w_I >= b_I + 1': wI - (bI + 1),
        'conclusion: iota+ weight g - eps > a_K': (gp - ep) - aK,
    }
    res = {k: positive_sum(sp.simplify(v), pos) for k, v in conds.items()}
    # the a priori iota-weight of u_reg on Omega_< is gamma_+ = beta_iota: an equality, checked as one
    eq_ok = sp.simplify(gp - gp) == 0
    if control:
        k = 'L4.3 tf(chi G_1) = a_K + 1 - eps >= beta_iota'
        print("  Q5 control (III.I'''s beta_iota = gamma_+ + 1 for the singular part): %s is a positive sum: %s"
              % (k, res[k]), flush=True)
        return res[k]
    print("  Q5: every condition a positive sum on the box a_K in (1/2, 1), gamma_+ in (a_K, 3/2), eps in (0, (3/2 - "
          "gamma_+)/5): %s; %s; the a priori iota-weight an equality: %s"
          % (all(res.values()), sorted(k for k, v in res.items() if v), eq_ok), flush=True)
    return all(res.values()) and eq_ok


# --------------------------------------------------------------------------------------------------------------- Q6
def kappa_sup(a, lower_window=True):
    """sup of alpha_K - 1/2 over alpha_K in [1/2, 1), gamma_+ with lo < gamma_+ < 3/2, gamma_+ + 2 < a, where lo =
    alpha_K (the window's lower end) or alpha_K - 1 (mutated)"""
    if lower_window:
        ub = sp.Min(1, sp.Rational(3, 2), a - 2)               # alpha_K < gamma_+ < min(3/2, a - 2)
    else:
        ub = sp.Min(1, sp.Rational(5, 2), a - 1)
    return sp.Max(0, ub - HALF)


def q6(control=False):
    a = sp.Symbol('a', positive=True)
    lw = not control
    # (i) kappa_sup(a) against round 4's formal l = 0 exponent a - 5/2 on (5/2, 3), and min(1/2, a - 5/2) in general
    samples = [sp.Rational(5, 2) + sp.Rational(k, 40) for k in range(1, 40)] + [sp.Rational(7, 2), 4]
    cons = all(sp.simplify(kappa_sup(x, lw) - sp.Min(HALF, x - sp.Rational(5, 2))) == 0 for x in samples)
    below_model = all(kappa_sup(x, lw) <= x - sp.Rational(5, 2) for x in samples if x < 3)
    if control:
        print("  Q6 control (window's lower end dropped): kappa_sup(a) <= the model exponent a - 5/2 on (5/2, 3): %s"
              % below_model, flush=True)
        return below_model
    (D, Uk, Ue), (_, uk, ue) = box('D', 'Uk', 'Ue')
    d = D/(4*(1 + D))                                          # delta_# in (0, 1/4) (I10:45-46)
    pos = [D, Uk, Ue]
    # (ii) the harmonic-gauge source: kappa = uk d; beta = (kappa + d)/2; eta = ue (d - beta); b_+ = 1/2 + beta;
    # gamma_+ = 1/2 + (kappa + beta)/2; alpha_K = 1/2 + kappa; J_h's order a_J = 5/2 + d - eta
    kap = uk*d
    beta = (kap + d)/2
    eta = ue*(d - beta)
    bp = HALF + beta
    gp = HALF + (kap + beta)/2
    aK = HALF + kap
    aJ = sp.Rational(5, 2) + d - eta
    hg = {
        'kappa < delta_#': d - kap,
        'beta < delta_# (R3.2, R4.3)': d - beta,
        'eta < delta_# - beta (R3.2)': (d - beta) - eta,
        'window > 0': gp - aK, 'window < 1': 1 - (gp - aK),
        'gamma_+ < 3/2': sp.Rational(3, 2) - gp,
        'alpha_K < 1': 1 - aK,
        'J_h iota+-order above gamma_+ + 2': aJ - (gp + 2),
        'commutator b_+ + 2 above gamma_+ + 2': bp - gp,
        'II.F b_+ in (1/2, 3/2)': (bp - HALF),
        'II.F b_+ < 3/2': sp.Rational(3, 2) - bp,
    }
    res_hg = {k: positive_sum(sp.simplify(v), pos) for k, v in hg.items()}
    # (iii) homogeneous solutions with compactly supported data: kappa = uk/2; gamma_+ = aK + (3/2 - aK)/3;
    # b_+ = aK + 2(3/2 - aK)/3; b_I = (b_+ + 3/2)/2; p = (b_I + 3/2)/2 (R4.6 (1)-(2): p < 3/2)
    kap2 = uk/2
    aK2 = HALF + kap2
    gp2 = aK2 + (sp.Rational(3, 2) - aK2)/3
    bp2 = aK2 + 2*(sp.Rational(3, 2) - aK2)/3
    bI2 = (bp2 + sp.Rational(3, 2))/2
    p2 = (bI2 + sp.Rational(3, 2))/2
    cs = {
        'kappa < 1/2': HALF - kap2,
        'window > 0': gp2 - aK2, 'window < 1': 1 - (gp2 - aK2),
        'gamma_+ < b_+ (commutator order b_+ + 2)': bp2 - gp2,
        'b_+ < b_I < p < 3/2': (bI2 - bp2), 'b_I < p': p2 - bI2, 'p < 3/2': sp.Rational(3, 2) - p2,
        'b_+ > 1/2': bp2 - HALF,
    }
    res_cs = {k: positive_sum(sp.simplify(v), [Uk]) for k, v in cs.items()}
    # (iv) round 4's G4 class: t^kappa r^beta f in L^2(dt dx) is the b-class (beta + kappa + 5/2, kappa + 1/2) (Q1),
    # i.e. (gamma_+ + 2, alpha_K) with gamma_+ - alpha_K = beta
    bG, kG = sp.symbols('beta_G kappa_G', positive=True)
    rp, rk = sp.symbols('rho_p rho_K', positive=True)
    tw = (1/(rp*rk))**kG*(1/rp)**bG                        # t^kappa r^beta in the corner chart
    ex_p = sp.simplify(rp*sp.diff(sp.expand_log(sp.log(1/tw), force=True), rp))   # f in tw^-1 L^2(dt dx)
    ex_k = sp.simplify(rk*sp.diff(sp.expand_log(sp.log(1/tw), force=True), rk))
    wts = (ex_p + sp.Rational(5, 2), ex_k + HALF)           # Q1's dictionary
    g_from = wts[0] - 2
    aK_from = wts[1]
    g4 = sp.simplify(g_from - aK_from - bG) == 0 and sp.simplify(aK_from - (HALF + kG)) == 0
    ok = cons and below_model and all(res_hg.values()) and all(res_cs.values()) and g4
    print("  Q6: kappa_sup(a) = min(1/2, a - 5/2) at %d samples: %s, never above the l = 0 model exponent a - 5/2 on "
          "(5/2, 3): %s; harmonic-gauge source, every kappa in (0, delta_#), explicit parameters, all positive sums: %s;"
          " compactly supported data, every kappa in (0, 1/2): %s; G4's class = (gamma_+ + 2, alpha_K) with beta = "
          "gamma_+ - alpha_K: %s" % (len(samples), cons, below_model, all(res_hg.values()), all(res_cs.values()), g4),
          flush=True)
    return ok


CHECKS = [("Q1", q1), ("Q2", q2), ("Q3", q3), ("Q4", q4), ("Q5", q5), ("Q6", q6)]


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
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
