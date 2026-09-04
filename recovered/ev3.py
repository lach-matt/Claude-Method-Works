import numpy as np, eldata as ed
from scipy import stats
CAP=lambda l: 2*(2*l+1)
zs=sorted(ed.E)
def V(c,g,e,tol=None):
    ok=(abs(g-e)<=tol) if tol is not None else (g==e)
    gs=f"{g:.4f}" if isinstance(g,float) else str(g)
    print(f"  {c:<52}{gs:>12}  exp {str(e):>9}  {'OK' if ok else '*** FAIL ***'}")

print("="*82); print("EVIDENCE AUDIT H — PART V NUMBERS"); print("="*82)
# exchange labelling
def ep(l,k):
    orb=2*l+1; up=min(k,orb); dn=max(0,k-orb); return up*(up-1)//2+dn*(dn-1)//2
ANOM={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
rows=[]
for z in zs:
    n,l,k=ed.E[z]
    if l<2 or k>=CAP(l): continue
    rows.append((z, ep(l,k+1)-ep(l,k), z in ANOM))
ga=[r[1] for r in rows if r[2]]; gn=[r[1] for r in rows if not r[2]]
u,pu=stats.mannwhitneyu(ga,gn,alternative='two-sided')
auc=u/(len(ga)*len(gn))
V("exchange-gain AUC",auc,0.589,0.02)
V("exchange-gain p (Mann-Whitney)",pu,0.23,0.06)
# half/one-below-full rule precision & recall
hits=[z for z in zs if ed.E[z][1]>=2 and (ed.E[z][2]==2*ed.E[z][1]+1 or ed.E[z][2]==CAP(ed.E[z][1])-1)]
tp=len([z for z in hits if z in ANOM]); fp=len(hits)-tp
fn=len([z for z in ANOM if z not in hits])
V("half/one-below-full precision",tp/(tp+fp) if tp+fp else 0,0.42,0.08)
V("half/one-below-full recall",tp/(tp+fn) if tp+fn else 0,0.26,0.08)
# ionisation
IE={1:13.598,2:24.587,3:5.392,4:9.323,5:8.298,6:11.260,7:14.534,8:13.618,9:17.423,
10:21.565,11:5.139,12:7.646,13:5.986,14:8.152,15:10.487,16:10.360,17:12.968,18:15.760,
19:4.341,20:6.113,21:6.561,22:6.828,23:6.746,24:6.767,25:7.434,26:7.902,27:7.881,
28:7.640,29:7.726,30:9.394,31:5.999,32:7.900,33:9.815,34:9.752,35:11.814,36:14.000,
37:4.177,38:5.695,39:6.217,40:6.634,41:6.759,42:7.092,44:7.361,45:7.459,46:8.337,
47:7.576,48:8.994,49:5.786,50:7.344,51:8.608,52:9.010,53:10.451,54:12.130,55:3.894,
56:5.212,57:5.577,72:6.825,73:7.550,74:7.864,75:7.834,76:8.438,77:8.967,78:8.959,
79:9.226,80:10.438,81:6.108,82:7.417,83:7.286,84:8.414,86:10.749}
ZI=sorted(IE); Y=np.array([IE[z] for z in ZI])
n_=np.array([ed.E[z][0] for z in ZI],float); l_=np.array([ed.E[z][1] for z in ZI],float)
k_=np.array([ed.E[z][2] for z in ZI],float)
def loo(cols,Yv):
    X=np.column_stack([np.ones(len(Yv))]+cols); pr=np.zeros(len(Yv))
    for i in range(len(Yv)):
        m=np.ones(len(Yv),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Yv[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((Yv-pr)**2)/np.sum((Yv-np.mean(Yv))**2)
V("ionisation: lattice coords alone",loo([n_,l_,k_],Y),0.19,0.06)
V("ionisation: with 1/n² imported",loo([1/n_**2,l_,k_/(2*(2*l_+1))],Y),0.42,0.06)
EN={1:2.20,3:0.98,4:1.57,5:2.04,6:2.55,7:3.04,8:3.44,9:3.98,11:0.93,12:1.31,13:1.61,
14:1.90,15:2.19,16:2.58,17:3.16,19:0.82,20:1.00,21:1.36,22:1.54,23:1.63,24:1.66,
25:1.55,26:1.83,27:1.88,28:1.91,29:1.90,30:1.65,31:1.81,32:2.01,33:2.18,34:2.55,
35:2.96,37:0.82,38:0.95,39:1.22,40:1.33,41:1.60,42:2.16,44:2.20,45:2.28,46:2.20,
47:1.93,48:1.69,49:1.78,50:1.96,51:2.05,52:2.10,53:2.66,55:0.79,56:0.89,57:1.10,
72:1.30,73:1.50,74:2.36,75:1.90,76:2.20,77:2.20,78:2.28,79:2.54,80:2.00,81:1.62,
82:2.33,83:2.02,84:2.00}
ZE=sorted(EN); Y2=np.array([EN[z] for z in ZE])
n2=np.array([ed.E[z][0] for z in ZE],float); l2=np.array([ed.E[z][1] for z in ZE],float)
k2=np.array([ed.E[z][2] for z in ZE],float)
V("electronegativity: lattice coords",loo([n2,l2,k2],Y2),0.12,0.06)

print()
print("="*82); print("EVIDENCE AUDIT I — MENDELEEV RETRODICTION"); print("="*82)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))
K1869={1,3,4,5,6,7,8,9,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,33,34,
35,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,62,63,64,65,66,67,
68,73,74,75,76,77,78,79,80,81,82,83,90,92}
o=set(ed.E[z] for z in K1869 if z in ed.E)
cells=set()
for x in o:
    for y in L:
        if leq(y,x) and y not in o: cells.add(y)
flag=sorted({z for z in ed.E if ed.E[z] in cells and z not in K1869})
V("cells flagged by the ideal test",len(cells),13)
print(f"      elements later found there: {[ed.SYM[z] for z in flag]}")
V("Mendeleev's three among them",len([z for z in flag if z in (21,31,32)]),3)

print()
print("="*82); print("EVIDENCE AUDIT J — ASSERTIONS WITH NO EMPIRICAL BACKING"); print("="*82)
print("""  Scanning the paper for claims that are neither proved, computed, nor cited:

  1. §3  'reactive cells represent transient overflow states in which an
         excess electron is promoted to a new shell'
         → INTERPRETATION ONLY. No computation, no citation, no test.
         The cells are well-defined (k > 2(2ℓ+1)); the physical reading is
         asserted. Should be marked as a proposed reading, not a finding.

  2. §12.2 the chemistry of kainosymmetry — compactness, absent same-ℓ
         screening, first-short-period irregularities
         → LITERATURE CLAIM, currently uncited in the paper.
         Needs a citation (Pyykkö or Kaupp).

  3. §15  '5g occupancy is predicted to begin near Z ≈ 121'
         → LITERATURE CLAIM, Pyykkö 2011 is in the reference list but is
         not cited at this sentence.

  4. §5  'σ²(t) measures the instantaneous spread'
         → DEFINITIONAL, follows from Equation (6). Adequate.

  5. §18.2 the description of Villars' Periodic Number as 'emphasising
         valence-electron count with rows corresponding to n'
         → LITERATURE CLAIM, citation present in reference list.""")