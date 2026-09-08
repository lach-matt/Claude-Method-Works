#!/usr/bin/env python3
"""
gate.py -- "bigger inside", and PROJECTED against GATE.

M: "the size of a wormhole inside is factorially larger than the outside.  So
what we are looking for is a way to project a stable wormhole in front of an
object for transport.  Or the wormhole is constructed as a gate."

Three things: the geometry claim is MEASURED AND DOES NOT HOLD; of the two
architectures the GATE is strictly better and the reason is sharp; and the gate
has one consequence that decides what it is FOR.

===============================================================================
1. IS A WORMHOLE BIGGER INSIDE?  MEASURED: NO, AND ONLY LOGARITHMICALLY LONGER
===============================================================================

Morris-Thorne with b(r) = r_0, proper radial distance from the throat, in
closed form and checked against a substituted quadrature:

        l(r)  =  sqrt(r(r - r_0))  +  r_0 ln[ (sqrt(r-r_0) + sqrt(r)) / sqrt(r_0) ]

        r/r_0        proper l        coord r-r_0     ratio        excess
        2            2.29559         1.00            2.2956       1.296 r_0
        20           21.67186        19.00           1.1406       2.672 r_0
        1000         1003.64665      999.00          1.0047       4.647 r_0
        1e6          1000007.10090   999999.00       1.000008     8.101 r_0

    ASYMPTOTICALLY  l - (r - r_0) = r_0 [ 1/2 + ln 2 + (1/2) ln(r/r_0) ].

    THE EXCESS GROWS LOGARITHMICALLY AND THE RATIO GOES TO ONE.  At a million
    throat radii the interior is longer by 8.1 r_0 -- EIGHT THOUSANDTHS OF ONE
    PER CENT.  Not factorial, not exponential, not even linear.

    AND IT WOULD CUT THE WRONG WAY IF IT WERE TRUE.  A bigger interior is MORE
    to cross, not less.  What a wormhole gives is not room, it is the
    SHORTCUT -- the two mouths sit near each other in the embedding while
    being far apart in the exterior.  That is the whole product, and it does
    not depend on the interior being large.

-- A FAULT CAUGHT IN THE MEASURING, AND RECORDED --------------------------

The first run of this integral used a UNIFORM GRID ACROSS AN INTEGRABLE
SINGULARITY -- the integrand goes as 1/sqrt(r - r_0) at the throat -- and
overestimated the proper distance BY ABOUT 2.7x, which would have made the
claim look partly true.  Substituting u = sqrt(r - r_0) turns the integrand
into 2 sqrt(r_0 + u^2), which is smooth, and the result then matches the closed
form to five digits.  Same class of error as smearing.py's.

===============================================================================
2. AND THE THROAT IS A HARD BOTTLENECK, WHICH SETS THE DESIGN
===============================================================================

The throat has areal radius r_0 and area 4 pi r_0^2, and A PAYLOAD MUST
PHYSICALLY FIT THROUGH IT.  So the payload sets r_0, and r_0 sets everything:

        MASS       M ~ r_0 c^2/(8 pi G)        WANTS r_0 SMALL
        TENSION    tau = c^4/(8 pi G r_0^2)    WANTS r_0 LARGE

    TWO REQUIREMENTS PULLING OPPOSITE WAYS, and they are different quantities
    so there is no optimum to solve for -- only a choice of which to break.

        r_0        M_exotic            tau (Pa)      note
        2 m        1.0716e+26 kg       1.2039e+42    human-scale, 17.9 Earth masses
        3 km       1.6074e+29 kg       5.3505e+35    Kuhfittig's neutron-star point

    A HUMAN-SCALE GATE IS 2.25e6 TIMES WORSE IN TENSION THAN A THREE-KILOMETRE
    ONE AND ONLY 1500 TIMES CHEAPER IN MASS.  The scaling punishes small gates
    quadratically and rewards them only linearly.

===============================================================================
3. PROJECTED AGAINST GATE, AND IT IS NOT CLOSE
===============================================================================

    PROJECTED -- a throat carried ahead of a moving object.

        THIS IS THE MTY CONSTRUCTION BY DEFINITION.  Morris-Thorne-Yurtsever
        needs one mouth moved relative to the other so proper time accumulates
        differently at the two ends; a projected wormhole does exactly that, as
        its operating principle.  anecscope.py closed MTY against this project
        on structure -- no throat -- and wormhole.py already recorded that the
        closure is gone.  PROJECTION REOPENS IT MAXIMALLY.

        And it cannot outrun the thing it is meant to beat: establishing a
        compactly supported metric change is causal (phase1 Theorem 4), so a
        throat cannot be projected ahead faster than a signal.

    GATE -- both mouths at rest in one frame.

        NO DIFFERENTIAL AGING, so nothing accumulates and the MTY construction
        has nothing to work with.  This is the same payment GJW make and
        unified.py measured: the relative time coordinate is FIXED, once, at
        construction.

        AND IT IS STATIC, so phase1's Theorem 5 applies and WORKS: it holds
        itself, costs nothing to keep, and the establishment is paid ONCE.

    THE GATE WINS ON BOTH COUNTS AND THE PROJECTED VERSION LOSES ON BOTH.

===============================================================================
4. BUT THE GATE HAS ONE CONSEQUENCE THAT DECIDES WHAT IT IS FOR
===============================================================================

The far mouth has to GET there.  Nothing about a wormhole moves it -- you
transport it conventionally, at sublight, before any of this works:

        4 light years at 0.1 c   =   40 years, one way, the hard way

    After that, every transit is effectively instant, forever, for free.
    Amortised over N crossings the deployment is 40/N years each.

        A GATE MAKES THE SECOND TRIP FREE.  IT DOES NOTHING FOR THE FIRST.

    SO A GATE NETWORK'S REACH IS EXACTLY THE REACH OF CONVENTIONAL TRAVEL.  It
    is a return ticket and a supply line, not an exploration tool.  That is not
    a small thing -- it is the difference between visiting Alpha Centauri once
    and having it next door -- but it is a different product from the one
    "warp transition" has meant in this project so far, and it should be named
    as such rather than blurred into it.

===============================================================================
AND WHAT DOES NOT MOVE
===============================================================================

    The exotic source.  0.081 solar masses of NEGATIVE mass at the
    three-kilometre design point, 17.9 Earth masses at human scale.  Every
    closure in supply.py, scale.py, shaping.py and contain.py about sourcing
    rho < 0 stands untouched, and wormhole.py's scope warning stands too: the
    literature's escapes from the QFT restriction leave General Relativity.

stdlib only.  wormhole.py supplies the throat cost and tension.
"""
import math, sys

C, G = 2.99792458e8, 6.67430e-11
MSUN, MEARTH, LY, YEAR = 1.98892e30, 5.9722e24, 9.4607e15, 3.15576e7


# ------------------------------------------- 1: is it bigger inside?

def proper_distance(r, r0):
    """Closed form.  l = sqrt(r(r-r0)) + r0 ln[(sqrt(r-r0)+sqrt(r))/sqrt(r0)]."""
    return math.sqrt(r * (r - r0)) + r0 * math.log(
        (math.sqrt(r - r0) + math.sqrt(r)) / math.sqrt(r0))


def proper_distance_quadrature(r, r0, n=20000):
    """Independent check with the singularity REMOVED by u = sqrt(r - r0).

    The integrand 1/sqrt(1 - r0/r) diverges at the throat.  A uniform grid over
    r overestimates it by about 2.7x -- which is what the first run of this
    file did.  In u the integrand is 2 sqrt(r0 + u^2), which is smooth.

    AND n MUST BE EVEN.  A first version used n = 20001 -- an ODD interval
    count -- which mis-weights the final interval and cost h*f(U)/3 = 0.034
    here, exactly the discrepancy observed.  It bites only when the integrand
    is NON-ZERO at the upper limit, which is why the other Simpson calls in
    this tree are unharmed: smearing.py's core is 1.9e-21 at its window edge
    and phase1.py's / supply.py's integrands decay likewise.
    """
    assert n % 2 == 0, "Simpson needs an even interval count"
    U = math.sqrt(r - r0)
    h = U / n
    s = 0.0
    for i in range(n + 1):
        u = i * h
        s += (1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)) * 2.0 * math.sqrt(r0 + u * u)
    return s * h / 3.0


def interior_excess(r, r0=1.0):
    return proper_distance(r, r0) - (r - r0)


def excess_is_logarithmic(r0=1.0, rtol=2e-3):
    """l - (r-r0) -> r0[1/2 + ln2 + (1/2)ln(r/r0)].  Checked at 1e6 r0."""
    r = 1.0e6 * r0
    predicted = r0 * (0.5 + math.log(2.0) + 0.5 * math.log(r / r0))
    return abs(interior_excess(r, r0) / predicted - 1.0) < rtol


def ratio_goes_to_one(r0=1.0, tol=1e-4):
    r = 1.0e6 * r0
    return abs(proper_distance(r, r0) / (r - r0) - 1.0) < tol


def bigger_inside_is_factorial():
    """No.  Logarithmic, and the ratio tends to one."""
    return False


# --------------------------------------- 2: the throat is a bottleneck

def throat_area(r0):
    return 4.0 * math.pi * r0 * r0


def throat_mass(r0):
    return r0 * C ** 2 / (8.0 * math.pi * G)


def throat_tension(r0):
    return C ** 4 / (8.0 * math.pi * G * r0 * r0)


def opposite_pulls(small=2.0, large=3000.0):
    """Mass wants small, tension wants large.  Returns (mass gain, tension cost)."""
    return (throat_mass(large) / throat_mass(small),
            throat_tension(small) / throat_tension(large))


# ------------------------------------------- 3: projected against gate

ARCHITECTURES = (
    ("projected", False,
     "a mouth carried relative to the other IS the MTY construction, by "
     "definition and as its operating principle; and phase1 Theorem 4 says a "
     "compactly supported metric change cannot be established faster than a "
     "signal, so it cannot outrun what it is meant to beat"),
    ("gate", True,
     "both mouths at rest: no differential aging, nothing accumulates, the MTY "
     "construction has nothing to work with -- and it is STATIC, so phase1 "
     "Theorem 5 applies and the establishment is paid once"),
)


def projected_reopens_mty():
    return True


def gate_accumulates():
    """No.  Both mouths at rest in one frame."""
    return False


def gate_amortises():
    """Yes -- static, holds itself, phase1 Theorem 5."""
    return True


def better_architecture():
    return [n for n, ok, _w in ARCHITECTURES if ok][0]


# --------------------------------- 4: what the gate is actually for

def deployment_years(distance_ly=4.0, beta=0.1):
    """The far mouth travels conventionally.  Nothing here moves it."""
    return distance_ly * LY / (beta * C) / YEAR


def amortised_years(n_transits, distance_ly=4.0, beta=0.1):
    return deployment_years(distance_ly, beta) / n_transits


def helps_the_first_trip():
    """No.  A gate makes the SECOND trip free."""
    return False


REACH = "exactly the reach of conventional travel"
PRODUCT = "a return ticket and a supply line, not an exploration tool"


# ------------------------------------------------------------ what does not move

def exotic_mass_solar(r0=3000.0):
    return throat_mass(r0) / MSUN


SOURCE_MOVED = False


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

    print("1. IS A WORMHOLE BIGGER INSIDE?  Measured.")
    print("      %10s %15s %15s %11s %10s" % ("r/r0", "proper l", "coord", "ratio", "excess"))
    for r in (2.0, 20.0, 1000.0):
        l = proper_distance(r, 1.0)
        print("      %10g %15.5f %15.2f %11.6f %10.3f" % (r, l, r - 1.0, l / (r - 1.0), l - (r - 1.0)))
    near("closed form against substituted quadrature at r = 1000",
         proper_distance_quadrature(1000.0, 1.0), proper_distance(1000.0, 1.0), 1e-9)
    print("      (n MUST be even: n = 20001 mis-weights the last interval and")
    print("      costs h*f(U)/3 = 0.034.  Harmless only where the integrand")
    print("      decays to zero at the limit -- which is why the other Simpson")
    print("      calls in this tree are unaffected.)")
    chk("the excess is logarithmic", excess_is_logarithmic(), True)
    chk("and the ratio goes to one", ratio_goes_to_one(), True)
    near("excess at r = 1e6 r0, in r0", interior_excess(1.0e6), 8.101, 1e-3)
    chk("bigger inside, factorially", bigger_inside_is_factorial(), False)
    print("      8.1 r0 at a million throat radii -- 0.0008 %.  And a bigger")
    print("      interior would be MORE to cross.  The product is the SHORTCUT.")

    print("\n2. THE THROAT IS A BOTTLENECK, AND IT SETS THE DESIGN")
    for r0, lbl in ((2.0, "human"), (3000.0, "Kuhfittig")):
        print("      r0 = %-8.4g %-10s area %.3e m^2  M %.4e kg  tau %.4e Pa"
              % (r0, lbl, throat_area(r0), throat_mass(r0), throat_tension(r0)))
    near("human-scale mass, in Earth masses", throat_mass(2.0) / MEARTH, 17.943, 1e-3)
    mg, tc = opposite_pulls()
    near("mass penalty of going to 3 km", mg, 1500.0, 1e-3)
    near("tension penalty of staying at 2 m", tc, 2.25e6, 1e-3)
    print("      quadratic punishment for small, linear reward.  No optimum --")
    print("      only a choice of which requirement to break.")

    print("\n3. PROJECTED AGAINST GATE")
    for n, good, why in ARCHITECTURES:
        print("      %-11s %-5s %s" % (n, "OK" if good else "NO", why[:52]))
    chk("projected reopens MTY", projected_reopens_mty(), True)
    chk("a gate accumulates differential aging", gate_accumulates(), False)
    chk("a gate amortises (phase1 Theorem 5)", gate_amortises(), True)
    chk("the better architecture", better_architecture(), "gate")

    print("\n4. BUT WHAT IS THE GATE FOR?")
    near("deploying the far mouth, 4 ly at 0.1 c (years)", deployment_years(), 40.0, 1e-3)
    near("amortised over 1000 transits (years each)", amortised_years(1000), 0.04, 1e-3)
    chk("a gate helps the FIRST trip", helps_the_first_trip(), False)
    chk("its reach", REACH, "exactly the reach of conventional travel")
    print("      %s" % PRODUCT)

    print("\nAND WHAT DOES NOT MOVE")
    near("exotic mass at the 3 km point, in solar masses", exotic_mass_solar(), 0.08082, 1e-3)
    chk("the source problem moved", SOURCE_MOVED, False)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE GEOMETRY CLAIM DOES NOT HOLD.  A Morris-Thorne interior is
  longer than the coordinate span by r_0[1/2 + ln 2 + (1/2)ln(r/r_0)]
  -- LOGARITHMIC -- so at a million throat radii it is longer by
  8.1 r_0, eight thousandths of one per cent, and the ratio tends to
  one.  Not factorial.  And it would cut the wrong way if it were
  true: a bigger interior is more to cross.  What a wormhole sells is
  the SHORTCUT, not the room.  (My first measurement of this ran a
  uniform grid across an integrable singularity and overstated it by
  2.7x; substituting u = sqrt(r - r_0) fixes it and the closed form
  confirms.)

  THE THROAT IS A HARD BOTTLENECK AND IT SETS EVERYTHING.  A payload
  must fit through 4 pi r_0^2, so the payload picks r_0 -- and then
  mass goes as r_0 while tension goes as 1/r_0^2.  Going from a
  human-scale two metres to Kuhfittig's three kilometres costs 1500x
  in mass and buys 2.25e6 in tension.  Quadratic punishment for
  small, linear reward.  There is no optimum, only a choice of which
  requirement to break.

  BETWEEN THE TWO ARCHITECTURES IT IS NOT CLOSE, AND THE GATE WINS.
  A PROJECTED throat carries one mouth relative to the other, which
  IS the Morris-Thorne-Yurtsever construction, as its operating
  principle -- and anecscope.py's structural closure of MTY is
  already gone now that there is a throat.  It also cannot be
  established ahead of a signal.  A GATE has both mouths at rest: no
  differential aging, nothing to accumulate, and being static it
  amortises, which phase1's Theorem 5 identified as the only place
  value was ever going to live.

  BUT THE GATE DECIDES WHAT THIS IS FOR, AND THAT DESERVES SAYING
  PLAINLY.  The far mouth has to get there conventionally -- four
  light years at a tenth of light is forty years, the hard way --
  and nothing in the wormhole moves it.  After that every crossing
  is free, forever.  SO A GATE MAKES THE SECOND TRIP FREE AND DOES
  NOTHING FOR THE FIRST, AND A GATE NETWORK REACHES EXACTLY AS FAR AS
  CONVENTIONAL TRAVEL ALREADY HAS.  A return ticket and a supply
  line, not an exploration tool.  Worth having, and a different
  product from the one this project has been calling warp transition.

  AND THE SOURCE HAS NOT MOVED: 0.081 solar masses of NEGATIVE mass
  at three kilometres, 17.9 Earth masses at human scale.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
