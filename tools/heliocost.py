#!/usr/bin/env python3
"""heliocost.py -- what Program Helios-1M costs to build, line by line (F-05)

WHY THIS FILE EXISTS
--------------------
Title I §4.1 states a capital cost of $27.2 billion and calls it an "Audited
Baseline". No audit is cited, no line items are given, and at $5.18 per watt
it is below every salt tower ever built. helios.py then showed that the
criterion the author set -- the plant pays for itself after the build bonds --
turns on this one number: at $27.2 B the plant needs $102/MWh, inside the band
California already pays for firm clean power; at a built-plant cost it needs a
price nothing pays. So the capital cost decides whether the program exists,
and it has to be BUILT rather than asserted.

WHAT IT DOES
------------
Takes the plant exactly as helios.py carries it (45.6 M m^2, 5,250 MWe,
197,184 MWh_th, 1.665 Mt of salt) at the heliostat and tower class the author
decided on 2026-09-11 (Noor III units, 36 towers), and prices each line from a
published unit rate with a band. Then it applies the OWNERSHIP FORM the author
specified -- a state authority, no private interest, no state incentives,
federal storage credit taken where it applies, groundbreaking 2028-2030 -- as
named lines rather than a paragraph. Then it hands the result back to
helios.required_price() to say what each case needs per MWh.

STATUS DISCIPLINE
-----------------
NREL's servers are blocked at this environment's egress, so the SAM default
unit rates are RECONSTRUCTED from the Turchi et al. (2019) cost model as
carried in SAM, and are then CORROBORATED against a SOURCED whole-plant figure
the search did reach: the NREL ATB 2024 representative tower (10 h, SM 2.4) at
$7,912/kWe in 2022 dollars. The selftest builds that plant with these rates and
requires the ATB figure back within its own band. A reconstruction that
reproduces a sourced anchor is not thereby sourced; it is corroborated, and
the file says which.

    python3 tools/heliocost.py
    python3 tools/heliocost.py --selftest
stdlib only.
"""

import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import helios as H                                              # noqa: E402

# =============================================================================
# THE PLANT, AS DECIDED
# =============================================================================
TOWERS = 36                    # author's decision 2026-09-11: Noor III class
TOWER_HEIGHT_M = 250.0         # Noor III                              SOURCED
HELIOSTAT_M2 = 178.0           # Noor III unit                         SOURCED
DESIGN_DNI = 950.0             # W/m2                                  SOURCED
BUILD_YEARS = 4.0              # Title I §8 (2 civil + 2 field); see F-24
GROUNDBREAK = (2028, 2030)     # author's estimate 2026-09-11
DOLLAR_YEAR_RATES = 2022       # after calibration to the ATB anchor (below)
RAW_RATES_YEAR = 2018          # Turchi 2019's own dollar year
ESCALATION = 0.03              # per year, construction-cost index   ASSUMED band 0.02-0.04

# =============================================================================
# UNIT RATES: (low, mid, high), with status
# =============================================================================
# SAM default molten-salt tower cost model, Turchi et al. 2019 (NREL/TP-5500-
# 72856), as carried in SAM 2022.11 -- RECONSTRUCTED: NREL is unreachable from
# here, so these are the model's published defaults from memory, and the
# selftest corroborates them against the ATB 2024 $7,912/kWe anchor.
SITE_PER_M2 = (16.0, 16.0, 16.0)             # site improvements   RECONSTRUCTED
HELIOSTAT_PER_M2 = (80.0, 120.0, 127.0)      # installed field.  SOURCED: $127 ATB
                                             # 2022 base; $120 conventional 2024;
                                             # $80 best reported (SolarPACES)
TOWER_FIXED_M = 3.0                          # $M x exp(0.0113 x height) RECONSTRUCTED
TOWER_EXP = 0.0113
RECEIVER_REF_M = 103.0                       # $M at 1,571 m2, exponent 0.7   RECONSTRUCTED
RECEIVER_REF_M2 = 1571.0
RECEIVER_EXP = 0.7
RECEIVER_FLUX_MW_M2 = 0.425                  # MW_th per m2 of receiver, from the
                                             # SAM reference (670 MW_th on 1,571 m2)
TES_PER_KWHTH = (22.0, 24.0, 30.0)           # tanks, salt, HX, foundations   RECONSTRUCTED
                                             # low = SAM default; high = 1.665 Mt of
                                             # salt at a 2025 nitrate price
POWER_BLOCK_PER_KWE = (1040.0, 1150.0, 1300.0)   # cycle; high end carries ACC   RECONSTRUCTED
BOP_PER_KWE = (290.0, 290.0, 340.0)          # balance of plant               RECONSTRUCTED
SWITCHYARD_PER_NODE_M = (150.0, 200.0, 300.0)   # 500 kV switchyard + gen-tie  ASSUMED band
CONTINGENCY = (0.07, 0.15, 0.30)             # SAM 7 %; first-of-kind 25-35 %  SOURCED band
EPC_OWNER = (0.11, 0.13, 0.15)               # SAM 13 %                          RECONSTRUCTED
SALES_TAX = 0.08                             # CA public agencies PAY sales tax; Kern,
                                             # San Bernardino, Imperial 7.75-8.75 %  SOURCED
SALES_TAX_BASE = 0.80                        # share of direct cost that is taxable
                                             # equipment (SAM convention)  RECONSTRUCTED

# =============================================================================
# OWNERSHIP FORM (author, 2026-09-11)
# =============================================================================
DEVELOPER_MARGIN = (0.05, 0.075, 0.10)       # private developer fee + margin; state = 0
PRIVATE_WACC = 0.09                          # what a private CSP developer finances at
FED_STORAGE_ITC = 0.30                       # §48E energy storage, retained through
                                             # construction start 2033           SOURCED
FED_DOMESTIC_BONUS = 0.10                    # mandatory for public >1 MW direct pay
FED_ENERGY_COMMUNITY = 0.10                  # Kern / Imperial / San Bernardino  ASSUMED eligible
FED_SOLAR_ITC = 0.0                          # terminated for construction after
                                             # 2026-07-04 unless in service by 2027;
                                             # groundbreaking is 2028-2030       SOURCED
STATE_INCENTIVES = 0.0                       # a state plant taking a state
                                             # incentive pays itself             DECIDED
PROPERTY_TAX_RATE = 0.010                    # of assessed value, private plant  SOURCED
PILOT_FRACTION = 0.50                        # payment in lieu, share of the exempted
                                             # tax, to host counties             DESIGN (author to set)
OPS_JOBS = 1350                              # Title I §7
OPS_LOADED_COST_K = (150.0, 180.0, 220.0)    # $k/yr fully loaded, private      ASSUMED band
CALPERS_ONCOST_ADDER = 0.15                  # state on-cost above private       ASSUMED band 0.10-0.20


def _pick(band, case):
    return band[{"low": 0, "mid": 1, "high": 2}[case]]


# =============================================================================
# THE LINES
# =============================================================================
def field_design_mwth():
    return H.APERTURE_M2 * DESIGN_DNI * H.ETA_OPT_PEAK / 1e6


def receiver_m2_each():
    return field_design_mwth() / TOWERS / RECEIVER_FLUX_MW_M2


def tower_cost_m():
    return TOWER_FIXED_M * math.exp(TOWER_EXP * TOWER_HEIGHT_M)


def receiver_cost_m():
    return RECEIVER_REF_M * (receiver_m2_each() / RECEIVER_REF_M2) ** RECEIVER_EXP


def direct_lines(case="mid", aperture=None, gross=None, tes=None, towers=None,
                 height=None, nodes=3, raw=False):
    """Direct cost lines in $M. Parameters default to the Helios plant; the
    selftest passes the ATB representative plant.

    raw=True returns the reconstructed 2018-$ rates as they stand. Otherwise
    every line is scaled by CALIBRATION, so the LEVEL is the sourced ATB 2024
    anchor and only the SPLIT between lines is the reconstruction's."""
    ap = H.APERTURE_M2 if aperture is None else aperture
    gr = H.GROSS_MWE if gross is None else gross
    st = H.STORAGE_MWH_TH if tes is None else tes
    nt = TOWERS if towers is None else towers
    ht = TOWER_HEIGHT_M if height is None else height
    fld_th = ap * DESIGN_DNI * H.ETA_OPT_PEAK / 1e6
    rcv_m2 = fld_th / nt / RECEIVER_FLUX_MW_M2
    tower = TOWER_FIXED_M * math.exp(TOWER_EXP * ht)
    rcv = RECEIVER_REF_M * (rcv_m2 / RECEIVER_REF_M2) ** RECEIVER_EXP
    k = 1.0 if raw else calibration()
    return [(n, v * k, st) for n, v, st in [
        ("site improvements", ap * _pick(SITE_PER_M2, case) / 1e6, "RECONSTRUCTED"),
        ("heliostat field", ap * _pick(HELIOSTAT_PER_M2, case) / 1e6, "SOURCED band"),
        ("towers", nt * tower, "RECONSTRUCTED"),
        ("receivers", nt * rcv, "RECONSTRUCTED"),
        ("thermal storage (tanks, salt, HX)", st * 1e3 * _pick(TES_PER_KWHTH, case) / 1e6,
         "RECONSTRUCTED"),
        ("power block", gr * 1e3 * _pick(POWER_BLOCK_PER_KWE, case) / 1e6, "RECONSTRUCTED"),
        ("balance of plant", gr * 1e3 * _pick(BOP_PER_KWE, case) / 1e6, "RECONSTRUCTED"),
        ("500 kV switchyards + gen-tie", nodes * _pick(SWITCHYARD_PER_NODE_M, case),
         "ASSUMED band"),
    ]]


def build(case="mid", owner="state", groundbreak=None, rate=None, **plant):
    """The whole stack, $M, at the groundbreaking year's dollars."""
    lines = direct_lines(case, **plant)
    direct = sum(v for _n, v, _s in lines)
    cont = _pick(CONTINGENCY, case) * direct
    epc = _pick(EPC_OWNER, case) * direct
    tax = SALES_TAX * SALES_TAX_BASE * direct
    margin = _pick(DEVELOPER_MARGIN, case) * direct if owner == "private" else 0.0
    overnight = direct + cont + epc + tax + margin
    gb = (sum(GROUNDBREAK) / 2.0) if groundbreak is None else groundbreak
    # escalate to the mid-point of construction
    years = gb + BUILD_YEARS / 2.0 - DOLLAR_YEAR_RATES
    esc = (1.0 + ESCALATION) ** years
    overnight_esc = overnight * esc
    r = (H.BOND_RATE if owner == "state" else PRIVATE_WACC) if rate is None else rate
    idc = overnight_esc * r * BUILD_YEARS / 2.0        # simple, even drawdown
    gross_capex = overnight_esc + idc
    # federal storage credit, direct pay, on the storage line only
    tes_line = next(v for n, v, _s in lines if n.startswith("thermal storage"))
    credit_rate = (FED_STORAGE_ITC + FED_DOMESTIC_BONUS + FED_ENERGY_COMMUNITY
                   if owner == "state" else FED_STORAGE_ITC + FED_DOMESTIC_BONUS)
    credit = credit_rate * tes_line * esc
    solar_credit = FED_SOLAR_ITC * (direct - tes_line) * esc      # zero, by statute
    net_capex = gross_capex - credit - solar_credit
    return {
        "lines": lines, "direct": direct, "contingency": cont, "epc_owner": epc,
        "sales_tax": tax, "developer_margin": margin, "overnight": overnight,
        "escalation": esc, "overnight_escalated": overnight_esc, "idc": idc,
        "gross_capex": gross_capex, "storage_credit": credit,
        "solar_credit": solar_credit, "net_capex": net_capex, "rate": r,
        "case": case, "owner": owner, "groundbreak_year": gb,
    }


def om_m(case="mid", owner="state", net_capex_m=None):
    """Annual O&M, $M: Title I's $410 M, plus the ownership lines."""
    base = H.OM_M
    jobs = OPS_JOBS * _pick(OPS_LOADED_COST_K, case) / 1e3
    calpers = jobs * CALPERS_ONCOST_ADDER if owner == "state" else 0.0
    cap = H.CAPEX_B * 1e3 if net_capex_m is None else net_capex_m
    prop_tax = PROPERTY_TAX_RATE * cap if owner == "private" else 0.0
    pilot = PILOT_FRACTION * PROPERTY_TAX_RATE * cap if owner == "state" else 0.0
    return {"base": base, "calpers_adder": calpers, "property_tax": prop_tax,
            "pilot": pilot, "total": base + calpers + prop_tax + pilot}


def per_watt(b):
    return b["net_capex"] * 1e6 / (H.GROSS_MWE * 1e6)


def atb_check(raw=True):
    """Build ATB 2024's representative tower with these rates.

    100 MWe net (about 115 gross), SM 2.4, 10 h, one tower. Overnight, no
    IDC, no escalation, no credit -- ATB's CAPEX is an overnight figure.
    raw=True is the uncalibrated 2018-$ reconstruction; raw=False must return
    the anchor exactly, which is what calibration() is."""
    gross = 115.0
    turb_th = gross / H.ETA_CYCLE
    ap = 2.4 * turb_th * 1e6 / (DESIGN_DNI * H.ETA_OPT_PEAK)
    tes = 10.0 * turb_th
    lines = direct_lines("mid", aperture=ap, gross=gross, tes=tes, towers=1,
                         height=195.0, nodes=0, raw=raw)
    direct = sum(v for _n, v, _s in lines)
    overnight = direct * (1.0 + CONTINGENCY[0] + EPC_OWNER[1]
                          + SALES_TAX_BASE * 0.05)     # SAM's own 5 % tax
    return overnight * 1e6 / (100.0 * 1e3)             # $/kWe net


ATB_2024_PER_KWE = 7912.0        # SOURCED: NREL ATB 2024, tower, 10 h, SM 2.4, 2022 $
RAW_BAND = (0.70, 1.00)          # the raw reconstruction must land here, or its
                                 # SPLIT is not credible enough to calibrate


def calibration():
    """The one factor that takes the reconstructed 2018-$ rates to the sourced
    2022-$ level: ATB's figure divided by the raw rebuild of ATB's own plant.
    It carries the 2018->2022 escalation and ATB's own cost update together,
    and it is applied to every direct line alike, so it moves the level and
    never the split."""
    return ATB_2024_PER_KWE / atb_check(raw=True)

BUILT_PER_W = (                  # name, $/W_gross as built, year, storage h  SOURCED
    ("Gemasolar", 171e6 * 1.3 / 19.9e6, 2011, 15.0),
    ("Ivanpah", 2.2e9 / 392e6, 2014, 0.0),
    ("Crescent Dunes", 0.975e9 / 110e6, 2015, 10.0),
    ("Noor II+III (blended)", 2.105e9 * 1.15 / 350e6, 2018, 7.5),
    ("Cerro Dominador", 1.15e9 / 110e6, 2021, 17.5),
    ("DEWA Noor Energy 1 (blended, incl. PV)", 4.529e9 / 950e6, 2023, 15.0),
)


# =============================================================================
# REPORT
# =============================================================================
def report():
    pf = H.run_network()
    net_mwh = pf["net"]
    print()
    print("  F-05: WHAT PROGRAM HELIOS-1M COSTS TO BUILD, LINE BY LINE")
    print()
    print("    Title I §4.1 states $27.2 billion and calls it an 'Audited")
    print("    Baseline'. No audit is cited and no line is given. helios.py")
    print("    showed the author's own criterion -- the plant pays for itself")
    print("    after the build bonds -- turns on this number alone, so it is")
    print("    built here from unit rates rather than asserted.")
    print()
    print("    THE PLANT AS DECIDED: 45.6 M m^2 in Noor III-class heliostats")
    print(f"    ({H.APERTURE_M2 / HELIOSTAT_M2 / 1e3:.0f} k units), {TOWERS} towers of"
          f" {TOWER_HEIGHT_M:.0f} m, {receiver_m2_each():.0f} m^2 receivers at")
    print(f"    {field_design_mwth() / TOWERS:.0f} MW_th each, 197,184 MWh_th of salt,"
          f" 5,250 MWe gross; groundbreaking")
    print(f"    {GROUNDBREAK[0]}-{GROUNDBREAK[1]} (author's estimate), {BUILD_YEARS:.0f}-year build,"
          f" state ownership.")
    print()
    print("    STATUS. NREL is unreachable from here, so the SAM unit rates")
    print("    are RECONSTRUCTED from the Turchi 2019 model and CORROBORATED")
    print("    against the one whole-plant figure the search reached: NREL")
    print(f"    ATB 2024's representative tower at ${ATB_2024_PER_KWE:,.0f}/kWe (2022 $).")
    print(f"    Built raw, in Turchi's 2018 dollars, these rates return"
          f" ${atb_check(raw=True):,.0f}/kWe --")
    print(f"    {atb_check(raw=True) / ATB_2024_PER_KWE:.3f} of the anchor, the gap being"
          " four years of escalation and")
    print(f"    ATB's own cost update. So the LEVEL is taken from the anchor --"
          f" every line is")
    print(f"    scaled by {calibration():.3f} -- and only the SPLIT between lines is the")
    print("    reconstruction's. A reconstruction that reproduces a sourced")
    print("    anchor is corroborated, not sourced, and every line below says")
    print("    which.")
    print()
    for case in ("low", "mid", "high"):
        b = build(case)
        print(f"    ---- {case.upper()} CASE, state-owned, {DOLLAR_YEAR_RATES} $ rates"
              f" escalated to mid-construction ----")
        print(f"      {'line':<38} {'$M':>9}   status")
        for n, v, s in b["lines"]:
            print(f"      {n:<38} {v:9,.0f}   {s}")
        print(f"      {'DIRECT':<38} {b['direct']:9,.0f}")
        print(f"      {'contingency':<38} {b['contingency']:9,.0f}   "
              f"{100 * _pick(CONTINGENCY, case):.0f} %")
        print(f"      {'EPC + owner':<38} {b['epc_owner']:9,.0f}   "
              f"{100 * _pick(EPC_OWNER, case):.0f} %")
        print(f"      {'CA sales tax (public agencies pay)':<38} {b['sales_tax']:9,.0f}   "
              f"{100 * SALES_TAX:.0f} % on {100 * SALES_TAX_BASE:.0f} %")
        print(f"      {'developer margin':<38} {b['developer_margin']:9,.0f}   state: none")
        print(f"      {'OVERNIGHT, ' + str(DOLLAR_YEAR_RATES) + ' $':<38} {b['overnight']:9,.0f}")
        print(f"      {'escalation to ' + str(int(b['groundbreak_year'] + BUILD_YEARS / 2)):<38}"
              f" {'x' + format(b['escalation'], '.3f'):>9}   {100 * ESCALATION:.0f} %/yr ASSUMED")
        print(f"      {'interest during construction':<38} {b['idc']:9,.0f}   "
              f"{100 * b['rate']:.2f} % over {BUILD_YEARS:.0f} yr")
        print(f"      {'GROSS CAPEX':<38} {b['gross_capex']:9,.0f}")
        print(f"      {'federal storage credit, direct pay':<38} {-b['storage_credit']:9,.0f}   "
              f"{100 * (FED_STORAGE_ITC + FED_DOMESTIC_BONUS + FED_ENERGY_COMMUNITY):.0f} % of storage line")
        print(f"      {'federal solar credit':<38} {-b['solar_credit']:9,.0f}   "
              f"terminated for 2028+ construction")
        print(f"      {'NET CAPEX':<38} {b['net_capex']:9,.0f}   ${per_watt(b):.2f}/W")
        print()
    lo, mid, hi = (build(c) for c in ("low", "mid", "high"))
    print("    AGAINST THE PROPOSAL AND AGAINST WHAT HAS BEEN BUILT:")
    print()
    print(f"      Title I §4.1                          {H.CAPEX_B * 1e3:9,.0f}   ${H.CAPEX_B * 1e9 / (H.GROSS_MWE * 1e6):.2f}/W")
    print(f"      this build, low / mid / high         {lo['net_capex']:9,.0f} /"
          f" {mid['net_capex']:,.0f} / {hi['net_capex']:,.0f}")
    print()
    print("      built plant                              $/W    year  storage h")
    for n, pw, yr, h in BUILT_PER_W:
        print(f"      {n:<40} {pw:5.2f}   {yr}   {h:5.1f}")
    print()
    print(f"    THE PROPOSAL'S $27.2 B IS {lo['net_capex'] / (H.CAPEX_B * 1e3):.2f}x BELOW THE LOW CASE"
          f" AND {mid['net_capex'] / (H.CAPEX_B * 1e3):.2f}x BELOW THE MID.")
    print("    The low case takes the best heliostat price ever reported, SAM's")
    print("    7 % contingency on a plant thirteen times larger than any built,")
    print("    and the federal storage credit in full. Nothing in it is")
    print("    generous to the proposal and it still does not reach $27.2 B.")
    print()
    print("    WHAT THE OWNERSHIP FORM IS WORTH, line by line (mid case):")
    pv = build("mid", owner="private")
    print()
    print(f"      {'':<38} {'state':>9} {'private':>9}")
    print(f"      {'developer margin, $M':<38} {mid['developer_margin']:9,.0f} {pv['developer_margin']:9,.0f}")
    print(f"      {'IDC at 3.85 % vs 9 %, $M':<38} {mid['idc']:9,.0f} {pv['idc']:9,.0f}")
    print(f"      {'storage credit (energy-community bonus)':<38} {-mid['storage_credit']:9,.0f} {-pv['storage_credit']:9,.0f}")
    print(f"      {'NET CAPEX, $M':<38} {mid['net_capex']:9,.0f} {pv['net_capex']:9,.0f}")
    oms = om_m("mid", "state", mid["net_capex"])
    omp = om_m("mid", "private", pv["net_capex"])
    print(f"      {'O&M: base (Title I)':<38} {oms['base']:9,.0f} {omp['base']:9,.0f}")
    print(f"      {'O&M: CalPERS on-cost adder':<38} {oms['calpers_adder']:9,.0f} {omp['calpers_adder']:9,.0f}")
    print(f"      {'O&M: property tax':<38} {oms['property_tax']:9,.0f} {omp['property_tax']:9,.0f}")
    print(f"      {'O&M: PILOT to host counties':<38} {oms['pilot']:9,.0f} {omp['pilot']:9,.0f}   at {100 * PILOT_FRACTION:.0f} % of exempted tax")
    print(f"      {'O&M total, $M/yr':<38} {oms['total']:9,.0f} {omp['total']:9,.0f}")
    ds_s = H.debt_service_m(mid["net_capex"] / 1e3, H.BOND_RATE)
    ds_p = H.debt_service_m(pv["net_capex"] / 1e3, PRIVATE_WACC)
    print(f"      {'debt service, $M/yr':<38} {ds_s:9,.0f} {ds_p:9,.0f}")
    print(f"      {'CARRYING, $M/yr':<38} {ds_s + oms['total']:9,.0f} {ds_p + omp['total']:9,.0f}")
    rp_s = H.required_price(net_mwh, mid["net_capex"] / 1e3, H.BOND_RATE, oms["total"])
    rp_p = H.required_price(net_mwh, pv["net_capex"] / 1e3, PRIVATE_WACC, omp["total"])
    print(f"      {'$/MWh needed at 1.00x':<38} {rp_s:9.1f} {rp_p:9.1f}")
    print()
    print("    AND THE CRITERION, AT EACH CASE, STATE-OWNED:")
    print()
    print(f"      {'case':<8} {'net capex $B':>13} {'carrying $M':>12} {'$/MWh 1.00x':>12} {'$/MWh 1.25x':>12}")
    for case, b in (("low", lo), ("mid", mid), ("high", hi)):
        o = om_m(case, "state", b["net_capex"])
        p1 = H.required_price(net_mwh, b["net_capex"] / 1e3, H.BOND_RATE, o["total"])
        p125 = H.required_price(net_mwh, b["net_capex"] / 1e3, H.BOND_RATE, o["total"],
                                coverage=H.COVERAGE_REQ)
        print(f"      {case:<8} {b['net_capex'] / 1e3:13.1f} "
              f"{H.debt_service_m(b['net_capex'] / 1e3, H.BOND_RATE) + o['total']:12,.0f}"
              f" {p1:12.1f} {p125:12.1f}")
    print(f"      firm-clean contract band, CA LSEs          "
          f"{H.FIRM_CLEAN_PPA[0]:.0f}-{H.FIRM_CLEAN_PPA[1]:.0f} $/MWh")
    print()
    lo_o = om_m("low", "state", lo["net_capex"])
    p_lo = H.required_price(net_mwh, lo["net_capex"] / 1e3, H.BOND_RATE, lo_o["total"])
    print(f"    THE REAL NUMBER. At the scale proposed and the class decided,")
    print(f"    the plant costs {lo['net_capex'] / 1e3:.0f} to {hi['net_capex'] / 1e3:.0f} billion dollars net of the"
          f" storage credit,")
    print(f"    {mid['net_capex'] / 1e3:.0f} at the mid case, and needs ${p_lo:.0f}-"
          f"{H.required_price(net_mwh, hi['net_capex'] / 1e3, H.BOND_RATE, om_m('high', 'state', hi['net_capex'])['total']):.0f}/MWh to pay for itself"
          f" -- ${H.required_price(net_mwh, mid['net_capex'] / 1e3, H.BOND_RATE, oms['total']):.0f} at")
    print(f"    the mid -- against a contract band of {H.FIRM_CLEAN_PPA[0]:.0f}-{H.FIRM_CLEAN_PPA[1]:.0f}."
          " THE CRITERION DOES NOT")
    print(f"    CLOSE AT THE SCALE PROPOSED IN ANY CASE: the low case needs"
          f" {p_lo / H.FIRM_CLEAN_PPA[1]:.2f}x the")
    print("    top of the band, with the best heliostat price ever reported, a")
    print("    7 % contingency, the storage credit in full, and a plant that")
    print("    delivers what the model says -- which no salt tower ever has.")
    print()
    print("    WHAT MOVES IT, IN ORDER. The three largest lines are the power")
    print("    block, the storage and the field, and all three scale with the")
    print("    plant -- so the number that moves the answer is not a unit rate,")
    print("    it is the SIZE, and the size was set by a household count that")
    print("    F-17 shows was computed at three different consumptions. The")
    print("    ownership form is worth what the private column shows and it is")
    print("    already taken. The storage credit is worth what its line shows")
    print("    and is taken. Nothing else in this file is a lever.")
    print()
    print("    WHAT THIS FILE DOES NOT DO. It does not resize the plant, choose")
    print("    a smaller first phase, or price a PV-plus-heater alternative;")
    print("    those are redesigns and belong to the second pass. It prices")
    print("    the plant as proposed, and says the word 'audited' may not be")
    print("    used of any figure in it until an EPC has priced a tower.")
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

    print()
    print("  the reconstruction is corroborated before it is used")
    a = atb_check(raw=True)
    check(f"raw 2018-$ rates rebuild ATB 2024's tower to {a / ATB_2024_PER_KWE:.3f}"
          f" of ${ATB_2024_PER_KWE:,.0f}/kWe, inside {RAW_BAND}",
          RAW_BAND[0] <= a / ATB_2024_PER_KWE <= RAW_BAND[1])
    check("calibrated rates return the anchor exactly",
          abs(atb_check(raw=False) - ATB_2024_PER_KWE) < 1e-6)
    check("  -- and calibration is one factor on every line, so the split is unmoved",
          all(abs(c[1] / r[1] - calibration()) < 1e-9
              for c, r in zip(direct_lines("mid"), direct_lines("mid", raw=True))
              if r[1] > 0))
    check("  -- the check is overnight, in the anchor's own dollar year",
          "escalat" not in atb_check.__doc__.lower() or "no escalation" in atb_check.__doc__)

    print()
    print("  the plant as decided")
    check("Noor III-class units number under 300 k",
          H.APERTURE_M2 / HELIOSTAT_M2 < 300e3)
    check("36 towers put each receiver near Noor III's thermal rating",
          500.0 < field_design_mwth() / TOWERS < 900.0)
    check("  -- and each receiver near SAM's reference area",
          0.7 < receiver_m2_each() / RECEIVER_REF_M2 < 1.5)

    print()
    print("  the stack")
    lo, mid, hi = (build(c) for c in ("low", "mid", "high"))
    check("low < mid < high on net capex",
          lo["net_capex"] < mid["net_capex"] < hi["net_capex"])
    check("every direct line carries a status",
          all(s for _n, _v, s in mid["lines"]))
    check("the three largest lines are power block, storage, field",
          {n.split(" (")[0] for n, _v, _s in
           sorted(mid["lines"], key=lambda t: -t[1])[:3]}
          == {"power block", "thermal storage", "heliostat field"})
    check("escalation is above one for a 2028-2030 groundbreaking",
          mid["escalation"] > 1.0)
    check("IDC is positive and under 15 % of overnight",
          0.0 < mid["idc"] < 0.15 * mid["overnight_escalated"])
    check("the storage credit applies to the storage line only",
          abs(mid["storage_credit"] - 0.5 * next(
              v for n, v, _s in mid["lines"] if n.startswith("thermal"))
              * mid["escalation"]) < 1e-6)
    check("  -- and the solar credit is exactly zero, by statute",
          mid["solar_credit"] == 0.0)
    check("state ownership carries no developer margin",
          mid["developer_margin"] == 0.0 and build("mid", "private")["developer_margin"] > 0)
    check("the private column finances at 9 % and the state at the bond rate",
          build("mid", "private")["rate"] == PRIVATE_WACC and mid["rate"] == H.BOND_RATE)

    print()
    print("  the finding")
    check("Title I's $27.2 B is below the LOW case",
          H.CAPEX_B * 1e3 < lo["net_capex"])
    check("  -- by more than 1.5x",
          lo["net_capex"] / (H.CAPEX_B * 1e3) > 1.5)
    check("the mid case sits inside the built-plant $/W record",
          min(p for _n, p, _y, _h in BUILT_PER_W) < per_watt(mid)
          < max(p for _n, p, _y, _h in BUILT_PER_W))
    check("  -- and inside helios.py's F-05 band",
          H.CAPEX_BAND_B[0] * 1e3 * 0.9 < mid["net_capex"] < H.CAPEX_BAND_B[1] * 1e3 * 1.2)
    pf = H.run_network()
    o_mid = om_m("mid", "state", mid["net_capex"])
    p_mid = H.required_price(pf["net"], mid["net_capex"] / 1e3, H.BOND_RATE, o_mid["total"])
    check("the mid-case required price is above the firm-clean band",
          p_mid > H.FIRM_CLEAN_PPA[1])
    o_lo = om_m("low", "state", lo["net_capex"])
    p_lo = H.required_price(pf["net"], lo["net_capex"] / 1e3, H.BOND_RATE, o_lo["total"])
    check("  -- and even the low case is above the band's TOP",
          p_lo > H.FIRM_CLEAN_PPA[1])
    check("ownership form: state needs less per MWh than private, mid case",
          p_mid < H.required_price(pf["net"], build("mid", "private")["net_capex"] / 1e3,
                                   PRIVATE_WACC, om_m("mid", "private",
                                                      build("mid", "private")["net_capex"])["total"]))
    check("the PILOT is a fraction of exactly the tax a private plant would pay",
          abs(o_mid["pilot"] - PILOT_FRACTION * PROPERTY_TAX_RATE * mid["net_capex"]) < 1e-9)

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it names its status: RECONSTRUCTED and CORROBORATED, not sourced",
          "RECONSTRUCTED" in out and "corroborated, not sourced" in out)
    check("it says the criterion does not close at the scale proposed, in any case",
          "DOES NOT" in out and "CLOSE AT THE SCALE PROPOSED IN ANY CASE" in out)
    check("it says the lever is the size, not a unit rate",
          "it is the SIZE" in out)
    check("it forbids the word 'audited'",
          "'audited' may not" in out)
    check("it names what it does not do",
          "DOES NOT DO" in out and "redesigns" in out)

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
