#!/usr/bin/env python3
"""predict_test.py -- can the mechanisms predict a defect they have not seen?

Register 763. The proposal is that with enough elements the compendium could
predict the spectra of the sixteen where none has been measured. Before that is
worth attempting, the mechanisms must be shown to predict an element they DO
have — with that element withheld.

Method: for each element and l, remove it entirely, fit the surviving data with
P.polar's linear-in-Z form (for l >= 4) or P.iso's charge dependence, predict the
withheld value, and compare.

A mechanism that cannot predict a measured element cannot predict an unmeasured
one, and the size of the error here is the honest bound on any extrapolation.
"""
import re, statistics as st
from collections import defaultdict
from zeno import State, step

Z = {"He":2,"Li":3,"C":6,"Ne":10,"Na":11,"Mg":12,"Al":13,"Si":14,"Ar":18,"Ca":20,
     "Sc":21,"Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83,"K":19,"N":7,"Be":4}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

def run():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    D = defaultdict(list)
    for r in rows:
        m = re.match(r"([A-Z][a-z]?)\s+([IVX]+)", r[0].strip())
        lm = re.search(r"n([spdfghik])\b", r[1])
        if not (m and lm) or m.group(1) not in Z: continue
        try: d = float(r[7])
        except Exception: continue
        D[(m.group(1), LM[lm.group(1)])].append(d)
    pts = {k: st.mean(v) for k, v in D.items() if len(v) >= 1}

    out = []
    for l in range(0, 7):
        at_l = [(Z[e], d, e) for (e, ll), d in pts.items() if ll == l]
        if len(at_l) < 4: continue
        for zi, di, ei in at_l:
            rest = [(a, b) for a, b, _ in at_l if _ != ei]
            if len(rest) < 3: continue
            zs = [a for a, _ in rest]; ds = [b for _, b in rest]
            mz, md = st.mean(zs), st.mean(ds)
            den = sum((a-mz)**2 for a in zs)
            if den == 0: continue
            slope = sum((a-mz)*(b-md) for a, b in rest)/den
            pred = md + slope*(zi-mz)
            out.append((l, ei, zi, di, pred, abs(pred-di)))
    return out

with State("predict_test") as s:
    out = step(s, "leave one element out and predict it", run, budget=300)

print(f"  {'l':<3}{'element':<9}{'Z':>4}{'measured':>11}{'predicted':>11}{'error':>10}")
by = defaultdict(list)
for l, e, z, d, p, err in sorted(out):
    by[l].append((err, abs(d)))
    print(f"  {'spdfghi'[l]:<3}{e:<9}{z:>4}{d:>11.4f}{p:>11.4f}{err:>10.4f}")
print()
print(f"  {'l':<3}{'tests':>7}{'median error':>15}{'median |defect|':>18}{'error/defect':>14}")
for l in sorted(by):
    v = by[l]
    me = st.median([a for a, _ in v]); mdf = st.median([b for _, b in v])
    print(f"  {'spdfghi'[l]:<3}{len(v):>7}{me:>15.4f}{mdf:>18.4f}"
          f"{(me/mdf if mdf > 1e-6 else float('inf')):>14.2f}")
