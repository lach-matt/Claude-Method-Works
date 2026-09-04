import math
from itertools import product, permutations
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
def minE(cells,axes):
    best=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if best is None or E<best[0]: best=(E,p)
    return best
L="spdfg"
def integ(l1,l2):
    F=list(range(0,2*min(l1,l2)+1,2))
    G=list(range(abs(l1-l2),l1+l2+1,2))
    return F,G
PAIRS=[(0,2),(0,1),(0,0),(1,1),(2,2),(3,3)]
print("  THE F¹ DEFECT AND ITS FIX\n")
print("      raw rank k is NOT a free coordinate:")
print("          F^k exists for k even only")
print("          G^k exists for k ≡ ℓ+ℓ' (mod 2)")
print("      so ℛ admitting F¹ from G¹ and F⁰ is a coordinate error, not a gap.\n")
print("      the fix: index by POSITION IN SEQUENCE, i = 0,1,2,… within each")
print("      integral's own allowed set. parity then cannot clash.\n")
old=set(); new=set()
for l1,l2 in PAIRS:
    F,G=integ(l1,l2)
    for k in F: old.add((k,0,max(l1,l2)))
    for k in G: old.add((k,1,max(l1,l2)))
    for i,k in enumerate(F): new.add((i,0,max(l1,l2)))
    for i,k in enumerate(G): new.add((i,1,max(l1,l2)))
ks=sorted({c[0] for c in old}); ls=sorted({c[2] for c in old})
co={(ks.index(a),b,ls.index(c)) for a,b,c in old}
Eo,_=minE(co,[len(ks),2,len(ls)])
isq=sorted({c[0] for c in new}); ls2=sorted({c[2] for c in new})
cn={(isq.index(a),b,ls2.index(c)) for a,b,c in new}
En,pn=minE(cn,[len(isq),2,len(ls2)])
print(f"      raw rank k        : {len(co)} cells · E = {Eo}")
print(f"      sequence index i  : {len(cn)} cells · E = {En}\n")
if En==0: print("      → CLOSED.\n")
print(f"      {'':<8}" + "".join(f"{L[ls2[i]]:>8}" for i in pn[2]))
for ii in pn[0]:
    for b in pn[1]:
        row=f"      {['F','G'][b]}_{isq[ii]:<6}"
        for li in pn[2]:
            row+=f"{('X' if (ii,b,li) in cn else '.'):>8}"
        print(row)
print()
print("  WHAT THE SEQUENCE INDEX MEANS\n")
print("      i = 0 is the leading term of each kind: F₀ = F⁰ always, and")
print("      G₀ = G^|ℓ−ℓ'| — the lowest allowed exchange multipole.")
print("      i counts how far up the multipole ladder a term sits, and THAT")
print("      is the coordinate the physics uses, not the rank itself.\n")
print(f"      {'pair':>6}{'F sequence':>18}{'G sequence':>18}")
for l1,l2 in PAIRS:
    F,G=integ(l1,l2)
    print(f"      {L[l1]+'/'+L[l2]:>6}{str(F):>18}{str(G):>18}")
print()
print("  AND THE AMPLITUDE'S TWO NUMBERS, NAMED\n")
print("      every s/d competition in the table uses exactly F₀ and G₀:")
print("          F₀ = F⁰(ns, n'd)      the direct repulsion")
print("          G₀ = G²(ns, n'd)      the sole exchange term")
print("      two integrals, one pair of subshells, no others admitted.")
