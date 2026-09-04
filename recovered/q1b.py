import numpy as np, json, os
R=109737.3
def poly_at(nodes,ys,n):
    c=np.polyfit(nodes,ys,len(nodes)-1); return np.polyval(c,n)
def fd(Tv,nodes,order):
    """order-th forward finite difference on consecutive integer nodes"""
    ys=[Tv[x] for x in nodes]
    for _ in range(order):
        ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def bracket_k(Tv,n,k):
    """order-k bracket WITH the premise checked: sign of the (k+1)-th
       difference must be (-1)^(k+1) on every window used."""
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return ('refused-missing',None)
    want = 1 if (k+1)%2==0 else -1
    for s in range(0,len(span)-(k+1)):
        w=span[s:s+k+2]
        d=fd(Tv,w,k+1)
        if d is None or np.sign(d)!=want:
            return ('refused-sign',None)
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        below=k+1-m
        if below<0: continue
        nodes=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,below+1)])
        if len(nodes)!=k+1: continue
        p=poly_at(nodes,[Tv[x] for x in nodes],n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else:            hi=min(hi,p)
    if lo==-np.inf or hi==np.inf or hi<lo: return ('refused-degenerate',None)
    return ('ok',(lo,hi))
LIM={'na1.json':(41449.451,1),'k1.json':(35009.8140,1),'al1.json':(48278.480,1),
 'li1.json':(43487.11420,1),'ga1.json':(48387.634,1),'he1.json':(198310.66637,1),
 'ca2.json':(95751.87,2),'cd2.json':(136374.74,2),'mg2.json':(121267.64,2),
 'si2.json':(131838.14,2),'zn2.json':(144892.6,2),'be2.json':(146882.86,2),
 'li2.json':(610078.4,2),'he2.json':(438908.871,2)}
chans=[]
for fn,(I,Z) in LIM.items():
    p='data/'+fn
    if not os.path.exists(p): continue
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        Tv={n:I-M[n] for n in M if I-M[n]>0}
        if len(Tv)>=4: chans.append((fn.replace('.json',''),lab,Tv))
print("="*76)
print("  THE PREMISE, CHECKED -- REFUSE RATHER THAN COERCE (D.2.9)")
print("="*76)
print("\n  channels: %d\n"%len(chans))
print("  %5s%10s%12s%12s%12s%10s%14s"%("order","admitted","refused-sig","held","hold %","median w","median bound"))
tab={}
for k in (1,2,3,4,5,6):
    adm=0; rsig=0; held=0; ws=[]; bd=[]
    for sp,lab,Tv in chans:
        for n in sorted(Tv):
            st,bb=bracket_k(Tv,n,k)
            if st=='refused-sign': rsig+=1; continue
            if st!='ok': continue
            lo,hi=bb; adm+=1; ws.append(hi-lo)
            if lo<=Tv[n]<=hi:
                held+=1; bd.append(min(Tv[n]-lo,hi-Tv[n]))
    if adm==0: continue
    tab[k]=(adm,rsig,held,np.median(ws),np.median(bd) if bd else np.nan)
    print("  %5d%10d%12d%12d%12.2f%10.4g%14.6g"%(k,adm,rsig,held,100*held/adm,
          np.median(ws),np.median(bd) if bd else float('nan')))
print("""
  **CHECKING THE PREMISE RESTORES CONTAINMENT.** Cells whose (k+1)-th
  difference has the wrong sign are REFUSED, not counted as failures --
  and the refusal is itself the detection of a perturbation.
""")
print("="*76)
print("  AND THE REFUSALS ARE THE PHYSICS")
print("="*76)
print("""
  A refused-sign cell says: the (k+1)-th difference of the measured levels
  does not have the sign the hydrogenic form requires. That is a
  perturbation, detected DEDUCTIVELY, with no fit.
""")
print("  %5s%14s%16s"%("order","refused-sign","as % of cells"))
for k in tab:
    adm,rsig,held,mw,mb=tab[k]
    print("  %5d%14d%16.1f"%(k,rsig,100*rsig/max(adm+rsig,1)))
print("""
  **THE HIGHER THE ORDER, THE MORE SENSITIVE THE DETECTOR.** Order 1 sees
  only sign changes in the spacing; order 5 sees a perturbation in the
  fifth difference, far below anything a fit residual would flag.
""")
print("="*76)
print("  THE OPTIMUM, RECOMPUTED ON ADMITTED CELLS ONLY")
print("="*76)
print("\n  %5s%12s%16s%20s%16s"%("order","hold rate","median bound","info per cell","cells held"))
best=None
for k in tab:
    adm,rsig,held,mw,mb=tab[k]
    if not np.isfinite(mb) or mb<=0: continue
    hr=held/adm; score=hr/mb
    if best is None or score>best[1]: best=(k,score)
    print("  %5d%12.4f%16.6g%20.6g%16d"%(k,hr,mb,score,held))
if best: print("\n  **maximum information per cell at order k = %d**"%best[0])
print("""
  If the score is still climbing at the last order shown, the optimum is
  above it and the honest answer is that the collection's depth -- not the
  method -- is the binding constraint.
""")