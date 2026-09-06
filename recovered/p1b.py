import sys, math, random; sys.path.insert(0,"/home/claude/work")
exec(open("p1.py").read().split("p=lambda")[0])   # reuse STEPS, corridors, verdict
p=lambda n,l:n-l-1
random.seed(7)
def run(vec):
    A=lambda n,l:n; B=lambda n,l:vec[p(n,l)]
    return verdict(corridors(A,B))
def concave(v):
    return all(v[i+1]-v[i] <= v[i]-v[i-1] + 1e-12 for i in range(1,len(v)-1))
def increasing(v):
    return all(v[i+1]>v[i] for i in range(len(v)-1))
from collections import Counter
tab=Counter(); ex={}
N=40000
for _ in range(N):
    d=[random.random() for _ in range(7)]          # positive increments
    v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    if not increasing(v): continue
    c=concave(v)
    dead,live,cl=run(v)
    key=(c, dead==0, cl)
    tab[key]+=1
    if key not in ex: ex[key]=[round(x,3) for x in v]
print(f"  sampled {N} increasing 8-vectors on p=0..7 (normalised f(0)=0, f(7)=1)\n")
print(f"  {'concave':>8}{'0 refuted':>11}{'clique':>8}{'count':>9}")
for k in sorted(tab, key=lambda k:(-tab[k])):
    print(f"  {str(k[0]):>8}{str(k[1]):>11}{k[2]:>8}{tab[k]:>9}")
print("\n  CONCAVE and REFUTED (counterexample to sufficiency)?")
bad=[k for k in tab if k[0] and not k[1]]
print("   ",bad if bad else "NONE FOUND")
print("\n  NON-CONCAVE and NOT refuted (concavity not necessary)?")
good=[k for k in tab if (not k[0]) and k[1]]
print("   ",good if good else "NONE FOUND")
for k in good[:2]: print("    example vector:",ex[k])