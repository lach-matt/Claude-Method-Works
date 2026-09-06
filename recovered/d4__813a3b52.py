import re, math, statistics as st
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit
Rinf=109737.31568; mp=1836.15267343
SPEC=[("BaII",56,2,137.33,"5g|6g|7g|8g|9g","2G"),
      ("CaII_full",20,2,40.078,"[5-9]g","2G"),
      ("CdII_full",48,2,112.41,"[5-9]g|1[01]g","2G"),
      ("SiII",14,2,28.085,r"3s2\.[5-9]g","2G"),
      ("SiIII",14,3,28.085,"[5-9]g","1G")]
print("  REFITTING WITH δ₄ — the raw levels, on data already held\n")
print(f"  {'channel':<10}{'n':>3}{'  members':<12}{'δ₀':>9}{'δ₂':>10}{'ratio':>8}"
      f"{'   →   δ₀':>11}{'δ₂':>10}{'δ₄':>11}{'ratio':>8}")
out=[]
for f,Z,c,A,pat,term in SPEC:
    RM=Rinf/(1+1/(A*mp))
    lv=[]; lim=None
    for line in open(f"spectra_raw/{f}.tsv",encoding="utf-8"):
        if line.startswith("#"):
            m=re.search(r"limit[= ]+([\d.]+)",line,re.I)
            if m: lim=float(m.group(1))
            continue
        r=line.rstrip("\n").split("\t")
        if len(r)<4: continue
        if not re.match(pat,r[0]) or term not in r[1]: continue
        n=re.search(r"(\d+)g",r[0])
        if not n: continue
        try: lv.append((int(n.group(1)),float(r[3])))
        except Exception: pass
    lv=sorted(set(lv))
    if len(lv)<4: print(f"  {f:<10}   only {len(lv)} members"); continue
    # derive the limit from the series itself if not stored
    def resid(L,order):
        n=np.array([x[0] for x in lv],float); E=np.array([x[1] for x in lv])
        if E.max()>=L: return 1e9,None
        ns=c*np.sqrt(RM/(L-E)); d=n-ns
        def g2(x,a,b): return a+b/(x-a)**2
        def g4(x,a,b,cc): return a+b/(x-a)**2+cc/(x-a)**4
        try:
            p,_=curve_fit(g4 if order==4 else g2, n, d,
                          p0=([0.02,-0.1,0.0] if order==4 else [0.02,-0.1]),maxfev=200000)
            r=d-(g4(n,*p) if order==4 else g2(n,*p))
            return float(np.sqrt(np.mean(r**2))), p
        except Exception: return 1e9,None
    from scipy.optimize import minimize_scalar
    best=None
    for L in np.linspace(max(x[1] for x in lv)+50, max(x[1] for x in lv)+40000, 400):
        s,_=resid(L,2)
        if best is None or s<best[0]: best=(s,L)
    L=best[1]
    s2,p2=resid(L,2); s4,p4=resid(L,4)
    if p2 is None: continue
    l=4; pr=-l*(l+1)/3.0
    r2=(p2[1]/p2[0])/pr
    if p4 is not None and abs(p4[0])>1e-6:
        r4=(p4[1]/p4[0])/pr
        print(f"  {f:<10}{len(lv):>3}{'  '+str([x[0] for x in lv])[:9]:<12}"
              f"{p2[0]:>9.5f}{p2[1]:>10.5f}{r2:>8.2f}"
              f"{p4[0]:>11.5f}{p4[1]:>10.5f}{p4[2]:>11.5f}{r4:>8.2f}")
        out.append((f,len(lv),r2,r4,p4[2]))
    else:
        print(f"  {f:<10}{len(lv):>3}   δ₄ fit failed")
print()
if out:
    print(f"      median ratio with δ₂ only : {st.median([x[2] for x in out]):.3f}")
    print(f"      median ratio with δ₄      : {st.median([x[3] for x in out]):.3f}")
    print(f"      δ₄ values                 : " + " ".join(f"{x[4]:+.4f}" for x in out))
    same=all(x[4]<0 for x in out) or all(x[4]>0 for x in out)
    print(f"      δ₄ same sign in all?      : {'YES' if same else 'no'}")