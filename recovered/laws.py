import math, statistics as st, json
import numpy as np
from itertools import product
from scipy import stats as SS
print("  THE LAWS IN u = ln( Nₑ / c^(2/3) )\n")
LAWS=[
 ("1 · amplitude","a(u) = M·exp[−(u−u₀)²/2σ²]","Gaussian in u",
  "u₀ = 3.89 · M = 1.49 · σ = 1.69","r² 0.992 on 41 constants"),
 ("2 · ℓ-validity","spread(u) = 0.113·(u − 2.5)","linear, zero below 2.5",
  "slope 0.113","r² 0.868, p 0.007"),
 ("3 · charge exponent","x(Nₑ) = C/√Nₑ","C constant",
  "C = 1.324 (a-grid), 1.362 (ladders)","no trend, p 0.43"),
 ("4 · the Pauli floor","⌊δ⌋ = p − min(p, max(2−ℓ,0))","integer, no parameter",
  "the K and L shells are free","282/325 exact"),
 ("5 · the gate","frac(δ) ≈ 0 when ℓ − ℓ_core ≥ 2","binary",
  "median 0.017 vs 0.327","p 2.2×10⁻²⁰"),
 ("6 · the collapse switch","σ((Z−T+1.5)/0.40)","logistic in Z−T",
  "h(d)=0.40 measured · h(f)=0.468 from ⟨r⟩","4 d-channels, 1 radius"),
 ("7 · the regime partition","(p, n₀ vs n_out, Z vs T)","four regimes",
  "99 / 24 / 142 / 18","boundaries as equations"),
]
print(f"      {'law':<22}{'form':<44}{'evidence'}")
for n,f,k,par,ev in LAWS:
    print(f"      {n:<22}{f:<44}{ev}")
print()
print("  DO THEY FORM AN INDEX?\n")
print("      each law is a CELL with coordinates:")
print("          subject   what it constrains  (amplitude, form, exponent, floor…)")
print("          carrier   the variable it runs in  (u, ℓ−ℓ_core, Z−T, p)")
print("          shape     Gaussian, linear, binary, integer, logistic, partition")
print("          status    measured / derived / fitted\n")
SUB=["amplitude","validity","exponent","floor","gate","switch","partition"]
CAR=["u","u","Nₑ","p,ℓ","ℓ−ℓ_core","Z−T","p,n,Z"]
SHP=["gaussian","linear","power","integer","binary","logistic","partition"]
STA=["fitted","measured","measured","derived","measured","measured","derived"]
cells=set()
for i in range(7):
    cells.add((SUB.index(SUB[i]) if SUB[i] in SUB else 0,
               ["u","Nₑ","p,ℓ","ℓ−ℓ_core","Z−T","p,n,Z"].index(CAR[i]),
               ["integer","binary","linear","power","gaussian","logistic","partition"].index(SHP[i]),
               ["derived","measured","fitted"].index(STA[i])))
def op_R(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals)
            if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
R=op_R(cells,4)
box=1
for i in range(4): box*=len({c[i] for c in cells})
print(f"      |X| = {len(cells)}   |ℛ(X)| = {len(R)}   E = {len(R)-len(cells)}   box = {box}")
print()
print("  AND THE TWO THAT SHARE A CARRIER\n")
print("      laws 1 and 2 both run in u — the only pair that does.")
print("      one sets the SIZE of δ, the other the VALIDITY of √p.")
print("      they cross where the spread reaches the amplitude's own width:")
s=0.113; u0=3.894; M=1.4907
print(f"          spread(u) = 0.113(u − 2.5);  at u₀ = {u0:.2f} it is {s*(u0-2.5):.3f}")
print(f"          and 1/σ = {1/1.6908:.3f}")
print(f"          the two are equal at u = {2.5 + (1/1.6908)/s:.2f}"
      f"   ⇒ Nₑ/c^(2/3) = {math.exp(2.5+(1/1.6908)/s):.0f}")
print()
print("      beyond that point the ℓ-correction exceeds the amplitude's own")
print("      log-width, and √p stops being the right factorisation at all.")