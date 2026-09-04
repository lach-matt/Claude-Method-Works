from itertools import product, combinations
def R(X,d=3):
    A=[sorted({x[i] for x in X}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            phi[(i,j)]={v:(max([x[i] for x in X if x[j]<=v]) if any(x[j]<=v for x in X) else None)
                        for v in A[j]}
    return [y for y in product(*A)
            if all(phi[(i,j)][y[j]] is not None and y[i]<=phi[(i,j)][y[j]]
                   for i in range(d) for j in range(d) if i!=j)]
def jm(X):
    S=set(X); jf=mf=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in S: jf+=1
        if tuple(map(min,a,b)) not in S: mf+=1
    return jf,mf

def run(N):
    trip=[(a,b,c) for a in range(N+1) for b in range(a+1) for c in range(b+1) if a+b+c<=N]
    # system A: (m1, S, M)
    A_exact=[(m1,m1+m2,m1+m2+m3) for m1,m2,m3 in trip]
    A_env=[(m1,S,M) for m1 in range(N+1) for S in range(m1,min(2*m1,N)+1)
                    for M in range(S,min(2*S,N)+1)]
    # system B: (S12, S13, S23)
    B_exact=[(m1+m2,m1+m3,m2+m3) for m1,m2,m3 in trip]
    cap=max(x[0] for x in B_exact)
    B_env=[(a,b,c) for a in range(cap+1) for b in range((a+1)//2, a+1)
                   for c in range(b+1) if a<=2*b]
    out={}
    for nm,ex,en in (("A",A_exact,A_env),("B",B_exact,B_env)):
        Ee=len(R(en))-len(en); jf_e,mf_e=jm(en)
        Ex=len(R(ex))-len(ex); jf_x,mf_x=jm(ex)
        out[nm]=(len(en),Ee,jf_e,mf_e,len(ex),Ex,jf_x,mf_x,100*len(ex)/len(en))
    return out

print(f"{'N':>3} {'sys':>4} {'envelope':>9} {'E':>4} {'jF':>3} {'mF':>3} "
      f"{'exact':>7} {'E':>5} {'joinF':>7} {'meetF':>7} {'density':>8}")
for N in (8,12,16,20):
    r=run(N)
    for nm in "AB":
        e,Ee,je,me,x,Ex,jx,mx,d=r[nm]
        print(f"{N:>3} {nm:>4} {e:>9} {Ee:>4} {je:>3} {me:>3} {x:>7} {Ex:>5} "
              f"{jx:>7} {mx:>7} {d:>7.1f}%")

# decompose system B's gap
N=16
trip=[(a,b,c) for a in range(N+1) for b in range(a+1) for c in range(b+1) if a+b+c<=N]
Bx=set((m1+m2,m1+m3,m2+m3) for m1,m2,m3 in trip)
cap=max(x[0] for x in Bx)
Ben=[(a,b,c) for a in range(cap+1) for b in range((a+1)//2,a+1) for c in range(b+1) if a<=2*b]
gap=[y for y in Ben if y not in Bx]
tri=sum(1 for a,b,c in gap if a>b+c)
par=sum(1 for a,b,c in gap if a<=b+c and (a+b+c)%2)
cp =sum(1 for a,b,c in gap if a<=b+c and (a+b+c)%2==0 and (a+b+c)//2>N)
print(f"\nsystem B gap at N={N}: {len(gap)} cells = triangle {tri} + congruence {par} + cap {cp}"
      f"  (sum {tri+par+cp})")