#!/usr/bin/env python3
"""fuelform.py -- is there a material other than salt, and what does it cost?

WHY THIS FILE EXISTS
--------------------
materials.py says the blanket's chemistry is FORCED rather than chosen, in a
chain of three links:

    1. nu = 2.9 is Pu-239 FAST, so there is no thermal spectrum
    2. L = 0.20 must cover fission products for forty years, so the fuel
       must be LIQUID
    3. a liquid fast fuel is a SALT, and a fast salt is a CHLORIDE

deck.py --provenance then found that the chloride is the one material in the
design with no critical benchmark behind it: the first fast-chloride
criticality experiment is being built and has not run, the Cl-35 evaluated
data are known to disagree with measurement OUTSIDE their own covariance, and
this project's one-group model has never been checked on it.

So the question is whether the chain is as forced as it says. THIS FILE TESTS
EACH LINK, and two of the three turn out to be weaker than stated.

THE RESULT THAT MATTERS, AND IT WAS NOT EXPECTED
------------------------------------------------
The always-subcritical property -- criticality.py's central claim, the reason
k = 0.900 was adopted, the reason the hazard class "stops existing rather
than being managed" -- IS NOT BOUGHT BY THE SALT.

k_inf is a RATIO of macroscopic cross sections, and every one of them scales
with density, so DENSITY CANCELS. A dense fuel and a dilute one at the same
fissile fraction and the same absorber-per-heavy-atom have the same k_inf.
What sets the threshold is the fissile fraction and what the carrier absorbs,
and across every candidate fuel form the crossing sits in a band 1.35 wide.

    python3 tools/fuelform.py
    python3 tools/fuelform.py --selftest
stdlib only.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fuelchoice as F                                          # noqa: E402
import materials as M                                           # noqa: E402

# ---- carrier cross sections, one-group fast, barns -------------------------
# The same discipline as fuelchoice.XS, which these join: each is a SOURCED
# band with the mid used, and the selftest asserts the ORDERING they imply
# rather than the values, because the ordering survives a better spectrum and
# the values do not.
CARRIERS = {
    "O": (0.0, 0.0002, 0.0),    # oxygen is nearly transparent in a fast
                                # spectrum, which is why oxide fuel needs the
                                # least fissile of any form here
    "N14": (0.0, 0.030, 0.0),   # the (n,p) is large -- which is exactly why
                                # nitride fuel programmes discuss N-15
                                # enrichment, and it is the same argument
                                # this design makes for Cl-37
    "Zr": (0.0, 0.020, 0.0),    # the IFR metal fuel's alloying addition
    "Pb": (0.0, 0.005, 0.0),
    "Bi": (0.0, 0.010, 0.0),    # and its (n,gamma) makes Po-210, which is
                                # LBE's own worst problem and not a
                                # neutronic one
    "Fe": (0.0, 0.010, 0.0),
}

# ---- the candidate fuel forms ----------------------------------------------
# (carriers per heavy-metal atom, state, fission-product removal, operating
#  history, criticality benchmarks)
Form = "name carriers state removal history benchmarks".split()


def forms():
    x = F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    r = F.atom_ratios(x)
    eu = F.atom_ratios(F.EUTECTIC_MOL_UCL3)
    return (
        ("NaCl-UCl3, the design's 18.9 mol %",
         {"Cl": r["Cl"], "Na": r["Na"]}, "liquid", "online, continuous",
         "NONE -- no fast chloride salt has ever gone critical",
         "NONE -- MCRE is being built to make the first"),
        ("NaCl-UCl3 at the eutectic, 34 mol %",
         {"Cl": eu["Cl"], "Na": eu["Na"]}, "liquid", "online, continuous",
         "NONE", "NONE -- this is MCRE's own salt"),
        ("LiF-ThF4-UF4 fluoride salt",
         {"F": 7.444, "Li7": 3.444}, "liquid", "online, continuous",
         "MSRE, thermal, 1965-69", "MSFR two-code benchmark, thermal-adjacent"),
        ("MOX oxide, bare fuel",
         {"O": 2.0}, "solid", "batch, aqueous or pyro",
         "Phenix, Superphenix, BN-600, BN-800, Joyo, FFTF -- decades",
         "abundant"),
        ("MOX in lead-bismuth, 50 vol % coolant",
         {"O": 2.0, "Pb": 2.6, "Bi": 1.4}, "solid", "batch",
         "the ADS field's own choice: MYRRHA and CiADS",
         "abundant, plus LBE-specific work"),
        ("U-Pu-Zr metal, the IFR fuel",
         {"Zr": 0.30}, "solid", "batch pyroprocessing, DEMONSTRATED",
         "EBR-II, thirty years, with its fuel cycle closed on site",
         "abundant"),
        ("mononitride fuel",
         {"N14": 1.0}, "solid", "batch",
         "test irradiations only", "some"),
        ("molten plutonium metal, Pu-Fe eutectic",
         {"Fe": 1.0}, "liquid", "liquid, but never demonstrated",
         "LAMPRE, Los Alamos, critical 1961, several thousand hours",
         "little"),
    )


def _xs():
    """fuelchoice's table, extended with the carriers this file adds.

    Extended rather than copied: an instrument imports a seated table, it
    never restates one."""
    x = dict(F.XS)
    x.update(CARRIERS)
    return x


def crossing(carriers, fissile="Pu239", fertile="U238"):
    """The fissile fraction at which k_inf = 1 for this form."""
    saved = dict(F.XS)
    F.XS.update(CARRIERS)
    try:
        lo, hi = 0.0, 0.95
        if F.k_infinity(hi, fissile, fertile, carriers=carriers) < 1.0:
            raise ValueError("no fissile fraction reaches k_inf = 1 here")
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if F.k_infinity(mid, fissile, fertile, carriers=carriers) < 1.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    finally:
        F.XS.clear()
        F.XS.update(saved)


def crossing_band():
    vals = [crossing(c) for _n, c, _s, _r, _h, _b in forms()]
    return min(vals), max(vals)


def salt_is_special():
    """Does the chloride salt buy a threshold the other forms cannot reach?

    Returns the design salt's crossing divided by the best other form's. If
    it is not comfortably below one, the salt is not what buys the property.
    """
    rows = forms()
    salt = crossing(rows[0][1])
    others = [crossing(c) for n, c, _s, _r, _h, _b in rows
              if "NaCl" not in n]
    return salt / min(others)


def report():
    lo, hi = crossing_band()
    print()
    print("  IS THERE A MATERIAL OTHER THAN SALT?")
    print()
    print("    materials.py says the chemistry is FORCED rather than chosen,")
    print("    in three links: the spectrum must be fast, so the fuel must be")
    print("    liquid to remove fission products for forty years, so it must")
    print("    be a salt, and a fast salt is a chloride. deck.py --provenance")
    print("    then found the chloride is the one material in the design with")
    print("    NO CRITICAL BENCHMARK BEHIND IT. So the chain is worth")
    print("    testing, and two of its three links are weaker than stated.")
    print()
    print("    LINK 3 FIRST, BECAUSE IT IS THE ONE THAT BREAKS.")
    print()
    print("    The always-subcritical property -- criticality.py's central")
    print("    claim and the reason k = 0.900 was adopted -- IS NOT BOUGHT BY")
    print("    THE SALT. k_inf is a RATIO of macroscopic cross sections and")
    print("    every one of them scales with density, SO DENSITY CANCELS. A")
    print("    dense fuel and a dilute one at the same fissile fraction and")
    print("    the same absorber per heavy atom have the same k_inf. What")
    print("    sets the threshold is the fissile fraction and what the")
    print("    carrier absorbs, and nothing else.")
    print()
    print("      fuel form                                k_inf = 1 at")
    for name, car, _st, _rem, _hist, _bench in sorted(
            forms(), key=lambda t: crossing(t[1])):
        mark = "   <- the design" if "18.9" in name else ""
        print(f"      {name:<42} {100 * crossing(car):5.2f} %{mark}")
    print()
    print(f"    THE WHOLE BAND IS {100 * lo:.2f} TO {100 * hi:.2f} PERCENT --"
          f" A SPREAD OF {hi / lo:.2f}.")
    print("    Every fast fuel form has an always-subcritical threshold, and")
    print("    they are all in the same place. The salt is not special, and")
    print(f"    the design's own salt is the SECOND WORST of them: it")
    print(f"    crosses at {100 * crossing(forms()[0][1]):.2f} % against"
          f" {100 * lo:.2f} % for bare oxide and"
          f" {100 * crossing(forms()[4][1]):.2f} % for")
    print(f"    MOX in lead-bismuth, so it needs {salt_is_special():.2f} times"
          " MORE fissile than")
    print("    the best form for the same property.")
    print()
    print("    LINK 2, WHICH IS WEAKER THAN IT LOOKS. 'The fuel must be")
    print("    liquid' is really 'fission products must come out', and a")
    print("    liquid is one way to do that. It is not the only demonstrated")
    print("    one:")
    print()
    print("      form                                       fission-product"
          " removal")
    for name, _c, _st, rem, _h, _b in forms():
        print(f"      {name:<42} {rem}")
    print()
    print("    EBR-II CLOSED ITS OWN FUEL CYCLE ON SITE FOR THIRTY YEARS with")
    print("    solid metal fuel and batch pyroprocessing. Batch is not online")
    print("    and the difference is real -- an online loop holds a lower")
    print("    equilibrium fission-product inventory -- but 'the fuel must be")
    print("    liquid' overstates it, and this work has never priced the")
    print("    difference.")
    print()
    print("    LINK 1 STANDS. Nothing here challenges the fast spectrum:")
    print("    nu = 2.9 is Pu-239 fast, materials.py derives it, and every")
    print("    form in the table above is a fast form.")
    print()
    print("    AND NOW THE COLUMN THAT DECIDES IT, WHICH IS THE ONE THIS")
    print("    PROJECT KEEPS LEARNING TO PUT FIRST.")
    print()
    print("      form                                       operating"
          " history")
    for name, _c, _st, _r, hist, _b in forms():
        print(f"      {name:<42} {hist}")
    print()
    print("      form                                       criticality"
          " benchmarks")
    for name, _c, _st, _r, _h, bench in forms():
        print(f"      {name:<42} {bench}")
    print()
    print("    THE DESIGN'S OWN MATERIAL IS THE ONLY ROW WITH 'NONE' IN BOTH")
    print("    COLUMNS, and the ADS field -- MYRRHA and CiADS, the two")
    print("    accelerator-driven systems actually being built -- chose MOX")
    print("    in lead-bismuth, which has decades of operating fast reactors")
    print("    and abundant benchmarks behind it AND a lower threshold.")
    print()
    print("    SO WHAT DOES THE SALT UNIQUELY BUY? ONE THING: ONLINE fission-")
    print("    product removal, which is link 2 and is real. What it uniquely")
    print("    costs is PROVENANCE -- no benchmark, no operating history, and")
    print("    a chlorine evaluation known to disagree with measurement")
    print("    outside its own covariance.")
    print()
    print("    AND deck.py --provenance SAYS THE SALT MAY NOT DELIVER THE")
    print("    SAFETY PROPERTY AT ITS OPERATING FRACTION ANYWAY. If that flag")
    print("    holds, the design is paying its entire provenance budget for a")
    print("    property it does not get, and the same property is available")
    print("    at a lower fissile fraction in a material with sixty years of")
    print("    operating history.")
    print()
    print("    THIS FILE DOES NOT TAKE THE DECISION. It is a change of")
    print("    material, it costs the online removal loop, and what that loop")
    print("    is worth in equilibrium fission-product inventory has never")
    print("    been computed here. WHAT IT DOES IS REMOVE THE WORD 'FORCED'")
    print("    FROM A CHOICE THAT WAS NEVER FORCED, and put the trade where")
    print("    the author can see both sides of it.")
    print()


def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<64} {'PASS' if ok else 'FAIL'}")

    def raises(fn):
        try:
            fn()
        except ValueError:
            return True
        return False

    print()
    print("  the table is a table")
    rows = forms()
    check("every form carries all six columns",
          all(len(r) == 6 for r in rows))
    check("every carrier has a cross section",
          all(n in _xs() for _nm, c, _s, _r, _h, _b in rows for n in c))
    check("the design's salt is the first row",
          "18.9" in rows[0][0])
    check("fuelchoice's own table is left unmodified afterwards",
          "O" not in F.XS and "Pb" not in F.XS)

    print()
    print("  the result the file was written to get")
    lo, hi = crossing_band()
    check("every form has a k_inf = 1 crossing",
          all(0.0 < crossing(c) < 0.5 for _n, c, _s, _r, _h, _b in rows))
    check("  -- so the always-subcritical property is not the salt's alone",
          hi / lo < 2.0)
    check("  -- and the band is narrow, which is the finding",
          hi / lo < 1.5)
    check("the design's salt is NOT the best form on this axis",
          salt_is_special() > 1.0)
    check("  -- MOX in lead-bismuth crosses lower than the design's salt",
          crossing(rows[4][1]) < crossing(rows[0][1]))
    check("oxygen is the most transparent carrier, so oxide needs least",
          crossing(rows[3][1]) == min(crossing(c)
                                      for _n, c, _s, _r, _h, _b in rows))
    # DENSITY CANCELS, which is the physics the whole finding rests on, and
    # the cleanest way to assert it is STRUCTURAL: k_inf is a ratio of
    # macroscopic cross sections, every one of which carries the same number
    # density, so a density cannot enter the function at all. It does not.
    import inspect
    check("k_inf takes no density, because a ratio cannot depend on one",
          not any("rho" in p or "dens" in p
                  for p in inspect.signature(F.k_infinity).parameters))
    check("  -- and a form is specified by carriers PER HEAVY ATOM alone",
          all(isinstance(v, float) for _n, c, _s, _r, _h, _b in rows
              for v in c.values()))

    print()
    print("  the provenance column, which is what decides it")
    only_none = [n for n, _c, _s, _r, h, b in rows
                 if h.startswith("NONE") and b.startswith("NONE")]
    check("some form has NONE in both history and benchmarks",
          len(only_none) > 0)
    check("  -- and every one of them is the chloride",
          all("NaCl" in n for n in only_none))
    check("the ADS field's own choice is in the table",
          any("MYRRHA" in h for _n, _c, _s, _r, h, _b in rows))
    # A carrier heavy enough in absorption that NO fissile fraction reaches
    # k_inf = 1 is refused rather than returned as a number, because "the
    # threshold is 100 %" would read as an answer and is the absence of one.
    check("a form that cannot reach k_inf = 1 at all is refused",
          raises(lambda: crossing({"Cl": 2000.0})))

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it does not take the decision",
          "DOES NOT TAKE THE DECISION" in out)
    check("  -- and says what the salt uniquely buys",
          "ONLINE fission-" in out)
    check("  -- and that the cost of losing it has never been computed here",
          "never" in out and "been computed here" in out)
    check("  -- and removes the word 'forced' rather than choosing for anyone",
          "REMOVE THE WORD 'FORCED'" in out)
    check("link 1 is left standing", "LINK 1 STANDS" in out)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report()


if __name__ == "__main__":
    sys.exit(main())
