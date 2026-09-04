#!/usr/bin/env python3
"""coords.py -- the coordinate supply, as a table the book can read.

Register 1215. The Spectra Compendium's purpose is to hand Λ values. Everything
else in it — the mechanisms, the equation, the propagation — exists to produce
those values or to state their standing. This writes the values themselves.

    (Z, charge, l, 2S+1)  ->  delta,  grade,  source

GRADES, in order of standing:
    exact        forced by symmetry: delta = 0 at Ne = 1
    measured     fitted to captured levels against a limit
    derived      propagated along a sequence, or bounded by aufbau
    computed     supplied by the channel equation, domain stated

Nothing is ungraded. A value with no provenance is not a coordinate.
"""
import json, math, csv
from collections import Counter

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z+1; _z += 2*(2*_l+1)

A, E0, E1, K, HH = 0.3772, 0.8297, -0.0900, 0.4942, 0.5415

def _load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return ns["config"], ns["mults"], ns["measured"]()

config, mults, MEAS = _load()
MEAS = dict(MEAS)
# the five out-of-sample captures of this session
MEAS.update({(38,2,0,2):2.7113,(38,2,1,2):2.3501,(38,2,2,2):1.4577,(38,2,3,2):0.0618,
             (38,2,4,2):0.0098,(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,
             (22,4,3,2):0.0774,(7,4,0,1):0.2948,(7,4,1,1):0.1782,(7,4,2,1):0.0335,
             (20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,
             (19,3,0,2):1.6589,(19,3,1,2):1.2110})

def corb(ne, l): return sum(1 for n, ll, o in config(ne) if ll == l and o > 0)
def n0f(ne, l):
    v = [n for n, ll, o in config(ne) if ll == l and o > 0]
    return (max(v)+1) if v else l+1
def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0, cap, 1, cap-1) else {0:1, 1:3, 2:16, 3:119}.get(l, 8)

def equation(Z, c, l):
    ne = Z-c+1; p = corb(ne-1, l); t = math.log(c+1)/c
    if p > 0:
        return A*(p**max(E0 + E1*math.log(max(ne,2)), 0.05))*ne**K*t
    thr = OPEN.get((n0f(ne-1, l), l), 999)
    C = min(max((Z-thr+4.0)/8.0, 0.0), 1.0)
    return HH*C*((ne-1)/ne)*ne**K*t

def status(Z, c, l):
    ne = Z-c+1
    if Z > 103:  return "improbable", "element too short-lived"
    if c > 10:   return "improbable", "no analysed data at this charge"
    if l > 4:    return "improbable", "series unresolved above ng"
    if parents(config(ne-1)) > 1:
        return "improbable", f"open-shell core, {parents(config(ne-1))} parents"
    if Z > 92:   return "improbable", "not naturally occurring"
    return "possible", "separable series, not yet measured"

rows = []
for Z in range(1, 119):
    for c in range(1, Z+1):
        ne = Z-c+1
        for S in mults(ne):
            for l in range(8):
                k = (Z, c, l, S)
                B = min(corb(ne-1, l), n0f(ne-1, l)-l-1)
                if k in MEAS:
                    rows.append((Z, c, l, S, round(MEAS[k], 5), "measured",
                                 "captured levels", B, "verified"))
                elif ne == 1:
                    rows.append((Z, c, l, S, 0.0, "exact",
                                 "one electron, delta = 0 by symmetry", B, "verified"))
                else:
                    st, why = status(Z, c, l)
                    rows.append((Z, c, l, S, round(equation(Z, c, l), 5), "computed",
                                 "the channel equation", B, st))

with open("COORDINATES.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["Z","charge","l","mult","delta","grade","source","B","status"])
    w.writerows(rows)

g = Counter(r[5] for r in rows); s = Counter(r[8] for r in rows)
print(f"  COORDINATES.tsv — {len(rows):,} rows")
print("      by grade : " + " · ".join(f"{k} {v:,}" for k, v in g.most_common()))
print("      by status: " + " · ".join(f"{k} {v:,}" for k, v in s.most_common()))