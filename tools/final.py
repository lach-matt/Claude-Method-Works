#!/usr/bin/env python3
"""final.py -- the proposal and the pitch in their reader-facing edition.

proposal.py renders the working edition: it names the models that computed each
figure, the flaw register it answers, and the decisions and dates that shaped it.
That is matter about the MAKING of the document and it belongs to the record. This
file renders the edition a reader is handed: numbered sections, an abstract that
states the problem, a table of contents, a bibliography, an author line and no
version, and prose that is analytical and instructive about the SUBJECT alone.

It reads the same gathered numbers as proposal.py (one gather, one set of figures)
and carries no number the working edition does not. Every string that comes from a
data table (the risk register, the study register, the site notes, the study budget)
passes through scrub(), which removes model names, flaw ids, decision dates and
authorial asides. The selftest then scans the whole rendered text for any such
token and fails on one, so the separation is enforced rather than hoped for.

Outputs: proposals/California_Sovereign_Infrastructure.md and
proposals/California_Sovereign_Infrastructure_Pitch.md; --docx and --pdf emit both
as .docx and .pdf; --export-only does that from the files on disk.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import proposal as P                                            # noqa: E402
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

ROOT = P.ROOT
OUT = os.path.join(ROOT, "proposals", "California_Sovereign_Infrastructure.md")
PITCH = os.path.join(ROOT, "proposals", "California_Sovereign_Infrastructure_Pitch.md")
CASES = ("mid", "critical")
TITLE = "California Sovereign Infrastructure"
SUBTITLE = "Firm electricity and firm water for three million households, priced at two cases"
AUTHOR = "Matthew Lach, Independent Researcher, 2026"
money, whole_price, program_b, milestones = P.money, P.whole_price, P.program_b, P.milestones

# =============================================================================
# THE SCRUB -- workshop matter out of every string that comes from a data table
# =============================================================================
_MODEL = {
    "receiver.py": "the receiver model", "hourly3.py": "the hourly model", "helios.py": "the hourly model",
    "cspchain.py": "the chain model", "studies.py": "the study register", "pilot.py": "the acceptance protocol",
    "both.py": "the closing-route analysis", "sites.py": "the site screening", "predev.py": "the study budget",
    "profiles.py": "the measured-profile ingestion", "joinder.py": "the water-route analysis",
    "titleone.py": "the Title I analysis", "titletwo.py": "the Title II analysis", "majors.py": "the impact analysis",
    "minors.py": "the impact analysis", "aquacost.py": "the water pricing", "helios3.py": "the risk register",
    "firmpower.py": "the candidate comparison", "heliocost.py": "the capital build-up",
}
_WORKSHOP = ("proposal.py", "final.py", "rebase.py", "rebase2.py", "rebase3.py")
FORBIDDEN = (".py", "F-0", "F-1", "F-2", "F-3", "F-4", "v0.1", "v0.2", "selftest", "docs/", "tools/", "the author",
             "The author", "author's", "2026-09-", "rendered by", "Rendered", "workshop", "FLAWS", "instrument",
             "this repository", "register price")


def scrub(text):
    t = text
    t = re.sub(r"\s*\((?:[^()]*\.py[^()]*)\)", "", t)                          # parentheticals naming a model
    t = re.sub(r"\((?:the )?author,? 2026-09-11\)", "", t)
    t = re.sub(r"\(author'?s? [^()]*2026-09-11\)", "", t)
    t = t.replace("Adopted by the author 2026-09-11", "Adopted").replace("adopted by the author 2026-09-11", "adopted")
    t = t.replace("adopted as it stands 2026-09-11", "adopted as it stands")
    t = t.replace("FLAGGED FOR SIMULATION 2026-09-11", "Modelled").replace("(reviewed 2026-09-11)", "(reviewed 2026)")
    t = t.replace("SOURCED (reviewed 2026-09-11)", "SOURCED (reviewed 2026)")
    t = re.sub(r",? ?2026-09-11", "", t)
    t = re.sub(r"\s*\(F-\d\d(?:[,/ ]+F-\d\d)*\)", "", t)                        # flaw references, before the names
    t = re.sub(r"\s*F-\d\d(?:/F-\d\d)*(?='s)", "", t)
    t = re.sub(r"\s*F-\d\d(?:/F-\d\d)*:", ":", t)
    t = re.sub(r"\bF-\d\d(?:[,/ ]+F-\d\d)*:?\s*", "", t)
    for k, v in _MODEL.items():
        t = t.replace(k + "'s", v + "'s").replace(k, v)
    for k in _WORKSHOP:
        t = t.replace(k + "'s", "this work's").replace(k, "this work")
    t = t.replace("tools/", "this work: ").replace("(this repository)", "(this work)")
    t = t.replace("Author's", "This work's").replace("the author's", "this work's").replace("author's", "this work's")
    t = t.replace("the author", "this work").replace("The author", "This work")
    t = t.replace("RUN (this work: hourly model)", "Run")
    t = t.replace("register price", "plant price")
    t = t.replace("FLAGGED FOR SIMULATION", "Modelled")
    t = re.sub(r"  +", " ", t).replace(" ,", ",").replace(" .", ".").replace(" ;", ";").replace(" :", ":")
    return t.strip().rstrip(",;").strip()


# =============================================================================
# THE BIBLIOGRAPHY -- every source the study register names, plus the constants'
# =============================================================================
REFERENCES = [
    ("eia", "U.S. Energy Information Administration. Electric Sales, Revenue, and Average Price, 2024 data: California residential consumption per customer and residential customer count."),
    ("atb", "National Renewable Energy Laboratory. Annual Technology Baseline 2024: concentrating solar power, tower with 10 h storage, solar multiple 2.4 (the capital calibration anchor)."),
    ("nsrdb", "National Renewable Energy Laboratory. National Solar Radiation Database and TMY3 station data (Daggett), and the NSRDB direct-normal irradiance classes for the Imperial and Westside nodes."),
    ("caiso", "California Independent System Operator, Department of Market Monitoring. 2024 Annual Report on Market Issues and Performance: average prices, evening-peak prices and negative-price hours."),
    ("sam", "Turchi, C. S., et al. CSP Systems Analysis: Final Project Report, NREL/TP-5500-72716 (2019), and the System Advisor Model cost defaults from which the capital split is reconstructed."),
    ("oceanplan", "California State Water Resources Control Board. Water Quality Control Plan for Ocean Waters of California, 2015 desalination amendment: brine salinity at the mixing-zone edge and intake requirements."),
    ("carlsbad", "San Diego County Water Authority and Poseidon Water. Claude 'Bud' Lewis Carlsbad Desalination Plant: capital, delivered water price and permitting chronology (1998–2015)."),
    ("huntington", "California Coastal Commission. Decision on the Poseidon Huntington Beach desalination project, May 2022, and the project's 2020 capital estimate."),
    ("ppic", "Public Policy Institute of California. Water and the Future of the San Joaquin Valley: groundwater overdraft under the Sustainable Groundwater Management Act."),
    ("asce", "American Society of Civil Engineers. ASCE 7-22, Minimum Design Loads and Associated Criteria for Buildings and Other Structures: mapped risk-targeted maximum considered earthquake ground motion."),
    ("cgs", "California Geological Survey. Seismic hazard and tsunami inundation maps for the coastal and desert sites named."),
    ("sb6x", "California Senate Bill 6X (2001), establishing the California Consumer Power and Conservation Financing Authority; Public Utilities Code section 366.2 (community choice aggregation); Government Code section 8571 (emergency suspension of regulatory statutes)."),
    ("prc", "California Public Resources Code section 25524.2: the moratorium on new nuclear fission plants."),
    ("geo", "National Renewable Energy Laboratory, Annual Technology Baseline 2024 (geothermal); Fervo Energy, Cape Station development record; Southern California Edison and Google geothermal power purchase agreements."),
    ("smr", "Tennessee Valley Authority, Clinch River small modular reactor cost estimates; Ontario Power Generation, Darlington New Nuclear Project cost disclosure."),
    ("lpo", "U.S. Department of Energy Loan Programs Office, Crescent Dunes project record; SolarPACES, 'What happened with Crescent Dunes' (2020)."),
    ("staff", "Operating staff and construction peak of Ivanpah and Crescent Dunes, from the plants' public records; Carlsbad plant staffing."),
    ("reservoir", "California Department of Water Resources. Sites Reservoir cost and capacity; the Edmonston Pumping Plant lift and the San Luis (Gianelli) pumped-storage head."),
]


def build_bibliography():
    """Numbered entries: the study register's sources in order of first citation,
    then the constants' sources. Returns (entries, index-by-key)."""
    entries, index = [], {}

    def add(key, text):
        if key not in index:
            entries.append(text)
            index[key] = len(entries)
        return index[key]

    for _k, _s, _sc, _y, _st, _w, source in ST.STUDIES:
        for part in re.split(r";\s*(?![^()]*\))", source):
            part = scrub(part.strip())
            if part and not part.startswith("this work"):
                add(part, part)
    for key, text in REFERENCES:
        add(key, text)
    return entries, index


# =============================================================================
# THE PROPOSAL
# =============================================================================
def render(g):
    d, p, hr, bo, m = g["design"], g["priced"], g["hourly"], g["both"], g["mirrors"]
    pm, pc = p["mid"], p["critical"]
    bm, bc = bo["mid"], bo["critical"]
    ms = {c: milestones(g, c) for c in CASES}
    bib, bix = build_bibliography()

    def cite(*keys):
        nums = sorted({bix[k] for k in keys if k in bix})
        return "[" + ", ".join(str(n) for n in nums) + "]" if nums else ""

    def cite_source(source):
        parts = [scrub(x.strip()) for x in re.split(r";\s*(?![^()]*\))", source)]
        nums = sorted({bix[x] for x in parts if x in bix})
        own = any(x.startswith("this work") for x in parts)
        s = ", ".join(f"[{n}]" for n in nums)
        return (s + ("; this work" if own else "")).strip("; ") or "this work"

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

    sections = [
        "Summary and the decision requested", "The requirement", "The record of salt-tower solar and the cost of building it",
        "The equipment question", "The energy chain", "The plant", "The plant hour by hour", "Closing the load",
        "The risk register", "Provenance: the studies behind every technology", "The pilot receiver: an acceptance protocol",
        "Studies and surveys first", "Price, the household and the financing", "Title II: the water", "Title III: the joinder",
        "The sites", "Environment, employment, land and procurement", "What is not settled", "How the figures were produced",
    ]

    def h2(n):
        a(f"## {n}. {sections[n - 1]}")
        a("")

    # ---------------------------------------------------------------- front matter
    a(f"# {TITLE}")
    a("")
    a(f"*{SUBTITLE}*")
    a("")
    a(f"**{AUTHOR}**")
    a("")
    a("### Abstract")
    a("")
    a("California's two fundamental scarcities are firm electricity and fresh water, and both are worsening on the same")
    a("timescale. The state's residential load peaks after sunset and in summer, its grid is served at those hours by gas")
    a("and imports at rising prices, and the utilities' generation charge for a household has risen to about")
    a(f"${money(g['today_hh'])} a year. Its water is drawn from an over-allocated river system and from groundwater basins")
    a(f"that are overdrafted by {R3.SGMA_RECHARGE_GAP_MAF[0]:.1f}–{R3.SGMA_RECHARGE_GAP_MAF[1]:.1f} million acre-feet a year in the San Joaquin Valley alone, under a")
    a("statute that now requires the deficit to close. Neither scarcity yields to demand reduction at the scale required,")
    a("and every supply that can meet them at scale is capital-intensive, first-of-a-kind, or both. This proposal sets out")
    a("one state-owned program that addresses the two together: Title I, a concentrating-solar plant of a new")
    a(f"generation, sized to make {g['e_req']:.1f} TWh a year of firm electricity for three million households; Title II, seawater")
    a("reverse-osmosis modules on retired coastal power plants; and Title III, the contract and the one shared asset that")
    a("join them, by which the plant's summer surplus lifts the water to an elevated reservoir and the water's year-round")
    a("descent closes the plant's evening peak. Every figure is computed rather than asserted, at a middle case and at a")
    a("critical case in which every uncertain constant sits at its adverse end, and the design is held to the critical")
    a(f"case. The program costs ${program_b(g, 'mid'):.0f} to {program_b(g, 'critical'):.0f} billion once, carries no public money after the build, and returns a")
    a(f"household's generation charge to ${money(H.per_household(g['postbond']['mid']))}–{money(H.per_household(g['postbond']['critical']))} a year once the bonds retire. It proceeds in stages, each")
    a(f"reversible until a pilot receiver has passed a test whose pass mark is fixed in advance; the first stage is ${g['predev']['mid']['total_m']:.0f}")
    a(f"to {g['predev']['critical']['total_m']:.0f} million of studies and surveys, which is the decision this document requests.")
    a("")
    a("### Contents")
    a("")
    for i, s in enumerate(sections, 1):
        a(f"- {i}. {s}")
    a("- Bibliography")
    a("")
    a("**How to read the figures in this document.** Every number is printed at two cases. *Mid* is the middle of each")
    a("constant's band; *critical* is the adverse end of every band at once. The design is held to critical, and the mid")
    a("column is margin. A number quoted without its case is misquoted. Each figure also carries a status: SOURCED is a")
    a("published figure with its source in the bibliography; ASSUMED is a band the record does not fix, stated as such;")
    a("RECONSTRUCTED is a shape or split rebuilt from physics or from a published model; DERIVED is computed from the")
    a("others; DECIDED is a choice this work has made and recorded. A status is never flattened: how a number was got is")
    a("part of what it is.")
    a("")
    # ---------------------------------------------------------------- 1
    h2(1)
    a("The program is one state-owned enterprise under one Authority, two severable projects, funded once by bonds and")
    a("never again by the treasury. Title I builds a concentrating-solar plant on three desert nodes, with falling-particle")
    a("receivers and supercritical-CO₂ turbines in place of nitrate salt and steam, photovoltaics serving the daytime load")
    a(f"directly and a mirror field sized for the night, to make **{g['e_req']:.1f} TWh** of firm electricity a year for three million")
    a(f"households. Title II builds **{bm['modules']:.0f} to {bc['modules']:.0f}** seawater reverse-osmosis modules of 50,000 acre-feet a year on retired")
    a("coastal power plants. Title III lifts the water to an elevated reservoir with Title I's summer surplus and returns it")
    a("year-round through pump-turbines to Title I's evenings, and states the contract, the shared asset and the")
    a("severability that make the two projects one program without making either dependent on the other.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("Title I plant with its risk register, $B", pm["capex_net"] / 1e3, pc["capex_net"] / 1e3, "{:.1f}")
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
    a(f"**The decision requested.** Fund the studies and surveys now, at ${g['predev']['mid']['total_m']:.0f} to {g['predev']['critical']['total_m']:.0f} million, and know within")
    a(f"{g['predev']['mid']['gate_years']:.0f} to {g['predev']['critical']['gate_years']:.0f} years whether the rest is worth ${program_b(g, 'mid'):.0f} to {program_b(g, 'critical'):.0f} billion. Nothing irreversible is bought before the")
    a("pilot receiver has passed its test.")
    a("")
    fig("fig-10-capital.png", "The program's capital at the adopted route, both cases.")
    # ---------------------------------------------------------------- 2
    h2(2)
    a(f"**Households.** Three million households is the program's minimum, growing with population. At the state average of")
    a(f"{H.HH_KWH_YR:,.0f} kWh a year per residential customer {cite('eia')} that is **{g['e_req']:.1f} TWh** of firm supply, growing to **{g['growth'][0]:.2f}–{g['growth'][1]:.2f}×** over the")
    a(f"{H.BOND_TERM_Y}-year bond term at {100 * H.GROWTH_BAND[0]:.0f}–{100 * H.GROWTH_BAND[1]:.0f} % a year of residential growth including electrification. California has")
    a(f"{H.CA_RES_CUSTOMERS:,} residential customers {cite('eia')}, so three million is a fifth of them, and a program that serves them at the")
    a("state average serves the households that consume least, which is the fairer half of any tariff question.")
    a("")
    a("**The criterion.** The plant must pay for itself after the build bonds: revenue must cover debt service and O&M in")
    a(f"every year of the {H.BOND_TERM_Y}-year term, with the coverage a bond buyer requires, and after the term everything above O&M is")
    a("the household's dividend. A free tariff is therefore an output of the balance and never an input to it. Inverted, the")
    a("criterion is a required price per MWh, and it is read against two references.")
    a("")
    a("| reference | $/MWh | $ per household per year |")
    a("|---|---|---|")
    a(f"| what a household pays the utility for generation today ({H.GEN_RATE_NOW:.3f} $/kWh) | {g['today_mwh']:.0f} | {money(g['today_hh'])} |")
    a(f"| what California's load-serving entities pay for firm clean energy under contract | {H.FIRM_CLEAN_PPA[0]:.0f}–{H.FIRM_CLEAN_PPA[1]:.0f} | {money(H.per_household(H.FIRM_CLEAN_PPA[0]))}–{money(H.per_household(H.FIRM_CLEAN_PPA[1]))} |")
    a("")
    a("**Size is not a lever.** Because the households are a requirement, the plant cannot be shrunk to make the price close.")
    a("Only the equipment and the ownership form move the price, and the sections that follow work through both.")
    a("")
    # ---------------------------------------------------------------- 3
    h2(3)
    a("The natural first candidate for firm solar power in California is the nitrate-salt power tower, the one form of")
    a("concentrating solar with a commercial storage record. This section establishes what such a plant actually makes and")
    a("what it actually costs, because both are commonly overstated and the program's design follows from the difference.")
    a("")
    a(f"**What a salt-tower plant of the size first considered makes.** A plant of {H.GROSS_MWE:,.0f} MWe gross across three desert nodes,")
    a(f"with {H.APERTURE_M2 / 1e6:.1f} million m² of heliostats and {H.STORAGE_MWH_TH / 1e3:,.0f} GWh_th of salt storage, run hour by hour on exact solar geometry at")
    a(f"each node's annual direct-normal irradiance {cite('nsrdb')}, with the salt tank, the turbine's part-load curve and the parasitic")
    a("loads modelled explicitly:")
    a("")
    a("| | figure |")
    a("|---|---|")
    a(f"| net output, TWh/yr | {g['pf']['net_twh']:.1f} |")
    a(f"| net capacity factor | {g['pf']['cf_net']:.3f} |")
    a(f"| revenue selling everything at the 2024 CAISO price shape {cite('caiso')}, $M/yr | {g['revenue_2024_m']:,.0f} |")
    a(f"| revenue with ${H.CLAIMED_PEAK_PRICES[2]:.0f}/MWh on the four peak hours of every day, the rest at the 2024 shape, $M/yr | {g['revenue_peak_m']:,.0f} |")
    a(f"| carrying cost at ${H.CAPEX_B:.1f} B of capital, {100 * H.BOND_RATE:.2f} % and {H.BOND_TERM_Y} years, plus ${H.OM_M:.0f} M of O&M, $M/yr | {g['carrying_m']:,.0f} |")
    a(f"| required price at ${H.CAPEX_B:.1f} B, $/MWh | {g['req_price_asbuilt']:.0f} |")
    a("")
    a(f"Two things follow. Such a plant makes {g['pf']['net_twh']:.1f} TWh, about what three million households consume, and no more: a firm")
    a("export on top of the in-state supply does not exist. And evening-peak pricing exists for about 1,500–2,000 hours a")
    a(f"year while {H.NEG_HOURS_2024:,} hours in 2024 cleared negative {cite('caiso')}, so a plant that sells at the market shape earns a third")
    a(f"of its carrying cost. At ${H.CAPEX_B:.1f} B of capital the required price would be ${g['req_price_asbuilt']:.0f}/MWh, inside the contract band; the")
    a("question is whether the plant can be built for that.")
    a("")
    a(f"**What it costs to build.** Line by line at the class that exists (Noor III-class heliostats of {HC.HELIOSTAT_M2:.0f} m² on {HC.TOWERS} towers of")
    a(f"{HC.TOWER_HEIGHT_M:.0f} m), state-owned, groundbreaking {HC.GROUNDBREAK[0]}–{HC.GROUNDBREAK[1]}: no developer margin, bond-rate interest during construction, the")
    a("federal storage credit with the public direct-pay and energy-community bonuses, public-pension on-cost, property tax")
    a(f"out and a payment in lieu in. The level is calibrated to NREL's 2024 technology baseline at ${HC.ATB_2024_PER_KWE:,.0f}/kWe {cite('atb')} and")
    a(f"the split is reconstructed from the System Advisor Model's published cost structure {cite('sam')}.")
    a("")
    a("| case | net capital, $B | $/W gross | required price, $/MWh | $ per household |")
    a("|---|---|---|---|---|")
    for (c, (_n, pr)), hh in zip(zip(("low", "mid", "high"), g["hc_price"]), g["hh_at_hc"]):
        a(f"| {c} | {g['hc'][c]['net_capex'] / 1e3:.1f} | {g['hc_perw'][c]:.2f} | {pr:.0f} | {money(hh)} |")
    a(f"| at ${H.CAPEX_B:.1f} B, for comparison | {H.CAPEX_B:.1f} | {H.CAPEX_B * 1e9 / (H.GROSS_MWE * 1e6):.2f} | {g['req_price_asbuilt']:.0f} | {money(H.per_household(g['req_price_asbuilt']))} |")
    a("")
    a(f"A ${H.CAPEX_B:.1f} B figure for this plant is {g['hc']['low']['net_capex'] / 1e3 / H.CAPEX_B:.2f}× below the low case. **At the built cost, a salt-tower plant of this size does")
    a("not pay for itself after the bonds at any case**, and at the mid case it charges a household more than the utility does")
    a("today. The built record is the reason:")
    a("")
    a("| plant | $/W gross as built | year | storage, h |")
    a("|---|---|---|---|")
    for n, w, y, hrs in HC.BUILT_PER_W:
        a(f"| {n} | {w:.2f} | {y} | {hrs:.1f} |")
    a("")
    a("And what those plants delivered against their design:")
    a("")
    a("| plant | delivered / designed | the year, and why |")
    a("|---|---|---|")
    for n, f, note in g["fidelity"]:
        a(f"| {n} | {f:.2f} | {note} |")
    a("")
    a(f"No commercial salt tower has delivered its design output {cite('lpo')}, and an hourly model still flatters that record.")
    a("That is why every figure in this document is printed at a critical case, and why the design is held to it.")
    a("")
    fig("fig-01-built-record.png", "Salt-tower concentrating solar as built, in dollars per watt gross, against the capital first considered.")
    # ---------------------------------------------------------------- 4
    h2(4)
    a(f"Before a technology is chosen, every candidate that can make a firm MWh in California is sized to the same {g['e_req']:.1f} TWh,")
    a("state-owned, and priced on the one criterion. The salt tower is priced from the line-by-line build above; the")
    a("built-up candidates from their parts; the alternatives at their low, mid and high bands, the high band standing")
    a("where the critical case stands elsewhere.")
    a("")
    a("| candidate | MW | mid: net capital $B / price $/MWh / $ per household | band top: net capital $B / price $/MWh | acres | status |")
    a("|---|---|---|---|---|---|")
    for k in ("salton_flash", "egs", "pv_salt", "csp_proposed", "pv_ironair", "smr"):
        fm, fc = g["fp"]["mid"][k], g["fp"]["critical"][k]
        cap = " (capped: exceeds the developable resource)" if fm.get("capped") else ""
        top = "mid only" if k == "csp_proposed" else f"{fc['capex_net'] / 1e3:.1f} / {fc['price']:.0f}"
        legal = scrub(FP.TECH[k]["legal"]).replace("; open", "")
        a(f"| {scrub(FP.TECH[k]['name']).replace(' (heliocost mid)', '')} | {fm['mw']:,.0f} | {fm['capex_net'] / 1e3:.1f} / {fm['price']:.0f} / {money(H.per_household(fm['price']))} | {top} | {fm['acres']:,.0f} | {legal}{cap} |")
    a(f"| {FP.TECH['offshore_wind']['name']} | — | — | — | — | {FP.TECH['offshore_wind']['legal']}; {FP.TECH['offshore_wind']['status']} |")
    a("")
    port = g["fp_port"]
    a(f"Two results stand out. Salton Sea geothermal, in the program's own Imperial node, has {FP.TECH['salton_flash']['cap_mw']:,.0f} MW developable, {port['e_geo'] / g['e_req']:.2f} of")
    a(f"the requirement, and prices at ${g['fp']['mid']['salton_flash']['price']:.0f}/MWh at mid {cite('geo')}; its hypersaline capital band is assumed, and it cannot grow with")
    a(f"the requirement. The small modular reactor is barred by statute {cite('prc', 'smr')}. Concentrating solar is chosen on a different ground:")
    a("it is the one firm-solar form whose output can be raised by engineering within the program's control, and the rest of")
    a("this document is the engineering. The comparison is kept beside the choice so that the choice is priced.")
    a("")
    fig("fig-02-candidates.png", "Every firm candidate sized to the requirement, state-owned, required price at mid and at the band's top.")
    # ---------------------------------------------------------------- 5
    h2(5)
    a("Sun to socket is a product of seven links, `E = A · DNI · opt · rec · tes · dispatch · cycle · (1 − par) · avail`. Each")
    a("is stated for the salt tower as it exists, at the best achieved or designed, and at its physical bound:")
    a("")
    a("| link | salt tower as it exists | best achieved / designed | bound | status of the best |")
    a("|---|---|---|---|---|")
    for k, name, _hv, best, bound, status in C.CHAIN:
        a(f"| {name} | {g['base_links'][k]:.3f} | {'—' if best is None else f'{best:.3f}'} | {'—' if bound is None else f'{bound:.3f}'} | {scrub(status)} |")
    a("")
    prod_base = C.chain_product(g["base_links"].values())
    prod_best = C.chain_product(g["best_links"].values())
    a(f"The salt tower's product is **{prod_base:.3f}** sun to socket; the best chain is **{prod_best:.3f}**, ×{prod_best / prod_base:.2f}. Three links move: the cycle")
    a(f"({H.ETA_CYCLE:.2f} for steam at 565 °C against {g['best_links']['cycle']:.2f} for supercritical CO₂ at 715 °C), the optics ({g['base_links']['opt']:.3f} against a Noor")
    a(f"III-class field's {g['best_links']['opt']:.2f}), and the one thing no link fixes: **a thermal plant serves daytime load at {H.ETA_CYCLE:.0%} where a panel")
    a("serves it at 100 %.** The daytime third of the load should therefore never touch a mirror, and the mirror field should")
    a("be sized for the night. Two plants on that architecture, against the salt tower scaled to the requirement:")
    a("")
    a(f"| | salt tower, scaled to {g['e_req']:.1f} TWh | Helios-2 (nitrate salt, steam) | Helios-3 (particles, sCO₂), mid |")
    a("|---|---|---|---|")
    br, h2_, h3 = g["baseline_row"], g["h2"], d["mid"]
    a(f"| mirror aperture, M m² | {br['aperture'] / 1e6:.1f} | {h2_['aperture'] / 1e6:.1f} | {h3['aperture'] / 1e6:.1f} |")
    a(f"| towers, Noor III class | {br['towers']:.0f} | {h2_['towers']:.0f} | {h3['towers']:.0f} |")
    a(f"| thermal block, MWe | {br['mw']:,.0f} | {h2_['turb_mw']:,.0f} | {h3['turb_mw']:,.0f} |")
    a(f"| PV, MW_AC | — | {h2_['pv_mw']:,.0f} | {h3['pv_mw']:,.0f} |")
    a(f"| price, $/MWh | {br['price']:.0f} | {h2_['price']:.0f} | {h3['price']:.0f} |")
    a(f"| $ per household per year (today {money(g['today_hh'])}) | {money(H.per_household(br['price']))} | {money(H.per_household(h2_['price']))} | {money(H.per_household(h3['price']))} |")
    a(f"| status | built class | {scrub(h2_['status'])} | {scrub(h3['status'])} |")
    a("")
    a(f"Helios-2 is **{br['aperture'] / h2_['aperture']:.1f}× smaller in mirror** for the same energy and every part of it has been built. Helios-3 replaces the")
    a("salt with sintered-bauxite particles and the steam cycle with supercritical CO₂; it is a pilot-stage technology, and")
    a("the program adopts it on the condition, enforced in Section 11, that its receiver passes a test before any module is")
    a("ordered, with Helios-2's salt block on the same field as the recorded fallback.")
    a("")
    fig("fig-03-chain.png", "The chain, link by link: the salt tower as it exists, Helios-3 at mid, Helios-3 at critical.")
    # ---------------------------------------------------------------- 6
    h2(6)
    a("Helios-3 is a Noor III-class surround heliostat field sized for the night; a multi-aperture falling-particle receiver")
    a("behind a compound quartz aperture (a hexagonal low-OH rod-lens dome on a cooled lattice frame); sintered-bauxite")
    a("particles as medium and store, in cold-shell refractory-lined silos with replaceable liners, not buried; a moving")
    a("packed-bed particle-to-sCO₂ exchanger into a 715 °C, 250 bar supercritical-CO₂ recompression Brayton block, dry-cooled")
    a("at 45 °C ambient; Inconel 740H pressure parts with Haynes 282 and Inconel 617 on the alloy ladder; photovoltaics")
    a("serving the daytime load directly and feeding electric particle heaters in winter; one cold-side particle lift per")
    a(f"aperture, gravity everywhere else. The cycle is {g['cycle']['helios3']} at {g['cycle']['helios3_eta']:.2f} gross; the nitrate-salt fallback")
    a(f"on the same field is {g['cycle']['fallback']} at {g['cycle']['fallback_eta']:.2f}.")
    a("")
    a("**The chain at both cases.** The critical receiver figure comes from the receiver model of Section 6.3, handed up the")
    a("chain rather than taken from the chain's own best: a downstream calculation hands its critical figure to the one above it.")
    a("")
    a("| link | mid | critical |")
    a("|---|---|---|")
    for k, name in (("opt", "field optical efficiency, annual"), ("rec", "receiver thermal efficiency"), ("tes", "storage round trip"),
                    ("dispatch", "dispatch"), ("cycle", "power cycle, gross"), ("par", "1 − parasitic share"), ("avail", "availability")):
        a(f"| {name} | {d['mid']['links'][k]:.3f} | {d['critical']['links'][k]:.3f} |")
    a(f"| **sun to socket** | **{C.chain_product(d['mid']['links'].values()):.3f}** | **{C.chain_product(d['critical']['links'].values()):.3f}** |")
    a("")
    a("**Sized to the requirement**, and on the adopted route of Section 8:")
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
    both_row("**on the adopted route**: mirror aperture, M m²", d["mid"]["aperture"] * bm["field"] / 1e6, d["critical"]["aperture"] * bc["field"] / 1e6, "{:.1f}")
    both_row("on the adopted route: towers", d["mid"]["towers"] * bm["field"], d["critical"]["towers"] * bc["field"])
    both_row("on the adopted route: sCO₂ block, MWe", d["mid"]["turb_mw"] * bm["block"], d["critical"]["turb_mw"] * bc["block"])
    both_row("on the adopted route: land, acres", g["land"]["mid"]["acres"], g["land"]["critical"]["acres"])
    a("")
    a("**Direct cost by line, $M, before contingency, EPC, tax, escalation and interest.** The field, tower, receiver and")
    a("balance-of-plant lines use the same calibrated rates as the salt tower of Section 3; the particle and sCO₂ lines")
    a(f"come from the Gen3 and STEP programme records {cite('Sandia Gen3 Roadmap / TEA (Ho et al. 2019-2021)', 'DOE SunShot sCO2 (2012-2018)')}.")
    a("")
    a("| line | mid | critical |")
    a("|---|---|---|")
    for k in d["mid"]["lines"]:
        both_row(k, d["mid"]["lines"][k], d["critical"]["lines"][k])
    both_row("**direct total**", sum(d["mid"]["lines"].values()), sum(d["critical"]["lines"].values()), "{:,.0f}", True)
    a("")
    a("### 6.3. The receiver")
    a("")
    a("A falling curtain is a per-metre machine: its power goes with its width, so scale is bought in width and in aperture")
    a("count, the loss fraction at fixed flux does not change with size, and the edge losses shrink as perimeter over area.")
    a("The receiver model runs with every banded constant at nominal and at critical; the critical flux is halved to")
    a(f"{RX.FLUX_MW_M2[1]:.1f} MW/m², below the {RX.DEMO_FLUX_MW_M2[0]:.1f}–{RX.DEMO_FLUX_MW_M2[1]:.1f} MW/m² at which the largest curtain was measured {cite('Ho et al., AIP Conf. Proc. 1734 (2016)')}.")
    a("")
    a("| | nominal (mid) | critical |")
    a("|---|---|---|")
    both_row("open-aperture thermal efficiency", g["rx"]["mid"]["open"], g["rx"]["critical"]["open"], "{:.3f}")
    both_row("with the compound quartz dome", g["rx"]["mid"]["domed"], g["rx"]["critical"]["domed"], "{:.3f}")
    both_row("field factor handed upstream, against the chain's own receiver link", g["rx"]["mid"]["field"], g["rx"]["critical"]["field"], "{:.2f}")
    a("")
    a(f"The dome loses on the model and pays on the measured record, and both are printed. The critical open receiver, **{g['rx']['critical']['open']:.3f}**")
    a(f"against the chain's {g['best_links']['rec']:.2f}, grows the field by **{g['rx']['critical']['field']:.2f}**, and that is what the critical column carries. The ladder of")
    a("scale, from what has run to a fleet tower:")
    a("")
    a("| rung | MW_th | step |")
    a("|---|---|---|")
    for name, mw, f in g["ladder"]:
        a(f"| {name} | {mw:,.0f} | {'—' if f is None else f'×{f:.1f}'} |")
    a("")
    a(f"The first 100 MWe module is already {g['ladder'][2][1] / g['ladder'][3][1]:.2f} of a fleet tower's duty, so a pilot aperture at about {PL.PILOT_MWTH:.0f} MW_th belongs")
    a("before it (Section 11).")
    a("")
    # ---------------------------------------------------------------- 7
    h2(7)
    a("The chain sizes the plant on annual energy. Run through 8,760 hours across the three nodes, with photovoltaics")
    a("serving the load first, the block serving the residual from the store and the heaters charging the store from")
    a("surplus PV, the plant as sized serves less than the annual chain implies. The load shape is reconstructed: residential,")
    a("evening-peaked, summer-peaked, pinned to the sourced annual; measured hourly profiles replace it as they become")
    a("available and the sizing is re-run.")
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
    a("**By month, mid** (TWh; the critical share beside the last column):")
    a("")
    a("| month | load | PV direct | block net | heaters (PV in) | unserved | share unserved, mid / critical |")
    a("|---|---|---|---|---|---|---|")
    for i in range(1, 13):
        r, rc = hr["mid"], hr["critical"]
        a(f"| {HR.MONTHS[i]} | {r['month_load'][i] / 1e6:.2f} | {r['month_pv_direct'][i] / 1e6:.2f} | {r['month_net'][i] / 1e6:.2f} | {r['month_heater'][i] / 1e6:.2f} | {r['month_unserved'][i] / 1e6:.2f} | {r['month_unserved'][i] / r['month_load'][i]:.1%} / {rc['month_unserved'][i] / rc['month_load'][i]:.1%} |")
    a("")
    a("**What the annual chain cannot see.** The block is sized to the average night and a residential load peaks after")
    a("sunset, so the block cannot carry the evening in any month; the shortfall is year-round and evening-led, worst in")
    a(f"December at {hr['mid']['month_unserved'][12] / hr['mid']['month_load'][12]:.0%} (mid). Sixteen hours of store cannot move June into December: the store empties on winter")
    a("nights while a share of June's field is defocused. The heaters and PV overbuild are not the lever; the block, the")
    a("field and the water are, and Section 8 prices each.")
    a("")
    a(f"**The Central Valley node.** Its irradiance is {g['cv']['dni_ratio']:.2f} of the Mojave's. Moving it to a desert site lifts the served share from")
    a(f"{g['cv']['served_as_sited']:.3f} to {g['cv']['served_all_desert']:.3f} and December's shortfall from {g['cv']['dec_as_sited']:.1%} to {g['cv']['dec_all_desert']:.1%}, and does not change the closing sizing. The")
    a("node is kept for its land (Section 16), which the deserts do not offer in fallowed, private, disturbed form.")
    a("")
    fig("fig-04-monthly.png", "The load by month and what the plant as sized serves, both cases.")
    fig("fig-05-load-shape.png", "The residential load shape on a late-July and a late-December day, relative to the annual mean hour; the shaded band is the day PV serves directly.")
    # ---------------------------------------------------------------- 8
    h2(8)
    mb, mf, msd = HR.MIRRORS_ROUTE
    a(f"**Three routes.** The *mirrors* route grows the block to ×{mb:.2f}, the field to ×{mf:.1f} and the store to {msd:.0f} days, the cheapest")
    a("point that closes the shortfall to 1 % with the plant alone. The *water* route lifts Title II's product to an elevated")
    a("reservoir with the summer surplus (the field the plant would otherwise defocus and the PV it would curtail) and")
    a(f"returns it year-round through pump-turbines to the evenings, the reservoir holding {J.RESERVOIR_DAYS[0]:.0f} / {J.RESERVOIR_DAYS[1]:.0f} days rather than a season")
    a("because the water is delivered year-round, as summer irrigation and winter recharge. The feasibility rule is that a")
    a("closing point must lift its water inside its own surplus: a lift bought from the grid is not this route. **Water alone")
    a("has no feasible point on this load**, because with the field and store at design the block that closes the evening")
    a("consumes the spill the lift runs on. **The adopted route is both**: the water returns half the shortfall and the plant")
    a("the other half, each point on a ladder over the water's share required to lift inside its own surplus.")
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
    a("The two levers fail differently and each carries a real share, which is the reason for choosing both over the")
    a("cheapest point: a cheapest-point search returns the mirrors with a token water plant, and a program served by one")
    a("thing is a program with one failure mode. Two features of the table should be read carefully. The water is *sized*")
    a(f"to return half the shortfall as sized ({bm['budget_twh']:.2f} TWh at mid) and the run *dispatches* {bm['hydro_twh']:.2f}, because the larger block serves the")
    a("evening first and the pump-turbines take what it leaves; the modules are sized on the shortfall, so the water plant")
    a("runs at about half its evening sizing and all of its water is delivered as irrigation and recharge regardless. That is")
    a("the conservative side for Title II and the expensive side for Title I. And the mirrors-alone figure the comparison")
    a(f"uses is the one fixed route above (${m['mid']['cost_b']:.1f} / {m['critical']['cost_b']:.1f} B); the ladder's own scan, which lets the block and field vary per")
    a(f"case, finds a cheaper mirrors-only point at critical (${g['scan']['critical']['ladder'][0.0]['title1_b']:.1f} B). Both are printed.")
    a("")
    a(f"**The hydraulics.** The adopted route is priced at one head, {B.HEAD_M:.0f} m (assumed; the Edmonston lift is 587 m and the Gianelli")
    a(f"head about 100 {cite('reservoir')}), at both cases. There a cubic metre returns {g['hyd']['mid']['returned_kwh_m3']:.3f} / {g['hyd']['critical']['returned_kwh_m3']:.3f} kWh and costs")
    a(f"{g['hyd']['mid']['lift_kwh_m3']:.3f} / {g['hyd']['critical']['lift_kwh_m3']:.3f} kWh to lift, a round trip of {g['hyd']['mid']['round_trip']:.2f} / {g['hyd']['critical']['round_trip']:.2f}; reverse osmosis itself takes {AQ.RO_KWH_M3[0]:.1f}–{AQ.RO_KWH_M3[1]:.1f} kWh/m³ on")
    a("Title II's own account. The lift is invariant in head, being the returned energy over the round trip, so feasibility")
    a("does not depend on the site; the volume, and so the modules and Title II's capital, go as one over head. The")
    a(f"pump-turbine plant and reservoir carry O&M at {100 * J.HYDRO_OM_SHARE[0]:.1f} / {100 * J.HYDRO_OM_SHARE[1]:.1f} % of their capital a year (assumed band).")
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
    fig("fig-06-ladder.png", "The ladder over the water's share: Title I's capital to close the load at each share, both cases, every point carrying the larger field.")
    fig("fig-07-head.png", "Title II modules the adopted route needs against the reservoir head, at each case's days of holding.")
    # ---------------------------------------------------------------- 9
    h2(9)
    a("A plant of a new generation carries risks a salt tower does not, and a proposal that prices the plant must price")
    a("them. Sixteen rows are graded before and after mitigation, each carried by a named part of the build, each marked")
    a("DESIGN (retired by specification), HOURS (retired only by operating time) or BENEFIT, and each with the evidence")
    a("that grades it. An HOURS row is never flattened: a specification cannot make a machine have run, and the rows so")
    a("marked are what the pilot of Section 11 and the ladder of Section 10 exist to retire.")
    a("")
    for rid, risk, before, mit, after, kind, carrier, source in H3.REGISTER:
        a(f"**{rid}. {scrub(risk)}** — {before} → **{after}**, {kind}.")
        a("")
        a(f"- *Mitigation:* {scrub(mit)}")
        a(f"- *Carried by:* {scrub(carrier)}")
        a(f"- *Evidence:* {scrub(source)}")
        adder = pm["adders"].get(rid)
        if adder:
            a(f"- *Priced:* ${adder:,.0f} M at mid, ${pc['adders'].get(rid, 0.0):,.0f} M at critical")
        a("")
    b0, b1 = g["grades"]
    a("Before mitigation: " + ", ".join(f"{v} {k}" for k, v in b0.items() if v) + ". After: " + ", ".join(f"{v} {k}" for k, v in b1.items() if v) + ".")
    a("")
    a("**The risk register, priced**, from the direct lines to the net capital:")
    a("")
    a("| $M | mid | critical |")
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
    both_row("direct plant lines (Section 6)", stack["mid"]["direct"], stack["critical"]["direct"])
    both_row("mitigation adders, direct", pm["mit_total"], pc["mit_total"])
    both_row(f"contingency ({100 * HC.CONTINGENCY[1]:.0f} / {100 * HC.CONTINGENCY[2]:.0f} %), EPC and owner's cost ({100 * HC.EPC_OWNER[1]:.0f} / {100 * HC.EPC_OWNER[2]:.0f} %), sales tax on those", stack["mid"]["overhead"], stack["critical"]["overhead"])
    both_row("studies and surveys (Section 12), with contingency", stack["mid"]["studies"], stack["critical"]["studies"])
    both_row(f"first-module premium ({H3.FIRST_MODULE_PREMIUM:.1f}× / {H3.FIRST_MODULE_PREMIUM_CRITICAL:.1f}× on its share of the thermal block)", pm["foak"], pc["foak"])
    both_row("overnight, groundbreaking dollars", stack["mid"]["over"], stack["critical"]["over"])
    both_row(f"escalation to the build and interest during construction ({HC.BUILD_YEARS:.0f} years at the bond rate)", stack["mid"]["escidc"], stack["critical"]["escidc"])
    both_row("gross capital", stack["mid"]["gross"], stack["critical"]["gross"])
    both_row("federal storage credit, direct pay", -pm["credit"], -pc["credit"])
    both_row("**net capital with the register**", pm["capex_net"], pc["capex_net"], "{:,.0f}", True)
    both_row(f"O&M with particle makeup ({100 * H3.PARTICLE_MAKEUP_PER_YEAR:.0f} / {100 * H3.PARTICLE_MAKEUP_CRITICAL:.0f} %/yr) and rejuvenation, $M/yr", pm["om"], pc["om"])
    both_row("price with the register, $/MWh", pm["price"], pc["price"])
    a("")
    # ---------------------------------------------------------------- 10
    h2(10)
    a(f"No plant of this kind exists at commercial scale, so the provenance of each technology must be listed rather than")
    a(f"asserted. The register below holds {len(ST.STUDIES)} rows over the {len(ST.TECHNOLOGIES)} technologies the design uses, each with a status from a")
    a("closed set — OPERATED (a plant has run at the stated scale), TESTED (a prototype has run, below plant scale),")
    a("DESIGNED (a published design or code case; nothing has run), or this work's own analysis — and each with its")
    a("sources in the bibliography. The register is complete over technologies and a floor over studies: a technology may")
    a("have more studies than are listed, never fewer.")
    a("")
    for key, tech, need in ST.TECHNOLOGIES:
        n = [t[0] for t in ST.TECHNOLOGIES].index(key) + 1
        a(f"### 10.{n}. {scrub(tech)}")
        a("")
        a(f"*What the design needs:* {scrub(need)}.")
        a("")
        a("| study or plant | scale | year | status | what it settled | sources |")
        a("|---|---|---|---|---|---|")
        for _k, study, scale, year, status, settled, source in ST.by_tech(key):
            st = "THIS WORK" if status == "AUTHOR" else status
            a(f"| {scrub(study)} | {scrub(scale)} | {year} | {st} | {scrub(settled)} | {cite_source(source)} |")
        rec = next(r for r in ST.RECOMMEND if r[0] == key)
        a("")
        if key == "architecture":
            a(f"*Further study, on the first rung:* the plant run hour by hour at both cases (Section 7), which found the shortfall year-round")
            a("and evening-led and set the closing routes of Section 8.")
        else:
            a(f"*Further study recommended, on the {rec[4]} rung ({rec[3]:.1f} years):* {scrub(rec[1])}. *It settles:* {scrub(rec[2])}.")
        a("")
    a(f"**The critical path of study is {g['path_years']:.1f} years**, run against the build rather than before it, the studies within a rung in")
    a(f"parallel. Delay escalates the whole plant at {100 * HC.ESCALATION:.0f} % a year (assumed band 2–4 %) before a dollar is spent:")
    a("")
    a("| per year of delay | mid | critical |")
    a("|---|---|---|")
    both_row("capital, $B", g["delay"]["mid"]["delta_capex_m"] / 1e3, g["delay"]["critical"]["delta_capex_m"] / 1e3, "{:.2f}")
    both_row("price, $/MWh", g["delay"]["mid"]["delta_price"], g["delay"]["critical"]["delta_price"], "{:.1f}")
    both_row("household, $/yr", g["delay"]["mid"]["delta_hh"], g["delay"]["critical"]["delta_hh"])
    a("")
    # ---------------------------------------------------------------- 11
    h2(11)
    pl = g["pilot"]
    a("The receiver's real efficiency is the one open item no calculation can close, and a test graded after it runs is not")
    a("a test. The unit, the measurements and the pass mark are therefore fixed here, before the pilot is built.")
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
        a(f"- **{name}.** {scrub(how)}. *Condition:* {scrub(what)}.")
    a("")
    u = pl["u"]
    a(f"**The pass mark**, the thermal efficiency at critical conditions averaged over the last {PL.GRADED_HOURS:.0f} of {PL.ON_SUN_HOURS:.0f} on-sun hours, with")
    a(f"a calorimetric uncertainty of **{100 * u:.1f} %** in quadrature (mass flow {100 * PL.U_MASSFLOW:.0f} %, temperatures {100 * PL.U_DT:.0f} %, flux {100 * PL.U_FLUX:.0f} %):")
    a("")
    a("| grade | measured efficiency | what follows |")
    a("|---|---|---|")
    a(f"| PASS-CHAIN | ≥ {pl['th']['chain'] * (1 + u):.3f} | the chain's own link is witnessed; the mid case is witnessed too |")
    a(f"| PASS-DESIGN | ≥ {pl['th']['critical_open'] * (1 + u):.3f} | the critical design basis holds; the first module is ordered |")
    a(f"| UNDECIDED | {pl['th']['critical_open'] * (1 - u):.3f} – {pl['th']['critical_open'] * (1 + u):.3f} | not a pass and not a fail; the pilot runs on |")
    a(f"| FAIL | < {pl['th']['critical_open'] * (1 - u):.3f} | the salt-block fallback is the recorded route; the first module is not ordered |")
    a("")
    a("**What each result does upstream**, priced against each case's own receiver link, so that a pass at the design basis")
    a("costs the critical design nothing:")
    a("")
    a("| measured | grade | field factor, mid / critical | price, mid / critical, $/MWh |")
    a("|---|---|---|---|")
    for e, cons in pl["cons"].items():
        a(f"| {e:.3f} | {pl['grades'][e]} | {cons['mid_factor']:.2f} / {cons['critical_factor']:.2f} | {cons['mid']:+.0f} / {cons['critical']:+.0f} |")
    a("")
    a(f"Scheduled {pl['tranche']['mid']['years'][0]:.0f}–{pl['tranche']['mid']['years'][1]:.0f} (mid) / {pl['tranche']['critical']['years'][0]:.0f}–{pl['tranche']['critical']['years'][1]:.0f} (critical) at ${pl['tranche']['mid']['cost_m']:.0f} / {pl['tranche']['critical']['cost_m']:.0f} M including the ladder's technology")
    a("studies. The protocol's constants are assumed and marked; the pass mark is not.")
    a("")
    # ---------------------------------------------------------------- 12
    h2(12)
    a("Every study and survey is its own line item, first in priority and first in the capital. The costs are bands from")
    a("the class of study rather than quotes, and are marked as such; they are carried ahead of every plant line, with")
    a("contingency and without EPC margin or sales tax.")
    a("")
    a("**Title I.** Gating studies must finish before the field is built; the technology studies run on the ladder against the build.")
    a("")
    a("| id | study or survey | what it settles | scope | mid: $M each × n = total, years | critical: the same |")
    a("|---|---|---|---|---|---|")
    for rm, rc in zip(g["predev"]["mid"]["rows"], g["predev"]["critical"]["rows"]):
        a(f"| {rm['id']} | {scrub(rm['name'])} | {scrub(rm['settles'])} | {rm['scope']}, {'GATE' if rm['gate'] else 'ladder'} | {rm['unit_m']:.1f} × {rm['n']} = {rm['cost_m']:.1f}, {rm['years']:.1f} | {rc['unit_m']:.1f} × {rc['n']} = {rc['cost_m']:.1f}, {rc['years']:.1f} |")
    a("")
    a(f"The {PL.PILOT_MWTH:.0f} MW_th pilot aperture is priced as its own tranche (Section 13) and is not repeated here.")
    a("")
    a("| Title I | mid | critical |")
    a("|---|---|---|")
    both_row("gating studies and surveys, $M", g["predev"]["mid"]["gate_m"], g["predev"]["critical"]["gate_m"])
    both_row("technology studies on the ladder, $M", g["predev"]["mid"]["ladder_m"], g["predev"]["critical"]["ladder_m"])
    both_row(f"owner's engineer on the study phase ({100 * PD.OWNERS_ENGINEER_SHARE[0]:.0f} / {100 * PD.OWNERS_ENGINEER_SHARE[1]:.0f} %), $M", g["predev"]["mid"]["owners_engineer_m"], g["predev"]["critical"]["owners_engineer_m"])
    both_row("**total, first in the capital, $M**", g["predev"]["mid"]["total_m"], g["predev"]["critical"]["total_m"], "{:,.0f}", True)
    both_row("longest gating study, years", g["predev"]["mid"]["gate_years"], g["predev"]["critical"]["gate_years"], "{:.1f}")
    both_row("studies start / field construction starts", f"{PD.START_YEAR:.0f} / {g['predev']['mid']['field_start']:.0f}", f"{PD.START_YEAR:.0f} / {g['predev']['critical']['field_start']:.0f}", "{}")
    a("")
    a(f"**Title II**, per selected coastal site, plus a screening pass over the {PD.CANDIDATE_SITES} candidates of Section 16:")
    a("")
    a("| id | study | what it settles | mid: $M, years | critical: $M, years |")
    a("|---|---|---|---|---|")
    for rm, rc in zip(g["predev2"]["mid"]["rows"], g["predev2"]["critical"]["rows"]):
        a(f"| {rm['id']} | {scrub(rm['name'])} | {scrub(rm['settles'])} | {rm['cost_m']:.1f}, {rm['years']:.1f} | {rc['cost_m']:.1f}, {rc['years']:.1f} |")
    a("")
    a("| Title II | mid | critical |")
    a("|---|---|---|")
    both_row("per selected site, $M", g["predev2"]["mid"]["per_site_m"], g["predev2"]["critical"]["per_site_m"], "{:.1f}")
    both_row("screening of the candidates, $M", g["predev2"]["mid"]["screening_m"], g["predev2"]["critical"]["screening_m"], "{:.1f}")
    both_row(f"per module at {PD.MODULES_PER_SITE[0]:.0f} / {PD.MODULES_PER_SITE[1]:.0f} modules a site, $M", g["predev2"]["mid"]["per_module_m"], g["predev2"]["critical"]["per_module_m"], "{:.1f}")
    both_row("longest study (the coastal permit), years", g["predev2"]["mid"]["gate_years"], g["predev2"]["critical"]["gate_years"], "{:.1f}")
    a("")
    # ---------------------------------------------------------------- 13
    h2(13)
    a("| $/MWh | mid | critical |")
    a("|---|---|---|")
    both_row("Helios-3 as chained", d["mid"]["price"], d["critical"]["price"])
    both_row("with the risk register (Section 9) and the studies (Section 12)", pm["price"], pc["price"])
    both_row("serving the whole load, mirrors route", pm["price"] + m["mid"]["dprice"], pc["price"] + m["critical"]["dprice"])
    both_row("**serving the whole load, both (adopted)**", whole_price(g, "mid"), whole_price(g, "critical"), "{:,.0f}", True)
    both_row("after the bonds retire: O&M only, plant and closing plant", g["postbond"]["mid"], g["postbond"]["critical"])
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
    a(f"costs ${whole_price(g, 'mid'):.0f}, at which a household pays ${money(H.per_household(whole_price(g, 'mid')))}. At critical the plant price is ${pc['price']:.0f} and the whole load")
    a(f"${whole_price(g, 'critical'):.0f}: **${money(H.per_household(whole_price(g, 'critical')))} a household, above today's bill**. The plant pays for itself after the bonds at a price")
    a("above the contract band, and the critical case is the threshold the design is held to. A plant designed to the mid")
    a("case would have no margin; this document does not offer one.")
    a("")
    a("**No further public money after the build.** The bill carries debt service and O&M; the treasury carries nothing once")
    a("the plant runs at capacity. That holds on three conditions: the plant delivers its modelled output; the HOURS rows of")
    a("Section 9 hold, since a mid-life replacement of a major component is new capital and not O&M; and Title II stands on")
    a("its own rate (Section 15).")
    a("")
    a("| per year, Title I | mid | critical |")
    a("|---|---|---|")
    both_row(f"debt service, {H.BOND_TERM_Y}-year bonds at {100 * H.BOND_RATE:.2f} %, $M", g["reserve"]["mid"]["debt_service_m"], g["reserve"]["critical"]["debt_service_m"])
    both_row("O&M, plant with its register, $M", pm["om"], pc["om"])
    both_row("O&M the closing plant adds on the adopted route (Section 8), $M", bm["extra_om_m"], bc["extra_om_m"])
    both_row("share of the plant's bill that is the bonds", g["reserve"]["mid"]["debt_service_m"] / (g["reserve"]["mid"]["debt_service_m"] + pm["om"]), g["reserve"]["critical"]["debt_service_m"] / (g["reserve"]["critical"]["debt_service_m"] + pc["om"]), "{:.0%}")
    a("")
    a(f"**The security behind the rate.** The {100 * H.BOND_RATE:.2f} % is a general-obligation or contracted-revenue rate; the security is contracted")
    a("in-state offtake at the required price with a state general-obligation backstop for the first-of-kind rungs. Priced")
    a("to each security, with the register:")
    a("")
    a("| security | rate | mid, $/MWh ($/household) | critical, $/MWh ($/household) |")
    a("|---|---|---|---|")
    for (name, r, prm, hhm), (_n, _r, prc, hhc) in zip(g["rates"]["mid"], g["rates"]["critical"]):
        a(f"| {name} | {100 * r:.2f} % | {prm:.0f} ({hhm:,.0f}) | {prc:.0f} ({hhc:,.0f}) |")
    a("")
    a(f"**The mechanism behind the tariff.** The household pays the bill above, an output of the balance, through {scrub(T1.MECHANISM)} {cite('sb6x')}.")
    a("A free tariff is a subsidy paid by someone, and this program names no one to pay it.")
    a("")
    a("**Contingency, reserve and the downside.**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("contingency carried on direct cost", g["reserve"]["mid"]["contingency"], g["reserve"]["critical"]["contingency"], "{:.0%}")
    both_row("EPC and owner's cost", g["reserve"]["mid"]["epc"], g["reserve"]["critical"]["epc"], "{:.0%}")
    both_row(f"debt-service reserve, {MJ.DSRF_YEARS:.0f} year, $M", g["reserve"]["mid"]["dsrf_m"], g["reserve"]["critical"]["dsrf_m"])
    both_row(f"price at {H.COVERAGE_REQ:.2f}× coverage (a revenue bond's requirement), $/MWh", g["downside"]["mid"]["price_at_coverage"], g["downside"]["critical"]["price_at_coverage"])
    a("")
    a("The downside case is the critical column throughout.")
    a("")
    a("**The schedule.** Tranche zero is the studies and surveys, from the first study year to the field start; the field")
    a("waits on the longest gating study; each later tranche follows a rung passed at its critical figure. Direct cost by")
    a("rung, with each case's own years:")
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
    a(f"The realistic column is the critical one. The two-year slide comes from one item, the {MJ.NEPA_YEARS[1]:.0f}-year federal environmental")
    a("impact statement on the Mojave node, which is why the studies go first.")
    a("")
    a("**Transmission.** No firm export exists, so no export right is needed. The in-state gen-tie per node at the adopted")
    a(f"sizing peaks at {g['gentie']['mid']['per_node']:,.0f} MW (mid) / {g['gentie']['critical']['per_node']:,.0f} MW (critical) from the hour-by-hour, the same at both cases because the block is")
    a(f"the same size at both and sets the peak, {g['gentie']['mid']['circuits']:.2f} / {g['gentie']['critical']['circuits']:.2f} of one 500 kV circuit (rated {T1.CIRCUIT_500KV_MW[0]:,.0f} / {T1.CIRCUIT_500KV_MW[1]:,.0f} MW), priced in the")
    a(f"switchyard line at ${g['gentie']['mid']['switchyard_m']:,.0f} / {g['gentie']['critical']['switchyard_m']:,.0f} M (Section 6). The interconnection study is the Authority's to file and no")
    a("authority shortens it.")
    a("")
    fig("fig-08-price.png", "Title I's required price step by step, both cases, against the contract band and today's generation charge.")
    fig("fig-09-household.png", "A household's annual generation charge: today, during the bond term on the adopted route, and after the bonds retire.")
    fig("fig-11-schedule.png", "The schedule by tranche at mid and critical; tranche zero is the studies and surveys.")
    # ---------------------------------------------------------------- 14
    h2(14)
    ar, mod = g["aqua_route"], g["aqua"]
    a("**The module.** A 50,000 acre-foot-a-year seawater reverse-osmosis module on a retired coastal power-plant brownfield,")
    a("reusing its intake channel and permitted outfall, state-owned on Title I's form. The unit capital is the built record")
    a(f"escalated to the groundbreaking dollar: Carlsbad at ${g['record']['carlsbad']:,.0f} per AFY (mid) {cite('carlsbad')} and Huntington Beach as designed at")
    a(f"${g['record']['huntington']:,.0f} (critical) {cite('huntington')}.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("overnight, $M", mod["mid"]["overnight_m"], mod["critical"]["overnight_m"])
    both_row("of which site studies and surveys per module (Section 12), $M", mod["mid"]["studies_m"], mod["critical"]["studies_m"], "{:.1f}")
    both_row("financed (contingency, EPC, interest during construction), $M", mod["mid"]["financed_m"], mod["critical"]["financed_m"])
    both_row("electricity, kWh/m³, bought from Title I at its plant price", f"{mod['mid']['kwh_m3']:.1f} at ${mod['mid']['energy_price']:.0f}/MWh", f"{mod['critical']['kwh_m3']:.1f} at ${mod['critical']['energy_price']:.0f}/MWh", "{}")
    a("")
    a("**The water**, at cost recovery: debt service, energy and operations, with no mineral revenue.")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("debt service / energy / non-energy O&M, $M/yr", f"{mod['mid']['debt_m']:.0f} / {mod['mid']['energy_m']:.0f} / {mod['mid']['om_m']:.0f}", f"{mod['critical']['debt_m']:.0f} / {mod['critical']['energy_m']:.0f} / {mod['critical']['om_m']:.0f}", "{}")
    both_row("**$ per acre-foot**", mod["mid"]["per_af"], mod["critical"]["per_af"], "{:,.0f}", True)
    both_row("$ per m³", mod["mid"]["per_m3"], mod["critical"]["per_m3"], "{:.2f}")
    both_row("of which energy", mod["mid"]["energy_m"] / mod["mid"]["total_m"], mod["critical"]["energy_m"] / mod["critical"]["total_m"], "{:.0%}")
    both_row(f"per household per year at {AQ.HOUSEHOLD_AF_YR:.2f} AF", mod["mid"]["household"], mod["critical"]["household"])
    a("")
    a(f"Carlsbad delivers at ${AQ.CARLSBAD_PRICE_AF[0]:,.0f}–{AQ.CARLSBAD_PRICE_AF[1]:,.0f} an acre-foot {cite('carlsbad')} and a district pays about ${AQ.WHOLESALE_TODAY_AF:,.0f} wholesale today.")
    a("Desalinated water is firm water and is priced as such; capital dominates the price, not energy.")
    a("")
    a("**The process decisions.**")
    a("")
    a("- **Reverse osmosis, not thermal distillation.** A coastal brownfield has no heat source of the 500 MW_th a thermal")
    a(f"  module needs; against a condensing cycle on the same heat the water would cost {g['topping']['mid']['cost_kwh_e_m3']:.1f} / {g['topping']['critical']['cost_kwh_e_m3']:.1f} kWh/m³ of electricity")
    a(f"  forgone, {g['topping']['mid']['cost_kwh_e_m3'] / g['topping']['mid']['ro_kwh_e_m3']:.1f}× / {g['topping']['critical']['cost_kwh_e_m3'] / g['topping']['critical']['ro_kwh_e_m3']:.1f}× reverse osmosis. Reverse osmosis at {AQ.RO_KWH_M3[0]:.1f}–{AQ.RO_KWH_M3[1]:.1f} kWh/m³ is what is priced.")
    a(f"- **No zero-liquid-discharge and no mineral train.** Seawater holds {T2.LI_SEAWATER_MG_L} mg/L of lithium: one module's feed contains")
    a(f"  {g['minerals']['mid']['li_t']:.1f} tonnes a year, three orders below any revenue that could carry a plant. Its magnesium as hydroxide would be")
    a(f"  {g['minerals']['mid']['mgoh2_kt']:.0f} kt a year, {g['minerals']['mid']['share_of_market']:.2f} of the US magnesium-compounds market ({g['minerals']['critical']['share_of_market']:.2f} at critical) from one module. Crystallising")
    a("  the brine costs 20–30 kWh per m³ of brine. Neither mineral is a revenue and neither is in the price. Chloride")
    a("  chemistry is excluded from every system on hazard grounds, which rules out magnesium metal.")
    a(f"- **Brine through the outfall at Ocean Plan concentration** {cite('oceanplan')}. At {T2.RECOVERY:.0%} recovery the brine is {g['brine']['brine_ppt']:.0f} ppt, {g['brine']['excess_ppt']:.1f}")
    a(f"  above ambient, against a limit of {T2.OCEAN_PLAN_LIMIT_PPT:.0f} ppt at the {T2.MIXING_ZONE_M:.0f} m edge — a diffuser dilution of {g['brine']['dilution']:.0f} : 1, which a retired plant's")
    a("  outfall must achieve without cooling water.")
    a(f"- **Intake.** A {scrub(T2.INTAKE)}. Slant wells are site-specific and were the failure at Huntington Beach {cite('huntington')}; entrainment is")
    a("  non-zero and mitigated under the Ocean Plan, not eliminated.")
    a(f"- **On-site power covers a tenth, not all.** A module draws {g['onsite']['mid']['need_mw']:.0f}–{g['onsite']['critical']['need_mw']:.0f} MW on average; the {T2.BROWNFIELD_ACRES[0]:.0f} / {T2.BROWNFIELD_ACRES[1]:.0f} acre site's PV makes")
    a(f"  {g['onsite']['mid']['pv_avg_mw']:.1f}–{g['onsite']['critical']['pv_avg_mw']:.1f} MW, {g['onsite']['mid']['share']:.0%}–{g['onsite']['critical']['share']:.0%} of it. Islanding is a battery for the intake, pretreatment and controls ({g['onsite']['mid']['islanding_mw']:.1f} MW), so the plant")
    a("  rides through an outage without fouling; full-load islanding is not claimed.")
    a(f"- **Energy at the contract price, full-time.** Title I's surplus is {g['surplus']['mid']['share']:.0%} of hours; a membrane plant runs steadily. The")
    a("  surplus is the water route's lift, an upside the water price does not count.")
    n = g["noise"]
    a(f"- **{MN.BOUNDARY_DBA:.0f} dBA at the boundary is bought, not assumed.** High-pressure pumps at {n['mid']['source']:.0f}–{n['critical']['source']:.0f} dBA at 1 m reach {MN.BOUNDARY_DBA:.0f} dBA at")
    a(f"  {n['mid']['d_open_m']:,.0f}–{n['critical']['d_open_m']:,.0f} m in the open; a full enclosure of {n['mid']['enclosure']:.0f}–{n['critical']['enclosure']:.0f} dB brings the boundary to {n['mid']['d_enclosed_m']:.0f}–{n['critical']['d_enclosed_m']:.0f} m, inside the brownfield, at")
    a(f"  ${n['mid']['cost_m']:.0f}–{n['critical']['cost_m']:.0f} M a module, carried in the module's band.")
    a(f"- **Employment.** At Carlsbad's staffing per plant {cite('staff')}, the adopted route's modules employ {g['jobs']['mid']['title2_permanent']:,.0f}–{g['jobs']['critical']['title2_permanent']:,.0f} permanently.")
    a("")
    s2 = g["schedule2"]
    a(f"**The schedule.** Carlsbad was proposed in {T2.CARLSBAD_YEARS[0]}, permitted in {T2.CARLSBAD_YEARS[1]} and delivered water in {T2.CARLSBAD_YEARS[2]}, {s2['mid']['carlsbad']} years {cite('carlsbad')};")
    a(f"Huntington Beach ran from {T2.HUNTINGTON_YEARS[0]} to a {T2.HUNTINGTON_YEARS[1]} denial {cite('huntington')}. Stated honestly, permitting of {s2['mid']['permit']:.0f} years (mid) to {s2['critical']['permit']:.0f} (critical,")
    a(f"assumed from the record) and a {s2['mid']['build']:.0f}-year build put first water at **{s2['mid']['first_water']:.0f}–{s2['critical']['first_water']:.0f}** from a {T2.PROGRAM_START} start. Each year of delay")
    a(f"escalates a module by ${s2['mid']['delay_m_per_year']:.0f}–{s2['critical']['delay_m_per_year']:.0f} M.")
    a("")
    a("**Title II's side of the adopted route:**")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row(f"modules at {B.HEAD_M:.0f} m of head (built as whole modules: {ar['mid']['modules']:.0f} / {ar['critical']['modules'] + 0.5:.0f})", ar["mid"]["modules"], ar["critical"]["modules"], "{:.1f}")
    both_row("water, million acre-feet a year", ar["mid"]["maf"], ar["critical"]["maf"], "{:.2f}")
    both_row("modules' capital, financed, $B", ar["mid"]["capex_b"], ar["critical"]["capex_b"], "{:.1f}")
    both_row("lift on the water's bill, kWh/m³", ar["mid"]["lift"], ar["critical"]["lift"], "{:.2f}")
    both_row("water with the lift on its bill, $/acre-foot", ar["mid"]["per_af"], ar["critical"]["per_af"])
    both_row("per household per year", ar["mid"]["household"], ar["critical"]["household"])
    a("")
    # ---------------------------------------------------------------- 15
    h2(15)
    a("**The relation.** One Authority, two projects, two revenue accounts. Title I sells electricity at cost recovery to")
    a("in-state load-serving entities and to Title II; Title II sells water at cost recovery to districts. Neither")
    a("subsidises the other: each carries its own capital, its own debt service and its own price, and the joinder is two")
    a("contracts and one asset. Four standing decisions govern it: one program, two projects, severable; nitrate salt is")
    a("retained only as the fallback and chloride chemistry is excluded everywhere; Noor III-class heliostats; no")
    a("zero-liquid-discharge, brine returned through the existing outfall.")
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
    a("year-round delivery returns through pump-turbines to Title I's evenings. The reservoir and the pump-turbines are")
    a("Title I's, because they close its load; the modules are Title II's, because they make its water; the lift energy is")
    a("the surplus, priced at nothing because it was worth nothing.")
    a("")
    a("**The decision table.** The three routes of Section 8, side by side:")
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
    a(f"and winter recharge, where the San Joaquin Valley's groundwater overdraft is about {R3.SGMA_RECHARGE_GAP_MAF[0]:.1f}–{R3.SGMA_RECHARGE_GAP_MAF[1]:.1f} million acre-feet a year")
    a(f"{cite('ppic')}. That is the match of supply to demand the joinder rests on, and it is a contract question: irrigation and")
    a("recharge districts under contract for firm water at three to five thousand dollars an acre-foot, which is what firm")
    a("water costs.")
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
    # ---------------------------------------------------------------- 16
    h2(16)
    a("None of the site terms can be computed without a site, and this document does not pretend to. The three Title I")
    a("nodes and the retired or retiring coastal plants a Title II module could stand on are each graded on the terms the")
    a("Title needs of a site, from what is on the public record — MET, CONDITIONAL (clears on an assumption the site study")
    a(f"confirms), OPEN (not knowable here), FAIL — and ranked: MET {SI.WEIGHT['MET']:.0f}, CONDITIONAL {SI.WEIGHT['CONDITIONAL']:.1f}, OPEN {SI.WEIGHT['OPEN']:.0f}, FAIL {SI.WEIGHT['FAIL']:.0f}. Every site value")
    a("is assumed from the public record unless computed here, and the note beside each grade says which. **The rank")
    a("orders the site studies; it does not choose a site.**")
    a("")
    a("### 16.1. Title I: the three nodes")
    a("")
    a("The terms a node must meet:")
    a("")
    a("| term | requirement | what settles it |")
    a("|---|---|---|")
    for t, req, settle in SI.T1_TERMS:
        a(f"| {t} | {scrub(req)} | {scrub(settle)} |")
    a("")
    for name, lat, lon, ap, mw, st, dni, status in H.NODES:
        s1m, s1c = g["sites1"]["mid"][name], g["sites1"]["critical"][name]
        (pgm, fm), (pgc, fc) = g["seismic"]["mid"][name], g["seismic"]["critical"][name]
        a(f"#### {name}")
        a("")
        a(f"{lat:.2f}° N, {abs(lon):.2f}° W. Annual direct-normal irradiance **{dni:,.0f} kWh/m²/yr** ({scrub(status)} {cite('nsrdb')}; band {H.DNI_BAND[name][0]:,.0f}–{H.DNI_BAND[name][1]:,.0f}). One third")
        a(f"of the fleet: {d['mid']['aperture'] / 3e6:.1f} / {d['critical']['aperture'] / 3e6:.1f} million m² of mirror at design and {d['mid']['aperture'] * bm['field'] / 3e6:.1f} / {d['critical']['aperture'] * bc['field'] / 3e6:.1f} on the adopted route, {d['mid']['towers'] * bm['field'] / 3:.0f} / {d['critical']['towers'] * bc['field'] / 3:.0f} towers,")
        a(f"{d['mid']['pv_mw'] / 3:,.0f} / {d['critical']['pv_mw'] / 3:,.0f} MW_AC of PV; land {g['land']['mid']['per_node']:,.0f} / {g['land']['critical']['per_node']:,.0f} acres on the adopted route; mirror washing {g['wash']['mid']['afy_per_node']:,.0f} / {g['wash']['critical']['afy_per_node']:,.0f} acre-feet a")
        a(f"year from the program's own water; one 500 kV circuit at {g['gentie']['mid']['per_node']:,.0f} / {g['gentie']['critical']['per_node']:,.0f} MW peak injection. Seismic: the {MN.DESIGN_PGA_G:.2f} g design target over a")
        a(f"mapped MCE_R PGA of {pgm:.2f} / {pgc:.2f} g {cite('asce', 'cgs')} is {fm:.2f}× / {fc:.2f}× (a site study must confirm {SI.SEISMIC_MARGIN:.1f}×).")
        a("")
        a("| term | mid | critical | note |")
        a("|---|---|---|---|")
        for t, _req, _settle in SI.T1_TERMS:
            gm, nm = s1m["rows"][t]
            gc, nc = s1c["rows"][t]
            a(f"| {t} | {gm} | {gc} | {scrub(nm) if nm == nc else scrub(nm) + ' / ' + scrub(nc)} |")
        ftm = SI.first_study(s1m["rows"], SI.T1_TERMS)
        ftc = SI.first_study(s1c["rows"], SI.T1_TERMS)
        a("")
        a(f"Score {s1m['score']:.1f} (mid) / {s1c['score']:.1f} (critical). *First study:* {ftm[0]} — {scrub(ftm[1])}" + ("" if ftm == ftc else f"; at critical {ftc[0]} — {scrub(ftc[1])}") + ".")
        a("")
    rm1, rc1 = SI.ranked(g["sites1"]["mid"]), SI.ranked(g["sites1"]["critical"])
    a("**Ranking.** Mid: " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in rm1) + ". Critical: " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in rc1) + ".")
    a("At mid the Westside ties the Mojave for first: it meets land, nexus and grid outright and is conditional on")
    a("irradiance and head, so the node the record doubts for its sun has the fewest open terms. At critical the Mojave")
    a(f"leads alone, because the Westside's seismic margin falls under the {SI.SEISMIC_MARGIN:.1f}× a site study must confirm. The Central Valley")
    a(f"node's land is the reason it is kept: {g['land']['mid']['westlands']:,.0f} / {g['land']['critical']['westlands']:,.0f} acres of fallowed, drainage-impaired Westside farmland cover a node")
    a(f"{g['land']['mid']['westlands_covers']:.1f}× / {g['land']['critical']['westlands_covers']:.1f}× over. Land across the program on the adopted route is {g['land']['mid']['acres']:,.0f} / {g['land']['critical']['acres']:,.0f} acres ({g['land']['mid']['km2']:.0f} / {g['land']['critical']['km2']:.0f} km²). A")
    a(f"federal environmental review on the Mojave node's federal nexus is budgeted as {MJ.NEPA_YEARS[0]:.0f} / {MJ.NEPA_YEARS[1]:.0f} years of escalation on that node,")
    a(f"${g['nepa']['mid']['delay_m']:,.0f} / {g['nepa']['critical']['delay_m']:,.0f} M.")
    a("")
    a("### 16.2. Title II: the coastal brownfields")
    a("")
    a("The terms a coastal site must meet:")
    a("")
    a("| term | requirement | what settles it |")
    a("|---|---|---|")
    for t, req, settle in SI.T2_TERMS:
        a(f"| {t} | {scrub(req)} | {scrub(settle)} |")
    a("")
    for name, r in SI.ranked(g["sites2"]):
        a(f"#### {name}")
        a("")
        a("| term | grade | note |")
        a("|---|---|---|")
        for t, _req, _settle in SI.T2_TERMS:
            gr, note = r["rows"][t]
            a(f"| {t} | {gr} | {scrub(note)} |")
        ft = SI.first_study(r["rows"], SI.T2_TERMS)
        a("")
        a(f"Score {r['score']:.1f}. *First study:* {ft[0]} — {scrub(ft[1])}.")
        a("")
    for name, why in SI.EXCLUDED.items():
        a(f"**Excluded: {name}.** {scrub(why).replace('the record this work prices from', 'the record the module is priced from')}.")
    a("")
    a("**Ranking.** " + ", ".join(f"{n.split(' (')[0]} {r['score']:.1f}" for n, r in SI.ranked(g["sites2"])) + ". The Oxnard plain")
    a("(Ormond Beach, Mandalay) and Moss Landing meet the taker and head terms the water route needs; Huntington Beach")
    a("carries its 2022 denial as a FAIL and is not a first site; no coastal site is MET on every term, so a site study is")
    a(f"always owed. The adopted route needs {bm['modules']:.0f}–{bc['modules']:.0f} modules and this list holds {len(SI.T2_SITES)} sites: {PD.MODULES_PER_SITE[1]:.0f}–{PD.MODULES_PER_SITE[0]:.0f} modules a site, or sites this")
    a("list does not name. That is a finding, not a plan.")
    a("")
    fig("fig-12-sites.png", "The sites scored: the three Title I nodes on six terms at both cases, and the eight coastal brownfields on seven terms.")
    # ---------------------------------------------------------------- 17
    h2(17)
    a(f"**CO₂ avoided.** From the hour-by-hour at a CAISO marginal factor of {g['co2']['mid']['factor']:.2f} / {g['co2']['critical']['factor']:.2f} t/MWh (the critical case credits")
    a("less, because a cleaner grid displaces less):")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("served as sized, TWh", g["co2"]["mid"]["as_sized_twh"], g["co2"]["critical"]["as_sized_twh"], "{:.2f}")
    both_row("avoided as sized, million t/yr", g["co2"]["mid"]["as_sized_mmt"], g["co2"]["critical"]["as_sized_mmt"], "{:.2f}")
    both_row("avoided with the load closed, million t/yr", g["co2"]["mid"]["closed_mmt"], g["co2"]["critical"]["closed_mmt"], "{:.2f}")
    a("")
    a(f"**Employment.** From built plants per MW {cite('staff')} — Crescent Dunes and Ivanpah for the permanent staff, Ivanpah's peak for")
    a(f"construction — at the adopted route's block of {g['jobs']['mid']['block_mw']:,.0f} MWe and its {bm['modules']:.0f} / {bc['modules']:.0f} water modules:")
    a("")
    a("| | mid | critical |")
    a("|---|---|---|")
    both_row("permanent, Title I", g["jobs"]["mid"]["permanent"], g["jobs"]["critical"]["permanent"])
    both_row("construction peak, Title I", g["jobs"]["mid"]["construction_peak"], g["jobs"]["critical"]["construction_peak"])
    both_row("permanent, Title II's modules", g["jobs"]["mid"]["title2_permanent"], g["jobs"]["critical"]["title2_permanent"])
    a("")
    a(f"**Resource adequacy.** No firm export exists, so no export capacity is sold; the in-state resource adequacy is the")
    a(f"block's net capacity on the adopted route, {g['ra']['mid']['block_net_mw']:,.0f} / {g['ra']['critical']['block_net_mw']:,.0f} MW, self-supplied by the Authority as load-serving entity.")
    a("")
    a(f"**Water for the mirrors.** At Ivanpah's dry-cooled record ({MJ.IVANPAH_WASH_AFY:.0f} acre-feet a year on {MJ.IVANPAH_M2 / 1e6:.1f} million m²) the program's field on")
    a(f"the adopted route needs {g['wash']['mid']['afy']:,.0f} / {g['wash']['critical']['afy']:,.0f} acre-feet a year, from {g['wash']['mid']['source']}.")
    a("")
    a(f"**Seismic.** The basis is ASCE 7 {cite('asce')}, site class and mapped MCE_R. The {MN.DESIGN_PGA_G:.2f} g target clears the mapped PGA at every node")
    a("(Section 16.1); the mapped values are taken from the hazard record and the site study fixes them.")
    a("")
    a("**Nitrate.** No nitrate salt anywhere in Helios-3: the medium is sintered bauxite, with no freezing point, no")
    a("decomposition ceiling, no oxidiser and no toxic medium (R-13 to R-15). The nitrate hazard applies only to the")
    a("salt-block fallback, whose failure mode — the hot-salt tank leak that took Crescent Dunes and Noor III each offline")
    a("for more than a year — is on the record in Section 10.1.")
    a("")
    a("**Procurement.** One EPC contractor per node under an owner's engineer across the program; the pilot aperture and the")
    a("first module let as separate contracts. No contractor has delivered more than one commercial tower at a time in the")
    a("United States, and the ladder buys the hours before the fleet.")
    a("")
    a("**The Authority.** A statutory public entity created by the Act on the pattern of the California Consumer Power and")
    a(f"Conservation Financing Authority of 2001 {cite('sb6x')}, whose defunding by 2004 the Act acknowledges, registered as the")
    a("load-serving entity of Section 13 in the community-choice form. Emergency powers under the Government Code are cited")
    a("only for what they do, which is to suspend regulatory statutes in a declared emergency; they issue no coastal permit")
    a("and shorten no federal review.")
    a("")
    a("**Dry cooling.** Zero water for heat rejection; supercritical CO₂ needs about a sixth of steam's cooling airflow")
    a("(R-16), at a compressor-inlet penalty at 45 °C that the critical cycle band carries.")
    a("")
    # ---------------------------------------------------------------- 18
    h2(18)
    a("- **No plant of this kind has run.** The largest falling-particle receiver is 2 MW_th; the 715 °C recompression cycle")
    a("  has not run. The pilot aperture (Section 11) and the ladder (Section 10) buy the hours before the fleet, and the")
    a("  salt block on the same field is the recorded fallback at a price this document prints.")
    a("- **The plant must deliver its modelled output.** Every dollar of the bill is per MWh; a plant at Crescent Dunes'")
    a("  0.39 of design does not pay its bonds from the bill. The critical column is the defence, and the mid column is margin.")
    a("- **The load and irradiance shapes are reconstructed**, pinned to sourced levels; measured hourly series replace them")
    a("  as they become available, and the evening block factor may move either way.")
    a("- **The coastal permits are the longest studies on the path** and set the critical schedule; a statutory")
    a("  consolidation shortens litigation, not the Coastal Commission.")
    a("- **The head is the site question that sizes Title II**; the reservoir's days of holding move Title I by under a billion.")
    a("- **The takers** are a contract question: irrigation and recharge districts under contract for firm water, year-round.")
    a("- **The split of the shortfall** between the two routes is adopted even and is movable on the ladder of Section 8.")
    a("- **At the critical case a household pays more than today for one bond term**, and this document says so on every page.")
    a("- **The HOURS rows of the register** — receiver, exchanger, turbine, chemistry, scale, provenance — retire only by")
    a("  operating time; a specification cannot make a machine have run.")
    a("- **The brine as a carbonate sink** for the power block's maintenance vents is noted and not priced.")
    a("")
    # ---------------------------------------------------------------- 19
    h2(19)
    a("Every figure in this document is the output of a calculation that can be re-run, never a figure typed into prose.")
    a("The plant is run hour by hour over a year at each node on exact solar geometry; the energy chain, the capital by")
    a("line, the risk register, the closing routes, the water, the sites and the schedule are each computed from published")
    a("constants whose status is marked, and each result is printed at the mid and the critical case. A document's figures")
    a("are drawn from the same computed values as its tables. Where a constant is assumed, the band is stated and the")
    a("adverse end of the band is what the critical case carries; where a measured series is not available, the")
    a("reconstruction is marked and the path to replacing it is named. The pass mark of the pilot, the O&M ratio of the")
    a("closing plant, the reservoir head and its days of holding, the study costs and durations, and the hydro O&M share")
    a("are the assumptions that most move the result, and each is marked where it is used.")
    a("")
    a("## Bibliography")
    a("")
    for i, e in enumerate(bib, 1):
        a(f"{i}. {e}")
    a("")
    return "\n".join(L) + "\n"


# =============================================================================
# THE PITCH
# =============================================================================
def render_pitch(g):
    d, p, bo, m = g["design"], g["priced"], g["both"], g["mirrors"]
    pm, pc = p["mid"], p["critical"]
    bm, bc = bo["mid"], bo["critical"]
    ms = {c: milestones(g, c) for c in CASES}
    L = []
    a = L.append
    a(f"# {TITLE}: the case in brief")
    a("")
    a(f"**{AUTHOR}**")
    a("")
    a("*The accompaniment to the full proposal. Every figure here is the proposal's, labelled mid / critical, and the")
    a("proposal carries its source and its case.*")
    a("")
    a("## The problem")
    a("")
    a("- California's residential load peaks after sunset and in summer, and the grid serves those hours with gas and")
    a(f"  imports at rising prices; a household's generation charge has reached about ${money(g['today_hh'])} a year.")
    a(f"- The San Joaquin Valley's groundwater is overdrafted by {R3.SGMA_RECHARGE_GAP_MAF[0]:.1f}–{R3.SGMA_RECHARGE_GAP_MAF[1]:.1f} million acre-feet a year under a statute that")
    a("  requires the deficit to close; the coast has no new firm water source in service.")
    a("- Neither scarcity yields to demand reduction at scale, and every supply that can meet them is capital-intensive,")
    a("  first-of-a-kind, or both. This program addresses the two together, and prices both honestly.")
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
    a(f"  (sun to socket {C.chain_product(g['base_links'].values()):.3f} for the salt tower, {C.chain_product(d['mid']['links'].values()):.3f} at mid).")
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
    a(f"- A salt-tower plant of this size costs ${g['hc']['low']['net_capex'] / 1e3:.1f}–{g['hc']['high']['net_capex'] / 1e3:.1f} B on the built record and does not pay for itself; this")
    a("  program builds a different plant and prices it from the record, not from a promise.")
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
    a("- The realistic column is critical. The two-year slide is one item, the four-year federal environmental statement on")
    a("  the Mojave node, which is why the studies go first.")
    a("- Only a pass at the pilot orders the first module. A fail records the nitrate-salt plant on the same field as the")
    a("  route, already priced.")
    a("")
    a("## Why it holds up")
    a("")
    a("- Every number comes from a calculation that can be re-run, printed at a middle case and at a critical case where")
    a("  every uncertain constant sits at its adverse end. The design is held to critical; mid is margin.")
    a(f"- The plant is sized to a requirement, three million households growing {g['growth'][0]:.2f}–{g['growth'][1]:.2f}× over the term, and the")
    a("  requirement is met before a kilowatt-hour is sold outside the state.")
    a("- It takes no developer's margin and no state subsidy after the build, and keeps the federal storage credit where")
    a("  statute allows.")
    a(f"- Every technology in it is on a register of {len(ST.STUDIES)} published studies and plants, each with a status and a source, and")
    a("  a recommended further study on a dated ladder.")
    a(f"- It mines nothing new, consumes no cooling water, and avoids {g['co2']['mid']['closed_mmt']:.2f} / {g['co2']['critical']['closed_mmt']:.2f} million tonnes of CO₂ a year with the load closed.")
    a(f"- About {g['jobs']['mid']['construction_peak']:,.0f} construction jobs at peak and {g['jobs']['mid']['permanent']:,.0f} / {g['jobs']['critical']['permanent']:,.0f} permanent on the nodes, plus {g['jobs']['mid']['title2_permanent']:,.0f} / {g['jobs']['critical']['title2_permanent']:,.0f} at the water modules.")
    a("")
    a("## Where")
    a("")
    a("- Title I: the Mojave (Kramer Junction), Imperial (Desert Center) and the Westside. At mid the Westside ties the")
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
    a("  because a plan that hides its worst case is not one that can be built.")
    a("")
    a("## The decision")
    a("")
    a(f"- Fund the studies now, for ${g['predev']['mid']['total_m']:.0f}–{g['predev']['critical']['total_m']:.0f} million, and know within {g['predev']['mid']['gate_years']:.0f}–{g['predev']['critical']['gate_years']:.0f} years whether the rest is worth")
    a(f"  ${program_b(g, 'mid'):.0f}–{program_b(g, 'critical'):.0f} billion.")
    a("- Nothing irreversible is bought before the receiver has passed its test.")
    return "\n".join(L) + "\n"


# =============================================================================
# SELFTEST
# =============================================================================
def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    g = P.gather()
    text, pitch = render(g), render_pitch(g)
    for path, t, name in ((OUT, text, "proposal"), (PITCH, pitch, "pitch")):
        check(f"the {name} exists on disk", os.path.exists(path))
        if os.path.exists(path):
            check(f"the {name} on disk is byte-identical to a fresh render", open(path, encoding="utf-8").read() == t)
    body = text.split("## Bibliography")[0]
    hits = sorted({tok for tok in FORBIDDEN if tok in body or tok in pitch})
    check(f"no workshop token in either document ({', '.join(hits) if hits else 'none found'})", not hits)
    check("no version number in either document", "v0." not in text and "v0." not in pitch)
    check("the author line and the year appear, and no render date", AUTHOR in text and AUTHOR in pitch and "Rendered 20" not in text)
    check("the abstract states the two scarcities", "### Abstract" in text and "fresh water" in text.lower()[:4000] and "electricity" in text[:4000])
    toc = [ln[2:] for ln in text.split("### Contents")[1].split("**How to read")[0].splitlines() if ln.startswith("- ")]
    heads = [ln[3:] for ln in text.splitlines() if ln.startswith("## ")]
    check("the contents list matches the section headings in order", toc == heads)
    check("sections are numbered", all(re.match(r"\d+\. ", h) for h in heads[:-1]) and heads[-1] == "Bibliography")
    bib_n = len([ln for ln in text.split("## Bibliography")[1].splitlines() if re.match(r"\d+\. ", ln)])
    cited = {int(n) for n in re.findall(r"\[(\d+)(?:, \d+)*\]", body)} | {int(n) for grp in re.findall(r"\[([\d, ]+)\]", body) for n in grp.split(",")}
    check(f"every citation resolves to a bibliography entry ({bib_n} entries)", cited and max(cited) <= bib_n)
    check("every bibliography entry is cited at least once", all(n in cited for n in range(1, bib_n + 1)))
    check("the pitch carries no number the proposal does not", P.numbers(pitch) <= P.numbers(text))
    check("the proposal places twelve figures that exist", len(re.findall(r"!\[Figure \d+\]", text)) == 12
          and all(os.path.exists(os.path.join(ROOT, "proposals", r)) for r in re.findall(r"!\[Figure \d+\]\((figures/[^)]+)\)", text)))
    check("every risk row, every study and every site is present", all(f"**{r[0]}. " in text for r in H3.REGISTER)
          and all(scrub(s[1]) in text for s in ST.STUDIES) and all(f"#### {n}" in text for n in SI.T2_SITES))
    check("the program total is Title III's", f"| **program at the adopted route (both), $B** | **{program_b(g, 'mid'):.0f}** | **{program_b(g, 'critical'):.0f}** |" in text)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--docx", action="store_true")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--export-only", action="store_true", help="skip the render; emit .docx / .pdf from the files on disk")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    if a.export_only:
        text, pitch = open(OUT, encoding="utf-8").read(), open(PITCH, encoding="utf-8").read()
    else:
        g = P.gather()
        text, pitch = render(g), render_pitch(g)
        for path, t in ((OUT, text), (PITCH, pitch)):
            with open(path, "w", encoding="utf-8") as f:
                f.write(t)
            print(f"rendered {os.path.relpath(path, ROOT)}: {len(t.splitlines())} lines, {len(t.split()):,} words")
    titles = {OUT: TITLE, PITCH: TITLE + ": the case in brief"}
    for path, t in ((OUT, text), (PITCH, pitch)):
        if a.docx:
            P.emit_docx(t, path[:-3] + ".docx", os.path.dirname(path))
            print(f"emitted {os.path.relpath(path[:-3] + '.docx', ROOT)}")
        if a.pdf:
            P.emit_pdf(t, path[:-3] + ".pdf", os.path.dirname(path), titles[path], author="Matthew Lach")
            print(f"emitted {os.path.relpath(path[:-3] + '.pdf', ROOT)}")
