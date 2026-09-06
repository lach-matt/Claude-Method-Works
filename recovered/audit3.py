import numpy as np, eldata as ed, itertools
from itertools import combinations
from collections import Counter
CAP=lambda l: 2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
occ=set(ed.E.values()); zs=sorted(ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
def R(claim, got, exp):
    ok = (got==exp)
    print(f"  {claim:<52}{str(got):>12}  exp {str(exp):>10}  {'OK' if ok else '*** FAIL ***'}")
    return ok

print("="*78); print("AUDIT 4 — ORDER DIMENSION WITNESS"); print("="*78)
A=[(7,2,6),(5,4,6),(5,2,8)]; B=[(5,4,8),(7,2,8),(7,4,6)]
adm=all(c in set(L) for c in A+B)
pat=all((leq(A[i],B[j]) == (i!=j)) for i in range(3) for j in range(3))
R("all six witness cells admissible", adm, True)
R("incidence aᵢ≤bⱼ iff i≠j", pat, True)
print("  → dim(Λ) ≥ 3; with Λ⊆ℕ³ giving dim ≤ 3, dim = 3 exactly.")

print()
print("="*78); print("AUDIT 5 — SPERNER, PARITY, RANKS"); print("="*78)
rk=Counter(sum(c) for c in L)
R("largest rank level", max(rk.values()), 15)
ev=sum(1 for c in L if sum(c)%2==0)
R("even-rank cells in Λ", ev, 105)
R("odd-rank cells in Λ", len(L)-ev, 105)
oe=sum(1 for c in occ if sum(c)%2==0)
R("even-rank occupied", oe, 59)
R("odd-rank occupied", len(occ)-oe, 59)
seq=[rk[i] for i in range(min(rk),max(rk)+1)]
R("rank sequence palindromic?", seq==seq[::-1], False)

print()
print("="*78); print("AUDIT 6 — MADELUNG SLICES & PERIOD LENGTHS"); print("="*78)
Lbig=[(n,l,k) for n in range(1,40) for l in range(0,n) for k in range(1,CAP(l)+1)]
c=Counter(n+l for (n,l,k) in Lbig)
got=[c[i] for i in range(1,11)]
R("slice volumes n+ℓ=1..10", got, [2,2,8,8,18,18,32,32,50,50])

print()
print("="*78); print("AUDIT 7 — OCCUPIED SET STRUCTURE"); print("="*78)
R("order-ideal violations", sum(1 for x in occ for y in L if leq(y,x) and y not in occ), 0)
cols=set((n,l) for (n,l,k) in occ)
R("occupied columns", len(cols), 19)
part=[(n,l) for (n,l) in cols if max(k for (a,b,k) in occ if (a,b)==(n,l))!=CAP(l)]
R("partially filled columns", len(part), 0)
allcols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
R("empty columns", len(allcols)-len(cols), 6)
maxel=[x for x in occ if not any(leq(x,y) and x!=y for y in occ)]
R("maximal occupied cells", len(maxel), 3)
S=set(L); nxt=set()
for m in maxel:
    for d in range(3):
        cc=list(m); cc[d]+=1; cc=tuple(cc)
        if cc in S and cc not in occ: nxt.add(cc)
R("covering cells (frontier)", len(nxt), 5)
def cleq(a,b): return a[0]<=b[0] and a[1]<=b[1]
ds=[]; order=sorted(allcols)
def enum(i,ch):
    if i==len(order): ds.append(frozenset(ch)); return
    cc=order[i]; enum(i+1,ch)
    if all(d in ch for d in allcols if cleq(d,cc) and d!=cc): enum(i+1,ch|{cc})
enum(0,frozenset())
R("down-sets of column poset", len(ds), 120)

print()
print("="*78); print("AUDIT 8 — RIGIDITY & SHEAR"); print("="*78)
def test_l(perm):
    cap={i:CAP(perm[i]) for i in range(5)}
    Lx=[(n,i,k) for n in range(1,8) for i in range(0,min(n,5)) for k in range(1,cap[i]+1)]
    pos={perm[i]:i for i in range(5)}
    Ox=set()
    for (n,l,k) in occ:
        i=pos[l]
        if i>n-1 or k>cap[i]: return False
        Ox.add((n,i,k))
    return not any(leq(y,x) and y not in Ox for x in Ox for y in Lx)
R("ℓ-orderings admissible (of 120)", sum(1 for p in itertools.permutations(range(5)) if test_l(p)), 1)
def seqof(a,b,cc):
    cnt=Counter(a*n+b*l+cc*k for (n,l,k) in Lbig)
    ks=sorted(cnt); return [cnt[x] for x in ks[:8]]
hits=[(a,b,cc) for a in range(3) for b in range(3) for cc in range(3)
      if (a,b,cc)!=(0,0,0) and seqof(a,b,cc)==[2,2,8,8,18,18,32,32]]
R("shears giving period lengths", sorted(hits), [(1,1,0),(2,2,0)])

print()
print("="*78); print("AUDIT 9 — LINEAR EXTENSIONS"); print("="*78)
pairs=[(a,b) for a in zs for b in zs if a!=b and leq(ed.E[a],ed.E[b])]
R("comparable pairs (all 118)", len(pairs), 3742)
R("Z-order violations", sum(1 for a,b in pairs if a>b), 0)
mad={z:i for i,z in enumerate(sorted(zs,key=lambda z:(ed.E[z][0]+ed.E[z][1],ed.E[z][0],ed.E[z][2])))}
R("Madelung-order violations", sum(1 for a,b in pairs if mad[a]>mad[b]), 0)