#!/usr/bin/env python3
"""rows_large.py -- item 356: the four rows that rest on M1 alone, re-derived at the family's large end on C3's large
brane hole -- Z1t, Z2r, E4r and B2t, the large halves split from rows_small.py's Z1t-s, Z2r-s, E4r-s and B2t-s.  Each
is read off m1_large.py (imported by path, never copied), with AFPY's brane metric, their eq. (13) and fit (15), to
first order in (ell/r0)^2.  Worked in the conversation (computed with sympy, exact where marked; READ where marked;
not verified by a separate session; not seated); 2026-10-13.

  R0 (read) M's item-356 words, verbatim in the rulings file; 183's "never violated as a pair".
  Z1t (computed) Along the mouth's radial ray, our leg: the five-dimensional null energy is zero -- the bulk is Einstein
     with R_AB = -(4/ell^2) g_AB (m1_large M1), so R_AB k^A k^B = 0 on every null ray.  The plane's reading on the same
     ray is zero on the horizon and negative outside it, of order (ell/r0)^2/r0^2 and falling as rho^-5; on tangential
     rays it is negative too (m1_large M4 (v)).  It is the bulk's projected Weyl term on the plane, FW's dual stress
     (their eq. (7), READ) -- the appearance, under 183.  At the small end the radial reading was zero at flat order
     (Z1t-s); at the large end the warp makes it small and negative, never a five-dimensional violation.
  Z2r (computed) Our leg's integral within the reach equals the plane's reading, to M1-c's order -- the row's own tag.
     The five-dimensional integral is zero (Z1t).  The plane's, along the radial null ray from the horizon outward with
     k^t = 1/f, k^rho = 1, is -0.00482 lambda/M^3 = -0.00643 (ell/r0)^2/r0, lambda = ell^2/6 (computed; the integrand
     falls as rho^-5, so the reach, R_reach >> r0, takes all of it).  Both are zero at the order at which the plane reads
     four-dimensional Schwarzschild; they differ at O((ell/r0)^2), the order of M1 (c)'s own corrections.  So Z2r holds
     to M1-c's order at the large end, as at the small end, and the difference is the Weyl term's.
  E4r (computed) The field energy outside the neck within the reach.  In five dimensions the bulk outside the horizon
     carries no stress (Z1t), so no matter energy lies between the horizon and any surface.  The plane's four-
     dimensional reading, its Misner-Sharp mass m(R) = (R/2)(1 - g^RR) in the area radius, is M + 93 lambda/(2000 M) on
     the horizon and M at infinity (computed; 93/250 = F(1)), so between them it reads -F(1) lambda/(8M) = -0.031
     (ell/r0)^2 E -- negative, as at the small end, and negligible: the small end's -5.3e14 E came from gravity being
     five-dimensional at r << ell, while at the large end the plane reads four-dimensional gravity and the deficit is
     the dual stress's energy.
  B2t (READ; from m1_large) Its instance beneath the corridor at the large end: the large hole's bulk, Figueras and
     Wiseman's, Einstein with Lambda = -6/ell^2 and not a Ricci soliton (m1_large M1, M3), the plane carrying our
     tension alone with the RS kink K_mn = gamma_mn/ell (m1_large M2) -- umbilic, not totally geodesic: at the small end
     the plane was totally geodesic at flat order (B2t-s), and the kink entered at warp order.

What this does not claim: the plane's reading beyond first order in (ell/r0)^2; the interior; position 2's side.

Imports m1_large.py by path.  Stdlib + sympy.  python3 rows_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((356, "I still see a lot, including items that rest on M1 and B4d"),
         (183, 'M chose: "Yes: never violated as a pair"'))
_MOD, _C = {}, {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def ML():
    return _load("m1_large.py", "rl_ml")


def rows():
    if "rows" in _C and not MUT:
        return _C["rows"]
    ml = ML()
    o1, o2, o4 = ml.m1(), ml.m2(), ml.m4()
    rho, M, lam = sp.symbols("rho M lambda", positive=True)
    F = sp.Function("F")(rho)
    cf = ml.F_FLW
    FF = sum(sp.nsimplify(c) * (2 * M / rho) ** i for i, c in enumerate(cf))
    G = [sp.simplify(e.subs(F, FF).doit()) for e in o4["generic_G"]]
    f = 1 - 2 * M / rho
    kt2 = (1 / f) if not MUT.get("unaffine") else 1             # k^t = 1/f with k^rho = 1 on the radial null ray
    radial = sp.simplify((-G[0] + G[1]) * kt2)
    I = float(sp.N(sp.Integral((radial * M ** 3 / lam).subs({M: 1, lam: 1}), (rho, 2, sp.oo)), 12))
    # E4r: the plane's Misner-Sharp mass in the area radius
    grr = (1 - lam / rho ** 2 * (rho - 2 * M) / (rho - sp.Rational(3, 2) * M) * (FF - rho * sp.diff(FF, rho))) / f
    R = sp.sqrt(rho ** 2 + lam * FF) if not MUT.get("areal_rho") else rho   # the mutant: rho for the area radius
    gRRinv = sp.diff(R, rho) ** 2 / grr
    mMS = R / 2 * (1 - gRRinv)
    mh = sp.simplify(sp.series(mMS.subs(rho, 2 * M), lam, 0, 2).removeO())
    minf = sp.simplify(sp.limit(sp.series(mMS, lam, 0, 2).removeO(), rho, sp.oo))
    outside = sp.simplify(minf - mh)
    # in r0 = 2M and ell (lambda = ell^2/6): I lambda/M^3 over (ell/r0)^2/r0, and outside/M over (ell/r0)^2
    z2r = I * (sp.Rational(1, 6) * 8)
    e4r = float(sp.simplify(outside / M / (lam / M ** 2)) * sp.Rational(1, 6) * 4)
    res = dict(bulk_null=o1["null"], einstein=o1["einstein"], radial=o4["radial"], tang=o4["tang"], I=I,
               z2r=float(z2r), mh=mh, minf=minf, outside=outside, e4r=e4r, kink=o2["K_is_gamma"], q=o2["q"])
    if not MUT:
        _C["rows"] = res
    return res


def compute():
    return dict(rows=rows())


def report(o):
    r = o["rows"]
    print("rows_large.py -- Z1t, Z2r, E4r, B2t at the large end (item 356)\n")
    print("Z1t the bulk's null energy on a null ray: %s; the plane's radial reading (x lambda/M^2): %s" %
          (r["bulk_null"], " ".join("%+.3g" % v for v in r["radial"])))
    print("Z2r the plane's radial integral: %.6g lambda/M^3 = %.4g (ell/r0)^2/r0" % (r["I"], r["z2r"]))
    print("E4r the plane's Misner-Sharp mass: %s on the horizon, %s at infinity; outside %s = %.4f (ell/r0)^2 E"
          % (r["mh"], r["minf"], r["outside"], r["e4r"]))
    print("B2t the kink K_mn = gamma_mn/ell: %s; the tension our sigma: %s" % (r["kink"], r["q"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    r = o["rows"]
    add("R0 356 and 183 verbatim, each inside its own item", all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    add("Z1t the bulk Einstein, its null energy zero on every null ray; the plane's radial reading zero on the horizon, "
        "negative outside; the tangential negative", r["einstein"] and r["bulk_null"] == 0 and abs(r["radial"][0])
        < 1e-15 and all(v < 0 for v in r["radial"][1:]) and all(v < 0 for v in r["tang"]))
    add("Z2r the plane's radial integral -0.00482 lambda/M^3 = -0.00643 (ell/r0)^2/r0, against the bulk's zero",
        "%.3g" % r["I"] == "-0.00482" and "%.3g" % r["z2r"] == "-0.00643")
    M, lam = sp.symbols("M lambda", positive=True)
    add("E4r the plane's Misner-Sharp mass M + 93 lambda/(2000 M) on the horizon, M at infinity: -0.031 (ell/r0)^2 E "
        "outside", sp.simplify(r["mh"] - (M + sp.Rational(93, 2000) * lam / M)) == 0 and r["minf"] == M
        and "%.3f" % r["e4r"] == "-0.031")
    add("B2t the plane umbilic with the RS kink K_mn = gamma_mn/ell, carrying our tension (q = 1)",
        r["kink"] and r["q"] == 1)
    return res


MUTANTS = {"unaffine": "the radial ray's k^t taken as 1, not 1/f (Z2r)",
           "areal_rho": "the Misner-Sharp mass read in rho, not the sphere's area radius (E4r)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        _C.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        _C.clear()
        caught += bool(failed)
        print("  mutant %-9s %-76s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
