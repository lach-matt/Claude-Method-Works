from itertools import product, combinations
print("="*90)
print("  APPLYING DILWORTH–LARSON–SIGGERS TO Λ ITSELF")
print("="*90)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM=sorted({z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)})
d=8; NM=['n','l','k','q','e','f','g','2S']
Ls=set(LAM)
print("\n     |Λ| = %d   d = %d   alphabets %s"%(len(LAM),d,[len(a) for a in AX]))
print("     Σ(|A_i| − 1) = %d"%sum(len(a)-1 for a in AX))
le=lambda x,y: all(x[i]<=y[i] for i in range(d))
bot=tuple(min(x[i] for x in LAM) for i in range(d))
top=tuple(max(x[i] for x in LAM) for i in range(d))
print("     bottom %s   top %s   both in Λ : %s"%(bot,top,bot in Ls and top in Ls))
print("="*90)
print("  1.  THE JOIN-IRREDUCIBLES")
print("="*90)
J=[]
for x in LAM:
    below=[y for y in LAM if le(y,x) and y!=x]
    if not below: continue
    j=tuple(max(y[i] for y in below) for i in range(d))
    if j!=x: J.append(x)
print("\n     **|J(Λ)| = %d**   (the book states seventeen)"%len(J))
print("     Σ(|A_i| − 1) = %d   equal : %s"%(sum(len(a)-1 for a in AX),len(J)==sum(len(a)-1 for a in AX)))
print("="*90)
print("  2.  IS THE EMBEDDING TIGHT?  (Siggers Lemma 5.1(iii))")
print("="*90)
print("""
  **Tight ⟺ L and P have the same height.** Height of Λ = length of a maximal
  cover chain from bottom to top; height of the box = Σ(|A_i| − 1).
""")
import collections
rank={x:sum(x[i]-bot[i] for i in range(d)) for x in LAM}
h=max(rank.values())
print("     height of Λ                 : %d"%h)
print("     height of the box Σ(|A_i|−1) : %d"%sum(len(a)-1 for a in AX))
print("     **tight : %s**"%(h==sum(len(a)-1 for a in AX)))
print("="*90)
print("  3.  DOES J(Λ) DECOMPOSE INTO THE d AXES AS CHAINS?")
print("="*90)
grp=collections.defaultdict(list)
for x in J:
    ax=tuple(i for i in range(d) if x[i]>bot[i])
    grp[ax].append(x)
print("\n  %26s%8s%12s"%("axes above bottom","count","a chain?"))
print("  "+"-"*50)
def is_chain(T): return all(le(x,y) or le(y,x) for x,y in combinations(T,2))
allsingle=True; allch=True
for k in sorted(grp,key=lambda t:(len(t),t)):
    v=grp[k]
    nm="+".join(NM[i] for i in k)
    if len(k)!=1: allsingle=False
    c=is_chain(v); allch&=c
    print("  %26s%8d%12s"%(nm,len(v),c))
print("\n     every join-irreducible carried by ONE axis : %s"%allsingle)
print("     every axis group is a chain                : %s"%allch)
print("     number of groups                           : %d   (d = %d)"%(len(grp),d))
print("="*90)
print("  4.  WIDTH OF J(Λ)")
print("="*90)
inc=[(x,y) for x,y in combinations(J,2) if not le(x,y) and not le(y,x)]
best=1
for k in range(2,min(len(J),9)+1):
    found=False
    for T in combinations(J,k):
        if all((x,y) in inc or (y,x) in inc for x,y in combinations(T,2)): found=True; break
    if found: best=k
    else: break
print("\n     **width(J(Λ)) = %d**      d = %d      width ≤ d : %s"%(best,d,best<=d))
print("""
  **By Dilworth, J(Λ) decomposes into width(J) chains; by Larson each such
  decomposition is a TIGHT embedding into that many chains.** So if the width
  equals d and the groups above are the chains, **Λ's embedding is exactly the
  one the theory predicts, and nothing about it is open.**
""")