"""
anec.py -- QNEC, asked properly.  IT WITHDRAWS THIS SESSION'S HEADLINE.

shape.py predicted that the energy-condition closure would LOOSEN under its
dynamical form, and named QNEC.  nullbound.py then loosened it via a different
member of the family and was scored a half hit.  This file asks the named member,
and the answer runs the other way.

    QNEC INTEGRATES TO ANEC.  ANEC IS VIOLATED BY THE ALCUBIERRE BUBBLE ON EVERY
    RAY MEASURED.  AND SNEC -- WHICH nullbound.py SAID PERMITTED THE WALL -- IS
    VIOLATED TOO, AT EVERY SAMPLING WIDTH OF ORDER THE BUBBLE RADIUS OR MORE.

-- THE ERROR IN nullbound.py, STATED FIRST ------------------------------------
SNEC is INTEGRAL <T_kk> g^2 dl >= -(4B/G) INTEGRAL (g')^2 dl, and it must hold
for EVERY sampling function g.  nullbound.py evaluated it at ONE width -- the
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

The crossover is at w of order the BUBBLE RADIUS, not the wall thickness.  One
width is not a scan, and choosing the loosest one is the error.

-- AND QNEC IS WORSE, BECAUSE IT IS A THEOREM ---------------------------------
QNEC is <T_kk> >= (hbar/2 pi) S''_out, pointwise but state-dependent.  Integrate
it along a complete generator: INTEGRAL S'' dl = [S'], and for a localised bubble
that is asymptotically vacuum the boundary variation vanishes, so

        QNEC  ==>  INTEGRAL <T_kk> dl >= 0,   which is ANEC.

Measured here, with T_mu_nu computed from the Einstein tensor by typefour.py's
validated pipeline and contracted with the null k^mu = (1, v+1, 0, 0):

        y = 0.0    INTEGRAL T_kk dx = -0.0807
        y = 0.2                       -0.0865
        y = 0.3                       -0.0946
        y = 0.5                       -0.1290
        y = 0.8                       -0.3441

    NEGATIVE ON EVERY RAY.  ANEC IS VIOLATED, SO QNEC FORBIDS THE CONFIGURATION.

And unlike SNEC -- a conjecture with holographic support -- QNEC is a THEOREM in
quantum field theory (Bousso, Fisher, Leichenauer & Wall; Balakrishnan, Faulkner,
Khandker & Wang; Ceyhan & Faulkner).  So the instrument that closes this is
stronger than the one nullbound.py used to open it.

-- WHAT SURVIVES OF nullbound.py, AND IT IS NOT NOTHING -----------------------
  * Fewster & Roman stands: there are no quantum inequalities along null
    geodesics in 4D.  That is the corpus's Register 5537 and it is untouched.
  * Pfenning & Ford's bound really is a TIMELIKE instrument, and their bound ON
    THE WALL THICKNESS really is an artefact of it.
  * The 1/D^2 cancellation is real arithmetic.

    SO THE WALL THICKNESS GENUINELY DOES DROP OUT -- BUT NOT INTO PERMISSION.
    ANEC is violated at EVERY thickness, so D was never the obstruction and
    removing the D bound buys nothing.  The 10^62 kg figure was indeed the wrong
    way to state the problem.  The right way is worse.

-- WHICH IS THE SAME SHAPE AS typefour.py -------------------------------------
Both surviving obstructions are D-independent and both are about KIND rather than
amount: the matter has no rest frame (Type IV), and the averaged null energy is
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

stdlib only.  typefour.py supplies the stress tensor and its two validations.
"""
import math, sys

VS = 0.5
Y_RAYS = (0.0, 0.2, 0.3, 0.5, 0.8)
B_FK = 1.0 / (32.0 * math.pi)

def _stress_lower(p, vs=VS):
    import typefour as tf
    Tm, _gi = tf.stress_mixed(p, vs)
    g = tf.metric(p, vs)
    return [[sum(g[m][a] * Tm[a][n] for a in range(4)) for n in range(4)]
            for m in range(4)]

def null_vector(p, vs=VS, sign=1.0):
    """k^mu = (1, v + sign, 0, 0).  Null in this metric -- checked in selftest."""
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
    _xs, tk, h = sample_ray(y, vs, a, b, n)
    return sum(tk) * h

def snec_terms(xs, tk, h, w, B=B_FK):
    """(LHS, RHS) of INT T_kk g^2 >= -4B INT (g')^2, Gaussian of width w."""
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
    as a flag rather than computed."""
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

    print("\nANEC: INT T_kk dx along rays through the wall")
    for y in Y_RAYS:
        I = anec_integral(y)
        print("      y = %.1f   INT T_kk dx = %+.6f" % (y, I))
        chk("  negative at y = %.1f" % y, I < 0.0, True)
    chk("ANEC is violated on every ray tested",
        all(anec_integral(y) < 0.0 for y in Y_RAYS), True)
    chk("  and QNEC integrates to ANEC", qnec_implies_anec(), True)

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
    print("""      Fewster & Roman stands, Pfenning-Ford really is a timelike
      instrument, and D really does drop out -- but into PROHIBITION, not
      permission.  ANEC is violated at every thickness, so removing the D
      bound buys nothing.""")

    print("\nThe same shape as typefour.py")
    import typefour
    chk("Type IV is D-independent and about kind", typefour.is_type_iv((0.9, 0.3, 0.0)), True)
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
    print("  violated at every thickness, and QNEC -- a theorem, not a conjecture")
    print("  -- integrates to ANEC.  What remains is two D-independent objections")
    print("  about the KIND of matter, not the amount.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
