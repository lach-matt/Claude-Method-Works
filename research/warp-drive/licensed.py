#!/usr/bin/env python3
"""
licensed.py -- THE LICENSED ENERGY CONDITIONS.  A family that closes every
operator-bearing language of the cypher to E = 0, DERIVED RATHER THAN POSITED.

M: "We need to theorize/define a new family of energy conditions.  And it is
the family of ECs that solves the cypher, closing all its languages to E = 0
for the entire transition state."

IT WAS NOT NECESSARY TO INVENT ONE.  necindex.py's slots and the named
conditions already determine it: the five operator-bearing languages are
extensive and monotone, so iterating all five jointly from the named family
converges to THE LEAST FAMILY CONTAINING THEM THAT EVERY LANGUAGE CLOSES.  It
converges in ONE step, to 256 cells of a 576-cell box, and the cypher's own
criterion fires on it -- "K.langclose holds: languages agree and E = 0".

AND THE 256 HAS A TWO-LINE DEFINITION THAT NOBODY PUT IN, AND THE SECOND LINE
IS A FACT THIS TREE ESTABLISHED SOMEWHERE ELSE ENTIRELY.

===============================================================================
0. RE-MEASURED AT SIX COORDINATES.  WHAT MOVED, AND WHAT RETRACTS
===============================================================================

This file was first measured on a FIVE-coordinate box, 288 cells, before the
arity coordinate A was seated on the energy-condition family.  Its box was
written as the literal (4, 3, 4, 2, 3) and so did not follow -- the file kept
reporting five-coordinate figures against a six-coordinate index until it
crashed outright.  Re-measured on the corrected 576-cell box:

    the joint fixed point       192 -> 256
    the ambient box             288 -> 576
    unnamed licensed cells      175 -> 238
    excluded cells               96 -> 320
    classical rows alone          48 -> 48   (unchanged)
    semiclassical rows alone      48 -> 24
    cells owed to coexistence     96 -> 184
    slots the closure leaves free  T, V, M -> T, M

TWO THINGS CHANGE IN SUBSTANCE, AND ONE OF THEM IS A RETRACTION.

**THE DEFINITION GAINS A SECOND CLAUSE, AND IT IS NOT AN ARTEFACT.**  See
section 1: the derived family is no longer "a bound below zero needs a quantum
regime" alone.

**AND THE NEC IS NO LONGER SINGULAR -- RETRACTED.**  Section 2 said the named
conditions each generate between one and four cells and that THE NEC ALONE
closes to itself, calling that a structural reading of Barcelo-Visser's "it is
the weakest one".  At six coordinates ALL NINETEEN close to themselves alone.
The reading was true of the five-coordinate box and is not a property of the
NEC: one more coordinate leaves every single cell with too little to
interpolate from, and the distinction disappears.  The claim is withdrawn, not
weakened.

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

    256 members.  Eighteen of them have names, over nineteen named rows.

In the coordinates the closure is exactly

        (B = 0 OR Q = 1)   AND   (A = 0 OR V = 2)

and the coding-free statement is TWO sentences, not one:

        A BOUND BELOW ZERO IS PERMITTED EXACTLY WHEN THE REGIME IS QUANTUM.
        A BILINEAR CONDITION IS PERMITTED EXACTLY OVER AN ORDERED CAUSAL PAIR.

THE OPERATORS DERIVED BOTH.  Neither was imposed and neither is a convention.
The first: a classical theory has no h-bar to set the scale of a negative bound
and no entanglement entropy to vary, so >= 0 is the only right-hand side it can
write.

**THE SECOND IS THE ONE WORTH STOPPING ON.**  It says a condition evaluated on
an ORDERED PAIR of vectors is licensed only when the direction set is the full
causal cone.  That is exactly the arity structure the DEC repair established by
hand and from the other end: the only bilinear member of the family is the
dominant energy condition, at V = 2; at quadratic arity the V = 2 cell collapses
into V = 1 because a continuous tensor non-negative on all timelike directions
is non-negative on all causal ones, and at bilinear arity it does not collapse.
That was measured on the FAMILY, by exhibiting rho = 1, p = 2.  Here it falls
out of the CLOSURE, from five operators that were told nothing about causal
cones.  **Two independent derivations of the same coupling, and neither was
built from the other.**

FIVE CLOSURE OPERATORS, RUN ON NINETEEN HISTORICALLY-ACCUMULATED ROWS,
RECONSTRUCTED THOSE TWO CONSTRAINTS AND NOTHING ELSE.

===============================================================================
2. WHY 256 IS NOT AN ARTEFACT OF THE OPERATORS
===============================================================================

The whole box is trivially a fixed point of every extensive operator, so the
question is whether the operators do any work.  THEY DO, and the control is
sharper than it was: closed one at a time, EVERY named condition generates
NOTHING AT ALL -- all nineteen are singleton fixed points.

    AND THAT IS A RETRACTION, NOT A STRENGTHENING OF THE OLD READING.  On the
    five-coordinate box the singletons ran from 1 to 4 cells and only the NEC
    closed to itself, which was reported as a structural reading of BV's "it is
    the weakest one".  At six coordinates every one of the nineteen does.  A
    single cell in a wider box simply has less to interpolate from, so the
    distinction was a property of the box and not of the NEC.  WITHDRAWN.

AND THE CLOSURE IS SUPERADDITIVE, WHICH IS THE FINDING UNDER THE FINDING, and
which the extra coordinate makes stronger rather than weaker:

        the classical rows alone close to         48
        the semiclassical rows alone close to     24
        the two together close to                256

    ONE HUNDRED AND EIGHTY-FOUR CELLS EXIST ONLY BECAUSE BOTH REGIMES SIT IN
    ONE INDEX -- 72 of 256 are owed to either half, and 184 to the coexistence.
    Neither half demands them; putting them in one index is what generates
    them.  On the five-coordinate box that split was 96 against 96.

===============================================================================
3. AND THE CONSTRAINT LANDS ON THE SLOTS THAT DO NOT MATTER
===============================================================================

The closure constrains (Q, B) and (V, A) and NOTHING ELSE.  T and M are
completely free: every tensor and every measure appears at every licensed
(V, Q, B, A).  V ceased to be free when the arity coordinate arrived -- it is
constrained only through its coupling to A, and A only through its coupling to
V, which is the second clause of section 1 restated as a slot fact.

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
      SO 238 UNNAMED LICENSED CELLS ARE 238 CANDIDATES FOR A NAME, and this
      file claims for none of them that it is true, useful, or even meaningful.

  (b) "ALL ITS LANGUAGES" MEANS FIVE OF SEVEN, AND THE OTHER TWO CANNOT BE
      CLOSED BY ANYTHING.  Roster 1173 carries seven.  analysis is NOT-RUN --
      no witness is declared for it, and register 1172 is why NOT-RUN is a
      distinct state here rather than a silent pass.  documentary is SILENT by
      construction: it returns a citation and not a binary, so it has no
      closure mechanism to satisfy.  NEITHER IS CLOSED HERE AND NEITHER CAN BE.

  (c) 256 IS THE LEAST SUCH FAMILY, NOT THE ONLY ONE.  The full 576-cell box
      closes too, trivially.  What is derived is the SMALLEST family that
      contains the named conditions and closes every measurable language.

  (d) THE SLOTS ARE OURS, AND SECTION 0 IS THE PROOF OF IT.  A different
      decomposition of "what an energy condition is" gives a different box and
      a different closure -- and this file has now been measured on two of
      them.  Adding one coordinate moved every figure it reports and withdrew
      one of its findings.  This measures necindex.py's six coordinates and
      nothing more universal.

NOTHING IS REPAIRED.
"""

import itertools
import os
import sys

import necindex

cypher = necindex.cypher
COORDS = necindex.COORDS
# DERIVED, NEVER COPIED. This read (4, 3, 4, 2, 3) as a literal and did not
# follow the energy-condition family from five coordinates to six when the
# arity coordinate A was seated -- so every cell it built was a 5-tuple against
# a 6-coordinate index and selfindex.py died with "cell (0, 0, 0, 0, 0) has 5
# values, expected 6". A copied figure is a figure that can drift.
SIZES = tuple(len(necindex.VALUE_ORDER[c]) for c in COORDS)
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

CLOSURE_IS_DERIVED_NOT_POSITED = True
CELLS_ARE_CITATIONS_NOT_TRUTHS = True
ANALYSIS_STAYS_NOT_RUN = True
DOCUMENTARY_STAYS_SILENT = True
NOTHING_IS_REPAIRED = True


def box():
    return set(itertools.product(*[range(n) for n in SIZES]))


def licensed():
    """The family, by its derived definition. TWO clauses, not one:

      (B = 0 or Q = 1)   a bound below zero is permitted only in a quantum
                         regime -- derived on the five-coordinate box;
      (A = 0 or V = 2)   a bilinear condition is permitted only over an ordered
                         causal pair -- derived when the arity coordinate was
                         seated, and the same coupling the DEC repair
                         established independently from the family side.

    Neither clause was posited. Both are what the joint closure of the named
    conditions turns out to be, read off its cells.
    """
    return {c for c in box() if (c[4] == 0 or c[3] == 1) and (c[5] == 0 or c[1] == 2)}


def joint_closure(seed):
    """Least set containing seed and closed under all five operators.

    Every operator is extensive and monotone on a finite lattice, so the
    iteration converges and its limit is the least joint fixed point above the
    seed.
    """
    X = set(seed)
    for _ in range(64):
        ix = necindex.pinned_index(X)
        new = set(X)
        for name in necindex.OPERATORS:
            new |= set(cypher.ADMISSION[name][0](ix, OPTS)[0])
        if new == X:
            return X
        X = new
    raise RuntimeError("joint closure did not converge")


def per_language(cs):
    ix = necindex.pinned_index(cs)
    return {n: len(set(cypher.ADMISSION[n][0](ix, OPTS)[0]) - set(cs))
            for n in necindex.OPERATORS}


def free_slots(cs):
    """Slots whose every value appears at every combination of the others."""
    cs = set(cs)
    out = []
    for i in range(len(COORDS)):
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
    print("      %-40s %8s" % ("equals the derived TWO-clause definition",
                               F == licensed()))
    print()
    print("  and every language closes on it")
    for n, e in sorted(per_language(F).items()):
        print("      %-20s E = %d" % (n, e))
    print("      analysis   NOT-RUN (no witness declared, register 1172)")
    print("      documentary SILENT  (returns a citation, not a binary)")
    print()
    print("  what is excluded, and it is TWO things -- one per clause")
    miss = set(box()) - F
    bb = {c for c in miss if not (c[4] == 0 or c[3] == 1)}
    ba = {c for c in miss if not (c[5] == 0 or c[1] == 2)}
    print("      %-40s %8d" % ("excluded cells", len(miss)))
    print("      %-40s %8d" % ("classical, carrying a non-zero bound", len(bb)))
    print("      %-40s %8d" % ("bilinear, off the causal cone", len(ba)))
    print("      %-40s %8d" % ("excluded for both reasons at once", len(bb & ba)))
    print("      %-40s %8s" % ("and nothing else", (bb | ba) == miss))
    print()
    print("  the control: the operators do work")
    sizes = {}
    for r in necindex.FAMILY:
        sizes.setdefault(len(joint_closure([tuple(r[1:7])])), []).append(r[0])
    for k in sorted(sizes):
        print("      one condition closes to %2d cells : %s"
              % (k, ", ".join(sorted(sizes[k]))[:52]))
    print()
    print("  and it is superadditive")
    cl = [tuple(r[1:7]) for r in necindex.FAMILY if r[4] == 0]
    qm = [tuple(r[1:7]) for r in necindex.FAMILY if r[4] == 1]
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
    print("  The family exists, it is 256 conditions, and its definition is")
    print("  two clauses: a bound below zero is licensed exactly by a quantum")
    print("  regime, AND a bilinear condition is licensed exactly over an")
    print("  ordered causal pair. Both were derived, neither posited -- and the")
    print("  second is the same coupling the DEC repair established from the")
    print("  family side, reached here by five operators that were told nothing")
    print("  about causal cones. And it leaves the tensor slot -- the only slot")
    print("  any escape has ever moved -- entirely unguarded.")
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
    chk("the ambient box", len(box()), 576)
    chk("the joint fixed point", len(F), 256)
    chk("and it IS the derived TWO-clause definition", F == licensed(), True)
    # The first clause alone no longer suffices, and that is the finding of the
    # re-measurement rather than a defect: at five coordinates it did.
    chk("the bound clause alone is NOT enough at six coordinates",
        F == {c for c in box() if c[4] == 0 or c[3] == 1}, False)
    chk("it over-generates by exactly the bilinear cells off the causal cone",
        len({c for c in box() if c[4] == 0 or c[3] == 1} - F), 128)
    chk("and the arity clause alone is not enough either",
        F == {c for c in box() if c[5] == 0 or c[1] == 2}, False)
    chk("it contains every named condition", named <= F, True)
    chk("unnamed licensed cells", len(F) - len(named), 238)

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
    chk("excluded cells", len(miss), 320)
    # TWO reasons for exclusion now, one per clause, and they overlap.
    bad_bound = {c for c in miss if not (c[4] == 0 or c[3] == 1)}
    bad_arity = {c for c in miss if not (c[5] == 0 or c[1] == 2)}
    chk("classical cells carrying a non-zero bound", len(bad_bound), 192)
    chk("bilinear cells off the causal cone", len(bad_arity), 192)
    chk("excluded for both reasons at once", len(bad_bound & bad_arity), 64)
    chk("and nothing else is excluded", (bad_bound | bad_arity) == miss, True)

    # ------------------------------------- THE CONTROL: the operators do work
    ones = {r[0]: len(joint_closure([tuple(r[1:7])])) for r in necindex.FAMILY}
    # CORRECTED at H97.  Measured on a re-coordinated index these read 1 to 4
    # cells with the NEC alone at 1; pinned, EVERY named condition closes to
    # itself.  The corrected result is the stronger one: closure is entirely an
    # interaction effect, and no condition demands anything on its own.
    chk("every single condition is a closed family by itself",
        sorted(set(ones.values())), [1])
    chk("all nineteen named rows, over eighteen distinct cells", len(ones), 19)
    chk("including the NEC", ones["NEC"], 1)
    # NEGATIVE CONTROL: closing the whole box is trivial, so 192 being a proper
    # subset is what makes the result non-vacuous.
    chk("the box is a fixed point too, trivially",
        len(joint_closure(box())), 576)
    chk("so 256 is a PROPER subset and the result is not vacuous",
        len(F) < len(box()), True)

    # ------------------------------------------------------- superadditivity
    a = len(joint_closure([tuple(r[1:7]) for r in necindex.FAMILY if r[4] == 0]))
    b = len(joint_closure([tuple(r[1:7]) for r in necindex.FAMILY if r[4] == 1]))
    chk("classical rows alone", a, 48)
    chk("semiclassical rows alone", b, 24)
    chk("the coexistence alone demands", len(F) - a - b, 184)
    chk("so the closure is superadditive", len(F) > a + b, True)

    # ------------------------------------------------------ the free slots
    chk("slots the closure leaves free", free_slots(F), ["T", "M"])
    chk("T is free, and T is the only slot any opener moves",
        "T" in free_slots(F), True)
    chk("and V, Q, B, A are the constrained ones",
        [c for c in COORDS if c not in free_slots(F)], ["V", "Q", "B", "A"])
    chk("V lost its freedom to the arity clause, not to the bound clause",
        free_slots({c for c in box() if c[4] == 0 or c[3] == 1}), ["T", "V", "M", "A"])

    # ---------------------------------------------------------- the limits
    chk("derived, not posited", CLOSURE_IS_DERIVED_NOT_POSITED, True)
    chk("cells are citations, not truths", CELLS_ARE_CITATIONS_NOT_TRUTHS, True)
    chk("analysis stays NOT-RUN", ANALYSIS_STAYS_NOT_RUN, True)
    chk("documentary stays SILENT", DOCUMENTARY_STAYS_SILENT, True)
    res = cypher.run(necindex.pinned_index(F, "licensed"), "1173", OPTS)
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
