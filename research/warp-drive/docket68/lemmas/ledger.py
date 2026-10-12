#!/usr/bin/env python3
"""ledger.py -- Warp Theorem lemmas E3 and E4: the energy ledger closes, and the field energy outside the neck is placed.
CONFIRMED BY M (item 155): the board's reading (a) -- E's remainder absorbed as position 2's expansion, part of the
build -- is M's (H-EXPANSION-IS-BUILD).  E3 is derived from M's rulings.

  E4a the plane's energy outside the neck is computed: the Misner-Sharp mass of eq. (17) at r0 = 2m is
          M(R) = m + (m/4) (1 - m/(2R - 3m)),
      m at the throat, 5m/4 far away (the ADM total).  So the E/4 lies close in: two thirds within R = 3m, 98% within
      the hold's span (O3, ~30m).  It cannot be set aside as a far field a brief hold never forms
  E4b it is not the plane's energy.  The plane carries no matter (B1: R = 0, tau = 0, escape.py S3), so its Einstein
      tensor is the bulk's Weyl projection, G = -E (Maartens-Koyama eq. 143, READ in throatbulk.py): the E/4 is the
      bulk's gravitational field read on the plane -- the same kind of reading as Z1's, where the plane's null-energy
      deficit is the bulk's pull.  Its density is positive (dM/dR > 0 outside the neck).  So the plane's own ledger --
      the one exact energy E carried from the device into position 2 (items 104 (b), 110, 111, 133) -- is complete
      without it; where the bulk's field comes from belongs to the five-dimensional formation (B7)
  E3  the ledger closes under the board's reading (a) (WARPTHEOREM.md): the copy, exact (146) and made of reorganized
      matter (137, 148), absorbs at most the assembly energy; the remainder is absorbed as the expansion of position 2's
      universe (136 G, 136 answer 6, 139 (3)), counted as part of the build, which keeps 111 (a).  Computed at the
      example README and at item 108's full snapshot: E = E_copy + E_expansion with both terms non-negative and E_copy
      within the assembly ceiling (z3, exact rationals).  Control: with no expansion term the ledger is unsatisfiable.
      PROVED UNDER reading (a), which stays the board's and is withdrawn if M corrects it
  E3s (item 331; computed, z3 over exact rationals) the ledger at the family's small end.  The README's E there is the
      localized hole's, E = 3 pi c^4 r_h^2/(8 G5), r_h = (2 N ln2/pi^2)^(1/3) l5 (rows_small G1s, C2/C4 verified):
      1.28098e9 J at the example README, 1.11904e9 J and 1.61394e9 J under the bulk's G5 readings (3/2) G ell and G ell/2
      (E ~ g^(-1/3), c7_oneway V12 (Q2), verified) -- each below the 1.1947e10 J assembly ceiling.  So at the example
      the ledger closes with the expansion term and closes without it too: E3's control ("with no expansion term the
      ledger is unsatisfiable") flips there, the example behaving as T3's 600-bit control, as item 271's verifier
      deduced (rows_small G1s).  At the full snapshot (N = 1.088e29, still r_h << ell) E = 1.49e18 J, above the ceiling:
      the control holds there.  E3 itself -- E = E_copy + E_expansion, both non-negative, the copy within the ceiling --
      closes at both ends and both READMEs.  Item 239 (M-NEED-IS-ACTIVATION) set the ceiling aside as the build's need,
      so the flip moves T3's verdict for its own premise only, not the build: 239's setting-aside "softens this, it does
      not remove it" (rows_small G1s), and the large end's figures stand as computed above.
Imports copy/exactE.py and lemmas/p2_gravity.py by path.  Stdlib + sympy + z3.
python3 ledger.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972
SNAPSHOT_N = 1.088e29                 # item 108's full atomic snapshot
ASSEMBLY_MAX_J = 1.1947e10            # LOOSE.md L1, H-BOND-CEILING
C = 299792458
MUT = {}
G5_READINGS = (1, 1.5, 0.5)            # g = G5/(G ell): the bulk's readings (items 310, 319 (Q2))


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def e4():
    r, m, R = sp.symbols("r m R", positive=True)
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    M = sp.simplify(r / 2 * (1 - H))
    closed = m + m / 4 * (1 - m / (2 * r - 3 * m))
    frac = lambda Rv: float(((M - m) / (m / 4)).subs({m: 1, r: Rv}))
    dM = sp.simplify(sp.diff(M, r))
    return {"M": M, "closed_ok": sp.simplify(M - closed) == 0, "at_throat": sp.simplify(M.subs(r, 2 * m)),
            "far": sp.limit(M, r, sp.oo), "f3": frac(3), "f30": frac(30.48), "dM": dM,
            "dM_pos": all(float(dM.subs({m: 1, r: x})) > 0 for x in (2.01, 2.5, 3, 10, 1e3))}


def e3(E_per_sqrt_bit):
    import z3

    def ledger(E_value, with_expansion):
        E, cp, ex = z3.Reals("E copy expansion")
        s = z3.Solver()
        s.add(E == E_value, cp >= 0, cp <= z3.RealVal(str(Fraction(ASSEMBLY_MAX_J))), E == cp + ex)
        s.add(ex >= 0 if with_expansion else ex == 0)
        ok = s.check() == z3.sat
        return ok, (float(s.model()[ex].as_fraction()) if ok and with_expansion else None)
    out = {}
    for name, N in (("example", EXAMPLE_N), ("snapshot", SNAPSHOT_N)):
        Ev = E_per_sqrt_bit * math.sqrt(N)
        Ez = z3.RealVal(str(Fraction(Ev)))
        out[name] = {"N": N, "E": Ev, "E_over_c2_kg": Ev / C**2, "closes": ledger(Ez, True)[0],
                     "no_expansion": ledger(Ez, False)[0], "expansion_least": Ev - ASSEMBLY_MAX_J}
    return out


def e_small(N, g=1.0):
    """E3s: the small end's E for N bits, G5 = g G ell (rows_small G1s)"""
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "lg_pg")
    G5 = g * PG.G * PG.ELL_MAX
    l5 = (PG.HBAR * G5 / PG.C ** 3) ** (1 / 3)
    rh = (2 * N * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    if MUT.get("record_E"):
        return None, rh, PG.ELL_MAX                                   # the mutant: the record's 4D E kept at the small end
    return 3 * math.pi * PG.C ** 4 * rh ** 2 / (8 * G5), rh, PG.ELL_MAX


def e3s(E_per_sqrt_bit):
    """E3s (item 331): the ledger at the small end, both READMEs, the three G5 readings"""
    import z3

    def ledger(E_value, with_expansion):
        E, cp, ex = z3.Reals("E copy expansion")
        s = z3.Solver()
        s.add(E == z3.RealVal(str(Fraction(E_value))), cp >= 0, cp <= z3.RealVal(str(Fraction(ASSEMBLY_MAX_J))),
              E == cp + ex)
        s.add(ex >= 0 if with_expansion else ex == 0)
        return s.check() == z3.sat
    out = {}
    for name, N in (("example", EXAMPLE_N), ("snapshot", SNAPSHOT_N)):
        for g in G5_READINGS:
            Ev, rh, ell = e_small(N, g)
            if Ev is None:
                Ev = E_per_sqrt_bit * math.sqrt(N)
            out[(name, g)] = {"E": Ev, "rh_over_ell": rh / ell, "closes": ledger(Ev, True),
                              "no_expansion": ledger(Ev, False), "below": Ev < ASSEMBLY_MAX_J}
    return out


def compute():
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "lg_exactE")
    return {"e4": e4(), "e3": e3(ex.e_per_sqrt_bit()), "e3s": e3s(ex.e_per_sqrt_bit())}


def report(d):
    a, b = d["e4"], d["e3"]
    print("ledger.py -- Warp Theorem lemmas E3, E4\n")
    print("E4a Misner-Sharp M(R) = m + (m/4)(1 - m/(2R - 3m)): %s; m at the throat (%s), %s far away; share of the E/4 "
          "within 3m %.3f, within the hold's span %.3f" % (a["closed_ok"], a["at_throat"], a["far"], a["f3"], a["f30"]))
    print("E4b dM/dR = %s > 0 outside the neck: %s -- the bulk's Weyl field read on the plane (G = -E, MK 143)"
          % (a["dM"], a["dM_pos"]))
    for k, v in b.items():
        print("E3  %s README (N = %.4g): E = %.6e J (E/c^2 = %.4g kg); closes with the expansion: %s, least expansion "
              "%.6e J; with none: %s" % (k, v["N"], v["E"], v["E_over_c2_kg"], v["closes"], v["expansion_least"],
                                        v["no_expansion"]))
    for (k, g), v in d["e3s"].items():
        print("E3s (item 331) small end, %s README, G5 = %.1f G ell: E = %.5e J (r_h/ell = %.3g); below the ceiling: %s; "
              "closes with the expansion: %s; with none: %s" % (k, g, v["E"], v["rh_over_ell"], v["below"], v["closes"],
                                                                v["no_expansion"]))


def checks(d):
    out = []

    def chk(name, cond):
        out.append((name, bool(cond)))

    a, b = d["e4"], d["e3"]
    m = sp.Symbol("m", positive=True)
    chk("E4a: M(R) = m + (m/4)(1 - m/(2R - 3m)) exactly; m at the throat, 5m/4 far away",
        a["closed_ok"] and sp.simplify(a["at_throat"] - m) == 0 and sp.simplify(a["far"] - 5 * m / 4) == 0)
    chk("E4a: two thirds of the E/4 lies within 3m, 98% within the hold's span", abs(a["f3"] - 2 / 3) < 1e-9
        and a["f30"] > 0.98)
    chk("E4b: its density is positive outside the neck", a["dM_pos"])
    chk("E3: the ledger closes with the expansion term, at the example README and at the full snapshot",
        b["example"]["closes"] and b["snapshot"]["closes"])
    chk("E3 control: with no expansion term it cannot close at either", not b["example"]["no_expansion"]
        and not b["snapshot"]["no_expansion"])
    s = d["e3s"]
    ex = [s[("example", g)] for g in G5_READINGS]
    chk("E3s (item 331): at the small end the example README's E is 1.28098e9 J (1.11904e9, 1.61394e9 under G5 = 3/2, 1/2 "
        "G ell), below the 1.1947e10 J ceiling: the ledger closes with and without the expansion term -- E3's control "
        "flips there, as T3's 600-bit control",
        ["%.5e" % v["E"] for v in ex] == ["1.28098e+09", "1.11904e+09", "1.61394e+09"]
        and all(v["below"] and v["closes"] and v["no_expansion"] for v in ex) and all(v["rh_over_ell"] < 0.1 for v in ex))
    sn = [s[("snapshot", g)] for g in G5_READINGS]
    chk("E3s: at the full snapshot (N = 1.088e29, r_h << ell) E ~ 1.5e18 J is above the ceiling: closes only with the "
        "expansion term; E3 closes at every README, end and reading",
        all(v["closes"] and not v["no_expansion"] and v["rh_over_ell"] < 0.1 for v in sn)
        and "%.2g" % s[("snapshot", 1)]["E"] == "1.5e+18")
    return out


MUTANTS = {"record_E": "the record's four-dimensional E kept at the small end (E3s; item 271 (8))"}


def selftest():
    r_ = checks(compute())
    for name, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = sorted({nm.split(":")[0].split()[0] for nm, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-72s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)




if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
