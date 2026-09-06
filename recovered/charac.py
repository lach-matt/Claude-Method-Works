import pickle, numpy as np
from itertools import combinations, product
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
DIMS=D['dims']; cells=D['cells']; tab=D['tab']; NF=D['nforms']; n=len(cells)
print("="*88)
print("  CHARACTERISING FROM THE EXHAUSTIVE 2×3×3 DATA")
print("="*88)
# rebuild canonical form representatives
def alph(S,d=3): return [sorted({x[i] for x in S}) for i in range(d)]
from itertools import permutations
def relab(S,o,d=3):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def canon(T,d=3):
    A=alph(T); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        c=tuple(sorted(relab(T,[list(p) for p in ps])))
        if best is None or c<best: best=c
    return best
rep={}
for T,f in tab.items():
    if f not in rep: rep[f]=canon({cells[i] for i in T})
def is_sublat(S,d=3):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord_small(S,d=3):
    A=alph(S)
    for ps in product(*[list(permutations(a)) for a in A]):
        if is_sublat(relab(S,[list(p) for p in ps])): return True
    return False
print("\n  THE 19 CANONICAL 3-SUBSET FORMS\n")
print("  %4s%34s%10s%12s"%("id","representative","reord?","axes used"))
print("  "+"-"*62)
for f in sorted(rep):
    S=set(rep[f]); A=alph(S)
    print("  %4d%34s%10s%12s"%(f,str(sorted(S))[:32],reord_small(S),[len(x) for x in A]))
print("="*88)
print("  WHICH FORMS APPEAR IN REORDERABLE SETS?")
print("="*88)
pres_in_yes=[0]*NF; pres_in_no=[0]*NF; nyes=nno=0
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    seen=set()
    for T in combinations(idx,3): seen.add(tab[T])
    if v==2:
        nyes+=1
        for f in seen: pres_in_yes[f]+=1
    else:
        nno+=1
        for f in seen: pres_in_no[f]+=1
print("\n     reorderable %d      not %d"%(nyes,nno))
print("\n  %4s%16s%16s%16s"%("id","in YES sets","in NO sets","FATAL?"))
print("  "+"-"*56)
fatal=[]
for f in range(NF):
    fat = (pres_in_yes[f]==0)
    if fat: fatal.append(f)
    print("  %4d%16d%16d%16s"%(f,pres_in_yes[f],pres_in_no[f],"**YES**" if fat else ""))
print("\n     **fatal forms (never in a reorderable set) : %s**"%fatal)
print("="*88)
print("  SO IS 'CONTAINS NO FATAL FORM' THE CHARACTERISATION?")
print("="*88)
tp=fp=fn=tn=0
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    has=False
    for T in combinations(idx,3):
        if tab[T] in fatal: has=True; break
    pred = not has
    act = (v==2)
    if pred and act: tp+=1
    elif pred and not act: fp+=1
    elif not pred and act: fn+=1
    else: tn+=1
print("\n     predicted reorderable AND is      : %d"%tp)
print("     predicted reorderable, is NOT     : %d   <- false positives"%fp)
print("     predicted NOT, but IS             : %d   <- **must be 0**"%fn)
print("     predicted NOT, and is not         : %d"%tn)
print("     accuracy                          : %.4f"%((tp+tn)/(tp+fp+fn+tn)))
pickle.dump({'rep':rep,'fatal':fatal,'pres_yes':pres_in_yes,'pres_no':pres_in_no},
            open('/home/claude/stage/s4.pkl','wb'))
print("\n     saved  /home/claude/stage/s4.pkl")