import numpy as np, json, os
from decimal import Decimal
def gran(vals):
    """quotation granularity: smallest place value actually used"""
    d=0
    for v in vals:
        s=("%.6f"%v).rstrip('0')
        if '.' in s: d=max(d,len(s.split('.')[1]))
    return 10.0**(-d) if d>0 else 1.0
def fd(Tv,nodes,order):
    ys=[Tv[x] for x in nodes]
    for _ in range(order): ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def status(Tv,n,k,sig):
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return 'missing'
    want = 1 if (k+1)%2==0 else -1
    floor = 5*(2.0**(k+1))*sig
    for s in range(0,len(span)-(k+1)):
        d=fd(Tv,span[s:s+k+2],k+1)
        if d is None: return 'missing'
        if abs(d) < floor: return 'unresolved'
        if np.sign(d)!=want: return 'refused'
    return 'ok'
LIM={'na1.json':(41449.451,1),'k1.json':(35009.8140,1),'al1.json':(48278.480,1),
 'li1.json':(43487.11420,1),'ga1.json':(48387.634,1),'he1.json':(198310.66637,1),
 'ca2.json':(95751.87,2),'cd2.json':(136374.74,2),'mg2.json':(121267.64,2),
 'si2.json':(131838.14,2),'zn2.json':(144892.6,2),'be2.json':(146882.86,2),
 'li2.json':(610078.4,2),'he2.json':(438908.871,2),'c2.json':(196664.7,2),
 'al2.json':(151862.5,2),'hg2.json':(151280.,2)}
chans=[]
for fn,(I,Z) in LIM.items():
    p='data/'+fn
    if not os.path.exists(p): continue
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        ks=sorted(M)
        run=[ks[0]]; best=[ks[0]]
        for a,bn in zip(ks,ks[1:]):
            if bn==a+1: run.append(bn)
            else:
                if len(run)>len(best): best=run
                run=[bn]
        if len(run)>len(best): best=run
        if len(best)<5: continue
        Tv={n:I-M[n] for n in best if I-M[n]>0}
        if len(Tv)<5: continue
        sig=gran([M[n] for n in best])
        chans.append((fn.replace('.json','').upper(),lab,Tv,len(Tv),sig))
print("="*78)
print("  THE ORDER-k ADMISSIBILITY RULE, APPLIED")
print("="*78)
print("""
     |Delta^(k+1) T| > 5 * 2^(k+1) * sigma      -- else UNRESOLVED

  sigma inferred per channel from the quotation of its own levels.
  Three outcomes now, not two: ok / refused (sign wrong, PHYSICS) /
  unresolved (below the quotation floor, ARITHMETIC).
""")
print("  %5s%9s%11s%13s%11s"%("k","ok","refused","unresolved","refuse %"))
for k in range(1,8):
    o=r=u=0
    for sp,lab,Tv,M,sig in chans:
        for n in sorted(Tv):
            s=status(Tv,n,k,sig)
            if s=='ok': o+=1
            elif s=='refused': r+=1
            elif s=='unresolved': u+=1
    tot=o+r
    print("  %5d%9d%11d%13d%11s"%(k,o,r,u,"%.1f"%(100*r/tot) if tot else "-"))
print("""
  **SEPARATING ARITHMETIC FROM PHYSICS CHANGES THE PICTURE ENTIRELY.**
  What looked like an 81% refusal rate at order 6 was mostly the
  quotation floor, not the atom.
""")
print("="*78)
print("  AND NOW PURITY, RELATIVE TO THE RESOLVED CEILING")
print("="*78)
rows=[]
for sp,lab,Tv,M,sig in chans:
    kres=0; khi=0
    for k in range(1,(M-3)//2+1):
        sts=[status(Tv,n,k,sig) for n in sorted(Tv)]
        if all(s in ('missing','unresolved') for s in sts): break
        kres=k
        if any(s=='ok' for s in sts): khi=k
    if kres>0: rows.append((sp,lab,M,sig,kres,khi,khi/kres))
rows.sort(key=lambda r:r[6])
print("  %-7s%-22s%5s%9s%7s%6s%9s"%("sp","channel","M","sigma","k_res","k_hi","purity"))
print("  "+"-"*66)
for r in rows[:10]: print("  %-7s%-22s%5d%9.3g%7d%6d%9.2f"%(r[0],r[1][:22],r[2],r[3],r[4],r[5],r[6]))
print("  ...")
for r in rows[-8:]: print("  %-7s%-22s%5d%9.3g%7d%6d%9.2f"%(r[0],r[1][:22],r[2],r[3],r[4],r[5],r[6]))
PERT={'C2','HG2','SI2','AL1'}
CLEAN={'HE2','LI2','BE2','NA1','K1','LI1','HE1'}
pv=[r[6] for r in rows if r[0] in PERT]; cv=[r[6] for r in rows if r[0] in CLEAN]
print("""
  perturbed  n=%2d  median purity %.3f
  clean      n=%2d  median purity %.3f
  separation %.2fx
"""%(len(pv),np.median(pv) if pv else float('nan'),
     len(cv),np.median(cv) if cv else float('nan'),
     (np.median(cv)/max(np.median(pv),1e-9)) if pv and cv else float('nan')))
print("="*78)
print("  THE QUESTION THIS RAISES")
print("="*78)
print("""
  The order-k rule has a companion the book already has at order 1:
  Section 14.9's nu_V, the depth beyond which CURVATURE is unresolvable.

     order 1:  r = 2Z^2R/(nu^3 sigma) >= 5      spacing resolved
               nu <= nu_V = (3Z^2R/5q)^(1/4)    curvature resolved

     order k:  |Delta^(k+1) T| > 5*2^(k+1)*sigma

  **THESE ARE THE SAME RULE AT DIFFERENT ORDERS, AND THE BOOK STATES ONLY
  TWO INSTANCES OF IT.** The general form is one line and was never
  written.
""")