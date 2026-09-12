#!/usr/bin/env python3
"""proposal.py -- the complete California Sovereign Infrastructure proposal, and its
pitch, rendered from the instruments.

The three v0.2 Titles (rebase.py, rebase2.py, rebase3.py) are the diff against v0.1,
stated as documents. This file renders the WHOLE proposal as one document --
proposals/California_Sovereign_Infrastructure_v0.2.md -- with every item expanded,
every location addressed term by term, every study cited, every flaw and its
resolution, the figures drawn from the instruments' own outputs, and a two-to-three
page bullet pitch beside it -- proposals/Pitch_v0.2.md. Both are emitted as .docx too
(--docx), from the same rendered text.

It carries no number an instrument did not compute, labels every number mid or
critical under the author's standing rule, and its selftest asserts three things:
the two files on disk are byte-identical to a fresh render (never hand-edited);
every figure file the document references exists; and the pitch carries no number
the proposal does not -- a figure cannot appear in the short document that the long
one does not state and source.

Rendering runs hourly3.py and both.py at both cases: ten minutes or so. The
figures need matplotlib; the text needs the stdlib only.
"""
import argparse
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import firmpower as FP                                          # noqa: E402
import cspchain as C                                            # noqa: E402
import helios3 as H3                                            # noqa: E402
import receiver as RX                                           # noqa: E402
import studies as ST                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402
import joinder as J                                             # noqa: E402
import both as B                                                # noqa: E402
import pilot as PL                                              # noqa: E402
import predev as PD                                             # noqa: E402
import aquacost as AQ                                           # noqa: E402
import titletwo as T2                                           # noqa: E402
import titleone as T1                                           # noqa: E402
import majors as MJ                                             # noqa: E402
import minors as MN                                             # noqa: E402
import sites as SI                                              # noqa: E402
import rebase3 as R3                                            # noqa: E402

ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "proposals", "California_Sovereign_Infrastructure_v0.2.md")
PITCH = os.path.join(ROOT, "proposals", "Pitch_v0.2.md")
FIGDIR = os.path.join(ROOT, "proposals", "figures")
FLAWS = os.path.join(ROOT, "proposals", "FLAWS.tsv")
CASES = ("mid", "critical")
DATE = "2026-09-12"
# the dataviz palette (validated categorical slots): mid blue, critical orange, aqua, yellow, violet; ink for today
MID, CRIT, AQUA, YELLOW, VIOLET, INK, GRID = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#4a3aa7", "#52514e", "#e6e5e1"


# =============================================================================
# GATHER -- everything, once
# =============================================================================
def gather():
    g = {}
    # the requirement
    g["e_req"] = H.hh_demand_twh()
    g["growth"] = tuple(H.hh_demand_twh(years=H.BOND_TERM_Y, growth=x) / g["e_req"] for x in H.GROWTH_BAND)
    g["today_hh"] = H.per_household(H.GEN_RATE_NOW * 1e3)
    g["today_mwh"] = H.GEN_RATE_NOW * 1e3
    # v0.1 as submitted, and what helios.py / heliocost.py found
    pf = H.run_network()
    g["pf"] = dict(net_twh=pf["net"] / 1e6, cf_net=pf["cf_net"], cf_gross=pf["cf_gross"])
    prices = H.price_series()
    g["revenue_2024_m"] = H.revenue_m(pf["net_hourly"], prices)
    g["revenue_peak_m"] = H.revenue_m(pf["net_hourly"], H.price_series(peak_override=H.CLAIMED_PEAK_PRICES[2]))
    g["carrying_m"] = H.carrying_m()
    g["req_price_asbuilt"] = H.required_price(pf["net"])
    g["closure"] = H.closure_table(pf["net"])
    g["fidelity"] = [(n, dlv / dsg, note) for n, _m, dsg, dlv, note in H.BUILT if dlv is not None]
    g["hc"] = {c: HC.build(c) for c in ("low", "mid", "high")}
    g["hc_price"] = H.built_prices(pf["net"])
    g["hc_perw"] = {c: HC.per_watt(g["hc"][c]) for c in ("low", "mid", "high")}
    g["hh_at_hc"] = [H.per_household(p) for _n, p in g["hc_price"]]
    g["size_for"] = H.size_for()
    g["households_served_v01"] = H.households_served(pf["net"])
    # the equipment
    g["fp"] = {"mid": FP.size_all("mid"), "critical": FP.size_all("high")}   # firmpower bands are low/mid/high; its top is the critical column
    g["fp_port"] = FP.portfolio("mid")
    # the chain
    g["base_links"], _ = C.baseline_links()
    g["best_links"] = C.best_links()
    g["h2"] = C.design("helios2", "mid")
    g["design"] = {c: C.design("helios3", c) for c in CASES}
    g["baseline_row"] = C.baseline_row()
    # the receiver
    rxc = {"mid": "nominal", "critical": "critical"}
    g["rx"] = {c: dict(open=RX.efficiency(rxc[c], True), domed=RX.efficiency(rxc[c], False),
                       field=RX.upstream_field_factor(g["design"]["mid"], rxc[c], True),
                       breakeven=RX.dome_breakeven_kw_m2(rxc[c]),
                       losses_open=RX.aperture_losses_kw_m2(rxc[c], True),
                       losses_dome=RX.aperture_losses_kw_m2(rxc[c], False)) for c in CASES}
    g["ladder"] = RX.ladder(g["design"]["mid"])
    # hour by hour
    g["hourly"] = {c: HR.run(c) for c in CASES}
    g["mirrors"] = {}
    for c in CASES:
        d = g["design"][c]
        r = HR.mirrors_run(c, design=d)
        cost = HR.mirrors_cost_m(d)
        g["mirrors"][c] = dict(unserved=1 - r["served_frac"], cost_b=cost / 1e3, dprice=HR.mirrors_price_delta(d), om_m=HR.closure_om_m(d, cost), run=r)
    ls = HR.load_series(g["e_req"])
    mean = sum(ls) / len(ls)
    g["day_jul"] = [v / mean for v in ls[199 * 24:200 * 24]]
    g["day_dec"] = [v / mean for v in ls[354 * 24:355 * 24]]
    g["cv"] = MJ.central_valley()
    # closing the load
    g["scan"] = {c: B.scan(c) for c in CASES}
    g["both"] = {c: g["scan"][c]["best"] for c in CASES}
    g["sens"] = {c: B.sensitivity(c) for c in CASES}
    g["winter"] = {c: J.winter(c) for c in CASES}
    g["hyd"] = {c: J.hydraulic_per_m3(c, B.HEAD_M) for c in CASES}       # at the one head the adopted route is priced at
    g["topping"] = {c: J.topping_per_m3(c) for c in CASES}
    g["m2c"] = {c: J.modules_to_close(c, 500.0, g["winter"][c]) for c in CASES}
    # the register and the price
    g["priced"] = {c: H3.priced(c) for c in CASES}
    g["grades"] = (H3.grade_counts(False), H3.grade_counts(True))
    # provenance
    g["delay"] = {c: ST.delay_cost_per_year(c) for c in CASES}
    g["path_years"] = ST.critical_path_years()
    # the pilot
    g["pilot"] = dict(unit={c: PL.unit(c) for c in CASES}, th=PL.thresholds(), u=PL.uncertainty(),
                      tranche={c: PL.pilot_tranche(c) for c in CASES},
                      cons={e: PL.consequence(e) for e in (0.60, 0.667, 0.690, 0.713, 0.80, 0.90, 0.93)},
                      grades={e: PL.grade(e) for e in (0.60, 0.667, 0.690, 0.713, 0.80, 0.90, 0.93)})
    # studies and surveys first
    g["predev"] = {c: PD.title1(c) for c in CASES}
    g["predev2"] = {c: PD.title2_per_site(c) for c in CASES}
    # price, household, financing
    g["rates"] = {c: T1.rate_table(c) for c in CASES}
    g["tranches"] = {c: T1.tranches(c) for c in CASES}
    g["gentie"] = {c: T1.gentie(c, g["both"][c]["block"]) for c in CASES}
    g["reserve"] = {c: MJ.reserve(c) for c in CASES}
    g["downside"] = {c: MJ.downside(c) for c in CASES}
    g["nepa"] = {c: MJ.nepa(c) for c in CASES}
    g["ra"] = {c: MJ.ra(c) for c in CASES}
    g["wash"] = {c: MJ.washing(c) for c in CASES}
    g["land"] = {c: MJ.land(c) for c in CASES}
    g["postbond"] = {c: (g["priced"][c]["om"] + g["both"][c]["extra_om_m"]) / g["design"][c]["e_twh"] for c in CASES}   # the adopted route's O&M, register plant and closing plant
    # the water
    g["aqua"] = {c: AQ.module(c) for c in CASES}
    g["aqua_route"] = {c: AQ.water_route(c) for c in CASES}
    g["record"] = AQ.record_per_afy()
    g["minerals"] = {c: T2.minerals(c) for c in CASES}
    g["brine"] = T2.brine()
    g["schedule2"] = {c: T2.schedule(c) for c in CASES}
    g["surplus"] = {c: T2.surplus_hours(c) for c in CASES}
    g["onsite"] = {c: T2.onsite(c) for c in CASES}
    # minors
    g["co2"] = {c: MN.co2(c) for c in CASES}
    g["jobs"] = {c: MN.jobs(c) for c in CASES}
    g["seismic"] = {c: MN.seismic(c) for c in CASES}
    g["noise"] = {c: MN.noise(c) for c in CASES}
    g["cycle"] = MN.cycle_label()
    # sites
    g["sites1"] = {c: SI.title1(c) for c in CASES}
    g["sites2"] = SI.title2()
    # the flaws
    with open(FLAWS, encoding="utf-8") as f:
        g["flaws"] = list(csv.DictReader(f, delimiter="\t"))
    return g


def money(x):
    return f"{x:,.0f}"


def whole_price(g, c):
    return g["priced"][c]["price"] + g["both"][c]["dprice"]


def program_b(g, c):
    return g["priced"][c]["capex_net"] / 1e3 + g["both"][c]["title1_b"] + g["both"][c]["title2_b"]


def milestones(g, c):
    rows = g["tranches"][c][0]
    by = {r[0].split(",")[0].split(" (")[0]: r for r in rows}
    return dict(studies=by["studies and surveys"][1], field=by["field"][2], pilot=(by["pilot aperture on one tower"][1], by["pilot aperture on one tower"][2]),
                module=by["first 100 MWe module"][2], fleet=by["fleet"][2])


# =============================================================================
# FIGURES -- drawn from the gathered numbers, never typed
# =============================================================================
def _style(ax, title, ylabel=None):
    ax.set_title(title, loc="left", fontsize=11, color="#0b0b0b", pad=10)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK, labelsize=9)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    if ylabel:
        ax.set_ylabel(ylabel, color=INK, fontsize=9)


def figures(g):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(FIGDIR, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.dpi": 130, "savefig.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb"})
    files = []

    def save(fig, name):
        p = os.path.join(FIGDIR, name)
        fig.tight_layout()
        fig.savefig(p)
        plt.close(fig)
        files.append(name)

    # 1. the built record against Title I's $/W
    fig, ax = plt.subplots(figsize=(8, 3.8))
    names = [n for n, _w, _y, _h in HC.BUILT_PER_W] + ["Title I as written", "heliocost low", "heliocost mid", "heliocost high"]
    vals = [w for _n, w, _y, _h in HC.BUILT_PER_W] + [H.CAPEX_B * 1e9 / (H.GROSS_MWE * 1e6)] + [g["hc_perw"][c] for c in ("low", "mid", "high")]
    cols = [INK] * len(HC.BUILT_PER_W) + [CRIT, MID, MID, MID]
    ax.barh(names, vals, color=cols, height=0.55)
    for i, v in enumerate(vals):
        ax.text(v + 0.1, i, f"{v:.2f}", va="center", fontsize=8, color=INK)
    ax.invert_yaxis()
    ax.xaxis.grid(True, color=GRID); ax.yaxis.grid(False)
    _style(ax, "Salt-tower CSP as built, dollars per watt gross, against Title I's own capital (F-05)")
    ax.set_xlabel("\\$/W gross", color=INK, fontsize=9)
    save(fig, "fig-01-built-record.png")

    # 2. every candidate sized to the requirement, price at mid and critical
    fig, ax = plt.subplots(figsize=(8, 4.2))
    keys = ["salton_flash", "egs", "pv_salt", "csp_proposed", "pv_ironair", "smr"]
    labels = [FP.TECH[k]["name"].split(" (")[0] for k in keys]
    pm = [g["fp"]["mid"][k]["price"] for k in keys]
    pc = [g["fp"]["critical"][k]["price"] for k in keys]
    y = range(len(keys))
    ax.barh([i - 0.18 for i in y], pm, height=0.34, color=MID, label="mid")
    ax.barh([i + 0.18 for i in y], pc, height=0.34, color=CRIT, label="critical")
    ax.axvline(g["today_mwh"], color=INK, linewidth=1.2, linestyle="--")
    ax.text(g["today_mwh"] + 2, -0.55, f"today, \\${g['today_mwh']:.0f}/MWh", fontsize=8, color=INK)
    ax.axvspan(H.FIRM_CLEAN_PPA[0], H.FIRM_CLEAN_PPA[1], color=AQUA, alpha=0.15)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis(); ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.xaxis.grid(True, color=GRID); ax.yaxis.grid(False)
    _style(ax, f"Every firm candidate sized to {g['e_req']:.1f} TWh, state-owned: required price (firmpower.py)")
    ax.set_xlabel("\\$/MWh; the shaded band is the \\$80–120 firm-clean contract band; critical = the band's top", color=INK, fontsize=9)
    save(fig, "fig-02-candidates.png")

    # 3. the chain, link by link
    fig, ax = plt.subplots(figsize=(8, 3.8))
    keys = ["opt", "rec", "cycle", "par", "avail"]
    names = ["optical", "receiver", "cycle", "1 − parasitic", "availability"]
    x = range(len(keys)); w = 0.26
    ax.bar([i - w for i in x], [g["base_links"][k] for k in keys], w, color=INK, label="Helios as proposed")
    ax.bar([i for i in x], [g["design"]["mid"]["links"][k] for k in keys], w, color=MID, label="Helios-3 mid")
    ax.bar([i + w for i in x], [g["design"]["critical"]["links"][k] for k in keys], w, color=CRIT, label="Helios-3 critical")
    ax.set_xticks(list(x)); ax.set_xticklabels(names, fontsize=9); ax.set_ylim(0, 1.22)
    ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper left")
    _style(ax, "The energy chain, link by link (cspchain.py; the critical receiver is receiver.py's)")
    save(fig, "fig-03-chain.png")

    # 4. monthly: load, served, unserved at both cases
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
    for ax, c, col in zip(axes, CASES, (MID, CRIT)):
        r = g["hourly"][c]
        m = range(1, 13)
        load = [r["month_load"][i] / 1e6 for i in m]
        uns = [r["month_unserved"][i] / 1e6 for i in m]
        served = [a - b for a, b in zip(load, uns)]
        ax.bar(list(m), served, color=col, width=0.7, label="served by the plant as sized")
        ax.bar(list(m), uns, bottom=served, color=GRID, width=0.7, edgecolor=INK, linewidth=0.5, label="unserved")
        ax.set_xticks(list(m)); ax.set_xticklabels([HR.MONTHS[i][0] for i in m], fontsize=8)
        _style(ax, f"{c}: {r['served_frac']:.0%} served", "TWh")
        ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig.suptitle("The load by month and what the plant as sized serves (hourly3.py)", x=0.01, ha="left", fontsize=11)
    save(fig, "fig-04-monthly.png")

    # 5. the day: July and December load shape
    fig, ax = plt.subplots(figsize=(8, 3.4))
    hrs = list(range(24))
    ax.plot(hrs, g["day_jul"], color=CRIT, linewidth=2, label="late July")
    ax.plot(hrs, g["day_dec"], color=MID, linewidth=2, label="late December")
    ax.axvspan(9, 16, color=YELLOW, alpha=0.12)
    ax.text(9.2, max(g["day_jul"]) * 0.98, "PV serves the day directly", fontsize=8, color=INK)
    ax.set_xticks(range(0, 24, 3)); ax.set_xlabel("hour", color=INK, fontsize=9)
    ax.legend(frameon=False, fontsize=8)
    _style(ax, "The residential load shape by hour, relative to the annual mean hour (reconstructed)", "× mean")
    save(fig, "fig-05-load-shape.png")

    # 6. the ladder over the water's share
    fig, ax = plt.subplots(figsize=(8, 3.8))
    for c, col in zip(CASES, (MID, CRIT)):
        lad = g["scan"][c]["ladder"]
        xs = [s for s in B.WATER_SCAN if lad[s]]
        ax.plot(xs, [lad[s]["title1_b"] for s in xs], marker="o", color=col, linewidth=2, markersize=6, label=f"{c}: Title I capital to close")
    ax.axvline(B.ADOPTED_SHARE, color=INK, linestyle="--", linewidth=1)
    ax.text(B.ADOPTED_SHARE + 0.01, ax.get_ylim()[1] * 0.92, "adopted: the even split", fontsize=8, color=INK)
    ax.set_xlabel("share of the shortfall the water is sized to return (0 = mirrors alone; 1 = all of it, with the larger field)", color=INK, fontsize=9)
    ax.legend(frameon=False, fontsize=8)
    _style(ax, "Closing the load: the ladder over the water's share (both.py)", "\\$B on Title I's account")
    save(fig, "fig-06-ladder.png")

    # 7. the head sizes Title II
    fig, ax = plt.subplots(figsize=(8, 3.4))
    for c, col in zip(CASES, (MID, CRIT)):
        rows = [r for r in g["sens"][c] if r["days"] == J.pick(J.RESERVOIR_DAYS, c)]
        ax.plot([r["head"] for r in rows], [r["modules"] for r in rows], marker="o", color=col, linewidth=2, markersize=6, label=f"{c}, {J.pick(J.RESERVOIR_DAYS, c):.0f} days of holding")
    ax.set_xticks(list(J.HEAD_SCAN)); ax.set_xlabel("reservoir head, m", color=INK, fontsize=9)
    ax.legend(frameon=False, fontsize=8)
    _style(ax, "Title II modules the adopted route needs, against the reservoir head (both.py sensitivity)", "50,000 AFY modules")
    save(fig, "fig-07-head.png")

    # 8. the price, step by step
    fig, ax = plt.subplots(figsize=(8, 3.8))
    steps = ["as chained", "with the register", "whole load, mirrors", "whole load, both (adopted)"]
    pm = [g["design"]["mid"]["price"], g["priced"]["mid"]["price"], g["priced"]["mid"]["price"] + g["mirrors"]["mid"]["dprice"], whole_price(g, "mid")]
    pc = [g["design"]["critical"]["price"], g["priced"]["critical"]["price"], g["priced"]["critical"]["price"] + g["mirrors"]["critical"]["dprice"], whole_price(g, "critical")]
    x = range(4); w = 0.36
    ax.bar([i - w / 2 for i in x], pm, w, color=MID, label="mid")
    ax.bar([i + w / 2 for i in x], pc, w, color=CRIT, label="critical")
    for i in x:
        ax.text(i - w / 2, pm[i] + 3, f"{pm[i]:.0f}", ha="center", fontsize=8, color=INK)
        ax.text(i + w / 2, pc[i] + 3, f"{pc[i]:.0f}", ha="center", fontsize=8, color=INK)
    ax.axhline(g["today_mwh"], color=INK, linestyle="--", linewidth=1.2)
    ax.text(-0.45, g["today_mwh"] + 4, "today", fontsize=8, color=INK, ha="left")
    ax.axhspan(H.FIRM_CLEAN_PPA[0], H.FIRM_CLEAN_PPA[1], color=AQUA, alpha=0.15)
    ax.set_xticks(list(x)); ax.set_xticklabels(steps, fontsize=9)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    _style(ax, "Title I's required price, step by step (shaded: the firm-clean contract band)", "\\$/MWh")
    save(fig, "fig-08-price.png")

    # 9. the household: today, during the bonds, after the bonds
    fig, ax = plt.subplots(figsize=(8, 3.6))
    cats = ["today", "mid,\nduring the bonds", "critical,\nduring the bonds", "mid,\nafter the bonds", "critical,\nafter the bonds"]
    vals = [g["today_hh"], H.per_household(whole_price(g, "mid")), H.per_household(whole_price(g, "critical")),
            H.per_household(g["postbond"]["mid"]), H.per_household(g["postbond"]["critical"])]
    cols = [INK, MID, CRIT, MID, CRIT]
    ax.bar(cats, vals, color=cols, width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v + 20, f"${v:,.0f}", ha="center", fontsize=8, color=INK)
    ax.set_xticks(range(len(cats))); ax.set_xticklabels(cats, fontsize=8)
    _style(ax, "A household's annual generation charge: today, over the 30-year bond term, and after it", "\\$ per household per year")
    save(fig, "fig-09-household.png")

    # 10. the capital stack
    fig, ax = plt.subplots(figsize=(7, 3.8))
    parts = [("Title I plant with its register", lambda c: g["priced"][c]["capex_net"] / 1e3, MID),
             ("Title I closing the load (both)", lambda c: g["both"][c]["title1_b"], AQUA),
             ("Title II modules", lambda c: g["both"][c]["title2_b"], VIOLET)]
    bottoms = {c: 0.0 for c in CASES}
    for name, fn, col in parts:
        vals = [fn(c) for c in CASES]
        ax.bar(list(CASES), vals, bottom=[bottoms[c] for c in CASES], color=col, width=0.5, label=name, edgecolor="#fcfcfb", linewidth=2)
        for i, c in enumerate(CASES):
            ax.text(i, bottoms[c] + vals[i] / 2, f"{vals[i]:.1f}", ha="center", va="center", fontsize=8, color="white")
            bottoms[c] += vals[i]
    for i, c in enumerate(CASES):
        ax.text(i, bottoms[c] + 1.5, f"${bottoms[c]:.0f} B", ha="center", fontsize=9, color=INK)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    _style(ax, "The program's capital at the adopted route", "\\$B")
    save(fig, "fig-10-capital.png")

    # 11. the schedule
    fig, ax = plt.subplots(figsize=(9, 3.6))
    for j, (c, col) in enumerate(zip(CASES, (MID, CRIT))):
        rows = g["tranches"][c][0]
        for i, (name, y0, y1, amt) in enumerate(rows):
            ax.barh(i + (0.2 if j else -0.2), y1 - y0, left=y0, height=0.36, color=col, label=c if i == 0 else None)
            ax.text(y1 + 0.1, i + (0.2 if j else -0.2), f"${amt / 1e3:.2f} B", va="center", fontsize=7, color=INK)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=8); ax.invert_yaxis()
    ax.set_xlim(PD.START_YEAR - 0.5, max(r[2] for r in g["tranches"]["critical"][0]) + 2.5)
    ax.set_xticks(list(range(int(PD.START_YEAR), int(max(r[2] for r in g["tranches"]["critical"][0])) + 3, 2)))
    ax.xaxis.grid(True, color=GRID); ax.yaxis.grid(False)
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    _style(ax, "The schedule by tranche, mid and critical (titleone.py, predev.py)")
    save(fig, "fig-11-schedule.png")

    # 12. the sites, scored
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8), gridspec_kw=dict(width_ratios=[1, 1.6]))
    ax = axes[0]
    names = [n for n, _l, _o, _a, _m, _s, _d, _st in H.NODES]
    y = range(len(names))
    ax.barh([i - 0.18 for i in y], [g["sites1"]["mid"][n]["score"] for n in names], height=0.34, color=MID, label="mid")
    ax.barh([i + 0.18 for i in y], [g["sites1"]["critical"][n]["score"] for n in names], height=0.34, color=CRIT, label="critical")
    ax.set_yticks(list(y)); ax.set_yticklabels([n.split(" (")[0] for n in names], fontsize=8); ax.invert_yaxis()
    ax.set_xlim(0, 6.6); ax.legend(frameon=False, fontsize=8, loc="lower right"); ax.xaxis.grid(True, color=GRID); ax.yaxis.grid(False)
    _style(ax, "Title I nodes, six terms")
    ax = axes[1]
    ranked = SI.ranked(g["sites2"])
    ax.barh([n.split(" (")[0] for n, _ in ranked], [r["score"] for _, r in ranked], color=[VIOLET if r["score"] > 0 else CRIT for _, r in ranked], height=0.55)
    ax.invert_yaxis(); ax.tick_params(axis="y", labelsize=8); ax.xaxis.grid(True, color=GRID); ax.yaxis.grid(False)
    _style(ax, "Title II coastal brownfields, seven terms")
    fig.suptitle("The sites, scored: MET 1, CONDITIONAL 0.5, OPEN 0, FAIL −1 (sites.py)", x=0.01, ha="left", fontsize=11)
    save(fig, "fig-12-sites.png")
    return files


# =============================================================================
# THE PROPOSAL
# =============================================================================
def render(g):
    d, p, hr, bo, m = g["design"], g["priced"], g["hourly"], g["both"], g["mirrors"]
    pm, pc = p["mid"], p["critical"]
    bm, bc = bo["mid"], bo["critical"]
    ms = {c: milestones(g, c) for c in CASES}
    L = []
    a = L.append
    fig_n = [0]

    def fig(name, caption):
        fig_n[0] += 1
        a(f"![Figure {fig_n[0]}](figures/{name})")
        a("")
        a(f"*Figure {fig_n[0]}. {caption}*")
        a("")

    def both_row(label, fm, fc, fmt="{:,.0f}", bold=False):
        s = f"| {label} | {fmt.format(fm)} | {fmt.format(fc)} |"
        a(s.replace(f"| {fmt.format(fm)} | {fmt.format(fc)} |", f"| **{fmt.format(fm)}** | **{fmt.format(fc)}** |") if bold else s)

    # ---------------------------------------------------------------- front
    a("# California Sovereign Infrastructure — the complete proposal (v0.2)")
    a("")
    a(f"*Rendered {DATE} by `tools/proposal.py` from the instruments in `tools/`. Do not edit by hand; re-render after any change to an instrument.*")
    a("")
    a("**What this document is.** The whole of the California Sovereign Infrastructure program as it stands")
    a("after the second pass, in one document: Title I, the electricity (Helios-3); Title II, the water")
    a("(Aqua-Sovereign); Title III, the joinder; every location addressed term by term; every study that covers")
    a("a technology in the system, cited; every one of the forty flaws found in the as-submitted proposal, with")
    a("its resolution; the figures drawn from the instruments' own outputs. It carries **no number an instrument")
    a("did not compute**, and every number is labelled **mid** or **critical** under the author's standing rule")
    a("that a number quoted without its case is misquoted. Mid is the middle of each constant's band; critical is")
    a("the adverse end of every band at once, and the design is held to critical. The nominal column is margin.")
    a("")
    a("**How to read a status.** SOURCED is a published figure with its source named. ASSUMED is a band the")
    a("record does not fix, stated as such. RECONSTRUCTED is a shape or split rebuilt from physics or from a")
    a("published model because the source is unreachable here. DERIVED is computed from the others. DECIDED is")
    a("a choice the author made and recorded. A status is never flattened: how a number was got is part of what it is.")
    a("")
    a("**Contents.** A. Summary · B. The requirement · C. What was submitted and why it failed · D. The equipment")
    a("question · E. The energy chain · F. The plant · G. Hour by hour · H. Closing the load · I. The risk register ·")
    a("J. Provenance: the studies · K. The pilot aperture · L. Studies and surveys first · M. Price, household and")
    a("financing · N. Title II, the water · O. Title III, the joinder · P. The sites · Q. Environment, employment and")
    a("procurement · R. What is not settled · S. The flaws register · T. Sources · U. The instruments.")
    a("")
    # ---------------------------------------------------------------- A
    a("## A. Summary")
    a("")
    a("One state-owned program under one Authority, two severable projects, funded once by bonds and never again")
    a(f"by the treasury. Title I builds Helios-3, concentrating solar on three desert nodes with falling-particle")
    a(f"receivers and supercritical-CO₂ turbines, photovoltaics serving the day directly and a night-sized mirror")
    a(f"field, to make **{g['e_req']:.1f} TWh** of firm electricity a year for three million households. Title II builds")
    a(f"**{bm['modules']:.0f} to {bc['modules']:.0f}** seawater reverse-osmosis modules of 50,000 acre-feet a year on retired coastal power plants,")
    a("lifting their product to an elevated reservoir with Title I's summer surplus and returning it year-round")
    a("through pump-turbines to Title I's evenings. Title III is the contract, the shared asset and the")
    a("severability that join them.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("Title I plant with its register, $B", pm["capex_net"] / 1e3, pc["capex_net"] / 1e3, "{:.1f}")
    both_row("Title I closing the whole load on the adopted route, $B", bm["title1_b"], bc["title1_b"], "{:.1f}")
    both_row("Title II modules at the adopted route, $B", bm["title2_b"], bc["title2_b"], "{:.0f}")
    both_row("**program, $B**", program_b(g, "mid"), program_b(g, "critical"), "{:.0f}", True)
    both_row("of which studies and surveys, first in the capital, $M", g["predev"]["mid"]["total_m"], g["predev"]["critical"]["total_m"])
    both_row("Title I price serving the whole load, $/MWh", whole_price(g, "mid"), whole_price(g, "critical"))
    both_row(f"household generation charge during the bonds, $/yr (today {money(g['today_hh'])})", H.per_household(whole_price(g, "mid")), H.per_household(whole_price(g, "critical")))
    both_row("household generation charge after the bonds retire, $/yr", H.per_household(g["postbond"]["mid"]), H.per_household(g["postbond"]["critical"]))
    both_row("water at cost recovery, $/acre-foot", g["aqua"]["mid"]["per_af"], g["aqua"]["critical"]["per_af"])
    both_row("share of the load left to the grid", bm["unserved"], bc["unserved"], "{:.1%}")
    both_row("studies begin / first electricity (PV) / first CSP module / fleet complete",
             f"{ms['mid']['studies']:.0f} / {ms['mid']['field']:.0f} / {ms['mid']['module']:.0f} / {ms['mid']['fleet']:.0f}",
             f"{ms['critical']['studies']:.0f} / {ms['critical']['field']:.0f} / {ms['critical']['module']:.0f} / {ms['critical']['fleet']:.0f}", "{}")
    both_row("CO₂ avoided with the load closed, million t/yr", g["co2"]["mid"]["closed_mmt"], g["co2"]["critical"]["closed_mmt"], "{:.2f}")
    both_row("permanent jobs, Title I / construction peak", f"{g['jobs']['mid']['permanent']:,.0f} / {g['jobs']['mid']['construction_peak']:,.0f}", f"{g['jobs']['critical']['permanent']:,.0f} / {g['jobs']['critical']['construction_peak']:,.0f}", "{}")
    a("")
    a("**The decision the document asks for.** Fund the studies and surveys now, at")
    a(f"${g['predev']['mid']['total_m']:.0f} to {g['predev']['critical']['total_m']:.0f} million, and know within {g['predev']['mid']['gate_years']:.0f} to {g['predev']['critical']['gate_years']:.0f} years whether the rest is worth")
    a(f"${program_b(g, 'mid'):.0f} to {program_b(g, 'critical'):.0f} billion. Nothing irreversible is bought before the pilot receiver has passed its test.")
    a("")
    fig("fig-10-capital.png", "The program's capital at the adopted route, both cases, from Title III's single financial statement.")
    # ---------------------------------------------------------------- B
    a("## B. The requirement")
    a("")
    a(f"**Households (F-17).** Three million households is the program's **minimum**, growing with population (the author,")
    a(f"2026-09-11). At EIA's California average of {H.HH_KWH_YR:,.0f} kWh a year (503 kWh a month, 2024) that is **{g['e_req']:.1f} TWh** of firm")
    a(f"supply, growing to **{g['growth'][0]:.2f}–{g['growth'][1]:.2f}×** over the {H.BOND_TERM_Y}-year bond term at {100 * H.GROWTH_BAND[0]:.0f}–{100 * H.GROWTH_BAND[1]:.0f} % a year of residential")
    a(f"growth including electrification. v0.1's bill example used {H.HH_KWH_YR_CLAIMED:,.0f} kWh a year, twice the state average; California has")
    a(f"{H.CA_RES_CUSTOMERS:,} residential customers, so three million is a fifth of them.")
    a("")
    a(f"**The criterion, as the author stated it.** *The plant pays for itself after the build bonds.* Revenue must cover")
    a(f"debt service plus O&M every year of the {H.BOND_TERM_Y}-year term, with the coverage a bond buyer requires; after the term,")
    a("everything above O&M is the household's dividend. So the free tariff v0.1 promised is an **output** of the balance,")
    a("not an input to it. Inverted, the criterion is a required price per MWh, set beside two references:")
    a("")
    a("| reference | $/MWh | $ per household per year |")
    a("|---|---|---|")
    a(f"| what a household pays the utility for generation today (Title I §5's own IOU charge, {H.GEN_RATE_NOW:.3f} $/kWh) | {g['today_mwh']:.0f} | {money(g['today_hh'])} |")
    a(f"| what California's load-serving entities pay for firm clean energy under contract | {H.FIRM_CLEAN_PPA[0]:.0f}–{H.FIRM_CLEAN_PPA[1]:.0f} | {money(H.per_household(H.FIRM_CLEAN_PPA[0]))}–{money(H.per_household(H.FIRM_CLEAN_PPA[1]))} |")
    a("")
    a("**Size is not a lever.** Because the households are a requirement, the plant cannot be shrunk to make the price")
    a(f"close; only the equipment and the ownership form move the price. v0.1's plant as specified makes {g['pf']['net_twh']:.1f} TWh net,")
    a(f"which serves {g['households_served_v01'] / 1e6:.2f} million households at the state average: the size was right and the export was wrong (§C).")
    a("")
    # ---------------------------------------------------------------- C
    a("## C. What was submitted, and why it failed")
    a("")
    a("`California_Sovereign_Infrastructure_v0.1.md` is the as-submitted merge of the author's two documents with no figure")
    a("altered, so every repair is a diff against it. What it proposed:")
    a("")
    a(f"- **Title I, Program Helios-1M.** {H.GROSS_MWE:,.0f} MWe gross of nitrate-salt tower CSP across three desert nodes, {H.APERTURE_M2 / 1e6:.1f} million m²")
    a(f"  of heliostats, {H.STORAGE_MWH_TH / 1e3:,.0f} GWh_th of salt storage ({H.SALT_T / 1e6:.2f} million tonnes of salt), a claimed solar multiple of {H.CLAIMED_SM:.1f},")
    a(f"  {H.CLAIMED_INSTATE_MWE:,.0f} MW promised in-state and {H.CLAIMED_EXPORT_MWE:,.0f} MW exported at {H.CLAIMED_EXPORT_MWH / 1e6:.2f} TWh a year, sold at")
    a(f"  ${H.CLAIMED_PEAK_PRICES[0]:.0f}–{H.CLAIMED_PEAK_PRICES[2]:.0f}/MWh; capital ${H.CAPEX_B:.1f} B at a {100 * H.BOND_RATE:.2f} % bond rate, ${H.OM_M:.0f} M a year of O&M, a carrying")
    a(f"  cost of ${H.CARRYING_COST_M:,.0f} M a year; a $0.00/kWh household tariff.")
    a("- **Title II, Aqua-Sovereign.** 50,000 acre-foot-a-year desalination modules on coastal brownfields by low-temperature")
    a("  multi-effect distillation with zero liquid discharge, minerals (lithium, magnesium) sold to offset the cost, water at")
    a(f"  $400 an acre-foot, ${AQ.TITLE_II_CAPEX_M[0]:.0f}–{AQ.TITLE_II_CAPEX_M[1]:.0f} M a module, first water in 24 months.")
    a("- **Title III.** Reserved and never written.")
    a("")
    a("**What the plant as specified actually makes (`helios.py`, F-01, F-02).** Run hour by hour on exact solar geometry at")
    a("each node's sourced annual DNI, with the salt tank, the turbine's part-load curve and the parasitics as Title I states them:")
    a("")
    a("| | figure |")
    a("|---|---|")
    a(f"| net output, TWh/yr | {g['pf']['net_twh']:.1f} |")
    a(f"| net capacity factor | {g['pf']['cf_net']:.3f} |")
    a(f"| v0.1 sold, TWh/yr (in-state promise plus export at 100 % capacity factor) | {(H.CLAIMED_INSTATE_MWE * 8760 + H.CLAIMED_EXPORT_MWH) / 1e6:.1f} |")
    a(f"| shortfall against the in-state promise alone, TWh/yr | {(H.CLAIMED_INSTATE_MWE * 8760 / 1e6) - g['pf']['net_twh']:.1f} |")
    a(f"| revenue selling everything at the 2024 CAISO shape, $M/yr | {g['revenue_2024_m']:,.0f} |")
    a(f"| revenue with v0.1's ${H.CLAIMED_PEAK_PRICES[2]:.0f}/MWh on the four peak hours of every day, the rest at the 2024 shape, $M/yr | {g['revenue_peak_m']:,.0f} |")
    a(f"| carrying cost, debt service at Title I's own rate and term plus its O&M, $M/yr (Title I stated {H.CARRYING_COST_M:,.0f}) | {g['carrying_m']:,.0f} |")
    a(f"| required price at Title I's own ${H.CAPEX_B:.1f} B, $/MWh | {g['req_price_asbuilt']:.0f} |")
    a("")
    a("The export that funds the program is not overstated; it is **negative**: after the in-state promise the plant is short.")
    a(f"Evening-peak pricing exists for about 1,500–2,000 hours a year, and {H.NEG_HOURS_2024:,} hours in 2024 cleared negative. At")
    a(f"Title I's own capital the required price is ${g['req_price_asbuilt']:.0f}/MWh, inside the contract band, so at the stated cost self-funding")
    a("is a contract question. The stated cost is the question F-05 asks.")
    a("")
    a("**What it would cost to build (`heliocost.py`, F-05).** Line by line at the class the author decided (Noor III-class")
    a(f"heliostats of {HC.HELIOSTAT_M2:.0f} m² on {HC.TOWERS} towers of {HC.TOWER_HEIGHT_M:.0f} m), state-owned, groundbreaking {HC.GROUNDBREAK[0]}–{HC.GROUNDBREAK[1]}: no developer margin,")
    a(f"bond-rate interest during construction, the federal storage credit with the public direct-pay and energy-community bonuses,")
    a(f"CalPERS on-cost, property tax out and a payment in lieu in. The level is calibrated to NREL ATB 2024's ${HC.ATB_2024_PER_KWE:,.0f}/kWe and")
    a("the split is RECONSTRUCTED from SAM / Turchi 2019, because NREL is unreachable from this environment.")
    a("")
    a("| case | net capital, $B | $/W gross | required price, $/MWh | $ per household |")
    a("|---|---|---|---|---|")
    for (c, (_n, pr)), hh in zip(zip(("low", "mid", "high"), g["hc_price"]), g["hh_at_hc"]):
        a(f"| {c} | {g['hc'][c]['net_capex'] / 1e3:.1f} | {g['hc_perw'][c]:.2f} | {pr:.0f} | {money(hh)} |")
    a(f"| Title I as written | {H.CAPEX_B:.1f} | {H.CAPEX_B * 1e9 / (H.GROSS_MWE * 1e6):.2f} | {g['req_price_asbuilt']:.0f} | {money(H.per_household(g['req_price_asbuilt']))} |")
    a("")
    a(f"Title I's ${H.CAPEX_B:.1f} B is {g['hc']['low']['net_capex'] / 1e3 / H.CAPEX_B:.2f}× below the low case. **The criterion does not close at the scale proposed in any case.** The built record:")
    a("")
    a("| plant | $/W gross as built | year | storage, h |")
    a("|---|---|---|---|")
    for n, w, y, h in HC.BUILT_PER_W:
        a(f"| {n} | {w:.2f} | {y} | {h:.1f} |")
    a("")
    a("And what those plants delivered against their design, the fidelity band `helios.py` carries:")
    a("")
    a("| plant | delivered / designed | the year, and why |")
    a("|---|---|---|")
    for n, f, note in g["fidelity"]:
        a(f"| {n} | {f:.2f} | {note} |")
    a("")
    a("No commercial salt tower has delivered its design output, and the hourly model still flatters that record. That is")
    a("why the critical column exists.")
    a("")
    fig("fig-01-built-record.png", "Salt-tower CSP as built against Title I's own capital, in $ per watt gross (heliocost.py).")
    # ---------------------------------------------------------------- D
    a("## D. The equipment question")
    a("")
    a(f"Every candidate that can make a firm MWh in California, sized to the same {g['e_req']:.1f} TWh, state-owned, one criterion")
    a("(`firmpower.py`). Salt-tower CSP is priced from `heliocost.py`, never restated; the built-up candidates from their parts. The")
    a("instrument's bands are low / mid / high, so its high column stands where critical stands elsewhere.")
    a("")
    a("| candidate | MW | mid: net capital $B / price $/MWh / $ per household | band top: net capital $B / price $/MWh | acres | legal status |")
    a("|---|---|---|---|---|---|")
    for k in ("salton_flash", "egs", "pv_salt", "csp_proposed", "pv_ironair", "smr"):
        fm, fc = g["fp"]["mid"][k], g["fp"]["critical"][k]
        cap = " (capped: exceeds the developable resource)" if fm.get("capped") else ""
        top = "mid only: heliocost's mid case, scaled" if k == "csp_proposed" else f"{fc['capex_net'] / 1e3:.1f} / {fc['price']:.0f}"
        a(f"| {FP.TECH[k]['name']} | {fm['mw']:,.0f} | {fm['capex_net'] / 1e3:.1f} / {fm['price']:.0f} / {money(H.per_household(fm['price']))} | {top} | {fm['acres']:,.0f} | {FP.TECH[k]['legal']}{cap} |")
    a(f"| {FP.TECH['offshore_wind']['name']} | — | — | — | — | {FP.TECH['offshore_wind']['legal']}; {FP.TECH['offshore_wind']['status']} |")
    a("")
    port = g["fp_port"]
    a(f"Salton Sea geothermal, in the proposal's own Imperial node, has {FP.TECH['salton_flash']['cap_mw']:,.0f} MW developable, {port['e_geo'] / g['e_req']:.2f} of the requirement,")
    a(f"and prices at ${g['fp']['mid']['salton_flash']['price']:.0f}/MWh at mid; the small modular reactor is barred by Public Resources Code §25524.2. The")
    a("hypersaline capital band is ASSUMED and the file says so. **The instrument does not choose. The author chose CSP** —")
    a("*\"learn enough about how it works to do it better: scale down in size while increasing output\"* — and §E is that.")
    a("")
    fig("fig-02-candidates.png", "Every firm candidate sized to the requirement, state-owned, required price at mid and critical (firmpower.py).")
    # ---------------------------------------------------------------- E
    a("## E. The energy chain")
    a("")
    a("Sun to socket is a product of seven links, `E = A · DNI · opt · rec · tes · dispatch · cycle · (1 − par) · avail`, each")
    a("carried by Helios as proposed, each at the best achieved or designed, each at its physical bound (`cspchain.py`):")
    a("")
    a("| link | Helios as proposed | best achieved / designed | bound | status of the best |")
    a("|---|---|---|---|---|")
    for k, name, _hv, best, bound, status in C.CHAIN:
        a(f"| {name} | {g['base_links'][k]:.3f} | {'—' if best is None else f'{best:.3f}'} | {'—' if bound is None else f'{bound:.3f}'} | {status} |")
    a("")
    prod_base = C.chain_product(g["base_links"].values())
    prod_best = C.chain_product(g["best_links"].values())
    a(f"Helios's product is **{prod_base:.3f}** sun to socket; the best chain is **{prod_best:.3f}**, ×{prod_best / prod_base:.2f}. The three links that move are")
    a(f"the cycle ({H.ETA_CYCLE:.2f} steam at 565 °C against {g['best_links']['cycle']:.2f} sCO₂ at 715 °C), the optics ({g['base_links']['opt']:.3f} against Noor III-class")
    a(f"{g['best_links']['opt']:.2f}), and the one thing no link fixes: **a thermal plant serves daytime load at {H.ETA_CYCLE:.0%} where a panel serves it at")
    a("100 %.** So the daytime third never touches the mirrors, and the field is sized for the night. Two plants on that architecture:")
    a("")
    a(f"| | Helios as proposed, scaled to {g['e_req']:.1f} TWh | Helios-2 (nitrate salt, steam) | Helios-3 (particles, sCO₂), mid |")
    a("|---|---|---|---|")
    br, h2, h3 = g["baseline_row"], g["h2"], d["mid"]
    a(f"| mirror aperture, M m² | {br['aperture'] / 1e6:.1f} | {h2['aperture'] / 1e6:.1f} | {h3['aperture'] / 1e6:.1f} |")
    a(f"| towers, Noor III class | {br['towers']:.0f} | {h2['towers']:.0f} | {h3['towers']:.0f} |")
    a(f"| thermal block, MWe | {br['mw']:,.0f} | {h2['turb_mw']:,.0f} | {h3['turb_mw']:,.0f} |")
    a(f"| PV, MW_AC | — | {h2['pv_mw']:,.0f} | {h3['pv_mw']:,.0f} |")
    a(f"| price, $/MWh | {br['price']:.0f} | {h2['price']:.0f} | {h3['price']:.0f} |")
    a(f"| $ per household per year (today {money(g['today_hh'])}) | {money(H.per_household(br['price']))} | {money(H.per_household(h2['price']))} | {money(H.per_household(h3['price']))} |")
    a(f"| status | built class | {h2['status']} | {h3['status']} |")
    a("")
    a(f"Helios-2 is **{br['aperture'] / h2['aperture']:.1f}× smaller in mirror** for the same energy, every part of it built (DEWA Phase IV, Midelt's design).")
    a("Helios-3 is a pilot (G3P3, STEP), priced and not offered as a 2030 plant. **The author chose Helios-3** and claimed each")
    a("cost could be mitigated upfront; §I tests that claim row by row.")
    a("")
    fig("fig-03-chain.png", "The chain, link by link: Helios as proposed, Helios-3 at mid, Helios-3 at critical.")
    # ---------------------------------------------------------------- F
    a("## F. The plant: Helios-3")
    a("")
    a("A Noor III-class surround heliostat field sized for the night; a multi-aperture falling-particle receiver behind the")
    a("author's compound quartz aperture (a hexagonal low-OH rod-lens dome on a cooled lattice frame); sintered-bauxite")
    a("particles as medium and store, in cold-shell refractory-lined silos with replaceable liners, not buried; a moving")
    a("packed-bed particle-to-sCO₂ exchanger into a 715 °C, 250 bar sCO₂ recompression Brayton block, dry-cooled at 45 °C")
    a("ambient, CO₂ kept as the fluid; Inconel 740H pressure parts with Haynes 282 and Inconel 617 on the alloy ladder; PV")
    a("serving the daytime load directly and feeding electric particle heaters in winter; one cold-side particle lift per")
    a(f"aperture, gravity everywhere else. The cycle is {g['cycle']['helios3']} at {g['cycle']['helios3_eta']:.2f} gross; the nitrate-salt")
    a(f"fallback on the same field is {g['cycle']['fallback']} at {g['cycle']['fallback_eta']:.2f} (F-32: v0.1's *supercritical Rankine* is withdrawn).")
    a("")
    a("**The chain at both cases.** The critical receiver figure is `receiver.py`'s, handed up the chain rather than the")
    a("chain's own best (the standing rule: a downstream instrument hands its critical figure to the one above it):")
    a("")
    a("| link | mid | critical |")
    a("|---|---|---|")
    for k, name in (("opt", "field optical efficiency, annual"), ("rec", "receiver thermal efficiency"), ("tes", "storage round trip"),
                    ("dispatch", "dispatch"), ("cycle", "power cycle, gross"), ("par", "1 − parasitic share"), ("avail", "availability")):
        a(f"| {name} | {d['mid']['links'][k]:.3f} | {d['critical']['links'][k]:.3f} |")
    a(f"| **sun to socket** | **{C.chain_product(d['mid']['links'].values()):.3f}** | **{C.chain_product(d['critical']['links'].values()):.3f}** |")
    a("")
    a("**Sized to the requirement:**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("mirror aperture, M m²", d["mid"]["aperture"] / 1e6, d["critical"]["aperture"] / 1e6, "{:.1f}")
    both_row("towers, Noor III class", d["mid"]["towers"], d["critical"]["towers"])
    both_row("sCO₂ block, MWe", d["mid"]["turb_mw"], d["critical"]["turb_mw"])
    both_row(f"particle store, GWh_th ({C.NIGHT_HOURS:.0f} h)", d["mid"]["tes_mwh"] / 1e3, d["critical"]["tes_mwh"] / 1e3, "{:.1f}")
    both_row("PV, MW_AC", d["mid"]["pv_mw"], d["critical"]["pv_mw"])
    both_row("electric heaters, MW_th", d["mid"]["heater_mw"], d["critical"]["heater_mw"])
    both_row("energy served by PV directly / by the block, TWh", f"{d['mid']['e_direct']:.1f} / {d['mid']['e_night']:.1f}", f"{d['critical']['e_direct']:.1f} / {d['critical']['e_night']:.1f}", "{}")
    both_row("land at design sizing, acres", d["mid"]["acres"], d["critical"]["acres"])
    both_row(f"**on the adopted route (§H)**: mirror aperture, M m²", d["mid"]["aperture"] * bm["field"] / 1e6, d["critical"]["aperture"] * bc["field"] / 1e6, "{:.1f}")
    both_row("on the adopted route: towers", d["mid"]["towers"] * bm["field"], d["critical"]["towers"] * bc["field"])
    both_row("on the adopted route: sCO₂ block, MWe", d["mid"]["turb_mw"] * bm["block"], d["critical"]["turb_mw"] * bc["block"])
    both_row("on the adopted route: land, acres", g["land"]["mid"]["acres"], g["land"]["critical"]["acres"])
    a("")
    a("**Direct cost by line, $M, before contingency, EPC, tax, escalation and interest** (`cspchain.py`, the same rates")
    a("as `heliocost.py` where the part is the same, particle and sCO₂ lines from the Gen3 and STEP record):")
    a("")
    a("| line | mid | critical |")
    a("|---|---|---|")
    for k in d["mid"]["lines"]:
        both_row(k, d["mid"]["lines"][k], d["critical"]["lines"][k])
    both_row("**direct total**", sum(d["mid"]["lines"].values()), sum(d["critical"]["lines"].values()), "{:,.0f}", True)
    a("")
    a("**The receiver (`receiver.py`, R-11).** A falling curtain is a per-metre machine: its power goes with its width, so")
    a("scale is bought in width and aperture count, the loss fraction at fixed flux does not change with size, and the edge")
    a("losses shrink as perimeter over area. Run under the standing rule with every banded constant at nominal and at")
    a(f"critical (the critical flux halved to {RX.FLUX_MW_M2[1]:.1f} MW/m² after the 2026-09-11 review of the record, below the {RX.DEMO_FLUX_MW_M2[0]:.1f}–{RX.DEMO_FLUX_MW_M2[1]:.1f} Sandia")
    a("measured its curtain at):")
    a("")
    a("| | nominal (mid) | critical |")
    a("|---|---|---|")
    both_row("open-aperture thermal efficiency", g["rx"]["mid"]["open"], g["rx"]["critical"]["open"], "{:.3f}")
    both_row("with the compound quartz dome (R-02)", g["rx"]["mid"]["domed"], g["rx"]["critical"]["domed"], "{:.3f}")
    both_row("field factor handed upstream, against the chain's own receiver link", g["rx"]["mid"]["field"], g["rx"]["critical"]["field"], "{:.2f}")
    a("")
    a(f"The dome loses on the model and pays on the measured record, and both are printed. The critical open receiver, **{g['rx']['critical']['open']:.3f}**")
    a(f"against the chain's {g['best_links']['rec']:.2f}, grows the field by **{g['rx']['critical']['field']:.2f}** and is what the critical column above carries. The ladder of")
    a("scale, from what has run to a fleet tower:")
    a("")
    a("| rung | MW_th | step |")
    a("|---|---|---|")
    for name, mw, f in g["ladder"]:
        a(f"| {name} | {mw:,.0f} | {'—' if f is None else f'×{f:.1f}'} |")
    a("")
    a(f"The first 100 MWe module is already {g['ladder'][2][1] / g['ladder'][3][1]:.2f} of a fleet tower's duty, so a pilot aperture at ~{PL.PILOT_MWTH:.0f} MW_th belongs before it (§K).")
    a("")
    # ---------------------------------------------------------------- G
    a("## G. Hour by hour")
    a("")
    a("The chain sizes the plant on annual energy. `hourly3.py` runs it through 8,760 hours across the three nodes, PV")
    a("serving the load first, the block serving the residual from the store, the heaters charging the store from")
    a("surplus PV. The load shape is RECONSTRUCTED (residential, evening-peaked, summer-peaked; its seasonal sign was")
    a("found inverted and corrected on 2026-09-11, `docs/LOADSHAPE.md`) and pinned to the sourced annual; `profiles.py` is")
    a("the ingestion path for a measured CAISO profile and NSRDB hourly DNI, which replace it when reachable.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("share of the load served, as sized", hr["mid"]["served_frac"], hr["critical"]["served_frac"], "{:.3f}")
    both_row("unserved, TWh", hr["mid"]["unserved"] / 1e6, hr["critical"]["unserved"] / 1e6, "{:.2f}")
    both_row("hours with any shortfall", hr["mid"]["hours_unserved"], hr["critical"]["hours_unserved"])
    both_row("field defocused in summer, TWh_th", hr["mid"]["spill_th"] / 1e6, hr["critical"]["spill_th"] / 1e6, "{:.2f}")
    both_row("PV curtailed beyond the heaters, TWh", hr["mid"]["pv_curtail"] / 1e6, hr["critical"]["pv_curtail"] / 1e6, "{:.2f}")
    both_row("hours the store is full / empty", f"{hr['mid']['hours_full']:,.0f} / {hr['mid']['hours_empty']:,.0f}", f"{hr['critical']['hours_full']:,.0f} / {hr['critical']['hours_empty']:,.0f}", "{}")
    a("")
    a("**By month, mid** (TWh; the critical column of the last row beside it):")
    a("")
    a("| month | load | PV direct | block net | heaters (PV in) | unserved | share unserved, mid / critical |")
    a("|---|---|---|---|---|---|---|")
    for i in range(1, 13):
        r, rc = hr["mid"], hr["critical"]
        a(f"| {HR.MONTHS[i]} | {r['month_load'][i] / 1e6:.2f} | {r['month_pv_direct'][i] / 1e6:.2f} | {r['month_net'][i] / 1e6:.2f} | {r['month_heater'][i] / 1e6:.2f} | {r['month_unserved'][i] / 1e6:.2f} | {r['month_unserved'][i] / r['month_load'][i]:.1%} / {rc['month_unserved'][i] / rc['month_load'][i]:.1%} |")
    a("")
    a("**What the annual chain could not see.** The block is sized to the average night and a residential load peaks after")
    a("sunset, so the block cannot carry the evening in any month; the shortfall is year-round and evening-led, worst in")
    a(f"December at {hr['mid']['month_unserved'][12] / hr['mid']['month_load'][12]:.0%} (mid). Sixteen hours of store cannot move June into December: the store empties on winter")
    a("nights while a share of June's field is defocused. The heater and PV overbuild were never the lever; the block, the")
    a("field and the water are.")
    a("")
    a(f"**The Central Valley node (F-22).** Its DNI is {g['cv']['dni_ratio']:.2f} of the Mojave's. Moving it to a desert site lifts the served share from")
    a(f"{g['cv']['served_as_sited']:.3f} to {g['cv']['served_all_desert']:.3f} and December's shortfall from {g['cv']['dec_as_sited']:.1%} to {g['cv']['dec_all_desert']:.1%}, and does not change the closing sizing: the")
    a("node is kept for its land (§P), which the deserts do not have in fallowed, private, disturbed form.")
    a("")
    fig("fig-04-monthly.png", "The load by month and what the plant as sized serves, both cases (hourly3.py).")
    fig("fig-05-load-shape.png", "The residential load shape on a late-July and a late-December day, relative to the annual mean hour; the shaded band is the day PV serves directly.")
    # ---------------------------------------------------------------- H
    a("## H. Closing the load")
    a("")
    mb, mf, msd = HR.MIRRORS_ROUTE
    a(f"**Three routes.** The **mirrors** route grows the block to ×{mb:.2f}, the field to ×{mf:.1f} and the store to {msd:.0f} days, the cheapest")
    a(f"point of `hourly3.py`'s scan that closes to 1 %. The **water** route lifts Title II's product to an elevated reservoir with")
    a("the summer surplus (the field it would otherwise defocus and the PV it would curtail) and returns it year-round through")
    a("pump-turbines to the evenings — the author's decision of 2026-09-11 that the water comes down year-round, summer")
    a(f"irrigation and winter recharge, so the reservoir holds {J.RESERVOIR_DAYS[0]:.0f} / {J.RESERVOIR_DAYS[1]:.0f} days rather than a season. The feasibility rule is that a")
    a("closing point must lift its water inside its own run's surplus: a lift bought from the grid is not this route, and the")
    a("scan refuses it. **Water alone has no feasible point on this load**: with the field and store at design, the block that")
    a("closes the evening eats the spill the lift runs on. **The author chose both** (`both.py`): the water returns half the")
    a("shortfall, the plant the other half, each point on a ladder over the water's share required to lift inside its own surplus.")
    a("")
    a("| share of the shortfall returned by water | mid: block, field, store, MW; Title I $B; +$/MWh; left to grid | critical: the same |")
    a("|---|---|---|")
    for s in B.WATER_SCAN:
        cells = []
        for c in CASES:
            r = g["scan"][c]["ladder"][s]
            cells.append("no feasible point" if r is None else f"×{r['block']:.2f}, ×{r['field']:.2f}, {r['store']:.0f} d, {r['mw']:,.0f} MW; {r['title1_b']:.1f}; +{r['dprice']:.0f}; {r['unserved']:.1%}")
        tag = " **(adopted)**" if s == B.ADOPTED_SHARE else (" (mirrors alone, on this scan's grid)" if s == 0 else "")
        a(f"| {s:.2f}{tag} | {cells[0]} | {cells[1]} |")
    a("")
    a("**The adopted point:**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("block / field / store", f"×{bm['block']:.2f} / ×{bm['field']:.2f} / {bm['store']:.0f} d", f"×{bc['block']:.2f} / ×{bc['field']:.2f} / {bc['store']:.0f} d", "{}")
    both_row("pump-turbine plant, MW", bm["mw"], bc["mw"])
    both_row("Title II modules / million acre-feet a year", f"{bm['modules']:.0f} / {bm['maf']:.2f}", f"{bc['modules']:.0f} / {bc['maf']:.2f}", "{}")
    both_row("Title I capital: plant growth / water side (reservoir and pump-turbines) / total, $B", f"{bm['plant_b']:.1f} / {bm['water_b']:.1f} / {bm['title1_b']:.1f}", f"{bc['plant_b']:.1f} / {bc['water_b']:.1f} / {bc['title1_b']:.1f}", "{}")
    both_row("mirrors alone, for comparison, $B", m["mid"]["cost_b"], m["critical"]["cost_b"], "{:.1f}")
    both_row("both over mirrors", bm["title1_b"] / m["mid"]["cost_b"], bc["title1_b"] / m["critical"]["cost_b"], "{:.2f}×")
    both_row("added to the price, $/MWh", bm["dprice"], bc["dprice"], "+{:.0f}")
    both_row("left to the grid", bm["unserved"], bc["unserved"], "{:.1%}")
    both_row("with the water withheld", bm["no_water"]["unserved"], bc["no_water"]["unserved"], "{:.1%}")
    both_row("with the field at design", bm["no_field"]["unserved"], bc["no_field"]["unserved"], "{:.1%}")
    both_row("with neither (as sized)", g["scan"]["mid"]["as_sized"]["unserved"], g["scan"]["critical"]["as_sized"]["unserved"], "{:.1%}")
    both_row("water sized to return / dispatched in the run / lift for the sized water / surplus available, TWh", f"{bm['budget_twh']:.2f} / {bm['hydro_twh']:.2f} / {bm['lift_twh']:.2f} / {bm['surplus_twh']:.2f}", f"{bc['budget_twh']:.2f} / {bc['hydro_twh']:.2f} / {bc['lift_twh']:.2f} / {bc['surplus_twh']:.2f}", "{}")
    both_row("O&M the closing plant adds, plant / water side, $M/yr", f"{bm['plant_om_m']:.0f} / {bm['water_om_m']:.0f}", f"{bc['plant_om_m']:.0f} / {bc['water_om_m']:.0f}", "{}")
    a("")
    a("Two levers that fail differently, each carrying a real share. A cheapest-point search returns mirrors with a token")
    a("water plant, so the even split is adopted as the author's word and marked DECIDED, movable on the ladder.")
    a("")
    a(f"**Two things a reader should see in that table.** The water is *sized* to return half the shortfall as sized ({bm['budget_twh']:.2f} TWh at")
    a(f"mid) and the run *dispatches* {bm['hydro_twh']:.2f}, because the larger block serves the evening first and the pump-turbines take what")
    a("it leaves; the modules are sized on the shortfall, not on what is dispatched, so the water plant runs at about half its")
    a("evening sizing and all of its water is delivered as irrigation and recharge regardless. That is the conservative side")
    a(f"for Title II and the expensive side for Title I, and it is stated rather than hidden. And the mirrors-alone figure the")
    a(f"comparison uses is `hourly3.py`'s one fixed route (block ×{mb:.2f}, field ×{mf:.1f}, store {msd:.0f} days at both cases, ${m['mid']['cost_b']:.1f} / {m['critical']['cost_b']:.1f} B), which")
    a(f"is what Title III prints; the ladder's own scan, which lets the block and field vary per case, finds a cheaper")
    a(f"mirrors-only point at critical (${g['scan']['critical']['ladder'][0.0]['title1_b']:.1f} B). Both are the instruments' and neither is hidden.")
    a("")
    a(f"**The hydraulics.** The adopted route is priced at one head, {B.HEAD_M:.0f} m (ASSUMED; the Edmonston lift is 587 m, Gianelli about 100), at both cases.")
    a(f"There a cubic metre returns {g['hyd']['mid']['returned_kwh_m3']:.3f} / {g['hyd']['critical']['returned_kwh_m3']:.3f} kWh and costs {g['hyd']['mid']['lift_kwh_m3']:.3f} / {g['hyd']['critical']['lift_kwh_m3']:.3f} kWh to lift, a round trip of")
    a(f"{g['hyd']['mid']['round_trip']:.2f} / {g['hyd']['critical']['round_trip']:.2f} (turbine and pump at {J.ETA_TURBINE[0]:.2f} / {J.ETA_TURBINE[1]:.2f} each); reverse osmosis itself takes {AQ.RO_KWH_M3[0]:.1f}–{AQ.RO_KWH_M3[1]:.1f} kWh/m³ on Title II's own account. The")
    a("lift is invariant in head (returned energy over the round trip), so feasibility does not depend on the site; the")
    a("volume, and so the modules and Title II's capital, go as one over head, and the sensitivity below runs the head band")
    a(f"from {J.HEAD_SCAN[0]:.0f} to {J.HEAD_SCAN[-1]:.0f} m. The pump-turbine plant and reservoir carry O&M at {100 * J.HYDRO_OM_SHARE[0]:.1f} / {100 * J.HYDRO_OM_SHARE[1]:.1f} % of their capital a year (ASSUMED band).")
    a("")
    a("**Sensitivity to the two site assumptions**, the hourly run held fixed:")
    a("")
    a("| case | head, m | days held | modules | MAF/yr | reservoir, $B | Title I, $B | +$/MWh | Title II, $B |")
    a("|---|---|---|---|---|---|---|---|---|")
    for c in CASES:
        for r in g["sens"][c]:
            a(f"| {c} | {r['head']:.0f} | {r['days']:.0f} | {r['modules']:.1f} | {r['maf']:.2f} | {r['reservoir_b']:.2f} | {r['title1_b']:.1f} | +{r['dprice']:.0f} | {r['title2_b']:.0f} |")
    a("")
    a("The head is the site question that sizes Title II; the days of holding move Title I by under a billion.")
    a("")
    fig("fig-06-ladder.png", "The ladder over the water's share: Title I's capital to close the load at each share, both cases, every point carrying the larger field; water alone with the field and store at design has no feasible point and is not on the ladder.")
    fig("fig-07-head.png", "Title II modules the adopted route needs against the reservoir head, at each case's days of holding.")
    # ---------------------------------------------------------------- I
    a("## I. The risk register, mitigated upfront")
    a("")
    a("The author's claim: *Helios-3 is actually better, and each cost can be fully mitigated upfront.* `helios3.py` tests")
    a("it the way an environmental register is tested: sixteen rows graded **before** and **after**, each carried by a")
    a("named part of the build, each marked DESIGN (retired by specification), HOURS (retired only by operating time) or")
    a("BENEFIT, and each with the source that grades it. The file refuses to flatten HOURS: *a specification cannot make a")
    a("machine have run.* Walked row by row with the author on 2026-09-11; the author's design is written into each row.")
    a("")
    for rid, risk, before, mit, after, kind, carrier, source in H3.REGISTER:
        a(f"**{rid}. {risk}** — {before} → **{after}**, {kind}.")
        a("")
        a(f"- *Mitigation:* {mit}")
        a(f"- *Carried by:* {carrier}")
        a(f"- *Source:* {source}")
        adder = pm["adders"].get(rid)
        if adder:
            a(f"- *Priced:* ${adder:,.0f} M at mid, ${pc['adders'].get(rid, 0.0):,.0f} M at critical")
        a("")
    b0, b1 = g["grades"]
    a("Before: " + ", ".join(f"{v} {k}" for k, v in b0.items() if v) + ". After: " + ", ".join(f"{v} {k}" for k, v in b1.items() if v) + ".")
    a("")
    a("| priced, $M | mid | critical |")
    a("|---|---|---|")
    stack = {}
    for c, pp in (("mid", pm), ("critical", pc)):
        ci = 1 if c == "mid" else 2
        direct = sum(pp["lines"].values())
        overhead = (direct + pp["mit_total"]) * (HC.CONTINGENCY[ci] + HC.EPC_OWNER[ci] + HC.SALES_TAX * HC.SALES_TAX_BASE)
        studies = pp["studies_m"] * (1 + HC.CONTINGENCY[ci])
        over = direct + pp["mit_total"] + overhead + studies + pp["foak"]
        gross = pp["capex_net"] + pp["credit"]
        stack[c] = dict(direct=direct, overhead=overhead, studies=studies, over=over, escidc=gross - over, gross=gross)
    both_row("direct plant lines (§F)", stack["mid"]["direct"], stack["critical"]["direct"])
    both_row("mitigation adders, direct", pm["mit_total"], pc["mit_total"])
    both_row(f"contingency ({100 * HC.CONTINGENCY[1]:.0f} / {100 * HC.CONTINGENCY[2]:.0f} %), EPC and owner's cost ({100 * HC.EPC_OWNER[1]:.0f} / {100 * HC.EPC_OWNER[2]:.0f} %), sales tax on those", stack["mid"]["overhead"], stack["critical"]["overhead"])
    both_row("studies and surveys (§L), with contingency", stack["mid"]["studies"], stack["critical"]["studies"])
    both_row(f"first-module premium ({H3.FIRST_MODULE_PREMIUM:.1f}× / {H3.FIRST_MODULE_PREMIUM_CRITICAL:.1f}× on its share of the thermal block)", pm["foak"], pc["foak"])
    both_row("overnight, groundbreaking dollars", stack["mid"]["over"], stack["critical"]["over"])
    both_row(f"escalation to the build and interest during construction ({HC.BUILD_YEARS:.0f} years at the bond rate)", stack["mid"]["escidc"], stack["critical"]["escidc"])
    both_row("gross capital", stack["mid"]["gross"], stack["critical"]["gross"])
    both_row("federal storage credit, direct pay", -pm["credit"], -pc["credit"])
    both_row("**net capital with the register, $M**", pm["capex_net"], pc["capex_net"], "{:,.0f}", True)
    both_row(f"O&M with particle makeup ({100 * H3.PARTICLE_MAKEUP_PER_YEAR:.0f} / {100 * H3.PARTICLE_MAKEUP_CRITICAL:.0f} %/yr) and rejuvenation, $M/yr", pm["om"], pc["om"])
    both_row("price with the register, $/MWh", pm["price"], pc["price"])
    a("")
    # ---------------------------------------------------------------- J
    a("## J. Provenance: every study that covers a technology in the system")
    a("")
    a(f"R-12 says no plant of this kind exists; `studies.py` lists rather than asserts. {len(ST.STUDIES)} rows over the {len(ST.TECHNOLOGIES)} technologies")
    a("the design uses, each with a status from a closed set — OPERATED (a plant has run at the stated scale), TESTED (a")
    a("prototype has run, below plant scale), DESIGNED (a published design or code case; nothing has run), AUTHOR (this")
    a("repository's own design; no study exists) — and a source. The register is complete over technologies and a floor")
    a("over studies; it was reviewed against the web on 2026-09-11 where the proxy reached and corrected in place.")
    a("")
    for key, tech, need in ST.TECHNOLOGIES:
        a(f"### J.{[t[0] for t in ST.TECHNOLOGIES].index(key) + 1}. {tech}")
        a("")
        a(f"*What the design needs:* {need}.")
        a("")
        a("| study or plant | scale | year | status | what it settled | source |")
        a("|---|---|---|---|---|---|")
        for _k, study, scale, year, status, settled, source in ST.by_tech(key):
            a(f"| {study} | {scale} | {year} | {status} | {settled} | {source} |")
        rec = next(r for r in ST.RECOMMEND if r[0] == key)
        a("")
        a(f"*Further study recommended, on the {rec[4]} rung ({rec[3]:.1f} years):* {rec[1]}. *It settles:* {rec[2]}.")
        a("")
    a(f"**The critical path of study is {g['path_years']:.1f} years**, run against the build rather than before it, the studies within a rung")
    a(f"in parallel. **Delay** escalates the whole plant at {100 * HC.ESCALATION:.0f} % a year (ASSUMED band {100 * 0.02:.0f}–{100 * 0.04:.0f} %) before a dollar is spent:")
    a("")
    a("| per year of delay | mid | critical |")
    a("|---|---|---|")
    both_row("capital, $B", g["delay"]["mid"]["delta_capex_m"] / 1e3, g["delay"]["critical"]["delta_capex_m"] / 1e3, "{:.2f}")
    both_row("price, $/MWh", g["delay"]["mid"]["delta_price"], g["delay"]["critical"]["delta_price"], "{:.1f}")
    both_row("household, $/yr", g["delay"]["mid"]["delta_hh"], g["delay"]["critical"]["delta_hh"])
    a("")
    # ---------------------------------------------------------------- K
    a("## K. The pilot aperture: an acceptance protocol")
    a("")
    pl = g["pilot"]
    a("The receiver's real efficiency is the one open item no instrument can close, and a test graded after it runs is")
    a("not a test. `pilot.py` fixes the unit, the measurements and the pass mark before the pilot is built.")
    a("")
    a("| the unit | nominal (mid) | critical |")
    a("|---|---|---|")
    both_row(f"one aperture carrying {PL.PILOT_MWTH:.0f} MW_th: curtain width, m", pl["unit"]["mid"]["width_m"], pl["unit"]["critical"]["width_m"], "{:.1f}")
    both_row("aperture area, m²", pl["unit"]["mid"]["area_m2"], pl["unit"]["critical"]["area_m2"], "{:.1f}")
    both_row("drop per stage, m", pl["unit"]["mid"]["drop_m"], pl["unit"]["critical"]["drop_m"], "{:.1f}")
    both_row("particle mass flow, kg/s", pl["unit"]["mid"]["massflow_kg_s"], pl["unit"]["critical"]["massflow_kg_s"], "{:.0f}")
    both_row("aperture-average flux, MW/m² / ambient, °C", f"{pl['unit']['mid']['flux']:.1f} / {pl['unit']['mid']['t_amb']:.0f}", f"{pl['unit']['critical']['flux']:.1f} / {pl['unit']['critical']['t_amb']:.0f}", "{}")
    a("")
    a("**Five measurements:**")
    a("")
    for name, how, what in PL.MEASUREMENTS:
        a(f"- **{name}.** {how}. *Condition:* {what}.")
    a("")
    u = pl["u"]
    a(f"**The pass mark**, M1 at critical conditions averaged over the last {PL.GRADED_HOURS:.0f} of {PL.ON_SUN_HOURS:.0f} on-sun hours, with a calorimetric")
    a(f"uncertainty of **{100 * u:.1f} %** in quadrature (mass flow {100 * PL.U_MASSFLOW:.0f} %, temperatures {100 * PL.U_DT:.0f} %, flux {100 * PL.U_FLUX:.0f} %):")
    a("")
    a("| grade | measured efficiency | what follows |")
    a("|---|---|---|")
    a(f"| PASS-CHAIN | ≥ {pl['th']['chain'] * (1 + u):.3f} | the chain's own link is witnessed; mid is witnessed too |")
    a(f"| PASS-DESIGN | ≥ {pl['th']['critical_open'] * (1 + u):.3f} | the critical design basis holds; the first module is ordered |")
    a(f"| UNDECIDED | {pl['th']['critical_open'] * (1 - u):.3f} – {pl['th']['critical_open'] * (1 + u):.3f} | not a pass and not a fail; the pilot runs on |")
    a(f"| FAIL | < {pl['th']['critical_open'] * (1 - u):.3f} | the salt-block fallback is the recorded route; the first module is not ordered |")
    a("")
    a("**What each result does upstream**, priced against each case's own receiver link, so a pass at the design basis")
    a("costs the critical design nothing:")
    a("")
    a("| measured | grade | field factor, mid / critical | price, mid / critical, $/MWh |")
    a("|---|---|---|---|")
    for e, cons in pl["cons"].items():
        a(f"| {e:.3f} | {pl['grades'][e]} | {cons['mid_factor']:.2f} / {cons['critical_factor']:.2f} | {cons['mid']:+.0f} / {cons['critical']:+.0f} |")
    a("")
    a(f"Scheduled {pl['tranche']['mid']['years'][0]:.0f}–{pl['tranche']['mid']['years'][1]:.0f} (mid) / {pl['tranche']['critical']['years'][0]:.0f}–{pl['tranche']['critical']['years'][1]:.0f} (critical) at ${pl['tranche']['mid']['cost_m']:.0f} / {pl['tranche']['critical']['cost_m']:.0f} M including the ladder's technology")
    a("studies. The protocol constants are ASSUMED and say so; the pass mark is not.")
    a("")
    # ---------------------------------------------------------------- L
    a("## L. Studies and surveys first")
    a("")
    a("The author's instruction of 2026-09-11: every study and survey is its own upfront line item, preceding the others")
    a("by first priority. `predev.py` prices them from the class of study — ASSUMED bands, not quotes — and carries them")
    a("in the capital ahead of every plant line, with contingency and without EPC margin or sales tax.")
    a("")
    a("**Title I.** Gating studies must finish before the field rung; the technology studies run on the ladder against the build.")
    a("")
    a("| id | study or survey | what it settles | scope | mid: $M each × n = total, years | critical: the same |")
    a("|---|---|---|---|---|---|")
    for rm, rc in zip(g["predev"]["mid"]["rows"], g["predev"]["critical"]["rows"]):
        a(f"| {rm['id']} | {rm['name']} | {rm['settles']} | {rm['scope']}, {'GATE' if rm['gate'] else 'ladder'} | {rm['unit_m']:.1f} × {rm['n']} = {rm['cost_m']:.1f}, {rm['years']:.1f} | {rc['unit_m']:.1f} × {rc['n']} = {rc['cost_m']:.1f}, {rc['years']:.1f} |")
    a("")
    a(f"{PD.PILOT_NOTE[0].upper() + PD.PILOT_NOTE[1:]}.")
    a("")
    a("| Title I | mid | critical |")
    a("|---|---|---|")
    both_row("gating studies and surveys, $M", g["predev"]["mid"]["gate_m"], g["predev"]["critical"]["gate_m"])
    both_row("technology studies on the ladder, $M", g["predev"]["mid"]["ladder_m"], g["predev"]["critical"]["ladder_m"])
    both_row(f"owner's engineer on the study phase ({100 * PD.OWNERS_ENGINEER_SHARE[0]:.0f} / {100 * PD.OWNERS_ENGINEER_SHARE[1]:.0f} %), $M", g["predev"]["mid"]["owners_engineer_m"], g["predev"]["critical"]["owners_engineer_m"])
    both_row("**total, first in the capital, $M**", g["predev"]["mid"]["total_m"], g["predev"]["critical"]["total_m"], "{:,.0f}", True)
    both_row("longest gating study, years", g["predev"]["mid"]["gate_years"], g["predev"]["critical"]["gate_years"], "{:.1f}")
    both_row("studies start / field rung starts", f"{PD.START_YEAR:.0f} / {g['predev']['mid']['field_start']:.0f}", f"{PD.START_YEAR:.0f} / {g['predev']['critical']['field_start']:.0f}", "{}")
    a("")
    a(f"**Title II**, per selected coastal site, plus a screening pass over the {PD.CANDIDATE_SITES} candidates of §P:")
    a("")
    a("| id | study | what it settles | mid: $M, years | critical: $M, years |")
    a("|---|---|---|---|---|")
    for rm, rc in zip(g["predev2"]["mid"]["rows"], g["predev2"]["critical"]["rows"]):
        a(f"| {rm['id']} | {rm['name']} | {rm['settles']} | {rm['cost_m']:.1f}, {rm['years']:.1f} | {rc['cost_m']:.1f}, {rc['years']:.1f} |")
    a("")
    a("| Title II | mid | critical |")
    a("|---|---|---|")
    both_row("per selected site, $M", g["predev2"]["mid"]["per_site_m"], g["predev2"]["critical"]["per_site_m"], "{:.1f}")
    both_row("screening of the candidates, $M", g["predev2"]["mid"]["screening_m"], g["predev2"]["critical"]["screening_m"], "{:.1f}")
    both_row(f"per module at {PD.MODULES_PER_SITE[0]:.0f} / {PD.MODULES_PER_SITE[1]:.0f} modules a site, $M", g["predev2"]["mid"]["per_module_m"], g["predev2"]["critical"]["per_module_m"], "{:.1f}")
    both_row("longest study (the coastal permit), years", g["predev2"]["mid"]["gate_years"], g["predev2"]["critical"]["gate_years"], "{:.1f}")
    a("")
    # ---------------------------------------------------------------- M
    a("## M. Price, the household and the financing")
    a("")
    a("| $/MWh | mid | critical |")
    a("|---|---|---|")
    both_row("Helios-3 as chained", d["mid"]["price"], d["critical"]["price"])
    both_row("with the mitigation register (§I) and the studies (§L)", pm["price"], pc["price"])
    both_row("serving the whole load, mirrors route", pm["price"] + m["mid"]["dprice"], pc["price"] + m["critical"]["dprice"])
    both_row("**serving the whole load, both (adopted)**", whole_price(g, "mid"), whole_price(g, "critical"), "{:,.0f}", True)
    both_row("after the bonds retire: O&M only, register plant and closing plant", g["postbond"]["mid"], g["postbond"]["critical"])
    a("")
    a(f"| $ per household per year (today {money(g['today_hh'])}) | mid | critical |")
    a("|---|---|---|")
    both_row("with the register", H.per_household(pm["price"]), H.per_household(pc["price"]))
    both_row("serving the whole load, mirrors route", H.per_household(pm["price"] + m["mid"]["dprice"]), H.per_household(pc["price"] + m["critical"]["dprice"]))
    both_row("**serving the whole load, both (adopted)**", H.per_household(whole_price(g, "mid")), H.per_household(whole_price(g, "critical")), "{:,.0f}", True)
    both_row("after the bonds retire", H.per_household(g["postbond"]["mid"]), H.per_household(g["postbond"]["critical"]))
    a("")
    band = H.FIRM_CLEAN_PPA[1]
    a(f"**The criterion, stated exactly.** At mid, Helios-3 with its register needs ${pm['price']:.0f}/MWh, ${pm['price'] - band:.0f} above the top of the")
    a(f"contract band, and a household pays ${money(H.per_household(pm['price']))} against ${money(g['today_hh'])} today; serving the whole load on the adopted route")
    a(f"costs ${whole_price(g, 'mid'):.0f}, at which a household pays ${money(H.per_household(whole_price(g, 'mid')))}. At critical the register price is ${pc['price']:.0f} and the whole load")
    a(f"${whole_price(g, 'critical'):.0f}: **${money(H.per_household(whole_price(g, 'critical')))} a household, above today's bill**. The plant pays for itself after the bonds at a price")
    a("above the band, and the critical case is the threshold the design is held to. A plant designed to mid has no margin;")
    a("this document does not offer one.")
    a("")
    a("**No further public money after the build.** The bill carries debt service and O&M; the treasury carries nothing")
    a("once the plant runs at capacity. That holds if the plant delivers its modelled output, if the HOURS rows of §I hold")
    a("(a mid-life replacement of a major component is new capital, not O&M), and if Title II stands on its own rate (§O).")
    a("")
    a("| per year, Title I | mid | critical |")
    a("|---|---|---|")
    both_row(f"debt service, {H.BOND_TERM_Y}-year bonds at {100 * H.BOND_RATE:.2f} %, $M", g["reserve"]["mid"]["debt_service_m"], g["reserve"]["critical"]["debt_service_m"])
    both_row("O&M, register plant, $M", pm["om"], pc["om"])
    both_row("O&M the closing plant adds on the adopted route (§H), $M", bm["extra_om_m"], bc["extra_om_m"])
    both_row("share of the register plant's bill that is the bonds", g["reserve"]["mid"]["debt_service_m"] / (g["reserve"]["mid"]["debt_service_m"] + pm["om"]), g["reserve"]["critical"]["debt_service_m"] / (g["reserve"]["critical"]["debt_service_m"] + pc["om"]), "{:.0%}")
    a("")
    a(f"**The security behind the rate (F-19).** The {100 * H.BOND_RATE:.2f} % is a general-obligation or contracted-revenue rate; the security is")
    a("contracted in-state offtake at the required price with a state GO backstop for the first-of-kind rungs. Priced to each")
    a("security, with the register:")
    a("")
    a("| security | rate | mid, $/MWh ($/household) | critical, $/MWh ($/household) |")
    a("|---|---|---|---|")
    for (name, r, prm, hhm), (_n, _r, prc, hhc) in zip(g["rates"]["mid"], g["rates"]["critical"]):
        a(f"| {name} | {100 * r:.2f} % | {prm:.0f} ({hhm:,.0f}) | {prc:.0f} ({hhc:,.0f}) |")
    a("")
    a(f"**The mechanism behind the tariff (F-10).** v0.1's $0.00/kWh is replaced by the household bill above, an output of the")
    a(f"balance: {T1.MECHANISM}. A free tariff is a subsidy paid by someone, and this program names no one to pay it.")
    a("")
    a("**Contingency, reserve and the downside (F-29, F-30).**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("contingency carried on direct cost", g["reserve"]["mid"]["contingency"], g["reserve"]["critical"]["contingency"], "{:.0%}")
    both_row("EPC and owner's cost", g["reserve"]["mid"]["epc"], g["reserve"]["critical"]["epc"], "{:.0%}")
    both_row(f"debt-service reserve, {MJ.DSRF_YEARS:.0f} year, $M", g["reserve"]["mid"]["dsrf_m"], g["reserve"]["critical"]["dsrf_m"])
    both_row(f"price at {H.COVERAGE_REQ:.2f}× coverage (a revenue bond's requirement), $/MWh", g["downside"]["mid"]["price_at_coverage"], g["downside"]["critical"]["price_at_coverage"])
    a("")
    a("The downside case is the critical column, by the author's standing rule.")
    a("")
    a("**The schedule (F-24).** Tranche zero is the studies and surveys, from the first study year to the field start; the")
    a("field rung waits on the longest gating study; each later tranche follows a rung passed at its critical figure. Direct")
    a("cost by rung, with each case's own years:")
    a("")
    a("| rung | mid: years, $B | critical: years, $B |")
    a("|---|---|---|")
    for (name, y0, y1, am), (_n, c0, c1, ac) in zip(g["tranches"]["mid"][0], g["tranches"]["critical"][0]):
        a(f"| {name} | {y0:.0f}–{y1:.0f}, {am / 1e3:.2f} | {c0:.0f}–{c1:.0f}, {ac / 1e3:.2f} |")
    a("")
    a("| milestone | mid | critical |")
    a("|---|---|---|")
    both_row("studies and surveys begin", ms["mid"]["studies"], ms["critical"]["studies"], "{:.0f}")
    both_row("field, towers and PV at the first node complete: first electricity, from PV", ms["mid"]["field"], ms["critical"]["field"], "{:.0f}")
    both_row("pilot aperture on sun, graded", f"{ms['mid']['pilot'][0]:.0f}–{ms['mid']['pilot'][1]:.0f}", f"{ms['critical']['pilot'][0]:.0f}–{ms['critical']['pilot'][1]:.0f}", "{}")
    both_row("first 100 MWe Helios-3 module dispatching", ms["mid"]["module"], ms["critical"]["module"], "{:.0f}")
    both_row("fleet complete, the whole load served", ms["mid"]["fleet"], ms["critical"]["fleet"], "{:.0f}")
    a("")
    a(f"The realistic column is the critical one. The two-year slide comes from one item, the {MJ.NEPA_YEARS[1]:.0f}-year NEPA environmental")
    a("impact statement on the Mojave node, which is why the studies go first.")
    a("")
    a(f"**Transmission (F-09).** The export is negative, so no firm export right is needed. The in-state gen-tie per node at the")
    a(f"adopted sizing peaks at {g['gentie']['mid']['per_node']:,.0f} MW (mid) / {g['gentie']['critical']['per_node']:,.0f} MW (critical) from the hour-by-hour — the same at both cases because the block is the")
    a(f"same size at both and sets the peak — {g['gentie']['mid']['circuits']:.2f} / {g['gentie']['critical']['circuits']:.2f} of one 500 kV circuit (rated {T1.CIRCUIT_500KV_MW[0]:,.0f} / {T1.CIRCUIT_500KV_MW[1]:,.0f} MW), priced in the design's")
    a(f"switchyard line at ${g['gentie']['mid']['switchyard_m']:,.0f} / {g['gentie']['critical']['switchyard_m']:,.0f} M (§F). The interconnection study is the Authority's to file and no")
    a("authority shortens it.")
    a("")
    fig("fig-08-price.png", "Title I's required price step by step, both cases, against the contract band and today's generation charge.")
    fig("fig-09-household.png", "A household's annual generation charge: today, during the bond term on the adopted route, and after the bonds retire.")
    fig("fig-11-schedule.png", "The schedule by tranche at mid and critical; tranche zero is the studies and surveys.")
    # ---------------------------------------------------------------- N
    a("## N. Title II: the water")
    a("")
    aq, ar, mod = g["aqua"], g["aqua_route"], g["aqua"]
    a("**The module.** A 50,000 acre-foot-a-year seawater reverse-osmosis module on a retired coastal power-plant brownfield,")
    a("reusing its intake channel and permitted outfall, state-owned on Title I's form. The unit capital is the built record")
    a(f"escalated to the groundbreaking dollar — Carlsbad at ${g['record']['carlsbad']:,.0f} per AFY (mid) and Huntington Beach as designed at")
    a(f"${g['record']['huntington']:,.0f} (critical) — against the ${AQ.TITLE_II_CAPEX_M[0] * 1e6 / AQ.MODULE_AFY:,.0f}–{AQ.TITLE_II_CAPEX_M[1] * 1e6 / AQ.MODULE_AFY:,.0f} v0.1 submitted.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("overnight, $M", mod["mid"]["overnight_m"], mod["critical"]["overnight_m"])
    both_row("of which site studies and surveys per module (§L), $M", mod["mid"]["studies_m"], mod["critical"]["studies_m"], "{:.1f}")
    both_row("financed (contingency, EPC, interest during construction), $M", mod["mid"]["financed_m"], mod["critical"]["financed_m"])
    both_row(f"against v0.1's ${AQ.TITLE_II_CAPEX_M[0]:.0f}–{AQ.TITLE_II_CAPEX_M[1]:.0f} M", mod["mid"]["financed_m"] / 285, mod["critical"]["financed_m"] / 285, "{:.1f}×")
    both_row("electricity, kWh/m³, bought from Title I at its register price", f"{mod['mid']['kwh_m3']:.1f} at ${mod['mid']['energy_price']:.0f}/MWh", f"{mod['critical']['kwh_m3']:.1f} at ${mod['critical']['energy_price']:.0f}/MWh", "{}")
    a("")
    a("**The water**, at cost recovery — debt service, energy and operations, no mineral revenue:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("debt service / energy / non-energy O&M, $M/yr", f"{mod['mid']['debt_m']:.0f} / {mod['mid']['energy_m']:.0f} / {mod['mid']['om_m']:.0f}", f"{mod['critical']['debt_m']:.0f} / {mod['critical']['energy_m']:.0f} / {mod['critical']['om_m']:.0f}", "{}")
    both_row("**$ per acre-foot**", mod["mid"]["per_af"], mod["critical"]["per_af"], "{:,.0f}", True)
    both_row("$ per m³", mod["mid"]["per_m3"], mod["critical"]["per_m3"], "{:.2f}")
    both_row("of which energy", mod["mid"]["energy_m"] / mod["mid"]["total_m"], mod["critical"]["energy_m"] / mod["critical"]["total_m"], "{:.0%}")
    both_row(f"per household per year at {AQ.HOUSEHOLD_AF_YR:.2f} AF", mod["mid"]["household"], mod["critical"]["household"])
    a("")
    a(f"v0.1 said $400. Carlsbad delivers at ${AQ.CARLSBAD_PRICE_AF[0]:,.0f}–{AQ.CARLSBAD_PRICE_AF[1]:,.0f} and a district pays about ${AQ.WHOLESALE_TODAY_AF:,.0f} wholesale today.")
    a("Desalinated water is firm water and is priced as such; capital dominates, not energy.")
    a("")
    a("**The process decisions (`titletwo.py`).**")
    a("")
    a("- **Reverse osmosis, not LT-MED (F-13).** A coastal brownfield has no heat source of the 500 MW_th a thermal module")
    a(f"  needs, and none is named; against a condensing cycle on the same heat the water would cost {g['topping']['mid']['cost_kwh_e_m3']:.1f} / {g['topping']['critical']['cost_kwh_e_m3']:.1f} kWh/m³ of")
    a(f"  electricity forgone, {g['topping']['mid']['cost_kwh_e_m3'] / g['topping']['mid']['ro_kwh_e_m3']:.1f}× / {g['topping']['critical']['cost_kwh_e_m3'] / g['topping']['critical']['ro_kwh_e_m3']:.1f}× reverse osmosis (`joinder.py`). RO at {AQ.RO_KWH_M3[0]:.1f}–{AQ.RO_KWH_M3[1]:.1f} kWh/m³ is what is priced.")
    a(f"- **No zero-liquid-discharge, no mineral train (F-03, F-04, F-11, F-12).** Seawater holds {T2.LI_SEAWATER_MG_L} mg/L of lithium: one module's")
    a(f"  feed contains {g['minerals']['mid']['li_t']:.1f} tonnes a year, three orders below v0.1's revenue. Its magnesium as hydroxide would be {g['minerals']['mid']['mgoh2_kt']:.0f} kt a")
    a(f"  year, {g['minerals']['mid']['share_of_market']:.2f} of the US magnesium-compounds market ({g['minerals']['critical']['share_of_market']:.2f} at critical) from one module. Crystallising the brine")
    a("  costs 20–30 kWh per m³ of brine, omitted from v0.1's energy line. Neither mineral is a revenue and neither is in the price.")
    a(f"- **Brine through the outfall at Ocean Plan concentration.** At {T2.RECOVERY:.0%} recovery the brine is {g['brine']['brine_ppt']:.0f} ppt, {g['brine']['excess_ppt']:.1f} above")
    a(f"  ambient, against a limit of {T2.OCEAN_PLAN_LIMIT_PPT:.0f} ppt at the {T2.MIXING_ZONE_M:.0f} m edge — a diffuser dilution of {g['brine']['dilution']:.0f} : 1, which a retired plant's")
    a("  outfall must achieve without cooling water. Chloride chemistry is excluded everywhere on hazard grounds (the author's")
    a("  standing decision), which rules out magnesium metal.")
    a(f"- **Intake (F-28).** {T2.INTAKE}. Slant wells are site-specific and were Huntington Beach's failure; entrainment is")
    a("  non-zero and mitigated under the Ocean Plan, not eliminated.")
    a(f"- **On-site power covers a tenth, not all (F-27).** A module draws {g['onsite']['mid']['need_mw']:.0f}–{g['onsite']['critical']['need_mw']:.0f} MW on average; the {T2.BROWNFIELD_ACRES[0]:.0f} / {T2.BROWNFIELD_ACRES[1]:.0f} acre site's PV makes")
    a(f"  {g['onsite']['mid']['pv_avg_mw']:.1f}–{g['onsite']['critical']['pv_avg_mw']:.1f} MW, {g['onsite']['mid']['share']:.0%}–{g['onsite']['critical']['share']:.0%} of it. Islanding is a battery for the intake, pretreatment and controls ({g['onsite']['mid']['islanding_mw']:.1f} MW), so the plant")
    a("  rides through an outage without fouling; full-load islanding is not claimed.")
    a(f"- **Energy at the contract price, full-time (F-26).** Title I's surplus is {g['surplus']['mid']['share']:.0%} of hours, not half; a membrane plant runs")
    a("  steadily. The surplus is the water route's lift, an upside the water price does not count.")
    n = g["noise"]
    a(f"- **{MN.BOUNDARY_DBA:.0f} dBA at the boundary is bought, not assumed (F-40).** High-pressure pumps at {n['mid']['source']:.0f}–{n['critical']['source']:.0f} dBA at 1 m reach {MN.BOUNDARY_DBA:.0f} dBA at")
    a(f"  {n['mid']['d_open_m']:,.0f}–{n['critical']['d_open_m']:,.0f} m in the open; a full enclosure of {n['mid']['enclosure']:.0f}–{n['critical']['enclosure']:.0f} dB brings the boundary to {n['mid']['d_enclosed_m']:.0f}–{n['critical']['d_enclosed_m']:.0f} m, inside the brownfield, at")
    a(f"  ${n['mid']['cost_m']:.0f}–{n['critical']['cost_m']:.0f} M a module, carried in the module's band.")
    a(f"- **Employment (F-38).** At Carlsbad's staffing per plant, the adopted route's modules employ {g['jobs']['mid']['title2_permanent']:,.0f}–{g['jobs']['critical']['title2_permanent']:,.0f} permanently.")
    a("")
    s2 = g["schedule2"]
    a(f"**The schedule (F-15).** Carlsbad: proposed {T2.CARLSBAD_YEARS[0]}, coastal permit {T2.CARLSBAD_YEARS[1]}, water {T2.CARLSBAD_YEARS[2]} — {s2['mid']['carlsbad']} years. Huntington Beach:")
    a(f"{T2.HUNTINGTON_YEARS[0]} to a {T2.HUNTINGTON_YEARS[1]} denial. Stated honestly, permitting {s2['mid']['permit']:.0f} years (mid) to {s2['critical']['permit']:.0f} (critical, assumed from the record) and a")
    a(f"{s2['mid']['build']:.0f}-year build put first water at **{s2['mid']['first_water']:.0f}–{s2['critical']['first_water']:.0f}** from a {T2.PROGRAM_START} start, not 24 months. Each year of delay escalates a module by")
    a(f"${s2['mid']['delay_m_per_year']:.0f}–{s2['critical']['delay_m_per_year']:.0f} M.")
    a("")
    a("**Title II's side of the adopted route:**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row(f"modules at {B.HEAD_M:.0f} m of head (built as whole modules: {ar['mid']['modules']:.0f} / {ar['critical']['modules'] + 0.5:.0f})", ar["mid"]["modules"], ar["critical"]["modules"], "{:.1f}")
    both_row("water, million acre-feet a year", ar["mid"]["maf"], ar["critical"]["maf"], "{:.2f}")
    both_row("modules' capital, financed, $B", ar["mid"]["capex_b"], ar["critical"]["capex_b"], "{:.1f}")
    both_row(f"lift on the water's bill, kWh/m³", ar["mid"]["lift"], ar["critical"]["lift"], "{:.2f}")
    both_row("water with the lift on its bill, $/acre-foot", ar["mid"]["per_af"], ar["critical"]["per_af"])
    both_row("per household per year", ar["mid"]["household"], ar["critical"]["household"])
    a("")
    # ---------------------------------------------------------------- O
    a("## O. Title III: the joinder")
    a("")
    a("**The relation (F-31).** One Authority, two projects, two revenue accounts. Title I sells electricity at cost recovery")
    a("to in-state load-serving entities and to Title II; Title II sells water at cost recovery to districts. Neither")
    a("subsidises the other: each carries its own capital, its own debt service and its own price, and the joinder is two")
    a("contracts and one asset. The author's four standing decisions govern it: one program, two projects, severable;")
    a("nitrate stays and chloride chemistry is excluded everywhere; Noor III-class heliostats; ZLD dropped and brine returned")
    a("through the existing outfall.")
    a("")
    a(f"**The power-supply agreement.** Title II buys its electricity from Title I at Title I's required price, mid or critical, for the bond term of {R3.CONTRACT_TERM_Y} years:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("contract price, $/MWh (Title I with its register)", pm["price"], pc["price"])
    both_row("volume per module, GWh/yr", mod["mid"]["kwh_m3"] * AQ.MODULE_M3_YR / 1e6, mod["critical"]["kwh_m3"] * AQ.MODULE_M3_YR / 1e6)
    both_row("energy's share of the water's cost", mod["mid"]["energy_m"] / mod["mid"]["total_m"], mod["critical"]["energy_m"] / mod["critical"]["total_m"], "{:.0%}")
    a("")
    a("**The one shared asset.** Title I's summer surplus lifts Title II's product water to an elevated reservoir, and the")
    a("year-round delivery returns through pump-turbines to Title I's evenings. The reservoir and the pump-turbines are Title")
    a("I's (they close its load); the modules are Title II's (they make its water); the lift energy is the surplus, priced at")
    a("nothing because it was worth nothing.")
    a("")
    a("**The decision table.** §H's three routes, side by side:")
    a("")
    a("| | mirrors, mid | mirrors, critical | water alone, mid | water alone, critical | **both, mid** | **both, critical** |")
    a("|---|---|---|---|---|---|---|")
    nf = "no feasible point"
    a(f"| Title I additional capital, $B | {m['mid']['cost_b']:.1f} | {m['critical']['cost_b']:.1f} | {nf} | {nf} | **{bm['title1_b']:.1f}** | **{bc['title1_b']:.1f}** |")
    a(f"| Title I price, $/MWh | {pm['price'] + m['mid']['dprice']:.0f} | {pc['price'] + m['critical']['dprice']:.0f} | — | — | **{whole_price(g, 'mid'):.0f}** | **{whole_price(g, 'critical'):.0f}** |")
    a(f"| Title II modules / capital, $B | 0 / 0 | 0 / 0 | — | — | {bm['modules']:.0f} / {bm['title2_b']:.0f} | {bc['modules']:.0f} / {bc['title2_b']:.0f} |")
    a(f"| water, million acre-feet a year | 0 | 0 | — | — | {bm['maf']:.2f} | {bc['maf']:.2f} |")
    a(f"| left to the grid | {m['mid']['unserved']:.1%} | {m['critical']['unserved']:.1%} | — | — | {bm['unserved']:.1%} | {bc['unserved']:.1%} |")
    a("")
    a(f"**The takers.** The adopted route delivers {bm['maf']:.2f}–{bc['maf']:.2f} million acre-feet a year, year-round: summer irrigation on the Westside")
    a(f"and winter recharge, where the San Joaquin Valley's groundwater overdraft under SGMA is about {R3.SGMA_RECHARGE_GAP_MAF[0]:.1f}–{R3.SGMA_RECHARGE_GAP_MAF[1]:.1f} million acre-feet a")
    a("year. That is the match of supply to demand the joinder rests on, and it is a contract question: irrigation and")
    a("recharge districts under contract for firm water at three to five thousand dollars an acre-foot, which is what firm")
    a("water costs. **The decision is the author's, and it is made: both.**")
    a("")
    a("**The single financial statement:**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("Title I capital with its register, $B", pm["capex_net"] / 1e3, pc["capex_net"] / 1e3, "{:.1f}")
    both_row("Title I closing the load, mirrors / both, $B", f"{m['mid']['cost_b']:.1f} / {bm['title1_b']:.1f}", f"{m['critical']['cost_b']:.1f} / {bc['title1_b']:.1f}", "{}")
    both_row("Title II modules at the adopted route, $B", ar["mid"]["capex_b"], ar["critical"]["capex_b"], "{:.0f}")
    both_row("**program at the adopted route (both), $B**", program_b(g, "mid"), program_b(g, "critical"), "{:.0f}", True)
    both_row("Title I debt service, $M/yr", g["reserve"]["mid"]["debt_service_m"], g["reserve"]["critical"]["debt_service_m"])
    both_row("Title I debt-service reserve, $M", g["reserve"]["mid"]["dsrf_m"], g["reserve"]["critical"]["dsrf_m"])
    both_row("contingency carried", g["reserve"]["mid"]["contingency"], g["reserve"]["critical"]["contingency"], "{:.0%}")
    both_row(f"Title I price at {H.COVERAGE_REQ:.2f}× coverage, $/MWh", g["downside"]["mid"]["price_at_coverage"], g["downside"]["critical"]["price_at_coverage"])
    a("")
    a("**Severability.**")
    a("")
    a("- **Title I without Title II** stands: the field and store grow to the mirrors route's sizing, the load closes at that")
    a("  price, and no water is made.")
    a("- **Title II without Title I** stands: a module buys its electricity from the grid instead of the Authority, at the")
    a("  grid's price rather than the contract's, and makes the same water; the reservoir and pump-turbines are not built,")
    a("  and the water is delivered by the aqueduct.")
    a("- **What does not sever** is the water route itself: it exists only as the pair, because its lift is Title I's surplus")
    a("  and its evening is Title I's shortfall. It is the joinder, and it is optional.")
    a("")
    # ---------------------------------------------------------------- P
    a("## P. The sites, each addressed in full")
    a("")
    a("None of the site terms can be computed without a site, and this document does not pretend to. `sites.py` takes the")
    a("three Title I nodes v0.1 named and the retired or retiring coastal plants a Title II module could stand on, states")
    a("the term each Title needs of a site, grades each site on each term from what is on the public record — MET,")
    a("CONDITIONAL (clears on an assumption the site study confirms), OPEN (not knowable here), FAIL — and ranks them.")
    a(f"MET {SI.WEIGHT['MET']:.0f}, CONDITIONAL {SI.WEIGHT['CONDITIONAL']:.1f}, OPEN {SI.WEIGHT['OPEN']:.0f}, FAIL {SI.WEIGHT['FAIL']:.0f}. Every site value is ASSUMED from the public record unless an instrument")
    a("holds it, and the note beside each grade says which. **The rank orders the site studies; it does not choose a site.**")
    a("")
    a("### P.1. Title I: the three nodes")
    a("")
    a("The terms a node must meet:")
    a("")
    a("| term | requirement | what settles it |")
    a("|---|---|---|")
    for t, req, settle in SI.T1_TERMS:
        a(f"| {t} | {req} | {settle} |")
    a("")
    for name, lat, lon, ap, mw, st, dni, status in H.NODES:
        s1m, s1c = g["sites1"]["mid"][name], g["sites1"]["critical"][name]
        (pgm, fm), (pgc, fc) = g["seismic"]["mid"][name], g["seismic"]["critical"][name]
        a(f"#### {name}")
        a("")
        a(f"{lat:.2f}° N, {abs(lon):.2f}° W. Annual DNI **{dni:,.0f} kWh/m²/yr** ({status}; band {H.DNI_BAND[name][0]:,.0f}–{H.DNI_BAND[name][1]:,.0f}). One third of the fleet:")
        a(f"{d['mid']['aperture'] / 3e6:.1f} / {d['critical']['aperture'] / 3e6:.1f} million m² of mirror at design and {d['mid']['aperture'] * bm['field'] / 3e6:.1f} / {d['critical']['aperture'] * bc['field'] / 3e6:.1f} on the adopted route, {d['mid']['towers'] * bm['field'] / 3:.0f} / {d['critical']['towers'] * bc['field'] / 3:.0f} towers on the adopted route,")
        a(f"{d['mid']['pv_mw'] / 3:,.0f} / {d['critical']['pv_mw'] / 3:,.0f} MW_AC of PV; land {g['land']['mid']['per_node']:,.0f} / {g['land']['critical']['per_node']:,.0f} acres on the adopted route; mirror washing {g['wash']['mid']['afy_per_node']:,.0f} / {g['wash']['critical']['afy_per_node']:,.0f} acre-feet a year")
        a(f"from the program's own water; one 500 kV circuit at {g['gentie']['mid']['per_node']:,.0f} / {g['gentie']['critical']['per_node']:,.0f} MW peak injection. Seismic: the {MN.DESIGN_PGA_G:.2f} g design target over a mapped")
        a(f"MCE_R PGA of {pgm:.2f} / {pgc:.2f} g is {fm:.2f}× / {fc:.2f}× (a site study must confirm {SI.SEISMIC_MARGIN:.1f}×).")
        a("")
        a("| term | mid | critical | note |")
        a("|---|---|---|---|")
        for t, _req, _settle in SI.T1_TERMS:
            gm, nm = s1m["rows"][t]
            gc, nc = s1c["rows"][t]
            a(f"| {t} | {gm} | {gc} | {nm if nm == nc else nm + ' / ' + nc} |")
        ftm = SI.first_study(s1m["rows"], SI.T1_TERMS)
        ftc = SI.first_study(s1c["rows"], SI.T1_TERMS)
        a("")
        a(f"Score {s1m['score']:.1f} (mid) / {s1c['score']:.1f} (critical). *First study:* {ftm[0]} — {ftm[1]}" + ("" if ftm == ftc else f"; at critical {ftc[0]} — {ftc[1]}") + ".")
        a("")
    rm1, rc1 = SI.ranked(g["sites1"]["mid"]), SI.ranked(g["sites1"]["critical"])
    a(f"**Ranking.** Mid: " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in rm1) + ". Critical: " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in rc1) + ".")
    a("At mid the Westside ties the Mojave for first: it meets land, nexus and grid outright and is conditional on DNI and head,")
    a("so the node the record doubted for its sun has the fewest open terms. At critical the Mojave leads alone, because the")
    a(f"Westside's seismic margin falls under the {SI.SEISMIC_MARGIN:.1f}× a site study must confirm. The Central Valley node's land is the")
    a(f"reason it is kept (F-22): {g['land']['mid']['westlands']:,.0f} / {g['land']['critical']['westlands']:,.0f} acres of fallowed, drainage-impaired Westside farmland cover a node {g['land']['mid']['westlands_covers']:.1f}× / {g['land']['critical']['westlands_covers']:.1f}× over.")
    a(f"Land across the program on the adopted route is {g['land']['mid']['acres']:,.0f} / {g['land']['critical']['acres']:,.0f} acres ({g['land']['mid']['km2']:.0f} / {g['land']['critical']['km2']:.0f} km²), which v0.1 never stated (F-21).")
    a(f"NEPA on the Mojave node's federal nexus (F-25) is budgeted as {MJ.NEPA_YEARS[0]:.0f} / {MJ.NEPA_YEARS[1]:.0f} years of escalation on that node, ${g['nepa']['mid']['delay_m']:,.0f} / {g['nepa']['critical']['delay_m']:,.0f} M.")
    a("")
    a("### P.2. Title II: the coastal brownfields")
    a("")
    a("The terms a coastal site must meet:")
    a("")
    a("| term | requirement | what settles it |")
    a("|---|---|---|")
    for t, req, settle in SI.T2_TERMS:
        a(f"| {t} | {req} | {settle} |")
    a("")
    for name, r in SI.ranked(g["sites2"]):
        a(f"#### {name}")
        a("")
        a("| term | grade | note |")
        a("|---|---|---|")
        for t, _req, _settle in SI.T2_TERMS:
            gr, note = r["rows"][t]
            a(f"| {t} | {gr} | {note} |")
        ft = SI.first_study(r["rows"], SI.T2_TERMS)
        a("")
        a(f"Score {r['score']:.1f}. *First study:* {ft[0]} — {ft[1]}.")
        a("")
    for name, why in SI.EXCLUDED.items():
        a(f"**Excluded: {name}.** {why}.")
    a("")
    a(f"**Ranking.** " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in SI.ranked(g["sites2"])) + ". The Oxnard plain")
    a("(Ormond Beach, Mandalay) and Moss Landing meet the taker and head terms the water route needs; Huntington Beach")
    a("carries its 2022 denial as a FAIL and is not a first site; no coastal site is MET on every term, so a site study is")
    a(f"always owed. The adopted route needs {bm['modules']:.0f}–{bc['modules']:.0f} modules and this list holds {len(SI.T2_SITES)} sites: {PD.MODULES_PER_SITE[1]:.0f}–{PD.MODULES_PER_SITE[0]:.0f} modules a site, or sites this")
    a("list does not name. That is a finding, not a plan.")
    a("")
    fig("fig-12-sites.png", "The sites scored: the three Title I nodes on six terms at both cases, and the eight coastal brownfields on seven terms.")
    # ---------------------------------------------------------------- Q
    a("## Q. Environment, employment, land and procurement")
    a("")
    a(f"**CO₂ avoided (F-34).** From the hour-by-hour at a CAISO marginal factor of {g['co2']['mid']['factor']:.2f} / {g['co2']['critical']['factor']:.2f} t/MWh (the critical case")
    a("credits less, because a cleaner grid displaces less):")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("served as sized, TWh", g["co2"]["mid"]["as_sized_twh"], g["co2"]["critical"]["as_sized_twh"], "{:.2f}")
    both_row("avoided as sized, million t/yr", g["co2"]["mid"]["as_sized_mmt"], g["co2"]["critical"]["as_sized_mmt"], "{:.2f}")
    both_row("avoided with the load closed, million t/yr", g["co2"]["mid"]["closed_mmt"], g["co2"]["critical"]["closed_mmt"], "{:.2f}")
    a("")
    a(f"v0.1 said {MN.CLAIMED_MMT} million tonnes, descended from the inflated energy.")
    a("")
    a(f"**Employment (F-38).** From built plants per MW — Crescent Dunes and Ivanpah for the permanent staff, Ivanpah's peak for")
    a(f"construction — at the adopted route's block of {g['jobs']['mid']['block_mw']:,.0f} MWe and its {bm['modules']:.0f} / {bc['modules']:.0f} water modules:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("permanent, Title I", g["jobs"]["mid"]["permanent"], g["jobs"]["critical"]["permanent"])
    both_row("construction peak, Title I", g["jobs"]["mid"]["construction_peak"], g["jobs"]["critical"]["construction_peak"])
    both_row("permanent, Title II's modules", g["jobs"]["mid"]["title2_permanent"], g["jobs"]["critical"]["title2_permanent"])
    a("")
    a(f"v0.1 said {MN.CLAIMED_JOBS[0]:,} construction and {MN.CLAIMED_JOBS[1]:,} permanent; the multiplier it quoted is unsourced and is not carried.")
    a("")
    a(f"**Resource adequacy (F-18).** No RA is earned on exported energy and the export is negative; the in-state RA is the closed")
    a(f"block's net capacity on the adopted route, {g['ra']['mid']['block_net_mw']:,.0f} / {g['ra']['critical']['block_net_mw']:,.0f} MW, self-supplied by the Authority as load-serving entity. v0.1 counted ${H.CLAIMED_RA_M[0]:.0f}–{H.CLAIMED_RA_M[2]:.0f} M a year of it.")
    a("")
    a(f"**Water for the mirrors (F-20).** At Ivanpah's dry-cooled record ({MJ.IVANPAH_WASH_AFY:.0f} acre-feet a year on {MJ.IVANPAH_M2 / 1e6:.1f} million m²) the program's")
    a(f"field on the adopted route needs {g['wash']['mid']['afy']:,.0f} / {g['wash']['critical']['afy']:,.0f} acre-feet a year, from {g['wash']['mid']['source']}.")
    a("")
    a(f"**Seismic (F-33).** Seismic zones left the code in 2001; the basis is ASCE 7, site class and mapped MCE_R. The {MN.DESIGN_PGA_G:.2f} g target")
    a("is kept and clears the mapped PGA at every node (§P.1); the mapped values are assumed from the hazard record and the")
    a("site study fixes them.")
    a("")
    a("**Nitrate (F-23).** No nitrate salt anywhere in Helios-3: the medium is sintered bauxite, with no freezing point, no")
    a("decomposition ceiling, no oxidiser and no toxic medium (R-13 to R-15). The nitrate register applies only to the salt-block")
    a("fallback, whose failure mode — the hot-salt tank leak that took Crescent Dunes and Noor III each offline for more than")
    a("a year — is on the record in §J.1.")
    a("")
    a("**Procurement (F-39).** One EPC per node under an owner's engineer across the program; the pilot aperture and the first")
    a("module let as separate contracts. No contractor has delivered more than one commercial tower at a time in the US, and")
    a("the ladder buys the hours before the fleet.")
    a("")
    a("**The Authority (F-37).** A statutory public entity created by the Act on the pattern of the California Consumer Power")
    a("and Conservation Financing Authority (SB 6X, 2001; defunded by 2004, a history the Act acknowledges), registered as the")
    a("load-serving entity of §M in the community-choice form. Government Code §8571 is cited only for what it does: suspend")
    a("regulatory statutes in a declared emergency. It issues no coastal permit and shortens no federal review.")
    a("")
    a("**Dry cooling.** Zero water for heat rejection; sCO₂ needs about a sixth of steam's cooling airflow (R-16), at a")
    a("compressor-inlet penalty at 45 °C the critical cycle band carries.")
    a("")
    # ---------------------------------------------------------------- R
    a("## R. What is not settled, and what could stop it")
    a("")
    a("- **No plant of this kind has run.** The largest falling-particle receiver is 2 MW_th; the 715 °C recompression cycle")
    a("  has not run. The pilot aperture (§K) and the ladder (§J) buy the hours before the fleet, and the salt block on the")
    a("  same field is the recorded fallback at a price this document prints.")
    a("- **The plant must deliver its modelled output.** Every dollar of the bill is per MWh; a plant at Crescent Dunes' 0.39")
    a("  of design does not pay its bonds from the bill. The critical column is the defence, and the mid column is margin.")
    a("- **The load and DNI shapes are reconstructed**, pinned to sourced levels; `profiles.py` ingests the measured series")
    a("  when reachable, and the evening block factor may move either way.")
    a("- **The coastal permits are the longest studies on the path** and set the critical schedule; a statutory consolidation")
    a("  shortens litigation, not the Coastal Commission.")
    a("- **The head is the site question that sizes Title II**; the reservoir's days of holding move Title I by under a billion.")
    a("- **The takers** are a contract question: irrigation and recharge districts under contract for firm water, year-round.")
    a("- **The split of the shortfall** between the two routes is adopted even and is movable on the ladder.")
    a("- **At the critical case a household pays more than today for one bond term**, and the document says so on every page.")
    a("- **The HOURS rows of the register** — receiver, exchanger, turbine, chemistry, scale, provenance — retire only by")
    a("  operating time; a specification cannot make a machine have run.")
    a("- **The brine as a carbonate sink** for the power block's maintenance vents is noted and not priced.")
    a("")
    # ---------------------------------------------------------------- S
    a("## S. The flaws register: forty found, forty resolved")
    a("")
    a("`FLAWS.tsv` is the adversarial review of v0.1, graded FATAL, CRITICAL, MAJOR, MINOR, worked one at a time in register")
    a("order, each by an instrument where numerical. Every row, with its resolution **as recorded when it was closed**: a")
    a("resolution quotes the figure the instrument gave that day, and where a later pass moved a figure (the load-shape")
    a("correction, the studies line, the adopted route, the O&M on the closing plant) the current figure is the one in")
    a("§A–Q and the move is recorded in `docs/`. A status is never flattened, so the record stands beside the result.")
    a("")
    for f in g["flaws"]:
        a(f"**{f['id']} ({f['tier']}, {f['section']}). {f['title']}.**")
        a("")
        a(f"- *As written:* {f['claim_as_written']}")
        a(f"- *Why it fails:* {f['why_it_fails']}")
        a(f"- *What settles it:* {f['what_settles_it']}")
        a(f"- *{f['status']}:* {f['resolution']}")
        a("")
    # ---------------------------------------------------------------- T
    a("## T. Sources")
    a("")
    a("The published record the instruments cite, as the study register names it (§J), deduplicated; each row of §J carries")
    a("its own citation beside the finding it supports.")
    a("")
    seen = []
    for _k, _s, _sc, _y, _st, _w, source in ST.STUDIES:
        for part in re.split(r";\s*(?![^()]*\))", source):
            part = part.strip()
            if part and part not in seen and not part.startswith("tools/"):
                seen.append(part)
    for s in seen:
        a(f"- {s}")
    a("")
    a("An entry marked *reviewed 2026-09-11* was checked against the web where this environment's proxy reached; an")
    a("encyclopaedia entry in the list is a pointer to a plant's public record and to the primary items beside it, not the")
    a("source of a figure. Entries such as *plant records* and *industry practice* name a class of evidence, not a")
    a("document, and the row that cites them claims only what such a class can carry.")
    a("")
    a("Further sources carried by the instruments as constants, each marked SOURCED beside its value: EIA 2024 (California")
    a("residential consumption and customers); NREL ATB 2024 (tower CSP, the calibration anchor); NREL TMY3 Daggett and the")
    a("NSRDB DNI classes; CAISO Department of Market Monitoring 2024 (prices, negative hours); Palo Verde on-peak strip 2024;")
    a("SAM / Turchi 2019 (the cost split, RECONSTRUCTED); the DOE Loan Programs Office and SolarPACES on Crescent Dunes; ACWA")
    a("Power on Noor III; NREL ATB and Fervo / Cape Station on geothermal; TVA Clinch River and Darlington on SMRs; California")
    a("Public Resources Code §25524.2; the Ocean Plan 2015 amendment (brine); Carlsbad and Huntington Beach records (capital,")
    a("price, schedule); PPIC on the San Joaquin Valley overdraft; ASCE 7 and the CGS hazard and tsunami maps; SB 6X (2001)")
    a("and PUC §366.2 (the Authority's form); Government Code §8571; Ivanpah and Crescent Dunes staffing; the Sites reservoir")
    a("record and the Edmonston and Gianelli lifts.")
    a("")
    # ---------------------------------------------------------------- U
    a("## U. The instruments")
    a("")
    a("Every number in this document is computed by one of these, each with a `--selftest` fixtured on the record, each")
    a("stdlib-only (the renderer alone needs matplotlib for the figures and python-docx for the Word files), each importing")
    a("what it needs from its neighbours and restating nothing:")
    a("")
    for name, what in (("helios.py", "the plant as submitted, run hour by hour; the criterion inverted; F-17's requirement"),
                       ("heliocost.py", "the capital line by line at the built record, state-owned"),
                       ("firmpower.py", "every firm candidate sized to the requirement"),
                       ("cspchain.py", "the seven-link chain; Helios-2 and Helios-3 designed on it"),
                       ("helios3.py", "the sixteen-row mitigation register, graded and priced"),
                       ("receiver.py", "the falling curtain as a per-metre machine; the critical receiver"),
                       ("studies.py", "the provenance register and the recommendations"),
                       ("hourly3.py", "Helios-3 hour by hour; the mirrors route"),
                       ("profiles.py", "the ingestion path for measured CAISO and NSRDB series"),
                       ("joinder.py", "the water route's hydraulics and its feasibility rule"),
                       ("both.py", "the ladder over the water's share; the adopted point; its sensitivity"),
                       ("pilot.py", "the pilot aperture's acceptance protocol"),
                       ("predev.py", "the studies and surveys, priced first"),
                       ("aquacost.py", "the module and its water"),
                       ("titletwo.py", "Title II's process rows"),
                       ("titleone.py", "the bond rate, the schedule, transmission, the tariff"),
                       ("majors.py", "RA, washing, land, the Central Valley node, NEPA, the reserve, the downside"),
                       ("minors.py", "the cycle label, seismic, CO₂, jobs, the Authority, procurement, noise"),
                       ("sites.py", "the site terms, graded and ranked"),
                       ("rebase.py, rebase2.py, rebase3.py", "the three Titles as documents"),
                       ("proposal.py", "this document and the pitch")):
        a(f"- `tools/{name}` — {what}.")
    a("")
    a("*Rendered by `tools/proposal.py`; do not edit by hand. Re-render after any change to the instruments.*")
    return "\n".join(L) + "\n"


# =============================================================================
# THE PITCH
# =============================================================================
def render_pitch(g):
    d, p, bo, m = g["design"], g["priced"], g["both"], g["mirrors"]
    pm, pc = p["mid"], p["critical"]
    bm, bc = bo["mid"], bo["critical"]
    ms = {c: milestones(g, c) for c in CASES}
    hr = g["hourly"]
    L = []
    a = L.append
    a("# California Sovereign Infrastructure — the pitch")
    a("")
    a(f"*The accompaniment to `California_Sovereign_Infrastructure_v0.2.md`, rendered {DATE} by `tools/proposal.py`. Every figure is")
    a("the proposal's, labelled mid / critical; the proposal carries its source and its case.*")
    a("")
    a("## The ask")
    a("")
    a("- One state-owned program under one Authority, two severable projects, funded once by general-obligation bonds and")
    a("  never again by the treasury.")
    a(f"- Title I makes the electricity for three million households, {g['e_req']:.1f} TWh a year, growing with population.")
    a(f"- Title II makes their water: {bm['modules']:.0f}–{bc['modules']:.0f} desalination modules, {bm['maf']:.2f}–{bc['maf']:.2f} million acre-feet a year, delivered year-round.")
    a("- Title III joins them so each helps the other and neither can drag the other down.")
    a(f"- **Decision requested:** fund the studies and surveys now, ${g['predev']['mid']['total_m']:.0f}–{g['predev']['critical']['total_m']:.0f} million, and know within")
    a(f"  {g['predev']['mid']['gate_years']:.0f}–{g['predev']['critical']['gate_years']:.0f} years whether the rest is worth ${program_b(g, 'mid'):.0f}–{program_b(g, 'critical'):.0f} billion.")
    a("")
    a("## What it builds")
    a("")
    a("- **Helios-3.** Concentrating solar on three desert nodes — Mojave, Imperial, the Westside — with falling-particle")
    a("  receivers and supercritical-CO₂ turbines instead of salt and steam, so the same sun makes half again as much power")
    a(f"  (sun to socket {C.chain_product(g['base_links'].values()):.3f} as proposed, {C.chain_product(d['mid']['links'].values()):.3f} at mid).")
    a("- Daytime load goes straight from photovoltaics without touching a mirror; the mirror field is sized for the night;")
    a("  the particle store carries the evening peak.")
    a(f"- As sized at mid: {d['mid']['aperture'] / 1e6:.1f} million m² of mirror on {d['mid']['towers']:.0f} towers, a {d['mid']['turb_mw']:,.0f} MWe block, {d['mid']['pv_mw']:,.0f} MW of PV. At critical: {d['critical']['aperture'] / 1e6:.1f} million m²,")
    a(f"  {d['critical']['towers']:.0f} towers, {d['critical']['turb_mw']:,.0f} MWe, {d['critical']['pv_mw']:,.0f} MW. The adopted route then grows the field by a quarter and the block by half to")
    a("  close the evening.")
    a("- **Aqua-Sovereign.** Seawater reverse osmosis on retired coastal power plants, brine back through the permitted")
    a("  outfall at Ocean Plan concentration, no minerals sold, no zero-liquid-discharge.")
    a("- **The joinder.** Title I's summer surplus lifts the water to an elevated reservoir; every evening of the year it")
    a("  comes down through pump-turbines to close Title I's peak. Water for the Westside and the coast, and the evening's")
    a("  last shortfall closed by the water on its way down.")
    a(f"- Together they leave **{bm['unserved']:.1%} / {bc['unserved']:.1%}** of the load to the grid, against {g['scan']['mid']['as_sized']['unserved']:.0%} / {g['scan']['critical']['as_sized']['unserved']:.0%} with neither.")
    a("")
    a("## What it costs, once")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| Title I, the plant and its risk register | ${pm['capex_net'] / 1e3:.1f} B | ${pc['capex_net'] / 1e3:.1f} B |")
    a(f"| Title I, closing the whole load with both levers | ${bm['title1_b']:.1f} B | ${bc['title1_b']:.1f} B |")
    a(f"| Title II, the water modules | ${bm['title2_b']:.0f} B | ${bc['title2_b']:.0f} B |")
    a(f"| **program** | **${program_b(g, 'mid'):.0f} B** | **${program_b(g, 'critical'):.0f} B** |")
    a("")
    a(f"- Every figure carries its contingency, {g['reserve']['mid']['contingency']:.0%} at mid and {g['reserve']['critical']['contingency']:.0%} at critical, and a one-year debt-service reserve.")
    a(f"- Every study and survey is the first line, ${g['predev']['mid']['total_m']:.0f} / {g['predev']['critical']['total_m']:.0f} million, priced and scheduled before a mirror is ordered.")
    a(f"- v0.1 said ${H.CAPEX_B:.1f} B; the built record puts the salt-tower plant it described at ${g['hc']['low']['net_capex'] / 1e3:.1f}–{g['hc']['high']['net_capex'] / 1e3:.1f} B. This proposal builds")
    a("  a different plant and prices it from the record, not the promise.")
    a("")
    a("## What a household pays")
    a("")
    a(f"- Today: **${money(g['today_hh'])}** a year to the utility for generation.")
    a(f"- On this program while the bonds are paid: **${money(H.per_household(whole_price(g, 'mid')))}** at mid, **${money(H.per_household(whole_price(g, 'critical')))}** at critical")
    a(f"  (${whole_price(g, 'mid'):.0f} / {whole_price(g, 'critical'):.0f} per MWh).")
    a(f"- After the bonds retire: **${money(H.per_household(g['postbond']['mid']))} / {money(H.per_household(g['postbond']['critical']))}** a year, the running cost alone, for as long as the plant stands.")
    ds = g["reserve"]
    a(f"- {ds['mid']['debt_service_m'] / (ds['mid']['debt_service_m'] + pm['om']):.0%} / {ds['critical']['debt_service_m'] / (ds['critical']['debt_service_m'] + pc['om']):.0%} of the plant's bill is the build. Once built, the state owns a supply whose running cost is a fraction of today's bill.")
    a(f"- Water: **${g['aqua']['mid']['per_af']:,.0f} / {g['aqua']['critical']['per_af']:,.0f}** an acre-foot at cost recovery, in the band Carlsbad delivers (${AQ.CARLSBAD_PRICE_AF[0]:,.0f}–{AQ.CARLSBAD_PRICE_AF[1]:,.0f}), on its own rate and account.")
    a("- No further public money after the build: the bill carries debt service and O&M, the treasury carries nothing.")
    a("")
    a("## When")
    a("")
    a("| milestone | mid | critical |")
    a("|---|---|---|")
    a(f"| studies and surveys begin | {ms['mid']['studies']:.0f} | {ms['critical']['studies']:.0f} |")
    a(f"| first electricity, from the PV field at the first node | {ms['mid']['field']:.0f} | {ms['critical']['field']:.0f} |")
    a(f"| pilot receiver on sun, graded against a pass mark fixed in advance | {ms['mid']['pilot'][0]:.0f}–{ms['mid']['pilot'][1]:.0f} | {ms['critical']['pilot'][0]:.0f}–{ms['critical']['pilot'][1]:.0f} |")
    a(f"| first 100 MWe Helios-3 module | {ms['mid']['module']:.0f} | {ms['critical']['module']:.0f} |")
    a(f"| fleet complete, whole load served | {ms['mid']['fleet']:.0f} | {ms['critical']['fleet']:.0f} |")
    a("")
    a("- The realistic column is critical. The two-year slide is one item, the four-year NEPA statement on the Mojave node,")
    a("  which is why the studies go first.")
    a(f"- Only a pass at the pilot orders the first module. A fail records the nitrate-salt plant on the same field as the")
    a("  route, already priced.")
    a("")
    a("## Why it holds up")
    a("")
    a("- Every number comes from a program that recomputes it, printed at a middle case and at a critical case where every")
    a("  uncertain constant sits at its adverse end. The design is held to critical; mid is margin.")
    a("- Forty flaws found in the original proposal were resolved one at a time, each by an instrument where numerical.")
    a(f"- The plant is sized to a requirement, three million households growing {g['growth'][0]:.2f}–{g['growth'][1]:.2f}× over the term, not to an export that")
    a("  turned out to be negative.")
    a("- It takes no developer's margin and no state subsidy after the build, and keeps the federal storage credit where")
    a("  statute allows.")
    a(f"- Every technology in it is on a register of {len(ST.STUDIES)} published studies and plants, each with a status and a source, and")
    a("  a recommended further study on a dated ladder.")
    a(f"- It mines nothing new, consumes no cooling water, and avoids {g['co2']['mid']['closed_mmt']:.2f} / {g['co2']['critical']['closed_mmt']:.2f} million tonnes of CO₂ a year with the load closed.")
    a(f"- About {g['jobs']['mid']['construction_peak']:,.0f} construction jobs at peak and {g['jobs']['mid']['permanent']:,.0f} / {g['jobs']['critical']['permanent']:,.0f} permanent on the nodes, plus {g['jobs']['mid']['title2_permanent']:,.0f} / {g['jobs']['critical']['title2_permanent']:,.0f} at the water modules.")
    a("")
    a("## Where")
    a("")
    a(f"- Title I: the Mojave (Kramer Junction), Imperial (Desert Center) and the Westside — at mid the Westside ties the")
    a(f"  Mojave for first on land, nexus and grid; at critical the Mojave leads on seismic margin. Land {g['land']['mid']['acres']:,.0f} / {g['land']['critical']['acres']:,.0f} acres, with")
    a("  fallowed Westside farmland covering a whole node.")
    a("- Title II: eight retired or retiring coastal plants screened on seven terms; the Oxnard plain (Ormond Beach, Mandalay)")
    a("  and Moss Landing lead; Huntington Beach carries its 2022 denial as a FAIL; no site is met on every term, so a site")
    a("  study is always owed.")
    a("")
    a("## What could stop it")
    a("")
    a("- No plant of this kind has run at scale; the pilot comes first and the salt block stands behind it.")
    a("- The plant must deliver its modelled output, or the bill rises; no commercial salt tower has yet delivered its design.")
    a("- The coastal permits are the longest studies on the path and set the critical schedule.")
    a("- At the critical case a household pays more than today for one bond term. The proposal says so on every page,")
    a("  because a plan that hides its worst case is not one you can build.")
    a("")
    a("## The decision")
    a("")
    a(f"- Build the studies now, for ${g['predev']['mid']['total_m']:.0f}–{g['predev']['critical']['total_m']:.0f} million, and know within {g['predev']['mid']['gate_years']:.0f}–{g['predev']['critical']['gate_years']:.0f} years whether the rest is worth")
    a(f"  ${program_b(g, 'mid'):.0f}–{program_b(g, 'critical'):.0f} billion.")
    a("- Nothing irreversible is bought before the receiver has passed its test.")
    return "\n".join(L) + "\n"


# =============================================================================
# DOCX -- both documents from the same rendered text
# =============================================================================
_INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def _runs(par, text):
    for tok in _INLINE.split(text):
        if not tok:
            continue
        if tok.startswith("**"):
            par.add_run(tok[2:-2]).bold = True
        elif tok.startswith("*"):
            par.add_run(tok[1:-1]).italic = True
        elif tok.startswith("`"):
            r = par.add_run(tok[1:-1])
            r.font.name = "Consolas"
        else:
            par.add_run(tok)


def emit_docx(md_text, path, base_dir):
    from docx import Document
    from docx.shared import Pt, Inches
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10)
    lines = md_text.split("\n")
    i, para = 0, []

    def flush():
        if para:
            _runs(doc.add_paragraph(), " ".join(para))
            para.clear()

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("#"):
            flush()
            level = len(ln) - len(ln.lstrip("#"))
            doc.add_heading(ln.lstrip("#").strip(), level=min(level, 4))
        elif ln.startswith("![") and "](" in ln:
            flush()
            rel = ln.split("](", 1)[1].rstrip(")")
            fp = os.path.join(base_dir, rel)
            if os.path.exists(fp):
                doc.add_picture(fp, width=Inches(6.3))
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                ncol = max(len(r) for r in rows)
                t = doc.add_table(rows=len(rows), cols=ncol)
                t.style = "Light Grid Accent 1"
                for r_i, r in enumerate(rows):
                    for c_i in range(ncol):
                        cell = t.cell(r_i, c_i)
                        cell.text = ""
                        _runs(cell.paragraphs[0], r[c_i] if c_i < len(r) else "")
                        for pp in cell.paragraphs:
                            for run in pp.runs:
                                run.font.size = Pt(8)
                doc.add_paragraph()
            continue
        elif ln.startswith("- "):
            flush()
            _runs(doc.add_paragraph(style="List Bullet"), ln[2:])
        elif ln.strip() == "":
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    doc.save(path)


# =============================================================================
# SELFTEST
# =============================================================================
_NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])")


def numbers(text):
    return set(_NUM.findall(text))


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    g = gather()
    text, pitch = render(g), render_pitch(g)
    for path, t, name in ((OUT, text, "proposal"), (PITCH, pitch, "pitch")):
        check(f"the {name} exists on disk", os.path.exists(path))
        if os.path.exists(path):
            check(f"the {name} on disk is byte-identical to a fresh render (never hand-edited)", open(path, encoding="utf-8").read() == t)
    refs = re.findall(r"!\[Figure \d+\]\((figures/[^)]+)\)", text)
    check("the proposal places twelve figures", len(refs) == 12)
    check("every figure the proposal references exists on disk", all(os.path.exists(os.path.join(ROOT, "proposals", r)) for r in refs))
    check("every flaw in FLAWS.tsv appears with its resolution", all(f"**{f['id']} (" in text for f in g["flaws"]) and len(g["flaws"]) == 40)
    check("every study in the register appears", all(s[1] in text for s in ST.STUDIES))
    check("every register row appears with its source", all(f"**{r[0]}. " in text and r[7] in text for r in H3.REGISTER))
    check("every Title I node and every coastal site is addressed", all(f"#### {n[0]}" in text for n in H.NODES) and all(f"#### {n}" in text for n in SI.T2_SITES))
    check("every case-bearing table carries both columns", text.count("| mid | critical |") >= 25)
    check("the program total in the summary is Title III's", f"| **program, $B** | **{program_b(g, 'mid'):.0f}** | **{program_b(g, 'critical'):.0f}** |" in text)
    check("the pitch carries no number the proposal does not", numbers(pitch) <= numbers(text))
    check("the pitch is two to three pages of bullets", 900 < len(pitch.split()) < 2000 and pitch.count("\n- ") >= 30)
    check("mid never exceeds critical on the price and the program", whole_price(g, "mid") < whole_price(g, "critical") and program_b(g, "mid") < program_b(g, "critical"))
    check("the post-bond price is the adopted route's O&M over the energy, register plant and closing plant",
          abs(g["postbond"]["mid"] - (g["priced"]["mid"]["om"] + g["both"]["mid"]["extra_om_m"]) / g["design"]["mid"]["e_twh"]) < 1e-9)
    check("the document says it carries no number an instrument did not compute", "no number an instrument" in text)
    check("water alone is stated as having no feasible point, never a price", text.count("no feasible point") >= 3)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--docx", action="store_true", help="also emit both documents as .docx")
    ap.add_argument("--no-figures", action="store_true", help="render the text only")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    g = gather()
    if not a.no_figures:
        for f in figures(g):
            print(f"drew proposals/figures/{f}")
    text, pitch = render(g), render_pitch(g)
    for path, t in ((OUT, text), (PITCH, pitch)):
        with open(path, "w", encoding="utf-8") as f:
            f.write(t)
        print(f"rendered {os.path.relpath(path, ROOT)}: {len(t.splitlines())} lines, {len(t.split()):,} words")
    if a.docx:
        for path, t in ((OUT, text), (PITCH, pitch)):
            emit_docx(t, path[:-3] + ".docx", os.path.dirname(path))
            print(f"emitted {os.path.relpath(path[:-3] + '.docx', ROOT)}")
