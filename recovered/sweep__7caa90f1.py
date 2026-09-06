import math, statistics as st
from collections import defaultdict
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,op_S,op_R,op_W,region=g["load"],g["op_S"],g["op_R"],g["op_W"],g["region"]
config,mults,H=load()
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
S=op_S(Hin,config); R=op_R(set(Hin)); Xs=set(Hin)
print("  THE TOLERANCE SWEEP\n")
print("      steps: " + " | ".join(f"{k} scatter {v[1]:.3f}" for k,v in S.items()))
print(f"      |X| = {len(Hin)}   |R(X)| = {len(R)}   E = {len(R)-len(Hin)}\n")
print(f"  {'tau':>6}{'|W(X)|':>9}{'E_W':>8}{'placed+valued':>16}{'capture':>9}{'extrap':>8}")
for tau in (1.5,1.8,2.0,2.5,3.0,4.0,6.0,10.0,20.0):
    W=op_W(Hin,S,config,tau,region); Ws=set(W)
    print(f"  {tau:>6.1f}{len(W):>9}{len(W)-len(Xs):>8}{len((R&Ws)-Xs):>16}"
          f"{len((R-Ws)-Xs):>9}{len((Ws-R)-Xs):>8}")
for tau in (2.0,4.0):
    W=op_W(Hin,S,config,tau,region); Ws=set(W); new=sorted(Ws-Xs)
    if not new: continue
    byl=defaultdict(int); byc=defaultdict(int)
    for Z,c,l,Sm in new: byl[l]+=1; byc[c]+=1
    print(f"\n  AT tau = {tau}:  {len(new)} cells valued that were not held")
    print("      by l     : " + "  ".join(f"{'spdfghik'[l]}:{byl[l]}" for l in sorted(byl)))
    print("      by charge: " + "  ".join(f"{c}:{byc[c]}" for c in sorted(byc)))
    print(f"      R places {len((R&Ws)-Xs)} of them and refuses {len((Ws-R)-Xs)}")