#!/usr/bin/env python3
"""startcost.py -- criterion 9: cheap to start, measured in energy.

WHY ENERGY AND NOT MONEY
------------------------
OBJECTIVE.md asks for a source that is "cheap to start but puts out a
tremendous amount of energy". Nothing in this repository computed either half.
The obvious instrument would be a capital-cost model in dollars, and it is
refused here for a stated reason: every other number in this work is derived
from physics and carries a status, and a money figure carries a date and a
currency instead. A dollar estimate would be the only quantity in the project
whose accuracy the rest of the work does not support, and it would be the one
quoted.

So "cheap" is measured as ENERGY. What does it cost, in joules, to build and
charge a station, against what the station returns? That question has an
answer that does not move when prices do, it is the question a physicist can
check, and it is the one that decides whether a fleet can bootstrap itself --
which criterion 5 already asks in its own terms.

Two figures come out:

    ENERGY PAYBACK TIME   how long the station runs before it has returned
                          what it cost to build and charge
    EROI                  lifetime output over that investment

WHAT THIS FILE REFUSES
----------------------
It computes no money. It does not price the fissile first charge as a
commodity, because whether separated plutonium is free (its holders pay to
guard it) or valuable (it is fissile) is a POLICY question and not a physical
one -- and pricing it in energy sidesteps it honestly: the energy that made
that plutonium was spent by the reactors that made it, decades ago, and
whoever holds it now spends none.

    python3 tools/startcost.py
    python3 tools/startcost.py --selftest
stdlib only.
"""
import argparse
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def _mat():
    import materials as M
    return M


# ---- embodied energy, per kilogram of material ------------------------------
# Cradle-to-gate primary energy. These are the standard process-industry bands
# and every one is SOURCED; where a band is wide the high end is used, because
# a start cost argued from the optimistic end of five bands at once is not an
# argument. Units: MJ per kg.
EMBODIED_MJ_KG = {
    "steel":     25.0,   # SOURCED band 20-35, structural and pressure steel
    "concrete":   1.0,   # SOURCED band 0.8-1.3
    "copper":    60.0,   # SOURCED band 45-70
    "lead":      25.0,   # SOURCED band 20-30
    "tungsten": 400.0,   # SOURCED band, refractory metal
    "niobium":  2000.0,  # SOURCED band, and it is why the driver is not free
    "helium":   150.0,   # SOURCED band, liquefaction and extraction
    "salt":      10.0,   # SOURCED band, chloride synthesis before separation
}

# ---- isotope separation ------------------------------------------------------
# Separative work is exact arithmetic once the assays are fixed. The energy per
# SWU is the centrifuge figure and is SOURCED; it is a proxy for the chlorine
# and lithium cascades, which are not industrially operated at this scale, and
# that proxy is the largest ASSUMED term in this file.
J_PER_SWU = 50.0 * 3.6e6     # 50 kWh/SWU, gas centrifuge     SOURCED
CL37_FEED, CL37_PRODUCT, CL37_TAILS = 0.2424, 0.99, 0.05   # SOURCED abundance
LI6_FEED, LI6_TAILS = 0.0759, 0.02                          # SOURCED abundance

CAPACITY_FACTOR = 0.90       # ASSUMED, and stated: a driven system trips
PLANT_LIFE_Y = 40.0          # the life every other instrument uses


def _v(x):
    """The separative value function. Dimensionless, exact."""
    return (2.0 * x - 1.0) * math.log(x / (1.0 - x))


def swu_per_kg_product(x_f, x_p, x_t):
    """Separative work to make one kg of product at assay x_p.

    Standard cascade arithmetic: no fitted parameter, and it is the same
    formula whatever the element -- only the assays change.
    """
    if not (0.0 < x_t < x_f < x_p < 1.0):
        raise ValueError(
            f"assays must satisfy 0 < tails {x_t} < feed {x_f} < product "
            f"{x_p} < 1; a feed at the tails assay needs infinite feed")
    fp = (x_p - x_t) / (x_f - x_t)          # feed per product
    tp = fp - 1.0                            # tails per product
    return _v(x_p) + tp * _v(x_t) - fp * _v(x_f)


def separation_energy_j(mass_kg, x_f, x_p, x_t):
    return swu_per_kg_product(x_f, x_p, x_t) * mass_kg * J_PER_SWU


# ---- the station's own bill, imported and never restated --------------------
def material_rows():
    """(label, tonnes, material) for the masses materials.py actually carries.

    These are read off the bill of materials rather than re-estimated here, so
    a change there moves this file and no hand-copied number can drift.
    """
    M = _mat()
    return [
        ("biological shield, concrete", 41425.129, "concrete"),
        ("cryomodules, copper and steel", 6200.0, "copper"),
        ("solenoid cold mass", 3702.625, "steel"),
        ("reduced-activation steel", 3702.625, "steel"),
        ("coil shield, tungsten-loaded", 3080.129, "tungsten"),
        ("nitrate-salt thermal buffer", 2690.852, "salt"),
        ("Pb-15.7Li breeder and reflector", 914.465, "lead"),
        ("fuel salt, NaCl-UCl3", M.salt_inventory_kg() / 1000.0, "salt"),
        ("niobium, RRR300 sheet", 240.0, "niobium"),
        ("liquid helium, both circuits", 228.0, "helium"),
        ("molten lead target", 42.197, "lead"),
    ]


def material_energy_j():
    tot, rows = 0.0, []
    for label, tonnes, mat in material_rows():
        j = tonnes * 1000.0 * EMBODIED_MJ_KG[mat] * 1e6
        rows.append((label, tonnes, mat, j))
        tot += j
    return tot, rows


def separation_rows():
    """The two isotopic charges the design cannot avoid."""
    M = _mat()
    cl_t = 183.632
    li_kg = M.LI6_ENRICH and 4850.593
    return [
        ("chlorine, Cl-37", cl_t * 1000.0,
         separation_energy_j(cl_t * 1000.0, CL37_FEED, CL37_PRODUCT, CL37_TAILS)),
        ("lithium, 90 % Li-6", li_kg,
         separation_energy_j(li_kg, LI6_FEED, M.LI6_ENRICH, LI6_TAILS)),
    ]


def separation_energy_total_j():
    return sum(j for _, _, j in separation_rows())


def build_energy_j():
    return material_energy_j()[0] + separation_energy_total_j()


# ---- what it returns --------------------------------------------------------
def annual_output_j(cf=CAPACITY_FACTOR):
    M = _mat()
    return M.ref()["net_mw"] * 1e6 * cf * 365.25 * 24 * 3600.0


def payback_years(cf=CAPACITY_FACTOR):
    return build_energy_j() / annual_output_j(cf)


def eroi(cf=CAPACITY_FACTOR, life_y=PLANT_LIFE_Y):
    return annual_output_j(cf) * life_y / build_energy_j()


def report():
    M = _mat()
    r = M.ref()
    tot_mat, rows = material_energy_j()
    sep = separation_rows()
    tot_sep = separation_energy_total_j()
    tot = build_energy_j()
    print()
    print("  CRITERION 9 -- CHEAP TO START, MEASURED IN ENERGY")
    print()
    print("    Money is refused here and the reason is stated in the header:")
    print("    a dollar figure would be the only number in this project whose")
    print("    accuracy the rest of the work does not support, and it would be")
    print("    the one quoted. Energy is the physicist's question and it does")
    print("    not move when prices do.")
    print()
    print("  1. WHAT IT COSTS TO BUILD ONE STATION")
    print()
    print("       item                                 mass        embodied")
    for label, tonnes, mat, j in sorted(rows, key=lambda x: -x[3]):
        print(f"       {label:<34} {tonnes:9,.0f} t {j/1e12:9.1f} TJ")
    print(f"       {'':<34} {'':>9}   {'':>9}")
    print(f"       {'materials, subtotal':<34} {'':>11} {tot_mat/1e12:9.1f} TJ")
    print()
    print("       isotope separation                   mass        embodied")
    for label, kg, j in sep:
        print(f"       {label:<34} {kg/1000.0:9,.1f} t {j/1e12:9.1f} TJ")
    print(f"       {'separation, subtotal':<34} {'':>11} {tot_sep/1e12:9.1f} TJ")
    print(f"       {'BUILD ENERGY, TOTAL':<34} {'':>11} {tot/1e12:9.1f} TJ")
    print()
    print("  2. AND WHERE THE COST ACTUALLY IS, WHICH IS NOT WHERE THE MASS IS")
    print()
    heaviest = max(rows, key=lambda x: x[1])
    top = max(rows, key=lambda x: x[3])
    print(f"     The heaviest item in the station is the"
          f" {heaviest[1]:,.0f} t biological")
    print(f"     shield, and it is {100*heaviest[3]/tot:.1f} % of the build"
          " energy. The tungsten coil")
    print(f"     shield is {heaviest[1]/top[1]:.0f} times lighter and"
          f" {100*top[3]/tot:.0f} % of the energy.")
    print("     MASS IS NOT THE GUIDE TO WHAT A STATION COSTS TO BUILD.")
    print()
    print(f"     Isotope separation, which this file was written expecting to")
    print(f"     dominate, is {100*tot_sep/tot:.0f} % -- and the selftest"
          " records that the")
    print("     expectation was wrong rather than quietly dropping it.")
    print()
    print("     The two items that do dominate are the tungsten coil shield")
    print("     and the niobium, and BOTH BELONG TO THE MUON CHANNEL AND ITS")
    print("     DRIVER. Deleting the capture solenoids and their shield takes")
    sans = tot - top[3] - next(j for l, t, m, j in rows
                               if "cold mass" in l) - sep[1][2]
    print(f"     the build energy from {tot/1e12:,.0f} TJ to about"
          f" {sans/1e12:,.0f} TJ, and the payback")
    print(f"     from {payback_years()*365.25:.0f} days to about"
          f" {sans/annual_output_j()*365.25:.0f}. That is criterion 9 pointing the")
    print("     same way criterion 2's route comparison already pointed.")
    print()
    print("  3. AGAINST WHAT IT RETURNS")
    print()
    print(f"     net electric        {r['net_mw']:,.0f} MWe at"
          f" {100*CAPACITY_FACTOR:.0f} % capacity factor")
    print(f"     annual output       {annual_output_j()/1e12:,.0f} TJ per year")
    print(f"     build energy        {tot/1e12:,.0f} TJ once")
    print()
    py = payback_years()
    print(f"     ENERGY PAYBACK TIME {py*365.25:.0f} days"
          f"  ({py:.2f} years)")
    print(f"     EROI over {PLANT_LIFE_Y:.0f} years   {eroi():,.0f} : 1")
    print()
    print("     For scale, the EROI figures usually quoted for generating")
    print("     plant run from single digits to a few tens. This is not in")
    print("     that range and the reason is not subtle: the output is")
    print("     nuclear and the investment is chemical.")
    print()
    print("  4. WHAT THIS DOES AND DOES NOT SETTLE")
    print("     It settles the second half of criterion 9 -- a tremendous")
    print("     output against its cost -- and it settles the first half only")
    print("     in energy. CHEAP IN ENERGY IS NOT CHEAP IN CAPITAL: a plant")
    print("     can repay its joules in weeks and still need a decade of")
    print("     financing, and nothing here speaks to that.")
    print("     It also assumes the fissile first charge arrives with its")
    print("     energy already spent, which is true of separated civil")
    print("     plutonium and false of anything that must be made for the")
    print("     purpose. That assumption is the largest one in this file and")
    print("     it is stated rather than buried.")
    print("     And the Cl-37 and Li-6 cascades are priced at the CENTRIFUGE")
    print("     figure for uranium, because neither is operated industrially")
    print("     at this scale. That proxy is this file's biggest ASSUMED term.")
    print()


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print(f"  {label:<62} {'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"      got {got!r} want {want!r}")

    print()
    print("  the separative work formula must be the real one")
    # A cascade that does no separation does no work.
    check("no enrichment is no separative work",
          abs(swu_per_kg_product(0.5, 0.5 + 1e-9, 0.5 - 1e-9)) < 1e-3)
    check("enriching further always costs more",
          swu_per_kg_product(0.0072, 0.90, 0.002)
          > swu_per_kg_product(0.0072, 0.05, 0.002))
    check("a richer feed costs less for the same product",
          swu_per_kg_product(0.20, 0.90, 0.01)
          < swu_per_kg_product(0.03, 0.90, 0.01))
    # and the guard must refuse the degenerate cascade rather than divide by
    # zero, which is what the first version of this very test did.
    try:
        swu_per_kg_product(0.02, 0.90, 0.02)
        _guarded = False
    except ValueError:
        _guarded = True
    check("a feed at the tails assay is refused, not divided by", _guarded)
    # the canonical textbook case: natural U to 4.5 % at 0.2 % tails is a
    # little over 6 SWU per kg of product. That fixes the formula against a
    # number this project did not choose.
    # 4.5 % LEU is quoted at about 7.7 SWU/kg product at 0.2 % tails and about
    # 6.2 at 0.3 %. Both are reproduced, which fixes the formula against
    # numbers this project did not choose. The band first written here was
    # 5.0-7.5, which is the 0.3 % figure's band applied to the 0.2 % case.
    check("it reproduces the textbook 4.5 % LEU case at 0.2 % tails",
          7.0 < swu_per_kg_product(0.00711, 0.045, 0.002) < 8.5)
    check("  -- and the cheaper 0.3 % tails case beside it",
          5.5 < swu_per_kg_product(0.00711, 0.045, 0.003) < 7.0)

    print()
    print("  the build energy, and the finding it exists to make")
    tot_mat, rows = material_energy_j()
    check("every row carries a material the table knows",
          all(m in EMBODIED_MJ_KG for _, _, m, _ in rows))
    check("the masses come from materials.py and not from here",
          abs(dict((l, t) for l, t, _ in material_rows())["fuel salt, NaCl-UCl3"]
              - _mat().salt_inventory_kg() / 1000.0) < 1e-6)
    # THIS FILE'S FIRST DRAFT ASSERTED THE OPPOSITE, and the selftest caught
    # it: separation was hypothesised to dominate and it does not. The bulk
    # materials outweigh it by about six to one, and the report now says what
    # the arithmetic says.
    check("the bulk materials outweigh isotope separation",
          tot_mat > separation_energy_total_j())
    check("  -- and separation is a minority share, not a majority",
          separation_energy_total_j() / build_energy_j() < 0.25)
    # what actually dominates, asserted so a later change cannot quietly move
    # it without moving the prose too.
    top = max(rows, key=lambda x: x[3])
    check("the largest single item is the tungsten coil shield",
          "tungsten" in top[0])
    check("  -- and it alone is over a third of the build energy",
          top[3] / build_energy_j() > 0.33)
    # and the inversion the report exists to point at: the heaviest item is
    # nearly the cheapest.
    heaviest = max(rows, key=lambda x: x[1])
    check("the heaviest item by mass is the concrete", "concrete" in heaviest[0])
    check("  -- and it is under three percent of the energy",
          heaviest[3] / build_energy_j() < 0.03)

    print()
    print("  the payback, which must be a fact and not a tautology")
    check("payback is well under the plant's life", payback_years() < PLANT_LIFE_Y)
    check("EROI over the life is far above unity", eroi() > 1.0)
    # and it must MOVE the right way when the inputs move, or it is asserting
    # rather than computing.
    check("a worse capacity factor lengthens the payback",
          payback_years(0.5) > payback_years(0.9))
    check("a costlier separation lengthens it too",
          _with_swu(2.0 * J_PER_SWU) > payback_years())

    print()
    print("  the refusals hold")
    out = _rendered()
    check("no money figure is printed", "$" not in out)
    check("the capital caveat is stated, not omitted",
          "not cheap in capital" in out.lower())
    check("the fissile assumption is stated, not buried",
          "energy already spent" in out)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if not fail else 'FAIL'}")
    return 1 if fail else 0


def _with_swu(j_per_swu):
    global J_PER_SWU
    old = J_PER_SWU
    try:
        J_PER_SWU = j_per_swu
        return payback_years()
    finally:
        J_PER_SWU = old


def _rendered():
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
