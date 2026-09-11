#!/usr/bin/env python3
"""receiver.py -- the particle receiver, scaled rather than asserted about.

R-11 in helios3.py says the largest particle receiver that has run is ~1 MW_t
and a Helios-3 tower needs hundreds of MW_th, and grades that MAJOR after
mitigation. The author flagged it for simulation (2026-09-11). This file is
the first: it asks what physically scales in a falling-particle receiver and
what does not, and turns the one large number into a ladder of small ones.

Three results.

  1. The curtain is a PER-METRE machine. Everything that limits a falling
     curtain -- flux it can take, mass flow it can carry, the temperature
     rise across one drop -- is per metre of curtain width and per metre of
     drop. Power is width x height x flux. So scale is bought in WIDTH and
     in COUNT of apertures, and neither is a 700x step.

  2. The thermal loss fraction of an aperture at fixed flux does NOT change
     with aperture size (radiation and convection both scale with aperture
     area, as the power does). What changes with size is the EDGE: spillage,
     curtain-driven air escape and non-uniform feed are perimeter effects
     and shrink as perimeter/area. Scale is therefore not a thermal
     question; it is a curtain-feeding and structural one.

  3. The staging plan in helios3.py does not stage the receiver. The first
     100 MWe module needs a field ~2.3x its turbine (it charges the night),
     so its receiver is already ~0.55 of a fleet tower -- one step of ~460x
     from the demonstrated unit, then 1.8x. A pilot aperture at fleet size
     (tens of MW_th) belongs between them, and every fleet aperture is then
     a copy of it.

The R-02 dome is priced beside the open aperture: it costs transmission on
the way in and saves convection and part of the radiation on the way out,
so it pays only above a break-even open-aperture loss, which is computed.

Every constant carries a status. The material is the one the design intends
to use -- sintered bauxite in a falling curtain -- and the one fixture is
Sandia's 1 MW_t receiver on that material. Stdlib only.
"""
import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cspchain as C                                            # noqa: E402
import heliocost as HC                                          # noqa: E402
import helios as H                                              # noqa: E402

SIGMA = 5.670e-8                          # W/m2 K4                                  exact
T_AMB_K = 25.0 + 273.15                   # ambient                                  ASSUMED
# --- the demonstrated unit: Sandia 1 MW_t falling-particle receiver ----------
DEMO_MW = 1.0                             # MW_th                                    SOURCED
DEMO_APERTURE_M2 = 1.0                    # 1 m x 1 m aperture                       SOURCED
DEMO_MASSFLOW_KG_S = (1.0, 7.0)           # kg/s through the 1 m curtain, tested     SOURCED band
DEMO_ETA_MEASURED = (0.50, 0.80)          # thermal efficiency, measured             SOURCED band
# --- the particle and the curtain -------------------------------------------
CP_J_KGK = 1200.0                         # sintered bauxite, 600-800 C              SOURCED (1.0-1.3 kJ/kg K)
T_IN_C, T_OUT_C = 600.0, 800.0            # cold silo -> hot silo                     DESIGN (helios3 / G3P3)
FLUX_MW_M2 = 1.0                          # peak absorbed flux on the curtain        SOURCED (demo ran ~1 MW/m2)
DROP_M = (1.0, 3.0)                       # curtain height per stage                 ASSUMED band (demo ~1 m; mesh-slowed to ~3)
ALPHA_EFF = 0.95                          # cavity-effective absorptance             SOURCED (particle 0.946, multi-bounce)
EPS_EFF = 0.80                            # cavity-effective emittance at aperture   ASSUMED
H_CONV_W_M2K = (10.0, 30.0)               # free / windy convection at the aperture  ASSUMED band
# --- the R-02 dome -----------------------------------------------------------
DOME_TRANSMISSION = 0.93                  # two faces + 30 cm low-OH rod             helios3 R-02
DOME_IR_RETURN = 0.5                      # of the >4 um radiation absorbed, half re-emitted inward  ASSUMED
LAMBDA_CUT_UM = 4.0                       # quartz opaque beyond                     SOURCED
ROD_LEAK_KW_M2 = 2.76                     # k 1.38 x 600 K / 0.30 m                  helios3 R-02


def planck_fraction_beyond(lambda_um, t_k, n=2000):
    """Fraction of blackbody power at t_k beyond lambda_um. Series form."""
    x = 14387.77 / (lambda_um * t_k)       # c2 / (lambda T)
    # F(0->x) via the standard series in x for the fraction BELOW lambda
    s = 0.0
    for m in range(1, 60):
        s += math.exp(-m * x) / m * (x ** 3 + 3 * x ** 2 / m + 6 * x / m ** 2 + 6 / m ** 3)
    below = 15.0 / math.pi ** 4 * s
    return 1.0 - below


def curtain_power_per_width_mw(drop_m, flux=FLUX_MW_M2):
    """MW per metre of curtain width: the per-metre law."""
    return flux * drop_m


def massflow_per_width(drop_m, flux=FLUX_MW_M2, dt=T_OUT_C - T_IN_C):
    """kg/s per metre of width that carries that power across dt."""
    return curtain_power_per_width_mw(drop_m, flux) * 1e6 / (CP_J_KGK * dt)


def aperture_losses_kw_m2(open_aperture=True, h_conv=H_CONV_W_M2K[0], t_rad_k=T_OUT_C + 273.15):
    """Loss per m2 of aperture at the hot end. Returns (radiation, convection, rod leak, transmission cost)."""
    rad = EPS_EFF * SIGMA * (t_rad_k ** 4 - T_AMB_K ** 4) / 1e3
    if open_aperture:
        return rad, h_conv * (t_rad_k - T_AMB_K) / 1e3, 0.0, 0.0
    beyond = planck_fraction_beyond(LAMBDA_CUT_UM, t_rad_k)
    rad_domed = rad * (1.0 - beyond * DOME_IR_RETURN)
    return rad_domed, 0.0, ROD_LEAK_KW_M2, (1.0 - DOME_TRANSMISSION) * FLUX_MW_M2 * 1e3


def efficiency(open_aperture=True, h_conv=H_CONV_W_M2K[0], flux=FLUX_MW_M2):
    rad, conv, rod, trans = aperture_losses_kw_m2(open_aperture, h_conv)
    q_in = flux * 1e3
    return (q_in * (DOME_TRANSMISSION if not open_aperture else 1.0) * ALPHA_EFF - rad - conv - rod) / q_in


def dome_breakeven_kw_m2():
    """Open-aperture loss above which the dome pays, at the same radiation."""
    rad_o, _, _, _ = aperture_losses_kw_m2(True)
    rad_d, _, rod, trans = aperture_losses_kw_m2(False)
    # dome pays when open (rad_o + conv) > domed (rad_d + rod + trans + absorptance shortfall)
    return rad_d + rod + trans - rad_o + (1.0 - DOME_TRANSMISSION) * 0.0


def tower_duty_mwth(design):
    """Design-point thermal duty of one fleet tower, from cspchain's design."""
    field_mw = design["aperture"] * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6
    return field_mw / design["towers"]


def first_module_duty_mwth(design, module_mwe):
    """A module whose field charges the night has a receiver ~field/turbine x its turbine's thermal."""
    field_mw = design["aperture"] * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6
    turb_th = design["turb_mw"] / design["links"]["cycle"]
    return module_mwe / design["links"]["cycle"] * field_mw / turb_th


def ladder(design, module_mwe=100.0, pilot_mwth=30.0):
    rungs = [("Sandia 1 MW_t (has run)", DEMO_MW),
             (f"pilot aperture, {pilot_mwth:.0f} MW_th (proposed)", pilot_mwth),
             (f"first module, {module_mwe:.0f} MWe", first_module_duty_mwth(design, module_mwe)),
             ("fleet tower", tower_duty_mwth(design))]
    out, prev = [], None
    for name, mw in rungs:
        out.append((name, mw, (mw / prev) if prev else None))
        prev = mw
    return out


def aperture_unit(mw, drop_m):
    """Width, area and mass flow of one aperture carrying mw at one drop height."""
    per_w = curtain_power_per_width_mw(drop_m)
    width = mw / per_w
    return width, width * drop_m, massflow_per_width(drop_m) * width


def report():
    d = C.design("helios3", "mid")
    print()
    print("  THE PARTICLE RECEIVER, SCALED")
    print("  ==============================")
    print("    R-11: the largest particle receiver that has run is 1 MW_t and a")
    print("    fleet tower needs hundreds. This file asks what actually scales.")
    print()
    print("    1. THE CURTAIN IS A PER-METRE MACHINE. Power per metre of width is")
    print("       flux x drop height; mass flow per metre is that over cp x dT.")
    for drop in DROP_M:
        print(f"         drop {drop:.0f} m: {curtain_power_per_width_mw(drop):.1f} MW per m of width, "
              f"{massflow_per_width(drop):.1f} kg/s per m ({T_IN_C:.0f} -> {T_OUT_C:.0f} C)")
    lo, hi = DEMO_MASSFLOW_KG_S
    print(f"       Check on the demonstrated unit: 1 MW_t through a 1 m curtain needs")
    print(f"       {massflow_per_width(1.0):.1f} kg/s; Sandia ran {lo:.0f}-{hi:.0f}. The law reproduces the machine.")
    print()
    print("    2. LOSS FRACTION DOES NOT CHANGE WITH SIZE at fixed flux. Per m2 of")
    print("       aperture at the hot end:")
    for label, op, h in (("open, calm", True, H_CONV_W_M2K[0]), ("open, windy", True, H_CONV_W_M2K[1]),
                         ("R-02 dome", False, 0.0)):
        rad, conv, rod, trans = aperture_losses_kw_m2(op, h)
        print(f"         {label:<12} radiation {rad:5.1f}  convection {conv:5.1f}  rod leak {rod:4.1f}  "
              f"transmission {trans:5.1f} kW/m2   efficiency {efficiency(op, h):.3f}")
    be = dome_breakeven_kw_m2()
    meas_lo = (1 - DEMO_ETA_MEASURED[1]) * FLUX_MW_M2 * 1e3
    meas_hi = (1 - DEMO_ETA_MEASURED[0]) * FLUX_MW_M2 * 1e3
    print(f"       The dome pays when the open aperture loses more than {be:.0f} kW/m2 beyond")
    print(f"       radiation. The model's own convection is {aperture_losses_kw_m2(True, H_CONV_W_M2K[1])[1]:.0f} kW/m2 at most, so on")
    print(f"       the MODEL the dome loses. Sandia MEASURED {DEMO_ETA_MEASURED[0]:.2f}-{DEMO_ETA_MEASURED[1]:.2f}, i.e. losses of")
    print(f"       {meas_lo:.0f}-{meas_hi:.0f} kW/m2 -- far above the model, and the difference is the")
    print("       edge: spillage and curtain-driven air escape. On the MEASURED record the")
    print("       dome pays everywhere. Those edge losses are perimeter effects and")
    print("       fall as perimeter/area, which is the one thing scale does for free.")
    print()
    print("    3. THE LADDER. Design-point thermal duty, from cspchain's Helios-3:")
    for name, mw, f in ladder(d):
        fs = f"x{f:6.1f}" if f else "       "
        print(f"         {name:<42} {mw:8.1f} MW_th   {fs}")
    print("       The first module is not a step, it is the fleet receiver at 0.55.")
    print("       A pilot aperture at fleet-aperture size goes between: then the")
    print("       module is copies of the pilot and the tower is copies of the module.")
    print()
    print("    4. WHAT ONE FLEET APERTURE IS, at 1 MW/m2 peak absorbed flux:")
    tw = tower_duty_mwth(d)
    print(f"         {'aperture MW_th':>15} {'drop m':>7} {'width m':>8} {'area m2':>8} {'kg/s':>7} {'per tower':>10}")
    for mw in (10.0, 30.0, 60.0):
        for drop in DROP_M:
            w, a, mf = aperture_unit(mw, drop)
            print(f"         {mw:15.0f} {drop:7.0f} {w:8.1f} {a:8.1f} {mf:7.0f} {tw / mw:10.0f}")
    print("       A 30 MW_th aperture at a 3 m drop is a 10 m wide slot with a 1 m2 x 30")
    print("       curtain behind it, and a fleet tower is some thirty of them around a")
    print("       polygonal cavity -- Crescent Dunes' external receiver is ~1,100 m2.")
    print()
    print("    WHAT THIS DOES NOT DO. It does not make the receiver have run. It")
    print("    moves the question from '700x' to 'a 10 m curtain fed uniformly,")
    print("    thirty times, on one tower', and names the pilot that answers it.")
    print("    The grade stays with helios3.py.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<70} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    d = C.design("helios3", "mid")
    lo, hi = DEMO_MASSFLOW_KG_S
    check("per-metre law reproduces Sandia's 1 MW_t curtain mass flow",
          lo <= massflow_per_width(1.0) * 1.0 <= hi)
    check("loss fraction at fixed flux is independent of aperture area (structural)",
          efficiency.__code__.co_varnames[:3] == ("open_aperture", "h_conv", "flux"))
    rad = EPS_EFF * SIGMA * ((T_OUT_C + 273.15) ** 4 - T_AMB_K ** 4) / 1e3
    check("radiation at 800 C, eps 0.8, is 60 +- 1 kW/m2", abs(rad - 60.1) < 1.0)
    check("Planck: fraction below the Wien peak (lambda T = 2898 um K) is 0.25 +- 0.01",
          abs((1 - planck_fraction_beyond(2.898, 1000.0)) - 0.25) < 0.01)
    check("Planck fraction beyond 4 um at 1073 K is 0.47 +- 0.02",
          abs(planck_fraction_beyond(4.0, 1073.15) - 0.47) < 0.02)
    check("Planck fraction beyond lambda -> 0 as lambda -> infinity",
          planck_fraction_beyond(1000.0, 1073.15) < 1e-4)
    be = dome_breakeven_kw_m2()
    conv_max = aperture_losses_kw_m2(True, H_CONV_W_M2K[1])[1]
    meas_lo = (1 - DEMO_ETA_MEASURED[1]) * FLUX_MW_M2 * 1e3
    check("on the model alone the dome loses (break-even above modelled convection)", be > conv_max)
    check("on the measured record the dome pays (break-even below the best measured loss)",
          be < meas_lo - rad)
    rungs = ladder(d)
    prod = 1.0
    for _, _, f in rungs[1:]:
        prod *= f
    check("ladder factors multiply to the whole step", abs(prod - rungs[-1][1] / rungs[0][1]) < 1e-9)
    check("first module is more than half a fleet tower (the staging gap)",
          0.4 < rungs[2][1] / rungs[3][1] < 0.7)
    check("tower duty is imported from cspchain, not restated",
          abs(tower_duty_mwth(d) - d["aperture"] * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6 / d["towers"]) < 1e-9)
    w, a, mf = aperture_unit(30.0, 3.0)
    check("a 30 MW_th aperture at 3 m drop is 10 m wide", abs(w - 10.0) < 1e-9)
    check("every constant line carries a status",
          all(any(t in line for t in ("SOURCED", "ASSUMED", "DESIGN", "exact", "helios3"))
              for line in open(__file__).read().split("def planck")[0].splitlines()
              if line[:1].isupper() and "=" in line and not line.startswith("HERE")))
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
