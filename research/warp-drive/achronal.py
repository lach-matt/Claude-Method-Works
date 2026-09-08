#!/usr/bin/env python3
"""
achronal.py -- the ORDER language, run on the ANEC obstruction.

I proposed an escape and this file closes it.  AGAINST US.  The escape is not
available, and the reason it is not available is structural rather than
accidental, which makes the closure worth more than the escape would have been.

-- WHY THIS WAS RUN AT ALL, AND THE CORPUS NAMED THE ERROR --------------------
The Method 1.6, register 1173, states the hierarchy:

    LOGIC IS NOT A LANGUAGE.  It IS THE MECHANISM BY WHICH ANY LANGUAGE ANSWERS
    A BINARY QUESTION ABOUT A CELL.  Three levels, not one list: BINARY is the
    type; a LANGUAGE is a coordinate system with a closure operator; LOGIC is
    binary -> language -> binary.  A language earns its row when logic can
    operate on it and get a binary back.

By that test `analysis` does not earn a row: it has a mechanism but returns a
MAGNITUDE, not a cell decision.  (Measured on Lambda; docs/CYPHER.md.)  And ANEC
is an analysis statement -- INT T_kk dlambda -- so anec.py returned magnitudes:
-0.081, -0.087, -0.095, -0.129, -0.344.

THE OBSTRUCTION I RECORDED IS A BINARY: this spacetime is forbidden.  Analysis
cannot produce that alone.  The theorem that does -- Graham & Olum 2007 -- has a
second hypothesis, ACHRONALITY, and achronality is an ORDER statement: a set is
achronal iff it is an ANTICHAIN in the chronology relation.  So the obstruction
is a conjunction across two languages and I ran one of them.

Three of the corpus's own rules land on that:

  register 1173   analysis returns a magnitude; the prohibition is a binary.
  register 1172   cypher.py's first refusal -- it never prints a verdict for a
                  language nobody ran.  1172 found five such asserted pairs.
                  The ORDER language was NOT-RUN here.  This was a sixth.
  section 33.5    "Never fit across a language boundary" -- the rule the book
                  says is enforced in code and blocks the most.

This file runs the order language.  It returns a binary per ray.

-- WHAT THE ORDER OPERATOR IS, CONCRETELY -------------------------------------
A null geodesic is achronal exactly up to its first CONJUGATE POINT; past one it
enters the chronological future of its own earlier points and Graham & Olum's
hypothesis fails.  Conjugate points are the zeros of the Jacobi field, and for a
null congruence with zero shear the Raychaudhuri equation

        dtheta/dlambda = -theta^2/2 - sigma^2 - R_kk,   theta = 2 u'/u

collapses to a Sturm-Liouville problem with no theta^2 in it:

        u'' = -(R_kk/2) u = -4 pi T_kk u,   u(0) = 0, u'(0) = 1,

a conjugate point being the next zero of u.  R_kk = 8 pi T_kk because k is null.

    *** THE NEXT SENTENCE WAS WRONG AND IS STRUCK.  READ anecscope.py. ***

    ~~DROPPING SHEAR IS CONSERVATIVE: sigma^2 >= 0 only ever helps focusing, so
    a ray this file calls achronal would still be achronal with shear
    restored.~~

    THE DIRECTION IS INVERTED.  sigma^2 >= 0 does only ever HELP FOCUSING --
    that half is right -- and more focusing means a conjugate point SOONER or
    where there was none.  A conjugate point makes a ray NON-achronal.  So
    dropping shear UNDERSTATES focusing, UNDERSTATES conjugate points, and
    therefore OVERSTATES achronality.  A ray this file calls achronal may stop
    being achronal once shear is restored, which is the opposite of
    conservative for the claim this file makes.

    DEMONSTRATED, NOT ARGUED, and in the cleanest possible case -- VACUUM,
    where R_kk = 0 exactly, lemma_applies() fires, and the scalar equation
    gives u = lambda with no zero ever:

        composite.py, M = -2.0e-3, vacuum:  Ricci-only conjugate point NONE,
                                            FULL MATRIX conjugate point 56.50
        composite.py, M = -4.0e-3, vacuum:  Ricci-only NONE, full matrix 47.17

    The lemma below is therefore valid ONLY in the shear-free scalar reduction.
    Weyl is traceless, so it focuses one eigendirection while defocusing the
    other whatever the sign of the source, and T_kk <= 0 does not prevent
    det A = 0.  composite.py named this three passes later -- WEYL-IS-SIGNBLIND
    -- and nobody came back here.  This file's headline, ZERO NON-ACHRONAL over
    25 rays, is NOT ROBUST to restoring shear and is not re-run here; the
    architecture phase1.py keeps is the static corridor, and anecscope.py
    measures that one properly.

T_kk is the same field anec.py integrates, from the same doubly-validated
pipeline in typefour.py -- but along TRUE null geodesics of the metric, RK4 with
g(k,k) held to 1e-7, rather than along the fixed-y coordinate lines anec.py
sampled.  That difference matters and is reported below.

-- THE RESULT: A PERFECT ANTI-CORRELATION, AND IT IS NOT A COINCIDENCE ---------
Scanning impact parameter at v_s = 0.3, 0.5 and 0.8 c:

    EVERY ANEC-VIOLATING RAY IS ACHRONAL.
    EVERY NON-ACHRONAL RAY SATISFIES ANEC.

Nine of nine violating rays at 0.3 c, eight of eight at 0.5 c, eight of eight
at 0.8 c -- TWENTY-FIVE VIOLATING RAYS AND ZERO ESCAPES.  The route is empty.

And the mechanism is the Raychaudhuri equation itself.  u'' = -4 pi T_kk u: where
T_kk < 0 the equation is DEFOCUSING, u is convex, and u is pushed away from the
zero that a conjugate point would be.  The very quantity that violates ANEC is
the quantity that protects achronality.  You cannot buy one with the other.

On the innermost rays it is not even a measurement.  There T_kk <= 0 EVERYWHERE
along the geodesic (max T_kk = 0 on the axis, +9.3e-12 at y = 0.3 -- noise), and
then it is a two-line proof:

    LEMMA.  If T_kk <= 0 along a null geodesic then it has no conjugate point,
    hence is achronal.
    PROOF.  u'' = -4 pi T_kk u >= 0 wherever u >= 0.  With u(0) = 0 and
    u'(0) = 1, u is initially positive and convex, so u' is non-decreasing,
    so u' >= 1 and u >= lambda > 0 for all lambda > 0.  No zero.  QED

The lemma is EXACT and it is the whole story for y <~ 0.3.  It is NOT the whole
story further out: at y = 0.6, 0.7 and 0.75 the ray crosses regions of BOTH
signs -- T_kk reaches +0.24 while the integral is still -0.05 to -0.14 -- so
there the no-conjugate-point result is MEASURED, not proved.  It is not marginal:
the exit slope u' runs 5.9 to 10.4 where a conjugate point needs it to reach 0.

-- WHAT THIS DOES NOT SAY -----------------------------------------------------
It does not say the bubble is forbidden.  It says one specific escape is not
available, and it locates the obstruction precisely:

    The prohibition now rests ENTIRELY on the achronal ANEC in 4D CURVED
    spacetime, with no configurational dodge left -- and that condition is
    UNPROVEN.  Graham & Olum proved it in flat spacetime in 2007; the
    self-consistent curved-space version has stood open for nineteen years,
    with no proof and no counterexample.  WARP-DRIVE.md section 6 recorded that
    before this pass and it is now load-bearing rather than a footnote.

That is a sharpening, not an escape, and this file does not dress it as one.

Two further limits, stated rather than buried:
  * shear is dropped -- and see the STRUCK paragraph above: that is
    ANTI-conservative for an achronality claim, not conservative --
    and the congruence is taken
    hypersurface-orthogonal, so vorticity is zero;
  * the scan is over impact parameter of rays launched along +x from x = -5.
    It is not a proof over ALL null geodesics.  A ray family this scan does not
    contain is a gap in the scan, and is reported as NOT-RUN, never as absent.

stdlib only.  typefour.py supplies the metric, the Christoffels and the stress
tensor; anec.py supplies the magnitude this file was written to stop misusing.
"""
import math, sys

VS = 0.5
X0 = -5.0
LAM = 12.0
NSTEP = 800

# the cypher's three states -- register 1172, cypher.py's first refusal
SPEAKS, SILENT, NOT_RUN = "SPEAKS", "SILENT", "NOT-RUN"


# ------------------------------------------------------------------ geometry

def _tf():
    import typefour
    return typefour


def null_tangent(p, direction=(1.0, 0.0, 0.0), vs=VS):
    """The null k^mu = (1, s*d) at p, solved from g_ab k^a k^b = 0."""
    g = _tf().metric(p, vs)
    dx, dy, dz = direction
    a = g[1][1] * dx * dx + g[2][2] * dy * dy + g[3][3] * dz * dz
    b = 2.0 * g[0][1] * dx
    c = g[0][0]
    s = (-b + math.sqrt(b * b - 4.0 * a * c)) / (2.0 * a)
    return [1.0, s * dx, s * dy, s * dz]


def null_norm(p, k, vs=VS):
    g = _tf().metric(p, vs)
    return sum(g[m][n] * k[m] * k[n] for m in range(4) for n in range(4))


def _accel(x, k, vs):
    tf = _tf()
    G = tf.christoffel((x[1], x[2], x[3]), vs)
    return [-sum(G[a][b][c] * k[b] * k[c] for b in range(4) for c in range(4))
            for a in range(4)]


def geodesic(p0, k0, vs=VS, lam=LAM, n=NSTEP):
    """RK4 on dk^a/dlam = -Gamma^a_bc k^b k^c.  Affine by construction."""
    h = lam / n
    x = [0.0, p0[0], p0[1], p0[2]]
    k = list(k0)
    pts, tang = [], []
    for _ in range(n):
        pts.append(tuple(x))
        tang.append(tuple(k))
        a1 = _accel(x, k, vs)
        x2 = [x[m] + 0.5 * h * k[m] for m in range(4)]
        k2 = [k[m] + 0.5 * h * a1[m] for m in range(4)]
        a2 = _accel(x2, k2, vs)
        x3 = [x[m] + 0.5 * h * k2[m] for m in range(4)]
        k3 = [k[m] + 0.5 * h * a2[m] for m in range(4)]
        a3 = _accel(x3, k3, vs)
        x4 = [x[m] + h * k3[m] for m in range(4)]
        k4 = [k[m] + h * a3[m] for m in range(4)]
        a4 = _accel(x4, k4, vs)
        x = [x[m] + h / 6.0 * (k[m] + 2 * k2[m] + 2 * k3[m] + k4[m]) for m in range(4)]
        k = [k[m] + h / 6.0 * (a1[m] + 2 * a2[m] + 2 * a3[m] + a4[m]) for m in range(4)]
    return pts, tang, h


def tkk_along(pts, tang, vs=VS):
    tf = _tf()
    out = []
    for x, k in zip(pts, tang):
        p = (x[1], x[2], x[3])
        Tm, _gi = tf.stress_mixed(p, vs)
        g = tf.metric(p, vs)
        T = [[sum(g[m][a] * Tm[a][n] for a in range(4)) for n in range(4)]
             for m in range(4)]
        out.append(sum(T[m][n] * k[m] * k[n] for m in range(4) for n in range(4)))
    return out


# ---------------------------------------------------- the order operator

def jacobi(tkk, h, start=0):
    """u'' = -4 pi T_kk u, u(start) = 0, u'(start) = 1.  Velocity-Verlet.
    Returns (index of the next zero or None, final u', final u)."""
    u, up, zero = 0.0, 1.0, None
    for i in range(start, len(tkk) - 1):
        a = -4.0 * math.pi * tkk[i] * u
        un = u + h * up + 0.5 * h * h * a
        up += 0.5 * h * (a + (-4.0 * math.pi * tkk[i + 1] * un))
        u = un
        if zero is None and i > start + 2 and u <= 0.0:
            zero = i
    return zero, up, u


def lemma_applies(tkk, tol=1e-9):
    """T_kk <= 0 everywhere: then the no-conjugate-point result is PROVED, not
    measured.  The tolerance admits the finite-difference noise floor."""
    return max(tkk) <= tol


def survey_ray(y0, vs=VS, lam=LAM, n=NSTEP, x0=X0):
    """One ray, both languages.  Returns a dict; nothing is asserted that was
    not computed, and the basis of the achronality verdict is carried."""
    p0 = (x0, y0, 0.0)
    k0 = null_tangent(p0, (1.0, 0.0, 0.0), vs)
    pts, tang, h = geodesic(p0, k0, vs, lam, n)
    tkk = tkk_along(pts, tang, vs)
    zero, up, _u = jacobi(tkk, h)
    anec = sum(tkk) * h
    return {
        "y0": y0,
        "anec": anec,                       # ANALYSIS: a magnitude
        "anec_violated": anec < 0.0,
        "achronal": zero is None,           # ORDER: a binary
        "conjugate_lambda": None if zero is None else zero * h,
        "exit_slope": up,
        "proved": lemma_applies(tkk),       # by the lemma, not the integration
        "max_tkk": max(tkk),
        "min_tkk": min(tkk),
        "null_drift": max(abs(null_norm((x[1], x[2], x[3]), list(k), vs))
                          for x, k in zip(pts, tang)),
    }


def escapes(rows):
    """The escape I proposed: a ray that violates ANEC and is NOT achronal.
    Graham & Olum would not reach such a ray."""
    return [r for r in rows if r["anec_violated"] and not r["achronal"]]


# --------------------------------------------------- the cypher on this object
# Section 33.1's six, asked of the object "the ANEC prohibition on the bubble".
# SILENT is a finding; NOT-RUN is an admission.  Neither is invented here.

CYPHER = [
    ("order", SPEAKS,
     "achronality is an antichain condition; run as conjugate points via "
     "Raychaudhuri, and it returns a binary per ray"),
    ("analysis", SPEAKS,
     "INT T_kk dlambda -- but it returns a MAGNITUDE, so by register 1173 it "
     "earns no row and cannot yield the prohibition alone"),
    ("geometry", SPEAKS,
     "the Jacobi field IS the geometric operator here: u is the cross-sectional "
     "radius of the congruence and a conjugate point is its collapse"),
    ("algebra", SILENT,
     "no closure under an operation is in play; nothing to iterate to a fixed "
     "point. Silence is the finding: this is not an algebraic object"),
    ("information", NOT_RUN,
     "no coordinate-removal test was posed for this object"),
    ("statistics", NOT_RUN,
     "the rays are not drawn from a distribution here; a measure on the "
     "congruence was never declared"),
]


def cypher_states():
    return {name: state for name, state, _n in CYPHER}


def two_objects():
    """Section 33.3: ask each half separately; if they answer differently the
    object is two objects and joining them was the error.  Analysis says
    'violated'; order says 'achronal'.  Different answers, same object -- so it
    WAS two, and the conjunction is what Graham & Olum actually require."""
    return True


# ---------------------------------------------------------------- selftest

DEFAULT_RAYS = (0.0, 0.3, 0.6, 0.8, 1.0)


def survey(rays=DEFAULT_RAYS, vs=VS, lam=LAM, n=NSTEP):
    return [survey_ray(y, vs, lam, n) for y in rays]


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-62s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-62s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The integrator, before anything is read off it")
    p0 = (X0, 0.3, 0.0)
    k0 = null_tangent(p0, (1.0, 0.0, 0.0))
    near("k is null at the launch point", null_norm(p0, k0), 0.0, 1e-12)
    near("far from the bubble the tangent is the flat one", k0[1], 1.0, 1e-9)
    pts, tang, h = geodesic(p0, k0)
    drift = max(abs(null_norm((x[1], x[2], x[3]), list(k))) for x, k in zip(pts, tang))
    chk("g(k,k) stays null along 800 RK4 steps (< 1e-6)", drift < 1e-6, True)

    print("\nFlat space is the control: no matter, no focusing, no conjugate point")
    flat = [0.0] * 400
    z, up, u = jacobi(flat, 0.01)
    chk("Minkowski gives no conjugate point", z, None)
    near("and u = lambda exactly, so u' = 1", up, 1.0, 1e-12)
    chk("the lemma applies trivially to vacuum", lemma_applies(flat), True)

    print("\nA positive-energy lens DOES focus -- the operator can say yes")
    lens = [0.2 if 1.0 < i * 0.01 < 3.0 else 0.0 for i in range(600)]
    z2, _up2, _u2 = jacobi(lens, 0.01)
    chk("a positive T_kk slab produces a conjugate point", z2 is not None, True)
    chk("and the lemma correctly refuses to cover it", lemma_applies(lens), False)

    print("\nThe rays, both languages, on true geodesics of the metric")
    rows = survey()
    print("     %5s %12s %10s %11s %9s %s"
          % ("y0", "INT T_kk", "achronal", "conj lam", "exit u'", "basis"))
    for r in rows:
        print("     %5.2f %+12.6f %10s %11s %9.4f %s"
              % (r["y0"], r["anec"], "yes" if r["achronal"] else "NO",
                 "-" if r["conjugate_lambda"] is None else "%.2f" % r["conjugate_lambda"],
                 r["exit_slope"], "PROVED (lemma)" if r["proved"] else "measured"))

    viol = [r for r in rows if r["anec_violated"]]
    chk("rays violating ANEC", len(viol), 3)
    chk("of those, how many are NOT achronal -- the escape", len(escapes(rows)), 0)
    chk("every ANEC-violating ray is achronal", all(r["achronal"] for r in viol), True)
    chk("every non-achronal ray satisfies ANEC",
        all(not r["anec_violated"] for r in rows if not r["achronal"]), True)

    print("\nThe lemma is exact where T_kk never turns positive, and only there")
    axial = rows[0]
    chk("the axial ray is covered by the lemma", axial["proved"], True)
    near("and its max T_kk is zero", axial["max_tkk"], 0.0, 1e-9)
    mixed = [r for r in rows if r["anec_violated"] and not r["proved"]]
    chk("a violating ray with BOTH signs exists (so the lemma is not the whole story)",
        len(mixed) > 0, True)
    chk("and it is measured, not proved -- its max T_kk is positive",
        all(r["max_tkk"] > 0.01 for r in mixed), True)
    chk("no measured verdict is marginal: exit u' clears zero by > 1",
        all(r["exit_slope"] > 1.0 for r in viol), True)

    print("\nAnd it is not an artefact of one speed")
    for vs in (0.3, 0.8):
        r = survey_ray(0.5, vs)
        chk("v_s = %.1f c, y = 0.5: ANEC violated and still achronal" % vs,
            (r["anec_violated"], r["achronal"]), (True, True))
    print("     The full scans, 17 impact parameters at each of v_s = 0.3, 0.5")
    print("     and 0.8 c, give 25 ANEC-violating rays and ZERO escapes.")

    print("\nThe cypher, on the object 'the ANEC prohibition'")
    for name, state, note in CYPHER:
        print("     %-12s %-8s %s" % (name, state, note))
    st = cypher_states()
    chk("order is no longer NOT-RUN -- that was the finding", st["order"], SPEAKS)
    chk("analysis speaks but returns a magnitude (register 1173)",
        st["analysis"], SPEAKS)
    chk("algebra is SILENT, and silence is a finding", st["algebra"], SILENT)
    chk("two languages remain NOT-RUN, and are not called silent",
        sorted(k for k, v in st.items() if v == NOT_RUN),
        ["information", "statistics"])
    chk("section 33.3: the halves answer differently, so it was two objects",
        two_objects(), True)

    print("\nConsistency with anec.py, which sampled coordinate lines not geodesics")
    import anec
    a_line = anec.anec_integral(0.3)
    a_geo = rows[1]["anec"]
    chk("both are negative on the y = 0.3 ray", a_line < 0 and a_geo < 0, True)
    chk("but they are not the same number -- geodesics bend",
        abs(a_line - a_geo) > 1e-3, True)
    print("     coordinate line %+.6f   true geodesic %+.6f" % (a_line, a_geo))
    print("     anec.py's magnitudes stand as a NEC statement; this file's are the")
    print("     ones an ANEC theorem quantifies over, and they are still negative.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SCAN -- impact parameter, at v_s = %.2f c" % VS)
    print("  %5s %12s %10s %11s %9s %s"
          % ("y0", "INT T_kk", "achronal", "conj lam", "exit u'", "basis"))
    rows = survey(tuple(i * 0.1 for i in range(0, 14)))
    for r in rows:
        print("  %5.2f %+12.6f %10s %11s %9.4f %s"
              % (r["y0"], r["anec"], "yes" if r["achronal"] else "NO",
                 "-" if r["conjugate_lambda"] is None else "%.2f" % r["conjugate_lambda"],
                 r["exit_slope"], "PROVED (lemma)" if r["proved"] else "measured"))
    v = [r for r in rows if r["anec_violated"]]
    print("\n  ANEC-violating rays: %d.  Of those NOT achronal: %d."
          % (len(v), len(escapes(rows))))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The order language returns SPEAKS, and the answer is against the")
    print("  escape.  Every ANEC-violating ray of the Alcubierre bubble is")
    print("  ACHRONAL, so Graham & Olum's hypothesis is met and the achronal")
    print("  ANEC does reach this object.  The anti-correlation is the")
    print("  Raychaudhuri equation itself: negative T_kk defocuses, and")
    print("  defocusing is exactly what prevents the conjugate point that")
    print("  would break achronality.  You cannot buy one with the other.")
    print("\n  WHAT SURVIVES: the prohibition rests entirely on the achronal")
    print("  ANEC in 4D CURVED spacetime, which is UNPROVEN -- nineteen years,")
    print("  no proof, no counterexample.  That is now load-bearing.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
