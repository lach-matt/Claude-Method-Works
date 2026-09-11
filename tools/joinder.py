#!/usr/bin/env python3
"""joinder.py -- Title III: can Title II return Title I's winter?

hourly3.py found that a sun-following plant sized on the annual energy
serves 84 % of the load: a third of December goes unserved while a quarter
of June's field is defocused. Sixteen hours of store cannot move June into
December. The author (2026-09-11): water stores across seasons and
electricity does not -- desalinate on the summer surplus, hold the water,
"and the offset is returned from the desalination plants from their
turbines."

There are two turbines that sentence can mean, and this file prices both,
at mid and at critical, against the winter hourly3.py measured.

  A. STEAM-TOPPING turbines at the desalination plant (Title II's own
     architecture: solar-thermal skids, steam through a back-pressure
     turbine, the exhaust heat into LT-MED). Electricity is a co-product
     of making water from heat. It returns in winter only what heat is
     there in winter, and F-13 / F-27 found a coastal brownfield has no
     heat source at the scale a module needs. Priced here as what it WOULD
     return per m3 if the heat existed, and what it costs in electricity
     against a condensing cycle -- so the reader sees it is a way of
     making water dear, not of making winter power.

  B. HYDRAULIC turbines on the water itself. Summer surplus electricity
     desalinates AND lifts the product water to an elevated off-stream
     reservoir; in winter the water is delivered downhill through
     pump-turbines to the aqueduct and to groundwater recharge, and the
     head comes back as electricity. That is pumped storage whose working
     fluid is the state's own water supply, on the pattern of San Luis /
     Gianelli, and it is seasonal because the reservoir is. The energy per
     m3 is rho.g.H.eta; the winter it can return is bounded by the water
     Title II makes and the head the site allows; the cost is a reservoir
     and a pump-generation plant, priced on sourced analogues.

Both are set against hourly3.py's Nov-Feb unserved energy and its summer
spill, at both cases. The file decides nothing; it says which turbine
returns a winter and what it costs beside the field oversizing hourly3.py
priced. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hourly3 as HR                                            # noqa: E402
import cspchain as C                                            # noqa: E402
import firmpower as FP                                          # noqa: E402

CASES = ("mid", "critical")
# --- water --------------------------------------------------------------------
M3_PER_AF = 1233.48                       # exact
MODULE_AFY = 50_000.0                     # Title II's baseline module                 Title II §4
MODULE_M3_YR = MODULE_AFY * M3_PER_AF     # m3 per module-year                          exact
# --- desalination energy --------------------------------------------------------
RO_KWH_M3 = (3.0, 3.6)                    # SWRO with energy recovery, plant total     SOURCED band (Carlsbad ~3.6)
LTMED_KWH_TH_M3 = 70.0                    # LT-MED thermal duty                        FLAWS F-13 (SOURCED band 60-80)
LTMED_KWH_E_M3 = 1.5                      # LT-MED pumping / vacuum electricity        SOURCED band 1.0-2.0
# --- A: steam-topping cogeneration -----------------------------------------------
ETA_BACKPRESSURE = (0.33, 0.28)           # electric efficiency exhausting at ~70 C    ASSUMED band (nominal, critical)
ETA_CONDENSING = None                     # taken from cspchain's cycle link per case (0.50 / 0.45)
# --- B: hydraulic return ---------------------------------------------------------
HEAD_M = (500.0, 300.0)                   # off-stream reservoir head above delivery   ASSUMED band (Edmonston lift 587 m; Gianelli ~100 m)
ETA_TURBINE = (0.90, 0.85)                # pump-turbine generating                    SOURCED band
ETA_PUMP = (0.90, 0.85)                   # pump-turbine pumping                       SOURCED band
RHO_G_KWH_M3_PER_M = 9.81 * 1000.0 / 3.6e6   # kWh per m3 per metre of head             exact (0.002725)
RESERVOIR_B_PER_KM3 = (2.5, 4.0)          # $B per km3, off-stream, new-build          SOURCED band (Sites ~$4.5 B for ~1.8 km3)
PUMPGEN_PER_KW = (1500.0, 2500.0)         # $/kW pump-turbine plant                    ASSUMED band
WINTER_MONTHS = (11, 12, 1, 2)            # hourly3's winter                          exact
WINTER_DELIVERY_H = 120.0 * 24.0          # the reservoir is drawn over Nov-Feb         exact
WATER_END_USE = "aqueduct and groundwater recharge (SGMA winter recharge)"


def pick(band, case):
    return band[CASES.index(case)] if isinstance(band, tuple) else band


def winter(case):
    r = HR.run(case)
    unserved = sum(r["month_unserved"][m] for m in WINTER_MONTHS) / 1e6        # TWh_e
    surplus_e = (r["spill_th"] * r["design"]["links"]["cycle"] + r["pv_curtail"]) / 1e6   # TWh_e the plant could have made
    return dict(unserved_twh=unserved, surplus_twh=surplus_e, run=r)


# ---- A ---------------------------------------------------------------------
def topping_per_m3(case):
    """Electricity a back-pressure turbine returns per m3 of LT-MED water, and
    what that water costs in electricity against a condensing cycle on the
    same heat."""
    eb = pick(ETA_BACKPRESSURE, case)
    ec = C.design("helios3", case)["links"]["cycle"]
    heat_in = LTMED_KWH_TH_M3 / (1.0 - eb)          # heat the turbine needs to leave 70 kWh_th behind
    e_returned = heat_in * eb
    e_condensing = heat_in * ec                     # what that heat makes with no water
    cost_of_water = e_condensing - e_returned + LTMED_KWH_E_M3
    return dict(heat_in=heat_in, e_returned=e_returned, e_condensing=e_condensing,
                cost_kwh_e_m3=cost_of_water, ro_kwh_e_m3=pick(RO_KWH_M3, case))


# ---- B ---------------------------------------------------------------------
def hydraulic_per_m3(case):
    h = pick(HEAD_M, case)
    ret = RHO_G_KWH_M3_PER_M * h * pick(ETA_TURBINE, case)
    lift = RHO_G_KWH_M3_PER_M * h / pick(ETA_PUMP, case)
    return dict(head=h, returned_kwh_m3=ret, lift_kwh_m3=lift, round_trip=ret / lift)


def hydraulic_winter(case, w=None):
    """Two bounds. REQUIREMENT: the water and plant that would return the
    whole winter. SURPLUS-BOUNDED: the water the summer surplus can both
    desalinate and lift, and the winter THAT returns -- the physically honest
    figure, since the surplus is what the scheme runs on."""
    w = winter(case) if w is None else w
    per = hydraulic_per_m3(case)
    ci = CASES.index(case)
    ro = pick(RO_KWH_M3, case)

    def plant(m3):
        ret_twh = m3 * per["returned_kwh_m3"] / 1e9
        mw = ret_twh * 1e6 / WINTER_DELIVERY_H
        reservoir_b = m3 / 1e9 * RESERVOIR_B_PER_KM3[ci]
        pumpgen_b = mw * 1e3 * PUMPGEN_PER_KW[ci] / 1e9
        return dict(m3=m3, km3=m3 / 1e9, af=m3 / M3_PER_AF, modules=m3 / MODULE_M3_YR,
                    lift_twh=m3 * per["lift_kwh_m3"] / 1e9, desal_twh=m3 * ro / 1e9,
                    summer_needed_twh=m3 * (per["lift_kwh_m3"] + ro) / 1e9,
                    returned_twh=ret_twh, winter_share=ret_twh / w["unserved_twh"], mw=mw,
                    reservoir_b=reservoir_b, pumpgen_b=pumpgen_b, capex_b=reservoir_b + pumpgen_b)

    req = plant(w["unserved_twh"] * 1e9 / per["returned_kwh_m3"])
    bounded = plant(w["surplus_twh"] * 1e9 / (per["lift_kwh_m3"] + ro))
    return dict(per=per, winter=w, requirement=req, bounded=bounded)


HEAD_SCAN = (300.0, 500.0, 800.0)         # m, sites from the Gianelli class to the Tehachapi crest   ASSUMED scan


def modules_to_close(case, head=None, w=None):
    """The author's question (2026-09-11): not more storage on the power side
    -- more MODULES. The water is on Title II's own account (its cost model
    already carries its energy line), so Title I's surplus is spent on the
    LIFT alone, and the winter closes when enough water comes down. Returns
    the modules, the lift energy against the surplus, the reservoir and the
    plant, at a head."""
    w = winter(case) if w is None else w
    h = pick(HEAD_M, case) if head is None else head
    ci = CASES.index(case)
    ret = RHO_G_KWH_M3_PER_M * h * pick(ETA_TURBINE, case)
    lift = RHO_G_KWH_M3_PER_M * h / pick(ETA_PUMP, case)
    m3 = w["unserved_twh"] * 1e9 / ret
    lift_twh = m3 * lift / 1e9
    mw = w["unserved_twh"] * 1e6 / WINTER_DELIVERY_H
    reservoir_b = m3 / 1e9 * RESERVOIR_B_PER_KM3[ci]
    pumpgen_b = mw * 1e3 * PUMPGEN_PER_KW[ci] / 1e9
    return dict(head=h, m3=m3, km3=m3 / 1e9, maf=m3 / M3_PER_AF / 1e6, modules=m3 / MODULE_M3_YR,
                lift_twh=lift_twh, surplus_twh=w["surplus_twh"], lift_within_surplus=lift_twh <= w["surplus_twh"],
                desal_twh_on_title_ii=m3 * pick(RO_KWH_M3, case) / 1e9, mw=mw,
                reservoir_b=reservoir_b, pumpgen_b=pumpgen_b, capex_b=reservoir_b + pumpgen_b)


def field_closure_b(case):
    """hourly3's closing overbuild, direct $B, for comparison."""
    d = C.design("helios3", case)
    return HR.closure_cost_m(d, 1.0, 1.0, 1.5, 2.0, 2.0) / 1e3


def price_delta(case, capex_b):
    d = C.design("helios3", case)
    return HR.price_delta(d, capex_b * 1e3)


def report():
    print()
    print("  TITLE III: CAN TITLE II RETURN TITLE I'S WINTER?")
    print("  ==================================================")
    print("    hourly3.py: a third of December unserved, a quarter of June's field")
    print("    defocused. The author: desalinate on the summer surplus, hold the water,")
    print("    and return the offset from the desalination plants' turbines. Two")
    print("    turbines that can mean; both priced, at mid and at critical.")
    ws = {c: winter(c) for c in CASES}
    print()
    print(f"      {'':<44}{'mid':>10}{'critical':>10}")
    print(f"      {'winter (Nov-Feb) unserved, TWh_e':<44}" + "".join(f"{ws[c]['unserved_twh']:10.2f}" for c in CASES))
    print(f"      {'summer surplus the plant threw away, TWh_e':<44}" + "".join(f"{ws[c]['surplus_twh']:10.2f}" for c in CASES))
    print("      (surplus = defocused field at the cycle efficiency + curtailed PV)")
    print()
    print("    A. STEAM-TOPPING TURBINES AT THE DESALINATION PLANT (Title II's own")
    print("       architecture). Per m3 of LT-MED water:")
    print(f"      {'':<44}{'mid':>10}{'critical':>10}")
    tp = {c: topping_per_m3(c) for c in CASES}
    for label, key in (("heat the turbine must take in, kWh_th", "heat_in"),
                       ("electricity returned by the turbine, kWh_e", "e_returned"),
                       ("what that heat makes with NO water, kWh_e", "e_condensing"),
                       ("so the water COSTS, kWh_e per m3", "cost_kwh_e_m3"),
                       ("reverse osmosis, for comparison, kWh_e", "ro_kwh_e_m3")):
        print(f"      {label:<44}" + "".join(f"{tp[c][key]:10.1f}" for c in CASES))
    print("       The topping turbine returns electricity it was given as heat, less what")
    print("       the water took. Against a condensing cycle the water costs")
    print(f"       {tp['mid']['cost_kwh_e_m3'] / tp['mid']['ro_kwh_e_m3']:.1f}x (mid) / {tp['critical']['cost_kwh_e_m3'] / tp['critical']['ro_kwh_e_m3']:.1f}x (critical) what reverse osmosis costs. And in")
    print("       winter it returns only what heat is there in winter: F-13 and F-27 found")
    print("       a coastal brownfield has no heat source at a module's scale. THIS")
    print("       TURBINE DOES NOT RETURN A WINTER; it makes water dear in summer.")
    print()
    print("    B. HYDRAULIC TURBINES ON THE WATER ITSELF. Summer surplus desalinates")
    print("       AND lifts the product to an elevated off-stream reservoir; in winter")
    print("       the water is delivered downhill through pump-turbines and the head")
    print("       comes back. Pumped storage whose working fluid is the water supply.")
    hy = {c: hydraulic_winter(c, ws[c]) for c in CASES}
    print(f"      {'':<44}{'mid':>10}{'critical':>10}")
    for label, f, fmt in (("head, m", lambda h: h["per"]["head"], "{:10.0f}"),
                          ("returned per m3 delivered, kWh_e", lambda h: h["per"]["returned_kwh_m3"], "{:10.2f}"),
                          ("lift per m3 in summer, kWh_e", lambda h: h["per"]["lift_kwh_m3"], "{:10.2f}"),
                          ("round trip", lambda h: h["per"]["round_trip"], "{:10.2f}")):
        print(f"      {label:<44}" + "".join(fmt.format(f(hy[c])) for c in CASES))
    print("       THE REQUIREMENT -- to return the whole winter:")
    for label, key, fmt in (("water, km3", "km3", "{:10.2f}"), ("  = Title II modules' annual output", "modules", "{:10.1f}"),
                            ("summer electricity to desalinate + lift, TWh_e", "summer_needed_twh", "{:10.2f}")):
        print(f"      {label:<44}" + "".join(fmt.format(hy[c]["requirement"][key]) for c in CASES))
    print(f"      {'  against the surplus thrown away, TWh_e':<44}" + "".join(f"{ws[c]['surplus_twh']:10.2f}" for c in CASES))
    print("       The surplus cannot make and lift that much water. So the honest figure")
    print("       is the other bound:")
    print("       SURPLUS-BOUNDED -- what the thrown-away summer can desalinate AND lift:")
    for label, key, fmt in (("water made and lifted, km3", "km3", "{:10.2f}"),
                            ("  = acre-feet, M", "af", "{:10.2f}"),
                            ("  = Title II modules' annual output", "modules", "{:10.1f}"),
                            ("winter returned, TWh_e", "returned_twh", "{:10.2f}"),
                            ("  = share of the winter unserved", "winter_share", "{:10.2f}"),
                            ("pump-generation plant, MW", "mw", "{:10,.0f}"),
                            ("reservoir, $B", "reservoir_b", "{:10.2f}"),
                            ("pump-generation, $B", "pumpgen_b", "{:10.2f}"),
                            ("capex, $B", "capex_b", "{:10.2f}")):
        v = {c: hy[c]["bounded"][key] for c in CASES}
        if key == "af":
            v = {c: v[c] / 1e6 for c in CASES}
        print(f"      {label:<44}" + "".join(fmt.format(v[c]) for c in CASES))
    print(f"      {'  + $/MWh on Title I':<44}" + "".join(f"{price_delta(c, hy[c]['bounded']['capex_b']):10.1f}" for c in CASES))
    print(f"      {'  $B per TWh of winter returned':<44}" + "".join(f"{hy[c]['bounded']['capex_b'] / hy[c]['bounded']['returned_twh']:10.2f}" for c in CASES))
    print(f"      {'hourly3 field oversizing: $B, whole winter':<44}" + "".join(f"{field_closure_b(c):10.2f}" for c in CASES))
    print(f"      {'  $B per TWh of winter':<44}" + "".join(f"{field_closure_b(c) / ws[c]['unserved_twh']:10.2f}" for c in CASES))
    print("       Per TWh of winter returned the water is cheaper than the mirrors at")
    print("       both cases, and it is bounded by the surplus: the scheme returns a")
    print("       share of the winter and makes that much water as its product. The")
    print("       water is not consumed by the return; it is delivered, to the")
    print(f"       {WATER_END_USE}, which is where winter")
    print("       water goes in California anyway. What it needs is HEAD and a RESERVOIR")
    print("       where the water is wanted below it -- a siting question, and the")
    print("       reason San Luis exists.")
    print()
    print()
    print("    C. MORE MODULES, NOT MORE STORAGE (the author, 2026-09-11). Put the water")
    print("       on Title II's own account -- its cost model already carries its energy")
    print("       line -- and spend Title I's surplus on the LIFT alone. Then the winter")
    print("       closes when enough water comes down, and the question is how many")
    print("       modules and how much head:")
    print(f"      {'':<10}{'head m':>7}{'modules':>9}{'MAF/yr':>8}{'km3':>7}{'lift TWh':>10}{'surplus':>9}{'fits':>6}{'desal TWh (II)':>15}{'MW':>7}{'capex $B':>10}{'+ $/MWh':>9}")
    for c in CASES:
        for h in HEAD_SCAN:
            m = modules_to_close(c, h, ws[c])
            print(f"      {c:<10}{m['head']:7.0f}{m['modules']:9.1f}{m['maf']:8.2f}{m['km3']:7.2f}{m['lift_twh']:10.2f}{m['surplus_twh']:9.2f}"
                  f"{'yes' if m['lift_within_surplus'] else 'NO':>6}{m['desal_twh_on_title_ii']:15.2f}{m['mw']:7,.0f}{m['capex_b']:10.2f}{price_delta(c, m['capex_b']):9.1f}")
    print(f"      {'field oversizing, for comparison':<27}" + "".join(f"  {c}: ${field_closure_b(c):.1f} B, +{price_delta(c, field_closure_b(c)):.0f} $/MWh" for c in CASES))
    print("       Hydro output at a desalination plant is volume x head, and the plant")
    print("       is at sea level: the head is where the water comes DOWN, a property of")
    print("       the reservoir site, not of the plant. So the two levers are exactly")
    print("       the author's two -- more modules (volume) and a higher site (head) --")
    print("       and head is worth more: it halves the water for each doubling. The")
    print("       lift fits inside the surplus at every head at both cases; what the")
    print("       modules cost is Title II's, and what they need is TAKERS for a")
    print("       million acre-feet or more a year, delivered in winter -- which is what")
    print("       SGMA recharge is short of.")
    print()
    print("    WHAT THIS DOES NOT DO. It does not find the reservoir; head and site are")
    print("    ASSUMED bands. It does not net the evening peak, which hourly3 closes with")
    print("    the block, not the winter. It says which turbine the author's sentence")
    print("    can mean and returns a winter: the hydraulic one, at a capex under the")
    print("    field oversizing at both cases, conditional on head.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    check("rho.g.H in kWh/m3/m is 0.002725 (exact)", abs(RHO_G_KWH_M3_PER_M - 0.0027250) < 1e-6)
    check("1 acre-foot is 1,233.48 m3 (exact)", abs(M3_PER_AF - 1233.48) < 0.01)
    for c in CASES:
        tp = topping_per_m3(c)
        check(f"{c}: A returns less electricity than the same heat condensing (water is not free)",
              tp["e_returned"] < tp["e_condensing"])
        check(f"{c}: A makes water dearer than reverse osmosis in electricity",
              tp["cost_kwh_e_m3"] > tp["ro_kwh_e_m3"])
        hy = hydraulic_per_m3(c)
        check(f"{c}: B round trip equals turbine x pump efficiency exactly",
              abs(hy["round_trip"] - pick(ETA_TURBINE, c) * pick(ETA_PUMP, c)) < 1e-12)
    ws = {c: winter(c) for c in CASES}
    check("winter unserved is Nov-Feb of hourly3's own run (imported, not restated)",
          all(abs(ws[c]["unserved_twh"] - sum(ws[c]["run"]["month_unserved"][m] for m in WINTER_MONTHS) / 1e6) < 1e-12 for c in CASES))
    hy = {c: hydraulic_winter(c, ws[c]) for c in CASES}
    check("the whole winter needs more water than the surplus can make and lift (the requirement exceeds the bound)",
          all(hy[c]["requirement"]["summer_needed_twh"] > ws[c]["surplus_twh"] for c in CASES))
    check("the surplus-bounded scheme uses exactly the surplus",
          all(abs(hy[c]["bounded"]["summer_needed_twh"] - ws[c]["surplus_twh"]) < 1e-9 for c in CASES))
    check("critical returns a smaller share of the winter than mid", hy["critical"]["bounded"]["winter_share"] < hy["mid"]["bounded"]["winter_share"])
    check("the returned share is between a tenth and the whole", all(0.1 < hy[c]["bounded"]["winter_share"] < 1.0 for c in CASES))
    check("per TWh of winter, the water is cheaper than the mirrors at both cases",
          all(hy[c]["bounded"]["capex_b"] / hy[c]["bounded"]["returned_twh"] < field_closure_b(c) / ws[c]["unserved_twh"] for c in CASES))
    check("the bounded reservoir is a plausible size (0.1-3 km3, San Luis is 2.5)",
          all(0.1 < hy[c]["bounded"]["km3"] < 3.0 for c in CASES))
    check("energy returned = m3 x kWh/m3 exactly (no hidden term)",
          all(abs(hy[c]["requirement"]["m3"] * hy[c]["per"]["returned_kwh_m3"] / 1e9 - ws[c]["unserved_twh"]) < 1e-9 for c in CASES))
    for c in CASES:
        for h in HEAD_SCAN:
            m = modules_to_close(c, h, ws[c])
            check(f"{c} @ {h:.0f} m: the lift fits inside the surplus", m["lift_within_surplus"])
            check(f"{c} @ {h:.0f} m: returned energy = m3 x kWh/m3 exactly",
                  abs(m["m3"] * RHO_G_KWH_M3_PER_M * h * pick(ETA_TURBINE, c) / 1e9 - ws[c]["unserved_twh"]) < 1e-9)
    check("doubling the head halves the water at fixed winter (mid, 300 -> 600 m)",
          abs(modules_to_close("mid", 300.0, ws["mid"])["m3"] / modules_to_close("mid", 600.0, ws["mid"])["m3"] - 2.0) < 1e-9)
    check("at 500 m the modules that close mid are within the surplus and under the field oversizing",
          modules_to_close("mid", 500.0, ws["mid"])["capex_b"] < field_closure_b("mid"))
    head = open(__file__).read().split("def pick")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES", "WATER_END", "ETA_CONDENSING"))]
    check("every constant line carries a status",
          all(any(t in l for t in ("SOURCED", "ASSUMED", "exact", "Title II", "FLAWS")) for l in consts))
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report says the topping turbine does not return a winter", "DOES NOT RETURN A WINTER" in out)
    check("the report says head and site are assumed and it does not find the reservoir",
          "does not find the reservoir" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
