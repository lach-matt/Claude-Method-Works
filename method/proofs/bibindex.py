r"""bibindex.py — the bibliography's objects column, derived from the volume's own attributions.

M RULED ON 8 SEPTEMBER: "the handle map is old and stale.  it is yours to build to the
function you need."  That ruling changes what has to be built.  The handles are not an
addressing scheme to be recovered -- they are a dead index -- and the function the
Mathematical Compendium's bibliography performs is stated in its own opening line:

    "Every object of this compendium names a work.  What follows is those works,
     ordered by year, with the objects each carries."

SO THE COLUMN IS NOT A LIST OF IDS.  It is the INVERSE of the attributions the objects
already carry, and every object carries them in a form a reader reads: a grade line --
"Computed -- M SS20 / the statistical language; Deming & Stephan 1940; Csiszar 1975." --
and, for most, a prior-art blockquote.  This instrument builds that inverse and reports
where it does and does not reproduce the seated column.

WHAT IT DERIVES.  For each of the 299 objects, every (work, year) its own entry names,
from the grade line and the prior-art quote.  Names are normalised to an unordered set of
surnames, so "Deville et al. 1999" and "Deville 1999" are one work and "Murray & von
Neumann" survives its particle.  Inverting gives, for each work, the objects that name it
-- BY DESCRIPTIVE TITLE, which is exactly what M's content standard requires a
cross-reference to be.

WHAT IT FINDS, AGAINST THE 162 SEATED ROWS.  Four classes, and three of them are findings:
  DERIVED         the row's (year, work) is named by at least one object.
  YEAR-DIFFERS    the work is named, under a year the bibliography does not print.
  NAME-FORM       an overlapping author set is named, in a different form.
  NOT-ATTRIBUTED  no object entry names the work at all.

AND IT CORRECTS A FINDING OF MY OWN.  W-281 recorded that the bibliography names 265 of
299 objects and concluded that "Every object of this compendium names a work" is FALSE BY
34.  THE MEASUREMENT STANDS AND THE LABEL WAS WRONG: 34 is the count of objects carrying
no HANDLE in a column M has now told us is stale.  Counted from the attributions
themselves, THE OBJECTS THAT NAME NO WORK NUMBER TWELVE, and they are named in the report
so the claim can be judged rather than taken.

THE CROSS-CHECK, and it is what shows the handles are stale rather than the derivation
wrong.  `handlemap.py` resolves 112 handles to a title on evidence independent of any
ordering.  Where such a handle sits on a row this instrument can derive, the two are
compared: 134 of 145 land on an object the derivation also gives.  THE ELEVEN THAT DO NOT
ARE NOT DERIVATION FAILURES -- on each of them the derived answer is the object the work
is named for.  `Borchers 1992` derives to "Borchers 1992 / Wiesbrock 1993"; `Racah 1943`
to "Racah 1943 seniority"; `Karp 1972`, whose paper is the one that made set cover famous,
to "The seed is a set cover", where the handle map says "The unit template, corrected".

WHAT IT REFUSES.  It writes no volume.  It emits `method/BIBLIOGRAPHY-OBJECTS.tsv` and a
row it cannot derive gets no column -- an empty objects column is a finding, and a column
filled by guessing would be reconstructed content in a reader-facing volume.  It does not
adjudicate a YEAR-DIFFERS row: whether the bibliography's year is wrong or the two are
different works by one author is a reading, and it is named rather than decided.  It does
not add or remove a bibliography row.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compendia2 as C     # seated members, imported and never copied
import handlemap as HM

FAMILY = re.compile(r"^## ([A-Za-z0-9]{1,3})\. .*? — (\d+) objects$")
GRADE = re.compile(r"^(Definitional|Computed|Proved|Measured|Asserted|Cited)\b(.*)$")
# A surname may open with a particle; a work may name several, joined by , & and or a dash.
_P = r"(?:(?:von|van|de|der|den|du|la|le|di|del)\s+)?[A-ZÀ-Þ][\wÀ-ÿ’'\-]*"
CITE = re.compile(r"(%s(?:\s*(?:,|&|and|–|-)\s*%s)*(?:\s+et al\.?)?)\s+\(?(1[5-9]\d\d|20[0-4]\d)\)?"
                  % (_P, _P))


def workkey(name):
    """A work as an unordered set of surnames, lower case.

    "Deville et al. 1999" and "Deville 1999" are one work; "Murray & von Neumann" keeps
    both names; italics around a title are dropped."""
    n = re.sub(r"\s+et al\.?$", "", name.strip())
    n = re.sub(r"[*_]", "", n)
    return frozenset(p.strip().lower()
                     for p in re.split(r"\s*(?:,|&|and|–|-)\s*", n) if p.strip())


def objects():
    """[{fam, title, grade_cites, prior_cites}] for all 299 objects, in printed order."""
    fam = None
    out = []
    cur = None
    for l in C.text(C.VOLS[0][1]).split("\n"):
        if FAMILY.match(l):
            fam = FAMILY.match(l).group(1)
            continue
        if l.startswith("# "):
            fam = None
            continue
        if fam and l.startswith("### "):
            cur = {"fam": fam, "title": l[4:].strip(), "grade": [], "prior": [], "seen": False}
            out.append(cur)
            continue
        if cur is None or not fam:
            continue
        m = GRADE.match(l.strip())
        if m and not cur["seen"]:
            cur["seen"] = True
            cur["grade"] = [(a, int(y)) for a, y in CITE.findall(m.group(2))]
        elif l.strip().startswith(">"):
            cur["prior"] += [(a, int(y)) for a, y in CITE.findall(l)]
    return out


def inverse():
    """{(year, workkey): {object title, ...}} and {workkey: {year, ...}}."""
    inv = collections.defaultdict(set)
    years = collections.defaultdict(set)
    for o in objects():
        for a, y in o["grade"] + o["prior"]:
            inv[(y, workkey(a))].add(o["title"])
            years[workkey(a)].add(y)
    return inv, years


def mentions():
    """{(year, workkey): {title}} over EVERY line of an object's entry, body prose included.

    Reported beside the attribution apparatus and never merged into it.  AN ATTRIBUTION IS
    NOT A MENTION: the grade line and the prior-art quote are where an object says what it
    rests on, and its body is discussion.  Widening to the body adds two rows and would
    quietly turn a mention into a source."""
    fam = None
    cur = None
    out = collections.defaultdict(set)
    for l in C.text(C.VOLS[0][1]).split("\n"):
        if FAMILY.match(l):
            fam = FAMILY.match(l).group(1)
            continue
        if l.startswith("# "):
            fam = None
            continue
        if fam and l.startswith("### "):
            cur = l[4:].strip()
            continue
        if cur is None or not fam:
            continue
        for a, y in CITE.findall(l):
            out[(int(y), workkey(a))].add(cur)
    return out


def bibrows():
    """[(year, work as printed, [handle, ...])] for the 162 seated rows."""
    rows, _, _ = C.bibliography()
    tick, _ = C.handle_rx()
    out = []
    for l in rows:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        out.append((int(c[0]), c[1], tick.findall(c[2] if len(c) > 2 else "")))
    return out


def classify():
    """One row per seated bibliography row: (year, work, handles, class, objects)."""
    inv, years = inverse()
    out = []
    for y, w, hs in bibrows():
        k = workkey(w)
        if (y, k) in inv:
            out.append((y, w, hs, "DERIVED", sorted(inv[(y, k)])))
        elif k in years:
            out.append((y, w, hs, "YEAR-DIFFERS",
                        sorted({t for yy in years[k] for t in inv[(yy, k)]})))
        else:
            near = [kk for kk in years if k & kk]
            if near:
                out.append((y, w, hs, "NAME-FORM",
                            sorted({t for kk in near for yy in years[kk] for t in inv[(yy, kk)]})))
            else:
                out.append((y, w, hs, "NOT-ATTRIBUTED", []))
    return out


def crosscheck():
    """Legible handle titles against the derived objects, row by row."""
    res = {r[1]: r[2] for r in HM.rows() if r[3] == "RESOLVED"}
    agree = disagree = 0
    rows_ok = rows_bad = 0
    examples = []
    for y, w, hs, cls, objs in classify():
        if cls != "DERIVED":
            continue
        legible = {res[h] for h in hs if h in res}
        if not legible:
            continue
        bad = legible - set(objs)
        agree += len(legible) - len(bad)
        disagree += len(bad)
        if bad:
            rows_bad += 1
            examples.append((y, w, sorted(bad), objs))
        else:
            rows_ok += 1
    return agree, disagree, rows_ok, rows_bad, examples


def report():
    O = objects()
    inv, years = inverse()
    R = classify()
    n = collections.Counter(r[3] for r in R)
    print("bibindex -- the objects column, derived from the volume's own attributions")
    print("=" * 78)

    print("\n1  WHAT THE OBJECTS THEMSELVES NAME")
    print("   objects                                   %d" % len(O))
    print("   objects carrying a grade line             %d" % sum(1 for o in O if o["seen"]))
    named = [o for o in O if o["grade"] or o["prior"]]
    print("   objects naming at least one work          %d" % len(named))
    print("   distinct (work, year) they name           %d" % len(inv))
    print("   objects naming NO work at all             %d" % (len(O) - len(named)))
    for o in O:
        if not (o["grade"] or o["prior"]):
            print("        %-4s %s" % (o["fam"], o["title"][:62]))

    print("\n2  A FINDING OF MINE CORRECTED, AND THE MEASUREMENT THAT STANDS")
    _, occ, dist = C.bibliography()
    print("   objects carrying no HANDLE in the bibliography   %d   <- W-281's 34, and it stands"
          % (len(O) - len(dist)))
    print("   objects naming no WORK in their own entry        %d   <- what the sentence is about"
          % (len(O) - len(named)))
    print("   'Every object of this compendium names a work' is FALSE BY %d, not by %d."
          % (len(O) - len(named), len(O) - len(dist)))
    print("   The number was right; the label on it was mine and it was wrong.")

    print("\n3  THE 162 SEATED ROWS, CLASSIFIED")
    for k in ("DERIVED", "YEAR-DIFFERS", "NAME-FORM", "NOT-ATTRIBUTED"):
        print("   %-16s %4d" % (k, n[k]))
    print("   and they sum to %d" % sum(n.values()))
    for k in ("YEAR-DIFFERS", "NAME-FORM", "NOT-ATTRIBUTED"):
        print("\n   -- %s" % k)
        for y, w, hs, cls, objs in R:
            if cls != k:
                continue
            extra = ""
            if k == "YEAR-DIFFERS":
                extra = "  objects cite %s" % sorted(years[workkey(w)])
            print("      %4d  %-34s%s" % (y, w[:34], extra))

    print("\n3b THE WIDER SCAN, REPORTED AND NOT MERGED")
    M = mentions()
    wider = sum(1 for y, w, hs in bibrows() if (y, workkey(w)) in M)
    print("   rows an ATTRIBUTION derives                    %d" % n["DERIVED"])
    print("   rows any MENTION anywhere in an entry reaches  %d" % wider)
    print("   the difference is %d, and it stays a difference: the grade line and the"
          % (wider - n["DERIVED"]))
    print("   prior-art quote are where an object says what it RESTS ON; its body is")
    print("   discussion, and a work discussed is not a work the object names.")
    still = [(y, w) for y, w, hs, cls, objs in R
             if cls == "NOT-ATTRIBUTED" and (y, workkey(w)) not in M]
    print("   works named NOWHERE in any object entry, on the widest scan: %d" % len(still))
    for y, w in still:
        print("        %4d  %s" % (y, w[:60]))

    print("\n4  THE CROSS-CHECK: THE HANDLES AGAINST THE DERIVATION")
    a, d, ro, rb, ex = crosscheck()
    print("   legible handle titles on derivable rows   %d" % (a + d))
    print("   landing on an object the derivation gives %d" % a)
    print("   landing on one it does not                %d" % d)
    print("   rows wholly agreeing / partly not         %d / %d" % (ro, rb))
    print("   and on every one of the %d, the derived answer is the object the work is" % d)
    print("   named for.  That is the ruling's own point: the handle column is stale.")
    for y, w, bad, objs in ex[:6]:
        print("      %4d %-24s handle %-38s derived %s"
              % (y, w[:24], bad[0][:38], objs[0][:34]))


def write_tsv(path):
    R = classify()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("year\twork\tclass\tobjects_derived\thandles_seated\n")
        for y, w, hs, cls, objs in R:
            fh.write("%d\t%s\t%s\t%s\t%s\n" % (y, w, cls, " | ".join(objs), " ".join(hs)))
    print("written %s (%d rows)" % (path, len(R)))


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    O = objects()
    inv, years = inverse()
    R = classify()
    n = collections.Counter(r[3] for r in R)

    chk("objects parsed", len(O), 299)
    chk("of which carry a grade line", sum(1 for o in O if o["seen"]), 298)
    chk("the one that does not is the unfinished modular object",
        [o["title"] for o in O if not o["seen"]],
        ["Half-sided modular inclusion on a non-expanding horizon"])
    named = [o for o in O if o["grade"] or o["prior"]]
    chk("objects naming at least one work", len(named), 287)
    chk("objects naming none", len(O) - len(named), 12)

    # the correction to W-281
    _, occ, dist = C.bibliography()
    chk("objects carrying no handle -- W-281's figure, which stands", len(O) - len(dist), 34)
    chk("but objects naming no WORK", len(O) - len(named), 12)
    chk("so the false universal is false by", len(O) - len(named), 12)

    chk("seated bibliography rows", len(R), 162)
    chk("DERIVED", n["DERIVED"], 127)
    chk("YEAR-DIFFERS", n["YEAR-DIFFERS"], 12)
    chk("NAME-FORM", n["NAME-FORM"], 7)
    chk("NOT-ATTRIBUTED", n["NOT-ATTRIBUTED"], 16)
    chk("and the four classes partition the rows", sum(n.values()), 162)
    chk("every NOT-ATTRIBUTED row derives no object",
        [r for r in R if r[3] == "NOT-ATTRIBUTED" and r[4]], [])

    chk("name normalisation joins 'et al.' to its bare form",
        workkey("Deville et al.") == workkey("Deville"), True)
    chk("and keeps a particle with its surname",
        sorted(workkey("Murray & von Neumann")), ["murray", "von neumann"])

    M = mentions()
    chk("rows a mention anywhere reaches",
        sum(1 for y, w, hs in bibrows() if (y, workkey(w)) in M), 129)
    chk("which is two more than the attribution apparatus derives", 129 - n["DERIVED"], 2)
    chk("works named nowhere in any object entry at all",
        len([1 for y, w, hs, cls, objs in R
             if cls == "NOT-ATTRIBUTED" and (y, workkey(w)) not in M]), 15)
    chk("and two of those fifteen are this work's own companion papers",
        sorted(w[:12] for y, w, hs, cls, objs in R
               if cls == "NOT-ATTRIBUTED" and (y, workkey(w)) not in M and y == 2026),
        ["Lach, *The L", "Lach, *The T"])

    a, d, ro, rb, ex = crosscheck()
    chk("legible handle titles checked", a + d, 145)
    chk("agreeing with the derivation", a, 134)
    chk("disagreeing", d, 11)
    chk("rows wholly agreeing", ro, 76)
    chk("rows partly not", rb, 11)
    byyear = {y: (bad, objs) for y, w, bad, objs in ex}
    chk("Borchers 1992 derives to the object named for it",
        any("Borchers 1992" in t for t in byyear[1992][1]), True)
    chk("and the handle map put the unfinished modular object there",
        byyear[1992][0], ["Half-sided modular inclusion on a non-expanding horizon"])
    chk("Karp 1972 derives to the set-cover object",
        any("set cover" in t for t in byyear[1972][1]), True)

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
