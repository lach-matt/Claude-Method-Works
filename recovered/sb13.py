import numpy as np, eldata as ed
from collections import Counter
from scipy import stats

zs=sorted(ed.E)
print("="*72); print("AD.  DOES THE LATTICE PREDICT ANYTHING ABOUT IONISATION ENERGY?"); print("="*72)
# first ionisation energies, eV (CRC), main-group + TM subset
IE={1:13.598,2:24.587,3:5.392,4:9.323,5:8.298,6:11.260,7:14.534,8:13.618,9:17.423,10:21.565,
11:5.139,12:7.646,13:5.986,14:8.152,15:10.487,16:10.360,17:12.968,18:15.760,
19:4.341,20:6.113,21:6.561,22:6.828,23:6.746,24:6.767,25:7.434,26:7.902,27:7.881,
28:7.640,29:7.726,30:9.394,31:5.999,32:7.900,33:9.815,34:9.752,35:11.814,36:14.000,
37:4.177,38:5.695,39:6.217,40:6.634,41:6.759,42:7.092,44:7.361,45:7.459,46:8.337,
47:7.576,48:8.994,49:5.786,50:7.344,51:8.608,52:9.010,53:10.451,54:12.130,
55:3.894,56:5.212,57:5.577,72:6.825,73:7.550,74:7.864,75:7.834,76:8.438,77:8.967,
78:8.959,79:9.226,80:10.438,81:6.108,82:7.417,83:7.286,84:8.414,86:10.749}
Y=np.array([IE[z] for z in sorted(IE)])
ZS=sorted(IE)
F={'n':np.array([ed.E[z][0] for z in ZS],float),
   'l':np.array([ed.E[z][1] for z in ZS],float),
   'k':np.array([ed.E[z][2] for z in ZS],float),
   'k/kmax':np.array([ed.E[z][2]/(2*(2*ed.E[z][1]+1)) for z in ZS]),
   'Z':np.array(ZS,float)}
def loo(cols):
    X=np.column_stack([np.ones(len(Y))]+[F[c] for c in cols]); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2)
print(f"  n = {len(ZS)} elements")
for c in [['Z'],['n'],['l'],['k'],['n','k'],['n','l','k'],['n','k/kmax'],['n','l','k/kmax']]:
    print(f"    {'+'.join(c):<16} LOO R2 = {loo(c):+.3f}")
print("  -> 1/n^2 is the hydrogenic expectation; test that explicitly:")
F['inv_n2']=1/F['n']**2
for c in [['inv_n2'],['inv_n2','k/kmax'],['inv_n2','l','k/kmax']]:
    print(f"    {'+'.join(c):<16} LOO R2 = {loo(c):+.3f}")

print()
print("="*72); print("AE.  ELECTRONEGATIVITY"); print("="*72)
EN={1:2.20,3:0.98,4:1.57,5:2.04,6:2.55,7:3.04,8:3.44,9:3.98,11:0.93,12:1.31,13:1.61,
14:1.90,15:2.19,16:2.58,17:3.16,19:0.82,20:1.00,21:1.36,22:1.54,23:1.63,24:1.66,
25:1.55,26:1.83,27:1.88,28:1.91,29:1.90,30:1.65,31:1.81,32:2.01,33:2.18,34:2.55,
35:2.96,37:0.82,38:0.95,39:1.22,40:1.33,41:1.60,42:2.16,44:2.20,45:2.28,46:2.20,
47:1.93,48:1.69,49:1.78,50:1.96,51:2.05,52:2.10,53:2.66,55:0.79,56:0.89,57:1.10,
72:1.30,73:1.50,74:2.36,75:1.90,76:2.20,77:2.20,78:2.28,79:2.54,80:2.00,81:1.62,
82:2.33,83:2.02,84:2.00}
Y=np.array([EN[z] for z in sorted(EN)]); ZS=sorted(EN)
F={'n':np.array([ed.E[z][0] for z in ZS],float),
   'l':np.array([ed.E[z][1] for z in ZS],float),
   'k':np.array([ed.E[z][2] for z in ZS],float),
   'k/kmax':np.array([ed.E[z][2]/(2*(2*ed.E[z][1]+1)) for z in ZS]),
   'Z':np.array(ZS,float)}
F['inv_n2']=1/F['n']**2
print(f"  n = {len(ZS)} elements")
for c in [['Z'],['n'],['n','k'],['n','l','k'],['inv_n2','k/kmax'],['n','l','k/kmax']]:
    print(f"    {'+'.join(c):<16} LOO R2 = {loo(c):+.3f}")