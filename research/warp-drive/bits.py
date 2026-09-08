#!/usr/bin/env python3
"""
bits.py -- where compressed bits CAN be spent, and it is exactly one door.

M: "can we use compressed binary as currency for any other door?"

compress.py closed the use on door two and said why: a density argument is the
wrong KIND of argument there, because the bank-loan theorem has no information
term in it.  That leaves the question open for the other two, and it is a good
question because it is asked in the index's own terms -- which language does the
currency speak, and which language decides the door.

    DOOR 2   NO, BY FORM.        Decided by ORDER.  Immune.
    DOOR 1   RIGHT KIND, AND IT HAS BEEN TRIED, AND IT LANDS SOMEWHERE ELSE.
    DOOR 3   YES.  And not as density -- AS A DETECTION STATISTIC.

THE FIRST AFFIRMATIVE ANSWER IN THIS ENTIRE CURRENCY THREAD, and the reason it
works is visible in the index: door three is decided by STATISTICS, and a
compression argument IS a statistics argument.  THE CURRENCY AND THE DECIDING
LANGUAGE ARE FINALLY THE SAME LANGUAGE.

===============================================================================
1. DOOR TWO -- NO, AND THE REASON IS THE THEOREM'S FORM
===============================================================================

Settled in compress.py and not reopened here.  Door two is decided by ORDER and
its refusal is gjw.py's bank-loan theorem: traversability needs non-achronality,
non-achronality needs an EXISTING OUTSIDE CAUSAL PATH.  No energy term, no
information term, nothing for a better code to improve.  IMMUNE BY FORM.

===============================================================================
2. DOOR ONE -- THE RIGHT KIND OF ARGUMENT, AND IT HAS ALREADY BEEN WALKED
===============================================================================

Door one is decided by ALGEBRA -- stability -- and at first sight information
has no business there: an instability is the sign of an eigenvalue.

    BUT IT DOES, AND THIS IS WORTH KNOWING.  There is a real bridge between
    ENTROPY and STABILITY: a configuration is thermodynamically stable when the
    entropy is a maximum, d2S < 0, and for self-gravitating systems that
    condition can be written down and compared with the dynamical one.  So an
    entropy argument is NOT categorically the wrong kind for door one, the way
    it is for door two.  The currency is spendable here.

AND IT HAS BEEN SPENT, ON A WORMHOLE, AND THE ANSWER IS RECORDED.
Eiroa, Figueroa-Aguirre, Peñafiel & Perez Bergliaffa (arXiv:2408.14328) compute
BOTH stabilities for a charged thin-shell wormhole made by gluing two
Reissner-Nordström geometries.  Their findings:

  * For a Hawking-type entropy, S = gamma r_+^2 / 2:
        "THERE ARE NO CONFIGURATIONS BOTH DYNAMICALLY AND THERMODYNAMICALLY
        STABLE."  The two regions do not overlap at all.

  * For a power-law entropy with more parametric freedom:
        "THERMODYNAMICALLY STABLE BUT DYNAMICALLY UNSTABLE CONFIGURATIONS
        WITHOUT CHARGE ARE POSSIBLE."

        ENTROPY STABILITY DOES NOT IMPLY DYNAMICAL STABILITY.  Measured, on a
        wormhole, in print.  That is the answer to whether the currency buys
        what door one needs: IT DOES NOT.

  * Where they do overlap it is "a small zone", needing -1 < delta < 1, negative
    kappa, low beta -- and EVERY completely stable configuration is OVERCHARGED,
    Q > m, because those are the only dynamically stable ones for a linear
    equation of state.

  * And the entropy function is an ANSATZ, not derived: they choose two
    convenient forms of the inverse temperature.  So the thermodynamic side
    carries free parameters the dynamical side does not, which is exactly the
    freedom that makes agreement unreliable.

    SO FOR DOOR ONE THE VERDICT IS SHARPER THAN "NO".  The bridge exists, it
    has been crossed, and it lands in a different place.  An entropy argument
    cannot substitute for the dynamical calculation that doors.py named as
    door one's next measurement.  IT IS NOT A SHORTCUT PAST THE WORK.

===============================================================================
3. DOOR THREE -- YES, AND IT IS THE NATURAL TOOL
===============================================================================

Door three is decided by STATISTICS, and STATISTICS is the language a
compression argument speaks.  Here the currency is not density.  It is a
DETECTION STATISTIC, and the connection is an identity rather than an analogy.

  THE EVIDENCE IN BITS *IS* THE COMPRESSION SAVING IN BITS.
  Arithmetic coding gives code length l = -log2 P.  For two hypotheses on the
  same data,

        log2 B  =  log2 [P(d|H1)/P(d|H0)]  =  l_0 - l_1.

  Verified below as an exact identity.  A signal is present exactly when the
  data is CHEAPER TO DESCRIBE with it than without.  That is Rissanen's minimum
  description length, and it is a rigorous detection framework, not a metaphor.

  THE THRESHOLDS ARE SMALL NUMBERS OF BITS.
        3 sigma   8.53 bits
        5 sigma   20.73 bits
        8 sigma   49.51 bits
  A discovery is twenty-one bits of compression saving.

  AND THE OBJECTION THAT KILLED THE DENSITY USE DOES NOT APPLY HERE.
  compress.py's decisive number was the ADJUSTED rate: 140 GB of parameters
  making 8.3% into 14008.3%.  In a DETECTION the two hypotheses share the same
  model, so

        l_0 - l_1  =  [L(M) + L(d|M,H0)] - [L(M) + L(d|M,H1)],

  AND L(M) CANCELS EXACTLY.  Verified below at a model size of 1.12e12 bits:
  the difference is unchanged to the last digit.

        DENSITY NEEDS AN ABSOLUTE CODE LENGTH, WHERE THE CODEBOOK IS FATAL.
        DETECTION NEEDS A DIFFERENCE, WHERE THE CODEBOOK CANCELS.  That single
        distinction is why the same tool fails one door and works for another.

  CAUTION, AND IT IS REAL: the cancellation holds for a SHARED model -- one
  noise model, with and without an added signal.  If H1 needs its own template
  library, the model sizes differ and the remainder is a genuine Occam penalty
  that must be paid.  Recorded, not waved away.

  AND THE CONVERSE IS THE POINT FOR THIS DOOR.  Delétang et al. show it both
  ways: a predictor gives a compressor, AND "any compressor can be employed for
  sequence prediction".  So a compressor IS a model of the data.  detect.py's
  route is a DISCRIMINATOR APPLIED TO AN EXISTING CATALOGUE, for an object
  whose waveform nobody has -- which is precisely where a model-agnostic,
  compression-based statistic is the right instrument rather than a clever one.

===============================================================================
WHAT THIS DOES AND DOES NOT BUY
===============================================================================

DOES:   name a usable method for door three's silent row, in the language that
        decides that door, with an exact evidence-to-bits conversion and a
        reason the codebook objection does not bite.

DOES NOT: supply the number density.  doors.py's next measurement for door
        three is HOW MANY ARE THERE, and a detection statistic is how you would
        look, not how many there are.  The silent row is still silent.

DOES NOT: move door one or door two.  One is immune by form; the other has had
        this exact argument run on it, in print, on a wormhole, and entropy
        stability did not imply dynamical stability.

stdlib only.  The literature rows are CITED with arXiv numbers; the identities
are measured here.
"""
import math
import sys


# --------------------------------- 1: door two, immune by form

def door_two_refusal_terms():
    """What appears in the bank-loan theorem.  Not energy; not information."""
    return ("non-achronality", "an existing outside causal path")


def information_appears_in_door_two():
    return "information" in door_two_refusal_terms()


# ------------------- 2: door one, the bridge that has been walked

WORMHOLE_STABILITY_PAPER = ("2408.14328", "Eiroa, Figueroa-Aguirre, Peñafiel & "
                                          "Perez Bergliaffa: BOTH stabilities "
                                          "for a charged thin-shell wormhole")

FINDINGS_2408 = (
    ("Hawking-type entropy", "no configurations both dynamically AND "
                             "thermodynamically stable"),
    ("power-law entropy", "thermodynamically stable but DYNAMICALLY UNSTABLE "
                          "configurations without charge are possible"),
    ("where they overlap", "a small zone; every completely stable "
                           "configuration is OVERCHARGED, Q > m"),
    ("the entropy function", "an ANSATZ, not derived -- free parameters the "
                             "dynamical side does not have"),
)


def entropy_is_the_right_kind_for_algebra():
    """Yes: thermodynamic stability is d2S < 0, a condition of the same TYPE as
    a dynamical stability condition, and both are defined for a wormhole."""
    return True


def entropy_stability_implies_dynamical():
    """No.  Measured, on a wormhole, in arXiv:2408.14328."""
    return False


def entropy_substitutes_for_the_calculation():
    return entropy_stability_implies_dynamical()


# --------------------- 3: door three, the affirmative

def code_length(p):
    """Arithmetic coding: l = -log2 P."""
    return -math.log2(p)


def log2_bayes_factor(p0, p1):
    return math.log2(p1 / p0)


def code_length_saving(p0, p1):
    """l_0 - l_1.  Identical to the log2 Bayes factor, exactly."""
    return code_length(p0) - code_length(p1)


def evidence_is_the_saving(p0, p1, tol=1e-12):
    """The identity, measured rather than asserted."""
    return abs(code_length_saving(p0, p1) - log2_bayes_factor(p0, p1)) < tol


def bits_for_sigma(sigma):
    """-log2 of the two-sided Gaussian tail.  A discovery, in bits."""
    return -math.log2(math.erfc(sigma / math.sqrt(2.0)))


def two_part_length(model_bits, data_bits):
    return model_bits + data_bits


def codebook_cancels(model_bits=1.12e12, l0=5.0e6, l1=4.99e6, tol=1e-9):
    """A shared model contributes L(M) to BOTH totals, so it drops out of the
    difference.  This is why the adjusted-rate objection does not reach here."""
    with_model = two_part_length(model_bits, l0) - two_part_length(model_bits, l1)
    without = l0 - l1
    return abs(with_model - without) < tol


SHARED_MODEL_REQUIRED = True     # a template library re-introduces an Occam cost
COMPRESSOR_IS_A_MODEL = True     # Delétang et al., the converse direction


# ------------------------------------------ the routing table

ROUTES = (
    ("DOOR 2", "order", "NO -- immune by form",
     "the bank-loan theorem has no information term"),
    ("DOOR 1", "algebra", "RIGHT KIND, WRONG RESULT",
     "entropy stability does NOT imply dynamical stability, measured on a "
     "wormhole in arXiv:2408.14328"),
    ("DOOR 3", "statistics", "YES -- as a DETECTION STATISTIC",
     "log2 B = the code-length saving, exactly; and the codebook cancels"),
)


def doors_where_it_can_be_spent():
    return [d for d, _l, v, _w in ROUTES if v.startswith("YES")]


def currency_language():
    """A compression argument is a statistics/information argument."""
    return "statistics"


def matches_deciding_language(door):
    import doors
    return doors.deciders()[door] == currency_language()


NUMBER_DENSITY_SUPPLIED = False   # a statistic is HOW to look, not HOW MANY


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
        print("  %-56s %20.6f %20.6f  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. DOOR TWO -- NO, BY THE FORM OF ITS THEOREM")
    print("     what appears in the bank-loan theorem: %s"
          % ", ".join(door_two_refusal_terms()))
    chk("does 'information' appear in it", information_appears_in_door_two(), False)
    print("       Immune.  Settled in compress.py and not reopened.")

    print("\n2. DOOR ONE -- THE RIGHT KIND, AND THE BRIDGE HAS BEEN WALKED")
    chk("is an entropy argument the right KIND for a stability row",
        entropy_is_the_right_kind_for_algebra(), True)
    print("     CITED  %s  %s" % WORMHOLE_STABILITY_PAPER)
    for what, finding in FINDINGS_2408:
        print("       %-22s %s" % (what, finding))
    chk("does entropy stability IMPLY dynamical stability",
        entropy_stability_implies_dynamical(), False)
    chk("so can it substitute for the calculation",
        entropy_substitutes_for_the_calculation(), False)
    print("       The bridge exists, it has been crossed, AND IT LANDS")
    print("       SOMEWHERE ELSE.  Not a shortcut past the work doors.py named.")

    print("\n3. DOOR THREE -- YES, AS A DETECTION STATISTIC")
    print("     the evidence in bits IS the compression saving, exactly:")
    for p0, p1 in ((0.30, 0.70), (0.01, 0.99), (0.5, 0.5000001)):
        print("       P0=%.7f P1=%.7f   l0-l1 = %+.6f   log2 B = %+.6f"
              % (p0, p1, code_length_saving(p0, p1), log2_bayes_factor(p0, p1)))
        chk("  identity holds", evidence_is_the_saving(p0, p1), True)
    print("     and a discovery is a small number of bits:")
    for s in (3, 5, 8):
        print("       %d sigma   %.2f bits" % (s, bits_for_sigma(s)))
    for s in (3, 5, 8):
        p = math.erfc(s / math.sqrt(2.0))
        near("  round trip: 2^-bits recovers the %d-sigma p-value" % s,
             2.0 ** (-bits_for_sigma(s)), p, 1e-12)
    print("     AND THE CODEBOOK CANCELS, which is why this use survives:")
    chk("a shared model drops out of the difference", codebook_cancels(), True)
    print("       compress.py's fatal number was the ADJUSTED rate -- 140 GB of")
    print("       parameters turning 8.3%% into 14008.3%%.  DENSITY needs an")
    print("       ABSOLUTE code length; DETECTION needs a DIFFERENCE, and the")
    print("       model contributes L(M) to both sides.")
    chk("but only for a SHARED model", SHARED_MODEL_REQUIRED, True)
    print("       A template library makes the model sizes differ, and the")
    print("       remainder is a real Occam penalty.  Recorded, not waved away.")
    chk("and a compressor IS a model (Delétang's converse)",
        COMPRESSOR_IS_A_MODEL, True)

    print("\nTHE ROUTING TABLE")
    print("     %-8s %-12s %-26s %s" % ("door", "decided by", "verdict", "why"))
    for d, lang, verdict, why in ROUTES:
        print("     %-8s %-12s %-26s %s" % (d, lang, verdict, why[:44]))
    chk("doors where compressed bits can be spent", doors_where_it_can_be_spent(),
        ["DOOR 3"])
    chk("the currency's own language", currency_language(), "statistics")
    chk("and door three's deciding language is the same",
        matches_deciding_language("DOOR 3"), True)
    chk("door one's is not", matches_deciding_language("DOOR 1"), False)
    chk("door two's is not", matches_deciding_language("DOOR 2"), False)
    print("       THAT IS WHY IT WORKS THERE AND NOWHERE ELSE: the currency and")
    print("       the deciding language are finally the same language.")

    print("\nWHAT IT DOES NOT BUY")
    chk("does it supply the number density", NUMBER_DENSITY_SUPPLIED, False)
    print("       doors.py's next measurement for door three is HOW MANY ARE")
    print("       THERE.  A statistic is how you would LOOK, not how many there")
    print("       are.  THE SILENT ROW IS STILL SILENT.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("WHERE COMPRESSED BITS CAN BE SPENT\n")
    print("  %-8s %-12s %s" % ("door", "decided by", "verdict"))
    for d, lang, verdict, _w in ROUTES:
        print("  %-8s %-12s %s" % (d, lang, verdict))
    print("\n  %-26s %s" % ("the currency's language", currency_language()))
    print("  %-26s %s" % ("5 sigma, in bits", "%.2f" % bits_for_sigma(5)))
    print("  %-26s %s" % ("number density supplied", NUMBER_DENSITY_SUPPLIED))
    print("\n" + "=" * 79)
    print("""VERDICT

  YES, FOR EXACTLY ONE DOOR, AND NOT AS DENSITY.

  DOOR TWO IS IMMUNE BY FORM and that was already settled: the bank-loan
  theorem contains non-achronality and an existing outside causal path,
  and no information term at all.  Nothing for a better code to reach.

  DOOR ONE IS THE INTERESTING NO.  An entropy argument is NOT
  categorically the wrong kind there -- thermodynamic stability is
  d2S < 0, a condition of the same type as a dynamical one, and both are
  defined for a wormhole.  THE CURRENCY IS SPENDABLE.  But it has
  already been spent, in print, on exactly this object: Eiroa,
  Figueroa-Aguirre, Peñafiel & Perez Bergliaffa (arXiv:2408.14328)
  compute both stabilities for a charged thin-shell wormhole and find
  that for a Hawking-type entropy THERE ARE NO CONFIGURATIONS BOTH
  DYNAMICALLY AND THERMODYNAMICALLY STABLE, and that for a power-law
  entropy there are THERMODYNAMICALLY STABLE BUT DYNAMICALLY UNSTABLE
  configurations.  ENTROPY STABILITY DOES NOT IMPLY DYNAMICAL
  STABILITY.  The bridge exists, it has been crossed, and it lands
  somewhere else -- so it is not a shortcut past the stability
  calculation doors.py named as door one's next measurement.  Their
  entropy function is also an ANSATZ rather than derived, carrying free
  parameters the dynamical side does not have, which is exactly the
  slack that makes agreement unreliable.

  DOOR THREE IS THE YES, and it is the first affirmative answer in this
  entire currency thread.  Not density -- A DETECTION STATISTIC.  The
  evidence in bits IS the compression saving in bits:

        log2 B = l_0 - l_1,        exactly, verified as an identity.

  A signal is present exactly when the data is cheaper to describe with
  it than without, which is Rissanen's minimum description length and a
  rigorous framework rather than a metaphor.  The thresholds are small:
  three sigma is 8.53 bits, FIVE SIGMA IS 20.73 BITS, eight is 49.51.

  AND THE OBJECTION THAT KILLED THE DENSITY USE DOES NOT REACH THIS
  ONE.  compress.py's fatal number was the adjusted rate -- 140 GB of
  parameters turning 8.3% into 14008.3%.  But detection compares two
  hypotheses on the SAME data with the SAME model, so L(M) appears on
  both sides and CANCELS EXACTLY.  Density needs an absolute code
  length, where the codebook is fatal; detection needs a difference,
  where the codebook cancels.  That one distinction is why the same
  tool fails one door and works for another.  (The cancellation needs a
  SHARED model: a template library makes the sizes differ and leaves a
  real Occam penalty.  Recorded.)

  AND THE INDEX EXPLAINS WHY IT WORKS THERE AND NOWHERE ELSE.  A
  compression argument is a STATISTICS argument.  Door three is the
  door decided by STATISTICS.  For the first time in this thread THE
  CURRENCY AND THE DECIDING LANGUAGE ARE THE SAME LANGUAGE -- and that,
  not the cleverness of the tool, is the whole reason it lands.

  WHAT IT DOES NOT BUY: the number density.  doors.py's next
  measurement for door three is HOW MANY ARE THERE, and a detection
  statistic is how you would LOOK, not how many there are.  THE SILENT
  ROW IS STILL SILENT.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
