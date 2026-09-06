import sys; sys.path.insert(0,"/home/claude/work")
from fractions import Fraction as F
LCODE={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6}
def lev(tag):
    nr=int(tag[0]); l=LCODE[tag[1]]; num,den=tag[2:].split('/')
    j=F(int(num),int(den)); N=2*(nr-1)+l
    return dict(tag=tag,nr=nr,l=l,j=j,N=N)
PAIRS=[("2s1/2","1d3/2",+1),("2p3/2","1f5/2",+1),("3p3/2","2f5/2",+1),
       ("2d3/2","3s1/2",-1),("1g7/2","2d5/2",-1),("1h9/2","2f7/2",-1)]
# the validated filling order, from Krane/Wong (R 1367) — magic closures 2,8,20,28,50,82,126
ORDER=["1s1/2","1p3/2","1p1/2","1d5/2","2s1/2","1d3/2","1f7/2","2p3/2","1f5/2",
       "2p1/2","1g9/2","1g7/2","2d5/2","2d3/2","3s1/2","1h11/2","1h9/2","2f7/2",
       "1i13/2","3p3/2","2f5/2","3p1/2"]
CAPS={"1s1/2":2,"1p3/2":4,"1p1/2":2,"1d5/2":6,"2s1/2":2,"1d3/2":4,"1f7/2":8,
      "2p3/2":4,"1f5/2":6,"2p1/2":2,"1g9/2":10,"1g7/2":8,"2d5/2":6,"2d3/2":4,
      "3s1/2":2,"1h11/2":12,"1h9/2":10,"2f7/2":8,"1i13/2":14,"3p3/2":4,
      "2f5/2":6,"3p1/2":2}
tot=0; shell={}
MAGIC=[2,8,20,28,50,82,126]
for t in ORDER:
    tot+=CAPS[t]
    s=next((i for i,m in enumerate(MAGIC) if tot<=m), len(MAGIC))
    shell[t]=s
print("  C3 — THE FALSIFIER. does a SINGLE major shell contain BOTH orientations?")
print("  if not, the regional fitting the field already does is sufficient.\n")
BOUND=["≤2","2-8","8-20","20-28","28-50","50-82","82-126"]
print(f"  {'pair':<20}{'osc N':>7}{'major shell':>14}{'demands'}")
from collections import defaultdict
byN=defaultdict(list); byS=defaultdict(list)
for a,b,sense in PAIRS:
    A,B=lev(a),lev(b)
    sh=BOUND[max(shell[a],shell[b])]
    byN[A['N']].append(sense); byS[sh].append(sense)
    print(f"  {a+' -> '+b:<20}{A['N']:>7}{sh:>14}   4β+α {'>' if sense>0 else '<'} 0")
print("\n  BY OSCILLATOR SHELL N:")
for N in sorted(byN):
    s=set(byN[N])
    print(f"      N = {N}: {len(byN[N])} pairs, senses {sorted(s)}"
          f"   {'BOTH — cannot be split' if len(s)>1 else 'one sense only'}")
print("\n  BY MAJOR SHELL (where κ and μ are fitted as a unit):")
for sh in sorted(byS,key=lambda x:BOUND.index(x)):
    s=set(byS[sh])
    print(f"      {sh:>8}: {len(byS[sh])} pairs, senses {sorted(s)}"
          f"   {'BOTH — cannot be split' if len(s)>1 else 'one sense only'}")
both=[k for k,v in byS.items() if len(set(v))>1]
print(f"\n  VERDICT: {len(both)} major shell(s) contain both orientations: {both}")
print("  -> regional fitting " + ("CANNOT repair it." if both else "IS SUFFICIENT — the claim falls."))