#!/usr/bin/env python3
"""Gap 4: disjunctive edges. The closure operator is rewritten.

A profile is CONSISTENT iff:
  (a) closed under positive (forcing) edges
  (b) violates no negative (forbidding) edge
  (c) every disjunction whose antecedent is broken has >=1 disjunct broken

Disjuncts may lie OUTSIDE the box (instability, locality, energy-momentum).
Extra-box disjuncts are always available: adopting them costs nothing the
box can measure.  This is the honest reading - and it is why a disjunction
is NOT the same as the forcing edge it was collapsed to.
"""
from itertools import combinations

BOX = ["T", "H", "L", "U", "DN", "C", "E", "SD", "Rdf", "Rdi"]
OUT = ["inst", "loc", "em"]          # leaked vertices, no edges retrieved

POS = [("T", "H"), ("T", "E"), ("T", "L"), ("T", "DN"), ("T", "U"),
       ("DN", "C"), ("SD", "C"), ("H", "U"), ("L", "C"), ("Rdi", "H")]

NEG = [("Rdf", "T"), ("Rdi", "T")]

# antecedent -> list of disjuncts (any one suffices)
DISJ = [("E",  ["inst", "C"],            "Buniy+: NEC violation => instability OR superluminal"),
        ("C",  ["T", "Rdf", "Rdi"],      "Visser/BBN: superluminal + causality => extra structure"),
        ("U",  ["loc", "em"],            "Banks-Susskind-Peskin"),
        ("DN", ["C"],                    "discrimination => cloning OR signalling (cloning is DN itself)"),
       ]

def close(S):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b in POS:
            if a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

def neg_ok(S):
    return not any(a in S and b in S for a, b in NEG)

def disj_ok(S, allow_extrabox=True):
    for ant, disjuncts, _ in DISJ:
        if ant in S:
            sat = any(d in S for d in disjuncts if d in BOX)
            if allow_extrabox:
                sat = sat or any(d in OUT for d in disjuncts)
            if not sat:
                return False
    return True

def run(allow_extrabox, label):
    closed = {close(c) for r in range(len(BOX)+1) for c in combinations(BOX, r)}
    ok = {c for c in closed if neg_ok(c) and disj_ok(c, allow_extrabox)}
    mins = [c for c in ok if c and not any(d < c and d for d in ok)]
    print(f"\n  {label}")
    print(f"    consistent profiles   {len(ok)} of {len(closed)} closed")
    print(f"    empty profile ok?     {frozenset() in ok}")
    print(f"    minimal profiles      "
          f"{', '.join('{'+','.join(sorted(c))+'}' for c in sorted(mins, key=lambda s:(len(s),sorted(s))))}")
    return ok, set(mins)

print("="*72)
print("  GAP 4 CLOSED: disjunctive edges implemented")
print("="*72)
a_ok, a_min = run(True,  "extra-box disjuncts AVAILABLE  (instability/locality/em acceptable)")
b_ok, b_min = run(False, "extra-box disjuncts BLOCKED    (must discharge inside the box)")

print("\n" + "="*72)
print("  WHAT THE DISJUNCTIONS COST")
print("="*72)
print(f"  is {{E}} minimal when extra-box allowed?   "
      f"{frozenset({'E'}) in a_min}")
print(f"  is {{E}} minimal when extra-box blocked?   "
      f"{frozenset({'E'}) in b_min}")
print(f"  is {{C}} minimal when extra-box allowed?   "
      f"{frozenset({'C'}) in a_min}")
print(f"  is {{U}} minimal when extra-box allowed?   "
      f"{frozenset({'U'}) in a_min}")
print(f"  is {{U}} minimal when extra-box blocked?   "
      f"{frozenset({'U'}) in b_min}")
print(f"\n  profiles lost by blocking extra-box discharge: "
      f"{len(a_ok) - len(b_ok)}")
print(f"  => {len(a_ok)-len(b_ok)} profiles exist ONLY because the box leaks")
