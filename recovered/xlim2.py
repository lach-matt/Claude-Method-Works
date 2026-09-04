import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
HYD=sorted(ORDER,key=lambda t:(t[0],t[1])); L="spdfg"
def build(ne,o):
    left,out=ne,[]
    for n,l in o:
        if left<=0: break
        cap=2*(2*l+1); k=min(left,cap); out.append((n,l,k)); left-=k
    return out
def cfg(ne,c): return build(ne, ORDER if c<=2 else HYD)
def cp_(ne,l,c): return sum(1 for n,ll,o in cfg(ne,c) if ll==l and o>0)
ns={}
exec(open("aufbau.py",encoding="utf-8").read().split("with State(")[0]
     .replace("from zeno import State, step",""),ns)
H=dict(ns["measured"]())
H.update({(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,(20,4,0,2):1.3280,
 (20,4,1,2):1.0703,(19,3,0,2):1.6589,(19,3,1,2):1.2110,
 (37,1,0,2):3.1357,(37,1,1,2):2.6566,(37,1,2,2):1.3307,
 (38,2,0,2):2.7115,(38,2,1,2):2.3636,(38,2,2,2):1.4592,
 (39,3,0,2):2.4462,(39,3,1,2):2.1216,(39,3,2,2):1.3965,
 (81,2,1,2):3.7167,(82,3,1,2):3.5402,(83,4,1,2):3.3684})
def par(cf):
    if not cf: return 1
    n,l,o=cf[-1]; cap=2*(2*l+1)
    return 1 if o in (0,cap,1,cap-1) else {0:1,1:3,2:16,3:119}.get(l,8)
seq=defaultdict(dict); pm={}
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5 or d<=0.02: continue
    if par(cfg(ne-1,c))>1: continue
    seq[(ne,l)][c]=d; pm[(ne,l)]=cp_(ne-1,l,c)
print("  x AT EVERY ELECTRON COUNT — penetrating channels, p ≥ 1\n")
print(f"      {'Nₑ':>4}{'ℓ':>3}{'p':>3}{'chg':>5}{'x':>9}{'r²':>8}")
PTS=[]
for k in sorted(seq):
    d=seq[k]
    if len(d)<3 or pm[k]==0: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.80: continue
    PTS.append((k[0],k[1],pm[k],-rr.slope))
    print(f"      {k[0]:>4}{L[k[1]]:>3}{pm[k]:>3}{len(cs):>5}{-rr.slope:>9.4f}{rr.rvalue**2:>8.4f}")
by=defaultdict(list)
for ne,l,p,x in PTS: by[ne].append(x)
S=[(ne,st.median(v)) for ne,v in sorted(by.items())]
print(f"\n  THE SEQUENCE — one value per Nₑ\n")
print(f"      {'Nₑ':>4}{'x':>9}{'1/x':>9}{'x·√Nₑ':>10}")
for ne,x in S: print(f"      {ne:>4}{x:>9.4f}{1/x:>9.3f}{x*math.sqrt(ne):>10.3f}")
ne=np.array([a for a,_ in S],float); x=np.array([b for _,b in S])
print()
print("  IS 1/x LINEAR?\n")
for nm,X in (("Nₑ",ne),("√Nₑ",np.sqrt(ne)),("Nₑ^(1/3)",ne**(1/3)),("ln Nₑ",np.log(ne))):
    r=SS.linregress(X,1/x)
    print(f"      1/x vs {nm:<10}{r.intercept:>8.3f} {r.slope:+.4f}   r² {r.rvalue**2:.4f}")
r=SS.linregress(np.sqrt(ne),1/x)
print(f"\n      1/x = {r.intercept:.3f} {r.slope:+.4f}·√Nₑ\n")
for n_ in (1,2,3,12,20,40,80,118):
    print(f"          Nₑ = {n_:>3} :  x = {1/(r.intercept+r.slope*math.sqrt(n_)):>7.3f}")