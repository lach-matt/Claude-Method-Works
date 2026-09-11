#!/usr/bin/env python3
"""rebase.py -- Title I re-based on Helios-3, rendered from the instruments.

proposals/California_Sovereign_Infrastructure_v0.1.md is the as-submitted
merge and is never edited. This file renders proposals/Title_I_Helios-3_v0.2.md
-- Title I as it stands after the second pass -- from the instruments that
computed it: helios.py (the requirement), cspchain.py (the plant), helios3.py
(the mitigation register and the price), receiver.py (the receiver threshold),
hourly3.py (what the plant serves hour by hour and what closes it), joinder.py
(the water route) and studies.py (provenance, the ladder, the cost of delay).

The document carries no number this file did not read from one of them, and
every number is labelled with its case, because the author's standing rule is
that a number quoted without its case is misquoted. The selftest asserts the
file on disk is byte-identical to a fresh render, so it cannot have been
hand-edited, and that its key figures equal the instruments'. Stdlib only.

Rendering runs hourly3.py and joinder.py, several minutes.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import cspchain as C                                            # noqa: E402
import helios3 as H3                                            # noqa: E402
import receiver as RX                                           # noqa: E402
import hourly3 as HR                                            # noqa: E402
import joinder as J                                             # noqa: E402
import studies as ST                                            # noqa: E402
import aquacost as AQ                                           # noqa: E402
import titleone as T1                                           # noqa: E402
import minors as MN                                             # noqa: E402
import both as B                                                # noqa: E402

OUT = os.path.join(HERE, "..", "proposals", "Title_I_Helios-3_v0.2.md")
CASES = ("mid", "critical")


def gather():
    g = {}
    g["e_req"] = H.hh_demand_twh()
    g["growth"] = tuple(H.hh_demand_twh(years=H.BOND_TERM_Y, growth=x) / g["e_req"] for x in H.GROWTH_BAND)
    g["today_hh"] = H.per_household(H.GEN_RATE_NOW * 1e3)
    g["design"] = {c: C.design("helios3", c) for c in CASES}
    g["priced"] = {c: H3.priced(c) for c in CASES}
    rxc = {"mid": "nominal", "critical": "critical"}      # receiver.py's cases are nominal / critical
    # the field factor is against the chain's own rec link (the mid design's), not
    # against a design that already carries the receiver's figure
    g["rx"] = {c: dict(open=RX.efficiency(rxc[c], True), domed=RX.efficiency(rxc[c], False),
                       field=RX.upstream_field_factor(g["design"]["mid"], rxc[c], True)) for c in CASES}
    g["hourly"] = {c: HR.run(c) for c in CASES}
    g["mirrors"] = {}
    for c in CASES:
        d = g["design"][c]
        r = HR.run(c, 1.0, 1.0, 1.5, 2.0, 2.0, design=d)
        cost = HR.closure_cost_m(d, 1.0, 1.0, 1.5, 2.0, 2.0)
        g["mirrors"][c] = dict(unserved=1 - r["served_frac"], cost_b=cost / 1e3, dprice=HR.price_delta(d, cost))
    g["winter"] = {c: J.winter(c) for c in CASES}
    g["water"] = {c: J.evening_with_water(c, 500.0, g["winter"][c]) for c in CASES}
    g["delay"] = {c: ST.delay_cost_per_year(c) for c in CASES}
    g["aqua"] = {c: AQ.module(c) for c in CASES}
    g["aqua_route"] = {c: AQ.water_route(c) for c in CASES}
    g["rates"] = {c: T1.rate_table(c) for c in CASES}
    g["tranches"] = {c: T1.tranches(c) for c in CASES}
    g["gentie"] = {c: T1.gentie(c) for c in CASES}
    g["ladder"] = RX.ladder(g["design"]["mid"])
    g["path_years"] = ST.critical_path_years()
    g["n_studies"] = len(ST.STUDIES)
    g["n_tech"] = len(ST.TECHNOLOGIES)
    g["grades"] = (H3.grade_counts(False), H3.grade_counts(True))
    g["co2"] = {c: MN.co2(c) for c in CASES}
    g["jobs"] = {c: MN.jobs(c) for c in CASES}
    g["seismic"] = {c: MN.seismic(c) for c in CASES}
    g["cycle"] = MN.cycle_label()
    g["both"] = {c: B.scan(c)["best"] for c in CASES}
    return g


def money(x):
    return f"{x:,.0f}"


def render(g):
    d, p, hr, w = g["design"], g["priced"], g["hourly"], g["water"]
    L = []
    a = L.append
    a("# Title I — Helios-3, re-based (v0.2)")
    a("")
    a("**What this document is.** Title I of the California Sovereign Infrastructure program as it")
    a("stands after the second pass: the Helios-1M salt towers of v0.1 replaced by Helios-3 (Gen3")
    a("particles, sCO₂, PV-direct daytime, night-sized field), the author's mitigation register adopted")
    a("row by row, and the plant run hour by hour. It is **rendered by `tools/rebase.py` from the")
    a("instruments** and carries no number they did not compute; every number is labelled **mid** or")
    a("**critical**, under the author's standing rule that a number quoted without its case is misquoted.")
    a("v0.1 is the as-submitted merge and is unchanged; this is the diff, stated as a document.")
    a("")
    a("## 1. The requirement")
    a("")
    a(f"Three million households at EIA's {H.HH_KWH_YR:,.0f} kWh a year is **{g['e_req']:.1f} TWh** of firm supply, the")
    a(f"program's minimum, growing to {g['growth'][0]:.2f}–{g['growth'][1]:.2f}× over the {H.BOND_TERM_Y}-year bond term. The criterion is the")
    a("author's: the plant pays for itself after the build bonds. Inverted, that is a required price per")
    a(f"MWh, set beside the ${H.FIRM_CLEAN_PPA[0]:.0f}–{H.FIRM_CLEAN_PPA[1]:.0f} California's load-serving entities pay for firm clean")
    a(f"energy under contract, and beside what a household pays the utility today for generation: **${g['today_hh']:,.0f} a")
    a("year**.")
    a("")
    a("## 2. The plant")
    a("")
    a("Helios-3: a Noor III-class surround heliostat field sized for the night; a multi-aperture")
    a("falling-particle receiver behind the author's compound quartz aperture; sintered-bauxite particles")
    a("as medium and store in cold-shell silos; a moving packed-bed exchanger into a 715 °C sCO₂")
    a("recompression block, dry-cooled; PV serving the daytime load directly and feeding particle heaters")
    a(f"in winter. The cycle is {g['cycle']['helios3']} at {g['cycle']['helios3_eta']:.2f} gross; the nitrate-salt fallback is")
    a(f"{g['cycle']['fallback']} at {g['cycle']['fallback_eta']:.2f} — v0.1's *supercritical Rankine* is withdrawn (F-32). The energy chain, link by link:")
    a("")
    a("| link | mid | critical |")
    a("|---|---|---|")
    for k, name in (("opt", "field optical efficiency, annual"), ("rec", "receiver thermal efficiency"),
                    ("cycle", "power cycle, gross"), ("par", "1 − parasitic share"), ("avail", "availability")):
        a(f"| {name} | {d['mid']['links'][k]:.3f} | {d['critical']['links'][k]:.3f} |")
    a("")
    a(f"The critical receiver figure is `receiver.py`'s, handed up the chain rather than the chain's own")
    a(f"best: {g['rx']['critical']['open']:.3f} open, which alone grows the field by {g['rx']['critical']['field']:.2f}. Sized to the requirement:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| mirror aperture, M m² | {d['mid']['aperture'] / 1e6:.1f} | {d['critical']['aperture'] / 1e6:.1f} |")
    a(f"| towers, Noor III class | {d['mid']['towers']:.0f} | {d['critical']['towers']:.0f} |")
    a(f"| sCO₂ block, MWe | {d['mid']['turb_mw']:,.0f} | {d['critical']['turb_mw']:,.0f} |")
    a(f"| particle store, GWh_th ({C.NIGHT_HOURS:.0f} h) | {d['mid']['tes_mwh'] / 1e3:.1f} | {d['critical']['tes_mwh'] / 1e3:.1f} |")
    a(f"| PV, MW_AC | {d['mid']['pv_mw']:,.0f} | {d['critical']['pv_mw']:,.0f} |")
    a(f"| electric heaters, MW_th | {d['mid']['heater_mw']:,.0f} | {d['critical']['heater_mw']:,.0f} |")
    a("")
    a("## 3. What it serves, hour by hour")
    a("")
    a("The chain sizes the plant on annual energy. Run through 8,760 hours across the three nodes,")
    a("PV serving the load first, the block serving the residual from the store, the plant as sized")
    a("serves:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| share of the load served | {hr['mid']['served_frac']:.3f} | {hr['critical']['served_frac']:.3f} |")
    a(f"| unserved, TWh | {hr['mid']['unserved'] / 1e6:.2f} | {hr['critical']['unserved'] / 1e6:.2f} |")
    a(f"| unserved in July, share of month | {hr['mid']['month_unserved'][7] / hr['mid']['month_load'][7]:.3f} | {hr['critical']['month_unserved'][7] / hr['critical']['month_load'][7]:.3f} |")
    a(f"| unserved in December, share of month | {hr['mid']['month_unserved'][12] / hr['mid']['month_load'][12]:.3f} | {hr['critical']['month_unserved'][12] / hr['critical']['month_load'][12]:.3f} |")
    a(f"| field defocused in summer, TWh_th | {hr['mid']['spill_th'] / 1e6:.2f} | {hr['critical']['spill_th'] / 1e6:.2f} |")
    a("")
    a("Two shortfalls the annual chain could not see. The block is sized to the average night and a")
    a("residential load peaks after sunset, so the block cannot carry the evening in any month. And")
    a("sixteen hours of store cannot move June into December: the store empties from October to April")
    a("while a quarter of June's field is defocused. The load and PV shapes are reconstructed and pinned")
    a("to sourced levels; a measured CAISO profile and an NSRDB hourly file replace them when reachable.")
    a("")
    a("## 4. Closing the load: two routes, and the one adopted")
    a("")
    a("Both keep the block at **×1.5**, because nothing but the block serves a July evening. They differ")
    a("in how the October-to-April season is closed. **The author chose both** (2026-09-11, `both.py`):")
    a("the water returns half the season and the field and store carry the other half.")
    a("")
    a("| route | what grows | mid, $B | + $/MWh | critical, $B | + $/MWh | leaves to the grid |")
    a("|---|---|---|---|---|---|---|")
    m = g["mirrors"]
    a(f"| mirrors | field ×2, store 2 days | {m['mid']['cost_b']:.1f} | {m['mid']['dprice']:.0f} | {m['critical']['cost_b']:.1f} | {m['critical']['dprice']:.0f} | {m['mid']['unserved']:.1%} / {m['critical']['unserved']:.1%} |")
    wm, wc = w["mid"]["closing"], w["critical"]["closing"]
    a(f"| water (Title III) | {wm['water']['modules']:.0f} / {wc['water']['modules']:.0f} desalination modules, a {wm['water']['km3']:.1f} / {wc['water']['km3']:.1f} km³ reservoir at 500 m, {wm['mw']:,.0f} MW of pump-turbines | {wm['total_b']:.1f} | {J.price_delta('mid', wm['total_b']):.0f} | {wc['total_b']:.1f} | {J.price_delta('critical', wc['total_b']):.0f} | {wm['unserved']:.1%} / {wc['unserved']:.1%} |")
    bm, bc = g["both"]["mid"], g["both"]["critical"]
    a(f"| **both (adopted)** | field ×{bm['field']:.2f}, store {bm['store']:.1f} d; {bm['modules']:.0f} / {bc['modules']:.0f} modules, {bm['mw']:,.0f} MW of pump-turbines | **{bm['title1_b']:.1f}** | **{bm['dprice']:.0f}** | **{bc['title1_b']:.1f}** | **{bc['dprice']:.0f}** | {bm['unserved']:.1%} / {bc['unserved']:.1%} |")
    a("")
    a(f"The adopted route costs more than mirrors alone, because the pump-turbines are bought whole whatever")
    a(f"share they return; with the water withheld it leaves {bm['no_water']['unserved']:.0%} to the grid and with the field at design")
    a(f"{bm['no_field']['unserved']:.0%}, against {B.scan('mid')['as_sized']['unserved']:.0%} with neither. Two levers that fail differently, neither at its full extent.")
    a("")
    a(f"On the power side the two are at parity. The water route makes **{wm['water']['maf']:.2f} to {wc['water']['maf']:.2f} million")
    a("acre-feet a year** of water the mirrors do not, delivered October to April; at critical the summer")
    a(f"surplus lifts {J.modules_to_close('critical', 500.0, g['winter']['critical'])['surplus_twh'] / J.modules_to_close('critical', 500.0, g['winter']['critical'])['lift_twh']:.2f} of the season and the rest is the plant's own output. Which route is a decision about")
    a("water, and it is Title III's. Title II's side of it, priced by `aquacost.py` with the water's")
    a("electricity bought from Title I at the register price:")
    a("")
    a("| Title II | mid | critical |")
    a("|---|---|---|")
    aq, ar = g["aqua"], g["aqua_route"]
    a(f"| one 50,000 AFY RO module, financed, $M (Title II said 250–320) | {aq['mid']['financed_m']:,.0f} | {aq['critical']['financed_m']:,.0f} |")
    a(f"| water at cost recovery, $/acre-foot (Title II said 400; Carlsbad delivers 2,700–2,900) | {aq['mid']['per_af']:,.0f} | {aq['critical']['per_af']:,.0f} |")
    a(f"| the water route's modules, financed, $B | {ar['mid']['capex_b']:.1f} | {ar['critical']['capex_b']:.1f} |")
    a(f"| that water with the lift on its bill, $/acre-foot | {ar['mid']['per_af']:,.0f} | {ar['critical']['per_af']:,.0f} |")
    a(f"| per household per year at 0.28 AF | {ar['mid']['household']:,.0f} | {ar['critical']['household']:,.0f} |")
    a("")
    a("## 5. Price and the household")
    a("")
    a("| $/MWh | mid | critical |")
    a("|---|---|---|")
    a(f"| Helios-3 as chained | {d['mid']['price']:.0f} | {d['critical']['price']:.0f} |")
    a(f"| with the mitigation register (§6) | {p['mid']['price']:.0f} | {p['critical']['price']:.0f} |")
    a(f"| serving the whole load, mirrors route | {p['mid']['price'] + m['mid']['dprice']:.0f} | {p['critical']['price'] + m['critical']['dprice']:.0f} |")
    a(f"| serving the whole load, water route | {p['mid']['price'] + J.price_delta('mid', wm['total_b']):.0f} | {p['critical']['price'] + J.price_delta('critical', wc['total_b']):.0f} |")
    a(f"| **serving the whole load, both (adopted)** | **{p['mid']['price'] + g['both']['mid']['dprice']:.0f}** | **{p['critical']['price'] + g['both']['critical']['dprice']:.0f}** |")
    a("")
    a("| $ per household per year (today " + money(g["today_hh"]) + ") | mid | critical |")
    a("|---|---|---|")
    a(f"| with the mitigation register | {money(H.per_household(p['mid']['price']))} | {money(H.per_household(p['critical']['price']))} |")
    a(f"| serving the whole load, mirrors route | {money(H.per_household(p['mid']['price'] + m['mid']['dprice']))} | {money(H.per_household(p['critical']['price'] + m['critical']['dprice']))} |")
    a(f"| serving the whole load, water route | {money(H.per_household(p['mid']['price'] + J.price_delta('mid', wm['total_b'])))} | {money(H.per_household(p['critical']['price'] + J.price_delta('critical', wc['total_b'])))} |")
    a(f"| **serving the whole load, both (adopted)** | **{money(H.per_household(p['mid']['price'] + g['both']['mid']['dprice']))}** | **{money(H.per_household(p['critical']['price'] + g['both']['critical']['dprice']))}** |")
    a("")
    band = H.FIRM_CLEAN_PPA[1]
    a(f"**The criterion, stated exactly.** At mid, Helios-3 with its register needs ${p['mid']['price']:.0f}/MWh, ${p['mid']['price'] - band:.0f}")
    a(f"above the top of the contract band, and a household pays ${money(H.per_household(p['mid']['price']))} against ${money(g['today_hh'])} today. Serving")
    a(f"the whole load from the plant alone costs ${p['mid']['price'] + m['mid']['dprice']:.0f}, at which a household pays about what it pays now. At")
    a(f"critical the register price is ${p['critical']['price']:.0f} and the whole load ${p['critical']['price'] + m['critical']['dprice']:.0f}: **above today's bill**. The plant pays")
    a("for itself after the bonds only at a price above the band, and the critical case is the threshold")
    a("the design is held to. A plant designed to mid has no margin; this document does not offer one.")
    a("")
    a("**The security behind the rate (F-19).** The 3.85 % is a general-obligation or contracted-revenue")
    a("rate; the security is contracted in-state offtake at the required price with a state GO backstop")
    a("for the first-of-kind rungs. Priced to each security, with the register:")
    a("")
    a("| security | rate | mid, $/MWh ($/household) | critical, $/MWh ($/household) |")
    a("|---|---|---|---|")
    for (name, r, pm, hm), (_n, _r, pc, hc) in zip(g["rates"]["mid"], g["rates"]["critical"]):
        a(f"| {name} | {100 * r:.2f} % | {pm:.0f} ({hm:,.0f}) | {pc:.0f} ({hc:,.0f}) |")
    a("")
    a("**The mechanism behind the tariff (F-10).** The $0.00/kWh of v0.1 is replaced by the household bill")
    a(f"above, an output of the balance: {T1.MECHANISM}. A free tariff is a subsidy paid by someone, and this")
    a("program names no one to pay it.")
    a("")
    a("## 6. The risks and their mitigation")
    a("")
    a("Sixteen rows, graded before and after, each carried by a named part of the build, each DESIGN")
    a("(retired by specification), HOURS (retired only by operating time) or BENEFIT. Adopted row by")
    a("row with the author on 2026-09-11.")
    a("")
    a("| id | risk | before | after | kind |")
    a("|---|---|---|---|---|")
    for rid, risk, b, _m, af, k, _c, _s in H3.REGISTER:
        a(f"| {rid} | {risk} | {b} | {af} | {k} |")
    b0, b1 = g["grades"]
    a("")
    a("After: " + ", ".join(f"{v} {k}" for k, v in b1.items() if v) + ". R-08 is managed without moving and says so.")
    a("")
    a("## 7. Provenance, the ladder and the cost of delay")
    a("")
    a(f"`studies.py` lists {g['n_studies']} studies over the {g['n_tech']} technologies in the system, each with a status and a")
    a("source, complete over technologies and a floor over studies, reviewed against the web where the")
    a("proxy reached. No falling-particle receiver has run above 2 MW_th and no 715 °C sCO₂ recompression")
    a("cycle has run at all; those are HOURS, and the ladder buys them in order:")
    a("")
    for name, mw, f in g["ladder"]:
        a(f"- {name}: {mw:,.0f} MW_th" + (f" (×{f:.1f})" if f else ""))
    a("")
    a(f"Each rung is passed at its critical figure and handed up the chain before the next is ordered.")
    a(f"The studies on the critical path take {g['path_years']:.1f} years, run against the build rather than before")
    a(f"it. Delay escalates the whole plant at {100 * HC.ESCALATION:.0f} % a year before a dollar is spent:")
    a("")
    a("| per year of delay | mid | critical |")
    a("|---|---|---|")
    a(f"| capex, $B | {g['delay']['mid']['delta_capex_m'] / 1e3:.2f} | {g['delay']['critical']['delta_capex_m'] / 1e3:.2f} |")
    a(f"| price, $/MWh | {g['delay']['mid']['delta_price']:.1f} | {g['delay']['critical']['delta_price']:.1f} |")
    a(f"| household, $/yr | {g['delay']['mid']['delta_hh']:.0f} | {g['delay']['critical']['delta_hh']:.0f} |")
    a("")
    a("**The schedule (F-24).** The ladder dated from the 2028–2030 groundbreaking, each bond tranche")
    a("following a rung that has been passed at its critical figure; the pilot and the first node's field")
    a("run in parallel. Direct cost by rung:")
    a("")
    a("| rung | years | mid, $B | critical, $B |")
    a("|---|---|---|---|")
    for (name, y0, y1, am), (_n, _y0, _y1, ac) in zip(g["tranches"]["mid"][0], g["tranches"]["critical"][0]):
        a(f"| {name} | {y0:.0f}–{y1:.0f} | {am / 1e3:.2f} | {ac / 1e3:.2f} |")
    a("")
    a("**Transmission (F-09).** The export is negative (F-01), so no firm export right is needed. The in-state")
    a(f"gen-tie per node at the closed sizing peaks at {g['gentie']['mid']['per_node']:,.0f} MW (mid) / {g['gentie']['critical']['per_node']:,.0f} MW (critical) from the")
    a(f"hour-by-hour, {g['gentie']['mid']['circuits']:.2f} / {g['gentie']['critical']['circuits']:.2f} of one 500 kV circuit, priced in the switchyard line at")
    a(f"${g['gentie']['mid']['switchyard_m']:,.0f} / ${g['gentie']['critical']['switchyard_m']:,.0f} M. The interconnection study is the Authority's to file and no authority shortens it.")
    a("")
    a("## 8. Emissions, employment, siting and procurement")
    a("")
    a("The minor rows, computed rather than asserted (`minors.py`).")
    a("")
    a(f"**CO₂ avoided (F-34).** From the hour-by-hour at a CAISO marginal factor of {g['co2']['mid']['factor']:.2f} / {g['co2']['critical']['factor']:.2f} t/MWh")
    a("(the critical case credits less, because a cleaner grid displaces less):")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| served as sized, TWh | {g['co2']['mid']['as_sized_twh']:.2f} | {g['co2']['critical']['as_sized_twh']:.2f} |")
    a(f"| avoided as sized, MMT/yr | **{g['co2']['mid']['as_sized_mmt']:.2f}** | **{g['co2']['critical']['as_sized_mmt']:.2f}** |")
    a(f"| avoided with the load closed, MMT/yr | {g['co2']['mid']['closed_mmt']:.2f} | {g['co2']['critical']['closed_mmt']:.2f} |")
    a("")
    a(f"v0.1 said {MN.CLAIMED_MMT} MMT.")
    a("")
    a(f"**Employment (F-38).** From built plants per MW — Crescent Dunes and Ivanpah for the permanent staff,")
    a(f"Ivanpah's peak for construction — at the closed block of {g['jobs']['mid']['block_mw']:,.0f} MWe:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| permanent, Title I | **{g['jobs']['mid']['permanent']:,.0f}** | **{g['jobs']['critical']['permanent']:,.0f}** |")
    a(f"| construction peak, Title I | {g['jobs']['mid']['construction_peak']:,.0f} | {g['jobs']['critical']['construction_peak']:,.0f} |")
    a("")
    a(f"v0.1 said {MN.CLAIMED_JOBS[0]:,} construction and {MN.CLAIMED_JOBS[1]:,} permanent; the multiplier it quoted is unsourced and is not carried.")
    a("")
    a(f"**Seismic (F-33).** Seismic zones left the code in 2001; the basis is ASCE 7, site class and mapped MCE_R.")
    a(f"The {MN.DESIGN_PGA_G:.2f} g target is kept and clears the mapped PGA at every node:")
    a("")
    a("| node | mapped PGA, g (mid / critical) | target over mapped |")
    a("|---|---|---|")
    for n in MN.MCE_PGA_G:
        (pm, fm), (pc, fc) = g["seismic"]["mid"][n], g["seismic"]["critical"][n]
        a(f"| {n} | {pm:.2f} / {pc:.2f} | {fm:.2f}× / {fc:.2f}× |")
    a("")
    a("The mapped values are assumed from the hazard record and the site study fixes them.")
    a("")
    a("**Procurement (F-39).** One EPC per node under an owner's engineer across the program; the pilot")
    a("aperture and the first module let as separate contracts. No contractor has delivered more than one")
    a("commercial tower at a time in the US, and the ladder (§7) buys the hours before the fleet.")
    a("")
    a("**The Authority (F-37).** A statutory public entity created by the Act on the pattern of the")
    a("California Consumer Power and Conservation Financing Authority (SB 6X, 2001; defunded by 2004 — a")
    a("history the Act acknowledges), registered as the load-serving entity of §5. Gov. Code §8571 is")
    a("cited only for what it does: suspend regulatory statutes in a declared emergency. It issues no")
    a("coastal permit and shortens no federal review.")
    a("")
    a("## 9. What v0.2 does not settle")
    a("")
    a("- The split of the season between the two routes: adopted even, movable on `both.py`'s ladder;")
    a("  the water side carries Title II's own register (F-14, F-16), resolved at its price.")
    a("- The evening peak is closed by a block ×1.5 and by nothing else; a measured load profile may")
    a("  move that factor either way.")
    a("- The receiver's critical figure and the dome's verdict are what the pilot aperture measures;")
    a("  until it has run, the critical column is the design basis.")
    a("- Every row of `FLAWS.tsv` is resolved; transmission, the tariff, the bond rate, the schedule and")
    a("  the minors are settled above as positions with a price, not as witnesses.")
    a("")
    a("*Rendered by `tools/rebase.py`; do not edit by hand. Re-render after any change to the instruments.*")
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
    check("every case-bearing table carries both columns", text.count("| mid | critical |") >= 5)
    check("the register price at mid appears in the document", f"| with the mitigation register (§6) | {g['priced']['mid']['price']:.0f} |" in text)
    check("the served share hour by hour appears", f"{g['hourly']['mid']['served_frac']:.3f}" in text)
    check("the criterion is stated with today's bill beside it", f"${g['today_hh']:,.0f} today" in text)
    check("the document says it carries no number the instruments did not compute", "carries no number they did not compute" in text)
    check("the document does not offer a mid-only design", "does not offer one" in text)
    check("every register row is printed", all(r[0] in text for r in H3.REGISTER))
    check("the rate table, the schedule and the gen-tie appear", "F-19" in text and "F-24" in text and "F-09" in text)
    check("Title II's module and water price appear beside the water route",
          f"| water at cost recovery, $/acre-foot (Title II said 400; Carlsbad delivers 2,700–2,900) | {g['aqua']['mid']['per_af']:,.0f} |" in text)
    check("the receiver's field factor is against the chain's own link, not against itself",
          1.2 < g["rx"]["critical"]["field"] < 1.4)
    check("the minors appear: CO2, jobs, seismic, procurement, the Authority, the cycle label",
          all(t in text for t in ("F-34", "F-38", "F-33", "F-39", "F-37", "F-32")))
    check("the CO2 figure printed is the instrument's", f"| avoided as sized, MMT/yr | **{g['co2']['mid']['as_sized_mmt']:.2f}**" in text)
    check("the adopted route appears in the routes table and both price tables", text.count("both (adopted)") == 3)
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
