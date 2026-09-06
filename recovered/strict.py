import eldata as ed
from collections import Counter
CAP=lambda l:2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))

# Measured ground-state configurations, valence = the differentiating subshell
# as actually observed (NIST / standard tables). Only the 20 anomalies differ
# from the idealised assignment; everything else follows aufbau.
MEAS_OVERRIDE={
 24:(3,2,5),  # Cr [Ar]3d5 4s1
 29:(3,2,10), # Cu [Ar]3d10 4s1
 41:(4,2,4),  # Nb [Kr]4d4 5s1
 42:(4,2,5),  # Mo [Kr]4d5 5s1
 44:(4,2,7),  # Ru [Kr]4d7 5s1
 45:(4,2,8),  # Rh [Kr]4d8 5s1
 46:(4,2,10), # Pd [Kr]4d10
 47:(4,2,10), # Ag [Kr]4d10 5s1
 57:(5,2,1),  # La [Xe]5d1 6s2
 58:(4,3,1),  # Ce [Xe]4f1 5d1 6s2
 64:(4,3,7),  # Gd [Xe]4f7 5d1 6s2
 78:(5,2,9),  # Pt [Xe]4f14 5d9 6s1
 79:(5,2,10), # Au [Xe]4f14 5d10 6s1
 89:(6,2,1),  # Ac [Rn]6d1 7s2
 90:(6,2,2),  # Th [Rn]6d2 7s2
 91:(5,3,2),  # Pa [Rn]5f2 6d1 7s2
 92:(5,3,3),  # U  [Rn]5f3 6d1 7s2
 93:(5,3,4),  # Np [Rn]5f4 6d1 7s2
 96:(5,3,7),  # Cm [Rn]5f7 6d1 7s2
 103:(7,1,1), # Lr [Rn]5f14 7s2 7p1
}
STRICT=dict(ed.E); STRICT.update(MEAS_OVERRIDE)
print("="*80)
print("DOES THE DOWN-SET PROPERTY SURVIVE A STRICTLY MEASURED CONVENTION?")
print("="*80)
for nm,cfg in [('module (mixed)',ed.E),('strictly measured',STRICT)]:
    occ=set(cfg.values())
    viol=[(y,x) for x in occ for y in L if leq(y,x) and y not in occ]
    print(f"\n  {nm}: {len(occ)} distinct cells, down-set violations {len(viol)}")
    if viol:
        seen=set()
        for y,x in sorted(viol):
            if y in seen: continue
            seen.add(y)
            print(f"      missing cell {y}  (below occupied {x})")
        print(f"      distinct missing cells: {len(seen)}")

print()
print("="*80)
print("WHERE THE HOLES APPEAR — the 3d and 4d columns under strict measurement")
print("="*80)
for (n,l),nm in [((3,2),'3d'),((4,2),'4d'),((5,2),'5d'),((4,3),'4f'),((5,3),'5f')]:
    ks=sorted({k for z,(a,b,k) in STRICT.items() if (a,b)==(n,l)})
    full=list(range(1,CAP(l)+1))
    miss=[k for k in full if k not in ks]
    print(f"  {nm}: occupied k = {ks}")
    print(f"      missing  k = {miss or 'none'}")
    if miss:
        for k in miss:
            print(f"        k={k}: no element has exactly {k} electrons in {nm}")