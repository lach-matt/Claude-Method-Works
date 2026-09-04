from itertools import product
from collections import Counter, defaultdict

# Sec 2.1 constraints, Sec 2.4 caps (3,3,2,3) on n, e, l, k
CN,CE,CL,CK = 3,3,2,3
def build():
    cells=[]
    for n in range(1,CN+1):
        for l in range(0, min(n-1,CL)+1):                 # l <= n-1
            for k in range(0, min(2*(2*l+1),CK)+1):        # k <= 2(2l+1)
                for S2 in range(0,k+1):                    # 2S <= k
                    for q in range(0,k+1):                 # q <= k
                        for e in range(1,CE+1):
                            for f in range(0, min(e-1,CL)+1):   # f <= e-1
                                for g in range(0, min(q,2*(2*f+1))+1):  # g<=q, g<=2(2f+1)
                                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
L=build(); S=set(L)
print(f"|Lambda| = {len(L)}          book states 976     {'MATCH' if len(L)==976 else 'MISMATCH'}")
COORD=['n','l','k','q','e','f','g','2S']
rng=[(min(c[i] for c in L),max(c[i] for c in L)) for i in range(8)]
box=1
for lo,hi in rng: box*=(hi-lo+1)
print("realised ranges: "+"  ".join(f"{COORD[i]}:{rng[i][0]}-{rng[i][1]}" for i in range(8)))
print(f"bounding box = {box}   book states 6,912   {'MATCH' if box==6912 else 'MISMATCH'}"
      f"    density {100*len(L)/box:.1f}%  (book 14.1%)")

# closure under meet and join
jf=mf=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        x,y=L[i],L[j]
        if tuple(map(max,x,y)) not in S: jf+=1
        if tuple(map(min,x,y)) not in S: mf+=1
npairs=len(L)*(len(L)-1)//2
print(f"\npairs = {npairs}  (book: 475,800)   join failures {jf}   meet failures {mf}")

# rank modularity
mv=0
for i in range(len(L)):
    x=L[i]
    for j in range(i+1,len(L)):
        y=L[j]
        if sum(map(max,x,y))+sum(map(min,x,y))!=sum(x)+sum(y): mv+=1
print(f"rank-modularity violations over all {npairs} pairs: {mv}")

# generating function
F1=len(L); Fm1=sum((-1)**sum(c) for c in L)
print(f"\nF(1) = {F1}   F(-1) = {Fm1}   book states 976 and 2   "
      f"{'MATCH' if (F1,Fm1)==(976,2) else 'MISMATCH'}")

# rank levels
lev=Counter(sum(c) for c in L)
print(f"rank levels = {len(lev)}  height {max(lev)}  widest {max(lev.values())} at rank "
      f"{max(lev,key=lev.get)}   book: 18 levels, widest 122 at 11")

# join-irreducibles: cells covering exactly one cell
idx={c:i for i,c in enumerate(L)}
def covers(c):
    out=[]
    for i in range(8):
        d=list(c); d[i]-=1
        if d[i]>=0 and tuple(d) in S: out.append(tuple(d))
    return out
ji=[c for c in L if len(covers(c))==1]
print(f"join-irreducibles = {len(ji)}   book states 17   {'MATCH' if len(ji)==17 else 'MISMATCH'}")
# covering relations among the join-irreducibles, under the lattice order
def leq(a,b): return all(p<=q for p,q in zip(a,b))
edges=0
for a in ji:
    for b in ji:
        if a!=b and leq(a,b) and not any(c!=a and c!=b and leq(a,c) and leq(c,b) for c in ji): edges+=1
print(f"covering relations among them = {edges}   book states 20   {'MATCH' if edges==20 else 'MISMATCH'}")