import sys, math, statistics as st; sys.path.insert(0,"/home/claude/work")
import ground as G
import numpy as np
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
def corr(Z,use_q=True):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]
    rad=lambda n,l:(n-l-1)+(pr.get((n,l),0)/cap(l) if use_q else 0)
    rg=rad(gn,gl); cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF; bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(rad(n,l))-math.sqrt(rg); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo=r/d
    return (gn,gl),lo,hi,bhi,pr
def slater_Zeff(Z,n,l,occ):
    """Slater's rules, no fitting: screening of an electron in (n,l)."""
    s=0.0
    for (m,k),o in occ.items():
        if (m,k)==(n,l): o=max(0,o-0)          # the others in its own group
        if m==n and k<=1 and l<=1: s+=0.35*(o-(1 if (m,k)==(n,l) else 0))
        elif m==n and (k>=2 or l>=2): s+=0.35*(o-(1 if (m,k)==(n,l) else 0))
        elif m==n-1 and l<=1: s+=0.85*o
        elif m<n-1 or (l>=2 and m<n): s+=1.00*o
    return Z-s
REC={3,19,37,42,43,45,55,58,64,65,80,81,87,91,96,97,103,104}
a=None; R=[]
for Z in range(3,109):
    c0=corr(Z,False); cq=corr(Z,True)
    if not c0 or not cq: continue
    lo,hi=c0[1],c0[2]
    if a is None or not (lo-1e-9<=a<=hi+1e-9):
        a = lo if (lo>-INF/2 and abs(lo)>1e-9) else (hi if hi<INF/2 else lo)
    if cq[2]>=INF/2: continue
    (gn,gl),_,hiq,bhi,pr = cq
    ze = slater_Zeff(Z,gn,gl,pr)
    R.append((Z,hiq-a,ze,gl,Z in REC,bhi))
m=np.array([r[1] for r in R]); ze=np.array([r[2] for r in R])
rst=np.array([r[4] for r in R])
print(f"  MARGIN against SLATER Z*  —  {len(R)} steps, no fitted parameter\n")
for lab,f_ in (("margin vs Z*", ze),("margin vs 1/Z*",1/ze),("margin vs Z*^2",ze**2)):
    c=np.corrcoef(m,f_)[0,1]
    print(f"      {lab:<18} r = {c:+.4f}   r^2 = {c*c:.4f}")
print(f"\n  and Z* itself: resets {np.median(ze[rst]):.2f}"
      f"   non-resets {np.median(ze[~rst]):.2f}")
print("\n  THE PROPOSAL: the CHARGE OF TWO creates proximity by attraction.")
print("  test — is the margin smallest where the binding rival is an s shell")
print("  holding TWO, or holding ONE?\n")
from collections import defaultdict
g=defaultdict(list)
for Z,mm,z_,gl,r,bhi in R:
    if bhi is None: continue
    occ=corr(Z,True)[4].get(bhi,0)
    key=(LS[bhi[1]], occ)
    g[key].append((mm,r))
print(f"  {'rival kind':>14}{'occ':>5}{'n':>5}{'median margin':>15}{'resets':>8}")
for k in sorted(g,key=lambda k:st.median([x[0] for x in g[k]])):
    v=g[k]; print(f"  {k[0]:>14}{k[1]:>5}{len(v):>5}"
                  f"{st.median([x[0] for x in v]):>15.4f}{sum(1 for _,r in v if r):>8}")