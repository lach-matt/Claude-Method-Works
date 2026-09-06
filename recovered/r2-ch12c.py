# r2-ch12c.py — Phase R2 instrument for main §12.8–§12.9 (chat 72). Requires tower-2.py beside it.
# Every figure printed here is measured on ALL cells, ALL comparable pairs or ALL 475,800 unordered pairs of the rebuilt Λ8,
# and on the rebuilt Λ9…Λ13 where the claim reaches the tower. Nothing is sampled.
import importlib.util, itertools, collections, math, random, sys
from fractions import Fraction
import numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8=tw.L8(); n=len(L8); S8=set(L8); print('|Λ8| =',n)
NAMES='n l k q e f g 2S'.split()
X=np.array(L8,dtype=np.int16)
# ---------------------------------------------------------------- §12.8 the fibre table (two-body separation of §12.6.1)
Aof=lambda c:(c[0],c[1],c[2],c[7]); Bof=lambda c:(c[4],c[5],c[6])
N={}; Aq={}; Bq={}
for qq in range(4):
    C=[c for c in L8 if c[3]==qq]; N[qq]=len(C); Aq[qq]=set(map(Aof,C)); Bq[qq]=set(map(Bof,C))
A=[len(Aq[q]) for q in range(4)]; B=[len(Bq[q]) for q in range(4)]
print('§12.8 fibre counts N_q =',[N[q] for q in range(4)],'Σ =',sum(N.values()),'| |A_q| =',A,'| |B_q| =',B,'| |A_q||B_q| =',[A[q]*B[q] for q in range(4)],'exact separation at every q:',all(A[q]*B[q]==N[q] for q in range(4)))
print('§12.8.1 |A_q| non-increasing:',all(A[i]>=A[i+1] for i in range(3)),'| falls at EVERY step (strict):',all(A[i]>A[i+1] for i in range(3)),'| |B_q| rises at every step (strict):',all(B[i]<B[i+1] for i in range(3)))
print('  no q improves both (no ordered pair q≠q′ with |A_q|>|A_q′| and |B_q|>|B_q′|):',not any(A[i]>A[j] and B[i]>B[j] for i in range(4) for j in range(4) if i!=j))
# §12.8.2
seq=[N[q] for q in range(4)]; p=max(range(4),key=lambda q:seq[q])
mean=Fraction(sum(q*N[q] for q in range(4)),n); m2=Fraction(sum(q*q*N[q] for q in range(4)),n); var=m2-mean*mean
print('§12.8.2 peak at q=%d with %d cells = %.2f%% of Λ | log-concave (N_q² ≥ N_{q−1}N_{q+1} at q=1,2): %s | unimodal (rises to the peak, falls after): %s'%(p,seq[p],100*seq[p]/n,all(seq[i]**2>=seq[i-1]*seq[i+1] for i in (1,2)),all(seq[i]<=seq[i+1] for i in range(p)) and all(seq[i]>=seq[i+1] for i in range(p,3))))
print('  ⟨q⟩ = Σ q·N_q / 976 = %d/976 = %.4f | sd = %.4f'%(sum(q*N[q] for q in range(4)),float(mean),math.sqrt(float(var))))
# §12.8.3 the shape polynomial S(base,left,right) = Σ_q base^q · A_q(left) · B_q(right): S(1,1,1) and S′_base(1)/S(1)
S111=sum(A[q]*B[q] for q in range(4)); Sp=sum(q*A[q]*B[q] for q in range(4))
print('§12.8.3 S(1,1,1) = Σ_q |A_q||B_q| = %d | S′(1)/S(1) in the base variable = %d/%d = %.4f (equals ⟨q⟩ because the separation is exact at every q)'%(S111,Sp,S111,Sp/S111))
# §12.8.4 the eight slices: closure (E), the modular law on conditioned triples, the distributive law on all triples
def closure(Xs):
    Xs=set(Xs)
    while True:
        new=set()
        for a in Xs:
            for b in Xs:
                j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
                if j not in Xs: new.add(j)
                if m not in Xs: new.add(m)
        if not new: return Xs
        Xs|=new
def leq(a,b): return all(u<=v for u,v in zip(a,b))
def jn(a,b): return tuple(map(max,a,b))
def mt(a,b): return tuple(map(min,a,b))
totE=0; modtrip=0; modtrip_strict=0; modfail=0; distrip=0; disfail=0; lattice_ok=True
for side,D in (('A',Aq),('B',Bq)):
    for qq in range(4):
        Xs=D[qq]; E=len(closure(Xs))-len(Xs); totE+=E
        el=list(Xs)
        for x in el:
            for b in el:
                if leq(x,b):
                    for a in el:
                        modtrip+=1; modtrip_strict+= (x!=b)
                        if jn(x,mt(a,b))!=mt(jn(x,a),b): modfail+=1
        for a in el:
            for b in el:
                for c in el:
                    distrip+=1
                    if mt(a,jn(b,c))!=jn(mt(a,b),mt(a,c)): disfail+=1
        print('  slice %s_%d: |X| = %2d  E(X) = %d  closed under coordinatewise join and meet: %s'%(side,qq,len(Xs),E,E==0))
print('§12.8.4 all eight slices closed (ΣE = %d) | modular law x∨(a∧b) = (x∨a)∧b for x ≤ b: %d conditioned triples (x ≤ b incl. x = b), %d with x < b, failures %d | distributive law a∧(b∨c) = (a∧b)∨(a∧c): %d ordered triples, failures %d'%(totE,modtrip,modtrip_strict,modfail,distrip,disfail))
# §12.8.5 "the second does not follow from the first": E(Λ)=0 ⇒ every fixed-q fibre and its two projections are closed.
#   Proof. x,y ∈ A_q lift to cells (x,q,b),(y,q,b′) ∈ Λ; Λ closed ⇒ (x∨y, q, b∨b′) ∈ Λ (max(q,q)=q) ⇒ x∨y ∈ A_q; likewise meets and B_q.
#   Mechanical corroboration on random closed sets: no closed set in a small box has a defective slice.
rng=random.Random(1); trials=0; fails=0
for t in range(3000):
    d=rng.choice([3,4]); box=list(itertools.product(range(3),repeat=d))
    Xs=closure(set(rng.sample(box,rng.randint(2,8)))); trials+=1
    for i in range(d):
        for v in range(3):
            fib=[c for c in Xs if c[i]==v]
            if not fib: continue
            proj={c[:i]+c[i+1:] for c in fib}
            if len(closure(fib))!=len(fib) or len(closure(proj))!=len(proj): fails+=1
print('§12.8.5 E(Λ8) (closure of all 976 cells) =',len(closure(S8))-n,'| random closed sets in [0,2]^d, d∈{3,4}: %d sets, fixed-coordinate fibres/projections with E>0: %d'%(trials,fails))
# ---------------------------------------------------------------- §12.9 intervals: the box criterion, on ALL comparable pairs and ALL meet-join intervals
CONS=[('ℓ≤n−1',1,lambda v:v-1,0),('k≤2(2ℓ+1)',2,lambda v:2*(2*v+1),1),('q≤k',3,lambda v:v,2),('2S≤k',7,lambda v:v,2),('g≤q',6,lambda v:v,3),('f≤e−1',5,lambda v:v-1,4),('g≤4f+2',6,lambda v:4*v+2,5)]
LE=np.all(X[:,None,:]<=X[None,:,:],axis=2); LT=LE&~np.eye(n,dtype=bool)
I=(LE.astype(np.int32)@LE.astype(np.int32))          # I[i,j] = |{z ∈ Λ : x_i ≤ z ≤ x_j}|
ii,jj=np.nonzero(LT); print('§12.9 comparable pairs x < y:',len(ii))
xs=X[ii].astype(np.int32); ys=X[jj].astype(np.int32)
boxsize=np.prod(ys-xs+1,axis=1); isbox=(I[ii,jj]==boxsize)
binds=np.stack([ys[:,i]>np.vectorize(f)(xs[:,j]) for (_,i,f,j) in CONS],axis=1)
crit=~binds.any(axis=1)
print('  I_{x,y} = Box(x,y) ⟺ no constraint binds: agree on %d of %d (disagreements %d) | boxes %d of %d = %.2f%% | not boxes %.2f%%'%((crit==isbox).sum(),len(ii),(crit!=isbox).sum(),isbox.sum(),len(ii),100*isbox.mean(),100*(1-isbox.mean())))
print('  binding rates over ALL comparable intervals: '+', '.join('%s %.1f%%'%(c[0],100*binds[:,t].mean()) for t,c in enumerate(CONS)))
iu,ju=np.triu_indices(n,1); m=np.minimum(X[iu],X[ju]).astype(np.int32); M=np.maximum(X[iu],X[ju]).astype(np.int32)
bindsMJ=np.stack([M[:,i]>np.vectorize(f)(m[:,j]) for (_,i,f,j) in CONS],axis=1)
print('  meet-join intervals [x∧y, x∨y] of all %d unordered pairs: boxes (no constraint binds) %d = %.2f%% | binding rates: '%(len(iu),(~bindsMJ.any(axis=1)).sum(),100*(~bindsMJ.any(axis=1)).mean())+', '.join('%s %.1f%%'%(c[0],100*bindsMJ[:,t].mean()) for t,c in enumerate(CONS)))
order=sorted(range(7),key=lambda t:-binds[:,t].mean()); print('  ranking on comparable intervals, most to least active:',[CONS[t][0] for t in order],'| on meet-join intervals:',[CONS[t][0] for t in sorted(range(7),key=lambda t:-bindsMJ[:,t].mean())])
# rank levels, antichains, width
rank=X.sum(axis=1); levels=collections.Counter(rank.tolist()); lv=sorted(levels)
LT2=(LT.astype(np.int32)@LT.astype(np.int32))>0; COV=LT&~LT2
ci,cj=np.nonzero(COV); print('  rank = coordinate sum, ranks %d..%d = %d levels | every cover raises rank by exactly 1 (graded): %s | covers %d'%(lv[0],lv[-1],len(lv),bool(np.all(rank[cj]-rank[ci]==1)),len(ci)))
mx=max(levels.values()); print('  level sizes:',[levels[r] for r in lv],'| largest %d at rank %d | 976 = 8 × %d: %s'%(mx,[r for r in lv if levels[r]==mx][0],mx,8*mx==n))
try:
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import maximum_bipartite_matching
    mm=maximum_bipartite_matching(csr_matrix(LT),perm_type='column'); width=n-int((mm>=0).sum())
    print('  width(Λ8) by Dilworth (n − maximum matching in the comparability bipartite graph):',width,'| equals the largest level (Sperner):',width==mx)
except Exception as e: print('  width: scipy unavailable',e)
# maximal chains: all from 0̂ to 1̂, all of the same length; their number = e(P) for P the 17 join-irreducibles (Birkhoff)
bot=[i for i in range(n) if not LT[:,i].any()]; top=[i for i in range(n) if not LT[i,:].any()]
print('  minimal elements %d %s | maximal elements %d %s'%(len(bot),[tuple(X[i].tolist()) for i in bot],len(top),[tuple(X[i].tolist()) for i in top]))
ordr=np.argsort(rank,kind='stable'); ways=np.zeros(n,dtype=object); lo=np.full(n,10**9); hi=np.full(n,-1); ways[bot[0]]=1; lo[bot[0]]=0; hi[bot[0]]=0
ups=collections.defaultdict(list)
for a,b in zip(ci,cj): ups[b].append(a)
for v in ordr:
    v=int(v)
    for u in ups[v]:
        ways[v]+=ways[u]; lo[v]=min(lo[v],lo[u]+1); hi[v]=max(hi[v],hi[u]+1)
t=top[0]; print('  maximal chains 0̂→1̂: shortest %d steps, longest %d steps (elements %d); number of maximal chains e(P) = %s = %s'%(lo[t],hi[t],hi[t]+1,ways[t],format(int(ways[t]),',')))
# join-irreducibles: elements with exactly one lower cover
lowc=collections.Counter(cj.tolist()); ji=[i for i in range(n) if lowc[i]==1]; print('  join-irreducibles (exactly one lower cover):',len(ji),'| chain length %d = |J| %d: %s'%(hi[t],len(ji),hi[t]==len(ji)))
# the constraint graph
edges={(min(i,j),max(i,j)) for (_,i,_,j) in CONS}; adj=collections.defaultdict(set)
for a,b in edges: adj[a].add(b); adj[b].add(a)
seen={0}; st=[0]
while st:
    u=st.pop()
    for w in adj[u]:
        if w not in seen: seen.add(w); st.append(w)
print('  constraint graph: %d vertices, %d edges, connected %s ⇒ tree (acyclic) %s'%(8,len(edges),len(seen)==8,len(seen)==8 and len(edges)==7))
# ---------------------------------------------------------------- the tower: ⟨q⟩ at every stage, the printed sections, the two sides at Λ13
for d in range(8,14):
    L=tw.STAGES[d](); Nq=collections.Counter(c[3] for c in L); tot=len(L)
    mq=sum(q*Nq[q] for q in range(4))/tot
    print('  Λ%d: sections by q %s Σ %d | ⟨q⟩ = %d/%d = %.4f'%(d,[Nq[q] for q in range(4)],tot,sum(q*Nq[q] for q in range(4)),tot,mq))
L13=tw.L13(); A13=lambda c:(c[0],c[1],c[2],c[7],c[10],c[11],c[12]); B13=lambda c:(c[4],c[5],c[6],c[8],c[9])
a13=[len({A13(c) for c in L13 if c[3]==q}) for q in range(4)]; b13=[len({B13(c) for c in L13 if c[3]==q}) for q in range(4)]
print('  Λ13 sides (r2-ch12b split): |A(q)| =',a13,'non-increasing',all(a13[i]>=a13[i+1] for i in range(3)),'strictly falls',all(a13[i]>a13[i+1] for i in range(3)),'| |B(q)| =',b13,'strictly rises',all(b13[i]<b13[i+1] for i in range(3)))
