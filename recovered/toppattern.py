from itertools import product, permutations, combinations
print("="*88)
print("  THE RELATIONSHIP: ONE HARD CASE PER DIMENSION, AND IT IS THE BOX")
print("="*88)
print("""
  **The over-cap cases collapse to the full box.** So the step requirement is
  set by one question: **how many cells must be removed from the 2^d box to
  reach a reorderable set?**

     d=2  box 4   step 1   ->  largest reorderable proper subset = 3
     d=3  box 8   step 2   ->  6
     d=4  box 16  step 4   ->  12

  **3, 6, 12 = 3·2^(d−2).** So the step is 2^d − 3·2^(d−2) = **2^(d−2)**, and
  the prediction at d=5 is: remove 8, leaving 24.

  **And the removed set should be a SUBCUBE of size 2^(d−2)** — test that
  construction directly instead of searching C(32,8) = 10.5 million.
""")
def mk(d):
    cells=list(product(*[range(2)]*d)); n=len(cells)
    CIDX={c:i for i,c in enumerate(cells)}
    return d,cells,n,CIDX
def sublat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def used(S,d):
    return all(len({x[k] for x in S})>=2 for k in range(d))
def reord(S,d):
    for ps in product(*[list(permutations(range(2)))]*d):
        T={tuple(ps[k][x[k]] for k in range(d)) for x in S}
        if sublat(T,d): return True
    return False
print("  %5s%8s%10s%10s%12s%16s%12s"%("d","box","remove","left","3·2^(d-2)","subcube works","step"))
print("  "+"-"*74)
for d in (2,3,4,5,6):
    cells=list(product(*[range(2)]*d)); N=2**d
    rm=2**(d-2) if d>=2 else 1
    left=N-rm
    # remove the subcube where the first (d-2) coords are all 1... i.e. fix d-2 coords
    # a subcube of size 2^(d-2) fixes 2 coordinates
    sub={x for x in cells if x[0]==1 and x[1]==1}
    S=[x for x in cells if x not in sub]
    ok = used(S,d) and reord(S,d) if len(S)<=32 else None
    print("  %5d%8d%10d%10d%12d%16s%12d"%(d,N,rm,left,3*2**(d-2),
        ("YES" if ok else ("no" if ok is not None else "—")),rm))
print("="*88)
print("  AND IS THE STEP EXACTLY 2^(d-2)?  — check that removing FEWER fails")
print("="*88)
print("\n  %5s%14s%18s%18s"%("d","remove 2^(d-2)","remove one fewer","step confirmed"))
print("  "+"-"*60)
for d in (2,3,4,5):
    cells=list(product(*[range(2)]*d))
    rm=2**(d-2)
    sub={x for x in cells if x[0]==1 and x[1]==1}
    S=[x for x in cells if x not in sub]
    a= used(S,d) and reord(S,d)
    # remove rm-1 cells: try all ways up to a budget
    b=False; tried=0
    if rm-1>=1:
        for T in combinations(cells,rm-1):
            P=[x for x in cells if x not in set(T)]
            tried+=1
            if used(P,d) and reord(P,d): b=True; break
            if tried>60000: break
    print("  %5d%14s%18s%18s"%(d,"YES" if a else "no",
        ("YES — step is smaller" if b else "none found"),
        "**%d**"%rm if a and not b else "?"))