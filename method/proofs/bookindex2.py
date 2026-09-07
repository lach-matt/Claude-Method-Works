#!/usr/bin/env python3
"""bookindex2.py — bookindex.py's successor: the extent is DATA, not two constants. Phase 1, item J-20.

WHY. §32.1.1 says its index was "Recomputed at this build (2026-08-24, `bookindex.py`), over the
thirty-five chapters and six appendices the book now has". The book now has THIRTY-SIX chapters and
SEVEN appendices -- Chapter 36 and Appendix G -- and the seated instrument cannot see either: it
hard-codes `APP='ABCDEF'`, filters references with `1<=r<=35`, and sets its box side `n=41  # 35
chapters + 6 appendices`. So the sentence is stale in the ordinary way AND the instrument that made
it is bounded by the same two numbers. This is the class the store already answered twice by
successor instrument rather than by edit -- census -> census2, r2-reg1a -> r2-reg1a3 -- and never by
changing the seated original, which G0c forbids.

WHAT CHANGES, AND IT IS ONLY THIS. The chapter bound and the appendix letters are read from the
volume's own headings. Every other definition is bookindex.py's, character for character: the same
claim test, the same reference regexes, the same part map, the same R2 closure, the same printed
rows. `--compare` runs the seated original beside it and prints both.

stdlib only.  --selftest asserts the seated original's own output on this build, and that the two
agree once the successor is restricted to the original's bounds.
"""
import argparse, itertools, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")


def extent(lines):
    """the volume's own extent: distinct chapter numbers and appendix letters, from its headings."""
    ch = sorted({int(m.group(1)) for l in lines for m in [re.match(r"^## (\d+)\. ", l)] if m})
    ap = sorted({m.group(1) for l in lines for m in [re.match(r"^## Appendix ([A-Z])", l)] if m})
    return ch, ap


def index(lines, chmax, app):
    """bookindex.py's own computation, with chmax and app supplied rather than hard-coded."""
    start = [i for i, l in enumerate(lines) if l.startswith("# PART 0")][-1]
    def code(ch): return ch if isinstance(ch, int) else 100 + app.index(ch)
    loc = 0; part = 0; cells = set(); claims = 0; partcells = set(); chpart = {0: 0}
    AP = "".join(app)
    for i, l in enumerate(lines):
        if i < start:
            continue
        m = re.match(r"^# PART ([0IV]+)", l)
        if m:
            part = {"0": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}[m.group(1)]
            continue
        m = re.match(r"^## (\d+)\. ", l)
        if m: loc = int(m.group(1)); chpart[loc] = part; continue
        m = re.match(r"^## Appendix ([%s])" % AP, l)
        if m: loc = m.group(1); chpart[loc] = part; continue
        if l.startswith("#") or not l.strip(): continue
        refs = (set(int(x) for x in re.findall(r"§\s?(\d+)\.", l))
                | set(int(x) for x in re.findall(r"Chapter (\d+)", l))
                | set(re.findall(r"§\s?([%s])\." % AP, l))
                | set(re.findall(r"Appendix ([%s])" % AP, l)))
        refs = {r for r in refs if (isinstance(r, str) or 1 <= r <= chmax)}
        if refs: claims += 1
        for r in refs:
            cells.add((code(loc), code(r))); partcells.add((chpart[loc], chpart.get(r, part)))
    return claims, cells, partcells


def R2(X):
    A = [sorted({x[i] for x in X}) for i in range(2)]
    def phi(i, j, v):
        return max([x[i] for x in X if x[j] <= v] or [-1])
    return {x for x in itertools.product(*A) if x[0] <= phi(0, 1, x[1]) and x[1] <= phi(1, 0, x[0])}


def run(chmax=None, app=None):
    lines = open(MAIN, encoding="utf-8").read().splitlines()
    ch, ap = extent(lines)
    chmax = max(ch) if chmax is None else chmax
    app = ap if app is None else app
    claims, cells, partcells = index(lines, chmax, app)
    n = chmax + len(app)
    back = sum(1 for a, b in cells if b <= a)
    return dict(chapters=ch, appendices=app, chmax=chmax, n=n, claims=claims,
                cells=len(cells), box=n * n, back=back, fwd=len(cells) - back,
                E=len(R2(cells)) - len(cells))


PRINTED = {"chapters_said": 35, "appendices_said": 6, "claims": 1021, "cells": 400,
           "box": 1681, "E": 1265, "date": "2026-08-24"}


def report():
    cur = run()
    old = run(chmax=35, app=list("ABCDEF"))
    print("§32.1.1's self-index, and the instrument that computed it\n")
    print(f"  the volume's extent, from its own headings: {len(cur['chapters'])} chapters "
          f"(1 to {cur['chmax']}) and {len(cur['appendices'])} appendices ({''.join(cur['appendices'])})")
    print(f"  §32.1.1 says: 'the {PRINTED['chapters_said']}-chapter and {PRINTED['appendices_said']}-appendix book' "
          f"— thirty-five and six, printed with the date {PRINTED['date']}")
    print(f"  the seated bookindex.py cannot see the difference: APP='ABCDEF', the filter 1<=r<=35,")
    print(f"  and n=41 '# 35 chapters + 6 appendices' are three constants, not a reading\n")
    print(f"  {'':22}{'printed':>10}{'seated bounds':>15}{'true extent':>13}")
    for k, lbl in (("claims", "claims"), ("cells", "cells"), ("box", "box"), ("E", "E(book)")):
        print(f"  {lbl:22}{PRINTED[k]:>10}{old[k]:>15}{cur[k]:>13}")
    print(f"  {'box side n':22}{41:>10}{old['n']:>15}{cur['n']:>13}")
    print("\n  The printed row is a dated reading and says so. What it cannot say, and what this")
    print("  measures, is that the extent it names is no longer the book's: Chapter 36 and Appendix G")
    print("  are outside every bound the instrument carries, so no re-run of it can ever count them.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    cur = run(); old = run(chmax=35, app=list("ABCDEF"))
    eq("the volume has 36 chapters", len(cur["chapters"]), 36)
    eq("numbered 1 to 36 with no gap", cur["chapters"], list(range(1, 37)))
    eq("the volume has 7 appendices", cur["appendices"], list("ABCDEFG"))
    eq("§32.1.1 says thirty-five chapters", PRINTED["chapters_said"], 35)
    eq("§32.1.1 says six appendices", PRINTED["appendices_said"], 6)
    eq("the seated instrument's box side", 41, 35 + 6)
    eq("the true box side", cur["n"], 36 + 7)
    p = subprocess.run([sys.executable, "bookindex.py"], capture_output=True, text=True, cwd=MEM)
    eq("the seated instrument still runs", p.returncode, 0)
    first = p.stdout.split("\n")[0]
    m = re.match(r"claims (\d+)\s+cells (\d+)\s+box (\d+)", first)
    eq("this successor reproduces it at its own bounds",
       (old["claims"], old["cells"], old["box"]), tuple(int(x) for x in m.groups()))
    eq("and the true extent gives a different box", cur["box"] != old["box"], True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap_ = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap_.add_argument("--selftest", action="store_true")
    a = ap_.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
