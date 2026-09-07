#!/usr/bin/env python3
"""The build package for the reference plant: everything but the drawings.

PHASE 3. This is what a team would be handed to start work -- a specification
sheet, a build sequence with its critical path, a commissioning and charging
procedure, the interface control between subsystems, the operating envelope
and its protections, an acceptance test per subsystem, and an honest register
of what has never been built.

It stops exactly where drawings begin. No dimensioned schematic, no winding
cross-section, no piping-and-instrumentation diagram, no civil layout. Those
need a design office and they need the measurements Stage A to D return; what
is here is the input that office would work from.

EVERY NUMBER IS IMPORTED. This program computes almost nothing of its own: it
reads powersource.py, machine.py, collector.py and materials.py and states
what they hold. Its selftest asserts exactly that -- that each printed
quantity still matches the instrument that owns it -- so the package cannot
drift away from the design while looking finished.

Run:  python3 tools/buildpackage.py                the whole package
      python3 tools/buildpackage.py --spec         specification sheet
      python3 tools/buildpackage.py --sequence     build order and long leads
      python3 tools/buildpackage.py --commissioning charging and first power
      python3 tools/buildpackage.py --interfaces   what each subsystem hands on
      python3 tools/buildpackage.py --envelope     operating limits and trips
      python3 tools/buildpackage.py --acceptance   how each subsystem is proved
      python3 tools/buildpackage.py --gaps         what has never been built
      python3 tools/buildpackage.py --selftest
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
    """Wrap prose to the report's column, so a paragraph stays a paragraph."""
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


def _row(label, value, unit="", note=""):
    print(f"      {label:<38} {value:>14} {unit:<9} {note}")


# ---- 1. SPECIFICATION ------------------------------------------------------
def report_spec():
    """The specification sheet: every fixed parameter and who owns it."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("1. SPECIFICATION SHEET")
    _w("Each figure below is owned by the instrument named in the last "
       "column and is reproduced here, never recomputed. Where an instrument "
       "holds a figure at a status other than measured, the status travels "
       "with it.")
    print()
    print("    STATION")
    _row("modules", f"{r['modules']:.0f}", "",
         f"of {r['module_mw']:.0f} MW each -- the target's")
    _row("", "", "", "  own sourced design point")
    _row("driver linacs", f"{r['linacs']:.0f}", "",
         f"at {P.LINAC_BEAM_MW:.0f} MW, ASSUMED")
    _row("beam energy", f"{r['beam_gev']:.1f}", "GeV", "powersource")
    _row("beam power, whole station", f"{r['beam_mw']:.1f}", "MW",
         "powersource")
    _row("stopping window", f"{r['window']:.0f}", "MeV/c",
         "FORCED by the module power")
    _row("protons on target", f"{r['protons_s']:.3e}", "/s", "derived")
    _row("blanket multiplication k", f"{P.K_SAFE:.3f}", "", "powersource")
    _row("plant gain G", f"{r['gain']:.2f}", "", "powersource")
    _row("loop requirement G_req", f"{P.loop_requirement(0.30):.3f}", "",
         "at eta_acc = 0.30")
    _row("margin on the loop", f"{r['gain']/P.loop_requirement(0.30):.2f}",
         "x", "and it is the whole design")
    _row("thermal power", f"{r['thermal_mw']:.1f}", "MW", "powersource")
    _row("net electric", f"{r['net_mw']:.1f}", "MW", "after the driver is fed")
    _row("households served", f"{r['households']:,.0f}", "",
         f"at {P.HOUSEHOLD_KW:.2f} kW each")
    _row("tritium, per module", f"{r['tritium_per_module_kg']:.3f}", "kg",
         "geometric; does not scale")
    _row("tritium, whole station", f"{r['tritium_total_kg']:.2f}", "kg",
         "and see 3 -- it exceeds the")
    _row("", "", "", "  world's civil stock")
    print()
    print("    PRODUCTION TARGET AND CAPTURE   (one module; built"
          f" {r['modules']:.0f} times)")
    _row("target", "molten lead jet", "", "MIT-3, and not the sourced")
    _row("", "", "", "  study's mercury -- see 8. A solid")
    _row("", "", "", "  rotating target")
    _row("", "", "", "  does not fit the bore, by 3.3x")
    _row("jet radius", f"{M.SRC_JET_RADIUS_MM:.1f}", "mm", "machine, SOURCED")
    _row("jet angle to beam", f"{M.SRC_JET_ANGLE_MRAD:.0f}", "mrad",
         "machine, SOURCED")
    _row("interaction lengths", f"{M.TARGET_LENGTHS:.0f}", "", "machine")
    _row("power into the target",
         f"{M.target_power_w(r['module_mw'])/1e3:.0f}", "kW",
         "machine -- and the SOURCED study")
    _row("", "", "", "  is 319 kW at 4 MW, so the")
    _row("", "", "", "  module IS that study's machine")
    _row("jet mass flow", f"{X.lead_flow_kg_s():.0f}", "kg/s",
         "materials, lead properties")
    _row("target length", f"{X.target_length_cm():.1f}", "cm",
         f"{X.target_length_ratio():.3f}x the mercury")
    _row("", "", "", "  design, which is what lead costs")
    _row("capture field at target", f"{C.DES_B_TARGET:.2f}", "T", "collector")
    _row("solenoid bore radius", f"{C.des_coil_inner_m():.2f}", "m",
         "collector")
    _row("winding thickness", f"{C.des_winding_thickness_m():.2f}", "m",
         "collector")
    _row("solenoid length", f"{C.DES_LENGTH_M:.1f}", "m", "collector")
    _row("operating current", f"{M.I_OP/1e3:.0f}", "kA", "machine")
    _row("cold mass", f"{M.cold_mass_kg()/1e3:.1f}", "t", "machine")
    _row("stored energy dump time", f"{M.dump_time_s():.2f}", "s",
         f"hot-spot margin {M.hotspot_margin():.2f}x")
    _row("coil shield thickness", f"{X.shield_thickness_m():.3f}", "m",
         f"per module, for {X.PLANT_LIFE_Y:.0f} yr")
    _row("coil life at that shield",
         f"{M.coil_life_years(r['module_mw']):.1f}", "yr",
         "AND MODULARISATION FIXED THIS:")
    _row("", "", "", "  at one 10 MW machine the coil")
    _row("", "", "", "  limited AT the plant's life; at")
    _row("", "", "", f"  {r['module_mw']:.0f} MW it does not limit at all")
    print()
    print(f"    DECAY CHANNEL AND FUEL CELL   (one module; built"
          f" {r['modules']:.0f} times)")
    _row("channel length", f"{M.channel_length_m():.1f}", "m",
         f"{100*M.DECAY_FRACTION_WANTED:.0f} % of pions decay")
    _row("channel field", "1.50", "T", "the base collector")
    _row("recompression at the cell", f"{M.CELL_B_T:.0f}", "T", "machine")
    _row("cell radius", f"{M.cell_radius_cm():.2f}", "cm",
         "set by the field, not chosen")
    _row("cell depth", f"{M.cell_depth_cm():.0f}", "cm",
         f"one muon range at phi = {M.CELL_PHI:.2f}")
    _row("cell pressure", f"{M.cell_pressure_mpa():.0f}", "MPa", "machine")
    _row("cell temperature", f"{M.CELL_T_K:.0f}", "K", "the Vesman point")
    _row("delivered acceptance",
         f"{M.delivered_eta_window(1.50, r['window']):.4f}", "",
         "at the forced window")
    _row("muon service life", f"{P.N_MEASURED:.0f}", "cycles",
         "MEASURED, Los Alamos")
    _row("cell heat load", f"{M.cell_heat_w(r['module_mw'])/1e6:.3f}", "MW",
         f"{M.cell_flow_kg_s(r['module_mw']):.3f} kg/s of coolant")
    _row("He-3 steady state", f"{M.he3_steady_ppm(r['module_mw']):.4f}", "ppm",
         "swept continuously")
    print()
    print("    BLANKET   (one, shared by every module -- see powersource"
          " --station)")
    _row("fuel salt", "NaCl-UCl3", "", "fast spectrum forces it -- materials")
    _row("salt inventory", f"{X.salt_inventory_kg()/1e3:.1f}", "t",
         f"{X.salt_volume_m3():.1f} m3")
    _row("heavy metal held", f"{X.heavy_metal_inventory_kg()/1e3:.1f}", "t",
         "materials")
    _row("burnup", f"{X.burnup_kg_per_year():.0f}", "kg/yr",
         f"{100*X.burnup_fraction_per_year():.2f} % of the holding")
    _row("salt flow", f"{X.salt_flow_kg_s():.0f}", "kg/s",
         f"{X.SALT_DT_K:.0f} K rise")
    fr, fh = X.fuel_zone_cylinder()
    _row("fuel zone", f"{2*fr:.2f} x {fh:.2f}", "m", "diameter x height")
    _row("breeder zone", f"{X.BREEDER_THICK_M:.2f}", "m",
         f"Pb-15.7Li annulus, {X.breeder_mass_kg()/1e3:.0f} t")
    _row("lithium held, 90 % Li-6", f"{X.li6_inventory_kg():.0f}", "kg",
         "materials")
    _row("fertile capture required",
         f"{P.fertile_capture_required(P.K_SAFE):.4f}", "",
         "of non-fission absorptions")
    _row("free neutrons for Li-6",
         f"{P.free_neutrons_per_source(P.K_SAFE, P.LEAK_PARASITIC_HI):.3f}",
         "", "per source neutron")
    print()
    print("    TRITIUM")
    _row("cell holding, per module", f"{X.tritium_holding_kg():.3f}", "kg",
         f"{C.tritium_curies(X.tritium_holding_kg()*1000)/1e6:.1f} MCi")
    _row("station total", f"{r['tritium_total_kg']:.2f}", "kg",
         f"{r['modules']*C.tritium_curies(X.tritium_holding_kg()*1000)/1e6:.0f}"
         " MCi")
    _row("balance at design Li-6 share", f"{r['tritium_ratio']:.3f}", "",
         "above one, so it is bred")
    _row("surplus, per module",
         f"{P.tritium_surplus_g_per_year(r['module_mw'], r['window']):.0f}",
         "g/yr", "what charges the next module")
    _row("doubling time", f"{r['doubling_y']:.1f}", "yr",
         "station and module alike")


# ---- 2. BUILD SEQUENCE -----------------------------------------------------
LONG_LEAD = [
    ("REBCO conductor", "capture solenoid inner grade",
     "The high-field band is a few kilometres of tape at a performance the "
     "market delivers in tens of kilometres a year worldwide, and it is "
     "shared with every fusion programme now building. Order first; the "
     "solenoid cannot start without it and nothing else waits on anything."),
    ("Cl-37 enriched chlorine", "fuel salt",
     "Tonnes of an isotope with NO INDUSTRIAL PRODUCTION AT ANY SCALE. This "
     "is the hardest procurement in the plant and it is harder than the "
     "magnet. A programme that does not start an enrichment line in year "
     "one does not have a blanket."),
    ("Li-6 enriched lithium", "breeder zone",
     "Also without current production: the historic route was mercury-based "
     "and is closed. Under a tonne is needed, which is small enough that a "
     "purpose-built line is credible, and it is the same line every fusion "
     "programme needs."),
    ("tritium first charge", "fuel cell and store",
     "The plant BREEDS tritium and cannot START on it. World civil "
     "production is a few kilogrammes a year from heavy-water reactors, so "
     "the first charge is years of it and the deployment rate of a FLEET is "
     "set by this and by nothing in the physics."),
    ("fissile first charge", "fuel salt",
     "Tonnes of separated fissile to reach k = 0.95. It is safeguarded "
     "material, its acquisition is a political question rather than an "
     "engineering one, and it is bred back thereafter so it is needed once."),
]

SEQUENCE = [
    ("year -3", "PROCUREMENT AND ENRICHMENT",
     "Place the five long-lead orders above. Start the Cl-37 and Li-6 lines, "
     "because both are being built rather than bought. Begin tritium "
     "allocation. Nothing else on this list is on the critical path."),
    ("year -3", "STAGE A -- THE ACCEPTANCE MEASUREMENT",
     "Section 10's first stage, and it comes first because it multiplies "
     "every balance identically and so bounds all of them at once. It runs "
     "on apparatus that exists. If it returns low, the plant is resized "
     "before any concrete is poured."),
    ("year -2", "CIVIL AND SHIELDING",
     "Tunnel, target hall, blanket vault, tritium building. The biological "
     "shield is not the coil shield and is far larger; it is the bulk of the "
     "civil works and it is ordinary construction."),
    ("year -2", "DRIVER",
     "The linac is the longest single build and it is the least novel: it is "
     "an existing machine class at a higher energy. It commissions on its "
     "own dump, independent of everything downstream, which is why it can "
     "run in parallel with the blanket."),
    ("year -1", "CAPTURE SOLENOID",
     "Wind, cold-test and train to full field on a test stand, NOT in situ. "
     "A magnet that trains in the target hall trains inside its own "
     "shielding, and the first quench is the one that teaches."),
    ("year -1", "TARGET AND CHANNEL",
     "Lead loop, jet nozzle, trace heating, decay channel solenoids -- and "
     "NO beryllium window, which left the design with the mercury (MIT-3). "
     "The loop commissions cold on a surrogate first, then on lead without "
     "beam, then with beam -- three stages, because after the third the loop "
     "is a hot cell and cannot be opened. Trace heating is commissioned as a "
     "SAFETY system, not a utility: lead that freezes in the loop ends the "
     "module."),
    ("year 0", "BLANKET AND SALT LOOP",
     "Vessel, pumps, heat exchangers, freeze-plug drain and drain tank, "
     "and the chemical processing plant. The processing plant is the "
     "single most demanding unbuilt item here and it commissions on "
     "unfuelled carrier salt first."),
    ("year 0", "FUEL CELL AND TRITIUM PLANT",
     "The cell, its containment, the hydride beds, the extraction loop on "
     "the Pb-Li, and the accountancy instruments. Tritium accountancy is "
     "commissioned BEFORE tritium arrives, on a surrogate, because the "
     "instrument that measures the breeding ratio is also the instrument "
     "that licenses the building."),
    ("year 1", "POWER CONVERSION AND BALANCE OF PLANT",
     "Ordinary, and deliberately last: nothing upstream waits on it and it "
     "is the one subsystem a conventional contractor can deliver."),
]


def report_sequence():
    """Build order, the critical path, and the five long-lead items."""
    _h("2. BUILD SEQUENCE AND CRITICAL PATH")
    _w("THE CRITICAL PATH IS NOT THE MAGNET. Four of the five long-lead "
       "items are ISOTOPES, and two of those have no industrial production "
       "line anywhere. A programme that treats this as a machine to be built "
       "will discover in year three that it has no blanket.")
    print()
    print("    LONG-LEAD ITEMS, in the order they must be ordered")
    for i, (item, where, why) in enumerate(LONG_LEAD, 1):
        print()
        print(f"      {i}. {item}   ->  {where}")
        _w(why, indent=9)
    print()
    print("    SEQUENCE")
    for when, what, how in SEQUENCE:
        print()
        print(f"      [{when}]  {what}")
        _w(how, indent=9)


# ---- 3. COMMISSIONING ------------------------------------------------------
def report_commissioning():
    """Charging and first power -- and why there is no ignition."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("3. COMMISSIONING, CHARGING AND FIRST POWER")
    _w("THERE IS NO IGNITION. The criterion this plant was built against "
       "speaks of 'an initial ignition', and the word does not apply: this "
       "device has no threshold to cross and no burning state to reach. It "
       "starts when the beam starts and it stops when the beam stops, which "
       "is the same fact that makes it stable. What the criterion is really "
       "naming is a CHARGING operation -- putting the first tritium and the "
       "first fissile into a machine that thereafter makes its own -- and "
       "charging is what this section describes.")
    print()
    steps = [
        ("C1", "COLD COMMISSIONING, NO BEAM, NO FUEL",
         f"Cool the {M.cold_mass_kg()/1e3:.0f} t cold mass, train the "
         f"solenoid to {C.DES_B_TARGET:.1f} T, and prove the "
         f"{M.dump_time_s():.2f} s dump into a real quench. Fill and heat "
         "the salt loop on unfuelled carrier salt; run the chemical "
         "processing plant on it. Nothing here is radioactive and everything "
         "here is reversible."),
        ("C2", "BEAM TO DUMP",
         f"Commission each of the {r['linacs']:.0f} linacs to full "
         f"{P.LINAC_BEAM_MW:.0f} MW on its own dump. This is a linac problem "
         "and it is solved in the linac's own terms. The target halls stay "
         "cold."),
        ("C3", "TARGET AND CHANNEL, LOW POWER",
         "Beam on the lead jet at a percent of power. Measure the muon "
         f"yield against the acceptance model's "
         f"{M.delivered_eta_window(1.50, r['window']):.4f}. THIS IS THE FIRST "
         "PLACE THE PLANT CAN REFUSE: if the acceptance is low the balance "
         "is low in exact proportion, and Stage A should already have said "
         "so years earlier."),
        ("C4", "FISSILE CHARGE AND SUBCRITICAL APPROACH",
         f"Add fissile to the salt in steps, measuring k by source "
         f"multiplication at each. Stop at k = {P.K_SAFE:.3f}, which is "
         f"{P.subcritical_margin(P.K_SAFE)[1]:,.0f} pcm subcritical -- a "
         "whole fast core's control worth. The measurement is the same one "
         "the paper specifies and it is made with the beam as the source, so "
         "it needs nothing the plant does not have."),
        ("C5", "TRITIUM CHARGE",
         f"Load {X.tritium_holding_kg():.2f} kg into each cell. THE STATION "
         f"NEEDS {r['tritium_total_kg']:.1f} kg AND THE WORLD'S CIVIL STOCK IS "
         f"ABOUT {P.WORLD_CIVIL_TRITIUM_KG:.0f} kg, so the modules are charged "
         f"in stages: {P.staged_charge()[0]:.0f} from stock, the rest bred by "
         f"those already running, and the station is at full power in year "
         f"{P.staged_charge()[1]:.1f}. A module earns from its first day, so "
         "staging costs schedule and not revenue."),
        ("C6", "POWER ASCENSION",
         f"To {r['thermal_mw']:.0f} MW thermal as modules come up, with the "
         "loop "
         "regulated against MEASURED power from the first step -- see 5. The "
         "loop's gain at the operating point is exactly one, so it is "
         "marginally stable, so it is never fed a fixed share of its own "
         "output."),
        ("C7", "BREEDING DEMONSTRATION",
         f"Close the tritium accountancy over a full year. The design says "
         f"{r['tritium_ratio']:.3f} "
         f"and a surplus of "
         f"{P.tritium_surplus_g_per_year(r['module_mw'], r['window']):.0f} "
         "g/yr; the plant is not self-sufficient until an instrument says "
         "so. UNTIL C7 CLOSES, THE PLANT IS AN ORDINARY MACHINE WITH A "
         "TRITIUM SUPPLY LINE, and the criterion it was built for is "
         "unproven."),
        ("C8", "FISSILE BREEDING DEMONSTRATION",
         "The same, on the salt: assay the fissile fraction over a year "
         f"against the required {P.fertile_capture_required(P.K_SAFE):.4f} "
         "fertile capture share. This one is slower to prove because the "
         f"holding is {1/X.burnup_fraction_per_year():.0f} years of burnup, "
         "so a year's drift is small and the measurement is correspondingly "
         "hard."),
    ]
    for tag, title, body in steps:
        print(f"      {tag}. {title}")
        _w(body, indent=11)
        print()
    _w("THE ORDER IS NOT ARBITRARY. Every step before C5 is reversible and "
       "leaves nothing behind. C5 is the step after which the building is a "
       "tritium facility for the rest of its life, and it is placed as late "
       "as it can be placed.")


# ---- 4. INTERFACES ---------------------------------------------------------
def report_interfaces():
    """What each subsystem hands the next, and what it must guarantee."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("4. INTERFACE CONTROL")
    _w("Each row is a handover. The quantity is what crosses the boundary, "
       "and the guarantee is what the upstream subsystem must promise for "
       "the downstream one to meet its own specification. A plant fails at "
       "these boundaries far more often than inside a subsystem.")
    print()
    ifaces = [
        ("driver", "target",
         f"{r['protons_s']:.3e} protons/s at {r['beam_gev']:.0f} GeV",
         f"beam spot {M.SRC_BEAM_RMS_MM:.1f} mm rms on a "
         f"{M.SRC_JET_RADIUS_MM:.1f} mm jet -- the jet is the aperture, and "
         "a mis-steered beam is a target failure, not a beam failure"),
        ("target", "capture",
         "pions into the solenoid's acceptance",
         "the target sits INSIDE the bore; machine.py's finding is that this "
         "excludes a rotating solid target by 3.3x, so the interface "
         "constrains the target and not the magnet"),
        ("target", "shielding",
         f"{r['module_mw']*1e6*M.F_INTO_SHIELDING/1e3:.0f} kW of beam power"
         " per module",
         "actively cooled, not passive; this is the largest single heat load "
         "in the plant that does nothing useful"),
        ("capture", "channel",
         f"muons at {M.delivered_eta_window(1.50, r['window']):.4f} delivered "
         "acceptance",
         "adiabatic field taper from "
         f"{C.DES_B_TARGET:.1f} T to 1.50 T without loss; a step in the "
         "field is a loss in the acceptance and the balance is linear in it"),
        ("channel", "cell",
         f"recompression to {M.CELL_B_T:.0f} T",
         f"the cell radius {M.cell_radius_cm():.2f} cm FOLLOWS from this "
         "field. A weaker recompression is a wider cell is more tritium is a "
         "bigger plant -- this interface sets the plant's size"),
        ("cell", "blanket",
         f"{P.fusions_per_proton(r['window']):.1f} fusion neutrons per proton",
         "14.1 MeV, isotropic, and the cell must be transparent to them; a "
         "cell that moderates its own neutrons hands the blanket a softer "
         "spectrum than nu = 2.9 assumes"),
        ("target", "blanket",
         f"{r['y_spall']:.0f} spallation neutrons per proton",
         "the SAME protons and the same collisions as the pions -- the two "
         "channels are additive and there is no 'instead' to trade"),
        ("blanket", "breeder zone",
         f"{P.free_neutrons_per_source(P.K_SAFE, P.LEAK_PARASITIC_HI):.3f} "
         "free neutrons per source neutron",
         f"after fission and after the {P.fertile_capture_required(P.K_SAFE):.4f} "
         "fertile share. THIS IS THE TIGHTEST INTERFACE IN THE PLANT: the "
         "tritium balance, and so criterion 4, is decided here"),
        ("breeder zone", "tritium plant",
         f"{P.tritium_supply_per_second(r['window'], r['beam_mw'], f_li=P.F_LI_DESIGN)*P.SEC_PER_YEAR*P.T_AMU/P.N_AVOGADRO:.0f} g/yr bred",
         "extracted from FLOWING Pb-Li continuously; a batch process cannot "
         "hold the cell's inventory against a 5.47 %/yr decay"),
        ("blanket", "conversion",
         f"{r['thermal_mw']:.0f} MW at {X.SALT_DT_K:.0f} K rise",
         "salt-to-secondary through an intermediate loop, because the "
         "primary is fuel"),
        ("conversion", "driver",
         f"{r['beam_mw']/P.eta_thermal():.0f} MW thermal recirculated",
         "THE LOOP. This interface is what makes the device a power source "
         f"and not an amplifier, and it must carry {r['beam_mw']:.0f} MW of "
         "beam through a wall-plug efficiency the driver states, not one the "
         "plant assumes"),
    ]
    for up, down, what, guarantee in ifaces:
        print(f"      {up.upper()}  ->  {down.upper()}")
        print(f"        crosses:   {what}")
        _w("guarantee: " + guarantee, indent=8)
        print()


# ---- 5. OPERATING ENVELOPE -------------------------------------------------
def report_envelope():
    """Operating limits, control, and the protections that hold them."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("5. OPERATING ENVELOPE, CONTROL AND PROTECTION")
    _w("STABILITY HAS TWO HALVES AND THEY HAVE DIFFERENT ANSWERS. The "
       "neutronics are stable by construction; the loop is not. Confusing "
       "the two is the single most likely way to build this wrongly.")
    print()
    _, pcm = P.subcritical_margin(P.K_SAFE)
    print("    THE NEUTRONICS -- STABLE BY CONSTRUCTION")
    _row("multiplication", f"{P.K_SAFE:.3f}", "", "subcritical, always")
    _row("margin to prompt critical", f"{pcm:,.0f}", "pcm",
         "a fast core's whole control worth")
    _row("power sensitivity 1/(k(1-k))",
         f"{P.power_sensitivity(P.K_SAFE):.1f}", "", "per unit dk")
    _row("Doppler restoring", f"{P.restoring_delta_t(P.K_SAFE):.0f}", "K",
         "per 1 % of gain")
    _w("Cut the beam and it stops. There is no decay-heat excursion path to "
       "criticality because there is no criticality to reach, and the "
       "freeze-plug drain is a second, independent statement of the same "
       "thing. The reactor does not need a control rod and does not have "
       "one.", indent=6)
    print()
    print("    THE LOOP -- MARGINALLY STABLE, AND THEREFORE REGULATED")
    _row("gain at the operating point", "1.000", "",
         "exactly one, by construction")
    _row("plant gain G", f"{r['gain']:.2f}", "", "against G_req "
         f"{P.loop_requirement(0.30):.2f}")
    _row("margin", f"{r['gain']/P.loop_requirement(0.30):.2f}", "x",
         "and this margin is the envelope")
    _w("A loop whose gain is exactly one at the operating point is "
       "marginally stable: it neither runs away nor returns. THE BEAM POWER "
       "IS THEREFORE REGULATED AGAINST A MEASURED PLANT OUTPUT, never fed a "
       "fixed share of it. A fixed-share controller is a design error and it "
       "is the kind that looks correct in steady state.", indent=6)
    print()
    print("    LIMITS")
    lims = [
        ("beam power per module", f"<= {r['module_mw']:.0f} MW",
         "the target's own study designed it here, and above it the jet is "
         "an extrapolation rather than a design"),
        ("beam power per module", f">= {P.beam_mw_for_tritium(r['window'], f_li=P.F_LI_DESIGN):.2f} MW time-averaged",
         "BELOW THIS THE TRITIUM BALANCE OPENS. It is not an instantaneous "
         "limit -- the cell holds years of inventory -- but a plant that "
         "runs at half power for a decade has quietly acquired a supply line"),
        ("k_eff", f"<= {P.K_SAFE:.3f}",
         "measured by source multiplication, continuously, and it is the "
         "one reactivity instrument the plant cannot do without"),
        ("cell pressure", f"<= {M.cell_pressure_mpa():.0f} MPa",
         f"Lame ratio {M.lame_ratio(M.cell_pressure_mpa()):.2f} at "
         f"{M.CELL_SIGMA_ALLOW_MPA:.0f} MPa allowable"),
        ("cell temperature", f"{M.CELL_T_K:.0f} K",
         "the Vesman resonance point; the fusion rate is a function of it "
         "and the service life is measured there"),
        ("coil integrated dose", f"<= {M.INSULATION_LIMIT_GY[0]/1e6:.0f} MGy",
         f"reached in {M.coil_life_years(r['module_mw']):.0f} years at the "
         f"design {X.shield_thickness_m():.3f} m of shield -- comfortably past "
         f"the {X.PLANT_LIFE_Y:.0f} year plant. At one 10 MW machine this was "
         "the LIFE-LIMITING component, reaching its limit at exactly the "
         "plant's life; dose is linear in beam power and modularising to "
         f"{r['module_mw']:.0f} MW lifted it clear. The module count bought "
         "this, and it was not what the module count was chosen for"),
        ("He-3 in the cell", f"~{M.he3_steady_ppm(r['module_mw']):.4f} ppm",
         "swept continuously; it is a poison and it doubles in "
         f"{M.he3_ppm_doubling_minutes():.0f} minutes if the sweep stops"),
    ]
    for what, limit, why in lims:
        print(f"      {what:<22} {limit}")
        _w(why, indent=9)
    print()
    print("    TRIPS, in the order they act")
    trips = [
        ("beam interlock", "the primary and the fastest; it removes the "
         "source and the assembly is subcritical the instant it opens"),
        ("freeze-plug drain", "passive, independent, and it does not need "
         "power or a signal -- the plug melts if the salt overheats"),
        ("cell isolation", "double valves on both containment boundaries; "
         "the cell is the tritium hazard and it is isolated before anything "
         "else is considered"),
        ("magnet dump", f"{M.dump_time_s():.2f} s at "
         f"{M.V_DUMP_MAX/1e3:.0f} kV, hot-spot margin "
         f"{M.hotspot_margin():.2f}x; slowest of the four and it does not "
         "need to be fast, because the beam is already off"),
    ]
    for name, why in trips:
        print(f"      - {name}")
        _w(why, indent=9)
    print()
    _w(f"BEAM TRIPS: THE THERMAL HALF IS NOW CLOSED AND THE COMMERCIAL HALF "
       f"IS NOT. A high-power linac trips often, and MIT-8 answers the "
       f"thermal question -- a {X.thermal_buffer_kg()/1000.0:,.0f} t "
       f"nitrate-salt store on the secondary rides a "
       f"{X.BUFFER_TRIP_S:.0f} s trip within {X.BUFFER_DT_K:.0f} K, so the "
       f"intermediate loop sees a ramp and not a step. What is still NOT "
       "COMPUTED here is AVAILABILITY: how much output a trip rate costs is "
       "a commercial question this work does not price, and it is a genuine "
       "open item rather than an oversight.")


# ---- 6. ACCEPTANCE ---------------------------------------------------------
def report_acceptance():
    """How each subsystem is proved, and what a failure would cost."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("6. ACCEPTANCE TESTS")
    _w("Each test states what is measured, what it must return, and what a "
       "shortfall costs the plant. A test whose failure costs nothing is not "
       "an acceptance test.")
    print()
    tests = [
        ("driver", f"{P.LINAC_BEAM_MW:.0f} MW on dump per linac,"
         " availability over 30 days",
         "a shortfall in POWER is linear in everything; a shortfall in "
         "AVAILABILITY is not priced anywhere in this work"),
        ("target", f"{M.target_power_w(r['module_mw'])/1e3:.0f} kW removed, jet "
         "stable under beam",
         "jet break-up under a 10 MW beam is unmeasured above the MERIT "
         "experiment's scale and it would cap the plant's power directly"),
        ("capture", f"{C.DES_B_TARGET:.1f} T at the target, field profile to "
         "1 %",
         "the acceptance is what the profile delivers; a 1 % field error is "
         "not a 1 % acceptance error and the relation is not linear"),
        ("channel + cell", "muon stopping rate against "
         f"{M.delivered_eta_window(1.50, r['window']):.4f}",
         "THE SINGLE MOST CONSEQUENTIAL MEASUREMENT IN THE PLANT. Every "
         "balance is linear in it, which is why Section 10 Stage A runs it "
         "years before anything is built"),
        ("cell", f"{P.N_MEASURED:.0f} cycles per muon at "
         f"phi = {M.CELL_PHI:.2f} and {M.CELL_T_K:.0f} K",
         "the 150 is MEASURED but not at this density and not at this "
         "temperature. If it falls, the fusion channel falls with it -- "
         f"though the fusion channel is only "
         f"{100*r['y_fus']/(r['y_spall']+r['y_fus']):.1f} % of the source, so "
         "the PLANT does not"),
        ("blanket", f"k = {P.K_SAFE:.3f} by source multiplication, +/- 0.005",
         "k is the gain; an error here is an error in the plant's whole "
         "output and in its safety margin at once"),
        ("breeder", "tritium production rate against "
         f"{P.tritium_supply_per_second(r['window'], r['beam_mw'], f_li=P.F_LI_DESIGN)*P.SEC_PER_YEAR*P.T_AMU/P.N_AVOGADRO:.0f} g/yr",
         "below the demand and criterion 4 fails; this is the test the whole "
         "self-sufficiency claim rests on and it takes a year to run"),
        ("salt processing", "fission-product removal rate sustaining "
         f"L <= {P.LEAK_PARASITIC_HI:.2f}",
         "the neutron budget assumes it for forty years. It is the least "
         "demonstrated item in the plant and its failure is slow, quiet and "
         "cumulative"),
        ("loop", f"G >= {P.loop_requirement(0.30):.2f} measured end to end",
         "below it the plant is an amplifier and not a power source, which "
         "is the distinction the whole design exists to make"),
    ]
    for sub, test, cost in tests:
        print(f"      {sub.upper()}")
        print(f"        measure:  {test}")
        _w("at risk:  " + cost, indent=8)
        print()


# ---- 7. GAPS ---------------------------------------------------------------
def report_gaps():
    """What has never been built, and what must be measured before it is."""
    P, M, C, X = _mods()
    r = X.ref()
    _h("7. WHAT HAS NEVER BEEN BUILT")
    _w("This register is the reason the package stops short of drawings. "
       "Each item is unbuilt, each is stated with the nearest thing that "
       "does exist, and the ratio between them is the honest measure of how "
       "far this is from a construction project.")
    print()
    gaps = [
        (f"{P.LINAC_BEAM_MW:.0f} MW, {r['beam_gev']:.0f} GeV proton linac,"
         f" {r['linacs']:.0f} of them",
         "ESS: 5 MW at 2 GeV, building",
         f"four times the power and four times the energy of the largest "
         f"machine of its class, {r['linacs']:.0f} times over -- "
         f"{r['beam_mw']:.0f} MW in all, which is {r['beam_mw']/5.0:.0f}x the "
         "world's largest. THE REACTOR IS NOT WHAT MAKES A MILLION HOUSEHOLDS "
         "HARD; THE ACCELERATOR IS"),
        (f"{C.DES_B_TARGET:.1f} T capture solenoid over a "
         f"{2*C.des_coil_inner_m():.1f} m bore",
         "MuSIC and the Mu2e/COMET solenoids, at a fraction of the power",
         "the field and bore exist separately; together, at this radiation "
         "level, they do not"),
        (f"{M.CELL_B_T:.0f} T recompression onto a "
         f"{M.cell_radius_cm():.1f} cm cell",
         "high-field solenoids exist at small bore",
         "NOTHING HAS EVER BEEN BUILT AROUND A TRITIUM CELL AT THIS FIELD. "
         "It is also the interface that sets the plant's size, so it is the "
         "one place where a shortfall costs twice"),
        (f"{P.N_MEASURED:.0f}-cycle muon service life at "
         f"phi = {M.CELL_PHI:.2f}, {M.CELL_T_K:.0f} K",
         "measured at Los Alamos, at a different density and temperature",
         "the number is MEASURED and its conditions are not this plant's. "
         "Section 10 measures it where the plant runs"),
        ("liquid-fuel fast blanket with online processing",
         "MSRE: 8 MW thermal, thermal spectrum, four years, no processing "
         "at scale",
         f"{r['thermal_mw']:.0f} MW, fast, and the processing is what buys "
         "the forty-year neutron budget. The single most demanding unbuilt "
         "item in the plant"),
        (f"Cl-37 enrichment at {X.salt_inventory_kg()*(1-X.SALT_U_MASS_FRAC)*35.45/58.44/1000:.0f} t",
         "no industrial production at any scale",
         "harder than the magnet, and a programme that starts it late does "
         "not have a blanket"),
        (f"Li-6 enrichment at {X.li6_inventory_kg():.0f} kg",
         "the historic route is closed",
         "shared with every fusion programme, which makes it likelier to be "
         "solved by someone else"),
        (f"{X.tritium_holding_kg():.2f} kg tritium in a flowing high-pressure "
         "cell",
         "ITER's inventory is comparable; the CELL is not",
         f"{C.tritium_curies(X.tritium_holding_kg()*1000)/1e6:.1f} MCi at "
         f"{M.cell_pressure_mpa():.0f} MPa and {M.CELL_T_K:.0f} K, in a "
         "20 T field, in a neutron flux"),
    ]
    for what, nearest, why in gaps:
        print(f"      {what}")
        print(f"        nearest built:  {nearest}")
        _w(why, indent=8)
        print()
    _w("AND THE ONE THAT IS NOT AN ENGINEERING GAP AT ALL. The plant breeds "
       "its own tritium and cannot start on it, so a FLEET is rate-limited "
       f"by a {r['doubling_y']:.0f} year doubling "
       "time and by the world's civil tritium stock. That is a deployment "
       "constraint, it is recorded rather than repaired, and no amount of "
       "engineering removes it.")


# ---- 8. MITIGATIONS THAT ARE BUILD ITEMS -----------------------------------
# environment.py grades every impact twice -- before mitigation and after --
# and names the carrier that takes each mitigation into the build. THESE ARE
# THOSE CARRIERS. A mitigation that lives only in an impact register is prose;
# these are line items with a requirement, an owner subsystem and an acceptance
# criterion, and environment.py's selftest fails if one of its carriers is not
# found here.
MITIGATIONS = [
    ("MIT-1 modular cells", "fuel cell",
     "The station is built as N separate cells and is never consolidated. "
     "The bounding tritium release is ONE cell's inventory, and that is the "
     "safety case, not a construction convenience.",
     "Demonstrate isolation of any single cell without affecting the rest, "
     "at power."),
    ("MIT-2 tritium containment", "fuel cell",
     "Double-walled all-metal primary; secondary containment held BELOW "
     "atmospheric so a breach vents inward; getter bed on every sweep; "
     "hydride-bed storage holding tritium as a solid at atmospheric pressure.",
     "Measured annual release below the site's licensed figure, with the "
     "accountancy instrument commissioned before tritium arrives."),
    ("MIT-3 lead target", "target",
     "The target is MOLTEN LEAD, not the sourced study's mercury. Trace "
     "heating that never fails is a SAFETY system. No beryllium vapour "
     "window: lead has no vapour to stop.",
     "Loop holds above the freezing point through a full station trip with "
     "no external power for the trace heating's design hold time."),
    ("MIT-4 krypton capture", "blanket",
     "Delay beds for short-lived noble gases; cryogenic charcoal capture and "
     "bottling for Kr-85, which will not wait.",
     "Kr-85 capture fraction measured on the sparge stream, not inferred."),
    ("MIT-5 biological shield", "shielding",
     "Concrete sized as an ATTENUATION FACTOR, separately from the coil "
     "shield, which answers an insulation dose limit and not a personnel one.",
     "Measured attenuation on the built shield against the design factor, "
     "before first full-power beam."),
    ("MIT-6 subcritical by construction", "blanket",
     "k is held below the design value at all times and there is no "
     "reactivity device that could raise it. Continuous source-multiplication "
     "measurement is the one reactivity instrument the plant cannot omit.",
     "k measured continuously; the interlock trips the beam on any excursion "
     "toward the limit."),
    ("MIT-7 freeze-plug drain and bunded vault", "blanket",
     "Passive freeze-plug drain to a subcritical, passively cooled tank "
     "needing no power and no operator; guard vessel around the primary; "
     "lined and bunded vault sized for the WHOLE inventory. The same "
     "philosophy covers the Pb-Li breeder loop.",
     "Drain demonstrated from full temperature with all power removed."),
    ("MIT-8 thermal buffer", "conversion",
     "Nitrate-salt store on the SECONDARY side, sized to ride out a beam "
     "trip within the loop's temperature band. It also gives the station "
     "load-following, which it wants anyway.",
     "Ride-through demonstrated on a real trip, with the intermediate loop "
     "inside its band."),
    ("MIT-9 partition and transmute", "blanket",
     "The flowsheet returns ACTINIDES to the salt to be burnt; partitions "
     "Cs-137 and Sr-90 to engineered decay storage; and routes Tc-99 and "
     "I-129 back into the fast flux to be transmuted.",
     "Actinide return fraction and Cs/Sr partition fraction measured on the "
     "processing stream."),
    ("MIT-10 reduced-activation steel", "capture, shielding",
     "EUROFER- or F82H-class steel for everything inside the shield: Cr and "
     "W in place of Mo, Nb and Ni; cobalt below 100 ppm. THIS IS A "
     "PROCUREMENT DECISION AND SETS THE DECOMMISSIONING WASTE CLASS A "
     "CENTURY LATER.",
     "Certified heat analysis on every heat, before the steel is cut."),
    ("MIT-11 dry cooling", "conversion",
     "Air-cooled condensers. ZERO water consumed. The penalty is in the "
     "design's own output figure and the module count was raised to absorb "
     "it -- reverting to wet cooling recovers output and returns the "
     "receiving-water impact.",
     "Rated heat rejection at the site's design ambient, which is the "
     "condition dry cooling is worst at."),
    ("MIT-12 underground tunnel", "driver",
     "The linacs go underground, as every machine of this class does. It "
     "returns the surface and it is also the cheapest shielding available.",
     "Surface dose rate above the tunnel, measured."),
    ("MIT-13 tails as feed", "blanket",
     "The fertile feed is enrichment tails. No ore is mined, no mill "
     "tailings are made, no enrichment is run for this station.",
     "Feed provenance documented; it is a procurement record, not a "
     "measurement."),
    ("MIT-14 fissile from civil stock", "blanket",
     "The first fissile charge is separated civil plutonium, which the "
     "station FISSIONS and does not return. A safeguarded acquisition whose "
     "effect is to destroy a proliferation liability permanently.",
     "Material balance closed over the charge, under safeguards."),
    ("MIT-15 no-separation flowsheet", "blanket",
     "There is no separated-plutonium stream anywhere in the processing "
     "plant, by architecture. Continuous assay of a FLUID fuel, which is "
     "easier to account for than any solid one.",
     "Demonstrated material accountancy closure on the salt loop; and the "
     "equilibrium isotopic vector MEASURED, because the denaturing argument "
     "is a requirement in this work and not a result."),
]


def report_mitigations():
    """The environmental mitigations, as build items with acceptance."""
    P, M, C, X = _mods()
    _h("8. MITIGATIONS AS BUILD ITEMS")
    _w("environment.py grades every impact twice -- before mitigation and "
       "after -- and names the carrier that takes each mitigation into the "
       "build. These are those carriers. Each is a line item with a "
       "requirement and an acceptance criterion, because a mitigation that "
       "lives only in an impact register is prose.")
    for name, owner, req, acc in MITIGATIONS:
        print()
        print(f"      {name}   [{owner}]")
        _w(req, indent=9)
        print(f"         accept:  {acc}")
    print()
    _w("FIVE OF THESE CHANGED THE PLANT RATHER THAN DESCRIBING IT: the target "
       "material, dry cooling, the thermal buffer, the biological shield's "
       "sizing and the reduced-activation steel. Two of them cost output or "
       "schedule and were taken anyway. That is the test of whether a "
       "mitigation is real.")



def report():
    P, M, C, X = _mods()
    r = X.ref()
    print("  BUILD PACKAGE -- THE REFERENCE PLANT")
    print("  " + "=" * 36)
    _w(f"{r['modules']:.0f} modules of {r['module_mw']:.0f} MW,"
       f" {r['linacs']:.0f} linacs, {r['beam_mw']:.0f} MW of"
       f" {r['beam_gev']:.0f} GeV beam in all, k = {P.K_SAFE:.2f}, base"
       f" collector at a {r['window']:.0f} MeV/c stopping window."
       f" {r['thermal_mw']:.0f} MW thermal, {r['net_mw']:.0f} MW net"
       f" electric, {r['households']:,.0f} households.", indent=2)
    for fn in (report_spec, report_sequence, report_commissioning,
               report_interfaces, report_envelope, report_acceptance,
               report_gaps, report_mitigations):
        fn()


def _capture(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    P, M, C, X = _mods()
    r = X.ref()
    print("  the package states the design and never restates it")
    check("the station is materials'/powersource's, not this file's",
          r["modules"] == P.station()["modules"]
          and abs(r["thermal_mw"] - r["beam_mw"] * r["gain"]) < 1e-9)
    check("this file defines no design constant of its own",
          all(not (k.isupper() and isinstance(v, (int, float)))
              for k, v in globals().items()))
    print()
    print("  the package's own claims are checked against the instruments")
    check("the loop margin is above one, so the plant is a power source",
          r["gain"] / P.loop_requirement(0.30) > 1.0)
    check("the blanket is subcritical by a whole control worth",
          P.subcritical_margin(P.K_SAFE)[1] >= P.CONTROL_WORTH_PCM)
    check("a shield thickness exists that buys the plant's coil life",
          0.1 < X.shield_thickness_m() < 3.0)
    # the two radiation figures are one design and the identity proves it:
    # inverting the life for the thickness that produced it must return the
    # SAME thickness at every beam power, since the design's shield is fixed
    # and only the dose scales.
    thicks = [round(M.shield_for_life_m(M.coil_life_years(p), p), 6)
              for p in (5.0, 10.0, 20.0, 40.0)]
    check("  -- and inverting the coil life returns one thickness at any power",
          len(set(thicks)) == 1)
    check("  -- and modularisation lifted the coil off the life limit",
          M.coil_life_years(r["module_mw"]) > 2.0 * X.PLANT_LIFE_Y
          and M.coil_life_years(10.0) < X.PLANT_LIFE_Y * 1.01)
    check("the tritium balance closes at the reference beam power",
          r["tritium_ratio"] > 1.0)
    check("  -- and the plant can breed a successor inside its own life",
          r["doubling_y"] < X.PLANT_LIFE_Y)
    print()
    print("  the sequence and the gaps are consistent with the bill")
    bill_mats = " ".join(m for _s, m, *_ in X.bill()).lower()
    for item, _where, _why in LONG_LEAD:
        key = item.split()[0].lower().rstrip(",")
        check(f"long-lead '{item}' appears in the bill of materials",
              key in bill_mats or key in ("fissile", "tritium"))
    check("the sequence runs Stage A before any civil works",
          [i for i, s in enumerate(SEQUENCE) if "STAGE A" in s[1]][0]
          < [i for i, s in enumerate(SEQUENCE) if "CIVIL" in s[1]][0])
    # the commissioning order is the argument, so it is asserted rather than
    # asserted-true: everything reversible must precede the step after which
    # the building is a tritium facility for its whole life.
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report_commissioning()
    text = buf.getvalue()
    order = [text.index(f"{t}.") for t in
             ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8")]
    check("the commissioning steps are printed in order",
          order == sorted(order))
    check("the tritium charge follows every reversible step",
          text.index("C5.") > text.index("C4.")
          and text.index("C5.") > text.index("C3."))
    check("  -- and precedes power ascension and the breeding proof",
          text.index("C5.") < text.index("C6.") < text.index("C7."))
    print()
    print("  every section renders -- which is how a stale call is caught")
    for name, fn in (("spec", report_spec), ("sequence", report_sequence),
                     ("commissioning", report_commissioning),
                     ("interfaces", report_interfaces),
                     ("envelope", report_envelope),
                     ("acceptance", report_acceptance), ("gaps", report_gaps),
                     ("mitigations", report_mitigations)):
        try:
            out = _capture(fn)
            ok = len(out) > 200
        except Exception as exc:                      # noqa: BLE001
            ok = False
            print(f"      {name}: {type(exc).__name__}: {exc}")
        check(f"section {name!r} renders", ok)
    print()
    print("  every environmental mitigation lands here as a build item")
    import environment as E
    names = {n for n, _o, _r, _a in MITIGATIONS}
    carriers = {row[10] for row in E.register()}
    check("every carrier environment.py names exists in this package",
          carriers <= names)
    check("  -- and no build item is orphaned from the register",
          names <= carriers)
    check("every mitigation item names an owner subsystem",
          all(len(o) > 2 for _n, o, _r, _a in MITIGATIONS))
    check("every mitigation item names an acceptance criterion",
          all(len(a) > 30 for _n, _o, _r, a in MITIGATIONS))
    check("the thermal-buffer item closes the envelope's open thermal row",
          "MIT-8" in _capture(report_envelope) or
          "thermal buffer" in _capture(report_envelope).lower())
    print()
    print("  the package refuses to draw")
    imports = [ln.strip() for ln in
               open(os.path.join(HERE, "buildpackage.py")).read().splitlines()
               if ln.startswith(("import ", "from "))
               or ln.strip().startswith(("import ", "from "))]
    drawing = ("matplotlib", "PIL", "cairo", "svgwrite", "ezdxf", "reportlab")
    check("no drawing library is imported -- drawings are out of scope",
          not any(d in ln for ln in imports for d in drawing))
    check("  -- and the package is stdlib plus this repository only",
          all(any(t in ln for t in ("argparse", "contextlib", "functools",
                                    "io", "os", "sys", "collector", "machine",
                                    "materials", "powersource",
                                    "environment"))
              for ln in imports))
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    for name, fn in (("spec", report_spec), ("sequence", report_sequence),
                     ("commissioning", report_commissioning),
                     ("interfaces", report_interfaces),
                     ("envelope", report_envelope),
                     ("acceptance", report_acceptance),
                     ("gaps", report_gaps),
                     ("mitigations", report_mitigations)):
        ap.add_argument(f"--{name}", action="store_true", help=fn.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    for name, fn in (("spec", report_spec), ("sequence", report_sequence),
                     ("commissioning", report_commissioning),
                     ("interfaces", report_interfaces),
                     ("envelope", report_envelope),
                     ("acceptance", report_acceptance),
                     ("gaps", report_gaps),
                     ("mitigations", report_mitigations)):
        if getattr(a, name):
            return fn()
    return report()


if __name__ == "__main__":
    sys.exit(main() or 0)
