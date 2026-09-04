import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; cfg_c=g["cfg_c"]; L="spdfg"
print("  WHAT IS THE RELATION OF p AND Nₑ?\n")
print("      p = the number of core orbitals at THIS ℓ.")
print("      Nₑ = the total electron count. p is a COUNT DRAWN FROM Nₑ.\n")
print("      For a core of Nₑ−1 electrons filled by aufbau, p(ℓ) is fixed by Nₑ.")
print("      So they are not independent at all — p is a STEP FUNCTION of Nₑ.\n")
print(f"      {'ℓ':>3}   p as Nₑ rises (the thresholds)")
for l in range(4):
    steps=[]; last=-1
    for ne in range(1,104):
        p=sum(1 for n,ll,o in cfg_c(ne,1) if ll==l and o>0)
        if p!=last: steps.append((ne,p)); last=p
    print(f"      {L[l]:>3}   " + "  ".join(f"Nₑ≥{a}:p={b}" for a,b in steps[:8]))
print()
print("  SO THE PRODUCT FORM IS OVER-PARAMETERISED\n")
print("      √p·Nₑ^k treats p and Nₑ as two coordinates. They are one.")
print("      Within a species and ℓ, p is determined. Across species at fixed p,")
print("      Nₑ varies only inside one 'plateau' of the step function.\n")
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
LL=np.array([r["l"] for r in ROWS],float); D=np.array([r["d"] for r in ROWS])
C=np.array([r["c"] for r in ROWS],float)
keep=(D>0.05)&(P>0)
P,NE,LL,D,C=P[keep],NE[keep],LL[keep],D[keep],C[keep]
print(f"      correlation of ln p with ln Nₑ, overall : "
      f"{np.corrcoef(np.log(P),np.log(NE))[0,1]:.4f}")
for l in range(4):
    m=LL==l
    if m.sum()<8 or len(set(P[m]))<2: continue
    print(f"          at ℓ = {L[l]} : {np.corrcoef(np.log(P[m]),np.log(NE[m]))[0,1]:.4f}"
          f"   ({int(m.sum())} channels)")
print()
print("  THE HONEST VARIABLE:  p IS A FUNCTION OF Nₑ AND ℓ\n")
print("      p(Nₑ, ℓ) counts the shells of angular momentum ℓ below the Fermi level.")
print("      For a hydrogenic filling that is roughly  p ≈ n_max(Nₑ) − ℓ,")
print("      with n_max the outermost principal number.\n")
print(f"      {'ℓ':>3}{'n':>5}{'measured p':>12}{'n_max − ℓ':>12}{'agree':>8}")
for l in range(4):
    ok=0; tot=0; vals=[]
    for ne in range(2,104):
        cfg=cfg_c(ne,1)
        p=sum(1 for n,ll,o in cfg if ll==l and o>0)
        if p==0: continue
        nmax=max(n for n,ll,o in cfg if o>0)
        tot+=1; vals.append((p,nmax-l))
        if p==nmax-l: ok+=1
    if tot: print(f"      {L[l]:>3}{tot:>5}{st.median([a for a,_ in vals]):>12.1f}"
                  f"{st.median([b for _,b in vals]):>12.1f}{100*ok/tot:>7.0f}%")
print()
print("  AND THE CONSEQUENCE FOR THE EQUATION\n")
print("      if p ≈ n_max − ℓ then √p·Nₑ^½ is really √(n_max−ℓ)·√Nₑ, and n_max")
print("      itself grows only as Nₑ^(1/3)-ish. Testing that directly:\n")
Y=np.log(D/C**(-np.maximum(0.86-0.18*np.log(NE),0.02)))
NMAX=np.array([max(n for n,ll,o in cfg_c(int(x)-1,1) if o>0) for x in NE],float)
for nm,X in (("ln p, ln Nₑ",[np.log(P),np.log(NE)]),
             ("ln(n_max−ℓ), ln Nₑ",[np.log(np.maximum(NMAX-LL,1)),np.log(NE)]),
             ("ln n_max, ln Nₑ",[np.log(NMAX),np.log(NE)]),
             ("ln Nₑ alone",[np.log(NE)]),
             ("ln p alone",[np.log(P)]),
             ("ln(p·Nₑ) — one variable",[np.log(P*NE)])):
    Xm=np.column_stack(X+[np.ones(len(Y))])
    b,*_=np.linalg.lstsq(Xm,Y,rcond=None); r=Y-Xm@b
    ex=" ".join(f"{z:+.3f}" for z in b[:-1])
    print(f"      {nm:<28}r² {1-np.var(r)/np.var(Y):>7.4f}   rms {float(np.sqrt(np.mean(r**2))):.4f}   [{ex}]")
