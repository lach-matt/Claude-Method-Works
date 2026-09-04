import json,sys,time,numpy as np
exec(open('tower-2.py').read().split("if __name__")[0])
cells=L8()
C=json.load(open('census.json')); slots=[tuple(x) for x in C['slots']]; steps=[tuple(x) for x in C['steps']]
elems=[('A',)+s for s in slots]+[('S',i,j,t) for (i,j,t,phi) in steps]; E={e:i for i,e in enumerate(elems)}; M=len(elems)
A=np.zeros((len(cells),M),dtype=np.int16)
for s,c in enumerate(cells):
    for (j,v) in slots:
        if c[j]==v: A[s,E[('A',j,v)]]=1
    for (i,j,t,phi) in steps:
        if c[j]<=t and c[i]==phi: A[s,E[('S',i,j,t)]]=1
NS=len(cells)
K=int(sys.argv[1]); a=int(sys.argv[2]); b=int(sys.argv[3]); LIMIT=float(sys.argv[4]); t0=time.time(); nodes=0; found=[]; timed_out=False
def rec(cov,excl,chosen,depth):
    global nodes,timed_out
    if timed_out: return
    nodes+=1
    if nodes%20000==0 and time.time()-t0>LIMIT: timed_out=True; return
    unc=~cov; nu=int(unc.sum())
    if nu==0: found.append(tuple(chosen)); return
    r=K-depth
    if r==0: return
    allowed=~excl
    sub=A[allowed][:,unc]            # allowed sets × uncovered elements
    if sub.shape[0]==0: return
    gain=sub.sum(1)
    top=np.sort(gain)[-r:]
    if int(top.sum())<nu: return
    cnt=sub.sum(0)
    if int(cnt.min())==0: return
    e_local=int(np.argmin(cnt)); e=np.flatnonzero(unc)[e_local]
    L=np.flatnonzero(A[:,e].astype(bool)&allowed)
    ex=excl.copy()
    for s in L:
        rec(cov|A[s].astype(bool),ex,chosen+[int(s)],depth+1); ex[s]=True
cov0=np.zeros(M,bool); ex0=np.zeros(NS,bool)
cnt=A.sum(0); e0=int(np.argmin(cnt)); L0=np.flatnonzero(A[:,e0])
print('first element',elems[e0],'carriers',len(L0),'range',a,b)
ex=ex0.copy()
for idx,s in enumerate(L0):
    if a<=idx<b: rec(A[s].astype(bool),ex,[int(s)],1)
    ex[s]=True
print(f'K={K} branches [{a},{b}) covers {len(found)} distinct {len(set(tuple(sorted(f)) for f in found))} nodes {nodes} time {time.time()-t0:.1f}s timed_out {timed_out}')
json.dump([[cells[s] for s in f] for f in found],open(f'found{K}_{a}_{b}.json','w'))
