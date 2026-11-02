#!/usr/bin/env python3
"""eqlayer5.py -- the equality layer's vanishing to every order (verifier 259's item 1, D605; supplement EQUALITY5.md
Lemma E.1 (c), Proposition E.2, Remark E.6).

At mu0 = sqrt72 l5^2 the margin of x_K = 1 is (EQUALITY5.md (0.2)) m0(v) = sqrt(mu/mu0) - 1 + r_q mu'/(2 mu), with
r_q = (sqrt72 mu l5^2)^(1/4) = (mu0 mu)^(1/4) and mu(v) = mu0 + (2/9) A^2 int_(v_s)^v env^2. Lemma E.1 (c) says m0 and
all its derivatives vanish at v_s := inf supp env; Remark E.6 says the expansion does not decide the sign of g_lam^-1
(dPhi0, dPhi0) in the layer v_s < v < v_s + eta_lam, because the profiles of g_app are not shown to have (Phi0#, Phi0#)
components bounded by C (env^2 + int env^2) near v_s (the higher profiles contain derivatives of env, which near v_s are
not so bounded). Here x = v - v_s and env = exp(-1/x) near x = 0+, the standard flat edge of
a C^inf_c envelope (any C^inf_c envelope vanishing on (-inf, v_s) is flat there; this one makes it explicit).

  L1 (exact) m0 > 0 for x > 0, and m0 = o(x^k) for every k = 0, ..., 12: with int_0^x env^2 <= x env^2 (the integrand
     increases), m0 <= (x + mu0^(1/2)) (A^2/9) env^2/mu0, and the limits x^-k times that bound -> 0 are computed; m0 >=
     (A^2/9) mu0^(1/4) mu_up^(-3/4) env^2 (the second term alone), so m0/env^2 has a positive lower bound: the order-lam
     term lam chi ~ lam A^2 env^2 is a fraction of m0 (Remark E.6's heuristic).
  L2 (exact) env'/(env^2 + x env^2) and env''/(env^2 + x env^2) tend to +infinity as x -> 0+, hence so do the ratios
     to env^2 + int env^2 <= env^2 + x env^2: env's derivatives are not bounded by the margin's order there (Remark
     E.6's parenthesis, checked for env itself).
  Controls: L1, an envelope with a finite-order edge, env = x^4: L1's upper bound up ~ c x^8, so up/x^9 -> infinity
     for the envelope tested and L1's criterion (up/x^k -> 0) rejects it; L2, an envelope with no edge, env = 1 + x:
     env'/(env^2 + x env^2) -> 1 and env'' = 0, so L2's criterion (both -> infinity) must reject it.

Labels: computed (exact, sympy limits). Reach: the sign of g_lam^-1(dPhi0, dPhi0) in the layer is not computed. L2
does not show that the (Phi0#, Phi0#) profiles carry env' (EQUALITY5.md Remark E.6: "not shown"); it shows only that,
if they do, the margin's order does not bound them.

Run: python3 checks/eqlayer5.py   (a few seconds)
"""
import sys

import sympy as sp

x, A, mu0 = sp.symbols("x A mu0", positive=True)


def margin_bound(env):
    """(upper, lower) bounds of m0: mu0 <= mu <= mu_up := mu0 + (2/9) A^2 x env^2 (int_0^x env^2 <= x env^2, the
    integrand increasing near 0), sqrt(mu/mu0) - 1 <= (mu - mu0)/(2 mu0), and r_q/mu = mu0^(1/4) mu^(-3/4) between
    mu0^(1/4) mu_up^(-3/4) and mu0^(-1/2)"""
    dmu = sp.Rational(2, 9)*A**2*env**2
    mu_up = mu0 + x*dmu
    up = x*dmu/(2*mu0) + mu0**sp.Rational(-1, 2)*dmu/2
    low = mu0**sp.Rational(1, 4)*mu_up**sp.Rational(-3, 4)*dmu/2
    return up, low


def l1(control=False):
    env = x**4 if control else sp.exp(-1/x)
    up, low = margin_bound(env)
    vals = {A: 1, mu0: 7}
    orders = range(0, 13) if not control else [9]
    flat = all(sp.limit((up/x**k).subs(vals), x, 0, "+") == 0 for k in orders)
    if control:
        return flat
    ratio = sp.limit((low/env**2).subs(vals), x, 0, "+")
    pos = sp.simplify(low.subs(vals).subs(x, sp.Rational(1, 3))) > 0          # low > 0 implies m0 > 0
    print("  L1: x^-k m0 -> 0 for k = 0..12 (env = exp(-1/x)): %s; lower bound of m0 > 0 at x = 1/3: %s; m0/env^2 >= %s"
          " > 0 as x -> 0+ (A = 1, mu0 = 7)" % (flat, pos, ratio), flush=True)
    return flat and pos and ratio > 0


def l2(control=False):
    env = 1 + x if control else sp.exp(-1/x)
    scale = env**2 + x*env**2
    d1 = sp.limit(sp.diff(env, x)/scale, x, 0, "+")
    d2 = sp.limit(sp.diff(env, x, 2)/scale, x, 0, "+")
    print("  L2%s: env'/(env^2 + x env^2) -> %s and env''/(env^2 + x env^2) -> %s as x -> 0+"
          % (" control (env = 1 + x)" if control else "", d1, d2), flush=True)
    return d1 == sp.oo and d2 == sp.oo


CHECKS = [("L1", l1), ("L2", l2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
