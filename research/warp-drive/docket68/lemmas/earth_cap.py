#!/usr/bin/env python3
"""earth_cap.py -- items 370-372: the largest corridor the theorem must prove is the one large enough for the Earth
(M-EARTH-CAP, (B): the corridor at the Earth's crossover N*, whose one E is the Earth's rest energy), and only one
README ever crosses, so for the Earth it holds every README of the Earth as one, is finite and in practice is (A)
(M-ONE-README).  Worked in the conversation (computed, stdlib; READ where marked; deduced and estimate where marked;
not verified by a separate session); 2026-10-13.

  K0 (read) The words, verbatim in the rulings file: 370 "Perhaps we can limit the large end to the current earth
     mass"; 371 "the largest warp carridor we need to prove would be large enough for the earth itself"; 372 "There is
     only ever one README that goes".
  K1 (computed) The crossover of item 108, N* = 8 pi^2 G M^2/(h c ln2), reproduces the record's 1.875e20 bits for 70 kg;
     for the Earth (GM = 3.986004418e14 m^3/s^2, the IERS value, not READ here; G CODATA 2018 as p2_gravity carries it)
     it is 1.3651e66 bits.  It is the corridor whose horizon is the Earth-mass Schwarzschild horizon (4 pi r0^2 =
     N A_bit, r0 = 2GM/c^2 = 8.870 mm) and whose one E = E1 sqrt(N) is the Earth's rest energy, 5.3675e41 J.
  K2 (computed) Against the theorem's present top, the Nariai cap N_max = 1.5918e122 (p2_gravity.corridor): the cap is
     8.6e-57 of it.  The large end becomes finite: from its start (ell/m = 1.596) to N*.
  K3 (computed) At ell's table-top ceiling, 13.964 um: r0/ell = 635.2, ell^2/r0^2 = 2.48e-6 (the plane's reading is
     four-dimensional Schwarzschild to that order at the top, FW and Abdolrahimi et al. as C3 reads them); the large end
     starts at 1.178e22 kg (r0 = 1.253 ell), 507 times below the Earth.  The cap stays at the large end for every ell
     below 1.596 m_earth = 7.08 mm, which the window's ceiling is far inside.
  K4 (computed) The offset drops out of the large end: r0^2 Lambda4 at the cap is 8.6e-57 (Lambda4 = 8 pi G dsigma/c^4
     from p2_gravity's offset), so the flat-plane solutions the interior is computed on hold there to that order; the
     Nariai end, where the offset entered, is outside the goal.
  K5 (estimate) (A), the Earth's one README: item 108's full atomic snapshot, 1.088e29 bits for 70 kg, scaled by mass,
     is 9.3e51 bits (order 1e51-1e52; an atom-count scaling is a few times lower).  It is 6.8e-15 of N*, so it lies
     within (B) and appears negative in item 108's deficit sense.  It is at the small end, N below
     N_L = (pi^2/(2 ln2)) (ell/l_P)^2, for every ell above 5.84e-10 m, and at the large end below that.
  K6 (deduced) The board's reading of 372: (B) is the bound independent of ell, and it covers (A) wherever ell falls in
     the window, so the large end proved up to N* proves the Earth's corridor at either end.  O1b and O1c at the large
     end stay OPEN; their family is now finite.  The cap does not fix ell: at the cap r0/ell runs from 635 (ceiling) to
     2.45e31 (the floor 22.4 l_P).  Nor can the Earth's own gravity see ell: MK's correction 2 ell^2/(3 r^2) is 3.2e-24
     at its surface (R = 6.371e6 m, standard value) with ell at the ceiling.
  K7 (estimate) What the cap supplies the interior: a calibrated target.  Inside the horizon the plane reads the
     four-dimensional Schwarzschild interior until the curvature radius reaches ell (K = 12 r0^2/r^6 = ell^-4, taken as
     the edge; radial geodesic from rest at the horizon): 99.87 % of the proper time to r = 0 at r0/ell = 635, 95.8 % at
     r0/ell = 20 (the largest FW hole computed), none at 1.13 (where the interior runs sit).

Imports p2_gravity.py by path.  Stdlib only.
python3 earth_cap.py [--selftest | --mutants]
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
MUT = {}
WORDS = ((370, "Perhaps we can limit the large end to the current earth mass"),
         (371, "the largest warp carridor we need to prove would be large enough for the earth itself"),
         (372, "There is only ever one README that goes"))
GM_EARTH = 3.986004418e14                 # m^3/s^2, IERS conventions (standard value, not READ in this session)
SNAPSHOT = (1.088e29, 70.0)               # item 108's full atomic snapshot: bits, for a body of kg
ELL_START = 1.596                         # ell/m at the large end's start (WARPTHEOREM, 355 Q14)
LP_FLOOR = 22.4                           # ell >= 22.4 l_P, a classical bulk (WARPTHEOREM)
R_EARTH = 6.371e6                         # m, the Earth's mean radius (standard value, not READ in this session)
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


def share(q):
    """the share of the proper time from the horizon to r = 0 (radial geodesic from rest at the horizon) spent before
    the four-dimensional Kretschmann 12 r0^2/r^6 reaches ell^-4, for r0/ell = q; None when it is there at the horizon"""
    xe = 12 ** (1 / 6) * q ** (-2 / 3) if not MUT.get("edge_at_r0") else q ** (-1)
    if xe >= 1:
        return None
    rem = math.asin(math.sqrt(xe)) - math.sqrt(xe) * math.sqrt(1 - xe)
    return 1 - rem / (math.pi / 2)


def compute():
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "ec_pg")
    C, G, H, HB, LN2 = pg.C, pg.G, pg.H, pg.HBAR, pg.LN2
    h_ = HB if MUT.get("hbar_for_h") else H
    nstar = lambda M: 8 * math.pi ** 2 * G * M ** 2 / (h_ * C * LN2)
    M = GM_EARTH / G * (1.01 if MUT.get("earth_heavier") else 1.0)
    co = pg.corridor(G)
    A_bit = co["A_bit"] if not MUT.get("abit_no_ln2") else co["A_bit"] / LN2
    r0 = 2 * G * M / C ** 2
    N = nstar(M)
    lP = math.sqrt(HB * G / C ** 3)
    ell = pg.ELL_MAX
    NL = lambda e: (math.pi ** 2 / (2 * LN2)) * (e / lP) ** 2
    dsig = pg.DSIG * (10.0 if MUT.get("offset_x10") else 1.0)
    L4 = 8 * math.pi * G * dsig / C ** 4
    snap_bits, snap_kg = SNAPSHOT
    A = snap_bits * (M / snap_kg if not MUT.get("snapshot_unscaled") else 1.0)
    m_start = ell / ELL_START
    return dict(n70=nstar(70.0), N=N, r0=r0, area_N=4 * math.pi * r0 ** 2 / A_bit, E=co["E1"] * math.sqrt(N),
                Mc2=M * C ** 2, N_max=co["N_max"], frac=N / co["N_max"], q_top=r0 / ell, corr=(ell / r0) ** 2,
                M_start=m_start * C ** 2 / G, r_start=2 * m_start / ell, ell_leave=ELL_START * G * M / C ** 2,
                lam_r0=r0 ** 2 * L4, A=A, A_over_N=A / N, ell_A=lP * math.sqrt(A * 2 * LN2 / math.pi ** 2),
                N_over_NL=N / NL(ell), q_floor=r0 / (LP_FLOOR * lP), surf=2 * ell ** 2 / (3 * R_EARTH ** 2),
                share={q: share(q) for q in (635.2, 20.0, 1.13)})


def report(o):
    print("earth_cap.py -- the largest corridor the theorem must prove (items 370-372)\n")
    print("K1 N*(70 kg) %.4g; N*(Earth) %.5g bits; r0 %.4g m; 4 pi r0^2/A_bit %.5g; E1 sqrt(N) %.5g J = M c^2 %.5g J"
          % (o["n70"], o["N"], o["r0"], o["area_N"], o["E"], o["Mc2"]))
    print("K2 N_max %.5g; N*/N_max %.2g" % (o["N_max"], o["frac"]))
    print("K3 at ell = 13.964 um: r0/ell %.1f, ell^2/r0^2 %.3g; the large end starts at %.4g kg (r0 = %.3f ell), %.0f "
          "times below; the cap leaves the large end only for ell above %.3g m" % (
              o["q_top"], o["corr"], o["M_start"], o["r_start"], o["Mc2"] / o["M_start"] / 299792458.0 ** 2,
              o["ell_leave"]))
    print("K4 r0^2 Lambda4 at the cap %.2g" % o["lam_r0"])
    print("K5 (A) ~ %.2g bits, %.2g of N*; at the small end for ell above %.3g m" % (o["A"], o["A_over_N"], o["ell_A"]))
    print("K6 N*/N_L at the ceiling %.3g; r0/ell at the cap with ell at the floor %.3g; the Earth's surface sees ell as "
          "2 ell^2/(3 R^2) = %.2g" % (o["N_over_NL"], o["q_floor"], o["surf"]))
    print("K7 the Schwarzschild share of the interior's proper time: %s" % ", ".join(
        "r0/ell %g: %s" % (q, "%.2f %%" % (100 * s) if s is not None else "none") for q, s in o["share"].items()))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("K0 370, 371 and 372 verbatim, each inside its own item",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    add("K1 N* reproduces item 108's 1.875e20 for 70 kg; the Earth's N* is 1.3651e66, the Earth-mass horizon's bits, "
        "and its one E is the Earth's rest energy", "%.4g" % o["n70"] == "1.875e+20" and "%.5g" % o["N"] == "1.3651e+66"
        and abs(o["area_N"] / o["N"] - 1) < 1e-12 and abs(o["E"] / o["Mc2"] - 1) < 1e-6
        and "%.4g" % o["r0"] == "0.00887")
    add("K2 the cap is 8.6e-57 of the Nariai cap", "%.2g" % o["frac"] == "8.6e-57")
    add("K3 at the ceiling r0/ell 635.2, ell^2/r0^2 2.48e-6; the large end starts at 1.178e22 kg (r0 = 1.253 ell); the "
        "cap leaves the large end only above 7.08 mm", "%.1f" % o["q_top"] == "635.2" and "%.3g" % o["corr"] ==
        "2.48e-06" and "%.4g" % o["M_start"] == "1.178e+22" and "%.3f" % o["r_start"] == "1.253"
        and "%.3g" % o["ell_leave"] == "0.00708")
    add("K4 the offset at the cap, r0^2 Lambda4, is 8.6e-57", "%.2g" % o["lam_r0"] == "8.6e-57")
    add("K5 (A) 9.3e51 bits, 6.8e-15 of N*, small end above ell = 5.84e-10 m", "%.2g" % o["A"] == "9.3e+51"
        and "%.2g" % o["A_over_N"] == "6.8e-15" and "%.3g" % o["ell_A"] == "5.84e-10")
    add("K6 the cap at the large end at the ceiling (N*/N_L 2.57e5) and r0/ell 2.45e31 at the floor: ell not fixed; the "
        "Earth's surface sees ell at 3.2e-24", "%.3g" % o["N_over_NL"] == "2.57e+05" and "%.3g" % o["q_floor"] ==
        "2.45e+31" and "%.2g" % o["surf"] == "3.2e-24")
    s = o["share"]
    add("K7 the Schwarzschild share: 99.87 % at r0/ell 635.2, 95.8 % at 20, none at 1.13",
        s[1.13] is None and "%.4f" % s[635.2] == "0.9987" and "%.3f" % s[20.0] == "0.958")
    return res


MUTANTS = {"hbar_for_h": "the crossover with hbar in place of h (K1)",
           "earth_heavier": "the Earth's mass read 1 % high (K1-K4)",
           "abit_no_ln2": "the bit's area without its ln2 (K1)",
           "offset_x10": "the offset read ten times too large (K4)",
           "snapshot_unscaled": "item 108's snapshot taken for the Earth without scaling (K5)",
           "edge_at_r0": "Schwarzschild's edge put at r = ell instead of where the curvature reaches ell^-4 (K7)"}


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
        print("  mutant %-18s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
