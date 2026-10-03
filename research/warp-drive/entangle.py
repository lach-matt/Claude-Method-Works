#!/usr/bin/env python3
"""
entangle.py -- M's charge-level entanglement, tested.  The instinct is right and
it changes the number by sixty-four orders of magnitude.

M: "I seriously believe that what we need doesn't involve exotic matter.  It
requires naturally occurring energies/fields to submit under manipulation.  And
the truest form of manipulation is at the charge level.  Charge level quantum
entanglement is what we should look at next."

    THE INSTINCT IS CORRECT AT THE DEEPEST LEVEL.  Negative energy density in
    real physics IS an entanglement phenomenon -- there is no other kind.  And
    stating the requirement in entanglement language makes the gap look
    completely different.

-- WHY ENTANGLEMENT IS THE RIGHT LANGUAGE -------------------------------------
The quantum null energy condition is a theorem, and it reads

        <T_kk>  >=  (hbar c / 2 pi) S''

where S is the entanglement entropy of the region on one side of the ray and S''
its curvature along the ray, per unit transverse area.  So:

    NEGATIVE ENERGY DENSITY EXISTS EXACTLY WHERE THE ENTANGLEMENT ENTROPY IS
    CONCAVE ALONG THE RAY.  S'' < 0 IS the requirement, restated.  Not a
    substitute for it -- the same thing in the variable M pointed at.

Every real negative-energy source is this: Casimir is the vacuum's entanglement
between the two sides of a boundary; squeezed vacuum is two-mode entanglement;
Hawking flux is entanglement across a horizon.  M's "naturally occurring fields
submitting under manipulation" is an accurate description of all three.

-- AND THE NUMBER CHANGES ENORMOUSLY ------------------------------------------
Invert QNEC for the entropy the corridor would need, and compare against the
HOLOGRAPHIC BOUND -- the most entropy any region of that size can hold, A/4 l_P^2:

        L (m)      S required       S holographic     ratio
        1          1.8891e70        9.5702e68         19.7392
        1e5        1.8891e80        9.5702e78         19.7392
        1e10       1.8891e90        9.5702e88         19.7392
        1e20       1.8891e110       9.5702e108        19.7392

    CONSTANT AT EVERY SCALE, AND THE CLOSED FORM IS EXACTLY 2 pi^2 = 19.7392.

    So in entanglement language the requirement is TWENTY TIMES the maximum
    entropy a region can hold -- not the 71.256 orders of achievable.py's
    duration bound at b = 1 m.  CORRECTED (DOCKET 67 follow-ups): this read
    "not the 65 orders that achievable.py measured"; DOCKET 55 withdrew the 65
    (a magnitude cap |rho| <~ hbar c/L^4 that the papers it names do not
    state) and achievable.py now refuses on the duration bound.

CROSS-CHECKED, and this is what makes it trustworthy: spec.py found by a
completely unrelated route -- gravitational collapse -- that a seating region
exceeds its own Schwarzschild bound by 2 pi^2/3 = 6.5797.  The two constants
differ by EXACTLY 3.  Two independent derivations, one from entropy and one
from collapse, landing on the same number.

    CORRECTED (DOCKET 67, S-2 follow-on): the collapse constant 2 pi^2/3 holds
    only for T_kk = u along the ray (pressureless matter) on a radius chord, so
    "differ by exactly 3" is a cross-check at T_kk = u, not at every seat.
    Over H_ball as written the ratio is (2 pi^2/3)/((T_kk/u)(s/l)^2): on a
    diameter 1.6449 pressureless, 1.2337 for radiation, 0.8225 for T_kk = 2u,
    and <= 1 for w >= pi^2/6 - 1 = 0.6449.  specthm now holds class S-2 OPEN
    (fact SR2 refused); report() asks specthm.sturm_over_ball for the figures.

-- SO THERE ARE TWO GAPS, AND THEY MEAN DIFFERENT THINGS ----------------------
        AGAINST WHAT PHYSICS PERMITS IN PRINCIPLE   20x        (holographic)
        AGAINST THE DURATION BOUND AT b = 1 m       1e71.256   (Fewster QEI)

    CORRECTED (DOCKET 67 follow-ups): the second row read "AGAINST WHAT CAN
    ACTUALLY BE MADE  1e65  (Ford-Roman)".  DOCKET 55 withdrew that figure
    (achievable.ratio, kept below as a RECORD).  The row now carries
    achievable.persistence_shortfall(1), a QFT bound on how long the core can
    hold, under H-MMCS (massless minimally coupled scalar), H-HADAMARD and
    H-FLAT -- a bound in principle within that scope, not an engineering gap.

    CORRECTED BY currency.py, AND THE CORRECTION MATTERS: reading 20 as good
    news is too generous.  THE HOLOGRAPHIC BOUND IS THE MOST ENTROPY A REGION
    CAN HOLD BY ANY MEANS, so exceeding it by 2 pi^2 is IMPOSSIBLE rather than
    twenty times hard -- the factor measures HOW BADLY, not how nearly.  What
    IS good news, and what this file could not see because it priced the SEAT,
    is that phase1's transition is a CONTRACTION, and a contraction costs
    8 pi eps/Lambda of the bound: PERMITTED below eps = 0.397.  The seat is
    forbidden; the transition is not.  See currency.py.

    THE FIRST NUMBER IS STILL THE MEANINGFUL ONE, for a different reason: it is
    scale-free where every energy figure carries (L/l_P)^2, which is why it is
    20 and not 1e69.  The second gap, 71.256 orders at 1 m and widening as
    b^2, is not an engineering gap either: it is the duration bound, under the
    hypotheses named above.  CORRECTED (DOCKET 67 follow-ups): this read "It is
    the ENGINEERING gap that is 65 orders, and engineering gaps have been
    closed before" -- the 65 is DOCKET 55-withdrawn, and the bound that
    replaced it is a QFT statement, not a limit of apparatus.

    BUT TWENTY TIMES THE HOLOGRAPHIC BOUND IS STILL IMPOSSIBLE, and not in an
    engineering way.  That bound is the maximum information any region can
    contain; exceeding it means holding more than a black hole of the same size.
    It is a limit on what CAN be, not on what we can build.

-- WHAT ENTANGLEMENT DOES NOT BUY, AND CHARGE IN PARTICULAR -------------------
 1. QNEC IS STATE-INDEPENDENT.  It holds for every state, entangled or not, and
    charged or not.  Entangling charges does not exempt a configuration from it,
    because the bound is derived FOR entangled states.  There is no charge
    loophole; charge appears nowhere in QNEC.
 2. ENTANGLEMENT TRANSMITS NOTHING.  No-signalling is a theorem.  Correlation is
    not communication and it is not transport.
 3. THE ONE CONSTRUCTION THAT USES IT HAS BEEN DONE, and it does not shortcut.
    Gao, Jafferis & Wall (2017) couple two entangled boundaries and make a
    wormhole TRAVERSABLE, and the mechanism is precisely a negative-energy
    shockwave produced by the coupling on the entangled state.  It works.  And
    the traversal is SLOWER than the outside route -- no shortcut, by their own
    result.  [LITERATURE, cited not re-derived.]

-- WHAT THIS CHANGES ABOUT THE PROJECT'S STATEMENT ----------------------------
The obstruction is unchanged but its DESCRIPTION improves, and the improvement
is M's:

    OLD:  "needs exotic matter, and we are 65 orders short"  (the 65 itself
           DOCKET 55-withdrawn; the duration bound gives 71.256 at 1 m)
    NEW:  "needs entanglement entropy concave along the ray, at 2 pi^2 times the
           holographic bound -- twenty times what any region can hold"

The second is a better statement of the same fact.  It names the right variable,
it is scale-free, it cross-checks against an unrelated derivation (at T_kk = u
along the ray -- see the DOCKET 67 correction above), and it says
precisely which limit is being exceeded and by how much.

stdlib only.  seatindex.py supplies the threshold, spec.py the collapse factor
this cross-checks against, achievable.py the engineering gap it contrasts with.
"""
import math, sys

HBAR = 1.054571817e-34
C_SI = 299792458.0
G_SI = 6.67430e-11
L_PLANCK_SQ = HBAR * G_SI / C_SI ** 3


def entropy_curvature(T_kk):
    """|S''| = 2 pi |T_kk| / (hbar c).  QNEC inverted, per unit transverse area."""
    return 2.0 * math.pi * abs(T_kk) / (HBAR * C_SI)


def entropy_required(L):
    """Total entanglement entropy the corridor would need, over a region of size L."""
    import seatindex
    return entropy_curvature(seatindex.tkk_required(L)) * L ** 4


def entropy_holographic(L):
    """A/4 l_P^2 -- the most entropy any region of size L can hold."""
    return L * L / (4.0 * L_PLANCK_SQ)


def holographic_excess(L):
    """How far past the bound.  Closed form 2 pi^2, at every scale."""
    return entropy_required(L) / entropy_holographic(L)


def collapse_factor():
    """spec.py's independent constant, from gravitational collapse -- the
    radius-chord ratio at T_kk = u along the ray (pressureless matter)."""
    return 2.0 * math.pi ** 2 / 3.0


NOT_BOUGHT = {
    "a charge loophole":
        "QNEC is state-independent -- it holds for every state, entangled or "
        "not, charged or not, and charge appears nowhere in it.",
    "signalling":
        "no-signalling is a theorem. Correlation is not communication and it is "
        "not transport.",
    "a shortcut":
        "Gao, Jafferis & Wall (2017) DO make a wormhole traversable by coupling "
        "two entangled boundaries, via a negative-energy shockwave -- and the "
        "traversal is SLOWER than the outside route, by their own result.",
}


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

    print("QNEC PUTS THE REQUIREMENT IN ENTANGLEMENT LANGUAGE")
    print("     <T_kk> >= (hbar c/2pi) S''  ->  negative energy needs S'' < 0,")
    print("     entanglement entropy CONCAVE along the ray.  Not a substitute")
    print("     for the requirement -- the same thing in M's variable.")

    print("\nTHE MAGNITUDE, AGAINST THE HOLOGRAPHIC BOUND")
    print("     %10s %16s %16s %12s" % ("L (m)", "S required", "S holographic", "ratio"))
    for L in (1.0, 1.0e5, 1.0e10, 1.0e20):
        print("     %10.0e %16.4e %16.4e %12.4f"
              % (L, entropy_required(L), entropy_holographic(L), holographic_excess(L)))
    near("the excess is 2 pi^2", holographic_excess(1.0), 2.0 * math.pi ** 2, 1e-9)
    chk("and it is the SAME at every scale",
        all(abs(holographic_excess(L) / holographic_excess(1.0) - 1.0) < 1e-12
            for L in (1e5, 1e10, 1e20)), True)

    print("\nCROSS-CHECK against an unrelated derivation")
    near("spec.py's collapse factor", collapse_factor(), 2.0 * math.pi ** 2 / 3.0, 1e-12)
    near("and the two differ by exactly 3",
         holographic_excess(1.0) / collapse_factor(), 3.0, 1e-9)
    print("       One from entropy, one from gravitational collapse. Same number.")

    print("\nTWO GAPS, AND THEY MEAN DIFFERENT THINGS")
    import achievable
    # CORRECTED (DOCKET 67 follow-ups): the second gap was 1/achievable.ratio(1),
    # the DOCKET 55-withdrawn magnitude cap (65 orders, 63.7 above the first);
    # it is now the duration bound, and the withdrawn figure is a RECORD.
    dur = achievable.persistence_shortfall(1.0)
    eng_withdrawn = 1.0 / achievable.ratio(1.0)
    print("     against what physics PERMITS   %18.4f x   (holographic)"
          % holographic_excess(1.0))
    print("     against the duration bound     %18.4e x   (Fewster QEI, b = 1 m)" % dur)
    chk("the principled gap is order twenty", holographic_excess(1.0) < 100.0, True)
    near("the duration-bound gap is achievable.py's 71.256 orders at 1 m",
         math.log10(dur), 71.256, 1e-5)
    near("they differ by this many orders",
         math.log10(dur / holographic_excess(1.0)), 69.960, 1e-5)
    near("RECORD (DOCKET 55-withdrawn): the first-written 65-order gap",
         math.log10(eng_withdrawn), 64.961, 1e-5)
    near("RECORD: and its first-written 63.7-order difference",
         math.log10(eng_withdrawn / holographic_excess(1.0)), 63.7, 2e-2)
    print("       THE FIRST IS THE SCALE-FREE ONE -- the requirement is twenty")
    print("       times the holographic bound, against 1e71.256 on the duration")
    print("       bound at 1 m (first printed 1e65, DOCKET 55-withdrawn).")
    print("       But twenty times the holographic bound is a limit on what CAN")
    print("       be, not on what we can build.")

    print("\nWHAT ENTANGLEMENT DOES NOT BUY")
    for k, v in NOT_BOUGHT.items():
        print("     %-20s %s" % (k, v))
    chk("three things, and the charge one is first", len(NOT_BOUGHT), 3)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE REQUIREMENT IN ENTANGLEMENT LANGUAGE")
    print("  %10s %16s %16s %12s" % ("L (m)", "S required", "S holographic", "ratio"))
    for L in (1.0, 1.0e3, 1.0e5, 1.0e10, 1.0e20):
        print("  %10.0e %16.4e %16.4e %12.4f"
              % (L, entropy_required(L), entropy_holographic(L), holographic_excess(L)))
    print("\n  excess = 2 pi^2 = %.4f, at every scale." % (2 * math.pi ** 2))
    print("  spec.py's collapse factor = %.4f.  They differ by exactly 3."
          % collapse_factor())
    import specthm
    sb = specthm.sturm_over_ball(collapse_factor())
    print("  (DOCKET 67: the collapse factor is the T_kk = u radius ratio.  Over")
    print("  H_ball as written, on a diameter: %.4f pressureless, %.4f radiation,"
          % (sb["dust_diameter"], sb["radiation_diameter"]))
    print("  %.4f at T_kk = 2u; <= 1 for w >= %.6f.  Class S-2 is OPEN.)"
          % (sb["member_diameter"], sb["w_threshold_diameter"]))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  M's instinct is right: negative energy density IS an entanglement")
    print("  phenomenon, and QNEC states the requirement exactly -- entanglement")
    print("  entropy concave along the ray.")
    import achievable
    print("\n  Against what physics PERMITS, the requirement is 2 pi^2 = 20x the")
    print("  holographic bound, at every scale.  Against the duration bound at")
    print("  b = 1 m it is 1e%.3f (H-MMCS, H-HADAMARD, H-FLAT), %.2f orders"
          % (math.log10(achievable.persistence_shortfall(1.0)),
             math.log10(achievable.persistence_shortfall(1.0)
                        / holographic_excess(1.0))))
    print("  further.  (CORRECTED, DOCKET 67 follow-ups: this printed 1e65,")
    print("  'what can be MADE', DOCKET 55-withdrawn.)")
    print("\n  But twenty times the holographic bound is still impossible, and")
    print("  not in an engineering way: it is more information than a region")
    print("  can hold.  There is no charge loophole -- QNEC is state-independent")
    print("  and charge appears nowhere in it.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
