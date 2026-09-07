"""
selfconsistent.py -- the sharp question, answered.  And the answer has a name.

universal.py left exactly one thing open: Type IV is realized by a quantum STATE
(the Unruh vacuum) but only as a TEST FIELD on a fixed background, and Martin-
Moruno & Visser's whole paper is about how back-reaction changes that.  So:

    DOES A TYPE IV STRESS-ENERGY EVER SOURCE ITS OWN GEOMETRY?

-- THE ANSWER: YES, TO FIRST ORDER IN hbar, AND IT IS AN EVAPORATING BLACK HOLE

Abdolrahimi, Page & Tzounis (Phys. Rev. D 100, 124038; arXiv:1607.05280) do
exactly this.  They take the Unruh-state <T_munu> and put it on the right-hand
side of the semiclassical Einstein equation, G_munu = 8 pi <T_munu>, and solve
for the metric -- an approximate time-dependent metric in ingoing Eddington-
Finkelstein coordinates for an evaporating non-rotating black hole, as a
first-order perturbation of Schwarzschild.  And then, in their own words:

    "We believe that we are the first to show that a conformally coupled
     massless scalar field in the Unruh state has a stress-energy tensor that is
     Hawking-Ellis Type IV everywhere outside the horizon of a slowly
     evaporating Schwarzschild black hole, so that there are no observers
     anywhere outside that see zero energy flux."

    SO THE OBJECTION "NOTHING KNOWN IS TYPE IV" IS FALSE.  Something known is
    Type IV, it sources a metric, and if Hawking radiation is real then it
    occurs in nature -- around every evaporating black hole there is.

-- THE PRECISION THAT MATTERS, STATED BEFORE THE CONSEQUENCE ------------------
This is FIRST ORDER IN hbar, not an exact solution.  APT compute <T> on the
UNPERTURBED Schwarzschild background and use it to source the metric
perturbation; they do not iterate to a fixed point where <T>[g] = G[g]/8 pi.
Their own phrasing is "the linearized backreaction from the stress-energy tensor
... in the unperturbed spacetime".

MMV's theorems are statements about EXACT solutions.  So there is no
contradiction in either direction: APT do not refute MMV, and MMV do not exclude
APT.  What APT establish is that the test-field/back-reaction gap -- which was
the whole of universal.py's open question -- IS CROSSED AT FIRST ORDER.

    ANSWERED AT FIRST ORDER.  STILL OPEN AT EXACT ORDER.

That is the honest scope, and it is smaller than "yes".

-- WHY MMV's THEOREMS DO NOT FORBID IT ANYWAY ---------------------------------
Their four Type-I-forced cases, against an evaporating hole:
  static?              NO -- the mass depends on retarded time, mu' = -alpha/mu^2
  Killing horizon?     NO -- an evaporating horizon is dynamical, not Killing
  circular axisym?     the flux breaks it, exactly as the warp shift does
  homogeneous?         NO
Same escape route as the warp bubble's, for the same structural reason: a
time-dependent flux is not block-diagonalisable.

-- THE MAGNITUDE, WHICH IS NOW THE LIVE QUESTION ------------------------------
APT's scaling is exact and simple: for massless fields at fixed z = 2m/r, the
orthonormal components go as mu^-4, so <T> = (1/mu_0^4) x [dimensionless], and
their flux component is closed form, f(z) = alpha z^2/(16 pi (1-z)) with
alpha = 3.7474e-5.

Against warpenergy.py's requirement rho = beta^2/(144 pi D^2) in Planck units,
at the flatness-limited wall D = R/3:

        warp bubble           needs Type IV of the strength held by
        R = 1 m,   beta=0.1   a 1.13e9 kg black hole
        R = 1 m,   beta=0.01  a 3.56e9 kg black hole
        R = 100 m, beta=0.1   a 1.13e10 kg black hole

    THOSE ARE PRIMORDIAL-BLACK-HOLE MASSES, NOT ABSURD ONES.  A billion
    kilogrammes is a mountain, and the required Type IV strength is what such an
    object carries in its Hawking flux as a matter of course.

-- WHAT THIS DOES NOT SAY, AND THE LIST IS THE POINT ---------------------------
  1. A MAGNITUDE MATCH IS NOT A CONSTRUCTION.  The black hole's Type IV is a
     spherically symmetric RADIAL flux.  The warp bubble needs Type IV in a
     TWISTED, non-circular configuration.  Same type, same strength, different
     shape, and nothing here arranges one into the other.
  2. First order in hbar, as above.
  3. Established for the conformally coupled massless SCALAR.  For spin 1 APT
     are explicit that they are "not certain" -- Type IV only for z < 0.044, and
     possibly nowhere if the disputed k_3 term vanishes.
  4. ANEC is untouched.  It is the other obstruction and it is independent.

-- AND A NOTE ON WHY THIS IS NOT THE nullbound EPISODE AGAIN ------------------
Earlier this session a headline was withdrawn because it rested on my own
inference from a scan I had not done.  This rests on a published, peer-reviewed,
back-reacting calculation with an explicit metric, and the claim being made is
narrower than the paper's.  That is a different epistemic position -- but the
scope line above is drawn deliberately tight for the same reason.

stdlib only.  Every figure is computed from APT's own closed forms.
"""
import math, sys

G = 6.67430e-11
C = 299792458.0
HBAR = 1.054571817e-34
ALPHA = 3.7474e-5                    # APT Eq (2): Hawking emission coefficient
L_PLANCK = math.sqrt(HBAR * G / C ** 3)
M_PLANCK = math.sqrt(HBAR * C / G)
RHO_PLANCK = C ** 5 / (HBAR * G * G)

def flux_component(z):
    """APT Eq (64), exact: f(z) = alpha z^2/(16 pi (1-z)), dimensionless."""
    return ALPHA * z * z / (16.0 * math.pi * (1.0 - z))

def bh_stress_planck(M_kg, z=0.5):
    """|<T>| in Planck densities.  APT: components go as mu^-4 at fixed z."""
    mu = M_kg / M_PLANCK
    return flux_component(z) / mu ** 4

def warp_stress_planck(beta, D_m):
    """warpenergy.py's rho = beta^2/(144 pi D^2), in Planck densities."""
    D = D_m / L_PLANCK
    return beta * beta / (144.0 * math.pi * D * D)

def matching_bh_mass(beta, R_m, sigma_R=3.0, z=0.5):
    """DERIVED.  The black hole whose Hawking Type IV has the strength a warp
    bubble of this size and speed requires, at the flatness-limited wall."""
    need = warp_stress_planck(beta, R_m / sigma_R)
    return M_PLANCK * (flux_component(z) / need) ** 0.25

def schwarzschild_radius(M_kg):
    return 2.0 * G * M_kg / (C * C)

def hawking_temperature(M_kg):
    return HBAR * C ** 3 / (8.0 * math.pi * G * M_kg * 1.380649e-23)

# -- MMV's four cases, against an evaporating hole ---------------------------

def evaporating_is_static():
    """mu' = -alpha/mu^2 != 0, so the mass depends on retarded time."""
    return False

def evaporating_has_killing_horizon():
    """A shrinking apparent horizon is dynamical, not Killing."""
    return False

def evaporating_is_circular():
    """A net outgoing flux breaks (t -> -t) invariance, as the warp shift does."""
    return False

def evaporating_is_homogeneous():
    return False

def escapes_mmv():
    return not (evaporating_is_static() or evaporating_has_killing_horizon()
                or evaporating_is_circular() or evaporating_is_homogeneous())

# -- scope ------------------------------------------------------------------

SCOPE = {
    "first order in hbar": True,       # T computed on the unperturbed background
    "exact self-consistent": False,    # not iterated to a fixed point
    "conformal massless scalar": True,
    "spin 1 (electromagnetic)": False, # APT: "we are not certain"
    "configuration matched": False,    # radial flux, not a twisted one
    "ANEC addressed": False,
}

def answered_at_first_order():
    return SCOPE["first order in hbar"] and not SCOPE["exact self-consistent"]

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("APT's closed forms")
    chk("f(z) = alpha z^2/(16 pi(1-z)) at z = 0.5", flux_component(0.5), 3.727608e-7, 1e-12)
    chk("  monotone increasing toward the horizon",
        all(flux_component(a) < flux_component(b)
            for a, b in zip((0.1, 0.3, 0.5, 0.7), (0.3, 0.5, 0.7, 0.9))), True)
    chk("Planck length (m)", L_PLANCK, 1.61626e-35, 1e-39)
    chk("Planck mass (kg)", M_PLANCK, 2.17643e-8, 1e-12)

    print("\nThe scaling: <T> goes as mu^-4")
    chk("doubling the mass divides |T| by 16",
        bh_stress_planck(1e9) / bh_stress_planck(2e9), 16.0, 1e-9)
    print("      %-16s %18s" % ("BH mass (kg)", "|T|/rho_Planck"))
    for M in (1e8, 1e9, 1e11, 1e15, 1.98847e30):
        print("      %-16.4g %18.4e" % (M, bh_stress_planck(M)))

    print("\nMMV's four cases, against an evaporating hole")
    chk("static?", evaporating_is_static(), False)
    chk("Killing horizon?", evaporating_has_killing_horizon(), False)
    chk("circular axisymmetric?", evaporating_is_circular(), False)
    chk("homogeneous?", evaporating_is_homogeneous(), False)
    chk("so it escapes them, as the warp bubble does", escapes_mmv(), True)

    print("\nTHE MAGNITUDE MATCH")
    print("      %-24s %16s %14s %12s"
          % ("warp bubble", "matching BH (kg)", "r_s (m)", "T_H (K)"))
    for R, b in ((1.0, 0.1), (1.0, 0.01), (100.0, 0.1)):
        M = matching_bh_mass(b, R)
        print("      R=%-6g beta=%-8g %16.4e %14.4e %12.3e"
              % (R, b, M, schwarzschild_radius(M), hawking_temperature(M)))
    chk("a 1 m, 0.1c bubble matches a 1.13e9 kg hole",
        matching_bh_mass(0.1, 1.0), 1.1263e9, 1e5)
    chk("  which is a mountain, not a star", matching_bh_mass(0.1, 1.0) < 1e12, True)
    chk("  and the match scales as R^(1/2)",
        matching_bh_mass(0.1, 100.0) / matching_bh_mass(0.1, 1.0), 10.0, 1e-9)
    chk("warp requirement is independent of R at fixed D/R",
        warp_stress_planck(0.1, 1.0 / 3.0) / warp_stress_planck(0.1, 100.0 / 3.0),
        1e4, 1e-6)

    print("\nSCOPE -- what is and is not claimed")
    for k, v in SCOPE.items():
        print("      %-28s %s" % (k, "yes" if v else "NO"))
    chk("answered at FIRST order, not exact", answered_at_first_order(), True)
    chk("  configuration is NOT matched", SCOPE["configuration matched"], False)
    chk("  spin 1 is NOT established", SCOPE["spin 1 (electromagnetic)"], False)
    import anec
    chk("  and ANEC is untouched and still violated", anec.anec_integral(0.3) < 0.0, True)

    print("\nConsistency with what came before")
    import universal, typefour
    chk("universal.py's Unruh Type IV is the same state", universal.unruh_type(0.5), "IV")
    chk("typefour.py's bubble is Type IV too", typefour.is_type_iv((0.9, 0.3, 0.0)), True)
    print("      same type, same strength available, different configuration.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE MAGNITUDE MATCH\n")
    print("  %-26s %16s %14s %12s"
          % ("warp bubble", "matching BH (kg)", "r_s (m)", "T_H (K)"))
    for R, b in ((1.0, 0.001), (1.0, 0.01), (1.0, 0.1), (10.0, 0.1), (100.0, 0.1)):
        M = matching_bh_mass(b, R)
        print("  R=%-8g beta=%-8g %16.4e %14.4e %12.3e"
              % (R, b, M, schwarzschild_radius(M), hawking_temperature(M)))
    print("\nSCOPE\n")
    for k, v in SCOPE.items():
        print("  %-30s %s" % (k, "yes" if v else "NO"))
    print("\nVERDICT")
    print("  Answered at first order in hbar: a Type IV stress-energy DOES source")
    print("  a metric, the solution is an evaporating black hole, and if Hawking")
    print("  radiation is real the configuration exists in nature.  Still open at")
    print("  exact order.  And a magnitude match is not a construction: the hole's")
    print("  Type IV is a radial flux, the bubble needs a twisted one.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
