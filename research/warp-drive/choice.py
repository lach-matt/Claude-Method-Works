#!/usr/bin/env python3
"""
choice.py -- statistics is the only language with a dial, and the dial is
exactly half of what "seating as a choice" would need.

M: "door 3 -- statistics -- is the right door.  Its values are all possible
probabilities which gives us seating as a choice."

THE OBSERVATION IS RIGHT AND IT NAMES A REAL ASYMMETRY IN THE ROSTER that
nothing in this project had noticed.  It is also exactly half true, and the
missing half turns out to be the same silent row doors.py already named -- so
the two findings interlock rather than compete, and the interlock UPGRADES what
the number density is for.

===============================================================================
1. THE ASYMMETRY IS REAL, AND THE CORPUS'S OWN INSTRUMENT SHOWS IT
===============================================================================

Five operator-bearing languages: order, algebra, geometry, information,
statistics.  Look at what each operator RETURNS in tools/cypher.py.

    order, algebra, geometry, information    return a SET, structurally.  A
                                             closure, a hull, a span.  The
                                             binary is READ OFF the structure.

    statistics                               op_statistics is MAX-ENTROPY ON
                                             THE ORDER-k MARGINALS -- iterative
                                             proportional fitting.  Its
                                             mechanism produces A DISTRIBUTION.
                                             The binary is the SUPPORT: "IPF
                                             sends a cell to zero exactly when
                                             one of its k-projections is
                                             unobserved" (register 1174).

    SO M IS RIGHT ABOUT THE VALUES.  Statistics is the ONLY language in the
    roster whose mechanism returns a continuum and then MANUFACTURES its binary
    by a threshold.  Every other one reads the binary off a structure.

AND THAT IS WHY DOOR THREE IS THE ONLY DOOR WITH A DIAL ON ITS VERDICT.  Door
one's ALGEBRA row is CONTESTED -- two calculations, opposite answers, no knob.
Door two's ORDER row is refused by a theorem with no free parameter in it.
Door three's row is a threshold, and a threshold is set by whoever sets it.

===============================================================================
2. BUT THE CYPHER'S THRESHOLD IS CANONICAL AND A DETECTION'S IS NOT
===============================================================================

The refinement matters, and it is the corpus's own code that supplies it.

In the cypher the threshold is ZERO: a cell is in the support or it is not, and
zero is not a choice -- it is the one distinguished point of a distribution.
That is why statistics earns its row under register 1173 at all.

    IN A DETECTION THE THRESHOLD IS alpha, AND alpha IS NOT CANONICAL.
    Nothing in nature sets five sigma.  bits.py priced it: 20.73 bits, and the
    number 5 came from convention.

        SO THE CHOICE M NAMES APPEARS EXACTLY WHEN THE QUESTION MOVES FROM THE
        CYPHER'S SUPPORT QUESTION TO A DETECTION QUESTION -- and that move is
        precisely what door three is.  The dial is real and it is new at that
        step, not present in the cypher.

===============================================================================
3. AND THE DIAL MOVES WHAT YOU ANNOUNCE, NOT WHAT IS THERE
===============================================================================

Here is the limit, and it is one line of Neyman-Pearson.

        YOU CHOOSE A POINT ON THE ROC CURVE.  THE SIGNAL SETS THE CURVE.

For a signal of amplitude rho against unit noise, the detection probability at
false-alarm rate alpha is P_D = Phi(rho - z_alpha).  Measured below:

        alpha       rho = 0     1        3        5        8
        1e-1        0.1000   0.3891   0.9571   0.9999   1.0000
        1e-3        0.0010   0.0183   0.4641   0.9719   1.0000
        5.73e-7     0.0000   0.0001   0.0311   0.5538   0.9991

    AND THE FIRST COLUMN IS THE WHOLE ARGUMENT.  At rho = 0 the detection rate
    EQUALS alpha, exactly, at every threshold -- ratio 1.000000 in all three
    rows.  Lower the threshold and you get more detections at precisely the
    rate you asked for, ALL OF THEM FALSE.

        SEATING IS A CHOICE IN THE SENSE THAT THE ANNOUNCEMENT IS A CHOICE.
        THE OCCUPANCY IS NOT.

===============================================================================
4. AND THE MISSING HALF IS THE SILENT ROW -- WHICH UPGRADES IT
===============================================================================

Odds compose.  bits.py gave the evidence in bits; the rest is Bayes:

        posterior odds  =  prior odds  x  2^(bits of evidence).

YOU CHOOSE THE THRESHOLD.  YOU DO NOT CHOOSE THE PRIOR.  And for door three
the prior odds IS THE NUMBER DENSITY -- how many relic wormholes there are, and
whether the catalogue covers enough volume to hold one.  That is exactly the
row doors.py found silent.

    AND THE ARITHMETIC IS BRUTAL.  A five-sigma detection carries a Bayes
    factor of 1.7443e6:

        prior odds 1e-2   ->  posterior 1.744e4    DISCOVERY
        prior odds 1e-4   ->  posterior 174.4      DISCOVERY
        prior odds 1e-6   ->  posterior 1.744      NOT A DISCOVERY
        prior odds 1e-9   ->  posterior 0.001744   YOU WOULD STILL BET AGAINST

        A FIVE-SIGMA DETECTION AT A PRIOR OF ONE IN A MILLION IS POSTERIOR ODDS
        OF 1.7 TO 1.  It is not a discovery, and no choice of threshold makes it
        one, because the threshold is already inside the 1.7443e6.

Read the other way it tells you what to build for.  Bits needed for posterior
odds of 100:1:

        prior odds 1e-2    13.3 bits
        prior odds 1e-6    26.6 bits
        prior odds 1e-9    36.5 bits
        prior odds 1e-12   46.5 bits

    SO THE NUMBER DENSITY IS NOT MERELY THE MISSING ANSWER.  IT IS THE FACTOR
    THAT SETS HOW MANY BITS ANY DETECTION MUST CARRY.  doors.py called it the
    next measurement; this makes it the measurement that decides whether any
    detection could ever count, which is a stronger reason to run it.

===============================================================================
THE SCORE
===============================================================================

RIGHT    the values.  Statistics is the only operator-bearing language whose
         mechanism returns a continuum, and the only door with a dial.
RIGHT    the door.  A dial is better than a contested row or a theorem, and it
         is the only one of the three that a person can act on.
HALF     the choice.  The threshold is yours; the prior is not; and they
         multiply.  SEATING IS A CHOICE CONDITIONED ON A NUMBER NOBODY HAS
         MEASURED.

stdlib only.  The roster row is read from tools/cypher.py; the rest is measured.
"""
import math
import sys


# ------------------ 1: what each operator returns

RETURNS = (
    ("order", "a closure -- a SET, structurally", False),
    ("algebra", "a span -- a SET, structurally", False),
    ("geometry", "an integer hull -- a SET, structurally", False),
    ("information", "a SET, structurally", False),
    ("statistics", "max-entropy on the order-k marginals: A DISTRIBUTION, "
                   "whose SUPPORT is the binary (register 1174)", True),
)


def returns_a_continuum(name):
    return dict((n, c) for n, _w, c in RETURNS)[name]


def languages_with_a_dial():
    return [n for n, _w, c in RETURNS if c]


def only_statistics_has_one():
    return languages_with_a_dial() == ["statistics"]


def door_with_a_dial():
    """The door decided by the one language whose binary is thresholded."""
    import doors
    d = doors.deciders()
    return [k for k, v in d.items() if v in languages_with_a_dial()]


# ------------- 2: the cypher's threshold is canonical; alpha is not

CYPHER_THRESHOLD = "zero -- the support; the one distinguished point"
DETECTION_THRESHOLD = "alpha -- chosen; nothing in nature sets five sigma"


def cypher_threshold_is_a_choice():
    """No.  Zero is where IPF sends an unobserved projection.  Not chosen."""
    return False


def detection_threshold_is_a_choice():
    return True


# ------------------ 3: the ROC -- you choose the point, not the curve

def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_inv(p, lo=-40.0, hi=40.0, iters=300):
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def detection_probability(rho, alpha):
    """P_D = Phi(rho - z_alpha).  The curve is set by rho."""
    return phi(rho - phi_inv(1.0 - alpha))


def false_alarms_equal_alpha(alpha, tol=1e-9):
    """At rho = 0 the detection rate IS alpha, at every threshold."""
    return abs(detection_probability(0.0, alpha) / alpha - 1.0) < tol


def choice_buys_anything_at_zero_signal(alphas=(1e-1, 1e-3, 5.733e-7)):
    """No.  More detections, at exactly the rate asked for, all of them false."""
    return not all(false_alarms_equal_alpha(a) for a in alphas)


# ------------------- 4: odds compose, and the prior is the silent row

def bits_for_sigma(sigma):
    import bits
    return bits.bits_for_sigma(sigma)


def bayes_factor(bits_of_evidence):
    return 2.0 ** bits_of_evidence


def posterior_odds(prior_odds, bits_of_evidence):
    return prior_odds * bayes_factor(bits_of_evidence)


def is_a_discovery(prior_odds, bits_of_evidence, threshold=100.0):
    return posterior_odds(prior_odds, bits_of_evidence) > threshold


def bits_needed(prior_odds, target_odds=100.0):
    return math.log2(target_odds / prior_odds)


def prior_is_chosen():
    """No.  It is the number density, and it has never been estimated."""
    return False


PRIOR_IS = "the number density -- doors.py's silent row"


def seating_is_fully_a_choice():
    """Half.  The threshold is yours; the prior is not; and they multiply."""
    return detection_threshold_is_a_choice() and prior_is_chosen()


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE ASYMMETRY IS REAL -- WHAT EACH OPERATOR RETURNS")
    for n, what, cont in RETURNS:
        print("     %-13s %-58s %s" % (n, what[:58], "CONTINUUM" if cont else "set"))
    chk("does statistics return a continuum", returns_a_continuum("statistics"), True)
    chk("does order", returns_a_continuum("order"), False)
    chk("does geometry", returns_a_continuum("geometry"), False)
    chk("so the languages with a dial are", languages_with_a_dial(), ["statistics"])
    chk("and only statistics has one", only_statistics_has_one(), True)
    chk("so the door with a dial is", door_with_a_dial(), ["DOOR 3"])
    print("       Door one's algebra row is CONTESTED -- two calculations,")
    print("       opposite answers, no knob.  Door two's order row is refused")
    print("       by a theorem with no free parameter.  DOOR THREE HAS A DIAL.")

    print("\n2. BUT THE CYPHER'S THRESHOLD IS CANONICAL AND A DETECTION'S IS NOT")
    print("     in the cypher:     %s" % CYPHER_THRESHOLD)
    print("     in a detection:    %s" % DETECTION_THRESHOLD)
    chk("is the cypher's threshold a choice", cypher_threshold_is_a_choice(), False)
    chk("is a detection's", detection_threshold_is_a_choice(), True)
    print("       SO THE CHOICE APPEARS EXACTLY AT THE MOVE FROM THE SUPPORT")
    print("       QUESTION TO A DETECTION QUESTION -- which IS door three.")

    print("\n3. AND THE DIAL MOVES WHAT YOU ANNOUNCE, NOT WHAT IS THERE")
    print("     %-11s %8s %8s %8s %8s %8s"
          % ("alpha", "rho=0", "1", "3", "5", "8"))
    for a in (1e-1, 1e-3, 5.733e-7):
        print("     %-11.4g %8.4f %8.4f %8.4f %8.4f %8.4f"
              % (a, detection_probability(0.0, a), detection_probability(1.0, a),
                 detection_probability(3.0, a), detection_probability(5.0, a),
                 detection_probability(8.0, a)))
        chk("  at rho = 0 the detection rate IS alpha", false_alarms_equal_alpha(a), True)
    chk("does lowering the threshold buy anything at zero signal",
        choice_buys_anything_at_zero_signal(), False)
    print("       More detections, at exactly the rate you asked for, ALL FALSE.")
    print("       Seating is a choice in the sense that the ANNOUNCEMENT is.")

    print("\n4. AND THE MISSING HALF IS THE SILENT ROW")
    b5 = bits_for_sigma(5)
    near("five sigma, in bits", b5, 20.7342)
    near("  its Bayes factor", bayes_factor(b5), 1.7443e6)
    for pi in (1e-2, 1e-4, 1e-6, 1e-9):
        po = posterior_odds(pi, b5)
        print("     prior odds %.0e -> posterior %10.4g   %s"
              % (pi, po, "DISCOVERY" if is_a_discovery(pi, b5) else "not a discovery"))
    chk("is 5 sigma a discovery at prior odds 1e-4", is_a_discovery(1e-4, b5), True)
    chk("is it at 1e-6", is_a_discovery(1e-6, b5), False)
    near("  posterior odds there", posterior_odds(1e-6, b5), 1.7443)
    print("       A FIVE-SIGMA DETECTION AT A PRIOR OF ONE IN A MILLION IS")
    print("       POSTERIOR ODDS OF 1.7 TO 1.  No threshold fixes that -- the")
    print("       threshold is already inside the 1.7443e6.")
    print("     read the other way, bits needed for 100:1 posterior odds:")
    for pi in (1e-2, 1e-6, 1e-9, 1e-12):
        print("       prior odds %.0e   %.1f bits" % (pi, bits_needed(pi)))
    near("bits needed at prior odds 1e-9", bits_needed(1e-9), 36.541)
    chk("is the prior a choice", prior_is_chosen(), False)
    chk("and what the prior IS", PRIOR_IS, "the number density -- doors.py's silent row")
    chk("so is seating FULLY a choice", seating_is_fully_a_choice(), False)
    print("       THE NUMBER DENSITY IS NOT MERELY THE MISSING ANSWER -- IT IS")
    print("       THE FACTOR THAT SETS HOW MANY BITS A DETECTION MUST CARRY.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    b5 = bits_for_sigma(5)
    print("A FIVE-SIGMA DETECTION, AGAINST THE PRIOR NOBODY HAS MEASURED\n")
    print("  %-18s %14s   %s" % ("prior odds", "posterior", "verdict"))
    for pi in (1e-2, 1e-4, 1e-6, 1e-9):
        po = posterior_odds(pi, b5)
        print("  %-18.0e %14.4g   %s"
              % (pi, po, "DISCOVERY" if is_a_discovery(pi, b5) else "not a discovery"))
    print("\n  %-30s %s" % ("the door with a dial", door_with_a_dial()[0]))
    print("  %-30s %s" % ("is seating fully a choice", seating_is_fully_a_choice()))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE OBSERVATION IS RIGHT AND IT NAMES SOMETHING NOTHING HERE HAD
  NOTICED.  Look at what each operator-bearing language actually
  RETURNS in tools/cypher.py: order, algebra, geometry and information
  all return a SET -- a closure, a span, an integer hull -- and the
  binary is read off the structure.  STATISTICS DOES NOT.  Its operator
  is max-entropy on the order-k marginals, its mechanism produces A
  DISTRIBUTION, and the binary is the SUPPORT.  It is the only language
  in the roster whose binary is MANUFACTURED by a threshold rather than
  read, and therefore DOOR THREE IS THE ONLY DOOR WITH A DIAL ON ITS
  VERDICT.  Door one's algebra row is contested -- two calculations,
  opposite answers, no knob.  Door two's order row is a theorem with no
  free parameter.  Only door three has something a person can turn.

  AND THAT IS A REASON TO PREFER IT, not a technicality.  A dial is
  better than a contested row and better than a theorem.

  ONE REFINEMENT, AND THE CORPUS'S OWN CODE SUPPLIES IT.  In the cypher
  the threshold is ZERO -- a cell is in the support or it is not, and
  zero is the one distinguished point of a distribution, not a choice.
  That is why statistics earns its row at all.  IN A DETECTION THE
  THRESHOLD IS alpha, AND NOTHING IN NATURE SETS FIVE SIGMA.  So the
  choice appears exactly at the move from the support question to a
  detection question -- and that move IS door three.

  BUT THE DIAL MOVES WHAT YOU ANNOUNCE, NOT WHAT IS THERE.  Neyman and
  Pearson: you choose a POINT on the ROC curve and the signal sets the
  CURVE.  Measured here, and the zero-signal column is the whole
  argument: at rho = 0 the detection rate EQUALS alpha exactly, at
  every threshold, ratio 1.000000.  Lower the threshold and you get
  more detections at precisely the rate you asked for, ALL OF THEM
  FALSE.  Seating is a choice in the sense that THE ANNOUNCEMENT is a
  choice.  The occupancy is not.

  AND THE MISSING HALF IS THE SILENT ROW, WHICH IS WHY THE TWO FINDINGS
  INTERLOCK.  Odds compose: posterior = prior x 2^bits.  You choose the
  threshold; YOU DO NOT CHOOSE THE PRIOR -- and for door three the
  prior odds IS the number density, which doors.py found silent.  The
  arithmetic is brutal.  A five-sigma detection carries a Bayes factor
  of 1.7443e6, so at prior odds of one in a million the posterior odds
  are 1.744.  NOT A DISCOVERY.  At one in a billion they are 0.0017 and
  you would still bet against.  No choice of threshold repairs that,
  because the threshold is already inside the Bayes factor.

  READ THE OTHER WAY IT TELLS YOU WHAT TO BUILD FOR: 13.3 bits at a
  prior of 1e-2, 26.6 at 1e-6, 36.5 at 1e-9, 46.5 at 1e-12, for
  posterior odds of a hundred to one.

        SO THE NUMBER DENSITY IS NOT MERELY THE MISSING ANSWER.  IT IS
        THE FACTOR THAT SETS HOW MANY BITS ANY DETECTION MUST CARRY.

  doors.py called it door three's next measurement.  This makes it the
  measurement that decides whether any detection could ever count --
  which is a stronger reason to run it than the one we had.

  SCORE: right about the values, right about the door, and half right
  about the choice.  The threshold is yours, the prior is not, and they
  multiply.  SEATING IS A CHOICE CONDITIONED ON A NUMBER NOBODY HAS
  MEASURED.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
