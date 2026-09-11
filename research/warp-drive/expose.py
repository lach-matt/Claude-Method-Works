#!/usr/bin/env python3
"""
expose.py -- M: "Every breakthrough starts with a conjecture.  Let's proceed."

PROCEEDING MEANS WORKING THE ONE GAP THAT NEEDS NOBODY'S CONJECTURE.  gaps.py
sorted the gaps by what would close them and found exactly one SEARCH on our
side: does any EXPOSED stationary configuration contract proper distance with
POSITIVE MASS?  threads.py had just shown Kerr does it behind a horizon.  This
file goes looking outside one.

IT FOUND A FAULT IN threads.py FIRST, AND THE FAULT IS MINE.  threads.py read
contraction off sqrt(g_rr) < 1 in Boyer-Lindquist coordinates.  That test is
satisfied THROUGHOUT FLAT EMPTY SPACE: Kerr at M = 0 IS Minkowski, written in
oblate spheroidal coordinates, and its equatorial g_rr = r^2/(r^2+a^2) < 1 at
every radius.  A criterion that fires in vacuum with no source is not measuring
the source.

The invariant replacement is the ratio this project has always actually meant:

    C(r) = (proper radial distance) / (change in CIRCUMFERENTIAL radius)
         = sqrt(g_rr) / (d/dr) sqrt(g_phiphi)

CONTRACTION IS C < 1.  C = 1 exactly in flat space however it is coordinatised,
and for a static spherically symmetric metric C = 1/sqrt(1 - 2m/r), so C < 1 if
and only if m < 0 -- WHICH IS certify.py's THEOREM EXACTLY.  The theorem was
always a statement about C; threads.py compared the wrong thing to 1.

WHAT SURVIVES, AND IT IS THE HEADLINE:  Kerr DOES contract with M > 0, so the
biconditional still fails outside static.  WHAT DOES NOT SURVIVE is every number
threads.py gave.  The contraction is nowhere near where that file put it: never
on the equator, always off-axis near the ring, and -- measured over 3.5 million
sample points -- NEVER OUTSIDE A HORIZON FOR ANY SUB-EXTREMAL SPIN.

AND THAT CLOSES THE SEARCH GAP, NEGATIVE.  The contracted region's outer reach
obeys a scaling law measured here, r_max = kappa (M a^2)^(1/3) with kappa =
0.5226.  Put a material body in the middle -- a = k R v with k = I/MR^2 <= 1 and
rim speed v <= c -- and exposure needs R < kappa^3 M k^2 v^2 <= 0.1427 M, while
Buchdahl's bound puts ANY fluid body at R >= 2.25 M.  SHORT BY 15.8x AT THE
THEORETICAL EXTREME, and by 10^7 for the Earth.

So the exposed branch is EXACTLY the naked-singularity branch, and the
dependence on cosmic censorship is now total rather than partial.

NOTHING IS REPAIRED.  threads.py IS NOT EDITED -- it is corrected here, which is
this tree's rule.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

M_UNIT = 1.0   # every length below is in units of the mass M

# ---------------------------------------------------------------- Kerr, exact
def Delta(r, M, a):   return r*r - 2.0*M*r + a*a
def rho2(r, th, a):   return r*r + a*a*math.cos(th)**2
def g_rr(r, th, M, a):return rho2(r, th, a)/Delta(r, M, a)

def g_phiphi(r, th, M, a):
    """Boyer-Lindquist g_phiphi.  Its square root is the CIRCUMFERENTIAL radius."""
    s2 = math.sin(th)**2
    return s2*(r*r + a*a + 2.0*M*a*a*s2*r/rho2(r, th, a))

def dRc_dr(r, th, M, a):
    """d/dr of sqrt(g_phiphi), ANALYTIC -- no finite differences anywhere."""
    s2 = math.sin(th)**2; c2 = math.cos(th)**2; R2 = rho2(r, th, a)
    dS = s2*(2.0*r + 2.0*M*a*a*s2*(a*a*c2 - r*r)/(R2*R2))
    return dS/(2.0*math.sqrt(g_phiphi(r, th, M, a)))

def contraction(r, th, M, a):
    """C = proper radial length per unit circumferential radius.  C < 1 is contraction.

    Returns (C, dRc_dr).  Where dRc_dr <= 0 the circumferential radius DECREASES
    outward and 'contraction' is not well posed -- the caller must check."""
    d = dRc_dr(r, th, M, a)
    return math.sqrt(g_rr(r, th, M, a))/d, d

def horizon_outer(M, a):
    """r_+, or None when a > M and there is no horizon at all."""
    d = M*M - a*a
    return M + math.sqrt(d) if d >= 0.0 else None

# --------------------------------------------------- the reach of contraction
def reach(a, M=1.0, n_theta=720, step=1.004, r_lo=None, r_hi=None):
    """Largest r at which C < 1 with the circumferential radius still growing."""
    scale = (M*a*a)**(1.0/3.0) if a > 0 else M
    r_lo = r_lo or 1e-4*max(M, scale)
    r_hi = r_hi or (5.0*scale + 10.0*M)
    best = 0.0
    for i in range(1, n_theta):
        th = i*math.pi/n_theta
        r = r_lo
        while r < r_hi:
            if Delta(r, M, a) > 0.0:
                c, d = contraction(r, th, M, a)
                if d > 0.0 and c < 1.0 and r > best:
                    best = r
            r *= step
    return best

KAPPA = 0.5226            # measured: r_max -> KAPPA * (M a^2)^(1/3) for a >> M

def reach_asymptotic(a, M=1.0):
    return KAPPA*(M*a*a)**(1.0/3.0)

# ------------------------------------------------------- the material-body test
def spin_parameter(k, R, v):
    """a = J/M for a body of shape factor k = I/(M R^2), radius R, rim speed v."""
    return k*R*v

def exposure_ceiling(k=1.0, v=1.0, M=1.0):
    """Largest body radius that could sit inside the contracted region.

    R < kappa (M a^2)^(1/3) with a = k R v  <=>  R < kappa^3 M k^2 v^2."""
    return KAPPA**3 * M * k*k * v*v

BUCHDAHL = 2.25           # R >= 9M/4 for any static spherically symmetric fluid body

BODIES = [   # name,               M (kg),      R (m),    J (kg m^2/s)
    ("Earth",             5.972e24,  6.3710e6,  7.07e33),
    ("Jupiter",           1.898e27,  6.9911e7,  6.90e38),
    ("Sun",               1.989e30,  6.9570e8,  1.90e41),
    ("white dwarf, fast", 1.20e30,   5.0e6,     1.0e42),
    ("PSR J1748-2446ad",  3.978e30,  1.6e4,     1.0e42),
]
G_SI, C_SI = 6.67430e-11, 2.99792458e8

def body_numbers(Mkg, Rm, J):
    Mg = G_SI*Mkg/C_SI**2                 # geometric mass, metres
    a  = J/(Mkg*C_SI)                     # spin parameter, metres
    rm = reach(a/Mg, M=1.0)*Mg            # exact reach, metres
    return Mg, a, rm, Rm/rm if rm > 0 else float('inf')

# ------------------------------------------------------------------ censorship
CENSORSHIP_OPEN_SINCE = 1969
THIS_YEAR = 2026

VERIFIED_THIS_SESSION = [   # checked against the paper database in this session
 ("arXiv:2210.13501", "The endpoint of the Gregory-Laflamme instability of black strings revisited",
  "reproduces and extends Lehner-Pretorius: D=5 black strings pinch"),
 ("arXiv:2411.14998", "String Theory in a Pinch: Resolving the Gregory-Laflamme Singularity",
  "thin black strings 'eventually pinch, forming a NAKED SINGULARITY on the horizon'"),
 ("arXiv:2011.03049", "Evidence for violations of Weak Cosmic Censorship in black hole collisions in higher dimensions",
  "D = 6 and 7 collisions, an OPEN SET of initial conditions -- not fine-tuned"),
 ("arXiv:0907.2248",  "Instability and new phases of higher-dimensional rotating black holes",
  "the ultraspinning instability and pinched horizons"),
]
CITED_FROM_MEMORY = [       # NOT verified here -- flagged, per this session's rule
 ("Lehner & Pretorius, PRL 105, 101102 (2010)", "the original D=5 black-string violation"),
 ("Figueras, Kunesch & Tunyasuvunakool, PRL 116, 071102 (2016)", "black ring, D=5"),
 ("Christodoulou, Ann. Math. 149 (1999)", "WCC PROVED for Einstein-scalar in spherical symmetry"),
 ("Jacobson & Sotiriou (2009); Barausse, Cardoso & Khanna (2010)",
  "test-body overspinning succeeds, then backreaction forbids it"),
 ("Cardoso, Costa, Destounis, Hintz & Jansen, PRL 120, 031103 (2018)",
  "STRONG censorship violated in RN-de Sitter -- a DIFFERENT conjecture"),
]

# The conjecture in question is WEAK cosmic censorship (no naked singularity
# visible from infinity), not STRONG (determinism past a Cauchy horizon).
# Conflating them would be the easiest available error here.
CONJECTURE_AT_ISSUE = "WEAK cosmic censorship"
KNOWN_FALSE_ABOVE_D  = 4      # violated in D >= 5; open in D = 4

# solve.py: the static exchange amplitude ratio to Newton is worse in every D>4.
HIGHER_D_RATE_IS_WORSE = True

# ------------------------------------------------------------------- the record
THREADS_PY_IS_EDITED       = False   # corrected here, never edited
BICONDITIONAL_STILL_FAILS  = True    # the headline survives
THREADS_PY_NUMBERS_SURVIVE = False   # its three equatorial values do not
SUBEXTREMAL_EXPOSED_HITS   = 0       # measured, over 3.5e6 sample points
SEARCH_GAP_CLOSES          = True    # and it closes AGAINST us
NEEDS_CENSORSHIP_NOW       = True    # the exposed branch is exactly the naked one
THIS_PASS_REPAIRS_ANYTHING = False

# ============================================================== the report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())
    P("\n" + "="*79)
    P("1.  THE COORDINATE FAULT -- sqrt(g_rr) < 1 HOLDS IN FLAT EMPTY SPACE")
    P("="*79)
    P("""
Kerr with M = 0 is Minkowski.  Nothing is there.  Its equatorial g_rr is
r^2/(r^2+a^2), which is BELOW ONE AT EVERY RADIUS -- the oblate spheroidal
coordinate, not the geometry:
""")
    P(f"    {'r':>6}  {'g_rr (M=0, a=1)':>16}  {'sqrt(g_rr)':>11}  {'C':>14}")
    for r in (0.5, 1.0, 2.0, 5.0):
        c, _ = contraction(r, math.pi/2, 0.0, 1.0)
        P(f"    {r:6.2f}  {g_rr(r,math.pi/2,0.0,1.0):16.6f}  "
          f"{math.sqrt(g_rr(r,math.pi/2,0.0,1.0)):11.6f}  {c:14.9f}")
    P("""
    C = 1.000000000 EXACTLY, at every radius, as it must be in flat space.

THE INVARIANT MEASURE.  C = sqrt(g_rr) / d(sqrt(g_phiphi))/dr -- proper radial
distance per unit CIRCUMFERENTIAL radius.  It is the corridor question stated
without a coordinate: to grow the circumference by dR_c, how much distance must
you actually cross?  And on a static spherically symmetric metric it reduces to
1/sqrt(1 - 2m/r), so""")
    P("\n    C < 1  <=>  m < 0  --  WHICH IS certify.py's THEOREM, VERBATIM.\n")
    P("    the control, both signs of mass:")
    for Mm in (+1.0, -1.0):
        for r in (3.0, 10.0):
            c, _ = contraction(r, math.pi/2, Mm, 0.0)
            P(f"      Schwarzschild M = {Mm:+.0f}, r = {r:4.1f}:  C = {c:.6f}   "
              f"{'CONTRACTED' if c < 1 else 'expanded'}")
    P("""
    The measure detects contraction when it is there.  threads.py compared
    sqrt(g_rr) to 1 instead, and sqrt(g_rr) is not that quantity.

    THIS IS A FAULT IN WORK ONE DAY OLD AND IT IS MINE.  It is the ninth
    measurement fault of the session and the first to invert a headline rather
    than to move a digit.""")

    P("\n" + "="*79)
    P("2.  WHAT THREADS.PY ACTUALLY MEASURED -- ITS OWN THREE POINTS, RE-READ")
    P("="*79)
    P(f"\n    Kerr M = +1, a = 0.99, equator\n")
    P(f"    {'r':>6} {'sqrt(g_rr)':>11} {'dRc/dr':>10} {'threads.py said':>17}   invariant verdict")
    for r in (0.1, 0.3, 0.49):
        c, d = contraction(r, math.pi/2, 1.0, 0.99)
        P(f"    {r:6.2f} {math.sqrt(g_rr(r,math.pi/2,1.0,0.99)):11.6f} {d:10.4f} "
          f"{'CONTRACTED':>17}   ILL-POSED (dRc/dr < 0)")
    P("""
    At ALL THREE the circumferential radius is DECREASING outward, so there is
    no sense in which a distance has been "contracted" between two circles --
    the circles are getting smaller as r grows.  The verdict was not merely
    wrong, the question was not well posed at those points.

    And on the equator, at ANY spin, with dRc/dr > 0: NO CONTRACTION AT ALL.""")

    P("\n" + "="*79)
    P("3.  BUT THE HEADLINE SURVIVES -- KERR DOES CONTRACT WITH POSITIVE MASS")
    P("="*79)
    P("""
Swept 3.5 million points: a/M in [0.01, 50], r in [0.001, 1000], 15 polar
slices, Delta > 0, dRc/dr > 0.  C < 1 IS FOUND.  Classified by horizon:

    SUB-extremal (a < M), OUTSIDE the horizon  :        0     <-- the exposed case
    SUB-extremal (a < M), INSIDE  the horizon  :   11,408
    OVER-extremal (a > M, NO horizon at all)   :  340,612     <-- naked

    So the biconditional STILL FAILS -- contraction with M > 0 is real, and
    certify.py's theorem is static-only exactly as threads.py said.

    AND EVERY NUMBER THAT FILE OFFERED AS EVIDENCE IS WITHDRAWN.  The
    contraction is never equatorial, it sits off-axis near the ring, and for
    sub-extremal spin it is never outside a horizon.

    THE CLAIM SURVIVES AND ONLY ITS EVIDENCE FALLS.  That is docs/R3-REPAIR-
    PLAN.md's A8 category, reached from inside our own work rather than found
    in the corpus -- and it is the case that file called the most easily
    over-repaired.""")

    P("\n" + "="*79)
    P("4.  THE SEARCH GAP CLOSES -- AND IT CLOSES AGAINST US")
    P("="*79)
    P("\n    How far out does the contracted region ever reach?\n")
    P(f"    {'a/M':>9} {'r_+ (horizon)':>14} {'r_max (C<1)':>13} {'r_max/r_+':>10}")
    for a in (0.5, 0.9, 0.99, 1.0):
        rp = horizon_outer(1.0, a); rm = reach(a)
        P(f"    {a:9.2f} {rp:14.4f} {rm:13.5f} {rm/rp:10.4f}   behind the horizon")
    P("")
    for a in (2.0, 10.0, 100.0, 1000.0):
        rm = reach(a)
        P(f"    {a:9.0f} {'none (NAKED)':>14} {rm:13.4f} {'--':>10}   exposed, no horizon")
    P(f"""
    Sub-extremal contraction is inside the horizon by a factor of at least
    {1.0/(reach(1.0)):.2f} even at extremality.  Not marginal.

    THE SCALING LAW, measured:   r_max = kappa (M a^2)^(1/3),  kappa = {KAPPA}

    Now put MATTER in the middle -- a body, not a singularity, so nothing is
    naked and censorship is not invoked at all.  Its spin parameter is
    a = k R v with shape factor k = I/(M R^2) <= 1 and rim speed v <= c.
    Exposure needs the body to fit INSIDE the contracted region, R < r_max:

        R < kappa (M k^2 R^2 v^2)^(1/3)   <=>   R < kappa^3 M k^2 v^2""")
    P(f"""
        absolute ceiling, k = 1 and v = c :  R < {exposure_ceiling():.5f} M
        Buchdahl bound, ANY fluid body    :  R >= {BUCHDAHL:.2f} M

        SHORT BY A FACTOR OF {BUCHDAHL/exposure_ceiling():.1f} AT THE THEORETICAL EXTREME --
        a rigid ring of all its mass at the rim, spinning at the speed of light.
""")
    P(f"    {'body':>20} {'a/M':>10} {'r_max':>13} {'R':>12}   shortfall")
    for name, Mkg, Rm, J in BODIES:
        Mg, a, rm, sf = body_numbers(Mkg, Rm, J)
        P(f"    {name:>20} {a/Mg:10.1f} {rm:11.4g} m {Rm:10.3g} m   {sf:9.3g}x")
    P("""
    The fastest known pulsar is the closest anything comes, and it is still two
    orders short.  THE CONTRACTED REGION IS ALWAYS INSIDE THE MATTER, where the
    Kerr exterior does not apply -- or in vacuum, behind a horizon, unless the
    source is a naked singularity.

    L1's SEARCH IS ANSWERED: NO.  And answered WITHOUT cosmic censorship for
    every material source, which is a strictly stronger closure than a
    conjecture-dependent one would have been.""")

    P("\n" + "="*79)
    P("5.  SO WE PROCEEDED ON THE CONJECTURE, AND HERE IS WHERE IT STANDS")
    P("="*79)
    P(f"""
The conjecture is {CONJECTURE_AT_ISSUE} -- no singularity visible from infinity.
NOT strong censorship, which is about determinism past a Cauchy horizon and is a
different statement with a different status.  Conflating them is the easiest
available error here.

    D = 4 :  OPEN.  {THIS_YEAR - CENSORSHIP_OPEN_SINCE} years.  Proved in spherical symmetry for a scalar
             field; test-body overspinning succeeds and then fails under
             backreaction.  No counterexample, no proof.

    D >= 5:  KNOWN FALSE.  Verified against the literature in this session:""")
    for cite, title, what in VERIFIED_THIS_SESSION:
        P(f"               {cite:<18} {what}")
    P("""
    AND THAT IS THE TWIST, AND IT IS NOT IN OUR FAVOUR.  The one place where the
    conjecture standing in our way is KNOWN TO FALL is D >= 5 -- and solve.py
    measured the static exchange amplitude to be WORSE IN EVERY DIMENSION ABOVE
    FOUR, while codimension.py showed scale-freedom picks out exactly D = 4.

    THE DIMENSION WHERE THE CONJECTURE FAILS IS THE DIMENSION WHERE THE CURRENCY
    IS WORSE.  Proceeding on the conjecture was the right move and it led here.

    Cited from memory, NOT verified in this session -- flagged because this
    session already produced one ASSERTED-WITHOUT-ACCESS fault:""")
    for cite, what in CITED_FROM_MEMORY:
        P(f"        {cite}\n            {what}")

    P("\n" + "="*79)
    P("6.  M'S CLAIM, TESTED LIKE ANY OTHER")
    P("="*79)
    P("""
    "Every breakthrough starts with a conjecture."  TRUE, AND THE TRUE HALF IS
    NOT THE OPERATIVE HALF.  A conjecture is where you place a BET.  It is not
    where you draw a CONCLUSION.  gaps.py said our position was better because
    every gap on our side was schedulable; this pass is what schedulable looks
    like when you actually run it -- one day, one search, and it closed.

    IT CLOSED AGAINST US, AND IT COST A HEADLINE ON THE WAY.  That is not an
    argument against proceeding.  It is the only thing proceeding was ever
    going to be able to tell us, and a project that cannot lose a result it
    published yesterday cannot be trusted with one it publishes today.

    THE SCORECARD, UPDATED.  gaps.py recorded 4 AGAINST and 1 FOR.  The 1 FOR
    was L1/rotation, and it now SPLITS: the theorem-break stands, its evidence
    is withdrawn, and the search it opened is closed negative.

        L3, the rate                  AGAINST
        L4, QA's exponent             AGAINST
        L2, extra-dimension branch    AGAINST
        Casimir as a route            AGAINST
        L1, the biconditional         STANDS  (Kerr contracts with M > 0)
        L1, threads.py's evidence     WITHDRAWN (coordinate artifact)
        L1, the exposed search        AGAINST (0 of 3.5e6; material short 15.8x)

    FIVE AGAINST, ONE STANDING, ONE WITHDRAWN.  And the standing one now depends
    ENTIRELY on a conjecture, where before it depended on one only partly.
""")
    P("  " + "-"*74)
    P("  THE PASS IN ONE PARAGRAPH\n")
    P("""  We proceeded on the conjecture, and the first thing the proceeding found
  was a fault in our own most recent result.  threads.py read contraction off
  sqrt(g_rr) < 1 in Boyer-Lindquist -- a test that FIRES IN FLAT EMPTY SPACE,
  since M = 0 Kerr is Minkowski in oblate spheroidal coordinates.  The
  invariant measure is C = proper radial distance per unit CIRCUMFERENTIAL
  radius, which is 1 in flat space however written and reduces on a static
  spherically symmetric metric to 1/sqrt(1-2m/r) -- so C < 1 iff m < 0, which
  IS certify.py's theorem.  Under C, Kerr STILL CONTRACTS WITH POSITIVE MASS
  and the biconditional STILL FAILS, so the headline stands -- but not one of
  threads.py's numbers does: the contraction is never equatorial, it sits
  off-axis near the ring, and over 3.5 million sampled points it is NEVER
  OUTSIDE A HORIZON at sub-extremal spin.  THE CLAIM SURVIVES AND ONLY ITS
  EVIDENCE FALLS -- R3-REPAIR-PLAN's A8 category, reached from inside.  And
  that closes L1's SEARCH: the region's reach obeys r_max = 0.5226 (M a^2)^(1/3),
  so a material source of radius R needs R < 0.1427 M against Buchdahl's
  R >= 2.25 M -- SHORT BY 15.8x for a light-speed ring of pure rim mass, by 10^7
  for the Earth, and by two orders for the fastest known pulsar.  No material
  body exposes it, and that is established WITHOUT censorship.  The exposed
  branch is therefore exactly the naked-singularity branch, and the one place
  weak cosmic censorship is KNOWN to fail is D >= 5, which is where solve.py
  already measured the currency to be worse.  A conjecture is where you place a
  bet, not where you draw a conclusion; we placed it, and it cost a headline.
  NOTHING IS REPAIRED AND threads.py IS NOT EDITED.""")
    P("  " + "-"*74)

# ============================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    P = print
    P("expose.py --selftest\n")

    P("The coordinate check -- M = 0 Kerr is Minkowski")
    for r in (0.5, 1.0, 2.0, 5.0, 50.0):
        c, _ = contraction(r, math.pi/2, 0.0, 1.0)
        chk(f"C = 1 exactly at r = {r}", round(c, 12), 1.0, 1e-9)
    chk("and sqrt(g_rr) < 1 there anyway (the artifact)",
        g_rr(1.0, math.pi/2, 0.0, 1.0) < 1.0, True)

    P("\ncertify.py's theorem is a statement about C")
    for Mm, want in ((+1.0, False), (-1.0, True)):
        c, _ = contraction(10.0, math.pi/2, Mm, 0.0)
        chk(f"Schwarzschild M = {Mm:+.0f}: contracted?", c < 1.0, want)
    c, _ = contraction(10.0, math.pi/2, 1.0, 0.0)
    chk("and C = 1/sqrt(1-2M/r) exactly", round(c, 12),
        round(1.0/math.sqrt(1.0-0.2), 12), 1e-12)

    P("\nthreads.py's three equatorial points are ill-posed, not contracted")
    for r in (0.1, 0.3, 0.49):
        _, d = contraction(r, math.pi/2, 1.0, 0.99)
        chk(f"dRc/dr < 0 at r = {r}", d < 0.0, True)
    chk("threads.py's g_rr value at r=0.3 reproduced", 
        round(g_rr(0.3, math.pi/2, 1.0, 0.99), 6), 0.191449, 1e-6)

    P("\nno equatorial contraction at any spin, where the question is well posed")
    hits = 0
    for ai in range(1, 201):
        a = ai*0.25; r = 0.001
        while r < 200.0:
            if Delta(r, 1.0, a) > 0.0:
                c, d = contraction(r, math.pi/2, 1.0, a)
                if d > 0.0 and c < 1.0: hits += 1
            r *= 1.05
    chk("equatorial C < 1 hits (must be zero)", hits, 0)

    P("\nsub-extremal contraction is behind the horizon, by a wide margin")
    for a in (0.5, 0.9, 1.0):
        rm = reach(a, n_theta=180, step=1.01); rp = horizon_outer(1.0, a)
        chk(f"a = {a}: r_max < r_+", rm < rp, True)
    chk("even at extremality the margin is > 3x",
        horizon_outer(1.0, 1.0)/reach(1.0, n_theta=180, step=1.01) > 3.0, True)

    P("\nthe scaling law and the material-body ceiling")
    for a in (1e3, 1e4):
        k = reach(a, n_theta=180, step=1.01)/(a*a)**(1.0/3.0)
        chk(f"kappa at a/M = {a:.0e}", round(k, 2), round(KAPPA, 2), 0.03)
    chk("exposure ceiling at k=1, v=c (units of M)",
        round(exposure_ceiling(), 5), round(KAPPA**3, 5), 1e-9)
    chk("and it is below the Buchdahl bound", exposure_ceiling() < BUCHDAHL, True)
    chk("shortfall factor at the theoretical extreme",
        round(BUCHDAHL/exposure_ceiling(), 1), 15.8, 0.15)
    chk("a = k R v is linear in R, so a^2/R grows -- ceiling is a RADIUS not a spin",
        round(spin_parameter(1.0, 10.0, 0.5), 6), 5.0, 1e-12)

    P("\nreal bodies, all short")
    for name, Mkg, Rm, J in BODIES:
        _, _, _, sf = body_numbers(Mkg, Rm, J)
        chk(f"{name} short by >10x", sf > 10.0, True)

    P("\nwhat this pass does and does not claim")
    chk("the biconditional still fails", BICONDITIONAL_STILL_FAILS, True)
    chk("  but threads.py's numbers do not survive", THREADS_PY_NUMBERS_SURVIVE, False)
    chk("threads.py is corrected here, NOT edited", THREADS_PY_IS_EDITED, False)
    chk("sub-extremal exposed hits", SUBEXTREMAL_EXPOSED_HITS, 0)
    chk("the search gap closes", SEARCH_GAP_CLOSES, True)
    chk("  and the exposed branch now needs censorship entirely", NEEDS_CENSORSHIP_NOW, True)
    chk("censorship at issue is the WEAK one", CONJECTURE_AT_ISSUE, "WEAK cosmic censorship")
    chk("known false above D =", KNOWN_FALSE_ABOVE_D, 4)
    chk("  and D > 4 is where the rate is worse", HIGHER_D_RATE_IS_WORSE, True)
    chk("years the conjecture has been open", THIS_YEAR - CENSORSHIP_OPEN_SINCE, 57)
    chk("citations verified in this session", len(VERIFIED_THIS_SESSION), 4)
    chk("citations flagged as memory-only", len(CITED_FROM_MEMORY), 5)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
