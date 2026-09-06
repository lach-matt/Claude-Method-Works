import numpy as np, random
from itertools import product
random.seed(67)
CONS=[("l<=n-1",  1,0,lambda x:x[0]-1),
      ("k<=4l+2", 2,1,lambda x:4*x[1]+2),
      ("q<=k",    3,2,lambda x:x[2]),
      ("2S<=k",   7,2,lambda x:x[2]),
      ("f<=e-1",  5,4,lambda x:x[4]-1),
      ("g<=4f+2", 6,5,lambda x:4*x[5]+2),
      ("g<=q",    6,3,lambda x:x[3])]
sat=lambda x: all(x[v]<=ub(x) for nm,v,p,ub in CONS)
NC,LC,KC,QC,EC,FC,GC,SC=3,2,3,3,3,2,3,3
AX=[list(range(1,NC+1)),list(range(0,LC)),list(range(1,KC+1)),list(range(0,QC+1)),
    list(range(1,EC+1)),list(range(0,FC)),list(range(0,GC+1)),list(range(0,SC+1))]
BOX=[z for z in product(*AX)]
LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8; grid=np.array(BOX,dtype=np.int32)
def closed_set(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return {tuple(int(v) for v in z) for z in grid[m]}
print("="*90)
print("  THE ANOMALY, DEFINED STRUCTURALLY RATHER THAN FITTED")
print("="*90)
print("""
  Adding y widens the recovered bound on the violated coordinate v. The
  new cells are those the widened bound admits -- but they must STILL
  satisfy every OTHER constraint, including any other bound on v itself.

     FIBRE(y) = { z in BOX : z agrees with y on the constraint that was
                  widened, and satisfies all remaining constraints }

  **If v carries a second bound, the fibre is TRUNCATED by it.**
  g carries two: g <= q and g <= 4f+2. Every other bounded variable
  carries one.
""")
def viol(y): return [i for i,(nm,v,p,ub) in enumerate(CONS) if y[v]>ub(y)]
outside=[z for z in BOX if z not in LAM]
print("  %-12s%10s%12s%14s%16s"%("constraint","actual A","fibre calc","other bounds","truncated by"))
print("  "+"-"*66)
rows=[]
for i,(nm,v,p,ub) in enumerate(CONS):
    front=[y for y in outside if viol(y)==[i] and y[v]-ub(y)==1]
    if not front: continue
    y=front[0]
    A=len(closed_set(np.array(LL+[y],dtype=np.int32)))-len(LAM)-1
    others=[CONS[j][0] for j in range(len(CONS)) if j!=i and CONS[j][1]==v]
    fib=[z for z in BOX if z[v]==y[v] and z[p]==y[p] and
         all(z[v2]<=u2(z) for j,(n2,v2,p2,u2) in enumerate(CONS) if j!=i)]
    rows.append((nm,A,len(fib),len(others),others[0] if others else "—"))
    print("  %-12s%10d%12d%14d%16s"%(nm,A,len(fib),len(others),others[0] if others else "—"))
Aa=np.array([r[1] for r in rows],dtype=float); Fb=np.array([r[2] for r in rows],dtype=float)
print("\n     corr(A, fibre) = %+.3f    ratio A/fibre: min %.2f  max %.2f  median %.2f"
      %(np.corrcoef(Fb,Aa)[0,1],(Aa/Fb).min(),(Aa/Fb).max(),np.median(Aa/Fb)))
print("="*90)
print("  AND THE DECISIVE TEST — REMOVE THE SECOND BOUND ON g")
print("="*90)
print("""
  If domination is the cause, deleting g <= q should make g <= 4f+2 the
  ONLY bound on g, and its amplification should jump into the normal band.
""")
C2=[c for c in CONS if c[0]!="g<=q"]
sat2=lambda x: all(x[v]<=ub(x) for nm,v,p,ub in C2)
LAM2={z for z in BOX if sat2(z)}
LL2=sorted(LAM2)
def closed2(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
base2=closed2(np.array(LL2,dtype=np.int32))
print("     |Lambda| with g<=q     = %d"%len(LAM))
print("     |Lambda| without g<=q  = %d   (closure %d, fixed point %s)"%(len(LAM2),base2,base2==len(LAM2)))
out2=[z for z in BOX if z not in LAM2]
def viol2(y): return [i for i,(nm,v,p,ub) in enumerate(C2) if y[v]>ub(y)]
res2={}
for i,(nm,v,p,ub) in enumerate(C2):
    front=[y for y in out2 if viol2(y)==[i] and y[v]-ub(y)==1]
    if not front: continue
    A=[closed2(np.array(LL2+[y],dtype=np.int32))-len(LAM2)-1 for y in random.sample(front,min(8,len(front)))]
    res2[nm]=np.median(A)
print("\n     %-12s%16s%16s%12s"%("constraint","A/|L| WITH g<=q","A/|L| WITHOUT","change"))
print("     "+"-"*56)
withd={r[0]:r[1]/len(LAM) for r in rows}
for nm in res2:
    a1=withd.get(nm,float('nan')); a2=res2[nm]/len(LAM2)
    print("     %-12s%16.4f%16.4f%12s"%(nm,a1,a2,"%+.0f%%"%(100*(a2-a1)/a1) if a1==a1 and a1>0 else "—"))
g1=withd.get("g<=4f+2",float('nan')); g2=res2.get("g<=4f+2",float('nan'))/len(LAM2)
print("""
{0}
  VERDICT
{0}
""".format("="*90))
if g2==g2 and g1==g1:
    print("     g<=4f+2 amplification:  %.4f with the rival bound, %.4f without"%(g1,g2))
    band=[withd[k] for k in withd if k not in ("g<=4f+2",)]
    lo,hi=min(band),max(band)
    print("     normal band for the other constraints: %.4f to %.4f"%(lo,hi))
    if lo<=g2<=hi*1.5:
        print("""
  **CONFIRMED, AND DEFINED.** Removing the rival bound moves g<=4f+2 from
  %.4f into the normal band. The anomaly is DOMINATION:

     **a constraint that shares its variable with a stricter one is
       almost never active, and violating it therefore contradicts almost
       nothing -- so its fibre is truncated to near-nothing.**

  That is a structural definition, not a fitted curve, and it was in the
  lattice from the start: g is the only variable in the tree with TWO
  incoming bounds."""%g1)
    else:
        print("""
  **NOT CONFIRMED.** Removing the rival bound gives %.4f, still outside
  the normal band %.4f-%.4f. Domination is not the whole cause."""%(g2,lo,hi))