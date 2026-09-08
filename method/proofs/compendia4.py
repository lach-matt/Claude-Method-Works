r"""compendia4.py — successor to compendia3.py: the Spectra Compendium after the narrow relabel.

WHY IT SUPERSEDES.  `compendia3.py` is HELD and is not edited.  Two of its fixtures measure a
state W-299's relabel replaced:
  * it pins `("Ba III", "nd 2[3/2]* J=2")` as the label printed at two limits, and after the
    relabel that label is printed at NEITHER -- the two rows now name different parents;
  * it pins the short-key duplicate count at nine, which is now TEN, and the reason is the
    point of the whole pass rather than an accident of it.

WHAT THE RELABEL DID.  M ruled the narrow option -- relabel only where the parent is genuinely
ambiguous -- and then one uniform style.  Ambiguity needs TWO LIMITS IN ONE SPECIES AND A ROW
THAT NAMES NO PARENT, which is Ba III 12, Ne II 37, Si I 14 and Ne I 3: sixty-six rows, all
taking the dotted full-configuration form.  Rows naming a parent moved 73 -> 139.

AND IT MADE TWO HIDDEN PAIRS VISIBLE, WHICH IS WHY THE SHORT-KEY COUNT ROSE RATHER THAN FELL.
Ba III `nd 2[3/2]* J=2` LEFT the duplicate list.  In its place two pairs ENTERED, both Ba III
and both under one parent: `nd 2[3/2]* J=2` at n = 5-7 and 8-22, and `ns 2[3/2]* J=1` at
n = 6-8 and 9-23.  Each is one channel fitted in two adjacent n-windows -- delta drifting
toward its asymptote across the join, the earlier row bracketed and the later untested.  THE
BARE LABELS HID THAT THE TWO HALVES SHARED A PARENT.  On the key M ruled, (species, series,
n-range), the count is unchanged at two.

THE NOTATION DUPLICATES, MEASURED RATHER THAN ASSERTED.  Normalise a label by removing its
parent prefix and folding superscript typography, and a repeat on (species, series, n-range)
is ONE SERIES PRINTED TWICE.  Over all 596 rows there are exactly FOUR, all Ar II, and
register 815's withdrawal already names them: "the same series from two capture files".  They
agree in n-range, levels, interior, n* range, delta to four decimals, fits and limit, and
differ in notation, in bracket (1/1 against untested) and in sigma(delta), which the later row
prints 2.26-2.45x smaller in all four.  THE TEST FINDS NO FIFTH: eight groups share
(species, n-range, delta, J), and the other four are degenerate TERMS -- B V and Be IV's
np 2P*/ns 2S, C V and Mg I's singlet/triplet nf F* -- which are not duplicates at all.

AR II IS NOT AN AMBIGUOUS SPECIES AND WAS RIGHTLY LEFT OUT.  All 44 of its rows carry one
limit, so no Ar II row is ambiguous about its parent.  Had the wide relabel run, those four
pairs would have become BYTE-IDENTICAL rows.

WHAT IT REFUSES.  It does not repair the four, it does not choose between the two Si I rows
nothing printed separates, and it does not touch the three species whose two limits differ by
less than a wavenumber.  Each is a reading of the material and each is M's.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compendia3 as C3           # seated member, imported and never copied

SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹°", "0123456789*")
PREFIX = re.compile(r"^(?:[0-9a-z.]*\.)?\([^)]*\)\.?")
DOTTED = re.compile(r"^\S*\.\(.*?\)\.")      # compendia3's own PARENT test
AMBIGUOUS_SPECIES = ("Ba III", "Ne II", "Si I", "Ne I")


def rows():
    """The channel table, from compendia3's own reader."""
    return C3.spectra_rows()[1]


def species(c):
    return c[0].replace("*", "").strip()


def normalise(label):
    """Strip the parent prefix and fold superscripts: what the series IS, not how it prints."""
    return re.sub(r"\s+", " ", PREFIX.sub("", label).translate(SUP)).strip()


def by_species():
    g = collections.defaultdict(list)
    for i, c in rows():
        g[species(c)].append((i, c))
    return g


def two_limit_species():
    """Species carrying more than one limit, split by how far apart the limits are."""
    parents, roundings = [], []
    for k, v in sorted(by_species().items()):
        lims = sorted({c[10] for i, c in v})
        if len(lims) < 2:
            continue
        f = sorted(float(x.replace(",", "")) for x in lims)
        (roundings if f[-1] - f[0] < 1 else parents).append((k, lims, f[-1] - f[0]))
    return parents, roundings


def bare(sp=None):
    return [(i, c) for i, c in rows()
            if "(" not in c[1] and (sp is None or species(c) == sp)]


def notation_duplicates():
    """One series printed twice: same species and n-range, same series once normalised."""
    g = collections.defaultdict(list)
    for i, c in rows():
        g[(species(c), normalise(c[1]), c[2])].append((i, c))
    return {k: v for k, v in g.items()
            if len(v) > 1 and len({x[1][1] for x in v}) > 1}


def window_pairs():
    """Same species, series and limit, adjacent n-windows: one channel fitted twice."""
    g = collections.defaultdict(list)
    for i, c in rows():
        g[(species(c), c[1], c[10])].append((i, c))
    return {k: v for k, v in g.items() if len(v) > 1}


def report():
    print("compendia4 -- the Spectra Compendium after the narrow relabel")
    print("=" * 78)
    print()
    d = rows()
    print("1  THE TABLE, AND WHAT THE RELABEL MOVED")
    print("   data rows                                       %d" % len(d))
    print("   rows naming a parent (any parenthesised form)   %d   <- was 73"
          % sum(1 for i, c in d if "(" in c[1]))
    print("   the same by compendia3's dotted test            %d   <- it does not see"
          % sum(1 for i, c in d if DOTTED.match(c[1])))
    print("        `(3P)ns 4P J=5/2` or `2s22p5(2P*3/2)nd ...`, so it UNDERCOUNTS")
    print("   duplicated on (species, series) -- the short key %d   <- was 9"
          % len(C3.duplicated_keys(n_in_key=False)))
    print("   duplicated on M's key, with the n-range          %d   <- unchanged"
          % len(C3.duplicated_keys()))
    print()
    print("2  THE FOUR SPECIES WHOSE TWO LIMITS ARE TWO PARENTS")
    parents, roundings = two_limit_species()
    for k, lims, gap in parents:
        print("   %-8s %-30s gap %10.3f cm-1   bare rows now %d"
              % (k, " / ".join(lims), gap, len(bare(k))))
    print()
    print("3  AND THE THREE WHOSE TWO LIMITS ARE ONE LIMIT AT TWO ROUNDINGS")
    for k, lims, gap in roundings:
        print("   %-8s %-30s gap %10.3f cm-1" % (k, " / ".join(lims), gap))
    print("   NOT a parent case, and not touched by the relabel.")
    print()
    print("4  ONE SERIES PRINTED TWICE -- register 815's capture-file class")
    for k, v in sorted(notation_duplicates().items()):
        print("   %-8s %-24s n=%s" % k)
        for i, c in v:
            print("      L%-5d %-34s bracket %-9s sigma %s" % (i, c[1], c[5], c[8]))
    print("   Recorded, not repaired.")
    print()
    print("5  THE TWO PAIRS THE RELABEL MADE VISIBLE")
    for k, v in sorted(window_pairs().items()):
        if k[0] != "Ba III":
            continue
        print("   %-8s %-40s" % (k[0], k[1]))
        for i, c in v:
            print("      L%-5d n=%-8s delta %-9s bracket %s" % (i, c[2], c[7], c[5]))


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    d = rows()
    chk("channel table data rows", len(d), 596)
    chk("rows naming a parent -- was 73", sum(1 for i, c in d if "(" in c[1]), 139)
    chk("compendia3's dotted test undercounts it", sum(1 for i, c in d if DOTTED.match(c[1])), 80)
    chk("duplicated on the short key -- compendia3 pins 9",
        len(C3.duplicated_keys(n_in_key=False)), 10)
    chk("duplicated on M's ruled key -- unchanged", len(C3.duplicated_keys()), 2)

    parents, roundings = two_limit_species()
    chk("species whose two limits are two parents",
        [k for k, l, g in parents], ["Ba III", "Ne I", "Ne II", "Si I"])
    chk("and every one of them now has no bare row",
        [len(bare(k)) for k, l, g in parents], [0, 0, 0, 0])
    chk("bare rows in those four before the relabel: 12 + 37 + 14 + 3",
        12 + 37 + 14 + 3, 66)
    chk("species whose two limits are one limit at two roundings",
        [k for k, l, g in roundings], ["Ca II", "Li I", "Zn I"])
    chk("and none of their gaps reaches a wavenumber",
        [round(g, 3) for k, l, g in roundings], [0.010, 0.036, 0.020])
    chk("Ar II carries ONE limit, so no Ar II row was ambiguous",
        len({c[10] for i, c in rows() if species(c) == "Ar II"}), 1)

    N = notation_duplicates()
    chk("one series printed twice, over the whole table", len(N), 4)
    chk("and every one is Ar II", sorted({k[0] for k in N}), ["Ar II"])
    chk("each pair is one bracketed row and one untested",
        sorted({tuple(sorted(x[1][5] for x in v)) for v in N.values()}),
        [("1/1", "untested")])
    chk("and their deltas agree exactly",
        [len({x[1][7] for x in v}) for v in N.values()], [1, 1, 1, 1])
    chk("while sigma(delta) does not",
        [len({x[1][8] for x in v}) for v in N.values()], [2, 2, 2, 2])

    W = {k: v for k, v in window_pairs().items() if k[0] == "Ba III"}
    chk("Ba III channels the relabel showed to be fitted in two n-windows", len(W), 2)
    chk("and their n-ranges are adjacent, not overlapping",
        sorted(tuple(sorted(x[1][2] for x in v)) for v in W.values()),
        [("5–7", "8–22†"), ("6–8", "9–23")])
    chk("the label compendia3 pins is now printed at neither limit",
        [i for i, c in rows() if c[1] == "nd 2[3/2]* J=2"], [])

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a = a.parse_args()
    selftest() if a.selftest else report()
