#!/usr/bin/env python3
"""gdtail5.py -- GAUGEDECAY5.md Rounds 7-8: the t^-2 term of a gauge vector with compactly supported data, proved by
an explicit model and Theorem R6.4 carried past the window for sources of zero total charge; the spherically symmetric
part of the harmonic-gauge representative; and the bookkeeping of the slab order.  Repaired in round 8 as round 7's
verifier asks ((A84)): every control runs the computed path with a mutated input and must fail.

  T1 (exact) The time-domain model in flat n+1, n = 4.  The switched-on field of the charge Q_n delta_0, a = r^(2-n) -
     Q_n int_t^oo E_int d tau with E_int = (t^2 - r^2)^((1-n)/2)/(2 pi^((n-1)/2) Gamma((3-n)/2)) (Riesz's interior
     coefficient) and Q_n = (n - 2)|S^(n-1)|: it solves the radial equation, d_t a = Q_n E_int, a -> r^(2-n), a =
     t/(r^2 sqrt(t^2 - r^2)) and a - r^-2 = (1/2) t^-2 + O(t^-4).  Control: the same path at n = 3, where the
     coefficient vanishes (Gamma's pole; Huygens) and the t^-2 coefficient is 0.
  T2 (exact; the resolvent side formal) The coefficient the other way.  Round 6's D5 chain recomputed here with both
     components kept: P-hat(0) W* = 0 (u_0 in the kernel, which D5 did not check), and u_2's log r coefficients at r^0
     are -1/2 in dv and +1/2 in dr (recorded, not checked: their sum vanishes for every source O(r^-2)); with kappa_2 =
     -1/2 so computed, D6's formula gives the sigma log sigma coefficient -(i ell(f)/8 pi^2) d psi, and FT[t^-2 H(t -
     1)] = E_2(-i sigma) = 1 + (-i sigma) log(-i sigma) + analytic (sympy's expint series): the t^-2 coefficient (c/2) d
     psi, c = ell(f)/4 pi^2, equal to T1's and the model's (T6).  Control: W* with its dr component dropped is not in
     the kernel of P-hat(0).
  T3 (exact) The model in the far zone.  In the outgoing chart (u, r), g = -f du^2 - 2 du dr + r^2 gamma, with W* =
     r^-2 du + dr/(r(r - r_h)) and d psi = du + (1 + mu/(r(r - r_h))) dr (both solutions), E := Box(chi(u) W* + A(u, r)
     d psi) for arbitrary chi, A, reduced by the flat equation of a := chi r^-2 + A, vanishes at mu = 0 and is a sum
     of coefficients times chi', d_u A, d_r A, d_r^2 A; with the I+-orders of A (3/2, ..., d_r adding one) every term
     has I+-order >= 4.  The reduction is the one A obeys: with A = K, chi = 1 the flat relation holds and the
     Tangherlini one does not, and E equals the flat-reduced E and not the Tangherlini-reduced one.  With A = K E has
     I+-order >= 9/2 at fixed u and iota+-order 6 along u = lam r.  Control: without the flat reduction E does not
     vanish at mu = 0.
  T4 (exact) The model near compact sets.  In the ingoing chart, for every phi(v, r): Box(phi d psi) = (Box_0 phi) d psi
     - 2 nabla_{grad phi} d psi, and phi + const gives the same, so every term carries a derivative of phi.  With A =
     K(T, r), T = v - 2 r (A = chi_1' * K = K + O(T^-3)): T^2 A -> 1/2 (Lemma R7.2 (d)'s coefficient, read off the
     kernel) and the source is O(T^-3).  Control: dv - dr (not a solution) in place of d psi.
  T5 (exact) The charge: Q[phi(v, r) d psi] = -4 pi^2 r_h^3 d_r phi(v, r_h), Q[W*] = 4 pi^2, so Q[u_ex] -> 4 pi^2 and
     int ell(f_ex) = 4 pi^2.  Control: Q[phi W*] = 4 pi^2 phi, not a derivative.
  T6 (exact) The kernel K(w, r) = a(w + r, r) - r^-2 computed from T1's field: it is r^-2 ((w + r)/sqrt(w (w + 2 r))
     - 1), homogeneous of degree -2; K = (1/2) w^-2 - r w^-3 + O(w^-4) at fixed r, d_r K = -w^-3 + O(w^-4); r^(3/2) K
     -> (2 w)^(-1/2) at fixed w; K + r^-2 solves the flat equation in (u, r).  Control: the same path at n = 3 gives
     the kernel 0.
  T7 (exact, whole box) Theorem R7.1's conditions on its own box (alpha_K in (2, 3), gamma_+ in (alpha_K, 3), eps_1 in
     (0, 3 - gamma_+), eps in (0, eps_1/3], the endpoint included), and the model source's orders (I+ 4, iota+ 6, K+
     3) against (R6.1), each a positive sum.  Control: the same conditions with a nonzero charge, whose order-0
     equation needs the column in Y_0 at the weight beta_tf + 2, i.e. gamma_+ < 2, which fails on the box.
  T8 (exact) The spherically symmetric gauge data of the paper's own perturbations.  In III.B's outgoing Kerr-Schild
     chart near infinity, where the initial surface is {t = C''}: W**_H = W** - V^flat restricted to it has the r^-1
     tail (-dt + dr/4)/r, its t-derivative is W*/2 = O(r^-2), and K = r^-2 (dt - dr)^2 has normal components of order
     2: the data of Z^(K) are of order exactly 1 at spatial infinity.  Control: W* in place of W**_H has no r^-1 term.
  T9 (exact, whole box) Corollary R7.6's chain for homogeneous solutions with data of order p in (1/2, 3/2) at spatial
     infinity (a_0 < p - 3/2, alpha_I < a_0, p_slab = alpha_I + 3/2, 1/2 + beta < b_I < p_slab, gamma_+ < b_+ =
     1/2 + beta, alpha_K < gamma_+) reaches every alpha_K < min(p, 3/2); in the class p_0 >= min(1, q - 1) > 1/2 +
     2 gam > 1/2 + delta_#.  Control: p = 1/2 leaves the chain empty.
  T10 (exact, whole box) The slab order: every use of Z_1 at null infinity on the initial slab in the paper's
     statements (R4.4 / R3.6, R5.3 at kappa, and Corollary R8.11's l >= 2 part) asks p > 1/2 + beta, each beta computed
     from its statement's parameters, below Theorem R4.3's min(3/2, q - 1).  Control: with the source's margin delta_#
     replaced by 1 the asked orders exceed that bound.
  T11 (exact, whole box) Theorem R6.4's conditions with w_I = max(5/2, gamma_+ + 1 + eps_1) encoded and II.G'
     Proposition 3.3 (1) taken with eps_PP = min(eps, eps_1) (the round-6 verifier's minor on D2; a max or min handled
     exactly, argument by argument).  Control: Proposition 3.3's eps not reduced to min(eps, eps_1).
  T12 (exact) Lemma R7.2 (b)'s corners ((A78)): with chi = 1 the flat-reduced E is sum_m c_m(r) D_m K, D_m in {d_u,
     d_r, d_r^2}, c_m ~ r^-p_m; D_m K(lam r, r) = r^-d_m k_m(lam) exactly; with a_m, b_m the exponents of k_m at lam ->
     0, oo, every term has iota+-order p_m + d_m = 6, I+-order p_m + d_m + a_m >= 9/2 at iota+ cap I+ and K+-order
     -b_m >= 3 at iota+ cap K+.  Control: the degree -2 kernel K + 1/(r u) fails at K+.
Labels: computed (exact, sympy; T2's resolvent side recomputes round 6's formal D5-D6 chain; T7, T9, T10, T11 on the
whole parameter box).  Run: python3 checks/gdtail5.py   (a few minutes)
"""
import sys

import sympy as sp

from gdrad5 import box as pbox, positive_sum
from hgauge5 import A_EXPR, B_EXPR, GEO, Q_l0, WSTAR, delta1, hodge
from rwgauge5 import Geo, N, X, r, s, v, zero

HALF = sp.Rational(1, 2)
mu = s**2
_print = print


def print(*args, **kw):                                         # report lines wrapped at 121 characters
    import textwrap
    text = ' '.join(str(a_) for a_ in args)
    _print('\n'.join(textwrap.fill(ln, 121, subsequent_indent='      ', break_on_hyphens=False) if ln else ln
                     for ln in text.split('\n')), **kw)


class GeoOut(Geo):
    """-F du^2 - 2 du dr + r^2 gamma: the outgoing chart, the coordinate v of rwgauge5 standing for u"""

    def __init__(self, F):
        super().__init__(F)
        g = self.g
        g[0, 1] = g[1, 0] = -1
        self.g = g
        self.gi = sp.simplify(g.inv())
        gi = self.gi
        self.Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                - sp.diff(g[b, c], X[d])) for d in range(N))/2)
                      for c in range(N)] for b in range(N)] for a in range(N)]


def kernel(w, rr):
    return ((w + rr)/sp.sqrt(w*(w + 2*rr)) - 1)/rr**2


# --------------------------------------------------------------------------------------------------------------- T1
def switched_on(n):
    """the field of the charge Q_n delta_0 switched on at t = 0 in flat n+1, for t > r: a = r^(2-n) - Q_n int_t^oo
    E_int(tau, r) d tau, with E_int the interior part of the retarded fundamental solution of d_t^2 - Lap (Riesz):
    (t^2 - r^2)^((1-n)/2) / (2 pi^((n-1)/2) Gamma((3-n)/2)), and Q_n = (n - 2)|S^(n-1)| (so a -> r^(2-n))"""
    t, tau = sp.symbols('t tau', positive=True)
    cn = 1/(2*sp.pi**sp.Rational(n - 1, 2)*sp.gamma(sp.Rational(3 - n, 2)))        # 0 for odd n (Gamma's pole)
    Qn = (n - 2)*2*sp.pi**sp.Rational(n, 2)/sp.gamma(sp.Rational(n, 2))
    pw = sp.Rational(1 - n, 2)
    Eint = lambda T_: cn*(T_**2 - r**2)**pw
    if cn != 0:
        # tau = r (1 + Y): int_t^oo (tau^2 - r^2)^pw d tau = r^(2 pw + 1) [G(oo) - G(t/r - 1)], G' = (Y (Y + 2))^pw
        Y = sp.Symbol('Y', positive=True)
        G = sp.integrate((Y*(Y + 2))**pw, Y)
        assert sp.simplify(sp.diff(G, Y) - (Y*(Y + 2))**pw) == 0
        tail = cn*r**(2*pw + 1)*(sp.limit(G, Y, sp.oo) - G.subs(Y, t/r - 1))
    else:
        tail = sp.Integer(0)
    a = sp.simplify(r**(2 - n) - Qn*tail)
    return a, t, Eint, Qn


def t1(control=False):
    n = 3 if control else 4                                     # control: the same path in 3+1 (Huygens)
    a, t, Eint, Qn = switched_on(n)
    x = sp.Symbol('x', positive=True)
    eq = sp.simplify(sp.diff(a, t, 2) - sp.diff(a, r, 2) - (n - 1)/r*sp.diff(a, r))
    dta = sp.simplify(sp.diff(a, t) - Qn*Eint(t))
    stat = sp.limit(a, t, sp.oo)
    ser = sp.expand(sp.series((a - r**(2 - n)).subs(t, 1/x), x, 0, 6).removeO())
    coef = ser.coeff(x, 2)
    closed = sp.simplify(a - t/(r**2*sp.sqrt(t**2 - r**2))) == 0
    ok = eq == 0 and dta == 0 and sp.simplify(stat - r**(2 - n)) == 0 and coef == HALF and closed
    tag = "  T1 control (the same path in 3+1)" if control else "  T1"
    print("%s: n = %d, Riesz interior coefficient %s, Q_n = %s; a solves the radial equation: %s; d_t a = Q_n E_int: "
          "%s; a -> %s; a - r^(2-n) = %s; = t/(r^2 sqrt(t^2 - r^2)): %s; t^-2 coefficient %s, = 1/2: %s"
          % (tag, n, sp.simplify(Eint(t)*(t**2 - r**2)**sp.Rational(n - 1, 2)), Qn, eq == 0, dta == 0, stat,
             sp.collect(ser.subs(x, 1/t), t), closed, coef, coef == HALF), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T2
def chain_round6(kill_dr=False):
    """round 6's D5 chain (gdrad5.d5) recomputed here with both components of u_2 kept: returns (P-hat(0) W*,
    time and radial components of u_1 and u_2)"""
    from gdrad5 import chain_setup
    C = chain_setup()
    a, b, rr, f = C['a'], C['b'], C['r'], C['f']
    x = sp.Symbol('x', positive=True)

    def asym(e, n=7):
        ex = sp.expand(sp.simplify(e.subs(rr, 1/x)))
        ser = sp.series(ex, x, 0, n).removeO()
        return sp.expand(sp.expand(ser).subs(sp.log(x), -sp.log(rr)).subs(x, 1/rr))

    def integ(e):
        e = sp.expand(e)
        return sp.expand(sum(sp.integrate(tm, rr) for tm in e.as_ordered_terms())) if e != 0 else sp.Integer(0)

    def drop_const(e):
        e = sp.expand(e)
        return sp.expand(e - sum(tm for tm in e.as_ordered_terms() if not tm.has(rr)))

    def apply_op(op, A_, B_):
        return [sp.simplify(o.subs({sp.Derivative(a, rr): sp.diff(A_, rr), sp.Derivative(b, rr): sp.diff(B_, rr)})
                            .subs({a: A_, b: B_})) for o in op]

    def solve_P0(sv, sr, kill=True):
        q_ = integ(asym(rr**3*sv/f))
        ph_ = integ(asym(sr + sv/f))
        A_ = integ(asym(-q_/rr**3))
        if kill:
            A_ = drop_const(A_)
        S_ = integ(asym(-rr**3*ph_))
        return sp.expand(A_), sp.expand(asym((S_/rr**3 - A_)/f))

    A0, B0 = C['W'][0], (0 if kill_dr else C['W'][1])
    ker = [sp.simplify(z) for z in apply_op(C['P0'], A0, B0)]
    s1 = [sp.I*z for z in apply_op(C['L1'], A0, B0)]
    A1, B1 = solve_P0(s1[0], s1[1])
    s2 = [sp.I*z for z in apply_op(C['L1'], A1, B1)]
    A2, B2 = solve_P0(asym(s2[0]), asym(s2[1]), kill=False)
    k_t = sp.simplify(sp.expand(A2).coeff(sp.log(rr)).coeff(rr, 0))
    k_r = sp.simplify(sp.expand(B2).coeff(sp.log(rr)).coeff(rr, 0))
    return ker, A1, k_t, k_r


def t2(control=False):
    ker, A1, k_t, k_r = chain_round6(kill_dr=control)
    in_ker = all(z == 0 for z in ker)
    if control:
        print("  T2 control (W* with its dr component dropped): P-hat(0) u_0 = 0: %s" % in_ker, flush=True)
        return in_ker
    kap2 = k_t
    sg, L, lf, mu0, al, b0, a1, Qw = sp.symbols('sigma L ell_f mu alpha beta_0 a_1 Q_w')
    W, Kf, u1 = sp.symbols('W K u_1', commutative=True)
    Q = {W: 4*sp.pi**2, Kf: 4*sp.pi**2*mu0}
    u2L = b0*Kf + al*W
    qu = 4*sp.pi**2 + a1*sg + (b0*Q[Kf] + al*Q[W])*sg**2*L
    u = W + sg*u1 + sg**2*L*u2L
    expr = -(lf + sp.I*sg*Qw)/(sp.I*sg*qu)*u
    ser = sp.expand(sp.series(expr, sg, 0, 2).removeO())
    coef = sp.simplify(ser.coeff(sg, 1).coeff(L, 1))
    dpsi = mu0*W - Kf
    ratio = sp.simplify(coef/dpsi)
    z = sp.Symbol('z')
    e2 = sp.expand(sp.series(sp.expint(2, z), z, 0, 2).removeO())
    c_zlogz = sp.simplify(e2.coeff(sp.log(z)).coeff(z, 1))
    c_inf = sp.Symbol('c_inf')
    tail = sp.simplify((ratio.subs(b0, -kap2)*sp.I*c_zlogz).subs(lf, 4*sp.pi**2*c_inf))
    model = HALF*c_inf                                     # T1 and the model's A = (1/2) T^-2 (T6)
    # recorded, not checked: k_t + k_r = 0 holds for every source decaying like r^-2 (the round-7 verifier)
    killing = sp.simplify(k_t + k_r) == 0
    ok = in_ker and c_zlogz == 1 and sp.simplify(tail - model) == 0
    print("  T2: P-hat(0) W* = 0: %s; u_2's log r coefficients at r^0: dv %s, dr %s (recorded: k_t + k_r = 0 is %s, as "
          "for any source O(r^-2), not a check); "
          "sigma log sigma coefficient (%s) d psi; FT[t^-2 H(t-1)] = E_2(z), z = -i sigma, has z log z with coefficient "
          "%s; t^-2 tail from the resolvent (formal) (%s) d psi, from the time-domain model (%s) d psi: equal %s"
          % (in_ker, k_t, k_r, killing, sp.factor(ratio), c_zlogz, tail, model, sp.simplify(tail - model) == 0),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T3
_OUT = {}


def outgoing():
    if not _OUT:
        G = GeoOut(1 - mu/r**2)
        G0 = GeoOut(sp.Integer(1))
        _OUT.update(G=G, G0=G0)
    return _OUT['G'], _OUT['G0']


_FZ = {}


def far_zone():
    """E := Box(chi(u) W* + A(u, r) d psi) in the outgoing chart; the relations Box_0(chi r^-2 + A) = 0 for the flat and
    for the Tangherlini scalar operator, solved for d_u d_r A; E reduced by each"""
    if not _FZ:
        G, G0 = outgoing()
        u = v
        Ws = [1/r**2, 1/(r*(r - s)), 0, 0, 0]
        dps = [sp.Integer(1), 1 + mu/(r*(r - s)), 0, 0, 0]
        sol = all(zero(c) for c in hodge(G, Ws)[:2]) and all(zero(c) for c in hodge(G, dps)[:2])
        A = sp.Function('A')(u, r)
        chi = sp.Function('chi')(u)
        Y = [chi*Ws[i] + A*dps[i] for i in range(N)]
        E = [sp.expand(sp.simplify(c)) for c in hodge(G, Y)[:2]]
        phi = sp.Function('phi')(u, r)
        dudr = sp.Derivative(A, u, r)
        red = {}
        for name, GG in (("flat", G0), ("Tangherlini", G)):
            box0 = sp.expand(sp.simplify(delta1(GG, [sp.diff(phi, u), sp.diff(phi, r), 0, 0, 0])))
            rel = sp.expand(box0.subs(phi, chi/r**2 + A).doit())
            sol_dudr = sp.solve(rel, dudr)[0]
            red[name] = (rel, [sp.expand(sp.simplify(c.subs(dudr, sol_dudr))) for c in E])
        _FZ.update(G=G, u=u, A=A, chi=chi, E=E, red=red, sol=sol)
    return _FZ


def t3(control=False):
    FZ = far_zone()
    u, A, chi, E, sol = FZ['u'], FZ['A'], FZ['chi'], FZ['E'], FZ['sol']
    Ered = E if control else FZ['red']['flat'][1]
    flat0 = [sp.simplify(c.subs(s, 0)) for c in Ered]
    flat_ok = all(c == 0 for c in flat0)
    if control:
        print("  T3 control (no flat reduction): E at mu = 0 vanishes: %s" % flat_ok, flush=True)
        return flat_ok
    # the reduction is the one A obeys: with A = K, chi = 1 the flat relation holds and the Tangherlini one does not,
    # and E itself equals the flat-reduced E (not the Tangherlini-reduced one)
    Ksub = lambda e: sp.simplify(e.subs(chi, 1).doit().subs(A, kernel(u, r)).doit())
    rel_f, rel_T = FZ['red']['flat'][0], FZ['red']['Tangherlini'][0]
    holds_f = Ksub(rel_f) == 0
    holds_T = Ksub(rel_T) == 0
    EK = [Ksub(c) for c in E]
    match_f = all(sp.simplify(Ksub(c) - e_) == 0 for c, e_ in zip(FZ['red']['flat'][1], EK))
    match_T = all(sp.simplify(Ksub(c) - e_) == 0 for c, e_ in zip(FZ['red']['Tangherlini'][1], EK))
    consistent = holds_f and not holds_T and match_f and not match_T
    # monomials and their I+-orders: A, d_u A: 3/2; d_r A: 5/2; d_r^2 A: 7/2; chi, chi': 0
    ords = {A: HALF*3, sp.Derivative(A, u): HALF*3, sp.Derivative(A, r): HALF*5,
            sp.Derivative(A, (r, 2)): HALF*7, chi: 0, sp.Derivative(chi, u): 0}
    y = sp.Symbol('y', positive=True)
    worst = sp.oo
    report = []
    for c in Ered:
        c = sp.expand(c)
        for mon, o in ords.items():
            co = sp.expand(c).coeff(mon)
            co = sp.simplify(co.subs({m: 0 for m in ords if m != mon}))
            if co == 0:
                continue
            ser = sp.series(co.subs(r, 1/y), y, 0, 8).removeO()
            lead = min(sp.Poly(sp.expand(ser), y).monoms())[0] if ser != 0 else sp.oo
            worst = min(worst, lead + o)
            report.append((str(mon).replace('(v, r)', '').replace('(v)', '').replace(', v)', ', u)'), lead + o))
        rest = sp.simplify(c - sum(sp.expand(c).coeff(m)*m for m in ords))
        if rest != 0:
            worst = -sp.oo
    # with A = K(u, r) and chi = 1 (late): I+ at fixed u, iota+ along u = lam r
    uu, lam, z = sp.symbols('u_0 lambda z', positive=True)
    I_ord = []
    for c in EK:
        e = sp.simplify(c.subs({u: uu}).subs(r, 1/z**2))
        ser = sp.series(e, z, 0, 14).removeO()
        I_ord.append(sp.Rational(min(sp.Poly(sp.expand(ser), z).monoms())[0], 2) if ser != 0 else sp.oo)
    io_ord = []
    for c in EK:
        e = sp.simplify(c.subs(u, lam*r).subs(r, 1/z))
        ser = sp.series(e, z, 0, 9).removeO()
        io_ord.append(min(sp.Poly(sp.expand(ser), z).monoms())[0] if ser != 0 else sp.oo)
    ok = (sol and flat_ok and consistent and worst >= 4 and min(I_ord) >= sp.Rational(9, 2)
          and min(io_ord) >= 6)
    print("  T3: W*, d psi solve Box in the outgoing chart: %s; E reduced by the flat equation vanishes at mu = 0: %s; "
          "with A = K, chi = 1 the flat relation holds: %s, the Tangherlini one: %s, E = flat-reduced E: %s, = "
          "Tangherlini-reduced E: %s; I+-orders of its terms %s (least %s); with A = K, chi = 1: I+-orders %s, "
          "iota+-orders %s" % (sol, flat_ok, holds_f, holds_T, match_f, match_T,
                               sorted(set(report), key=lambda p_: (p_[1], p_[0]))[:6], worst, I_ord, io_ord),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T4
def t4(control=False):
    phi = sp.Function('phi')(v, r)
    c0 = sp.Symbol('c_0')
    Fp = -(r**2 + r*s + s**2)/(r*(r + s))                      # d psi = dv + F' dr (round 2's B5)
    form = [sp.Integer(1), sp.Integer(-1), 0, 0, 0] if control else [sp.Integer(1), Fp, 0, 0, 0]
    BX = [sp.simplify(c) for c in hodge(GEO, [phi*f_ for f_ in form])]
    BXc = [sp.simplify(c) for c in hodge(GEO, [(phi + c0)*f_ for f_ in form])]
    deriv_only = all(zero(BX[i] - BXc[i]) for i in range(N))
    if control:
        print("  T4 control (dv - dr in place of d psi): every term carries a derivative of phi: %s" % deriv_only,
              flush=True)
        return deriv_only
    box0phi = sp.simplify(delta1(GEO, [sp.diff(phi, v), sp.diff(phi, r), 0, 0, 0]))
    cov = GEO.cov1(form)
    grad = [sum(GEO.gi[m, n_]*sp.diff(phi, X[n_]) for n_ in range(2)) for m in range(N)]
    rhs = [box0phi*form[c] - 2*sum(grad[m]*cov[m][c] for m in range(N)) for c in range(N)]
    formula = all(zero(BX[c] - rhs[c]) for c in range(N))
    # A near compact sets: A(T, r) = int chi_1'(s) K(T - s, r) ds = K(T, r) + O(T^-3) (int chi_1' = 1, d_T K =
    # O(T^-3)), T = v - 2 r; the coefficient 1/2 of Lemma R7.2 (d) read off the kernel itself, and the source O(T^-3)
    vv = sp.Symbol('w', positive=True)
    Ak = kernel(v - 2*r, r)
    coef2 = sp.limit(sp.simplify(Ak.subs(v, vv + 2*r))*vv**2, vv, sp.oo)
    coef3 = sp.limit(sp.simplify((Ak.subs(v, vv + 2*r) - coef2/vv**2))*vv**3, vv, sp.oo)
    src = [sp.simplify(c.subs(phi, Ak).doit()) for c in BX[:2]]
    order = [sp.limit(sp.simplify(e.subs(v, vv + 2*r))*vv**3, vv, sp.oo) for e in src]
    finite = all(o.is_finite for o in order)
    ok = deriv_only and formula and finite and coef2 == HALF
    print("  T4: Box(phi d psi) = (Box_0 phi) d psi - 2 nabla_grad phi d psi for phi(v, r): %s; phi + const gives the "
          "same (every term differentiates phi): %s; with A = K(T, r), T = v - 2 r: T^2 A -> %s (= 1/2: %s), T^3 (A - "
          "T^-2/2) -> %s; T^3 x source -> %s (finite: %s)"
          % (formula, deriv_only, coef2, coef2 == HALF, sp.simplify(coef3), [sp.simplify(o) for o in order], finite),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T5
def t5(control=False):
    phi = sp.Function('phi')(v, r)
    Fp = -(r**2 + r*s + s**2)/(r*(r + s))
    form = WSTAR if control else [sp.Integer(1), Fp, 0, 0, 0]
    Q = sp.simplify(Q_l0(GEO, [phi*c for c in form]).doit())
    target = -4*sp.pi**2*s**3*sp.Subs(sp.Derivative(phi, r), r, s).doit()
    target = sp.simplify(-4*sp.pi**2*s**3*sp.diff(phi, r).subs(r, s))
    QW = sp.simplify(Q_l0(GEO, WSTAR))
    if control:
        is_deriv = sp.simplify(Q.subs(phi, sp.Symbol('c_0')).doit()) == 0
        print("  T5 control (phi W*): Q = %s; a pure derivative of phi: %s" % (Q, is_deriv), flush=True)
        return is_deriv
    ok = sp.simplify(Q - target) == 0 and sp.simplify(QW - 4*sp.pi**2) == 0
    print("  T5: Q[phi d psi] = %s (= -4 pi^2 r_h^3 d_r phi at r_h: %s); Q[W*] = %s" % (Q, sp.simplify(Q - target) == 0,
                                                                                    QW), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T6
def t6(control=False):
    w, lam, x = sp.symbols('w lambda x', positive=True)
    n = 3 if control else 4                                     # control: the kernel the same path gives in 3+1
    a, t, _, _ = switched_on(n)
    K = sp.simplify(a.subs(t, w + r) - r**(2 - n))              # the kernel computed from T1's field, w = t - r > 0
    same = sp.simplify(K - kernel(w, r)) == 0
    hom = sp.simplify(K.subs({w: lam*w, r: lam*r}, simultaneous=True) - K/lam**2) == 0
    ser = sp.expand(sp.series(K.subs(w, 1/x), x, 0, 5).removeO())
    c2, c3 = ser.coeff(x, 2), ser.coeff(x, 3)
    dser = sp.expand(sp.series(sp.diff(K, r).subs(w, 1/x), x, 0, 5).removeO())
    I_lim = sp.limit(r**sp.Rational(3, 2)*K, r, sp.oo)
    u = v
    G, G0 = outgoing()
    phi = sp.Function('phi')(u, r)
    box0 = delta1(G0, [sp.diff(phi, u), sp.diff(phi, r), 0, 0, 0])
    flat = sp.simplify(box0.subs(phi, K.subs(w, u) + 1/r**2).doit())
    ok = (same and hom and c2 == HALF and sp.simplify(c3 + r) == 0 and dser.coeff(x, 3) == -1
          and sp.simplify(I_lim - 1/sp.sqrt(2*w)) == 0 and flat == 0)
    tag = "  T6 control (the same path in 3+1)" if control else "  T6"
    print("%s: K from T1's field = the kernel of Lemma R7.2: %s; homogeneous of degree -2: %s; K = %s + O(w^-4); d_r K "
          "= %s + O(w^-4); r^(3/2) K -> %s; K + r^-2 solves the flat equation in (u, r): %s"
          % (tag, same, hom, sp.collect(ser.subs(x, 1/w), w), dser.coeff(x, 3)/w**3, I_lim, flat == 0), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T7
def t7(control=False):
    (x1, x2, x3, x4), (y1, y2, y3, y4) = pbox('x1', 'x2', 'x3', 'x4')
    aK = 2 + y1                                                 # alpha_K in (2, 3)
    gp = aK + y2*(3 - aK)                                       # gamma_+ in (alpha_K, 3) = (alpha_K, min(3, aK + 1))
    bt = gp - 1                                                 # beta_tf
    e1 = y3*(3 - gp)                                            # eps_1 in (0, 3 - gamma_+): Theorem R7.1's box
    pos = [x1, x2, x3, x4]
    cond = {}
    for tagE, ep in (("eps < eps_1/3", y4*e1/3), ("eps = eps_1/3", e1/3)):  # eps in (0, eps_0], eps_0 = eps_1/3
        wI = gp + 1 + e1                                        # w_I (>= 5/2 as gamma_+ > 2)
        cond.update({
            "window gamma_+ - alpha_K > 0": gp - aK, "window < 1": 1 - (gp - aK),
            "order 0: beta_tf in (0, 2)": bt, "beta_tf < 2 (W* in the domain)": 2 - bt,
            "order 1: beta_tf - 1 > 0": bt - 1, "order 1: beta_tf - 1 < 1": 2 - bt,
            "column in Y_0 at beta_tf + 1": 3 - (bt + 1),
            "zf of sigma^2 terms: alpha_K - 1 < 2": 3 - aK,
            "column difference tf: 4 - eps >= beta_tf + 2 (%s)" % tagE: 2 - bt - ep,
            "column difference zf: 2 - eps > alpha_K - 1 (%s)" % tagE: 3 - aK - ep,
            "scf: min(w_I, gamma_+ + 2) >= 5/2": wI - sp.Rational(5, 2),
            "Prop 3.3 (1): w_I >= gamma_+ + 1 + eps (%s)" % tagE: wI - (gp + 1 + ep),
            "Lemma 4.1: w_I - 1 >= 3/2": wI - sp.Rational(5, 2),
            "Prop 2.8 (2): alpha_K - 1 in (1, 2)": aK - 2,
            "model I+: 4 > w_I": 4 - wI, "model iota+: 6 > gamma_+ + 2": 4 - gp, "model K+: 3 > alpha_K": 3 - aK,
            "eps small: 3 - gamma_+ > 3 eps (%s)" % tagE: 3 - gp - 3*ep,
        })
    if control:
        # the same path with a nonzero total charge: the order-0 equation then needs the column in Y_0 at beta_tf + 2
        cond["column in Y_0 at beta_tf + 2 (charge != 0)"] = 3 - (bt + 2)
    res = {k: positive_sum(e, pos) for k, e in cond.items()}
    ok = all(res.values())
    tag = "  T7 control (the same conditions with a nonzero charge)" if control else "  T7"
    bad = [k for k, val in res.items() if not val]
    print("%s: %d conditions on Theorem R7.1's box (eps_1 < 3 - gamma_+, eps <= eps_1/3), all positive sums: %s%s"
          % (tag, len(res), ok, "; failing %s" % bad if bad else ""), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T8
def t8(control=False):
    t, C2 = sp.symbols('t C2', positive=True)
    m_ = sp.Symbol('m', positive=True)
    z = sp.Symbol('z', positive=True)
    Tm = sp.sqrt(m_)*sp.log((r + sp.sqrt(m_))/(r - sp.sqrt(m_)))
    T0 = Tm.subs(m_, mu)
    dmuT = sp.diff(Tm, m_).subs(m_, mu)
    vv = t + r - T0
    f = 1 - mu/r**2
    # a 1-form X_v dv + X_r dr in the (t, r) chart: dv = dt + (1 - T') dr
    Tp = sp.diff(T0, r)

    def to_tr(Xv, Xr):
        return [Xv, Xv*(1 - Tp) + Xr]
    Wv, Wr = WSTAR[0], WSTAR[1]
    if control:
        comp = to_tr(Wv, Wr)
    else:
        Wss = to_tr(vv/2*Wv + A_EXPR, vv/2*Wr + B_EXPR)
        Vflat = [dmuT*f, dmuT*mu/r**2]                          # V = -d_mu T d_t, (d_t)^flat = (-f, -mu/r^2)
        comp = [Wss[0] - Vflat[0], Wss[1] - Vflat[1]]
    on = [c.subs(t, C2) for c in comp]
    tail, nxt = [], []
    for c in on:
        lead = sp.limit(r*c, r, sp.oo)
        tail.append(sp.simplify(lead))
        nxt.append(sp.limit(r**2*(c - lead/r)/sp.log(r), r, sp.oo))   # the remainder is O(r^-2 log r)
    if control:
        print("  T8 control (W*): r^-1 coefficients on {t = C''} %s; a nonzero r^-1 tail: %s"
              % (tail, any(c != 0 for c in tail)), flush=True)
        return any(c != 0 for c in tail)
    dt_comp = [sp.simplify(sp.diff(c, t)) for c in comp]
    dt_lim = [sp.limit(sp.simplify(c*r**2), r, sp.oo) for c in dt_comp]
    # K = d_mu g_mu at fixed (t, x), g_mu of III.B (3.4): -f dt^2 - 2 mu r^-2 dt dr + (2 - f) dr^2
    gm = [[-(1 - m_/r**2), -m_/r**2], [-m_/r**2, 1 + m_/r**2]]
    Kn = [sp.simplify(sp.diff(gm[0][0], m_)), sp.simplify(sp.diff(gm[0][1], m_))]   # K(d_t, d_t), K(d_t, d_r)
    ok = (tail == [-1, sp.Rational(1, 4)] and all(l_.is_finite for l_ in dt_lim) and all(n_.is_finite for n_ in nxt)
          and Kn == [1/r**2, -1/r**2])
    print("  T8: W**_H on {t = C''} has the r^-1 tail (%s dt + %s dr)/r; r^2 d_t W**_H -> %s (= W*/2: order 2); K's "
          "normal components %s (order 2): the data of Z^(K) have order exactly 1" % (tail[0], tail[1], dt_lim, Kn),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T9
def t9(control=False):
    (x1, x2, x3, x4, x5, x6, x7), (y1, y2, y3, y4, y5, y6, y7) = pbox('x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7')
    pos = [x1, x2, x3, x4, x5, x6, x7]
    p = HALF if control else HALF + y1                         # data order p in (1/2, 3/2)
    target = sp.Min(p, sp.Rational(3, 2))
    aK = HALF + y7*(p - HALF)                                   # the rate exponent reached: any alpha_K in (1/2, p)
    # chain from the top: gamma_+ in (alpha_K, b_+), b_+ = 1/2 + beta < b_I < p_slab < p, a_0 in (alpha_I, p - 3/2)
    gp = aK + y2*(p - aK)/4
    bp = gp + y3*(p - gp)/4
    beta = bp - HALF
    bI = bp + y4*(p - bp)/4
    pslab = bI + y5*(p - bI)/4
    aI = pslab - sp.Rational(3, 2)
    a0 = aI + y6*(p - sp.Rational(3, 2) - aI)
    cond = {"a_0 < p - 3/2": p - sp.Rational(3, 2) - a0, "alpha_I < a_0": a0 - aI, "alpha_I < 0": -aI,
            "p_slab > 1/2 + beta": pslab - HALF - beta, "beta > 0": beta, "b_I > b_+": bI - bp,
            "p_slab > b_I": pslab - bI, "b_I < 3/2": sp.Rational(3, 2) - bI, "gamma_+ < b_+": bp - gp,
            "alpha_K < gamma_+": gp - aK, "alpha_K >= 1/2": aK - HALF,
            "gamma_+ < 2 (R6.4) / 3/2 (R5.1)": sp.Rational(3, 2) - gp}
    res = {k: positive_sum(e, pos) for k, e in cond.items()}
    if control:
        bad = [k for k, val in res.items() if not val]
        print("  T9 control (p = 1/2): conditions failing %s" % bad, flush=True)
        return all(res.values())
    # in the class: p_0 >= min(1, q - 1), q > 3/2 + 2 gam, gam in (0, 1/4), delta_# = (1 - e) gam, e in (0, 1)
    (a1, a2, a3), (b1, b2, b3) = pbox('a1', 'a2', 'a3')
    gam = b1/4
    q = sp.Rational(3, 2) + 2*gam + a2
    e_ = b3
    dsh = (1 - e_)*gam
    cls = {"1 - (1/2 + delta_#)": 1 - HALF - dsh, "(q - 1) - (1/2 + 2 gam)": q - 1 - HALF - 2*gam,
           "2 gam - delta_#": 2*gam - dsh}
    cres = {k: positive_sum(e, [a1, a2, a3]) for k, e in cls.items()}
    ok = all(res.values()) and all(cres.values())
    print("  T9: Corollary R7.6's chain on the box, every alpha_K < min(p, 3/2) reached: %s; in the class p_0 > 1/2 + "
          "2 gam > 1/2 + delta_#: %s" % (all(res.values()), cres), flush=True)
    return ok


# -------------------------------------------------------------------------------------------------------------- T10
def t10(control=False):
    (x1, x2, x3, x4, x5), (y1, y2, y3, y4, y5) = pbox('x1', 'x2', 'x3', 'x4', 'x5')
    pos = [x1, x2, x3, x4, x5]
    gam = y1/4
    dsh = sp.Integer(1) if control else (1 - y2)*gam            # control: the source's margin delta_# taken as 1
    q = sp.Rational(3, 2) + 2*gam + y3
    kap = y4*dsh                                                # R5.3's rate exponent: kappa < delta_#
    beta53 = (kap + dsh)/2                                      # R5.3's choice
    gp = HALF + y4*dsh                                          # Corollary R8.11: gamma_+ in (1/2, 1/2 + delta_#)
    beta811 = (gp - HALF) + (dsh - (gp - HALF))*y5              # beta in (gamma_+ - 1/2, delta_#)
    uses = {"R4.4 / R3.6: p > 1/2 + beta, beta in (0, delta_#)": HALF + y5*dsh,
            "R5.3 at kappa: p > 1/2 + beta, beta = (kappa + delta_#)/2": HALF + beta53,
            "l >= 2 (Corollary R8.11): p > 1/2 + beta, beta in (gamma_+ - 1/2, delta_#)": HALF + beta811}
    res = {}
    for k, need in uses.items():
        # need < 3/2 and need < q - 1, each a positive sum
        res[k] = positive_sum(sp.Rational(3, 2) - need, pos) and positive_sum(q - 1 - need, pos)
    extra = positive_sum(beta53 - kap, pos) and positive_sum(dsh - beta53, pos)
    ok = all(res.values()) and extra
    tag = "  T10 control (delta_# replaced by 1)" if control else "  T10"
    print("%s: each required slab order below Theorem R4.3's min(3/2, q - 1): %s; kappa < beta < delta_#: %s"
          % (tag, res, extra), flush=True)
    return ok


# -------------------------------------------------------------------------------------------------------------- T11
def t11(control=False):
    """Theorem R6.4's conditions with w_I encoded (the round-6 verifier's minor on D2): alpha_K in (1, 2), gamma_+ in
    (alpha_K, 2), eps_1 in (0, 1/2), eps in (0, (2 - gamma_+)/5], w_I := max(5/2, gamma_+ + 1 + eps_1), and II.G'
    Proposition 3.3 (1) taken with eps_PP := min(eps, eps_1).  A max on the left (a min on the right) is handled
    exactly: the condition holds if it holds for one argument (for every argument), each a positive sum or 0."""
    (x1, x2, x3, x4), (y1, y2, y3, y4) = pbox('x1', 'x2', 'x3', 'x4')
    pos = [x1, x2, x3, x4]
    aK = 1 + y1
    gp = aK + y2*(2 - aK)
    e1 = y3/2
    ep = y4*(2 - gp)/5
    WI = [sp.Rational(5, 2), gp + 1 + e1]                       # w_I = max(WI)
    EPP = [ep] if control else [ep, e1]                         # eps_PP = min(EPP)

    def nonneg(e):
        e = sp.simplify(e)
        return e == 0 or positive_sum(e, pos)

    def maxge(args, rhs):                                       # max(args) >= rhs
        return any(nonneg(a_ - rhs) for a_ in args)

    def ge(lhs, rhs_args_max):                                  # lhs >= max(rhs_args)
        return all(nonneg(lhs - a_) for a_ in rhs_args_max)
    cond = {
        "Lemma 4.1: w_I - 1 >= 3/2": maxge(WI, sp.Rational(5, 2)),
        "Lemma 4.1: w_I >= gamma_+ + 1 + eps_1": maxge(WI, gp + 1 + e1),
        # Prop 3.3 (1): w_I >= gamma_+ + 2 - (1 - eps_PP): for eps_PP = min(EPP) it suffices for one argument of EPP
        "Prop 3.3 (1): w_I >= gamma_+ + 1 + eps_PP": any(maxge(WI, gp + 1 + e_) for e_ in EPP),
        # scf: min(w_I, gamma_+ + 2) - eps_PP >= 5/2 - eps, i.e. both w_I and gamma_+ + 2 >= 5/2 - eps + eps_PP
        "scf (w_I)": any(maxge(WI, sp.Rational(5, 2) - ep + e_) for e_ in EPP),
        "scf (gamma_+ + 2)": any(nonneg(gp + 2 - (sp.Rational(5, 2) - ep + e_)) for e_ in EPP),
        "step 3.1: 0 < gamma_+ - 1 < 1": nonneg(gp - 1) and nonneg(2 - gp),
        "column: gamma_+ + 1 < 3": nonneg(2 - gp),
        "f_2 tf: gamma_+ + 1 <= 3 - eps": nonneg(2 - gp - ep),
        "f_2 zf: alpha_K - 1 < 1 - eps": nonneg(2 - aK - ep),
        "density: b_+ = 1 <= gamma_+, b_I + 1 = 9/4 <= w_I": nonneg(gp - 1) and maxge(WI, sp.Rational(9, 4)),
        "step 3.3: eps <= (2 - gamma_+)/5": nonneg((2 - gp)/5 - ep),
        "window: 0 < gamma_+ - alpha_K < 1": nonneg(gp - aK) and nonneg(1 - (gp - aK)),
    }
    ok = all(cond.values())
    bad = [k for k, val in cond.items() if not val]
    tag = "  T11 control (Prop 3.3's eps not reduced to min(eps, eps_1))" if control else "  T11"
    print("%s: %d conditions with w_I = max(5/2, gamma_+ + 1 + eps_1), all hold on the box: %s%s"
          % (tag, len(cond), ok, "; failing %s" % bad if bad else ""), flush=True)
    return ok


# -------------------------------------------------------------------------------------------------------------- T12
def t12(control=False):
    """Lemma R7.2 (b): the joint orders of E[K] at the corners iota+ cap I+ and iota+ cap K+ (the round-7 verifier's
    finding).  With chi = 1, E (reduced by the flat equation, which K obeys: T3) is a sum c_m(r) D_m A over D_m in
    {d_u, d_r, d_r^2}, c_m rational in r with leading power r^-p_m at infinity.  K is homogeneous of degree -2, so
    D_m K(lam r, r) = r^(-d_m) k_m(lam) exactly, d_m = 3, 3, 4.  Near iota+ cap I+ (rho_+ = 1/u, rho_I = lam = u/r)
    the term is rho_+^(p_m + d_m) rho_I^(p_m + d_m + a_m), a_m the exponent of k_m at lam -> 0; near iota+ cap K+
    (rho_+ = 1/r, rho_K = 1/lam) it is rho_+^(p_m + d_m) rho_K^(-b_m), b_m the exponent at lam -> oo.  Lower-order
    terms of c_m add powers of 1/r and only raise these orders; b-derivatives (lam d_lam, r d_r) keep the forms."""
    FZ = far_zone()
    u, A, chi = FZ['u'], FZ['A'], FZ['chi']
    Ered = [sp.expand(c.subs(chi, 1).doit()) for c in FZ['red']['flat'][1]]
    lam, z, y = sp.symbols('lambda z y', positive=True)
    Kk = kernel(u, r) + (1/(r*u) if control else 0)             # control: a degree -2 kernel decaying like 1/(r u)
    mons = [(sp.Derivative(A, u), 3, lambda e: sp.diff(e, u)), (sp.Derivative(A, r), 3, lambda e: sp.diff(e, r)),
            (sp.Derivative(A, (r, 2)), 4, lambda e: sp.diff(e, r, 2))]
    others = [A] + [m_ for m_, _, _ in mons]
    rows, ok = [], True
    for ic, c in enumerate(Ered):
        rest = sp.simplify(c - sum(c.coeff(m_)*m_ for m_, _, _ in mons))
        ok &= rest == 0                                          # neither A nor chi undifferentiated
        for m_, dm, D in mons:
            co = sp.simplify(c.coeff(m_).subs({o: 0 for o in others if o != m_}))
            if co == 0:
                continue
            ser = sp.series(co.subs(r, 1/y), y, 0, 8).removeO()
            pm = min(sp.Poly(sp.expand(ser), y).monoms())[0]
            km = sp.simplify(D(Kk).subs({u: lam*r}).subs(r, 1)*1)        # D_m K(lam, 1); homogeneity checked below
            hom = sp.simplify(D(Kk).subs(u, lam*r) - r**(-dm)*km) == 0
            s0 = sp.series(sp.simplify(km.subs(lam, z**2)), z, 0, 6).removeO()
            am = sp.Rational(min(sp.Poly(sp.expand(s0*z**8), z).monoms())[0] - 8, 2)
            s1 = sp.series(sp.simplify(km.subs(lam, 1/y)), y, 0, 8).removeO()
            bm = -min(sp.Poly(sp.expand(s1), y).monoms())[0]
            io, iI, iK = pm + dm, pm + dm + am, -bm
            rows.append((ic, str(m_).replace('(v, r)', '').replace(', v)', ', u)'), pm, dm, am, bm, io, iI, iK, hom))
            ok &= hom and io >= 6 and iI >= sp.Rational(9, 2) and iK >= 3
    tag = "  T12 control (kernel K + 1/(r u))" if control else "  T12"
    print("%s: (component, D_m, p_m, d_m, a_m, b_m, iota+, I+ at the corner, K+ at the corner, homogeneous): %s; "
          "joint orders >= (6, 9/2) and (6, 3): %s" % (tag, rows, ok), flush=True)
    return ok


CHECKS = [("T1", t1), ("T2", t2), ("T3", t3), ("T4", t4), ("T5", t5), ("T6", t6), ("T7", t7), ("T8", t8),
          ("T9", t9), ("T10", t10), ("T11", t11), ("T12", t12)]


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
