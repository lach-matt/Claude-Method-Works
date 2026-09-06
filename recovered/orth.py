import numpy as np, eldata as ed
from scipy import stats
exec(open('bench.py').read().split("ZS=[")[0])

ZS=[z for z in sorted(dHf) if z in MN and z in MIE]
Y=np.array([dHf[z] for z in ZS],float)
lv=np.array([ed.E[z][1] for z in ZS],float); kv=np.array([ed.E[z][2] for z in ZS],float)
mn=np.array([MN[z] for z in ZS],float)
phi=np.array([MIE[z][0] for z in ZS]); nws=np.array([MIE[z][1] for z in ZS])

def loo(cols):
    X=np.column_stack([np.ones(len(Y))]+cols); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2), (Y-pr)**2

print("Does k add to each established scheme? (LOO R2, and permutation p)")
print("-"*64)
rng=np.random.default_rng(3)
for nm, base in [('Pettifor MN',[mn]),('Pettifor MN+MN^2',[mn,mn**2]),
                 ('Miedema phi+nws',[phi,nws]),
                 ('Miedema full',[phi,nws,(phi-2.1)**2,(nws-1.5)**2])]:
    r0,_=loo(base); r1,_=loo(base+[kv])
    # permutation null on k
    null=[]
    for _ in range(2000):
        kk=rng.permutation(kv); rn,_=loo(base+[kk]); null.append(rn-r0)
    null=np.array(null); obs=r1-r0
    p=(null>=obs).mean()
    flag='  <<<' if p<0.05 and obs>0 else ''
    print(f"  {nm:<20} {r0:.3f} -> {r1:.3f}  ({obs:+.3f})  perm p={p:.3f}{flag}")