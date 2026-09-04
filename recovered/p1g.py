import sys, math, random
sys.path.insert(0,"/home/claude/work")
exec(open("p1d.py").read().split("# ---- TEST THE CLAIM")[0])
F=[(-1,0,2,0,-1,0,0,0),(-2,0,3,0,0,0,-1,0),(0,-1,0,0,2,0,-1,0),(0,-1,0,2,0,-1,0,0),(0,0,0,-1,0,2,0,-1)]
def five(v): return all(sum(f[i]*v[i] for i in range(8))>0 for f in F)
def s1(v,idx): return all(v[i+1]-v[i] <= v[i]-v[i-1]+1e-12 for i in idx)
def s2(v,idx): return all(v[i-2]-2*v[i]+v[i+2] < 0 for i in idx)
random.seed(11); feas=[];infe=[]
for _ in range(30000):
    d=[random.random() for _ in range(7)]; v=[0.0]
    for x in d: v.append(v[-1]+x)
    s=v[-1]; v=[x/s for x in v]
    (feas if five(v) else infe).append(v)
print(f"feasible {len(feas)}  infeasible {len(infe)}")
for nm,fn in [("STRIDE 1 concave at {2,3,5}",lambda v:s1(v,[2,3,5])),
              ("STRIDE 2 concave at {2,3,5}",lambda v:s2(v,[2,3,5])),
              ("STRIDE 2 at {2,3,5} + facets 2,3",lambda v: s2(v,[2,3,5]) and five(v))]:
    tp=sum(1 for v in feas if fn(v)); fp=sum(1 for v in infe if fn(v))
    print(f"  {nm:<34} covers {tp:>5}/{len(feas)} feasible   admits {fp:>6}/{len(infe)} infeasible")
# how many of the 106 steps contribute ANY chord constraint at all
gen=set()
for k,provs in uniq.items():
    for z,*_ in provs: gen.add(z)
allz=set(z for z,_,_,_ in STEPS)
print(f"\nsteps generating any chord row: {len(gen)} of {len(allz)}")
FKEYS=[]
for f in F:
    g=math.gcd(*[abs(int(x)) for x in f if x]); FKEYS.append(tuple(round(x/g,12) for x in f))
binding=set()
for k in FKEYS:
    for z,*_ in (uniq.get(k) or uniq.get(tuple(-x for x in k)) or []): binding.add(z)
print(f"steps generating an IRREDUNDANT facet: {sorted(binding)}")
print("  names:", [G.GROUND[z][0] for z in sorted(binding)])