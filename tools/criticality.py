#!/usr/bin/env python3
"""criticality.py -- can handling or storing this fuel ever cause an accident?

WHY THIS FILE EXISTS
--------------------
The question put to it was direct: make sure the handling and storage of the
uranium is never a safety question, and that no catastrophe of any kind is
possible. That is not a question a reassurance answers. It is a criticality
safety question, criticality safety is a mature discipline with its own
arithmetic, and nothing in this repository had done any of it.

THE FIRST ANSWER IS THAT THE URANIUM IS NOT THE HAZARD
------------------------------------------------------
Depleted uranium is an alpha emitter with a 4.5-billion-year half-life. Its
specific activity is computed below and it is small; handled dry and unpowdered
it is a HEAVY-METAL TOXICITY problem of roughly lead's character and not a
radiological one, and no quantity of it in any geometry can sustain a chain
reaction, because U-238 is fertile. THE FERTILE FEED IS NOT THE SAFETY
QUESTION, and if this file had only been asked about uranium it would end here.

THE REAL QUESTION IS THE FISSILE, AND IT HAS TWO HALVES
--------------------------------------------------------
  GEOMETRY   an accumulation large enough in the right shape goes critical.
             This is computable, it is computed below, and the answer is
             comfortable: the salt is dilute, so critical dimensions are
             METRES rather than centimetres, and favourable-geometry storage
             is easy rather than delicate.

  MODERATION  and this is the one that kills people. A FAST assembly that is
             safely subcritical dry can become critical WET, because water
             slows neutrons into the energy range where fission cross sections
             are hundreds of times larger. Every serious criticality accident
             in the industry's history involved moderation, solution, or both.

ON THE SECOND HALF THIS FILE REFUSES TO COMPUTE AND SAYS SO. Moderation is a
SPECTRUM effect and the model available here is one-group -- it has no spectrum
by construction, so it cannot represent the excursion it would need to bound.
Reporting a moderated k from a one-group model would be worse than reporting
nothing, because it would look like an answer. What this file does instead is
state the requirement that follows, which is absolute and which does not need a
calculation to justify.

    python3 tools/criticality.py
    python3 tools/criticality.py --selftest
stdlib only.
"""
import argparse
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def _fc():
    import fuelchoice as F
    return F


def _mat():
    import materials as M
    return M


def _ps():
    import powersource as P
    return P


# ---- how radioactive the fertile feed actually is ---------------------------
AVOGADRO = 6.02214076e23        # exact by definition
U238_HALFLIFE_Y = 4.468e9       # SOURCED
SECONDS_PER_YEAR = 365.25 * 24 * 3600.0
A_U238 = 238.05                 # SOURCED


def specific_activity_bq_per_kg(mass_number=A_U238, halflife_y=U238_HALFLIFE_Y):
    """Activity of one kilogram of a pure nuclide. A = lambda.N, exactly."""
    n = 1000.0 / mass_number * AVOGADRO
    lam = math.log(2.0) / (halflife_y * SECONDS_PER_YEAR)
    return lam * n


# ---- criticality geometry ---------------------------------------------------
# One-group diffusion, which IS the right tool for a geometric question and is
# NOT the right tool for a moderation question. The non-leakage probability of
# a bare assembly is 1/(1 + M^2 B^2), so k_eff = k_inf / (1 + M^2 B^2), and the
# assembly is critical when B^2 reaches (k_inf - 1)/M^2.
#
# M^2 is the migration area. For a fast chloride salt it is large -- neutrons
# travel far before they are absorbed -- and it is carried as a SOURCED band
# because it is the one input here that a transport code would refine.
MIGRATION_AREA_CM2_LO = 150.0   # SOURCED band, fast chloride salt
MIGRATION_AREA_CM2_HI = 300.0   # SOURCED band

# Geometric buckling by shape. Standard closed forms, exact.
#   sphere            B^2 = (pi/R)^2
#   infinite cylinder B^2 = (2.405/R)^2
#   infinite slab     B^2 = (pi/a)^2      a = thickness
SHAPES = {
    "sphere": ("radius", math.pi),
    "infinite cylinder": ("radius", 2.4048),
    "infinite slab": ("thickness", math.pi),
}

SAFETY_FACTOR = 2.0             # ASSUMED: storage dimensions halved against
                                # the critical one. Criticality safety practice
                                # is stricter than this and this is a floor.


def critical_buckling(k_inf, m2):
    """B^2 at which an assembly of this k_inf is critical. Negative means it
    cannot be made critical at any size."""
    return (k_inf - 1.0) / m2


def critical_dimension_cm(k_inf, shape, m2):
    """The dimension at which this shape goes critical. None if it cannot."""
    if shape not in SHAPES:
        raise ValueError(f"unknown shape {shape!r}; have {sorted(SHAPES)}")
    b2 = critical_buckling(k_inf, m2)
    if b2 <= 0.0:
        return None
    _, const = SHAPES[shape]
    return const / math.sqrt(b2)


def k_inf_of_fuel(f=None):
    """k_inf of the fuel salt at fissile fraction f, from fuelchoice's model."""
    F, P = _fc(), _ps()
    if f is None:
        f = F.fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    return F.k_infinity(f, "Pu239", "U238")


def always_subcritical_threshold(leak_unused=None):
    """The fissile fraction below which NO geometry of this salt is critical.

    k_inf < 1 means the multiplication cannot sustain itself however much is
    assembled -- an infinite block is subcritical. Below this fraction, an
    accumulation of fuel salt is not a criticality question AT ALL, dry, and
    the whole hazard class disappears rather than being managed.
    """
    lo, hi = 0.0, 1.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if k_inf_of_fuel(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def k_inf_of_fertile_only():
    """k_inf of the fertile feed alone. It is the number that makes the
    uranium a non-question, so it is computed and not asserted."""
    return _fc().k_infinity(0.0, "Pu239", "U238")


def report():
    F, M, P = _fc(), _mat(), _ps()
    f_op = F.fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    k_fuel = k_inf_of_fuel()
    k_fert = k_inf_of_fertile_only()
    print()
    print("  CAN HANDLING OR STORING THIS FUEL CAUSE AN ACCIDENT?")
    print()
    print("  1. THE URANIUM IS NOT THE HAZARD, AND THE ARITHMETIC IS SHORT")
    print()
    sa = specific_activity_bq_per_kg()
    print(f"     Depleted uranium is U-238: half-life"
          f" {U238_HALFLIFE_Y:.3e} years, specific")
    print(f"     activity {sa/1e6:.1f} MBq/kg, an alpha emitter. For scale a"
          " domestic smoke")
    print("     detector holds about 0.037 MBq and a human body about 0.004.")
    print("     A kilogram of DU is more active than either and it is an ALPHA")
    print("     emitter, so the hazard is INTERNAL -- inhalation of oxide dust")
    print("     -- and its character is heavy-metal toxicity of roughly lead's")
    print("     kind. Handled as a solid it is a chemical control problem.")
    print()
    print(f"     And it cannot go critical at any size in any shape:"
          f" k_inf = {k_fert:.4f}")
    print("     for the fertile feed alone, which is below one, so the")
    print(f"     critical buckling is negative and"
          f" {critical_dimension_cm(k_fert, 'sphere', MIGRATION_AREA_CM2_LO)}"
          " is what the")
    print("     geometry returns. THE FERTILE FEED IS NOT A CRITICALITY")
    print("     QUESTION. If the question had been only about uranium, it")
    print("     would end here.")
    print()
    print("  2. THE FISSILE IS, AND THE GEOMETRY IS COMFORTABLE")
    print()
    print(f"     The fuel salt at the operating fraction"
          f" ({100*f_op:.1f} % fissile) has")
    print(f"     k_inf = {k_fuel:.4f}. Critical dimensions follow from"
          " diffusion theory:")
    print()
    print("       shape                dimension     critical at      store below")
    for shape in SHAPES:
        which, _ = SHAPES[shape]
        d_lo = critical_dimension_cm(k_fuel, shape, MIGRATION_AREA_CM2_LO)
        d_hi = critical_dimension_cm(k_fuel, shape, MIGRATION_AREA_CM2_HI)
        if d_lo is None:
            continue
        worst = min(d_lo, d_hi)
        print(f"       {shape:<20} {which:<12} {worst/100:5.2f} -"
              f" {max(d_lo,d_hi)/100:4.2f} m    {worst/SAFETY_FACTOR/100:5.2f} m")
    print()
    print(f"     The band is the migration area,"
          f" {MIGRATION_AREA_CM2_LO:.0f}-{MIGRATION_AREA_CM2_HI:.0f} cm^2, and the")
    print("     tighter end is the conservative one because it makes the")
    print("     critical size SMALLER. Storage limits are quoted against it")
    print(f"     with a factor of {SAFETY_FACTOR:.0f} on the dimension.")
    print()
    print("     THAT IS A COMFORTABLE ANSWER AND THE REASON IS DILUTION. The")
    print(f"     fissile is {100*f_op:.1f} % of a heavy metal that is itself part of")
    print("     a salt, so the critical sizes are METRES. Compare the figure")
    print("     everyone knows: a bare sphere of plutonium metal is critical")
    print("     at about 5 cm radius. Favourable-geometry storage here means")
    print("     pipes and trays of ordinary dimensions, not precision")
    print("     engineering.")
    print()
    print("  3. AND THE OPERATING CORE IS LARGER THAN THAT, WHICH IS NOT A")
    print("     CONTRADICTION AND IS WORTH SAYING PLAINLY")
    print()
    r_m, h_m = M.fuel_zone_cylinder()
    r_c = critical_dimension_cm(k_fuel, "infinite cylinder",
                                MIGRATION_AREA_CM2_LO) / 100.0
    print(f"     The fuel zone is {r_m:.2f} m in radius against a critical")
    print(f"     cylinder radius of {r_c:.2f} m. The core IS above the critical")
    print("     geometry, and it is subcritical because the design holds")
    print("     k = 0.95 by its FISSILE FRACTION, not by its size. That is the")
    print("     whole architecture: a driven assembly held below one on")
    print("     composition, with the beam supplying what the multiplication")
    print("     does not.")
    print()
    print("     THE CONSEQUENCE FOR STORAGE IS THE IMPORTANT PART. Fuel salt")
    print("     removed from the core must never be allowed to accumulate in")
    print("     a geometry approaching the core's own, and the drain tank is")
    print("     exactly such an accumulation. IT MUST BE FAVOURABLE GEOMETRY")
    print("     BY CONSTRUCTION -- slabs or tubes below the limits above --")
    print("     and restart.py's drained mode assumed a tank without saying")
    print("     so. That is now a stated requirement on it.")
    print()
    print("  4. AND THE RESULT THAT CHANGES THE QUESTION")
    print()
    thr = always_subcritical_threshold()
    floor = F.loop_floor()
    _, g_thr, ch_thr = F.charge_and_gain(thr, "Pu239", "U238",
                                         P.LEAK_PARASITIC_LO)
    _, g_op, ch_op = F.charge_and_gain(f_op, "Pu239", "U238",
                                       P.LEAK_PARASITIC_LO)
    print(f"     BELOW {100*thr:.2f} % FISSILE, k_inf IS UNDER ONE, and an")
    print("     assembly whose k_inf is under one cannot be made critical by")
    print("     ANY amount in ANY shape -- an infinite block of it is")
    print("     subcritical. Below that fraction, an accumulation of fuel salt")
    print("     is not a criticality question at all. The hazard class does")
    print("     not get managed; it stops existing.")
    print()
    print(f"     And that fraction is INSIDE the operating window."
          f" The loop closes")
    print(f"     from {100*floor:.1f} %, the always-subcritical ceiling is"
          f" {100*thr:.2f} %, and the")
    print(f"     k = 0.95 point is {100*f_op:.1f} %. So there is a real band --")
    print(f"     {100*floor:.1f} % to {100*thr:.2f} % -- in which the plant runs"
          " AND no geometry")
    print("     of its own fuel can ever be critical when dry.")
    print()
    print("       operating point        fissile   gain   charge   dry storage")
    print(f"       always-subcritical    {100*thr:6.2f} % {g_thr:6.1f}"
          f" {ch_thr:6.1f} t   NO geometry")
    print(f"       maximum gain          {100*f_op:6.2f} % {g_op:6.1f}"
          f" {ch_op:6.1f} t   favourable only")
    print()
    print(f"     THE PRICE IS A FACTOR OF {g_op/g_thr:.2f} IN GAIN, and the loop")
    print(f"     requirement is 7.41 -- which {g_thr:.1f} still clears by"
          f" {g_thr/7.41:.2f}x.")
    print("     The plant still works. It sells less surplus.")
    print()
    print("     THIS FILE DOES NOT MAKE THAT CHOICE. What it says is that")
    print("     'never a safety question' is PURCHASABLE here, that the price")
    print("     is known, and that the property bought is intrinsic rather")
    print("     than procedural -- it holds under any handling error, any")
    print("     storage mistake and any spill, because it is a fact about the")
    print("     material and not about the operator.")
    print()
    print("  5. MODERATION, WHICH THIS FILE REFUSES TO COMPUTE")
    print()
    print("     Every serious criticality accident in the industry's history")
    print("     involved moderation, solution, or both. A FAST assembly safely")
    print("     subcritical dry can be critical WET, because water slows")
    print("     neutrons into the range where fission cross sections are")
    print("     hundreds of times larger. The margin computed above is a DRY")
    print("     margin and it does not survive water.")
    print()
    print("     THIS FILE DOES NOT COMPUTE THE WET CASE. Moderation is a")
    print("     spectrum effect and the model here is one-group -- it has no")
    print("     spectrum by construction, so it cannot represent the excursion")
    print("     it would need to bound. A moderated k from a one-group model")
    print("     would look like an answer and would not be one.")
    print()
    print("     WHAT FOLLOWS INSTEAD IS A REQUIREMENT, AND IT IS ABSOLUTE:")
    print("       - no water, no hydrogenous material, and no hydrogenous")
    print("         fire suppressant in any space the fuel salt can reach,")
    print("         including under fault;")
    print("       - the salt is a CHLORIDE and reacts with water to give HCl,")
    print("         so the chemical and the nuclear requirement coincide and")
    print("         reinforce each other rather than trading off;")
    print("       - cooling that could contact the salt is a molten salt or a")
    print("         metal, never water;")
    print("       - and a two-group or transport criticality analysis of every")
    print("         credible ingress path is a DELIVERABLE before any licence,")
    print("         not an optimisation.")
    print()
    print("  6. THE HONEST BOTTOM LINE")
    print()
    print("     Handling and storing the URANIUM is not a safety question --")
    print("     it is a chemical-toxicity and industrial-hygiene question,")
    print("     answered by the same practices that handle any heavy metal.")
    print()
    print("     Handling and storing the FISSILE is a safety question, it is")
    print("     the ordinary and well-understood one, and this design starts")
    print("     from an unusually good position: the fissile is DILUTE, it is")
    print("     never separated (buildpackage's no-separation flowsheet is an")
    print("     architectural commitment, not a procedure), and the critical")
    print("     dimensions are metres.")
    print()
    print("     AND THE FISSILE FRACTION IS A LEVER ON EXACTLY THIS. Run")
    print(f"     below {100*always_subcritical_threshold():.2f} % and no dry accumulation"
          " of fuel salt is")
    print("     critical in any geometry, for a known price in gain.")
    print()
    print("     'NEVER A SAFETY QUESTION' IS NOT A PROMISE THIS OR ANY FILE")
    print("     CAN MAKE. What it can say is that the dominant accident")
    print("     pathway is water ingress, that the requirement excluding it is")
    print("     absolute rather than probabilistic, and that the calculation")
    print("     which would BOUND it has not been done here and is named as")
    print("     owed. A design that says that is safer than one that says")
    print("     nothing, and both are less safe than one that has run the")
    print("     transport code.")
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

    P = _ps()
    print()
    print("  the fertile feed must be a non-question, and provably")
    check("fertile-only k_inf is below one", k_inf_of_fertile_only() < 1.0)
    check("  -- so no size or shape of it is critical",
          critical_dimension_cm(k_inf_of_fertile_only(), "sphere",
                                MIGRATION_AREA_CM2_LO) is None)
    check("  -- and the buckling that says so is negative",
          critical_buckling(k_inf_of_fertile_only(), 200.0) < 0.0)
    sa = specific_activity_bq_per_kg()
    # DU is quoted at roughly 15 MBq/kg; U-238 alone gives a little less,
    # which is right because DU carries some U-234 and U-235 too.
    check("DU specific activity lands in the published range",
          1.0e7 < sa < 1.6e7)

    print()
    print("  the criticality geometry must be geometry")
    k = k_inf_of_fuel()
    check("the fuel salt's k_inf exceeds one, or nothing is critical", k > 1.0)
    check("a sphere is the most reactive shape, so it goes critical smallest",
          critical_dimension_cm(k, "sphere", 200.0)
          > critical_dimension_cm(k, "infinite cylinder", 200.0))
    check("a larger migration area means a larger critical size",
          critical_dimension_cm(k, "sphere", MIGRATION_AREA_CM2_HI)
          > critical_dimension_cm(k, "sphere", MIGRATION_AREA_CM2_LO))
    check("more fissile means a smaller critical size",
          critical_dimension_cm(k_inf_of_fuel(0.20), "sphere", 200.0)
          < critical_dimension_cm(k_inf_of_fuel(0.10), "sphere", 200.0))
    # THE RESULT THIS FILE EXISTS FOR, and it was found by a test failing:
    # 0.05 was written into the line above as "a low fraction" and returned
    # None, because at 5 % NOTHING is critical at any size.
    thr = always_subcritical_threshold()
    check("below a threshold fraction no geometry is critical at all",
          critical_dimension_cm(k_inf_of_fuel(thr * 0.9), "sphere", 200.0)
          is None)
    check("  -- and just above it, something is",
          critical_dimension_cm(k_inf_of_fuel(thr * 1.1), "sphere", 200.0)
          is not None)
    # THE CROSS-CHECK THAT KEEPS THE DECISION HONEST. powersource.K_DESIGN is
    # the adopted operating point and it is DERIVED from the threshold this
    # file computes. This file cannot be imported there without a cycle, so
    # the value is stated once in powersource and asserted here. A change in
    # the cross sections that moved the threshold and did not move K_DESIGN
    # would be a test failure rather than a silent divergence.
    k_at_thr = _fc().k_effective(thr, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    check("powersource's adopted k matches the threshold this file derives",
          abs(k_at_thr - P.K_DESIGN) < 5e-4)
    check("  -- and the adopted point is BELOW the ADS convention",
          P.K_DESIGN < P.K_SAFE)
    check("  -- and it is the highest k the property allows",
          k_inf_of_fuel(thr * 1.02) > 1.0)

    check("the threshold sits between the loop floor and the k=0.95 point",
          _fc().loop_floor() < thr
          < _fc().fraction_for_k(P.K_SAFE, "Pu239", "U238",
                                 P.LEAK_PARASITIC_LO))
    check("  -- so an always-subcritical plant is a real option",
          _fc().charge_and_gain(thr, "Pu239", "U238",
                                P.LEAK_PARASITIC_LO)[1] > 7.41)
    check("an unknown shape is refused rather than guessed",
          _raises(lambda: critical_dimension_cm(k, "torus", 200.0)))
    # and the scale must be metres, which is the whole comfort of the result
    d = critical_dimension_cm(k, "infinite cylinder", MIGRATION_AREA_CM2_LO)
    check("critical dimensions are metres, not centimetres", d > 50.0)

    print()
    print("  the core must be ABOVE critical geometry, which is the point")
    M = _mat()
    r_m, _ = M.fuel_zone_cylinder()
    check("the operating core exceeds the critical cylinder radius",
          r_m * 100.0 > critical_dimension_cm(k, "infinite cylinder",
                                              MIGRATION_AREA_CM2_LO))
    check("  -- so subcriticality is held by composition, not by size",
          P.K_SAFE < 1.0)

    print()
    print("  the refusal must be stated, not implied")
    out = _rendered()
    check("it refuses to compute the moderated case",
          "DOES NOT COMPUTE THE WET CASE" in out)
    check("it names water ingress as the dominant pathway",
          "water ingress" in out)
    check("it does not promise that nothing can ever go wrong",
          "NOT A PROMISE THIS OR ANY FILE" in out)
    check("it states the drain tank as a geometry requirement",
          "FAVOURABLE GEOMETRY" in out)
    check("it prints no probability of an accident",
          "probability of" not in out.lower())

    print()
    print(f"selftest: {fail} failures -> {'PASS' if not fail else 'FAIL'}")
    return 1 if fail else 0


def _raises(fn):
    try:
        fn()
        return False
    except ValueError:
        return True


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
