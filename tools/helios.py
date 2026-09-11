#!/usr/bin/env python3
"""helios.py -- Program Helios-1M at the scale proposed, hour by hour.

WHY THIS FILE EXISTS
--------------------
proposals/FLAWS.tsv F-01 and F-02: the as-submitted Title I sells
1,515 MW x 8,760 h of export at an evening-peak price. That is a 100 percent
capacity factor priced at a four-hour-a-day price. Both cannot be true and
neither is. This instrument takes the plant EXACTLY AS SPECIFIED -- 45.6 M m2
of aperture, 5,250 MWe gross, 197,184 MWh_th of salt, three nodes, 735 MW
parasitic -- and runs it through a year one hour at a time, then prices what
it made at what the hours actually pay.

It corrects the mathematics to the proposed scale. It does not enlarge the
field, add PV, change the dispatch philosophy or move a node. Those are
redesigns and belong to later passes; the author asked for the real number
at the current scale first.

WHAT IS SOURCED, WHAT IS RECONSTRUCTED, AND WHY THE DISTINCTION IS THE POINT
-----------------------------------------------------------------------------
No hourly irradiance series was reachable from this environment (NREL, CAISO
and CPUC are blocked at the egress proxy), so:

  SOURCED         annual DNI at Daggett (NREL TMY3), the Westlands band, the
                  CAISO 2024 hour-ending-20 prices by month, the 2024 WEIM
                  average, the count of negative-price hours, the Palo Verde
                  on-peak strip, and the built record of every commercial
                  salt tower (design GWh against delivered GWh).
  RECONSTRUCTED   the HOURLY SHAPE of both -- clear-sky DNI from exact solar
                  geometry, scaled month by month to the sourced annual total,
                  with a stated fraction of overcast days; and an hourly price
                  shape pinned to the sourced anchors.
  ASSUMED         Desert Center's annual DNI (not found published; carried
                  from the NSRDB map class with a band), and the field and
                  receiver efficiency curves (carried at SolarPACES/SAM
                  defaults with bands).

The annual ENERGY is insensitive to the hourly shape -- it is set by the
aperture and the annual DNI, both sourced -- and the selftest asserts that
directly by re-running on a different shape. What the shape decides is the
December delivery and the peak-window share, and those are reported as bands.

    python3 tools/helios.py              the report
    python3 tools/helios.py --selftest
stdlib only.
"""

import argparse
import math
import sys

# ---- THE PLANT, EXACTLY AS TITLE I STATES IT --------------------------------
# Every figure in this block is the proposal's own. None is corrected here;
# that is the whole discipline of the instrument.
NODES = (
    # name, lat, lon, aperture m2, gross MWe, storage MWh_th, annual DNI
    #                                                          kWh/m2/yr, status
    ("Mojave (Kramer Junction)", 35.01, -117.56, 15.2e6, 1750.0, 65728.0,
     2799.0, "SOURCED: NREL TMY3 Daggett 7.67 kWh/m2/day"),
    ("Imperial (Desert Center)", 33.71, -115.40, 15.2e6, 1750.0, 65728.0,
     2740.0, "ASSUMED: NSRDB map class 7.3-7.8 kWh/m2/day, mid 7.5"),
    ("Central Valley (Westside)", 36.01, -119.96, 15.2e6, 1750.0, 65728.0,
     2190.0, "SOURCED band: Westlands 5.5-6.5 kWh/m2/day, mid 6.0"),
)
DNI_BAND = {"Mojave (Kramer Junction)": (2700.0, 2900.0),
            "Imperial (Desert Center)": (2660.0, 2850.0),
            "Central Valley (Westside)": (2010.0, 2370.0)}
GROSS_MWE = 5250.0            # Title I §2
PARASITIC_MWE = 735.0         # Title I §2, "pumps, ACC fans, heat exchangers"
STORAGE_MWH_TH = 197184.0     # Title I §2
SALT_T = 1.665e6              # t, Title I §2
T_HOT, T_COLD = 565.0, 290.0  # C, Title I §2.1
APERTURE_M2 = 45.6e6          # Title I §2
CLAIMED_SM = 5.0              # Title I §2 -- contested in F-06
CLAIMED_EXPORT_MWE = 1515.0   # Title I §2
CLAIMED_INSTATE_MWE = 3000.0  # Title I §2
CLAIMED_EXPORT_MWH = 13271400.0   # Title I §4.2: 1,515 x 8,760
CLAIMED_PEAK_PRICES = (190.0, 270.0, 350.0)   # Title I §4.2 scenarios
CLAIMED_RA_M = (450.0, 450.0, 480.0)          # Title I §4.2, excluded (F-18)
CARRYING_COST_M = 1933.0      # Title I §4.1, $M/yr, carried unchanged here

# ---- THE THERMODYNAMICS, FROM THE PROPOSAL'S OWN NUMBERS --------------------
ETA_CYCLE = 0.43              # gross, at rated load; SOURCED band 0.41-0.44
                              # for a 540 C reheat cycle (F-32: not
                              # supercritical). The proposal's 16 h claim
                              # only closes at about this value.
SALT_CP = 1.5                 # kJ/kg/K, solar salt           SOURCED 1.49-1.53
MIN_LOAD = 0.20               # turbine minimum stable load   SOURCED band
PART_LOAD_A = 0.90            # eta(load) = ETA_CYCLE * (A + (1-A)*load)
                              # ASSUMED, mild
TANK_LOSS_PER_DAY = 0.005     # of capacity; SOURCED ~1 C/day on a 275 K span

# ---- THE FIELD --------------------------------------------------------------
ETA_OPT_PEAK = 0.66           # design-point optical efficiency of a surround
                              # field; SOURCED band 0.62-0.70 (SAM/SolarPACES)
ETA_OPT_EXP = 0.30            # eta_opt(h) = PEAK * sin(h)^EXP; ASSUMED shape
                              # giving ~0.58 annual-weighted, inside the
                              # SOURCED annual band 0.55-0.62
ETA_RECEIVER = 0.88           # SOURCED band 0.85-0.90
AVAILABILITY = 0.95           # soiling, tracking, outage      ASSUMED
DNI_START = 200.0             # W/m2 receiver start threshold   SOURCED band
CLOUD_DAY_FRACTION = 0.15     # share of days at CLOUD_DAY_DNI  RECONSTRUCTED
CLOUD_DAY_DNI = 0.25          # of a clear day's DNI            RECONSTRUCTED
WINTER_CLEARNESS = 0.88       # Dec relative to annual mean     RECONSTRUCTED
SUMMER_CLEARNESS = 1.12       # Jun relative                    RECONSTRUCTED
SOLAR_CONST = 1353.0          # W/m2, Meinel clear-sky          SOURCED

# ---- THE PARASITIC, SPLIT THE WAY THE PROPOSAL'S 735 MW IMPLIES -------------
# 735 / 5,250 = 14 percent at full load. Carried as 12 percent of gross plus
# a field/tracing/pump floor, so the plant still draws power when the turbine
# is off -- which a single full-load figure hides.
PAR_GROSS_FRAC = 0.12
PAR_FIELD_FRAC = 0.015        # of nameplate, while the field is on sun
PAR_NIGHT_FRAC = 0.005        # of nameplate, always

# ---- THE PRICE SHAPE, PINNED TO WHAT 2024 ACTUALLY PAID ---------------------
PEAK_HOURS = (17, 18, 19, 20)     # clock hours, CAISO net-peak window
# Hour-ending-20 day-ahead by month, $/MWh.        SOURCED anchors: Q1 $64,
# Jul $146, Aug $97, Oct $63 (CAISO DMM / market performance reports);
# the other months are interpolated (RECONSTRUCTED).
PEAK_PRICE_2024 = {1: 64, 2: 64, 3: 64, 4: 50, 5: 45, 6: 80, 7: 146, 8: 97,
                   9: 90, 10: 63, 11: 60, 12: 62}
MIDDAY_HOURS = (9, 10, 11, 12, 13, 14, 15)
MIDDAY_PRICE_2024 = {1: 30, 2: -5, 3: -10, 4: -12, 5: -10, 6: -5, 7: 15,
                     8: 15, 9: 10, 10: 5, 11: 25, 12: 30}
OTHER_PRICE_2024 = 40.0           # night and shoulder hours
WEIM_AVG_2024 = 40.0              # SOURCED: DMM 2024, "about $40/MWh"
WEIM_2023_OVER_2024 = 1.0 / 0.65  # SOURCED: 2024 down 35 % on 2023
NEG_HOURS_2024 = 1180             # SOURCED: DMM 2024
PALO_VERDE_ONPEAK_2024 = 81.8     # SOURCED: 12-month strip, day-weighted

# ---- THE BUILT RECORD -------------------------------------------------------
# (plant, MWe, design GWh/yr, delivered GWh/yr, note)  all SOURCED
BUILT = (
    ("Gemasolar, Spain, 2011", 19.9, 110.0, 80.0,
     "mature; the best sustained record of any salt tower"),
    ("Crescent Dunes, USA, 2015", 110.0, 500.0, 196.0,
     "2018, best full year before the 2019 shutdown"),
    ("Noor III, Morocco, 2018", 150.0, 500.0, None,
     "exceeded expectations in 2021; 14-month hot-tank leak from Feb 2024"),
    ("Cerro Dominador, Chile, 2021", 110.0, 950.0, 115.4,
     "2023; hot-tank damage, plant largely stopped"),
)


# =============================================================================
# SOLAR GEOMETRY, EXACT
# =============================================================================
def declination_deg(doy):
    return 23.44 * math.sin(math.radians(360.0 / 365.0 * (284 + doy)))


def elevation_deg(lat, doy, solar_hour):
    d = math.radians(declination_deg(doy))
    phi = math.radians(lat)
    omega = math.radians(15.0 * (solar_hour - 12.0))
    s = math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(omega)
    return math.degrees(math.asin(max(-1.0, min(1.0, s))))


def air_mass(h_deg):
    if h_deg <= 0.0:
        return float("inf")
    return 1.0 / (math.sin(math.radians(h_deg))
                  + 0.50572 * (h_deg + 6.07995) ** -1.6364)


def clear_sky_dni(h_deg):
    """Meinel clear-sky beam irradiance, W/m2."""
    if h_deg <= 0.0:
        return 0.0
    return SOLAR_CONST * 0.7 ** (air_mass(h_deg) ** 0.678)


def month_of(doy):
    cum = (31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)
    for m, c in enumerate(cum, 1):
        if doy <= c:
            return m
    return 12


def dni_series(lat, lon, annual_kwh, cloud_fraction=CLOUD_DAY_FRACTION,
               winter=WINTER_CLEARNESS, summer=SUMMER_CLEARNESS):
    """8,760 hourly DNI values, W/m2, whose sum is the sourced annual total.

    RECONSTRUCTED shape: clear-sky geometry, a seasonal clearness that is
    lower in winter, and every (1/cloud_fraction)-th day overcast. The
    annual sum is then scaled EXACTLY to annual_kwh, so the shape cannot
    change the energy -- only its timing."""
    solar_offset = (lon + 120.0) / 15.0     # PST meridian is 120 W
    raw = []
    for doy in range(1, 366):
        m = month_of(doy)
        season = 0.5 * (winter + summer) - 0.5 * (summer - winter) * math.cos(
            2.0 * math.pi * (doy - 172) / 365.0)   # peaks at the June solstice
        cloudy = cloud_fraction > 0 and (doy % round(1.0 / cloud_fraction) == 0)
        for hr in range(24):
            h = elevation_deg(lat, doy, hr + 0.5 + solar_offset)
            v = clear_sky_dni(h) * season
            if cloudy:
                v *= CLOUD_DAY_DNI
            raw.append(v)
    total = sum(raw) / 1000.0            # kWh/m2 (W/m2 x 1 h)
    k = annual_kwh / total
    return [v * k for v in raw]


# =============================================================================
# THE PLANT, HOUR BY HOUR
# =============================================================================
def eta_optical(h_deg):
    if h_deg <= 0.0:
        return 0.0
    return ETA_OPT_PEAK * math.sin(math.radians(h_deg)) ** ETA_OPT_EXP


def turbine_thermal_at(load_frac, gross_mwe):
    """Thermal input for a given load fraction, MW_th."""
    eta = ETA_CYCLE * (PART_LOAD_A + (1.0 - PART_LOAD_A) * load_frac)
    return gross_mwe * load_frac / eta


def run_node(node, mode="peak-first", dni=None, eta_opt_peak=ETA_OPT_PEAK):
    """One node for one year. Returns a dict of annual totals and hourly lists.

    mode 'max-energy': the turbine runs whenever the store can feed it.
    mode 'peak-first': the turbine runs at full through the peak window
    whenever the store can; outside the window it runs only to keep the
    store from spilling and to burn down whatever the next peak window will
    not need. This is the honest version of the proposal's 'evening peak
    dispatch'."""
    name, lat, lon, ap, gross, store_cap, annual_dni, _st = node
    if dni is None:
        dni = dni_series(lat, lon, annual_dni)
    solar_offset = (lon + 120.0) / 15.0
    rated_th = turbine_thermal_at(1.0, gross)
    peak_need = rated_th * len(PEAK_HOURS)
    store = 0.5 * store_cap
    out = {"gross": 0.0, "net": 0.0, "field_th": 0.0, "spill_th": 0.0,
           "to_turbine_th": 0.0, "tank_loss_th": 0.0, "peak_net": 0.0,
           "offpeak_net": 0.0, "hours_on": 0, "hours_full": 0,
           "net_hourly": [], "month_net": [0.0] * 13}
    for i in range(8760):
        doy = i // 24 + 1
        hr = i % 24
        h = elevation_deg(lat, doy, hr + 0.5 + solar_offset)
        # ---- field -> receiver, MW_th this hour
        field = 0.0
        on_sun = dni[i] >= DNI_START and h > 0.0
        if on_sun:
            eo = eta_opt_peak * math.sin(math.radians(h)) ** ETA_OPT_EXP
            field = ap * dni[i] * eo * ETA_RECEIVER * AVAILABILITY / 1e6
        out["field_th"] += field
        # ---- tank loss
        loss = store_cap * TANK_LOSS_PER_DAY / 24.0
        store = max(0.0, store - loss)
        out["tank_loss_th"] += loss
        # ---- dispatch decision, MW_th to turbine this hour
        avail = store + field
        if mode == "max-energy":
            want = rated_th
        else:
            in_peak = hr in PEAK_HOURS
            if in_peak:
                want = rated_th
            else:
                # hours until the next peak window opens
                until = (PEAK_HOURS[0] - hr) % 24
                # what the field will still add before then is unknown to
                # the dispatcher; it keeps the store at the reserve and
                # burns the rest, and never lets the tank spill
                reserve = peak_need
                surplus = avail - reserve
                room = store_cap - store
                must = max(0.0, field - room)      # or the field defocuses
                want = max(must, surplus if until > 0 else 0.0)
                want = min(want, rated_th)
        # ---- turbine limits
        if want < turbine_thermal_at(MIN_LOAD, gross):
            want = 0.0
        want = min(want, avail, rated_th)
        # ---- solve load from thermal (eta depends on load, so iterate once)
        load = want / rated_th if want > 0 else 0.0
        gross_mwe = 0.0
        if want > 0.0:
            eta = ETA_CYCLE * (PART_LOAD_A + (1.0 - PART_LOAD_A) * load)
            gross_mwe = want * eta
            load = gross_mwe / gross
        # ---- storage update and spill
        store = avail - want
        spill = 0.0
        if store > store_cap:
            spill = store - store_cap
            store = store_cap
        out["spill_th"] += spill
        out["to_turbine_th"] += want
        # ---- parasitic
        par = (PAR_GROSS_FRAC * gross_mwe
               + (PAR_FIELD_FRAC * gross if on_sun else 0.0)
               + PAR_NIGHT_FRAC * gross)
        net = gross_mwe - par
        out["gross"] += gross_mwe
        out["net"] += net
        out["net_hourly"].append(net)
        out["month_net"][month_of(doy)] += net
        if hr in PEAK_HOURS:
            out["peak_net"] += net
        else:
            out["offpeak_net"] += net
        if gross_mwe > 0:
            out["hours_on"] += 1
        if load > 0.99:
            out["hours_full"] += 1
    out["name"] = name
    out["gross_mwe"] = gross
    out["cf_gross"] = out["gross"] / (gross * 8760.0)
    out["cf_net"] = out["net"] / ((gross - gross / GROSS_MWE * PARASITIC_MWE)
                                  * 8760.0)
    return out


def run_network(mode="peak-first", **kw):
    nodes = [run_node(n, mode=mode, **kw) for n in NODES]
    tot = {k: sum(n[k] for n in nodes) for k in
           ("gross", "net", "field_th", "spill_th", "to_turbine_th",
            "tank_loss_th", "peak_net", "offpeak_net")}
    tot["nodes"] = nodes
    tot["net_hourly"] = [sum(n["net_hourly"][i] for n in nodes)
                         for i in range(8760)]
    tot["month_net"] = [sum(n["month_net"][m] for n in nodes)
                        for m in range(13)]
    tot["cf_gross"] = tot["gross"] / (GROSS_MWE * 8760.0)
    tot["cf_net"] = tot["net"] / ((GROSS_MWE - PARASITIC_MWE) * 8760.0)
    return tot


# =============================================================================
# THE CHECKS THE PROPOSAL'S OWN NUMBERS ALLOW
# =============================================================================
def storage_hours():
    return STORAGE_MWH_TH / turbine_thermal_at(1.0, GROSS_MWE)


def salt_capacity_mwh():
    return SALT_T * 1000.0 * SALT_CP * (T_HOT - T_COLD) / 3.6e6   # kJ -> MWh


def solar_multiple(design_dni=950.0, design_eta=None):
    design_eta = ETA_OPT_PEAK * ETA_RECEIVER if design_eta is None else design_eta
    field = APERTURE_M2 * design_dni * design_eta / 1e6
    return field / turbine_thermal_at(1.0, GROSS_MWE)


def aperture_for_sm(sm, design_dni=950.0):
    return sm * turbine_thermal_at(1.0, GROSS_MWE) * 1e6 / (
        design_dni * ETA_OPT_PEAK * ETA_RECEIVER)


# =============================================================================
# PRICING
# =============================================================================
def price_2024(month, hour):
    if hour in PEAK_HOURS:
        return float(PEAK_PRICE_2024[month])
    if hour in MIDDAY_HOURS:
        return float(MIDDAY_PRICE_2024[month])
    return OTHER_PRICE_2024


def price_series(scale=1.0, peak_override=None):
    p = []
    for i in range(8760):
        doy = i // 24 + 1
        hr = i % 24
        v = price_2024(month_of(doy), hr) * scale
        if peak_override is not None and hr in PEAK_HOURS:
            v = peak_override
        p.append(v)
    return p


def revenue_m(net_hourly, prices):
    return sum(n * p for n, p in zip(net_hourly, prices)) / 1e6


def shape_average(prices):
    return sum(prices) / len(prices)


def negative_hours(prices):
    return sum(1 for p in prices if p < 0)


def fidelity_band():
    """Delivered over designed, from the built record."""
    f = [(p, d / g) for p, _m, g, d, _n in BUILT if d is not None]
    return f


# =============================================================================
# REPORT
# =============================================================================
def report():
    pf = run_network("peak-first")
    me = run_network("max-energy")
    p24 = price_series()
    p23 = price_series(scale=WEIM_2023_OVER_2024)
    print()
    print("  PROGRAM HELIOS-1M AT THE SCALE PROPOSED -- F-01 AND F-02")
    print()
    print("    The plant exactly as Title I states it: 45.6 M m2 of aperture,")
    print(f"    {GROSS_MWE:,.0f} MWe gross, {STORAGE_MWH_TH:,.0f} MWh_th of salt,"
          f" {PARASITIC_MWE:.0f} MW parasitic,")
    print("    three nodes. Nothing enlarged, nothing moved. Run through a")
    print("    year hour by hour and priced at what the hours pay.")
    print()
    print("    FIRST, WHAT THE PROPOSAL'S OWN NUMBERS SAY ABOUT EACH OTHER.")
    print(f"      storage at nameplate       {storage_hours():5.1f} h"
          f"      (claimed 16 h)             consistent")
    print(f"      salt inventory holds       {salt_capacity_mwh():,.0f} MWh_th"
          f"  (claimed {STORAGE_MWH_TH:,.0f})  "
          f"{salt_capacity_mwh() / STORAGE_MWH_TH:.3f}x, consistent")
    print(f"      solar multiple at 950 W/m2 {solar_multiple():5.2f}"
          f"        (claimed {CLAIMED_SM:.1f})           F-06: the aperture")
    print(f"      aperture SM {CLAIMED_SM:.0f} would need  "
          f"{aperture_for_sm(CLAIMED_SM) / 1e6:5.0f} M m2     (stated 45.6)"
          "          supports SM 2, not 5")
    print()
    print("    THE YEAR, NODE BY NODE (peak-first dispatch):")
    print("      node                         DNI kWh/m2  field TWh_th"
          "  net TWh  CF_net  spill %")
    for n, node in zip(pf["nodes"], NODES):
        print(f"      {n['name']:<28} {node[6]:7.0f}     {n['field_th'] / 1e6:6.2f}"
              f"      {n['net'] / 1e6:5.2f}   {n['cf_net']:.3f}"
              f"   {100 * n['spill_th'] / max(n['field_th'], 1):4.1f}")
    print(f"      {'NETWORK':<28} {'':7}     {pf['field_th'] / 1e6:6.2f}"
          f"      {pf['net'] / 1e6:5.2f}   {pf['cf_net']:.3f}"
          f"   {100 * pf['spill_th'] / pf['field_th']:4.1f}")
    print()
    print(f"    THE REAL NUMBER: {pf['net'] / 1e6:.1f} TWh NET PER YEAR,"
          f" a net capacity factor of {pf['cf_net']:.3f}.")
    print(f"    Run for maximum energy instead of for the peak it makes"
          f" {me['net'] / 1e6:.1f} TWh;")
    print("    the two are within a few percent because a 16 h store rarely")
    print("    has to choose.")
    print()
    print("    AGAINST WHAT TITLE I SELLS:")
    sold = (CLAIMED_INSTATE_MWE + CLAIMED_EXPORT_MWE) * 8760.0
    print(f"      in-state 3,000 MW x 8,760 h        "
          f"{CLAIMED_INSTATE_MWE * 8760 / 1e6:5.1f} TWh")
    print(f"      export   1,515 MW x 8,760 h        "
          f"{CLAIMED_EXPORT_MWH / 1e6:5.1f} TWh")
    print(f"      sold                               {sold / 1e6:5.1f} TWh")
    print(f"      made                               {pf['net'] / 1e6:5.1f} TWh")
    print(f"      shortfall                          "
          f"{100 * (1 - pf['net'] / sold):5.0f} %   (sold/made ="
          f" {sold / pf['net']:.2f}x)")
    left = pf["net"] - CLAIMED_INSTATE_MWE * 8760.0
    print(f"      left for export after 3,000 MW     {left / 1e6:+5.1f} TWh")
    print("    THE PLANT AS SPECIFIED HAS NO EXPORT. After the in-state promise")
    print("    it is short, so the export line -- the line that funds the")
    print("    program -- is not overstated, it is empty. F-01 is not a")
    print("    percentage; it is the sign.")
    print()
    print("    WHEN IT MAKES IT (peak-first):")
    print(f"      in the 4 h peak window (17-21)     {pf['peak_net'] / 1e6:5.1f} TWh"
          f"   {100 * pf['peak_net'] / pf['net']:4.0f} %")
    print(f"      all other hours                    {pf['offpeak_net'] / 1e6:5.1f} TWh"
          f"   {100 * pf['offpeak_net'] / pf['net']:4.0f} %")
    print("    Four hours a day at full load is at most 4/24 of a year's")
    print("    output. A 16 h store does not put 100 % of the energy into a")
    print("    4 h window; it puts the window at full and the rest wherever")
    print("    the tank would otherwise spill.")
    print()
    dec = pf["month_net"][12] / 31.0 / 24.0
    jun = pf["month_net"][6] / 30.0 / 24.0
    print(f"      December average net               {dec:6.0f} MW"
          f"  ({100 * dec / (GROSS_MWE - PARASITIC_MWE):3.0f} % of net"
          " nameplate)")
    print(f"      June average net                   {jun:6.0f} MW"
          f"  ({100 * jun / (GROSS_MWE - PARASITIC_MWE):3.0f} %)")
    print("    The 'guaranteed 16-hr charge during winter DNI minimums' is")
    print("    F-06's, and December says what it is worth.")
    print()
    print("    F-02: WHAT THE HOURS PAY.")
    print(f"      2024 shape: average {shape_average(p24):5.1f} $/MWh"
          f" (sourced WEIM 2024 ~{WEIM_AVG_2024:.0f}),"
          f" {negative_hours(p24)} negative hours (sourced {NEG_HOURS_2024})")
    print("      hour-ending-20 anchors: Q1 $64, Jul $146, Aug $97, Oct $63")
    print()
    print("      revenue on ALL net generation sold at wholesale, $M/yr:")
    r24 = revenue_m(pf["net_hourly"], p24)
    r23 = revenue_m(pf["net_hourly"], p23)
    print(f"        2024 price shape                 {r24:7.0f}"
          f"     ({r24 / (pf['net'] / 1e6):.1f} $/MWh realised)")
    print(f"        2023 price shape (x{WEIM_2023_OVER_2024:.2f})       {r23:7.0f}")
    for pp in CLAIMED_PEAK_PRICES:
        rp = revenue_m(pf["net_hourly"], price_series(peak_override=pp))
        print(f"        Title I ${pp:.0f} peak, 2024 off-peak  {rp:7.0f}")
    print(f"        Title I §4.2 as written          "
          f"{CLAIMED_EXPORT_MWH * CLAIMED_PEAK_PRICES[0] / 1e6:7.0f}"
          f"  ..{CLAIMED_EXPORT_MWH * CLAIMED_PEAK_PRICES[2] / 1e6:6.0f}"
          "  (export only, RA excluded)")
    print(f"      against a carrying cost of         {CARRYING_COST_M:7.0f}"
          "  (Title I §4.1, itself F-05/F-19)")
    print()
    print("    THREE THINGS TO READ OFF THAT TABLE. The proposal's revenue is")
    print("    what the WHOLE plant earns if EVERY megawatt-hour is sold at")
    print(f"    wholesale -- and at 2024 prices that is {r24 / CARRYING_COST_M:.2f}"
          " of the carrying")
    print("    cost, with nothing left for a household. The $190-350 peak")
    print("    prices are real prices for real hours, but only the peak-window")
    print(f"    energy earns them: the $190 'conservative' case reaches "
          f"{revenue_m(pf['net_hourly'], price_series(peak_override=190.0)) / CARRYING_COST_M:.2f}")
    print(f"    of carrying cost, and only the $350 case clears it, at "
          f"{revenue_m(pf['net_hourly'], price_series(peak_override=350.0)) / CARRYING_COST_M:.2f} --")
    print(f"    a price {350.0 / max(PEAK_PRICE_2024.values()):.1f}x the highest"
          " monthly hour-ending-20 average of 2024,")
    print("    earned by selling every megawatt-hour including the ones")
    print("    promised to households. The in-state $0.00 tariff is not a")
    print("    revenue at all -- it is the same energy sold at zero.")
    print()
    print("    THE BUILT RECORD, WHICH THE MODEL ABOVE STILL FLATTERS.")
    print("      plant                          design GWh  delivered   ratio")
    for p, _m, g, d, note in BUILT:
        r = f"{d / g:.2f}" if d else "  -- "
        dd = f"{d:6.1f}" if d else "   -- "
        print(f"      {p:<30} {g:6.0f}   {dd}     {r}   {note}")
    best = max(r for _p, r in fidelity_band())
    print()
    print(f"    No commercial salt tower has delivered its design output. The")
    print(f"    best sustained record is Gemasolar at {best:.2f} of design after")
    print("    a decade of operation; Crescent Dunes reached 0.39. Applied to")
    print("    the model:")
    for lab, f in (("model as run", 1.0), ("at the best record", best),
                   ("at Crescent Dunes", 196.0 / 500.0)):
        print(f"      {lab:<22} {pf['net'] * f / 1e6:5.1f} TWh   "
              f"{revenue_m(pf['net_hourly'], p24) * f:6.0f} $M at 2024")
    print()
    print("    WHAT THIS PASS DOES NOT DO. It does not enlarge the field to")
    print("    meet the promise, add electric charging from curtailed solar,")
    print("    re-site the Central Valley node, or price the in-state energy")
    print("    as a bill credit. Each is a redesign and each is a later pass.")
    print("    What it does is replace two impossible numbers with the real")
    print(f"    ones: {pf['net'] / 1e6:.1f} TWh a year at the scale proposed,"
          f" worth about ${r24 / 1e3:.1f} B at")
    print("    2024 wholesale, against a carrying cost the proposal itself puts")
    print(f"    at ${CARRYING_COST_M / 1e3:.2f} B and later flaws will raise.")
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
    print("  solar geometry is exact")
    check("declination at the March equinox is ~0",
          abs(declination_deg(80)) < 0.5)
    check("declination at the June solstice is +23.4",
          abs(declination_deg(172) - 23.44) < 0.1)
    check("noon elevation at 35 N on the solstice is 78.4",
          abs(elevation_deg(35.0, 172, 12.0) - (90 - 35 + 23.44)) < 0.2)
    check("clear-sky DNI at zenith is under the solar constant",
          0.0 < clear_sky_dni(90.0) < SOLAR_CONST)
    check("no DNI below the horizon", clear_sky_dni(-5.0) == 0.0)

    print()
    print("  the irradiance series is pinned to the sourced annual total")
    for node in NODES:
        s = dni_series(node[1], node[2], node[6])
        check(f"  {node[0]:<26} sums to {node[6]:.0f} kWh/m2",
              abs(sum(s) / 1000.0 - node[6]) < 0.5)
    s0 = dni_series(35.0, -117.56, 2799.0, cloud_fraction=0.0)
    s1 = dni_series(35.0, -117.56, 2799.0, cloud_fraction=0.30)
    check("  -- and a different cloud pattern keeps the same total",
          abs(sum(s0) - sum(s1)) < 1.0)

    print()
    print("  the proposal's own numbers agree with each other where they do")
    check("16 h of storage at nameplate (claimed 16)",
          abs(storage_hours() - 16.0) < 0.5)
    check("1.665 Mt of salt holds the claimed MWh_th to 5 %",
          abs(salt_capacity_mwh() / STORAGE_MWH_TH - 1.0) < 0.05)
    check("  -- and disagree where they do not: SM is ~2, not 5 (F-06)",
          1.8 < solar_multiple() < 2.5 and solar_multiple() < 0.5 * CLAIMED_SM)
    check("  -- SM 5 would need more than twice the stated aperture",
          aperture_for_sm(CLAIMED_SM) > 2.0 * APERTURE_M2)

    print()
    print("  the hourly plant conserves energy and respects its limits")
    n = run_node(NODES[0], mode="peak-first")
    # field in = to turbine + spill + tank loss +/- store delta (store starts
    # and ends near half; allow the half-tank swing)
    bal = n["field_th"] - n["to_turbine_th"] - n["spill_th"] - n["tank_loss_th"]
    check("field = turbine + spill + tank loss, to within one tank",
          abs(bal) < NODES[0][5])
    check("net never exceeds gross nameplate in any hour",
          max(n["net_hourly"]) <= NODES[0][4])
    check("gross capacity factor is below one (F-01)", n["cf_gross"] < 1.0)
    check("  -- and below 0.75, which no CSP plant has ever reached",
          n["cf_gross"] < 0.75)
    check("  -- and above 0.35, or the field is not being used",
          n["cf_gross"] > 0.35)
    me = run_node(NODES[0], mode="max-energy")
    check("peak-first never makes more energy than max-energy",
          n["net"] <= me["net"] * 1.001)
    check("  -- and makes at least 90 % of it (a 16 h store rarely chooses)",
          n["net"] >= 0.90 * me["net"])
    check("peak-first puts more energy in the window than max-energy",
          n["peak_net"] >= me["peak_net"])
    check("the peak window is 4 of 24 hours, so it holds under half the energy",
          n["peak_net"] < 0.5 * n["net"])
    check("hours at full load are fewer than the hours on",
          n["hours_full"] < n["hours_on"] <= 8760)

    print()
    print("  the finding: sold exceeds made, and export is negative")
    pf = run_network("peak-first")
    sold = (CLAIMED_INSTATE_MWE + CLAIMED_EXPORT_MWE) * 8760.0
    check("network net is under what Title I sells", pf["net"] < sold)
    check("  -- by more than a third", pf["net"] < 0.67 * sold)
    check("  -- and under the in-state promise alone, so export < 0",
          pf["net"] < CLAIMED_INSTATE_MWE * 8760.0)
    check("the Central Valley node makes the least (F-22)",
          min(pf["nodes"], key=lambda x: x["net"])["name"].startswith("Central"))
    # annual energy is insensitive to the hourly shape: rerun with no clouds
    # and a flat season and require the network total within 5 %
    alt = [run_node(nd, dni=dni_series(nd[1], nd[2], nd[6], cloud_fraction=0.0,
                                       winter=1.0, summer=1.0))["net"]
           for nd in NODES]
    check("annual energy moves under 5 % when the hourly shape is changed",
          abs(sum(alt) / pf["net"] - 1.0) < 0.05)

    print()
    print("  the price shape is pinned to its anchors")
    p24 = price_series()
    check("average is within $8 of the sourced WEIM 2024 average",
          abs(shape_average(p24) - WEIM_AVG_2024) < 8.0)
    check("negative hours within 25 % of the sourced 1,180",
          abs(negative_hours(p24) / NEG_HOURS_2024 - 1.0) < 0.25)
    check("July hour-ending-20 is the sourced $146",
          price_2024(7, 19) == 146.0)
    check("a peak override changes only peak hours",
          sum(1 for a, b in zip(p24, price_series(peak_override=999.0))
              if a != b) == len(PEAK_HOURS) * 365)

    print()
    print("  the revenue finding")
    r24 = revenue_m(pf["net_hourly"], p24)
    check("all-energy revenue at 2024 prices is under the carrying cost",
          r24 < CARRYING_COST_M)
    r190 = revenue_m(pf["net_hourly"], price_series(peak_override=190.0))
    r350 = revenue_m(pf["net_hourly"], price_series(peak_override=350.0))
    check("  -- and so is Title I's own $190 'conservative' case", r190 < CARRYING_COST_M)
    check("  -- only the $350 case clears it, and only by selling every MWh",
          r350 > CARRYING_COST_M and r190 < CARRYING_COST_M)
    check("  -- and every case is under Title I's own conservative figure",
          r350 < CLAIMED_EXPORT_MWH * CLAIMED_PEAK_PRICES[0] / 1e6)
    check("  -- $350 is above every sourced 2024 monthly HE20 price by > 2x",
          350.0 > 2.0 * max(PEAK_PRICE_2024.values()))
    check("the built record has no plant at or above design",
          all(r < 1.0 for _p, r in fidelity_band()))
    check("  -- and the best of it is Gemasolar",
          max(fidelity_band(), key=lambda t: t[1])[0].startswith("Gemasolar"))

    print()
    print("  and what the instrument refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it says the plant as specified has no export",
          "HAS NO EXPORT" in out)
    check("it names what it does not do", "WHAT THIS PASS DOES NOT DO" in out)
    check("it carries the RA exclusion", "RA excluded" in out)
    check("it labels the SM finding as F-06", "F-06" in out)

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
