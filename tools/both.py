#!/usr/bin/env python3
"""both.py -- the author's decision on the season: BOTH routes.

Title III put two routes to the author for closing the October-April season
and the evening: mirrors (block x1.5, a second day of store, field x2) or
water (block x1.5 and Title II's product lifted on the summer surplus,
returned through pump-turbines). At parity on the power side. The author
(2026-09-11) answered "both".

Both means a combination, not a sum: the field and store are sized smaller
than the mirrors route and the water carries the rest of the season, so
neither lever is at its full extent and the plant is served by two things
that fail differently. This file scans the combination at mid and at
critical -- block held at x1.5 (nothing else serves a July evening), the
hydro plant at joinder.py's evening size, field factor, store days and the
SHARE of the season the water returns as the free axes -- and reports:

  1. a LADDER over the water's share of the season -- 0 (mirrors alone),
     1/4, 1/2, 3/4, 1 (water alone) -- each rung the cheapest closing point
     (<= 1 % to the grid) on Title I's account at that share;
  2. the resilience each rung buys: the same plant with the water withheld,
     and with the field at design, run through the hour-by-hour, so the
     reader sees what each route covers when the other is out;
  3. both routes in full -- the margin case -- and its cost.

"Both" is read as the EVEN split -- the water returns half the season and
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
BLOCK = 1.5                               # the evening; joinder.py section D and hourly3.py agree   DERIVED
HEAD_M = 500.0                            # the head Title III's table is stated at                    ASSUMED (joinder HEAD_SCAN)
FIELD_SCAN = (1.0, 1.25, 1.5, 1.75, 2.0)  # aperture factor                                          scan
STORE_SCAN = (1.0, 1.5, 2.0)              # days of the 16 h store                                   scan
WATER_SCAN = (0.0, 0.25, 0.5, 0.75, 1.0)  # share of the full water route's modules and lift          scan
HYDRO_MW_SCAN = (1000.0, 1500.0, 2500.0)  # pump-turbine plant; joinder's evening size is the top       scan
TARGET = 0.01                             # left to the grid, as joinder.py section D                 DERIVED
ADOPTED_SHARE = 0.5                       # "both": the even split, the author's word read literally    DECIDED (2026-09-11)


def water_side(case, share, w, mw=None):
    """Title I's water-side capital at a share of the full route, and Title II's modules."""
    ci = CASES.index(case)
    m = J.modules_to_close(case, HEAD_M, w)
    mw = J.pick(J.HYDRO_PLANT_MW, case) if mw is None else mw
    reservoir_b = m["reservoir_b"] * share
    pumpgen_b = mw * 1e3 * J.PUMPGEN_PER_KW[ci] / 1e9 if share > 0 else 0.0
    modules = m["modules"] * share
    return dict(share=share, modules=modules, maf=m["maf"] * share, mw=mw if share > 0 else 0.0,
                budget_twh=w["unserved_twh"] * share, lift_twh=m["lift_twh"] * share,
                reservoir_b=reservoir_b, pumpgen_b=pumpgen_b, title1_b=reservoir_b + pumpgen_b,
                title2_b=AQ.module(case, lift_kwh_m3=J.hydraulic_per_m3(case)["lift_kwh_m3"])["financed_m"] * modules / 1e3)


def point(case, field, store, share, w, d, mw=None):
    ws = water_side(case, share, w, mw)
    hydro = (ws["mw"], ws["budget_twh"]) if share > 0 else None
    r = HR.run(case, 1.0, 1.0, BLOCK, field, store, design=d, hydro=hydro)
    plant_b = HR.closure_cost_m(d, 1.0, 1.0, BLOCK, field, store) / 1e3
    surplus = (r["spill_th"] * d["links"]["cycle"] + r["pv_curtail"]) / 1e6
    return dict(field=field, store=store, share=share, mw=ws["mw"], unserved=1.0 - r["served_frac"],
                hydro_twh=r["hydro"] / 1e6, surplus_twh=surplus, lift_within_surplus=ws["lift_twh"] <= surplus,
                plant_b=plant_b, water_b=ws["title1_b"], title1_b=plant_b + ws["title1_b"],
                title2_b=ws["title2_b"], modules=ws["modules"], maf=ws["maf"], run=r)


_SCAN = {}


def scan(case):
    if case in _SCAN:
        return _SCAN[case]
    d = C.design("helios3", case)
    w = J.winter(case)
    pts = [point(case, f, s, x, w, d, mw) for f in FIELD_SCAN for s in STORE_SCAN for x in WATER_SCAN
           for mw in (HYDRO_MW_SCAN if x > 0 else (0.0,))]
    closing = [p for p in pts if p["unserved"] <= TARGET]
    ladder = {}
    for x in WATER_SCAN:
        rung = min([p for p in closing if p["share"] == x], key=lambda p: p["title1_b"], default=None)
        if rung:
            rung["dprice"] = price(case, rung["title1_b"])
            rung["no_water"] = point(case, rung["field"], rung["store"], 0.0, w, d)
            rung["no_field"] = point(case, 1.0, 1.0, x, w, d, rung["mw"])
        ladder[x] = rung
    best = ladder[ADOPTED_SHARE]
    mirrors, water = ladder[0.0], ladder[1.0]
    full = point(case, 2.0, 2.0, 1.0, w, d)
    as_sized = point(case, 1.0, 1.0, 0.0, w, d)
    _SCAN[case] = dict(points=pts, ladder=ladder, best=best, mirrors=mirrors, water=water, full=full,
                       as_sized=as_sized, winter=w, design=d)
    return _SCAN[case]


def price(case, title1_b):
    return J.price_delta(case, title1_b)


def report():
    print()
    print("  THE SEASON: BOTH ROUTES (the author's decision, 2026-09-11)")
    print("  ============================================================")
    print("    Block x1.5 held; field, store days and the water's share of the season")
    print("    scanned; cheapest closing point on Title I's account with both engaged.")
    S = {c: scan(c) for c in CASES}
    for c in CASES:
        print()
        print(f"    {c.upper()} -- the ladder over the water's share of the season (cheapest closing point at each rung):")
        print(f"      {'share':>6}{'field':>7}{'store d':>8}{'hydro MW':>9}{'grid':>6}{'Title I $B':>11}{'$/MWh':>7}{'modules':>8}{'MAF/yr':>7}{'water out':>10}{'field out':>10}")
        for x, r in S[c]["ladder"].items():
            if r is None:
                print(f"      {x:>6.2f}   (no closing point)")
                continue
            print(f"      {x:>6.2f}{r['field']:>7.2f}{r['store']:>8.1f}{r['mw']:>9,.0f}{r['unserved']:>6.1%}{r['title1_b']:>11.1f}{r['dprice']:>7.0f}"
                  f"{r['modules']:>8.1f}{r['maf']:>7.2f}{r['no_water']['unserved']:>10.1%}{r['no_field']['unserved']:>10.1%}")
        print(f"      as sized, no route: {S[c]['as_sized']['unserved']:.1%} to the grid")
    print()
    print(f"    ADOPTED: share {ADOPTED_SHARE:.2f} -- the even split, the author's 'both' read literally.")
    print(f"      {'':<46}{'mid':>12}{'critical':>12}")
    rows = (("field factor", lambda b: f"{b['field']:.2f}"), ("store, days", lambda b: f"{b['store']:.1f}"),
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
    print("      Both costs more than mirrors alone on Title I's account -- the pump-turbine plant is")
    print("      bought whole whatever share it returns -- and buys a plant served by two things that")
    print("      fail differently: with either route out it is still mostly served.")
    print()
    print("    Both in full (field x2, store 2 d, the whole water route) -- the margin case:")
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
        check(f"[{c}] both levers are engaged at the adopted rung", b["field"] > 1.0 and b["share"] == ADOPTED_SHARE)
        check(f"[{c}] it costs more than mirrors alone on Title I's account (the pump-turbines are bought whole)",
              b["title1_b"] > S[c]["mirrors"]["title1_b"])
        check(f"[{c}] with either route out the plant is better served than with neither",
              max(b["no_water"]["unserved"], b["no_field"]["unserved"]) < S[c]["as_sized"]["unserved"])
        check(f"[{c}] withholding the water leaves the plant short (the water is load-bearing)", b["no_water"]["unserved"] > TARGET)
        check(f"[{c}] the field at design leaves the plant short (the field is load-bearing)", b["no_field"]["unserved"] > TARGET)
        check(f"[{c}] the lift stays inside the surplus", b["lift_within_surplus"])
        check(f"[{c}] every rung of the ladder closes", all(r is not None for r in S[c]["ladder"].values()))
        check(f"[{c}] both in full closes and costs more than the adopted rung",
              S[c]["full"]["unserved"] <= TARGET and S[c]["full"]["title1_b"] > b["title1_b"])
    check("critical needs no less than mid on Title I's account", S["critical"]["best"]["title1_b"] >= S["mid"]["best"]["title1_b"])
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(0 if selftest() else 1) if a.selftest else report()
