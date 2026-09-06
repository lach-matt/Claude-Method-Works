import numpy as np
rng=np.random.default_rng(3)
def build(A):
    N=len(A); le=np.all(A[:,None,:]<=A[None,:,:],axis=2); np.fill_diagonal(le,True)
    return N,le,[np.where(le[:,i])[0] for i in range(N)],[np.where(le[i,:])[0] for i in range(N)]
def make_T(A):
    n,l,k=A[:,0],A[:,1],A[:,2]; t={}
    t['linear']=1.0*n+1.0*l+0.3*k; t['steep']=2.0**n+l+0.2*k
    t['sat']=(1-np.exp(-0.6*n))*10+l+0.15*k; t['kdom']=0.2*n+0.2*l+1.0*k
    return {a:(v-v.min())/(v.max()-v.min()) for a,v in t.items()}
def run(A,label):
    N,le,DOWN,UP=build(A); T=make_T(A)
    ext=[i for i in range(N) if le[i].sum()==1 or le[:,i].sum()==1]
    dens=(le|le.T).sum()-N; dens/= N*(N-1)
    def widths(m,f):
        w=np.zeros(N)
        for i in range(N):
            if m[i]: continue
            b=[f[j] for j in DOWN[i] if m[j]]; a=[f[j] for j in UP[i] if m[j]]
            w[i]=(min(a)-max(b)) if (b and a) else 1.0
        return w
    def sc(m,f): return widths(m,f)[~m].mean()
    def static(B):
        m=np.zeros(N,bool); m[ext[:B]]=True
        while m.sum()<B:
            best,bi=-1,None
            for i in range(N):
                if m[i]: continue
                d=sum(1 for j in DOWN[i] if not m[j]); u=sum(1 for j in UP[i] if not m[j])
                if d*u>best: best,bi=d*u,i
            m[bi]=True
        return m
    def adap(B,f):
        m=np.zeros(N,bool); m[ext[:B]]=True
        while m.sum()<B:
            best,bi=1e9,None
            for i in range(N):
                if m[i]: continue
                b=[f[j] for j in DOWN[i] if m[j]]; a=[f[j] for j in UP[i] if m[j]]
                g=(max(b)+min(a))/2 if (b and a) else 0.5
                fg=f.copy(); fg[i]=g; m[i]=True; v=sc(m,fg); m[i]=False
                if v<best: best,bi=v,i
            m[bi]=True
        return m
    def orc(B,f):
        m=np.zeros(N,bool)
        for _ in range(B):
            best,bi=1e9,None
            for i in range(N):
                if m[i]: continue
                m[i]=True; v=sc(m,f); m[i]=False
                if v<best: best,bi=v,i
            m[bi]=True
        return m
    out=[]
    for B in [16,32,48]:
        s=np.mean([sc(static(B),f) for f in T.values()])
        a=np.mean([sc(adap(B,f),f) for f in T.values()])
        o=np.mean([sc(orc(B,f),f) for f in T.values()])
        out.append((B,s,a,o,s/a,a/o))
    print(f"\n{label}  |P|={N} density={dens:.3f} maximal={sum(1 for i in range(N) if le[i].sum()==1)}")
    print(f"{'B':>4}{'static':>9}{'adaptive':>10}{'oracle':>9}{'adapt gain':>12}{'gap to orc':>12}")
    for B,s,a,o,g1,g2 in out: print(f"{B:4d}{s:9.4f}{a:10.4f}{o:9.4f}{g1:11.2f}x{g2:11.2f}x")

SUB=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),
     (6,0),(4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
run(np.array(sorted({(n,l,k) for (n,l) in SUB for k in range(1,2*(2*l+1)+1)})),"Lambda (real)")
# plain 3D box with matched size
run(np.array([(a,b,c) for a in range(1,6) for b in range(1,6) for c in range(1,6)])[:118],"3D box 5x5x5")
# random 3-coordinate cloud, matched N
run(rng.integers(1,15,size=(118,3)),"random 3-coord cloud")