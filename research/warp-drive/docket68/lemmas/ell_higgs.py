#!/usr/bin/env python3
"""ell_higgs.py -- item 382: the window's top, for the math; and the object that would force the Higgs quartic to vanish
at the bulk's five-dimensional Planck energy, lambda(E5) = 0 (381's route: an equality from relativity, by means of the
Higgs tie).  Worked in the conversation (computed, stdlib, with p2_offset's three-loop run; READ where marked; deduced
and estimate where marked; not verified by a separate session); 2026-10-14.

  H0 (read) M's words, verbatim in the rulings file, 382: "that is a question for the math"; "agreed, continue".
  H1 (READ) Gravity's own fixed point for lambda.  Shaposhnikov and Wetterich, arXiv:0912.0208, READ: "For a positive
     gravity induced anomalous dimension A_λ > 0 the running of the quartic scalar self interaction λ at scales beyond
     the Planck mass is determined by a fixed point at zero"; "λ(k_tr) ≈ 0, β_λ(k_tr) ≈ 0", k_tr the scale where gravity
     becomes strong; "We expect this form to hold for a wide class of theories with an ultraviolet fixed point, where the
     high energy regime may involve additional fields or even higher dimensions"; "The case A_λ > 0 is favored by
     explicit computations existing in the literature".
  H2 (READ) Black holes seed Higgs vacuum decay, on a brane too.  Burda, Gregory and Moss, arXiv:1501.04937, READ:
     "small black holes can act as seeds for vacuum decay".  Cuspinera, Gregory, Marshall and Moss, arXiv:1803.02871
     (Randall-Sundrum brane black holes), READ: "small black hole seeds preferentially catalyse vacuum decay"; the action
     is "the difference in areas of the seed and remnant black hole horizon geometries"; "the instability scale should
     satisfy Λ_φ < M_5" (their consistency range, where the decay is computed).  Their 1907.11046, READ: without a black
     hole "the extra dimension has little impact" on the Higgs case; "black holes are required to produce significant
     decay rates".
  H3 (computed) The Higgs tie as numbers.  E5 = hbar c/l5, l5 = (l_P^2 ell)^(1/3), falls as ell^(-1/3).  The quartic's
     zero (p2_offset's run at m_H = 125.09, alpha_s = 0.1180) is 3.68e10 GeV at m_t = 172.57 GeV, 1.06e11 and 1.45e10
     at m_t -+ 0.29 GeV.  E5 = E_I at ell_H = 0.588 nm (0.024 to 9.6 nm within 1 sigma); with the reduced Planck length
     ell_H is 8 pi smaller (0.023 nm).  Beyond the zero the potential falls fast: V = lambda mu^4/4 is -8.7e39 GeV^4 at
     2 E_I and -2.8e47 at 100 E_I.
  H4 (computed; deduced) B5a on the plane's own Higgs.  B5a holds for matter with rho > -sigma/6 (b5a_residue A2); its
     pointwise proof holds inside our vacuum's basin (pointwise P8, item 339's note).  With ell below ell_H the
     instability lies inside the plane's matter theory (E_I < E5).  There the deepest potential within it, at E5, is
     below -sigma/6 for ell from 56.7 l_P up to ell_H: a plane whose Higgs left our basin there would break B5a, by up to
     2e14.  Below 56.7 l_P the tension is so large that -sigma/6 lies below the whole potential, and B5a alone
     says nothing.  So B5a alone does not give the bound.
  H5 (READ; deduced) The theorem's own corridors are the seeds.  Its corridors are black holes on our plane, from the one
     -bit hole at the five-dimensional Planck scale upward (clause (H)); H2's danger range -- small holes, of order 1 to
     1e6 M5 in Cuspinera et al.'s example -- lies inside that family.  With E_I < E5 such a hole seeds a bubble of the
     deeper vacuum, which changes our plane's offset dsigma -- one of the two numbers that define our universe (201) --
     by more than eighty orders.  A corridor that ends our universe is not the theorem's.  So the theorem requires
     E_I >= E5, ell >= ell_H: a bound from relativity (Euclidean gravity's tunnelling, its action an area difference)
     with the measured Standard Model, under 380 (nothing added between to save the vacuum).  It excludes item 380's
     reduced-Planck value (12.28 l_P, E5 = 5.3e18 GeV) and the integer kind's floor, and keeps 0.59 nm to 13.964 um.
     The tunnelling action for the theorem's own holes is not computed here; H2's is for tidal brane holes.
  H6 (READ; deduced) The equality.  H1's fixed point drives lambda to zero where gravity becomes strong.  On our plane
     gravity becomes five-dimensional and strong at E5, so k_tr = E5 and lambda(E5) ~ 0: the Higgs tie, sitting exactly
     on H5's bound -- the corridor-safe region's edge.  It rests on asymptotic safety with A_lambda > 0, a property of
     gravity's quantum running: gravity's own, as 326's alpha was, but not classical relativity.
  H7 (computed) What the equality fixes, given it: ell = 0.588 nm (0.024 to 9.6 nm within the top mass's 1 sigma, a
     further factor 25 with the convention for "Planck").  There N_L = 9.4e51 bits -- the Earth's README (372 K5,
     9.3e51): item 380's coincidence is this equality seen from the Earth.  The interior's Planck span is 1e68; the
     table-top correction at 52 um is 8.5e-11.
  H8 (deduced) The window's top, for the math (382 (1)).  Positivity sets none (381).  The theorem's domain sets the
     Planck curvature, 3.99 l_P (proved).  The plane's own Higgs with the theorem's own corridors sets ell >= ell_H
     (H5), far stronger; it becomes the top once H5's literature step is computed for the record's own holes.  The
     seated window and its dependents change once, when that is settled; until then the top is the Planck curvature.

Imports p2_gravity.py, p2_offset.py, ell_map.py and earth_cap.py by path.  Stdlib only.
python3 ell_higgs.py [--selftest | --mutants]
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
WORDS = ((382, "that is a question for the math"), (382, "agreed, continue"))
SW = ("For a positive gravity induced anomalous dimension A_λ > 0 the running of the quartic scalar self interaction λ "
      "at scales beyond the Planck mass is determined by a fixed point at zero", "λ(k_tr) ≈ 0, β_λ(k_tr) ≈ 0",
      "We expect this form to hold for a wide class of theories with an ultraviolet fixed point, where the high energy "
      "regime may involve additional fields or even higher dimensions",
      "The case A_λ > 0 is favored by explicit computations existing in the literature")   # 0912.0208, READ
BGM = ("small black holes can act as seeds for vacuum decay",)                            # 1501.04937, READ
CGMM = ("small black hole seeds preferentially catalyse vacuum decay",
        "the difference in areas of the seed and remnant black hole horizon geometries",
        "the instability scale should satisfy Λ_φ < M_5")                                 # 1803.02871, READ
CGMM19 = ("the extra dimension has little impact", "black holes are required to produce significant decay rates")
MT, MT_SIG, MH, A3 = 172.57, 0.29, 125.09, 0.1180
R_TEST = 52e-6
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
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "eh_pg")
    po = _load(os.path.join(HERE, "p2_offset.py"), "eh_po")
    em = _load(os.path.join(HERE, "ell_map.py"), "eh_em")
    ec = _load(os.path.join(HERE, "earth_cap.py"), "eh_ec")
    c, G, hb, LN2, ceil = pg.C, pg.G, pg.HBAR, pg.LN2, pg.ELL_MAX
    eV = 1.602176634e-19
    GEV4 = po.GEV4
    lP = math.sqrt(hb * G / c ** 3)
    lpx = math.sqrt(8 * math.pi) * lP if MUT.get("reduced_default") else lP
    E5 = lambda e: hb * c / (lpx ** 2 * e) ** (1 / 3) / eV / 1e9               # GeV
    ell_of_E = lambda E: (hb * c / (E * 1e9 * eV)) ** 3 / lpx ** 2
    sig = lambda e: 3 * c ** 4 / (4 * math.pi * G * e ** 2) + 2 * pg.DSIG       # J/m^3
    cross, paths = {}, {}
    for mt in (MT - MT_SIG, MT, MT + MT_SIG):
        y, path = po.run(MH, mt, A3)
        neg = [m for m, l in path if l < 0]
        cross[mt], paths[mt] = neg[0], path
    path = paths[MT]
    lam_at = lambda mu: min(path, key=lambda p: abs(math.log(p[0] / mu)))[1]
    EI = cross[MT]
    ellH = {mt: ell_of_E(E) for mt, E in cross.items()}
    ellH_red = ellH[MT] / (8 * math.pi)
    depth = {f: lam_at(EI * f) * (EI * f) ** 4 / 4 for f in (2, 100)}          # GeV^4

    # H4: where the deepest potential inside the plane's matter theory (at E5) lies below -sigma/6
    frac = 2.0 if MUT.get("bound_half") else 6.0
    def gap(e):                                                                # > 0: B5a broken by the deep region
        E = E5(e)
        if E <= EI:
            return -1.0
        V = lam_at(E) * E ** 4 / 4 * GEV4
        return -V - sig(e) / frac
    lo, hi = math.log(5 * lP), math.log(ellH[MT] * 0.999)
    assert gap(math.exp(lo)) < 0 < gap(math.exp(hi))
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if gap(math.exp(mid)) < 0 else (lo, mid)
    ell_low = math.exp(hi)
    over_at_H = (-lam_at(E5(ellH[MT] * 0.5)) * E5(ellH[MT] * 0.5) ** 4 / 4 * GEV4) / (sig(ellH[MT] * 0.5) / frac)
    over_max = max((-lam_at(E5(e)) * E5(e) ** 4 / 4 * GEV4) / (sig(e) / frac)
                   for e in (ellH[MT] * k for k in (0.9, 0.5, 0.1, 0.01)))
    red = math.sqrt(48 * math.pi) * lP
    M_E = ec.GM_EARTH / G
    A = ec.SNAPSHOT[0] * M_E / ec.SNAPSHOT[1]
    NL = math.pi ** 2 / (2 * LN2) * (ellH[MT] / lP) ** 2
    return dict(cross=cross, EI=EI, ellH=ellH, ellH_red=ellH_red, depth=depth, ell_low=ell_low / lP,
                over_at_H=over_at_H, over_max=over_max, red_E5=E5(red), red_excluded=E5(red) > EI,
                gkp_excluded=E5(22.3 * lP) > EI and E5(57.4 * lP) > EI, ceil_ok=E5(ceil) < EI,
                NL=NL, A=A, span=(ellH[MT] / lP) ** (8 / 3), corr=2 * ellH[MT] ** 2 / (3 * R_TEST ** 2),
                planck=40 ** (3 / 8), E5_slope=math.log(E5(2e-9) / E5(1e-9)) / math.log(2))


def report(o):
    print("ell_higgs.py -- the window's top and the object for lambda(E5) = 0 (item 382)\n")
    print("H3 quartic's zero %s GeV -> ell_H %s m; reduced %.3e m; E5 ~ ell^%.3f"
          % (" / ".join("%.3e" % v for v in o["cross"].values()), " / ".join("%.3e" % v for v in o["ellH"].values()),
             o["ellH_red"], o["E5_slope"]))
    print("H3 V beyond the zero: %.2e GeV^4 at 2 E_I, %.2e at 100 E_I" % (o["depth"][2], o["depth"][100]))
    print("H4 B5a broken by the deep region for ell from %.1f l_P to ell_H; excess %.1e at ell_H/2, up to %.1e"
          % (o["ell_low"], o["over_at_H"], o["over_max"]))
    print("H5 380's reduced-Planck value: E5 = %.2e GeV > E_I (excluded: %s); integer floor excluded: %s; ceiling "
          "safe: %s" % (o["red_E5"], o["red_excluded"], o["gkp_excluded"], o["ceil_ok"]))
    print("H7 at ell_H: N_L %.3e bits (the Earth's README %.3e); Planck span %.2e; table-top at 52 um %.2e"
          % (o["NL"], o["A"], o["span"], o["corr"]))
    print("H8 the domain's limit, the Planck curvature, at %.2f l_P" % o["planck"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    eh = o["ellH"]
    add("H0 382 verbatim in its item", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("H1-H2 the reads are carried (four from Shaposhnikov-Wetterich, one from Burda et al., five from Cuspinera et "
        "al.)", len(SW) == 4 and len(BGM) == 1 and len(CGMM) + len(CGMM19) == 5)
    add("H3 the zero at 3.68e10 GeV (1.06e11, 1.45e10 within 1 sigma); ell_H 0.588 nm (0.024-9.6 nm); reduced 0.023 "
        "nm; E5 falls as ell^(-1/3); V -8.7e39 at 2 E_I", "%.3g" % o["EI"] == "3.68e+10"
        and "%.3g" % eh[MT - MT_SIG] == "2.45e-11" and "%.3g" % eh[MT] == "5.88e-10" and "%.2g" % eh[MT + MT_SIG]
        == "9.6e-09" and "%.2g" % o["ellH_red"] == "2.3e-11" and abs(o["E5_slope"] + 1 / 3) < 1e-9
        and "%.2g" % o["depth"][2] == "-8.7e+39")
    add("H4 B5a is broken by the deep region only for ell from 56.7 l_P to ell_H (excess 1.8e14 at ell_H/2); below, "
        "-sigma/6 lies under the whole potential", "%.3g" % o["ell_low"] == "56.7"
        and "%.2g" % o["over_at_H"] == "1.8e+14" and o["over_max"] > 1e14)
    add("H5 the corridor-safe bound excludes 380's reduced-Planck value (E5 5.3e18 GeV) and the integer floor; the "
        "ceiling is safe", o["red_excluded"] and "%.2g" % o["red_E5"] == "5.3e+18" and o["gkp_excluded"]
        and o["ceil_ok"])
    add("H7 at ell_H: N_L 9.4e51 bits against the Earth's README 9.3e51; Planck span 1e68; table-top 8.5e-11",
        "%.2g" % o["NL"] == "9.4e+51" and "%.2g" % o["A"] == "9.3e+51" and "%.0e" % o["span"] == "1e+68"
        and "%.2g" % o["corr"] == "8.5e-11")
    add("H8 the domain's limit at 3.99 l_P", "%.3g" % o["planck"] == "3.99")
    return res


MUTANTS = {"reduced_default": "E5 taken with the reduced Planck length throughout (H3, H5, H7)",
           "bound_half": "B5a's matter bound read as -sigma/2, not -sigma/6 (H4)"}


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
