#!/usr/bin/env python3
"""predev.py -- the studies and surveys, priced as their own line and put first.

The author (2026-09-11): every study and survey is built into the upfront cost
as its own line item, first in priority, preceding most of the others. Before
this the register carried them as a ladder of HOURS (studies.py), a pilot
tranche (titleone.py) and a list of site studies (sites.py), and none of the
site, resource, permit or interconnection work was priced at all; the price
began at the field.

This file enumerates them -- resource, load, site, environmental, permit,
interconnection and reservoir studies that GATE construction, and the
technology studies that run on the ladder (studies.py's recommendations) --
prices each at mid and at critical (ASSUMED bands, from the class of study
rather than a quote), and hands the totals to the instruments that carry the
program: helios3.priced() adds the line to Title I's capital before overheads;
titleone.tranches() puts a tranche ZERO before the field rung and delays the
field by the longest gating study; aquacost.module() carries Title II's site
studies per module. The pilot aperture is not repeated here: titleone.py
already prices it as a tranche from cspchain's own lines, and it is listed
below as such so nothing is double-counted. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402

CASES = ("mid", "critical")
NODES = len(H.NODES)
START_YEAR = 2027.0                       # the first study year: the next legislative cycle after the Act   ASSUMED
OWNERS_ENGINEER_SHARE = (0.10, 0.15)      # programme management of the study phase, on the studies          ASSUMED band
MODULES_PER_SITE = (5.0, 3.0)             # Title II modules a coastal site carries; fewer at critical         ASSUMED (sites.py: 15-17 modules on ~3-8 sites)
CANDIDATE_SITES = 8                       # coastal brownfields screened (sites.py)                            sites.py
# (id, name, what it settles, $M mid, $M critical, years mid, years critical, scope, gate)
# scope: "node" (x NODES), "program" (once), "mojave" (one node); gate: True precedes the field rung
TITLE_I = (
    ("dni", "one year of on-site DNI at each node (class-A pyrheliometer station)", "the node's field size; profiles.py's replacement of the reconstructed series", 0.15, 0.30, 1.0, 1.5, "node", True),
    ("load", "measured residential load profile for the served territory (CAISO / CCA metered data)", "the evening block factor; profiles.py's load series", 0.5, 1.0, 0.5, 1.0, "program", True),
    ("title", "title search, land survey and fallowing agreements", "sites.py's land term", 3.0, 6.0, 1.0, 2.0, "node", True),
    ("geotech", "geotechnical investigation and ASCE 7 site-specific seismic hazard (mapped MCE_R)", "minors.py's seismic margin; the tower foundation", 2.0, 4.0, 1.0, 1.5, "node", True),
    ("bio", "biological and cultural resource surveys (protocol-level, two seasons)", "CEQA / NEPA baseline; desert tortoise and cultural sites", 3.0, 8.0, 1.5, 2.0, "node", True),
    ("ceqa", "CEQA environmental impact report per node", "the state permit; majors.py F-25", 15.0, 30.0, 2.0, 3.0, "node", True),
    ("nepa", "NEPA environmental impact statement on the Mojave node (BLM nexus)", "majors.py F-25: 2 / 4 years", 15.0, 30.0, 2.0, 4.0, "mojave", True),
    ("grid", "CAISO interconnection cluster study per node (deposits refundable, excluded)", "titleone.py F-09's gen-tie", 2.0, 4.0, 2.0, 3.0, "node", True),
    ("reservoir", "reservoir siting, head survey and geotechnical study for the water route", "both.py's head: the site question that sizes Title II", 15.0, 40.0, 2.0, 3.0, "program", True),
    ("field-meas", "field commissioning measurement of annual optical efficiency at the first node", "studies.py: the 0.58-0.64 band", 2.0, 4.0, 1.0, 1.0, "program", False),
    ("dome", "compound quartz aperture beside an open aperture on the pilot tower", "studies.py / pilot.py M3", 5.0, 10.0, 1.0, 1.0, "program", False),
    ("ageing", "long-duration particle ageing sampled quarterly on the pilot", "studies.py / pilot.py M4; R-01, R-08", 3.0, 6.0, 3.0, 3.0, "program", False),
    ("silo", "one full-size cold-shell silo cycled daily on the pilot", "studies.py: liner life as O&M", 5.0, 10.0, 3.0, 3.0, "program", False),
    ("hx", "particle-to-sCO2 exchanger module at 800 C / 25 MPa on the pilot", "studies.py: R-03's 4-6x scale-up", 20.0, 40.0, 2.0, 2.0, "program", False),
    ("sco2", "STEP's 715 C recompression phase, then one 10-50 MWe unit on the first module", "studies.py: R-04 turbine, seals, bearings", 40.0, 80.0, 3.0, 3.0, "program", False),
    ("alloy", "coupon and component exposure in the pilot's CO2 loop", "studies.py: carburisation by extrapolation", 3.0, 6.0, 3.0, 3.0, "program", False),
    ("heater", "PV-fed electric particle heater at MW scale on the pilot", "studies.py: heater efficiency on particles", 8.0, 15.0, 0.5, 0.5, "program", False),
    ("cooler", "compressor-inlet performance at 45 C on the first module's dry cooler", "studies.py: the cycle's critical band", 2.0, 4.0, 1.0, 1.0, "program", False),
)
PILOT_NOTE = "the 30 MW_th pilot aperture is priced by titleone.py as its own tranche from cspchain's lines and is not repeated here"
# Title II, per selected coastal site, plus a screening pass over the candidates
TITLE_II = (
    ("screen", "screening of the candidate brownfields against sites.py's seven terms", "which sites go to study", 0.5, 1.0, 0.5, 0.5, "candidate", True),
    ("outfall", "outfall diffuser hydraulic and dilution study (Ocean Plan 17:1)", "titletwo.py's brine term", 2.0, 4.0, 1.0, 1.5, "site", True),
    ("entrain", "intake entrainment study, two years under the Ocean Plan", "titletwo.py's intake decision", 3.0, 6.0, 2.0, 2.0, "site", True),
    ("survey", "site survey, remediation scope and acreage confirmation", "sites.py's acreage term", 2.0, 5.0, 1.0, 1.5, "site", True),
    ("hazard", "seismic and tsunami basis for the site", "sites.py's hazard term", 1.0, 3.0, 1.0, 1.0, "site", True),
    ("coastal", "Coastal Development Permit pre-application and CEQA EIR per site", "sites.py's permit term; titletwo.py's schedule", 10.0, 25.0, 3.0, 5.0, "site", True),
)


def _ci(case):
    return CASES.index(case)


def title1(case):
    ci = _ci(case)
    rows = []
    for rid, name, settles, m_mid, m_crit, y_mid, y_crit, scope, gate in TITLE_I:
        unit = (m_mid, m_crit)[ci]
        n = NODES if scope == "node" else 1
        rows.append(dict(id=rid, name=name, settles=settles, unit_m=unit, n=n, cost_m=unit * n,
                         years=(y_mid, y_crit)[ci], scope=scope, gate=gate))
    gate_m = sum(r["cost_m"] for r in rows if r["gate"])
    ladder_m = sum(r["cost_m"] for r in rows if not r["gate"])
    oe = (gate_m + ladder_m) * OWNERS_ENGINEER_SHARE[ci]
    return dict(rows=rows, gate_m=gate_m, ladder_m=ladder_m, owners_engineer_m=oe,
                total_m=gate_m + ladder_m + oe, gate_years=max(r["years"] for r in rows if r["gate"]),
                field_start=START_YEAR + max(r["years"] for r in rows if r["gate"]))


def title2_per_site(case):
    ci = _ci(case)
    rows = []
    for rid, name, settles, m_mid, m_crit, y_mid, y_crit, scope, gate in TITLE_II:
        unit = (m_mid, m_crit)[ci]
        cost = unit * (CANDIDATE_SITES if scope == "candidate" else 1)
        rows.append(dict(id=rid, name=name, settles=settles, unit_m=unit, cost_m=cost, years=(y_mid, y_crit)[ci], scope=scope))
    per_site = sum(r["cost_m"] for r in rows if r["scope"] == "site")
    screen = sum(r["cost_m"] for r in rows if r["scope"] == "candidate")
    oe = (per_site + screen) * OWNERS_ENGINEER_SHARE[ci]
    return dict(rows=rows, per_site_m=per_site, screening_m=screen, owners_engineer_m=oe,
                per_module_m=(per_site + screen / 3.0 + oe) / MODULES_PER_SITE[ci],
                gate_years=max(r["years"] for r in rows))


def report():
    print()
    print("  THE STUDIES AND SURVEYS, PRICED AS THE FIRST LINE")
    print("  ==================================================")
    print("    The author: every study and survey is its own upfront line item, first in")
    print("    priority. Costs are ASSUMED bands from the class of study; durations too.")
    for c in CASES:
        t = title1(c)
        print(f"\n    TITLE I ({c}) -- start {START_YEAR:.0f}; the gating studies take {t['gate_years']:.1f} years, so the field rung starts {t['field_start']:.0f}")
        print(f"      {'id':<11}{'$M':>8}{'x':>3}{'total':>8}{'yrs':>5}  {'gate':<6}name")
        for r in t["rows"]:
            print(f"      {r['id']:<11}{r['unit_m']:>8.1f}{r['n']:>3}{r['cost_m']:>8.1f}{r['years']:>5.1f}  {'GATE' if r['gate'] else 'ladder':<8}{r['name']}")
        print(f"      {'':<11}{'':>8}{'':>3}{t['gate_m']:>8.1f}       gating studies and surveys")
        print(f"      {'':<11}{'':>8}{'':>3}{t['ladder_m']:>8.1f}       technology studies on the ladder ({PILOT_NOTE})")
        print(f"      {'':<11}{'':>8}{'':>3}{t['owners_engineer_m']:>8.1f}       owner's engineer on the study phase")
        print(f"      {'':<11}{'':>8}{'':>3}{t['total_m']:>8.1f}       TOTAL, carried into helios3.priced() as the first line")
    for c in CASES:
        t = title2_per_site(c)
        print(f"\n    TITLE II ({c}) -- per selected coastal site, {CANDIDATE_SITES} candidates screened; gating {t['gate_years']:.1f} years")
        for r in t["rows"]:
            print(f"      {r['id']:<11}{r['unit_m']:>8.1f}{'':>3}{r['cost_m']:>8.1f}{r['years']:>5.1f}  {r['scope']:<10}{r['name']}")
        print(f"      per site {t['per_site_m']:.1f} + screening {t['screening_m']:.1f} + owner's engineer {t['owners_engineer_m']:.1f} -> ${t['per_module_m']:.1f} M per module at {MODULES_PER_SITE[_ci(c)]:.0f} modules a site")
    print("\n    What it does. The line precedes the field: titleone.py's schedule now opens with")
    print("    tranche zero, the field rung waits on the longest gating study, and the delay that")
    print("    buys is priced by studies.py's escalation. Nothing here is a quote.")


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    for c in CASES:
        t = title1(c)
        check(f"[{c}] every Title I row carries a cost, a duration and a scope", all(r["cost_m"] > 0 and r["years"] > 0 and r["scope"] in ("node", "program", "mojave") for r in t["rows"]))
        check(f"[{c}] the gating studies are the larger share (site and permit work, not the lab)", t["gate_m"] > t["ladder_m"])
        check(f"[{c}] the field rung starts after the longest gating study", t["field_start"] == START_YEAR + t["gate_years"])
        t2 = title2_per_site(c)
        check(f"[{c}] every Title II row carries a cost and a duration", all(r["cost_m"] > 0 and r["years"] > 0 for r in t2["rows"]))
        check(f"[{c}] the coastal permit is the longest Title II gate", max(t2["rows"], key=lambda r: r["years"])["id"] == "coastal")
    check("critical costs more and takes longer than mid on Title I", title1("critical")["total_m"] > title1("mid")["total_m"] and title1("critical")["gate_years"] > title1("mid")["gate_years"])
    check("critical costs more per module than mid on Title II", title2_per_site("critical")["per_module_m"] > title2_per_site("mid")["per_module_m"])
    check("the pilot is not repeated here (no row prices the aperture)", not any(r["id"] == "pilot" for r in title1("mid")["rows"]) and "titleone.py" in PILOT_NOTE)
    check("node-scoped rows are multiplied by the node count", all(r["n"] == NODES for r in title1("mid")["rows"] if r["scope"] == "node"))
    check("the study line is under two percent of a $30 B plant (a line, not a plant)", title1("critical")["total_m"] < 0.02 * 30_000)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(0 if selftest() else 1) if a.selftest else report()
