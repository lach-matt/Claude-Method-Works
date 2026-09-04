import numpy as np, random
from itertools import product, permutations
random.seed(41)
print("="*86)
print("  IS 2-D REORDERABILITY THE TOTALLY-BALANCED MATRIX PROBLEM?")
print("="*86)
print("""
  A 2-D cell set X ⊆ A₁ × A₂ is REORDERABLE if some ordering of each
  alphabet makes X closed under its own recovered monotone bounds.

  **Closed under two monotone bounds in 2-D means the 1s of the incidence
  matrix form a STAIRCASE** — a Young-diagram region, rows and columns
  each an initial segment.

  **A 0-1 matrix reorderable to a staircase is exactly a Γ-FREE matrix**,
  and 'reorderable to Γ-free' is the definition of TOTALLY BALANCED.

  Total balancedness is decidable in polynomial time (Lubiw 1987;
  Hoffman–Kolen–Sakarovitch 1985). **If the equivalence holds, §23.4's
  open question has a poly answer at d = 2.**
""")
def closed_2d(M):
    """is the 0-1 matrix M a staircase in the GIVEN order?"""
    r,c=M.shape
    for i in range(r):
        row=M[i]
        ones=np.where(row==1)[0]
        if len(ones) and not np.array_equal(ones,np.arange(len(ones))): return False
    for j in range(c):
        col=M[:,j]
        ones=np.where(col==1)[0]
        if len(ones) and not np.array_equal(ones,np.arange(len(ones))): return False
    return True
def reorderable_bruteforce(M):
    r,c=M.shape
    for pr in permutations(range(r)):
        Mr=M[list(pr),:]
        for pc in permutations(range(c)):
            if closed_2d(Mr[:,list(pc)]): return True
    return False
def has_gamma(M):
    """Γ = [[1,1],[1,0]] as a submatrix in the GIVEN order"""
    r,c=M.shape
    for i in range(r):
        for j in range(i+1,r):
            for a in range(c):
                for b in range(a+1,c):
                    sub=[M[i,a],M[i,b],M[j,a],M[j,b]]
                    if sub==[1,1,1,0]: return True
    return False
def totally_balanced(M):
    """reorderable to Γ-free — brute force for small M"""
    r,c=M.shape
    for pr in permutations(range(r)):
        Mr=M[list(pr),:]
        for pc in permutations(range(c)):
            if not has_gamma(Mr[:,list(pc)]): return True
    return False
print("  %6s%14s%18s%12s"%("size","reorderable","totally balanced","agree"))
print("  "+"-"*52)
agree=0; tot=0; disagree=[]
for r,c in [(3,3),(3,4),(4,4)]:
    for trial in range(60):
        M=np.random.randint(0,2,(r,c))
        a=reorderable_bruteforce(M); b=totally_balanced(M)
        tot+=1; agree+= (a==b)
        if a!=b and len(disagree)<4: disagree.append((M.copy(),a,b))
    print("  %6s%14s%18s%12s"%("%dx%d"%(r,c),"—","—","%d/60"%sum(1 for _ in range(0))))
print("\n     total tested : %d"%tot)
print("     agree        : %d  (%.1f%%)"%(agree,100*agree/tot))
if disagree:
    print("\n     DISAGREEMENTS:")
    for M,a,b in disagree:
        print("       reorderable=%s  totally_balanced=%s"%(a,b))
        print(M); print()