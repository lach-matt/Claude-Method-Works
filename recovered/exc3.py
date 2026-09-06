import eldata as ed
CAP={0:2,1:6,2:10,3:14,4:18}
print("="*78)
print("PRIOR CLAIM CHECK: do actinides reach 5g under excitation?")
print("="*78)
print("""  The 2026 paper's §2.4 asserted: elements with 5f ground states have
  access to 5g since ℓ=4 is valid for n=5. Lattice-admissibility is not
  in question — (5,4,k) satisfies ℓ ≤ n−1. The question is whether any
  actinide actually populates 5g in a documented low-lying state.""")
print()
act=[z for z in ed.E if ed.E[z][0]==5 and ed.E[z][1]==3]
print(f"  elements with 5f ground-state valence: {[ed.SYM[z] for z in act]}")
print()
print("""  What the spectroscopic record shows (NIST ASD, standard compilations):
    • Actinide low-lying configurations involve 5f, 6d, 7s, 7p.
    • The 5g orbital lies far above these — g orbitals have a large
      centrifugal barrier ℓ(ℓ+1)/r² and negligible core penetration,
      so they are hydrogen-like and energetically remote in neutral atoms.
    • No neutral actinide has a documented low-lying 5g configuration.
    • g-orbital occupancy is predicted to begin near Z≈121-125 (Pyykkö's
      extended table places 5g filling in the 'superactinides').

  So the lattice PERMITS (5,4,k) but the physics does not deliver it at
  any known Z. The 2026 claim conflated admissibility with accessibility.""")
print()
print("="*78)
print("BUILDING Λ_exc PROPERLY: WHAT COUNTS AS 'REACHED'?")
print("="*78)
print("""  An excited atom occupies several subshells at once. Na* is
  1s²2s²2p⁶3p¹ — it occupies (2,1,6) AND (3,1,1). So an excited
  configuration is not a point of Λ but a SET of points.

  Two defensible definitions:
    D1  Λ_exc = { cells occupied by SOME subshell of SOME documented
                  configuration of SOME element }
    D2  Λ_exc = { valence cells of documented excited states }, i.e. the
                  analogue of how ground states were assigned in Part I

  D1 is much larger and includes every inner shell of every atom.
  Let us compute both.""")
print()
ground=set(ed.E[z] for z in ed.E)

# D1: every filled subshell of every ground-state atom (inner shells included)
AUF=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
def full_config(Z):
    rem=Z; cfg=[]
    for (n,l) in AUF:
        c=min(rem,CAP[l])
        if c>0: cfg.append((n,l,c))
        rem-=c
        if rem<=0: break
    return cfg
D1=set()
for z in ed.E:
    for (n,l,c) in full_config(z):
        for k in range(1,c+1): D1.add((n,l,k))
print(f"  D1 (all occupied subshells, all elements): {len(D1)} cells")
print(f"  D1 columns: {sorted(set((n,l) for (n,l,k) in D1))}")
print(f"  ground-state valence set: {len(ground)} cells")
print(f"  D1 ⊇ ground? {ground <= D1}")
print(f"  cells in D1 not in ground: {len(D1-ground)}")