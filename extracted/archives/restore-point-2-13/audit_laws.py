import math, statistics as st, json
import numpy as np
from itertools import product
from collections import defaultdict
from scipy import stats as SS
print("  THE LAW INDEX, AUDITED BY THE DAY'S OWN METHODS\n")
# law, carrier, n used, n available, r2, p-value, standing
LAWS=[
 ("1 amplitude a(u)","u",43,43,0.9920,0.0,"fitted, 3 numbers"),
 ("2 ℓ-spread","p",19,19,0.3555,0.0071,"CORRECTED — was u, was 6 species"),
 ("3 charge exponent","u",15,15,0.9121,0.0,"C′ = 1.0065, no free number"),
 ("4 Pauli floor","p,ℓ",325,325,None,None,"282/325 exact, integer"),
 ("5 the gate","ℓ−ℓ_core",324,324,None,2.2e-20,"binary, median 0.017 vs 0.327"),
 ("6 collapse switch","Z−T",4,53,None,None,"4 channels near threshold of 53"),
 ("7 regime partition","p,n₀,Z",283,283,None,None,"99/24/142/18"),
]
print(f"      {'law':<20}{'carrier':<12}{'used':>6}{'avail':>7}{'r²':>9}{'  standing'}")
for n,c,u_,a_,r2,pv,st_ in LAWS:
    rr=f"{r2:.4f}" if r2 else "—"
    flag="  ← FRACTION OF DATA" if u_<a_*0.5 else ""
    print(f"      {n:<20}{c:<12}{u_:>6}{a_:>7}{rr:>9}   {st_}{flag}")
print()
print("  1 · THE SELECTION AUDIT — was each law fitted on all its data?\n")
print("      law 2 was fitted on 6 of 19 species and gave r² 0.868;")
print("      on all 19 it gives r² 0.044 in u and 0.356 in p. **CORRECTED**")
print("      law 6 is fitted on 4 channels of 53 — the other 49 sit far below")
print("      the threshold and constrain only the tail. **AT RISK**\n")
print("  2 · THE CARRIER AUDIT — is each law in its best carrier?\n")
print("      law 1  : u tested against Nₑ, c, ln Nₑ — u wins by collapse")
print("      law 2  : u vs p — **p WINS**, u contributes nothing (slope +0.006)")
print("      law 3  : Nₑ vs u — **u WINS**, r² 0.912 vs 0.834, and C′ → 1")
print("      law 5  : ℓ−ℓ_core vs ℓ — untested")
print("      law 6  : Z−T vs charge — **charge won earlier** (register 1264)\n")
print("  3 · THE ABSORPTION AUDIT — which pairs are degenerate?\n")
print("      x(Nₑ) vs regime-2 factor : degenerate, 1.234 → 1.03 when x locked")
print("      k vs charge form         : degenerate, k = 0.539 → 0.388")
print("      c^(−C/√Nₑ) vs c·lnNₑ     : degenerate, cross term absorbed")
print("      → every degeneracy found today was between a CHARGE term and")
print("        something else. charge is the coordinate that absorbs.\n")
print("  4 · THE CLOSURE AUDIT — the law index as an object\n")
cells={(0,0),(1,1),(2,0),(3,1),(4,2),(5,3),(6,1)}
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
R=opR(cells,2)
print(f"      (law, carrier) as a 2-coordinate index: |X| = {len(cells)}"
      f"   |ℛ| = {len(R)}   E = {len(R)-len(cells)}")
print(f"      box = {len({c[0] for c in cells})*len({c[1] for c in cells})}\n")
print("  WHAT IS RIGHT\n")
print("      law 3 · the charge exponent. C′ = 1.0065 with sd 0.179 across 15")
print("              sequences, no free number, best carrier confirmed by test.")
print("      law 4 · the Pauli floor. 282/325 exact, integer, derived.")
print("      law 5 · the gate. p = 2×10⁻²⁰ on 324 channels, binary, no parameter.")
print("      law 7 · the regime partition. Boundaries as equations, all channels used.\n")
print("  WHAT IS AT RISK\n")
print("      law 1 · three fitted numbers, and M is exceeded by the two species")
print("              nearest its own peak. u₀ ≈ 4 is untested as a locked value.")
print("      law 2 · corrected once today; now r² 0.356 in p on 19 species.")
print("      law 6 · four channels of fifty-three. h(f) rests on ONE published radius.")
