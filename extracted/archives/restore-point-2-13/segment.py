import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from scipy import stats as SS
from collections import defaultdict
import ground as G
L="spdfg"; R=13.605693122994
def cap(l): return 2*(2*l+1)
def bracket(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return lo,hi
# the reset points from the minimal walk
a=0.0; RESET=[]
for Z in range(3,109):
    b=bracket(Z)
    if b is None: continue
    lo,hi=b
    if lo<a<hi: continue
    a=(lo+1e-9) if a<=lo else (hi-1e-9); RESET.append(Z)
print(f"  THE RESET POINTS : {RESET}\n")
IE={3:5.391714996,4:9.322699,5:8.298019,6:11.2602880,7:14.53413,8:13.618055,
9:17.42282,10:21.564541,11:5.13907696,12:7.646236,13:5.985769,14:8.15168,
15:10.486686,16:10.3600167,17:12.967633,18:15.7596119,19:4.34066373,
20:6.1131549210,21:6.56149,22:6.828120,23:6.746187,24:6.76651,25:7.4340380,
26:7.9024681,27:7.88101,28:7.639878,29:7.726380,30:9.394197,31:5.9993020,
32:7.899435,33:9.78855,34:9.752368,35:11.81381,36:13.9996055,37:4.1771281,
38:5.69486745,39:6.21726,40:6.634126,41:6.75885,42:7.09243,43:7.11938,
44:7.36050,45:7.45890,46:8.336839,47:7.576234,48:8.993820,49:5.7863558,
50:7.343918,51:8.608389,52:9.009808,53:10.451236,54:12.1298437,
55:3.89390572743,56:5.2116646}
def seg(Z):
    s=0
    for r in RESET:
        if Z>=r: s=r
    return s
D=[]
for Z in sorted(IE):
    if Z<3: continue
    prd={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; gp=gn-gl-1
    if gp<1: continue
    q=prd.get((gn,gl),0); nu=math.sqrt(R/IE[Z])
    D.append((Z,gn,gl,gp,q,(gn-nu)/math.sqrt(gp),seg(Z)))
print("  THE OCCUPANCY SLOPE, PER (SUBSHELL, SEGMENT)  —  no pooling\n")
BY=defaultdict(list)
for Z,gn,gl,gp,q,am,s in D: BY[(gn,gl,s)].append((q,Z,am))
print(f"      {'shell':>7}{'segment':>9}{'n':>4}{'slope':>10}{'r²':>9}{'p':>10}")
OUT=[]
for k in sorted(BY):
    v=sorted(BY[k])
    if len(v)<3: continue
    q=np.array([x[0] for x in v],float); aa=np.array([x[2] for x in v])
    if len(set(q))<2: continue
    r=SS.linregress(q,aa)
    print(f"      {f'{k[0]}{L[k[1]]}':>7}{f'Z≥{k[2]}':>9}{len(v):>4}"
          f"{r.slope:>10.4f}{r.rvalue**2:>9.4f}{r.pvalue:>10.5f}")
    OUT.append((k,r.slope,r.rvalue**2,len(v)))
print()
print("  AND THE SAME SUBSHELL SPLIT ACROSS SEGMENTS\n")
sub=defaultdict(list)
for (n,l,s),sl,r2,cnt in OUT: sub[(n,l)].append((s,sl,r2,cnt))
for k in sorted(sub):
    if len(sub[k])<2: continue
    print(f"      {k[0]}{L[k[1]]} :")
    for s,sl,r2,cnt in sorted(sub[k]):
        print(f"          segment Z≥{s:<4} n={cnt}  slope {sl:+.4f}  r² {r2:.4f}")
print()
print("      → if the slope is constant within a segment and jumps between,")
print("        the reset mechanism and the slope variation are one object.")
