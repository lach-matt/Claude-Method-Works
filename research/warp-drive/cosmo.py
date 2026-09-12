#!/usr/bin/env python3
"""
cosmo.py -- the shared hypothesis, and the case that is already observed.

Every device-level no-go this project established carries the same hypothesis:

    CM-THEOREM   no isolated system moves its own CoM   P_ADM  -> asympt. flat
    T2-ADM       P_ADM = 0, M_ADM > 0, cannot translate P_ADM  -> asympt. flat
    SSV-NOGO     Natario drives violate the NEC         asymptotically flat
    NO-TAPER     a shift cannot terminate in vacuum     MINKOWSKI background
    NO-PORTAL    topological censorship, no shortcut    asympt. flat + glob. hyp.

Five of eight.  The three that do not (EM-GAP, NO-BORE, SWIMMER) are arithmetic
or local material timescales and are untouched by anything here.

THE UNIVERSE IS NOT ASYMPTOTICALLY FLAT.  It is FLRW, and in FLRW none of those
five theorems is even statable: there is no ADM mass, no ADM momentum, and the
hypotheses of topological censorship fail.

And metric transport faster than light is not speculative there.  It is measured.

  PINNED, Planck 2018 (arXiv:1807.06209): H0 = 67.36 km/s/Mpc, age 13.797 Gyr,
  comoving particle horizon 14.26 Gpc.

stdlib only.
"""
import math, sys

c   = 299792458.0
MPC = 3.0856775814913673e22
GLY = 9.4607304725808e24
YR  = 3.15576e7        # Julian year, 365.25 x 86400 -- must match GLY

H0_KMSMPC   = 67.36          # PINNED Planck 2018
AGE_GYR     = 13.797         # PINNED
HORIZON_GPC = 14.26          # PINNED, comoving particle horizon

def H0():
    """s^-1."""
    return H0_KMSMPC*1e3/MPC

def hubble_time_gyr():
    return 1.0/H0()/(1e9*YR)

def hubble_radius_gly():
    return c/H0()/GLY

def horizon_gly():
    return HORIZON_GPC*1e3*MPC/GLY

def recession(d_gly):
    """Hubble-law recession speed at comoving distance d, in c."""
    return H0()*d_gly*GLY/c

def superluminal_distance_gly():
    """Comoving distance at which recession reaches c: exactly the Hubble radius."""
    return hubble_radius_gly()

def transport_ratio():
    """Comoving horizon divided by (c x age): how far metric transport has
    outrun light in the observed universe."""
    return horizon_gly()/AGE_GYR

# Energy conditions of a perfect fluid, exactly (rho > 0 assumed):
def conditions(w):
    """w = p/rho.  Returns (NEC, WEC, SEC, DEC) as booleans."""
    return (1.0+w >= 0.0, 1.0+w >= 0.0, 1.0+3.0*w >= 0.0, 1.0 >= abs(w))

FLUIDS = [("dust (matter)", 0.0), ("radiation", 1.0/3.0),
          ("curvature", -1.0/3.0), ("cosmological constant", -1.0)]

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-4):
        nonlocal ok
        if isinstance(want, (bool, tuple)):
            good = (got == want)
        else:
            good = abs(got-want) <= tol*abs(want)
        ok &= good
        fmt = (lambda v: str(v)) if isinstance(want, (bool, tuple)) else (lambda v: "%.6g" % v)
        g, w = fmt(got), fmt(want)
        print("  %-40s %18s %18s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Planck 2018 values reproduced")
    chk("H0 (s^-1)", H0(), 2.182989e-18, tol=1e-6)
    chk("Hubble time (Gyr)", hubble_time_gyr(), 14.515918, tol=1e-6)
    chk("Hubble radius (Gly)", hubble_radius_gly(), 14.515918, tol=1e-6)
    chk("  Hubble radius == Hubble time x c (identity)",
        hubble_radius_gly(), hubble_time_gyr(), tol=1e-12)
    chk("comoving particle horizon (Gly)", horizon_gly(), 46.509899, tol=1e-6)

    print("\nMetric transport already exceeds c, in the observed universe")
    chk("recession at the horizon (c)", recession(horizon_gly()), 3.204062, tol=1e-6)
    chk("recession at the Hubble radius (c)", recession(hubble_radius_gly()), 1.0, tol=1e-12)
    chk("horizon / (c x age) -- light outrun by", transport_ratio(), 3.371015, tol=1e-6)
    chk("recession is linear in distance (identity)",
        recession(20.0)/recession(10.0), 2.0, tol=1e-12)

    print("\nEnergy conditions of the expanding fluid")
    n, w_, s, d = conditions(0.0)
    chk("dust: NEC", n, True); chk("dust: WEC", w_, True)
    chk("dust: SEC", s, True); chk("dust: DEC", d, True)
    chk("radiation: all four", all(conditions(1.0/3.0)), True)
    chk("Lambda violates SEC only", conditions(-1.0), (True, True, False, True))
    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE SHARED HYPOTHESIS -- and the case already in the sky")
    print("="*78)
    print("""
Five of the eight bounds this project established assume ASYMPTOTIC FLATNESS:
CM-THEOREM, T2-ADM, SSV-NOGO, NO-TAPER and NO-PORTAL.  In an FLRW universe not
one of them is even statable -- there is no ADM mass, no ADM momentum, and
topological censorship loses its hypotheses.

That is the same shape of finding as CM-THEOREM itself.  There, every failure
shared the word ISOLATED, and dropping it opened the coupling family.  Here,
every failure shares ASYMPTOTICALLY FLAT, and the universe is not.

-- What is already measured ------------------------------------------------""")
    print("  Hubble radius            %8.3f Gly" % hubble_radius_gly())
    print("  comoving particle horizon %7.3f Gly   (Planck 2018)" % horizon_gly())
    print("  age of the universe      %8.3f Gyr" % AGE_GYR)
    print("  recession at the horizon %8.3f c" % recession(horizon_gly()))
    print("  horizon / (c x age)      %8.3f      <-- light outrun by this factor"
          % transport_ratio())
    print("""
  Objects beyond %.2f Gly recede faster than light, and the horizon recedes at
  %.2f c.  This is geodesic: comoving observers are in free fall and feel
  nothing.  There is no thrust, no exotic matter and no violation.
""" % (hubble_radius_gly(), recession(horizon_gly())))
    print("  %-24s %6s %6s %6s %6s %6s" % ("fluid","w","NEC","WEC","SEC","DEC"))
    for name, w in FLUIDS:
        n, we, s, d = conditions(w)
        f = lambda b: " ok " if b else "FAIL"
        print("  %-24s %6.3f %6s %6s %6s %6s" % (name, w, f(n), f(we), f(s), f(d)))
    print("""
  DUST SATISFIES ALL FOUR AND STILL EXPANDS SUPERLUMINALLY AT LARGE DISTANCE.
  Superluminal metric transport therefore requires NO energy-condition
  violation whatever.  It is not exotic, it is not hypothetical, and it is
  not rare -- it is the largest and best-measured thing there is.

-- Stated precisely, because this is where it would be easy to overclaim ----
  WHAT THIS SHOWS.  Metric transport at v > c, geodesic, zero felt
  acceleration, sourced by ordinary matter satisfying all four pointwise
  energy conditions, is OBSERVED.  Warp travel in that sense is not a
  conjecture and never was: TARGET-1 measured a local warp state, and
  cosmology measures the transport.

  WHAT THIS DOES NOT SHOW.  Dropping asymptotic flatness removes the PROOFS,
  not necessarily the OBSTRUCTION.  Five theorems become unstatable; that is
  not the same as their conclusions becoming false.  Nothing here exhibits a
  localized, steerable construction.

  AND THE SIGN IS WRONG.  Expansion SEPARATES.  Travel needs the opposite:
  contraction between here and there.  Nature does that too -- overdense
  regions decouple from the Hubble flow and collapse, with ordinary matter and
  no violation -- which is structure formation, and it is the same borrowed
  gradient the coupling family already exploits, written at cosmological scale.

-- Where this says to look --------------------------------------------------
  The question is no longer "can spacetime transport a payload superluminally
  without exotic matter", because the answer is measured and it is yes.  It is:

      CAN THAT MECHANISM BE LOCALIZED AND GIVEN THE OPPOSITE SIGN?

  Every no-go this project holds was proved in the wrong background.  That does
  not make them false, and it does make them silent on this question.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
