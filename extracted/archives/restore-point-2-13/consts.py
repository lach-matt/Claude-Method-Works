import math, statistics as st, json
import numpy as np
from scipy import stats as SS
print("  EVERY CONSTANT IN THE EQUATION, AND ITS STANDING\n")
K=[("M",1.4907,"amplitude ceiling, δ/√p","fitted","Cd I 1.638, In I 1.667 EXCEED it"),
   ("u₀",3.8937,"peak position, Nₑ/c^⅔ = 49.1","fitted","In I sits at 3.892 — dead on"),
   ("σ",1.6908,"log-width of the window","fitted","too narrow: top band residual 1.073"),
   ("C′",1.0065,"x = C′·e^(−u/2)","MEASURED","unity to within sd 0.179"),
   ("β",2/3,"the collapse variable's exponent","ATTRIBUTED","Thomas–Fermi, Carcassés 2009"),
   ("½",0.5,"exponent on p","CONFIRMED","e(p)=0.4971 with k free"),
   ("0.113",0.113,"ℓ-validity slope","measured","r² 0.868, p 0.007"),
   ("2.5",2.5,"where ℓ-validity vanishes","measured","extrapolated zero-crossing"),
   ("h(d)",0.40,"collapse ceiling at d","measured","K→Ca charge-normalised table"),
   ("h(f)",0.468,"collapse ceiling at f","DERIVED","La ⟨r⟩ = 0.7 a₀, published"),
   ("−1.5",-1.5,"switch centre in Z−T","measured","the d table, D = −2…+1"),
   ("0.40",0.40,"switch width in Z","measured","same table"),
   ("2",2,"free shells in ⌊δ⌋","DERIVED","K and L, where the field is −Z/r"),
   ("2",2,"the gate, ℓ−ℓ_core ≥ 2","measured","p = 2.2×10⁻²⁰")]
print(f"      {'const':<8}{'value':>9}  {'what it is':<32}{'standing':<12}{'note'}")
for n,v,w,s,note in K:
    print(f"      {n:<8}{v:>9.4f}  {w:<32}{s:<12}{note}")
print()
print(f"      fitted {sum(1 for k in K if k[3]=='fitted')} · "
      f"measured {sum(1 for k in K if k[3]=='measured')} · "
      f"derived/attributed/confirmed {sum(1 for k in K if k[3] in ('DERIVED','ATTRIBUTED','CONFIRMED','MEASURED'))}")
print()
print("  WHAT C′ = 1 BUYS — refit the amplitude with x = e^(−u/2) LOCKED\n")
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]+[(48,1,48,1.6381,0,0,3),(49,1,49,1.6667,0,0,3)]
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); LA=np.log(A)
u=np.log(NE)-(2/3)*np.log(C)
X=np.column_stack([u,u**2,np.ones(len(u))])
b,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@b
u0=-b[0]/(2*b[1]); M=math.exp(b[2]+b[0]*u0+b[1]*u0**2); sg=1/math.sqrt(-2*b[1])
print(f"      ln a = {b[0]:.4f}·u {b[1]:+.4f}·u² {b[2]:+.4f}")
print(f"      r² {1-np.var(r)/np.var(LA):.4f}   rms {float(np.sqrt(np.mean(r**2))):.4f}")
print(f"      u₀ = {u0:.4f} (Nₑ/c^⅔ = {math.exp(u0):.1f})   M = {M:.4f}   σ = {sg:.4f}\n")
print("  ARE u₀, M, σ RECOGNISABLE?\n")
for nm,v,cand in (("u₀",u0,[("2e",2*math.e),("π+e/4",math.pi+math.e/4),("4",4.0),
                            ("ln 49",math.log(49)),("2π−2.4",2*math.pi-2.4)]),
                  ("M",M,[("3/2",1.5),("√e",math.sqrt(math.e)),("π/2",math.pi/2),
                          ("e/φ",math.e/1.618)]),
                  ("σ",sg,[("√e",math.sqrt(math.e)),("φ",1.618),("5/3",5/3),
                           ("π/2",math.pi/2)])):
    print(f"      {nm} = {v:.4f}")
    for cn,cv in cand:
        print(f"          {cn:<10}{cv:>8.4f}   ratio {v/cv:.4f}")
print()
print("  AND THE RELATION BETWEEN THEM\n")
print(f"      u₀·σ  = {u0*sg:.4f}      u₀/σ = {u0/sg:.4f}")
print(f"      M·σ   = {M*sg:.4f}      M/σ  = {M/sg:.4f}")
print(f"      u₀ − 2.5 = {u0-2.5:.4f}   (2.5 is where ℓ-validity vanishes)")
print(f"      0.113·(u₀−2.5) = {0.113*(u0-2.5):.4f}   the ℓ-spread AT the peak")
