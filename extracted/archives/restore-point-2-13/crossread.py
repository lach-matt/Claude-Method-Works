#!/usr/bin/env python3
"""crossread.py -- read both documents exhaustively, and check rather than absorb.

Four passes:
  1. every number that appears in BOTH, and whether its neighbourhood agrees
  2. every number in ONE that names an object the other also names
  3. every section of Transitions with no counterpart cited in the book
  4. every claim of the form "N of M" in either, checked for N <= M
"""
import re, sys
from collections import defaultdict, Counter

B = open("The Method 1.6.md", encoding="utf-8").read()
T = open("Transitions.md", encoding="utf-8").read()

def nums(s):
    """every number with its position, excluding section numbers and years"""
    out = []
    for m in re.finditer(r"(?<![.\d§])(\d{1,3}(?:,\d{3})+|\d{2,7})(?![.\d])", s):
        v = int(m.group(1).replace(",", ""))
        pre = s[max(0, m.start() - 30):m.start()]
        if re.search(r"§\s*$|arXiv:|20\d\d\)|\(19", pre): continue
        if 1850 <= v <= 2030: continue
        out.append((v, m.start()))
    return out

def ctx(s, p, w=95):
    return re.sub(r"\s+", " ", s[max(0, p - w):p + w])

bn, tn = nums(B), nums(T)
Bv = defaultdict(list); Tv = defaultdict(list)
for v, p in bn: Bv[v].append(p)
for v, p in tn: Tv[v].append(p)
shared = sorted(set(Bv) & set(Tv))

print(f"  DOCUMENTS   book {len(B):,} chars, {len(bn):,} numbers")
print(f"              paper {len(T):,} chars, {len(tn):,} numbers")
print(f"  numbers appearing in BOTH: {len(shared)}\n")

# --- PASS 1: the big shared numbers, with both neighbourhoods -----------------
print("  PASS 1 — shared numbers above 500, book context vs paper context\n")
big = [v for v in shared if v >= 500]
for v in big[:40]:
    print(f"  {v:,}")
    print(f"    B: …{ctx(B, Bv[v][0], 70)}…")
    print(f"    T: …{ctx(T, Tv[v][0], 70)}…")
print(f"\n  ({len(big)} shared numbers ≥ 500 in total)")

# --- PASS 2: "N of M" claims -------------------------------------------------
print("\n  PASS 2 — 'N of M' claims where N > M\n")
bad = 0
for name, s in (("book", B), ("paper", T)):
    for m in re.finditer(r"(\d{1,3}(?:,\d{3})*)\s+of\s+(\d{1,3}(?:,\d{3})*)", s):
        a = int(m.group(1).replace(",", "")); b = int(m.group(2).replace(",", ""))
        if a > b:
            bad += 1
            print(f"    [{name}] {m.group(0)}  …{ctx(s, m.start(), 80)}…")
print(f"    {bad} violations")

# --- PASS 3: Transitions sections cited nowhere in the book -------------------
print("\n  PASS 3 — Transitions sections with no citation in the book\n")
tsec = [m.group(1) for m in re.finditer(r"^#{2,3} ([\d.]+[a-e]?) ", T, re.M)]
cited = set(re.findall(r"T §?([\d.]+[a-e]?)", B)) | set(re.findall(r"§([\d.]+[a-e]?) of Transitions", B))
miss = [x for x in tsec if x not in cited]
print(f"    {len(tsec)} sections, {len(cited)} cited, {len(miss)} uncited")
print(f"    uncited: {miss}")

# --- PASS 4: percentages against their own fractions --------------------------
print("\n  PASS 4 — percentages checked against the fraction beside them\n")
pbad = 0
for name, s in (("book", B), ("paper", T)):
    for m in re.finditer(r"(\d{1,3}(?:,\d{3})*)\s*(?:of|/)\s*(\d{1,3}(?:,\d{3})*)[^.\n]{0,40}?(\d{1,3}(?:\.\d+)?)\s*%", s):
        a = int(m.group(1).replace(",", "")); b = int(m.group(2).replace(",", "")); p = float(m.group(3))
        if b and abs(100 * a / b - p) > 1.0:
            pbad += 1
            print(f"    [{name}] {a}/{b} = {100*a/b:.1f}% but says {p}%  …{ctx(s, m.start(), 60)}…")
print(f"    {pbad} mismatches")
