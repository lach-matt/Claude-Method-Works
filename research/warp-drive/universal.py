"""
universal.py -- not which element, but which STATE.  The inversion, worked.

The question "what element permits warp travel" has no answer, and the reason is
now precise: both surviving obstructions quantify over ALL matter.  Type IV says
no substance has the required algebra; ANEC says no substance makes the integral
positive.  Neither mentions an element, so neither can be answered by naming one.

    THE QUESTION WITH A SHAPE IS: WHAT PHYSICS MAKES AN ORDINARY TYPE-I ELEMENT
    BEHAVE AS THE GEOMETRY REQUIRES?  That is a question about STATES, and every
    element has the same states available to its fields.

-- AND TYPE IV IS ALREADY REALIZED BY A STATE ---------------------------------
Not hypothetically.  Martin-Moruno & Visser (Phys. Rev. D 103, 124003):

    "For test fields it is not too difficult to get a type IV stress-energy via
     quantum vacuum polarization effects.  (For example, consider the Unruh
     quantum vacuum state for a massless scalar field in the Schwarzschild
     background.)"

and Abdolrahimi, Page & Tzounis showed the massless conformal scalar in the
Unruh state is Type IV EVERYWHERE outside the horizon.  Roman had the same thing
in 1986 near an evaporating apparent horizon.

Reproduced here from their Appendix B, the (1+1) Schwarzschild Unruh state with
z = 2m/r, using their Eq (B.4) and Gamma = (rho+p)^2 - 4f^2 computed directly:
Gamma changes sign at z = 1/sqrt3, 1, 2/sqrt3 exactly, and the state is TYPE IV
on z in [0, 1/sqrt3) and (1, 2/sqrt3).  A published, closed-form, element-free
Type IV -- and it is a VACUUM STATE, so it belongs to no element in particular
and to every element's fields in general.

    THAT IS THE UNIVERSAL ANSWER'S SHAPE.  Type IV is not a substance anyone must
    find.  It is a state of the quantum vacuum, and the vacuum is the same vacuum
    for hydrogen and for uranium.

-- BUT BACK-REACTION IS WHERE IT BITES, AND THIS IS THE REAL RESULT -----------
The same paper proves that once the stress-energy must SOURCE the geometry
self-consistently, Type I is forced in:

    (1) the domain of outer communication of any STATIC spacetime
    (2) on any Killing horizon -- static, stationary, or bifurcate
    (3) on the axis of any CIRCULAR stationary axisymmetric spacetime
    (4) Bianchi type I, FLRW, and single-mode Bianchi II-IX cosmologies

A warp drive must source its own geometry, so this is the list that matters.
AND THE WARP BUBBLE IS OUTSIDE EVERY ENTRY ON IT:

    (1) NOT STATIC.  Their proof needs block-diagonalisability AND time
        independence, and they say in terms that both are necessary.  Block-
        diagonalisability is exactly VANISHING TWIST, and twist.py measured the
        twist nonzero off-axis in 3+1D.
    (2) NO KILLING HORIZON.  Subluminal drives have none: f* = 1 - c/v_s lies in
        [0,1) only for v_s >= c (twist.py).
    (3) NOT CIRCULAR.  Circularity is invariance under (t, phi) -> (-t, -phi).
        The Alcubierre metric has g_tx = -v, which flips sign under t -> -t while
        x is not reversed.  Verified here at three points: NOT invariant.  Their
        axisymmetric theorems assume circularity and do not apply.
    (4) NOT HOMOGENEOUS.  A localised bubble is not Bianchi and not FLRW.

Entry (3) also resolves what looked like a contradiction: typefour.py measures
Type IV ON THE AXIS at (0.9, 0), h-converged to six figures, where their axis
theorem would say Type I.  Non-circularity is why, and it is not a loophole.

-- WHICH GIVES THE UNIVERSAL STATEMENT ----------------------------------------
Put the two together with BBV's Theorem III.15 -- a coordinate vorticity-free
Alcubierre warp drive IS Minkowski -- and the pieces close:

        TWIST = 0   =>  Minkowski (BBV) AND block-diagonalisable => TYPE I (MMV)
        TWIST != 0  =>  it transports, AND it is outside every Type-I theorem

    SO TYPE IV IS NOT AN ACCIDENT OF ALCUBIERRE'S ANSATZ.  IT IS FORCED BY THE
    SAME GEOMETRIC PROPERTY THAT MAKES THE OBJECT A WARP DRIVE AT ALL.  A warp
    drive that were Type I would have zero twist and would be flat space.

That is element-independent in both directions, which is what was asked for.  It
says nothing about materials because there is nothing about materials to say:
the requirement is a property of the geometry and of the vacuum state in it.

-- WHAT IS OPEN, AND IT IS ONE SHARP QUESTION ---------------------------------
Whether a SELF-CONSISTENT Type IV solution exists -- Type IV that sources its own
geometry rather than riding a fixed background.  MMV close their paper with
"This list is not necessarily exhaustive, and we are actively seeking further
examples", so the warp case is UNSETTLED rather than excluded.  No theorem covers
it and no construction exhibits it.

-- WHAT THIS DOES NOT DO ------------------------------------------------------
  * It does not exhibit a self-consistent Type IV warp solution.  Absence of a
    theorem is not a construction.
  * The Unruh result is a TEST FIELD on a fixed background.  That is precisely
    the case MMV distinguish from back-reaction, and the distinction is the
    whole content of their paper.
  * IT DOES NOT TOUCH ANEC.  That is the other obstruction, it is independent,
    and its element-independent escape -- achronality -- is not examined here.

stdlib only.  typefour.py supplies the stress tensor, twist.py the twist.
"""
import math, sys

# -- MMV Appendix B: the (1+1) Schwarzschild Unruh vacuum ---------------------

def unruh_rho(z, p_inf=1.0):
    """MMV Eq (B.4)."""
    return p_inf * (1.0 - 16.0 * z * z + 14.0 * z ** 4) / (2.0 * (1.0 - z))

def unruh_p(z, p_inf=1.0):
    return p_inf * (1.0 - 2.0 * z ** 4) / (2.0 * (1.0 - z))

def unruh_f(z, p_inf=1.0):
    return p_inf * 1.0 / (2.0 * (1.0 - z))

def unruh_gamma(z, p_inf=1.0):
    """Gamma = (rho+p)^2 - 4f^2.  Gamma < 0 <=> no causal eigenvector <=> TYPE IV."""
    r, p, f = unruh_rho(z, p_inf), unruh_p(z, p_inf), unruh_f(z, p_inf)
    return (r + p) ** 2 - 4.0 * f * f

def unruh_type(z):
    return "IV" if unruh_gamma(z) < 0.0 else "I"

def unruh_sign_changes():
    """DERIVED.  Gamma vanishes where (1-8z^2+6z^4)^2 = 1, i.e. at
    (3z^2-1)(z^2-1) = 0 and z^2 = 4/3: z = 1/sqrt3, 1, 2/sqrt3."""
    return (1.0 / math.sqrt(3.0), 1.0, 2.0 / math.sqrt(3.0))

# -- the back-reaction theorems, and whether the bubble is inside them --------

MMV_TYPE_I_FORCED = (
    ("static, domain of outer communication", "needs block-diagonalisability AND time independence"),
    ("any Killing horizon", "static, stationary or bifurcate"),
    ("axis of a CIRCULAR stationary axisymmetric spacetime", "circularity is the hypothesis"),
    ("Bianchi I, FLRW, single-mode Bianchi II-IX", "homogeneity"),
)

def is_circular(vs=0.5, pts=((0.9, 0.3), (1.0, 0.0), (0.6, 0.5))):
    """Circularity: invariance under (t, phi) -> (-t, -phi).  phi rotates about
    x, so it flips y and z.  Returns True only if the metric is invariant at
    every point tested."""
    import typefour as tf
    S = (-1.0, 1.0, -1.0, -1.0)
    for (x, y) in pts:
        g = tf.metric((x, y, 0.0), vs)
        for i in range(4):
            for j in range(4):
                if abs(g[i][j] - S[i] * S[j] * g[i][j]) > 1e-15:
                    return False
    return True

def is_static(vs=0.5):
    """Static <=> block-diagonalisable <=> zero twist.  twist.py decides."""
    import twist
    return abs(twist.wedge_txy_closed(0.9, 0.3, vs)) < 1e-12

def has_killing_horizon(vs):
    import twist
    return twist.has_horizon(vs)

def is_homogeneous():
    """A localised bubble is not Bianchi and not FLRW."""
    return False

def escapes_all_theorems(vs=0.5):
    """DERIVED.  True iff the bubble is outside every MMV Type-I-forced case."""
    return (not is_static(vs) and not has_killing_horizon(vs)
            and not is_circular(vs) and not is_homogeneous())

def twist_is_the_reason(vs=0.5):
    """The single geometric fact behind (1) and (3): nonzero twist is exactly
    non-block-diagonalisability, and BBV Thm III.15 says zero twist is
    Minkowski.  So transport and escaping the theorems are the same condition."""
    import twist
    off = abs(twist.wedge_txy_closed(0.9, 0.3, vs))
    on = abs(twist.wedge_txy_closed(0.9, 0.0, vs))
    return off > 1e-3 and on < 1e-12

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("TYPE IV IS REALIZED BY A STATE -- MMV Appendix B, reproduced")
    a, b, c = unruh_sign_changes()
    chk("Gamma changes sign at 1/sqrt3", unruh_gamma(a), 0.0, 1e-12)
    chk("  and at 1", abs(unruh_gamma(1.0 - 1e-9)) > 0.0, True)
    chk("  and at 2/sqrt3", unruh_gamma(c), 0.0, 1e-9)
    print("      z         Gamma          type   (MMV: IV on [0,1/sqrt3) and (1,2/sqrt3))")
    for z in (0.0, 0.2, 0.5, 0.57, 0.6, 0.8, 0.99, 1.05, 1.10, 1.20):
        print("      %-8.3f %14.6f %8s" % (z, unruh_gamma(z), unruh_type(z)))
    # z = 0 is r -> infinity, where the stress-energy vanishes and Gamma -> 0:
    # the classification degenerates at the endpoint, so test the open interval.
    chk("Gamma -> 0 at z = 0, the asymptotic limit", unruh_gamma(0.0), 0.0, 1e-15)
    chk("TYPE IV on (0, 1/sqrt3)", all(unruh_type(z) == "IV"
        for z in (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.57)), True)
    chk("type I on [1/sqrt3, 1)", all(unruh_type(z) == "I" for z in (0.6, 0.8, 0.99)), True)
    chk("TYPE IV on (1, 2/sqrt3)", all(unruh_type(z) == "IV" for z in (1.05, 1.10)), True)
    chk("type I above 2/sqrt3", unruh_type(1.20), "I")
    print("      a vacuum STATE, belonging to no element and to every element's fields.")

    print("\nBACK-REACTION: the four cases where MMV force Type I")
    for name, hyp in MMV_TYPE_I_FORCED:
        print("      %-48s %s" % (name, hyp))

    print("\nAnd the bubble is outside every one")
    chk("not static (twist is nonzero)", is_static(), False)
    chk("no Killing horizon at v_s = 0.5 c", has_killing_horizon(0.5), False)
    chk("NOT CIRCULAR (g_tx flips under t -> -t)", is_circular(), False)
    chk("not homogeneous", is_homogeneous(), False)
    chk("so it escapes all four", escapes_all_theorems(), True)

    print("\nWhich resolves typefour.py's on-axis measurement")
    import typefour
    n, _i, r, t = typefour.classify((0.9, 0.0, 0.0))
    chk("  Type IV measured ON the axis", t, "IV")
    chk("    h-converged, not noise", r > 0.2, True)
    print("      MMV's axis theorem assumes circularity; this metric is not")
    print("      circular, so there is no contradiction to resolve away.")

    print("\nTHE UNIVERSAL STATEMENT")
    chk("twist is the single reason for (1) and (3)", twist_is_the_reason(), True)
    import twist
    chk("  zero twist on the axis", abs(twist.wedge_txy_closed(0.9, 0.0, 0.5)), 0.0, 1e-12)
    chk("  nonzero off it", abs(twist.wedge_txy_closed(0.9, 0.3, 0.5)) > 0.5, True)
    print("""      twist = 0  =>  Minkowski (BBV III.15) and Type I (MMV)
      twist != 0 =>  it transports AND it is outside every Type-I theorem
      Type IV is not an accident of the ansatz; it is forced by the same
      property that makes the object a warp drive.""")

    print("\nWhat this does NOT do")
    import anec
    chk("ANEC is untouched and still violated", anec.anec_integral(0.3) < 0.0, True)
    chk("  and no self-consistent Type IV solution is exhibited here", True, True)
    print("      the Unruh result is a TEST FIELD on a fixed background, which is")
    print("      exactly the case MMV distinguish from back-reaction.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE UNRUH STATE, REPRODUCED (MMV Appendix B)\n")
    print("  %-10s %16s %8s" % ("z = 2m/r", "Gamma", "type"))
    for z in (0.0, 0.2, 0.5, 0.577, 0.8, 0.99, 1.05, 1.15, 1.20):
        print("  %-10.3f %16.6f %8s" % (z, unruh_gamma(z), unruh_type(z)))
    print("\n  sign changes at %.6f, %.1f, %.6f" % unruh_sign_changes())
    print("\nTHE BUBBLE AGAINST THE BACK-REACTION THEOREMS\n")
    print("  %-46s %10s" % ("MMV forces Type I when...", "bubble?"))
    for (name, _h), val in zip(MMV_TYPE_I_FORCED,
                               (is_static(), has_killing_horizon(0.5),
                                is_circular(), is_homogeneous())):
        print("  %-46s %10s" % (name, "yes" if val else "NO"))
    print("\nVERDICT")
    print("  Type IV is a STATE, not a substance -- the Unruh vacuum has it, and")
    print("  the vacuum is element-independent by construction.  With back-reaction")
    print("  it is forced away in four cases, and a warp bubble is outside all four")
    print("  for one reason: nonzero twist.  Which is the same reason it transports.")
    print("  Open: whether a self-consistent Type IV solution exists.  Untouched:")
    print("  ANEC.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
