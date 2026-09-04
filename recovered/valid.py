import numpy as np, json, os
def fd(Tv,nodes,order):
    ys=[Tv[x] for x in nodes]
    for _ in range(order): ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def status(Tv,n,k,sig):
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return 'missing'
    want = 1 if (k+1)%2==0 else -1
    floor=5*(2.0**(k+1))*sig
    for s in range(0,len(span)-(k+1)):
        d=fd(Tv,span[s:s+k+2],k+1)
        if d is None: return 'missing'
        if abs(d)<floor: return 'unresolved'
        if np.sign(d)!=want: return 'refused'
    return 'ok'
LIM={'na1.json':(41449.451,'clean'),'k1.json':(35009.8140,'clean'),
 'li1.json':(43487.11420,'clean'),'he1.json':(198310.66637,'clean'),
 'he2.json':(438908.871,'clean'),'li2.json':(610078.4,'clean'),
 'be2.json':(146882.86,'clean'),'mg2.json':(121267.64,'clean'),
 'al1.json':(48278.480,'PERTURBED'),'ga1.json':(48387.634,'PERTURBED'),
 'c2.json':(196664.7,'PERTURBED'),'si2.json':(131838.14,'PERTURBED'),
 'hg2.json':(151280.,'PERTURBED'),'ca2.json':(95751.87,'PERTURBED'),
 'al2.json':(151862.5,'PERTURBED'),'cd2.json':(136374.74,'?'),'zn2.json':(144892.6,'?')}
print("="*84)
print("  DO THE REFUSALS LAND ON THE KNOWN PERTURBERS?")
print("="*84)
print("""
  RATE, not count: refused / (refused + admitted), which is independent of
  channel length. Only cells that are RESOLVED enter the denominator, so
  quotation coarseness cannot bias it.
""")
rows=[]
for fn,(I,tag) in LIM.items():
    p='/home/claude/data/'+fn
    if not os.path.exists(p): continue
    ok=rf=0
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        Tv={n:I-M[n] for n in M if I-M[n]>0}
        if len(Tv)<5: continue
        dg=0
        for v in [M[n] for n in M]:
            s=("%.6f"%v).rstrip('0')
            if '.' in s: dg=max(dg,len(s.split('.')[1]))
        sig=10.0**(-dg) if dg else 1.0
        for k in (1,2,3):
            for n in sorted(Tv):
                s=status(Tv,n,k,sig)
                if s=='ok': ok+=1
                elif s=='refused': rf+=1
    if ok+rf>=10:
        rows.append((fn.replace('.json','').upper(),tag,ok,rf,100*rf/(ok+rf)))
rows.sort(key=lambda r:-r[4])
print("  %-8s%-12s%8s%9s%12s"%("species","expected","admitted","refused","refusal %"))
print("  "+"-"*50)
for sp,tag,ok,rf,rate in rows:
    print("  %-8s%-12s%8d%9d%12.1f"%(sp,tag,ok,rf,rate))
P=[r[4] for r in rows if r[1]=='PERTURBED']
C=[r[4] for r in rows if r[1]=='clean']
print("\n     PERTURBED  n=%d  median %.1f%%   range %.1f–%.1f"%(len(P),np.median(P),min(P),max(P)))
print("     clean      n=%d  median %.1f%%   range %.1f–%.1f"%(len(C),np.median(C),min(C),max(C)))
print("     separation : %.2fx"%(np.median(P)/max(np.median(C),1e-9)))
ranks=sorted(rows,key=lambda r:-r[4])
top=[r[1] for r in ranks[:len(P)]]
print("\n     of the %d highest refusal rates, %d are the ones expected to be perturbed"
      %(len(P),sum(1 for t in top if t=='PERTURBED')))
from itertools import combinations
wins=sum(1 for a in P for c in C if a>c); tot=len(P)*len(C)
print("     pairwise: perturbed > clean in %d of %d comparisons  (%.0f%%)"%(wins,tot,100*wins/tot))
print("="*84)
print("  VERDICT")
print("="*84)
if tot and wins/tot>0.75:
    print("""
  **THE DETECTOR VALIDATES.** Species the literature flags as perturbed
  refuse at a higher rate than species it does not, in %.0f%% of pairwise
  comparisons, on a measure that cannot be biased by channel length or
  quotation coarseness.

  **AND IT USES NO FIT, NO LIMIT AND NO UNCERTAINTY ESTIMATE** -- only the
  signs of finite differences of measured levels, and the quotation floor
  to decide which differences are resolvable at all.
"""%(100*wins/tot))
else:
    print("""
  **NOT VALIDATED. %.0f%% of pairwise comparisons favour the expected
  direction, which is not enough to call it a detector.** The rate
  separates the extremes but not the middle, and the species labels are
  themselves coarse -- 'perturbed' is a property of a CHANNEL, not of a
  species, and this test aggregates over channels.
"""%(100*wins/tot))