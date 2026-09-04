import itertools, collections
from tower2mod import L9
from l33b import E
# entry 34: path vs triangle regions at box caps
for cap in (4,6):
    path=[(P,Q,F) for P in range(cap+1) for Q in range(cap+1) for F in range(cap+1) if F<=Q<=P]
    tri=[(P,Q,F) for P in range(cap+1) for Q in range(cap+1) for F in range(cap+1) if abs(P-Q)<=F<=P+Q]
    print(f'cap {cap}: path region {len(path)} E={E(path)};  triangle region {len(tri)} E={E(tri)}')
# entry 35
A=L9(); S=set(A)
rev=[(c[4],c[5],c[6],c[3],c[0],c[1],c[2],c[8],c[7]) for c in A]; R=set(rev)
print('rev(L9):',len(R),'cells, E=',E(rev),'; equals L9:',R==S)
I=S&R; print('intersection',len(I),f'{100*len(I)/len(A):.1f}%','all g=q=k:',all(c[2]==c[3]==c[6] for c in I),'E=',E(sorted(I)))
objs=set((c[0],c[1],c[2],c[7]) for c in I); print(' objects',len(objs),'identities present:',all((o[0],o[1],o[2],o[2],o[0],o[1],o[2],o[3],o[3]) in I for o in objs),
      'every morphism has inverse in I:',all((c[4],c[5],c[6],c[3],c[0],c[1],c[2],c[8],c[7]) in I for c in I))
# factorises over its own transfer
byq=collections.defaultdict(list)
for c in I: byq[c[3]].append(c)
tot=sum(len(set((c[0],c[1],c[2],c[7]) for c in v))*len(set((c[4],c[5],c[6],c[8]) for c in v)) for v in byq.values()); print(' conditioned product over q',tot,'defect',tot-len(I))
U=sorted(S|R); Us=set(U); jf=mf=0
for i in range(len(U)):
    x=U[i]
    for y in U[i+1:]:
        if tuple(map(max,x,y)) not in Us: jf+=1
        if tuple(map(min,x,y)) not in Us: mf+=1
print('union',len(U),'failing joins',jf,'failing meets',mf)
# sublattice closure: iterate join and meet to fixed point
C=set(U); frontier=list(C)
while frontier:
    new=set(); Cl=list(C)
    for x in frontier:
        for y in Cl:
            for z in (tuple(map(max,x,y)),tuple(map(min,x,y))):
                if z not in C and z not in new: new.add(z)
    C|=new; frontier=list(new)
print('sublattice closure adds',len(C)-len(U),'cells')
