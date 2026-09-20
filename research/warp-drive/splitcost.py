#!/usr/bin/env python3
r"""
splitcost.py -- CAN THE CORRIDOR'S COST BE SPLIT BETWEEN ITS TWO ENDS?
YES, AND BETWEEN N.  THE GAIN LAW IS QUADRATIC SO SEGMENTING DIVIDES THE BILL
BY N EXACTLY -- BUT THE PRODUCT IS CONSERVED AND THE RESIDUE IS THE PATH
MEASURED IN PLANCK CELLS.

M: "If the same elements must be present at both ends of the corridor for
transition to happen, I wonder if the energy cost can be split between the two
points."

    python3 splitcost.py             the reading
    python3 splitcost.py --selftest  fixtures, stdlib only

THE QUESTION HAS FOUR ANSWERS BECAUSE THERE ARE FOUR COSTS, AND THEY DIFFER.

    cost                              splittable?
    ---------------------------------------------------------------
    the GJW coupling                  IRREDUCIBLY TWO-SIDED -- it is not
                                      merely splittable, there is no
                                      one-sided version of it at all
    the flat-space amplification      YES, exactly as 1/N, with a floor
    entanglement distribution         YES, exponential -> linear (repeaters)
    the relativistic clock, D/c       NO.  Causality.  Nothing moves it.

M's intuition is right in three of the four, and the one that refuses is the
one that was never about energy.

===============================================================================
1. THE COUPLING IS NOT SPLITTABLE -- IT IS TWO-SIDED BY CONSTRUCTION
===============================================================================

`gjw.py` reads the deformation that makes the wormhole traversable:

    dS = INT dt d^{d-1}x  h(t,x) O_R(t,x) O_L(-t,x),    Delta < d/2

**THAT IS A PRODUCT OF AN OPERATOR AT THE RIGHT BOUNDARY WITH AN OPERATOR AT
THE LEFT.**  It cannot be applied from one end.  There is no term in it that
acts on R alone, and setting either factor to the identity kills it -- which is
exactly why GJW's closed form vanishes at Delta = 0, "where the only operator
is the identity, so there is nothing to couple."

So the answer to M's question, for the mechanism the tree actually holds, is
stronger than yes.  **The cost is not merely SHAREABLE between the two points;
it is UNPAYABLE from one.**  A corridor is a two-ended object in its defining
equation, not only in its geometry.

===============================================================================
2. THE AMPLIFICATION SPLITS AS 1/N, EXACTLY
===============================================================================

`gjw.py` closes the flat-space calculation GJW leave as a remark, and the answer
is a quadratic law -- measured at exponent 2.0000 over six decades:

    required gain  =  C D^2,        C = 4.386649e71 m^-2

**A QUADRATIC COST IS THE BEST POSSIBLE NEWS FOR SPLITTING.**  Break the span
into N segments of length D/N.  Each needs C(D/N)^2, so the total is

    N * C (D/N)^2  =  C D^2 / N

and the bill falls as 1/N while the per-segment gain falls as 1/N^2.
`split_gain()` computes it; `split_is_exactly_one_over_n()` verifies the law
rather than restating it.

===============================================================================
3. BUT THE PRODUCT IS CONSERVED, AND THAT IS THE REAL RESULT
===============================================================================

Segments cannot usefully be shorter than the length at which the gain is
already unity.  `gjw.py` computes that length: **d1 = 1.509849e-36 m = 0.0934
Planck lengths**, where C d1^2 = 1 exactly.  So N <= D/d1, and at that floor

    total  =  C D^2 / (D/d1)  =  C D d1  =  D / d1  =  N itself.

**THE FLOOR EQUALS THE SEGMENT COUNT.**  Verified to one part in 10^9 at four
separations by `floor_equals_count()`.  Splitting does not destroy the cost, it
CHANGES ITS UNITS: amplitude becomes multiplicity, and the invariant is

    (total bill)  x  (number of segments)  =  C D^2

so the two things you trade are the BILL and the COUNT, and the floor is
exactly where they cross -- total = N = D/d1.  (A first draft of this file
wrote that product as "gain per segment times count"; that quantity is merely
the total again, and `product_invariant`'s fixture caught it.)
What survives at maximum splitting is

    D / d1  --  THE PATH LENGTH MEASURED IN UNITS OF 0.0934 PLANCK LENGTHS.

For Proxima Centauri at 4.2465 ly that residue is **2.6609e52**.  It is not an
energy, a mass or a gain; it is a count of cells along the path, and no way of
dividing the work reduces it.

**BOTH COST MEASURES AGREE, AND ONE OF THEM WAS GUESSED WRONG BEFORE IT WAS
COMPUTED.**  If cost is linear in gain, the total falls monotonically to the
floor.  If cost is measured in decibels, `decibel_cost()` rises from 1.05e3 dB
at N = 1, peaks, and falls to EXACTLY ZERO at N = N_max where every segment
needs unity gain.  The stationary point at N_max/e is a MAXIMUM -- the second
derivative is -20/(N ln 10) < 0 -- so the dB measure is worst in the middle and
cheapest at maximum splitting.  `db_stationary_is_a_maximum()` checks the sign
by evaluation, because the first draft of this file called it an optimum.

===============================================================================
4. THE ENTANGLEMENT CHANNEL SPLITS TOO, AND THIS ONE IS PRACTICAL
===============================================================================

`transit.py` establishes that the corridor must be traversed once in order to
exist -- a channel spanning D required something to cross D beforehand.  That
laying cost splits, and the result is the central theorem of long-distance
quantum communication: **Briegel, Dur, Cirac & Zoller (1998), the quantum
repeater.**

Direct distribution through a lossy line survives with probability
exp(-D/L_att), so the expected trials go as exp(D/L_att).  Split into N
segments with entanglement swapping between them and the resource is
N exp(D/(N L_att)), minimised at N* = D/L_att, giving

    e * D / L_att   --  LINEAR IN D, NOT EXPONENTIAL.

`repeater_saving()` reports the orders saved.  Over 10^4 km of fibre that is
194 orders of magnitude; over one light year, 1.87e11 orders.

**THIS IS THE ONE PLACE WHERE SPLITTING CHANGES THE ASYMPTOTIC CLASS RATHER
THAN THE CONSTANT.**  The amplification split in section 2 divides by N; this
one converts an exponential into a linear.

===============================================================================
5. WHAT DOES NOT SPLIT
===============================================================================

**THE CLOCK.**  D/c is irreducible.  Meet-in-the-middle halves each photon's
flight, but confirming the pair exists returns the other half, and `transit.py`
already measures the end of it: advantage over light 0.000 at four separations,
because withholding the two classical bits leaves the far end at exactly I/2.
Splitting is a statement about RESOURCES.  It says nothing about the light cone
and cannot.

**AND ONE STEP IS NOT ESTABLISHED ANYWHERE.**  Section 2's arithmetic assumes N
segments can be CONCATENATED into one traversable corridor.  Entanglement
swapping does that for Bell pairs and is proved; **no result in this tree or in
GJW shows that N traversable wormhole segments compose into a traversable
corridor.**  That is the load-bearing gap in the whole answer and it is stated
here rather than buried.  `CONCATENATION_STATUS` carries it in the code.

===============================================================================
6. AND THE STOCK SPLITS BY BEING PER-NODE
===============================================================================

`stock.py` costs the destination stock constraint M raised: a 70 kg payload
needs 1.7167e3 kg of stellar feedstock per kg, or 10.06 at a carbonaceous
chondrite.  That cost is LOCAL by construction -- the destination processes its
own matter, and nothing is shipped.

**SO A TWO-WAY NODE PAYS IT ONCE AND EVERY LATER TRANSIT IS FREE OF IT.**  The
stock bill is per-NODE, not per-TRIP, which is the sharpest form of M's
question: the cost is not split between two points so much as AMORTISED over
every transit those points ever carry.

**THREE INDEPENDENT ARGUMENTS NOW FORCE THE SAME TOPOLOGY.**  `stock.py` says
the arrival must hold accessible matter; `arrival.py` says reverse-slingshot
braking "needs a deflector AT THE DESTINATION, which turns the drive into a
NETWORK with nodes"; and section 2 here says the bill falls as 1/N in the number
of intermediate stations.  Matter, braking and cost, arrived at separately,
all say the same thing.

    A TRANSITION DEVICE IS A NETWORK.  SPLITTING THE COST IS NOT A TRICK
    PERFORMED ON IT -- IT IS WHAT THE ARCHITECTURE ALREADY IS.

===============================================================================
7. WHAT THIS FILE REFUSES
===============================================================================

**TO SUM GAINS WITHOUT SAYING SO.**  Section 2 adds per-segment gains, which
prices cost as LINEAR IN GAIN.  That is an assumption about amplifiers, not a
theorem, and section 3 computes the decibel measure alongside it precisely so
the conclusion does not rest on the choice.  Both agree; neither is assumed.

**TO CLAIM THE CONCATENATION.**  See section 5.  Without it, section 2 is
arithmetic about a chain nobody has shown can be built.

**TO CALL 2.6609e52 AN ENERGY.**  It is a dimensionless residue -- a count of
0.0934-Planck-length cells along the path.  Converting it to joules needs a cost
per cell that nothing here supplies.

**TO RE-DERIVE gjw.py.**  C, d1 and the D^2 law are IMPORTED from it, never
copied, exactly as an instrument in this tree imports a seated member.
"""

import math
import sys

import gjw

#: The step section 2 needs and nobody has established.  Carried in code so it
#: travels with the number rather than living only in prose.
CONCATENATION_STATUS = (
    "NOT ESTABLISHED.  Entanglement swapping concatenates Bell pairs (Zukowski, "
    "Zeilinger, Horne & Ekert 1993).  No result in this tree or in GJW shows "
    "that N traversable wormhole segments compose into one traversable "
    "corridor.  Section 2's 1/N is arithmetic conditional on this."
)

#: Fibre attenuation length at 1550 nm (0.2 dB/km).  Cited, not measured here.
L_ATT = 22.0e3
REPEATER_CITE = ("Briegel, Dur, Cirac & Zoller (1998), PRL 81, 5932 -- "
                 "quantum repeaters")
SWAP_CITE = ("Zukowski, Zeilinger, Horne & Ekert (1993), PRL 71, 4287 -- "
             "entanglement swapping")

LY = 9.4607304726e15
C_LIGHT = 2.99792458e8
PROXIMA_M = 4.2465 * LY


# ------------------------------------------------ 2 & 3. the amplification split

def gain_one_span(D):
    """Required amplification over a single span.  IMPORTED from gjw.py."""
    return gjw.amplification_needed(D)


def unity_length():
    """The segment length at which the gain is already 1.  From gjw.py."""
    return gjw.unity_separation()


def split_gain(D, N):
    """(per segment, total over N) with the total priced LINEAR IN GAIN."""
    seg = gjw.amplification_needed(D / N)
    return seg, N * seg


def split_is_exactly_one_over_n(D=PROXIMA_M, Ns=(2, 10, 1000, 10 ** 9)):
    """[(N, total_N / total_1)] -- measured, and it must be 1/N.

    This MEASURES the law rather than restating it: if gjw.py's exponent were
    not 2 the ratios would not be 1/N, and the fixture would catch it.
    """
    one = gain_one_span(D)
    return [(N, split_gain(D, N)[1] / one) for N in Ns]


def max_segments(D):
    """D / d1 -- beyond this a segment would be shorter than unity gain."""
    return D / unity_length()


def floor_total(D):
    """The linear-measure total at maximum splitting."""
    return split_gain(D, max_segments(D))[1]


def floor_equals_count(Ds=(1e3, 1.495978707e11, PROXIMA_M, 1e5 * LY)):
    """[(D, N_max, floor, agree)] -- the floor IS the segment count.

    C D^2 / (D/d1) = C D d1 = D/d1 since C d1^2 = 1.  Checked numerically at
    four separations rather than trusted from the algebra.
    """
    out = []
    for D in Ds:
        n, f = max_segments(D), floor_total(D)
        out.append((D, n, f, abs(f - n) / n < 1e-9))
    return out


def product_invariant(D=PROXIMA_M, Ns=(1, 1e10, 1e30, 1e50)):
    """[(N, total x N)] -- constant, = C D^2, at every N.

    THE INVARIANT IS THE TOTAL TIMES THE COUNT, not the per-segment gain times
    the count -- that second product is just the total again, and a first draft
    of this file printed it as though it were conserved.  The fixture caught it.
    What you trade is TOTAL BILL against SEGMENT COUNT, and their product is
    fixed at C D^2.
    """
    return [(N, split_gain(D, N)[1] * N) for N in Ns]


def decibel_cost(D, N):
    """Total cost if each amplifier is priced in dB rather than in gain."""
    return 10.0 * N * math.log10(gjw.amplification_needed(D / N))


def db_stationary_is_a_maximum(D=PROXIMA_M):
    """(value at N_max/e, at half that, at twice that, is_a_maximum).

    The stationary point of the dB curve sits at N_max/e.  A first draft called
    it an optimum; the second derivative is -20/(N ln 10) < 0, so it is a
    MAXIMUM.  Checked by evaluating on both sides instead of by differentiating.
    """
    n = max_segments(D) / math.e
    a, b, c = decibel_cost(D, n / 2), decibel_cost(D, n), decibel_cost(D, n * 2)
    return a, b, c, (b > a and b > c)


def decibel_floor(D=PROXIMA_M):
    """dB cost at maximum splitting.  Exactly zero: unity gain is 0 dB."""
    return decibel_cost(D, max_segments(D))


def planck_residue(D=PROXIMA_M):
    """What survives maximum splitting: the path in 0.0934-Planck-length cells."""
    return max_segments(D), unity_length() / gjw.L_PLANCK


# ---------------------------------------------- 4. the entanglement channel

def log10_direct(D, L=L_ATT):
    """log10 of expected trials for direct distribution.  exp overflows; log does not."""
    return (D / L) / math.log(10.0)


def log10_chained(D, N, L=L_ATT):
    return math.log10(N) + (D / (N * L)) / math.log(10.0)


def repeater_saving(D, L=L_ATT):
    """(N*, log10 direct, log10 chained, orders saved).  N* = D/L_att."""
    N = max(1.0, round(D / L))
    a, b = log10_direct(D, L), log10_chained(D, N, L)
    return N, a, b, a - b


def repeater_is_linear(D=1e9, L=L_ATT):
    """(e*D/L, chained resource at N*) -- the asymptotic form, checked."""
    N = max(1.0, round(D / L))
    return math.e * D / L, N * math.exp(D / (N * L))


# ------------------------------------------------------- 5. what does not split

def light_time(D=PROXIMA_M):
    """D/c in years.  Not splittable by any architecture."""
    return D / C_LIGHT / 3.15576e7


# ------------------------------------------------------------------- reading

def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 74)
    print("2 & 3.  THE AMPLIFICATION SPLIT, AND ITS FLOOR")
    print("=" * 74)
    D = PROXIMA_M
    print("   span: Proxima Centauri, 4.2465 ly = %.4e m" % D)
    print("   one-span required gain            %.4e" % gain_one_span(D))
    print()
    print("   %-14s %-16s %-16s %s" % ("N", "per segment", "total", "vs one span"))
    for N in (1, 10, 1000, 10 ** 9, 10 ** 30):
        s, t = split_gain(D, N)
        print("   %-14.3e %-16.4e %-16.4e %.4e" % (N, s, t, t / gain_one_span(D)))
    print()
    print("   measured total/one-span ratios (must be 1/N):")
    for N, r in split_is_exactly_one_over_n():
        print("      N %-12.3e  ratio %.6e   1/N %.6e" % (N, r, 1.0 / N))
    print()
    print("   THE FLOOR")
    print("   %-16s %-16s %-16s %s" % ("D (m)", "N_max", "floor total", "equal?"))
    for Dd, n, f, ok in floor_equals_count():
        print("   %-16.4e %-16.4e %-16.4e %s" % (Dd, n, f, ok))
    print()
    print("   (total) x (segment count), at every N -- invariant = C D^2:")
    for N, p in product_invariant():
        print("      N %-12.3e  product %.6e" % (N, p))
    n, cells = planck_residue()
    print()
    print("   RESIDUE AT MAXIMUM SPLITTING: %.4e" % n)
    print("   = the path in units of %.4f Planck lengths." % cells)
    print()
    a, b, c, ismax = db_stationary_is_a_maximum()
    print("   decibel measure: N_max/e is a MAXIMUM, not an optimum (%s)" % ismax)
    print("      at N_max/2e  %.4e" % a)
    print("      at N_max/e   %.4e   <- peak" % b)
    print("      at 2 N_max/e %.4e" % c)
    print("      at N_max     %.4e   <- unity gain is 0 dB" % decibel_floor())
    print()
    print("=" * 74)
    print("4.  THE ENTANGLEMENT CHANNEL -- EXPONENTIAL TO LINEAR")
    print("=" * 74)
    print("   %-14s %-16s %-14s %-12s %s"
          % ("D (m)", "log10 direct", "N* = D/L", "log10 chain", "orders saved"))
    for Dd in (1e5, 1e7, 1e9, LY, PROXIMA_M):
        N, a2, b2, s = repeater_saving(Dd)
        print("   %-14.3e %-16.4e %-14.3e %-12.4f %.4e" % (Dd, a2, N, b2, s))
    e1, e2 = repeater_is_linear()
    print("\n   at N* the resource is e*D/L: %.4f against chained %.4f" % (e1, e2))
    print("   %s" % REPEATER_CITE)
    print()
    print("=" * 74)
    print("5.  WHAT DOES NOT SPLIT")
    print("=" * 74)
    print("   the clock: Proxima at c is %.4f years, and no architecture moves it"
          % light_time())
    print()
    print("   CONCATENATION: %s" % CONCATENATION_STATUS)


# ------------------------------------------------------------------ fixtures

def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-60s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("splitcost.py fixtures  (stdlib only; imports gjw.py, never copies it)")

    # -- the quadratic law is gjw.py's, and we MEASURE it rather than assume ---
    chk("gjw's exponent is 2 to four places",
        float("%.4f" % ((math.log10(gain_one_span(1e6))
                         - math.log10(gain_one_span(1e3)))
                        / 3.0)), 2.0)
    chk("C d1^2 = 1 exactly", round(gjw.gain_coefficient()
                                    * unity_length() ** 2, 9), 1.0)

    # -- the split is exactly 1/N ---------------------------------------------
    for N, r in split_is_exactly_one_over_n():
        chk("split at N=%.0e gives exactly 1/N" % N,
            float("%.9g" % r), float("%.9g" % (1.0 / N)))

    # -- the floor equals the count -------------------------------------------
    chk("the floor equals N_max at all four separations",
        [ok for _d, _n, _f, ok in floor_equals_count()],
        [True, True, True, True])
    chk("Proxima's residue", float("%.5g" % max_segments(PROXIMA_M)), 2.6609e52)
    chk("and it is the path in 0.0934 Planck lengths",
        float("%.4g" % planck_residue()[1]), 0.09342)

    # -- the product is invariant ---------------------------------------------
    ps = [p for _n, p in product_invariant()]
    chk("total x count is invariant across 50 decades of N",
        all(abs(p - ps[0]) / ps[0] < 1e-9 for p in ps), True)
    chk("and it equals the one-span gain, C D^2",
        float("%.6g" % ps[0]), float("%.6g" % gain_one_span(PROXIMA_M)))
    chk("whereas total ALONE is not invariant -- it falls as 1/N",
        all(abs(split_gain(PROXIMA_M, N)[1] - ps[0]) / ps[0] > 0.5
            for N in (1e10, 1e30)), True)

    # -- the dB stationary point is a MAXIMUM (the corrected claim) -----------
    a, b, c, ismax = db_stationary_is_a_maximum()
    chk("the dB stationary point at N_max/e is a MAXIMUM, not an optimum",
        ismax, True)
    chk("and the dB cost at maximum splitting is exactly zero",
        round(decibel_floor(), 6), 0.0)

    # -- the repeater changes the asymptotic class ----------------------------
    _N, a2, b2, s = repeater_saving(1e7)
    chk("10,000 km of fibre: repeaters save 194 orders", int(round(s)), 194)
    chk("direct is exponential in D -- doubling D doubles log10 trials",
        float("%.6g" % (log10_direct(2e7) / log10_direct(1e7))), 2.0)
    chk("chained is sub-linear -- doubling D adds less than 0.31 to log10",
        log10_chained(2e7, round(2e7 / L_ATT))
        - log10_chained(1e7, round(1e7 / L_ATT)) < 0.31, True)
    e1, e2 = repeater_is_linear()
    chk("at N* the chained resource is e*D/L to 3 digits",
        float("%.3g" % e1), float("%.3g" % e2))

    # -- what does not split ---------------------------------------------------
    chk("the clock to Proxima, in years", float("%.4g" % light_time()), 4.247)
    chk("the concatenation step is flagged NOT ESTABLISHED",
        CONCATENATION_STATUS.startswith("NOT ESTABLISHED"), True)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
