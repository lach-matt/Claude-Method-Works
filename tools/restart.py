#!/usr/bin/env python3
"""restart.py -- criterion 8: restartable quickly after a shutdown.

WHY THIS FILE EXISTS
--------------------
OBJECTIVE.md sets nine criteria. Eight of them were adjudicated somewhere in
tools/ before this file existed; this one was adjudicated by nothing at all. A
grep over the whole instrument set found no decay heat, no trip recovery, no
afterheat and no restart anywhere. A criterion nothing computes is a criterion
the paper cannot state, so this computes it.

WHAT "RESTART" MEANS HERE, AND WHY THE USUAL ANSWER DOES NOT APPLY
------------------------------------------------------------------
In a thermal critical reactor the restart clock is set by XENON. Xe-135 is a
fission product with an enormous thermal absorption cross section; it builds up
after shutdown from iodine decay and then burns out, and for roughly a day the
reactor cannot be restarted at all whatever the operator wants. That is the
"xenon dead time", and it is the reason a large PWR is not a fast-restart
machine.

Two independent features of this plant delete that constraint:

  1. THE SPECTRUM IS FAST. Xe-135's absorption cross section is about 2.6e6
     barns at thermal energies and a few barns above 100 keV -- six orders of
     magnitude down. A fast core does not see xenon.
  2. THE ASSEMBLY IS SUBCRITICAL AND SOURCE-DRIVEN. k = 0.95, so the power is
     whatever the beam makes it. There is no criticality to re-establish and no
     reactivity balance to win: the beam goes on and the power follows it
     within a prompt-neutron lifetime.

So the neutronic restart is immediate, and this file's real question is the
THERMAL one, which is where the constraint actually lives.

THE CONSTRAINT THAT IS REAL
---------------------------
The fuel is a liquid salt. It must not freeze, and it must not overheat. After
a trip the fissions stop with the beam, but the fission PRODUCTS do not, and
decay heat is large: this file computes the adiabatic rise and it is hundreds
of kelvin in the first hour. So the plant cannot simply be walked away from --
decay heat removal is mandatory, and that is a FINDING rather than a design
choice.

That gives the two restart modes the design must choose between, and they
differ by orders of magnitude:

  HELD MOLTEN -- decay heat removed actively, salt kept above liquidus.
                 Restart is beam-on. Minutes.
  DRAINED     -- the freeze-plug drain tank, which is the passive-safety
                 answer and the MSRE's own. Restart requires re-melting the
                 whole inventory. Hours to days.

Both are computed below. The design cannot have both, and this file does not
choose -- it prices the choice.

    python3 tools/restart.py            the full report
    python3 tools/restart.py --selftest
stdlib only.
"""
import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def _mat():
    import materials as M
    return M


# ---- decay heat -------------------------------------------------------------
# Wigner-Way / ANS-5.1 in its classical closed form. P(t)/P0 for a reactor run
# at P0 for T0 seconds and shut down at t = 0:
#
#     P(t)/P0 = A [ t^-a  -  (t + T0)^-a ]
#
# The constants are the standard ones and are SOURCED, not fitted here. They are
# derived for U-235 thermal fission; a fast Pu-239 core differs by of order ten
# percent in the first hours, which is inside every other band in this file and
# is stated rather than corrected for.
DECAY_A = 0.066              # SOURCED, Wigner-Way coefficient
DECAY_EXP = 0.20             # SOURCED, Wigner-Way exponent
FULL_POWER_S = 40.0 * 365.25 * 24 * 3600.0   # the plant's whole life at power

# ---- the salt, and the temperature it must stay between ---------------------
# The liquidus is the number that decides everything below. NaCl-UCl3 near the
# eutectic is quoted in the 500-550 C band; it is carried as a BAND because the
# exact composition is not fixed in this design.
LIQUIDUS_C_LO = 500.0        # SOURCED band, NaCl-UCl3 near the eutectic
LIQUIDUS_C_HI = 550.0        # SOURCED band
SALT_LATENT_J_KG = 3.0e5     # J/kg, heat of fusion, chloride salt  SOURCED band
BOIL_MARGIN_C = 1400.0       # ASSUMED: chloride salts boil far above operation

# What the loop runs at, imported and never restated -- materials.py owns it.
LOOP_COLD_K = 700.0          # materials.SALT_DT_K is the 700 -> 900 K rise
LOOP_HOT_K = 900.0

TRACE_HEAT_MW = 10.0         # ASSUMED: installed trace heating for a re-melt


def decay_fraction(t_s, t0_s=FULL_POWER_S):
    """Decay heat as a fraction of the power the plant was running at."""
    if t_s <= 0:
        return DECAY_A * (1e-3 ** -DECAY_EXP - (1e-3 + t0_s) ** -DECAY_EXP)
    return DECAY_A * (t_s ** -DECAY_EXP - (t_s + t0_s) ** -DECAY_EXP)


def decay_heat_mw(t_s, thermal_mw=None):
    if thermal_mw is None:
        thermal_mw = _mat().ref()["thermal_mw"]
    return decay_fraction(t_s) * thermal_mw


def decay_energy_j(t_s, thermal_mw=None):
    """Energy released by decay heat from shutdown to t, integrated exactly.

    The integral of A t^-a is A t^(1-a)/(1-a); the (t+T0) term contributes
    negligibly over the hours this file cares about and is carried anyway.
    """
    if thermal_mw is None:
        thermal_mw = _mat().ref()["thermal_mw"]
    p0 = thermal_mw * 1e6
    b = 1.0 - DECAY_EXP
    t0 = FULL_POWER_S
    return DECAY_A * p0 / b * (t_s ** b - ((t_s + t0) ** b - t0 ** b))


def adiabatic_rise_k(t_s):
    """Salt temperature rise if decay heat is removed by NOTHING.

    This is the number that makes decay-heat removal mandatory rather than
    optional, so it is computed rather than asserted.
    """
    M = _mat()
    m = M.salt_inventory_kg()
    return decay_energy_j(t_s) / (m * M.SALT_CP)


def time_to_boil_s(margin_c=None):
    """How long adiabatic heating has before the salt is in trouble."""
    if margin_c is None:
        margin_c = BOIL_MARGIN_C - (LOOP_HOT_K - 273.15)
    lo, hi = 1.0, 1.0e7
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if adiabatic_rise_k(mid) < margin_c:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---- the freeze question, which turns out to run the other way --------------
def freeze_margin_k():
    """Loop cold leg against the liquidus band. NEGATIVE means it freezes.

    This is a check on the design rather than on the restart, and it is here
    because restart is the first question that forces the comparison.
    """
    cold_c = LOOP_COLD_K - 273.15
    return cold_c - LIQUIDUS_C_HI, cold_c - LIQUIDUS_C_LO


def remelt_energy_j():
    """Sensible plus latent heat to bring a frozen inventory back to hot."""
    M = _mat()
    m = M.salt_inventory_kg()
    dt = LOOP_HOT_K - (LIQUIDUS_C_LO + 273.15)
    return m * (M.SALT_CP * dt + SALT_LATENT_J_KG)


def remelt_hours(trace_mw=TRACE_HEAT_MW):
    return remelt_energy_j() / (trace_mw * 1e6) / 3600.0


# ---- xenon, and why it is not the clock here --------------------------------
XE_SIGMA_THERMAL_B = 2.6e6   # SOURCED, Xe-135 absorption at 0.025 eV
XE_SIGMA_FAST_B = 5.0        # SOURCED band, above ~100 keV


def xenon_suppression():
    """How much weaker xenon is in this spectrum than in a thermal one."""
    return XE_SIGMA_THERMAL_B / XE_SIGMA_FAST_B


def report():
    M = _mat()
    r = M.ref()
    th = r["thermal_mw"]
    print()
    print("  CRITERION 8 -- RESTARTABLE QUICKLY AFTER A SHUTDOWN")
    print()
    print("    Nothing in this repository computed this before. The criterion")
    print("    is adjudicated here and the verdict is split, because the")
    print("    neutronics and the thermals give different answers.")
    print()
    print("  1. THE NEUTRONIC RESTART IS IMMEDIATE, AND TWO INDEPENDENT")
    print("     FEATURES MAKE IT SO.")
    print(f"     Xe-135 absorbs at {XE_SIGMA_THERMAL_B:.1e} barns thermal and")
    print(f"     about {XE_SIGMA_FAST_B:.0f} barns fast -- a factor of"
          f" {xenon_suppression():.0e} down.")
    print("     A fast core does not see xenon, so the xenon dead time that")
    print("     stops a thermal reactor restarting for a day does not exist.")
    print("     And the assembly is SUBCRITICAL: there is no criticality to")
    print("     re-establish. The beam goes on and the power follows it.")
    print("     THE CLOCK IS NOT NEUTRONIC.")
    print()
    print("  2. THE CLOCK IS THERMAL, AND DECAY HEAT IS WHY.")
    print(f"     The station runs at {th:,.0f} MW thermal. After a trip:")
    print()
    print("       time        decay heat    energy since trip   rise if unremoved")
    tb = time_to_boil_s()
    for label, t in (("1 s", 1.0), ("1 min", 60.0), ("1 hour", 3600.0),
                     ("1 day", 86400.0), ("1 week", 604800.0)):
        rise = adiabatic_rise_k(t)
        mark = "" if t < tb else "   (already boiled)"
        print(f"       {label:<10} {decay_heat_mw(t):8.1f} MW"
              f"     {decay_energy_j(t)/1e9:11.0f} GJ"
              f"   {rise:8.0f} K{mark}")
    print()
    print(f"     The salt inventory is {M.salt_inventory_kg()/1000:.0f} t at"
          f" {M.SALT_CP:.0f} J/kg/K. The last column is a")
    print("     COUNTERFACTUAL and stops being physical early -- the salt")
    print(f"     would reach boiling about {tb/3600.0:.1f} hours after the trip,")
    print("     so the rises quoted past that point are what the heat would")
    print("     do if it could, not what the salt would do.")
    print(f"     The first hour alone is {adiabatic_rise_k(3600.0):.0f} K."
          " DECAY HEAT REMOVAL IS")
    print("     MANDATORY. That is a finding, not a design option: the plant")
    print("     cannot be walked away from after a trip.")
    print()
    print("  3. SO THE RESTART TIME IS A DESIGN CHOICE BETWEEN TWO MODES,")
    print("     AND THEY DIFFER BY THREE ORDERS OF MAGNITUDE.")
    print()
    print("       HELD MOLTEN -- decay heat removed actively, salt above")
    print("         liquidus throughout. Restart is beam-on plus the")
    print("         protection-system reset. MINUTES.")
    print(f"       DRAINED -- the freeze-plug drain tank, which is the")
    print("         passive-safety answer and the one the MSRE actually")
    print("         used. Restart requires re-melting the inventory:")
    print(f"         {remelt_energy_j()/3.6e9:.1f} MWh, or"
          f" {remelt_hours():.1f} hours at {TRACE_HEAT_MW:.0f} MW of trace heat.")
    print()
    print("     The design cannot have both and this file does not choose.")
    print("     What it says is that FAST RESTART AND PASSIVE SHUTDOWN ARE IN")
    print("     TENSION HERE, which nothing in the build package had stated.")
    print()
    print("  4. AND A CHECK THIS QUESTION FORCED, WHICH FAILS.")
    hi, lo = freeze_margin_k()
    print(f"     materials.py runs the loop {LOOP_COLD_K:.0f} ->"
          f" {LOOP_HOT_K:.0f} K, a cold leg of"
          f" {LOOP_COLD_K-273.15:.0f} C.")
    print(f"     The NaCl-UCl3 liquidus band is"
          f" {LIQUIDUS_C_LO:.0f}-{LIQUIDUS_C_HI:.0f} C. The cold leg is")
    print(f"     therefore {abs(hi):.0f} to {abs(lo):.0f} C BELOW the"
          " liquidus, and the fuel")
    print("     salt freezes in the cold leg in normal operation.")
    print("     RECORDED, NOT REPAIRED. It is a fault in the loop")
    print("     temperatures rather than in the restart argument, it is")
    print("     materials.py's to fix, and the fix is to raise the loop --")
    print("     which costs nothing this file can see, since the Carnot")
    print("     figure the plant is priced at assumes the HOT leg.")
    print()


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print(f"  {label:<62} {'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"      got {got!r} want {want!r}")

    print()
    print("  decay heat behaves as decay heat")
    check("it falls monotonically after shutdown",
          all(decay_heat_mw(t) > decay_heat_mw(t * 10)
              for t in (1.0, 60.0, 3600.0, 86400.0)))
    check("one second after trip it is a few percent of full power",
          0.02 < decay_fraction(1.0) < 0.10)
    check("at one hour it is around one percent",
          0.005 < decay_fraction(3600.0) < 0.02)
    # a long-irradiated core sits near 0.3-0.4 % a week after shutdown; the
    # first threshold written here was 0.3 %, which this returns 0.36 % against
    # -- the assertion was wrong and the physics was right.
    check("at one week it is a few tenths of a percent",
          0.002 < decay_fraction(604800.0) < 0.005)
    # the integral must be consistent with the instantaneous rate: energy over
    # a short window near t must be close to P(t) . dt.
    t, dt = 3600.0, 1.0
    approx = decay_heat_mw(t) * 1e6 * dt
    exact = decay_energy_j(t + dt) - decay_energy_j(t)
    check("the energy integral agrees with the rate it integrates",
          abs(exact - approx) / approx < 0.01)

    print()
    print("  the finding that makes removal mandatory")
    check("the first hour is a large adiabatic rise, not a small one",
          adiabatic_rise_k(3600.0) > 100.0)
    check("  -- and it is larger still at a day",
          adiabatic_rise_k(86400.0) > adiabatic_rise_k(3600.0))
    check("so the salt would be in trouble within hours unattended",
          time_to_boil_s() < 86400.0)

    print()
    print("  the two restart modes, and the gap between them")
    check("re-melting takes hours, not minutes", remelt_hours() > 1.0)
    check("  -- so the drained mode is orders slower than beam-on",
          remelt_hours() * 60.0 > 100.0)
    check("re-melt energy counts latent heat and not only sensible",
          remelt_energy_j() > _mat().salt_inventory_kg() * SALT_LATENT_J_KG)

    print()
    print("  xenon is not the clock, and the selftest proves the direction")
    check("the fast cross section is orders below the thermal one",
          xenon_suppression() > 1e4)

    print()
    print("  the check this question forced, which must keep failing until")
    print("  materials.py raises the loop")
    hi, lo = freeze_margin_k()
    check("the cold leg is BELOW the liquidus band, both ends", hi < 0 and lo < 0)
    check("  -- and the report says so rather than passing silently",
          "freezes in the cold leg" in _rendered())

    print()
    print(f"selftest: {fail} failures -> {'PASS' if not fail else 'FAIL'}")
    return 1 if fail else 0


def _rendered():
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
