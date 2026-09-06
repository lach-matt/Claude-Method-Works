import re, math, statistics as st
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit
Rinf=109737.31568; mp=1836.15267343
L={"s":0,"p":1,"d":2,"f":3,"g":4,"h":5}
SPEC=[("RbI","Rb I",37,1,84.912,None),
      ("SrII","Sr II",38,2,87.906,88965.18),
      ("YIII","Y III",39,3,88.906,165540.5)]
print("  THE KRYPTON-CORE SEQUENCE — Nₑ = 37, charges 1, 2, 3\n")
OUT={}
for f,nm,Z,c,A,lim in SPEC:
    RM=Rinf/(1+1/(A*mp))
    ser=defaultdict(list)
    for line in open(f"spectra_raw/{f}.tsv",encoding="utf-8"):
        if line.startswith("#"): continue
        r=line.rstrip("\n").split("\t")
        if len(r)<4: continue
        m=re.match(r"(\d+)([spdfgh])",r[0])
        if not m: continue
        try: E=float(r[3])
        except Exception: continue
        ser[L[m.group(2)]].append((int(m.group(1)),E))
    # fit limit if absent, jointly across the longest series
    if lim is None:
        best=None
        cand=max(ser.items(),key=lambda kv:len(kv[1]))
        n=np.array([a for a,_ in cand[1]],float); E=np.array([b for _,b in cand[1]])
        for Ltry in np.linspace(E.max()+20, E.max()+400, 4000):
            ns=c*np.sqrt(RM/(Ltry-E)); d=n-ns
            s=float(np.std(d))
            if best is None or s<best[0]: best=(s,Ltry)
        lim=best[1]
        print(f"  {nm}: limit fitted to {lim:.2f} cm⁻¹ (sd of δ {best[0]:.4f})")
    print(f"\n  {nm}   Z = {Z}, charge {c}, limit {lim:.2f}\n")
    print(f"      {'ℓ':>3}{'members':>9}{'n range':>12}{'δ':>10}{'σ(δ)':>9}")
    for l in sorted(ser):
        v=sorted(ser[l])
        if len(v)<2: continue
        n=np.array([a for a,_ in v],float); E=np.array([b for _,b in v])
        keep=E<lim-1
        n,E=n[keep],E[keep]
        if len(n)<2: continue
        ns=c*np.sqrt(RM/(lim-E)); d=n-ns
        # use the highest members: least affected by perturbation
        dd=d[-min(6,len(d)):]
        print(f"      {'spdfgh'[l]:>3}{len(n):>9}{f'{int(n[0])}–{int(n[-1])}':>12}"
              f"{st.median(dd):>10.4f}{st.pstdev(dd):>9.4f}")
        OUT[(Z,c,l)]=st.median(dd)
import json
json.dump({f"{k[0]},{k[1]},{k[2]}":v for k,v in OUT.items()},
          open("/tmp/kr.json","w"))
print(f"\n  {len(OUT)} channels extracted")