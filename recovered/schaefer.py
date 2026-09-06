import random
from itertools import product, permutations, combinations
from collections import Counter
random.seed(677)
print("="*88)
print("  SCHAEFER'S DICHOTOMY APPLIED TO THE CONSTRAINT LANGUAGE")
print("="*88)
print("""
  **A boolean CSP is polynomial iff the WHOLE language admits one of:**

     bijunctive  — closed under MAJORITY        (2-SAT)
     Horn        — closed under MIN  (∧)
     dual-Horn   — closed under MAX  (∨)
     affine      — closed under x⊕y⊕z
     0-valid     — contains all-zeros
     1-valid     — contains all-ones

  **Otherwise NP-complete.** And the class must be shared across the language,
  not chosen per constraint.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def constraints(S,d):
    Ss=set(S); out=[]
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
def to_xor(A,k): return frozenset(tuple(b[i]^b[i+1] for i in range(k-1)) for b in A)
def cl_maj(T,m):
    for a in T:
        for b in T:
            for c in T:
                if tuple((a[i]&b[i])|(b[i]&c[i])|(a[i]&c[i]) for i in range(m)) not in T: return False
    return True
def cl_min(T,m):
    return all(tuple(a[i]&b[i] for i in range(m)) in T for a in T for b in T)
def cl_max(T,m):
    return all(tuple(a[i]|b[i] for i in range(m)) in T for a in T for b in T)
def cl_aff(T,m):
    for a in T:
        for b in T:
            for c in T:
                if tuple(a[i]^b[i]^c[i] for i in range(m)) not in T: return False
    return True
seen={}
for _ in range(1600):
    d=random.choice([4,5]); a=2
    cells=list(product(*[range(a)]*d))
    S=set(random.sample(cells,random.randint(4,min(len(cells),12))))
    for k,A in constraints(S,d):
        if k<4: continue
        T=to_xor(A,k); m=k-1
        seen[(m,T)]=seen.get((m,T),0)+1
print("     distinct arity ≥4 XOR constraints : %d"%len(seen))
rows=[]
for (m,T),cnt in seen.items():
    rows.append(dict(m=m,T=T,n=cnt,maj=cl_maj(T,m),mn=cl_min(T,m),mx=cl_max(T,m),
                     aff=cl_aff(T,m),z=tuple([0]*m) in T,o=tuple([1]*m) in T))
nb=[r for r in rows if not r['maj']]
print("     not bijunctive (the 45)           : %d"%len(nb))
print("="*88)
print("  THE 45, CLASSIFIED")
print("="*88)
print("\n  %-14s%10s%12s"%("property","count","by occurrence"))
print("  "+"-"*40)
for key,nm in [('mn','Horn (min-closed)'),('mx','dual-Horn (max)'),('aff','affine (⊕)'),
               ('z','0-valid'),('o','1-valid')]:
    c=sum(1 for r in nb if r[key]); w=sum(r['n'] for r in nb if r[key])
    print("  %-14s%10d%12d"%(nm,c,w))
none=[r for r in nb if not (r['mn'] or r['mx'] or r['aff'] or r['z'] or r['o'])]
print("\n     **in NO Schaefer class at all : %d**"%len(none))
if none:
    for r in sorted(none,key=lambda x:-x['n'])[:3]:
        print("        %s   arity %d   %d occurrences"%(sorted(r['T']),r['m']+1,r['n']))
print("="*88)
print("  DOES THE WHOLE LANGUAGE SHARE A CLASS?")
print("="*88)
allr=rows
for key,nm in [('maj','bijunctive'),('mn','Horn'),('mx','dual-Horn'),('aff','affine'),
               ('z','0-valid'),('o','1-valid')]:
    c=sum(1 for r in allr if r[key])
    print("     %-12s : %d of %d constraints  ->  language-wide : %s"%(nm,c,len(allr),c==len(allr)))
print("""
  **If no class covers every constraint, Schaefer gives NP-completeness for
  the language — and the question 'is reorderability polynomial at d ≥ 4' is
  ANSWERED NO**, subject to the reduction being realisable by cell sets, which
  is the obstruction measured twice today.
""")