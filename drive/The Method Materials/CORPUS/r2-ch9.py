# r2-ch9.py — Phase R2, main Chapter 9 "The arithmetic encoding" (chat 70). Run beside tower-2.py.
import importlib.util, itertools, random, math, collections
import numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
cells=tw.L8(); S=set(cells); n=len(cells); A=np.array(cells,dtype=np.int16)
P=[2,3,5,7,11,13,17,19]
def N(x):
    v=1
    for p,e in zip(P,x): v*=p**e
    return v
def Omega(m):
    c=0
    for p in P:
        while m%p==0: m//=p; c+=1
    return c
def omega(m): return sum(1 for p in P if m%p==0)
def tau(m):
    t=1
    for p in P:
        e=0
        while m%p==0: m//=p; e+=1
        t*=e+1
    return t
Nv=[N(x) for x in cells]
print('rank = Ω(N) on all cells:',all(sum(x)==Omega(v) for x,v in zip(cells,Nv)),'| ω ≤ 8 on all:',max(omega(v) for v in Nv)<=8,'| cell (2,1,3,3,2,1,3,3) in Λ:',(2,1,3,3,2,1,3,3) in S,'ω there:',omega(N((2,1,3,3,2,1,3,3))),'| cells with ω = 8:',sum(omega(v)==8 for v in Nv))
# gcd/lcm = meet/join on all pairs; divisibility = order
bad=0; comp=0
for i in range(n):
    for j in range(i+1,n):
        x,y=cells[i],cells[j]; a,b=Nv[i],Nv[j]; g=math.gcd(a,b)
        if N(tuple(map(min,x,y)))!=g or N(tuple(map(max,x,y)))!=a*b//g: bad+=1
        if (all(p<=q for p,q in zip(x,y)) != (b%a==0)) or (all(q<=p for p,q in zip(x,y)) != (a%b==0)): bad+=1
        if all(p<=q for p,q in zip(x,y)) or all(q<=p for p,q in zip(x,y)): comp+=1
pairs=n*(n-1)//2
print(f'gcd/lcm = meet/join and divisibility = order on all {pairs} pairs: violations {bad} | comparable pairs {comp} = {100*comp/pairs:.1f}% of pairs')
# the five forms of d
def interval_cells(x,y):
    lo=tuple(map(min,x,y)); hi=tuple(map(max,x,y))
    return sum(1 for z in itertools.product(*[range(l,h+1) for l,h in zip(lo,hi)]) if z in S)
def box(x,y): return math.prod(abs(p-q)+1 for p,q in zip(x,y))
random.seed(1); eq12=0; eq23=0; eq24=0; eq25=0; tot=0; voidbearing=0
for _ in range(2000):
    x=random.choice(cells); y=random.choice(cells); a,b=N(x),N(y); g=math.gcd(a,b)
    f1=interval_cells(x,y); f2=box(x,y); f3=tau(a*b//(g*g)); f4=tau((a//g)*(b//g)); f5=math.prod(abs(p-q)+1 for p,q in zip(x,y))
    tot+=1; eq12+=(f1==f2); eq23+=(f2==f3); eq24+=(f2==f4); eq25+=(f2==f5); voidbearing+=(f1!=f2)
print(f'2,000 random pairs: form1 (Λ-interval count) = form2 (∏(|Δ|+1)) in {eq12}; form2=form3 {eq23}; form2=form4 {eq24}; form2=form5 {eq25}; pairs whose box holds a non-cell (void-bearing) {voidbearing}')
# exhaustive: how many of all pairs have a void in their box?
def boxfree(x,y):
    lo=tuple(map(min,x,y)); hi=tuple(map(max,x,y))
    # seven comparisons: the box is in Λ iff every constraint holds at its worst corner (hi on the bounded side, lo on the bounding side)
    return (hi[1]<=lo[0]-1 and hi[2]<=4*lo[1]+2 and hi[3]<=lo[2] and hi[5]<=lo[4]-1 and hi[6]<=4*lo[5]+2 and hi[6]<=lo[3] and hi[7]<=lo[2])
# validate the seven-comparison test against brute force on 3,000 pairs
ok=all(boxfree(x,y)==(interval_cells(x,y)==box(x,y)) for x,y in ((random.choice(cells),random.choice(cells)) for _ in range(3000)))
print('seven-comparison void-free test agrees with brute force on 3,000 pairs:',ok)
vf=sum(boxfree(cells[i],cells[j]) for i in range(n) for j in range(i+1,n)); print(f'void-free boxes over all {pairs} pairs: {vf} ({100*vf/pairs:.1f}%); void-bearing {pairs-vf}')
# triangle inequality, log d metric checks
viol=0
for _ in range(4000):
    x,y,z=(random.choice(cells) for _ in range(3))
    if box(x,z)>box(x,y)*box(y,z): viol+=1
print('multiplicative triangle inequality on 4,000 triples: violations',viol,'| d(x,x)=1:',box(cells[5],cells[5])==1)
# join-irreducible representation for the Möbius closed form
LE=np.ones((n,n),dtype=bool)
for c in range(8): LE&=(A[:,c][:,None]<=A[:,c][None,:])
LT=LE&~np.eye(n,dtype=bool)
ji=[x for x in range(n) if LT[:,x].any() and (lambda b:(~LT[np.ix_(b,b)].any(axis=1)).sum()==1)(np.nonzero(LT[:,x])[0])]
m=len(ji); rep=[frozenset(j for j in ji if LE[j,x]) for x in range(n)]     # JI below each cell
jiLT={(a,b):bool(LT[a,b]) for a in ji for b in ji}
def mu_closed(x,y):
    D=rep[y]-rep[x]
    if any(jiLT[(a,b)] for a in D for b in D): return 0
    return (-1)**len(D)
idx={c:i for i,c in enumerate(cells)}
def mu_rec(x,y,memo):
    if x==y: return 1
    if (x,y) in memo: return memo[(x,y)]
    lo=cells[x]; hi=cells[y]
    zs=[idx[z] for z in itertools.product(*[range(l,h+1) for l,h in zip(lo,hi)]) if z in S and z!=hi]
    v=-sum(mu_rec(x,z,memo) for z in zs); memo[(x,y)]=v; return v
random.seed(2); cmp_pairs=[(i,j) for i in range(n) for j in range(n) if LT[i,j]]
sample=random.sample(cmp_pairs,300); memo={}
agree=sum(mu_closed(i,j)==mu_rec(i,j,memo) for i,j in sample)
print(f'join-irreducibles {m}; Möbius closed form = recursive definition on {agree} of 300 sampled comparable pairs; values ⊆ {{-1,0,1}}:',set(mu_closed(i,j) for i,j in cmp_pairs)<= {-1,0,1})
# μ_Λ = μ_arith iff void-free unit hypercube — on ALL comparable pairs
def mu_arith(x,y):
    d=[q-p for p,q in zip(x,y)]
    return 0 if any(e>=2 for e in d) else (-1)**sum(d)
cnt=collections.Counter()
for i,j in cmp_pairs:
    x,y=cells[i],cells[j]; unit=all(q-p<=1 for p,q in zip(x,y)); vfree=boxfree(x,y); ag=(mu_closed(i,j)==mu_arith(x,y))
    cnt[(unit,vfree,ag)]+=1
print('all comparable pairs (unit-hypercube?, void-free?, μ_Λ = μ_arith?) →',dict(cnt))
