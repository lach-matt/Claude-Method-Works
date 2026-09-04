import numpy as np, math
from itertools import combinations
from collections import deque
W={'shell':(0,4),'subshell':(1,5),'occupancy':(2,9),'spin':(7,8)}
names=list(W)
adj={'shell':['subshell'],'subshell':['shell','occupancy'],
     'occupancy':['subshell','spin'],'spin':['occupancy']}
def dist(a,b):
    q=deque([(a,0)]); seen={a}
    while q:
        u,d=q.popleft()
        if u==b: return d
        for v in adj[u]:
            if v not in seen: seen.add(v); q.append((v,d+1))
def build(NM,EM,LM,KM,FM):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            for G in range(g,2*(2*f+1)+1):
             for sp in range(0,G+1):
              out.append((n,l,k,q,e,f,g,s,sp,G))
    return np.array(out,dtype=np.int16)
def run(cp):
    A=build(*cp); N=len(A)
    rad=(A.max(0)+1).astype(np.int64); mult=np.ones(10,dtype=np.int64)
    for i in range(8,-1,-1): mult[i]=mult[i+1]*rad[i+1]
    enc=lambda M:(M.astype(np.int64)*mult).sum(1)
    dec={int(c):tuple(t) for c,t in zip(enc(A).tolist(),A.tolist())}
    def codes(combo):
        m=np.logical_and.reduce([A[:,W[w][1]]<=A[:,W[w][0]] for w in combo])
        return set(enc(A[m]).tolist())
    def gen(cs):
        cur=set(cs)
        while True:
            arr=np.array([dec[c] for c in cur],dtype=np.int16); new=set()
            for i in range(len(arr)):
                r=arr[i]
                new|=set(enc(np.maximum(r,arr[i+1:])).tolist())
                new|=set(enc(np.minimum(r,arr[i+1:])).tolist())
            new-=cur
            if not new: return cur
            cur|=new
    rows=[]
    for a,b in combinations(names,2):
        U=codes((a,))|codes((b,)); G=gen(U)
        amp=len(G)-len(U); gap=N-len(U)
        rows.append((dist(a,b),amp,amp/len(U),amp/gap if gap else 0,a,b))
    return N,rows
for cp in [(3,3,1,3,1),(4,4,1,3,1),(3,3,1,4,1)]:
    N,rows=run(cp)
    print(f"\ncaps {cp}  |X|={N:,}")
    print(f"  {'pair':<26} {'d':>2} {'amp':>7} {'amp/|U|':>9} {'amp/gap':>9}")
    for d,amp,r1,r2,a,b in sorted(rows):
        print(f"  {a+' ∪ '+b:<26} {d:>2} {amp:>7,} {r1:>9.4f} {r2:>9.4f}")
    for lab,idx in (("raw amp",1),("amp/|U|",2),("amp/gap",3)):
        byd={dd:[r[idx] for r in rows if r[0]==dd] for dd in (1,2,3)}
        mono=all(max(byd[dd])<min(byd[dd-1]) for dd in (2,3) if byd[dd] and byd[dd-1])
        rev =all(min(byd[dd])>max(byd[dd-1]) for dd in (2,3) if byd[dd] and byd[dd-1])
        print(f"    {lab:<9} monotone by distance: {mono}   reversed: {rev}")