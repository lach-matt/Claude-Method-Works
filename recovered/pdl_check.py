import math
from fractions import Fraction as F
LN="s p d f g h i k".split()
print("  CHECK 1 — THE SEQUENCE DIAGNOSTIC\n")
print("      his E = (N + 3/2) ∓ s·ℓ, lower sign for j = ℓ+½, ordered by energy.")
print("      is the ORDERING produced, or is s tuned to produce it?\n")
def levels(s):
    L=[]
    for N in range(8):
        for l in range(N%2,N+1,2):
            for j,sg in ((l+F(1,2),-1),(l-F(1,2),+1)):
                if j<0: continue
                L.append((F(2*N+3,2)+sg*s*l, N,l,j,int(2*j+1)))
    L.sort(key=lambda x:(x[0],x[1],-x[2]))
    return L
def magics(s):
    c=0; out=[]
    for E,N,l,j,d in levels(s):
        c+=d; out.append(c)
    return out
TRUE={2,8,20,28,50,82,126}
print(f"      {'s':>10}{'cumulative closures hit':>44}{'  count'}")
best=[]
for num,den in ((1,12),(1,10),(1,11),(1,13),(1,14),(1,8),(1,9),(1,16),(1,6),(1,20)):
    s=F(num,den); cum=magics(s)
    hit=sorted(TRUE & set(cum))
    print(f"      {f'{num}/{den}':>10}{str(hit):>44}{len(hit):>7}")
    best.append((len(hit),num,den))
print()
print("      → the number of true magic numbers hit, by s:")
print(f"         best = {max(best)[0]}/7 at s = {max(best)[1]}/{max(best)[2]}")
print()
print("  AND THE RANGE OF s THAT WORKS\n")
ok=[]
for den in range(4,40):
    s=F(1,den); cum=set(magics(s))
    if TRUE <= cum: ok.append(den)
print(f"      s = 1/d gives ALL SEVEN for d in {ok}")
print(f"      → {'UNIQUE' if len(ok)==1 else f'{len(ok)} values work — s is NOT uniquely determined by the sequence'}")
print()
print("  CHECK 2 — IS 149 LOAD-BEARING?\n")
print("      Δ(Δn) = 22329 − 8Δn² + 8Δn, from r_val = 930 (so 1860 = 2·930).")
print("      degeneracy test: perturb r_val by ±1 and ±2.\n")
print(f"      {'r_val':>7}{'Δn values giving a perfect square':>40}")
for rv in (927,928,929,930,931,932,933):
    hits=[]
    for dn in range(0,60,4):
        D=(2*dn-3)**2+12*(2*rv-dn*(dn-1))
        if D>=0 and int(math.isqrt(D))**2==D:
            nu=(-(2*dn-3)+math.isqrt(D))
            if nu>0 and nu%6==0 and (nu//6)%4==0: hits.append((dn,nu//6))
    print(f"      {rv:>7}{str(hits):>40}{'  ← his value' if rv==930 else ''}")