from itertools import product, combinations

def build(N):
    """coordinates (m1, S, M); m2 = S-m1, m3 = M-S recovered."""
    env=[]; exact=[]
    for m1 in range(0,N+1):
        for S in range(m1, min(2*m1, N)+1):
            for M in range(S, min(2*S, N)+1):          # envelope: M <= 2S
                env.append((m1,S,M))
                if M <= 2*S - m1:                       # law: m2 >= m3
                    exact.append((m1,S,M))
    return env, exact

def R(X,d=3):
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
    for y in product(*A):
        if all(phi[(i,j)][y[j]] is not None and y[i]<=phi[(i,j)][y[j]]
               for i in range(d) for j in range(d) if i!=j):
            out.append(y)
    return out

def jm(X):
    S=set(X); jf=mf=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in S: jf+=1
        if tuple(map(min,a,b)) not in S: mf+=1
    return jf,mf

print(f"{'cap N':>6} {'envelope':>9} {'E_env':>6} {'joinF':>6} {'meetF':>6} "
      f"{'exact':>7} {'E_exact':>8} {'joinF':>6} {'meetF':>6} {'density':>8}")
for N in (8,12,16,20):
    env,exa=build(N)
    Ee=len(R(env))-len(env); Ex=len(R(exa))-len(exa)
    je,me=jm(env); jx,mx=jm(exa)
    print(f"{N:>6} {len(env):>9} {Ee:>6} {je:>6} {me:>6} "
          f"{len(exa):>7} {Ex:>8} {jx:>6} {mx:>6} {100*len(exa)/len(env):>7.1f}%")

# what the surplus contains -- the tripwire
env,exa=build(12); surplus=set(env)-set(exa)
print(f"\nsurplus at N=12: {len(surplus)} cells; every one violates m2 >= m3:")
bad=[(m1,S-m1,M-S) for (m1,S,M) in surplus]
print("  all have m2 < m3:", all(b[1]<b[2] for b in bad))
print("  sample (m1,m2,m3):", sorted(bad)[:6])

# the two-parent bound restored: does the exact set close if M<=2S-m1 is a real constraint?
print("\nis the exact set a sublattice?  join/meet failures above answer it.")