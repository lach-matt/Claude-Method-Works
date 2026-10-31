"""e2cplx5.py -- E2-PILOT section 3h (D394): the Morawetz bounds of sections 3e-3g off the real axis, Im sigma > 0.

For Im sigma > 0 the outgoing solution of -u'' + (V - sigma^2) u = f decays at both ends, so there is no flux term; with
sigma^2 = a + i b the identity of Lemma E2.8' (q >= 0; q = 0 is Lemma E2.8) becomes (J1)

    2 int (phi' - q)|u'|^2 + int W_q |u|^2 + 2a int q|u|^2 = Re int f (2 phi u'bar + (phi' - 2q) u-bar)
                                                             - 2b int phi Im(u u-bar'),

and the energy identity (J2) gives b ||u||^2 = -Im int f u-bar and ||u'||^2 <= ||f|| ||u||_I + max(a, 0) ||u||^2, so
|2b int phi Im(u u-bar')| <= 2(|b|^(1/2) + max(a, 0)^(1/2)) ||f|| ||u||_I <= 4|sigma| ||f|| ||u||_I. Hence the bound
B^+(sigma) := ((2/m' + (M' + 4|sigma|)^2/w_I)/w_I)^(1/2) for every sigma with Im sigma > 0 (Lemma E2.8), and for
|Re sigma| >= Im sigma > 0 with q (Lemma E2.8', where 2a int q|u|^2 >= 0 needs a >= 0).

  J1 (exact) the identity, as an exact derivative, for complex sigma^2; with the b-term's sign flipped it fails.
  J2 (exact) the energy identity f u-bar = |u'|^2 + (V - sigma^2)|u|^2 - (u' u-bar)'.
  J3 (computed) at l = 1, the cut-off resolvent norm ||chi_I R(sigma) chi_I|| at sigma = 3 + i eta, eta = 0.25, 0.5, 1,
     2, by finite differences on r_* in [-80, 120] (u decays like e^(-eta |r_*|)), and at eta = 0.25 on a grid twice as
     fine; each lies below B^+(sigma) with the certified l = 1 constants of checks/e2certify5.py C5 (peak centre),
     recomputed here. Independent check of the solver: since -d^2 + V >= 0 is self-adjoint, ||R(sigma)|| <=
     1/|Im sigma^2|, and each computed norm lies below that too.
Labels: J1-J2 computed (exact, sympy); J3 computed (floating point, not certified); the bound itself proved in
E2-PILOT section 3h.

    python3 checks/e2cplx5.py [--selftest]
"""
import math
import sys

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import sympy as sp


def identities():
    X = sp.symbols("x", real=True)
    p, q_, V, ph, Q = [sp.Function(n)(X) for n in ("p", "q", "V", "phi", "Q")]
    a, b = sp.symbols("a b", real=True)
    u, ub = p + sp.I*q_, p - sp.I*q_
    f = -sp.diff(u, X, 2) + (V - (a + sp.I*b))*u
    fb = -sp.diff(ub, X, 2) + (V - (a - sp.I*b))*ub
    m = lambda uu: 2*ph*sp.diff(uu, X) + (sp.diff(ph, X) - 2*Q)*uu
    rhs = sp.expand((f*m(ub) + fb*m(u))/2)
    imuub = sp.expand((u*sp.diff(ub, X) - ub*sp.diff(u, X))/(2*sp.I))
    bd = (-ph*sp.diff(u, X)*sp.diff(ub, X) + ph*(V - a)*u*ub
          - sp.diff(ph, X)*(sp.diff(u, X)*ub + u*sp.diff(ub, X))/2 + sp.diff(ph, X, 2)*u*ub/2
          + Q*(sp.diff(u, X)*ub + u*sp.diff(ub, X)) - sp.diff(Q, X)*u*ub)
    ok = []
    for sign in (1, -1):
        lhs = (2*(sp.diff(ph, X) - Q)*sp.diff(u, X)*sp.diff(ub, X)
               + (-ph*sp.diff(V, X) - sp.Rational(1, 2)*sp.diff(ph, X, 3) + sp.diff(Q, X, 2) - 2*Q*V + 2*a*Q)*u*ub
               + sign*2*b*ph*imuub)
        ok.append(sp.simplify(sp.expand(rhs - lhs - sp.diff(bd, X))) == 0)
    e = sp.expand(f*ub - (sp.diff(u, X)*sp.diff(ub, X) + (V - (a + sp.I*b))*u*ub - sp.diff(sp.diff(u, X)*ub, X)))
    return ok[0] and not ok[1], sp.simplify(e) == 0


def potential_on(xg, l):
    """V_l on a uniform r_*-grid, r from r_* by interpolation on a fine t = ln(r - 1) grid"""
    t = np.linspace(-200.0, math.log(1e6), 2000001)
    e = np.exp(t)
    r = 1 + e
    xs = r + 0.5*(t - np.log(2 + e))
    rg = np.interp(xg, xs, r)
    tg = np.interp(xg, xs, t)
    eg = np.exp(tg)
    f = eg*(2 + eg)/(1 + eg)**2
    y = 1/rg**2
    a, b = l*(l + 2) + 0.75, 2.25
    return f*(a*y + b*y*y), rg


def resolvent_norm(sigma, l=1, h=0.02, L=(-80.0, 120.0)):
    xg = np.arange(L[0], L[1] + h/2, h)
    V, rg = potential_on(xg, l)
    n = len(xg)
    main = 2/h**2 + V - sigma**2
    A = sps.diags([np.full(n - 1, -1/h**2), main, np.full(n - 1, -1/h**2)], [-1, 0, 1], format="csc")
    I = np.where((rg >= 1.2) & (rg <= 4.0))[0]
    lu = spla.splu(A.astype(complex))
    G = np.empty((len(I), len(I)), complex)
    for k, i in enumerate(I):
        rhs = np.zeros(n, complex)
        rhs[i] = 1/h                     # a unit L^2 delta on the grid
        G[:, k] = lu.solve(rhs)[I]*h     # kernel times the cell weight: the operator on l^2 with weight h
    return np.linalg.norm(G, 2)


def c5_constants_l1():
    """m', M', w_I at l = 1 for the peak-centred multiplier, as e2certify5.py C5 computes them (lower, upper, lower)"""
    import importlib.util
    import os
    spec = importlib.util.spec_from_file_location("e2certify5", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                           "e2certify5.py"))
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    tg = np.linspace(-3, 1.5, 20001)
    yg = 1/(1 + np.exp(tg))**2
    tp = float(tg[np.argmax((1 - yg)*(3.75*yg + 2.25*yg*yg))])
    xc = C.xr(C.iv.mpf(tp))
    tIa, tIb = C.iv.log(C.iv.mpf("0.2")).a, C.iv.log(C.iv.mpf(3)).b
    wI = C.min_lower(C.A_(1), tIa, tIb, 2000, xc=xc)
    m1 = min(C.parts(C.iv.mpf(tIa), C.S, xc)[1].a, C.parts(C.iv.mpf(tIb), C.S, xc)[1].a)
    return float(C.mpf(m1)), float(C.mpf((1/C.S).b)), float(C.mpf(wI))


def main():
    ok = {}
    j1, j2 = identities()
    ok["J1"], ok["J2"] = j1, j2
    print("  J1: identity off the axis exact, b-sign control fails: %s; J2 energy identity exact: %s" % (j1, j2))
    m1, M1, wI = c5_constants_l1()
    j3, sane = True, True
    for eta in (0.25, 0.5, 1.0, 2.0):
        sg = complex(3.0, eta)
        nr = resolvent_norm(sg)
        Bp = math.sqrt((2/m1 + (M1 + 4*abs(sg))**2/wI)/wI)
        cap = 1/abs((sg**2).imag)
        j3 = j3 and nr <= Bp
        sane = sane and nr <= cap
        print("  J3: sigma = 3 + %.2fi: ||chi R chi|| = %.4f <= B^+ = %.1f: %s; <= 1/|Im sigma^2| = %.4f: %s"
              % (eta, nr, Bp, nr <= Bp, cap, nr <= cap), flush=True)
    coarse, fine = resolvent_norm(complex(3.0, 0.25)), resolvent_norm(complex(3.0, 0.25), h=0.01)
    print("  J3: sigma = 3 + 0.25i at h = 0.02, 0.01: %.5f, %.5f (grid check)" % (coarse, fine))
    ok["J3"] = j3 and abs(fine - coarse)/fine < 0.05
    ok["J3 solver check"] = sane
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
