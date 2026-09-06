"""p1e.py -- the irredundant facet list of the feasible cone, and where the
concave cone sits inside it."""
import sys, math, random, numpy as np
sys.path.insert(0,"/home/claude/work")
exec(open("p1d.py").read().split("# ---- TEST THE CLAIM")[0])
from scipy.optimize import linprog

MONO = []
for i in range(7):
    c = [0.0]*8; c[i+1] = 1.0; c[i] = -1.0
    MONO.append(tuple(c))

CH = list(uniq.keys())
print(f"\nsystem: {len(CH)} chord rows + {len(MONO)} monotonicity rows")

def redundant(target, others):
    """is  target . v > 0  implied by  others . v > 0 (and v bounded)?
    minimise target.v subject to others.v >= 1, |v| <= 100. If min >= 0 -> implied."""
    A_ub = [[-x for x in r] for r in others]
    b_ub = [-1.0]*len(others)
    res = linprog(c=list(target), A_ub=A_ub, b_ub=b_ub,
                  bounds=[(-100,100)]*8, method="highs")
    if not res.success: return None
    return res.fun >= -1e-7

ALL = CH + MONO
keep = list(range(len(ALL)))
changed = True
while changed:
    changed = False
    for i in list(keep):
        others = [ALL[j] for j in keep if j != i]
        if not others: continue
        r = redundant(ALL[i], others)
        if r:
            keep.remove(i); changed = True
print(f"irredundant rows: {len(keep)}  "
      f"(chord {sum(1 for i in keep if i < len(CH))}, "
      f"mono {sum(1 for i in keep if i >= len(CH))})")

def show(c):
    t = []
    for i,x in enumerate(c):
        if abs(x) < 1e-9: continue
        t.append(f"{'+' if x>0 else '-'}{abs(x):g}*v{i}")
    return " ".join(t).lstrip("+")

print("\nTHE EXACT CONDITION -- irredundant facets:")
for i in keep:
    tag = "chord" if i < len(CH) else "mono "
    prov = ""
    if i < len(CH):
        ps = uniq[CH[i]]
        zs = sorted(set(z for z,_,_,_,_,_,_ in ps))
        trip = ps[0]
        prov = f"   [p1={trip[1]} pg={trip[2]} p2={trip[3]}]  Z={zs if len(zs)<8 else str(len(zs))+' steps'}"
    print(f"  {tag}  {show(ALL[i]):<44}{prov}")

# --- does the concave cone lie inside? which facet is nearest the boundary? ---
print("\nCONCAVE CONE vs THE FACETS")
random.seed(3)
worst = {}
for _ in range(5000):
    d = sorted([random.random() for _ in range(7)], reverse=True)
    v = [0.0]
    for x in d: v.append(v[-1]+x)
    s = v[-1]; v = [x/s for x in v]
    for i in keep:
        if i >= len(CH): continue
        val = sum(ALL[i][k]*v[k] for k in range(8))
        if i not in worst or val < worst[i][0]: worst[i] = (val, list(v))
for i in sorted(worst, key=lambda i: worst[i][0]):
    print(f"  min over concave cone: {worst[i][0]:+.6f}   {show(ALL[i])}")

# --- is concavity necessary at any single index? ------------------------------
print("\nHOW MUCH BIGGER IS THE FEASIBLE CONE THAN THE CONCAVE CONE?")
random.seed(7)
feas = 0; conc = 0; N = 40000
for _ in range(N):
    d = [random.random() for _ in range(7)]
    v = [0.0]
    for x in d: v.append(v[-1]+x)
    s = v[-1]; v = [x/s for x in v]
    f = all(sum(k[i]*v[i] for i in range(8)) > 0 for k in CH)
    c = all(v[i+1]-v[i] <= v[i]-v[i-1]+1e-12 for i in range(1,7))
    feas += f; conc += c
    if c and not f: print("  COUNTEREXAMPLE: concave but infeasible", v)
print(f"  of {N} uniform increasing vectors: feasible {feas}  concave {conc}")
