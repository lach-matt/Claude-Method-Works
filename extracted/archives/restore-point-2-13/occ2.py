import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from scipy import stats as SS
from collections import defaultdict
import ground as G
L="spdfg"; R=13.605693122994
exec(open("/tmp/occ.py").read().split("print(")[0].split("import ground")[1]
     .replace(" as G","")) if False else None
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
D=[]
for Z in sorted(IE):
    prd={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>prd.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; gp=gn-gl-1
    if gp<1: continue
    q=prd.get((gn,gl),0)
    nu=math.sqrt(R/IE[Z])
    D.append((Z,gn,gl,gp,q,nu))
print("  THE OCCUPANCY SLOPE, BY SUBSHELL — is it a constant or does it scale?\n")
BY=defaultdict(list)
for Z,gn,gl,gp,q,nu in D: BY[(gn,gl)].append((q,Z,(gn-nu)/math.sqrt(gp)))
print(f"      {'shell':>7}{'ℓ':>3}{'p':>4}{'n':>4}{'slope':>10}{'r²':>8}"
      f"{'slope·(2ℓ+1)':>15}{'slope·√p':>11}")
S=[]
for k in sorted(BY):
    v=sorted(BY[k])
    if len(v)<4: continue
    q=np.array([x[0] for x in v],float); a=np.array([x[2] for x in v])
    r=SS.linregress(q,a); gp=k[0]-k[1]-1
    print(f"      {f'{k[0]}{L[k[1]]}':>7}{k[1]:>3}{gp:>4}{k[0]:>4}{r.slope:>10.4f}"
          f"{r.rvalue**2:>8.4f}{r.slope*(2*k[1]+1):>15.4f}{r.slope*math.sqrt(gp):>11.4f}")
    S.append((k[0],k[1],gp,r.slope))
print()
v1=[s*(2*l+1) for n,l,p,s in S]; v2=[s*math.sqrt(p) for n,l,p,s in S]
print(f"      slope·(2ℓ+1) : median {st.median(v1):.4f}  sd {st.pstdev(v1):.4f}")
print(f"      slope·√p     : median {st.median(v2):.4f}  sd {st.pstdev(v2):.4f}")
print()
print("  THE FORM  ν = n − a√p − b·q/(2ℓ+1)·√p   —  fitted on all data\n")
NN=np.array([d[1] for d in D],float); GL=np.array([d[2] for d in D],float)
GP=np.array([d[3] for d in D],float); Q=np.array([d[4] for d in D],float)
NU=np.array([d[5] for d in D])
y=NN-NU
for nm,X in (("a√p only",[np.sqrt(GP)]),
             ("a√p + b·q√p",[np.sqrt(GP),Q*np.sqrt(GP)]),
             ("a√p + b·q√p/(2ℓ+1)",[np.sqrt(GP),Q*np.sqrt(GP)/(2*GL+1)]),
             ("a√p + b·q/(2ℓ+1)",[np.sqrt(GP),Q/(2*GL+1)]),
             ("a√p + b·q",[np.sqrt(GP),Q])):
    M=np.column_stack(X)
    b,*_=np.linalg.lstsq(M,y,rcond=None); r=y-M@b
    print(f"      {nm:<26}r² {1-np.var(r)/np.var(y):>7.4f}"
          f"   rms {float(np.sqrt(np.mean(r**2))):.4f}   coefs "
          + " ".join(f"{x:+.4f}" for x in b))
