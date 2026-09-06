import math, statistics as st
from collections import Counter, deque, defaultdict
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
print("  THE TWO DEFECTS ARE INTERIOR AND EXTERIOR — measuring both properly\n")
print("  E(X)   counts what the index ADMITS.       Bounded by the sample.")
print("  E_W(X) counts what the steps REACH.        Unbounded by it.")
print("  Their intersection is where both operators speak.\n")
print(f"  {'tau':>6}{'E':>7}{'E_W':>7}{'interior':>10}{'exterior':>10}{'BOTH':>7}{'  both/E':>9}")
for tau in (1.5,1.8,2.5,3.0,4.0,6.0,10.0,20.0):
    W=W2(tau); Ws=set(W)
    both=len((Ws&R)-Xs); ext=len(Ws-R); intr=len(R-Ws)
    print(f"  {tau:>6.1f}{len(R)-len(Xs):>7}{len(Ws)-len(Xs):>7}{intr:>10}{ext:>10}"
          f"{both:>7}{100*both/max(len(R)-len(Xs),1):>8.1f}%")
print()
W=W2(3.0); Ws=set(W)
print("  THE THREE POPULATIONS AT tau = 3.0\n")
inter=sorted(R-Ws); ext=sorted(Ws-R); both=sorted((Ws&R)-Xs)
print(f"      {'':<34}{'cells':>7}{'med ℓ':>8}{'med c':>8}{'med Nₑ':>8}")
for lab,pop in (("interior — ℛ admits, W cannot reach",inter),
                ("both — placed and valued",both),
                ("exterior — W reaches, ℛ refuses",ext)):
    if not pop: continue
    print(f"      {lab:<34}{len(pop):>7}{st.median([x[2] for x in pop]):>8.1f}"
          f"{st.median([x[1] for x in pop]):>8.1f}"
          f"{st.median([x[0]-x[1]+1 for x in pop]):>8.1f}")
print()
print("  AND WHAT EACH POPULATION IS FOR\n")
print("      INTERIOR   1,503 cells the order places and no step values.")
print("                 These are CAPTURES: the index says they belong and")
print("                 nothing in the compendium can put a number on them.")
print()
print("      BOTH         145 cells placed AND valued. The working part —")
print("                 where the ordinal and metric halves agree.")
print()
print("      EXTERIOR     218 cells the steps reach past the sample edge.")
print("                 These are PREDICTIONS the order cannot check, and")
print("                 every one fails 'charge given Z'.")
print()
ex=sorted(Ws-R,key=lambda k:-abs(W[k][0]))[:10]
print("  the ten largest exterior predictions:\n")
EL={1:"H",19:"K",20:"Ca",21:"Sc",22:"Ti",26:"Fe",30:"Zn",31:"Ga",32:"Ge",38:"Sr",
    48:"Cd",56:"Ba",80:"Hg",83:"Bi",84:"Po",85:"At",13:"Al",14:"Si",16:"S",18:"Ar"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
print(f"      {'species':<10}{'ℓ':>3}{'2S+1':>6}{'δ':>10}{'error factor':>14}")
for k in ex:
    v,e=W[k]
    print(f"      {EL.get(k[0],'Z'+str(k[0]))+' '+RO.get(k[1],str(k[1])):<10}"
          f"{'spdfg'[k[2]]:>3}{k[3]:>6}{v:>10.4f}{e:>14.2f}")