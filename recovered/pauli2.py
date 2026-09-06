import math
import numpy as np
TRUE=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
      (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
L="spdfg"
b0,b1,b2=-2.2402,1.3250,-0.1602
def a_of(ne):
    if ne<2: return 0.0
    u=math.log(ne)
    return math.exp(b0+b1*u+b2*u*u)
def build(af,lmax=3,nmax=8):
    occ={}; seq=[]; ne=0
    while ne<118:
        a=af(max(ne,2)); best=None
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
print("  WITH THE MEASURED a(u),  u = ln Nₑ\n")
s=build(a_of)
m=0
for i in range(min(len(s),len(TRUE))):
    if s[i]==TRUE[i]: m+=1
    else: break
print(f"      built : " + "  ".join(f"{n}{L[l]}" for n,l in s[:19]))
print(f"      true  : " + "  ".join(f"{n}{L[l]}" for n,l in TRUE))
print(f"\n      matched in sequence: {m} of {len(TRUE)}")
tot=sum(1 for i in range(min(len(s),len(TRUE))) if s[i]==TRUE[i])
print(f"      matched in position: {tot} of {min(len(s),len(TRUE))}\n")
print("      a at each filling step:")
ne=0; occ={}
for i,(n0,l) in enumerate(s[:14]):
    print(f"          step {i+1:>2}  Nₑ={max(ne,2):>3}  a={a_of(max(ne,2)):.3f}  → {n0}{L[l]}")
    ne+=2*(2*l+1)
print()
print("  WHERE IT BREAKS AND WHAT WOULD FIX IT\n")
if m<len(TRUE):
    print(f"      first divergence at step {m+1}: built {s[m][0]}{L[s[m][1]]},"
          f" true {TRUE[m][0]}{L[TRUE[m][1]]}")
    ne=sum(2*(2*l+1) for n,l in s[:m])
    print(f"      at Nₑ = {ne}, a = {a_of(max(ne,2)):.4f}")
    occ={}
    for n,l in s[:m]: occ[(n,l)]=1
    print(f"      {'ℓ':>3}{'p':>3}{'n₀':>4}{'√p':>8}{'n*':>9}")
    for l in range(4):
        p=sum(1 for (n,ll) in occ if ll==l); n0=p+l+1
        if n0>8: continue
        print(f"      {L[l]:>3}{p:>3}{n0:>4}{math.sqrt(p):>8.3f}"
              f"{n0-a_of(max(ne,2))*math.sqrt(p):>9.4f}")
    print()
    tl=TRUE[m]; bl=s[m]
    pt=sum(1 for (n,ll) in occ if ll==tl[1]); pb=sum(1 for (n,ll) in occ if ll==bl[1])
    A=a_of(max(ne,2))
    need=(tl[0]-bl[0])/(math.sqrt(pt)-math.sqrt(pb)) if pt!=pb else float('nan')
    print(f"      for {tl[0]}{L[tl[1]]} to win, a must exceed {need:.4f}"
          f"   (it is {A:.4f})")