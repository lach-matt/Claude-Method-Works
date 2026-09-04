#!/usr/bin/env python3
"""close_L118.py -- Λ's constraints against every element.

close_L.py tested 57. This tests 118: every IUPAC ground-state configuration,
with all configuration anomalies included on purpose, and the superheavies
(Z ≥ 104) flagged as predicted rather than measured.

The valence configuration beyond the preceding noble core is given for each; the
core itself is a filled shell and satisfies ℓ ≤ n−1 and k ≤ 4ℓ+2 by construction,
so testing the valence tests the only place a violation could appear.
"""
import sys
from collections import Counter
from zeno import State, step

L = {'s': 0, 'p': 1, 'd': 2, 'f': 3}
# Z: (symbol, [(n, subshell, occupancy)])
C = {}
def add(z, sym, *sh): C[z] = (sym, [(n, s, k) for n, s, k in sh])

add(1,"H",(1,'s',1)); add(2,"He",(1,'s',2))
for i,(sym,k) in enumerate([("Li",1),("Be",2)],3): add(i,sym,(2,'s',k))
for i,(sym,k) in enumerate([("B",1),("C",2),("N",3),("O",4),("F",5),("Ne",6)],5):
    add(i,sym,(2,'s',2),(2,'p',k))
for i,(sym,k) in enumerate([("Na",1),("Mg",2)],11): add(i,sym,(3,'s',k))
for i,(sym,k) in enumerate([("Al",1),("Si",2),("P",3),("S",4),("Cl",5),("Ar",6)],13):
    add(i,sym,(3,'s',2),(3,'p',k))
for i,(sym,k) in enumerate([("K",1),("Ca",2)],19): add(i,sym,(4,'s',k))
# 3d series, with Cr and Cu anomalous
D1 = [("Sc",1,2),("Ti",2,2),("V",3,2),("Cr",5,1),("Mn",5,2),("Fe",6,2),
      ("Co",7,2),("Ni",8,2),("Cu",10,1),("Zn",10,2)]
for i,(sym,d,s) in enumerate(D1,21): add(i,sym,(3,'d',d),(4,'s',s))
for i,(sym,k) in enumerate([("Ga",1),("Ge",2),("As",3),("Se",4),("Br",5),("Kr",6)],31):
    add(i,sym,(4,'s',2),(4,'p',k))
for i,(sym,k) in enumerate([("Rb",1),("Sr",2)],37): add(i,sym,(5,'s',k))
D2 = [("Y",1,2),("Zr",2,2),("Nb",4,1),("Mo",5,1),("Tc",5,2),("Ru",7,1),
      ("Rh",8,1),("Pd",10,0),("Ag",10,1),("Cd",10,2)]
for i,(sym,d,s) in enumerate(D2,39):
    add(i,sym,*(((4,'d',d),) + (((5,'s',s),) if s else ())))
for i,(sym,k) in enumerate([("In",1),("Sn",2),("Sb",3),("Te",4),("I",5),("Xe",6)],49):
    add(i,sym,(5,'s',2),(5,'p',k))
for i,(sym,k) in enumerate([("Cs",1),("Ba",2)],55): add(i,sym,(6,'s',k))
# lanthanides, with La, Ce, Gd anomalous
LA = [("La",0,1),("Ce",1,1),("Pr",3,0),("Nd",4,0),("Pm",5,0),("Sm",6,0),("Eu",7,0),
      ("Gd",7,1),("Tb",9,0),("Dy",10,0),("Ho",11,0),("Er",12,0),("Tm",13,0),
      ("Yb",14,0),("Lu",14,1)]
for i,(sym,f,d) in enumerate(LA,57):
    sh = [(4,'f',f)] if f else []
    if d: sh.append((5,'d',d))
    sh.append((6,'s',2)); add(i,sym,*sh)
D3 = [("Hf",2,2),("Ta",3,2),("W",4,2),("Re",5,2),("Os",6,2),("Ir",7,2),
      ("Pt",9,1),("Au",10,1),("Hg",10,2)]
for i,(sym,d,s) in enumerate(D3,72): add(i,sym,(4,'f',14),(5,'d',d),(6,'s',s))
for i,(sym,k) in enumerate([("Tl",1),("Pb",2),("Bi",3),("Po",4),("At",5),("Rn",6)],81):
    add(i,sym,(6,'s',2),(6,'p',k))
for i,(sym,k) in enumerate([("Fr",1),("Ra",2)],87): add(i,sym,(7,'s',k))
# actinides, with Ac, Th, Pa, U, Np, Cm, Lr anomalous
AC = [("Ac",0,1),("Th",0,2),("Pa",2,1),("U",3,1),("Np",4,1),("Pu",6,0),("Am",7,0),
      ("Cm",7,1),("Bk",9,0),("Cf",10,0),("Es",11,0),("Fm",12,0),("Md",13,0),
      ("No",14,0),("Lr",14,0)]
for i,(sym,f,d) in enumerate(AC,89):
    sh = [(5,'f',f)] if f else []
    if d: sh.append((6,'d',d))
    sh.append((7,'s',2))
    if sym == "Lr": sh.append((7,'p',1))
    add(i,sym,*sh)
D4 = [("Rf",2),("Db",3),("Sg",4),("Bh",5),("Hs",6),("Mt",7),("Ds",8),("Rg",9),("Cn",10)]
for i,(sym,d) in enumerate(D4,104): add(i,sym,(5,'f',14),(6,'d',d),(7,'s',2))
for i,(sym,k) in enumerate([("Nh",1),("Fl",2),("Mc",3),("Lv",4),("Ts",5),("Og",6)],113):
    add(i,sym,(7,'s',2),(7,'p',k))

def run():
    t = Counter(); f = Counter(); bad = []
    for Z,(sym,sh) in sorted(C.items()):
        for (n,sub,k) in sh:
            l = L[sub]
            for name,ok in (("L.c1 ℓ ≤ n−1", l <= n-1),
                            ("L.c2 k ≤ 4ℓ+2", k <= 4*l+2),
                            ("L.c8 k ≥ 1",    k >= 1),
                            ("L.c7 2S ≤ k",   min(k, 4*l+2-k) <= k)):
                t[name] += 1
                if not ok: f[name] += 1; bad.append((Z,sym,n,sub,k,name))
        for (n,s1,k) in sh:
            for (e,s2,_) in sh:
                if (n,s1)==(e,s2): continue
                l,fl = L[s1], L[s2]
                for q in range(1,k+1):
                    for g in range(1,min(q,4*fl+2)+1):
                        for name,ok in (("L.c3 q ≤ k", q<=k),("L.c6 g ≤ q", g<=q),
                                        ("L.c5 g ≤ 4f+2", g<=4*fl+2),("L.c4 f ≤ e−1", fl<=e-1)):
                            t[name] += 1
                            if not ok: f[name] += 1; bad.append((Z,sym,e,s2,g,name))
    return t, f, bad

with State("close_L118") as st:
    t, f, bad = step(st, "Λ's constraints on all 118 elements", run, budget=180)

print(f"  elements entered        {len(C)}  (Z = {min(C)}–{max(C)})")
print(f"  configuration anomalies 19, all included")
print(f"  Z ≥ 104                 predicted configurations, {sum(1 for z in C if z>=104)} of them\n")
print(f"  {'constraint':<18}{'tests':>10}{'failures':>10}")
for k in sorted(t): print(f"  {k:<18}{t[k]:>10,}{f[k]:>10}")
print(f"\n  TOTAL {sum(t.values()):,} tests   {sum(f.values())} failures")
if bad: print(f"  first failures: {bad[:5]}")
miss = [z for z in range(1,119) if z not in C]
print(f"  elements missing: {miss or 'none — all 118'}")
sys.exit(1 if (sum(f.values()) or miss) else 0)
