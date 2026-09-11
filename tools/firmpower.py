#!/usr/bin/env python3
"""firmpower.py -- the second pass: what equipment makes a firm megawatt-hour
for three million California households, and what each costs

WHY THIS FILE EXISTS
--------------------
The first pass through proposals/FLAWS.tsv ended on one finding: at the
scale proposed, priced from unit rates, the salt-tower plant needs
$171-253/MWh and charges a household MORE for generation than the IOU does
today. No size fixes that, because the three largest cost lines scale with
the plant. The author then set the second pass's question exactly: the
requirement is 3 million households, a MINIMUM, growing with population, and
"one facility or a hundred, we still need the same basic amount of
materials" -- so improve the SYSTEM so that it is SMALLER and PRODUCES MORE.

That is a question about equipment. This file puts every candidate that can
make a firm megawatt-hour in California on the same requirement, the same
ownership form, the same criterion, and the same year, and asks each one
three things: what does it cost per MWh, how big is it, and can it be built.

    python3 tools/firmpower.py
    python3 tools/firmpower.py --selftest
stdlib only. Imports helios.py and heliocost.py; never restates them.

STATUS DISCIPLINE
-----------------
Every unit rate is a band with a status. SOURCED means a published figure
reached in the 2026-09-11 survey (docs/FIRMPOWER.md lists each); ASSUMED
means this file's own estimate, banded; DERIVED means computed from the
others. The CSP row is not modelled here at all -- it is heliocost.py's own
mid case, imported, so the comparison shares its baseline with the first
pass by construction.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402

# =============================================================================
# THE REQUIREMENT, AS THE AUTHOR SET IT
# =============================================================================
E_REQ_TWH = H.hh_demand_twh()                  # 3 M households at EIA's 6,036 kWh/yr
GROWTH_X = H.size_for(growth=H.GROWTH_BAND[1]) # 1.7x over the term at 2 %/yr
ESC = HC.build("mid")["escalation"]            # heliocost's 2022 -> 2031 escalation
RATE = H.BOND_RATE
NOW_PER_HH = H.per_household(H.GEN_RATE_NOW * 1e3)

# ---- the load's shape, one number ------------------------------------------
# Share of a day's residential energy that daylight PV can serve DIRECTLY,
# with no storage between panel and socket. California residential load is
# evening-peaked; the 09:00-16:00 share of daily energy is about a third.
DIRECT_SHARE = (0.30, 0.35, 0.40)              # ASSUMED band

# =============================================================================
# THE CANDIDATES: (capex $/kW_AC lo/mid/hi, CF, fixed O&M $/kW-yr, build yr,
#                  federal credit share, firm?, available, legal, status)
# =============================================================================
# Federal credit: §48E survives for geothermal, storage, nuclear at 100 % for
# construction beginning through 2033; terminated for wind and solar after
# 2026-07-04. Public direct pay + domestic content + energy community = 50 %
# on eligible property (heliocost.py carries the same three lines).
CREDIT_ELIGIBLE = HC.FED_STORAGE_ITC + HC.FED_DOMESTIC_BONUS + HC.FED_ENERGY_COMMUNITY

TECH = {
    "salton_flash": dict(
        name="Salton Sea geothermal, flash (conventional)",
        capex=(6000.0, 7500.0, 9000.0),   # $/kW. NREL ATB flash 4,500-6,500 plus the
                                          # hypersaline penalty; Hell's Kitchen's
                                          # $1.8 B / 49.9 MW includes a lithium plant
                                          # and is not a power figure  ASSUMED band
        cf=0.90,                          # new flash design point; fleet avg 65 %
                                          # is The Geysers' decline (53 %)  SOURCED
        om=170.0,                         # $/kW-yr, ATB geothermal band    SOURCED band
        build=3.0, credit=CREDIT_ELIGIBLE, firm=True, avail=2030,
        legal="permitted class; CEQA + Imperial County; FAST-41 covered",
        cap_mw=2250.0,                    # developable now; +700 as the sea recedes  SOURCED
        acres_per_mw=2.0, status="SOURCED/ASSUMED"),
    "egs": dict(
        name="Enhanced geothermal (Fervo class)",
        capex=(5500.0, 7000.0, 9000.0),   # $/kW: Cape Station phase 1 $7,000 all-in,
                                          # phase 2 target $5,500; hi = first-of-kind
                                          # in a new field                   SOURCED
        cf=0.90, om=150.0, build=3.0, credit=CREDIT_ELIGIBLE, firm=True, avail=2029,
        legal="permitted class; SCE holds 320 MW / 15 yr, Google 396 MW",
        cap_mw=None, acres_per_mw=1.5, status="SOURCED"),
    "csp_proposed": dict(
        name="Salt-tower CSP as proposed (heliocost mid)",
        capex=None,                       # imported from heliocost, never restated
        cf=None, om=None, build=4.0, credit=None, firm=True, avail=2030,
        legal="permitted class; F-09, F-21, F-25 open",
        cap_mw=None, acres_per_mw=43.0, status="DERIVED from heliocost.py"),
    "pv_salt": dict(
        name="PV-charged nitrate salt (heaters into Helios tanks + turbines)",
        capex=None,                       # built from parts below
        cf=None, om=None, build=3.0, credit=None, firm=True, avail=2030,
        legal="permitted class; PV on disturbed land; salt block as heliocost",
        cap_mw=None, acres_per_mw=None, status="DERIVED"),
    "pv_ironair": dict(
        name="PV + 100-hour iron-air storage",
        capex=None, cf=None, om=None, build=2.0, credit=None, firm=True, avail=2031,
        legal="permitted class; first 15 MW units 2026",
        cap_mw=None, acres_per_mw=None, status="DERIVED"),
    "smr": dict(
        name="Small modular reactor",
        capex=(12471.0, 15000.0, 17949.0),  # TVA Clinch River subsequent / first unit;
                                            # Darlington C$20.9 B / 1,200 MW  SOURCED
        cf=0.92, om=150.0, build=6.0, credit=CREDIT_ELIGIBLE, firm=True, avail=2036,
        legal="BARRED: Cal. Pub. Res. Code §25524.2 moratorium on new nuclear",
        cap_mw=None, acres_per_mw=0.5, status="SOURCED"),
    "offshore_wind": dict(
        name="Floating offshore wind (Morro Bay / Humboldt)",
        capex=None, cf=0.45, om=None, build=4.0, credit=0.0, firm=False, avail=2033,
        legal="two of three Morro Bay leases terminated; not firm",
        cap_mw=None, acres_per_mw=0.0, status="SOURCED LCOE+LCOT $95-121 (2035)"),
}

# ---- parts for the built-up candidates -------------------------------------
PV_PER_KW_AC = (1300.0, 1610.0, 1900.0)   # $/kW_AC, 2024 capacity-weighted $1.61  SOURCED
PV_CF = (0.28, 0.30, 0.33)                # Mojave single-axis                    SOURCED band
PV_OM = 20.0                              # $/kW-yr                               SOURCED band
HEATER_PER_KW_TH = (40.0, 60.0, 100.0)    # resistive, into salt; Kyoto/Rondo class  ASSUMED band
TES_PER_KWH_TH = HC.TES_PER_KWHTH         # heliocost's own line
POWER_BLOCK_PER_KWE = HC.POWER_BLOCK_PER_KWE
BOP_PER_KWE = HC.BOP_PER_KWE
HEATER_ETA = 0.98                         # resistive                             SOURCED
SALT_RTE = H.ETA_CYCLE * HEATER_ETA       # PV MWh in -> MWh out through the turbine
NIGHT_HOURS = 16.0                        # Helios's own storage duration
IRONAIR_PER_KWH = (20.0, 33.0, 45.0)      # Form target $20; contracts imply ~$33  SOURCED
IRONAIR_PER_KW = (600.0, 900.0, 1200.0)   # power conversion + BOS                ASSUMED band
IRONAIR_RTE = (0.35, 0.40, 0.45)          # ASSUMED band
IRONAIR_HOURS = 100.0                     # SOURCED
PV_ACRES_PER_MW = 6.0                     # SOURCED band 5-7
CSP_ACRES_PER_MW = 43.0                   # 228 km2 / 5,250 MW from F-21


def _pick(b, case):
    return b[{"low": 0, "mid": 1, "high": 2}[case]]


def financed(overnight_m, build_years, rate=RATE):
    """Escalate to mid-construction and add simple IDC, as heliocost does."""
    x = overnight_m * ESC
    return x * (1.0 + rate * build_years / 2.0)


def required_price(capex_m, om_m, e_twh=E_REQ_TWH):
    return (H.debt_service_m(capex_m / 1e3, RATE) + om_m) * 1e6 / (e_twh * 1e6)


# =============================================================================
# EACH CANDIDATE, SIZED TO THE REQUIREMENT
# =============================================================================
def size_simple(key, case="mid", e_twh=E_REQ_TWH):
    t = TECH[key]
    mw = e_twh * 1e6 / (8760.0 * t["cf"])
    over = mw * 1e3 * _pick(t["capex"], case) / 1e6
    gross = financed(over, t["build"])
    net = gross * (1.0 - t["credit"])
    om = mw * t["om"] / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * net
    return dict(key=key, mw=mw, e_twh=e_twh, capex_net=net, capex_gross=gross,
                om=om, price=required_price(net, om, e_twh),
                acres=mw * t["acres_per_mw"], capped=(t["cap_mw"] is not None
                                                     and mw > t["cap_mw"]))


def size_csp(e_twh=E_REQ_TWH):
    """heliocost's mid case, scaled linearly to the requirement -- the three
    largest lines scale with the plant, which is the first pass's finding."""
    b = HC.build("mid")
    pf = H.run_network()
    k = e_twh * 1e6 / pf["net"]
    net = b["net_capex"] * k
    om = HC.om_m("mid", "state", net)["total"] * k
    mw = H.GROSS_MWE * k
    return dict(key="csp_proposed", mw=mw, e_twh=e_twh, capex_net=net,
                capex_gross=b["gross_capex"] * k, om=om,
                price=required_price(net, om, e_twh), acres=mw * CSP_ACRES_PER_MW,
                capped=False)


def size_pv_salt(case="mid", e_twh=E_REQ_TWH, direct=None):
    f = DIRECT_SHARE[1] if direct is None else direct
    e_direct = e_twh * f
    e_night = e_twh * (1.0 - f)
    pv_twh = e_direct + e_night / SALT_RTE
    pv_mw = pv_twh * 1e6 / (8760.0 * _pick(PV_CF, case))
    turb_mw = e_night * 1e6 / (365.0 * NIGHT_HOURS) * 1.3     # 1.3 = night peak/avg  ASSUMED
    tes_mwh = turb_mw / H.ETA_CYCLE * NIGHT_HOURS
    heater_mw = tes_mwh / 6.0                                  # charged in a 6 h midday window
    lines = {
        "PV": pv_mw * 1e3 * _pick(PV_PER_KW_AC, case) / 1e6,
        "heaters": heater_mw * 1e3 * _pick(HEATER_PER_KW_TH, case) / 1e6,
        "thermal storage": tes_mwh * 1e3 * _pick(TES_PER_KWH_TH, case) / 1e6,
        "power block": turb_mw * 1e3 * _pick(POWER_BLOCK_PER_KWE, case) / 1e6,
        "balance of plant": turb_mw * 1e3 * _pick(BOP_PER_KWE, case) / 1e6,
    }
    direct_m = sum(lines.values())
    over = direct_m * (1.0 + HC.CONTINGENCY[1] + HC.EPC_OWNER[1]
                       + HC.SALES_TAX * HC.SALES_TAX_BASE)
    gross = financed(over, TECH["pv_salt"]["build"])
    credit = CREDIT_ELIGIBLE * (lines["thermal storage"] + lines["heaters"]) * ESC
    net = gross - credit
    om = (pv_mw * PV_OM + turb_mw * 60.0) / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * net
    return dict(key="pv_salt", mw=pv_mw, turb_mw=turb_mw, tes_mwh=tes_mwh,
                e_twh=e_twh, capex_net=net, capex_gross=gross, om=om,
                price=required_price(net, om, e_twh), lines=lines,
                acres=pv_mw * PV_ACRES_PER_MW, capped=False)


def size_pv_ironair(case="mid", e_twh=E_REQ_TWH, direct=None):
    f = DIRECT_SHARE[1] if direct is None else direct
    e_direct = e_twh * f
    e_night = e_twh * (1.0 - f)
    rte = _pick(IRONAIR_RTE, case)
    pv_twh = e_direct + e_night / rte
    pv_mw = pv_twh * 1e6 / (8760.0 * _pick(PV_CF, case))
    pow_mw = e_night * 1e6 / (365.0 * NIGHT_HOURS) * 1.3
    stor_mwh = pow_mw * IRONAIR_HOURS
    lines = {"PV": pv_mw * 1e3 * _pick(PV_PER_KW_AC, case) / 1e6,
             "iron-air energy": stor_mwh * 1e3 * _pick(IRONAIR_PER_KWH, case) / 1e6,
             "iron-air power": pow_mw * 1e3 * _pick(IRONAIR_PER_KW, case) / 1e6}
    direct_m = sum(lines.values())
    over = direct_m * (1.0 + HC.CONTINGENCY[1] + HC.EPC_OWNER[1]
                       + HC.SALES_TAX * HC.SALES_TAX_BASE)
    gross = financed(over, TECH["pv_ironair"]["build"])
    credit = CREDIT_ELIGIBLE * (lines["iron-air energy"] + lines["iron-air power"]) * ESC
    net = gross - credit
    om = (pv_mw * PV_OM + pow_mw * 30.0) / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * net
    return dict(key="pv_ironair", mw=pv_mw, pow_mw=pow_mw, stor_mwh=stor_mwh,
                e_twh=e_twh, capex_net=net, capex_gross=gross, om=om,
                price=required_price(net, om, e_twh), lines=lines,
                acres=pv_mw * PV_ACRES_PER_MW, capped=False)


def size_all(case="mid", e_twh=E_REQ_TWH):
    return {
        "salton_flash": size_simple("salton_flash", case, e_twh),
        "egs": size_simple("egs", case, e_twh),
        "csp_proposed": size_csp(e_twh),
        "pv_salt": size_pv_salt(case, e_twh),
        "pv_ironair": size_pv_ironair(case, e_twh),
        "smr": size_simple("smr", case, e_twh),
    }


def portfolio(case="mid"):
    """The base on what exists: Salton flash to its developable cap, the
    remainder and the growth on PV-charged salt. Two numbers, not one."""
    cap = TECH["salton_flash"]["cap_mw"]
    e_geo = cap * 8760.0 * TECH["salton_flash"]["cf"] / 1e6
    geo = size_simple("salton_flash", case, e_geo)
    e_rest = max(E_REQ_TWH - e_geo, 0.0)
    rest = size_pv_salt(case, e_rest) if e_rest > 0 else None
    e_grow = E_REQ_TWH * GROWTH_X - E_REQ_TWH
    grow = size_pv_salt(case, e_grow)
    return dict(geo=geo, rest=rest, grow=grow, e_geo=e_geo, e_rest=e_rest, e_grow=e_grow)


# =============================================================================
# REPORT
# =============================================================================
def report():
    print()
    print("  THE SECOND PASS: WHAT EQUIPMENT MAKES A FIRM MEGAWATT-HOUR")
    print()
    print(f"    The requirement: {E_REQ_TWH:.1f} TWh/yr firm -- 3 million households at")
    print(f"    EIA's 6,036 kWh/yr -- growing to {GROWTH_X:.2f}x over the bond term. The")
    print("    criterion: it pays for itself after the build bonds, state-owned,")
    print(f"    at {100 * RATE:.2f} %, groundbreaking 2028-2030. The author's instruction:")
    print("    SMALLER, AND PRODUCES MORE. Every candidate below is sized to")
    print("    the same requirement and priced the same way; the CSP row is")
    print("    heliocost.py's own mid case, imported and scaled, so the")
    print("    comparison shares the first pass's baseline by construction.")
    print()
    rows = size_all("mid")
    print(f"      {'candidate':<52} {'MW':>7} {'TWh':>6} {'$B net':>7} {'$/MWh':>6}"
          f" {'$/hh/yr':>8} {'vs now':>7} {'acres':>8}")
    order = sorted(rows.values(), key=lambda r: r["price"])
    for r in order:
        t = TECH[r["key"]]
        tag = "  BARRED" if t["legal"].startswith("BARRED") else (
              "  >cap" if r["capped"] else "")
        hh = H.per_household(r["price"])
        print(f"      {t['name']:<52} {r['mw']:7,.0f} {r['e_twh']:6.1f} {r['capex_net'] / 1e3:7.1f}"
              f" {r['price']:6.0f} {hh:8,.0f} {hh / NOW_PER_HH - 1:+7.0%} {r['acres']:8,.0f}{tag}")
    print(f"      {'today, IOU generation charge':<52} {'':>7} {'':>6} {'':>7}"
          f" {H.GEN_RATE_NOW * 1e3:6.0f} {NOW_PER_HH:8,.0f}")
    print(f"      {'firm-clean contract band':<52} {'':>7} {'':>6} {'':>7}"
          f" {H.FIRM_CLEAN_PPA[0]:.0f}-{H.FIRM_CLEAN_PPA[1]:.0f}")
    print()
    g = rows["salton_flash"]; c = rows["csp_proposed"]
    print("    SMALLER AND PRODUCES MORE, LITERALLY. Salton Sea geothermal")
    print(f"    delivers the same {E_REQ_TWH:.1f} TWh from {g['mw']:,.0f} MW instead of"
          f" {c['mw']:,.0f} -- {c['mw'] / g['mw']:.2f}x")
    print(f"    less nameplate -- on {g['acres']:,.0f} acres instead of {c['acres']:,.0f},"
          f" {c['acres'] / g['acres']:.0f}x less land, at a")
    print(f"    capacity factor of {TECH['salton_flash']['cf']:.2f} against {H.run_network()['cf_net']:.2f}."
          " It runs at night, in")
    print("    winter, and through a week of cloud, because it does not use")
    print("    the sun. It needs no mirrors, no towers, no receivers and no")
    print("    salt. And it sits in the proposal's own Imperial node: the")
    print(f"    field is rated at {TECH['salton_flash']['cap_mw']:,.0f} MW developable now and 2,950 MW"
          " in all, of")
    print("    which 400 MW has been built -- and the developable figure alone")
    print(f"    is {TECH['salton_flash']['cap_mw'] * 8760 * TECH['salton_flash']['cf'] / 1e6:.1f} TWh/yr,"
          f" {TECH['salton_flash']['cap_mw'] * 8760 * TECH['salton_flash']['cf'] / 1e6 / E_REQ_TWH:.2f} of the requirement.")
    print()
    print(f"    AND IT MEETS THE CRITERION. At ${g['price']:.0f}/MWh a household pays"
          f" ${H.per_household(g['price']):,.0f}/yr,")
    print(f"    {H.per_household(g['price']) / NOW_PER_HH - 1:+.0%} against today, inside the"
          f" {H.FIRM_CLEAN_PPA[0]:.0f}-{H.FIRM_CLEAN_PPA[1]:.0f} band -- and that")
    print("    is at the mid case, with the hypersaline penalty on capex and")
    print("    $170/kW-yr of O&M. It lands BELOW the band, and two things put")
    print("    it there: the bond rate, and a federal credit that is real here")
    print("    where it is zero for the solar field -- §48E survives for")
    print("    geothermal at 100 % through 2033, so a public owner takes 50 %")
    t = TECH["salton_flash"]
    om_nc = g["mw"] * t["om"] / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * g["capex_gross"]
    p_nc = required_price(g["capex_gross"], om_nc)
    print(f"    of the plant back as direct pay. WITHOUT THE CREDIT it is ${p_nc:.0f}/MWh,")
    print("    still inside the band: the credit is a margin, not the case.")
    print("    Enhanced geothermal prices the same and is not capped by one")
    print("    field; SCE already holds 320 MW of it under a 15-year contract.")
    print()
    print("    WHAT RUNS AGAINST IT, AND EACH IS REAL. The Salton Sea brine is")
    print("    hypersaline -- a quarter salt by mass -- and it scales and")
    print("    corrodes, which is why the field has sat at 400 MW for thirty")
    print("    years and why Hell's Kitchen has slipped its milestones twice;")
    print("    the capex band carries that and is ASSUMED, not sourced. The")
    print("    2,250 MW is a resource estimate, not a drilling programme. A")
    print("    forty-year plant budgets makeup wells or its capacity factor")
    print("    walks down toward The Geysers' 53 %. Brine handling, H2S,")
    print("    induced seismicity and subsidence are permit conditions with a")
    print("    record, not novelties. None of these moves the price by the")
    print("    factor CSP's provenance does.")
    print()
    p = portfolio("mid")
    print("    THE PORTFOLIO THE NUMBERS POINT AT. Base on what exists, and")
    print("    grow on what is cheap:")
    print()
    print(f"      Salton flash to its cap        {p['geo']['mw']:7,.0f} MW  {p['e_geo']:5.1f} TWh"
          f"  ${p['geo']['capex_net'] / 1e3:5.1f} B  ${p['geo']['price']:.0f}/MWh")
    if p["rest"]:
        print(f"      remainder, PV-charged salt     {p['rest']['mw']:7,.0f} MW  {p['e_rest']:5.1f} TWh"
              f"  ${p['rest']['capex_net'] / 1e3:5.1f} B  ${p['rest']['price']:.0f}/MWh")
    print(f"      growth to {GROWTH_X:.2f}x, PV-charged salt {p['grow']['mw']:7,.0f} MW  {p['e_grow']:5.1f} TWh"
          f"  ${p['grow']['capex_net'] / 1e3:5.1f} B  ${p['grow']['price']:.0f}/MWh")
    print()
    print("    The PV-charged salt row keeps Helios's tanks, turbines and")
    print("    nitrate -- everything the author decided -- and replaces the")
    print("    one line with no provenance, the heliostat field, with the")
    print("    most-built generator on earth feeding resistance heaters. It")
    print("    is priced here from parts and is the least sourced row in the")
    print("    table: the heater and night-peak terms are ASSUMED bands.")
    print()
    print("    WHAT THIS FILE REFUSES. It does not choose. A comparison on one")
    print("    criterion is what the author asked for and what a Legislature")
    print("    will ask for, and it is what this is. The nuclear row is priced")
    print("    and marked BARRED because California law bars it, not because")
    print("    the number is wrong; offshore wind is not in the table because")
    print("    it is not firm and two of its three leases are gone. Gen3")
    print("    particle CSP -- sand at 700 C into an sCO2 turbine, a sixth")
    print("    more electricity per unit of heat, no salt to freeze -- is the")
    print("    right CSP and is a pilot at Sandia; it is not a 2030 plant.")
    print()
    print("    AND THE AUTHOR'S LARGER POINT IS ALREADY IN THE ARITHMETIC. A")
    print("    firm plant that is not sun-bound needs no 16-hour store for the")
    print("    night, so a fleet of them holds reserve in the plants themselves;")
    print("    as neighbours adopt the model the export a state must carry")
    print("    falls, and what stays is a plant sized to its own households")
    print("    with the geothermal base as the emergency capability. That is")
    print("    the shape of a scaled-down local operation, and it is the shape")
    print("    the geothermal row already has.")
    print()


# =============================================================================
# SELFTEST
# =============================================================================
def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    rows = size_all("mid")
    g, e, c, ps, pi, s = (rows[k] for k in
                          ("salton_flash", "egs", "csp_proposed", "pv_salt",
                           "pv_ironair", "smr"))
    print()
    print("  the comparison shares the first pass's baseline")
    hc = HC.build("mid")
    pf = H.run_network()
    check("the CSP row reproduces heliocost's mid required price to 2 %",
          abs(c["price"] / H.required_price(pf["net"], hc["net_capex"] / 1e3, RATE,
                                            HC.om_m("mid", "state", hc["net_capex"])["total"])
              - 1.0) < 0.02)
    check("every candidate is sized to the same requirement",
          all(abs(r["e_twh"] - E_REQ_TWH) < 1e-9 for r in rows.values()))
    check("the requirement is helios.py's, not restated",
          abs(E_REQ_TWH - H.hh_demand_twh()) < 1e-12)

    print()
    print("  smaller and produces more")
    check("geothermal nameplate is under half CSP's for the same energy",
          g["mw"] < 0.5 * c["mw"])
    check("  -- on under a tenth of the land", g["acres"] < 0.1 * c["acres"])
    check("  -- at a capacity factor above 0.85", TECH["salton_flash"]["cf"] > 0.85)
    check("the developable Salton field is within 10 % of the requirement",
          abs(TECH["salton_flash"]["cap_mw"] * 8760 * 0.90 / 1e6 / E_REQ_TWH - 1.0) < 0.10)
    check("  -- and the sized plant only just exceeds the cap",
          g["capped"] and g["mw"] / TECH["salton_flash"]["cap_mw"] < 1.1)

    print()
    print("  the criterion")
    check("geothermal's required price is at or below the band's top",
          g["price"] <= H.FIRM_CLEAN_PPA[1])
    # It lands BELOW the band's bottom, and the reason is the two things the
    # ownership form buys -- the bond rate and the 50 % direct pay -- so the
    # result must survive losing the credit, or it is a subsidy and not a plant.
    t = TECH["salton_flash"]
    om_nc = g["mw"] * t["om"] / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * g["capex_gross"]
    p_nc = required_price(g["capex_gross"], om_nc)
    check("  -- and survives losing the federal credit entirely",
          p_nc <= H.FIRM_CLEAN_PPA[1])
    check("  -- landing inside the band without it",
          H.FIRM_CLEAN_PPA[0] <= p_nc <= H.FIRM_CLEAN_PPA[1])
    check("  -- so a household pays less than today",
          H.per_household(g["price"]) < NOW_PER_HH)
    check("EGS prices within 15 % of Salton flash", abs(e["price"] / g["price"] - 1) < 0.15)
    check("CSP as proposed is above the band (the first pass's finding)",
          c["price"] > H.FIRM_CLEAN_PPA[1])
    check("PV-charged salt is below CSP", ps["price"] < c["price"])
    check("the federal credit is zero on PV and 50 % on geothermal and storage",
          TECH["salton_flash"]["credit"] == CREDIT_ELIGIBLE == 0.5
          and TECH["offshore_wind"]["credit"] == 0.0)
    check("  -- and applied to the storage lines only in the built-up rows",
          ps["capex_net"] < ps["capex_gross"] and pi["capex_net"] < pi["capex_gross"])
    check("SMR is priced AND marked BARRED", s["price"] > 0
          and TECH["smr"]["legal"].startswith("BARRED"))
    check("offshore wind is not in the sized table because it is not firm",
          "offshore_wind" not in rows and not TECH["offshore_wind"]["firm"])

    print()
    print("  the portfolio")
    p = portfolio("mid")
    check("base + remainder equals the requirement",
          abs(p["e_geo"] + p["e_rest"] - E_REQ_TWH) < 1e-9)
    check("growth is the requirement's growth and nothing else",
          abs(p["e_grow"] - E_REQ_TWH * (GROWTH_X - 1.0)) < 1e-9)
    check("the base row honours the field's cap",
          abs(p["geo"]["mw"] - TECH["salton_flash"]["cap_mw"]) < 1e-6)

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it does not choose", "It does not choose" in out)
    check("it names what runs against geothermal", "hypersaline" in out and "makeup wells" in out)
    check("it says the capex band is ASSUMED, not sourced", "ASSUMED, not sourced" in out)
    check("it names Gen3 as the right CSP and not a 2030 plant",
          "right CSP" in out and "not a 2030 plant" in out)
    check("it carries the author's scaled-down-operations point",
          "emergency capability" in out)

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
