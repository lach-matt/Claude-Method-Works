#!/usr/bin/env python3
"""
concentric.py -- the two-region device, with M_ADM = 0 and a vacuum corridor.

The last structural item.  composite.py showed a negative mass can seat a
congruence AND lead, because vacuum Weyl focusing is sign-blind -- the vacuum
tidal matrix is traceless, so a congruence focuses at the first-order
astigmatic focal length b^2/4|m| for either sign -- while the Shapiro delay
flips sign with m.  But a BARE negative mass violates the dominant energy
condition, so it lies outside the positive mass theorem (which does not forbid
it), and a result that needs one is not a device.  This file builds the
two-region version M asked about and measures it.
    CORRECTED (DOCKET 67).  (a) This said "Weyl focusing is quadratic in the
    source": Weyl's effect on AREA is second order, but the conjugate point is
    set by the first-order focal length this file prints (f = b^2/4m).  (b) It
    said a bare negative mass "violates the positive mass theorem": a static
    constant-negative-density ball is complete, regular and asymptotically
    flat with E_ADM < 0; it violates the DEC, and the theorem does not forbid it.

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

Nothing else in this file moves.  The conjugate point, M_ADM = 0 (exact for
the metric as written; see below), the vacuum corridor and the shell's
ordinariness are all unaffected -- they are not statements about arrival time.  See chronology.py, which measured this.

-- THE CONSTRUCTION -----------------------------------------------------------
A compact NEGATIVE core inside a POSITIVE shell of the same magnitude:

        Phi(r)  =  m / sqrt(r^2 + a^2)  -  m / max(r, R_s)

  first term    a Plummer-smoothed core of mass -m  (Phi > 0: it advances)
  second term   a thin shell of mass +m at R_s      (Phi < 0: it delays)

    THE MONOPOLES CANCEL, SO M_ADM = 0 EXACTLY FOR THE METRIC AS WRITTEN
    (g - delta = m a^2/r^3, no 1/r term) and the positive mass theorem's
    INEQUALITY is satisfied -- true and vacuous, since the theorem assumes the
    DEC, which this core violates; it could object to no configuration here,
    a bare negative mass included.  Measured at m = 5e-3: Phi(1000) =
    -1.0e-15, against Phi(1) = +4.974e-3.  (Its RIGIDITY clause is not, and
    cannot be -- see pair.py: M_ADM = 0 with the DEC would force a flat slice,
    so the DEC fails here of necessity.)
    CORRECTED (DOCKET 67).  (a) The pair first printed here, -6.2e-13 and
    +4.4e-3, are the values at a = 0.5, the broken harness's a (error 3).
    (b) "Exactly" holds at the metric level.  Reading the metric as "a core of
    -m plus a shell of +m" identifies M_ADM with the sum of linear source
    monopoles, true only to first order in m/a; a Newtonian post-linear
    estimate of the binding term is -0.074 m at m = 5e-3 and -0.29 m at
    m = 2e-2.

And the division of labour is Newton's, not an assumption:

    THE SHELL DELAYS BUT DOES NOT FOCUS.  Inside a spherical shell the
    potential is constant, so it contributes to g_tt -- a real delay for a
    clock inside relative to infinity -- and NOTHING to the tidal field.  All
    the focusing comes from the core, through Weyl, sign-blind.

So the budget is explicit: the core's advance minus the shell's delay, against
the core's focusing alone.

-- IT WORKS, AND THE POSITIVE MASS THEOREM COSTS ~13 % OF THE ADVANCE ---------
    (CORRECTED (DOCKET 67): this heading read "TURNS OUT TO BE NEARLY FREE",
    resting on the design-rule ratio below as first written, 7.8 %.)
At b = 1, a = 0.02, R_s = 200, a run of 300 from x = -150 (n = 2500):

        m         f = b^2/4m   conjugate    t - |dx|      relative   verdict
        1.0e-3    250.0        none         -1.921e-2     -6.4e-5    leads, no seat
        3.0e-3     83.3        none         -5.404e-2     -1.8e-4    leads, no seat
        5.0e-3     50.0        228.6        -8.424e-2     -2.8e-4    *** SEATS + LEADS ***
        1.0e-2     25.0        182.3        -1.405e-1     -4.7e-4    *** SEATS + LEADS ***
        2.0e-2     12.5        165.4        -1.785e-1     -6.0e-4    *** SEATS + LEADS ***
        4.0e-2      6.2        158.0        -7.690e-3     -2.6e-5    *** SEATS + LEADS ***
        8.0e-2      3.1        154.4        +1.036e+0     +3.5e-3    seats, LATE

    THE DEVICE SEATS AND LEADS WITH M_ADM = 0 EXACTLY, over a window from
    5e-3 to 4e-2 -- most of a decade, no narrower than composite.py's bare
    negative mass.  Converged: the conjugate point sits at 228.65 +- 0.05 over
    n = 1500 to 9000, a sixfold refinement, and the delay to five figures.
    CORRECTED (DOCKET 67, M: "address/correct/repair all figures"): the
    Jacobi loop first ran with the opposite sign to Gao-Wald eq. (11)
    (A'' = +K A; see survey()).  Corrected, the table's conjugate points at
    5e-3 and 1e-2 move by one step, 228.5 -> 228.6 and 182.2 -> 182.3, and the
    convergence band from 228.45 +- 0.04 to 228.65 +- 0.05 (computed: 228.60,
    228.70, 228.65, 228.67 at n = 1500, 3000, 6000, 9000).  The rows at 2e-2,
    4e-2 and 8e-2, every delay, every seat / lead verdict and the window's
    edges do not move: on this vacuum corridor the flip only swaps which
    transverse axis collapses.
    The linearised slice (1 - 2Phi) delta is a Riemannian metric only for
    m < m* = 0.0100010; above it -- the upper half of this window, the best
    lead at 2e-2 included -- it is not an initial data set and the rigidity
    argument below is silent (a positive completion such as exp(-Phi/2),
    RECONSTRUCTED, keeps E = 0 and R(0) < 0 across the window) (DOCKET 67).

    THE BEST RELATIVE LEAD is -6.0e-4 at m = 2e-2 (composite.py's bare mass
    gives ~5e-4 in another geometry).  Zeroing M_ADM costs the shell's delay,
    13.1 % of the core's first-order advance here, and that share is set by a
    design rule rather than luck:

        shell delay / core advance  ~  (L / R_s) / (2 ln(L/b))     (b >> a)

    The core's advance carries a logarithm and the shell's delay does not, so
    PUT THE SHELL FAR.  At these numbers the ratio is 0.1315 (computed; the
    exact first-order form 2(L/R_s) / (4 asinh((L/2)/sqrt(b^2+a^2))) gives
    the same 0.1315).
    CORRECTED (DOCKET 67): this paragraph read "is if anything slightly
    BETTER than the bare mass's ~5e-4.  Respecting the positive mass theorem
    costs almost nothing here ... the measured lead is what 'nearly free'
    means".
    CORRECTED (DOCKET 67): the rule was first written with the core radius a
    in the logarithm, (L/R_s)/(2 ln(L/a)) = 7.8 % (0.0780 computed; pinned
    as 0.0781), read as "the core's advance carries a logarithm of its
    compactness ... MAKE THE CORE SMALL".
    For this potential the first-order advance is 4m asinh((L/2)/sqrt(b^2 +
    a^2)), ln(L/b) at b = 1 >> a, so the ratio is 13.1 %; the advance per
    unit m is 22.8144 at a = 0.02 and 22.8152 at a = 0.002, and this file's
    integrator agrees with the b-form (ratio 1.0002).  The core is still made
    small, for the vacuum corridor (error 2), not for the delay.  The table
    above is integrated, not taken from this rule, and is unaffected.
    What rested on the < 10 % does move: "costs almost nothing" and "nearly
    free" are restated as what is computed -- the shell's delay is 13.1 % of
    the core's first-order advance at this geometry (L = 300, R_s = 200,
    b = 1), and it falls as R_s grows.  "Slightly BETTER than the bare mass's
    ~5e-4" compares two geometries (composite.py: b = 0.3, L = 75; here b = 1,
    L = 300), so it is not a like-for-like measurement of the shell's cost;
    the like-for-like figure is the 13.1 %.

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
    of.  RIGIDITY: on a complete, asymptotically flat, boundaryless time-
    symmetric slice -- hypotheses this device meets for m < m* = 0.0100010 --
    M_ADM = 0 under the dominant energy condition implies the slice IS FLAT
    (Euclidean).  This one is not -- its scalar curvature at the centre is
    R(0) = -2.9994e4 at m = 5e-3 -- so its matter CANNOT satisfy the DEC.
    CORRECTED (DOCKET 67): this said "the spacetime IS MINKOWSKI" and gave
    "it seats a conjugate point" as the witness; the published k = 0
    conclusion is a Euclidean slice, and that witness rests on linearised
    optics on rays whose lead the header withdraws.  The
    negative energy density is forced by the design's own M_ADM = 0, by a
    theorem, with no appeal to any magnitude.  What follows below stands
    unchanged; only the word ASSUMED does not.
    AND NARROWED BY apply.py: M_ADM is a FREE PARAMETER here -- letting the
    shell mass float free of the core's still seats and still leads at
    M_ADM > 0, while a POSITIVE core seats and arrives LATE.  So the exotic
    matter belongs to THE LEAD, locally, and rigidity is a second proof of it
    rather than its source.
 2. LINEARISED WEAK FIELD, as composite.py.  Along the b = 1 ray |Phi| is at
    most 4.97e-3 at m = 5e-3 and 3.98e-2 at m = 4e-2; in the CORE it is not
    small -- m/a = 0.25 at m = 5e-3 -- and g_ii = 1 - 2Phi reaches 0 at the
    core centre at m = 0.010001 and is negative inside r* = 0.0346 at m = 2e-2
    and r* = 0.0774 at m = 4e-2.  No ray enters that region.  The window's
    edges are INDICATIVE and a strong-field treatment could move them.  This
    is the weakest point here.  CORRECTED (DOCKET 67) from "Phi_max ~ m/a =
    0.25 at the design point", which put the core's value on the ray and
    understated the core across the window.
 3. THE FOCUS IS ASTIGMATIC, as composite.py: a line focus, enough to break
    achronality, not a point-to-point image.
 4. NO PAYLOAD.  Null-geodesic optics throughout.
 5. NO STABILITY ANALYSIS.  A negative core inside a positive shell is a
    configuration nobody has shown to hold together, and wall.py's history in
    this project is a warning about assuming it would.

stdlib only.  composite.py supplies the geodesic, Riemann and Jacobi-matrix
machinery, validated there against 4M/b, the traceless condition and the
analytic Shapiro, and (DOCKET 67) its Jacobi sign against neighbouring
geodesics.
"""
import math, sys

A_CORE = 0.02
R_SHELL = 200.0
B_RAY = 1.0
X0 = -150.0
LAM = 300.0
NSTEP = 2500


def potential(m, a=A_CORE, Rs=R_SHELL):
    """Phi(r) = m/sqrt(r^2+a^2) - m/max(r,R_s).  Monopoles cancel: M_ADM = 0.

    A prescribed potential: core and shell are superposed with no stress
    content specified.  The shell term makes Phi only Lipschitz at r = R_s,
    so the metric is C^{0,1} there and its curvature carries a delta on the
    shell -- below the C^2 the conjugate-point theorems assume, a NAMED
    hypothesis for any ray that crosses r = R_s (DOCKET 67 found conjugate
    points on anecscope's seven rays re-run from inside the shell)."""
    def f(p, _M=None):
        r = math.sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2])
        return m / math.sqrt(r * r + a * a) - m / max(r, Rs)
    return f


def _install(m, a=A_CORE, Rs=R_SHELL):
    import composite
    composite.phi = potential(m, a, Rs)
    return composite


def adm_residual(m, a=A_CORE, Rs=R_SHELL, r=1000.0):
    """Phi far away.  Zero ADM mass means this tends to zero, not to a 1/r tail.

    That reads the ADM flux because composite.py's metric is isotropic, the
    same Phi in g_tt and g_ij (Psi = Phi) -- a NAMED hypothesis (DOCKET 67)."""
    return potential(m, a, Rs)((r, 0.0, 0.0))


def trace_ratio(m, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """|trace| / |largest component| of the tidal matrix at closest approach.
    At linear order in Phi vacuum forces the trace to zero, so this measures
    how empty the corridor is: the linear density term 2 lap Phi.

    Only at linear order (DOCKET 67): the metric is not an exact vacuum
    solution where lap Phi = 0, and this probe (k null in eta, not in g;
    coordinate screen) cancels its O(Phi^2) residue.  With an exactly null k
    and the orthonormal screen survey() integrates, |tr|/max = 7.32e-3 at
    a = 0.02, dominated by the metric's own O(Phi) residue."""
    cp = _install(m, a, Rs)
    T = cp.tidal((0.0, b, 0.0), [1.0, 1.0, 0.0, 0.0],
                 [0., 0., 1., 0.], [0., 0., 0., 1.], m)
    return abs(T[0][0] + T[1][1]) / max(abs(T[0][0]), abs(T[1][1]))


def survey(m, b=B_RAY, a=A_CORE, Rs=R_SHELL, x0=X0, lam=LAM, n=NSTEP,
           sign=None):
    """One corridor ray: does it seat, and does it lead?

    sign = None takes composite.JACOBI_SIGN (Gao-Wald eq. 11); pass
    composite.AS_WRITTEN_SIGN only to reproduce the first-written loop."""
    cp = _install(m, a, Rs)
    if sign is None:
        sign = cp.JACOBI_SIGN
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
        # SIGN: composite.tidal returns T = -K, so eq. (11) (Gao-Wald / MTW
        # 11.10), A'' = -K A, is A'' = +T A.  CORRECTED (DOCKET 67, on M's
        # ruling): this loop first integrated A'' = -T A = +K A.  That agrees
        # for a traceless diagonal tidal matrix -- the vacuum corridor used
        # here moves by about one step (228.48 -> 228.60 at m = 5e-3) -- and
        # gave wrong conjugate points on a ray through matter, such as the
        # withdrawn a = 0.5 corridor (error 2): the selftest keeps that ray as
        # the control.
        acc = [[sign * sum(T[r][s] * A[s][c] for s in range(2)) for c in range(2)]
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


def first_order_delay(m, b=B_RAY, a=A_CORE, Rs=R_SHELL, lam=LAM):
    """t - |dx| at first order in m for the straight ray x0 = -lam/2 .. +lam/2:
    the shell's delay 2 m L / R_s (constant Phi = -m/R_s inside it) minus the
    core's advance 4 m asinh((L/2)/sqrt(b^2 + a^2)) (Shapiro, linear in the
    potential; Will 2014 eq. 62 / arXiv:1710.05834 eq. 3, READ-VIA-
    RESTATEMENT in DOCKET 67).  The closest approach d = sqrt(b^2 + a^2) is
    what enters the logarithm, not the core radius a (DOCKET 67)."""
    return 2.0 * m * lam / Rs - 4.0 * m * math.asinh((lam / 2.0) / math.hypot(b, a))


def shell_to_core_ratio(b=B_RAY, a=A_CORE, Rs=R_SHELL, lam=LAM):
    """The shell's first-order delay over the core's first-order advance."""
    return (2.0 * lam / Rs) / (4.0 * math.asinh((lam / 2.0) / math.hypot(b, a)))


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
    print("       positive mass theorem's INEQUALITY has nothing to object to --")
    print("       vacuously: the DEC it assumes fails here (DOCKET 67).")
    print("       Its RIGIDITY clause does, and productively: M_ADM = 0 under")
    print("       the DEC forces a flat (Euclidean) slice, so the DEC must fail")
    print("       here.  pair.py")
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
    # CORRECTED (DOCKET 67): pinned 228.45 +- 0.3 with the opposite Jacobi
    # sign (228.48 at n = 2500); eq. (11)'s sign gives 228.60 here and
    # 228.65 +- 0.05 over n = 1500 .. 9000.  The tolerance is one step of
    # h = 0.12, so the as-written 228.48 now FAILS this pin.
    near("the conjugate point at m = 5e-3 (eq. 11 sign)", rows[5e-3]["conjugate"],
         228.65, 0.1)

    print("\nThe Jacobi sign, on a ray through matter (DOCKET 67)")
    # error 2's withdrawn corridor, a = 0.5: the ray runs inside the core's
    # NEGATIVE density, R_kk < 0, so Ricci DEFOCUSES.  eq. (11)'s sign seats
    # nothing at m = 5e-3; the first-written sign seated at 261.36, i.e. it
    # let negative R_kk focus.  A control that fails if the sign regresses.
    import composite
    wet = survey(5.0e-3, a=0.5)
    wet_old = survey(5.0e-3, a=0.5, sign=composite.AS_WRITTEN_SIGN)
    print("       a = 0.5, m = 5e-3: eq. (11) sign %s; as-written sign %s"
          % (wet["conjugate"], wet_old["conjugate"]))
    chk("eq. (11) sign: negative R_kk defocuses, no seat", wet["seats"], False)
    chk("CONTROL: the as-written sign seats there (Ricci reversed)",
        wet_old["seats"], True)

    print("\nWhat M_ADM = 0 costs: the shell's delay against the core's advance")
    best = abs(rows[2e-2]["relative"])
    near("best relative lead, at m = 2e-2", best / 5.96e-4, 1.0, 0.05)
    chk("no worse than composite.py's bare mass (~5e-4; b = 0.3)",
        best > 4.0e-4, True)
    # CORRECTED (DOCKET 67, key shapiro-delay): this block pinned the a-form
    # (L/R_s)/(2 ln(L/a)) = 0.0781 and checked it "under 10 %".  Shapiro's
    # logarithm carries the closest approach, so the b-form is the figure.
    bform = (LAM / R_SHELL) / (2.0 * math.log(LAM / B_RAY))
    near("b-form design rule (L/R_s)/(2 ln(L/b))", bform, 0.1315, 1e-3)
    near("first-order shell delay / core advance, this potential",
         shell_to_core_ratio(), 0.1315, 1e-3)
    chk("the shell's share is NOT under 10 % (the a-form's < 10 % withdrawn)",
        shell_to_core_ratio() < 0.1, False)
    # The integrator decides between the forms: the antisymmetric part of the
    # integrated delay is the first-order (linear-in-m) term.
    dp, dm = survey(1.0e-3)["delay"], survey(-1.0e-3)["delay"]
    anti = 0.5 * (dp - dm)
    aform = (LAM / R_SHELL) / (2.0 * math.log(LAM / A_CORE))
    aform_delay = 2.0e-3 * LAM / R_SHELL - 4.0e-3 * math.log(LAM / A_CORE)
    print("       antisymmetric delay at m = 1e-3: %+.5e; b-form %+.5e; a-form %+.5e"
          % (anti, first_order_delay(1.0e-3), aform_delay))
    near("integrated / first-order b-form (closest approach in the log)",
         anti / first_order_delay(1.0e-3), 1.0, 2e-3)
    # pinned 0.0781 +- 1e-3 as first written; computed 0.077997 (DOCKET 67).
    near("CONTROL: a-form (WITHDRAWN) (L/R_s)/(2 ln(L/a))",
         aform, 0.07800, 1e-4)
    chk("CONTROL: the a-form misses the integrated delay by > 10 %",
        abs(anti / aform_delay - 1.0) > 0.1, True)
    print("       DESIGN RULE: put the shell far (b-form ratio 13.1 %).")

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
    print("  configuration (vacuously: the core violates the DEC it assumes) --")
    print("  and its RIGIDITY clause then DERIVES the exotic matter this file")
    print("  had only assumed, for m < 1.0001e-2, where the slice is Riemannian.")
    print("  See pair.py.")
    print("  The corridor is vacuum at linear order -- density term 7.5e-4 of")
    print("  the tidal scale; the trace the Jacobi loop sees is ~0.7 %, the")
    print("  linearisation floor -- which needs the core compact against the")
    print("  impact parameter, b/a >~ 50.")
    print("  The shell delays without focusing, by Newton's shell theorem, so")
    print("  all the focusing is the core's Weyl term.")
    print("\n  WHAT M_ADM = 0 COSTS: the window runs 5e-3 to 4e-2, most of a")
    print("  decade, and the best relative lead is -6.0e-4 (a bare negative")
    print("  mass gives ~5e-4 in composite.py's different geometry). The shell")
    print("  delay is 13.1 % of the core's first-order advance, because the")
    print("  core's advance carries ln(L/b) and the shell's does not. Put the")
    print("  shell far. (DOCKET 67: first written \"NEARLY FREE\", ~8 % with")
    print("  ln(L/a).)")
    print("\n  Negative mass is still assumed, the field is linearised with")
    print("  m/a = 0.25 in the core, which is NOT small, the focus is astigmatic, there")
    print("  is no payload, and NOTHING here shows the configuration is stable.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
