import numpy as np, json, os
def fd(Tv,nodes,order):
    ys=[Tv[x] for x in nodes]
    for _ in range(order): ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def status(Tv,n,k):
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return 'missing'
    want = 1 if (k+1)%2==0 else -1
    for s in range(0,len(span)-(k+1)):
        d=fd(Tv,span[s:s+k+2],k+1)
        if d is None or np.sign(d)!=want: return 'refused'
    return 'ok'
LIM={'na1.json':(41449.451,1),'k1.json':(35009.8140,1),'al1.json':(48278.480,1),
 'li1.json':(43487.11420,1),'ga1.json':(48387.634,1),'he1.json':(198310.66637,1),
 'ca2.json':(95751.87,2),'cd2.json':(136374.74,2),'mg2.json':(121267.64,2),
 'si2.json':(131838.14,2),'zn2.json':(144892.6,2),'be2.json':(146882.86,2),
 'li2.json':(610078.4,2),'he2.json':(438908.871,2),'c2.json':(196664.7,2),
 'al2.json':(151862.5,2),'hg2.json':(151280.,2),'ne1.json':None}
chans=[]
for fn,v in LIM.items():
    if v is None: continue
    I,Z=v; p='data/'+fn
    if not os.path.exists(p): continue
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        Tv={n:I-M[n] for n in M if I-M[n]>0}
        ks=sorted(Tv)
        run=[ks[0]]; best=[ks[0]]
        for a,bnd in zip(ks,ks[1:]):
            if bnd==a+1: run.append(bnd)
            else:
                if len(run)>len(best): best=run
                run=[bnd]
        if len(run)>len(best): best=run
        if len(best)>=5:
            chans.append((fn.replace('.json','').upper(),lab,{n:Tv[n] for n in best},len(best)))
print("="*78)
print("  LENGTH-MATCHED PURITY -- REMOVING THE CONFOUND")
print("="*78)
print("""
  A channel of M CONSECUTIVE members can reach at most order k_max where
  2(k_max+1)+1 <= M, i.e. k_max = floor((M-3)/2). Purity must be measured
  RELATIVE to that ceiling.

        PURITY = (highest admitted k) / k_max
""")
rows=[]
for sp,lab,Tv,M in chans:
    kmax=max(1,(M-3)//2)
    hi=0
    for k in range(1,kmax+1):
        if any(status(Tv,n,k)=='ok' for n in sorted(Tv)): hi=k
    rows.append((sp,lab,M,kmax,hi,hi/kmax))
rows.sort(key=lambda r:r[5])
print("  %-7s%-24s%6s%7s%7s%9s"%("species","channel","M","k_max","k_hi","purity"))
print("  " + "-"*62)
for r in rows[:12]: print("  %-7s%-24s%6d%7d%7d%9.2f"%(r[0],r[1][:24],r[2],r[3],r[4],r[5]))
print("  ...")
for r in rows[-10:]: print("  %-7s%-24s%6d%7d%7d%9.2f"%(r[0],r[1][:24],r[2],r[3],r[4],r[5]))
print("""
{0}
  DOES PURITY SEPARATE THE KNOWN PERTURBED FROM THE KNOWN CLEAN?
{0}
""".format("="*78))
PERT={'C2','HG2','SI2'}
CLEAN={'HE2','LI2','BE2','NA1','K1','LI1'}
pv=[r[5] for r in rows if r[0] in PERT]
cv=[r[5] for r in rows if r[0] in CLEAN]
print("  perturbed species (C II, Hg II, Si II)  n=%2d   median purity %.3f"%(len(pv),np.median(pv) if pv else float('nan')))
print("  clean species     (He/Li/Be II, Na/K/Li I) n=%2d   median purity %.3f"%(len(cv),np.median(cv) if cv else float('nan')))
if pv and cv:
    print("\n  separation: %.2fx"%(np.median(cv)/max(np.median(pv),1e-9)))
print("""
{0}
  AND THE ONE THE BOOK FLAGGED BY NAME
{0}
""".format("="*78))
for sp,lab,M,kmax,hi,pu in rows:
    if sp=='AL1' or sp=='AL2' or sp=='C2':
        print("  %-7s%-26s M=%2d  k_max=%d  k=%d  purity %.2f"%(sp,lab[:26],M,kmax,hi,pu))
print("""
{0}
  AND A CLEANLINESS INDEX THAT NEEDS NO LIMIT AND NO FIT
{0}

  PURITY is computed from the SIGNS of finite differences of measured
  levels. It needs:

     no ionisation limit          (differences are limit-free)
     no quantum defect            (no fit)
     no uncertainty estimate      (only signs)
     no theory of the perturber   (only that hydrogenic form is violated)

  **IT IS THE MOST ASSUMPTION-FREE DIAGNOSTIC IN THIS BOOK**, and it falls
  directly out of the k-th order bracket -- which itself fell out of one
  question asked about a chapter that was already written.
""".format("="*78))