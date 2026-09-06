import itertools,sys
sys.setrecursionlimit(10000)
A=[0,1,2]
def cells(n,edges):   # edges (parent,child): child<=parent
    return [c for c in itertools.product(A,repeat=n) if all(c[b]<=c[a] for a,b in edges)]
def steps_slots(X):
    d=len(X[0]); alph=[sorted(set(x[i] for x in X)) for i in range(d)]
    slots=[(j,v) for j in range(d) for v in alph[j]]; steps=[]
    for i in range(d):
        for j in range(d):
            if i==j: continue
            prev=None
            for t in alph[j]:
                phi=max(x[i] for x in X if x[j]<=t)
                if phi!=prev: steps.append((i,j,t,phi)); prev=phi
    return slots,steps
def seed(X):
    slots,steps=steps_slots(X)
    els=[('A',)+s for s in slots]+[('S',i,j,t) for (i,j,t,p) in steps]; E={e:k for k,e in enumerate(els)}; M=len(els); FULL=(1<<M)-1
    def w(c):
        m=0
        for (j,v) in slots:
            if c[j]==v: m|=1<<E[('A',j,v)]
        for (i,j,t,p) in steps:
            if c[j]<=t and c[i]==p: m|=1<<E[('S',i,j,t)]
        return m
    S=[w(c) for c in X]; car=[[s for s in range(len(S)) if S[s]>>e&1] for e in range(M)]
    for K in range(1,12):
        def rec(cov,excl,depth):
            if cov==FULL: return True
            if depth==K: return False
            unc=FULL&~cov
            best=max((bin(S[s]&unc).count('1') for s in range(len(S)) if not excl>>s&1),default=0)
            if best*(K-depth)<unc.bit_count(): return False
            e=min((e for e in range(M) if unc>>e&1),key=lambda e:sum(1 for s in car[e] if not excl>>s&1))
            ex=excl
            for s in car[e]:
                if ex>>s&1: continue
                if rec(cov|S[s],ex,depth+1): return True
                ex|=1<<s
            return False
        if rec(0,0,0): return K,len(steps),len(slots)
shapes={'path':[(0,1),(1,2),(2,3),(3,4),(4,5)],
        'star':[(0,1),(0,2),(0,3),(0,4),(0,5)],
        'caterpillar':[(0,1),(1,2),(2,3),(1,4),(2,5)],
        'binary tree':[(0,1),(0,2),(1,3),(1,4),(2,5)],
        'double star':[(0,1),(0,2),(0,3),(3,4),(3,5)],
        'forest':[(0,1),(1,2),(3,4),(4,5)]}
for nm,ed in shapes.items():
    X=cells(6,ed); K,S,sl=seed(X)
    print(f'{nm:12s} edges {len(ed)} cells {len(X):4d} S steps {S:3d} alphabet {sl} seed {K}')