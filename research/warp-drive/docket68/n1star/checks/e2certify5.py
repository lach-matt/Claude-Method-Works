"""e2certify5.py -- E2-PILOT section 3f (D384): Lemma E2.8's hypothesis certified for every harmonic l >= 1, by interval
arithmetic (mpmath.iv) and two explicit tail bounds.

The multiplier is fixed at the photon sphere: phi_* := tanh((r_* - x_*)/s), x_* := r_*(sqrt 2), s = 49/50. With
y = 1/r^2, f = 1 - y, V_l = a U + b Q, U := f y, Q := f y^2, a = l(l+2) + 3/4, b = 9/4, and d/dr_* = f d/dr,

    U' = (2f/r^3)(2y - 1),    Q' = (2f/r^3) y (3y - 2),    w_l := -phi_* V_l' - phi_*'''/2 = w_1 + (a - a_1)(-phi_* U').

U' changes sign exactly at r = sqrt 2, where phi_* does, so -phi_* U' >= 0 on R and w_l >= w_1 for every l >= 1. So
w_1 >= 0 on R gives E2.8's hypothesis for every l >= 1, and min_I w_l >= min_I w_l0 for l >= l0 gives
B_l(sigma) <= B_l0(sigma): m' and M' do not depend on l.

  C1 w_1 >= 0 on r_* in [x(t = -120), x(r = 120)], t := ln(r - 1), by adaptive bisection in t: every subinterval's
     interval enclosure of w_1 has a non-negative lower end.
  C2 the tails: for r_* below that range, phi_*'''/2 <= (8/s^3) e^(2z) and -phi_* V_1' >= tanh|z_L| C e^(2 r_*), so the
     ratio is at most K e^(2 r_*(1/s - 1)), which decreases toward the horizon as s < 1; its value at the left end is
     certified < 1. For r_* above, the ratio is at most (8/s^3) e^(-2z) (r_* + d_R)^3/(2 a c_R tanh z_R), decreasing
     once r_* + d_R > 3s/2; its value at the right end is certified < 1.
  C3 certified lower bounds for min_I w_l at l = 1, ..., 6 (I = {r in [1.2, 4]}), enclosures of m' = min_I phi_*'
     (at an end of I) and M' <= 1/s, and so certified upper bounds for B_l(sigma) at sigma = 0+, 1, 3, 10; for l >= 6
     they bound every B_l.
  C5 for l = 1, ..., 5, the multiplier centred instead at a float near V_l's own peak (any centre is allowed: E2.8 needs
     only w >= 0): w_l >= 0 on R, certified as in C1-C2, and the constants as in C3; they are better than C3's at
     l = 1 only, so the table takes C5 at l = 1 and C3 at l = 2, ..., 5.
  C4 controls: with the centre moved to r = 1.6, -phi U' < 0 at a point between the two centres (no monotonicity);
     with s = 3/2 the left tail ratio's exponent 2(1/s - 1) is negative, so the bound grows toward the horizon; and
     C1's bisection itself must fail at l = 0 with phi_* and at l = 1 with s = 3/2, and a point enclosure there must
     be negative (D385).
Away from the centre (|z| > 3) sech^2 is computed from e^(-2|z|), so that 1 - tanh^2 is never formed: at t = -72 it
is below 30 digits. Every subdivision endpoint is carried at iv's 103 bits (mp.prec = iv.prec), so the pieces cover
the range exactly, and every printed decimal is rounded outward from the enclosure's end (an upper bound up, a lower
bound down) by exact rational arithmetic (D385). Labels: certified (interval arithmetic, outward rounding, 30
digits), given mpmath.iv's correctness; the analytic steps (the monotonicity in a, the tail inequalities) are proved
in E2-PILOT section 3f.

    python3 checks/e2certify5.py [--selftest]
"""
import math
import sys
import time
from fractions import Fraction

from mpmath import iv, mp, mpf

iv.dps = 30
mp.prec = iv.prec          # an iv endpoint converts to mpf exactly (D385)
S = iv.mpf(49)/50
A_ = lambda l: iv.mpf(l*(l + 2)) + iv.mpf(3)/4
B_ = iv.mpf(9)/4


def xr(tt):
    """r_* as a function of t = ln(r - 1), for an interval tt"""
    e = iv.exp(tt)
    return 1 + e + (tt - iv.log(2 + e))/2


T_C = iv.log(iv.sqrt(2) - 1)
X_C = xr(T_C)


def tanh_of(z):
    E = iv.exp(2*z)
    return 1 - 2/(E + 1)


def parts(tt, s=S, xc=X_C):
    e = iv.exp(tt)
    r = 1 + e
    y = 1/r**2
    f = e*(2 + e)/r**2
    z = (xr(tt) - xc)/s
    T = tanh_of(z)
    if z.b < -3 or z.a > 3:
        # away from the centre: sech^2 from e^(-2|z|), so 1 - tanh^2 is never formed (it cancels below 30 digits)
        E = iv.exp(2*z) if z.b < 0 else iv.exp(-2*z)
        sech2 = 4*E/(1 + E)**2
        ph1 = sech2/s
        ph3 = -(2/s**3)*sech2*(3*sech2 - 2)
    else:
        P = T**2
        ph1 = (1 - P)/s
        ph3 = -(2/s**3)*(3*(P - iv.mpf(2)/3)**2 - iv.mpf(1)/3)
    Up = (2*f/r**3)*(2*y - 1)
    Qp = (2*f/r**3)*y*(3*y - 2)
    return T, ph1, ph3, Up, Qp


def w_of(tt, a, s=S, xc=X_C):
    T, ph1, ph3, Up, Qp = parts(tt, s, xc)
    return -T*(a*Up + B_*Qp) - ph3/2


def dec(x, sig, up):
    """x (an mpf or a point interval) as a decimal of sig significant digits, rounded up or down exactly"""
    sign, man, ex, _ = mpf(x)._mpf_
    q = Fraction(-man if sign else man)*Fraction(2)**ex
    if q == 0:
        return "0"
    e = math.floor(math.log10(abs(float(q))))
    k = sig - 1 - e
    sc = q*Fraction(10)**k
    n = math.ceil(sc) if up else math.floor(sc)
    neg, d = n < 0, str(abs(n))
    if k > 8 or k < -8:
        out = "%s.%se%d" % (d[0], d[1:], len(d) - 1 - k) if len(d) > 1 else "%se%d" % (d, -k)
    elif k > 0:
        d = d.rjust(k + 1, "0")
        out = d[:-k] + "." + d[-k:]
    else:
        out = d + "0"*(-k)
    return ("-" if neg else "") + out


def certify_positive(a, t0, t1, minw=mpf("1e-9"), s=S, xc=X_C):
    """endpoints exact at 103 bits; a split shares its midpoint, so the accepted pieces cover [t0, t1]"""
    stack, n, acc = [(mpf(t0), mpf(t1))], 0, 0
    while stack:
        lo, hi = stack.pop()
        val = w_of(iv.mpf([lo, hi]), a, s, xc)
        n += 1
        if val.a >= 0:
            acc += 1
            continue
        if hi - lo < minw:
            return False, (n, acc), (lo, hi, val)
        mid = (lo + hi)/2
        stack += [(lo, mid), (mid, hi)]
    return True, (n, acc), None


def min_lower(a, t0, t1, pieces, s=S, xc=X_C):
    """the first and last endpoints are t0 and t1 exactly, and consecutive pieces share theirs"""
    t0, t1 = mpf(t0), mpf(t1)
    ends = [t0] + [t0 + (t1 - t0)*k/pieces for k in range(1, pieces)] + [t1]
    lo = None
    for ta, tb in zip(ends[:-1], ends[1:]):
        v = w_of(iv.mpf([ta, tb]), a, s, xc).a
        lo = v if lo is None or v < lo else lo
    return lo


def tail_left(a, tL, s=S, xc=X_C):
    """bound of (phi'''/2)/(-phi V') at r_* = x(tL), valid and decreasing for all r_* below it (needs s < 1)"""
    eL = iv.exp(iv.mpf(tL))
    rL = 1 + eL
    XL = xr(iv.mpf(tL))
    zL = (XL - xc)/s
    th = -tanh_of(zL)                       # tanh|z_L|, z_L < 0
    eps = 6*eL
    C = 8*(a + B_)*(1 - eps)*iv.exp(-2*rL)/rL**5
    K = 8*iv.exp(-2*xc/s)/(s**3*th*C)
    return K*iv.exp(2*XL*(1/s - 1)), (1/s - 1)


def tail_right(a, rR, s=S, xc=X_C):
    """bound of the ratio at r = rR, valid and decreasing for all larger r once r_* + d_R > 3s/2"""
    rR = iv.mpf(rR)
    XR = xr(iv.log(rR - 1))
    dR = -iv.log((rR - 1)/(rR + 1))/2
    zR = (XR - xc)/s
    th = tanh_of(zR)
    cR = (1 - 1/rR**2)*(1 - 2/rR**2)
    g = (8/s**3)*iv.exp(-2*zR)*(XR + dR)**3/(2*a*cR*th)
    return g, XR + dR - 3*s/2


def b_bound(wlo, m1lo, M1hi, sigma):
    return iv.sqrt((2/m1lo + (M1hi + 2*sigma)**2/wlo)/wlo)


def run(verbose=True):
    t0 = time.time()
    ok = {}
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    good, (n, acc), bad = certify_positive(A_(1), tL, tR)
    ok["C1"] = good
    if verbose:
        print("  C1: w_1 >= 0 on t in [%d, ln %d]: %s, %d enclosures evaluated, %d pieces accepted (%.0fs)%s"
              % (tL, rR - 1, good, n, acc, time.time() - t0, "" if good else "  failed at %s" % (bad,)), flush=True)
    rhoL, expo = tail_left(A_(1), tL)
    rhoR, mono = tail_right(A_(1), rR)
    ok["C2"] = rhoL.b < 1 and expo.a > 0 and rhoR.b < 1 and mono.a > 0
    if verbose:
        print("  C2: left tail ratio <= %s (exponent 2(1/s - 1) >= %s); right tail ratio <= %s" %
              (dec(rhoL.b, 4, True), dec((2*expo).a, 4, False), dec(rhoR.b, 3, True)), flush=True)
    tIa, tIb = iv.log(iv.mpf("0.2")).a, iv.log(iv.mpf(3)).b
    ph1a = parts(iv.mpf(tIa))[1]
    ph1b = parts(iv.mpf(tIb))[1]
    m1lo = min(ph1a.a, ph1b.a)
    M1hi = (1/S).b
    rows = []
    for l in range(1, 7):
        wlo = min_lower(A_(l), tIa, tIb, 2000)
        bs = [b_bound(iv.mpf(wlo), m1lo, M1hi, sg).b if wlo > 0 else None for sg in (0, 1, 3, 10)]
        rows.append((l, wlo, bs))
        if verbose:
            print("  C3: l = %d  min_I w_l >= %s  B_l(0+, 1, 3, 10) <= %s" %
                  (l, dec(wlo, 5, False), ", ".join("-" if b is None else dec(b, 4, True) for b in bs)), flush=True)
    ok["C3"] = all(w > 0 for _, w, _ in rows) and m1lo > 0
    if verbose:
        print("  C3: m' >= %s (an end of I), M' <= %s" % (dec(m1lo, 4, False), dec(M1hi, 6, True)))
    ok["C5"] = True
    for l in range(1, 6):
        import numpy as np
        tg = np.linspace(-3, 1.5, 20001)
        rg = 1 + np.exp(tg)
        yg = 1/rg**2
        vg = (1 - yg)*((l*(l + 2) + 0.75)*yg + 2.25*yg*yg)
        tp = float(tg[np.argmax(vg)])
        xc = xr(iv.mpf(tp))
        good, (n, _), _ = certify_positive(A_(l), tL, tR, xc=xc)
        rl, el = tail_left(A_(l), tL, xc=xc)
        rr, mr = tail_right(A_(l), rR, xc=xc)
        wlo = min_lower(A_(l), tIa, tIb, 2000, xc=xc)
        m1 = min(parts(iv.mpf(tIa), S, xc)[1].a, parts(iv.mpf(tIb), S, xc)[1].a)
        good = good and rl.b < 1 and el.a > 0 and rr.b < 1 and mr.a > 0 and wlo > 0
        ok["C5"] = ok["C5"] and good
        if verbose:
            bs = [b_bound(iv.mpf(wlo), m1, M1hi, sg).b for sg in (0, 1, 3, 10)] if wlo > 0 else []
            print("  C5: l = %d centre r = %.4f: w >= 0 %s (%d enclosures), min_I w >= %s, B_l(0+, 1, 3, 10) <= %s"
                  % (l, 1 + float(iv.exp(iv.mpf(tp)).a), good, n, dec(wlo, 5, False),
                     ", ".join(dec(b, 4, True) for b in bs)), flush=True)
    xc2 = xr(iv.log(iv.mpf("1.6") - 1))
    tm = iv.log(iv.mpf("1.5") - 1)
    T, _, _, Up, _ = parts(tm, S, xc2)
    neg = (-T*Up).b < 0
    _, expo15 = tail_left(A_(1), tL, iv.mpf(3)/2)
    f0, _, bad0 = certify_positive(A_(0), tL, tR)
    f15, _, bad15 = certify_positive(A_(1), tL, tR, s=iv.mpf(3)/2)
    n0 = w_of(iv.mpf("0.8"), A_(0))                          # a certified negative value, not only a failed split
    n15 = w_of(iv.mpf(-8), A_(1), s=iv.mpf(3)/2)
    ok["C4 controls"] = neg and expo15.b < 0 and not f0 and not f15 and n0.b < 0 and n15.b < 0
    if verbose:
        print("  C4: centre at r = 1.6: -phi U' at r = 1.5 is %s; s = 3/2: exponent %s" %
              (iv.nstr(-T*Up, 4), iv.nstr(2*expo15, 4)))
        print("  C4: C1's bisection fails, as it must, at l = 0 with phi_* (near t = %s; w_0 <= %s at t = 0.8) and at "
              "l = 1 with s = 3/2 (near t = %s; w_1 <= %s at t = -8)" % (iv.nstr(iv.mpf(bad0[0]), 5), dec(n0.b, 4, True),
                                                                     iv.nstr(iv.mpf(bad15[0]), 5), dec(n15.b, 4, True)))
        print("  (%.0fs)" % (time.time() - t0))
    return ok, rows


def main():
    ok, _ = run()
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
