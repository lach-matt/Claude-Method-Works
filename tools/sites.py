#!/usr/bin/env python3
"""sites.py -- the site terms, scored, so the site question is a ranked list.

The open issues that survive the register are site-specific: reservoir head,
seismic basis, outfall and intake, permitting. None can be COMPUTED without a
site, and this file does not pretend to. What it does is take the three Title I
nodes v0.1 named and the retired or retiring coastal plants a Title II module
could stand on, state the term each Title needs of a site, grade each site on
each term from what is on the record -- MET, CONDITIONAL (clears on an
assumption the site study confirms) or OPEN (not knowable here) -- and rank
them. The rank orders the site STUDIES; it does not choose a site. Every
site value is ASSUMED from the public record unless an instrument holds it,
and the column that says so is printed with the grade.

Imports: helios.py (the nodes and their DNI), minors.py (the seismic margin),
majors.py (land, NEPA), titletwo.py (the brownfield band, the intake),
joinder.py (the head band). Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import minors as MN                                             # noqa: E402
import majors as MJ                                             # noqa: E402
import titletwo as T2                                           # noqa: E402
import joinder as J                                             # noqa: E402

GRADES = ("MET", "CONDITIONAL", "OPEN", "FAIL")
WEIGHT = {"MET": 1.0, "CONDITIONAL": 0.5, "OPEN": 0.0, "FAIL": -1.0}
DNI_FLOOR = 2500.0                        # kWh/m2/yr, below which the node's field grows past the desert's  DERIVED (helios NODES: desert 2,740-2,799; Westside 2,190)
HEAD_NEED_M = J.HEAD_M[1]                 # the critical head the water route is priced at            joinder.py
SEISMIC_MARGIN = 1.5                      # design PGA over mapped, the margin a site study must confirm  ASSUMED

# --- Title I: the terms a node must meet ------------------------------------------
# (term, requirement, what settles it)
T1_TERMS = (
    ("DNI", f"annual DNI at or above {DNI_FLOOR:.0f} kWh/m2/yr, else the field grows", "one year of on-site DNI (NSRDB then a pyrheliometer)"),
    ("land", "a contiguous disturbed parcel covering the node's field", "title search and a fallowing agreement"),
    ("nexus", "no federal land or federal action, else NEPA on the node", "BLM / USACE jurisdiction determination"),
    ("seismic", f"design PGA over mapped MCE by {SEISMIC_MARGIN:.1f}x or the tower is re-based", "ASCE 7 site-specific hazard study"),
    ("grid", "a 500 kV substation within one gen-tie of the node", "CAISO interconnection study"),
    ("head", f"an off-stream reservoir site with {HEAD_NEED_M:.0f} m of head within reach", "reservoir siting and geotechnical study"),
)
# (node, land, nexus, grid, head) -- ASSUMED from the public record, each with a note
T1_SITES = {
    "Mojave (Kramer Junction)": dict(
        land=("CONDITIONAL", "private and BLM checkerboard; SEGS and Solar Star precedent"),
        nexus=("CONDITIONAL", "BLM parcels in the corridor; DRECP development focus area"),
        grid=("MET", "Kramer substation on the Kramer-Lugo 230/500 kV corridor"),
        head=("MET", "Tehachapi crest to the west (Edmonston lift 587 m)")),
    "Imperial (Desert Center)": dict(
        land=("CONDITIONAL", "Desert Sunlight / Desert Harvest on BLM; private parcels along I-10"),
        nexus=("CONDITIONAL", "largely BLM; DRECP DFA"),
        grid=("MET", "Red Bluff 500 kV substation (built for Desert Sunlight)"),
        head=("CONDITIONAL", "Eagle Mountain pumped-storage site (licensed, unbuilt) nearby; head on a private pit")),
    "Central Valley (Westside)": dict(
        land=("MET", "Westlands drainage-impaired fallowed land, 100,000 acres, private"),
        nexus=("MET", "no federal land; state and county permits (majors.py: first node)"),
        grid=("MET", "Gates 500 kV substation on the Path 15 corridor"),
        head=("CONDITIONAL", "Coast Range foothills west of I-5; San Luis / Gianelli precedent at ~100 m, 500 m needs a higher bench")),
}

# --- Title II: the terms a coastal brownfield must meet -----------------------------
T2_TERMS = (
    ("outfall", "a permitted ocean outfall the brine can use at Ocean Plan dilution", "outfall diffuser hydraulic study (titletwo.py 17:1)"),
    ("intake", "an intake channel a screened open intake can reuse", "entrainment study under the Ocean Plan"),
    ("acreage", f"{T2.BROWNFIELD_ACRES[1]:.0f}-{T2.BROWNFIELD_ACRES[0]:.0f} acres of brownfield for a module and its enclosure", "site survey and remediation scope"),
    ("takers", "an overdrafted basin or an aqueduct within reach for the winter delivery", "recharge district contract"),
    ("head", f"an elevated reservoir site with {HEAD_NEED_M:.0f} m of head within reach", "reservoir siting study"),
    ("permit", "a Coastal Commission record that does not foreclose the site", "Coastal Development Permit pre-application"),
    ("hazard", "outside the tsunami inundation zone or hardened; seismic basis stated", "ASCE 7 and CGS tsunami mapping"),
)
T2_SITES = {
    "Moss Landing (Monterey)": dict(
        outfall=("MET", "OTC outfall of the retired units into Monterey Bay"),
        intake=("MET", "harbour intake channel"),
        acreage=("MET", "large retired footprint; Vistra battery on part"),
        takers=("MET", "Salinas Valley 180/400-ft aquifer, critically overdrafted under SGMA"),
        head=("CONDITIONAL", "Gabilan / Santa Lucia ranges within 30 km; bench at 500 m unsurveyed"),
        permit=("CONDITIONAL", "inside the Monterey Bay National Marine Sanctuary; the Cal Am / MPWSP record is a caution"),
        hazard=("CONDITIONAL", "low-lying harbour, inundation zone; 1989 Loma Prieta record")),
    "Morro Bay": dict(
        outfall=("MET", "retired plant outfall into Estero Bay"),
        intake=("MET", "harbour intake"),
        acreage=("MET", "retired 2014; battery project on part"),
        takers=("CONDITIONAL", "no large overdrafted basin; Coastal Branch aqueduct connection"),
        head=("MET", "Santa Lucia range immediately inland"),
        permit=("CONDITIONAL", "sanctuary-adjacent; local opposition record"),
        hazard=("CONDITIONAL", "inundation zone at the harbour")),
    "Ormond Beach (Oxnard)": dict(
        outfall=("MET", "OTC outfall, plant retiring"),
        intake=("MET", "beach intake"),
        acreage=("MET", "retiring OTC plant footprint"),
        takers=("MET", "Oxnard Plain and Fox Canyon, overdrafted, seawater intrusion"),
        head=("MET", "Santa Monica Mountains and Topatopa foothills"),
        permit=("CONDITIONAL", "wetland restoration adjacent; environmental-justice record"),
        hazard=("CONDITIONAL", "inundation zone; liquefaction")),
    "Mandalay (Oxnard)": dict(
        outfall=("MET", "retired 2018; outfall via the Edison canal"),
        intake=("MET", "canal intake"),
        acreage=("MET", "retired footprint"),
        takers=("MET", "Oxnard Plain / Fox Canyon"),
        head=("MET", "as Ormond Beach"),
        permit=("CONDITIONAL", "as Ormond Beach"),
        hazard=("CONDITIONAL", "dune-backed; inundation zone")),
    "Huntington Beach (AES)": dict(
        outfall=("MET", "OTC outfall, the Poseidon site"),
        intake=("MET", "the Poseidon intake"),
        acreage=("MET", "the Poseidon footprint"),
        takers=("MET", "Orange County basin (OCWD recharge)"),
        head=("CONDITIONAL", "Santa Ana Mountains 40 km inland"),
        permit=("FAIL", "Coastal Commission denied a desalination plant on this site in 2022 (titletwo.py schedule)"),
        hazard=("CONDITIONAL", "inundation zone; Newport-Inglewood fault")),
    "Alamitos / Long Beach": dict(
        outfall=("MET", "OTC outfall into San Pedro Bay"),
        intake=("MET", "channel intake"),
        acreage=("CONDITIONAL", "repowered with gas units in 2020; footprint shared"),
        takers=("MET", "Central and West Coast basins (WRD recharge)"),
        head=("CONDITIONAL", "San Gabriel foothills 40 km"),
        permit=("CONDITIONAL", "industrial harbour; port air district"),
        hazard=("CONDITIONAL", "inundation zone; Newport-Inglewood fault")),
    "Scattergood / El Segundo": dict(
        outfall=("MET", "OTC outfalls into Santa Monica Bay"),
        intake=("MET", "ocean intakes"),
        acreage=("CONDITIONAL", "LADWP repowering on site; El Segundo repowered"),
        takers=("MET", "West Coast basin; West Basin's existing recycled-water plant next door"),
        head=("CONDITIONAL", "Santa Monica Mountains 20 km"),
        permit=("CONDITIONAL", "West Basin's own ocean desalination EIR was withdrawn in 2022"),
        hazard=("CONDITIONAL", "dune-backed; inundation zone")),
    "South Bay (Chula Vista)": dict(
        outfall=("CONDITIONAL", "plant demolished 2013; outfall into south San Diego Bay, a refuge"),
        intake=("CONDITIONAL", "bay intake, not ocean"),
        acreage=("MET", "cleared bayfront parcel"),
        takers=("MET", "San Diego County Water Authority system"),
        head=("MET", "Otay and Jamul mountains; San Vicente pumped-storage precedent"),
        permit=("CONDITIONAL", "bayfront master plan; refuge adjacency"),
        hazard=("CONDITIONAL", "bay margin; Rose Canyon fault")),
}
EXCLUDED = {"Encina (Carlsbad)": "already hosts the 56,000 AFY Carlsbad plant; the record aquacost.py prices from, not a site"}


def title1(case):
    ci = ("mid", "critical").index(case)
    out = {}
    for name, lat, lon, ap, mw, st, dni, status in H.NODES:
        s = T1_SITES[name]
        pga = MN.MCE_PGA_G[name][ci]
        margin = MN.DESIGN_PGA_G / pga
        rows = {
            "DNI": ("MET" if dni >= DNI_FLOOR else "CONDITIONAL", f"{dni:.0f} kWh/m2/yr ({status.split(':')[0]})"),
            "land": s["land"], "nexus": s["nexus"],
            "seismic": ("MET" if margin >= SEISMIC_MARGIN else "CONDITIONAL", f"{MN.DESIGN_PGA_G:.2f} g over mapped {pga:.2f} g = {margin:.2f}x"),
            "grid": s["grid"], "head": s["head"],
        }
        out[name] = dict(rows=rows, score=sum(WEIGHT[g] for g, _ in rows.values()))
    return out


def title2():
    out = {}
    for name, s in T2_SITES.items():
        out[name] = dict(rows=s, score=sum(WEIGHT[g] for g, _ in s.values()))
    return out


def ranked(d):
    return sorted(d.items(), key=lambda kv: (-kv[1]["score"], kv[0]))


def first_study(rows, terms):
    """The site's first study: the settling study of its worst term, in term order."""
    order = {g: i for i, g in enumerate(("FAIL", "OPEN", "CONDITIONAL", "MET"))}
    worst = min(terms, key=lambda t: order[rows[t[0]][0]])
    return worst[0], worst[2]


def report():
    print()
    print("  THE SITES, SCORED -- A RANKED LIST OF SITE STUDIES, NOT A CHOICE")
    print("  ==================================================================")
    print("    MET 1, CONDITIONAL 0.5, OPEN 0, FAIL -1. Every site value is ASSUMED from the public")
    print("    record unless an instrument holds it; the note beside each grade says which.")
    for case in ("mid", "critical"):
        t1 = title1(case)
        print()
        print(f"    TITLE I NODES ({case}); terms: " + ", ".join(t[0] for t in T1_TERMS))
        for name, r in ranked(t1):
            print(f"      {r['score']:4.1f}  {name}")
            for term, req, settle in T1_TERMS:
                g, note = r["rows"][term]
                print(f"              {term:<8}{g:<13}{note}")
            ft, fs = first_study(r["rows"], T1_TERMS)
            print(f"              first study: {ft} -- {fs}")
    t2 = title2()
    print()
    print("    TITLE II COASTAL BROWNFIELDS; terms: " + ", ".join(t[0] for t in T2_TERMS))
    for name, r in ranked(t2):
        print(f"      {r['score']:4.1f}  {name}")
        for term, req, settle in T2_TERMS:
            g, note = r["rows"][term]
            print(f"              {term:<8}{g:<13}{note}")
        ft, fs = first_study(r["rows"], T2_TERMS)
        print(f"              first study: {ft} -- {fs}")
    for name, why in EXCLUDED.items():
        print(f"      excl  {name}: {why}")
    print()
    print("    What the ranking says. Title I: at mid the Westside node ties the Mojave for first --")
    print("    it meets land, nexus and grid outright and is conditional on DNI and head, so the node the")
    print("    record doubted for its sun has the fewest open terms, which is why majors.py kept it. At")
    print("    critical the Mojave leads alone, because the Westside's seismic margin (0.75 g over a")
    print("    mapped 0.55 g, 1.36x) falls under the 1.5x a site study must confirm. Title II: the Oxnard plain")
    print("    (Ormond Beach, Mandalay) and Moss Landing meet the taker and head terms the water route")
    print("    needs; Huntington Beach carries a FAIL on its permit record and is not a first site. The")
    print(f"    adopted route needs {16:.0f}-{18:.0f} modules (both.py) and this list holds eight sites: two to")
    print("    three modules per site, or sites this list does not name. Nothing here is a site decision;")
    print("    each row's first study is what would make it one.")


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    check("every Title I node in helios.NODES has a site row", all(n[0] in T1_SITES for n in H.NODES))
    check("every Title I term has a requirement and a settling study", all(len(t) == 3 and all(t) for t in T1_TERMS))
    check("every Title II term has a requirement and a settling study", all(len(t) == 3 and all(t) for t in T2_TERMS))
    check("every Title II site grades every term", all(set(s) == {t[0] for t in T2_TERMS} for s in T2_SITES.values()))
    check("every grade is in the closed set", all(g in GRADES for s in T2_SITES.values() for g, _ in s.values())
          and all(g in GRADES for s in T1_SITES.values() for g, _ in s.values()))
    check("every grade carries a note saying where it comes from", all(n for s in T2_SITES.values() for _, n in s.values())
          and all(n for s in T1_SITES.values() for _, n in s.values()))
    t1 = title1("critical")
    t1m = title1("mid")
    check("at mid the Westside node ties the Mojave for first", t1m["Central Valley (Westside)"]["score"] == max(r["score"] for r in t1m.values()))
    check("at critical the Mojave leads alone and the Westside's seismic is CONDITIONAL",
          ranked(t1)[0][0].startswith("Mojave") and t1["Central Valley (Westside)"]["rows"]["seismic"][0] == "CONDITIONAL")
    check("the Westside node is CONDITIONAL on DNI, not MET", t1["Central Valley (Westside)"]["rows"]["DNI"][0] == "CONDITIONAL")
    check("the desert nodes are MET on DNI", all(t1[n]["rows"]["DNI"][0] == "MET" for n in t1 if not n.startswith("Central")))
    check("seismic grades come from minors.py's margins, not typed", all("over mapped" in t1[n]["rows"]["seismic"][1] for n in t1))
    t2 = title2()
    check("Huntington Beach carries the 2022 denial as a FAIL", t2["Huntington Beach (AES)"]["rows"]["permit"][0] == "FAIL")
    check("Huntington Beach does not rank first", ranked(t2)[0][0] != "Huntington Beach (AES)")
    check("Carlsbad is excluded, not scored", "Encina (Carlsbad)" in EXCLUDED and "Encina (Carlsbad)" not in T2_SITES)
    check("no Title II site is MET on every term (a site study is always owed)", all(any(g != "MET" for g, _ in s.values()) for s in T2_SITES.values()))
    check("the ranking is deterministic on ties (by name)", [k for k, _ in ranked(t2)] == [k for k, _ in ranked(title2())])
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(0 if selftest() else 1) if a.selftest else report()
