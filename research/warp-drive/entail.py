#!/usr/bin/env python3
r"""
entail.py -- THE INEQUALITY OF INEQUALITIES, AND THE EQUALITY OF INEQUALITIES.

M: "There is one more route for payment that I want to consider and it's a
concept -- inequality of inequalities vs the equality of inequalities."

Both concepts are real, both are measurable on the seated index, and the first
of them is a better route than any forgery -- ON CONDITION, and the condition
is the finding.

    python3 entail.py             the reading
    python3 entail.py --selftest  fixtures

===============================================================================
THE TWO CONCEPTS, MADE PRECISE
===============================================================================

Every cell of the index IS an inequality.  So there are two further relations
available that the index has never carried, and both are between the
inequalities rather than inside them:

    EQUALITY OF INEQUALITIES    two cells that are the SAME statement
    INEQUALITY OF INEQUALITIES  one cell that ENTAILS another

Neither is the coordinate order.  The coordinate order is an encoding; these
two are properties of what the cells mean.

===============================================================================
1. THE EQUALITY -- 17 CELLS, 16 STATEMENTS
===============================================================================

Exactly one pair among the seated cells is one statement written twice:

        (T=2, V=0, M=0, Q=0, B=0)  ==  (T=3, V=0, M=0, Q=0, B=0)

the Einstein NEC and the Ricci NEC, identical because `G_kk = R_kk - (R/2)g_kk`
and `g_kk = 0` on a null vector.  This is already recorded in the index as a
QUOTIENT rather than a collision -- the T coordinate stops distinguishing on the
null slice and nowhere else -- and what is added here is the count.  **The
seventeen cells are sixteen statements**, and `statistics`' `E = 0` is a closure
over citations, not over distinct claims.  Recorded, not repaired.

===============================================================================
2. THE INEQUALITY -- AND THE INDEX IS ENCODED BACKWARDS IN TWO SLOTS
===============================================================================

`a => b` is decided by logic alone, never by a field equation, and only within a
fixed tensor and regime -- a different tensor is a different statement, not a
weaker one.  Three ladders, and they do not run the same way:

    V   quantify over a LARGER direction set  =>  STRONGER
        causal => timelike => null            (higher coordinate is stronger)
    M   pointwise => smeared => averaged => achronal-averaged
                                              (LOWER coordinate is stronger)
    B   `>= 0` => `>= a negative bound`       (LOWER coordinate is stronger)
        `B = 2` is INCOMPARABLE with both: the entropy variation has no fixed
        sign, so `>= 0` does not entail it.

That gives 22 entailments among the 17.  Asking which encoding would make
entailment coincide with the coordinate order, exactly four sign vectors work
and all four agree where it matters:

        +T  +V  -M  +Q  -B

**TWO OF THE FIVE SLOTS ARE ENCODED BACKWARDS.**  `T` and `Q` come out free
because no entailment ever crosses a tensor or a regime -- that is the
comparability rule restated, not a discovery, and the file says so rather than
reporting four answers as an ambiguity.

A STEP-PATH SEARCH FOUND HALF OF THIS WITH NO SEMANTICS AT ALL.  Of eight
candidate re-slicings tried on purely structural grounds, `inverse M` was the
one that produced jumps.  That search looked only at the V-M pair, so the B flip
was outside what it could see; within the pair it could see, it recovered the
correct flip.  Reported as a convergence and nothing more: an empirical search
agreeing with a semantic fact is corroboration, not evidence for either.

===============================================================================
3. THE PAYMENT -- ENTAILMENT IS FREE TRANSPORT, AT A PRICE IN ASSUMPTIONS
===============================================================================

If `a => b` then verifying `a` discharges `b` at no cost.  So the receipt is the
set of `=>`-MAXIMAL cells, and that set is EXACT rather than searched:
**necessary**, because nothing entails a maximal cell so it cannot be obtained
free, and **sufficient**, because those cells reach all seventeen.

        SIX CELLS OF SEVENTEEN DISCHARGE THE WHOLE INDEX.

And that six is **not unconditional**, which is the honest half of the result.
Two of the entailment steps carry a physical caveat -- `timelike => null` needs
continuity of the tensor, and `>= 0 => >= a negative bound` needs the bound to
be negative.  Withdraw them and the receipt grows:

        assumptions accepted                      receipt
        the measure ladder only (set restriction)   12 of 17
        + the larger-direction-set steps            10
        + the negative-bound step                    8
        + the continuity step                        7
        all of them                                  6

**SO THE TWO ROUTES ARE PRICED IN DIFFERENT CURRENCIES.**  A forged receipt
costs 8 cells for an `order`-reading account and assumes NO physics -- it is a
fact about closure operators.  Entailment costs 6 and assumes two steps, or 12
and assumes almost nothing.  Cheaper in cells is dearer in assumptions, and
neither table dominates the other.

===============================================================================
3b. AND THE LARGEST BANKNOTE IN THAT RECEIPT IS COUNTERFEIT
===============================================================================

The six are not six equal notes.  Ranked by what each discharges:

        matter T, timelike,  pointwise, semiclassical, >= 0       5 others
        matter T, causal,    pointwise, classical,     >= 0       4
        Ricci R,  timelike,  pointwise, classical,     >= 0       1
        effective T_eff, null, pointwise, classical,   >= 0       1
        Einstein G, null,    pointwise, classical,     >= 0       0
        matter T, null,      pointwise, semiclassical, >= entropy 0

**THE ONE THAT DISCHARGES THE MOST IS FALSE.**  The semiclassical WEC is
refuted -- the Casimir vacuum has measured negative energy density in a timelike
frame -- and the index seats it anyway, because an index enumerates CITATIONS
AND NOT TRUTHS.  That is the index behaving correctly and the RECEIPT behaving
incorrectly, because **entailment from a false premise is vacuous**: a refuted
cell discharges nothing, and the five it appeared to cover are not covered.

Priced against truth rather than against citation, the receipt is

        6 of 17   accepting every seated citation
        8 of 17   withholding discharge from the refuted one

**AND EIGHT IS EXACTLY WHAT THE FORGERY COSTS.**  The entailment route's whole
apparent advantage over forging was one refuted condition doing the work.  Two
routes that looked differently priced turn out to cost the same, and the file
prints both numbers rather than the flattering one.

===============================================================================
3c. WHAT IS ACTUALLY MAN-MADE HERE, AND IT IS THE COUNTERFEIT
===============================================================================

The refutation is not a technicality.  **The Casimir effect is man-made, it is
measured, and it is the failure of the strongest condition in the receipt.**  So
the family's one contact with a laboratory is not a note you can spend -- it is
the note that turned out to be forged, by nature, before anyone tried.

That cuts both ways and the second way is the honest limit.  A false condition
is a resource: its negation holds, and the negation is a real negative energy
density.  But the size of that resource is not free either -- it is bounded by
quantum energy inequalities, which in this index is the **B slot**, and the B
slot is what fixes the bound the opening inherits.  **The laboratory violation
is real and it is quantitatively capped by the same structure that makes the
opening small.**  Nothing here escapes that, and this file does not claim to.

===============================================================================
4. WHAT THE CORRECT ENCODING DOES TO THE LANGUAGES
===============================================================================

Re-encoding to `+V -M -B` flips two coordinates, which is a MIXED reversal --
and the hierarchy law's Clause F.2 says exactly who survives one: `order` and
`algebra` break, `geometry` survives because a hull is affine-invariant,
`statistics` survives because it reads only membership.  The prediction was
available before the measurement.  It holds, and the size of it was not
predicted:

        language        as encoded        aligned
        order            192  (E 175)     58  (E 41)
        algebra          192  (E 175)     58  (E 41)
        information      156  (E 139)     39  (E 22)
        geometry          29  (E  12)     29  (E 12)   UNMOVED
        statistics        17  (E   0)     17  (E  0)   UNMOVED

**MOST OF THE OVER-GENERATION WAS THE ENCODING.**  `order` admitted 192 cells
against 17 seated; in the encoding that carries entailment it admits 58.  The
residue those languages were reporting is substantially an artefact of running
the measure and bound ladders backwards.

**AND `statistics` RETURNS E = 0 IN BOTH.**  The one headline the index rests on
is encoding-independent, which is the check worth having: it would have been a
poor result if the family's exact closure had depended on a slot's direction.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not claim the entailment order is complete.**  It uses the stated
rules and no others.  Further entailments may hold; every count here is a floor
on the relation and therefore a CEILING on the receipt.

**It does not flatten the assumption levels.**  The receipt is a table against
what you accept, never a single number, because the single number would be the
one thing a reader would quote.

**It does not repair the index.**  The as-encoded form stands. That two slots
run against entailment is recorded, and nothing downstream is rewritten.

**It does not claim a cell is a unit of cost.**  Cells are citations. Whether
verifying one is work, and how much, is not a question this file touches.
"""

import itertools
import sys

import barter
import hlaw
import necindex

# The three ladders.  Each pair is "the first entails the second", and each
# ladder carries the status of the step rather than being asserted flat.
V_SET = {(2, 1), (2, 0)}            # a larger direction set: unconditional
V_CONT = {(1, 0)}                   # timelike => null: needs continuity of T
M_LADDER = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}   # unconditional
B_BOUND = {(0, 1)}                  # >= 0 => >= a NEGATIVE bound

LEVELS = (
    ("the measure ladder only (set restriction)", set(), M_LADDER, set()),
    ("+ the larger-direction-set steps", V_SET, M_LADDER, set()),
    ("+ the negative-bound step", V_SET, M_LADDER, B_BOUND),
    ("+ the continuity step", V_SET | V_CONT, M_LADDER, set()),
    ("all of them", V_SET | V_CONT, M_LADDER, B_BOUND),
)


# The index enumerates CITATIONS, not truths, and one seated citation is refuted:
# (matter T, timelike, pointwise, semiclassical, >= 0) -- the semiclassical WEC.
# The Casimir vacuum has measured negative energy density in a timelike frame.
# ENTAILMENT FROM A FALSE PREMISE IS VACUOUS, so a refuted cell discharges nothing.
REFUTED = frozenset({(0, 1, 0, 1, 0)})


def entails(a, b, vs=V_SET | V_CONT, ms=M_LADDER, bs=B_BOUND):
    """`a` entails `b`, by logic alone.

    Comparable only at a fixed tensor and regime: a different tensor is a
    different statement, not a weaker one, and no field equation is used to
    relate them.
    """
    if a == b or a[0] != b[0] or a[3] != b[3]:
        return False
    for x, y, ok in ((a[1], b[1], vs), (a[2], b[2], ms), (a[4], b[4], bs)):
        if x != y and (x, y) not in ok:
            return False
    return True


def order_on(cells, vs=V_SET | V_CONT, ms=M_LADDER, bs=B_BOUND):
    return [(a, b) for a in cells for b in cells if entails(a, b, vs, ms, bs)]


def receipt(cells, vs=V_SET | V_CONT, ms=M_LADDER, bs=B_BOUND, honest=False):
    """(the cells that must be established, how many of `cells` they reach).

    Exact, not searched: nothing entails a maximal cell, so each must be
    established on its own; and if they reach everything the set is sufficient.

    `honest=True` withholds the power to discharge from every REFUTED cell.
    That is not a stricter convention, it is the correct one -- a false premise
    entails nothing -- and it moves the answer, which is why both are offered
    and the report prints them side by side.
    """
    def pays(a, b):
        if honest and a in REFUTED:
            return False
        return entails(a, b, vs, ms, bs)
    mx = [a for a in cells if not any(pays(b, a) for b in cells)]
    reach = set(mx)
    for a in mx:
        reach |= {b for b in cells if pays(a, b)}
    return mx, len(reach)


def same_statement(cells):
    """Cells that are one statement written twice.

    `G_kk = R_kk - (R/2) g_kk` and `g_kk = 0` on a null vector, so the Einstein
    and Ricci conditions coincide at V = 0 and nowhere else.
    """
    return [(a, b) for a in sorted(cells) for b in sorted(cells)
            if a < b and a[1] == 0 == b[1] and {a[0], b[0]} == {2, 3}
            and a[2:] == b[2:]]


def aligning_signs(cells):
    """Every sign vector making entailment a coordinate order.  A sign is FREE
    where no entailment crosses that coordinate; the report names which."""
    e = order_on(cells)
    out = []
    for s in itertools.product((1, -1), repeat=5):
        if all(all(s[i] * a[i] >= s[i] * b[i] for i in range(5)) for a, b in e):
            out.append(s)
    free = [i for i in range(5) if all(a[i] == b[i] for a, b in e)]
    return out, free


def align(c):
    """The encoding that carries entailment: +T +V -M +Q -B."""
    return (c[0], c[1], 3 - c[2], c[3], 2 - c[4])


# --------------------------------------------------------------- the reading

def report():
    X = frozenset(necindex.cells())
    XA = frozenset(align(c) for c in X)
    print("=" * 74)
    print("THE INEQUALITY OF INEQUALITIES, AND THE EQUALITY OF INEQUALITIES")
    print("=" * 74)
    print()

    print("1. THE EQUALITY -- cells that are ONE statement written twice.")
    eq = same_statement(X)
    for a, b in eq:
        print("   %s  ==  %s" % (a, b))
    print("   Einstein NEC = Ricci NEC: G_kk - R_kk = -(R/2) g_kk, and g_kk = 0")
    print("   on a null vector. The T coordinate stops distinguishing there and")
    print("   nowhere else -- already recorded as a quotient; here it is counted.")
    print("   %d CELLS, %d STATEMENTS." % (len(X), len(X) - len(eq)))
    print()

    print("2. THE INEQUALITY -- and two slots are encoded backwards.")
    e = order_on(X)
    print("   %d entailments among the %d cells." % (len(e), len(X)))
    signs, free = aligning_signs(X)
    names = "TVMQB"
    print("   Sign vectors that make entailment the coordinate order: %d" % len(signs))
    for s in signs:
        print("      " + "  ".join("%s%s" % ("+" if s[i] > 0 else "-", names[i])
                                   for i in range(5)))
    print("   FREE (no entailment crosses them, so unconstrained): %s"
          % ", ".join(names[i] for i in free))
    print("   CONSTRAINED: %s" % ", ".join(
        "%s%s" % ("+" if signs[0][i] > 0 else "-", names[i])
        for i in range(5) if i not in free))
    print("   The identity encoding is NOT among them:", tuple([1] * 5) in signs)
    print()

    print("3. THE PAYMENT -- entailment is free transport, priced in assumptions.")
    print("   %-44s %s" % ("assumptions accepted", "receipt"))
    for label, vs, ms, bs in LEVELS:
        mx, reach = receipt(X, vs, ms, bs)
        print("   %-44s %2d of %d   (reaches %d)" % (label, len(mx), len(X), reach))
    print()
    mx, _ = receipt(X)
    print("   The six, and each is entailed by nothing in the index:")
    for c in mx:
        print("      %s" % (c,))
    print()
    print("   AGAINST A FORGED RECEIPT, WHICH IS PRICED DIFFERENTLY:")
    print("      forging for an `order` account   8 of 17, and assumes NO physics")
    print("      entailment, all steps            6 of 17, and assumes two")
    print("      entailment, set restriction only 12 of 17, and assumes almost none")
    print("   Cheaper in cells is dearer in assumptions. Neither dominates.")
    print()

    print("3b. AND THE LARGEST BANKNOTE IN THAT RECEIPT IS COUNTERFEIT.")
    ranked = sorted(mx, key=lambda c: -sum(1 for b in X if entails(c, b)))
    for c in ranked:
        n = sum(1 for b in X if entails(c, b))
        print("      %-18s discharges %d%s" % (str(c), n,
              "   <- REFUTED (the semiclassical WEC)" if c in REFUTED else ""))
    print("   The one that discharges the most is FALSE: the Casimir vacuum has")
    print("   measured negative energy density in a timelike frame. The index")
    print("   seats it because an index enumerates CITATIONS, not truths.")
    print("   ENTAILMENT FROM A FALSE PREMISE IS VACUOUS, so it discharges nothing.")
    hm, hr = receipt(X, honest=True)
    print()
    print("      %-42s %d of %d" % ("accepting every seated citation", len(mx), len(X)))
    print("      %-42s %d of %d" % ("withholding it from the refuted one", len(hm), len(X)))
    print("   AND %d IS EXACTLY WHAT THE FORGERY COSTS. The entailment route's" % len(hm))
    print("   whole advantage was one refuted condition doing the work.")
    print()
    print("3c. WHAT IS MAN-MADE HERE IS THE COUNTERFEIT. The Casimir effect is")
    print("   man-made, measured, and it IS the failure of the receipt's largest")
    print("   note. The family's one contact with a laboratory is not a note you")
    print("   can spend -- it is the note nature had already forged. And its size")
    print("   is capped by quantum energy inequalities, which in this index is the")
    print("   B slot, the same structure that makes the opening small.")
    print()

    print("4. WHAT THE CORRECT ENCODING DOES TO THE LANGUAGES.")
    print("   Flipping M and B is a MIXED reversal, and Clause F.2 says who")
    print("   survives one. The prediction was available before the measurement.")
    c0, _ = hlaw.closures(X)
    cA, _ = hlaw.closures(XA)
    print("   %-13s %-16s %-16s %s" % ("language", "as encoded", "aligned", ""))
    for L in hlaw.LANGS:
        moved = frozenset(align(y) for y in c0[L]) != cA[L]
        print("   %-13s %6d (E %3d)   %6d (E %3d)   %s"
              % (L, len(c0[L]), len(c0[L]) - len(X),
                 len(cA[L]), len(cA[L]) - len(X), "moved" if moved else "UNMOVED"))
    print()
    print("   MOST OF THE OVER-GENERATION WAS THE ENCODING: `order` admitted 192")
    print("   against 17 seated, and admits 58 in the encoding that carries")
    print("   entailment. AND `statistics` RETURNS E = 0 IN BOTH -- the one")
    print("   headline the index rests on does not depend on a slot's direction.")
    print()
    print("   Every count here is a FLOOR on the entailment relation and so a")
    print("   CEILING on the receipt. Nothing is repaired.")
    return 0


# -------------------------------------------------------------------- checks

def selftest():
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("entail selftest")
    X = frozenset(necindex.cells())

    chk("the seated index", len(X), 17)
    chk("one pair is one statement written twice", len(same_statement(X)), 1)
    chk("and it is Einstein/Ricci at the null slice", same_statement(X)[0],
        ((2, 0, 0, 0, 0), (3, 0, 0, 0, 0)))
    chk("17 cells, 16 statements", len(X) - len(same_statement(X)), 16)

    chk("entailments among the seated cells", len(order_on(X)), 22)
    chk("no entailment crosses a tensor or a regime",
        all(a[0] == b[0] and a[3] == b[3] for a, b in order_on(X)), True)

    signs, free = aligning_signs(X)
    chk("sign vectors aligning entailment with the coordinate order", len(signs), 4)
    chk("T and Q are the free ones", free, [0, 3])
    chk("V is +, M and B are -", [signs[0][i] for i in (1, 2, 4)], [1, -1, -1])
    chk("every solution agrees on the constrained slots",
        all([s[i] for i in (1, 2, 4)] == [1, -1, -1] for s in signs), True)
    chk("the identity encoding does NOT carry entailment", tuple([1] * 5) in signs, False)

    # The receipt: exact, and its dependence on what is assumed.
    chk("the receipt at each assumption level",
        [len(receipt(X, vs, ms, bs)[0]) for _, vs, ms, bs in LEVELS],
        [12, 10, 8, 7, 6])
    chk("every level still reaches all 17",
        [receipt(X, vs, ms, bs)[1] for _, vs, ms, bs in LEVELS], [17] * 5)
    mx, _ = receipt(X)
    chk("each of the six is entailed by nothing -- so six is NECESSARY",
        all(not any(entails(b, a) for b in X) for a in mx), True)
    chk("and the six are SUFFICIENT", receipt(X)[1], 17)
    chk("on pure set restriction the receipt is WORSE than a forgery",
        len(receipt(X, set(), M_LADDER, set())[0]) > barter.minimum_receipt(X, "order")[0],
        True)
    chk("with both physics steps it is BETTER",
        len(mx) < barter.minimum_receipt(X, "order")[0], True)

    # The truth layer: the biggest note in the receipt is a refuted citation.
    chk("the refuted cell is one of the maximal six", REFUTED <= set(mx), True)
    chk("and it is the one that discharges the most",
        max(mx, key=lambda c: sum(1 for b in X if entails(c, b))), (0, 1, 0, 1, 0))
    chk("it appeared to discharge five",
        sum(1 for b in X if entails((0, 1, 0, 1, 0), b)), 5)
    hm, hr = receipt(X, honest=True)
    chk("priced against TRUTH the receipt grows to 8", len(hm), 8)
    chk("and still reaches everything", hr, 17)
    chk("which is EXACTLY the forgery's price -- the advantage was the false note",
        len(hm), barter.minimum_receipt(X, "order")[0])

    # Clause F.2's prediction about a mixed reversal.
    XA = frozenset(align(c) for c in X)
    c0, _ = hlaw.closures(X)
    cA, _ = hlaw.closures(XA)
    moved = {L: frozenset(align(y) for y in c0[L]) != cA[L] for L in hlaw.LANGS}
    chk("F.2 predicted the movers: order, algebra, information",
        sorted(L for L in hlaw.LANGS if moved[L]), ["algebra", "information", "order"])
    chk("and the survivors: geometry, statistics",
        sorted(L for L in hlaw.LANGS if not moved[L]), ["geometry", "statistics"])
    chk("the over-generation collapses", (len(c0["order"]), len(cA["order"])), (192, 58))
    chk("information too", (len(c0["information"]), len(cA["information"])), (156, 39))
    chk("statistics is E = 0 in BOTH encodings",
        (len(c0["statistics"]) - 17, len(cA["statistics"]) - 17), (0, 0))

    print("entail selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
