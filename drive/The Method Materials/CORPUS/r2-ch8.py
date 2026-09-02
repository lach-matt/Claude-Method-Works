# r2-ch8.py — Phase R2, main Chapter 8 "What Λ is — distributive, modular, Sperner" (chat 70). Run beside tower-2.py.
# usage: python3 r2-ch8.py            (core claims)
#        python3 r2-ch8.py settings   (search for the six settings 976 … 27,873 and generator counts where affordable)
import itertools, importlib.util, sys, random, collections
import numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)

def leq_matrix(A):
    """A: (n,d) int array. returns boolean n×n matrix LE[i,j] = A[i] ≤ A[j] coordinatewise"""
    n=len(A); LE=np.ones((n,n),dtype=bool)
    for c in range(A.shape[1]): LE &= (A[:,c][:,None] <= A[:,c][None,:])
    return LE

def join_irreducibles(A):
    """elements with exactly one lower cover (bottom excluded). returns indices, and the list of lower covers per element"""
    n=len(A); LE=leq_matrix(A); LT=LE & ~np.eye(n,dtype=bool)
    ji=[]; 
    for x in range(n):
        below=np.nonzero(LT[:,x])[0]
        if len(below)==0: continue                       # bottom
        # lower covers: y below x with no z strictly between
        sub=LT[np.ix_(below,below)]                        # sub[i,j] = below[i] < below[j]
        maximal=below[~sub.any(axis=1)]
        if len(maximal)==1: ji.append(x)
    return ji, LE

def width_dilworth(LT):
    """width of a poset given strict-order matrix LT (n×n bool) = n − max matching in the comparability bipartite graph (Hopcroft–Karp)"""
    n=len(LT); adj=[np.nonzero(LT[i])[0].tolist() for i in range(n)]
    matchR=[-1]*n; INF=10**9
    def bfs():
        dist=[0 if matchL[u]==-1 else INF for u in range(n)]; q=collections.deque(u for u in range(n) if matchL[u]==-1); found=False
        while q:
            u=q.popleft()
            for v in adj[u]:
                w=matchR[v]
                if w==-1: found=True
                elif dist[w]==INF: dist[w]=dist[u]+1; q.append(w)
        return found,dist
    def dfs(u,dist):
        for v in adj[u]:
            w=matchR[v]
            if w==-1 or (dist[w]==dist[u]+1 and dfs(w,dist)):
                matchL[u]=v; matchR[v]=u; return True
        dist[u]=INF; return False
    matchL=[-1]*n; m=0
    sys.setrecursionlimit(10000)
    while True:
        found,dist=bfs()
        if not found: break
        for u in range(n):
            if matchL[u]==-1 and dfs(u,dist): m+=1
    return n-m

def chain_partition_and_antichain(LE):
    """small posets only: greedy chain partition via matching, and a maximum antichain by brute force"""
    n=len(LE); LT=LE & ~np.eye(n,dtype=bool)
    w=width_dilworth(LT)
    best=None
    for r in range(w,0,-1):
        for S in itertools.combinations(range(n),r):
            if all(not LT[a,b] and not LT[b,a] for a,b in itertools.combinations(S,2)): best=S; break
        if best: break
    return w,best

L8=np.array(tw.L8(),dtype=np.int16); n8=len(L8)
rank=L8.sum(axis=1); levels=collections.Counter(rank.tolist()); rs=[levels[r] for r in range(rank.min(),rank.max()+1)]
print('|Λ8|',n8,'rank = Σx: min',rank.min(),'max',rank.max(),'midpoint',(rank.min()+rank.max())/2,'centre of mass %.2f'%rank.mean(),'skew %.2f'%(rank.mean()-(rank.min()+rank.max())/2))
print('rank sequence',rs,'max level',max(rs),'at rank',rank.min()+rs.index(max(rs)))
print('log-concave:',all(rs[i]**2>=rs[i-1]*rs[i+1] for i in range(1,len(rs)-1)),'| symmetric:',rs==rs[::-1],'| unimodal:',rs.index(max(rs))==len(rs)-1-rs[::-1].index(max(rs)) and all(rs[i]<=rs[i+1] for i in range(rs.index(max(rs)))) and all(rs[i]>=rs[i+1] for i in range(rs.index(max(rs)),len(rs)-1)))
# modularity on all pairs
J=np.maximum(L8[:,None,:],L8[None,:,:]).sum(axis=2); Mn=np.minimum(L8[:,None,:],L8[None,:,:]).sum(axis=2)
viol=int((J+Mn != rank[:,None]+rank[None,:]).sum()//2); print('rank modularity over all C(976,2) =',n8*(n8-1)//2,'pairs: violations',viol)
# distributivity sample
random.seed(0); bad=0
for _ in range(20000):
    a,b,c=(L8[random.randrange(n8)] for _ in range(3))
    if not np.array_equal(np.minimum(a,np.maximum(b,c)),np.maximum(np.minimum(a,b),np.minimum(a,c))): bad+=1
print('distributive law on 20,000 random triples: failures',bad)
# bounding box
box=int(np.prod(L8.max(axis=0)-L8.min(axis=0)+1)); print('bounding box',box,'occupancy %.1f%%'%(100*n8/box),'| min',L8.min(axis=0).tolist(),'max',L8.max(axis=0).tolist())
# reflections
S=set(map(tuple,L8.tolist())); mx=L8.max(axis=0); mn=L8.min(axis=0)
r1=sum(tuple((mx-x).tolist()) in S for x in L8); r2=sum(tuple((mx+mn-x).tolist()) in S for x in L8); fx=sum(tuple((mx+mn-x).tolist())==tuple(x.tolist()) for x in L8)
print('x ↦ max − x: image in Λ for',r1,'cells | x ↦ max + min − x: image in Λ for',r2,'cells, fixed',fx)
# join-irreducibles, covers in J, down-sets
ji,LE=join_irreducibles(L8); Jset=L8[ji]; m=len(ji); print('join-irreducibles',m,'(57-fold: %.1f)'%(n8/m))
LEJ=LE[np.ix_(ji,ji)]; LTJ=LEJ & ~np.eye(m,dtype=bool)
covers=[(a,b) for a in range(m) for b in range(m) if LTJ[a,b] and not any(LTJ[a,c] and LTJ[c,b] for c in range(m))]
print('covering relations in J(Λ8):',len(covers))
# down-sets of J by subset enumeration (2^17)
cnt=0
for mask in range(1<<m):
    ok=True
    for a,b in covers:            # down-closed: if b in set then a in set
        if (mask>>b)&1 and not (mask>>a)&1: ok=False; break
    cnt+=ok
print('down-sets of J(Λ8):',cnt,'== |Λ8|:',cnt==n8)
w,ac=chain_partition_and_antichain(LEJ); print('width(J(Λ8)) =',w,'| a maximum antichain of size',len(ac),':',[tuple(Jset[i].tolist()) for i in ac])
names='n ℓ k q e f g 2S'.split(); bottom=L8.min(axis=0)
first={}
for i in ji:
    d=np.nonzero(L8[i]-bottom)[0]
    # 'the generator that first raises coordinate c': the least JI whose only raised coordinate beyond bottom-part includes c … report atoms (JI covering bottom)
for i in ji:
    x=tuple(L8[i].tolist())
    if x in [(1,0,1,1,1,0,1,0),(1,0,1,1,1,0,0,0)]: print('  JI present:',x)
qa=list(map(tuple,L8.tolist())).index((1,0,1,1,1,0,0,0)); ga=list(map(tuple,L8.tolist())).index((1,0,1,1,1,0,1,0))
print('  g-atom (1,0,1,1,1,0,1,0) above q-atom (1,0,1,1,1,0,0,0):',bool(LE[qa,ga]),'| coordinates raised by antichain members:',[names[int(np.argmax(Jset[i]-bottom))] for i in ac])
# the three printed covers
def idx(t): return list(map(tuple,Jset.tolist())).index(t) if t in list(map(tuple,Jset.tolist())) else None
for a,b in [((1,0,1,0,2,0,0,0),(1,0,1,0,2,1,0,0)),((1,0,2,0,1,0,0,0),(1,0,2,2,1,0,0,0)),((2,0,1,0,1,0,0,0),(2,1,1,0,1,0,0,0)),((2,1,1,0,1,0,0,0),(2,1,3,0,1,0,0,0))]:
    ia,ib=idx(a),idx(b); print('  printed cover',a,'⋖',b,':','both JI' if ia is not None and ib is not None else 'NOT both JI', '| is a cover in J:', (ia,ib) in covers if ia is not None and ib is not None else '-')
# Sperner / width of Λ8 (Dilworth by matching) at three settings
for name,X in [('Λ8 (3,3,1,1,3)',L8)]:
    LT=LE & ~np.eye(len(X),dtype=bool); wd=width_dilworth(LT); print('width of',name,'=',wd,'| max rank level',max(rs),'| Sperner:',wd==max(rs))
# Λ9: join-irreducibles and width of J
L9=np.array(tw.L9(),dtype=np.int16); ji9,LE9=join_irreducibles(L9); LEJ9=LE9[np.ix_(ji9,ji9)]
print('|Λ9|',len(L9),'join-irreducibles',len(ji9),'width(J(Λ9)) =',width_dilworth(LEJ9 & ~np.eye(len(ji9),dtype=bool)))
if len(sys.argv)>1 and sys.argv[1]=='settings':
    def build(nmax,emax,lmax,fmax,kmax,kmin=1):
        return [(n,l,k,q,e,f,g,S2) for n in range(1,nmax+1) for l in range(0,min(lmax,n-1)+1) for k in range(kmin,min(kmax,4*l+2)+1) for q in range(0,k+1)
                for e in range(1,emax+1) for f in range(0,min(fmax,e-1)+1) for g in range(0,min(4*f+2,q)+1) for S2 in range(0,k+1)]
    found=[]
    for s in itertools.product(range(2,7),range(2,7),range(0,3),range(0,3),range(1,9)):
        c=len(build(*s))
        if c in (976,27873): found.append((c,s))
    print('settings giving 976 or 27,873 in n,e≤6, ℓ,f≤2, k≤8:',found)
    # generator counts at a ladder of settings up to ~3,000 cells (JI needs O(n²) memory)
    for s in [(3,3,1,1,3),(3,3,1,1,4),(4,3,1,1,4),(4,4,1,1,4),(3,3,1,1,5),(4,4,1,1,3)]:
        X=np.array(build(*s),dtype=np.int16)
        if len(X)>3200: print(s,len(X),'skipped (size)'); continue
        j,_=join_irreducibles(X); print('setting',s,'cells',len(X),'join-irreducibles',len(j))
