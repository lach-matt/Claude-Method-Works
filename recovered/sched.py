import numpy as np, itertools
rng=np.random.default_rng(1)
SUB=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),
     (6,0),(4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
cells=sorted({(n,l,k) for (n,l) in SUB for k in range(1,2*(2*l+1)+1)})
A=np.array(cells); N=len(cells)
le=np.all(A[:,None,:]<=A[None,:,:],axis=2); np.fill_diagonal(le,True)
DOWN=[np.where(le[:,i])[0] for i in range(N)]   # cells <= i
UP  =[np.where(le[i,:])[0] for i in range(N)]   # cells >= i

def truths():
    n,l,k=A[:,0],A[:,1],A[:,2]
    t={}
    t['linear']   = 1.0*n+1.0*l+0.3*k
    t['steep-n']  = 2.0**n + l + 0.2*k
    t['saturating']=(1-np.exp(-0.6*n))*10 + l + 0.15*k
    t['k-dominant']=0.2*n+0.2*l+1.0*k
    for key in t:
        v=t[key]; t[key]=(v-v.min())/(v.max()-v.min())
    return t
T=truths()

def widths(meas, f):
    """meas: boolean array. returns per-cell width, np.nan if unbracketed one side"""
    w=np.zeros(N); M=np.where(meas)[0]
    for i in range(N):
        if meas[i]: w[i]=0.0; continue
        below=[f[j] for j in DOWN[i] if meas[j]]
        above=[f[j] for j in UP[i]   if meas[j]]
        if below and above: w[i]=min(above)-max(below)
        else: w[i]=1.0                      # unbracketed = full normalised range
    return w

def score(meas,f):
    w=widths(meas,f); un=~meas
    return w[un].mean() if un.any() else 0.0

# ---------------- strategies ----------------
def s_random(B,f,seed):
    r=np.random.default_rng(seed); return r.choice(N,B,replace=False)

def s_extremes_then_random(B,f,seed):
    # measure minimal + maximal elements first (guarantee bracketing), then random
    ext=[i for i in range(N) if le[i].sum()==1 or le[:,i].sum()==1]
    r=np.random.default_rng(seed); rest=[i for i in range(N) if i not in ext]
    return np.array(ext+list(r.choice(rest,max(0,B-len(ext)),replace=False)))[:B]

def s_product(B,f,seed):
    """structure-only: greedily pick argmax |unmeasured up| * |unmeasured down|"""
    meas=np.zeros(N,bool); pick=[]
    for _ in range(B):
        best,bi=-1,None
        for i in range(N):
            if meas[i]: continue
            d=sum(1 for j in DOWN[i] if not meas[j]); u=sum(1 for j in UP[i] if not meas[j])
            v=d*u
            if v>best: best,bi=v,i
        meas[bi]=True; pick.append(bi)
    return np.array(pick)

def s_chainbisect(B,f,seed):
    """decompose into chains (greedy longest-chain peeling), bisect each in turn"""
    remaining=set(range(N)); chains=[]
    while remaining:
        sub=sorted(remaining)
        best=[]
        # longest chain in remaining by DP over topological (sum) order
        order=sorted(sub,key=lambda i:A[i].sum())
        L={i:[i] for i in order}
        for i in order:
            for j in order:
                if j!=i and le[j,i] and j in L and len(L[j])+1>len(L[i]): L[i]=L[j]+[i]
        best=max((L[i] for i in order),key=len)
        chains.append(best); remaining-=set(best)
    chains.sort(key=len,reverse=True)
    # round-robin bisection within chains
    picks=[]; segs={ci:[(0,len(c)-1)] for ci,c in enumerate(chains)}
    done=set()
    while len(picks)<B:
        progressed=False
        for ci,c in enumerate(chains):
            if len(picks)>=B: break
            s=segs[ci]
            if not s: continue
            s.sort(key=lambda ab: ab[1]-ab[0], reverse=True)
            a,b=s.pop(0)
            if b<a: continue
            m=(a+b)//2
            if c[m] not in done:
                picks.append(c[m]); done.add(c[m]); progressed=True
            if m-1>=a: s.append((a,m-1))
            if m+1<=b: s.append((m+1,b))
        if not progressed: break
    while len(picks)<B:
        r=[i for i in range(N) if i not in done]; picks.append(r[0]); done.add(r[0])
    return np.array(picks[:B])

def s_greedy_oracle(B,f,seed):
    """adaptive, sees true values: myopic minimiser of mean width. Upper bound."""
    meas=np.zeros(N,bool); pick=[]
    for _ in range(B):
        best,bi=1e9,None
        for i in range(N):
            if meas[i]: continue
            meas[i]=True; v=score(meas,f); meas[i]=False
            if v<best: best,bi=v,i
        meas[bi]=True; pick.append(bi)
    return np.array(pick)

STRATS={'random':s_random,'extremes+random':s_extremes_then_random,
        'chain-bisect':s_chainbisect,'poset-product':s_product,
        'greedy-oracle(adaptive)':s_greedy_oracle}

BUD=[4,8,12,16,24,32]
print(f"{'strategy':26s}"+"".join(f"{b:>9d}" for b in BUD))
res={}
for name,fn in STRATS.items():
    row=[]
    for B in BUD:
        vals=[]
        for tname,f in T.items():
            reps=8 if name in ('random','extremes+random') else 1
            for r in range(reps):
                sel=fn(B,f,seed=100+r)
                meas=np.zeros(N,bool); meas[sel]=True
                vals.append(score(meas,f))
        row.append(np.mean(vals))
    res[name]=row
    print(f"{name:26s}"+"".join(f"{v:9.4f}" for v in row))
np.save('res.npy',res,allow_pickle=True)