import numpy as np, eldata as ed
from itertools import combinations

print("="*68)
print("WHAT DEPENDS ON THE ORIGIN, AND WHAT DOESN'T")
print("="*68)

# Candidate origins
origins = {
 'H = (1,0,1)  [current]' : np.array([1,0,1]),
 '(0,0,0)  [true zero]'   : np.array([0,0,0]),
 '(1,0,0)  [shell only]'  : np.array([1,0,0]),
 '(0.5,-0.5,0.5) [offset]': np.array([0.5,-0.5,0.5]),
}

print("\n1. ORIGIN-INVARIANT quantities (differences of coordinates):")
print("   ΔQ = Q₀ − ½(Q₁+Q₂) is a DIFFERENCE → shifting origin cannot change it.")
for nm,o in origins.items():
    dq,_,_ = ed.deltaQ(46)
    # recompute with shifted coordinates
    n,l,k = ed.E[46]
    Q0=np.array([n,l,k],float)-o
    Q1=np.array([n+1,l,k],float)-o
    Q2=(np.array([n,l+1,k],float) if l+1<=n-1 else np.array([n,l-1,k],float))-o
    dq2=Q0-0.5*(Q1+Q2)
    print(f"   {nm:<26} ΔQ(Pd) = {dq2}")
print("   → ΔQ, the direction classes, and σ²(t) are ALL origin-independent.")
print("     Sections 6 and 7 of the paper are unaffected by this choice.")

print("\n2. ORIGIN-DEPENDENT quantity: |Q₀| — and hence H_cp.")
print(f"   {'origin':<26}{'|Q₀| Pd':>10}{'|Q₀| Yb':>10}{'|Q₀| Pt':>10}{'Yb/Pd':>9}")
for nm,o in origins.items():
    vals={}
    for z in (46,70,78):
        n,l,k=ed.E[z]; vals[z]=np.linalg.norm(np.array([n,l,k],float)-o)
    print(f"   {nm:<26}{vals[46]:>10.3f}{vals[70]:>10.3f}{vals[78]:>10.3f}{vals[70]/vals[46]:>9.3f}")

print("\n3. Does moving the origin change the hydride regression?")
dHf = {21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,
39:-114.,40:-82.,41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,
57:-104.,58:-100.,59:-104.,60:-100.,62:-96.,63:-88.,64:-92.,65:-92.,
66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,72:-66.,73:-38.,
74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
ZS=sorted(dHf); Y=np.array([dHf[z] for z in ZS],float)
def loo(cols):
    X=np.column_stack([np.ones(len(Y))]+cols); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2)
lv=np.array([ed.E[z][1] for z in ZS],float); kv=np.array([ed.E[z][2] for z in ZS],float)
print(f"   model on ℓ,k (origin-free coords):   LOO R² = {loo([lv,kv]):.4f}")
for nm,o in origins.items():
    q=np.array([np.linalg.norm(np.array(ed.E[z],float)-o) for z in ZS])
    print(f"   model on |Q₀| with {nm:<24} LOO R² = {loo([q]):.4f}")

print("\n4. Is hydrogen still the poset minimum under each origin?")
print("   Order structure depends on the ORDER, not the origin.")
print("   Shifting coordinates by a constant is an order isomorphism:")
print("   a ≤ b  ⟺  a−o ≤ b−o.  So the poset, its bottom element,")
print("   the join/meet closure, and the 2n² count are ALL preserved.")