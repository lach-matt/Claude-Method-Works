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
import math
import os
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


def report_all():
    print("THE CAPTURE SOLENOID: BUILD PACKAGE")
    print()
    print("  collector.py --magnet designs the field and names three things it does")
    print("  not do. This finishes them, and adds what the magnet alone does not")
    print("  make a machine: the target, the lifetime, the plant, the integration.")
    print()
    for r in (report_circuit, report_mechanics, report_conductor, report_target,
              report_radiation, report_failure, report_plant, report_integration):
        r()
        print()
    print("  WHAT REMAINS UNDONE, AND IT IS ONE THING.")
    print("    The D-T cell's mechanical and thermal design beside a liquid-metal")
    print("    target in a 14 T field. Everything else above is either computed")
    print("    from a conserved quantity or referred to a machine that has been")
    print("    built and run.")
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
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description="the capture solenoid as a build package")
    ap.add_argument("--selftest", action="store_true")
    for name, fn in (("circuit", report_circuit), ("mechanics", report_mechanics),
                     ("conductor", report_conductor), ("target", report_target),
                     ("radiation", report_radiation), ("failure", report_failure),
                     ("plant", report_plant), ("integration", report_integration)):
        ap.add_argument("--" + name, action="store_true", help=fn.__doc__ or name)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    for name, fn in (("circuit", report_circuit), ("mechanics", report_mechanics),
                     ("conductor", report_conductor), ("target", report_target),
                     ("radiation", report_radiation), ("failure", report_failure),
                     ("plant", report_plant), ("integration", report_integration)):
        if getattr(a, name):
            fn()
            return 0
    return report_all()


if __name__ == "__main__":
    sys.exit(main())
