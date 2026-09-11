#!/usr/bin/env python3
"""titletwo.py -- Title II's process rows, each settled the way FLAWS.tsv
says it settles: a decision where the register asks for one, a computed
figure where it asks for one, at mid and at critical.

  F-03 / F-11  minerals. Lithium is three orders too small; magnesium is
               real and market-limited. Settled by counting NO mineral
               revenue in the water's price (aquacost.py does not), and by
               sizing the magnesium against the market so the reason is a
               number: one module's hydroxide against the US market.
  F-04 / F-12  ZLD and salt. The author dropped ZLD (2026-09-11): brine
               returns through the retired plant's permitted outfall at
               Ocean Plan concentration. Settled by computing what that
               takes -- the dilution a diffuser must achieve to hold the
               2 ppt limit at the mixing-zone edge with no cooling-water
               flow to dilute it, which a retired plant no longer has.
  F-13         LT-MED has no heat source. Settled by decision: seawater RO
               is the default (aquacost.py prices it); LT-MED only beside a
               named source of >= 500 MW_th per module, and none is named.
  F-15         24 months to first water. Settled by an honest schedule
               from the record -- Carlsbad proposed 1998, permitted 2006-12,
               water 2015; Huntington Beach 1998-2022, denied -- with the
               permitting band stated as assumed, and the cost of each year
               of it at the construction escalation.
  F-26         50 % of hours at cheap or negative price. Settled by pricing
               the energy at Title I's contract price full-time (aquacost.py)
               and computing how many hours of surplus Title I actually has
               (hourly3.py): the surplus is an upside, not a price.
  F-27         100 % on-site power. Settled by computing what a brownfield's
               acreage can host against what a module draws, and stating
               islanding as what it actually covers.
  F-28         slant wells. Settled by decision: a screened open intake
               through the retired plant's channel (1 mm wedge-wire at
               <= 0.5 ft/s, the Ocean Plan alternative and Carlsbad's path)
               is the default; slant wells where the hydrogeology permits;
               entrainment non-zero and mitigated under the Ocean Plan.
  F-35 / F-36  HPRO and citric CIP. Moot with ZLD and the mineral train gone;
               CIP waste neutralised and returned with the brine under the
               NPDES permit.

Every constant carries a status. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import heliocost as HC                                          # noqa: E402
import hourly3 as HR                                            # noqa: E402
import aquacost as AQ                                           # noqa: E402

CASES = ("mid", "critical")
# --- F-03 / F-11: minerals ------------------------------------------------------
MG_SEAWATER_MG_L = 1_290.0                # mg/L                                          SOURCED
LI_SEAWATER_MG_L = 0.18                   # mg/L                                          SOURCED
MG_OH2_PER_MG = 58.32 / 24.305            # kg Mg(OH)2 per kg Mg                          exact
US_MG_COMPOUNDS_KT_YR = (500.0, 300.0)    # US magnesium compounds market, kt/yr; critical = smaller market  ASSUMED band
RECOVERY = 0.50                           # RO recovery                                   SOURCED band 0.45-0.50
# --- F-04 / F-12: brine ----------------------------------------------------------
SEAWATER_PPT = 33.5                       # Pacific coastal salinity                      SOURCED
OCEAN_PLAN_LIMIT_PPT = 2.0                # above ambient at the mixing-zone edge         SOURCED (Ocean Plan 2015 amendment)
MIXING_ZONE_M = 100.0                     # brine mixing zone                             SOURCED
# --- F-15: schedule ------------------------------------------------------------------
CARLSBAD_YEARS = (1998, 2006, 2015)       # proposed, coastal permit, first water         SOURCED
HUNTINGTON_YEARS = (1998, 2022)           # proposed, denied                              SOURCED
PERMIT_YEARS = (5.0, 8.0)                 # permitting to a buildable permit, ASSUMED band from the record
PROGRAM_START = 2026                      # this year                                     exact
# --- F-27: on-site power ---------------------------------------------------------------
BROWNFIELD_ACRES = (80.0, 50.0)           # retired coastal plant footprint, nominal / critical  ASSUMED band
PV_W_PER_M2_DC = 40.0                     # ground-mount PV, DC per m2 of GROSS site (5-7 acres per MW)  SOURCED band 30-50
PV_CF_COASTAL = (0.22, 0.18)              # coastal, fixed-tilt, fog                       ASSUMED band
M2_PER_ACRE = 4046.86                     # exact
ISLANDING_CRITICAL_SHARE = 0.15           # intake, pretreatment, controls as a share of full load  ASSUMED
# --- F-28: intake ----------------------------------------------------------------------
INTAKE = ("screened open intake through the retired plant's channel, 1 mm wedge-wire at <= 0.5 ft/s "
          "(the Ocean Plan's alternative to subsurface intake), slant wells where per-site hydrogeology permits")


def minerals(case):
    ci = CASES.index(case)
    feed_m3 = AQ.MODULE_M3_YR / RECOVERY
    mg_t = feed_m3 * MG_SEAWATER_MG_L / 1e6 * 1e3 / 1e3            # tonnes Mg per module-year
    mgoh2_kt = mg_t * MG_OH2_PER_MG / 1e3
    li_t = feed_m3 * LI_SEAWATER_MG_L / 1e6
    return dict(mg_t=mg_t, mgoh2_kt=mgoh2_kt, market_kt=US_MG_COMPOUNDS_KT_YR[ci],
                share_of_market=mgoh2_kt / US_MG_COMPOUNDS_KT_YR[ci], li_t=li_t)


def brine():
    brine_ppt = SEAWATER_PPT / (1.0 - RECOVERY)          # salt conserved, water removed
    excess = brine_ppt - SEAWATER_PPT
    dilution = excess / OCEAN_PLAN_LIMIT_PPT              # seawater volumes per brine volume at the edge
    brine_m3 = AQ.MODULE_M3_YR                            # at 50 % recovery brine = product
    return dict(brine_ppt=brine_ppt, excess_ppt=excess, dilution=dilution, brine_m3_yr=brine_m3,
                dilution_m3_yr=dilution * brine_m3)


def schedule(case):
    ci = CASES.index(case)
    permit = PERMIT_YEARS[ci]
    first_water = PROGRAM_START + permit + AQ.BUILD_YEARS
    esc_m = AQ.module(case)["financed_m"] * HC.ESCALATION
    return dict(permit=permit, build=AQ.BUILD_YEARS, first_water=first_water,
                carlsbad=CARLSBAD_YEARS[2] - CARLSBAD_YEARS[0], carlsbad_permit=CARLSBAD_YEARS[1] - CARLSBAD_YEARS[0],
                huntington=HUNTINGTON_YEARS[1] - HUNTINGTON_YEARS[0], delay_m_per_year=esc_m)


def surplus_hours(case):
    r = HR.run(case)
    return dict(hours_full=r["hours_full"], share=r["hours_full"] / 8760.0, spill_twh_th=r["spill_th"] / 1e6)


def onsite(case):
    ci = CASES.index(case)
    need_mw = AQ.RO_KWH_M3[ci] * AQ.MODULE_M3_YR / 8760.0 / 1e3
    pv_dc = BROWNFIELD_ACRES[ci] * M2_PER_ACRE * PV_W_PER_M2_DC / 1e6
    pv_avg = pv_dc * PV_CF_COASTAL[ci]
    return dict(need_mw=need_mw, pv_dc_mw=pv_dc, pv_avg_mw=pv_avg, share=pv_avg / need_mw,
                islanding_mw=need_mw * ISLANDING_CRITICAL_SHARE)


def report():
    print()
    print("  TITLE II: THE PROCESS ROWS, SETTLED")
    print("  =====================================")
    print()
    print("    F-03 / F-11  MINERALS. No mineral revenue is in the water's price. Why, as a number:")
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    mm = {c: minerals(c) for c in CASES}
    for label, key, fmt in (("lithium per module-year, t", "li_t", "{:12.1f}"), ("magnesium per module-year, t", "mg_t", "{:12,.0f}"),
                            ("as Mg(OH)2, kt/yr", "mgoh2_kt", "{:12.0f}"), ("US magnesium-compounds market, kt/yr", "market_kt", "{:12.0f}"),
                            ("one module's share of that market", "share_of_market", "{:12.2f}")):
        print(f"      {label:<44}" + "".join(fmt.format(mm[c][key]) for c in CASES))
    print("          (F-11 counted the product volume; the brine carries the FEED's magnesium,")
    print("          twice that -- the correction runs against the revenue, not for it.)")
    print("          One module would be most of the whole US market or more than it; the")
    print("          water route's thirty-odd modules would be twenty to forty markets. A")
    print("          slipstream at a stated share is a possible line for one module and")
    print("          is not a program revenue. Lithium at a tonne a year is not a line.")
    print()
    print("    F-04 / F-12  BRINE. ZLD dropped (author, 2026-09-11); brine returns through")
    print("          the retired plant's outfall. What the Ocean Plan then requires:")
    b = brine()
    print(f"          brine at {RECOVERY:.0%} recovery       {b['brine_ppt']:.1f} ppt, {b['excess_ppt']:.1f} above ambient")
    print(f"          limit at the {MIXING_ZONE_M:.0f} m edge        {OCEAN_PLAN_LIMIT_PPT:.1f} ppt above ambient")
    print(f"          dilution the diffuser must achieve  {b['dilution']:.1f} : 1")
    print(f"          brine, M m3/yr per module           {b['brine_m3_yr'] / 1e6:.1f}; seawater entrained {b['dilution_m3_yr'] / 1e6:,.0f}")
    print("          A running power plant diluted its brine in cooling water; a retired one")
    print("          has none, so the dilution is the diffuser's alone -- multiport, high")
    print("          velocity, Carlsbad's post-2018 configuration. It is a design requirement")
    print("          on the outfall retrofit, priced in aquacost's outfall share.")
    print()
    print("    F-13  PROCESS. Seawater reverse osmosis is the default and is what aquacost")
    print("          prices. LT-MED only beside a named heat source of >= 500 MW_th per")
    print("          module; none is named on any coastal brownfield.")
    print()
    print("    F-15  SCHEDULE. The record: Carlsbad proposed 1998, coastal permit 2006,")
    sc = {c: schedule(c) for c in CASES}
    print(f"          water 2015 ({sc['mid']['carlsbad']} years, {sc['mid']['carlsbad_permit']} to a permit); Huntington Beach 1998-2022,")
    print(f"          denied ({sc['mid']['huntington']} years). Not 24 months. Stated honestly:")
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    for label, key, fmt in (("permitting, years (ASSUMED band from the record)", "permit", "{:12.0f}"), ("build, years", "build", "{:12.0f}"),
                            ("first water, starting now", "first_water", "{:12.0f}"), ("cost of each year of delay, $M per module", "delay_m_per_year", "{:12.0f}")):
        print(f"      {label:<44}" + "".join(fmt.format(sc[c][key]) for c in CASES))
    print("          A statutory consolidation with fixed clocks shortens the litigation,")
    print("          not the Coastal Commission's permit; the first module lands beside the")
    print("          water route's own need (2036-2041), which is the joinder's timing.")
    print()
    print("    F-26  ENERGY PRICE. The water's electricity is priced at Title I's contract")
    print("          price full-time (aquacost). Title I's actual surplus, hour by hour:")
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    sh = {c: surplus_hours(c) for c in CASES}
    for label, key, fmt in (("hours the store is full (surplus hours)", "hours_full", "{:12.0f}"), ("share of the year", "share", "{:12.1%}"),
                            ("field defocused, TWh_th", "spill_twh_th", "{:12.2f}")):
        print(f"      {label:<44}" + "".join(fmt.format(sh[c][key]) for c in CASES))
    print("          Seven percent of hours, not fifty; a membrane plant runs steadily and")
    print("          cannot live on them. The surplus is the water route's lift, an upside")
    print("          the price does not count.")
    print()
    print("    F-27  ON-SITE POWER. What a brownfield hosts against what a module draws:")
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    on = {c: onsite(c) for c in CASES}
    for label, key, fmt in (("module draw, MW average", "need_mw", "{:12.1f}"), ("site PV, MW_dc", "pv_dc_mw", "{:12.1f}"),
                            ("site PV, MW average", "pv_avg_mw", "{:12.1f}"), ("share of the draw", "share", "{:12.1%}"),
                            ("islanding: critical loads, MW", "islanding_mw", "{:12.1f}")):
        print(f"      {label:<44}" + "".join(fmt.format(on[c][key]) for c in CASES))
    print("          (the whole site given to PV, which the plant itself does not allow)")
    print("          On-site generation covers a tenth of the plant, not all of it; islanding")
    print("          is a battery for the intake, pretreatment and controls, so the plant")
    print("          rides through a grid outage without fouling, and restarts. Full-load")
    print("          islanding is not a claim this program makes.")
    print()
    print(f"    F-28  INTAKE. Decision: {INTAKE}.")
    print("          Entrainment is non-zero and is mitigated under the Ocean Plan, which is")
    print("          Carlsbad's path; 'eliminating 100 %' is withdrawn.")
    print()
    print("    F-35 / F-36  HPRO and citric CIP are moot with ZLD and the mineral train gone;")
    print("          CIP waste is neutralised and returned with the brine under the NPDES")
    print("          permit, as every coastal RO plant does.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    mm = {c: minerals(c) for c in CASES}
    check("one module's magnesium is a large share of the US market at both cases (not a program revenue)",
          all(mm[c]["share_of_market"] > 0.25 for c in CASES))
    check("the brine carries the FEED's magnesium: twice F-11's 79,600 t, which counted product volume (corrected here)",
          abs(mm["mid"]["mg_t"] - 2 * 79_600 * (1.0 / 0.5) / 2) / (2 * 79_600) < 0.02)
    check("lithium is tens of tonnes a year per module, not a revenue line", mm["mid"]["li_t"] < 50.0)
    b = brine()
    check("brine at 50 % recovery is twice seawater", abs(b["brine_ppt"] - 2 * SEAWATER_PPT) < 1e-9)
    check("the diffuser dilution is 15-20 : 1", 15.0 < b["dilution"] < 20.0)
    for c in CASES:
        sc = schedule(c)
        check(f"{c}: first water is eight or more years from now (the record, not 24 months)", sc["first_water"] - PROGRAM_START >= 8.0)
        on = onsite(c)
        check(f"{c}: on-site PV covers under a fifth of the module's draw", on["share"] < 0.2)
        sh = surplus_hours(c)
        check(f"{c}: Title I's surplus hours are under 15 % of the year (not 50 %)", sh["share"] < 0.15)
    check("critical permits take longer and its site hosts less", schedule("critical")["permit"] > schedule("mid")["permit"] and onsite("critical")["share"] < onsite("mid")["share"])
    head = open(__file__).read().split("def minerals")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES", "INTAKE"))]
    check("every constant line carries a status", all(any(t in l for t in ("SOURCED", "ASSUMED", "exact")) for l in consts))
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report withdraws 'eliminating 100 %' and 'full-load islanding'", "is withdrawn" in out and "not a claim this program makes" in out)
    check("the report says no mineral revenue is in the price", "No mineral revenue is in the water's price" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
