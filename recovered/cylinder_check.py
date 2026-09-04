import sys; sys.path.insert(0,'/home/claude/method')
import method_tower as mt
from collections import defaultdict
L=sorted(set(mt.base((3,3,1,3,1))))
# cell = (n,l,k,q,e,f,g,2S)
A=defaultdict(set); B=defaultdict(set); byq=defaultdict(int)
for (n,l,k,q,e,f,g,S2) in L:
    A[q].add((n,l,k,S2)); B[q].add((e,f,g)); byq[q]+=1
print('  THE CYLINDER FACTORISATION, RECHECKED')
print('  %-4s %8s %8s %10s %10s %6s' % ('q','|A(q)|','|B(q)|','product','actual','match'))
tot=0
for q in sorted(byq):
    pa,pb=len(A[q]),len(B[q]); pr=pa*pb; tot+=pr
    print('  %-4d %8d %8d %10d %10d %6s' % (q,pa,pb,pr,byq[q],pr==byq[q]))
print('  %-4s %8s %8s %10d %10d %6s' % ('SUM','','',tot,len(L),tot==len(L)))
print()
print('  book states: 33/5=165, 33/10=330, 23/15=345, 8/17=136, sum 976')
print('  computed   : %s' % ', '.join('%d/%d=%d'%(len(A[q]),len(B[q]),len(A[q])*len(B[q])) for q in sorted(byq)))
print('  reproduces : %s' % (tot==976 and len(L)==976))
print()
print('  AND THE LOCAL CLOSURE CLAIM  (12.8.5)')
def E(S,d):
    from itertools import product
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            ph[(i,j)]=o
    return sum(1 for x in product(*vals)
               if all(x[i]<=ph[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(S)
print('  %-4s %10s %10s' % ('q','E(A_q)','E(B_q)'))
allz=True
for q in sorted(byq):
    ea,eb=E(A[q],4),E(B[q],3)
    if ea or eb: allz=False
    print('  %-4d %10d %10d' % (q,ea,eb))
print('  every cross-section closed: %s   (E(Lambda) = %d)' % (allz, E(set(L),8)))
print()
print('  THE PARETO FRONTIER  (12.8.1)')
print('     |A(q)| falls %s while |B(q)| rises %s'
      % ([len(A[q]) for q in sorted(byq)],[len(B[q]) for q in sorted(byq)]))
mono=all(len(A[q])>=len(A[q+1]) for q in sorted(byq)[:-1]) and all(len(B[q])<=len(B[q+1]) for q in sorted(byq)[:-1])
print('     monotone in both directions, no q improves both: %s' % mono)
m=sum(q*byq[q] for q in byq)/len(L)
print('     <q> = %.4f   (book: 1.4631)' % m)