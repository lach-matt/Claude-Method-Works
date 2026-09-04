#!/usr/bin/env python3
"""isoelectronic.py -- does the ladder drop for every element, or only for neon?

Register 717. Ne I gives 1.29 / 0.84 / 0.015 across s, p, d and Ne II gives
0.93 / 0.62 / 0.07 / 0. Every rung lower in the ion. The question is whether
that is neon or whether it is general.

This tests every element in the compendium that has two or more ionisation
stages, comparing the defect at each l. Nothing is transcribed; it reads
SPECTRA-DATA.tsv.

The prediction, if the effect is real: for a given element and a given l, the
defect must FALL as the charge rises, because the outer electron sees a tighter
potential and penetrates less of the core.
"""
import re, statistics as st
from collections import defaultdict
from zeno import State, step

LMAP = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6}
ROMAN = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6}

def run():
    rows = [l.rstrip("\n").split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    # element -> stage -> l -> [defects]
    D = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for r in rows:
        if len(r) < 8: continue
        m = re.match(r"([A-Z][a-z]?)\s+([IVX]+)$", r[0].strip())
        if not m: continue
        el, st_ = m.group(1), ROMAN.get(m.group(2))
        if st_ is None: continue
        lm = re.search(r"n([spdfghi])\b", r[1])
        if not lm: continue
        try: d = float(r[7])
        except Exception: continue
        D[el][st_][LMAP[lm.group(1)]].append(d)
    return D

with State("isoelectronic") as s:
    D = step(s, "test the ladder across every element", run, budget=300)

multi = {e: v for e, v in D.items() if len(v) > 1}
print(f"  {len(D)} elements in the compendium, {len(multi)} with two or more stages\n")
print(f"  {'element':<9}{'l':<4}" + "".join(f"{'stage '+str(k):>12}" for k in (1,2,3)) + "   verdict")
tested = drops = 0
for el in sorted(multi):
    stages = sorted(multi[el])
    ls = sorted({l for k in stages for l in multi[el][k]})
    for l in ls:
        vals = {k: st.mean(multi[el][k][l]) for k in stages if multi[el][k][l]}
        if len(vals) < 2: continue
        tested += 1
        ks = sorted(vals)
        ok = all(vals[a] > vals[b] for a, b in zip(ks, ks[1:]))
        if ok: drops += 1
        row = f"  {el:<9}{'spdfghi'[l]:<4}"
        for k in (1,2,3):
            row += f"{vals[k]:>12.4f}" if k in vals else f"{'—':>12}"
        print(row + f"   {'falls' if ok else 'RISES'}")
print(f"\n  {tested} element-l pairs with two or more stages")
print(f"  {drops} fall as charge rises, {tested-drops} rise")
