#!/usr/bin/env python3
"""
overturn.py -- M asked the only question worth asking after a certification:

    "What math is needed to reverse the verdict?"

Not "is the verdict right" -- certify.py answered that.  What MATHEMATICS,
named and specific, would have to be true for it to be wrong.  That is a
different and much sharper question, because a verdict is never one claim.
It is a CHAIN, and a chain is reversed by breaking exactly one link.

This file states the chain as four links, and for each one states the exact
proposition whose truth would break it, and the current status of that
proposition.  Two of the four are settled -- and one of them is settled HERE,
in this pass, AGAINST US, which is the outcome I did not expect.  Two remain
live, and only one of those touches the number.

A door found here changes which no-go is doing the work, and that matters
more than it sounds: it is not the positive mass theorem and it is not ANEC.

===============================================================================
0. THE CHAIN
===============================================================================

The verdict, stated so it can be attacked:

    L1  SCOPE.      In any static spherically symmetric spacetime, proper
                    radial distance is contracted at r if and only if the
                    Misner-Sharp mass m(r) is negative.   [certify.py, THEOREM]

                    L1 IS TWO DOORS AND THIS FILE ONLY EVER NAMED ONE.  Section
                    2 below reads L1 as the SPHERICITY link and attacks it
                    there; the STATICITY half is a separate hypothesis and was
                    never argued here.  nonstatic.py (DOCKET 52) opened it --
                    dropping staticity gives contraction <=> 2m/R < e^{-2Phi}
                    Rdot^2, so m < 0 is sufficient and NOT necessary -- and
                    then closed it, twice and without any energy condition.
                    SPHERICITY HALF: still OPEN, exactly as section 2 says.

    L2  SOURCE.     m(r) = 4 pi int_0^r rho r'^2 dr' -- the geometry's mass
                    IS the matter's energy -- because G_munu = 8 pi T_munu.

                    L2 IS BROKEN, AND THE BREAK IS EMPTY.  It needs a REGULAR
                    CENTRE for that integral's lower limit; a point charge
                    supplies none, and Reissner-Nordstrom has m(r) < 0 for
                    r < Q^2/2M with rho > 0 everywhere.  So negative m(r)
                    demonstrably does NOT require negative matter energy, which
                    is precisely what "break L2" was supposed to buy -- and it
                    buys nothing, because the classical radius r_c = Q^2/2M
                    of any body of charge Q and mass M >= 0 satisfies
                    r_c <= a, its own radius, for every charged body that
                    exists.  The region is inside the source.  drivensource.py
                    section 3 derives it and machine-checks both halves.

    L3  RATE.       The distance bought per unit of that negative mass is
                    Delta d = |m| ln(r2/r1) -- the logarithm -- which is why
                    the exchange rate c^4/(G Lambda) is as brutal as it is.

    L4  MAGNITUDE.  The |rho| that L2+L3 demand at corridor scale R exceeds
                    every bound any known quantum inequality permits, by a
                    factor growing as R^2.       [candidates.py, Pfenning-Ford]

Break L1 and the theorem does not reach the geometry you want.
Break L2 and negative m(r) no longer needs negative energy.
Break L3 and the same |m| buys more distance.
Break L4 and the requirement becomes sourceable.

ANY ONE of these reverses the verdict.  All four are attacked below.

===============================================================================
1. L3, THE RATE -- CLOSED IN THIS PASS, AND CLOSED AGAINST US
===============================================================================

I expected this to be the soft link.  The logarithm was derived in the weak
field, where 1/sqrt(1-2m/r) ~ 1 + m/r and the integral of dr/r is a log.  The
obvious hope: the weak field UNDERSTATES the return, and a strong field buys
more distance per unit mass.

Measured, ansatz-free, by integrating the proper-length deficit directly

    Delta d(m) = int_r1^r2 [ 1 - 1/sqrt(1 - 2m/r) ] dr

over r1 = 1, r2 = 200, against the weak-field prediction |m| ln(r2/r1):

    WEAK FIELD (m < 0), ratio to |m| ln(r2/r1):

        |m| = 1e-8     1.000000
        |m| = 1e-6     1.000000
        |m| = 1e-4     0.999972
        |m| = 1e-2     0.997206

    -- the logarithm is not an approximation artefact.  It is exact in the
    limit and it is ansatz-free: no Phi, no Plummer, no shell, just the areal
    radius and the Misner-Sharp mass.

    STRONG FIELD, same ratio, and Delta d as a fraction of the whole gap:

        |m| = 1e0      0.833100     Delta d / (r2-r1) = 0.0222
        |m| = 1e1      0.504993                         0.1345
        |m| = 1e2      0.174544                         0.4647
        |m| = 1e3      0.029831                         0.7942
        |m| = 1e4      0.003505                         0.9332

THE RETURN FALLS MONOTONICALLY.  And the reason is not subtle once seen:
Delta d SATURATES.  You cannot contract 199 units of coordinate separation by
more than 199 units of proper distance; the integrand is bounded above by 1.
So the curve bends over, and every extra unit of |m| buys strictly less than
the one before it.

    THE WEAK-FIELD LOGARITHM IS NOT A LIMITATION OF THE DERIVATION.
    IT IS THE BEST CASE.

L3 is closed.  It was the link I thought most likely to give, and it gave in
the wrong direction: the true rate is the logarithm ONLY in the limit of
vanishing mass, and is worse everywhere else.  Recorded because it goes
against us -- the same discipline certify.py applied to Pfenning-Ford.

===============================================================================
2. L1, THE SCOPE -- LIVE, AND IT IS THE REAL DOOR
===============================================================================

certify.py states its own scope in its own source: THEOREM_SCOPE = "static and
spherically symmetric only".  That is not modesty, it is the hypothesis the
proof uses.  The proof needs an AREAL RADIUS -- a coordinate r with the
property that the sphere at r has area 4 pi r^2 -- and outside spherical
symmetry there is no such coordinate, so m(r) has no definition and the
biconditional has no statement.  Not false.  UNSTATED.

What mathematics would break it: a QUASI-LOCAL MASS for a closed 2-surface in
a static spacetime that (a) reduces to Misner-Sharp on round spheres, and
(b) controls proper distance the same way.  The candidates are named and the
literature is real:

    HAWKING MASS       m_H(S) = sqrt(|S|/16 pi) (1 - (1/16 pi) int_S H^2)
                       -- reduces to Misner-Sharp on round spheres, which is
                       exactly requirement (a).  Not monotone in general.

    GEROCH MONOTONICITY / HUISKEN-ILMANEN -- m_H IS monotone non-decreasing
                       under inverse mean curvature flow when the scalar
                       curvature R >= 0.  This is the machinery that proved
                       the Riemannian Penrose inequality.  It is the closest
                       existing thing to requirement (b).

    BARTNIK MASS       the infimum over admissible extensions.  Correct
                       variational object, notoriously hard to compute.

    THE DIRECTION THAT WOULD HELP US IS THE ONE GEROCH DOES NOT GIVE.
    Monotonicity under IMCF with R >= 0 is a statement that mass does not
    DECREASE outward.  What a reversal needs is a surface with m_H(S) >= 0
    whose enclosed region still contracts proper distance -- i.e. the
    biconditional FAILING in the direction that frees us.  Nobody has shown
    that, and nobody has shown it cannot happen.

This link is genuinely open.  It is open in the literature, not merely open
here, and it is the only place in the chain where new pure mathematics --
not new physics, not a new energy source -- could overturn the result.

    STATUS: OPEN.  NOT ATTEMPTED HERE.  Attempting it is a differential
    geometry programme, not an afternoon, and claiming otherwise would be
    the exact fault provenance.py was built to catch.

===============================================================================
3. A DOOR FOUND HERE: WHICH NO-GO IS ACTUALLY DOING THE WORK
===============================================================================

L2 puts the requirement on a BALL integral:  int_ball rho dV < 0.
Every averaged energy condition bounds a WORLDLINE integral: int_line rho dl.

Those are different functionals of the same rho, and the question of whether
one constrains the other is answerable by arithmetic.  It does not.

Take a two-zone profile, flat-space kinematics, purely as a statement about
the two integrals:

        rho(r) = -b   for r < r0        (negative core)
               = +a   for r0 < r < R    (positive shell)
               =  0   outside

With r0 = 1, R = 2, b = 1, a = 1.5:

        m(r0)  =  -4.188790  = -(4/3) pi b r0^3      NEGATIVE
                                       -- L1 gives contraction at r0
        m(R)   = +39.793507  = +(4/3) pi (9.5)        positive total mass,
                                                       so ADM-safe
        chord through the centre, p = 0:  +1.000000 = 2[a(R-r0) - b r0]
        every chord 0 <= p <= R:          >= 0

All four are closed forms; the quadrature below agrees with them to 1e-4,
which is the O(h) an endpoint on a discontinuous profile costs.

An ANEC-analogue holds on every straight chord while the enclosed mass at r0
is negative.  And the margin does not shrink under scaling -- hold a = 1.5 b
and raise b:

        b = 1       m(r0) = -4.1888e0    chord(0) = +1.0000e0
        b = 10      m(r0) = -4.1888e1    chord(0) = +1.0000e1
        b = 100     m(r0) = -4.1888e2    chord(0) = +1.0000e2
        b = 1000    m(r0) = -4.1888e3    chord(0) = +1.0000e3

-- both exactly linear in b, which is the whole point: the ratio between them
is fixed and neither sign nor magnitude of one says anything about the other.

    THE CHORD INTEGRAL DOES NOT BOUND THE BALL INTEGRAL BELOW.  AT ALL.
    m(r0) runs to minus infinity with every chord integral running to PLUS
    infinity simultaneously.

SCOPE, STATED TIGHTLY, BECAUSE THIS IS EASY TO OVER-READ:

    This is a statement about two integrals as functionals of a density.  It
    is NOT a solution of the field equations, the chords are straight rather
    than geodesics of the metric such a rho would produce, and rho < 0 in the
    core means the POINTWISE weak energy condition fails there -- as it must,
    since that is what is being asked for.

WHAT IT ESTABLISHES ANYWAY, AND IT IS WORTH HAVING:

    The positive mass theorem does not forbid this -- total mass is positive.
    ANEC does not forbid this -- it is satisfied and it is not even the right
    shape of constraint.
    The no-go that bites is the LOCAL, SAMPLED one: the Ford-Roman quantum
    inequality and its descendants, which bound |rho| itself over a sampling
    region rather than an average along a line.

    That is candidates.py's magnitude gate and it is Pfenning-Ford's result,
    and this file's contribution is to show that it is carrying the WHOLE
    weight.  Two of the three famous obstructions are not obstructions here.

===============================================================================
4. L2, THE FIELD EQUATION -- OPEN THE ENTIRE PROJECT, AND NOT MINE TO CLOSE
===============================================================================

L1 constrains m(r), the GEOMETRY's mass.  L2 identifies it with the MATTER's
energy, and that identification is G_munu = 8 pi T_munu and nothing else.  In
f(R) gravity, scalar-tensor, Einstein-Gauss-Bonnet or any higher-curvature
theory, the field equations rearrange to

        G_munu = 8 pi T^matter_munu + T^effective_munu

where T^effective is built from curvature.  An effective term can be negative
where the matter term is not.  If it can, L2 breaks and the requirement stops
being a requirement on matter at all.

    THIS IS THE LARGEST SINGLE UNEXPLORED BRANCH IN THE PROJECT, AND IT HAS
    BEEN FLAGGED AS SUCH SINCE wormhole.py, WHICH CARRIES

        SCOPE_CHOSEN_HERE = None        # M's constraint, M's decision

    and asserts that None in its own selftest so that nobody -- including me
    -- can quietly decide it.  The flag has stood unchanged for the whole
    project.  It is a scope decision about what counts as proven, and M's
    standing constraint is "true and proven in its math".  Whether a result
    inside modified gravity meets that bar is M's call, not mine.

    STATUS: OPEN BY DECISION, AWAITING M.  This file does not change the flag.

    THAT IS THE MODIFIED-GRAVITY BREAK AND IT IS STILL THE ONE AWAITING M.
    DOCKET 52 found a SECOND break of L2, inside general relativity and needing
    no scope decision at all: the integral m(r) = 4 pi int_0^r rho r'^2 dr'
    presumes a REGULAR CENTRE, and Reissner-Nordstrom has none.  There m(r) < 0
    for r < Q^2/2M with rho > 0 everywhere -- negative geometric mass, positive
    matter energy, in ordinary Einstein gravity.  L2 is therefore BROKEN as
    stated, and it is EMPTY: the radius Q^2/2M is inside every charged body
    that exists.  Two breaks of one link, and neither is a route.  See the
    LINKS table below, drivensource.py section 3, and the COROLLARY note in
    certify.py.

===============================================================================
5. L4, THE MAGNITUDE -- THE ONLY LINK THAT TOUCHES THE BILL
===============================================================================

Breaking L1, L2 or L3 changes what is required.  Only L4 changes what is
PAYABLE, and by §3 it is now the sole load-bearing obstruction.

The shape of the problem, from candidates.py:

    requirement    |rho| ~ c^4 / (G Lambda R^2)          goes as R^-2
    Ford-Roman     |rho| <= 3 hbar c / (32 pi^2 L^4)      goes as L^-4
    Casimir        |rho|  = pi^2 hbar c / (720 d^4)       goes as d^-4

Two different exponents, so the shortfall is not a constant to be engineered
around -- it grows as R^2 and the crossovers sit at 0.307933 l_P and
0.369917 l_P.  Sub-Planckian, which is Pfenning-Ford's conclusion in this
architecture's coordinates.

THE ONE CANDIDATE WHOSE EXPONENT MATCHES is candidate D, non-minimal coupling:

    Fewster & Osterbrink (arXiv:0708.2450) -- for a scalar with xi > 0 there
    is NO state-independent quantum energy inequality.  The bound that
    forbids us does not exist in that theory.

    Fliss, Freivogel, Kontou et al. (arXiv:2309.10848) -- the EFT bound is
    |rho| ~ hbar c / (l_UV^2 delta^2), which is delta^-2.  SAME EXPONENT AS
    THE REQUIREMENT.  The shortfall then collapses from a growing function to
    the pure number (l_UV / l_P)^2 / Lambda, which closes at

        l_UV = sqrt(Lambda) l_P = 3.159514 l_P.

    A factor of three in the UV cutoff, not twenty orders of magnitude.

    WHAT WOULD BE NEEDED: a quantum energy inequality for non-minimally
    coupled fields in curved spacetime, state-independent enough to be a
    bound and R^-2 enough to be the right shape, derived rather than
    scaling-argued.  That is quantum field theory in curved spacetime, it is
    an active literature, and the sign of the answer is not known.

    STATUS: OPEN.  This is where the money is and it is the hardest of the
    four.

===============================================================================
6. THE VERDICT ON THE VERDICT
===============================================================================

    L1  SCOPE      OPEN     quasi-local mass beyond spherical symmetry
                            -- the SPHERICITY half.  The STATICITY half was a
                            second door this file never named; DOCKET 52
                            opened and closed it.
    L2  SOURCE     BROKEN   by a point charge, and the break is EMPTY:
                   -EMPTY   r_c = Q^2/2M <= a for every charged body.  The
                            modified-gravity break is a different one and is
                            still OPEN BY DECISION, awaiting M.
    L3  RATE       CLOSED   against us, in this pass; the log is the best case
    L4  MAGNITUDE  OPEN     a non-minimal QEI with the right exponent

One link closed this pass and it closed the wrong way.  Two of the three
famous no-gos turn out not to apply.  Three links remain, and NONE of them
is engineering -- every one is mathematics, two of them open in the
literature rather than merely open here.

    WHAT DOCKET 52 DID TO THIS TABLE, AND WHAT IT DID NOT.  It broke L2 and
    left the verdict standing, which is the whole point of enumerating a chain:
    a link can fall without the conclusion falling, and you only find that out
    by naming the links first.  L4 remains the sole load-bearing obstruction
    and nothing here touches it.

    THE ANSWER TO M'S QUESTION IS THEREFORE SHORT AND IT IS NOT DISCOURAGING:

    No amount of measurement reverses this.  No power source reverses this.
    What reverses it is one of three theorems, none of which is known to be
    false, and the cheapest of the three is a decision M has been holding
    since wormhole.py rather than a discovery anyone has to make.

Nothing here is repaired and nothing here is claimed.  A door is not a result.
"""

import math
import sys

# ---------------------------------------------------------------------------
# THE CHAIN, as data.  A verdict you cannot enumerate is a verdict you cannot
# attack.
# ---------------------------------------------------------------------------

OPEN, CLOSED = "OPEN", "CLOSED"

# A third status, and it is not a synonym for either.  A link is BROKEN-EMPTY
# when the thing that would break it exists and reverses nothing: the chain no
# longer holds there, and the verdict is unmoved.  Introduced by DOCKET 52 for
# L2, which "break L2 and negative m(r) no longer needs negative energy" turned
# out to describe exactly, at a radius that is always inside the body.  Calling
# it CLOSED would claim the link holds; calling it OPEN would claim a route.
BROKEN_EMPTY = "BROKEN-EMPTY"

LINKS = [
    # (id, name, what breaking it would do, status, what would break it)
    ("L1", "SCOPE",
     "the theorem would not reach non-spherical geometry",
     OPEN,
     "a quasi-local mass reducing to Misner-Sharp on round spheres that "
     "controls proper distance (Hawking / Geroch-IMCF / Bartnik)"),
    ("L2", "SOURCE",
     "negative m(r) would not require negative matter energy",
     BROKEN_EMPTY,
     "BROKEN by a point charge: Reissner-Nordstrom has m(r) < 0 for "
     "r < Q^2/2M with rho > 0 everywhere, because the integral's lower "
     "limit needs a regular centre.  EMPTY because r_c = Q^2/2M <= a for "
     "every charged body with mass >= 0 -- the region is inside the "
     "source.  drivensource.py section 3, machine-checked."),
    ("L3", "RATE",
     "the same |m| would buy more distance",
     CLOSED,
     "measured here: the strong field returns strictly LESS, because "
     "Delta d saturates at r2 - r1"),
    ("L4", "MAGNITUDE",
     "the requirement would become sourceable",
     OPEN,
     "a state-independent QEI for non-minimal coupling scaling as R^-2 "
     "(Fewster-Osterbrink; Fliss et al.)"),
]

# The one link this file settles.  Named so it cannot be quietly widened.
CLOSED_HERE = "L3"
CLOSED_AGAINST_US = True

# This file does NOT touch wormhole.py's flag.  Asserted in selftest.
TOUCHES_SCOPE_FLAG = False

LAMBDA = 9.982529174194637


# ---------------------------------------------------------------------------
# L3.  The rate, measured ansatz-free.
#
#   ds^2 radial part = dr^2 / (1 - 2 m(r)/r),  proper length dl = dr/sqrt(...)
#   so the CONTRACTION relative to coordinate separation is
#
#       Delta d = int (1 - 1/sqrt(1 - 2m/r)) dr
#
#   Integrating the deficit directly rather than differencing two lengths --
#   the differencing form loses all its digits in the weak field and reports
#   a spurious gain, which is how this was nearly got wrong.
# ---------------------------------------------------------------------------

def deficit(m, r1, r2, n=100001):
    """int_r1^r2 (1 - 1/sqrt(1-2m/r)) dr.  Positive = contraction (m < 0)."""
    if n % 2 == 0:
        n += 1
    h = (r2 - r1) / (n - 1)
    s = 0.0
    for i in range(n):
        r = r1 + i * h
        w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
        s += w * (1.0 - 1.0 / math.sqrt(1.0 - 2.0 * m / r))
    return s * h / 3.0


def weakfield_prediction(m, r1, r2):
    """|m| ln(r2/r1) -- the logarithm, from 1/sqrt(1-2m/r) ~ 1 + m/r."""
    return abs(m) * math.log(r2 / r1)


def rate_ratio(m, r1, r2, n=100001):
    """Measured contraction as a fraction of the weak-field logarithm."""
    return deficit(-abs(m), r1, r2, n) / weakfield_prediction(m, r1, r2)


def rate_is_monotone_decreasing(masses, r1, r2, n=40001):
    """The finding: the return per unit |m| never rises."""
    rs = [rate_ratio(m, r1, r2, n) for m in masses]
    return all(rs[i + 1] < rs[i] for i in range(len(rs) - 1)), rs


# ---------------------------------------------------------------------------
# Section 3.  The ball integral and the chord integral, as functionals.
#
#   FLAT-SPACE KINEMATICS ONLY.  This exhibits no solution and claims none.
#   What it settles is whether one functional bounds the other.  It does not.
# ---------------------------------------------------------------------------

class TwoZone:
    """rho = -b inside r0, +a in the shell r0..R, 0 outside."""

    def __init__(self, r0=1.0, R=2.0, b=1.0, a=1.5):
        self.r0, self.R, self.b, self.a = r0, R, b, a

    def rho(self, r):
        if r < self.r0:
            return -self.b
        if r < self.R:
            return self.a
        return 0.0

    # -- closed forms.  A two-zone profile has them, so the quadrature is
    # -- validated rather than trusted.
    def exact_ball_r0(self):
        return -(4.0 / 3.0) * math.pi * self.b * self.r0 ** 3

    def exact_ball_R(self):
        return (4.0 / 3.0) * math.pi * (
            self.a * (self.R ** 3 - self.r0 ** 3) - self.b * self.r0 ** 3)

    def exact_chord0(self):
        return 2.0 * (self.a * (self.R - self.r0) - self.b * self.r0)

    def ball(self, rr, n=100001):
        """4 pi int_0^rr rho r^2 dr -- the Misner-Sharp mass content."""
        if n % 2 == 0:
            n += 1
        h = rr / (n - 1)
        s = 0.0
        for i in range(n):
            r = i * h
            w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
            s += w * self.rho(r) * r * r
        return 4.0 * math.pi * s * h / 3.0

    def chord(self, p, n=100001):
        """int rho dl along the straight chord at impact parameter p."""
        if p >= self.R:
            return 0.0
        if n % 2 == 0:
            n += 1
        X = math.sqrt(self.R * self.R - p * p)
        h = 2.0 * X / (n - 1)
        s = 0.0
        for i in range(n):
            x = -X + i * h
            w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
            s += w * self.rho(math.hypot(x, p))
        return s * h / 3.0

    def worst_chord(self, k=41, n=20001):
        """Minimum over ALL impact parameters 0 <= p <= R.

        The minimum is zero and it is attained only by a GRAZING chord, one
        that misses the body -- a chord of zero length integrates to zero.
        That is not a near-violation, so the number worth quoting is the
        other one: the chord that penetrates the negative core deepest,
        p = 0, which is `chord(0)` and is strictly positive.
        """
        out = [(j * self.R / (k - 1), self.chord(j * self.R / (k - 1), n))
               for j in range(k)]
        return min(out, key=lambda t: t[1])

    def deepest_chord(self, n=20001):
        """p = 0 -- the chord through the whole negative core."""
        return self.chord(0.0, n)


# What the two-zone profile establishes, stated as a predicate so it is
# testable rather than asserted.
def chord_does_not_bound_ball(scales=(1.0, 10.0, 100.0, 1000.0)):
    """m(r0) -> -inf while every chord integral -> +inf.  Independent."""
    rows = []
    for B in scales:
        z = TwoZone(b=B, a=1.5 * B)
        rows.append((B, z.ball(z.r0, 20001), z.chord(0.0, 20001)))
    masses_fall = all(rows[i + 1][1] < rows[i][1] for i in range(len(rows) - 1))
    chords_rise = all(rows[i + 1][2] > rows[i][2] for i in range(len(rows) - 1))
    return (masses_fall and chords_rise), rows


# ---------------------------------------------------------------------------
# L4.  The exponent mismatch, and the one candidate whose exponent matches.
# ---------------------------------------------------------------------------

def uv_cutoff_that_closes_L4(lam=LAMBDA):
    """sqrt(Lambda) l_P, in units of l_P.  Candidate D's closing point."""
    return math.sqrt(lam)


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        if tol is None:
            good = got == want
        else:
            good = abs(got - want) <= tol * max(1.0, abs(want))
        if not good:
            ok = False
            print("FAIL %-58s got %r want %r" % (label, got, want))
        else:
            print("ok   %-58s %r" % (label, got))

    # -- the chain is enumerable and each row has the same shape -------------
    shape = [l for l in LINKS if len(l) != 5]
    chk("every link is (id, name, effect, status, breaker)", shape, [])
    chk("four links", len(LINKS), 4)
    chk("exactly one is CLOSED", sum(1 for l in LINKS if l[3] == CLOSED), 1)
    chk("the closed one is L3",
        [l[0] for l in LINKS if l[3] == CLOSED], ["L3"])
    chk("and it closed against us", CLOSED_AGAINST_US, True)

    # -- this file does not decide M's scope question ------------------------
    chk("does not touch wormhole.py's scope flag", TOUCHES_SCOPE_FLAG, False)

    # -- L3: the weak field IS the logarithm, exactly -------------------------
    r1, r2 = 1.0, 200.0
    chk("weak field |m|=1e-8 returns the logarithm",
        rate_ratio(1e-8, r1, r2, 40001), 1.0, 1e-5)
    chk("weak field |m|=1e-6 returns the logarithm",
        rate_ratio(1e-6, r1, r2, 40001), 1.0, 1e-5)
    chk("weak field |m|=1e-2 is already 0.28% short",
        rate_ratio(1e-2, r1, r2, 40001), 0.99721, 1e-3)

    # -- L3: the strong field returns LESS, monotonically --------------------
    mono, rs = rate_is_monotone_decreasing([1.0, 10.0, 100.0, 1e3, 1e4],
                                           r1, r2)
    chk("strong-field return is monotone decreasing", mono, True)
    chk("|m|=1     ratio", rs[0], 0.83310, 1e-3)
    chk("|m|=1e2   ratio", rs[2], 0.174544, 1e-3)
    chk("|m|=1e4   ratio", rs[4], 0.003505, 1e-2)
    chk("the logarithm is the BEST case, not a limitation",
        all(r < 1.0 for r in rs), True)

    # -- L3: and the reason -- Delta d saturates -----------------------------
    d = deficit(-1e4, r1, r2, 40001)
    chk("Delta d saturates below the coordinate gap", d < (r2 - r1), True)
    chk("at |m|=1e4 it is 93% of the gap", d / (r2 - r1), 0.9332, 1e-3)

    # -- section 3: the two functionals are independent ----------------------
    z = TwoZone()
    # closed forms first -- the quadrature is checked AGAINST them, not
    # against a previous run of itself.
    chk("closed form m(r0) = -(4/3) pi b r0^3",
        z.exact_ball_r0(), -4.1887902, 1e-7)
    chk("closed form m(R)", z.exact_ball_R(), 39.7935069, 1e-7)
    chk("closed form central chord = 2[a(R-r0) - b r0]",
        z.exact_chord0(), 1.0, 1e-12)
    chk("negative core gives m(r0) < 0", z.ball(z.r0, 20001), -4.1887902, 1e-3)
    chk("quadrature converges to the closed form",
        abs(z.ball(z.r0, 80001) - z.exact_ball_r0())
        < abs(z.ball(z.r0, 20001) - z.exact_ball_r0()), True)
    chk("total mass is POSITIVE (ADM-safe)", z.ball(z.R, 20001) > 0, True)
    p, v = z.worst_chord()
    chk("no chord is negative", v >= -1e-6, True)
    chk("the minimum is a grazing chord, at p = R", p, z.R, 1e-9)
    chk("the deepest chord (p=0) is strictly positive",
        z.deepest_chord(), 1.0, 1e-3)
    indep, rows = chord_does_not_bound_ball()
    chk("chord integral does not bound ball integral below", indep, True)
    chk("m(r0) at b=1000", rows[3][1], -4188.7902, 1e-3)
    chk("chord(0) at b=1000", rows[3][2], 1000.0, 1e-3)

    # -- the scope caveat is in the file, not only in my head ----------------
    chk("flat-space kinematics is stated in the docstring",
        "FLAT-SPACE KINEMATICS ONLY" in __doc__ or
        "flat-space kinematics" in __doc__, True)
    chk("no solution is claimed",
        "NOT a solution of the field equations" in __doc__, True)

    # -- L4 ------------------------------------------------------------------
    chk("candidate D closes at sqrt(Lambda) l_P",
        uv_cutoff_that_closes_L4(), 3.159514, 1e-5)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    r1, r2 = 1.0, 200.0
    print("  ------------------------------------------------------------------------")
    print("  THE CHAIN\n")
    for lid, name, effect, status, breaker in LINKS:
        print("    %-3s %-10s %-7s %s" % (lid, name, status, effect))
        print("        breaks if: %s" % breaker)
    print()
    print("  ------------------------------------------------------------------------")
    print("  L3 MEASURED (r1=%g, r2=%g), ratio to |m| ln(r2/r1)\n" % (r1, r2))
    for m in (1e-8, 1e-6, 1e-4, 1e-2, 1.0, 10.0, 100.0, 1e3, 1e4):
        d = deficit(-m, r1, r2, 40001)
        print("    |m| = %-9.0e  Delta d = %12.6e   ratio = %.6f   "
              "frac of gap = %.4f" % (m, d, d / weakfield_prediction(m, r1, r2),
                                      d / (r2 - r1)))
    print("\n    The logarithm is the BEST case.  L3 is closed, against us.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  BALL vs CHORD -- flat-space kinematics, no solution claimed\n")
    for B in (1.0, 10.0, 100.0, 1000.0):
        z = TwoZone(b=B, a=1.5 * B)
        print("    b = %-7.1f  m(r0) = %+.4e   deepest chord (p=0) = %+.4e"
              "   min over all p = %+.1e"
              % (B, z.ball(z.r0, 20001), z.deepest_chord(),
                 z.worst_chord()[1]))
    print("\n    The chord integral does not bound the ball integral below.")
    print("    Neither the positive mass theorem nor ANEC is doing the work.")
    print("    The load-bearing obstruction is the sampled quantum inequality.")
    print()
    print("""  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asked what mathematics would reverse the verdict.  The verdict is a
  chain of four links -- the theorem's SCOPE, the identification of
  geometric mass with matter energy (the field EQUATION), the RATE at
  which negative mass buys distance, and the MAGNITUDE the result demands.
  Breaking any one reverses it.  L3, the rate, is closed here and closed
  against us: integrating the proper-length deficit directly shows the
  weak-field logarithm is exact in the limit and the strong field returns
  strictly less -- 0.833 of it at |m|=1, 0.0035 at |m|=1e4 -- because the
  contraction saturates at the coordinate gap.  The logarithm was the best
  case all along.  Against that, a door: the requirement is on a BALL
  integral of rho and every averaged energy condition bounds a WORLDLINE
  integral, and a two-zone profile shows these do not constrain each other
  at all -- m(r0) runs to minus infinity while every chord integral runs
  to plus infinity.  So neither the positive mass theorem nor ANEC is
  carrying this; the whole weight is on the sampled Ford-Roman bound,
  which is Pfenning-Ford's result and candidates.py's magnitude gate.
  Three links stay open: a quasi-local mass beyond spherical symmetry
  (open in the literature), a QEI for non-minimal coupling with R^-2
  scaling (open, and the only one that touches the bill), and the
  modified-gravity scope decision that wormhole.py has held as
  SCOPE_CHOSEN_HERE = None for the whole project and that is M's to make.
  Nothing is repaired and no door is a result.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
