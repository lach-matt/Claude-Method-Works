#!/usr/bin/env python3
"""stage1rate5: Lemma 2.3's energy constant at gt = g0, written out and certified on Omega at P* (CONSTANTS5.md, Round
5, R5.5). Stage 1 (N1STAR-PROOF.md Lemma 5.3 (a)) is a wave equation for m_1 with the operator box~ = g0^{ab} d_a d_b
componentwise, so the estimate it needs is Lemma 2.3 at gt = g0 itself (eps1 = 0), not at a gt within 0.0307686 of g0
as round 4 said (R4.2); its lower-order coefficients are computed in bbar5.py (D569: Bbar = B0 from g0 alone, Cbar = C0
plus the W_TT^2 means). Labels: computed (exact, sympy), certified (flint arb interval arithmetic on a cover of
Omega), deduced (the energy argument, Lemma 2.3's proof at N1STAR-PROOF.md:222-233 with its constant made explicit).

  K1 (exact) at xhat = e1 (O(4) invariance), with m = mu/r^2 and k = mu'/r, Y = -g0^-1 dtau = (1 + m, -m xhat), its
     deformation tensor pi = L_Y g0 = (1/r) Pi(m, k): Pi_tautau = 2 m^2 - k, Pi_tau1 = 2 m + 2 m^2 - k, Pi_11 = 4 m + 2 m^2
     - k, Pi_angular = -2 m; Gamma^b = d_a g0^{ab} = (1/r) gamma(m, k); g0(Y, Y) = -1 - m.
  K2 (deduced; exact forms) with T_ab = d_a u d_b u - (1/2) g0_ab g0^-1(du, du), J^a = T^a_b Y^b, E(tau) = int T(Y, Y) dx
     (det g0 = -1, so d_a J^a is the divergence): d_a J^a = (1/2) T^{ab} pi_ab + (Y u)(box~ u + Gamma . du). As quadratic
     forms in p = du: T(Y, Y) = p^T Q p, Q = Y Y^T + (1/2)(1 + m) g0^-1; the bulk is p^T M p, M = (1/2)(g0^-1 pi g0^-1 -
     (1/2) tr(g0^-1 pi) g0^-1) + sym(Y Gamma^T). The lateral fluxes have the sign Lemma 2.3 drops. So dE/dtau <= kappa E
     + c_Y E^(1/2) ||box~ u||, kappa = sup |lambda(M, Q)| (generalized eigenvalues), c_Y^2 = sup Y^T Q^-1 Y, and with
     -(1/2) box~ u = f: ||du(tau)|| <= q^(1/2) e^(kappa Dtau/2) ||du(tau0)|| + 2 c_Y q_lo^(-1/2) e^(kappa Dtau/2) int ||f||,
     q = sup q_hi/inf q_lo, q_lo, q_hi the Euclidean eigenvalues of Q.
  K3 (certified) on Omega at P*: r in [a, b(tau0)], m in [mu0/r^2, mu_end/r^2], k in [0, (2/9) c^2/r] (A = 1, env <=
     c <= 1.3241035, envelope5.out E1, READ), kappa <= sup over r-cells of (1/r_i) sup |K(m, k)|, K the generalized
     eigenvalues of (r M, Q) in closed form (2 x 2 block (tau, x1) and the angular ratios), on a cover of 400 r-cells x 8
     m-cells x 4 k-cells in arb. Printed: kappa, the Gronwall factor e^(kappa Dtau/2), q, c_Y.
  Controls (mutating the computed path; each must fail): C1 K2's bulk without the Gamma term (box~ read as the covariant
  wave operator): the computed kappa changes, so the term is not inert; C2 Y = d_tau (not g0-timelike at large m):
  Q is not positive definite at m = 2, so the energy is not coercive and K3's test fails on it.

    python3 checks/stage1rate5.py      (about a minute)
"""
import builtins
import math
import sys
import textwrap
from fractions import Fraction as Fr

import flint
import sympy as sp

OK = {}
MU0 = Fr(1)
MU_END = Fr(227, 192)
C_ENV = Fr(13241035, 10 ** 7)        # envelope5.out E1 (READ): c <= 1.3241035
A_LO = Fr(26985878, 10 ** 8)         # a = q0/2 >= 0.26985878 (lzerotrace5 T1: a in [0.269858788..., ...])
B_HI = Fr(134372083, 10 ** 7)        # b(tau0) <= 13.4372083 (lzeroconst5: 13.437208254)
DTAU = Fr(5937209, 10 ** 6)          # tau_end - tau0 <= 5.937209 (lzeroconst5, R2)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def forms(with_gamma=True, Yfield='g0'):
    tau = sp.Symbol('tau')
    xs = sp.symbols('x1:5')
    X = (tau,) + xs
    r = sp.sqrt(sum(q ** 2 for q in xs))
    mu = sp.Function('mu')
    m = mu(tau + r) / r ** 2
    xh = [q / r for q in xs]
    U, L = sp.Matrix([1] + xh), sp.Matrix([1] + [-q for q in xh])
    eta = sp.diag(-1, 1, 1, 1, 1)
    g, gi = eta + m * U * U.T, eta - m * L * L.T
    Y = -gi[:, 0] if Yfield == 'g0' else sp.Matrix([1, 0, 0, 0, 0])
    pi = sp.Matrix(5, 5, lambda a, b: sum(Y[c] * sp.diff(g[a, b], X[c]) + g[c, b] * sp.diff(Y[c], X[a])
                                          + g[a, c] * sp.diff(Y[c], X[b]) for c in range(5)))
    Gam = sp.Matrix([sum(sp.diff(gi[a, b], X[a]) for a in range(5)) for b in range(5)])
    R, mm, kk = sp.symbols('R m k', positive=True)
    sub = {xs[0]: R, xs[1]: 0, xs[2]: 0, xs[3]: 0}

    def ev(e):
        e = e.doit().subs(sub)
        e = e.replace(lambda q: isinstance(q, sp.Subs), lambda q: sp.Symbol('MUP'))
        e = e.subs(sp.Symbol('MUP'), kk * R).subs(mu(R + tau), mm * R ** 2)
        return sp.simplify(e)
    P, G = pi.applyfunc(ev), Gam.applyfunc(ev)
    Ye = Y.applyfunc(ev)
    gie = gi.applyfunc(ev)
    gYY = sp.simplify((Ye.T * g.applyfunc(ev) * Ye)[0])
    M = (gie * P * gie - sp.Rational(1, 2) * sum(gie[a, b] * P[a, b] for a in range(5) for b in range(5)) * gie) / 2
    if with_gamma:
        M = M + (Ye * G.T + G * Ye.T) / 2
    Q = Ye * Ye.T - sp.Rational(1, 2) * gYY * gie
    return (R * M).applyfunc(sp.simplify), Q.applyfunc(sp.simplify), (R * P).applyfunc(sp.simplify), \
        (R * G).applyfunc(sp.simplify), Ye, mm, kk, R


def to_arb_fn(expr, syms):
    num, den = sp.fraction(sp.together(expr))
    pn, pd = sp.Poly(num, *syms), sp.Poly(den, *syms)

    def ev(P, vals):
        tot = flint.arb(0)
        for mon, c in P.terms():
            t = flint.arb(int(sp.numer(c))) / int(sp.denom(c))
            for v_, e in zip(vals, mon):
                t *= v_ ** e
            tot += t
        return tot
    return lambda *vals: ev(pn, vals) / ev(pd, vals)


def arb_q(q):
    return flint.arb(q.numerator) / q.denominator


def sup_kappa(M, Q, mm, kk, ncell=400):
    """certified sup over Omega of (1/r) |generalized eigenvalues of (r M, Q)|"""
    a11, a12, a22 = M[0, 0], M[0, 1], M[1, 1]
    b11, b12, b22 = Q[0, 0], Q[0, 1], Q[1, 1]
    A = sp.simplify(b11 * b22 - b12 ** 2)
    B = sp.simplify(a11 * b22 + a22 * b11 - 2 * a12 * b12)
    C = sp.simplify(a11 * a22 - a12 ** 2)
    fA, fB, fC = (to_arb_fn(e, (mm, kk)) for e in (A, B, C))
    fang = to_arb_fn(sp.simplify(M[2, 2] / Q[2, 2]), (mm, kk))
    fdetq = fA
    best, worst_r = flint.arb(0), None
    ratio = (B_HI / A_LO) ** Fr(1, ncell) if False else None
    rs = [A_LO * (B_HI / A_LO) ** 0 + (B_HI - A_LO) * Fr(i, ncell) for i in range(ncell + 1)]
    mup = Fr(2, 9) * C_ENV ** 2
    for i in range(ncell):
        r0, r1 = rs[i], rs[i + 1]
        mlo, mhi = MU0 / r1 ** 2, MU_END / r0 ** 2
        khi = mup / r0
        loc = flint.arb(0)
        for jm in range(8):
            ml = mlo + (mhi - mlo) * Fr(jm, 8)
            mh = mlo + (mhi - mlo) * Fr(jm + 1, 8)
            mbox = flint.arb((arb_q(ml) + arb_q(mh)) / 2, (arb_q(mh) - arb_q(ml)) / 2)
            for jk in range(4):
                kl, kh = khi * Fr(jk, 4), khi * Fr(jk + 1, 4)
                kbox = flint.arb((arb_q(kl) + arb_q(kh)) / 2, (arb_q(kh) - arb_q(kl)) / 2)
                Av, Bv, Cv = fA(mbox, kbox), fB(mbox, kbox), fC(mbox, kbox)
                disc = Bv * Bv - 4 * Av * Cv
                sq = disc.sqrt() if disc > 0 else (abs(disc)).sqrt()
                lam = (abs(Bv) + sq) / (2 * Av) if Av > 0 else flint.arb('inf')
                if not (fdetq(mbox, kbox) > 0):
                    lam = flint.arb('inf')
                lam = max(lam, abs(fang(mbox, kbox)), key=lambda z: float(z.upper()))
                if float(lam.upper()) > float(loc.upper()):
                    loc = lam
        val = loc / arb_q(r0)
        if float(val.upper()) > float(best.upper()):
            best, worst_r = val, float(r0)
    return best, worst_r


def q_bounds(Q, Ye, mm, ncell=4000):
    """certified inf of Q's least eigenvalue, sup of its largest, and sup of Y^T Q^-1 Y over m in [mu0/b^2, mu_end/a^2]"""
    lam = sp.Symbol('lam')
    blk = Q[:2, :2]
    tr, dt = sp.simplify(blk.trace()), sp.simplify(blk.det())
    cy = sp.simplify((Ye[:2, :].T * blk.inv() * Ye[:2, :])[0])
    ftr, fdt, fang, fcy = (to_arb_fn(e, (mm,)) for e in (tr, dt, Q[2, 2], cy))
    mlo, mhi = MU0 / B_HI ** 2, MU_END / A_LO ** 2
    qlo, qhi, cyhi = flint.arb('inf'), flint.arb(0), flint.arb(0)
    for i in range(ncell):
        a_, b_ = mlo + (mhi - mlo) * Fr(i, ncell), mlo + (mhi - mlo) * Fr(i + 1, ncell)
        mb = flint.arb((arb_q(a_) + arb_q(b_)) / 2, (arb_q(b_) - arb_q(a_)) / 2)
        t, d = ftr(mb), fdt(mb)
        sq = (t * t - 4 * d).sqrt()
        lo_, hi_ = (t - sq) / 2, (t + sq) / 2
        ang = fang(mb)
        qlo = min(qlo, lo_, ang, key=lambda z: float(z.lower()))
        qhi = max(qhi, hi_, ang, key=lambda z: float(z.upper()))
        cyhi = max(cyhi, fcy(mb), key=lambda z: float(z.upper()))
    return qlo, qhi, cyhi, (tr, dt, cy)


def main():
    flint.ctx.prec = 120
    print('stage1rate5: Lemma 2.3 at gt = g0 on Omega at P*, its energy constant written out and certified')
    M, Q, P, G, Ye, mm, kk, R = forms()
    exp_P = {(0, 0): 2 * mm ** 2 - kk, (0, 1): 2 * mm + 2 * mm ** 2 - kk, (1, 1): 4 * mm + 2 * mm ** 2 - kk,
             (2, 2): -2 * mm}
    OK['K1'] = all(sp.simplify(P[i, j] - e) == 0 for (i, j), e in exp_P.items()) and sp.simplify(
        (Ye.T * (sp.diag(-1, 1, 1, 1, 1) + mm * sp.Matrix([1, 1, 0, 0, 0]) * sp.Matrix([[1, 1, 0, 0, 0]]))
         * Ye)[0] + 1 + mm) == 0
    print('  K1: r pi at xhat = e1 = %s (exact; matches the closed forms: %s); r Gamma = %s; Y = %s' % (
        [P[i, j] for i, j in ((0, 0), (0, 1), (1, 1), (2, 2))], OK['K1'], list(G), list(Ye)))
    qlo, qhi, cyhi, (tr, dt, cy) = q_bounds(Q, Ye, mm)
    kap, rworst = sup_kappa(M, Q, mm, kk)
    fac_log = kap * arb_q(DTAU) / 2
    q = qhi / qlo
    OK['K2'] = bool(qlo > 0)
    OK['K3'] = bool(kap.upper() < flint.arb('1e6')) and OK['K2']
    print('  K2: Q (tau, x1) block trace %s, det %s; Y^T Q^-1 Y = %s (exact); Q positive definite on Omega: %s' % (
        tr, dt, cy, OK['K2']))
    print('  K3 (certified): kappa <= %s (attained near r = %.4f); e^(kappa Dtau/2) <= exp(%s) = %s; q = q_hi/q_lo <= '
          '%s (q_lo >= %s, q_hi <= %s); c_Y^2 <= %s. So for stage 1\'s principal part ||du(tau)|| <= %s ||du(tau0)|| '
          '+ %s int ||f|| (Dtau <= 5.937209)' % (
              kap.upper().str(6, radius=False), rworst, fac_log.upper().str(6, radius=False),
              fac_log.exp().upper().str(4, radius=False), q.upper().str(6, radius=False),
              qlo.lower().str(6, radius=False), qhi.upper().str(6, radius=False), cyhi.upper().str(6, radius=False),
              (q.sqrt() * fac_log.exp()).upper().str(4, radius=False),
              (2 * cyhi.sqrt() / qlo.sqrt() * fac_log.exp()).upper().str(4, radius=False)))
    # controls
    M2, Q2, *_ = forms(with_gamma=False)
    kap2, _ = sup_kappa(M2, Q2, mm, kk, ncell=100)
    kap1, _ = sup_kappa(M, Q, mm, kk, ncell=100)
    OK['C1'] = abs(float(kap2.mid()) - float(kap1.mid())) > 1e-6
    print('  C1 (control): bulk without the Gamma term: kappa %s against %s on the coarse cover: differs: %s' % (
        kap2.mid().str(6), kap1.mid().str(6), OK['C1']))
    _, Q3, _, _, Y3, mm3, _, _ = forms(Yfield='dtau')
    ev3 = [sp.N(e.subs(mm3, 2)) for e in Q3.subs(mm3, 2).eigenvals()]
    OK['C2'] = any(e <= 0 for e in ev3)
    print('  C2 (control): Y = d_tau: Q at m = 2 has eigenvalues %s, not positive definite: K3\'s coercivity fails: %s'
          % ([round(float(e), 4) for e in ev3], OK['C2']))
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
