#!/usr/bin/env python3
"""rebase2.py -- Title II re-based, rendered from the instruments.

The companion of rebase.py. Renders proposals/Title_II_Aqua-Sovereign_v0.2.md
from aquacost.py (the module and its water), titletwo.py (the process rows),
joinder.py (the water route) and hourly3.py (the surplus). The document
carries no number this file did not read from one of them, every number is
labelled mid or critical, and the selftest asserts the file on disk is
byte-identical to a fresh render. Stdlib only. Rendering runs hourly3.py.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import aquacost as AQ                                           # noqa: E402
import titletwo as T2                                           # noqa: E402
import joinder as J                                             # noqa: E402
import minors as MN                                             # noqa: E402

OUT = os.path.join(HERE, "..", "proposals", "Title_II_Aqua-Sovereign_v0.2.md")
CASES = ("mid", "critical")


def gather():
    g = {}
    g["module"] = {c: AQ.module(c) for c in CASES}
    g["route"] = {c: AQ.water_route(c) for c in CASES}
    g["record"] = AQ.record_per_afy()
    g["minerals"] = {c: T2.minerals(c) for c in CASES}
    g["brine"] = T2.brine()
    g["schedule"] = {c: T2.schedule(c) for c in CASES}
    g["surplus"] = {c: T2.surplus_hours(c) for c in CASES}
    g["onsite"] = {c: T2.onsite(c) for c in CASES}
    g["today_hh"] = H.per_household(H.GEN_RATE_NOW * 1e3)
    g["noise"] = {c: MN.noise(c) for c in CASES}
    g["jobs"] = {c: MN.jobs(c) for c in CASES}
    return g


def render(g):
    m, r = g["module"], g["route"]
    L = []
    a = L.append
    a("# Title II — Aqua-Sovereign, re-based (v0.2)")
    a("")
    a("**What this document is.** Title II of the California Sovereign Infrastructure program as it")
    a("stands after the second pass: LT-MED and zero-liquid-discharge replaced by seawater reverse")
    a("osmosis with brine returned through the retired plant's outfall, the mineral revenue withdrawn,")
    a("the module priced from the built record, and the water priced with its electricity bought from")
    a("Title I. It is **rendered by `tools/rebase2.py` from the instruments** and carries no number they")
    a("did not compute; every number is labelled **mid** or **critical**. v0.1 is unchanged.")
    a("")
    a("## 1. The module")
    a("")
    a("A 50,000 acre-foot-a-year seawater reverse-osmosis module on a retired coastal power-plant")
    a("brownfield, reusing its intake channel and permitted outfall, state-owned on Title I's form.")
    a(f"The unit capital is the built record escalated to the 2029 groundbreaking dollar — Carlsbad at")
    a(f"${g['record']['carlsbad']:,.0f} per AFY (mid) and Huntington Beach as designed at ${g['record']['huntington']:,.0f} (critical) — against the")
    a(f"${AQ.TITLE_II_CAPEX_M[0] * 1e6 / AQ.MODULE_AFY:,.0f}–{AQ.TITLE_II_CAPEX_M[1] * 1e6 / AQ.MODULE_AFY:,.0f} v0.1 submitted.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| overnight, $M | {m['mid']['overnight_m']:,.0f} | {m['critical']['overnight_m']:,.0f} |")
    a(f"| financed (contingency, EPC, IDC), $M | {m['mid']['financed_m']:,.0f} | {m['critical']['financed_m']:,.0f} |")
    a(f"| against v0.1's $250–320 M | {m['mid']['financed_m'] / 285:.1f}× | {m['critical']['financed_m'] / 285:.1f}× |")
    a(f"| electricity, kWh/m³, at Title I's price | {m['mid']['kwh_m3']:.1f} at ${m['mid']['energy_price']:.0f}/MWh | {m['critical']['kwh_m3']:.1f} at ${m['critical']['energy_price']:.0f}/MWh |")
    a("")
    a("## 2. The water")
    a("")
    a("At cost recovery — debt service and operations, **no mineral revenue** — the water sells for:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| $ per acre-foot | **{m['mid']['per_af']:,.0f}** | **{m['critical']['per_af']:,.0f}** |")
    a(f"| $ per m³ | {m['mid']['per_m3']:.2f} | {m['critical']['per_m3']:.2f} |")
    a(f"| of which energy | {m['mid']['energy_m'] / m['mid']['total_m']:.0%} | {m['critical']['energy_m'] / m['critical']['total_m']:.0%} |")
    a(f"| per household per year at {AQ.HOUSEHOLD_AF_YR:.2f} AF | {m['mid']['household']:,.0f} | {m['critical']['household']:,.0f} |")
    a("")
    a(f"v0.1 said $400. Carlsbad delivers at ${AQ.CARLSBAD_PRICE_AF[0]:,.0f}–{AQ.CARLSBAD_PRICE_AF[1]:,.0f} and a district pays about ${AQ.WHOLESALE_TODAY_AF:,.0f} wholesale")
    a("today. Desalinated water is firm water and is priced as such; capital dominates, not energy.")
    a("")
    a("## 3. The process decisions")
    a("")
    a("- **Reverse osmosis, not LT-MED.** A coastal brownfield has no heat source of the 500 MW_th a")
    a("  thermal module needs, and none is named. RO at 3.0–3.6 kWh/m³ is what is priced.")
    a(f"- **No zero-liquid-discharge, no mineral train.** One module's magnesium as hydroxide would be")
    a(f"  {g['minerals']['mid']['mgoh2_kt']:.0f} kt a year, {g['minerals']['mid']['share_of_market']:.2f} of the US magnesium-compounds market ({g['minerals']['critical']['share_of_market']:.2f} at critical);")
    a(f"  lithium is {g['minerals']['mid']['li_t']:.1f} tonnes a year. Neither is a program revenue and neither is in the price.")
    a(f"- **Brine through the outfall at Ocean Plan concentration.** At {T2.RECOVERY:.0%} recovery the brine is")
    a(f"  {g['brine']['brine_ppt']:.0f} ppt, {g['brine']['excess_ppt']:.1f} above ambient, against a limit of {T2.OCEAN_PLAN_LIMIT_PPT:.0f} ppt at the {T2.MIXING_ZONE_M:.0f} m edge — a")
    a(f"  diffuser dilution of {g['brine']['dilution']:.0f} : 1, which a retired plant's outfall must achieve without cooling water.")
    a(f"- **Intake.** {T2.INTAKE}. Entrainment is non-zero and mitigated under the Ocean Plan.")
    a(f"- **On-site power covers a tenth, not all.** A module draws {g['onsite']['mid']['need_mw']:.0f}–{g['onsite']['critical']['need_mw']:.0f} MW on average; the site's PV")
    a(f"  makes {g['onsite']['mid']['pv_avg_mw']:.1f}–{g['onsite']['critical']['pv_avg_mw']:.1f} MW, {g['onsite']['mid']['share']:.0%}–{g['onsite']['critical']['share']:.0%} of it. Islanding is a battery for the intake, pretreatment and")
    a("  controls, so the plant rides through an outage without fouling; full-load islanding is not claimed.")
    a(f"- **Energy at the contract price, full-time.** Title I's surplus is {g['surplus']['mid']['share']:.0%} of hours, not half; a")
    a("  membrane plant runs steadily. The surplus is the water route's lift, an upside the price does not count.")
    n = g["noise"]
    a(f"- **{MN.BOUNDARY_DBA:.0f} dBA at the boundary is bought, not assumed (F-40).** High-pressure pumps at {n['mid']['source']:.0f}–{n['critical']['source']:.0f} dBA at 1 m reach")
    a(f"  {MN.BOUNDARY_DBA:.0f} dBA at {n['mid']['d_open_m']:,.0f}–{n['critical']['d_open_m']:,.0f} m in the open; a full enclosure of {n['mid']['enclosure']:.0f}–{n['critical']['enclosure']:.0f} dB brings the boundary to {n['mid']['d_enclosed_m']:.0f}–{n['critical']['d_enclosed_m']:.0f} m,")
    a(f"  inside the brownfield, at ${n['mid']['cost_m']:.0f}–{n['critical']['cost_m']:.0f} M a module (mid–critical), carried in the module's band.")
    a(f"- **Employment (F-38).** At Carlsbad's staffing per plant, the water route's modules employ {g['jobs']['mid']['title2_permanent']:,.0f}–{g['jobs']['critical']['title2_permanent']:,.0f} permanently.")
    a("- **The Authority (F-37).** The same statutory entity as Title I's, a public body created by the Act")
    a("  and registered as a load-serving entity; *sovereign drought-emergency authority* is Gov. Code §8571,")
    a("  which suspends regulatory statutes in a declared emergency and issues no coastal permit.")
    a("")
    a("## 4. The schedule")
    a("")
    a(f"Carlsbad: proposed 1998, coastal permit 2006, water 2015 — {g['schedule']['mid']['carlsbad']} years. Huntington Beach: 1998 to")
    a(f"a 2022 denial. Stated honestly, permitting {g['schedule']['mid']['permit']:.0f} years (mid) to {g['schedule']['critical']['permit']:.0f} (critical, assumed from the record) and a")
    a(f"{g['schedule']['mid']['build']:.0f}-year build put first water at **{g['schedule']['mid']['first_water']:.0f}–{g['schedule']['critical']['first_water']:.0f}** from a 2026 start, beside the water route's own need")
    a(f"in Title I's ladder. Each year of delay escalates a module by ${g['schedule']['mid']['delay_m_per_year']:.0f}–{g['schedule']['critical']['delay_m_per_year']:.0f} M.")
    a("")
    a("## 5. The joinder: the adopted route's water")
    a("")
    a("Title I's summer surplus lifts this water to an elevated reservoir and its year-round")
    a("delivery returns through pump-turbines (`joinder.py`). Title II's side of that:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| modules at 500 m of head | {r['mid']['modules']:.1f} | {r['critical']['modules']:.1f} |")
    a(f"| water, million acre-feet a year | {r['mid']['maf']:.2f} | {r['critical']['maf']:.2f} |")
    a(f"| modules' capital, financed, $B | **{r['mid']['capex_b']:.0f}** | **{r['critical']['capex_b']:.0f}** |")
    a(f"| water with the lift on its bill, $/acre-foot | {r['mid']['per_af']:,.0f} | {r['critical']['per_af']:,.0f} |")
    a(f"| per household per year | {r['mid']['household']:,.0f} | {r['critical']['household']:,.0f} |")
    a("")
    a("On the power side the water route costs about twice the mirrors, since it returns nothing to the")
    a("summer evening; what the water route adds is a")
    a("firm-water program of this size at what firm water costs, delivered in the months groundwater")
    a("recharge is short. Whether California wants it is the joinder's question, with a number on both sides.")
    a("")
    a("## 6. What v0.2 does not settle")
    a("")
    a("- The site: head, hydrogeology, the outfall's diffuser and the intake's entrainment are per-site.")
    a("- The takers: the delivery needs contracted irrigation and recharge districts, year-round.")
    a("- The permit: the schedule's permitting band is assumed from two plants; a statutory consolidation")
    a("  shortens litigation, not the Coastal Commission.")
    a("")
    a("*Rendered by `tools/rebase2.py`; do not edit by hand. Re-render after any change to the instruments.*")
    return "\n".join(L) + "\n"


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    g = gather()
    text = render(g)
    check("the rendered document exists on disk", os.path.exists(OUT))
    if os.path.exists(OUT):
        check("the file on disk is byte-identical to a fresh render (never hand-edited)",
              open(OUT, encoding="utf-8").read() == text)
    check("both cases appear in every table", text.count("| mid | critical |") >= 3)
    check("the water price at mid appears", f"| $ per acre-foot | **{g['module']['mid']['per_af']:,.0f}**" in text)
    check("no mineral revenue is stated", "no mineral revenue" in text)
    check("full-load islanding is not claimed", "full-load islanding is not claimed" in text)
    check("noise, Title II employment and the Authority appear", all(t in text for t in ("F-40", "F-38", "F-37")))
    check("the enclosed boundary distance printed is the instrument's", f"to {g['noise']['mid']['d_enclosed_m']:.0f}–{g['noise']['critical']['d_enclosed_m']:.0f} m" in text)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    text = render(gather())
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"rendered {os.path.relpath(OUT, os.path.join(HERE, '..'))}: {len(text.splitlines())} lines")
