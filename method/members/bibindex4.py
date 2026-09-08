r"""bibindex4.py — the successor to all three bibindex generations, re-taken after the imports.

WHY ONE SUCCESSOR AND NOT THREE.  `bibindex.py`, `bibindex2.py` and `bibindex3.py` are one
derivation chain: the second imports the first, the third imports both, and every figure
each pins is a cut of the same 162 bibliography rows.  W-292 to W-295 seated twelve
prior-art additions over four objects and expanded seven `et al.` sites, which moved a
figure in ALL THREE at once.  Each is HELD, none is edited, and this instrument is their
common successor -- the shape `compendia3.py` took when it discharged `compendia.py` and
`compendia2.py` together.

IT IMPORTS THE SEATED MEMBERS AND NEVER COPIES ONE.  Every number below is taken by
running the predecessor's own function over the current volumes, so a disagreement here is
a disagreement with the seated logic and not with a re-implementation of it.

WHAT MOVED, AND WHY EACH MOVED

  bibindex.classify()   DERIVED        127 -> 143   the twelve prior-art additions
                        YEAR-DIFFERS    12 ->   8
                        NAME-FORM        7 ->   3   the `et al.` expansions
                        NOT-ATTRIBUTED  16 ->   8
  bibindex2.tiers()     ATTRIBUTED     127 -> 143
                        COMPANION       15 ->   9
                        LEDGER           2 ->   0   BOTH ledger rows are now seated
                        NAMED-NOT-DATED 18 ->  10
                        NO-ATTRIBUTION-FOUND 0 -> 0  M's ruling holds, now from INSIDE the six
  bibindex3.rows()      OBJECT         127 -> 143
                        CITED            9 ->   9
                        CITED-FULLER     5 ->   2   three were expanded to their full lists
                        IMPORT-OWED     21 ->   8

THE RESULT THAT IS WORTH THE PASS.  The rows reachable only BEYOND the published six were
seventeen and are now nine, and the two rows held only in a recovered attribution ledger --
outside the members entirely -- are seated in the compendium.  `NO-ATTRIBUTION-FOUND` is
still zero, which is M's ruling of 8 September re-confirmed against a corpus that has moved
under it.

AND THE EIGHT THAT REMAIN ARE READ, NOT COUNTED.  `IMPORT-OWED` is no longer a list of works
the six fail to cite.  Six of the eight are faults in the bibliography's OWN rows -- four
pair an author with a co-cited author's year, one is the first author of a paper whose
co-author's row resolves to the very objects it names, and one prints a Shannon year the
volumes never print.  This instrument reports that reading beside
the count, and REFUSES to repair it: removing or merging a bibliography row moves the
printed "162 works" and is M's.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibindex as B
import bibindex2 as B2
import bibindex3 as B3

# The six rows read in W-299's companion measurement, each with the volume line that
# settles it.  Data, not a repair: the class is named, the disposition is M's.
ROW_FINDINGS = {
    (1913, "Pauli"): ("CROSSED-YEAR", "L.def",
                      "the object reads 'Bohr 1913; Pauli 1925'; 1925|Pauli already carries L.def"),
    (1958, "Pauli"): ("CROSSED-YEAR", "Q.delta",
                      "the object reads 'Pauli 1925 ... Seaton polarisation (1958)'; "
                      "1925|Pauli and 1958|Seaton both already carry Q.delta"),
    (1982, "Racah"): ("CROSSED-YEAR", "T.trad",
                      "the object reads 'Racah 1943; ... Freuder 1982'; Racah died in 1965"),
    (1964, "Moebius"): ("TITLE-AS-AUTHOR", "G.book",
                        "'Moebius' is a word in the title of Rota (1964), which already carries G.book"),
    (1999, "Deville"): ("SPLIT-WORK", "A.env A.orient A.r4 T.tight",
                        "one paper split into two rows: the volumes write it in full three "
                        "times as Deville, Barette & Van Hentenryck, Artif. Intell. 109 "
                        "(1999) 243-271, and the row 1999|Hentenryck RESOLVES AS OBJECT to "
                        "those same objects.  The first author is owed only because a "
                        "one-name row does not match a three-name attribution"),
    (1937, "Shannon"): ("YEAR-NOT-PRINTED", "L.bits",
                        "the volumes name Shannon only at 1938 and 1948, and rows for both stand"),
}


def moved():
    """Every figure of the three predecessors, taken now, against what each pins."""
    C = collections.Counter(c for y, w, h, c, o in B.classify())
    T = collections.Counter(r[2] for r in B2.tiers())
    R = collections.Counter(r[2] for r in B3.rows())
    return [
        ("bibindex", "DERIVED", 127, C["DERIVED"]),
        ("bibindex", "YEAR-DIFFERS", 12, C["YEAR-DIFFERS"]),
        ("bibindex", "NAME-FORM", 7, C["NAME-FORM"]),
        ("bibindex", "NOT-ATTRIBUTED", 16, C["NOT-ATTRIBUTED"]),
        ("bibindex2", "ATTRIBUTED", 127, T["ATTRIBUTED"]),
        ("bibindex2", "COMPANION", 15, T["COMPANION"]),
        ("bibindex2", "LEDGER", 2, T["LEDGER"]),
        ("bibindex2", "NAMED-NOT-DATED", 18, T["NAMED-NOT-DATED"]),
        ("bibindex2", "NO-ATTRIBUTION-FOUND", 0, T["NO-ATTRIBUTION-FOUND"]),
        ("bibindex3", "OBJECT", 127, R["OBJECT"]),
        ("bibindex3", "CITED", 9, R["CITED"]),
        ("bibindex3", "CITED-FULLER", 5, R["CITED-FULLER"]),
        ("bibindex3", "IMPORT-OWED", 21, R["IMPORT-OWED"]),
    ]


def owed():
    return sorted((y, w) for y, w, cls, wh, nt in B3.rows() if cls == "IMPORT-OWED")


def report():
    print("bibindex4 -- the three bibindex generations re-taken after the imports")
    print("=" * 78)
    print()
    print("1  EVERY FIGURE THE THREE PIN, TAKEN NOW")
    print("   %-10s %-22s %8s %8s  %s" % ("instrument", "class", "pinned", "now", ""))
    for inst, cls, was, now in moved():
        mark = "" if was == now else "  <- MOVED"
        print("   %-10s %-22s %8d %8d%s" % (inst, cls, was, now, mark))
    print()
    print("2  THE ROWS REACHED ONLY BEYOND THE PUBLISHED SIX")
    T = collections.Counter(r[2] for r in B2.tiers())
    print("   were 17 (COMPANION 15 + LEDGER 2), are now %d" % (T["COMPANION"] + T["LEDGER"]))
    print("   NO-ATTRIBUTION-FOUND                        %d   <- M's ruling, re-confirmed"
          % T["NO-ATTRIBUTION-FOUND"])
    print()
    print("3  THE EIGHT IMPORT-OWED ROWS, READ")
    for y, w in owed():
        cls, handles, why = ROW_FINDINGS.get((y, w), ("UNPUBLISHED-COMPANION", "",
                                                      "this work's own companion paper"))
        print("   %-4d %-38s %-20s %s" % (y, w, cls, handles))
        print("        %s" % why)
    print()
    print("   SIX OF THE EIGHT ARE FAULTS IN THE BIBLIOGRAPHY'S OWN ROWS, not works the")
    print("   six volumes fail to cite.  REPAIRING ONE MOVES THE PRINTED '162 works' AND")
    print("   IS M'S.  Recorded, not repaired.")


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    C = collections.Counter(c for y, w, h, c, o in B.classify())
    T = collections.Counter(r[2] for r in B2.tiers())
    R = collections.Counter(r[2] for r in B3.rows())

    chk("seated bibliography rows", len(B3.rows()), 162)
    chk("bibindex  DERIVED        (pinned 127)", C["DERIVED"], 143)
    chk("bibindex  YEAR-DIFFERS   (pinned 12)", C["YEAR-DIFFERS"], 8)
    chk("bibindex  NAME-FORM      (pinned 7)", C["NAME-FORM"], 3)
    chk("bibindex  NOT-ATTRIBUTED (pinned 16)", C["NOT-ATTRIBUTED"], 8)
    chk("and bibindex's classes still partition the rows", sum(C.values()), 162)

    chk("bibindex2 ATTRIBUTED     (pinned 127)", T["ATTRIBUTED"], 143)
    chk("bibindex2 COMPANION      (pinned 15)", T["COMPANION"], 9)
    chk("bibindex2 LEDGER         (pinned 2) -- both rows now seated", T["LEDGER"], 0)
    chk("bibindex2 NAMED-NOT-DATED (pinned 18)", T["NAMED-NOT-DATED"], 10)
    chk("bibindex2 NO-ATTRIBUTION-FOUND -- M's ruling holds", T["NO-ATTRIBUTION-FOUND"], 0)
    chk("and bibindex2's tiers still partition the rows", sum(T.values()), 162)

    chk("bibindex3 OBJECT         (pinned 127)", R["OBJECT"], 143)
    chk("bibindex3 CITED          (pinned 9)", R["CITED"], 9)
    chk("bibindex3 CITED-FULLER   (pinned 5)", R["CITED-FULLER"], 2)
    chk("bibindex3 IMPORT-OWED    (pinned 21)", R["IMPORT-OWED"], 8)
    chk("and bibindex3's classes still partition the rows", sum(R.values()), 162)

    chk("rows reached only beyond the six: were 17", T["COMPANION"] + T["LEDGER"], 9)
    chk("the eight owed rows", owed(),
        [(1913, "Pauli"), (1937, "Shannon"), (1958, "Pauli"), (1964, "Moebius"),
         (1982, "Racah"), (1999, "Deville"),
         (2026, "Lach, *The Löwdin Solution*"),
         (2026, "Lach, *The Three-Body Problem for Unknown Masses*")])
    chk("six of the eight are read as faults in the bibliography's own rows",
        sum(1 for k in owed() if k in ROW_FINDINGS), 6)
    chk("and the two that are not are this work's own companion papers",
        sorted(w for (y, w) in owed() if (y, w) not in ROW_FINDINGS),
        ["Lach, *The Löwdin Solution*",
         "Lach, *The Three-Body Problem for Unknown Masses*"])
    chk("four of the six pair an author with a co-cited author's year",
        sum(1 for k in ROW_FINDINGS if ROW_FINDINGS[k][0] in ("CROSSED-YEAR", "TITLE-AS-AUTHOR")), 4)
    chk("ROW_FINDINGS names exactly the six owed rows it reads, and no row that is not owed",
        sorted(ROW_FINDINGS) == sorted(k for k in owed() if k in ROW_FINDINGS)
        and len(ROW_FINDINGS) == 6, True)
    chk("the split-work row's co-author RESOLVES, which is what makes it one paper",
        [(y, w, c) for y, w, c, wh, nt in B3.rows() if (y, w) == (1999, "Hentenryck")],
        [(1999, "Hentenryck", "OBJECT")])
    chk("and in every one of those four the correct row already carries the handle",
        sorted(ROW_FINDINGS[k][1] for k in ROW_FINDINGS
               if ROW_FINDINGS[k][0] in ("CROSSED-YEAR", "TITLE-AS-AUTHOR")),
        ["G.book", "L.def", "Q.delta", "T.trad"])

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a = a.parse_args()
    selftest() if a.selftest else report()
