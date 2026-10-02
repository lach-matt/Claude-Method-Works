#!/usr/bin/env python3
"""
spec.py -- the achievable device.  ITS FIRST SPECIFICATION IS WITHDRAWN.

M's scoping, and it is a correction to how I had been posing the problem:

    "we are over reaching.  only some of the physics are in question... in the
     case of time travel, the physics don't change, only the location within
     the same physics.  space/interstellar/dimensional travel require only the
     same physics that allow for the state of existence of the specific matter
     being transported between two destinations, nothing else."

I had been demanding that the device BEAT LIGHT -- that the corridor deliver a
negative Shapiro lead -- and every theorem in the way (Olum, Ford-Roman,
Q <= M) is a theorem about that demand.  M's scope drops it.  What is required
is that the matter exist at both ends and traverse, under the same physics.

    DROP THE LEAD.  KEEP THE SEAT.  And the seat is achievable with ordinary
    matter that satisfies every energy condition.

-- WHAT SURVIVES THE SCOPING --------------------------------------------------
From transit.py's three parts, with the lead no longer required:

    PART 1  TRAVEL   declare both endpoints at onset.  Unchanged -- it is a
                     two-point problem and the far endpoint cannot be found
                     later.
    PART 2  TURN     a conjugate point.  T_kk > 0 over a long enough stretch
                     is SUFFICIENT for one, and ordinary matter has it; Weyl
                     focusing through vacuum (below) also gives one.
                     ACHIEVABLE.

    CORRECTED (DOCKET 67).  PART 2 first read "Needs T_kk > 0", as a
    requirement.  It is necessary only in the shear-free, twist-free reduction,
    and there only as T_kk > 0 somewhere on the segment; an exact GR plane wave
    with R_kk < 0 (so T_kk < 0) has a conjugate point (computed in DOCKET 67).
    ACHIEVABLE needs only sufficiency, so it stands.
    PART 3  SEAT     the turn lands on the declared arrival.  Unchanged.

and every blocked item was attached to a requirement that is no longer made.

-- WITHDRAWN: THE B*l INVARIANT DESCRIBES A BLACK HOLE, AND THE MAGNETAR
-- FIGURE COMPARED A PEAK AGAINST A LENGTH IT DOES NOT SUSTAIN ----------------
The first version of this file specified the device as a sustained field with
B * l = 1.5456e19 T m, and quoted a magnetar as clearing it beyond 155,000 km.
BOTH ARE WRONG, in two independent ways, and both are struck.

 1. A STURM-SEATING BALL OF PRESSURELESS MATTER, SEATED ALONG ITS RADIUS, IS
    INSIDE ITS OWN SCHWARZSCHILD RADIUS.  Sturm-universal seating over a
    stretch l is certified by T_kk >= pi c^4/(4 G l^2) -- a sufficient
    condition, not a necessary one -- and T_kk = u only for pressureless matter
    along the ray.  Not being trapped needs u < 3 c^4/(8 pi G l^2) for
    M = u (4/3) pi l^3 / c^2, with l the AREAL radius and M the Misner-Sharp
    mass.  With the stretch equal to that radius, their ratio is

            u_seat / u_collapse  =  2 pi^2 / 3  =  6.579

    CONSTANT AT EVERY SCALE -- measured identical at l = 1 m, 1e5, 1e8 and
    1e11 m.  So on that class the universal (Sturm) route does not describe a
    device; it describes a trapped region, by a factor of 6.58 at every scale,
    and a trapped region cannot be static (at 2m/R = 2 pi^2/3, 1 - 2m/R =
    Gamma^2 - U^2 forces |dR/dtau| >= 2.362 c; computed in DOCKET 67).  That is a real result and it
    is kept as one, below.

    IT DOES NOT HOLD OVER EVERY BALL.  On a chord s at T_kk = (T_kk/u) u the
    ratio is (2 pi^2/3)/((T_kk/u)(s/l)^2) (specthm.sturm_ratio): 6.5797 on the
    radius and 1.6449 on a diameter for pressureless matter, 1.2337 for
    radiation on a diameter, and 0.8225 for T_kk = 2u on a diameter -- the
    value this file's own magnetic field gives a ray crossing B at right
    angles.  On a diameter the ratio is <= 1 for w >= pi^2/6 - 1 = 0.644934;
    on the radius it stays above 1 for every w the dominant energy condition
    allows (it would need w > 5.58).  So class S-2 over H_ball as written is
    OPEN in specthm (fact SR2 refused, requirement SR2 OPEN), and the figures
    are specthm.sturm_over_ball's, not retyped here.

    CORRECTED (DOCKET 67).  First written as "ANY STURM-SEATING REGION IS
    INSIDE ITS OWN SCHWARZSCHILD RADIUS.  Seating needs u >= pi c^4/(4 G l^2)
    ... it describes a black hole, by a factor of 6.58, always."  Four things
    there were wider than the computation: "needs" (Sturm is sufficient),
    u where the theorem needs T_kk, the stretch taken as the radius, and
    "black hole" where the criterion gives a trapped sphere.  The constant
    2 pi^2/3, its scale invariance, and the withdrawal of the B*l
    specification stand: on that specification's own geometry (a stretch l,
    B across the ray, T_kk = 2u) the radius ratio is pi^2/3 = 3.29 > 1, and
    WITHDRAWN 2 is independent of it.

 2. THE MAGNETAR FIGURE COMPARED A PEAK TO A SUSTAINED VALUE.  Sturm needs
    q >= m over a CONTIGUOUS length.  A vacuum dipole falls as r^-3, so a
    magnetar's 1e11 T field (the order of an equatorial spin-down dipole
    estimate) is 2.7e-2 T at 1.55e8 m -- u = 2.9e2 Pa against a requirement
    of 4.0e27 Pa, short by twenty-five orders.  It does not seat.  charge.py
    carries the same error and is struck there too.

    CORRECTED (DOCKET 67).  First written "A dipole falls as r^-3 ... 1e11 T
    surface field", with neither hypothesis of the r^-3 law named: vacuum
    outside the star, and the near zone, inside the light cylinder.  Magnetar
    magnetospheres carry currents; a twisted field B ~ r^-(2+p) leaves the
    shortfall at 10^15.8 (p = 0) to 10^20 (p = 0.5), so "twenty-five orders"
    and the selftest's "more than twenty" are the r^-3 figures.  "Does not
    seat" survives every falloff: the falloff-independent bound B l <= 2 B_s R
    is at least 10^2.8 below the invariant.

-- WHAT ACTUALLY SEATS, AND IT IS ORDINARY LENSING ----------------------------
composite.py never used the Sturm route.  It measured CUMULATIVE Weyl focusing
along a long path -- a lens -- with focal length

        f  =  b^2 / (4 M_geo)  =  b^2 c^2 / (4 G M)

which is weak-field, subject to neither error above.  Validated against a number
this project did not produce:

        THE SUN, b = R_sun:   f = 8.1919e13 m = 547.6 AU
        published solar gravitational lens focus:  ~550 AU

        lens              M (kg)      b (m)        focal
        Sun               1.989e30    6.957e8      548 AU
        Jupiter           1.898e27    7.150e7      6061 AU
        Earth             5.972e24    6.371e6      15295 AU
        10 km asteroid    2.250e15    1.000e4      1580 ly

    CORRECTED (DOCKET 67).  The Sun's focal length was first printed here as
    8.1923e13 m; focal_length() gives 8.19191e13 m (547.6 AU was always the
    code's).  The "~550 AU" is uncited and 547.6 sits 0.44 % from it; the same
    formula with the IAU nominal GM_sun gives 547.758 AU, and 1.989e30 kg is a
    4-s.f. rounding, +2.97e-4 high, inside the selftest's 1e-3 pin.  The b
    column is one unlabelled radius per body in three conventions: the Sun's
    photospheric nominal, Jupiter's equatorial, Earth's MEAN radius.  A ray
    grazing in the polar plane focuses nearer (Jupiter 5298.8 AU, Earth 15226
    AU, monopole only).  The asteroid is the file's own figure: b = 1.0e4 m,
    so its "10 km" is a radius.  Every row is a NULL-GEODESIC focus, in
    geometric optics: for the asteroid 4GM/c^2 = 6.68e-12 m, and at 500 nm the
    on-axis wave gain is 1.00013 -- no light focus.  For the Sun the gain is
    2.3e11, so no use resting on the solar row moves.

    SO THE "SEAT" THIS PROJECT HAS BEEN SPECIFYING IS GRAVITATIONAL LENSING,
    AND THE SUN ALREADY DOES IT.  It is real, ordinary, observed since 1919, and
    there are active mission concepts for the solar focus.  Calling it a device
    this project designed would be false.

-- SO WHAT IS ACTUALLY NEW HERE, STATED WITHOUT INFLATION ---------------------
Not the seat.  What this project established that was not already known:

  * WEYL FOCUSING IS SIGN-BLIND and Ricci focusing is not (composite.py) -- the
    term that made a negative source focus while leading.
  * THE SEAT/LEAD SPLIT falls exactly on the energy-condition line (charge.py).
  * REVERSAL INVARIANCE of the conjugate pair, proved and measured to 1e-14
    (transit.py) -- M's own prediction.
  * ~~ANEC VIOLATION PROTECTS ACHRONALITY (achronal.py), so the obvious escape
    from Graham-Olum is structurally unavailable.~~  STRUCK -- anecscope.py
    overturned this.  achronal.py's shear claim was INVERTED, and with it
    corrected no ray of the corridor is both ANEC-violating and achronal.
  * THE LEAD'S NEGATIVE CORE CANNOT BE HELD: the worldline QEI's duration
    bound refuses holding it for one light-crossing by 71.256 orders at b = 1 m,
    widening as b^2 (achievable.persistence_shortfall; ledger D7) -- under
    H-MMCS (massless minimally coupled free scalar), H-HADAMARD and H-FLAT, so
    no-in-practice for that field and not a theorem about all matter.
    (CORRECTED, DOCKET 67 follow-up D: first written "THE LEAD IS SHORT BY 65
    ORDERS against Ford-Roman and THE GAP WIDENS WITH SCALE" -- the census
    withdrawn by DOCKET 55 in achievable.py: Ford-Roman is a time average at one
    point, not a cap over a scale, and that figure dropped its coefficient.
    report() repeated it as "the lead is 65 orders short and widening", also
    withdrawn and replaced the same way.)
  * AND NOW: STURM-UNIVERSAL SEATING OF PRESSURELESS MATTER ALONG A BALL'S
    RADIUS IMPLIES A TRAPPED REGION, at 2 pi^2/3 exactly, at every scale.  Over
    every ball (other pressures, a diameter) it is OPEN -- see WITHDRAWN 1.
    (CORRECTED, DOCKET 67: first written "STURM-UNIVERSAL SEATING IMPLIES
    COLLAPSE", unconditionally.)

That is a real inventory and none of it is a warp drive.

-- WHAT THIS DEVICE DOES, AND WHAT IT DOES NOT --------------------------------
DOES: establish a CONJUGATE POINT at a declared range -- a whole null congruence
leaving A and reconverging -- using a sustained classical field in a vacuum
corridor, whose electromagnetic stress-energy satisfies NEC, WEC and DEC
everywhere.  Past that point the geodesic is no longer achronal, so for B
strictly past it a timelike curve from A to B exists; at the conjugate point
itself the theorem gives none.  The seating condition is SUFFICIENT, and its
universality is Sturm's: if T_kk >= pi c^4/(4 G l^2) holds over a contiguous
stretch of length l, the congruence's area radius sqrt(A) has a zero -- a
point conjugate to A -- within that closed stretch, whatever the source's
profile inside it and whatever state the congruence enters it in (Sturm
comparison against sin(pi x/l); shear only adds focusing; Einstein's equation
gives R_kk = 8 pi G T_kk/c^4 for any Lambda).  So nothing outside the stretch
can prevent the seat.  That universality is over SHAPES and entry states, not
over matter: the condition is not necessary, and the trapped-region
consequence of WITHDRAWN 1 (2 pi^2/3) is computed only for T_kk = u along a
ball's radius -- over every ball (other T_kk/u, a diameter) S-2 is OPEN in
specthm.

    CORRECTED (DOCKET 67, follow-up D).  This read "The seating condition is
    UNIVERSAL in Sturm's sense: the zero falls within the closed focusing
    stretch, so nothing outside it can prevent the seat."  After S-2 was
    seated OPEN the unqualified "UNIVERSAL" read as covering the collapse
    claim too; Sturm's universality is that of a sufficient condition over
    shapes, and the collapse holds only for T_kk = u.  The sentence was kept
    verbatim until now because specthm.py quotes it; specthm's quote and its
    "still says" clause follow at integration.

    CORRECTED (DOCKET 67).  First written "reconverging at B ... so a timelike
    curve from A to B exists", which put B AT the conjugate point, where no
    timelike curve is given; "with NEC, WEC and DEC satisfied everywhere",
    which is the result for the CLASSICAL electromagnetic field alone -- the
    quantized field violates WEC between conductors (Casimir), and the matter
    that confines a sustained field at 1e11 T holds back 3.98e27 Pa, for which
    no energy condition is checked here; and "inside the focusing stretch",
    where Sturm gives the closed stretch (the zero can fall on its end; with
    the source strictly before the stretch, as here, it is strictly inside).
    This paragraph describes the withdrawn Sturm specification; what seats is
    the lensing of DOES below.

DOES NOT: beat light.  There is no lead.  Olum (gr-qc/9805003) proves that a
superluminal path in his sense -- a causal path no other beats (his Condition
1), under the generic condition -- needs WEC (indeed NEC) violation on it.  A
lead against a reference geometry is not such a path: DOCKET 67 exhibits one
with T_ab = 0 at every point of the leading path.  A conjugate point is a
FOCUS, not a shortcut, and the timelike curve it opens is an ordinary timelike
curve.  Nothing here transports a payload faster than a signal, and nothing
here is a wormhole.  (CORRECTED, DOCKET 67: first written "by Olum there cannot
be one without negative energy", which applied the theorem to a lead.)

    THE HONEST DESCRIPTION IS A CONTROLLED GRAVITATIONAL FOCUS AT A CHOSEN
    RANGE, addressed by declaring both endpoints, built from fields that satisfy
    every energy condition.  What that is USEFUL FOR is M's question, not this
    file's, and inventing an application here would be the failure mode every
    withdrawal in this tree was about.

-- ONE TEST HALTED RATHER THAN COMPLETED, AND WHY -----------------------------
KERR-NEWMAN -- charge WITH rotation -- was begun.  The Kerr-Schild metric was
built and validated (a = 0 reduces to Schwarzschild exactly; the ergosphere sits
at x = sqrt(4+a^2), matching r = 2M exactly), and the ergoregion IS the one
place a positive-potential region is outside a horizon and in vacuum.  The
geodesic integrator then hit a coordinate singularity at the ring, and the test
was HALTED BY M's SCOPING rather than fixed: it was a hunt for a LEAD, and the
lead is no longer required.

    NOT-RUN, WITH A REASON.  It is recorded here so it is a decision rather than
    an oversight, and so that anyone reopening the lead question knows where the
    one untested door is.

stdlib only.  seatindex.py supplies the seating threshold, charge.py the fields,
transit.py the gating this specification inherits.
"""
import math, sys

# CODATA 2018 values (provenance unlabelled until DOCKET 67).  MU0 is
# superseded in CODATA 2022 by ~1e-9 relative (4.4-4.6 sigma_2018); G is
# unchanged but carries u_r = 2.2e-5, typed here without it; c is exact.
MU0 = 1.25663706212e-6
G_SI = 6.67430e-11
C_SI = 299792458.0

# 1e11 T and 1e12 T are 22.7 and 227 times the QED critical field B_c =
# 4.41e9 T, where the classical u = B^2/(2 mu_0) assumes B << B_c.  One-loop
# Euler-Heisenberg shifts u by -9.57e-4 at 1e11 T (inside the 1e-3 check
# below, by 1.3e-5) and keeps NEC, WEC and DEC (DOCKET 67, on an unread
# one-loop form).
FIELDS = (
    ("continuous lab magnet", 45.0),
    ("destructive pulsed", 1.2e3),
    ("theoretical material limit", 1.0e4),
    ("neutron star surface", 1.0e8),
    ("magnetar", 1.0e11),
    ("magnetar interior (est.)", 1.0e12),
)
BEST_HUMAN_FIELD = 1.2e3
LIGHT_YEAR = 9.4607e15


def seating_invariant():
    """B * l = sqrt(2 mu_0 pi c^4/4G).  ARITHMETICALLY CORRECT AND WITHDRAWN AS
    A SPECIFICATION.  It feeds u = B^2/(2 mu_0) to a threshold seatindex puts
    on T_kk; for a pure magnetic field T_kk = 2u sin^2(theta) -- 0 along B, 2u
    across -- so the invariant would read 1.0929e19 T m with B across the ray,
    and no finite value along it (DOCKET 67).  With B across, the region is
    still trapped on its own radius (pi^2/3 = 3.29 > 1); along B it does not
    seat at all; and WITHDRAWN 2 stands apart from it.  Kept executable so the retraction is checkable.
    (CORRECTED, DOCKET 67: first said "inside its own Schwarzschild radius by
    2 pi^2/3", the T_kk = u figure.)"""
    import seatindex
    return math.sqrt(2.0 * MU0 * seatindex.T_COEFF)


def range_for_field(B):
    """Where a sustained field B seats.  l = invariant / B."""
    return seating_invariant() / B


def field_for_range(l):
    return seating_invariant() / l


def q_of(u):
    """The Jacobi potential q = (4 pi G/c^4) T_kk, in 1/m^2.  The argument is
    named u but must be T_kk: equal to the energy density only for
    pressureless matter along the ray; a magnetic field gives 2u sin^2(alpha)
    (DOCKET 67)."""
    return 4.0 * math.pi * G_SI / C_SI ** 4 * u


def conjugate_length_from_q(u):
    """pi/sqrt(q) -- the independent route to the same range, under its own
    hypotheses: POINT initial data (G(0) = 0, G'(0) = 1), q constant over the
    stretch, zero shear.  An initially parallel congruence focuses at half of
    it; with q >= q0 and shear it is an upper bound (DOCKET 67)."""
    return math.pi / math.sqrt(q_of(u))


def energy_density(B):
    return B * B / (2.0 * MU0)


def engineering_gap(B_target=1.0e11, B_have=BEST_HUMAN_FIELD):
    """Field ratio and energy-density ratio.  Against no theorem.  The
    target, 1e11 T, is 22.7 B_c, past the B << B_c the classical u assumes
    (see FIELDS)."""
    return B_target / B_have, (B_target / B_have) ** 2


DOES = (
    "establish a conjugate point at a declared range, by CUMULATIVE weak-field "
    "lensing -- f = b^2 c^2/(4 G M), a null-geodesic focus in geometric optics, "
    "not the Sturm condition, which is withdrawn",
    "using ordinary positive mass; the corridor is vacuum, where NEC/WEC/DEC "
    "hold trivially (the lens's own matter is checked by no owner cited here: "
    "charge.em_is_ordinary tests EM stress-energy only)",
    "with both endpoints declared at onset, per transit.py's gating",
    "past the conjugate point the geodesic is not achronal, so a timelike "
    "curve A->B exists",
    "and the Sun already does exactly this, focusing a source at infinity at "
    "548 AU (a null-geodesic focus, geometric optics; the point conjugate to a "
    "source at finite D_A lies f D_A/(D_A - f) beyond the lens, none if "
    "D_A <= f)",
)
DOES_NOT = (
    "constitute a new device -- this IS gravitational lensing, known since 1919",
    "beat light -- there is no lead; Olum's theorem needs negative energy for a "
    "path no other causal path beats, not for a lead against a reference "
    "geometry",
    "shortcut -- a conjugate point is a FOCUS, not a wormhole",
    "transport a payload faster than a signal",
    "require any exotic matter anywhere",
)
HALTED = {
    "Kerr-Newman (charge with rotation)":
        "metric built and validated; integrator hit the ring singularity; "
        "HALTED by scoping because it was a hunt for a LEAD, which is no "
        "longer required. The one untested door if the lead is reopened.",
}


MU0_ = MU0


def collapse_bound(l):
    """u below which a uniform ball of AREAL radius l (M its Misner-Sharp mass,
    u (4/3) pi l^3/c^2) is not inside its Schwarzschild radius."""
    return 3.0 * C_SI ** 4 / (8.0 * math.pi * G_SI * l * l)


def seat_over_collapse(l):
    """u_seat / u_collapse, with T_kk = u and the stretch equal to the radius.
    Constant 2 pi^2/3 = 6.579 at every scale.  Other cases: specthm.sturm_ratio."""
    import seatindex
    return seatindex.tkk_required(l) / collapse_bound(l)


def dipole_field(B_surface, R, r):
    """A VACUUM dipole, in the near zone, falls as r^-3.  This is what the
    magnetar claim ignored.  A magnetosphere carrying currents falls more
    slowly (B ~ r^-(2+p)); 'does not seat' survives every falloff (DOCKET
    67)."""
    return B_surface * (R / r) ** 3


def focal_length(M_kg, b):
    """f = b^2 c^2/(4 G M).  The WEAK-FIELD route, and the one that is real."""
    return b * b * C_SI ** 2 / (4.0 * G_SI * M_kg)


# b is one radius per body in three conventions (Sun photospheric nominal,
# Jupiter equatorial, Earth mean); the asteroid's b = 1.0e4 m makes its
# '10 km' a radius.  M_sun is a 4-s.f. rounding, +2.97e-4 high (DOCKET 67).
LENSES = (("Sun", 1.989e30, 6.957e8), ("Jupiter", 1.898e27, 7.15e7),
          ("Earth", 5.972e24, 6.371e6), ("10 km asteroid", 2.25e15, 1.0e4))
AU = 1.495979e11


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-56s %18.6g %18.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("WITHDRAWN 1 -- Sturm seating, T_kk = u along the radius, is TRAPPED")
    print("     %10s %16s %16s %10s" % ("l (m)", "u seat", "u collapse", "ratio"))
    for l in (1.0, 1.0e5, 1.0e8, 1.0e11):
        import seatindex
        print("     %10.0e %16.4e %16.4e %10.3f"
              % (l, seatindex.tkk_required(l), collapse_bound(l), seat_over_collapse(l)))
    near("the ratio is 2 pi^2/3", seat_over_collapse(1.0), 2.0 * math.pi ** 2 / 3.0, 1e-9)
    chk("and it is the SAME at every scale",
        all(abs(seat_over_collapse(l) / seat_over_collapse(1.0) - 1.0) < 1e-12
            for l in (1e5, 1e8, 1e11)), True)
    # T_kk = u, stretch = radius.  Over H_ball as written (other pressures, a
    # diameter) the ratio is specthm.sturm_ratio's and S-2 is OPEN (DOCKET 67).
    chk("so a T_kk = u Sturm ball (radius) is inside its Schwarzschild radius",
        seat_over_collapse(1.0) > 1.0, True)

    print("\nWITHDRAWN 2 -- the magnetar figure was a PEAK against a SUSTAINED need")
    import seatindex
    B_far = dipole_field(1.0e11, 1.0e4, 1.5456e8)
    u_far = B_far ** 2 / (2.0 * MU0)
    print("     dipole 1e11 T at R=1e4 m gives %.3e T at 1.55e8 m" % B_far)
    print("     u = %.3e Pa against a requirement of %.3e Pa"
          % (u_far, seatindex.tkk_required(1.5456e8)))
    # The r^-3 (vacuum, near-zone) figure, with the far end at r from the
    # star's centre rather than R + l (6e-5 relative).  A twisted field
    # B ~ r^-(2+p) gives 10^15.8 to 10^20; "does not seat" holds for every
    # falloff (DOCKET 67).
    chk("short by more than twenty orders (pure r^-3 dipole)",
        u_far / seatindex.tkk_required(1.5456e8) < 1e-20, True)

    print("\nWHAT ACTUALLY SEATS -- ordinary lensing, f = b^2 c^2/(4 G M)")
    near("the SOLAR lens focus, in AU", focal_length(1.989e30, 6.957e8) / AU,
         547.6, 1e-3)
    print("     published solar gravitational lens focus is ~550 AU (uncited;")
    print("     547.6 is 0.44 % from it; the IAU nominal GM_sun gives 547.758).")
    print("     %18s %14s %14s" % ("lens", "focal (m)", "AU"))
    for tag, M, b in LENSES:
        f = focal_length(M, b)
        print("     %18s %14.4e %14.4g" % (tag, f, f / AU))
    # The invariant scales as G^-1/2, so this 1e-4 pin trips at dG/G ~ 2e-4:
    # through spec's selftest return code it is the one route by which G
    # reaches a specthm class verdict (S-1) (DOCKET 67).  G's own u_r is
    # 2.2e-5, ten times inside it.
    chk("the invariant is kept executable so the retraction is checkable",
        abs(seating_invariant() / 1.54562e19 - 1.0) < 1e-4, True)

    print("\nWHAT IT DOES")
    for d in DOES:
        print("     + %s" % d)
    print("\nWHAT IT DOES NOT")
    for d in DOES_NOT:
        print("     - %s" % d)
    chk("five things it does", len(DOES), 5)
    chk("five it does not", len(DOES_NOT), 5)

    print("\nCONSISTENCY with the instruments this inherits from")
    # turnseat.py, NOT transit.py: the travel>turn>seat instrument was overwritten
    # by an unrelated file of the same name. Recovered from git as turnseat.py.
    import seatindex, charge
    import turnseat as transit
    # seatindex's threshold is on T_kk; energy_density is u.  Equal only for
    # T_kk = u (for a magnetic field T_kk = 2u sin^2 theta), and the classical u
    # at 1e11 T (22.7 B_c) is 9.57e-4 above the one-loop value, 1.3e-5 inside
    # the 1e-3 tolerance (DOCKET 67).
    near("seatindex's universal threshold at 1.5456e8 m",
         seatindex.tkk_required(1.5456e8), energy_density(1.0e11), 1e-3)
    # EM stress-energy only (classical field); not a check on the lens's matter.
    chk("charge.py: EM stress-energy is ordinary", charge.em_is_ordinary(), True)
    chk("transit.py still gates on both endpoints",
        transit.part2(transit.Conditions(1.0, arrival_length=None))[0], transit.BLOCKED)

    print("\nHALTED, NOT UNRUN")
    for k, v in HALTED.items():
        print("     %s" % k)
        print("       %s" % v)
    chk("one halted test, recorded with its reason", len(HALTED), 1)

    print("\nDOCKET 67 FOLLOW-UP D -- stale text, guarded")
    import inspect, achievable
    doc = " ".join(__doc__.split())
    chk("DOES scopes Sturm's universality to a sufficient condition over shapes",
        "The seating condition is SUFFICIENT, and its universality is Sturm's" in doc, True)
    chk("  and the collapse to T_kk = u along a radius (S-2 OPEN over every ball)",
        "computed only for T_kk = u along a ball's radius" in doc, True)
    chk("  the unqualified sentence survives only inside its CORRECTED note",
        doc.count("UNIVERSAL in Sturm's sense") == 1
        and "CORRECTED (DOCKET 67, follow-up D). This read \"The seating condition is "
            "UNIVERSAL in Sturm's sense" in doc, True)
    chk("report() no longer prints the withdrawn '65 orders'",
        "65 orders" in inspect.getsource(report), False)
    chk("  CONTROL: the withdrawn line is kept, marked, in the docstring",
        "report() repeated it as \"the lead is 65 orders short and widening\", also "
        "withdrawn" in doc, True)
    near("the figure it prints instead: duration shortfall at 1 m (orders)",
         math.log10(achievable.persistence_shortfall(1.0)), 71.256, 1e-4)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SPECIFICATION")
    print("\n  B * l  =  %.5e  T m        (one invariant, no free parameters)"
          % seating_invariant())
    print("\n  %28s %10s %16s %12s" % ("field source", "B (T)", "seats beyond (m)", "ly"))
    for tag, B in FIELDS:
        l = range_for_field(B)
        print("  %28s %10.3g %16.4e %12.3e" % (tag, B, l, l / LIGHT_YEAR))
    gb, gu = engineering_gap()
    print("\n  Gap to magnetar class from the best human field (1200 T):")
    print("    %.3e in field, %.3e in energy density -- against NO THEOREM." % (gb, gu))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  THE FIRST SPECIFICATION IN THIS FILE IS WITHDRAWN, twice over: a")
    print("  Sturm-seating ball, T_kk = u along its radius, is inside its own")
    print("  Schwarzschild radius by 2 pi^2/3 = 6.579 at EVERY scale (over every")
    print("  ball, S-2 is OPEN), and the magnetar figure compared a vacuum")
    print("  dipole's peak against a length it does not sustain, missing by")
    print("  twenty-five orders.")
    print("\n  WHAT ACTUALLY SEATS IS CUMULATIVE WEAK-FIELD LENSING,")
    print("  f = b^2 c^2/(4 G M), validated against the solar focus at 547.6 AU")
    print("  where the cited value is ~550.  That is gravitational lensing,")
    print("  it is ordinary, it has been known since 1919, and the Sun does it.")
    print("  Calling it a device this project designed would be false.")
    print("\n  WHAT IS ACTUALLY NEW is in the header's inventory: Weyl focusing")
    print("  is sign-blind, the seat/lead split is the energy-condition line,")
    # CORRECTED (DOCKET 67 follow-up D): the lines below printed the Ford-Roman
    # figure withdrawn by DOCKET 55 (verbatim in the docstring's inventory
    # note); they now print the duration bound's, computed by achievable.py.
    import achievable
    print("  reversal invariance holds to 1e-14, the lead's negative core cannot")
    print("  be held one light-crossing -- %.3f orders short on the DURATION axis"
          % math.log10(achievable.persistence_shortfall(1.0)))
    print("  at b = 1 m, widening as b^2 (massless minimal scalar, Hadamard, flat;")
    print("  not a theorem about all matter) -- and Sturm-universal seating of")
    print("  pressureless matter along a ball's radius implies a trapped region.")
    print("  None of it is a warp drive.")
    print("  (The header's ANEC-protects-achronality line is STRUCK: anecscope.py")
    print("  overturned it.)")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
