#!/usr/bin/env python3
"""e2asympsi5.py -- E2-PILOT section 3i (D477): D466's l >= 2 constants in section 3i's weight psi_*, certified.

D466 certified C_l <= 64.18 for l >= 2 in the asymmetric multiplier's own angular weight psi = -phi U', and section
3i's Corollary E2.11 states its angular bound in psi_* := -phi_* U', phi_* = tanh((r_* - x_*)/s), s = 49/50 (section
3f). D462 measured psi/psi_* in [0.64, 0.94] on I in floating point. U' cancels in the ratio: psi/psi_* = phi/phi_*,
and both vanish at x_* = r_*(sqrt 2), with the sign of r_* - x_*. With g D466's closed-form phase (g(x_*) = 0) and
z := (r_* - x_*)/s,

    phi/phi_* = (tanh g / g) (g / z) (z / tanh z) >= (tanh G / G) * s * min g' * 1

on each piece of I within |z| < 1/20 of x_*, G the largest |g| there (tanh(t)/t decreases in t) and min g' taken over
the hull of the piece and x_* (g/z = s (g(r_*) - g(x_*))/(r_* - x_*) by the mean value theorem; g' = 1/s_R + D(1 - sig)
decreases); elsewhere phi_* has no zero on the piece and the ratio is enclosed by interval division.

  P1 rho := min_I psi/psi_* >= that bound, enclosed over 2000 pieces of I = {r in [1.2, 4]}, each piece whose bound falls
     below 0.712 bisected up to eight times (interval arithmetic).
  P2 so (a - a_1) int_I psi_* |u|^2 <= (K_l/rho) ||f||^2, and with D466's X_l, K_l (recomputed here as in
     e2asymcert5's K3) C*_l = (X_l^2 + l(l + 2) K_l/((a - a_1) rho))^(1/2) for l = 2, ..., 6, every l >= 6 bounded by
     l = 6 as there; at l = 1 the angular part is 3 B_1^2, unweighted, so C_1 = 184.82 stands; the summed constant in
     psi_*'s weight over every l >= 1 at sigma = 3, and with D473's X_0(3) over every l >= 0.
  P3 controls: the bound is near sharp (at r = 1.6996, where floating point puts the minimum, 0.7134, psi/psi_* is
     enclosed within 0.01 of rho); and with phi_* centred off the photon sphere (x_* + 3/10) the ratio changes sign on I,
     so no such bound holds.

Labels: certified (interval arithmetic, mpmath.iv at 30 digits).

    python3 checks/e2asympsi5.py
"""
import importlib.util
import os
import sys

from mpmath import iv, mp, mpf

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("e2asymcert5", os.path.join(HERE, "e2asymcert5.py"))
AC = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(AC)
iv.dps = 30
SL, SR, KAP, DD, LN2, X_C = AC.SL, AC.SR, AC.KAP, AC.DD, AC.LN2, AC.X_C
S_STAR = iv.mpf(49) / 50
SIGMA = iv.mpf(3)


def g_of(x):
    z = (x - X_C) / KAP
    return (x - X_C) / SR + DD * ((x - X_C) - KAP * (AC.softplus(z) - LN2))


def gp_of(x):
    z = (x - X_C) / KAP
    if z.a > 0:
        em = iv.exp(-z); om = em / (1 + em)
    else:
        ep = iv.exp(z); om = 1 / (1 + ep)
    return 1 / SR + DD * om


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


def tanh_iv(z):
    return 1 - 2 / (iv.exp(2 * z) + 1)


def ratio_enclosure(tt, xc_star):
    """phi/phi_* on tt by direct interval division (valid where phi_* has no zero on tt)"""
    X = AC.xr(tt)
    return AC.mult(X)[0] / tanh_iv((X - xc_star) / S_STAR)


def ratio_lower(tt):
    """a lower bound for phi/phi_* on the piece tt (an interval in t): direct division where |z| >= 1/20 on the
    piece, the factorised bound (tanh G / G) s min g' (z/tanh z >= 1 dropped) where the piece comes nearer x_*"""
    X = AC.xr(tt)
    z = (X - X_C) / S_STAR
    if z.a >= mpf(1) / 20 or z.b <= -mpf(1) / 20:
        return ratio_enclosure(tt, X_C).a
    g = g_of(X)
    G = max(abs(g.a), abs(g.b))
    tg = iv.mpf(1) if G == 0 else tanh_iv(iv.mpf(G)) / iv.mpf(G)
    H = iv.mpf([min(X.a, X_C.a), max(X.b, X_C.b)])
    return (tg * S_STAR * gp_of(H).a).a


def main():
    ok = {}
    tIa, tIb = iv.log(iv.mpf("0.2")).a, iv.log(iv.mpf(3)).b
    pieces = 2000
    ends = [mpf(tIa) + (mpf(tIb) - mpf(tIa)) * k / pieces for k in range(pieces)] + [mpf(tIb)]
    def refine(lo, hi, depth=8):
        b = ratio_lower(iv.mpf([lo, hi]))
        if b >= mpf("0.712") or depth == 0:
            return b
        mid = (lo + hi) / 2
        return min(refine(lo, mid, depth - 1), refine(mid, hi, depth - 1))
    rho = min(refine(lo, hi) for lo, hi in zip(ends[:-1], ends[1:]))
    ok["P1"] = rho > 0
    print("  P1: psi/psi_* = phi/phi_* >= %s on I (2000 pieces, refined)" % dn(rho, 4), flush=True)
    m1lo, M1hi = AC.enclose_I(lambda tt: AC.mult(AC.xr(tt))[1])
    c = iv.mpf(M1hi) + 2 * SIGMA
    a1 = AC.A_(1)
    m = iv.mpf(m1lo)
    Cs = {}
    for l in range(2, 7):
        wlo, _ = AC.enclose_I(lambda tt, l=l: AC.w_of(tt, AC.A_(l)))
        w = iv.mpf(wlo)
        B = iv.sqrt((2 / m + c**2 / w) / w)
        X = (1 + iv.sqrt(1 + 2 * m * c * B)) / (2 * m)
        K = 2 * X + c * B
        A = iv.mpf(l * (l + 2)) * K / ((AC.A_(l) - a1) * iv.mpf(rho))
        Cs[l] = iv.sqrt(X**2 + A).b
    Cmax = max(Cs.values())
    ok["P2"] = Cmax < mpf("184.82")
    print("  P2: in psi_*'s weight, C*_l <= %s for l = 2..6 (l >= 6 bounded by l = 6); with C_1 <= 184.82 (its angular "
          "part unweighted) and D473's X_0(3) <= 158.57, the summed H^1 constant at sigma = 3 over every l >= 0 is <= "
          "184.82 in section 3i's weight" % ", ".join(up(Cs[l], 5) for l in range(2, 7)), flush=True)
    tmid = iv.log(iv.mpf("0.6996"))
    at_min = ratio_enclosure(tmid, X_C)
    sharp = at_min.b < rho + mpf("0.01")
    xs2 = X_C + iv.mpf(3) / 10
    signs = set()
    for k in range(0, pieces + 1, 50):
        tt = iv.mpf(ends[min(k, pieces)])
        X = AC.xr(tt)
        val = AC.mult(X)[0] * tanh_iv((X - xs2) / S_STAR)
        if val.b < 0:
            signs.add(-1)
        if val.a > 0:
            signs.add(1)
    ok["P3 controls"] = sharp and signs == {1, -1}
    print("  P3: psi/psi_* at r = %s (the floating-point minimum on I) <= %s, within 0.01 of rho: %s; phi_* centred at "
          "x_* + 3/10: phi phi_* takes both signs on I: %s"
          % (iv.nstr(1 + iv.exp(tmid), 4), up(at_min.b, 5), sharp, signs == {1, -1}), flush=True)
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
