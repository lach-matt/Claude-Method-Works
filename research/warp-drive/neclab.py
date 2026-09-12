#!/usr/bin/env python3
"""
neclab.py -- the door-passing measurement, taken.

THE QUESTION: can the medium carry the analogue NEC violation, and at what cost?
The geometry demands it; the material had never been asked.  Smolyaninov's own
paper is where the gap sits -- he writes

    "Since energy conditions violations do not appear to be a problem in this
     case, metamaterial realization of the warp drive is possible."

and moves on.  Asserted, not computed.  This file computes it.

THE ANSWER: YES, AND IT COSTS 3.2% OF THE STABILITY MARGIN.  And the reason is
structural, not numerical:

    THE MATERIAL IS STRESSED BY THE SHIFT.  THE GEOMETRY VIOLATES THE NEC WITH
    THE SHIFT'S GRADIENT.  THOSE LIVE IN DIFFERENT PLACES AND CANNOT COINCIDE.

  The stability margin m = (eps-1)(mu-1) - g_x^2 is a function of f~ ALONE and
  is strictly monotone decreasing, so its minimum is always at max f~ -- the
  asymptotic medium, OUTSIDE the wall, where the profile is flat.
  The NEC violation goes as (df~/dx~)^2, which vanishes wherever f~ is flat and
  peaks strictly INSIDE the wall.
  For any monotone shape function the two extrema are disjoint.  Verified here
  for three of them (Lorentzian, tanh, quartic): NEC peaks at f~ = 0.25, 0.50,
  0.37 and the margin minimum sits at f~ -> 1 in every case.

  At the exact design limit the separation is extreme: margin +0.9685 where the
  NEC violation is maximal, +0.0004 where the material is worst off -- a ratio
  of 2,510.  Where the medium is on the edge of instability the geometry asks
  nothing of it, and where the geometry asks most the medium has 97% of its
  margin in hand.

-- THE MAPPING, PINNED --------------------------------------------------------
Smolyaninov, Phys. Rev. B 84, 113103 (2011) = arXiv:1009.5663, Eqs (6),(7),(9):

    eps = mu = n / sqrt(1 - (n beta f~)^2)                            (6)
    g_x       = n^2 beta f~ / (1 - (n beta f~)^2)                     (7)
    g_x^2    <= (eps - 1)(mu - 1)     Brown-Hornreich-Shtrikman 1968  (9)

with beta = v_0/c, n the background index, f~ the shape function (f~(0) = 0 in
the bubble, f~ -> 1 outside).  His Eq (10) is (9) at leading order in beta:

    beta f~  <=  (n - 1) / n^2

-- A SECOND FINDING, SMALLER AND WORTH RECORDING ------------------------------
d/dn [(n-1)/n^2] = (2-n)/n^3, so the leading-order bound is maximised at n = 2
and gives beta <= 1/4 -- the published c/4, derived here rather than quoted.

But c/4 is the LEADING-ORDER answer.  Carried through the full Eqs (6) and (7),
the stability margin at f~ = 1 goes NEGATIVE before beta reaches 0.25: the exact
saturation is beta = 0.245826.  At exactly c/4 the medium is unstable by
m = -0.0632.  A 1.7% correction, recorded because a bound quoted to two figures
should be right at two figures.

stdlib only.  Nothing here is taken on trust: c/4 is re-derived, and the
mapping is transcribed from the equations, not from a summary of them.
"""
import math, sys

N_OPT = 2.0          # DERIVED: argmax of (n-1)/n^2
BETA_LEADING = 0.25  # DERIVED: the published c/4, reproduced

# ------------------------------------------------------------- the mapping ---
def eps_mu(n, beta, f):
    """PINNED, Smolyaninov Eq (6).  eps = mu = n / sqrt(1 - (n beta f)^2)."""
    return n / math.sqrt(1.0 - (n * beta * f) ** 2)

def g_x(n, beta, f):
    """PINNED, Eq (7).  The magnetoelectric coupling that carries the shift."""
    return (n * n * beta * f) / (1.0 - (n * beta * f) ** 2)

def margin(n, beta, f):
    """DERIVED.  m = (eps-1)(mu-1) - g_x^2, the slack in Eq (9).  Note it is a
    function of f ALONE at fixed (n, beta) -- no derivative of f appears.  That
    is the whole reason the answer comes out positive."""
    e = eps_mu(n, beta, f)
    return (e - 1.0) ** 2 - g_x(n, beta, f) ** 2

def leading_bound(n):
    """PINNED, Eq (10).  beta f <= (n-1)/n^2 at leading order in beta."""
    return (n - 1.0) / (n * n)

def beta_max_leading():
    """DERIVED.  d/dn[(n-1)/n^2] = (2-n)/n^3 = 0 at n = 2, value 1/4.
    This is the published c/4, obtained rather than quoted."""
    return leading_bound(N_OPT)

def beta_max_exact(n=N_OPT, lo=0.01, hi=0.49):
    """DERIVED.  Where the FULL Eqs (6),(7) saturate Eq (9) at f = 1.  Bisection;
    margin is monotone decreasing in beta at fixed f."""
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if margin(n, mid, 1.0) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

# ------------------------------------------------------- the two profiles ----
SHAPES = {
    "lorentzian": (lambda x: x * x / (x * x + 1.0),
                   lambda x: 2.0 * x / (x * x + 1.0) ** 2),
    "tanh":       (lambda x: 0.5 * (1.0 + math.tanh(x - 2.0)),
                   lambda x: 0.5 / math.cosh(x - 2.0) ** 2),
    "quartic":    (lambda x: x ** 4 / (x ** 4 + 1.0),
                   lambda x: 4.0 * x ** 3 / (x ** 4 + 1.0) ** 2),
}

def nec_density(beta, dfdx):
    """DERIVED.  Alcubierre's structure carried over: T^00 goes as v^2 (df/dr)^2.
    The transverse rho^2/4r^2 factor is dropped in Smolyaninov's 1+1D reduction,
    so this is the violation's SHAPE, not its normalisation -- which is all the
    question needs, since it asks WHERE the violation is."""
    return (beta * dfdx) ** 2

def nec_peak(shape="lorentzian", xmax=10.0, steps=200000):
    """DERIVED.  Where the violation peaks, and the f there."""
    f, df = SHAPES[shape]
    best = max((abs(df(i * xmax / steps)), i * xmax / steps)
               for i in range(1, steps + 1))
    return best[1], f(best[1])

def margin_min_f(n, beta, shape="lorentzian", xmax=40.0, steps=40000):
    """DERIVED.  The f at which the margin is worst over the profile."""
    f, _ = SHAPES[shape]
    return min((margin(n, beta, f(i * xmax / steps)), f(i * xmax / steps))
               for i in range(1, steps + 1))[1]

def margin_is_monotone(n, beta, steps=4000):
    """DERIVED, and this is the theorem.  m(f) strictly decreasing in f means the
    margin minimum is ALWAYS at max f -- outside the wall, where df/dx = 0."""
    ms = [margin(n, beta, i / float(steps)) for i in range(steps + 1)]
    return all(ms[i] >= ms[i + 1] - 1e-15 for i in range(steps))

def cost_of_the_violation(n=N_OPT, beta=None, shape="lorentzian"):
    """DERIVED.  The answer, as a fraction: how much of the stability margin the
    NEC-violating region actually consumes.  m(0) is the margin with no shift;
    m(f at the NEC peak) is the margin where the geometry asks the most."""
    if beta is None:
        beta = beta_max_exact(n)
    _, f_peak = nec_peak(shape)
    return 1.0 - margin(n, beta, f_peak) / margin(n, beta, 0.0)

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        if isinstance(want, bool):
            good, g, w = got == want, got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
            g, w = "%.7g" % got, "%.7g" % want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("c/4 re-derived, not quoted")
    chk("(n-1)/n^2 is maximised at n = 2", N_OPT, 2.0)
    chk("and equals exactly 1/4 there", beta_max_leading(), 0.25)
    # Identity: the derivative (2-n)/n^3 changes sign at 2, so 2 is the argmax.
    chk("the bound is lower on either side of n = 2",
        leading_bound(1.9) < 0.25 and leading_bound(2.1) < 0.25, True)
    chk("Eq (10) is Eq (9) at leading order: g_x = n^2 beta f, eps-1 = n-1",
        (N_OPT ** 2 * 0.25 * 1.0) / (N_OPT - 1.0), 1.0)

    print("\nThe full expressions correct it by 1.7%")
    be = beta_max_exact()
    chk("exact saturation beta", be, 0.2458262875, tol=1e-9)
    chk("margin at exactly c/4 is NEGATIVE", margin(N_OPT, 0.25, 1.0) < 0.0, True)
    chk("its value there", margin(N_OPT, 0.25, 1.0), -0.0632465980, tol=1e-9)
    chk("and zero at the exact bound", margin(N_OPT, be, 1.0), 0.0, tol=1e-8)

    print("\nTHE THEOREM: the margin depends on f alone and decreases")
    for b in (0.05, 0.10, 0.20, be):
        chk("m(f) monotone decreasing at beta = %.4f" % b,
            margin_is_monotone(N_OPT, b), True)
    chk("m(0) is the same at every beta -- no shift, no stress",
        margin(N_OPT, 0.05, 0.0), margin(N_OPT, 0.24, 0.0))
    chk("m(0) = (n-1)^2", margin(N_OPT, 0.2, 0.0), 1.0)

    print("\nTHE MEASUREMENT: the two extrema are disjoint")
    # The NEC peak is interior for every monotone shape; the margin minimum is
    # at f -> 1.  Analytic check on the Lorentzian: peak at x = 1/sqrt(3), f = 1/4.
    x, fp = nec_peak("lorentzian")
    chk("Lorentzian NEC peak at x = a/sqrt(3)", x, 1.0 / math.sqrt(3.0), tol=1e-4)
    chk("  where f = 1/4 exactly", fp, 0.25, tol=1e-4)
    for shape, want in (("lorentzian", 0.25), ("tanh", 0.50), ("quartic", 0.37500)):
        _, fpk = nec_peak(shape)
        chk("%s NEC peak sits at f =" % shape, fpk, want, tol=2e-3)
        chk("  and its margin minimum is at f -> 1",
            margin_min_f(N_OPT, 0.20, shape) > 0.98, True)
        chk("  so they do not coincide", abs(fpk - 1.0) > 0.1, True)

    print("\nTHE COST")
    cost = cost_of_the_violation()
    chk("fraction of margin the violation consumes", cost, 0.031503153, tol=1e-7)
    chk("  i.e. under 4%", cost < 0.04, True)
    _, fpk = nec_peak("lorentzian")
    chk("margin where the geometry asks most", margin(N_OPT, be, fpk), 0.968496847, tol=1e-7)
    chk("margin where the material is worst off", margin(N_OPT, be, 1.0), 0.0, tol=1e-8)
    chk("the medium CAN carry it", margin(N_OPT, be, fpk) > 0.0, True)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    be = beta_max_exact()
    x, fpk = nec_peak("lorentzian")
    print("""
neclab.py -- the door-passing measurement, taken
================================================================================
Q: can the medium carry the analogue NEC violation, and at what cost?

Smolyaninov's paper is where the gap sits.  He writes "Since energy conditions
violations do not appear to be a problem in this case, metamaterial realization
of the warp drive is possible" -- and moves on.  Asserted, never computed.

-- FIRST, c/4 RE-DERIVED RATHER THAN QUOTED -----------------------------------
  Eq (10) is beta f~ <= (n-1)/n^2.  Its derivative in n is (2-n)/n^3, zero at
  n = 2, so the bound is maximised there and equals exactly 1/4.  That is the
  published figure, obtained.

  But it is the LEADING-ORDER figure.  Carried through the full Eqs (6) and (7),
  the margin at f~ = 1 goes negative before beta reaches 0.25:

      exact saturation      beta = %.6f
      margin at exactly c/4        %+.6f      (unstable)

  A 1.7%% correction, recorded because a bound quoted to two figures should hold
  at two figures.

-- THE ANSWER, AND IT IS STRUCTURAL --------------------------------------------
  The stability margin m = (eps-1)(mu-1) - g_x^2 is a function of f~ ALONE.  No
  derivative of f~ appears in it.  And it is strictly monotone decreasing, so

      THE MARGIN MINIMUM IS ALWAYS AT MAX f~ -- OUTSIDE, WHERE f~ IS FLAT.

  The NEC violation goes as (df~/dx~)^2.  It vanishes wherever f~ is flat, so

      THE VIOLATION PEAK IS ALWAYS STRICTLY INSIDE THE WALL.

  For any monotone shape function those two cannot coincide.  Checked on three:
""" % (be, margin(N_OPT, 0.25, 1.0)))
    print("    %-12s %14s %16s %10s" % ("shape", "NEC peak at f~", "margin min at f~", "coincide"))
    for shape in SHAPES:
        _, fp = nec_peak(shape)
        fm = margin_min_f(N_OPT, 0.20, shape)
        print("    %-12s %14.4f %16.4f %10s" % (shape, fp, fm, "no"))
    print("""
  The material is stressed by the SHIFT.  The geometry violates the NEC with the
  shift's GRADIENT.  They live in different places, and the separation is not a
  numerical accident -- it follows from m depending on f~ and not on df~/dx~.

-- THE COST --------------------------------------------------------------------
  At the exact design limit beta = %.6f, on Smolyaninov's own profile:

      margin with no shift at all              %+.5f
      margin where the geometry asks MOST      %+.5f     (f~ = %.2f)
      margin where the material is WORST off   %+.5f     (f~ -> 1)

      THE NEC VIOLATION CONSUMES %.2f%% OF THE STABILITY MARGIN.

  The worst-point margin is zero AT saturation by definition, so the comparison
  is quoted just inside it, at 99%% of the limit (beta = %.6f):

      margin where the geometry asks MOST      %+.5f
      margin where the material is WORST off   %+.5f
      ratio                                    %.0f

  Where the medium sits on the edge of instability the geometry asks nothing of
  it; where the geometry asks most, the medium still holds 97%% of its margin.

    THE MEDIUM CAN CARRY THE ANALOGUE NEC VIOLATION.  IT IS NOT WHAT COSTS.
    WHAT COSTS IS THE ASYMPTOTIC SHIFT, AND THAT IS WHAT c/4 ALREADY PRICES.

-- WHAT IT DOES AND DOES NOT SETTLE --------------------------------------------
  Settles: the energy-condition objection does not transfer to the analogue, and
  now for a computed reason rather than an assertion.  Smolyaninov was right and
  did not show it.

  Does not settle: the remaining cost is materials, and it is the one he DID
  quantify -- classical magnetoelectrics (Cr2O3, multiferroics) sit two orders
  of magnitude below the Eq (9) limit, so the build needs the engineered
  split-ring-plus-magnetised-ferrite design, non-reciprocal and bi-anisotropic,
  with loss compensation.  That is an inventory of parts, not a bound.

  And it remains an ANALOGUE: it does not gravitate the emulated shift.  Under
  door.py's test it is a MEASUREMENT and not a relabel, because the requirement
  came from the geometry and was not designed into the material -- which is
  exactly why it could have come out the other way, and did not.
""" % (be, margin(N_OPT, be, 0.0),
       margin(N_OPT, be, fpk), fpk, margin(N_OPT, be, 1.0),
       100.0 * cost_of_the_violation(),
       0.99 * be, margin(N_OPT, 0.99 * be, fpk), margin(N_OPT, 0.99 * be, 1.0),
       margin(N_OPT, 0.99 * be, fpk) / margin(N_OPT, 0.99 * be, 1.0)))
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
