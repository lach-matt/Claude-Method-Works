"""e2lzero5.py -- E2-PILOT section 3g (D387): the harmonic l = 0, by a Morawetz identity with a Lagrangian term,
certified by interval arithmetic (mpmath.iv) and explicit tails.

Lemma E2.8 needs w := -phi V' - phi'''/2 >= 0, and at l = 0 no tanh multiplier gives it (section 3f: w_0 < 0 near
r = 3.2 for the photon-sphere centre). Adding -2q u-bar to the multiplier, with q >= 0, q, q' -> 0 at +-oo, gives (Z1)

    2 int (phi' - q)|u'|^2 + int W_q |u|^2 + 2 sigma^2 int q |u|^2 = Re int f (2 phi u'bar + (phi' - 2q) u-bar)
                                                                      + 2 sigma^2 (|c_+|^2 + |c_-|^2),
    W_q := w + q'' - 2 q V,

so E2.8's bound holds with phi' - q >= 0 and W_q >= 0 on R, m' := min_I (phi' - q), M' := max_I |phi' - 2q|,
w_I := min_I W_q (the sigma^2 q term has the good sign and is dropped).

Here phi = tanh((r_* - x_c)/s), s = 49/50, x_c = r_*(sqrt 2) - 3/10, and q = sum_k c_k sech^2((r_* - x_k)/kappa_k): 43
bumps, x_k - r_*(sqrt 2) on a lattice of 1/4, kappa_k = (3/10, 1/2, 9/10) s, c_k >= 0 rounded to four digits. The c_k
came from a linear program (maximise min_I W_q subject to W_q >= phi'/30 and q <= phi'/2 on a grid, over that
dictionary of bumps; scratchpad, D387); the certificate below checks this q itself, not the program.

  Z1 the identity, pointwise as an exact derivative (sympy), for any smooth u, V, phi, q; with q'' entering at -1 it
     fails.
  Z2 W_q >= 0 and phi' - q >= 0 on r_* in [x(t = -120), x(r = 120)], t := ln(r - 1), by adaptive bisection in t.
  Z3 the tails. Below the range, q'' >= 0 (every bump is past its inflection), so W_q >= -phi V' (1 - rho_3 - rho_q)
     with rho_3 := (|phi'''|/2)/(-phi V') <= K e^(2 r_*(1/s - 1)) (decreasing toward the horizon as s < 1) and
     rho_q := 2 q V/(-phi V') <= sum_k 8 c_k e^(2(r_* - x_k)/kappa_k) (a + b) r_L^3/(2 tanh|z_L| D_L) (increasing),
     where D_L := (a + b) - e_L (4a + 8b) bounds a(2y - 1) + b y (3y - 2) below for every a, b > 0 (section 3f used
     a >= b, false at l = 0); and q/phi' <= sum_k 4 s c_k e^(2(r_* - x_k)/kappa_k - 2(r_* - x_c)/s), increasing as
     kappa_k < s. Above it, the same with tail_right's bound for rho_3 and rho_q, q/phi' decreasing. Each sum is
     certified < 1 at the end of the range.
  Z4 certified m', M', w_I on I = {r in [1.2, 4]} (2000 pieces), so certified upper bounds for B_0(sigma) at
     sigma = 0+, 1, 3, 10.
  Z5 controls: without q, w_0 < 0 at a point (certified); with q'' entering at -1, the bisection fails and W < 0
     at a point (certified).
Labels: certified (interval arithmetic, outward rounding, 30 digits; endpoints at 103 bits; decimals rounded outward),
given mpmath.iv's correctness; the identity and the tail inequalities are proved in E2-PILOT section 3g.

    python3 checks/e2lzero5.py [--selftest]
"""
import importlib.util
import os
import sys
import time

import sympy as sp
from mpmath import iv, mp, mpf

_spec = importlib.util.spec_from_file_location("e2certify5", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                          "e2certify5.py"))
C5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C5)
assert mp.prec == iv.prec
S, B_, xr, tanh_of, dec, certify_positive = C5.S, C5.B_, C5.xr, C5.tanh_of, C5.dec, C5.certify_positive

A0 = iv.mpf(3)/4                                  # a at l = 0
X_STAR = C5.X_C                                   # r_*(sqrt 2)
XC = X_STAR - iv.mpf(3)/10
BUMPS = [
    (-2.25, 0.3, 0.001324), (-2.0, 0.3, 0.0005167), (-1.75, 0.3, 0.0002329), (-1.5, 0.3, 0.0003749),
    (-1.25, 0.3, 0.0005019), (-1.0, 0.3, 0.001073), (-0.75, 0.3, 0.001401), (0.0, 0.3, 7.142e-06),
    (0.5, 0.3, 3.506e-06), (0.75, 0.3, 7.241e-06), (1.0, 0.3, 9.589e-06), (1.25, 0.3, 1.412e-05),
    (1.5, 0.3, 2.57e-05), (1.75, 0.3, 5.525e-05), (2.0, 0.3, 0.0001279), (2.25, 0.3, 0.0002422),
    (2.5, 0.3, 0.0003176), (2.75, 0.3, 0.0002074), (3.0, 0.3, 9.863e-05), (3.5, 0.3, 0.0007565),
    (6.5, 0.3, 5.478e-07), (6.75, 0.3, 8.62e-07), (7.5, 0.3, 2.743e-07),
    (-2.25, 0.5, 0.007685), (-2.0, 0.5, 0.01241), (-1.75, 0.5, 0.01933), (-1.5, 0.5, 0.02541),
    (-1.25, 0.5, 0.03734), (-1.0, 0.5, 0.0512), (-0.75, 0.5, 0.07205), (-0.5, 0.5, 0.09774),
    (-0.25, 0.5, 0.1044), (0.0, 0.5, 0.08574), (0.25, 0.5, 0.05632), (0.5, 0.5, 0.03267),
    (0.75, 0.5, 0.01792), (1.0, 0.5, 0.009678), (1.25, 0.5, 0.005313), (1.5, 0.5, 0.003036),
    (1.75, 0.5, 0.001846), (2.0, 0.5, 0.001106), (2.25, 0.5, 0.0005728),
    (-3.0, 0.9, 0.0009532),
]
QB = [(X_STAR + iv.mpf(str(o)), iv.mpf(str(k))*S, iv.mpf(str(c))) for o, k, c in BUMPS]


def bump(z):
    """sech^2 z and tanh z on an interval, without forming 1 - tanh^2 away from 0"""
    T = tanh_of(z)
    if z.b < -3 or z.a > 3:
        E = iv.exp(2*z) if z.b < 0 else iv.exp(-2*z)
        return 4*E/(1 + E)**2, T
    return 1 - T**2, T


def qparts(r_star, sign=1):
    q, q2 = iv.mpf(0), iv.mpf(0)
    for xk, k, c in QB:
        Sk, Tk = bump((r_star - xk)/k)
        q += c*Sk
        q2 += c*2*Sk*(3*Tk**2 - 1)/k**2
    return q, sign*q2


def fields(tt, sign=1):
    e = iv.exp(tt)
    r = 1 + e
    y = 1/r**2
    f = e*(2 + e)/r**2
    X = xr(tt)
    T, ph1, ph3, Up, Qp = C5.parts(tt, S, XC)
    V = f*(A0*y + B_*y**2)
    w = -T*(A0*Up + B_*Qp) - ph3/2
    q, q2 = qparts(X, sign)
    return w + q2 - 2*q*V, ph1 - q, ph1 - 2*q, w


def certify(fn, t0, t1, minw=mpf("1e-9")):
    stack, n = [(mpf(t0), mpf(t1))], 0
    while stack:
        lo, hi = stack.pop()
        val = fn(iv.mpf([lo, hi]))
        n += 1
        if val.a >= 0:
            continue
        if hi - lo < minw:
            return False, n, (lo, hi, val)
        mid = (lo + hi)/2
        stack += [(lo, mid), (mid, hi)]
    return True, n, None


def tails(tL, rR):
    a, b, s = A0, B_, S
    # left
    eL = iv.exp(iv.mpf(tL)); rL = 1 + eL; XL = xr(iv.mpf(tL)); zL = (XL - XC)/s
    th = -tanh_of(zL)
    DL = (a + b) - eL*(4*a + 8*b)
    C = 8*DL*iv.exp(-2*rL)/rL**5
    rho3 = 8*iv.exp(-2*XC/s)/(s**3*th*C)*iv.exp(2*XL*(1/s - 1))
    rhoq = sum((8*c*iv.exp(2*(XL - xk)/k) for xk, k, c in QB), iv.mpf(0))*(a + b)*rL**3/(2*th*DL)
    qphi = sum((4*s*c*iv.exp(2*(XL - xk)/k - 2*(XL - XC)/s) for xk, k, c in QB), iv.mpf(0))
    past = all(((XL - xk)/k).b < -iv.mpf("0.66") for xk, k, c in QB)
    narrow = all((k - s).b < 0 for _, k, _ in QB)    # kappa_k < s: q decays faster than phi' at both ends
    left = (rho3 + rhoq).b < 1 and qphi.b < 1 and past and DL.a > 0 and (1/s - 1).a > 0 and narrow
    # right
    rR = iv.mpf(rR); XR = xr(iv.log(rR - 1)); dR = -iv.log((rR - 1)/(rR + 1))/2; zR = (XR - XC)/s
    thR = tanh_of(zR); cR = (1 - 1/rR**2)*(1 - 2/rR**2)
    rho3R = (8/s**3)*iv.exp(-2*zR)*(XR + dR)**3/(2*a*cR*thR)
    rhoqR = sum((8*c*iv.exp(-2*(XR - xk)/k) for xk, k, c in QB), iv.mpf(0))*(a + b)*(XR + dR)/(2*a*cR*thR)
    qphiR = sum((4*s*c*iv.exp(-2*(XR - xk)/k + 2*(XR - XC)/s) for xk, k, c in QB), iv.mpf(0))
    pastR = all(((XR - xk)/k).a > iv.mpf("0.66") for xk, k, c in QB)
    mono = (XR + dR - 3*s/2).a > 0 and min((XR + dR - k/2).a for _, k, _ in QB) > 0
    right = (rho3R + rhoqR).b < 1 and qphiR.b < 1 and pastR and mono and narrow
    return left, right, (rho3 + rhoq, qphi, rho3R + rhoqR, qphiR)


def identity_ok(flip=False):
    X = sp.symbols("x", real=True)
    p, q_, V, ph, Q = [sp.Function(n)(X) for n in ("p", "q", "V", "phi", "Q")]
    sg = sp.symbols("sigma", positive=True)
    u, ub = p + sp.I*q_, p - sp.I*q_
    f = -sp.diff(u, X, 2) + (V - sg**2)*u
    fb = -sp.diff(ub, X, 2) + (V - sg**2)*ub
    m = lambda uu: 2*ph*sp.diff(uu, X) + (sp.diff(ph, X) - 2*Q)*uu
    rhs = sp.expand((f*m(ub) + fb*m(u))/2)
    sq = -1 if flip else 1
    lhs = (2*(sp.diff(ph, X) - Q)*sp.diff(u, X)*sp.diff(ub, X)
           + (-ph*sp.diff(V, X) - sp.Rational(1, 2)*sp.diff(ph, X, 3) + sq*sp.diff(Q, X, 2) - 2*Q*V + 2*sg**2*Q)*u*ub)
    bd = (-ph*sp.diff(u, X)*sp.diff(ub, X) + ph*(V - sg**2)*u*ub
          - sp.diff(ph, X)*(sp.diff(u, X)*ub + u*sp.diff(ub, X))/2 + sp.diff(ph, X, 2)*u*ub/2
          + Q*(sp.diff(u, X)*ub + u*sp.diff(ub, X)) - sp.diff(Q, X)*u*ub)
    return sp.simplify(sp.expand(rhs - lhs - sp.diff(bd, X))) == 0


def run(verbose=True):
    t0 = time.time()
    ok = {}
    ok["Z1"] = identity_ok() and not identity_ok(flip=True)
    if verbose:
        print("  Z1: the identity with the Lagrangian term, exact; q'' at -1 fails: %s (%.0fs)" % (ok["Z1"],
              time.time() - t0), flush=True)
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    g1, n1, b1 = certify(lambda tt: fields(tt)[0], tL, tR)
    g2, n2, b2 = certify(lambda tt: fields(tt)[1], tL, tR)
    ok["Z2"] = g1 and g2
    if verbose:
        print("  Z2: W_q >= 0 on t in [%d, ln %d]: %s (%d enclosures); phi' - q >= 0: %s (%d) (%.0fs)%s"
              % (tL, rR - 1, g1, n1, g2, n2, time.time() - t0,
                 "" if ok["Z2"] else "  failed at %s %s" % (b1, b2)), flush=True)
    left, right, rh = tails(tL, rR)
    ok["Z3"] = left and right
    if verbose:
        print("  Z3: left rho_3 + rho_q <= %s, q/phi' <= %s; right rho_3 + rho_q <= %s, q/phi' <= %s: %s"
              % (dec(rh[0].b, 3, True), dec(rh[1].b, 3, True), dec(rh[2].b, 3, True), dec(rh[3].b, 3, True),
                 ok["Z3"]), flush=True)
    tIa, tIb = iv.log(iv.mpf("0.2")).a, iv.log(iv.mpf(3)).b
    pieces = 2000
    ta, tb = mpf(tIa), mpf(tIb)
    ends = [ta] + [ta + (tb - ta)*k/pieces for k in range(1, pieces)] + [tb]
    wI = m1 = M1 = None
    for lo, hi in zip(ends[:-1], ends[1:]):
        W, P, P2, _ = fields(iv.mpf([lo, hi]))
        wI = W.a if wI is None or W.a < wI else wI
        m1 = P.a if m1 is None or P.a < m1 else m1
        hiabs = max(abs(P2.a), abs(P2.b))
        M1 = hiabs if M1 is None or hiabs > M1 else M1
    bs = [C5.b_bound(iv.mpf(wI), m1, M1, sg).b for sg in (0, 1, 3, 10)] if wI > 0 and m1 > 0 else None
    ok["Z4"] = bs is not None
    if verbose:
        print("  Z4: min_I W_q >= %s, m' >= %s, M' <= %s; B_0(0+, 1, 3, 10) <= %s (%.0fs)"
              % (dec(wI, 4, False), dec(m1, 4, False), dec(M1, 4, True),
                 "-" if bs is None else ", ".join(dec(b, 4, True) for b in bs), time.time() - t0), flush=True)
    gflip, _, bflip = certify(lambda tt: fields(tt, sign=-1)[0], tL, tR)
    t0n, w0, tneg, neg = None, None, None, None     # certified negative values, not only failed splits
    for k in range(501):
        tt = mpf(-2) + mpf(5)*k/500
        W, _, _, wv = fields(iv.mpf(tt), sign=-1)
        if neg is None or W.b < neg.b:
            tneg, neg = tt, W
        if w0 is None or wv.b < w0.b:
            t0n, w0 = tt, wv
    ok["Z5 controls"] = w0.b < 0 and not gflip and neg.b < 0
    if verbose:
        print("  Z5: without q, w_0 <= %s at t = %s; with q'' at -1 the bisection fails and W <= %s at t = %s"
              % (dec(w0.b, 4, True), iv.nstr(iv.mpf(t0n), 4), dec(neg.b, 3, True), iv.nstr(iv.mpf(tneg), 4)))
        print("  (%.0fs)" % (time.time() - t0))
    return ok, bs


def main():
    ok, _ = run()
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
