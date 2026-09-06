import numpy as np, eldata as ed, itertools
from collections import Counter
from scipy import stats
CAP=lambda l:2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))
OV={24:(3,2,5),29:(3,2,10),41:(4,2,4),42:(4,2,5),44:(4,2,7),45:(4,2,8),46:(4,2,10),
47:(4,2,10),57:(5,2,1),58:(4,3,1),64:(4,3,7),78:(5,2,9),79:(5,2,10),89:(6,2,1),
90:(6,2,2),91:(5,3,2),92:(5,3,3),93:(5,3,4),96:(5,3,7),103:(7,1,1)}
STRICT=dict(ed.E); STRICT.update(OV)
def dcls(c):
    n,l,k=c; return 'B' if l+1<=n-1 else ('C' if l>0 else 'A')
print("="*84); print("SECOND SWEEP — EVERYTHING ELSE THAT USES THE OCCUPIED SET"); print("="*84)
for nm,cfg in [('idealised',ed.E),('strict',STRICT)]:
    occ=set(cfg.values()); zs=sorted(cfg)
    print(f"\n  ── {nm} ──")
    print(f"  §3  reserved cells (|Λ|−|occ|)      : {len(L)-len(occ)}")
    c=Counter(dcls(cfg[z]) for z in zs)
    print(f"  §6  class counts A/B/C              : {c['A']}/{c['B']}/{c['C']}")
    ev=sum(1 for x in occ if sum(x)%2==0)
    print(f"  §10.3 parity of occupied set        : {ev} even / {len(occ)-ev} odd  "
          f"{'balanced' if ev==len(occ)-ev else 'NOT balanced'}")
    print(f"  §17 Pt cell                         : {cfg[78]}    Yb cell: {cfg[70]}")
    mad=[cfg[z][0]+cfg[z][1] for z in zs]
    tau,_=stats.kendalltau(zs,mad)
    print(f"  §18.1 Kendall τ(Z, n+ℓ)             : {tau:.4f}")
    o=sorted(zs,key=lambda z:(cfg[z][0]+cfg[z][1],cfg[z][0],cfg[z][2]))
    mis=sum(1 for i,z in enumerate(o) if z!=zs[i])
    print(f"  §18.1 elements misplaced by Madelung: {mis}")
    mr=[sum(cfg[m]) for m in (2,8,20,28,50,82)]
    ar=[sum(cfg[z]) for z in zs]
    tt,pp=stats.ttest_1samp(mr,np.mean(ar))
    print(f"  §18.3 magic-Z mean rank / all       : {np.mean(mr):.2f} / {np.mean(ar):.2f}  p={pp:.3f}")

print()
print("="*84); print("§20  MN SLOPES BY BLOCK"); print("="*84)
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,44:62,
45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,67:24,68:23,
69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,1:92,3:1,
4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,19:10,
20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,52:92,
53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
for nm,cfg in [('idealised',ed.E),('strict',STRICT)]:
    print(f"  {nm}:", end=' ')
    out=[]
    for lv in (1,2,3):
        pts=sorted((cfg[z][2],MN[z]) for z in MN if z in cfg and cfg[z][1]==lv)
        s,i,r,p,se=stats.linregress([a for a,b in pts],[b for a,b in pts])
        out.append(f"ℓ={lv}: {s:+.2f}")
    print("   ".join(out))

print()
print("="*84); print("§23.1  HYDRIDE REGRESSION — the one surviving empirical result"); print("="*84)
dHf={21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,39:-114.,40:-82.,
41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,57:-104.,58:-100.,59:-104.,60:-100.,
62:-96.,63:-88.,64:-92.,65:-92.,66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,
72:-66.,73:-38.,74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
ZS=sorted(dHf); Y=np.array([dHf[z] for z in ZS])
def loo(cols):
    X=np.column_stack([np.ones(len(Y))]+cols); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    b2,*_=np.linalg.lstsq(X,Y,rcond=None)
    fit=1-np.sum((Y-X@b2)**2)/np.sum((Y-np.mean(Y))**2)
    return fit,1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2),b2
for nm,cfg in [('idealised',ed.E),('strict',STRICT)]:
    l=np.array([cfg[z][1] for z in ZS],float); k=np.array([cfg[z][2] for z in ZS],float)
    f,cv,b=loo([l,k])
    print(f"  {nm:<11} fit R²={f:.3f}  LOO R²={cv:.3f}  ΔH ≈ {b[0]:+.1f} {b[1]:+.1f}·ℓ {b[2]:+.1f}·k")
    B=[dHf[z] for z in ZS if dcls(cfg[z])=='B']; C=[dHf[z] for z in ZS if dcls(cfg[z])=='C']
    tt,pp=stats.ttest_ind(B,C,equal_var=False)
    print(f"              Class B {np.mean(B):+.1f} vs C {np.mean(C):+.1f}, Welch p={pp:.4f}")