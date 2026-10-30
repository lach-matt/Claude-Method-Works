#!/usr/bin/env python3
"""eq5.py -- the algebra behind EQUALITY5.md (the boundary and the horizon at mu0 = sqrt72 l5^2).  Labels: computed.

  E1 (computed) g0 of (2.3) in (v, r): -F dv^2 + 2 dv dr + r^2 (round), F = 1 - mu(v)/r^2; for Phi = r - rho(v),
     g0^{-1}(dPhi, dPhi) = F(rho) - 2 rho' on {r = rho}.  With rho = r_q := (sqrt72 mu l5^2)^(1/4) this is (3.1).
     Control: rho' with the factor 1 in place of 2 fails.
  E2 (computed) At mu0 = sqrt72 l5^2: -g0^{-1}(dPhi0, dPhi0) = sqrt(mu/mu0) - 1 + r_q mu'/(2 mu) =: m0, and 2 r_q' =
     r_q mu'/(2 mu).  Control: the exponent 1/2 in r_q fails.
  E3 (computed) For rho = r_q + sigma, sigma >= 0: mu (1/r_q^2 - 1/rho^2) <= 2 mu sigma / r_q^3, the gap being
     mu sigma^2 (3 r_q + 2 sigma) / (r_q^3 rho^2); and 2 mu / r_q^3 = 2 mu^(1/4) / mu0^(3/4) at equality.
  E4 (computed) On the future cone of g0 in (v, r, angles): dv(X) >= 0 and dr(X) <= (F/2) dv(X), checked on 20000
     future causal X (rejection sampling, g0(X, X) <= 0 and dtau(X) > 0) at random (r, mu), F of both signs; the bound
     is attained on the outgoing null direction.
     Control: dr(X) <= (F/4) dv(X) fails.
  E5 (computed) The margins of Proposition E.4 with c = 2 C_Phi and kappa sigma <= c lam on the layer: in the layer
     g^{-1}(dPhi_sigma, dPhi_sigma) <= -m0 - C_Phi lam < 0 for every m0 >= 0, and after the layer <= -delta/2 once
     lam <= delta/(6 C_Phi); symbolic in (m0, C_Phi, lam) >= 0.  Control: c = C_Phi leaves -m0, not uniformly negative.
"""
import sys
import random
import sympy as sp


def e1_e2():
    v, r, l5, mu0 = sp.symbols('v r l5 mu0', positive=True)
    mu = sp.Function('mu')(v); rho = sp.Function('rho')(v)
    F = 1 - mu / r**2
    # (2.3): eta + (mu/r^2) dv^2 with eta = -dtau^2 + dr^2, v = tau + r: in (v, r) the 2x2 block
    tau_v, tau_r = 1, -1                                   # dtau = dv - dr
    eta = sp.Matrix([[-tau_v**2, -tau_v * tau_r], [-tau_v * tau_r, 1 - tau_r**2]])
    g = eta + sp.Matrix([[mu / r**2, 0], [0, 0]])
    ok_form = sp.simplify(g - sp.Matrix([[-F, 1], [1, 0]])) == sp.zeros(2)
    gi = g.inv()
    dPhi = sp.Matrix([-sp.diff(rho, v), 1])
    val = sp.simplify((dPhi.T * gi * dPhi)[0])
    r1 = ok_form and sp.simplify(val - (F - 2 * sp.diff(rho, v))) == 0
    c1 = sp.simplify(val - (F - sp.diff(rho, v))) == 0
    rq = (sp.sqrt(72) * mu * l5**2)**sp.Rational(1, 4)
    on = sp.simplify(val.subs(rho, rq).doit().subs(r, rq))
    eq31 = 1 - sp.sqrt(mu / (sp.sqrt(72) * l5**2)) - rq * sp.diff(mu, v) / (2 * mu)
    r1 = r1 and sp.simplify(on - eq31) == 0
    # E2 at equality: sqrt72 l5^2 = mu0
    sub = {l5: sp.sqrt(mu0 / sp.sqrt(72))}
    m0 = sp.sqrt(mu / mu0) - 1 + rq.subs(sub) * sp.diff(mu, v) / (2 * mu)
    r2 = sp.simplify(sp.expand(-on.subs(sub) - m0)) == 0
    r2 = r2 and sp.simplify(2 * sp.diff(rq, v) - rq * sp.diff(mu, v) / (2 * mu)) == 0
    rq_bad = (sp.sqrt(72) * mu * l5**2)**sp.Rational(1, 2)
    on_bad = sp.simplify(val.subs(rho, rq_bad).doit().subs(r, rq_bad))
    c2 = sp.simplify(sp.expand(-on_bad.subs(sub) - m0)) == 0
    return r1, c1, r2, c2


def e3():
    rq, s, mu, mu0 = sp.symbols('r_q sigma mu mu0', positive=True)
    rho = rq + s
    gap = sp.together(2 * mu * s / rq**3 - mu * (1 / rq**2 - 1 / rho**2))
    r3 = sp.simplify(gap - mu * s**2 * (3 * rq + 2 * s) / (rq**3 * rho**2)) == 0
    kap = sp.simplify((2 * mu / rq**3).subs(rq, (mu0 * mu)**sp.Rational(1, 4)) - 2 * mu**sp.Rational(1, 4)
                      / mu0**sp.Rational(3, 4))
    return r3 and kap == 0


def e4(n=200000, seed=7):
    """rejection sampling: X with g0(X, X) <= 0 and dtau(X) = X^v - X^r > 0 (future causal), at random (r, mu)"""
    rng = random.Random(seed)
    kept, bad_v, worst, worst_c = 0, 0, -1e9, -1e9
    for _ in range(n):
        r = rng.uniform(0.3, 3.0); mu = rng.uniform(0.2, 4.0); F = 1 - mu / r**2
        Xv, Xr, a2 = rng.uniform(-2, 2), rng.uniform(-2, 2), rng.uniform(0, 0.05)
        if -F * Xv**2 + 2 * Xv * Xr + r**2 * a2 > 0 or Xv - Xr <= 0:
            continue
        kept += 1
        bad_v += Xv < 0
        worst = max(worst, Xr - F / 2 * Xv)
        if F > 0:
            worst_c = max(worst_c, Xr - F / 4 * Xv)
    # attained: the outgoing null direction X = d_v + (F/2) d_r is null, future, with equality
    r_, mu_ = 1.3, 0.7; F_ = 1 - mu_ / r_**2
    att = abs(-F_ + 2 * (F_ / 2)) < 1e-15 and 1 - F_ / 2 > 0
    return kept > 20000 and bad_v == 0 and worst <= 1e-12 and att, worst_c > 1e-3


def e5():
    m0, C, lam, dl = sp.symbols('m0 C_Phi lam delta', nonnegative=True)
    c = 2 * C
    layer = -m0 + c * lam - 2 * c * lam + C * lam             # kappa sigma <= c lam, sigma' = c lam, perturbation C lam
    r5a = sp.simplify(layer - (-m0 - C * lam)) == 0
    after = -dl + c * lam + C * lam                            # sigma' = 0, kappa sigma <= c lam
    r5b = sp.simplify(after.subs(lam, dl / (6 * C)) + dl / 2) == 0
    layer_c = sp.simplify(-m0 + C * lam - 2 * C * lam + C * lam)
    c5 = layer_c == -m0
    return r5a and r5b, c5


def main():
    r1, c1, r2, c2 = e1_e2()
    print('E1 g0^-1(dPhi, dPhi) = F(rho) - 2 rho\', and (3.1):', 'PASS' if r1 else 'FAIL', '| control factor 1:', c1)
    print('E2 the margin at equality:', 'PASS' if r2 else 'FAIL', '| control exponent 1/2:', c2)
    r3 = e3()
    print('E3 mu(1/r_q^2 - 1/rho^2) <= 2 mu sigma/r_q^3; kappa at equality:', 'PASS' if r3 else 'FAIL')
    r4, c4 = e4()
    print('E4 dv(X) >= 0, dr(X) <= (F/2) dv(X) on the future cone:', 'PASS' if r4 else 'FAIL', '| control F/4 fails:',
          c4)
    r5, c5 = e5()
    print('E5 the margins of Proposition E.4 with c = 2 C_Phi:', 'PASS' if r5 else 'FAIL',
          '| control c = C_Phi leaves -m0:', c5)
    ok = r1 and not c1 and r2 and not c2 and r3 and r4 and c4 and r5 and c5
    print('eq5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
