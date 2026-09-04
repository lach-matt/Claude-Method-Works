#!/usr/bin/env python3
"""determine.py -- bracket a missing defect from everything the compendium establishes.

Register 841. Register 839 bracketed eleven cells using P.iso alone, along one axis.
But the compendium establishes several relations, and a missing cell can be constrained
by all of them at once. Each contributes a one-sided or two-sided bound, and the
intersection is the answer.

    P.lcollapse   delta falls monotonically with l.  145/145.
                  -> delta(l) < delta(l-1) and delta(l) > delta(l+1)
    P.iso         delta falls monotonically with charge along a sequence.  23/24.
                  -> delta(c) < delta(c-1) and delta(c) > delta(c+1)
    hydrogenic    delta -> 0 as charge -> infinity, and delta -> 0 as l grows.
                  -> delta > 0 wherever the neighbours are positive
    P.coreblind   the defect does not depend on the parent term.  9/9.
                  -> a measured cell at another core DETERMINES this one
    P.jsplit      in a closed-shell light species the J components do not split.
                  -> one J determines the other

The first four give BOUNDS; P.coreblind gives a VALUE. They are reported separately,
because a bracket and a determination are not the same claim and the compendium has
been careful to keep them apart (registers 834, 840).
"""
import re, statistics as st
from collections import defaultdict
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
INV = {v: k for k, v in ZNUM.items()}
ROM = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI"}

def held():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    out = defaultdict(list)
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        try: out[(ZNUM[el.group(1)], int(r[9]), LM[m.group(1)])].append(float(r[7]))
        except Exception: pass
    return {k: st.mean(v) for k, v in out.items()}

def bracket(H):
    """for every cell adjacent to measured ones, the tightest bound each relation gives"""
    out = []
    cand = set()
    for (Z, c, l) in H:
        for dz, dc, dl in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,1,0),(-1,-1,0)]:
            k = (Z+dz, c+dc, l+dl)
            if k not in H and 1 <= k[0] <= 118 and 1 <= k[1] <= 5 and 0 <= k[2] <= 7 and k[0] > k[1]:
                cand.add(k)
    for (Z, c, l) in sorted(cand):
        lo, hi, why = 0.0, None, []
        # --- P.lcollapse, along l at fixed (Z, c)
        a = H.get((Z, c, l-1))
        if a is not None:
            hi = a if hi is None else min(hi, a); why.append(f"l<{('spdfghik')[l-1]}")
        b = H.get((Z, c, l+1))
        if b is not None:
            lo = max(lo, b); why.append(f"l>{('spdfghik')[l+1]}")
        # --- P.iso, along charge at fixed electron count (Z-c constant)
        a = H.get((Z-1, c-1, l))
        if a is not None:
            hi = a if hi is None else min(hi, a); why.append("iso<")
        b = H.get((Z+1, c+1, l))
        if b is not None:
            lo = max(lo, b); why.append("iso>")
        if hi is None or hi <= lo: continue
        out.append((Z, c, l, lo, hi, hi-lo, "+".join(why)))
    return out

def determine(H):
    """P.coreblind gives a VALUE, not a bound — but only within one spectrum"""
    return []          # requires parent-term resolution the channel table does not carry

with State("determine") as s:
    H  = step(s, "read what is measured",            held,               budget=120)
    BR = step(s, "bracket from every monotone relation", lambda: bracket(H), budget=300)

two = [b for b in BR if b[6].count("+") >= 1]
print(f"  MISSING CELLS BRACKETED BY THE COMPENDIUM'S OWN RELATIONS\n")
print(f"      cells adjacent to measured ones and bracketed : {len(BR)}")
print(f"      of those, constrained from TWO OR MORE sides  : {len(two)}")
print(f"      register 839 had, from P.iso alone            : 11")
print()
print(f"  {'element':>9}{'chg':>5}{'l':>3}{'bracket on delta':>26}{'width':>9}  from")
for Z, c, l, lo, hi, w, why in sorted(BR, key=lambda x: x[5])[:22]:
    print(f"  {INV.get(Z,Z):>9}{ROM.get(c,c):>5}{'spdfghik'[l]:>3}"
          f"{f'{lo:.4f} - {hi:.4f}':>26}{w:>9.4f}  {why}")
if len(BR) > 22: print(f"  ... and {len(BR)-22} more")
print()
tight = [b for b in BR if b[5] < 0.05]
print(f"  {len(tight)} brackets are narrower than 0.05 — tight enough to be a")
print(f"  useful prediction rather than a formality.")
