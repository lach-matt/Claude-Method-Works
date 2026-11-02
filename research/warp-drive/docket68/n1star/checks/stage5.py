#!/usr/bin/env python3
"""stage5.py -- the approximant's higher stages in the proof's wave-map gauge: computations behind three deduced steps
of paper/RESPONSE-HL-5D.md (section 4, "Higher stages"; section 3, Proposition 3.4 and Theorem 2 item 4), on lead5.py's
reduced Ricci (Ric^H relative to g0, ingoing Eddington-Finkelstein coordinates, ell = g0^-1 dv = d_r) with the
two-scale derivative D_a = d_a + lam^-1 (d_a u) d_s, u the phase. lead5 reports the orders lam^-1 and lam^0 only;
`series` below carries the same construction (lead5's background, christoffel, trunc) one order further, g^-1 by its
Neumann series to lam^(top+1), and reproduces lead5's two orders exactly (checked inside S1).

  S1 (exact) Row 2, N1STAR-PROOF.md Lemmas 5.1-5.3 at m = 1: the stage-1 system is triangular. Ansatz
     G = g0 + lam (W + m1) + lam^2 (g2 + m2) + lam^3 g3, phase u = v + lam phi1 + lam^2 phi2, W = lead5's W_TT + chi dv^2
     (chi generic in (v, r, th, s)), m1, m2 generic functions of (v, r, th), g2, g3 generic functions of (v, r, th, s),
     each in the eight T^2 x Z2 x Z2-invariant components (vv, vr, rr, v th, r th, th th, phi1 phi1, phi2 phi2; the
     symmetry class of Theorem 1), phi1, phi2 generic in (v, r, th). Every component: (a) no order below lam^0;
     (b) R^(0) = lead5's R^(0)[g0 + lam W] - (1/2) e1 d_s^2 W, e1 = 2 ell.d phi1 - m1(ell, ell); (c) in R^(1): g3 absent;
     m2, phi2 only in -(1/2)(2 ell.d phi2 - m2(ell, ell)) d_s^2 W; g2 only as -(ell.d) d_s g2 - (1/2) e1 d_s^2 g2 plus
     terms with no X-derivative of g2 and at most one d_s (Th of Lemma 5.2); second derivatives of m1 only as
     -(1/2) box~ m1 (box~ = g0^ab d_a d_b, componentwise), of phi1 only as -(1/2)(box~ phi1) d_s W; the part quadratic
     in (m1, phi1) is exactly (1/2) q2 d_s^2 W, q2 as printed after (5.2), which is also checked against the lam^2
     coefficient of gbar^-1(du, du). So the stage-1 unknowns enter as the supplement states: m1 by a wave operator,
     g2 by a transport along ell, phi1 through d phi1 and box~ phi1 only (its transport, e1 = 0, and Psi = box~ phi1's,
     from (0.1), ks5.py K3), and stage 2 only through e2. Restricted: the eight invariant components, not all fifteen;
     order lam^1 only (lam^2 not computed: the expansion with generic profiles did not fit the time here).
     Control: a non-null phase, u = v + r/3 + lam phi1 + lam^2 phi2 (dv -> dv + dr/3), must break the structure.
  S2 (exact) Row 8, Lemma 8.2 at j = 1 in this gauge: m1's source, the s-mean of R^(1)[g0 + lam W] with chi the
     transport solution of lead5 L4 (chi = int ds Y, (d_r + 3/(2r)) Y = F, F the vv second harmonic of R^(0), which is
     r^-3 f(v, th, s); Y = -2 f (r^-2 - k(v) r^(-3/2)), k(v) = (v - tau0)^(-1/2) for zero data on Sigma_tau0, any k
     carried), is odd under sigma (th -> pi/2 - th, phi1 <-> phi2): sigma^* S = -S, which with the unique solution of
     a sigma-equivariant problem gives sigma^* m1 = -m1. H is h(cos^2 2th), h generic (sigma-even, the record's H
     among them). Also printed: the nonzero components (dv dth only, as support5.py C9 found in ansatz5's Bondi gauge),
     that F is S-even, and that g1 = W (W_TT and chi) is S-odd, the induction's base. The phase mean is the 12-point
     average in s (checked equal to the 16-point one), exact for R^(1)'s harmonics (at most cubic in W, so at most 6).
     Control: one quadrature (the sin s term of W_TT removed): the check passes only if g1 is S-odd and the source odd.
     Found: with one quadrature the source alone stays odd (it is a dv dth component with a sigma-even coefficient);
     what the quarter turn carries is the base, g1 = W S-odd, which one quadrature breaks.
  S3 (exact) Row 13, Theorem 2 item 4 (supplement 9.5): the same source for the approximant from past null infinity,
     chi with no radiation there (past5.py P4-P5: Y = -2 f r^-2, r^(3/2) Y -> 0): odd, and equal to S2's (chi enters
     no mean at this order). What the record's programs do not give: m1 itself from past null infinity (past5.py has
     no m1; bondi5.py works in the Bondi gauge in r^(-1/2) series), so its parity rests on the uniqueness of Lemma
     9.1(f) with sigma-invariant data, deduced, not computed here; and the stages beyond m1 (j >= 2) are not computed
     on either route. Control: one quadrature, as S2.

Labels: computed (exact, sympy). Run: python3 checks/stage5.py   (about 45 minutes, S1 and its control most of it)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lead5 as L                                                               # noqa: E402

lam, s, X, v, r, th = L.lam, L.s, L.X, L.v, L.r, L.th
COMP = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]
TAGS = sp.symbols("ta tb tc td te")                     # m1, phi1, g2, (m2, phi2), g3


def series(H, psi, top=1):
    """lam^-3..lam^top coefficients of Ric^H(g0 + H), phase u = v + psi, in lead5's gauge and coordinates"""
    g0, g0i = L.background()
    du = [sp.diff(v + psi, x) for x in X]

    def D(e, k):
        return sp.diff(e, X[k]) + du[k]/lam*sp.diff(e, s)
    g = g0 + H
    gi, term = g0i, g0i
    for _ in range(top + 1):
        term = (-term*H*g0i).applyfunc(lambda e: L.trunc(e, top + 1))
        gi = gi + term
    G = [[[L.trunc(x, top + 1) for x in row] for row in M2] for M2 in L.christoffel(g, gi, D)]
    Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, X[k]))
    n = 5
    Dv = [L.trunc(sum(gi[a, b]*(G[p][a][b] - Gh[p][a][b]) for a in range(n) for b in range(n)), top + 1)
          for p in range(n)]
    out = {}
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += D(G[a][b][c], a) - D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            hb = sum(g[b, p]*(D(Dv[p], c) + sum(Gh[p][c][q]*Dv[q] for q in range(n))) for p in range(n))
            hc = sum(g[c, p]*(D(Dv[p], b) + sum(Gh[p][b][q]*Dv[q] for q in range(n))) for p in range(n))
            e = sp.expand(e - (hb + hc)/2)
            out[(b, c)] = {k: e.coeff(lam, k) for k in range(-3, top + 1)}
    return out


def zero(e):
    e = sp.expand(e)
    return e == 0 or sp.simplify(e) == 0


def sym(name, args):
    M = sp.zeros(5)
    for (a, b) in COMP:
        M[a, b] = M[b, a] = sp.Function("%s_%d%d" % (name, a, b))(*args)
    return M


def split(e):
    """terms of e by their degrees in the tags"""
    out = {}
    for t in sp.Add.make_args(sp.expand(e)):
        d = t.as_powers_dict()
        key = tuple(int(d.get(x, 0)) for x in TAGS)
        out[key] = out.get(key, 0) + t
    return out


def second(e, funcs):
    """the part of e linear in second derivatives of funcs, and whether any higher derivative of them occurs"""
    ds = [d for d in e.atoms(sp.Derivative) if d.expr in funcs]
    two = sum(e.coeff(d)*d for d in ds if d.derivative_count == 2)
    return two, any(d.derivative_count > 2 for d in ds)


def s1(control=False):
    t0 = time.time()
    ta, tb, tc, td, te = TAGS
    g0, g0i = L.background()
    ell = [g0i[a, 0] for a in range(5)]
    elld = lambda f: sum(ell[a]*sp.diff(f, X[a]) for a in range(5))
    box = lambda f: sum(g0i[a, b]*sp.diff(f, X[a], X[b]) for a in range(5) for b in range(5))
    m1, g2, m2, g3 = sym("m1", (v, r, th)), sym("g2", (v, r, th, s)), sym("m2", (v, r, th)), sym("g3", (v, r, th, s))
    ph1, ph2 = sp.Function("ph1")(v, r, th), sp.Function("ph2")(v, r, th)
    W = L.wave(with_chi=True)
    Ws, Wss = W.applyfunc(lambda e: sp.diff(e, s)), W.applyfunc(lambda e: sp.diff(e, s, 2))
    H = lam*(W + ta*m1) + lam**2*(tc*g2 + td*m2) + lam**3*te*g3
    psi = lam*tb*ph1 + lam**2*td*ph2 + (r/3 if control else 0)
    o = series(H, psi)
    R0 = L.reduced_ricci(W)
    mll = lambda m: sum(ell[a]*ell[b]*m[a, b] for a in range(5) for b in range(5))
    dp1 = [sp.diff(ph1, x) for x in X]
    q2f = lambda m, dp: (-sum(ell[a]*m[a, b]*g0i[b, c]*m[c, d]*ell[d] for a in range(5) for b in range(5)
                              for c in range(5) for d in range(5))
                         - sum(g0i[a, b]*dp[a]*dp[b] for a in range(5) for b in range(5))
                         + 2*sum(ell[a]*m[a, b]*g0i[b, c]*dp[c] for a in range(5) for b in range(5) for c in range(5)))
    q2 = q2f(m1, dp1)
    gbi = g0i - lam*g0i*m1*g0i + lam**2*(g0i*m1*g0i*m1*g0i - g0i*m2*g0i)        # (5.2), untagged
    du = sp.Matrix([sp.diff(v + lam*ph1 + lam**2*ph2, x) for x in X])
    e12 = sp.expand((du.T*gbi*du)[0])
    e1u, e2u = 2*elld(ph1) - mll(m1), 2*elld(ph2) - mll(m2) - q2
    eq52 = zero(e12.coeff(lam, 1) - e1u) and zero(e12.coeff(lam, 2) - e2u) and e12.coeff(lam, 0) == 0
    e1 = 2*tb*elld(ph1) - ta*mll(m1)
    q2t = q2f(ta*m1, [tb*x for x in dp1])
    m1f, g2f = {m1[a, b] for (a, b) in COMP}, {g2[a, b] for (a, b) in COMP}
    ok = dict(low=True, r0=True, g3=True, st2=True, g2=True, m1=True, phi1=True, quad=True)
    for k in o:
        ok["low"] &= all(zero(o[k][j]) for j in (-3, -2, -1))
        ok["r0"] &= zero(o[k][0] - (R0[k][1] - e1*Wss[k]/2))
        P = split(o[k][1])
        ok["g3"] &= not any(key[4] for key in P)
        ok["st2"] &= zero(sum(P[key] for key in P if key[3]) + td*(2*elld(ph2) - mll(m2))*Wss[k]/2)
        rest = sp.expand(sum(P[key] for key in P if key[2]) + tc*(elld(sp.diff(g2[k], s)) + e1*sp.diff(g2[k], s, 2)/2))
        ok["g2"] &= all(d.variables == (s,) for d in rest.atoms(sp.Derivative) if d.expr in g2f)
        AB = {key: P[key] for key in P if not any(key[2:]) and key[0] + key[1]}
        lin = sp.expand(sum(AB[key] for key in AB if key[0] + key[1] == 1))
        two, high = second(lin, m1f)
        ok["m1"] &= not high and zero(two + ta*box(m1[k])/2)
        two, high = second(lin, {ph1})
        ok["phi1"] &= not high and zero(two + tb*box(ph1)*Ws[k]/2)
        ok["quad"] &= zero(sum(AB[key] for key in AB if key[0] + key[1] == 2) - q2t*Wss[k]/2)
        ok["quad"] &= not any(key[0] + key[1] > 2 for key in AB)
    tag = "S1 control (u = v + r/3)" if control else "S1"
    print("  %s: (5.2) e1, e2 as printed: %s; no order below lam^0: %s; R^(0) = R_v^(0)[W] - (1/2) e1 d_s^2 W: %s;\n"
          "      in R^(1): g3 absent: %s; m2, phi2 only in -(1/2) e2 d_s^2 W: %s; g2 only as -(ell.d) d_s g2 - (1/2) e1"
          " d_s^2 g2 + (no X-derivative, one d_s): %s;\n      second derivatives of m1 only in -(1/2) box~ m1: %s; of"
          " phi1 only in -(1/2)(box~ phi1) d_s W: %s; quadratic part = (1/2) q2 d_s^2 W: %s [%.0fs]"
          % (tag, eq52, ok["low"], ok["r0"], ok["g3"], ok["st2"], ok["g2"], ok["m1"], ok["phi1"], ok["quad"],
             time.time() - t0), flush=True)
    return eq52 and all(ok.values())


def mean(e, M=12):
    return sp.expand(sum(e.subs(s, 2*sp.pi*j/M) for j in range(M))/M)


def sigma_star(M, phase=False):
    """sigma^* of a symmetric tensor field M(v, r, th[, s]), H -> h(cos^2 2th); with phase, also s -> 3 pi/2 - s"""
    J = sp.zeros(5)
    J[0, 0] = J[1, 1] = J[3, 4] = J[4, 3] = 1
    J[2, 2] = -1
    M = M.subs(L.Hf, sp.Function("h")(sp.cos(2*th)**2)).doit()
    sub = {th: sp.pi/2 - th, s: 3*sp.pi/2 - s} if phase else {th: sp.pi/2 - th}
    return M, J.T*M.subs(sub, simultaneous=True)*J


def source(single=False, past=False):
    W0 = L.wave(with_chi=False)
    if single:
        W0 = W0.subs(sp.sin(s), 0)
    cp, cm = L.modes(L.reduced_ricci(W0)[(0, 0)][1])[2]
    F = sp.expand((cp + cm)*sp.cos(2*s) + sp.I*(cp - cm)*sp.sin(2*s))
    f = sp.simplify(F*r**3)
    k = sp.Function("k")(v)
    Y = -2*f*r**-2 if past else -2*f*(r**-2 - k*r**sp.Rational(-3, 2))
    ok = zero(sp.diff(f, r)) and zero(sp.diff(Y, r) + 3*Y/(2*r) - F)
    tau0 = sp.Symbol("tau0")
    ok &= sp.limit(r**sp.Rational(3, 2)*Y, r, sp.oo) == 0 if past else zero(
        Y.subs(k, (v - tau0)**sp.Rational(-1, 2)).subs(r, v - tau0))
    Fs = F.subs(L.Hf, sp.Function("h")(sp.cos(2*th)**2))
    feven = zero(Fs.subs({th: sp.pi/2 - th, s: 3*sp.pi/2 - s}, simultaneous=True) - Fs)
    W = W0.copy()
    W[0, 0] = sp.integrate(sp.expand(Y), s)
    o = series(lam*W, 0)
    S = {key: mean(o[key][1]) for key in o}
    exact = all(zero(S[key] - mean(o[key][1], 16)) for key in o)
    return S, ok and exact, feven, W


def parity(name, control, past):
    t0 = time.time()
    S, ok, feven, W = source(single=control, past=past)
    M, Ms = sigma_star(sp.Matrix(5, 5, lambda a, b: S[(min(a, b), max(a, b))]))
    odd = all(zero(x) for x in Ms + M)
    Wm, Wms = sigma_star(W, phase=True)
    wodd = all(zero(x) for x in Wms + Wm)
    nz = [key for key in S if not zero(S[key])]
    if control:
        print("  %s control (one quadrature): g1 = W S-odd: %s; the source alone still odd, sigma^* S = -S: %s"
              % (name, wodd, odd), flush=True)
        return wodd and odd, S
    print("  %s: chi solves its transport (%s): %s; F S-even: %s; g1 = W (W_TT and chi) S-odd: %s;\n      source"
          " nonzero in %s: %s; sigma^* S = -S (m1 odd): %s [%.0fs]"
          % (name, "no radiation at past null infinity" if past else "zero data on Sigma_tau0", ok, feven, wodd, nz,
             [sp.factor(sp.trigsimp(M[a, b])) for (a, b) in nz], odd, time.time() - t0), flush=True)
    return ok and feven and wodd and odd and bool(nz), S


_S2 = {}


def s2(control=False):
    good, S = parity("S2", control, past=False)
    _S2[control] = S
    return good


def s3(control=False):
    good, S = parity("S3", control, past=True)
    if control or False not in _S2:
        return good
    same = all(zero(S[key] - _S2[False][key]) for key in S)
    print("      S3's source equals S2's (chi enters no mean at lam^1): %s" % same, flush=True)
    return good and same


CHECKS = [("S1", s1), ("S2", s2), ("S3", s3)]


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
