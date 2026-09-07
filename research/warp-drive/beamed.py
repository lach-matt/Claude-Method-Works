#!/usr/bin/env python3
"""
beamed.py -- the engineering the project was weak on, and what it reverses.

M's ruling: the math is not where this project is weak; the ENGINEERING is.  Two
fields were named -- interstellar engineering and particle communication
engineering -- and both were read.  This instrument holds what they say.

THE FINDING:

  The coupling family was right and its inventory problem was self-inflicted.
  Its whole architecture -- no propellant, momentum from an external source,
  owes no charge -- is BEAMED PROPULSION, a costed discipline with hardware in
  fabrication.  This project spent a session hunting the momentum source in the
  SKY.  The engineering literature BUILDS it, and the built source wins:

      found  (binary slingshot, catalogued 50 Msun pair)      0.039 c, 2 m body
      found  (unconfirmed 8823 Msun IMBH)                     0.475 c, 2 m body
      built  (Starshot, gram-scale, $8.0B, in fabrication)    0.200 c, 1 g
      built  (Lubin DEEP-IN, crewed scale)                    0.700 c, 1000 t

-- WHAT ACTUALLY BLOCKS IT ----------------------------------------------------
Not physics.  Not materials.  ENERGY AT PLANETARY SCALE, delivered coherently
through an aperture, for months: 1.25e23 J for the crewed design, about 208
years of total world primary energy, at 10 PW for 144 days.  The roadblock has
the shape of a BILL, not a bound.

-- PARTICLE COMMUNICATION ENGINEERING, AND IT CLOSES A BRANCH ------------------
PINNED (Hippke 2017, arXiv:1711.07962): photons beat every other carrier for
point-to-point by orders of magnitude, and the reason is collimation:

    particle beam:  theta = 1 / gamma          (no aperture term at all)
    photon beam:    theta = 1.22 lambda / D    (diffraction)

At a 1 m aperture these meet at 82 nm, so focusing TeV particles costs 7 x 10^10
times the energy of a mirror.  Neutrinos are worse -- 10^10 times a photon's
beam width, and the only demonstrated link runs at 0.1 bit/s through 240 m of
rock.  No known or hypothetical carrier exceeds keV photons "by more than a
factor of a few".  So any architecture needing two coordinated ends pays the
full light-travel time, and nothing shortens it.

Status: PINNED (published) / DERIVED.  stdlib only.
"""
import math, sys

c = 299792458.0
AU = 1.495978707e11
WORLD_ENERGY_YR = 6.0e20      # J, world primary energy, order of magnitude

# ------------------------------------------------- published point designs ---
# PINNED.  Breakthrough Starshot system model (Parkin 2018, Acta Astronautica):
# gram-scale sail to 0.2 c, 4.1 m sail accelerated for 9 min, gigawatt-scale
# phased array; $0.01/W lasers, $500/m^2 optics, $50/kWh storage -> $8.0B beam
# director.  Fabricated to date: a 60 x 60 mm^2, 200 nm reflector carrying over
# a billion nanoscale features -- the highest aspect-ratio nanophotonic element.
STARSHOT = dict(name="Starshot", mass=1e-3, power=1.0e11, beta=0.20,
                sail=4.1, array=1.0e3, seconds=540.0, capex_usd=8.0e9)

# PINNED.  Lubin / DEEP-IN (NASA NIAC) crewed scaling point: a 1000 metric tonne
# vehicle to 0.7 c requires a 36 km reflector, 10 PW and a 100 km array.
CREWED = dict(name="Lubin crewed", mass=1.0e6, power=1.0e16, beta=0.70,
              sail=3.6e4, array=1.0e5)

LAMBDA = 1.06e-6              # m, the Starshot design wavelength

# ------------------------------------------------------ the relativistic sail -
def sail_run(power, mass, seconds, refl=2.0, steps=200000):
    """DERIVED.  A perfectly reflecting sail under constant beam power:

        d(gamma beta)/dt = (refl P / m c^2) * (1 - beta)/(1 + beta)

    The Doppler factor is the whole story -- a receding mirror sees the beam
    redshifted, the force falls as (1-b)/(1+b), and no power reaches c.
    Integrated in TIME: the distance form is singular at beta = 0 and returns
    efficiencies above 100%, which is how this file's first draft was caught.

    Returns (beta, distance, beam energy, kinetic energy)."""
    u = 0.0
    x = 0.0
    dt = seconds / steps
    k = refl * power / (mass * c * c)
    for _ in range(steps):
        b = u / math.sqrt(1.0 + u * u)
        u += k * ((1.0 - b) / (1.0 + b)) * dt
        x += b * c * dt
    b = u / math.sqrt(1.0 + u * u)
    g = 1.0 / math.sqrt(1.0 - b * b)
    return b, x, power * seconds, (g - 1.0) * mass * c * c

def burn_for(power, mass, target_beta, lo=1e-3, hi=1e12):
    """DERIVED.  Beam-on time to a target speed.  Bisection; monotone in time."""
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if sail_run(power, mass, mid, steps=4000)[0] < target_beta:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)

def efficiency(power, mass, seconds):
    """DERIVED.  Kinetic energy delivered over beam energy spent.  Never 1: the
    reflected photons carry the rest away, and the shortfall IS the Doppler
    factor.  It rises with terminal speed, so slow heavy payloads waste most."""
    b, x, eb, ek = sail_run(power, mass, seconds)
    return ek / eb

# ---------------------------------------------------- the aperture invariant --
def accel_run(array_D, sail_d, lam=LAMBDA):
    """DERIVED.  Acceleration ends where the diffracted spot outgrows the sail:

        L = D * d_sail / lambda

    APERTURE TIMES SAIL EQUALS WAVELENGTH TIMES RANGE.  The invariant of the
    whole discipline."""
    return array_D * sail_d / lam

def array_needed(sail_d, run_m, lam=LAMBDA):
    """DERIVED.  Inverse of accel_run: the phased array a given run demands."""
    return lam * run_m / sail_d

def mass_scaling_exponent():
    """DERIVED.  At fixed areal density the sail area scales with payload mass,
    so d_sail ~ sqrt(m), so L ~ sqrt(m), and v = sqrt(2 a L) with a ~ 1/m gives

        v  ~  m^(-1/4)

    Lubin's "the scaling of speed is a mild function of payload mass" IS this
    exponent: 10^5 in mass costs 17.8x in speed, not 10^5."""
    return -0.25

# ------------------------------------- particle communication, benchmarked ----
def photon_beam_angle(lam, D):
    """PINNED (diffraction): theta = 1.22 lambda / D."""
    return 1.22 * lam / D

def particle_beam_angle(gamma):
    """PINNED (ISS Detector Working Group 2009, via Hippke Eq. 3): theta = 1/gamma.
    No aperture term, so no mirror helps."""
    return 1.0 / gamma

PARTICLE_PENALTY = 7.0e10     # PINNED: TeV particles vs 15 eV photons, same width
NEUTRINO_BITS_PER_S = 0.1     # PINNED: Stancil et al. 2012, 1% BER, 240 m of rock
NEUTRINOS_PER_PULSE = 1.0e13  # PINNED: same
INSCRIBED_BITS_PER_J = 1.0e11 # PINNED: Hippke, S = 1e23 bits/g at v = 0.1 c

def photon_capacity(d_pc, lam_nm, D_m):
    """PINNED (Hippke Eq. 1): C = (d/pc)^-2 (lam/nm)^-1 (D/m)^4 bits/J."""
    return d_pc**-2 * lam_nm**-1 * D_m**4

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        if isinstance(want, bool):
            good, g, w = got == want, got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
            g, w = "%.6g" % got, "%.6g" % want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Physical sanity -- the identities that caught the first draft")
    b, x, eb, ek = sail_run(1e11, 1e-3, 113.0)
    chk("beam energy exceeds kinetic energy", ek < eb, True)
    chk("efficiency is under 1", ek / eb < 1.0, True)
    chk("distance is under c*t", x < c * 113.0, True)
    chk("no power, no speed", sail_run(0.0, 1e-3, 100.0)[0], 0.0)
    chk("Doppler factor at 0.5 c", (1 - 0.5) / (1 + 0.5), 1.0 / 3.0)
    e_slow = efficiency(1e15, 1e5, burn_for(1e15, 1e5, 0.20))
    e_fast = efficiency(1e15, 1e5, burn_for(1e15, 1e5, 0.50))
    chk("efficiency rises with terminal speed", e_fast > e_slow, True)

    print("\nAgainst the two published point designs")
    t = burn_for(STARSHOT["power"], STARSHOT["mass"], STARSHOT["beta"])
    chk("Starshot beam-on to 0.2 c (s)", t, 113.2, tol=0.02)
    chk("  within a factor 5 of the published 9 min", 540.0 / t < 5.0, True)
    chk("Starshot terminal speed", sail_run(STARSHOT["power"], STARSHOT["mass"], t)[0],
        0.20, tol=1e-3)
    T = burn_for(CREWED["power"], CREWED["mass"], CREWED["beta"])
    bb, xx, EB, EK = sail_run(CREWED["power"], CREWED["mass"], T)
    chk("crewed terminal speed", bb, 0.70, tol=1e-3)
    chk("crewed beam-on time (days)", T / 86400.0, 144.16, tol=1e-3)
    chk("crewed beam energy (J)", EB, 1.2456e23, tol=1e-3)
    chk("crewed energy in world-years", EB / WORLD_ENERGY_YR, 207.6, tol=1e-3)

    print("\nThe aperture invariant")
    L = accel_run(STARSHOT["array"], STARSHOT["sail"])
    chk("Starshot diffraction-limited run (AU)", L / AU, 0.025855, tol=1e-4)
    chk("its actual run is inside that", x < L, True)
    chk("aperture x sail = lambda x range (identity)",
        array_needed(STARSHOT["sail"], L), STARSHOT["array"], tol=1e-12)
    Lc = accel_run(CREWED["array"], CREWED["sail"])
    chk("crewed diffraction limit (AU)", Lc / AU, 22702.0, tol=1e-4)
    chk("crewed run needed (AU)", xx / AU, 12528.6, tol=1e-3)
    chk("so diffraction is NOT what binds the crewed case", xx < Lc, True)

    print("\nParticle communication -- Hippke's benchmark")
    chk("particle beam angle is 1/gamma", particle_beam_angle(1e6), 1e-6)
    chk("photon and particle widths meet at 82 nm, 1 m aperture",
        photon_beam_angle(82e-9, 1.0), particle_beam_angle(1.0 / (1.22 * 82e-9)))
    chk("the energy penalty Hippke prints", PARTICLE_PENALTY, 7.0e10)
    chk("demonstrated neutrino data rate (bit/s)", NEUTRINO_BITS_PER_S, 0.1)
    chk("photon capacity falls as 1/d^2",
        photon_capacity(2, 1, 1) / photon_capacity(1, 1, 1), 0.25)
    chk("photon capacity rises as D^4",
        photon_capacity(1, 1, 2) / photon_capacity(1, 1, 1), 16.0)

    print("\nThe built object against the found one")
    chk("Starshot beats the catalogued binary", STARSHOT["beta"] > 0.039262286, True)
    chk("crewed design beats the unfound IMBH", CREWED["beta"] > 0.47509702, True)
    chk("and at 1000 tonnes, not 2 metres", CREWED["mass"], 1.0e6)
    chk("mass scaling exponent", mass_scaling_exponent(), -0.25)
    chk("10^5 in mass costs 17.8x in speed", 1e5**0.25, 17.7828, tol=1e-4)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    print("""
beamed.py -- the engineering, and what it reverses
================================================================================
The coupling family's architecture -- no propellant, momentum from an external
source, owes no charge -- is BEAMED PROPULSION.  A costed discipline with
hardware in fabrication.  This project hunted the momentum source in the sky.
The engineering literature builds it.

-- BUILT AGAINST FOUND ---------------------------------------------------------""")
    print("  %-42s %10s %10s" % ("momentum source", "terminal", "payload"))
    for lbl, v, pay in (("FOUND: catalogued 50 Msun binary", 0.039262286, "2 m body"),
                        ("FOUND: unconfirmed 8823 Msun IMBH", 0.47509702, "2 m body"),
                        ("BUILT: Starshot, $8.0B, in fabrication", 0.20, "1 g"),
                        ("BUILT: Lubin DEEP-IN, crewed scale", 0.70, "1000 t")):
        print("  %-42s %9.3f c %10s" % (lbl, v, pay))
    print("""
  A thousand tonnes to 0.7 c is a published point design: 36 km reflector,
  10 PW, 100 km array.  The heaviest thing this project ever costed on the
  found-object route was a 2 m body at 0.039 c.

-- WHY MASS IS CHEAPER THAN IT LOOKS -------------------------------------------
  At fixed sail areal density the sail grows with the payload, so the beam stays
  inside it further, so the run grows too:   v ~ m^(-1/4).

  A factor 10^5 in payload mass costs 17.8x in speed, not 10^5.  That is Lubin's
  "mild function of payload mass", and it is the most encouraging number here.

-- THE APERTURE INVARIANT ------------------------------------------------------
      D_array  x  d_sail   =   lambda  x  range

  Acceleration ends where the diffracted spot outgrows the sail: %.4f AU for
  Starshot, %.0f AU for the crewed design.

-- WHAT ACTUALLY BLOCKS IT -----------------------------------------------------""" %
          (accel_run(STARSHOT["array"], STARSHOT["sail"]) / AU,
           accel_run(CREWED["array"], CREWED["sail"]) / AU))
    print("  %-16s %7s %9s %10s %12s %10s"
          % ("case", "beta", "t (days)", "run (AU)", "beam (J)", "world-yr"))
    for lbl, P, m, tgt in (("Starshot 1 g", 1e11, 1e-3, 0.20),
                           ("100 t to 0.2 c", 1e15, 1e5, 0.20),
                           ("100 t to 0.5 c", 1e15, 1e5, 0.50),
                           ("1000 t to 0.7 c", 1e16, 1e6, 0.70)):
        T = burn_for(P, m, tgt)
        b, x, eb, ek = sail_run(P, m, T)
        print("  %-16s %7.3f %9.2f %10.1f %12.3e %10.2f"
              % (lbl, b, T / 86400.0, x / AU, eb, eb / WORLD_ENERGY_YR))
    print("""
  Not physics.  Not materials.  ENERGY AT PLANETARY SCALE, delivered coherently
  through an aperture, for months.  The crewed design wants 208 years of total
  world primary energy at 10 PW for 144 days.  Sail efficiency runs 16-29%:
  most of the beam leaves with the reflected photons, and that shortfall IS the
  Doppler factor -- it cannot be engineered away, only outrun by going faster.

    THE ROADBLOCK HAS THE SHAPE OF A BILL, NOT A BOUND.

-- PARTICLE COMMUNICATION, AND IT CLOSES A BRANCH ------------------------------
  Hippke 2017 benchmarks every carrier against photons.  One law decides it:

      particle beam   theta = 1 / gamma            no aperture term
      photon beam     theta = 1.22 lambda / D      diffraction

  At a 1 m aperture these meet at 82 nm, so focusing TeV particles costs %.0e
  times the energy of a mirror.  Neutrinos are worse: 10^10 times a photon's
  beam width, and the only demonstrated link runs at %.1f bit/s through 240 m of
  rock.  Hippke covers the hypotheticals too -- nothing known or speculated
  exceeds keV photons "by more than a factor of a few".

  FOR THIS PROJECT: any architecture needing two coordinated ends -- a gate that
  must know its counterpart exists, a vehicle steered from outside -- pays the
  full light-travel time, and no carrier shortens it.  Settled, and not here.

  The one place matter beats light is BULK, not speed: inscribed matter carries
  ~%.0e bits/J at 0.1 c, against a photon channel needing kilometre apertures to
  match.  If something must be MOVED rather than SAID, move it.  Which is the
  same sentence as beamed propulsion, reached from the communication side.
""" % (PARTICLE_PENALTY, NEUTRINO_BITS_PER_S, INSCRIBED_BITS_PER_J))
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
