"""sox_mc.py -- s32 gate G-S3: brute Monte Carlo of the 9-D second-order exchange, bare and screened, k_F units.
E/N = (3/(16 pi^5)) INT d^3q INT_L d^3k1 INT_L d^3k2  W(q) / (q^2 |q+k1+k2|^2 (q^2 + q.(k1+k2)))  [Ry],  L = {k<1,|k+q|>1}.
Proposal: q ~ Gamma(3,1) radial (p(q)=q^2 e^-q/2) isotropic; k1,k2 uniform in the unit ball (rejected if |k+q|<=1, weight 0).
Screened at (rs,zeta): per spin sigma, k_F,sigma = s k_F: q = s q~; weight s^3/2, W = S(Pi(s q~;rs,zeta)) with sox_table.S, sox_table.Pi.
usage: python3 sox_mc.py NSAMP SEED  -> prints bare and screened(2,0),(2,1) with 1-sigma errors, and the reduced values for comparison."""
import numpy as np, sys, sox_table as T
N=int(sys.argv[1]); rng=np.random.default_rng(int(sys.argv[2])); PRE=3/(16*np.pi**5); CH=500000
def ball(n):
    v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]; r=rng.random(n)**(1/3); return v*r[:,None]
acc={k:[] for k in ("bare","s20","s21")}
for start in range(0,N,CH):
    n=min(CH,N-start)
    q=rng.gamma(3.0,1.0,n); d=rng.normal(size=(n,3)); d/=np.linalg.norm(d,axis=1)[:,None]; qv=d*q[:,None]
    pq=q*q*np.exp(-q)/2.0/(4*np.pi*q*q)          # density of the vector q: radial p(q)/(4 pi q^2)
    k1=ball(n); k2=ball(n); VB=(4*np.pi/3)**2
    ok=(np.linalg.norm(k1+qv,axis=1)>1)&(np.linalg.norm(k2+qv,axis=1)>1)
    P=k1+k2; den=q*q*np.sum((qv+P)**2,axis=1)*(q*q+np.sum(qv*P,axis=1))
    f=np.where(ok,1.0/den,0.0)*VB/pq*PRE
    acc["bare"].append(f)
    for key,z in (("s20",0.0),("s21",1.0)):
        xp,xm=T.R.xs(z); w=np.zeros(n)
        for s in (xp,xm):
            if s<=0: continue
            w+=(s**3/2)*T.S(T.Pi(s*q,2.0,z))
        acc[key].append(f*w)
for key in acc:
    a=np.concatenate(acc[key]); m=a.mean()/2; e=a.std()/np.sqrt(len(a))/2      # Ry -> Ha
    red={"bare":T.eps2x(2.0,0.0,screen=False),"s20":T.eps2x(2.0,0.0),"s21":T.eps2x(2.0,1.0)}[key]
    print(f"{key}: MC {m:.6f} +- {e:.6f} Ha   reduced {red:.6f}   z-score {(red-m)/e:+.2f}")