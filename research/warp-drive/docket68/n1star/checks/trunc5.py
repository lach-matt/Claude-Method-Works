"""trunc5.py -- SETTLE-GLAM5 round 3, (b1): the truncated problems on the wedge W, posed as Cauchy problems whose
data on {v <= v1 + kappa'} are g_lam's own, so that no characteristic or corner problem is posed; the energy identity
for the quasilinear metric; the radial derivatives from the equation; (N2)'s dyadic flux identity with its powers of
lam; the Cauchy sequence as T -> -oo.

Setting: Cartesian (t, x1..x4), g_b0 = eta + mu r^-2 k k, k = dt + xhat.dx = dv, v = t + r, u = t - r; the record's
P (N1STAR-PROOF.md:1053-1060): t_P := 1 + tau0 - tau, h(tau) = kappa t_P^(-1/4), kappa = 1/2, Sigma_tau cap P+ =
{v_start <= v <= V_P - h(tau)}; N = {v = v1} with v1 <= V'_P - kappa (BEYOND5.md:205-207).

  T1 (exact) the causal structure: grad v = g_b0^-1 dv = -d_t + d_r is null and past-directed for every mu, so
     dv(Y) >= 0 for every future causal Y (computed at 2000 random points and directions with r^2 > mu, min >= 0):
     v never decreases along future causal curves and J^-(N) lies in {v <= v1}. The strip Sigma_tau cap
     {v1 <= v <= V_P - h(tau)} has width at least kappa (1 - t_P^(-1/4)) > 0 (exact), so g_lam's data on
     {t = T} cap {v <= v1 + kappa/4} exist for T <= tau0 - 15, and the Cauchy problem from {t = T} with those data,
     cut off beyond, reproduces g_lam on {v <= v1, t >= T} (domain of dependence): N carries g_lam's data with no
     characteristic problem. Control: dr(Y) takes both signs on future causal Y (r is not a time function). And
     (T1e) v + eps t is a time function for g_b0 with margin 2 eps (exact), which survives perturbations small
     against eps, used on the bounded part of N in Omega'; control (T1f): at eps = 0 there is no margin.
  T2 (exact) the cap energies of the truncation (cut-off over a unit width in v inside the strip): for h ~ r^-2
     (round 1's (b1), weight a_0) the cut region costs |T|^(2a_0 - 1) -> 0 exactly for a_0 < 1/2; for the remainder
     h_R = O(r^-(9/2)) ((b2), subtraction through p = 4) |T|^(2a - 6) -> 0 exactly for a < 3. Controls: a_0 = 1/2,
     and the subtraction through p = 7/2 only (h_R = O(r^-4)) at a = 11/4, do not tend to 0.
  T3 (computed, mpmath 40 digits) the energy identity for a non-stationary metric g = g_b0 + h and X = w(u) d_t:
        div(T(X)) = (box_g phi) X phi + T(grad w, d_t) + (1/2) w T^ab d_t g_ab,
     at three points (two weights); and g^ab d_a d_b phi = box_g phi + g^ab Gamma^c_ab d_c phi (the reduced
     operator differs from box_g by a first-order term with coefficient Gamma[g] = Gamma[g_b0] + O(d h)). Control:
     without the deformation term (1/2) w T^ab d_t h_ab the identity fails.
  T4 (exact) the radial derivatives from the equation: on phi(t, |x|), g_b0^ab d_a d_b phi = -(1 + mu/r^2) phi_tt
     + 2 (mu/r^2) phi_tr + (1 - mu/r^2) phi_rr + (first order; angular terms on general phi): the phi_rr coefficient
     g_b0^-1(dr, dr) = 1 - mu/r^2 is positive for r^2 > mu, so d_r^2 h is the equation's source plus d_t-commuted
     and angular terms (with Omega, the rotations). Control: at r^2 = mu it vanishes.
  T5 (exact) (N2)'s flux identity on a dyadic piece: for phi(t, r) with phi = 0 near {v = v_start}, on
     D = {tau_- <= t <= tau_+, v_start <= v <= v1} (flat radial model, measure r^3 dr), with e := (1/2)(phi_t^2 +
     phi_r^2) r^3 and box phi := -phi_tt + phi_rr + 3 phi_r/r,
        E(tau_+) + int_N (1/2)(phi_t - phi_r)^2 r^3 dr = E(tau_-) - int int_D phi_t box phi r^3 dr dt,
     exactly, for a polynomial phi; the flux through N carries only the tangential derivative d_t - d_r. Control:
     with the transverse (phi_t + phi_r)^2 in place of (phi_t - phi_r)^2 the identity fails.
  T6 (exact) the dyadic sums with the powers of lam. Far region (t_P >= lam^-2, Proposition 9.8 at order k):
     sum over pieces of 2^(2a(k+1)) M^2 lam^(2(K' - i)) 2^-k is C lam^(2(K' - i)), finite exactly for a < 1/2.
     Near region (1 <= t_P <= lam^-2, Proposition 9.9 at order k, the phi-parts with t_P^(1/2) and lam^-1): every
     piece is at most lam^(2(K' - 1) - 4 beta0 - 2(2a + 1)), and log2(lam^-2) pieces: polynomial, -> 0 once
     K' > 2 + 2 beta0 + 2a + eps (exact at beta0 = 2, 3; a = 1/4, 9/20). Control: the far-region sum at a = 1/2.
  T7 (exact) the Cauchy sequence: the flux tails int_(r >= |T|) on N tend to 0: |T|^(2a_0 - 2) for h ~ r^-2 with
     ell-gain (a_0 < 1), |T|^(2a - 7) for h_R = O(r^-(9/2)) (a < 7/2); with T2's cap energies and the integrable
     kernels (scatter5 S2, scale5 Z7) the differences h_T - h_T' tend to 0 in the energy class as T, T' -> -oo.
     Control: without the ell-gain (|d h| ~ r^-2 on N) the tail is infinite at every a_0 >= 0.
  T8 (computed, quadrature) R2.6's wording: a field r^(-3/2) F(v) at past null infinity with F' != 0 has cap energy
     ~ |T|^(2a) int F'^2 on {t = T} (excluded at every a > 0); with F constant in v the cap energy is |T|^(2a-1),
     which tends to 0 for a < 1/2: what the weight a < 1/2 fails to exclude is an r^(-3/2) tail constant in v.
Labels: computed (T1 numerical at random points, T3 mpmath at 40 digits, T8 quadrature; the rest exact, sympy).

    python3 checks/trunc5.py
"""
import random
import sys

import mpmath as mp
import sympy as sp


import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)

FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


t, x1, x2, x3, x4 = XS = sp.symbols("t x1 x2 x3 x4", real=True)
mu = sp.Symbol("mu", positive=True)
RR = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)


def t1():
    print("T1  the causal structure, the strip, and the domain of dependence of N")
    random.seed(3)
    worst = 1e9
    dr_signs = set()
    for _ in range(2000):
        m = random.uniform(0.1, 3)
        x = [random.uniform(-4, 4) for _ in range(4)]
        r = sum(c*c for c in x)**0.5
        if r*r <= 1.05*m:
            continue
        xh = [c/r for c in x]
        k = [1.0] + xh
        eta = [-1, 1, 1, 1, 1]
        g = [[(eta[i] if i == j else 0) + m/r**2*k[i]*k[j] for j in range(5)] for i in range(5)]
        # a random future causal Y: Y = d_t + c n, rescaled until g(Y, Y) <= 0, with dt(Y) > 0
        while True:
            n = [random.gauss(0, 1) for _ in range(4)]
            nn = sum(c*c for c in n)**0.5
            s = random.uniform(0, 1.5)
            Y = [1.0] + [s*c/nn for c in n]
            gYY = sum(g[i][j]*Y[i]*Y[j] for i in range(5) for j in range(5))
            if gYY <= 0:
                break
        dv = [1.0] + xh
        worst = min(worst, sum(dv[i]*Y[i] for i in range(5)))
        dr_signs.add(sum(xh[i]*Y[i + 1] for i in range(4)) > 0)
    check("T1a dv(Y) >= 0 for every sampled future causal Y (g_b0, r^2 > mu): v is a time function", worst >= -1e-12,
          f"min dv(Y) = {worst:.3e}")
    eta = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1, x1/RR, x2/RR, x3/RR, x4/RR])
    gi = eta - mu/RR**2*(eta*k)*(eta*k).T
    gradv = sp.simplify(gi*k)
    check("T1b grad v = -d_t + xhat.d_x (null, past-directed) for every mu",
          sp.simplify(gradv - sp.Matrix([-1, x1/RR, x2/RR, x3/RR, x4/RR])) == sp.zeros(5, 1)
          and sp.simplify((k.T*gi*k)[0, 0]) == 0)
    tP, kap = sp.symbols("t_P kappa", positive=True)
    width = kap - kap*tP**sp.Rational(-1, 4)  # (V_P - h) - v1 >= (V_P - h) - (V_P - kappa)
    ok = sp.simplify(width.subs(kap, sp.Rational(1, 2)).subs(tP, 16) - sp.Rational(1, 4)) == 0 and \
        sp.limit(width, tP, sp.oo) == kap
    check("T1c the strip {v1 <= v <= V_P - h(tau)} has width >= kappa(1 - t_P^(-1/4)): 1/4 at t_P = 16, -> 1/2",
          ok)
    check("T1d control: dr(Y) takes both signs on future causal Y", dr_signs == {True, False})
    ep = sp.Symbol("epsilon", positive=True)
    dt_ = sp.Matrix([1, 0, 0, 0, 0])
    form = sp.simplify(((k + ep*dt_).T*gi*(k + ep*dt_))[0, 0])
    check("T1e g_b0^-1(d(v + eps t), d(v + eps t)) = -2 eps - eps^2 (1 + mu/r^2): v + eps t is a time function with "
          "margin 2 eps, kept under |g^-1 - g_b0^-1| << eps (used on the bounded part of N in Omega')",
          sp.simplify(form + 2*ep + ep**2*(1 + mu/RR**2)) == 0, str(form))
    check("T1f control: at eps = 0 the margin is 0 (dv is null)", sp.simplify(form.subs(ep, 0)) == 0)


def t2():
    print("T2  the cap energies of the truncation")
    rr, T = sp.symbols("rr T", positive=True)
    res = {}
    for nm, q, a in (("b1 a0=1/4", 2, sp.Rational(1, 4)), ("b1 a0=9/20", 2, sp.Rational(9, 20)),
                     ("b1 a0=1/2", 2, sp.Rational(1, 2)), ("b2 q=9/2 a=11/4", sp.Rational(9, 2), sp.Rational(11, 4)),
                     ("b2 q=9/2 a=59/20", sp.Rational(9, 2), sp.Rational(59, 20)),
                     ("b2 q=4 a=11/4", 4, sp.Rational(11, 4))):
        # the cut region: r in [T, T + 1] (unit width in v at fixed t), |d(chi h)| ~ r^-q (the chi' term)
        e = sp.integrate(rr**(2*a)*rr**(-2*q)*rr**3, (rr, T, T + 1))
        res[nm] = sp.limit(e, T, sp.oo)
    print("     limits as |T| -> oo:", {k: str(v) for k, v in res.items()})
    check("T2a (b1): the cap energy tends to 0 at a0 = 1/4, 9/20", res["b1 a0=1/4"] == 0 and res["b1 a0=9/20"] == 0)
    check("T2b (b2): with q = 9/2 it tends to 0 at a = 11/4, 59/20", res["b2 q=9/2 a=11/4"] == 0
          and res["b2 q=9/2 a=59/20"] == 0)
    check("T2c controls: a0 = 1/2 (q = 2), and q = 4 at a = 11/4, do not tend to 0",
          res["b1 a0=1/2"] != 0 and res["b2 q=4 a=11/4"] != 0)


def t3():
    print("T3  the energy identity for a non-stationary metric (mpmath, 40 digits)")
    mp.mp.dps = 40
    m = sp.Rational(4, 5)
    k = [sp.Integer(1), x1/RR, x2/RR, x3/RR, x4/RR]
    eta = sp.diag(-1, 1, 1, 1, 1)
    q = ((t - sp.Rational(3, 10))**2 + (x1 - 1)**2 + (x2 + sp.Rational(1, 2))**2 + x3**2 + x4**2)/8
    cv = [[3, -2, 1, 4, -1], [-2, 5, 2, -3, 1], [1, 2, -4, 1, 3], [4, -3, 1, 2, -2], [-1, 1, 3, -2, 6]]
    hsym = sp.Matrix(5, 5, lambda i, j: sp.Rational(cv[i][j], 40)*sp.exp(-q)*(1 + t*x2/3))
    gsym = eta + m/RR**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j]) + hsym
    phisym = sp.Rational(1, 3)*t**2*x1 - x2*x3 + sp.Rational(2, 5)*t*x4**2 + x1*x2*x4 + sp.sin(t + x3)
    gf = sp.lambdify([XS], gsym, "mpmath")
    dgf = [sp.lambdify([XS], sp.diff(gsym, XS[c]), "mpmath") for c in range(5)]
    dphif = sp.lambdify([XS], [sp.diff(phisym, XS[c]) for c in range(5)], "mpmath")
    ddphif = sp.lambdify([XS], [[sp.diff(phisym, XS[a], XS[b]) for b in range(5)] for a in range(5)], "mpmath")
    R5 = range(5)

    def geo(y):
        g = mp.matrix(gf(y))
        return g, g**-1, mp.sqrt(abs(mp.det(g)))

    def cur(y, a, aa, with_w=True):
        g, gi, sq = geo(y)
        d = dphif(y)
        nrm = sum(gi[i, j]*d[i]*d[j] for i in R5 for j in R5)
        w = (mp.sqrt(sum(c*c for c in y[1:])) - y[0])**(2*aa)
        T0 = [d[b]*d[0] - g[b, 0]*nrm/2 for b in R5]
        return sq*w*sum(gi[a, b]*T0[b] for b in R5)

    def boxphi(y):
        def comp(a, z):
            yy = y[:a] + [z] + y[a + 1:]
            g, gi, sq = geo(yy)
            d = dphif(yy)
            return sq*sum(gi[a, j]*d[j] for j in R5)
        g, gi, sq = geo(y)
        return sum(mp.diff(lambda z: comp(a, z), y[a]) for a in R5)/sq

    worst, ctl, red = mp.mpf(0), mp.mpf(10)**9, mp.mpf(0)
    for aa in (mp.mpf(1)/4, mp.mpf(11)/4):
        for pt in ([0.3, 2.1, -1.2, 0.8, 1.5], [-1.4, 1.1, 1.9, -0.7, 0.6], [0.9, -1.6, 0.4, 2.2, -0.9]):
            y = [mp.mpf(c) for c in pt]
            g, gi, sq = geo(y)
            div = sum(mp.diff(lambda z: cur(y[:a] + [z] + y[a + 1:], a, aa), y[a]) for a in R5)/sq
            d = dphif(y)
            nrm = sum(gi[i, j]*d[i]*d[j] for i in R5 for j in R5)
            Tlow = [[d[a]*d[b] - g[a, b]*nrm/2 for b in R5] for a in R5]
            Tup = [[sum(gi[a, c]*gi[b, e]*Tlow[c][e] for c in R5 for e in R5) for b in R5] for a in R5]
            rr_ = mp.sqrt(sum(c*c for c in y[1:]))
            wv = (rr_ - y[0])**(2*aa)
            dw = [-2*aa*(rr_ - y[0])**(2*aa - 1)] + [2*aa*(rr_ - y[0])**(2*aa - 1)*c/rr_ for c in y[1:]]
            gw = [sum(gi[i, j]*dw[j] for j in R5) for i in R5]
            Tgt = sum(gw[b]*Tlow[b][0] for b in R5)
            dtg = mp.matrix(dgf[0](y))
            deform = wv*sum(Tup[a][b]*dtg[a, b] for a in R5 for b in R5)/2
            bp = boxphi(y)
            rhs = bp*wv*d[0] + Tgt + deform
            worst = max(worst, abs(div - rhs)/(1 + abs(div)))
            ctl = min(ctl, abs(div - (bp*wv*d[0] + Tgt))/(1 + abs(div)))
            # the reduced operator: g^ab d_a d_b phi = box_g phi + g^ab Gamma^c_ab d_c phi
            dd = ddphif(y)
            dg = [mp.matrix(dgf[c](y)) for c in R5]
            Gam = [[[sum(gi[c, s]*(dg[a][s, b] + dg[b][s, a] - dg[s][a, b]) for s in R5)/2 for b in R5] for a in R5]
                   for c in R5]
            red = max(red, abs(sum(gi[a, b]*dd[a][b] for a in R5 for b in R5)
                               - bp - sum(gi[a, b]*Gam[c][a][b]*d[c] for a in R5 for b in R5 for c in R5)))
    check("T3a div(T(X)) = (box_g phi) X phi + T(grad w, d_t) + (1/2) w T^ab d_t g_ab (relative, 6 cases)",
          worst < mp.mpf(10)**-20, mp.nstr(worst, 3))
    check("T3b g^ab d_a d_b phi = box_g phi + g^ab Gamma^c_ab d_c phi", red < mp.mpf(10)**-20, mp.nstr(red, 3))
    check("T3c control: without the deformation term the identity fails at every point", ctl > mp.mpf(10)**-6,
          mp.nstr(ctl, 3))


def t4():
    print("T4  the radial derivatives from the equation")
    r = sp.Symbol("r", positive=True)
    Ftt, Ftr, Frr, Fr = sp.symbols("F_tt F_tr F_rr F_r")
    xh = sp.symbols("y1:5", real=True)  # xhat, |xhat| = 1
    eta = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1] + list(xh))
    gi = eta - mu/r**2*(eta*k)*(eta*k).T
    # chain rule for F(t, |x|): d_i d_j F = F_rr y_i y_j + F_r (delta_ij - y_i y_j)/r, d_t d_i F = F_tr y_i
    hess = sp.zeros(5, 5)
    hess[0, 0] = Ftt
    for i in range(4):
        hess[0, i + 1] = hess[i + 1, 0] = Ftr*xh[i]
        for j in range(4):
            hess[i + 1, j + 1] = Frr*xh[i]*xh[j] + Fr*((1 if i == j else 0) - xh[i]*xh[j])/r
    op = sp.expand(sum(gi[a, b]*hess[a, b] for a in range(5) for b in range(5)))
    unit = {xh[3]: sp.sqrt(1 - xh[0]**2 - xh[1]**2 - xh[2]**2)}
    cr = sp.simplify(op.coeff(Frr).subs(unit))
    ct = sp.simplify(op.coeff(Ftt).subs(unit))
    ctr = sp.simplify(op.coeff(Ftr).subs(unit))
    check("T4a coefficients: F_rr (1 - mu/r^2), F_tt -(1 + mu/r^2), F_tr 2 mu/r^2: the radial second derivative is "
          "solved for where r^2 > mu", sp.simplify(cr - (1 - mu/r**2)) == 0 and sp.simplify(ct + 1 + mu/r**2) == 0
          and sp.simplify(ctr - 2*mu/r**2) == 0, f"{cr}, {ct}, {ctr}")
    check("T4b control: at r^2 = mu the F_rr coefficient vanishes", sp.simplify(cr.subs(r, sp.sqrt(mu))) == 0)


def t5():
    print("T5  (N2)'s flux identity on a dyadic piece (flat radial model)")
    tt, r = sp.symbols("tt r", real=True)
    vs, v1, tm, tp = sp.Rational(1, 2), sp.Integer(3), sp.Integer(-5), sp.Integer(-2)
    vv = tt + r
    phi = (vv - vs)**3*(1 + tt*r/7 - r**2/11)  # vanishes with two derivatives on v = v_start
    pt, pr = sp.diff(phi, tt), sp.diff(phi, r)
    box = -sp.diff(phi, tt, 2) + sp.diff(phi, r, 2) + 3*pr/r
    e = (pt**2 + pr**2)/2*r**3
    E = lambda T0: sp.integrate(e.subs(tt, T0), (r, vs - T0, v1 - T0))
    fluxN = sp.integrate(((pt - pr)**2/2*r**3).subs(tt, v1 - r), (r, v1 - tp, v1 - tm))
    bulk = sp.integrate(sp.integrate(sp.expand(pt*box*r**3), (r, vs - tt, v1 - tt)), (tt, tm, tp))
    lhs = E(tp) + fluxN
    rhs = E(tm) - bulk
    check("T5a E(tau_+) + int_N (1/2)(phi_t - phi_r)^2 r^3 = E(tau_-) - int int_D phi_t box phi r^3 (exact)",
          sp.simplify(lhs - rhs) == 0, f"both sides {sp.nsimplify(lhs) if False else sp.N(lhs, 12)}")
    bad = sp.integrate(((pt + pr)**2/2*r**3).subs(tt, v1 - r), (r, v1 - tp, v1 - tm))
    check("T5b control: with the transverse (phi_t + phi_r)^2 the identity fails", sp.simplify(E(tp) + bad - rhs) != 0)


def t6():
    print("T6  the dyadic sums with the powers of lam")
    lam, kk = sp.symbols("lambda kk", positive=True)
    n = sp.Symbol("n", integer=True, nonnegative=True)
    ok_far = True
    for a in (sp.Rational(1, 4), sp.Rational(9, 20)):
        s = sp.summation(2**(2*a*(n + 1))*2**(-n), (n, 0, sp.oo))
        ok_far = ok_far and s.is_finite
    s_half = sp.summation(2**(2*sp.Rational(1, 2)*(n + 1))*2**(-n), (n, 0, sp.oo))
    check("T6a far region: sum_k 2^(2a(k+1)) 2^-k is finite at a = 1/4, 9/20 (times M^2 lam^(2(K' - i)))", ok_far)
    check("T6b control: at a = 1/2 the far-region sum diverges", s_half == sp.oo)
    ok = True
    for b0 in (2, 3):
        for a in (sp.Rational(1, 4), sp.Rational(9, 20)):
            Kp = 2 + 2*b0 + 2*a + 1  # K' > 2 + 2 beta0 + 2a, with margin 1
            # piece k (t_P = 2^k <= lam^-2): 2^(2a(k+1)) lam^(2(K'-1)) 2^k (lam^-2 2^-k)^(2 beta0); worst k at an end
            piece = lambda kv: 2**(2*a*(kv + 1))*lam**(2*(Kp - 1))*2**kv*(lam**-2*2**(-kv))**(2*b0)
            K2 = sp.log(lam**-2, 2)
            worst = sp.Max(piece(0), piece(K2))
            tot = sp.simplify(K2*(piece(0) + piece(K2)))
            ok = ok and sp.limit(tot, lam, 0, "+") == 0
    check("T6c near region: log2(lam^-2) pieces, each <= lam^(2(K'-1) - 4 beta0 - 2(2a+1)); the sum -> 0 once "
          "K' > 2 + 2 beta0 + 2a (beta0 = 2, 3; a = 1/4, 9/20)", ok)


def t7():
    print("T7  the Cauchy sequence: tails")
    rr, T = sp.symbols("rr T", positive=True)
    a0 = sp.Rational(9, 20)
    tail1 = sp.integrate(rr**(2*a0)*rr**-6*rr**3, (rr, T, sp.oo))  # |ell h| ~ r^-3 (ell-gain), flux density
    a = sp.Rational(59, 20)
    tail2 = sp.integrate(rr**(2*a)*rr**-11*rr**3, (rr, T, sp.oo))  # |ell h_R| ~ r^(-11/2)
    check("T7a the flux tails on N beyond r = |T| tend to 0 (a0 = 9/20 with ell-gain; a = 59/20 for h_R)",
          sp.limit(tail1, T, sp.oo) == 0 and sp.limit(tail2, T, sp.oo) == 0, f"{tail1}, {tail2}")
    tail0 = sp.integrate(rr**0*rr**-4*rr**3, (rr, T, sp.oo))
    check("T7b control: without the ell-gain (|d h| ~ r^-2) the tail is infinite at a0 = 0", tail0 == sp.oo)


def t8():
    print("T8  (R2.6's wording) which incoming fields the weight a < 1/2 fails to exclude")
    rr, T, sv = sp.symbols("rr T sv", positive=True)
    a = sp.Rational(1, 4)
    # phi ~ r^(-3/2) F(v) at past null infinity; on the cap t = T, v = T + r = v1 + s, r = |T| + v1 + s ~ |T| + s:
    # the d_v part of |d phi|^2 r^3 is |F'(v1 + s)|^2 r^0, so the cap energy is int (|T| + s)^(2a) F'(v1 + s)^2 ds
    Fp = sp.exp(-(sv - 1)**2)*(-2*(sv - 1))
    capvar = sp.Integral((T + sv)**(2*a)*Fp**2, (sv, 0, sp.oo))
    ratio = [sp.N(capvar.subs(T, TT)/TT**(2*a), 12) for TT in (10**2, 10**4, 10**6)]
    lim = sp.N(sp.Integral(Fp**2, (sv, 0, sp.oo)), 12)
    check("T8a F varying in v: cap energy / |T|^(2a) -> int F'^2 > 0 (a = 1/4): grows like |T|^(2a), excluded",
          abs(ratio[-1] - lim) < 1e-3*lim and lim > 0, f"{[str(x) for x in ratio]} -> {lim}")
    capconst = sp.integrate(rr**(2*a)*rr**-5*rr**3, (rr, T, sp.oo))
    check("T8b F constant in v (an r^(-3/2) tail of the data on N): the cap energy |T|^(2a-1) -> 0 at a = 1/4 "
          "(round 2's S4c-d): this is what a < 1/2 fails to exclude", sp.limit(capconst, T, sp.oo) == 0)


def main():
    for f in (t1, t2, t4, t5, t6, t7, t8, t3):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
