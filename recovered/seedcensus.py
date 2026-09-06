# Envelope-step census on the rebuilt Λ8 (tower-2.py L8), by the envelope-step law as printed:
# a STEP (i,j,t): t minimal in coordinate j's alphabet at which the envelope φ̂_ij(t)=max{c_i : c_j<=t} changes;
# every generating set must contain a cell with c_j<=t and c_i=φ̂_ij(t).  Plus alphabet slots (j,v).
import sys, json, collections
sys.path.insert(0,'.')
from importlib import import_module
T=import_module('tower-2') if False else None
exec(open('tower-2.py').read().split("if __name__")[0])
cells=L8(); assert len(cells)==976
N=8
alph={j:sorted(set(c[j] for c in cells)) for j in range(N)}
slots=[(j,v) for j in range(N) for v in alph[j]]
steps=[]   # (i,j,t,value)
for i in range(N):
    for j in range(N):
        if i==j: continue
        prev=None
        for t in alph[j]:
            phi=max(c[i] for c in cells if c[j]<=t)
            if phi!=prev:
                steps.append((i,j,t,phi)); prev=phi
print('alphabet sizes',[len(alph[j]) for j in range(N)],'slots',len(slots))
print('steps',len(steps),'universe',len(slots)+len(steps))
bycoord=collections.Counter(s[1] for s in steps)
print('steps by stepped coordinate j (n l k q e f g 2S):',[bycoord[j] for j in range(N)])
# witness sets
def covers(c):
    out=set()
    for (j,v) in slots:
        if c[j]==v: out.add(('A',j,v))
    for (i,j,t,phi) in steps:
        if c[j]<=t and c[i]==phi: out.add(('S',i,j,t))
    return out
W={c:frozenset(covers(c)) for c in cells}
U=set().union(*W.values()); print('elements witnessed by some cell',len(U))
# elements covered by exactly one cell (Chvátal forcing)
cnt=collections.Counter(e for w in W.values() for e in w)
print('elements with a unique carrier:',[e for e,n in cnt.items() if n==1])
json.dump({'slots':slots,'steps':steps,'W':{str(c):sorted(map(list,w)) for c,w in W.items()}},open('census.json','w'))