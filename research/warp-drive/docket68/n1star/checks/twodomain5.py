#!/usr/bin/env python3
"""twodomain5: the record's Lemma 1.1 for the two-dust background (FAMILIES5 4i, D533).

The record's Lemma 1.1 (N1STAR-PROOF.md:154-173) is read off g0 = eta + (mu(v)/r^2) dv dv, five-dimensional Vaidya. For
two null dusts (FAMILIES5 4c, `twodust5.py`: g0 = -2 e^(2s) du dv + R^2 dOmega_3^2, K_in R^3 = A(v), K_out R^3 = B(u),
both >= 0) the background is not explicit. This checks that it nevertheless takes the record's form with one more
function, and what that does to the lemma.

  D1 (exact, sympy) with vhat(v) any increasing function and psi := ln(-e^(2s)/(R_u vhat')), f := -2 e^(-2s) R_u R_v = 1
     - mu/R^2 (mu as in twodust5 B3): wherever R_u < 0, (vhat, R) are coordinates, the (u, v) part of g0 is -e^(2 psi) f
     dvhat^2 + 2 e^psi dvhat dR, and its inverse is g^(vhat vhat) = 0, g^(vhat R) = e^(-psi), g^(RR) = f. Modulo the
     constraint C_u = 0: (e^(-2s) R_u)_u = -e^(-2s) B/(3R^2) and psi_u = B/(3 R^2 R_u). So, with B >= 0 and R_u < 0 on
     the outer cone u = u_0, R_u < 0 everywhere, and with vhat fixed by psi = 0 on u = u_0, psi <= 0 everywhere. With B
     = 0, psi = 0 and mu = mu(vhat): the record's Vaidya.
  D2 (exact) with tau := vhat - R: g^-1(dtau, dtau) = f - 2e^(-psi), g^-1(dR, dtau) = e^(-psi) - f, g^-1(d(vhat + tau),
     d(vhat + tau)) = f - 4e^(-psi); at psi = 0 the record's -1 - mu/r^2, mu/r^2 and -3 - mu/r^2 (Lemma 1.1 (a)-(c)).
     Since psi <= 0 and f <= 1: g^-1(dtau, dtau) <= -1 - mu/R^2, g^-1(d(vhat + tau), .) <= -3 - mu/R^2, and on R = a,
     g^-1(dR, dR) = 1 - mu/a^2 < 0 exactly when mu > a^2 there.
  D3 (computed) a seeded hole: corner data with mass mu0 = 1 at R = 4 (mu and R_u as 5D Tangherlini's, the gauge e^(2s)
     = R_v = 1/2); an ingoing pulse A = sin^4 on v in [0.5, 2] (mu to about 1.5) and an outgoing one B = 0.4 sin^4 on u
     in [1, 2]; twodust5's diamond scheme on u in [0, U1], v in [0, 2], U1 where R(U1, 2) = 0.62, clear of the
     singularity in R (min R about 0.67; later v needs resolving a strip between the horizon and the singularity that
     thins exponentially in v). At n = 40, 80, 160 steps per unit: R_u < 0 everywhere; with B = 0, max |psi| and max |mu
     - mu(v)| fall with n (discretisation, about first order near R = a, where R_u is steep); with B, max psi falls with
     n to 0 and min psi rises with n (-0.077, -0.035, -0.016, -0.0098 at n = 40 to 320, verifier 231), its limit small
     and negative, and |mu - mu(v)| is about 0.1, also still moving with n; max g^-1(dtau, dtau) <= -1, its ratio to -1
     - mu/R^2 rising to 1 with n (at least 1 analytically; 0.99 at n = 160 is the tolerance; the maximum sits on the
     data cone u = 0); the cells with a <= R <= a + 0.05, a = 0.7, are trapped with mu - a^2 >= 0.5, but on this
     rectangle they lie only at v >= 1.975 (verifier 231).
  D3b (computed) the inner boundary on the whole curve R = a (D537): on u in [0, 8], v in [0, 2], cells with R <= 0.3
     left out, at n = 80 and 160, every v-column crosses R = a = 0.7, the last cell with R >= a is trapped in every
     column, and min mu - a^2 there is 0.510 (B = 0) and 0.413 (B = 0.4), the same at both n to 10^-3.
  D4 (computed control) a strong outgoing pulse just outside the horizon (B = 3 sin^4 on u in [3.5, 5]) carries enough
     mass out that mu < a^2 on part of R = a, which is then not trapped there: (b) fails while (a) and (c) hold, so
     (b)'s condition is a real one.

Run: python3 checks/twodomain5.py   (about 45 seconds)
"""
import math
import sys

import numpy as np
import sympy as sp


def d1_d2():
    u, v = sp.symbols('u v')
    R, s, vh, Bf = sp.Function('R')(u, v), sp.Function('s')(u, v), sp.Function('vh')(v), sp.Function('B')(u)
    Ru, Rv, vp = sp.diff(R, u), sp.diff(R, v), sp.diff(vh, v)
    gold = sp.Matrix([[0, -sp.exp(2 * s)], [-sp.exp(2 * s), 0]])          # -2 e^(2s) du dv
    J = sp.Matrix([[0, vp], [Ru, Rv]])                                     # d(vhat, R)/d(u, v)
    Ji = J.inv()
    gnew = sp.simplify(Ji.T * gold * Ji)
    psi = sp.log(-sp.exp(2 * s) / (Ru * vp))
    f = -2 * sp.exp(-2 * s) * Ru * Rv
    want = sp.Matrix([[-sp.exp(2 * psi) * f, sp.exp(psi)], [sp.exp(psi), 0]])
    ok_form = sp.simplify(gnew - want) == sp.zeros(2, 2)
    ginv = sp.simplify(gnew.inv())
    ok_inv = sp.simplify(ginv - sp.Matrix([[0, sp.exp(-psi)], [sp.exp(-psi), f]])) == sp.zeros(2, 2)
    Ruu = 2 * sp.diff(s, u) * Ru - Bf / (3 * R**2)                          # C_u = 0
    ray = sp.simplify(sp.diff(sp.exp(-2 * s) * Ru, u).subs(sp.diff(R, u, 2), Ruu) + sp.exp(-2 * s) * Bf / (3 * R**2))
    psiu = sp.simplify(sp.diff(psi, u).subs(sp.diff(R, u, 2), Ruu) - Bf / (3 * R**2 * Ru))
    ok_u = ray == 0 and psiu == 0
    # D2: contractions in (vhat, R) with tau = vhat - R
    P, F = sp.symbols('psi f')
    gi = sp.Matrix([[0, sp.exp(-P)], [sp.exp(-P), F]])
    dtau, dR, dvt = sp.Matrix([1, -1]), sp.Matrix([0, 1]), sp.Matrix([2, -1])
    c = [sp.simplify((a.T * gi * b)[0]) for a, b in ((dtau, dtau), (dR, dtau), (dvt, dvt))]
    ok_c = (sp.simplify(c[0] - (F - 2 * sp.exp(-P))) == 0 and sp.simplify(c[1] - (sp.exp(-P) - F)) == 0
            and sp.simplify(c[2] - (F - 4 * sp.exp(-P))) == 0)
    mu, r = sp.symbols('mu r', positive=True)
    rec = [sp.simplify(x.subs({P: 0, F: 1 - mu / r**2})) for x in c]
    ok_rec = (sp.simplify(rec[0] + 1 + mu / r**2) == 0 and sp.simplify(rec[1] - mu / r**2) == 0
              and sp.simplify(rec[2] + 3 + mu / r**2) == 0)
    return ok_form, ok_inv, ok_u, ok_c and ok_rec


def bump(x, a, b):
    w = (x - a) / (b - a)
    return np.where((w > 0) & (w < 1), np.sin(np.pi * np.clip(w, 0, 1))**4, 0.0)


def cone(x, src, R0, R1, n):
    """R'' = -src(x)/(3 R^2) along a cone (s constant there), RK4 on n steps (twodust5's)"""
    h = (x[-1] - x[0]) / n
    R = np.empty(n + 1)
    P = np.empty(n + 1)
    R[0], P[0] = R0, R1
    fn = lambda xx, y: np.array([y[1], -src(np.array(xx)) / (3 * y[0]**2)])
    for k in range(n):
        y = np.array([R[k], P[k]])
        k1 = fn(x[k], y); k2 = fn(x[k] + h / 2, y + h / 2 * k1); k3 = fn(x[k] + h / 2, y + h / 2 * k2)
        k4 = fn(x[k] + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        R[k + 1], P[k + 1] = y
    return R, P


def solve(n, A, B, mu0=1.0, R0=4.0, U1=6.4, V1=2.0, Rmin=0.3):
    """twodust5's diamond scheme with seeded corner data: R = R0, R_v = 1/2, e^(2s) = 1/2 and mu = mu0 at (0, 0);
    cells whose past neighbours reach R <= Rmin are left out (nan)"""
    Nu, Nv = int(round(U1 * n)), int(round(V1 * n))
    uu, vv = np.linspace(0, U1, Nu + 1), np.linspace(0, V1, Nv + 1)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    R = np.full((Nu + 1, Nv + 1), np.nan)
    S = np.full((Nu + 1, Nv + 1), -math.log(2) / 2)
    R[0], _ = cone(vv, A, R0, 0.5, Nv)
    R[:, 0], _ = cone(uu, B, R0, (mu0 / R0**2 - 1) / 2, Nu)
    for i in range(1, Nu + 1):
        for j in range(1, Nv + 1):
            rs, re, rw = R[i - 1, j - 1], R[i - 1, j], R[i, j - 1]
            if not (rs > Rmin and re > Rmin and rw > Rmin):
                continue
            ss, se, sw = S[i - 1, j - 1], S[i - 1, j], S[i, j - 1]
            rn, sn = re + rw - rs, se + sw - ss
            for _ in range(3):
                rc, sc = (rs + re + rw + rn) / 4, (ss + se + sw + sn) / 4
                ru = (rw - rs + rn - re) / (2 * du)
                rv = (re - rs + rn - rw) / (2 * dv)
                Fc = math.exp(2 * sc) + 2 * ru * rv
                rn = re + rw - rs - du * dv * Fc / rc
                sn = se + sw - ss + du * dv * 1.5 * Fc / rc**2
            R[i, j], S[i, j] = rn, sn
    return uu, vv, R, S


def corner_u(A, B, V1=2.0, Rc=0.62):
    """the u at which R(u, V1) falls to Rc, from a run at n = 160 on a long rectangle: the rectangle [0, U1] x [0, V1]
    then reaches R = a = 0.7 inside the trapped region and stays clear of the singularity"""
    uu, vv, R, S = solve(160, A, B, U1=8.0, V1=V1)
    col = R[:, -1]
    return float(uu[np.where(np.isfinite(col) & (col >= Rc))[0][-1]])


def inner_curve(n, A, B, a=0.7, U1=8.0, V1=2.0):
    """D3b: along each v-column the last cell with R >= a before R falls below a; whether every column has one, all
    trapped (R_v < 0), and the least mu - a^2 there"""
    uu, vv, R, S = solve(n, A, B, U1=U1, V1=V1)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2 * (1 + 2 * np.exp(-2 * S) * Ru * Rv)
    cols, mua, trapped = 0, [], True
    for j in range(R.shape[1]):
        idx = np.where(np.isfinite(R[:, j]) & (R[:, j] < a))[0]
        if len(idx) == 0 or idx[0] < 2 or not np.isfinite(mu[idx[0] - 1, j]):
            continue
        i = idx[0] - 1
        cols += 1
        mua.append(mu[i, j] - a * a)
        trapped &= bool(Rv[i, j] < 0)
    return cols, R.shape[1], min(mua), trapped

def measure(n, A, B, a=0.7, **kw):
    uu, vv, R, S = solve(n, A, B, **kw)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2 * (1 + 2 * np.exp(-2 * S) * Ru * Rv)
    vhp = -np.exp(2 * S[0]) / Ru[0]                      # psi = 0 on u = 0
    psi = np.log(-np.exp(2 * S) / (Ru * vhp[None, :]))
    f = 1 - mu / R**2
    m = R >= a
    nb = m & (R <= a + 0.05)
    return dict(minR=float(np.min(R)), Ru_neg=bool(np.max(Ru) < 0), psimax=float(psi[m].max()),
                psimin=float(psi[m].min()), dmu=float(abs(mu - mu[0][None, :])[m].max()),
                ga=float((f - 2 * np.exp(-psi))[m].max()), gc=float((f - 4 * np.exp(-psi))[m].max()),
                ga_rel=float(((f - 2 * np.exp(-psi)) / (-1 - mu / R**2))[m].min()),
                nb=int(nb.sum()), nb_trapped=bool((nb.sum() > 0) and (Rv[nb] < 0).all()),
                mua=float(mu[nb].min() - a * a) if nb.any() else float('nan'),
                trapped=int((Rv[m] < 0).sum()), fb=float(f[nb].max()) if nb.any() else float('nan'))


def main():
    ok = {}
    f1, f2, f3, f4 = d1_d2()
    ok['D1'] = f1 and f2 and f3
    ok['D2'] = f4
    print('  D1: (vhat, R) form %s, inverse %s, (e^(-2s) R_u)_u and psi_u modulo C_u %s' % (f1, f2, f3))
    print('  D2: the three contractions, and the record\'s at psi = 0: %s' % f4, flush=True)

    A = lambda x: bump(x, 0.5, 2.0)
    zero = lambda x: 0.0 * x
    Bw = lambda x: 0.4 * bump(x, 1.0, 2.0)
    r0, rB = {}, {}
    U0, UB = corner_u(A, zero), corner_u(A, Bw)
    print('    rectangles: u in [0, %.3f] (B = 0) and [0, %.3f] (B = 0.4), v in [0, 2]' % (U0, UB))
    for n in (40, 80, 160):
        r0[n] = measure(n, A, zero, U1=U0)
        rB[n] = measure(n, A, Bw, U1=UB)
        for lab, r in (('B = 0', r0[n]), ('B = 0.4', rB[n])):
            print('    n = %d, %s: min R %.3f, R_u < 0 %s, psi in [%.4f, %.4f], max|mu - mu(v)| %.4f, max g(dtau, dtau) '
                  '%.4f (ratio to -1 - mu/R^2 >= %.4f), max g(d(v+tau)) %.4f; %d cells on a <= R <= a + 0.05, all '
                  'trapped %s, mu - a^2 >= %.4f' % (n, lab, r['minR'], r['Ru_neg'], r['psimin'], r['psimax'], r['dmu'],
                                                    r['ga'], r['ga_rel'], r['gc'], r['nb'], r['nb_trapped'], r['mua']),
                  flush=True)
    conv0 = r0[160]['psimax'] < r0[80]['psimax'] < r0[40]['psimax'] and r0[160]['dmu'] < r0[80]['dmu'] < r0[40]['dmu'] \
        and max(r0[160]['psimax'], -r0[160]['psimin']) < 0.02
    convB = rB[160]['psimax'] < rB[80]['psimax'] < rB[40]['psimax'] and rB[160]['psimax'] < 0.02
    geo = all(r['Ru_neg'] and r['ga'] < -1 and r['gc'] < -3 for r in list(r0.values()) + list(rB.values())) and all(
        r[40]['ga_rel'] < r[80]['ga_rel'] <= r[160]['ga_rel'] and r[160]['ga_rel'] > 0.99 for r in (r0, rB))
    inner = all(r['nb'] > 0 and r['nb_trapped'] and r['mua'] > 0.5 for r in (r0[160], rB[160]))
    ok['D3'] = conv0 and convB and geo and inner
    print('  D3: B = 0 converges to Vaidya (psi, mu - mu(v) -> 0) %s; with B, max psi -> 0 %s; R_u < 0 and (a), (c) '
          'with the record\'s margins %s; inner boundary trapped with mu > a^2 %s' % (conv0, convB, geo, inner))

    d3b = True
    for lab, Bf in (('B = 0', zero), ('B = 0.4', Bw)):
        res = {n: inner_curve(n, A, Bf) for n in (80, 160)}
        for n, (c, tot, m, tr) in res.items():
            print('    D3b, %s, n = %d: %d of %d v-columns cross R = a, all trapped %s, min mu - a^2 %.4f'
                  % (lab, n, c, tot, tr, m), flush=True)
        d3b &= all(c == tot and tr and m > 0.4 for c, tot, m, tr in res.values()) and abs(res[80][2] - res[160][2]) < 1e-3
    ok['D3b'] = d3b
    print('  D3b: the whole curve R = a crossed, trapped, mu > a^2: %s' % d3b, flush=True)

    Bs = lambda x: 3.0 * bump(x, 3.5, 5.0)
    rc = measure(80, A, Bs, U1=corner_u(A, Bs))
    ok['D4'] = rc['nb'] > 0 and rc['mua'] < 0 and rc['fb'] > 0 and rc['ga'] < -1 and rc['gc'] < -3
    print('  D4: strong outgoing pulse: %d cells on a <= R <= a + 0.05, min mu - a^2 = %.4f (negative), 1 - mu/R^2 up to '
          '%.4f there, so R = a is not trapped everywhere and (b) fails; (a), (c) still hold (%.4f, %.4f)'
          % (rc['nb'], rc['mua'], rc['fb'], rc['ga'], rc['gc']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
