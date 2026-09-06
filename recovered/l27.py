import itertools, collections, time
t0=time.time()
def region(cap,parity=False):
    R=[]
    for L2 in range(cap+1):
        for S2 in range(cap+1):
            for J2 in range(cap+1):
                if abs(L2-S2)<=J2<=L2+S2 and (not parity or (J2-L2-S2)%2==0): R.append((L2,S2,J2))
    return R
for cap in (6,8,10,12):
    R=region(cap); S=set(R); jf=mf=0
    for i in range(len(R)):
        x=R[i]
        for j in range(i+1,len(R)):
            y=R[j]
            if tuple(map(max,x,y)) not in S: jf+=1
            if tuple(map(min,x,y)) not in S: mf+=1
    print(f'cap {cap}: |region|={len(R)} join failures {jf} meet failures {mf}')
R=region(6,parity=True); S=set(R); jf=0
for i in range(len(R)):
    for j in range(i+1,len(R)):
        if tuple(map(max,R[i],R[j])) not in S: jf+=1
print('cap 6 with parity congruence: join failures',jf)
# LS terms of l^k by microstate enumeration: count terms (L,S multiset) 
def terms(l,k):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (-1,1)]
    cnt=collections.Counter()
    for combo in itertools.combinations(orbs,k):
        cnt[(sum(m for m,_ in combo), sum(s for _,s in combo))]+=1   # (ML, 2MS)
    T=collections.Counter()
    for (ML,MS2),n in sorted(cnt.items(),key=lambda t:(-t[0][0],-t[0][1])):
        pass
    # extract terms: standard peeling
    T=collections.Counter(); c=dict(cnt)
    while any(v>0 for v in c.values()):
        ML,MS2=max((k for k,v in c.items() if v>0),key=lambda t:(t[0],t[1]))
        T[(ML,MS2)]+=1
        for ml in range(-ML,ML+1):
            for ms in range(-MS2,MS2+1,2): c[(ml,ms)]-=1
    return T
for l,name in ((1,'p'),(2,'d')):
    sym=all(terms(l,k)==terms(l,4*l+2-k) for k in range(0,4*l+3))
    print(name,'shell: terms(l^k)==terms(l^(4l+2-k)) for all k:',sym)
# max 2J over terms of f^k
for k in range(0,15):
    T=terms(3,k); m=max((2*L+S2 for (L,S2) in T),default=0); print(f'f^{k}: max2J={m}',end='; ')
print(); print('time',round(time.time()-t0))