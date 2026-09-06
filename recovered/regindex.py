#!/usr/bin/env python3
"""regindex.py -- the register, indexed and closed.

Cells are register entries. Coordinates are assigned from the entry text, never
by hand. The bounds are not imposed: R recovers them, and what it recovers is
reported as the index's own law.

  corroboration  0 narrative · 1 owed · 2 object carried, unreferenced
                 3 object carried with a § reference
  caught         0 by hand · 1 by an instrument · 2 from outside the book
  repair         0 recorded, not repaired · 1 instance fixed · 2 class fixed
                 3 a protocol or an audit was created
  fibre          the four-body layer: OBJECT · LAW · PROCEDURE · REFERENCE
"""
import re, sys, itertools
from collections import Counter, defaultdict
from zeno import State, step

S = open("The Method 1.4.md", encoding="utf-8").read()
RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
T = S[RS:RE_]

MATH = re.compile(r"[=≤≥<>≠∈⊆∏Σ√∎]|\bE\(|\bℛ\(|φ̂|ⅅ|\bΛ|theorem|proof|lemma|proposition"
                  r"|\b\d[\d,]{2,}\b|\d+(?:\.\d+)?%|Baker|Pixley|Bergman|Birkhoff|Dilworth"
                  r"|Racah|Freuder|Montanari|Dechter|Deville|Brylawski|Nesterov|Aitken|Sperner")
SUBJ = re.compile(r"closure|closed|defect|arity|tree|cycle|density|fibrat|coordinate|bracket"
                  r"|monoton|coupling|seniority|precedent|attribut", re.I)
NARR = re.compile(r"cross-reference|heading|numbering|contents|markup|emphasis|apostrophe|stale"
                  r"|prepend|indent|renumber|caption|glyph|font|whitespace|dpi|the press"
                  r"|hardcode|literal|regex", re.I)

def coords(txt):
    ref = bool(re.search(r"§[\dA-G]", txt))
    if MATH.search(txt):   corr = 3 if ref else 2
    elif SUBJ.search(txt): corr = 1
    else:                  corr = 0
    if NARR.search(txt) and not MATH.search(txt): corr = min(corr, 0)
    if re.search(r"from outside|companion paper|referee|literature|precedent|located", txt, re.I):
        caught = 2
    elif re.search(r"audit|the script|the press|instrument|detector|tripwire", txt, re.I):
        caught = 1
    else:
        caught = 0
    if re.search(r"a protocol at|§2\.\d+ (?:now )?(?:says|states|exists)|audit \d+ (?:exists|added|defined)"
                 r"|now says|a \w+ audit", txt, re.I):        rep = 3
    elif re.search(r"the class|repaired the class|all \w+ (?:now|are) ", txt, re.I): rep = 2
    elif re.search(r"repaired|corrected|entered|defined|closed|withdrawn|swapped|renumbered",
                   txt, re.I):                                 rep = 1
    else:                                                      rep = 0
    if re.search(r"referent|conflat|ungrounded|precedent|attribut|cited|Condon|Racah", txt, re.I):
        fib = "REFERENCE"
    elif re.search(r"audit|protocol|register|press|build|contents|heading", txt, re.I):
        fib = "PROCEDURE"
    elif re.search(r"closure|E\(|theorem|law|arity|monoton|density", txt):
        fib = "LAW"
    else:
        fib = "OBJECT"
    return (corr, caught, rep), fib

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return ({x for x in itertools.product(*A)
             if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}, phi)

def build():
    pat = re.compile(r"^ {0,3}((?:\d{3}, )*\d{3})\. ", re.M)
    ms = list(pat.finditer(T)); rows = []
    for i, m in enumerate(ms):
        end = ms[i+1].start() if i+1 < len(ms) else len(T)
        nums = [int(x) for x in re.findall(r"\d{3}", m.group(1))]
        c, f = coords(T[m.end():end])
        for n in nums: rows.append((n, c, f))
    return rows

with State("regindex") as st:
    rows = step(st, "assign coordinates to every entry", build, budget=120)

print(f"  entries indexed: {len(rows)}   distinct: {len({r[0] for r in rows})}")
cells = {r[1] for r in rows}
box = 4 * 3 * 4
Rx, phi = R(cells, 3)
print(f"  distinct cells occupied: {len(cells)} of a box of {box}   density {100*len(cells)/box:.1f}%")
print(f"  |R(X)| = {len(Rx)}   E(register) = {len(Rx)-len(cells)}")

print("\n  the bounds ℛ RECOVERS -- the register's own law, not imposed:")
NM = ["corroboration", "caught", "repair"]
for (i, j), env in sorted(phi.items()):
    if len(set(env.values())) > 1:
        print(f"    {NM[i]:<14} ≤ f({NM[j]:<14})  {dict(sorted(env.items()))}")

print("\n  fibred by the four-body layer:")
byf = defaultdict(set); cnt = Counter()
for n, c, f in rows: byf[f].add(c); cnt[f] += 1
for f in ("OBJECT", "LAW", "PROCEDURE", "REFERENCE"):
    if byf[f]:
        Rf, _ = R(byf[f], 3)
        print(f"    {f:<10} {cnt[f]:>4} entries  {len(byf[f]):>3} cells  E = {len(Rf)-len(byf[f])}")

print("\n  the distributions the index now makes readable:")
for k, idx, names in (("corroboration", 0, ["narrative","owed","carried, unreferenced","carried + §"]),
                      ("caught",        1, ["by hand","by an instrument","from outside"]),
                      ("repair",        2, ["not repaired","instance","class","a protocol or audit"])):
    d = Counter(r[1][idx] for r in rows)
    print(f"    {k}")
    for v in sorted(d):
        print(f"      {names[v]:<24}{d[v]:>4}  {100*d[v]/len(rows):>5.1f}%")
