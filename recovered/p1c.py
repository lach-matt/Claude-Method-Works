import sys, math, random; sys.path.insert(0,"/home/claude/work")
exec(open("p1.py").read().split("p=lambda")[0])
p=lambda n,l:n-l-1
random.seed(11)
def run(vec):
    A=lambda n,l:n; B=lambda n,l:vec[p(n,l)]
    return verdict(corridors(A,B))
from collections import Counter
# --- sample the CONCAVE cone directly: positive, non-increasing increments
tab=Counter()
for _ in range(5000):
    d=sorted([random.random() for _ in range(7)],reverse=True)
    v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    dead,live,cl=run(v)
    tab[(dead==0,cl)]+=1
print("  CONCAVE CONE, 5000 samples  (0-refuted, clique) -> count")
for k in sorted(tab,key=lambda k:-tab[k]): print("   ",k,tab[k])
# --- what do FEASIBLE vectors actually satisfy? test second differences by index
feas=[];infeas=[]
for _ in range(30000):
    d=[random.random() for _ in range(7)]
    v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    dead,live,cl=run(v)
    (feas if dead==0 else infeas).append((v,cl))
print(f"\n  feasible {len(feas)}  infeasible {len(infeas)}")
print("  fraction with NEGATIVE second difference at each interior p:")
print(f"  {'p':>3}{'feasible':>11}{'infeasible':>12}")
for i in range(1,7):
    f=sum(1 for v,c in feas if v[i+1]-v[i] < v[i]-v[i-1])/max(1,len(feas))
    g=sum(1 for v,c in infeas if v[i+1]-v[i] < v[i]-v[i-1])/max(1,len(infeas))
    print(f"  {i:>3}{f:>11.3f}{g:>12.3f}")
print("\n  clique distribution among FEASIBLE:",Counter(c for v,c in feas))