import numpy as np
exec(open('sched.py').read().split('# ---------------- strategies')[0])

def widths(meas,f):
    w=np.zeros(N)
    for i in range(N):
        if meas[i]: continue
        b=[f[j] for j in DOWN[i] if meas[j]]; a=[f[j] for j in UP[i] if meas[j]]
        w[i]= (min(a)-max(b)) if (b and a) else 1.0
    return w
def score(meas,f):
    un=~meas; return widths(meas,f)[un].mean() if un.any() else 0.0
def oracle(B,f):
    meas=np.zeros(N,bool); pick=[]
    for _ in range(B):
        best,bi=1e9,None
        for i in range(N):
            if meas[i]: continue
            meas[i]=True; v=score(meas,f); meas[i]=False
            if v<best: best,bi=v,i
        meas[bi]=True; pick.append(bi)
    return pick

print("=== 1. is the optimal schedule data-dependent? ===")
picks={t:oracle(16,f) for t,f in T.items()}
names=list(T)
for t in names: print(f"  {t:12s} first 8: {[tuple(A[i]) for i in picks[t][:8]]}")
for i in range(len(names)):
    for j in range(i+1,len(names)):
        o=len(set(picks[names[i]])&set(picks[names[j]]))
        print(f"  overlap {names[i]:12s} vs {names[j]:12s}: {o}/16")

print("\n=== 2. cross-application: use one truth's schedule on another ===")
for src in names:
    row=[]
    for dst in names:
        m=np.zeros(N,bool); m[picks[src]]=True; row.append(score(m,T[dst]))
    print(f"  schedule from {src:12s} -> "+" ".join(f"{dst[:4]}:{v:.3f}" for dst,v in zip(names,row)))

print("\n=== 3. structure-only heuristics, seeded with the extremes ===")
ext=[i for i in range(N) if le[i].sum()==1 or le[:,i].sum()==1]
print(f"  extremes = {[tuple(A[i]) for i in ext]}")
def seeded(B,rule,f=None):
    meas=np.zeros(N,bool); pick=list(ext[:B]); meas[pick]=True
    while len(pick)<B:
        best,bi=-1,None
        for i in range(N):
            if meas[i]: continue
            d=sum(1 for j in DOWN[i] if not meas[j]); u=sum(1 for j in UP[i] if not meas[j])
            v = d*u if rule=='product' else d+u if rule=='sum' else min(d,u)
            if v>best: best,bi=v,i
        meas[bi]=True; pick.append(bi)
    return pick
BUD=[8,12,16,24,32]
for rule in ['product','sum','min']:
    row=[]
    for B in BUD:
        p=seeded(B,rule); m=np.zeros(N,bool); m[p]=True
        row.append(np.mean([score(m,f) for f in T.values()]))
    print(f"  extremes+{rule:8s} "+" ".join(f"{v:.4f}" for v in row))
row=[]
for B in BUD:
    v=[]
    for f in T.values():
        p=oracle(B,f); m=np.zeros(N,bool); m[p]=True; v.append(score(m,f))
    row.append(np.mean(v))
print(f"  ORACLE            "+" ".join(f"{v:.4f}" for v in row))

print("\n=== 4. control: same experiment on a 118-cell CHAIN ===")
Nc=118
def cwidths(meas,f):
    w=np.zeros(Nc)
    for i in range(Nc):
        if meas[i]: continue
        b=[f[j] for j in range(i) if meas[j]]; a=[f[j] for j in range(i+1,Nc) if meas[j]]
        w[i]=(min(a)-max(b)) if (b and a) else 1.0
    return w
def cscore(meas,f): un=~meas; return cwidths(meas,f)[un].mean()
fc=np.linspace(0,1,Nc)
def coracle(B):
    meas=np.zeros(Nc,bool); 
    for _ in range(B):
        best,bi=1e9,None
        for i in range(Nc):
            if meas[i]: continue
            meas[i]=True; v=cscore(meas,fc); meas[i]=False
            if v<best: best,bi=v,i
        meas[bi]=True
    return meas
def cbisect(B):
    meas=np.zeros(Nc,bool); segs=[(0,Nc-1)]; c=0
    while c<B and segs:
        segs.sort(key=lambda ab:ab[1]-ab[0],reverse=True); a,b=segs.pop(0)
        m=(a+b)//2
        if not meas[m]: meas[m]=True; c+=1
        if m-1>=a: segs.append((a,m-1))
        if m+1<=b: segs.append((m+1,b))
    return meas
for B in [8,16,32]:
    print(f"  B={B:2d}  oracle {cscore(coracle(B),fc):.4f}   bisection {cscore(cbisect(B),fc):.4f}")