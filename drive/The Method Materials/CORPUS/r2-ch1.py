# r2-ch1.py — Phase R2, main Chapter 1 (chat 69). Re-measures every tower-measurable figure printed in
# Chapter 1 on the rebuilt Λ8 (tower-2.py beside it). Every line printed is MEASURED; the read decides.
import importlib.util, itertools, math, numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L=tw.L8(); S=set(L); n=len(L); d=8
print('|Λ8| =',n,'; C(976,2) =',n*(n-1)//2,'(L546 "475,800 pairs")')
sums=[sum(c) for c in L]
print('rank(x)=Σx_i (L1947/L1952): min %d max %d mean %.4f  (L427 prints rank(x) 13, mean rank 11.0666)'%(min(sums),max(sums),sum(sums)/n))
rank={min(L,key=sum):0}
for c in sorted(L,key=sum):
    for i in range(d):
        t=list(c); t[i]+=1; t=tuple(t)
        if t in S: rank[t]=max(rank.get(t,0),rank[c]+1)
print('graded rank from the bottom: height %d, mean %.4f (L8517 "|J(Λ)| = 17 = height")'%(max(rank.values()),sum(rank.values())/n))
print('E_bits = log2 C(126,36) = %.2f  (L434/L7253 105.1; |ℛ| = 90 + 36 from L1583)'%math.log2(math.comb(126,36)))
def cells(sbound):
    out=[]
    for nn in range(1,4):
      for l in range(0,min(1,nn-1)+1):
        for k in range(1,min(3,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,min(1,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,sbound(k)+1):
                    out.append((nn,l,k,q,e,f,g,S2))
    return out
assert set(cells(lambda k:k))==S
def closed(X):
    Xs=set(X)
    return all(tuple(map(max,a,b)) in Xs and tuple(map(min,a,b)) in Xs for a in Xs for b in Xs)
y=(1,0,1,0,1,0,0,2); rev=set(cells(lambda k:2 if k==1 else k))
print('P22 example: y in Λ8:',y in S,'; revised rule 2S≤2 at k=1 admits',len(rev-S),'cells incl. y (L488 "74 further", L490 "75");',
      'revised index closed under join/meet:',closed(rev),'size',len(rev))
print('forged rule 2S≤k+1: +%d cells with the cap 2S≤3 kept (L504 "225"); +%d without the cap'%(len(set(cells(lambda k:min(k+1,3)))-S),len(set(cells(lambda k:k+1))-S)))
X=np.array(L); lo=X.min(0); hi=X.max(0)
def closure(Xs):
    A=np.array(sorted(Xs)); F={}; G={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            F[(i,j)]={v:(A[A[:,i]<=v][:,j].max() if (A[:,i]<=v).any() else -1) for v in range(lo[i],hi[i]+1)}
            G[(i,j)]={v:(A[A[:,i]>=v][:,j].min() if (A[:,i]>=v).any() else 10**6) for v in range(lo[i],hi[i]+1)}
    return {z for z in itertools.product(*[range(lo[i],hi[i]+1) for i in range(d)])
            if all(G[(i,j)][z[i]]<=z[j]<=F[(i,j)][z[i]] for (i,j) in F)}
print('tightest monotone two-variable-bound closure: closure(Λ8)==Λ8:',closure(S)==S)
fails=[x for x in L if x not in closure(S-{x})]
print('deletion repair over all %d cells: %d failures (L448 "30 deletions, 0 failures"; L446 "restores every deletion")'%(n,len(fails)))
