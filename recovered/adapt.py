import numpy as np
exec(open('sched.py').read().split('# ---------------- strategies')[0])
def widths(meas,f):
    w=np.zeros(N)
    for i in range(N):
        if meas[i]: continue
        b=[f[j] for j in DOWN[i] if meas[j]]; a=[f[j] for j in UP[i] if meas[j]]
        w[i]=(min(a)-max(b)) if (b and a) else 1.0
    return w
def score(m,f): un=~m; return widths(m,f)[un].mean()
ext=[i for i in range(N) if le[i].sum()==1 or le[:,i].sum()==1]

def oracle(B,f):
    m=np.zeros(N,bool)
    for _ in range(B):
        best,bi=1e9,None
        for i in range(N):
            if m[i]: continue
            m[i]=True; v=score(m,f); m[i]=False
            if v<best: best,bi=v,i
        m[bi]=True
    return m
def static_product(B):
    m=np.zeros(N,bool); m[ext]=True
    while m.sum()<B:
        best,bi=-1,None
        for i in range(N):
            if m[i]: continue
            d=sum(1 for j in DOWN[i] if not m[j]); u=sum(1 for j in UP[i] if not m[j])
            if d*u>best: best,bi=d*u,i
        m[bi]=True
    return m
def adaptive_mid(B,f):
    """implementable: uses ONLY measured values. Assumes an unmeasured cell sits at
       the midpoint of its current bracket, picks the cell minimising resulting mean width."""
    m=np.zeros(N,bool); m[ext]=True
    while m.sum()<B:
        w=widths(m,f)
        best,bi=1e9,None
        for i in range(N):
            if m[i]: continue
            b=[f[j] for j in DOWN[i] if m[j]]; a=[f[j] for j in UP[i] if m[j]]
            guess=(max(b)+min(a))/2 if (b and a) else 0.5
            fg=f.copy(); fg[i]=guess; m[i]=True
            v=score(m,fg); m[i]=False
            if v<best: best,bi=v,i
        m[bi]=True
    return m

print("=== POSET (118 cells, comparability 0.542) ===")
print(f"{'B':>4} {'static-product':>15} {'adaptive-midpoint':>19} {'oracle':>9} {'adapt gain':>11}")
for B in [8,12,16,24,32,48]:
    sp=np.mean([score(static_product(B),f) for f in T.values()])
    ad=np.mean([score(adaptive_mid(B,f),f) for f in T.values()])
    orc=np.mean([score(oracle(B,f),f) for f in T.values()])
    print(f"{B:4d} {sp:15.4f} {ad:19.4f} {orc:9.4f} {sp/ad:10.2f}x")

print("\n=== CHAIN control (118 cells, endpoints seeded) ===")
Nc=118; fc=np.linspace(0,1,Nc)
def cw(m,f):
    w=np.zeros(Nc)
    for i in range(Nc):
        if m[i]: continue
        b=[f[j] for j in range(i) if m[j]]; a=[f[j] for j in range(i+1,Nc) if m[j]]
        w[i]=(min(a)-max(b)) if (b and a) else 1.0
    return w
def cs(m,f): return cw(m,f)[~m].mean()
def cbis(B):
    m=np.zeros(Nc,bool); m[0]=m[Nc-1]=True; segs=[(1,Nc-2)]
    while m.sum()<B and segs:
        segs.sort(key=lambda ab:ab[1]-ab[0],reverse=True); a,b=segs.pop(0)
        if b<a: continue
        mid=(a+b)//2; m[mid]=True
        if mid-1>=a: segs.append((a,mid-1))
        if mid+1<=b: segs.append((mid+1,b))
    return m
def corc(B):
    m=np.zeros(Nc,bool)
    for _ in range(B):
        best,bi=1e9,None
        for i in range(Nc):
            if m[i]: continue
            m[i]=True; v=cs(m,fc); m[i]=False
            if v<best: best,bi=v,i
        m[bi]=True
    return m
print(f"{'B':>4} {'bisection':>11} {'oracle':>9} {'ratio':>8}")
for B in [8,16,32,48]:
    b=cs(cbis(B),fc); o=cs(corc(B),fc)
    print(f"{B:4d} {b:11.4f} {o:9.4f} {b/o:7.2f}x")