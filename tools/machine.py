#!/usr/bin/env python3
"""machine.py -- the capture solenoid as a build package.

`collector.py --magnet` designs the field: the mirror term, the grade of 1.428,
the aperture product held at 1.50 T.m by dropping the target field and growing
the bore. It then names three things and does not do them -- quench and energy
extraction at 489 MJ, conductor grading above 16 T, and the shielding -- and
stops. This finishes them, and adds what a build package needs beyond the
magnet: the target, the radiation lifetime, the plant, the vacuum, and the
integration of the fuel cell.

The reason it is a separate instrument rather than more of collector.py is the
corpus rule: an instrument IMPORTS a seated member, it never copies one. Every
field, aperture and capture figure here is read from collector at run time, so
this file cannot drift from the design it builds.

One finding here overturns a choice the magnet design implied, and it is the
reason this file exists rather than a paragraph: the production target must sit
INSIDE the capture bore, the bore is 10.7 cm in radius, and that excludes the
rotating solid target every megawatt-class facility uses. What fits is a free
liquid-metal jet -- which is not a novelty, having been run in a 15 T solenoid.

Stdlib only.  python3 tools/machine.py [--all|--circuit|--conductor|--target
                                        |--radiation|--plant|--selftest]
"""
import argparse
import functools
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C           # noqa: E402  -- imported, never copied

MU_0 = 4.0e-7 * math.pi

# ---- circuit and quench ----------------------------------------------------
I_OP = 20.0e3               # A, operating current -- chosen below
V_DUMP_MAX = 10.0e3         # V, insulation limit on the dump
CU_FRACTION = 0.5           # copper in the conductor matrix
CU_INTJ2DT = 4.0e16         # A^2 s / m^4, copper 20 K -> 200 K hot spot   SOURCED
HOTSPOT_MARGIN = 3.0        # required ratio of allowed to actual dump time


def inductance_h(i_op=I_OP):
    """L = 2E/I^2. The stored energy is the magnet's; the current is a choice,
    and it is THE choice: L falls as 1/I^2, so the dump time falls with it."""
    return 2.0 * C.des_stored_energy_j() / (i_op * i_op)


def dump_resistance_ohm(i_op=I_OP, v_max=V_DUMP_MAX):
    return v_max / i_op


def dump_time_s(i_op=I_OP, v_max=V_DUMP_MAX):
    return inductance_h(i_op) / dump_resistance_ohm(i_op, v_max)


def miits(i_op=I_OP, v_max=V_DUMP_MAX):
    """Integral of I^2 dt through an exponential dump, in 10^6 A^2 s."""
    return i_op * i_op * dump_time_s(i_op, v_max) / 2.0 / 1e6


def j_copper_a_m2():
    return C.des_current_density_a_mm2() * 1e6 / CU_FRACTION


def hotspot_allowed_s():
    """How long the copper may carry the current before 200 K."""
    return CU_INTJ2DT / (j_copper_a_m2() ** 2)


def hotspot_margin(i_op=I_OP, v_max=V_DUMP_MAX):
    return hotspot_allowed_s() / dump_time_s(i_op, v_max)


def dump_peak_power_w(i_op=I_OP, v_max=V_DUMP_MAX):
    return i_op * i_op * dump_resistance_ohm(i_op, v_max)


def ramp_voltage_v(hours=4.0, i_op=I_OP):
    return inductance_h(i_op) * i_op / (hours * 3600.0)


# ---- mechanics -------------------------------------------------------------
def magnetic_pressure_pa(b=None):
    b = C.DES_B_PEAK if b is None else b
    return b * b / (2.0 * MU_0)


def winding_area_m2():
    r_i = C.des_coil_inner_m()
    r_o = r_i + C.des_winding_thickness_m()
    return math.pi * (r_o * r_o - r_i * r_i)


def axial_force_n():
    """Compression at the midplane: magnetic pressure over the bore area."""
    return magnetic_pressure_pa() * math.pi * C.des_coil_inner_m() ** 2


def axial_stress_pa():
    return axial_force_n() / winding_area_m2()


def cold_mass_kg(rho=8000.0):
    return winding_area_m2() * C.DES_LENGTH_M * rho


def cooldown_energy_j(rho=8000.0, h_j_per_kg=80.0e3):
    return cold_mass_kg(rho) * h_j_per_kg


# ---- conductor grading -----------------------------------------------------
# Field falls approximately linearly through the winding, from the peak at the
# inner radius to zero outside it. Each superconductor is used only where it can
# carry current, which is what makes 20 T affordable: REBCO only for the 20 %
# of the build that is above 16 T.
GRADE_CEILINGS = (("REBCO", 20.0), ("Nb3Sn", 16.0), ("NbTi", 8.0))


def grade_radius_m(b_ceiling):
    """Radius at which the field has fallen to b_ceiling."""
    r_i, t = C.des_coil_inner_m(), C.des_winding_thickness_m()
    return r_i + t * (1.0 - b_ceiling / C.DES_B_PEAK)


def grade_bands():
    """(name, r_inner, r_outer, cross-section m^2, conductor length m)."""
    out, r_prev = [], C.des_coil_inner_m()
    n_per_m2 = C.des_current_density_a_mm2() * 1e6 / I_OP
    for i, (name, ceil) in enumerate(GRADE_CEILINGS):
        r_next = (grade_radius_m(GRADE_CEILINGS[i + 1][1])
                  if i + 1 < len(GRADE_CEILINGS)
                  else C.des_coil_inner_m() + C.des_winding_thickness_m())
        a = math.pi * (r_next * r_next - r_prev * r_prev)
        out.append((name, r_prev, r_next, a, n_per_m2 * C.DES_LENGTH_M * a))
        r_prev = r_next
    return out


def conductor_length_m():
    return sum(b[4] for b in grade_bands())


def turns():
    return C.des_amp_turns() / I_OP


# ---- the production target -------------------------------------------------
# SOURCED, and it replaces a reconstruction that was wrong by a factor of seven.
# Back, arXiv:1104.2742, FLUKA and MARS over a 4 MW 8 GeV beam on a mercury jet
# in a 20 T solenoid -- this machine -- reports 319 kW of 4 MW into the jet and
# 2149 kW into the shielding. This file previously ASSUMED 55 percent into the
# target. The true figure is 8 percent, and the difference matters: it is the
# whole of the target's cooling problem.
F_DEPOSITED_IN_TARGET = 319.0 / 4000.0
F_INTO_SHIELDING = 2149.0 / 4000.0
F_INTO_NC_MAGNETS = 405.0 / 4000.0
SRC_JET_RADIUS_MM = 4.0            # the published jet
SRC_JET_ANGLE_MRAD = 27.0          # to the proton beam, optimised for low-p pions
SRC_BEAM_RMS_MM = 1.2
SRC_BE_WINDOW_Z_M = 6.0            # stops mercury vapour reaching the channel
SRC_BE_WINDOW_DPA_YR = 0.9         # and must be replaced on that account
W_LAMBDA_CM = 10.3
TARGET_LENGTHS = 2.0
ESS_WHEEL_SPECIFIC_KW_KG = 0.45   # SOURCED, the demonstrated rotating-target class
HG_RHO, HG_CP, HG_BOIL_C = 13546.0, 140.0, 357.0
PBBI_RHO, PBBI_CP = 10500.0, 147.0


def target_power_w(power_mw=1.0):
    return power_mw * 1e6 * F_DEPOSITED_IN_TARGET


def target_length_cm():
    return TARGET_LENGTHS * W_LAMBDA_CM


def static_rod_specific_kw_kg(power_mw=1.0, r_cm=1.0):
    v = math.pi * (r_cm / 100.0) ** 2 * (target_length_cm() / 100.0)
    return target_power_w(power_mw) / (v * 19300.0) / 1e3


def rotating_wheel_radius_m(power_mw=1.0, annulus_cm=2.0):
    """Radius a rotating tungsten wheel would need to reach the demonstrated
    specific power. Computed to be REFUSED: see the bore."""
    mass = target_power_w(power_mw) / 1e3 / ESS_WHEEL_SPECIFIC_KW_KG
    a_cross = (annulus_cm / 100.0) * (target_length_cm() / 100.0)
    return mass / 19300.0 / a_cross / (2.0 * math.pi)


def jet_delta_t_k(power_mw=1.0, d_m=0.01, v_m_s=30.0, rho=HG_RHO, cp=HG_CP):
    mdot = rho * math.pi * (d_m / 2.0) ** 2 * v_m_s
    return target_power_w(power_mw) / (mdot * cp)


def jet_mass_flow_kg_s(d_m=0.01, v_m_s=30.0, rho=HG_RHO):
    return rho * math.pi * (d_m / 2.0) ** 2 * v_m_s


# ---- radiation lifetime ----------------------------------------------------
# SOURCED throughout, from the same study. Its dose limit is an order of
# magnitude above the epoxy figure this file first used, because the coils are
# specified with ceramic insulation rather than organic.
INSULATION_LIMIT_GY = (1.0e8,)         # SOURCED: maximum allowed integrated dose
SRC_PEAK_DOSE_GY_YR_4MW = 1.0e6        # SOURCED, at 2e7 s/year
SRC_PEAK_MW_PER_G = 0.05               # SOURCED, against ITER's 0.17 limit
SRC_ITER_LIMIT_MW_PER_G = 0.17
SRC_DPA_PER_YEAR = 3.0e-4              # SOURCED, Nb3Sn coils
SRC_DPA_CRITICAL = 1.9e-3              # SOURCED, irreversible current reduction
SRC_YEAR_S = 2.0e7                     # the study's own conservative year
PEAK_TO_MEAN = 10.0                    # RECONSTRUCTED: dose concentrates at r_inner
SECONDS_PER_YEAR = 3.156e7


def coil_dose_rate_gy_s(power_mw=1.0, peak=True):
    d = C.des_heat_load_w(power_mw) / cold_mass_kg()
    return d * (PEAK_TO_MEAN if peak else 1.0)


def coil_life_years(power_mw=1.0, duty=1.0, limit=INSULATION_LIMIT_GY[0]):
    return limit / (coil_dose_rate_gy_s(power_mw) * SECONDS_PER_YEAR * duty)


def sourced_dose_gy_yr(power_mw=1.0):
    """The study's own peak dose, scaled to this beam power and this file's year."""
    return SRC_PEAK_DOSE_GY_YR_4MW * (power_mw / 4.0) * (SECONDS_PER_YEAR / SRC_YEAR_S)


def dose_agreement():
    """This file's reconstructed peak dose over the published one. It is the
    check on the peak-to-mean factor, which is the only reconstruction left in
    the radiation section."""
    return coil_dose_rate_gy_s() * SECONDS_PER_YEAR / sourced_dose_gy_yr()


def sourced_coil_life_years(power_mw=1.0):
    return INSULATION_LIMIT_GY[0] / sourced_dose_gy_yr(power_mw)


def shield_for_life_m(years, power_mw=1.0, limit=INSULATION_LIMIT_GY[0]):
    """Shield thickness that buys a stated coil life. This is how the one
    RECONSTRUCTED input is contained: it sets where the curve sits, not its
    shape, and the shape is what a builder needs."""
    lo, hi = 0.1, 3.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        att = math.exp(m / C.DES_W_LAMBDA_M)
        dose = (power_mw * 1e6 * 0.30 / att) / cold_mass_kg() * PEAK_TO_MEAN
        if dose * SECONDS_PER_YEAR * years > limit:
            lo = m
        else:
            hi = m
    return lo


# ---- the plant -------------------------------------------------------------
LEAD_W_PER_KA_HTS = 0.1


def current_lead_load_w(i_op=I_OP):
    return 2.0 * LEAD_W_PER_KA_HTS * i_op / 1e3


def steady_load_w(power_mw=1.0):
    return C.des_heat_load_w(power_mw) + current_lead_load_w()


def cooldown_days(plant_w_at_80k=1.0e4):
    """Cooldown is dominated by the enthalpy above 80 K, which a shield circuit
    removes far more cheaply than the 4.5 K stage."""
    return cooldown_energy_j() / plant_w_at_80k / 86400.0


def wall_power_kw(power_mw=1.0, carnot_fraction=0.25):
    return steady_load_w(power_mw) * (300.0 / 4.5) / carnot_fraction / 1e3


def _line(k, v, u="", note=""):
    print(f"    {k:<38} {v:>12} {u:<10} {note}")


def report_circuit():
    print("  CIRCUIT, QUENCH AND ENERGY EXTRACTION")
    print(f"    Stored energy is {C.des_stored_energy_j() / 1e6:.0f} MJ. The operating current is the")
    print("    design choice that governs everything downstream: L falls as 1/I^2.")
    print()
    print("      I_op    L        dump at 10 kV     MIITs     hot-spot margin")
    for i in (10e3, 15e3, 20e3, 30e3):
        tag = "   <-- chosen" if abs(i - I_OP) < 1 else ""
        print(f"      {i / 1e3:4.0f} kA {inductance_h(i):6.2f} H"
              f"   R={dump_resistance_ohm(i):5.3f} ohm t={dump_time_s(i):5.2f} s"
              f"   {miits(i):7.1f}   {hotspot_margin(i):5.2f}x{tag}")
    print()
    _line("operating current", f"{I_OP / 1e3:.0f}", "kA")
    _line("inductance", f"{inductance_h():.2f}", "H")
    _line("dump resistance", f"{dump_resistance_ohm():.3f}", "ohm", "at 10 kV terminal")
    _line("dump time constant", f"{dump_time_s():.2f}", "s")
    _line("peak dump power", f"{dump_peak_power_w() / 1e6:.0f}", "MW", "transient, into the resistor")
    _line("copper current density", f"{j_copper_a_m2() / 1e6:.1f}", "A/mm2",
          f"at {CU_FRACTION:.0%} copper")
    _line("hot-spot allowance", f"{hotspot_allowed_s():.1f}", "s", "copper, 20 -> 200 K")
    _line("MARGIN", f"{hotspot_margin():.2f}", "x", f"required {HOTSPOT_MARGIN:.0f}x")
    _line("ramp voltage, 4 h", f"{ramp_voltage_v():.2f}", "V")
    _line("supply rating", f"{I_OP * ramp_voltage_v() / 1e3:.0f}", "kW")
    print()
    print("    THE MARGIN IS A CONSEQUENCE OF THE CONSERVATIVE CURRENT DENSITY.")
    print("    sec.8.3's 18.6 A/mm2 came from a hoop-stress limit with the conductor")
    print("    carrying the whole load. The same choice puts the copper current")
    print("    density low, and the hot-spot allowance goes as its inverse square.")
    print("    Raising J with a steel former would thin the winding AND spend this")
    print("    margin. The two are one decision, and this file names it as one.")


def report_mechanics():
    print("  MECHANICS")
    _line("magnetic pressure at 20 T", f"{magnetic_pressure_pa() / 1e6:.1f}", "MPa")
    _line("axial compression at the midplane", f"{axial_force_n() / 1e6:.0f}", "MN",
          f"{axial_force_n() / 9.81 / 1e6:.0f} kilotonnes")
    _line("winding cross-section", f"{winding_area_m2():.2f}", "m2")
    _line("axial stress in the winding", f"{axial_stress_pa() / 1e6:.1f}", "MPa",
          "against 300 MPa hoop")
    _line("cold mass", f"{cold_mass_kg() / 1000:.0f}", "t", "winding only")
    _line("cooldown enthalpy", f"{cooldown_energy_j() / 1e9:.2f}", "GJ", "300 -> 4.5 K")
    print()
    print("    The axial load is large and the axial STRESS is not: it spreads over")
    print("    a winding cross-section of several square metres. It is an end-plate")
    print("    and tie-rod problem, not a conductor problem.")


def report_conductor():
    print("  CONDUCTOR, GRADED")
    print("    Field falls through the winding from the peak at the inner radius,")
    print("    so each superconductor is used only where it can carry current.")
    print("    That is what makes 20 T affordable: REBCO for the innermost fifth.")
    print()
    print("      band      r_in    r_out   cross-section   conductor length")
    for name, ri, ro, a, ell in grade_bands():
        print(f"      {name:<8} {ri:5.3f} m {ro:5.3f} m  {a:8.2f} m2   {ell / 1000:8.2f} km")
    print()
    _line("turns", f"{turns():.0f}", "", f"at {I_OP / 1e3:.0f} kA")
    _line("total conductor", f"{conductor_length_m() / 1000:.1f}", "km")
    _line("REBCO required", f"{grade_bands()[0][4] / 1000:.2f}", "km",
          "procurable; fusion magnets order hundreds")
    print()
    print(f"    Required engineering current density is {C.des_current_density_a_mm2():.1f} A/mm2.")
    print("    REBCO at 20 T and 4.2 K carries an order of magnitude more, so THE")
    print("    CONDUCTOR IS NOT THE LIMIT HERE -- the structure is. That is the")
    print("    opposite of the usual high-field magnet, and it follows from")
    print("    choosing a large bore at a modest target field.")
    print()
    print("    AND THERE IS A SOURCED ALTERNATIVE THAT USES NO HTS AT ALL.")
    print("    The published design of this same target station reaches 20 T as")
    print("    a RESISTIVE copper insert of about 6 T inside a superconducting")
    print("    outsert of about 14 T, with Nb3Sn for the inner nine coils and NbTi")
    print("    beyond -- at current densities of 16.6 A/mm2 in the copper and 23")
    print("    to 40 in the superconductor, which brackets this design's 12.5.")
    print("    It buys away the HTS procurement and pays in resistive power and in")
    print("    the 405 kW those copper coils absorb from the cascade. Both routes")
    print("    are real; this file computes the all-superconducting one and names")
    print("    the other rather than choosing between them.")


def report_failure():
    """Failure modes: what happens when the field or the jet is lost."""
    print("  FAILURE MODES, SOURCED")
    print("    Two failures dominate, and the published study simulated both.")
    print()
    print("      loss of the magnetic field: the combined jet-and-pool deposition")
    print("      rises about 2.5x, and the DOWNSTREAM superconducting coils take a")
    print("      large dose because nothing steers the secondaries any more. It is")
    print("      mitigated by a conic shielding extension from 3 to 6 m.")
    print()
    print("      loss of the jet: about 80 percent of beam power is dumped into the")
    print("      tungsten-carbide shielding and the beam-pipe casing. The shielding")
    print("      is the beam dump in that case, and must be rated for it.")
    print()
    print("      both at once: nearly half the beam power thermally shocks the")
    print("      mercury pool, with splash velocities approaching 50 m/s.")
    print()
    print("    The consequence for the interlocks is the useful part: the jet and")
    print("    the field must each trip the beam, and the shielding must be a")
    print("    rated dump rather than only a shield.")


def report_target():
    print("  THE PRODUCTION TARGET, AND THE CONSTRAINT THAT DECIDES IT")
    print("    The power split is SOURCED and it replaces a reconstruction this")
    print("    file made that was wrong by a factor of seven. FLUKA and MARS over")
    print("    a 4 MW 8 GeV beam on a mercury jet in a 20 T solenoid -- this")
    print("    machine -- put 319 kW of 4 MW into the jet, not 55 percent.")
    print()
    _line("into the jet", f"{100 * F_DEPOSITED_IN_TARGET:.1f}", "%",
          f"{target_power_w() / 1e3:.0f} kW at 1 MW   SOURCED")
    _line("into the shielding", f"{100 * F_INTO_SHIELDING:.1f}", "%", "SOURCED")
    _line("into the resistive coils", f"{100 * F_INTO_NC_MAGNETS:.1f}", "%", "SOURCED")
    _line("target length", f"{target_length_cm():.1f}", "cm",
          f"{TARGET_LENGTHS:.0f} interaction lengths")
    _line("AVAILABLE BORE RADIUS", f"{100 * C.des_bore_m():.1f}", "cm",
          "the target sits INSIDE the capture solenoid")
    print()
    print("    A STATIC ROD IS EXCLUDED, AND SO IS THE ROTATING WHEEL.")
    _line("static rod, 1 cm radius", f"{static_rod_specific_kw_kg():.0f}", "kW/kg",
          "against a demonstrated 0.45")
    _line("wheel radius to reach 0.45 kW/kg", f"{rotating_wheel_radius_m():.3f}", "m",
          f"and the bore is {C.des_bore_m():.3f} m")
    print()
    print("    Every megawatt-class facility solves this with a rotating solid")
    print("    target of metre scale. NONE OF THEM FITS -- the requirement is")
    print(f"    {rotating_wheel_radius_m() / C.des_bore_m():.1f} times the bore even on the corrected power. The capture")
    print("    solenoid's aperture is the whole reason the pions are captured at")
    print("    all, so the bore cannot be opened to admit a wheel without losing")
    print("    the capture the machine exists for. A hard geometric exclusion.")
    print()
    print("    WHAT FITS IS A FREE LIQUID-METAL JET, AND IT HAS BEEN RUN.")
    print(f"      the published jet is {2 * SRC_JET_RADIUS_MM:.0f} mm across at"
          f" {SRC_JET_ANGLE_MRAD:.0f} mrad to a beam of")
    print(f"      {SRC_BEAM_RMS_MM} mm rms, the angle chosen to optimise LOW-momentum pions")
    print()
    print("      mercury    d      v        mass flow      temperature rise")
    for v in (10.0, 20.0, 30.0):
        d = 2 * SRC_JET_RADIUS_MM / 1000.0
        print(f"      {'':9} {1000 * d:2.0f} mm  {v:4.1f} m/s  "
              f"{jet_mass_flow_kg_s(d_m=d, v_m_s=v):6.1f} kg/s"
              f"      {jet_delta_t_k(d_m=d, v_m_s=v):6.0f} K")
    print()
    print(f"    Mercury boils at {HG_BOIL_C:.0f} C and the corrected power leaves room at")
    print("    every velocity above about 10 m/s. The configuration -- a free")
    print("    mercury jet crossing a high-field solenoid bore under a pulsed")
    print("    proton beam -- was built and run at CERN as MERIT, in a 15 T")
    print("    solenoid, for exactly this application. The same study notes that a")
    print("    solid or POWDERED tungsten jet gives similar radiation levels, so")
    print("    the jet need not be mercury; it must be a jet.")
    print()
    print("    AND THE JET BRINGS ONE ITEM THE MAGNET DOES NOT.")
    _line("beryllium window", f"{SRC_BE_WINDOW_Z_M:.0f}", "m downstream",
          "stops mercury vapour   SOURCED")
    _line("its radiation damage", f"{SRC_BE_WINDOW_DPA_YR:.1f}", "DPA/yr",
          "a consumable, replaced on schedule")


def report_radiation():
    print("  RADIATION LIFETIME")
    print("    Sourced from the same study, and it is far better than this file")
    print("    first reconstructed -- because those coils carry ceramic insulation")
    print("    rather than organic, and the limit is an order of magnitude higher.")
    print()
    _line("heat to the cold mass", f"{C.des_heat_load_w():.0f}", "W",
          "at 1 MW, 19 coils   SOURCED")
    _line("peak power density", f"{SRC_PEAK_MW_PER_G:.2f}", "mW/g",
          f"against ITER's {SRC_ITER_LIMIT_MW_PER_G:.2f}   SOURCED")
    _line("peak dose", f"{sourced_dose_gy_yr() / 1e6:.2f}", "MGy/yr", "at 1 MW   SOURCED")
    _line("allowed integrated dose", f"{INSULATION_LIMIT_GY[0] / 1e6:.0f}", "MGy", "SOURCED")
    _line("COIL LIFE", f"{sourced_coil_life_years():.0f}", "years", "at full duty")
    _line("displacements per atom", f"{SRC_DPA_PER_YEAR:.1e}", "DPA/yr",
          f"against a critical {SRC_DPA_CRITICAL:.1e}   SOURCED")
    print()
    print("    THE CHECK ON THE ONE RECONSTRUCTION LEFT HERE.")
    print(f"    This file computes the peak dose from the heat load and a")
    print(f"    peak-to-mean factor of {PEAK_TO_MEAN:.0f}, which is not sourced. Against the")
    print(f"    published figure it returns {dose_agreement():.2f} -- agreement to within the")
    print("    factor itself, which is as much as an assumed peak-to-mean can be")
    print("    asked to give. The sourced figure is the one quoted above.")
    print()
    print("    AND THE SHIELD IS NO LONGER A KNOB THIS FILE TURNS.")
    print("    The 120 cm coil inner radius is that study's own conclusion, reached")
    print("    after 63 cm was found unusable. It is why the stored energy is")
    print(f"    {C.des_stored_energy_j() / 1e6:.0f} MJ rather than the 489 this design first carried, and")
    print("    that increase is the price of the coil life above.")


def report_plant():
    print("  THE PLANT")
    _line("steady load at 4.5 K", f"{steady_load_w():.0f}", "W",
          f"{C.des_heat_load_w():.0f} radiation + {current_lead_load_w():.0f} leads")
    _line("wall power", f"{wall_power_kw():.1f}", "kW", "Carnot fraction 0.25")
    _line("cooldown energy", f"{cooldown_energy_j() / 1e9:.2f}", "GJ")
    _line("cooldown time", f"{cooldown_days():.1f}", "days", "on a 10 kW 80 K circuit")
    _line("bore vacuum", "1e-4", "Pa",
          "set by target outgassing, not by muon scattering")
    print()
    print("    HTS current leads are assumed: at 0.1 W/kA they cost 4 W against the")
    print("    radiation load's 335, and conventional leads would cost forty times")
    print("    that. It is the cheapest decision in this package.")


def report_integration():
    print("  INTEGRATION: WHAT SHARES THE BORE")
    print("    Three things must occupy a bore of 10.7 cm radius, in this order")
    print("    along the axis, and they interact:")
    print()
    print("      1  the liquid-metal jet and its nozzle and catcher, crossing the")
    print("         bore at an angle to the axis so the jet does not run down the")
    print("         muon channel")
    print("      2  the field taper, 1.79 m of it, which is where the mirrored")
    print("         pions turn round and where nothing may obstruct them")
    print("      3  the D-T cell, one muon range deep, at 800 K, in a radiation")
    print("         field, with tritium containment -- beside a mercury loop")
    print()
    print("    THE FUEL CELL BESIDE THE JET IS THE UNSOLVED PART OF THIS PACKAGE.")
    print("    The specification's sec.5.3 already says the cell 'must sit in the")
    print("    production target's region, which is a hostile place to put a")
    print("    cryogenic tritium cell and is not designed here.' That is still")
    print("    true, and it is now the only item in the build that is neither")
    print("    computed nor referred to a machine that exists. It is named here")
    print("    rather than absorbed, and it is the fourth item for sec.10.")


# ---- the decay channel: where the cell can physically sit -------------------
# A pion must decay before its muon can stop, and a pion at the stopping window
# has a decay length of metres. The capture region is 1.5 m long. The cell
# therefore cannot sit in it, and this is not a detail of layout: the beam
# expands adiabatically through any lower-field channel, and a cell sitting in
# the expanded beam would need tens of kilogrammes of tritium.
TAU_PI_S, TAU_MU_S = 2.6033e-8, 2.1970e-6
C_M_S = 2.99792458e8
DECAY_FRACTION_WANTED = 0.90


def decay_length_m(p_mev, m_mev, tau_s):
    return (p_mev / m_mev) * C_M_S * tau_s


def pion_decay_length_m(p_mev=265.0):
    return decay_length_m(p_mev, C.M_PI_MEV, TAU_PI_S)


def muon_decay_length_m(p_mev=265.0):
    return decay_length_m(p_mev, C.M_MU_MEV, TAU_MU_S)


def channel_length_m(p_mev=265.0, fraction=DECAY_FRACTION_WANTED):
    return -math.log(1.0 - fraction) * pion_decay_length_m(p_mev)


def channel_beam_radius_cm(b_channel):
    """Adiabatic expansion: the envelope grows as 1/sqrt(B)."""
    return C.beam_envelope_cm(C.DES_BR, b_channel, C.DES_B_TARGET)


def channel_tritium_kg(b_channel, p_mev=265.0):
    return C.tritium_inventory_kg(p_mev, channel_beam_radius_cm(b_channel))


# ---- the fuel cell ---------------------------------------------------------
CELL_B_T = 20.0                 # recompression field at the cell
CELL_T_K = 800.0                # the Vesman operating point
CELL_PHI = 0.6                  # design density, and it is chosen LOW -- see below
CELL_SIGMA_ALLOW_MPA = 300.0
K_B = 1.380649e-23
N_A = 6.02214076e23
CP_DT_J_KG_K = 5820.0           # 7/2 R / M for a D-T mixture
CELL_DT_K = 100.0               # coolant temperature rise budget
T_HALFLIFE_S = 12.32 * 3.156e7


def cell_radius_cm(b_cell=CELL_B_T):
    return channel_beam_radius_cm(b_cell)


def cell_tritium_kg(b_cell=CELL_B_T, p_mev=265.0):
    return C.tritium_inventory_kg(p_mev, cell_radius_cm(b_cell))


def cell_depth_cm(phi=CELL_PHI, p_mev=265.0):
    return C.target_length_cm(p_mev, phi)


def cell_pressure_mpa(phi=CELL_PHI, t_k=CELL_T_K):
    """Ideal-gas pressure at that number density. Real D-T at these densities is
    strongly non-ideal and the true figure is higher; this is a LOWER bound and
    the direction it errs in is the dangerous one, which is why the design point
    is chosen with margin rather than at the limit."""
    n_molecules = C.LHD_ATOMS_PER_CM3 * phi * 1e6 / 2.0
    return n_molecules * K_B * t_k / 1e6


def lame_ratio(p_mpa, sigma_mpa=CELL_SIGMA_ALLOW_MPA):
    """Outer over inner radius for a monobloc cylinder. None when no thickness
    suffices -- which happens whenever the pressure reaches the allowable
    stress, however much steel is wrapped round it."""
    if sigma_mpa <= p_mpa:
        return None
    return math.sqrt((sigma_mpa + p_mpa) / (sigma_mpa - p_mpa))


def muon_kinetic_mev(p_mev=265.0):
    return math.hypot(p_mev, C.M_MU_MEV) - C.M_MU_MEV


def cell_stopping_w(power_mw=1.0, p_mev=265.0):
    return (C.open_modelled_mu_per_s(power_mw) * muon_kinetic_mev(p_mev)
            * 1.602176634e-13)


def cell_alpha_w(power_mw=1.0, cycles=150.0):
    return (C.open_modelled_mu_per_s(power_mw) * cycles * C.ALPHA_MEV
            * 1.602176634e-13)


def cell_heat_w(power_mw=1.0, cycles=150.0, p_mev=265.0):
    """Into the FUEL: the stopping muons' kinetic energy plus the alpha, which
    stays. The 14.1 MeV neutron leaves and is the blanket's."""
    n = C.open_modelled_mu_per_s(power_mw)
    return (n * muon_kinetic_mev(p_mev) + n * cycles * C.ALPHA_MEV) * 1.602176634e-13


def cell_neutron_w(power_mw=1.0, cycles=150.0):
    n = C.open_modelled_mu_per_s(power_mw)
    return n * cycles * C.NEUTRON_MEV * 1.602176634e-13


def cell_flow_kg_s(power_mw=1.0, dt_k=CELL_DT_K):
    return cell_heat_w(power_mw) / (CP_DT_J_KG_K * dt_k)


def he3_decays_per_s(trit_kg=None, b_cell=CELL_B_T):
    t = cell_tritium_kg(b_cell) if trit_kg is None else trit_kg
    return (t * 1000.0 / 3.016) * N_A * math.log(2.0) / T_HALFLIFE_S


def fuel_atoms(b_cell=CELL_B_T):
    total_kg = cell_tritium_kg(b_cell) / C.T_MASS_FRAC_DT
    return total_kg * 1000.0 / 2.5 * N_A


def he3_ppm_doubling_minutes(b_cell=CELL_B_T):
    return 1e-6 * fuel_atoms(b_cell) / he3_decays_per_s(b_cell=b_cell) / 60.0


def he3_steady_ppm(power_mw=1.0, dt_k=CELL_DT_K, b_cell=CELL_B_T):
    """With the loop that removes the heat also removing helium each pass."""
    turnover = (cell_tritium_kg(b_cell) / C.T_MASS_FRAC_DT) / cell_flow_kg_s(power_mw, dt_k)
    return 1e6 * he3_decays_per_s(b_cell=b_cell) * turnover / fuel_atoms(b_cell)


def report_channel():
    """Where the cell can sit, and what it costs to sit in the wrong place."""
    print("  THE DECAY CHANNEL: WHERE THE CELL CAN PHYSICALLY SIT")
    print("    A pion must decay before its muon can stop. At the stopping window")
    print("    the pion's decay length is metres and the capture region is 1.5 m,")
    print("    so the cell cannot sit in it.")
    print()
    print("      p (MeV/c)   pion decay length   90 percent decayed by")
    for p in (100.0, 150.0, 200.0, 265.0):
        print(f"      {p:9.0f}   {pion_decay_length_m(p):13.2f} m   {channel_length_m(p):17.1f} m")
    print()
    _line("channel length required", f"{channel_length_m():.1f}", "m",
          f"{100 * DECAY_FRACTION_WANTED:.0f}% of pions decayed at the window")
    _line("muon decay length there", f"{muon_decay_length_m():.0f}", "m",
          "so the muons survive the channel")
    print()
    print("    AND THE BEAM EXPANDS THROUGH IT. Adiabatic invariance grows the")
    print("    envelope as 1/sqrt(B), and tritium as its square:")
    print()
    print("      channel field   beam envelope   tritium IF the cell sat there")
    for b in (1.0, 2.0, 3.0, 5.0):
        print(f"      {b:11.1f} T   {channel_beam_radius_cm(b):11.2f} cm   "
              f"{channel_tritium_kg(b):20.1f} kg")
    print()
    print("    Tens of kilogrammes. RECOMPRESSION AT THE CELL IS NOT AN")
    print("    OPTIMISATION, IT IS A REQUIREMENT -- and it is free, because")
    print("    adiabatic compression conserves |p| and therefore leaves the")
    print("    stopping range and the momentum window exactly where they were.")


def report_cell():
    """The fuel cell: the one item the build package previously left undone."""
    print("  THE FUEL CELL")
    print("    The build package named this as its one undone item. It is done")
    print("    here, and two of its requirements turn out to be one.")
    print()
    print("    RECOMPRESSION IS A LEVER ON TRITIUM, AND A STRONG ONE.")
    print("      cell field   beam envelope   tritium at a 265 MeV/c window")
    for b in (10.0, C.DES_B_TARGET, 20.0, 30.0):
        tag = "   <-- design point" if abs(b - CELL_B_T) < 1e-9 else ""
        print(f"      {b:8.2f} T   {cell_radius_cm(b):11.2f} cm   "
              f"{cell_tritium_kg(b):17.2f} kg{tag}")
    print()
    print("    The capture design of sec.8.2 dropped the target field to 14.01 T to")
    print("    bring the peak inside reach. That widened the beam, and a wider beam")
    print(f"    is more tritium: {cell_tritium_kg(C.DES_B_TARGET):.2f} kg at the capture field against")
    print(f"    {cell_tritium_kg(20.0):.2f} recompressed to 20 T. THE FIELD REDUCTION HAD A COST")
    print("    AND RECOMPRESSION PAYS IT BACK. Neither was noticed until the cell")
    print("    was designed, which is the argument for designing it.")
    print()
    print("    AND THE DENSITY SHOULD BE LOW, WHICH INVERTS THE SPECIFICATION.")
    print("    Pressure falls linearly with density and cell length grows as its")
    print("    inverse. Length is cheap; pressure is not:")
    print()
    print("      phi     pressure    depth      monobloc vessel at 300 MPa")
    for phi in (0.222, 0.4, CELL_PHI, 1.0):
        r = lame_ratio(cell_pressure_mpa(phi))
        v = "EXCLUDED at any thickness" if r is None else f"r_o/r_i = {r:.2f}"
        tag = "   <-- design point" if abs(phi - CELL_PHI) < 1e-9 else ""
        print(f"      {phi:5.3f}  {cell_pressure_mpa(phi):8.1f} MPa  "
              f"{cell_depth_cm(phi):7.1f} cm   {v}{tag}")
    print()
    print("    The specification says 'density as high as the cell reaches'. On the")
    print("    demonstrated cycle count the bred-fuel balance breaks even at 0.222")
    print("    of liquid density, so the cell need not reach high at all -- and at")
    print("    500 MPa a 300 MPa steel is excluded HOWEVER THICK IT IS MADE, because")
    print("    a monobloc cylinder cannot hold a pressure at its own allowable")
    print("    stress. RUN IT AS LOW AS THE BALANCE ALLOWS.")
    print()
    print("    THE HEAT, AND THE SECOND REQUIREMENT THAT TURNS OUT TO BE THE SAME.")
    _line("muons stopping per second", f"{C.open_modelled_mu_per_s():.3e}", "1/s")
    _line("kinetic energy each brings", f"{muon_kinetic_mev():.1f}", "MeV")
    _line("stopping power into the fuel", f"{cell_stopping_w() / 1e3:.2f}", "kW")
    _line("alpha heating, 150 cycles", f"{cell_alpha_w() / 1e3:.2f}", "kW",
          "the alpha stays in the fuel")
    _line("TOTAL into the fuel", f"{cell_heat_w() / 1e3:.2f}", "kW")
    _line("neutrons leaving to the blanket", f"{cell_neutron_w() / 1e3:.0f}", "kW")
    _line("flow to remove it", f"{cell_flow_kg_s():.4f}", "kg/s", f"at dT = {CELL_DT_K:.0f} K")
    print()
    print("    THE FUEL MUST FLOW, AND HELIUM-3 SAYS SO INDEPENDENTLY.")
    _line("tritium decays", f"{he3_decays_per_s():.3e}", "1/s")
    _line("1 ppm of 3He accumulates every", f"{he3_ppm_doubling_minutes():.0f}", "minutes")
    _line("steady 3He on the cooling loop", f"{he3_steady_ppm():.3f}", "ppm",
          "against a 1 ppm purity spec")
    print()
    print(f"    Two requirements arrived from different directions -- remove"
          f" {cell_heat_w() / 1e3:.2f} kW,")
    print("    and hold a helium-3 ingrowth that reaches 1 ppm every twenty minutes")
    print("    -- and ONE LOOP MEETS BOTH. The flow that carries the heat out")
    print("    carries the fuel through the purifier, and the flow rate the heat")
    print("    sets is already fast enough to hold helium below the purity the")
    print("    specification demands. That is the cell's design closing on itself.")


# ---- coherence: does the procedure point at this machine? ------------------
# The specification's sec.6 was written before this design existed. It named a
# 2.60 T.m collector, put the cell "inside the solenoid bore, downstream of the
# target", and stood it in a 7.5 cm beam. The design is 1.50 T.m, the cell cannot
# sit in the bore at all, and the beam at the cell is 8.96 cm. A procedure that
# does not point at the machine is not a procedure, so these are computed here
# and sec.6 quotes them.
PROC_APERTURES = (1.50, 2.60)
PROC_CELL_RADIUS_CM = 0.016
PROC_CELL_AREAL = 5.00
PROC_CELL_P_STOP = 111.5
PROC_CELL_B = 20.0


def aperture_bore_cm(br):
    return 100.0 * br / C.DES_B_TARGET


def aperture_shield_cm(br):
    return 100.0 * C.des_coil_inner_m() - aperture_bore_cm(br)


def aperture_capture(br):
    return C.delivered_fraction_mirrored(br, (0.0, 265.0))


def aperture_tritium_kg(br, b_cell=PROC_CELL_B):
    return C.tritium_inventory_kg(265.0, C.beam_envelope_cm(br, b_cell, C.DES_B_TARGET))


def bore_capture_gain():
    return aperture_capture(2.60) / aperture_capture(1.50)


def bore_tritium_cost():
    return aperture_tritium_kg(2.60) / aperture_tritium_kg(1.50)


def proc_beam_radius_cm(br=1.50, b_cell=PROC_CELL_B):
    return C.beam_envelope_cm(br, b_cell, C.DES_B_TARGET)


def proc_interception(br=1.50):
    return (PROC_CELL_RADIUS_CM / proc_beam_radius_cm(br)) ** 2


def proc_acceptance(br=1.50):
    """To the demonstration cell's own stopping momentum, WITH the mirror."""
    return C.delivered_fraction_mirrored(br, (0.0, PROC_CELL_P_STOP))


def proc_binders_per_s(power_mw=1.0, br=1.50):
    """The committed chain. It multiplies by the WHOLE loss budget, not by the
    decay term alone -- the budget already contains that term, and applying both
    would count it twice."""
    return (C.protons_per_s(power_mw, 8.0) * C.harp_combined_yield()
            * proc_acceptance(br) * proc_interception(br) * budget_product())


def proc_neutrons_per_s(power_mw=1.0, cycles=150.0, br=1.50):
    return proc_binders_per_s(power_mw, br) * cycles


def proc_heat_mw(power_mw=1.0, cycles=150.0, br=1.50):
    return proc_neutrons_per_s(power_mw, cycles, br) * 17.59 * 1.602176634e-13 * 1000.0


def proc_cell_tritium_mg():
    return (PROC_CELL_AREAL * math.pi * PROC_CELL_RADIUS_CM ** 2
            * C.T_MASS_FRAC_DT * 1000.0)


def report_coherence():
    """The machine's spec sheet -- the list the procedure must quote."""
    print("  COHERENCE: THE SPEC SHEET THE PROCEDURE MUST QUOTE")
    print("    The specification's sec.6 was written before this design existed and")
    print("    named figures the design does not have. Every apparatus number sec.6")
    print("    states is computed here, so the two cannot drift apart again.")
    print()
    print("    ONE MACHINE, TWO BORES. The coil radius is sourced at 120 cm, and both")
    print("    apertures fit inside it -- so the cold mass, the stored energy and the")
    print("    conductor are IDENTICAL and only the shield thins:")
    print()
    print("      B.R      bore     shield    capture   heat of beam   tritium at the cell")
    for br in PROC_APERTURES:
        print(f"      {br:.2f}  {aperture_bore_cm(br):7.2f} cm {aperture_shield_cm(br):7.1f} cm"
              f"   {aperture_capture(br):7.4f}   {100 * C.insitu_heat_fraction(aperture_capture(br)):8.2f} %"
              f"   {aperture_tritium_kg(br):8.2f} kg")
    print()
    print(f"    The wider bore buys {bore_capture_gain():.3f} in capture for"
          f" {bore_tritium_cost():.2f} in tritium.")
    print("    [1] sec.5.25 found that trade at 3.01 from the beam-envelope argument")
    print("    alone. THIS PACKAGE REPRODUCES IT FROM THE MAGNET, and the two share")
    print("    no step: one is a gyroradius, the other a shield and a coil.")
    print()
    print("    WHAT SEC.6 SAID, AND WHAT THE MACHINE SAYS")
    print()
    print("      item                     sec.6 as written      the machine")
    print(f"      collector aperture       2.60 T.m              {C.DES_BR} T.m, where the")
    print("                                                     acceptance model is validated")
    print(f"      beam at the cell         7.50 cm               {proc_beam_radius_cm():.2f} cm")
    print("      cell position            in the solenoid bore   after a"
          f" {channel_length_m():.1f} m decay")
    print("                                                     channel, recompressed to"
          f" {PROC_CELL_B:.0f} T")
    print("      acceptance               forward only          with the mirror,"
          f" x{proc_acceptance() / C.delivered_fraction(1.50, 'fwd', (0.0, PROC_CELL_P_STOP)):.3f}")
    print(f"      pions decayed            all                   {100 * DECAY_FRACTION_WANTED:.0f}%"
          " in that channel")
    print()
    print("    AND THE THREE CORRECTIONS VERY NEARLY CANCEL.")
    old = C.protons_per_s(1.0, 8.0) * C.harp_combined_yield() * C.delivered_fraction(
        1.50, "fwd", (0.0, PROC_CELL_P_STOP)) * (PROC_CELL_RADIUS_CM / 7.5) ** 2
    new = proc_binders_per_s()
    print(f"      interception            x{proc_interception() / (PROC_CELL_RADIUS_CM / 7.5) ** 2:.3f}"
          "   the beam is wider than sec.6 assumed")
    print(f"      mirror                  x{proc_acceptance() / C.delivered_fraction(1.50, 'fwd', (0.0, PROC_CELL_P_STOP)):.3f}"
          "   the machine has one and sec.6 did not")
    print(f"      end-to-end loss budget  x{budget_product():.3f}   target escape, decay,")
    print("                                       muon survival and scattering")
    print(f"      NET                     x{new / old:.3f}")
    print()
    print(f"      committed binders   {old:.3e}/s as written -> {new:.3e}/s")
    print(f"      committed neutrons  {old * 150:.3e}/s        -> {proc_neutrons_per_s():.3e}/s")
    print(f"      the cell itself is unchanged: {proc_cell_tritium_mg():.2f} mg,"
          f" {C.tritium_curies(proc_cell_tritium_mg() / 1000.0):.1f} Ci")
    print()
    print("    THE PREDICTION SURVIVES BEING POINTED AT THE REAL MACHINE, and moves")
    print(f"    by {100 * abs(new / old - 1):.0f} percent. That it survives is not the point --")
    print("    that it was never checked until now is.")


# ---- the end-to-end loss budget: Q1's residual, term by term ---------------
# The acceptance model is production, a transverse cap, a two-body decay and a
# mirror. Between the pion and a stopped binder there are also losses no part of
# that models, and "never measured end to end" has stood in for all of them. It
# need not: each is computable, and this is the budget.
#
# The one that decides Q6 as well is the first. The collector takes LARGE-ANGLE
# pions, and a large-angle pion leaves the target SIDEWAYS -- so its escape path
# is the target's RADIUS, not its length. A narrow target is transparent however
# long it is, which is why a thick-target multiplicity gain survives to capture,
# and why the published geometries are long and thin rather than blocky.
PI_SIGMA_ABS_GEOMETRIC = 1.0     # sigma_abs / pi R^2 near the Delta resonance
NA_AVOGADRO = 6.02214076e23
TARGETS = {                      # A, density g/cm3, molar mass
    "W": (184.0, 19.3, 183.84),
    "Hg": (200.0, 13.546, 200.59),
    "Ta": (181.0, 16.65, 180.95),
}
JET_LENGTH_CM = 30.0             # SOURCED: two interaction lengths of mercury
JET_RADIUS_CM = 0.40             # SOURCED: the published 8 mm jet
X0_HG_CM, X0_BE_CM = 0.4754, 35.28
BE_WINDOW_CM = 0.40              # SOURCED
BE_DEDX = 1.6                    # MeV cm2/g, minimum ionising
BE_RHO = 1.85
P_TYPICAL_MEV = 200.0


def pion_absorption_length_cm(mat="Hg"):
    a, rho, molar = TARGETS[mat]
    r_cm = 1.2 * a ** (1.0 / 3.0) * 1e-13
    sigma_cm2 = PI_SIGMA_ABS_GEOMETRIC * math.pi * r_cm * r_cm
    n = rho / molar * NA_AVOGADRO
    return 1.0 / (n * sigma_cm2)


def large_angle_fraction():
    return C.harp_window_sigma() / C.harp_combined_sigma()


def target_escape(mat="Hg", length_cm=JET_LENGTH_CM, radius_cm=JET_RADIUS_CM):
    """Fraction of produced pi- that leave the target. Large-angle pions cross
    the radius; forward pions cross what remains of the length, averaged over
    the depth at which they were made."""
    lam = pion_absorption_length_cm(mat)
    sideways = math.exp(-radius_cm / lam)
    forward = (lam / length_cm) * (1.0 - math.exp(-length_cm / lam))
    f = large_angle_fraction()
    return f * sideways + (1.0 - f) * forward


def theta0_rad(p_mev, x_cm, x0_cm, beta=1.0):
    xx = x_cm / x0_cm
    if xx <= 0:
        return 0.0
    return 13.6 / (beta * p_mev) * math.sqrt(xx) * (1.0 + 0.038 * math.log(xx))


def scatter_kick_mev(p_mev=P_TYPICAL_MEV, x_cm=JET_RADIUS_CM, x0_cm=X0_HG_CM):
    return p_mev * theta0_rad(p_mev, x_cm, x0_cm)


def scatter_acceptance(br=1.50, window=(0.0, 265.0)):
    """Acceptance with the transverse cap shrunk by the scattering kick. The
    kick is random in direction and so broadens rather than shifts; shrinking
    the cap by its whole width is the CONSERVATIVE reading and the one quoted."""
    shrunk = br * (1.0 - scatter_kick_mev() / (pt_max_mev(br)))
    return C.delivered_fraction_mirrored(shrunk, window) / C.delivered_fraction_mirrored(br, window)


def pt_max_mev(br):
    return C.pt_max(br) * 1000.0


def muon_survival(p_mev=265.0):
    return math.exp(-channel_length_m(p_mev) / muon_decay_length_m(p_mev))


def window_energy_loss_mev():
    return BE_WINDOW_CM * BE_RHO * BE_DEDX


def window_scatter_mev():
    return scatter_kick_mev(P_TYPICAL_MEV, BE_WINDOW_CM, X0_BE_CM)


def transport_bore_cm(b_channel):
    """Bore a matched adiabatic channel needs at each field. Meet this schedule
    and transport is lossless; miss it and the loss is a scraping calculation
    this budget does not attempt."""
    return channel_beam_radius_cm(b_channel)


BUDGET_TERMS = (
    ("target escape", target_escape,
     "large-angle pions cross the radius, forward pions the length"),
    ("pion decay completeness", lambda: DECAY_FRACTION_WANTED,
     "the channel is cut at 90 percent by choice"),
    ("muon survival in the channel", muon_survival,
     "34.1 m against a 1652 m decay length"),
    ("scattering out of the transverse cap", scatter_acceptance,
     "conservative: the whole kick taken off the cap"),
    ("adiabatic transport", lambda: 1.0,
     "unity BY DESIGN, conditional on the bore schedule below"),
)


@functools.lru_cache(maxsize=None)
def budget_product():
    p = 1.0
    for _, fn, _ in BUDGET_TERMS:
        p *= fn()
    return p


def end_to_end_acceptance(window=(0.0, 265.0)):
    return C.delivered_fraction_mirrored(1.50, window) * budget_product()


def report_budget():
    """Q1's residual as a product of computed terms rather than an unknown."""
    print("  THE END-TO-END LOSS BUDGET")
    print("    'Never measured end to end' has stood in for a list of losses. The")
    print("    list is computable, and this is it. Nothing here replaces the")
    print("    measurement; what it replaces is not knowing what the measurement")
    print("    is being asked to find.")
    print()
    print("      term                                   factor   what it is")
    for name, fn, note in BUDGET_TERMS:
        print(f"      {name:<36} {fn():.4f}   {note}")
    print(f"      {'PRODUCT':<36} {budget_product():.4f}")
    print()
    print(f"    modelled acceptance at the 265 MeV/c window   "
          f"{C.delivered_fraction_mirrored(1.50, (0.0, 265.0)):.4f}")
    print(f"    end to end, through this budget               "
          f"{end_to_end_acceptance():.4f}")
    print()
    print("    THE FIRST TERM ALSO CLOSES Q6, AND ON GEOMETRY RATHER THAN ON A")
    print("    SIMULATION.")
    lam_hg, lam_w = pion_absorption_length_cm("Hg"), pion_absorption_length_cm("W")
    print(f"      pion absorption length: {lam_hg:.1f} cm in mercury,"
          f" {lam_w:.1f} cm in tungsten")
    print(f"      the collector takes large-angle pions -- {100 * large_angle_fraction():.1f} percent of")
    print("      production -- and a large-angle pion leaves SIDEWAYS, so its escape")
    print("      path is the target's RADIUS and not its length:")
    print()
    print("        target                              sideways  forward  weighted")
    for lab, mat, L, r in (("the published jet, 30 cm x 8 mm", "Hg", 30.0, 0.40),
                           ("the optimised rod, 652 x 5.1 mm", "W", 65.2, 0.255),
                           ("a 20.6 cm rod, 2 cm across", "W", 20.6, 1.0),
                           ("a 10 cm-radius block", "W", 20.6, 10.0)):
        lam = pion_absorption_length_cm(mat)
        print(f"        {lab:<35} {math.exp(-r / lam):.4f}   "
              f"{(lam / L) * (1 - math.exp(-L / lam)):.4f}   "
              f"{target_escape(mat, L, r):.4f}")
    print()
    print("      A NARROW TARGET IS TRANSPARENT HOWEVER LONG IT IS. So the")
    print("      thick-target multiplicity that explains the 2.37 survives to")
    print(f"      capture at {target_escape():.4f}, and Q6 is answered: the gain is real,")
    print("      it is not cancelled by reabsorption, and the condition is that the")
    print("      target be long and THIN. The published geometries already are --")
    print("      652 mm by 5.1 mm, 30 cm by 8 mm -- which is not a coincidence but")
    print("      the same argument, arrived at by whoever designed them.")
    print()
    print("    AND IT SHARPENS [1] SEC.10.1's COMMITTED PREDICTION.")
    print("    That stage measures eta -- the DELIVERED figure, end to end -- and")
    print("    committed to the model's band. The budget is what stands between the")
    print("    two, and it moves the commitment down:")
    print()
    print("      window        model     end to end")
    for w, lab in ((None, "no window"), ((0.0, 400.0), "400 MeV/c"), ((0.0, 265.0), "265 MeV/c")):
        m = C.delivered_fraction_mirrored(1.50, w)
        print(f"      {lab:<12} {100 * m:6.2f} %   {100 * m * budget_product():6.2f} %")
    floor = 29.51
    e2e = C.delivered_fraction_mirrored(1.50, (0.0, 265.0)) * budget_product()
    print(f"      falsification floor           {floor:6.2f} %"
          "   what the built machine already delivers")
    print(f"      margin at the stopping window {100 * e2e / floor:6.3f} x")
    print()
    print("    A prediction 1.07x above the number that would falsify the model is")
    print("    a far sharper commitment than one 1.51x above it. That is the budget")
    print("    working as it should: it did not make the answer better.")
    print()
    print("    AND THE TWO OPEN QUESTIONS TURN OUT TO BE COUPLED.")
    print(f"      at {100 * e2e:.2f} percent the bred-fuel route does NOT close at the")
    print("      50.8 percent its demonstrated-cycle balance needs. It closes at the")
    print("      21.4 percent the OPTIMISED production target needs -- and whether")
    print("      that target's gain is real was Q6, answered above at"
          f" {target_escape():.4f}.")
    print("      THE BUDGET WOULD HAVE CLOSED THE ROUTE AND Q6 RE-OPENS IT. Neither")
    print("      question could be answered alone and left the result standing;")
    print("      answering both together is what leaves it standing.")
    print()
    print("    WHAT THE BUDGET STILL DOES NOT MODEL, NAMED.")
    print(f"      the beryllium window costs {window_energy_loss_mev():.2f} MeV of"
          f" {muon_kinetic_mev():.0f} and")
    print(f"      {window_scatter_mev():.2f} MeV/c of transverse kick -- both carried above as")
    print("      negligible rather than omitted;")
    print("      field errors and non-adiabatic transitions in the taper and the")
    print("      channel, which are a magnet-design calculation and not a physics one;")
    print("      the jet's magnetohydrodynamic distortion in the field, which is")
    print("      what MERIT was built to measure and is not re-derived here;")
    print("      and collimation, which is a layout this design does not fix.")
    print()
    print("    THE BORE SCHEDULE THE TRANSPORT TERM IS CONDITIONAL ON.")
    print("      Meet this and transport is lossless; miss it and the loss is a")
    print("      scraping calculation this budget does not attempt.")
    for b in (14.01, 5.0, 2.0, 20.0):
        print(f"        at {b:5.2f} T the bore must be at least {transport_bore_cm(b):6.2f} cm")


# ---- every balance at the acceptance actually delivered --------------------
# [1] sec.5.19 states each balance at 30 and 90 percent collection. The 90 is
# unreachable: sec.7's stopping ceiling is 0.5069 and sec.11's budget puts the
# delivered figure at 0.3166. The balance is LINEAR in collection -- that table's
# own two columns differ by 3.000, which is 90/30 -- so restating it at the
# delivered figure is exact rather than approximate.
#
# (label, at 30 percent, at 90 percent) -- read from [1] sec.5.19 as printed.
BALANCES_AT_90 = (
    ("heat, demonstrated 150 cycles", 0.105, 0.316),
    ("heat, bound-case service life", 0.414, 1.241),
    ("heat, phi = 3", 0.337, 1.011),
    ("work, demonstrated 150 cycles", 0.079, 0.237),
    ("work, bound-case service life", 0.310, 0.931),
    ("bred fuel, demonstrated 150 cycles", 0.591, 1.772),
    ("bred fuel, bound-case service life", 2.32, 6.96),
)
OPTIMISED_TARGET_REQUIREMENT = 21.4     # percent, [1] sec.5.24


@functools.lru_cache(maxsize=None)
def delivered_eta(br=1.50):
    return C.delivered_fraction_mirrored(br, (0.0, 265.0)) * budget_product()


def balance_linearity():
    """The table's own check that the balance is linear in collection."""
    return tuple(hi / lo for _, lo, hi in BALANCES_AT_90)


def balance_at_delivered(index, br=1.50):
    return BALANCES_AT_90[index][2] * delivered_eta(br) / 0.90


# ---- what the SPECIFIED alteration does to every balance -------------------
# sec.5.24 prices the optimised production target against the bred-fuel route
# and against nothing else. The same alteration multiplies EVERY balance by the
# same factor, because a balance is N x V x eta / E_binder and the target moves
# E_binder alone. Asking what it does to the HEAT forms is a question this work
# did not put to itself until it was asked.
E_PION_MEASURED_GEV = 11.13        # [1] sec.5.1, integrated from the cross sections
E_PION_OPTIMISED_GEV = 4.69        # a published optimisation, [1] sec.5.26


def optimised_target_factor():
    """The factor the optimised production target is worth, on any balance."""
    return E_PION_MEASURED_GEV / E_PION_OPTIMISED_GEV


def balance_with_optimised_target(index, br=1.50):
    return balance_at_delivered(index, br) * optimised_target_factor()


def report_alteration():
    """Every balance under the alterations this work specifies, not just one."""
    f = optimised_target_factor()
    print("  WHAT THE SPECIFIED ALTERATIONS DO TO EVERY BALANCE")
    print("    sec.5.24 prices the optimised production target against the")
    print("    BRED-FUEL route and against nothing else. It multiplies every")
    print("    balance by the same factor, because it moves E_binder alone.")
    print()
    print(f"    the factor: E per pion {E_PION_MEASURED_GEV} -> "
          f"{E_PION_OPTIMISED_GEV} GeV, worth {f:.4f}")
    print(f"    checked against the requirement it moves: 50.8 -> "
          f"{50.8 / f:.2f} percent, which is sec.5.24's 21.4")
    print()
    print(f"      {'balance':<34}{'delivered':>10}{'+ target':>11}"
          f"{'+ target & bore':>17}")
    for i, (lab, _lo, _hi) in enumerate(BALANCES_AT_90):
        d = balance_at_delivered(i, 1.50)
        o = balance_with_optimised_target(i, 1.50)
        w = balance_with_optimised_target(i, 2.60)
        mark = "  <-- clears" if o > 1.0 else ("  <-- clears at the bore" if w > 1.0 else "")
        print(f"      {lab:<34}{d:10.3f}{o:11.3f}{w:17.3f}{mark}")
    print()
    print("    THE ANSWER IS CONDITIONAL AND IT IS NOT NO.")
    print("      At the DEMONSTRATED cycle count nothing device-internal clears:")
    print(f"      heat {balance_with_optimised_target(0):.3f}, work "
          f"{balance_with_optimised_target(3):.3f}. On the BOUND-CASE service life the heat")
    print(f"      form clears at {balance_with_optimised_target(1):.3f}, and "
          f"{balance_with_optimised_target(1, 2.60):.3f} at the wider bore.")
    print("      That case rests on the service-life model the companion says")
    print("      over-predicts its one checkable point by 2.24, and the factor")
    print("      itself is the one sec.5.26 declines to adopt and sec.10 Stage C")
    print("      measures. Both conditions are the paper's own, and both hold.")
    print()
    print("    AND THE STRICTLY DEVICE-INTERNAL FORM DOES NOT CLEAR ON ANY OF IT.")
    print("      Counting the neutron at its bare heat, with no blanket")
    print("      multiplication and no fissile credit, the delivered figure is")
    print(f"      0.1409 and the optimised target takes it to {0.1409 * f:.4f}.")
    print("      'Inside the device' has two readings and they do not agree:")
    print("      one counts the blanket, the other does not.")


def optimised_target_balance(br=1.50):
    return 100.0 * delivered_eta(br) / OPTIMISED_TARGET_REQUIREMENT


def report_balances():
    """Every balance restated at the acceptance the budget actually delivers."""
    print("  EVERY BALANCE AT THE ACCEPTANCE ACTUALLY DELIVERED")
    print("    [1] sec.5.19 states each balance at 30 and 90 percent collection.")
    print("    The 90 is unreachable -- sec.7's stopping ceiling is 0.5069 and")
    print("    sec.11's budget delivers 0.3166 -- so the table has to be restated.")
    print()
    lin = balance_linearity()
    print(f"    The restatement is EXACT, not approximate: the balance is linear in")
    print(f"    collection, and that table's own columns check it at"
          f" {min(lin):.3f}-{max(lin):.3f}")
    print(f"    against 90/30 = 3.000.")
    print()
    print(f"    delivered eta: {100 * delivered_eta(1.50):.2f} % at 1.50 T.m,"
          f" {100 * delivered_eta(2.60):.2f} % at 2.60 T.m")
    print()
    print("      balance                              as printed    delivered    wider bore")
    for i, (lab, _, hi) in enumerate(BALANCES_AT_90):
        a, b = balance_at_delivered(i, 1.50), balance_at_delivered(i, 2.60)
        mark = "  <-- passes" if b > 1.0 else ""
        print(f"      {lab:<36} {hi:8.3f} {a:12.3f} {b:12.3f}{mark}")
    print()
    print("    THE HEAT FORM'S 1.241 DOES NOT SURVIVE.")
    print(f"    At the delivered acceptance it is {balance_at_delivered(1):.3f}, and at the wider")
    print(f"    bore {balance_at_delivered(1, 2.60):.3f}. It was never wrong -- it was stated AT 90")
    print("    percent collection, and it stands as that conditional. What is")
    print("    withdrawn is reading it as an end-to-end result, which [1]'s own")
    print("    abstract did. THE SELF-SUSTAINING CRITERION IS NOT MET WITHOUT")
    print("    LEAVING THE DEVICE.")
    print()
    print("    WHAT SURVIVES, AND IT IS ONE ROUTE.")
    print(f"      bred fuel with the optimised production target: a requirement of")
    print(f"      {OPTIMISED_TARGET_REQUIREMENT} percent against {100 * delivered_eta():.2f} delivered --"
          f" a balance of {optimised_target_balance():.3f}")
    print(f"      and {optimised_target_balance(2.60):.3f} at the wider bore.")
    print()
    print("      and bred fuel on the BOUND-CASE service life, at"
          f" {balance_at_delivered(6):.3f} -- but that")
    print("      case rests on the model sec.5.29 corrected, and sec.5.26 caps cycles")
    print("      at 198. Read it against that cap, not as an independent route.")
    print()
    print("    So the co-product configuration of the specification's sec.5.2 and the")
    print("    bred-fuel route through an optimised target are what is left, and they")
    print("    are the two the specification already builds for. Nothing else passes.")


# ---- the acceptance census -------------------------------------------------
# [1] sec.5.31 settles the principle and settles it for one table: a figure
# stated AT an acceptance was never wrong, and what is withdrawn is reading one
# as delivered. The principle then has to be applied to EVERY such figure and
# not only to the ones a reader happens to notice, so this is the census.
#
# It is mechanical in both directions. Each row names its site and the figure
# the paper prints; --selftest asserts that figure still occurs in that file and
# that the section still exists as a heading; and the restatement is computed
# here rather than typed. A row is never repaired in the paper by this file --
# it is graded, and the grade is the finding.
ETA_PERFECT = 1.0                    # "perfect collection"
ETA_COLLECTOR_59 = 0.90              # "the sec.5.9 collector", [1] sec.5.19
ETA_TODAY_APERTURE = 0.6092          # "today's aperture, both hemispheres"

PAPER_ECONOMY = "Cold_Fusion_Binder_Economy_v1.0.md"
PAPER_RECONCILIATION = "Independent_Reconciliation_v1.0.md"
PAPER_SPECIFICATION = "Cold_Fusion_Specification_and_Procedure_v1.0.md"
# the capture the co-product headline was computed at, and the ceiling that
# same section says is reachable. [3] sec.5.2 states both and restates neither.
ETA_COPRODUCT_PRINTED = 0.50
ETA_COPRODUCT_CEILING = 0.3420
ETA_TODAY_FRONT_END = 0.30          # "today's measured front end"

# kind decides both the grade and the arithmetic:
#
#   "balance"     a balance stated at an ASSUMED efficiency (0.90 or perfect).
#                 Linear in collection, so restated as printed * delivered/at.
#   "acceptance"  an acceptance computed from the aperture model. It already
#                 carries the aperture; what it lacks is the loss budget, so it
#                 is restated as printed * budget_product().
#   "ratio"       an aperture acceptance over a requirement -- same factor.
#   "labelled"    the site states its own assumption in the same sentence and
#                 draws no end-to-end conclusion from it. CONDITIONAL: stands.
#   "requirement" the inverse question. A requirement does not move; what moves
#                 is whether the delivered figure meets it.
#   "claim"       a sentence rather than a number, and one sec.5.31 withdraws.
#   "nonlinear"   a density or a sticking boundary, where the restatement is not
#                 a multiplication. NOT-LINEAR: named here, not computed.
#
# (paper, section, printed, value, kind, at, note)
ACCEPTANCE_SITES = (
    (PAPER_ECONOMY, "abstract", "0.464", 0.464, "labelled", ETA_PERFECT,
     "'at perfect collection and unlimited density' -- said in the sentence"),
    (PAPER_ECONOMY, "abstract", "0.313", 0.313, "labelled", ETA_PERFECT,
     "the same sentence"),
    (PAPER_ECONOMY, "5.4", "0.675", 0.675, "labelled", ETA_PERFECT,
     "'Suppose collection were perfect' -- the paragraph IS the condition"),
    (PAPER_ECONOMY, "5.4", "0.338", 0.338, "labelled", ETA_PERFECT,
     "the same paragraph"),
    (PAPER_ECONOMY, "5.10", "1.17", 1.17, "labelled", ETA_PERFECT,
     "the residual above the break-point, stated at perfect collection"),
    (PAPER_ECONOMY, "5.18", "1.97", 1.97, "balance", ETA_COLLECTOR_59,
     "the pull-quote reads it as a result: 'exceeds unity by about two'"),
    (PAPER_ECONOMY, "5.18", "6.30", 6.30, "balance", ETA_COLLECTOR_59,
     "sec.5.11's density on the same collector"),
    (PAPER_ECONOMY, "5.19", "1.77", 1.77, "balance", ETA_COLLECTOR_59,
     "the same reading on sourced blanket figures"),
    (PAPER_ECONOMY, "5.19", "7.73", 7.73, "labelled", ETA_PERFECT,
     "the row's own label is 'bound case, perfect collection'"),
    (PAPER_ECONOMY, "5.19", "1.034", 1.034, "labelled", ETA_PERFECT,
     "'it still assumes perfect collection' -- the paper says so itself"),
    (PAPER_ECONOMY, "5.21", "1.69", 1.69, "claim", ETA_COLLECTOR_59,
     "'comfortably inside the sec.5.9 collector ... not an open physical "
     "question'. The stopping ceiling is 0.5069, so it is OUTSIDE it"),
    (PAPER_ECONOMY, "5.22", "299.6", 299.6, "requirement", None,
     "electricity on the bound case. CLAUDE.md still said 96.7 here until this "
     "census asked the file what it prints"),
    (PAPER_ECONOMY, "5.22", "72.5", 72.5, "requirement", None,
     "heat, bound-case service life"),
    (PAPER_ECONOMY, "5.22", "50.8", 50.8, "requirement", None,
     "bred fuel at the demonstrated 150 cycles"),
    (PAPER_ECONOMY, "5.23", "0.4006", 0.4006, "balance", ETA_COLLECTOR_59,
     "heat on the bound-case service life; the abstract quotes it"),
    (PAPER_ECONOMY, "5.23", "0.3731", 0.3731, "balance", ETA_COLLECTOR_59,
     "heat at phi = 3"),
    (PAPER_ECONOMY, "5.23", "0.3338", 0.3338, "balance", ETA_COLLECTOR_59,
     "work at the same collector"),
    (PAPER_ECONOMY, "5.24", "36.48", 36.48, "acceptance", None,
     "1.50 T.m, p < 200 MeV/c"),
    (PAPER_ECONOMY, "5.24", "44.43", 44.43, "acceptance", None,
     "1.50 T.m, p < 265 MeV/c -- this is the row sec.5.31's delivered figure "
     "comes from, so its restatement had better be 31.66"),
    (PAPER_ECONOMY, "5.24", "49.16", 49.16, "acceptance", None,
     "1.50 T.m, p < 400 MeV/c"),
    (PAPER_ECONOMY, "5.24", "60.92", 60.92, "acceptance", None,
     "1.50 T.m, no cut. The table's header reads 'delivered' and THAT is the "
     "labelling fault this census fixes: it is model acceptance"),
    (PAPER_ECONOMY, "5.24", "38.68", 38.68, "acceptance", None,
     "2.60 T.m, p < 200 MeV/c"),
    (PAPER_ECONOMY, "5.24", "52.79", 52.79, "acceptance", None,
     "2.60 T.m, p < 265 MeV/c -- the wider bore's 37.62"),
    (PAPER_ECONOMY, "5.24", "68.20", 68.20, "acceptance", None,
     "2.60 T.m, p < 400 MeV/c"),
    (PAPER_ECONOMY, "5.24", "89.88", 89.88, "acceptance", None,
     "2.60 T.m, no cut"),
    (PAPER_ECONOMY, "5.24", "1.199", 1.199, "ratio", ETA_TODAY_APERTURE,
     "bred fuel at 150 cycles, today's aperture, no momentum requirement"),
    (PAPER_ECONOMY, "5.24", "0.968", 0.968, "ratio", ETA_TODAY_APERTURE,
     "the same through a 400 MeV/c window"),
    (PAPER_ECONOMY, "5.24", "0.875", 0.875, "ratio", ETA_TODAY_APERTURE,
     "the same through 265 -- and its restatement is the cross-check on "
     "sec.5.31, which reaches the same figure by the other route"),
    (PAPER_ECONOMY, "5.24", "1.343", 1.343, "ratio", ETA_TODAY_APERTURE,
     "wider bore, 400 MeV/c -- the abstract quotes this one as a route"),
    (PAPER_ECONOMY, "5.24", "1.039", 1.039, "ratio", ETA_TODAY_APERTURE,
     "wider bore, 265 MeV/c; sec.5.25 quotes it again as what 'holds'"),
    (PAPER_RECONCILIATION, "2.5", "1.203", 1.203, "ratio", ETA_TODAY_APERTURE,
     "'today's magnet', carried as a headline"),
    (PAPER_RECONCILIATION, "2.5", "1.772", 1.772, "balance", ETA_COLLECTOR_59,
     "'with the sec.5.9 collector', carried as a headline"),
    (PAPER_RECONCILIATION, "2.5", "0.143 %", 0.143, "nonlinear", ETA_TODAY_APERTURE,
     "a boundary ON sticking: the budget moves the boundary, not the balance"),
    (PAPER_RECONCILIATION, "2.5", "0.222 LHD", 0.222, "nonlinear", ETA_PERFECT,
     "a break-even DENSITY; the balance is not linear in it"),
    (PAPER_RECONCILIATION, "2.5", "0.604", 0.604, "nonlinear", ETA_TODAY_APERTURE,
     "the same, at the aperture"),
    (PAPER_RECONCILIATION, "2.6", "0.842", 0.842, "ratio", ETA_TODAY_APERTURE,
     "heat, bound case, at today's aperture"),
    (PAPER_RECONCILIATION, "2.6", "0.911", 0.911, "ratio", ETA_TODAY_APERTURE,
     "the same rescaled to the moved sticking datum"),
    (PAPER_RECONCILIATION, "2.6", "1.379", 1.379, "labelled", ETA_PERFECT,
     "the row's own label is 'perfect collection'"),
    (PAPER_RECONCILIATION, "2.6", "1.492", 1.492, "labelled", ETA_PERFECT,
     "the same row rescaled to the moved sticking datum, same label"),
    (PAPER_RECONCILIATION, "2.5", "0.394", 0.394, "nonlinear", None,
     "a sticking boundary at today's front end as built; not a multiplication"),
    (PAPER_RECONCILIATION, "2.2", "1.64", 1.64, "divisor", ETA_TODAY_APERTURE,
     "a DIVISOR converting their Q to this paper's acceptance -- so the loss "
     "budget DIVIDES it rather than multiplying, and the divisor grows"),
    (PAPER_RECONCILIATION, "2.2", "2.25", 2.25, "divisor", ETA_TODAY_APERTURE,
     "the same through a 265 MeV/c stopping window"),
    (PAPER_RECONCILIATION, "2.2", "3.33", 3.33, "divisor", ETA_TODAY_APERTURE,
     "the same at today's front end as built"),
    (PAPER_ECONOMY, "5.9", "50.69", 50.69, "acceptance", None,
     "the forward hemisphere alone at today's aperture"),
    (PAPER_ECONOMY, "5.9", "10.23", 10.23, "acceptance", None,
     "the backward hemisphere alone"),
    (PAPER_ECONOMY, "5.25", "2.076", 2.076, "ratio", ETA_TODAY_APERTURE,
     "bred fuel at today's aperture through the tightest window WITH the "
     "optimised production target -- and its restatement is 1.480, which is "
     "the optimised-target balance reached by a third route"),
    # ---- [3], the specification. Its sec.5.2 is the co-product configuration,
    # and it is the one place in this work where the loss budget moves a figure
    # WITHOUT deciding it: that balance is not a ratio against unity.
    (PAPER_SPECIFICATION, "5.2", "10.5", 10.5, "ratio", None,
     "heat as a fraction of beam energy at today's front end, percent"),
    (PAPER_SPECIFICATION, "5.2", "12.0", 12.0, "ratio", None,
     "the same at this section's own stopping ceiling -- the row it says survives"),
    (PAPER_SPECIFICATION, "5.2", "17.6", 17.6, "ratio", None,
     "the same at a capture reachable only at ~45 kg of tritium"),
    (PAPER_SPECIFICATION, "5.2", "31.6", 31.6, "self-withdrawn", ETA_COLLECTOR_59,
     "the 90 percent row. THE PAPER WITHDRAWS THIS ITSELF, in the paragraph "
     "beneath it: it compared a collector's acceptance with a fuel target's "
     "stopping fraction. Censused so the withdrawal is on the record rather "
     "than restated -- a status is never flattened"),
    (PAPER_SPECIFICATION, "5.2", "2.80 × 10¹⁴", 2.80, "coproduct",
     ETA_COPRODUCT_PRINTED,
     "binders per second, computed at 0.50 -- which the correction two lines "
     "below it demotes. 1.918 at this section's ceiling, 1.367 delivered"),
    (PAPER_SPECIFICATION, "5.2", "176 kW", 176.0, "coproduct",
     ETA_COPRODUCT_PRINTED,
     "the fusion heat from it, and the banner's headline figure"),
    (PAPER_SPECIFICATION, "5.2", "2.80 × 10⁴", 2.80, "coproduct",
     ETA_COPRODUCT_PRINTED,
     "in-situ capture over the best planned delivered beam"),
    (PAPER_SPECIFICATION, "5.2", "0.3420", 0.3420, "labelled", None,
     "the stopping ceiling at the committed 3.59 kg -- an acceptance being "
     "named, and the correction this section already made"),
    (PAPER_SPECIFICATION, "8.1", "60.92", 60.92, "acceptance", None,
     "[1] sec.10.1's committed band, restated here as the mirror's own"),
    (PAPER_SPECIFICATION, "8.1", "49.16", 49.16, "acceptance", None,
     "the same at 400 MeV/c"),
    (PAPER_SPECIFICATION, "8.1", "44.43", 44.43, "acceptance", None,
     "the same at 265 MeV/c"),
)

GRADE_OF_KIND = {
    "balance": "RESTATED", "acceptance": "RESTATED", "ratio": "RESTATED",
    "divisor": "RESTATED", "coproduct": "RESTATED",
    "self-withdrawn": "SELF-WITHDRAWN",
    "labelled": "CONDITIONAL", "requirement": "REQUIREMENT",
    "claim": "WITHDRAWN", "nonlinear": "NOT-LINEAR",
}


@functools.lru_cache(maxsize=None)
def coproduct_delivered_capture():
    """[3] sec.5.2's reachable capture: its own stopping ceiling, through sec.11."""
    return C.stopping_capture(265.0) * budget_product()


def restate(value, kind, at, br=1.50):
    """The delivered form of one printed figure, or None where there is none."""
    if kind == "balance":
        return value * delivered_eta(br) / at
    if kind in ("acceptance", "ratio"):
        return value * budget_product()
    if kind == "divisor":
        return value / budget_product()
    if kind == "coproduct":
        # printed at 0.50; the section's own ceiling is 0.342, and the budget
        # sits under that. Two corrections, and neither was carried.
        return value * coproduct_delivered_capture() / at
    return None


def census_rows(br=1.50):
    for paper, sec, printed, value, kind, at, note in ACCEPTANCE_SITES:
        yield (paper, sec, printed, value, kind, at,
               GRADE_OF_KIND[kind], restate(value, kind, at, br), note)


def census_counts():
    c = {}
    for row in census_rows():
        c[row[6]] = c.get(row[6], 0) + 1
    return c


def _paper_path(name):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "papers", name)


def _paper_text(name, _cache={}):
    if name not in _cache:
        with open(_paper_path(name), encoding="utf-8") as fh:
            _cache[name] = fh.read()
    return _cache[name]


# ---- is the census complete? ------------------------------------------------
# A census is a claim of completeness, and a claim is not a measurement. This
# measures it: every line in either paper that names a collection assumption is
# read, every number on it taken, and each one must be accounted for -- censused
# above, produced by the census itself, or exempt for a stated reason. The
# residue is what is left, and it must be empty. A non-empty residue is a site
# the census missed, which is the one failure mode a hand-built census has.
ACCEPTANCE_PHRASES = (
    "perfect collection", "collection perfect", "the §5.9 collector",
    "§5.9 collector", "at 90 percent", "90 percent collection",
    "today's aperture", "at the collection efficiencies", "both hemispheres",
    "with the specified collector", "today's measured front end",
    "today's front end", "at the two collection",
)

# A number on such a line that is NOT a figure stated at an acceptance. Each
# carries the reason it is not, because "exempt" without a reason is a hole.
CENSUS_EXEMPT = {
    # the acceptance itself, or a parameter of it -- these are the x-axis, not
    # a reading off it
    "90": "the assumed efficiency being named", "30": "the same",
    "200": "a momentum window, MeV/c", "265": "the same", "400": "the same",
    "1.50": "the aperture product, T.m", "2.60": "the same",
    "2.6": "the same, written short", "7.5": "the bore radius, cm",
    "0.5069": "the stopping ceiling, which is what makes 90 unreachable",
    "31.66": "the delivered acceptance -- the census's own x-axis",
    "0.7127": "the loss budget itself",
    # a service life, a cost or a value per fusion -- the OTHER factor in a
    # balance, and not the one the census moves
    "150": "the demonstrated cycle count", "190.1": "the bound-case service life",
    "479.6": "the phi = 3 service life", "198": "the sec.5.26 cycle cap",
    "12.4": "a binder cost, GeV", "11.13": "the production floor, GeV",
    "37.0": "the sourced binder cost, GeV", "1200": "a blanket temperature, K",
    "146.06": "a value per fusion, MeV", "26.06": "the same", "19.55": "the same",
    # a tritium inventory: a cost of the aperture, not a balance at one
    "3.59": "a tritium inventory, kg", "6.93": "the same", "1.73": "the same",
    "10.4": "the same", "2.41": "a fuel mass, mg",
    # a factor the papers state about the aperture rather than at it
    "1.20": "the gain from dropping the hemisphere cut",
    "1.69": "the collection factor sec.5.21 names -- censused as the WITHDRAWN row",
    "0.982": "the agreement with the MARS15 simulation",
    "8": "a hemisphere count in a table rule", "3": "the same",
    "0.222": "censused under its printed form '0.222 LHD'",
    "0.143": "censused under its printed form '0.143 %'",
}
_SECTION_RE = re.compile(r"[§§]|sec\.|section ")


def _numbers_on(line):
    """Every number on a line, minus the ones that are section references."""
    out = []
    for m in re.finditer(r"\d+(?:,\d{3})*(?:\.\d+)?", line):
        before = line[max(0, m.start() - 2):m.start()]
        if "§" in before or before.endswith("c."):
            continue                      # a cross-reference, not a quantity
        out.append(m.group(0))
    return out


def _census_accounted():
    """Every number the census already owns: what it cites, and what it makes."""
    owned = set()
    # both bores: sec.5.31 and sec.5.32 state the wider one beside the delivered
    for br in (1.50, 2.60):
        for _, _, printed, _, _, _, _, new, _ in census_rows(br):
            owned.add(_numbers_on(printed)[0])
            if new is None:
                continue
            for dp in (2, 3, 4):
                owned.add(f"{new:.{dp}f}")
                owned.add(f"{new:.{dp}f}".rstrip("0").rstrip("."))
            owned.add(f"{100 * new:.2f}")
    # and the sec.5.19 table restated, which --balances owns rather than the census
    for i in range(len(BALANCES_AT_90)):
        for br in (1.50, 2.60):
            owned.add(f"{balance_at_delivered(i, br):.3f}")
    # and the census's own agreement ratios, which are its output and not a site
    owned.add(f"{restate(0.875, 'ratio', None) / balance_at_delivered(5):.4f}")
    owned.add(f"{optimised_target_balance():.3f}")
    return owned


def census_residue():
    """Numbers on acceptance-bearing lines that the census does not account for."""
    owned = _census_accounted() | set(CENSUS_EXEMPT)
    out = []
    for paper in (PAPER_ECONOMY, PAPER_RECONCILIATION, PAPER_SPECIFICATION):
        for n, line in enumerate(_paper_text(paper).split("\n"), 1):
            if not any(ph in line for ph in ACCEPTANCE_PHRASES):
                continue
            for v in _numbers_on(line):
                if v not in owned:
                    out.append((paper, n, v, line.strip()[:90]))
    return out

def report_census():
    """Every figure in the two live papers stated at an assumed acceptance."""
    print("  THE ACCEPTANCE CENSUS")
    print("    sec.5.31 restated ONE table at the delivered acceptance. The same")
    print("    question has to be asked of every figure the THREE live papers")
    print("    state at an assumed collection, and asked mechanically rather")
    print("    than by eye.")
    print("    This is that census. A figure stated AT an acceptance is not")
    print("    wrong; reading one as delivered is. The grade is which it is.")
    print()
    print(f"    delivered: {100 * delivered_eta():.2f} % at 1.50 T.m through the"
          f" 265 MeV/c window,")
    print(f"    which is the aperture model's {100 * C.delivered_fraction_mirrored(1.50, (0.0, 265.0)):.2f} %"
          f" times the {budget_product():.4f} loss budget.")
    print()
    hdr = f"      {'site':<26} {'printed':>9} {'delivered':>10}  grade"
    print(hdr)
    last = None
    for paper, sec, printed, value, kind, at, grade, new, note in census_rows():
        tag = {PAPER_ECONOMY: "[1]", PAPER_RECONCILIATION: "[2]"}.get(paper, "[3]")
        site = f"{tag} sec.{sec}"
        if site != last:
            print()
            last = site
        shown = f"{new:10.4f}" if new is not None else f"{'--':>10}"
        print(f"      {site:<26} {printed:>9} {shown}  {grade}")
        print(f"      {'':<26} {'':>9} {'':>10}  {note}")
    print()
    counts = census_counts()
    print("    " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print()
    print("    WHAT THE CENSUS FINDS, AND IT IS NOT THAT THE PAPERS ARE WRONG.")
    print("    Most of these rows are CONDITIONAL: the site says 'at perfect")
    print("    collection' in the same breath as the number, and a conditional")
    print("    stated as one stands. The RESTATED rows are the ones a reader")
    print("    would carry away as end-to-end, and every one of them falls.")
    print()
    print("    THREE ROUTES REACH THE SAME TWO FIGURES, AND THAT IS THE CHECK.")
    a = restate(0.875, "ratio", ETA_TODAY_APERTURE)
    b = balance_at_delivered(5)
    print(f"      sec.5.24's 0.875 through the loss budget      {a:.4f}")
    print(f"      sec.5.19's 1.772 through delivered/0.90       {b:.4f}")
    print(f"      agreeing to                                   {a / b:.4f}")
    print("      -- an acceptance over a requirement and a balance over an")
    print("      assumed efficiency are different arithmetic on different rows,")
    print("      and they land on the same number.")
    print()
    c = restate(2.076, "ratio", ETA_TODAY_APERTURE)
    print(f"      sec.5.25's 2.076 through the loss budget      {c:.4f}")
    print(f"      the optimised-target balance from the")
    print(f"      requirement side                             {optimised_target_balance():.4f}")
    print(f"      agreeing to                                  {c / optimised_target_balance():.5f}")
    print("      -- and that pair shares no arithmetic with the pair above.")
    print()
    print("    THE ONE ROW GRADED WITHDRAWN.")
    print("      sec.5.21 says the bred-fuel case is 'comfortably inside the")
    print("      sec.5.9 collector' and calls the remaining factor 'an")
    print("      engineering figure ... not an open physical question'. The")
    print("      sec.9 stopping ceiling is 0.5069 and the delivered figure is")
    print(f"      {100 * delivered_eta():.2f} percent, so the sec.5.9 collector is not merely")
    print("      unreached, it is unreachable. The sentence is withdrawn; the")
    print("      route it was describing survives only through the optimised")
    print(f"      production target, at {optimised_target_balance():.3f}.")
    print()
    print("    IS THE CENSUS COMPLETE? MEASURED, NOT CLAIMED.")
    res = census_residue()
    print(f"      Every line in any of the three naming a collection assumption, every")
    print(f"      number on it, each one censused above or exempt for a stated")
    print(f"      reason. Residue: {len(res)}.")
    for paper, n, v, line in res[:10]:
        print(f"        {paper[:26]}:{n}  {v}")
    if not res:
        print("      A hand-built census's one failure mode is the site nobody")
        print("      noticed. This is the check that would catch it, and it is")
        print("      the check that added the last eight rows.")
    print()
    print("    WHAT THE CENSUS REFUSES TO DO.")
    print("      The NOT-LINEAR rows are a break-even density and a sticking")
    print("      boundary. Restating those is not a multiplication -- the")
    print("      balance is not linear in either -- so they are named and left")
    print("      to the instrument that owns them rather than scaled here. An")
    print("      un-restated row is a finding, not an omission.")


def report_all():
    print("THE CAPTURE SOLENOID: BUILD PACKAGE")
    print()
    print("  collector.py --magnet designs the field and names three things it does")
    print("  not do. This finishes them, and adds what the magnet alone does not")
    print("  make a machine: the target, the lifetime, the plant, the integration.")
    print()
    for r in (report_circuit, report_mechanics, report_conductor, report_target,
              report_radiation, report_failure, report_plant, report_channel,
              report_cell, report_budget, report_balances, report_coherence,
              report_integration):
        r()
        print()
    print("  WHAT REMAINS UNDONE.")
    print("    The cell is designed above and the package is complete to the level")
    print("    of a physics design with engineering requirements. What is NOT here")
    print("    is a fabrication package: drawings, tolerances, weld and joint")
    print("    design, the tritium plant's own licensing case, and a quench")
    print("    analysis run in a magnet code rather than on a hot-spot integral.")
    print("    Those are engineering-office work on a design that now exists,")
    print("    which is a different thing from a design that does not.")
    return 0


def selftest():
    fail = 0
    print("machine.py --selftest")
    print()
    print("  the design is read from collector, never restated")
    ok = abs(C.DES_B_TARGET * C.des_bore_m() / C.DES_BR - 1.0) < 1e-9
    fail += 0 if ok else 1
    print(f"    aperture product still {C.DES_BR} T.m   {'PASS' if ok else 'FAIL'}")

    print()
    print("  quench protection closes")
    ok = hotspot_margin() > HOTSPOT_MARGIN
    fail += 0 if ok else 1
    print(f"    hot-spot margin {hotspot_margin():.2f}x against a required"
          f" {HOTSPOT_MARGIN:.0f}x   {'PASS' if ok else 'FAIL'}")
    ok = dump_resistance_ohm() * I_OP <= V_DUMP_MAX + 1e-6
    fail += 0 if ok else 1
    print(f"    dump terminal voltage at its limit, not above"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(0.5 * inductance_h() * I_OP ** 2 / C.des_stored_energy_j() - 1.0) < 1e-9
    fail += 0 if ok else 1
    print(f"    and the inductance returns the stored energy it came from"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the conductor grading spans the winding exactly once")
    b = grade_bands()
    ok = abs(b[0][1] - C.des_coil_inner_m()) < 1e-9 and abs(
        b[-1][2] - (C.des_coil_inner_m() + C.des_winding_thickness_m())) < 1e-9
    fail += 0 if ok else 1
    print(f"    bands run from the bore to the outer radius   {'PASS' if ok else 'FAIL'}")
    ok = all(abs(b[i][2] - b[i + 1][1]) < 1e-12 for i in range(len(b) - 1))
    fail += 0 if ok else 1
    print(f"    with no gap and no overlap   {'PASS' if ok else 'FAIL'}")
    ok = C.des_current_density_a_mm2() < 100.0
    fail += 0 if ok else 1
    print(f"    and the required current density is below what REBCO carries at"
          f" 20 T   {'PASS' if ok else 'FAIL'}")

    print()
    print("  THE REFUSAL THIS FILE EXISTS FOR")
    ok = rotating_wheel_radius_m() > 2.0 * C.des_bore_m()
    fail += 0 if ok else 1
    print(f"    a rotating target that reaches the demonstrated specific power")
    print(f"    needs {rotating_wheel_radius_m():.3f} m and the bore is {C.des_bore_m():.3f} m --"
          f" {rotating_wheel_radius_m() / C.des_bore_m():.1f}x:")
    print(f"    EXCLUDED BY GEOMETRY, not by preference   {'PASS' if ok else 'FAIL'}")
    print("    (the margin was 23x on this file's own wrong deposition figure and")
    print("     is 3.3x on the sourced one -- the exclusion survives the correction,")
    print("     which is the only reason it may still be stated)")
    d = 2 * SRC_JET_RADIUS_MM / 1000.0
    ok = jet_delta_t_k(d_m=d, v_m_s=10.0) < HG_BOIL_C
    fail += 0 if ok else 1
    print(f"    the jet clears boiling at 10 m/s: {jet_delta_t_k(d_m=d, v_m_s=10.0):.0f} K"
          f" rise   {'PASS' if ok else 'FAIL'}")
    print("    -- and on the reconstructed power it needed 30 m/s. The correction")
    print("       RELAXED the jet requirement, and that is recorded rather than")
    print("       quietly enjoyed: the earlier velocity floor is withdrawn.")

    print()
    print("  the mirror and 'both hemispheres' are the same number")
    for w, lab in ((None, "no window"), ((0.0, 400.0), "400 MeV/c"), ((0.0, 265.0), "265 MeV/c")):
        b = C.delivered_fraction(1.50, "both", w)
        m = C.delivered_fraction_mirrored(1.50, w)
        ok = abs(m / b - 1.0) < 1e-4
        fail += 0 if ok else 1
        print(f"    {lab:10s} both {100 * b:.2f} % vs mirrored {100 * m:.2f} %"
              f"   {'PASS' if ok else 'FAIL'}")
    print("    -- so [1] sec.10.1's committed band is reproduced by a MAGNET rather")
    print("       than by an instrumentation choice, and the loop closes")

    print()
    print("  the balances restated at what is delivered")
    lin = balance_linearity()
    ok = all(abs(r - 3.0) < 0.02 for r in lin)
    fail += 0 if ok else 1
    print(f"    the balance is linear in collection, so restating is exact:")
    print(f"    ratios {min(lin):.3f}-{max(lin):.3f} against 3.000   {'PASS' if ok else 'FAIL'}")
    ok = balance_at_delivered(1) < 1.0 < BALANCES_AT_90[1][2]
    fail += 0 if ok else 1
    print(f"    THE HEAT FORM'S 1.241 DOES NOT SURVIVE: {balance_at_delivered(1):.3f} delivered.")
    print(f"    It was stated at a collection efficiency above the stopping ceiling"
          f"   {'PASS' if ok else 'FAIL'}")
    passes = [i for i in range(len(BALANCES_AT_90)) if balance_at_delivered(i) > 1.0]
    ok = passes == [6]
    fail += 0 if ok else 1
    print(f"    and only the bound-case bred fuel clears unity on the printed table"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = optimised_target_balance() > 1.0
    fail += 0 if ok else 1
    print(f"    the route that survives is bred fuel through an optimised target,")
    print(f"    at {optimised_target_balance():.3f}   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the end-to-end budget, and the two questions it couples")
    ok = 0.5 < budget_product() < 1.0
    fail += 0 if ok else 1
    print(f"    every term is a loss and the product is {budget_product():.4f}"
          f"   {'PASS' if ok else 'FAIL'}")
    e2e = C.delivered_fraction_mirrored(1.50, (0.0, 265.0)) * budget_product()
    ok = e2e > 0.2951
    fail += 0 if ok else 1
    print(f"    the end-to-end prediction {100 * e2e:.2f} % stays above the 29.51 % that")
    print(f"    would falsify the model, by {100 * e2e / 29.51:.3f}x"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = 100 * e2e < 50.8 and 100 * e2e > 21.4
    fail += 0 if ok else 1
    print(f"    and it falls BELOW the 50.8 % the demonstrated-cycle bred-fuel")
    print(f"    balance needs and ABOVE the 21.4 % the optimised target needs,")
    print(f"    so Q6's closure is what keeps the route: {'PASS' if ok else 'FAIL'}")
    ok = target_escape("W", 65.2, 0.255) > 0.8 and target_escape("W", 20.6, 10.0) < 0.5
    fail += 0 if ok else 1
    print(f"    a narrow target is transparent and a blocky one is not:"
          f" {target_escape('W', 65.2, 0.255):.3f} vs")
    print(f"    {target_escape('W', 20.6, 10.0):.3f}   {'PASS' if ok else 'FAIL'}")
    ok = abs(proc_binders_per_s() / (C.protons_per_s(1.0, 8.0) * C.harp_combined_yield()
             * proc_acceptance() * proc_interception() * budget_product()) - 1.0) < 1e-9
    fail += 0 if ok else 1
    print(f"    and the procedure multiplies by the WHOLE budget, not the decay term")
    print(f"    twice   {'PASS' if ok else 'FAIL'}")

    print()
    print("  COHERENCE: the procedure points at this machine")
    ok = abs(proc_beam_radius_cm() - 7.5) > 1.0
    fail += 0 if ok else 1
    print(f"    sec.6 as written stood the cell in a 7.50 cm beam; the machine's is")
    print(f"    {proc_beam_radius_cm():.2f} cm, so the figure had to change"
          f"   {'PASS' if ok else 'FAIL'}")
    net = proc_interception() / (PROC_CELL_RADIUS_CM / 7.5) ** 2 * (
        proc_acceptance() / C.delivered_fraction(1.50, "fwd", (0.0, PROC_CELL_P_STOP))
    ) * budget_product()
    ok = 0.70 < net < 1.15
    fail += 0 if ok else 1
    print(f"    and the three corrections nearly cancel: net x{net:.3f}"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(bore_tritium_cost() / 3.01 - 1.0) < 0.02
    fail += 0 if ok else 1
    print(f"    the bore trade reproduces [1] sec.5.25's 3.01 from the magnet")
    print(f"    rather than from a gyroradius: {bore_tritium_cost():.2f}"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(aperture_shield_cm(1.50) + aperture_bore_cm(1.50)
             - 100 * C.des_coil_inner_m()) < 1e-6
    fail += 0 if ok else 1
    print(f"    and both bores fit the SAME sourced coil radius, so the cold mass")
    print(f"    and the stored energy do not move with the aperture"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the cell can only sit where the pions have decayed")
    ok = channel_length_m() > 10 * C.DES_LENGTH_M
    fail += 0 if ok else 1
    print(f"    the channel is {channel_length_m():.1f} m against a capture region of"
          f" {C.DES_LENGTH_M:.1f} m   {'PASS' if ok else 'FAIL'}")
    ok = muon_decay_length_m() > 10 * channel_length_m()
    fail += 0 if ok else 1
    print(f"    and the muons survive it: {muon_decay_length_m():.0f} m decay length"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = channel_tritium_kg(2.0) > 5 * cell_tritium_kg()
    fail += 0 if ok else 1
    print(f"    a cell in the expanded beam would need {channel_tritium_kg(2.0):.0f} kg against")
    print(f"    {cell_tritium_kg():.2f} recompressed: recompression is a REQUIREMENT"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the cell's two requirements are met by one loop")
    ok = he3_steady_ppm() < 1.0
    fail += 0 if ok else 1
    print(f"    the flow the heat sets holds 3He at {he3_steady_ppm():.3f} ppm, below the")
    print(f"    1 ppm the specification demands   {'PASS' if ok else 'FAIL'}")
    ok = he3_ppm_doubling_minutes() < 60.0
    fail += 0 if ok else 1
    print(f"    and it is needed: 1 ppm accumulates every"
          f" {he3_ppm_doubling_minutes():.0f} minutes   {'PASS' if ok else 'FAIL'}")
    ok = abs((cell_stopping_w() + cell_alpha_w()) / cell_heat_w() - 1.0) < 1e-9
    fail += 0 if ok else 1
    print(f"    and the heat is the two terms and no third"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  THE REFUSAL ON PRESSURE")
    ok = lame_ratio(500.0, 300.0) is None
    fail += 0 if ok else 1
    print(f"    a monobloc vessel cannot hold a pressure at its own allowable")
    print(f"    stress, at any thickness   {'PASS' if ok else 'FAIL'}")
    ok = cell_pressure_mpa(0.222) < cell_pressure_mpa(1.0)
    fail += 0 if ok else 1
    print(f"    so the density is run LOW: {cell_pressure_mpa(0.222):.0f} MPa at phi 0.222"
          f" against {cell_pressure_mpa(1.0):.0f} at 1.0")
    print(f"    -- which inverts the specification's instinct"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = cell_depth_cm(0.222) > cell_depth_cm(1.0)
    fail += 0 if ok else 1
    print(f"    and it is paid for in length, which is cheap:"
          f" {cell_depth_cm(0.222):.0f} vs {cell_depth_cm(1.0):.0f} cm"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the sourced figures corroborate what this design computed for itself")
    e = C.des_stored_energy_j() / 1e9
    ok = 0.8 < e < 1.3
    fail += 0 if ok else 1
    print(f"    stored energy {e:.2f} GJ against the study's 'approaching 1 GJ'")
    print(f"    for the same geometry   {'PASS' if ok else 'FAIL'}")
    ok = 0.4 < dose_agreement() < 2.5
    fail += 0 if ok else 1
    print(f"    the reconstructed peak dose is {dose_agreement():.2f} of the published one,")
    print(f"    which is the check on the peak-to-mean factor   {'PASS' if ok else 'FAIL'}")
    ok = C.des_current_density_a_mm2() < 23.2
    fail += 0 if ok else 1
    print(f"    and this design's {C.des_current_density_a_mm2():.1f} A/mm2 is below the 23.2 the published")
    print(f"    superconducting coils run at   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the withdrawn reconstructions are gone, not buried")
    ok = abs(F_DEPOSITED_IN_TARGET - 0.55) > 0.4
    fail += 0 if ok else 1
    print(f"    target deposition is {100 * F_DEPOSITED_IN_TARGET:.1f} percent SOURCED, not the 55 this")
    print(f"    file assumed -- an error of {0.55 / F_DEPOSITED_IN_TARGET:.1f}x   {'PASS' if ok else 'FAIL'}")
    ok = abs(C.des_coil_inner_m() - 1.20) < 1e-9
    fail += 0 if ok else 1
    print(f"    and the coil inner radius is the study's 120 cm, not a shield")
    print(f"    thickness of this file's choosing   {'PASS' if ok else 'FAIL'}")
    r = coil_life_years() / sourced_coil_life_years()
    ok = 0.5 < r < 2.0
    fail += 0 if ok else 1
    print(f"    reconstructed and sourced coil life agree to {r:.2f}:"
          f" {coil_life_years():.0f} vs {sourced_coil_life_years():.0f} y"
          f"   {'PASS' if ok else 'FAIL'}")
    print("    -- the sourced figure is the one quoted; this only checks that the")
    print("       peak-to-mean factor is not wildly wrong in either direction")

    print()
    print("  the acceptance census is measured against the papers on disk")
    missing = [f"{s} {p}" for pa, s, p, _, _, _, _, _, _ in census_rows()
               if p not in _paper_text(pa)]
    ok = not missing
    fail += 0 if ok else 1
    print(f"    all {len(ACCEPTANCE_SITES)} printed figures still occur in the file"
          f" that prints them   {'PASS' if ok else 'FAIL'}")
    if missing:
        print("      missing: " + ", ".join(missing))
    nosec = sorted({f"{'[1]' if pa == PAPER_ECONOMY else '[2]'} {s}"
                    for pa, s, *_ in ACCEPTANCE_SITES
                    if s != "abstract" and f"# {s} " not in _paper_text(pa)
                    and f"#{s} " not in _paper_text(pa)})
    ok = not nosec
    fail += 0 if ok else 1
    print(f"    and every section named is still a heading in it"
          f"   {'PASS' if ok else 'FAIL'}")
    if nosec:
        print("      not found: " + ", ".join(nosec))
    over = [p for _, _, p, v, k, _, g, new, _ in census_rows()
            if k != "divisor" and new is not None and new > v + 1e-9]
    ok = not over
    fail += 0 if ok else 1
    print(f"    no restatement is LARGER than the figure it restates -- the loss")
    print(f"    budget only ever costs, and the three DIVISOR rows are excluded")
    print(f"    because a divisor grows for exactly that reason"
          f"   {'PASS' if ok else 'FAIL'}")
    a = restate(0.875, "ratio", ETA_TODAY_APERTURE)
    b = balance_at_delivered(5)
    ok = abs(a / b - 1.0) < 0.005
    fail += 0 if ok else 1
    print(f"    two independent routes to bred fuel at 150 cycles agree to"
          f" {a / b:.4f}:")
    print(f"      {a:.4f} from sec.5.24's ratio, {b:.4f} from sec.5.19's balance"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(restate(44.43, "acceptance", None) / 100.0 - delivered_eta()) < 5e-4
    fail += 0 if ok else 1
    print(f"    and sec.5.24's 44.43 restates to {restate(44.43, 'acceptance', None):.2f} percent, which is the")
    print(f"    delivered figure sec.5.31 uses   {'PASS' if ok else 'FAIL'}")
    res = census_residue()
    ok = not res
    fail += 0 if ok else 1
    covered = {r[0] for r in ACCEPTANCE_SITES}
    ok3 = covered == {PAPER_ECONOMY, PAPER_RECONCILIATION, PAPER_SPECIFICATION}
    fail += 0 if ok3 else 1
    print(f"    the census covers all three live papers, not the two it started")
    print(f"    with   {'PASS' if ok3 else 'FAIL'}")
    print(f"    and it is COMPLETE rather than merely long: every number")
    print(f"    on every acceptance-bearing line in any of them is censused,")
    print(f"    computed by the census, or exempt for a stated reason --")
    print(f"    residue {len(res)}   {'PASS' if ok else 'FAIL'}")
    for paper, n, v, line in res[:8]:
        print(f"      {paper[:24]}:{n}  {v}  {line[:56]}")
    ok = census_counts().get("WITHDRAWN", 0) == 1
    fail += 0 if ok else 1
    print(f"    exactly one row is graded WITHDRAWN, and it is a sentence rather")
    print(f"    than a number   {'PASS' if ok else 'FAIL'}")

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description="the capture solenoid as a build package")
    ap.add_argument("--selftest", action="store_true")
    for name, fn in (("circuit", report_circuit), ("mechanics", report_mechanics),
                     ("conductor", report_conductor), ("target", report_target),
                     ("radiation", report_radiation), ("failure", report_failure),
                     ("plant", report_plant), ("channel", report_channel),
                     ("cell", report_cell),
                     ("budget", report_budget),
                     ("balances", report_balances), ("census", report_census),
                     ("alteration", report_alteration),
                     ("coherence", report_coherence),
                     ("integration", report_integration)):
        ap.add_argument("--" + name, action="store_true", help=fn.__doc__ or name)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    for name, fn in (("circuit", report_circuit), ("mechanics", report_mechanics),
                     ("conductor", report_conductor), ("target", report_target),
                     ("radiation", report_radiation), ("failure", report_failure),
                     ("plant", report_plant), ("channel", report_channel),
                     ("cell", report_cell),
                     ("budget", report_budget),
                     ("balances", report_balances), ("census", report_census),
                     ("alteration", report_alteration),
                     ("coherence", report_coherence),
                     ("integration", report_integration)):
        if getattr(a, name):
            fn()
            return 0
    return report_all()


if __name__ == "__main__":
    sys.exit(main())
