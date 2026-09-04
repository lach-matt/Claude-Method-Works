import math, statistics as st
import numpy as np
from collections import defaultdict, Counter
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,region=g["load"],g["region"]
config,mults,H=load()
def corb(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def n0f(ne,l):
    v=[n for n,ll,o in config(ne) if ll==l and o>0]
    return (max(v)+1) if v else l+1
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN={}; z=0
for n,l in ORDER: OPEN[(n,l)]=z+1; z+=2*(2*l+1)
a,e0,e1,k,h=np.load("/tmp/anchored.npy")
def eq(Z,c,l,S=2):
    ne=Z-c+1; p=corb(ne-1,l); t=math.log(c+1)/c
    if p>0: return a*(p**max(e0+e1*math.log(max(ne,2)),0.05))*ne**k*t
    thr=OPEN.get((n0f(ne-1,l),l),999)
    return h*min(max((Z-thr+4.0)/8.0,0.0),1.0)*ne**k*t
print("  DOES THE ANCHORED EQUATION CHECK OUT AGAINST THE REST OF THE MATH?\n")
print("  1 · THE PAULI BOUND  (Q.bound, register 1141) — exceptionless on 311/311\n")
bad=0; tot=0
for (Z,c,l,S),d in H.items():
    ne=Z-c+1; B=min(corb(ne-1,l),n0f(ne-1,l)-l-1)
    v=eq(Z,c,l,S); tot+=1
    if math.floor(v)>B: bad+=1
print(f"      floor(δ) ≤ B on the equation's own output: {tot-bad}/{tot}"
      f"   {'PASSES' if bad==0 else str(bad)+' VIOLATIONS'}")
print()
print("  2 · THE HYDROGENIC BOUNDARY — δ = 0 exactly at Nₑ = 1\n")
w=[abs(eq(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4)]
print(f"      worst |δ| at Nₑ = 1: {max(w):.6f}   {'PASSES' if max(w)<0.01 else 'FAILS'}")
print()
print("  3 · THE MECHANISMS — the index's own ordering checks\n")
def checks(D):
    t=defaultdict(int)
    for (Z,c,l,S),d in D.items():
        ne=Z-c+1; B=min(corb(ne-1,l),n0f(ne-1,l)-l-1)
        if math.floor(d)>B: t["Pauli"]+=1
        if ne==1 and abs(d)>0.01: t["hydrogenic"]+=1
        if (Z,c,l+1,S) in D and D[(Z,c,l+1,S)]>d+0.02: t["ℓ-order"]+=1
        if (Z+1,c+1,l,S) in D and D[(Z+1,c+1,l,S)]>d+0.05: t["iso"]+=1
        if l<=1 and (Z,c+1,l,S) in D and D[(Z,c+1,l,S)]>d+0.05: t["charge"]+=1
    return t
tm=checks(H); te=checks({kk:eq(*kk) for kk in H})
print(f"      {'check':<14}{'measured':>10}{'anchored eq':>14}{'  verdict'}")
for kk in ("Pauli","hydrogenic","ℓ-order","iso","charge"):
    v="PASSES" if te[kk]<=tm[kk] else f"{te[kk]-tm[kk]} over"
    print(f"      {kk:<14}{tm[kk]:>10}{te[kk]:>14}   {v}")
print(f"      {'total':<14}{sum(tm.values()):>10}{sum(te.values()):>14}")
print()
print("  4 · SEATON  (A.seaton) — the polarisation arm at high ℓ\n")
hi=[(kk,d) for kk,d in H.items() if kk[2]>=4]
r=[eq(*kk)-d for kk,d in hi]
print(f"      {len(hi)} channels at ℓ ≥ 4: rms {np.sqrt(np.mean(np.square(r))):.5f}")
print()
print("  5 · Λ_α  (Q.alpha) — is the equation consistent with the polarisabilities?\n")
print("      the anchored form has NO α term — the polarisation arm is carried")
print("      entirely by the Janet collapse coordinate. So Λ_α is now UNUSED by")
print("      the equation, and that is a real change: register 1166 measured a")
print("      36% gain from α labels and the current form does not use them.")
print()
print("  6 · THE REGISTER'S OWN FIGURES\n")
IN=[(kk,d) for kk,d in H.items() if region(kk[0],kk[1],kk[2],config)]
rr=[eq(*kk)-d for kk,d in IN]
print(f"      in-region rms  {np.sqrt(np.mean(np.square(rr))):.4f}   "
      f"(register 1193 recorded 0.1329 for the unanchored fit)")
print(f"      in-region R²   {1-np.var(rr)/np.var([d for _,d in IN]):.4f}")