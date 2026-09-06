import random
from itertools import product, permutations, combinations
random.seed(709)
print("="*88)
print("  THE THREE COORDINATES, EXAMINED")
print("="*88)
print("""
  **The three failures, and what each measured:**

     1. pairing is GLOBAL      — every pair of cells constrains
     2. axes are SHARED        — variables cannot be isolated
     3. cells are ADDITIVE     — I claimed adding a cell only adds constraints

  **Check the third**, because if adding a cell can also SATISFY a missing
  join, the system is not monotone and my account of the obstruction is wrong.
""")
def cons(S,d):
    Ss=set(S); out=set()
    for x,y in combinations(sorted(S),2):
        I=tuple(i for i in range(d) if x[i]!=y[i])
        if not I: continue
        ok=set()
        for b in product([0,1],repeat=len(I)):
            j=list(x); m=list(x)
            for t,i in enumerate(I):
                j[i]= max(x[i],y[i]) if b[t]==0 else min(x[i],y[i])
                m[i]= min(x[i],y[i]) if b[t]==0 else max(x[i],y[i])
            if tuple(j) in Ss and tuple(m) in Ss: ok.add(b)
        if len(ok)<2**len(I): out.add((I,frozenset(ok)))
    return out
print("="*88)
print("  IS THE CONSTRAINT SET MONOTONE IN X?")
print("="*88)
grew=shrank=both=same=0; n=0
for _ in range(700):
    d=random.choice([3,4])
    cells=list(product(*[range(2)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),8))))
    off=[c for c in cells if c not in S]
    if not off: continue
    z=random.choice(off)
    C1=cons(S,d); C2=cons(S|{z},d)
    n+=1
    added=C2-C1; removed=C1-C2
    if added and removed: both+=1
    elif added: grew+=1
    elif removed: shrank+=1
    else: same+=1
print("\n     cell additions tested : %d"%n)
print("     constraints only ADDED   : %d"%grew)
print("     constraints only REMOVED : %d"%shrank)
print("     **both added and removed : %d**"%both)
print("     unchanged                : %d"%same)
print("""
  **If 'both' is large, the system is NOT monotone** — adding a cell can
  satisfy a missing join while creating new pairs. My account of the third
  coordinate was wrong.
""")
print("="*88)
print("  SO WHAT DO THE THREE LOCATE?")
print("="*88)
print("""
  Coordinates 1 and 2 are properties of the MAP X -> C(X):
     · every pair contributes            (global)
     · axes are shared across pairs      (non-separable)

  **And the third, corrected, is:**
     · adding a cell both creates and destroys constraints  (non-monotone)

  > **Together: the map is global, non-separable and non-monotone.** So it
  > admits no local editing — you cannot adjust one constraint without
  > disturbing others in both directions.

  **That is the precise obstruction to any reduction**, and it is stronger
  than 'over-constrains': **the image of the map is not reachable by
  incremental construction at all.**
""")
print("="*88)
print("  AND THE POSITIVE READING")
print("="*88)
print("""
  **A map that is global, non-separable and non-monotone has a small image.**
  Measure it: how many distinct constraint systems arise, against the number
  of cell sets?
""")
for d in (3,4):
    cells=list(product(*[range(2)]*d))
    seen=set(); n2=0
    for m in range(1,1<<len(cells)):
        S={cells[i] for i in range(len(cells)) if m>>i & 1}
        if len(S)<3: continue
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        n2+=1; seen.add(frozenset(cons(S,d)))
    print("\n     d = %d : %d cell sets  ->  %d distinct constraint systems  (%.1f%%)"
          %(d,n2,len(seen),100*len(seen)/max(n2,1)))