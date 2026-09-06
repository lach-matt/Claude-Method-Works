from itertools import combinations, product

# ---- test lattice: L = {(n,l) : 1<=n<=4, 0<=l<=min(n-1,2)} ----
# a sublattice of chain x chain, NOT interval-closed: (1,1) lies between
# (1,0) and (2,1) componentwise but violates l <= n-1.
L=[(n,l) for n in range(1,5) for l in range(0,min(n-1,2)+1)]
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
Ls=set(L)
assert all(jn(a,b) in Ls and mt(a,b) in Ls for a in L for b in L), "not a sublattice"
print(f"test lattice |L| = {len(L)}  elements {L}")
print("sublattice of chain x chain: yes;  interval-closed:",
      all((n,l) in Ls for n in range(1,5) for l in range(0,3)
          if any(a[0]<=n<=b[0] and a[1]<=l<=b[1] for a in L for b in L)))

def le(a,b): return all(x<=y for x,y in zip(a,b))

# ---- exact order dimension via minimum realizer ----
def linexts(P, leq, cap=200000):
    out=[]
    def rec(rem, cur):
        if not rem: out.append(tuple(cur)); return
        for x in sorted(rem):
            if not any(leq(y,x) and y!=x for y in rem):
                rec(rem-{x}, cur+[x])
    rec(set(P), [])
    return out
def order_dim(P, leq, kmax=6):
    inc=[(a,b) for a in P for b in P if a!=b and not leq(a,b) and not leq(b,a)]
    if not inc: return 1
    cov=set()
    for E in linexts(P,leq):
        pos={x:i for i,x in enumerate(E)}
        cov.add(frozenset((a,b) for (a,b) in inc if pos[a]<pos[b]))
    cov=list(cov); need=set(inc)
    for k in range(1,kmax+1):
        for c in combinations(range(len(cov)),k):
            u=set()
            for i in c: u|=cov[i]
            if u>=need: return k
    return None

dL=order_dim(L,le)
print(f"exact dim(L) = {dL}\n")

# ---- enumerate ALL functions h: L -> {0..V-1}; keep closure-preserving ----
for V in (3,4):
    tot=closed=mono=single=dim_eq=0
    counterex=[]
    for vals in product(range(V), repeat=len(L)):
        h=dict(zip(L,vals)); tot+=1
        ok=True
        for a in L:
            for b in L:
                if h[jn(a,b)]!=max(h[a],h[b]) or h[mt(a,b)]!=min(h[a],h[b]):
                    ok=False; break
            if not ok: break
        if not ok: continue
        closed+=1
        if all(h[a]<=h[b] for a in L for b in L if le(a,b)): mono+=1
        # depends on a single coordinate?
        s=False
        for i in (0,1):
            if all(h[a]==h[b] for a in L for b in L if a[i]==b[i]): s=True; break
        if s: single+=1
        else: counterex.append(dict(h))
    print(f"V={V}: {tot:,} functions -> {closed} closure-preserving")
    print(f"       monotone: {mono}/{closed}   depend on ONE coordinate: {single}/{closed}")
    print(f"       COUNTEREXAMPLES to old Thm 4.1: {closed-single}")
    if counterex:
        h=counterex[0]
        print(f"       e.g. h = {{{', '.join(f'{k}:{v}' for k,v in sorted(h.items()))}}}")
    # dimension check on every closure-preserving h
    bad=0; tested=0
    for vals in product(range(V), repeat=len(L)):
        h=dict(zip(L,vals)); ok=True
        for a in L:
            for b in L:
                if h[jn(a,b)]!=max(h[a],h[b]) or h[mt(a,b)]!=min(h[a],h[b]):
                    ok=False; break
            if not ok: break
        if not ok: continue
        G=[(a[0],a[1],h[a]) for a in L]
        if order_dim(G,le)!=dL: bad+=1
        tested+=1
    print(f"       dim(graph) == dim(L) in {tested-bad}/{tested};  raised in {bad}\n")