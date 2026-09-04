from itertools import product, combinations
L=[(n,l) for n in range(1,5) for l in range(0,min(n-1,2)+1)]
def le(a,b): return all(x<=y for x,y in zip(a,b))
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))

# Does MONOTONE alone (without closure) give an order-isomorphism onto the graph?
mono=iso=0
for vals in product(range(4), repeat=len(L)):
    h=dict(zip(L,vals))
    if not all(h[a]<=h[b] for a in L for b in L if le(a,b)): continue
    mono+=1
    G={a:(a[0],a[1],h[a]) for a in L}
    if all(le(a,b)==le(G[a],G[b]) for a in L for b in L): iso+=1
print(f"monotone h (V=4): {mono}   inducing order-isomorphism onto graph: {iso}")
print(f"mismatches: {mono-iso}")

# and non-monotone h: can any have a closed graph?
nonmono=nonmono_closed=0
for vals in product(range(3), repeat=len(L)):
    h=dict(zip(L,vals))
    if all(h[a]<=h[b] for a in L for b in L if le(a,b)): continue
    nonmono+=1
    if all(h[jn(a,b)]==max(h[a],h[b]) and h[mt(a,b)]==min(h[a],h[b])
           for a in L for b in L): nonmono_closed+=1
print(f"\nnon-monotone h (V=3): {nonmono}   with a CLOSED graph: {nonmono_closed}")