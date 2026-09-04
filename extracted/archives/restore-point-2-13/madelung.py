#!/usr/bin/env python3
"""madelung.py -- do measured quantum defects organise on n+l?

Register 1249. Loewdin 1969 named the derivation of the n+l rule a major unsolved
problem. The closest thing to a derivation is Demkov & Ostrovsky, n+l filling rule
in the periodic system and focusing potentials, Sov. Phys. JETP 35 (1972) 66-69:
a potential class whose levels depend only on n+l.

The quantum defect is exactly the quantity measuring how a real atomic potential
departs from Coulomb. So the question has a MEASURABLE form:

    does the effective quantum number n* = n - delta(l) order by n+l ?

Concretely, the Madelung rule says a subshell with a smaller n+l fills first, and
"fills first" means "lies lower in energy". For a Rydberg channel,

    E = - Zc^2 R / (n - delta)^2

so lower energy means smaller n*. The rule therefore predicts

    (n+l) < (n'+l')  =>  n* < n*'          [MADELUNG ORDER]

and, for ties in n+l, smaller n first.

THREE TESTS, on the compendium's own measured channels:

    1  ORDER    over all pairs of channels in one spectrum, how often does the
                pair with the smaller n+l have the smaller n*?
    2  COLLAPSE the same test restricted to pairs that straddle a Janet block
                boundary, where the rule is doing its real work
    3  DEFECT   is delta itself a function of n+l, or of n and l separately?
                If it were a function of n+l alone, the focusing-potential
                picture would hold exactly and the rule would follow.
"""
import csv, math, re, json
from collections import defaultdict
import statistics as st

def load_measured():
    """every measured (Z, charge, l, delta) with its lowest n from the raw fits"""
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    config, mults, H = ns["config"], ns["mults"], dict(ns["measured"]())
    H.update({(38,2,0,2):2.7113,(38,2,1,2):2.3501,(38,2,2,2):1.4577,(38,2,3,2):0.0618,
              (38,2,4,2):0.0098,(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,
              (22,4,3,2):0.0774,(20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,
              (19,3,0,2):1.6589,(19,3,1,2):1.2110})
    return config, H

def n0(config, ne, l):
    """the first Pauli-allowed principal number for this l in this species"""
    v = [n for n, ll, o in config(ne) if ll == l and o > 0]
    return (max(v) + 1) if v else l + 1

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z + 1; _z += 2*(2*_l+1)

config, H = load_measured()

# ---------------------------------------------------------------- build channels
CH = []
for (Z, c, l, S), d in H.items():
    ne = Z - c + 1
    n = n0(config, ne - 1, l)          # the first available n for this l
    CH.append(dict(Z=Z, c=c, l=l, S=S, d=d, n=n, nl=n + l, nstar=n - d, ne=ne))

print(f"  {len(CH)} measured channels\n")

# ---------------------------------------------------------------- 1 ORDER
print("  1 · DOES n* ORDER BY n+ℓ, WITHIN ONE SPECIES?\n")
bysp = defaultdict(list)
for x in CH: bysp[(x["Z"], x["c"])].append(x)
agree = tie = disagree = 0
for k, v in bysp.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            a, b = v[i], v[j]
            if a["nl"] == b["nl"]: tie += 1; continue
            lo, hi = (a, b) if a["nl"] < b["nl"] else (b, a)
            if lo["nstar"] < hi["nstar"]: agree += 1
            else: disagree += 1
tot = agree + disagree
print(f"      pairs with different n+ℓ : {tot}")
print(f"      Madelung order holds     : {agree}  ({100*agree/max(tot,1):.1f}%)")
print(f"      Madelung order fails     : {disagree}")
print(f"      ties in n+ℓ              : {tie}")
print()

# ---------------------------------------------------------------- control
print("  the control — does the RAW n order by n+ℓ, without the defect?\n")
a2 = d2 = 0
for k, v in bysp.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            a, b = v[i], v[j]
            if a["nl"] == b["nl"]: continue
            lo, hi = (a, b) if a["nl"] < b["nl"] else (b, a)
            if lo["n"] < hi["n"]: a2 += 1
            elif lo["n"] > hi["n"]: d2 += 1
print(f"      raw n agrees {a2}, fails {d2}  ({100*a2/max(a2+d2,1):.1f}%)")
print(f"      → the DEFECT contributes {100*agree/max(tot,1) - 100*a2/max(a2+d2,1):+.1f} points")
print()

# ---------------------------------------------------------------- 3 DEFECT
print("  3 · IS δ A FUNCTION OF n+ℓ ALONE?\n")
print("      If it were, the focusing-potential picture (Demkov & Ostrovsky 1972)")
print("      would hold exactly and the rule would follow. Test: within one")
print("      species, do channels sharing n+ℓ share δ?\n")
groups = []
for k, v in bysp.items():
    g = defaultdict(list)
    for x in v: g[x["nl"]].append(x["d"])
    for nl, ds in g.items():
        if len(ds) >= 2: groups.append((k, nl, ds))
if groups:
    spread = [max(ds) - min(ds) for _, _, ds in groups]
    allsp = [max(x["d"] for x in v) - min(x["d"] for x in v)
             for v in bysp.values() if len(v) >= 2]
    print(f"      {len(groups)} (species, n+ℓ) groups with 2+ channels")
    print(f"      median spread of δ WITHIN an n+ℓ group : {st.median(spread):.4f}")
    print(f"      median spread of δ across a whole species: {st.median(allsp):.4f}")
    r = st.median(spread) / max(st.median(allsp), 1e-9)
    print(f"      ratio {r:.3f}   "
          f"{'δ is NOT a function of n+ℓ alone' if r > 0.5 else 'δ largely tracks n+ℓ'}")
else:
    print("      no species has two channels sharing n+ℓ — the test cannot run")
print()

# ---------------------------------------------------------------- 2 COLLAPSE
print("  2 · THE PAIRS THAT STRADDLE A JANET BOUNDARY\n")
print("      the rule's real content is that (n−1)d fills before np, and 4f before 5d.")
print("      Those are exactly the pairs where n+ℓ ties or inverts the raw n.\n")
hard = []
for k, v in bysp.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            a, b = v[i], v[j]
            if a["nl"] == b["nl"]: continue
            lo, hi = (a, b) if a["nl"] < b["nl"] else (b, a)
            if lo["n"] > hi["n"]:                 # n+ℓ and raw n disagree
                hard.append((k, lo, hi, lo["nstar"] < hi["nstar"]))
if hard:
    ok = sum(1 for *_, g in hard if g)
    print(f"      {len(hard)} pairs where n+ℓ and raw n give OPPOSITE orders")
    print(f"      n* follows n+ℓ : {ok}  ({100*ok/len(hard):.1f}%)")
    print(f"      n* follows raw n: {len(hard)-ok}")
    print()
    print(f"      {'species':<10}{'lower n+ℓ':>16}{'higher n+ℓ':>16}{'n* order':>12}")
    EL = {3:"Li",11:"Na",19:"K",20:"Ca",21:"Sc",22:"Ti",30:"Zn",37:"Rb",38:"Sr",
          48:"Cd",55:"Cs",56:"Ba",80:"Hg",83:"Bi",13:"Al",14:"Si",12:"Mg",4:"Be"}
    RO = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI"}
    for k, lo, hi, g in hard[:14]:
        sp = f"{EL.get(k[0],'Z'+str(k[0]))} {RO.get(k[1],k[1])}"
        a = f"{lo['n']}{'spdfghi'[lo['l']]} (n+ℓ={lo['nl']})"
        b = f"{hi['n']}{'spdfghi'[hi['l']]} (n+ℓ={hi['nl']})"
        print(f"      {sp:<10}{a:>16}{b:>16}{'MADELUNG' if g else 'raw n':>12}")
else:
    print("      no such pairs in the measured set")

# ---------------------------------------------------------------- the failures
print()
print("  4 · THE EIGHTEEN FAILURES\n")
EL = {1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",
      12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",
      21:"Sc",22:"Ti",26:"Fe",30:"Zn",31:"Ga",32:"Ge",37:"Rb",38:"Sr",48:"Cd",
      55:"Cs",56:"Ba",80:"Hg",83:"Bi"}
RO = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
fails = []
for k, v in bysp.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            a, b = v[i], v[j]
            if a["nl"] == b["nl"]: continue
            lo, hi = (a, b) if a["nl"] < b["nl"] else (b, a)
            if lo["nstar"] >= hi["nstar"]: fails.append((k, lo, hi))
print(f"      {'species':<10}{'lower n+ℓ':>13}{'n*':>8}{'higher n+ℓ':>13}{'n*':>8}{'gap':>8}")
for k, lo, hi in sorted(fails, key=lambda x: -(x[1]["nstar"]-x[2]["nstar"])):
    sp = f"{EL.get(k[0],'Z'+str(k[0]))} {RO.get(k[1],k[1])}"
    a = f"{lo['n']}{'spdfghi'[lo['l']]}({lo['nl']})"
    b = f"{hi['n']}{'spdfghi'[hi['l']]}({hi['nl']})"
    print(f"      {sp:<10}{a:>13}{lo['nstar']:>8.3f}{b:>13}{hi['nstar']:>8.3f}"
          f"{lo['nstar']-hi['nstar']:>8.3f}")
print()
from collections import Counter
print("      by species : " + "  ".join(
    f"{EL.get(k[0],k[0])} {RO.get(k[1],k[1])}:{v}"
    for k, v in Counter(k for k,_,_ in fails).most_common()))
print("      by ℓ-pair  : " + "  ".join(
    f"{'spdfghi'[a]}–{'spdfghi'[b]}:{v}" for (a,b), v in
    Counter((lo['l'],hi['l']) for _,lo,hi in fails).most_common()))
print()
gaps = [lo["nstar"]-hi["nstar"] for _,lo,hi in fails]
print(f"      median inversion gap: {st.median(gaps):.4f}")
print(f"      how many by less than 0.05: {sum(1 for g in gaps if g < 0.05)} of {len(gaps)}")
