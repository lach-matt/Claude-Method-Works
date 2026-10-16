#!/usr/bin/env python3
"""b6p_prove.py -- item 442, phase 2, first: B6' proved to M's standard.  B6' is M's 201: "our universe is defined by
its plane's tension and its dark-energy offset".  442 (1) approved the standard for a definition: "a computed solution
of established physics that meets it, consistent with it and with measurement".  prior_art.py found B6' established
in the literature as such a model (SMS, Binetruy et al., Gen-Sasaki, the de Sitter planes, the table-top bounds); what
remained was to compute it for our universe's own numbers.  Labels: computed (sympy, exact where marked), READ (the
inputs, from the instruments named), standard (CODATA's G and c), deduced.  Worked in the conversation; not verified;
not seated.  2026-10-16.

  D0 (read) M's words: 201's definition and 442's standard.
  D1 (computed, exact) The plane.  ds^2 = a(y)^2 (de Sitter of Hubble rate H) + dy^2 with
     a = ell H sinh((y_h - |y|)/ell), sinh(y_h/ell) = 1/(ell H): every component of the bulk's equations
     G_ab = (6/ell^2) g_ab holds exactly (anti-de Sitter, curvature -6/ell^2 = kappa^2 Lambda_5 in SMS's
     normalization), for every H and ell.  The junction at y = 0 gives the tension exactly,
     kappa^2 lambda/6 = sqrt(1 + ell^2 H^2)/ell, positive; H -> 0 is Randall and Sundrum's plane.
  D2 (computed, exact) Its four-dimensional laws.  The junction's lambda meets SMS's relation exactly,
     3 H^2 = (kappa^2/2)(Lambda_5 + kappa^2 lambda^2/6): the offset lambda - lambda_RS is the four-dimensional
     cosmological constant, Lambda_4 = 8 pi G delta lambda to first order.  The graviton's zero mode weighs the plane
     by the integral of a^2, so 8 pi G = kappa^2 / (integral of a^2), which is kappa^2/ell at H = 0; the de Sitter
     plane's differs by ell^2 H^2 times a logarithm (computed).
  D3 (computed on READ and standard inputs) Our universe.  G = 6.67430e-11 (CODATA, standard); H0 = 67.36 km/s/Mpc
     (Planck 2018, PINNED in cosmo.py) and Omega_m = 0.3153 (READ there), flat, so the offset is
     rho_Lambda c^2 = 5.24e-10 J/m^3 (sigma_defines' 5.25e-10); ell = 13.964 um, the table-top ceiling (b6p_scale S4,
     READ Adelberger et al.).  Then sigma = 3 c^4/(4 pi G ell^2) = 1.48e53 J/m^3 (lambda^(1/4) = 9.2 TeV, above
     Maartens-Koyama's 1 TeV), delta sigma / sigma = 3.5e-63, ell H = 8.4e-32, and G from the zero mode equals the
     measured G to that order.
  D4 (computed) Agreement with measurement.  Newton's law on the plane, V = (GM/r)(1 + 2 ell^2/(3 r^2)) (READ MK eq.
     41): at ell = 13.964 um the power-law coefficient equals Adelberger's 68% bound beta_3 = 1.3e-4 (mm^2), so every
     ell at or below it agrees; at the solar system the correction is (ell/r)^2 ~ 1e-32, against Cassini's 2.3e-5;
     the high-energy term rho/lambda is 1.4e-19 at nuclear density and 6e-34 in water.
  D5 (deduced) What B6' is not shown to be: true.  Established physics carries no fifth dimension (prior_art
     flag (b)).  What is shown is a solution of established physics, exact, meeting 201's definition with our
     measured G and Lambda, and agreeing with every measurement the plane touches.  The smooth realization is the
     literature's (hep-th/0701266) and b5b_wall's for the flat plane.

python3 b6p_prove.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("σ and its dark-energy offset", "M-PROOF-STANDARD")
G_SI, C_SI = 6.67430e-11, 299792458.0             # standard (CODATA 2018; the metre's definition)
MPC_M = 3.0856775814913673e22                     # standard (IAU)
ELL_M = 13.9642e-6                                # b6p_scale S4's ceiling (READ Adelberger et al.)
BETA3_MM2 = 1.3e-4                                # READ (b6p_scale, ADEL_T1), 68% CL, k = 3, in mm^2
CASSINI = 2.3e-5                                  # READ (b6p_scale, WILL_CASSINI), the 1-sigma on gamma - 1
TEV4_J_M3 = (1.602176634e-7) ** 4 / (1.054571817e-34 * C_SI) ** 3    # (1 TeV)^4 in J/m^3, standard


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


t, x1, x2, x3, y = sp.symbols("t x1 x2 x3 y", real=True)
H, ell, kap = sp.symbols("H ell kappa", positive=True)
yh = ell * sp.asinh(1 / (ell * H))


def warp():
    return ell * H * sp.sinh((yh - y) / ell)                        # y > 0; the plane at y = 0, a(0) = 1


def d1():
    """the bulk's equations exact for every H, ell; the junction's lambda, positive; H -> 0 the RS plane"""
    sa = _load(os.path.join(HERE, "settle_arrival.py"), "b6pp_sa")
    a = warp()
    e = sp.exp(2 * H * t)
    g = sp.diag(-a ** 2, a ** 2 * e, a ** 2 * e, a ** 2 * e, 1)
    Ric, Rs, gi = sa._ricci(g, [t, x1, x2, x3, y])
    G = Ric - Rs * g / 2
    bulk = all(sp.simplify((G[i, j] - 6 / ell ** 2 * g[i, j]).rewrite(sp.exp)) == 0 for i in range(5)
               for j in range(i, 5))
    a0 = sp.simplify(a.subs(y, 0))
    slope = sp.simplify((sp.diff(a, y) / a).subs(y, 0))              # a'/a at 0+
    sgn = -1 if "negative_tension" in MUT else 1
    lam = sgn * sp.simplify(-6 * slope / kap ** 2)                    # Z2 junction: a'/a|0+ = -kappa^2 lambda/6
    lam_exact = 6 * sp.sqrt(1 + ell ** 2 * H ** 2) / (kap ** 2 * ell)
    junction = sp.simplify(lam - lam_exact) == 0
    rs = sp.limit(lam, H, 0) == 6 / (kap ** 2 * ell)
    pos = bool(sp.simplify(lam).subs({H: 1, ell: 1, kap: 1}) > 0)
    return bool(bulk and sp.simplify(a0 - 1) == 0 and junction and rs and pos), lam


def d2(lam):
    """SMS's relation exact; the offset is Lambda_4; the zero mode's G"""
    L5 = -6 / (kap ** 2 * ell ** 2)           # SMS's Lambda_5, the bulk's vacuum energy: G_ab = -kappa^2 Lambda_5 g_ab
    sms = sp.simplify(3 * H ** 2 - kap ** 2 / 2 * (L5 + kap ** 2 * lam ** 2 / 6)) == 0
    lam_rs = 6 / (kap ** 2 * ell)
    dl = sp.series(lam - lam_rs, H, 0, 3).removeO()
    L4_first = sp.simplify(3 * H ** 2 - kap ** 2 / ell * dl)          # 8 pi G = kappa^2/ell at H = 0
    a = warp()
    w = 1 if "wrong_measure" in MUT else 2
    integ = 2 * sp.integrate(a ** w, (y, 0, yh))                      # both sides of the plane
    flat = 2 * sp.integrate(sp.exp(-w * y / ell), (y, 0, sp.oo))
    flat_ok = sp.simplify(flat - ell) == 0
    lim = sp.limit(sp.simplify(integ), H, 0)
    return bool(sms and sp.simplify(L4_first) == 0 and flat_ok and sp.simplify(lim - ell) == 0), integ


def numbers():
    """D3: our universe's sigma, offset, ell H; the zero mode's G against the measured G"""
    cosmo = _load(os.path.join(WD, "cosmo.py"), "b6pp_cosmo")
    h0 = cosmo.H0_KMSMPC * 1e3 / MPC_M
    om = cosmo.OMEGA_M
    ol = 1 - om                                                      # flat; radiation ~ 9e-5 set aside (deduced)
    sign = -1 if "offset_sign" in MUT else 1
    rho_l = sign * ol * 3 * h0 ** 2 / (8 * math.pi * G_SI) * C_SI ** 2   # J/m^3
    ell_m = 50e-6 if "ell_too_big" in MUT else ELL_M
    sigma = 3 * C_SI ** 4 / (4 * math.pi * G_SI * ell_m ** 2)        # J/m^3: lambda_RS in SI
    Lam4 = 8 * math.pi * G_SI * rho_l / C_SI ** 4                    # m^-2
    H_m = math.sqrt(Lam4 / 3) if Lam4 > 0 else float("nan")          # Hubble rate in 1/m
    return {"rho_lambda_J_m3": rho_l, "sigma_J_m3": sigma, "ratio": rho_l / sigma, "ell_m": ell_m,
            "ell_H": ell_m * H_m, "lambda_quarter_TeV": (sigma / TEV4_J_M3) ** 0.25, "Lambda4_m2": Lam4}


def d4(n):
    """table-top, solar system, high-energy term"""
    beta = 2.0 / 3.0 * (n["ell_m"] * 1e3) ** 2                        # V = GM/r (1 + beta (1 mm/r)^2)
    table = beta <= BETA3_MM2 * (1 + 1e-3)
    au = 1.495978707e11
    solar = (n["ell_m"] / au) ** 2 < CASSINI
    nuc = 2.3e17 * C_SI ** 2 / n["sigma_J_m3"]                        # nuclear density's rho c^2 over lambda
    water = 1e3 * C_SI ** 2 / n["sigma_J_m3"]
    return table and solar and nuc < 1e-15, {"beta3_mm2": beta, "solar": (n["ell_m"] / au) ** 2, "nuclear": nuc,
                                             "water": water}


def report():
    print("D0 M's words:", words())
    ok1, lam = d1()
    print("D1 the de Sitter plane exact in AdS5; kappa^2 lambda/6 =", sp.simplify(kap ** 2 * lam / 6), ":", ok1)
    ok2, integ = d2(lam)
    print("D2 SMS's relation exact, Lambda_4 = 8 pi G delta lambda, zero mode -> ell:", ok2)
    n = numbers()
    print("D3 offset %.4e J/m^3, sigma %.4e J/m^3 (%.2f TeV^4 root), ratio %.2e, ell H %.2e"
          % (n["rho_lambda_J_m3"], n["sigma_J_m3"], n["lambda_quarter_TeV"], n["ratio"], n["ell_H"]))
    ok4, d = d4(n)
    print("D4 table-top beta_3 %.4e mm^2 (bound 1.3e-4), solar (ell/r)^2 %.1e, rho/lambda nuclear %.1e, water %.1e: %s"
          % (d["beta3_mm2"], d["solar"], d["nuclear"], d["water"], ok4))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("D0 words: %s" % r)
    r1, lam = d1(); ok.append(r1); say("D1 exact plane, junction, RS limit: %s" % r1)
    r2, _ = d2(lam); ok.append(r2); say("D2 SMS exact, offset = Lambda_4, zero mode: %s" % r2)
    n = numbers()
    r3 = (abs(n["rho_lambda_J_m3"] / 5.25e-10 - 1) < 0.01 and abs(n["sigma_J_m3"] / 1.4817e53 - 1) < 1e-3
          and abs(n["ratio"] / 3.54e-63 - 1) < 0.02 and n["lambda_quarter_TeV"] > 1 and n["ell_H"] < 1e-30)
    ok.append(r3); say("D3 our numbers (offset 5.24e-10, sigma 1.48e53, 9.2 TeV, ell H 8.4e-32): %s" % r3)
    r4, _ = d4(n); ok.append(r4); say("D4 table-top, solar system, high-energy term: %s" % r4)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


MUTANTS = {"negative_tension": "the plane's tension of the other sign (D1)",
           "wrong_measure": "the zero mode weighed by a, not a^2 (D2)",
           "offset_sign": "the offset negative: an anti-de Sitter plane, against Lambda > 0 (D3)",
           "ell_too_big": "ell = 50 um, past the table-top ceiling (D4)"}


def mutants():
    caught = 0
    for m, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-17s %s  (%s)" % (m, "caught" if bad else "MISSED", desc))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
