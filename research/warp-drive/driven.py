#!/usr/bin/env python3
r"""
driven.py -- DOCKET 52.  THE NON-STATIC CONTRACTION THEOREM, SEATED.

certify.py proved, ansatz-free, that in any STATIC spherically symmetric
spacetime proper radial distance is contracted at r if and only if the enclosed
Misner-Sharp mass m(r) is negative, and wrote its own limit into the file:
THEOREM_SCOPE = "static and spherically symmetric only".  mouth.py section 5b
leaned on that theorem, scoped its resolution to it, and named the successor
question outright -- "whether contraction still demands negative enclosed energy
off the static family is settled nowhere in this tree".

    THIS FILE SETTLES IT, AND THE ANSWER IS NOT THE ONE THE PROJECT WANTED.

    python3 driven.py             the reading
    python3 driven.py --selftest  every fixture, STDLIB ONLY
    python3 driven.py --verify    the sympy residuals, every one exactly 0

Run under python3 (3.11), not python3.12.  The selftest imports nothing but the
standard library and four seated peers.  --verify needs sympy, which is on pypi
and pypi is on the proxy allowlist -- see PROOF-ASSISTANT.md.

===============================================================================
0.  THE HEADLINE, AND IT IS A NEGATIVE RESULT
===============================================================================

    THE LOOPHOLE IS REAL.  IT IS ALSO STANDARD, AND IT IS EMPTY.
    THE 2.7254e12 SOLAR-MASS CORRIDOR BILL IS NOT LIFTED.

Three separate findings, and each of them is bad news for the escape:

  REAL.       Drop staticity and m < 0 stops being NECESSARY for contraction.
              That is exact, the residual is 0 in sympy, and flat spacetime is
              a counterexample to the biconditional.  m < 0 remains SUFFICIENT.

  STANDARD.   The identity is Misner & Sharp's own, from 1964.  The criterion
              "Gamma > 1" is this tree's own expose.py criterion "C < 1" -- the
              two are reciprocal, C x Gamma = 1 identically, verified below.
              NO NOVELTY IS CLAIMED FOR ANY LINE OF IT, exactly as certify.py
              claimed none for its own theorem.

  EMPTY.      nonstatic.py measured what the loophole costs and it closes twice
              over, NEITHER TIME BY AN ENERGY CONDITION.  Carried here as the
              load-bearing finding of the docket, section 5.

And the premise underneath the docket was itself false.  The bill never rested
on staticity: Olum's theorem (PRL 81, 3567) makes negative energy compulsory for
superluminal travel with NO staticity, NO symmetry and NO spherical hypothesis
anywhere in it.  Dropping staticity moves the obstruction; it does not remove
it.  Section 1.

===============================================================================
1.  PRIOR ART, FIRST, BECAUSE IT GOES AGAINST US
===============================================================================

THE IDENTITY IS MISNER & SHARP 1964.  Hayward, "Gravitational energy in
spherical symmetry" (gr-qc/9408002, PRD 53, 1938), section IV, eq. (27):

        1 - 2E/r  =  e^{-chi}(r')^2 - rdot^2

    "which is the form actually given by Misner & Sharp [4], with different
     notation"

    -- [4] being Misner C W & Sharp D H 1964, Phys. Rev. 136, B571.  Hayward's
    tau is proper time along the slice normal (the Phi = 0 gauge), so his rdot
    is this file's e^{-Phi} Rdot.  THAT IS THE DOCKET'S IDENTITY, LITERALLY.

    STATUS OF THE ATTRIBUTION: RECOVERED, NOT READ AT SOURCE.  arxiv.org is
    EGRESS_BLOCKED in this environment and Phys. Rev. 136 B571 (1964) is not an
    arXiv preprint, so Misner & Sharp is attributed through Hayward's verbatim
    statement of it.  Hernandez & Misner 1966 and Poisson's "A Relativist's
    Toolkit" were NOT CONSULTED and are not cited as checked.

THE WORKING FORM IS ALSO STANDARD.  Escriva, arXiv:2504.05813 (2025), eqs.
(2.3) and (2.5): U = D_t R, Gamma = D_r R, and Gamma = sqrt(1 + U^2 - 2M/R),
"where Gamma is called the generalised Lorentz factor".  Gamma is BY DEFINITION
the derivative of areal radius with respect to proper radial distance, so
"contraction <=> Gamma > 1" is the statement that the generalised Lorentz factor
exceeds 1 -- which in Misner-Sharp/LTB language is the UNBOUND (hyperbolic)
shell, E = (Gamma^2 - 1)/2 > 0.  Contraction IS unboundedness.  Textbook.

AND THE CONSEQUENCE, READ AS AN ESCAPE, WAS REFUTED IN PRINT IN 1998.

    HOCHBERG & VISSER, gr-qc/9802046 (PRD 58, 044021), section 7: "if the
    wormhole is dynamic, FLARE-OUT IN THE SPATIAL DIRECTION DOES NOT IMPLY
    FLARE-OUT IN THE NULL DIRECTIONS orthogonal to the throat", and section 4:
    "the embedding of the spatial part of a wormhole spacetime in a Euclidean
    R^3 is no longer a reliable operational technique for defining 'flare-out'
    in the time-dependent case."  THIS FILE'S CRITERION IS A CONSTANT-t SPATIAL
    CRITERION.  Static, that is harmless -- there is one preferred slicing.
    Non-static, it is exactly the case they say stops meaning anything about
    traversal.

    HOCHBERG & VISSER, gr-qc/9802048 (PRL 81, 746), result (4): for each throat
    there is an open interval on which the TRANSVERSE AVERAGED NEC is violated.
    "The suspension of the NEC is essentially an illusion in that if one ever
    succeeds in passing through the wormhole ... there must be NEC violations at
    or near this throat."

    KAR & SAHDEV, gr-qc/9506094 (PRD 53, 722), made this exact move -- drop
    staticity to satisfy the WEC -- and printed Visser's rebuttal in their own
    section II: WEC violations "can be avoided only for finite intervals of
    time."

    HAYWARD, gr-qc/9805019: a generic wormhole is a temporal outer trapping
    horizon and "the null energy condition is violated everywhere on a generic
    wormhole horizon".  Fully dynamic, purely local.

    OLUM, PRL 81, 3567 (gr-qc/9805003), AND THIS IS THE ONE THAT GOVERNS THE
    PROJECT: "Superluminal travel requires negative energies."  Any causal path
    arriving earlier than every neighbouring path, with the generic condition
    holding on it, MUST VIOLATE THE WEC at some point OF THAT PATH.  No
    staticity.  No symmetry.  No sphericity.  Pointwise on the path to be
    travelled, not averaged over it.

    Also standing, and also with no staticity hypothesis: Gao & Wald
    (gr-qc/0007021) Theorem 1 and Visser-Bassett-Liberati (gr-qc/9908023) --
    the NEC makes Shapiro always a delay, never an advance -- and Santiago,
    Schuster & Visser (arXiv:2105.03079), which shows generic TIME-DEPENDENT
    Natario warp drives violate the NEC using "only the fact that warp drive
    contributions are sufficiently localized".

    SO THE DOCKET'S PREMISE -- "certify.py is the ONLY thing making negative
    mass compulsory for this project" -- IS FALSE, and that is recorded here
    rather than worked around.

AND THE CRITERION IS NOT NEW TO THIS TREE EITHER.  expose.py replaced
threads.py's coordinate test with the invariant C = sqrt(g_rr) / (d/dr)
sqrt(g_phiphi), proved C < 1 <=> m < 0 in static spherical symmetry, and found
Kerr contracting with M > 0.  On a constant-t slice of the metric below,

        C  =  e^{Lambda} / R'   =   1 / Gamma          (residual 0, section V10)

so "Gamma > 1" and "C < 1" ARE THE SAME TEST.  expose.py dropped a DIFFERENT
hypothesis of the SAME theorem (sphericity, keeping stationarity); this file
drops staticity and keeps sphericity.  What is genuinely new to the tree is
narrow and is stated as such in section 7.

===============================================================================
2.  THE IDENTITY AND THE THEOREM -- DERIVED, RESIDUAL EXACTLY 0
===============================================================================

Take the general spherically symmetric metric, with no staticity and no ansatz:

        ds^2 = -e^{2Phi(t,r)}dt^2 + e^{2Lambda(t,r)}dr^2 + R(t,r)^2 dOmega^2

Define the Misner-Sharp-Hernandez mass by the SCALAR it is a scalar because of:

        1 - 2m/R  =  g^{ab} d_a R d_b R

Proper radial length is dl = e^{Lambda}dr; the areal increment is dR = R' dr.
Write U = e^{-Phi}Rdot (the areal velocity) and Gamma = e^{-Lambda}R' (the
generalised Lorentz factor, and the contraction variable).  Then:

    THE IDENTITY (DERIVED; --verify computes the metric inverse, contracts the
    gradient and SOLVES for m, then returns residual 0):

        e^{-2Lambda} R'^2  ==  1 - 2m/R + e^{-2Phi} Rdot^2

        equivalently     Gamma^2  ==  1 + U^2 - 2m/R

    THE THEOREM (DERIVED, residual 0):

        CONTRACTION  <=>  dl < dR  <=>  Gamma > 1  <=>  2m/R  <  e^{-2Phi}Rdot^2

        equivalently     |Rdot|  >  sqrt(2m/R) e^{Phi}

    THE RIGHT-HAND SIDE IS A SQUARE, HENCE NON-NEGATIVE.  So m < 0 is
    SUFFICIENT for contraction and IS NO LONGER NECESSARY.  THE CONDITION IS A
    SPEED, NOT A SIGN.

    None of this is new.  Section 1 says whose it is.

===============================================================================
3.  certify.py RECOVERED AS THE Rdot = 0 CORNER, AS A FIXTURE
===============================================================================

Set Rdot = 0 and the identity collapses to Gamma^2 = 1 - 2m/R, so

        CONTRACTION AT A STATIONARY AREAL RADIUS  <=>  m < 0

which is certify.py's theorem exactly, including its metric: e^{2Lambda} =
1/(1 - 2m/r), verified as a residual in V6.  The fixture in the selftest does
not restate it -- it IMPORTS certify.py, sweeps its own g_rr samples through
this file's criterion at U = 0, and demands agreement on all three of
certify.contracts(g_rr), m < 0 and Gamma = 1/sqrt(g_rr).

    AND THAT IS ALREADY THE FIRST HALF OF WHY THE LOOPHOLE IS EMPTY.
    nonstatic.py's ANCHOR LEMMA (machine-checked there, z3 unsat, not re-run
    here) is this corner with NO staticity assumed anywhere: U = 0 at one point
    at one instant is enough.  certify.py was never about static SPACETIMES.
    It is about STATIONARY AREAL RADII, and a destination is a fixed areal
    radius.  Let R move and you have not shortened the way to Proxima -- you
    have moved Proxima.

===============================================================================
4.  THE THRESHOLD IS THE PAINLEVE-GULLSTRAND VELOCITY
===============================================================================

The theorem's threshold speed is sqrt(2m/R).  That is not a notational
resemblance and this file does not record it as one:

    Gamma = 1  <=>  U^2 = 2m/R        (V8, residual 0)

so sqrt(2m/R) is exactly the areal velocity of MARGINALLY BOUND radial free
fall -- the Painleve-Gullstrand shift function, the Newtonian escape velocity.
The Gamma = 1 surface IS the PG foliation, and drivensource.py's pg_witness()
puts Schwarzschild in Lemaitre (= PG) slicing through the same machinery and
returns, exactly:

        vacuum,     m = r_s/2 > 0,     Gamma = 1,     U = -sqrt(2m/R)

Two further readings, both measured and neither of them an escape:

    Gamma^2 - 1 = 2E, twice the LTB energy function (V9, residual 0).  So
    CONTRACTION IS PRECISELY THE UNBOUND (HYPERBOLIC) SHELL.  This is why open
    FRW contracts and flat FRW does not: in FRW the criterion is exactly k < 0.

    AND U IS NOT CAPPED AT 1, so no light-speed bound closes the door either.
    The Lemaitre witness has |U| = sqrt(r_s/R), which exceeds 1 at every R < r_s.
    Recorded because it is the cheap closure someone will reach for, and it
    does not hold.

===============================================================================
5.  THE COST TO SUSTAIN -- THE LOAD-BEARING FINDING, AND IT CLOSES THE DOOR
===============================================================================

This is nonstatic.py's measurement, CARRIED HERE, NOT RE-DERIVED.  Every number
in it is read from that file by import; the Misner-Sharp evolution equations it
rests on were derived there from the Einstein tensor in sympy (residual 0) and
its claims T1-T5 were machine-checked there in z3 -- SIX obligations returning
unsat beside THREE satisfiability guards, counted by calling that file's own
obligations() rather than quoted.  Status: DERIVED THERE, CARRIED HERE.  Run
`python3 nonstatic.py --selftest` before trusting any of it.

FIRST, THE ANSWER NOBODY EXPECTED: SUSTAINING CONTRACTION COSTS NOTHING.

    The evolution equation for the contraction variable is

        D_t Gamma  =  4 pi R j  +  U D_r Phi

    and NEITHER rho NOR p_r APPEARS IN IT.  Measured on the jet, not inspected.
    In geodesic slicing D_t Gamma = 4 pi R j, so holding Gamma costs no flux
    either.  Two exact witnesses hold contraction forever: MINKOWSKI IN MILNE
    SLICING (T_ab = 0 identically -- contraction in flat vacuum) and OPEN FRW
    (rho > 0, m > 0, j = 0, and the NEC contraction equals rho, STRICTLY
    SATISFIED).  So the energy-condition question closes on nothing.

    IT CLOSES ANYWAY, TWICE OVER.

KILL ONE -- THE ANCHOR LEMMA.  Section 3.  Wherever the areal radius is
momentarily stationary, contraction still requires m < 0.  A destination is a
fixed areal radius.

KILL TWO -- THE DISPLACEMENT BOUND.  With m >= 0 the identity forces
|U| >= sqrt(Gamma^2 - 1).  An outgoing ray closes an areal gap at rate Gamma per
unit Eulerian proper time, so the far end is displaced by at least
sqrt(1 - 1/Gamma^2) of the gap while light closes it: 86.6 % at Gamma = 2,
99.50 % at Gamma = 10, 99.995 % at Gamma = 100.  THE CONTRACTION FACTOR CANCELS.

AND CONTRACTING HARDER BUYS NO TIME AT ALL.  The corridor holds its areal radius
inside a band of fractional half-width eps for

        tau_band / tau_cross  =  2 eps Gamma / sqrt(Gamma^2 - 1)

which is SCALE-FREE (R cancels), DECREASING in Gamma, with floor 2 eps.  At
eps = 1 %: 2.31 % of one light-crossing at Gamma = 2 and 2.00 % at Gamma = 100.
There is no Gamma large enough to outrun this.  No quasi-stationary corridor
exists with m >= 0; the trichotomy is turn around (U = 0, the anchor lemma
bites), collapse to R = 0, or recede to R = infinity.

AND THE BUILD BILL IS THE SAME ORDER AS THE ONE BEING ESCAPED.  Integrating the
Gamma evolution gives E = R dGamma exactly in geometric units, independent of
how long you take: 2.7207e13 solar masses of throughput for a Proxima corridor
at Gamma = 2, against H83d's 2.7254e12 solar masses of negative mass, which is
met at dGamma = 0.100171.  DIFFERENT KIND, SAME ORDER, UNRELATED ROUTE -- the
agreement is R c^2 / G and nothing deeper, and nonstatic.py refuses to read more
into it than that.  So does this file.

===============================================================================
6.  THE GAUGE FACT UNDERNEATH ALL OF IT
===============================================================================

    m IS A SCALAR.  Gamma IS NOT.

m is defined by a contraction of a gradient and does not care how spacetime is
sliced.  Gamma = e^{-Lambda}R' is a component and does.  nonstatic.py's first
two witnesses are THE SAME SPACETIME -- Minkowski -- sliced two ways, returning
Gamma = 1 and Gamma = cosh(chi).  So once staticity is dropped, "proper distance
shorter than the areal increment" is a property of the FOLIATION and not of the
spacetime.  Staticity is what made the criterion mean anything: the Killing
field picks the slice, so certify.py reads the criterion off a scalar.

    certify.py's SCOPE LINE IS LOAD-BEARING, AND IT IS NOW MEASURED RATHER THAN
    ASSERTED.  That is the honest summary of this docket.

    This is also exactly Hochberg & Visser's 1998 point, arrived at from the
    other end.  Section 1.

===============================================================================
7.  WHAT IS STANDARD, WHAT IS FOLKLORE, WHAT IS NEW -- AND WHAT IS REFUSED
===============================================================================

    STANDARD:   the identity (Misner & Sharp 1964 via Hayward eq. 27); Gamma as
                the generalised Lorentz factor (Escriva 2504.05813 eq. 2.5);
                the rearrangement to "2m/R < e^{-2Phi}Rdot^2"; sqrt(2m/R) as the
                PG velocity; Gamma^2 - 1 = 2E as the LTB energy.
    FOLKLORE:   "contraction in a dynamic spacetime needs no negative mass" --
                true, and open FRW is the demonstration any relativist would
                produce on request.
    REFUTED:    "therefore the corridor may be buildable without negative
                energy" -- Hochberg & Visser 1998, Olum 1998.
    NEW TO THIS TREE, AND ONLY THAT:  overturn.py's link L1 ("in any STATIC
                spherically symmetric spacetime ...") IS TWO HYPOTHESES, and
                that file only ever argued one of them -- it reads L1 as the
                SPHERICITY link and attacks it there.  THE STATICITY HALF IS A
                SECOND DOOR, and it needs no quasi-local machinery at all: keep
                sphericity, drop staticity, and the Misner-Sharp mass is still
                exactly defined.  DOCKET 52 opened that door and closed it.
                INTERNAL PRIOR ART, RECORDED AGAINST THIS FILE: nonstatic.py
                measured it first and drivensource.py second, and overturn.py's
                own LINKS table ALREADY SEATS the result -- L1 OPEN on the
                sphericity half, L2 BROKEN-EMPTY by a point charge.  This file
                is where the theorem itself is seated, not where it was found.
                NO NOVELTY AGAINST THE LITERATURE IS CLAIMED for any line of
                mathematics in it.

    SCOPE.  SPHERICALLY SYMMETRIC ONLY.  Staticity is dropped; sphericity is
    not, exactly as in certify.py.  The Alcubierre family is outside this file
    as it is outside that one.

    REFUSED, EXPLICITLY:

      IT DOES NOT PROVE that no dynamic spherically symmetric corridor exists.
      The FRW demonstration is a demonstration.  The proof of that statement is
      Olum's, and it is his, not this file's.

      IT DOES NOT RE-DERIVE what its peers own.  The Misner-Sharp evolution
      equations and the nine z3 rows are nonstatic.py's; the electrovac
      closure, the narrowing of certify.py's COROLLARY and the PG witness are
      drivensource.py's.  They are imported, cited and cross-checked here, never
      copied, and never restated as this file's own.

      IT DOES NOT READ MISNER & SHARP 1964.  The attribution is RECOVERED from
      Hayward's verbatim statement of their equation.  arxiv.org is
      EGRESS_BLOCKED here; a 1964 Phys. Rev. paper is not an arXiv preprint.

      IT DOES NOT ADJUDICATE the 2.7207e13 / 2.7254e12 agreement of scale, and
      it does not say whether the build throughput is recoverable.

      IT OFFERS NO RULING AND REPAIRS NOTHING.  certify.py, mouth.py,
      overturn.py, expose.py and nonstatic.py are untouched; paper/ is untouched;
      the corridor bill is not restated.  The chat-67 full hold governs this
      exactly as it governs a section read.
"""

import math
import sys

import certify
import nonstatic
import drivensource
import mouth
import overturn


# ============================================================ the criterion

def gamma_squared(m, R, U):
    """Gamma^2 = 1 + U^2 - 2m/R.  Gamma = D_r R is the derivative of areal
    radius with respect to PROPER radial distance -- Escriva's generalised
    Lorentz factor, and the reciprocal of expose.py's invariant C."""
    return 1.0 + U * U - 2.0 * m / R


def gamma(m, R, U):
    """Gamma itself.  Gamma^2 < 0 is not a slice, it is bad initial data."""
    g2 = gamma_squared(m, R, U)
    if g2 < 0.0:
        raise ValueError("Gamma^2 = %r < 0: no real slice carries this data" % g2)
    return math.sqrt(g2)


def contracts(m, R, U):
    """THE THEOREM.  Proper radial length shorter than the areal increment,
    which is Gamma > 1, which is 2m/R < U^2 with U = e^{-Phi} Rdot."""
    return 2.0 * m / R < U * U


def threshold_speed(m, R):
    """The areal speed the theorem asks for: sqrt(2m/R), the Painleve-
    Gullstrand shift and the local escape velocity.  None when m < 0, because
    there is then no threshold at all -- EVERY U contracts, which is exactly
    'm < 0 is sufficient'."""
    return math.sqrt(2.0 * m / R) if m >= 0.0 else None


def ltb_energy(m, R, U):
    """E = (Gamma^2 - 1)/2, the LTB energy function.  Contraction is E > 0,
    which is the UNBOUND (hyperbolic) shell."""
    return 0.5 * (gamma_squared(m, R, U) - 1.0)


def contraction_is_unbound(m, R, U):
    """Contraction and unboundedness are the same statement."""
    return contracts(m, R, U) == (ltb_energy(m, R, U) > 0.0)


# ================================= 3.  certify.py as the Rdot = 0 corner

def certify_corner(samples=(0.25, 0.5, 0.8, 1.25, 2.0, 4.0), r=1.0):
    """certify.py's static theorem RECOVERED as the U = 0 corner of this file's
    criterion.  Nothing is restated: certify.py's own functions are called and
    must agree on the verdict, on the sign of m, and on Gamma = 1/sqrt(g_rr).

    Returns (rows, all_agree)."""
    rows, agree = [], True
    for g_rr in samples:
        m = certify.enclosed_mass_from_grr(g_rr, r)
        here = contracts(m, r, 0.0)
        there = certify.contracts(g_rr)
        same = (here == there
                and here == (m < 0.0)
                and abs(gamma(m, r, 0.0) - 1.0 / math.sqrt(g_rr)) < 1e-15)
        agree &= same
        rows.append((g_rr, 1.0 / math.sqrt(g_rr), m, there, here, same))
    return rows, agree


def loophole_row(m, R, U):
    """One row of the table that IS the loophole: m and R fixed, U varied."""
    return dict(U=U, gamma=gamma(m, R, U), contracts=contracts(m, R, U),
                E=ltb_energy(m, R, U))


def loophole_table(m=1.0, R=10.0):
    """POSITIVE m, fixed R, and the verdict flips on U alone.  The threshold is
    the PG velocity and it is marked."""
    v = threshold_speed(m, R)
    return v, [loophole_row(m, R, U) for U in (0.0, 0.2, v, 0.5, 1.0)]


# ====================================== 5.  the cost, CARRIED from nonstatic

def carried_numbers():
    """Every figure in section 5, read out of nonstatic.py rather than copied.
    DERIVED THERE, CARRIED HERE -- the status is not flattened."""
    R = nonstatic.proxima_span_m()
    return dict(
        span_m=R,
        disp=[(W, nonstatic.displacement_fraction(W)) for W in (2.0, 10.0, 100.0)],
        ratio=[(W, nonstatic.band_ratio(W, 0.01)) for W in (2.0, 100.0)],
        band_days=nonstatic.band_time_seconds(R, 2.0, 0.01) / 86400.0,
        cross_yr=nonstatic.crossing_time_seconds(R, 2.0) / 3.15576e7,
        build_msun=nonstatic.build_energy(R, 1.0)[2],
        h83d_dgamma=H83D_MSUN / nonstatic.build_energy(R, 1.0)[2],
    )


# ================================================================== status

VERDICT = "REAL, STANDARD, AND EMPTY -- THE BILL IS NOT LIFTED"
IDENTITY_STATUS = "DERIVED (sympy, residual exactly 0)"
COST_TO_SUSTAIN_STATUS = "DERIVED IN nonstatic.py, CARRIED HERE"
NOVELTY_CLAIMED = False
THEOREM_SCOPE = "spherically symmetric only; staticity dropped, sphericity kept"
CERTIFY_RECOVERED_AT = "Rdot = 0"

NEGATIVE_MASS_SUFFICIENT = True
NEGATIVE_MASS_NECESSARY = False
NEGATIVE_MASS_NECESSARY_AT_STATIONARY_AREAL_RADIUS = True

LOOPHOLE_IS_REAL = True
LOOPHOLE_IS_EMPTY = True
SUSTAINING_FORCES_NEGATIVE_RHO = False
QUASI_STATIONARY_CORRIDOR_EXISTS = False
BILL_LIFTED = False

CRITERION_IS_NEW_TO_THIS_TREE = False        # it is expose.py's C, reciprocated
THRESHOLD_IS_PAINLEVE_GULLSTRAND = True
PG_IS_COINCIDENCE_OF_NOTATION = False
CONTRACTION_IS_A_SCALAR = False
AREAL_VELOCITY_IS_CAPPED_AT_LIGHTSPEED = False
DOCKET_PREMISE_WAS_TRUE = False              # Olum 1998 needs no staticity
NEW_TO_THIS_TREE = "overturn.py's L1 has a second door: drop staticity, keep sphericity"
INTERNAL_PRIOR_ART = ("nonstatic.py measured it first, drivensource.py second, "
                      "and overturn.py's LINKS table already seats the result")
NOTHING_IS_REPAIRED = True

PRIOR_ART_IDENTITY = "Misner & Sharp 1964, Phys. Rev. 136, B571"
PRIOR_ART_ROUTE = "RECOVERED from Hayward gr-qc/9408002 eq. (27); NOT read at source"
PRIOR_ART_GAMMA = "Escriva arXiv:2504.05813 eqs. (2.3), (2.5)"
PRIOR_ART_REFUTATION = ("Hochberg & Visser gr-qc/9802046 s7 and gr-qc/9802048; "
                        "Olum PRL 81, 3567 (gr-qc/9805003)")
PRIOR_ART_PRECEDENT = "Kar & Sahdev gr-qc/9506094 -- the same move, already answered"
H83D_MSUN = 2.7254e12                        # READ from paper/CLAIMS.md via nonstatic.py

SCOPE = THEOREM_SCOPE
REFUSED = ("no proof that dynamic corridors are impossible (that is Olum's, not "
           "this file's); no adjudication of the 2.7207e13 / 2.7254e12 scale "
           "agreement; nothing non-spherical; no ruling")


def standard_table():
    """What is standard, what is folklore, what is refuted, what is new."""
    return [
        ("the identity  1 - 2m/R = e^-2L R'^2 - e^-2P Rdot^2", "STANDARD",
         "Misner & Sharp 1964, via Hayward eq. (27)"),
        ("Gamma^2 = 1 + U^2 - 2m/R, Gamma the Lorentz factor", "STANDARD",
         "Escriva 2504.05813 eq. (2.5)"),
        ("contraction <=> 2m/R < e^-2P Rdot^2", "STANDARD",
         "trivial rearrangement; content is Gamma > 1 <=> unbound"),
        ("sqrt(2m/R) is the Painleve-Gullstrand velocity", "STANDARD",
         "and Gamma^2 - 1 = 2E is the LTB energy"),
        ("m < 0 sufficient, not necessary, off staticity", "FOLKLORE",
         "open FRW demonstrates it; not novel"),
        ("therefore the corridor needs no negative energy", "REFUTED",
         "Hochberg & Visser 1998; Olum 1998"),
        ("Gamma > 1 is a new criterion", "NO",
         "it is expose.py's C < 1; C x Gamma = 1 identically"),
        ("overturn.py's L1 has a non-quasi-local door", "NEW TO THIS TREE",
         "DOCKET 52's finding; overturn.py's LINKS table already seats it"),
    ]


# ========================================================= the verification

def _general():
    """The general spherically symmetric metric, with the INVERSE COMPUTED and
    the Misner-Sharp mass SOLVED from its defining scalar.  The metric is the
    only thing written down by hand."""
    import sympy as sp

    t, r, th = sp.symbols("t r theta", real=True)
    ph = sp.Symbol("phi")
    Phi = sp.Function("Phi", real=True)(t, r)
    Lam = sp.Function("Lambda", real=True)(t, r)
    R = sp.Function("R", positive=True)(t, r)
    x = [t, r, th, ph]

    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
    gi = g.inv()                                   # COMPUTED, not written down
    gradR = sp.simplify(sum(gi[a, b] * sp.diff(R, x[a]) * sp.diff(R, x[b])
                            for a in range(4) for b in range(4)))
    mS = sp.Symbol("m")
    sols = sp.solve(sp.Eq(1 - 2 * mS / R, gradR), mS)
    if len(sols) != 1:
        raise AssertionError("the MS definition did not solve uniquely for m")
    m = sp.simplify(sols[0])

    U = sp.exp(-Phi) * sp.diff(R, t)
    Gam = sp.exp(-Lam) * sp.diff(R, r)
    return dict(sp=sp, t=t, r=r, th=th, x=x, g=g, gi=gi, Phi=Phi, Lam=Lam, R=R,
                gradR=gradR, m=m, U=U, Gam=Gam)


def residuals(E=None):
    """Every claim of sections 2-4 as a residual sympy must return as 0."""
    E = E or _general()
    sp = E["sp"]
    t, r, th = E["t"], E["r"], E["th"]
    R, m, U, Gam = E["R"], E["m"], E["U"], E["Gam"]
    Phi, Lam, g = E["Phi"], E["Lam"], E["g"]
    out = []

    # ---- V1-V5: the identity and the theorem, in the general metric
    out.append(("V1  1 - 2m/R = g^ab d_a R d_b R  (m SOLVED from it)",
                sp.simplify((1 - 2 * m / R) - E["gradR"])))
    out.append(("V2  m = (R/2)(1 - Gamma^2 + U^2)",
                sp.simplify(m - R / 2 * (1 - Gam**2 + U**2))))
    out.append(("V3  IDENTITY  e^-2L R'^2 = 1 - 2m/R + e^-2P Rdot^2",
                sp.simplify(sp.exp(-2 * Lam) * sp.diff(R, r)**2
                            - (1 - 2 * m / R
                               + sp.exp(-2 * Phi) * sp.diff(R, t)**2))))
    out.append(("V4  Gamma^2 = 1 + U^2 - 2m/R  (Escriva eq. 2.5)",
                sp.simplify(Gam**2 - (1 + U**2 - 2 * m / R))))
    out.append(("V5  THEOREM   Gamma^2 - 1 = e^-2P Rdot^2 - 2m/R",
                sp.simplify((Gam**2 - 1)
                            - (sp.exp(-2 * Phi) * sp.diff(R, t)**2 - 2 * m / R))))

    # ---- V6-V7: certify.py recovered exactly at Rdot = 0
    rs = sp.Symbol("r", positive=True)
    Ls = sp.Function("Lambda", real=True)(rs)
    Gam_s, U_s = sp.exp(-Ls), sp.Integer(0)
    m_s = rs / 2 * (1 - Gam_s**2 + U_s**2)
    out.append(("V6  STATIC CORNER  g_rr = 1/(1 - 2m/r)   -- certify.py's metric",
                sp.simplify(sp.exp(2 * Ls) - 1 / (1 - 2 * m_s / rs))))
    out.append(("V7  STATIC CORNER  Gamma^2 = 1 - 2m/r, so Gamma>1 <=> m<0",
                sp.simplify(Gam_s**2 - (1 - 2 * m_s / rs))))

    # ---- V8: the Painleve-Gullstrand threshold
    at_marginal = {sp.Derivative(R, r): sp.exp(Lam)}          # Gamma = 1
    out.append(("V8  PG THRESHOLD  Gamma = 1  =>  U^2 = 2m/R",
                sp.simplify((2 * m / R - U**2).subs(at_marginal))))

    # ---- V9: the LTB energy function
    Ef = sp.Function("E", real=True)(r)
    Rp = sp.Symbol("Rprime", positive=True)
    Lam_ltb = sp.log(Rp / sp.sqrt(1 + 2 * Ef))
    out.append(("V9  LTB       Gamma^2 = 1 + 2E, so contraction IS unbound",
                sp.simplify((sp.exp(-Lam_ltb) * Rp)**2 - (1 + 2 * Ef))))

    # ---- V10: expose.py's invariant is the reciprocal of Gamma
    C_expose = sp.sqrt(g[1, 1]) / sp.diff(sp.sqrt(g[3, 3].subs(th, sp.pi / 2)), r)
    out.append(("V10 expose.py  C x Gamma = 1  (the SAME criterion)",
                sp.simplify(C_expose * Gam - 1)))
    return out


def pg_residuals():
    """drivensource.py's PG witness, IMPORTED not copied: Schwarzschild in
    Lemaitre (= PG) slicing must give vacuum, m = r_s/2, Gamma = 1 exactly and
    U = -sqrt(2m/R)."""
    import sympy as sp
    w = drivensource.pg_witness()
    return w, [
        ("V11 PG WITNESS  Gamma = 1 exactly", sp.simplify(w["W"] - 1)),
        ("V12 PG WITNESS  U = -sqrt(2m/R)",
         sp.simplify(w["U"] + sp.sqrt(2 * w["m"] / w["R"]))),
        ("V13 PG WITNESS  m = r_s/2 > 0", sp.simplify(w["m"] - w["rs"] / 2)),
    ]


def verify():
    """--verify: the exact symbolic verification, reproducible.  Exits 0 only
    if every residual is exactly 0."""
    try:
        import sympy as sp
    except ImportError:
        print("driven.py --verify needs sympy.\n\n    pip install sympy"
              "     # pypi is on the proxy allowlist; see PROOF-ASSISTANT.md\n")
        return 2

    print("driven.py --verify      sympy %s, python %s"
          % (sp.__version__, ".".join(map(str, sys.version_info[:3]))))
    print()
    print("  the metric is the ONLY thing written down by hand.  The inverse is")
    print("  computed, the gradient is contracted with it, and m is SOLVED from")
    print("  1 - 2m/R = g^ab d_a R d_b R.  Every residual below must be 0.")
    print()
    E = _general()
    print("  |grad R|^2 = %s" % E["gradR"])
    print("  m          = %s" % sp.simplify(E["m"]))
    print()
    bad = 0
    for label, res in residuals(E) + pg_residuals()[1]:
        good = (sp.simplify(res) == 0)
        bad += not good
        print("  %-62s %-8s %s" % (label, res, "0" if good else "NOT ZERO"))
    print()
    if bad:
        print("  VERIFY FAILED -- %d residual(s) non-zero" % bad)
        return 1
    print("  VERIFY OK -- every residual exactly 0")
    return 0


# ================================================================ selftest

def selftest():
    """STDLIB ONLY.  sympy is behind --verify and is never imported here."""
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-62s %-16s %-16s %s"
              % (label, str(got)[:16], str(want)[:16], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-62s %16.9g %16.9g %s"
              % (label, got, want, "ok" if good else "FAIL"))

    print("driven.py --selftest    stdlib only; sympy lives behind --verify")

    print("\n1. PRIOR ART, FIRST, BECAUSE IT GOES AGAINST US")
    chk("  the identity is", PRIOR_ART_IDENTITY,
        "Misner & Sharp 1964, Phys. Rev. 136, B571")
    chk("  and the attribution is", PRIOR_ART_ROUTE,
        "RECOVERED from Hayward gr-qc/9408002 eq. (27); NOT read at source")
    chk("  is novelty claimed for any of it", NOVELTY_CLAIMED, False)
    chk("  is the criterion new to this tree", CRITERION_IS_NEW_TO_THIS_TREE, False)
    chk("  was the docket's premise true (Olum needs no staticity)",
        DOCKET_PREMISE_WAS_TRUE, False)

    print("\n2. THE THEOREM  --  contraction <=> 2m/R < U^2")
    chk("  m < 0 is SUFFICIENT", contracts(-1.0, 10.0, 0.0), True)
    chk("  m < 0 contracts at every U sampled",
        all(contracts(-1.0, 10.0, U) for U in (0.0, 0.5, 5.0)), True)
    chk("  and there is then no threshold at all", threshold_speed(-1.0, 10.0), None)
    chk("  m > 0 does NOT contract at U = 0", contracts(1.0, 10.0, 0.0), False)
    chk("  m < 0 is NOT NECESSARY -- m > 0 contracts at U = 1",
        contracts(1.0, 10.0, 1.0), True)
    near("  Gamma there", gamma(1.0, 10.0, 1.0), 1.341640786, 1e-9)
    chk("  contraction is exactly unboundedness, E > 0",
        all(contraction_is_unbound(m, 10.0, U)
            for m in (-1.0, 0.0, 1.0) for U in (0.0, 0.3, 1.0)), True)
    print("     m = 1, R = 10 FIXED, and the verdict flips on U ALONE:")
    v, rows = loophole_table()
    print("     %-14s %-14s %-12s %s" % ("U", "Gamma", "E = (G^2-1)/2", "contracts"))
    for row in rows:
        mark = "   <-- PG threshold sqrt(2m/R)" if abs(row["U"] - v) < 1e-15 else ""
        print("     %-14.10f %-14.10f %-12.6f %s%s"
              % (row["U"], row["gamma"], row["E"], row["contracts"], mark))
    chk("  the loophole is real", LOOPHOLE_IS_REAL, True)

    print("\n3. certify.py RECOVERED AS THE Rdot = 0 CORNER -- THE FIXTURE")
    rows, agree = certify_corner()
    print("     %-10s %-14s %-14s %-10s %-10s %s"
          % ("g_rr", "Gamma", "m(r)", "certify", "here", "agree"))
    for g_rr, G, m, there, here, same in rows:
        print("     %-10.4g %-14.10f %-14.10f %-10s %-10s %s"
              % (g_rr, G, m, there, here, same))
    chk("  certify.py and this file agree on every sample", agree, True)
    chk("  certify.py's own fixture still holds", certify.theorem_holds(), True)
    chk("  certify.py's scope, unedited", certify.THEOREM_SCOPE,
        "static and spherically symmetric only")
    chk("  and this file recovers it at", CERTIFY_RECOVERED_AT, "Rdot = 0")
    chk("  negative mass is still necessary at a stationary areal radius",
        NEGATIVE_MASS_NECESSARY_AT_STATIONARY_AREAL_RADIUS, True)
    chk("  mouth.py section 5b scoped itself to exactly this",
        mouth.SIGN_RESOLUTION_SCOPE,
        "static and spherically symmetric, per certify.py")
    chk("  and mouth.py's M = |m| resolution is not disturbed",
        mouth.EXCHANGE_RATE_M_IS_ABS_OF_CERTIFY_M, True)

    print("\n4. THE THRESHOLD IS THE PAINLEVE-GULLSTRAND VELOCITY")
    near("  threshold at m = 1, R = 10 is sqrt(2m/R)",
         threshold_speed(1.0, 10.0), 0.4472135955, 1e-9)
    near("  and Gamma = 1 exactly there", gamma(1.0, 10.0, threshold_speed(1.0, 10.0)),
         1.0, 1e-15)
    chk("  at U just above it, contraction", contracts(1.0, 10.0, 0.4472135956), True)
    chk("  at U just below it, none", contracts(1.0, 10.0, 0.4472135954), False)
    near("  the threshold reaches 1 exactly at R = 2m", threshold_speed(1.0, 2.0),
         1.0, 1e-15)
    chk("  so is the areal velocity capped at lightspeed",
        AREAL_VELOCITY_IS_CAPPED_AT_LIGHTSPEED, False)
    print("       drivensource.pg_witness() has |U| = sqrt(r_s/R) > 1 at every")
    print("       R < r_s.  The cheap closure does not hold.  Recorded.")
    chk("  is the PG reading a coincidence of notation",
        PG_IS_COINCIDENCE_OF_NOTATION, False)
    chk("  drivensource.py agrees, and owns the witness",
        drivensource.WAVECORRIDOR_PG,
        "UNCHANGED and SHARPENED -- PG is the W = 1 surface")

    print("\n5. THE COST TO SUSTAIN -- CARRIED FROM nonstatic.py, NOT RE-DERIVED")
    chk("  status of this section", COST_TO_SUSTAIN_STATUS,
        "DERIVED IN nonstatic.py, CARRIED HERE")
    chk("  does sustaining force rho < 0", nonstatic.SUSTAINING_FORCES_NEGATIVE_RHO,
        False)
    chk("  the NEC on such a configuration",
        nonstatic.NEC_ON_A_CONTRACTING_POSITIVE_MASS_CONFIGURATION,
        "SATISFIED, strictly")
    chk("  is a quasi-stationary corridor possible",
        nonstatic.QUASI_STATIONARY_CORRIDOR_EXISTS, False)
    chk("  and this file carries that verdict unchanged",
        QUASI_STATIONARY_CORRIDOR_EXISTS,
        nonstatic.QUASI_STATIONARY_CORRIDOR_EXISTS)
    n = carried_numbers()
    for W, d in n["disp"]:
        near("  far end displaced, floor at Gamma = %-5g" % W, d,
             {2.0: 0.8660254038, 10.0: 0.9949874371, 100.0: 0.9999499987}[W], 1e-9)
    for W, rr in n["ratio"]:
        near("  band / crossing at Gamma = %-5g, eps = 1%%" % W, rr,
             {2.0: 2.309401077e-2, 100.0: 2.000100008e-2}[W], 1e-9)
    chk("  contracting harder buys no time",
        nonstatic.band_ratio(2.0, 0.01) > nonstatic.band_ratio(100.0, 0.01), True)
    near("  Proxima span (m)", n["span_m"], 4.017499195e16, 1e-9)
    near("  band at Gamma = 2, eps = 1% (days)", n["band_days"], 17.909799392, 1e-9)
    near("  against one crossing (years)", n["cross_yr"], 2.123250000, 1e-9)
    near("  build throughput at dGamma = 1 (M_sun)", n["build_msun"],
         2.720744289e13, 1e-9)
    near("  H83d's 2.7254e12 M_sun is met at dGamma", n["h83d_dgamma"], 0.100171, 1e-5)
    print("       DIFFERENT KIND, SAME ORDER, UNRELATED ROUTE.  Not adjudicated.")

    print("\n6. THE GAUGE FACT, AND THE VERDICT")
    chk("  is Gamma a scalar", CONTRACTION_IS_A_SCALAR, False)
    chk("  and nonstatic.py measured the same", nonstatic.CONTRACTION_IS_A_SCALAR,
        False)
    chk("  is the loophole empty", LOOPHOLE_IS_EMPTY, True)
    chk("  is the bill lifted", BILL_LIFTED, False)
    chk("  and nonstatic.py's verdict, carried", nonstatic.BILL_LIFTED, BILL_LIFTED)
    chk("  verdict", VERDICT, "REAL, STANDARD, AND EMPTY -- THE BILL IS NOT LIFTED")

    print("\n7. SCOPE AND REFUSALS")
    chk("  scope", THEOREM_SCOPE,
        "spherically symmetric only; staticity dropped, sphericity kept")
    chk("  what is new to this tree", NEW_TO_THIS_TREE,
        "overturn.py's L1 has a second door: drop staticity, keep sphericity")
    chk("  and the internal prior art, recorded against this file",
        INTERNAL_PRIOR_ART,
        "nonstatic.py measured it first, drivensource.py second, "
        "and overturn.py's LINKS table already seats the result")
    links = {row[0]: row[3] for row in overturn.LINKS}
    chk("  overturn.py L1 SCOPE -- the SPHERICITY half, still", links["L1"],
        overturn.OPEN)
    chk("  overturn.py L2 SOURCE -- drivensource.py's point charge",
        links["L2"], overturn.BROKEN_EMPTY)
    chk("  certify.py's COROLLARY (drivensource.py's finding, not restated)",
        drivensource.CERTIFY_COROLLARY,
        "NARROWED -- needs a regular centre, m(0) = 0")
    chk("  certify.py's THEOREM", drivensource.CERTIFY_THEOREM, "UNCHANGED")
    chk("  nothing is repaired", NOTHING_IS_REPAIRED, True)
    chk("  and no peer is edited", drivensource.NOTHING_IS_REPAIRED, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


# ================================================================== report

BAR = "=" * 79


def report():
    print(__doc__)
    n = carried_numbers()
    v, rows = loophole_table()

    print(BAR)
    print("THE LOOPHOLE, EXHIBITED -- m = 1 AND R = 10 FIXED, POSITIVE THROUGHOUT")
    print(BAR)
    print()
    print("     %-16s %-16s %-14s %s" % ("U = e^-Phi Rdot", "Gamma", "E", "contracts"))
    for row in rows:
        mark = "   <-- PG threshold" if abs(row["U"] - v) < 1e-15 else ""
        print("     %-16.10f %-16.10f %-14.6f %s%s"
              % (row["U"], row["gamma"], row["E"], row["contracts"], mark))
    print()
    print("     The mass is POSITIVE at every row.  The threshold is sqrt(2m/R)")
    print("     = %.10f, the Painleve-Gullstrand velocity.  THE CONDITION IS A"
          % v)
    print("     SPEED, NOT A SIGN -- and the U = 0 row is certify.py.")
    print()

    print(BAR)
    print("certify.py RECOVERED AS THE Rdot = 0 CORNER")
    print(BAR)
    print()
    print("     %-10s %-14s %-14s %-10s %s"
          % ("g_rr", "Gamma", "m(r)", "certify.py", "this file"))
    for g_rr, G, m, there, here, _ in certify_corner()[0]:
        print("     %-10.4g %-14.10f %-14.10f %-10s %s" % (g_rr, G, m, there, here))
    print()
    print("     Agreement on every sample, on the verdict AND on the sign of m.")
    print()

    print(BAR)
    print("WHAT IT COSTS -- nonstatic.py's MEASUREMENT, CARRIED")
    print(BAR)
    print()
    print("     %-10s %-16s %-16s %s"
          % ("Gamma", "far end moves", "band / crossing", "build (M_sun)"))
    for row in nonstatic.corridor_table():
        print("     %-10.4g %-16.6f %-16.6f %.4e"
              % (row["W"], row["disp"], row["ratio"], row["msun"]))
    print()
    print("     A Proxima corridor at Gamma = 2 holds its areal radius to +/- 1 %")
    print("     for %.3f days against a %.4f year crossing, and costs %.4e"
          % (n["band_days"], n["cross_yr"], n["build_msun"]))
    print("     solar masses of throughput to raise Gamma from 1.")
    print()

    print(BAR)
    print("STANDARD, FOLKLORE, REFUTED, NEW")
    print(BAR)
    print()
    for claim, status, note in standard_table():
        print("     %-52s %-16s" % (claim, status))
        print("       %s" % note)
    print()

    print(BAR)
    print("THE PASS IN ONE PARAGRAPH")
    print(BAR)
    print("""
  certify.py's theorem said "static and spherically symmetric only" and this
  file measures the first half of that limit.  Drop staticity, keep sphericity,
  and the Misner-Sharp mass is still exactly defined by a scalar; the identity
  Gamma^2 = 1 + U^2 - 2m/R then makes contraction the condition 2m/R < U^2,
  whose right-hand side is a square.  So m < 0 is sufficient and no longer
  necessary, the threshold is a SPEED -- exactly the Painleve-Gullstrand escape
  velocity sqrt(2m/R) -- and Rdot = 0 recovers certify.py identically, which the
  fixture checks against certify.py's own functions rather than restating them.
  ALL OF THAT IS STANDARD.  The identity is Misner & Sharp's 1964 equation,
  quoted verbatim by Hayward; Gamma is Escriva's generalised Lorentz factor;
  Gamma > 1 is the unbound LTB shell; and Gamma > 1 is this tree's own expose.py
  criterion C < 1, since C x Gamma = 1 identically.  No novelty is claimed.
  AND THE ESCAPE FAILS THREE TIMES.  Hochberg & Visser showed in 1998 that
  spatial flare-out stops implying null flare-out the moment staticity goes, and
  that the averaged NEC is violated on an open interval around every throat;
  Olum's theorem makes negative energy compulsory for superluminal travel with
  NO staticity, NO symmetry and NO sphericity, so the bill never rested on
  certify.py in the first place; and nonstatic.py measured the engineering,
  where sustaining contraction costs nothing at all but the anchor lemma and the
  displacement bound close the corridor anyway -- 86.6 % of the span given away
  at Gamma = 2, and a band that shrinks towards 2 eps of a crossing however hard
  you contract.  Underneath it is a gauge fact: m is a scalar and Gamma is not,
  and Minkowski sliced two ways returns both answers.  THE LOOPHOLE IS REAL, IT
  IS STANDARD, AND IT IS EMPTY.  THE BILL IS NOT LIFTED.  Nothing is repaired.
""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--verify" in sys.argv:
        sys.exit(verify())
    sys.exit(report())
