#!/usr/bin/env python3
"""e2asymcert5.py -- E2-PILOT section 3i (D466): D460's asymmetric multiplier certified for every l >= 1.

D460 computed in floating point that a multiplier narrow toward the horizon and wide outside lowers the summed cut-off
H^1 constant at sigma = 3 from 808.6 to 184.2. Here its l >= 1 half is certified by interval arithmetic (mpmath.iv),
as section 3f did for the symmetric multiplier. The width is interpolated harmonically, so that g has a closed form:

    phi = tanh(g),  g' = 1/s_R + D (1 - sig(z)),  z = (r_* - x_*)/kap,  sig(z) = 1/(1 + e^-z),  D = 1/s_L - 1/s_R,
    g = (r_* - x_*)/s_R + D ((r_* - x_*) - kap (L(z) - ln 2)),  L(z) = ln(1 + e^z),

with s_L = 49/50 (toward the horizon), s_R = 2 (outside), kap = 1/2 and x_* = r_*(sqrt 2), so g(x_*) = 0 and phi
changes sign exactly where U' does. Then, as in section 3f, w_l = w_1 + (a - a_1)(-phi U') >= w_1 for every l >= 1,
and m', M' do not depend on l.

  K1 w_1 >= 0 on t in [-120, ln 119], t = ln(r - 1), by adaptive bisection (every piece's enclosure non-negative).
  K2 the tails. Below the range, |phi'''| <= S (|g'''| + 6 g' |g''| + 6 g'^3) with S = sech^2 g <= 4 e^(2g), g <= (r_* -
     x_*)/s_L + D kap ln 2, g' <= 1/s_L and |g''|, |g'''| <= D e^z/kap, D e^z/kap^2, while -phi V' >= tanh|g_L| C e^(2
     r_*) (section 3f's C): the ratio of phi'''/2 to -phi V' is at most K e^(2 r_*(1/s_L - 1)), decreasing toward the
     horizon, and certified < 1 at the range's end. Above the range, g >= (r_* - x_*)/s_R and g' <= 1/s_R + D e^-z, so
     the ratio is at most G e^(-2 r_*/s_R) (r_* + d_R)^3, decreasing once r_* + d_R > 3 s_R/2, and certified < 1 at r =
     120.
  K0 the closed forms of phi, phi' and phi''' agree with mpmath's numerical derivatives of tanh(g) at five points to
     twelve digits (computed).
  K3 on I = {r in [1.2, 4]}, over 2000 pieces: m' = min_I phi' and M' = max_I phi' (enclosed, not assumed at an end),
     and min_I w_l for l = 1, ..., 6; then B_l(3), X_l(3), A_l = l(l + 2) K_l/(a - a_1) (A_1 = 3 B_1^2),
     C_l = (X_l^2 + A_l)^(1/2), all rounded outward, and their maximum. Every l >= 6 is bounded by l = 6: w_l >= w_6 on
     I (w_l increases with l), B, X and K decrease as w_I grows, and l(l + 2)/(a - a_1) = 1 + 3/(l(l + 2) - 3)
     decreases (checked for l = 2, ..., 7, and plain for every l); so C_l <= C_6 (verifier 200, D469).
  K4 controls: K1's bisection fails, as it must, at l = 0 (which needs section 3g's q), and w_0 is certified negative at
     t = -3.9, on the horizon side (D462); with the centre at r = 1.6 the product -phi U' is negative at r = 1.5 (no
     monotonicity in l). The tail bounds and the constants step fail where they should (D469, verifier 200): the left
     tail's ratio bound exceeds 1 at t = -3 and the right tail's at r = 2.5, where it is not monotone either, so neither
     certifies without K1's range; and K3's pipeline refuses l = 0, as its enclosure of min_I w_0 is not positive.

The angular weight is this multiplier's, -phi U', not section 3i's psi_*: D462 measured it at 0.64-0.94 times psi_* on
I. Labels: K1-K3 certified (interval arithmetic and explicit tail bounds); the corollary deduced as in section 3i.

    python3 checks/e2asymcert5.py
"""
import math
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

iv.dps = 30
mp.prec = iv.prec
SL, SR, KAP = iv.mpf(49) / 50, iv.mpf(2), iv.mpf(1) / 2
DD = 1 / SL - 1 / SR
LN2 = iv.log(2)
A_ = lambda l: iv.mpf(l * (l + 2)) + iv.mpf(3) / 4
B_ = iv.mpf(9) / 4
SIGMA = iv.mpf(3)


def xr(tt):
    e = iv.exp(tt)
    return 1 + e + (tt - iv.log(2 + e)) / 2


T_C = iv.log(iv.sqrt(2) - 1)
X_C = xr(T_C)


def softplus(z):
    if z.a > 0:
        return z + iv.log(1 + iv.exp(-z))
    return iv.log(1 + iv.exp(z))


def mult(x, sL=SL, sR=SR, xc=X_C):
    """phi, phi', phi''' at r_* = x (an interval)"""
    D = 1 / sL - 1 / sR
    z = (x - xc) / KAP
    if z.a > 0:
        em = iv.exp(-z); sg = 1 / (1 + em); om = em / (1 + em)
    else:
        ep = iv.exp(z); sg = ep / (1 + ep); om = 1 / (1 + ep)
    g1 = 1 / sR + D * om
    g2 = -D * sg * om / KAP
    g3 = -D * sg * om * (om - sg) / KAP**2
    g = (x - xc) / sR + D * ((x - xc) - KAP * (softplus(z) - LN2))
    if g.b < -3 or g.a > 3:
        E = iv.exp(2 * g) if g.b < 0 else iv.exp(-2 * g)
        S = 4 * E / (1 + E)**2
        T = (E - 1) / (E + 1) if g.b < 0 else (1 - E) / (1 + E)
    else:
        E = iv.exp(2 * g)
        T = 1 - 2 / (E + 1)
        S = 1 - T**2
    p1 = g1 * S
    p3 = g3 * S - 6 * g1 * g2 * T * S - 2 * g1**3 * S**2 + 4 * g1**3 * T**2 * S
    return T, p1, p3


def pots(tt):
    e = iv.exp(tt)
    r = 1 + e
    y = 1 / r**2
    f = e * (2 + e) / r**2
    return (2 * f / r**3) * (2 * y - 1), (2 * f / r**3) * y * (3 * y - 2)


def w_of(tt, a, **kw):
    T, _, p3 = mult(xr(tt), **kw)
    Up, Qp = pots(tt)
    return -T * (a * Up + B_ * Qp) - p3 / 2


def certify_positive(a, t0, t1, minw=mpf("1e-9"), **kw):
    stack, n = [(mpf(t0), mpf(t1))], 0
    while stack:
        lo, hi = stack.pop()
        val = w_of(iv.mpf([lo, hi]), a, **kw)
        n += 1
        if val.a >= 0:
            continue
        if hi - lo < minw:
            return False, n, (lo, hi, val)
        mid = (lo + hi) / 2
        stack += [(lo, mid), (mid, hi)]
    return True, n, None


def tail_left(a, tL):
    eL = iv.exp(iv.mpf(tL)); rL = 1 + eL; XL = xr(iv.mpf(tL))
    gL = (XL - X_C) / SL + DD * KAP * LN2                      # an upper bound for g there, and g(XL) < 0
    th = -(1 - 2 / (iv.exp(2 * gL) + 1))                       # tanh|g_L| from below (tanh increasing, gL < 0)
    eps = 6 * eL
    C = 8 * (a + B_) * (1 - eps) * iv.exp(-2 * rL) / rL**5    # V' >= C e^(2 r_*) below (section 3f)
    pre = 4 * iv.exp(2 * (-X_C / SL + DD * KAP * LN2))
    ezc = iv.exp(-X_C / KAP)                                   # e^z = e^(r_*/kap) e^(-x_*/kap) <= e^(2 r_*) ezc
    # S (|g'''| + 6 g'|g''| + 6 g'^3)/2 <= pre e^(2 r_*/s_L) (D ezc e^(2 r_*)/kap^2 + 6 D ezc e^(2 r_*)/(s_L kap)
    #                                     + 6/s_L^3)/2; at r_* <= XL the e^(2 r_*) terms are at most their value at XL
    e2 = iv.exp(2 * XL)
    num = pre * (DD * ezc * e2 / KAP**2 + 6 * DD * ezc * e2 / (SL * KAP) + 6 / SL**3) / 2
    K = num / (th * C)
    return K * iv.exp(2 * XL * (1 / SL - 1)), (1 / SL - 1)


def tail_right(a, rR):
    rR = iv.mpf(rR)
    XR = xr(iv.log(rR - 1))
    dR = -iv.log((rR - 1) / (rR + 1)) / 2
    zR = (XR - X_C) / KAP
    em = iv.exp(-zR)
    g1 = 1 / SR + DD * em
    gR = (XR - X_C) / SR                                       # g >= this for r_* >= x_*
    th = 1 - 2 / (iv.exp(2 * gR) + 1)
    cR = (1 - 1 / rR**2) * (1 - 2 / rR**2)
    num = 4 * iv.exp(-2 * gR) * (DD * em / KAP**2 + 6 * g1 * DD * em / KAP + 6 * g1**3) / 2
    ratio = num * (XR + dR)**3 / (2 * a * cR * th)
    return ratio, XR + dR - 3 * SR / 2


def enclose_I(fn, pieces=2000):
    tIa, tIb = iv.log(iv.mpf("0.2")).a, iv.log(iv.mpf(3)).b
    ends = [mpf(tIa) + (mpf(tIb) - mpf(tIa)) * k / pieces for k in range(pieces)] + [mpf(tIb)]
    lo = hi = None
    for ta, tb in zip(ends[:-1], ends[1:]):
        v = fn(iv.mpf([ta, tb]))
        lo = v.a if lo is None or v.a < lo else lo
        hi = v.b if hi is None or v.b > hi else hi
    return lo, hi


def k0():
    mp.dps = 40
    xc = mpf(X_C.a)
    D = 1 / mpf(SL.a) - 1 / mpf(SR.a)
    kap = mpf(KAP.a)
    g = lambda x: (x - xc) / mpf(SR.a) + D * ((x - xc) - kap * (mp.log(1 + mp.exp((x - xc) / kap)) - mp.log(2)))
    phi = lambda x: mp.tanh(g(x))
    worst = 0
    for x in (mpf(-5), mpf("0.3"), mpf("0.53"), mpf(2), mpf(6)):
        T, p1, p3 = mult(iv.mpf([x, x]))
        for a, b in ((phi(x), T), (mp.diff(phi, x), p1), (mp.diff(phi, x, 3), p3)):
            worst = max(worst, abs(a - mpf(b.a)) / (abs(a) + mpf(10)**-30))
    mp.prec = iv.prec
    return worst


def main():
    t0 = time.time()
    ok = {}
    wk = k0()
    ok["K0"] = wk < mpf(10)**-12
    print("  K0: phi, phi', phi''' against numerical derivatives at five points: worst relative difference %s"
          % mp.nstr(wk, 3), flush=True)
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    good, n, bad = certify_positive(A_(1), tL, tR)
    ok["K1"] = good
    print("  K1: w_1 >= 0 on t in [%d, ln %d]: %s, %d enclosures (%.0fs)%s"
          % (tL, rR - 1, good, n, time.time() - t0, "" if good else "  failed at %s" % (bad,)), flush=True)
    rl, el = tail_left(A_(1), tL)
    rr, mr = tail_right(A_(1), rR)
    ok["K2"] = rl.b < 1 and el.a > 0 and rr.b < 1 and mr.a > 0
    print("  K2: left tail ratio <= %s (exponent 2(1/s_L - 1) >= %s); right tail ratio <= %s, monotone from %s"
          % (up(rl.b, 4), dn((2 * el).a, 4), up(rr.b, 3), dn(mr.a, 3)), flush=True)
    m1lo, _ = enclose_I(lambda tt: mult(xr(tt))[1])
    _, M1hi = enclose_I(lambda tt: mult(xr(tt))[1])
    c = iv.mpf(M1hi) + 2 * SIGMA
    a1 = A_(1)
    Cmax, rows = None, []
    for l in range(1, 7):
        wlo, _ = enclose_I(lambda tt, l=l: w_of(tt, A_(l)))
        if wlo <= 0:
            rows.append((l, wlo, None)); continue
        w = iv.mpf(wlo); m = iv.mpf(m1lo)
        B = iv.sqrt((2 / m + c**2 / w) / w)
        X = (1 + iv.sqrt(1 + 2 * m * c * B)) / (2 * m)
        K = 2 * X + c * B
        A = 3 * B**2 if l == 1 else iv.mpf(l * (l + 2)) * K / (A_(l) - a1)
        Cl = iv.sqrt(X**2 + A)
        rows.append((l, wlo, (B.b, X.b, A.b, Cl.b)))
        Cmax = Cl.b if Cmax is None or Cl.b > Cmax else Cmax
        print("  K3: l = %d  min_I w_l >= %s  B_l(3) <= %s  X_l(3) <= %s  A_l <= %s  C_l <= %s"
              % (l, dn(wlo, 5), up(B.b, 5), up(X.b, 5), up(A.b, 6), up(Cl.b, 5)), flush=True)
    fac = [iv.mpf(l * (l + 2)) / (A_(l) - a1) for l in range(2, 8)]      # 1 + 3/(l(l + 2) - 3), decreasing
    ok["K3"] = all(r[2] is not None for r in rows) and m1lo > 0 and all(fac[k + 1].b < fac[k].a for k in range(5))
    print("  K3: m' >= %s, M' <= %s on I; over l >= 1, C <= %s at sigma = 3 (certified symmetric: 675.1 over l >= 1)"
          % (dn(m1lo, 5), up(M1hi, 5), up(Cmax, 5)), flush=True)
    f0, _, bad0 = certify_positive(A_(0), tL, tR)
    n0 = w_of(iv.mpf(mpf(-39) / 10), A_(0))                     # a certified negative value (the horizon side)
    xc2 = xr(iv.log(iv.mpf("1.6") - 1))
    tm = iv.log(iv.mpf("1.5") - 1)
    T2, _, _ = mult(xr(tm), xc=xc2)
    neg = (-T2 * pots(tm)[0]).b < 0
    rl3, _ = tail_left(A_(1), -3)
    rr25, mr25 = tail_right(A_(1), mpf("2.5"))
    w0lo, _ = enclose_I(lambda tt: w_of(tt, A_(0)), pieces=400)
    ok["K4 controls"] = (not f0) and n0 is not None and n0.b < 0 and neg and rl3.a > 1 and rr25.a > 1 \
        and mr25.b < 0 and w0lo <= 0
    print("  K4: tails fail where they should: left ratio at t = -3 >= %s, right ratio at r = 2.5 >= %s (monotone from "
          "%s); K3's pipeline refuses l = 0 (min_I w_0 enclosed from %s)"
          % (dn(rl3.a, 4), dn(rr25.a, 4), up(mr25.b, 3), dn(w0lo, 4)),
          flush=True)
    print("  K4: at l = 0 the bisection fails (near t = %s) and w_0 <= %s at t = -3.9; centre at r = 1.6: -phi U' at "
          "r = 1.5 is %s (%.0fs)" % (iv.nstr(iv.mpf(bad0[0]), 5) if bad0 else "-", iv.nstr(iv.mpf(n0.b), 4),
                                    iv.nstr(-T2 * pots(tm)[0], 4), time.time() - t0), flush=True)
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
