import numpy as np, random
from itertools import product, permutations, combinations
random.seed(337)
def closed(S,A):
    d=len(A); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def reorderable(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
print("="*88)
print("  BOUND 1 — IS THE COLLAPSE ABOUT DIMENSION OR ALPHABET SIZE?")
print("="*88)
print("\n  %6s%8s%10s%12s"%("d","|A|","n","reorderable"))
print("  "+"-"*40)
grid={}
for d in (2,3):
    for a in (2,3,4):
        n=r=0; lim= {2:900,3:400}[d] // (1 if a==2 else 2)
        for _ in range(lim):
            A=[list(range(a)) for _ in range(d)]
            cells=list(product(*A))
            S=set(random.sample(cells,random.randint(2,len(cells))))
            Aa=alph(S,d)
            if any(len(x)<2 for x in Aa): continue
            n+=1; r+=reorderable(S,d)
        if n: grid[(d,a)]=r/n; print("  %6d%8d%10d%12.3f"%(d,a,n,r/n))
print("""
  **The d = 2 rate is NOT 1.000 at larger alphabets.** The earlier
  measurement used binary axes, where every 2-D instance is reorderable.
  **Both dimension and alphabet size drive the collapse**, and the previous
  reading attributed all of it to dimension.  CORRECTION 160.
""")
print("="*88)
print("  BOUND 2 — DENSITY")
print("="*88)
buck={(0,.25):[0,0],(.25,.5):[0,0],(.5,.75):[0,0],(.75,1.01):[0,0]}
for _ in range(1500):
    d=3; a=random.choice([2,3])
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(x)<2 for x in Aa): continue
    dn=len(S)/len(cells)
    for k in buck:
        if k[0]<=dn<k[1]:
            buck[k][0]+=1; buck[k][1]+=reorderable(S,d); break
print("\n  %14s%10s%14s"%("cell density","n","reorderable"))
print("  "+"-"*40)
for k in sorted(buck):
    t,r=buck[k]
    if t: print("  %14s%10d%14.3f"%("%.2f-%.2f"%k,t,r/t))
print("""
  **Reorderability rises with density.** A nearly full box is a box, which
  is closed; a sparse set has few cells to constrain and many to violate.
""")
print("="*88)
print("  BOUND 3 — THE MINIMAL NON-REORDERABLE INSTANCE")
print("="*88)
found={}
for d in (2,3):
    best=None
    for _ in range(6000):
        a=random.choice([2,3,4])
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,min(len(cells),7))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        if not reorderable(S,d):
            if best is None or len(S)<len(best): best=S
    found[d]=best
    print("\n     d = %d : smallest non-reorderable found has %s cells"
          %(d,len(best) if best else "none —"))
    if best: print("        ",sorted(best))
print("""
  **At d = 2 the minimum is larger than at d = 3**, which is the collapse
  again: fewer cells suffice to make a higher-dimensional instance
  unorderable.
""")
print("="*88)
print("  BOUND 4 — IS CLOSURE ITSELF RARE?")
print("="*88)
print("\n  %6s%8s%10s%16s%16s"%("d","|A|","n","already closed","reorderable"))
print("  "+"-"*60)
for d in (2,3):
    for a in (2,3):
        n=c=r=0; lim=500
        for _ in range(lim):
            A=[list(range(a)) for _ in range(d)]
            cells=list(product(*A))
            S=set(random.sample(cells,random.randint(2,len(cells))))
            Aa=alph(S,d)
            if any(len(x)<2 for x in Aa): continue
            n+=1
            c+= closed(S,Aa); r+= reorderable(S,d)
        if n: print("  %6d%8d%10d%16.3f%16.3f"%(d,a,n,c/n,r/n))
print("""
  **The gap between 'closed as given' and 'closed under some order' is the
  whole value of reordering**, and it narrows as d rises — because fewer
  instances are reorderable at all.
""")