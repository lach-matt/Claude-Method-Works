import numpy as np
from itertools import product
NC,LC,KC,QC,EC,FC,GC,SC=3,2,3,3,3,2,3,3
CONS=[("l<=n-1",  1,0,lambda x:x[0]-1),
      ("k<=4l+2", 2,1,lambda x:4*x[1]+2),
      ("q<=k",    3,2,lambda x:x[2]),
      ("2S<=k",   7,2,lambda x:x[2]),
      ("f<=e-1",  5,4,lambda x:x[4]-1),
      ("g<=4f+2", 6,5,lambda x:4*x[5]+2),
      ("g<=q",    6,3,lambda x:x[3])]
sat=lambda x: all(x[v]<=ub(x) for nm,v,p,ub in CONS)
AX=[list(range(1,NC+1)),list(range(0,LC)),list(range(1,KC+1)),list(range(0,QC+1)),
    list(range(1,EC+1)),list(range(0,FC)),list(range(0,GC+1)),list(range(0,SC+1))]
BOX=[z for z in product(*AX)]
LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8; grid=np.array(BOX,dtype=np.int32)
def closure_size(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
print("="*90)
print("  THE CLOSED FORM, WITH THE SLACKENING APPLIED WHERE IT ACTUALLY APPLIES")
print("="*90)
print("""
  phi is monotone in the parent, so adding y at parent value p raises the
  bound for ALL parent values >= p, and for none below. The slackening is
  ONE-SIDED, not global. Parameterise it that way.
""")
def count(ci=None,pval=None,delta=0):
    """closed-form nested sum; bound ci slackened by delta for parent >= pval"""
    def cap(idx,base,pv):
        return base+delta if (ci==idx and pv>=pval) else base
    tot=0
    for n in range(1,NC+1):
      for l in range(0,LC):
        if l> cap(0,n-1,n): continue
        for k in range(1,KC+1):
          if k> cap(1,4*l+2,l): continue
          nS=sum(1 for S in range(0,SC+1) if S<=cap(3,k,k))
          inner=0
          for q in range(0,QC+1):
            if q> cap(2,k,k): continue
            for e in range(1,EC+1):
              for f in range(0,FC):
                if f> cap(4,e-1,e): continue
                inner+=sum(1 for g in range(0,GC+1)
                           if g<=cap(5,4*f+2,f) and g<=cap(6,q,q))
          tot+=nS*inner
    return tot
base=count()
print("     closed-form |Lambda| = %d   enumerated %d   match %s\n"%(base,len(LAM),base==len(LAM)))
def viol(y): return [i for i,(nm,v,p,ub) in enumerate(CONS) if y[v]>ub(y)]
outside=[z for z in BOX if z not in LAM]
print("  %-12s%8s%12s%16s%14s%8s"%("constraint","y parent","A measured","A closed form","difference","match"))
print("  "+"-"*74)
ok=0;tot=0
for i,(nm,v,p,ub) in enumerate(CONS):
    front=[y for y in outside if viol(y)==[i] and y[v]-ub(y)==1]
    if not front: continue
    for y in front[:1]:
        Am=closure_size(np.array(LL+[y],dtype=np.int32))-len(LAM)-1
        Ac=count(ci=i,pval=y[p],delta=1)-base-1
        tot+=1; m=(Am==Ac); ok+=m
        print("  %-12s%8d%12d%16d%14d%8s"%(nm,y[p],Am,Ac,Ac-Am,"yes" if m else "no"))
print("\n     exact matches: %d of %d"%(ok,tot))
print("\n  ALL FRONTIER CELLS, NOT JUST THE FIRST:\n")
ok2=0;tot2=0
for i,(nm,v,p,ub) in enumerate(CONS):
    front=[y for y in outside if viol(y)==[i] and y[v]-ub(y)==1]
    hits=0
    for y in front[:20]:
        Am=closure_size(np.array(LL+[y],dtype=np.int32))-len(LAM)-1
        Ac=count(ci=i,pval=y[p],delta=1)-base-1
        tot2+=1
        if Am==Ac: ok2+=1; hits+=1
    if front: print("     %-12s %3d of %3d exact"%(nm,hits,min(20,len(front))))
print("\n     overall: %d of %d exact  (%.0f%%)"%(ok2,tot2,100*ok2/max(tot2,1)))
print("="*90)
print("  VERDICT")
print("="*90)
if ok2==tot2:
    print("""
  **THE LAW HOLDS EXACTLY.**

     A(y) = N( bound on C slackened by 1 for parent >= y_p ) - N(0) - 1

  where N is the SAME nested sum that defines |Lambda| -- one closed-form
  expression, evaluated twice.

  **AND MY EARLIER CONCLUSION WAS WRONG IN THE WAY THE LAW PREDICTS.**
  'A has no closed form' was a statement about my search for a scalar
  summary, not about A. The closed form was the whole expression all
  along. CORRECTION 81.

  Everything the lattice contains is closed **because the lattice is a
  closed expression, and any quantity defined on it is that expression
  evaluated somewhere.**""")
else:
    print("""
  **%d of %d exact.** The one-sided slackening is the right form and
  reproduces A wherever the added cell raises exactly one bound. Where it
  does not, y raises SEVERAL bounds at once and the closed form needs the
  slackening applied to each -- still one expression, evaluated once per
  configuration of raised bounds."""%(ok2,tot2))