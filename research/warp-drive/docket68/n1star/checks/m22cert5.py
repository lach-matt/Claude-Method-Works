#!/usr/bin/env python3
"""m22cert5: the attempt at a certified lower bound m_lo on |M_22| by an a posteriori energy estimate (M22CERT5.md).
Labels: computed (exact, sympy), certified (exact rationals; Arb balls, python-flint), computed (floating point),
READ (cited values). It imports m22evol5.py (the system, the solver, the data) and changes nothing in it.

  X1 (exact) The tau-tau row of the lower-order operator. With eta = g0 - (mu/r^2) dv dv the flat metric of the
     Kerr-Schild Cartesian coordinates (in which the record's energy, Lemma 2.3 and Lemma 9.1, works componentwise),
     L := E - P_eta, P_eta(m) = -(1/2) g0^ab nabla^eta_a nabla^eta_b m, is the operator the estimate treats as forcing.
     Its tau-tau component, acting on the Cartesian scalar T = m(d_tau, d_tau) = m_vv (with m_vr = m_taur - T, m_rr =
     m_rr' - 2 m_taur + T), has no second derivative (the principal parts cancel), no d_th T, and
         L_tautau = (mu' r - mu/2)/r^3 e_tau T + (5 mu/2 - mu' r)/r^3 e_r T + z T + (other components),
     e_tau = d_tau, e_r = d_r at fixed tau (Euclidean unit vectors), z = (2 mu^3 - mu^2 r^2 + mu mu' r^3 - mu' r^5)/r^8.
  X2 (certified, exact rationals) An upper envelope rho^ >= rho of the outgoing null ray through X*, backwards from
     (tau*, a) in 2000 pieces with slopes (m_hi - 1)/(m_hi + 1), m_hi = mu_end/rho^2, rounded up.
  X3 (certified, Arb) The estimate's rate is at least (1/2) c_Y sup(||A|| q_lo^(-1/2)) with c_Y = 2^(1/2) exactly
     (stage1rate5 K2) and ||A|| >= |(5 mu/2 - mu' r)/r^3| (X1's e_r entry), evaluated on each piece at r = rho^ (a
     point of the slice), with mu >= 1, mu' <= (2/9) c^2 and q_lo, the least eigenvalue of Q (stage1rate5 K2), bounded
     above over m in [1/r^2, mu_end/r^2]. Its integral over [tau0, tau*] is a certified lower bound on the exponent of
     the estimate's Gronwall factor.
  X4 (computed, floating point) The residual: the tau-tau component of the PDE residual of the solver's interpolant,
     measured off the collocation nodes (on the grid with twice the nodes) at twelve times, at Nr x Nx = 32 x 12,
     40 x 12, 48 x 16, 64 x 20; the route's bound int e^(Lambda(s)) ||rho(s)|| ds against what m_lo > 0 needs, and the
     resolution at which it would fall below (extrapolated).
  X5 (computed) What m_lo buys (m22evol5's chain): the bounds at m_lo = 1 and 1/2.
  Controls (each mutates the computed path and must fail): C1 P_eta without its factor 1/2: X1's cancellation of the
  principal parts fails; C2 the envelope with each slope taken at the piece's end: X2's supersolution test fails; C3
  X3's bound evaluated at the outer boundary r = 3 - tau (a point of the slice, but where the coefficients are small):
  X3's threshold (a factor above 10^12) fails.

    python3 checks/m22cert5.py [--selftest]       (every check; about 20 minutes)
"""
import builtins
import contextlib
import io
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import flint
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import m22evol5 as ME              # noqa: E402  (the system, the solver, the Cauchy data)

OK = {}
T0 = time.time()
MU_END = Fr(227, 192)
C_HI = Fr(13241035, 10 ** 7)           # c <= 1.3241035 (envelope5.out E1, READ)
A_HI = Fr(26985880, 10 ** 8)           # a < 0.26985880, checked below from a^8 = 9/1250/2^8
NPIECE = 2000


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)
    sys.stdout.flush()


def el():
    return '[%.0fs]' % (time.time() - T0)


def arb(q):
    return flint.arb(q.numerator) / q.denominator if isinstance(q, Fr) else flint.arb(q)


# ------------------------------------------------------------------------------------------------------------------
# X1: the tau-tau row of L = E - P_eta
def tautau_row(res, half=sp.Rational(1, 2)):
    v, r, th, C, S, M0, M1 = ME.v, ME.r, ME.th, ME.C, ME.S, ME.M0, ME.M1_
    X5 = [v, r, th, sp.Symbol('p1'), sp.Symbol('p2')]
    eta = sp.diag(-1, 0, r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2)
    eta[0, 1] = eta[1, 0] = 1
    ei = eta.inv()
    gam = [[[sp.simplify(sum(ei[a, d] * (sp.diff(eta[d, b], X5[c]) + sp.diff(eta[d, c], X5[b])
                                          - sp.diff(eta[b, c], X5[d])) for d in range(5)) / 2)
             for c in range(5)] for b in range(5)] for a in range(5)]
    _, g0i = ME.background()
    g0i = g0i.subs(ME.Mf, M0)
    second = {(1, 1, 0): -half * 2 * g0i[0, 1], (0, 2, 0): -half * g0i[1, 1], (0, 0, 2): -half * g0i[2, 2],
              (2, 0, 0): -half * g0i[0, 0]}
    first = [half * sum(g0i[a, b] * gam[c][a][b] for a in range(5) for b in range(5)) for c in range(3)]
    J = {}
    for (fn, jet), c in res[('vv', 0)]['coef'].items():
        w = {'m_vv': 1, 'm_vr': -1, 'm_rr': 1}.get(fn)
        if w is not None:
            J[jet] = J.get(jet, 0) + w * c
    cancel = all(sp.simplify(J.get(j, 0) - s_) == 0 for j, s_ in second.items())
    a_ = sp.simplify(J.get((1, 0, 0), 0) - first[0])
    b_ = sp.simplify(J.get((0, 1, 0), 0) - first[1])
    c_ = sp.simplify(J.get((0, 0, 1), 0) - first[2])
    z_ = sp.simplify(J.get((0, 0, 0), 0))
    return cancel, a_, b_, c_, z_


def check_x1(res):
    cancel, a_, b_, c_, z_ = tautau_row(res)
    M0, M1, r = ME.M0, ME.M1_, ME.r
    et, er = sp.simplify(a_ - b_), b_
    want = (sp.simplify(et - (M1 * r - M0 / 2) / r ** 3) == 0 and sp.simplify(er - (5 * M0 / 2 - M1 * r) / r ** 3) == 0
            and c_ == 0 and sp.simplify(z_ - (2 * M0 ** 3 - M0 ** 2 * r ** 2 + M0 * M1 * r ** 3 - M1 * r ** 5) / r ** 8)
            == 0)
    OK['X1'] = cancel and want
    print('  X1 (exact): L = E - P_eta on the Cartesian scalar T = m(d_tau, d_tau): the principal parts cancel: %s; '
          'the e_tau, e_r, e_th coefficients are %s, %s, %s and the zero-order one %s (mu = M0, mu\' = M1): %s %s'
          % (cancel, et, er, c_, z_, OK['X1'], el()))
    bad = tautau_row(res, half=1)[0]
    OK['C1'] = not bad
    print('  C1 (control): P_eta without its factor 1/2: the principal parts cancel: %s, so X1 fails: %s'
          % (bad, OK['C1']))


# ------------------------------------------------------------------------------------------------------------------
# X2: the certified upper envelope of the ray, s = tau* - tau
def g_up(R):
    m = MU_END / (R * R)
    return (m - 1) / (m + 1)


def round_up(q, den=10 ** 12):
    return Fr(-((-q.numerator * den) // q.denominator), den)


def envelope_pieces(s_tot, at_end=False):
    ds = s_tot / NPIECE
    R, out = A_HI, []
    for _ in range(NPIECE):
        sl = g_up(R + ds) if at_end else g_up(R)
        R1 = round_up(R + ds * sl)
        out.append((R, R1, ds))
        R = R1
    return out


def super_ok(pieces):
    """each piece is linear from R0 to R1 with slope (R1 - R0)/ds >= g_up at every point of it (g_up decreasing in R,
    R nondecreasing on the piece, so the condition at R0 suffices), and stays in m_hi > 1 where g_up >= 0"""
    return all((R1 - R0) / ds >= g_up(R0) and R1 >= R0 for R0, R1, ds in pieces)


def check_x2():
    a_ok = (2 * A_HI) ** 8 > Fr(9, 1250)
    s_tot = 4 - Fr(26985878, 10 ** 8)                 # tau* - tau0 = 4 - a <= 4 - a_lo
    pieces = envelope_pieces(s_tot)
    ok = super_ok(pieces)
    OK['X2'] = a_ok and ok
    print('  X2 (certified, exact rationals): a < %s: %s; rho^ from (tau*, a^) back over %s in %d pieces is a '
          'supersolution of the backward ray equation with m <= mu_end/rho^2, so rho <= rho^: %s; rho^(tau0) = %.6f: '
          '%s' % (float(A_HI), a_ok, float(s_tot), NPIECE, ok, float(pieces[-1][1]), OK['X2']))
    OK['C2'] = not super_ok(envelope_pieces(s_tot, at_end=True))
    print('  C2 (control): each slope taken at the piece\'s end (where g_up is smaller): the supersolution test fails: '
          '%s' % OK['C2'])
    return pieces, s_tot


# ------------------------------------------------------------------------------------------------------------------
# X3: the certified lower bound on the estimate's exponent
def qlo_hi(r, n=16):
    """an upper bound of q_lo(m) over m in [1/r^2, mu_end/r^2]: the least eigenvalue of the (tau, x1) block of Q
    (trace m^2 + m + 1, det (m + 1)^2/4, so tr^2 - 4 det = m^2 (m^2 + 2 m + 2); the angular eigenvalue (1 + m)/2 is
    larger), in Arb on n sub-intervals of m, the largest upper end taken (rounded up)"""
    lo, hi = 1 / (r * r), MU_END / (r * r)
    best = 0.0
    for i in range(n):
        a_, b_ = lo + (hi - lo) * Fr(i, n), lo + (hi - lo) * Fr(i + 1, n)
        m = flint.arb((arb(a_) + arb(b_)) / 2, (arb(b_) - arb(a_)) / 2)
        tr, det = m * m + m + 1, (m + 1) ** 2 / 4
        lam = 2 * det / (tr + m * (m * m + 2 * m + 2).sqrt())
        best = max(best, float(lam.upper()) * (1 + 1e-12))
    return best


def k_lo(r):
    """(1/2) c_Y |b| / q_lo^(1/2) >= (1/2) 2^(1/2) (5/2 - (2/9) c^2 r)/r^3 / q_lo_hi^(1/2), at the point r of the
    slice"""
    rr = arb(r)
    b = (flint.arb(5) / 2 - flint.arb(2) / 9 * arb(C_HI) ** 2 * rr) / rr ** 3
    return (flint.arb(2).sqrt() / 2 * b / flint.arb(qlo_hi(r)).sqrt()).lower()


def check_x3(pieces, outer=False):
    tau_star_hi = 2 - Fr(26985878, 10 ** 8)
    tot, prof, s = flint.arb(0), [], Fr(0)
    inside = True
    for R0, R1, ds in pieces:
        if outer:
            pt = 3 - tau_star_hi + s          # r = 3 - tau at the piece's later end (smallest outer radius)
        else:
            pt = R1                           # >= rho(tau) on the whole piece
            inside &= pt <= 3 - tau_star_hi + s
        tot += k_lo(pt) * arb(ds)
        s += ds
        prof.append((float(s), float(tot.lower())))
    return tot.lower(), prof, inside


# ------------------------------------------------------------------------------------------------------------------
# X4: the residual, measured off the nodes
def bary_lobatto(xs, xt):
    n = len(xs)
    w = np.array([(-1.0) ** j * (0.5 if j in (0, n - 1) else 1.0) for j in range(n)])
    P = np.zeros((len(xt), n))
    for i, x in enumerate(xt):
        d = x - xs
        k = np.where(np.abs(d) < 1e-14)[0]
        if len(k):
            P[i, k[0]] = 1.0
        else:
            q = w / d
            P[i] = q / q.sum()
    return P


def cc_weights(N):
    xg = np.cos(np.pi * np.arange(N) / (N - 1))
    V = np.polynomial.chebyshev.chebvander(xg, N - 1)
    mom = np.array([0.0 if k % 2 else 2.0 / (1 - k * k) for k in range(N)])
    return np.linalg.solve(V.T, mom)


def xreg(Sv, tau, st):
    out = Sv.rhs(tau, st)
    _, L, speed = Sv.grid(tau)
    return out[1][0] - speed[:, None] * Sv.dr(st[1][0], L)


def residual_norm(Sv, Sf, tau, st):
    """|| alpha (I X_c - X(I u)) || over the slice in the measure pi^2 r^3 dx dr (the tau-tau component)"""
    xi_c = (1 - np.cos(np.pi * np.arange(Sv.Nr) / (Sv.Nr - 1))) / 2
    xi_f = (1 - np.cos(np.pi * np.arange(Sf.Nr) / (Sf.Nr - 1))) / 2
    Pr = bary_lobatto(xi_c, xi_f)
    Vc = np.polynomial.chebyshev.chebvander(Sv.x, Sv.Nx - 1)
    Ix = np.polynomial.chebyshev.chebvander(Sf.x, Sv.Nx - 1) @ np.linalg.inv(Vc)
    lift = lambda u: Pr @ u @ Ix.T                                  # noqa: E731
    m, pi, psi, phi, G = st
    stf = ([lift(u) for u in m], [lift(u) for u in pi], [lift(u) for u in psi], lift(phi), [lift(u) for u in G])
    Xc, Xf = xreg(Sv, tau, st), xreg(Sf, tau, stf)
    r1, L, _ = Sf.grid(tau)
    rr = r1[:, None] * np.ones((1, Sf.Nx))
    mm = Sf.mu(tau + rr) / rr ** 2
    rho = (1 + mm) / 2 * (lift(Xc) - Xf)
    wr = cc_weights(Sf.Nr) / 2 * L
    wx = np.pi / Sf.Nx * np.sqrt(1 - Sf.x ** 2)
    return float(np.sqrt(np.pi ** 2 * np.einsum('i,j,ij->', wr, wx, rho ** 2 * rr ** 3)))


def run_with_samples(funcs, env, fode, Nr, Nx, cfl, targets):
    Sv = ME.Solver(Nr, Nx, funcs, env)
    st = ME.cauchy_data(Sv, fode)
    steps, t = [], ME.TAU0
    while t < ME.TAU_STAR - 1e-14:
        _, Lt, _ = Sv.grid(t)
        h = min(cfl * Lt / Nr ** 2, ME.TAU_STAR - t)
        steps.append(h)
        t += h
    tau, out, ti = ME.TAU0, [], 0
    Sf = ME.Solver(2 * Nr, 2 * Nx, funcs, env)
    out.append((tau, residual_norm(Sv, Sf, tau, st)))
    with np.errstate(all='ignore'):
        for i, h in enumerate(steps):
            k1 = Sv.rhs(tau, st)
            k2 = Sv.rhs(tau + h / 2, ME.axpy(st, k1, h / 2))
            k3 = Sv.rhs(tau + h / 2, ME.axpy(st, k2, h / 2))
            k4 = Sv.rhs(tau + h, ME.axpy(st, k3, h))
            comb = tuple([(p + 2 * q + 2 * s_ + w) / 6 for p, q, s_, w in zip(a, b, c, d)] if isinstance(a, list)
                         else (a + 2 * b + 2 * c + d) / 6 for a, b, c, d in zip(k1, k2, k3, k4))
            st = ME.axpy(st, comb, h)
            tau += h
            while ti < len(targets) and tau >= targets[ti] - 1e-12:
                out.append((tau, residual_norm(Sv, Sf, tau, st)))
                ti += 1
    return out, ME.m22(Sv, st)


def check_x4(funcs, env, fode, prof, s_tot):
    targets = list(np.linspace(-1.6, 1.6, 9)) + [1.7, float(ME.TAU_STAR) - 1e-9]
    s_arr, l_arr = np.array([p[0] for p in prof]), np.array([p[1] for p in prof])
    rows = {}
    for cfg in ((32, 12, 1.0), (40, 12, 1.0), (48, 16, 1.0), (64, 20, 1.0)):
        t1 = time.time()
        smp, m22v = run_with_samples(funcs, env, fode, *cfg, targets)
        taus = np.array([q[0] for q in smp])
        rn = np.array([q[1] for q in smp])
        # Lambda(tau) = int_tau^tau* k_lo: prof is cumulative from tau* backwards in s = tau* - tau
        lam = np.interp(ME.TAU_STAR - taus, s_arr, l_arr)
        route = float(np.trapezoid(np.exp(lam) * rn, taus))
        rows[cfg] = (taus, rn, lam, route, m22v, time.time() - t1)
        print('    %d x %d: M_22 = %.9f; ||rho_tautau|| at tau = %s: %s; Lambda there %s; the route\'s bound int '
              'e^Lambda ||rho|| ds = %.3e (%.0fs) %s'
              % (cfg[0], cfg[1], m22v, ', '.join('%.2f' % t for t in taus), ', '.join('%.1e' % x for x in rn),
                 ', '.join('%.1f' % x for x in lam), route, time.time() - t1, el()))
    return rows


# ------------------------------------------------------------------------------------------------------------------
def main():
    print('m22cert5: the attempt at a certified lower bound m_lo on |M_22| (M22CERT5.md)')
    flint.ctx.prec = 120
    with contextlib.redirect_stdout(io.StringIO()):
        out, unk = ME.ric_h()
        res = ME.extract(out, unk)
    check_x1(res)
    pieces, s_tot = check_x2()
    lam, prof, inside = check_x3(pieces)
    lam_o, _, _ = check_x3(pieces, outer=True)
    a1 = arb(A_HI)
    vol = (flint.arb.pi() ** 2 / 2 * ((1 + a1) ** 4 - a1 ** 4)).upper()
    volm = (flint.arb(vol) + flint.arb.pi() ** 2 * arb(MU_END) * ((1 + a1) ** 2 - a1 ** 2)).upper()
    cpt = 1 / math.sqrt(float(volm)) * (1 - 1e-12)
    need = 2.207738 / (cpt / math.sqrt(2))
    fac = math.exp(float(lam))
    OK['X3'] = inside and fac > 1e12
    print('  X3 (certified, Arb): every evaluation point lies in its slice: %s; int_(tau0)^(tau*) k dtau >= %.4f, so '
          'the estimate\'s Gronwall factor for E^(1/2) from tau0 is >= e^%.4f = %.3e (from X1\'s e_r entry alone; the '
          'other rows, the zero-order terms, the couplings, the transports and the commuted energies only add); half '
          'of the exponent is gathered after tau = %.2f: %s %s'
          % (inside, float(lam), float(lam), fac,
             float(ME.TAU_STAR) - next(s_ for s_, l_ in prof if l_ >= float(lam) / 2), OK['X3'], el()))
    OK['C3'] = not math.exp(float(lam_o)) > 1e12
    print('  C3 (control): the same bound evaluated at the outer boundary r = 3 - tau: e^%.4f = %.3e: X3\'s threshold '
          'fails: %s' % (float(lam_o), math.exp(float(lam_o)), OK['C3']))
    print('  The requirement (deduced from X3): the route\'s point-evaluation constant, |e(X*)| <= C_pt E_s(tau*)^(1/2) '
          'with E_s containing int (1 + m) |e|^2 (the zero-order current), is >= (int over the tau* slice of (1 + '
          'm))^(-1/2) '
          '>= %.4f (the constant field; vol = %.3f, with m: %.3f); the forcing enters with c_Y/2 = 2^(-1/2); so the '
          'route certifies m_lo > 0 only if int_(tau0)^(tau*) e^(Lambda(s)) ||rho(s)|| ds < |M_22| 2^(1/2)/C_pt <= '
          '%.2f, '
          'Lambda(s) the exponent gathered from s to tau* (>= X3\'s profile), rho the residual (every component; its '
          'tau-tau part is a lower bound)' % (cpt, float(vol), float(volm), need))
    funcs, env = ME.load_system(res), ME.envelope()
    with contextlib.redirect_stdout(io.StringIO()):
        fode = ME.mode_setup()
    rows = check_x4(funcs, env, fode, prof, s_tot)
    b48, b64 = rows[(48, 16, 1.0)][3], rows[(64, 20, 1.0)][3]
    OK['X4'] = all(np.isfinite(r_[3]) for r_ in rows.values()) and b64 < b48 and b64 > need
    print('  X4 (computed, floating point): the route\'s bound for the solver\'s solution, int e^Lambda ||rho_tautau|| '
          'ds (rho_tautau alone, a lower bound on the residual the route needs), is %.2e at 32 x 12, %.2e at 40 x 12, '
          '%.2e at 48 x 16 and %.2e at 64 x 20, against the %.2f it must stay below: still a factor %.1e above it at '
          'the finest grid, though falling: %s' % (rows[(32, 12, 1.0)][3], rows[(40, 12, 1.0)][3], b48, b64, need,
                                                  b64 / need, OK['X4']))
    step = b48 / b64
    k = math.log(b64 / need) / math.log(step)
    kk = math.ceil(k)
    Nr, Nx = 64 + 16 * kk, 20 + 4 * kk
    t64 = rows[(64, 20, 1.0)][5]
    cost = t64 * (Nr / 64) ** 2 * (Nr * Nx * (Nr + Nx)) / (64 * 20 * 84)
    print('  Resolution and cost (extrapolated from the last two grids, floating point): one step (+16 in r, +4 in x) '
          'divides the bound by %.1f, so it would fall below %.2f after %.1f more steps, at about %d x %d; the run with '
          'its residual took %.0f s at 64 x 20, and scales as Nr^3 Nx (Nr + Nx), so about %.0f s there. That is for '
          'the lower bound of X3 alone, with the residual measured, not certified, and of the tau-tau component only'
          % (step, need, k, Nr, Nx, t64, cost))
    m1, mh = ME.lam_of(1.0), ME.lam_of(0.5)
    OK['X5'] = m1[0] < 0.0024433 and mh[0] < 0.0024433
    print('  X5 (computed): a certified m_lo would give lambda0 < %s at m_lo = 1 and %s at m_lo = 1/2 (operator norm, '
          'Frobenius, largest entry), against the certified 0.0024433, 0.0019079, 0.0012228, which stand: %s'
          % (', '.join('%.7f' % x for x in m1), ', '.join('%.7f' % x for x in mh), OK['X5']))
    for k, val in OK.items():
        builtins.print(k, 'PASS' if val else 'FAIL')
    builtins.print('m22cert5: %d/%d %s' % (sum(OK.values()), len(OK), el()))
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] not in ('--selftest',):
        builtins.print('usage: python3 checks/m22cert5.py [--selftest]   (both run every check)')
        sys.exit(2)
    sys.exit(main())
