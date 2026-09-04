import json,sys,time
exec(open('tower-2.py').read().split("if __name__")[0])
cells=L8()
C=json.load(open('census.json')); slots=[tuple(x) for x in C['slots']]; steps=[tuple(x) for x in C['steps']]
elems=[('A',)+s for s in slots]+[('S',)+s for s in steps]; E={e:i for i,e in enumerate(elems)}; M=len(elems)
def wit(c):
    m=0
    for (j,v) in slots:
        if c[j]==v: m|=1<<E[('A',j,v)]
    for (i,j,t,phi) in steps:
        if c[j]<=t and c[i]==phi: m|=1<<E[('S',i,j,t)]
    return m
sets=[wit(c) for c in cells]; FULL=(1<<M)-1
carriers=[[s for s in range(len(sets)) if sets[s]>>e&1] for e in range(M)]
K=int(sys.argv[1]); LIMIT=float(sys.argv[2]); t0=time.time(); nodes=0; found=[]; timed_out=False
def rec(cov,excl,chosen,depth):
    global nodes,timed_out
    if timed_out: return
    nodes+=1
    if nodes%200000==0 and time.time()-t0>LIMIT: timed_out=True; return
    if cov==FULL: found.append(tuple(chosen)); return
    r=K-depth
    if r==0: return
    unc=FULL&~cov
    # bound: r sets must cover all uncovered; max coverage among non-excluded sets
    best=0
    for s in range(len(sets)):
        if not excl>>s&1:
            v=bin(sets[s]&unc).count('1')
            if v>best: best=v
    if best*r<bin(unc).count('1'): return
    # branch on uncovered element with fewest allowed carriers
    bestE=None;bestL=None
    for e in range(M):
        if unc>>e&1:
            L=[s for s in carriers[e] if not excl>>s&1]
            if bestL is None or len(L)<len(bestL): bestE,bestL=e,L
            if len(L)==0: return
    ex=excl
    for s in bestL:
        rec(cov|sets[s],ex,chosen+[s],depth+1)
        ex|=1<<s     # duplicate-free: forbid earlier-tried carriers of this element
rec(0,0,[],0)
print(f'K={K} covers found {len(found)} distinct {len(set(tuple(sorted(f)) for f in found))} nodes {nodes} time {time.time()-t0:.1f}s timed_out {timed_out}')
if found: json.dump([[cells[s] for s in f] for f in found],open(f'found{K}.json','w'))