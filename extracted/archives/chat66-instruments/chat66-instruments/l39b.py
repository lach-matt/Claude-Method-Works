from tower2mod import L9
def subclose(U):
    C=set(U); frontier=list(C)
    while frontier:
        new=set(); Cl=list(C)
        for x in frontier:
            for y in Cl:
                for z in (tuple(map(max,x,y)),tuple(map(min,x,y))):
                    if z not in C: new.add(z)
        C|=new; frontier=list(new)
    return len(C)-len(U)
A=L9()
par=[c for c in A if abs(c[5]-c[1])==1]; print('parity set sublattice-closure E =',subclose(par))
spin=[c for c in A if c[8]==c[7]]; print('spin set sublattice-closure E =',subclose(spin))
dl=lambda c:c[5]-c[1]; ds=lambda c:c[8]-c[7]
for name,fs in {'(dl,dS)':[dl,ds],'(|dl|,dS)':[lambda c:abs(dl(c)),ds],'(dl,dS,|dl|)':[dl,ds,lambda c:abs(dl(c))],'(dl,|dS|)':[dl,lambda c:abs(ds(c))],'(|dl|,|dS|)':[lambda c:abs(dl(c)),lambda c:abs(ds(c))]}.items():
    X=[c+tuple(f(c) for f in fs) for c in A]; print(f'adjoin {name}: sublattice-closure E={subclose(X)}')
img=set((abs(dl(c)),ds(c)) for c in A); print('image (|dl|,dS) missing:',[(m,s) for m in (0,1) for s in range(-3,4) if (m,s) not in img])
img2=set((abs(dl(c)),abs(ds(c))) for c in A); print('image (|dl|,|dS|) missing:',[(m,s) for m in (0,1) for s in range(0,4) if (m,s) not in img2])
