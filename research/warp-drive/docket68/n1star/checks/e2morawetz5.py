"""e2morawetz5.py -- E2-PILOT section 3e (Lemma E2.8): a one-dimensional Morawetz bound for the cut-off resolvent of
the scalar wave on 5D Tangherlini (mu = 1, r_h = 1), harmonic by harmonic, at every real sigma != 0.

With x = r_*, V_l = (1 - y)(a y + b y^2), y = 1/r^2, a = l(l+2) + 3/4, b = 9/4 (E2.7's form), and u the outgoing
solution of -u'' + (V_l - sigma^2) u = f, f in L^2(I), I = {r in [1.2, 4]}, the identity

    2 int phi' |u'|^2 + int w |u|^2 = Re int f (2 phi u'bar + phi' u bar) + 2 sigma^2 (|c_+|^2 + |c_-|^2),
    w := -phi V_l' - phi'''/2,

holds for phi smooth, increasing, phi(+-oo) = +-1, phi', phi'' -> 0 (u ~ c_+- e^(+-i sigma x) at +-oo). With the flux
identity sigma (|c_+|^2 + |c_-|^2) = -Im int f u bar, w >= 0 on R, m' := min_I phi', M' := max_I phi', w_I := min_I w:

    ||chi_I R_l(sigma) chi_I|| <= B_l(sigma) := ((2/m' + (M' + 2|sigma|)^2/w_I)/w_I)^(1/2).

Here phi = tanh((x - x_p)/s), x_p the peak of V_l, so -phi V_l' >= 0, and s in (0, 1) is chosen per l; s < 1 is what
the horizon tail needs (V_l' ~ e^(2x) there, phi''' ~ e^(2x/s)).

  M1 the identity, pointwise as an exact derivative (sympy), for any smooth u, V, phi; a sign-flipped phi''' fails.
  M2 for each l >= 1, an s with w >= 0 on a grid of x in [-59, 120] and the horizon tail dominated (the ratio of
     |phi'''|/2 to -phi V_l' at most 1 on x < -20, and falling); at l = 0 the tanh family has no admissible s. Control:
     s = 1.5 fails at l = 5, as the horizon tail needs s < 1.
  M3 B_l(3) exceeds the computed norm of checks/e2band5_s3.out at every l >= 1 there (a bound, not an estimate); a
     hundredth of it does not, at the band's peak l = 5.
Labels: M1 computed (exact); M2-M3 computed (floating point, not certified).

    python3 checks/e2morawetz5.py [--selftest] [--table L_MAX]
"""
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RA, RB = 1.2, 4.0


def grid(n=600001):
    """t = log(r - 1); f = 1 - 1/r^2 from t, so nothing cancels near the horizon"""
    t = np.linspace(-120.0, math.log(119.0), n)
    e = np.exp(t)
    r = 1 + e
    x = r + 0.5*(t - np.log(2 + e))
    f = e*(2 + e)/r**2
    return r, x, f


def pot(r, f, l):
    a, b, y = l*(l + 2) + 0.75, 2.25, 1/r**2
    return f*(a*y + b*y*y)


def dpot_dx(r, f, l):
    a, b, y = l*(l + 2) + 0.75, 2.25, 1/r**2
    return f*(a + 2*(b - a)*y - 3*b*y*y)*(-2/r**3)


def phis(z, s):
    e = np.exp(-2*np.abs(z))
    th, sh2 = np.tanh(z), 4*e/(1 + e)**2
    return th, sh2/s, -2*sh2*(1 - 3*th*th)/s**3


def quantities(l, s, r, x, f):
    Vp = dpot_dx(r, f, l)
    xp = x[np.argmax(pot(r, f, l))]
    ph, ph1, ph3 = phis((x - xp)/s, s)
    w = -ph*Vp - 0.5*ph3
    inI = (r >= RA) & (r <= RB)
    core = (x > -30) & (x < 120)
    return dict(wmin=w[core].min(), wI=w[inI].min(), m1=ph1[inI].min(), M1=ph1[inI].max(), xp=xp,
                tail_left=(-ph*Vp)[x < -20].min() - (0.5*ph3)[x < -20].max(),
                tail_ratio=np.max((0.5*np.abs(ph3)/np.maximum(-ph*Vp, 1e-300))[(x < -20) & (x > -60)]))


def bound(q, sigma):
    if q["wI"] <= 0 or q["wmin"] < 0:
        return math.inf
    return math.sqrt((2/q["m1"] + (q["M1"] + 2*abs(sigma))**2/q["wI"])/q["wI"])


def best(l, r, x, f, sigma=3.0):
    out = None
    for s in np.linspace(0.2, 0.98, 40):
        q = quantities(l, s, r, x, f)
        if q["wmin"] < 0 or q["tail_ratio"] > 1:
            continue
        bnd = bound(q, sigma)
        if out is None or bnd < out[1]:
            out = (s, bnd, q)
    return out


def identity_ok(flip=False):
    X = sp.symbols("x", real=True)
    p, q, V, ph = [sp.Function(n)(X) for n in ("p", "q", "V", "phi")]
    sg = sp.symbols("sigma", positive=True)
    u = p + sp.I*q
    ub = p - sp.I*q
    f = -sp.diff(u, X, 2) + (V - sg**2)*u
    fb = -sp.diff(ub, X, 2) + (V - sg**2)*ub
    rhs = sp.expand((f*(2*ph*sp.diff(ub, X) + sp.diff(ph, X)*ub) + fb*(2*ph*sp.diff(u, X) + sp.diff(ph, X)*u))/2)
    s3 = -1 if flip else 1
    lhs = (2*sp.diff(ph, X)*sp.diff(u, X)*sp.diff(ub, X) - ph*sp.diff(V, X)*u*ub
           - s3*sp.Rational(1, 2)*sp.diff(ph, X, 3)*u*ub)
    bd = (-ph*sp.diff(u, X)*sp.diff(ub, X) + ph*(V - sg**2)*u*ub
          - sp.diff(ph, X)*(sp.diff(u, X)*ub + u*sp.diff(ub, X))/2 + sp.diff(ph, X, 2)*u*ub/2)
    return sp.simplify(sp.expand(rhs - lhs - sp.diff(bd, X))) == 0


def computed_norms():
    out = {}
    path = os.path.join(HERE, "e2band5_s3.out")
    for line in open(path):
        tok = line.split()
        if tok and tok[0] == "l":
            out[int(tok[1])] = float(tok[tok.index("||chiRchi||") + 1])
    return out


def main():
    r, x, f = grid()
    if "--table" in sys.argv:
        lmax = int(sys.argv[sys.argv.index("--table") + 1])
        print(" l      s     w_I       m'      M'    B(1)    B(3)   B(10)")
        for l in range(0, lmax + 1):
            b = best(l, r, x, f)
            if b is None:
                print("%2d  no admissible s" % l)
                continue
            s, _, q = b
            print("%2d  %5.3f %8.4f %8.5f %7.4f %7.3f %7.3f %7.3f" % (l, s, q["wI"], q["m1"], q["M1"], bound(q, 1),
                                                                     bound(q, 3), bound(q, 10)), flush=True)
        return
    ok = {}
    ok["M1"] = identity_ok() and not identity_ok(flip=True)
    norms = computed_norms()
    m2, m3, ctrl = True, True, False
    for l in sorted(norms):
        b = best(l, r, x, f)
        if b is None:
            m2 = m2 and l == 0
            print("  l = %d: no admissible s" % l)
            continue
        s, bnd, q = b
        m2 = m2 and q["wmin"] >= 0 and q["tail_ratio"] <= 1
        m3 = m3 and bnd >= norms[l]
        ctrl = ctrl or (l == 5 and 0.01*bnd < norms[l])
        print("  l = %2d  s = %.3f  w_I = %.4f  B(3) = %.3f  computed %.4f" % (l, s, q["wI"], bnd, norms[l]), flush=True)
    q15 = quantities(5, 1.5, r, x, f)
    ok["M2"] = m2
    ok["M2 control"] = q15["wmin"] < 0 or q15["tail_ratio"] > 1
    ok["M3"] = m3
    ok["M3 control"] = ctrl
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
