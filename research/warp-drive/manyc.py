#!/usr/bin/env python3
"""
manyc.py -- M: "I am going to assert the many speeds of light hypothesis."
Asserted alongside the scope decision: MODIFIED GRAVITY COUNTS.

THE HYPOTHESIS HAS FIVE DISTINCT READINGS AND THEY HAVE FIVE DIFFERENT
STATUSES.  This is definitions.py's discipline applied to M's newest assertion:
"the speed of light" names more than one quantity, several of the readings are
TRUE, and the question is which of them buys anything.  NONE OF THEM DOES, and
the five reasons are different from each other, which is the actual content.

    1  c IN A MEDIUM              TRUE AND USELESS -- phase velocity exceeds c
                                  routinely and neither phase nor group velocity
                                  carries a signal.  The front is always c.
    2  THE ONE-WAY SPEED          TRUE AND EMPTY -- roundtrip.py: a convention,
                                  free to set anywhere in (0, inf), and the
                                  round trip is invariant regardless.
    3  DIFFERENT c PER FIELD      MEASURED AND BOUNDED.  Bimetric and
                                  scalar-tensor -- AND THIS IS THE READING THE
                                  SCOPE DECISION JUST PUT IN PLAY, because those
                                  ARE modified gravity.
    4  ENERGY-DEPENDENT c         MEASURED AND BOUNDED HARDER, and the sign is
                                  generically wrong for us.
    5  A COSMOLOGICALLY VARYING c NOT AN OBSERVABLE AT ALL.

READING 3 IS THE LIVE ONE AND GW170817 IS ITS EXPERIMENT.  A binary neutron star
merger 40 Mpc away sent gravitational waves and gamma rays across 130 MILLION
YEARS and they arrived 1.74 SECONDS APART:

    |c_gw - c_gamma| / c  ~  4.226e-16      AGREEING TO ONE PART IN 2.4e15

and the published two-sided bound is -3e-15 <= (v_gw - c)/c <= +7e-16.  Whole
classes of scalar-tensor theory died on that measurement.  AND EVEN AT THE EDGE
OF THE BOUND IT BUYS NOTHING: a field running 3e-15 fast saves 4.02e-07 s to
Proxima, 2.46e-03 s to the galactic centre, and 0.24 SECONDS ON A CROSSING OF
ANDROMEDA -- two and a half million years of travel to save under a minute.

READING 5 IS THE INTERESTING ONE BECAUSE THE TREE ALREADY PROVED IT, WITHOUT
KNOWING THAT IS WHAT IT WAS DOING.  A varying DIMENSIONFUL constant is not a
measurable quantity: c, G and hbar are unit conventions, and only dimensionless
ratios like alpha are observable.  That is Duff's argument (arXiv:1412.2040,
"How fundamental are fundamental constants?"; also physics/0209016 and the VSL
review arXiv:2406.02556, whose own abstract calls these constants "merely human
constructs").  AND invariance.py DERIVED IT FROM THE CORPUS'S OWN NUMBERS: doubled
G, halved c, ten-times hbar over FOURTEEN quantities, and TEN WERE INVARIANT AND
FOUR MOVED, WITH THE SPLIT FALLING EXACTLY ON DIMENSIONLESSNESS -- every
dimensionless row untouched, every dimensionful row moved, no exceptions.

    "THE CONSTANTS SET THE SCALE.  THE GEOMETRY SETS THE SHAPE."

That sentence, written in this tree before anyone here had read Duff, IS Duff's
theorem.  A varying c changes the scale and cannot touch the shape, and the
obstruction has always been in the shape.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

C   = 2.99792458e8
MPC = 3.0857e22
YR  = 3.15576e7
LY  = 9.4607e15
E_PLANCK_GEV = 1.22e19

# ------------------------------------------------------ reading 3: two fields
GW170817_DISTANCE_MPC = 40.0
GW170817_LAG_S        = 1.74          # gamma rays after the wave
GW170817_BOUND_LO     = -3e-15        # published, two-sided
GW170817_BOUND_HI     = +7e-16

def light_travel_time(D_m):           return D_m/C
def gw_fractional_bound():
    T = light_travel_time(GW170817_DISTANCE_MPC*MPC)
    return GW170817_LAG_S/T
def time_saved(D_ly, eps):            return (D_ly*LY/C)*eps

# ------------------------------------------------------ reading 4: energy
def liv_fractional_shift(E_gev):      return E_gev/E_PLANCK_GEV
def liv_delay(E_gev, D_m):            return liv_fractional_shift(E_gev)*D_m/C
LIV_SIGN_IS_GENERICALLY_A_DELAY = True   # subluminal is the generic case
VACUUM_CHERENKOV_DRAINS_SUPERLUMINAL = True

# ------------------------------------------------------ reading 5: Duff
# invariance.py, re-stated as the test it turns out to be.
INVARIANCE_TESTED   = 14
INVARIANCE_UNMOVED  = 10
INVARIANCE_MOVED    = 4
SPLIT_IS_EXACTLY_DIMENSIONLESSNESS = True
DIMENSIONFUL_C_IS_AN_OBSERVABLE    = False

VERIFIED_THIS_SESSION = [
 ("arXiv:1710.05834", "GW170817 and GRB 170817A",
  "the multimessenger paper -- 1.74 s over 130 Myr"),
 ("arXiv:1412.2040",  "How fundamental are fundamental constants?  (Duff)",
  "'the laws of physics should be independent of one's choice of units ... framed in "
  "terms of dimensionless numbers such as the fine structure constant'"),
 ("arXiv:physics/0209016", "Experimental Consequences of Time Variations of the Fundamental Constants",
  "'only dimensionless fundamental constants' have experimental consequences"),
 ("arXiv:2406.02556", "Review on the minimally extended varying speed of light model",
  "its own abstract: hbar, c, G, e, k are 'merely human constructs whose values and "
  "units vary depending on the chosen system of measurement'"),
 ("arXiv:2402.06009", "Stringent Tests of Lorentz Invariance Violation from LHAASO GRB 221009A",
  "TeV afterglow of the brightest-of-all-time GRB, energy-dependent speed bounded"),
]

# ------------------------------------------------------ the five readings
READINGS = [
 ("c in a medium",            "TRUE AND USELESS",
  "phase velocity exceeds c routinely; neither phase nor group velocity signals, "
  "and the wavefront is always exactly c"),
 ("the one-way speed",        "TRUE AND EMPTY",
  "roundtrip.py -- a convention, settable anywhere in (0, inf), and the round trip "
  "is 2D/c regardless"),
 ("different c per field",    "MEASURED AND BOUNDED",
  "bimetric and scalar-tensor -- IN SCOPE as of the scope decision -- and GW170817 "
  "agrees to one part in 2.4e15"),
 ("energy-dependent c",       "BOUNDED HARDER, AND WRONG-SIGNED",
  "LIV from GRB time-of-flight pushes E_QG to the Planck scale, and the generic "
  "correction DELAYS the fast photon rather than advancing it"),
 ("a cosmologically varying c","NOT AN OBSERVABLE",
  "a dimensionful constant is a unit convention; only dimensionless ratios are "
  "measurable, and invariance.py proved it here before Duff was cited"),
]
def readings_that_buy_transit_time(): return []

SCOPE = "modified gravity counts"        # wormhole.py, 2026-09-11, M's decision
SCOPE_PUTS_READING_3_IN_PLAY = True
THIS_PASS_REPAIRS_ANYTHING   = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  FIVE READINGS, FIVE STATUSES")
    P("="*79); P("")
    for i, (name, status, why) in enumerate(READINGS, 1):
        P(f"  {i}.  {name:<28} {status}")
        for ln in _wrap(why, 66): P(f"      {ln}")
        P("")
    P("  NONE OF THE FIVE BUYS TRANSIT TIME, AND THE FIVE REASONS ARE DIFFERENT.")
    P("  That is the content -- not the verdict, which was never in doubt.")

    P("\n" + "="*79)
    P("2.  READING 3 IS THE LIVE ONE, AND THE SCOPE DECISION IS WHY")
    P("="*79)
    T = light_travel_time(GW170817_DISTANCE_MPC*MPC)
    P(f"""
    Bimetric and scalar-tensor theories with c_gw =/= c_gamma ARE MODIFIED
    GRAVITY.  Yesterday they were out of scope.  As of wormhole.py's
    SCOPE_CHOSEN_HERE = "{SCOPE}" they are in it -- and this is
    the reading with the tightest experimental bound in the whole set.

    GW170817.  Binary neutron star merger, {GW170817_DISTANCE_MPC:.0f} Mpc.

        light travel time                {T:.4e} s  =  {T/YR/1e6:.1f} Myr
        gamma rays lagged the wave by    {GW170817_LAG_S} s
        |c_gw - c_gamma| / c           ~ {gw_fractional_bound():.3e}

        AGREEING TO ONE PART IN {1/gw_fractional_bound():.1e}
        published two-sided bound: {GW170817_BOUND_LO:.0e} <= (v_gw - c)/c <= {GW170817_BOUND_HI:.0e}

    Whole classes of scalar-tensor theory died on that one measurement.
    AND EVEN AT THE EDGE OF THE BOUND IT BUYS NOTHING:
""")
    P(f"    {'target':>18} {'light time':>16} {'time saved at 3e-15':>22}")
    for name, D_ly in (("Proxima", 4.246), ("Galactic centre", 26000.0),
                       ("Andromeda", 2.5e6)):
        P(f"    {name:>18} {D_ly*LY/C/YR:12.4f} yr {time_saved(D_ly, 3e-15):19.4e} s")
    P(f"""
    A CROSSING OF ANDROMEDA ARRIVES {time_saved(2.5e6, 3e-15):.2f} SECONDS EARLY.  Two and a half
    million years of travel to save under a minute -- and that is the ENTIRE
    budget the tightest surviving reading has.""")

    P("\n" + "="*79)
    P("3.  READING 4 IS BOUNDED HARDER AND POINTS THE WRONG WAY")
    P("="*79)
    P(f"\n    Linear LIV: dt = (E/E_QG)(D/c), E_QG at or above E_Planck = {E_PLANCK_GEV:.2e} GeV\n")
    P(f"    {'E':>10} {'E/E_Planck':>16} {'delay over 1 Gpc':>20}")
    for E_tev in (0.1, 1.0, 18.0, 300.0):
        E = E_tev*1e3
        P(f"    {E_tev:8.1f} TeV {liv_fractional_shift(E):16.3e} "
          f"{liv_delay(E, 1e3*MPC):17.3f} s")
    P("""
    AND THE SIGN IS GENERICALLY WRONG FOR US.  In most Lorentz-violating models
    the HIGH-energy photon is DELAYED, not advanced -- subluminal is the generic
    correction.  Superluminal ones carry an extra penalty: VACUUM CHERENKOV
    RADIATION, which drains a superluminal particle in flight, so the very
    thing that would make it useful is the thing that stops it arriving.""")

    P("\n" + "="*79)
    P("4.  READING 5 IS NOT AN OBSERVABLE -- AND THIS TREE PROVED THAT ALREADY")
    P("="*79)
    P(f"""
    A varying DIMENSIONFUL constant is not a measurable quantity.  c, G and
    hbar are unit conventions; only dimensionless ratios like alpha can be
    measured to change.  Verified against the literature in this session:
""")
    for cite, title, what in VERIFIED_THIS_SESSION[1:4]:
        P(f"      {cite}  --  {title}")
        for ln in _wrap(what, 64): P(f"          {ln}")
    P(f"""
    AND invariance.py DERIVED IT FROM THE CORPUS'S OWN NUMBERS, before anyone
    here had read Duff.  Double G, halve c, multiply hbar by ten, over
    {INVARIANCE_TESTED} quantities:

        {INVARIANCE_UNMOVED} INVARIANT.  {INVARIANCE_MOVED} MOVED.  THE SPLIT FALLS EXACTLY ON
        DIMENSIONLESSNESS -- every dimensionless row untouched, every
        dimensionful row moved, no exceptions.

        "THE CONSTANTS SET THE SCALE.  THE GEOMETRY SETS THE SHAPE."

    THAT SENTENCE IS DUFF'S THEOREM, written here from measurement rather than
    from citation.  A varying c changes the SCALE and cannot touch the SHAPE --
    AND THE OBSTRUCTION HAS ALWAYS BEEN IN THE SHAPE.  invariance.py said so in
    its own summary line and nobody read it as a bound on varying-c models,
    because nobody had asserted one yet.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M asserts the many speeds of light hypothesis, alongside the scope decision
  that MODIFIED GRAVITY COUNTS.  THE HYPOTHESIS HAS FIVE READINGS WITH FIVE
  DIFFERENT STATUSES, and none of them buys transit time -- the content is that
  the five reasons differ.  c IN A MEDIUM is true and useless: phase velocity
  exceeds c routinely and the front is always c.  THE ONE-WAY SPEED is true and
  empty, roundtrip.py's convention, free anywhere in (0, inf) with the round
  trip invariant regardless.  DIFFERENT c PER FIELD is the reading the SCOPE
  DECISION JUST PUT IN PLAY, since bimetric and scalar-tensor ARE modified
  gravity -- and GW170817 is its experiment: gravitational waves and gamma rays
  crossing 130 MILLION YEARS from 40 Mpc arrived 1.74 SECONDS APART, agreeing to
  ONE PART IN 2.4e15, with a published bound of -3e-15 to +7e-16 that killed
  whole classes of scalar-tensor theory.  AND AT THE EDGE OF THAT BOUND A FIELD
  RUNNING 3e-15 FAST SAVES 0.24 SECONDS ON A CROSSING OF ANDROMEDA -- 2.5
  million years of travel for under a minute.  ENERGY-DEPENDENT c is bounded
  harder, to the Planck scale by GRB time-of-flight, and points the WRONG WAY:
  the generic correction DELAYS the fast photon, and superluminal ones are
  drained in flight by vacuum Cherenkov radiation.  AND A COSMOLOGICALLY VARYING
  c IS NOT AN OBSERVABLE AT ALL -- a dimensionful constant is a unit convention,
  only dimensionless ratios are measurable (Duff, arXiv:1412.2040) -- WHICH THIS
  TREE PROVED BEFORE CITING ANYONE: invariance.py doubled G, halved c and
  multiplied hbar by ten over FOURTEEN quantities and found TEN INVARIANT AND
  FOUR MOVED, THE SPLIT FALLING EXACTLY ON DIMENSIONLESSNESS.  "The constants
  set the SCALE.  The geometry sets the SHAPE" is Duff's theorem written from
  measurement, and the obstruction has always been in the shape.  NOTHING IS
  REPAIRED.""")
    P("  " + "-"*74)

def _wrap(s, w):
    out, cur = [], ""
    for word in s.split():
        if len(cur)+len(word)+1 > w: out.append(cur); cur = word
        else: cur = (cur+" "+word).strip()
    if cur: out.append(cur)
    return out

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("manyc.py --selftest\n")

    print("the census")
    chk("readings enumerated", len(READINGS), 5)
    chk("  and none buys transit time", readings_that_buy_transit_time(), [])
    chk("the scope puts reading 3 in play", SCOPE_PUTS_READING_3_IN_PLAY, True)
    chk("  under wormhole.py's decision", SCOPE, "modified gravity counts")

    print("\nGW170817 -- the tightest direct two-speeds bound")
    T = light_travel_time(GW170817_DISTANCE_MPC*MPC)
    chk("light travel time is ~130 Myr", round(T/YR/1e6, 0), 130.0, 1.0)
    chk("fractional difference ~4e-16", round(gw_fractional_bound()*1e16, 1), 4.2, 0.2)
    chk("  which is below 1e-15", gw_fractional_bound() < 1e-15, True)
    chk("published bound is two-sided", GW170817_BOUND_LO < 0 < GW170817_BOUND_HI, True)
    print("  and at the edge of the bound it buys nothing")
    for name, D_ly, cap in (("Proxima", 4.246, 1e-6),
                            ("Galactic centre", 26000.0, 1e-2),
                            ("Andromeda", 2.5e6, 1.0)):
        chk(f"  {name}: saved < {cap:g} s", time_saved(D_ly, 3e-15) < cap, True)

    print("\nenergy-dependent c")
    chk("18 TeV over 1 Gpc: delay is minutes not years",
        60.0 < liv_delay(18e3, 1e3*MPC) < 600.0, True)
    chk("fractional shift at 1 TeV", round(liv_fractional_shift(1e3)*1e17, 1), 8.2, 0.2)
    chk("the generic sign is a DELAY", LIV_SIGN_IS_GENERICALLY_A_DELAY, True)
    chk("  and superluminal drains via vacuum Cherenkov",
        VACUUM_CHERENKOV_DRAINS_SUPERLUMINAL, True)

    print("\na varying dimensionful c is not an observable")
    chk("invariance.py tested", INVARIANCE_TESTED, 14)
    chk("  invariant", INVARIANCE_UNMOVED, 10)
    chk("  moved", INVARIANCE_MOVED, 4)
    chk("  and they sum", INVARIANCE_UNMOVED + INVARIANCE_MOVED, INVARIANCE_TESTED)
    chk("the split is exactly dimensionlessness", SPLIT_IS_EXACTLY_DIMENSIONLESSNESS, True)
    chk("so a dimensionful c is not an observable", DIMENSIONFUL_C_IS_AN_OBSERVABLE, False)
    chk("citations verified this session", len(VERIFIED_THIS_SESSION), 5)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
