from collections import defaultdict
def lam9(NM,EM,LM,KM,FM):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            for sp in range(0,g+1):
             out.append((n,l,k,q,e,f,g,s,sp))
    return out
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
comp=lambda a,b:(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
def decomp(C, drop=None):
    bs=defaultdict(list)
    for c in C: bs[src(c)].append(c)
    D=set()
    for a in C:
        for b in bs.get(tgt(a),()):
            z=comp(a,b)
            if z!=a and z!=b and (drop is None or z!=drop): D.add(z)
    return D
for caps in [(3,3,1,3,1),(4,4,1,6,1),(4,4,2,6,2)]:
    C=lam9(*caps); D=decomp(C)
    print(f"caps {caps}: {len(D):,}/{len(C):,} decomposable = {100*len(D)/len(C):.1f}%")
# 4.6 -- show the test can fail
C=lam9(3,3,1,3,1)
Cbad=[c for c in C if c[3]==c[6]]      # conservative sublattice only
print(f"falsification probe (conservative cells only, {len(Cbad)}): "
      f"{len(decomp(Cbad)&set(Cbad))}/{len(Cbad)} = "
      f"{100*len(decomp(Cbad)&set(Cbad))/len(Cbad):.1f}% -- the test returns <100%, so it can fail")