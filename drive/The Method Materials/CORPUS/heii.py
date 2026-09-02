# He II quantum defects from the NIST ASD levels supplied 2026-08-24 (register 1758). T = limit − E; δ = n − Z√(R/T).
import re,numpy as np,itertools,sys
raw=open('heii_levels.txt',encoding='utf-8').read()
lev=[]; cur=None
for l in raw.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)<4: continue
    if c[0]: cur=c[0]
    n=int(cur[:-1]); L='spdfghikl'.index(cur[-1]); J=eval(c[2]); lev.append((n,L,float(J),float(c[3])))
print(len(lev),'levels')
Rinf=109737.31568; RHe=Rinf/(1+5.4857990907e-4/4.002602*1.007276466812/1.007276466812)  # placeholder
RHe=Rinf/(1+0.00054857990907/(4.002602-2*0.00054857990907))   # reduced mass with the He-4 nuclear mass
def delta(E,n,lim,R,Z=2): return n-Z*np.sqrt(R/(lim-E))
def series(lim,R,conv):
    out={}
    for L in range(7):
        ns=sorted({n for n,l,J,E in lev if l==L})
        vals=[]
        for n in ns:
            Js=[(J,E) for nn,l,J,E in lev if nn==n and l==L]
            if conv=='low': E=min(Js)[1]
            elif conv=='high': E=max(Js)[1]
            elif conv=='cent': E=sum((2*J+1)*E for J,E in Js)/sum(2*J+1 for J,E in Js)
            vals.append(delta(E,n,lim,R))
        out[L]=(ns,np.array(vals))
    return out
for lim in (438908.885,438908.871,438908.8874):
    for R in (Rinf,RHe):
        for conv in ('low','high','cent'):
            s=series(lim,R,conv); m=[abs(s[L][1]).mean() for L in range(7)]
            print(f'lim {lim} R {"Rinf" if R==Rinf else "RHe "} {conv:4s}  mean|δ| by ℓ:',' '.join(f'{x:.2e}' for x in m),' mono' if all(m[i]>m[i+1] for i in range(6)) else '')
print('--- limit by minimising the ng spread (n = 5..10, centroid, R_He), scanned at 0.001')
def ng_spread(lim):
    s=series(lim,RHe,'cent'); return s[4][1].max()-s[4][1].min()
grid=np.arange(438908.700,438909.100,0.001); sp=[ng_spread(x) for x in grid]; best=grid[int(np.argmin(sp))]
print('argmin',round(best,3),'spread',min(sp))
s=series(438908.871,RHe,'cent')
print('--- corrected He II series (centroid, R_He, limit 438,908.871)')
for L in range(7):
    ns,v=s[L]; print('spdfghi'[L],f'n {ns[0]}–{ns[-1]}',len(ns),f'δ̄ {v.mean():+.2e}  σ {v.std(ddof=0):.1e}  |δ̄| {abs(v.mean()):.2e}')
import json; json.dump({str(L):[abs(s[L][1].mean()),s[L][1].mean(),s[L][1].std(),s[L][0][0],s[L][0][-1],len(s[L][0])] for L in range(7)},open('heii_series.json','w'))
