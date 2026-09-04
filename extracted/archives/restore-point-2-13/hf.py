import math
import numpy as np
from scipy.optimize import curve_fit
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; cfg_c,cp,out_,n0_,thr_=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"]
regime,near24,ORDER,OPEN=g["regime"],g["near24"],g["ORDER"],g["OPEN"]
L="spdfg"
print("  h AS THE INNER-WELL BINDING, FROM PUBLISHED ORBITAL RADII\n")
print("      ⟨r⟩ = (3n*² − ℓ(ℓ+1)) / 2Z_c   for a nodeless state")
print("      arXiv:2402.02609 — the collapsed and uncollapsed f are BOTH nodeless,")
print("      so the collapse is pure phase and h is the inner-well defect.\n")
def hfrom(r_mean, n, l, Zc):
    ns=math.sqrt((2*Zc*r_mean + l*(l+1))/3.0)
    return n-ns, ns
for nm,r,n,l,Zc in (("La 4f (⟨r⟩ = 0.7 a₀)",0.70,4,3,1),
                    ("Ba 4f (hydrogenic)", 18.0,4,3,1),
                    ("Ce 4f (contracted further)",0.55,4,3,1)):
    d,ns=hfrom(r,n,l,Zc)
    print(f"      {nm:<30}n* = {ns:>6.3f}   δ = {d:>6.3f}")
print()
k=0.4423
sc=(55/56)*56**k*math.log(2)
print(f"      at La (Nₑ=57, c=1): scale = (Nₑ−1)/Nₑ · Nₑ^k · ln2 = {sc:.4f}")
print(f"      h(f) = 1.89 / {sc:.4f} = {1.89/sc:.4f}\n")
HF=1.89/sc
print("  REFIT WITH h(d) MEASURED AND h(f) FROM THE RADIUS\n")
A_=lambda rows,kk: np.array([r[kk] for r in rows],float)
G={r_: [x for x in ROWS if x["reg"]==r_] for r_ in (1,2,3,4)}
OUTR=G[3]+G[4]
P1,N1,C1=A_(G[1],"p"),A_(G[1],"ne"),A_(G[1],"c"); D1=A_(G[1],"n0")-A_(G[1],"non")
P2,N2,C2=A_(G[2],"p"),A_(G[2],"ne"),A_(G[2],"c"); B2=A_(G[2],"b24")
Zo,To,No,Co,Lo=(A_(OUTR,"Z"),A_(OUTR,"T"),A_(OUTR,"ne"),A_(OUTR,"c"),A_(OUTR,"l"))
Y1=np.array([r["d"] for r in G[1]]); Y2=np.array([r["d"] for r in G[2]])
Yo=np.array([r["d"] for r in OUTR])
t1,t2,to=np.log(C1+1)/C1,np.log(C2+1)/C2,np.log(Co+1)/Co
Do=Zo-To; YA=np.concatenate([Y1,Y2,Yo])
HD=0.40
HTAB={2:HD,3:HF,4:HF*math.sqrt(20/12)}      # g extrapolated by the barrier
HL=np.array([HTAB.get(int(l),HD) for l in Lo])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def M(_,a,q,a2,b,kk):
    return np.concatenate([
      (a+q*D1)*np.sqrt(np.maximum(P1,1e-9))*N1**kk*t1,
      a2*(1+b*B2)*np.sqrt(np.maximum(P2,1e-9))*N2**kk*t2,
      HL*sig((Do+1.5)/0.40)*((No-1)/No)*No**kk*to])
best=None
for p0 in ([0.50,-0.035,0.52,0.23,0.442],[0.5,-0.03,0.5,0.2,0.45]):
    try:
        pr,_=curve_fit(M,np.arange(len(YA)),YA,p0=p0,maxfev=900000)
        r=YA-M(None,*pr); s=float(np.sqrt(np.mean(r**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; r=YA-M(None,*pr); a,q,a2,b,kk=pr
print(f"      h(d) = {HD} measured   h(f) = {HF:.4f} from ⟨r⟩ = 0.7 a₀")
print(f"      a={a:.4f}  q={q:+.4f}  a₂={a2:.4f}  b={b:+.4f}  k={kk:.4f}")
print(f"      rms {s:.4f} · R² {1-np.var(r)/np.var(YA):.4f}\n")
def delta(Z,c,l):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    rg=regime(Z,c,l)
    if rg==1: return (a+q*(n0_(ne-1,l,c)-out_(ne-1,c)[0]))*math.sqrt(p)*ne**kk*t
    if rg==2: return a2*(1+b*near24(Z,c,l))*math.sqrt(p)*ne**kk*t
    T=thr_(ne-1,l,c); x=max(-60.,min(60.,(Z-T+1.5)/0.40))
    return HTAB.get(l,HD)*sig(x)*((ne-1)/ne)*ne**kk*t
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for X,Yl,O in cfg:
        if X==n and Yl==l: return O
    return 0
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z; c1=cfg_c(ne-1,1); full=cfg_c(ne,1)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(c1,n,l)>=cap(l): continue
        if n!=cp(ne-1,l,1)+l+1 and occ(c1,n,l)==0: continue
        cand.append((n,l,n-delta(Z,1,l)))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(c1,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,pick))
print(f"      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
if BAD: print("      failures: " + "  ".join(
    f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z,gt,pk in BAD))
wz=max(abs(delta(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4))
badp=sum(1 for r_ in ROWS if math.floor(delta(r_["Z"],r_["c"],r_["l"]))>
         min(r_["p"],n0_(r_["ne"]-1,r_["l"],r_["c"])-r_["l"]-1))
print(f"      hydrogenic {wz:.6f} · Pauli {len(ROWS)-badp}/{len(ROWS)}")
