import numpy as np, eldata as ed
from scipy import stats
from collections import Counter
print("="*80)
print("SYSTEM 1 — QUANTUM SORTING")
print("="*80)
print("""  Measurement basis: the quantum numbers of the ground-state configuration.
  Canonical orderings:
    Q1  Madelung / aufbau:  sort by (n+ℓ, n)          [Madelung 1936]
    Q2  Janet left-step:    blocks of constant n+ℓ    [Janet 1929]
    Q3  strict shell order: sort by (n, ℓ, k)         [naive]
  Observable anchors: spectroscopic term symbols, ionisation thresholds,
  orbital angular momentum. All three are ORDINAL constructions on (n,ℓ,k).""")
zs=sorted(ed.E)
def rank_of(key): 
    o=sorted(zs,key=key); return {z:i for i,z in enumerate(o)}
Q1=rank_of(lambda z:(ed.E[z][0]+ed.E[z][1], ed.E[z][0], ed.E[z][2]))
Q3=rank_of(lambda z:(ed.E[z][0], ed.E[z][1], ed.E[z][2]))
LACH=rank_of(lambda z: sum(ed.E[z]))    # Λ rank functional n+ℓ+k
print()
print(f"  {'ordering':<26}{'Kendall τ vs Z':>16}{'inversions':>12}")
print("  "+"-"*56)
for nm,R in [('Madelung (n+ℓ, n)',Q1),('strict (n,ℓ,k)',Q3),('Λ rank n+ℓ+k',LACH)]:
    r=[R[z] for z in zs]
    tau,_=stats.kendalltau(zs,r)
    inv=sum(1 for i in range(len(zs)) for j in range(i+1,len(zs)) if r[i]>r[j])
    print(f"  {nm:<26}{tau:>16.4f}{inv:>12}")
print()
print("  Λ's rank functional n+ℓ+k is NOT the Madelung functional n+ℓ.")
print("  They differ by the k term. Effect on ordering:")
same=sum(1 for z in zs if Q1[z]==LACH[z])
print(f"    positions where Madelung and Λ-rank agree: {same}/118")
tau,_=stats.kendalltau([Q1[z] for z in zs],[LACH[z] for z in zs])
print(f"    Kendall τ between them: {tau:.4f}")
print()
print("="*80)
print("QUANTUM SORTING — WHERE IT BREAKS")
print("="*80)
ANOM={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
print(f"  Madelung inversions vs Z: 28  (computed earlier)")
print(f"  documented anomalous ground states: {len(ANOM)}")
# do the Madelung inversions coincide with the anomalies?
o=sorted(zs,key=lambda z:(ed.E[z][0]+ed.E[z][1], ed.E[z][0], ed.E[z][2]))
misplaced=set(z for i,z in enumerate(o) if z!=zs[i])
print(f"  elements misplaced by Madelung: {len(misplaced)}")
ov=misplaced & ANOM
print(f"  overlap with documented anomalies: {len(ov)} -> {sorted(ed.SYM[z] for z in ov)}")
print(f"  misplaced but NOT anomalous: {len(misplaced-ANOM)}")
print(f"  anomalous but NOT misplaced: {len(ANOM-misplaced)} -> {sorted(ed.SYM[z] for z in ANOM-misplaced)}")