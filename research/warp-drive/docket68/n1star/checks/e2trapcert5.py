#!/usr/bin/env python3
"""e2trapcert5.py -- E2-PILOT section 3j (D497): section 3j's bound at sigma = 3, certified for every l >= 0.

Section 3j (D486, D493) computed, in floating point, that at sigma = 3 the sup over l of min(Lemma E2.7, Lemma E2.8
with a core-and-flank multiplier) is 10.98, set by l = 5 with the multiplier

    phi = tanh g,  g' = 1/s_R + (1/s_L - 1/s_R)/(1 + e^z) + beta sech^2((r_* - x_*)/kappa),  z = (r_* - x_*)/kappa_s,

s_L = 49/50, s_R = 4, kappa_s = 1/2, core width s_c = 1/g'(x_*) and kappa = s_c, centred at x_* = r_*(2^(1/2)). Here the
rational multiplier s_c = 10174/10000 (the program's choice to four digits; the certificate checks this one) is certified
by interval arithmetic (mpmath.iv, e2asymcert5's helpers), and with it the bound:

  C0 the closed forms of phi, phi', phi''' agree with mpmath's numerical derivatives of tanh(g) (computed).
  C1 w_5 = -phi V_5' - phi'''/2 >= 0 on t = ln(r - 1) in [-120, ln 119], by adaptive bisection.
  C2 the tails, by e2asymcert5's bounds with the core's terms added: below the range g <= the flank's g (the core term is
     negative there) and the core adds at most 4 beta e^(2y), 8 beta e^(2y)/kappa, 24 beta e^(2y)/kappa^2 to g', |g''|,
     |g'''| (y = (r_* - x_*)/kappa), each at most its value at the range's end; above it g >= (r_* - x_*)/s_R (the core
     term is positive there) and the core's terms are at most their values at r = 120, all decreasing outward. Both
     ratios certified < 1, decreasing away from the range.
  C3 monotone in l: -phi U' >= 0 on R (phi and U' change sign together at x_*), so w_l = w_5 + (a_l - a_5)(-phi U')
     >= w_5 for l >= 5: the multiplier is admissible for every l >= 5, w_I does not decrease, and B_l(3) <= B_5(3).
  C4 on I = {r in [1.2, 4]}, 8000 pieces: m' = min_I phi', M' = max_I phi', min_I w_5, and B_5(3) = ((2/m' + (M' +
     6)^2/w_I)/w_I)^(1/2), rounded up.
  C5 Lemma E2.7 for l = 0, ..., 4 (sigma^2 = 9 > max V_l, max V_l exact from the quadratic in y = 1/r^2): Lambda sigma/
     (sigma^2 - max V_l) with Lambda = r_*(4) - r_*(1.2), in intervals; and max V_5 > 9 (l = 5 is not above the barrier).
  So, certified: at sigma = 3, for every l >= 0, ||chi_I R_l(3) chi_I|| <= max(C5's values, B_5(3)).
  Controls: C1's bisection fails at l = 1 (the multiplier needs a larger a than a_1); the left tail's ratio bound
     exceeds 1 at t = -2 and the right's at r = 2.5 (so neither certifies without C1's range).

Labels: C1-C5 certified (interval arithmetic, explicit tail bounds, outward rounding); C0 computed. Lemmas E2.7 and E2.8
as in sections 3c and 3e (verifier 207, D493: E2.8's proof uses only phi in C^3, phi' >= 0, |phi| <= 1 on I, phi(+-inf)
= +-1 and phi', phi'' -> 0, which this multiplier has).

    python3 checks/e2trapcert5.py
"""
import sys
import time

from mpmath import iv, mp, mpf

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import e2asymcert5 as E  # noqa: E402

iv.dps = 30
mp.prec = iv.prec
SL, SR, KS = iv.mpf(49) / 50, iv.mpf(4), iv.mpf(1) / 2
SC = iv.mpf(10174) / 10000
DD = 1 / SL - 1 / SR
BETA = 1 / SC - (1 / SR + DD / 2)
KC = SC
X_C, LN2, B_, A_, xr, pots = E.X_C, E.LN2, E.B_, E.A_, E.xr, E.pots
SIGMA = iv.mpf(3)


def th_sech(y):
    """(tanh y, sech^2 y) for an interval y, stable at both ends"""
    if y.b < -3 or y.a > 3:
        Ey = iv.exp(2 * y) if y.b < 0 else iv.exp(-2 * y)
        S = 4 * Ey / (1 + Ey)**2
        T = (Ey - 1) / (Ey + 1) if y.b < 0 else (1 - Ey) / (1 + Ey)
    else:
        Ey = iv.exp(2 * y)
        T = 1 - 2 / (Ey + 1)
        S = 1 - T**2
    return T, S


def mult(x):
    """phi, phi', phi''' at r_* = x (an interval): e2asymcert5's flank with s_R = 4, plus the core"""
    z = (x - X_C) / KS
    if z.a > 0:
        em = iv.exp(-z); sg = 1 / (1 + em); om = em / (1 + em)
    else:
        ep = iv.exp(z); sg = ep / (1 + ep); om = 1 / (1 + ep)
    g1 = 1 / SR + DD * om
    g2 = -DD * sg * om / KS
    g3 = -DD * sg * om * (om - sg) / KS**2
    g = (x - X_C) / SR + DD * ((x - X_C) - KS * (E.softplus(z) - LN2))
    ty, sy = th_sech((x - X_C) / KC)
    g = g + BETA * KC * ty
    g1 = g1 + BETA * sy
    g2 = g2 - 2 * BETA / KC * sy * ty
    g3 = g3 - 2 * BETA / KC**2 * (sy**2 - 2 * sy * ty**2)
    T, S = th_sech(g)
    p1 = g1 * S
    p3 = g3 * S - 6 * g1 * g2 * T * S - 2 * g1**3 * S**2 + 4 * g1**3 * T**2 * S
    return T, p1, p3


def w_of(tt, a):
    T, _, p3 = mult(xr(tt))
    Up, Qp = pots(tt)
    return -T * (a * Up + B_ * Qp) - p3 / 2


def certify_positive(a, t0, t1, minw=mpf("1e-9")):
    stack, n = [(mpf(t0), mpf(t1))], 0
    while stack:
        lo, hi = stack.pop()
        val = w_of(iv.mpf([lo, hi]), a)
        n += 1
        if val.a >= 0:
            continue
        if hi - lo < minw:
            return False, n, (lo, hi, val)
        mid = (lo + hi) / 2
        stack += [(lo, mid), (mid, hi)]
    return True, n, None


def tail_left(a, tL):
    """the ratio (|phi'''|/2)/(-phi V') for t <= tL is at most K e^(2 r_*(1/s_L - 1)) <= the value returned"""
    eL = iv.exp(iv.mpf(tL)); rL = 1 + eL; XL = xr(iv.mpf(tL))
    gL = (XL - X_C) / SL + DD * KS * LN2                       # the flank's g bounds g above; the core term is < 0
    th = -(1 - 2 / (iv.exp(2 * gL) + 1))
    eps = 6 * eL
    C = 8 * (a + B_) * (1 - eps) * iv.exp(-2 * rL) / rL**5
    pre = 4 * iv.exp(2 * (-X_C / SL + DD * KS * LN2))
    ezc = iv.exp(-X_C / KS)
    e2 = iv.exp(2 * XL)
    ey = iv.exp(2 * (XL - X_C) / KC)                           # e^(2y) at the range's end, increasing in r_*
    g1m = 1 / SL + 4 * BETA * ey
    g2m = DD * ezc * e2 / KS + 8 * BETA * ey / KC
    g3m = DD * ezc * e2 / KS**2 + 24 * BETA * ey / KC**2
    num = pre * (g3m + 6 * g1m * g2m + 6 * g1m**3) / 2
    K = num / (th * C)
    return K * iv.exp(2 * XL * (1 / SL - 1)), (1 / SL - 1)


def tail_right(a, rR):
    rR = iv.mpf(rR)
    XR = xr(iv.log(rR - 1))
    dR = -iv.log((rR - 1) / (rR + 1)) / 2
    zR = (XR - X_C) / KS
    em = iv.exp(-zR)
    ey = iv.exp(-2 * (XR - X_C) / KC)                          # e^(-2y) at r = rR, decreasing outward
    g1 = 1 / SR + DD * em + 4 * BETA * ey
    g2 = DD * em / KS + 8 * BETA * ey / KC
    g3 = DD * em / KS**2 + 24 * BETA * ey / KC**2
    gR = (XR - X_C) / SR                                       # g >= this for r_* >= x_* (the core term is > 0)
    th = 1 - 2 / (iv.exp(2 * gR) + 1)
    cR = (1 - 1 / rR**2) * (1 - 2 / rR**2)
    num = 4 * iv.exp(-2 * gR) * (g3 + 6 * g1 * g2 + 6 * g1**3) / 2
    ratio = num * (XR + dR)**3 / (2 * a * cR * th)
    return ratio, XR + dR - 3 * SR / 2


def k0():
    mp.dps = 40
    xc, D, ks, kc = mpf(X_C.a), 1 / mpf(SL.a) - 1 / mpf(SR.a), mpf(KS.a), mpf(KC.a)
    beta = mpf(BETA.a)
    g = lambda x: (x - xc) / mpf(SR.a) + D * ((x - xc) - ks * (mp.log(1 + mp.exp((x - xc) / ks)) - mp.log(2))) \
        + beta * kc * mp.tanh((x - xc) / kc)
    phi = lambda x: mp.tanh(g(x))
    worst = 0
    for x in (mpf(-5), mpf("0.3"), mpf("0.53"), mpf(2), mpf(6)):
        T, p1, p3 = mult(iv.mpf([x, x]))
        for a, b in ((phi(x), T), (mp.diff(phi, x), p1), (mp.diff(phi, x, 3), p3)):
            worst = max(worst, abs(a - mpf(b.a)) / (abs(a) + mpf(10)**-30))
    mp.prec = iv.prec
    return worst


def vmax(l):
    a, b = A_(l), B_
    y = (-(2 * a - 2 * b) + iv.sqrt((2 * a - 2 * b)**2 + 12 * a * b)) / (6 * b)
    return (1 - y) * (a * y + b * y * y)


def main():
    t0 = time.time()
    ok = {}
    wk = k0()
    ok["C0"] = wk < mpf(10)**-12
    print("  C0: phi, phi', phi''' against numerical derivatives at five points: worst relative difference %s; beta = %s"
          % (mp.nstr(wk, 3), iv.nstr(BETA, 8)), flush=True)
    tL, rR = -120, 120
    tR = iv.log(iv.mpf(rR) - 1).b
    good, n, bad = certify_positive(A_(5), tL, tR)
    ok["C1"] = good
    print("  C1: w_5 >= 0 on t in [%d, ln %d]: %s, %d enclosures (%.0fs)%s"
          % (tL, rR - 1, good, n, time.time() - t0, "" if good else "  failed at %s" % (bad,)), flush=True)
    rl, el = tail_left(A_(5), tL)
    rr, mr = tail_right(A_(5), rR)
    ok["C2"] = rl.b < 1 and el.a > 0 and rr.b < 1 and mr.a > 0
    print("  C2: left tail ratio <= %s (exponent 2(1/s_L - 1) >= %s); right tail ratio <= %s, monotone from %s"
          % (E.up(rl.b, 4), E.dn((2 * el).a, 4), E.up(rr.b, 3), E.dn(mr.a, 3)), flush=True)
    # C3: -phi U' >= 0 everywhere: U' = (2 f/r^3)(2y - 1) changes sign only at r^2 = 2, and g(x_*) = 0 with g' > 0
    gmin = min(1 / SR, 1 / SL).a                                # g' >= the flank's least slope > 0 (beta > 0)
    ok["C3"] = BETA.a > 0 and gmin > 0
    print("  C3: beta > 0 and g' >= %s > 0, so phi and U' change sign together at x_*: -phi U' >= 0, and the multiplier "
          "certified at l = 5 is admissible for every l >= 5 with B_l(3) <= B_5(3)" % E.dn(gmin, 4))
    m1lo, M1hi = E.enclose_I(lambda tt: mult(xr(tt))[1], pieces=8000)
    wlo, _ = E.enclose_I(lambda tt: w_of(tt, A_(5)), pieces=8000)
    c = iv.mpf(M1hi) + 2 * SIGMA
    w, m = iv.mpf(wlo), iv.mpf(m1lo)
    B5 = iv.sqrt((2 / m + c**2 / w) / w)
    ok["C4"] = m1lo > 0 and wlo > 0
    print("  C4: on I: m' >= %s, M' <= %s, min_I w_5 >= %s; B_5(3) <= %s (section 3j's float value 10.98)"
          % (E.dn(m1lo, 5), E.up(M1hi, 5), E.dn(wlo, 5), E.up(B5.b, 5)), flush=True)
    lam = xr(iv.log(iv.mpf(3))) - xr(iv.log(iv.mpf("0.2")))
    e27, good7 = [], True
    for l in range(0, 5):
        vm = vmax(l)
        good7 &= (SIGMA**2 - vm).a > 0
        e27.append((l, vm, lam * SIGMA / (SIGMA**2 - vm)))
    above5 = (vmax(5) - SIGMA**2).a > 0
    ok["C5"] = good7 and above5
    print("  C5: Lambda = %s; E2.7 at sigma = 3: %s; max V_5 >= %s > 9" %
          (iv.nstr(lam, 8), ", ".join("l = %d: <= %s (max V = %s)" % (l, E.up(b.b, 5), iv.nstr(vm, 6))
                                      for l, vm, b in e27), E.dn(vmax(5).a, 6)), flush=True)
    sup = max([b.b for _, _, b in e27] + [B5.b])
    # controls
    f1, _, bad1 = certify_positive(A_(1), tL, tR)
    rl3, _ = tail_left(A_(5), -2)
    rr25, _ = tail_right(A_(5), mpf("2.5"))
    ok["controls"] = (not f1) and rl3.a > 1 and rr25.a > 1
    print("  controls: the bisection fails at l = 1 (near t = %s); left ratio at t = -2 >= %s; right ratio at r = 2.5 "
          ">= %s" % (iv.nstr(iv.mpf(bad1[0]), 5) if bad1 else "-", E.dn(rl3.a, 4), E.dn(rr25.a, 4)), flush=True)
    good_all = all(ok.values())
    print("  %s: at sigma = 3, ||chi_I R_l(3) chi_I|| <= %s for every l >= 0 (best certified before: 275.2 at "
          "l = 0, D387; 93.96 at l = 1, D466)" % ("CERTIFIED" if good_all else "NOT certified", E.up(sup, 5)))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("  (%.0f s)" % (time.time() - t0))
    return 0 if good_all else 1


if __name__ == "__main__":
    sys.exit(main())
