#!/usr/bin/env python3
"""twoparity5: the quarter-turn parity for the outgoing family, and what the mean-mass statement (item 7) needs with two
families (FAMILIES5-FULL.md section 9).

The record's Proposition 8.2 (the mean mass) rests on Lemma 8.2: under the combined map S (sigma: th -> pi/2 - th, p1 <->
p2, an isometry of g0; the phase reflection s -> 3 pi/2 - s; lam -> -lam), every profile of the approximant has parity
(-1)^j, so the first mean correction m1 is sigma-odd and DM[m1] = 0 by naturality. checks/stage5.py S4 computes the base
for the ingoing family: the whole R^(1)[g0 + lam W] (mean and oscillating part) is S-odd in every nonzero component,
and one quadrature fails. With two families the same induction needs the outgoing family's base, and the mixed one.

  P1 (exact) the outgoing family on its own background: outgoing Vaidya in outgoing Eddington-Finkelstein coordinates
     (u, r, th, p1, p2), g0 = -(1 - M(u)/r^2) du^2 - 2 du dr + r^2 dOmega_3^2, ell_out = g0^-1 du = -d_r, the phase s2 =
     u/lam, W_out = the record's W_TT at s2 (polarizations P1, P2 of lead5.py with amplitude A E(u) H(th) r^(-3/2), H =
     h(cos^2 2th)) + chi_out du^2. This is where the outgoing packet is posed (on Sigma_tau0, before the shell: section
     2). Computed with lead5.py's reduced Ricci (the wave-map gauge relative to g0) on this background: R^(-1) = 0; chi
     enters the uu second harmonic of R^(0) only through c (d_r + 3/(2r)) d_s chi (c printed); the source F_out (the uu
     second harmonic of R^(0)[W_TT]) is r^-3 f(u, th, s), S-even; chi_out := the transport solution (any k(u) r^(-3/2)
     homogeneous part, so any data on a round slice) solves (E2)'s uu harmonic and W_out = W_TT + chi_out du^2 is S-odd.
  P2 (exact) stage5.py S4 for the outgoing family: the whole R^(1)[g0 + lam W_out], mean and oscillating part, under
     sigma^* with s2 -> 3 pi/2 - s2, is odd in every nonzero component.
     Control (must fail): one quadrature (the sin s2 term of W_TT removed): W_out is not S-odd and R^(1) is not odd.
  P3 (exact) the two-family background and the mass: sigma is an isometry of every round double-null metric g0 = -2
     e^(2 sig) du dv + R^2 (dth^2 + cos^2 th dp1^2 + sin^2 th dp2^2) fixing each sphere, and the Hawking mass M[S] of the
     record (N1STAR-PROOF.md section 8: M = R^2 (1 + (R^2/9) <Theta>), Theta = 2 theta+ theta- / (-g(n+, n-))) of the
     sphere {u, v = const} is the Misner-Sharp mass mu = R^2 (1 + 2 e^(-2 sig) R_u R_v) of twodust5 B3.
     Control: a sheared angular metric R^2 (e^(2 b(th)) dth^2 + ...) with b not sigma-even is not sigma-invariant.
  P4 (exact) the mixed base: on stage0two5.py's general round double-null background with both families (H =
     h(cos^2 2th); each chi with its two harmonics related by sigma as S-oddness requires), the mixed harmonics (n1, n2),
     n1 n2 != 0, of R^(0) are S-even: J R^(0)_(-n)(sigma X) J i^(n1 + n2) = R^(0)_n(X) (the phase factor of s_k -> 3 pi/2
     - s_k on e^(i n_k s_k)); so ghat_2's mixed harmonics, fixed by division by -e^(-2 sig) n1 n2 (even in n), are S-even,
     the parity (-1)^2 the induction asks of stage 2. Control: the outgoing family with one quadrature: some mixed
     harmonic is not S-even.

Labels: computed (exact, sympy). Reach: P1-P4 are the inputs of the two-family Lemma 8.2; the induction itself (every
later stage the unique solution of an S-invariant problem) is deduced, as in the record. Run: python3
checks/twoparity5.py   (about ten minutes)
"""
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import lead5 as L                                                               # noqa: E402

v, r, th, s, lam = L.v, L.r, L.th, L.s, L.lam          # v is read as the outgoing coordinate u throughout P1-P2
C, S = sp.cos(th), sp.sin(th)


def outgoing_background():
    f = 1 - L.Mf/r**2
    g = sp.diag(-f, 0, r**2, r**2*C**2, r**2*S**2)
    g[0, 1] = g[1, 0] = -1
    gi = sp.zeros(5)
    gi[0, 1] = gi[1, 0] = -1
    gi[1, 1] = f
    for i, w in zip((2, 3, 4), (r**2, r**2*C**2, r**2*S**2)):
        gi[i, i] = 1/w
    return g, gi


L.background = outgoing_background                                              # lead5's machinery, outgoing Vaidya
import stage5 as S5                                                             # noqa: E402  (uses L.background)


def zero(e):
    e = sp.expand(e)
    return e == 0 or sp.simplify(e) == 0


def p1(single=False):
    """the outgoing wave and chi_out; returns (ok, W, info)"""
    g0, g0i = outgoing_background()
    ell = sp.simplify(g0i*sp.Matrix([1, 0, 0, 0, 0]))
    ell_ok = list(ell) == [0, -1, 0, 0, 0]
    W0 = L.wave(with_chi=False)
    if single:
        W0 = W0.subs(sp.sin(s), 0)
    R0 = L.reduced_ricci(W0)
    rm1 = all(zero(R0[k][0]) for k in R0)
    cp, cm = L.modes(R0[(0, 0)][1])[2]
    F = sp.expand((cp + cm)*sp.cos(2*s) + sp.I*(cp - cm)*sp.sin(2*s))
    f = sp.simplify(F*r**3)
    form = zero(sp.diff(f, r))
    # how chi enters: R^(0)[W0 + chi du^2] - R^(0)[W0], uu component
    chi = sp.Function("chi")(v, r, th, s)
    W1 = W0.copy()
    W1[0, 0] = chi
    R0c = L.reduced_ricci(W1)
    dchi = sp.expand(R0c[(0, 0)][1] - R0[(0, 0)][1])
    op = sp.diff(chi, r, s) + sp.Rational(3, 2)*sp.diff(chi, s)/r
    c = sp.simplify(dchi/op)
    chi_only = sp.diff(c, r) == 0 and not c.has(chi) and c != 0 and all(
        zero(R0c[k][1] - R0[k][1]) for k in R0 if k != (0, 0))
    # transport: c (d_r + 3/(2r)) Y + F = 0, Y = d_s chi; Y = -(1/c)(-2 f r^-2 + k r^(-3/2)) solves it
    k = sp.Function("k")(v)
    Y = -(-2*f*r**-2 + k*r**sp.Rational(-3, 2))/c
    solves = zero(c*(sp.diff(Y, r) + 3*Y/(2*r)) + F)
    chis = sp.integrate(sp.expand(Y), s)
    W = W0.copy()
    W[0, 0] = chis
    e2 = zero(sp.expand(L.modes(L.reduced_ricci(W)[(0, 0)][1])[2][0])) if not single else None
    Fs = F.subs(L.Hf, sp.Function("h")(sp.cos(2*th)**2))
    feven = zero(Fs.subs({th: sp.pi/2 - th, s: 3*sp.pi/2 - s}, simultaneous=True) - Fs)
    Wm, Wms = S5.sigma_star(W, phase=True)
    wodd = all(zero(x) for x in Wms + Wm)
    info = dict(ell=ell_ok, rm1=rm1, form=form, c=c, chi_only=chi_only, solves=solves, e2=e2, feven=feven, wodd=wodd)
    return W, info


def p2(W):
    o = S5.series(lam*W, 0)
    R1 = {key: o[key][1] for key in o}
    M, Ms = S5.sigma_star(sp.Matrix(5, 5, lambda a, b: R1[(min(a, b), max(a, b))]), phase=True)
    nz = [(a, b) for (a, b) in S5.COMP if not zero(M[a, b])]
    bad = [(a, b) for (a, b) in nz if not zero(Ms[a, b] + M[a, b])]
    odd = not bad and all(zero(Ms[a, b] + M[a, b]) for a in range(5) for b in range(5))
    return odd and bool(nz), nz, bad


def p3(control=False):
    u, vv, t, q1, q2 = sp.symbols("u v theta phi1 phi2", real=True)
    X = [u, vv, t, q1, q2]
    sg, R = sp.Function("sigma")(u, vv), sp.Function("R")(u, vv)
    b = sp.Function("b")(t) if control else 0
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -sp.exp(2*sg)
    g[2, 2], g[3, 3], g[4, 4] = R**2*sp.exp(2*b), R**2*sp.cos(t)**2*sp.exp(-2*b), R**2*sp.sin(t)**2*sp.exp(-2*b)
    J = sp.zeros(5)
    J[0, 0] = J[1, 1] = J[3, 4] = J[4, 3] = 1
    J[2, 2] = -1
    pulled = J.T*g.subs(t, sp.pi/2 - t)*J
    iso = all(zero(x) for x in pulled - g)
    if control:
        return iso
    # Hawking mass of {u, v = const}: theta+- along n+ = g^-1 du (outgoing, d_v direction), n- = g^-1 dv
    gi = g.inv()
    n_out = gi*sp.Matrix([1, 0, 0, 0, 0])
    n_in = gi*sp.Matrix([0, 1, 0, 0, 0])
    sq = sp.sqrt(g[2, 2]*g[3, 3]*g[4, 4])

    def expansion(n):
        return sp.simplify(sum(n[a]*sp.diff(sq, X[a]) for a in range(5))/sq)
    tp, tm = expansion(n_out), expansion(n_in)
    gnn = sp.simplify((n_out.T*g*n_in)[0])
    Theta = sp.simplify(2*tp*tm/(-gnn))
    Rs = R                                                                      # area radius: Area = 2 pi^2 R^3
    M = Rs**2*(1 + Rs**2*Theta/9)
    mu = R**2*(1 + 2*sp.exp(-2*sg)*sp.diff(R, u)*sp.diff(R, vv))
    return iso and zero(M - mu)


def p4(single=False):
    import stage0two5 as S0
    Hh = sp.Function("h")(sp.cos(2*S0.th)**2)
    th0 = S0.th
    W = S0.waves()
    if single:                                     # family out with one quadrature: the sin s2 term dropped
        a_, b_ = S0.amplitudes()
        W = W - S0.tt(b_, S0.z2) + one_quad(S0, b_)
    # chi's harmonics related by sigma: y2 = x2 o sigma, yy2 = xx2 o sigma
    sub = {S0.xi2b: S0.xi2.subs(th0, sp.pi/2 - th0), S0.et2b: S0.et2.subs(th0, sp.pi/2 - th0), S0.Hf: Hh}
    W = W.subs(sub).doit()
    o = S0.ricci_orders(W)
    J = sp.zeros(5)
    J[0, 0] = J[1, 1] = J[3, 4] = J[4, 3] = 1
    J[2, 2] = -1
    harm = {}
    for (a, b) in [(a, b) for a in range(5) for b in range(a, 5)]:
        harm[(a, b)] = S0.harmonics(o[(a, b)][1])
    M = {}
    for (a, b), hs in harm.items():
        for n, cf in hs.items():
            if n[0] and n[1]:
                M.setdefault(n, sp.zeros(5))
                M[n][a, b] = M[n][b, a] = cf
    bad, count = [], 0
    for n, Mn in M.items():
        Mm = M.get((-n[0], -n[1]), sp.zeros(5))
        img = (J.T*Mm.subs(th0, sp.pi/2 - th0)*J)*sp.I**(n[0] + n[1])
        for a in range(5):
            for b in range(a, 5):
                if not zero(Mn[a, b]) or not zero(img[a, b]):
                    count += 1
                    if not zero(sp.expand(img[a, b] - Mn[a, b])):
                        bad.append((n, (a, b)))
    return not bad and count > 0, count, bad[:6]


def one_quad(S0, amp):
    """stage0two5's TT wave in z2 with its sin s2 quadrature removed"""
    z = S0.z2
    co = (z + 1/z)/2
    q1 = amp*S0.Hf*(2*S0.C**2*co)/3
    q2 = amp*S0.Hf*(-S0.C**2*co)/3
    W = sp.zeros(S0.N)
    W[2, 2], W[3, 3], W[4, 4] = -2*S0.Rf**2*(q1 + q2), 2*S0.Rf**2*S0.C**2*q1, 2*S0.Rf**2*S0.S**2*q2
    return W


def main():
    t0 = time.time()
    ok = True
    W, I = p1()
    good1 = I["ell"] and I["rm1"] and I["form"] and I["chi_only"] and I["solves"] and I["e2"] and I["feven"] and \
        I["wodd"]
    print("  P1: ell_out = g0^-1 du = -d_r: %s; R^(-1) = 0: %s; F_out = r^-3 f(u, th, s): %s; chi enters only the uu\n"
          "      harmonic, as c (d_r + 3/(2r)) d_s chi with c = %s: %s; the transport solution solves it: %s, and (E2)'s\n"
          "      uu second harmonic vanishes with it: %s; F_out S-even: %s; W_out = W_TT + chi_out du^2 S-odd: %s"
          "  [%.0f s]" % (I["ell"], I["rm1"], I["form"], I["c"], I["chi_only"], I["solves"], I["e2"], I["feven"],
                          I["wodd"], time.time() - t0), flush=True)
    ok &= good1
    good2, nz, bad = p2(W)
    print("  P2: R^(1)[g0 + lam W_out] under sigma^* with s2 -> 3 pi/2 - s2: nonzero in %s;\n"
          "      odd in every component: %s; components where it fails: %s  [%.0f s]" % (nz, good2, bad, time.time() - t0),
          flush=True)
    ok &= good2
    Wc, Ic = p1(single=True)
    good2c, nzc, badc = p2(Wc)
    print("  P2 control (one quadrature): W_out S-odd: %s; R^(1) odd: %s; fails in %s  [%.0f s]"
          % (Ic["wodd"], good2c, badc, time.time() - t0), flush=True)
    ctl = Ic["wodd"] or good2c
    good3, c3 = p3(), p3(control=True)
    print("  P3: sigma is an isometry of the round double-null metric and the Hawking mass of {u, v = const} is the\n"
          "      Misner-Sharp mu: %s; control (sheared angular metric) sigma-invariant: %s" % (good3, c3), flush=True)
    ok &= good3
    ctl = ctl or c3
    good4, cnt, bad4 = p4()
    print("  P4: R^(0)'s mixed harmonics (both families, stage0two5) S-even: %s (%d nonzero entries checked; failures %s)"
          "  [%.0f s]" % (good4, cnt, bad4, time.time() - t0), flush=True)
    good4c, cntc, bad4c = p4(single=True)
    print("  P4 control (family out with one quadrature): S-even: %s; failures, first six: %s  [%.0f s]"
          % (good4c, bad4c, time.time() - t0), flush=True)
    ok &= good4
    ctl = ctl or good4c
    print("P1-P4:", "PASS" if ok else "FAIL")
    print("controls rejected:", "PASS" if not ctl else "FAIL")
    return 0 if ok and not ctl else 1


if __name__ == "__main__":
    sys.exit(main())
