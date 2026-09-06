import numpy as np
from scipy.stats import spearmanr
rng=np.random.default_rng(7)
def V_seq(y):
    y=np.asarray(y,float); w=np.abs(y[:-2]-y[2:]); e=np.abs(y[1:-1]-0.5*(y[:-2]+y[2:]))
    e=np.where(e<1e-15,1e-15,e); return w.sum()/e.sum()
def Sigma(y):
    Vp=V_seq(y); s=[V_seq(y[k::2]) for k in (0,1) if len(y[k::2])>=3]
    return 2*np.mean(s)/Vp
def D3(y):   # nuclear three-point staggering, mean |Delta3|
    d=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return d.mean()/ (np.abs(np.diff(y)).mean()+1e-12)
def ACF2(y):
    r=y-np.polyval(np.polyfit(np.arange(len(y)),y,3),np.arange(len(y)))
    r=r-r.mean(); 
    return -np.sum(r[2:]*r[:-2])/(np.sum(r*r)+1e-12)
def LS(y):   # power at f=0.5 after cubic detrend
    n=len(y); r=y-np.polyval(np.polyfit(np.arange(n),y,3),np.arange(n))
    return abs(np.sum(r*(-1)**np.arange(n)))/ (np.sqrt(np.sum(r*r))+1e-12)

def make(N,amp,snr,shape='rydberg'):
    n=np.arange(N)+8.0
    y = -1.0/n**2 if shape=='rydberg' else np.log(n)
    y=(y-y.min())/(y.max()-y.min())
    step=np.median(np.abs(np.diff(y)))
    y=y+amp*step*((-1)**np.arange(N))
    return y+rng.normal(0,step/snr,N)

stats={'Sigma':Sigma,'Delta3':D3,'ACF(2)':ACF2,'LombScargle f=.5':LS}
print("detection power at a 1% false-positive rate (null = single smooth channel)")
print("alternation amplitude = 0.5 x median step;  r = step/sigma = 20\n")
print(f"{'N':>4} " + " ".join(f"{k:>17}" for k in stats))
for N in [11,15,23,36,60]:
    line=f"{N:>4} "
    for k,f in stats.items():
        null=np.array([f(make(N,0.0,20)) for _ in range(3000)])
        thr=np.percentile(null,99)
        alt=np.array([f(make(N,0.5,20)) for _ in range(3000)])
        line+=f" {np.mean(alt>thr):16.1%}"
    print(line)
print("\nsame at r = 5 (the admission threshold)")
print(f"{'N':>4} " + " ".join(f"{k:>17}" for k in stats))
for N in [11,23,36]:
    line=f"{N:>4} "
    for k,f in stats.items():
        null=np.array([f(make(N,0.0,5)) for _ in range(3000)])
        thr=np.percentile(null,99)
        alt=np.array([f(make(N,0.5,5)) for _ in range(3000)])
        line+=f" {np.mean(alt>thr):16.1%}"
    print(line)