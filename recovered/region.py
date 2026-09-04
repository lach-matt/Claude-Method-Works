import pickle, numpy as np
from itertools import combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cells=D['cells']; tab=D['tab']; NF=D['nforms']; n=len(cells)
print("="*88)
print("  THE SHAPE OF THE REORDERABLE REGION IN COUNT SPACE")
print("="*88)
V={}
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    cnt=[0]*NF
    for T in combinations(idx,3): cnt[tab[T]]+=1
    V.setdefault(tuple(cnt),v)
Y=np.array([k for k,v in V.items() if v==2],dtype=float)
N=np.array([k for k,v in V.items() if v==1],dtype=float)
print("\n     distinct count-vectors : %d      reorderable %d      not %d"%(len(V),len(Y),len(N)))
print("="*88)
print("  1.  IS THE REGION A DOWNSET?  (coordinatewise ≤)")
print("="*88)
print("""
  If X reorderable and X' ≤ X coordinatewise implies X' reorderable, the
  region is a downset and is determined by its maximal elements.
""")
Ys={tuple(map(int,y)) for y in Y}
viol=0; tested=0
for y in list(Ys)[:400]:
    for k in range(NF):
        if y[k]==0: continue
        z=list(y); z[k]-=1; z=tuple(z)
        if z in V:
            tested+=1
            if V[z]!=2: viol+=1
print("     one-step decrements tested : %d      violations : %d"%(tested,viol))
print("     **downset : %s**"%(viol==0))
print("="*88)
print("  2.  IS A LINEAR SEPARATOR ENOUGH?")
print("="*88)
X=np.vstack([Y,N]); lab=np.array([1]*len(Y)+[0]*len(N))
X1=np.hstack([X,np.ones((len(X),1))])
w,*_=np.linalg.lstsq(X1,lab*2.0-1,rcond=None)
pred=(X1@w>0).astype(int)
acc=(pred==lab).mean()
print("\n     least-squares separator accuracy : %.4f"%acc)
print("     false negatives (said NO, is YES) : %d"%int(((pred==0)&(lab==1)).sum()))
print("     false positives                   : %d"%int(((pred==1)&(lab==0)).sum()))
print("="*88)
print("  3.  WHICH COORDINATES CARRY THE SIGNAL?")
print("="*88)
print("\n  %5s%14s%14s%14s"%("form","mean in YES","mean in NO","separation"))
print("  "+"-"*50)
sep=[]
for k in range(NF):
    my=Y[:,k].mean(); mn=N[:,k].mean()
    s=abs(my-mn)/max(np.sqrt(Y[:,k].var()+N[:,k].var()),1e-9)
    sep.append((s,k,my,mn))
for s,k,my,mn in sorted(sep,reverse=True)[:8]:
    print("  %5d%14.2f%14.2f%14.3f"%(k,my,mn,s))
print("="*88)
print("  4.  AND THE SIMPLEST EXACT RULE — TOTAL COUNT")
print("="*88)
print("""
  ΣV = C(|X|,3), so the total is just the set size. **Group by size and see
  whether the region separates within each size.**
""")
bysize={}
for k,v in V.items():
    tot=sum(k)
    # recover |X| from C(m,3)=tot
    m=3
    while m*(m-1)*(m-2)//6 < tot: m+=1
    bysize.setdefault(m,[0,0])
    bysize[m][0 if v==2 else 1]+=1
print("\n  %8s%14s%14s%12s"%("|X|","YES vectors","NO vectors","overlap?"))
print("  "+"-"*50)
for m in sorted(bysize):
    y,nn=bysize[m]
    print("  %8d%14d%14d%12s"%(m,y,nn,"both" if y and nn else ("YES only" if y else "NO only")))