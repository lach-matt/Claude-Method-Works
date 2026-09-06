import itertools, collections
def terms(l,k):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (-1,1)]
    cnt=collections.Counter()
    for combo in itertools.combinations(orbs,k):
        cnt[(sum(m for m,_ in combo), sum(s for _,s in combo))]+=1
    T=collections.Counter(); c=dict(cnt)
    while any(v>0 for v in c.values()):
        ML,MS2=max((q for q,v in c.items() if v>0),key=lambda t:(t[0],t[1]))
        T[(ML,MS2)]+=1
        for ml in range(-ML,ML+1):
            for ms in range(-MS2,MS2+1,2): c[(ml,ms)]-=1
    return T