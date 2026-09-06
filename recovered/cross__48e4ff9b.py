import numpy as np, eldata as ed
from scipy import stats
zs=sorted(ed.E)
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,
44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,
67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,
1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,
19:10,20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,
52:92,53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=[z for z in zs if z in MN]
mn=np.array([MN[z] for z in com],float)
n=np.array([ed.E[z][0] for z in com],float)
l=np.array([ed.E[z][1] for z in com],float)
k=np.array([ed.E[z][2] for z in com],float)
Z=np.array(com,float)
def loo(cols,y=mn):
    X=np.column_stack([np.ones(len(y))]+cols); pr=np.zeros(len(y))
    for i in range(len(y)):
        m=np.ones(len(y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],y[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((y-pr)**2)/np.sum((y-np.mean(y))**2)
print("="*80); print("VERIFYING THE NONLINEAR MN RESULT — is it overfitting?"); print("="*80)
sets=[('Λ linear (n,ℓ,k)',[n,l,k]),
      ('+ ℓ²',[n,l,k,l*l]),('+ k²',[n,l,k,k*k]),('+ ℓ²,k²',[n,l,k,l*l,k*k]),
      ('+ ℓ²,k²,ℓk',[n,l,k,l*l,k*k,l*k]),
      ('Z quadratic',[Z,Z*Z]),('Z with 5 poly terms',[Z,Z*Z,Z**3,Z**4,Z**5])]
print(f"  {'model':<26}{'params':>8}{'fit R²':>9}{'LOO R²':>9}{'overfit':>9}")
print("  "+"-"*61)
for nm,c in sets:
    X=np.column_stack([np.ones(len(mn))]+c)
    b,*_=np.linalg.lstsq(X,mn,rcond=None); p=X@b
    fit=1-np.sum((mn-p)**2)/np.sum((mn-np.mean(mn))**2)
    L=loo(c)
    print(f"  {nm:<26}{len(c):>8}{fit:>9.3f}{L:>9.3f}{fit-L:>9.3f}")
# permutation test on the l^2,k^2 gain
rng=np.random.default_rng(5)
base=loo([n,l,k]); obs=loo([n,l,k,l*l,k*k])-base
null=[]
for _ in range(2000):
    p1=rng.permutation(l*l); p2=rng.permutation(k*k)
    null.append(loo([n,l,k,p1,p2])-base)
null=np.array(null)
print(f"\n  permutation test on the (ℓ²,k²) gain, 2000 shuffles:")
print(f"    observed gain {obs:+.3f}, null mean {null.mean():+.3f}, 95th pct {np.percentile(null,95):+.3f}")
print(f"    p = {(null>=obs).mean():.4f}")

print()
print("="*80); print("WHY QUADRATIC? — THE SHAPE OF MN"); print("="*80)
print("""  Pettifor's scale runs UP one group then jumps: it snakes through the
  table. A snake is not a linear function of position — it is piecewise
  and turns. Quadratic terms in ℓ and k supply the turning.""")
# show MN vs k within each l block
for lv in [0,1,2,3]:
    sel=[(int(k[i]),mn[i]) for i in range(len(com)) if l[i]==lv]
    sel.sort()
    if len(sel)>3:
        ks=[s[0] for s in sel]; ms=[s[1] for s in sel]
        r,_=stats.pearsonr(ks,ms)
        print(f"    ℓ={lv}: MN vs k within block, r = {r:+.3f}  (n={len(sel)})")

print()
print("="*80); print("CROSS-SYSTEM: WHAT DOES EACH SYSTEM MEASURE?"); print("="*80)
rows=[("Quantum (Madelung)","n+ℓ then n","spectroscopy","ORDINAL","0.90 vs Z"),
      ("Quantum (Janet)","blocks of n+ℓ","spectroscopy","PARTITION","— "),
      ("Structural (Pettifor)","empirical snake","ICSD structures","ORDINAL","−0.23 vs Z"),
      ("Structural (Villars PN)","rows = n","compound formation","ORDINAL","—"),
      ("Integral (Z)","nuclear charge","Moseley X-ray","ORDINAL","1.00"),
      ("Integral (A)","nucleon count","mass spec","ORDINAL","0.997 vs Z"),
      ("Lach Λ","(n,ℓ,k) triple","none — definitional","PARTIAL ORDER","0.50 (rank)")]
print(f"  {'system':<24}{'sort key':<20}{'measured by':<22}{'type':<15}")
print("  "+"-"*78)
for a,b,c,d,e in rows:
    print(f"  {a:<24}{b:<20}{c:<22}{d:<15}")
print("""
  THE STRUCTURAL DIFFERENCE: every other system produces a TOTAL ORDER
  (a sequence, 1..118). Λ produces a PARTIAL ORDER. That is the single
  largest discrepancy between Λ and all prior sorting schemes, and it
  is why order dimension, ideals and antichains are available for Λ
  and undefined for the others — a total order has dimension 1.""")