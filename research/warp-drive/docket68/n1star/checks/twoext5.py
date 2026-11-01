#!/usr/bin/env python3
"""twoext5: an extension principle for the two-dust background (FAMILIES5 4c, 4i; D552).

[Mos17] (G. Moschidis, The Einstein-null dust system in spherical symmetry with an inner mirror, arXiv:1704.08685)
Lemma 5.1 (pp. 42-43, READ): for the spherically symmetric Einstein-null dust system with ingoing and outgoing dust in
3 + 1, a smooth solution on [u1, u2) x [v1, v2) whose data on the two initial cones extend smoothly to their far ends,
with inf r > 0 and sup r < oo, extends smoothly to [u1, u2] x [v1, v2]. The proof integrates d_u d_v (r^2) = -(1/2)(1 -
Lam r^2) Omega^2 ((5.210), (5.217)), d_u d_v log Omega^2 = (m~ r^-3 + Lam/6) Omega^2 ((5.211), (5.218)) and the mass's
d_u d_v m~ = 32 pi^2 r^-1 Omega^-2 (r^2 T_vv)(r^2 T_uu) ((5.212), (5.219)), and needs (5.220)-(5.222): int int Omega^2,
|m~| and the dust bounded. The 5D two-dust form (twodust5 B1-B3: g0 = -2 e^(2s) du dv + R^2 dOmega_3^2, K_in R^3 = A(v),
K_out R^3 = B(u), A, B >= 0):

  X1 (exact, sympy) on the evolution, with mu := R^2 (1 + 2 e^(-2s) R_u R_v):
         (R^3)_uv = -3 R e^(2s),   R_uv = -e^(2s) mu/R^3,   s_uv = (3/2) e^(2s) mu/R^4;
     R^3 plays r^2's part (the cross term R_u R_v cancels at exponent 3 exactly).
  X2 (exact) with the constraints C_u, C_v as well: mu_uv = (2/9) A B e^(-2s)/R^2 >= 0, the cross term of the two dusts.
  The chain (deduced) on Q = [u1, u2) x [v1, v2) with R >= a > 0; D[F](u, v) := F(u1, v) + F(u, v1) - F(u1, v1), the
  data's corner combination, |Q| the area:
    (i)   3 int int R e^(2s) = D[R^3] - R^3, so R <= Rmax := (max D[R^3])^(1/3) (sup R needs no hypothesis) and
          int int R e^(2s) <= Rmax^3/3;
    (ii)  mu >= m0 := min D[mu] (X2);
    (iii) s >= min D[s] - (3/2)(m0^-/a^5) Rmax^3/3 =: -S, m0^- := max(0, -m0) (X1, e^(2s)/R^4 <= R e^(2s)/a^5);
    (iv)  mu <= max D[mu] + (2/9) max(AB) e^(2S) |Q|/a^2 =: M;
    (v)   s <= max D[s] + (3/2)(M^+/a^5) Rmax^3/3;
    (vi)  R_u, R_v by integrating R_uv = -e^(2s) mu/R^3 from the cones; higher derivatives by commuting, the commuted
          equations linear in the top order, as [Mos17] does. So (R, s) extend to the closed rectangle, and the
          background exists on any characteristic rectangle on which R stays >= a > 0, which [Mos17]'s local existence
          (its Proposition 5.3, by the same Picard iteration in 5D) turns into: the development ends only where R -> 0.
  X3 (computed) on D3's background (twodomain5: seeded corner, A = sin^4 on v in [0.5, 2], B = 0.4 sin^4 on u in [1, 2],
     u in [0, U1], R(U1, 2) = 0.62): (i)'s identity on the computed solution, its residual falling with n = 40 to 320
     (ratios 1.72, 2.88, 3.48, approaching second order; first order near R = a at coarse n, as D3 records); and the bounds (i)-(v) from the
     cones' data alone contain the computed R, mu and s (mu and s attain their lower bounds on the data, mu_uv and
     s_uv being >= 0 there; the upper bounds are coarse, s <= 2.7e3 against 1.12).
  Control: X1 with R^2 in place of R^3 leaves the cross term -2 R_u R_v (the 4D identity is not the 5D one); X2 with B
     depending on v leaves a residual.

Run: python3 checks/twoext5.py   (about a minute)
"""
import math
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import twodomain5 as TD                                                         # noqa: E402


def identities():
    u, v = sp.symbols('u v')
    R = sp.Function('R')(u, v)
    s = sp.Function('s')(u, v)
    A = sp.Function('A')(v)
    Bu = sp.Function('B')(u)
    Bv = sp.Function('B')(u, v)
    Ru, Rv = sp.diff(R, u), sp.diff(R, v)
    F = -(sp.exp(2 * s) + 2 * Ru * Rv) / R                                      # R_uv (evolution)
    G = 3 * (sp.exp(2 * s) + 2 * Ru * Rv) / (2 * R**2)                          # s_uv
    mu = R**2 * (1 + 2 * sp.exp(-2 * s) * Ru * Rv)

    def onshell(e, B):
        Ruu = 2 * sp.diff(s, u) * Ru - B / (3 * R**2)                            # C_u = 0
        Rvv = 2 * sp.diff(s, v) * Rv - A / (3 * R**2)                            # C_v = 0
        rep = [(sp.Derivative(R, (u, 2), v), sp.diff(Ruu, v)), (sp.Derivative(R, u, (v, 2)), sp.diff(Rvv, u))]
        for _ in range(3):
            e = e.subs(rep).subs({sp.Derivative(R, u, v): F, sp.Derivative(s, u, v): G,
                                  sp.Derivative(R, (u, 2)): Ruu, sp.Derivative(R, (v, 2)): Rvv})
        return sp.simplify(e)

    ev = lambda e: sp.simplify(e.subs({sp.Derivative(R, u, v): F, sp.Derivative(s, u, v): G}))
    x1 = (ev(sp.diff(R**3, u, v) + 3 * R * sp.exp(2 * s)) == 0
          and sp.simplify(F + sp.exp(2 * s) * mu / R**3) == 0 and sp.simplify(G - sp.Rational(3, 2) * sp.exp(2 * s) * mu
                                                                              / R**4) == 0)
    x2 = onshell(sp.diff(mu, u, v), Bu) - sp.Rational(2, 9) * A * Bu * sp.exp(-2 * s) / R**2
    x2 = sp.simplify(x2) == 0
    ctl1 = ev(sp.diff(R**2, u, v) + 2 * sp.exp(2 * s)) != 0
    ctl2 = sp.simplify(onshell(sp.diff(mu, u, v), Bv) - sp.Rational(2, 9) * A * Bv * sp.exp(-2 * s) / R**2) != 0
    return x1, x2, ctl1 and ctl2


def corner(F):
    return F[0][None, :] + F[:, 0][:, None] - F[0, 0]


def cumint(f, du, dv):
    """int_0^u int_0^v f, trapezoidal, as an array on the grid"""
    g = np.concatenate([np.zeros((1, f.shape[1])), np.cumsum((f[1:] + f[:-1]) / 2 * du, axis=0)])
    return np.concatenate([np.zeros((g.shape[0], 1)), np.cumsum((g[:, 1:] + g[:, :-1]) / 2 * dv, axis=1)], axis=1)


def chain(n, A, B, U1):
    uu, vv, R, S = TD.solve(n, A, B, U1=U1)
    assert np.all(np.isfinite(R))
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2 * (1 + 2 * np.exp(-2 * S) * Ru * Rv)
    ident = np.max(np.abs(3 * cumint(R * np.exp(2 * S), du, dv) - (corner(R**3) - R**3)))
    a = float(R.min())
    Rmax = float(corner(R**3).max()) ** (1 / 3)
    m0 = float(corner(mu).min())
    Sb = -float(corner(S).min()) + 1.5 * max(0.0, -m0) / a**5 * Rmax**3 / 3
    AB = float(np.max(A(vv)[None, :] * B(uu)[:, None]))
    M = float(corner(mu).max()) + 2 / 9 * AB * math.exp(2 * Sb) * uu[-1] * vv[-1] / a**2
    smax = float(corner(S).max()) + 1.5 * max(M, 0.0) / a**5 * Rmax**3 / 3
    got = dict(Rmax=float(R.max()), mumin=float(mu.min()), mumax=float(mu.max()), smin=float(S.min()),
               smax=float(S.max()))
    bnd = dict(Rmax=Rmax, mumin=m0, mumax=M, smin=-Sb, smax=smax)
    ok = (got['Rmax'] <= bnd['Rmax'] + 1e-9 and got['mumin'] >= bnd['mumin'] - 1e-2 and got['mumax'] <= bnd['mumax']
          and got['smin'] >= bnd['smin'] - 1e-9 and got['smax'] <= bnd['smax'])
    return ident, a, got, bnd, ok


def main():
    ok = {}
    x1, x2, ctl = identities()
    ok['X1'], ok['X2'], ok['Ctl'] = x1, x2, ctl
    print('  X1: (R^3)_uv = -3 R e^(2s), R_uv = -e^(2s) mu/R^3, s_uv = (3/2) e^(2s) mu/R^4 on the evolution: %s' % x1)
    print('  X2: mu_uv = (2/9) A B e^(-2s)/R^2 with C_u, C_v: %s' % x2)
    print('  Ctl: (R^2)_uv keeps a cross term; B = B(u, v) leaves a residual in X2: %s' % ctl, flush=True)

    A = lambda x: TD.bump(x, 0.5, 2.0)
    Bw = lambda x: 0.4 * TD.bump(x, 1.0, 2.0)
    U1 = TD.corner_u(A, Bw)
    ids, x3 = [], True
    for n in (40, 80, 160, 320):
        ident, a, got, bnd, good = chain(n, A, Bw, U1)
        ids.append(ident)
        x3 &= good
        print('    n = %d (u in [0, %.3f], v in [0, 2], a = min R = %.3f): max |3 int int R e^(2s) - (D[R^3] - R^3)| = '
              '%.2e;  computed vs bound: max R %.3f <= %.3f, mu in [%.3f, %.3f] within [%.3f, %.3g], s in [%.3f, %.3f] '
              'within [%.3f, %.3g]' % (n, U1, a, ident, got['Rmax'], bnd['Rmax'], got['mumin'], got['mumax'],
                                       bnd['mumin'], bnd['mumax'], got['smin'], got['smax'], bnd['smin'], bnd['smax']),
              flush=True)
    rates = [ids[k] / ids[k + 1] for k in range(3)]
    x3 &= all(r > 1 for r in rates) and rates[-1] > 3
    ok['X3'] = x3
    print('  X3: identity (i)\'s residual falls with n (ratios %.2f, %.2f, %.2f: approaching second order; first order near R = '
          'a at coarse n, as D3 records), and every bound holds (mu\'s lower bound to the discretisation of '
          'R_u, R_v on the cones): %s' % (rates[0], rates[1], rates[2], x3))
    for k, val in ok.items():
        print(k, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
