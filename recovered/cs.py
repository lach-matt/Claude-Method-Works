import numpy as np
# ---- Cs I, Deiglmayr et al. arXiv:1601.08005 (PRA 2016) ----
R   = 109736.8627339        # cm^-1
EI  = 31406.4677325         # cm^-1
ser = {   # delta0, [delta2, delta4, delta6, delta8], validated n-range
 "ns_1/2": (4.0493532,[0.2391,0.06,11.0,-209.0], (11,31)),
 "nd_5/2": (2.4663144,[0.01381,-0.392,-1.9],     ( 9,36)),
 "np_1/2": (3.5915871,[0.36273],                 (27,74)),
 "np_3/2": (3.5590676,[0.37469],                 (27,74)),
}
def nu(n,d0,ds):
    x=(n-d0); d=d0+sum(c/x**(2*(k+1)) for k,c in enumerate(ds)); return n-d
def V_block(ns,d0,ds):
    v=np.array([nu(n,d0,ds) for n in ns]); T=R/v**2
    w=np.abs(T[:-2]-T[2:]); e=np.abs(T[1:-1]-0.5*(T[:-2]+T[2:]))
    return w.sum()/e.sum(), v

print("Cs I  --  V computed ONLY inside each series' validated fit range")
print(f"{'series':9s}{'block':>10s}{'nu range':>16s}{'V':>9s}{'4*nu_bar/3':>12s}")
for k,(d0,ds,(lo,hi)) in ser.items():
    for blk in ([ (lo,lo+6), (lo,hi) ] if k.startswith('n') else []):
        ns=list(range(blk[0],min(blk[1],hi)+1))
        if len(ns)<3: continue
        V,v=V_block(ns,d0,ds)
        print(f"{k:9s}{str(blk):>10s}{v.min():7.2f}-{v.max():<8.2f}{V:9.2f}{4*v[1:-1].mean()/3:12.2f}")

print("\nper-cell V inside the validated range (lowest few cells)")
for k in ("ns_1/2","nd_5/2"):
    d0,ds,(lo,hi)=ser[k]
    for n in range(lo+1,lo+5):
        v=[nu(m,d0,ds) for m in (n-1,n,n+1)]; T=R/np.array(v)**2
        Vc=abs(T[0]-T[2])/abs(T[1]-0.5*(T[0]+T[2]))
        print(f"  {k}  n={n:2d}  nu={v[1]:6.3f}   V={Vc:7.2f}")

print("\nEXTRAPOLATED below the fit range (flagged, not load-bearing)")
for k in ("np_3/2","ns_1/2","nd_5/2"):
    d0,ds,_=ser[k]
    n0 = 6 if k.startswith('np') else (6 if k.startswith('ns') else 5)
    ns=list(range(n0,n0+5)); V,v=V_block(ns,d0,ds)
    print(f"  {k} n={ns[0]}-{ns[-1]}  nu={v.min():.2f}-{v.max():.2f}   V={V:.2f}")

# ---------- SEMF vs the paper's AME2020 V_resolved ----------
from scipy.stats import spearmanr,pearsonr
semf =[18.99,22.15,24.15,27.00,29.06,29.60,32.56,36.65,40.21]
paper=[21.7 ,24.2 ,27.1 ,28.4 ,31.1 ,35.7 ,47.4 ,54.0 ,56.9 ]
Z=[20,22,24,26,28,30,32,34,36]
print("\nLiquid-drop prediction of the paper's AME2020 V_resolved (no fitted parameter)")
print(f"  Spearman = {spearmanr(semf,paper).correlation:+.4f}   Pearson = {pearsonr(semf,paper)[0]:+.4f}")
print(f"  ratio paper/SEMF: {[round(p/s,2) for p,s in zip(paper,semf)]}")