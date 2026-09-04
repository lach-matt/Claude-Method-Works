#!/usr/bin/env python3
"""channels_principle.py -- the principal structure of an ion channel.

Register 1251. The compendium indexes a channel by (Z, charge, l, 2S+1). That is a
CONVENIENCE, not a definition: it is what the captures happened to record. Going back
to principles, a Rydberg channel is fixed by strictly more than four numbers, and the
question is which of them the fractional defect needs.

WHAT A CHANNEL IS, FROM PRINCIPLES

A Rydberg channel is a one-electron problem in a fixed field. To state it you must
fix, in order:

    1  THE NUCLEUS            Z
    2  THE CORE'S ELECTRON COUNT   Ne_core = Z - c    (so the charge seen at
                                   large r is c = Z - Ne_core)
    3  THE CORE'S CONFIGURATION    which subshells hold those electrons
    4  THE CORE'S TERM             which LS term of that configuration -- the
                                   PARENT. A configuration with an open shell has
                                   several, and each is a different field.
    5  THE OUTER ORBITAL'S l       the centrifugal barrier it must cross
    6  THE COUPLING               how the outer l joins the parent: LS, jK, jj
    7  THE TOTAL J                 which member of the resulting multiplet

Only (1), (2), (5) and part of (4) are in the compendium's four coordinates. What
is MISSING is the parent term itself and the coupling scheme -- and those are
exactly the coordinates the tower adjoins at Lambda_9 through Lambda_13.

THE CLAIM TO TEST

    frac(delta) is not a function of (Z, c, l). It is a function of the PARENT.

If true, the fractional part is not an unexplained residue: it is the coordinate
the four-coordinate index averaged over. If false, the residue is real and sits
somewhere else.

Three tests, all on measured channels:

    A  does frac(delta) vary between channels of ONE species at ONE l, when the
       parent differs?  (the multiplicity 2S+1 is the only parent label held)
    B  is frac(delta) tighter within a parent class than across one?
    C  does the closed-shell subset -- one parent, no ambiguity -- have a
       tighter frac(delta) than the open-shell subset?
"""
import math, statistics as st
from collections import defaultdict, Counter

def load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return ns["config"], ns["mults"], dict(ns["measured"]())

config, mults, H = load()
H.update({(38,2,0,2):2.7113,(38,2,1,2):2.3501,(38,2,2,2):1.4577,(38,2,3,2):0.0618,
          (38,2,4,2):0.0098,(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,
          (22,4,3,2):0.0774,(20,4,0,2):1.3280,(20,4,1,2):1.0703,(19,3,0,2):1.6589,
          (19,3,1,2):1.2110})
L = "spdfghi"

def core_p(ne, l): return sum(1 for n, ll, o in config(ne) if ll == l and o > 0)

def parents(cfg):
    """how many LS parent terms the core's last open subshell carries"""
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    if occ in (0, cap, 1, cap-1): return 1
    return {0:1, 1:3, 2:16, 3:119}.get(l, 8)

def closed(cfg):
    """is the core closed-shell -- exactly one parent, the 1S ground term"""
    return parents(cfg) == 1

CH = []
for (Z, c, l, S), d in H.items():
    ne = Z - c + 1
    cfg = config(ne - 1)
    CH.append(dict(Z=Z, c=c, l=l, S=S, d=d, ne=ne,
                   p=core_p(ne-1, l), par=parents(cfg), cl=closed(cfg),
                   frac=d - math.floor(d)))

print("  THE PRINCIPAL STRUCTURE OF AN ION CHANNEL\n")
print("      1 nucleus Z · 2 core electron count · 3 core configuration")
print("      4 CORE TERM (the parent) · 5 outer ℓ · 6 coupling · 7 total J\n")
print("      the compendium's index holds 1, 2, 5 and a shadow of 4.")
print("      the tower adjoins 4, 6 and 7 as Λ₉…Λ₁₃.\n")
print(f"      {len(CH)} measured channels\n")

# ------------------------------------------------------------------ C
print("  C · CLOSED-SHELL AGAINST OPEN-SHELL CORES\n")
print("      A closed-shell core has ONE parent, so (Z, c, ℓ) determines the field")
print("      completely. An open-shell core has several, and the index cannot say")
print("      which. If frac(δ) needs the parent, the closed set is tighter.\n")
print(f"      {'core':<16}{'channels':>10}{'median frac':>14}{'sd':>9}{'IQR':>16}")
import numpy as np
for lab, sel in (("closed-shell", lambda x: x["cl"]),
                 ("open-shell",   lambda x: not x["cl"])):
    v = [x["frac"] for x in CH if sel(x)]
    if len(v) < 5: continue
    q1, q3 = np.percentile(v, [25, 75])
    print(f"      {lab:<16}{len(v):>10}{st.median(v):>14.3f}{st.pstdev(v):>9.3f}"
          f"{f'{q1:.2f} – {q3:.2f}':>16}")
print()
for l in range(4):
    print(f"      at ℓ = {L[l]}:")
    for lab, sel in (("closed", lambda x: x["cl"]), ("open", lambda x: not x["cl"])):
        v = [x["frac"] for x in CH if x["l"] == l and sel(x)]
        if len(v) < 4: continue
        print(f"          {lab:<8}{len(v):>5} channels   median {st.median(v):.3f}   "
              f"sd {st.pstdev(v):.3f}")
    print()

# ------------------------------------------------------------------ A
print("  A · WITHIN ONE SPECIES AND ONE ℓ, DOES THE MULTIPLICITY MOVE frac(δ)?\n")
g = defaultdict(list)
for x in CH: g[(x["Z"], x["c"], x["l"])].append(x)
pairs = [(k, v) for k, v in g.items() if len({y["S"] for y in v}) > 1]
print(f"      {len(pairs)} (species, ℓ) cells hold more than one multiplicity\n")
if pairs:
    dd = []
    for k, v in pairs:
        byS = defaultdict(list)
        for y in v: byS[y["S"]].append(y["frac"])
        ss = sorted(byS)
        for i in range(len(ss)-1):
            dd.append(abs(st.median(byS[ss[i]]) - st.median(byS[ss[i+1]])))
    print(f"      median |Δ frac(δ)| between multiplicities: {st.median(dd):.4f}")
    allf = [x["frac"] for x in CH]
    print(f"      against the overall spread of frac(δ)     : {st.pstdev(allf):.4f}")
    print(f"      ratio {st.median(dd)/st.pstdev(allf):.3f}")

# ------------------------------------------------------------------ B
print()
print("  B · HOW MUCH OF frac(δ)'s VARIANCE DOES EACH COORDINATE EXPLAIN?\n")
from scipy import stats as SS
allf = np.array([x["frac"] for x in CH])
tot = allf.var()
print(f"      {'grouping':<26}{'groups':>8}{'variance explained':>21}")
for lab, key in (("ℓ alone", lambda x: x["l"]),
                 ("charge alone", lambda x: x["c"]),
                 ("closed vs open core", lambda x: x["cl"]),
                 ("(ℓ, closed)", lambda x: (x["l"], x["cl"])),
                 ("(ℓ, charge)", lambda x: (x["l"], x["c"])),
                 ("core config (Nₑ−1)", lambda x: x["ne"]-1),
                 ("(ℓ, core config)", lambda x: (x["l"], x["ne"]-1))):
    gr = defaultdict(list)
    for x in CH: gr[key(x)].append(x["frac"])
    gr = {k: v for k, v in gr.items() if len(v) >= 2}
    if not gr: continue
    within = sum(np.var(v)*len(v) for v in gr.values()) / sum(len(v) for v in gr.values())
    print(f"      {lab:<26}{len(gr):>8}{100*(1-within/tot):>20.1f}%")
