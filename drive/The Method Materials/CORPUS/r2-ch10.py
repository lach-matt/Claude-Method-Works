# r2-ch10.py — Phase R2 instrument for main Chapter 10 "The void" (chat 71). Requires tower-2.py beside it.
# Every general claim is measured on ALL 475,800 unordered pairs of Λ8 cells, not on the printed samples.
import numpy as np, importlib.util, itertools, math
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
X=np.array(tw.L8(),dtype=np.int16); N=len(X); names='n l k q e f g S'.split()
print('|Λ8| =',N)
I,J=np.triu_indices(N,1); P=len(I); lo=np.minimum(X[I],X[J]).astype(np.int16); hi=np.maximum(X[I],X[J]).astype(np.int16)
box=np.prod((hi-lo+1).astype(np.int64),axis=1)
print('unordered pairs',P,'| Σ box points',int(box.sum()))
# --- brute-force |[x∧y, x∨y] ∩ Λ| for every pair (L2024's second term)
cnt=np.zeros(P,dtype=np.int32); ch=3000
for s in range(0,P,ch):
    L=lo[s:s+ch][:,None,:]; H=hi[s:s+ch][:,None,:]
    cnt[s:s+ch]=np.all((X[None,:,:]>=L)&(X[None,:,:]<=H),axis=2).sum(axis=1)
void=box-cnt
print('void(x,y) = ∏(|Δ|+1) − |box ∩ Λ|: void-free pairs',int((void==0).sum()),'= %.2f%%'%(100*(void==0).mean()),'| void-bearing',int((void>0).sum()),'| Σ void points',int(void.sum()))
# --- §10.3 seven comparisons hi_i ≤ φ(lo_j), constraint by constraint (bounded coordinate at the top, bounding at the bottom)
n,l,k,q,e,f,g,S=range(8)
C={'l≤n−1 (hydrogenic)': hi[:,l]<=lo[:,n]-1, 'k≤2(2l+1) (Pauli)': hi[:,k]<=4*lo[:,l]+2, 'q≤k (counting)': hi[:,q]<=lo[:,k],
   '2S≤k': hi[:,S]<=lo[:,k], 'g≤q (counting)': hi[:,g]<=lo[:,q], 'f≤e−1 (hydrogenic)': hi[:,f]<=lo[:,e]-1, 'g≤2(2f+1) (Pauli)': hi[:,g]<=4*lo[:,f]+2}
joint=np.ones(P,dtype=bool)
for c in C.values(): joint&=c
print('§10.3 iff: (all seven comparisons hold) == (void == 0) on all pairs:',bool(np.array_equal(joint,void==0)),'| disagreements',int((joint!=(void==0)).sum()))
rates={kname:float(v.mean()) for kname,v in C.items()}
for kname,v in rates.items(): print('   individual %-22s %.2f%%'%(kname,100*v))
prod=math.prod(rates.values()); jr=float(joint.mean())
print('   individual range %.2f–%.2f%% | product %.2f%% | joint %.2f%% | joint/product = %.4f'%(100*min(rates.values()),100*max(rates.values()),100*prod,100*jr,jr/prod))
# --- §10.4 closed form on all pairs: Σ over (n,l,k,q,e,f) in the box of [l≤n−1][1≤k≤2(2l+1)][q≤k][f≤e−1] · #{2S≤k} · #{g≤min(q,2(2f+1))}
def closed(with_S=True,with_listed=True):
    tot=np.zeros(P,dtype=np.int64)
    for nn,ll,kk,qq,ee,ff in itertools.product(range(1,4),range(0,2),range(1,4),range(0,4),range(1,4),range(0,2)):
        inb=(lo[:,n]<=nn)&(nn<=hi[:,n])&(lo[:,l]<=ll)&(ll<=hi[:,l])&(lo[:,k]<=kk)&(kk<=hi[:,k])&(lo[:,q]<=qq)&(qq<=hi[:,q])&(lo[:,e]<=ee)&(ee<=hi[:,e])&(lo[:,f]<=ff)&(ff<=hi[:,f])
        if not inb.any(): continue
        ok=(ll<=nn-1)&(1<=kk<=4*ll+2)&(qq<=kk)&(ff<=ee-1) if with_listed else True
        if not ok: continue
        nS=np.maximum(0,np.minimum(hi[:,S],kk)-lo[:,S]+1) if with_S else (hi[:,S]-lo[:,S]+1)
        ng=np.maximum(0,np.minimum(np.minimum(hi[:,g],qq),4*ff+2)-lo[:,g]+1) if with_listed else (hi[:,g]-lo[:,g]+1)
        tot+=inb*(nS.astype(np.int64)*ng.astype(np.int64))
    return tot
c7=closed(); print('§10.4 closed form == brute-force |box ∩ Λ| on all pairs:',bool(np.array_equal(c7,cnt)),'| mismatches',int((c7!=cnt).sum()))
c6=closed(with_S=False)  # the six constraints §10.1 lists, without 2S ≤ k
extra=c6-cnt; print('§10.1 list test: box points passing the six listed constraints but failing 2S ≤ k:',int(extra.sum()),'points on',int((extra>0).sum()),'pairs (of',int((void>0).sum()),'void-bearing pairs) | share of all void points %.2f%%'%(100*extra.sum()/void.sum()))
# --- §10.2 the eighth condition k ≥ 1, and Register 301's (3,3,2,3)
def L8p(ncap=3,lcap=1,kcap=3,ecap=3,fcap=1,kmin=1):
    out=[]
    for a in range(1,ncap+1):
      for b in range(0,min(lcap,a-1)+1):
        for c in range(kmin,min(kcap,4*b+2)+1):
          for d in range(0,c+1):
            for ee in range(1,ecap+1):
              for ff in range(0,min(fcap,ee-1)+1):
                for gg in range(0,min(4*ff+2,d)+1):
                  for ss in range(0,c+1):
                    out.append((a,b,c,d,ee,ff,gg,ss))
    return np.array(out,dtype=np.int16)
Y=L8p(kmin=0); Z=Y[Y[:,k]==0]
print('§10.2 with k ≥ 0: %d cells; k = 0 cells: %d; all with 2S = q = g = 0: %s'%(len(Y),len(Z),bool((Z[:,[q,g,S]]==0).all())))
print('   bounding box with k ≥ 1: %d | with k ≥ 0: %d'%(int(np.prod(X.max(0)-X.min(0)+1)),int(np.prod(Y.max(0)-Y.min(0)+1))))
print('   Register 301: caps (n,e,l,k) = (3,3,2,3) with k ≥ 1 gives',len(L8p(lcap=2)),'| (3,3,1,3) with k ≥ 1 gives',len(L8p()))
# --- Chapter 10's 776-million-pair population: arithmetic bound only (the record does not name the cap family)
nmax=int((1+math.sqrt(1+8*776e6))/2); print('776 million unordered pairs ⇒ largest lattice ≤ %d cells (C(N,2) ≤ 776M) ⇒ hundredfold range ⇒ smallest ≤ %d; seventeenfold ⇒ smallest ≤ %d'%(nmax,nmax//100,nmax//17))
