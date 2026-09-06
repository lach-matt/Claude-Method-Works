import sys,itertools; sys.path.insert(0,'.')
from tower import L8
X=sorted(set(L8())); d=8; S=set(X)
A=[sorted({x[i] for x in X}) for i in range(d)]
phi={}
for i in range(d):
    for j in range(d):
        if i==j: continue
        for t in A[j]: phi[(i,j,t)]=max(y[i] for y in X if y[j]<=t)
# steps: t minimal in A_j at which phi_ij takes its value
steps=[]
for i in range(d):
    for j in range(d):
        if i==j: continue
        prev=None
        for t in A[j]:
            v=phi[(i,j,t)]
            if v!=prev: steps.append((i,j,t)); prev=v
print('steps',len(steps))
cov={s:frozenset(k for k,x in enumerate(X) if x[s[1]]<=s[2] and x[s[0]]==phi[s]) for s in steps}
# minimum set cover, all solutions, branch and bound on size
best=[10**9]; sols=[]
def dfs(chosen,uncov):
    if len(chosen)>best[0]: return
    if not uncov:
        if len(chosen)<best[0]: best[0]=len(chosen); sols.clear()
        sols.append(tuple(sorted(chosen))); return
    if len(chosen)==best[0]: return
    # pick element with fewest covering cells
    s=min(uncov,key=lambda e:len(cov[e]))
    for k in cov[s]:
        if chosen and k<chosen[-1] and False: pass
        dfs(chosen+[k],[e for e in uncov if k not in cov[e]])
dfs([],steps)
sols=sorted(set(sols))
print('seed size',best[0],'minimum covers',len(sols))
common=set.intersection(*[set(s) for s in sols]); print('cells common to all covers',[X[k] for k in common])
tmpl=[k for k,x in enumerate(X) if (x[0],x[1],x[2],x[3],x[5],x[6],x[7])==(3,0,1,1,0,1,1)]
print('unit-template cells',[X[k] for k in tmpl],'covers containing one:',sum(1 for s in sols if any(k in s for k in tmpl)),'of',len(sols))
# lower bound: max number of pairwise-disjoint step sets (greedy) / breadth
print('LB (greedy disjoint steps)',end=' ')
used=set();lb=0
for s in sorted(steps,key=lambda e:len(cov[e])):
    if not (cov[s]&used): used|=cov[s]; lb+=1
print(lb)
open('/tmp/sols.txt','w').write(repr(sols))