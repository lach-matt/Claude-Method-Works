#!/usr/bin/env python3
r"""
probability.py -- THE PROBABILITY INDEX: one distribution over the twenty-five
subshells, read three ways, and every row of it sums to one.

M: "I wonder if any missing vertex might contain ... an index of probabilities."

    python3 probability.py             the reading
    python3 probability.py --selftest  fixtures

===============================================================================
0. BUILT BEFORE THE DEMAND TABLE WAS READ
===============================================================================

The same discipline as `inversion.py`: an index built to land on a cell
`demand.py` wants would be fitted, and a fitted vertex closes nothing.  The
construction below is fixed by the question -- what is the probability
distribution of the differentiating electron's address -- and section 5 reports
where it lands whichever way that goes.

===============================================================================
1. THERE IS ONE DISTRIBUTION HERE, AND IT IS ALREADY BANKED
===============================================================================

Draw an element uniformly from the seated reach of 170 and ask which subshell its
differentiating electron went into.  That is a probability distribution over the
twenty-five subshells and it needs no modelling: the counts are
`fibred.addresses()`, already measured, already seated.

    THE MEMBERS ARE SUBSHELLS, NOT ELEMENTS.  That is what makes this a different
    index and not a re-chart of `fibred.py`: twenty-five members against a
    hundred and seventy, and coordinates that are probabilities rather than
    quantum numbers.

===============================================================================
2. THE THREE COORDINATES ARE ONE DISTRIBUTION AND TWO CONDITIONALS
===============================================================================

        p     P(subshell)                  the marginal
        p_n   P(subshell | shell = n)      conditioned on the shell
        p_s   P(subshell | n + l = s)      conditioned on the Madelung group

    NOT THREE DISTRIBUTIONS -- ONE, CONDITIONED ON THE TWO BASES THE TREE
    ALREADY CHARTS.  `fibred.py` fibres the elements over n; `madelung.py` fibres
    them over n+l.  p_n and p_s are exactly those two fibrations read as
    conditionals, which is why these three and not some other three.

    EVERY ROW SUMS TO ONE AND `normalisation()` CHECKS IT.  p over all twenty-five
    subshells, p_n over each shell, p_s over each Madelung group.  A probability
    index whose rows do not normalise is not a probability index, and the check
    is cheap, so it is a fixture rather than a remark.

    THE COUNTS ARE OBSERVED, NOT CAPACITIES -- AND AT THIS REACH THEY COINCIDE.
    A subshell's count is how many elements actually differentiated into it, and
    this file was written expecting the final group to be cut short.  IT IS NOT.
    `truncation()` returns EMPTY at 170: the seated reach lands exactly on a
    Madelung shell boundary, so every subshell it touches is full and the count
    IS the capacity 2(2l+1).

    THAT COSTS THE MARGINAL ITS INDEPENDENCE, AND THE COST IS REPORTED RATHER
    THAN HIDDEN.  With no truncation, p = 2(2l+1)/N is a function of l alone --
    five values, one per capacity, and nothing a reader could not have computed
    from l.  `dependence()` measures it: p separates 5, l separates 5, and
    p is constant on l.  The two conditionals are NOT functions of l
    (`dependence()` again), so the index is not thereby a re-chart of l; but
    the marginal alone is, and the docstring said otherwise before the fixtures
    were run.

    AND p_n DETERMINES p.  Measured, not designed: the pair (p, p_n) separates
    exactly as many subshells as p_n does alone, so p adds nothing to it.  The
    triple is still faithful -- all twenty-five separate -- because p_s is
    independent of both.  An earlier draft of this file asserted the opposite,
    that p_n does not determine p, and the fixture refuted it.

===============================================================================
3. THE CHART CRITERION, MEASURED
===============================================================================

DOCKET 3, run in `criterion()`.  The reading in section 5 is void if any
coordinate moves.  Real-valued coordinates need no banding, for the reason
`entropy.py` gives: hlaw takes the OBSERVED alphabet as its chain, so the chain
here is simply the distinct probabilities.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

To call p a physical probability.  It is the distribution induced by drawing an
ELEMENT uniformly, which is a counting convention and not a statement about
nature.  A different measure on elements gives a different index, and nothing in
the corpus rules on one.

To smooth a truncated shell.  There is none at this reach, which is itself the
finding above; at a reach that does cut a group short, `truncation()` names the
subshells and nothing is adjusted.

To claim independence.  No factorisation is asserted, and the one dependence
there is -- p_n determines p -- was found by a fixture refuting the opposite
claim, not by design.  It is left standing in the index because dropping p
would make the chart a two-coordinate one and that is a different object.
"""

import collections
import sys

import fibred
import hlaw
import mi

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    "COMPUTED from fibred.py's Madelung construction; no table is read.",
    (),
)


REACH = fibred.REACH                        # 170
PLACES = 12


def counts(reach=REACH):
    """({(n,l): count}, {n: count}, {n+l: count}, total) -- all observed."""
    A = fibred.addresses(reach)
    sub = collections.Counter((n, l) for n, l, _k in A.values())
    byn = collections.Counter(n for n, _l, _k in A.values())
    bys = collections.Counter(n + l for n, l, _k in A.values())
    return dict(sub), dict(byn), dict(bys), len(A)


def probabilities(reach=REACH):
    """{(n,l): (p, p_n, p_s)} -- the marginal and the two conditionals."""
    sub, byn, bys, N = counts(reach)
    return {(n, l): (round(c / N, PLACES),
                     round(c / byn[n], PLACES),
                     round(c / bys[n + l], PLACES))
            for (n, l), c in sub.items()}


def index(reach=REACH):
    """The probability index as a set of cells."""
    return frozenset(probabilities(reach).values())


def normalisation(reach=REACH):
    """(marginal sum, {n: sum}, {s: sum}) -- every one must be 1."""
    sub, byn, bys, N = counts(reach)
    tot = round(sum(c / N for c in sub.values()), 9)
    pn = {n: round(sum(c / byn[nn] for (nn, _l), c in sub.items() if nn == n), 9)
          for n in sorted(byn)}
    ps = {s: round(sum(c / bys[nn + l] for (nn, l), c in sub.items()
                       if nn + l == s), 9) for s in sorted(bys)}
    return tot, pn, ps


def truncation(reach=REACH):
    """[(subshell, observed, capacity)] where the reach cut a subshell short."""
    sub, _byn, _bys, _N = counts(reach)
    return [((n, l), c, 2 * (2 * l + 1)) for (n, l), c in sorted(sub.items())
            if c != 2 * (2 * l + 1)]


def faithful(reach=REACH):
    """(members, distinct cells) -- whether the chart forgets a subshell."""
    return len(probabilities(reach)), len(index(reach))


def dependence(reach=REACH):
    """({coordinate set: distinct values}) -- what each projection can tell apart.

    If p_n alone determined p, the pair would have as many distinct values as
    p_n does.  It does not, and that is the entry.
    """
    P = list(probabilities(reach).values())
    out = {}
    for nm, sel in (("p", (0,)), ("p_n", (1,)), ("p_s", (2,)),
                    ("p,p_n", (0, 1)), ("p_n,p_s", (1, 2)),
                    ("p,p_n,p_s", (0, 1, 2))):
        out[nm] = len({tuple(t[i] for i in sel) for t in P})
    return out


def determines(reach=REACH):
    """{(a, b): does a determine b} over the three coordinates and l.

    a determines b iff the pair separates no more than a alone.  Measured, and
    it is how the p_n -> p dependence was found -- by a fixture asserting the
    opposite and failing.
    """
    pr = probabilities(reach)
    col = {"p": lambda s, t: t[0], "p_n": lambda s, t: t[1],
           "p_s": lambda s, t: t[2], "l": lambda s, t: s[1]}
    out = {}
    for a in col:
        for b in col:
            if a == b:
                continue
            va = {col[a](s, t) for s, t in pr.items()}
            vab = {(col[a](s, t), col[b](s, t)) for s, t in pr.items()}
            out[(a, b)] = len(va) == len(vab)
    return out


def criterion(reach=REACH):
    """{coordinate: moves under a monotone redundant append}.  DOCKET 3."""
    X = index(reach)
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def closers(reach=REACH):
    X = index(reach)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


def reach_control(reaches=None):
    """[(reach, subshells, cells, K)] -- the reach dependence, shown."""
    out = []
    for r in (reaches or (18, 36, 54, 86, 118, 170)):
        X = index(r)
        out.append((r, len(probabilities(r)), len(X), mi.K(X) if X else None))
    return out


# ---------------------------------------------------------------------------

def report():
    P = probabilities()
    print("=" * 74)
    print("THE PROBABILITY INDEX -- one distribution over the subshells,")
    print("read three ways")
    print("=" * 74)
    print()
    print("1. THE MEMBERS AND THE MEASURE.")
    _sub, _byn, _bys, N = counts()
    print("   elements drawn from   %d  (uniform -- a counting convention, and" % N)
    print("                             this file refuses to call it more)")
    print("   subshells             %d" % len(P))
    m, k = faithful()
    print("   distinct cells        %d   %s"
          % (k, "FAITHFUL -- no subshell is lost" if k == m else
             "%d collide" % (m - k)))
    print()
    print("2. NORMALISATION -- the check that makes it a probability index.")
    tot, pn, ps = normalisation()
    print("   sum over all subshells      %.9f" % tot)
    print("   sum within each shell n     %s"
          % ("all 1.0" if set(pn.values()) == {1.0} else pn))
    print("   sum within each group n+l   %s"
          % ("all 1.0" if set(ps.values()) == {1.0} else ps))
    print()
    print("3. THE FIRST EIGHT SUBSHELLS.")
    print("   %-10s %-12s %-12s %s" % ("subshell", "p", "p_n", "p_s"))
    for s in sorted(P)[:8]:
        p, a, b = P[s]
        print("   %-10s %-12.6f %-12.6f %.6f" % (str(s), p, a, b))
    print()
    print("4. TRUNCATION, NAMED RATHER THAN SMOOTHED.")
    tr = truncation()
    if not tr:
        print("   NONE at this reach -- 170 lands exactly on a Madelung shell")
        print("   boundary, so every subshell it touches is full. This file was")
        print("   written expecting otherwise; see section 5 for what it costs.")
        print("   At reach 100 there are %d truncated subshells."
              % len(truncation(100)))
    for s, obs, cap in tr:
        print("   %-10s observed %-4d capacity %d" % (str(s), obs, cap))
    print()
    print("5. WHAT EACH PROJECTION CAN TELL APART, AND WHAT DETERMINES WHAT.")
    for nm, v in dependence().items():
        print("   %-12s %2d distinct" % (nm, v))
    det = determines()
    yes = sorted("%s -> %s" % ab for ab, v in det.items() if v)
    print("   determines:  %s" % (", ".join(yes) or "nothing"))
    print("   -- p_n DETERMINES p, and l determines p because the reach is")
    print("      complete. Neither conditional is a function of l, so the index")
    print("      is not a re-chart of l; the marginal alone is.")
    print()
    print("6. THE CHART CRITERION (DOCKET 3).")
    crit = criterion()
    for nm, moved in sorted(crit.items()):
        print("   %-8s moves on %d   %s"
              % (nm, moved, "ADMISSIBLE" if not moved else "DISQUALIFIED"))
    if any(crit.values()):
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print()
    print("7. WHERE IT LANDS -- measured, reported whichever way it goes.")
    print("   closes in   %s" % (", ".join(closers()) or "nothing"))
    print("   CELL        %s" % (cell(),))
    try:
        import demand
        import figure as _fig
        if cell() in demand.demand(_fig.figure()):
            print("   AND THAT CELL IS ONE THE OCTAD DEMANDS.  E drops by one.")
        else:
            print("   THAT CELL IS NOT DEMANDED BY THE OCTAD.  Seating it raises E.")
    except Exception as exc:                       # pragma: no cover
        print("   (demand.py not consulted: %s)" % exc)
    print()
    print("8. THE REACH DEPENDENCE.")
    print("   %-8s %-11s %-8s %s" % ("reach", "subshells", "cells", "K"))
    for r, m2, c, k2 in reach_control():
        print("   %-8d %-11d %-8d %s" % (r, m2, c, k2))
    print()
    print("9. REFUSED: to call p physical -- it is induced by a uniform draw on")
    print("   ELEMENTS, a convention the corpus does not rule on. To smooth the")
    print("   truncated group. To assert any factorisation: section 5 measures")
    print("   the dependence and finds none to assert.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    _sub, _byn, _bys, N = counts()
    chk("the reach is the seated one", N, 170)
    chk("subshells", len(probabilities()), 25)
    m, k = faithful()
    chk("the chart is faithful -- no subshell lost", m == k, True)
    chk("distinct cells", k, 25)
    tot, pn, ps = normalisation()
    chk("the marginal sums to one", tot, 1.0)
    chk("every shell's conditional sums to one", set(pn.values()), {1.0})
    chk("every Madelung group's sums to one", set(ps.values()), {1.0})
    chk("there are nine shells", len(pn), 9)
    chk("there are nine Madelung groups", len(ps), 9)
    chk("every probability is in (0, 1]",
        all(0 < x <= 1 for t in index() for x in t), True)
    chk("1s is certain within its shell", probabilities()[(1, 0)][1], 1.0)
    chk("and within its group", probabilities()[(1, 0)][2], 1.0)
    dep = dependence()
    chk("p alone separates five", dep["p"], 5)
    chk("p_n separates more than p", dep["p_n"] > dep["p"], True)
    chk("the triple separates everything", dep["p,p_n,p_s"], 25)
    chk("p_n DETERMINES p -- measured, and the opposite was asserted first",
        dep["p,p_n"], dep["p_n"])
    det = determines()
    chk("p_n determines p", det[("p_n", "p")], True)
    chk("l determines p -- the reach is complete, so p is a formula in l",
        det[("l", "p")], True)
    chk("l does NOT determine p_n", det[("l", "p_n")], False)
    chk("l does NOT determine p_s", det[("l", "p_s")], False)
    chk("p does not determine p_n", det[("p", "p_n")], False)
    crit = criterion()
    chk("K admissible", crit["K"], 0)
    chk("height admissible", crit["height"], 0)
    chk("width admissible", crit["width"], 0)
    chk("closes in statistics alone", closers(), ["statistics"])
    chk("the cell is a 3-tuple", len(cell()), 3)
    chk("height and width bound the size",
        max(cell()[1], cell()[2]) <= len(index()) <= cell()[1] * cell()[2], True)
    chk("NO truncation at this reach -- it lands on a shell boundary",
        truncation(), [])
    chk("and a shorter reach does truncate", len(truncation(100)) >= 1, True)
    rc = reach_control()
    chk("the reach control has rows", len(rc), 6)
    chk("subshells are monotone in reach",
        all(rc[i][1] <= rc[i + 1][1] for i in range(len(rc) - 1)), True)
    print("probability selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
