import random
from itertools import product, permutations, combinations
random.seed(727)
print("="*90)
print("  THE TEST, RE-POSED")
print("="*90)
print("""
  **The ill-posed version.** 'Find a non-reorderable X with width(J(X)) ≤ d.'
  For a non-reorderable X there is no valid order, **so J(X) does not exist.**
  The condition cannot be violated because it cannot be evaluated.

  **What Dilworth actually gives.** For an ABSTRACT distributive lattice L, a
  chain decomposition of J(L) into w = width(J(L)) chains exists, and by
  Larson each gives a TIGHT embedding into w chains. **So width ≤ d IS
  sufficient — for abstract lattices.**

  **So the residue is not the width. It is the MATCHING:** the axis partitions
  are GIVEN, and they must coincide with a chain decomposition of J(X).

     reorderable  ⟺  X is a distributive lattice under some labelling
                     AND the given axis partitions form a chain decomposition
                     of J(X)

  **Test the second clause on reorderable instances.**
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
def joinirr(T,d):
    Ts=set(T); J=[]
    for x in Ts:
        below=[y for y in Ts if all(y[i]<=x[i] for i in range(d)) and y!=x]
        if not below: continue
        if tuple(max(y[i] for y in below) for i in range(d))!=x: J.append(x)
    return J
def is_chain(T,d):
    return all(all(x[i]<=y[i] for i in range(d)) or all(y[i]<=x[i] for i in range(d))
               for x,y in combinations(T,2))
print("="*90)
print("  TEST — DO THE AXIS PARTITIONS FORM A CHAIN DECOMPOSITION OF J(X)?")
print("="*90)
print("""
  For a reorderable X in its valid order, group J(X) by which axis 'carries'
  each join-irreducible — the axis where it exceeds the bottom. **Check each
  group is a CHAIN and that they partition J(X).**
""")
n=0; okchain=0; okcount=0; sizes=[]
bad=[]
for _ in range(700):
    d=random.choice([2,3]); a=random.choice([2,3,4])
    cells=list(product(*[range(a)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),8))))
    if any(len({x[k] for x in S})<2 for k in range(d)): continue
    A=alph(S,d); T=None
    for ps in product(*[list(permutations(x)) for x in A]):
        R=relab(S,[list(p) for p in ps],d)
        if lat(R,d): T=R; break
    if T is None: continue
    n+=1
    J=joinirr(T,d)
    bot=tuple(min(x[i] for x in T) for i in range(d))
    grp={}
    for x in J:
        ax=[i for i in range(d) if x[i]>bot[i]]
        grp.setdefault(tuple(ax),[]).append(x)
    single=all(len(k)==1 for k in grp)
    allch=all(is_chain(v,d) for v in grp.values())
    okchain+= (single and allch)
    AT=[sorted({x[i] for x in T}) for i in range(d)]
    exp=sum(len(x)-1 for x in AT)
    okcount+= (len(J)==exp)
    sizes.append((len(J),exp))
    if not (single and allch) and len(bad)<3: bad.append((sorted(T),sorted(grp)))
print("\n     reorderable instances                       : %d"%n)
print("     each join-irreducible carried by ONE axis,")
print("     and each axis-group is a CHAIN               : %d  (%.1f%%)"%(okchain,100*okchain/max(n,1)))
print("     |J(X)| = Σ(|A_i| − 1)                        : %d  (%.1f%%)"%(okcount,100*okcount/max(n,1)))
if bad:
    print("\n     counterexamples:")
    for T,g in bad: print("        %s   groups %s"%(str(T)[:40],g))
print("="*90)
print("  WHAT THIS MEANS FOR THE PROCEDURE")
print("="*90)
print("""
  **If both hold at 100%, reorderability is exactly:**

     1. some labelling makes X a distributive lattice        (the hard part)
     2. |J(X)| = Σ(|A_i| − 1), and the axis groups are chains (a check)

  > **And clause 1 is the original problem.** Dilworth supplies the embedding
  > once the lattice structure is known; **it does not supply the lattice
  > structure.** So the reduction places the problem and does not solve it.
""")