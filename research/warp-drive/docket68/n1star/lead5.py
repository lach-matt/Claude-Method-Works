#!/usr/bin/env python3
"""lead5.py -- N1*, Theorem A stage 0: the leading equation (E2) for the record's waves in the proof's gauge.

Commissioned at item 522 (N1STAR-LOG.md D7, D11).  N1STAR-PROOF.md works in the wave-map gauge relative to g0,
D = g^{ab}(Gamma[g] - Gamma[g0])_ab, Ric^H = Ric - (1/2)(g Dh D + (g Dh D)^T) (0.2), which is a tensor, so it is
computed here in the ingoing Eddington-Finkelstein coordinates (v, r, th, phi1, phi2) of the record, where
g0 = -(1 - M/r^2) dv^2 + 2 dv dr + r^2 (dth^2 + c^2 dphi1^2 + s^2 dphi2^2) and ell = g0^-1 dv = d_r.  The metric is
g = g0 + lam W(v, r, th, s), s = v/lam, with W = W_TT + chi dv dv: W_TT the record's first-order wave (ansatz5 A3:
P1 = A E H r^(-3/2) (2 c^2 cos s - s^2 sin s)/3, P2 = A E H r^(-3/2) (2 s^2 sin s - c^2 cos s)/3,
W_TT = r^2 diag(-2(P1 + P2), 2 c^2 P1, 2 s^2 P2) on (th, phi1, phi2)), chi an arbitrary function of (v, r, th, s).
Ric^H is expanded in lam with d_v -> d_v + lam^-1 d_s.  Labels: computed (exact, sympy).

  L1 R^(-1) = 0 in every component.
  L2 <R^(0)> (the s-mean) vanishes in every component exactly when M' = (2/9) A^2 E^2 H^2 (c^4 + s^4); with the
     record's H = sqrt(2/(1 + cos^2 2th)), H^2 (c^4 + s^4) = 1: the energy condition of ansatz5 A4, in this gauge.
  L3 With chi = 0 the oscillating part of R^(0) is nonzero only in the vv component, and only in the second
     harmonic: the transverse-traceless components vanish by the record's transport (r^(-3/2)).
  L4 chi enters R^(0) only through -(d_r + 3/(2 r)) d_s chi in the vv component (the transport -(D_ell + (1/2) box v)
     d_th applied to chi dv dv).  Hence (E2) holds for W = W_TT + chi dv dv iff (d_r + 3/(2r)) d_s chi equals the
     vv second harmonic of L3: a transport along ell, solvable with chi = 0 on the initial slice.
  L5 W(ell, .) = 0 and tr_g0 W = 0: (E1) and the polarization.
python3 lead5.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

MUT = set()
MUTANTS = {"not_reduced": "Ric in place of Ric^H (the gauge term dropped): the oscillating R^(0) leaves vv (L3)",
           "in_phase": "the two polarizations in phase: the mean is not round (L2)",
           "r_minus_1": "amplitude r^-1 in place of r^(-3/2): W_TT not transported (L3)",
           "chi_dvdr": "chi placed on dv dr: it is not transverse and enters other components (L4, L5)"}

v, r, th, p1, p2, s, lam, A = sp.symbols("v r theta phi1 phi2 s lam A", real=True)
X = [v, r, th, p1, p2]
Mf = sp.Function("M")(v)
Ef = sp.Function("E")(v)
Hf = sp.Function("H")(th)
chi = sp.Function("chi")(v, r, th, s)
C, S = sp.cos(th), sp.sin(th)
H_REC = sp.sqrt(2/(1 + sp.cos(2*th)**2))


def background():
    f = 1 - Mf/r**2
    g = sp.diag(-f, 0, r**2, r**2*C**2, r**2*S**2)
    g[0, 1] = g[1, 0] = 1
    gi = sp.zeros(5)
    gi[0, 1] = gi[1, 0] = 1
    gi[1, 1] = f
    for i, w in zip((2, 3, 4), (r**2, r**2*C**2, r**2*S**2)):
        gi[i, i] = 1/w
    return g, gi


def wave(with_chi=True):
    y3 = r**-1 if "r_minus_1" in MUT else r**sp.Rational(-3, 2)
    Gq, Fq = sp.cos(s), sp.sin(s)
    if "in_phase" in MUT:
        Fq = sp.cos(s)
    a1 = A*Ef*Hf*y3*(2*C**2*Gq - S**2*Fq)/3
    a2 = A*Ef*Hf*y3*(2*S**2*Fq - C**2*Gq)/3
    W = sp.zeros(5)
    W[2, 2], W[3, 3], W[4, 4] = -2*r**2*(a1 + a2), 2*r**2*C**2*a1, 2*r**2*S**2*a2
    if with_chi:
        if "chi_dvdr" in MUT:
            W[0, 1] = W[1, 0] = chi
        else:
            W[0, 0] = chi
    return W


def D(e, k):
    out = sp.diff(e, X[k])
    if k == 0:
        out += sp.diff(e, s)/lam
    return out


def trunc(e, top):
    e = sp.expand(e)
    return sum(e.coeff(lam, k)*lam**k for k in range(-3, top + 1))


def christoffel(g, gi, deriv):
    n = 5
    dg = [[[deriv(g[a, b], k) for k in range(n)] for b in range(n)] for a in range(n)]
    return [[[sum(gi[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(n))/2 for c in range(n)]
             for b in range(n)] for a in range(n)]


def reduced_ricci(W):
    """lam^-1 and lam^0 coefficients of Ric^H(g0 + lam W) in the wave-map gauge relative to g0"""
    g0, g0i = background()
    g = g0 + lam*W
    Wu = g0i*W*g0i
    gi = (g0i - lam*Wu + lam**2*Wu*W*g0i).applyfunc(lambda e: trunc(e, 2))
    G = christoffel(g, gi, D)
    G = [[[trunc(x, 1) for x in row] for row in M2] for M2 in G]
    Gh = christoffel(g0, g0i, lambda e, k: sp.diff(e, X[k]))
    n = 5
    Dv = [trunc(sum(gi[a, b]*(G[rho][a][b] - Gh[rho][a][b]) for a in range(n) for b in range(n)), 1)
          for rho in range(n)]
    out = {}
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += D(G[a][b][c], a) - D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            if "not_reduced" not in MUT:
                hb = sum(g[b, rho]*(D(Dv[rho], c) + sum(Gh[rho][c][sg]*Dv[sg] for sg in range(n))) for rho in range(n))
                hc = sum(g[c, rho]*(D(Dv[rho], b) + sum(Gh[rho][b][sg]*Dv[sg] for sg in range(n))) for rho in range(n))
                e -= (hb + hc)/2
            e = trunc(e, 0)
            out[(b, c)] = (sp.simplify(e.coeff(lam, -1)), e.coeff(lam, 0))
    return out


def modes(e):
    """s-Fourier modes of a trigonometric polynomial in s (other s-dependence left in the mean)"""
    z = sp.Symbol("z")
    sub = {}
    for k in range(4, 0, -1):
        sub[sp.sin(k*s)] = (z**k - z**-k)/(2*sp.I)
        sub[sp.cos(k*s)] = (z**k + z**-k)/2
    e = sp.expand(sp.expand_trig(sp.expand(e)))
    e = sp.expand(e.subs({sp.sin(s): (z - 1/z)/(2*sp.I), sp.cos(s): (z + 1/z)/2}))
    P = sp.Poly(sp.expand(e*z**8), z)
    out = {}
    for k in range(0, 9):
        ck, cm = P.coeff_monomial(z**(8 + k)), P.coeff_monomial(z**(8 - k))
        out[k] = (sp.simplify(ck), sp.simplify(cm)) if k else sp.simplify(ck)
    return out


def compute():
    R0 = reduced_ricci(wave(with_chi=False))
    R1 = reduced_ricci(wave(with_chi=True))
    return dict(R0=R0, R1=R1)


def checks(o):
    c = {}
    R0, R1 = o["R0"], o["R1"]
    c["L1 R^(-1) = 0 in every component"] = all(sp.simplify(R1[k][0]) == 0 for k in R1)
    # L2: means of R^(0) with chi = 0 (chi's terms are d_s-derivatives, mean zero, checked in L4)
    Mp = sp.Symbol("Mp")
    mean = {k: modes(R0[k][1].subs(sp.Derivative(Mf, v), Mp))[0] for k in R0}
    sol = sp.solve(mean[(0, 0)], Mp)
    others = all(sp.simplify(mean[k]) == 0 for k in mean if k != (0, 0))
    want = sp.Rational(2, 9)*A**2*Ef**2*Hf**2*(C**4 + S**4)
    c["L2 <R^(0)> = 0 iff M' = (2/9) A^2 E^2 H^2 (c^4 + s^4); with the record's H, M' = (2/9) A^2 E^2"] = (
        others and len(sol) == 1 and sp.simplify(sol[0] - want) == 0
        and sp.simplify((Hf**2*(C**4 + S**4)).subs(Hf, H_REC) - 1) == 0)
    osc_ok = True
    for k in R0:
        m = modes(R0[k][1])
        nz = [j for j in range(1, 9) if any(sp.simplify(x) != 0 for x in m[j])]
        if k == (0, 0):
            osc_ok = osc_ok and nz == [2]
        else:
            osc_ok = osc_ok and nz == []
    c["L3 chi = 0: the oscillating R^(0) lies in vv only, second harmonic only (W_TT transported)"] = osc_ok
    ok4 = True
    for k in R1:
        diff = sp.simplify(sp.expand(R1[k][1] - R0[k][1]))
        if k == (0, 0):
            ok4 = ok4 and sp.simplify(diff + sp.diff(chi, r, s) + sp.Rational(3, 2)*sp.diff(chi, s)/r) == 0
        else:
            ok4 = ok4 and diff == 0
    c["L4 chi enters R^(0) only as -(d_r + 3/(2r)) d_s chi in vv"] = ok4
    g0, g0i = background()
    W = wave(True)
    ell = [g0i[a, 0] for a in range(5)]
    transverse = all(sp.simplify(sum(W[a, b]*ell[a] for a in range(5))) == 0 for b in range(5))
    traceless = sp.simplify(sum(g0i[a, b]*W[a, b] for a in range(5) for b in range(5))) == 0
    c["L5 W(ell, .) = 0 and tr_g0 W = 0"] = transverse and traceless
    return c


def selftest():
    c = checks(compute())
    for k, v_ in c.items():
        print("%-118s %s" % (k[:118], "PASS" if v_ else "FAIL"))
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear()
        MUT.add(m_)
        try:
            c = checks(compute())
            failed = [k[:30] for k, v_ in c.items() if not v_]
        except Exception as ex:                       # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-12s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
