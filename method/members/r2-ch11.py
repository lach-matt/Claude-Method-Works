# r2-ch11.py — Phase R2 instrument for main Chapter 11 "The single expression" (chat 71). Requires tower-2.py beside it.
import numpy as np, importlib.util, itertools, math
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
X=np.array(tw.L8(),dtype=np.int16); N=len(X); S=set(map(tuple,X.tolist())); n,l,k,q,e,f,g,s=range(8)
print('|Λ8| =',N)
# ---- §11.1 logic / algebra: the seven Heaviside steps (L2162) = the seven rows of A (L2164); domain matters
chi=lambda x: (x[l]<=x[n]-1) and (x[k]<=4*x[l]+2) and (x[q]<=x[k]) and (x[s]<=x[k]) and (x[f]<=x[e]-1) and (x[g]<=4*x[f]+2) and (x[g]<=x[q])
lo_,hi_=X.min(0),X.max(0); box=list(itertools.product(*[range(int(a),int(b)+1) for a,b in zip(lo_,hi_)]))
inbox=sum(1 for x in box if chi(x)); print('χ = 1 on the bounding box [min,max] (%d points): %d cells; equal to Λ8: %s'%(len(box),inbox, set(x for x in box if chi(x))==S))
capbox=list(itertools.product(range(1,4),range(0,2),range(0,4),range(0,4),range(1,4),range(0,2),range(0,4),range(0,4)))
print('χ = 1 on the §7.4 caps with k ≥ 0 (%d points): %d  (k ≥ 1 is the eighth condition, §10.2); on ℤ⁸ the seven steps alone are unbounded in n and e'%(len(capbox),sum(1 for x in capbox if chi(x))))
# ---- §11.3 the printed nesting F(1,…,1): with the §7.4 caps and k ≥ 1; then with the printed bounds only (n,e ≤ 3, no caps on ℓ,k,f)
def F1(lcap=1,kcap=3,fcap=1,kmin=1):
    c=0
    for nn in range(1,4):
      for ll in range(0,min(lcap,nn-1)+1):
        for kk in range(kmin,min(kcap,4*ll+2)+1):
          for qq in range(0,kk+1):
            for ee in range(1,4):
              for ff in range(0,min(fcap,ee-1)+1):
                for gg in range(0,min(qq,4*ff+2)+1):
                  c+=kk+1
    return c
print('F(1,…,1): printed nesting + §7.4 caps (ℓ≤1,k≤3,f≤1) + k≥1: %d | printed bounds only (ℓ≤n−1, k≤4ℓ+2, f≤e−1; n,e≤3): %d | k from 0 with caps: %d'%(F1(),F1(lcap=9,kcap=99,fcap=9),F1(kmin=0)))
# ---- binary (L2099–2132, Register 258, 331): join-irreducibles, words, OR/AND, the 20 implications, depth
Xl=X.tolist(); ge=lambda a,b: all(u>=v for u,v in zip(a,b))
bottom=tuple(int(v) for v in lo_)
def is_ji(c):
    below=[d for d in Xl if d!=list(c) and ge(c,d)]
    return c!=bottom and len([d for d in below if not any(d!=dd and ge(dd,d) for dd in below)])==1
JI=[tuple(c) for c in Xl if is_ji(tuple(c))]; print('join-irreducibles',len(JI))
word=lambda c: tuple(1 if ge(c,j) else 0 for j in JI)
W={tuple(c):word(c) for c in Xl}; print('cell ↦ word is a bijection onto %d words of {0,1}^17: %s'%(len(set(W.values())),len(set(W.values()))==N))
inv={w:c for c,w in W.items()}
I,J=np.triu_indices(N,1); fails=0
for a,b in zip(I,J):
    ca,cb=tuple(Xl[a]),tuple(Xl[b]); wa,wb=W[ca],W[cb]
    jn=tuple(max(x) for x in zip(ca,cb)); mt=tuple(min(x) for x in zip(ca,cb))
    if W[jn]!=tuple(u|v for u,v in zip(wa,wb)) or W[mt]!=tuple(u&v for u,v in zip(wa,wb)): fails+=1
print('join = bitwise OR and meet = bitwise AND on all %d pairs: failures %d'%(len(I),fails))
covers=[(i,j) for i,a in enumerate(JI) for j,b in enumerate(JI) if a!=b and ge(b,a) and not any(c!=a and c!=b and ge(b,c) and ge(c,a) for c in JI)]
print('covering relations of J(Λ8):',len(covers))
ok=sum(1 for w in itertools.product((0,1),repeat=len(JI)) if all(not w[j] or w[i] for i,j in covers))
print('words of {0,1}^%d satisfying the %d implications (bit j ⇒ bit i): %d of %d; all are cells: %s'%(len(JI),len(covers),ok,2**len(JI),ok==N))
# longest chain in J(Λ8) (elements) — the only reading of "depth five" available from the record
up={i:[j for a,j in covers if a==i] for i in range(len(JI))}
def h(i,memo={}):
    if i in memo: return memo[i]
    memo[i]=1+max([h(j) for j in up[i]],default=0); return memo[i]
print('longest chain in J(Λ8): %d elements (%d covers)'%(max(h(i) for i in range(len(JI))),max(h(i) for i in range(len(JI)))-1))
print('bits 17 | log2(976) = %.4f | surplus %.2f | 976/131072 = %.4f%%'%(math.log2(N),17-math.log2(N),100*N/2**17))
# ---- rank polynomial (L2168–2170, L2182, L2278–2302)
r=X.sum(1); rs=[int((r==v).sum()) for v in range(int(r.min()),int(r.max())+1)]
print('F(z) = z^%d·(%s)'%(int(r.min()),' + '.join('%dz^%d'%(c,i) for i,c in reversed(list(enumerate(rs))) if c)))
print('F(1) = %d | F\'(1)/F(1) = mean rank = %.4f | F(−1) = %d | peak %d at rank %d, then %d at rank %d | forwards %s | backwards %s'%(sum(rs),float(r.mean()),int(((-1)**r).sum()),max(rs),int(r.min())+rs.index(max(rs)),rs[rs.index(max(rs))-1],int(r.min())+rs.index(max(rs))-1,rs[:6],rs[::-1][:6]))
print('palindromic: %s | first rank where forwards ≠ backwards: index %d (%d against %d)'%(rs==rs[::-1],next(i for i in range(len(rs)) if rs[i]!=rs[::-1][i]),rs[1],rs[-2]))
M=int(hi_.sum()); refl=[tuple(int(v) for v in (hi_-np.array(c))) for c in Xl]; surv=[c for c,d in zip(Xl,refl) if d in S]
print('M = Σmax = %d (even: %s); x ↦ max−x (§8.3): rank(σx) = M − rank(x) for all: %s | survivors %d, their ranks %s, all even: %s, contribution Σ(−1)^rank = %+d | fixed points %d'%(M,M%2==0,all(sum(d)==M-sum(c) for c,d in zip(Xl,refl)),len(surv),sorted(sum(c) for c in surv),all(sum(c)%2==0 for c in surv),sum((-1)**sum(c) for c in surv),sum(1 for c,d in zip(Xl,refl) if tuple(c)==d)))
# the biconditional "palindromic iff self-dual" (L2187, L2271, L2276) and "self-dual graded ⇒ F(−1) = 0" (L2302): counterexamples measured
def self_dual(P,rel):  # brute force: is there a bijection reversing the order?
    for perm in itertools.permutations(P):
        m=dict(zip(P,perm))
        if all(((m[b],m[a]) in rel)==((a,b) in rel) for a in P for b in P): return True
    return False
P=list(range(8)); rel=set([(0,1),(0,2),(0,3),(1,4),(1,5),(1,6),(2,4),(3,5),(4,7),(5,7),(6,7)])
def tc(rel):
    rel=set(rel)|{(a,a) for a in P}
    while True:
        new=set((a,c) for a,b in rel for b2,c in rel if b==b2); 
        if new<=rel: return rel
        rel|=new
R8=tc(rel); ranks=[0,1,1,1,2,2,2,3]; rank_seq=[ranks.count(v) for v in range(4)]
print('counterexample P8 (0̂, three atoms, three coatoms, 1̂; covers 0<1,2,3; 1<4,5,6; 2<4; 3<5; 4,5,6<7): rank sequence %s palindromic %s | self-dual %s | F(−1) = %d'%(rank_seq,rank_seq==rank_seq[::-1],self_dual(P,R8),sum((-1)**v for v in ranks)))
C3=[0,1,2]; RC=tc.__wrapped__ if hasattr(tc,'__wrapped__') else None
P=C3; R3=tc([(0,1),(1,2)]); print('3-element chain: graded, self-dual %s, F(z) = 1 + z + z², F(−1) = %d'%(self_dual(C3,R3),1-1+1))
# ---- §11.5 remove the coupling g ≤ 2(2f+1); §11.5 what the cells show; §11.6 remove 2S
def build(couple=True):
    out=[]
    for nn in range(1,4):
      for ll in range(0,min(1,nn-1)+1):
        for kk in range(1,min(3,4*ll+2)+1):
          for qq in range(0,kk+1):
            for ee in range(1,4):
              for ff in range(0,min(1,ee-1)+1):
                for gg in range(0,(min(4*ff+2,qq) if couple else qq)+1):
                  for ss in range(0,kk+1): out.append((nn,ll,kk,qq,ee,ff,gg,ss))
    return out
U=build(False); extra=[c for c in U if tuple(c) not in S]
print('without g ≤ 2(2f+1): %d cells; the extra %d all have f = 0 and g = 3: %s'%(len(U),len(extra),all(c[f]==0 and c[g]==3 for c in extra)))
print('max g by f on Λ8 (what the cell list shows): %s (the printed bound gives %s)'%({int(v):int(X[X[:,f]==v][:,g].max()) for v in (0,1)},{v:4*v+2 for v in (0,1)}))
P7=sorted(set(tuple(c[:7]) for c in Xl)); P7s=set(P7)
def E(cells):
    cells=set(cells); 
    while True:
        new=set(tuple(max(a) for a in zip(x,y)) for x in cells for y in cells)|set(tuple(min(a) for a in zip(x,y)) for x in cells for y in cells)
        if new<=cells: return len(cells)
        cells|=new
print('2S removed: %d seven-coordinate cells; E = %d added under join/meet closure; each carries k+1 spin values and Σ(k+1) = %d'%(len(P7),E(P7)-len(P7),sum(c[k]+1 for c in P7)))
# ---- constraint graph (L2164, L2222–2229): rows of A, two non-zeros each; the tree is a path with 2S pendant at k
rows=[(l,n),(k,l),(q,k),(s,k),(f,e),(g,f),(g,q)]; names='n l k q e f g 2S'.split(); deg={i:sum(1 for r_ in rows if i in r_) for i in range(8)}
print('constraint graph: 8 nodes 7 edges, degrees %s; leaves %s; path n-ℓ-k-q-g-f-e with 2S pendant at k: %s'%({names[i]:d for i,d in deg.items()},[names[i] for i,d in deg.items() if d==1],set(map(frozenset,rows))=={frozenset(p) for p in [(n,l),(l,k),(k,q),(q,g),(g,f),(f,e),(k,s)]}))
print('F_box(−1) factors: n 1..3 → %d, ℓ 0..1 → %d, k 1..3 → %d, q 0..3 → %d, e 1..3 → %d, f 0..1 → %d, g 0..3 → %d, 2S 0..3 → %d'%tuple(sum((-1)**v for v in rg) for rg in [range(1,4),range(0,2),range(1,4),range(0,4),range(1,4),range(0,2),range(0,4),range(0,4)]))
