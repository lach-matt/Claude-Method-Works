import numpy as np
aV,aS,aC,aA,aP = 15.75,17.8,0.711,23.7,12.0
def B(Z,N):
    A=Z+N
    b=aV*A-aS*A**(2/3)-aC*Z*(Z-1)/A**(1/3)-aA*(A-2*Z)**2/A
    d=np.where((Z%2==0)&(N%2==0), aP/np.sqrt(A), np.where((Z%2==1)&(N%2==1), -aP/np.sqrt(A),0.0))
    return b+d

def V_seq(y):
    y=np.asarray(y,float)
    w=np.abs(y[:-2]-y[2:]); e=np.abs(y[1:-1]-0.5*(y[:-2]+y[2:]))
    return w.sum()/e.sum(), w.mean()

def sigma(y):
    Vp,_=V_seq(y); Vs=[];
    for k in [0,1]:
        s=y[k::2]
        if len(s)>=3: Vs.append(V_seq(s)[0])
    return 2*np.mean(Vs)/Vp, Vp, np.mean(Vs)

print("SYNTHETIC (Bethe-Weizsacker) nuclear chart -- structural test only\n")
print(" Z   A-range  cells  V_pooled  V_resolved  Sigma   2S/|dS/dA| pred")
rows=[]
for Z,Amin,Amax in [(20,36,56),(22,40,58),(24,44,64),(26,48,67),(28,52,73),
                    (30,58,82),(32,64,83),(34,67,83),(36,71,83)]:
    A=np.arange(Amin,Amax+1); Nn=A-Z
    y=B(Z,Nn)
    Vp,Vr,_=None,None,None
    S,Vp,Vsub=sigma(y)
    # smooth-trend prediction on a resolved sub-channel (h=2 in A)
    ye=y[0::2]; Ae=A[0::2]
    Sn=np.gradient(ye,Ae)              # dB/dA ~ S_n
    dS=np.gradient(Sn,Ae)
    pred=np.mean(2*np.abs(Sn)/np.abs(dS))
    rows.append((Z,Vp,Vsub,S,pred))
    print(f" {Z:2d}  {Amin:3d}-{Amax:3d}   {len(A)-2:3d}   {Vp:7.2f}   {Vsub:8.2f}  {S:6.2f}   {pred:8.1f}")

Zs=np.array([r[0] for r in rows]); Vres=np.array([r[2] for r in rows]); Vpool=np.array([r[1] for r in rows])
from scipy.stats import spearmanr
print(f"\n Spearman(V_resolved, Z) = {spearmanr(Zs,Vres).correlation:+.3f}   "
      f"Spearman(V_pooled, Z) = {spearmanr(Zs,Vpool).correlation:+.3f}")
print(" (paper measures +1.000 and -0.10 on AME2020)")

# ---------------- multi-axis bracket ----------------
print("\n=== two-axis bracket: intersect the N-bracket and the Z-bracket ===")
gain=[];  ok=0; tot=0; monoZ=0; monoZtot=0
for Z in range(20,40):
    for N in range(Z, Z+30):
        A=Z+N
        if A<40 or A>110: continue
        try:
            yb=B(Z,N)
            # N-axis neighbours
            lo_N,hi_N=B(Z,N-1),B(Z,N+1)
            # Z-axis neighbours
            lo_Z,hi_Z=B(Z-1,N),B(Z+1,N)
        except Exception: continue
        monoZtot+=1
        if lo_Z<yb<hi_Z: monoZ+=1
        if not(lo_N<yb<hi_N and lo_Z<yb<hi_Z): continue
        wN=hi_N-lo_N; wZ=hi_Z-lo_Z
        lo=max(lo_N,lo_Z); hi=min(hi_N,hi_Z)
        if hi<=lo: continue
        tot+=1
        if lo<yb<hi: ok+=1
        gain.append(min(wN,wZ)/(hi-lo))
gain=np.array(gain)
print(f" Z-axis monotonicity holds on {monoZ}/{monoZtot} = {monoZ/monoZtot:.1%} of cells")
print(f" containment of the intersected bracket: {ok}/{tot}")
print(f" width gain over the better single axis: median {np.median(gain):.2f}x, "
      f"mean {gain.mean():.2f}x, 90th pct {np.percentile(gain,90):.2f}x")