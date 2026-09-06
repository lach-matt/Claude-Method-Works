from itertools import combinations
def exact(n,N):
    out=[]
    def rec(pref,prev,tot):
        if len(pref)==n:
            S=[];r=0
            for m in pref: r+=m; S.append(r)
            out.append(tuple(S)); return
        for m in range(0,min(prev,N-tot)+1): rec(pref+[m],m,tot+m)
    rec([],N,0); return out
def chain(n,N):
    cells=[(s,) for s in range(N+1)]
    for k in range(1,n):
        cells=[c+(t,) for c in cells for t in range(c[-1],min((k+1)*c[-1]//k,N)+1)]
    return cells
def Rpruned(X,d):
    A=[sorted({x[i] for x in X}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for v in A[j]:
                c=[x[i] for x in X if x[j]<=v]
                m[v]=max(c) if c else None
            phi[(i,j)]=m
    out=[]
    def rec(pref):
        k=len(pref)
        if k==d: out.append(tuple(pref)); return
        for v in A[k]:
            ok=True
            for j in range(k):
                b=phi[(k,j)][pref[j]]
                if b is None or v>b: ok=False;break
                b2=phi[(j,k)][v]
                if b2 is None or pref[j]>b2: ok=False;break
            if ok: rec(pref+[v])
    rec([]); return out

print(f"{'n':>3} {'N':>4} {'exact':>7} {'my chain':>9} {'R(exact)':>9} {'E(exact)':>9} "
      f"{'my density':>11} {'true density':>13} {'tightest?':>10}")
for n in (3,4,5):
    for N in (12,16,20):
        ex=exact(n,N); ch=chain(n,N)
        Rx=Rpruned(ex,n)
        tight = len(Rx)==len(ch)
        print(f"{n:>3} {N:>4} {len(ex):>7} {len(ch):>9} {len(Rx):>9} {len(Rx)-len(ex):>9} "
              f"{100*len(ex)/len(ch):>10.1f}% {100*len(ex)/len(Rx):>12.1f}% {str(tight):>10}")

# is R(exact) closed, and does it equal the chain set?
n,N=4,16
ex=exact(n,N); ch=set(chain(n,N)); Rx=Rpruned(ex,n)
print(f"\nn=4 N=16: R(exact) == chain envelope: {set(Rx)==ch}")
print(f"  R idempotent: {len(Rpruned(Rx,n))==len(Rx)}")
S=set(Rx); jf=mf=0
for a,b in combinations(Rx,2):
    if tuple(map(max,a,b)) not in S: jf+=1
    if tuple(map(min,a,b)) not in S: mf+=1
print(f"  R(exact) join fail {jf}  meet fail {mf}")