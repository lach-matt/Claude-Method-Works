from tower2mod import L12,L13,PHI
from l27 import terms
print('phi-hat (tower-2):',PHI,' realised p-shell max2J by term enumeration:',{k:max(2*L+S2 for (L,S2) in terms(1,k)) for k in (1,2,3)})
A=L12(); B=L13()
# two-parent law 2K <= 2Jc + 2f (cell's f, idx5) ; 2K idx 11, 2Jc idx 10
b12=sum(1 for c in A if c[11]>c[10]+2*c[5]); b13=sum(1 for c in B if c[11]>c[10]+2*c[5])
print(f'L12 cells breaking 2K<=2Jc+2f: {b12} ({100*b12/len(A):.1f}%)  L13: {b13} ({100*b13/len(B):.1f}%)')
print('L12 cells with f below the cap (f=0):',sum(1 for c in A if c[5]<1),'of',len(A))
# entry 29: dipole region |d2J|<=2 on (2J,2J') box 0..cap, minus (0,0)
for cap in (4,6,8):
    R=[(a,b) for a in range(cap+1) for b in range(cap+1) if abs(a-b)<=2 and (a,b)!=(0,0)]; S=set(R)
    mf=[]; jf=0
    for i in range(len(R)):
        for j in range(i+1,len(R)):
            m=(min(R[i][0],R[j][0]),min(R[i][1],R[j][1]))
            if m not in S: mf.append((R[i],R[j],m))
            if (max(R[i][0],R[j][0]),max(R[i][1],R[j][1])) not in S: jf+=1
    # closure R(X): add cells implied; pairwise projections in 2 coords = the set itself... use: cells whose meet/join closure
    C=set(S); ch=True
    while ch:
        ch=False
        for x in list(C):
            for y in list(C):
                for z in ((min(x[0],y[0]),min(x[1],y[1])),(max(x[0],y[0]),max(x[1],y[1]))):
                    if z not in C: C.add(z); ch=True
    print(f'cap {cap}: meet failures {len(mf)} (restored cells {set(m for _,_,m in mf)}), join failures {jf}, E={len(C)-len(S)}')
    if cap==4: print('   failing meets:',[(x,y) for x,y,_ in mf])