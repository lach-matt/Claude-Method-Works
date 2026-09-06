import math, statistics as st, json
import numpy as np
from collections import defaultdict
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]   # Z,c,ne,a,rms,R2,n
print("  STEP 2 · COMPARING THE 41 EQUATIONS\n")
print("  A · WHAT THEY HAVE IN COMMON\n")
print("      every one is δ = a·√p. The FORM is identical; only a differs.")
print("      p is read from the ground configuration, never fitted.\n")
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); W=np.array([o[6] for o in O],float)
print("  B · HOW a DEPENDS ON CHARGE, AT FIXED Nₑ\n")
print(f"      {'Nₑ':>5}{'charges':>9}{'x = −dln a/dln c':>19}{'r²':>8}{'C = x√Nₑ':>11}")
byne=defaultdict(dict)
for Z,c,ne,a,rms,R2,n in O: byne[ne][c]=a
XS=[]
for ne in sorted(byne):
    d=byne[ne]
    if len(d)<3: continue
    cs=sorted(d)
    r=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    print(f"      {ne:>5}{len(cs):>9}{-r.slope:>19.4f}{r.rvalue**2:>8.4f}"
          f"{-r.slope*math.sqrt(ne):>11.4f}")
    XS.append((ne,-r.slope,-r.slope*math.sqrt(ne),len(cs)))
if XS:
    Cv=[c for _,_,c,_ in XS]
    print(f"\n      C = x·√Nₑ : median {st.median(Cv):.4f}   sd {st.pstdev(Cv):.4f}"
          f"   range {min(Cv):.3f}–{max(Cv):.3f}")
    r=SS.linregress(np.log([n for n,_,_,_ in XS]),Cv)
    print(f"      C against ln Nₑ : slope {r.slope:+.4f}  r² {r.rvalue**2:.3f}"
          f"  p {r.pvalue:.4f}   → {'DRIFTS' if r.pvalue<0.05 else 'CONSTANT'}")
print()
print("  C · HOW a DEPENDS ON Nₑ, AT FIXED CHARGE\n")
print(f"      {'charge':>7}{'species':>9}{'k = dln a/dln Nₑ':>19}{'r²':>8}")
bych=defaultdict(dict)
for Z,c,ne,a,rms,R2,n in O: bych[c][ne]=a
KS=[]
for c in sorted(bych):
    d=bych[c]
    if len(d)<4: continue
    ns=sorted(d)
    r=SS.linregress(np.log(ns),np.log([d[n] for n in ns]))
    print(f"      {c:>7}{len(ns):>9}{r.slope:>19.4f}{r.rvalue**2:>8.4f}")
    KS.append((c,r.slope,len(ns)))
if KS:
    kk=[k for _,k,_ in KS]
    print(f"\n      k : median {st.median(kk):.4f}   sd {st.pstdev(kk):.4f}"
          f"   range {min(kk):.3f}–{max(kk):.3f}")
    r=SS.linregress([c for c,_,_ in KS],kk)
    print(f"      k against charge : slope {r.slope:+.4f}  r² {r.rvalue**2:.3f}"
          f"  p {r.pvalue:.4f}   → {'DRIFTS' if r.pvalue<0.05 else 'CONSTANT'}")
print()
print("  D · THE JOINT FIT ON THE 41 CONSTANTS ALONE\n")
X=np.column_stack([np.log(NE),-np.log(C)/np.sqrt(NE),np.ones(len(A))])
b,*_=np.linalg.lstsq(X,np.log(A),rcond=None); r=np.log(A)-X@b
print(f"      ln a = {b[0]:.4f}·ln Nₑ − {b[1]:.4f}·ln c/√Nₑ {b[2]:+.4f}")
print(f"      k = {b[0]:.4f}   C = {b[1]:.4f}   A = {math.exp(b[2]):.4f}")
print(f"      r² {1-np.var(r)/np.var(np.log(A)):.4f}   rms in ln a {float(np.sqrt(np.mean(r**2))):.4f}")
print(f"      {len(A)} species, and NOT ONE channel — the constants alone\n")
np.save("/tmp/step2.npy",b)
print("  E · WHERE THE 41 DISAGREE WITH THE JOINT FIT\n")
pred=np.exp(X@b)
q=A/pred
print(f"      {'charge':>7}{'n':>4}{'median a/pred':>15}")
for c in (1,2,3,4,5):
    m=C==c
    if m.sum()<3: continue
    print(f"      {c:>7}{int(m.sum()):>4}{st.median(q[m]):>15.3f}")
print()
print(f"      {'Nₑ band':>9}{'n':>4}{'median a/pred':>15}")
for lo,hi in ((2,6),(6,15),(15,32),(32,60)):
    m=(NE>=lo)&(NE<hi)
    if m.sum()<3: continue
    print(f"      {f'{lo}–{hi}':>9}{int(m.sum()):>4}{st.median(q[m]):>15.3f}")