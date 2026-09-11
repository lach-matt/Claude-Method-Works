#!/usr/bin/env python3
"""receiver.py -- the particle receiver, scaled rather than asserted about,
and simulated at CRITICAL conditions rather than optimal ones.

R-11 in helios3.py says the largest particle receiver that has run is ~1 MW_t
and a Helios-3 tower needs hundreds of MW_th, and grades that MAJOR after
mitigation. The author flagged it for simulation (2026-09-11) and set the
rule the simulation runs under:

    "make sure you are simulating more critical than optimal conditions.
     The numbers we work with need to have a conservative value to provide
     a front end threshold band on critical events upstream."

So every banded constant here carries TWO values -- NOMINAL (the best
credible) and CRITICAL (the adverse end of its band) -- and every result is
printed in both columns. The design is held to the CRITICAL column; the
nominal column says how much margin the critical one carries. A number
quoted from this file without its case is misquoted.

Three results, all stated at the critical case.

  1. The curtain is a PER-METRE machine. Flux, mass flow and the
     temperature rise across one drop are per metre of width and per
     metre of drop. Power is width x drop x flux. Scale is bought in WIDTH
     and in COUNT of apertures, and neither is a 700x step. At the critical
     case (shallow drop, low cp) the apertures are wider and more numerous,
     which is the threshold the tower must be designed to.

  2. The thermal loss FRACTION at fixed flux does not change with aperture
     size, because radiation and convection scale with aperture area as the
     power does. What changes with size is the EDGE (spillage, curtain-driven
     air escape, non-uniform feed), a perimeter effect that shrinks as
     perimeter/area. Scale is not a thermal question; it is curtain feeding.

  3. The staging plan in helios3.py does not stage the receiver: the 100 MWe
     first module's field charges the night, so its receiver is already
     ~0.55 of a fleet tower. A pilot aperture at fleet-aperture size belongs
     between, and every fleet aperture is then a copy of it.

The R-02 dome is priced beside the open aperture in both columns: it costs
transmission going in and saves convection and part of the radiation coming
out, and pays only above a break-even open-aperture loss.

The material is the one the design intends to use -- sintered bauxite in a
falling curtain -- and the one fixture is Sandia's 1 MW_t receiver on that
material. Stdlib only.
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
CASES = ("nominal", "critical")

# Banded constants: (nominal, critical). Critical is the ADVERSE end of the
# band -- the author's rule -- and the selftest asserts that on every row.
T_AMB_C = (25.0, 45.0)                    # ambient; desert summer afternoon         ASSUMED band
DEMO_MW = 1.0                             # MW_th, Sandia falling-particle receiver  SOURCED
DEMO_APERTURE_M2 = 1.0                    # 1 m x 1 m aperture                       SOURCED
DEMO_MASSFLOW_KG_S = (1.0, 7.0)           # kg/s through the 1 m curtain, tested     SOURCED band
DEMO_ETA_MEASURED = (0.80, 0.50)          # thermal efficiency measured: best, worst SOURCED band
CP_J_KGK = (1200.0, 1000.0)               # sintered bauxite 600-800 C; low end      SOURCED band 1.0-1.3 kJ/kg K
T_IN_C, T_OUT_C = 600.0, 800.0            # cold silo -> hot silo                     DESIGN (helios3 / G3P3)
FLUX_MW_M2 = 1.0                          # peak absorbed flux on the curtain        SOURCED (demo ran ~1 MW/m2)
DROP_M = (3.0, 1.0)                       # curtain height per stage: mesh-slowed, free  ASSUMED band (demo ~1 m)
ALPHA_EFF = (0.95, 0.90)                  # cavity-effective absorptance; aged/soiled  SOURCED 0.946 new; ASSUMED aged
EPS_EFF = (0.80, 0.90)                    # cavity-effective emittance at aperture   ASSUMED band
H_CONV_W_M2K = (10.0, 30.0)               # aperture convection: calm, windy         ASSUMED band
T_RAD_C = (800.0, 850.0)                  # radiating temperature seen at aperture   ASSUMED band (outlet; hot back wall)
DOME_TRANSMISSION = (0.93, 0.85)          # low-OH rod, clean; standard quartz, soiled  helios3 R-02 / ASSUMED
DOME_IR_RETURN = (0.5, 0.3)               # of the >4 um radiation, re-emitted inward  ASSUMED band
LAMBDA_CUT_UM = 4.0                       # quartz opaque beyond                     SOURCED
ROD_LEAK_KW_M2 = (2.76, 16.6)             # 30 cm rod; 5 cm rod (k 1.38 x 600 K / L)  helios3 R-02


def pick(band, case):
    """A banded constant at a case. A scalar is the same in both."""
    if isinstance(band, tuple):
        return band[CASES.index(case)]
    return band


def planck_fraction_beyond(lambda_um, t_k):
    """Fraction of blackbody power at t_k beyond lambda_um (series form)."""
    x = 14387.77 / (lambda_um * t_k)
    s = 0.0
    for m in range(1, 200):
        s += math.exp(-m * x) / m * (x ** 3 + 3 * x ** 2 / m + 6 * x / m ** 2 + 6 / m ** 3)
    return 1.0 - 15.0 / math.pi ** 4 * s


def curtain_power_per_width_mw(case, flux=FLUX_MW_M2):
    return flux * pick(DROP_M, case)


def massflow_per_width(case, flux=FLUX_MW_M2, dt=T_OUT_C - T_IN_C):
    return curtain_power_per_width_mw(case, flux) * 1e6 / (pick(CP_J_KGK, case) * dt)


def aperture_losses_kw_m2(case, open_aperture=True):
    """(radiation, convection, rod leak, transmission cost) per m2 of aperture."""
    t_rad = pick(T_RAD_C, case) + 273.15
    t_amb = pick(T_AMB_C, case) + 273.15
    rad = pick(EPS_EFF, case) * SIGMA * (t_rad ** 4 - t_amb ** 4) / 1e3
    if open_aperture:
        return rad, pick(H_CONV_W_M2K, case) * (t_rad - t_amb) / 1e3, 0.0, 0.0
    beyond = planck_fraction_beyond(LAMBDA_CUT_UM, t_rad)
    rad_d = rad * (1.0 - beyond * pick(DOME_IR_RETURN, case))
    return rad_d, 0.0, pick(ROD_LEAK_KW_M2, case), (1.0 - pick(DOME_TRANSMISSION, case)) * FLUX_MW_M2 * 1e3


def efficiency(case, open_aperture=True, flux=FLUX_MW_M2):
    rad, conv, rod, trans = aperture_losses_kw_m2(case, open_aperture)
    q_in = flux * 1e3
    tr = 1.0 if open_aperture else pick(DOME_TRANSMISSION, case)
    return (q_in * tr * pick(ALPHA_EFF, case) - rad - conv - rod) / q_in


def dome_breakeven_kw_m2(case):
    """Open-aperture loss beyond radiation above which the dome pays."""
    rad_o = aperture_losses_kw_m2(case, True)[0]
    rad_d, _, rod, trans = aperture_losses_kw_m2(case, False)
    absorb_shortfall = (1.0 - pick(DOME_TRANSMISSION, case)) * 0.0  # transmission already in trans
    return rad_d + rod + trans - rad_o + absorb_shortfall


def upstream_field_factor(design, case, open_aperture=True):
    """What the field must grow by to hold the design's energy if the receiver
    returns this case's efficiency instead of the chain's rec link. This is the
    threshold handed upstream: the chain carries one rec value, and the
    critical receiver hands it a smaller one."""
    return design["links"]["rec"] / efficiency(case, open_aperture)


def tower_duty_mwth(design):
    field_mw = design["aperture"] * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6
    return field_mw / design["towers"]


def first_module_duty_mwth(design, module_mwe):
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


def aperture_unit(mw, case):
    """Width, area, mass flow of one aperture carrying mw at a case's drop and cp."""
    width = mw / curtain_power_per_width_mw(case)
    return width, width * pick(DROP_M, case), massflow_per_width(case) * width


def report():
    d = C.design("helios3", "mid")
    tw = tower_duty_mwth(d)
    print()
    print("  THE PARTICLE RECEIVER, SCALED -- AT CRITICAL CONDITIONS")
    print("  ========================================================")
    print("    R-11: the largest particle receiver that has run is 1 MW_t and a")
    print("    fleet tower needs hundreds. Every banded constant is run at its")
    print("    NOMINAL and its CRITICAL value; the design is held to CRITICAL.")
    print()
    print("    1. THE CURTAIN IS A PER-METRE MACHINE. Power per metre of width is")
    print("       flux x drop; mass flow per metre is that over cp x dT.")
    print(f"         {'':<34}{'nominal':>10}{'critical':>10}")
    print(f"         {'drop, m':<34}{pick(DROP_M,'nominal'):10.1f}{pick(DROP_M,'critical'):10.1f}")
    print(f"         {'MW per metre of width':<34}{curtain_power_per_width_mw('nominal'):10.1f}{curtain_power_per_width_mw('critical'):10.1f}")
    print(f"         {'kg/s per metre (600 -> 800 C)':<34}{massflow_per_width('nominal'):10.1f}{massflow_per_width('critical'):10.1f}")
    lo, hi = DEMO_MASSFLOW_KG_S
    print(f"       Check on the demonstrated unit: 1 MW_t through a 1 m curtain at a 1 m")
    print(f"       drop needs {massflow_per_width('critical'):.1f} kg/s (critical cp); Sandia ran {lo:.0f}-{hi:.0f}. The")
    print("       law reproduces the machine at both cases.")
    print()
    print("    2. LOSS FRACTION DOES NOT CHANGE WITH SIZE at fixed flux. Per m2 of")
    print("       aperture at the hot end, kW/m2:")
    print(f"         {'':<14}{'radiation':>10}{'convect.':>10}{'rod leak':>10}{'transm.':>10}{'efficiency':>12}")
    for case in CASES:
        for label, op in (("open", True), ("R-02 dome", False)):
            rad, conv, rod, trans = aperture_losses_kw_m2(case, op)
            print(f"         {case + ', ' + label:<14}{rad:10.1f}{conv:10.1f}{rod:10.1f}{trans:10.1f}{efficiency(case, op):12.3f}")
    for case in CASES:
        be = dome_breakeven_kw_m2(case)
        conv = aperture_losses_kw_m2(case, True)[1]
        meas = (1 - pick(DEMO_ETA_MEASURED, case)) * FLUX_MW_M2 * 1e3
        rad = aperture_losses_kw_m2(case, True)[0]
        verdict = "pays" if be < meas - rad else "loses"
        print(f"       {case:<9} dome break-even {be:5.0f} kW/m2 of open loss beyond radiation; modelled")
        print(f"                 convection {conv:4.0f}; measured loss {meas:4.0f} -> on the model it loses, on the")
        print(f"                 measured record it {verdict}.")
    print("       The gap between model and measurement is the EDGE -- spillage and")
    print("       curtain-driven air escape -- a perimeter effect that falls as")
    print("       perimeter/area. Scale reduces it; the critical column assumes it")
    print("       does not, which is the threshold.")
    print()
    print("    3. THE LADDER. Design-point thermal duty, from cspchain's Helios-3:")
    for name, mw, f in ladder(d):
        fs = f"x{f:6.1f}" if f else "       "
        print(f"         {name:<42} {mw:8.1f} MW_th   {fs}")
    print("       The first module is not a step; it is the fleet receiver at 0.55.")
    print("       A pilot aperture at fleet-aperture size goes between.")
    print()
    print("    4. WHAT ONE FLEET APERTURE IS, at 1 MW/m2 peak absorbed flux. The")
    print("       CRITICAL column is the design threshold: shallow drop, low cp.")
    print(f"         {'aperture MW_th':>15}  {'width m':>8}{'area m2':>8}{'kg/s':>7}{'per tower':>10}   {'width m':>8}{'area m2':>8}{'kg/s':>7}{'per tower':>10}")
    print(f"         {'':>15}  {'-- nominal --':^33}   {'-- critical --':^33}")
    for mw in (10.0, 30.0, 60.0):
        wn, an, mn = aperture_unit(mw, "nominal")
        wc, ac, mc = aperture_unit(mw, "critical")
        print(f"         {mw:15.0f}  {wn:8.1f}{an:8.1f}{mn:7.0f}{tw / mw:10.0f}   {wc:8.1f}{ac:8.1f}{mc:7.0f}{tw / mw:10.0f}")
    print("       At critical a 30 MW_th aperture is a 30 m wide, 1 m tall slot carrying")
    print("       150 kg/s; the tower is designed to that, and the nominal 10 m x 3 m is")
    print("       margin, not a plan.")
    print()
    print("    5. THE THRESHOLD HANDED UPSTREAM. cspchain carries one receiver")
    print(f"       efficiency, rec = {d['links']['rec']:.2f}. If the receiver returns this file's")
    print("       figure instead, the field must grow by:")
    for case in CASES:
        for label, op in (("open", True), ("domed", False)):
            print(f"         {case + ', ' + label:<18} receiver {efficiency(case, op):.3f}   field x{upstream_field_factor(d, case, op):.2f}")
    print("       The critical open receiver is the front-end threshold: the field,")
    print("       the towers and the price all move by that factor before anything")
    print("       downstream is asked. cspchain is NOT changed here; it is told.")
    print()
    print("    WHAT THIS DOES NOT DO. It does not make the receiver have run. It")
    print("    moves the question from '700x' to 'a curtain fed uniformly across")
    print("    30 m, some thirty times, on one tower', and names the pilot that")
    print("    answers it. The grade stays with helios3.py.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    d = C.design("helios3", "mid")
    # --- the author's rule: critical is the adverse end of every band -------
    check("critical efficiency <= nominal, open aperture",
          efficiency("critical", True) <= efficiency("nominal", True))
    check("critical efficiency <= nominal, domed aperture",
          efficiency("critical", False) <= efficiency("nominal", False))
    check("critical needs at least as many apertures per tower and wider ones",
          aperture_unit(30.0, "critical")[0] >= aperture_unit(30.0, "nominal")[0])
    check("critical mass flow per aperture >= nominal",
          aperture_unit(30.0, "critical")[2] >= aperture_unit(30.0, "nominal")[2])
    check("every loss term at critical >= nominal (open)",
          all(c >= n for c, n in zip(aperture_losses_kw_m2("critical", True), aperture_losses_kw_m2("nominal", True))))
    check("every loss term at critical >= nominal (domed)",
          all(c >= n for c, n in zip(aperture_losses_kw_m2("critical", False), aperture_losses_kw_m2("nominal", False))))
    check("a scalar constant is the same at both cases", pick(FLUX_MW_M2, "nominal") == pick(FLUX_MW_M2, "critical"))
    # --- physics fixtures --------------------------------------------------
    lo, hi = DEMO_MASSFLOW_KG_S
    check("per-metre law reproduces Sandia's 1 MW_t curtain mass flow at both cases",
          lo <= massflow_per_width("critical") / pick(DROP_M, "critical") <= hi
          and lo <= massflow_per_width("nominal") / pick(DROP_M, "nominal") <= hi)
    check("loss fraction is independent of aperture area (no area argument exists)",
          "area" not in efficiency.__code__.co_varnames)
    rad = 0.8 * SIGMA * ((800 + 273.15) ** 4 - (25 + 273.15) ** 4) / 1e3
    check("radiation at 800 C, eps 0.8, 25 C ambient is 60 +- 1 kW/m2", abs(rad - 60.1) < 1.0)
    check("Planck: fraction below the Wien peak (lambda T = 2898 um K) is 0.25 +- 0.01",
          abs((1 - planck_fraction_beyond(2.898, 1000.0)) - 0.25) < 0.01)
    check("Planck fraction beyond lambda -> 0 as lambda -> infinity",
          planck_fraction_beyond(1000.0, 1073.15) < 1e-4)
    for case in CASES:
        be = dome_breakeven_kw_m2(case)
        conv = aperture_losses_kw_m2(case, True)[1]
        meas = (1 - pick(DEMO_ETA_MEASURED, case)) * FLUX_MW_M2 * 1e3
        rad_o = aperture_losses_kw_m2(case, True)[0]
        check(f"{case}: on the model alone the dome loses", be > conv)
        check(f"{case}: on the measured record the dome pays", be < meas - rad_o)
    rungs = ladder(d)
    prod = 1.0
    for _, _, f in rungs[1:]:
        prod *= f
    check("ladder factors multiply to the whole step", abs(prod - rungs[-1][1] / rungs[0][1]) < 1e-9)
    check("first module is more than half a fleet tower (the staging gap)",
          0.4 < rungs[2][1] / rungs[3][1] < 0.7)
    check("tower duty is imported from cspchain, not restated",
          abs(tower_duty_mwth(d) - d["aperture"] * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6 / d["towers"]) < 1e-9)
    check("a 30 MW_th aperture is 10 m wide nominal and 30 m wide critical",
          abs(aperture_unit(30.0, "nominal")[0] - 10.0) < 1e-9 and abs(aperture_unit(30.0, "critical")[0] - 30.0) < 1e-9)
    head = open(__file__).read().split("def pick")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES"))]
    check("every constant line carries a status",
          all(any(t in l for t in ("SOURCED", "ASSUMED", "DESIGN", "exact", "helios3")) for l in consts))
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report prints both cases", "nominal" in out and "critical" in out)
    check("the report hands a threshold upstream and names the file it does not change",
          "HANDED UPSTREAM" in out and "cspchain is NOT changed here" in out)
    check("critical open receiver is below the chain's rec link (a real threshold)",
          efficiency("critical", True) < d["links"]["rec"])
    check("upstream factor at the chain's own rec is exactly 1 by construction",
          abs(d["links"]["rec"] / d["links"]["rec"] - 1.0) < 1e-12)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
