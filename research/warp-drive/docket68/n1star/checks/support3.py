#!/usr/bin/env python3
"""support3.py -- computations behind four deduced steps of the paper's sections 2.5-3 (RESPONSE-HL-5D.md).

  D1 (exact) section 3, Proposition 3.3's proof: "sqrt(mu(v)) - r_q(v) = mu^(1/4)(mu^(1/4) - (sqrt72 l5^2)^(1/4)) >= its
     value at mu0 > 0", with r_q := (sqrt72 mu l5^2)^(1/4) (paper (2.3)). The identity holds exactly; the derivative of
     f(mu) = sqrt(mu) - r_q in mu is mu^(-3/4) (2 mu^(1/4) - c^(1/4))/4, c := sqrt72 l5^2, positive exactly when
     mu > c/16 -- so f is increasing on mu >= c/16, which contains mu >= mu0 >= c (the seed condition), not on all of
     mu > 0 (it decreases on (0, c/16)); with mu nondecreasing, f(mu(v)) >= f(mu0), and f(mu0) > 0 iff mu0 > c.
     Control: r_q with exponent 1/2 in place of 1/4 does not satisfy the identity.
  D2 (exact; computed, floating point) section 3, Theorem 1 item 4: "dg_lam -> dg0 weakly in L^2(Omega), and not
     strongly wherever env != 0", dg_lam - dg0 = dv (x) [d_s g1] + O(lam). With lead5.py's stage-0 profile g1 = W_TT
     + chi dv dv (phase s = v/lam; chi any 2pi-periodic function, its oscillating part the second harmonic of lead5
     L4), exactly: the phase mean <d_s g1> over s in [0, 2pi] is 0 in every component, and <|d_s g1|^2>, the g0-norm
     g0^ac g0^bd d_s W_ab d_s W_cd (chi drops out: g0^vv = 0), is A^2 E^2 H^2 r^-3 (4/3)(c^4 + s^4), which is
     (4/3) A^2 E^2 r^-3 with the record's H: > 0 wherever env = E != 0. Floating point: for a smooth psi on a
     v-interval [a, b] of the shell (psi = 1 + v, env a C_c^inf bump), I(lam) = int_a^b psi(v) [d_s W_p1p1](v,
     v/lam) dv at lam = a/(2 pi n), n = 4, 8, 16 (a/lam, b/lam multiples of 2 pi): the rate
     log2(I(lam)/I(lam/2)) is ~1 (O(lam), from the endpoint terms; for psi env vanishing to all orders at a and b it
     would be O(lam^inf)), while int_a^b [d_s W_p1p1]^2 dv tends to int <(d_s W_p1p1)^2>, not to 0.
     Control: env = 0 gives <|d_s g1|^2> = 0, so the 'not strongly' criterion fails.
  D3 (exact) sections 2.5 and 3: "symmetry follows from uniqueness, since Ric^H and D are built from g and the
     O(4)-invariant g0". On S^3 with x1 + i x2 = cos th e^(i phi1), x3 + i x4 = sin th e^(i phi2) (lead5's coordinates,
     round metric dth^2 + c^2 dphi1^2 + s^2 dphi2^2), the six so(4) generators x_a d_b - x_b d_a, pulled back, are
     linearly independent and Killing for lead5's g0 (L_X g0 = 0 in (v, r, th, phi1, phi2), M(v) arbitrary); the
     reflections phi1 -> -phi1, phi2 -> -phi2 (paper 2.1, "both reflections of its orbits") pull g0 back to itself;
     and lead5's stage-0 approximant g0 + lam W (W = W_TT + chi dv dv) is invariant under the T^2 rotations d_phi1,
     d_phi2 and both reflections (it is not invariant under all of so(4), printed: the class is T^2-mirror, not O(4)).
     Reused: past5.py P6 (the rotation x1 d_2 - x2 d_1 commutes with L0 and box~) and mass5.py M4 (sigma is an
     isometry of g0). Control: the conformal (boost-like) field grad(x1) of S^3 is not Killing.
  D4 (exact, a ledger) section 3: "the data are solved in H^s(S^3) with s > 3/2 + 4" (supplement Proposition 6.5:
     s0 > 3/2 + 4, s := s0 + 2; Lemma 6.4: s > 3/2 + 2). Rule: on S^3 (dim 3), H^t c C^k iff t > 3/2 + k. Rows, at
     the contraction's index s0: Lemma 6.4 at s0 and at s; the frozen coefficients' two derivatives of gamma (of a)
     in L^inf, and two more for the difference estimate (C^4); K's one derivative (of (w, q)), plus two (C^3); and
     Theorem E's k + 1 = 7 derivatives of the data, at the integer s. The binding row is C^4, its threshold 3/2 + 4
     is the stated one, and the least admissible integer (and half-integer) is s0 = 6, s = 8. The ledger is this
     program's reading of the derivative counts the proof names; the supplement states the threshold, not the
     ledger. Control: s0 = 3/2 + 3 fails the C^4 row.

Labels: computed (exact, sympy) for D1, D3, D4 and D2's phase means; computed (floating point, numpy) for D2's rates.
Run: python3 checks/support3.py   (about 100 seconds)
"""
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)


def d1(control=False):
    mu, l5, mu0 = sp.symbols("mu l5 mu0", positive=True)
    c = sp.sqrt(72)*l5**2
    rq = (c*mu)**(sp.Rational(1, 2) if control else sp.Rational(1, 4))
    f = sp.sqrt(mu) - rq
    rhs = mu**sp.Rational(1, 4)*(mu**sp.Rational(1, 4) - c**sp.Rational(1, 4))
    ident = sp.simplify(sp.expand_power_base(f - rhs, force=True)) == 0
    if control:
        return ident
    df = sp.diff(f, mu)
    form = mu**sp.Rational(-3, 4)*(2*mu**sp.Rational(1, 4) - c**sp.Rational(1, 4))/4
    dform = sp.simplify(sp.expand_power_base(df - form, force=True)) == 0
    # sign of df: positive iff mu^(1/4) > c^(1/4)/2 iff mu > c/16; check at mu = c/16 (zero), below and above
    t = sp.symbols("t", positive=True)                                 # mu = t c
    dft = sp.simplify(sp.expand_power_base((df*mu**sp.Rational(3, 4)).subs(mu, t*c), force=True))
    crit = sp.solve(sp.Eq(dft, 0), t)
    below = sp.simplify(dft.subs(t, sp.Rational(1, 32))) < 0
    above = all(sp.simplify(dft.subs(t, q)) > 0 for q in (sp.Rational(1, 15), 1, 7))
    seed_in = 1 > sp.Rational(1, 16)                                    # mu >= mu0 >= c lies in mu > c/16
    f0 = rhs.subs(mu, mu0)
    pos = sp.simplify(sp.expand_power_base(f0.subs(mu0, t*c), force=True))
    pos_iff = (sp.solve(sp.Eq(pos, 0), t) == [1] and sp.simplify(pos.subs(t, 2)) > 0
               and sp.simplify(pos.subs(t, sp.Rational(1, 2))) < 0)
    print("  D1: sqrt(mu) - r_q = mu^(1/4)(mu^(1/4) - c^(1/4)), c = sqrt72 l5^2: %s; d/dmu = mu^(-3/4)(2 mu^(1/4) -\n"
          "      c^(1/4))/4: %s; zero at mu/c = %s, negative below (mu = c/32: %s), positive above: %s -- increasing\n"
          "      on mu > c/16 only, which contains mu >= mu0 >= c: %s; f(mu0) > 0 iff mu0 > c: %s"
          % (ident, dform, crit, below, above, seed_in, pos_iff), flush=True)
    return ident and dform and crit == [sp.Rational(1, 16)] and below and above and seed_in and pos_iff


def d2(control=False):
    import lead5 as L
    s, A, r, th, v = L.s, L.A, L.r, L.th, L.v
    W = L.wave(with_chi=False)
    chi = sum(sp.Function("c%d" % k)(v, r, th)*sp.cos(k*s) + sp.Function("d%d" % k)(v, r, th)*sp.sin(k*s)
              for k in (1, 2)) + sp.Function("c0")(v, r, th)
    W[0, 0] = chi
    if control:
        W = W.subs(L.Ef, 0)
    g0, g0i = L.background()
    dW = W.diff(s)
    mean = lambda e: sp.integrate(sp.expand(e), (s, 0, 2*sp.pi))/(2*sp.pi)
    mean0 = all(sp.simplify(mean(dW[a, b])) == 0 for a in range(5) for b in range(5))
    nrm = sp.expand(sum(g0i[a, c]*g0i[b, d]*dW[a, b]*dW[c, d]
                        for a in range(5) for b in range(5) for c in range(5) for d in range(5)))
    msq = sp.simplify(mean(nrm))
    if control:
        return sp.simplify(msq) != 0                                    # 'not strongly' needs <|d_s g1|^2> > 0
    ang = sp.simplify(sp.trigsimp(msq/(A**2*L.Ef**2*L.Hf**2*r**-3)))
    free = not ang.has(A, L.Ef, L.Hf, r, v, s)
    tt = sp.symbols("tt")
    angf = sp.lambdify(tt, ang.subs(th, tt))
    pos = free and min(angf(x_) for x_ in np.linspace(0, np.pi/2, 401)) > 0
    # floating point: I(lam) = int_a^b psi(v) [d_s W_p1p1](v, v/lam) dv at r = 2, th = 0.6, H = record's H
    env = lambda x_: np.where((x_ > 0) & (x_ < 1), np.exp(-1/np.clip(x_*(1 - x_), 1e-300, None)), 0.0)
    comp = dW[3, 3].subs({L.Hf: L.H_REC, A: 1}).subs({r: 2, th: sp.Rational(3, 5)})
    e_, ss = sp.symbols("e_ ss")
    fc = sp.lambdify((e_, ss), comp.subs(L.Ef, e_).subs(s, ss), "numpy")
    a_, b_ = 0.25, 0.75
    vv = np.linspace(a_, b_, 400001)
    psi = 1 + vv

    def simpson(y):
        h = (vv[-1] - vv[0])/(len(vv) - 1)
        return h/3*(y[0] + y[-1] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum())
    lams = [a_/(2*math.pi*n) for n in (4, 8, 16)]                     # a/lam and b/lam multiples of 2 pi
    I = [simpson(psi*fc(env(vv), vv/lm)) for lm in lams]
    rates = [math.log2(abs(I[i]/I[i + 1])) for i in range(2)]
    sq = [simpson(fc(env(vv), vv/lm)**2) for lm in lams]
    sqmean = simpson(env(vv)**2)*float(sp.N(mean(sp.expand(comp**2/L.Ef**2)).subs(s, 0)))
    weak = all(0.8 < q < 1.2 for q in rates) and abs(I[-1]) < 1e-2*math.sqrt(sq[-1])
    strong_not = all(abs(q/sqmean - 1) < 1e-2 for q in sq) and sqmean > 0
    print("  D2: <d_s g1> = 0 in every component (chi any periodic): %s; <|d_s g1|^2>_g0 = A^2 E^2 H^2 r^-3 *\n"
          "      (%s), the factor positive on [0, pi/2]: %s;\n"
          "      I(lam) at lam = %s: %s, rates %s;\n      int [d_s W_p1p1]^2 dv = %s -> int <.> = %.6g (not 0): %s"
          % (mean0, ang, pos, ", ".join("%.4g" % q for q in lams), ", ".join("%.3e" % q for q in I),
             ", ".join("%.3f" % q for q in rates), ", ".join("%.6g" % q for q in sq), sqmean, strong_not),
          flush=True)
    return mean0 and pos and weak and strong_not


def d3(control=False):
    import lead5 as L
    import mass5
    import past5
    X, th, p1, p2, lam = L.X, L.th, L.p1, L.p2, L.lam
    c, s_ = sp.cos(th), sp.sin(th)
    g0, _ = L.background()

    def lie(Xv, g):
        n = 5
        return sp.Matrix(n, n, lambda a, b: sp.simplify(
            sum(Xv[k]*sp.diff(g[a, b], X[k]) + g[k, b]*sp.diff(Xv[k], X[a]) + g[a, k]*sp.diff(Xv[k], X[b])
                for k in range(n))))
    emb = [c*sp.cos(p1), c*sp.sin(p1), s_*sp.cos(p2), s_*sp.sin(p2)]
    J = sp.Matrix(4, 3, lambda i, j: sp.diff(emb[i], (th, p1, p2)[j]))
    JtJi = sp.diag(1, 1/c**2, 1/s_**2)
    gens = []
    for a in range(4):
        for b in range(a + 1, 4):
            Kv = sp.zeros(4, 1)
            Kv[b], Kv[a] = emb[a], -emb[b]                       # x_a d_b - x_b d_a
            comp = (JtJi*J.T*Kv).applyfunc(sp.simplify)
            gens.append([0, 0] + list(comp))
    if control:
        x1 = emb[0]                                              # grad_S3(x1), conformal, not Killing
        Xc = [0, 0, sp.diff(x1, th), sp.diff(x1, p1)/c**2, sp.diff(x1, p2)/s_**2]
        return lie(Xc, g0) == sp.zeros(5)
    killing = all(lie(G, g0) == sp.zeros(5) for G in gens)
    pts = [{th: sp.Rational(1, 3), p1: sp.Rational(1, 2), p2: sp.Rational(2, 7)},
           {th: sp.Rational(4, 5), p1: sp.Rational(3, 2), p2: sp.Rational(1, 9)},
           {th: sp.Rational(6, 7), p1: sp.Rational(-1, 3), p2: sp.Rational(5, 4)}]
    Mx = sp.Matrix([[sp.N(G[k].subs(q), 30) for q in pts for k in (2, 3, 4)] for G in gens])
    indep = Mx.rank(iszerofunc=lambda e: abs(e) < 1e-20) == 6

    def pull(Fm, g):                                             # (F*g)_ab = g_cd(F(x)) dF^c_a dF^d_b, F linear
        Jf = sp.Matrix(5, 5, lambda i, j: sp.diff(Fm[i], X[j]))
        return (Jf.T*g.subs(dict(zip(X, Fm)), simultaneous=True)*Jf).applyfunc(sp.simplify)
    refl = [[X[0], X[1], th, -p1, p2], [X[0], X[1], th, p1, -p2]]
    same = lambda P, Q: (P - Q).applyfunc(sp.simplify) == sp.zeros(5)
    refl_g0 = all(same(pull(F, g0), g0) for F in refl)
    W = L.wave(with_chi=True)
    gl = g0 + lam*W
    gl_phi = lie([0, 0, 0, 1, 0], gl) == sp.zeros(5) and lie([0, 0, 0, 0, 1], gl) == sp.zeros(5)
    gl_refl = all(same(pull(F, gl), gl) for F in refl)
    notO4 = sum(lie(G, W) != sp.zeros(5) for G in gens)
    p6 = past5.p6(0) and not past5.p6(1)
    m4 = mass5.m4() and not mass5.m4(control=True)
    print("  D3: the six so(4) generators are Killing for g0: %s, independent: %s; both reflections pull g0 back to\n"
          "      itself: %s; g0 + lam W is d_phi1-, d_phi2-invariant: %s, reflection-invariant: %s; W not invariant\n"
          "      under %d of the 6 (T^2-mirror, not O(4)); past5 P6 (with control): %s; mass5 M4 (with control): %s"
          % (killing, indep, refl_g0, gl_phi, gl_refl, notO4, p6, m4), flush=True)
    return killing and indep and refl_g0 and gl_phi and gl_refl and p6 and m4


def d4(control=False):
    half = Fr(3, 2)                                              # dim S^3 / 2
    emb = lambda t, k: t > half + k                              # H^t(S^3) c C^k
    stated_s0 = half + 4

    def rows(s0):
        s = s0 + 2
        return [("Lemma 6.4 at index s0: s0 > 3/2 + 2", s0 > half + 2, half + 2),
                ("Lemma 6.4 at index s = s0 + 2: s > 3/2 + 2", s > half + 2, half),
                ("frozen coefficients: 2 derivatives of gamma (a in H^s0) + 2 for the difference: C^4", emb(s0, 4),
                 half + 4),
                ("K's 1 derivative ((w, q) in H^s0) + 2 for the difference: C^3", emb(s0, 3), half + 3),
                ("Theorem E: k + 1 = 7 derivatives of the data at the integer s", math.floor(s) >= 7, Fr(9, 2))]
    if control:
        return all(ok for _, ok, _ in rows(half + 3))
    s0_test = Fr(6)
    rs = rows(s0_test)
    binding = max(t for _, _, t in rs)
    cands = [Fr(k, 2) for k in range(0, 40)]
    least = min(q for q in cands if all(ok for _, ok, _ in rows(q)))
    least_int = min(q for q in cands if q.denominator == 1 and all(ok for _, ok, _ in rows(q)))
    print("  D4: the Sobolev ledger (H^t(S^3) c C^k iff t > 3/2 + k), at s0 = %s, s = %s:" % (s0_test, s0_test + 2),
          flush=True)
    for name, ok, t in rs:
        print("      %-96s s0 > %-5s %s" % (name, t, ok), flush=True)
    print("      binding threshold s0 > %s = stated 3/2 + 4: %s; least admissible half-integer s0 = %s, integer %s,\n"
          "      s = s0 + 2 = %s" % (binding, binding == stated_s0, least, least_int, least_int + 2), flush=True)
    return all(ok for _, ok, _ in rs) and binding == stated_s0 and least == least_int == 6


CHECKS = [("D1", d1), ("D2", d2), ("D3", d3), ("D4", d4)]


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
