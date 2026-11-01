#!/usr/bin/env python3
"""twophase5.py -- FAMILIES5 section 4f (D511): the record's section 5.2 with two families.

The record's section 5.2 (RESPONSE-HL-5D.md:490-511) writes the remainder as w = h + phi [d_theta g1], with
L0 phi = -(1/2) P s, and closes the estimate with three facts: Lemma 5.1 (the phase shift is a symmetry), [d_theta
g1](ell, .) = 0 (so contracting with ell x ell kills every lam^-1 term and the box~ phi term), and the commutator (2.4)
of box~ with L0 (so Psi := box~ phi obeys the transport (5.3)). With two families the decomposition is
w = h + phi_in [d_s1 G] + phi_out [d_s2 G], one transport along each family's own generator (section 4f). This
script computes what that needs of the background and of the waves.

  Q1 (exact, sympy) The commutator on the general round double-null background g0 = -2 e^(2 sigma) du dv + R^2 dOmega_3
     (sigma, R any functions of (u, v): the two-dust background of section 4c is of this form). For L_in := ell_in.d
     = -e^(-2 sigma) d_u and L_out := ell_out.d = -e^(-2 sigma) d_v and any function f,
         [box, L_k] f = a_k box f + (second derivatives of f each carrying the generator's own index) + (first order),
     with a_k = 2 L_k R / R (two-thirds of the expansion of ell_k), and no third derivative. A second derivative with
     the generator's index is a first-order operator applied to L_k f plus a first-order term, so
         box (L_k f) = L_k (box f) + a_k box f + M_k (L_k f) + N_k f,    M_k, N_k first order,
     which is the structure of the record's (2.4): Psi_k := box phi_k obeys a transport along ell_k whose source is
     box of L_k phi_k and first derivatives. The reason is that each generator is shear-free on a round background:
     d_v of the angular inverse metric is a multiple of itself.
     Control: an angular metric with shear, R^2 (e^(2 b) dth^2 + e^(-2 b)(cos^2 th dp1^2 + sin^2 th dp2^2)), b = b(u, v),
     leaves angular second derivatives that no multiple of box removes.
  Q2 (exact, stage0two5's waves) The contractions. [d_s1 g1_in](ell_in, .) = 0 and [d_s2 g1_out](ell_out, .) = 0 in
     every component (each family's own, as in the record); [d_s2 g1_out](ell_in, ell_in) = e^(-4 sigma) F2 chi' and
     [d_s1 g1_in](ell_out, ell_out) = e^(-4 sigma) F1 chi, through the second-harmonic gauge terms alone, so the
     coefficient of Psi_out in the s_in equation is -(1/2) e^(-4 sigma) F2 chi' (bounded, oscillating in s2), and
     likewise for the mirror term. With chi = chi' = 0 these vanish; the generalised wave gauge's phase-shift defect,
     -lam^-1 phi_k F_k^2 h_k k_k x k_k (k_in = dv, k_out = du; deduced in FAMILIES5 4f), is killed by ell_k x ell_k
     and enters the other family's contraction with (dv(ell_out))^2 = (du(ell_in))^2 = e^(-4 sigma), nonzero.
     Control: the record's single-family statement [d_theta g1](ell, .) = 0 is false for the other family's
     generator whenever chi' != 0.
Labels: computed (exact, sympy). About 5 s.

Measured (D512): Q1 holds for both generators, a_in = -2 e^(-2 sigma) R_u/R and a_out = -2 e^(-2 sigma) R_v/R; for
L_out the remaining second derivatives are d_u d_v f (coefficient -4 e^(-4 sigma) R_v/R) and d_v^2 f (-4 e^(-4 sigma)
sigma_u). The control leaves the three diagonal angular second derivatives. Q2 as stated.

    python3 checks/twophase5.py [--selftest]
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage0two5 as S0   # noqa: E402

u, v, th, p1, p2 = S0.u, S0.v, S0.th, S0.p1, S0.p2
X = [u, v, th, p1, p2]
sig, R = S0.sig, S0.Rf
C, S = sp.cos(th), sp.sin(th)
f = sp.Function("f")(*X)
bsh = sp.Function("b")(u, v)


def metric(shear=False):
    """the round double-null metric, or (shear=True) one whose angular part is sheared along both generators"""
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -sp.exp(2*sig)
    e = sp.exp(2*bsh) if shear else 1
    g[2, 2], g[3, 3], g[4, 4] = R**2*e, R**2*C**2/e, R**2*S**2/e
    return g


def box(g, q):
    gi = g.inv()
    sq = sp.exp(2*sig)*sp.sqrt(g[2, 2]*g[3, 3]*g[4, 4])
    sq = sp.simplify(sq)
    return sum(sp.diff(sq*gi[a, b]*sp.diff(q, X[b]), X[a]) for a in range(5) for b in range(5))/sq


def derivs(order):
    out = []
    for i in range(5):
        if order == 1:
            out.append(sp.diff(f, X[i]))
            continue
        for j in range(i, 5):
            if order == 2:
                out.append(((i, j), sp.diff(f, X[i], X[j])))
            else:
                for k in range(j, 5):
                    out.append(((i, j, k), sp.diff(f, X[i], X[j], X[k])))
    return out


def commutator(g, k):
    """[box, L_k] f, L_k = -e^(-2 sigma) d_(u or v): k = 0 for L_in (d_u), k = 1 for L_out (d_v)"""
    L = lambda q: -sp.exp(-2*sig)*sp.diff(q, X[k])            # noqa: E731
    return sp.expand(box(g, L(f)) - L(box(g, f))), L


def q1(g, k, verbose=True):
    """returns (ok, a): the second-order part of [box, L_k] - a box, with a = 2 L_k R / R, has only derivatives
    carrying index k; no third derivatives"""
    com, L = commutator(g, k)
    bx = sp.expand(box(g, f))
    a = sp.simplify(2*L(R)/R)
    rest = sp.expand(com - a*bx)
    third = [d for (_, d) in derivs(3) if sp.simplify(rest.coeff(d)) != 0]
    bad = []
    for (ij, d) in derivs(2):
        if k in ij:
            continue
        c = sp.simplify(rest.coeff(d))
        if c != 0:
            bad.append((ij, c))
    return (not third and not bad), a, bad, third


def main():
    t0 = time.time()
    ok = {}
    g = metric()
    names = {0: "L_in = -e^(-2 sigma) d_u", 1: "L_out = -e^(-2 sigma) d_v"}
    for k in (0, 1):
        good, a, bad, third = q1(g, k)
        ok["Q1 %s" % ("in" if k == 0 else "out")] = good
        print("  Q1 %s: [box, L] - a box has no third derivative and only second derivatives carrying the generator's "
              "index: %s; a = %s (%.0f s)" % (names[k], good, a, time.time() - t0), flush=True)
    # control: shear
    gs = metric(shear=True)
    good, a, bad, third = q1(gs, 1)
    ok["Q1 control"] = not good and len(bad) > 0
    print("  Q1 control (sheared angular metric, L_out): remaining angular second derivatives %s; removed by a box: %s"
          % ([ij for (ij, _) in bad], good), flush=True)
    # M_k and N_k for L_out, written out once (the second-derivative terms with a v index)
    com, L = commutator(g, 1)
    rest = sp.expand(com - sp.simplify(2*L(R)/R)*sp.expand(box(g, f)))
    mterms = {ij: sp.simplify(rest.coeff(d)) for (ij, d) in derivs(2) if 1 in ij and sp.simplify(rest.coeff(d)) != 0}
    print("  Q1 out: the second-derivative terms with a v index (they form M_out(L_out f) + first order):", flush=True)
    for ij, c in mterms.items():
        print("      d_%s d_%s f : %s" % (S0.NAMES[ij[0]], S0.NAMES[ij[1]], c), flush=True)

    # Q2: contractions with stage0two5's waves
    g0, g0i = S0.background()
    a_, b_ = S0.amplitudes()
    chi = S0.xi2*S0.z1**2 + S0.xi2b/S0.z1**2
    chip = S0.et2*S0.z2**2 + S0.et2b/S0.z2**2
    gin = S0.tt(a_, S0.z1)
    gin[1, 1] += chi
    gout = S0.tt(b_, S0.z2)
    gout[0, 0] += chip
    Fin = gin.applyfunc(lambda q: S0.ex(S0.fast(q, 1)))
    Fout = gout.applyfunc(lambda q: S0.ex(S0.fast(q, 0)))
    lin = [g0i[a, 1] for a in range(5)]
    lout = [g0i[a, 0] for a in range(5)]

    def one(T, x):
        return [sp.simplify(sum(T[a, b]*x[a] for a in range(5))) for b in range(5)]

    def two(T, x, y):
        return sp.simplify(sum(T[a, b]*x[a]*y[b] for a in range(5) for b in range(5)))

    own = all(c == 0 for c in one(Fin, lin)) and all(c == 0 for c in one(Fout, lout))
    cin = two(Fout, lin, lin)
    cout = two(Fin, lout, lout)
    exp_in = sp.exp(-4*sig)*S0.fast(chip, 0)
    exp_out = sp.exp(-4*sig)*S0.fast(chi, 1)
    cross = sp.simplify(cin - exp_in) == 0 and sp.simplify(cout - exp_out) == 0 and cin != 0 and cout != 0
    g0sub = {S0.xi2: 0, S0.xi2b: 0, S0.et2: 0, S0.et2b: 0}
    gauge = all(sp.simplify(c.subs(g0sub)) == 0 for c in one(Fout, lin) + one(Fin, lout))
    dv, du = [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]
    kk = sp.simplify(sum(dv[a]*lout[a] for a in range(5))**2), sp.simplify(sum(du[a]*lin[a] for a in range(5))**2)
    kself = sp.simplify(sum(dv[a]*lin[a] for a in range(5))), sp.simplify(sum(du[a]*lout[a] for a in range(5)))
    defect = kk[0] == sp.exp(-4*sig) and kk[1] == sp.exp(-4*sig) and kself == (0, 0)
    ok["Q2"] = own and cross and gauge and defect
    print("  Q2: [F1 g1_in](ell_in, .) = [F2 g1_out](ell_out, .) = 0: %s; [F2 g1_out](ell_in, ell_in) = %s, "
          "[F1 g1_in](ell_out, ell_out) = %s (= e^(-4 sigma) F chi): %s; with chi = chi' = 0 every cross contraction "
          "vanishes: %s; dv(ell_out)^2 = %s, du(ell_in)^2 = %s, dv(ell_in) = du(ell_out) = 0: %s"
          % (own, cin, cout, cross, gauge, kk[0], kk[1], defect), flush=True)
    ok["Q2 control"] = not all(c == 0 for c in one(Fout, lin))
    print("  Q2 control: [F2 g1_out](ell_in, .) = 0 fails with chi' != 0: %s" % ok["Q2 control"], flush=True)
    for name, val in ok.items():
        print(name, "PASS" if val else "FAIL")
    print("  %.0f s" % (time.time() - t0))
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
