#!/usr/bin/env python3
"""ell_si.py -- item 542: which ell the statement's SI figures use, and the figures at each of the record's readings.
M, 542, to "The SI figures in the statement use ell = 13.964 um without saying which of the three readings that is":
"address and correct this".  Labels: computed (exact unless marked numerical), READ, deduced, M's.

  L0 (read) M's words, verbatim in the rulings file, 542.
  L1 (computed, exact) What carries ell.  At the small end r_h = (2 N ln2/pi^2)^(1/3) l5 with l5^3 = l_P^2 ell, and
     E = 3 pi c^4 r_h^2/(8 G5) with G5 = G ell, so r_h is proportional to ell^(1/3) and E to ell^(-1/3); r_h/l5 and the
     clocks of r_h/c (the life, the write, the release) carry N alone.  At the large end E = (N h c^5 ln2/(8 pi^2
     G))^(1/2) and r0 = 2GE/c^4 carry no ell.  So among the statement's SI figures only the small end's r_h, E and
     r_h/ell depend on the reading.
  L2 (computed) The example README (N = 2,742,570,311,524,972) at each reading the record holds (qb_baez B2):
     - (F) the measured window's top, 13.964 um: r_h 1.12008e-20 m, E 1.28098e9 J, r_h/ell 8.0e-16 -- the statement's
       figures;
     - (D) the dark-energy tie, ell_D = lam_C (hbar c/rho_L c^2)^(1/4) = 7.43 um: r_h 9.08e-21 m, E 1.58e9 J,
       r_h/ell 1.2e-15;
     - (H) the Higgs tie, E5 = hbar c/l5 at the running quartic's zero, ell_H = 0.611 nm: r_h 3.95e-22 m, E 3.63e10 J,
       r_h/ell 6.5e-13.
     The example stays at the small end at every reading (r_h/ell <= 6.5e-13).
  L3 (deduced) What the statement's figures are, and what is correct.  13.964 um is the window's top: the largest ell
     observation allows (Adelberger et al.'s bound through the one-plane law, b6p_scale S4, READ there).  ell is not yet
     fixed (380: not free), M chose to fix it by an equality from relativity through the Higgs tie (381), and 384
     withdrew asymptotic safety as that equality's object, leaving ell >= ell_H standing as a bound (ell_higgs;
     WARPTHEOREM items 382-384).  So the statement gave one end of the window as if it were the value.  Corrected:
     the small end's figures at both ends of the window, ell_H <= ell <= 13.964 um, with the dark-energy tie inside it,
     and the scalings.
  L4 (computed, exact) The computed domain N >= 7.12e9 is r_h >= 1000 l5, ell's free; the large end's start N_L, where
     r0 reaches ell, is not: pi (ell/l_P)^2/ln2, 6.49e51 at ell_H and 3.38e60 at the window's top.

Imports qb_baez.py (the readings, and through it p2_offset's run) by path.
python3 ell_si.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, math, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "The SI figures in the statement use"), (542, "address and correct this"))
N_EX = 2742570311524972                         # the example README (the identity core)
G, C, HBAR = 6.67430e-11, 299792458.0, 1.054571817e-34
H_PL = 2 * math.pi * HBAR
L_P = math.sqrt(HBAR * G / C ** 3)              # the theorem's l_P, no 8 pi (384)
_MOD = {}


def _load(name, alias):
    if alias not in _MOD:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        _MOD[alias] = mod
    return _MOD[alias]


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def scalings():
    """L1: the exponents of ell in the small end's r_h and E, and the large end's freedom from it"""
    ell, lp, n, g, c, h = sp.symbols("ell l_P N G c h", positive=True)
    l5 = (lp ** 2 * ell) ** sp.Rational(1, 3)
    p = 1 if MUT.get("cube") else sp.Rational(1, 3)
    rh = (2 * n * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3) * (l5 if p == sp.Rational(1, 3) else l5 ** 3 / lp ** 2)
    e = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * g * ell)
    er = sp.simplify(ell * sp.diff(rh, ell) / rh)
    ee = sp.simplify(ell * sp.diff(e, ell) / e)
    el = sp.sqrt(n * h * c ** 5 * sp.log(2) / (8 * sp.pi ** 2 * g))
    return dict(r_exp=er, e_exp=ee, large_free=sp.diff(el, ell) == 0, rh_l5_free=sp.simplify(sp.diff(rh / l5, ell)) == 0)


def small(ell, n=N_EX):
    l5 = (L_P ** 2 * ell) ** (1 / 3)
    if MUT.get("reduced"):
        l5 *= math.sqrt(8 * math.pi)
    rh = (2 * n * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    e = 3 * math.pi * C ** 4 * rh ** 2 / (8 * G * ell)
    return dict(ell=ell, l5=l5, rh=rh, E=e, ratio=rh / ell)


def readings():
    QZ = _load("qb_baez.py", "elsi_qz")
    ei = QZ.e_i(QZ.OURS["mh"], QZ.OURS["mt"], QZ.OURS["a3"])
    return {"F": QZ.ELL_TOP, "D": QZ.ell_d(), "H": QZ.ell_h(ei)}, ei


def compute():
    r, ei = readings()
    return dict(words=words(), sc=scalings(), ells=r, E_I=ei, at={k: small(v) for k, v in r.items()},
                domain=(2 * 7.12e9 * math.log(2) / math.pi ** 2) ** (1 / 3),
                NL={k: math.pi * (v / L_P) ** 2 / math.log(2) for k, v in r.items()})


def checks(o):
    sc, a = o["sc"], o["at"]
    out = {}
    out["L0"] = o["words"]
    out["L1"] = (sc["r_exp"] == sp.Rational(1, 3) and sc["e_exp"] == -sp.Rational(1, 3) and sc["large_free"]
                 and sc["rh_l5_free"])
    out["L2"] = ("%.5e" % a["F"]["rh"] == "1.12008e-20" and "%.5e" % a["F"]["E"] == "1.28098e+09"
                 and "%.1e" % a["F"]["ratio"] == "8.0e-16" and "%.3g" % (o["ells"]["H"] * 1e9) == "0.611"
                 and "%.3g" % (o["ells"]["D"] * 1e6) == "7.43" and all(x["ratio"] < 1e-12 for x in a.values()))
    out["L3"] = o["ells"]["H"] < o["ells"]["D"] < o["ells"]["F"]
    out["L4"] = abs(o["domain"] - 1000) < 1 and "%.3g" % o["NL"]["F"] == "3.38e+60" \
        and "%.3g" % o["NL"]["H"] == "6.49e+51"
    return out


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("L0 M's words:", o["words"])
    print("L1 small end: r_h ~ ell^(%s), E ~ ell^(%s); r_h/l5 free of ell: %s; large end free of ell: %s"
          % (o["sc"]["r_exp"], o["sc"]["e_exp"], o["sc"]["rh_l5_free"], o["sc"]["large_free"]))
    names = {"F": "the window's top", "D": "the dark-energy tie", "H": "the Higgs tie (E_I %.4g GeV)" % o["E_I"]}
    for k in ("F", "D", "H"):
        x = o["at"][k]
        print("L2 %-34s ell %.4g m: l5 %.4g m, r_h %.5e m, E %.5e J, r_h/ell %.2g"
              % (names[k], x["ell"], x["l5"], x["rh"], x["E"], x["ratio"]))
    print("L3 ell_H < ell_D < the window's top: %s -- the statement's figures are the window's top" % ck["L3"])
    print("L4 the computed domain N >= 7.12e9 is r_h >= %.1f l5; N_L = %s" % (
        o["domain"], ", ".join("%s %.3g" % (k, v) for k, v in o["NL"].items())))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return ck


def selftest(quiet=False):
    with contextlib.redirect_stdout(io.StringIO()) if quiet else contextlib.nullcontext():
        ck = report()
    ok = all(ck.values())
    if not quiet:
        print("selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


MUTANTS = {"cube": "r_h taken proportional to ell, not ell^(1/3) (L1)",
           "reduced": "the reduced Planck length, 8 pi in l5 (L2)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-8s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
