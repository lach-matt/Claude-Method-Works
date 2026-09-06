import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])

# Rounding to granularity q gives each value an error of sd q/sqrt(12).
# A second difference D = y_{i+1} - 2y_i + y_{i-1} combines them with weights (1,-2,1),
# so var(D_round) = (1+4+1) q^2/12 = q^2/2  ->  sd(D_round) = q/sqrt(2).
# Resolution ratio  kappa = mean|D_measured| / (q/sqrt(2)).
def kappa(y,q):
    y=np.asarray(y,float)
    if len(y)<3: return np.nan,0
    D=y[2:]-2*y[1:-1]+y[:-2]
    return np.mean(np.abs(D))/(q/np.sqrt(2)), len(D)
def report(name,y,q):
    y=np.asarray(y,float); i=np.arange(len(y))
    kp,np_=kappa(y,q); ke,ne=kappa(y[i%2==0],q); ko,no=kappa(y[i%2==1],q)
    worst=np.nanmin([kp,ke,ko])
    ok = worst>=5 and min(ne,no)>=2
    print(f"{name:40}{kp:11.1f}{ke:10.1f}{ko:9.1f}{worst:11.1f}   {'admit' if ok else 'REJECT'}")
    return worst

print(f"{'sequence':40}{'k pooled':>11}{'k even':>10}{'k odd':>9}{'worst':>11}   verdict")
C=np.arange(4,15)
report("n-alkane melting points (q=0.1 K)",[134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0],0.1)
report("n-alkane boiling points (q=0.1 K)",[272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7],0.1)
report("n-alkane dHvap (q=0.1 kJ/mol)",[26.4,31.6,36.6,41.5,46.6,51.4,56.6,61.5],0.1)
for el in ['Ca','Ni','Se','Kr']:
    Z,rows=CH[el]; A=np.array([r[0] for r in rows],float)
    B=np.array([r[0]*r[1] for r in rows])            # keV; B/A quoted to 1e-4 keV
    q=float(np.mean(A))*1e-4
    report(f"{el} binding energy (q={q:.4f} keV)",B,q)
# Ba I levels are quoted to 1e-3 cm-1; use the paper's 6s-nf series spacing scale
report("Ba I 6s-nf, model 1/n^2 (q=0.001 cm-1)",1e5/np.arange(5,20.)**2,0.001)

print("\ndHvap detail — why it fails:")
y=np.array([26.4,31.6,36.6,41.5,46.6,51.4,56.6,61.5]); i=np.arange(len(y))
for lbl,z in [("pooled",y),("even",y[i%2==0]),("odd",y[i%2==1])]:
    D=z[2:]-2*z[1:-1]+z[:-2]
    print(f"   {lbl:7} second differences {np.round(D,3)}  mean|D| = {np.mean(np.abs(D)):.3f} kJ/mol vs rounding sd {0.1/np.sqrt(2):.3f}")