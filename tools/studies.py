#!/usr/bin/env python3
"""studies.py -- provenance for Helios-3: every technology in the system, the
studies and plants that cover it, the gap to what the design needs, the
further study recommended, and what delay costs.

The author (2026-09-11), on R-12 provenance: "we must provide a complete
list of all studies that cover any technology being used in this system,
and then provide a recommendation of further study, with a note that delay
increases cost of start up at the rate of inflation."

What this file is honest about. The register below is COMPILED from the
published record as known to the session that wrote it; no live database was
queried (NREL, DOE and most journal hosts are blocked at this environment's
egress). Every row names its source so it can be checked, and every row
carries a status from a closed set. "Complete" is therefore a claim about
the TECHNOLOGIES -- the selftest asserts every technology the design uses
has at least one row and one recommendation -- and a FLOOR about the
STUDIES: a technology may have more studies than are listed, never fewer.
A row that turns out wrong is corrected in place with its source, never
silently.

Statuses (closed set):
  OPERATED   a plant or facility that has run at the stated scale
  TESTED     a prototype or loop that has run, below plant scale
  DESIGNED   a published design, TEA or code case; nothing has run
  AUTHOR     the author's own design in this repository; no study exists

Delay. heliocost.py carries ESCALATION (construction-cost index, ASSUMED
band 2-4 %/yr). Each year of delay escalates the overnight cost by that rate
before a dollar is spent, and the required price with it, because the debt
service is proportional to the capex. That is computed here at mid and at
critical, per year, and stated beside the recommendation. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import heliocost as HC                                          # noqa: E402
import helios as H                                              # noqa: E402
import helios3 as H3                                            # noqa: E402

STATUSES = ("OPERATED", "TESTED", "DESIGNED", "AUTHOR")

# (key, technology as the design uses it, what the design needs)
TECHNOLOGIES = [
    ("field", "Heliostat field, Noor III class, surround, night-sized",
     "~27 M m2 critical / 18 M m2 mid across 3 nodes; 14-21 towers"),
    ("receiver", "Falling-particle cavity receiver, multi-aperture",
     "~800 MW_th per tower; 30 MW_th per aperture, 26 apertures"),
    ("aperture", "Compound quartz aperture: hex rod-lens dome with cooled lattice frame",
     "one dome per aperture, hot face at cavity temperature"),
    ("particles", "Sintered bauxite particles as medium and store",
     "hundreds of kt inventory, 600-800 C, forty years"),
    ("storage", "Cold-shell refractory-lined particle silos, replaceable liner",
     "84 GWh_th mid; 800 C hot silo; daily cycling"),
    ("lift", "Cold-side particle lift (skip hoist / bucket elevator)",
     "~150 kg/s per aperture, ambient temperature"),
    ("hx", "Moving packed-bed particle-to-sCO2 heat exchanger",
     "800 C particles against 250 bar CO2, 2,620 MWe fleet"),
    ("sco2", "sCO2 recompression Brayton power block, 715 C / 250 bar, dry-cooled",
     "10-50 MWe units, 2,620 MWe fleet, 45 C ambient"),
    ("alloy", "Inconel 740H / Haynes 282 / Inconel 617 pressure parts",
     "715 C / 250 bar, 100,000 h, CO2 carburisation"),
    ("pv", "PV direct daytime supply with PV-fed electric heaters for winter",
     "2.9 GW_AC PV, 3.5 GW_th heaters"),
    ("cooling", "Dry (air-cooled) heat rejection for sCO2",
     "zero water, 45 C ambient"),
    ("architecture", "Hybrid CSP + PV, thermal block sized for the night",
     "18.1 TWh/yr firm to 3 M households"),
]

# (technology key, study / plant, scale, year, status, what it settled, source)
STUDIES = [
    # --- field ---------------------------------------------------------------
    ("field", "Gemasolar (Torresol), Fuentes de Andalucia", "19.9 MWe, 15 h salt storage", 2011, "OPERATED",
     "first commercial salt tower; 24 h operation demonstrated; CF ~0.73 of design",
     "Torresol Energy; Burgaleta et al., SolarPACES 2011"),
    ("field", "Crescent Dunes (SolarReserve), Nevada", "110 MWe, 10 h salt, 1.2 M m2", 2015, "OPERATED",
     "US utility-scale salt tower; hot-tank leak 2016 cost eight months; CF ~0.39 of design",
     "NREL SolarPACES project database; DOE Loan Programs Office"),
    ("field", "Noor III (ACWA/SENER), Ouarzazate", "150 MWe, 7.5 h salt, 1.3 M m2, 178 m2 heliostats", 2018, "OPERATED",
     "the heliostat class the design carries; receiver outage 2024 reported",
     "SENER; MASEN; SolarPACES project database"),
    ("field", "Cerro Dominador (EIG), Atacama", "110 MWe tower + 100 MWe PV, 17.5 h salt", 2021, "OPERATED",
     "CSP + PV hybrid at one site; $10.45/W built cost", "Cerro Dominador; SolarPACES project database"),
    ("field", "DEWA Phase IV (ACWA/Shanghai Electric), Dubai", "100 MWe tower + 600 MWe trough + 250 MWe PV", 2023, "OPERATED",
     "night-sized thermal block beside daytime PV -- the Helios-2/3 architecture",
     "DEWA; ACWA Power; SolarPACES project database"),
    ("field", "Chinese tower fleet: Shouhang Dunhuang 100 MWe, Supcon Delingha 50 MWe, Luneng Haixi 50 MWe", "50-100 MWe each", 2018, "OPERATED",
     "salt towers at 100 MWe with small heliostats; multiple operators", "CSPPLAZA; SolarPACES project database"),
    ("field", "NREL HelioCon heliostat consortium", "cost and performance roadmap", 2022, "DESIGNED",
     "heliostat cost targets and failure modes; the $80-120/m2 band", "NREL HelioCon (2022-)"),
    ("field", "Ivanpah (BrightSource), California", "392 MWe direct steam, 3 towers", 2014, "OPERATED",
     "California desert siting, permitting, avian and dust record; no storage; contracts ending",
     "NRG/BrightSource; CEC docket 07-AFC-5"),
    # --- receiver ------------------------------------------------------------
    ("receiver", "Sandia NSTTF falling-particle receiver", "1 MW_th, 1 m x 1 m aperture", 2015, "TESTED",
     "on-sun operation to 800 C; efficiency 50-80 % measured; 1-7 kg/s; the fixture in receiver.py",
     "Ho et al., Sandia SAND reports 2015-2019; Solar Energy 2017"),
    ("receiver", "G3P3 Gen3 Particle Pilot Plant, Sandia", ">1 MW_th, 6 h storage, integrated", 2024, "TESTED",
     "receiver + silos + lift + heat exchanger as one system; the lift-cold-fall-hot arrangement",
     "DOE SETO Gen3 CSP; Sandia G3P3 (2018-2025)"),
    ("receiver", "DLR CentRec centrifugal particle receiver, Julich", "~0.5 MW_th", 2017, "TESTED",
     "rotating-drum alternative to a falling curtain; 900 C outlet", "DLR; Ebert et al., SolarPACES 2016-2019"),
    ("receiver", "CSIRO / ASTRI falling-particle receiver, Newcastle", "~0.5 MW_th", 2023, "TESTED",
     "second falling-particle receiver on sun, independent of Sandia", "CSIRO; ASTRI (Australia)"),
    ("receiver", "King Saud University / Sandia multi-stage receiver, Riyadh", "sub-MW", 2018, "TESTED",
     "multi-stage (staggered) curtain to raise residence time", "KSU / Sandia collaboration"),
    ("receiver", "Sandia Gen3 100 MWe particle plant design study", "100 MWe, multi-aperture", 2019, "DESIGNED",
     "the multi-aperture layout and the $/kWe the design carries", "Sandia Gen3 Roadmap / TEA (Ho et al. 2019-2021)"),
    ("receiver", "receiver.py (this repository)", "scaling law, critical case", 2026, "AUTHOR",
     "curtain as a per-metre machine; loss fraction size-invariant; pilot aperture rung", "tools/receiver.py"),
    # --- aperture ------------------------------------------------------------
    ("aperture", "DLR REFOS / SOLGATE pressurised volumetric receivers, PSA", "250-400 kW_th, quartz window", 2003, "TESTED",
     "domed quartz windows on cavity receivers at 800-1000 C air; window cooling and failure modes",
     "Buck et al., J. Solar Energy Eng. 2002; SOLGATE final report 2005"),
    ("aperture", "Sandia windowed falling-particle receiver study", "modelled, 1 MW_th class", 2016, "DESIGNED",
     "+11.9 % efficiency over an aerowindow; quartz half-shell transmissivity 0.97/0.94",
     "Ho / Yellowhair, Sandia SAND (Gen3 windowed receiver)"),
    ("aperture", "Author's compound quartz aperture (helios3.py R-02)", "hex rod-lens dome, cooled lattice", 2026, "AUTHOR",
     "no study exists; receiver.py prices it against the open aperture", "tools/helios3.py R-02; tools/receiver.py"),
    # --- particles -----------------------------------------------------------
    ("particles", "Sandia particle durability and optical studies (CARBO HSP / CP)", "lab + 1 MW_th on-sun", 2014, "TESTED",
     "absorptance 0.946 new, ~0.93 after 200 h on-sun; attrition low for sintered bauxite; oxide transformations on heating in air (R-08)",
     "Siegel et al. 2014; Ho et al. 2016; Sandia SAND reports"),
    ("particles", "CARBO Ceramics proppant production", "industrial, Mt/yr", 2000, "OPERATED",
     "the medium is a commodity with a supply chain", "CARBO Ceramics product data"),
    # --- storage -------------------------------------------------------------
    ("storage", "G3P3 hot and cold particle bins", "6 h at ~1 MW_th, refractory-lined", 2024, "TESTED",
     "800 C particle storage in a lined steel bin", "Sandia G3P3"),
    ("storage", "Sandia / Bridgers & Paxton commercial-scale particle silo design", "100 MWe-class, 6-12 h", 2020, "DESIGNED",
     "cold-shell lined silo design and cost; thermal ratcheting analysis", "Sandia Gen3 storage design reports"),
    ("storage", "Siemens Gamesa ETES rock-bed thermal store, Hamburg", "130 MWh_th, 750 C, electrically charged", 2019, "OPERATED",
     "a hot solid store at scale, charged by resistance heaters -- the winter heater path",
     "Siemens Gamesa ETES pilot (2019-2022)"),
    ("storage", "Hot-blast stoves and cement preheaters (industrial precedent)", "decades, daily cycling, >1,000 C", 1900, "OPERATED",
     "refractory linings cycling daily for decades; replaceable liners as O&M", "steel and cement industry practice"),
    # --- lift ----------------------------------------------------------------
    ("lift", "G3P3 skip hoist / bucket elevator", "~1 MW_th class, cold side", 2024, "TESTED",
     "cold particle lift to receiver top", "Sandia G3P3"),
    ("lift", "Mining skip hoists and bulk-solids bucket elevators", "thousands of t/h, ambient", 1950, "OPERATED",
     "cold abrasive bulk lift is an industry, not a development", "bulk-solids handling practice"),
    # --- hx ------------------------------------------------------------------
    ("hx", "Sandia / Solex / VPE moving packed-bed particle-to-sCO2 exchanger", "~100 kW_th prototype", 2019, "TESTED",
     "tested to ~500 C / 17 MPa against a design point of 800 C / 25 MPa; 4-6x any known particle/sCO2 exchanger",
     "Albrecht & Ho, Sandia; Solex Thermal; VPE (2018-2022)"),
    ("hx", "G3P3 integrated particle-to-sCO2 exchanger", "~1 MW_th", 2024, "TESTED",
     "exchanger in the loop with receiver and storage", "Sandia G3P3"),
    ("hx", "NREL fluidised-bed particle heat exchanger (Ma et al.)", "lab / design", 2017, "DESIGNED",
     "the fluidised-bed alternative; particle-side heat transfer coefficients", "Ma et al., NREL (2014-2020)"),
    # --- sco2 ----------------------------------------------------------------
    ("sco2", "STEP Demo (GTI / SwRI / GE), San Antonio", "10 MWe sCO2 RCBC", 2024, "TESTED",
     "first operation 2024 at ~500 C; 715 C recompression is the next phase; 16 MW turbine under 100 kg",
     "GTI Energy STEP Demo (DOE FE); SwRI"),
    ("sco2", "Sandia sCO2 recompression Brayton test loop", "~1 MWe class", 2012, "TESTED",
     "recompression cycle operated; compressor near the critical point", "Sandia SAND2012-9546 (Wright et al.)"),
    ("sco2", "Echogen EPS100", "8 MWe sCO2 waste-heat", 2014, "TESTED",
     "a commercial sCO2 turbine-generator at MW scale (simple recuperated, ~300 C)", "Echogen Power Systems"),
    ("sco2", "Xi'an Thermal Power Research Institute sCO2 test facility", "5 MWe", 2021, "TESTED",
     "second MW-class sCO2 loop, independent of the US programme", "XTPRI / Huaneng"),
    ("sco2", "SCARABEUS CO2-blend cycle project (EU)", "lab loops + design", 2019, "DESIGNED",
     "CO2 + dopant blends to raise the critical point for hot-ambient dry cooling (R-03 note)", "EU H2020 SCARABEUS (2019-2023)"),
    ("sco2", "NETL / SunShot sCO2 CSP system studies", "design + TEA", 2015, "DESIGNED",
     "sCO2 RCBC at ~50 % for 700 C CSP; the cycle value the chain carries", "DOE SunShot sCO2 (2012-2018); NETL"),
    # --- alloy ---------------------------------------------------------------
    ("alloy", "ASME Code Case 2702, Inconel 740H", "650-825 C pressure parts", 2011, "DESIGNED",
     "the only age-hardened superalloy approved for welded creep-limited pressure parts", "ASME BPVC Code Case 2702 (2011)"),
    ("alloy", "US DOE / EPRI A-USC ComTest programme", "700 C steam components, full scale", 2015, "TESTED",
     "740H headers, piping and valves fabricated and tested for 760 C steam", "DOE/OCDO A-USC (2001-2021); EPRI"),
    ("alloy", "ASME Code Case, Haynes 282", "pressure parts, same class", 2019, "DESIGNED",
     "the second source", "ASME BPVC Code Case (Haynes 282)"),
    ("alloy", "ASME Section III Division 5, Inconel 617", "to 950 C, nuclear high-temperature", 2019, "DESIGNED",
     "the fallback with the deepest temperature margin", "ASME BPVC III-5 (2019 edition, Alloy 617)"),
    ("alloy", "sCO2 corrosion / carburisation testing of Ni alloys", "coupons, 700-750 C, 20-25 MPa, to ~10,000 h", 2016, "TESTED",
     "carburisation slow but present; 100,000 h is extrapolated -- the residual in R-04", "ORNL, NETL, Sandia coupon programmes"),
    # --- pv ------------------------------------------------------------------
    ("pv", "Midelt I (EDF/Masdar/Green of Africa), Morocco", "800 MW CSP + PV hybrid, PV-charged storage", 2024, "DESIGNED",
     "PV-fed electric heating of thermal storage at plant scale -- under construction", "MASEN Noor Midelt I"),
    ("pv", "California utility PV fleet", ">20 GW installed, Mojave single-axis", 2020, "OPERATED",
     "the PV capacity factor band the chain carries", "CEC / EIA installed capacity data"),
    ("pv", "Electric resistance heaters for high-temperature stores", "MW-class, 750 C (ETES); salt heaters commercial", 2019, "OPERATED",
     "resistance heating of a hot solid store at MW scale", "Siemens Gamesa ETES; Kraftblock; Malta (design)"),
    # --- cooling -------------------------------------------------------------
    ("cooling", "Air-cooled condensers at CSP plants (Ivanpah, Cerro Dominador, Noor III)", "100-400 MWe", 2014, "OPERATED",
     "dry cooling in desert CSP is standard", "plant records"),
    ("cooling", "sCO2 dry-cooling studies (Sandia / NREL)", "design", 2016, "DESIGNED",
     "sCO2 needs ~1/6 the cooling airflow of steam; hot-ambient compressor-inlet penalty", "Sandia / NREL sCO2 CSP studies"),
    # --- architecture --------------------------------------------------------
    ("architecture", "DEWA Phase IV hybrid", "CSP night + PV day, one site", 2023, "OPERATED",
     "the architecture at 950 MW total", "DEWA / ACWA Power"),
    ("architecture", "Cerro Dominador hybrid", "110 MWe tower + 100 MWe PV", 2021, "OPERATED",
     "CSP + PV hybrid dispatch record", "Cerro Dominador"),
    ("architecture", "cspchain.py / helios.py (this repository)", "hourly model, mid and critical", 2026, "AUTHOR",
     "night-sized field; PV direct; winter heaters; the critical case", "tools/cspchain.py; tools/helios.py"),
]

# (technology key, further study recommended, what it settles, duration years, rung)
RECOMMEND = [
    ("field", "Field commissioning at the first node with measured annual optical efficiency against the 0.58-0.64 band",
     "the largest chain link after the receiver; sets the mirror count at critical", 1.0, "field"),
    ("receiver", "A ~30 MW_th pilot aperture on one fleet tower: curtain fed uniformly across 30 m (critical) / 10 m (nominal); efficiency, edge loss vs aperture size, wind",
     "receiver.py's threshold: 0.795 critical open; whether the edge losses fall as perimeter/area", 2.0, "pilot"),
    ("aperture", "The compound quartz aperture on the pilot: one dome, open aperture beside it, both measured on one tower",
     "whether the dome pays on the measured record as receiver.py says, or loses as the model says", 1.0, "pilot"),
    ("particles", "Long-duration particle ageing on the pilot: absorptance, attrition and oxide state sampled quarterly",
     "R-08's rate over decades, the UNMOVED row; R-01's makeup rate", 3.0, "pilot"),
    ("storage", "One full-size cold-shell silo on the pilot, cycled daily, liner inspected annually",
     "thermal ratcheting and liner life as O&M", 3.0, "pilot"),
    ("lift", "None beyond the pilot's own lift: cold abrasive lift is an industry",
     "nothing open", 0.0, "pilot"),
    ("hx", "A particle-to-sCO2 exchanger module at its design point, 800 C / 25 MPa, on the pilot",
     "R-03: the 4-6x scale-up and the design-point pressure-temperature pair", 2.0, "pilot"),
    ("sco2", "STEP's 715 C recompression phase, then one 10-50 MWe unit on the first module",
     "R-04: turbine, seals and bearings at 715 C; carburisation on the real loop", 3.0, "module"),
    ("alloy", "Coupon and component exposure in the pilot's CO2 loop to the longest hours the schedule allows",
     "R-04/R-06 residual: carburisation at 100,000 h, by extrapolation from the longest real exposure", 3.0, "pilot"),
    ("pv", "None: Midelt I and the Californian PV fleet answer it; heaters at MW scale exist",
     "nothing open beyond winter dispatch, which helios.py's hourly run measures", 0.0, "field"),
    ("cooling", "Compressor-inlet performance at 45 C on the first module's dry cooler",
     "the cycle's 0.45-0.50 critical band; whether a CO2 blend is needed (R-03 note)", 1.0, "module"),
    ("architecture", "Run Helios-3 hour by hour in helios.py at both cases (cspchain's stated next step)",
     "winter under-supply (F-06) and the heater sizing at critical", 0.5, "now"),
]

RUNGS = ("now", "field", "pilot", "module", "fleet")


def by_tech(key):
    return [s for s in STUDIES if s[0] == key]


def delay_cost_per_year(case):
    """What one year of delay adds to the overnight cost and to the price."""
    p = H3.priced(case)
    capex = p["capex_net"]
    return dict(capex_m=capex, delta_capex_m=capex * HC.ESCALATION,
                price=p["price"], delta_price=p["price"] * HC.ESCALATION,
                hh=H.per_household(p["price"]), delta_hh=H.per_household(p["price"]) * HC.ESCALATION)


def critical_path_years():
    """Longest chain of recommended studies by rung, studies within a rung in parallel."""
    total = 0.0
    for rung in RUNGS:
        total += max([r[3] for r in RECOMMEND if r[4] == rung] or [0.0])
    return total


def report(recommend_only=False):
    print()
    print("  HELIOS-3 PROVENANCE: EVERY TECHNOLOGY, EVERY STUDY THAT COVERS IT")
    print("  ==================================================================")
    print("    The author's requirement on R-12: a complete list of the studies")
    print("    covering every technology in the system, a recommendation of")
    print("    further study, and the cost of delay. The list is complete over")
    print("    TECHNOLOGIES (the selftest asserts it) and a FLOOR over STUDIES:")
    print("    compiled from the published record, not queried live, every row")
    print("    with its source so it can be checked.")
    if not recommend_only:
        counts = {s: 0 for s in STATUSES}
        for s in STUDIES:
            counts[s[4]] += 1
        print()
        print(f"    {len(STUDIES)} rows over {len(TECHNOLOGIES)} technologies: "
              + ", ".join(f"{v} {k}" for k, v in counts.items()))
        for key, tech, need in TECHNOLOGIES:
            rows = by_tech(key)
            best = max((STATUSES.index(r[4]) for r in rows if r[4] != "AUTHOR"), default=None)
            print()
            print(f"    {tech}")
            print(f"      needs: {need}")
            for _k, study, scale, year, status, settled, source in rows:
                print(f"      {status:<9} {year}  {study}")
                print(f"                      {scale}")
                print(f"                      settled: {settled}")
                print(f"                      source: {source}")
    print()
    print("    FURTHER STUDY RECOMMENDED, by rung of the R-12 ladder")
    print("    (now -> field -> pilot aperture -> first module -> fleet):")
    for rung in RUNGS:
        rows = [r for r in RECOMMEND if r[4] == rung]
        if not rows:
            continue
        print(f"      {rung.upper()}  (longest study {max(r[3] for r in rows):.1f} y; studies within a rung run in parallel)")
        for key, what, settles, years, _r in rows:
            tech = next(t[1] for t in TECHNOLOGIES if t[0] == key)
            print(f"        {tech.split(',')[0]:<52} {years:4.1f} y")
            print(f"          study:   {what}")
            print(f"          settles: {settles}")
    print(f"      Critical path through the rungs: {critical_path_years():.1f} years of study, run")
    print("      against the build rather than before it: the field is built while the")
    print("      pilot runs, the pilot runs while the module is ordered.")
    print()
    print("    THE COST OF DELAY. heliocost.py escalates construction cost at")
    print(f"    {100 * HC.ESCALATION:.0f} %/yr (ASSUMED band 2-4 %, a construction-cost index, i.e. the")
    print("    rate of inflation for what this plant is made of). Each year the")
    print("    start is delayed adds, before a dollar is spent:")
    print(f"      {'':<14}{'capex net $B':>14}{'+ per year $B':>15}{'$/MWh':>8}{'+ per year':>12}{'$/hh/yr':>10}{'+ per year':>12}")
    for case in ("mid", "critical"):
        c = delay_cost_per_year(case)
        print(f"      {case:<14}{c['capex_m'] / 1e3:14.1f}{c['delta_capex_m'] / 1e3:15.2f}{c['price']:8.0f}{c['delta_price']:12.1f}{c['hh']:10,.0f}{c['delta_hh']:12.0f}")
    print("    A study that takes a year and is not run against the build costs")
    print("    that year's escalation on the whole plant; a study run beside the")
    print("    build costs only itself. That is why the rungs overlap. The")
    print("    escalation rate is ASSUMED and the delay cost is exactly as")
    print("    uncertain as it is.")
    print()
    print("    WHAT THIS DOES NOT DO. It does not make any of it have run. R-12")
    print("    stays MAJOR / HOURS in helios3.py; what this file adds is the list")
    print("    the author asked for and the order in which the hours are bought.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    keys = [t[0] for t in TECHNOLOGIES]
    check("every technology has at least one study row", all(by_tech(k) for k in keys))
    check("every technology has exactly one recommendation",
          all(sum(1 for r in RECOMMEND if r[0] == k) == 1 for k in keys))
    check("every study row names a technology the design uses", all(s[0] in keys for s in STUDIES))
    check("every study row carries a status from the closed set", all(s[4] in STATUSES for s in STUDIES))
    check("every study row names a source", all(s[6].strip() for s in STUDIES))
    check("every study row names what it settled", all(s[5].strip() for s in STUDIES))
    check("every AUTHOR row points at a file in this repository",
          all("tools/" in s[6] for s in STUDIES if s[4] == "AUTHOR"))
    check("every AUTHOR-row file exists",
          all(os.path.exists(os.path.join(HERE, "..", f.strip().split()[0]))
              for s in STUDIES if s[4] == "AUTHOR" for f in s[6].split(";")))
    check("no technology rests on AUTHOR rows alone (an author design is not provenance)",
          all(any(r[4] != "AUTHOR" for r in by_tech(k)) for k in keys))
    hours = ("receiver", "hx", "sco2", "aperture")
    check("the HOURS technologies have no OPERATED row at plant scale (the honest gap)",
          all(not any(r[4] == "OPERATED" for r in by_tech(k)) for k in hours))
    check("every recommendation sits on a rung of the ladder", all(r[4] in RUNGS for r in RECOMMEND))
    check("the receiver recommendation is the pilot aperture receiver.py named",
          "pilot aperture" in next(r[1] for r in RECOMMEND if r[0] == "receiver"))
    check("critical path is years, not decades, and positive", 0.0 < critical_path_years() < 10.0)
    for case in ("mid", "critical"):
        c = delay_cost_per_year(case)
        check(f"{case}: delay cost per year is exactly capex x ESCALATION",
              abs(c["delta_capex_m"] - c["capex_m"] * HC.ESCALATION) < 1e-9)
        check(f"{case}: price drifts at the same rate as capex (debt service is proportional)",
              abs(c["delta_price"] / c["price"] - HC.ESCALATION) < 1e-12)
    check("critical delay cost exceeds mid delay cost",
          delay_cost_per_year("critical")["delta_capex_m"] > delay_cost_per_year("mid")["delta_capex_m"])
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report calls the study list a FLOOR and says it was not queried live",
          "FLOOR over STUDIES" in out and "not queried live" in out)
    check("the report states the cost of delay at both cases", "THE COST OF DELAY" in out and "critical" in out)
    check("the report says it does not make anything have run", "does not make any of it have run" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--recommend", action="store_true", help="recommendations and delay cost only")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report(recommend_only=a.recommend)
