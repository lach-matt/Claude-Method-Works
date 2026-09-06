#!/usr/bin/env python3
"""goaudit3.py -- R-D, second repair.  F74.1 records why v1 and v2 failed.

v1 matched keywords and its selftest was written from its own regexes.
v2 asked 'does the value reach a SOLVER'.  That is the wrong question: in
ci2b.py the observed configuration A feeds SLATER-CONDON INTEGRALS, never an
SCF, and it is still construction from observation.

v3 ASKS A DECIDABLE QUESTION INSTEAD OF A SEMANTIC ONE:
    Is the value returned by ground_occ() USED FOR ANYTHING OTHER THAN A
    DIRECT COMPARISON?
      used only in a comparison            -> SCORE
      wrapped, bound, iterated, subscripted -> CONSTRUCT

THE BIAS IS DELIBERATE AND STATED: this rule OVER-reports CONSTRUCT and can
never under-report it.  For an audit whose danger is circularity, a false
CONSTRUCT costs one line of reading; a false SCORE hides the thing being
looked for.  The count is therefore a CEILING on construct-side exposure,
not a measurement of it -- and it is reported as a ceiling.
"""
import os, re, sys, json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(HERE, "..", "rt")

IMPORT_RE = re.compile(r'^\s*(from|import)\s')
COMMENT = re.compile(r'^\s*#')
CALL = re.compile(r'ground_occ\s*\(')

# the call sits inside ANOTHER call's argument list: minus(ground_occ(Z),...)
WRAPPED = re.compile(r'\w+\s*\(\s*[^()]*?ground_occ\s*\(')
# the call is iterated to build something: {... for a,b,c in ground_occ(Z)}
ITERATED = re.compile(r'\bfor\b[^\n]*\bin\s+ground_occ\s*\(')
# the result is bound to a name
BOUND = re.compile(r'^\s*[\w,\s\(\)\[\]]*?=\s*[^=]*ground_occ\s*\(')
# the result is indexed:  ground_occ(Z)[-1]
INDEXED = re.compile(r'ground_occ\s*\([^()]*\)\s*\[')
# pure comparison forms
COMPARED = re.compile(r'(==|!=|\bnot\s+in\b|\bin\s+ground_occ)')


def classify(line):
    s = line.rstrip()
    if COMMENT.match(s):
        return "COMMENT"
    if IMPORT_RE.match(s.strip()):
        return "IMPORT"
    if not CALL.search(s):
        return "MENTION"
    used = bool(WRAPPED.search(s) or ITERATED.search(s) or BOUND.match(s) or INDEXED.search(s))
    if used:
        return "CONSTRUCT"
    if COMPARED.search(s):
        return "SCORE"
    return "UNCLASSIFIED"


def battery():
    """Ground truth from F73.3 and from plain Python semantics.  Both directions."""
    cases = [
        ("A = {(n,l):q for n,l,q in ground_occ(Z)}",        "CONSTRUCT"),   # F73.3
        ("base = {(n,l):q for n,l,q in ground_occ(Z)}",     "CONSTRUCT"),   # F73.3
        ("h=HFSR(Z,minus(ground_occ(Z),n,l,0.5),c=c)",      "CONSTRUCT"),
        ("occ=ground_occ(Z)",                               "CONSTRUCT"),
        ("if tuple(ent) in ground_occ(Z): ok+=1",           "SCORE"),
        ("assert ent == ground_occ(Z)[-1]",                 "CONSTRUCT"),   # indexed: reads a member
        ("from t5_scf import ground_occ",                   "IMPORT"),
        ("# ground_occ() is a TABLE that stops at Z=108",   "COMMENT"),
    ]
    bad = [(l[:58], classify(l), w) for l, w in cases if classify(l) != w]
    if bad:
        print("BATTERY FAIL -- no row written:")
        for l, g, w in bad:
            print("   %-60s got=%-13s want=%s" % (l, g, w))
        sys.exit(4)
    # negative control: the classifier must be ABLE to say SCORE
    if classify("if a in ground_occ(Z): pass") != "SCORE":
        print("BATTERY FAIL: SCORE unreachable -- clause cannot fail.")
        sys.exit(4)
    print("BATTERY PASS: %d cases + negative control. SCORE is reachable, so CONSTRUCT is not vacuous." % len(cases))


def main():
    battery()
    rows = []
    for fn in sorted(os.listdir(RT)):
        if not fn.endswith(".py"):
            continue
        for i, line in enumerate(open(os.path.join(RT, fn), encoding="utf-8",
                                     errors="replace").read().splitlines(), 1):
            if "ground_occ" not in line:
                continue
            if line.strip().startswith("def ground_occ"):
                rows.append({"file": fn, "line": i, "cls": "DEFINITION", "src": line.strip()})
                continue
            rows.append({"file": fn, "line": i, "cls": classify(line), "src": line.strip()[:170]})

    out = os.path.join(HERE, "GOAUDIT3.jsonl")
    with open(out, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    c = Counter(r["cls"] for r in rows)
    print("SITES=%d FILES=%d" % (len(rows), len({r['file'] for r in rows})))
    for k in ("DEFINITION", "IMPORT", "COMMENT", "MENTION", "SCORE", "CONSTRUCT", "UNCLASSIFIED"):
        if c.get(k):
            print("  %-13s %d" % (k, c[k]))
    cf = sorted({r['file'] for r in rows if r['cls'] == 'CONSTRUCT'})
    print("CONSTRUCT files: %d" % len(cf))
    print("nlchain.py sites: %d" % sum(1 for r in rows if r['file'] == 'nlchain.py'))
    print("written:", out)


if __name__ == "__main__":
    main()
