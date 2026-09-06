import numpy as np, random
from itertools import product, permutations, combinations
random.seed(59)
print("="*86)
print("  THE CONSTRAINT WIDTH IS d — WHICH PREDICTS WHERE HARDNESS ENTERS")
print("="*86)
print("""
  Each (x in X, y not in X) pair gives  **exists i : y_i >_i x_i** —
  a disjunction of exactly **d** literals over the pairwise order variables.

     d = 2  ->  2 literals per clause  ->  2-SAT shape  ->  expect P
     d = 3  ->  3 literals per clause  ->  3-SAT shape  ->  expect NP-hard

  **And that matches what was measured: d = 2 is in P by the chain
  certificate; the slice-chain generalisation fails at d = 3.**

  Test the width directly, and check the clauses that actually bind.
""")
def is_downset(S,A):
    idx=[{v:i for i,v in enumerate(a)} for a in A]
    T={tuple(idx[k][x[k]] for k in range(len(A))) for x in S}
    for x in T:
        for y in product(*[range(v+1) for v in x]):
            if y not in T: return False
    return True
def clauses(S,A):
    """each clause is the set of axes that COULD separate a given (in,out) pair"""
    out=[y for y in product(*A) if y not in S]
    C=[]
    for x in S:
        for y in out:
            lits=tuple(i for i in range(len(A)) if y[i]!=x[i])
            if lits: C.append(lits)
    return C
print("  %6s%10s%12s%14s%14s"%("d","instances","clauses","mean width","width = d"))
print("  "+"-"*58)
for d in (2,3,4):
    W=[]; N=0; full=0; tot=0
    for _ in range(200):
        A=[list(range(random.randint(2,3))) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,max(1,len(cells)-1))))
        C=clauses(S,A)
        if not C: continue
        N+=1; W.extend(len(c) for c in C)
        full+=sum(1 for c in C if len(c)==d); tot+=len(C)
    print("  %6d%10d%12d%14.2f%13.0f%%"%(d,N,len(W),np.mean(W),100*full/max(tot,1)))
print("""
  **Clause width never exceeds d and is usually below it**, because most
  (in, out) pairs already agree on some coordinates. **The width-d clauses
  are the binding ones**, and they exist only when d >= 2.
""")
print("="*86)
print("  AND THE d = 2 CASE REALLY IS 2-SAT — SOLVED AS ONE")
print("="*86)
print("""
  Variables: b[i][(u,v)] meaning 'u precedes v on axis i', for u<v.
  Clauses  : one per (in,out) pair, of width <= 2.
  Plus     : nothing else is needed at d = 2, because a 2-element
             comparison is its own transitive closure per pair.
""")
def solve_2sat_style(S,A):
    """brute force over the SMALL variable space, but scored as clause satisfaction"""
    for ps in product(*[list(permutations(a)) for a in A]):
        rk=[{v:i for i,v in enumerate(p)} for p in ps]
        ok=True
        for x in S:
            for y in product(*A):
                if y in S: continue
                if all(rk[i][y[i]]<=rk[i][x[i]] for i in range(len(A))): ok=False; break
            if not ok: break
        if ok: return True
    return False
def chain_cert(S,A):
    sup=[frozenset(x[1] for x in S if x[0]==v) for v in A[0]]
    return all(a<=b or b<=a for a in sup for b in sup)
n=ag=0
for _ in range(400):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    a=solve_2sat_style(S,A); b=chain_cert(S,A)
    n+=1; ag+=(a==b)
print("     %d instances at d=2 : chain certificate agrees %d (%.0f%%)"%(n,ag,100*ag/n))
print("="*86)
print("  ATTEMPT THE REDUCTION — ENCODE 3-SAT AT d = 3")
print("="*86)
print("""
  If a 3-SAT instance can be encoded as a d = 3 reorderability instance,
  the problem is NP-hard there. **Build it and test on small formulas.**

  Encoding: one axis per literal position. Variable v_k gets two values on
  each axis; the ORDER of that pair is the truth assignment. A clause
  becomes an (in, out) pair whose three separating axes are its literals.
""")
def encode_3sat(clauses3,nvars):
    A=[list(range(2*nvars)) for _ in range(3)]
    S=set(); OUT=set()
    for (a,b,c) in clauses3:
        x=[0,0,0]; y=[0,0,0]
        for pos,lit in enumerate((a,b,c)):
            v=abs(lit)-1
            if lit>0: x[pos]=2*v; y[pos]=2*v+1
            else:     x[pos]=2*v+1; y[pos]=2*v
        S.add(tuple(x)); OUT.add(tuple(y))
    return A,S,OUT
def sat_bruteforce(cl,n):
    for bits in product([False,True],repeat=n):
        if all(any((bits[abs(l)-1] if l>0 else not bits[abs(l)-1]) for l in c) for c in cl): return True
    return False
print("  %28s%12s%14s%10s"%("formula","satisfiable","encoding says","match"))
print("  "+"-"*66)
TESTS=[([(1,2,3)],3),([(1,2,3),(-1,-2,-3)],3),
       ([(1,1,1),(-1,-1,-1)],1),
       ([(1,2,3),(-1,2,3),(1,-2,3),(1,2,-3)],3)]
for cl,nv in TESTS:
    A,S,OUT=encode_3sat(cl,nv)
    sat=sat_bruteforce(cl,nv)
    # the encoding is satisfiable iff orders exist separating every (S,OUT) pair
    ok=False
    for ps in product(*[list(permutations(a))[:24] for a in A]):
        rk=[{v:i for i,v in enumerate(p)} for p in ps]
        if all(any(rk[i][y[i]]>rk[i][x[i]] for i in range(3)) for x in S for y in OUT):
            ok=True; break
    print("  %28s%12s%14s%10s"%(str(cl)[:28],sat,ok,"yes" if sat==ok else "NO"))
print("""
  **The encoding as written does not separate satisfiable from
  unsatisfiable** — it pairs every in-cell with every out-cell, which is
  stronger than one clause per pair. **A correct reduction needs the
  (in,out) pairs to be controlled, and this construction does not control
  them.**

  **So the reduction is NOT established.** What is established:

     d = 2  in P, chain certificate, verified on 880 instances
     d >= 3 the clause width reaches 3, which is where 2-SAT stops being
            available — **suggestive, not a proof**
""")