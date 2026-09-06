import re, sys
sys.path.insert(0,"/home/claude/work")
from merged_triples import subshells
import importlib.util as iu
sp=iu.spec_from_file_location("_g","ground.py"); g=iu.module_from_spec(sp); sp.loader.exec_module(g)
cells=set()
for z,(sym,cfg,term) in g.GROUND.items():
    for n,l,k in subshells(cfg): cells.add((z,1,z,n,l,k))
N=["Z","c","Ne","n","l","k"]; d=6
def env(X,i,j):
    m={}
    for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
    b,o=-10**9,{}
    for t in sorted(m): b=max(b,m[t]); o[t]=b
    return o
print("  IS EACH COORDINATE AN AXIS?  an axis is determined when its values")
print("  form a MONOTONE CHAIN against another coordinate — A.rule, T.tight.\n")
print("  envelope STEPS phi(x_i | x_j <= v).  0 steps = flat = no constraint.\n")
print(f"  {'':>4}" + "".join(f"{n:>6}" for n in N) + "   <- given j")
tot={}
for i in range(d):
    row=[]
    for j in range(d):
        if i==j: row.append("  ."); continue
        o=env(cells,i,j)
        vals=[o[t] for t in sorted(o)]
        steps=sum(1 for a,b in zip(vals,vals[1:]) if b>a)
        row.append(f"{steps:>3}")
        tot[i]=tot.get(i,0)+steps
    print(f"  {N[i]:>4}" + "".join(f"{c:>6}" for c in row))
print("\n  total envelope steps per coordinate (its claim to be an axis):")
for i in sorted(tot,key=lambda x:-tot[x]):
    verdict = "AXIS" if tot[i]>0 else "NOT AN AXIS — flat everywhere"
    print(f"      {N[i]:<4} {tot[i]:>4}   {verdict}")
print("\n  and the reverse: which coordinates does each BOUND?")
for i in range(d):
    b=[N[j] for j in range(d) if i!=j and
       sum(1 for a,c in zip([env(cells,j,i)[t] for t in sorted(env(cells,j,i))],
                            [env(cells,j,i)[t] for t in sorted(env(cells,j,i))][1:]) if c>a)>0]
    print(f"      {N[i]:<4} bounds: {', '.join(b) if b else 'nothing'}")