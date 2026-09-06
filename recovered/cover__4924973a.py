import numpy as np
aV,aS,aC,aA,aP=15.75,17.8,0.711,23.7,12.0
def B(Z,N):
    A=Z+N
    b=aV*A-aS*A**(2/3)-aC*Z*(Z-1)/A**(1/3)-aA*(A-2*Z)**2/A
    d=aP/np.sqrt(A) if (Z%2==0 and N%2==0) else (-aP/np.sqrt(A) if (Z%2==1 and N%2==1) else 0.0)
    return b+d

# simulate an "experimental frontier": measured if N <= Nmax(Z), a ragged boundary
rng=np.random.default_rng(0)
Zr=range(20,45)
Nmax={Z: int(1.35*Z+4+rng.integers(-3,4)) for Z in Zr}
meas={(Z,N) for Z in Zr for N in range(Z-4, Nmax[Z]+1) if 40<=Z+N<=130}
allc={(Z,N) for Z in Zr for N in range(Z-4, Nmax[Z]+9) if 40<=Z+N<=130}
unk=allc-meas
def interior(c,axis):
    Z,N=c
    if axis=='N': return (Z,N-1) in meas and (Z,N+1) in meas
    return (Z-1,N) in meas and (Z+1,N) in meas
nN=sum(interior(c,'N') for c in unk)
nZ=sum(interior(c,'Z') for c in unk)
nB=sum(interior(c,'N') and interior(c,'Z') for c in unk)
nE=sum(interior(c,'N') or interior(c,'Z') for c in unk)
print(f"unmeasured cells adjacent to the frontier: {len(unk)}")
print(f"  bracketable on N only          : {nN}")
print(f"  bracketable on Z only          : {nZ}")
print(f"  bracketable on both            : {nB}")
print(f"  bracketable on EITHER (2-axis) : {nE}   -> coverage gain {nE/max(nN,1):.2f}x over N alone")
ok=0;tot=0
for c in unk:
    Z,N=c; y=B(Z,N); lo=-1e9; hi=1e9
    if interior(c,'N'): lo=max(lo,B(Z,N-1)); hi=min(hi,B(Z,N+1))
    if interior(c,'Z'): lo=max(lo,B(Z-1,N)); hi=min(hi,B(Z+1,N))
    if lo>-1e8:
        tot+=1; ok+= (lo<=y<=hi)
print(f"  containment of the 2-axis bracket on those cells: {ok}/{tot}")