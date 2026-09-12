#!/usr/bin/env python3
"""both.py -- the author's decision on the season: BOTH routes.

Title III put two routes to the author for closing the load (year-round, evening-led)
and the evening: mirrors (block x1.5, a second day of store, field x2) or
water (block x1.5 and Title II's product lifted on the summer surplus,
returned through pump-turbines). At parity on the power side. The author
(2026-09-11) answered "both".

Both means a combination, not a sum: the field and store are sized smaller
than the mirrors route and the water carries the rest of the shortfall, so
neither lever is at its full extent and the plant is served by two things
that fail differently. This file scans the combination at mid and at
critical -- block held at x1.5 (nothing else serves a July evening), the
hydro plant at joinder.py's evening size, field factor, store days and the
SHARE of the season the water returns as the free axes -- and reports:

  1. a LADDER over the water's share of the shortfall -- 0 (mirrors alone),
     1/4, 1/2, 3/4, 1 (water alone) -- each rung the cheapest closing point
     (<= 1 % to the grid) on Title I's account at that share;
  2. the resilience each rung buys: the same plant with the water withheld,
     and with the field at design, run through the hour-by-hour, so the
     reader sees what each route covers when the other is out;
  3. both routes in full -- the margin case -- and its cost.

"Both" is read as the EVEN split -- the water returns half the shortfall and
the field and store carry the other half -- because a cheapest-point search
with "both engaged" as its only constraint returns mirrors with a token
water plant, which is both in name. The even split is adopted here and the
ladder is printed so the author can move it; the split is the author's word,
not this file's optimum.

Costs are the routes' own: hourly3.closure_cost_m for the field, store and
block; joinder's reservoir per km3 and pump-generation per kW for the water;
the modules on Title II's account through aquacost. Stdlib only; runs
hourly3.py some fifty times per case (about a second each).
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cspchain as C                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402
import joinder as J                                             # noqa: E402
import aquacost as AQ                                           # noqa: E402

CASES = ("mid", "critical")
BLOCK_SCAN = (1.25, 1.5, 2.0)             # block factor; mirrors closes at 1.25, water alone at 2.0  scan
HEAD_M = 500.0                            # the head Title III's table is stated at                    ASSUMED (joinder HEAD_SCAN)
FIELD_SCAN = (1.0, 1.25, 1.5, 2.0)        # aperture factor                                          scan
STORE_SCAN = (1.0, 2.0)                   # days of the 16 h store                                   scan
WATER_SCAN = (0.0, 0.25, 0.5, 0.75, 1.0)  # share of the full water route's modules and lift          scan
HYDRO_MW_SCAN = (1500.0, 2500.0)          # pump-turbine plant; joinder's evening size is the top       scan
TARGET = 0.01                             # left to the grid, as joinder.py section D                 DERIVED
ADOPTED_SHARE = 0.5                       # "both": the even split, the author's word read literally    DECIDED (2026-09-11)


def water_side(case, share, w, mw=None):
    """Title I's water-side capital at a share of the full route, and Title II's modules."""
    ci = CASES.index(case)
    m = J.modules_to_close(case, HEAD_M, w, 1.0)
    mw = J.pick(J.HYDRO_PLANT_MW, case) if mw is None else mw
    reservoir_b = J.reservoir_capex_b(case, m["m3"] * share)
    pumpgen_b = mw * 1e3 * J.PUMPGEN_PER_KW[ci] / 1e9 if share > 0 else 0.0
    modules = m["modules"] * share
    water_b = reservoir_b + pumpgen_b
    return dict(share=share, modules=modules, maf=m["maf"] * share, mw=mw if share > 0 else 0.0,
                budget_twh=w["unserved_twh"] * share, lift_twh=m["lift_twh"] * share,
                reservoir_b=reservoir_b, pumpgen_b=pumpgen_b, title1_b=water_b,
                om_m=water_b * 1e3 * J.HYDRO_OM_SHARE[ci],
                title2_b=AQ.module(case, lift_kwh_m3=J.hydraulic_per_m3(case, HEAD_M)["lift_kwh_m3"])["financed_m"] * modules / 1e3)


def point(case, block, field, store, share, w, d, mw=None):
    ws = water_side(case, share, w, mw)
    hydro = (ws["mw"], ws["budget_twh"]) if share > 0 else None
    r = HR.run(case, 1.0, 1.0, block, field, store, design=d, hydro=hydro)
    plant_b = HR.closure_cost_m(d, 1.0, 1.0, block, field, store) / 1e3
    plant_om = HR.closure_om_m(d, plant_b * 1e3)
    surplus = (r["spill_th"] * d["links"]["cycle"] + r["pv_curtail"]) / 1e6
    return dict(block=block, field=field, store=store, share=share, mw=ws["mw"], unserved=1.0 - r["served_frac"],
                hydro_twh=r["hydro"] / 1e6, budget_twh=ws["budget_twh"], lift_twh=ws["lift_twh"],
                surplus_twh=surplus, lift_within_surplus=ws["lift_twh"] <= surplus,
                plant_b=plant_b, water_b=ws["title1_b"], title1_b=plant_b + ws["title1_b"],
                plant_om_m=plant_om, water_om_m=ws["om_m"], extra_om_m=plant_om + ws["om_m"],
                title2_b=ws["title2_b"], modules=ws["modules"], maf=ws["maf"], run=r)


_SCAN = {}


def scan(case):
    if case in _SCAN:
        return _SCAN[case]
    d = C.design("helios3", case)
    w = J.winter(case)
    pts = [point(case, b, f, s, x, w, d, mw) for b in BLOCK_SCAN for f in FIELD_SCAN for s in STORE_SCAN for x in WATER_SCAN
           for mw in (HYDRO_MW_SCAN if x > 0 else (0.0,))]
    closing = [p for p in pts if p["unserved"] <= TARGET and p["lift_within_surplus"]]     # a lift bought from the grid is not this route
    ladder = {}
    for x in WATER_SCAN:
        rung = min([p for p in closing if p["share"] == x], key=lambda p: p["title1_b"], default=None)
        if rung:
            rung["dprice"] = price(case, rung["title1_b"], rung["extra_om_m"])
            rung["no_water"] = point(case, rung["block"], rung["field"], rung["store"], 0.0, w, d)
            rung["no_field"] = point(case, rung["block"], 1.0, 1.0, x, w, d, rung["mw"])
        ladder[x] = rung
    best = ladder[ADOPTED_SHARE]
    mirrors, water = ladder[0.0], ladder[1.0]
    full = point(case, 2.0, 2.0, 2.0, 1.0, w, d)
    as_sized = point(case, 1.0, 1.0, 1.0, 0.0, w, d)
    _SCAN[case] = dict(points=pts, ladder=ladder, best=best, mirrors=mirrors, water=water, full=full,
                       as_sized=as_sized, winter=w, design=d)
    return _SCAN[case]


def price(case, title1_b, om_m=0.0):
    return J.price_delta(case, title1_b, om_m)


DAYS_SCAN = (14.0, 30.0, 60.0, 90.0)      # reservoir holding, days of delivery, for the sensitivity   scan


def sensitivity(case):
    """The two site assumptions the adopted point rests on -- the head and the reservoir's
    days of holding -- re-priced with the hourly run held fixed. At fixed share the water's
    RETURNED energy is what the run dispatched, so the volume goes as 1/head, the modules and
    Title II capital with it, the lift is invariant in head (returned energy over the round
    trip), and the reservoir goes as days x volume. Nothing here re-runs the hours."""
    b = scan(case)["best"]
    ci = CASES.index(case)
    w = scan(case)["winter"]
    rows = []
    for head in J.HEAD_SCAN:
        m = J.modules_to_close(case, head, w, b["share"])
        lift_fits = m["lift_twh"] <= b["surplus_twh"]
        for days in DAYS_SCAN:
            reservoir_b = m["m3"] * days / 365.0 / 1e9 * J.RESERVOIR_B_PER_KM3[ci]
            water_b = reservoir_b + b["mw"] * 1e3 * J.PUMPGEN_PER_KW[ci] / 1e9
            title1 = b["plant_b"] + water_b
            om = b["plant_om_m"] + water_b * 1e3 * J.HYDRO_OM_SHARE[ci]
            title2 = AQ.module(case, lift_kwh_m3=J.hydraulic_per_m3(case, head)["lift_kwh_m3"])["financed_m"] * m["modules"] / 1e3
            rows.append(dict(head=head, days=days, modules=m["modules"], maf=m["maf"], lift_twh=m["lift_twh"], lift_fits=lift_fits,
                             reservoir_b=reservoir_b, title1_b=title1, dprice=price(case, title1, om), title2_b=title2))
    return rows


def report():
    print()
    print("  THE SEASON: BOTH ROUTES (the author's decision, 2026-09-11)")
    print("  ============================================================")
    print("    Block, field, store days and the water's share of the shortfall scanned;")
    print("    cheapest closing point on Title I's account at each share of the shortfall.")
    S = {c: scan(c) for c in CASES}
    for c in CASES:
        print()
        print(f"    {c.upper()} -- the ladder over the water's share of the shortfall (cheapest closing point at each rung):")
        print(f"      {'share':>6}{'block':>7}{'field':>7}{'store d':>8}{'hydro MW':>9}{'grid':>6}{'Title I $B':>11}{'$/MWh':>7}{'modules':>8}{'MAF/yr':>7}{'water out':>10}{'field out':>10}")
        for x, r in S[c]["ladder"].items():
            if r is None:
                print(f"      {x:>6.2f}   (no closing point)")
                continue
            print(f"      {x:>6.2f}{r['block']:>7.2f}{r['field']:>7.2f}{r['store']:>8.1f}{r['mw']:>9,.0f}{r['unserved']:>6.1%}{r['title1_b']:>11.1f}{r['dprice']:>7.0f}"
                  f"{r['modules']:>8.1f}{r['maf']:>7.2f}{r['no_water']['unserved']:>10.1%}{r['no_field']['unserved']:>10.1%}")
        print(f"      as sized, no route: {S[c]['as_sized']['unserved']:.1%} to the grid")
    print()
    print(f"    ADOPTED: share {ADOPTED_SHARE:.2f} -- the even split, the author's 'both' read literally.")
    print(f"      {'':<46}{'mid':>12}{'critical':>12}")
    rows = (("block factor", lambda b: f"{b['block']:.2f}"), ("field factor", lambda b: f"{b['field']:.2f}"), ("store, days", lambda b: f"{b['store']:.1f}"),
            ("pump-turbine plant, MW", lambda b: f"{b['mw']:,.0f}"),
            ("Title II modules", lambda b: f"{b['modules']:.1f}"), ("water, MAF/yr", lambda b: f"{b['maf']:.2f}"),
            ("left to the grid", lambda b: f"{b['unserved']:.1%}"),
            ("hydro returned, TWh", lambda b: f"{b['hydro_twh']:.2f}"),
            ("lift inside the surplus", lambda b: "yes" if b["lift_within_surplus"] else "NO"),
            ("Title I plant additions, $B", lambda b: f"{b['plant_b']:.1f}"),
            ("Title I reservoir + pump-turbines, $B", lambda b: f"{b['water_b']:.1f}"),
            ("Title I total, $B", lambda b: f"{b['title1_b']:.1f}"),
            ("Title I price delta, $/MWh", lambda b: f"{b['dprice']:.0f}"),
            ("Title II modules' capital, $B", lambda b: f"{b['title2_b']:.0f}"),
            ("water withheld, to the grid", lambda b: f"{b['no_water']['unserved']:.1%}"),
            ("field at design, to the grid", lambda b: f"{b['no_field']['unserved']:.1%}"))
    for label, f in rows:
        print(f"      {label:<46}" + "".join(f"{f(S[c]['best']):>12}" for c in CASES))
    for c in CASES:
        print(f"      {c}: against mirrors alone, {S[c]['best']['title1_b'] / S[c]['mirrors']['title1_b']:.2f}x on Title I's account")
    print("      What the combination buys is a plant served by two things that fail differently:")
    print("      with either route out it is still mostly served.")
    print()
    print("    THE TWO SITE ASSUMPTIONS, AS A BAND (hourly run held; head moves the volume, days move the reservoir):")
    for c in CASES:
        print(f"      {c}:  {'head m':>7}{'days':>6}{'modules':>9}{'MAF/yr':>8}{'lift TWh':>10}{'fits':>6}{'reservoir $B':>14}{'Title I $B':>12}{'+$/MWh':>8}{'Title II $B':>13}")
        for r in sensitivity(c):
            print(f"           {r['head']:>7.0f}{r['days']:>6.0f}{r['modules']:>9.1f}{r['maf']:>8.2f}{r['lift_twh']:>10.2f}{'yes' if r['lift_fits'] else 'NO':>6}{r['reservoir_b']:>14.2f}{r['title1_b']:>12.1f}{r['dprice']:>8.0f}{r['title2_b']:>13.0f}")
    print("      The lift does not move with head; the modules halve when the head doubles; the reservoir is")
    print("      the only term the days touch. The head is the site question that sizes Title II.")
    print()
    print("    Both in full (block x2, field x2, store 2 d, the whole water route) -- the margin case:")
    for c in CASES:
        f = S[c]["full"]
        print(f"      {c:<10} {f['unserved']:.1%} to the grid, Title I {f['title1_b']:.1f} $B, surplus thrown away {f['surplus_twh']:.2f} TWh")
    print()
    print("    The combination is the author's: two levers that fail differently, neither at")
    print("    its full extent. Sized to close, it is priced; the margin case is printed and")
    print("    not adopted.")


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    S = {c: scan(c) for c in CASES}
    for c in CASES:
        b = S[c]["best"]
        check(f"[{c}] the adopted rung closes to the target", b is not None and b["unserved"] <= TARGET)
        if b is None:
            continue
        check(f"[{c}] both levers are engaged at the adopted rung", (b["field"] > 1.0 or b["store"] > 1.0) and b["share"] == ADOPTED_SHARE)
        check(f"[{c}] its cost against mirrors alone is within 0.5-2.5x (printed, not pinned in direction)",
              0.5 < b["title1_b"] / S[c]["mirrors"]["title1_b"] < 2.5)
        check(f"[{c}] with either route out the plant is better served than with neither",
              max(b["no_water"]["unserved"], b["no_field"]["unserved"]) < S[c]["as_sized"]["unserved"])
        check(f"[{c}] withholding the water leaves the plant short (the water is load-bearing)", b["no_water"]["unserved"] > TARGET)
        check(f"[{c}] the field and store at design leave the plant short (they are load-bearing)", b["no_field"]["unserved"] > TARGET)
        check(f"[{c}] the lift stays inside the surplus", b["lift_within_surplus"])
        check(f"[{c}] every rung of the ladder closes", all(r is not None for r in S[c]["ladder"].values()))
        check(f"[{c}] both in full closes and costs more than the adopted rung",
              S[c]["full"]["unserved"] <= TARGET and S[c]["full"]["title1_b"] > b["title1_b"])
    check("critical needs no less than mid on Title I's account", S["critical"]["best"]["title1_b"] >= S["mid"]["best"]["title1_b"])
    for c in CASES:
        sv = sensitivity(c)
        at = lambda h, d: next(r for r in sv if r["head"] == h and r["days"] == d)
        check(f"[{c}] the lift is invariant in head", abs(at(300.0, 30.0)["lift_twh"] - at(800.0, 30.0)["lift_twh"]) < 1e-9)
        check(f"[{c}] the modules scale as 1/head (300 -> 800 m is 8/3)", abs(at(300.0, 30.0)["modules"] / at(800.0, 30.0)["modules"] - 800.0 / 300.0) < 1e-9)
        check(f"[{c}] Title I cost rises with days of holding at fixed head", at(500.0, 90.0)["title1_b"] > at(500.0, 14.0)["title1_b"])
        check(f"[{c}] the adopted point is reproduced at 500 m and the design's days",
              abs(at(500.0, J.pick(J.RESERVOIR_DAYS, c))["title1_b"] - S[c]["best"]["title1_b"]) < 1e-9)
        check(f"[{c}] the lift fits at every head (the feasibility does not depend on the site)", all(r["lift_fits"] for r in sv))
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(0 if selftest() else 1) if a.selftest else report()
