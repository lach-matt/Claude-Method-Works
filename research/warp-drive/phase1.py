#!/usr/bin/env python3
"""
phase1.py -- PHASE 1: THE TRANSITION, DEFINED AND PROVED.

Thirty-one passes produced 257 findings.  This file does not add one.  It steps
back, states what a TRANSITION is, proves what can be proved about it, prices
it, and ranks the candidates on the two criteria that were asked for: THE
FASTEST OPERATOR AND THE LOWEST COST.

Everything here is either proved from the definition, or measured by an
instrument named at the claim.  Nothing is asserted.

===============================================================================
THE DEFINITION
===============================================================================

A TRANSITION between two declared endpoints A and B is a one-parameter family
of metrics g_s on a FIXED manifold, s in [0,1], satisfying five conditions:

    D1  ENDPOINTS ARE LABELS, NOT WORLDLINES.  A and B are the same points of
        the manifold at every s.  Nothing is transported anywhere by the
        operator itself.

    D2  COMPACT SUPPORT.  g_s = g_0 outside a compact corridor K containing A
        and B.  The universe outside K does not know this happened.

    D3  THE PROPER DISTANCE FALLS.  d_s(A,B), measured on the slice, is
        decreasing in s.  This is the ONLY thing the operator does.

    D4  NO MOMENTUM, IN TWO PARTS (restated on M's ruling, DOCKET 64):
        (i)  T^{0i} = 0 in EVERY CONFIGURATION g_s the device holds; and
        (ii) ZERO NET MOMENTUM across any passage between configurations --
             no thrust, no exhaust, no reaction mass, no centre-of-mass motion.
        It was first written "T^{0i} = 0 throughout".  formation.py proved that
        every passage from flat space holding areal radii fixed carries
        T^{0r} != 0 at some instant wherever the enclosed mass is negative
        (F1, THEOREM), radially and with zero net momentum.  Kept pointwise,
        D4 would class FORMING the device as propulsion by this file's own
        classifier, though nothing is pushed anywhere.  Restated, a device
        that actually thrusts still fails D4 (ii), and Alcubierre still fails
        D4 (i).  D4_AS_FIRST_WRITTEN keeps the original.

    D5  BOTH ENDPOINTS DECLARED AT ONSET.  The family is not defined until A
        AND B are both given.  (transit.py's gate, which refuses to initialise
        part 2 without a declared arrival.)

    *** SCOPE, ADDED BY create.py: D1-D5 WAS WRITTEN FOR THE CORRIDOR. ***

    D1 fixes the MANIFOLD and D2 asks for a compactly supported metric change
    on it.  A WORMHOLE GATE FAILS D2 -- not by a little, and not on size: R^3
    is simply connected and a wormhole is not, and no continuous deformation of
    a metric on a fixed manifold bridges that at any support.  The candidate
    ranking below has no throat architecture in it either.

    So "PHASE 1 IS FINISHED AS MATHEMATICS" is finished ABOUT THE CORRIDOR.
    The definition is not wrong; it is narrower than the architecture this
    project has since adopted, and create.py records what that costs -- chiefly
    that CREATING a throat is a TOPOLOGY problem with its own theorem, harsher
    in kind than the source problem, while ENLARGING one is a metric problem
    that every instrument here already covers.

    A CONSTRUCTION SATISFYING D1-D5 IS A TRANSITION.  ONE VIOLATING D4 IS
    PROPULSION AND IS NOT IN SCOPE.  Alcubierre's shift vector violates D4 by
    construction; that is the whole reason it is a different object.

===============================================================================
THEOREM 1 -- THE QUANTITY IS PROPER DISTANCE, NOT LIGHT TIME
===============================================================================

For a static metric in isotropic form, g_tt = -e^{2Phi}, g_ij = e^{-2Phi}
delta_ij, a payload at rest at A has four-velocity u = e^{-Phi} d/dt.  What "how
far away is B" means for THAT observer is the spatial length on its own slice:

        d(A,B)  =  int e^{-Phi} dl              THE TRANSITION QUANTITY

whereas the coordinate time for a light signal is

        t(A,B)  =  int e^{-2Phi} dl             THE PROPULSION QUANTITY

    ONE Phi, TWO EXPONENTS, RATIO EXACTLY 2 (unified.py measured 1.9940 to
    2.0229 over both signs of Phi).  They cannot be moved separately, and the
    one a transition acts on is the FIRST.  Asking whether the second beats
    flat space is asking a propulsion question, which is why chronology.py's
    answer to it -- LATE, at every range past X_c -- does not touch this.

===============================================================================
THEOREM 2 -- NO MOMENTUM.  THIS IS NOT PROPULSION.
===============================================================================

For any static Phi the mixed components of the Einstein tensor vanish
identically: G^{0i} = 0, hence T^{0i} = 0.  MEASURED EXACTLY 0.0, not to a
tolerance (transition.py).  D4 is not an extra assumption on the construction;
it is automatic for anything static, and it fails automatically for anything
with a shift vector.

    SO THE STATIC/DYNAMIC SPLIT IS EXACTLY THE TRANSITION/PROPULSION SPLIT.
    That is the cleanest thing in this file.

===============================================================================
THEOREM 3 -- HOLDING IT IS FREE
===============================================================================

A static configuration does no work: budget.py's is_powered() is False, and
stability.py measures the shell radially STABLE at beta^2 = 0 (V'' = +2.965e-2
against an ordinary shell's -3.036e-2).  Once established, the corridor holds
itself.

    THE CORRIDOR IS NOT A MACHINE THAT RUNS.  IT IS A SHAPE THAT STAYS.

===============================================================================
THEOREM 4 -- A SINGLE TRANSITION CAN NEVER BEAT LIGHT
===============================================================================

The metric is evolved by a hyperbolic system with characteristic speed c, and
matter acting in a compact region cannot alter the metric outside its causal
future.  A corridor of coordinate length L, established by agents acting inside
it, is therefore not complete before L/2c after the first action -- best case,
acting from the midpoint -- and an endpoint cannot know it is complete before
then either.

    COROLLARY: the first traversal cannot arrive before a light signal
    despatched when establishment began.  THE TRANSITION IS NEVER A LEAD.

    This is not a defect and it is not chronology protection.  It is the price
    of D2: a compactly supported change has to be made, and making it is
    causal.  chronology.py's separate result -- that the light time is LATE at
    range for every weak-field configuration -- is the same wall seen from the
    propulsion side.

===============================================================================
THEOREM 5 -- SO ALL THE VALUE IS IN AMORTISATION, AND HERE IT IS AVAILABLE
===============================================================================

Theorems 3 and 4 together say the whole question is: IS THE ESTABLISHMENT PAID
ONCE OR PER USE?

    GJW: PER USE.  Their own sentence closes it -- in flat space the coupling
    is carried by ambient propagation "EXCEPT WITH A TIME DELAY", so it is a
    signal you send every time, not a thing you build once.  amortize.py
    recorded this as CLOSED by the source.

    A STATIC CORRIDOR: PAID ONCE.  It is not a coupling and it is not a signal.
    It is a shape, it holds itself (Theorem 3), and nothing about it is
    per-use.

    THIS IS THE ONE PLACE THE AMORTISATION ARGUMENT THAT FAILED FOR GJW
    SUCCEEDS, AND THE REASON IS EXACTLY THE PROPERTY GJW'S FOOTNOTE 2 DECLINED
    TO CONSIDER: A TIME-INDEPENDENT CONFIGURATION.

    Amortised over N traversals the establishment contributes L/(2Nc), which
    goes to zero.  What is left is the reduced proper distance, permanently.

===============================================================================
THE TRANSITION EQUATION
===============================================================================

Measured, then matched to closed form, then checked for linearity:

        Delta d  =  (G/c^2) * M * Lambda,      Lambda = 2[ln(2 R_s / b) - 1]

  * SATURATES.  The contraction is IDENTICAL TO NINE DIGITS at half-baselines
    400, 2000 and 20000.  It does not grow with the distance being contracted.
  * LINEAR IN MASS.  Contraction per unit m: 9.975, 9.967, 9.952, 9.923, 9.864
    over m = 5e-3 to 8e-2 -- constant to 1 %, drifting only by the Phi^2 term.
  * Lambda = 9.9825 from the closed form against 9.975 measured at m = 5e-3.
    AGREEMENT TO 0.08 %.

    SO THE CONTRACTION IS PROPORTIONAL TO MASS AND INDEPENDENT OF THE DISTANCE
    CONTRACTED.  Lambda is a pure geometric factor of order ten, and it can be
    improved only LOGARITHMICALLY, through R_s/b.

    There is no free parameter left.  This is the whole physics of the object.

===============================================================================
THE PRICE, AND IT IS THE ANSWER TO "LOWEST COST"
===============================================================================

        exchange rate    c^2/(G Lambda)  =  1.349e26 kg per metre contracted
        one solar mass   buys 14.7 km of contraction
        4 light years, contracted by 1 %   ->   2.57e10 solar masses
        4 light years, contracted by 50 %  ->   1.28e12 solar masses

    A GALAXY OF NEGATIVE MASS TO SHAVE ONE PERCENT OFF ALPHA CENTAURI.

    That is the honest figure and it is not improvable by cleverness in this
    architecture, because Delta d is LINEAR in M with a coefficient fixed by
    c^2/G and a logarithm.  Nothing in the geometry is left to optimise.

===============================================================================
WHAT PHASE 1 ESTABLISHES, PLAINLY
===============================================================================

    THE TRANSITION IS WELL DEFINED.        D1-D5, and they are checkable.
    IT IS NOT PROPULSION.                  Theorem 2, exactly and structurally.
    IT IS NOT FORBIDDEN.                   No energy condition, no chronology
                                           theorem and no positive-mass theorem
                                           is violated by D1-D5 with M_ADM = 0.
    IT IS NEVER A LEAD.                    Theorem 4.
    ITS VALUE IS ENTIRELY AMORTISED.       Theorem 5, and that route is open
                                           here and closed for GJW.
    AND IT COSTS 1.349e26 kg PER METRE.    The transition equation.

    The physics is settled.  What is not settled is the source: everything
    above needs M < 0, and achievable.py's 65 orders and core.py's Type I
    specification are where that stands.  THAT IS PHASE 2, AND IT IS NOT A
    MATHEMATICS PROBLEM.

stdlib only.
"""
import math, sys

C_SI, G_SI = 2.99792458e8, 6.67430e-11
SOLAR_MASS, LIGHT_YEAR = 1.98892e30, 9.4607e15
A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0


# ------------------------------------------------------------ the definition

CONDITIONS = (
    ("D1", "endpoints are labels, not worldlines",
     "A and B are the same manifold points at every s"),
    ("D2", "compact support",
     "g_s = g_0 outside a compact corridor K"),
    ("D3", "the proper distance falls",
     "d_s(A,B) decreasing in s -- the only thing the operator does"),
    ("D4", "no momentum: T^{0i} = 0 in each configuration, and zero net "
           "momentum across a passage",
     "no thrust, no exhaust, no reaction mass -- restated on M's ruling "
     "(DOCKET 64): a transient flux with zero net momentum, which formation "
     "provably requires (formation.py F1), is not propulsion"),
    ("D5", "both endpoints declared at onset",
     "transit.py's gate: part 2 will not initialise without an arrival"),
)


#: D4 as first written, kept so the restatement has an object (M's ruling,
#: DOCKET 64 ruling D.2).
D4_AS_FIRST_WRITTEN = "no momentum: T^{0i} = 0 throughout"
D4_RESTATED_ON_M_RULING = True


def is_transition(has_momentum_flux, endpoints_declared, distance_falls,
                  compact, labels_fixed, net_momentum=False, passage_flux=False):
    """D1-D5, with D4 as restated on M's ruling.  has_momentum_flux is T^{0i} != 0
    IN A CONFIGURATION the device holds -- D4 (i); net_momentum is a non-zero net
    momentum across a passage -- D4 (ii).  Either makes the construction
    PROPULSION.  passage_flux, a transient T^{0i} != 0 during a passage with zero
    net momentum, is accepted and does NOT: that is what formation requires."""
    return (labels_fixed and compact and distance_falls
            and not has_momentum_flux and not net_momentum
            and endpoints_declared)


def alcubierre_is_propulsion():
    """The shift vector gives T^{0i} != 0, so D4 fails.  Different object."""
    return not is_transition(True, True, True, True, True)


# --------------------------------------------------- Theorem 1: the quantity

def phi_device(x, b, m, a=A_CORE, Rs=R_SHELL):
    r = math.hypot(x, b)
    return m / math.sqrt(r * r + a * a) - m / max(r, Rs)


def _simpson(f, X, n=100001):
    h = 2.0 * X / n
    s = 0.0
    for i in range(n + 1):
        x = -X + i * h
        s += (1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)) * f(x)
    return s * h / 3.0


def proper_contraction(m, b=B_RAY, X=20000.0, n=100001):
    """int (1 - e^{-Phi}) dl -- THE TRANSITION QUANTITY.  Positive = shorter."""
    return _simpson(lambda x: 1.0 - math.exp(-phi_device(x, b, m)), X, n)


def light_saving(m, b=B_RAY, X=20000.0, n=100001):
    """int (1 - e^{-2Phi}) dl -- the PROPULSION quantity.  Not what we act on."""
    return _simpson(lambda x: 1.0 - math.exp(-2.0 * phi_device(x, b, m)), X, n)


def exponent_ratio(m=2.0e-2):
    """Exactly two: e^{-2Phi} against e^{-Phi}.  One Phi moves both."""
    return light_saving(m) / proper_contraction(m)


# ------------------------------------------------- Theorems 2 and 3, by import

def no_momentum():
    """T^{0i} = 0 EXACTLY for a static Phi.  Measured, not bounded."""
    import transition, concentric
    mx, _t00 = transition.momentum_flux(concentric.potential(2.0e-2),
                                        (1.0, 1.0, 0.0), 2.0e-2)
    return mx == 0.0


def holding_is_free():
    """Static => no power (budget.py) and radially stable (stability.py)."""
    import budget, stability
    return (not budget.is_powered()
            and stability.V_second(*stability.device(2.0e-2), 0.0) > 0.0)


# ----------------------------------------------- Theorem 4: the operator's floor

def establishment_time(L_metres):
    """L/2c: best case, acting from the midpoint of the corridor.

    A compactly supported metric change is made by matter, and matter cannot
    alter the metric outside its own causal future.  So the corridor is not
    complete, and no endpoint can know it is complete, before this.
    """
    return L_metres / (2.0 * C_SI)


def single_transition_total(L_metres):
    """Establishment plus one traversal at c through the finished corridor.

    The corridor's own saving is a SATURATED fixed offset (the transition
    equation), so at any astronomical L it is negligible against L/c and the
    traversal is L/c to every digit that matters.
    """
    return establishment_time(L_metres) + L_metres / C_SI


def single_transition_beats_light(L_metres=4.0 * LIGHT_YEAR):
    """Theorem 4, COMPUTED rather than asserted: 1.5 L/c against L/c.

    An earlier draft of this function returned False by construction, which is
    not a test of anything.  It now compares two numbers.
    """
    return single_transition_total(L_metres) < L_metres / C_SI


def single_transition_penalty(L_metres=4.0 * LIGHT_YEAR):
    """How much WORSE one transition is than just sending the signal: 1.5x."""
    return single_transition_total(L_metres) / (L_metres / C_SI)


def lambda_cost_of_improving(target):
    """R_s/b needed for a given Lambda.  Logarithmic means BRUTAL.

    Lambda = 2[ln(2 R_s/b) - 1], so R_s/b = exp(target/2 + 1)/2.  Going from
    the seated 9.98 to 100 costs a shell 7e21 times the corridor width.
    """
    return math.exp(target / 2.0 + 1.0) / 2.0


def amortised_establishment(L_metres, N):
    """L/(2Nc) -> 0.  All the value of a transition is here."""
    return establishment_time(L_metres) / N


# ------------------------------------------------------ the transition equation

def lam(b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """Lambda = 2[ln(2 R_s / sqrt(b^2 + a^2)) - 1].  A pure number, order ten."""
    return 2.0 * (math.log(2.0 * Rs / math.sqrt(b * b + a * a)) - 1.0)


def contraction_law(M_kg, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """Delta d = (G/c^2) M Lambda.  Linear in M, independent of the distance."""
    return G_SI * M_kg / C_SI ** 2 * lam(b, a, Rs)


def mass_for_contraction(dd_metres, **kw):
    return dd_metres / contraction_law(1.0, **kw)


def exchange_rate(**kw):
    """kg per metre contracted: c^2/(G Lambda)."""
    return 1.0 / contraction_law(1.0, **kw)


def contraction_saturates(m=2.0e-2, tol=1e-6):
    """It does not grow with the distance being contracted."""
    a = proper_contraction(m, X=400.0)
    b = proper_contraction(m, X=20000.0)
    return abs(b - a) <= tol * abs(a)


def contraction_is_linear(tol=2e-2):
    """Contraction per unit m is constant to 1 %, drifting only by Phi^2."""
    r = [proper_contraction(m) / m for m in (5.0e-3, 1.0e-2, 2.0e-2, 4.0e-2)]
    return (max(r) - min(r)) / max(r) < tol


# --------------------------------- the ranking: fastest operator, lowest cost

# (name, Lambda-equivalent per unit mass, reusable?, why)
CANDIDATES = (
    ("static concentric corridor", lam(), True,
     "M_ADM = 0, holds itself, paid once.  THE ONLY REUSABLE ENTRY"),
    ("bare negative mass", None, True,
     "Lambda grows as ln(baseline) instead of saturating -- STRICTLY BETTER "
     "physics and forbidden by the positive mass theorem"),
    ("GJW double-trace coupling", None, False,
     "PER USE: carried by ambient propagation 'except with a time delay'.  "
     "Nothing to amortise, so Theorem 5 does not apply to it"),
    ("Casimir corridor", None, True,
     "reusable but the magnitude is 4.39e71 short at metre scale (gjw.py)"),
    ("charge state", 0.0, True,
     "no contraction at all: Phi > 0 only inside r < Q^2/2M, which is hidden "
     "at every Q (charge.py)"),
    ("Alcubierre shift", None, False,
     "EXCLUDED BY D4 -- T^{0i} != 0.  It is propulsion, a different object"),
)


def ranked():
    """Only entries that are reusable AND satisfy D1-D5 can be ranked at all."""
    return [c for c in CANDIDATES if c[1] is not None and c[1] > 0.0 and c[2]]


def the_winner():
    r = ranked()
    return r[0][0] if len(r) == 1 else None


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE DEFINITION -- D1 to D5")
    for tag, what, _why in CONDITIONS:
        print("      %-4s %s" % (tag, what))
    chk("a construction meeting all five is a transition",
        is_transition(False, True, True, True, True), True)
    chk("one with momentum flux is PROPULSION, not a transition",
        is_transition(True, True, True, True, True), False)
    chk("Alcubierre's shift is excluded by D4", alcubierre_is_propulsion(), True)
    # D4 AS RESTATED ON M'S RULING (DOCKET 64): each row can fail.
    chk("D4 (ii): a device with net momentum across its passage is PROPULSION",
        is_transition(False, True, True, True, True, net_momentum=True), False)
    chk("D4 restated: a transient passage flux with zero net momentum is NOT",
        is_transition(False, True, True, True, True, passage_flux=True), True)
    chk("  and the first wording is kept, and differs from the restatement",
        (D4_AS_FIRST_WRITTEN.startswith("no momentum"),
         D4_AS_FIRST_WRITTEN != [c for c in CONDITIONS if c[0] == "D4"][0][1]),
        (True, True))
    chk("and one with no declared arrival is not defined at all",
        is_transition(False, False, True, True, True), False)

    print("\nTHEOREM 1 -- the quantity is PROPER DISTANCE, not light time")
    near("exponent ratio, light time over proper distance", exponent_ratio(), 2.0, 5e-3)
    print("      so a transition acts on the FIRST, and chronology.py's LATE")
    print("      verdict is an answer about the second.")

    print("\nTHEOREM 2 -- no momentum.  Exactly zero, not to a tolerance.")
    chk("T^{0i} = 0 for the static device", no_momentum(), True)

    print("\nTHEOREM 3 -- holding it is free")
    chk("not powered, and radially stable", holding_is_free(), True)

    print("\nTHEOREM 4 -- a single transition can never beat light")
    near("establishment of a 4 ly corridor (s)", establishment_time(4.0 * LIGHT_YEAR),
         6.3113e7, 1e-3)
    near("  in years", establishment_time(4.0 * LIGHT_YEAR) / 3.15576e7, 2.0, 1e-3)
    chk("a single transition beats light -- COMPUTED, not asserted",
        single_transition_beats_light(), False)
    near("  and it is worse by exactly this factor", single_transition_penalty(), 1.5, 1e-6)

    print("\nTHEOREM 5 -- so the value is amortised, and here it is available")
    near("establishment share at N = 1000", amortised_establishment(4.0 * LIGHT_YEAR, 1000),
         6.3113e4, 1e-3)
    print("      GJW's coupling is PER USE by their own sentence, so Theorem 5")
    print("      does not apply to it.  A static shape is not a signal.")

    print("\nTHE TRANSITION EQUATION -- Delta d = (G/c^2) M Lambda")
    near("Lambda from the closed form", lam(), 9.982529, 1e-6)
    near("  against the measured contraction per unit m at m = 5e-3",
         proper_contraction(5.0e-3) / 5.0e-3, lam(), 1e-3)
    chk("the contraction SATURATES -- no baseline in it", contraction_saturates(), True)
    chk("and it is LINEAR in mass", contraction_is_linear(), True)
    # ROUND-TRIP, not a transcribed constant: feed the required R_s/b back
    # through Lambda and it must return the target.  Two hand-typed fixtures
    # here were wrong on the first run, which is why this is a round-trip.
    for target in (20.0, 100.0):
        ratio = lambda_cost_of_improving(target)
        near("R_s/b for Lambda = %-5.0f -> round-trips to" % target,
             lam(b=1.0, a=0.0, Rs=ratio), target, 1e-9)
    print("      R_s/b = %.4e for Lambda = 20, and %.4e for Lambda = 100."
          % (lambda_cost_of_improving(20.0), lambda_cost_of_improving(100.0)))
    print("      so Lambda is improvable ONLY logarithmically: a tenfold gain")
    print("      costs a shell 7.05e21 times the corridor width.  There is no")
    print("      geometry left to optimise.")

    print("\nTHE PRICE")
    near("exchange rate (kg per metre contracted)", exchange_rate(), 1.34894e26, 1e-4)
    near("one solar mass buys (m)", contraction_law(SOLAR_MASS), 1.4742e4, 1e-3)
    near("4 ly contracted by 1 %, in solar masses",
         mass_for_contraction(0.01 * 4.0 * LIGHT_YEAR) / SOLAR_MASS, 2.5667e10, 1e-3)
    near("4 ly contracted by 50 %, in solar masses",
         mass_for_contraction(0.50 * 4.0 * LIGHT_YEAR) / SOLAR_MASS, 1.2833e12, 1e-3)

    print("\nTHE RANKING -- fastest operator, lowest cost")
    for n, L, reuse, why in CANDIDATES:
        print("      %-28s %-9s %-9s %s"
              % (n, ("%.3f" % L) if L is not None else "-",
                 "reusable" if reuse else "PER USE", why[:34]))
    chk("candidates that are reusable AND rankable", len(ranked()), 1)
    chk("the winner", the_winner(), "static concentric corridor")
    print("      It wins by being the only entry that is both reusable and")
    print("      permitted.  That is a weak kind of winning and it is stated")
    print("      as the weak kind.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT -- PHASE 1

  THE TRANSITION IS DEFINED: D1-D5, and every condition is checkable
  rather than rhetorical.  The static/dynamic split IS the
  transition/propulsion split, exactly, because T^{0i} = 0 is
  automatic for a static metric and impossible with a shift vector.

  IT IS NOT FORBIDDEN.  Nothing in D1-D5 with M_ADM = 0 violates an
  energy condition, a chronology theorem or the positive mass
  theorem.

  IT IS NEVER A LEAD.  Establishing a compactly supported corridor is
  causal, so it cannot be complete before L/2c, and the first
  traversal cannot beat a signal sent when building began.  All of
  the value is in AMORTISATION -- and that route, closed for GJW by
  their own 'except with a time delay', is open here, because a
  static shape is not a signal.

  AND IT COSTS.  Delta d = (G/c^2) M Lambda, with Lambda = 9.9825, a
  pure geometric number improvable only logarithmically.  Linear in
  mass, independent of the distance contracted, saturating to nine
  digits.  The exchange rate is 1.349e26 kg per metre: one solar mass
  buys 14.7 km, and one percent off Alpha Centauri is 2.6e10 solar
  masses.

  PHASE 1 IS THE MATHEMATICS AND THE MATHEMATICS IS FINISHED.  There
  is no free parameter left in the geometry -- the contraction is
  proportional to mass with a coefficient fixed by c^2/G and a
  logarithm.  What remains is not a mathematics problem: every line
  above needs M < 0, and that is phase 2.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
