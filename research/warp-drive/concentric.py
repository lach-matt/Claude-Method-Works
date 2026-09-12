#!/usr/bin/env python3
"""
concentric.py -- the two-region device, with M_ADM = 0 and a vacuum corridor.

The last structural item.  composite.py showed a negative mass can seat a
congruence AND lead, because Weyl focusing is quadratic in the source while the
Shapiro delay is linear.  But a BARE negative mass violates the positive mass
theorem, and a result that needs one is not a device.  This file builds the
two-region version M asked about and measures it.

-- WITHDRAWN: THE LEAD MEASURED HERE IS INTERIOR-ONLY -------------------------

    READ THIS BEFORE QUOTING ANY LEAD FROM THIS FILE.

Every ray below runs x0 = -150 to +150 with the shell at R_s = 200, so BOTH
ENDPOINTS SIT INSIDE THE SHELL.  In there the metric is not asymptotically
flat, and "t - |dx|" compares a coordinate time against a coordinate distance
in a region where neither is the asymptotic one.  It is not a statement about
causal structure.  Move the endpoints out past R_s and THE SIGN REVERSES:

        X = 150 (inside)   -1.785e-01   early     <-- what this file reports
        X = 210 (outside)  -9.635e-02   early
        X = 260 (outside)  -2.532e-02   early
        X = 280 (outside)  +3.117e-03   LATE
        X = 1000 (outside) +1.026e+00   LATE

The reason is the one composite.py already wrote down and nobody applied here:
M_ADM = 0 makes the Shapiro gain CONVERGE (constant to five digits over three
decades of baseline) while the deflection the shell does NOT cancel -- a ray at
b << R_s passes wholly inside, where a shell has no field, and exits nearly
radially, where a radial field cannot bend it back -- costs path length
LINEARLY.  Bounded gain, unbounded loss, crossover at X_c ~ 250.

    THE LEAD SURVIVES ONLY AS A BOUNDED, SHORT-RANGE CLAIM: 200 < X < 277.
    IT IS WITHDRAWN AS A GLOBAL ONE.

Nothing else in this file moves.  The conjugate point, M_ADM = 0, the vacuum
corridor and the shell's ordinariness are all unaffected -- they are not
statements about arrival time.  See chronology.py, which measured this.

-- THE CONSTRUCTION -----------------------------------------------------------
A compact NEGATIVE core inside a POSITIVE shell of the same magnitude:

        Phi(r)  =  m / sqrt(r^2 + a^2)  -  m / max(r, R_s)

  first term    a Plummer-smoothed core of mass -m  (Phi > 0: it advances)
  second term   a thin shell of mass +m at R_s      (Phi < 0: it delays)

    THE MONOPOLES CANCEL, SO M_ADM = 0 EXACTLY and the positive mass theorem's
    INEQUALITY is satisfied.  Measured: Phi(1000) = -6.2e-13, against
    Phi(1) = +4.4e-3.  (Its RIGIDITY clause is not, and cannot be -- see
    pair.py: M_ADM = 0 with the DEC would force Minkowski, so the DEC fails
    here of necessity.)

And the division of labour is Newton's, not an assumption:

    THE SHELL DELAYS BUT DOES NOT FOCUS.  Inside a spherical shell the
    potential is constant, so it contributes to g_tt -- a real delay for a
    clock inside relative to infinity -- and NOTHING to the tidal field.  All
    the focusing comes from the core, through Weyl, sign-blind.

So the budget is explicit: the core's advance minus the shell's delay, against
the core's focusing alone.

-- IT WORKS, AND THE POSITIVE MASS THEOREM TURNS OUT TO BE NEARLY FREE --------
At b = 1, a = 0.02, R_s = 200, a run of 300 from x = -150 (n = 2500):

        m         f = b^2/4m   conjugate    t - |dx|      relative   verdict
        1.0e-3    250.0        none         -1.921e-2     -6.4e-5    leads, no seat
        3.0e-3     83.3        none         -5.404e-2     -1.8e-4    leads, no seat
        5.0e-3     50.0        228.5        -8.424e-2     -2.8e-4    *** SEATS + LEADS ***
        1.0e-2     25.0        182.2        -1.405e-1     -4.7e-4    *** SEATS + LEADS ***
        2.0e-2     12.5        165.4        -1.785e-1     -6.0e-4    *** SEATS + LEADS ***
        4.0e-2      6.2        158.0        -7.690e-3     -2.6e-5    *** SEATS + LEADS ***
        8.0e-2      3.1        154.4        +1.036e+0     +3.5e-3    seats, LATE

    THE DEVICE SEATS AND LEADS WITH M_ADM = 0 EXACTLY, over a window from
    5e-3 to 4e-2 -- most of a decade, no narrower than composite.py's bare
    negative mass.  Converged: the conjugate point sits at 228.45 +- 0.04 over
    n = 1500 to 9000, a sixfold refinement, and the delay to five figures.

    AND THE BEST RELATIVE LEAD, -6.0e-4 at m = 2e-2, is if anything slightly
    BETTER than the bare mass's ~5e-4.  Respecting the positive mass theorem
    costs almost nothing here, and the reason is a design rule rather than luck:

        shell delay / core advance  ~  (L / R_s) / (2 ln(L/a))

    The core's advance carries a logarithm of its compactness and the shell's
    delay does not, so PUT THE SHELL FAR AND MAKE THE CORE SMALL.  At these
    numbers the ratio is about 8 %, which is what "nearly free" means.

-- THREE ERRORS MADE BUILDING THIS, ALL KEPT AS TESTS -------------------------
 1. THE FIRST POTENTIAL WAS NOT ZERO-ADM AT ALL.  I wrote  m/sqrt(r^2+a^2) -
    m/R_s  with the constant applied EVERYWHERE, which is a bare negative
    monopole plus an offset -- ADM mass -m, exactly the thing the shell was
    meant to fix.  The fix is max(r, R_s).  The measured numbers survived
    because the ray never left r < 150 < R_s, but the CLAIM did not.
 2. THE FIRST CORRIDOR WAS NOT VACUUM.  With a = 0.5 and b = 1 the ray runs
    inside the Plummer core's own negative density: the tidal matrix's trace
    was 40 % of its largest component, so R_kk was large and negative -- Ricci
    DEFOCUSING, fighting the Weyl term, in a corridor advertised as empty.
    Compactness fixes it, and the approach to vacuum is clean:

        a       b/a     |trace| / |max component|
        0.50      2     3.99e-1        <- not vacuum
        0.10     10     1.97e-2
        0.02     50     7.55e-4        <- the configuration used

    THE CORRIDOR IS VACUUM ONLY IF THE CORE IS COMPACT AGAINST THE IMPACT
    PARAMETER, and b/a >~ 50 is what it takes.  A design constraint, not a
    numerical detail.
 3. AND THE FIRST WINDOW WAS MEASURED WITH A BROKEN HARNESS.  The scratch
    driver's run() reset the potential to its own a = 0.5, R_s = 30 defaults on
    entry, so every "a = 0.02" scratch run silently used a = 0.5.  It reported
    a window five times narrower and a relative lead two orders smaller, and an
    earlier draft of this header stated both as findings.  WITHDRAWN: the
    numbers above are this file's own, stable over a sixfold refinement.
    The disagreement between harness and instrument is what surfaced it, which
    is the argument for running the instrument rather than the sketch.

-- WHAT IS NOT CLAIMED --------------------------------------------------------
 1. NEGATIVE MASS IS STILL ASSUMED.  M_ADM = 0 removes the positive-mass-
    theorem objection to the CONFIGURATION; it does not make the core's matter
    less exotic.  Its local energy density is negative and that is unchanged.

    *** SUPERSEDED BY pair.py: IT IS NOT ASSUMED, IT IS DERIVED. ***
    The positive mass theorem has a second half this file read only the first
    of.  RIGIDITY: M_ADM = 0 under the dominant energy condition implies the
    spacetime IS MINKOWSKI.  This one is not -- it seats a conjugate point and
    has structure at every radius -- so its matter CANNOT satisfy the DEC.  The
    negative energy density is forced by the design's own M_ADM = 0, by a
    theorem, with no appeal to any magnitude.  What follows below stands
    unchanged; only the word ASSUMED does not.
    AND NARROWED BY apply.py: M_ADM is a FREE PARAMETER here -- letting the
    shell mass float free of the core's still seats and still leads at
    M_ADM > 0, while a POSITIVE core seats and arrives LATE.  So the exotic
    matter belongs to THE LEAD, locally, and rigidity is a second proof of it
    rather than its source.
 2. LINEARISED WEAK FIELD, as composite.py.  Phi_max ~ m/a = 0.25 at the
    design point, which is NOT small.  The window's edges are INDICATIVE and a
    strong-field treatment could move them.  This is the weakest point here.
 3. THE FOCUS IS ASTIGMATIC, as composite.py: a line focus, enough to break
    achronality, not a point-to-point image.
 4. NO PAYLOAD.  Null-geodesic optics throughout.
 5. NO STABILITY ANALYSIS.  A negative core inside a positive shell is a
    configuration nobody has shown to hold together, and wall.py's history in
    this project is a warning about assuming it would.

stdlib only.  composite.py supplies the geodesic, Riemann and Jacobi-matrix
machinery, validated there against 4M/b, the traceless condition and the
analytic Shapiro.
"""
import math, sys

A_CORE = 0.02
R_SHELL = 200.0
B_RAY = 1.0
X0 = -150.0
LAM = 300.0
NSTEP = 2500


def potential(m, a=A_CORE, Rs=R_SHELL):
    """Phi(r) = m/sqrt(r^2+a^2) - m/max(r,R_s).  Monopoles cancel: M_ADM = 0."""
    def f(p, _M=None):
        r = math.sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2])
        return m / math.sqrt(r * r + a * a) - m / max(r, Rs)
    return f


def _install(m, a=A_CORE, Rs=R_SHELL):
    import composite
    composite.phi = potential(m, a, Rs)
    return composite


def adm_residual(m, a=A_CORE, Rs=R_SHELL, r=1000.0):
    """Phi far away.  Zero ADM mass means this tends to zero, not to a 1/r tail."""
    return potential(m, a, Rs)((r, 0.0, 0.0))


def trace_ratio(m, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """|trace| / |largest component| of the tidal matrix at closest approach.
    Vacuum forces the trace to zero, so this measures how empty the corridor is."""
    cp = _install(m, a, Rs)
    T = cp.tidal((0.0, b, 0.0), [1.0, 1.0, 0.0, 0.0],
                 [0., 0., 1., 0.], [0., 0., 0., 1.], m)
    return abs(T[0][0] + T[1][1]) / max(abs(T[0][0]), abs(T[1][1]))


def survey(m, b=B_RAY, a=A_CORE, Rs=R_SHELL, x0=X0, lam=LAM, n=NSTEP):
    """One corridor ray: does it seat, and does it lead?"""
    cp = _install(m, a, Rs)
    p0 = (x0, b, 0.0)
    k0 = cp.null_tangent(p0, m)
    pts, tang, h = cp.geodesic(p0, k0, m, lam, n)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]
    A = [[0.0, 0.0], [0.0, 0.0]]
    dA = [[1.0, 0.0], [0.0, 1.0]]
    conj, rmax = None, 0.0
    for i in range(len(pts) - 1):
        x = pts[i]
        k = list(tang[i])
        p = (x[1], x[2], x[3])
        rmax = max(rmax, math.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2))
        T = cp.tidal(p, k, e1, e2, m)
        acc = [[-sum(T[r][s] * A[s][c] for s in range(2)) for c in range(2)]
               for r in range(2)]
        for r in range(2):
            for c in range(2):
                A[r][c] += h * dA[r][c] + 0.5 * h * h * acc[r][c]
                dA[r][c] += h * acc[r][c]
        if i > 5 and conj is None and (A[0][0] * A[1][1] - A[0][1] * A[1][0]) <= 0.0:
            conj = i * h
        G = cp.christoffel(p, m)
        for e in (e1, e2):
            de = [-sum(G[q][al][be] * k[al] * e[be]
                       for al in range(4) for be in range(4)) for q in range(4)]
            for q in range(4):
                e[q] += h * de[q]
    a0, b0 = pts[0], pts[-1]
    dt = b0[0] - a0[0]
    dx = math.sqrt(sum((b0[j] - a0[j]) ** 2 for j in (1, 2, 3)))
    return {"m": m, "conjugate": conj, "seats": conj is not None,
            "delay": dt - dx, "leads": (dt - dx) < 0.0,
            "max_r": rmax, "inside_shell": rmax < Rs,
            "relative": (dt - dx) / dt}


LEAD_IS_INTERIOR_ONLY = True     # see the withdrawal at the top of this file
LEAD_WINDOW = (200.0, 277.0)     # (R_s, measured crossover): outside this, LATE


def lead_is_global():
    """Does the measured lead hold at any baseline?  NO -- withdrawn.

    Kept as an executable assertion so the retraction cannot be walked past by
    someone reading only the numbers below.
    """
    return not LEAD_IS_INTERIOR_ONLY


def works(m, **kw):
    r = survey(m, **kw)
    return r["seats"] and r["leads"] and r["inside_shell"]


def selftest():
    ok = True
    print("WITHDRAWAL -- the lead below is INTERIOR-ONLY; see the file header")
    print("  lead_is_global() = %s   window = %s" % (lead_is_global(), LEAD_WINDOW))
    assert lead_is_global() is False, "the retraction must not be silently reversed"


    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-58s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("M_ADM = 0 -- the monopoles cancel, so the far field dies")
    near("Phi at r = 1 (the corridor)", potential(5e-3)((1.0, 0, 0)), 4.9750e-3, 1e-6)
    chk("Phi at r = 1000 is negligible against it",
        abs(adm_residual(5e-3)) < 1e-10, True)
    print("       Phi(1000) = %+.4e.  No 1/r tail, so no ADM mass, so the"
          % adm_residual(5e-3))
    print("       positive mass theorem's INEQUALITY has nothing to object to.")
    print("       Its RIGIDITY clause does, and productively: M_ADM = 0 under")
    print("       the DEC forces Minkowski, so the DEC must fail here.  pair.py")
    # error 1, kept as a test: the constant applied EVERYWHERE is a bare monopole
    bad = lambda r: 5e-3 / math.sqrt(r * r + A_CORE ** 2) - 5e-3 / R_SHELL
    chk("the FIRST potential I wrote had a bare negative monopole",
        abs(bad(1000.0)) > 1e-6, True)
    print("       bad(1000) = %+.4e -- a -m ADM mass, the very thing the shell"
          % bad(1000.0))
    print("       was there to cancel.  The fix is max(r, R_s).")

    print("\nThe corridor is vacuum only if the core is COMPACT")
    print("     %8s %8s %16s" % ("a", "b/a", "|trace|/|max|"))
    ratios = []
    for a in (0.5, 0.1, 0.02):
        tr = trace_ratio(5e-3, a=a)
        ratios.append(tr)
        print("     %8.2f %8.0f %16.3e" % (a, B_RAY / a, tr))
    chk("at a = 0.5 the corridor is NOT vacuum", ratios[0] > 0.1, True)
    chk("at a = 0.02 it is, to better than a tenth of a percent",
        ratios[2] < 1e-3, True)
    chk("and it improves monotonically with compactness",
        ratios[0] > ratios[1] > ratios[2], True)

    print("\nTHE DEVICE -- does it seat and lead, with M_ADM = 0?")
    print("     %8s %10s %12s %14s %11s %s"
          % ("m", "f=b^2/4m", "conjugate", "t-|dx|", "relative", "verdict"))
    rows = {}
    for m in (3.0e-3, 5.0e-3, 2.0e-2, 8.0e-2):
        r = survey(m)
        rows[m] = r
        print("     %8.1e %10.1f %12s %+14.4e %11.2e %s"
              % (m, B_RAY ** 2 / (4 * m),
                 ("%.1f" % r["conjugate"]) if r["seats"] else "none",
                 r["delay"], r["relative"],
                 "*** SEATS + LEADS ***" if (r["seats"] and r["leads"])
                 else "seats, LATE" if r["seats"] else "leads, no seat"))
    chk("below the window: leads but does not seat",
        (rows[3e-3]["seats"], rows[3e-3]["leads"]), (False, True))
    chk("IN the window: SEATS AND LEADS", works(5.0e-3), True)
    chk("still in it an order of magnitude up", works(2.0e-2), True)
    chk("above it: seats, but the delay wins",
        (rows[8e-2]["seats"], rows[8e-2]["leads"]), (True, False))
    chk("and the ray stays inside the shell throughout",
        all(r["inside_shell"] for r in rows.values()), True)
    near("the conjugate point at m = 5e-3", rows[5e-3]["conjugate"], 228.45, 0.3)

    print("\nThe positive mass theorem turns out to be NEARLY FREE")
    best = abs(rows[2e-2]["relative"])
    near("best relative lead, at m = 2e-2", best / 5.96e-4, 1.0, 0.05)
    chk("which is no worse than composite.py's bare mass (~5e-4)",
        best > 4.0e-4, True)
    ratio = (LAM / R_SHELL) / (2.0 * math.log(LAM / A_CORE))
    near("shell delay / core advance ~ (L/R_s)/(2 ln(L/a))", ratio, 0.0781, 1e-3)
    chk("under 10 %, because the core's advance carries a logarithm and the "
        "shell's delay does not", ratio < 0.1, True)
    print("       DESIGN RULE: put the shell far and make the core small.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE DEVICE   core -m (a=%.2f) inside shell +m (R=%.0f), M_ADM = 0"
          % (A_CORE, R_SHELL))
    print("  %8s %10s %12s %14s %10s %s"
          % ("m", "f=b^2/4m", "conjugate", "t-|dx|", "rel", "verdict"))
    for m in (3e-3, 4e-3, 5e-3, 6e-3, 7e-3, 1e-2):
        r = survey(m)
        print("  %8.1e %10.1f %12s %+14.4e %10.2e %s"
              % (m, B_RAY ** 2 / (4 * m),
                 ("%.1f" % r["conjugate"]) if r["seats"] else "none",
                 r["delay"], r["relative"],
                 "*** SEATS + LEADS ***" if (r["seats"] and r["leads"])
                 else "seats, late" if r["seats"] else "leads, no seat"))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The two-region device seats and leads with M_ADM = 0 EXACTLY, so")
    print("  the positive mass theorem's INEQUALITY has no objection to the")
    print("  configuration -- and its RIGIDITY clause then DERIVES the exotic")
    print("  matter this file had only assumed.  See pair.py.")
    print("  The corridor is genuinely vacuum -- traceless to 7.5e-4 -- which")
    print("  needs the core compact against the impact parameter, b/a >~ 50.")
    print("  The shell delays without focusing, by Newton's shell theorem, so")
    print("  all the focusing is the core's Weyl term.")
    print("\n  AND IT IS NEARLY FREE: the window runs 5e-3 to 4e-2, most of a")
    print("  decade, and the best relative lead -6.0e-4 is no worse than a bare")
    print("  negative mass. The shell delay is only ~8 % of the core advance,")
    print("  because the core's advance carries ln(L/a) and the shell's does")
    print("  not. Put the shell far and make the core small.")
    print("\n  Negative mass is still assumed, the field is linearised with")
    print("  Phi_max ~ 0.25 which is NOT small, the focus is astigmatic, there")
    print("  is no payload, and NOTHING here shows the configuration is stable.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
