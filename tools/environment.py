#!/usr/bin/env python3
"""What the station does to its surroundings, assessed and mitigated.

Every impact this design has that a reader would want assessed: what it is,
how big, who receives it, how long it lasts, whether it is reversible, and
what is done about it. Nothing is asserted as safe. Each row is graded and
each grade carries a mitigation, and where a mitigation has not been
demonstrated the row says so.

WHAT THIS PROGRAM REFUSES TO DO. It never restates a quantity: the
inventories, the burnup, the beam power and the module count are IMPORTED
from materials.py and powersource.py. And it refuses to compute a DOSE. A
dose needs site meteorology, a stack height, a population distribution and a
pathway model, none of which exist for a station with no site. Every
radiological row is therefore a SOURCE TERM and a REQUIREMENT on the release
that a site licence would test -- never a reassurance about a consequence.

GRADES, and they carry a sign, because two of these impacts run the other way:

    BENEFIT     the station reduces an existing burden
    NEGLIGIBLE  below the threshold at which the receptor could detect it
    MINOR       real, bounded, and handled by ordinary practice
    MODERATE    needs a designed system whose failure would matter
    MAJOR       needs a designed system, a monitoring case and a licence
    DOMINANT    the impact that decides whether the station is permitted

and a mitigation carries a status of its own:

    PRACTICE    routine in an existing industry, at this scale
    DESIGNED    in this design, and buildable from what exists
    REQUIREMENT stated as a target; the means are not demonstrated here

Run:  python3 tools/environment.py                the impact register
      python3 tools/environment.py --radiological the source terms
      python3 tools/environment.py --waste        what leaves, and for how long
      python3 tools/environment.py --conventional chemical, thermal, water, land
      python3 tools/environment.py --benefit      the two that run the other way
      python3 tools/environment.py --proliferation the one that is not
                                                  environmental but belongs here
      python3 tools/environment.py --mitigation   the plan, consolidated
      python3 tools/environment.py --selftest
"""

import argparse
import contextlib
import functools
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


@functools.lru_cache(maxsize=None)
def _mods():
    import collector
    import machine
    import materials
    import powersource
    return powersource, machine, collector, materials


def _w(text, indent=6, width=76):
    pad = " " * indent
    line = pad
    for word in text.split():
        if len(line) + len(word) + 1 > width and line.strip():
            print(line.rstrip())
            line = pad
        line += word + " "
    if line.strip():
        print(line.rstrip())


def _h(title):
    print()
    print("  " + title)
    print("  " + "=" * len(title))
    print()


# ---- quantities, all imported ----------------------------------------------
HOURS_PER_YEAR = 8766.0
CP_WATER = 4186.0            # J/kg/K
LATENT_WATER = 2.26e6        # J/kg
COOLING_RISE_K = 10.0        # ASSUMED: a permit-typical once-through limit
# construction emission factors, SOURCED bands, tonnes CO2 per tonne
CO2_PER_T_STEEL = 1.85
CO2_PER_T_CONCRETE = 0.11
CO2_PER_T_COPPER = 4.0
# a like-for-like comparison, SOURCED order-of-magnitude, g CO2 per kWh
LIFECYCLE_G_PER_KWH = {"coal": 820.0, "gas": 490.0, "solar PV": 48.0,
                       "nuclear, PWR": 12.0, "wind": 11.0}
PWR_SPENT_FUEL_T_PER_GWE_YR = 25.0     # SOURCED order: discharged heavy metal


def st():
    _P, _M, _C, X = _mods()
    return X.ref()


def electricity_twh_per_year():
    return st()["net_mw"] * HOURS_PER_YEAR / 1e6


def waste_heat_mw():
    r = st()
    return r["thermal_mw"] - r["net_mw"]


def cooling_once_through_m3_s(rise_k=COOLING_RISE_K):
    return waste_heat_mw() * 1e6 / (CP_WATER * rise_k) / 1000.0


def cooling_evaporative_t_per_day():
    return waste_heat_mw() * 1e6 / LATENT_WATER * 86.4


def tritium_station_mci():
    _P, _M, C, X = _mods()
    return (st()["modules"]
            * C.tritium_curies(X.tritium_holding_kg() * 1000.0) / 1e6)


def mercury_station_t():
    _P, _M, _C, X = _mods()
    return st()["modules"] * X.mercury_inventory_kg() / 1000.0


def lead_station_t():
    _P, _M, _C, X = _mods()
    return X.breeder_mass_kg() * (1.0 - X.PBLI_LI_MASS_FRAC) / 1000.0


def activated_mass_t():
    """Everything inside the shielding that becomes waste at decommissioning."""
    _P, _M, _C, X = _mods()
    r = st()
    return (r["modules"] * (X.solenoid_cold_mass_kg()
                            + X.shield_mass_kg()) / 1000.0
            + X.salt_inventory_kg() / 1000.0
            + X.breeder_mass_kg() / 1000.0)


def construction_co2_t():
    """From the bill's own masses. Construction only -- operation emits none."""
    _P, _M, _C, X = _mods()
    r = st()
    steel = (r["modules"] * X.solenoid_cold_mass_kg() / 1000.0
             + r["linacs"] * X.linac_length_m() * 2.0)
    concrete = r["modules"] * X.shield_mass_kg() / 1000.0
    return steel * CO2_PER_T_STEEL + concrete * CO2_PER_T_CONCRETE


def construction_g_per_kwh(life_y=None):
    _P, _M, _C, X = _mods()
    years = X.PLANT_LIFE_Y if life_y is None else life_y
    kwh = electricity_twh_per_year() * 1e9 * years
    return construction_co2_t() * 1e6 / kwh


def spent_fuel_avoided_t_per_year():
    """A PWR of the same output discharges this much heavy metal; the station
    discharges FISSION PRODUCTS only, because the actinides stay in the salt
    and are burnt. The difference is the waste-mass saving."""
    _P, _M, _C, X = _mods()
    return (PWR_SPENT_FUEL_T_PER_GWE_YR * st()["net_mw"] / 1000.0
            - X.burnup_kg_per_year() / 1000.0)


def du_liability_removed_t_per_year():
    _P, _M, _C, X = _mods()
    return X.uranium_feed_t_per_year()


def land_linac_km():
    _P, _M, _C, X = _mods()
    return st()["linacs"] * X.linac_length_m() / 1000.0


# ---- THE REGISTER ----------------------------------------------------------
# (domain, impact, quantity, unit, grade, receptor, duration,
#  mitigation, mitigation status)
def register():
    P, M, C, X = _mods()
    r = st()
    rows = []
    A = rows.append

    # --- radiological, routine
    A(("radiological", "tritium inventory, whole station",
       tritium_station_mci(), "MCi", "DOMINANT", "public, via HTO in water",
       "12.32 y half-life",
       "The inventory is not the release and the design attacks the "
       "inventory first: the cell is the smallest the physics allows, its "
       "size is set by the muon range and not by the power, and the station "
       f"holds it as {r['modules']:.0f} separate cells of "
       f"{X.tritium_holding_kg():.2f} kg rather than one. Then double-walled "
       "all-metal containment, secondary at sub-atmospheric pressure, a "
       "getter bed on every sweep, and hydride-bed storage that holds "
       "tritium as a SOLID at atmospheric pressure. A REQUIREMENT on annual "
       "release, tested by a site licence, is what governs -- not this "
       "inventory figure.", "DESIGNED"))
    A(("radiological", "tritium routine release", 0.0, "-", "MAJOR",
       "public", "continuous",
       "NOT COMPUTED HERE and it must not be guessed: a dose needs site "
       "meteorology, stack height, population and a pathway model, and the "
       "station has no site. What is stated is the REQUIREMENT -- the annual "
       "release must meet the site's dose constraint, and the ITER-class "
       "target of order grams a year is the benchmark a design of this "
       "inventory is held to.", "REQUIREMENT"))
    A(("radiological", "activated mercury, Hg-203 and Au-198",
       mercury_station_t(), "t", "MODERATE", "workers", "months to years",
       f"{r['modules']:.0f} sealed loops, each a hot cell rather than a "
       "chemical hazard with a radiological footnote. The loop is never "
       "opened after first beam; maintenance is remote and the whole loop is "
       "a replaceable cartridge.", "DESIGNED"))
    A(("radiological", "noble gases from salt processing", 0.0, "-",
       "MODERATE", "public", "hours to days",
       "Kr and Xe are sparged from the salt continuously -- that sparging is "
       "what buys the forty-year neutron budget, so it is not optional. "
       "Delay beds sized to let the short-lived decay before stack release; "
       "Kr-85 at 10.8 y is the one that must be captured rather than "
       "delayed.", "PRACTICE"))
    A(("radiological", "direct radiation and skyshine", r["beam_mw"], "MW",
       "MODERATE", "public and workers", "while the beam runs",
       "The coil shield is sized for an INSULATION dose limit and is not a "
       "biological shield; the biological shield is separate, larger, and "
       "sized by a shielding calculation this work does not do. Stated as a "
       "requirement in buildpackage.py's bill, not as a solved item.",
       "REQUIREMENT"))

    # --- radiological, accident
    A(("accident", "fuel cell breach", X.tritium_holding_kg(), "kg",
       "MAJOR", "public", "the release, then 12.32 y",
       "ONE MODULE'S cell is the bounding release and that is why the "
       "station is modular in the first place -- twenty cells of "
       f"{X.tritium_holding_kg():.2f} kg cannot fail as one of "
       f"{r['tritium_total_kg']:.1f} kg. Each cell sits inside its own "
       "secondary containment at sub-atmospheric pressure with an isolation "
       "pair on both boundaries, so a breach vents inward.", "DESIGNED"))
    A(("accident", "criticality", 0.0, "-", "NEGLIGIBLE", "public", "-",
       "THERE IS NO CRITICALITY ACCIDENT TO MITIGATE. The blanket is "
       f"subcritical by {P.subcritical_margin(P.K_SAFE)[1]:,.0f} pcm -- a "
       "whole fast core's control worth -- so cutting the beam stops it, and "
       "the freeze-plug drain says the same thing a second time without "
       "power or a signal. This is the one place where this design is "
       "categorically safer than a reactor rather than incrementally.",
       "DESIGNED"))
    A(("accident", "fuel salt spill", X.salt_inventory_kg() / 1000.0, "t",
       "MAJOR", "workers, site", "long",
       "Freeze-plug drain to a passively cooled subcritical tank, below the "
       "vessel, needing no power and no operator. The salt is molten and "
       "hot, so a spill is a thermal and chemical event as well as a "
       "radiological one; the vault is lined and bunded for the whole "
       "inventory.", "DESIGNED"))
    A(("accident", "beam trip thermal cycling", 0.0, "-", "MODERATE",
       "plant, not public", "over the life",
       "A high-power linac trips often. How many cycles the intermediate "
       "loop tolerates is NOT COMPUTED in this work and is carried as an "
       "open item in buildpackage.py's envelope; it is a plant-life question "
       "rather than a release question.", "REQUIREMENT"))

    # --- waste
    A(("waste", "fission products", X.burnup_kg_per_year(), "kg/yr",
       "MODERATE", "repository", "300 y for the bulk",
       "The mass is the same per unit of energy as any fission plant's, "
       "because it is the same fission. What differs is that the ACTINIDES "
       "do not leave with it: online processing removes fission products "
       "from the salt and leaves the actinides in, where they are burnt. So "
       "the long-lived fraction that drives repository design is "
       "consumed rather than buried.", "DESIGNED"))
    A(("waste", "spent heavy metal, avoided",
       spent_fuel_avoided_t_per_year(), "t/yr", "BENEFIT", "repository",
       "over the life",
       f"A PWR of the same output discharges about "
       f"{PWR_SPENT_FUEL_T_PER_GWE_YR:.0f} t of heavy metal per GWe-year, "
       "nearly all of it unburnt uranium. This station discharges fission "
       "products only. The difference is not a mitigation -- it is the "
       "design being a different kind of thing.", "DESIGNED"))
    A(("waste", "activated structure at decommissioning",
       activated_mass_t(), "t", "MODERATE", "repository, site",
       "decades to centuries",
       "Solenoids, shielding, salt and breeder. Steel activation is "
       "dominated by Co-60 at 5.27 y and Nb-94 at 20,000 y, so LOW-COBALT "
       "AND LOW-NIOBIUM STEEL IS SPECIFIED FOR EVERYTHING INSIDE THE SHIELD "
       "-- a material choice made at procurement decides the waste class "
       "forty years later, and it cannot be made afterwards.", "PRACTICE"))
    A(("waste", "beryllium windows", r["modules"] * 0.5, "kg/yr",
       "MINOR", "workers, repository", "long",
       "One per module per year, activated and a chemical toxin both. "
       "Glovebox handling, and the spent window is waste rather than "
       "recycled.", "PRACTICE"))

    # --- conventional
    A(("conventional", "mercury inventory", mercury_station_t(), "t",
       "MODERATE", "workers, site", "permanent if released",
       "Mercury is a persistent bioaccumulative toxin and 51 t of it is a "
       "large holding by any standard. Sealed loops, double containment, "
       "vapour capture on every penetration, and full inventory "
       "accountancy -- the same accountancy the radiological case needs "
       "anyway, which is why it costs nothing extra.", "DESIGNED"))
    A(("conventional", "lead in the breeder", lead_station_t(), "t",
       "MINOR", "workers, site", "permanent if released",
       "Pb-Li is molten and reactive with water. It is a closed loop in a "
       "bunded vault; the hazard is conventional and the practice is the "
       "fusion programme's own.", "PRACTICE"))
    A(("conventional", "waste heat", waste_heat_mw(), "MW", "MODERATE",
       "receiving water or air", "while running",
       f"{cooling_once_through_m3_s():.1f} m3/s at a {COOLING_RISE_K:.0f} K "
       f"rise once-through, or {cooling_evaporative_t_per_day():,.0f} t/day "
       "evaporated in towers. This is an ordinary thermal-plant impact at "
       "an ordinary thermal-plant size and it is the LARGEST PHYSICAL "
       "INTERACTION THE STATION HAS WITH ITS SURROUNDINGS. Dry cooling "
       "removes the water impact and costs efficiency; the choice is the "
       "site's.", "PRACTICE"))
    A(("conventional", "cooling water", cooling_once_through_m3_s(), "m3/s",
       "MODERATE", "receiving water", "while running",
       "Entrainment and thermal plume, both regulated and both routine. "
       "Note this scales with the WASTE heat, so it falls with any gain in "
       "thermal efficiency and the station's own eta_th is a conservative "
       "0.45 of a Carnot bound at the blanket temperature.", "PRACTICE"))
    A(("conventional", "linac tunnel", land_linac_km(), "km", "MINOR",
       "site", "permanent",
       f"{r['linacs']:.0f} linacs of {X.linac_length_m():.0f} m, "
       f"{r['modules']:.0f} target-and-channel assemblies of order 40 m "
       "each, one blanket vault, and a conventional turbine hall. Large for "
       "a power station and small for the energy: no mine, no fuel "
       "fabrication plant, no enrichment plant, no ash pond, no reservoir.",
       "PRACTICE"))

    # --- lifecycle
    A(("lifecycle", "construction CO2", construction_co2_t(), "t",
       "MINOR", "atmosphere", "one-off",
       f"{construction_g_per_kwh():.3f} g/kWh over the life, from the bill's "
       "own steel and concrete. OPERATION EMITS NONE. The figure counts "
       "structural mass only and is a floor, not a life-cycle assessment.",
       "DESIGNED"))
    A(("lifecycle", "front-end mining and milling", 0.0, "t/yr",
       "BENEFIT", "mine sites", "-",
       "ZERO, and this is the largest environmental result in the design. "
       "The fuel is enrichment TAILS, already mined and already stored as a "
       "liability. No ore is moved, no mill tailings are made, no "
       "enrichment is run. Most of nuclear power's material footprint is in "
       "the front end and this station does not have one.", "DESIGNED"))
    A(("lifecycle", "depleted uranium liability removed",
       du_liability_removed_t_per_year(), "t/yr", "BENEFIT",
       "existing storage sites", "over the life",
       f"Every tonne burnt is a tonne of stored UF6 removed. The world's "
       "tails are a liability someone is paying to keep; this is the only "
       "technology that turns the whole of it into energy rather than a "
       "small fraction.", "DESIGNED"))

    # --- the one that is not environmental
    A(("proliferation", "plutonium bred in a processed liquid fuel",
       X.burnup_kg_per_year(), "kg/yr fissioned", "MAJOR",
       "the non-proliferation regime", "permanent",
       "STATED PLAINLY BECAUSE IT IS THE OBJECTION THAT MATTERS: a fast "
       "blanket breeding Pu-239 in a liquid fuel with an online chemical "
       "plant attached is, on its face, the worst proliferation geometry in "
       "civil power. Three things answer it and none of them is "
       "reassurance. The processing removes FISSION PRODUCTS and returns "
       "ACTINIDES -- there is no separated-plutonium stream anywhere in the "
       "flowsheet, by design, and a flowsheet that produced one would be a "
       "different plant. The salt is intensely radioactive at all times, so "
       "diversion is not a chemistry problem but a hot-cell problem. And "
       "the inventory is measurable continuously because the fuel is a "
       "fluid, which makes material accountancy easier here than in any "
       "solid-fuel reactor. The first fissile charge remains a safeguarded "
       "acquisition and a political question, exactly as buildpackage.py "
       "says.", "REQUIREMENT"))
    return rows


GRADES = ("BENEFIT", "NEGLIGIBLE", "MINOR", "MODERATE", "MAJOR", "DOMINANT")
MIT_STATUS = ("PRACTICE", "DESIGNED", "REQUIREMENT")


def report():
    """The impact register: everything, graded."""
    r = st()
    print("  ENVIRONMENTAL IMPACT REGISTER -- THE STATION")
    print()
    _w(f"{r['modules']:.0f} modules, {r['beam_mw']:.0f} MW of beam, "
       f"{r['thermal_mw']:.0f} MW thermal, {r['net_mw']:.0f} MW net "
       f"electric, {electricity_twh_per_year():.2f} TWh a year.", indent=4)
    print()
    _w("No dose is computed anywhere in this file. A dose needs a site and "
       "there is no site; every radiological row is a SOURCE TERM and a "
       "requirement on release, which is what a licence tests.", indent=4)
    print()
    print(f"    {'domain':<15} {'impact':<38} {'quantity':>12} {'':<6}"
          f" {'grade':<11} mitigation")
    last = None
    for dom, imp, q, u, grade, _rec, _dur, _mit, mstat in register():
        if dom != last:
            print()
            last = dom
        qs = "--" if u == "-" else f"{q:12,.2f}"
        print(f"    {dom:<15} {imp:<38} {qs} {u:<6} {grade:<11} {mstat}")
    print()
    counts = {}
    for _d, _i, _q, _u, g, *_ in register():
        counts[g] = counts.get(g, 0) + 1
    print("    " + "  ".join(f"{g} {counts.get(g, 0)}" for g in GRADES))
    print()
    _w("THE SHAPE OF IT. One DOMINANT row and it is tritium inventory, "
       "which is set by the muon range and not by the power -- so it is the "
       "price of the fusion channel and of nothing else. Three BENEFIT "
       "rows, two of which come from the same fact: the fuel is already "
       "mined. And one NEGLIGIBLE row that is worth more than the rest, "
       "because criticality is not a risk this design manages, it is one it "
       "does not have.", indent=4)


def _section(domains, title, tail=None):
    print(f"  {title}")
    print("  " + "=" * len(title))
    for dom, imp, q, u, grade, rec, dur, mit, mstat in register():
        if dom not in domains:
            continue
        qs = "" if u == "-" else f"   {q:,.2f} {u}"
        print()
        print(f"    {imp.upper()}{qs}")
        print(f"      grade {grade}   receptor: {rec}   duration: {dur}")
        _w(f"[{mstat}] {mit}", indent=6)
    if tail:
        print()
        _w(tail, indent=4)


def report_radiological():
    """The source terms, and the refusal to turn them into doses."""
    _section(("radiological", "accident"), "RADIOLOGICAL SOURCE TERMS",
             "NONE OF THE ABOVE IS A DOSE. Each is a source term or a "
             "requirement on release. Turning one into a dose needs site "
             "meteorology, a stack, a population and a pathway model; a "
             "station with no site has none of those, and a number produced "
             "without them would be a reassurance rather than a result.")


def report_waste():
    """What leaves the site, and for how long it matters."""
    _section(("waste",), "WASTE",
             "THE ACTINIDES ARE THE POINT. A solid-fuel reactor buries its "
             "unburnt heavy metal and its minor actinides, and those are "
             "what set a repository's design life. A liquid fuel with "
             "online processing returns them to the salt and burns them, so "
             "what leaves is fission products -- three hundred years rather "
             "than three hundred thousand. That is a consequence of the "
             "chemistry the NEUTRON BUDGET already forced, not an extra.")


def report_conventional():
    """Chemical, thermal, water and land."""
    _section(("conventional", "lifecycle"), "CONVENTIONAL AND LIFECYCLE",
             "The largest physical interaction this station has with its "
             "surroundings is the waste heat, and it is an ordinary "
             "thermal-plant impact at an ordinary thermal-plant size.")


def report_benefit():
    """The rows that run the other way."""
    P, M, C, X = _mods()
    print("  WHAT THE STATION REDUCES")
    print("  " + "=" * 27)
    _section(("lifecycle",), "")
    print()
    print("    LIFECYCLE CARBON, AGAINST WHAT IS BUILT TODAY")
    print(f"      {'this station':<16} {construction_g_per_kwh():>8.3f}"
          "  g CO2/kWh   construction only, from the bill")
    for k, v in sorted(LIFECYCLE_G_PER_KWH.items(), key=lambda x: -x[1]):
        print(f"      {k:<16} {v:>8.1f}  g CO2/kWh   SOURCED")
    print()
    ratio = LIFECYCLE_G_PER_KWH["nuclear, PWR"] / construction_g_per_kwh()
    _w(f"READ THAT GAP AS A WARNING, NOT AS A RESULT. The station's figure "
       f"is {ratio:.0f}x below the sourced PWR row, and a gap that size is "
       f"not a finding about the design -- it is a measure of how little of "
       f"a life-cycle assessment is structural steel. This counts the "
       f"solenoids, the cryomodule structure and the coil shielding from "
       f"materials.py's bill and NOTHING ELSE: no cryoplant, no isotope "
       f"separation, no civil works, no transport, no decommissioning. It "
       f"is a FLOOR. A real assessment would land in the same band as the "
       f"other non-combustion rows. What is not an estimate is the row "
       f"above it -- operation emits nothing, and the front end does not "
       f"exist.", indent=4)
    print()
    print("    AND THE ONE THAT IS NOT CARBON")
    _w(f"No ore is moved for this station. The front end -- mining, "
       f"milling, tailings, conversion, enrichment -- is most of nuclear "
       f"power's material footprint and this design does not have one, "
       f"because it eats what enrichment already threw away: "
       f"{du_liability_removed_t_per_year():.2f} t a year of a stockpile "
       f"holding {X.stock_station_lifetimes():,.0f} station-lifetimes.",
       indent=6)


def report_proliferation():
    """The objection that is not environmental and belongs here anyway."""
    _section(("proliferation",), "PROLIFERATION",
             "This row is in an environmental register because it is the "
             "objection a permitting authority will raise first and because "
             "nothing else in this work would otherwise state it. Its "
             "mitigation status is REQUIREMENT and not DESIGNED: the "
             "flowsheet that returns actinides and separates nothing is "
             "described but not demonstrated, and until it is built the "
             "answer is a specification rather than a fact.")


def report_mitigation():
    """The mitigation plan, consolidated by what it demands of the builder."""
    print("  MITIGATION PLAN")
    print("  " + "=" * 15)
    print()
    _w("Grouped by what each measure demands, because that is how a builder "
       "meets them: some are ordinary practice, some are already in this "
       "design, and some are targets whose means are not demonstrated.",
       indent=4)
    for stat in MIT_STATUS:
        rows = [r for r in register() if r[8] == stat]
        print()
        print(f"    {stat}  ({len(rows)} of {len(register())})")
        for dom, imp, _q, _u, grade, _rec, _dur, mit, _s in rows:
            print()
            print(f"      [{grade}] {dom}: {imp}")
            _w(mit, indent=9)
    print()
    print("    WHAT A BUILDER MUST DECIDE EARLY AND CANNOT REVISIT")
    for item in (
        "LOW-COBALT, LOW-NIOBIUM STEEL for everything inside the shield. "
        "Co-60 and Nb-94 decide the decommissioning waste class forty years "
        "later and the choice is made at procurement.",
        "THE SALT FLOWSHEET SEPARATES NOTHING. A processing plant that "
        "produced a plutonium stream would be a different plant and the "
        "proliferation answer would be gone. This is an architecture "
        "decision, not an operating rule.",
        "MODULARITY IS A SAFETY CASE, not only a construction convenience. "
        "The bounding tritium release is one cell because the station is "
        "twenty cells; building it as one would multiply the bounding "
        "release by the module count.",
        "COOLING ROUTE. Once-through, towers or dry cooling changes the "
        "water impact, the thermal plume and the efficiency, and it is a "
        "site decision that constrains the site.",
    ):
        print()
        _w("- " + item, indent=6)


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    P, M, C, X = _mods()
    r = st()
    reg = register()
    print("  the register imports rather than restates")
    check("the station is materials'/powersource's",
          r["modules"] == P.station()["modules"])
    check("the tritium inventory is the bill's, module count included",
          abs(tritium_station_mci()
              - r["modules"]
              * C.tritium_curies(X.tritium_holding_kg() * 1000.0) / 1e6)
          < 1e-9)
    check("waste heat is thermal less net, and nothing else",
          abs(waste_heat_mw() - (r["thermal_mw"] - r["net_mw"])) < 1e-9)
    check("the DU liability removed is the fertile feed, same number",
          abs(du_liability_removed_t_per_year()
              - X.uranium_feed_t_per_year()) < 1e-12)
    print()
    print("  no row is unassessed and no grade is silently absent")
    check("every row carries a known grade",
          all(g in GRADES for _d, _i, _q, _u, g, *_ in reg))
    check("every row carries a known mitigation status",
          all(s in MIT_STATUS for *_x, s in reg))
    check("every row names a receptor",
          all(len(rec) > 3 for _d, _i, _q, _u, _g, rec, *_ in reg))
    check("every row names a duration",
          all(len(d) > 0 for _d, _i, _q, _u, _g, _r, d, *_ in reg))
    check("every mitigation is a sentence, not a word",
          all(len(m) > 60 for _d, _i, _q, _u, _g, _r, _du, m, _s in reg))
    print()
    print("  the file refuses to compute a dose")
    # checked against what the program PRINTS, not against its own source --
    # a source scan would trip over the words in this very check.
    import re as _re
    printed = "".join(_capture(f) for f in
                      (report, report_radiological, report_waste,
                       report_conventional, report_benefit,
                       report_proliferation, report_mitigation))
    for unit in (r"\bm?Sv\b", r"\brem\b", r"\bmrem\b", r"\bBq\b",
                 r"\bCi/m3\b", r"\bgray\b"):
        check(f"no dose unit matching {unit} is ever printed",
              _re.search(unit, printed) is None)
    check("  -- and the radiological report says so in as many words",
          "NONE OF THE ABOVE IS A DOSE" in _capture(report_radiological))
    check("  -- while inventories, which are NOT doses, are printed",
          "MCi" in printed)
    print()
    print("  the assessment is not self-congratulatory")
    grades = [g for _d, _i, _q, _u, g, *_ in reg]
    check("there are more adverse rows than beneficial ones",
          sum(1 for g in grades if g in ("MODERATE", "MAJOR", "DOMINANT"))
          > sum(1 for g in grades if g == "BENEFIT"))
    check("the dominant impact is the design's own, not an externality",
          [i for _d, i, _q, _u, g, *_ in reg if g == "DOMINANT"]
          == ["tritium inventory, whole station"])
    check("proliferation is graded MAJOR and is not called mitigated",
          [(g, s) for d, _i, _q, _u, g, _r, _du, _m, s in reg
           if d == "proliferation"] == [("MAJOR", "REQUIREMENT")])
    check("criticality is NEGLIGIBLE because there is none, not because"
          " it is managed",
          [(g, s) for _d, i, _q, _u, g, _r, _du, _m, s in reg
           if i == "criticality"] == [("NEGLIGIBLE", "DESIGNED")]
          and P.subcritical_margin(P.K_SAFE)[1] >= P.CONTROL_WORTH_PCM)
    check("the construction carbon figure is stated as a floor",
          "FLOOR" in _capture(report_benefit))
    check("  -- and the report says how far below the sourced rows it sits",
          "x below the sourced PWR row" in _capture(report_benefit))
    check("  -- because a floor two orders under a real LCA is a warning",
          LIFECYCLE_G_PER_KWH["nuclear, PWR"] / construction_g_per_kwh()
          > 100.0)
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def _capture(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    opts = (("radiological", report_radiological), ("waste", report_waste),
            ("conventional", report_conventional), ("benefit", report_benefit),
            ("proliferation", report_proliferation),
            ("mitigation", report_mitigation))
    for name, fn in opts:
        ap.add_argument(f"--{name}", action="store_true", help=fn.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    for name, fn in opts:
        if getattr(a, name):
            return fn()
    return report()


if __name__ == "__main__":
    sys.exit(main() or 0)
