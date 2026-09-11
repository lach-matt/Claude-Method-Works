#!/usr/bin/env python3
"""aquacost.py -- Title II priced: what a desalination module costs and what
its water must sell for, with the energy at Title I's own price.

FLAWS F-16 says Title II's capital is understated three- to four-fold and
names no source for it; F-14 says $400 per acre-foot depends entirely on a
mineral offset that F-03 / F-11 / F-12 dissolved. Both name what settles
them: a bottom-up cost build per module with the energy at the Title I
contract price, and a stated financing structure. This file is that, at
mid and at critical, under the author's standing rule.

The module is the one the second pass decided: 50,000 AFY, seawater
reverse osmosis (F-13: RO is the default; LT-MED only beside a named heat
source), brownfield intake and outfall, brine returned through the retired
plant's permitted outfall (F-12: ZLD dropped), state-owned under the same
form heliocost.py prices for Title I -- municipal bonds, no developer
margin, no property tax with a PILOT in. The joinder is the energy line:
the water's electricity is bought from Title I at the price helios3.py
requires, mid or critical, so the water carries Title I's case.

Two questions and a third that joins them.

  1. What a module costs, bottom-up, against the built record (Carlsbad,
     Huntington Beach as designed), and against Title II's $250-320 M.
  2. What the water must sell for at cost recovery, per acre-foot, against
     the $400 claimed, Carlsbad's delivered price, and the wholesale price
     a California district pays today.
  3. What the water route of joinder.py costs Title II: the modules whose
     water it lifts, and the lift energy on the water's own price.

Every constant carries a status; no mineral revenue is counted (F-03,
F-11). Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import firmpower as FP                                          # noqa: E402
import helios3 as H3                                            # noqa: E402
import joinder as J                                             # noqa: E402

CASES = ("mid", "critical")
M3_PER_AF = 1233.48                       # exact
MODULE_AFY = 50_000.0                     # Title II's baseline module                  Title II §4
MODULE_M3_YR = MODULE_AFY * M3_PER_AF     # exact
TITLE_II_CAPEX_M = (250.0, 320.0)         # $M per module as submitted                  Title II §4
# --- the built record ----------------------------------------------------------
CARLSBAD_AFY = 56_000.0                   # Claude "Bud" Lewis plant, Encina brownfield  SOURCED
CARLSBAD_CAPEX_M_2015 = 1_000.0           # ~$1.0 B all-in, 2015                        SOURCED (F-16)
CARLSBAD_PRICE_AF = (2_700.0, 2_900.0)    # delivered, $/AF                             SOURCED (F-14)
HUNTINGTON_AFY = 50_000.0                 # Poseidon, as designed (denied 2022)          SOURCED
HUNTINGTON_CAPEX_M_2020 = 1_400.0         # ~$1.4 B estimate, 2020                      SOURCED band 1.2-1.5
WHOLESALE_TODAY_AF = 1_300.0              # MWD full-service treated, 2024 class          SOURCED band 1,200-1,500
DOLLAR_YEAR_RECORD = 2018                 # midpoint of the two record dollars           exact
# --- the module, bottom-up ----------------------------------------------------------
# unit capex is DERIVED from the record below, never typed: mid = Carlsbad
# (built) escalated to the groundbreaking dollar, critical = Huntington Beach
# (designed, denied) escalated -- see unit_capex_per_afy()
BUILD_YEARS = 3.0                         # F-15: not 24 months                          ASSUMED
RO_KWH_M3 = J.RO_KWH_M3                   # (3.0, 3.6) plant total with energy recovery  SOURCED band (joinder.py)
OM_NONENERGY_PER_M3 = (0.35, 0.50)        # membranes, chemicals, labour, intake/outfall upkeep  ASSUMED band (Carlsbad-class)
BRINE_OUTFALL_SHARE = 0.03                # of capex, diffuser and outfall retrofit      ASSUMED
HOUSEHOLD_AF_YR = 0.28                    # ~85 gal/person/day x 2.9 persons             SOURCED band 0.25-0.35 (urban CA)
# --- financing, Title I's form ----------------------------------------------------
BOND_RATE = H.BOND_RATE
BOND_TERM = H.BOND_TERM_Y
CONTINGENCY = HC.CONTINGENCY              # heliocost bands, index 1 mid / 2 critical
EPC_OWNER = HC.EPC_OWNER


def pick(band, case):
    return band[CASES.index(case)] if isinstance(band, tuple) else band


def record_per_afy():
    """The built record in $/AFY, escalated to the groundbreaking dollar."""
    years = sum(HC.GROUNDBREAK) / 2.0 - DOLLAR_YEAR_RECORD
    esc = (1.0 + HC.ESCALATION) ** years
    carl = CARLSBAD_CAPEX_M_2015 * 1e6 / CARLSBAD_AFY * (1.0 + HC.ESCALATION) ** (DOLLAR_YEAR_RECORD - 2015)
    hunt = HUNTINGTON_CAPEX_M_2020 * 1e6 / HUNTINGTON_AFY / (1.0 + HC.ESCALATION) ** (2020 - DOLLAR_YEAR_RECORD)
    return dict(carlsbad=carl * esc, huntington=hunt * esc, esc=esc, years=years)


def unit_capex_per_afy(case):
    """$/AFY overnight in groundbreaking dollars: mid = Carlsbad built, critical = Huntington designed.  DERIVED"""
    rec = record_per_afy()
    return rec["carlsbad"] if case == "mid" else rec["huntington"]


def energy_price(case):
    """Title I's required price with the register, $/MWh -- the joinder's energy line."""
    return H3.priced(case)["price"]


def module(case, lift_kwh_m3=0.0):
    ci = CASES.index(case)
    overnight = unit_capex_per_afy(case) * MODULE_AFY / 1e6                     # $M
    overnight *= (1.0 + BRINE_OUTFALL_SHARE)
    over = overnight * (1.0 + CONTINGENCY[ci + 1] + EPC_OWNER[ci + 1])
    import predev as PD                                                              # lazy: predev imports helios only
    studies = PD.title2_per_site(case)["per_module_m"]                               # the author's first line, per module
    over += studies * (1.0 + CONTINGENCY[ci + 1])
    financed = over * (1.0 + BOND_RATE * BUILD_YEARS / 2.0)                         # simple IDC; the dollars are already 2028-30
    debt = H.debt_service_m(financed / 1e3, BOND_RATE, BOND_TERM)                    # $M/yr
    kwh = (RO_KWH_M3[ci] + lift_kwh_m3) * MODULE_M3_YR                               # kWh/yr
    energy_m = kwh / 1e3 * energy_price(case) / 1e6                                  # $M/yr
    om_m = OM_NONENERGY_PER_M3[ci] * MODULE_M3_YR / 1e6
    total_m = debt + energy_m + om_m
    per_af = total_m * 1e6 / MODULE_AFY
    return dict(case=case, overnight_m=overnight, studies_m=studies, financed_m=financed, debt_m=debt, energy_m=energy_m,
                om_m=om_m, total_m=total_m, per_af=per_af, per_m3=per_af / M3_PER_AF,
                energy_price=energy_price(case), kwh_m3=RO_KWH_M3[ci] + lift_kwh_m3,
                household=per_af * HOUSEHOLD_AF_YR)


def water_route(case):
    """The modules the ADOPTED route (both.py: water at half the shortfall, delivered
    year-round) lifts, and their water priced with the lift. Water alone at design
    field and store has no feasible closing point on the corrected load shape -- its
    own surplus cannot lift what closes -- so the route priced here is the adopted one."""
    import both as B                                           # lazy: both imports this module
    m = B.scan(case)["best"]
    lift = J.hydraulic_per_m3(case)["lift_kwh_m3"]
    mod = module(case, lift_kwh_m3=lift)
    return dict(modules=m["modules"], maf=m["maf"], capex_b=mod["financed_m"] * m["modules"] / 1e3,
                per_af=mod["per_af"], household=mod["household"], lift=lift, mod=mod)


def report():
    rec = record_per_afy()
    print()
    print("  TITLE II PRICED: THE MODULE AND ITS WATER, AT MID AND AT CRITICAL")
    print("  ===================================================================")
    print("    F-16: capital understated three- to four-fold, no source named. F-14:")
    print("    $400 per acre-foot rests on a mineral offset that is gone. Both settle")
    print("    on a bottom-up build with the energy at Title I's own price -- which")
    print("    is the joinder, and which carries Title I's case into the water.")
    print()
    print("    1. THE MODULE. 50,000 AFY seawater RO on a coastal brownfield, brine")
    print("       through the existing outfall, state-owned on Title I's form.")
    print(f"       The built record, escalated to {sum(HC.GROUNDBREAK) / 2:.0f} dollars at {100 * HC.ESCALATION:.0f} %/yr:")
    print(f"         Carlsbad (56,000 AFY, 2015, ~$1.0 B)      ${rec['carlsbad']:,.0f} per AFY")
    print(f"         Huntington Beach (50,000 AFY, 2020 est.)  ${rec['huntington']:,.0f} per AFY")
    print(f"         Title II as submitted ($250-320 M)        ${TITLE_II_CAPEX_M[0] * 1e6 / MODULE_AFY:,.0f}-{TITLE_II_CAPEX_M[1] * 1e6 / MODULE_AFY:,.0f} per AFY")
    print()
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    mods = {c: module(c) for c in CASES}
    for label, key, fmt in (("unit capex, $/AFY", None, None),
                            ("overnight per module, $M", "overnight_m", "{:12,.0f}"),
                            ("financed (contingency, EPC, IDC), $M", "financed_m", "{:12,.0f}"),
                            ("  against Title II's $250-320 M, x", None, None),
                            ("debt service, $M/yr", "debt_m", "{:12,.1f}"),
                            ("electricity, kWh/m3", "kwh_m3", "{:12.1f}"),
                            ("  at Title I's price, $/MWh", "energy_price", "{:12,.0f}"),
                            ("energy, $M/yr", "energy_m", "{:12,.1f}"),
                            ("non-energy O&M, $M/yr", "om_m", "{:12,.1f}"),
                            ("total, $M/yr", "total_m", "{:12,.1f}")):
        if key is None and "unit" in label:
            print(f"      {label:<40}" + "".join(f"{unit_capex_per_afy(c):12,.0f}" for c in CASES))
        elif key is None:
            print(f"      {label:<40}" + "".join(f"{mods[c]['financed_m'] / (sum(TITLE_II_CAPEX_M) / 2):12.1f}" for c in CASES))
        else:
            print(f"      {label:<40}" + "".join(fmt.format(mods[c][key]) for c in CASES))
    print()
    print("    2. THE WATER, at cost recovery (debt service + O&M, no mineral revenue):")
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    print(f"      {'$ per acre-foot':<40}" + "".join(f"{mods[c]['per_af']:12,.0f}" for c in CASES))
    print(f"      {'$ per m3':<40}" + "".join(f"{mods[c]['per_m3']:12.2f}" for c in CASES))
    print(f"      {'  of which energy':<40}" + "".join(f"{mods[c]['energy_m'] / mods[c]['total_m']:12.0%}" for c in CASES))
    print(f"      {'$ per household per year (0.28 AF)':<40}" + "".join(f"{mods[c]['household']:12,.0f}" for c in CASES))
    print(f"       Against: Title II's claim ${400:,.0f}/AF; Carlsbad delivered ${CARLSBAD_PRICE_AF[0]:,.0f}-{CARLSBAD_PRICE_AF[1]:,.0f};")
    print(f"       wholesale today ~${WHOLESALE_TODAY_AF:,.0f}. The claim was {mods['mid']['per_af'] / 400:.1f}x (mid) / {mods['critical']['per_af'] / 400:.1f}x (critical)")
    print("       below the cost; the cost sits where the built record sits. Desalinated")
    print("       water is not cheap water; it is firm water, and it is priced as such.")
    print()
    print("    3. THE WATER ROUTE (joinder.py): the modules it lifts, with the lift on")
    print("       the water's own bill:")
    wr = {c: water_route(c) for c in CASES}
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    print(f"      {'modules at 500 m':<40}" + "".join(f"{wr[c]['modules']:12.1f}" for c in CASES))
    print(f"      {'water, M acre-feet/yr':<40}" + "".join(f"{wr[c]['maf']:12.2f}" for c in CASES))
    print(f"      {'modules capital, financed, $B':<40}" + "".join(f"{wr[c]['capex_b']:12.1f}" for c in CASES))
    print(f"      {'lift, kWh/m3':<40}" + "".join(f"{wr[c]['lift']:12.2f}" for c in CASES))
    print(f"      {'$ per acre-foot with the lift':<40}" + "".join(f"{wr[c]['per_af']:12,.0f}" for c in CASES))
    print(f"      {'$ per household per year':<40}" + "".join(f"{wr[c]['household']:12,.0f}" for c in CASES))
    print("       This is Title II's capital, beside the reservoir and pump-turbines")
    print("       joinder.py priced to Title I. The parity on the power side stands;")
    print("       what the water route adds is a water program of this size, priced")
    print("       at what firm water costs. Whether California wants that much firm")
    print("       water at that price is the joinder's question, now with a number.")
    print()
    print("    WHAT THIS DOES NOT DO. It counts no mineral revenue (F-03, F-11), prices")
    print("    no site, and takes the unit capex from two plants -- one built, one")
    print("    designed and denied. The energy price is Title I's register price at")
    print("    each case; a plant serving its whole load would charge more (rebase.py)")
    print("    and the water would follow it.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    rec = record_per_afy()
    check("the record, escalated, is 3-8x Title II's unit capex (F-16's 3-4x was itself understated)",
          all(3.0 < v / (sum(TITLE_II_CAPEX_M) / 2 * 1e6 / MODULE_AFY) < 8.0 for v in (rec["carlsbad"], rec["huntington"])))
    check("the mid unit capex IS Carlsbad escalated (derived, not typed)", unit_capex_per_afy("mid") == rec["carlsbad"])
    check("critical unit capex is above mid", unit_capex_per_afy("critical") > unit_capex_per_afy("mid"))
    check("Carlsbad's 2015 figure is ~$18,000/AFY before escalation",
          abs(CARLSBAD_CAPEX_M_2015 * 1e6 / CARLSBAD_AFY - 17_857) < 100)
    mods = {c: module(c) for c in CASES}
    check("critical water costs more than mid", mods["critical"]["per_af"] > mods["mid"]["per_af"])
    esc_price = CARLSBAD_PRICE_AF[0] * (1.0 + HC.ESCALATION) ** (sum(HC.GROUNDBREAK) / 2.0 - 2024)
    check("the mid water price is at or above Carlsbad's delivered price escalated to the same dollar (the record, not a hope)",
          mods["mid"]["per_af"] >= esc_price * 0.9)
    check("the $400 claim is at least 4x below the cost at both cases", all(mods[c]["per_af"] > 4 * 400 for c in CASES))
    check("energy is a minority of the water's cost at both cases (capital dominates RO)",
          all(mods[c]["energy_m"] / mods[c]["total_m"] < 0.5 for c in CASES))
    check("the energy price is helios3's register price, imported not restated",
          all(abs(mods[c]["energy_price"] - H3.priced(c)["price"]) < 1e-9 for c in CASES))
    check("debt service = helios.debt_service_m on the financed capital",
          all(abs(mods[c]["debt_m"] - H.debt_service_m(mods[c]["financed_m"] / 1e3, BOND_RATE, BOND_TERM)) < 1e-9 for c in CASES))
    wr = {c: water_route(c) for c in CASES}
    check("the lift adds to the water's price and never subtracts",
          all(wr[c]["per_af"] > mods[c]["per_af"] for c in CASES))
    import both as B
    check("the route's module count is both.py's adopted point (imported)",
          all(abs(wr[c]["modules"] - B.scan(c)["best"]["modules"]) < 1e-9 for c in CASES))
    check("water alone at design field and store has no feasible closing point (its surplus cannot lift what closes)",
          all(J.evening_with_water(c, 500.0, J.winter(c))["closing"] is None for c in CASES))
    head = open(__file__).read().split("def pick")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES", "BOND_", "CONTINGENCY", "EPC_OWNER"))]
    check("every constant line carries a status",
          all(any(t in l for t in ("SOURCED", "ASSUMED", "exact", "Title II", "joinder")) for l in consts))
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report counts no mineral revenue and says so", "no mineral revenue" in out and "counts no mineral revenue" in out)
    check("the report prints both cases", "critical" in out and "mid" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
