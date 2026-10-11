#!/usr/bin/env python3
"""hold_small.py -- item 251's last step at the family's small end: O1b/O1c restated (item 259), and the hold against the
hole's temperature.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; estimates
marked; not verified by a separate session; not seated); 2026-10-11.  L4 re-read on item 260 against the write's count
redone at the small end (write_small.py); first written with the record's 4D count.

  L0 (read) M's item-259 words, verbatim in the rulings file.
  L1 (computed, exact; item 259) O1b/O1c at the small end: the static bulk, its horizon and the bridge's slice are
     regular (C1 H4-H5, verified, item 254) and the passage -- the README crossing as information across the bridge's
     slice (item 251) -- needs no geodesic through the interior.  The interior is where the incompleteness lives: a body
     falling from rest at radius R reaches r = 0 in proper time R^2/(r_h c) (computed), one clock r_h/c from rest at the
     horizon -- finite, outside the passage, admitted by item 259.
  L2 (computed, exact) The hole's capture radius for fields on the plane: null rays of f = 1 - r_h^2/r^2 have their
     photon sphere at r = sqrt2 r_h and critical impact parameter b_c = 2 r_h, so its geometric-optics absorption
     cross-section is pi b_c^2 = 4 pi r_h^2.
  L3 (estimate; Emparan-Horowitz-Myers, abstract READ: "Most of the energy goes into the modes on the brane") The hole
     radiates mainly into the plane's own fields.  As a blackbody of cross-section 4 pi r_h^2 at T = hbar c/(2 pi k
     r_h), with g* = 106.75 (all Standard Model species, T ~ 3e16 K ~ 2.8 TeV) and greybody factors between 0.1 and 1,
     the power is P = (g*/2) sigma_SB 4 (4 pi r_h^2) T^4 x greybody.  Since P ~ r_h^-2 ~ 1/E, the lifetime is E/(2P).
     For the example README at ell = 13.964 um (C2: r_h = 1.120e-20 m, E = 1.281e9 J): P = 2.1e22 W at greybody 1,
     lifetime 3.0e-14 s (3.0e-13 s at greybody 0.1).
  L4 (computed, exact in its scaling) The lifetime in the hole's own clock r_h/c grows as N and carries no ell -- t / (r_h
     /c) is fixed by N alone: 8.0e14 clocks for the example (0.29 N), at every ell.  The write at the small end
     (write_small.py S3, item 260: T >= (3/2)(5 N ln2/Z)^(1/3) - 1 clocks of r_h/c, 66,980 for the example at Z =
     106.75) grows as N^(1/3) and carries no ell either; at ell = 13.964 um it is 2.5e-24 s.  The hole outlives the
     write's floor by 1.2e10 (greybody 1), 1.2e11 (greybody 0.1); every variant of write_small S3 fits.  [First written
     with the record's 4D count, 199,702 clocks of m/c (O3-WRITE), carried into the small end's clock as 7.5e-24 s and
     outlived by 4e9 -- M, item 260: "The write's clock count is still the record's 4D derivation. Redoing it at the
     small end belongs to the WRITE row."  The record's write in its own 4D clock, 1.3e-31 s, is printed for
     comparison.]

What this does not show.
  - The evaporation's greybody factors and species beyond the Standard Model; bulk graviton emission (subdominant by
    the abstract read).
  - The WRITE row's cypher at the small end (item 260 (b)); L4 uses write_small's count, a floor.

Imports p2_gravity.py and write_small.py by path.  Stdlib + sympy.  python3 hold_small.py [--selftest | --mutants]
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
M259 = "Admitted (Recommended)"
N_EX = 2742570311524972
G_STAR = 106.75
WRITE_CLOCKS_RECORD = 199702.19                 # the record's 4D count, clocks of m/c (O3-WRITE), for comparison


def infall():
    """proper time from rest at R to r = 0 under f = 1 - r_h^2/r^2 (units c = 1): (dr/dtau)^2 = f(R) - f(r)"""
    r, R, rh = sp.symbols("r R r_h", positive=True)
    f = lambda x: 1 - rh ** 2 / x ** 2
    integrand = 1 / sp.sqrt(f(R) - f(r))
    tau = sp.simplify(sp.integrate(sp.simplify(integrand), (r, 0, R)))
    return dict(tau=tau, at_horizon=sp.simplify(tau.subs(R, rh)))


def capture():
    r, rh = sp.symbols("r r_h", positive=True)
    f = 1 - rh ** 2 / r ** 2
    if MUT.get("four_d_sphere"):
        f = 1 - rh / r
    rps = [x for x in sp.solve(sp.diff(f / r ** 2, r), r) if x.is_positive][0]
    bc = sp.simplify(rps / sp.sqrt(f.subs(r, rps)))
    return dict(rps=sp.simplify(rps), bc=bc)


def lifetime():
    spec = importlib.util.spec_from_file_location("hs_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    G, c, hbar, kB = PG.G, PG.C, PG.HBAR, 1.380649e-23
    sigma_SB = 5.670374419e-8
    L2 = math.log(2)
    spec = importlib.util.spec_from_file_location("hs_ws", os.path.join(HERE, "write_small.py"))
    WS = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(WS)
    write_clocks = WS.head_clocks()
    out = {}
    for ell in (PG.ELL_MAX, 1e-9, 1e-20):
        G5 = G * ell
        l5 = (hbar * G5 / c ** 3) ** (1 / 3)
        rh = (2 * N_EX * L2 / math.pi ** 2) ** (1 / 3) * l5
        E = 3 * math.pi * c ** 4 * rh ** 2 / (8 * G5)
        T = hbar * c / (2 * math.pi * kB * rh)
        rows = {}
        for grey in (1.0, 0.1):
            P = (G_STAR / 2) * sigma_SB * 4 * (4 * math.pi * rh ** 2) * T ** 4 * grey
            t = E / (2 * P)
            rows[grey] = dict(P=P, t=t, clocks=t / (rh / c))
        out[ell] = dict(rh=rh, E=E, T=T, rows=rows, clock=rh / c, write_s=write_clocks * rh / c)
    m = G * PG.corridor(G)["E1"] * math.sqrt(N_EX) / c ** 4
    return dict(rows=out, ell_max=PG.ELL_MAX, write_clocks=write_clocks, write_4d_s=WRITE_CLOCKS_RECORD * m / c)


def compute():
    return dict(inf=infall(), cap=capture(), life=lifetime())


def report(o):
    print("hold_small.py -- O1b/O1c restated, and the hold against the temperature (item 251, small end)\n")
    print("L1 infall from rest at R to r = 0: proper time %s; from the horizon %s" % (o["inf"]["tau"], o["inf"]["at_horizon"]))
    print("L2 photon sphere r = %s, critical impact parameter %s" % (o["cap"]["rps"], o["cap"]["bc"]))
    L = o["life"]
    for ell, x in L["rows"].items():
        print("L3 ell %.3e: r_h %.3e m, E %.3e J, T %.3e K, clock %.3e s; lifetime %.2e s (grey 1) / %.2e s (grey 0.1) = "
              "%.2e / %.2e clocks; the write's %d clocks = %.2e s" % (ell, x["rh"], x["E"], x["T"], x["clock"], x["rows"][1.0]["t"],
                                                                     x["rows"][0.1]["t"], x["rows"][1.0]["clocks"],
                                                                     x["rows"][0.1]["clocks"], L["write_clocks"],
                                                                     x["write_s"]))
    print("   for comparison, the record's 4D write (%.2f clocks of m/c) in its own clock: %.2e s" % (
        WRITE_CLOCKS_RECORD, L["write_4d_s"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("L0 M's item-259 words verbatim in the rulings file", M259 in rul)
    R, rh = sp.symbols("R r_h", positive=True)
    add("L1 infall from rest at R reaches r = 0 in proper time R^2/r_h -- one clock r_h from the horizon: finite, in the "
        "interior", sp.simplify(o["inf"]["tau"] - R ** 2 / rh) == 0 and sp.simplify(o["inf"]["at_horizon"] - rh) == 0)
    add("L2 photon sphere sqrt2 r_h, critical impact parameter 2 r_h (cross-section 4 pi r_h^2)",
        sp.simplify(o["cap"]["rps"] - sp.sqrt(2) * rh) == 0 and sp.simplify(o["cap"]["bc"] - 2 * rh) == 0)
    L = o["life"]
    x = L["rows"][L["ell_max"]]
    ok = "%.1e" % x["rows"][1.0]["t"] == "3.0e-14" and "%.1e" % x["rows"][0.1]["t"] == "3.0e-13"
    clocks = [row["rows"][1.0]["clocks"] for row in L["rows"].values()]
    ok &= max(clocks) / min(clocks) - 1 < 1e-9 and "%.1e" % clocks[0] == "8.0e+14"
    ok &= "%.2g" % (x["rows"][1.0]["t"] / x["write_s"]) == "1.2e+10" and "%.1e" % x["write_s"] == "2.5e-24"
    ok &= "%.0f" % L["write_clocks"] == "66980"
    add("L3/L4 the example's lifetime 3.0e-14 s (grey 1) to 3.0e-13 s (grey 0.1); 8.0e14 clocks at every ell; the write "
        "at the small end (write_small: 66,980 clocks = 2.5e-24 s) outlived by 1.2e10", ok)
    return res


MUTANTS = {"four_d_sphere": "the capture radius from the 4D f = 1 - r_h/r"}


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
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-48s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
