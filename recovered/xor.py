import random
from itertools import product, permutations, combinations
random.seed(653)
print("="*88)
print("  THE COORDINATE: THE PROBLEM LIVES ON XOR-DIFFERENCES")
print("="*88)
print("""
  **Every constraint is closed under complementing s|_I.** A function of s|_I
  invariant under complementation depends only on the DIFFERENCES
  s_i ⊕ s_j for i,j ∈ I. **So the problem is a CSP on differences.**

     |I| = 2  ->  one XOR variable  ->  **2-COLOURING of a signed graph**
     |I| ≥ 3  ->  several XORs, tied by t_ij ⊕ t_jk = t_ik

  **That is exactly why d = 2 is polynomial: two cells in two dimensions
  differ on at most two axes, so every constraint is a single XOR — and
  signed-graph 2-colouring is linear time.**

  Verify the invariance, then measure how far the arity-2 part alone decides.
""")
def allowed(Ss,x,y,d):
    I=[i for i in range(d) if x[i]!=y[i]]
    if not I: return None,None
    ok=set()
    for bits in product([0,1],repeat=len(I)):
        j=list(x); m=list(x)
        for t,i in enumerate(I):
            if bits[t]: j[i]=min(x[i],y[i]); m[i]=max(x[i],y[i])
            else:       j[i]=max(x[i],y[i]); m[i]=min(x[i],y[i])
        if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
    return tuple(I),ok
print("="*88)
print("  TEST 1 — ARE THE CONSTRAINTS COMPLEMENT-CLOSED?")
print("="*88)
n=ok=0
for _ in range(500):
    d=random.choice([3,4,5])
    cells=list(product(*[range(2)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),9))))
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        I,A=allowed(Ss,x,y,d)
        if I is None or not A: continue
        n+=1
        comp={tuple(1-b for b in bits) for bits in A}
        ok+= (comp==A)
print("\n     constraints checked : %d      complement-closed : %d  (%.1f%%)"%(n,ok,100*ok/max(n,1)))
print("="*88)
print("  TEST 2 — HOW MANY CONSTRAINTS ARE ARITY 2  (a single XOR)?")
print("="*88)
from collections import Counter
print("\n  %6s%14s%12s%12s%12s"%("d","constraints","|I|=2","|I|=3","|I|≥4"))
print("  "+"-"*56)
for d in (3,4,5,6):
    ar=Counter(); tot=0
    for _ in range(160):
        cells=list(product(*[range(2)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),10))))
        Ss=set(S)
        for x,y in combinations(sorted(S),2):
            I,A=allowed(Ss,x,y,d)
            if I is None: continue
            if len(A)==2**len(I): continue
            ar[min(len(I),4)]+=1; tot+=1
    if tot: print("  %6d%14d%12.3f%12.3f%12.3f"%(d,tot,ar[2]/tot,ar[3]/tot,ar[4]/tot))
print("="*88)
print("  TEST 3 — DOES THE ARITY-2 PART ALONE DECIDE?")
print("="*88)
print("""
  **Build the signed graph from the arity-2 constraints and 2-colour it.**
  If 2-colouring alone matches brute force, the arity-2 part decides.
""")
def brute(S,d):
    Ss=set(S)
    for s in product([0,1],repeat=d):
        good=True
        for x,y in combinations(sorted(S),2):
            j=tuple((min if s[i] else max)(x[i],y[i]) for i in range(d))
            m=tuple((max if s[i] else min)(x[i],y[i]) for i in range(d))
            if j not in Ss or m not in Ss: good=False; break
        if good: return True
    return False
def two_colour(S,d):
    """signed-graph 2-colouring from arity-2 constraints only"""
    Ss=set(S); edges=[]
    for x,y in combinations(sorted(S),2):
        I,A=allowed(Ss,x,y,d)
        if I is None or len(I)!=2: continue
        if len(A)==4: continue
        if not A: return False
        # A is complement-closed: either {00,11} (equal) or {01,10} (differ)
        if A=={(0,0),(1,1)}: edges.append((I[0],I[1],0))
        elif A=={(0,1),(1,0)}: edges.append((I[0],I[1],1))
        else: return None
    col={}
    import collections
    adj=collections.defaultdict(list)
    for a,b,p in edges: adj[a].append((b,p)); adj[b].append((a,p))
    for st in range(d):
        if st in col: continue
        col[st]=0; stack=[st]
        while stack:
            u=stack.pop()
            for v,p in adj[u]:
                want=col[u]^p
                if v in col:
                    if col[v]!=want: return False
                else: col[v]=want; stack.append(v)
    return True
print("\n  %6s%12s%14s%14s%12s"%("d","instances","2-colour==bf","false pos","false neg"))
print("  "+"-"*58)
for d in (3,4,5,6):
    n=ag=fp=fn=0
    for _ in range(400):
        cells=list(product(*[range(2)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),10))))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        b=brute(S,d); c=two_colour(S,d)
        if c is None: continue
        n+=1; ag+= (b==c)
        if c and not b: fp+=1
        if b and not c: fn+=1
    if n: print("  %6d%12d%14d%14d%12d"%(d,n,ag,fp,fn))