#!/usr/bin/env python3
r"""
docket27.py -- IS EVERY PARTICLE OTHER THAN A PERIODIC ATOM NOW INDEXED?
THE QUESTION ASKED OF THE WHOLE TABLE, AND ANSWERED WITH A COUNT.

    python3 docket27.py             the reading
    python3 docket27.py --selftest  fixtures

M: "Can you now please produce indexes and plates for all particles other than
periodic atoms.  We need photons, muons, anti-matter, whatever particle there
is that isn't already indexed.  We are essentially filling in the rest of the
space in the master index."

===============================================================================
1. THE ANSWER, AND IT IS EXACT
===============================================================================

    6,506   entries in the Particle Data Group's 2026 table
   -5,880   composite nuclei -- THESE ARE THE PERIODIC ATOMS, and `gravity`
            already seats 3,394 nuclide-charge states over them
      -54   PDG status 4, "NotInPDT" -- diquarks and the fourth generation,
            excluded on PDG's OWN flag and not on a judgement made here
    -----
      572   observable non-nuclear particles

        12  quarks         `fundamental`
        12  leptons        `fundamental`
         6  gauge + Higgs  `fundamental`
       250  mesons         `mesons`
       292  baryons        `baryons`
    -----
       572  EVERY ONE OF THEM IS A MEMBER OF A SEATED INDEX.

THIS IS A COMPLETENESS CLAIM AND IT IS A NARROW ONE.  It says every particle
in one table is a member of some index here.  It does not say every index of
those particles has been found -- `registry.COMPLETE` is False and stays
False, and this file does not touch it.  Two quite different questions.

===============================================================================
2. TWENTY-TWO ARE MEMBERS BUT NOT CHARTED, AND THEY ARE NAMED
===============================================================================

Eight mesons and fourteen baryons carry no parity in the table, so a chart
carrying P cannot place them.  They are members of the declared member set and
they are listed by `mesons.unplaced()` and `baryons.unplaced()`; 550 of the 572
land on a cell.

    A GAP IN THE TABLE IS NOT A GAP IN PHYSICS, and it is not a gap in this
    index either -- it is a parity nobody has measured yet.  A later Review
    that measures those twenty-two parities seats them with no change to any
    instrument but the count.

===============================================================================
3. WHAT IS STILL NOT INDEXED, SAID PLAINLY
===============================================================================

    HYPOTHETICAL PARTICLES.  Supersymmetric partners, axions, dark-matter
    candidates: none is in the table as an observed state, and a particle with
    no measured quantum numbers cannot be a member of an index whose criterion
    is that a member carries them.  Not a refusal -- there is nothing to seat.

    QUASIPARTICLES.  Phonons, magnons, excitons, Cooper pairs.  These DO carry
    quantum numbers and would pass the criterion, and they are simply not in
    this table; PDG catalogues elementary and hadronic states, not collective
    excitations of a solid.  THIS IS THE ONE HONEST GAP IN DOCKET 27 and it is
    recorded rather than closed: indexing them needs a different source, which
    is a fetch this pass did not make.

    THE PERIODIC ATOMS THEMSELVES.  Out of scope by the docket's own wording,
    and already indexed nine ways over.
"""

import sys

import baryons
import fundamental
import mesons
import pdgcapture
import registry

# The census the capture's own header records, so this file can state it
# without needing the `particle` package on the read path.
CENSUS_LINE = "# census  PDG table"

FAMILIES = (
    ("quarks", "fundamental", 12),
    ("leptons", "fundamental", 12),
    ("gauge bosons and the Higgs", "fundamental", 6),
    ("mesons", "mesons", 250),
    ("baryons", "baryons", 292),
)


def census():
    """(total, composite nuclei, status 4, kept) read from the capture header.

    NOT recomputed: the capture recorded it at write time, when the `particle`
    package was present, and re-deriving it here would need that package on
    every read.  `pdgcapture.census()` is the deriving one.
    """
    for ln in pdgcapture.header():
        if ln.startswith(CENSUS_LINE):
            n = [int(t) for t in ln.replace("=", " ").replace("+", " ").split()
                 if t.isdigit()]
            return tuple(n)
    raise AssertionError("the capture header records no census -- rewrite it")


def held():
    """{family: how many rows of the capture that index holds}."""
    return {
        "quarks": sum(1 for r in pdgcapture.read() if r["family"] == "quark"),
        "leptons": sum(1 for r in pdgcapture.read() if r["family"] == "lepton"),
        "gauge bosons and the Higgs":
            sum(1 for r in pdgcapture.read() if r["family"] == "gauge"),
        "mesons": len(mesons.all_rows()),
        "baryons": len(baryons.all_rows()),
    }


def accounted():
    """(kept by the capture, summed over the three indexes, they agree)."""
    kept = census()[3]
    tot = sum(held().values())
    return (kept, tot, kept == tot)


def unplaced():
    """[(index, name)] -- members with no cell, because P is not printed."""
    return ([("mesons", n) for n in mesons.unplaced()]
            + [("baryons", n) for n in baryons.unplaced()])


def charted():
    """(members, charted, unplaced) over the three indexes."""
    m = sum(held().values())
    u = len(unplaced())
    return (m, m - u, u)


def cells():
    """[(index, members charted, cells, cell, channel)]."""
    out = []
    for nm, mod in (("fundamental", fundamental), ("mesons", mesons),
                    ("baryons", baryons)):
        X = mod.index()
        c = mod.cell()
        out.append((nm, len(mod.rows()), len(X), c, c[0]))
    return out


def seated():
    """The three rows as registry.py holds them -- read, never retyped."""
    return [r for r in registry.rows()
            if r[1] in ("fundamental", "mesons", "baryons")]


def report():
    tot, ncomp, nst4, kept = census()
    print("=" * 74)
    print("DOCKET 27 -- is every particle other than a periodic atom indexed?")
    print("=" * 74)
    print()
    print("1. THE TABLE, ACCOUNTED FOR.")
    print("   %6d  entries in the PDG 2026 table" % tot)
    print("   %6d  composite nuclei -- THE PERIODIC ATOMS, seated as gravity"
          % -ncomp)
    print("   %6d  PDG status 4 NotInPDT -- diquarks, fourth generation"
          % -nst4)
    print("   %6s" % ("-" * 6))
    print("   %6d  observable non-nuclear particles" % kept)
    print()
    H = held()
    for nm, idx, _n in FAMILIES:
        print("   %6d  %-28s %s" % (H[nm], nm, idx))
    k, t, ok = accounted()
    print("   %6s" % ("-" * 6))
    print("   %6d  %s" % (t, "EVERY ONE IS A MEMBER OF A SEATED INDEX"
                          if ok else "MISMATCH against %d kept" % k))
    print()
    m, c, u = charted()
    print("2. MEMBERS AGAINST CHARTED: %d members, %d charted, %d unplaced."
          % (m, c, u))
    print("   Unplaced means PDG prints no parity, so a chart carrying P")
    print("   cannot place them.  A gap in the table, not in physics:")
    for idx, n in unplaced():
        print("     %-9s %s" % (idx, n))
    print()
    print("3. THE THREE INDEXES.")
    print("   %-13s %-9s %-7s %-12s %s"
          % ("index", "charted", "cells", "cell", "channel"))
    for nm, mem, nc, cl, ch in cells():
        print("   %-13s %-9d %-7d %-12s K%d" % (nm, mem, nc, str(cl), ch))
    print()
    print("4. WHAT IS STILL NOT INDEXED.")
    print("   hypothetical particles  nothing to seat -- no measured quantum")
    print("                           numbers, so the criterion has no purchase")
    print("   quasiparticles          THE ONE HONEST GAP.  They would pass the")
    print("                           criterion; they are not in this table,")
    print("                           and indexing them needs another source")
    print("   the periodic atoms      out of scope, and already indexed")
    print()
    print("5. WHAT IS NOT CLAIMED.")
    print("   registry.COMPLETE is %s and this file does not touch it."
          % registry.COMPLETE)
    print("   'Every particle in one table is a member of some index' is not")
    print("   'every index of those particles has been found'.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    tot, ncomp, nst4, kept = census()
    chk("the capture's header records the whole-table census",
        (tot, ncomp, nst4, kept), (6506, 5880, 54, 572))
    chk("and the three parts sum to the whole", ncomp + nst4 + kept, tot)
    chk("the excluded nuclei are 90% of the table -- they are the periodic "
        "elements", round(ncomp / float(tot), 2), 0.9)

    H = held()
    chk("the capture's families are the sizes the three indexes declare",
        [H[nm] for nm, _i, _n in FAMILIES], [n for _nm, _i, n in FAMILIES])
    k, t, agree = accounted()
    chk("EVERY KEPT ROW IS A MEMBER OF A SEATED INDEX -- none unaccounted",
        (k, t, agree), (572, 572, True))

    m, c, u = charted()
    chk("550 of the 572 land on a cell", (m, c, u), (572, 550, 22))
    chk("and the 22 unplaced are 8 mesons and 14 baryons",
        [sum(1 for i, _n in unplaced() if i == x)
         for x in ("mesons", "baryons")], [8, 14])
    chk("every unplaced member is named, not counted",
        len(unplaced()) == len({n for _i, n in unplaced()}), True)

    chk("three indexes, and registry.py holds all three",
        sorted(r[1] for r in seated()), ["baryons", "fundamental", "mesons"])
    chk("their channels, read from the instruments",
        [(nm, ch) for nm, _m, _c, _cl, ch in cells()],
        [("fundamental", 2), ("mesons", 0), ("baryons", 0)])
    chk("no new channel was reached -- K2 and K0 were both occupied already",
        sorted({ch for _nm, _m, _c, _cl, ch in cells()}), [0, 2])

    # the completeness claim is narrow, and the file must not widen it
    chk("COMPLETE is untouched and still False", registry.COMPLETE, False)
    chk("and this file says so in its own text, whitespace normalised so a "
        "reflow cannot silently pass it",
        "does not say every index of those particles has been found"
        in " ".join(__doc__.split()), True)

    print("docket27 selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
