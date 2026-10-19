#!/usr/bin/env python3
"""ks5.py -- N1*, the coordinates of the proof: five-dimensional Vaidya in ingoing Kerr-Schild form.

Commissioned at item 522 (N1STAR-LOG.md, D7).  The proof (N1STAR-PROOF.md) runs in the Cartesian coordinates
(tau, x) in R x R^4, r = |x|, in which the T^2 axes are regular points, with the phase v = tau + r.  This instrument
checks the facts about the background the proof uses there.  Labels: computed (exact, sympy).

  K1 The ingoing Kerr-Schild form.  g0 = eta + (mu(v)/r^2) dv dv, v = tau + r, eta the Minkowski metric, pulls back
     under tau = v - r, x = r omega(th, phi1, phi2) (omega = (c cos phi1, c sin phi1, s cos phi2, s sin phi2)) to
     -(1 - mu/r^2) dv^2 + 2 dv dr + r^2 (dth^2 + c^2 dphi1^2 + s^2 dphi2^2): the Vaidya metric of ansatz5 A2, whose
     Ricci tensor is F0^2 dv dv, F0^2 = 3 mu'/(2 r^3).  det g0 = det eta = -1.
  K2 The inverse and the null generator.  g0^-1 = eta^-1 - (mu/r^2) L0 L0 with L0 = -g0^-1(dv) = d_tau - xhat.d_x,
     g0(L0, L0) = 0, L0(v) = 0, L0(xhat) = 0: the components of L0 are constant along L0.
  K3 Touati's Lemma 3.1 in these coordinates, as an identity: for the principal part box~ = g0^{mn} d_m d_n and any
     u(tau, x),  [L0, box~] u = (2/r) (box~ u + (d_tau + d_r)(L0 u)) - (3/r^2) d_r u,  d_r = xhat.d_x.  The mass drops
     out.  The second derivatives are d(L0 u) and box~ u only.
  K4 The transport is L^2-neutral at leading order.  div(L0) = -3/r and box_g0 v = 3/r, so for the scalar transport
     operator -2 L0 + box_g0 v the flat-measure identity d/dtau int f^2 dx = -int f (-2 L0 f + (3/r) f) dx holds with
     no zeroth-order remainder (sqrt|g0| = 1).
  K5 The gauge source of the background.  H0^rho = g0^{mn} Gamma^rho_mn = -box_g0 x^rho = (-mu/r^3, mu xhat^i/r^3):
     smooth for r > 0.
sympy.  python3 ks5.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

MUT = set()
MUTANTS = {"wrong_sign_ks": "g0 = eta - (mu/r^2) dv dv: the pullback is not Vaidya (K1)",
           "outgoing_phase": "v = tau - r: L0 not null (K2)",
           "drop_box": "the box~ u term dropped from K3",
           "flat_div": "div L0 taken as -4/r (R^5 count) (K4)"}

T, x1, x2, x3, x4 = sp.symbols("tau x1 x2 x3 x4", real=True)
XS = [x1, x2, x3, x4]
X = [T] + XS
mu = sp.Function("mu")


def setup():
    r = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    v = T - r if "outgoing_phase" in MUT else T + r
    dv = [sp.diff(v, y) for y in X]
    eta = sp.diag(-1, 1, 1, 1, 1)
    s = -1 if "wrong_sign_ks" in MUT else 1
    g = eta + s*mu(v)/r**2*sp.Matrix(5, 5, lambda i, j: dv[i]*dv[j])
    L = [1] + [-y/r for y in XS]
    gi = eta.inv() - s*mu(v)/r**2*sp.Matrix(5, 5, lambda i, j: L[i]*L[j])
    return r, v, dv, g, gi, L


def k1():
    vv, rr, th, f1, f2 = sp.symbols("v r theta phi1 phi2", positive=True)
    c, s = sp.cos(th), sp.sin(th)
    om = [c*sp.cos(f1), c*sp.sin(f1), s*sp.cos(f2), s*sp.sin(f2)]
    Y = [vv, rr, th, f1, f2]
    sgn = -1 if "wrong_sign_ks" in MUT else 1
    tau_e = vv - rr
    xs_e = [rr*o for o in om]
    # pull back eta + sgn (mu(v)/r^2) dv dv; on the image r = |x| = rr and v = tau + r = vv
    J = sp.Matrix(5, 5, lambda a, b: sp.diff(([tau_e] + xs_e)[a], Y[b]))
    eta = sp.diag(-1, 1, 1, 1, 1)
    dvY = sp.Matrix([1, 0, 0, 0, 0])
    G = sp.simplify(J.T*eta*J + sgn*mu(vv)/rr**2*dvY*dvY.T)
    F = 1 - mu(vv)/rr**2
    V = sp.diag(-F, 0, rr**2, rr**2*c**2, rr**2*s**2)
    V[0, 1] = V[1, 0] = 1
    return sp.simplify(G - V) == sp.zeros(5)


def k2():
    r, v, dv, g, gi, L = setup()
    inv_ok = sp.simplify(g*gi - sp.eye(5)) == sp.zeros(5)
    Lup = [-sp.simplify(sum(gi[a, b]*dv[b] for b in range(5))) for a in range(5)]
    gen = all(sp.simplify(Lup[a] - L[a]) == 0 for a in range(5))
    null = sp.simplify(sum(g[a, b]*L[a]*L[b] for a in range(5) for b in range(5))) == 0
    Lv = sp.simplify(sum(L[a]*dv[a] for a in range(5))) == 0
    Lxhat = all(sp.simplify(sum(L[a]*sp.diff(y/r, X[a]) for a in range(5))) == 0 for y in XS)
    det = sp.simplify(g.det())
    return dict(inv=inv_ok, gen=gen, null=null, Lv=Lv, Lxhat=Lxhat, det=det)


def k3():
    """the identity is a linear differential operator of order <= 3 in u; it vanishes identically iff it annihilates
    (y - p)^alpha at p for every multi-index |alpha| <= 3 and every p; checked exactly at two rational points with
    mu(q) = 1 + q^2/7"""
    import itertools
    r, v, dv, g, gi, L = setup()
    mq = sp.Lambda(sp.Symbol("q"), 1 + sp.Symbol("q")**2/7)
    gi = gi.subs(mu, mq).doit()
    box = lambda w: sum(gi[a, b]*sp.diff(w, X[a], X[b]) for a in range(5) for b in range(5))
    Lop = lambda w: sum(L[a]*sp.diff(w, X[a]) for a in range(5))
    dr = lambda w: sum((y/r)*sp.diff(w, y) for y in XS)
    cb = 0 if "drop_box" in MUT else 1
    D = lambda w: Lop(box(w)) - box(Lop(w)) - ((2/r)*(cb*box(w) + sp.diff(Lop(w), T) + dr(Lop(w)))
                                               - (3/r**2)*dr(w))
    pts = [(sp.Rational(3, 7), sp.Rational(1, 2), sp.Rational(-2, 3), sp.Rational(5, 4), sp.Rational(1, 3)),
           (sp.Rational(-1, 5), sp.Rational(2, 1), sp.Rational(1, 3), sp.Rational(-1, 2), sp.Rational(3, 2))]
    worst = 0
    for p in pts:
        for deg in range(0, 4):
            for alpha in itertools.combinations_with_replacement(range(5), deg):
                mono = sp.Integer(1)
                for k in alpha:
                    mono *= (X[k] - p[k])
                val = sp.simplify(D(mono).subs(dict(zip(X, p))))
                worst = max(worst, abs(float(val)))
    return dict(worst=worst)


def k4():
    r, v, dv, g, gi, L = setup()
    divL = sp.simplify(sum(sp.diff(L[a], X[a]) for a in range(5)))
    if "flat_div" in MUT:
        divL = -4/r
    # box_g0 v with sqrt|g| = 1: d_a (g^{ab} d_b v)
    boxv = sp.simplify(sum(sp.diff(sum(gi[a, b]*dv[b] for b in range(5)), X[a]) for a in range(5)))
    return dict(divL=divL, boxv=boxv, sumz=sp.simplify(divL + boxv))


def k5():
    r, v, dv, g, gi, L = setup()
    H = [sp.simplify(-sum(sp.diff(gi[a, b], X[a]) for a in range(5)) * 1) for b in range(5)]   # -box x^b (sqrt g = 1)
    return dict(H=H, r=r)


def compute():
    return dict(k1=k1(), k2=k2(), k3=k3(), k4=k4(), k5=k5())


def checks(o):
    c = {}
    c["K1 eta + (mu(v)/r^2) dv dv, v = tau + r, pulls back to the Vaidya metric of ansatz5 A2"] = o["k1"]
    q = o["k2"]
    c["K2 g0^-1 = eta^-1 - (mu/r^2) L0 L0, L0 = -g0^-1 dv = d_tau - xhat.d_x null, L0(v) = L0(xhat) = 0, "
      "det g0 = -1"] = (
        q["inv"] and q["gen"] and q["null"] and q["Lv"] and q["Lxhat"] and q["det"] == -1)
    c["K3 [L0, box~] u = (2/r)(box~ u + (d_tau + d_r) L0 u) - (3/r^2) d_r u, exactly (at exact rational points)"] = (
        o["k3"]["worst"] == 0)
    q = o["k4"]
    r = o["k5"]["r"]
    c["K4 div L0 = -3/r, box_g0 v = 3/r: the scalar transport is L^2-neutral in the flat measure"] = (
        sp.simplify(q["divL"] + 3/r) == 0 and sp.simplify(q["boxv"] - 3/r) == 0 and q["sumz"] == 0)
    H = o["k5"]["H"]
    m = mu(T + r)
    c["K5 H0 = g0^{mn} Gamma_mn = (-mu/r^3, mu xhat/r^3)"] = (
        sp.simplify(H[0] + m/r**3) == 0 and all(sp.simplify(H[i + 1] - m*XS[i]/r**4) == 0 for i in range(4)))
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
        print("mutant %-16s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
