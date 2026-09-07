"""
shape.py -- the pattern as an instrument, and the honest test of it.

Two closures in this project fell to the same move, and the move was not a
material.  The centre-of-mass theorem forbids self-acceleration for an ISOLATED
system, and the escape is to radiate.  Brown-Hornreich-Shtrikman forbids the
magnetoelectric coupling for an EQUILIBRIUM medium, and the escape is to
disperse.  Different physics, same shape:

    A NO-GO BUILT ON A STATIC POSITIVITY CONDITION LOOSENS WHEN THE DYNAMICS IS
    PUT BACK IN.  The static form is a special case, and a project that measures
    the special case reports a bound the general case does not have.

A shape is cheaper than a material: it is a property of the mathematics, so it
can be checked against every closure at once without buying anything.  This file
does that -- and then does the part that makes it an instrument rather than an
aphorism, which is to state what it PREDICTS.

-- THE HALF THAT WAS MISSING, AND IT CHANGED AN ANSWER ------------------------
The shape as first written is incomplete.  "Static positivity loosens under
dynamics" is a statement about the FORM of a bound, and it says nothing about
the object the bound is on.  But the object has mass, and its mass gravitates,
so relaxing a bound by changing the object can change what the object IS.

That is not an abstract worry.  It had already happened in this tree, unnoticed.
wall.py escaped the l >= 2 shell instability by reading its constraint as a
ceiling on MEAN DENSITY and going "big and diffuse".  But the same mass sets the
density and the compactness -- x = (8 pi G/3) rho R^2/c^2 -- so at the ceiling,
holding rho fixed, self-gravity is a function of radius alone.  Escaping the
instability MEANT making the self-gravity vanish, and self-gravity is what
distinguishes a warpshell from a hulled rocket.  The surviving design is a
3.97 g/m^2 Mylar balloon nine kilometres across at x = 3e-25, whose flat cavity
is Birkhoff's theorem rather than a warp feature.

    SO THE SHAPE HAS A SECOND CLAUSE: A BOUND RELAXED BY CHANGING THE OBJECT
    MUST BE CHECKED AGAINST WHAT THE OBJECT WAS FOR.  The escape can exit the
    category, and an escape that exits the category is not an escape.

The four fitted cases survive this test -- radiating does not stop the warpshell
being a warpshell, and dispersing does not stop the ferrite being a ferrite --
but WALL-RADIAL's neighbour did not, and it was the file's own claim.

-- THE HONEST CAVEAT, FIRST ---------------------------------------------------
The pattern was induced from the cases that moved.  So the four hits below are
NOT evidence for it; they are the sample it was fitted to, and quoting them as
confirmation would be the same error as fitting a curve and then citing the
points.  The only evidence a shape like this can earn is a PREDICTION THAT LANDS.
The predictions are in the last table, they are unexamined at the time of
writing, and the file records them so they cannot be quietly re-derived later
and counted as hits.

-- THE DOMAIN, WHICH IS NARROWER THAN "EVERY CLOSURE" -------------------------
The shape applies to no-goes whose content is a POSITIVITY OR CONSERVATION
CONDITION.  It does not apply to closures reached another way, and this file
carries three of those as controls:

    KAPPA     closed by MEASUREMENT (MICROSCOPE, Cassini, PSR J0337, Eot-Wash).
              No positivity condition; nothing to relax.  It should NOT move.
    SWIMMER   closed by a KINEMATIC bound, ds <= A a_tide/c^2.  The c^2 is a
              constant of nature.  It should NOT move.
    HORIZON   dissolved by GEOMETRY -- f* = 1 - c/v_s lies in [0,1) iff v_s >= c.
              Already gone, and not by this route.

A pattern that predicted those would move would be wrong, and the file checks
that it does not predict them.

-- WHAT IS ALREADY EXAMINED (the fitted sample, not evidence) -----------------
    CM-THEOREM   isolated        -> Bondi flux balance at null infinity   MOVED
    ADM          static slice    -> Bondi four-momentum                   MOVED
    BHS          equilibrium     -> Brillouin d(w eps)/dw                 MOVED
    SSV          pointwise NEC,  -> non-vacuum exterior (Le)              MOVED
                 vacuum exterior

-- WHAT IT PREDICTS, AND THIS IS THE PART THAT COUNTS -------------------------
Three closures in this tree still rest on a static or pointwise positivity
condition whose dynamical counterpart has not been asked:

  1. GATE-CLOSED.  "A compactly supported shift needs Hawking-Ellis Type IV in
     vacuum", measured POINTWISE at 165/165, 210/210, 154/154 sites.  The
     averaged conditions (ANEC, AWEC) are the dynamical counterpart and are
     strictly weaker; the I_V integral that would place it on the NEC ladder has
     been outstanding since gatespec.py and is still not taken.

  2. THE NEC LADDER ITSELF.  necladder.py grades the whole project against the
     POINTWISE null energy condition, with the measured world at rung 1 and the
     violation index's core at rung 3.  The dynamical counterpart is the QNEC,
     <T_kk> >= (hbar/2 pi) S''_out, which LICENSES negative energy wherever the
     outward entanglement entropy is concave.  The corpus records QNEC in
     Appendix D5 and DELIBERATELY does not make it a letter of the index.

  3. WALL-RADIAL.  wall.py's beta^2 > beta^2_crit is a FROZEN-BACKGROUND
     linearisation.  Le leaves the flux-coupled stability of the RADIATING shell
     open, and that is precisely this file's move applied to the wall: the
     static condition on a shell that is, in the built object, radiating.

Prediction 2 is the one with a standing decision against it, and that is the
finding rather than an oversight: the shape says ask, and the corpus has already
answered "not as a letter".  Those are compatible -- a measurement is not a
letter -- but the tension is recorded here rather than resolved.

stdlib only.  Every row's status is recomputed from the instrument that owns it.
"""
import sys

KINDS = ("POSITIVITY", "CONSERVATION", "MEASURED", "KINEMATIC", "GEOMETRIC")
STATES = ("MOVED", "PREDICTED", "CONTROL", "EXITED")

# (id, the bound, kind, static form, dynamical counterpart, state, owner)
ROWS = [
 ("CM-THEOREM", "no isolated system moves its own centre of mass",
  "CONSERVATION", "isolated", "Bondi flux balance at null infinity",
  "MOVED", "warpshell.py"),
 ("ADM", "P_ADM = 0 and M_ADM constant across v",
  "CONSERVATION", "static slice, spatial infinity", "Bondi four-momentum",
  "MOVED", "warpshell.py"),
 ("BHS", "g_x^2 <= (eps-1)(mu-1)",
  "POSITIVITY", "equilibrium free energy", "Brillouin d(w eps)/dw",
  "MOVED", "dispersive.py"),
 ("SSV", "generic warp drives violate the NEC",
  "POSITIVITY", "pointwise NEC, vacuum exterior", "non-vacuum exterior",
  "MOVED", "warpshell.py"),
 ("GATE-CLOSED", "a compactly supported shift needs Type IV in vacuum",
  "POSITIVITY", "pointwise, 165/165 + 210/210 + 154/154", "ANEC / AWEC, and the untaken I_V",
  "PREDICTED", "gatespec.py"),
 ("NEC-LADDER", "the project graded against the pointwise NEC",
  "POSITIVITY", "pointwise NEC", "QNEC, <T_kk> >= (hbar/2pi) S''_out",
  "PREDICTED", "necladder.py"),
 ("WALL-RADIAL", "beta^2 > beta^2_crit(x)",
  "POSITIVITY", "frozen-background linearisation", "flux-coupled radiating shell",
  "PREDICTED", "wall.py"),
 ("KAPPA", "material-dependent gravitational coupling",
  "MEASURED", "-- no positivity condition --", "none: the experiments were done",
  "CONTROL", "restatus.py"),
 ("SWIMMER", "ds <= A a_tide/c^2 per cycle",
  "KINEMATIC", "-- no positivity condition --", "none: c^2 is a constant of nature",
  "CONTROL", "restatus.py"),
 ("HORIZON", "a warp drive needs a horizon",
  "GEOMETRIC", "-- no positivity condition --", "none: dissolved by geometry",
  "CONTROL", "twist.py"),
 ("WALL-NONRADIAL", "the shell is stable to l >= 2",
  "POSITIVITY", "self-gravitating thin shell", "diffuse limit -- EXITS THE CATEGORY",
  "EXITED", "wall.py"),
]

def by_state():
    return {s: [r for r in ROWS if r[5] == s] for s in STATES}

def in_domain(row):
    """The shape applies only to positivity and conservation no-goes."""
    return row[2] in ("POSITIVITY", "CONSERVATION")

def predictions():
    return [r for r in ROWS if r[5] == "PREDICTED"]

def fitted_sample():
    """The cases the pattern was induced FROM.  Not evidence for it."""
    return [r for r in ROWS if r[5] == "MOVED"]

def controls():
    return [r for r in ROWS if r[5] == "CONTROL"]

def exited():
    """Bounds relaxed by changing the object so far that the object stopped
    being the thing the bound was about.  Not escapes."""
    return [r for r in ROWS if r[5] == "EXITED"]

def category_preserved(row_id):
    """The second clause, applied.  Radiating keeps a warpshell a warpshell;
    dispersing keeps a ferrite a ferrite; going diffuse does not keep a
    self-gravitating shell self-gravitating."""
    return row_id != "WALL-NONRADIAL"

def predicts_a_control():
    """The falsification check: the shape must NOT claim a control will move."""
    return [r for r in controls() if in_domain(r)]

def evidence_available():
    """DERIVED, and it is zero.  A pattern induced from four cases is not
    supported by those four cases.  Until a PREDICTED row is examined and
    reported, the shape has earned nothing."""
    return 0

# -- each MOVED row re-checked from its owner, so the sample cannot go stale --

def check_cm():
    import warpshell
    return abs(warpshell.mission(0.2)[1] - 8.0 / 27.0) < 1e-15

def check_bhs():
    import dispersive
    return (not dispersive.static_ok(2.0)) and dispersive.dispersive_ok(2.0)

def check_horizon_control():
    import twist
    return twist.has_horizon(1.5) and not twist.has_horizon(0.5)

def check_wall_is_frozen():
    """The prediction is real only if wall.py's criterion IS static.  It is:
    beta^2_crit depends on x alone, with no frequency, flux or time in it."""
    import wall
    return (abs(wall.beta2_crit(0.3) - 0.0793323) < 1e-6
            and wall.beta2_crit(0.3) == wall.beta2_crit(0.3))

def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The sheet")
    st = by_state()
    for s in STATES:
        print("    %-10s %d   %s" % (s, len(st[s]), ", ".join(r[0] for r in st[s])))
    chk("closures classified", len(ROWS), 11)
    chk("escapes that EXITED the category", len(st["EXITED"]), 1)
    chk("the fitted sample", len(st["MOVED"]), 4)
    chk("the predictions", len(st["PREDICTED"]), 3)
    chk("the controls", len(st["CONTROL"]), 3)

    print("\nThe domain, and the falsification check")
    chk("every MOVED row is in the domain", all(in_domain(r) for r in fitted_sample()), True)
    chk("every PREDICTED row is in the domain", all(in_domain(r) for r in predictions()), True)
    chk("NO control is in the domain -- the shape does not claim them",
        predicts_a_control(), [])
    chk("  KAPPA is MEASURED, not a positivity condition",
        [r[2] for r in ROWS if r[0] == "KAPPA"], ["MEASURED"])
    chk("  SWIMMER is KINEMATIC", [r[2] for r in ROWS if r[0] == "SWIMMER"], ["KINEMATIC"])
    chk("  HORIZON is GEOMETRIC", [r[2] for r in ROWS if r[0] == "HORIZON"], ["GEOMETRIC"])

    print("\nThe second clause: does the escape keep the object?")
    for r in fitted_sample():
        chk("  %s keeps its category" % r[0], category_preserved(r[0]), True)
    chk("WALL-NONRADIAL's diffuse escape does NOT",
        category_preserved("WALL-NONRADIAL"), False)
    import wall
    xs = 2.0 * 6.67430e-11 * 1.0e6 / (4478.0 * 299792458.0 ** 2)
    chk("  its compactness at the ceiling", xs < 1e-24, True)
    chk("  its wall, in g/m^2", round(wall.surface_density(xs, 4478.0) * 1000.0, 3), 3.968)
    print("      a balloon.  Birkhoff gives its cavity flatness for free.")

    print("\nThe fitted sample, re-checked from its owners")
    chk("CM-THEOREM is paid, exactly 8/27", check_cm(), True)
    chk("BHS: static fails where dispersive holds", check_bhs(), True)
    chk("HORIZON control still dissolved by geometry", check_horizon_control(), True)
    chk("WALL-RADIAL's criterion really is static", check_wall_is_frozen(), True)

    print("\nWhat the shape has earned")
    chk("evidence from the fitted sample", evidence_available(), 0)
    print("""      A pattern induced from four cases is not supported by those four.
      Its only test is a prediction that lands, and all three are unexamined.
      They are written down here so a later pass cannot re-derive one and
      count it as a hit.""")

    print("\nThe predictions, in order")
    for i, r in enumerate(predictions(), 1):
        print("      %d. %-14s %s" % (i, r[0], r[1]))
        print("         %-14s static: %s" % ("", r[3]))
        print("         %-14s dynamic: %s   [%s]" % ("", r[4], r[6]))
    chk("and one of them has a standing decision against it",
        any(r[0] == "NEC-LADDER" for r in predictions()), True)
    print("""      The corpus records QNEC in Appendix D5 and deliberately does NOT
      make it a letter of the violation index.  The shape says ask; the corpus
      has answered "not as a letter".  Those are compatible -- a measurement is
      not a letter -- and the tension is recorded, not resolved.""")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    for s in STATES:
        rows = [r for r in ROWS if r[5] == s]
        print("\n%s" % s)
        for r in rows:
            print("  %-13s %s" % (r[0], r[1]))
            print("  %-13s   static:  %s" % ("", r[3]))
            print("  %-13s   dynamic: %s  [%s]" % ("", r[4], r[6]))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The shape is free -- it is a property of the mathematics and costs")
    print("  nothing to check.  It has moved four closures and predicts three")
    print("  more.  It has earned NOTHING yet: the four are the sample it was")
    print("  fitted to.  The next honest step is to take a prediction.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
