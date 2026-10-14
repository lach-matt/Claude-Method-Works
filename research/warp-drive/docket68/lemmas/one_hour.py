#!/usr/bin/env python3
"""one_hour.py -- item 218: the one-hour experiment.  Position 2 is "a universe identical to this one with a singular
exception, that that universe is 1 hour ahead of ours".  Its values, computed from the record's Planck 2018 inputs
(../../cosmo.py, imported read-only: H0 = 67.36 km/s/Mpc, Omega_m = 0.3153, T_CMB = 2.7255 K, N_eff = 3.046, one
0.06 eV neutrino) and 201's offset (rho_Lambda c^2 = 5.25e-10 J/m^3, constant); worked in the conversation; seated under
206; 2026-10-11.

  H1 (READ, M's words; the board's reading (a) of 218) identical: position 2 carries our defining values -- the same
     tension sigma and the same dark-energy offset (201), hence the same G and ell (sigma_defines.py), the same
     README mass m and the same horizon radius 2Gm/c^2 at position 2 (G2 = G)
  H2 (computed) flat LCDM with those inputs: Omega_r = 7.964e-5 (photons and two relativistic neutrino species, as
     cosmo.py counts them; the massive one is matter today), Omega_Lambda = 1 - Omega_m - Omega_r = 0.684620,
     deceleration q0 = Omega_m/2 + Omega_r - Omega_Lambda = -0.526891
  H3 (computed, to second order in H0 dt and checked against a direct integration of the Friedmann equation; dt = 3600 s)
     position 2 against position 1:
       H0 dt                         = 7.858760e-15
       scale factor a2/a1 - 1        = 7.858760e-15   (light from position 1's epoch reaches it redshifted by this z)
       Hubble rate H2/H1 - 1         = -(1 + q0) H0 dt = -3.718052e-15
       matter density                = a^-3: -2.357628e-14 relative
       radiation density             = a^-4: -3.143504e-14 relative
       CMB temperature               = 2.7255 K / a: -2.141905e-14 K
       dark-energy density, offset   = unchanged exactly (w = -1, 201)
       critical density 3H^2/(8 pi G) = -7.436105e-15 relative
       Omega_Lambda                  = +7.436105e-15 relative (the constant's share grows as H falls)
       age                           = 13.797 Gyr + 3600 s
  H4 (deduced from H1 and 201) by 201's two coordinates -- sigma and the offset -- position 2 and position 1 are the same
     cell: they differ in no defining value.  The bulk index needs cosmic time as a coordinate to tell them apart, and
     in that index the two positions differ in exactly one coordinate, t, by 3600 s
So position 2's precise values, for the one-hour experiment, are ours with every time-dependent quantity advanced by
one hour of cosmic expansion -- relative changes of order 1e-14 -- and every defining value unchanged.  In the bulk index
the corridor joins two cells that differ only in cosmic time.
What this does not show: what the corridor does to the traveller's own clock; anything beyond the homogeneous
background (our local surroundings an hour on are not in the background model); the conflict with 139 (1) (position 2's
plane negative, a quarter of ours) is noted, not resolved -- an identical universe's plane carries our positive sigma.
Imports ../../cosmo.py by path.  Stdlib + mpmath.  python3 one_hour.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WARP = os.path.dirname(os.path.dirname(HERE))
MUT = {}
DT = 3600.0
OFFSET = 5.25e-10                                   # rho_Lambda c^2, J/m^3 (201)
M218 = ("The warp corridor will put me in a universe identical to this one with a singular exception, that that universe "
        "is 1 hour ahead of ours.")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def compute():
    import mpmath as mp
    mp.mp.dps = 40
    co = _load(os.path.join(WARP, "cosmo.py"), "oh_cosmo")
    H0 = mp.mpf(co.H0())
    G = mp.mpf(co._G)
    c = mp.mpf(co.c)
    rhoc = 3 * H0 ** 2 / (8 * mp.pi * G)
    Og = (mp.pi ** 2 / 15) * (mp.mpf(co._KB) * co.T_CMB_K) ** 4 / (mp.mpf(co._HBAR) * c) ** 3 / c ** 2 / rhoc
    O1 = Og * mp.mpf(7) / 8 * (mp.mpf(co.N_EFF) / 3) * (mp.mpf(4) / 11) ** (mp.mpf(4) / 3)
    Om = mp.mpf(co.OMEGA_M)
    Orad = Og + 2 * O1
    OL = 1 - Om - Orad
    w = -1 if not MUT.get("w_minus_09") else mp.mpf("-0.9")
    E2 = lambda a: Om * a ** -3 + Orad * a ** -4 + OL * a ** (-3 * (1 + w))
    q0 = Om / 2 + Orad + OL * (1 + 3 * w) / 2
    x = H0 * DT
    # second-order series: a(dt) = 1 + x - q0 x^2/2 ; H(dt) = H0 (1 - (1 + q0) x)
    a2s = 1 + x - q0 * x ** 2 / 2
    # direct integration of da/dt = H0 a sqrt(E2(a)) over dt (RK4, 200 steps)
    a, n = mp.mpf(1), 200
    h = mp.mpf(DT) / n
    f = lambda aa: H0 * aa * mp.sqrt(E2(aa))
    for _ in range(n):
        k1 = f(a); k2 = f(a + h / 2 * k1); k3 = f(a + h / 2 * k2); k4 = f(a + h * k3)
        a += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    a2 = a
    H2 = H0 * mp.sqrt(E2(a2))
    rel = lambda v: float(v)
    out = {"H0": float(H0), "x": rel(x), "Om": float(Om), "Orad": float(Orad), "OL": float(OL), "q0": float(q0),
           "da": rel(a2 - 1), "da_series": rel(a2s - 1), "series_vs_int": float(abs(a2 - a2s)),
           "dH": rel(H2 / H0 - 1), "dH_series": rel(-(1 + q0) * x),
           "drho_m": rel(a2 ** -3 - 1), "drho_r": rel(a2 ** -4 - 1),
           "dT": float(mp.mpf(co.T_CMB_K) * (1 / a2 - 1)),
           "drho_L": rel(a2 ** (-3 * (1 + w)) - 1),
           "drhoc": rel((H2 / H0) ** 2 - 1),
           "dOL": rel((OL * a2 ** (-3 * (1 + w)) / E2(a2)) / OL - 1),
           "age_gyr": co.AGE_GYR, "c": float(c)}
    return out


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    text = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read().replace("\n    ", " ")
    add("H0 M's 218 verbatim in the rulings file", M218 in text)
    add("H2 flat LCDM from the record's inputs: Omega_r = 7.964e-5, Omega_Lambda = 0.684620, q0 = -0.526891",
        abs(d["Orad"] - 7.964e-5) < 1e-8 and abs(d["OL"] - 0.684620) < 1e-6 and abs(d["q0"] + 0.526891) < 1e-6)
    add("H3 one hour ahead: H0 dt = 7.858760e-15; a2/a1 - 1 = 7.858760e-15 (series and direct integration agree to "
        "1e-30); H2/H1 - 1 = -(1 + q0) H0 dt = -3.7181e-15; matter -2.3576e-14, radiation -3.1435e-14, CMB -2.1419e-14 K; "
        "dark energy unchanged exactly", abs(d["x"] - 7.858760e-15) < 1e-20 and abs(d["da"] - d["x"]) < 1e-27
        and d["series_vs_int"] < 1e-30 and abs(d["dH"] - d["dH_series"]) < 1e-27 and abs(d["dH"] + 3.718052e-15) < 1e-20
        and abs(d["drho_m"] + 2.35763e-14) < 1e-18 and abs(d["drho_r"] + 3.14350e-14) < 1e-18
        and abs(d["dT"] + 2.14190e-14) < 1e-18 and d["drho_L"] == 0.0)
    add("H4 by 201's two coordinates the positions are the same cell: no defining value differs (sigma, offset, G, ell, "
        "m identical by 218); they differ only in cosmic time, by 3600 s", d["drho_L"] == 0.0)
    return res


MUTANTS = {"w_minus_09": "dark energy entered as w = -0.9 (the offset would then change in an hour)"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-11s %-66s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("one_hour.py -- position 2 is our universe one hour ahead (item 218)\n")
    print("inputs: H0 = %.6e s^-1, Omega_m = %.4f, Omega_r = %.4e, Omega_Lambda = %.6f, q0 = %.6f" % (d["H0"], d["Om"], d["Orad"], d["OL"], d["q0"]))
    print("H0 dt                %.6e" % d["x"])
    print("a2/a1 - 1            %.6e   (series %.6e; |series - integration| %.1e)" % (d["da"], d["da_series"], d["series_vs_int"]))
    print("H2/H1 - 1            %.6e" % d["dH"])
    print("matter density       %.6e relative" % d["drho_m"])
    print("radiation density    %.6e relative" % d["drho_r"])
    print("CMB temperature      %.6e K" % d["dT"])
    print("dark energy          %.1e relative (offset %.2e J/m^3 unchanged)" % (d["drho_L"], OFFSET))
    print("critical density     %.6e relative" % d["drhoc"])
    print("Omega_Lambda         %+.6e relative" % d["dOL"])
    print("age                  %.3f Gyr + %d s" % (d["age_gyr"], DT))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
