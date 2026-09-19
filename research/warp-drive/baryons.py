#!/usr/bin/env python3
r"""
baryons.py -- THE BARYONS, CHARTED ON SPIN, PARITY, ISOSPIN, CHARGE AND ALL
THREE FLAVOUR NUMBERS.  DOCKET 27.

    python3 baryons.py             the reading
    python3 baryons.py --selftest  fixtures

===============================================================================
1. THE MEMBERS
===============================================================================

One member is a baryon in the PDG table: 292 of them, antibaryons counted
separately for the reason `fundamental.py` section 1 gives.  Read from
`captures/PDG-2026.tsv`; `pdgcapture.py` is the provenance.

    FOURTEEN ARE NAMED AND SET ASIDE, not silently dropped.  PDG reports no
    parity for the Xi(1690), Xi(1950), Xi(2030) and Omega(2250) states and
    their antiparticles, so a chart carrying P cannot place them.
    `unplaced()` lists them.  A gap in the TABLE, not in physics.  278 members
    are charted.

===============================================================================
2. THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN
===============================================================================

    2J    spin, doubled.  Every baryon is a fermion, so 2J is odd.
    P     parity, +1 or -1.
    2I    isospin, doubled: 0, 1, 2 or 3.
    Q3    electric charge in thirds: -6, -3, 0, +3, +6.
    S     strangeness.
    C     charm.
    B     beauty.

    THE THREE FLAVOUR NUMBERS ARE CHARTABLE HERE AND WERE NOT FOR THE MESONS,
    and that contrast is the reason they are declared.  All 292 baryon quark
    contents are plain strings of quark letters, so `mesons.flavour()` parses
    every one; 59 of the 250 meson contents are mixtures and two of those --
    K(L)0 and K(S)0 -- have no strangeness to read at all.  A baryon is never
    a flavour mixture in this table.

    THE CASE CONVENTION IS INHERITED, NOT RE-DERIVED.  `mesons.flavour()` is
    imported rather than copied, and it pins lowercase as the quark against
    six named states.  An instrument imports; it does not reimplement.

    WHAT IS REFUSED:

    C-PARITY AND G-PARITY are not coordinates and could not be: the table
    prints neither for ANY baryon, all 292 of 292.  That is not a gap -- C and
    G are eigenvalues of operations under which no baryon is invariant, since
    conjugating a baryon gives an antibaryon.  `cg_absent()` checks that the
    table agrees, and it is the cleanest totality refusal in this tree: not
    "mostly missing" but missing without exception.

    BARYON NUMBER is not a coordinate.  It is +1 on every particle here and -1
    on every antiparticle, so as a column it would be the sign of the PDG id
    written twice -- a relabelling, which is what the overlap ruling's second
    ground refuses.  `baryon_number_is_the_sign()` measures it.

    MASS AND WIDTH are reported and not charted, as in `mesons.py`.

===============================================================================
3. CHARM AND BEAUTY EARN THEIR PLACE JOINTLY, NOT SEPARATELY
===============================================================================

Measured after the chart was run, and reported because a coordinate that adds
nothing is over-representation:

    all seven                     184 cells
    drop charm only               184 cells -- adds nothing alone
    drop beauty only              184 cells -- adds nothing alone
    drop BOTH charm and beauty    178 cells -- six cells lost

Either one alone is a function of the other six on these 278 members; the two
together are not.  So neither is dropped, and the declaration in section 2
stands on a measurement rather than on the fact that it was made first.  The
redundancy of each alone is a property of THE TABLE, not of baryons: charm
takes all three of -1, 0, +1 here and simply never separates two members that
(2J, P, 2I, Q3, S, B) had already merged.

===============================================================================
4. CONJUGATION SPLITS EVERY PAIR, AND THE MESONS' DOES NOT
===============================================================================

All 139 conjugate pairs are split by this chart, with no exception, and the
mechanism is uniform: 2J and 2I are invariant, and P, Q3, S, C and B ALL
negate.

    THE PARITY FLIP IS THE INTERESTING ONE.  A fermion and its antifermion
    carry OPPOSITE intrinsic parity -- the neutron is P = +1 and the
    antineutron P = -1 in this very table -- while a meson and its antimeson
    carry the SAME parity, because a meson is a boson.  So `mesons.py` finds
    28 of its 79 pairs collided (the neutral ones, which only Q3 could have
    separated) and this file finds none: here parity separates a pair even
    when every charge on it is zero.  Two indexes, one operation, opposite
    answers, and the difference is spin-statistics.
"""

import sys

import hlaw
import mesons
import mi
import pdgcapture

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    '"Review of Particle Physics", Particle Data Group, Int. J. Mod. Phys. A 41, 2630011 (2026), via the `particle` package -- see pdgcapture.py',
    (
        'research/warp-drive/captures/PDG-2026.tsv',
    ),
)


NAMES = ("2J", "P", "2I", "Q3", "S", "C", "B")
ARITY = len(NAMES)
FAMILY = "baryon"

_C = {}


def all_rows():
    """Every baryon in the capture: [(name, pdgid, 2J, P, 2I, Q3, S, C, B)],
    with P None where the table prints none."""
    if "a" not in _C:
        out = []
        for r in pdgcapture.read():
            if r["family"] != FAMILY:
                continue
            f = mesons.flavour(r["quarks"])
            if f is None:
                raise AssertionError(
                    "a baryon quark content did not parse: %s %s"
                    % (r["name"], r["quarks"]))
            out.append((r["name"], int(r["pdgid"]), int(r["J2"]),
                        None if r["P"] == "?" else int(r["P"]),
                        int(r["I2"]), int(r["Q3"])) + f)
        _C["a"] = sorted(out, key=lambda t: (t[2], t[4], t[5], t[1]))
    return _C["a"]


def unplaced():
    """[name] -- section 1's fourteen, no parity printed."""
    return sorted(n for n, _p, _j, P, *_x in all_rows() if P is None)


def rows():
    """The 278 charted: [(name, pdgid, 2J, P, 2I, Q3, S, C, B)]."""
    return [t for t in all_rows() if t[3] is not None]


def index():
    return frozenset(t[2:] for t in rows())


def cg_absent():
    """(baryons, with a C printed, with a G printed) -- section 2's refusal.

    Expected (292, 0, 0).  Not "mostly missing": missing without exception.
    """
    n = c = g = 0
    for r in pdgcapture.read():
        if r["family"] != FAMILY:
            continue
        n += 1
        c += r["C"] != "?"
        g += r["G"] != "?"
    return (n, c, g)


def baryon_number_is_the_sign():
    """(agree, disagreements) -- A = +1 iff the PDG id is positive.

    Section 2's relabelling refusal, measured.  Baryon number is derived here
    from the quark content -- three quarks is A = +1, three antiquarks -1 --
    and compared against the sign of the id, so the two are independent
    derivations and the check is not circular.
    """
    by = {int(r["pdgid"]): r["quarks"]
          for r in pdgcapture.read() if r["family"] == FAMILY}
    bad = []
    for pid, q in by.items():
        nq = sum(1 if ch.islower() else -1 for ch in q)
        A = nq // 3
        if A != (1 if pid > 0 else -1):
            bad.append((pid, q, A))
    return (not bad, sorted(bad))


def axis_contributions():
    """[(dropped axis name or None, cells)] -- section 3's table."""
    X = [t[2:] for t in rows()]
    out = [(None, len(set(X)))]
    for i, nm in enumerate(NAMES):
        out.append((nm, len({tuple(v for j, v in enumerate(t) if j != i)
                             for t in X})))
    out.append(("C and B", len({t[:5] for t in X})))
    return out


def conjugation():
    """(pairs, collided, split, the mechanism as a per-coordinate verdict).

    The mechanism is [(name, "invariant"|"negates"|"MIXED")] over every pair
    in the table, so section 4's claim is checked and not asserted.
    """
    c = {t[1]: t[2:] for t in rows()}
    same = split = 0
    inv = [True] * ARITY
    neg = [True] * ARITY
    for pid in c:
        if pid < 0 or -pid not in c:
            continue
        a, z = c[pid], c[-pid]
        if a == z:
            same += 1
        else:
            split += 1
        for i in range(ARITY):
            inv[i] &= a[i] == z[i]
            neg[i] &= a[i] == -z[i]
    mech = [(NAMES[i], "invariant" if inv[i] else
             "negates" if neg[i] else "MIXED") for i in range(ARITY)]
    return (same + split, same, split, mech)


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def report():
    X = index()
    print("=" * 74)
    print("THE BARYONS -- the PDG table, charted")
    print("=" * 74)
    print()
    print("1. THE MEMBERS.")
    print("   in the table   %d" % len(all_rows()))
    print("   set aside      %d, no parity printed" % len(unplaced()))
    for n in unplaced():
        print("                  %s" % n)
    print("   charted        %d" % len(rows()))
    print()
    print("2. THE CHART on %s." % (", ".join(NAMES)))
    print("   cells    %d of %d members" % (len(X), len(rows())))
    print("   cell     %s" % (cell(),))
    print("   closes   %s" % (", ".join(closers()) or "NOTHING"))
    print()
    n, c, g = cg_absent()
    print("3. C AND G ARE ABSENT WITHOUT EXCEPTION.")
    print("   %d baryons, %d with a C printed, %d with a G" % (n, c, g))
    print("   Conjugating a baryon gives an antibaryon, so no baryon is an")
    print("   eigenstate of either operation.  The table agrees exactly.")
    print()
    ok, bad = baryon_number_is_the_sign()
    print("4. BARYON NUMBER IS THE SIGN OF THE ID: %s" % ok)
    print("   so charting it would be a relabelling, and the overlap ruling's")
    print("   second ground refuses one.  %d disagreements." % len(bad))
    print()
    print("5. WHAT EACH COORDINATE CONTRIBUTES.")
    for nm, k in axis_contributions():
        print("   %-16s %d cells" % ("all seven" if nm is None
                                     else "drop " + nm, k))
    print("   Charm alone and beauty alone each add nothing; the two together")
    print("   add six cells.  Neither is dropped.")
    print()
    pairs, same, split, mech = conjugation()
    print("6. CONJUGATION SPLITS EVERY PAIR.")
    print("   %d pairs: %d split, %d collided" % (pairs, split, same))
    for nm, v in mech:
        print("   %-6s %s" % (nm, v))
    print("   P NEGATES -- a fermion and its antifermion carry opposite")
    print("   intrinsic parity.  mesons.py collides 28 of its 79 pairs because")
    print("   a meson is a boson and its parity does not flip.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    A = all_rows()
    R = rows()
    chk("292 baryons in the table", len(A), 292)
    chk("fourteen carry no parity and are set aside", len(unplaced()), 14)
    chk("and they are the Xi and Omega excited states, with antiparticles",
        sorted({n.split("(")[0].replace("~", "") for n in unplaced()}),
        ["Omega", "Xi"])
    chk("278 charted", len(R), 278)

    # the quantum numbers, against the physics
    chk("every baryon is a fermion -- 2J is odd",
        sorted({t[2] % 2 for t in A}), [1])
    chk("and the spins tabled are 1/2 through 7/2",
        sorted({t[2] for t in A}), [1, 3, 5, 7])
    chk("parity is +1 or -1 and nothing else",
        sorted({t[3] for t in R}), [-1, 1])
    chk("isospin runs 0 to 3/2 -- 2I in 0..3",
        sorted({t[4] for t in R}), [0, 1, 2, 3])
    chk("charge reaches a doubly charged state either way -- Q3 in thirds",
        sorted({t[5] for t in R}), [-6, -3, 0, 3, 6])
    chk("strangeness runs -3 to +3", sorted({t[6] for t in R}),
        [-3, -2, -1, 0, 1, 2, 3])
    chk("charm and beauty each take -1, 0, +1",
        (sorted({t[7] for t in R}), sorted({t[8] for t in R})),
        ([-1, 0, 1], [-1, 0, 1]))

    # the nucleons, by name, because a code-range slip once dropped them
    by = {t[0]: t for t in A}
    chk("the proton is there, 1/2+, isodoublet, charge +1, no flavour",
        by["p"][2:], (1, 1, 1, 3, 0, 0, 0))
    chk("the neutron is there, and differs from the proton in charge alone",
        by["n"][2:], (1, 1, 1, 0, 0, 0, 0))
    chk("the antiproton carries the OPPOSITE PARITY, not just the charge",
        by["p~"][2:], (1, -1, 1, -3, 0, 0, 0))
    chk("the Lambda is strangeness -1 and an isosinglet",
        by["Lambda"][2:], (1, 1, 0, 0, -1, 0, 0))
    chk("the Omega- is spin 3/2, strangeness -3",
        by["Omega-"][2:], (3, 1, 0, -3, -3, 0, 0))

    # every quark content parses -- the contrast with the mesons
    chk("every one of the 292 quark contents parses",
        [t[0] for t in A if mesons.flavour(
            {int(r["pdgid"]): r["quarks"]
             for r in pdgcapture.read()}[t[1]]) is None], [])
    chk("whereas 59 meson contents do not", len(mesons.unparsed()), 59)

    # C and G: absent without exception
    chk("no baryon carries a C or a G, all 292 of 292", cg_absent(),
        (292, 0, 0))

    # baryon number is the sign of the id
    agree, bad = baryon_number_is_the_sign()
    chk("baryon number is the sign of the PDG id, derived independently",
        (agree, bad), (True, []))

    # the chart
    X = index()
    chk("arity 7", len(next(iter(X))), 7)
    chk("184 cells over 278 members", (len(X), len(R)), (184, 278))
    chk("channel K0 -- nothing closes it", closers(), [])
    chk("cell (K, height, width)", cell(), (0, 10, 40))
    chk("and |X| <= height x width, Dilworth",
        len(X) <= cell()[1] * cell()[2], True)

    import overlap
    chk("no coordinate is a row LABEL",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # section 3: charm and beauty jointly
    ac = dict(axis_contributions())
    chk("all seven give 184 cells", ac[None], 184)
    chk("dropping charm alone loses nothing, and so does beauty",
        (ac["C"], ac["B"]), (184, 184))
    chk("dropping BOTH loses six cells -- so neither is dropped",
        ac["C and B"], 178)
    chk("and every other coordinate loses cells on its own",
        [nm for nm in ("2J", "P", "2I", "Q3", "S") if ac[nm] == 184], [])

    # section 4: conjugation
    pairs, same, split, mech = conjugation()
    chk("139 conjugate pairs, every one split", (pairs, split, same),
        (139, 139, 0))
    chk("2J and 2I are invariant; P, Q3, S, C and B all negate", mech,
        [("2J", "invariant"), ("P", "negates"), ("2I", "invariant"),
         ("Q3", "negates"), ("S", "negates"), ("C", "negates"),
         ("B", "negates")])
    chk("the MESONS' parity does NOT negate -- which is why 28 of their "
        "pairs collide", mesons.conjugation()[1], 28)

    print("baryons selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
