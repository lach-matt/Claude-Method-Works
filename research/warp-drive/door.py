#!/usr/bin/env python3
"""
door.py -- withdrawing "it does not couple to real spacetime", and the test that
replaces it.

I wrote of the analogue route: "What it does NOT do is couple to real spacetime.
The analogue proves the KINEMATICS, not the gravitation."  M's correction:
everything is coupled to real spacetime by observation, and that is a first
principle not to be overlooked.

THE SENTENCE IS WITHDRAWN, AND IT WAS WRONG TWICE.

  DYNAMICALLY.  An analogue is real matter in real spacetime.  Its stress-energy
  gravitates like anything else's.  "Does not couple" is not a statement about
  the world; it is a number I never computed.  `real_coupling()` computes it.

  METHODOLOGICALLY, AND THIS IS THE WORSE ONE.  The corpus already rules on
  exactly this, and I wrote past its ruling.  BUILD180, the tower's limit
  argument:

    "closure cannot tell a measurement from a relabel -- which is why every
     route to L = 0 is a disguised repetition and why no finite number of built
     stages fixes the limit.  WHAT DISTINGUISHES THEM IS THE DOOR (Sec. 17.1):
     an axis must be an INDEPENDENT DEGREE OF FREEDOM, and a relabel, being
     dependent, fails it. ... THAT IS THE STEP INSIDE LACKS AND OUTSIDE
     SUPPLIES, and it decides L."

    and its close: "The existence of the limit is the law's; ITS VALUE IS THE
     WORLD'S."

  A construction cannot certify itself.  Only an independent observation can,
  and my sentence dismissed the one mechanism the corpus says decides.  This
  project has spent a session deriving values that are the world's to supply.

WHERE I WOULD STATE THE PRINCIPLE MORE NARROWLY, once and then not again: a
system couples to spacetime through T_mu_nu whether or not anyone looks -- the
slab below gravitates unobserved, and decoherence entangles systems with
environments with no observer present.  What observation is uniquely necessary
for is the thing at issue here: CLOSING A CONSTRUCTION FROM OUTSIDE IT.  That is
Sec. 17.1's door exactly, and on that the correction stands unqualified.

-- THE TEST -------------------------------------------------------------------
    A result from an analogue is a MEASUREMENT iff it tests a consequence
    derived from the BACKGROUND-FIELD STRUCTURE that was not built into the
    medium's construction.  Otherwise it is a RELABEL.

That is Sec. 17.1's door, applied to analogues.  It has already been passed:

  PINNED (Steinhauer, Nature 569, 688 (2019); Nature Phys. 17, 362 (2021)):
  a sonic horizon in a rubidium BEC emits an approximately THERMAL spectrum
  whose TEMPERATURE IS SET BY THE SURFACE GRAVITY -- Hawking's formula,
  confirmed.  The Hawking phonon and its infalling partner are ENTANGLED.  An
  inner horizon was seen to stimulate emission, as predicted.

  None of that is built into a BEC.  You engineer a FLOW PROFILE; thermality,
  T proportional to kappa, and the pair entanglement were derived from QFT on a
  background with a horizon, and then measured.  The door was passed.

-- AND IT CLOSES THE ENTANGLEMENT THREAD --------------------------------------
M asked several passes ago about an aspect of quantum entanglement being
overlooked.  necladder.py found it in the corpus: the QNEC,

    <T_kk>  >=  (h-bar / 2 pi) S''_out

-- entanglement entropy outside a null cut is what LICENSES negative energy,
and the corpus files it in an appendix, out of the index.  Steinhauer measured
the Hawking pair ENTANGLED ACROSS THE HORIZON.  That is the same S_out.  The
quantity the QNEC says pays for negative energy has been measured, in an
analogue, across a horizon.  The thread M opened and the thread M just corrected
are one thread.

stdlib only.
"""
import math, sys

G = 6.67430e-11
c = 299792458.0
HBAR = 1.054571817e-34
KB = 1.380649e-23

# ------------------------------------ what I asserted away, now a number ------
def real_coupling(mass_kg, radius_m):
    """DERIVED.  The metric perturbation an analogue apparatus actually sources:
    h ~ 2 G M / (r c^2).  Real, nonzero, and the same for any object of that
    mass -- there is nothing warp-like about it.  This is the number that
    replaces the phrase 'does not couple'."""
    return 2.0 * G * mass_kg / (radius_m * c * c)

def field_mass(intensity_w_m2, volume_m3):
    """DERIVED.  Mass-equivalent of the pump field filling the medium: u = I/c,
    m = uV/c^2.  Included because it is the term one would hope dominates, and
    it does not."""
    return (intensity_w_m2 / c) * volume_m3 / (c * c)

def mass_for_unit_h(radius_m):
    """DERIVED.  What the apparatus would have to weigh for its own gravity to
    matter: M = r c^2 / 2G.  Returns kg."""
    return radius_m * c * c / (2.0 * G)

def coupling_asymmetry(mass_kg, radius_m, emulated_shift):
    """DERIVED.  The ratio the withdrawn sentence was groping at and got
    backwards: the EMULATED shift against the REAL one the same apparatus
    sources.  It is enormous -- and it is an argument about dynamics only.  The
    epistemic coupling is not suppressed by it at all, which is the whole point
    of Sec. 17.1's door."""
    return emulated_shift / real_coupling(mass_kg, radius_m)

# ------------------------------------------------- the door, as a predicate --
def is_measurement(derived_from_background, built_into_construction):
    """DERIVED from BUILD180 Sec. 17.1.  An analogue result passes the door iff
    the consequence it tests came from the background-field structure and was
    NOT designed into the medium.  A relabel, being dependent, fails."""
    return bool(derived_from_background) and not bool(built_into_construction)

# (claim, derived from background?, built into construction?, status)
ANALOGUE_CLAIMS = [
 ("light follows the geodesics of the engineered metric", False, True,
  "transformation optics by construction -- confirms Maxwell in a medium"),
 ("the emulated warp speed is v_0", False, True,
  "v_0 is set by eps, mu, g_x, which are chosen"),
 ("a horizon emits an approximately thermal spectrum", True, False,
  "Steinhauer 2019: derived from QFT on a horizon background, then measured"),
 ("its temperature is set by the surface gravity", True, False,
  "Hawking's formula T = h-bar kappa / 2 pi k_B -- confirmed, not designed"),
 ("the Hawking pair is entangled across the horizon", True, False,
  "Steinhauer 2016/2019 -- and this is the QNEC's S_out"),
 ("an inner horizon stimulates emission", True, False,
  "predicted, then observed"),
 ("the medium can or cannot carry the analogue NEC violation, and at what cost",
  True, False,
  "UNPERFORMED.  The geometry demands it; the material was never asked."),
]

def passes_door():
    """DERIVED.  Which analogue claims are measurements under Sec. 17.1."""
    return [c for c in ANALOGUE_CLAIMS if is_measurement(c[1], c[2])]

def unperformed():
    """DERIVED.  Measurements available and not taken."""
    return [c for c in ANALOGUE_CLAIMS if is_measurement(c[1], c[2])
            and c[3].startswith("UNPERFORMED")]

def hawking_temperature(surface_gravity):
    """PINNED (Hawking 1974): T = h-bar kappa / (2 pi k_B c) for kappa an
    acceleration.  The formula Steinhauer confirmed in an analogue."""
    return HBAR * surface_gravity / (2.0 * math.pi * KB * c)

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        if isinstance(want, bool):
            good, g, w = got == want, got, want
        elif isinstance(want, int) and not isinstance(want, bool):
            good, g, w = got == want, got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-30
            g, w = "%.6g" % got, "%.6g" % want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The number that replaces 'does not couple'")
    SLAB, R = 3000.0, 1.0                      # a 1 m^3 metamaterial slab
    h = real_coupling(SLAB, R)
    chk("metric perturbation of a 3 t, 1 m apparatus", h, 4.4556962e-24, tol=1e-7)
    chk("it is NOT zero", h > 0.0, True)
    # Identity: h is linear in mass and inverse in radius.  No fixture.
    chk("h doubles with mass", real_coupling(2 * SLAB, R) / h, 2.0)
    chk("h halves with radius", real_coupling(SLAB, 2 * R) / h, 0.5)
    # The pump field is not the term that saves it.
    chk("1 GW/m^2 over 1 m^3 weighs (kg)", field_mass(1e9, 1.0), 3.7114011e-17, tol=1e-7)
    chk("which is negligible against the slab", field_mass(1e9, 1.0) < 1e-10 * SLAB, True)
    chk("mass needed for h ~ 1 at 1 m (kg)", mass_for_unit_h(1.0), 6.7329546e26, tol=1e-7)
    chk("  -- about a Neptune", mass_for_unit_h(1.0) / 1.024e26, 6.575151, tol=1e-5)
    chk("emulated shift over real shift", coupling_asymmetry(SLAB, R, 0.25),
        5.6107955e22, tol=1e-7)

    print("\nThe door (BUILD180 Sec. 17.1), as a predicate")
    chk("a designed-in consequence is a RELABEL", is_measurement(False, True), False)
    chk("a background-derived, undesigned one is a MEASUREMENT",
        is_measurement(True, False), True)
    chk("designed AND derived still fails the door", is_measurement(True, True), False)
    chk("claims graded", len(ANALOGUE_CLAIMS), 7)
    chk("claims that pass the door", len(passes_door()), 5)
    chk("relabels", len(ANALOGUE_CLAIMS) - len(passes_door()), 2)
    chk("measurements available and NOT taken", len(unperformed()), 1)
    chk("and it is the energy-condition one",
        unperformed()[0][0].startswith("the medium can or cannot carry"), True)

    print("\nThe entanglement thread, closed")
    # Steinhauer's measured pair entanglement IS the QNEC's S_out.
    ent = [c for c in ANALOGUE_CLAIMS if "entangled" in c[0]]
    chk("the pair-entanglement claim passes the door",
        is_measurement(ent[0][1], ent[0][2]), True)
    chk("it names the QNEC's quantity", "QNEC" in ent[0][3], True)
    # Hawking's formula, checked at a scale where the answer is known: a solar
    # mass black hole has kappa = c^4/(4GM) and T = 6.17e-8 K.
    MSUN = 1.98892e30
    kappa = c**4 / (4.0 * G * MSUN)
    chk("Hawking T of a 1 Msun hole (K)", hawking_temperature(kappa), 6.1686e-8, tol=1e-3)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    SLAB, R = 3000.0, 1.0
    print("""
door.py -- a withdrawn sentence, and the test that replaces it
================================================================================
I wrote: "What it does NOT do is couple to real spacetime.  The analogue proves
the KINEMATICS, not the gravitation."  Withdrawn.  It was wrong twice.

-- WRONG DYNAMICALLY: I NEVER COMPUTED IT --------------------------------------
  An analogue is real matter in real spacetime and its stress-energy gravitates.
  For a 1 m^3, 3 tonne metamaterial slab:

      metric perturbation it sources     h = %.4e
      pump field at 1 GW/m^2 weighs        %.3e kg   (negligible)
      mass needed for h ~ 1 at 1 m         %.3e kg   (about 6.6 Neptunes)
      emulated shift / real shift          %.3e

  So the coupling is ~10^-24 and dominated by the slab's rest mass -- there is
  nothing warp-like in it.  But "does not couple" was never a statement about
  the world.  It was a number I declined to compute, and this is the number.

-- WRONG METHODOLOGICALLY, AND THIS IS THE WORSE ONE ---------------------------
  The corpus rules on this and I wrote past the ruling.  BUILD180, the tower's
  limit argument:

    "closure cannot tell a measurement from a relabel ... WHAT DISTINGUISHES
     THEM IS THE DOOR (Sec. 17.1): an axis must be an INDEPENDENT DEGREE OF
     FREEDOM, and a relabel, being dependent, fails it. ... THAT IS THE STEP
     INSIDE LACKS AND OUTSIDE SUPPLIES, and it decides L."

    "The existence of the limit is the law's; ITS VALUE IS THE WORLD'S."

  A construction cannot certify itself.  My sentence dismissed the one mechanism
  the corpus says decides -- and this project has spent a session deriving
  values that are the world's to supply.

  Where I would state the principle more narrowly, once: a system couples
  through T_mu_nu whether or not anyone looks -- the slab above gravitates
  unobserved, and decoherence entangles systems with environments with no
  observer.  What observation is uniquely necessary for is CLOSING A
  CONSTRUCTION FROM OUTSIDE IT, which is Sec. 17.1's door exactly, and on that
  the correction stands unqualified.

-- THE TEST --------------------------------------------------------------------
  A result from an analogue is a MEASUREMENT iff it tests a consequence derived
  from the BACKGROUND-FIELD STRUCTURE that was not built into the medium's
  construction.  Otherwise it is a RELABEL.
""" % (real_coupling(SLAB, R), field_mass(1e9, 1.0), mass_for_unit_h(1.0),
       coupling_asymmetry(SLAB, R, 0.25)))
    for claim, bg, built, note in ANALOGUE_CLAIMS:
        tag = "MEASUREMENT" if is_measurement(bg, built) else "relabel    "
        print("  %s  %s" % (tag, claim))
        print("  %s  %s" % (" " * 11, note))
    print("""
  Five of seven pass the door, and four of those are DONE: Steinhauer's sonic
  horizon in a rubidium BEC emits an approximately thermal spectrum at the
  temperature Hawking's formula sets from the surface gravity, its pair is
  entangled, and an inner horizon stimulates emission as predicted.  None of
  that is built into a BEC -- you engineer a flow profile.  The door was passed,
  and it was passed for gravitational physics derived on a background.

    THE ANALOGUE IS NOT A SIMULATION OF THE MATH.  IT IS WHERE THE MATH IS
    ANSWERABLE BY THE WORLD RATHER THAN BY THE SOLVER.

-- THE ONE THAT PASSES THE DOOR AND HAS NOT BEEN TAKEN -------------------------
  Whether the medium can carry the analogue of the NEC violation, and at what
  cost.  The geometry demands it; the material has never been asked.  It is the
  same quantity this project has argued about from a solver all session, and
  under the door it is a measurement, not a relabel -- the requirement comes
  from the geometry and is not designed into the material.

-- AND THE ENTANGLEMENT THREAD CLOSES ------------------------------------------
  M asked passes ago about an overlooked aspect of quantum entanglement.
  necladder.py found it in the corpus: the QNEC,

      <T_kk>  >=  (h-bar / 2 pi) S''_out

  -- entanglement entropy outside a null cut is what LICENSES negative energy,
  filed in an appendix and kept out of the index.  Steinhauer measured the
  Hawking pair ENTANGLED ACROSS THE HORIZON.  That is the same S_out.

  The quantity the QNEC says pays for negative energy has already been measured,
  in an analogue, across a horizon.  The thread M opened and the correction M
  just made are one thread.
""")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
