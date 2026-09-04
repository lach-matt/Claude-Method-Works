#!/usr/bin/env python3
"""goaudit.py -- R-D, ruled at s74.  F73.3 audit.
Classify EVERY ground_occ call site as IMPORT / SCORE / CONSTRUCT / UNCLASSIFIED.

THE QUESTION THIS ANSWERS, AND IT IS THE ONLY ONE:
  ground_occ(Z) returns the OBSERVED ground configuration from a table.
  A SCORE use compares a derived result against it -- legitimate.
  A CONSTRUCT use builds the field / configuration being derived FROM it -- circular.

CAN-FAIL: the classifier is verified in both directions before any site is read
(see --selftest): a known SCORE line must classify SCORE and a known CONSTRUCT
line must classify CONSTRUCT, or the instrument exits rc=4 and no row is written.
"""
import os, re, sys, json

RT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "rt")

IMPORT_RE = re.compile(r'^\s*(from|import)\s')

# CONSTRUCT markers: the returned occupancy flows into something that is SOLVED.
CONSTRUCT_HINT = re.compile(r'''
      occ\s*=          # bound as the occupancy that gets solved
    | \bscf\s*\(       # fed to an SCF driver
    | \bsolve\w*\s*\(
    | \bbuild\w*\s*\(
    | \bfield\w*\s*\(
    | cfg_?A\s*=       # s73: configuration A constructed from it
    | \bconf\w*\s*=
''', re.X)

# SCORE markers: the returned occupancy is COMPARED, printed, or diffed.
SCORE_HINT = re.compile(r'''
      ==            | \!=
    | \bin\b\s      | \bset\s*\(
    | obs\w*\s*=    | ref\w*\s*=
    | \bcompare\b   | \bmatch\b   | \bdiff\b
    | \bprint\b     | \bcheck\b
''', re.X)


def classify(line):
    s = line.strip()
    if IMPORT_RE.match(s):
        return "IMPORT"
    if CONSTRUCT_HINT.search(s):
        return "CONSTRUCT"
    if SCORE_HINT.search(s):
        return "SCORE"
    return "UNCLASSIFIED"


def selftest():
    """Can-fail gate.  Both directions, before any real row is read."""
    cases = [
        ("from t5_scf import ground_occ",            "IMPORT"),
        ("occ = ground_occ(Z)",                      "CONSTRUCT"),
        ("if tuple(ent) == ground_occ(Z)[-1]:",      "SCORE"),
        ("zzz(ground_occ(Z))",                       "UNCLASSIFIED"),
    ]
    bad = [(l, classify(l), w) for l, w in cases if classify(l) != w]
    if bad:
        for l, got, want in bad:
            print("SELFTEST FAIL: %-40s got=%s want=%s" % (l, got, want))
        sys.exit(4)
    print("SELFTEST PASS: classifier separates all four classes (can-fail, both directions).")


def main():
    selftest()
    rows = []
    for fn in sorted(os.listdir(RT)):
        if not fn.endswith(".py"):
            continue
        p = os.path.join(RT, fn)
        try:
            txt = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except Exception:
            continue
        for i, line in enumerate(txt, 1):
            if "ground_occ" not in line:
                continue
            if line.strip().startswith("def ground_occ"):
                rows.append({"file": fn, "line": i, "cls": "DEFINITION",
                             "src": line.strip()})
                continue
            rows.append({"file": fn, "line": i, "cls": classify(line),
                         "src": line.strip()[:160]})

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GOAUDIT.jsonl")
    with open(out, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    from collections import Counter
    c = Counter(r["cls"] for r in rows)
    print("SITES=%d  FILES=%d" % (len(rows), len({r["file"] for r in rows})))
    for k in ("DEFINITION", "IMPORT", "SCORE", "CONSTRUCT", "UNCLASSIFIED"):
        print("  %-14s %d" % (k, c.get(k, 0)))
    print("written:", out)


if __name__ == "__main__":
    main()
