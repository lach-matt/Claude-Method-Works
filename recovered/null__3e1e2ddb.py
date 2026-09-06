import numpy as np
rng=np.random.default_rng(2024)
def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def Sig(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    a,b=V(y[i%2==0]),V(y[i%2==1]); return 2*np.nanmean([a,b])/V(y)

print("=== NULL DISTRIBUTION OF Sigma for a genuinely single channel ===")
print("smooth monotone y(x) + Gaussian noise, no interleaving. n = 11 members.\n")
shapes={'Rydberg 1/n^2':lambda x:-1e5/(x+16.)**2,'exponential':lambda x:np.exp(0.25*x),
        'linear+curv':lambda x:5*x-0.15*x**2,'power 3/2':lambda x:(x+4)**1.5}
print(f"{'shape':16}{'noise/step':>12}{'median':>9}{'90%':>8}{'95%':>8}{'99%':>8}{'max':>9}")
allS=[]
for nm,f in shapes.items():
    for frac in [0.0,0.02,0.05,0.10]:
        x=np.arange(11.); y0=f(x); step=np.mean(np.abs(np.diff(y0)))
        S=[]
        for _ in range(4000):
            y=y0+rng.normal(0,frac*step,len(x))
            if np.all(np.diff(y)>0): S.append(Sig(y))
        S=np.array(S); allS.append(S)
        print(f"{nm:16}{frac:>12.2f}{np.median(S):>9.2f}{np.percentile(S,90):>8.2f}{np.percentile(S,95):>8.2f}{np.percentile(S,99):>8.2f}{S.max():>9.2f}")
pooled=np.concatenate(allS)
print(f"\npooled null (n={len(pooled)}): median {np.median(pooled):.2f}, 95% {np.percentile(pooled,95):.2f}, "
      f"99% {np.percentile(pooled,99):.2f}, 99.9% {np.percentile(pooled,99.9):.2f}, max {pooled.max():.2f}")

print("\n=== POWER: Sigma when a period-2 alternation of amplitude A is present ===")
print("steps alternate S(1+A), S(1-A) on a smooth trend, 5% noise")
print(f"{'A':>6}{'V pooled':>11}{'median Sigma':>14}{'5th pct':>10}  detect at 2.0?")
for A in [0.0,0.05,0.1,0.2,0.3,0.5]:
    S=[]; Vp=[]
    for _ in range(2000):
        d=np.array([5*(1+A*(-1)**k) for k in range(10)])*(1-0.03*np.arange(10))
        y=np.concatenate([[0],np.cumsum(d)]); y=y+rng.normal(0,0.05*5,len(y))
        if np.all(np.diff(y)>0): S.append(Sig(y)); Vp.append(V(y))
    S=np.array(S)
    print(f"{A:>6.2f}{np.mean(Vp):>11.1f}{np.median(S):>14.2f}{np.percentile(S,5):>10.2f}   {np.mean(S>2)*100:5.1f}%")