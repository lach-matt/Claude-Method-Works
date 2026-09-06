#!/usr/bin/env python3
"""refindex.py -- the vocabulary of reference, as an index, then applied.

The book carries 51 index terms and none of them says what a term points at.
This defines that vocabulary the way the book defines any vocabulary: ordered
coordinates, one categorical fibre, constraints of §16.4 form, closed.

COORDINATES

  access     can the referent be reached at all?      (Transitions App. B)
             0 blocked  1 secondary  2 abstract  3 full text
  referent   how much of the referent is carried?     (Transitions App. A, §10.3)
             0 none  1 named  2 named with its stated hypothesis
  checked    against how much of the naming literature? (audit 22)
             0 not checked  1 against one theorem  2 against every theorem naming it
  verdict    what the check returned                   (audit 22's own column)
             0 undetermined  1 conflated  2 partial  3 match

  fibre: KIND -- coordinate | equation | source | result

CONSTRAINTS, each binding one coordinate by a monotone function of one other

  referent <= f(access)    you cannot state a hypothesis you cannot read
  checked  <= f(referent)  you cannot check a term against a referent you have not named
  verdict  <= f(checked)   an unchecked term has no verdict

NOT A COORDINATE

  repair -- none | dictionary | split | translator -- is a function of verdict
  and referent, so by §1.7 it inflates the box and cannot repair closure. It is
  read off, never carried.
"""
import itertools
from zeno import State, step

ACCESS   = ["blocked", "secondary", "abstract", "full text"]
REFERENT = ["none", "named", "named with hypothesis"]
CHECKED  = ["not checked", "one theorem", "every theorem naming it"]
VERDICT  = ["undetermined", "conflated", "partial", "match"]
AX = [ACCESS, REFERENT, CHECKED, VERDICT]

def admissible(a, r, c, v):
    if r > 0 and a < 1: return False          # a named referent needs a reachable source
    if r > 1 and a < 2: return False          # a stated hypothesis needs the text
    if c > 0 and r < 1: return False          # no check without a referent
    if c > 1 and r < 2: return False          # exhaustive check needs the hypothesis
    if v > 0 and c < 1: return False          # no verdict without a check
    return True

CELLS = {(a, r, c, v) for a in range(4) for r in range(3)
         for c in range(3) for v in range(4) if admissible(a, r, c, v)}

def R(X, d):
    A = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def close():
    Rx = R(CELLS, 4)
    box = 1
    for a in AX: box *= len(a)
    return Rx, box

def repair(cell):
    a, r, c, v = cell
    if r == 0:            return "TRANSLATOR -- a referent must be manufactured"
    if v == 1:            return "SPLIT -- two meanings under one letter"
    if v == 2:            return "DICTIONARY -- one meaning, two bases"
    if v == 0:            return "unpaid -- the check has not been run"
    return "none"

with State("refindex") as st:
    Rx, box = step(st, "close the reference index", close, budget=60)

print(f"  cells                {len(CELLS)}")
print(f"  ambient box          {box}")
print(f"  density              {100*len(CELLS)/box:.1f}%")
print(f"  |R(X)|               {len(Rx)}")
print(f"  E(reference)         {len(Rx)-len(CELLS)}")
print(f"  possibility bound    0 <= E <= {box-len(CELLS)}")
print(f"  constraint graph     access — referent — checked — verdict : a path, "
      f"4 nodes 3 edges, width 1")

# ---------------------------------------------------------------- applied
print("\n\n  APPLIED TO THE CORPUS\n")
TERMS = [
 # (term, kind, access, referent, checked, verdict, source of the reading)
 ("n, l  (Lambda)",        "coordinate", 3, 1, 1, 1, "T §10.3 exact in hydrogen, labels elsewhere"),
 ("k, q, g  occupancies",  "coordinate", 3, 1, 1, 1, "T §10.3 conflated, 7 of 13"),
 ("q  (transfer)",         "coordinate", 3, 0, 0, 0, "T §10.3 NO REFERENT IN THE LITERATURE"),
 ("2S, 2S'",               "coordinate", 3, 2, 1, 3, "Condon-Shortley, reproduced by audit 23"),
 ("v  seniority",          "coordinate", 3, 2, 1, 3, "Racah 1943"),
 ("2J_c",                  "coordinate", 3, 2, 1, 3, "Racah 1942"),
 ("2K",                    "coordinate", 3, 1, 1, 2, "T §2.1b scheme-contingent -- a dictionary case"),
 ("X causal ladder",       "coordinate", 3, 1, 1, 1, "T §6.1 spontaneous vs explicit"),
 ("U unitarity",           "coordinate", 3, 1, 1, 1, "T §6.1 open-system vs ghosts"),
 ("NEC",                   "coordinate", 3, 1, 1, 1, "T §6.1 ANEC vs achronal ANEC"),
 ("L linearity",           "coordinate", 3, 1, 1, 1, "T §6.1 dynamical vs kinematical"),
 ("SD microcausality",     "coordinate", 3, 1, 1, 1, "T §6.1 observables vs fields"),
 ("S_corr",                "coordinate", 3, 2, 1, 3, "T §6.1 clean, a measured number"),
 ("IC",                    "coordinate", 3, 1, 0, 0, "T §6.4 NEVER CHECKED ONCE, load-bearing"),
 ("R(X) = X",              "result",     1, 1, 1, 3, "Baker-Pixley via Bergman, reg. 224"),
 ("E(X) = 0",              "result",     2, 1, 1, 3, "2-decomposability, Kimura 2024, reg. 226"),
 ("the certificate",       "result",     3, 2, 2, 1, "Freuder vs Dechter -- CONFLATED, found this session"),
 ("staircase / monotone",  "result",     3, 1, 0, 0, "Deville 1999, located and not yet entered"),
 ("V = 4nu/3",             "result",     1, 1, 1, 2, "M §27.4 four owners of the framing"),
 ("lambda^2",              "result",     3, 2, 1, 3, "Nesterov-Nemirovskii 1994"),
 ("the n-body index",      "result",     2, 1, 1, 1, "Brylawski 1973, reg. 355"),
 ("Edlen Handbuch 1964",   "source",     0, 1, 0, 0, "M §27.6 blocked, rho <= 2"),
 ("Ritz 1908 PZ",          "source",     0, 1, 0, 0, "M §27.6 blocked"),
 ("Paschen & Gotze 1922",  "source",     0, 1, 0, 0, "M §27.6 blocked, Q item B"),
 ("Dunz 1911",             "source",     0, 1, 0, 0, "M §27.6 blocked"),
 ("Kreuzer-Skarke file",   "source",     1, 1, 0, 0, "Q item D, a file format"),
 ("the 15 equations",      "equation",   3, 2, 1, 3, "T App. A, hypotheses now supplied"),
 ("the other 35 equations","equation",   3, 2, 0, 0, "T App. A, stated, never checked against use"),
]

bad = [(t, c) for t, k, *c4, s in TERMS for c in [tuple(c4)] if c not in CELLS]
print(f"  terms placed: {len(TERMS)}   cells they occupy: {len({tuple(t[2:6]) for t in TERMS})}"
      f"   inadmissible placements: {len(bad)}")
if bad:
    for t, c in bad: print(f"    INADMISSIBLE {t} at {c}")

occ = {tuple(t[2:6]) for t in TERMS}
print(f"\n  E over the terms actually placed: {len(R(occ,4)) - len(occ)}"
      f"   (the corpus occupies {len(occ)} of {len(CELLS)} admissible cells)")

print(f"\n  {'term':<24}{'kind':<12}{'acc':>4}{'ref':>4}{'chk':>4}{'vrd':>4}   repair owed")
for t, k, a, r, c, v, s in TERMS:
    print(f"  {t:<24}{k:<12}{a:>4}{r:>4}{c:>4}{v:>4}   {repair((a,r,c,v))}")

from collections import Counter
print("\n  THE DEBT, counted")
print(f"    terms with NO referent (translator owed)   "
      f"{sum(1 for t in TERMS if t[3]==0)}")
print(f"    terms named but never checked (unpaid)     "
      f"{sum(1 for t in TERMS if t[3]>0 and t[4]==0)}")
print(f"    terms checked and conflated (split owed)   "
      f"{sum(1 for t in TERMS if t[5]==1)}")
print(f"    terms checked and partial (dictionary)     "
      f"{sum(1 for t in TERMS if t[5]==2)}")
print(f"    terms matching                            "
      f"{sum(1 for t in TERMS if t[5]==3)}")
print(f"    terms blocked at the source                "
      f"{sum(1 for t in TERMS if t[2]==0)}")
print(f"\n    checked at all: {sum(1 for t in TERMS if t[4]>0)} of {len(TERMS)}"
      f"  = {100*sum(1 for t in TERMS if t[4]>0)/len(TERMS):.0f}%")
