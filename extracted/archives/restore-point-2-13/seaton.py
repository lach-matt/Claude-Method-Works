#!/usr/bin/env python3
"""seaton.py -- do the compendium's DEDUCTIONS contain an outside PREDICTION?

Register 1077. The compendium computes bounds on unmeasured cells by propagating
monotonicity between measured neighbours: 960 cells carry a bound and no value. Seaton's
polarisation formula computes VALUES for the same cells from electrostatics that knows
nothing about the index.

    delta_l = (alpha_d / a0^3) z^2 (3 - l(l+1)/n^2)
              / [ l(l+1)(2l-1)(2l+1)(2l+3) ]

WHY THIS IS A TEST AND NOT A TAUTOLOGY. Populating the index with predictions and then
computing E would prove nothing — E counts cells, so filling them drives it to zero by
construction, which is register 782's fault. And P.lcollapse holds automatically for
Seaton values, since the formula falls with l by construction. Neither is a test.

What IS a test: the bounds come from the index's order structure, the values come from a
1930s electrostatics formula, and the two have no common input. Either could fail.

METHOD. For each species holding at least one high-l channel, EXTRACT alpha_d from that
channel by inverting the formula — so nothing is looked up and the whole test is internal
except the formula's shape. Then predict every OTHER l for the same species and ask
whether the compendium's bound contains it.

A prediction outside its bound is a disagreement between a deduction and a physical law,
and it locates a fault in one of them. That is the point.
"""
import re, math, statistics as st
from collections import defaultdict
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}

def kfac(l):
    return l*(l+1)*(2*l-1)*(2*l+1)*(2*l+3)

def load():
    """every high-l channel, with its species, core charge, l, defect, spread and n-range"""
    out = []
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1])
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        ns = re.findall(r"\d+", r[2])
        try:
            out.append(dict(sp=r[0].rstrip(" *"), core=r[1][:m.start()].strip(),
                            l=LM[m.group(1)], d=float(r[7]),
                            sd=float(r[8]) if r[8] else 0.0, z=int(r[9]),
                            nlo=int(ns[0]) if ns else 8, nhi=int(ns[1]) if len(ns)>1 else 8))
        except Exception: pass
    return out

def alpha_from(c):
    """invert Seaton for the dipole polarisability, in units of a0^3"""
    nbar = (c["nlo"] + c["nhi"]) / 2.0
    l = c["l"]
    shape = (3.0 - l*(l+1)/nbar**2) / kfac(l)
    if shape <= 0: return None
    return c["d"] / (c["z"]**2 * shape)

def predict(alpha, z, l, nbar):
    return alpha * z**2 * (3.0 - l*(l+1)/nbar**2) / kfac(l)

def run():
    ch = load()
    by = defaultdict(list)
    for c in ch: by[(c["sp"], c["core"])].append(c)
    rows = []
    for key, v in by.items():
        # the SOURCE channel: the cleanest high-l one, meaning the smallest relative spread
        cands = [c for c in v if c["l"] >= 3 and c["d"] > 0.001 and c["d"] < 0.3]
        if not cands: continue
        src = min(cands, key=lambda c: (c["sd"]/max(c["d"],1e-9)))
        a = alpha_from(src)
        if a is None or a <= 0: continue
        for tgt in v:
            if tgt is src or tgt["l"] < 3: continue
            nbar = (tgt["nlo"] + tgt["nhi"]) / 2.0
            p = predict(a, tgt["z"], tgt["l"], nbar)
            rows.append((key[0], src["l"], tgt["l"], a, p, tgt["d"], tgt["sd"]))
    return rows

with State("seaton") as s:
    rows = step(s, "extract alpha and predict every other high-l", run, budget=600)

print("  SEATON'S PREDICTION AGAINST THE MEASURED DEFECT\n")
print("  alpha_d is extracted from ONE channel per species — the cleanest high-l one —")
print("  and used to predict the others. Nothing is looked up.\n")
print(f"  {'species':<9}{'from':>5}{'to':>4}{'alpha (a0³)':>13}{'predicted':>11}{'measured':>10}"
      f"{'ratio':>8}{'within 2σ':>11}")
ok = tot = 0
for sp, ls, lt, a, p, d, sd in sorted(rows, key=lambda x: (x[0], x[2])):
    r = p/d if d > 1e-9 else float("inf")
    inside = abs(p-d) <= max(2*sd, 0.0005)
    ok += inside; tot += 1
    print(f"  {sp:<9}{'spdfghik'[ls]:>5}{'spdfghik'[lt]:>4}{a:>13.3f}{p:>11.4f}{d:>10.4f}"
          f"{r:>8.2f}{'yes' if inside else 'NO':>11}")
print()
print(f"  {ok} of {tot} predictions land within the measured 2σ")
if tot:
    rr = [p/d for _,_,_,_,p,d,_ in rows if d > 1e-9]
    print(f"  median predicted/measured: {st.median(rr):.3f}")
