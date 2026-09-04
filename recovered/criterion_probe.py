#!/usr/bin/env python3
"""criterion_probe.py -- probe the register's own unfinished criterion.

Register 612: §2.24's rule applied to a criterion rather than a heuristic —
feed it cases whose answer you know before trusting what it says about cases
you do not.

Every combination of grade x named x checked x has-dependency is fed in, and
the verdict printed. A criterion that classifies a known case wrongly is a
broken instrument regardless of what the register currently contains.
"""
import itertools, sys
from zeno import State, step

def why(grade, dep, named, check):
    if grade in ("OPEN", "ASSERTED"): return "graded open"
    if not dep and not named: return "unnamed root"
    if grade in ("COMPUTED", "CITED") and not check: return "unverified"
    return None

GRADES = ["DEFINITIONAL", "PROVED", "COMPUTED", "CITED", "OPEN", "ASSERTED"]

# what the criterion SHOULD say, stated independently (§2.13: before reading)
def expected(grade, dep, named, check):
    if grade in ("OPEN", "ASSERTED"): return "graded open"
    # a root's name is its only identifier; a derived object is identified by
    # its derivation, so naming is optional there
    if not dep and not named: return "unnamed root"
    # a claim about the world must be checked; a definition need not be
    if grade in ("COMPUTED", "CITED") and not check: return "unverified"
    return None

def run():
    rows, bad = [], []
    for g, d, n, c in itertools.product(GRADES, [0, 1], [0, 1], [0, 1]):
        got = why(g, [1] if d else [], "x" if n else None, "x" if c else None)
        want = expected(g, [1] if d else [], "x" if n else None, "x" if c else None)
        rows.append((g, d, n, c, got, want))
        if got != want: bad.append((g, d, n, c, got, want))
    return rows, bad

with State("criterion_probe") as st:
    rows, bad = step(st, "probe the unfinished criterion", run, budget=120)

print(f"  {len(rows)} combinations probed\n")
print(f"  {'grade':<14}{'dep':>4}{'name':>5}{'chk':>4}   verdict")
seen = set()
for g, d, n, c, got, want in rows:
    key = (g, d, n, c)
    if key in seen: continue
    seen.add(key)
    print(f"  {g:<14}{d:>4}{n:>5}{c:>4}   {got or 'settled'}")
print(f"\n  disagreements with the stated expectation: {len(bad)}")
for b in bad: print(f"    {b}")
print("\n" + ("CRITERION PROBE PASSES" if not bad else f"FAILURES: {len(bad)}"))
sys.exit(1 if bad else 0)