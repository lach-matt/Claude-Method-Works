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


def lead_station_t():
    """The TARGET loops' lead. Imported; the substitution is materials.py's."""
    _P, _M, _C, X = _mods()
    return st()["modules"] * X.lead_inventory_kg() / 1000.0


def lead_breeder_t():
    """The BREEDER zone's lead, which is a different inventory entirely."""
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
# (domain, impact, quantity, unit, grade_before, residual, receptor, duration,
#  mitigation, mitigation status, carrier)
#
# TWO GRADES PER ROW, and the second is the one that matters. `grade_before` is
# what the impact is if nothing is done about it; `residual` is what is left
# once the mitigation named in the row is BUILT. A mitigation that does not
# move the grade is not a mitigation, and this file says so by printing both.
#
# `carrier` names the item in buildpackage.py that carries the mitigation into
# the build. The selftest checks every one of them exists there: a mitigation
# that lives only in this file is prose, and prose does not get built.
def register():
    P, M, C, X = _mods()
    r = st()
    rows = []
    A = rows.append

    # --- radiological, routine
    A(("radiological", "tritium inventory, whole station",
       tritium_station_mci(), "MCi", "DOMINANT", "MAJOR",
       "public, via HTO in water", "12.32 y half-life",
       "THE INVENTORY CANNOT BE MADE NEGLIGIBLE AND THIS ROW SAYS SO. It is "
       "the fuel. What the design does is attack it from every side that "
       "exists: the cell is the smallest the physics allows, its size is set "
       "by the muon range rather than by the power, the stopping window is "
       f"already the narrow one the scale-up forced, and the station holds it "
       f"as {r['modules']:.0f} separate cells of "
       f"{X.tritium_holding_kg():.2f} kg rather than one. One further lever "
       f"is available and not taken: recompressing the cell to 25 T instead "
       f"of {M.CELL_B_T:.0f} would cut the holding to "
       f"{r['modules']*C.tritium_inventory_kg(r['window'], M.channel_beam_radius_cm(25.0)):.1f} kg, "
       "and it is left as a requirement because it changes a seated design "
       "parameter. WHAT WOULD CLEAR THIS ROW IS A DIFFERENT FUEL, NOT A "
       "BETTER CONTAINMENT: window.py --fuels finds that a deuterium cell "
       "tritiates itself to about half a percent and holds some sixty times "
       "less, at the cost of a fusion channel fifty times weaker -- which is "
       "the same eight percent of beam that deleting the channel costs. "
       "--tradeoff prices all three routes. This file does not choose among "
       "them.", "DESIGNED", "MIT-1 modular cells"))
    A(("radiological", "tritium routine release", 0.0, "-", "MAJOR", "MINOR",
       "public", "continuous",
       "Double-walled all-metal primary, secondary containment held BELOW "
       "atmospheric so a breach vents inward, a getter bed on every sweep, and "
       "hydride-bed storage that holds tritium as a solid at atmospheric "
       "pressure. The release requirement itself is not computed here -- a "
       "dose needs a site -- so the residual is MINOR and not NEGLIGIBLE: the "
       "containment is designed, the release figure is a requirement, and "
       "those are different things.", "DESIGNED", "MIT-2 tritium containment"))
    A(("radiological", "activated lead, target loops",
       lead_station_t(), "t", "MODERATE", "MINOR", "workers",
       "months to years",
       f"{r['modules']:.0f} sealed loops, never opened after first beam, "
       "maintained remotely, each a replaceable cartridge. It stays MINOR "
       "rather than NEGLIGIBLE because activated lead is activated lead -- "
       "what the material change bought is that its failure mode is a puddle "
       "rather than a vapour.", "DESIGNED", "MIT-3 lead target"))
    A(("radiological", "noble gases from salt processing", 0.0, "-",
       "MODERATE", "NEGLIGIBLE", "public", "hours to days",
       "Delay beds let the short-lived decay before any stack release, and "
       "Kr-85 at 10.8 y -- the one that will not wait -- is captured on "
       "cryogenic charcoal and bottled. Routine at reprocessing plants. THIS "
       "MOVES AN ATMOSPHERIC RELEASE INTO THE WASTE INVENTORY, which is the "
       "trade and is named as one rather than counted twice.", "PRACTICE",
       "MIT-4 krypton capture"))
    A(("radiological", "direct radiation and skyshine",
       X.bio_shield_mass_kg() * r["modules"] / 1000.0, "t of concrete",
       "MODERATE", "NEGLIGIBLE", "public and workers", "while the beam runs",
       f"SIZED, where an earlier pass carried it open: {X.bio_shield_m():.2f} m "
       f"of concrete, an attenuation of {X.BIO_ATTENUATION:.0e} at a "
       f"{X.CONCRETE_REMOVAL_CM:.0f} cm removal length. An attenuation FACTOR "
       "is computable without a site where a dose is not, and shielding is an "
       "engineering certainty rather than a research question -- the only "
       "question was ever how much concrete, and now it is answered.",
       "DESIGNED", "MIT-5 biological shield"))

    # --- radiological, accident
    A(("accident", "fuel cell breach", X.tritium_holding_kg(), "kg",
       "MAJOR", "MINOR", "public", "the release, then 12.32 y",
       "ONE MODULE'S CELL IS THE BOUNDING RELEASE, AND THAT IS WHY THE "
       f"STATION IS MODULAR. {r['modules']:.0f} cells of "
       f"{X.tritium_holding_kg():.2f} kg cannot fail as one of "
       f"{r['tritium_total_kg']:.1f} kg, and modularity was chosen for the "
       "target's sourced power before it was ever a safety case -- it is one "
       "anyway. Each cell has its own secondary containment at sub-atmospheric "
       "pressure with an isolation pair on both boundaries.", "DESIGNED",
       "MIT-1 modular cells"))
    A(("accident", "criticality", 0.0, "-", "NEGLIGIBLE", "NEGLIGIBLE",
       "public", "-",
       "THERE IS NO CRITICALITY ACCIDENT TO MITIGATE, so this row is the one "
       "place where the two grades are equal because nothing needed doing. "
       f"The blanket is subcritical by "
       f"{P.subcritical_margin(P.K_SAFE)[1]:,.0f} pcm -- a whole fast core's "
       "control worth -- so cutting the beam stops it, and the freeze-plug "
       "drain says the same thing again without power or a signal. "
       "Categorically safer than a reactor rather than incrementally.",
       "DESIGNED", "MIT-6 subcritical by construction"))
    A(("accident", "fuel salt spill", X.salt_inventory_kg() / 1000.0, "t",
       "MAJOR", "MINOR", "workers, site", "long",
       "Freeze-plug drain to a passively cooled subcritical tank below the "
       "vessel, needing no power and no operator; a guard vessel around the "
       "primary; and a lined, bunded vault sized for the whole inventory. "
       "This is molten-salt-reactor standard practice and the MSRE ran it. "
       "MINOR rather than NEGLIGIBLE because the salt is hot, chemically "
       "active and radioactive at once, so a spill is three events.",
       "DESIGNED", "MIT-7 freeze-plug drain and bunded vault"))
    A(("accident", "beam trip thermal cycling",
       X.thermal_buffer_kg() / 1000.0, "t of buffer salt", "MODERATE",
       "NEGLIGIBLE", "plant, not public", "over the life",
       f"CLOSED, where an earlier pass carried it open. A "
       f"{X.thermal_buffer_kg()/1000.0:,.0f} t nitrate-salt store on the "
       f"SECONDARY side rides out a {X.BUFFER_TRIP_S:.0f} s trip within "
       f"{X.BUFFER_DT_K:.0f} K, so the intermediate loop sees a slow ramp "
       "instead of a step. Concentrating-solar plants build stores at this "
       "tonnage as a matter of routine, and the same store lets the station "
       "load-follow. Trips still cost AVAILABILITY, which is a commercial "
       "question and not an environmental one.", "DESIGNED",
       "MIT-8 thermal buffer"))

    # --- waste
    A(("waste", "fission products", X.burnup_kg_per_year(), "kg/yr",
       "MODERATE", "MINOR", "repository", "300 y for the bulk",
       "The mass is the same per unit of energy as any fission plant's, "
       "because it is the same fission, so it cannot be made negligible -- it "
       "IS the energy. What a liquid fuel with online processing does is keep "
       "the ACTINIDES in the salt, where they burn, and then split what is "
       "left: Cs-137 and Sr-90, which drive the three-hundred-year heat, go "
       "to engineered decay storage; Tc-99 and I-129, which drive the "
       "long-lived mobile risk, are transmuted in the same fast flux that "
       "made them. What remains needs a century of decay storage and not a "
       "geological repository.", "DESIGNED", "MIT-9 partition and transmute"))
    A(("waste", "spent heavy metal, avoided",
       spent_fuel_avoided_t_per_year(), "t/yr", "BENEFIT", "BENEFIT",
       "repository", "over the life",
       f"A PWR of the same output discharges about "
       f"{PWR_SPENT_FUEL_T_PER_GWE_YR:.0f} t of heavy metal per GWe-year, "
       "nearly all of it unburnt uranium. This station discharges fission "
       "products only. Not a mitigation -- the design being a different kind "
       "of thing.", "DESIGNED", "MIT-9 partition and transmute"))
    A(("waste", "activated structure at decommissioning",
       activated_mass_t(), "t", "MODERATE", "MINOR", "repository, site",
       "about a century, not centuries",
       "REDUCED-ACTIVATION STEEL for everything inside the shield -- "
       "EUROFER- or F82H-class, chromium and tungsten in place of the "
       "molybdenum, niobium and nickel that make Nb-94 and Ni-63, cobalt "
       "below 100 ppm. It is the fusion programme's own material and its "
       "whole point is that activation decays to hands-on levels in about a "
       "century rather than needing a deep repository. MINOR and not "
       "NEGLIGIBLE because thousands of tonnes still need that century. THIS "
       "IS A PROCUREMENT DECISION AND CANNOT BE MADE AFTERWARDS.",
       "PRACTICE", "MIT-10 reduced-activation steel"))
    A(("waste", "beryllium windows", 0.0, "-", "MINOR", "NEGLIGIBLE",
       "workers, repository", "-",
       "ELIMINATED. The sourced design carries a beryllium window six metres "
       "downstream for exactly one reason -- to stop mercury vapour reaching "
       "the channel. Lead has no vapour to stop, so the window, its annual "
       "replacement, its beryllium dust and its waste stream all leave the "
       "design with the mercury. A mitigation that deletes a component rather "
       "than managing one.", "DESIGNED", "MIT-3 lead target"))

    # --- conventional
    A(("conventional", "mercury inventory", 0.0, "-", "MODERATE",
       "NEGLIGIBLE", "workers, site", "-",
       "ELIMINATED. The target is molten lead. Mercury's vapour pressure at "
       "its operating temperature is about eight orders of magnitude above "
       "lead's, which is why the sourced design needs a vapour window and why "
       "a mercury breach is a release where a lead breach is a puddle. The "
       "pion production this design integrates is HARP's, measured on LEAD, "
       "so the substitution also makes the machine and its own source data "
       "the same material. Pure lead and not lead-bismuth, because LBE breeds "
       f"Po-210 from Bi-209. It costs {X.target_length_ratio():.3f}x in target "
       f"length and it costs a trace-heating system that must never fail, "
       f"because lead freezes at {X.PB_MELT_C:.0f} C.", "DESIGNED",
       "MIT-3 lead target"))
    A(("conventional", "lead in the breeder", lead_breeder_t(), "t",
       "MINOR", "NEGLIGIBLE", "workers, site", "permanent if released",
       "Pb-Li is molten and reacts with water. Closed loop in a bunded vault, "
       "with the same drain philosophy as the fuel salt. The hazard is "
       "conventional and the practice is the fusion programme's own.",
       "PRACTICE", "MIT-7 freeze-plug drain and bunded vault"))
    A(("conventional", "waste heat", waste_heat_mw(), "MW", "MODERATE",
       "MINOR", "air, or a heat network", "while running",
       f"{waste_heat_mw():,.0f} MW cannot be made to vanish -- it is the "
       "second law. Two things are done with it. Air-cooled condensers move "
       "it to the atmosphere instead of to a river, which removes the "
       "receiving-water pathway entirely; and at a station serving a million "
       "households a DISTRICT HEAT network can take a large share of it, at "
       "which point the row turns into a product. MINOR is the honest "
       "residual for a site with no heat network.", "DESIGNED",
       "MIT-11 dry cooling"))
    A(("conventional", "cooling water", 0.0, "m3/s", "MODERATE",
       "NEGLIGIBLE", "receiving water", "-",
       f"ZERO. Once-through cooling would have entrained and plumed at "
       f"{cooling_once_through_m3_s():.1f} m3/s and a wet tower would have "
       f"evaporated {cooling_evaporative_t_per_day():,.0f} t/day. Air cooling "
       f"consumes no water and costs "
       f"{100*P.DRY_COOLING_PENALTY:.0f} % of gross output "
       f"({r['dry_cooling_mw']:.0f} MW). IT IS ADOPTED IN THE DESIGN RATHER "
       "THAN OFFERED BESIDE IT, and the module count absorbs the cost -- "
       "which is what a mitigation looks like when it is real.", "DESIGNED",
       "MIT-11 dry cooling"))
    A(("conventional", "linac tunnel and site", land_linac_km(), "km",
       "MINOR", "NEGLIGIBLE", "site", "permanent",
       f"{r['linacs']:.0f} linacs of {X.linac_length_m():.0f} m go "
       "UNDERGROUND, as every machine of this class already does, which "
       "returns the surface. What is left above ground is a blanket vault, "
       "the module halls and a conventional turbine hall. No mine, no fuel "
       "fabrication plant, no enrichment plant, no ash pond, no reservoir.",
       "PRACTICE", "MIT-12 underground tunnel"))

    # --- lifecycle
    A(("lifecycle", "construction CO2", construction_co2_t(), "t",
       "MINOR", "MINOR", "atmosphere", "one-off",
       f"{construction_g_per_kwh():.3f} g/kWh over the life on the counted "
       "mass, and OPERATION EMITS NONE. This one does not move, because "
       "concrete and steel are concrete and steel; the residual equals the "
       "grade and the row says so rather than inventing a measure. Read the "
       "figure as a floor -- see --benefit for how far below a real "
       "assessment it sits and why.", "DESIGNED", "MIT-10 reduced-activation steel"))
    A(("lifecycle", "front-end mining and milling", 0.0, "t/yr",
       "BENEFIT", "BENEFIT", "mine sites", "-",
       "ZERO, and it is the largest environmental result in the design. The "
       "fuel is enrichment TAILS, already mined and already stored as a "
       "liability. No ore is moved, no mill tailings are made, no enrichment "
       "is run. Most of nuclear power's material footprint is a front end "
       "this station does not have.", "DESIGNED", "MIT-13 tails as feed"))
    A(("lifecycle", "depleted uranium liability removed",
       du_liability_removed_t_per_year(), "t/yr", "BENEFIT", "BENEFIT",
       "existing storage sites", "over the life",
       "Every tonne burnt is a tonne of stored UF6 removed. The world's tails "
       "are a liability someone is paying to keep, and this is the only "
       "technology that turns the whole of it into energy rather than a small "
       "fraction.", "DESIGNED", "MIT-13 tails as feed"))
    A(("lifecycle", "separated civil plutonium consumed",
       X.heavy_metal_inventory_kg() * P.FISSILE_FRACTION[0] / 1000.0, "t",
       "BENEFIT", "BENEFIT", "the non-proliferation regime", "permanent",
       "The first fissile charge is separated civil plutonium -- a material "
       f"the world holds about {P.WORLD_CIVIL_PU_T:.0f} t of, has no use for, "
       "and is paying to guard, and which is a proliferation liability by "
       "simply existing. This station DESTROYS it: the plutonium is fissioned "
       "and does not come back out. That is the same shape of answer as the "
       "tails, on the other stockpile, and it is the reason the "
       "proliferation row below is not the whole story.", "DESIGNED",
       "MIT-14 fissile from civil stock"))

    # --- the one that is not environmental
    A(("proliferation", "plutonium bred in a processed liquid fuel",
       X.burnup_kg_per_year(), "kg/yr fissioned", "MAJOR", "MODERATE",
       "the non-proliferation regime", "permanent",
       "STATED PLAINLY BECAUSE IT IS THE OBJECTION THAT MATTERS, AND IT DOES "
       "NOT REACH NEGLIGIBLE. A fast blanket breeding Pu-239 in a liquid fuel "
       "with an online chemical plant attached is, on its face, the worst "
       "proliferation geometry in civil power. Four things answer it and none "
       "of them is reassurance. The flowsheet removes FISSION PRODUCTS and "
       "returns ACTINIDES -- there is no separated-plutonium stream anywhere "
       "in it, by architecture, and a plant that had one would be a different "
       "plant. The salt is intensely radioactive at all times, so diversion "
       "is a hot-cell problem rather than a chemistry problem. Material "
       "accountancy is EASIER here than in any solid-fuel reactor because the "
       "fuel is a fluid and can be assayed continuously. And the station is a "
       "net DESTROYER of separated plutonium, not a producer of it. What "
       "keeps the residual at MODERATE is that the equilibrium isotopic "
       "vector is a depletion result this work does not compute, so the "
       "denaturing argument is stated as a requirement and not as a fact.",
       "REQUIREMENT", "MIT-15 no-separation flowsheet"))
    return rows


GRADES = ("BENEFIT", "NEGLIGIBLE", "MINOR", "MODERATE", "MAJOR", "DOMINANT")
MIT_STATUS = ("PRACTICE", "DESIGNED", "REQUIREMENT")


def _tally(idx):
    counts = {}
    for row in register():
        counts[row[idx]] = counts.get(row[idx], 0) + 1
    return counts


def moved(row):
    """Did the mitigation actually move the grade?"""
    return GRADES.index(row[5]) < GRADES.index(row[4])


def report():
    """The impact register: every row graded before and after mitigation."""
    P, M, C, X = _mods()
    r = st()
    print("  ENVIRONMENTAL IMPACT REGISTER -- THE STATION")
    print()
    _w(f"{r['modules']:.0f} modules, {r['beam_mw']:.0f} MW of beam, "
       f"{r['thermal_mw']:.0f} MW thermal, {r['net_mw']:.0f} MW net "
       f"electric, {electricity_twh_per_year():.2f} TWh a year.", indent=4)
    print()
    _w("TWO GRADES PER ROW. 'before' is the impact with nothing done about "
       "it; 'after' is what is left once the named mitigation is BUILT. A "
       "mitigation that does not move the grade is not a mitigation, and "
       "printing both is what stops one from being claimed. The last column "
       "names the item in buildpackage.py that carries it -- a mitigation "
       "that lives only here is prose.", indent=4)
    print()
    _w("No dose is computed anywhere in this file. A dose needs a site; every "
       "radiological row is a source term and a requirement on release.",
       indent=4)
    print()
    print(f"    {'domain':<14} {'impact':<37} {'before':<11} {'after':<11}"
          f" carrier")
    last = None
    for dom, imp, _q, _u, g0, g1, _rec, _dur, _mit, _ms, car in register():
        if dom != last:
            print()
            last = dom
        mark = " " if moved((dom, imp, _q, _u, g0, g1)) or g0 == g1 else "!"
        print(f"    {dom:<14} {imp:<37} {g0:<11} {g1:<11}{mark}{car}")
    print()
    before, after = _tally(4), _tally(5)
    print("    BEFORE  " + "   ".join(f"{g} {before.get(g, 0)}" for g in GRADES))
    print("    AFTER   " + "   ".join(f"{g} {after.get(g, 0)}" for g in GRADES))
    print()
    stuck = [(i, g1) for _d, i, _q, _u, _g0, g1, *_ in register()
             if g1 not in ("BENEFIT", "NEGLIGIBLE")]
    _w(f"EVERYTHING ABOVE NEGLIGIBLE, AND THERE ARE {len(stuck)} OF THEM. "
       "These are the rows a mitigation could not clear, each with what stops "
       "it:", indent=4)
    print()
    for imp, g1 in stuck:
        print(f"      [{g1}] {imp}")
    print()
    _w("Two of those are structural rather than unfinished. TRITIUM INVENTORY "
       "is the fuel of the fusion channel, and the only thing that makes it "
       "negligible is deleting the channel -- which --tradeoff prices, "
       "because it is a decision about what this project is for and not an "
       "engineering call. PROLIFERATION stays MODERATE because the "
       "denaturing argument rests on an equilibrium isotopic vector this work "
       "does not compute. The rest are MINOR: real, bounded, and each one a "
       "quantity that cannot be driven to zero without deleting the energy "
       "that produces it.", indent=4)


def report_tradeoff():
    """The muon channel, priced against the impacts it creates."""
    P, M, C, X = _mods()
    r = st()
    _h("THE MUON CHANNEL, PRICED AGAINST WHAT IT COSTS THE ENVIRONMENT")
    _w("This is the one decision in the register that is not an engineering "
       "call, so it is put here as arithmetic and left to the reader. The "
       "fusion channel is the project's subject. It is also the sole cause of "
       "the register's only MAJOR row, and of several others.", indent=4)
    print()
    g_with = P.plant_gain(P.K_SAFE, r["y_spall"], r["y_fus"])
    g_without = P.plant_gain(P.K_SAFE, r["y_spall"], 0.0)
    print("    WHAT THE CHANNEL BUYS")
    print(f"      source neutrons per proton, with     "
          f"{r['y_spall'] + r['y_fus']:8.1f}")
    print(f"      without                              {r['y_spall']:8.1f}")
    print(f"      plant gain, with                     {g_with:8.2f}")
    print(f"      without                              {g_without:8.2f}")
    print(f"      beam needed for the same households  "
          f"{g_with/g_without:8.3f} x   "
          f"= {r['beam_mw']*g_with/g_without:.1f} MW")
    kw = _k_for_loop(r["y_spall"], r["y_fus"])
    kwo = _k_for_loop(r["y_spall"], 0.0)
    print(f"      k needed to close the loop, with     {kw:8.4f}")
    print(f"      without                              {kwo:8.4f}")
    print(f"      extra subcritical margin it buys     "
          f"{P.subcritical_margin(kw)[1]-P.subcritical_margin(kwo)[1]:8,.0f} pcm")
    print()
    print("    WHAT THE CHANNEL COSTS THE REGISTER")
    for _d, imp, _q, _u, g0, g1, *_ in register():
        if any(w in imp.lower() for w in ("tritium", "cell", "beryll")):
            print(f"      {g1:<11} {imp}")
    print(f"      and with it go {r['tritium_total_kg']:.1f} kg of tritium, "
          f"{X.li6_inventory_kg():,.0f} kg of enriched")
    print(f"      lithium, {r['modules']:.0f} capture solenoids, "
          f"{r['modules']:.0f} fuel cells, and the Pb-Li breeder loop.")
    print()
    print("    AND THERE ARE THREE OPTIONS, NOT TWO. window.py --fuels found")
    print("    the third, and it was hiding inside the fuel question.")
    print()
    sys.path.insert(0, HERE)
    import window as W
    _fdt, _fdd, c_t, n_cyc, _e, n_per_mu, m_t = W.selftritiation()
    dt = [r for r in W.fuel_table() if r[0] == "d-t"][0]
    y_dd = P.PI_PER_PROTON * M.delivered_eta_window(1.50, r["window"]) * n_per_mu
    g_dd = P.plant_gain(P.K_SAFE, r["y_spall"], y_dd)
    print(f"      {'route':<26} {'station T':>10} {'y_fus':>8} {'G':>8}"
          f" {'beam':>8}")
    print(f"      {'1  d-t, as designed':<26} {r['tritium_total_kg']:9.2f} kg"
          f" {r['y_fus']:8.2f} {g_with:8.2f} {'--':>8}")
    print(f"      {'2  d-d, self-tritiating':<26}"
          f" {r['tritium_total_kg']*m_t/0.600:9.2f} kg"
          f" {y_dd:8.2f} {g_dd:8.2f} {g_with/g_dd:7.3f}x")
    print(f"      {'3  no muon channel':<26} {0.0:9.2f} kg"
          f" {0.0:8.2f} {g_without:8.2f} {g_with/g_without:7.3f}x")
    print()
    _w("Route 2 is the one that was not obvious. A deuterium cell makes its "
       "own tritium -- one d-d branch is d + d -> t + p -- and dtmu forms far "
       "faster than ddmu, so the cell tritiates ITSELF to an equilibrium of "
       f"about {100*c_t:.2f} % and runs as a mixture. It holds "
       f"{0.600/m_t:.0f}x less tritium than the design does, it needs no "
       "lithium, no breeder zone, no tritium plant, no staged charging and no "
       "fleet doubling time, and IT IS STILL MUON-CATALYSED FUSION. It costs "
       f"{g_with/g_dd:.3f}x in beam -- which is what route 3 costs too.",
       indent=4)
    print()
    _w("A LATER PASS CORRECTED THIS COMPARISON AND THE CORRECTION IS NOT "
       "SMALL. Everything above prices the routes on BEAM POWER, on which "
       "route 2 and route 3 are within 0.001 of each other. The machine is "
       "not the beam power: a pure spallation plant's gain is EXACTLY "
       "invariant in beam energy, so the 8 GeV is bought by pion production "
       "alone and route 3 drops the driver to about 1 GeV and deletes every "
       "capture solenoid, while route 2 keeps both to deliver a fusion "
       "channel worth a tenth of a percent. ROUTE 2 PAYS ROUTE 1'S MACHINE "
       "FOR ROUTE 3'S OUTPUT. See powersource.py --routes, which is where "
       "that decision now lives.", indent=4)
    print()
    _w("SO THE TRADE IS THIS. Removing the fusion channel entirely costs "
       f"{100*(g_with/g_without-1):.1f} % more beam and about "
       f"{P.subcritical_margin(kw)[1]-P.subcritical_margin(kwo)[1]:,.0f} pcm "
       "of subcritical margin. Keeping it on deuterium costs the SAME beam "
       "and keeps the subject, at the price of a fusion channel "
       f"{dt[7]/n_per_mu:.0f}x weaker and an equilibrium this work computes to "
       "first order and does not measure. Keeping it on d-t is the design as "
       "it stands, and it is the only route that carries a MAJOR row. THIS "
       "FILE DOES NOT DECIDE IT. It states the numbers so that whoever does "
       "decide is deciding rather than assuming.", indent=4)


def _k_for_loop(y_spall, y_fus, eta_acc=0.30):
    P, _M, _C, _X = _mods()
    req = P.loop_requirement(eta_acc)
    lo, hi = 0.05, 0.999
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if P.plant_gain(mid, y_spall, y_fus) < req:
            lo = mid
        else:
            hi = mid
    return hi


def _section(domains, title, tail=None):
    if title:
        print(f"  {title}")
        print("  " + "=" * len(title))
    for dom, imp, q, u, g0, g1, rec, dur, mit, mstat, car in register():
        if dom not in domains:
            continue
        qs = "" if u == "-" else f"   {q:,.2f} {u}"
        print()
        print(f"    {imp.upper()}{qs}")
        print(f"      {g0}  ->  {g1}      receptor: {rec}   duration: {dur}")
        print(f"      carried by: {car}   [{mstat}]")
        _w(mit, indent=6)
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
             "unburnt heavy metal and its minor actinides, and those are what "
             "set a repository's design life. A liquid fuel with online "
             "processing returns them to the salt and burns them, and then "
             "partitions what is left. What remains needs about a century of "
             "decay storage rather than a geological repository -- and that "
             "follows from the chemistry the NEUTRON BUDGET already forced.")


def report_conventional():
    """Chemical, thermal, water and land."""
    _section(("conventional", "lifecycle"), "CONVENTIONAL AND LIFECYCLE",
             "The waste heat is the only conventional row that does not "
             "clear, and it does not clear because it is the second law. Dry "
             "cooling removes the water pathway entirely at the cost of a "
             "share of output, and the module count was raised to absorb it.")


def report_benefit():
    """The rows that run the other way."""
    P, M, C, X = _mods()
    print("  WHAT THE STATION REDUCES")
    print("  " + "=" * 24)
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
       f"not a finding about the design -- it is a measure of how little of a "
       f"life-cycle assessment is structural steel. This counts the "
       f"solenoids, the cryomodule structure and the coil shielding from "
       f"materials.py's bill and NOTHING ELSE: no cryoplant, no isotope "
       f"separation, no civil works, no transport, no decommissioning. It is "
       f"a FLOOR. A real assessment would land in the same band as the other "
       f"non-combustion rows. What is not an estimate is the row above it -- "
       f"operation emits nothing, and the front end does not exist.", indent=4)
    print()
    print("    AND THE TWO THAT ARE NOT CARBON")
    _w(f"No ore is moved for this station: the front end -- mining, milling, "
       f"tailings, conversion, enrichment -- is most of nuclear power's "
       f"material footprint and this design does not have one, because it "
       f"eats what enrichment already threw away, "
       f"{du_liability_removed_t_per_year():.2f} t a year of a stockpile "
       f"holding {X.stock_station_lifetimes():,.0f} station-lifetimes.",
       indent=6)
    print()
    _w(f"And the first fissile charge is separated civil plutonium -- about "
       f"{P.WORLD_CIVIL_PU_T:.0f} t of it exists, nobody has a use for it, "
       f"everybody is paying to guard it, and it is a proliferation liability "
       f"by simply existing. This station FISSIONS it. Two stockpiles the "
       f"world is paying to store, and this is the only design that consumes "
       f"both.", indent=6)


def report_proliferation():
    """The objection that is not environmental and belongs here anyway."""
    _section(("proliferation",), "PROLIFERATION",
             "This row is in an environmental register because it is the "
             "objection a permitting authority raises first and because "
             "nothing else in this work would otherwise state it. Its status "
             "is REQUIREMENT and not DESIGNED, and its residual is MODERATE "
             "and not NEGLIGIBLE: the flowsheet that returns actinides and "
             "separates nothing is described but not demonstrated, and the "
             "isotopic denaturing argument rests on a depletion calculation "
             "this work does not do. Read it beside the BENEFIT row above "
             "it -- the station consumes separated plutonium -- because "
             "neither is the whole picture alone.")


def report_mitigation():
    """The mitigation plan, consolidated by what it demands of the builder."""
    print("  MITIGATION PLAN")
    print("  " + "=" * 15)
    print()
    _w("Grouped by CARRIER -- the item in buildpackage.py that takes the "
       "mitigation into the build. A mitigation with no carrier is prose, and "
       "the selftest fails one.", indent=4)
    carriers = {}
    for row in register():
        carriers.setdefault(row[10], []).append(row)
    for car in sorted(carriers):
        rows = carriers[car]
        print()
        print(f"    {car}")
        for _d, imp, _q, _u, g0, g1, _r, _du, _m, ms, _c in rows:
            arrow = f"{g0} -> {g1}" if g0 != g1 else f"{g0} (unchanged)"
            print(f"      [{ms}] {imp}:  {arrow}")
    print()
    print("    WHAT A BUILDER MUST DECIDE EARLY AND CANNOT REVISIT")
    for item in (
        "REDUCED-ACTIVATION STEEL inside the shield. Co-60 and Nb-94 decide "
        "the decommissioning waste class a century later and the choice is "
        "made at procurement, not at decommissioning.",
        "THE TARGET IS LEAD, NOT MERCURY. It changes the loop, the trace "
        "heating, the target length and the absence of a beryllium window, "
        "and it cannot be swapped back once the loop is built.",
        "THE SALT FLOWSHEET SEPARATES NOTHING. A processing plant that "
        "produced a plutonium stream would be a different plant and the "
        "proliferation answer would be gone. Architecture, not procedure.",
        "MODULARITY IS A SAFETY CASE. The bounding tritium release is one "
        "cell because the station is many cells; building it as one would "
        "multiply the bounding release by the module count.",
        "DRY COOLING. It is in the design and the module count pays for it. "
        "Reverting to wet cooling recovers output and returns the "
        "receiving-water impact the register no longer carries.",
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
    check("every row carries a known grade, before AND after",
          all(g0 in GRADES and g1 in GRADES
              for _d, _i, _q, _u, g0, g1, *_ in reg))
    check("every row carries a known mitigation status",
          all(row[9] in MIT_STATUS for row in reg))
    check("every row names a receptor",
          all(len(row[6]) > 3 for row in reg))
    check("every row names a duration",
          all(len(row[7]) > 0 for row in reg))
    check("every mitigation is a sentence, not a word",
          all(len(row[8]) > 60 for row in reg))
    check("every row names a carrier",
          all(len(row[10]) > 4 for row in reg))
    print()
    print("  a mitigation must move the grade or say it did not")
    check("no residual is WORSE than the grade it mitigates",
          all(GRADES.index(row[5]) <= GRADES.index(row[4]) for row in reg))
    check("most rows actually moved",
          sum(1 for row in reg if moved(row)) > len(reg) / 2)
    check("the rows that did not move are the ones that could not",
          all(row[1] in ("criticality", "spent heavy metal, avoided",
                         "front-end mining and milling",
                         "depleted uranium liability removed",
                         "separated civil plutonium consumed",
                         "construction CO2")
              for row in reg if not moved(row)))
    check("nothing is left at DOMINANT after mitigation",
          all(row[5] != "DOMINANT" for row in reg))
    print()
    print("  every carrier lands in the build package as a real item")
    sys.path.insert(0, HERE)
    import buildpackage as B
    names = {n for n, _o, _r, _a in B.MITIGATIONS}
    check("every carrier exists in buildpackage.MITIGATIONS",
          {row[10] for row in reg} <= names)
    check("  -- a mitigation that lived only here would fail this",
          "MIT-99 imaginary" not in names)
    print()
    print("  the file refuses to compute a dose")
    # checked against what the program PRINTS, not against its own source --
    # a source scan would trip over the words in this very check.
    import re as _re
    printed = "".join(_capture(f) for f in
                      (report, report_radiological, report_waste,
                       report_conventional, report_benefit,
                       report_proliferation, report_mitigation,
                       report_tradeoff))
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
    check("the worst row before mitigation is the design's own doing",
          [row[1] for row in reg if row[4] == "DOMINANT"]
          == ["tritium inventory, whole station"])
    check("  -- and after mitigation it is still the worst, honestly",
          [row[1] for row in reg if row[5] == "MAJOR"]
          == ["tritium inventory, whole station"])
    check("proliferation is not claimed mitigated below MODERATE",
          [(row[5], row[9]) for row in reg if row[0] == "proliferation"]
          == [("MODERATE", "REQUIREMENT")])
    check("criticality is NEGLIGIBLE because there is none, not because"
          " it is managed",
          [(row[4], row[5]) for row in reg if row[1] == "criticality"]
          == [("NEGLIGIBLE", "NEGLIGIBLE")]
          and P.subcritical_margin(P.K_SAFE)[1] >= P.CONTROL_WORTH_PCM)
    r2 = st()
    check("the muon-channel trade is priced rather than argued",
          f"{P.plant_gain(P.K_SAFE, r2['y_spall'], r2['y_fus'])/P.plant_gain(P.K_SAFE, r2['y_spall'], 0.0):.3f}"
          in _capture(report_tradeoff))
    sys.path.insert(0, HERE)
    import window as _W
    _f1, _f2, _ct, _nc, _e, _npm, _mt = _W.selftritiation()
    _dt = [q for q in _W.fuel_table() if q[0] == "d-t"][0]
    check("the tradeoff offers three routes, not two",
          "no muon channel" in _capture(report_tradeoff)
          and "self-tritiating" in _capture(report_tradeoff))
    check("  -- and the deuterium route really holds far less tritium",
          0.600 / _mt > 10.0)
    check("  -- at a fusion channel really that much weaker",
          _dt[7] / _npm > 10.0)
    check("  -- and this file chooses none of them",
          "DOES NOT DECIDE" in _capture(report_tradeoff))
    check("  -- and removing it really would cost only single-digit percent",
          1.0 < P.plant_gain(P.K_SAFE, r2["y_spall"], r2["y_fus"])
          / P.plant_gain(P.K_SAFE, r2["y_spall"], 0.0) < 1.10)
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
            ("mitigation", report_mitigation),
            ("tradeoff", report_tradeoff))
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
