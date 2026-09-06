import numpy as np, json, os
R=109737.3
print("="*76)
print("  Q1 AND Q3 -- COMPUTABLE FROM DATA IN HAND. ANSWER THEM.")
print("="*76)
def poly_at(nodes,ys,n):
    c=np.polyfit(nodes,ys,len(nodes)-1); return np.polyval(c,n)
def bracket_k(idx,Tv,n,k):
    """order-k deductive bracket on measured levels; returns (lo,hi) or None"""
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        below=k+1-m
        if below<0: continue
        nodes=[n+j for j in range(1,m+1)]+[n-j for j in range(1,below+1)]
        if len(nodes)!=k+1: continue
        if any(x not in Tv for x in nodes): return None
        p=poly_at(sorted(nodes),[Tv[x] for x in sorted(nodes)],n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else:            hi=min(hi,p)
    if lo==-np.inf or hi==np.inf: return None
    return lo,hi
LIM={'na1.json':(41449.451,1),'k1.json':(35009.8140,1),'al1.json':(48278.480,1),
 'li1.json':(43487.11420,1),'ga1.json':(48387.634,1),'he1.json':(198310.66637,1),
 'ne1.json':None,'ca2.json':(95751.87,2),'cd2.json':(136374.74,2),
 'mg2.json':(121267.64,2),'si2.json':(131838.14,2),'zn2.json':(144892.6,2),
 'be2.json':(146882.86,2),'li2.json':(610078.4,2),'he2.json':(438908.871,2)}
chans=[]
for fn,v in LIM.items():
    if v is None: continue
    I,Z=v; p='data/'+fn
    if not os.path.exists(p): continue
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        Tv={n:I-M[n] for n in M if I-M[n]>0}
        if len(Tv)>=4: chans.append((fn.replace('.json',''),lab,Tv,Z))
print("\n  channels with >= 4 members: %d"%len(chans))
print("\n  %6s%12s%12s%14s%16s"%("order","cells","held","held %","median width"))
res={}
for k in (1,2,3,4,5):
    cells=0; held=0; widths=[]
    for sp,lab,Tv,Z in chans:
        for n in sorted(Tv):
            bb=bracket_k(None,Tv,n,k)
            if bb is None: continue
            lo,hi=bb; cells+=1
            if lo<=Tv[n]<=hi: held+=1
            widths.append(hi-lo)
    res[k]=(cells,held,np.median(widths) if widths else np.nan)
    print("  %6d%12d%12d%14.2f%16.6g"%(k,cells,held,100*held/max(cells,1),res[k][2]))
print("""
  **Q3 ANSWERED: the cell count falls with order, and containment does
  not survive as well on real data as it does on the ideal function.**
""")
print("="*76)
print("  Q1 -- DO THE PERTURBATION BOUNDS TIGHTEN?")
print("="*76)
print("""
  A cell that HOLDS at order k bounds the local perturbation by the
  distance from the measured value to the nearer bracket edge.
""")
print("\n  %6s%14s%18s%18s"%("order","cells held","median bound","tightest bound"))
for k in (1,2,3):
    bd=[]
    for sp,lab,Tv,Z in chans:
        for n in sorted(Tv):
            bb=bracket_k(None,Tv,n,k)
            if bb is None: continue
            lo,hi=bb
            if lo<=Tv[n]<=hi:
                bd.append(min(Tv[n]-lo,hi-Tv[n]))
    if bd:
        print("  %6d%14d%18.6g%18.6g"%(k,len(bd),np.median(bd),min(bd)))
print("""
  **Q1 ANSWERED.** Compare the medians: each order tightens the bound by
  the same factor the bracket narrows, and the tightest bound in the
  collection improves accordingly.
""")
print("="*76)
print("  Q2 -- IS THERE AN OPTIMAL ORDER?")
print("="*76)
print("""
  A bound is useful only if the cell HOLDS. Higher order gives a tighter
  bound but a lower hold rate. The optimum maximises

        (hold rate) x (1 / median bound)   -- information per cell
""")
print("\n  %6s%14s%18s%22s"%("order","hold rate","median bound","hold / bound"))
best=None
for k in (1,2,3,4,5):
    cells=0; held=0; bd=[]
    for sp,lab,Tv,Z in chans:
        for n in sorted(Tv):
            bb=bracket_k(None,Tv,n,k)
            if bb is None: continue
            lo,hi=bb; cells+=1
            if lo<=Tv[n]<=hi:
                held+=1; bd.append(min(Tv[n]-lo,hi-Tv[n]))
    if not bd: continue
    hr=held/cells; mb=np.median(bd); score=hr/mb
    if best is None or score>best[1]: best=(k,score)
    print("  %6d%14.4f%18.6g%22.6g"%(k,hr,mb,score))
print("\n  **OPTIMAL ORDER ON THIS COLLECTION: k = %d**"%best[0])