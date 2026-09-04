#!/usr/bin/env python3
"""steps.py -- each relation as a STEP with a measured accuracy.

Register 1102. Placement is 99.3% and valuation 22.8%. The gap closes if each relation
is converted from a BOUND — "delta falls" — into a STEP: a multiplier with a measured
accuracy, so a value can be walked from a measured cell to an unmeasured one and the
error accumulated honestly.

Three relations move between cells, and each is measured here on pairs where BOTH
cells are known, so the step's accuracy is observed rather than assumed:

    l    -> l+1     within one species and core
    iso            along an isoelectronic sequence, charge c -> c+1
    elem           along one element's charge states, c -> c+1

For each, the step is expressed as a RATIO delta(target)/delta(source), and what is
measured is the distribution of that ratio. A step is usable if its ratio is tight;
a step whose ratio scatters by a factor of two carries almost no information and
walking two of them carries less.

The l step has a PREDICTED ratio from Seaton — kfac(l)/kfac(l+1) — so for that one the
question is whether the observed ratio matches the prediction, which register 1076
answered at median 1.12. For iso and elem there is no formula and the ratio must be
measured outright.
"""
import re, math, statistics as st
from collections import defaultdict
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}

def kfac(l): return l*(l+1)*(2*l-1)*(2*l+1)*(2*l+3)

def load():
    """the mean defect at each (Z, charge, l), and separately at (species, core, l)"""
    byc = defaultdict(list); bysp = defaultdict(list)
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1])
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        try:
            Z = ZNUM[el.group(1)]; c = int(r[9]); l = LM[m.group(1)]; d = float(r[7])
        except Exception: continue
        byc[(Z,c,l)].append(d)
        bysp[(r[0].rstrip(" *"), r[1][:m.start()].strip(), l)].append(d)
    return ({k: st.mean(v) for k,v in byc.items()},
            {k: st.mean(v) for k,v in bysp.items()})

def ratios(byc, bysp):
    out = defaultdict(list)
    # l -> l+1, within one species and core
    for (sp,core,l), d in bysp.items():
        t = bysp.get((sp,core,l+1))
        if t is None or d <= 1e-4 or t <= 1e-4: continue
        out[("l", l)].append(d/t)
    # iso: (Z,c) -> (Z+1,c+1), same electron count
    for (Z,c,l), d in byc.items():
        t = byc.get((Z+1,c+1,l))
        if t is None or d <= 1e-4 or t <= 1e-4: continue
        out[("iso", l)].append(d/t)
    # elem: (Z,c) -> (Z,c+1), same element
    for (Z,c,l), d in byc.items():
        t = byc.get((Z,c+1,l))
        if t is None or d <= 1e-4 or t <= 1e-4: continue
        out[("elem", l)].append(d/t)
    return out

with State("steps") as s:
    byc, bysp = step(s, "read the measured defects", load, budget=120)
    R = step(s, "measure every one-step ratio", lambda: ratios(byc, bysp), budget=300)

print("  EACH RELATION AS A STEP — the ratio delta(source)/delta(target)\n")
print("  A step is usable when its ratio is tight. The spread is what accumulates")
print("  when two steps are walked, so it is reported as a geometric factor.\n")
print(f"  {'relation':<10}{'l':>3}{'pairs':>7}{'median':>9}{'geo. sd':>9}"
      f"{'Seaton':>9}{'usable?':>9}")
for kind in ("l","iso","elem"):
    for l in range(8):
        v = R.get((kind,l))
        if not v or len(v) < 3: continue
        lg = [math.log(x) for x in v if x > 0]
        med = math.exp(st.median(lg)); sd = math.exp(st.pstdev(lg)) if len(lg) > 1 else float("inf")
        pred = kfac(l+1)/kfac(l) if (kind == "l" and l >= 3) else None
        ok = "yes" if sd < 1.5 else ("weak" if sd < 2.5 else "no")
        print(f"  {kind:<10}{'spdfghik'[l]:>3}{len(v):>7}{med:>9.2f}{sd:>9.2f}"
              f"{(f'{pred:.2f}' if pred else '—'):>9}{ok:>9}")
print()
allsd = {}
for kind in ("l","iso","elem"):
    v = [x for l in range(8) for x in R.get((kind,l),[]) if x > 0]
    if len(v) < 3: continue
    lg = [math.log(x) for x in v]
    allsd[kind] = (math.exp(st.median(lg)), math.exp(st.pstdev(lg)), len(v))
print(f"  {'relation':<10}{'all pairs':>11}{'median ratio':>14}{'geometric sd':>14}"
      f"{'2 steps':>10}{'3 steps':>10}")
for kind,(m,sd,n) in allsd.items():
    print(f"  {kind:<10}{n:>11}{m:>14.2f}{sd:>14.2f}{sd**1.41:>10.2f}{sd**1.73:>10.2f}")
print()
print("  '2 steps' and '3 steps' are the accumulated factor if the errors are")
print("  independent — sd^sqrt(k). A step whose factor exceeds about 2 after two")
print("  walks cannot value a cell; it can only bound it.")
