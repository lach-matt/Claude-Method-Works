import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from scipy import stats as SS
from collections import defaultdict
import ground as G
L="spdfg"; R=13.605693122994
def cap(l): return 2*(2*l+1)
def brack(Z):
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
IE={21:6.56149,22:6.828120,23:6.746187,24:6.76651,25:7.4340380,26:7.9024681,
27:7.88101,28:7.639878,29:7.726380,30:9.394197,
39:6.21726,40:6.634126,41:6.75885,42:7.09243,43:7.11938,44:7.36050,
45:7.45890,46:8.336839,47:7.576234,48:8.993820,
57:5.5769,71:5.425871,72:6.825070,73:7.549571,74:7.86403,75:7.83352,
76:8.43823,77:8.96702,78:8.95883,79:9.225554,80:10.437504,
5:8.298019,6:11.2602880,7:14.53413,8:13.618055,9:17.42282,10:21.564541,
13:5.985769,14:8.15168,15:10.486686,16:10.3600167,17:12.967633,18:15.7596119,
31:5.9993020,32:7.899435,33:9.78855,34:9.752368,35:11.81381,36:13.9996055,
49:5.7863558,50:7.343918,51:8.608389,52:9.009808,53:10.451236,54:12.1298437,
81:6.1082873,82:7.4166799,83:7.285516,84:8.418070,85:9.31751,86:10.74850}
print("  IS THE HIGH INITIATION A d PROPERTY?  —  per subshell, no pooling\n")
BY=defaultdict(list)
for Z in sorted(IE):
    b=brack(Z)
    if b is None: continue
    lo,hi,gn,gl,gp=b
    if gp<1 or lo<-1e8 or hi>1e8: continue
    prd={(n,l):o for n,l,o in G.expand(Z-1)}
    q=prd.get((gn,gl),0)
    nu=math.sqrt(R/IE[Z]); am=(gn-nu)/math.sqrt(gp)
    BY[(gn,gl)].append((q,Z,am,lo,hi,(am-lo)/(hi-lo)))
print(f"      {'shell':>7}{'n':>4}{'t at q=0':>11}{'t at q=max':>13}"
      f"{'slope':>10}{'r²':>9}{'p':>10}")
for k in sorted(BY,key=lambda x:(x[1],x[0])):
    v=sorted(BY[k])
    if len(v)<3: continue
    q=np.array([x[0] for x in v],float); t=np.array([x[5] for x in v])
    r=SS.linregress(q,t)
    print(f"      {f'{k[0]}{L[k[1]]}':>7}{len(v):>4}{v[0][5]:>11.4f}{v[-1][5]:>13.4f}"
          f"{r.slope:>10.4f}{r.rvalue**2:>9.4f}{r.pvalue:>10.5f}")
print()
print("  GROUPED BY ℓ  —  reported as a LIST, not summarised\n")
for l in (1,2):
    print(f"      ℓ = {L[l]}")
    for k in sorted(BY):
        if k[1]!=l: continue
        v=sorted(BY[k])
        if len(v)<3: continue
        print(f"          {k[0]}{L[l]} : t(q=0) = {v[0][5]:.4f}   "
              f"corridor ({v[0][3]:.3f}, {v[0][4]:.3f})   a_meas {v[0][2]:.4f}")
    print()
