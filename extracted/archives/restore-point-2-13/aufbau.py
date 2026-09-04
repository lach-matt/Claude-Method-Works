#!/usr/bin/env python3
"""aufbau.py -- the index built from the ground state, not from what was captured.

Register 1139. Every index in the book until now has taken its alphabets from the data:
the Z values are the elements collected, the charge values are the stages captured. The
envelope phi(charge | Z) is then a cumulative maximum over that sample, and register 1138
found the consequence — N VI, O VI, F VI and four more are refused because sulphur is the
only element held at charge 6, though every one satisfies charge < Z.

But the cell set does not need the sample. From one atom's ground state:

    Z                          the atomic number
    aufbau(Ne)                 the ground configuration of every charge state
    S_core = unpaired/2        Hund's first rule on the outermost open subshell
    2S+1 in {2S_core+-1+1}     the channel's allowed multiplicities
    l free                     the Rydberg electron's orbital

and the cell set follows with no spectrum at all. Register 1139 verified the multiplicity
step of that chain on every electron count the compendium holds: 24 of 24, exact
containment, and 17 of 24 matching precisely.

THIS SCRIPT builds the index that way and asks two things. First, what E becomes when the
alphabet is physical rather than sampled. Second — the harder question — whether the
construction supplies VALUES as well as cells, or whether it places and stops.
"""
import re, math, statistics as st
from itertools import product
from collections import defaultdict
from zeno import State, step

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,
      "Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,
      "Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹","0123456789")

def config(ne):
    left, out = ne, []
    for n, l in ORDER:
        if left <= 0: break
        cap = 2*(2*l+1); occ = min(left, cap); out.append((n,l,occ)); left -= occ
    return out

def core_spin(ne_core):
    """Hund's first rule on the outermost open subshell of the CORE"""
    cfg = config(ne_core)
    if not cfg: return 0.0
    n, l, occ = cfg[-1]
    cap, half = 2*(2*l+1), 2*l+1
    return (occ if occ <= half else cap-occ) / 2.0

def mults(ne):
    """the multiplicities a channel of Ne electrons may carry"""
    sc = core_spin(ne-1)
    return {int(2*(sc+d)+1) for d in (0.5,-0.5) if sc+d >= 0}

def aufbau_index(Zmax=83, lmax=7):
    """every cell the physics admits, from the ground state alone"""
    cells = set()
    for Z in range(1, Zmax+1):
        for c in range(1, Z+1):              # charge < Z, plus the bare-core stage
            ne = Z - c + 1
            if ne < 1: continue
            for S in mults(ne):
                for l in range(lmax+1):
                    cells.add((Z, c, l, S))
    return cells

def measured():
    H = defaultdict(list)
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZN: continue
        mu = re.search(r"(\d)[SPDFG]", r[1][m.end():].translate(SUP))
        if not mu: continue
        try: H[(ZN[el.group(1)], int(r[9]), LM[m.group(1)], int(mu.group(1)))].append(float(r[7]))
        except Exception: pass
    return {k: st.mean(v) for k, v in H.items()}

def RR(X, d=4):
    X = set(X)
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def run():
    H = measured()
    # the SAMPLED index, as the compendium has built it
    A = [sorted({x[i] for x in H}) for i in range(4)]
    SAMP = {x for x in product(*A) if x[1] < x[0]}
    # the AUFBAU index, restricted to the same Z range so the comparison is fair
    Zs = sorted({k[0] for k in H})
    AUF = {x for x in aufbau_index(max(Zs)) if x[0] in Zs}
    return H, SAMP, AUF

with State("aufbau") as s:
    H, SAMP, AUF = step(s, "build both indexes", run, budget=600)

print("  THE INDEX FROM THE GROUND STATE AGAINST THE INDEX FROM THE SAMPLE\n")
print(f"  {'':<34}{'cells':>10}{'holds':>9}{'admits & does not hold':>26}")
for lab, G in (("sampled  (alphabets from data)", SAMP), ("aufbau   (alphabets from physics)", AUF)):
    held = len(set(H) & G)
    print(f"  {lab:<34}{len(G):>10,}{held:>9}{len(G)-held:>26,}")
print()
mis = set(H) - AUF
print(f"  measured cells the aufbau index does NOT admit: {len(mis)}")
if mis:
    INV = {v:k for k,v in ZN.items()}
    for k in sorted(mis)[:8]:
        Z,c,l,S = k
        print(f"      {INV.get(Z,Z)} {c}  n{'spdfghik'[l]}  2S+1={S}   "
              f"Nₑ={Z-c+1}, allowed {sorted(mults(Z-c+1))}")
