# He II quantum defects from the NIST ASD levels supplied 2026-08-24 (register 1758). T = limit − E; δ = n − Z√(R/T).
import re,numpy as np,itertools,sys
raw=open('heii_levels.txt',encoding='utf-8').read()
lev=[]; cur=None
for l in raw.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)<4: continue
    if c[0]: cur=c[0]
    m=re.match(r'\(?([\d.]+)\)?$',c[3].strip('() '))
    if cur and re.match(r'\d+[spdfghikl]$',cur) and c[2] and m:
        n=int(cur[:-1]); L='spdfghikl'.index(cur[-1]); J=eval(c[2].replace('/','/')); lev.append((n,L,float(J),float(m.group(1))))
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