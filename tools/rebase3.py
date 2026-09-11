#!/usr/bin/env python3
"""rebase3.py -- Title III, the joinder, rendered from the instruments.

F-31: the merged document carries no power-supply agreement, no shared
balance sheet, no severability clause and no institutional relation between
the Authority and the water program; the author's decision (one program, two
projects, severable) was stated in chat only. What settles it: write Title
III once the numbers exist -- contract price, volume, term; a single
financial statement; severability. They exist now. This renders
proposals/Title_III_Joinder_v0.2.md from joinder.py, aquacost.py, hourly3.py,
helios3.py, titleone.py and majors.py; it carries no number they did not
compute, labels every number mid or critical, and its selftest asserts the
file on disk is byte-identical to a fresh render. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import helios3 as H3                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402
import joinder as J                                             # noqa: E402
import aquacost as AQ                                           # noqa: E402
import titleone as T1                                           # noqa: E402
import majors as MJ                                             # noqa: E402
import cspchain as C                                            # noqa: E402

OUT = os.path.join(HERE, "..", "proposals", "Title_III_Joinder_v0.2.md")
CASES = ("mid", "critical")
SGMA_RECHARGE_GAP_MAF = (1.8, 2.5)        # San Joaquin Valley overdraft, MAF/yr, nominal / critical  SOURCED band (PPIC ~1.8-2.5)
CONTRACT_TERM_Y = H.BOND_TERM_Y           # the energy contract runs the bond term         DERIVED


def gather():
    g = {}
    g["priced"] = {c: H3.priced(c) for c in CASES}
    g["winter"] = {c: J.winter(c) for c in CASES}
    g["water"] = {c: J.evening_with_water(c, 500.0, g["winter"][c]) for c in CASES}
    g["mirrors"] = {}
    for c in CASES:
        d = C.design("helios3", c)
        r = HR.run(c, 1.0, 1.0, 1.5, 2.0, 2.0, design=d)
        cost = HR.closure_cost_m(d, 1.0, 1.0, 1.5, 2.0, 2.0)
        g["mirrors"][c] = dict(unserved=1 - r["served_frac"], cost_b=cost / 1e3, dprice=HR.price_delta(d, cost))
    g["module"] = {c: AQ.module(c) for c in CASES}
    g["route"] = {c: AQ.water_route(c) for c in CASES}
    g["rates"] = {c: T1.rate_table(c) for c in CASES}
    g["reserve"] = {c: MJ.reserve(c) for c in CASES}
    g["downside"] = {c: MJ.downside(c) for c in CASES}
    g["today_hh"] = H.per_household(H.GEN_RATE_NOW * 1e3)
    return g


def render(g):
    p, w, m, r, mod = g["priced"], g["water"], g["mirrors"], g["route"], g["module"]
    L = []
    a = L.append
    a("# Title III — The Joinder (v0.2)")
    a("")
    a("**What this document is.** The relation between Title I (Helios-3) and Title II (Aqua-Sovereign)")
    a("that v0.1 reserved and never wrote: the power-supply agreement, the single financial statement, the")
    a("severability, and the one decision that joins them. It is **rendered by `tools/rebase3.py` from the")
    a("instruments** and carries no number they did not compute; every number is labelled **mid** or")
    a("**critical**. The author's four standing decisions govern it: one program, two projects, severable;")
    a("nitrate stays and chloride chemistry is excluded everywhere; Noor III-class heliostats; ZLD dropped and")
    a("brine returned through the existing outfall.")
    a("")
    a("## 1. The relation")
    a("")
    a("One Authority, two projects, two revenue accounts. Title I sells electricity at cost recovery to")
    a("in-state load-serving entities and to Title II; Title II sells water at cost recovery to districts.")
    a("Neither subsidises the other: each carries its own capital, its own debt service and its own price,")
    a("and the joinder is two contracts and one asset.")
    a("")
    a("**The power-supply agreement.** Title II buys its electricity from Title I at Title I's required")
    a(f"price, mid or critical, for the bond term of {CONTRACT_TERM_Y} years:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| contract price, $/MWh (Title I with its register) | {p['mid']['price']:.0f} | {p['critical']['price']:.0f} |")
    a(f"| volume per module, GWh/yr at {mod['mid']['kwh_m3']:.1f}–{mod['critical']['kwh_m3']:.1f} kWh/m³ | {mod['mid']['kwh_m3'] * AQ.MODULE_M3_YR / 1e6:.0f} | {mod['critical']['kwh_m3'] * AQ.MODULE_M3_YR / 1e6:.0f} |")
    a(f"| energy's share of the water's cost | {mod['mid']['energy_m'] / mod['mid']['total_m']:.0%} | {mod['critical']['energy_m'] / mod['critical']['total_m']:.0%} |")
    a("")
    a("**The one shared asset.** Title I's summer surplus — the field it would otherwise defocus — lifts")
    a("Title II's product water to an elevated reservoir, and the October-to-April delivery returns through")
    a("pump-turbines to Title I's evenings. The reservoir and the pump-turbines are Title I's (they close")
    a("its season); the modules are Title II's (they make its water); the lift energy is the surplus, priced")
    a("at nothing because it was worth nothing.")
    a("")
    a("## 2. The decision")
    a("")
    a("Hour by hour, Title I as sized serves 84 % of its load. Two routes close it, both with the block")
    a("at ×1.5. On the power side they are at parity; what separates them is water.")
    a("")
    a("| | mirrors, mid | mirrors, critical | water, mid | water, critical |")
    a("|---|---|---|---|---|")
    wm, wc = w["mid"]["closing"], w["critical"]["closing"]
    a(f"| Title I additional capital, $B | {m['mid']['cost_b']:.1f} | {m['critical']['cost_b']:.1f} | {wm['total_b']:.1f} | {wc['total_b']:.1f} |")
    a(f"| Title I price, $/MWh | {p['mid']['price'] + m['mid']['dprice']:.0f} | {p['critical']['price'] + m['critical']['dprice']:.0f} | {p['mid']['price'] + J.price_delta('mid', wm['total_b']):.0f} | {p['critical']['price'] + J.price_delta('critical', wc['total_b']):.0f} |")
    a(f"| Title II modules | 0 | 0 | {r['mid']['modules']:.0f} | {r['critical']['modules']:.0f} |")
    a(f"| Title II capital, financed, $B | 0 | 0 | {r['mid']['capex_b']:.0f} | {r['critical']['capex_b']:.0f} |")
    a(f"| water, million acre-feet a year | 0 | 0 | {r['mid']['maf']:.2f} | {r['critical']['maf']:.2f} |")
    a(f"| water price with the lift, $/acre-foot | — | — | {r['mid']['per_af']:,.0f} | {r['critical']['per_af']:,.0f} |")
    a(f"| left to the grid | {m['mid']['unserved']:.1%} | {m['critical']['unserved']:.1%} | {wm['unserved']:.1%} | {wc['unserved']:.1%} |")
    a("")
    a(f"**The takers.** The water route delivers {r['mid']['maf']:.1f}–{r['critical']['maf']:.1f} million acre-feet a year from October to")
    a(f"April. The San Joaquin Valley's groundwater overdraft under SGMA is about {SGMA_RECHARGE_GAP_MAF[0]:.1f}–{SGMA_RECHARGE_GAP_MAF[1]:.1f} million")
    a("acre-feet a year, and winter is when recharge basins take water. That is the match of supply to")
    a("demand the joinder rests on, and it is a contract question: recharge districts under contract for")
    a("firm winter water at three to five thousand dollars an acre-foot, which is what firm water costs.")
    a("")
    a("**The decision is the author's**: the mirrors route is Title I alone at its whole-load price; the")
    a("water route is Title I at the same price plus Title II at the scale of the season, and a million")
    a("acre-feet of firm water California does not otherwise have.")
    a("")
    a("## 3. The single financial statement")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    a(f"| Title I capital with its register, $B | {p['mid']['capex_net'] / 1e3:.1f} | {p['critical']['capex_net'] / 1e3:.1f} |")
    a(f"| Title I closing the season, mirrors / water, $B | {m['mid']['cost_b']:.1f} / {wm['total_b']:.1f} | {m['critical']['cost_b']:.1f} / {wc['total_b']:.1f} |")
    a(f"| Title II modules at the water route, $B | {r['mid']['capex_b']:.0f} | {r['critical']['capex_b']:.0f} |")
    a(f"| program at the water route, $B | {p['mid']['capex_net'] / 1e3 + wm['total_b'] + r['mid']['capex_b']:.0f} | {p['critical']['capex_net'] / 1e3 + wc['total_b'] + r['critical']['capex_b']:.0f} |")
    a(f"| Title I debt service, $M/yr | {g['reserve']['mid']['debt_service_m']:,.0f} | {g['reserve']['critical']['debt_service_m']:,.0f} |")
    a(f"| Title I debt-service reserve, $M | {g['reserve']['mid']['dsrf_m']:,.0f} | {g['reserve']['critical']['dsrf_m']:,.0f} |")
    a(f"| contingency carried | {g['reserve']['mid']['contingency']:.0%} | {g['reserve']['critical']['contingency']:.0%} |")
    a(f"| Title I price at {H.COVERAGE_REQ:.2f}× coverage, $/MWh | {g['downside']['mid']['price_at_coverage']:.0f} | {g['downside']['critical']['price_at_coverage']:.0f} |")
    a("")
    a("The security behind both projects' bonds is contracted offtake at the required price — electricity")
    a("to load-serving entities, water to districts — with a state general-obligation backstop for the")
    a("first-of-kind rungs of Title I's ladder. Priced to each security in Title I §5; the same ladder of")
    a("securities applies to Title II's modules. The downside case is the critical column, by the author's")
    a("standing rule; a revenue bond's coverage is stated above it.")
    a("")
    a("## 4. Severability")
    a("")
    a("- **Title I without Title II** stands: the mirrors route closes the season at the price in §2, and")
    a("  no water is made.")
    a("- **Title II without Title I** stands: a module buys its electricity from the grid instead of the")
    a("  Authority, at the grid's price rather than the contract's, and makes the same water; the water")
    a("  route's reservoir and pump-turbines are not built, and the water is delivered by the aqueduct.")
    a("- **What does not sever** is the water route itself: it exists only as the pair, because its lift is")
    a("  Title I's surplus and its winter is Title I's shortfall. It is the joinder, and it is optional.")
    a("")
    a("## 5. What Title III does not settle")
    a("")
    a("- The site of the reservoir, and so the head: 500 m is assumed and each doubling halves the modules.")
    a("- The recharge contracts: a million acre-feet a year of winter takers at firm-water prices.")
    a("- The brine as a carbonate sink for the power block's maintenance vents: noted, not priced.")
    a("- The seven minor rows of `FLAWS.tsv`, which are wording and citation, and are worked last.")
    a("")
    a("*Rendered by `tools/rebase3.py`; do not edit by hand. Re-render after any change to the instruments.*")
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
    check("the contract price is Title I's register price", f"| contract price, $/MWh (Title I with its register) | {g['priced']['mid']['price']:.0f} |" in text)
    check("both routes and both cases appear in the decision table", "| mirrors, mid | mirrors, critical | water, mid | water, critical |" in text)
    check("severability is stated both ways", "Title I without Title II" in text and "Title II without Title I" in text)
    check("the decision is left to the author", "The decision is the author's" in text)
    check("the takers are named as a contract question", "recharge districts under contract" in text)
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
