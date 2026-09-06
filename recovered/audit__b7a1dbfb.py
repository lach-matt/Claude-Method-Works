import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])
rng=np.random.default_rng(7)
def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def Sig(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    return 2*np.nanmean([V(y[i%2==0]),V(y[i%2==1])])/V(y)

def matched_null(y,sig,N=4000,deg=3):
    """single-channel surrogate: smooth fit to the even sub-channel, evaluated on the full
       grid (so curvature and step scale match), then this sequence's own noise added."""
    y=np.asarray(y,float); x=np.arange(len(y)); m=x%2==0
    c=np.polyfit(x[m],y[m],min(deg,m.sum()-1)); base=np.polyval(c,x)
    out=[]
    for _ in range(N):
        z=base+rng.normal(0,sig,len(x))
        if np.all(np.diff(z)>0): out.append(Sig(z))
    return np.array(out)

def boot_V(y,sig,N=4000):
    y=np.asarray(y,float)
    return np.array([V(y+rng.normal(0,sig,len(y))) for _ in range(N)])

CASES=[]
C=np.arange(4,15)
CASES.append(("n-alkane melting pts C4-C14",np.array([134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0]),0.3))
CASES.append(("n-alkane boiling pts C4-C14",np.array([272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7]),0.3))
CASES.append(("Ba I 6snf 3F2 n=17-25",np.array([41647.85,41689.80,41725.39,41755.48,41782.02,41804.59,41824.30,41841.63,41856.85]),0.1))
for el in ['Ca','Ti','Cr','Fe','Ni','Zn','Ge','Se','Kr']:
    Z,rows=CH[el]; B=np.array([r[0]*r[1] for r in rows]); sB=np.array([r[0]*r[2] for r in rows])
    CASES.append((f"{el} binding energy",B,float(np.median(sB))))

print(f"{'sequence':30}{'V':>8}{'V 90% CI':>18}{'Sigma':>8}{'null 99%':>10}{'null max':>10}  verdict")
for nm,y,sig in CASES:
    bv=boot_V(y,sig); nl=matched_null(y,sig); S=Sig(y)
    lo,hi=np.percentile(bv,[5,95])
    v = "SUPERPOSED" if S>np.percentile(nl,99.9) else ("marginal" if S>np.percentile(nl,99) else "single channel")
    print(f"{nm:30}{V(y):>8.1f}  [{lo:>6.1f},{hi:>6.1f}]  {S:>8.2f}{np.percentile(nl,99):>10.2f}{nl.max():>10.2f}  {v}")

print("\n=== sensitivity of the alkane rows to the assumed sigma ===")
for sig in [0.1,0.3,1.0,3.0]:
    mp=np.array([134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0])
    nl=matched_null(mp,sig); print(f"  melting pts, sigma={sig:4.1f} K : Sigma=12.69 vs null 99% {np.percentile(nl,99):5.2f}, max {nl.max():5.2f}")

print("\n=== Ba I: sensitivity to block choice ===")
full={17:41647.85,18:41689.80,19:41725.39,20:41755.48,21:41782.02,22:41804.59,23:41824.30,24:41841.63,25:41856.85}
for a,b in [(17,25),(17,23),(19,25),(18,24),(17,21),(21,25)]:
    y=np.array([full[n] for n in range(a,b+1)])
    print(f"  n={a}-{b} ({b-a+1} members): V={V(y):6.2f}  Sigma={Sig(y):5.2f}")

print("\n=== basis of the r >= 5 admission threshold ===")
def cont(r,N=400000):
    lo=-r+rng.normal(0,1,N); hi=r+rng.normal(0,1,N)
    return np.mean((np.minimum(lo,hi)<=0)&(0<=np.maximum(lo,hi)))
for r in [1,2,3,4,5,6,8]:
    print(f"  r={r}: containment {100*cont(r):6.2f}%   shortfall from 100%: {100*(1-cont(r)):5.2f} pp")