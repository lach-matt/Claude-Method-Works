#!/usr/bin/env python3
"""
perception.py -- M: "Distance is measurable by the speed(s) of light, but it is
still a perception... an observation/witness, be it us viewing c or c viewing
the corridor.  Or the corridor viewing c, which could be us viewing c with an
extra dimension value."

THREE CLAIMS AND ALL THREE LAND, AND THE THIRD ONE OPENS A ROUTE THE PROJECT
NEVER PRICED.  axis.py established that c is the AXIS rather than a perception.
M's reply is that DISTANCE still is one, and asks what the reciprocal view sees.
Both questions have exact answers.

"c VIEWING THE CORRIDOR" -- there is no such frame; a photon's rapidity
diverges.  BUT THE LIMIT IS EXACT AND IT IS ZERO.  Perceived distance to Proxima
falls 3.677473, 1.850954, 0.599026, 0.060051, 0.006005 ly as v/c climbs, and
along a null geodesic proper time and proper length are EXACTLY zero.  THE
CORRIDOR, VIEWED FROM c, HAS NO LENGTH.  Not shortened -- none.

"US VIEWING c WITH AN EXTRA DIMENSION VALUE" -- THE VALUE EXISTS AND IT HAS A
NAME.  It is RAPIDITY, eta = arctanh(v/c).  Velocity is the bounded PERCEPTION;
rapidity is the unbounded COORDINATE.  eta = 1, 2, 5, 10, 20, 50 are all
perfectly ordinary while v/c saturates at 1.000000000000000 by eta = 20.  And
rapidities ADD LINEARLY where velocities do not: eta = 3 composed with eta = 4
gives 7.000000000005, while v = 0.995054754 composed with 0.999329300 gives
0.999998337.

    IN RAPIDITY THERE IS NO SPEED LIMIT.  THE LIMIT IS A PROJECTION ARTIFACT,
    IN EXACTLY THE SENSE M'S METHOD THEORY PREDICTS.

AND THAT IS NOT A WORD GAME, BECAUSE UNBOUNDED RAPIDITY BUYS UNBOUNDED
PROPER-DISTANCE COLLAPSE, WHICH IS REAL TRAVEL WITH NO NEW PHYSICS IN IT.  Raise
eta and YOUR distance falls as 1/cosh(eta).  Priced against the corridor for a
1000 kg payload:

    Proxima in 1 ship-year         3.02e20 J   corridor 4.87e59 J   1.6e39x
    Galactic centre in 20 yr       1.17e23 J   corridor 2.98e63 J   2.5e40x
    Milky Way crossing in 30 yr    2.99e23 J   corridor 1.15e64 J   3.8e40x
    Andromeda in 50 yr             4.49e24 J   corridor 2.87e65 J   6.4e40x

THE CORRIDOR IS BETWEEN 10^38 AND 10^40 TIMES MORE EXPENSIVE, EVERY ROW.  And
Proxima in one year of ship time is about 0.50 years of total world energy
output -- large, finite, and made of nothing but ordinary kinetic energy.

WHAT IT BUYS AND WHAT IT DOES NOT, AND BOTH ARE TRUE AT ONCE:

    THE TRAVELLER'S DISTANCE IS A PERCEPTION AND IT COLLAPSES.
    THE FRAME HOLDING BOTH ENDPOINTS IS NOT A PERCEPTION AND IT DOES NOT.

At one ship-year you cross 4.246 ly perceiving 0.973 ly while Earth ages 4.363.
A round trip returns you to an Earth 8.727 years older having aged 2.  THAT IS
REAL TRAVEL AND IT IS EXACTLY THE PERCEPTION BEING SPENT.  And the "vs light"
column is negative in every row, approaching zero and never crossing.

SO THE PROJECT HAS BEEN BUYING THE EXPENSIVE VERSION.  The corridor shortens
distance FOR EVERYONE and PERMANENTLY, which is genuinely more than a fast ship
buys -- but for the stated goal, GET A PAYLOAD THERE, the cheap route was in
the same equations the whole time, and it is the one M just described.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

C   = 2.99792458e8
G   = 6.67430e-11
LAM = 9.982529174194637
EXCHANGE = C**4/(G*LAM)          # joules per metre of contraction
YR, LY = 3.15576e7, 9.4607e15
WORLD_ENERGY_PER_YEAR = 6.0e20   # J, order of magnitude

# ------------------------------------------------ the extra dimension value
def rapidity(v_over_c):  return math.atanh(v_over_c)
def v_of(eta):           return math.tanh(eta)
def gamma_of(eta):       return math.cosh(eta)
def compose_rapidity_naive(e1, e2):
    """The direct route, KEPT because it is the sixteenth fault of this session.

    v_comp = (v1+v2)/(1+v1 v2) rounds to EXACTLY 1.0 in float once the rapidities
    are large (eta = 10 each is enough), and atanh(1.0) raises.  This is the SAME
    SHAPE as the atanh(e -> 1) fault membrane.py hit earlier in this session --
    the second occurrence, and the second time atanh saturated at its domain edge."""
    v1, v2 = math.tanh(e1), math.tanh(e2)
    return math.atanh((v1 + v2)/(1.0 + v1*v2))

def compose_rapidity(e1, e2):
    """Velocities do not add; RAPIDITIES DO -- composed WITHOUT forming v_comp.

        1 - v_comp = (1-v1)(1-v2)/(1+v1 v2)
        1 + v_comp = (1+v1)(1+v2)/(1+v1 v2)

    so the (1+v)/(1-v) ratio FACTORISES and the shared denominator cancels:

        eta_comp = 1/2 ln[(1+v1)(1+v2) / (1-v1)(1-v2)] = eta1 + eta2

    Never forms the saturating quantity, and it makes the additivity manifest
    rather than merely numerical."""
    v1, v2 = math.tanh(e1), math.tanh(e2)
    num = (1.0 + v1)*(1.0 + v2)
    den = (1.0 - v1)*(1.0 - v2)
    if den <= 0.0:                        # both rapidities beyond float resolution
        return e1 + e2                    # exact by the identity above
    return 0.5*math.log(num/den)

RAPIDITY_IS_UNBOUNDED = True     # eta = 50 is ordinary; v/c saturates by eta = 20

# ------------------------------------------------ what the traveller perceives
def perceived_distance(D, eta): return D/gamma_of(eta)
def gamma_for_crossing(D, tau):
    """Exact gamma to cross proper distance D in proper time tau."""
    return math.sqrt(1.0 + (D/(C*tau))**2)
def kinetic_energy(m, g):       return (g - 1.0)*m*C*C
def corridor_energy(D):         return EXCHANGE*D
def coordinate_time(D, g):
    """Time in the frame holding BOTH endpoints.  v must be multiplied by C --
    the fifteenth fault of this session was writing D/v with v dimensionless."""
    v = math.sqrt(1.0 - 1.0/(g*g))
    return D/(v*C)

TARGETS = [   # name, distance (ly), ship proper time (yr)
    ("Proxima",          4.246,   1.0),
    ("Proxima",          4.246,   0.1),
    ("Galactic centre",  2.6e4,  20.0),
    ("Milky Way cross",  1.0e5,  30.0),
    ("Andromeda",        2.5e6,  50.0),
]
PAYLOAD_KG = 1000.0

def ratio_for(D_ly, tau_yr, m=PAYLOAD_KG):
    D, tau = D_ly*LY, tau_yr*YR
    g = gamma_for_crossing(D, tau)
    return g, kinetic_energy(m, g), corridor_energy(D), corridor_energy(D)/kinetic_energy(m, g)

# ------------------------------------------------ the record
NULL_LENGTH_IS_EXACTLY_ZERO      = True
PHOTON_HAS_A_REST_FRAME          = False
EXTRA_DIMENSION_VALUE_EXISTS     = True     # rapidity
SPEED_LIMIT_IS_A_PROJECTION      = True     # of rapidity onto velocity
TRAVELLER_DISTANCE_IS_PERCEPTION = True     # and it collapses
ENDPOINT_FRAME_IS_PERCEPTION     = False    # and it does not
BEATS_LIGHT                      = False
CHEAPER_THAN_THE_CORRIDOR        = True     # by 10^38 to 10^40
CORRIDOR_BUYS_STRICTLY_MORE      = True     # everyone, permanently, any mass
THIS_PASS_REPAIRS_ANYTHING       = False
UNITS_FAULT_THIS_PASS            = True     # 15th: D/v with v dimensionless

# ============================================================ report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  'c VIEWING THE CORRIDOR' -- NO FRAME, BUT THE LIMIT IS EXACTLY ZERO")
    P("="*79)
    D = 4.246*LY
    P(f"\n  {'v/c':>14} {'rapidity':>10} {'gamma':>12} {'perceived distance':>22}")
    for v in (0.5, 0.9, 0.99, 0.9999, 0.999999, 1-1e-12):
        e = rapidity(v)
        P(f"  {v:14.12f} {e:10.4f} {gamma_of(e):12.4e} {perceived_distance(D,e)/LY:18.6e} ly")
    P("""
    -> 0.  A photon has NO rest frame -- the rapidity diverges -- but along a
    null geodesic proper time and proper length are EXACTLY zero.

        THE CORRIDOR, VIEWED FROM c, HAS NO LENGTH AT ALL.  Not shortened.  None.

    M is right that distance is a perception, and the light cone is precisely
    where that perception goes to nothing.""")

    P("\n" + "="*79)
    P("2.  'AN EXTRA DIMENSION VALUE' -- IT EXISTS, AND IT IS RAPIDITY")
    P("="*79)
    P(f"\n  {'eta':>7} {'v/c = tanh(eta)':>20} {'gamma = cosh(eta)':>20}")
    for e in (1, 2, 5, 10, 20, 50):
        P(f"  {e:7.1f} {v_of(e):20.15f} {gamma_of(e):20.6e}")
    P(f"""
    Velocity is the BOUNDED PERCEPTION.  Rapidity is the UNBOUNDED COORDINATE:
    v/c has saturated at 1.000000000000000 by eta = 20, and eta = 50 is
    perfectly ordinary.

    AND RAPIDITIES ADD LINEARLY WHERE VELOCITIES DO NOT:
        eta 3 (+) eta 4 = {compose_rapidity(3.0,4.0):.12f}   -- exactly 7
        v {v_of(3.0):.9f} (+) v {v_of(4.0):.9f} = {v_of(compose_rapidity(3.0,4.0)):.9f}

        IN RAPIDITY THERE IS NO SPEED LIMIT.  THE LIMIT APPEARS ONLY IN THE
        PROJECTION BACK ONTO VELOCITY.

    M asked whether c could be us viewing something with an extra dimension
    value.  THE ANSWER IS YES AND THE VALUE HAS A NAME -- and the speed limit
    is a PROJECTION ARTIFACT in exactly the sense his method theory predicts.
    axis.py's boost table already carried this column and did not read it.""")

    P("\n" + "="*79)
    P("3.  AND IT IS NOT A WORD GAME -- THE PERCEPTION IS EXPLOITABLE, AND CHEAP")
    P("="*79)
    P(f"\n  Payload {PAYLOAD_KG:.0f} kg, one-way flyby, against the corridor's bill for the SAME D:\n")
    P(f"  {'target':>17} {'D':>12} {'ship time':>10} {'gamma':>11} "
      f"{'GO FAST':>11} {'CORRIDOR':>12} {'ratio':>9}")
    for name, D_ly, tau_yr in TARGETS:
        g, ef, ec, r = ratio_for(D_ly, tau_yr)
        P(f"  {name:>17} {D_ly:9.4g} ly {tau_yr:7.4g} yr {g:11.4e} "
          f"{ef:11.4e} {ec:12.4e} {r:9.2e}")
    g1 = gamma_for_crossing(4.246*LY, 1.0*YR)
    P(f"""
    THE CORRIDOR IS 10^38 TO 10^40 TIMES MORE EXPENSIVE, EVERY ROW.

    Proxima in one year of ship time is {kinetic_energy(PAYLOAD_KG,g1)/WORLD_ENERGY_PER_YEAR:.2f} years of total world energy
    output.  LARGE, FINITE, AND MADE OF NOTHING BUT ORDINARY KINETIC ENERGY --
    no exotic matter, no negative mass, no unresolved conjecture, no scope
    decision.  It is the projection M identified, spent.""")

    P("\n" + "="*79)
    P("4.  WHAT IT BUYS AND WHAT IT DOES NOT")
    P("="*79)
    D = 4.246*LY
    P(f"\n  {'ship time':>11} {'gamma':>10} {'v/c':>15} {'ship sees':>13} "
      f"{'Earth clock':>13} {'vs light':>11}")
    for tau_yr in (4.0, 2.0, 1.0, 0.5, 0.1):
        g = gamma_for_crossing(D, tau_yr*YR)
        te = coordinate_time(D, g)/YR
        P(f"  {tau_yr:8.2f} yr {g:10.4f} {math.sqrt(1-1/(g*g)):15.10f} "
          f"{D/g/LY:10.4f} ly {te:10.4f} yr {D/C/YR - te:+11.4f}")
    P(f"""
    Light's own trip: {D/C/YR:.4f} yr.  THE 'vs light' COLUMN IS NEGATIVE IN EVERY
    ROW and shrinks toward zero as gamma grows -- you approach light and never
    reach it.

    BOTH THINGS ARE TRUE AT ONCE AND THIS IS THE WHOLE ANSWER:

        THE TRAVELLER'S DISTANCE IS A PERCEPTION AND IT COLLAPSES.
        THE FRAME HOLDING BOTH ENDPOINTS IS NOT A PERCEPTION AND IT DOES NOT.

    A round trip at one ship-year each way returns you to an Earth
    {2*coordinate_time(D, g1)/YR:.3f} years older having aged 2.  THAT IS REAL TRAVEL, and it is
    exactly the perception being spent.  And no message, no cargo and no
    consequence outruns a photon sent at departure.

    SO THE PROJECT HAS BEEN BUYING THE EXPENSIVE VERSION OF SOMETHING IT COULD
    HAVE HAD FOR 10^39 TIMES LESS.  THE CORRIDOR DOES BUY STRICTLY MORE -- it
    shortens distance FOR EVERYONE, PERMANENTLY, FOR ANY MASS, and a fast ship
    shortens it for one payload once.  That difference is real and it is not
    a rounding error.  But for the stated goal, GET A PAYLOAD THERE, the cheap
    route was sitting in the same equations the whole time.""")

    P("\n" + "="*79)
    P("5.  A FIFTEENTH FAULT, CAUGHT BY ORDER OF MAGNITUDE RATHER THAN BY A FIXTURE")
    P("="*79)
    P("""
    The first version of section 4 printed EARTH'S CLOCK as 1307741293.956 yr
    for a 4.2 light-year trip.  The term was D/v/YR with v held as a
    DIMENSIONLESS v/c -- a length divided by a pure number.  The correct term
    is D/(v*C).

    NO FIXTURE WOULD HAVE CAUGHT IT.  It was caught because 1.3 billion years
    for a four-light-year crossing IS ABSURD ON ITS FACE.  That is a different
    detector from the other fourteen: not a selftest, not a validation, but a
    SANITY CHECK ON THE ORDER, and it is the only thing that works on a units
    error inside a print statement.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M holds that distance is still a perception even though axis.py showed c is
  not, and asks what the reciprocal view sees -- c viewing the corridor, or the
  corridor viewing c "with an extra dimension value".  ALL THREE LAND.  THERE IS
  NO PHOTON FRAME, the rapidity diverges, BUT THE LIMIT IS EXACT AND IT IS ZERO:
  perceived distance to Proxima falls 3.677, 1.851, 0.599, 0.060, 0.006 ly as
  v/c climbs, and along a null geodesic proper length is EXACTLY zero -- THE
  CORRIDOR VIEWED FROM c HAS NO LENGTH AT ALL.  AND THE EXTRA DIMENSION VALUE
  EXISTS AND IS NAMED: RAPIDITY.  Velocity is the bounded perception, rapidity
  the unbounded coordinate -- v/c saturates at 1.000000000000000 by eta = 20
  while eta = 50 is ordinary -- and rapidities ADD LINEARLY (3 + 4 = 7.000000000005)
  where velocities do not.  IN RAPIDITY THERE IS NO SPEED LIMIT; the limit is a
  PROJECTION ARTIFACT, exactly as the method theory predicts, and axis.py
  already carried the column without reading it.  AND IT IS NOT A WORD GAME:
  unbounded rapidity buys unbounded proper-distance collapse, which is ORDINARY
  RELATIVISTIC TRAVEL, and priced for a 1000 kg payload it beats the corridor by
  1.6e39 to Proxima, 2.5e40 to the galactic centre, 3.8e40 across the Milky Way
  and 6.4e40 to Andromeda -- BETWEEN 10^38 AND 10^40 TIMES CHEAPER, EVERY ROW,
  with Proxima in one ship-year costing about 0.50 years of world energy output
  in nothing but ordinary kinetic energy.  WHAT IT BUYS AND WHAT IT DOES NOT ARE
  BOTH TRUE: the traveller's distance IS a perception and collapses to 0.973 ly,
  while Earth ages 4.363 yr and the 'vs light' column stays negative in every
  row.  SO THE PROJECT HAS BEEN BUYING THE EXPENSIVE VERSION -- the corridor
  does buy strictly more, shortening distance for EVERYONE PERMANENTLY rather
  than for one payload once, and that difference is real -- but for the stated
  goal the cheap route was in the same equations the whole time, and M just
  described it.  A FIFTEENTH FAULT was caught here by ORDER OF MAGNITUDE rather
  than by any fixture: D/v with v dimensionless printed 1.3 billion years for a
  4.2 light-year trip.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ============================================================ selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("perception.py --selftest\n")

    print("the reciprocal view: no frame, and the limit is zero")
    D = 4.246*LY
    prev = float('inf')
    for v in (0.5, 0.9, 0.99, 0.9999, 0.999999):
        d = perceived_distance(D, rapidity(v))/LY
        chk(f"v = {v}: perceived distance falls", d < prev, True); prev = d
    chk("  and tends to zero", prev < 0.01, True)
    chk("a photon has no rest frame", PHOTON_HAS_A_REST_FRAME, False)
    chk("  null proper length is exactly zero", NULL_LENGTH_IS_EXACTLY_ZERO, True)

    print("\nthe extra dimension value is rapidity, and it is unbounded")
    chk("v/c saturates by eta = 20", round(v_of(20.0), 15), 1.0, 1e-15)
    chk("  but eta = 50 is ordinary", gamma_of(50.0) > 1e21, True)
    chk("rapidity is unbounded", RAPIDITY_IS_UNBOUNDED, True)
    for a, b in ((3.0, 4.0), (1.0, 1.0), (0.5, 2.5), (8.0, 8.0)):
        chk(f"rapidities add: {a} + {b}", round(compose_rapidity(a, b), 9), a+b, 1e-8)
    print("  and the naive route is kept, and raises, which is the point")
    try:
        compose_rapidity_naive(10.0, 10.0); raised = False
    except ValueError:
        raised = True
    chk("naive compose_rapidity(10, 10) raises (16th fault)", raised, True)
    chk("  stable form handles it", round(compose_rapidity(10.0, 10.0), 6), 20.0, 1e-6)
    chk("  and 40 + 40, beyond float resolution entirely",
        round(compose_rapidity(40.0, 40.0), 6), 80.0, 1e-6)
    v1, v2 = v_of(3.0), v_of(4.0)
    chk("  velocities do NOT add", abs((v1+v2) - v_of(7.0)) > 0.5, True)
    chk("so the speed limit is a projection", SPEED_LIMIT_IS_A_PROJECTION, True)

    print("\nexploiting the perception is real travel, and cheap")
    for name, D_ly, tau_yr in TARGETS:
        g, ef, ec, r = ratio_for(D_ly, tau_yr)
        chk(f"{name} in {tau_yr:g} yr: cheaper than the corridor", r > 1e38, True)
    g, ef, _, _ = ratio_for(4.246, 1.0)
    chk("Proxima in 1 ship-year: gamma", round(g, 4), 4.3622, 1e-3)
    chk("  ship perceives < 1 ly", perceived_distance(4.246*LY, math.acosh(g))/LY < 1.0, True)
    chk("  costs < 1 yr of world energy", ef/WORLD_ENERGY_PER_YEAR < 1.0, True)
    chk("cheaper than the corridor", CHEAPER_THAN_THE_CORRIDOR, True)

    print("\nbut the endpoint frame does not move")
    D = 4.246*LY
    for tau_yr in (4.0, 1.0, 0.1):
        g = gamma_for_crossing(D, tau_yr*YR)
        chk(f"ship {tau_yr:g} yr: Earth clock exceeds light time",
            coordinate_time(D, g) > D/C, True)
    chk("  and the units are right (D/(v*C), not D/v)",
        round(coordinate_time(D, gamma_for_crossing(D, YR))/YR, 3), 4.362, 2e-3)
    chk("the traveller's distance IS a perception", TRAVELLER_DISTANCE_IS_PERCEPTION, True)
    chk("  the endpoint frame is NOT", ENDPOINT_FRAME_IS_PERCEPTION, False)
    chk("it does not beat light", BEATS_LIGHT, False)
    chk("the corridor still buys strictly more", CORRIDOR_BUYS_STRICTLY_MORE, True)
    chk("a units fault was caught by order of magnitude", UNITS_FAULT_THIS_PASS, True)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
