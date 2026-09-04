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
    return lo,hi,gn,gl,gp
IE={5:8.298019,6:11.2602880,7:14.53413,8:13.618055,9:17.42282,10:21.564541,
13:5.985769,14:8.15168,15:10.486686,16:10.3600167,17:12.967633,18:15.7596119,
19:4.34066373,20:6.1131549210,31:5.9993020,32:7.899435,33:9.78855,34:9.752368,
35:11.81381,36:13.9996055,37:4.1771281,38:5.69486745,39:6.21726,40:6.634126,
41:6.75885,49:5.7863558,50:7.343918,51:8.608389,52:9.009808,53:10.451236,
54:12.1298437,55:3.89390572743,56:5.2116646}
print("  THE POSITION IN THE CORRIDOR  —  t = (a_meas − L)/(U − L)\n")
print("      if the path is graded, t should be a function of the grade —")
print("      here, of q, the occupancy already present.\n")
BY=defaultdict(list)
for Z in sorted(IE):
    b=bracket(Z)
    if b is None: continue
    lo,hi,gn,gl,gp=b
    if gp<1 or lo<-1e8 or hi>1e8: continue
    prd={(n,l):o for n,l,o in G.expand(Z-1)}
    q=prd.get((gn,gl),0)
    nu=math.sqrt(R/IE[Z]); am=(gn-nu)/math.sqrt(gp)
    t=(am-lo)/(hi-lo)
    BY[(gn,gl)].append((q,Z,am,lo,hi,t))
print(f"      {'shell':>7}{'q':>4}{'Z':>5}{'el':>4}{'a_meas':>9}{'L':>8}{'U':>8}{'t':>9}")
for k in sorted(BY):
    v=sorted(BY[k])
    if len(v)<3: continue
    for q,Z,am,lo,hi,t in v:
        print(f"      {f'{k[0]}{L[k[1]]}':>7}{q:>4}{Z:>5}{G.GROUND[Z][0]:>4}"
              f"{am:>9.4f}{lo:>8.3f}{hi:>8.3f}{t:>9.4f}")
    qq=np.array([x[0] for x in v],float); tt=np.array([x[5] for x in v])
    r=SS.linregress(qq,tt)
    print(f"      → t vs q : slope {r.slope:+.4f}  intercept {r.intercept:+.4f}"
          f"  r² {r.rvalue**2:.4f}  p {r.pvalue:.5f}\n")
print("  THE GRADING, PER SUBSHELL — the bridge from L to U\n")
print("      if t runs from ~0 at q=0 to ~1 at q=full, the corridor's two ends")
print("      ARE the two observations and the grading is the path between.\n")
print(f"      {'shell':>7}{'t at q=0':>11}{'t at q=max':>13}{'span':>9}")
for k in sorted(BY):
    v=sorted(BY[k])
    if len(v)<3: continue
    print(f"      {f'{k[0]}{L[k[1]]}':>7}{v[0][5]:>11.4f}{v[-1][5]:>13.4f}"
          f"{v[-1][5]-v[0][5]:>9.4f}")
