#!/usr/bin/env python3
"""goaudit2.py -- R-D, repaired after F74.1.

WHY v1 FAILED: it matched keywords, and its selftest cases were written from its
own regexes, so it could not fail for the reason it named (R 1671).

WHAT v2 DOES INSTEAD: dataflow, not keywords.  A site is CONSTRUCT if the value
returned by ground_occ() reaches a SOLVER -- directly as an argument, or via a
name that is later passed to one.  It is SCORE only if it reaches a COMPARISON
and no solver.

GROUND TRUTH COMES FROM OUTSIDE THE CLASSIFIER.  The battery is built from sites
established by F73.3 (ci2b.py L38, rg.py L33 = CONSTRUCT) and from t7c_hfsr.py L72
(a print of a derived value against the table = SCORE).  If any battery case
misclassifies, rc=4 and NO row is written.
"""
import os, re, sys, json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(HERE, "..", "rt")

# Names that SOLVE a field.  Reaching one of these means the observed table
# entered the construction of something the project derives.
SOLVERS = r'(HFSR|HFCf|HFC|HF|scf_\w+|scf|zeta|run2|shoot\w*|solve\w*)'
SOLVER_CALL = re.compile(SOLVERS + r'\s*\(')

COMPARE = re.compile(r'(==|!=|\bin\b|\bset\s*\(|\bsorted\s*\(|- *set|\.get\()')

CALL = re.compile(r'ground_occ\s*\(')
IMPORT_RE = re.compile(r'^\s*(from|import)\s')
COMMENT = re.compile(r'^\s*#')


def reaches_solver(line, later_lines, varname=None):
    """Direct: ground_occ(...) sits inside a solver call on this line.
       Indirect: bound to a name that a later line passes to a solver."""
    if SOLVER_CALL.search(line):
        return True
    if varname:
        for l in later_lines:
            if re.search(r'\b' + re.escape(varname) + r'\b', l) and SOLVER_CALL.search(l):
                return True
    return False


def bound_name(line):
    m = re.match(r'\s*(?:[\w,\s\(\)]*?)\b(\w+)\s*=\s*[^=].*ground_occ', line)
    return m.group(1) if m else None


def classify(line, later_lines):
    s = line.rstrip()
    if COMMENT.match(s):
        return "COMMENT"
    if IMPORT_RE.match(s.strip()):
        return "IMPORT"
    if not CALL.search(s):
        return "MENTION"
    v = bound_name(s)
    if reaches_solver(s, later_lines, v):
        return "CONSTRUCT"
    if COMPARE.search(s):
        return "SCORE"
    return "UNCLASSIFIED"


def battery():
    """Ground truth established OUTSIDE this file.  Both directions."""
    cases = [
        # F73.3, established at s73 independently of any classifier:
        ("A = {(n,l):q for n,l,q in ground_occ(Z)}",
         ["V = slater(A,B)", "E,h = HFSR(Z, A).run2()"], "CONSTRUCT"),
        ("base = {(n,l):q for n,l,q in ground_occ(Z)}",
         ["cfg = promote(base)", "E = scf_pol_sr(Z,1,occ=cfg)"], "CONSTRUCT"),
        # direct solver argument:
        ("h=HFSR(Z,minus(ground_occ(Z),n,l,0.5),c=c)", [], "CONSTRUCT"),
        # comparison only, never solved:
        ("if tuple(ent) in ground_occ(Z): ok+=1", [], "SCORE"),
        ("from t5_scf import ground_occ", [], "IMPORT"),
        # a bound name that NEVER reaches a solver must NOT read CONSTRUCT:
        ("g = ground_occ(Z)", ["print(g)"], "UNCLASSIFIED"),
    ]
    bad = []
    for line, later, want in cases:
        got = classify(line, later)
        if got != want:
            bad.append((line[:60], got, want))
    if bad:
        print("BATTERY FAIL -- no row written:")
        for l, g, w in bad:
            print("   %-62s got=%-12s want=%s" % (l, g, w))
        sys.exit(4)
    print("BATTERY PASS: %d cases, both directions, ground truth from F73.3 not from regex." % len(cases))


def main():
    battery()
    rows = []
    for fn in sorted(os.listdir(RT)):
        if not fn.endswith(".py"):
            continue
        txt = open(os.path.join(RT, fn), encoding="utf-8", errors="replace").read().splitlines()
        for i, line in enumerate(txt):
            if "ground_occ" not in line:
                continue
            if line.strip().startswith("def ground_occ"):
                rows.append({"file": fn, "line": i + 1, "cls": "DEFINITION", "src": line.strip()})
                continue
            cls = classify(line, txt[i + 1:i + 40])
            rows.append({"file": fn, "line": i + 1, "cls": cls, "src": line.strip()[:170]})

    out = os.path.join(HERE, "GOAUDIT2.jsonl")
    with open(out, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    c = Counter(r["cls"] for r in rows)
    print("SITES=%d FILES=%d" % (len(rows), len({r['file'] for r in rows})))
    for k in ("DEFINITION", "IMPORT", "COMMENT", "MENTION", "SCORE", "CONSTRUCT", "UNCLASSIFIED"):
        if c.get(k):
            print("  %-13s %d" % (k, c[k]))
    print("written:", out)


if __name__ == "__main__":
    main()
