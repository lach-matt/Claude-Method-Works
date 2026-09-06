import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(523)
print("="*88)
print("  CHECKING THE REDUCTION AGAINST THE LAWS")
print("="*88)
print("""
  **C.2.16.3** — a reduced question is still open.
  **C.2.8**    — two independent routes.
  **P23**      — completeness needs every definition identified.

  **The claim:** the d ≥ 3 question can be asked on instances with all
  fibres distinct. **That is a reduction, so two things must be checked:**

     (i)  does the reduction PRESERVE the answer?
     (ii) is the reduced question still open?
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
def reord(S,d,cap=200000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def fibre(S,d,i,u): return frozenset(tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==u)
def quotient(S,d):
    """merge values with IDENTICAL fibres, one axis at a time, to a fixed point"""
    cur=set(S)
    while True:
        A=alph(cur,d); done=True
        for i in range(d):
            g={}
            for u in A[i]: g.setdefault(fibre(cur,d,i,u),[]).append(u)
            for f,vals in g.items():
                if len(vals)>1:
                    keep=vals[0]
                    cur={tuple(keep if (k==i and x[k] in vals) else x[k] for k in range(d)) for x in cur}
                    done=False; break
            if not done: break
        if done: break
    return cur
print("="*88)
print("  (i)  DOES THE QUOTIENT PRESERVE THE ANSWER?")
print("="*88)
print("""
  **Note:** merging ARBITRARY values was measured at 93% preserving. The
  claim is only about merging IDENTICAL fibres. **Test that specifically.**
""")
n=pres=0; ex=[]
for _ in range(1200):
    d=random.choice([2,3]); a=random.choice([2,3,4])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    r1=reord(S,d)
    if r1 is None: continue
    Q=quotient(S,d)
    AQ=alph(Q,d)
    if any(len(x)<2 for x in AQ): continue
    if Q==S: continue                      # nothing merged
    r2=reord(Q,d)
    if r2 is None: continue
    n+=1; pres+= (r1==r2)
    if r1!=r2 and len(ex)<3: ex.append((sorted(S),sorted(Q),r1,r2))
print("     instances where something merged : %d"%n)
print("     **answer preserved : %d  (%.1f%%)**"%(pres,100*pres/max(n,1)))
for S,Q,r1,r2 in ex:
    print("        X=%s r=%s  ->  Q=%s r=%s"%(str(S)[:34],r1,str(Q)[:30],r2))
print("="*88)
print("  (ii)  IS THE REDUCED QUESTION STILL OPEN?")
print("="*88)
print("""
  On instances with all fibres distinct: **is reorderability decidable in
  polynomial time at d ≥ 3?** Nothing established today touches it.

     the characterisation      — still empty
     the decision procedure    — still empty
     the data structure        — still empty
     §13.4 still applies       — projections remain insufficient
     Tucker still applies      — obstructions remain unbounded
     the valid set is now a SET of representatives, not a union of orbits

  > **The reduction removes a trivial degeneracy and leaves every empty cell
  > empty.** By C.2.16.3 it is still open, and by the operational rule the
  > residue must be stated with it:

  **'The problem reduces to fibre-distinct instances, where the valid orders
  are in bijection with the components — and on those instances the
  characterisation, the procedure and the data structure are all still
  missing.'**
""")
print("="*88)
print("  AND WHAT THE REDUCTION DOES BUY")
print("="*88)
n=0; before=[]; after=[]
for _ in range(600):
    d=3; a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    Q=quotient(S,d); AQ=alph(Q,d)
    if any(len(x)<2 for x in AQ): continue
    n+=1
    before.append(int(np.prod([math.factorial(len(x)) for x in A])))
    after.append(int(np.prod([math.factorial(len(x)) for x in AQ])))
print("\n     instances %d"%n)
print("     search space before quotient : median %d"%int(np.median(before)))
print("     after                        : median %d"%int(np.median(after)))
print("     **reduction factor           : median %.1f×**"%np.median([b/max(a2,1) for b,a2 in zip(before,after)]))