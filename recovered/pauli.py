import math
import numpy as np
print("  DOES  n* = p + ℓ + 1 − a·√p  GENERATE THE AUFBAU SEQUENCE?\n")
print("      build the table from scratch: at each electron count, fill the ℓ")
print("      with the smallest n*. p(ℓ) counts what is already filled. Pauli")
print("      gives each subshell 2(2ℓ+1). NOTHING is looked up.\n")
TRUE=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
      (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
def build(a,lmax=3,nmax=8):
    occ={}; seq=[]; ne=0
    while ne<118:
        best=None
        for l in range(lmax+1):
            p=sum(1 for (n,ll) in occ if ll==l)
            n0=p+l+1
            if n0>nmax: continue
            ns=n0-a*math.sqrt(p)
            if best is None or ns<best[0]-1e-12: best=(ns,n0,l)
        if best is None: break
        _,n0,l=best
        occ[(n0,l)]=2*(2*l+1); seq.append((n0,l)); ne+=2*(2*l+1)
    return seq
print(f"      {'a':>6}{'matches':>9}{'of':>4}   first divergence")
L="spdfg"
best=None
for a in np.arange(0.0,1.61,0.05):
    s=build(float(a))
    m=0
    for i in range(min(len(s),len(TRUE))):
        if s[i]==TRUE[i]: m+=1
        else: break
    div=f"{s[m][0]}{L[s[m][1]]} vs {TRUE[m][0]}{L[TRUE[m][1]]}" if m<min(len(s),len(TRUE)) else "none"
    if abs(a*100-round(a*100))<1e-9 and round(a*20)==a*20:
        print(f"      {a:>6.2f}{m:>9}{len(TRUE):>4}   {div}")
    if best is None or m>best[0]: best=(m,a,s)
m,a,s=best
print(f"\n      best: a = {a:.2f} reproduces {m} of {len(TRUE)} in sequence\n")
print("      the sequence it builds:")
print("          " + "  ".join(f"{n}{L[l]}" for n,l in s[:20]))
print("      the true aufbau order:")
print("          " + "  ".join(f"{n}{L[l]}" for n,l in TRUE))
print()
print("  THE RANGE OF a THAT WORKS\n")
good=[]
for a in np.arange(0.0,2.01,0.01):
    s=build(float(a))
    m=0
    for i in range(min(len(s),len(TRUE))):
        if s[i]==TRUE[i]: m+=1
        else: break
    good.append((float(a),m))
mx=max(g[1] for g in good)
rng=[a for a,m in good if m==mx]
print(f"      maximum matched = {mx} of {len(TRUE)}")
print(f"      achieved for a from {min(rng):.2f} to {max(rng):.2f}"
      f"   ({len(rng)} values of 201)")
print()
print("      measured a runs 0.07 (C V) to 2.02 (Rn I); for NEUTRALS 0.22 to 2.02.")