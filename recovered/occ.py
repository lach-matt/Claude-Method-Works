import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from scipy import stats as SS
import ground as G
L="spdfg"; R=13.605693122994
IE={3:5.391714996,4:9.322699,5:8.298019,6:11.2602880,7:14.53413,8:13.618055,
9:17.42282,10:21.564541,11:5.13907696,12:7.646236,13:5.985769,14:8.15168,
15:10.486686,16:10.3600167,17:12.967633,18:15.7596119,19:4.34066373,
20:6.1131549210,21:6.56149,22:6.828120,23:6.746187,24:6.76651,25:7.4340380,
26:7.9024681,27:7.88101,28:7.639878,29:7.726380,30:9.394197,31:5.9993020,
32:7.899435,33:9.78855,34:9.752368,35:11.81381,36:13.9996055,37:4.1771281,
38:5.69486745,39:6.21726,40:6.634126,41:6.75885,42:7.09243,43:7.11938,
44:7.36050,45:7.45890,46:8.336839,47:7.576234,48:8.993820,49:5.7863558,
50:7.343918,51:8.608389,52:9.009808,53:10.451236,54:12.1298437,
55:3.89390572743,56:5.2116646,80:10.437504,81:6.1082873,86:10.74850,
87:4.0727411,88:5.2784239}
print("  THE STATEMENT: ν depends on OCCUPANCY, which the law has no coordinate for\n")
print("      test: within a subshell being filled, does a_meas rise with the")
print("      number of electrons already in it?\n")
D=[]
for Z in sorted(IE):
    cfg=G.expand(Z); pr=G.expand(Z-1)
    prd={(n,l):o for n,l,o in pr}
    cu={(n,l):o for n,l,o in cfg}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; gp=gn-gl-1
    if gp<1: continue
    q=prd.get((gn,gl),0)          # electrons ALREADY in the subshell
    nu=math.sqrt(R/IE[Z]); am=(gn-nu)/math.sqrt(gp)
    D.append((Z,gn,gl,gp,q,am))
print(f"      {'shell':>7}{'q':>4}{'Z':>5}{'el':>4}{'a_meas':>10}")
from collections import defaultdict
BY=defaultdict(list)
for Z,gn,gl,gp,q,am in D: BY[(gn,gl)].append((q,Z,am))
for k in sorted(BY):
    v=sorted(BY[k])
    if len(v)<3: continue
    for q,Z,am in v:
        print(f"      {f'{k[0]}{L[k[1]]}':>7}{q:>4}{Z:>5}{G.GROUND[Z][0]:>4}{am:>10.4f}")
    qs=np.array([x[0] for x in v],float); aa=np.array([x[2] for x in v])
    r=SS.linregress(qs,aa)
    print(f"      → slope {r.slope:+.4f} per electron · r² {r.rvalue**2:.4f}"
          f" · p {r.pvalue:.5f}\n")
print("  POOLED ACROSS ALL SUBSHELLS\n")
Q=np.array([d[4] for d in D],float); A=np.array([d[5] for d in D])
NN=np.array([d[1] for d in D],float); GP=np.array([d[3] for d in D],float)
r=SS.linregress(Q,A)
print(f"      a_meas vs q : slope {r.slope:+.4f}  r² {r.rvalue**2:.4f}  p {r.pvalue:.2e}")
X=np.column_stack([Q,NN,GP,np.ones(len(A))])
b,*_=np.linalg.lstsq(X,A,rcond=None); res=A-X@b
print(f"      a_meas vs q, n, p : r² {1-np.var(res)/np.var(A):.4f}"
      f"   coef_q {b[0]:+.4f}")
print()
print("  AND THE CORRECTED FORM  ν = n − (a + b·q)·√p\n")
print("      solving for a and b from all data:")
Xc=np.column_stack([np.sqrt(GP),Q*np.sqrt(GP)])
NU=np.array([d[1] for d in D],float)-A*np.sqrt(GP)
y=np.array([d[1] for d in D],float)-NU
bb,*_=np.linalg.lstsq(Xc,y,rcond=None)
print(f"          a = {bb[0]:.4f}   b = {bb[1]:.4f} per electron")
pred=Xc@bb; rr=y-pred
print(f"          r² {1-np.var(rr)/np.var(y):.4f}   rms {float(np.sqrt(np.mean(rr**2))):.4f}")