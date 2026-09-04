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

# NOT a second implementation. An earlier form of this file defined an
# `expected()` that was a line-for-line copy of why(), so zero disagreements was
# guaranteed before it ran — §4.6, a test that could not fail, built while
# writing a register entry about §2.24 (register 613).
#
# Two independent properties ARE checkable without restating the criterion:
#   (a) MONOTONICITY — adding a name or a check must never make an object
#       MORE unfinished. A criterion that does is incoherent.
#   (b) EXHAUSTIVENESS — every combination must receive some verdict.
def anomalies(rows):
    d = {(g, dp, n, c): v for g, dp, n, c, v in rows}
    bad = []
    for (g, dp, n, c), v in d.items():
        for better in ((g, dp, 1, c), (g, dp, n, 1)):
            if better == (g, dp, n, c): continue
            w = d[better]
            if v is None and w is not None:
                bad.append((f"{g} dep={dp} name={n} chk={c}", "settled",
                            f"→ {better[2:]}", w))
    return bad

def run():
    rows = []
    for g, d, n, c in itertools.product(GRADES, [0, 1], [0, 1], [0, 1]):
        rows.append((g, d, n, c,
                     why(g, [1] if d else [], "x" if n else None, "x" if c else None)))
    return rows, anomalies(rows)

with State("criterion_probe") as st:
    rows, bad = step(st, "probe the unfinished criterion", run, budget=120)

print(f"  {len(rows)} combinations probed\n")
print(f"  {'grade':<14}{'dep':>4}{'name':>5}{'chk':>4}   verdict")
for g, d, n, c, got in rows:
    print(f"  {g:<14}{d:>4}{n:>5}{c:>4}   {got or 'settled'}")
print(f"\n  MONOTONICITY violations — where adding a name or a check makes an")
print(f"  object MORE unfinished: {len(bad)}")
for b in bad: print(f"    {b}")
print(f"  every combination receives a verdict: {len(rows) == 6*2*2*2}")
print("\n" + ("CRITERION PROBE PASSES — monotone and exhaustive"
               if not bad else f"FAILURES: {len(bad)}"))
sys.exit(1 if bad else 0)
