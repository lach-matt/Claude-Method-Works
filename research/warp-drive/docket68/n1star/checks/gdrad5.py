#!/usr/bin/env python3
"""gdrad5.py -- GAUGEDECAY5.md Round 6: III.I''' Proposition 2.1 with Lemmas 1.1-1.3 carried over to the 1-form wave
operator Box on Tangherlini (K+-weights alpha_K in (1, 2)), the rate it gives for gauge vectors with compactly
supported data, the low-frequency expansion of Box's resolvent (formal), the sharpness of the harmonic-gauge exponent
in its source class, III.I' at Box (the expansion at null infinity), and the corrected checks the verifiers of rounds
4 and 5 asked for.  Every check has a control that mutates the code path under test and must fail.

  D1 (exact) III.I''' Lemmas 1.2-1.3 at Box.  (a) The column: in flat 4+1 on the l = 0 time component,
     r^4 [Box_0, chi(r/t)] r^-2 is a function of r/t alone, so the column's time transform is r^-3 G(sigma r) (III.H
     Lemma 2.4 (a)'s form, the order 3 of Lemma 1.2 (b)); control: the Killing form's component r^0 gives r^2 g(r/t).
     (b) The Fubini count: for r^-q H, |H| <= min(sigma r, 1), the squared (N, g_tf, g_zf) norm on {sigma <x> <= 1}
     is finite iff g_zf < 1 and g_tf < q: q = 3 for the column (Lemma 1.2 (b)), q = 2 for W* (Lemma 1.3); and
     sigma^j chi_zf P u_0 (Lemma 1.1 (a)) iff g_zf < j and g_tf <= a + p + j.  (c) The cut-off state's tf-order
     computed with the weight W_beta of II.G' Lemma 4.6 (not assigned): ||W_beta^-1 Phi(sigma r) r^-q||_{L^2(mu_b)}
     = sigma^(q - eps) (2 eps)^(-1/2) (1 + o(1)) for Phi = exp(-z^2), q = 2 (W* in A^2).  Controls: (a) as said;
     (b) q = 1 (the Killing form's column) gives g_tf < 1; (c) q = 0 ((d_v)^flat) gives the order -eps.
  D2 (exact, whole box) Theorem R6.4's weight conditions (III.I''' Proposition 2.1 at Box: Steps 3.1-3.4 with one
     integration) on alpha_K in (1, 2), gamma_+ in (alpha_K, 2), w_I >= gamma_+ + 1 + eps_1 free, eps small: each a
     positive sum on the box; and Theorem R5.1's conditions with w_I a box variable from its minimum and the condition
     gamma_+ <= 3/2 - 2 eps of its step 7 (the round-5 verifier's minor 3).  Control: without the zero-energy step 3.1
     the transform's zf-weight is that of its Taylor term, 0, below Lemma 4.2's beta_zf = alpha_K - 1.
  D3 (exact) The coefficient B at alpha_K in (1, 2): the transform of (1 + t^2)^(-alpha_K/2) is B-hat(0) + C
     |sigma|^(alpha_K - 1) + O(sigma^2) (II.G' Definition 2.7 with a constant polynomial part, the same for both
     signs, equal to int B), at alpha_K in {11/10, 5/4, 3/2, 19/10}.  Control (the main path at the integer):
     alpha_K = 2, where the one-sided t^-2 tail's transform carries w log w (no power law; the window's end).
  D4 (exact) The rate.  With Theorem R6.4, kappa_sup(a) = min(3/2, a - 5/2) for a source of iota+-order a (sources
     with compact support: every kappa < 3/2, so t^(-2+eps)); the harmonic-gauge source a = 5/2 + delta_# keeps kappa
     < delta_#.  Control: without step 3.1 (alpha_K < 1) the compact-support exponent is 1/2.
  D5 (exact; formal expansion) The low-frequency chain of Box on Tangherlini, l = 0, retarded frame T = v - 2 r_*:
     P-hat(sigma) = P-hat(0) - i sigma L_1 exactly (L_2 = 0), P-hat(0) = (r^-3 f q', phi' - r^-3 q') (round 2's B5);
     u_0 = W*, u_1 solves P-hat(0) u_1 = i L_1 W*: its time component -i/r + O(r^-3), no logarithm; u_2's time
     component carries -(1/2) log r at the root 0.  So the first non-smooth term of the resolvent is sigma log sigma,
     one order above sigma^0 (the round-4 verifier's m1).  Control: with u_0 = r W* the chain has -(i/2) log r already
     at order sigma.
  D6 (exact series; formal) The sigma log sigma coefficient.  From P-hat(sigma)^-1 f = w - (d/c) u (III.D' Proposition
     4.1, Step 1), with u = W* + sigma u_1 + sigma^2 log sigma u_2L + ..., c ell(psi) = i sigma q(sigma, u): the
     coefficient is -(ell(f)/(4 pi^2 i))(u_2L - (Q[u_2L]/4 pi^2) W*), which for u_2L = beta_0 (d_v)^flat + alpha W* is
     -beta_0 (ell(f)/(4 pi^2 i)) (-d psi), independent of alpha; FT[t_+^-2] = (-i sigma) log(-i sigma) + analytic.
     So, formally, Y - c W* = (c/2) t^-2 d psi + o(t^-2), c = Q[Y]/4 pi^2.  Control: the charge's sigma^2 log sigma
     term dropped from c (sigma), the coefficient keeps alpha.
  D7 (exact) Sharpness in the class.  For phi = phi(v): Box(phi d psi) = (Box_0 phi) d psi - 2 nabla_{grad phi} d psi
     with Box_0 phi = -3 phi'/r; Q[phi(v) d psi] = 0 identically; L_{phi d psi} g = mu phi L_{W*} g + 2 phi' dv (x)_s
     d psi; with phi = v^(2-a) the source is O(v^(1-a) r^-1): iota+-order a, K+-order a - 1.  Control: W* in place of
     d psi has Q != 0.
  D8 (exact, whole box) The round-4 verifier's m2: T3's S4 and S7 rows with b_I = (b_+ + p)/2, p in (1/2 + beta,
     P), P = min(3/2, q - 1), q > 3/2 + 2 gam, alpha >= 4 free.  Control: T3's old b_I = (beta + 2)/2 against p in
     the new range fails at gam = 1/20.
  D9 (exact) E4 of gdext5.py recomputed, with a control that mutates its normalisation (rho^(-1-alpha)).
  D10 (exact) E3 of gdext5.py: the conjugation by rho (n = 3) run through the same radial and full 1-form pipeline.
  D11 (exact) G4 (b) of gdrate5.py with the convergence computed by integration; control at a = beta + 3.
  D12 (exact, rational samples) E6 of gdext5.py with the source's I+-weight computed and the interval reported.
  D13 (exact) III.I' Lemma 1.1 and Proposition 3.1 at Box: rho_I^-1 rho_+^-2 Box_0 = (X_+ - X_I)(X_I - 3/2) + rho_I
     (smooth) in III.I's chart, the coupling of Box gaining rho_I^2, and L_0 (rho_I^z u) = rho_I^z (z - 3/2)(X_+ - z) u.
     Control: n = 3 gives the root 1.

Labels: computed (exact, sympy; D5-D6 compute a formal expansion; D8 and D2 on the whole parameter box, D12 at exact
rational samples).  Run: python3 checks/gdrad5.py   (about ten minutes)
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

HALF = sp.Rational(1, 2)


def positive_sum(expr, pos):
    """expr equals a quotient of polynomials in the 'pos' symbols (each in (0, oo)) whose coefficients all have one
    sign, the same for numerator and denominator: a sufficient, exact test of positivity on the open box"""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    if num.is_number and den.is_number:
        return bool(num/den > 0)
    Nm, Dn = sp.Poly(sp.expand(num), *pos), sp.Poly(sp.expand(den), *pos)

    def allpos(P):
        return not P.is_zero and all(c > 0 for c in P.coeffs())

    def allneg(P):
        return not P.is_zero and all(c < 0 for c in P.coeffs())
    return (allpos(Nm) and allpos(Dn)) or (allneg(Nm) and allneg(Dn))


def box(*names):
    syms = sp.symbols(' '.join(names), positive=True)
    return syms, [S/(1 + S) for S in syms]


# --------------------------------------------------------------------------------------------------------------- D1
def d1(control=False):
    t, r, lam = sp.symbols('t r lambda', positive=True)
    chi = sp.Function('chi')

    def box0(u):                                            # flat 4+1, l = 0 (sign immaterial)
        return -sp.diff(u, t, 2) + sp.diff(u, r, 2) + 3/r*sp.diff(u, r)
    q_state = 0 if control else 2                           # (d_v)^flat ~ dt: r^0; W* ~ dt/r^2: r^-2
    st = r**(-q_state)
    com = box0(chi(r/t)*st) - chi(r/t)*box0(st)
    ex = sp.simplify((r**(q_state + 2)*com).subs(t, r/lam).doit())
    homog = not ex.has(r)
    # (b) Fubini: int_1^oo r^(-2q + 2 + 2(gtf - gzf)) [int_0^(1/r) s^(2 - 2 gzf) ds/s] r^-1 dr
    gt, gz, sg, a_, p_ = sp.symbols('g_tf g_zf sigma a p', real=True)
    res = {}
    for q in ((1, 2, 3) if control else (2, 3)):
        inner = sp.integrate(sg**(1 - 2*gz), (sg, 0, 1/r), conds='none')     # valid for g_zf < 1
        integrand = r**(-2*q + 2 + 2*(gt - gz))*inner*r**-1
        res[q] = sp.expand(sp.expand_log(sp.log(integrand*(2 - 2*gz)), force=True)).coeff(sp.log(r))
    thr = {q: sp.solve(sp.Eq(res[q], -1), gt)[0] for q in res}               # finite iff exponent < -1
    zf_cond = sp.integrate(sg**(1 - 2*sp.Rational(1, 2)), (sg, 0, 1))      # g_zf = 1/2: finite
    zf_edge = sp.integrate(sg**(1 - 2*1), (sg, sp.Rational(1, 10**8), 1))  # g_zf = 1: log divergence
    # Lemma 1.1 (a): int |sigma|^(2j) rho^(-2(gtf - gzf)) |sigma|^(-2 gzf) 1_{sigma <= rho/4} dsigma/sigma
    j = sp.Symbol('j', positive=True)
    inner11 = sp.integrate(sg**(2*j - 2*gz - 1), (sg, 0, 1/(4*r)), conds='none')     # valid for g_zf < j
    w11 = sp.expand(sp.expand_log(sp.log(inner11*r**(2*(gt - gz))*(2*j - 2*gz)), force=True)).coeff(sp.log(r))
    l11 = sp.simplify(w11 - (2*gt - 2*j))                                    # the weight rho^(-2(g_tf - j))
    # (c) the cut-off state with W_beta: rho-hat = 1/z, W^-1 = (1 + z)^N (z/(1 + z))^(q - eps)
    z, eps = sp.symbols('z epsilon', positive=True)
    qc = 0 if control else 2
    rows = []
    okc = True
    for e_ in (sp.Rational(1, 4), sp.Rational(1, 10)):
        Nn = 3
        g = (1 + z)**(2*Nn)*(z/(1 + z))**(2*(qc - e_))*sp.exp(-2*z**2)*z**(-2*qc)      # times sigma^(2 qc)
        main = sp.integrate(sp.expand(sp.series(g, z, 0, 1).removeO())/z, (z, sg, 1))
        total = sg**(2*qc)*main                                                    # the squared norm, near 0
        order2 = sp.limit(sp.log(total)/sp.log(sg), sg, 0)                         # computed, not assigned
        lead = sp.limit(total/sg**order2, sg, 0)
        rows.append((str(e_), lead, order2/2))
        okc &= sp.simplify(order2/2 - (2 - e_)) == 0 and lead == 1/(2*e_)
    ok = (homog and thr.get(3) == 3 and thr.get(2) == 2 and zf_cond.is_finite and zf_edge > 18
          and l11 == 0 and okc)
    if control:
        print("  D1 control (the Killing form's component r^0 / q = 1 / q = 0): r^2 [Box_0, chi] r^0 homogeneous of "
              "degree 0: %s; tf thresholds %s; cut-off state (eps, lim, order) %s; the claims hold: %s"
              % (homog, thr, rows, homog and okc), flush=True)
        return homog and okc
    print("  D1: r^4 [Box_0, chi(r/t)] r^-2 = %s, a function of r/t alone: %s, so the column's transform is r^-3 G(sigma"
          " r); Fubini: finite iff g_zf < 1 and g_tf < q, thresholds %s (q = 3 column, q = 2 W*); Lemma 1.1 (a) weight "
          "rho^(2(g_tf - j)) exactly: %s; cut-off state with W_beta, (eps, lim sigma^(2 eps) int, tf-order) = %s"
          % (sp.simplify(ex), homog, thr, l11 == 0, rows), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D2
def d2(control=False):
    (U1, U2, U3, U4), (u1, u2, u3, u4) = box('U1', 'U2', 'U3', 'U4')
    pos = [U1, U2, U3, U4]
    aK = 1 + u1                                              # (1, 2)
    gp = aK + u2*(2 - aK)                                    # (alpha_K, 2)
    ep = u3*(2 - gp)/5                                       # small
    e1 = u4/2                                                # eps_1 in (0, 1/2)
    conds = {
        'zero energy alpha + 2 = g - 1 in (0,1)': [gp - 1, 2 - gp],
        'Y_0: column A^3 at mu_b-weight g + 1 < 3': [2 - gp],
        'window g - a_K in (0,1)': [gp - aK, 1 - (gp - aK)],
        'f2 tf: g + 1 <= 3 - eps': [(3 - ep) - (gp + 1)],
        'f2 zf: a_K - 1 < 1 - eps': [(1 - ep) - (aK - 1)],
        'L4.1 beta_K = a_K non-integer in (1,2)': [aK - 1, 2 - aK],
        'L4.2 beta_scf = 3/2 - eps < 3/2; source scf >= 5/2 - eps': [ep, (gp + 2 - ep) - (sp.Rational(5, 2) - ep)],
        'L1.3 tf(chi G_1) = min(2, a_K + 1) - eps >= beta_iota = g': [(2 - ep) - gp, (aK + 1 - ep) - (2 - ep)],
        'L3.1 beta_iota = g > beta_I = 1 + g - a_K': [aK - 1],
        'L3.1 beta_K = a_K - 1 in (0, 1)': [aK - 1, 2 - aK],
        'II.G 2.8 beta = a_K in (1, 2), one Taylor term': [aK - 1, 2 - aK],
        'II.F b_+ = 1 <= g, b_I = 5/4 < 3/2': [gp - 1],
    }
    # w_I >= max(5/2, g + 1 + eps_1) is the hypothesis; what is asked of it is dominated by those two bounds
    conds['L4.1 / (2.25a): g + 2 - min(a_K, 1 - eps_1) = g + 1 + eps_1'] = [aK - (1 - e1)]
    conds['II.F source I+: b_I + 1 = 9/4 <= 5/2'] = [sp.Rational(5, 2) - sp.Rational(9, 4)]
    if control:
        # step 3.1 dropped: Lemma 4.2 is applied to f-hat itself, whose zf part is ((0,0), a_K - 1): its plain zf-weight
        # is 0, which must be >= beta_zf = a_K - 1
        ok = positive_sum(sp.simplify(0 - (aK - 1)), pos)
        print("  D2 control (step 3.1 dropped): the transform's plain zf-weight 0 >= beta_zf = a_K - 1 on the box: %s"
              % ok, flush=True)
        return ok
    res = {k: all(positive_sum(sp.simplify(e), pos) for e in v) for k, v in conds.items()}
    # Theorem R5.1's box (round-5 verifier's minor 3): a_K in [1/2, 1), gamma_+ in (a_K, 3/2), eps <= (3/2 - g)/5,
    # w_I from its minimum max(5/2, g + 2 - a_K)
    (V1, V2, V3), (v1, v2, v3) = box('V1', 'V2', 'V3')
    posv = [V1, V2, V3]
    a5 = HALF + v1/2
    g5 = a5 + v2*(sp.Rational(3, 2) - a5)
    e5 = v3*(sp.Rational(3, 2) - g5)/5
    b5p = (HALF + g5)/2
    b5I = (b5p + sp.Rational(3, 2))/2
    c5 = {'step 7: g <= 3/2 - 2 eps': [(sp.Rational(3, 2) - 2*e5) - g5],
          'L4.3 tf a_K + 1 - eps >= g': [(a5 + 1 - e5) - g5],
          'window': [g5 - a5, 1 - (g5 - a5)],
          # w_I >= max(5/2, g + 2 - a_K) is the hypothesis; (2.25a)'s g + 2 - min(a_K, 1 - eps') equals the second
          # bound for eps' < 1 - a_K, and II.F's b_I + 1 is below the first
          '(2.25a) with eps\' = (1 - a_K)/2': [(1 - (1 - a5)/2) - a5],
          'II.F b_I + 1 <= 5/2': [sp.Rational(5, 2) - (b5I + 1)],
          'II.F b_+ <= g, 1/2 < b_+ < b_I < 3/2': [g5 - b5p, b5p - HALF, b5I - b5p, sp.Rational(3, 2) - b5I]}
    res5 = {k: all(positive_sum(sp.simplify(e), posv) for e in v) for k, v in c5.items()}
    print("  D2: Theorem R6.4's conditions, each a positive sum on the box a_K in (1,2), g in (a_K, 2), eps, eps_1, w_I "
          "from its minimum: %s; Theorem R5.1's box with w_I free and step 7's g <= 3/2 - 2 eps: %s"
          % (all(res.values()), all(res5.values())), flush=True)
    if not all(res.values()):
        print("    failing:", [k for k, v in res.items() if not v], flush=True)
    return all(res.values()) and all(res5.values())


# --------------------------------------------------------------------------------------------------------------- D3
def d3(control=False):
    w, t = sp.symbols('w t', positive=True)
    rows = []
    ok = True
    samples = [sp.Integer(2)] if control else [sp.Rational(11, 10), sp.Rational(5, 4), sp.Rational(3, 2),
                                               sp.Rational(19, 10)]
    for aK in samples:
        if aK == 2:
            # the main path at the integer: the one-sided t^-aK tail, transform at sigma = i w (Laplace)
            tr = sp.integrate(sp.exp(-w*t)*(1 + t)**(-aK), (t, 0, sp.oo))
            ser = sp.series(sp.simplify(tr), w, 0, 2).removeO()
            power_law = not sp.expand(ser).has(sp.log)
            rows.append((str(aK), sp.simplify(ser), power_law))
            ok &= power_law
            continue
        nu = (aK - 1)/2
        # FT of (1 + t^2)^(-s), s = a_K/2: (2 sqrt(pi)/Gamma(s)) (|sigma|/2)^nu K_nu(|sigma|), nu = s - 1/2
        Kser = sp.gamma(nu)/2*(w/2)**(-nu) + sp.gamma(-nu)/2*(w/2)**nu            # K_nu(w) to O(w^(2 - nu))
        B_hat = sp.expand(2*sp.sqrt(sp.pi)/sp.gamma(aK/2)*(w/2)**nu*Kser)
        const = sp.simplify(B_hat.subs(w, 0)) if not B_hat.subs(w, 0).has(sp.zoo) else None
        integral = sp.integrate((1 + t**2)**(-aK/2), (t, -sp.oo, sp.oo))
        sing = sp.simplify(B_hat - const) if const is not None else None
        expo = sp.simplify(sp.log(sp.simplify(sing/sing.subs(w, 1)))/sp.log(w)) if sing is not None else None
        good = (const is not None and sp.simplify(const - integral) == 0 and expo is not None
                and sp.simplify(expo - (aK - 1)) == 0)
        # the membership threshold of II.G' Definition 2.1 at beta = a_K: <t>^(beta - 1/2) t^-a_K in L^2 iff beta < a_K
        be = sp.Symbol('beta')
        thr = sp.solve(sp.Eq(2*(be - HALF) - 2*aK, -1), be)[0]
        rows.append((str(aK), good, thr))
        ok &= good and thr == aK
    if control:
        print("  D3 control (main path at a_K = 2): (a_K, transform near 0, a power law) = %s" % rows, flush=True)
        return ok
    print("  D3: (a_K, transform = int B + C |sigma|^(a_K - 1) + O(sigma^2) with the constant = int B, the K+ threshold "
          "beta = a_K) = %s" % rows, flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D4
def kappa_sup(a, aK_max=2, g_max=2):
    """sup of alpha_K - 1/2 over alpha_K in [1/2, aK_max) for which gamma_+ exists with alpha_K < gamma_+ <
    min(g_max, a - 2) and gamma_+ - alpha_K < 1 (Fourier-Motzkin by hand: the bounds are linear)"""
    up = min(g_max, a - 2)
    top = min(aK_max, up)                                     # alpha_K < gamma_+ < up; window automatic below
    return max(Fr(0), top - Fr(1, 2))


def d4(control=False):
    aKm = 1 if control else 2
    samples = [Fr(5, 2) + Fr(k, 40) for k in range(1, 40)] + [Fr(7, 2), Fr(4), Fr(10**6)]
    agree = all(kappa_sup(a, aKm) == min(Fr(aKm) - Fr(1, 2), a - Fr(5, 2)) for a in samples)
    compact = kappa_sup(Fr(10**6), aKm)                        # compactly supported source: every iota+-order
    gauge = [(d, kappa_sup(Fr(5, 2) + d, aKm)) for d in (Fr(1, 100), Fr(1, 10), Fr(1, 5))]
    gauge_ok = all(k == d for d, k in gauge)
    ok = agree and compact == Fr(3, 2) and gauge_ok
    if control:
        print("  D4 control (step 3.1 dropped, a_K < 1): compact-support kappa_sup = %s, not 3/2: %s"
              % (compact, compact != Fr(3, 2)), flush=True)
        return compact == Fr(3, 2)
    print("  D4: kappa_sup(a) = min(3/2, a - 5/2) at %d samples: %s; compactly supported source: kappa_sup = %s (rate "
          "t^(-2+eps)); harmonic-gauge source a = 5/2 + delta_#: %s" % (len(samples), agree, compact, gauge),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D5
_CHAIN = {}


def chain_setup():
    if _CHAIN:
        return _CHAIN
    from hgauge5 import GEO, hodge, WSTAR, delta1, dform
    from rwgauge5 import v, r, s
    sig = sp.Symbol('sigma')
    f = 1 - s**2/r**2
    a, b = sp.Function('a')(r), sp.Function('b')(r)
    Rf = sp.Function('R')(r)
    ph = sp.exp(-sp.I*sig*(v - 2*Rf))
    H = hodge(GEO, [ph*a, ph*b, 0, 0, 0])
    P = [sp.expand(sp.simplify(H[i]/ph)) for i in (0, 1)]
    rep = {sp.Derivative(Rf, (r, 2)): sp.diff(1/f, r), sp.Derivative(Rf, r): 1/f}
    P = [sp.expand(p.subs(rep)) for p in P]
    _CHAIN.update(dict(P0=[p.coeff(sig, 0) for p in P], L1=[sp.simplify(p.coeff(sig, 1)/(-sp.I)) for p in P],
                       L2=[sp.simplify(-p.coeff(sig, 2)) for p in P], a=a, b=b, r=r, s=s, f=f, W=WSTAR,
                       delta1=delta1, dform=dform, GEO=GEO))
    return _CHAIN


def d5(control=False):
    C = chain_setup()
    a, b, r, s, f = C['a'], C['b'], C['r'], C['s'], C['f']
    x = sp.Symbol('x', positive=True)

    def asym(e, n=7):
        ex = sp.expand(sp.simplify(e.subs(r, 1/x)))
        ser = sp.series(ex, x, 0, n).removeO()
        return sp.expand(sp.expand(ser).subs(sp.log(x), -sp.log(r)).subs(x, 1/r))

    def integ(e):
        e = sp.expand(e)
        return sp.expand(sum(sp.integrate(tm, r) for tm in e.as_ordered_terms())) if e != 0 else sp.Integer(0)

    def drop_const(e):
        e = sp.expand(e)
        return sp.expand(e - sum(tm for tm in e.as_ordered_terms() if not tm.has(r)))

    def apply_op(op, A, B):
        return [sp.simplify(o.subs({sp.Derivative(a, r): sp.diff(A, r), sp.Derivative(b, r): sp.diff(B, r)})
                            .subs({a: A, b: B})) for o in op]

    def solve_P0(sv, sr, kill=True):
        q_ = integ(asym(r**3*sv/f))
        ph_ = integ(asym(sr + sv/f))
        A = integ(asym(-q_/r**3))
        if kill:
            A = drop_const(A)
        S = integ(asym(-r**3*ph_))
        return sp.expand(A), sp.expand(asym((S/r**3 - A)/f))

    # the operator: L_2 = 0, and P-hat(0) is round 2's B5 form
    Yst = [a, b, 0, 0, 0]
    phi = C['delta1'](C['GEO'], Yst)
    q = r**3*C['dform'](Yst)[0][1]
    b5 = [sp.simplify(C['P0'][0] - f*sp.diff(q, r)/r**3), sp.simplify(C['P0'][1] - (sp.diff(phi, r)
                                                                                     - sp.diff(q, r)/r**3))]
    struct = C['L2'] == [0, 0] and b5 == [0, 0]
    A0, B0 = C['W'][0], C['W'][1]
    if control:
        A0, B0 = r*A0, r*B0                                     # a state decaying like r^-1 (the verifier's chain)
    s1 = [sp.I*z for z in apply_op(C['L1'], A0, B0)]
    A1, B1 = solve_P0(s1[0], s1[1])
    res1 = [sp.simplify(asym(sp.expand(z - y), 5)) for z, y in zip(apply_op(C['P0'], A1, B1), s1)]
    log1 = sp.expand(A1).coeff(sp.log(r))
    if control:
        print("  D5 control (u_0 = r W*): the time component of u_1 = %s; a logarithm at order sigma: %s"
              % (sp.collect(A1, sp.log(r)), log1 != 0), flush=True)
        return log1 == 0
    lead1 = sp.limit(A1*r, r, sp.oo)
    s2 = [sp.I*z for z in apply_op(C['L1'], A1, B1)]
    A2, B2 = solve_P0(asym(s2[0]), asym(s2[1]), kill=False)
    kappa2 = sp.simplify(sp.expand(A2).coeff(sp.log(r)).coeff(r, 0))
    ok = struct and res1 == [0, 0] and log1 == 0 and lead1 == -sp.I and kappa2 == -HALF
    _CHAIN['kappa2'] = kappa2
    print("  D5: L_2 = 0 and P-hat(0) = (r^-3 f q', phi' - r^-3 q'): %s; time component of u_1 = %s (no log: %s, "
          "residual of P-hat(0) u_1 - i L_1 W* to O(r^-5): %s); coefficient of log r at r^0 in u_2's time component: %s"
          % (struct, sp.collect(A1, r), log1 == 0, res1, kappa2), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D6
def d6(control=False):
    sg, L, lf, mu0, al, b0, a1, Qw, k2 = sp.symbols('sigma L ell_f mu alpha beta_0 a_1 Q_w kappa_2')
    W, K, u1, w0 = sp.symbols('W K u_1 w_0', commutative=True)        # W*, (d_v)^flat, placeholders
    Q = {W: 4*sp.pi**2, K: 4*sp.pi**2*mu0}                             # H3's charges
    u2L = b0*K + al*W
    QuL = b0*Q[K] + al*Q[W]
    # c ell(psi) = i sigma q(sigma, u),  d ell(psi) = ell(f) + i sigma q(sigma, w); L stands for log sigma
    qu = 4*sp.pi**2 + a1*sg + (0 if control else QuL)*sg**2*L
    qw = Qw
    u = W + sg*u1 + sg**2*L*u2L
    expr = -(lf + sp.I*sg*qw)/(sp.I*sg*qu)*u
    ser = sp.expand(sp.series(expr, sg, 0, 2).removeO())
    coef = sp.simplify(sp.expand(ser).coeff(sg, 1).coeff(L, 1))
    dpsi = mu0*W - K
    ratio = sp.simplify(coef/dpsi)
    indep = not ratio.has(al) and not ratio.has(W) and not ratio.has(K)
    # FT[t_+^-2]: finite part of Gamma(s) w^-s at s = -1, w = -i sigma
    s_, w = sp.symbols('s w', positive=True)
    e_ = sp.Symbol('e')
    ft = sp.series(sp.gamma(-1 + e_)*w**(1 - e_), e_, 0, 1).removeO()
    fp = sp.expand(sp.expand_log(sp.expand(ft.coeff(e_, 0)), force=True))
    c_wlogw = sp.simplify(fp.coeff(sp.log(w)).coeff(w, 1))
    if control:
        print("  D6 control (the charge's sigma^2 log sigma dropped): sigma log sigma coefficient %s, a multiple of "
              "d psi independent of alpha: %s" % (coef, indep), flush=True)
        return indep
    kap2 = _CHAIN.get('kappa2', -HALF)
    # beta_0 = -kappa_2 ((d_v)^flat ~ -dt at infinity); sigma log sigma = i (-i sigma) log(-i sigma) + analytic
    tail = sp.simplify((ratio*dpsi).subs(b0, -kap2)*sp.I*c_wlogw/dpsi)
    c_inf = sp.Symbol('c_inf')
    tail_c = sp.simplify(tail.subs(lf, 4*sp.pi**2*c_inf))
    ok = indep and c_wlogw == 1 and sp.simplify(tail_c - c_inf/2) == 0
    print("  D6: sigma log sigma coefficient of -(d/c) u = %s = (%s) d psi, independent of alpha: %s; FT[t_+^-2] has "
          "(-i sigma) log(-i sigma) with coefficient %s; with beta_0 = -kappa_2 = %s the t^-2 tail is (%s) d psi"
          % (coef, ratio, indep, c_wlogw, -kap2, tail_c), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D7
def d7(control=False):
    from hgauge5 import GEO, hodge, Q_l0, WSTAR, delta1
    from rwgauge5 import v, r, s, N
    mu0 = s**2
    f = 1 - mu0/r**2
    phi = sp.Function('phi')(v)
    Fp = -(r**2 + r*s + s**2)/(r*(r + s))                     # psi = v + F (round 2's B5)
    dpsi = [sp.Integer(1), Fp, 0, 0, 0]
    form = WSTAR if control else dpsi
    Y = [phi*c for c in form]
    Q = sp.simplify(Q_l0(GEO, Y))
    if control:
        print("  D7 control (W* in place of d psi): Q[phi(v) W*] = %s, not 0: %s" % (Q, Q != 0), flush=True)
        return Q == 0
    BX = [sp.simplify(c) for c in hodge(GEO, Y)]
    box0phi = sp.simplify(-sum(sp.diff(sp.sqrt(-GEO.g.det())*0, v) for _ in [0]))  # placeholder, replaced below
    # Box_0 phi(v) = -r^-3 d_r(r^3 g^{rv} phi') = -3 phi'/r
    box0phi = -sp.diff(r**3*sp.diff(phi, v), r)/r**3
    cov = GEO.cov1(dpsi)
    grad = [sum(GEO.gi[m, n]*sp.diff(phi, [v, r][n]) for n in range(2)) for m in range(N)]
    rhs = [sp.simplify(box0phi*dpsi[c] - 2*sum(grad[m]*cov[m][c] for m in range(N))) for c in range(N)]
    ok_box = all(sp.simplify(BX[c] - rhs[c]) == 0 for c in range(N))
    lieY = GEO.lie(Y)
    lieW = GEO.lie(WSTAR)
    dv = [1, 0, 0, 0, 0]
    sym = [[(dv[i]*dpsi[j] + dv[j]*dpsi[i]) for j in range(N)] for i in range(N)]
    ok_lie = all(sp.simplify(lieY[i][j] - mu0*phi*lieW[i][j] - sp.diff(phi, v)*sym[i][j]) == 0
                 for i in range(N) for j in range(N))
    lw = sp.simplify(lieW[0][1].subs(r, 2*s))
    # orders: phi = v^(2 - a): the source along r = lam v, times v^(a-1) r, has a finite nonzero limit
    aa, lam = sp.symbols('a lambda', positive=True)
    src = [sp.simplify(z.subs(phi, v**(2 - aa)).doit()) for z in BX[:2]]
    lim = [sp.limit(sp.simplify((z*v**(aa - 1)*r).subs(r, lam*v)), v, sp.oo) for z in src]
    ok_ord = any(sp.simplify(l_) != 0 and l_.is_finite is not False for l_ in lim)
    ok = Q == 0 and ok_box and ok_lie and lw != 0 and ok_ord
    print("  D7: Q[phi(v) d psi] = %s; Box(phi d psi) = (Box_0 phi) d psi - 2 nabla_grad phi d psi, Box_0 phi = -3 "
          "phi'/r: %s; L_{phi d psi} g = mu phi L_{W*} g + 2 phi' dv (x)_s d psi: %s; (L_{W*} g)_vr at r = 2 r_h = %s; "
          "source with phi = v^(2-a) along r = lam v: v^(a-1) r (Box Y)_(v,r) -> %s" % (Q, ok_box, ok_lie, lw, lim),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- D8
def d8(control=False):
    (D, U, S, W, A, G, E), (_, u, sv, wv, _, gv, ev) = box('D', 'U', 'S', 'W', 'A', 'G', 'E')
    pos = [D, U, S, W, A, G, E]
    d = D/(4*(1 + D))                                        # delta_# = (1 - e) gam in (0, 1/4)
    beta = u*d
    eta = ev*(d - beta)
    P = HALF + 2*d + wv*(1 - 2*d)                            # covers min(3/2, q - 1) > 1/2 + 2 gam >= 1/2 + 2 delta_#
    p = HALF + beta + sv*(P - HALF - beta)
    bp = HALF + beta
    bI = (bp + p)/2
    alpha = 4 + A
    lam = sp.Rational(3, 2) + d
    if control:
        # the old encoding b_I = (beta + 2)/2 with p from the new range, at gam = 1/20, e = 0, beta = d/2, q - 1 at
        # its least: p < 0.6
        gam = sp.Rational(1, 20)
        dd = gam
        bb = dd/2
        Pv = HALF + 2*gam
        pv = HALF + bb + sp.Rational(1, 2)*(Pv - HALF - bb)
        old = pv - (bb + 2)/2
        print("  D8 control (old b_I = (beta + 2)/2): at gam = 1/20, p = %s, b_I = %s, p > b_I: %s"
              % (pv, (bb + 2)/2, old > 0), flush=True)
        return bool(old > 0)
    conds = {
        'S4 b_I < 3/2': sp.Rational(3, 2) - bI,
        'S4 b_+ < b_I': bI - bp,
        'S4 b_+ > 1/2': bp - HALF,
        'S7 p > b_I': p - bI,
        'p < P <= 3/2': [P - p, sp.Rational(3, 2) - P],
        'p > 1/2 + beta': p - HALF - beta,
        'K4 h K+: alpha - 2 - eta > 1/2': (alpha - 2 - eta) - HALF,
        'K4 h iota+': (lam - eta) - (sp.Rational(3, 2) + beta),
        'S4 iota+': (lam + 1 - eta) - (beta + sp.Rational(5, 2)),
    }
    res = {}
    for k, v_ in conds.items():
        vs = v_ if isinstance(v_, list) else [v_]
        res[k] = all(positive_sum(sp.simplify(e), pos) for e in vs)
    print("  D8: T3's S4/S7 rows with b_I = (b_+ + p)/2, p in (1/2 + beta, min(3/2, q - 1)), alpha >= 4 free, each a "
          "positive sum on the whole box: %s" % res, flush=True)
    return all(res.values())


# --------------------------------------------------------------------------------------------------------------- D9
def d9(control=False):
    from gdext5 import radial_box0, TT, RR, mu
    tau, rh, alpha = sp.symbols("tau rho alpha", real=True)
    vf = sp.Function("v")
    ph = (1/RR)**alpha*vf(TT/RR)
    ex = radial_box0(ph, mu/RR**2).subs({TT: tau/rh, RR: 1/rh})
    nexp = (1 + alpha) if control else (2 + alpha)
    ex = (ex/rh**nexp).doit()
    V0, V1, V2 = sp.symbols("v v' v''")
    ex = ex.subs(sp.Derivative(vf(tau), (tau, 2)), V2).subs(sp.Derivative(vf(tau), tau), V1).subs(vf(tau), V0)
    ex = sp.expand(sp.powsimp(sp.expand_power_base(sp.expand(ex), force=True), force=True))
    lim = sp.simplify(sp.limit(ex, rh, 0))
    c2 = sp.simplify(sp.expand(lim).coeff(V2))
    ok = sp.simplify(c2 - (1 - tau**2)) == 0 and not c2.has(alpha)
    print("  D9%s: rho^-(%s) Box_0(rho^alpha v(tau)) at rho = 0 = %s; v'' coefficient 1 - tau^2 independent of alpha: %s"
          % (" control (normalisation rho^(-1-alpha))" if control else "", nexp, lim, ok), flush=True)
    return ok


# -------------------------------------------------------------------------------------------------------------- D10
def d10(control=False):
    import gdext5
    old = gdext5.e3
    c_val = 1 if control else sp.Rational(3, 2)
    a_, lam = gdext5.a_, gdext5.lam
    p0 = 1/(2 - gdext5.TT + gdext5.RR)
    pI = (2 - gdext5.TT + gdext5.RR)/gdext5.RR
    rho = 1/gdext5.RR
    phi = rho**c_val*p0**a_*pI**lam
    ex = gdext5.to_rho(gdext5.rI*rho**-sp.Rational(7, 2)*gdext5.radial_box0(phi, gdext5.mu/gdext5.RR**2)
                       / (p0**a_*pI**lam))
    ex = sp.simplify(sp.powsimp(sp.expand_power_base(ex, force=True), force=True))
    lim = sp.simplify(sp.limit(ex, gdext5.rI, 0))
    ok_rad = sp.simplify(lim + 2*lam*(a_ - lam)) == 0
    # the full 1-form operator at the sample, the same mutation
    G = gdext5.KS(1/gdext5.R**2)
    A, L_ = sp.Rational(1, 3), sp.Rational(1, 5)
    t, R, XS, rI, r0 = gdext5.t, gdext5.R, gdext5.XS, gdext5.rI, gdext5.r0
    rhoC = 1/R
    p0C = 1/(2 - t + R)
    pIC = (2 - t + R)/R
    phiC = rhoC**c_val*p0C**A*pIC**L_
    om = [sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5), sp.Rational(4, 5)]
    ok_full = True
    lims = []
    for nu in (0,):
        Z = [0]*gdext5.N
        Z[nu] = phiC
        H = G.hodge(Z)
        e_ = H[nu]*pIC*rhoC**-sp.Rational(7, 2)/(p0C**A*pIC**L_)
        sub = {XS[i]: om[i]/(r0*rI) for i in range(4)}
        sub[gdext5.RS] = 1/(r0*rI)
        sub[t] = 2 - 1/r0 + 1/(r0*rI)
        e_ = sp.simplify(sp.powsimp(sp.expand_power_base(e_.subs(sub), force=True), force=True))
        lm = sp.limit(e_, rI, 0)
        lims.append(lm)
        ok_full &= sp.simplify(lm + 2*L_*(A - L_)) == 0
    del old
    print("  D10%s: radial limit %s (= -2 lam (a - lam): %s); full 1-form Box, dt component at (a, lam) = (1/3, 1/5): "
          "limit %s (= -2 lam (a - lam): %s)" % (" control (conjugation by rho)" if control else "", lim, ok_rad,
                                                  lims, ok_full), flush=True)
    return ok_rad and ok_full


# -------------------------------------------------------------------------------------------------------------- D11
def d11(control=False):
    rr, tt = sp.symbols('r t', positive=True)
    rows = []
    ok = True
    for (a, b, beta) in [(Fr(37, 10), Fr(5, 2), Fr(1, 20)), (Fr(33, 10), Fr(3), Fr(1, 4)), (Fr(4), Fr(4), Fr(1, 2))]:
        A, B, BE = [sp.Rational(x.numerator, x.denominator) for x in (a, b, beta)]
        if control:
            A = BE + 3
        Fhat = sp.integrate(rr**(-A)*(rr/tt)**B, (tt, 4*rr, sp.oo))                 # the pointwise bound of G4 (b)
        I_ = sp.integrate(rr**(2*BE)*Fhat**2*rr**3, (rr, 1, sp.oo))                # in rho^beta L^2(dx), computed
        conv = I_.is_finite
        pred = A > BE + 3
        rows.append((str(A), str(BE), conv, pred))
        ok &= conv == pred and (conv if not control else True)
    if control:
        print("  D11 control (a = beta + 3): (a, beta, integral finite) = %s" % [(x[0], x[1], x[2]) for x in rows],
              flush=True)
        return all(x[2] for x in rows)
    print("  D11: G4 (b) with the integral computed: (a, beta, finite, a > beta + 3) = %s" % rows, flush=True)
    return ok


# -------------------------------------------------------------------------------------------------------------- D12
def d12(control=False):
    gams = [Fr(1, 50), Fr(1, 10), Fr(1, 5), Fr(1, 3)]
    es = [Fr(0), Fr(1, 4), Fr(1, 2)]
    gain = 0 if control else 1
    rows_ok = True
    nonempty = 0
    cnt = 0
    for gam, e in itertools.product(gams, es):
        dsh = (1 - e)*gam
        for k in range(1, 6):
            beta = dsh*Fr(k, 6)
            q_F = Fr(3, 2) + 2*gam + gain                # F_Y's I_0-order (least), the factor |x|^-1 of c_Ups
            a0 = q_F - Fr(7, 2)                          # conjugated: rho_I rho^(-7/2), the solution two less
            lsharp = Fr(3, 2) + dsh                      # E^Ups G sees no radiation slot (S1): I+-order lam_# + 1
            fI = (lsharp + 1) - Fr(5, 2)                 # conjugated I+-weight of the source: delta_# > 0
            hi = min(a0, Fr(0), fI)
            lo = beta - 1
            pmax = Fr(3, 2) + hi                         # the least upper bound of p = 3/2 + a_I
            good = lo < hi and pmax > Fr(1, 2) + beta
            nonempty += good
            rows_ok &= good
            cnt += 1
    if control:
        print("  D12 control (no factor |x|^-1): the interval (beta - 1, min(a_0, 0, f_I)) is non-empty at %d of %d "
              "samples" % (nonempty, cnt), flush=True)
        return nonempty > 0
    print("  D12: with f_I computed (delta_# > 0, not binding) the interval is non-empty and p_max = 3/2 + min(a_0, 0) "
          "> 1/2 + beta at %d of %d samples" % (nonempty, cnt), flush=True)
    return rows_ok


# -------------------------------------------------------------------------------------------------------------- D13
def d13(control=False):
    n = 3 if control else 4
    T, R, mu = sp.symbols('t_* r mu', positive=True)
    rI, rp, lam, m = sp.symbols('rho_I rho_p lambda m', positive=True)
    u = sp.Function('u')

    def box0(ph):
        """scalar operator of the Kerr-Schild metric eta + mu r^(2-n) (dt - dr)^2 in (t_*, r), t = t_* + r"""
        V = mu*R**(2 - n)
        gtt, gtr, grr = -1 - V, -V, 1 - V
        Dt = lambda e: sp.diff(e, T)
        Dr = lambda e: sp.diff(e, R) - sp.diff(e, T)
        pt_, pr_ = Dt(ph), Dr(ph)
        return -(Dt(R**(n - 1)*(gtt*pt_ + gtr*pr_)) + Dr(R**(n - 1)*(gtr*pt_ + grr*pr_)))/R**(n - 1)
    # III.I (3.1): rho_+ = (t_* + 1)^-1, rho_I = (t_* + 1)/r
    mono = (T + 1)**(-m)*((T + 1)/R)**lam                    # rho_+^m rho_I^lam
    ex = box0(mono)/mono
    ex = ex.subs({T: 1/rp - 1, R: 1/(rp*rI)})
    ex = sp.simplify(sp.expand(ex/(rI*rp**2)))
    lead = sp.simplify(sp.limit(ex, rI, 0))
    want = (m - lam)*(lam - sp.Rational(n - 1, 2))          # (X_+ - X_I)(X_I - (n-1)/2) on rho_+^m rho_I^lam
    ok_lead = sp.simplify(lead - want) == 0
    rest = sp.simplify((ex - lead)/rI)
    ok_rest = sp.limit(rest, rI, 0).is_finite                # smooth coefficients: the remainder gains rho_I
    roots = sp.solve(sp.Eq(lead.subs(m, lam + 1), 0), lam)
    # the coupling of Box (degrees -3 and -4, gdext5 E1): r^-3 d and r^-4 relative to rho_I rho_+^2
    c3 = sp.simplify(((T + 1)*R**-3/(rI*rp**2)).subs({T: 1/rp - 1, R: 1/(rp*rI)}))   # d_t* in rho_+ V_b
    c4 = sp.simplify((R**-4/(rI*rp**2)).subs({R: 1/(rp*rI)}))
    gain = [sp.Poly(c3, rI).degree() if c3.is_polynomial(rI) else None,
            sp.Poly(c4, rI).degree() if c4.is_polynomial(rI) else None]
    # Proposition 3.1's indicial factor: L_0 (rho_I^z w(rho_+)) = rho_I^z (z - 3/2)(X_+ - z) w
    z = sp.Symbol('z')
    w = sp.Function('w')
    Xp = lambda e: rp*sp.diff(e, rp)
    XI = lambda e: rI*sp.diff(e, rI)
    tgt = rI**z*w(rp)
    L0 = Xp(XI(tgt) - sp.Rational(n - 1, 2)*tgt) - XI(XI(tgt) - sp.Rational(n - 1, 2)*tgt)
    fac = sp.simplify(L0/rI**z - (z - sp.Rational(n - 1, 2))*(Xp(w(rp)) - z*w(rp)))
    ok = ok_lead and ok_rest and fac == 0 and sp.Rational(3, 2) in roots and gain == [3, 2]
    if control:
        print("  D13 control (n = 3): leading part %s, indicial roots %s; the root 3/2 present: %s"
              % (sp.factor(lead), roots, sp.Rational(3, 2) in roots), flush=True)
        return sp.Rational(3, 2) in roots
    print("  D13: rho_I^-1 rho_+^-2 Box_0 on rho_+^m rho_I^lam -> %s = (X_+ - X_I)(X_I - 3/2): %s; the rest gains rho_I "
          "(smooth): %s; I+ roots (with m = lam + 1) %s; the coupling r^-3 (rho_+ X), r^-4 relative to rho_I rho_+^2: "
          "rho_I-degrees %s; L_0(rho_I^z w) = rho_I^z (z - 3/2)(X_+ - z) w: %s"
          % (sp.factor(lead), ok_lead, ok_rest, roots, gain, fac == 0), flush=True)
    return ok


CHECKS = [("D1", d1), ("D2", d2), ("D3", d3), ("D4", d4), ("D5", d5), ("D6", d6), ("D7", d7), ("D8", d8),
          ("D9", d9), ("D10", d10), ("D11", d11), ("D12", d12), ("D13", d13)]


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
