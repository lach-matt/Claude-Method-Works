#!/usr/bin/env python3
"""Artefact coverage: what the corpus names, against what the repo holds.

The books name their own working artefacts by filename -- handoffs, reading
slips, definitions, figures. This walks the two live bundles, collects every
such name, and reports whether the repo holds it. It answers one question:
*for every artefact the corpus refers to, is it here?*

Three statuses, and the third is the point:

  HELD             a file of that name exists somewhere in the repo
  IN-CHAT-BODY     absent as a file, but a chat shard carries its own title line,
                   so the document body is recoverable from that conversation
  IN-CHAT          absent as a file; the name is spoken in a chat shard, which
                   may be a passing mention rather than the content
  HELD-VIA-ALIAS   the image exists under its pre-rename source name, per the
                   mapping in CORPUS/FIGURE_ASSETS.md; only the renamed copy
                   has not been written
  ABSENT           no file of that name, and no alias, anywhere in the repo

``--chats`` resolves what is left against the sharded chat export in
``drive/chats``. That turns this census into a recovery index: for an artefact
the repo does not hold, ``held_as`` names the conversation to open.

**ABSENT is a census result, not a finding of loss.** A name in prose is not
proof a file ever existed, and the corpus refers to artefacts that were never
exported from the chat that made them. ABSENT means "not reachable from any
source in this repo" -- nothing more. It may not be quoted as evidence that an
artefact was lost or deleted.

Reference extraction is deliberately literal: a token that looks like a
filename. It does not follow prose ("the handoff for chat 40"), so the true
number of artefacts the work produced is higher than the number counted here.
The undercount is measurable: the bundles name 58 handoffs in filename shape but
refer to 88 distinct `HANDOFF-<n>` by bare number. Treat every ABSENT count as a
floor, never a total.

Regenerate:  python3 tools/coverage.py            # writes COVERAGE.tsv, prints the summary
Verify:      python3 tools/coverage.py --selftest

Stdlib only.
"""

import argparse
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUNDLES = (
    "method/The_Method_1_6_BUILD180_compendia_papers_audits.md",
    "method/The_Method_1_6_BUILD90_main_and_register.md",
)
FIGURE_ASSETS = "drive/The Method Materials/CORPUS/FIGURE_ASSETS.md"
CHATS = "drive/chats"
OUT = os.path.join(ROOT, "COVERAGE.tsv")

NAME_RE = re.compile(r"\b([A-Za-z0-9][A-Za-z0-9._-]{2,60}\.(?:md|png|py|tsv|csv|json|txt))\b")
EMBED_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
MAP_RE = re.compile(r"\|\s*Figure [^|]+\|\s*Figure [^|]+\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")

FAMILIES = (
    ("HANDOFF", re.compile(r"^HANDOFF[-.]")),
    ("READ", re.compile(r"^READ[-.]")),
    ("DEF", re.compile(r"^DEF-")),
    ("RULING", re.compile(r"^RULING-")),
    ("REGISTER", re.compile(r"^REGISTER-")),
    ("REWRITE", re.compile(r"^REWRITE-")),
    ("figure", re.compile(r"\.png$")),
    ("instrument", re.compile(r"\.py$")),
    ("data", re.compile(r"\.(?:tsv|csv|json)$")),
)


def family(name):
    for label, pattern in FAMILIES:
        if pattern.search(name):
            return label
    return "other"


def read_text(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def held_names():
    """Every basename present anywhere in the repo."""
    names = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        names.update(filenames)
    return names


def figure_aliases():
    """Renamed figure -> source file, from FIGURE_ASSETS.md."""
    path = os.path.join(ROOT, FIGURE_ASSETS)
    if not os.path.isfile(path):
        return {}
    doc = open(path, encoding="utf-8", errors="replace").read()
    return {target: source for source, target in MAP_RE.findall(doc)}


def referenced():
    """Every artefact filename the live bundles name."""
    names = set()
    for rel in BUNDLES:
        text = read_text(rel)
        names.update(NAME_RE.findall(text))
        for embed in EMBED_RE.findall(text):
            base = os.path.basename(embed.split()[0].strip("<>"))
            if "." in base:
                names.add(base)
    return names


def resolve_against_chats(rows):
    """Re-status ABSENT rows against the sharded chat export.

    One pass over the shards: collect the filename-shaped tokens each one
    speaks, and the heading stems it carries. A heading is the document's own
    title line, so it is evidence of the body rather than a mention; headings
    only mean that for Markdown, so the stronger status is claimed only there.
    """
    base = os.path.join(ROOT, CHATS)
    if not os.path.isdir(base):
        return rows, False
    absent = {r[0] for r in rows if r[2] == "ABSENT"}
    if not absent:
        return rows, True
    stems = {a[:-3]: a for a in absent if a.endswith(".md")}
    # NOT anchored with ^/re.M: inside a shard the newlines are JSON-escaped
    # "\\n" literals, so a line-anchored pattern matches nothing at all.
    heading = re.compile(r"#+[ \t]*([A-Za-z0-9][A-Za-z0-9._-]{2,60})")
    named, bodied = {}, {}
    for dirpath, _, names in os.walk(base):
        for name in sorted(names):
            if not name.endswith(".json") or name == "SUMMARY.json":
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, base)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for tok in set(NAME_RE.findall(text)):
                if tok in absent:
                    named.setdefault(tok, rel)
            for stem in set(heading.findall(text)):
                if stem in stems:
                    bodied.setdefault(stems[stem], rel)
    out = []
    for name, fam, status, via in rows:
        if status == "ABSENT" and name in bodied:
            out.append((name, fam, "IN-CHAT-BODY", bodied[name]))
        elif status == "ABSENT" and name in named:
            out.append((name, fam, "IN-CHAT", named[name]))
        else:
            out.append((name, fam, status, via))
    return out, True


def survey():
    held = held_names()
    alias = figure_aliases()
    rows = []
    for name in sorted(referenced()):
        if name in held:
            status, viaentry = "HELD", ""
        elif name in alias and alias[name] in held:
            status, viaentry = "HELD-VIA-ALIAS", alias[name]
        else:
            status, viaentry = "ABSENT", ""
        rows.append((name, family(name), status, viaentry))
    return rows


def report(rows):
    with open(OUT, "w") as fh:
        fh.write("artefact\tfamily\tstatus\theld_as\n")
        for row in rows:
            fh.write("\t".join(row) + "\n")
    grid = defaultdict(Counter)
    for name, fam, status, _ in rows:
        grid[fam][status] += 1
    total = Counter(r[2] for r in rows)
    print("Artefact coverage -- what the two live bundles name, against what the repo holds\n")
    print("%-12s %6s %6s %7s %8s %9s %8s"
          % ("family", "named", "held", "alias", "in-body", "in-chat", "ABSENT"))
    for fam in sorted(grid, key=lambda f: -sum(grid[f].values())):
        counts = grid[fam]
        print("%-12s %6d %6d %7d %8d %9d %8d" % (
            fam, sum(counts.values()), counts["HELD"], counts["HELD-VIA-ALIAS"],
            counts["IN-CHAT-BODY"], counts["IN-CHAT"], counts["ABSENT"]))
    print("%-12s %6d %6d %7d %8d %9d %8d" % (
        "TOTAL", len(rows), total["HELD"], total["HELD-VIA-ALIAS"],
        total["IN-CHAT-BODY"], total["IN-CHAT"], total["ABSENT"]))
    print("\nwritten: %s" % os.path.relpath(OUT, ROOT))
    print("ABSENT = not reachable from any source in this repo. Not a claim of loss:")
    print("a name in prose is not proof a file ever existed.")
    return 0


def selftest():
    """Fixtures are the corpus's own recorded numbers."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-52s = %-5s expected %-5s %s" % (label, got, want, "ok" if good else "FAIL"))

    alias = figure_aliases()
    check("main-volume figures mapped in FIGURE_ASSETS.md", len(alias), 33)
    held = held_names()
    check("all 33 mapped source images held", sum(1 for s in alias.values() if s in held), 33)

    rows = survey()
    absent = {n for n, f, s, _ in rows if s == "ABSENT"}
    check("renamed figures held only via their source name",
          sum(1 for r in rows if r[2] == "HELD-VIA-ALIAS"), 15)
    check("the one absent figure-<N.M> is the archived D.1 prior",
          sorted(n for n in absent if n.startswith("figure-")),
          ["figure-D.1-prior-32-elements.png"])
    check("papers' f<N>_<M>.png set absent in full",
          sum(1 for n in absent if re.match(r"^f\d+_\d+\.png$", n)), 25)
    check("HANDOFF names of filename shape", sum(1 for r in rows if r[1] == "HANDOFF"), 58)
    check("no row is both aliased and absent",
          sum(1 for r in rows if r[2] == "HELD-VIA-ALIAS" and r[3] == ""), 0)
    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chats", action="store_true",
                        help="resolve ABSENT artefacts against the sharded chat "
                             "export in drive/chats")
    parser.add_argument("--selftest", action="store_true",
                        help="assert the corpus's own recorded numbers and exit")
    args = parser.parse_args()
    if args.selftest:
        sys.exit(selftest())
    rows = survey()
    if args.chats:
        rows, ok = resolve_against_chats(rows)
        if not ok:
            print("no %s tree; nothing to resolve against.\n" % CHATS)
    sys.exit(report(rows))
