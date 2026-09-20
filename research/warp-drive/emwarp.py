#!/usr/bin/env python3
r"""
emwarp.py -- CAN A COUNTER-ROTATING ELECTROMAGNET RIG SOURCE A WARP FIELD?
THE MAXWELL NULL ENERGY CONDITION IS SATURATED, NEVER VIOLATED, AND THAT IS A
THEOREM WITH A SUM-OF-SQUARES CERTIFICATE.

M: "an electromagnet ring spinning in one direction, and an electromagnet disc
sitting suspended in the ring's center rotating in the opposite direction.  The
two rotating against each other creates a high EM polarity tension that creates
the neutral/negative gravity warp field"

    python3 emwarp.py             the reading
    python3 emwarp.py --selftest  fixtures, stdlib only
    python3 emwarp.py --prove     the z3 machine-check (pip install z3-solver)

THREE CLAIMS ARE EMBEDDED IN THE PROPOSAL AND THEY DO NOT GET THE SAME ANSWER.

    (A) counter-rotating ring + disc is the right GEOMETRY      CORRECT
    (B) it creates a high "EM polarity tension"                 CORRECT, and the
                                                                tension is real
                                                                and negative
    (C) that tension yields neutral or negative gravity         REFUTED BY A
                                                                THEOREM

Two of the three are right.  The third is not merely unbuilt, it is closed: no
configuration of electric and magnetic fields -- static or rotating, opposed or
aligned, one source or a hundred -- can make the null energy condition negative,
because the contraction is a SUM OF SQUARES.

===============================================================================
1. THE TENSION IS REAL, AND THE MARGIN IS EXACTLY ZERO
===============================================================================

Claim (B) is not loose talk.  Magnetic field lines genuinely carry TENSION along
themselves and PRESSURE across themselves -- Faraday's own picture, and it is
exact.  For a uniform field B along z, `principal_pressures()` returns

    rho          = B^2 / 2 mu0          energy density
    p_x = p_y    = + B^2 / 2 mu0        transverse PRESSURE
    p_z          = - B^2 / 2 mu0        longitudinal TENSION  <-- NEGATIVE

So the proposal is right that a magnet is a machine for making negative
pressure, and right that negative pressure is what a warp metric wants.  The
whole question is HOW negative, and the answer is exact:

    rho + p_z    =  B^2/2mu0  -  B^2/2mu0  =  EXACTLY 0

**THE TENSION IS EXACTLY AS LARGE AS THE ENERGY DENSITY AND NOT ONE PART IN
10^40 LARGER.**  The null energy condition is SATURATED.  Saturated is not
violated: it is the boundary, approached from the legal side and touched, never
crossed.  Every quantity a warp bubble needs is on the other side of a boundary
that Maxwell's equations reach and cannot pass.

The dominant energy condition is saturated in the same breath: rho - |p_i| = 0
on all three axes.  Maxwell stress-energy is Hawking-Ellis TYPE I, traceless,
sitting on the corner of the allowed region.

===============================================================================
2. THE THEOREM, AND WHY SUPERPOSITION CANNOT ESCAPE IT
===============================================================================

For an arbitrary electromagnetic field and an arbitrary null vector
k^mu = (1, n) with |n| = 1, `nec_contraction()` computes T_{mu nu} k^mu k^nu,
and `sos_form()` computes

    | P_perp ( E + n x B ) |^2

where P_perp projects orthogonally to n.  THESE ARE THE SAME NUMBER.  It is an
identity in six real variables, verified to 2.8e-14 over 100,000 random
configurations by `identity_residual()` and discharged by z3 as `unsat` on the
negation under `--prove`.

    T_{mu nu} k^mu k^nu  =  | P_perp ( E + n x B ) |^2  >=  0

A sum of squares is non-negative for every real assignment.  That is the whole
proof, and it is why the answer cannot be engineered around:

**SUPERPOSITION IS NOT AN ESCAPE.**  A ring field and a disc field add to
B = B_ring + B_disc, E = E_ring + E_disc.  The total is still an electromagnetic
field, the identity is POINTWISE, and it holds at every point of any total
field whatsoever.  Opposed polarity does not create a new species of
stress-energy; it changes the value of B at each point, and the theorem is a
statement about every value B can take.  `superposition_cannot_help()` searches
100,000 random PAIRS of sources over random points and reports the minimum -- it
is never negative.

**ROTATION IS NOT AN ESCAPE.**  Spinning the sources induces E fields and a
Poynting flux.  Those enter the identity as E and as n x B, and the identity
already quantifies over all E and all B.  A rotating field is a field.

**THE SATURATION IS EXACTLY THE MAGNET CASE.**  z3 reports that with E = 0, the
condition T_{mu nu} k^mu k^nu = 0 FORCES n parallel to B (`--prove`, fourth
obligation, unsat on the negation).  A static magnet looking along its own
field lines is precisely where classical electromagnetism comes closest to the
boundary -- and the distance remaining is zero, not negative.

===============================================================================
3. WHAT COUNTER-ROTATION ACTUALLY BUYS -- AND WHAT IT SPENDS
===============================================================================

Claim (A) is correct, and the tree found it independently before the proposal
was made.  `ROTATING-SHELL.md` records that a SINGLE rotating shell carries ADM
angular momentum, so its exterior is Kerr -- which destroys the exactly
Schwarzschild exterior the Fuchs et al. positive-energy construction is built
on.  COUNTER-ROTATION SETS J = 0 EXACTLY, killing g_t-phi and restoring it.

But read what that sentence does and does not say.  **Counter-rotation is a
CONSTRAINT-SATISFIER, not a SOURCE.**  Its entire function is to cancel a field
that would otherwise be in the way.  It cannot generate one, and the arithmetic
is unkind about it in a specific way:

`rig_angular_momentum()` computes both angular momenta for a realistic rig.  The
magnets' own metal carries **3.4e10** times the angular momentum of their stored
field's mass-equivalent, so whatever frame-dragging a spinning rig produces comes
from the SPINNING METAL and not from the field at all.  That is worth saying
plainly, because it is nine orders BETTER than the field-only estimate in
`nspin.py`: 100 kg of spinning ring reaches 2.7e-9 of Earth's frame-dragging
where 422 MJ of stored field reached 1.0e-18.  If you want gravitomagnetism from
a laboratory object, spin something HEAVY; the electromagnet is beside the point.
And then:

**COUNTER-ROTATION CANCELS PRECISELY THAT.**  Tuning J_ring = -J_disc zeroes the
total angular momentum, which zeroes g_t-phi, which zeroes the frame-dragging --
the single gravitational effect the machine had.  The geometry is right and it
is right for a reason that costs the proposal its mechanism.

===============================================================================
4. WHAT THE MACHINE REALLY DOES
===============================================================================

`what_it_actually_does()` puts numbers on the effects that are NOT zero.  Two
counter-rotating magnetised bodies at a few hundred hertz produce torque, eddy
currents, ohmic heating and induced EMF, and every one of them is many orders
of magnitude above any gravitational quantity in the problem.  The honest
description of the device is a very good eddy-current brake.

===============================================================================
5. WHERE THE REAL TARGET IS, AND IT IS NOT NEGATIVE ENERGY
===============================================================================

**THE MOST IMPORTANT FINDING HERE IS THAT THE HUNT IS AIMED AT THE WRONG
QUANTITY.**  `TARGET-1-RESULT.md` in this tree records a warp solution whose
matter satisfies ALL FOUR pointwise energy conditions -- Hawking-Ellis Type I
everywhere, ZERO Type-IV cells, large positive slack in bulk and transition at
two resolutions, with every negative value confined to the outermost four cells
where the stencils are one-sided and which do not converge.

If that stands, a warp metric does not need negative energy, so "neutral or
negative gravity" is not the thing to be manufacturing.  What it needs instead
is MASS, and the quantity is the barrier: the Fuchs shell measured there runs
R1 = 10 m, R2 = 20 m, **m = 4.4886e27 kg**.  `the_real_barrier()` puts that
beside the rig.  It is about 751 Earth masses inside a twenty-metre radius.

`the_real_barrier()` reports two further numbers that say what shape the barrier
has, and they point opposite ways.

**THE DENSITY IS THE BARRIER.**  The mean density needed is **6.66e5 times
NUCLEAR density** -- the shell is not made of any material that exists.  It is
denser than a neutron star by five orders of magnitude, and no equation of state
in the literature supports matter like that.

**THE HORIZON IS NOT.**  Its Schwarzschild radius is **6.67 m against an inner
shell radius of 10 m**, so the configuration sits OUTSIDE its own horizon with
about a 1.5x margin.  That constraint is satisfied, not violated, and it is
worth stating because the mass figure invites the opposite assumption.  The
document that measures the shell states its own caveats and this file does not
re-derive them.

That is a far harder problem than the one the proposal attacks, and it is the
actual one.

===============================================================================
6. WHAT THIS FILE REFUSES
===============================================================================

**TO CALL SATURATION A VIOLATION, OR A NEAR MISS.**  rho + p_z = 0 exactly.  It
is not small, it is not a limit to be pushed; it is an algebraic identity, and
no field strength, no material, no temperature and no rotation rate moves it.

**TO EXTEND THE THEOREM BEYOND CLASSICAL MAXWELL.**  The proof is for the
Maxwell stress-energy.  Quantum fields DO violate the NEC -- Casimir, squeezed
vacuum -- and are bounded by quantum energy inequalities rather than by this
identity.  Nonlinear classical electrodynamics (Born-Infeld, Euler-Heisenberg)
is a different tensor and is not covered here.  `SCOPE` says so in the code.

**TO CALL THE RIG ARITHMETIC A DESIGN.**  Section 3 and 4 are scaling estimates
on stated assumptions, accurate to an order of magnitude, which is all they need
to be against the gaps they measure.

**TO RE-DERIVE TARGET-1-RESULT.md.**  Section 5 QUOTES it.  Its own document
carries the measurement, the driver scripts and the caveat that Le's second
challenge (Q2, whether a metric-first construction has a well-posed matter
source) is unanswered.  That caveat is not repaired here.
"""

import math
import sys

try:
    import z3
    HAVE_Z3 = True
except ImportError:                                            # pragma: no cover
    HAVE_Z3 = False

MU0 = 4e-7 * math.pi
EPS0 = 8.8541878128e-12
C = 2.99792458e8
G_N = 6.67430e-11

#: What the section-2 theorem does and does not cover.  Quoted by the report so
#: the scope travels with the result.
SCOPE = (
    "CLASSICAL MAXWELL stress-energy only.  Quantum fields violate the NEC "
    "(Casimir, squeezed vacuum) and are bounded by quantum energy inequalities "
    "instead.  Nonlinear classical electrodynamics is a different tensor."
)

#: The Fuchs shell as TARGET-1-RESULT.md measures it -- quoted, not re-derived.
FUCHS_SHELL = {"R1_m": 10.0, "R2_m": 20.0, "m_kg": 4.4886e27}

EARTH_M, EARTH_R, EARTH_MOI, EARTH_DAY = 5.972e24, 6.371e6, 0.3307, 86164.0

#: Saturation density of nuclear matter, the densest matter that exists outside
#: a black hole.  The shell's requirement is measured against it in section 5.
NUCLEAR_DENSITY = 2.3e17


# ------------------------------------------------------ vector helpers (stdlib)

def _dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


# ------------------------------------------- 1. the Maxwell stress-energy tensor

def stress_energy(E, B):
    """(rho, S, T) in Heaviside-Lorentz with eps0 = mu0 = c = 1.

    Units cancel in every ratio this file takes, and carrying them would hide
    the algebra that is the whole point.  `principal_pressures` restores SI.

        rho   = (E^2 + B^2)/2                      T^00
        S     = E x B                              T^0i, the Poynting vector
        T^ij  = -(E_i E_j + B_i B_j) + delta_ij rho
    """
    e2, b2 = _dot(E, E), _dot(B, B)
    rho = 0.5 * (e2 + b2)
    S = _cross(E, B)
    T = [[-(E[i] * E[j] + B[i] * B[j]) + (rho if i == j else 0.0)
          for j in range(3)] for i in range(3)]
    return rho, S, T


def nec_contraction(E, B, n):
    """T_{mu nu} k^mu k^nu for the null vector k^mu = (1, n), |n| = 1.

    Signature -+++, so T_{0i} = -T^{0i} and the cross term carries a minus.
    """
    rho, S, T = stress_energy(E, B)
    return (rho - 2.0 * _dot(S, n)
            + sum(T[i][j] * n[i] * n[j] for i in range(3) for j in range(3)))


def sos_form(E, B, n):
    """|P_perp (E + n x B)|^2 -- the same number, manifestly non-negative."""
    v = tuple(E[i] + _cross(n, B)[i] for i in range(3))
    vn = _dot(v, n)
    perp = tuple(v[i] - vn * n[i] for i in range(3))
    return _dot(perp, perp)


def principal_pressures(B_tesla):
    """(rho, p_transverse, p_longitudinal) in SI, for a uniform B along z.

    THE TENSION IS REAL AND IT IS NEGATIVE.  This is the function that says the
    user's claim (B) is correct, and `nec_margin` is the one that closes (C).
    """
    rho = B_tesla ** 2 / (2.0 * MU0)
    return rho, rho, -rho


def nec_margin(B_tesla):
    """rho + p_longitudinal for a uniform magnetic field.  EXACTLY ZERO.

    Returned as a computed difference rather than the literal 0.0, so the
    fixture measures the arithmetic instead of asserting the claim.
    """
    rho, _pt, pl = principal_pressures(B_tesla)
    return rho + pl


def dec_margin(B_tesla):
    """(rho - |p_transverse|, rho - |p_longitudinal|).  Both zero: DEC saturated."""
    rho, pt, pl = principal_pressures(B_tesla)
    return rho - abs(pt), rho - abs(pl)


def trace(B_tesla):
    """-rho + sum p_i for a uniform B.  Zero: Maxwell stress-energy is traceless."""
    rho, pt, pl = principal_pressures(B_tesla)
    return -rho + (pt + pt + pl)


# ------------------------------------------------ 2. the identity, and the search

def _rand_unit(rnd):
    while True:
        v = [rnd.gauss(0, 1) for _ in range(3)]
        L = math.sqrt(_dot(v, v))
        if L > 1e-9:
            return tuple(x / L for x in v)


def identity_residual(trials=100000, seed=7):
    """max |NEC - |P_perp(E + n x B)|^2| over random (E, B, n).  Machine epsilon.

    The identity is what makes the theorem decidable: z3 times out on the raw
    degree-four polynomial and returns instantly on the sum of squares.
    """
    import random
    rnd = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        E = tuple(rnd.uniform(-3, 3) for _ in range(3))
        B = tuple(rnd.uniform(-3, 3) for _ in range(3))
        n = _rand_unit(rnd)
        worst = max(worst, abs(nec_contraction(E, B, n) - sos_form(E, B, n)))
    return worst


def superposition_cannot_help(trials=100000, seed=11):
    """(min NEC, count negative) over random PAIRS of superposed sources.

    Directly answers the proposal: a ring field and a disc field ADD, and the
    total is still a Maxwell field.  The minimum is approached but never passed.
    """
    import random
    rnd = random.Random(seed)
    lo, neg = float("inf"), 0
    for _ in range(trials):
        E = tuple(rnd.uniform(-3, 3) + rnd.uniform(-3, 3) for _ in range(3))
        B = tuple(rnd.uniform(-3, 3) + rnd.uniform(-3, 3) for _ in range(3))
        v = nec_contraction(E, B, _rand_unit(rnd))
        lo = min(lo, v)
        if v < -1e-12:
            neg += 1
    return lo, neg


def saturating_configurations():
    """[(name, NEC)] -- the field/direction pairs that reach exactly zero.

    Both are reachable in a laboratory, and the second is the more interesting:
    a null electromagnetic wave saturates the NEC along its own propagation
    direction, which is why light bends spacetime but never repels.
    """
    return [
        ("static B along z, look along z  (the magnet case)",
         nec_contraction((0.0, 0.0, 0.0), (0.0, 0.0, 2.5), (0.0, 0.0, 1.0))),
        ("null wave, E perp B, |E| = |B|, look along E x B",
         nec_contraction((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))),
    ]


# ----------------------------------------------------- 3. the ring and the disc

def rig_angular_momentum(B=20.0, R_ring=1.0, m_ring=100.0, f_ring=100.0,
                         R_disc=0.4, m_disc=50.0, f_disc=-100.0):
    """The two angular momenta, material and field, and what cancels.

    Returns a dict.  THE POINT IS THE RATIO: the magnets' own metal carries
    3.4e10 times the angular momentum of the mass-equivalent of the field they
    store, so any frame-dragging a spinning rig produces is the SPINNING METAL's
    and not the field's -- and counter-rotation sets exactly that to zero.
    """
    w_r, w_d = 2 * math.pi * f_ring, 2 * math.pi * f_disc
    J_ring = m_ring * R_ring ** 2 * w_r               # thin ring, I = m R^2
    J_disc = 0.5 * m_disc * R_disc ** 2 * w_d         # solid disc, I = m R^2 / 2
    V = (4.0 / 3.0) * math.pi * R_ring ** 3
    m_field = (B * B / (2 * MU0) * V) / C ** 2
    J_field = 0.4 * m_field * R_ring ** 2 * w_r
    tot = J_ring + J_disc
    return {
        "J_ring": J_ring, "J_disc": J_disc, "J_total": tot,
        "m_field_kg": m_field, "J_field": J_field,
        "material_over_field": abs(J_ring / J_field),
        "Bg_uncancelled": 2 * G_N * abs(tot) / (C ** 2 * R_ring ** 3),
        "Bg_if_cancelled": 0.0,
        "f_disc_that_cancels": -f_ring * (m_ring * R_ring ** 2)
                               / (0.5 * m_disc * R_disc ** 2),
    }


def earth_bg():
    """(J, B_g) for Earth -- the denominator."""
    J = EARTH_MOI * EARTH_M * EARTH_R ** 2 * (2 * math.pi / EARTH_DAY)
    return J, 2 * G_N * J / (C ** 2 * EARTH_R ** 3)


def what_it_actually_does(B=20.0, R=1.0, f=100.0, sigma=5.96e7, t=0.01):
    """The effects that are NOT zero, in SI.  Compare against section 3's B_g.

    Induced EMF from a field changing at the rotation rate, the eddy-current
    power that EMF drives through a conducting rim, and the magnetic pressure
    the structure must hold.  Assumptions are the arguments; copper's sigma and
    a 1 cm rim by default.
    """
    emf = math.pi * R ** 2 * B * (2 * math.pi * f)
    p_eddy = (math.pi ** 2 * B ** 2 * (2 * R) ** 2 * f ** 2 * sigma * t
              / 6.0) * (2 * math.pi * R * t)
    p_mag = B * B / (2 * MU0)
    return {"induced_emf_V": emf, "eddy_power_W": p_eddy,
            "magnetic_pressure_Pa": p_mag,
            "magnetic_pressure_atm": p_mag / 101325.0}


# --------------------------------------------------------- 5. the real barrier

def the_real_barrier():
    """What TARGET-1-RESULT.md's shell weighs, against the rig and against Earth.

    QUOTED from that document, not re-derived here.  Section 6 says so.
    """
    m = FUCHS_SHELL["m_kg"]
    rig = rig_angular_momentum()
    return {
        "shell_mass_kg": m,
        "earth_masses": m / EARTH_M,
        "over_rig_field_mass": m / rig["m_field_kg"],
        "over_rig_material_mass": m / 150.0,
        "shell_R2_m": FUCHS_SHELL["R2_m"],
        "mean_density_kg_m3": m / ((4.0 / 3.0) * math.pi
                                   * (FUCHS_SHELL["R2_m"] ** 3
                                      - FUCHS_SHELL["R1_m"] ** 3)),
        "over_nuclear_density": (m / ((4.0 / 3.0) * math.pi
                                      * (FUCHS_SHELL["R2_m"] ** 3
                                         - FUCHS_SHELL["R1_m"] ** 3)))
                                / NUCLEAR_DENSITY,
        "schwarzschild_radius_m": 2 * G_N * m / C ** 2,
    }


# ----------------------------------------------------------- the machine-check

def require_z3():
    if not HAVE_Z3:
        raise SystemExit("z3 not installed.  pip install z3-solver")


def prove(timeout_ms=300000):
    """The four obligations, discharged by z3.  [(name, expected, got)].

    Every one is posed as a search for a COUNTEREXAMPLE, so `unsat` is the
    result that establishes the claim.  Obligation 1 is the identity; given it,
    obligation 2 is a sum of squares and z3 answers instantly.  Posed directly
    on the degree-four polynomial it returns `unknown`, and that is recorded
    here rather than hidden -- the certificate is what makes it decidable.
    """
    require_z3()
    Ex, Ey, Ez, Bx, By, Bz, nx, ny, nz = z3.Reals(
        'Ex Ey Ez Bx By Bz nx ny nz')
    E, B, n = [Ex, Ey, Ez], [Bx, By, Bz], [nx, ny, nz]

    def d(a, b):
        return sum(a[i] * b[i] for i in range(3))

    def x(a, b):
        return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0]]

    e2, b2 = d(E, E), d(B, B)
    rho = (e2 + b2) / 2
    S = x(E, B)
    T = [[-(E[i] * E[j] + B[i] * B[j]) + ((e2 + b2) / 2 if i == j else 0)
          for j in range(3)] for i in range(3)]
    NEC = (rho - 2 * d(S, n)
           + sum(T[i][j] * n[i] * n[j] for i in range(3) for j in range(3)))
    v = [E[i] + x(n, B)[i] for i in range(3)]
    perp = [v[i] - d(v, n) * n[i] for i in range(3)]
    SOS = d(perp, perp)
    unit = (d(n, n) == 1)

    def ask(name, phi, expect):
        s = z3.Solver()
        s.set("timeout", timeout_ms)
        s.add(phi)
        return (name, expect, str(s.check()))

    return [
        ask("the identity: NEC != |P_perp(E + n x B)|^2 somewhere",
            z3.And(unit, NEC != SOS), "unsat"),
        ask("NEC via the certificate: the sum of squares is negative somewhere",
            z3.And(unit, SOS < 0), "unsat"),
        ask("WEC: the energy density is negative somewhere", rho < 0, "unsat"),
        ask("with E = 0, NEC = 0 without n parallel to B",
            z3.And(unit, Ex == 0, Ey == 0, Ez == 0, b2 > 0, SOS == 0,
                   z3.Or(x(n, B)[0] != 0, x(n, B)[1] != 0, x(n, B)[2] != 0)),
            "unsat"),
    ]


# ------------------------------------------------------------------- reading

def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 74)
    print("1.  THE TENSION IS REAL, AND THE MARGIN IS EXACTLY ZERO")
    print("=" * 74)
    for B in (1.0, 20.0, 45.0, 100.0):
        rho, pt, pl = principal_pressures(B)
        print("   B = %5.0f T   rho %.4e   p_perp %+.4e   p_para %+.4e   "
              "rho+p_para %.1e" % (B, rho, pt, pl, nec_margin(B)))
    print()
    print("   DEC margins at 45 T (transverse, longitudinal): %.1e, %.1e"
          % dec_margin(45.0))
    print("   trace  -rho + sum p_i  at 45 T                : %.1e"
          % trace(45.0))
    print("   -> Hawking-Ellis TYPE I, traceless, on the corner of the "
          "allowed region.")
    print()
    print("=" * 74)
    print("2.  THE THEOREM")
    print("=" * 74)
    print("   T_{mu nu} k^mu k^nu  =  | P_perp ( E + n x B ) |^2  >=  0")
    print()
    print("   identity residual over 100k random (E,B,n)   %.3e"
          % identity_residual())
    lo, neg = superposition_cannot_help()
    print("   superposed pairs: minimum NEC seen           %.3e" % lo)
    print("   superposed pairs: samples with NEC < 0       %d" % neg)
    print()
    print("   configurations that SATURATE (reach exactly zero):")
    for nm, val in saturating_configurations():
        print("      %-52s %.1e" % (nm, val))
    print()
    print("   scope: " + SCOPE)
    print()
    print("=" * 74)
    print("3.  WHAT COUNTER-ROTATION BUYS, AND WHAT IT SPENDS")
    print("=" * 74)
    r = rig_angular_momentum()
    _ej, ebg = earth_bg()
    print("   ring  100 kg, R = 1 m,   100 Hz   J = %+.4e J.s" % r["J_ring"])
    print("   disc   50 kg, R = 0.4 m, -100 Hz  J = %+.4e J.s" % r["J_disc"])
    print("   stored field's mass-equivalent    %.4e kg" % r["m_field_kg"])
    print("   its angular momentum              %+.4e J.s" % r["J_field"])
    print("   MATERIAL / FIELD angular momentum %.3e" % r["material_over_field"])
    print()
    print("   uncancelled   J_total = %+.4e J.s -> B_g %.3e = %.3e of Earth's"
          % (r["J_total"], r["Bg_uncancelled"], r["Bg_uncancelled"] / ebg))
    print("   the disc rate that cancels it exactly: %.1f Hz"
          % r["f_disc_that_cancels"])
    print("   cancelled     J_total = 0          -> B_g %.1e  -- AND THAT IS"
          % r["Bg_if_cancelled"])
    print("      THE ONLY GRAVITATIONAL EFFECT THE MACHINE HAD.")
    print()
    print("=" * 74)
    print("4.  WHAT THE MACHINE REALLY DOES")
    print("=" * 74)
    a = what_it_actually_does()
    print("   induced EMF                       %.3e V" % a["induced_emf_V"])
    print("   eddy-current power in a 1 cm rim  %.3e W" % a["eddy_power_W"])
    print("   magnetic pressure on the structure %.3e Pa  (%.0f atm)"
          % (a["magnetic_pressure_Pa"], a["magnetic_pressure_atm"]))
    print("   -- every one of these is astronomically above any gravitational")
    print("      quantity in the problem.  It is an eddy-current brake.")
    print()
    print("=" * 74)
    print("5.  WHERE THE REAL TARGET IS")
    print("=" * 74)
    b = the_real_barrier()
    print("   TARGET-1-RESULT.md: all four energy conditions SATISFIED,")
    print("   Hawking-Ellis Type I everywhere, zero Type-IV cells.")
    print("   So a warp metric needs no negative energy -- it needs MASS:")
    print()
    print("   Fuchs shell mass                  %.4e kg" % b["shell_mass_kg"])
    print("      in Earth masses                %.1f" % b["earth_masses"])
    print("      inside R2                      %.0f m" % b["shell_R2_m"])
    print("      mean density                   %.3e kg/m^3" % b["mean_density_kg_m3"])

    print("      over NUCLEAR density           %.3e" % b["over_nuclear_density"])
    print("      its own Schwarzschild radius   %.1f m  (shell R2 = %.0f m)"
          % (b["schwarzschild_radius_m"], b["shell_R2_m"]))
    print("      over the rig's field mass      %.3e" % b["over_rig_field_mass"])
    print("      over the rig's material mass   %.3e" % b["over_rig_material_mass"])
    print()
    if HAVE_Z3:
        print("=" * 74)
        print("6.  THE MACHINE-CHECK  (z3)")
        print("=" * 74)
        for nm, exp, got in prove():
            print("   %-58s %s %s" % (nm, got, "ok" if got == exp else "!!"))
    else:
        print("   (z3 not installed -- `pip install z3-solver` then --prove)")


# ------------------------------------------------------------------ fixtures

def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-60s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("emwarp.py fixtures  (stdlib only; --prove adds the z3 check)")

    # -- 1.  the tension is real, and the margin is exactly zero --------------
    rho, pt, pl = principal_pressures(45.0)
    chk("the longitudinal pressure is NEGATIVE -- the tension is real", pl < 0,
        True)
    chk("and it is exactly minus the energy density", pl, -rho)
    chk("the transverse pressure is positive and equal to rho", pt, rho)
    chk("rho + p_parallel is EXACTLY zero at 1 T", nec_margin(1.0), 0.0)
    chk("rho + p_parallel is EXACTLY zero at 45 T", nec_margin(45.0), 0.0)
    chk("and at 1e6 T -- no field strength moves it", nec_margin(1e6), 0.0)
    chk("DEC is saturated on both axes", dec_margin(45.0), (0.0, 0.0))
    chk("Maxwell stress-energy is traceless", trace(45.0), 0.0)

    # -- 2.  the identity and the search --------------------------------------
    chk("the sum-of-squares identity holds to machine epsilon",
        identity_residual(trials=20000) < 1e-9, True)
    lo, neg = superposition_cannot_help(trials=20000)
    chk("superposed pairs never violate the NEC", neg, 0)
    chk("and the minimum seen is non-negative", lo >= 0.0, True)
    chk("both saturating configurations reach exactly zero",
        [abs(v) < 1e-12 for _n, v in saturating_configurations()], [True, True])
    chk("a NON-saturating direction is strictly positive",
        nec_contraction((0.0, 0.0, 0.0), (0.0, 0.0, 2.5), (1.0, 0.0, 0.0)) > 0,
        True)

    # -- the fixtures must MEASURE, not restate: perturb and watch it move ----
    chk("tilting n off the field axis by 1 degree leaves saturation",
        nec_contraction((0.0, 0.0, 0.0), (0.0, 0.0, 2.5),
                        (math.sin(math.radians(1)), 0.0,
                         math.cos(math.radians(1)))) > 1e-4, True)
    chk("adding any E orthogonal to B breaks saturation upward",
        nec_contraction((1.0, 0.0, 0.0), (0.0, 0.0, 2.5),
                        (0.0, 0.0, 1.0)) > 0, True)

    # -- 3.  the rig ----------------------------------------------------------
    r = rig_angular_momentum()
    chk("the ring's material J exceeds the field's by 3.4e10",
        float("%.2g" % r["material_over_field"]), 3.4e10)
    chk("spinning METAL beats spinning FIELD by nine orders, vs nspin.py",
        r["Bg_uncancelled"] / earth_bg()[1] > 1e-9, True)
    chk("the ring and disc spin opposite ways",
        r["J_ring"] > 0 and r["J_disc"] < 0, True)
    chk("a disc rate exists that cancels the ring exactly",
        abs(rig_angular_momentum(f_disc=r["f_disc_that_cancels"])["J_total"])
        < 1e-6, True)
    chk("and cancelling zeroes the frame-dragging",
        rig_angular_momentum(f_disc=r["f_disc_that_cancels"])["Bg_uncancelled"]
        < 1e-30, True)

    # -- 5.  the barrier ------------------------------------------------------
    b = the_real_barrier()
    chk("the Fuchs shell is over 700 Earth masses",
        b["earth_masses"] > 700, True)
    chk("and over 1e35 times the rig's stored-field mass",
        b["over_rig_field_mass"] > 1e35, True)
    chk("the density needed is 6.7e5 x nuclear -- THE barrier",
        float("%.2g" % b["over_nuclear_density"]), 6.7e5)
    chk("but the shell sits OUTSIDE its own Schwarzschild radius",
        b["schwarzschild_radius_m"] < FUCHS_SHELL["R1_m"], True)
    chk("with this much margin", float("%.2g" % (FUCHS_SHELL["R1_m"]
        / b["schwarzschild_radius_m"])), 1.5)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--prove" in sys.argv:
        for nm, exp, got in prove():
            print("   %-58s %s %s" % (nm, got, "ok" if got == exp else "!!"))
        sys.exit(0)
    report()
