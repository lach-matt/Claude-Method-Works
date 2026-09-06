#!/usr/bin/env python3
"""recat.py -- structural mechanism, or operation?

The current taxonomy sorts the principles by WHETHER AN EXPRESSION EXISTS, which
is a property of the writing. The proposal sorts them by WHAT KIND OF THING THEY
ARE. That is only an improvement if it explains the verdicts of batch 3 rather
than relabelling them.

  MECHANISM  a fact about an index. settled by proof or computation.
  OPERATION  a thing an agent does. settled by the failure it prevents.

One-hot test, per Transitions §8.4: a principle predicating on BOTH is a
RELATION between the structure and the working, and cannot be content of either.

Committed before computing: the OPEN / PARTIAL / CONDITIONAL / ASSERTED verdicts
will land on the weight-2 principles.
"""
import itertools, sys
from collections import Counter
from zeno import State, step

# (id, statement, predicates-on, batch-3 verdict)
P = [
 ("P1","a complete index is self-referencing",              {"MECH"},        "PROVED"),
 ("P2","a complete index is self-defending",                {"MECH"},        "CONDITIONAL"),
 ("P3","work backwards from the desired output",            {"OP"},          "ASSERTED"),
 ("P4","always audit results",                              {"OP"},          "NOT CORROBORABLE"),
 ("P5","compute the result before assuming it",             {"OP"},          "NOT CORROBORABLE"),
 ("P6","when a question is confusing, reframe it",          {"OP"},          "NOT CORROBORABLE"),
 ("P7","all questions must close",                          {"MECH","OP"},   "OPEN"),
 ("P8","any true answer is a bound",                        {"MECH","OP"},   "PROVED"),
 ("P9","the first dimension; every other a perspective",    {"MECH"},        "PARTIAL"),
 ("P10","allow continued expansions",                       {"MECH"},        "PROVED"),
 ("P11","close all gaps before continuing",                 {"OP"},          "NOT CORROBORABLE"),
 ("P12","every test run against every cell",                {"MECH","OP"},   "PROVED"),
 ("P13","coherence not claimed while a caveat stands",      {"MECH","OP"},   "DEFINITIONAL"),
 ("P14","a structural problem suggests a structural fix",   {"OP"},          "NOT CORROBORABLE"),
 ("P15","use the index to navigate; fetch in pieces",       {"OP"},          "NOT CORROBORABLE"),
 ("P16","treat bounds and limits as coordinate values",     {"MECH","OP"},   "NOT CORROBORABLE"),
 ("P17","the path is always through the bounds",            {"MECH","OP"},   "OPEN"),
 ("P18","a work comprehending an index is itself an index", {"MECH"},        "OPEN"),
 ("P19","complete only when no questions remain",           {"MECH"},        "PROVED"),
 ("P20","the language bounds whether a question closes",    {"MECH"},        "COMPUTED"),
 ("P21","every definition true in every language",          {"MECH","OP"},   "COMPUTED"),
 ("P22","no lie can exist within a complete index",         {"MECH"},        "PARTIAL"),
 ("P23","complete only when no question can ever be had",   {"MECH"},        "NOT CORROBORABLE"),
]
SETTLED = {"PROVED","COMPUTED","DEFINITIONAL","NOT CORROBORABLE"}

def test():
    w = {p[0]: len(p[2]) for p in P}
    rows = []
    for pid, stmt, on, verdict in P:
        rows.append((pid, len(on), "+".join(sorted(on)), verdict,
                     "settled" if verdict in SETTLED else "UNSETTLED"))
    return rows

with State("recat") as st:
    rows = step(st, "one-hot the principles", test, budget=30)

print(f"  {'':<5}{'weight':>7}  {'predicates on':<12}{'batch-3 verdict':<20}status")
for pid, w, on, v, st_ in rows:
    print(f"  {pid:<5}{w:>7}  {on:<12}{v:<20}{st_}")

w1 = [r for r in rows if r[1] == 1]
w2 = [r for r in rows if r[1] == 2]
print(f"\n  weight 1 (content of one category): {len(w1)}")
print(f"    unsettled among them: {sum(1 for r in w1 if r[4]=='UNSETTLED')}"
      f"  -> {[r[0] for r in w1 if r[4]=='UNSETTLED']}")
print(f"  weight 2 (a RELATION between structure and working): {len(w2)}")
print(f"    unsettled among them: {sum(1 for r in w2 if r[4]=='UNSETTLED')}"
      f"  -> {[r[0] for r in w2 if r[4]=='UNSETTLED']}")

# the committed prediction, scored
pred = {r[0] for r in rows if r[1] == 2}
actual = {r[0] for r in rows if r[4] == "UNSETTLED"}
tp = len(pred & actual); fp = len(pred - actual); fn = len(actual - pred)
print(f"""
  THE COMMITTED PREDICTION, SCORED
    predicted unsettled (weight 2) : {sorted(pred)}
    actually unsettled             : {sorted(actual)}
    hit {tp}   predicted-and-settled {fp}   unsettled-and-weight-1 {fn}
""")
if fn:
    print(f"  REFUTED in part: {sorted(actual-pred)} are unsettled and predicate on ONE category.")
    for pid in sorted(actual - pred):
        r = next(x for x in rows if x[0] == pid)
        print(f"    {pid}  {r[2]:<8} {r[3]}")
if fp:
    print(f"\n  and {sorted(pred-actual)} are weight 2 and SETTLED, so weight 2 does not force"
          f"\n  an open verdict either.")
print(f"""
  WHAT THE SPLIT ACTUALLY DOES
    it removes the demand for an expression from {len([r for r in rows if r[2]=='OP'])} operations,
    which dissolves the mismatch that made P3 'asserted' and left the seven
    procedural principles looking deficient.
    it does NOT settle the {fn} mechanism{'s' if fn!=1 else ''} that are open on their own terms.""")
