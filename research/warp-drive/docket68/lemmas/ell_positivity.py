#!/usr/bin/env python3
"""ell_positivity.py -- item 381, first step: "positivity requires ℓ > 2.0 l_P", to be proved.  Where the floor comes
from, whether its premise stands in the theorem as it is now, and what positivity does require of ell there.  Worked in
the conversation (computed, stdlib; machine-checked with z3 where marked, with its guards; READ from the record where
marked; deduced where marked; not verified by a separate session); 2026-10-14.

  Y0 (read) The words, verbatim in the rulings file: 381 "we need to start by proving this"; 275 "Coincident
     everywhere"; and the record's claim, ITEM197-REFLECTION.md: "ℓ > 8.5415m (2m/ℓ < 0.23415)", "−3/4, at every ℓ".
  Y1 (computed; reproduced) Where the floor comes from.  Item 197's facing configuration (m1_facing.py F3, C6b): our
     plane P1 at the RS tension with eq. (17)'s Q = 0 data, position 2's plane P2 a Z2 plane held at a depth y2 in
     (0, y_s).  With P2's tension at 139 (1)'s -1/4, the energy left on P2 is positive somewhere in depth exactly when
     2m/ell < 0.23415, ell > 8.5415 m; for the one-bit README m = m1, so ell > 2.006 l_P.  That is the floor, and it
     is a correct computation in its own configuration.
  Y2 (computed) In the same configuration, at the coincidence (y2 -> 0) P2 tends to the RS1 sheet, e2 -> -1, and the
     remainder tends to -3/4 at every ell computed (2m/ell from 0.0044 to 1.72).  The floor is a statement about a
     plane held apart; at the coincidence no ell gives positivity in that configuration.
  Y3 (deduced) Under 275 no depth exists: the planes coincide everywhere, and no slab of bulk lies between them.  The
     floor's premise is gone, and so is the floor.  "positivity requires ℓ > 2.0 l_P" is not a statement of the theorem
     as it stands, and it cannot be proved there; the board withdraws it.
  Y4 (machine-checked, z3, with guards; the record's B5a) What positivity does require.  The theorem's positivity row
     is B5a at the coincidence, one way (b5a_residue.py A1, A2; verified at item 339).  A bulk null ray crossing the one
     surface gathers S(k, k)/|k_y|, S(k, k) = (lambda + rho) k_y^2 + (rho + p) |k_s|^2.  On the four readings A2 names --
     the summed stress, our side, position 2's side (S1 + 2 S2) and the split at tau = 3/4 -- with 139 (1)'s tensions
     (ours sigma, position 2's -sigma/4), z3 proves every one strictly positive for every sigma > 0, every matter with
     rho + p >= 0 and rho > -sigma/6 (both proved pointwise, item 320), and every crossing ray (k_y != 0).  Since sigma =
     3c^4/(4 pi G ell^2) + 2 dsigma > 0 at every ell > 0, positivity holds at every ell: it sets no floor.  Guards: the
     hypotheses are satisfiable (no vacuous proof), and two broken readings each return a counterexample -- position 2's
     side counted S1 + 4 S2 (its tension then zero) and the matter bound loosened to -sigma/2.
  Y5 (computed; deduced) What the window's floor becomes.  The bulk reaches the Planck curvature, 40 (l_P/ell)^(8/3) =
     1, at ell = 3.99 l_P: a limit of where classical GR applies (353's M-PLANCK-ENDS), not a positivity bound, and an
     order of magnitude rather than a sharp line (it moves with the invariant called "Planck").  Above it sits the
     board's own 1 % threshold, 22.4 l_P.  The window's top in sigma, 2.75e112 J/m^3 (sigma_cypher W1, imported by
     p2_gravity), rests on the withdrawn floor; at the Planck curvature it would be 6.95e111 J/m^3.  Seven places carry
     the withdrawn floor -- sigma_cypher W1, p2_planck's ELL_MIN_OVER_M1, corridor_family F3, ell_map E3, ell_fix X2, and
     WARPTHEOREM.md's items 378 and 380 -- and each is noted, not changed: the window is seated (209), so its change is
     put to M.
  Y6 (deduced) For the route M chose.  The floor was an inequality, and it is gone; no equality was to come from it.
     The Higgs tie's own range (0.024 to 9.6 nm within the top mass's 1 sigma, ell_fix X5) lies far above every floor,
     so it is untouched.  What the tie asserts as an equality is lambda(E5) = 0: the Higgs quartic vanishing at the
     bulk's Planck energy.  The next step is the object in relativity that would force it.

Imports m1_facing.py, p2_gravity.py and ell_map.py by path.  Stdlib + z3.
python3 ell_positivity.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
ITEM197 = os.path.join(HERE, "ITEM197-REFLECTION.md")
MUT = {}
WORDS = ((381, "we need to start by proving this"), (275, "Coincident everywhere"))
RECORD = ("ℓ > 8.5415m (2m/ℓ < 0.23415)", "−3/4, at every ℓ")                 # ITEM197-REFLECTION.md, the table
XS = (0.0044, 0.0739, 0.179, 0.5, 1.72)                                         # 2m/ell, as m1_facing samples
CARRIERS = ("sigma_cypher.py", "p2_planck.py", "corridor_family.py", "ell_map.py", "ell_fix.py")
_MOD = {}


def _load(path, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
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


def readings(sig, r1, r2, w1, w2):
    """b5a_residue A2's four readings as (tension part + matter) on k_y^2 and the matter weight on |k_s|^2."""
    q2 = -sig / 4
    two = 4 if MUT.get("side_s1_4s2") else 2                     # position 2's side S1 + 2 S2 (A1)
    return {"summed S1 + S2": (sig + q2 + r1 + r2, w1 + w2),
            "our side S1": (sig + r1, w1),
            "position 2's side S1 + 2 S2": (sig + two * q2 + r1 + two * r2, w1 + two * w2),
            "split at tau = 3/4": (sig / 2 + 3 * r1 / 4 + r2, 3 * w1 / 4 + w2)}


def b5a_z3():
    """For every sigma > 0, matter rho + p >= 0 and rho > -sigma/6, and every crossing null ray (k_y != 0), each
    reading's S(k, k) = a k_y^2 + b |k_s|^2 is strictly positive.  Returns per reading (proved, guard_sat)."""
    import z3
    sig, r1, r2, w1, w2, ky, ks = z3.Reals("sigma rho1 rho2 w1 w2 ky ks")
    bound = sig / 2 if MUT.get("loose_bound") else sig / 6
    hyp = [sig > 0, w1 >= 0, w2 >= 0, r1 > -bound, r2 > -bound, ky != 0]
    out = {}
    for name, (a, b) in readings(sig, r1, r2, w1, w2).items():
        S = a * ky * ky + b * ks * ks
        s_ = z3.Solver()
        s_.add(*hyp)
        s_.add(z3.Not(S > 0))
        proved = s_.check() == z3.unsat
        g = z3.Solver()
        g.add(*hyp)
        out[name] = (proved, g.check() == z3.sat)
    return out


def b5a_broken():
    """the guards' second half: the two broken readings must each return a counterexample"""
    res = {}
    for key in ("side_s1_4s2", "loose_bound"):
        saved = dict(MUT)
        MUT.clear()
        MUT[key] = True
        try:
            r = b5a_z3()
        finally:
            MUT.clear()
            MUT.update(saved)
        res[key] = not all(p for p, _ in r.values())
    return res


def compute():
    mf = _load(os.path.join(HERE, "m1_facing.py"), "ep_mf")
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "ep_pg")
    em = _load(os.path.join(HERE, "ell_map.py"), "ep_em")
    c, G, hb, LN2 = pg.C, pg.G, pg.HBAR, pg.LN2
    lP = math.sqrt(hb * G / c ** 3)
    m1 = lP * math.sqrt(LN2 / math.pi) / 2
    thr = mf.threshold(-0.25, 0.05, 0.6)                         # 2m/ell where the band closes (C6b)
    coinc, bandmax = {}, {}
    q2 = -0.125 if MUT.get("q2_eighth") else -0.25
    for x in XS:
        ell, ys, T = mf.traj(x, 20000)
        S = [mf.p2_stress(s, ell) for s in T[1:]]
        coinc[x] = (S[0][0] / ys, S[0][1] - q2)
        bandmax[x] = max(r[1] for r in S) - q2
    z = b5a_z3()
    brk = b5a_broken()
    sigP = c ** 7 / (hb * G ** 2)
    planck = 40 ** (3 / 8) * lP
    sig_at = lambda e: 3 * c ** 4 / (4 * math.pi * G * e ** 2) + 2 * pg.DSIG
    flagged = {f: ("8.5415" in open(os.path.join(HERE, f), encoding="utf-8").read()
                   or "2.0 l_P" in open(os.path.join(HERE, f), encoding="utf-8").read()) for f in CARRIERS}
    item197 = " ".join(open(ITEM197, encoding="utf-8").read().split())
    return dict(thr=thr, ell_over_m=2 / thr, floor_lp=2 / thr * m1 / lP, coinc=coinc, bandmax=bandmax, z3=z,
                broken=brk, planck=planck / lP, sig_top=sig_at(2 / thr * m1), sig_planck=sig_at(planck),
                window_top=pg.SIGMA_WINDOW[1], sigP=sigP, flagged=flagged,
                record=all(" ".join(t.split()) in item197 for t in RECORD), floor_board=em.FLOOR_LP)


def report(o):
    print("ell_positivity.py -- positivity and ell's floor (item 381, first step)\n")
    print("Y1 item 197's facing configuration: band closes at 2m/ell = %.5f, ell > %.4f m = %.3f l_P for one bit"
          % (o["thr"], o["ell_over_m"], o["floor_lp"]))
    for x in XS:
        y, r = o["coinc"][x]
        print("Y2 2m/ell %-6g remainder at y2/y_s = %.0e: %+.5f (largest over depth %+.4f)" % (x, y, r, o["bandmax"][x]))
    for k, (p, g) in o["z3"].items():
        print("Y4 %-28s z3: %s (hypotheses satisfiable: %s)" % (k, "PROVED > 0" if p else "NOT PROVED", g))
    print("Y4 guards, broken readings refuted: %s" % o["broken"])
    print("Y5 the Planck curvature at %.2f l_P (sigma %.3e J/m^3); the withdrawn top %.3e (window's %.3e); board's "
          "%.1f l_P" % (o["planck"], o["sig_planck"], o["sig_top"], o["window_top"], o["floor_board"]))
    print("Y5 carriers of the withdrawn floor: %s" % ", ".join(f for f, v in o["flagged"].items() if v))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Y0 381 and 275 verbatim in their items; the record's floor and coincidence value in ITEM197-REFLECTION.md",
        all(" ".join(t.split()) in _item(n) for n, t in WORDS) and o["record"])
    add("Y1 item 197's band closes at 2m/ell = 0.23415: ell > 8.5415 m, 2.006 l_P for the one-bit README",
        "%.5f" % o["thr"] == "0.23415" and "%.4f" % o["ell_over_m"] == "8.5415" and "%.3f" % o["floor_lp"] == "2.006")
    add("Y2 at the coincidence the remainder tends to -3/4 at every ell computed; the band exists only below the "
        "threshold", all(abs(o["coinc"][x][1] + 0.75) < 0.01 and o["coinc"][x][0] < 2e-4 for x in XS)
        and all((o["bandmax"][x] > 0) == (x < o["thr"]) for x in XS))
    add("Y4 z3 proves all four B5a readings strictly positive for every sigma > 0, matter rho + p >= 0, rho > -sigma/6, "
        "every crossing ray; hypotheses satisfiable", len(o["z3"]) == 4 and all(p and g for p, g in o["z3"].values()))
    add("Y4 guards: position 2's side as S1 + 4 S2 and the bound -sigma/2 each return a counterexample",
        all(o["broken"].values()) and len(o["broken"]) == 2)
    add("Y5 the Planck curvature at 3.99 l_P (sigma 6.95e111 J/m^3); the window's top 2.75e112 is the withdrawn "
        "floor's; every carrier named holds the floor", "%.3g" % o["planck"] == "3.99" and "%.3g" % o["sig_planck"] == "6.95e+111"
        and "%.3g" % o["sig_top"] == "2.75e+112" and abs(o["sig_top"] / o["window_top"] - 1) < 2e-3
        and all(o["flagged"].values()) and o["planck"] < o["floor_board"])
    return res


MUTANTS = {"side_s1_4s2": "position 2's side counted S1 + 4 S2: its tension part zero (Y4)",
           "loose_bound": "the matter bound loosened to rho > -sigma/2 (Y4)",
           "q2_eighth": "position 2's tension read -1/8 (the doubled count) in item 197's remainder (Y2)"}


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
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-72s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
