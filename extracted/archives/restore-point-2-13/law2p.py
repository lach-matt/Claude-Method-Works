import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
EL={2:"He",4:"Be",6:"C",12:"Mg",13:"Al",19:"K",20:"Ca",30:"Zn",31:"Ga",37:"Rb",
48:"Cd",49:"In",11:"Na",14:"Si",15:"P",16:"S",38:"Sr",39:"Y",55:"Cs",56:"Ba",
5:"B",7:"N",8:"O",21:"Sc",22:"Ti",32:"Ge",80:"Hg",83:"Bi",50:"Sn"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX"}
sp=defaultdict(list)
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5 or d<=0.02: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    sp[(Z,c)].append((l,p,d))
# add the peak captures
sp[(48,1)]=[(0,5,3.6629),(1,3,3.0513),(2,2,2.0864)]
sp[(49,1)]=[(0,5,3.7268),(1,3,3.2371),(2,2,2.2752)]
print("  LAW 2 IN TWO CARRIERS\n")
print("      the ℓ-spread of δ/√p is the width of the √p factorisation.")
print("      written in u it is 0.113·(u − 2.5).  what is it in p ?\n")
print(f"      {'species':<9}{'u':>7}{'⟨p⟩':>6}{'spread':>9}")
R=[]
for k,v in sorted(sp.items()):
    if len(v)<3: continue
    q=[d/math.sqrt(p) for l,p,d in v]
    if len(q)<3: continue
    ne=k[0]-k[1]+1
    u=math.log(ne)-(2/3)*math.log(k[1])
    pm=st.median([p for l,p,d in v])
    s=(max(q)-min(q))/st.median(q)
    R.append((u,pm,s,ne,k))
    print(f"      {EL.get(k[0],k[0])} {RO.get(k[1],k[1]):<5}{u:>7.3f}{pm:>6.1f}{s:>9.4f}")
U=np.array([a for a,_,_,_,_ in R]); PM=np.array([b for _,b,_,_,_ in R],float)
S=np.array([c for _,_,c,_,_ in R]); NE=np.array([d for _,_,_,d,_ in R],float)
print(f"\n      {len(R)} species with 3+ penetrating channels\n")
print(f"      {'carrier':<16}{'slope':>10}{'intercept':>11}{'zero at':>10}{'r²':>8}{'p':>9}")
for nm,V in (("u",U),("p (median)",PM),("ln Nₑ",np.log(NE)),("√Nₑ",np.sqrt(NE)),
             ("Nₑ",NE)):
    r=SS.linregress(V,S)
    z=-r.intercept/r.slope if abs(r.slope)>1e-9 else float("nan")
    print(f"      {nm:<16}{r.slope:>10.4f}{r.intercept:>11.4f}{z:>10.3f}"
          f"{r.rvalue**2:>8.4f}{r.pvalue:>9.4f}")
print()
print("  ARE u AND p THE SAME CARRIER HERE?\n")
print(f"      corr(u, p) = {np.corrcoef(U,PM)[0,1]:.4f}")
X=np.column_stack([U,PM,np.ones(len(S))])
b,*_=np.linalg.lstsq(X,S,rcond=None); r=S-X@b
print(f"      both together: slope_u {b[0]:+.4f}  slope_p {b[1]:+.4f}"
      f"   r² {1-np.var(r)/np.var(S):.4f}")
ru=SS.linregress(U,S); rp=SS.linregress(PM,S)
print(f"      u alone r² {ru.rvalue**2:.4f}  ·  p alone r² {rp.rvalue**2:.4f}")
print(f"      → {'u is the carrier; p is not equivalent' if ru.rvalue**2>rp.rvalue**2+0.1 else 'the two are comparable — same law, two carriers'}")
