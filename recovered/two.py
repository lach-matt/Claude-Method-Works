import math, statistics as st, json
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfgh"
# add the new captures
NEW=[(37,1,0,3.1357),(37,1,1,2.6566),(37,1,2,1.3307),(37,1,3,0.0143),
     (38,2,0,2.7115),(38,2,1,2.3636),(38,2,2,1.4592),(38,2,3,0.0610),(38,2,4,0.0092),
     (39,3,0,2.4462),(39,3,1,2.1216),(39,3,2,1.3965),(39,3,3,0.1466),(39,3,4,0.0150),
     (39,3,5,0.0042)]
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
for Z,c,l,d in NEW:
    ne=Z-c+1
    CH.append(dict(Z=Z,c=c,l=l,S=2,d=d,ne=ne,p=core_p(ne-1,l),frac=d-math.floor(d)))
ORDER=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN={}; z=0
for n,l in ORDER: OPEN[(n,l)]=z+1; z+=2*(2*l+1)
def n0(ne,l):
    v=[n for n,ll,o in config(ne) if ll==l and o>0]
    return (max(v)+1) if v else l+1
def thresh(ne,l): return OPEN.get((n0(ne,l),l),9999)
print("  TWO LADDERS — is the DIRECTION set by collapse?\n")
print("      Below its collapse threshold, an orbital sits in the OUTER well of a")
print("      double-well potential. Raising the charge pulls it inward, so δ RISES.")
print("      Above the threshold it is already inside, and δ falls with charge as")
print("      screening weakens — the ordinary Edlén ladder.\n")
seq=defaultdict(dict)
for x in CH: seq[(x["ne"],x["l"])][x["c"]]=(x["d"], x["Z"])
rows=[]
for (ne,l),d in seq.items():
    if len(d)<3: continue
    cs=sorted(d)
    ys=np.array([d[c][0] for c in cs])
    xs=np.array([float(c) for c in cs])
    r=SS.linregress(xs,ys)
    Zs=[d[c][1] for c in cs]
    thr=thresh(ne-1,l)
    below=sum(1 for Z in Zs if Z<thr)
    rows.append(dict(ne=ne,l=l,slope=r.slope,r2=r.rvalue**2,n=len(d),
                     thr=thr,Zs=Zs,below=below,frac_below=below/len(Zs)))
print(f"      {'Nₑ':>4}{'ℓ':>3}{'n':>3}{'dδ/dc':>10}{'Z range':>12}{'collapse Z':>12}{'below?':>9}")
for r in sorted(rows,key=lambda x:(x["l"],x["ne"])):
    if r["l"]<2: continue
    print(f"      {r['ne']:>4}{L[r['l']]:>3}{r['n']:>3}{r['slope']:>10.4f}"
          f"{f'{min(r[chr(39)+chr(90)+chr(115)+chr(39)] if False else r[chr(90)] if False else r[chr(39)] if False else 0)}':>0}"
          f"{f'{min(r[chr(39)]) if False else min(r[chr(90)+chr(115)]) if False else 0}':>0}"
          f"{f'{min(r[chr(90)+chr(115)])}–{max(r[chr(90)+chr(115)])}':>12}"
          f"{(r['thr'] if r['thr']<999 else 0):>12}"
          f"{('yes' if r['frac_below']>0.5 else 'no'):>9}")
print()
up=[r for r in rows if r["slope"]>0]; dn=[r for r in rows if r["slope"]<0]
print(f"      sequences with δ RISING with charge : {len(up)}")
print(f"      sequences with δ FALLING            : {len(dn)}")
print()
print(f"      {'':>22}{'median frac below threshold':>30}")
if up: print(f"      {'rising':>22}{st.median([r['frac_below'] for r in up]):>30.2f}")
if dn: print(f"      {'falling':>22}{st.median([r['frac_below'] for r in dn]):>30.2f}")
if up and dn:
    u=SS.mannwhitneyu([r["frac_below"] for r in up],[r["frac_below"] for r in dn],
                      alternative="greater")
    print(f"\n      Mann-Whitney (rising more below threshold): p = {u.pvalue:.4f}")