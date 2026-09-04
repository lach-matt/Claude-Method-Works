import sys, math, itertools; sys.path.insert(0,"/home/claude/work")
import ground as G
def cap(l): return 2*(2*l+1)
STEPS=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    STEPS.append((Z,gn,gl,cand))
print("steps:",len(STEPS))
def corridors(A,B):
    IV=[]
    for Z,gn,gl,cand in STEPS:
        lo,hi=-math.inf,math.inf; dead=False
        for n,l in cand:
            if (n,l)==(gn,gl): continue
            d=B(n,l)-B(gn,gl); r=A(n,l)-A(gn,gl)
            if abs(d)<1e-12:
                if r<=0: dead=True
                continue
            if d>0: hi=min(hi,r/d)
            else:   lo=max(lo,r/d)
        if dead or lo>=hi: IV.append((Z,None,None)); continue
        IV.append((Z,lo,hi))
    return IV
def verdict(IV):
    live=[(Z,lo,hi) for Z,lo,hi in IV if lo is not None]
    dead=len(IV)-len(live)
    n=len(live); adj=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if live[i][2]<=live[j][1] or live[j][2]<=live[i][1]:
                adj[i][j]=adj[j][i]=True
    best=[0]
    def ext(R,P):
        if not P:
            best[0]=max(best[0],R); return
        if R+len(P)<=best[0]: return
        for k,v in enumerate(P): ext(R+1,[u for u in P[k+1:] if adj[v][u]])
    ext(0,list(range(n)))
    return dead,n,best[0]
p=lambda n,l:n-l-1
FORMS={
 "n - a*sqrt(p)      (the work's nu)": (lambda n,l:n, lambda n,l:math.sqrt(p(n,l))),
 "n - a*p":                            (lambda n,l:n, lambda n,l:float(p(n,l))),
 "n + a*l":                            (lambda n,l:n, lambda n,l:-float(l)),
 "n - a*ln(1+p)":                      (lambda n,l:n, lambda n,l:math.log(1+p(n,l))),
 "(n+l) - a/n        (Gemini I)":      (lambda n,l:float(n+l), lambda n,l:1.0/n),
 "(n+l) + a*l":                        (lambda n,l:float(n+l), lambda n,l:-float(l)),
 "n - a*sqrt(n)":                      (lambda n,l:n, lambda n,l:math.sqrt(n)),
}
print(f"  {'form':<36}{'refuted':>8}{'live':>6}{'clique':>8}")
for name,(A,B) in FORMS.items():
    d,nn,c=verdict(corridors(A,B))
    print(f"  {name:<36}{d:>8}{nn:>6}{c:>8}")

print("\n--- IS CLIQUE 3 AN INVARIANT OF THE CONCAVE-IN-p CLASS? ---")
print(f"  {'B(n,l) = f(p)':<28}{'refuted':>8}{'clique':>8}{'stab pts':>34}")
def stab(IV):
    live=sorted([(lo,hi) for Z,lo,hi in IV if lo is not None],key=lambda t:t[1])
    pts=[];last=-math.inf
    for lo,hi in live:
        if lo>=last: last=hi; pts.append(last)
    return pts
import numpy as np
FS=[("p**0.25",lambda x:x**0.25),("p**0.4",lambda x:x**0.4),
    ("p**0.5 = sqrt(p)",lambda x:x**0.5),("p**0.6",lambda x:x**0.6),
    ("p**0.75",lambda x:x**0.75),("p**0.9",lambda x:x**0.9),
    ("p**1.0 (linear)",lambda x:float(x)),("p**1.25 (convex)",lambda x:x**1.25),
    ("ln(1+p)",lambda x:math.log(1+x)),("1-exp(-p)",lambda x:1-math.exp(-x)),
    ("atan(p)",lambda x:math.atan(x)),("p/(1+p)",lambda x:x/(1+x))]
for nm,f in FS:
    A=lambda n,l:n; B=lambda n,l:f(p(n,l))
    IV=corridors(A,B); d,nn,c=verdict(IV)
    sp=stab(IV)
    print(f"  {nm:<28}{d:>8}{c:>8}{str([round(x,4) for x in sp]):>34}")

print("\n--- WHERE THE CLASS BOUNDARY LIES ---")
for b in (0.05,0.1,0.5,0.95,0.99,0.999,1.0,1.001,1.01):
    A=lambda n,l:n; B=lambda n,l:(p(n,l))**b
    d,nn,c=verdict(corridors(A,B))
    print(f"  beta={b:<6} refuted={d:>3}  clique={c}")
print("\n--- THE SIX STEPS THAT REFUTE A LINEAR OR CONVEX FORM ---")
L="spdfg"
A=lambda n,l:n; B=lambda n,l:float(p(n,l))
IV=corridors(A,B)
bad=[Z for Z,lo,hi in IV if lo is None]
for Z,gn,gl,cand in STEPS:
    if Z in bad:
        print(f"  Z={Z:>3} {G.GROUND[Z][0]:<3} enters {gn}{L[gl]}  p={p(gn,gl)}")
