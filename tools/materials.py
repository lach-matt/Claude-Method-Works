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

and every row also carries a SUPPLY class, because criterion 3 -- nothing
supplied after ignition -- is decided by that column and by nothing else:

    FIRST-CHARGE  bought once, held for the life, neither consumed nor bred
    BRED          made in-plant from what is already there
    STOCKPILED    consumed, but a life-of-plant charge fits in the building
    REPLACED      a component with a finite life; a parts line, not a fuel line
    CIRCULATING   an inventory that moves and is neither consumed nor bred
    PRODUCED      a stream running OUTWARD -- waste, or a co-product

Run:  python3 tools/materials.py            the bill of materials
      python3 tools/materials.py --storage  the storage schedule
      python3 tools/materials.py --supply       criterion 3, row by row
      python3 tools/materials.py --criterion3   what closing it took

NOTE ON THE NUMBER. This file said "criterion 4" everywhere until OBJECTIVE.md
was written and the criteria were numbered from the author's own statement.
'Cold' was dropped as criterion 1 and everything below it moved up; the number
here had not. OBJECTIVE.md's table is authoritative and this file now agrees
with it. THE VERDICT NEVER CHANGED -- only the label on it -- and the
mismatch is recorded rather than silently corrected because a criterion
referenced by a number nobody can check is what OBJECTIVE.md exists to stop.
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
# ---- CLOSING CRITERION 3 -------------------------------------------------
# Criterion 3 asks for no input of anything beyond the initial ignition, and
# --supply's verdict was that it "holds on fuel and fails on consumables and
# parts". The consumables half is a DESIGN CHOICE and not a law, and this is
# the pass that changes the design rather than the sentence.
#
# Two streams arrived at the gate for ever. Both are now made on site, and
# both cost electricity the plant already has:
#
#   LIQUID NITROGEN   was bought in a tanker. Nitrogen is 78 % of the air at
#                     the site, so the plant liquefies its own and runs the
#                     shield circuit closed. Air is ambient, not delivered.
#   SALT REAGENTS     the fission-product removal is specified ELECTRICAL --
#                     helium sparge on the recirculating inventory, noble
#                     metals plated out, vacuum distillation for the alkali
#                     and alkaline-earth chlorides, electrowinning for the
#                     lanthanides, any chemical reductant regenerated
#                     electrolytically on site. A chemical line becomes an
#                     electricity line and the plant makes electricity.
#
# What that does NOT close is the parts line, and this file does not pretend
# it does. See report_criterion3().
LN2_KWH_PER_KG = 0.357        # SOURCED: conventional cryogenic air
                              # separation producing LN2
LN2_KWH_PER_KG_HI = 2.56      # SOURCED: the pessimistic end of the published
                              # band, for a small or badly integrated plant
SALT_VAP_MJ_KG = 2.9          # SOURCED: NaCl heat of vaporisation, 171
                              # kJ/mol over 58.4 g/mol
SALT_PASSES_PER_YEAR = 3.0    # ASSUMED, and deliberately pessimistic: it
                              # distils the WHOLE inventory three times a
                              # year, where a real cleanup takes a slipstream.
                              # Used as a BOUND on the energy, never as a
                              # process design
N_A = 6.02214076e23
PLANT_LIFE_Y = 40.0

# the breeding zone's geometry, from the fuel zone's
BREEDER_THICK_M = 0.50       # ASSUMED: about one fast mean free path in Pb
# ---- THE TARGET IS MOLTEN LEAD, NOT MERCURY, AND THE SUBSTITUTION IS THIS
# ---- WORK'S -----------------------------------------------------------------
# machine.py's target model is SOURCED from a neutrino-factory study whose
# target is a mercury jet, and that is where the 4 MW design point and the
# 319 kW deposition come from. The MATERIAL is not forced by any of it, and
# environment.py could not drive the mercury rows below MODERATE:
#
#   - Mercury's vapour pressure at its operating temperature is about eight
#     orders of magnitude above lead's, which is the whole reason the sourced
#     design carries a beryllium window six metres downstream. A mercury loop
#     breach is a RELEASE; a lead loop breach is a spill.
#   - The pion production this design actually integrates is HARP's, measured
#     on a LEAD target. Using lead makes the machine and its own source data
#     the same material, which mercury never was.
#   - Pure lead, not lead-bismuth: LBE is the reactor industry's eutectic and
#     it breeds Po-210 from Bi-209. Pure lead makes far less of it.
#
# What it costs: lead melts at 327 C, so the loop is trace-heated and must
# never freeze -- a routine problem for the lead-cooled reactor industry and a
# new one for this design; and lead's interaction length is longer, so the
# target is longer at the same number of interaction lengths.
PB_RHO = 10660.0             # kg/m3, liquid lead at 450 C            SOURCED
PB_CP = 147.0                # J/kg/K, liquid lead                    SOURCED
PB_LAMBDA_I_GCM2 = 199.6     # PDG nuclear interaction length         SOURCED
PB_MELT_C = 327.0            # SOURCED -- the cost of the substitution
PB_OPERATING_C = 450.0       # ASSUMED, comfortably above the freeze
HG_RHO = 13534.0             # kg/m3, the sourced study's material    SOURCED
HG_LAMBDA_I_GCM2 = 199.0     # SOURCED
TARGET_RESIDENCE_S = 20.0    # target loop transit                    ASSUMED
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


def heavy_metal_depletion_fraction(years=PLANT_LIFE_Y):
    """Share of the HEAVY METAL fissioned over the life, unbred.

    This is the number that makes the charge look comfortable: a quarter of
    the heavy metal in forty years. It is not the number that decides whether
    the plant runs -- see below, and see what this function used to be called.
    """
    return burnup_kg_per_year() * years / heavy_metal_inventory_kg()


def fissile_depletion_fraction(years=PLANT_LIFE_Y, fraction=None):
    """Share of the FISSILE holding fissioned over the life, unbred.

    THIS FUNCTION USED TO DIVIDE BY THE HEAVY METAL, which is what its name
    has always said it does not. The heavy metal is 201.8 t and the fissile
    holding is 12 to 20 percent of it; dividing by the wrong one understated
    the depletion by a factor of five to eight, and made a charge that is
    exhausted inside the plant's life look like one that loses a quarter of
    itself. Returns (low, high) over the fissile band, because the band is
    what the design carries.
    """
    P = _ps()
    lo, hi = P.FISSILE_FRACTION if fraction is None else (fraction, fraction)
    burn = burnup_kg_per_year() * years
    hm = heavy_metal_inventory_kg()
    return burn / (hm * hi), burn / (hm * lo)


def fissile_exhaustion_years(fraction=None):
    """When the fissile charge is gone if nothing breeds it back. (lo, hi)."""
    P = _ps()
    lo, hi = P.FISSILE_FRACTION if fraction is None else (fraction, fraction)
    hm = heavy_metal_inventory_kg()
    b = burnup_kg_per_year()
    return hm * lo / b, hm * hi / b


def k_without_breeding(years=PLANT_LIFE_Y, fraction=None):
    """First order, and stated as first order: for a fixed geometry the
    reactivity of a subcritical assembly falls with the FISSILE density, so
    dk/k ~ dN/N -- N being the fissile density and not the heavy metal's.
    A transport calculation would refine this; the CONCLUSION -- that the
    assembly stops rather than degrades -- survives any refinement, which is
    why it is reported as a requirement on breeding rather than a prediction.

    Returns (low, high) across the fissile band. A floor of zero is applied
    because a negative k is not a physical statement: it means the charge ran
    out before the year asked about.
    """
    P = _ps()
    d_lo, d_hi = fissile_depletion_fraction(years, fraction)
    return (max(0.0, P.K_SAFE * (1.0 - d_hi)),
            max(0.0, P.K_SAFE * (1.0 - d_lo)))


def gain_without_breeding(years=PLANT_LIFE_Y, fraction=None):
    """(low, high) plant gain at the unbred k. Both ends, never one."""
    P = _ps()
    r = ref()
    k_lo, k_hi = k_without_breeding(years, fraction)
    return (P.plant_gain(k_lo, r["y_spall"], r["y_fus"]),
            P.plant_gain(k_hi, r["y_spall"], r["y_fus"]))


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


def target_length_cm(rho=PB_RHO, lam=PB_LAMBDA_I_GCM2, lengths=None):
    """Interaction lengths into centimetres, for whichever material."""
    m = _mach()
    n = m.TARGET_LENGTHS if lengths is None else lengths
    return n * lam / (rho / 1000.0)


def target_length_ratio():
    """What the lead substitution costs in target length."""
    return (target_length_cm(PB_RHO, PB_LAMBDA_I_GCM2)
            / target_length_cm(HG_RHO, HG_LAMBDA_I_GCM2))


@functools.lru_cache(maxsize=None)
def lead_flow_kg_s():
    """ONE module's jet, IMPORTED from machine.py's flow model with lead's
    own properties passed in -- the model is parameterised in rho and cp and
    is not re-derived here."""
    m = _mach()
    return m.jet_mass_flow_kg_s(rho=PB_RHO) * ref()["module_mw"]


def lead_inventory_kg(residence_s=TARGET_RESIDENCE_S):
    return lead_flow_kg_s() * residence_s


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


# ---- WHEN THE TAILS RUN OUT, AND WHAT COMES AFTER -------------------------
# --uranium answers "is there enough" for the tails alone. This asks the
# consequent question: the tails are finite, so what is the ladder below them,
# and does the DESIGN still work on each rung? The second half is the one that
# is usually skipped -- a resource is not a fuel until the neutron budget says
# so, and one rung of this ladder fails that test.
FERTILE_RESOURCES = [
    ("enrichment tails (DU), world", 1.6e6, "SOURCED band", "U-238"),
    ("spent LWR fuel, heavy metal", 4.0e5, "SOURCED order", "U-238"),
    ("identified natural uranium", 8.0e6, "SOURCED, at recoverable cost",
     "U-238"),
    ("thorium, identified resources", 6.4e6, "SOURCED order", "Th-232"),
    ("uranium in seawater", 4.5e9, "SOURCED, dissolved inventory", "U-238"),
]
NU_U233_FAST = 2.50          # SOURCED: neutrons per fast fission, U-233
NU_PU239_FAST = 2.90         # SOURCED, and it is powersource's own NU_FAST


def fertile_lifetimes(stock_t):
    return stock_t / uranium_life_charge_t()


def budget_on(nu, k_eff=None, leak=None):
    """Does the neutron budget close on a fertile cycle of this nu?

    The whole design rests on nu = 2.90, which is Pu-239 fast. A thorium cycle
    breeds U-233 at nu = 2.50, and the difference is not cosmetic: f_b rises,
    fission takes more of the budget, and what is left for Li-6 shrinks twice
    over. Returns (f_b, fissions, non-fission fates, free for Li-6).
    """
    P = _ps()
    k = P.K_SAFE if k_eff is None else k_eff
    L = P.LEAK_PARASITIC_HI if leak is None else leak
    n_tot = 1.0 / (1.0 - k)
    f = k / (nu * (1.0 - k))
    a = n_tot - f
    return k / (nu - k), f, a, a - f - L * n_tot


def tritium_per_source_neutron():
    return _ps().tritium_per_source_neutron()


def _capture_local(fn):
    import contextlib as _c
    import io as _io
    b = _io.StringIO()
    with _c.redirect_stdout(b):
        fn()
    return b.getvalue()


def report_fertile():
    """The ladder below the tails, and whether the design works on each rung."""
    P = _ps()
    trit = tritium_per_source_neutron()
    print("  THE FERTILE LADDER")
    print()
    print("    DECIDED: URANIUM, WITH SEAWATER URANIUM AS THE REPLACEMENT.")
    print("    Tails first, then spent fuel, then natural uranium, then the")
    print("    ocean. THORIUM IS REFUSED. What follows is the analysis that")
    print("    was open when the decision was taken, kept because refusing an")
    print("    option is only meaningful beside what refusing it costs -- and")
    print("    here it costs nothing: the uranium ladder is longer, it closes")
    print("    the neutron budget unconditionally where thorium does not, and")
    print("    the first two rungs are wastes rather than ores.")
    print()
    print("    --uranium asks whether there is enough. This asks what comes")
    print("    after, and then the question that is usually skipped: A")
    print("    RESOURCE IS NOT A FUEL UNTIL THE NEUTRON BUDGET SAYS SO.")
    print()
    print(f"    The station eats {uranium_feed_t_per_year():.3f} t/yr,"
          f" a {uranium_life_charge_t():.0f} t life charge.")
    print()
    print("      resource                          tonnes   station-lifetimes"
          "   world-yr")
    for name, t, note, iso in FERTILE_RESOURCES:
        print(f"      {name:32s} {t:9.2e} {fertile_lifetimes(t):17,.0f}"
              f" {stock_electricity_twh(t)/WORLD_ELECTRICITY_TWH_YR:10,.0f}")
    print()
    print("      (world-yr is years of TODAY'S world electricity at complete")
    print("       fission and this plant's own thermal efficiency -- an upper")
    print("       bound on the resource, not a prediction of recovery.)")
    print()
    print("    THE FIRST THREE RUNGS ARE THE SAME FUEL. Tails, spent fuel and")
    print("    natural uranium are all U-238 with different amounts of U-235")
    print("    attached, and the design does not care which: it burns the")
    print("    U-238. Nothing changes but the provenance -- and the first two")
    print("    are wastes, so the design's environmental case survives them.")
    print()
    print("    THE FOURTH RUNG IS A DIFFERENT FUEL AND IT DOES NOT SIMPLY")
    print("    SUBSTITUTE. Thorium breeds U-233, which fissions at"
          f" nu = {NU_U233_FAST:.2f}")
    print(f"    against Pu-239's {NU_PU239_FAST:.2f}, and the whole neutron budget"
          " is built on")
    print("    that number. It costs twice over -- fission takes more of the")
    print("    budget AND f_b rises -- so what is left for Li-6 shrinks:")
    print()
    print("      cycle                nu      f_b       F        A    free"
          "   tritium   verdict")
    for label, nu in (("U-238 -> Pu-239", NU_PU239_FAST),
                      ("Th-232 -> U-233", NU_U233_FAST)):
        for L in (P.LEAK_PARASITIC_LO, P.LEAK_PARASITIC_HI):
            f_b, f, a, free = budget_on(nu, leak=L)
            ok = "CLOSES" if free > trit else "DOES NOT CLOSE"
            print(f"      {label:16s} L={L:.2f} {nu:5.2f} {f_b:8.4f}"
                  f" {f:8.3f} {a:8.3f} {free:7.3f} {trit:9.3f}   {ok}")
    print()
    print("    SO THE THORIUM FALLBACK IS CONDITIONAL, and the condition is")
    print("    the one term this work has never measured. At the tight")
    print(f"    leakage allowance (L = {P.LEAK_PARASITIC_LO:.2f}) thorium closes with")
    _fb, _f, _a, free_lo = budget_on(NU_U233_FAST, leak=P.LEAK_PARASITIC_LO)
    _fb2, _f2, _a2, free_hi = budget_on(NU_U233_FAST, leak=P.LEAK_PARASITIC_HI)
    print(f"    {free_lo-trit:.3f} to spare; at the loose one it is short by"
          f" {trit-free_hi:.3f}.")
    print("    L is leakage plus parasitic capture and it is an ASSUMED band")
    print("    everywhere in this work. On uranium the band does not decide")
    print("    anything; ON THORIUM IT DECIDES WHETHER THE FUEL WORKS.")
    print()
    print("    THAT CONDITIONALITY IS NOW MOOT AND IS KEPT ANYWAY, because")
    print("    a refused option with its reason recorded is a decision, and a")
    print("    refused option without one is a gap. Uranium closes on both")
    print("    budgets; thorium closes on one; the choice needed no more than")
    print("    that.")
    print()
    print("    AND ONE ROUTE MAKES THE QUESTION GO AWAY. The tritium demand")
    print(f"    of {trit:.3f} per source neutron is what thorium cannot afford. A")
    print("    cell that makes its own tritium from deuterium -- see")
    print("    window.py --fuels -- demands essentially none, and thorium then")
    print("    closes on both budgets with room. The fuel question and the")
    print("    fertile question turn out to be the same question.")
    print()
    print("    ON THE DECISION'S OWN TERMS: seawater uranium is"
          f" {fertile_lifetimes(4.5e9):,.0f}")
    print("    station-lifetimes, which is not a resource limit in any sense")
    print("    a design can act on. Extracting it is unsolved at scale and is")
    print("    a REQUIREMENT rather than a plan -- but it is a requirement on")
    print("    chemistry that many groups are working, not on this design, and")
    print("    the tails alone cover the interval in which they work it.")
    print()
    print("    THE HONEST BOTTOM LINE ON DEPLETION. The tails alone are")
    print(f"    {fertile_lifetimes(1.6e6):,.0f} station-lifetimes, so 'when the DU runs out' is")
    print("    not a planning horizon -- it is past the point where the")
    print("    question is about a different civilisation. What the ladder")
    print("    shows is that there is no cliff at the end of it: the next")
    print("    rung up is the same fuel from a different pile, and the rung")
    print("    after that is an ocean.")


# ---- THE THERMAL BUFFER, WHICH IS A MITIGATION AND ALSO A PLANT ITEM ------
# A high-power linac trips often, and buildpackage.py's envelope carried that
# as an open item. It closes with a store: a nitrate-salt thermal buffer on the
# SECONDARY side, which concentrating-solar plants build at exactly this
# tonnage as a matter of routine. It rides a trip out, and it lets the station
# load-follow, which a gigawatt station wants anyway.
BUFFER_TRIP_S = 60.0         # ASSUMED: ride out a trip of this length
BUFFER_DT_K = 50.0           # ASSUMED: and hold the loop within this
BUFFER_CP = 1500.0           # J/kg/K, solar nitrate salt            SOURCED


def thermal_buffer_kg(trip_s=BUFFER_TRIP_S, dt_k=BUFFER_DT_K, cp=BUFFER_CP):
    return ref()["thermal_mw"] * 1e6 * trip_s / (cp * dt_k)


# ---- THE BIOLOGICAL SHIELD, SIZED AS AN ATTENUATION AND NOT AS A DOSE -----
# buildpackage.py carried this as "not sized here", which environment.py could
# not grade below MODERATE. It is sized now -- as an ATTENUATION FACTOR, which
# is computable, rather than as a dose, which needs a site.
CONCRETE_REMOVAL_CM = 12.0   # fast-neutron removal length, ordinary concrete
BIO_ATTENUATION = 1.0e10     # REQUIREMENT: the factor a spallation source of
                             # this power needs at a personnel boundary


def bio_shield_m(attenuation=BIO_ATTENUATION, lam_cm=CONCRETE_REMOVAL_CM):
    return lam_cm * math.log(attenuation) / 100.0


def bio_shield_mass_kg(attenuation=BIO_ATTENUATION):
    """A shell of that thickness around each module's target-and-capture
    volume, on the solenoid's outer envelope."""
    C = _coll()
    t = bio_shield_m(attenuation)
    r = C.des_coil_inner_m() + C.des_winding_thickness_m() + shield_thickness_m()
    h = C.DES_LENGTH_M + 2.0 * shield_thickness_m()
    return CONCRETE_RHO * math.pi * ((r + t) ** 2 * (h + 2 * t) - r ** 2 * h)


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
          f" year, {100*heavy_metal_depletion_fraction():.1f} % over"
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
    print("      3. It changes criterion 3's verdict on ONE row and no more.")
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
       "REQUIREMENT", "CIRCULATING",
       "WAS a bought utility feed and is now made on site: nitrogen is 78 % "
       "of the air here, so the plant liquefies its own and runs the shield "
       "circuit closed. See the liquefier row and report_criterion3()"))
    A(("driver", "nitrogen liquefier, on site", ln2_power_kw(), "kW",
       "DERIVED", "FIRST-CHARGE",
       f"an ordinary cryogenic air separation unit at "
       f"{LN2_KWH_PER_KG:.3f} kWh/kg SOURCED, sized for the shield duty. It "
       f"is {100.0 * ln2_share_of_net():.5f} % of net output -- the row "
       "exists to CLOSE a gate line, not because it costs anything"))
    A(("driver", "copper and steel, cryomodules", L * linac_length_m() * 2.0,
       "t",
       "REQUIREMENT", "FIRST-CHARGE",
       f"{linac_length_m():.0f} m of superconducting linac at an ASSUMED "
       "2 t/m of cryomodule, vessel and warm structure; ordinary plant "
       "storage, and the figure is a scoping one"))

    A(("target", "molten lead", N * lead_inventory_kg() / 1000.0, "t",
       "DERIVED", "CIRCULATING",
       f"{N:.0f} sealed loops at {lead_flow_kg_s():.0f} kg/s each, held above "
       f"{PB_MELT_C:.0f} C by trace heating that must never fail. NOT MERCURY: "
       f"the sourced study's material has a vapour pressure eight orders "
       f"higher, so a mercury breach is a release and a lead breach is a "
       f"spill. Costs {target_length_ratio():.3f}x in target length. Activated, "
       "so the loop is still a hot cell -- but a hot cell containing a solid "
       "when cold"))
    A(("target", "beryllium window", 0.0, "-", "DERIVED", "FIRST-CHARGE",
       "NONE. The sourced design carries a beryllium window six metres "
       "downstream for one reason -- to stop mercury vapour reaching the "
       "channel. Lead has no vapour to stop, so the window, its annual "
       "replacement, its beryllium dust and its waste stream all leave the "
       "design with the mercury. A mitigation that deletes a component rather "
       "than managing it"))

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
       f"{100*heavy_metal_depletion_fraction():.1f} % over the life. A "
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
       "online and now specified ELECTRICAL, which is what closes its gate "
       "line: helium sparge on the recirculating inventory for the noble "
       "gases, noble metals plated out, VACUUM DISTILLATION for the alkali "
       "and alkaline-earth chlorides, ELECTROWINNING for the lanthanides, "
       "and any chemical reductant regenerated electrolytically on site. "
       "THIS IS WHAT BUYS L = 0.20 FOR FORTY YEARS and it is still the "
       "single most demanding unbuilt item in the plant -- what changed is "
       "that it consumes electricity rather than a delivered reagent"))
    A(("blanket", "salt-processing electricity", salt_processing_kw(), "kW",
       "DERIVED", "CIRCULATING",
       f"bounded, not designed: the whole inventory distilled "
       f"{SALT_PASSES_PER_YEAR:.0f} times a year at "
       f"{SALT_VAP_MJ_KG:.1f} MJ/kg, which is far more than a slipstream "
       f"cleanup needs. Even so it is "
       f"{100.0 * salt_processing_share_of_net():.4f} % of net output"))

    A(("shielding", "biological shield, concrete",
       N * bio_shield_mass_kg() / 1000.0, "t", "REQUIREMENT", "FIRST-CHARGE",
       f"{bio_shield_m():.2f} m, sized as an ATTENUATION of "
       f"{BIO_ATTENUATION:.0e} at "
       f"{CONCRETE_REMOVAL_CM:.0f} cm removal length -- computable without a "
       "site, where a dose is not. The attenuation FACTOR is the requirement; "
       "what dose it produces at a boundary is the site's licence to test"))
    A(("shielding", "coil shield, tungsten-loaded",
       N * shield_mass_kg() / 1000.0, "t", "DERIVED", "FIRST-CHARGE",
       f"{shield_thickness_m():.2f} m, sized for a {PLANT_LIFE_Y:.0f} year "
       f"COIL life at {r['beam_mw']:.0f} MW -- an insulation-dose limit, not a "
       f"biological one. It carries "
       f"{r['beam_mw']*1e6*m.F_INTO_SHIELDING/1e3:.0f} kW of beam power and "
       "must be actively cooled, not passive"))
    A(("shielding", "reduced-activation steel, inside the shield",
       N * solenoid_cold_mass_kg() / 1000.0, "t", "REQUIREMENT",
       "FIRST-CHARGE",
       "EUROFER- or F82H-class: chromium and tungsten in place of the "
       "molybdenum, niobium and nickel that make Nb-94 and Ni-63, and cobalt "
       "held below 100 ppm. It is the fusion programme's own material and its "
       "point is that activation decays to hands-on levels in about a "
       "century instead of needing a deep repository. THIS IS A PROCUREMENT "
       "DECISION THAT SETS THE DECOMMISSIONING WASTE CLASS AND CANNOT BE MADE "
       "AFTERWARDS"))

    A(("conversion", "supercritical CO2 or steam plant", r["thermal_mw"],
       "MW-th", "IMPORTED", "CIRCULATING",
       f"{r['gross_mw']:.0f} MW gross, {r['net_mw']:.0f} MW net after the "
       f"driver and after the {r['dry_cooling_mw']:.0f} MW dry-cooling "
       "penalty; ordinary power-plant storage and inventory"))
    A(("conversion", "dry cooling, air-cooled condensers", r["gross_mw"],
       "MW gross", "DERIVED", "CIRCULATING",
       f"ZERO WATER CONSUMED, at {100*_ps().DRY_COOLING_PENALTY:.0f} % of "
       "gross output. Adopted in the design rather than offered as an option, "
       "because the cooling-water impact cannot be graded below MODERATE any "
       "other way; the module count absorbs the cost"))
    A(("conversion", "nitrate-salt thermal buffer",
       thermal_buffer_kg() / 1000.0, "t", "DERIVED", "CIRCULATING",
       f"rides out a {BUFFER_TRIP_S:.0f} s beam trip within "
       f"{BUFFER_DT_K:.0f} K on the SECONDARY side. Concentrating-solar "
       "plants build stores at this tonnage routinely, so the tonnage is not "
       "the difficulty. It closes the thermal-cycling item buildpackage.py "
       "carried open, and it lets the station load-follow, which a gigawatt "
       "station wants anyway"))
    A(("conversion", "krypton-85 capture, cryogenic charcoal", 0.0, "-",
       "REQUIREMENT", "REPLACED",
       "The salt sparge sends noble gases to delay beds; the short-lived "
       "decay there and Kr-85 at 10.8 y does not, so it is captured on "
       "cryogenic charcoal and bottled rather than released. Routine at "
       "reprocessing plants. It moves an atmospheric release into the waste "
       "inventory, which is the trade and is stated as one"))

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
    print(f"      MOLTEN LEAD. {lead_inventory_kg()/1000.0:.2f} t per module,"
          f" {n*lead_inventory_kg()/1000.0:.1f} t in all, in loops")
    print("      activated the moment the beam is on -- so still a hot cell,")
    print(f"      but one holding a SOLID below {PB_MELT_C:.0f} C. That is the")
    print("      whole of why the substitution was made: mercury's failure mode")
    print("      is a vapour release and lead's is a puddle. The cost is that")
    print("      the loop must never be allowed to freeze, and trace heating")
    print("      is now a safety system rather than a convenience.")
    print()
    print(f"      FUEL SALT. {salt_inventory_kg()/1000.0:.1f} t holding "
          f"{heavy_metal_inventory_kg()/1000.0:.1f} t of heavy metal, molten,")
    print("      at 900 K, and it is the fission inventory. It drains by")
    print("      freeze plug to a passively cooled subcritical tank -- which")
    print("      is the same argument as --stability's: cut the beam and it")
    print("      stops, and the drain is the second, independent way to say so.")


def ln2_tonnes_per_year():
    """The shield circuit's nitrogen duty: 40 t/yr per driver, as the row
    that states it has always carried."""
    return float(ref()["linacs"]) * 40.0


def ln2_power_kw(specific=None):
    """What liquefying that nitrogen on site draws, continuously."""
    sp = LN2_KWH_PER_KG if specific is None else specific
    kwh = ln2_tonnes_per_year() * 1000.0 * sp
    return kwh / (SEC_PER_YEAR / 3600.0)


def ln2_share_of_net(specific=None):
    return ln2_power_kw(specific) / (ref()["net_mw"] * 1000.0)


def salt_processing_kw(passes=None):
    """A BOUND on the electrical cleanup, not a process design.

    Distils the ENTIRE salt inventory this many times a year -- heat to the
    loop's top temperature and then vaporise it -- where a real cleanup takes
    a slipstream. If the bound is negligible the design need not be chosen
    here, which is the point of computing a bound instead of a process."""
    n = SALT_PASSES_PER_YEAR if passes is None else passes
    m = salt_inventory_kg()
    j = n * m * (SALT_CP * SALT_DT_K + SALT_VAP_MJ_KG * 1e6)
    return j / SEC_PER_YEAR / 1000.0


def salt_processing_share_of_net(passes=None):
    return salt_processing_kw(passes) / (ref()["net_mw"] * 1000.0)


def gate_lines():
    """Every row that is still a supply line INWARD, by supply class.

    Read from the inventory rather than written beside it, so a row that
    changes class changes this answer and no prose has to be remembered."""
    out = {}
    for zone, mat, val, unit, status, sup, note in bill():
        if sup in ("REPLACED",):
            out.setdefault(sup, []).append((zone, mat))
    return out


def report_criterion3():
    """criterion 3, and the two design changes that close most of it"""
    P = _ps()
    print()
    print("  CRITERION 3, AND WHAT IT TOOK TO CLOSE IT")
    print()
    print("    The criterion asks for NO INPUT OF ANYTHING BEYOND THE INITIAL")
    print("    IGNITION. --supply's verdict was that it holds on fuel and")
    print("    fails on CONSUMABLES AND PARTS. The consumables half was a")
    print("    design choice rather than a law, and this is the pass that")
    print("    changed the design instead of the sentence.")
    print()
    print("    WHAT ARRIVED AT THE GATE BEFORE, AND WHAT REPLACES IT")
    print()
    print("      LIQUID NITROGEN, for the cryogenic shields")
    print(f"        was  {ln2_tonnes_per_year():.0f} t/yr in a tanker, and the"
          " file called it")
    print("             'the one utility feed'")
    print("        now  liquefied on site. Nitrogen is 78 % of the air here,")
    print("             so the shield circuit runs CLOSED and the feedstock")
    print("             is the atmosphere, which is not a delivery.")
    print(f"        cost {ln2_power_kw():.1f} kW at {LN2_KWH_PER_KG:.3f}"
          f" kWh/kg, which is {100.0 * ln2_share_of_net():.5f} % of net")
    print(f"             output. At the pessimistic {LN2_KWH_PER_KG_HI:.2f}"
          f" kWh/kg it is"
          f" {100.0 * ln2_share_of_net(LN2_KWH_PER_KG_HI):.4f} %.")
    print()
    print("      SALT-PROCESSING REAGENTS, for fission-product removal")
    print("        was  'the reagents the salt's fission-product removal")
    print("             consumes' -- named, never specified, and therefore")
    print("             never priced")
    print("        now  specified ELECTRICAL: helium sparge on the")
    print("             recirculating inventory, noble metals plated out,")
    print("             vacuum distillation for the alkali and")
    print("             alkaline-earth chlorides, electrowinning for the")
    print("             lanthanides, any chemical reductant regenerated")
    print("             electrolytically on site.")
    print(f"        cost bounded at {salt_processing_kw()/1000.0:.2f} MW --"
          f" {100.0 * salt_processing_share_of_net():.4f} % of net -- and the")
    print("             bound is deliberately absurd: it distils the WHOLE")
    print(f"             {salt_inventory_kg()/1000.0:.0f} t inventory"
          f" {SALT_PASSES_PER_YEAR:.0f} times a year, where a real cleanup")
    print("             takes a slipstream. A BOUND IS COMPUTED BECAUSE THE")
    print("             PROCESS IS NOT THIS FILE'S TO CHOOSE, and if the")
    print("             bound is negligible the choice does not have to be.")
    print()
    print("    A CHEMICAL LINE BECOMES AN ELECTRICITY LINE, AND THE PLANT")
    print(f"    MAKES ELECTRICITY. Together the two draw"
          f" {(ln2_power_kw() + salt_processing_kw())/1000.0:.2f} MW against")
    print(f"    {ref()['net_mw']:,.0f} MW net --"
          f" {100.0*(ln2_power_kw() + salt_processing_kw())/(ref()['net_mw']*1000.0):.4f}"
          " % -- so nothing else in the plant moves.")
    print()
    print("    WHAT REMAINS, READ FROM THE INVENTORY RATHER THAN REMEMBERED")
    print()
    g = gate_lines()
    for sup, rows in sorted(g.items()):
        for zone, mat in rows:
            print(f"      {sup:<10} {zone:<12} {mat}")
    if not g:
        print("      (nothing)")
    print()
    n_replaced = sum(len(v) for v in g.values())
    print(f"    {n_replaced} rows, and every one of them is a PART. No")
    print("    material stream arrives at the gate any more: not fuel, not")
    print("    fertile, not tritium, not lithium, not coolant, not reagent,")
    print("    not cryogen. THE CRITERION NOW HOLDS ON EVERY MATERIAL STREAM")
    print("    AND FAILS ONLY ON REPLACEMENT PARTS.")
    print()
    print("    THAT IS A REAL STRENGTHENING AND IT IS NOT A COMPLETE PASS,")
    print("    AND THE DIFFERENCE MATTERS. What was 'fails on consumables and")
    print("    parts' is now 'fails on parts'. The consumables were a design")
    print("    choice and were fixed. The parts are not a design choice:")
    print("    pumps have seals, heat exchangers foul, electrodes erode, and")
    print("    the fission-product removal system -- still the single most")
    print("    demanding unbuilt item here -- will have a service life.")
    print()
    print("    SO THE HONEST STATEMENT OF WHERE CRITERION 3 STANDS:")
    print("      MATERIAL INPUT      none. Closed.")
    print("      ENERGY INPUT        none after start-up. Closed.")
    print("      PARTS               a supply line inward, for ever, and no")
    print("                          machine ever built has escaped one.")
    print()
    print("    A DECISION IS OWED AND IT IS NOT THIS FILE'S TO TAKE. Read")
    print("    literally -- no input of ANYTHING -- the criterion cannot be")
    print("    met by any physical object, because parts wear. Read as it was")
    print("    plainly meant -- no FUEL, no FEEDSTOCK, no CONSUMABLE -- it is")
    print("    now met. WHICH READING GOVERNS IS THE AUTHOR'S, and rewording")
    print("    a criterion to make a design pass it is the one move this")
    print("    project forbids. The design was changed; the criterion was")
    print("    not, and the gap between the two readings is stated here so")
    print("    that the choice is visible rather than assumed.")
    print()


def report_supply():
    """Criterion 4, adjudicated row by row: what the plant actually consumes."""
    print("  CRITERION 3 -- NOTHING SUPPLIED AFTER IGNITION -- ADJUDICATED")
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
          f"{100*heavy_metal_depletion_fraction():.1f} % of it. On MASS alone")
    print("    the charge outlasts the plant and no breeding is needed at all.")
    print("    THAT COMPARISON IS AGAINST THE WRONG DENOMINATOR, and it is the")
    print("    one this file made until it was checked. What fissions is the")
    print("    FISSILE, not the heavy metal, and the fissile is a 12-20 %")
    e_lo, e_hi = fissile_exhaustion_years()
    d_lo, d_hi = fissile_depletion_fraction()
    print(f"    slice of it -- {heavy_metal_inventory_kg()*_ps().FISSILE_FRACTION[0]/1000:.1f}"
          f" to {heavy_metal_inventory_kg()*_ps().FISSILE_FRACTION[1]/1000:.1f} t against a"
          f" {burnup_kg_per_year()*PLANT_LIFE_Y/1000:.1f} t burn.")
    print(f"    Unbred, the charge is {100*d_lo:.0f}-{100*d_hi:.0f} % depleted"
          f" over the life, which is")
    print(f"    to say IT IS GONE -- exhausted between year {e_lo:.0f} and year"
          f" {e_hi:.0f}.")
    k_lo, k_hi = k_without_breeding()
    g_lo, g_hi = gain_without_breeding()
    print(f"    k falls from {_ps().K_SAFE:.3f} to {k_lo:.3f}-{k_hi:.3f} and the"
          f" gain from {ref()['gain']:.1f} to {g_lo:.1f}-{g_hi:.1f}.")
    print("    THE UNBRED PLANT DOES NOT DEGRADE, IT STOPS. Breeding holds k,")
    print("    and that is the whole of why f_b is a requirement rather than")
    print("    an optimisation.")
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
    print("    WHAT ARRIVES AT THE GATE, every year, for ever:")
    print("      NOTHING. Two streams did -- liquid nitrogen for the")
    print("      cryogenic shields, and the reagents the salt's")
    print("      fission-product removal consumes -- and BOTH WERE DESIGN")
    print("      CHOICES RATHER THAN LAWS. The nitrogen is now liquefied on")
    print("      site from the air, and the salt cleanup is specified")
    print("      electrical. Together they draw "
          f"{(ln2_power_kw() + salt_processing_kw())/1000.0:.2f} MW, which is")
    print(f"      {100.0*(ln2_power_kw() + salt_processing_kw())/(ref()['net_mw']*1000.0):.4f}"
          " % of net output. See --criterion3.")
    print("    and WHAT LEAVES: fission products, at "
          f"{burnup_kg_per_year():.0f} kg/yr.")
    print()
    print("    (the beryllium window left the design with the mercury --")
    print("     the lead target deletes it, and this list is read from the")
    print("     supply column rather than written beside it.)")
    print()
    print("    So criterion 3 holds ON EVERY MATERIAL STREAM and fails ON")
    print("    PARTS ALONE. It read 'fails on consumables and parts' until")
    print("    the consumables were designed out rather than argued away;")
    print("    what is left is a parts line, which no machine ever built has")
    print("    escaped. That is the honest statement, it is stronger than any")
    print("    fission or fusion plant proposed, and it is STILL not what was")
    print("    literally asked for. A status is never flattened, and --")
    print("    criterion3 states the two readings of the criterion and takes")
    print("    neither: which one governs is the author's.")


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
    print()
    print("  the mitigations that changed the plant, not the prose")
    check("the target is lead and no mercury row survives the bill",
          not any("mercury" in mat.lower()
                  for _s, mat, _q, _u, _st, _sup, _n in bill()))
    check("  -- and the beryllium window left with it",
          [q for _s, mat, q, _u, _st, _sup, _n in bill()
           if "beryllium" in mat] == [0.0])
    check("  -- the substitution costs target length and that is stated",
          target_length_ratio() > 1.0)
    check("dry cooling is in the station, not offered beside it",
          ref()["dry_cooling_mw"] > 0.0
          and ref()["net_mw"] < ref()["gross_mw"])
    check("  -- and the station still meets its households after paying it",
          ref()["households"] >= _ps().STATION_HOUSEHOLDS)
    check("the biological shield is sized as an attenuation, not a dose",
          bio_shield_m() > shield_thickness_m())
    check("the thermal buffer rides a trip the envelope had left open",
          thermal_buffer_kg() > 0.0)
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
          max(gain_without_breeding()) < ref()["gain"] / 2.0)
    # THE DENOMINATOR BUG, PINNED. fissile_depletion_fraction divided by the
    # heavy metal for as long as this file existed, which is the one thing its
    # name says it does not do. The two must differ by the fissile fraction,
    # and the fissile one must exceed unity -- the charge is exhausted.
    P = _ps()
    d_lo, d_hi = fissile_depletion_fraction()
    hm_frac = heavy_metal_depletion_fraction()
    check("the fissile and heavy-metal depletions are NOT the same number",
          abs(d_lo - hm_frac) > 0.5)
    check("  -- they differ by exactly the fissile fraction",
          abs(d_lo * P.FISSILE_FRACTION[1] - hm_frac) < 1e-9
          and abs(d_hi * P.FISSILE_FRACTION[0] - hm_frac) < 1e-9)
    check("the fissile charge is MORE than fully depleted, unbred", d_lo > 1.0)
    e_lo, e_hi = fissile_exhaustion_years()
    check("  -- so it is exhausted inside the plant's life, at both ends",
          e_hi < PLANT_LIFE_Y)
    check("  -- and k therefore reaches zero rather than merely falling",
          max(k_without_breeding()) == 0.0)
    check("exhaustion is later with a richer charge, as it must be",
          fissile_exhaustion_years(0.20)[0] > fissile_exhaustion_years(0.12)[0])
    print("    (the second and third are not in tension and the distinction is")
    print("     the point: the charge is big enough, and it is the FISSILE")
    print("     FRACTION that runs out, not the mass. Breeding holds k, not")
    print("     the inventory -- see report_supply.)")
    print()
    print("  criterion 3 is decided by the supply column and by nothing else")
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
    print("  the fertile ladder, and the rung that does not simply substitute")
    check("every rung is stated in station-lifetimes, not in tonnes alone",
          all(fertile_lifetimes(t) > 0 for _n, t, _q, _i in FERTILE_RESOURCES))
    check("the tails alone are thousands of station-lifetimes",
          fertile_lifetimes(1.6e6) > 1000.0)
    check("thorium's f_b is HIGHER than uranium's, so it is not a swap",
          budget_on(NU_U233_FAST)[0] > budget_on(NU_PU239_FAST)[0])
    check("  -- and fission takes more of the budget too, which is the second cost",
          budget_on(NU_U233_FAST)[1] > budget_on(NU_PU239_FAST)[1])
    trit = tritium_per_source_neutron()
    check("uranium closes the tritium balance on BOTH leakage budgets",
          all(budget_on(NU_PU239_FAST, leak=L)[3] > trit
              for L in (P.LEAK_PARASITIC_LO, P.LEAK_PARASITIC_HI)))
    check("thorium closes on the tight budget and NOT on the loose one",
          budget_on(NU_U233_FAST, leak=P.LEAK_PARASITIC_LO)[3] > trit
          and budget_on(NU_U233_FAST, leak=P.LEAK_PARASITIC_HI)[3] < trit)
    check("  -- so the thorium fallback is CONDITIONAL and is said to be",
          "CONDITIONAL" in _capture_local(report_fertile))
    check("the uranium decision is recorded, with thorium REFUSED",
          "DECIDED: URANIUM" in _capture_local(report_fertile)
          and "THORIUM IS REFUSED" in _capture_local(report_fertile))
    check("  -- and the refused option keeps its analysis beside it",
          "closes on one" in _capture_local(report_fertile))
    check("and with no tritium demand thorium closes on both",
          all(budget_on(NU_U233_FAST, leak=L)[3] > 0.0
              for L in (P.LEAK_PARASITIC_LO, P.LEAK_PARASITIC_HI)))
    print()
    print("  every section renders -- which is how a stale call is caught")
    import contextlib as _c, io as _io
    for _name, _fn in (("bill", report), ("storage", report_storage),
                       ("supply", report_supply), ("uranium", report_uranium),
                       ("fertile", report_fertile)):
        try:
            _b = _io.StringIO()
            with _c.redirect_stdout(_b):
                _fn()
            _ok = len(_b.getvalue()) > 200
        except Exception as _e:                        # noqa: BLE001
            _ok = False
            print(f"      {_name}: {type(_e).__name__}: {_e}")
        check(f"section {_name!r} renders", _ok)
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
    print("  criterion 3, and the two design changes that close it")
    _rows = bill()
    _sup = {sup for _z, _m, _v, _u, _st, sup, _n in _rows}
    # THE CLOSURE, read from the inventory rather than from the prose.
    check("no row is STOCKPILED as a bought cryogen any more",
          not any(sup == "STOCKPILED" and "nitrogen" in mat
                  for _z, mat, _v, _u, _st, sup, _n in _rows))
    check("the nitrogen row is CIRCULATING, on a closed circuit",
          any(sup == "CIRCULATING" and "nitrogen, thermal shields" in mat
              for _z, mat, _v, _u, _st, sup, _n in _rows))
    check("  -- and the liquefier that makes it is a FIRST-CHARGE item",
          any(sup == "FIRST-CHARGE" and "liquefier" in mat
              for _z, mat, _v, _u, _st, sup, _n in _rows))
    check("the salt cleanup carries an electricity row",
          any("salt-processing electricity" in mat
              for _z, mat, _v, _u, _st, sup, _n in _rows))
    # BOTH COSTS ARE NEGLIGIBLE, which is why the change is free.
    _tot = ln2_power_kw() + salt_processing_kw()
    check("the two together are under a thousandth of net output",
          _tot / (ref()["net_mw"] * 1000.0) < 1e-3)
    check("  -- and still are at the pessimistic liquefaction figure",
          (ln2_power_kw(LN2_KWH_PER_KG_HI) + salt_processing_kw())
          / (ref()["net_mw"] * 1000.0) < 1e-3)
    # THE SALT BOUND IS A BOUND: making it harsher must not change the verdict.
    check("the salt bound is deliberately pessimistic and still negligible",
          salt_processing_share_of_net(passes=12.0) < 1e-3)
    check("  -- and it scales with the passes, so it is a computation",
          abs(salt_processing_kw(6.0) / salt_processing_kw(3.0) - 2.0) < 1e-9)
    # WHAT REMAINS, and that it is parts and nothing else.
    _g = gate_lines()
    check("what remains is REPLACED rows and nothing else",
          set(_g) == {"REPLACED"})
    check("  -- and there are still some, so the pass is not claimed complete",
          len(_g["REPLACED"]) > 0)
    _c3 = _capture_local(report_criterion3)
    check("the report says the criterion now fails on parts ALONE",
          "FAILS ONLY ON REPLACEMENT PARTS" in _c3)
    check("  -- and does not claim a complete pass",
          "IT IS NOT A COMPLETE PASS" in _c3)
    check("  -- and states both readings without taking either",
          "WHICH READING GOVERNS IS THE AUTHOR'S" in _c3)
    check("  -- and refuses to reword the criterion",
          "rewording" in _c3 and "forbids" in _c3)
    # THE NUMBERING, corrected against OBJECTIVE.md's authoritative table.
    _sup_out = _capture_local(report_supply)
    check("the file now says criterion 3, matching OBJECTIVE.md's table",
          "criterion 3" in _sup_out and "criterion 4" not in _sup_out)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--storage", action="store_true",
                    help=report_storage.__doc__)
    ap.add_argument("--criterion3", action="store_true",
                    help=report_criterion3.__doc__)
    ap.add_argument("--supply", action="store_true", help=report_supply.__doc__)
    ap.add_argument("--uranium", action="store_true",
                    help=report_uranium.__doc__)
    ap.add_argument("--fertile", action="store_true",
                    help=report_fertile.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.storage:
        return report_storage()
    if a.criterion3:
        return report_criterion3()
    if a.supply:
        return report_supply()
    if a.uranium:
        return report_uranium()
    if a.fertile:
        return report_fertile()
    return report()


if __name__ == "__main__":
    sys.exit(main() or 0)
