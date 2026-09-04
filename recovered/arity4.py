import random
from itertools import product, permutations, combinations
from collections import Counter
random.seed(673)
print("="*88)
print("  ARITY 4 IN XOR COORDINATES — WHICH CONSTRAINTS ARISE?")
print("="*88)
print("""
  An arity-k complement-closed constraint becomes an arity-(k−1) constraint on
  XOR variables t_1 = s_1⊕s_2, …, t_{k−1} = s_{k−1}⊕s_k. **For k = 4 that is
  an arity-3 constraint on {0,1}³ — 2⁸ = 256 possible allowed-sets.**

  **The question is which of the 256 actually arise from cell sets, and
  whether each is expressible as a conjunction of 2-clauses.**
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def constraints(S,d):
    A=alph(S,d); Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        if not I: continue
        ok=set()
        for bits in product([0,1],repeat=len(I)):
            j=list(x); m=list(x)
            for t,i in enumerate(I):
                u,v=sorted((x[i],y[i]))
                j[i]= v if bits[t]==0 else u
                m[i]= u if bits[t]==0 else v
            if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
        if len(ok)<2**len(I): out.append((len(I),frozenset(ok)))
    return out
def to_xor(A,k):
    return frozenset(tuple(b[i]^b[i+1] for i in range(k-1)) for b in A)
def is_2sat_expressible(T,m):
    """is T the solution set of a 2-CNF on m variables?"""
    # the 2-CNF closure of T: keep clauses satisfied by every member of T
    cl=[]
    for i in range(m):
        for j in range(i+1,m):
            for si in (0,1):
                for sj in (0,1):
                    if all(not(t[i]==si and t[j]==sj) for t in T):
                        cl.append((i,si,j,sj))
    for i in range(m):
        for si in (0,1):
            if all(t[i]!=si for t in T): cl.append((i,si,i,si))
    sol=set()
    for t in product([0,1],repeat=m):
        if all(not(t[i]==si and t[j]==sj) for i,si,j,sj in cl): sol.add(t)
    return sol==set(T)
print("="*88)
print("  ENUMERATE THE ARITY-4 CONSTRAINTS THAT OCCUR")
print("="*88)
seen4=Counter(); seen3=Counter(); seen5=Counter()
for _ in range(1400):
    d=random.choice([4,5]); a=2
    cells=list(product(*[range(a)]*d))
    S=set(random.sample(cells,random.randint(4,min(len(cells),12))))
    for k,A in constraints(S,d):
        if k==3: seen3[to_xor(A,3)]+=1
        elif k==4: seen4[to_xor(A,4)]+=1
        elif k==5: seen5[to_xor(A,5)]+=1
print("\n     distinct arity-3 XOR constraints (on 2 vars) : %d of %d possible"%(len(seen3),2**4))
print("     distinct arity-4 XOR constraints (on 3 vars) : %d of %d possible"%(len(seen4),2**8))
print("     distinct arity-5 XOR constraints (on 4 vars) : %d of %d possible"%(len(seen5),2**16))
print("="*88)
print("  ARE THEY 2-SAT EXPRESSIBLE?")
print("="*88)
for k,seen,m in [(3,seen3,2),(4,seen4,3),(5,seen5,4)]:
    if not seen: continue
    ok=sum(1 for T in seen if is_2sat_expressible(T,m))
    tot=len(seen)
    wt=sum(seen[T] for T in seen if is_2sat_expressible(T,m)); wtot=sum(seen.values())
    print("\n     arity %d -> %d XOR vars : %d of %d distinct are 2-SAT expressible"%(k,m,ok,tot))
    print("        by occurrence : %d of %d  (%.1f%%)"%(wt,wtot,100*wt/max(wtot,1)))
    bad=[T for T in seen if not is_2sat_expressible(T,m)]
    if bad:
        print("        NOT expressible, most common:")
        for T in sorted(bad,key=lambda t:-seen[t])[:3]:
            print("           %s   (%d occurrences)"%(sorted(T),seen[T]))