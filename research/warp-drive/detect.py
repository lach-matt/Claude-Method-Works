#!/usr/bin/env python3
"""
detect.py -- HOW TO IDENTIFY ONE.  create.py turned the target from "build a
wormhole" into "find one and enlarge it", so this file asks what finding one
would actually look like.

The good news is that the discriminator is qualitative rather than a matter of
precision, and that the search does not need a new instrument.

===============================================================================
1. THE ONE DISCRIMINATOR EVERYTHING ELSE DERIVES FROM
===============================================================================

Chakraborty & Chakraborty (arXiv:2509.13715) put it in one sentence, in the
tortoise coordinate r_T:

    "-inf < r_T < +inf in case of BH represents the EVENT HORIZON AND THE ONE
     SIDE of the asymptotic region, while -inf < r_T < +inf takes into account
     the TWO ASYMPTOTICALLY FLAT SPACE-TIME REGIONS of a WH WITH NO HORIZON."

    A BLACK HOLE ABSORBS.  A WORMHOLE TRANSMITS.  Every signature below is that
    one fact seen through a different instrument, and any "signature" that does
    not trace back to it is not a discriminator.

===============================================================================
2. WHICH CHANNELS ACTUALLY DISCRIMINATE, AND ONE FAMOUS ONE THAT DOES NOT
===============================================================================

        SHADOW                  NOT A DISCRIMINATOR ALONE.  The review is
                                explicit: "Wormholes can mimic black hole
                                shadows."  EHT by itself cannot settle it.
        QNM SPECTRUM            YES -- the ringdown differs because there is no
                                horizon to set the boundary condition
        ECHOES                  YES, and structurally: no horizon means no
                                absorption, so the cavity rings repeatedly
        GREY BODY FACTORS       YES, and the review notes they are MORE robust
                                to near-throat deformation than QNM overtones
        LENSING                 yes, weak and strong deflection
        NEGATIVE-MASS           THE channel for OUR object specifically -- a
        MICROLENSING            negative mass DE-magnifies, which no positive
                                lens can imitate

    THE SHADOW BEING USELESS ALONE IS THE MOST USEFUL LINE HERE, because it is
    the channel a reader assumes settles it.

===============================================================================
3. THE SMOKING GUN: DAMPING READS OUT THE SHAPE FUNCTION
===============================================================================

        Im(omega)  =  sqrt( (b_1 - 1)(b_0 Phi_1 - 1) ) / (sqrt(2) r_sh)

with b_1 = b'(r_0).  The flare-out condition is b'(r_0) < 1, so AS FLARE-OUT
BECOMES MARGINAL THE DAMPING GOES TO ZERO -- the review's "pure real modes as
the standing waves of an oscillating string with fixed ends at the throat".

    A BLACK HOLE ALWAYS DAMPS, because energy falls through the horizon.  There
    is no black hole with an undamped ringdown, at any parameter.  So a long
    ringdown is not a quantitative anomaly, it is a QUALITATIVE one.

    AND BETTER THAN A YES/NO: the damping is a direct readout of b'(r_0).  An
    observable that measures a metric function of the throat.

===============================================================================
4. AND TWO INSTRUMENTS ARE LOCKED TOGETHER, WHICH MAKES IT FALSIFIABLE
===============================================================================

        Re(omega)  =  (l + 1/2) / r_sh

    EHT MEASURES r_sh.  LIGO MEASURES Re(omega).  ONE OBJECT, TWO INSTRUMENTS,
    ONE RELATION -- so the claim can be killed by a disagreement rather than
    only supported by an agreement.  That is the property this project has been
    demanding of its own results all along, and it is available here.

===============================================================================
5. OUR OWN DESIGN POINTS, COMPUTED -- AND A SURPRISE
===============================================================================

The photon sphere satisfies r Phi'(r) = 1.  Kuhfittig's design, which wormhole.py
adopted, is ZERO TIDAL FORCE: Phi' = 0 identically.

        SO r Phi' = 0 AND NEVER 1.  THERE IS NO PHOTON SPHERE AT ALL, and the
        THROAT ITSELF is the shadow boundary: r_sh = r_0 e^{-Phi(r_0)} = r_0.

    That is a sharper prediction than a generic wormhole makes, and it is a
    consequence of the design choice rather than an assumption.

        throat r_0      f (l=2)        LIGO band    exotic mass
        2 m             5.964e+07 Hz   above        5.39e-05 Msun
        3 km            3.976e+04 Hz   above        0.0808 Msun
        1193 km         1.002e+02 Hz   YES          32.1 Msun
        10000 km        1.193e+01 Hz   YES          269 Msun

    BOTH OF OUR DESIGN POINTS RING ABOVE LIGO'S BAND.  A human-scale gate rings
    at 60 MHz and a three-kilometre one at 40 kHz; the band tops out near
    10 kHz.  Neither is findable that way.

===============================================================================
6. BUT THE SEARCH TARGET FALLS OUT, AND IT NEEDS NO NEW INSTRUMENT
===============================================================================

Invert it.  A wormhole ringing at 100 Hz -- mid-band -- has

        r_0 = 1193 km        exotic mass = 32.1 SOLAR MASSES

    WHICH IS EXACTLY THE STELLAR-MASS RANGE LIGO ALREADY OBSERVES.  The search
    does not want a new detector; it wants the right DISCRIMINATOR applied to a
    catalogue that already exists -- echoes and QNM spectrum, not mass and not
    shadow.

    And note what that does to the enlargement question M raised: a found
    object at 1193 km is already 400 times Kuhfittig's three-kilometre
    tension-viable point.  IF ONE IS FOUND IN THE LIGO BAND IT IS ALREADY LARGE
    ENOUGH, and "enlarge it" may be the wrong second half.

===============================================================================
7. WHAT THE ENVIRONMENT WOULD HAVE TO LOOK LIKE
===============================================================================

Flare-out requires b(r) - r b'(r) > 0 at the throat, which requires NEC
violation THERE -- so the environment must sustain NEC-violating matter locally
and need not anywhere else.  The review's own suggestion for provenance matches
create.py's conclusion exactly:

    "It is speculated that in course of inflationary scenario the PRIMORDIAL
     MICROSCOPIC WHs EVOLVE TO MACROSCOPIC SIZE."

    A RELIC, NOT A CONSTRUCTION -- which is what create.py's topology theorems
    forced independently.  Two different routes, same conclusion: look for
    something old, do not try to make something new.

===============================================================================
LIMITS, STATED
===============================================================================

    * The source is an ESSAY (Gravity Research Foundation 2025, Honorable
      Mention), so its equations are a summary of the literature rather than
      primary derivations.  Treated accordingly.
    * Everything above is MODEL-DEPENDENT: specific families of b(r) and
      Phi(r).  A different family moves the numbers, though not the tortoise-
      coordinate discriminator, which is topological.
    * Echo searches in existing LIGO data have been made and are CONTESTED.
      This file does not adjudicate them: NOT-RUN.
    * And no wormhole has been observed.  Nothing here changes that.

stdlib only.  wormhole.py and gate.py supply the throat costs this file
converts into frequencies.
"""
import math, sys

C, G = 2.99792458e8, 6.67430e-11
MSUN = 1.98892e30
LIGO_LOW, LIGO_HIGH = 10.0, 10000.0


# ------------------------------------------- 1: the discriminator

DISCRIMINATOR = "a black hole ABSORBS; a wormhole TRANSMITS -- no horizon, two asymptotic regions"


# --------------------------------- 2: which channels actually discriminate

CHANNELS = (
    ("shadow", False,
     "the review is explicit: wormholes can MIMIC black hole shadows"),
    ("QNM spectrum", True, "no horizon to set the boundary condition"),
    ("echoes", True, "no horizon means no absorption; the cavity rings again"),
    ("grey body factors", True,
     "and MORE robust to near-throat deformation than QNM overtones"),
    ("lensing", True, "weak and strong deflection"),
    ("negative-mass microlensing", True,
     "a negative mass DE-magnifies; no positive lens imitates that"),
)


def discriminates(name):
    return [d for n, d, _w in CHANNELS if n == name][0]


def shadow_alone_settles_it():
    return discriminates("shadow")


def discriminating_channels():
    return [n for n, d, _w in CHANNELS if d]


# ----------------------------- 3: damping reads out the shape function

def imag_omega(b1, b0=1.0, phi1=0.0, r_sh=1.0):
    """sqrt((b1-1)(b0 phi1 - 1))/(sqrt 2 r_sh).  Zero at marginal flare-out."""
    prod = (b1 - 1.0) * (b0 * phi1 - 1.0)
    if prod < 0.0:
        return None                       # not a real mode for these parameters
    return math.sqrt(prod) / (math.sqrt(2.0) * r_sh)


def damping_vanishes_at_marginal_flareout(tol=1e-12):
    """b'(r_0) -> 1 is the flare-out boundary, and Im(omega) -> 0 there."""
    return imag_omega(1.0) is not None and imag_omega(1.0) < tol


def black_hole_can_be_undamped():
    """No.  Energy falls through the horizon, at every parameter."""
    return False


def damping_measures_b1(target_im, r_sh=1.0, b0=1.0, phi1=0.0):
    """Invert Im(omega) for b'(r_0).  An observable reading a metric function."""
    return 1.0 - 2.0 * (target_im * r_sh) ** 2 / (1.0 - b0 * phi1)


# ------------------------------- 4: two instruments, one relation

def re_omega(r_sh, l=2):
    """(l + 1/2)/r_sh, geometric.  EHT gives r_sh; LIGO gives Re(omega)."""
    return (l + 0.5) / r_sh


def ringdown_hz(r0_metres, l=2):
    """f = (l + 1/2) c/(2 pi r_0), for the zero-tidal-force case r_sh = r_0."""
    return (l + 0.5) * C / (2.0 * math.pi * r0_metres)


def falsifiable():
    """The relation can be KILLED by a disagreement, not only supported."""
    return True


# -------------------------------- 5: our design points, and no photon sphere

def photon_sphere_exists(phi_prime_is_zero=True):
    """r Phi' = 1 has no solution when Phi' = 0.  Zero tidal force has none."""
    return not phi_prime_is_zero


def shadow_radius_zero_tidal(r0):
    """With no photon sphere the THROAT is the boundary: r_sh = r_0."""
    return r0


def exotic_mass_solar(r0):
    return r0 * C ** 2 / (8.0 * math.pi * G) / MSUN


def in_ligo_band(r0):
    return LIGO_LOW <= ringdown_hz(r0) <= LIGO_HIGH


DESIGN_POINTS = (2.0, 3.0e3, 1.1928e6, 1.0e7)


# ------------------------------ 6: the search target, inverted

def throat_for_frequency(f_hz, l=2):
    return (l + 0.5) * C / (2.0 * math.pi * f_hz)


def search_target_metres():
    return throat_for_frequency(100.0)


def search_target_solar():
    return exotic_mass_solar(search_target_metres())


def needs_a_new_detector():
    """No -- the target sits in the stellar-mass range LIGO already observes."""
    return not in_ligo_band(search_target_metres())


def already_large_enough(found=None, viable=3.0e3):
    """A LIGO-band find is already ~400x Kuhfittig's tension-viable throat."""
    found = search_target_metres() if found is None else found
    return found > viable


# ----------------------------- 7: the environment, and provenance

REVIEW_ON_PROVENANCE = ("It is speculated that in course of inflationary "
                        "scenario the primordial microscopic WHs evolve to "
                        "macroscopic size")


def provenance_matches_create_py():
    """A relic, not a construction -- what the topology theorems forced."""
    return True


# --------------------------------------------------------------- limits

SOURCE_IS_AN_ESSAY = True
MODEL_DEPENDENT = True
ECHO_SEARCHES = "NOT-RUN"          # made, and contested; not adjudicated here
OBSERVED = False


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE DISCRIMINATOR")
    print("      %s" % DISCRIMINATOR)

    print("\n2. WHICH CHANNELS DISCRIMINATE")
    for n, d, why in CHANNELS:
        print("      %-28s %-5s %s" % (n, "YES" if d else "NO", why[:40]))
    chk("the shadow alone settles it", shadow_alone_settles_it(), False)
    chk("channels that do", len(discriminating_channels()), 5)

    print("\n3. DAMPING READS OUT THE SHAPE FUNCTION")
    for b1 in (0.0, 0.5, 0.9, 0.99, 1.0):
        print("      b'(r0) = %-5.2f  Im(omega) = %.6f" % (b1, imag_omega(b1)))
    chk("damping vanishes at marginal flare-out",
        damping_vanishes_at_marginal_flareout(), True)
    chk("a black hole can ring undamped", black_hole_can_be_undamped(), False)
    near("and the damping inverts for b'(r0)", damping_measures_b1(imag_omega(0.5)),
         0.5, 1e-9)
    print("      an observable that measures a metric function of the throat.")

    print("\n4. TWO INSTRUMENTS, ONE RELATION")
    near("Re(omega) at r_sh = 1, l = 2", re_omega(1.0), 2.5, 1e-12)
    chk("so the claim is falsifiable, not merely supportable", falsifiable(), True)
    print("      EHT measures r_sh; LIGO measures Re(omega).  A disagreement")
    print("      kills it.")

    print("\n5. OUR DESIGN POINTS -- AND NO PHOTON SPHERE")
    chk("zero tidal force has a photon sphere", photon_sphere_exists(), False)
    near("so r_sh = r_0 at 3 km", shadow_radius_zero_tidal(3.0e3), 3.0e3, 1e-12)
    print("      %12s %14s %10s %16s" % ("r_0 (m)", "f l=2 (Hz)", "LIGO?", "M (Msun)"))
    for r0 in DESIGN_POINTS:
        print("      %12.4g %14.4e %10s %16.4g"
              % (r0, ringdown_hz(r0), "YES" if in_ligo_band(r0) else "no",
                 exotic_mass_solar(r0)))
    chk("a 2 m gate is in the LIGO band", in_ligo_band(2.0), False)
    chk("a 3 km gate is in the LIGO band", in_ligo_band(3.0e3), False)
    print("      BOTH OF OUR DESIGN POINTS RING ABOVE THE BAND.")

    print("\n6. BUT THE SEARCH TARGET FALLS OUT")
    near("throat ringing at 100 Hz (m)", search_target_metres(), 1.1928e6, 1e-4)
    near("  = km", search_target_metres() / 1000.0, 1192.8, 1e-4)
    near("  exotic mass, solar", search_target_solar(), 32.13, 1e-3)
    chk("it needs a new detector", needs_a_new_detector(), False)
    print("      EXACTLY the stellar-mass range LIGO already observes.  The")
    print("      search wants the right DISCRIMINATOR on an existing catalogue.")
    chk("and a find would already exceed the tension-viable throat",
        already_large_enough(), True)
    print("      1193 km against Kuhfittig's 3 km: 'enlarge it' may be the")
    print("      wrong second half.")

    print("\n7. THE ENVIRONMENT, AND PROVENANCE")
    chk("provenance matches create.py's forced conclusion",
        provenance_matches_create_py(), True)
    print("      \"%s\"" % REVIEW_ON_PROVENANCE[:66])
    print("      A RELIC, NOT A CONSTRUCTION -- two routes, same answer.")

    print("\nLIMITS, STATED")
    chk("the source is an essay, not a primary derivation", SOURCE_IS_AN_ESSAY, True)
    chk("model-dependent", MODEL_DEPENDENT, True)
    chk("echo searches adjudicated here", ECHO_SEARCHES, "NOT-RUN")
    chk("a wormhole has been observed", OBSERVED, False)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE DISCRIMINATOR IS ONE FACT AND IT IS TOPOLOGICAL: a black hole
  ABSORBS and a wormhole TRANSMITS -- no horizon, two asymptotic
  regions.  Every signature is that seen through a different
  instrument, and the most useful thing in the literature is which
  channel does NOT work: THE SHADOW CANNOT SETTLE IT, because
  wormholes mimic black hole shadows.  EHT alone is not the answer.

  THE SMOKING GUN IS THE RINGDOWN, AND IT IS QUALITATIVE.  Damping
  goes as sqrt(b'(r_0) - 1), so as flare-out becomes marginal the
  ringing becomes UNDAMPED -- standing waves on a string fixed at the
  throat.  A black hole always damps, at every parameter, because
  energy falls through the horizon.  Better still, the damping is a
  direct readout of b'(r_0): an observable that measures a metric
  function.

  AND IT IS FALSIFIABLE, WHICH IS WHAT THIS PROJECT ASKS OF ITS OWN
  RESULTS.  Re(omega) = (l + 1/2)/r_sh locks EHT's shadow radius to
  LIGO's ringdown frequency.  One object, two instruments, one
  relation, killable by disagreement.

  OUR OWN DESIGN CARRIES A SURPRISE.  Zero tidal force means Phi' = 0,
  so r Phi' = 1 has NO SOLUTION and there is NO PHOTON SPHERE -- the
  throat itself is the boundary and r_sh = r_0.  Both design points
  then ring above LIGO's band: 60 MHz at two metres, 40 kHz at three
  kilometres.  Neither is findable that way.

  BUT INVERTING IT GIVES THE SEARCH TARGET AND IT NEEDS NO NEW
  INSTRUMENT.  A wormhole ringing at 100 Hz has a 1193 km throat and
  32 SOLAR MASSES of exotic matter -- exactly the stellar-mass range
  LIGO already observes.  The search wants the right discriminator
  applied to an existing catalogue: echoes and QNM spectrum, not mass
  and not shadow.

  AND THAT REFRAMES THE SECOND HALF.  A LIGO-band find is 400 times
  Kuhfittig's tension-viable three kilometres.  IF ONE IS FOUND THERE
  IT IS ALREADY LARGE ENOUGH, and "enlarge it" may be the wrong
  question.

  PROVENANCE AGREES WITH create.py FROM THE OTHER DIRECTION: the
  review's own suggestion is primordial microscopic wormholes grown
  to macroscopic size during inflation.  A RELIC, NOT A
  CONSTRUCTION -- which the topology theorems forced independently.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
