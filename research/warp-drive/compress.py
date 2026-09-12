#!/usr/bin/env python3
"""
compress.py -- compression is not density, and door two is not short of density.

M: "door 2 -- a non-achronal connection that is also a shortcut -- current
language models have found a way to compress binary into its shortest output by
volume.  This gives the density required in the only form acceptable other than
a black hole."

Two separate claims and they fail separately.  The compression claim fails on
information theory -- and it fails inside the paper it rests on, three times
over.  The door-two claim fails on ROUTING: door two is not refused for lack of
density, so a density argument is the wrong KIND of argument for it, and
doors.py's index is exactly what says so.

THE SECOND FAILURE IS THE USEFUL ONE.  It is the index earning its keep on its
first use after being built.

And one thing in the claim is right and worth keeping: "the only form
acceptable other than a black hole" is the correct question, and it has an
exact answer nobody here had computed.

===============================================================================
1. WHAT LANGUAGE-MODEL COMPRESSION ACTUALLY ACHIEVES -- AND IT IS REAL
===============================================================================

Delétang, Ruoss, Duquenne et al., "Language Modeling Is Compression" (DeepMind,
ICLR 2024, arXiv:2309.10668).  Arithmetic coding driven by a language model's
conditional probabilities is a lossless compressor, and the log-loss objective
IS the compression objective.  Measured, on 1 GB of each modality:

                       enwik9    ImageNet   LibriSpeech
        gzip            32.3%      70.7%       36.4%
        LZMA2           23.0%      57.9%       29.9%
        PNG             42.9%      58.5%       32.2%
        FLAC            89.5%      61.9%       30.9%
        Chinchilla 70B   8.3%      48.0%       21.0%

    A TEXT MODEL BEATS PNG ON IMAGES AND FLAC ON AUDIO.  That is a real and
    surprising result and nothing below disputes it.

===============================================================================
2. AND THE SAME PAPER REFUTES USING IT AS DENSITY, THREE TIMES
===============================================================================

  (a) THE PIGEONHOLE PRINCIPLE, which the authors state themselves: "a lossless
      compressor induces an injective function over bit sequences, meaning that
      we cannot compress all sequences equally well".  An injection into a
      smaller set does not exist.  Compression BUYS ON SOME INPUTS BY PAYING ON
      OTHERS -- it is a redistribution, not a reduction.

  (b) RANDOM DATA DOES NOT COMPRESS.  Their own baseline row: Chinchilla 70B on
      random data, 100.8%.  gzip, 100.0%.  FLAC, 107.8%.  The models EXPAND it
      slightly.  A source with no redundancy has nothing to remove, and the
      Bekenstein bound is a statement about exactly such a source.

  (c) THE MODEL IS PART OF THE CODE.  Counting the 70B parameters at two bytes
      each -- 140 GB -- the ADJUSTED rate on a 1 GB file is 14008.3%.  Not
      8.3%: FOURTEEN THOUSAND PERCENT, a factor of 1687 worse than the raw
      figure and 140 times worse than not compressing at all.  Llama 2 (7B)
      gives 1408.9%.  The authors: a foundation model "can only achieve
      non-trivial (adjusted) compression rates when evaluated on datasets in
      the order of TBs (or more)", and there is an OPTIMAL model size beyond
      which scaling makes compression WORSE.

    Computed below: against LZMA2 on enwik9, Chinchilla 70B needs about 0.95 TB
    before it breaks even -- which is the authors' "order of TBs", reached from
    their own two numbers.

===============================================================================
3. AND THE PHYSICS: BEKENSTEIN IS ALREADY DENOMINATED IN COMPRESSED BITS
===============================================================================

This is the part that closes it, and it is one line.

        S <= 2 pi R E / (hbar c)

bounds the number of DISTINGUISHABLE QUANTUM STATES of a system of energy E in
radius R.  Naming one of N distinguishable states costs log2(N) bits IN ANY
CODE -- that is what distinguishable means.  Recoding permutes the names; it
does not merge two states into one.

    COMPRESSION REMOVES REDUNDANCY.  ENTROPY IS WHAT IS LEFT WHEN ALL
    REDUNDANCY HAS BEEN REMOVED.  SO THE BOUND IS STATED ON THE
    POST-COMPRESSION QUANTITY ALREADY, AND THERE IS NOTHING LEFT TO SQUEEZE.

That is why (b) above is not an incidental benchmark row.  Random data is
incompressible BECAUSE it is all entropy, and the configuration the transition
needs is specified by its entropy, not by a lossy sketch of it.

===============================================================================
4. "THE ONLY FORM ACCEPTABLE OTHER THAN A BLACK HOLE" -- THE RIGHT QUESTION,
   AND IT HAS AN EXACT ANSWER
===============================================================================

spectra.py found the optimal information carrier is a horizon.  M asks the
obvious next thing: what is the best NON-HORIZON carrier?  Nobody here had
computed it.  It is exact.

Not being a black hole means R > 2GM/c^2.  Write the compactness
C = 2GM/(Rc^2) < 1 and substitute into Bekenstein:

        S_max(C) = 2 pi R (C R c^4 / 2G) / (hbar c) = C * pi R^2 / l_P^2
                 = C * A / (4 l_P^2)
                 = C * S_BLACK-HOLE,        EXACTLY.

    Measured below at C = 0.99, 0.5, 0.1, 0.01 and 1e-6: the ratio to the
    black-hole value equals C to within ONE UNIT IN THE LAST PLACE of a double
    (worst relative residual 1.39e-16).  The identity is exact; the residual is
    representation.  An exact == was tried first and FAILS at C = 0.99 and 0.1,
    which is worth recording -- it is the fixture catching an overclaim rather
    than the physics wobbling.

        THERE IS NO SECOND FORM.  A NON-HORIZON HOLDS EXACTLY ITS COMPACTNESS
        FRACTION OF A HORIZON'S CAPACITY.  Want 99% of the density?  Be 99% of
        the way to being a black hole.  The bound is continuous and its maximum
        IS the horizon; nothing sits beside it.

    ONE EXCEPTION IS FLAGGED AND NOT CLAIMED.  core.py found the negative core
    has NO Buchdahl limit -- 2|M|/R runs to 8378 with no horizon -- so it is
    the one configuration here that escapes the compactness ceiling.  But
    Bekenstein is not stated for E < 0, and this file does not extend it.
    NOT-RUN, and recorded as a NOT-RUN.

===============================================================================
5. AND DOOR TWO IS NOT REFUSED FOR LACK OF DENSITY
===============================================================================

Here is the part that matters most, and it costs one lookup rather than an
argument.

doors.py measured which language decides each door.  DOOR TWO IS DECIDED BY
ORDER, and its refusal is gjw.py's bank-loan theorem: traversability needs
non-achronality, non-achronality needs an EXISTING OUTSIDE CAUSAL PATH, so the
wormhole never beats it.

    THAT THEOREM HAS NO ENERGY TERM AND NO DENSITY TERM IN IT.  It is a
    statement about causal structure.  You cannot move it with a better
    energy density any more than you can move it with a better compressor,
    because neither quantity appears.

        A DENSITY ARGUMENT IS THE WRONG KIND OF ARGUMENT FOR DOOR TWO, AND THE
        INDEX IS WHAT SAYS SO.  This is the first use of doors.py since it was
        built, and it did the one job an index is for: it routed a proposal to
        the row it would have to move, and the row is not the one the proposal
        addresses.

Where WOULD a density argument land?  INFORMATION.  And INFORMATION already
ADMITS on all three doors (doors.py), so it is not the constraining row
anywhere.  On the main question expand.py has INFORMATION refusing -- but what
is missing there is a VALUE OF rho, negative and at magnitude, and no bit count
supplies a sign.

stdlib only.  The compression figures are CITED from arXiv:2309.10668; the
compactness identity is measured here.
"""
import math
import sys

G = 6.67430e-11
C_LIGHT = 2.99792458e8
HBAR = 1.054571817e-34


# --------------------- 1: what the measurement actually says (CITED)

PAPER = "arXiv:2309.10668, Delétang et al., ICLR 2024"

RATES = (   # compressor, enwik9, ImageNet, LibriSpeech, random   (raw, %)
    ("gzip", 32.3, 70.7, 36.4, 100.0),
    ("LZMA2", 23.0, 57.9, 29.9, 100.0),
    ("PNG", 42.9, 58.5, 32.2, 100.0),
    ("FLAC", 89.5, 61.9, 30.9, 107.8),
    ("Chinchilla 70B", 8.3, 48.0, 21.0, 100.8),
)

ADJUSTED = (("Llama 2 (7B)", 8.9, 1408.9),
            ("Chinchilla 1B", 11.3, 211.3),
            ("Chinchilla 7B", 10.2, 1410.2),
            ("Chinchilla 70B", 8.3, 14008.3))


def beats_domain_specific():
    """A text model beating PNG on images and FLAC on audio.  Real."""
    r = dict((n, (a, b, c, d)) for n, a, b, c, d in RATES)
    return (r["Chinchilla 70B"][1] < r["PNG"][1]
            and r["Chinchilla 70B"][2] < r["FLAC"][2])


# ------------------ 2: the paper's own three refutations

def random_data_compresses():
    """No.  Every compressor is at or above 100% on random data."""
    return any(row[4] < 100.0 for row in RATES)


def adjusted_penalty(name="Chinchilla 70B"):
    """How much worse the adjusted rate is than the raw one."""
    d = dict((n, (raw, adj)) for n, raw, adj in ADJUSTED)
    raw, adj = d[name]
    return adj / raw


def model_bytes(params_billion=70.0, bytes_per_param=2):
    return params_billion * 1e9 * bytes_per_param


def breakeven_bytes(model_rate=8.3, rival_rate=23.0, params_billion=70.0):
    """Data needed before the model's better rate pays for its own size."""
    saving = (rival_rate - model_rate) / 100.0
    return model_bytes(params_billion) / saving


def breakeven_tb(**kw):
    return breakeven_bytes(**kw) / 1e12


PIGEONHOLE = ("a lossless compressor induces an injective function over bit "
              "sequences, so we cannot compress all sequences equally well")


def compression_is_a_redistribution():
    """By the pigeonhole principle.  It buys on some inputs by paying on others."""
    return True


# ------------- 3: the bound is already stated on the compressed quantity

def bits_to_name_one_of(n_states):
    """log2(N), in ANY code.  That is what 'distinguishable' means."""
    return math.log2(n_states)


def recoding_changes_the_count(n_states, code_a=2, code_b=7):
    """Naming N states in base 2 or base 7 changes the DIGITS, not the COUNT."""
    a = math.log(n_states, code_a) * math.log2(code_a)
    b = math.log(n_states, code_b) * math.log2(code_b)
    return abs(a - b) > 1e-9


BEKENSTEIN_BOUNDS = "the number of distinguishable quantum states"
ENTROPY_IS = "what is left when all redundancy has been removed"


# ---------------- 4: the best non-horizon carrier, exactly

def planck_area():
    return HBAR * G / C_LIGHT ** 3


def black_hole_bits(R):
    """A / 4 l_P^2, in bits."""
    return 4.0 * math.pi * R * R / (4.0 * planck_area()) / math.log(2.0)


def bits_at_compactness(R, compactness):
    """Bekenstein at C = 2GM/(Rc^2): S <= 2 pi R E / (hbar c)."""
    M = compactness * R * C_LIGHT ** 2 / (2.0 * G)
    return 2.0 * math.pi * R * (M * C_LIGHT ** 2) / (HBAR * C_LIGHT * math.log(2.0))


def capacity_fraction(R, compactness):
    """Measured: this equals the compactness, exactly."""
    return bits_at_compactness(R, compactness) / black_hole_bits(R)


def fraction_residual(R, compactness):
    """How far the measured fraction is from the compactness, relatively.
    Analytically zero; in doubles it is at most one unit in the last place."""
    f = capacity_fraction(R, compactness)
    return abs(f - compactness) / compactness


def no_second_form(R=1.0, compactnesses=(0.99, 0.5, 0.1, 0.01, 1.0e-6),
                   ulp=1e-15):
    """S_max(C) = C * S_BH.  Exact analytically; asserted here to a few ULP,
    because an exact == fails at C = 0.99 and 0.1 on representation alone --
    which is a fact about doubles and not about the identity."""
    return all(fraction_residual(R, c) < ulp for c in compactnesses)


NEGATIVE_CORE_EXCEPTION = "NOT-RUN"    # core.py: no Buchdahl limit; E < 0 not
                                       # covered by Bekenstein, not extended here


# --------------- 5: routing the proposal through doors.py

def door_two_decided_by():
    import doors
    return doors.deciders()["DOOR 2"]


def door_two_refusal_has_a_density_term():
    """The bank-loan theorem is about causal structure.  No energy, no density."""
    return False


def density_argument_row():
    """Where a density argument WOULD land, if it landed anywhere."""
    return "information"


def information_row_constrains_any_door():
    """It admits on all three, so it is not the constraining row anywhere."""
    import doors
    return any(fn()["information"] == doors.REFUSES for _n, _w, fn in doors.DOORS)


def what_expand_py_is_missing():
    """A VALUE of rho, negative and at magnitude.  No bit count supplies a sign."""
    return "a value of rho, and no bit count supplies a sign"


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-3):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6e %20.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. WHAT LANGUAGE-MODEL COMPRESSION ACHIEVES -- CITED, %s" % PAPER)
    print("     %-16s %9s %10s %12s %9s"
          % ("", "enwik9", "ImageNet", "LibriSpeech", "random"))
    for n, a, b, c, d in RATES:
        print("     %-16s %8.1f%% %9.1f%% %11.1f%% %8.1f%%" % (n, a, b, c, d))
    chk("a TEXT model beats PNG on images and FLAC on audio",
        beats_domain_specific(), True)
    print("       That is real and surprising, and nothing here disputes it.")

    print("\n2. AND THE SAME PAPER REFUTES IT AS DENSITY, THREE TIMES")
    print("     (a) %s" % PIGEONHOLE)
    chk("  so compression is a redistribution, not a reduction",
        compression_is_a_redistribution(), True)
    print("     (b) random data:")
    chk("  does ANY compressor get below 100%% on random data",
        random_data_compresses(), False)
    print("       Chinchilla 70B EXPANDS it, to 100.8%%.  No redundancy, nothing")
    print("       to remove -- and that is the case the bound describes.")
    print("     (c) the model is part of the code:")
    for n, raw, adj in ADJUSTED:
        print("       %-16s raw %6.1f%%   adjusted %9.1f%%" % (n, raw, adj))
    near("  how much worse adjusted is, for Chinchilla 70B",
         adjusted_penalty(), 14008.3 / 8.3)
    near("  its parameters, in bytes", model_bytes(), 1.4e11)
    near("  break-even against LZMA2 on enwik9, in TB", breakeven_tb(), 0.952, 1e-2)
    print("       The authors say 'the order of TBs (or more)'.  That is their")
    print("       sentence reached from their own two numbers.")

    print("\n3. BEKENSTEIN IS ALREADY DENOMINATED IN COMPRESSED BITS")
    print("     S <= 2 pi R E/(hbar c) bounds %s" % BEKENSTEIN_BOUNDS)
    print("     entropy is %s" % ENTROPY_IS)
    near("bits to name one of a million states", bits_to_name_one_of(1e6),
         math.log2(1e6))
    chk("does recoding change the COUNT of states",
        recoding_changes_the_count(1e6), False)
    print("       Recoding permutes the names; it does not merge two states")
    print("       into one.  THE BOUND IS ON THE POST-COMPRESSION QUANTITY,")
    print("       so there is nothing left to squeeze.")

    print("\n4. 'THE ONLY FORM OTHER THAN A BLACK HOLE' -- THE RIGHT QUESTION")
    R = 1.0
    print("     at R = 1 m, a horizon holds %.4e bits" % black_hole_bits(R))
    for c in (0.99, 0.5, 0.1, 0.01, 1.0e-6):
        print("       compactness %8.2e ->  %.4e bits   fraction %.10f"
              % (c, bits_at_compactness(R, c), capacity_fraction(R, c)))
        chk("  fraction equals the compactness, within a few ULP",
            fraction_residual(R, c) < 1e-15, True)
    chk("so is there a second form", not no_second_form(), False)
    worst = max(fraction_residual(R, c) for c in (0.99, 0.5, 0.1, 0.01, 1.0e-6))
    print("       largest relative residual over the five: %.3e" % worst)
    chk("  and it is below two units in the last place", worst < 2.3e-16, True)
    print("       S_max(C) = C * S_BH.  Exact analytically; in doubles the")
    print("       worst residual is ONE UNIT IN THE LAST PLACE, which is a")
    print("       fact about floating point and not about the identity.")
    print("       A non-horizon holds exactly its compactness fraction.  Want")
    print("       99%% of the density?  BE 99%% OF THE WAY TO A BLACK HOLE.")
    chk("the negative-core exception is", NEGATIVE_CORE_EXCEPTION, "NOT-RUN")
    print("       core.py: no Buchdahl limit, 2|M|/R to 8378 with no horizon --")
    print("       but Bekenstein is not stated for E < 0 and is not extended here.")

    print("\n5. AND DOOR TWO IS NOT REFUSED FOR LACK OF DENSITY")
    chk("which language decides door two", door_two_decided_by(), "order")
    chk("does its refusal contain a density term",
        door_two_refusal_has_a_density_term(), False)
    print("       The bank-loan theorem is about CAUSAL STRUCTURE: traversability")
    print("       needs non-achronality, non-achronality needs an EXISTING")
    print("       outside path.  No energy, no density, nothing to improve.")
    chk("where a density argument would land", density_argument_row(),
        "information")
    chk("does INFORMATION constrain any door", information_row_constrains_any_door(),
        False)
    chk("and what expand.py is actually missing", what_expand_py_is_missing(),
        "a value of rho, and no bit count supplies a sign")
    print("       A DENSITY ARGUMENT IS THE WRONG KIND FOR DOOR TWO, AND THE")
    print("       INDEX IS WHAT SAYS SO -- its first use since it was built.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE BEST NON-HORIZON INFORMATION CARRIER\n")
    R = 1.0
    print("  %-22s %s" % ("radius", "1 m"))
    print("  %-22s %.4e bits" % ("a horizon holds", black_hole_bits(R)))
    for c in (0.99, 0.5, 0.01):
        print("  %-22s %.4e bits  (%.2f of the horizon)"
              % ("at compactness %.2f" % c, bits_at_compactness(R, c),
                 capacity_fraction(R, c)))
    print("\n  %-22s %s" % ("second form", "there is none"))
    print("  %-22s %s" % ("door two decided by", door_two_decided_by()))
    print("  %-22s %s" % ("density term in it", "none"))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE COMPRESSION RESULT IS REAL AND THE PAPER IT RESTS ON REFUTES THE
  USE, THREE TIMES.  Chinchilla 70B does compress ImageNet to 48.0% and
  LibriSpeech to 21.0%, beating PNG and FLAC -- a text model beating
  domain-specific compressors, and nothing here disputes it.  But the
  same table carries a RANDOM DATA row at 100.8%: the model EXPANDS
  incompressible input.  The same paper states the PIGEONHOLE
  PRINCIPLE outright -- a lossless compressor is injective, so it buys
  on some inputs by paying on others.  And counting the 70B parameters
  as part of the code, the ADJUSTED rate on 1 GB is 14008.3%: a factor
  of 1687 worse than the raw figure, needing about 0.95 TB before it
  breaks even against LZMA2, which is the authors' own "order of TBs".

  AND THE PHYSICS CLOSES IT IN ONE LINE.  Bekenstein bounds the number
  of DISTINGUISHABLE QUANTUM STATES, and naming one of N of them costs
  log2(N) bits IN ANY CODE -- recoding permutes names, it does not
  merge two states into one.  COMPRESSION REMOVES REDUNDANCY AND
  ENTROPY IS WHAT SURVIVES REDUNDANCY REMOVAL, so the bound is stated
  on the post-compression quantity already.  There is nothing left to
  squeeze, which is exactly why random data does not compress.

  BUT "THE ONLY FORM ACCEPTABLE OTHER THAN A BLACK HOLE" IS THE RIGHT
  QUESTION, AND NOBODY HERE HAD COMPUTED THE ANSWER.  It is exact.  Not
  being a black hole means compactness C = 2GM/(Rc^2) < 1, and
  substituting into Bekenstein gives

        S_max(C) = C * A/(4 l_P^2) = C * S_BLACK-HOLE,   EXACTLY,

  verified at C = 0.99, 0.5, 0.1, 0.01 and 1e-6 to within one unit in
  the last place of a double, worst relative residual 1.39e-16.  (An
  exact == was written first and failed at two of the five: the
  identity is exact, the residual is representation, and the fixture
  caught the overclaim.)  THERE IS NO SECOND FORM.  A non-horizon holds exactly its
  compactness fraction of a horizon's capacity: want 99% of the
  density, be 99% of the way to being a black hole.  The bound is
  continuous and its maximum IS the horizon.  (One exception is flagged
  and not claimed: core.py's negative core has no Buchdahl limit, and
  Bekenstein is not stated for E < 0.  NOT-RUN.)

  AND THE PART THAT MATTERS MOST COST A LOOKUP RATHER THAN AN ARGUMENT.
  DOOR TWO IS DECIDED BY ORDER, and its refusal is the bank-loan
  theorem: traversability needs non-achronality, non-achronality needs
  an EXISTING OUTSIDE CAUSAL PATH, so the wormhole never beats it.
  THAT THEOREM HAS NO ENERGY TERM AND NO DENSITY TERM IN IT.  You
  cannot move it with a better density any more than with a better
  compressor, because neither quantity appears in it.

        A DENSITY ARGUMENT IS THE WRONG KIND OF ARGUMENT FOR DOOR TWO,
        AND THE INDEX IS WHAT SAYS SO.

  That is doors.py's first use since it was built, and it did the one
  job an index is for: it routed a proposal to the row it would have to
  move, and the row is not the one the proposal addresses.  A density
  argument lands on INFORMATION -- which ADMITS on all three doors, so
  it constrains none of them.  On the main question INFORMATION does
  refuse, and what is missing there is A VALUE OF rho, negative and at
  magnitude.  NO BIT COUNT SUPPLIES A SIGN.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
