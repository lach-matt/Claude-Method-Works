import math, statistics as st
import numpy as np
Rinf=109737.31568; mp=1836.15267343
# the 1P* members of the 5d10.6s.np series -- the cleanest single series
DATA={
 "Tl II":(81,2,204.38,164765,{6:75663.33,7:122379,8:141000,9:149063,
                              10:153633,11:156475}),
 "Pb III":(82,3,207.2,None,{6:95340.1,7:177181.4,8:209318}),
 "Bi IV":(83,4,208.98,365900,{6:114602,7:231913}),
}
print("  THE MERCURY-CORE np SERIES — 5d¹⁰6s core, p = 4\n")
OUT={}
for nm,(Z,c,A,lim,ser) in DATA.items():
    RM=Rinf/(1+1/(A*mp))
    n=np.array(sorted(ser),float); E=np.array([ser[int(x)] for x in n])
    if lim is None:
        best=None
        for Ltry in np.linspace(E.max()+2000, E.max()+120000, 12000):
            ns=c*np.sqrt(RM/(Ltry-E)); d=n-ns
            s=float(np.std(d))
            if best is None or s<best[0]: best=(s,Ltry)
        lim=best[1]
        print(f"  {nm}: limit fitted to {lim:.0f} cm⁻¹  (sd of δ {best[0]:.4f})")
    ns=c*np.sqrt(RM/(lim-E)); d=n-ns
    print(f"\n  {nm}   Z={Z} charge {c}   limit {lim:.0f}\n")
    print(f"      {'n':>4}{'E':>12}{'n*':>9}{'δ':>9}")
    for a,b,cc in zip(n,E,d): print(f"      {int(a):>4}{b:>12.1f}{a-cc:>9.4f}{cc:>9.4f}")
    dd=d[-min(4,len(d)):]
    print(f"      δ (highest {len(dd)}) = {st.median(dd):.4f}   sd {st.pstdev(dd):.4f}")
    OUT[(Z,c)]=float(st.median(dd))
print()
print("  AND WHAT THE EQUATION SAYS\n")
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
cp,out_,n0_,regime=g["cp"],g["out_"],g["n0_"],g["regime"]
a2,k=0.5060,0.4514
print(f"      {'species':<9}{'Nₑ':>5}{'p':>3}{'regime':>8}{'measured δ':>13}{'equation':>11}{'ratio':>8}")
for (Z,c),dm in sorted(OUT.items()):
    ne=Z-c+1; p=cp(ne-1,1,c); rg=regime(Z,c,1)
    pred=a2*math.sqrt(p)*ne**k*(math.log(c+1)/c)
    nm=[x for x,(zz,ccc,_,_,_) in DATA.items() if zz==Z][0]
    print(f"      {nm:<9}{ne:>5}{p:>3}{rg:>8}{dm:>13.4f}{pred:>11.4f}{dm/pred:>8.3f}")
import json
json.dump({f"{k2[0]},{k2[1]}":v for k2,v in OUT.items()},open("/tmp/hg.json","w"))