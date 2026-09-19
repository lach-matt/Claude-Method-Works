#!/usr/bin/env python3
r"""
fundamental.py -- THE STANDARD MODEL'S FUNDAMENTAL PARTICLES, CHARTED ON THE
QUANTUM NUMBERS THAT DEFINE THEM.  DOCKET 27.

    python3 fundamental.py             the reading
    python3 fundamental.py --selftest  fixtures

===============================================================================
1. THE MEMBERS
===============================================================================

One member is a fundamental particle of the Standard Model: a quark, a lepton,
a gauge boson or the Higgs.  ANTIPARTICLES ARE SEPARATE MEMBERS, because they
carry different quantum numbers -- the positron's charge is not the electron's
-- and a chart that merged them would be charting an equivalence class it had
not declared.

    12 quarks (six flavours and their antiquarks)
    12 leptons (three charged, three neutrinos, and their antiparticles)
     6 gauge bosons and the Higgs: g, gamma, W+, W-, Z0, H0
    30 members.

Read from `captures/PDG-2026.tsv`, whose provenance is in `pdgcapture.py`.  The
fourth-generation tau' PDG ships is excluded there by PDG's own status flag,
so this is the three-generation Standard Model and not a superset of it.

===============================================================================
2. THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN
===============================================================================

    2J    spin, doubled so it is an integer.  1 for every fermion, 2 for every
          gauge boson, 0 for the Higgs.
    Q3    electric charge in thirds, so the quarks are integers: +2 and -1 and
          not 2/3 and -1/3.
    COL   the DIMENSION of the colour representation -- 3 for a quark, 8 for
          the gluon, 1 for everything else.  A quantum number of the strong
          interaction and the one coordinate here that is not in the capture;
          it is assigned from the Standard Model's own definition, which is
          why `colour_rule()` prints the assignment rather than hiding it.
    GEN   generation, 1 to 3 for a fermion and 0 for a boson.  Derived from the
          PDG id, which numbers the generations in order by construction.

    WHAT IS REFUSED AS A COORDINATE, and why, since the refusals decide the
    chart as much as the choices:

    WEAK ISOSPIN AND HYPERCHARGE are the textbook gauge quantum numbers and are
    NOT charted.  They are properties of a CHIRAL field -- the left-handed
    electron and the right-handed electron carry different T3 and Y -- and the
    PDG table lists particles, not chiral components.  Charting a single T3
    against a particle would require choosing a chirality the data does not
    name.  Recorded as the sharpest thing this index cannot say.

    MASS is not charted, AND THE REASON IS NOT THE USUAL ONE.  Elsewhere in
    this tree a near-injective coordinate is refused as a row LABEL.  That
    argument DOES NOT APPLY here and the measurement says so: 13 distinct
    values over 30 members, 0.433, far below the 0.9 threshold -- because CPT
    forces a particle and its antiparticle to carry exactly equal mass, so
    every mass in the table is doubled.  Mass is refused here for a different
    and stronger reason: IT IS NOT TOTAL.  Six of the thirty members carry no
    mass at all -- the three neutrinos and their antiparticles, for which PDG
    publishes limits and not values -- and a coordinate undefined on a fifth of
    the membership cannot chart the membership.  `masses()` reports it; the
    chart does not use it, and `mass_is_not_a_label()` is the measurement that
    withdraws the label argument rather than letting it stand unchecked.

    LEPTON NUMBER AND BARYON NUMBER are derivable from the PDG id and are NOT
    charted.  They were not declared in this section before the chart was run,
    and the only reason to reach for them now is that the chart collided --
    which is the definition of fitted, and DOCKET 23's precedent refuses it.
    `additive()` reports both and `what_L_would_do()` measures exactly what
    adopting L would buy, so the refusal is on the record with its price.

===============================================================================
3. THE COLLISIONS ARE THE FINDING
===============================================================================

26 cells over 30 members: FOUR collisions, and they are not a defect in the
coordinate set but the two facts it is sharp enough to expose.

  THREE NEUTRINO PAIRS.  nu(e) and nu(e)~ agree on all four coordinates, and
  so do the mu and tau pairs.  What separates them is lepton number, refused
  above -- so the chart says, correctly, that spin, charge, colour and
  generation do not know a neutrino from an antineutrino.  For every OTHER
  fermion the charge does the work; the neutrinos are the members on which it
  cannot, because they are the neutral ones.

  ONE ELECTROWEAK PAIR.  gamma and Z0 agree on all four, and this collision
  survives EVERY additive quantum number, L and B included -- both are zero on
  both.  What distinguishes the photon from the Z is the weak mixing angle: a
  continuous parameter of the model, not a quantum number.  Both refusals in
  section 2 land on this one pair, and it is the only cell in the index that
  no admissible coordinate could split.
"""

import os
import sys

import hlaw
import mi
import pdgcapture

NAMES = ("2J", "Q3", "COL", "GEN")
ARITY = len(NAMES)
FAMILIES = ("quark", "lepton", "gauge")

# The colour representation's dimension.  Standard Model definition, assigned
# here because the PDG table does not carry it.
COLOUR_TRIPLET = 3
COLOUR_OCTET = 8
COLOUR_SINGLET = 1

# overlap.py's threshold for calling a coordinate a row label rather than a
# measurement.  Named here because section 2 quotes it.
LABEL_RATIO = 0.9

_C = {}


def rows():
    """[(name, pdgid, 2J, Q3, COL, GEN)] -- the 30, from the capture."""
    if "r" not in _C:
        out = []
        for r in pdgcapture.read():
            if r["family"] not in FAMILIES:
                continue
            pid = int(r["pdgid"])
            a = abs(pid)
            col = (COLOUR_TRIPLET if r["family"] == "quark"
                   else COLOUR_OCTET if a == 21 else COLOUR_SINGLET)
            if r["family"] == "quark":
                gen = (a + 1) // 2
            elif r["family"] == "lepton":
                gen = (a - 9) // 2
            else:
                gen = 0
            out.append((r["name"], pid, int(r["J2"]), int(r["Q3"]), col, gen))
        _C["r"] = sorted(out, key=lambda t: (t[5], t[2], t[3], t[1]))
    return _C["r"]


def index():
    """The fundamental-particle index as a set of cells."""
    return frozenset((j, q, c, g) for _n, _p, j, q, c, g in rows())


def colour_rule():
    """[(what, dimension)] -- the one assignment not read from the capture."""
    return [("quark or antiquark", COLOUR_TRIPLET), ("gluon", COLOUR_OCTET),
            ("lepton, photon, W, Z, Higgs", COLOUR_SINGLET)]


def masses():
    """[(name, mass MeV or None)] -- reported, never charted.  Section 2."""
    by = {int(r["pdgid"]): r for r in pdgcapture.read()}
    out = []
    for n, pid, *_x in rows():
        m = by[pid]["mass_MeV"]
        out.append((n, None if m == "?" else float(m)))
    return out


def mass_is_not_a_label():
    """(distinct, members, ratio, verdict) -- the withdrawal of section 2's
    usual refusal.  CPT doubles every mass, so the ratio is nowhere near the
    label threshold and the label argument may not be quoted here."""
    ms = [m for _n, m in masses() if m is not None]
    d = len({round(m, 9) for m in ms})
    n = len(rows())
    r = d / float(n)
    return (d, n, r, "LABEL" if r >= LABEL_RATIO else "NOT-A-LABEL")


def mass_is_not_total():
    """(with a mass, without, [names without]) -- the refusal that does hold."""
    no = sorted(n for n, m in masses() if m is None)
    return (len(rows()) - len(no), len(no), no)


def additive():
    """[(name, L, B)] -- lepton and baryon number, reported and NOT charted.

    Derived from the PDG id: a lepton is 11..16 and carries L = +1, its
    antiparticle -1; a quark is 1..6 and carries B = +1/3 as thirds, so B3.
    """
    out = []
    for n, pid, *_x in rows():
        a = abs(pid)
        s = 1 if pid > 0 else -1
        L = s if 11 <= a <= 16 else 0
        B3 = s if 1 <= a <= 6 else 0
        out.append((n, L, B3))
    return out


def what_L_would_do():
    """(cells now, cells with L, what would still collide) -- the price of the
    refusal in section 2, measured so the refusal is not a bare assertion."""
    L = {n: l for n, l, _b in additive()}
    wide = {}
    for n, _p, j, q, c, g in rows():
        wide.setdefault((j, q, c, g, L[n]), []).append(n)
    left = [sorted(v) for v in wide.values() if len(v) > 1]
    return (len(index()), len(wide), sorted(left))


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def by_generation():
    """{generation: [names]} -- the three generations and the bosons."""
    out = {}
    for n, _p, _j, _q, _c, g in rows():
        out.setdefault(g, []).append(n)
    return {k: sorted(v) for k, v in sorted(out.items())}


def charge_multiplet():
    """{Q3: how many} -- the charges the Standard Model actually uses."""
    out = {}
    for _n, _p, _j, q, _c, _g in rows():
        out[q] = out.get(q, 0) + 1
    return dict(sorted(out.items()))


def collisions():
    """[(cell, [names])] where two fundamental particles share a cell.

    FOUR OF THEM, AND THEY ARE THE POINT -- section 3 reads them.  Three are
    neutrino/antineutrino pairs, which only lepton number separates; the
    fourth is gamma against Z0, which no additive quantum number separates
    at all.
    """
    seen = {}
    for n, _p, j, q, c, g in rows():
        seen.setdefault((j, q, c, g), []).append(n)
    return [(k, sorted(v)) for k, v in sorted(seen.items()) if len(v) > 1]


def report():
    X = index()
    print("=" * 74)
    print("THE FUNDAMENTAL PARTICLES -- the Standard Model, charted")
    print("=" * 74)
    print()
    print("DOCKET 27.  M: \"These are legitimate particles and can and must be")
    print("accepted.\"")
    print()
    print("1. THE MEMBERS: %d." % len(rows()))
    print("   %-14s %-8s %-4s %-5s %-5s %s"
          % ("name", "pdgid", "2J", "Q3", "COL", "GEN"))
    for n, pid, j, q, c, g in rows():
        print("   %-14s %-8d %-4d %-5d %-5d %d" % (n, pid, j, q, c, g))
    print()
    print("2. THE CHART.")
    print("   cells    %d of %d members" % (len(X), len(rows())))
    print("   cell     %s" % (cell(),))
    print("   closes   %s" % (", ".join(closers()) or "NOTHING"))
    print()
    print("3. THE COLOUR ASSIGNMENT, which is not in the capture.")
    for what, d in colour_rule():
        print("   %-32s %d" % (what, d))
    print()
    print("4. GENERATIONS.")
    for g, ns in by_generation().items():
        print("   %s  %s" % ("bosons" if g == 0 else "gen %d" % g,
                             ", ".join(ns)))
    print()
    print("5. THE CHARGES THE MODEL USES, in thirds.")
    print("   %s" % charge_multiplet())
    print()
    col = collisions()
    print("6. CELL COLLISIONS: %d.  Section 3 reads them." % len(col))
    for k, ns in col:
        print("   %s  %s" % (k, ", ".join(ns)))
    print()
    print("7. MASS, REFUSED -- and the usual reason WITHDRAWN.")
    d, n, r, v = mass_is_not_a_label()
    print("   resolution   %d distinct over %d members, %.4f -- %s" % (d, n, r, v))
    print("   so the label argument does NOT refuse mass here.  CPT doubles")
    print("   every value: a particle and its antiparticle share a mass exactly.")
    have, lack, names = mass_is_not_total()
    print("   totality     %d carry a mass, %d do not: %s"
          % (have, lack, ", ".join(names)))
    print("   THAT is the refusal: a coordinate undefined on %d of %d members"
          % (lack, len(rows())))
    print("   cannot chart the membership.")
    print()
    print("8. LEPTON NUMBER, REFUSED AS FITTED -- with the price measured.")
    now, with_L, left = what_L_would_do()
    print("   cells now %d; with L appended %d" % (now, with_L))
    print("   still colliding under (2J, Q3, COL, GEN, L): %s"
          % ("; ".join(", ".join(g) for g in left) or "nothing"))
    print("   L was not declared in section 2 before the chart was run, and the")
    print("   only reason to reach for it is that the chart collided.  DOCKET 23")
    print("   refuses exactly that move.  Recorded, not adopted.")
    print()
    print("9. WHAT IS NOT CHARTED: weak isospin and hypercharge, because they")
    print("   belong to a CHIRAL field and the table lists particles; mass,")
    print("   because it is not total; L and B, because adopting them now")
    print("   would be fitted.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    R = rows()
    chk("thirty fundamental particles", len(R), 30)
    import collections
    fam = collections.Counter(
        "quark" if abs(p) <= 6 else "lepton" if 11 <= abs(p) <= 16 else "boson"
        for _n, p, *_x in R)
    chk("twelve quarks, twelve leptons, six bosons",
        dict(sorted(fam.items())), {"boson": 6, "lepton": 12, "quark": 12})

    # the quantum numbers, against the Standard Model
    chk("every fermion has 2J = 1",
        sorted({j for _n, p, j, *_x in R if abs(p) <= 16}), [1])
    chk("the gauge bosons have 2J = 2",
        sorted({j for _n, p, j, *_x in R if abs(p) in (21, 22, 23, 24)}), [2])
    chk("the Higgs is a scalar, 2J = 0",
        [j for _n, p, j, *_x in R if abs(p) == 25], [0])
    chk("up-type quarks carry Q3 = +2, down-type -1",
        (sorted({q for _n, p, _j, q, _c, _g in R if p in (2, 4, 6)}),
         sorted({q for _n, p, _j, q, _c, _g in R if p in (1, 3, 5)})),
        ([2], [-1]))
    chk("the antiquarks carry the opposite charge",
        (sorted({q for _n, p, _j, q, _c, _g in R if p in (-2, -4, -6)}),
         sorted({q for _n, p, _j, q, _c, _g in R if p in (-1, -3, -5)})),
        ([-2], [1]))
    chk("every neutrino is neutral",
        sorted({q for _n, p, _j, q, _c, _g in R if abs(p) in (12, 14, 16)}), [0])
    chk("the charged leptons carry Q3 = -3 and their antiparticles +3",
        (sorted({q for _n, p, _j, q, _c, _g in R if p in (11, 13, 15)}),
         sorted({q for _n, p, _j, q, _c, _g in R if p in (-11, -13, -15)})),
        ([-3], [3]))
    chk("W+ and W- are the only charged bosons",
        sorted(n for n, p, _j, q, _c, _g in R if abs(p) > 20 and q != 0),
        ["W+", "W-"])

    # colour
    chk("quarks are triplets, the gluon an octet, the rest singlets",
        (sorted({c for _n, p, _j, _q, c, _g in R if abs(p) <= 6}),
         [c for _n, p, _j, _q, c, _g in R if abs(p) == 21],
         sorted({c for _n, p, _j, _q, c, _g in R if 11 <= abs(p) <= 16})),
        ([3], [8], [1]))

    # generations.  A member is a particle iff its PDG id is positive -- the
    # name suffix will not do it, because the positron is `e+` and not `e-~`.
    G = by_generation()
    part = {n for n, p, *_x in R if p > 0}
    chk("three generations and one boson class", sorted(G), [0, 1, 2, 3])
    chk("eight fermions in each generation -- 2 quarks, 2 leptons, and the "
        "antiparticles of both", [len(G[g]) for g in (1, 2, 3)], [8, 8, 8])
    chk("the first generation is the stable matter one",
        sorted(n for n in G[1] if n in part), ["d", "e-", "nu(e)", "u"])
    chk("and every generation is four particles and four antiparticles",
        [(len([n for n in G[g] if n in part]),
          len([n for n in G[g] if n not in part])) for g in (1, 2, 3)],
        [(4, 4), (4, 4), (4, 4)])

    # the chart, and the four collisions that ARE the finding
    X = index()
    chk("arity 4", len(next(iter(X))), 4)
    chk("26 cells over 30 members", (len(X), len(R)), (26, 30))
    col = collisions()
    chk("four collisions, and section 3 names them -- cell and members both",
        col,
        [((1, 0, 1, 1), ["nu(e)", "nu(e)~"]),
         ((1, 0, 1, 2), ["nu(mu)", "nu(mu)~"]),
         ((1, 0, 1, 3), ["nu(tau)", "nu(tau)~"]),
         ((2, 0, 1, 0), ["Z0", "gamma"])])
    chk("three of the four are a neutrino against its antineutrino",
        len([1 for _k, ns in col if all(n.startswith("nu(") for n in ns)]), 3)
    chk("every collision is a pair, never a triple",
        sorted({len(ns) for _k, ns in col}), [2])

    # resolution: a coordinate that separates everything is a label
    import overlap
    res = {a: (r, v) for a, _d, _n, r, v in overlap.resolution(X)}
    chk("no coordinate is a row LABEL",
        [a for a, (r, v) in res.items() if v == "LABEL"], [])

    # mass: the usual refusal is WITHDRAWN and the real one measured
    have, lack, names = mass_is_not_total()
    chk("six members carry no mass at all -- the neutrinos", (have, lack),
        (24, 6))
    chk("and they are exactly the neutrinos", names,
        ["nu(e)", "nu(e)~", "nu(mu)", "nu(mu)~", "nu(tau)", "nu(tau)~"])
    d, n, r, v = mass_is_not_a_label()
    chk("mass is NOT near-injective here -- CPT doubles every value", v,
        "NOT-A-LABEL")
    chk("because each mass is carried by a particle and an antiparticle alike",
        sorted({round(m, 9) for _x, m in masses() if m is not None}) ==
        sorted({round(m, 9) for n2, m in masses()
                if m is not None and n2 in {q for q, p, *_y in R if p > 0}}),
        True)
    chk("so it is not a coordinate", "mass" in NAMES, False)

    # lepton number: refused as fitted, with the price on the record
    A = {n: (l, b) for n, l, b in additive()}
    chk("lepton number is +1 on the leptons, -1 on the antileptons",
        (sorted({A[n][0] for n, p, *_x in R if 11 <= abs(p) <= 16 and p > 0}),
         sorted({A[n][0] for n, p, *_x in R if 11 <= abs(p) <= 16 and p < 0})),
        ([1], [-1]))
    chk("baryon number in thirds is +1 on the quarks, -1 on the antiquarks",
        (sorted({A[n][1] for n, p, *_x in R if abs(p) <= 6 and p > 0}),
         sorted({A[n][1] for n, p, *_x in R if abs(p) <= 6 and p < 0})),
        ([1], [-1]))
    chk("both are zero on every boson",
        sorted({A[n] for n, p, *_x in R if abs(p) > 16}), [(0, 0)])
    now, with_L, left = what_L_would_do()
    chk("appending L would seat 29 cells, not 30", (now, with_L), (26, 29))
    chk("and gamma against Z0 would still collide -- no additive quantum "
        "number splits it", left, [["Z0", "gamma"]])

    print("fundamental selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
