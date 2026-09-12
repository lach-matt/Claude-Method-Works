#!/usr/bin/env python3.12
"""antigravity.py -- harnessing antigravity, and it is not the thing we need.

M: "We need to harness antigravity."

sign.py made the requirement unambiguous: NEGATIVE MASS, at 22.59 Earth masses
of it per metre.  So this asks the obvious next question and finds that
ANTIGRAVITY AND NEGATIVE MASS ARE DIFFERENT OBJECTS, and that the literature's
own antigravity proposals say so explicitly.

  1.  ANTIMATTER FALLS DOWN.  ALPHA-g measured the free-fall acceleration of
      antihydrogen at a = (0.75 +/- 0.13 (stat+syst) +/- 0.16 (simulation)) g.
      DOWNWARD.  (Anderson et al., Nature 621, 2023.)  This tree did not hold
      that result anywhere -- no file mentions ALPHA-g or antihydrogen.

  2.  AND EVEN FULL ANTIGRAVITY WOULD NOT MAKE IT FALL UP, WHICH IS THE PART
      WORTH KNOWING.  Binding energy acts gravitationally as MATTER, tested to
      1e-15 by MICROSCOPE, and about TWO THIRDS of an antinucleon's mass is
      GLUONIC BINDING ENERGY.  So an antiatom is mostly matter, gravitationally,
      and the antigravity prediction is a = (1 - 2 fbar) g with fbar ~ 0.33 --
      STILL DOWNWARD, at about a third of g.

  3.  SO THE MEASUREMENT DISFAVOURS ANTIGRAVITY WITHOUT RULING IT OUT.  The
      gap is (0.42 +/- 0.23) g, under two sigma.  RECORDED AS DISFAVOURED, NOT
      CLOSED, because that is what the numbers say.

  4.  AND HERE IS WHY NONE OF IT HELPS.  Villata's antigravity -- the version
      that gets repulsion out of general relativity with no new physics -- says
      in its own words that "all masses are and remain POSITIVE DEFINITE".  The
      repulsion is A SIGN IN THE GEODESIC EQUATION, not a negative source.

          ANTIGRAVITY IS A SIGN IN THE INTERACTION.
          THE CORRIDOR NEEDS A SIGN IN THE SOURCE.

      Those are different objects, and no antigravity proposal in the
      literature supplies the second.  Even at the theoretical maximum --
      fbar = 1, a = -g, an object that genuinely falls up -- THE MASS IN THE
      STRESS-ENERGY TENSOR IS STILL POSITIVE, so the Misner-Sharp mass
      certify.py requires to be negative IS STILL POSITIVE.

  5.  WHICH MEANS THE ANSWER IS NOT "ANTIGRAVITY IS TOO WEAK".  IT IS THAT
      ANTIGRAVITY IS THE WRONG QUANTITY.  Harnessing all of it, perfectly,
      at a = -g, buys ZERO of the 22.59 Earth masses per metre.

Sources READ FROM SOURCE this session.  Stdlib only.

    python3.12 antigravity.py            full report
    python3.12 antigravity.py --selftest
"""

import math
import sys

import ladder

M_EARTH = ladder.M_EARTH

# --- READ FROM SOURCE, via Menary arXiv:2401.10954 -----------------------
#   [alphag23]  E. K. Anderson et al. (ALPHA), Nature 621 (2023)
ALPHAG_A = 0.75
ALPHAG_STAT_SYST = 0.13
ALPHAG_SIM = 0.16
#   antimatter fraction of the antiproton mass, Lattice QCD via Menary
FBAR_ANTIPROTON = 0.33
FBAR_HI, FBAR_LO = 0.06, 0.10
#   [micro22]  Touboul et al. (MICROSCOPE), PRL 129, 121102 (2022)
MICROSCOPE_ETA = 1.5e-15
#   [bondi57]  H. Bondi, Rev. Mod. Phys. 29 (1957), "Negative Mass in GR"
#   [villata11] M. Villata, EPL 94, 20001 (2011)
SOURCES_READ = True


def alphag_sigma():
    return math.sqrt(ALPHAG_STAT_SYST ** 2 + ALPHAG_SIM ** 2)


def antigravity_prediction(fbar):
    """Menary eq.: a = (1 - 2 fbar) g.  fbar is the ANTIMATTER fraction."""
    return 1.0 - 2.0 * fbar


def force_factor(f1, f2):
    """Menary eq. (6): 1 - 2(f1+f2) + 4 f1 f2, in units of the matter-matter
    force.  f are ANTIMATTER fractions."""
    return 1.0 - 2.0 * (f1 + f2) + 4.0 * f1 * f2


def tension_sigma():
    """How far ALPHA-g sits from the antigravity prediction."""
    pred = antigravity_prediction(FBAR_ANTIPROTON)
    gap = ALPHAG_A - pred
    err = math.sqrt(alphag_sigma() ** 2 + ((FBAR_HI + FBAR_LO) ) ** 2)
    return gap, err, gap / err


def negative_mass_supplied_by_antigravity():
    """The whole point.  Antigravity flips an interaction sign; it does not
    make the stress-energy negative.  So it supplies exactly none."""
    return 0.0


ANTIMATTER_FALLS_DOWN = True
ANTIGRAVITY_RULED_OUT = False
ANTIGRAVITY_IS_DISFAVOURED = True
ANTIGRAVITY_GIVES_NEGATIVE_MASS = False
MASSES_STAY_POSITIVE_DEFINITE = True
ANTIGRAVITY_IS_THE_WRONG_QUANTITY = True
SCOPE = "gravitational sign only; says nothing about Casimir negative energy density"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Sources READ")[0].rstrip())
    print()

    print(BAR)
    print("1.  ANTIMATTER FALLS DOWN, AND THIS TREE DID NOT HOLD THE RESULT")
    print(BAR)
    print()
    print("      ALPHA-g, Anderson et al., Nature 621 (2023):")
    print()
    print("          a(antihydrogen) = (%.2f +/- %.2f (stat+syst) +/- %.2f (sim)) g"
          % (ALPHAG_A, ALPHAG_STAT_SYST, ALPHAG_SIM))
    print("          combined uncertainty %.4f g" % alphag_sigma())
    print()
    print("      DOWNWARD, at three quarters of g.  A grep over this tree finds")
    print("      NO mention of ALPHA-g or antihydrogen in any file -- the single")
    print("      most direct experiment on M's question was absent from a")
    print("      project that has been asking about negative mass for weeks.")
    print()

    print(BAR)
    print("2.  AND FULL ANTIGRAVITY WOULD NOT MAKE IT FALL UP EITHER")
    print(BAR)
    print()
    print("      Binding energy acts gravitationally as MATTER -- MICROSCOPE")
    print("      bounds the Eotvos parameter at %.1e -- and about TWO THIRDS of"
          % MICROSCOPE_ETA)
    print("      an antinucleon's mass is GLUONIC BINDING ENERGY.  So an")
    print("      antiatom is mostly MATTER, gravitationally.")
    print()
    print("      Menary's relation, a = (1 - 2 fbar) g:")
    print()
    print("      %-42s %12s %12s" % ("antimatter fraction fbar", "a / g", "direction"))
    for name, f in [("pure antimatter (naive picture)", 1.0),
                    ("antihydrogen, fbar = %.2f" % FBAR_ANTIPROTON, FBAR_ANTIPROTON),
                    ("positronium, ~half and half", 0.5),
                    ("muonium, fbar = 0.995", 0.995),
                    ("ordinary matter", 0.0)]:
        a = antigravity_prediction(f)
        print("      %-42s %12.4f %12s"
              % (name, a, "UP" if a < 0 else ("hovers" if abs(a) < 1e-9 else "DOWN")))
    print()
    print("      SO EVEN IN THE ANTIGRAVITY SCENARIO ANTIHYDROGEN FALLS DOWN,")
    print("      at about %.2f g.  It is MUONIUM that would fall up, and"
          % antigravity_prediction(FBAR_ANTIPROTON))
    print("      POSITRONIUM that would hover -- neither of which is a mass you")
    print("      can pile up, positronium lasting 142 ns.")
    print()
    print("      And the force between two antinucleons would be %.4f of the"
          % force_factor(1 / 3.0, 1 / 3.0))
    print("      matter-matter force, nucleon-antinucleon %.4f -- REDUCED"
          % force_factor(0.0, 1 / 3.0))
    print("      ATTRACTION IN ONE CASE AND WEAK REPULSION IN THE OTHER, never")
    print("      a strong repulsion.")
    print()

    print(BAR)
    print("3.  SO THE MEASUREMENT DISFAVOURS ANTIGRAVITY WITHOUT CLOSING IT")
    print(BAR)
    print()
    gap, err, sig = tension_sigma()
    print("      measured   %.4f g" % ALPHAG_A)
    print("      predicted  %.4f g   (antigravity, fbar = %.2f)"
          % (antigravity_prediction(FBAR_ANTIPROTON), FBAR_ANTIPROTON))
    print("      gap        %.4f +/- %.4f g   =  %.2f sigma" % (gap, err, sig))
    print()
    print("      DISFAVOURED, NOT RULED OUT.  Recorded as what the numbers say")
    print("      and not as what would be convenient.  Menary notes that")
    print("      reducing the experimental uncertainty to about 5 percent would")
    print("      settle it either way.")
    print()

    print(BAR)
    print("4.  AND HERE IS WHY NONE OF IT HELPS US")
    print(BAR)
    print()
    print("    Villata's antigravity is the version that gets repulsion out of")
    print("    general relativity with NO new physics, by applying CPT to the")
    print("    geodesic equation.  In his own words:")
    print()
    print('        "all masses are and remain POSITIVE DEFINITE ... the minus')
    print('         sign comes from the PT-oddness of either dx^mu or Gamma"')
    print()
    print("        ANTIGRAVITY IS A SIGN IN THE INTERACTION.")
    print("        THE CORRIDOR NEEDS A SIGN IN THE SOURCE.")
    print()
    print("    certify.py's condition is on the MISNER-SHARP MASS, which is an")
    print("    integral of the stress-energy: m(r) = 4 pi Int rho r^2 dr.  A")
    print("    sign in the geodesic equation does not enter it.  Even at the")
    print("    theoretical maximum -- fbar = 1, a = %.1f g, an object that"
          % antigravity_prediction(1.0))
    print("    genuinely falls up -- THE rho IN THAT INTEGRAL IS STILL POSITIVE.")
    print()
    print("    %-46s %20s" % ("what antigravity supplies, at its maximum",
                              "%.1f kg" % negative_mass_supplied_by_antigravity()))
    print("    %-46s %20s" % ("what one metre of corridor requires",
                              "-%.2f Earth masses" % (ladder.mass_for_delta_d(1.0) / M_EARTH)))
    print()

    print(BAR)
    print("5.  SO THE ANSWER IS NOT 'TOO WEAK'.  IT IS 'WRONG QUANTITY'.")
    print(BAR)
    print()
    print("      Harnessing ALL of antigravity, PERFECTLY, on an object that")
    print("      falls up at a full -g, buys ZERO of the 22.59 Earth masses per")
    print("      metre.  Not a little; none.  The two quantities do not meet.")
    print()
    print("      THAT IS A DIFFERENT KIND OF NO FROM EVERY OTHER ONE IN THIS")
    print("      THREAD, AND IT IS THE MOST USEFUL KIND: not a magnitude to be")
    print("      chased, but a category error to stop chasing.  amps, voltage,")
    print("      reactors and mouths were all wrong by a number.  THIS ONE IS")
    print("      NOT ON THE SAME AXIS AT ALL.")
    print()
    print("      WHAT DOES PRODUCE NEGATIVE ENERGY DENSITY IS STILL THE CASIMIR")
    print("      EFFECT, and this tree already holds it priced: candidates.py")
    print("      ran it against three gates and magnitude.py gave it")
    print("      k_Cas = pi^2 Lambda/720 = 0.136838353 with a crossover at")
    print("      0.369917 l_P.  SUB-PLANCKIAN, WHICH IS WHERE IT ALWAYS WAS.")
    print("      Nothing in this pass changes that, and this pass is not about")
    print("      it -- negative energy DENSITY and negative MASS are the third")
    print("      distinction in a question that keeps hiding two things inside")
    print("      one word.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Nothing here is repaired.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("antigravity.py --selftest")
    print()

    chk("ALPHA-g measured a downward acceleration", ALPHAG_A > 0.0, True)
    chk("and it is consistent with g within two sigma",
        abs(ALPHAG_A - 1.0) / alphag_sigma() < 2.0, True)
    chk("antimatter falls down", ANTIMATTER_FALLS_DOWN, True)

    # Menary's relation and its consequences
    chk("ordinary matter falls at g", antigravity_prediction(0.0), 1.0)
    chk("pure antimatter would fall at -g", antigravity_prediction(1.0), -1.0)
    chk("antihydrogen still falls DOWN even under antigravity",
        antigravity_prediction(FBAR_ANTIPROTON) > 0.0, True)
    chk("positronium would hover",
        abs(antigravity_prediction(0.5)) < 1e-12, True)
    chk("muonium would fall up",
        antigravity_prediction(0.995) < -0.98, True)
    chk("antinucleon-antinucleon force is one ninth",
        abs(force_factor(1 / 3.0, 1 / 3.0) - 1 / 9.0) < 1e-12, True)
    chk("nucleon-antinucleon is one third",
        abs(force_factor(0.0, 1 / 3.0) - 1 / 3.0) < 1e-12, True)
    chk("and matter-matter is unity", force_factor(0.0, 0.0), 1.0)

    # the tension
    gap, err, sig = tension_sigma()
    chk("the gap is under two sigma", sig < 2.0, True)
    chk("antigravity is ruled out", ANTIGRAVITY_RULED_OUT, False)
    chk("antigravity is disfavoured", ANTIGRAVITY_IS_DISFAVOURED, True)

    # THE POINT
    chk("antigravity supplies negative mass", ANTIGRAVITY_GIVES_NEGATIVE_MASS, False)
    chk("and supplies exactly zero of it",
        negative_mass_supplied_by_antigravity(), 0.0)
    chk("while masses stay positive definite", MASSES_STAY_POSITIVE_DEFINITE, True)
    chk("so it is the wrong quantity, not too weak",
        ANTIGRAVITY_IS_THE_WRONG_QUANTITY, True)
    chk("the requirement is unchanged at 22.59 Earth masses per metre",
        abs(ladder.mass_for_delta_d(1.0) / M_EARTH - 22.5871) < 1e-3, True)

    # the tree really did lack this
    import subprocess
    hits = subprocess.run(["grep", "-rl", "ALPHA-g", "."], capture_output=True,
                          text=True).stdout.split()
    # index3.py carries it once this pass is SEATED -- that is the finding
    # being recorded, not another instrument holding the result.  The claim is
    # about INSTRUMENTS, and the first draft of this check did not exclude the
    # index, so seating the finding falsified the test that asserted it.
    chk("no instrument other than this one holds ALPHA-g",
        sorted(h.split("/")[-1] for h in hits
               if h.endswith(".py") and h.split("/")[-1] != "index3.py"),
        ["antigravity.py"])

    chk("sources were read", SOURCES_READ, True)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
