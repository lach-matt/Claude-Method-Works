# r2-ch12g.py — Phase R2, main §12.11.0.2 "The clock is an assumption" (chat 73). Beside tower-2.py.
# The (g, G) index of §17.4's repair: every Λ8 cell (tower-2.py) extended by G ∈ [g, 2(2f+1)] and 2S′ ∈ [0, G].
# Closure tested pairwise on every pair (numpy); composition and occupancy-raising counted on all composable pairs.
import importlib.util, os, itertools, collections
import numpy as np
_sp=importlib.util.spec_from_file_location('tower2', os.path.join(os.path.dirname(os.path.abspath(__file__)),'tower-2.py'))
_t2=importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_t2)
L8=_t2.L8()
# coordinates: n0 l1 k2 q3 e4 f5 g6 2S7 G8 2S'9
X=[c+(G,S2p) for c in L8 for G in range(c[6], 4*c[5]+2+1) for S2p in range(0, G+1)]
alt=[c+(G,S2p) for c in L8 for G in range(c[6], 4*c[5]+2+1) for S2p in range(0, c[6]+1)]   # variant: 2S′ ≤ g
print(f'(g, G) index: {len(X):,} cells (2S′ ≤ G) | variant 2S′ ≤ g: {len(alt):,} | Λ9 for comparison 1,654 = the G = g slice: {sum(1 for c in X if c[8]==c[6]):,}')
A=np.array(X, dtype=np.int64)
radix=A.max(axis=0)+1
def encode(M): 
    code=np.zeros(len(M),dtype=np.int64); mult=1
    for j in range(M.shape[1]-1,-1,-1):
        code+=M[:,j]*mult; mult*=int(radix[j])
    return code
def closed(sub, label):
    """count pairs (x,y) in sub whose join / meet leaves sub; every pair tested."""
    S=A[sub]; codes=encode(S); cs=set(codes.tolist())
    n=len(S); bad_join=0; bad_meet=0; jset=set(); mset=set()
    lookup=np.zeros(int(np.prod(radix))+1, dtype=bool)  # dense membership over the box
    lookup[codes]=True
    for i in range(n):
        J=np.maximum(S[i], S[i:]); Mt=np.minimum(S[i], S[i:])
        cj=encode(J); cm=encode(Mt)
        bj=~lookup[cj]; bm=~lookup[cm]
        bad_join+=int(bj.sum()); bad_meet+=int(bm.sum())
        if bad_join and not jset: jset.update(map(int,cj[bj][:2]))
        if bad_meet and not mset: mset.update(map(int,cm[bm][:2]))
    tot=n*(n+1)//2
    print(f'   {label:<22} cells {n:>6,} | pairs tested {tot:>11,} | join leaves the set {bad_join:>9,} | meet leaves the set {bad_meet:>9,} | closed {bad_join==0 and bad_meet==0}')
    return bad_join, bad_meet
full=np.arange(len(A))
closed(full, 'extended index')
# --- composition ---
n_,l_,k_,q_,e_,f_,g_,S_,G_,Sp_=range(10)
src=collections.defaultdict(list)
for i,c in enumerate(X): src[(c[n_],c[l_],c[k_],c[S_])].append(i)
def pairs(tkey):
    cnt=0; raise_a=0; raise_b=0; raise_ab=0; raise_g=0; raise_Gg=0
    for i,c in enumerate(X):
        lst=src.get(tkey(c),())
        m=len(lst)
        if not m: continue
        cnt+=m
        if c[G_]>c[k_]: raise_a+=m                      # a's own step: present-after > present-before
        if c[g_]>c[k_]: raise_g+=m                      # a's placed > a's source occupancy (never, g ≤ q ≤ k)
        for j in lst:
            b=X[j]
            if b[G_]>b[k_]: raise_b+=1                  # b's step raises
            if b[G_]>c[k_]: raise_ab+=1                 # composite: end occupancy > start occupancy
            if b[G_]>b[g_]: raise_Gg+=1
    return cnt, raise_a, raise_b, raise_ab, raise_g, raise_Gg
cnt,ra,rb,rab,rg,rGg=pairs(lambda c:(c[e_],c[f_],c[G_],c[Sp_]))
print(f'composable pairs, matching (e,f,G,2S′)_a = (n,ℓ,k,2S)_b: {cnt:,} | pairs where the first step raises occupancy (G_a > k_a) {ra:,} = {100*ra/cnt:.1f}% | second step raises (G_b > k_b) {rb:,} = {100*rb/cnt:.1f}% | composite raises (G_b > k_a) {rab:,} = {100*rab/cnt:.1f}% | placed exceeds source (g_a > k_a) {rg:,} | b arrives on a non-empty subshell (G_b > g_b) {rGg:,} = {100*rGg/cnt:.1f}%')
cnt2,ra2,rb2,rab2,_,_=pairs(lambda c:(c[e_],c[f_],c[g_],c[Sp_]))
print(f'variant matching on placed, (e,f,g,2S′)_a = (n,ℓ,k,2S)_b: {cnt2:,} pairs | G_a > k_a {ra2:,} | G_b > k_b {rb2:,} | G_b > k_a {rab2:,}')
# cells whose own step raises occupancy, and the one-way clock on the G = g slice
own=sum(1 for c in X if c[G_]>c[k_]); print(f'cells with G > k (a transition that raises the target subshell above the source occupancy): {own:,} of {len(X):,} = {100*own/len(X):.1f}%')
slice_idx=[i for i,c in enumerate(X) if c[G_]==c[g_]]
s_src=collections.defaultdict(list)
for i in slice_idx: c=X[i]; s_src[(c[n_],c[l_],c[k_],c[S_])].append(i)
sc=0; sr=0
for i in slice_idx:
    c=X[i]; lst=s_src.get((c[e_],c[f_],c[G_],c[Sp_]),())
    sc+=len(lst); sr+=sum(1 for j in lst if X[j][G_]>X[j][k_] or c[G_]>c[k_])
print(f'destinations-begin-empty slice (G = g): composable pairs {sc:,}, raising {sr} (Λ9: 41,682 and 0)')
# --- weight restrictions ---
w={'shell (e ≤ n)':lambda c:c[e_]<=c[n_], 'subshell (f ≤ ℓ)':lambda c:c[f_]<=c[l_], 'occupancy (G ≤ k)':lambda c:c[G_]<=c[k_],
   'occupancy (g ≤ k)':lambda c:c[g_]<=c[k_], 'spin (2S′ ≤ 2S)':lambda c:c[Sp_]<=c[S_],
   'shell+occ (e+G ≤ n+k)':lambda c:c[e_]+c[G_]<=c[n_]+c[k_], 'max(e,G) ≤ max(n,k)':lambda c:max(c[e_],c[G_])<=max(c[n_],c[k_]),
   'min(e,G) ≤ min(n,k)':lambda c:min(c[e_],c[G_])<=min(c[n_],c[k_])}
print('weight restrictions X_w = {a : w(tgt a) ≤ w(src a)} on the (g, G) index:')
for lab,fn in w.items():
    sub=np.array([i for i,c in enumerate(X) if fn(c)]); closed(sub, lab)
