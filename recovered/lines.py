import re, math, statistics as st
from collections import defaultdict
from scipy import stats as SS
import numpy as np
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; bysp=defaultdict(list)
for x in CH: bysp[(x["Z"],x["c"])].append(x)

print("  LINE 2 · DOES δ's n+ℓ GROUPING WEAKEN WITH CHARGE?\n")
print("      If the focusing picture is a NEUTRAL-atom fact, the within-group")
print("      spread should grow with charge relative to the whole-species spread.\n")
print(f"      {'charge':>7}{'species':>9}{'within':>10}{'whole':>9}{'ratio':>9}")
rows=[]
for c in (1,2,3,4,5,6):
    W=[];A=[]
    for k,v in bysp.items():
        if k[1]!=c or len(v)<2: continue
        grp=defaultdict(list)
        for x in v: grp[x["nl"]].append(x["d"])
        for nl,ds in grp.items():
            if len(ds)>=2: W.append(max(ds)-min(ds))
        A.append(max(x["d"] for x in v)-min(x["d"] for x in v))
    if len(W)<3 or len(A)<3: continue
    r=st.median(W)/max(st.median(A),1e-9)
    rows.append((c,r))
    print(f"      {c:>7}{len(A):>9}{st.median(W):>10.4f}{st.median(A):>9.4f}{r:>9.3f}")
if len(rows)>=4:
    rr=SS.linregress([a for a,_ in rows],[b for _,b in rows])
    print(f"\n      ratio against charge: slope {rr.slope:+.4f}, r² {rr.rvalue**2:.3f}, p {rr.pvalue:.4f}")
    print(f"      → {'GROUPING WEAKENS with charge' if rr.slope>0 and rr.pvalue<0.1 else 'no charge trend'}")

print("\n\n  LINE 3 · DOES THE MADELUNG AGREEMENT RATE FALL WITH CHARGE?\n")
print(f"      {'charge':>7}{'pairs':>8}{'agree':>8}{'rate':>9}")
pts=[]
for c in range(1,10):
    a=d=0
    for k,v in bysp.items():
        if k[1]!=c: continue
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                x,y=v[i],v[j]
                if x["nl"]==y["nl"]: continue
                lo,hi=(x,y) if x["nl"]<y["nl"] else (y,x)
                if lo["nstar"]<hi["nstar"]: a+=1
                else: d+=1
    if a+d<8: continue
    pts.append((c,100*a/(a+d)))
    print(f"      {c:>7}{a+d:>8}{a:>8}{100*a/(a+d):>8.1f}%")
if len(pts)>=4:
    rr=SS.linregress([x for x,_ in pts],[y for _,y in pts])
    print(f"\n      rate against charge: slope {rr.slope:+.2f} pts/charge, "
          f"r² {rr.rvalue**2:.3f}, p {rr.pvalue:.4f}")
    print(f"      → {'AGREEMENT FALLS with charge' if rr.slope<0 and rr.pvalue<0.1 else 'no trend'}")

print("\n\n  LINE 4 · THE s–d GAP ITSELF, AGAINST CHARGE\n")
gaps=[]
for k,v in bysp.items():
    s=[x for x in v if x["l"]==0]; d=[x for x in v if x["l"]==2]
    if not s or not d: continue
    ns=min(x["nstar"] for x in s); nd=min(x["nstar"] for x in d)
    gaps.append((k[1], nd-ns))
if gaps:
    by=defaultdict(list)
    for c,gp in gaps: by[c].append(gp)
    print(f"      {'charge':>7}{'species':>9}{'median n*(d) − n*(s)':>24}")
    xs=[];ys=[]
    for c in sorted(by):
        print(f"      {c:>7}{len(by[c]):>9}{st.median(by[c]):>24.3f}")
        xs+= [c]*len(by[c]); ys+=by[c]
    rr=SS.linregress(xs,ys)
    print(f"\n      slope {rr.slope:+.4f} per charge, r² {rr.rvalue**2:.3f}, p {rr.pvalue:.2e}")
    print(f"      the gap crosses zero at charge {(-rr.intercept/rr.slope):.2f}"
          if rr.slope else "")
    print(f"      → POSITIVE means 3d ABOVE 4s (Madelung holds); negative means inverted")