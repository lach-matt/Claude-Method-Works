import numpy as np, sys
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
    def masks(w): return A[:,W[w][1]]<=A[:,W[w][0]]
    rows=[]
    for a,b in combinations(names,2):
        U=A[masks(a)|masks(b)]
        cur=U.copy()
        seen=set(map(tuple,cur.tolist()))
        work=deque(map(tuple,cur.tolist()))
        while work:
            x=np.array(work.popleft(),dtype=np.int16)
            arr=cur
            J=np.maximum(x,arr); M=np.minimum(x,arr)
            add=[]
            for R in (J,M):
                for t in map(tuple,R.tolist()):
                    if t not in seen:
                        seen.add(t); add.append(t); work.append(t)
            if add:
                cur=np.vstack([cur,np.array(add,dtype=np.int16)])
        amp=len(seen)-len(U); gap=N-len(U)
        rows.append((dist(a,b),amp,amp/gap if gap else 0.0,a,b))
        sys.stdout.flush()
    return N,rows
for cp in [(3,3,1,3,1),(4,4,1,3,1),(3,3,1,4,1),(3,4,1,3,1)]:
    N,rows=run(cp)
    byd={d:[r[2] for r in rows if r[0]==d] for d in (1,2,3)}
    mono_rev=all(min(byd[d])>max(byd[d-1]) for d in (2,3) if byd[d] and byd[d-1])
    print(f"caps {cp}  |X|={N:>7,}   amp/gap rises strictly with distance: {mono_rev}")
    print("   " + "   ".join(f"d{d}: {[round(x,3) for x in sorted(byd[d])]}" for d in (1,2,3)))