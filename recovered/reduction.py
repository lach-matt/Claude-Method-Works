import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(389)
print("="*86)
print("  ENCODING SAT AT FIXED d = 3, ALPHABETS GROWING")
print("="*86)
print("""
  **The mechanism.** For cells x,y differing on all three axes, the join is
  the corner taking the max on each axis — and WHICH corner that is depends
  on the three relative orders. **Removing a corner from X forbids exactly
  one orientation: a 3-clause.**

  **The limit.** x and y are themselves corners (all-max and all-min), and
  they are in X by construction. **So only MIXED corners can be forbidden**,
  which means the clauses have mixed polarity. That is still NP-hard by the
  standard transformation.

  **The construction.** Variable v_t gets a value pair on each axis. Alphabet
  size grows with the variable count; d stays 3.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d,cap=10**7):
    A=alph(S,d)
    n=int(np.prod([np.math.factorial(len(a)) if False else 1 for a in A]))
    import math
    n=int(np.prod([math.factorial(len(a)) for a in A]))
    if n>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def encode(clauses,nv):
    """one value-pair per variable on each axis; a pair of cells per clause"""
    S=set()
    # value pair for variable t on axis i : (2t, 2t+1)
    for (a,b,c) in clauses:
        vs=[abs(a)-1,abs(b)-1,abs(c)-1]
        sg=[a>0,b>0,c>0]
        lo=tuple(2*vs[i] for i in range(3))
        hi=tuple(2*vs[i]+1 for i in range(3))
        S.add(lo); S.add(hi)
        # all corners except the one encoding the FORBIDDEN assignment
        for bits in product([0,1],repeat=3):
            corner=tuple((2*vs[i]+1) if bits[i] else (2*vs[i]) for i in range(3))
            # forbidden orientation: literal i FALSE for every i
            forbidden=tuple((0 if sg[i] else 1) for i in range(3))
            if bits!=forbidden: S.add(corner)
    return S
def sat_bf(cl,n):
    for bits in product([False,True],repeat=n):
        if all(any((bits[abs(l)-1] if l>0 else not bits[abs(l)-1]) for l in c) for c in cl): return True
    return False
TESTS=[
 ([(1,-2,3)],3),
 ([(1,-2,3),(-1,2,-3)],3),
 ([(1,-2,3),(-1,2,3),(1,2,-3),(-1,-2,-3)],3),
 ([(1,-1,2)],2),
 ([(1,-2,3),(-1,-2,-3),(1,2,3)],3),
]
print("  %34s%12s%14s%10s"%("formula","satisfiable","reorderable","match"))
print("  "+"-"*72)
agree=0; n=0
for cl,nv in TESTS:
    S=encode(cl,nv)
    A=alph(S,3)
    if any(len(a)<2 for a in A): 
        print("  %34s%12s%14s%10s"%(str(cl)[:34],"—","degenerate","—")); continue
    r=reord(S,3)
    if r is None:
        print("  %34s%12s%14s%10s"%(str(cl)[:34],sat_bf(cl,nv),"too large","—")); continue
    s=sat_bf(cl,nv); n+=1; agree+= (s==r)
    print("  %34s%12s%14s%10s"%(str(cl)[:34],s,r,"yes" if s==r else "**NO**"))
print("\n     matches : %d of %d"%(agree,n))
print("="*86)
print("  RANDOM FORMULAS")
print("="*86)
ag=0; tot=0; bad=[]
for _ in range(120):
    nv=random.randint(2,3); m=random.randint(1,3)
    cl=[]
    for _ in range(m):
        vs=random.sample(range(1,nv+1),min(3,nv))
        while len(vs)<3: vs.append(random.randint(1,nv))
        c=tuple(v*random.choice([1,-1]) for v in vs)
        cl.append(c)
    S=encode(cl,nv)
    A=alph(S,3)
    if any(len(a)<2 for a in A): continue
    r=reord(S,3)
    if r is None: continue
    s=sat_bf(cl,nv); tot+=1; ag+= (s==r)
    if s!=r and len(bad)<3: bad.append((cl,s,r))
print("\n     random formulas : %d    encoding agrees : %d  (%.0f%%)"%(tot,ag,100*ag/max(tot,1)))
for cl,s,r in bad: print("       %s  sat=%s reord=%s"%(cl,s,r))
print("""
{0}
  WHAT THIS SETTLES
{0}
""".format("="*86))
print("""  **If the encoding tracks satisfiability, then reorderability at d = 3 is
  NP-hard in the alphabet size**, and the question 'is it polynomial in
  |A|?' is answered: no, unless P = NP.

  **If it does not track, the encoding is wrong** — and the reason will be
  the same one that defeated the earlier attempt: the construction imposes
  constraints the formula does not.
""")