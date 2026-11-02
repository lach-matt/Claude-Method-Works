#!/usr/bin/env python3
"""eindcert5.py -- c6: eps_ind's bound certified, the scan of eind5.py E2 below l* = 10^4 made rigorous.

eind5.py E2 proves (8.13) beyond l* = 10^4 exactly (Sturm) and scans l = 0, 2, 3, ..., l* - 1 in floating point (mpmath,
30 digits); epsind5.py E3 finds the least distance from Z of a box^Ups root plus 1 with |lam| <= 50, delta_50 =
1.94137e-8, also in floating point. Here every root that scan visits is enclosed rigorously. For each l, the three
polynomials of eind5.py (box^C's scalar sextic and vector quadratic at lam + 1, box^Ups's quartic Q(lam - 1)) have exact
rational coefficients at kappa = l (l + 2); approximate roots z_k (mpmath, 50 digits) are rounded to Gaussian rationals
and each is given the Weierstrass inclusion radius

    r_k = n |p(z_k)| / (|a_n| prod_(j != k) |z_k - z_j|),      n = deg p,

computed in exact rational arithmetic (squared, then a rational upper bound of the square root). By the inclusion
theorem of Braess and Hadeler (the discs D(z_k, r_k) contain every zero of p, and a component made of m discs exactly m
of them), pairwise disjoint discs hold one root each. An integer root is identified exactly (p vanishes at the integer,
in rationals) and set aside, as the scan sets aside integer roots; for every other root the distance of its real part
from Z is bounded below by dist(Re z_k, Z) - r_k, and |lam| <= 50 is decided from the disc (an undecided disc is kept,
which can only lower the minimum).

  I1 (certified, exact rational arithmetic) Over l = 0, 2, 3, ..., 9999 every disc of the three polynomials is disjoint
     from the others, and the least distance from Z of the real part of a non-integer root with |lam| <= 50 lies in
     [lo, hi] with hi - lo below 10^-40: lo > 1.94137e-8 (delta_50, so epsind5.py E3's value is certified to the digits
     printed) and hi < 1.94138e-8 (the upper bound response5.py R10 uses). The root attaining it is box^Ups's, as E3
     says; box^C's own least distance is printed.
  Control: a polynomial with a planted root 3 + 10^-30 next to an integer root 4: the certifier keeps the first, at
     distance 10^-30 from Z (not set aside as an integer, since p(3) != 0), and sets aside the second.

Reach: l = 1 is eind5.py's 10.24(iv) case, computed at l <= 12, and not rescanned here; the region l >= l* is eind5.py
E2's exact certificate; the physical roots -l, l + 2, 2 - l, l + 4 are integers. Labels: computed (exact rational
arithmetic; the approximate roots only seed the discs).

Run: python3 checks/eindcert5.py   (a few minutes; imports eind5.py and damping5.py)
"""
import math
import os
import sys
import time
from fractions import Fraction as Fr

import mpmath as mpm
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import eind5 as E                                                                 # noqa: E402

LSTAR = E.LSTAR
D = 60                                       # digits of the rational upper bound of a square root


def sqrt_up(x):
    """a rational >= sqrt(x), x a nonnegative Fraction, within 10^-D relative"""
    if x == 0:
        return Fr(0)
    s = math.isqrt(x.numerator*x.denominator*10**(2*D)) + 1
    return Fr(s, x.denominator*10**D)


def sqrt_dn(x):
    if x == 0:
        return Fr(0)
    return Fr(math.isqrt(x.numerator*x.denominator*10**(2*D)), x.denominator*10**D)


class G:
    """Gaussian rationals"""
    __slots__ = ("re", "im")

    def __init__(self, re, im=Fr(0)):
        self.re, self.im = re, im

    def __add__(self, o):
        return G(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return G(self.re*o.re - self.im*o.im, self.re*o.im + self.im*o.re)

    def abs2(self):
        return self.re*self.re + self.im*self.im


def horner(coeffs, z):
    acc = G(Fr(0))
    for c in coeffs:
        acc = acc*z + G(c)
    return acc


def to_rat(x):
    """the exact value of an mpf as a Fraction"""
    sign, man, exp, _ = mpm.mpf(x)._mpf_
    if not man:
        return Fr(0)
    v = Fr(int(man))*(Fr(2)**exp)
    return -v if sign else v


def certify(coeffs, shift=0, drop=()):
    """the roots of sum c_i x^(n-i) (exact Fractions), as (z_k, r_k^2-bound r_k, integer or None), shifted by -shift
    (lam = x - shift); drop: exact roots removed beforehand (they must vanish exactly). Returns None if discs overlap."""
    mpm.mp.dps = 50
    n = len(coeffs) - 1
    approx = mpm.polyroots([mpm.mpf(c.numerator)/c.denominator for c in coeffs], maxsteps=500, extraprec=500)
    zs = [G(to_rat(mpm.re(z)), to_rat(mpm.im(z))) for z in approx]
    an2 = coeffs[0]*coeffs[0]
    rs = []
    for k, z in enumerate(zs):
        prod = Fr(1)
        for j, w in enumerate(zs):
            if j != k:
                prod *= (z - w).abs2()
        if prod == 0:
            return None
        rs.append(sqrt_up(n*n*horner(coeffs, z).abs2()/(an2*prod)))
    for k in range(n):
        for j in range(k + 1, n):
            if sqrt_dn((zs[k] - zs[j]).abs2()) <= rs[k] + rs[j]:
                return None
    out = []
    for z, r in zip(zs, rs):
        lam_re = z.re - shift
        n0 = round(lam_re)
        integer = None
        if abs(lam_re - n0) <= r and abs(z.im) <= r:
            x0 = Fr(n0 + shift)
            if horner(coeffs, G(x0)).abs2() == 0:
                integer = n0
        if integer is not None and integer in drop:
            continue
        out.append((G(lam_re, z.im), r, integer))
    return out


def lowest(roots, lam_max=50):
    """(lower bound, upper bound, root) of the least distance from Z over the non-integer roots with |lam| <= lam_max"""
    best = None
    for z, r, integer in roots:
        if integer is not None:
            continue
        m2 = z.abs2()
        if sqrt_dn(m2) - r > lam_max:
            continue                                         # certainly outside |lam| <= 50
        n0 = round(z.re)
        d = abs(z.re - n0)
        if d - r <= 0:
            return (Fr(0), d + r, z)                         # cannot be separated from an integer: no certificate
        lo, hi = d - r, d + r
        if best is None or lo < best[0]:
            best = (lo, hi, z)
    return best


def frac_poly(P):
    """eind5's Poly in lam with coefficients in kappa -> list of lists of Fractions (highest power first)"""
    out = []
    for c in P.all_coeffs():
        pc = sp.Poly(c, E.K)
        out.append([Fr(int(sp.Rational(x).p), int(sp.Rational(x).q)) for x in pc.all_coeffs()])
    return out


def at(cp, kv):
    vals = []
    for cs in cp:
        acc = Fr(0)
        for x in cs:
            acc = acc*kv + x
        vals.append(acc)
    while vals and vals[0] == 0:
        vals.pop(0)
    return vals


def i1(control=False):
    if control:
        x = sp.Symbol("x")
        p = sp.Poly(sp.expand((x - 3 - sp.Rational(1, 10**30))*(x - 4)*(x**2 + x + 7)), x)
        res = certify([Fr(int(c.p), int(c.q)) for c in p.all_coeffs()])
        low = lowest(res)
        ints = [i for _, _, i in res if i is not None]
        return low is not None and low[0] > 0 and low[1] < Fr(1, 10**29) and ints == [4]
    E.boxC()
    PC, PV, P0 = frac_poly(E.boxC()), frac_poly(E.boxCv()), [Fr(int(sp.Rational(c).p), int(sp.Rational(c).q))
                                                               for c in E._PC["p0"].all_coeffs()]
    lam = E.lam
    z = sp.Rational(E.Z_UPS)
    QU = frac_poly(sp.Poly(sp.expand(E.Q(lam - 1, E.K, z)), lam))
    best = {"box^C": None, "box^Ups": None}
    t0 = time.time()
    nfail = 0
    for lv in [0] + list(range(2, LSTAR)):
        kv = Fr(lv*(lv + 2))
        if lv == 0:
            groups = [("box^C", certify(P0, shift=1, drop=(1,)))]       # eind5 removes box^C's Coulomb root 2 = lam + 1
        else:
            groups = [("box^C", certify(at(PC, kv), shift=1)), ("box^C", certify(at(PV, kv), shift=1))]
        if lv <= 60:
            q = QU if lv else frac_poly(sp.Poly(sp.expand(E.Q(lam - 1, 0, z)), lam))
            groups.append(("box^Ups", certify(at(q, kv) if lv else [x[0] for x in q])))
        for name, res in groups:
            if res is None:
                nfail += 1
                continue
            low = lowest(res)
            if low is not None and (best[name] is None or low[0] < best[name][0]):
                best[name] = low + (lv,)
    lo = min(b[0] for b in best.values() if b)
    hi = min(b[1] for b in best.values() if b)
    who = min((b for b in best.values() if b), key=lambda b: b[0])
    print("  I1: l = 0, 2, ..., %d (%.0fs): discs overlapping in %d polynomials; least distance from Z of a non-integer"
          " root with |lam| <= 50 in [%s, %s] (width %.1e), at l = %d, lam = %s + %s i (box^Ups: %s); box^C's least "
          "%s at l = %d" % (LSTAR - 1, time.time() - t0, nfail, mpm.nstr(mpm.mpf(lo.numerator)/lo.denominator, 12),
                            mpm.nstr(mpm.mpf(hi.numerator)/hi.denominator, 12), float(hi - lo), who[3],
                            mpm.nstr(mpm.mpf(who[2].re.numerator)/who[2].re.denominator, 15),
                            mpm.nstr(mpm.mpf(who[2].im.numerator)/who[2].im.denominator, 3), who is best["box^Ups"],
                            mpm.nstr(mpm.mpf(best["box^C"][0].numerator)/best["box^C"][0].denominator, 6),
                            best["box^C"][3]), flush=True)
    return (nfail == 0 and lo > Fr(194137, 10**13) and hi < Fr(194138, 10**13) and hi - lo < Fr(1, 10**40)
            and who is best["box^Ups"])


CHECKS = [("I1", i1)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s; control (planted root at 10^-30 from Z kept, integer root set aside) %s" %
              (name, "PASS" if good else "FAIL", "behaves" if ctl else "MISBEHAVES"), flush=True)
        ok &= good and ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
