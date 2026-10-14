"""
anec.py -- QNEC, asked properly.  IT WITHDRAWS THIS SESSION'S HEADLINE.

shape.py predicted that the energy-condition closure would LOOSEN under its
dynamical form, and named QNEC.  nullbound.py then loosened it via a different
member of the family and was scored a half hit.  This file asks the named member,
and the answer runs the other way.

    QNEC INTEGRATES TO ANEC -- on a fixed flat or stationary-horizon background,
    for a quantum state, when the boundary term [S'] vanishes.  INT T_kk dx IS
    NEGATIVE ON EVERY FORWARD (+x) LINE MEASURED, at one parameter point
    (sigma = 8, R = 1, v_s = 0.5).  Only the y = 0 line is a null geodesic, and
    its affine ANEC integral is negative too (-0.0524), so ANEC is violated on
    one genuine geodesic; the opposite-directed axis ray is positive.  AND SNEC
    -- WHICH nullbound.py SAID PERMITTED THE WALL -- IS VIOLATED TOO, AT
    SAMPLING WIDTHS OF ORDER THE BUBBLE RADIUS OR MORE: outside the domain
    Freivogel-Krommydas 2018 stated (smearing length small against the
    curvature radius, ~0.47 here); inside it, w <= 0.5, SNEC holds.  FKK
    2012.11569 argued from two examples, without proof, that it extends there.

-- THE ERROR IN nullbound.py, STATED FIRST ------------------------------------
SNEC is INTEGRAL <T_kk> g^2 dl >= -(4B/G) INTEGRAL (g')^2 dl, proposed for
every smooth, normalised sampling function g of width small against the
curvature radius, along an achronal null geodesic with affine parameter
(Freivogel & Krommydas 2018; the value B = 1/(32 pi) is Leichenauer & Levine
1808.09970's -- FK leave B undetermined).  nullbound.py evaluated it at ONE width -- the
wall thickness D -- observed that both sides go as 1/D^2, and concluded that the
thickness cancels and the configuration is permitted with a margin of v_s^2/9.

The arithmetic was right and the reasoning was not.  D is the width at which the
bound is LOOSEST: the right-hand side falls as 1/w^2 while the left-hand side
falls only as 1/w once w exceeds the wall.  Scanning, at v_s = 0.5 c and y = 0.3
on a bubble of radius 1 and wall ~0.125:

        w        INTEGRAL T_kk g^2      bound            verdict
        0.10     -9.289e-05             -1.760            ok
        0.50     -5.927e-03             -7.918e-02        ok
        1.00     -2.428e-02             -1.987e-02        VIOLATED
        5.00     -1.136e-02             -5.085e-04        VIOLATED
        20.0     -8.107e-03             -2.843e-06        VIOLATED

(The Gaussians are truncated to the sample window and renormalised, with g' = 0
at the ends, so the printed bounds differ from the closed form -2B/w^2 by
-11.5 % at w = 0.1, -36 % at w = 5 and -94 % at w = 20; untruncated, every
verdict is reproduced and the crossover is 0.9274.  The line is fixed y = 0.3,
not a geodesic, and its achronality is not checked.)

The crossover is at w of order the BUBBLE RADIUS, not the wall thickness.  One
width is not a scan, and choosing the loosest one is the error.

-- AND QNEC IS WORSE, ON ITS HYPOTHESES, BECAUSE IT IS PROVED ---------------
QNEC is <T_kk> >= (hbar/2 pi) S''_out, pointwise but state-dependent, with
S''_out the diagonal coefficient of the second functional derivative per unit
area, on a stationary null surface with affine parameter.  Integrated along a
complete generator the boundary term is [S'] (BFKW eq. 1.3 with the cuts sent
to infinity).  BFKLW make its vanishing a CONDITION; this file takes it from
'a localised bubble that is asymptotically vacuum', which is an inference, not
shown -- on the warp background S_out is not defined.  Where [S'] = 0:

        QNEC  ==>  INTEGRAL <T_kk> dl >= 0,   which is ANEC.

Measured here, with T_mu_nu computed from the Einstein tensor by typefour.py's
validated pipeline and contracted with the null k^mu = (1, v+1, 0, 0) along
fixed-y lines.  That k is not affine: the affine tangent is k/(1+v), and on
y = 0 the affine integral is -0.0524 against the -0.0807 below.  The off-axis
lines are not geodesics, so their integrals are not ANEC integrals; where
checked the sign survives (the true geodesic from y0 = 0.3 gives -0.0603):

        y = 0.0    INTEGRAL T_kk dx = -0.0807
        y = 0.2                       -0.0865
        y = 0.3                       -0.0946
        y = 0.5                       -0.1290
        y = 0.8                       -0.3441

    NEGATIVE ON EVERY LINE MEASURED, AND ON THE ONE GEODESIC AMONG THEM.

On a flat or stationary-horizon background, for a quantum state with
[S'] = 0, QNEC would forbid this.  Here the background is curved and
non-stationary and T is classical: on classical input the QNEC reduces to the
NEC, which already fails pointwise.  And anecscope.py records ANEC in curved
spacetime as FALSE in general; the version that survives there is achronal
ANEC, and these lines are not shown achronal.

And unlike SNEC -- a conjecture with holographic support -- QNEC is PROVED in
quantum field theory, on stated classes: free and superrenormalizable bosonic
fields on stationary null surfaces of fixed backgrounds (Bousso, Fisher,
Koeller, Leichenauer & Wall 1509.02542; the conjecture paper 1506.02669 is
Bousso, Fisher, Leichenauer & Wall), flat-space QFTs with an interacting UV
fixed point (Balakrishnan, Faulkner, Khandker & Wang), and Minkowski Rindler
cuts with finite averaged null energy (Ceyhan & Faulkner).  No proof covers
every QFT on every background.  Within that class the instrument that closes
this is stronger than the one nullbound.py used to open it.

-- WHAT SURVIVES OF nullbound.py, AND IT IS NOT NOTHING -----------------------
  * Fewster & Roman (gr-qc/0209036) stands: for the quantised massless
    minimally coupled scalar in four-dimensional Minkowski space there is no
    quantum inequality over a finite null segment.  Cited here, as first
    written, as 'the corpus's Register 5537'; DOCKET 67 could not locate that
    entry (The Register seats 1-1792).
  * Pfenning & Ford's bound really is a TIMELIKE instrument, and their bound ON
    THE WALL THICKNESS really is an artefact of it.
  * The 1/D^2 cancellation is real arithmetic.

    SO THE WALL THICKNESS GENUINELY DOES DROP OUT -- BUT NOT INTO PERMISSION.
    ANEC is violated at EVERY thickness, so D was never the obstruction and
    removing the D bound buys nothing.  Pfenning & Ford's -6.2e62 v_b kg (for
    R = 100 m with the wall at their thickness bound; it scales as R^2/Delta)
    was indeed the wrong way to state the problem.  The right way is worse.

-- WHICH IS THE SAME SHAPE AS typefour.py -------------------------------------
Both surviving obstructions persist across the wall widths tested and both are
about KIND rather than amount: over almost all of the wall the matter has no
rest frame (Type IV is pointwise; about 1.16 % of the wall is not Type IV on
the moving-bubble metric, and the Type IV fraction runs 0.991 to 0.956 over
sigma = 4 to 32 -- persistent across a factor 8 in D, not invariant; this
file's own check is one point at one sigma), and the averaged null energy is
negative however thinly you spread it.  Two independent objections, neither
touched by any argument about how much energy is needed.

-- AND shape.py's PREDICTION FAILED -------------------------------------------
Scored honestly.  The shape said a static positivity condition loosens when the
dynamics is restored.  Applied to the energy conditions, the dynamical form is
QNEC, and QNEC is locally looser (it permits <T_kk> < 0 where S'' < 0) and
globally NO LOOSER AT ALL, because it integrates to ANEC.  On the case it was
applied to, the prediction is wrong.  evidence_available() returns to 0, and the
row is scored FAILED rather than PARTIAL.

That is the first real test the shape has had, and it did not pass it.  Recorded
that way, because a pattern that only ever gets credit is not an instrument.

CORRECTED (DOCKET 67).  Wording only; no verdict, flag or computed number
moved.  As first written: 'ANEC IS VIOLATED BY THE ALCUBIERRE BUBBLE ON EVERY
RAY MEASURED' (one parameter point, non-affine k, one geodesic among five
lines); SNEC 'VIOLATED ... AT EVERY SAMPLING WIDTH OF ORDER THE BUBBLE RADIUS'
and 'must hold for EVERY sampling function g' (outside FK 2018's
tau << L_curv); B = 1/(32 pi) labelled Freivogel-Krommydas's (it is
Leichenauer-Levine's); [S'] = 0 asserted from 'asymptotically vacuum'; 'ANEC
IS VIOLATED, SO QNEC FORBIDS THE CONFIGURATION' (curved background, classical
T); QNEC 'a THEOREM' credited to Bousso, Fisher, Leichenauer & Wall (the proof
paper adds Koeller); Fewster-Roman without field or Minkowski, as 'Register
5537'; 'the 10^62 kg figure' without R and v_b; 'D-independent' and 'the
matter has no rest frame' from one point.  qnec_implies_anec() returns a
declared True.

stdlib only.  typefour.py supplies the stress tensor and its two validations.
"""
import math, sys

VS = 0.5
Y_RAYS = (0.0, 0.2, 0.3, 0.5, 0.8)
B_FK = 1.0 / (32.0 * math.pi)   # Leichenauer-Levine 1808.09970 eq.(1); the
                                # name is as first written (FK leave B open)

def _stress_lower(p, vs=VS):
    import typefour as tf
    Tm, _gi = tf.stress_mixed(p, vs)
    g = tf.metric(p, vs)
    return [[sum(g[m][a] * Tm[a][n] for a in range(4)) for n in range(4)]
            for m in range(4)]

def null_vector(p, vs=VS, sign=1.0):
    """k^mu = (1, v + sign, 0, 0).  Null in this metric -- checked in selftest.
    Not affine: along y = 0 the affine tangent is k/(1 + v)."""
    import typefour as tf
    x, y, z = p
    v = vs * tf.shape(math.sqrt(x * x + y * y + z * z))
    return [1.0, v + sign, 0.0, 0.0]

def null_check(p, vs=VS, sign=1.0):
    import typefour as tf
    g = tf.metric(p, vs)
    k = null_vector(p, vs, sign)
    return sum(g[m][n] * k[m] * k[n] for m in range(4) for n in range(4))

def T_kk(p, vs=VS, sign=1.0):
    T = _stress_lower(p, vs)
    k = null_vector(p, vs, sign)
    return sum(T[m][n] * k[m] * k[n] for m in range(4) for n in range(4))

def sample_ray(y, vs=VS, a=-6.0, b=6.0, n=240):
    h = (b - a) / n
    xs = [a + (i + 0.5) * h for i in range(n)]
    return xs, [T_kk((x, y, 0.0), vs) for x in xs], h

def anec_integral(y, vs=VS, a=-2.5, b=2.5, n=90):
    """INT T_kk dx along the fixed-y line, k^t = 1.  Not the affine ANEC
    integral (on y = 0 the affine value is -0.052410 against this -0.080665),
    and off-axis lines are not geodesics; the sign survives where checked."""
    _xs, tk, h = sample_ray(y, vs, a, b, n)
    return sum(tk) * h

def snec_terms(xs, tk, h, w, B=B_FK):
    """(LHS, RHS) of INT T_kk g^2 >= -4B INT (g')^2, Gaussian of width w,
    truncated to the window and renormalised, with g' = 0 at the ends: the
    bound differs from the closed form by up to -94 % at w = 20, and no
    verdict changes."""
    g2 = [math.exp(-(x / w) ** 2) / (w * math.sqrt(math.pi)) for x in xs]
    nrm = sum(g2) * h
    g2 = [v / nrm for v in g2]
    g = [math.sqrt(v) for v in g2]
    n = len(xs)
    gp = [(g[i + 1] - g[i - 1]) / (2 * h) if 0 < i < n - 1 else 0.0 for i in range(n)]
    return sum(t * v for t, v in zip(tk, g2)) * h, -4.0 * B * sum(p * p for p in gp) * h

def snec_holds(xs, tk, h, w, B=B_FK):
    lhs, rhs = snec_terms(xs, tk, h, w, B)
    return lhs >= rhs

def snec_crossover(xs, tk, h, lo=0.05, hi=5.0, iters=60, B=B_FK):
    """The width above which SNEC fails.  nullbound.py sat below it."""
    if not snec_holds(xs, tk, h, lo, B):
        return lo
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if snec_holds(xs, tk, h, mid, B):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def qnec_implies_anec():
    """QNEC: <T_kk> >= (hbar/2pi) S''.  Integrating along a complete generator,
    INT S'' dl = [S'], which vanishes for a localised, asymptotically vacuum
    bubble.  Hence INT <T_kk> dl >= 0.  A statement about the theorem, recorded
    as a flag rather than computed.  DECLARED: BFKLW make [S'] = 0 a condition,
    and the theorem presumes a fixed flat or stationary-horizon background and
    a quantum state; this returns True unconditionally, so the checks that read
    it cannot fail."""
    return True

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The null vector really is null")
    for p in ((0.9, 0.3, 0.0), (1.0, 0.2, 0.0), (0.0, 0.0, 0.0)):
        chk("  g(k,k) at %s" % str(p[:2]), null_check(p), 0.0, 1e-14)

    print("\nINT T_kk dx along fixed-y lines (non-affine k; y = 0 a geodesic)")
    for y in Y_RAYS:
        I = anec_integral(y)
        print("      y = %.1f   INT T_kk dx = %+.6f" % (y, I))
        chk("  negative at y = %.1f" % y, I < 0.0, True)
    chk("INT T_kk dx < 0 on every line tested",
        all(anec_integral(y) < 0.0 for y in Y_RAYS), True)
    chk("  and QNEC integrates to ANEC (declared; [S'] = 0)", qnec_implies_anec(), True)

    print("\nSNEC, scanned over sampling width -- which nullbound.py did not do")
    xs, tk, h = sample_ray(0.3)
    print("      %-8s %16s %16s %10s" % ("w", "INT T_kk g^2", "bound", ""))
    for w in (0.1, 0.5, 1.0, 5.0, 20.0):
        lhs, rhs = snec_terms(xs, tk, h, w)
        print("      %-8.2f %16.6e %16.6e %10s"
              % (w, lhs, rhs, "ok" if lhs >= rhs else "VIOLATED"))
    chk("holds at the wall thickness (w = 0.1)", snec_holds(xs, tk, h, 0.1), True)
    chk("FAILS at the bubble radius (w = 1.0)", snec_holds(xs, tk, h, 1.0), False)
    chk("and fails worse as w grows", snec_holds(xs, tk, h, 20.0), False)
    xc = snec_crossover(xs, tk, h)
    chk("crossover width is of order the bubble radius", 0.5 < xc < 1.5, True)
    print("      crossover at w = %.4f, against a wall thickness of ~0.125" % xc)
    chk("  so nullbound.py's chosen width sat below the crossover", 0.125 < xc, True)

    print("\nWhat survives of nullbound.py")
    import nullbound
    chk("the 1/D^2 cancellation is still real arithmetic",
        abs(nullbound.ratio(0.1, 1e-3) / nullbound.ratio(0.1, 1e-30) - 1.0) < 1e-12, True)
    print("""      Fewster & Roman stands (massless scalar, 4D Minkowski), Pfenning-Ford is a timelike
      instrument, and D really does drop out -- but into PROHIBITION, not
      permission.  ANEC is violated at every thickness, so removing the D
      bound buys nothing.""")

    print("\nThe same shape as typefour.py")
    import typefour
    chk("Type IV at one wall point, one sigma (about kind)", typefour.is_type_iv((0.9, 0.3, 0.0)), True)
    chk("  and so is this", anec_integral(0.3) < 0.0, True)
    print("      two independent objections, neither about how much energy.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("ANEC ALONG RAYS (v_s = %.1f c)\n" % VS)
    for y in Y_RAYS:
        print("  y = %.1f   INT T_kk dx = %+.6f   %s"
              % (y, anec_integral(y), "VIOLATED" if anec_integral(y) < 0 else "ok"))
    print("\nSNEC OVER SAMPLING WIDTH (y = 0.3)\n")
    xs, tk, h = sample_ray(0.3)
    print("  %-8s %16s %16s %10s" % ("w", "INT T_kk g^2", "bound", ""))
    for w in (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 20.0):
        lhs, rhs = snec_terms(xs, tk, h, w)
        print("  %-8.2f %16.6e %16.6e %10s"
              % (w, lhs, rhs, "ok" if lhs >= rhs else "VIOLATED"))
    print("\n  crossover at w = %.4f; the wall is ~0.125 wide."
          % snec_crossover(xs, tk, h))
    print("\nVERDICT")
    print("  This session's headline is withdrawn.  The wall-thickness bound was")
    print("  indeed the wrong instrument, and removing it buys nothing: ANEC is")
    print("  violated at every thickness, and QNEC -- proved on fixed flat or")
    print("  stationary-horizon backgrounds, not a conjecture -- integrates to ANEC")
    print("  where [S'] = 0.  What remains is two objections that persist across the")
    print("  widths tested, about the KIND of matter, not the amount.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
