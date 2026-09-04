import statistics as st
from collections import defaultdict
from scipy import stats as SS
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; bysp=defaultdict(list)
for x in CH: bysp[(x["Z"],x["c"])].append(x)
print("  THE DICHOTOMY: NEUTRAL AGAINST ION\n")
print("  The three lines are not smooth in charge. They are a STEP at charge 2.\n")
def rate(sel):
    a=d=0
    for k,v in bysp.items():
        if not sel(k[1]): continue
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                x,y=v[i],v[j]
                if x["nl"]==y["nl"]: continue
                lo,hi=(x,y) if x["nl"]<y["nl"] else (y,x)
                if lo["nstar"]<hi["nstar"]: a+=1
                else: d+=1
    return a,d
a1,d1=rate(lambda c:c==1); a2,d2=rate(lambda c:c>=2)
print(f"      {'set':<16}{'pairs':>8}{'agree':>8}{'fail':>7}{'rate':>9}")
print(f"      {'NEUTRAL (c=1)':<16}{a1+d1:>8}{a1:>8}{d1:>7}{100*a1/(a1+d1):>8.1f}%")
print(f"      {'IONS (c≥2)':<16}{a2+d2:>8}{a2:>8}{d2:>7}{100*a2/(a2+d2):>8.1f}%")
tab=[[a1,d1],[a2,d2]]
try:
    odds,p=SS.fisher_exact(tab)
    print(f"\n      Fisher exact: p = {p:.4f}   {'SIGNIFICANT' if p<0.05 else 'not significant'}")
except Exception as e: print(f"      {e}")
print()
print("  and the s–d gap, neutral against ion:\n")
def gaps(sel):
    out=[]
    for k,v in bysp.items():
        if not sel(k[1]): continue
        s=[x for x in v if x["l"]==0]; d=[x for x in v if x["l"]==2]
        if not s or not d: continue
        out.append(min(x["nstar"] for x in d)-min(x["nstar"] for x in s))
    return out
g1=gaps(lambda c:c==1); g2=gaps(lambda c:c>=2)
print(f"      neutral: n = {len(g1):>3}   median {st.median(g1):+.3f}   "
      f"negative in {sum(1 for x in g1 if x<0)}")
print(f"      ions   : n = {len(g2):>3}   median {st.median(g2):+.3f}   "
      f"negative in {sum(1 for x in g2 if x<0)}")
u=SS.mannwhitneyu(g1,g2,alternative="greater")
print(f"\n      Mann-Whitney (neutral > ion): U = {u.statistic:.0f}, p = {u.pvalue:.4f}")
print()
print("  and the grouping ratio, neutral against ion:\n")
def ratio(sel):
    W=[];A=[]
    for k,v in bysp.items():
        if not sel(k[1]) or len(v)<2: continue
        grp=defaultdict(list)
        for x in v: grp[x["nl"]].append(x["d"])
        for nl,ds in grp.items():
            if len(ds)>=2: W.append(max(ds)-min(ds))
        A.append(max(x["d"] for x in v)-min(x["d"] for x in v))
    return st.median(W)/max(st.median(A),1e-9), len(A)
r1,n1=ratio(lambda c:c==1); r2,n2=ratio(lambda c:c>=2)
print(f"      neutral: {r1:.3f}  ({n1} species)")
print(f"      ions   : {r2:.3f}  ({n2} species)")
