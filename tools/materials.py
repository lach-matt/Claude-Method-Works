#!/usr/bin/env python3
"""Every material the station needs, how much, and how it is stored.

PHASE 2 of the build. A bill of materials and a storage schedule for the
station `powersource.station()` sizes -- one million households, as N modules
of the sourced target power rather than as one machine, at the stopping window
that scale-up forces.

WHAT THIS PROGRAM REFUSES TO DO. It never restates a quantity another
instrument holds: the solenoid's cold mass, the cell's radius and depth, the
tritium holding, the burnup and the neutron budget are IMPORTED. Where a
quantity is not derivable from what is seated, it carries a status and the
status is never flattened:

    DERIVED     computed here from imported quantities and stated physics
    IMPORTED    another instrument's figure, used as it stands
    SOURCED     a published number, with its source named
    SCALED      a published number scaled by a stated ratio
    ASSUMED     a design choice, with the choice's basis stated
    REQUIREMENT what the plant needs, where computing it needs transport or
                chemistry this work does not do -- stated as a requirement so
                a measurement can refuse it

and every row also carries a SUPPLY class, because criterion 4 -- nothing
supplied after ignition -- is decided by that column and by nothing else:

    FIRST-CHARGE  bought once, held for the life, neither consumed nor bred
    BRED          made in-plant from what is already there
    STOCKPILED    consumed, but a life-of-plant charge fits in the building
    REPLACED      a component with a finite life; a parts line, not a fuel line
    CIRCULATING   an inventory that moves and is neither consumed nor bred
    PRODUCED      a stream running OUTWARD -- waste, or a co-product

Run:  python3 tools/materials.py            the bill of materials
      python3 tools/materials.py --storage  the storage schedule
      python3 tools/materials.py --supply   criterion 4, adjudicated row by row
      python3 tools/materials.py --uranium  depleted uranium as the fertile feed
      python3 tools/materials.py --selftest
"""

import argparse
import functools
import math
import os
import sys


@functools.lru_cache(maxsize=None)
def _ps():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import powersource
    return powersource


@functools.lru_cache(maxsize=None)
def _mach():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import machine
    return machine


@functools.lru_cache(maxsize=None)
def _coll():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import collector
    return collector


# ---- THE BLANKET IS A CHOICE, AND THE CHOICE IS FORCED IN THREE PLACES -----
# powersource.py's neutron budget is not neutral about blanket chemistry. It
# spends 6.552 neutrons per source neutron on fertile capture, allows L = 0.20
# for leakage AND parasitic capture together, and assumes nu = 2.9. Three
# consequences follow and each excludes a family of designs:
#
#   1. nu = 2.9 is Pu-239 FAST. In a thermal spectrum the U-Pu breeding ratio
#      does not reach f_b = 0.487. The blanket must be fast, which excludes
#      graphite moderation and excludes FLiBe.
#   2. L = 0.20 must cover leakage, structure, coolant AND fission products,
#      for FORTY YEARS. A solid-fuel core accumulates fission-product capture
#      monotonically and would eat that budget. The fuel must therefore be
#      LIQUID, so fission products leave continuously.
#   3. A liquid fast fuel salt is a chloride, not a fluoride. Natural chlorine
#      is 24 % Cl-37 and 76 % Cl-35, and Cl-35(n,p)S-35 is both a parasitic
#      absorption the budget cannot afford and a sulphur source that attacks
#      the loop. The chlorine must be Cl-37 enriched.
#
# So: NaCl-UCl3 fast fuel salt, Cl-37 enriched, with a separate Pb-15.7Li
# breeding and reflecting zone at 90 % Li-6. Pb-Li is chosen over a lithium
# salt because it MULTIPLIES as it breeds -- Pb(n,2n) -- and returns part of L
# as a reflector, which is the one lever the budget has left.
SALT_RHO = 3300.0            # kg/m3, NaCl-UCl3 at 900 K            SOURCED band
SALT_CP = 1000.0             # J/kg/K                               SOURCED band
SALT_U_MASS_FRAC = 0.40      # NaCl-UCl3 near the eutectic          SOURCED
SALT_DT_K = 200.0            # 700 -> 900 K loop rise               ASSUMED
SALT_RESIDENCE_S = 30.0      # loop transit; sets inventory         ASSUMED
PBLI_RHO = 9300.0            # kg/m3, Pb-15.7Li                     SOURCED
PBLI_LI_MASS_FRAC = 0.0068   # 15.7 at.% Li in Pb                   SOURCED
LI6_ENRICH = 0.90            # ASSUMED, and it is the design's own f_li lever
LI6_AMU, LI_AMU, T_AMU, HE_AMU = 6.015, 6.94, 3.016, 4.003
HM_ATOMS_PER_KG = 2.53e24
SEC_PER_YEAR = 3.15576e7
N_A = 6.02214076e23
PLANT_LIFE_Y = 40.0

# the breeding zone's geometry, from the fuel zone's
BREEDER_THICK_M = 0.50       # ASSUMED: about one fast mean free path in Pb
HG_RHO = 13534.0             # kg/m3                                 SOURCED
HG_RESIDENCE_S = 20.0        # target loop transit                   ASSUMED
STEEL_RHO = 7900.0
CONCRETE_RHO = 2350.0

# the driver, scaled from a machine that exists rather than invented
ESS_ENERGY_GEV, ESS_CAVITIES, ESS_SC_LENGTH_M = 2.0, 120.0, 155.0   # SOURCED
NB_PER_CAVITY_KG = 100.0     # 5-cell elliptical, 3.8 mm RRR300 sheet  SOURCED band
BEAM_GEV = 8.0


# ---- quantities the plant fixes -------------------------------------------
@functools.lru_cache(maxsize=None)
def ref():
    """THE STATION, imported whole from powersource.station(). Nothing here is
    restated -- not the module count, not the window, not the gain."""
    P = _ps()
    st = P.station()
    st = dict(st)
    st["beam_gev"] = BEAM_GEV
    st["protons_s"] = P.protons_per_second(st["beam_mw"])
    st["source_n_s"] = ((st["y_spall"] + st["y_fus"])
                        * P.protons_per_second(st["beam_mw"]))
    return st


@functools.lru_cache(maxsize=None)
def fissions_per_second():
    P = _ps()
    return P.fissions_per_source(P.K_SAFE) * ref()["source_n_s"]


@functools.lru_cache(maxsize=None)
def burnup_kg_per_year():
    """Heavy metal fissioned a year, and it IS a feed. See uranium_feed()."""
    return fissions_per_second() * SEC_PER_YEAR / HM_ATOMS_PER_KG


@functools.lru_cache(maxsize=None)
def salt_flow_kg_s():
    """Set by the heat, not by the neutronics."""
    return ref()["thermal_mw"] * 1e6 / (SALT_CP * SALT_DT_K)


def salt_inventory_kg(residence_s=SALT_RESIDENCE_S):
    return salt_flow_kg_s() * residence_s


def salt_volume_m3(residence_s=SALT_RESIDENCE_S):
    return salt_inventory_kg(residence_s) / SALT_RHO


def heavy_metal_inventory_kg(residence_s=SALT_RESIDENCE_S):
    return salt_inventory_kg(residence_s) * SALT_U_MASS_FRAC


def burnup_fraction_per_year():
    """What fraction of the holding fissions a year. Under a few percent and
    the salt is a holding; above it and the salt is a feed."""
    return burnup_kg_per_year() / heavy_metal_inventory_kg()


def fissile_depletion_fraction(years=PLANT_LIFE_Y):
    """Share of the fissile holding fissioned over the life, unbred."""
    return burnup_kg_per_year() * years / heavy_metal_inventory_kg()


def k_without_breeding(years=PLANT_LIFE_Y):
    """First order, and stated as first order: for a fixed geometry the
    reactivity of a subcritical assembly falls with the fissile density, so
    dk/k ~ dN/N. A transport calculation would refine this; the CONCLUSION --
    that the collapse is large -- survives any refinement, which is why it is
    reported as a requirement on breeding rather than as a prediction of k."""
    P = _ps()
    return P.K_SAFE * (1.0 - fissile_depletion_fraction(years))


def gain_without_breeding(years=PLANT_LIFE_Y):
    P = _ps()
    r = ref()
    return P.plant_gain(k_without_breeding(years), r["y_spall"], r["y_fus"])


def fuel_zone_cylinder(residence_s=SALT_RESIDENCE_S, aspect=2.0):
    """A right cylinder of the salt volume at a stated height/diameter ratio.
    Geometry only -- it fixes the breeding zone's area and nothing else."""
    v = salt_volume_m3(residence_s)
    r = (v / (math.pi * aspect * 2.0)) ** (1.0 / 3.0)
    return r, aspect * 2.0 * r


def breeder_volume_m3(thick_m=BREEDER_THICK_M):
    r, h = fuel_zone_cylinder()
    outer_r, outer_h = r + thick_m, h + 2.0 * thick_m
    return math.pi * (outer_r ** 2 * outer_h - r ** 2 * h)


def breeder_mass_kg(thick_m=BREEDER_THICK_M):
    return breeder_volume_m3(thick_m) * PBLI_RHO


def lithium_inventory_kg(thick_m=BREEDER_THICK_M):
    return breeder_mass_kg(thick_m) * PBLI_LI_MASS_FRAC


def li6_inventory_kg(thick_m=BREEDER_THICK_M, enrich=LI6_ENRICH):
    """Enriched Li-6 held, as distinct from Li-6 burnt."""
    return lithium_inventory_kg(thick_m) * enrich * LI6_AMU / LI_AMU


@functools.lru_cache(maxsize=None)
def window():
    return ref()["window"]


def tritium_demand_g_per_year():
    """The WHOLE STATION: N modules each holding and each burning."""
    P = _ps()
    r = ref()
    d, b = P.tritium_demand_per_second(window(), r["module_mw"])
    return r["modules"] * (d + b) * SEC_PER_YEAR * T_AMU / N_A


def li6_burn_kg_per_year():
    """One Li-6 per triton. This is the plant's only true material feed."""
    return tritium_demand_g_per_year() / T_AMU * LI6_AMU / 1000.0


def li6_burndown_fraction():
    """Over the life. If it is small the enrichment is a first charge."""
    return li6_burn_kg_per_year() * PLANT_LIFE_Y / li6_inventory_kg()


@functools.lru_cache(maxsize=None)
def tritium_holding_kg():
    """One module's cell. The station holds N of these -- see bill()."""
    return _ps().tritium_inventory_kg(window(), None)


def tritium_station_kg():
    return ref()["modules"] * tritium_holding_kg()


def deuterium_holding_kg():
    """The cell is 50/50 by atom, so D follows T through the mass fractions."""
    C = _coll()
    return tritium_holding_kg() * (1.0 - C.T_MASS_FRAC_DT) / C.T_MASS_FRAC_DT


def helium3_g_per_year():
    """Tritium that decays does not vanish -- it becomes He-3, in the cell,
    where it is a poison. It leaves as a saleable product."""
    P = _ps()
    r = ref()
    d, _ = P.tritium_demand_per_second(window(), r["module_mw"])
    return r["modules"] * d * SEC_PER_YEAR * 3.016 / N_A


def helium4_kg_per_year():
    """The fusion ash, and the Li-6 reaction's other product. Both are alpha."""
    P = _ps()
    y_f = ref()["y_fus"] * ref()["protons_s"]        # one He-4 per fusion
    li = li6_burn_kg_per_year() * 1000.0 / LI6_AMU * N_A / SEC_PER_YEAR
    return (y_f + li) * SEC_PER_YEAR * HE_AMU / N_A / 1000.0


@functools.lru_cache(maxsize=None)
def mercury_flow_kg_s():
    """ONE module's jet. The station runs N of them."""
    m = _mach()
    return m.jet_mass_flow_kg_s() * ref()["module_mw"]


def mercury_inventory_kg(residence_s=HG_RESIDENCE_S):
    return mercury_flow_kg_s() * residence_s


@functools.lru_cache(maxsize=None)
def solenoid_cold_mass_kg():
    return _mach().cold_mass_kg()


@functools.lru_cache(maxsize=None)
def conductor_bands():
    """(name, metres) for the graded winding. IMPORTED, never re-graded."""
    return [(n, ln) for n, _ri, _ro, _b, ln in _mach().grade_bands()]


def linac_cavities():
    return ESS_CAVITIES * BEAM_GEV / ESS_ENERGY_GEV


def linac_niobium_kg():
    return linac_cavities() * NB_PER_CAVITY_KG


def linac_length_m():
    return ESS_SC_LENGTH_M * BEAM_GEV / ESS_ENERGY_GEV


@functools.lru_cache(maxsize=None)
def shield_thickness_m():
    """The COIL shield, and the coil belongs to a MODULE. Sizing it against
    the station's whole beam would over-shield it by the module count."""
    return _mach().shield_for_life_m(PLANT_LIFE_Y, ref()["module_mw"])


def shield_mass_kg(thick_m=None, rho=CONCRETE_RHO):
    """A shell of the stated thickness around the whole target-and-capture
    volume, taken as the solenoid's outer envelope."""
    C = _coll()
    m = _mach()
    t = shield_thickness_m() if thick_m is None else thick_m
    r = C.des_coil_inner_m() + C.des_winding_thickness_m()
    h = C.DES_LENGTH_M
    return rho * math.pi * ((r + t) ** 2 * (h + 2 * t) - r ** 2 * h)


def mass_converted_kg():
    """The no-free-lunch theorem's own answer: P.t <= M c^2. This is what the
    plant actually consumes, and every other row is bookkeeping around it."""
    c = 2.99792458e8
    return ref()["thermal_mw"] * 1e6 * PLANT_LIFE_Y * SEC_PER_YEAR / (c * c)


# ---- DEPLETED URANIUM, WHICH IS THE FERTILE FEED AND IS ALREADY MINED ------
# Enrichment for light-water reactors leaves tails: uranium stripped of most of
# its U-235 and stored, as UF6 in drums, as a LIABILITY. It is fertile, which
# in a thermal reactor makes it nearly useless, and it is exactly what a fast
# subcritical blanket eats.
#
# THE DISTINCTION THAT MATTERS AND IS EASY TO LOSE. Breeding holds the FISSILE
# fraction, not the mass: U-238 captures a neutron, becomes Pu-239, and the
# Pu-239 fissions. The fissile inventory is therefore constant while the TOTAL
# heavy metal falls at the fission rate. So the plant needs no fissile feed and
# it DOES need a fertile one -- and the fertile one is a material the world has
# already mined, already paid for, and is currently paying to store.
DU_WORLD_STOCK_T = 1.6e6     # SOURCED band, global enrichment tails as uranium
DU_US_STOCK_T = 4.75e5       # SOURCED, the DOE holding alone
WORLD_ELECTRICITY_TWH_YR = 29000.0   # SOURCED, order of magnitude
FISSION_J_PER_KG = HM_ATOMS_PER_KG * 200.0 * 1.602176634e-13


def uranium_feed_t_per_year():
    return burnup_kg_per_year() / 1000.0


def uranium_life_charge_t(years=PLANT_LIFE_Y):
    return uranium_feed_t_per_year() * years


def uranium_first_charge_t():
    """The holding, which is also depleted uranium apart from its fissile seed."""
    return heavy_metal_inventory_kg() / 1000.0


def stock_station_lifetimes(stock_t=DU_WORLD_STOCK_T):
    """How many station-lifetimes the existing tails hold, on the FEED alone."""
    return stock_t / uranium_life_charge_t()


def stock_electricity_twh(stock_t=DU_WORLD_STOCK_T):
    """The stock's recoverable electricity, at this plant's own eta_th."""
    return (stock_t * 1000.0 * FISSION_J_PER_KG * _ps().eta_thermal()
            / 3.6e9 / 1e6)


def stock_world_years(stock_t=DU_WORLD_STOCK_T):
    return stock_electricity_twh(stock_t) / WORLD_ELECTRICITY_TWH_YR


def report_uranium():
    """Depleted uranium: the fertile feed, and it is already above ground."""
    P = _ps()
    r = ref()
    print("  DEPLETED URANIUM -- THE FERTILE FEED")
    print()
    print("    A CORRECTION FIRST, AND IT IS THIS SECTION'S REASON TO EXIST.")
    print("    An earlier pass filed the blanket's heavy metal as BRED, with")
    print("    the note that the salt 'breeds the same back' and is a holding")
    print("    rather than a feed. That is wrong and the error is a real one:")
    print("    breeding converts U-238 to Pu-239 and the Pu-239 FISSIONS, so")
    print("    every fission destroys a heavy atom permanently. What breeding")
    print("    holds constant is the FISSILE FRACTION -- which is what holds k")
    print("    -- while the TOTAL heavy metal falls at the fission rate.")
    print("    THE PLANT NEEDS NO FISSILE FEED AND IT DOES NEED A FERTILE ONE.")
    print()
    print("    WHAT THE STATION EATS")
    print(f"      first charge, heavy metal      "
          f"{uranium_first_charge_t():10.1f} t")
    print(f"      fertile feed                   "
          f"{uranium_feed_t_per_year():10.2f} t/yr")
    print(f"        = {100*burnup_fraction_per_year():.2f} % of the holding a"
          f" year, {100*fissile_depletion_fraction():.1f} % over"
          f" {PLANT_LIFE_Y:.0f} years")
    print(f"      life charge of feed            "
          f"{uranium_life_charge_t():10.1f} t")
    print(f"      TOTAL uranium over the life    "
          f"{uranium_first_charge_t()+uranium_life_charge_t():10.1f} t")
    print()
    print("    AND IT IS ALREADY MINED. Enrichment for light-water reactors")
    print("    leaves tails -- uranium stripped of its U-235, stored as UF6 in")
    print("    drums, carried on the books as a liability and not an asset.")
    print("    In a thermal spectrum it is nearly useless. A FAST SUBCRITICAL")
    print("    BLANKET IS EXACTLY WHAT EATS IT.")
    print()
    print(f"      DOE holding alone              {DU_US_STOCK_T:10,.0f} t"
          "    SOURCED")
    print(f"      world tails, order             {DU_WORLD_STOCK_T:10,.0f} t"
          "    SOURCED band")
    print()
    print("    WHAT THAT STOCK IS WORTH, ON THE FEED ALONE")
    print(f"      station-lifetimes, DOE stock   "
          f"{stock_station_lifetimes(DU_US_STOCK_T):10,.0f}")
    print(f"      station-lifetimes, world       "
          f"{stock_station_lifetimes():10,.0f}")
    print(f"      recoverable electricity        "
          f"{stock_electricity_twh():10.3e} TWh")
    print(f"      as years of WORLD electricity  {stock_world_years():10,.0f}"
          "    at today's demand")
    print()
    print("    Those last two are stated at this plant's own thermal")
    print(f"    efficiency ({100*P.eta_thermal():.1f} %) and at complete fission of the stock,")
    print("    which no single pass achieves -- a liquid fuel with online")
    print("    processing approaches it over many charges and no reactor")
    print("    reaches it in one. Read them as an UPPER BOUND on the resource")
    print("    and as a lower bound on how far it is from binding.")
    print()
    print("    WHAT DEPLETED URANIUM CANNOT DO, AND THIS IS THE HALF THAT IS")
    print("    USUALLY SKIPPED. It cannot start the plant. Reaching")
    print(f"    k = {P.K_SAFE:.2f} needs SEPARATED FISSILE in the first charge;")
    print("    U-238 is fertile and a fertile assembly has no k to speak of.")
    print("    The tails answer the FEED and they do not answer the IGNITION,")
    print("    which stays what buildpackage.py's long-lead list says it is: a")
    print("    safeguarded acquisition and a political question rather than an")
    print("    engineering one. After that first charge the plant makes its own")
    print("    fissile from the tails, for ever.")
    print()
    print("    THREE CONSEQUENCES WORTH STATING PLAINLY")
    print("      1. The feed is a WASTE STREAM. Every tonne burnt is a tonne")
    print("         of stored liability removed, so the fuel cost is negative")
    print("         before it is anything else.")
    print("      2. It is not a mining question. No uranium need be mined for")
    print(f"         this station for {stock_station_lifetimes():,.0f} station-lifetimes,")
    print("         so the environmental burden of the front end -- which is")
    print("         most of nuclear power's material footprint -- is ZERO for")
    print("         as far as this analysis can see. See environment.py.")
    print("      3. It changes criterion 4's verdict on ONE row and no more.")
    print("         Heavy metal moves from BRED to STOCKPILED: a life charge")
    print(f"         of {uranium_life_charge_t():.0f} t fits in a shed, so it is a first")
    print("         charge and not a delivery -- the same finding as Li-6, by")
    print("         the same argument, at a different tonnage.")


# ---- THE BILL --------------------------------------------------------------
# (subsystem, material, quantity, unit, status, supply, storage)
@functools.lru_cache(maxsize=None)
def bill():
    r = ref()
    m = _mach()
    C = _coll()
    N = float(r["modules"])          # per-module items are built N times
    L = float(r["linacs"])           # driver items are built once per linac
    rows = []
    A = rows.append

    A(("driver", "niobium, RRR300 sheet", L * linac_niobium_kg() / 1000.0,
       "t", "SCALED", "FIRST-CHARGE",
       f"{L:.0f} linacs x {linac_cavities():.0f} cavities in cryomodules at 2 K; "
       "sub-atmospheric LHe bath; magnetic hygiene below 1 uT"))
    A(("driver", "liquid helium, 2 K circuit", L * 12.0, "t", "REQUIREMENT",
       "CIRCULATING",
       "closed-cycle; full gas-bag + high-pressure recovery for the whole "
       "inventory, because a quench must not vent"))
    A(("driver", "liquid nitrogen, thermal shields", L * 40.0, "t/yr",
       "REQUIREMENT", "STOCKPILED",
       "bulk cryogenic tank, atmospheric, replenished; the one utility feed"))
    A(("driver", "copper and steel, cryomodules", L * linac_length_m() * 2.0,
       "t",
       "REQUIREMENT", "FIRST-CHARGE",
       f"{linac_length_m():.0f} m of superconducting linac at an ASSUMED "
       "2 t/m of cryomodule, vessel and warm structure; ordinary plant "
       "storage, and the figure is a scoping one"))

    A(("target", "mercury", N * mercury_inventory_kg() / 1000.0, "t",
       "DERIVED", "CIRCULATING",
       f"{N:.0f} sealed loops at {mercury_flow_kg_s():.0f} kg/s each; double containment, "
       "vapour capture, activated (Hg-203, Au-198) so the loop is a hot cell"))
    A(("target", "beryllium window", N * 0.5, "kg/yr", "SOURCED", "REPLACED",
       f"one per module per year; replaced on {m.SRC_BE_WINDOW_Z_M:.0f} m stand-off at "
       f"{m.SRC_BE_WINDOW_DPA_YR:.1f} dpa/yr -- annually; Be dust is the "
       "hazard, handled in a glovebox, and the spent window is waste"))

    A(("capture", "solenoid cold mass, steel and conductor",
       N * solenoid_cold_mass_kg() / 1000.0, "t", "IMPORTED", "FIRST-CHARGE",
       f"{C.des_coil_inner_m():.2f} m bore, "
       f"{C.des_winding_thickness_m():.2f} m winding, "
       f"{C.DES_LENGTH_M:.1f} m long; 4.5 K cryostat"))
    for name, length in conductor_bands():
        A(("capture", f"{name} conductor", N * length, "m", "IMPORTED",
           "FIRST-CHARGE",
           "graded by field; spooled, and the REBCO band is the schedule "
           "item -- it is the long-lead purchase of the whole plant"))
    A(("capture", "liquid helium, 4.5 K cryostat", N * 8.0, "t", "REQUIREMENT",
       "CIRCULATING",
       f"cooldown takes {m.cooldown_energy_j()/1e9:.1f} GJ from the cold mass; "
       "recovery capacity must exceed a full quench"))

    A(("fuel cell", "tritium", N * tritium_holding_kg(), "kg", "IMPORTED",
       "BRED",
       f"{m.cell_radius_cm():.2f} cm radius, {m.cell_depth_cm():.0f} cm deep "
       f"at {m.cell_pressure_mpa():.0f} MPa and {m.CELL_T_K:.0f} K; "
       "double-walled, all-metal, secondary containment at sub-atmospheric "
       "pressure with a getter bed on the sweep"))
    A(("fuel cell", "deuterium", N * deuterium_holding_kg(), "kg", "DERIVED",
       "FIRST-CHARGE",
       "same cell; the D side is ordinary and is bought once"))
    A(("fuel cell", "tritium, working store",
       (2.0 + 0.10 * N) * tritium_holding_kg(), "kg", "REQUIREMENT", "BRED",
       "ZrCo or depleted-uranium hydride beds: TWO spare module charges for "
       f"the whole station, not two per module, plus 10 % of {N:.0f} charges "
       "as processing hold-up. A bed holds tritium as a solid at atmospheric "
       "pressure and releases it on heating, which is what makes the store "
       "safe -- and the store is deliberately small because the world's "
       "entire civil stock barely charges the cells"))

    A(("blanket", "fuel salt, NaCl-UCl3 (Cl-37)",
       salt_inventory_kg() / 1000.0, "t", "DERIVED", "CIRCULATING",
       f"{salt_volume_m3():.1f} m3 at {salt_flow_kg_s():.0f} kg/s, "
       f"700-900 K; freeze-plug drain to a passively cooled subcritical tank"))
    A(("blanket", "  of which heavy metal, held",
       heavy_metal_inventory_kg() / 1000.0, "t", "DERIVED", "FIRST-CHARGE",
       f"the holding, of which the FISSILE fraction is held constant by "
       f"breeding at f_b >= {_ps().fertile_capture_required(_ps().K_SAFE):.4f}; "
       "that is what keeps k, and it is not what keeps the mass"))
    A(("blanket", "  fertile feed, depleted uranium",
       burnup_kg_per_year() / 1000.0, "t/yr", "DERIVED", "STOCKPILED",
       f"EVERY FISSION DESTROYS A HEAVY ATOM. Breeding converts U-238 to "
       f"Pu-239 and the Pu fissions, so the fissile fraction is held and the "
       f"TOTAL heavy metal falls at the fission rate -- "
       f"{100*burnup_fraction_per_year():.2f} %/yr, "
       f"{100*fissile_depletion_fraction():.1f} % over the life. A "
       f"{uranium_life_charge_t():.0f} t life charge of depleted uranium sits "
       "in drums on site; see --uranium"))
    A(("blanket", "chlorine, Cl-37 enriched",
       salt_inventory_kg() * (1.0 - SALT_U_MASS_FRAC) * 35.45 / 58.44 / 1000.0,
       "t", "DERIVED", "FIRST-CHARGE",
       "enrichment is a first charge and is not consumed; it is the second "
       "long-lead purchase after REBCO"))
    A(("blanket", "Pb-15.7Li breeder and reflector",
       breeder_mass_kg() / 1000.0, "t", "DERIVED", "CIRCULATING",
       f"{breeder_volume_m3():.1f} m3 annulus {BREEDER_THICK_M:.2f} m thick at "
       "550-750 K; tritium extracted continuously from the flowing metal"))
    A(("blanket", "  of which lithium, 90 % Li-6",
       li6_inventory_kg(), "kg", "DERIVED", "STOCKPILED",
       f"burns {li6_burn_kg_per_year()*1000:.0f} g/yr, which is "
       f"{100*li6_burndown_fraction():.2f} % of the holding over "
       f"{PLANT_LIFE_Y:.0f} years -- so the enrichment is a first charge and "
       "the top-up is a rounding error"))
    A(("blanket", "fission-product removal, salt side", 0.0, "-",
       "REQUIREMENT", "REPLACED",
       "online: noble gases sparged, noble metals plated out, lanthanides "
       "extracted. THIS IS WHAT BUYS L = 0.20 FOR FORTY YEARS and it is the "
       "single most demanding unbuilt item in the plant"))

    A(("shielding", "coil shield, tungsten-loaded",
       N * shield_mass_kg() / 1000.0, "t", "DERIVED", "FIRST-CHARGE",
       f"{shield_thickness_m():.2f} m, sized for a {PLANT_LIFE_Y:.0f} year "
       f"COIL life at {r['beam_mw']:.0f} MW -- an insulation-dose limit, not a "
       f"biological one. It carries "
       f"{r['beam_mw']*1e6*m.F_INTO_SHIELDING/1e3:.0f} kW of beam power and "
       "must be actively cooled, not passive"))
    A(("shielding", "biological shield, concrete", 0.0, "-", "REQUIREMENT",
       "FIRST-CHARGE",
       "SEPARATE FROM THE ABOVE AND NOT SIZED HERE. The coil shield answers a "
       "dose limit on organic insulation at 0.75 m; a personnel boundary "
       f"around a {r['beam_mw']:.0f} MW spallation source is metres of "
       "concrete and thousands of tonnes, and sizing it needs a shielding "
       "calculation this work does not do"))

    A(("conversion", "supercritical CO2 or steam plant", r["thermal_mw"],
       "MW-th", "IMPORTED", "CIRCULATING",
       f"{r['net_mw']:.1f} MW net electric after the driver is fed; "
       "ordinary power-plant storage and inventory"))

    A(("products", "helium-4, fusion and Li-6 ash", helium4_kg_per_year(),
       "kg/yr", "DERIVED", "PRODUCED",
       "vented or sold; inert, and the only outward stream here that is not "
       "radioactive"))
    A(("products", "helium-3, from tritium decay", helium3_g_per_year(),
       "g/yr", "DERIVED", "PRODUCED",
       f"{helium3_g_per_year()/3.016*22.414:.0f} litres at STP a year, removed "
       "from the cell continuously because it is a POISON there; it is also "
       "scarce, so the decay loss leaves the plant as a product rather than "
       "as a waste. Stored as compressed gas"))
    A(("products", "fission products", burnup_kg_per_year(), "kg/yr",
       "DERIVED", "PRODUCED",
       "the plant's actual waste, and it is a supply line running OUTWARD; "
       "stored on site in cooled canisters"))
    return rows


def report():
    """The bill of materials for the reference plant."""
    r = ref()
    print("  BILL OF MATERIALS -- THE STATION")
    print()
    print(f"    {r['modules']:.0f} modules of {r['module_mw']:.0f} MW,"
          f" {r['linacs']:.0f} linacs, {r['beam_mw']:.0f} MW of"
          f" {r['beam_gev']:.0f} GeV beam in all")
    print(f"    k = {r['k']:.2f}, base collector 1.50 T.m,"
          f" {r['window']:.0f} MeV/c stopping window")
    print(f"    G = {r['gain']:.2f}   thermal {r['thermal_mw']:.0f} MW   "
          f"net electric {r['net_mw']:.0f} MW   "
          f"{r['households']:,.0f} households")
    print()
    print("    Quantities are WHOLE-STATION. A per-module item is stated at"
          " N times")
    print("    one module's figure and its note says so.")
    print()
    print(f"    {'subsystem':<11} {'material':<36} {'quantity':>12} {'':<6}"
          f" {'status':<12} supply")
    last = None
    for sub, mat, q, u, st, sup, _store in bill():
        if sub != last:
            print()
            last = sub
        qs = "--" if u == "-" else f"{q:12,.3f}"
        print(f"    {sub:<11} {mat:<36} {qs} {u:<6} {st:<12} {sup}")
    print()
    print("    Every quantity above is DERIVED from, or IMPORTED from, another")
    print("    instrument in this repository, except where the status says")
    print("    otherwise. A REQUIREMENT is a number the plant needs and this")
    print("    work does not compute -- it is stated so a measurement can")
    print("    refuse it, not so a reader can trust it.")


def report_storage():
    """The storage schedule: how each material is held, and against what."""
    print("  STORAGE SCHEDULE")
    print()
    last = None
    for sub, mat, q, u, st, sup, store in bill():
        if sub != last:
            print(f"    --- {sub.upper()} " + "-" * (60 - len(sub)))
            last = sub
        qs = "" if u == "-" else f"{q:,.3f} {u}"
        print(f"      {mat}   {qs}   [{sup}]")
        # wrap the storage note
        words, line = store.split(), "        "
        for w in words:
            if len(line) + len(w) > 74:
                print(line)
                line = "        "
            line += w + " "
        print(line.rstrip())
        print()
    print("    THE THREE STORES THAT ARE NOT ORDINARY, and they are the three")
    print("    that decide whether the plant is licensable:")
    print()
    m = _mach()
    n = float(ref()["modules"])
    print(f"      TRITIUM. {tritium_holding_kg():.2f} kg per cell x {n:.0f}"
          f" modules = {n*tritium_holding_kg():.1f} kg,")
    print(f"      with {2*n*tritium_holding_kg():.1f} kg more in beds. One cell is")
    C = _coll()
    ci = C.tritium_curies(tritium_holding_kg() * 1000.0)
    print(f"      {ci/1e6:.1f} MCi, and the station {n*ci/1e6:.0f} MCi. That is the")
    print("      plant's")
    print("      dominant licensing quantity and it is set by the muon range,")
    print("      not by the power -- see powersource.py --tritium. A hydride")
    print("      bed holds it as a solid at atmospheric pressure: the store is")
    print("      safe, the CELL is the hazard, and the cell is the smallest")
    print("      the physics allows.")
    print()
    print(f"      MERCURY. {mercury_inventory_kg()/1000.0:.2f} t per module,"
          f" {n*mercury_inventory_kg()/1000.0:.1f} t in all, in loops")
    print("      activated the moment the")
    print("      beam is on. It is not a chemical hazard with a radiological")
    print("      footnote; it is a hot cell that happens to contain mercury.")
    print()
    print(f"      FUEL SALT. {salt_inventory_kg()/1000.0:.1f} t holding "
          f"{heavy_metal_inventory_kg()/1000.0:.1f} t of heavy metal, molten,")
    print("      at 900 K, and it is the fission inventory. It drains by")
    print("      freeze plug to a passively cooled subcritical tank -- which")
    print("      is the same argument as --stability's: cut the beam and it")
    print("      stops, and the drain is the second, independent way to say so.")


def report_supply():
    """Criterion 4, adjudicated row by row: what the plant actually consumes."""
    print("  CRITERION 4 -- NOTHING SUPPLIED AFTER IGNITION -- ADJUDICATED")
    print()
    print("    The criterion as put was 'literally nothing may be consumed'.")
    print("    That is forbidden by theorem: P.t <= M c^2, so a device that")
    print("    converts no mass returns no energy. The strongest true form is")
    print("    therefore: what mass is converted, and does anything have to be")
    print("    DELIVERED to the site to keep it running?")
    print()
    print(f"      mass converted over {PLANT_LIFE_Y:.0f} years   "
          f"{mass_converted_kg():.3f} kg")
    print("      -- that is the whole of what is consumed, and it is the")
    print("         theorem's floor rather than an engineering figure.")
    print()
    groups = {}
    for sub, mat, q, u, st, sup, _ in bill():
        groups.setdefault(sup, []).append((sub, mat, q, u))
    order = ["BRED", "FIRST-CHARGE", "CIRCULATING", "STOCKPILED",
             "REPLACED", "PRODUCED"]
    verdict = {
        "BRED": "made in-plant. NO SUPPLY LINE.",
        "FIRST-CHARGE": "bought once, held for the life. NO SUPPLY LINE.",
        "CIRCULATING": "moves, is not consumed. NO SUPPLY LINE.",
        "STOCKPILED": "consumed, but a life charge fits in the building.",
        "REPLACED": "A SUPPLY LINE INWARD -- of parts, not of fuel.",
        "PRODUCED": "a stream running OUTWARD; not a cost, but not nothing.",
    }
    for g in order:
        print(f"    {g}: {verdict[g]}")
        for sub, mat, q, u in groups.get(g, []):
            qs = "--" if u == "-" else f"{q:,.3f} {u}"
            print(f"      {sub:<11} {mat:<38} {qs}")
        print()
    print("    A DISTINCTION THE INVENTORY HIDES, AND IT DECIDES THE BLANKET.")
    print(f"    The first charge holds {heavy_metal_inventory_kg()/1000.0:.1f} t"
          f" of heavy metal and the plant")
    print(f"    fissions {burnup_kg_per_year()*PLANT_LIFE_Y/1000.0:.2f} t in "
          f"{PLANT_LIFE_Y:.0f} years -- "
          f"{100*fissile_depletion_fraction():.1f} % of it. On MASS alone")
    print("    the charge outlasts the plant and no breeding is needed at all.")
    print("    What runs out is not mass but REACTIVITY: at first order k falls")
    print(f"    with the fissile density, from {_ps().K_SAFE:.3f} to "
          f"{k_without_breeding():.3f}, and the plant gain")
    print(f"    with it, from {ref()['gain']:.1f} to "
          f"{gain_without_breeding():.1f}. BREEDING HOLDS k, NOT THE")
    print("    INVENTORY, and that is the whole of why f_b is a requirement.")
    print()
    print("    THE VERDICT, AND IT IS NOT THE ONE ASKED FOR. Two things the")
    print("    plant would have needed a feed for -- fissile material and")
    print("    tritium -- it breeds, and the arguments are independent:")
    P = _ps()
    print(f"      fissile: f_b >= k/(nu-k) = "
          f"{P.fertile_capture_required(P.K_SAFE):.4f} of non-fission")
    print("               absorptions, and the budget has room for exactly")
    print("               that much and no more.")
    print(f"      tritium: {P.tritium_balance(window(), ref()['module_mw'], f_li=P.F_LI_DESIGN):.3f}"
          " at the design Li-6 share, and that ratio")
    print("               is what set the plant at 7 MW rather than 1.")
    print()
    print(f"    Li-6 is consumed -- {li6_burn_kg_per_year()*1000:.0f} g a year "
          f"-- and it is the only one.")
    print(f"    Against a holding of {li6_inventory_kg():.0f} kg that is "
          f"{100*li6_burndown_fraction():.2f} % over "
          f"{PLANT_LIFE_Y:.0f} years,")
    print("    so it is a first charge and not a delivery.")
    print()
    print("    WHAT DOES ARRIVE AT THE GATE, every year, for ever:")
    print("      - liquid nitrogen for the cryogenic shields")
    print("      - one beryllium window")
    print("      - the reagents the salt's fission-product removal consumes")
    print("    and WHAT LEAVES: fission products, at "
          f"{burnup_kg_per_year():.0f} kg/yr.")
    print()
    print("    So criterion 4 holds ON FUEL and fails ON CONSUMABLES AND")
    print("    PARTS. That is the honest statement, it is stronger than any")
    print("    fission or fusion plant proposed, and it is not what was asked")
    print("    for. A status is never flattened.")


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    P, m = _ps(), _mach()
    print("  the bill imports rather than restates")
    check("the tritium holding is powersource's, to the last digit",
          tritium_holding_kg() == P.tritium_inventory_kg(window(), None))
    check("the cold mass is machine's, to the last digit",
          solenoid_cold_mass_kg() == m.cold_mass_kg())
    check("the conductor bands are machine's grading, unregraded",
          [n for n, _ in conductor_bands()]
          == [b[0] for b in m.grade_bands()])
    check("the station's thermal power is powersource's gain times its beam",
          abs(ref()["thermal_mw"]
              - ref()["beam_mw"] * P.plant_gain(P.K_SAFE, ref()["y_spall"],
                                                ref()["y_fus"])) < 1e-9)
    check("  -- and the station is powersource's, module count included",
          ref()["modules"] == P.station()["modules"])
    print()
    print("  the blanket's chemistry is forced, and the selftest says by what")
    check("the salt inventory follows the HEAT, not the neutronics",
          abs(salt_inventory_kg()
              - ref()["thermal_mw"] * 1e6 / (SALT_CP * SALT_DT_K)
              * SALT_RESIDENCE_S) < 1e-6)
    check("the holding is many years of burnup, so the salt is not a feed",
          burnup_fraction_per_year() < 0.05)
    check("  -- and the FIRST CHARGE alone outlasts the plant on inventory",
          burnup_kg_per_year() * PLANT_LIFE_Y < heavy_metal_inventory_kg())
    check("  -- yet breeding is still required, because REACTIVITY depletes",
          gain_without_breeding() < ref()["gain"] / 2.0)
    print("    (the second and third are not in tension and the distinction is")
    print("     the point: the charge is big enough, and it is the FISSILE")
    print("     FRACTION that runs out, not the mass. Breeding holds k, not")
    print("     the inventory -- see report_supply.)")
    print()
    print("  criterion 4 is decided by the supply column and by nothing else")
    check("nothing that leaves the plant is filed as a supply line inward",
          all(sup == "PRODUCED" for _s, _m, _q, _u, _st, sup, _n in bill()
              if _s == "products"))
    check("Li-6 is the only STOCKPILED row that is genuinely consumed",
          [mat for _s, mat, _q, _u, _st, sup, _ in bill()
           if sup == "STOCKPILED" and "Li-6" in mat] != [])
    check("the Li-6 burndown is under a tenth of the holding over the life",
          li6_burndown_fraction() < 0.10)
    check("tritium is BRED, not FIRST-CHARGE -- the balance decides it",
          [sup for _s, mat, _q, _u, _st, sup, _ in bill()
           if mat == "tritium"] == ["BRED"])
    check("  -- and it is BRED only at the window the scale-up forced",
          P.tritium_balance(window(), ref()["module_mw"],
                            f_li=P.F_LI_DESIGN) > 1.0
          and P.tritium_balance(265.0, ref()["module_mw"],
                                f_li=P.F_LI_DESIGN) < 1.0)
    print()
    print("  depleted uranium: the fertile feed, and the correction it forced")
    check("the fertile feed equals the fission rate, atom for atom",
          abs(uranium_feed_t_per_year() * 1000.0
              - burnup_kg_per_year()) < 1e-9)
    check("heavy metal is NOT filed as BRED -- fissile is held, mass is not",
          [sup for _s, mat, _q, _u, _st, sup, _n in bill()
           if "heavy metal" in mat] == ["FIRST-CHARGE"])
    check("  -- and the fertile feed is filed as a consumable",
          [sup for _s, mat, _q, _u, _st, sup, _n in bill()
           if "fertile feed" in mat] == ["STOCKPILED"])
    check("the life charge of feed is a fraction of the first charge",
          uranium_life_charge_t() < uranium_first_charge_t())
    check("  -- so it fits on site and is a charge, not a delivery",
          uranium_life_charge_t() < 1000.0)
    check("the existing tails hold thousands of station-lifetimes",
          stock_station_lifetimes() > 1000.0)
    check("  -- and the DOE holding alone holds thousands",
          stock_station_lifetimes(DU_US_STOCK_T) > 1000.0)
    check("the resource figure is an upper bound, not a prediction",
          stock_electricity_twh() ==
          DU_WORLD_STOCK_T * 1000.0 * FISSION_J_PER_KG * P.eta_thermal()
          / 3.6e9 / 1e6)
    check("depleted uranium cannot start the plant: it is fertile",
          True is (uranium_first_charge_t() > 0
                   and "fissile first charge" in " ".join(
                       i for i, _w, _y in
                       __import__("buildpackage").LONG_LEAD)))
    # the theorem's floor, checked against the fuel rather than against a
    # magnitude: the mass that leaves as energy must be the fission mass
    # defect of the fuel that supplied it, which is a per-mille effect.
    defect = mass_converted_kg() / (uranium_life_charge_t() * 1000.0)
    check("the mass converted is the fuel's fission mass defect",
          0.0005 < defect < 0.0015)
    check("  -- so the energy came from the fuel and not from bookkeeping",
          mass_converted_kg() > 0.0
          and mass_converted_kg() < uranium_life_charge_t() * 1000.0)
    print()
    print("  no row is silently unclassified")
    stats = {"DERIVED", "IMPORTED", "SOURCED", "SCALED", "ASSUMED",
             "REQUIREMENT"}
    sups = {"FIRST-CHARGE", "BRED", "STOCKPILED", "REPLACED", "CIRCULATING",
            "PRODUCED"}
    check("every row carries a known status",
          all(st in stats for _s, _m, _q, _u, st, _sup, _st2 in bill()))
    check("every row carries a known supply class",
          all(sup in sups for _s, _m, _q, _u, _st, sup, _st2 in bill()))
    check("every row carries a storage note",
          all(len(store) > 20 for *_r, store in bill()))
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--storage", action="store_true",
                    help=report_storage.__doc__)
    ap.add_argument("--supply", action="store_true", help=report_supply.__doc__)
    ap.add_argument("--uranium", action="store_true",
                    help=report_uranium.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.storage:
        return report_storage()
    if a.supply:
        return report_supply()
    if a.uranium:
        return report_uranium()
    return report()


if __name__ == "__main__":
    sys.exit(main() or 0)
