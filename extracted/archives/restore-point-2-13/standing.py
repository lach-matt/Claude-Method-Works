#!/usr/bin/env python3
"""standing.py -- every closure condition of the Spectra Compendium, computed fresh.

Register 825. The compendium's closure is not one number. It is a set of conditions,
each with its own measure, and this computes all of them in one pass so the standing
can be read rather than assembled from memory.

    COVERAGE     E(X) on the channel set — what the structure implies and the table lacks
    VERIFICATION every mechanism's rate and 95% interval
    THE BRACKET  both forms, since they measure different things
    PROVENANCE   how many channels rest on a limit this work computed
    RESOLUTION   how many steps can be distinguished from their own error

A condition is CLOSED when its measure is at its ceiling and the ceiling is defensible.
A rate of 100% on three instances is not closed; a rate of 87% on 130 may be as closed
as the data permits. The distinction is the interval, not the rate.
"""
import re, math, itertools, glob, os, statistics as st
from collections import defaultdict, Counter
from zeno import State, step

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return (max(0.0, c-h), min(1.0, c+h))

ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"Ne":10,"Na":11,"Mg":12,
        "Al":13,"Si":14,"P":15,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,"Zn":30,
        "Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

def coverage():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    X = set()
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        try: X.add((ZNUM[el.group(1)], int(r[9]), LM[m.group(1)]))
        except Exception: pass
    A = [sorted({x[i] for x in X}) for i in range(3)]
    phi = {}
    for i in range(3):
        for j in range(3):
            if i == j: continue
            phi[(i,j)] = {v: (max([x[i] for x in X if x[j] <= v])
                              if [x[i] for x in X if x[j] <= v] else None) for v in A[j]}
    Rx = {c for c in itertools.product(*A) if all(
        phi[(i,j)][c[j]] is not None and c[i] <= phi[(i,j)][c[j]]
        for i in range(3) for j in range(3) if i != j)}
    miss = Rx - X
    lo = sum(1 for c in miss if c[2] <= 3)
    return len(X), len(Rx), len(miss), lo, len(rows)

def provenance():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    return Counter(r[11] if len(r) > 11 else "published" for r in rows)

CLAIMS = [
    # Re-measured against the current channel set at register 1048. `pverify.py` checks
    # the first six against the established scripts on every run; the rest are carried
    # from their registers and are the ones a future pverify should reach next.
    ("P.lcollapse",  "adjacent-l pairs ordered",           229, 230),   # R 1048, pverify
    ("P.mono/pen",   "penetration series falling",         146, 163),   # R 1048, two-claim
    ("P.mono/pol",   "polarisation series RISING",          52,  52),   # R 987, R 1048
    ("P.jj",         "J-pairs consistent",                 114, 129),   # R 1048, pverify
    ("P.charge",     "s/p ladders monotone at fixed Z",     37,  37),   # R 1048
    ("P.selfsame",   "disjoint windows agreeing",           67,  72),   # R 1048, pverify
    ("P.jsplit",     "open/heavy split, closed/light not",  29,  29),   # R 758
    ("P.iso",        "ladders and pairs monotone",          27,  28),   # R 894
    ("P.converge",   "limit within 3x the fit error",       38,  58),   # R 813
    ("P.dcollapse",  "iso exceptions that are d",           10,  10),   # R 719
    ("P.termsplit",  "terms separating, J-pairs together",  12,  15),   # R 826
    ("P.polar",      "high-l defect rising with Z",          6,   7),   # R 790, direction
    ("P.lens",       "high half wider than low",            44,  79),   # R 827 WEAKENED
    ("P.trunc",      "species gaining when untruncated",     4,   4),   # R 828
    ("P.qdt",        "independent confirmations",            4,   4),
    ("P.coreblind",  "parent-term pairs agreeing",           2,   2),   # R 845, R 947
    ("P.buildlimit", "constructed limits confirmed",         1,   1),   # R 816
    ("P.perturb",    "wide spreads with a named perturber",  1,   1),
]

with State("standing") as s:
    nX, nR, nMiss, missLo, nCh = step(s, "coverage: E(X) on the channel set",
                                      coverage, budget=600)
    prov = step(s, "provenance of every limit", provenance, budget=120)

print(f"  THE SPECTRA COMPENDIUM — closure standing\n")
print(f"  1 · COVERAGE")
print(f"      channels                 {nCh}")
print(f"      cells held  |X|          {nX}")
print(f"      recovered   |R(X)|       {nR}")
print(f"      E(X)                     {nMiss}      ({missLo} at l<=3, {nMiss-missLo} above)")
print(f"      closure fraction         {100*nX/nR:.1f}%")
print()
print(f"  2 · PROVENANCE OF THE LIMIT")
for k, v in prov.most_common():
    print(f"      {k:<24}{v:>5}   {100*v/nCh:>5.1f}%")
print()
print(f"  3 · VERIFICATION — every claim, with its interval")
print(f"      {'mechanism':<14}{'what':<38}{'k/n':>9}{'rate':>7}{'95% interval':>15}{'':>3}")
tot_at_ceiling = 0
for m, w, k, n in CLAIMS:
    lo, hi = wilson(k, n)
    width = hi - lo
    mark = "closed" if width <= 0.10 else ("near" if width <= 0.20 else "OPEN")
    tot_at_ceiling += mark == "closed"
    print(f"      {m:<14}{w:<38}{f'{k}/{n}':>9}{100*k/n:>6.0f}%"
          f"{f'{100*lo:.0f}-{100*hi:.0f}%':>15}   {mark}")
print()
print(f"      {tot_at_ceiling} of {len(CLAIMS)} claims have an interval of 10 points or less")
