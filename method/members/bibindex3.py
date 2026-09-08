r"""bibindex3.py — what the six PUBLISHED volumes must import, and where each contribution is held.

M CORRECTED THE SCOPE ON 8 SEPTEMBER: "only the six volumes will be published, so any
bibliography reference that doesn't have a direct correspondent in the six volumes must
have its work imported to appropriate compendium so the bibliography remains intact and
the reader given what the references contributed."

THAT UNDOES A TIER OF bibindex2.py.  Its COMPANION tier counted a row resolved when the
work was cited in `Transitions`, `THE-LOWDIN-SOLUTION-2` or the three-body paper.  THOSE
THREE ARE NOT PUBLISHED.  A row whose only correspondent is one of them gives a reader of
the six nothing, so it is not resolved -- it is WORK OWED.  bibindex2.py stands as seated;
this is its successor and the tier is re-cut.

THE SIX: the main volume, The Register, and the four compendia.
THE THREE UNPUBLISHED: Transitions v3.0, The Lowdin Solution, The Three-Body Problem for
Unknown Masses -- plus the two recovered attribution ledgers, which are not even members.

THE TEST, in the order a row takes:
  OBJECT           an object of the Mathematical Compendium carries the work in its own
                   grade line or prior-art quote.  This is what the bibliography's column
                   is FOR, and a row that has one gives the reader what it contributed.
  CITED            the work is cited at that year somewhere in the six, though no object
                   carries it.  The reader can follow it; the objects column cannot.
  CITED-FULLER     the six cite it under a LONGER author list of which the bibliography's
                   is a subset -- "Maier & Yannakakis 1983" against "Beeri, Fagin, Maier &
                   Yannakakis 1983", "Fano 1970" against "Lu & Fano 1970".  The work is
                   present; the row abbreviates it.  NOT A MISSING WORK.
  IMPORT-OWED      no correspondent in the six at all.

AND IT NAMES WHERE EACH IMPORT'S CONTRIBUTION IS ALREADY WRITTEN, so the import is a move
and not an invention: the three unpublished papers, the two recovered ledgers, and the
recovered generator `mathreg.py`, whose `src` and `check` fields carry the prior-art
sentence for every object it registers.

WHAT IT REFUSES.  It does not write the import.  Putting an object into a reader-facing
compendium is authoring, and the text is M's to approve; this sizes the class, sources
every row, and proposes the target volume from where the contribution is held -- the
three-body paper's works to the compendium that holds the three-body family, the
constraint literature to the operator family, and so on.  It proposes and does not place.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibindex as B
import bibindex2 as B2

PUBLISHED = ("main", "register", "mathematical", "physics", "indices", "spectra")
UNPUBLISHED = ("transitions", "lowdin-paper", "threebody-paper",
               "ledger-threebody", "ledger-lowdin")
# where a family's material belongs, from the family the contribution serves
TARGET = {"threebody-paper": "Mathematical Compendium, family 3B (three bodies)",
          "ledger-threebody": "Mathematical Compendium, family 3B (three bodies)",
          "lowdin-paper": "Mathematical Compendium, family LS (the Löwdin solution)",
          "ledger-lowdin": "Mathematical Compendium, family LS (the Löwdin solution)",
          "transitions": "Mathematical Compendium, the family the object already sits in",
          "generator": "Mathematical Compendium, the family the object already sits in"}


def _six():
    t = B2.corpus()
    return {k: v for k, v in t.items() if k in PUBLISHED}


def _unpublished():
    t = B2.corpus()
    return {k: v for k, v in t.items() if k in UNPUBLISHED}


def citations(texts):
    """{year: {(workkey, tag)}} over the given texts."""
    out = collections.defaultdict(set)
    for tag, t in texts.items():
        for a, y in B.CITE.findall(t):
            out[int(y)].add((B.workkey(a), tag))
    return out


def generator_text():
    """The recovered generator as one searchable text, or '' if absent.

    Its `src` and `check` fields carry the prior-art sentence for each object, which is
    where several imports' contributions are already written."""
    REG = B2.generator()
    if not REG:
        return ""
    return "\n".join(" ; ".join(str(r.get(k) or "") for k in
                                ("id", "named", "stmt", "src", "check"))
                     for r in REG.values())


def rows():
    """(year, work, class, where, note) for each seated bibliography row."""
    six = _six()
    cit = citations(six)
    attributed = {(y, w) for y, w, hs, cls, objs in B.classify() if cls == "DERIVED"}
    out = []
    for y, w, hs, cls, objs in B.classify():
        k = B.workkey(w)
        if (y, w) in attributed:
            out.append((y, w, "OBJECT", "the object's own apparatus", " | ".join(objs)))
            continue
        here = sorted({tag for kk, tag in cit.get(y, ()) if kk == k})
        if here:
            out.append((y, w, "CITED", ", ".join(here), ""))
            continue
        fuller = sorted({" ".join(sorted(kk)) for kk, tag in cit.get(y, ()) if k < kk})
        if fuller:
            tags = sorted({tag for kk, tag in cit.get(y, ()) if k < kk})
            out.append((y, w, "CITED-FULLER", ", ".join(tags), "; ".join(fuller)))
            continue
        out.append((y, w, "IMPORT-OWED", "", ""))
    return out


def sources():
    """{(year, work): (where the contribution is written, proposed target)} for the owed."""
    un = _unpublished()
    gen = generator_text()
    haystack = dict(un)
    if gen:
        haystack["generator"] = gen
    cit = citations(haystack)
    out = {}
    for y, w, cls, where, note in rows():
        if cls != "IMPORT-OWED":
            continue
        k = B.workkey(w)
        sn = [s for s in k if len(s) > 2]
        # AT THE YEAR THE ROW PRINTS -- a surname alone finds a DIFFERENT work by the
        # same author, which is how a first draft of this reported Shannon 1937 held
        # when what it had found was Shannon 1948.
        dated = sorted({tag for kk, tag in cit.get(y, ()) if k <= kk})
        named = [tag for tag, t in haystack.items()
                 if sn and all(re.search(r"\b%s\b" % re.escape(s), t, re.I) for s in sn)]
        hit = dated or []
        out[(y, w)] = (hit, TARGET.get(hit[0], "") if hit else "",
                       [t for t in named if t not in hit])
    return out


def report():
    R = rows()
    n = collections.Counter(r[2] for r in R)
    print("bibindex3 -- what the six published volumes must import")
    print("=" * 78)

    print("\n1  THE 162 ROWS AGAINST THE SIX THAT WILL BE PUBLISHED")
    for k in ("OBJECT", "CITED", "CITED-FULLER", "IMPORT-OWED"):
        print("   %-16s %4d" % (k, n[k]))
    print("   and they sum to %d" % sum(n.values()))
    print("\n   bibindex2.py resolved 15 rows into a COMPANION tier.  Under M's scope")
    print("   correction that tier is void: Transitions, The Löwdin Solution and The")
    print("   Three-Body Problem are not published, so a reader of the six gets nothing")
    print("   from them.  Those rows are work owed, not rows resolved.")

    print("\n2  CITED-FULLER — THE ROW ABBREVIATES A LONGER AUTHOR LIST, AND IS NOT MISSING")
    for y, w, cls, where, note in R:
        if cls == "CITED-FULLER":
            print("   %4d  %-26s -> %-44s [%s]" % (y, w[:26], note[:44], where[:22]))

    print("\n3  CITED BUT CARRYING NO OBJECT — the reader can follow it, the column cannot")
    for y, w, cls, where, note in R:
        if cls == "CITED":
            print("   %4d  %-34s %s" % (y, w[:34], where))

    print("\n4  IMPORT OWED — %d ROWS, AND WHERE EACH CONTRIBUTION IS ALREADY WRITTEN" % n["IMPORT-OWED"])
    print("   A hit AT THE ROW'S OWN YEAR is a pinned source.  A hit on the author at")
    print("   another year is weaker and is marked as such: a first draft of this counted")
    print("   both alike and reported Shannon 1937 held, when what it had found was")
    print("   Shannon 1948.")
    S = sources()
    nowhere = []
    for y, w, cls, where, note in R:
        if cls != "IMPORT-OWED":
            continue
        hit, target, weak = S[(y, w)]
        if hit:
            print("   %4d  %-32s held in %-22s -> %s" % (y, w[:32], ", ".join(hit)[:22], target))
        else:
            nowhere.append((y, w, weak))
    if nowhere:
        print("\n   AND WITH NO CONTRIBUTION WRITTEN ANYWHERE HELD HERE:")
        for y, w, weak in nowhere:
            print("      %4d  %-32s %s" % (y, w[:32],
                  ("the author is named in %s, at another year" % ", ".join(weak))
                  if weak else "the author is named nowhere held here"))
        print("   These need the outside search M directed before an import can be written.")


def write_tsv(path):
    S = sources()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("year\twork\tclass\twhere\tnote\tcontribution_held_in\tproposed_target\n")
        for y, w, cls, where, note in rows():
            hit, target, weak = S.get((y, w), ([], "", []))
            fh.write("%d\t%s\t%s\t%s\t%s\t%s\t%s\n"
                     % (y, w, cls, where, note, ", ".join(hit), target))
    print("written %s (%d rows)" % (path, len(rows())))


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    R = rows()
    n = collections.Counter(r[2] for r in R)
    chk("seated bibliography rows", len(R), 162)
    chk("OBJECT -- an object of the compendium carries it", n["OBJECT"], 127)
    chk("CITED in the six, no object", n["CITED"], 9)
    chk("CITED-FULLER -- the row abbreviates a longer list", n["CITED-FULLER"], 5)
    chk("IMPORT-OWED -- no correspondent in the six", n["IMPORT-OWED"], 21)
    chk("and the classes partition the rows", sum(n.values()), 162)

    ff = {w for y, w, cls, wh, nt in R if cls == "CITED-FULLER"}
    chk("the abbreviated rows", sorted(ff),
        ["Andrew & Cowan", "Fano", "Fredenhagen & Verch",
         "Inokuti & Manson", "Maier & Yannakakis"])

    S = sources()
    held = [k for k, (hit, t, weak) in S.items() if hit]
    chk("owed rows pinned to their year in an unpublished source", len(held), 9)
    chk("owed rows held only by author, at another year", len(S) - len(held), 12)
    chk("owed rows with nothing held anywhere",
        len([k for k, (hit, t, weak) in S.items() if not hit and not weak]), 0)
    chk("Shannon 1937 is one of the twelve, and the corpus cites Shannon 1948",
        (S[(1937, "Shannon")][0], bool(S[(1937, "Shannon")][2])), ([], True))
    tb = [k for k, (hit, t, weak) in S.items()
          if any("threebody" in x for x in hit + weak)]
    chk("owed rows the three-body paper or ledger holds", len(tb), 13)
    chk("two of the owed rows are the unpublished papers themselves",
        sorted(w for (y, w) in S if y == 2026),
        ["Lach, *The Löwdin Solution*", "Lach, *The Three-Body Problem for Unknown Masses*"])

    # bibindex2's COMPANION tier is what this re-cuts
    T2 = collections.Counter(r[2] for r in B2.tiers())
    chk("bibindex2 called this many COMPANION", T2["COMPANION"], 15)
    chk("and none of those is a published volume", T2["NO-ATTRIBUTION-FOUND"], 0)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a.add_argument("--write", metavar="PATH")
    a = a.parse_args()
    if a.selftest:
        selftest()
    elif a.write:
        write_tsv(a.write)
    else:
        report()
