# r2-ch7.py — Phase R2, main Chapter 7 "The construction of Λ" (chat 70). Run beside tower-2.py.
import itertools, importlib.util, numpy as np, sys
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
T8=tw.L8(); print('tower-2.py |Λ8| =',len(T8))

def build(nmax,emax,lmax,fmax,kmax,kmin=1):
    """the seven printed constraints of §7.1 at explicit caps"""
    out=[]
    for n in range(1,nmax+1):
      for l in range(0,min(lmax,n-1)+1):                 # ℓ ≤ n−1
        for k in range(kmin,min(kmax,4*l+2)+1):           # k ≤ 2(2ℓ+1)
          for q in range(0,k+1):                          # q ≤ k
            for e in range(1,emax+1):
              for f in range(0,min(fmax,e-1)+1):          # f ≤ e−1
                for g in range(0,min(4*f+2,q)+1):         # g ≤ 2(2f+1), g ≤ q
                  for S2 in range(0,k+1):                 # 2S ≤ k
                    out.append((n,l,k,q,e,f,g,S2))
    return out

X=build(3,3,1,1,3); print('§7.1 constraints at printed caps (3,3,1,3), k≥1, with f≤1:',len(X),'equal to tower-2.py:',set(X)==set(T8))
Xnof=build(3,3,1,99,3); print('same without an f-cap (f ≤ e−1 only):',len(Xnof))
X0=build(3,3,1,1,3,kmin=0); print('with k ≥ 0 instead of k ≥ 1:',len(X0))

# §7.2 / Figure 7.1: constraint graph
edges=[('n','ℓ'),('ℓ','k'),('k','q'),('e','f'),('f','g'),('q','g'),('k','2S')]
nodes={a for e in edges for a in e}
adj={v:set() for v in nodes}
for a,b in edges: adj[a].add(b); adj[b].add(a)
seen={'n'}; st=['n']
while st:
    v=st.pop()
    for w in adj[v]:
        if w not in seen: seen.add(w); st.append(w)
print('constraint graph: nodes',len(nodes),'edges',len(edges),'connected',len(seen)==len(nodes),'tree (connected, |E|=|V|−1):',len(seen)==len(nodes) and len(edges)==len(nodes)-1)

def E_of(X):
    """E(X) = |ℛ(X)| − |X| with ℛ the join/meet closure to a fixed point; also the size after one pass and after a second"""
    A=np.array(sorted(set(X)),dtype=np.int16); n0=len(A)
    def one_pass(A):
        J=np.maximum(A[:,None,:],A[None,:,:]).reshape(-1,A.shape[1]); Mn=np.minimum(A[:,None,:],A[None,:,:]).reshape(-1,A.shape[1])
        return np.unique(np.concatenate([A,J,Mn]),axis=0)
    A1=one_pass(A); A2=one_pass(A1)
    return len(A1)-n0, len(A2)-len(A1)

targets={216,976,1636,2394,27873}
hits={}
for nmax,emax,lmax,fmax,kmax in itertools.product(range(2,6),range(2,6),range(0,4),range(0,4),range(1,9)):
    c=len(build(nmax,emax,lmax,fmax,kmax))
    if c in targets: hits.setdefault(c,[]).append((nmax,emax,lmax,fmax,kmax))
for c in sorted(targets):
    print(f'{c:6d} cells: settings (n,e,ℓ,f,k) =',hits.get(c,'NONE in grid n,e≤5, ℓ,f≤3, k≤8'))
for c in (216,976,1636,2394):
    for s in (hits.get(c) or [])[:1]:
        e1,e2=E_of(build(*s)); print(f'   E at {s} ({c} cells): first pass +{e1}, second pass +{e2}')

# 48.5 % density candidates at the printed caps
phys=lambda l,k,S2: (S2%2==k%2) and S2<=min(k,4*l+2-k)
c1=sum(phys(l,k,S2) for (n,l,k,q,e,f,g,S2) in X)/len(X)
pairs=[(l,k,S2) for l in range(0,2) for k in range(1,min(3,4*l+2)+1) for S2 in range(0,k+1)]
c2=sum(phys(*p) for p in pairs)/len(pairs)
box=3*2*3*4*3*2*7*4
print(f'density candidates: cells with physical 2S / |Λ8| = {c1:.3%}; physical (ℓ,k,2S) triples / envelope triples = {c2:.3%} ({sum(phys(*p) for p in pairs)} of {len(pairs)}); |Λ8|/product box (3·2·3·4·3·2·7·4) = {len(X)/box:.3%}')
# the envelope's surplus: cells whose 2S no k electrons can carry
print('cells with unphysical 2S:',sum(not phys(l,k,S2) for (n,l,k,q,e,f,g,S2) in X),'of',len(X))
print('ratio 27873/976 =',round(27873/976,2),'; 2394/216 =',round(2394/216,2))
