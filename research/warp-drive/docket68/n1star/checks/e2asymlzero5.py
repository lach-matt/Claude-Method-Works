#!/usr/bin/env python3
"""e2asymlzero5.py -- E2-PILOT section 3i (D473): l = 0 under D466's asymmetric multiplier, certified.

D466 certified the asymmetric multiplier (width 49/50 toward the horizon, 2 outside, harmonically interpolated with
kap = 1/2, centred at x_* = r_*(sqrt 2); checks/e2asymcert5.py) for every l >= 1, C <= 184.82 at sigma = 3, and left
l = 0 open: there w_0 < 0 (D462, certified negative at t = -3.9). As in section 3g (Lemma E2.8'), the multiplier takes
a Lagrangian term -2 q u-bar, q = sum_k c_k sech^2((r_* - x_k)/kappa_k) >= 0, and E2.8's bound holds with
W_q := -phi V' - phi'''/2 + q'' - 2 q V >= 0 and phi' - q >= 0 on R, m' := min_I (phi' - q), M' := max_I |phi' - 2q|,
w_I := min_I W_q. Here phi is D466's (the same closed form, e2asymcert5.mult), so one multiplier serves every l, and q
has 37 bumps: x_k - x_* on a lattice of 1/4 in [-3, 3], kappa_k in {3/10, 1/2, 9/10} s_L (each < s_L < s_R, so q
decays faster than phi' at both ends), c_k > 0 rounded to four digits. The c_k came from a linear program (maximise
min_I W_q subject to W_q >= phi'/30 and q <= 7 phi'/10 on a grid, over that dictionary; scratchpad, D473); the
certificate checks this q, not the program.

  L1 the identity of Lemma E2.8' (e2lzero5's Z1, which holds for any smooth phi, q, V), exact; with q'' entering at
     -1 it fails.
  L2 W_q >= 0 and phi' - q >= 0 on t in [-120, ln 119], t := ln(r - 1), by adaptive bisection.
  L3 the tails. Below the range every bump is past its inflection (q'' >= 0), so W_q >= -phi V' (1 - rho_3 - rho_q):
     rho_3 := (|phi'''|/2)/(-phi V') <= K e^(2 r_*(1/s_L - 1)) as in D466's left tail, with the V' bound valid for
     every a, b > 0 (section 3g's D_L = (a + b) - e_L (4a + 8b)); rho_q := 2qV/(-phi V') <= sum_k 8 c_k
     e^(2(r_* - x_k)/kappa_k) (a + b) r_L^3/(2 tanh|g_L| D_L), increasing; and q/phi' <= sum_k 4 c_k s_R
     e^(2(r_* - x_k)/kappa_k - 2(r_* - x_*)/s_L), increasing (phi' >= sech^2(g)/s_R >= e^(2g)/s_R and g >= (r_* -
     x_*)/s_L for r_* <= x_*). Above it, rho_3 as in D466's right tail (its V' bound uses only a > 0), rho_q <= sum_k
     8 c_k e^(-2(r_* - x_k)/kappa_k) (a + b)(r_* + d_R)/(2 a c_R tanh g_R) and q/phi' <= sum_k 4 c_k s_R
     e^(-2(r_* - x_k)/kappa_k + 2(r_* - x_*)/s_R + 2 D kap ln 2) (g <= (r_* - x_*)/s_R + D kap ln 2), all decreasing.
     Each is certified < 1 at the end of its range.
  L4 on I = {r in [1.2, 4]}, over 2000 pieces: w_I, m', M' enclosed, then B_0(3) = ((2/m' + c^2/w_I)/w_I)^(1/2) and
     X_0(3) = (1 + (1 + 2 m' c B_0)^(1/2))/(2 m'), c = M' + 6 (e2asymcert5's K3 at l = 0, where A_0 = 0), rounded
     outward; with D466's C_l (l >= 1; C_1 recomputed here, D478) the summed H^1 constant at sigma = 3 over every
     l >= 0. Every bound is printed rounded outward (D478).
  L5 controls: without q, w_0 < 0 at t = -3.9 (certified); with q'' entering at -1 the bisection fails and W < 0 at a
     point (certified); and the left tail's bound does not certify at t = -3.

Labels: certified (interval arithmetic, mpmath.iv at 30 digits; explicit tails), given mpmath.iv's correctness.

    python3 checks/e2asymlzero5.py
"""
import importlib.util
import os
import sys
import time

from mpmath import iv, mp, mpf


def _round(x, d, f):
    x = mpf(x)
    if x == 0:
        return "0"
    q = mpf(10) ** (d - 1 - int(mp.floor(mp.log10(abs(x)))))
    return mp.nstr(f(x * q) / q, d)


def up(x, d=5):
    """x rounded up to d significant digits: an upper bound printed as one (D478)"""
    return _round(x, d, mp.ceil)


def dn(x, d=5):
    """x rounded down to d significant digits: a lower bound printed as one (D478)"""
    return _round(x, d, mp.floor)


HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


AC = _load("e2asymcert5")
E0 = _load("e2lzero5")
iv.dps = 30
SL, SR, KAP, DD, LN2, X_C = AC.SL, AC.SR, AC.KAP, AC.DD, AC.LN2, AC.X_C
A0, B_ = iv.mpf(3) / 4, AC.B_
SIGMA = iv.mpf(3)
BUMPS = [
    (-3.0, 0.9, 0.0001019), (-2.25, 0.3, 0.005884), (-2.0, 0.3, 0.002439), (-2.0, 0.5, 0.01627),
    (-1.75, 0.3, 0.0005424), (-1.75, 0.5, 0.0228), (-1.5, 0.3, 0.0002401), (-1.5, 0.5, 0.02852),
    (-1.25, 0.3, 0.0001029), (-1.25, 0.5, 0.03843), (-1.0, 0.3, 0.0002491), (-1.0, 0.5, 0.04784),
    (-0.75, 0.3, 0.0002909), (-0.75, 0.5, 0.06217), (-0.5, 0.3, 0.0001926), (-0.5, 0.5, 0.0726),
    (-0.25, 0.5, 0.07546), (0.0, 0.3, 0.0001608), (0.0, 0.5, 0.06012), (0.25, 0.5, 0.04728),
    (0.5, 0.3, 0.0001531), (0.5, 0.5, 0.03303), (0.75, 0.5, 0.02793), (1.0, 0.3, 0.0001528),
    (1.0, 0.5, 0.0197), (1.25, 0.5, 0.01804), (1.5, 0.3, 0.0001949), (1.5, 0.5, 0.01157),
    (1.75, 0.3, 0.0001426), (1.75, 0.5, 0.01109), (2.0, 0.3, 0.0005671), (2.0, 0.5, 0.005387),
    (2.25, 0.3, 0.0009074), (2.25, 0.5, 0.00561), (2.5, 0.3, 0.001778), (2.75, 0.3, 0.001609),
    (3.0, 0.3, 0.000706),
]
QB = [(X_C + iv.mpf(str(o)), iv.mpf(str(k)) * SL, iv.mpf(str(c))) for o, k, c in BUMPS]


def qparts(x, sign=1):
    q, q2 = iv.mpf(0), iv.mpf(0)
    for xk, k, c in QB:
        Sk, Tk = E0.bump((x - xk) / k)
        q += c * Sk
        q2 += c * 2 * Sk * (3 * Tk**2 - 1) / k**2
    return q, sign * q2


def fields(tt, sign=1, with_q=True):
    e = iv.exp(tt)
    r = 1 + e
    y = 1 / r**2
    f = e * (2 + e) / r**2
    X = AC.xr(tt)
    T, p1, p3 = AC.mult(X)
    Up, Qp = AC.pots(tt)
    V = f * (A0 * y + B_ * y**2)
    w = -T * (A0 * Up + B_ * Qp) - p3 / 2
    if not with_q:
        return w, p1, p1, w
    q, q2 = qparts(X, sign)
    return w + q2 - 2 * q * V, p1 - q, p1 - 2 * q, w


def tails(tL, rR):
    a, b = A0, B_
    eL = iv.exp(iv.mpf(tL)); rL = 1 + eL; XL = AC.xr(iv.mpf(tL))
    gL = (XL - X_C) / SL + DD * KAP * LN2                       # an upper bound for g there, negative
    th = -(1 - 2 / (iv.exp(2 * gL) + 1))                         # tanh|g| from below
    DL = (a + b) - eL * (4 * a + 8 * b)
    C = 8 * DL * iv.exp(-2 * rL) / rL**5                         # V' >= C e^(2 r_*) below, every a, b > 0
    pre = 4 * iv.exp(2 * (-X_C / SL + DD * KAP * LN2))
    ezc = iv.exp(-X_C / KAP)
    e2 = iv.exp(2 * XL)
    num = pre * (DD * ezc * e2 / KAP**2 + 6 * DD * ezc * e2 / (SL * KAP) + 6 / SL**3) / 2
    rho3 = num / (th * C) * iv.exp(2 * XL * (1 / SL - 1))
    rhoq = sum((8 * c * iv.exp(2 * (XL - xk) / k) for xk, k, c in QB), iv.mpf(0)) * (a + b) * rL**3 / (2 * th * DL)
    qphi = sum((4 * c * SR * iv.exp(2 * (XL - xk) / k - 2 * (XL - X_C) / SL) for xk, k, c in QB), iv.mpf(0))
    past = all(((XL - xk) / k).b < -iv.mpf("0.66") for xk, k, c in QB)
    narrow = all((k - SL).b < 0 for _, k, _ in QB)
    left = ((rho3 + rhoq).b < 1 and qphi.b < 1 and past and DL.a > 0 and (1 / SL - 1).a > 0 and narrow
            and gL.b < 0)
    rR = iv.mpf(rR); XR = AC.xr(iv.log(rR - 1)); dR = -iv.log((rR - 1) / (rR + 1)) / 2
    rho3R, mono3 = AC.tail_right(a, rR)
    gR = (XR - X_C) / SR
    thR = 1 - 2 / (iv.exp(2 * gR) + 1)
    cR = (1 - 1 / rR**2) * (1 - 2 / rR**2)
    rhoqR = sum((8 * c * iv.exp(-2 * (XR - xk) / k) for xk, k, c in QB), iv.mpf(0)) * (a + b) * (XR + dR) / (
        2 * a * cR * thR)
    qphiR = sum((4 * c * SR * iv.exp(-2 * (XR - xk) / k + 2 * (XR - X_C) / SR + 2 * DD * KAP * LN2)
                 for xk, k, c in QB), iv.mpf(0))
    pastR = all(((XR - xk) / k).a > iv.mpf("0.66") for xk, k, c in QB)
    mono = mono3.a > 0 and min((XR + dR - k / 2).a for _, k, _ in QB) > 0
    right = ((rho3R + rhoqR).b < 1 and qphiR.b < 1 and pastR and mono and narrow and thR.a > 0 and cR.a > 0
             and (rho3R.a >= 0))
    return left, right, (rho3 + rhoq, qphi, rho3R + rhoqR, qphiR)


def main():
    t0 = time.time()
    ok = {}
    ok["L1"] = E0.identity_ok() and not E0.identity_ok(flip=True)
    print("  L1: Lemma E2.8''s identity, exact; q'' at -1 fails: %s (%.0fs)" % (ok["L1"], time.time() - t0), flush=True)
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    g1, n1, b1 = E0.certify(lambda tt: fields(tt)[0], tL, tR)
    g2, n2, b2 = E0.certify(lambda tt: fields(tt)[1], tL, tR)
    ok["L2"] = g1 and g2
    print("  L2: W_q >= 0 on t in [%d, ln %d]: %s (%d enclosures); phi' - q >= 0: %s (%d) (%.0fs)%s"
          % (tL, rR - 1, g1, n1, g2, n2, time.time() - t0, "" if ok["L2"] else "  failed at %s %s" % (b1, b2)),
          flush=True)
    left, right, rh = tails(tL, rR)
    ok["L3"] = left and right
    print("  L3: left rho_3 + rho_q <= %s, q/phi' <= %s; right rho_3 + rho_q <= %s, q/phi' <= %s: %s"
          % tuple([up(x.b, 4) for x in rh] + [ok["L3"]]), flush=True)
    tIa, tIb = iv.log(iv.mpf("0.2")).a, iv.log(iv.mpf(3)).b
    pieces = 2000
    ends = [mpf(tIa) + (mpf(tIb) - mpf(tIa)) * k / pieces for k in range(pieces)] + [mpf(tIb)]
    wI = m1 = M1 = None
    for lo, hi in zip(ends[:-1], ends[1:]):
        W, P, P2, _ = fields(iv.mpf([lo, hi]))
        wI = W.a if wI is None or W.a < wI else wI
        m1 = P.a if m1 is None or P.a < m1 else m1
        hiabs = max(abs(P2.a), abs(P2.b))
        M1 = hiabs if M1 is None or hiabs > M1 else M1
    ok["L4"] = wI > 0 and m1 > 0
    if ok["L4"]:
        w, m = iv.mpf(wI), iv.mpf(m1)
        c = iv.mpf(M1) + 2 * SIGMA
        B = iv.sqrt((2 / m + c**2 / w) / w)
        X0 = (1 + iv.sqrt(1 + 2 * m * c * B)) / (2 * m)
        m1a, M1a = AC.enclose_I(lambda tt: AC.mult(AC.xr(tt))[1])      # D466's l = 1 constant, recomputed (D478)
        w1, _ = AC.enclose_I(lambda tt: AC.w_of(tt, AC.A_(1)))
        ma, wa, ca = iv.mpf(m1a), iv.mpf(w1), iv.mpf(M1a) + 2 * SIGMA
        B1 = iv.sqrt((2 / ma + ca**2 / wa) / wa)
        X1 = (1 + iv.sqrt(1 + 2 * ma * ca * B1)) / (2 * ma)
        C1 = iv.sqrt(X1**2 + 3 * B1**2)
        C = max(X0.b, C1.b)
        ok["L4"] = X0.b < C1.b
        print("  L4: min_I W_q >= %s, m' >= %s, M' <= %s; B_0(3) <= %s, X_0(3) <= %s; with D466's C_1 <= %s "
              "(recomputed) and C_l <= 64.18 for l >= 2 the summed H^1 constant over every l >= 0 at sigma = 3 is <= %s "
              "(%.0fs)" % (dn(wI, 5), dn(m1, 5), up(M1, 5), up(B.b, 5), up(X0.b, 5), up(C1.b, 5), up(C, 5),
                           time.time() - t0), flush=True)
    w0 = fields(iv.mpf(mpf(-39) / 10), with_q=False)[0]
    gflip, _, _ = E0.certify(lambda tt: fields(tt, sign=-1)[0], tL, tR)
    neg, tneg = None, None
    for k in range(501):
        tt = mpf(-2) + mpf(5) * k / 500
        W = fields(iv.mpf(tt), sign=-1)[0]
        if neg is None or W.b < neg.b:
            neg, tneg = W, tt
    lft3, _, rh3 = tails(-3, rR)
    ok["L5 controls"] = w0.b < 0 and not gflip and neg.b < 0 and not lft3
    print("  L5: without q, w_0 <= %s at t = -3.9; with q'' at -1 the bisection fails and W <= %s at t = %s; the left "
          "tail at t = -3: rho_3 + rho_q <= %s, not certified (%.0fs)"
          % (up(w0.b, 4), up(neg.b, 4), iv.nstr(iv.mpf(tneg), 4), up(rh3[0].b, 4), time.time() - t0), flush=True)
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
