"""Phase 4's census: the nine transversal classes, measured over the four compendia.

`PLAN-R4-PUBLICATION.md` Phase 4 names nine transversal classes over the four
volumes and then a list of the volumes' own defects.  The plan was written several
builds ago and its figures have moved -- "interiority twice" is now zero
occurrences, and the plan's "twenty-seven objects rest on it" is twenty-eight --
so the phase is worked from THIS census and not from the plan's numbers.  That is
the same lesson DEF-153P's class taught at W-275: a list is a lead, and the tree
is the record.

THE FOUR VOLUMES
  the Mathematical Compendium, the Physics Compendium, the Index of Indices and
  the Spectra Compendium, as seated.

THE NINE CLASSES, and what each is measured as
  1  WARNING sweep          -- passages carrying an unresolved WARNING marker.
  2  citations and pointers -- deferred to tools/pointers.py, which already
                              resolves every pointer corpus-wide; not re-done here.
  3  attributions           -- names attributed in the text against the volume's
                              own References/bibliography section.
  4  handles                -- workshop object ids printed to a reader, and
                              whether a key that resolves them is printed anywhere.
  5  counts vs the Register -- figures a volume states about the Register against
                              what the Register holds.
  6  data rows              -- duplicated keys in the volumes' data tables.
  7  front matter           -- ruling 46 material: script names, rebuild commands,
                              "generated on" stamps.
  8  withdrawn statements   -- deferred to RETRACTION-AUDIT.tsv, which is the
                              corpus's own instrument for it; not re-done here.
  9  interface disclosures  -- sessions, chats and fetch machinery named to a reader.

REFUSALS
  It does not repair anything, and it does not decide the handle question.  Whether
  221 handles are given a printed key or removed in favour of the descriptive
  titles is an editorial ruling: the plan proposes a key, and the standing content
  standard says "no object handles or workshop jargon in reader-facing volumes".
  Those are different repairs and the choice is M's.  This measures the size of the
  class and stops.

  It does not re-run the pointer audit or the retraction audit.  Both already exist
  as instruments with their own contracts, and duplicating them here would produce
  a second set of numbers with no authority over the first.

  It counts a handle only where the volume prints it as a handle -- in backticks or
  as a bare dotted id -- and prints the sites so a reader can check the regex
  rather than trust it.  A count taken by pattern is a floor.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, collections, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
VOLS = [("MC", "The_Method_1_6___Mathematical_Compendium-2.md"),
        ("PC", "The_Method_1_6___The_Physics_Compendium-2.md"),
        ("IoI", "The_Method_1_6___The_Index_of_Indices-2.md"),
        ("SC", "The_Method_1_6___Spectra_Compendium-2.md")]
REG = "The_Method_1_6___The_Register-2.md"

# A workshop handle: a capitalised letter (optionally with one lower-case letter),
# a dot, then a lower-case identifier.  Printed to a reader it resolves to nothing.
HANDLE = re.compile(r"\b[A-Z][a-z]?\.[a-z][a-z0-9_]*\b")
# Ruling 46 material.
SCRIPT = re.compile(r"`?\b[a-z_][a-z0-9_]*\.py\b`?")
STAMP = re.compile(r"[Gg]enerated (from|on)\b|Rebuild with\b|python3 ")
# Interface disclosure: the machinery of how the work was done, named to a reader.
IFACE = re.compile(r"\bsessions?\b|\bchats?\b|\bconversations?\b|the assistant\b", re.I)


def text(name):
    return open(os.path.join(MEM, name), encoding="utf-8").read()


def lines(name):
    """Split for scanning; the LAST element is the empty string after the final
    newline, so a line count taken from this must drop it -- see nlines()."""
    return text(name).split("\n")


def nlines(name):
    """The store counts lines as wc -l does: newlines, not split pieces."""
    return text(name).count("\n")


def sites(name, rx):
    """(line number, the matched token) for every match, in order."""
    out = []
    for i, l in enumerate(lines(name), 1):
        for m in rx.finditer(l):
            out.append((i, m.group(0)))
    return out


def handle_key():
    """Is a key that resolves the handles printed in ANY of the four volumes?

    A key would be a passage that lists handles against their descriptive titles.
    Measured as: a line carrying three or more distinct handles AND a word that
    would introduce a key.  Reported, not asserted -- see the refusals."""
    hits = []
    for tag, name in VOLS:
        for i, l in enumerate(lines(name), 1):
            hs = {m.group(0) for m in HANDLE.finditer(l)}
            if len(hs) >= 3 and re.search(r"\bkey\b|\bglossar|\bvocabular|\bnotation\b", l, re.I):
                hits.append((tag, i, sorted(hs)[:4]))
    return hits


def duplicated_keys():
    """Duplicated KEYS in the Spectra Compendium's data table.

    A FIRST DRAFT OF THIS FUNCTION WAS WRONG AND THE WRONGNESS IS INSTRUCTIVE.  It
    scanned every pipe table in all four volumes and called a repeated FIRST CELL a
    duplicated key, which returned 571.  The first column of these tables is a
    CATEGORY, not a key -- the language table repeats "analysis" and "order" by
    design, one row per statement, and the bibliography repeats a year because
    several works share it.  571 was a count of a detector's premise, not of a
    defect.

    The Spectra Compendium's data table has a compound key, (species, series), and
    that is what is measured here: eleven-cell rows, keyed on the first two cells.
    Nothing else in the four volumes has a key this function can identify, so
    nothing else is scanned -- a class it cannot define is a class it refuses.
    """
    L = lines("The_Method_1_6___Spectra_Compendium-2.md")
    rows = []
    for i, l in enumerate(L, 1):
        if not l.strip().startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) == 11 and not set("".join(cells)) <= set("-: "):
            rows.append((i, cells))
    seen = collections.defaultdict(list)
    for i, c in rows:
        seen[(c[0], c[1])].append(i)
    dups = {k: v for k, v in seen.items() if len(v) > 1}
    return len(rows), dups


def register_extent():
    """What the Register actually runs to, for class 5.

    GROUPED HEADINGS ARE COUNTED.  A bare `### N` read misses headings of the form
    `### 219, 220, 221` and so undercounts the Register and invents gaps -- the trap
    the store records against its own gap census.  Both figures are returned: the
    numbered headings, and the total with the grouped ones expanded."""
    numbered = [int(m) for m in re.findall(r"^### (\d+)$", text(REG), re.M)]
    grouped = re.findall(r"^### (\d+(?:, *\d+)+)$", text(REG), re.M)
    covered = sum(len(g.split(",")) for g in grouped)
    hi = max(numbered + [int(x) for g in grouped for x in g.split(",")])
    # The store counts a grouped heading as ONE entry, which is why the seated
    # total is 1,724 + 7 and not 1,724 + 32; the 32 is what a bare `### N` read
    # would turn into invented gaps.
    return len(numbered), len(numbered) + len(grouped), len(grouped), covered, hi


def stated_extent():
    """Every place a compendium states the Register's extent or entry count."""
    out = []
    rx = re.compile(r"1 to (\d{3,4})|(\d[\d,]{2,}) entries")
    for tag, name in VOLS:
        for i, l in enumerate(lines(name), 1):
            if "egister" not in l:
                continue
            for m in rx.finditer(l):
                out.append((tag, i, m.group(0)))
    return out


def census():
    c = {}
    for tag, name in VOLS:
        L = lines(name)
        c[tag] = {
            "lines": nlines(name),
            "bytes": len(text(name).encode()),
            "warning": [i for i, l in enumerate(L, 1) if "WARNING" in l],
            "handles": sites(name, HANDLE),
            "scripts": sites(name, SCRIPT),
            "stamps": sites(name, STAMP),
            "iface": sites(name, IFACE),
        }
    return c


def report():
    c = census()
    print("PHASE 4 CENSUS — THE NINE CLASSES OVER THE FOUR COMPENDIA")
    print()
    print("  volume                          lines   WARNING  handles  scripts  stamps  interface")
    for tag, name in VOLS:
        d = c[tag]
        print("  %-4s %-26s %5d  %6d  %7d  %7d  %6d  %9d"
              % (tag, name.replace("The_Method_1_6___", "")[:26], d["lines"], len(d["warning"]),
                 len(d["handles"]), len(d["scripts"]), len(d["stamps"]), len(d["iface"])))
    tot = lambda k: sum(len(c[t][k]) for t, _ in VOLS)
    print("  %-31s %5d  %6d  %7d  %7d  %6d  %9d"
          % ("TOTAL", sum(c[t]["lines"] for t, _ in VOLS), tot("warning"),
             tot("handles"), tot("scripts"), tot("stamps"), tot("iface")))
    print()

    print("1  WARNING SWEEP")
    print("   unresolved WARNING markers in the four volumes: %d" % tot("warning"))
    print()

    print("2  CITATIONS AND POINTERS — deferred to tools/pointers.py, not re-done here.")
    print()

    print("3  ATTRIBUTIONS — no volume prints a References heading of its own;")
    print("   the Physics Compendium carries a bibliography as a bullet list. The")
    print("   attribution class is the prose pass's and is not measured further here.")
    print()

    print("4  HANDLES — workshop object ids printed to a reader")
    hs = collections.Counter(h for t, _ in VOLS for _, h in c[t]["handles"])
    print("   sites: %d    distinct: %d    all of them in: %s"
          % (tot("handles"), len(hs),
             ", ".join(t for t, _ in VOLS if c[t]["handles"])))
    print("   most cited: %s" % ", ".join("%s x%d" % kv for kv in hs.most_common(6)))
    k = handle_key()
    print("   a printed key that resolves them: %s" % (k if k else "NONE FOUND"))
    print("   So a reader meets %d distinct ids and can resolve none of them." % len(hs))
    print()

    print("5  COUNTS AGAINST THE REGISTER")
    n, tot, ng, cov, hi = register_extent()
    print("   %d numbered headings + %d grouped = %d entries, 1 to %d" % (n, ng, tot, hi))
    print("   the grouped ones cover %d numbers; a bare heading read would miss all" % cov)
    print("   %d of them and invent that many gaps, which is the store's own caution." % cov)
    st = stated_extent()
    print("   places a compendium states an extent or a count of it: %d" % len(st))
    for tag, i, s in st[:8]:
        print("     %-4s L%-5d %s" % (tag, i, s))
    print()

    print("6  DATA ROWS — duplicated keys in the Spectra Compendium's data table")
    n, d = duplicated_keys()
    print("   data rows: %d, each eleven cells, keyed on (species, series)" % n)
    print("   duplicated keys: %d" % len(d))
    for (a, b), ls in sorted(d.items()):
        print("     %-8s %-26s at lines %s" % (a, b, ls))
    print("   The plan says nine and nine is what measures. A first draft of this")
    print("   check scanned every table's first column and returned 571, which was a")
    print("   count of its own wrong premise: those columns are categories, not keys.")
    print()

    print("7  FRONT MATTER AND RULING 46 — script names, rebuild commands, stamps")
    for tag, _ in VOLS:
        if c[tag]["scripts"] or c[tag]["stamps"]:
            print("   %-4s %d script names, %d stamps" % (tag, len(c[tag]["scripts"]), len(c[tag]["stamps"])))
            for i, s in c[tag]["scripts"][:6]:
                print("        L%-5d %s" % (i, s))
    names = sorted({s.strip("`") for t, _ in VOLS for _, s in c[t]["scripts"]})
    print("   distinct scripts named to a reader: %d -- %s" % (len(names), ", ".join(names)))
    print()

    print("8  WITHDRAWN STATEMENTS — deferred to RETRACTION-AUDIT.tsv, not re-done here.")
    print()

    print("9  INTERFACE DISCLOSURES — the machinery named to a reader")
    for tag, _ in VOLS:
        for i, s in c[tag]["iface"]:
            ln = lines(dict(VOLS)[tag])[i - 1].strip()
            print("   %-4s L%-5d %r" % (tag, i, ln[:96]))
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    c = census()
    chk("the four volumes are seated", [t for t, _ in VOLS], ["MC", "PC", "IoI", "SC"])
    chk("their line counts",
        [c[t]["lines"] for t, _ in VOLS], [3812, 913, 2093, 1159])

    # 1
    chk("no unresolved WARNING marker in any compendium",
        sum(len(c[t]["warning"]) for t, _ in VOLS), 0)

    # 4
    hs = {h for t, _ in VOLS for _, h in c[t]["handles"]}
    chk("handle sites", sum(len(c[t]["handles"]) for t, _ in VOLS), 326)
    chk("distinct handles", len(hs), 221)
    chk("and every one is in the Mathematical Compendium",
        [t for t, _ in VOLS if c[t]["handles"]], ["MC"])
    chk("no printed key resolves them", handle_key(), [])

    # 6
    nrows, dups = duplicated_keys()
    chk("the Spectra data table's rows", nrows, 597)
    chk("duplicated (species, series) keys", len(dups), 9)
    chk("every duplicate is a pair, none a triple",
        sorted({len(v) for v in dups.values()}), [2])
    chk("and they fall in three species",
        sorted({k[0] for k in dups}), ["Ba III", "Ca II", "Si I"])

    # 5
    n, tot, ng, cov, hi = register_extent()
    chk("the Register's numbered headings", n, 1724)
    chk("its grouped headings", ng, 7)
    chk("counted as one entry each, the seated total", tot, 1731)
    chk("the numbers those grouped headings cover", cov, 32)
    chk("and a bare read would invent that many gaps", cov, 32)
    chk("the extent", hi, 1889)

    # 7
    names = sorted({s.strip("`") for t, _ in VOLS for _, s in c[t]["scripts"]})
    chk("script names printed to a reader", len(names), 18)
    chk("and they include the rebuild command's own script", "compendium.py" in names, True)
    chk("three of the four carry a generated-from stamp; the Spectra Compendium does not",
        [bool(c[t]["stamps"]) for t, _ in VOLS], [True, True, True, False])

    # 9
    chk("interface disclosures", sum(len(c[t]["iface"]) for t, _ in VOLS), 6)
    chk("and none is in the Mathematical Compendium", len(c["MC"]["iface"]), 0)

    # The plan's own figures, which have moved -- measured, so the phase is worked
    # from the tree and not from the plan.
    both = text(VOLS[2][1]) + text(VOLS[3][1])
    chk("the plan's 'interiority twice' now occurs", both.count("interiority"), 0)
    # The plan says twenty-seven; the Physics Compendium holds twenty-eight.
    # RECONNAISSANCE FOR THIS PASS REPORTED TWENTY-NINE AND THAT FIGURE WAS WRONG
    # TWICE OVER, which is why the reason is written down rather than the number
    # quietly corrected.  It was first explained as `grep -c` counting LINES where
    # the occurrences were twenty-eight; measured, `grep -c` and `grep -o | wc -l`
    # BOTH give twenty-eight on this volume, so that explanation was itself wrong.
    # The twenty-ninth occurrence is REAL and it is in ANOTHER VOLUME -- one site in
    # the Index of Indices.  The difference is SCOPE, not counting method.  This
    # check is scoped to the Physics Compendium, which is the volume the plan's row
    # is about, and says so.
    chk("the plan's twenty-seven 'rest on it', in the Physics Compendium",
        text(VOLS[1][1]).count("rest on it"), 28)
    chk("and one more in the Index of Indices, which is the reconnaissance's 29",
        text(VOLS[2][1]).count("rest on it"), 1)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
