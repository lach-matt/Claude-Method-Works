#!/usr/bin/env python3
"""
gradients.py -- is the space of usable gradients closed?

"The engine is a found object nobody has found" hides three different claims.
This file separates them, and then asks the question underneath: is there a
SIXTH kind of gradient nobody has tried, or is the space enumerable and closed?

A gradient you can couple to is a metric perturbation, and in vacuum GR its
character is exhausted by what sources it:

    1  MASS at rest        static well            THE-BORROWED-WELL.md
    2  MOMENTUM            moving well            THE-ENGINE.md, THE-GR-FLYBY.md
    3  ANGULAR MOMENTUM    rotating well          kerr.py
    4  RADIATION           propagating wave       <- never examined until now
    5  COSMOLOGICAL        expanding background   cosmo.py

That list is the multipole character of the field plus the background it sits
on. There is no sixth entry to find.

stdlib only.
"""
import math, sys

G, c, hbar = 6.67430e-11, 299792458.0, 1.054571817e-34
MSUN, AU, YR = 1.98892e30, 1.495978707e11, 3.15576e7

# ---- 4. RADIATION: the one type this project never priced -------------------
def h_memory(eps, M, r):
    """Permanent strain left by a burst radiating eps*Mc^2, at distance r.

    h_mem ~ G dE / (c^4 r) = eps G M / (c^2 r) = (eps/2)(r_s/r).
    Order-of-magnitude; the angular factor is O(1) and is not carried.
    """
    return 0.5*eps*(2.0*G*M/c**2)/r

def memory_displacement(eps, M, r, L):
    """Permanent displacement of a free-falling pair separated by L."""
    return 0.5*h_memory(eps, M, r)*L

# ---- can the engine be manufactured? ----------------------------------------
def t_evap(M):
    """Hawking lifetime, 5120 pi G^2 M^3 / (hbar c^4)."""
    return 5120.0*math.pi*G**2*M**3/(hbar*c**4)

def mass_for_lifetime(t):
    return (t*hbar*c**4/(5120.0*math.pi*G**2))**(1.0/3.0)

# ---- the tidal floor is a PAYLOAD-SIZE constraint, not an engine one --------
def mass_floor(a_max_g, d, r_over_rs=3.0):
    """Deflector mass holding the tide under a_max across payload extent d.

    Radius in units of r_s, MATCHING slingshot.py -- an earlier draft used units
    of M and disagreed with it by exactly sqrt(8), since r_s = 2M. The identity
    check below now pins the two instruments together.
    """
    return c**3*math.sqrt(d/(a_max_g*9.80665))/(2.0*G*r_over_rs**1.5)

GRADIENTS = [
 ("1 static well",    "mass at rest",      "LENS: returns on exit what it gave on entry"),
 ("2 moving well",    "momentum",          "PUMP: dv = 2U/(1+U^2), bounded by SPEED not depth"),
 ("3 rotating well",  "angular momentum",  "CIRCULAR: drags at 0.5c and points nowhere"),
 ("4 radiation",      "GW memory",         "DISPLACEMENT only: no velocity, ~cm at 10 r_s"),
 ("5 cosmological",   "expansion",         "WRONG SIGN: separates, and unlocalizable"),
]

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        good = (got == want) if isinstance(want, bool) else abs(got-want) <= tol*abs(want)
        g = got if isinstance(want, bool) else "%.7g" % got
        w = want if isinstance(want, bool) else "%.7g" % want
        ok &= good
        print("  %-52s %13s %13s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Radiation -- the gradient never priced here")
    chk("h_mem at 10 r_s, eps = 0.05", h_memory(0.05, 10*MSUN, 10*2*G*10*MSUN/c**2), 2.5e-3)
    chk("h_mem falls as 1/r (identity)",
        h_memory(0.05,10*MSUN,2e9)/h_memory(0.05,10*MSUN,1e9), 0.5, tol=1e-12)
    chk("h_mem is linear in eps (identity)",
        h_memory(0.10,10*MSUN,1e9)/h_memory(0.05,10*MSUN,1e9), 2.0, tol=1e-12)
    rs10 = 2*G*10*MSUN/c**2
    chk("displacement of a 20 m payload at 10 r_s (m)",
        memory_displacement(0.05, 10*MSUN, 10*rs10, 20.0), 0.025)
    chk("  and at 1 AU (m)", memory_displacement(0.05, 10*MSUN, AU, 20.0), 4.9365805e-8, tol=1e-6)

    print("\nManufacture -- can we make the deflector?")
    chk("a 1 tonne hole evaporates in (s)", t_evap(1e3), 8.4114779e-8, tol=1e-6)
    chk("evaporation is cubic in mass (identity)", t_evap(2e3)/t_evap(1e3), 8.0, tol=1e-12)
    M100 = mass_for_lifetime(100*YR)
    chk("mass to last a century (kg)", M100, 3.3476796e8, tol=1e-6)
    chk("  its r_s (m)", 2*G*M100/c**2, 4.9720807e-19, tol=1e-6)
    chk("  r_s is far inside a proton (1e-15 m)", 2*G*M100/c**2 < 1e-15, True)

    print("\nThe tidal floor is a PAYLOAD constraint")
    chk("floor scales as sqrt(payload extent) (identity)",
        mass_floor(1.0, 80.0)/mass_floor(1.0, 20.0), 2.0, tol=1e-12)
    # slingshot.py reports 27901.6 for the same configuration; it used g = 9.8 where
    # this uses standard gravity 9.80665, and sqrt(9.80665/9.8) = 1.00034 is the gap.
    chk("20 m payload at 1 g (Msun)", mass_floor(1.0,20.0)/MSUN, 27892.141, tol=1e-6)
    chk("  agrees with slingshot.py up to the g convention",
        mass_floor(1.0,20.0)/MSUN*math.sqrt(9.80665/9.8), 27901.6, tol=1e-4)
    chk("1 mm payload at 1 g (Msun)", mass_floor(1.0,1e-3)/MSUN, 197.22722, tol=1e-6)
    chk("a proton-scale payload needs no IMBH",
        mass_floor(1.0,1e-15)/MSUN < 1.0, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print('"A FOUND OBJECT NOBODY HAS FOUND" -- three claims, separated')
    print("="*78)
    print("""
CLAIM 1: THE CLASS EXISTS AND IS OBSERVED.  LIGO has catalogued of order a
hundred black-hole binaries.  These are engines of exactly the specified type,
and they are not hypothetical.

CLAIM 2: THEY ALREADY DO THIS.  Zhang's mechanism is not a proposal for a
machine -- it is an explanation of ultra-high-energy cosmic rays.  Particles
swept into chaotic orbits around a black-hole binary take repeated slingshots
and leave at extreme Lorentz factors.  THE ENGINE IS OBSERVED RUNNING, and the
payload it carries is a proton.

CLAIM 3: NOBODY HAS FOUND ONE BIG ENOUGH TO CARRY A PERSON.  That is the only
part that is missing, and it is a payload-size constraint, not an engine one.

-- Why the payload size sets the engine size -------------------------------""")
    print("  %-26s %16s" % ("payload extent at 1 g", "deflector floor"))
    for d, lbl in ((20.0,"20 m hull"), (1.0,"1 m unit"), (1e-2,"1 cm unit"),
                   (1e-3,"1 mm grain"), (1e-15,"a proton")):
        print("  %-26s %13.4g Msun" % (lbl, mass_floor(1.0, d)/MSUN))
    print("""
  Tides fall as 1/M^2 and rise linearly with payload extent, so the floor goes
  as sqrt(d) -- a weak scaling that punishes anything human-sized.  A proton
  needs no compact object at all, which is exactly why nature runs this engine
  for cosmic rays and not for ships.

-- Could we make the deflector ourselves? ----------------------------------
  No, and by two independent numbers.  A manufactured black hole must survive:
  Hawking evaporation goes as M^3, so lasting a century needs %.3e kg
  compressed inside r_s = %.3e m -- far smaller than a proton.  And
  degenerate matter needs ~1e34 Pa against a laboratory best of 1e13.

  THE DEFLECTOR IS NOT A DESIGN PROBLEM.  It is an inventory problem.

-- Is there a sixth kind of gradient? --------------------------------------
  A gradient is a metric perturbation, and its character is exhausted by what
  sources it.  The list is not a survey; it is a classification.
""" % (mass_for_lifetime(100*YR), 2*G*mass_for_lifetime(100*YR)/c**2))
    for name, src, verdict in GRADIENTS:
        print("  %-18s %-20s %s" % (name, src, verdict))
    rs10 = 2*G*10*MSUN/c**2
    print("""
  Radiation was the one never priced here, so: a burst radiating 5%% of a
  10 Msun binary leaves a PERMANENT displacement of %.3f m across a 20 m
  payload at 10 r_s, and %.2e m at 1 AU.  It is a displacement, not a
  velocity -- you are moved a few centimetres and then stop.  Dead.

  ONLY ENTRY 2 PUMPS.  The static well is a lens, rotation points nowhere,
  radiation displaces without accelerating, and expansion has the wrong sign
  and cannot be localised.  There is no sixth row to look for: mass, momentum,
  angular momentum, radiation and the background are what a metric has.

-- So, to the question -----------------------------------------------------
  NOT something to design.  We cannot make compact objects, by evaporation and
  by pressure, both computed above.

  NOT an original concept waiting to be had.  The gradient space is closed by
  enumeration, and the one entry that pumps is already in hand.

  IT IS AN INVENTORY PROBLEM WITH AN OBSERVED PROOF OF CONCEPT.  The engine
  runs today, on protons.  Scaling it to a person is not new physics; it is
  finding a heavier deflector, and the required mass follows from the payload
  you insist on carrying.  Shrink the payload and the requirement falls -- as
  sqrt, which is why it is hard, and it is arithmetic rather than a barrier.
""" % (memory_displacement(0.05,10*MSUN,10*rs10,20.0),
       memory_displacement(0.05,10*MSUN,AU,20.0)))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
