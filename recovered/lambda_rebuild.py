from collections import Counter
import random

# Reconstruction of Lambda from the recovered construction:
# coords (n, l, k, q, e, f, g, 2S), caps n<=3, e<=3, l<=1, k<=3, k>=1
# constraints: l<=n-1, k<=2(2l+1), q<=k, f<=e-1, g<=2(2f+1), g<=q, 2S<=k
CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
S=set(L)

ok=[]
def chk(name, got, want):
    m = (got==want)
    ok.append(m)
    print(f"{'PASS' if m else 'FAIL'}  {name}: {got}  (committed {want})")

chk("F(1) = |Lambda|", len(L), 976)
box=1
for i in range(8):
    box*= max(c[i] for c in L)-min(c[i] for c in L)+1
chk("bounding box", box, 6912)
chk("F(-1)", sum((-1)**sum(c) for c in L), 2)

jf=mf=mv=0; n=len(L)
for i in range(n):
    x=L[i]
    for j in range(i+1,n):
        y=L[j]; J=tuple(map(max,x,y)); M=tuple(map(min,x,y))
        if J not in S: jf+=1
        if M not in S: mf+=1
        if sum(J)+sum(M)!=sum(x)+sum(y): mv+=1
chk("pairs tested", n*(n-1)//2, 475800)
chk("join failures", jf, 0)
chk("meet failures", mf, 0)
chk("rank-modularity violations", mv, 0)

lev=Counter(sum(c) for c in L)
chk("rank levels", len(lev), 18)
chk("widest level", max(lev.values()), 122)
chk("  at rank", max(lev,key=lev.get), 11)

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
chk("covers among join-irreducibles", ed, 20)

dv=0
random.seed(0); sm=random.sample(L,40)
for x in sm:
    for y in sm:
        for z in sm:
            if tuple(max(p,min(q,r)) for p,q,r in zip(x,y,z))!=tuple(min(max(p,q),max(p,r)) for p,q,r in zip(x,y,z)): dv+=1
chk("distributivity violations /64,000 triples", dv, 0)
lg=[lev[r] for r in sorted(lev)]
chk("rank profile log-concave", all(lg[i]**2>=lg[i-1]*lg[i+1] for i in range(1,len(lg)-1)), True)

# coupling removed -> 1000, excluded 24 all f=0 g=3
L2=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,3)+1)]  # replace g<=2(2f+1) coupling by flat g<=q,g<=3
chk("coupling removed -> cells", len(L2), 1000)
diff=set(L2)-S
chk("excluded cells", len(diff), 24)
chk("all excluded have f=0, g=3", all(c[5]==0 and c[6]==3 for c in diff), True)

# cylinder cross-sections
prof=[]
for q in sorted(set(c[3] for c in L)):
    Aq=set((c[0],c[1],c[2],c[7]) for c in L if c[3]==q)
    Bq=set((c[4],c[5],c[6]) for c in L if c[3]==q)
    act=sum(1 for c in L if c[3]==q)
    prof.append((q,len(Aq),len(Bq),len(Aq)*len(Bq),act))
chk("cylinder profile exact", [(p[3],p[4]) for p in prof],
    [(165,165),(330,330),(345,345),(136,136)])

print()
print("rank profile:", " ".join(str(lev[r]) for r in sorted(lev)))
print("cylinder:", " | ".join(f"q={p[0]}: |A|={p[1]} |B|={p[2]} -> {p[4]}" for p in prof))
print()
print(f"{'ALL INVARIANTS VERIFIED' if all(ok) else 'MISMATCHES PRESENT'}  ({sum(ok)}/{len(ok)})")

# regenerate the enumeration file
with open('/mnt/user-data/outputs/lambda_976_cells.txt','w') as fh:
    fh.write(
     "Lambda — THE LACH CYLINDER, COMPLETE ENUMERATION (rebuilt 2026-07-31)\n"
     "Built from §2.1's seven constraints at caps (n≤3, e≤3, ℓ≤1, k≤3), k≥1.\n"
     "Coordinates: (n, ℓ, k, q, e, f, g, 2S)\n"
     "  n  source shell        q  electrons removed    g  target occupancy\n"
     "  ℓ  source subshell     e  target shell         2S multiplicity\n"
     "  k  source occupancy    f  target subshell\n"
     "Constraints: ℓ≤n−1 · k≤2(2ℓ+1) · q≤k · f≤e−1 · g≤2(2f+1) · g≤q · 2S≤k\n"
     "976 cells · E(X)=0 · F(1)=976 · F(−1)=2 · box 6912 · density 14.1%\n"
     + "="*62 + "\n"
     + "\n".join(f"{i+1:4d}  ({c[0]}, {c[1]}, {c[2]}, {c[3]}, {c[4]}, {c[5]}, {c[6]}, {c[7]})   rank {sum(c):2d}"
                 for i,c in enumerate(sorted(L, key=lambda c:(sum(c),c)))) + "\n")
print("enumeration written")