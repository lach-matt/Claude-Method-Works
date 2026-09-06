import math, statistics as st
from itertools import product
from collections import defaultdict, Counter, deque
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,op_S,op_R,region,parents=g["load"],g["op_S"],g["op_R"],g["region"],g["parents"]
config,mults,H=load()
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
Xs=set(Hin); R=op_R(Xs)
def admissible(Z,c,l,S):
    """every constraint the index states — register 1178 and 1191"""
    if c>Z or c<1 or l<0 or Z<1: return False
    ne=Z-c+1
    if ne<1: return False
    if S not in mults(ne): return False
    cfg=config(ne-1)
    v=[n for n,ll,occ in cfg if ll==l and occ>0]
    n0=(max(v)+1) if v else l+1
    if l>=n0: return False
    return region(Z,c,l,config)
def op_W2(H,S,tau):
    """the walk, respecting the index's own constraints at every step"""
    val={k:(v,1.0) for k,v in H.items()}
    q=deque(sorted(H))
    while q:
        k=q.popleft(); v0,e0=val[k]
        for name,(f,sc,n,dv) in S.items():
            for sgn in (1,-1):
                t=(k[0]+sgn*dv[0],k[1]+sgn*dv[1],k[2]+sgn*dv[2],
                   k[3]+2*sgn if dv[3] else k[3])
                if not admissible(*t): continue
                e=e0*sc
                if e>tau: continue
                nv=v0*(f if sgn>0 else 1/f)
                if t not in val or e<val[t][1]:
                    val[t]=(nv,e); q.append(t)
    return val
print("  THE WALK, CONSTRAINED — every step checked against the index's own rules\n")
print(f"      |X| = {len(Xs)}   |ℛ(X)| = {len(R)}   E = {len(R)-len(Xs)}\n")
print(f"  {'tau':>6}{'|W|':>7}{'E_W':>7}{'|ℛ(W)|':>9}{'E(W)':>8}{'closed?':>9}"
      f"{'placed+valued':>15}{'refused':>9}")
S=op_S(Hin,config)
for tau in (1.5,1.8,2.5,3.0,4.0,6.0,10.0):
    W=op_W2(Hin,S,tau); Ws=set(W); RW=op_R(Ws)
    print(f"  {tau:>6.1f}{len(Ws):>7}{len(Ws)-len(Xs):>7}{len(RW):>9}{len(RW)-len(Ws):>8}"
          f"{('YES' if len(RW)==len(Ws) else 'no'):>9}{len((Ws&R)-Xs):>15}{len(Ws-R):>9}")
print()
W=op_W2(Hin,S,3.0); Ws=set(W)
new=sorted(Ws-Xs)
print(f"  AT tau = 3.0 — {len(new)} cells valued that were not held\n")
byl=Counter(x[2] for x in new); byc=Counter(x[1] for x in new)
print("      by ℓ     : " + "  ".join(f"{'spdfghik'[l]}:{byl[l]}" for l in sorted(byl)))
print("      by charge: " + "  ".join(f"{c}:{byc[c]}" for c in sorted(byc)))
print(f"\n      ℛ places {len((Ws&R)-Xs)} of them and refuses {len(Ws-R)}")
print(f"      and ℛ(W) = {len(op_R(Ws))} against |W| = {len(Ws)}")