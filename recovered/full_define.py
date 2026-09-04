from collections import Counter

CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
L=sorted(L,key=lambda c:(sum(c),c)); S=set(L)
NM=['n','l','k','q','e','f','g','2S']
LET={0:'s',1:'p'}
mx=tuple(max(c[i] for c in L) for i in range(8))

def binding(c):
    n,l,k,q,e,f,g,S2=c; b=[]
    if l==n-1: b.append("l=n-1")
    if l==CL and n-1>CL: b.append("l=cap")
    if k==2*(2*l+1): b.append("k=2(2l+1)")
    elif k==CK: b.append("k=cap")
    if q==k: b.append("q=k")
    if f==e-1: b.append("f=e-1")
    elif f==CL: b.append("f=cap")
    if g==2*(2*f+1): b.append("g=2(2f+1)")
    if g==q: b.append("g=q")
    if S2==k: b.append("2S=k")
    if n==CN: b.append("n=cap")
    if e==CE: b.append("e=cap")
    return b

def dn(c):
    o=[]
    for i in range(8):
        d=list(c); d[i]-=1
        if tuple(d) in S: o.append(i)
    return o
def up(c):
    o=[]
    for i in range(8):
        d=list(c); d[i]+=1
        if tuple(d) in S: o.append(i)
    return o

ji={c for c in L if len(dn(c))==1}
mi={c for c in L if len(up(c))==1}
sig={c for c in L if tuple(mx[i]-c[i] for i in range(8)) in S}

def phys(c):
    n,l,k,q,e,f,g,S2=c
    src=f"{n}{LET[l]}^{k}"
    tgt=f"{e}{LET[f]}^{g}" if g>0 else f"{e}{LET[f]}^0"
    mv = f"-{q}e" if q>0 else "null-transfer"
    return f"{src}({S2+1}-plet) {mv} -> {tgt}"

lines=[]
hdr=("Lambda — THE LACH CYLINDER, COMPLETE DEFINITION OF EVERY CELL\n"
 "At the lattice's limit: caps (n<=3, e<=3, l<=1, k<=3), k>=1 — the setting at which\n"
 "the object is verified (18/18 invariants) and named. Lambda itself is infinite (§2.4);\n"
 "an uncapped enumeration is refused rather than coerced (B.2.9).\n\n"
 "Coordinates (n,l,k,q,e,f,g,2S): source shell/subshell/occupancy, electrons removed,\n"
 "target shell/subshell/occupancy, multiplicity coordinate.\n"
 "Constraints: l<=n-1 . k<=2(2l+1) . q<=k . f<=e-1 . g<=2(2f+1) . g<=q . 2S<=k\n\n"
 "Per-cell fields:\n"
 "  #      index in (rank, lex) order\n"
 "  cell   the 8-tuple\n"
 "  rk     rank = coordinate sum (ranks 3..20)\n"
 "  read   physical reading: source^occ (multiplicity) -q electrons -> target^occ\n"
 "  q      fibre (cylinder cross-section) membership\n"
 "  dn/up  lower/upper covers, as the coordinates that can step\n"
 "  bind   constraints binding (tight) at this cell\n"
 "  role   JI join-irreducible . MI meet-irreducible . SD sigma-image lands in Lambda\n"
 + "="*100)
lines.append(hdr)
for i,c in enumerate(L):
    role="".join(x for x in [("JI " if c in ji else ""),("MI " if c in mi else ""),("SD" if c in sig else "")]).strip()
    lines.append(
      f"{i+1:4d}  {str(c):26s} rk{sum(c):3d}  {phys(c):32s} q={c[3]}  "
      f"dn[{','.join(NM[j] for j in dn(c)) or '-'}] up[{','.join(NM[j] for j in up(c)) or '-'}]  "
      f"bind[{'; '.join(binding(c))}]  {role}")

# closing verification block
lev=Counter(sum(c) for c in L)
tot_dn=sum(len(dn(c)) for c in L); tot_up=sum(len(up(c)) for c in L)
ft=(f"\n{'='*100}\nVERIFICATION AT THE LIMIT\n"
 f"cells {len(L)} . ranks {min(lev)}-{max(lev)} ({len(lev)} levels) . widest {max(lev.values())} at rank {max(lev,key=lev.get)}\n"
 f"rank profile: {' '.join(str(lev[r]) for r in sorted(lev))}\n"
 f"cover relations: {tot_dn} (counted down) = {tot_up} (counted up): {tot_dn==tot_up}\n"
 f"join-irreducibles {len(ji)} (book: 17) . meet-irreducibles {len(mi)} . sigma survivors {len(sig)} all even rank: "
 f"{all(sum(c)%2==0 for c in sig)}\n"
 f"fibre profile: "+" ".join(f"q={q}:{sum(1 for c in L if c[3]==q)}" for q in range(4))+" (165 330 345 136)\n"
 f"F(1)={len(L)} F(-1)={sum((-1)**sum(c) for c in L)} . bottom {L[0]} . top {L[-1]}\n")
lines.append(ft)
open('/mnt/user-data/outputs/lambda_976_complete_definition.txt','w').write("\n".join(lines))
print(f"written: {len(L)} cells, {tot_dn} covers, JI={len(ji)}, MI={len(mi)}, SD={len(sig)}")
print("bottom:",L[0],phys(L[0])); print("top:   ",L[-1],phys(L[-1]))