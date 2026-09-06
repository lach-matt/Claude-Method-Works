"""INDEPENDENT RE-DERIVATION — deliberately not importing eldata.
Rebuild the lattice and the element assignment from scratch."""
import numpy as np
from itertools import combinations, permutations
from collections import Counter

# --- rebuild aufbau independently ---
AUF=[(n,l) for s in range(1,20) for n in range(1,20) for l in range(0,5)
     if n+l==s and l<=n-1]
AUF=sorted(set(AUF), key=lambda c:(c[0]+c[1], c[0]))
CAP=lambda l: 2*(2*l+1)

def valence(Z):
    """valence (n,l,k) by strict aufbau, independent implementation"""
    rem=Z; last=None
    for (n,l) in AUF:
        t=min(rem, CAP(l))
        if t>0: last=(n,l,t)
        rem-=t
        if rem<=0: break
    return last

E2={Z: valence(Z) for Z in range(1,119)}
# cross-check against the module used throughout
import eldata as ed
mismatch=[z for z in range(1,119) if E2[z]!=ed.E[z]]
print("="*78); print("AUDIT 0 — element assignment"); print("="*78)
print(f"  independent aufbau vs eldata.E: {len(mismatch)} mismatches")
if mismatch:
    for z in mismatch[:10]: print(f"    Z={z} {ed.SYM[z]}: indep {E2[z]} vs module {ed.E[z]}")
    print("  NOTE: eldata.E uses IDEALISED configurations (no anomalies).")
    print("  Verify the independent version reproduces the same set of cells:")
    print(f"    same 118 cells? {set(E2.values())==set(ed.E.values())}")

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
occ=set(ed.E.values())
print()
print("="*78); print("AUDIT 1 — cell census"); print("="*78)
void=sum(1 for n in range(1,8) for l in range(0,5) for k in range(1,19) if l>=n)
react=sum(1 for n in range(1,8) for l in range(0,5) for k in range(1,19)
          if l<n and k>CAP(l))
res=sum(1 for c in L if c not in occ)
print(f"  |Λ| admissible          = {len(L):>4}   claim 210   {'OK' if len(L)==210 else 'FAIL'}")
print(f"  occupied                = {len(occ):>4}   claim 118   {'OK' if len(occ)==118 else 'FAIL'}")
print(f"  reserved (admis, empty) = {res:>4}   claim  92   {'OK' if res==92 else 'FAIL'}")
print(f"  void (ℓ≥n)              = {void:>4}   claim 180   {'OK' if void==180 else 'FAIL'}")
print(f"  reactive (k>cap)        = {react:>4}   claim 240   {'OK' if react==240 else 'FAIL'}")
print(f"  total 7×5×18            = {void+react+res+len(occ):>4}   claim 630   "
      f"{'OK' if void+react+res+len(occ)==630 else 'FAIL'}")

print()
print("="*78); print("AUDIT 2 — 2n² shell capacity"); print("="*78)
ok=True
for n in range(1,8):
    s=sum(CAP(l) for l in range(0,min(n,5)))
    exp=2*n*n if n<=5 else None
    tag='OK' if (n<=5 and s==2*n*n) else ('truncated by ℓ≤4' if n>5 else 'FAIL')
    if n<=5 and s!=2*n*n: ok=False
    print(f"    n={n}: Σ2(2ℓ+1) = {s:>3}   2n² = {2*n*n:>3}   {tag}")
print(f"  claim '2n² exactly' holds for n ≤ 5 only: {'OK' if ok else 'FAIL'}")
print("  ⚠ PAPER CLAIM CHECK: the abstract says 'counting cells at fixed n")
print("    returns the Pauli capacities 2n² exactly'. TRUE only for n≤5;")
print("    n=6,7 give 50 not 72/98 because of the ℓ≤4 ceiling.")

print()
print("="*78); print("AUDIT 3 — closure under join and meet"); print("="*78)
S=set(L)
jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
bj=sum(1 for a,b in combinations(L,2) if jn(a,b) not in S)
bm=sum(1 for a,b in combinations(L,2) if mt(a,b) not in S)
print(f"  pairs tested: {len(L)*(len(L)-1)//2}")
print(f"  join failures {bj}, meet failures {bm}   {'OK' if bj==bm==0 else 'FAIL'}")
print(f"  minimum element: {min(L)}   {'OK — hydrogen' if min(L)==(1,0,1) else 'FAIL'}")
print(f"  maximum element: {max(L)}")