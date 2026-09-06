import numpy as np, eldata as ed
from collections import Counter

print("="*66)
print("PERIOD LENGTHS AS MADELUNG SLICES  (unbounded lattice)")
print("="*66)
# use large n so the 7-shell truncation doesn't distort
L=[(n,l,k) for n in range(1,40) for l in range(0,n) for k in range(1,2*(2*l+1)+1)]
c=Counter(n+l for n,l,k in L)
seq=[c[i] for i in range(1,16)]
print("  cells per Madelung level (n+ℓ = 1..15):")
print("   ",seq)
print("  observed period lengths of the periodic system:")
print("    [2, 8, 8, 18, 18, 32, 32, 50, 50, ...]")
print()
# the doubling structure
print("  Level sizes come in equal consecutive pairs:")
for i in range(0,12,2):
    print(f"    n+ℓ = {i+1},{i+2}:  {seq[i]}, {seq[i+1]}   "
          f"{'← pair' if seq[i]==seq[i+1] else '← MISMATCH'}")
print()
print("  This pairing IS the reason periods repeat their lengths.")
print("  In the 2D table it must be imposed by layout; here it is a")
print("  counting fact about parallel slices of Λ.")

print()
print("="*66)
print("JANET LEFT-STEP TABLE  —  the closest existing relative")
print("="*66)
print("  Janet (1929) reorders the table by (n+ℓ) blocks, giving")
print("  period lengths 2,2,8,8,18,18,32,32 and placing He over Be.")
print("  The Lach lattice generates exactly this ordering as the")
print("  Madelung functional f = n+ℓ sweeping through Λ.")
print("  → Janet's table is the 2D projection of Λ along f.")
print("     This is a REAL correspondence, not a loose analogy:")
print("     Janet's blocks = level sets of a linear functional on Λ.")

print()
print("="*66)
print("WHERE THE FIELD EQUATION SITS")
print("="*66)
print("  Ψ±(t) = √2 sin(Ωt+π/4) Σ|n,ℓ,k⟩  assigns every element the")
print("  SAME time dependence — the sum carries no element label and")
print("  the prefactor is element-independent. Check:")
import sympy as sp
t,Om=sp.symbols('t Omega',positive=True)
c0=sp.cos(Om*t); c1=sp.sin(Om*t)/sp.sqrt(2)
norm=sp.simplify(c0**2+2*c1**2)
print(f"    normalisation c₀²+2c₁² = {norm}   (constant ⇒ valid)")
comb=sp.simplify(sp.cos(Om*t)+sp.sin(Om*t)-sp.sqrt(2)*sp.sin(Om*t+sp.pi/4))
print(f"    cos+sin−√2sin(·+π/4) = {comb}   (identity holds)")
print()
print("  So Eq.(4) is mathematically sound but element-independent:")
print("  all 118 elements share one envelope. The element-specific")
print("  content lives entirely in ΔQ and σ²(t), not in Ψ±.")
print("  → The equation is a normalisation statement about the lattice,")
print("     not a dynamical law distinguishing elements.")