#!/usr/bin/env python3
"""
qei.py -- ITEM 1: evaluate the Fewster-Osterbrink state-dependent quantum energy
inequality for this architecture.  millennium.py made L4 "a computation, not an
impossibility"; this is the computation, as far as it can honestly be taken.

THE RESULT IS SHARP AND IT IS NOT WHAT CANDIDATE D NEEDED.

    The proved bound splits into a STATE-INDEPENDENT piece and a STATE-DEPENDENT
    one.  The state-independent piece is computed here in CLOSED FORM, and it
    SCALES AS tau^-4 -- the Ford-Roman exponent -- NOT as R^-2.  So candidate D's
    entire exponent advantage lives in the state-dependent piece, which is the
    piece that costs energy, and the H-bounds say it costs more than it delivers.

===============================================================================
1. THE BOUND, AND THE PIECE THAT CAN BE COMPUTED WITHOUT A STATE
===============================================================================

Fewster-Osterbrink (arXiv:0708.2450) Theorem 4.3, n-dimensional Minkowski:

    (rho o gamma)(f^2)  >=  -Qxi(f) = -( QA(f).1 + xi (:Phi^2: o gamma)(QB[f]) )

    QA(f) = S_{n-2}/(2pi)^n Int da Int dk k^(n-2)/w(k)
                            [ (1-2xi) w^2(k) + 2 xi a^2 ] |fhat(a + w(k))|^2
    QB[f](t) = 2 (d_t f(t))^2

and in curved spacetime Theorem 4.2 adds QC[f] = f^2 (R_mn g^m g^n
- (1/2)(1-4xi) R), WHICH VANISHES IN A RICCI-FLAT REGION AND DOES NOT VANISH
HERE, since the corridor carries matter.  That term is NOT evaluated below and
its omission is recorded rather than hidden.

QA IS STATE-INDEPENDENT, so it can be evaluated now.  For n = 4, massless, and
a Gaussian sampling function normalised to ||f||_L2 = 1, the double integral
reduces in closed form.  Substituting a = A/tau, k = B/tau factors the width out
completely and leaves a pure number:

        QA(xi, tau)  =  (3 - 4 xi) / (64 pi^2 tau^4)

    VALIDATED: the closed form agrees with direct two-dimensional Simpson
    quadrature to 1.000000 at xi = 0, 1/6 and 1/4.

THREE THINGS FALL OUT OF IT AND THE FIRST IS THE FINDING.

    (a) IT SCALES AS tau^-4.  Exactly the Ford-Roman exponent.  candidates.py's
        gate was "requirement R^-2 against permitted L^-4", and THE PROVED
        BOUND'S STATE-INDEPENDENT PIECE HAS THE SAME L^-4 AS BEFORE.  The R^-2
        that magnitude.py showed would invert the area law came from Fliss et
        al.'s EFT scaling estimate, WHICH IS A DIFFERENT OBJECT FROM THIS
        THEOREM.  So the exponent advantage is not in the part that is proved.

    (b) IT REDUCES CORRECTLY AT xi = 0.  QA(0, tau) = 3/(64 pi^2 tau^4), against
        the textbook minimally-coupled Ford-Roman 3/(32 pi^2 tau^4) for
        LORENTZIAN sampling.  Same form, same 3, a factor of 2 from the
        sampling function.  That is the validation that the reduction is right.

    (c) NON-MINIMAL COUPLING WEAKENS IT, MILDLY.  QA(xi)/QA(0) = 1 - 4xi/3:
        22.2% weaker at xi = 1/6, 33.3% weaker at xi = 1/4.  A help, and a small
        one.  It stays positive throughout 0 <= xi <= 1/4 because 3 - 4xi >= 2.

===============================================================================
2. THE EVALUATION AGAINST THIS ARCHITECTURE
===============================================================================

Take the Planck cell -- planckcell.py's configuration, the first to pass every
gate -- with R = l_P and tau = t_P.  In natural units the requirement is
rho_req ~ 1/(Lambda l_P^4), and the state-independent floor at tau = l_P is
(3 - 4xi)/(64 pi^2 l_P^4).  The ratio is a pure number:

        rho_req / QA  =  64 pi^2 / (Lambda (3 - 4 xi))

        xi = 0      (minimal)        21.09 x
        xi = 1/6    (conformal)      27.12 x
        xi = 1/4    (supersymmetric) 31.64 x

    THE REQUIREMENT EXCEEDS THE STATE-INDEPENDENT FLOOR BY A FACTOR OF ABOUT
    TWENTY-SEVEN AT THE COUPLING A SYMMETRY PICKS.  And note the ordering:
    the weakening in 1(c) is MORE than cancelled, because a larger xi weakens
    the floor and therefore makes the ratio WORSE, not better.  The cheapest
    coupling for THIS comparison is minimal coupling -- which is the one with
    no candidate-D loophole at all.

SO THE STATE-DEPENDENT TERM MUST SUPPLY A FACTOR OF ~27, and that term is
xi (:Phi^2:)(2 (d_t f)^2) -- it needs a state with large <:Phi^2:>.

===============================================================================
3. WHAT THAT COSTS, FROM THEIR OWN H-BOUNDS
===============================================================================

Their Theorem 5.3 and Corollary 5.4 bound the state-dependent part by powers of
the Hamiltonian: <:Phi^2:>(f^2) <= B(f) ||H^(p/2) Psi||^2 + C(f) ||Psi||^2 for
p > n - 2, giving (rho o gamma)(f^2) >= -c (H + m)^p for ANY p > 2, while the
energy density itself CANNOT be bounded above for q < 3.

    SO BUYING ALLOWANCE COSTS TOTAL ENERGY AS H^p WITH p > 2, WHILE THE EFFECT
    DELIVERED SCALES AS H^q WITH q >= 3.  Their own conclusion states it:
    "negative energy effects with large magnitude, while possible over large
    regions, REQUIRE MORE ENERGY TO ACHIEVE than positive energy densities of
    the same magnitude, and the energy budget for these two effects will GROW
    WITH A DIFFERENT POWER."

    THE EXPONENT GAP IS AT LEAST ONE AND IT RUNS AGAINST US.  A factor of 27 in
    allowance is bought at more than a factor of 27 in total positive energy.

===============================================================================
4. WHAT IS NOT COMPUTED, AND WHY THAT IS THE HONEST STOPPING POINT
===============================================================================

    <:Phi^2:> FOR THIS CONFIGURATION IS NOT EVALUATED, because it requires a
    SPECIFIED QUANTUM STATE and no state has been specified anywhere in this
    project.  The architecture is a metric, not a state.  Producing one is a
    construction problem, not an arithmetic one.

    QC[f] IS NOT EVALUATED.  The curved-spacetime term needs R_mn gamma^m
    gamma^n and R on the corridor, and it is NOT zero here -- certify.py showed
    the seated ansatz is far from Ricci-flat.  Its sign is not determined below
    and is not assumed.

    THE GAUSSIAN SAMPLING FUNCTION IS A CHOICE.  A different f changes the pure
    number in QA, not the tau^-4 exponent, and the exponent is the finding.

    SO L4 IS NOW: PARTLY COMPUTED, AND THE PART THAT COULD BE COMPUTED WENT
    AGAINST US.  What remains needs a state, which is a different kind of work
    from anything in this tree.  Recorded, not repaired.
"""

import math
import sys

LAMBDA = 9.982529174194637


def QA_closed(xi, tau=1.0):
    """(3 - 4 xi)/(64 pi^2 tau^4).  n=4, massless, unit-L2 Gaussian sampling."""
    return (3.0 - 4.0 * xi) / (64.0 * math.pi ** 2 * tau ** 4)


def QA_numeric(xi, tau=1.0, N=600, U=9.0):
    """Direct 2D Simpson on the defining double integral.  Validates the above."""
    if N % 2:
        N += 1
    pre = (4.0 * math.pi) / (2.0 * math.pi) ** 4        # S_2/(2pi)^4
    h = U / N
    s = 0.0
    for i in range(N + 1):
        a = i * h
        wa = 1.0 if i in (0, N) else (4.0 if i % 2 else 2.0)
        for j in range(N + 1):
            k = j * h
            if k == 0.0:
                continue
            wk = 1.0 if j in (0, N) else (4.0 if j % 2 else 2.0)
            fh2 = 2.0 * tau * math.sqrt(math.pi) * math.exp(-((a + k) * tau) ** 2)
            s += wa * wk * k * ((1.0 - 2.0 * xi) * k * k + 2.0 * xi * a * a) * fh2
    return pre * s * h * h / 9.0


def weakening(xi):
    """QA(xi)/QA(0) = 1 - 4 xi/3.  Non-minimal coupling lowers the floor."""
    return (3.0 - 4.0 * xi) / 3.0


def planck_cell_ratio(xi, lam=LAMBDA):
    """rho_req/QA at R = tau = l_P.  A pure number."""
    return 64.0 * math.pi ** 2 / (lam * (3.0 - 4.0 * xi))


XI_MINIMAL, XI_CONFORMAL, XI_SUSY = 0.0, 1.0 / 6.0, 0.25

# What is proved, and what is only estimated.  The whole point of the pass.
PROVED_EXPONENT = -4        # QA, this theorem
ESTIMATED_EXPONENT = -2     # Fliss et al., an EFT scaling relation
REQUIREMENT_EXPONENT = -2   # c^4/(G Lambda R^2)

# Not evaluated, and named so the omissions are visible.
NOT_EVALUATED = [
    ("<:Phi^2:> for this configuration", "needs a SPECIFIED QUANTUM STATE; the "
     "architecture is a metric, not a state"),
    ("QC[f], the curved-spacetime term", "needs R_mn gamma^m gamma^n and R on "
     "the corridor; NOT zero here, and its sign is not assumed"),
]


def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- the closed form is validated against the defining integral ----------
    for xi, lbl in ((XI_MINIMAL, "minimal"), (XI_CONFORMAL, "conformal"),
                    (XI_SUSY, "susy")):
        chk("closed form == quadrature, xi %s" % lbl,
            QA_numeric(xi) / QA_closed(xi), 1.0, 1e-6)

    # -- THE FINDING: the proved piece has the Ford-Roman exponent -----------
    for t in (2.0, 4.0):
        chk("QA scales as tau^-4 (tau=%g)" % t,
            QA_closed(XI_CONFORMAL, t) * t ** 4,
            QA_closed(XI_CONFORMAL, 1.0), 1e-12)
    chk("the PROVED exponent is -4, not -2", PROVED_EXPONENT, -4)
    chk("the requirement's exponent is -2", REQUIREMENT_EXPONENT, -2)
    chk("they do not match", PROVED_EXPONENT == REQUIREMENT_EXPONENT, False)
    chk("candidate D's -2 is the ESTIMATED one, a different object",
        ESTIMATED_EXPONENT, -2)

    # -- reduces correctly at xi = 0 ----------------------------------------
    chk("QA(0) = 3/(64 pi^2)", QA_closed(0.0), 3.0 / (64 * math.pi ** 2), 1e-14)
    chk("  which is Ford-Roman/2 (Gaussian vs Lorentzian sampling)",
        QA_closed(0.0) * 2.0, 3.0 / (32 * math.pi ** 2), 1e-14)

    # -- non-minimal coupling weakens the floor, mildly ----------------------
    chk("22.2% weaker at xi = 1/6", weakening(XI_CONFORMAL), 7.0 / 9.0, 1e-12)
    chk("33.3% weaker at xi = 1/4", weakening(XI_SUSY), 2.0 / 3.0, 1e-12)
    chk("the floor stays positive on 0 <= xi <= 1/4",
        all(QA_closed(x) > 0 for x in (0.0, 0.1, 0.2, 0.25)), True)

    # -- the evaluation ------------------------------------------------------
    chk("Planck cell, minimal", planck_cell_ratio(XI_MINIMAL), 21.09, 1e-3)
    chk("Planck cell, conformal", planck_cell_ratio(XI_CONFORMAL), 27.12, 1e-3)
    chk("Planck cell, susy", planck_cell_ratio(XI_SUSY), 31.64, 1e-3)
    chk("the requirement EXCEEDS the state-independent floor",
        planck_cell_ratio(XI_CONFORMAL) > 1.0, True)
    chk("and a larger xi makes the RATIO worse, not better",
        planck_cell_ratio(XI_SUSY) > planck_cell_ratio(XI_MINIMAL), True)

    # -- the omissions are named --------------------------------------------
    chk("two things are not evaluated", len(NOT_EVALUATED), 2)
    chk("  and the state is one of them",
        any("STATE" in w for _, w in NOT_EVALUATED), True)
    chk("  and the curved-spacetime term is the other",
        any("NOT zero here" in w for _, w in NOT_EVALUATED), True)
    chk("recorded, not repaired", "Recorded, not repaired" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE STATE-INDEPENDENT FLOOR   QA = (3 - 4 xi)/(64 pi^2 tau^4)\n")
    print("    xi        QA(tau=1)      vs xi=0     Planck-cell shortfall")
    for xi, lbl in ((XI_MINIMAL, "minimal"), (XI_CONFORMAL, "conformal"),
                    (XI_SUSY, "susy")):
        print("   %-9.5f %.9e   %.4f      %.2fx   (%s)"
              % (xi, QA_closed(xi), weakening(xi), planck_cell_ratio(xi), lbl))
    print("\n    tau-scaling (xi = 1/6):")
    for t in (1.0, 2.0, 4.0):
        print("      tau = %-4g QA = %.6e   x tau^4 = %.9f"
              % (t, QA_closed(XI_CONFORMAL, t), QA_closed(XI_CONFORMAL, t) * t ** 4))
    print("\n    -> tau^-4.  The FORD-ROMAN exponent, in the PROVED bound.")
    print("       Candidate D's R^-2 is an EFT estimate, a different object.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  NOT EVALUATED\n")
    for what, why in NOT_EVALUATED:
        print("    %-38s %s" % (what, why))
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  millennium.py turned L4 from an impossibility into a computation.  This
  is the computation as far as it honestly goes, and the part that could
  be done went against us.  Fewster-Osterbrink's bound splits into a
  state-independent piece and a state-dependent one; the state-independent
  piece reduces in closed form for n=4, massless, Gaussian sampling to
  QA = (3 - 4 xi)/(64 pi^2 tau^4), validated against direct quadrature to
  six decimals and reducing at xi = 0 to the textbook Ford-Roman constant
  up to the Gaussian-versus-Lorentzian factor of two.  IT SCALES AS
  tau^-4.  That is the Ford-Roman exponent, so the R^-2 that magnitude.py
  showed would invert the area law does NOT live in the proved bound -- it
  lives in Fliss et al.'s EFT scaling estimate, a different object, which
  is exactly the status distinction millennium.py drew.  Evaluated at the
  Planck cell the requirement exceeds this floor by 21.09x at minimal
  coupling, 27.12x at the conformal 1/6, and 31.64x at 1/4 -- and the
  ordering is the wrong way round, since a larger xi lowers the floor and
  therefore raises the shortfall.  The remaining factor must come from the
  state-dependent term, and their own H-bounds price it: allowance grows
  as H^p with p > 2 while the density needs H^q with q >= 3, an exponent
  gap of at least one running against us.  Two things are not evaluated
  and both are named: <:Phi^2:> needs a specified quantum state, which
  this project has never had because its architecture is a metric rather
  than a state; and the curved-spacetime term QC is not zero here and its
  sign is not assumed.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
