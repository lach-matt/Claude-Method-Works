#!/usr/bin/env python3
"""vii5read.py -- the reading (VII5) asks for, held against the census that makes it finite (vii5census.py).

Part VII Lemma 3.1 (proof5/PART-VII-ASSEMBLY.md) averages over O(4) the linear maps given by existence statements (C3),
their families in b (C3') and one complement (C4), and says the proofs of Parts III-IV use those objects "only through
the conditions stated at the sites listed". vii5census.py lists every line of Parts III-IV that names one of them by its
printed symbol outside its site. checks/VII5-READING.tsv records, for each such line, a reader's verdict:
  SITE-ONLY   only the site's conditions are used (or consequences any object meeting them shares);
  NAMING      the line names, cites or restates; no property of the choice is used;
  MORE        a property of the particular choice beyond them is used (the finding that matters);
  UNDECIDED   the reader could not tell;
  HOMONYM     the spelling names another object.
A MORE or UNDECIDED row must carry a resolution: where it is answered, or why the averaged choice still has the property.

  Q1 (computed, a census) The table's lines are exactly the census's use lines for C3, C3', the object built from C3'
     and C4 -- none missing, none extra, none twice -- each with the census's symbols, a verdict from the list above,
     a note where one is required, and the symbol still printed on that line of the file (a stale line number fails).
  Q2 (computed) Every MORE and UNDECIDED row carries a resolution. The counts per verdict are printed.
  Controls: the table with one row dropped, with one row doubled, with a verdict misspelt, with a resolution removed,
     and the census widened by one radial cut-off (chi_9, treated as if averaged) must each fail.

Lemma 3.1's (C3) names since D608 the 1-form towers of every type, with their site PART-III-I10-CORR4.md:127-147; the
census keeps those lines as uses, and they were read as such (each NAMING, a definition).

Labels: computed (that the reading covers every listed use and is complete in form); the verdicts are READ (each
reader's reading of the proof at that line), not computed. Reach: vii5census.py's -- a literal census of printed
symbols.

Run: python3 checks/vii5read.py   (a second)
"""
import csv
import os
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vii5census as V                                                           # noqa: E402

TABLE = os.path.join(HERE, "VII5-READING.tsv")
VERDICTS = ("SITE-ONLY", "NAMING", "MORE", "UNDECIDED", "HOMONYM")
NEED_NOTE = ("MORE", "UNDECIDED", "HOMONYM")
NEED_RES = ("MORE", "UNDECIDED")


def say(s, indent="      "):
    print("\n".join(textwrap.wrap(s, 119, subsequent_indent=indent, break_long_words=False,
                                   break_on_hyphens=False)), flush=True)


def entries(widen=False):
    out = [e for name, es in V.GROUPS if name.startswith(("C3", "C4")) for e in es]
    if widen:
        out += [e for name, es in V.GROUPS if name.startswith("C1") for e in es if e[0] == "\\chi_9"]
    return out


def uses(es):
    """{(file, line): set of symbols used there (not at their site)}"""
    hits = V.census(es, V.files())
    out = {}
    for k, v in hits.items():
        used = {s for s, site in v.items() if not site}
        if used:
            out[k] = used
    return out


def load():
    with open(TABLE, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter="\t")]


def q1(rows, es, show=True):
    want = uses(es)
    seen, bad = {}, []
    text = {}
    for r in rows:
        k = (r["file"], int(r["line"]))
        seen[k] = seen.get(k, 0) + 1
        syms = {s.strip() for s in r["symbols"].split("|")}
        if k in want and syms != want[k]:
            bad.append("%s:%d symbols %s, census %s" % (k[0], k[1], sorted(syms), sorted(want[k])))
        if r["verdict"] not in VERDICTS:
            bad.append("%s:%d verdict %r" % (k[0], k[1], r["verdict"]))
        if r["verdict"] in NEED_NOTE and not r["note"].strip():
            bad.append("%s:%d %s without a note" % (k[0], k[1], r["verdict"]))
        if k[0] not in text:
            text[k[0]] = open(os.path.join(V.P5, k[0]), encoding="utf-8").read().split("\n")
        line = text[k[0]][k[1] - 1] if k[1] <= len(text[k[0]]) else ""
        if not all(s in line for s in syms):
            bad.append("%s:%d no longer prints %s" % (k[0], k[1], sorted(syms)))
    missing = sorted(set(want) - set(seen))
    extra = sorted(set(seen) - set(want))
    twice = sorted(k for k, n in seen.items() if n > 1)
    ok = not (missing or extra or twice or bad)
    if show:
        say("  Q1: %d census use lines (C3, C3', the built object, C4) in %d files; table rows %d; missing %d, extra %d,"
            " doubled %d, malformed %d" % (len(want), len({f for f, _ in want}), len(rows), len(missing), len(extra),
                                           len(twice), len(bad)))
        for x in (missing[:5] + extra[:5] + twice[:5]):
            print("      %s:%d" % x, flush=True)
        for x in bad[:10]:
            say("      " + x)
    return ok


def q2(rows, show=True):
    count = {v: 0 for v in VERDICTS}
    unres = []
    for r in rows:
        count[r["verdict"]] = count.get(r["verdict"], 0) + 1
        if r["verdict"] in NEED_RES and not r.get("resolution", "").strip():
            unres.append("%s:%s" % (r["file"], r["line"]))
    if show:
        say("  Q2: " + ", ".join("%s %d" % (v, count[v]) for v in VERDICTS) +
            "; MORE/UNDECIDED rows without a resolution: %d" % len(unres))
        for r in rows:
            if r["verdict"] in NEED_RES:
                say("      %s:%s %s [%s] %s -- resolution: %s" % (r["file"], r["line"], r["verdict"], r["symbols"],
                                                                 r["note"], r.get("resolution", "")), "        ")
    return not unres


def control(rows):
    es = entries()
    dropped = rows[1:]
    doubled = rows + rows[:1]
    misspelt = [dict(r) for r in rows]
    misspelt[0]["verdict"] = "SITE ONLY"
    unresolved = [dict(r) for r in rows]
    tgt = [i for i, r in enumerate(unresolved) if r["verdict"] in NEED_RES]
    if tgt:
        unresolved[tgt[0]]["resolution"] = ""
    else:                                   # no MORE/UNDECIDED row: plant one without a resolution
        unresolved[0]["verdict"], unresolved[0]["note"], unresolved[0]["resolution"] = "MORE", "planted", ""
    fails = [not q1(dropped, es, False), not q1(doubled, es, False), not q1(misspelt, es, False),
             not q2(unresolved, False), not q1(rows, entries(widen=True), False)]
    say("  control: dropped row fails %s; doubled row fails %s; misspelt verdict fails %s; resolution removed fails %s;"
        " census widened by chi_9 fails %s" % tuple(fails))
    return all(fails)


def main():
    rows = load()
    a = q1(rows, entries())
    b = q2(rows)
    c = control(rows)
    print("Q1 %s; Q2 %s; control %s" % ("PASS" if a else "FAIL", "PASS" if b else "FAIL",
                                       "behaves" if c else "MISBEHAVES"), flush=True)
    return 0 if a and b and c else 1


if __name__ == "__main__":
    sys.exit(main())
