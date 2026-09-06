import json,sys,time
exec(open('tower-2.py').read().split("if __name__")[0])
cells=L8()
C=json.load(open('census.json')); slots=[tuple(x) for x in C['slots']]; steps=[tuple(x) for x in C['steps']]
elems=[('A',)+s for s in slots]+[('S',i,j,t) for (i,j,t,phi) in steps]; E={e:i for i,e in enumerate(elems)}; M=len(elems)
def wit(c):
    m=0
    for (j,v) in slots:
        if c[j]==v: m|=1<<E[('A',j,v)]
    for (i,j,t,phi) in steps:
        if c[j]<=t and c[i]==phi: m|=1<<E[('S',i,j,t)]
    return m
sets=[wit(c) for c in cells]; FULL=(1<<M)-1; NS=len(sets)
carriers=[[s for s in range(NS) if sets[s]>>e&1] for e in range(M)]
K=int(sys.argv[1]); a=int(sys.argv[2]); b=int(sys.argv[3]); LIMIT=float(sys.argv[4]); t0=time.time(); nodes=0; found=[]; timed_out=False
def rec(cov,excl,chosen,depth):
    global nodes,timed_out
    if timed_out: return
    nodes+=1
    if nodes%100000==0 and time.time()-t0>LIMIT: timed_out=True; return
    if cov==FULL: found.append(tuple(chosen)); return
    r=K-depth
    if r==0: return
    unc=FULL&~cov; nu=unc.bit_count()
    best=0
    for s in range(NS):
        if not excl>>s&1:
            v=(sets[s]&unc).bit_count()
            if v>best: best=v
    if best*r<nu: return
    bestE=None;bestL=None
    for e in range(M):
        if unc>>e&1:
            L=[s for s in carriers[e] if not excl>>s&1]
            if bestL is None or len(L)<len(bestL): bestE,bestL=e,L
            if not L: return
    ex=excl
    for s in bestL:
        rec(cov|sets[s],ex,chosen+[s],depth+1); ex|=1<<s
# first level, split
e0=min(range(M),key=lambda e:len(carriers[e])); L0=carriers[e0]
print('first element',elems[e0],'carriers',len(L0),'range',a,b)
ex=0
for idx,s in enumerate(L0):
    if a<=idx<b: rec(sets[s],ex,[s],1)
    ex|=1<<s
print(f'K={K} branches [{a},{b}) covers {len(found)} nodes {nodes} time {time.time()-t0:.1f}s timed_out {timed_out}')
json.dump([[cells[s] for s in f] for f in found],open(f'found{K}_{a}_{b}.json','w'))