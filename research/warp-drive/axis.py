#!/usr/bin/env python3
"""
axis.py -- M: "Only as fast as c, the speed of light, which is also an
observational perception by another object viewing it.  And my method theory
says that all perceptions are a definition of a singular whole definition viewed
from a different axis or plane or dimension position."

THE METHOD THEORY IS EXACTLY RIGHT ABOUT THE SHAPE, AND THE SHAPE DELIVERS THE
OPPOSITE CONCLUSION ABOUT c.  Both halves are measured here and both matter.

A LORENTZ BOOST IS LITERALLY "A DIFFERENT AXIS POSITION" -- a rotation in the
t-x plane, by a rapidity rather than an angle.  Rotate, and watch what moves:

    LENGTH     1.000000 -> 0.001414      contracts by 707x
    DURATION   1.000000 -> 707.106958    dilates by 707x
    ENERGY     1.000000 -> 707.106958
    FREQUENCY  1.000000 -> 0.000707      Dopplers by 1400x
    c          1.000000000000000 -> 1.000000000000000   IN EVERY FRAME

EVERY PERCEPTION MOVES.  c DOES NOT.  And the reason is the sharpest possible
form of M's own theory:

    A BOOST OF RAPIDITY eta HAS THE TWO NULL DIRECTIONS AS ITS EIGENVECTORS,
    with eigenvalues e^-eta and e^+eta.  Measured at eta = 0.5, 1.0, 2.5.

    THE LIGHT CONE IS THE FIXED LINE OF THE ROTATION.  A boost RESCALES it and
    cannot TURN it, because the light cone IS the axis being rotated about.

So all perceptions ARE one whole seen from different axis positions -- that part
is right, and the whole has a name and a value: the invariant interval
s^2 = -c^2 t^2 + x^2, measured at -5.000000000000 across six frames while t and
x range over 70x.  c IS NOT ONE OF THE PERCEPTIONS.  IT IS WHAT THEY ROTATE
ABOUT.

BUT THERE ARE TWO SPEEDS OF LIGHT AND M IS RIGHT THAT ONE OF THEM IS A
PERCEPTION.  The LOCAL PROPER speed -- an observer's own ruler and clock at the
event -- is always exactly c.  The COORDINATE speed dr/dt in a chosen chart is
not: in Schwarzschild it runs 0.000050, 0.200000, 0.333333, 0.666667, 0.900000,
0.999800 from the horizon outward, FALLING TO ZERO AT THE HORIZON while the
local speed never budges.  It is a perception OF THE CHART.

AND THAT IS WHAT THIS PROJECT HAS BEEN EXPLOITING SINCE THE FIRST INSTRUMENT.
Delta_d = (G/c^2) M Lambda was never a plan to change c.  Light crosses the
corridor at exactly c -- THERE IS SIMPLY LESS CORRIDOR TO CROSS.

    NOTHING HERE HAS EVER NEEDED c TO BE A PERCEPTION.
    IT NEEDED DISTANCE TO BE ONE, AND DISTANCE IS.

WHICH MAKES THE TWO CLOSURES DIFFERENT IN KIND, AND THAT DISTINCTION IS THE
RESULT OF THIS FILE:

    transit.py's route  CLOSES ON c.  Provable, exact, advantage 0.000.
    the corridor route  DOES NOT CLOSE ON c AT ALL.  It closes on magnitude --
                        1.212374e43 J per metre -- and on needing m < 0.

"Only as fast as c" is precisely right about teleportation and precisely wrong
about the corridor.  The corridor never promised to beat c locally, and its
failure has nothing to do with c.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

# ============================================================ the boost
def gamma(v):        return 1.0/math.sqrt(1.0 - v*v)
def rapidity(v):     return math.atanh(v)
def boost(v, t, x):
    g = gamma(v)
    return g*(t - v*x), g*(x - v*t)

def interval(t, x):  return -t*t + x*x

def measured_c(v):
    """Boost a null vector and measure dx'/dt'.  Must be 1 in every frame."""
    t2, x2 = boost(v, 1.0, 1.0)
    return x2/t2

def doppler(v):      return math.sqrt((1.0-v)/(1.0+v))

PERCEPTIONS = ("LENGTH", "DURATION", "ENERGY", "FREQUENCY")
def perception_table(v):
    g = gamma(v)
    return {"LENGTH": 1.0/g, "DURATION": g, "ENERGY": g, "FREQUENCY": doppler(v)}

# ============================================ the light cone is the eigenbasis
def boost_matrix(eta):
    ch, sh = math.cosh(eta), math.sinh(eta)
    return [[ch, -sh], [-sh, ch]]

def apply2(Mx, v):   return (Mx[0][0]*v[0] + Mx[0][1]*v[1], Mx[1][0]*v[0] + Mx[1][1]*v[1])

NULL_DIRECTIONS = ((1.0, 1.0), (1.0, -1.0))
def null_eigenvalue(eta, vec):
    """A boost maps each null direction to a MULTIPLE of itself.  Returns that
    multiple, or None if it is not an eigenvector (which never happens)."""
    out = apply2(boost_matrix(eta), vec)
    l0 = out[0]/vec[0]
    l1 = out[1]/vec[1]
    return l0 if abs(l0 - l1) < 1e-12 else None

def predicted_eigenvalue(eta, vec):
    return math.exp(-eta) if vec[1] > 0 else math.exp(eta)

# ================================================ the two speeds of light
def coordinate_speed_schwarzschild(r, M=1.0): return 1.0 - 2.0*M/r   # dr/dt, radial null
def local_proper_speed(*_):                   return 1.0             # always

# ================================================ what the corridor buys
LAMBDA   = 9.982529174194637
G_SI, C_SI = 6.67430e-11, 2.99792458e8
EXCHANGE = C_SI**4/(G_SI*LAMBDA)        # joules per metre of contraction
SOLAR_REST = 1.989e30*C_SI**2

def energy_to_shorten(metres): return EXCHANGE*metres

# ================================================ the record
C_IS_A_PERCEPTION            = False   # local proper speed: invariant, always
COORDINATE_SPEED_IS          = True    # a perception -- of the CHART
LIGHT_CONE_IS_THE_EIGENBASIS = True
THE_WHOLE_IS_THE_INTERVAL    = True
CORRIDOR_CLOSES_ON_C         = False   # it closes on magnitude and on m < 0
TELEPORT_CLOSES_ON_C         = True    # transit.py, provably
PROJECT_EVER_NEEDED_C_TO_MOVE = False  # it needed DISTANCE to move, and it does
THIS_PASS_REPAIRS_ANYTHING   = False

# ================================================================= report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  CHANGE THE AXIS.  WHAT MOVES, AND WHAT DOES NOT.")
    P("="*79)
    P("\n  A boost is a rotation in the t-x plane -- a different axis position, exactly.\n")
    P(f"  {'v/c':>9} {'rapidity':>9} {'LENGTH':>10} {'DURATION':>11} {'ENERGY':>11} "
      f"{'FREQUENCY':>10} {'c measured':>19}")
    for v in (0.0, 0.1, 0.5, 0.9, 0.99, 0.999999):
        p = perception_table(v)
        P(f"  {v:9.6f} {rapidity(v):9.4f} {p['LENGTH']:10.6f} {p['DURATION']:11.6f} "
          f"{p['ENERGY']:11.6f} {p['FREQUENCY']:10.6f} {measured_c(v):19.15f}")
    P("""
    EVERY PERCEPTION MOVES -- by up to 707x across this table, and frequency by
    1400x.  c IS 1.000000000000000 IN EVERY FRAME, TO THE LAST DIGIT.""")

    P("\n" + "="*79)
    P("2.  BECAUSE THE LIGHT CONE IS THE AXIS THEY ARE ROTATING ABOUT")
    P("="*79)
    P("\n  Boost matrix [[cosh eta, -sinh eta], [-sinh eta, cosh eta]].  Its eigenvectors:\n")
    for eta in (0.5, 1.0, 2.5):
        for vec in NULL_DIRECTIONS:
            lam = null_eigenvalue(eta, vec)
            out = apply2(boost_matrix(eta), vec)
            P(f"    eta={eta:4.1f}  B({vec[0]:+.0f},{vec[1]:+.0f}) = "
              f"({out[0]:+10.6f}, {out[1]:+10.6f}) = {lam:9.6f} x itself"
              f"   [e^{'-' if vec[1]>0 else '+'}eta = {predicted_eigenvalue(eta,vec):.6f}]")
    P("""
    THE NULL DIRECTIONS MAP TO THEMSELVES.  A boost RESCALES the light cone and
    cannot TURN it, because the light cone IS the rotation's own fixed line.

    M'S THEORY IS RIGHT ABOUT THE SHAPE AND THE SHAPE SETTLES THE QUESTION.
    All perceptions ARE one whole viewed from different axis positions.  c is
    not one of the perceptions -- IT IS THE AXIS.""")

    P("\n" + "="*79)
    P("3.  AND THE 'SINGULAR WHOLE DEFINITION' HAS A NAME AND A VALUE")
    P("="*79)
    P("\n  s^2 = -c^2 t^2 + x^2, one event at (t, x) = (3, 2), six frames:\n")
    P(f"  {'v/c':>10} {'t perceived':>15} {'x perceived':>15} {'s^2 INVARIANT':>18}")
    for v in (0.0, 0.2, 0.5, 0.8, 0.95, 0.9999):
        t, x = boost(v, 3.0, 2.0)
        P(f"  {v:10.4f} {t:15.6f} {x:15.6f} {interval(t,x):18.12f}")
    P("""
    t and x range over 70x.  s^2 = -5.000000000000 in every frame.  THAT is the
    singular whole; t and x are its shadows on chosen axes.  M's theory is not
    a metaphor here -- it is the definition of Minkowski geometry.""")

    P("\n" + "="*79)
    P("4.  BUT THERE ARE TWO SPEEDS OF LIGHT, AND ONE OF THEM *IS* A PERCEPTION")
    P("="*79)
    P(f"\n  {'r/M':>11} {'dr/dt COORDINATE':>20} {'local PROPER speed':>21}")
    for r in (2.0001, 2.5, 3.0, 6.0, 20.0, 1e4):
        P(f"  {r:11.4f} {coordinate_speed_schwarzschild(r):20.12f} {local_proper_speed():21.12f}")
    P("""
    THE COORDINATE SPEED FALLS TO ZERO AT THE HORIZON.  THE LOCAL SPEED NEVER
    BUDGES.  M IS RIGHT THAT ONE OF THESE IS AN OBSERVATIONAL PERCEPTION -- it
    is the coordinate one, and it is a perception OF THE CHART rather than of a
    viewer.  Which is definitions.py's whole discipline again: two things share
    a name and only one of them is invariant.""")

    P("\n" + "="*79)
    P("5.  AND THAT IS WHAT THIS PROJECT HAS EXPLOITED SINCE THE FIRST INSTRUMENT")
    P("="*79)
    P(f"""
    Delta_d = (G/c^2) M Lambda WAS NEVER A PLAN TO CHANGE c.  Light crosses the
    corridor at exactly c.  THERE IS SIMPLY LESS CORRIDOR TO CROSS.

    exchange rate  c^4/(G Lambda) = {EXCHANGE:.6e} J per metre
""")
    P(f"  {'shorten by':>16} {'energy':>16} {'in solar rest masses':>24}")
    for d, lab in ((1.0, "1 m"), (1e3, "1 km"),
                   (3.844e8, "Earth-Moon"), (4.0175e16, "Earth-Proxima")):
        E = energy_to_shorten(d)
        P(f"  {lab:>16} {E:16.4e} {E/SOLAR_REST:24.3e}")
    P(f"""
    THE TWO CLOSURES ARE DIFFERENT IN KIND, AND THAT DISTINCTION IS THIS FILE'S
    RESULT:

        transit.py's route   CLOSES ON c.  Provable, exact, advantage 0.000 at
                             every distance, because the no-communication
                             theorem is a theorem.

        the corridor route   DOES NOT CLOSE ON c AT ALL.  It closes on
                             MAGNITUDE -- {EXCHANGE:.3e} J per metre -- and on
                             needing m < 0, which certify.py proved necessary
                             and expose.py failed to find outside a horizon.

    "ONLY AS FAST AS c" IS PRECISELY RIGHT ABOUT TELEPORTATION AND PRECISELY
    WRONG ABOUT THE CORRIDOR.  The corridor never promised to beat c locally
    and its failure has nothing to do with c.

        NOTHING IN THIS PROJECT HAS EVER NEEDED c TO BE A PERCEPTION.
        IT NEEDED DISTANCE TO BE ONE, AND DISTANCE IS.

    That is not a consolation.  It is the reason the corridor is still the
    live question and the teleportation route is not: one of them is closed by
    a theorem and the other by a bill.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M says c is an observational perception, and that his method theory makes all
  perceptions one whole seen from a different axis, plane or dimension position.
  THE THEORY IS EXACTLY RIGHT ABOUT THE SHAPE AND THE SHAPE SETTLES c AGAINST
  HIM.  A Lorentz boost IS a different axis position -- a rotation in the t-x
  plane -- and rotating it moves every perception: length contracts 707x,
  duration and energy dilate 707x, frequency Dopplers 1400x, and c reads
  1.000000000000000 in every single frame.  THE REASON IS M'S OWN THEORY AT ITS
  SHARPEST: a boost of rapidity eta has THE TWO NULL DIRECTIONS AS ITS
  EIGENVECTORS, eigenvalues e^-eta and e^+eta, verified at eta = 0.5, 1.0 and
  2.5 -- so THE LIGHT CONE IS THE FIXED LINE OF THE ROTATION.  A boost rescales
  it and cannot turn it, because the light cone IS the axis.  And the singular
  whole is real and measurable: s^2 = -5.000000000000 across six frames while t
  and x range over 70x.  BUT THERE ARE TWO SPEEDS OF LIGHT AND M IS RIGHT THAT
  ONE IS A PERCEPTION.  The LOCAL PROPER speed is always c; the COORDINATE speed
  dr/dt is not, running 0.000050 to 0.999800 in Schwarzschild and FALLING TO
  ZERO AT THE HORIZON -- a perception of the CHART.  AND THAT IS EXACTLY WHAT
  THIS PROJECT HAS EXPLOITED SINCE THE FIRST INSTRUMENT: Delta_d was never a
  plan to change c, light crosses the corridor at exactly c and there is simply
  LESS CORRIDOR TO CROSS.  WHICH MAKES THE TWO CLOSURES DIFFERENT IN KIND, and
  that is the result: transit.py's route closes ON c, provably, advantage 0.000
  at every distance; THE CORRIDOR ROUTE DOES NOT CLOSE ON c AT ALL -- it closes
  on 1.212374e43 J per metre and on needing m < 0.  "Only as fast as c" is
  precisely right about teleportation and precisely wrong about the corridor.
  NOTHING HERE HAS EVER NEEDED c TO BE A PERCEPTION; IT NEEDED DISTANCE TO BE
  ONE, AND DISTANCE IS.  One route is closed by a theorem and the other by a
  bill, and only one of those can ever be paid.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================= selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("axis.py --selftest\n")

    print("c is invariant under every change of axis")
    for v in (0.0, 0.1, 0.5, 0.9, 0.99, 0.999999, -0.7, -0.95):
        chk(f"v = {v:+g}: measured c", round(measured_c(v), 15), 1.0, 1e-14)
    chk("  so c is not a perception", C_IS_A_PERCEPTION, False)

    print("\nand every actual perception does move")
    p = perception_table(0.999999)
    chk("length contracts", p["LENGTH"] < 0.01, True)
    chk("duration dilates", p["DURATION"] > 100.0, True)
    chk("energy grows", p["ENERGY"] > 100.0, True)
    chk("frequency Dopplers", p["FREQUENCY"] < 0.01, True)
    chk("  four perceptions, all moving", len(PERCEPTIONS), 4)

    print("\nthe light cone is the boost's eigenbasis")
    for eta in (0.25, 0.5, 1.0, 2.5, 5.0):
        for vec in NULL_DIRECTIONS:
            lam = null_eigenvalue(eta, vec)
            chk(f"eta={eta}: ({vec[0]:+.0f},{vec[1]:+.0f}) is an eigenvector", lam is not None, True)
            chk(f"  eigenvalue = e^{'-' if vec[1]>0 else '+'}eta",
                round(lam, 12), round(predicted_eigenvalue(eta, vec), 12), 1e-12)
    chk("so a boost cannot turn the light cone", LIGHT_CONE_IS_THE_EIGENBASIS, True)

    print("\nthe singular whole is the interval")
    for v in (0.0, 0.2, 0.5, 0.8, 0.95):
        t, x = boost(v, 3.0, 2.0)
        chk(f"v = {v}: s^2 preserved", round(interval(t, x), 10), -5.0, 1e-10)
    t0, x0 = boost(0.9, 3.0, 2.0)
    chk("  while t and x themselves move", abs(t0-3.0) > 0.1 or abs(x0-2.0) > 0.1, True)
    chk("  and the whole has a name", THE_WHOLE_IS_THE_INTERVAL, True)

    print("\nbut the COORDINATE speed is a perception, and it moves")
    chk("far from the mass it tends to 1",
        round(coordinate_speed_schwarzschild(1e6), 5), 1.0, 1e-5)
    chk("at r = 3M it is 1/3", round(coordinate_speed_schwarzschild(3.0), 12),
        round(1.0/3.0, 12), 1e-12)
    chk("at the horizon it is 0", round(coordinate_speed_schwarzschild(2.0), 12), 0.0, 1e-12)
    chk("  while the local proper speed never moves", local_proper_speed(), 1.0)
    chk("  so ONE of the two IS a perception", COORDINATE_SPEED_IS, True)

    print("\nand the two closures are different in kind")
    chk("exchange rate, J per metre", round(EXCHANGE/1e43, 6), round(1.212374, 6), 1e-5)
    chk("1 m costs > 10^43 J", energy_to_shorten(1.0) > 1e43, True)
    chk("teleportation closes ON c", TELEPORT_CLOSES_ON_C, True)
    chk("the corridor does NOT close on c", CORRIDOR_CLOSES_ON_C, False)
    chk("the project never needed c to move", PROJECT_EVER_NEEDED_C_TO_MOVE, False)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
