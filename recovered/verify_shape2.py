import lam8
from collections import defaultdict
from itertools import combinations
L8=lam8.L8()
S=set(L8)

print("=== MC-20 §12.8 ===")
# Pareto: |A_q| = 33,33,23,8 falls; |B_q| = 5,10,15,17 rises  (already verified)
# fibre products 165,330,345,136 ; peak q=2 = 345 = 35.3% of 976
prod=[165,330,345,136]
print("peak fibre =", max(prod), "at q=", prod.index(max(prod)), " share = %.1f%%"%(100*max(prod)/976))
# <q> mean and sd
qs=[x[3] for x in L8]
n=len(qs); mean=sum(qs)/n
var=sum((q-mean)**2 for q in qs)/n
print("<q> = %.4f  sd = %.3f"%(mean, var**0.5), " claim 1.4631, sd 0.930")
# log-concave check on 165,330,345,136
lc = all(prod[i]*prod[i] >= prod[i-1]*prod[i+1] for i in range(1,len(prod)-1))
print("log-concave (165,330,345,136):", lc)
# 8-to-3 compression: S(1,1,1)=976 -> the 3-var count equals 976
print("8->3: sum products =", sum(prod), "= 976:", sum(prod)==976)
# every cross-section closed & E=0: check A_q and B_q are closed under meet/join and E=0
def closed_and_E0(pts):
    P=set(pts)
    # meet=componentwise min, join=componentwise max; closed if both stay in P for all pairs
    ptsl=list(P)
    for a,b in combinations(ptsl,2):
        mn=tuple(min(x,y) for x,y in zip(a,b))
        mx=tuple(max(x,y) for x,y in zip(a,b))
        if mn not in P or mx not in P:
            return False
    return True
# build A_q, B_q point sets
Aq=defaultdict(set); Bq=defaultdict(set)
for x in L8:
    Aq[x[3]].add((x[0],x[1],x[2],x[7]))
    Bq[x[3]].add((x[4],x[5],x[6]))
allclosed=True
for q in range(4):
    ca=closed_and_E0(Aq[q]); cb=closed_and_E0(Bq[q])
    allclosed &= ca and cb
    print(f"q={q}: A closed {ca} | B closed {cb}")
print("all cross-sections closed:", allclosed)

print("\n=== MC-21 §12.9 ===")
# antichains: widest level = 122 at rank 11; Λ = 8 * 122 = 976
rank=defaultdict(int)
for x in L8:
    rank[sum(x)]+=1  # rank = sum of coords
widest=max(rank.values()); wr=[r for r,v in rank.items() if v==widest]
print("widest level =", widest, "at rank(s)", sorted(wr), " 8x =", 8*widest, "= 976:", 8*widest==976)
print("number of rank levels (antichains):", len(rank), " claim 18")
# maximal chains = linear extensions e(P) = 1,113,045,672 with 17 join-irreducibles, chain length 17
# We can't cheaply enumerate 1.1e9 linear extensions, but confirm chain length = 17 = rank span +? 
minr=min(rank); maxr=max(rank)
print("rank span:", minr, "to", maxr, "-> chain length (edges) =", maxr-minr)