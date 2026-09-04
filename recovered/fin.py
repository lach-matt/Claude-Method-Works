import numpy as np, itertools
rng=np.random.default_rng(11)
def V_seq(y):
    y=np.asarray(y,float); w=np.abs(y[:-2]-y[2:]); e=np.abs(y[1:-1]-0.5*(y[:-2]+y[2:]))
    e=np.where(e<1e-15,1e-15,e); return w.sum()/e.sum()
def Sigma(y):
    Vp=V_seq(y); s=[V_seq(y[k::2]) for k in (0,1) if len(y[k::2])>=3]; return 2*np.mean(s)/Vp
def D3(y): return (np.abs(y[2:]-2*y[1:-1]+y[:-2])/2).mean()/(np.abs(np.diff(y)).mean()+1e-12)
def make(N,amp,snr):
    n=np.arange(N)+8.0; y=-1.0/n**2; y=(y-y.min())/(y.max()-y.min())
    st=np.median(np.abs(np.diff(y)))
    return y+amp*st*((-1)**np.arange(N))+rng.normal(0,st/snr,N)
print("power vs alternation amplitude (N=11, r=20, 1% FPR)")
print(f"{'amp':>6}{'Sigma':>9}{'Delta3':>9}")
for amp in [0.02,0.05,0.10,0.20,0.35]:
    row=[]
    for f in (Sigma,D3):
        null=np.array([f(make(11,0.0,20)) for _ in range(4000)]); thr=np.percentile(null,99)
        alt=np.array([f(make(11,amp,20)) for _ in range(4000)]); row.append(np.mean(alt>thr))
    print(f"{amp:6.2f}{row[0]:9.1%}{row[1]:9.1%}")

# ---------------- lattice-homomorphism characterisation of 4.2 ----------------
print("\n=== §4.2 as a characterisation, not a retraction ===")
L=[(n,l) for n in range(1,5) for l in range(0,min(n-1,2)+1)]
idx={c:i for i,c in enumerate(L)}
def jn(a,b): return (max(a[0],b[0]),max(a[1],b[1]))
def mt(a,b): return (min(a[0],b[0]),min(a[1],b[1]))
def closed(h):
    for a in L:
        for b in L:
            j,m=jn(a,b),mt(a,b)
            if j not in idx or m not in idx: return False
            if h[idx[j]]!=max(h[idx[a]],h[idx[b]]): return False
            if h[idx[m]]!=min(h[idx[a]],h[idx[b]]): return False
    return True
def is_prime_filter(S):
    if not S: return False
    for a in L:                     # upward closed
        if a in S:
            for b in L:
                if jn(a,b)==b and b not in S: return False
    for a in L:                     # meet-prime
        for b in L:
            if mt(a,b) in S and not(a in S or b in S): return False
    return True
cl=[h for h in itertools.product(range(3),repeat=len(L)) if closed(list(h))]
multi=[h for h in cl if len({c[0] for c in L if True})>0 and
       len({h[idx[c]] for c in L})>1 and
       (len({h[idx[c]] for c in L if c[0]==L[0][0]})>0)]
def depends(h,ax):
    for a in L:
        for b in L:
            if a[1-ax]==b[1-ax] and a[ax]!=b[ax] and h[idx[a]]!=h[idx[b]]: return True
    return False
two=[h for h in cl if depends(h,0) and depends(h,1)]
print(f" closure-preserving h into 3 values: {len(cl)};  depending on BOTH coords: {len(two)}")
# every closure-preserving h's sublevel sets should be nested prime filters
allprime=all(is_prime_filter({c for c in L if h[idx[c]]>=k}) for h in cl for k in (1,2))
print(f" every up-set h^-1[k,inf) is a prime filter: {allprime}")
# coordinate filters and their comparability
F={('n',c):{x for x in L if x[0]>=c} for c in range(2,5)}
F.update({('l',c):{x for x in L if x[1]>=c} for c in range(1,3)})
comp=[(a,b) for a in F for b in F if a[0]!=b[0] and F[a]<F[b]]
print(f" cross-coordinate filter containments in L: {len(comp)}  e.g. {comp[:2]}")
# product of chains control
P=[(n,l) for n in range(1,5) for l in range(0,3)]
FP={('n',c):{x for x in P if x[0]>=c} for c in range(2,5)}
FP.update({('l',c):{x for x in P if x[1]>=c} for c in range(1,3)})
compP=[(a,b) for a in FP for b in FP if a[0]!=b[0] and FP[a]<FP[b]]
print(f" same in the 4x3 product of chains: {len(compP)}  -> single-coordinate property holds there")