from itertools import combinations, product
from fractions import Fraction as F
def classes(n,N):
    out={k:[] for k in ["concave","mean-concave","mean-concave+falling","starshaped",
                        "2nd-mean falling","subadditive"]}
    for S in product(range(N+1),repeat=n):
        if any(S[i]>S[i+1] for i in range(n-1)): continue
        d=[S[0]]+[S[i]-S[i-1] for i in range(1,n)]
        if any(x<0 for x in d): continue
        mu=[F(S[k],k+1) for k in range(n)]
        mu2=[sum(mu[:k+1])/(k+1) for k in range(n)]
        if all(d[i]>=d[i+1] for i in range(n-1)): out["concave"].append(S)
        if all(mu[i-1]+mu[i+1]<=2*mu[i] for i in range(1,n-1)): out["mean-concave"].append(S)
        if all(mu[i-1]+mu[i+1]<=2*mu[i] for i in range(1,n-1)) and \
           all(mu[i]>=mu[i+1] for i in range(n-1)): out["mean-concave+falling"].append(S)
        if all(mu[i]>=mu[i+1] for i in range(n-1)): out["starshaped"].append(S)
        if all(mu2[i]>=mu2[i+1] for i in range(n-1)): out["2nd-mean falling"].append(S)
        if all(S[i+j+1]<=S[i]+S[j] for i in range(n) for j in range(n) if i+j+1<n):
            out["subadditive"].append(S)
    return out
def fails(X):
    T=set(X); j=m=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in T: j+=1
        if tuple(map(min,a,b)) not in T: m+=1
    return j,m
def R(X,d):
    A=[sorted({x[i] for x in X}) for i in range(d)]
    phi={(i,j):{v:(max([x[i] for x in X if x[j]<=v]) if any(x[j]<=v for x in X) else None)
                for v in A[j]} for i in range(d) for j in range(d) if i!=j}
    return [y for y in product(*A) if all(phi[(i,j)][y[j]] is not None and y[i]<=phi[(i,j)][y[j]]
            for i in range(d) for j in range(d) if i!=j)]
for n,N in ((4,12),(5,9)):
    C=classes(n,N)
    print(f"\nn = {n}, N = {N}")
    print(f"  {'class':<24} {'cells':>6} {'join':>6} {'meet':>6} {'E':>5}  closed")
    for k,v in C.items():
        j,m=fails(v); E=len(set(R(v,n)))-len(set(v))
        print(f"  {k:<24} {len(v):>6} {j:>6} {m:>6} {E:>5}  {j==0 and m==0 and E==0}")
    conc=set(C["concave"]); star=set(C["starshaped"]); sub=set(C["subadditive"])
    mc=set(C["mean-concave"]); mcf=set(C["mean-concave+falling"]); m2=set(C["2nd-mean falling"])
    print(f"  chain concave ⊆ mean-concave+falling ⊆ starshaped ⊆ subadditive: "
          f"{conc<=mcf<=star<=sub}")
    print(f"  densities: concave/mcf {100*len(conc)/len(mcf):.1f}%  "
          f"mcf/star {100*len(mcf)/len(star):.1f}%  concave/star {100*len(conc)/len(star):.1f}%  "
          f"star/sub {100*len(star)/len(sub):.1f}%")