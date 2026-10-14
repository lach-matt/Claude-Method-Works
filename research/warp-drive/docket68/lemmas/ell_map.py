#!/usr/bin/env python3
"""ell_map.py -- item 378: ell isolated in the theorem.  Every place the bulk's curvature radius ell enters, its power,
its value across ell's window, what it would decide if ell were known, and what ell itself rests on.  Worked in the
conversation (computed, stdlib; READ where marked; search summary where marked; deduced where marked; not verified by a
separate session); 2026-10-14.

  E0 (read) M's words, verbatim in the rulings file, 378: "Everything comes down to ℓ".
  E1 (computed; READ) What ell is.  B6' (201, a definition) with SMS (19): G ell^2 = 3c^4/(4 pi (sigma - 2 dsigma)), so
     ell is our plane's tension sigma in other units, the offset dsigma fixed by the dark energy.  The same one unknown
     is the five-dimensional coupling G5 = G ell, the bulk's Lambda5 = -6/ell^2, the five-dimensional Planck length
     l5 = (l_P^2 ell)^(1/3), and -- through AdS/CFT, Hawking, Hertog and Reall (hep-th/0003052) eqs. (2.2), (2.17),
     READ:
     "l^3/G = 2N^2/pi", "G4 = G/l" -- the rank N of the conformal field theory dual to the bulk, N^2 = (pi/2)(ell/l_P)^2.
     Their (2.1), READ: "l = lambda^(1/4) l_s": in string theory ell is the string length times the 't Hooft coupling's
     fourth root.
  E2 (computed) The family's two ends meet at N_L = (pi^2/(2 ln2))(ell/l_P)^2, which is exactly pi N^2/ln2: the small end
     is a README with fewer bits than that CFT's count of degrees of freedom, the large end one with more.
  E3 (computed) ell's window, as the record holds it: at most 13.964 um (the table-top floor on sigma, B6P-SCALE, from
     Adelberger et al. and Maartens-Koyama (41), READ in b6p_scale); at least 22.4 l_P for a classical bulk (m1_large,
     w <= 189.9), and 8.5415 m1 = 2.0 l_P on positivity (item 197, sigma_cypher W1).  sigma^(1/4) runs from 9.18e3 GeV at
     the ceiling to 1.80e18 GeV at the classical floor; N runs from 1.08e30 to 28.
  E4 (computed) The theorem's headline small-end numbers take ell at its ceiling.  For the identity-core README
     (N = 2.7426e15): r_h = 1.12008e-20 m x (ell/ceiling)^(1/3), E = 1.2810e9 J x (ell/ceiling)^(-1/3), r_h/ell =
     8.0e-16 x (ell/ceiling)^(-2/3), the classical core r_c = 7.09e-23 m x (ell/ceiling)^(1/3).  No row's status turns
     on these values: the rows are proved in N and ell.
  E5 (computed) The interior.  273's region begins at the Planck curvature (360 (c)), which in units of ell is
     (ell/l5)^4 = (ell/l_P)^(8/3): 6.77e79 at the ceiling, 3.99e3 at the classical floor.  The runs reach 2.5e3, which is
     (ell/l_P)^(8/3) at ell = 18.8 l_P, below the classical floor: for no ell in the window does an evolution so far
     reach the Planck curvature.  The interior problem in units of ell depends on r0/ell alone; ell sets only how far
     it must be carried.
  E6 (computed) The large end: its start at m = ell/1.596 (1.18e22 kg at the ceiling), its corrections (ell/r0)^2, the
     Earth's cap at r0/ell = 635 at the ceiling (372), and the Earth's own README on the small end for every ell above
     0.584 nm (earth_cap K5).  Position 2's bulk at 139 (1)'s quarter has 2 ell (k_R = k_L/2).
  E7 (computed) The ledger: the small end's E for the identity core stays under the assembly ceiling 1.1947e10 J (T3s,
     no sink) only for ell >= 17.2 nm -- informational, since item 239 set the ceiling aside as the build's need.
  E8 (computed; search summary) Scales a tension could take: TeV gives ell = 1.18 mm (excluded by the table-top); 1e11
     GeV, 1.2e-19 m; the GUT scale 1e16 GeV, 1.2e-29 m (Planck span 4.3e15); the reduced Planck scale, 12.3 l_P, below
     the classical floor.  The dark energy's own length (hbar c/dsigma)^(1/4) = 88.1 um is 6.3 times the ceiling; the
     "dark dimension" proposal (Montero, Vafa and Valenzuela, arXiv:2205.12293, search summary) ties one extra
     dimension's size to the dark energy at about a micron -- for a flat compact dimension, not a warped one.
  E9 (deduced) What ell rests on, and what knowing it decides.  Nothing in the theory sets sigma (sigma_cypher C1-C3,
     201), so nothing sets ell: it is the theory's one free scale.  Closing it takes one input of a named kind: a
     measurement (gravity deviating from Newton's law as 2 ell^2/(3 r^2) below about 14 um), the hidden CFT's rank N or
     string data, or a tie to something the theory already holds (the offset, a corridor, the README).  Known, ell would
     fix where the two ends meet, the small end's numbers, the large end's range in units of ell, and how far the
     interior must be carried; it would not by itself change a row's status.

Imports p2_gravity.py by path.  Stdlib only.
python3 ell_map.py [--selftest | --mutants]
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
WORDS = ((378, "Everything comes down to ℓ"),)
HHR = ("l^3/G = 2N^2/pi", "G4 = G/l", "l = lambda^(1/4) l_s")     # hep-th/0003052 (2.2), (2.17), (2.1), READ
N_CORE = 2.7426e15                       # the identity-core README behind the theorem's 1.12008e-20 m (item 108)
A_CEIL = 1.1947e10                       # T3's assembly ceiling, J
RUNS_K = 2.5e3                           # the curvature the large end's interior runs reach, ell^-4 (README C4)
FLOOR_LP, POS_M1, START = 22.4, 8.5415, 1.596
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


def compute():
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "em_pg")
    c, G, hb, LN2, dsig, ceil = pg.C, pg.G, pg.HBAR, pg.LN2, pg.DSIG, pg.ELL_MAX
    eV = 1.602176634e-19
    lP = math.sqrt(hb * G / c ** 3)
    m1 = lP * math.sqrt(LN2 / math.pi) / 2
    nrs2 = lambda e: (math.pi / 2) * (e / lP) ** 2 * (2.0 if MUT.get("hhr_g4_twice") else 1.0)
    NL = lambda e: (math.pi ** 2 / (2 * LN2)) * (e / lP) ** 2
    l5 = lambda e: (lP ** 2 * e) ** (1 / 3)
    span = lambda e: (e / l5(e)) ** 4
    sig = lambda e: 3 * c ** 4 / (4 * math.pi * G * e ** 2) + 2 * dsig
    gev = lambda s: (s * (hb * c) ** 3) ** 0.25 / eV / 1e9
    def small(N, e):
        rh = (2 * N * LN2 / math.pi ** 2) ** (1 / 3) * l5(e)
        G5 = G * e * (1.5 if MUT.get("g5_three_halves") else 1.0)
        return rh, 3 * math.pi * c ** 4 * rh ** 2 / (8 * G5), 72 ** 0.125 * math.sqrt(rh * l5(e))
    floor, pos = FLOOR_LP * lP, POS_M1 * m1
    win = {k: dict(ell=e, lp=e / lP, NL=NL(e), N=math.sqrt(nrs2(e)), span=span(e), gev=gev(sig(e)))
           for k, e in (("ceiling", ceil), ("floor", floor), ("positivity", pos))}
    rh, E, rc = small(N_CORE, ceil)
    rh2, E2, rc2 = small(N_CORE, ceil * 8)
    ell_reach = lP * RUNS_K ** (3 / 8)
    M_earth = 3.986004418e14 / G
    snap = 1.088e29 * M_earth / 70.0
    ell_A = ceil * (E / A_CEIL) ** 3
    scales = {}
    for nm, Eg in (("TeV", 1e3), ("1e11 GeV", 1e11), ("GUT", 1e16), ("reduced Planck", 2.435e18)):
        s = (Eg * 1e9 * eV) ** 4 / (hb * c) ** 3
        e = math.sqrt(3 * c ** 4 / (4 * math.pi * G * (s - 2 * dsig)))
        scales[nm] = dict(ell=e, lp=e / lP, span=span(e))
    Ld = (hb * c / dsig) ** 0.25
    return dict(win=win, NL_over=NL(ceil) / (math.pi * nrs2(ceil) / LN2), rh=rh, E=E, q=rh / ceil, rc=rc,
                pw_rh=math.log(rh2 / rh) / math.log(8), pw_E=math.log(E2 / E) / math.log(8),
                pw_rc=math.log(rc2 / rc) / math.log(8), ell_reach=ell_reach / lP,
                m_start=ceil / START * c ** 2 / G, earth_q=2 * G * M_earth / c ** 2 / ceil,
                earth_readme_ell=lP * math.sqrt(snap * 2 * LN2 / math.pi ** 2), ell_A=ell_A, scales=scales,
                Ld=Ld, Ld_ratio=Ld / ceil)


def report(o):
    print("ell_map.py -- ell isolated in the theorem (item 378)\n")
    for k, w in o["win"].items():
        print("E3 %-10s ell %.4e m = %.3e l_P | N_L %.4e | N %.3e | Planck span %.3e ell^-4 | sigma^(1/4) %.3e GeV"
              % (k, w["ell"], w["lp"], w["NL"], w["N"], w["span"], w["gev"]))
    print("E2 N_L / (pi N^2/ln2) = %.12f" % o["NL_over"])
    print("E4 at the ceiling: r_h %.5e m, E %.4e J, r_h/ell %.2e, r_c %.3e m; powers of ell %.3f, %.3f, %.3f"
          % (o["rh"], o["E"], o["q"], o["rc"], o["pw_rh"], o["pw_E"], o["pw_rc"]))
    print("E5 the runs' 2.5e3 is the Planck span at ell = %.1f l_P" % o["ell_reach"])
    print("E6 large end's start %.3e kg; the Earth's cap r0/ell %.1f; the Earth's README small-end above %.3e m"
          % (o["m_start"], o["earth_q"], o["earth_readme_ell"]))
    print("E7 E_small <= the assembly ceiling needs ell >= %.3e m" % o["ell_A"])
    for k, s in o["scales"].items():
        print("E8 %-15s ell %.3e m = %.3e l_P, Planck span %.2e" % (k, s["ell"], s["lp"], s["span"]))
    print("E8 dark-energy length %.3e m = %.2f x the ceiling" % (o["Ld"], o["Ld_ratio"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    w = o["win"]
    add("E0 378 verbatim inside its own item", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("E2 N_L is exactly pi N^2/ln2 with HHR's N^2 = (pi/2)(ell/l_P)^2", abs(o["NL_over"] - 1) < 1e-12)
    add("E3 the window: 8.640e29 l_P (N 1.08e30, 9.18e3 GeV) to 22.4 l_P (N 28.1, 1.80e18 GeV); positivity 2.0 l_P",
        "%.3e" % w["ceiling"]["lp"] == "8.640e+29" and "%.2e" % w["ceiling"]["N"] == "1.08e+30"
        and "%.3g" % w["ceiling"]["gev"] == "9.18e+03" and "%.3g" % w["floor"]["N"] == "28.1"
        and "%.3g" % w["floor"]["gev"] == "1.8e+18" and "%.2g" % w["positivity"]["lp"] == "2")
    add("E4 the headline small-end numbers are the ceiling's: 1.12008e-20 m, 1.2810e9 J, 8.0e-16, 7.09e-23 m; powers "
        "1/3, -1/3, 1/3", "%.5e" % o["rh"] == "1.12008e-20" and "%.4e" % o["E"] == "1.2810e+09"
        and "%.1e" % o["q"] == "8.0e-16" and "%.3g" % o["rc"] == "7.09e-23" and abs(o["pw_rh"] - 1 / 3) < 1e-9
        and abs(o["pw_E"] + 1 / 3) < 1e-9 and abs(o["pw_rc"] - 1 / 3) < 1e-9)
    add("E5 the Planck span 6.77e79 at the ceiling, 3.99e3 at the floor; the runs' reach is 18.8 l_P, below the floor",
        "%.3g" % w["ceiling"]["span"] == "6.77e+79" and "%.3g" % w["floor"]["span"] == "3.99e+03"
        and "%.3g" % o["ell_reach"] == "18.8" and o["ell_reach"] < FLOOR_LP)
    add("E6 the large end's start 1.18e22 kg, the Earth's cap at 635 ell, the Earth's README small-end above 0.584 nm",
        "%.3g" % o["m_start"] == "1.18e+22" and round(o["earth_q"]) == 635
        and "%.3g" % o["earth_readme_ell"] == "5.84e-10")
    add("E7 the ledger's no-sink condition at the small end needs ell >= 17.2 nm", "%.3g" % o["ell_A"] == "1.72e-08")
    s = o["scales"]
    add("E8 TeV 1.18 mm; GUT 1.18e-29 m (span 4.3e15); reduced Planck 12.3 l_P; the dark-energy length 88.1 um, 6.31x",
        "%.3g" % s["TeV"]["ell"] == "0.00118" and "%.3g" % s["GUT"]["ell"] == "1.18e-29"
        and "%.2g" % s["GUT"]["span"] == "4.3e+15" and "%.3g" % s["reduced Planck"]["lp"] == "12.3"
        and "%.3g" % o["Ld"] == "8.81e-05" and "%.3g" % o["Ld_ratio"] == "6.31")
    return res


MUTANTS = {"hhr_g4_twice": "HHR's N read with G4 = 2 G5/ell, the other brane convention (E2, E3)",
           "g5_three_halves": "the small end's E under G5 = (3/2) G ell instead of the theorem's G ell (E4, E7)"}


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
        print("  mutant %-16s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
