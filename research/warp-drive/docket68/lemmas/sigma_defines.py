#!/usr/bin/env python3
"""sigma_defines.py -- is our plane's tension a definition of our universe?  (M, after sigma_cypher.py: "Test it".)
Computed, deduced, STRUCTURAL; the cypher CLASSIFIES; not verified by a separate session; not seated; 2026-10-10.

The reading tested (the board's, from M's words): H-SIGMA-DEFINES-UNIVERSE -- each universe is a closed index (M: "Each
universe/spacetime is a repository/closed index"), with its own laws (138) and its own G from its own plane (187 (2));
our plane's tension sigma is part of what defines ours, not a lemma to derive -- a DEFINITION in the sense axioms.py
gives R0-R2 ("they say what the theory's words mean; a definition is not derived"), which must be shown consistent with
the rest.

  T1 (imported) no lemma derives sigma: every chain clause is free of ell (b6_k.py B6b), and on the index of what the
     theory fixes sigma is an axis nothing determines (sigma_cypher.py C1).  A definition cannot contradict a derived
     value; there is none
  T2 (computed) it meets every constraint: the window [1.48e53, 2.75e112] J/m^3 is not empty (sigma_cypher W1);
     sigma > 0 gives G > 0 (SMS p.3, READ); 139 (1) and 200 (1) then give position 2's plane -sigma/4 and k_R = k_L/2
  T3 (computed; cypher) it individuates the gravitational sector: with one coupling (H-ONE-G5), G = kappa5^4 sigma/(48 pi)
     (SMS 19), ell^2 = 3c^4/(4 pi G sigma), k_R/k_L = 1/2, sigma2 = -sigma/4 are functions of sigma.  On an index of
     universes, information reports all of them as adding nothing beside sigma -- sigma is the one axis of that sector.
     Control: a universe property free of sigma breaks it (it adds something)
  T4 (computed) dark energy needs a second number.  With sigma alone and Randall-Sundrum's tuning, SMS (18) gives
     Lambda4 = 0 identically.  Our Lambda4 is observed (Planck, via cosmo.py: rho_Lambda = 5.84e-27 kg/m^3), so either
     (a) the definition is the pair (sigma, delta sigma) with delta sigma = rho_Lambda c^2 = 5.25e-10 J/m^3 -- at most
     3.5e-63 of sigma -- or (b) sigma alone, with Lambda4 = 0 and dark energy a field on the plane with w > -1 strictly
     (Z3c allows it): a prediction that w is not exactly -1.  On the universe index with Lambda4 included, information
     reports Lambda4 as adding something: sigma alone does not individuate the universe once dark energy is counted
  T5 (deduced, STRUCTURAL; flagged, not decided) with sigma a universe's key, 139 (1)'s quarter ties a destination's key
     to its origin's: a corridor from ours reaches a plane of tension -sigma/4.  Between universes that is consistent.
     Within one universe position 2 is on our own plane, tension sigma, which 139 (1)'s negative quarter reads against:
     on this reading the quarter belongs to the between-universes class
So: CONSISTENT as a definition of our plane's tension and of the gravitational sector it fixes (T1-T3); NOT SUFFICIENT
alone to define our universe once its dark energy is counted (T4: a second number, or the prediction w != -1).
Imports b6_k.py and sigma_cypher.py (and tools/cypher.py) by path.  Stdlib + sympy.  python3 sigma_defines.py
[--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def t1_t2():
    b6 = _load(os.path.join(HERE, "b6_k.py"), "sd_b6k").compute()
    sc = _load(os.path.join(HERE, "sigma_cypher.py"), "sd_sigma")
    d = sc.compute()
    return {"free": b6["n_kk_free"] and b6["closed_forms_free"], "axis": not d["fixed_main"], "window": d["w"]}


def t4_symbolic():
    k5, s, ell = sp.symbols("kappa5 sigma ell", positive=True)
    L5 = -6 / (k5**2 * ell**2)                                   # AdS bulk: kappa5^2 Lambda = -6/ell^2 (SMS normalization)
    L4 = k5**2 / 2 * (L5 + k5**2 * s**2 / 6)                     # SMS (18), READ
    tuned = sp.simplify(L4.subs(s, 6 / (k5**2 * ell)))           # RS: sigma = 6/(kappa5^2 ell)
    if MUT.get("untuned"):
        tuned = sp.simplify(L4.subs(s, 7 / (k5**2 * ell)))
    c, G = 299792458.0, 6.67430e-11
    rho_L = 5.84e-27                                             # kg/m^3, Planck via cosmo.py (B1-MATTER / F1-AUDIT)
    dsig = rho_L * c**2                                          # Lambda4 c^4/(8 pi G) = rho_L c^2
    return {"tuned": tuned, "dsig": dsig, "frac": dsig / 1.482e53}


def universe_index(cy, with_L4=False, sigma_free_prop=False):
    """cells = universes keyed by sigma (one kappa5): G ~ sigma, ell ~ sigma^-1, k_R/k_L = 1/2, sigma2 = -sigma/4 (binned),
    plus non-injective properties so a key is not the register-1356 artefact: tension sign (+) and the classical-bulk flag."""
    cells = []
    for s in range(1, 7):
        for L4 in ((1, 2, 3) if with_L4 else ((0, 1) if sigma_free_prop else (0,))):
            G = s
            ell = 7 - s
            row = [s, G, ell, 1, -s, 1, 1 if s < 6 else 0]       # sigma, G, ell, kR/kL, sigma2, sign, classical
            if with_L4:
                row.append(L4)
            if sigma_free_prop:
                row.append(L4)                                   # two universes share sigma and differ in this property
            cells.append(row)
    coords = ["sigma", "G", "ell", "kR_kL", "sigma2", "sign", "classical"] + (["Lambda4"] if with_L4 else []) + \
             (["free_prop"] if sigma_free_prop else [])
    return cy.Index("universes", coords, cells)


def t3_t4_cypher():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "sd_cypher")

    def report(ix):
        rows, keys = cy.coordinate_report(ix)
        return {r["coordinate"]: r["adds_nothing"] for r in rows}, keys
    grav, gkeys = report(universe_index(cy))
    withL4, lkeys = report(universe_index(cy, with_L4=True))
    ctrl, _ = report(universe_index(cy, sigma_free_prop=True))
    return {"grav": grav, "gkeys": gkeys, "withL4": withL4, "lkeys": lkeys, "ctrl": ctrl}


def compute():
    return {"t12": t1_t2(), "t4": t4_symbolic(), "cy": t3_t4_cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    t = d["t12"]
    add("T1 no lemma derives sigma (chain clauses free of ell; sigma an axis on the theory's index)", t["free"] and t["axis"])
    w = t["window"]
    add("T2 the window is not empty and sigma > 0 there (G > 0, SMS)", 0 < w["smin"] < w["smax"])
    g = d["cy"]["grav"]
    add("T3 on the universe index G, ell, k_R/k_L, sigma2, sign, classical add nothing beside sigma; sigma is the one "
        "axis of the gravitational sector", all(g[c] for c in ("G", "ell", "kR_kL", "sigma2", "sign", "classical")))
    add("T3 control: a universe property free of sigma adds something", not d["cy"]["ctrl"]["free_prop"])
    t4 = d["t4"]
    add("T4 RS tuning gives Lambda4 = 0 identically (SMS 18); our observed dark energy needs delta sigma = rho_L c^2 = "
        "5.25e-10 J/m^3 (<= 3.5e-63 of sigma) or a field with w > -1", t4["tuned"] == 0
        and 5.2e-10 < t4["dsig"] < 5.3e-10 and t4["frac"] < 4e-63)
    add("T4 cypher: with Lambda4 counted, Lambda4 adds something on the universe index (sigma alone does not individuate "
        "the universe); sigma no longer a key", not d["cy"]["withL4"]["Lambda4"] and "sigma" not in d["cy"]["lkeys"])
    return res


MUTANTS = {"untuned": "the RS tuning broken (sigma = 7/(kappa5^2 ell))"}


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
        failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-10s %-46s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("sigma_defines.py -- is our plane's tension a definition of our universe?\n")
    print("T1 free of ell / sigma an axis:", d["t12"]["free"], d["t12"]["axis"])
    print("T3 gravitational sector, adds nothing beside sigma:", d["cy"]["grav"], " keys:", d["cy"]["gkeys"])
    print("T4 Lambda4 under RS tuning:", d["t4"]["tuned"], "; delta sigma = %.3e J/m^3 (%.2e of sigma_min)" % (d["t4"]["dsig"], d["t4"]["frac"]))
    print("T4 with Lambda4 counted:", d["cy"]["withL4"], " keys:", d["cy"]["lkeys"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
