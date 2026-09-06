import pickle, time
from itertools import combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
DIMS=D['dims']; cells=D['cells']; tab=D['tab']; NF=D['nforms']; n=len(cells)
print("="*82)
print("  STAGE 3 — THE SIGNATURE, AND THE CONSISTENCY CHECK")
print("="*82)
print("\n     canonical forms (the label alphabet) : %d"%NF)
print("     subsets to check                     : %d"%sum(1 for m in range(1<<n) if res[m]))
# index the 3-subset table by the three cell indices
T3=[(T,tab[T]) for T in tab]
by=[[] for _ in range(n)]
for T,f in T3:
    for i in T: by[i].append((T,f))
t0=time.time()
classes={}
mixed=[]
done=0
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    cnt=[0]*NF
    for T in combinations(idx,3):
        cnt[tab[T]]+=1
    sig=tuple(cnt)
    if sig in classes:
        if classes[sig]!=v and len(mixed)<5: mixed.append((sig,mask))
        if classes[sig]!=v: classes[sig]=-1
    else:
        classes[sig]=v
    done+=1
    if done%40000==0: print("        %d  %.0fs"%(done,time.time()-t0))
nmixed=sum(1 for v in classes.values() if v==-1)
print("\n     signature classes      : %d"%len(classes))
print("     **MIXED classes        : %d**"%nmixed)
print("     time                   : %.1fs"%(time.time()-t0))
if mixed:
    print("\n     a mixed class, two members:")
    sig,mask=mixed[0]
    print("        signature :",sig)
    got=[]
    for m in range(1,1<<n):
        if not res[m]: continue
        idx=[i for i in range(n) if m>>i & 1]
        cnt=[0]*NF
        for T in combinations(idx,3): cnt[tab[T]]+=1
        if tuple(cnt)==sig:
            got.append((m,res[m]))
            if len(got)>=2 and len({g[1] for g in got})>1: break
    for m,v in got[:4]:
        print("        %s   reorderable=%s"%(sorted(cells[i] for i in range(n) if m>>i & 1),v==2))
pickle.dump(classes,open('/home/claude/stage/s3.pkl','wb'))
print("\n     saved  /home/claude/stage/s3.pkl")