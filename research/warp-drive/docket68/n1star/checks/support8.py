#!/usr/bin/env python3
"""support8.py -- computations behind deduced steps of the paper's section 8 (verifier 258's list, D600).

  K8 (exact, sympy) section 8.1: the class of [Hol08] (SU(2) x U(1)-invariant) and this paper's T^2-mirror class (2.1)
     meet only in spherical symmetry. On S^3 with c = cos th, s = sin th, the round metric is the sum of the base part
     (sigma1^2 + sigma2^2)/4 = dth^2 + c^2 s^2 (dphi1 - dphi2)^2 and the fibre part eta^2, eta = c^2 dphi1 + s^2 dphi2
     (computed: the two add to dth^2 + c^2 dphi1^2 + s^2 dphi2^2). [Hol08]'s squashed sphere e^(2B) (base) + e^(-4B)
     eta^2 has dphi1 dphi2 coefficient 2 c^2 s^2 (e^(-4B) - e^(2B)), zero for c s != 0 exactly when B = 0, where the
     sphere is round; the class (2.1) has no dphi1 dphi2 term. Control: e^(2B) in place of e^(-4B) on the fibre (no
     squashing) makes the coefficient vanish for every B.
  K1 (exact) section 8.1's 'after the shell the oscillating profiles vanish' (supplement 10.50(a), by induction): its
     base and first step on the profiles the programs compute. Every oscillating profile of ansatz5.py (the waves a1,
     a2 and the second-order terms bc, bs, kc, ks) and lead5.py's leading wave W_TT carries the envelope: each vanishes
     identically where E = 0 (so on v > v_end), and the source of chi's transport (lead5 L3's vv second harmonic) is
     quadratic in E, so chi = 0 solves it there with zero data. Control: a profile with an E-free term added.

Run: python3 checks/support8.py
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def k8(control=False):
    th, ph1, ph2, B = sp.symbols("theta phi1 phi2 B", real=True)
    c, s = sp.cos(th), sp.sin(th)
    d = sp.symbols("dth dph1 dph2")                                  # the coordinate differentials, as symbols

    def quad(form):
        return sp.expand(form)
    base = quad(d[0]**2 + c**2 * s**2 * (d[1] - d[2])**2)
    eta = c**2 * d[1] + s**2 * d[2]
    roundm = quad(d[0]**2 + c**2 * d[1]**2 + s**2 * d[2]**2)
    split = sp.simplify(base + quad(eta**2) - roundm) == 0
    fibre = sp.exp(2 * B) if control else sp.exp(-4 * B)
    g = quad(sp.exp(2 * B) * base + fibre * eta**2)
    cross = sp.simplify(g.coeff(d[1]).coeff(d[2]))
    want = 2 * c**2 * s**2 * (sp.exp(-4 * B) - sp.exp(2 * B))
    exact = sp.simplify(cross - want) == 0
    only_round = sp.solve(sp.Eq(sp.exp(-4 * B) - sp.exp(2 * B), 0), B) == [0]
    if control:
        return sp.simplify(cross) != 0                                 # must fail: no squashing, no cross term
    print("  K8: base + fibre = round: %s; [Hol08]'s squashed sphere's dphi1 dphi2 coefficient 2 c^2 s^2 (e^(-4B) -\n"
          "      e^(2B)): %s; zero only at B = 0 (round): %s" % (split, exact, only_round), flush=True)
    return split and exact and only_round


def k1(control=False):
    sys.path.insert(0, HERE)
    import ansatz5 as a5
    import lead5 as L
    a1_, a2_ = a5._waves()
    prof = [a1_, a2_] + list(a5.g2_terms())
    if control:
        prof[0] = prof[0] + a5.A * a5.Hf * sp.cos(a5.s)               # an E-free part
    vanish = all(sp.simplify(q.subs(a5.Ef, 0).doit()) == 0 for q in prof)
    W = L.wave(with_chi=False)
    wt = all(sp.simplify(e.subs(L.Ef, 0).doit()) == 0 for e in W)
    if control:
        return vanish
    R0 = L.reduced_ricci(W)[(0, 0)][1]
    e_ = sp.Symbol("e_")
    harm = L.modes(R0)[2]                                             # the source: vv's second harmonic (lead5 L3)
    quad_ok = True
    for part in harm:
        src = sp.expand(sp.sympify(part).subs(L.Ef, e_).doit())
        if src == 0:
            continue
        mons = sp.Poly(src, e_).monoms()
        quad_ok &= all(m_[0] >= 2 for m_ in mons)
    print("  K1: every oscillating profile of ansatz5 vanishes where E = 0: %s; lead5's W_TT too: %s; chi's transport\n"
          "      source (R^(0)_vv's second harmonic, chi = 0) has E-degree >= 2 in every term, so it vanishes there: %s"
          % (vanish, wt, quad_ok), flush=True)
    return vanish and wt and quad_ok


CHECKS = [("K1", k1), ("K8", k8)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", "" if not ctl else " (control passed)"),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
