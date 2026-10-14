#!/usr/bin/env python3
"""corridor_family.py -- item 256: clauses (G) and (H) restated as one family with two ends.  M: "One family, both ends"
-- the corridor is the hole on the plane whose horizon holds the README's N bits: small (five-dimensional, C1/C2) when N
is below a crossover set by ell, large (the record's four-dimensional clause (G)/(H)) above it.  Worked in the
conversation (computed, exact where marked; verified once -- item 261, CONFIRMED with qualifications, all seated below
(205/206); not seated); 2026-10-11.  First headed "... not verified by a separate session ...".

  F0 (read) M's item-256 words, verbatim in the rulings file.
  F1 (computed, exact) The two ends, each holding N bits on its horizon.
     Small end (C2): r_h = (2 N ln2 / pi^2)^(1/3) l5, l5^3 = hbar G5 / c^3, G5 = G ell;
       E = 3 pi c^4 r_h^2 / (8 G5);  S = 2 pi^2 r_h^3 / (4 l5^3) = N ln2.
     Large end (the record's clause (G)/(H)): r0 = 2m = (N A_bit / 4 pi)^(1/2), A_bit = 4 ln2 l_P^2;
       E = c^4 r0 / (2G) = (N h c^5 ln2 / (8 pi^2 G))^(1/2);  S = 4 pi r0^2 / (4 l_P^2) = N ln2.
  F2 (computed, exact) The crossover.  The small end's r_h reaches ell at N = pi^2 ell^2 / (2 ln2 l_P^2); the large
     end's r0 reaches ell at N = pi ell^2 / (ln2 l_P^2) -- the same scale, (ell/l_P)^2, a factor pi/2 apart.  The two
     ends meet within order one there: at equal horizon radius ell the small end's E is 3 pi/4 of the large end's; at
     the small end's crossover N the ratio is (3/4) sqrt(2 pi) = 1.88.  The family is continuous up to the order-one
     factors the numerical brane-hole family settles (F5).  [Verifier, item 261: the two-end construct itself jumps at
     the small end's crossover N, by x1.88 in E and x sqrt(pi/2) = 1.253 in radius; the physical family is one smooth
     branch (Figueras-Wiseman: R4/ell 0.07-20, one negative mode, no zero modes); its E(N) through the crossover is
     published in neither paper read, so "settles" points to numbers not in hand.  E_s/E_l = (3/4) 2^(2/3) pi^(1/6)
     x^(1/6), x = N ln2 l_P^2/ell^2: the 1.88 gap spans a factor ~44 in N.]
  [Item 381 (ell_positivity Y1-Y5): the positivity floor ell > 8.5415 m1 = 2.0 l_P is item 197's, for position 2's
     plane held at a depth; under 275 the planes coincide everywhere, the floor has no premise and is withdrawn, and
     B5a holds at every ell.  Kept as written; the window's change is put to M.]
  F3 (computed) ell is set by our plane's tension: ell^2 = 3 c^4 / (4 pi G (sigma - 2 delta sigma)) (p2_planck), so
     with our tension at S0 x 2^w, ell = 13.964 um x 2^(-w/2) up to the offset's 2^-206 -- 13.964 um at the window's
     floor, 8.5415 m1 = 3.24e-35 m at its top -- and the crossover N moves as 2^-w: 5.31e60 bits at the floor, 28.7 at the
     top.  The example README (N = 2,742,570,311,524,972) is at the small end for w < 150.44 doublings of the window's
     196.885, at the large end above.  [Verifier, item 261: 150.44 is the r_h = ell convention -- 149.79 by r0 = ell,
     144.98 where the two energy formulas agree (r_h = 0.283 ell); neither end is controlled for about 140.5 < w <
     156.4 (r_h > 0.1 ell, r0 < 10 ell), so the switch is a labelling convention, not a sharp physical one.  The
     28.7-bit crossover at the window's top (ell = 2.0 l_P, l5 = 1.26 l_P) is a Planck-scale extrapolation outside
     semiclassical control.]
  F4 (computed, exact) The head statement: at each end the corridor is fixed by N alone in that end's own Planck units --
     r_h / l5 at the small end, r0 / l_P at the large; in SI the small end's size and energy also carry ell, our tension.
  F5 (named, not computed) Between the ends, the numerical brane-hole family: Kudoh-Tanaka-Nakamura's small holes going
     smoothly to five-dimensional Schwarzschild (read in full by the C1 verifier, item 254), Figueras-Wiseman's holes of
     every size going over to five-dimensional behaviour small and to four-dimensional large (abstract; read in full by
     the C3 verifier, item 261).  Both ends are non-extremal; the large end reads four-dimensional Schwarzschild, not
     eq. (17) -- the record's E and r0 are Schwarzschild's and carry, its eq. (17)-specific results (the extremal throat)
     do not.  [Verifier, item 261: the large end is 4D Schwarzschild on the plane with corrections O(ell^2/r0^2); T and S
     are Schwarzschild's at fixed ADM mass to first order (Abdolrahimi et al., 1206.0708, read in full), but the brane
     horizon area exceeds 4 pi (2M)^2 by ~0.78 ell^2 -- so the large end's "N bits on the horizon" is the thermodynamic
     entropy with r0 = 2GM/c^2, not the brane areal radius (relative difference ~0.062 (ell/r0)^2).  Kudoh-Tanaka-
     Nakamura's holes reach only ~0.2 ell, and Yoshino (2009) and Kleihaus et al. (2011) disputed even the small holes:
     the full-size evidence is Figueras-Wiseman's.]

Imports p2_gravity.py by path.  Stdlib + sympy.  python3 corridor_family.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M256 = "One family, both ends (Recommended)"
N_EX = 2742570311524972

N, G, ell, hb, c, h = sp.symbols("N G ell hbar c h", positive=True)
LN2 = sp.log(2)
lP2 = hb * G / c ** 3
l5 = (hb * G * ell / c ** 3) ** sp.Rational(1, 3)


def ends():
    rh = (2 * N * LN2 / sp.pi ** 2) ** sp.Rational(1, 3) * l5
    if MUT.get("small_one_side"):
        rh = (4 * N * LN2 / sp.pi ** 2) ** sp.Rational(1, 3) * l5
    Es = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * G * ell)
    Ss = sp.simplify(2 * sp.pi ** 2 * rh ** 3 / (4 * l5 ** 3))
    r0 = sp.sqrt(N * 4 * LN2 * lP2 / (4 * sp.pi))
    El = c ** 4 * r0 / (2 * G)
    Sl = sp.simplify(4 * sp.pi * r0 ** 2 / (4 * lP2))
    return dict(rh=rh, Es=Es, Ss=Ss, r0=r0, El=El, Sl=Sl)


def crossover(e):
    Ns = sp.solve(sp.Eq(e["rh"], ell), N)[0]
    Nl = sp.solve(sp.Eq(e["r0"], ell), N)[0]
    E_equal_radius = sp.simplify(e["Es"].subs(N, Ns) / e["El"].subs(N, Nl))
    E_equal_N = sp.simplify(e["Es"].subs(N, Ns) / e["El"].subs(N, Ns))
    return dict(Ns=sp.simplify(Ns), Nl=sp.simplify(Nl), ratio_N=sp.simplify(Ns / Nl), E_equal_radius=E_equal_radius,
                E_equal_N=E_equal_N)


def window(e):
    spec = importlib.util.spec_from_file_location("cf_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    lp = math.sqrt(PG.HBAR * PG.G / PG.C ** 3)
    S0, S1 = PG.SIGMA_WINDOW
    W = math.log2(S1 / S0)
    kap = 3 * PG.C ** 4 / (4 * math.pi * PG.G)
    ell_w = lambda w: math.sqrt(kap / (S0 * 2.0 ** w - 2 * PG.DSIG))
    Nx = lambda w: math.pi ** 2 * ell_w(w) ** 2 / (2 * math.log(2) * lp ** 2)
    # the example README's switch: N_EX = Nx(w)
    wx = math.log2(Nx(0) / N_EX)
    # item 261: the switch by r0 = ell (the large end's crossover, pi/2 higher in N) and where the two E formulas agree
    wx_r0 = math.log2(Nx(0) * 2 / math.pi / N_EX)
    xi = float(sp.solve(sp.Eq(e["Es"] / e["El"], 1), N)[0] / (sp.pi ** 2 * ell ** 2 / (2 * LN2 * lP2)))
    wx_E = math.log2(Nx(0) * xi / N_EX)
    m1 = PG.corridor(PG.G)["m1"]
    return dict(W=W, ell0=ell_w(0), ellW=ell_w(W), ell_max=PG.ELL_MAX, top=8.5415 * m1, Nx0=Nx(0), NxW=Nx(W), wx=wx,
                wx_r0=wx_r0, wx_E=wx_E, rh_E=xi ** (1 / 3))


def compute():
    e = ends()
    return dict(e=e, x=crossover(e), w=window(e))


def report(o):
    e, x, w = o["e"], o["x"], o["w"]
    print("corridor_family.py -- clauses (G) and (H) as one family, both ends (item 256)\n")
    print("F1 small end: r_h = %s; E = %s; S = %s" % (e["rh"], sp.simplify(e["Es"]), e["Ss"]))
    print("   large end: r0 = %s; E = %s; S = %s" % (e["r0"], sp.simplify(e["El"]), e["Sl"]))
    print("F2 crossover N: small %s, large %s, ratio %s; E small/large at equal radius %s, at equal N %s = %.4f" % (
        x["Ns"], x["Nl"], x["ratio_N"], x["E_equal_radius"], x["E_equal_N"], float(x["E_equal_N"])))
    print("F3 ell across the window: %.4e m (floor; table-top %.4e) .. %.4e m (top; 8.5415 m1 = %.4e); crossover N %.3e .. "
          "%.3g; the example README switches ends at w = %.2f of W = %.3f" % (w["ell0"], w["ell_max"], w["ellW"], w["top"],
                                                                                w["Nx0"], w["NxW"], w["wx"], w["W"]))
    print("   (item 261) the switch by r0 = ell: w = %.2f; where the two E formulas agree (r_h = %.3f ell): w = %.2f" % (
        w["wx_r0"], w["rh_E"], w["wx_E"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("F0 M's item-256 words verbatim in the rulings file", M256 in rul)
    e, x, w = o["e"], o["x"], o["w"]
    ok = sp.simplify(e["Ss"] - N * LN2) == 0 and sp.simplify(e["Sl"] - N * LN2) == 0
    ok &= sp.simplify(e["El"] - sp.sqrt(N * 2 * sp.pi * hb * c ** 5 * LN2 / (8 * sp.pi ** 2 * G))) == 0
    add("F1 both ends hold N ln2 on their horizons; the large end's E is the record's (N h c^5 ln2 / 8 pi^2 G)^(1/2)", ok)
    ok = sp.simplify(x["Ns"] - sp.pi ** 2 * ell ** 2 / (2 * LN2 * lP2)) == 0
    ok &= sp.simplify(x["Nl"] - sp.pi * ell ** 2 / (LN2 * lP2)) == 0 and sp.simplify(x["ratio_N"] - sp.pi / 2) == 0
    ok &= sp.simplify(x["E_equal_radius"] - 3 * sp.pi / 4) == 0
    ok &= sp.simplify(x["E_equal_N"] - sp.Rational(3, 4) * sp.sqrt(2 * sp.pi)) == 0
    add("F2 crossover at N = pi^2 ell^2/(2 ln2 l_P^2) (small) and pi ell^2/(ln2 l_P^2) (large), pi/2 apart; the ends' E "
        "agree within 3 pi/4 (equal radius) and (3/4) sqrt(2 pi) = 1.88 (equal N)", ok)
    ok = abs(w["ell0"] / w["ell_max"] - 1) < 1e-9 and abs(w["ellW"] / w["top"] - 1) < 1e-6
    ok &= "%.3g" % w["Nx0"] == "5.31e+60" and "%.3g" % w["NxW"] == "28.7" and "%.2f" % w["wx"] == "150.44"
    add("F3 ell runs from 13.964 um (floor) to 8.5415 m1 (top); the crossover from 5.31e60 to 28.7 bits; the example "
        "README switches ends at w = 150.44 of 196.885", ok)
    ok = "%.2f" % w["wx_r0"] == "149.79" and "%.2f" % w["wx_E"] == "144.98" and "%.3f" % w["rh_E"] == "0.283"
    add("F3b (item 261) the switch is a convention: 149.79 by r0 = ell, 144.98 where the E formulas agree (r_h = 0.283 "
        "ell)", ok)
    ok = not (sp.simplify(e["rh"] / l5).free_symbols - {N}) and not (sp.simplify(e["r0"] / sp.sqrt(lP2)).free_symbols - {N})
    add("F4 each end fixed by N alone in its own Planck units (r_h/l5, r0/l_P)", ok)
    return res


MUTANTS = {"small_one_side": "the small end counted over one side"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-40s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
