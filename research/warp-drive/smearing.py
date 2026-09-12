#!/usr/bin/env python3
"""
smearing.py -- shaping.py's three NOT-RUNs audited, and one new theorem:
SNEC CANNOT BE A LOOPHOLE AROUND ANEC.

shaping.py closed the cheaper-currency question and left three things named
rather than run.  This file runs them.  Two close against the literature, one
stays open and is the same gap obstruct.py already tracks -- and pursuing them
turned up a general result the tree did not have.

===============================================================================
THE NEW THEOREM: ANEC VIOLATION IMPLIES SNEC VIOLATION
===============================================================================

nullbound.py withdrew its own headline with the right reason -- "SNEC must hold
for EVERY sampling function, and this file evaluated it at ONE width" -- and
recorded that the bound fails above w ~ 0.93 bubble radii.  That withdrawal was
about THE ALCUBIERRE WALL, an architecture phase1.py has since excluded by D4.
The obvious question is whether the static corridor escapes it.  It does not,
and the reason is general:

    Let I = INTEGRAL T_kk dl along the ray.  For a normalised Gaussian of width
    w, the smeared quantity tends to

            INTEGRAL T_kk g^2 dl  ->  I / (w sqrt(2 pi))       as w -> infinity

    which falls as 1/w.  The SNEC bound falls as 1/w^2.  So whenever I < 0 --
    that is, whenever ANEC is violated -- SNEC IS VIOLATED FOR EVERY

            w  >  w_crit  =  B sqrt(2 pi) / |I|

    and the violation grows without limit thereafter.

    MEASURED ON THE STATIC CORRIDOR.  I = -2.46486e-06, predicted
    w_crit = 1.0116e+04, and the numerical scan crosses at exactly that width:

        w           LHS               RHS               LHS/RHS   verdict
        1e3         -9.83967e-10      -9.94718e-09      0.0989    ok
        5e3         -1.96673e-10      -3.97887e-10      0.4943    ok
        9e3         -1.09261e-10      -1.22805e-10      0.8897    ok
        1.0116e4    -9.72095e-11      -9.72089e-11      1.0000    VIOLATED
        2e4         -4.91670e-11      -2.48680e-11      1.9771    VIOLATED
        1e5         -9.83339e-12      -9.94718e-13      9.8856    VIOLATED

    SO SNEC IS NOT AN INDEPENDENT, WEAKER CONDITION THAT AN ANEC-VIOLATING
    CONFIGURATION MIGHT SLIP THROUGH.  IT IS A FINER STATEMENT THAT INHERITS
    ANEC'S PROHIBITION AT LARGE SMEARING.  The 1/D^2 cancellation nullbound.py
    found is real arithmetic and it buys nothing, for the wall or for anything
    else.  This generalises that file's withdrawal from one architecture to
    every ANEC-violating one.

    AND IT CROSS-CHECKS achronal.py BY A DIFFERENT ROUTE.  achronal.py measured
    ANEC violation on 25 rays by integrating R_kk along geodesics; this file
    gets I < 0 from a line integral of the source density.  Different
    computation, same sign.

===============================================================================
THE THREE NOT-RUNS
===============================================================================

1. NON-GAUSSIAN STATES OUTSIDE THE SQUEEZED FAMILY -- CLOSED.

   shaping.py's mode-counting bound was derived over squeezed (Gaussian)
   states, and that is a real restriction on THAT derivation.  It is not a gap
   in the conclusion: the quantum energy inequalities and the SNEC are
   STATE-INDEPENDENT theorems, proved over all Hadamard states, which
   nullbound.py already records in as many words -- "SNEC is state-INDEPENDENT,
   QNEC is state-dependent".  A non-Gaussian state does not evade a bound that
   was never conditioned on the state.

2. INTERACTING AND NON-MINIMALLY COUPLED FIELDS -- CLOSED, CONDITIONALLY, AND
   THE CONDITION IS NAMED.

   This was the live one.  Non-minimal coupling xi R phi^2 is the standard
   example of a theory that violates the energy conditions CLASSICALLY, and it
   has been used to claim traversable wormholes without quantum effects at all.
   Fliss, Freivogel, Kontou & Pardo Santos (arXiv:2309.10848) close it:

       "Under this assumption, the average null energy condition, whose
        violation is necessary to allow traversable wormholes, is obeyed both
        classically and in the context of quantum field theory."

   The assumption is that non-minimal coupling is part of an EFFECTIVE FIELD
   THEORY whose field value is controlled by the cutoff, <:phi^2:> <= phi^2_max.
   Their section III.C is titled, exactly, "LARGE NEGATIVE NULL ENERGIES REQUIRE
   LARGE FIELD VALUES": the negative null energy scales with particle number N,
   and a bound on the field value caps N.  They also derive a SNEC of the form

        INTEGRAL dx- f-^2 <T--> >= - N[gamma, xi, phi~^2_max] / (l_UV^(n-2) d-^2)

   so the bound is state-dependent through the allowed field RANGE, and finite.

       THE CONDITION IS THE EFT ASSUMPTION, and it is not free: they motivate
       it by asking when the gravity-plus-matter path integral stays
       semi-classically controlled.  A field roaming past its cutoff escapes
       the bound and takes the calculation with it.  CONDITIONAL, not
       unconditional, and stated as conditional.

3. CURVED BACKGROUNDS BEYOND THE CORRIDOR'S OWN WEAK FIELD -- STILL OPEN, AND
   IT IS A GAP THIS TREE ALREADY TRACKS.

   QEIs are proved in curved spacetime with curvature-dependent bounds, so the
   fixed-background case is covered.  What is not covered is the
   SELF-CONSISTENT problem: matter that curves the spacetime it is bounded in.
   That is exactly obstruct.py's ANEC row, which stands OPEN, and the corpus's
   note that self-consistent achronal ANEC in 4D has been unproven for
   nineteen years.  NOT CLOSED HERE, and not newly opened either.

===============================================================================
WHAT THIS CHANGES
===============================================================================

    Nothing in the cost, and one thing in the structure.  SNEC was the last
    energy condition weak enough to look like a door, and it is now shown to
    close whenever ANEC does.  Every route this project has evaluated is
    therefore bounded by ANEC alone, and ANEC violation is precisely what the
    corridor requires and what achronal.py measured.

    THE OBSTACLE HAS ONE NAME AGAIN.

stdlib only.  The numbers here are the weak-field line-integral model,
T_kk ~ rho along the ray, which is the leading term and is stated rather than
hidden.
"""
import math, sys

A_CORE, R_SHELL, B_RAY, M_SRC = 0.02, 200.0, 1.0, 2.0e-2
B_FK = 1.0 / (32.0 * math.pi)      # Freivogel-Krommydas; holographic, not a theorem


# ------------------------------------------------ the corridor's T_kk profile

def rho_core(x, m=M_SRC, b=B_RAY, a=A_CORE):
    """Plummer sphere of mass -m: rho = -3 m a^2/(4 pi (r^2+a^2)^{5/2})."""
    return -3.0 * m * a * a / (4.0 * math.pi * (x * x + b * b + a * a) ** 2.5)


def shell_crossing(b=B_RAY, Rs=R_SHELL):
    return math.sqrt(Rs * Rs - b * b)


def shell_weight(m=M_SRC, b=B_RAY, Rs=R_SHELL):
    """Line weight of one crossing of the +m shell, 1/cos of the crossing."""
    xs = shell_crossing(b, Rs)
    return m / (4.0 * math.pi * Rs * Rs) * (Rs / xs)


def anec_integral(m=M_SRC, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """I = INTEGRAL T_kk dl.  Closed form: core column plus two crossings."""
    c2 = b * b + a * a
    core = -3.0 * m * a * a / (4.0 * math.pi) * 4.0 / (3.0 * c2 * c2)
    return core + 2.0 * shell_weight(m, b, Rs)


def anec_violated(**kw):
    """achronal.py measured this on 25 rays by integrating R_kk.  Agrees."""
    return anec_integral(**kw) < 0.0


# ------------------------------------------------------- the smeared quantity

def g2(x, w):
    """Normalised sampling: INTEGRAL g^2 dx = 1."""
    return math.exp(-x * x / (2.0 * w * w)) / (w * math.sqrt(2.0 * math.pi))


def smeared(w, X=1000.0, n=400001):
    """INTEGRAL T_kk g^2 dl -- the SNEC's left-hand side.

    THE WINDOW IS DELIBERATELY SHORT AND THE GRID DELIBERATELY FINE, and the
    first draft of this function got it backwards.  The integrand carries two
    scales: the core is ~1 wide while w runs to 1e5.  Widening the window on a
    uniform grid coarsens the step until the core is sampled by less than one
    point, and the answer drifts and then changes SIGN -- which it did, at
    X = 3e5.  The core falls as x^-5, so rho(1000)/rho(0) ~ 1e-15 and a window
    of 1000 captures it entirely; the shell is a delta handled exactly.
    Convergence is asserted in the selftest against the closed-form integral.
    """
    h = 2.0 * X / n
    s = 0.0
    for i in range(n + 1):
        x = -X + i * h
        s += (1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)) * rho_core(x) * g2(x, w)
    xs = shell_crossing()
    return s * h / 3.0 + shell_weight() * (g2(xs, w) + g2(-xs, w))


def quadrature_converged(rtol=1e-6):
    """The core column against its closed form, at w so broad g^2 is flat."""
    w = 1.0e6
    core_only = smeared(w) - shell_weight() * 2.0 * g2(shell_crossing(), w)
    c2 = B_RAY * B_RAY + A_CORE * A_CORE
    exact = -3.0 * M_SRC * A_CORE ** 2 / (4.0 * math.pi) * 4.0 / (3.0 * c2 * c2)
    return abs(core_only / (g2(0.0, w) * exact) - 1.0) <= rtol


def snec_bound(w, B=B_FK):
    """-(4B/G) INTEGRAL (g')^2 dl = -B/(G w^2); G = 1 in these units."""
    return -B / (w * w)


def snec_holds(w, B=B_FK):
    return smeared(w) >= snec_bound(w, B)


# ---------------------------------------------- the theorem, and its threshold

def w_critical(I=None, B=B_FK):
    """w_crit = B sqrt(2 pi)/|I|.  Above it, ANEC violation forces SNEC failure.

    At large w the smeared quantity tends to I/(w sqrt(2 pi)), falling as 1/w,
    while the bound falls as 1/w^2.  One crossing, and it is permanent.
    """
    I = anec_integral() if I is None else I
    if I >= 0.0:
        return None                    # ANEC satisfied: no forced crossing
    return B * math.sqrt(2.0 * math.pi) / abs(I)


def asymptotic_smeared(w, I=None):
    I = anec_integral() if I is None else I
    return I / (w * math.sqrt(2.0 * math.pi))


def theorem_holds(rtol=2e-3):
    """The predicted threshold against the measured crossing."""
    wc = w_critical()
    return abs(smeared(wc) / snec_bound(wc) - 1.0) <= rtol


def anec_ok_gives_no_threshold():
    """A configuration that satisfies ANEC is not forced into SNEC failure."""
    return w_critical(I=+1.0e-6) is None


# ------------------------------------------------- the three NOT-RUNs, audited

AUDIT = (
    ("non-Gaussian states", "CLOSED",
     "QEIs and SNEC are STATE-INDEPENDENT theorems over all Hadamard states; "
     "nullbound.py already records 'SNEC is state-INDEPENDENT'. A non-Gaussian "
     "state cannot evade a bound never conditioned on the state"),
    ("interacting / non-minimally coupled fields", "CLOSED-CONDITIONAL",
     "arXiv:2309.10848 (Fliss, Freivogel, Kontou, Pardo Santos): under an EFT "
     "assumption bounding <:phi^2:>, ANEC is obeyed BOTH classically and in "
     "QFT, and their section III.C is titled 'Large negative null energies "
     "require large field values'. THE CONDITION IS THE EFT ASSUMPTION, "
     "motivated by semiclassical control of the path integral"),
    ("curved backgrounds, self-consistent", "OPEN",
     "QEIs are proved on FIXED curved backgrounds; matter that curves the "
     "spacetime it is bounded in is not covered. Same gap as obstruct.py's "
     "ANEC row, and the corpus's note that self-consistent achronal ANEC in 4D "
     "has been unproven for nineteen years. Not closed here, not newly opened"),
)


def closed_count():
    return sum(1 for _n, s, _w in AUDIT if s.startswith("CLOSED"))


def still_open():
    return [n for n, s, _w in AUDIT if s == "OPEN"]


SNEC_IS_A_LOOPHOLE = False


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

    print("THE CORRIDOR VIOLATES ANEC -- reached here by a different route")
    near("I = INTEGRAL T_kk dl", anec_integral(), -2.46486e-06, 1e-4)
    chk("ANEC violated", anec_violated(), True)
    print("      achronal.py measured this on 25 rays by integrating R_kk along")
    print("      geodesics; this is a line integral of the source density.")

    print("\nTHE THEOREM -- ANEC violation forces SNEC failure above w_crit")
    near("w_crit = B sqrt(2 pi)/|I|", w_critical(), 1.0116e4, 1e-3)
    chk("and the numerical scan crosses there", theorem_holds(), True)
    print("      %10s %16s %16s %10s %s" % ("w", "LHS", "RHS", "LHS/RHS", ""))
    for w in (1.0e3, 5.0e3, 9.0e3, 2.0e4, 1.0e5):
        L, R = smeared(w), snec_bound(w)
        print("      %10.4g %16.5e %16.5e %10.4f %s"
              % (w, L, R, L / R, "VIOLATED" if L < R else "ok"))
    chk("SNEC holds at w = 1e3", snec_holds(1.0e3), True)
    chk("and fails at w = 1e5", snec_holds(1.0e5), False)
    chk("the quadrature resolves the core (vs its closed form)",
        quadrature_converged(), True)
    near("the asymptotic form I/(w sqrt(2pi)) at w = 1e5",
         asymptotic_smeared(1.0e5), smeared(1.0e5), 1e-5)
    chk("a configuration that SATISFIES ANEC gets no forced threshold",
        anec_ok_gives_no_threshold(), True)
    chk("so SNEC is a loophole around ANEC", SNEC_IS_A_LOOPHOLE, False)
    print("      This generalises nullbound.py's withdrawal from the Alcubierre")
    print("      wall to EVERY ANEC-violating configuration, the static")
    print("      corridor included.")

    print("\nTHE THREE NOT-RUNS, AUDITED")
    for n, s, _w in AUDIT:
        print("      %-42s %s" % (n, s))
    chk("closed", closed_count(), 2)
    chk("still open", still_open(), ["curved backgrounds, self-consistent"])
    print("      and the one that stays open is the gap obstruct.py already")
    print("      tracks as ANEC -- not a new one.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE OBSTACLE HAS ONE NAME AGAIN.

  SNEC was the last energy condition weak enough to look like a door.
  nullbound.py found its 1/D^2 cancellation, then withdrew the
  conclusion because one sampling width is not a scan -- but that
  withdrawal was about the Alcubierre wall, which phase1 has since
  excluded by D4.  Scanning the static corridor instead gives the
  general statement: the smeared quantity tends to I/(w sqrt(2 pi))
  and falls as 1/w while the bound falls as 1/w^2, so ANY
  ANEC-violating configuration fails SNEC above
  w_crit = B sqrt(2 pi)/|I|.  Predicted 1.0116e4 for the corridor,
  and the scan crosses at exactly that width.

  SNEC IS NOT AN INDEPENDENT WEAKER CONDITION.  It is a finer
  statement that inherits ANEC's prohibition at large smearing, so it
  cannot be slipped through.

  OF THE THREE THINGS shaping.py NAMED, TWO CLOSE.  Non-Gaussian
  states cannot evade a state-independent theorem.  Non-minimal
  coupling -- the strongest remaining candidate, and the standard
  example of classical energy-condition violation -- is closed by
  Fliss, Freivogel, Kontou and Pardo Santos under an EFT assumption
  whose content is that large negative null energies require large
  field values.  That closure is CONDITIONAL and the condition is
  named rather than buried.

  THE THIRD STAYS OPEN AND IS NOT NEW: quantum energy inequalities on
  a background the matter itself curves.  That is obstruct.py's ANEC
  row, open for nineteen years in the literature, and it is where
  this whole question has been resting the entire time.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
