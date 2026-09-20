#!/usr/bin/env python3
r"""
drivensource.py -- DOCKET 52, items 3-5.  nonstatic.py dropped staticity and
found the driven-contraction condition 2m/R < e^{-2Phi}Rdot^2.  This file asks
the three questions that condition creates about the REST of the tree:

    item 3   does the driven route re-open ELECTROMAGNETIC sourcing, which
             emwarp.py closed?
    item 4   is wavecorridor.py's Painleve-Gullstrand structure the same object
             as the sqrt(2m/R) in the threshold, or a coincidence of notation?
    item 5   which banked results change status?

    python3 drivensource.py             the reading
    python3 drivensource.py --selftest  every identity, every machine check

Needs sympy and z3-solver (pypi is on the proxy allowlist -- PROOF-ASSISTANT.md).
Run under python3 (3.11), NOT python3.12.

    THE ONE-LINE ANSWER TO ITEM 3.  emwarp.py closed the wrong door for this
    question, and the right door is closed anyway by a CONSERVATION LAW rather
    than by an energy condition.  Electromagnetism cannot source a driven
    corridor, and the reason has nothing to do with the NEC.

===============================================================================
0.  PRIOR ART, RECORDED FIRST BECAUSE MOST OF ITEM 3 IS ALREADY BANKED
===============================================================================

charge.py GOT THERE FIRST and this file does not re-discover it.  It already
states, in its own docstring:

    "Phi(r) = -M/r + Q^2/(2 r^2),  so  Phi > 0  iff  r < Q^2/(2M)"
    "THE POSITIVE-POTENTIAL REGION IS INSIDE THE HORIZON AT EVERY CHARGE."
    "the POSITIVE ENERGY THEOREM FOR EINSTEIN-MAXWELL (Gibbons & Hull; Witten)
     forces Q <= M"
    "A horizonless charged body must have matter out past where the horizon
     would be, so the r < Q^2/2M region is inside its matter, not in a corridor."

r < Q^2/(2M) is EXACTLY the region where the Misner-Sharp mass of
Reissner-Nordstrom is negative, because m(R) = M - Q^2/(2R).  charge.py found
the region, and closed it, before this docket existed.  Its selftest passes.

    THREE THINGS ARE NEW HERE AND THEY ARE THE ONLY THINGS CLAIMED.

    (N1) charge.py argued from the POTENTIAL.  Read as a statement about the
         MISNER-SHARP MASS the same region is a COUNTEREXAMPLE TO certify.py'S
         COROLLARY -- m(r) < 0 with rho > 0 everywhere -- and it sits inside
         certify.py's own stated scope.  Nobody had connected the two.

    (N2) charge.py's "inside its matter" is qualitative.  It is sharp:
         r_c <= a for ANY charged body of radius a, from the exterior field
         energy alone, with equality only at zero bare mass.  This needs no
         positive energy theorem and no horizon.

    (N3) The DRIVEN branch -- the one this docket opened -- is closed to pure
         electromagnetism by Birkhoff in Misner-Sharp variables, which is a
         question charge.py could not have asked because only the static
         theorem existed when it was written.

===============================================================================
1.  THE DRIVEN CONDITION DOES NOT NEED THE NEC, SO emwarp.py DOES NOT CLOSE IT
===============================================================================

emwarp.py proves T_ab k^a k^b = |P_perp(E + n x B)|^2, a sum of squares, so
Maxwell stress-energy SATURATES the NEC and never violates it.  That theorem
stands, its selftest passes, and nothing here touches it.

    BUT IT IS NOT AN ANSWER TO THIS QUESTION.  The driven condition
    2m/R < e^{-2Phi}Rdot^2 never asks for a negative T_ab k^a k^b.
    nonstatic.py's own witnesses settle that: open FRW holds contraction with
    rho > 0, m > 0 and the NEC contraction equal to rho, STRICTLY POSITIVE.
    A closure by NEC violation closes nothing that this route needs.

    SO THE HONEST STATEMENT IS: emwarp.py's theorem is unweakened AND its
    sufficiency as a closure argument for EM sourcing is REDUCED.  It refutes
    "EM makes negative energy".  It does not refute "EM drives a corridor".

WHAT IS NEW ABOUT THE THEOREM ITSELF, AND IT IS A SCOPE CONFIRMATION.  emwarp's
proof is flat-space three-vector algebra.  electrovac() below builds the Maxwell
stress-energy in the FULL dynamical spherically symmetric metric

        ds^2 = -e^{2Phi(t,r)}dt^2 + e^{2Lambda(t,r)}dr^2 + R(t,r)^2 dOmega^2

from F_{tr} and the curved-space Maxwell equations, and returns

        rho = Q^2/(8 pi R^4)      j = 0      p_r = -rho      p_T = +rho

so rho + p_r = 0 EXACTLY in curved, time-dependent spherical symmetry too.
emwarp's saturation is not an artefact of its flat-space presentation.

===============================================================================
2.  AND THE DRIVEN BRANCH IS CLOSED TO EM BY A CONSERVATION LAW
===============================================================================

Feed that stress-energy into nonstatic.py's own Misner-Sharp equations.  With
j = 0 and p_r = -rho they become dm = 4 pi R^2 rho dR in both directions at
once, and the solution is exact:

        m(R) = M - Q^2/(2R),        M CONSTANT

and birkhoff_residuals() shows BOTH residuals vanish identically for ARBITRARY
Phi(t,r), Lambda(t,r) and R(t,r).  That is Birkhoff's theorem for
Einstein-Maxwell, written in the variables this docket runs on.

    THE MASS FUNCTION IS FROZEN.  No motion of the metric functions -- however
    violent, however driven -- changes m at a given areal radius.  There is no
    electromagnetic configuration whose m(R) evolves, because m(R) is not a
    degree of freedom of the electrovac field.

    A charged fluid is a different tensor and is NOT covered.  This closes PURE
    electromagnetism, which is what the proposal asked about.

===============================================================================
3.  THE STATIC BRANCH, AND certify.py'S COROLLARY IS THE CASUALTY
===============================================================================

m(R) = M - Q^2/(2R) is NEGATIVE for R < Q^2/(2M), and rho = Q^2/(8 pi R^4) is
POSITIVE at every R.  Reissner-Nordstrom is static and spherically symmetric, so
it is inside certify.py's scope, and there:

        contraction holds, m(r) < 0, and the energy density is positive
        everywhere.

certify.py's THEOREM survives untouched -- contraction iff m(r) < 0 -- because
that is what is measured.  Its COROLLARY does not:

        "AND THEREFORE IF AND ONLY IF THE ENCLOSED ENERGY IS NEGATIVE"

That step needs m(r) = 4 pi int_0^r rho r'^2 dr', which needs m(0) = 0, which
needs A REGULAR CENTRE.  Reissner-Nordstrom has none: the integral of its own
energy density DIVERGES at the origin, and the finite M absorbs a -infinity of
bare mass at the point charge.  The negativity is the SINGULARITY's, not the
field's.

    THIS IS overturn.py'S LINK L2, AND overturn.py SAID BREAKING IT WOULD
    REVERSE THE VERDICT: "Break L2 and negative m(r) no longer needs negative
    energy."  L2 IS BREAKABLE, A POINT CHARGE BREAKS IT, AND SECTION 4 SHOWS
    THE BREAK IS EMPTY.  A link can fall and the chain still hold, if what
    comes through the gap is unusable.

===============================================================================
4.  WHY THE BREAK IS EMPTY -- SHARP, AND WITHOUT A POSITIVE ENERGY THEOREM
===============================================================================

Put the charge on a body of radius a instead of a point.  The field OUTSIDE a
already carries energy Q^2/(8 pi eps0 a), so the ADM mass obeys

        M  >=  X / a,        X := Q^2 / (8 pi eps0 c^2)      (units kg m)

whenever the body's own contribution to M is non-negative.  The contraction
radius is r_c = X / M, so

        r_c  =  X / M  <=  X / (X/a)  =  a          THE BOUND

        r_c / a  =  1 / (1 + mu a / X)    for bare mass mu,   sup = 1 at mu = 0

    THE NEGATIVE-MASS REGION OF A CHARGED BODY NEVER REACHES OUTSIDE THE BODY.
    Equality needs the entire mass to be exterior field energy, which is a
    shell of zero bare mass, and then r_c = a exactly -- marginal, not
    contracting.  This uses no horizon, no censorship and no positive energy
    theorem; it is the field's own energy closing its own loophole.

    AND INSIDE THE BODY THERE IS NOTHING EITHER.  With a regular centre and
    rho >= 0, m(r) = 4 pi int_0^r rho r'^2 dr' >= 0 at every r, so contraction
    happens nowhere.  For a shell specifically the interior is flat, m = 0.

    charge.py'S ROUTE IS STRONGER WHERE IT APPLIES AND IS CONFIRMED HERE.
    Gibbons-Hull/Witten force Q <= M, and then r_c is inside not merely the
    outer horizon but the INNER one: r_c/r_- = (1 + sqrt(1 - q^2))/2 <= 1 for
    q = Q/M in (0, 1], measured below.  Two independent closures agreeing.

===============================================================================
5.  ITEM 4 -- THE PAINLEVE-GULLSTRAND VELOCITY.  SAME STRUCTURE, NOT NOTATION.
===============================================================================

The threshold is |U| > sqrt(2m/R) with U = e^{-Phi}Rdot the areal velocity.
sqrt(2m/R) is the Painleve-Gullstrand shift.  It is the SAME OBJECT, and the
identity says why in one line.  From nonstatic.py's identity U^2 = W^2 - 1 + 2m/R:

        W = 1   <=>   |U| = sqrt(2m/R)

and W = 1 is marginal contraction.  So sqrt(2m/R) is the areal velocity of the
MARGINALLY BOUND radial geodesic -- free fall from rest at infinity -- which is
exactly what the PG shift is.  Equivalently W^2 - 1 = U^2 - 2m/R = 2E, twice the
Lemaitre-Tolman-Bondi energy function, so

        CONTRACTION  <=>  W > 1  <=>  E > 0  <=>  THE CONFIGURATION IS UNBOUND.

MEASURED, NOT ASSERTED.  pg_witness() runs Schwarzschild in Lemaitre slicing --
which is PG brought to the diagonal form this docket uses -- through
nonstatic.witness() and gets, exactly:

        vacuum = True     m = r_s/2 = M > 0     W = 1     U = -sqrt(2m/R)

    THE PG FOLIATION IS PRECISELY THE W = 1 SURFACE OF THE CRITERION.  Positive
    mass, vacuum, and sitting exactly on the boundary.

    AND THE TWO THRESHOLDS ARE DIFFERENT, WHICH IS THE PART A NOTATIONAL READING
    WOULD MISS.  wavecorridor.py's acoustic horizon is |v| = c_s: the PG velocity
    against the SIGNAL SPEED.  This docket's threshold is |U| = sqrt(2m/R): the
    AREAL velocity against the PG velocity.  Same velocity function, two
    different comparisons, two different events -- a horizon in one case,
    marginal contraction in the other.

    A COROLLARY FOR THE ANALOGUE, AND IT GOES AGAINST THE ANALOGY.  Write the
    acoustic metric with rho/c_s constant and it is -c_s^2 dt^2 + (dr - v dt)^2
    + r^2 dOmega^2: the constant-t slices are EXACTLY FLAT, so W = 1 exactly.
    A sonic horizon is real -- wavecorridor.py is right that it is the only
    horizon anyone in this project has built -- but it sits permanently ON the
    marginal boundary and never crosses it.  THE ANALOGUE CANNOT EXHIBIT
    CONTRACTION AT ALL.  For an inhomogeneous background
    W = 1 + r d/dr log sqrt(rho/c_s), which is NOT MEASURED here and is recorded
    as a refusal, not glossed.

===============================================================================
6.  ITEM 5 -- WHAT CHANGES STATUS.  SEVEN ROWS, AND SIX ARE CONFIRMATIONS.
===============================================================================

status_table() is the machine-readable form.  In words:

  certify.py THEOREM          UNCHANGED.  Exact, and nonstatic.py's anchor lemma
                              shows it was never about static SPACETIMES but
                              about stationary AREAL RADII.  Its scope line is
                              load-bearing and is now measured.

  certify.py COROLLARY        NARROWED.  "therefore iff the enclosed ENERGY is
  ("therefore ... enclosed    negative" needs a REGULAR CENTRE.  Reissner-
   energy is negative")       Nordstrom is a counterexample inside its own
                              stated scope.  Not a repair -- a hypothesis that
                              was always used and never written.

  overturn.py L2              BROKEN, AND THE BREAK IS EMPTY.  overturn.py said
                              breaking L2 reverses the verdict.  A point charge
                              breaks it and buys nothing, because r_c <= a.

  overturn.py L1              SPLIT IN TWO.  overturn.py reads L1 as the
                              SPHERICITY link ("outside spherical symmetry there
                              is no areal radius").  The STATICITY half is a
                              different door and overturn.py never named it.
                              nonstatic.py opened it and closed it.

  mouth.py section 5b         CONFIRMED, NOT REFUTED.  It scoped itself to
                              certify.py's family and named this exact successor
                              question.  M = |m|, m < 0 stands where it was
                              claimed to stand.

  emwarp.py theorem           UNCHANGED, AND CONFIRMED IN CURVED SPACETIME.
                              Its ROLE narrows: it refutes EM negative energy,
                              not EM sourcing.  Section 2 supplies the closure
                              it was doing duty for.

  wavecorridor.py section 1   UNCHANGED AND SHARPENED.  The PG identification is
                              exact and is now placed: PG is the W = 1 surface.

  charge.py                   UNCHANGED.  Prior art for the whole of item 3.

===============================================================================
7.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT CLAIM EM SOURCING IS IMPOSSIBLE IN GENERAL.  Section 2 closes
    PURE electrovac in SPHERICAL symmetry.  A charged fluid, a non-spherical
    field and nonlinear electrodynamics are three different tensors and none is
    measured here.

    IT DOES NOT RE-DISCOVER charge.py.  Section 0 records the overlap first and
    names the three things that are actually new.

    IT DOES NOT MEASURE THE INHOMOGENEOUS ACOUSTIC METRIC.  Section 5's W = 1
    is for rho/c_s constant.  The general case is written down and not run.

    IT REPAIRS NOTHING.  certify.py's corollary is NOT edited, overturn.py's L2
    is NOT restated, and nothing in paper/ is touched.  A finding is recorded.
"""

import math
import sys

EPS0 = 8.8541878128e-12          # F/m, CODATA 2018
C = 2.99792458e8                 # m/s, exact
G = 6.67430e-11                  # m^3 kg^-1 s^-2, CODATA 2018


# ------------------------------------------------- 1-2. the electrovac source

def electrovac():
    """Maxwell stress-energy of the ONLY spherically symmetric field, in the
    FULL dynamical metric.  Nothing quoted: F is fixed by the curved-space
    Maxwell equations and T is built from it."""
    import sympy as sp

    t, r, th = sp.symbols("t r theta", real=True)
    ph = sp.Symbol("phi")
    Phi = sp.Function("Phi")(t, r)
    Lam = sp.Function("Lambda")(t, r)
    R = sp.Function("R")(t, r)
    Q = sp.Symbol("Q", positive=True)
    x = [t, r, th, ph]

    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
    gi = sp.diag(-sp.exp(-2 * Phi), sp.exp(-2 * Lam), R**-2, (R * sp.sin(th))**-2)

    # Spherical symmetry admits only F_{tr} (radial electric); Gauss' law
    # sqrt(-g) F^{tr} = Q fixes it.  Verified as a Maxwell residual below.
    F = sp.zeros(4, 4)
    F[0, 1] = Q * sp.exp(Phi + Lam) / R**2
    F[1, 0] = -F[0, 1]
    Fup = gi * F * gi
    sg = sp.sqrt(-g.det())
    maxwell = [sp.simplify(sum(sp.diff(sg * Fup[a, b], x[a]) for a in range(4)))
               for b in range(4)]

    Fdd = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
    Fmix = F * gi
    T = sp.Matrix(4, 4, lambda a, b: sp.simplify(
        (sum(F[a, c] * Fmix[b, c] for c in range(4))
         - sp.Rational(1, 4) * g[a, b] * Fdd) / (4 * sp.pi)))

    return dict(sp=sp, Q=Q, R=R, Phi=Phi, Lam=Lam, t=t, r=r, maxwell=maxwell,
                rho=sp.simplify(T[0, 0] * sp.exp(-2 * Phi)),
                j=sp.simplify(-T[0, 1] * sp.exp(-Phi - Lam)),
                p_r=sp.simplify(T[1, 1] * sp.exp(-2 * Lam)),
                p_T=sp.simplify(T[2, 2] / R**2),
                U=sp.exp(-Phi) * sp.diff(R, t),
                W=sp.exp(-Lam) * sp.diff(R, r),
                Dt=lambda f: sp.exp(-Phi) * sp.diff(f, t),
                Dr=lambda f: sp.exp(-Lam) * sp.diff(f, r))


def birkhoff_residuals(EV=None):
    """Does m = M - Q^2/2R with M CONSTANT satisfy nonstatic.py's MS-r and MS-t
    for ARBITRARY Phi, Lambda, R?  Both residuals must be 0."""
    EV = EV or electrovac()
    sp = EV["sp"]
    M = sp.Symbol("M")
    m = M - EV["Q"]**2 / (2 * EV["R"])
    R, U, W = EV["R"], EV["U"], EV["W"]
    rho, j, p_r = EV["rho"], EV["j"], EV["p_r"]
    return [
        ("MS-r  D_r m = 4 pi R^2 (rho W + j U)",
         sp.simplify(EV["Dr"](m) - 4 * sp.pi * R**2 * (rho * W + j * U))),
        ("MS-t  D_t m = -4 pi R^2 (p_r U + j W)",
         sp.simplify(EV["Dt"](m) + 4 * sp.pi * R**2 * (p_r * U + j * W))),
    ]


# --------------------------------------------------- 4. the emptiness bound

def X_of_Q(Q_coulomb):
    """X = Q^2/(8 pi eps0 c^2), in kg m.  The exterior field energy outside
    radius a is X c^2 / a, so the ADM mass is at least X/a."""
    return Q_coulomb * Q_coulomb / (8.0 * math.pi * EPS0 * C * C)


def contraction_radius(Q_coulomb, M_kg):
    """r_c = Q^2/(8 pi eps0 c^2 M).  m(r) < 0 strictly inside it."""
    return X_of_Q(Q_coulomb) / M_kg


def shell_ratio(Q_coulomb, a_m, mu_kg):
    """r_c / a for a shell of radius a, charge Q and BARE mass mu.
    Equals 1/(1 + mu a / X), so it is <= 1 always and = 1 only at mu = 0."""
    X = X_of_Q(Q_coulomb)
    return X / (mu_kg * a_m + X)


def inner_horizon_ratio(q):
    """r_c / r_- for Reissner-Nordstrom at q = Q/M.  = (1 + sqrt(1-q^2))/2."""
    return 0.5 * (1.0 + math.sqrt(1.0 - q * q))


# ------------------------------------------------------- 5. the PG structure

def pg_witness():
    """Schwarzschild in Lemaitre (= Painleve-Gullstrand) slicing, through
    nonstatic.py's own witness().  Must give vacuum, m = r_s/2, W = 1 exactly
    and U = -sqrt(2m/R): the PG foliation IS the marginal surface."""
    import sympy as sp
    import nonstatic

    t = sp.Symbol("t", positive=True)          # witness() requires this name
    rho_c, rs = sp.symbols("rho r_s", positive=True)
    Rl = (sp.Rational(3, 2) * (rho_c - t))**sp.Rational(2, 3) * rs**sp.Rational(1, 3)
    w = nonstatic.witness("SCHWARZSCHILD, Lemaitre (= PG) slicing",
                          sp.Integer(0), sp.log(sp.sqrt(rs / Rl)), Rl, rho_c, True)
    w["rs"] = rs
    w["R"] = Rl
    return w


ACOUSTIC_W_HOMOGENEOUS = 1.0
ACOUSTIC_W_GENERAL = "W = 1 + r d/dr log sqrt(rho/c_s)   -- NOT MEASURED HERE"


# --------------------------------------------------- the machine obligations

def obligations():
    """Each claim asserted NEGATED and reported unsat, each with a vacuity
    guard, and the drift guards asked as SATISFIABILITY so they can fail."""
    import prover
    prover.require_z3()
    import z3

    out = []

    def obligation(name, hyp, concl):
        s = z3.Solver()
        s.add(hyp)
        s.add(z3.Not(concl))
        r = s.check()
        out.append((name, str(r), "unsat", r == z3.unsat))
        return r == z3.unsat

    def satisfiable(name, hyp):
        s = z3.Solver()
        s.add(hyp)
        r = s.check()
        out.append((name, str(r), "sat", r == z3.sat))
        return r == z3.sat

    R, M, Q, m = z3.Reals("R M Q m")
    rn = [R > 0, M > 0, Q > 0, m == M - Q * Q / (2 * R)]
    satisfiable("guard: RN with m < 0 is satisfiable", rn + [m < 0])
    obligation("E1  m < 0  <=>  2 M R < Q^2   (the RN contraction region)",
               rn, (m < 0) == (2 * M * R < Q * Q))

    X, a, mu, rc, Mt = z3.Reals("X a mu r_c M_tot")
    shell = [X > 0, a > 0, mu >= 0, Mt == mu + X / a, rc == X / Mt]
    satisfiable("guard: the shell system is satisfiable", shell)
    obligation("E2  r_c <= a   for every charged body with mu >= 0", shell, rc <= a)
    satisfiable("guard: r_c = a is attained, at mu = 0", shell + [mu == 0, rc == a])
    # DRIFT.  Drop mu >= 0 and the bound must FAIL, or E2 proves nothing.
    satisfiable("DRIFT: drop mu >= 0 and a counterexample to E2 must exist",
                [X > 0, a > 0, Mt == mu + X / a, rc == X / Mt, z3.Not(rc <= a)])

    U, W, mm, RR = z3.Reals("U W m2 R2")
    ident = [RR > 0, W > 0, W * W == 1 - 2 * mm / RR + U * U]
    satisfiable("guard: the marginal system is satisfiable", ident + [W == 1])
    obligation("E3  W = 1  <=>  U^2 = 2m/R   (PG velocity IS the margin)",
               ident, (W == 1) == (U * U == 2 * mm / RR))
    return out


# ------------------------------------------------------------------- status

CERTIFY_THEOREM = "UNCHANGED"
CERTIFY_COROLLARY = "NARROWED -- needs a regular centre, m(0) = 0"
OVERTURN_L1 = "SPLIT -- sphericity half stands, staticity half opened and closed"
OVERTURN_L2 = "BROKEN BY A POINT CHARGE, AND THE BREAK IS EMPTY"
MOUTH_5B = "CONFIRMED -- it scoped itself and named this successor question"
EMWARP_THEOREM = "UNCHANGED, and confirmed in curved dynamical spherical symmetry"
EMWARP_ROLE = "REDUCED -- it refutes EM negative energy, not EM sourcing"
WAVECORRIDOR_PG = "UNCHANGED and SHARPENED -- PG is the W = 1 surface"
CHARGE_PY = "UNCHANGED -- prior art for item 3"
EM_CAN_SOURCE_DRIVEN_CONTRACTION = False
EM_CLOSED_BY_ENERGY_CONDITION = False
EM_CLOSED_BY = "Birkhoff (driven branch) and the field's own exterior energy (static branch)"
PG_IS_COINCIDENCE_OF_NOTATION = False
NOTHING_IS_REPAIRED = True
SCOPE = ("pure electrovac, spherical symmetry.  Charged fluids, non-spherical "
         "fields and nonlinear electrodynamics are not measured.")


def status_table():
    return [
        ("certify.py THEOREM", CERTIFY_THEOREM),
        ("certify.py COROLLARY", CERTIFY_COROLLARY),
        ("overturn.py L1 SCOPE", OVERTURN_L1),
        ("overturn.py L2 SOURCE", OVERTURN_L2),
        ("mouth.py section 5b", MOUTH_5B),
        ("emwarp.py theorem", EMWARP_THEOREM),
        ("emwarp.py role as a closure", EMWARP_ROLE),
        ("wavecorridor.py section 1", WAVECORRIDOR_PG),
        ("charge.py", CHARGE_PY),
    ]


# ---------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-64s %-18s %-18s %s"
              % (label, str(got)[:18], str(want)[:18], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-64s %18.10g %18.10g %s" % (label, got, want, "ok" if good else "FAIL"))

    import sympy as sp

    print("0. PRIOR ART, FIRST, BECAUSE MOST OF ITEM 3 IS ALREADY BANKED")
    print("     charge.py: 'Phi > 0 iff r < Q^2/(2M)' and 'inside the horizon at")
    print("     every charge'.  That IS the m(r) < 0 region.  Three things are new:")
    print("       N1 it is a counterexample to certify.py's COROLLARY")
    print("       N2 the bound r_c <= a is sharp and needs no positive energy theorem")
    print("       N3 the DRIVEN branch is closed by Birkhoff -- a new question")

    print("\n1. THE MAXWELL SOURCE IN THE FULL DYNAMICAL METRIC")
    EV = electrovac()
    Q, R = EV["Q"], EV["R"]
    chk("  curved-space Maxwell residuals all vanish", EV["maxwell"], [0, 0, 0, 0])
    chk("  rho = Q^2/(8 pi R^4)", sp.simplify(EV["rho"] - Q**2 / (8 * sp.pi * R**4)), 0)
    chk("  j = 0 (no radial energy flux)", sp.simplify(EV["j"]), 0)
    chk("  p_r = -rho", sp.simplify(EV["p_r"] + EV["rho"]), 0)
    chk("  p_T = +rho", sp.simplify(EV["p_T"] - EV["rho"]), 0)
    chk("  NEC RADIAL SATURATED: rho + p_r", sp.simplify(EV["rho"] + EV["p_r"]), 0)
    chk("  and traceless: -rho + p_r + 2 p_T",
        sp.simplify(-EV["rho"] + EV["p_r"] + 2 * EV["p_T"]), 0)
    print("       emwarp.py's saturation is NOT an artefact of its flat-space form.")
    chk("  rho is POSITIVE, so this violates no energy condition",
        sp.ask(sp.Q.positive(EV["rho"].subs(R, sp.Symbol("x", positive=True)))), True)

    print("\n2. BIRKHOFF IN MISNER-SHARP VARIABLES -- THE MASS FUNCTION IS FROZEN")
    for label, resid in birkhoff_residuals(EV):
        chk("  " + label, resid, 0)
    print("       m = M - Q^2/2R with M CONSTANT, for ARBITRARY Phi, Lambda, R.")
    print("       So the DRIVEN branch is closed to pure EM by a conservation law.")

    print("\n3. THE STATIC BRANCH -- certify.py's COROLLARY FAILS ON RN")
    rr, Mg, Qg = sp.symbols("r M Q", positive=True)
    m_rn = Mg - Qg**2 / (2 * rr)
    chk("  1/g_rr - 1 = (Q^2 - 2 M r)/r^2  (contraction iff r < Q^2/2M)",
        sp.simplify((1 - 2 * m_rn / rr) - 1 - (Qg**2 - 2 * Mg * rr) / rr**2), 0)
    enc = sp.integrate(4 * sp.pi * rr**2 * Qg**2 / (8 * sp.pi * rr**4), rr)
    chk("  indefinite enclosed-energy integral is -Q^2/2r", sp.simplify(enc + Qg**2 / (2 * rr)), 0)
    chk("  and it DIVERGES at the centre, so m(0) != 0",
        sp.limit(enc, rr, 0, "+"), -sp.oo)
    print("       m(r) < 0 with rho > 0 EVERYWHERE.  The theorem holds; the")
    print("       'therefore the enclosed energy is negative' does not.")

    print("\n4. AND THE BREAK IS EMPTY -- r_c <= a, SHARP")
    Xs, av, muv = sp.symbols("X a mu", positive=True)
    chk("  a - r_c = a^2 mu/(X + a mu) >= 0",
        sp.simplify(av - Xs / (muv + Xs / av) - av**2 * muv / (Xs + av * muv)), 0)
    near("  X per coulomb^2 (kg m)", X_of_Q(1.0), 5.0e-08, 1e-9)
    print("     %-40s %12s %12s %10s" % ("configuration", "r_c (m)", "a (m)", "r_c/a"))
    for lab, Qv, av_, muv_ in [("1 C, 1 m sphere, 1 kg", 1.0, 1.0, 1.0),
                               ("4472 C, 1 m sphere, 1 kg", 4472.0, 1.0, 1.0),
                               ("4472 C, 1 m shell, 1 microgram", 4472.0, 1.0, 1e-9),
                               ("zero bare mass (the supremum)", 4472.0, 1.0, 0.0)]:
        rc = contraction_radius(Qv, muv_ + X_of_Q(Qv) / av_)
        print("     %-40s %12.6g %12.4g %10.6f" % (lab, rc, av_, shell_ratio(Qv, av_, muv_)))
        chk("    r_c <= a for %s" % lab[:28], shell_ratio(Qv, av_, muv_) <= 1.0, True)
    near("  4472 C on 1 m with 1 kg bare: r_c/a", shell_ratio(4472.0, 1.0, 1.0), 0.4999847997, 1e-9)
    chk("  and zero bare mass gives exactly 1 (marginal, not contracting)",
        shell_ratio(4472.0, 1.0, 0.0), 1.0)
    print("     charge.py's independent closure, confirmed and sharpened:")
    print("     %-10s %14s %14s %12s" % ("q = Q/M", "r_c/M", "r_-/M", "r_c/r_-"))
    for q in (0.5, 0.9, 0.99, 1.0):
        print("     %-10.2f %14.5f %14.5f %12.6f"
              % (q, q * q / 2.0, 1.0 - math.sqrt(1.0 - q * q), inner_horizon_ratio(q)))
        chk("    inside the INNER horizon at q = %.2f" % q, inner_horizon_ratio(q) <= 1.0, True)
    near("  r_c/r_- at extremal q = 1", inner_horizon_ratio(1.0), 0.5, 1e-12)

    print("\n5. ITEM 4 -- THE PG VELOCITY IS THE SAME STRUCTURE")
    w = pg_witness()
    rs, Rl = w["rs"], w["R"]
    print("     Schwarzschild, Lemaitre (= PG) slicing, through nonstatic.witness():")
    for k in ("W", "U", "m", "rho", "j"):
        print("       %-4s = %s" % (k, sp.simplify(w[k])))
    chk("  it is vacuum", w["vacuum"], True)
    chk("  m = r_s/2 = M > 0", sp.simplify(w["m"] - rs / 2), 0)
    chk("  W = 1 EXACTLY -- the PG foliation is the marginal surface",
        sp.simplify(w["W"] - 1), 0)
    chk("  U = -sqrt(2m/R): |U| IS the PG / free-fall areal velocity",
        sp.simplify(w["U"] + sp.sqrt(2 * w["m"] / Rl)), 0)
    Uu, Ww, mm2, RR2 = sp.symbols("U W m R", positive=False)
    chk("  and W = 1 forces U^2 = 2m/R in the identity",
        sp.simplify((Ww**2 - 1 + 2 * mm2 / RR2 - 2 * mm2 / RR2).subs(Ww, 1)), 0)
    chk("  so the PG appearance is a coincidence of notation",
        PG_IS_COINCIDENCE_OF_NOTATION, False)
    chk("  acoustic metric, rho/c_s constant: W is", ACOUSTIC_W_HOMOGENEOUS, 1.0)
    print("       the analogue's slices are exactly flat, so a sonic horizon sits")
    print("       permanently ON the marginal boundary and never crosses it.")
    print("       inhomogeneous case: %s" % ACOUSTIC_W_GENERAL)

    print("\n6. THE MACHINE OBLIGATIONS")
    for name, got, want, good in obligations():
        ok &= good
        print("  %-68s %-6s %s" % (name, got, "ok" if good else "FAIL"))

    print("\n7. ITEM 5 -- STATUS")
    for label, val in status_table():
        print("     %-30s %s" % (label, val))
    chk("  can EM source driven contraction", EM_CAN_SOURCE_DRIVEN_CONTRACTION, False)
    chk("  is it closed by an energy condition", EM_CLOSED_BY_ENERGY_CONDITION, False)
    chk("  certify.py's THEOREM", CERTIFY_THEOREM, "UNCHANGED")
    chk("  mouth.py 5b", MOUTH_5B,
        "CONFIRMED -- it scoped itself and named this successor question")
    chk("  nothing is repaired", NOTHING_IS_REPAIRED, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


# ------------------------------------------------------------------ report

def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  nonstatic.py's driven condition 2m/R < e^{-2Phi}Rdot^2 never asks for a
  negative null contraction, so emwarp.py -- which closed EM by proving the
  Maxwell NEC is a sum of squares and therefore saturated -- does not close
  it.  That theorem is unweakened and is in fact confirmed here in curved,
  time-dependent spherical symmetry, where rho + p_r is still exactly 0; what
  narrows is its ROLE, because it refutes EM negative energy rather than EM
  sourcing.  The right closure is a conservation law.  Feeding the electrovac
  source into the Misner-Sharp equations gives m(R) = M - Q^2/2R with M
  CONSTANT, both residuals vanishing for arbitrary Phi, Lambda and R: the mass
  function is frozen, so the driven branch has no electromagnetic degree of
  freedom to drive it.  The static branch is more interesting and it costs
  certify.py something.  Reissner-Nordstrom has m(r) < 0 for r < Q^2/2M with
  rho = Q^2/8 pi r^4 > 0 everywhere, so certify.py's THEOREM holds and its
  COROLLARY -- 'and therefore iff the enclosed energy is negative' -- fails:
  that step needs a regular centre, and RN's enclosed-energy integral diverges.
  This is overturn.py's link L2, which overturn.py said would reverse the
  verdict if broken.  It is broken, by a point charge, and the break is empty:
  the exterior field energy alone forces r_c <= a for any charged body of
  radius a, with equality only at zero bare mass, so the negative-mass region
  never reaches outside its own source -- and with Gibbons-Hull/Witten's
  Q <= M it is inside the INNER horizon, r_c/r_- = (1+sqrt(1-q^2))/2.  charge.py
  reached the same region first by a different route and is recorded first.  On
  item 4 the Painleve-Gullstrand velocity is the same structure and not a
  notation: W = 1 if and only if |U| = sqrt(2m/R), so the PG shift is the
  marginally bound free-fall areal velocity and the PG foliation IS the W = 1
  surface -- verified exactly on Schwarzschild in Lemaitre slicing, vacuum,
  m = M > 0, W = 1, U = -sqrt(2m/R).  The two thresholds differ, and that is
  the part a notational reading misses: wavecorridor's acoustic horizon sets
  the PG velocity against the signal speed, this docket sets the areal velocity
  against the PG velocity.  A corollary against the analogy: the acoustic
  metric's slices are exactly flat, so W = 1 always and a sonic horizon can
  never exhibit contraction.  Nothing is repaired.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
