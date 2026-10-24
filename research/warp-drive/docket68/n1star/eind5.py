#!/usr/bin/env python3
"""eind5.py -- [Hin26] Lemma 8.4's simplicity and (8.13) in five dimensions for every l, in the class's types (Phase
B's B8; N1STAR-PROOF.md section 10.52; D120).

10.24 computed the indicial roots of the linearized gauge-fixed Einstein operator L at the record's point for l <= 12
and deduced their location for every l; simplicity and his (8.13) -- "d(Re lam, Z) >= eps_ind" for the non-integer
roots with |lam| <= 50 -- were left at l <= 12.  By 10.24(ii) the scalar type l >= 2 roots are those of (lam + l)(lam -
l - 2), of box^Ups's factor (l + 3 - lam')(l + lam' - 1) Q(lam'), lam' = lam - 1 (gaugepot5.py G1: Q = s^2 - (2 + 2
kappa + z) s + kappa (kappa + 1) + z kappa, s = lam'(lam' - 1), kappa = l (l + 2), z = 4 e_U gam_U^2), and of box^C's
sextic at lam + 1 (damping5.py); the vector type's are -l, l + 2, box^Ups's 1 - l and l + 3 (G1) and box^C's quadratic
at lam + 1; the tensor type's are -l and l + 2.  At the point (v, e_C, gam_C) = (1/2, 1/102400, 10^6), (e_U, gam_U) =
(1/100, 1/100):

  E1 (computed, exact) Simplicity for every l >= 2.  Q(lam - 1) at lam = -l, l + 2, l + 4, 2 - l is a nonzero polynomial
     in l with no root l >= 1; Q's roots in s are real, distinct and positive ((z + 2)^2 + 4 kappa > 0), so its four
     roots in lam are distinct; box^C's discriminant in lam, a polynomial of degree 9 in kappa, has its positive real
     roots strictly between consecutive values l (l + 2) (isolated exactly) -- near l = 135.59, 14640.49, 1534412.09,
     4959861.06, where two roots merge -- so it vanishes at no integer l; box^C at lam + 1 = 1 - l, l + 3, l + 5, 3 - l
     has no root l >= 2 (Sturm), and its resultant with Q(lam - 1) has no positive root in kappa (Sturm); box^C's
     vector quadratic has a positive discriminant and at lam + 1 = 1 - l, l + 3, 2 - l, l + 4 no root l >= 2.  So every
     scalar, vector and tensor root is simple at every l >= 2.  Control: at z = 0, Q(lam - 1) vanishes at lam = -l and
     l + 2, the physical roots, which are then double.
  E2 (computed; exact certificate, numerical scan) (8.13).  box^C's three lower scalar roots lie below -100 at every l
     (damping5.py U4); its three upper ones have real part above 51 for every kappa >= kappa* = l*(l* + 2), l* = 10^4
     (three roots right of the line at kappa*, and none crossing it beyond: the constant coefficient and the Hurwitz
     determinant shifted to the line have no root kappa >= kappa*, Sturm), and so does its vector type's upper root,
     the lower one below -100 (Proposition 10.9); box^Ups's roots are 2 - l, l + 4 and within
     O(z) of -l, 1 - l, l + 2, l + 3, so only l <= 52 reach |lam| <= 50.  Scanning l = 0, 2, 3, ..., l* - 1 (mpmath, 30
     digits; scalar and vector types), the least distance from Z of the real part of a non-integer root with |lam| <=
     50 is printed, with the l
     where it occurs; it is positive, so (8.13) holds for every l with eps_ind below it.  Control: over l <= 12 the scan
     reproduces 10.24(iv)'s 7.3846 x 10^-8.  Mutant: the certificate placed at l* = 12, where it fails.  Simplicity at
     l = 0 and 1, and (8.13) at l = 1, are 10.24(iv)'s, computed for every type at l <= 12; E1 starts at l = 2, and
     the scan covers l = 0 and every l >= 2 (D129).

sympy, mpmath; imports damping5.py.  python3 eind5.py [--selftest | --mutants]   (a few minutes)
"""
import sys
import time

import mpmath as mpm
import sympy as sp

import damping5 as D
from damping5 import Checklist

lam, K = D.lam, D.K
l = sp.Symbol("l", positive=True)
Z_UPS = 4 * sp.Rational(1, 100) * sp.Rational(1, 100)**2


def Q(lm, kap, z=Z_UPS):
    return (lm * (lm - 1))**2 - (2 + 2 * kap + z) * lm * (lm - 1) + kap * (kap + 1) + z * kap


_PC = {}


def boxC():
    """box^C's scalar sextic in lam at the point, kappa symbolic (damping5.py's weight 2/3)"""
    if "p" not in _PC:
        pk, p0, pv = D.polys(4, sp.Rational(2, 3))
        _PC["p"] = sp.Poly(sp.expand(pk.subs(D.PARAMS)), lam)
        _PC["p0"] = sp.Poly(sp.expand(p0.subs(D.PARAMS)), lam)
        _PC["v"] = sp.Poly(sp.expand(pv.subs(D.PARAMS)), lam)
    return _PC["p"]


def boxCv():
    """box^C's vector-type quadratic in lam at the point, kappa symbolic"""
    boxC()
    return _PC["v"]


def off_integers(P):
    """exact: the discriminant in lam of P(lam, kappa) vanishes at no kappa = l (l + 2), l >= 1 an integer; returns
    (ok, the l of its positive real roots, each isolated strictly between consecutive integers)"""
    disc = sp.Poly(sp.discriminant(P.as_expr(), lam), K)
    ok, where = not disc.is_zero, []
    for (a, b), m in disc.intervals():
        if b <= 0:
            continue
        while True:
            la = (-2 + sp.sqrt(4 + 4 * a)) / 2 if a > 0 else 0
            lb = (-2 + sp.sqrt(4 + 4 * b)) / 2
            if sp.floor(la) == sp.floor(lb) or b - a < sp.Rational(1, 10**30):
                break
            a, b = disc.refine_root(a, b, eps=(b - a) / 10)
        ok &= sp.floor(la) == sp.floor(lb) and m == 1 and not (sp.floor(lb) == lb)
        where.append(float((la + lb) / 2))
    return ok, where, disc.degree()


def no_root_from(expr, var, lo):
    """exact: the polynomial expr in var has no real root >= lo (and is not identically zero)"""
    P = sp.Poly(sp.expand(expr), var)
    return not P.is_zero and P.count_roots(lo, None) == 0


# ------------------------------------------------------------------------------------------------- E1
def e1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    z = 0 if control == 1 else Z_UPS
    kap = l * (l + 2)
    QL = sp.expand(Q(lam - 1, kap, z))
    vals = {nm: sp.factor(QL.subs(lam, r)) for nm, r in (("-l", -l), ("l+2", l + 2), ("l+4", l + 4), ("2-l", 2 - l))}
    chk(f"Q(lam - 1) at the integer roots: {vals}; none vanishes at an l >= 1",
        all(no_root_from(v, l, 1) for v in vals.values()))
    ds = sp.expand((2 + 2 * K + z)**2 - 4 * (K * (K + 1) + z * K))
    chk(f"Q's discriminant in s: {sp.factor(ds)} > 0 for kappa >= 0, and its roots in s positive", sp.Poly(ds, K)
        .count_roots(0, None) == 0 and sp.expand(ds - (z + 2)**2 - 4 * K) == 0)
    PC = boxC()
    ok, where, dg = off_integers(PC)
    chk(f"box^C's discriminant in lam: degree {dg} in kappa, positive real roots at l = "
        f"{[round(w, 2) for w in where]}, each strictly between consecutive integers", ok and len(where) == 4)
    cub = {nm: sp.expand(PC.as_expr().subs(K, kap).subs(lam, r + 1)) for nm, r in
           (("-l", -l), ("l+2", l + 2), ("l+4", l + 4), ("2-l", 2 - l))}
    chk("box^C at lam + 1 for the integer roots lam = -l, l + 2, l + 4, 2 - l: no root l >= 2",
        all(no_root_from(v, l, 2) for v in cub.values()))
    R = sp.resultant(sp.expand(PC.as_expr().subs(lam, lam + 1)), sp.expand(Q(lam - 1, K, z)), lam)
    chk(f"resultant of box^C(lam + 1) and Q(lam - 1): degree {sp.Poly(R, K).degree()} in kappa, no root kappa > 0",
        no_root_from(R, K, sp.Rational(1, 10**9)))
    PV = boxCv()
    okv, wv, _ = off_integers(PV)
    vec = [sp.expand(PV.as_expr().subs(K, kap).subs(lam, r + 1)) for r in (-l, l + 2, 1 - l, l + 3)]
    chk(f"vector type: box^C's quadratic {PV.as_expr()} has discriminant roots at l = {wv}, and at lam + 1 for "
        "lam = -l, l + 2, 1 - l, l + 3 no root l >= 2", okv and not wv and all(no_root_from(v, l, 2) for v in vec))
    return chk.ok


# ------------------------------------------------------------------------------------------------- E2
LSTAR = 10**4


def roots_at(lv, dps=30):
    """the scalar and vector type l roots of L at the point with |lam| <= 50: box^C's minus 1, box^Ups's plus 1, the
    physical"""
    mpm.mp.dps = dps
    out = []
    if lv == 0:
        P = _PC["p0"]
        rC = mpm.polyroots([mpm.mpf(sp.Rational(c)) for c in P.all_coeffs()], maxsteps=400, extraprec=400)
        out += [r - 1 for r in rC if abs(r - 2) > mpm.mpf(10)**-20]                 # D removes box^C's Coulomb 2
        z = mpm.mpf(sp.Rational(Z_UPS))
        out += [mpm.mpf(4), (1 + mpm.sqrt(9 + 4 * z)) / 2 + 1, (1 - mpm.sqrt(9 + 4 * z)) / 2 + 1]  # D removes 0 + 1
        out += [mpm.mpf(0), mpm.mpf(2)]
    else:
        kv = lv * (lv + 2)
        P = boxC()
        rC = mpm.polyroots([mpm.mpf(sp.Rational(c.subs(K, kv))) for c in P.all_coeffs()], maxsteps=400,
                           extraprec=400)
        out += [r - 1 for r in rC]
        cv = [mpm.mpf(sp.Rational(c.subs(K, kv))) for c in boxCv().all_coeffs()]
        out += [r - 1 for r in mpm.polyroots(cv, maxsteps=400, extraprec=400)]
        z = mpm.mpf(sp.Rational(Z_UPS))
        b = 2 + 2 * kv + z
        dsq = mpm.sqrt(b**2 - 4 * (kv * (kv + 1) + z * kv))
        for sv in ((b + dsq) / 2, (b - dsq) / 2):
            for sg in (1, -1):
                out.append((1 + sg * mpm.sqrt(1 + 4 * sv)) / 2 + 1)
        out += [mpm.mpf(lv + 4), mpm.mpf(2 - lv), mpm.mpf(-lv), mpm.mpf(lv + 2)]
    return [r for r in out if abs(r) <= 50]


def dist_Z(r):
    x = mpm.re(r)
    return abs(x - mpm.nint(x))


def scan(lmax):
    best, at = mpm.inf, None
    for lv in [0] + list(range(2, lmax)):
        for r in roots_at(lv):
            if abs(mpm.im(r)) < mpm.mpf(10)**-25 and dist_Z(r) < mpm.mpf(10)**-25:
                continue                                                         # an integer root
            d = dist_Z(r)
            if d < best:
                best, at = d, (lv, r)
    return best, at


def e2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    PC = boxC()
    lst = 12 if control == 1 else LSTAR
    kstar = lst * (lst + 2)
    P1 = sp.Poly(PC.as_expr().subs(K, kstar), lam)
    rgt = D.right_of(P1.as_expr(), 51)
    nc = D.no_crossing(PC.as_expr(), 51, kstar)
    PV = boxCv()
    rgv = D.right_of(PV.as_expr().subs(K, kstar), 51)
    ncv = D.no_crossing(PV.as_expr(), 51, kstar)
    chk(f"box^C at l* = {lst}: {rgt} scalar and {rgv} vector roots right of Re lam = 51, none crossing it for kappa >= "
        "kappa*", rgt == 3 and nc and rgv == 1 and ncv)
    b12, at12 = scan(13)
    chk(f"control: over l <= 12 the least distance is {mpm.nstr(b12, 6)} (10.24(iv): 7.3846 x 10^-8), at l = {at12[0]}",
        abs(b12 - mpm.mpf("7.3846e-8")) < mpm.mpf("5e-12"))
    t0 = time.time()
    best, at = scan(13 if control == 1 else LSTAR)
    chk(f"(8.13): over l = 0, 2, ..., {LSTAR - 1}, |lam| <= 50, the least distance from Z of the real part of a non-"
        f"integer root is {mpm.nstr(best, 6)}, at l = {at[0]}, lam = {mpm.nstr(at[1], 12)} ({time.time() - t0:.0f}s)",
        best > 0)
    return chk.ok


CHECKS = [("E1 simplicity for every l >= 2: box^Ups, box^C and the physical roots, exact", e1),
          ("E2 (8.13) for every l: certificate beyond l* = 10^4, scan below; eps_ind's bound", e2)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"eind5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"eind5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
