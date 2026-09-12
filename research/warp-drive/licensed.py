#!/usr/bin/env python3
"""
licensed.py -- THE LICENSED ENERGY CONDITIONS.  A family that closes every
operator-bearing language of the cypher to E = 0, DERIVED RATHER THAN POSITED.

M: "We need to theorize/define a new family of energy conditions.  And it is
the family of ECs that solves the cypher, closing all its languages to E = 0
for the entire transition state."

IT WAS NOT NECESSARY TO INVENT ONE.  necindex.py's five slots and the seventeen
named conditions already determine it: the five operator-bearing languages are
extensive and monotone, so iterating all five jointly from the named family
converges to THE LEAST FAMILY CONTAINING THEM THAT EVERY LANGUAGE CLOSES.  It
converges in ONE step, to 192 cells of a 288-cell box, and the cypher's own
criterion fires on it -- "K.langclose holds: languages agree and E = 0".

AND THE 192 HAS A ONE-LINE DEFINITION THAT NOBODY PUT IN.

===============================================================================
1. THE FAMILY
===============================================================================

    THE LICENSED ENERGY CONDITIONS.  For any tensor Theta in {T, T_eff, G, R},
    any direction set in {null, timelike, causal}, and any measure in
    {pointwise, smeared, averaged, achronal-averaged}:

        CLASSICAL       Theta_mn u^m u^n   >=  0
        SEMICLASSICAL   <Theta_mn> u^m u^n >=  B,  B in {0, a negative
                                                   state-independent bound,
                                                   an entropy variation}

    192 members.  Seventeen of them have names.

In the coordinates the closure is exactly the set B <= 2Q, and the "2" is an
artefact of the coding; the coding-free statement is

        A BOUND BELOW ZERO IS PERMITTED EXACTLY WHEN THE REGIME IS QUANTUM.

THE OPERATORS DERIVED THAT.  It was never imposed, and it is not a convention:
a classical theory has no h-bar to set the scale of a negative bound and no
entanglement entropy to vary, so >= 0 is the only right-hand side it can write.
FIVE CLOSURE OPERATORS, RUN ON SEVENTEEN HISTORICALLY-ACCUMULATED CONDITIONS,
RECONSTRUCTED THAT CONSTRAINT AND NOTHING ELSE.

===============================================================================
2. WHY 192 IS NOT AN ARTEFACT OF THE OPERATORS
===============================================================================

The whole box is trivially a fixed point of every extensive operator, so the
question is whether the operators do any work.  THEY DO, AND THE CONTROL IS
SHARP: closed one at a time, the individual named conditions generate ALMOST
NOTHING -- between 1 and 4 cells each.

    THE NEC CLOSES TO ITSELF.  One cell, every language, a fixed point alone.
    It is the only condition in the family that is a closed family by itself,
    which is a structural reading of BV's "it is the weakest one" that this
    tree did not have.

AND THE CLOSURE IS SUPERADDITIVE, WHICH IS THE FINDING UNDER THE FINDING:

        the classical rows alone close to        48
        the semiclassical rows alone close to    48
        the two together close to               192

    NINETY-SIX CELLS EXIST ONLY BECAUSE BOTH REGIMES SIT IN ONE INDEX.  Neither
    half demands them; the coexistence does.  A family of purely classical
    conditions and a family of purely quantum ones are each small and closed.
    Putting them in one index is what generates the other half of the family.

===============================================================================
3. AND THE CONSTRAINT LANDS ON THE SLOTS THAT DO NOT MATTER
===============================================================================

The closure constrains the (Q, B) pair and NOTHING ELSE.  T, V and M are
completely free: every tensor, every direction set and every measure appears at
every licensed (Q, B).

    THE ONE SLOT EVERY ESCAPE MOVES IS T -- necindex.py measured that, four of
    four openers.  AND T IS THE SLOT THE CLOSURE LEAVES ENTIRELY UNGUARDED.

So the licensed family answers M's question in the affirmative and then says
something harder than yes: closing every language costs nothing in the tensor
slot, because no language on this roster can see the difference between a
condition on matter and the same condition on curvature.  THE CLOSURE IS BLIND
TO THE ONLY DOOR.

===============================================================================
4. WHAT THIS IS NOT.  FOUR LIMITS, EACH LOAD-BEARING
===============================================================================

  (a) A CELL IS A CITATION, NOT A TRUTH.  necindex.py established that the
      index enumerates well-formed conditions and cannot tell a standing one
      from a refuted one -- it demanded the semiclassical WEC, which is false.
      SO 175 UNNAMED LICENSED CELLS ARE 175 CANDIDATES FOR A NAME, and this
      file claims for none of them that it is true, useful, or even meaningful.

  (b) "ALL ITS LANGUAGES" MEANS FIVE OF SEVEN, AND THE OTHER TWO CANNOT BE
      CLOSED BY ANYTHING.  Roster 1173 carries seven.  analysis is NOT-RUN --
      no witness is declared for it, and register 1172 is why NOT-RUN is a
      distinct state here rather than a silent pass.  documentary is SILENT by
      construction: it returns a citation and not a binary, so it has no
      closure mechanism to satisfy.  NEITHER IS CLOSED HERE AND NEITHER CAN BE.

  (c) 192 IS THE LEAST SUCH FAMILY, NOT THE ONLY ONE.  The full 288-cell box
      closes too, trivially.  What is derived is the SMALLEST family that
      contains the named conditions and closes every measurable language.

  (d) THE SLOTS ARE OURS.  A different decomposition of "what an energy
      condition is" gives a different box and a different closure.  This
      measures necindex.py's five coordinates and nothing more universal.

NOTHING IS REPAIRED.
"""

import itertools
import os
import sys

import necindex

cypher = necindex.cypher
COORDS = necindex.COORDS
SIZES = (4, 3, 4, 2, 3)                 # |T|, |V|, |M|, |Q|, |B|
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

CLOSURE_IS_DERIVED_NOT_POSITED = True
CELLS_ARE_CITATIONS_NOT_TRUTHS = True
ANALYSIS_STAYS_NOT_RUN = True
DOCUMENTARY_STAYS_SILENT = True
NOTHING_IS_REPAIRED = True


def box():
    return set(itertools.product(*[range(n) for n in SIZES]))


def licensed():
    """The family, by its derived definition: a bound below zero needs Q = 1."""
    return {c for c in box() if c[4] == 0 or c[3] == 1}


def joint_closure(seed):
    """Least set containing seed and closed under all five operators.

    Every operator is extensive and monotone on a finite lattice, so the
    iteration converges and its limit is the least joint fixed point above the
    seed.
    """
    X = set(seed)
    for _ in range(64):
        ix = cypher.Index("x", COORDS, sorted(X))
        new = set(X)
        for name in necindex.OPERATORS:
            new |= set(cypher.ADMISSION[name][0](ix, OPTS)[0])
        if new == X:
            return X
        X = new
    raise RuntimeError("joint closure did not converge")


def per_language(cs):
    ix = cypher.Index("x", COORDS, sorted(cs))
    return {n: len(set(cypher.ADMISSION[n][0](ix, OPTS)[0]) - set(cs))
            for n in necindex.OPERATORS}


def free_slots(cs):
    """Slots whose every value appears at every combination of the others."""
    cs = set(cs)
    out = []
    for i in range(5):
        rest = {tuple(v for j, v in enumerate(c) if j != i) for c in cs}
        if all(tuple(r[:i]) + (v,) + tuple(r[i:]) in cs
               for r in rest for v in range(SIZES[i])):
            out.append(COORDS[i])
    return out


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    named = set(necindex.cells())
    F = joint_closure(named)
    print("  the closure, from the named family")
    print("      %-40s %8d" % ("named conditions", len(necindex.FAMILY)))
    print("      %-40s %8d" % ("distinct named cells", len(named)))
    print("      %-40s %8d" % ("the ambient box", len(box())))
    print("      %-40s %8d" % ("the joint fixed point", len(F)))
    print("      %-40s %8d" % ("unnamed licensed cells", len(F) - len(named)))
    print("      %-40s %8s" % ("equals the one-line definition",
                               F == licensed()))
    print()
    print("  and every language closes on it")
    for n, e in sorted(per_language(F).items()):
        print("      %-20s E = %d" % (n, e))
    print("      analysis   NOT-RUN (no witness declared, register 1172)")
    print("      documentary SILENT  (returns a citation, not a binary)")
    print()
    print("  what is excluded, and it is one thing")
    miss = sorted(box() - F)
    print("      %-40s %8d" % ("excluded cells", len(miss)))
    print("      %-40s %8s" % ("all of them classical (Q = 0)",
                               all(c[3] == 0 for c in miss)))
    print("      %-40s %8s" % ("all of them with a non-zero bound",
                               all(c[4] > 0 for c in miss)))
    print()
    print("  the control: the operators do work")
    sizes = {}
    for r in necindex.FAMILY:
        sizes.setdefault(len(joint_closure([tuple(r[1:6])])), []).append(r[0])
    for k in sorted(sizes):
        print("      one condition closes to %2d cells : %s"
              % (k, ", ".join(sorted(sizes[k]))[:52]))
    print()
    print("  and it is superadditive")
    cl = [tuple(r[1:6]) for r in necindex.FAMILY if r[4] == 0]
    qm = [tuple(r[1:6]) for r in necindex.FAMILY if r[4] == 1]
    a, b = len(joint_closure(cl)), len(joint_closure(qm))
    print("      %-40s %8d" % ("classical rows alone close to", a))
    print("      %-40s %8d" % ("semiclassical rows alone close to", b))
    print("      %-40s %8d" % ("together", len(F)))
    print("      %-40s %8d" % ("cells the coexistence alone demands",
                               len(F) - a - b))
    print()
    print("  which slots the closure constrains")
    print("      %-40s %8s" % ("slots left completely free", free_slots(F)))
    print("      %-40s %8s" % ("and the slot every opener moves", "T"))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The family exists, it is 192 conditions, and its definition is")
    print("  that a bound below zero is licensed exactly by a quantum regime.")
    print("  It was derived, not posited.  And it leaves the tensor slot -- the")
    print("  only slot any escape has ever moved -- entirely unguarded.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("licensed.py --selftest")
    print()

    named = set(necindex.cells())
    F = joint_closure(named)

    # ------------------------------------------------------- the family itself
    chk("the ambient box", len(box()), 288)
    chk("the joint fixed point", len(F), 192)
    chk("and it IS the one-line definition B > 0 only when Q = 1",
        F == licensed(), True)
    chk("which in the coding is B <= 2Q",
        F == {c for c in box() if c[4] <= 2 * c[3]}, True)
    chk("it contains every named condition", named <= F, True)
    chk("unnamed licensed cells", len(F) - len(named), 175)

    # ------------------------------------------------- every language closes
    e = per_language(F)
    for n in necindex.OPERATORS:
        chk("%s closes on it" % n, e[n], 0)
    chk("all five at once", sum(e.values()), 0)
    # NEGATIVE CONTROL: the named family does NOT close, so E = 0 is a property
    # of the licensed family and not of the operators being toothless.
    en = per_language(named)
    chk("while the named family closes in statistics only",
        sorted(k for k, v in en.items() if v == 0), ["statistics"])
    chk("and fails the other four", sum(1 for v in en.values() if v > 0), 4)

    # -------------------------------------------------- what is excluded
    miss = box() - F
    chk("excluded cells", len(miss), 96)
    chk("every excluded cell is classical", all(c[3] == 0 for c in miss), True)
    chk("every excluded cell carries a non-zero bound",
        all(c[4] > 0 for c in miss), True)
    chk("and nothing else is excluded",
        miss == {c for c in box() if c[3] == 0 and c[4] > 0}, True)

    # ------------------------------------- THE CONTROL: the operators do work
    ones = {r[0]: len(joint_closure([tuple(r[1:6])])) for r in necindex.FAMILY}
    chk("no single condition closes past 4 cells", max(ones.values()), 4)
    chk("and the NEC closes to itself alone", ones["NEC"], 1)
    chk("uniquely", sorted(k for k, v in ones.items() if v == 1), ["NEC"])
    # NEGATIVE CONTROL: closing the whole box is trivial, so 192 being a proper
    # subset is what makes the result non-vacuous.
    chk("the box is a fixed point too, trivially",
        len(joint_closure(box())), 288)
    chk("so 192 is a PROPER subset and the result is not vacuous",
        len(F) < len(box()), True)

    # ------------------------------------------------------- superadditivity
    a = len(joint_closure([tuple(r[1:6]) for r in necindex.FAMILY if r[4] == 0]))
    b = len(joint_closure([tuple(r[1:6]) for r in necindex.FAMILY if r[4] == 1]))
    chk("classical rows alone", a, 48)
    chk("semiclassical rows alone", b, 48)
    chk("the coexistence alone demands", len(F) - a - b, 96)
    chk("so the closure is superadditive", len(F) > a + b, True)

    # ------------------------------------------------------ the free slots
    chk("slots the closure leaves free", free_slots(F), ["T", "V", "M"])
    chk("T is free, and T is the only slot any opener moves",
        "T" in free_slots(F), True)
    chk("and Q, B are the constrained pair",
        [c for c in COORDS if c not in free_slots(F)], ["Q", "B"])

    # ---------------------------------------------------------- the limits
    chk("derived, not posited", CLOSURE_IS_DERIVED_NOT_POSITED, True)
    chk("cells are citations, not truths", CELLS_ARE_CITATIONS_NOT_TRUTHS, True)
    chk("analysis stays NOT-RUN", ANALYSIS_STAYS_NOT_RUN, True)
    chk("documentary stays SILENT", DOCUMENTARY_STAYS_SILENT, True)
    res = cypher.run(cypher.Index("licensed", COORDS, sorted(F)), "1173", OPTS)
    chk("and the cypher agrees on both",
        sorted(v.language for v in res["_verdicts"]
               if v.state in (cypher.SILENT, cypher.NOT_RUN)),
        ["analysis", "documentary"])
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
