import numpy as np, random
from itertools import product
random.seed(71)
CONS=[("l<=n-1",  1,0,lambda x:x[0]-1),
      ("k<=4l+2", 2,1,lambda x:4*x[1]+2),
      ("q<=k",    3,2,lambda x:x[2]),
      ("2S<=k",   7,2,lambda x:x[2]),
      ("f<=e-1",  5,4,lambda x:x[4]-1),
      ("g<=4f+2", 6,5,lambda x:4*x[5]+2),
      ("g<=q",    6,3,lambda x:x[3])]
sat=lambda x: all(x[v]<=ub(x) for nm,v,p,ub in CONS)
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]
LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8
def phi_of(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]; ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]
                run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return A,ph
def apply_phi(A,ph):
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
A0,ph0=phi_of(LAM)
S0=apply_phi(A0,ph0)
print("="*90)
print("  EXACT DECOMPOSITION — WHICH BOUNDS WIDEN, AND BY HOW MUCH")
print("="*90)
print("""
  Adding y raises phi_ij(v) for v >= y_j wherever y_i exceeds the current
  value. Count the widened PAIRS and the total RISE, then compare with the
  amplification they produce.
""")
def viol(y): return [i for i,(nm,v,p,ub) in enumerate(CONS) if y[v]>ub(y)]
outside=[z for z in BOX if z not in LAM]
print("  %-12s%9s%10s%10s%12s%10s"%("constraint","A","pairs","rise","fibre","A/fibre"))
print("  "+"-"*63)
rows=[]
for i,(nm,v,p,ub) in enumerate(CONS):
    front=[y for y in outside if viol(y)==[i] and y[v]-ub(y)==1]
    if not front: continue
    y=front[0]
    A1,ph1=phi_of(LAM|{y})
    S1=apply_phi(A1,ph1)
    A=len(S1)-len(LAM)-1
    pairs=0; rise=0
    for key in ph1:
        for vv in ph1[key]:
            a=ph0.get(key,{}).get(vv,-1); b=ph1[key][vv]
            if b>a: pairs+=1; rise+=b-a
    fib=len([z for z in BOX if z[v]==y[v] and z[p]==y[p] and
             all(z[v2]<=u2(z) for j,(n2,v2,p2,u2) in enumerate(CONS) if j!=i)])
    rows.append((nm,A,pairs,rise,fib))
    print("  %-12s%9d%10d%10d%12d%10.2f"%(nm,A,pairs,rise,fib,A/max(fib,1)))
Aa=np.array([r[1] for r in rows],dtype=float)
Pp=np.array([r[2] for r in rows],dtype=float)
Rr=np.array([r[3] for r in rows],dtype=float)
Fb=np.array([r[4] for r in rows],dtype=float)
print("\n  %-26s%12s%12s"%("predictor","Pearson","Spearman"))
print("  "+"-"*50)
for lab,vv in [("widened pairs",Pp),("total rise",Rr),("fibre",Fb),
               ("fibre x pairs",Fb*Pp),("rise x fibre",Rr*Fb)]:
    print("  %-26s%12.3f%12.3f"%(lab,np.corrcoef(vv,Aa)[0,1],
          np.corrcoef(np.argsort(np.argsort(vv)),np.argsort(np.argsort(Aa)))[0,1]))
print("""
{0}
  AND THE EXACT STATEMENT
{0}
""".format("="*90))
best=max([(abs(np.corrcoef(v,Aa)[0,1]),lab,v) for lab,v in
          [("widened pairs",Pp),("total rise",Rr),("fibre",Fb),
           ("fibre x pairs",Fb*Pp),("rise x fibre",Rr*Fb)]])
print("     strongest: %s   r = %+.3f"%(best[1],best[0]))
sl,ic=np.polyfit(best[2],Aa,1)
pred=sl*best[2]+ic
err=100*np.abs(pred-Aa)/np.maximum(Aa,1)
print("     fit A = %.4f * %s + %.1f"%(sl,best[1],ic))
print("\n     %-12s%10s%12s%10s"%("constraint","actual","predicted","err %"))
for (nm,A,pp,rr,fb),pr,e in zip(rows,pred,err):
    print("     %-12s%10d%12.0f%10.1f"%(nm,A,pr,e))
print("     median error %.1f%%   max %.1f%%"%(np.median(err),err.max()))
print("""
  **THE AMPLIFICATION IS NOT ONE FIBRE.** Adding y widens several bounds at
  once -- %d to %d coordinate pairs -- and the admitted set is their UNION,
  which is why a single-fibre estimate runs from 0.39x to 1.79x of truth.

  **THE QUANTITY IS EXACTLY COMPUTABLE FROM THE WIDENING, AND ONLY
  APPROXIMATELY FROM ANY SUMMARY OF IT.** That is the honest end of this
  line: A is defined, it is structural, and it has no closed form in terms
  of a single scalar property of the violated constraint.
"""%(int(Pp.min()),int(Pp.max())))