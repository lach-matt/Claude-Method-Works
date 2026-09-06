from collections import Counter
CN,CE,CL,CK = 3,3,1,3          # caps on n, e, l, k  (Sec 2.4)
def build(coup=True):
    C=[]
    for n in range(1,CN+1):
     for l in range(0,min(n-1,CL)+1):                  # l <= n-1
      for k in range(1,min(2*(2*l+1),CK)+1):           # k <= 2(2l+1),  k >= 1
       for S2 in range(0,k+1):                         # 2S <= k
        for q in range(0,k+1):                         # q <= k
         for e in range(1,CE+1):
          for f in range(0,min(e-1,CL)+1):             # f <= e-1
           gm=min(q,2*(2*f+1)) if coup else q          # g <= q,  g <= 2(2f+1)
           for g in range(0,gm+1): C.append((n,l,k,q,e,f,g,S2))
    return C
L=build(); S=set(L); L0=build(False); diff=set(L0)-S
def chk(name,got,want): print(f"  {name:42s} {str(got):>12s}   book {str(want):>8s}   {'MATCH' if str(got)==str(want) else 'MISMATCH'}")
print("VERIFICATION OF Λ  — built from §2.1 constraints at §2.4 caps (3,3,1,3), k≥1\n")
chk("|Λ|", len(L), 976)
b=1
for i in range(8): b*=(max(c[i] for c in L)-min(c[i] for c in L)+1)
chk("bounding box", b, 6912)
chk("density", f"{100*len(L)/b:.1f}%", "14.1%")
chk("coupling removed → cells", len(L0), 1000)
chk("cells the coupling excludes", len(diff), 24)
chk("  ...all with f=0 and g=3", all(c[5]==0 and c[6]==3 for c in diff), True)
jf=mf=mv=0; n=len(L)
for i in range(n):
    x=L[i]
    for j in range(i+1,n):
        y=L[j]; J=tuple(map(max,x,y)); M=tuple(map(min,x,y))
        if J not in S: jf+=1
        if M not in S: mf+=1
        if sum(J)+sum(M)!=sum(x)+sum(y): mv+=1
chk("pairs tested", n*(n-1)//2, 475800)
chk("join failures", jf, 0); chk("meet failures", mf, 0)
chk("rank-modularity violations", mv, 0)
chk("F(1)", len(L), 976)
chk("F(-1)", sum((-1)**sum(c) for c in L), 2)
lev=Counter(sum(c) for c in L)
chk("rank levels", len(lev), 18)
chk("widest level", max(lev.values()), 122)
chk("  ...at rank", max(lev,key=lev.get), 11)
def cov(c):
    o=[]
    for i in range(8):
        d=list(c); d[i]-=1
        if d[i]>=0 and tuple(d) in S: o.append(tuple(d))
    return o
ji=[c for c in L if len(cov(c))==1]
chk("join-irreducibles", len(ji), 17)
leq=lambda a,b: all(p<=q for p,q in zip(a,b))
ed=sum(1 for a in ji for bb in ji if a!=bb and leq(a,bb)
       and not any(c!=a and c!=bb and leq(a,c) and leq(c,bb) for c in ji))
chk("covering relations among them", ed, 20)
dv=0
import random; random.seed(0); sm=random.sample(L,40)
for x in sm:
    for y in sm:
        for z in sm:
            if tuple(max(p,min(q,r)) for p,q,r in zip(x,y,z))!=tuple(min(max(p,q),max(p,r)) for p,q,r in zip(x,y,z)): dv+=1
chk("distributivity violations /64,000 triples", dv, 0)
lg=[lev[r] for r in sorted(lev)]
chk("log-concave", all(lg[i]**2>=lg[i-1]*lg[i+1] for i in range(1,len(lg)-1)), True)
open('/mnt/user-data/outputs/lambda_976_cells.txt','w').write(
 "Λ — THE LACH CYLINDER, COMPLETE ENUMERATION\n"
 "Built from §2.1's seven constraints at §2.4's caps (n≤3, e≤3, ℓ≤1, k≤3), k≥1.\n"
 "Coordinates: (n, ℓ, k, q, e, f, g, 2S)\n"
 "  n  source shell        q  electrons removed    g  target occupancy\n"
 "  ℓ  source subshell     e  target shell         2S multiplicity\n"
 "  k  source occupancy    f  target subshell\n"
 "Constraints: ℓ≤n−1 · k≤2(2ℓ+1) · q≤k · f≤e−1 · g≤2(2f+1) · g≤q · 2S≤k\n"
 f"976 cells · E(X)=0 · F(1)=976 · F(−1)=2 · box 6912 · density 14.1%\n"
 + "="*62 + "\n"
 + "\n".join(f"{i+1:4d}  ({c[0]}, {c[1]}, {c[2]}, {c[3]}, {c[4]}, {c[5]}, {c[6]}, {c[7]})   rank {sum(c):2d}"
             for i,c in enumerate(sorted(L, key=lambda c:(sum(c),c)))) + "\n")
print("\n  rank profile:", " ".join(str(lev[r]) for r in sorted(lev)))