#!/usr/bin/env python3
"""axis5.py -- CERTIFY-10L5-RESULT.md round 4 (task 1): the axis charts.  Near each axis the class is four-
dimensional axisymmetric Einstein-scalar; its double-null frame is regular there; the curvature-level pairs close
their angular terms with the axisymmetric measure, the axis contributing no boundary term; the axis's 1/s terms are
tamed by Hardy inequalities with explicit constants; and the frame quantities of the record's solution are bounded up
to the axis, where Theorem 7.L's grow like the inverse distance.  Labels: deduced (exact, sympy) for X1-X3 and X6's
counterexample; deduced with a computed check for X4; computed (floating point, on the record's run) for X5.

The chart at x = +1 (the phi2-circle degenerates there; reduce on phi1 alone).  g5 = g4 + e^{2A} dphi1^2 with
g4 = h + e^{2B} dphi2^2 (reduce5.py's A, B, h).  In dimension four the Einstein frame is ghat = e^A g4, and
    Ric(ghat) - (3/2) dA dA = Ric5|_4 + (1/2) e^{-2A} Ric5_11 g4,     Box_ghat A = -e^{-3A} Ric5_11,
so the vacuum class is four-dimensional Einstein-scalar ([Wu26] (1.4), Phi = sqrt(3/2) A) with the Killing field
d_phi2, hypersurface orthogonal (twist free) and with the reflection phi2 -> -phi2.  In [Wu26]'s form (1.1),
    ghat = -2 Omh^2 (du dv + dv du) + gh (dx - b du)^2 + Y^2 dphi2^2,
    Omh^2 = e^{A + 2W},  gh = e^A Gx,  Y = e^{A/2 + B},  b = (1 - x^2) s.
The chart at x = -1 is the same with (A, phi1) and (B, phi2) exchanged.

  X1 (exact) the reduction identities above, for the general warped metric (h general (2+1), A, B free), and the chart
     is regular at x = 1 in the record's variables: e^A -> R e^P, so Omh^2 -> R e^{P + 2W} > 0 (where the three-
     dimensional Einstein frame of reduce5.py R4 has Omt^2 ~ (1 - x^2) -> 0); and with s the proper distance to the
     axis along x, Y/s -> e^{P + 2Q} = e^{(1 - x) n} -> 1 (elementary flatness, exact in the record's variables).
     Control: with P + 2Q -> c != 0 at x = 1 (a conical defect) the limit is e^c, not 1.
  X2 (exact) the twist-free double-null structure of the general ghat: with e4 = Omh^-1 d_v, e3 = Omh^-1 (d_u + b d_x),
     e1 = gh^-1/2 d_x, e2 = Y^-1 d_phi, the Ricci coefficients of [Wu26] (2.1) have chi_12 = chib_12 = eta_2 = etab_2
     = zeta_2 = 0 and
        chi_11 = e4 log sqrt(gh), chi_22 = e4 log Y, chib_11 = Omh^-1 ((d_u + b d_x) log sqrt(gh) + b_x),
        chib_22 = e3 log Y, omega = -(1/2) e4 log Omh, omegab = -(1/2) e3 log Omh,
        zeta = -(1/4) Omh^-2 sqrt(gh) b_v, eta = zeta + e1 log Omh, etab = -zeta + e1 log Omh,
     every Christoffel symbol with an odd number of phi indices vanishes (so sigma = 0 and every curvature component
     odd under phi -> -phi vanishes: the reduced curvature is (alpha_11, beta_1, rho, betab_1, alphab_11, K)).  The
     section S_{u,v} has metric gh dx^2 + Y^2 dphi^2 and Gauss curvature K = -Y^-1 e1 e1 Y.
  X3 (exact) the measure: with dmu = Y sqrt(gh) dx,  d_v log(Y sqrt(gh)) = Omh tr chi  and
     d_u (Y sqrt(gh)) + d_x (b Y sqrt(gh)) = Omh tr chib Y sqrt(gh)  (div e4 and div e3 on S);  and for any functions
     K, beta (a scalar and the e1-component of a one-form), the pair operators div and grad are adjoint:
        K div(Omh beta) + Omh beta e1 K = (Y sqrt(gh))^-1 d_x (Y Omh K beta),
     an exact x-derivative for the measure dmu, whose boundary value at the axis, Y Omh K beta, vanishes where Y does
     (K, beta bounded).  So the Bianchi pairs (beta, K) and (K, betab) of [Wu26] (2.13)-(2.14) have energy identities
     on S including the axis, with no boundary term there.  Control: with the three-dimensional measure sqrt(gh) dx
     (no Y) the sum is not an exact derivative: the remainder is (e1 log Y) Omh K beta, the axis's 1/s term.
  X4 (deduced, with a computed check) the Hardy inequalities that recover angular derivatives from the axis.  On
     [0, S] with Y = s y(s), 0 < y_min <= y <= y_max and |s y'/y| <= q, for g in L^2(Y ds):
       (H1) eta := Y^-1 int_0^s Y g (the solution of div eta = g regular at the axis) has
            ||(e1 log Y) eta|| <= C1 ||g||,  C1 = (1 + q) (y_max/y_min)^(3/2);
       (H2) chih := Y^-2 int_0^s Y^2 g (the solution of (e1 + 2 e1 log Y) chih = g, Codazzi's operator) has
            ||(e1 log Y) chih|| <= C2 ||g||,  C2 = (1 + q) (y_max/y_min)^(5/2)/2,
     both in L^2(Y ds) (proof: |e1 log Y| <= (1 + q)/s, and the weighted Hardy inequality int_0^inf s^-r G^2 ds <=
     (2/(r - 1))^2 int_0^inf s^(2 - r) G'^2 ds for r = 3 and 5).  [Round 5, the verifier of round 4, m10: the same
     proof gives the sharper C1 = (1 + q) (y_max/y_min)^(1/2) and C2 = (1 + q) (y_max/y_min)^(3/2)/2; both are
     checked.]  Checked on test functions; control: the solution integrated from s = S instead of the axis (not
     regular there) makes the ratio grow without bound as the grid is refined.
  X5 (computed) on the record's solution (D432's run, rcert5's box): in the chart at x = +1 the frame quantities
     (Omh times tr chi, chih, tr chib, chibh, omega, omegab, eta, etab, zeta, and the scalar's e4, e3, e1 derivatives;
     the hierarchy's coefficients are polynomials in these) are bounded on 0 <= x < 1 up to the outermost node, and
     chih, eta, zeta, e1 Phi vanish toward the axis at the rates regularity requires (chih/(1 - x), eta/sqrt(1 - x)
     bounded); the same at x = -1 in the other chart.  Against them: Theorem 7.L's three-dimensional coefficient sums,
     which grow from 122 (|x| <= 1/2) to 1.8e5 at the outermost node (linest5.out E4).
  X6 (deduced; exact counterexample) why the axis needs the curvature level.  In the axis chart the section has the
     connection k = e1 log Y ~ 1/s.  A level-0 frame-difference estimate (7.L's unknowns) would carry dk; but for the
     regular perturbation gh -> (1 + eps) gh, Y -> (1 + eps)^(1/2) Y (elementary flatness kept), dk = -(eps/2) k exactly,
     and int_0^S (dk)^2 Y ds diverges logarithmically.  So no estimate whose unknowns include dk in L^2(dmu) exists, and
     the angular derivatives of the metric differences must be carried as tensors (Codazzi, H2), i.e. at the curvature
     level: nothing weaker than [Wu26]'s level suffices at the axis.

  X7 (exact; computed constant) the glue.  For a cut-off psi(x) (psi = 1 near the axis, 0 away from it):
        psi [K div(Omh beta) + Omh beta e1 K] = (Y sqrt gh)^-1 d_x(psi Y Omh K beta) - (e1 psi) Omh K beta,
        d_u(psi f Y sqrt gh) + d_x(b psi f Y sqrt gh)
            = psi [d_u(f Y sqrt gh) + d_x(b f Y sqrt gh)] + b (d_x psi) f Y sqrt gh,
     so the cut-off energy obeys the axis chart's identity with two added bulk terms, (e1 psi) Omh K beta and
     b (d_x psi) f, supported where psi is not constant: Gronwall coefficients a_glue = sup Omh |e1 psi| (the angular
     term, split as |K beta| <= (K^2 + beta^2)/2, so 1/2 to each) and sup |b d_x psi| (the shift).  Computed on the
     record's solution for psi linear in x from 0 at x = 1/4 to 1 at x = 3/4 (chart +), and the mirror (chart -).
     The bulk terms are curvature-level (K, beta): an energy that does not control them on the strip (Theorem 7.L,
     level 0) cannot absorb them, which is why the glue to the interior needs the interior at level 1 (lev1_5.py).
     Control: the identity without the (e1 psi) term fails.

  python3 checks/axis5.py RUN.npz        (RUN: the record's l1_rc0.9_M32.npz; without it X5 is skipped)
"""
import os, sys, time, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('linest5', os.path.join(HERE, 'linest5.py'))
L5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L5)
print = L5.print
_s = importlib.util.spec_from_file_location('dnull5', os.path.join(os.path.dirname(HERE), 'dnull5.py'))
dn = importlib.util.module_from_spec(_s); _s.loader.exec_module(dn)

u, v, x, ph = sp.symbols('u v x phi', real=True)
C4 = [u, v, x, ph]


def zero(e, trials=3, digits=60):
    """the identity holds for every smooth choice of the functions: every function and every derivative of it is
    replaced by an independent random rational (the expression is a rational-exponential function of these jets), and
    the value is computed to 60 digits; three independent trials must each vanish below 1e-45 (an identity holds at
    every jet; a false one fails at random jets with probability one)"""
    from sympy.core.function import AppliedUndef
    import random
    e = sp.sympify(e)
    if e == 0:
        return True
    rnd = random.Random(20261106)
    for _ in range(trials):
        sub = {}
        for d in e.atoms(sp.Derivative):
            sub[d] = sp.Rational(rnd.randint(-900, 900), rnd.randint(101, 997))
        for f in e.atoms(AppliedUndef):
            sub[f] = sp.Rational(rnd.randint(150, 900), rnd.randint(101, 997))      # positive (logs, roots)
        e2 = e.xreplace(sub)
        e2 = e2.xreplace({q: sp.Rational(rnd.randint(150, 900), rnd.randint(1001, 1997)) for q in e2.free_symbols})
        val = sp.N(e2, digits)
        if not val.is_number or abs(complex(val)) > 1e-45:
            return False
    return True


def x1():
    """the reduction identities on a general warped metric; regularity of the chart in the record's variables"""
    w, k, b, A, B = [sp.Function(n)(u, v, x) for n in ('w', 'k', 'b', 'A', 'B')]
    p1 = sp.Symbol('phi1', real=True)
    C5 = [u, v, x, ph, p1]
    h = sp.zeros(3)
    h[0, 1] = h[1, 0] = -2 * sp.exp(2 * w)
    h[2, 2] = sp.exp(2 * k); h[0, 2] = h[2, 0] = -sp.exp(2 * k) * b; h[0, 0] = sp.exp(2 * k) * b ** 2
    g4 = sp.zeros(4); g4[:3, :3] = h; g4[3, 3] = sp.exp(2 * B)
    g5 = sp.zeros(5); g5[:4, :4] = g4; g5[4, 4] = sp.exp(2 * A)
    Ric5 = dn.ricci(g5, C5)
    gh = sp.exp(A) * g4
    Rich = dn.ricci(gh, C4)
    ok = True
    res = []
    for i in range(4):
        for j in range(i, 4):
            if (i == 3) != (j == 3):
                continue
            lhs = Rich[i, j] - sp.Rational(3, 2) * sp.diff(A, C4[i]) * sp.diff(A, C4[j])
            rhs = Ric5[i, j] + sp.Rational(1, 2) * sp.exp(-2 * A) * Ric5[4, 4] * g4[i, j]
            z = zero(lhs - rhs)
            res.append(z); ok &= z
    gi = gh.inv(); sq = sp.sqrt(-gh.det())
    sq = sp.exp(2 * A) * 2 * sp.exp(2 * w) * sp.exp(k) * sp.exp(B)           # sqrt|det ghat|, exact for this form
    zsq = zero(sq ** 2 + gh.det())
    boxA = sum(sp.diff(sq * gi[a, c] * sp.diff(A, C4[c]), C4[a]) for a in range(3) for c in range(3)) / sq
    zbox = zero(boxA + sp.exp(-3 * A) * Ric5[4, 4])
    # control: the conformal weight e^{2A} (the five-dimensional one) in place of e^A
    gw = sp.exp(2 * A) * g4
    Ricw = dn.ricci(gw, C4)
    ctl = zero(Ricw[0, 1] - sp.Rational(3, 2) * sp.diff(A, u) * sp.diff(A, v) - Ric5[0, 1]
               - sp.Rational(1, 2) * sp.exp(-2 * A) * Ric5[4, 4] * g4[0, 1])
    # regularity in the record's variables
    R, P, Q, W, s_ = sp.symbols('R P Q W s', positive=True)
    xx = sp.Symbol('x')
    eA = R * sp.exp(P) * sp.sqrt((1 + xx) / 2)
    Om2 = eA * sp.exp(2 * W)
    lim_om = sp.simplify(Om2.subs(xx, 1))
    # Y/s at the axis: Gx ~ R^2 e^{-2(P+Q)}/(8(1 - x)), s = int_x^1 sqrt(e^A Gx) dx' ~ 2 sqrt(C (1 - x))
    e = sp.Symbol('e', positive=True)                   # e = 1 - x
    ghat = (eA * R ** 2 * sp.exp(-2 * (P + Q)) / (4 * (1 - xx ** 2))).subs(xx, 1 - e)
    lead = sp.limit(ghat * e, e, 0)                     # gh ~ lead/e
    s_lead = 2 * sp.sqrt(lead * e)                      # s = int_0^e sqrt(lead/e') de'
    Y = sp.sqrt((eA * R ** 2 * (1 - xx) / 2 * sp.exp(2 * Q)).subs(xx, 1 - e))
    ratio = sp.simplify(sp.limit(Y / s_lead, e, 0))
    want = sp.exp(P + 2 * Q)
    zr = zero(ratio - want)
    cdef = sp.Symbol('c')
    ratio_c = sp.simplify(ratio.subs(Q, (cdef - P) / 2))
    ctl2 = zero(ratio_c - 1)
    m_, n_ = sp.symbols('m n')
    Pr = (2 * (1 + xx) * m_ - (1 - xx) * n_) / 3; Qr = (2 * (1 - xx) * n_ - (1 + xx) * m_) / 3
    flat = sp.simplify((Pr + 2 * Qr).subs(xx, 1))
    return res, zsq, zbox, ctl, lim_om, ratio, zr, ctl2, flat


def x2():
    Om, gg, b, Y = [sp.Function(n)(u, v, x) for n in ('Om', 'gg', 'b', 'Y')]
    g = sp.zeros(4)
    g[0, 1] = g[1, 0] = -2 * Om ** 2
    g[2, 2] = gg; g[0, 2] = g[2, 0] = -gg * b; g[0, 0] = gg * b ** 2; g[3, 3] = Y ** 2
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, bb], C4[c]) + sp.diff(g[d, c], C4[bb]) - sp.diff(g[bb, c], C4[d]))
                 for d in range(4)) / 2 for c in range(4)] for bb in range(4)] for a in range(4)]
    odd = all(sp.expand(Gam[a][bb][c]) == 0 for a in range(4) for bb in range(4) for c in range(4)
              if ([a, bb, c].count(3)) % 2 == 1)
    E = {'3': [1 / Om, 0, b / Om, 0], '4': [0, 1 / Om, 0, 0], '1': [0, 0, 1 / sp.sqrt(gg), 0], '2': [0, 0, 0, 1 / Y]}

    def D(X, Yv):
        """covariant derivative D_X Y of frame vectors (components)"""
        return [sum(X[c] * sp.diff(Yv[a], C4[c]) for c in range(4)) +
                sum(Gam[a][c][d] * X[c] * Yv[d] for c in range(4) for d in range(4)) for a in range(4)]
    gp = lambda X, Yv: sum(g[a, c] * X[a] * Yv[c] for a in range(4) for c in range(4))
    chi = {(A_, B_): gp(D(E[A_], E['4']), E[B_]) for A_ in '12' for B_ in '12'}
    chib = {(A_, B_): gp(D(E[A_], E['3']), E[B_]) for A_ in '12' for B_ in '12'}
    eta = {A_: -gp(D(E['3'], E[A_]), E['4']) / 2 for A_ in '12'}
    etab = {A_: -gp(D(E['4'], E[A_]), E['3']) / 2 for A_ in '12'}
    om = -gp(D(E['4'], E['3']), E['4']) / 4
    omb = -gp(D(E['3'], E['4']), E['3']) / 4
    zet = {A_: gp(D(E[A_], E['4']), E['3']) / 2 for A_ in '12'}
    e4 = lambda f: sp.diff(f, v) / Om
    e3 = lambda f: (sp.diff(f, u) + b * sp.diff(f, x)) / Om
    e1 = lambda f: sp.diff(f, x) / sp.sqrt(gg)
    claims = {
        'chi_12 = chib_12 = eta_2 = etab_2 = zeta_2 = 0': [chi[('1', '2')], chi[('2', '1')], chib[('1', '2')],
                                                         eta['2'], etab['2'], zet['2']],
        'chi_11 = e4 log sqrt(gh)': [chi[('1', '1')] - e4(sp.log(gg) / 2)],
        'chi_22 = e4 log Y': [chi[('2', '2')] - e4(sp.log(Y))],
        'chib_11 = Omh^-1 ((d_u + b d_x) log sqrt(gh) + b_x)': [chib[('1', '1')] - (e3(sp.log(gg) / 2)
                                                                                + sp.diff(b, x) / Om)],
        'chib_22 = e3 log Y': [chib[('2', '2')] - e3(sp.log(Y))],
        'omega = -(1/2) e4 log Omh': [om + e4(sp.log(Om)) / 2],
        'omegab = -(1/2) e3 log Omh': [omb + e3(sp.log(Om)) / 2],
        'zeta = -(1/4) Omh^-2 sqrt(gh) b_v': [zet['1'] + sp.sqrt(gg) * sp.diff(b, v) / (4 * Om ** 2)],
        'eta = zeta + e1 log Omh': [eta['1'] - zet['1'] - e1(sp.log(Om))],
        'etab = -zeta + e1 log Omh': [etab['1'] + zet['1'] - e1(sp.log(Om))],
    }
    out = {k_: all(zero(e) for e in es) for k_, es in claims.items()}
    # control: chi_22 claimed as e4 log sqrt(gh) (the wrong circle)
    ctl = zero(chi[('2', '2')] - e4(sp.log(gg) / 2))
    # Gauss curvature of the section metric gg dx^2 + Y^2 dphi^2
    gs = sp.Matrix([[gg, 0], [0, Y ** 2]]); X2c = [x, ph]; gsi = gs.inv()
    G2 = [[[sum(gsi[a, d] * (sp.diff(gs[d, bb], X2c[c]) + sp.diff(gs[d, c], X2c[bb]) - sp.diff(gs[bb, c], X2c[d]))
                for d in range(2)) / 2 for c in range(2)] for bb in range(2)] for a in range(2)]
    # R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce} G^e_{db} - G^a_{de} G^e_{cb};  K = R_{x phi x phi}/det
    Rud = lambda a, bb, c, d: (sp.diff(G2[a][d][bb], X2c[c]) - sp.diff(G2[a][c][bb], X2c[d])
                               + sum(G2[a][c][e_] * G2[e_][d][bb] - G2[a][d][e_] * G2[e_][c][bb] for e_ in range(2)))
    Rdown = sum(gs[0, a] * Rud(a, 1, 0, 1) for a in range(2))
    Kc = Rdown / gs.det()
    zK = zero(Kc + e1(e1(Y)) / Y)
    return odd, out, ctl, zK


def x3():
    Om, gg, b, Y, K, be = [sp.Function(n)(u, v, x) for n in ('Om', 'gg', 'b', 'Y', 'K', 'be')]
    sq = Y * sp.sqrt(gg)
    trchi = (sp.diff(sp.log(gg) / 2, v) + sp.diff(sp.log(Y), v)) / Om
    trchib = ((sp.diff(sp.log(gg) / 2, u) + b * sp.diff(sp.log(gg) / 2, x) + sp.diff(b, x))
              + (sp.diff(sp.log(Y), u) + b * sp.diff(sp.log(Y), x))) / Om
    m1 = zero(sp.diff(sp.log(sq), v) - Om * trchi)
    m2 = zero(sp.diff(sq, u) + sp.diff(b * sq, x) - Om * trchib * sq)
    e1 = lambda f: sp.diff(f, x) / sp.sqrt(gg)
    div = lambda f: sp.diff(Y * f, x) / sq            # div of the one-form with e1-component f
    pair = K * div(Om * be) + Om * be * e1(K) - sp.diff(Y * Om * K * be, x) / sq
    p_ok = zero(pair)
    div3 = lambda f: sp.diff(f, x) / sp.sqrt(gg)        # the 1D section's divergence (no Y)
    rem = K * div(Om * be) + Om * be * e1(K) - sp.diff(Om * K * be, x) / sp.sqrt(gg)
    rem_is = zero(rem - e1(sp.log(Y)) * Om * K * be)
    return m1, m2, p_ok, rem_is


def x7():
    Om, gg, b, Y, K, be, f, psi = [sp.Function(n)(u, v, x) for n in ('Om', 'gg', 'b', 'Y', 'K', 'be', 'f', 'psi')]
    psi = sp.Function('psi')(x)
    sq = Y * sp.sqrt(gg)
    e1 = lambda F_: sp.diff(F_, x) / sp.sqrt(gg)
    div = lambda F_: sp.diff(Y * F_, x) / sq
    i1 = zero(psi * (K * div(Om * be) + Om * be * e1(K)) - (sp.diff(psi * Y * Om * K * be, x) / sq
                                                           - e1(psi) * Om * K * be))
    i2 = zero(sp.diff(psi * f * sq, u) + sp.diff(b * psi * f * sq, x)
              - (psi * (sp.diff(f * sq, u) + sp.diff(b * f * sq, x)) + b * sp.diff(psi, x) * f * sq))
    ctl = zero(psi * (K * div(Om * be) + Om * be * e1(K)) - sp.diff(psi * Y * Om * K * be, x) / sq)
    return i1, i2, ctl


def x7_const(path):
    Z = np.load(path)
    uu, vv, xx, mask = Z['u'], Z['v'], Z['x'], Z['mask']
    box = (-4.0, -1.1, 0.55, 1.6)
    su = (uu >= box[0]) & (uu <= box[1]); sv = (vv >= box[2]) & (vv <= box[3])
    F = {k_: Z[k_][np.ix_(su, sv)] for k_ in ('R', 'm', 'n', 'W', 's')}
    keep = ~mask[np.ix_(su, sv)]
    X = xx[None, None, :]
    P = (2 * (1 + X) * F['m'] - (1 - X) * F['n']) / 3
    Q = (2 * (1 - X) * F['n'] - (1 + X) * F['m']) / 3
    lR = np.log(F['R'])
    lGx = 2 * lR - 2 * (P + Q) - np.log(4.0) - np.log(1 - X ** 2)
    b = (1 - X ** 2) * F['s']
    out = {}
    for chart, A_ in (('+', lR + P + 0.5 * np.log((1 + X) / 2)), ('-', lR + Q + 0.5 * np.log((1 - X) / 2))):
        lOm = 0.5 * A_ + F['W']; lgh = A_ + lGx
        dpsi = np.where((np.abs(X) >= 0.25) & (np.abs(X) <= 0.75) & ((X > 0) if chart == '+' else (X < 0)), 2.0, 0.0)
        ang = np.exp(lOm - 0.5 * lgh) * dpsi
        sh = np.abs(b) * dpsi
        sel = keep[:, :, None] & np.ones_like(X, bool)
        out[chart] = (float(np.max(np.where(sel, ang, 0))), float(np.max(np.where(sel, sh, 0))))
    return out


def x4():
    """Hardy checks on [0, 1] with Y = s y(s), y = 1 + s^2/2 (so y_min = 1, y_max = 1.5, q = s y'/y <= 2/3)"""
    out = []
    for n in (2000, 8000, 32000):
        s = (np.arange(n) + 0.5) / n; ds = 1.0 / n
        y = 1 + s ** 2 / 2; Y = s * y; yp = s
        kY = (y + s * yp) / (s * y)                     # e1 log Y with e1 = d_s
        q = np.max(np.abs(s * yp / y)); ymin, ymax = y.min(), y.max()
        C1 = (1 + q) * (ymax / ymin) ** 1.5; C2 = (1 + q) * (ymax / ymin) ** 2.5 / 2
        C1s = (1 + q) * (ymax / ymin) ** 0.5; C2s = (1 + q) * (ymax / ymin) ** 1.5 / 2      # round 5, m10
        nrm = lambda f: np.sqrt(np.sum(f ** 2 * Y) * ds)
        worst1 = worst2 = wbad = 0.0
        ws1 = ws2 = 0.0
        for g in (np.ones(n), np.cos(7 * s), s ** -0.4, np.sign(np.sin(30 * s)), np.exp(-50 * (s - 0.3) ** 2)):
            I1 = np.cumsum(Y * g) * ds - 0.5 * Y * g * ds; eta = I1 / Y
            I2 = np.cumsum(Y ** 2 * g) * ds - 0.5 * Y ** 2 * g * ds; chh = I2 / Y ** 2
            worst1 = max(worst1, nrm(kY * eta) / nrm(g) / C1)
            worst2 = max(worst2, nrm(kY * chh) / nrm(g) / C2)
            ws1 = max(ws1, nrm(kY * eta) / nrm(g) / C1s); ws2 = max(ws2, nrm(kY * chh) / nrm(g) / C2s)
            # control: integrated from s = 1 (not regular at the axis)
            Ib = -(np.cumsum((Y * g)[::-1])[::-1] * ds - 0.5 * Y * g * ds); etab = Ib / Y
            wbad = max(wbad, nrm(kY * etab) / nrm(g) / C1)
        out.append((n, C1, C2, worst1, worst2, wbad, C1s, C2s, ws1, ws2))
    return out


def x5(path):
    """frame quantities of the axis charts on the record's run over rcert5's box"""
    Z = np.load(path)
    uu, vv, xx, mask = Z['u'], Z['v'], Z['x'], Z['mask']
    box = (-4.0, -1.1, 0.55, 1.6)
    iu = np.where((uu >= box[0] - 0.05) & (uu <= box[1] + 0.05))[0]
    iv = np.where((vv >= box[2] - 0.05) & (vv <= box[3] + 0.05))[0]
    sl = (slice(iu[0], iu[-1] + 1), slice(iv[0], iv[-1] + 1))
    F = {k_: Z[k_][sl] for k_ in ('R', 'm', 'n', 'W', 's')}
    u_, v_ = uu[sl[0]], vv[sl[1]]
    M = len(xx)
    xg, D1, _ = L5.D5.cheb_gauss(M)
    X = xx[None, None, :]
    P = (2 * (1 + X) * F['m'] - (1 - X) * F['n']) / 3
    Q = (2 * (1 - X) * F['n'] - (1 + X) * F['m']) / 3
    lR = np.log(F['R'])
    du = lambda A_: np.gradient(A_, u_, axis=0)
    dv = lambda A_: np.gradient(A_, v_, axis=1)
    dx = lambda A_: np.einsum('ij,abj->abi', D1, A_)
    keep = (~mask[sl]) & ((u_ >= box[0]) & (u_ <= box[1]))[:, None] & ((v_ >= box[2]) & (v_ <= box[3]))[None, :]
    b = (1 - X ** 2) * F['s']
    lGx = 2 * lR - 2 * (P + Q) - np.log(4.0) - np.log(1 - X ** 2)
    res = {}
    for chart in ('+', '-'):
        if chart == '+':
            A_ = lR + P + 0.5 * np.log((1 + X) / 2)       # the regular circle at x = +1 (phi1)
            Bc = lR + Q + 0.5 * np.log((1 - X) / 2)       # the degenerating one (phi2)
        else:
            A_ = lR + Q + 0.5 * np.log((1 - X) / 2)
            Bc = lR + P + 0.5 * np.log((1 + X) / 2)
        lOm = 0.5 * A_ + F['W']                            # log Omh
        lgh = A_ + lGx                                      # log gh
        lY = 0.5 * A_ + Bc
        # regular combinations differentiated as such (the log(1 -+ x) parts are v- and u-independent)
        Om = np.exp(lOm); isg = np.exp(-0.5 * lgh)
        D3 = lambda f: du(f) + b * dx(f)
        q = {}
        q['tr chi'] = Om * (dv(0.5 * lgh) + dv(lY)) / Om        # Omh tr chi = d_v log(sqrt(gh) Y)
        q['chih'] = 0.5 * (dv(0.5 * lgh) - dv(lY))               # Omh chih
        q['tr chib'] = D3(0.5 * lgh) + dx(b) + D3(lY)
        q['chibh'] = 0.5 * (D3(0.5 * lgh) + dx(b) - D3(lY))
        q['omega'] = -0.5 * dv(lOm); q['omegab'] = -0.5 * D3(lOm)
        zeta = -0.25 * np.exp(-lOm) * np.exp(0.5 * lgh) * dv(b)
        q['zeta'] = Om * zeta
        q['eta'] = Om * (zeta + isg * dx(lOm)); q['etab'] = Om * (-zeta + isg * dx(lOm))
        Phi = np.sqrt(1.5) * A_
        q['e4 Phi'] = dv(Phi); q['e3 Phi'] = D3(Phi); q['e1 Phi'] = Om * isg * dx(Phi)
        side = (xx > 0) if chart == '+' else (xx < 0)
        dist = 1 - np.abs(xx)
        tab = {}
        for k_, A2 in q.items():
            vals = np.where(keep[:, :, None], np.abs(A2), np.nan)
            per_node = np.nanmax(vals, axis=(0, 1))
            tab[k_] = (float(np.nanmax(per_node[side])), per_node)
        # rates toward the axis: chih/(1 - |x|), eta, zeta, e1 Phi over sqrt(1 - |x|), at the four outermost nodes
        order = np.argsort(dist)
        outer = [j for j in order if side[j]][:4]
        rates = {k_: [float(tab[k_][1][j] / (dist[j] if k_ == 'chih' else np.sqrt(dist[j]))) for j in outer]
                 for k_ in ('chih', 'eta', 'zeta', 'e1 Phi')}
        res[chart] = (tab, rates, [float(xx[j]) for j in outer])
    return res


def main():
    t0 = time.time(); ok = True
    r = x1()
    res, zsq, zbox, ctl, lim_om, ratio, zr, ctl2, flat = r
    good = all(res) and zsq and zbox and not ctl and zr and not ctl2 and flat == 0
    print('X1 (exact) Ric(ghat) - (3/2) dA dA = Ric5|_4 + (1/2) e^{-2A} Ric5_11 g4 on the eight components %s; '
          'sqrt|det ghat| exact %s; Box_ghat A = -e^{-3A} Ric5_11 %s; control (weight e^{2A}) %s' % (
              'all hold' if all(res) else 'FAIL', zsq, zbox, 'fails (good)' if not ctl else 'holds (bad)'))
    print('   at x = 1 in the record\'s variables: Omh^2 -> %s; Y/s -> %s (= e^{P+2Q}: %s); P + 2Q at x = 1 with the '
          'record\'s P, Q of m, n: %s; control (P + 2Q -> c): Y/s -> e^c, = 1 only if c = 0: %s' % (
              lim_om, ratio, zr, flat, 'fails (good)' if not ctl2 else 'holds (bad)'))
    print('X1', 'PASS' if good else 'FAIL'); ok &= good
    print('   (%.0f s)' % (time.time() - t0), flush=True)
    odd, out, ctl, zK = x2()
    good = odd and all(out.values()) and not ctl and zK
    print('X2 (exact) every Christoffel symbol with an odd number of phi indices vanishes: %s' % odd)
    for k_, v_ in out.items():
        print('   %s: %s' % (k_, 'holds' if v_ else 'FAILS'))
    print('   K = -Y^-1 e1 e1 Y for the section metric: %s; control (chi_22 = e4 log sqrt(gh)): %s' % (
        zK, 'fails (good)' if not ctl else 'holds (bad)'))
    print('X2', 'PASS' if good else 'FAIL'); ok &= good
    print('   (%.0f s)' % (time.time() - t0), flush=True)
    m1, m2, p_ok, rem_is = x3()
    good = m1 and m2 and p_ok and rem_is
    print('X3 (exact) d_v log(Y sqrt(gh)) = Omh tr chi: %s; d_u(Y sqrt gh) + d_x(b Y sqrt gh) = Omh tr chib Y sqrt gh: '
          '%s; K div(Omh beta) + Omh beta e1 K = (Y sqrt gh)^-1 d_x(Y Omh K beta): %s; control (measure sqrt(gh) dx): '
          'the remainder is exactly (e1 log Y) Omh K beta, not zero: %s' % (m1, m2, p_ok, rem_is))
    print('X3', 'PASS' if good else 'FAIL'); ok &= good
    hx = x4()
    good = all(r_[3] <= 1 and r_[4] <= 1 and r_[8] <= 1 and r_[9] <= 1 for r_ in hx) and \
        hx[-1][5] > 1.5 * hx[0][5] and hx[-1][5] > 1
    print('X4 (deduced; computed check) Hardy at the axis, Y = s (1 + s^2/2) on [0, 1]:')
    for n, C1, C2, w1, w2, wb, C1s, C2s, s1, s2 in hx:
        print('   n = %6d: C1 = %.3f, C2 = %.3f; worst ||k eta||/(C1 ||g||) = %.3f, ||k chih||/(C2 ||g||) = %.3f (<= 1 '
              'required); control, integrated from s = 1: %.3f' % (n, C1, C2, w1, w2, wb))
        print('      the sharper constants (round 5, m10) C1 = %.3f, C2 = %.3f: ratios %.3f, %.3f (<= 1 required)' % (
            C1s, C2s, s1, s2))
    print('X4', 'PASS (the bounds hold; the control grows with the grid, unbounded)' if good else 'FAIL')
    ok &= good
    # X6 the counterexample: dk = -(eps/2) k exactly, and int k^2 Y ds diverges
    eps, s_, S = sp.symbols('epsilon s S', positive=True)
    gg = sp.Function('gg')(s_); Yf = sp.Function('Yf')(s_)
    k0 = sp.diff(Yf, s_) / Yf / sp.sqrt(gg)
    k1 = sp.diff(sp.sqrt(1 + eps) * Yf, s_) / (sp.sqrt(1 + eps) * Yf) / sp.sqrt((1 + eps) * gg)
    dk = sp.series(k1 - k0, eps, 0, 2).removeO()
    zk = zero(dk + eps / 2 * k0)
    a_ = sp.Symbol('a', positive=True)
    Ilog = sp.integrate((1 / s_) ** 2 * s_, (s_, a_, 1))
    div = sp.limit(Ilog, a_, 0)
    good = zk and div == sp.oo
    print('X6 (exact) under gh -> (1 + eps) gh, Y -> (1 + eps)^(1/2) Y: dk = -(eps/2) k to first order: %s; '
          'with k ~ 1/s, '
          'Y ~ s: int_a^1 k^2 Y ds = %s -> %s as a -> 0 ->' % (zk, Ilog, div), 'PASS' if good else 'FAIL')
    ok &= good
    i1, i2, ctl = x7()
    good = i1 and i2 and not ctl
    print('X7 (exact) the cut-off identities: angular %s, shift %s; control (without the (e1 psi) term): %s ->' % (
        i1, i2, 'fails (good)' if not ctl else 'holds (bad)'), 'PASS' if good else 'FAIL')
    ok &= good
    if len(sys.argv) > 1:
        gc = x7_const(sys.argv[1])
        print('X7 (computed) the glue\'s added coefficients for psi linear on 1/4 <= |x| <= 3/4: chart +: sup Omh |e1 '
              'psi| = %.3g, sup |b d_x psi| = %.3g; chart -: %.3g, %.3g' % (gc['+'][0], gc['+'][1], gc['-'][0],
                                                                            gc['-'][1]))
        res = x5(sys.argv[1])
        print('X5 (computed) the axis charts on the record\'s run (rcert5\'s box), frame quantities times Omh (as '
              'linest5.py E4 states them), sup over the chart\'s half 0 < +-x < 1 including the outermost node:')
        good = True
        for chart, (tab, rates, xo) in res.items():
            print('   chart %s1: ' % chart + ', '.join('%s %.3g' % (k_, v_[0]) for k_, v_ in tab.items()))
            print('      toward the axis (nodes x = %s): ' % ', '.join('%.4f' % z for z in xo) + '; '.join(
                '%s/%s %s' % (k_, '(1-|x|)' if k_ == 'chih' else 'sqrt(1-|x|)', ', '.join('%.3g' % z for z in vv_))
                for k_, vv_ in rates.items()))
            good &= all(np.isfinite(v_[0]) and v_[0] < 1e3 for v_ in tab.values())
            good &= all(max(vv_) < 50 * max(min(vv_), 1e-12) for vv_ in rates.values())
        print('   against Theorem 7.L\'s coefficient sums in the three-dimensional frame: 122 on |x| <= 1/2, 1.8e5 at '
              'the outermost node (linest5.out E4)')
        print('X5', 'PASS (bounded up to the axis; the regular rates hold)' if good else 'FAIL')
        ok &= good
    print('axis5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
