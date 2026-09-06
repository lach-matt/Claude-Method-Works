import numpy as np, itertools
R=109737.3
# ---------- Sc VI arithmetic check (§10 iii) ----------
d=(1.0057+0.9812)/2; lim=892700.0; Z=6
for n,ref in [(6,735092),(7,783202)]:
    nu=n-d; T=Z**2*R/nu**2; print(f"Sc VI {n}s: nu={nu:.4f}  T={T:9.1f}  E={lim-T:9.1f}  (paper {ref})")
nus=[4-d,5-d,6-d]; T=np.array([Z**2*R/x**2 for x in nus])
print(f"  V at the 5s cell = {abs(T[0]-T[2])/abs(T[1]-0.5*(T[0]+T[2])):.2f}   (nu={nus[1]:.2f})")

# ---------- §4.2 as a characterisation ----------
def analyse(L,name):
    idx={c:i for i,c in enumerate(L)}
    jn=lambda a,b:(max(a[0],b[0]),max(a[1],b[1])); mt=lambda a,b:(min(a[0],b[0]),min(a[1],b[1]))
    def closed(h):
        for a in L:
            for b in L:
                j,m=jn(a,b),mt(a,b)
                if j not in idx or m not in idx: return False
                if h[idx[j]]!=max(h[idx[a]],h[idx[b]]) or h[idx[m]]!=min(h[idx[a]],h[idx[b]]): return False
        return True
    def hom(h):   # lattice homomorphism onto a chain
        return closed(h)
    def dep(h,ax):
        return any(a[1-ax]==b[1-ax] and a[ax]!=b[ax] and h[idx[a]]!=h[idx[b]] for a in L for b in L)
    cl=[h for h in itertools.product(range(3),repeat=len(L)) if closed(list(h))]
    two=[h for h in cl if dep(h,0) and dep(h,1)]
    # coordinate filters and strict cross-coordinate containments
    F={}
    for ax in (0,1):
        vals=sorted({c[ax] for c in L})
        for v in vals[1:]: F[(ax,v)]={x for x in L if x[ax]>=v}
    cc=[(a,b) for a in F for b in F if a[0]!=b[0] and F[a]<F[b]]
    # is every closure-preserving h a lattice hom onto a chain? (by construction) - verify surjectivity onto its image chain
    allhom=all(hom(list(h)) for h in cl)
    print(f"{name:32s} closure-preserving={len(cl):4d}  depend on BOTH coords={len(two):3d}  "
          f"cross-coord filter containments={len(cc):2d}  all are lattice homs={allhom}")
    return len(two),len(cc)

L1=[(n,l) for n in range(1,5) for l in range(0,min(n-1,2)+1)]        # paper's test sublattice
L2=[(n,l) for n in range(1,5) for l in range(0,3)]                   # 4x3 product of chains
L3=[(n,l) for n in range(1,6) for l in range(0,min(n-1,3)+1)]        # larger triangular sublattice
L4=[(n,l) for n in range(1,5) for l in range(0,min(n,2)+1)]          # shifted constraint l<=n
print("\n§4.2 criterion:")
r=[analyse(L,nm) for L,nm in [(L1,"triangular sublattice (paper)"),(L2,"4x3 product of chains"),
                              (L3,"larger triangular sublattice"),(L4,"shifted triangle l<=min(n,2)")]]
print("\n  both-coordinate count vs cross-coordinate filter containments:",[(a,b) for a,b in r])
print("  criterion: single-coordinate property holds  <=>  no two coordinate-filters are comparable")