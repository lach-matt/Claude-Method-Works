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
in rationals, and lies in the disc: (Re z_k - n0)^2 + (Im z_k)^2 <= r_k^2) and set aside, as the scan sets aside integer
roots; for every other root the distance of its real part
from Z is bounded below by dist(Re z_k, Z) - r_k, and |lam| <= 50 is decided from the disc (an undecided disc is kept,
which can only lower the minimum).

  I1 (certified, exact rational arithmetic) Over l = 0, 2, 3, ..., 9999 every disc of box^C's two polynomials, and
     over l = 0, 2, 3, ..., 60 every disc of box^Ups's quartic Q(lam - 1) (I2 covers l >= 52), is disjoint from the
     others, and the least distance from Z of the real part of a non-integer root with |lam| <= 50 lies in
     [lo, hi] with hi - lo below 10^-40: lo > 1.94137e-8 (delta_50, so epsind5.py E3's value is certified to the digits
     printed) and hi < 1.94138e-8 (the upper bound response5.py R10 uses). The root attaining it is box^Ups's, as E3
     says, and its disc lies certainly inside |lam| <= 50 (|z_k| + r_k <= 50, rationally); box^C's own least distance
     is printed.
  Control: (a) a polynomial with a planted root 3 + 10^-30 next to an integer root 4: the certifier keeps the first, at
     distance 10^-30 from Z (its disc already excludes 3, so the exact test p(n) = 0 is not what keeps it), and
     sets aside the second; (b) x^2 - 1
     seeded at 1 + 1/10 and -1 - 1/10: each exact root lies in its disc. At these seeds |W_k| = (21/220) < 1/10, so a
     radius |W_k| without the factor n misses the root and fails (b).
  I2 (exact, sympy) box^Ups's roots for l >= 52, where I1 does not scan. With s = lam'(lam' - 1) and lam' = lam - 1
     (the program's Q(lam - 1), checked equal to the formula below), Q(lam') = s^2 - (2 + 2 kappa + z) s + kappa (kappa
     + 1) + z kappa has discriminant D = (z + 2)^2 + 4 kappa > 0 and real roots s_+-(z) with ds_+-/dz = (1 +- (z + 2)/
     sqrt(D))/2 >= 0 (b_z > 0, D_z >= 0 and 4 b_z^2 D - D_z^2 = 16 kappa >= 0, each a polynomial in (kappa, z) with
     nonnegative coefficients), so for z = 4 x 10^-6 >= 0, s_+- >= s_+-(0) = (l + 1)(l + 2), l (l + 1). Then lam' = (1
     +- sqrt(1 + 4 s))/2 is real with |lam'| >= (sqrt(1 + 4 l (l + 1)) - 1)/2 = l, so |lam| >= l - 1 >= 51 > 50: no
     box^Ups root with |lam| <= 50 at l >= 52, and I1's scan to l = 60 overlaps it. Control: the same derivation with
     the z terms' sign flipped (z -> -z in Q): b_z = -1 < 0, and I2 rejects it.

Reach: l = 1 is eind5.py's 10.24(iv) case, computed at l <= 12, and not rescanned here; the region l >= l* is eind5.py
E2's exact certificate; the physical roots -l, l + 2, 2 - l, l + 4 are integers. Labels: computed (exact rational
arithmetic; the approximate roots only seed the discs).

Run: python3 checks/eindcert5.py   (about twelve minutes; imports eind5.py and damping5.py)
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


def certify(coeffs, shift=0, drop=(), seeds=None):
    """the roots of sum c_i x^(n-i) (exact Fractions), as (z_k, r_k^2-bound r_k, integer or None), shifted by -shift
    (lam = x - shift); drop: exact roots removed beforehand (they must vanish exactly); seeds: Gaussian rationals in
    place of the mpmath roots. Returns None if discs overlap."""
    mpm.mp.dps = 50
    n = len(coeffs) - 1
    if seeds is None:
        approx = mpm.polyroots([mpm.mpf(c.numerator)/c.denominator for c in coeffs], maxsteps=500, extraprec=500)
        zs = [G(to_rat(mpm.re(z)), to_rat(mpm.im(z))) for z in approx]
    else:
        zs = seeds
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
        if (lam_re - n0)**2 + z.im**2 <= r*r:
            x0 = Fr(n0 + shift)
            if horner(coeffs, G(x0)).abs2() == 0:
                integer = n0
        if integer is not None and integer in drop:
            continue
        out.append((G(lam_re, z.im), r, integer))
    return out


def lowest(roots, lam_max=50):
    """(lower bound, upper bound, root, disc certainly inside |lam| <= lam_max) of the least distance from Z over the
    non-integer roots with |lam| <= lam_max"""
    best = None
    for z, r, integer in roots:
        if integer is not None:
            continue
        m2 = z.abs2()
        if sqrt_dn(m2) - r > lam_max:
            continue                                         # certainly outside |lam| <= 50
        inside = sqrt_up(m2) + r <= lam_max
        n0 = round(z.re)
        d = abs(z.re - n0)
        if d - r <= 0:
            return (Fr(0), d + r, z, inside)                 # cannot be separated from an integer: no certificate
        lo, hi = d - r, d + r
        if best is None or lo < best[0]:
            best = (lo, hi, z, inside)
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
        ok_a = low is not None and low[0] > 0 and low[1] < Fr(1, 10**29) and ints == [4]
        e = Fr(1, 10)
        res = certify([Fr(1), Fr(0), Fr(-1)], seeds=[G(1 + e), G(-1 - e)])
        ok_b = res is not None and all((z.re - t)**2 + z.im**2 <= r*r for (z, r, _), t in zip(res, (1, -1)))
        return ok_a and ok_b
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
    hiw = min((b for b in best.values() if b), key=lambda b: b[1])
    print("  I1: l = 0, 2, ..., %d (%.0fs): discs overlapping in %d polynomials; least distance from Z of a non-integer"
          " root with |lam| <= 50 in [%s, %s] (width %.1e), at l = %d, lam = %s + %s i (box^Ups: %s); box^C's least "
          "%s at l = %d" % (LSTAR - 1, time.time() - t0, nfail, mpm.nstr(mpm.mpf(lo.numerator)/lo.denominator, 12),
                            mpm.nstr(mpm.mpf(hi.numerator)/hi.denominator, 12), float(hi - lo), who[4],
                            mpm.nstr(mpm.mpf(who[2].re.numerator)/who[2].re.denominator, 15),
                            mpm.nstr(mpm.mpf(who[2].im.numerator)/who[2].im.denominator, 3), who is best["box^Ups"],
                            mpm.nstr(mpm.mpf(best["box^C"][0].numerator)/best["box^C"][0].denominator, 6),
                            best["box^C"][4]), flush=True)
    print("  I1: the disc giving hi lies certainly inside |lam| <= 50: %s" % hiw[3], flush=True)
    return (nfail == 0 and lo > Fr(194137, 10**13) and hi < Fr(194138, 10**13) and hi - lo < Fr(1, 10**40)
            and who is best["box^Ups"] and hiw[3])


def nonneg_poly(e, gens):
    """e a polynomial in gens with every coefficient >= 0 (so e >= 0 for gens >= 0)"""
    p = sp.Poly(sp.expand(e), *gens)
    return all(c >= 0 for c in p.coeffs())


def i2(control=False):
    k, z, l = sp.symbols("kappa z l", positive=True)
    sg = -1 if control else 1
    s, lp, lam = sp.symbols("s lam' lam")
    Qs = s**2 - (2 + 2*k + sg*z)*s + k*(k + 1) + sg*z*k
    same = sp.expand(E.Q(lam - 1, k, z) - Qs.subs(s, (lam - 1)*(lam - 2))) == 0      # the program's shift lam' = lam - 1
    b, c = -Qs.coeff(s, 1), Qs.coeff(s, 0)
    D = sp.expand(b**2 - 4*c)
    bz, Dz = sp.diff(b, z), sp.diff(D, z)
    sq = sp.sqrt(D)
    spm = [(b + sq)/2, (b - sq)/2]
    roots = all(sp.simplify(Qs.subs(s, x)) == 0 for x in spm)
    dform = all(sp.simplify(sp.diff(x, z) - (bz + sgn*Dz/(2*sq))/2) == 0 for x, sgn in zip(spm, (1, -1)))
    mono = (nonneg_poly(bz, (k, z)) and sp.Poly(bz, k, z).eval({k: 0, z: 0}) > 0 and nonneg_poly(Dz, (k, z))
            and nonneg_poly(4*bz**2*D - Dz**2, (k, z)) and nonneg_poly(D, (k, z)) and D.subs({k: 0, z: 0}) > 0)
    sq0 = sp.sqrt(sp.factor(D.subs({z: 0, k: l*(l + 2)})))
    at0 = [sp.factor((b.subs({z: 0, k: l*(l + 2)}) + sgn*sq0)/2) for sgn in (1, -1)]
    vals = (sp.simplify(at0[0] - (l + 1)*(l + 2)) == 0 and sp.simplify(at0[1] - l*(l + 1)) == 0)
    lmin = sp.simplify((sp.sqrt(sp.factor(1 + 4*l*(l + 1))) - 1)/2 - l) == 0
    zpos = sp.Rational(E.Z_UPS) >= 0
    ok = same and roots and dform and mono and vals and lmin and zpos and 52 - 1 > 50 and 61 > 52
    if control:
        print("  I2 control (z -> -z): b_z = %s, monotonicity test %s" % (bz, "passes" if mono else "rejects"),
              flush=True)
        return not mono
    else:
        print("  I2: Q(lam - 1) is the formula in s = lam'(lam' - 1), lam' = lam - 1: %s; D = %s; s_+- roots: %s; "
              "ds_+-/dz = (b_z +- D_z/(2 sqrt D))/2: %s; >= 0 (b_z = %s, D_z = %s, 4 b_z^2 D - D_z^2 = %s): %s; "
              "s_+-(0) = %s: %s; min |lam'| at s = l (l + 1) is l: %s; so |lam| >= l - 1 > 50 for l >= 52"
              % (same, D, roots, dform, bz, Dz, sp.factor(4*bz**2*D - Dz**2), mono, at0, vals, lmin), flush=True)
    return ok


CHECKS = [("I1", i1, "planted root at 10^-30 from Z kept, integer root set aside, true roots inside offset-seeded"
                     " discs"),
          ("I2", i2, "z terms' sign flipped: monotonicity in z rejected")]


def main():
    ok = True
    for name, f, what in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s; control (%s) %s" % (name, "PASS" if good and ctl else "FAIL", what,
                                          "behaves" if ctl else "MISBEHAVES"), flush=True)
        ok &= good and ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
