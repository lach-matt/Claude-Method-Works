"""p1f.py -- verify the five-facet condition to witness level."""
import sys, math, random, numpy as np
sys.path.insert(0,"/home/claude/work")
exec(open("p1d.py").read().split("# ---- TEST THE CLAIM")[0])
from scipy.optimize import linprog

F = [((-1,0,2,0,-1,0,0,0), "v0 - 2*v2 + v4 < 0      stride-2 concavity at p=2"),
     ((-2,0,3,0,0,0,-1,0), "2*v0 - 3*v2 + v6 < 0    chord (0,6) at p=2"),
     ((0,-1,0,0,2,0,-1,0), "v1 - 2*v4 + v6 < 0      chord (1,6) at p=4"),
     ((0,-1,0,2,0,-1,0,0), "v1 - 2*v3 + v5 < 0      stride-2 concavity at p=3"),
     ((0,0,0,-1,0,2,0,-1), "v3 - 2*v5 + v7 < 0      stride-2 concavity at p=5")]
MONO = []
for i in range(7):
    c=[0.0]*8; c[i+1]=1.0; c[i]=-1.0; MONO.append(tuple(c))

def oracle(v):
    A=lambda n,l:n; B=lambda n,l:v[p_of(n,l)]
    return all(lo is not None for Z,lo,hi in corridors(A,B))
def five(v): return all(sum(f[i]*v[i] for i in range(8))>0 for f,_ in F)

# 1. the five reproduce the oracle
random.seed(101); agree=dis=0
for _ in range(30000):
    d=[random.random() for _ in range(7)]; v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    if oracle(v)==five(v): agree+=1
    else: dis+=1
print(f"1. five facets vs oracle, 30,000 increasing vectors: agree {agree} disagree {dis}")

# 2. each facet is INDEPENDENTLY NECESSARY: find v satisfying the other four
#    + monotonicity but violating this one, and confirm the oracle refuses it.
print("\n2. independence witnesses (satisfy other four + monotone, violate this one):")
for k,(f,desc) in enumerate(F):
    others=[F[j][0] for j in range(len(F)) if j!=k]+MONO
    A_ub=[[-x for x in r] for r in others]+[list(f)]
    b_ub=[-1.0]*len(others)+[-1e-6]
    res=linprog(c=[0]*8, A_ub=A_ub, b_ub=b_ub, bounds=[(-50,50)]*8, method="highs")
    if not res.success:
        print(f"   facet {k+1}: NO WITNESS -> redundant"); continue
    v=list(res.x); mn,mx=min(v),max(v); v=[(x-mn)/(mx-mn) for x in v]
    A2=lambda n,l:n; B2=lambda n,l:v[p_of(n,l)]
    bad=[Z for Z,lo,hi in corridors(A2,B2) if lo is None]
    print(f"   facet {k+1}: witness found, oracle refuses {len(bad)} steps at Z={bad}   [{desc}]")

# 3. concavity => feasible, proved by the chord argument, checked numerically
print("\n3. strict concavity implies all five (checked on the cone):")
random.seed(5); mins=[math.inf]*5
for _ in range(20000):
    d=sorted([random.random() for _ in range(7)],reverse=True); v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    for k,(f,_) in enumerate(F):
        mins[k]=min(mins[k],sum(f[i]*v[i] for i in range(8)))
for k,(f,desc) in enumerate(F): print(f"   facet {k+1} min over cone = {mins[k]:+.6f}   [{desc}]")

# 4. which steps GENERATE each facet
print("\n4. generating steps per facet:")
for f,desc in F:
    g=math.gcd(*[abs(int(x)) for x in f if x])
    key=tuple(round(x/g,12) for x in f)
    key2=tuple(-x for x in key)
    prov=uniq.get(key) or uniq.get(key2) or []
    zs=sorted(set(z for z,*_ in prov))
    nm=[G.GROUND[z][0] for z in zs]
    print(f"   {desc:<40} {len(zs)} steps: {nm}")
