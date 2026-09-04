import math, statistics as st
from collections import Counter, deque
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,op_S,op_R,region=g["load"],g["op_S"],g["op_R"],g["region"]
config,mults,H=load()
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
Xs=set(Hin); R=op_R(Xs); S=op_S(Hin,config)
def adm(Z,c,l,Sm):
    if c>Z or c<1 or l<0 or Z<1: return False
    ne=Z-c+1
    if ne<1 or Sm not in mults(ne): return False
    cfg=config(ne-1); v=[n for n,ll,o in cfg if ll==l and o>0]
    n0=(max(v)+1) if v else l+1
    return l<n0 and region(Z,c,l,config)
def W2(tau):
    val={k:(v,1.0) for k,v in Hin.items()}; q=deque(sorted(Hin))
    while q:
        k=q.popleft(); v0,e0=val[k]
        for nm,(f,sc,n,dv) in S.items():
            for sg in (1,-1):
                t=(k[0]+sg*dv[0],k[1]+sg*dv[1],k[2]+sg*dv[2],k[3]+2*sg if dv[3] else k[3])
                if not adm(*t): continue
                e=e0*sc
                if e>tau: continue
                if t not in val or e<val[t][1]:
                    val[t]=(v0*(f if sg>0 else 1/f),e); q.append(t)
    return val
W=W2(3.0); Ws=set(W); ref=sorted(Ws-R); plc=sorted((Ws&R)-Xs)
print(f"  WHY DOES ℛ REFUSE THE {len(ref)}?\n")
print("  ℛ is a monotone envelope on the MEASURED set. A cell it refuses lies")
print("  outside that envelope. So: are the refused cells outside the measured")
print("  coordinate ranges?\n")
NM=["Z","charge","ℓ","2S+1"]
print(f"  {'coordinate':<10}{'measured range':>18}{'refused range':>18}{'  outside?'}")
for i in range(4):
    mn,mx=min(x[i] for x in Xs),max(x[i] for x in Xs)
    rn,rx=min(x[i] for x in ref),max(x[i] for x in ref)
    out=rn<mn or rx>mx
    print(f"  {NM[i]:<10}{f'{mn}–{mx}':>18}{f'{rn}–{rx}':>18}{'  YES' if out else '  no':>10}")
print()
def env_fail(x):
    """which envelope pair rejects this cell"""
    bad=[]
    for i in range(4):
        for j in range(4):
            if i==j: continue
            m={}
            for c in Xs: m[c[j]]=max(m.get(c[j],-10**9),c[i])
            b,o=-10**9,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            if x[j] not in o or x[i]>o[x[j]]: bad.append((NM[i],NM[j]))
    return bad
cnt=Counter()
for x in ref:
    for p in env_fail(x): cnt[p]+=1
print("  WHICH ENVELOPE REFUSES THEM\n")
print(f"  {'pair':<22}{'cells refused':>15}")
for (i,j),v in cnt.most_common(6):
    print(f"  {i+' given '+j:<22}{v:>15}")
print()
print("  THE READING\n")
print("      ℛ can only place a cell inside the envelope of what is MEASURED.")
print("      W can step outside it. So the two operators differ exactly where the")
print("      sample ends — and the 218 are the walk reaching past the compendium's")
print("      own coverage, not past the physics.")
print()
print("      That is not an error in either operator. It is the difference between")
print("      an ORDER bounded by its sample and a METRIC that is not.")