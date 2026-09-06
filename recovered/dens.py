from tower import base, exact_2S, exact_2J, phihat

def densities(caps):
    n_,e_,l_,k_,f_=caps
    B=base(caps)
    ph={k:phihat(k,l_) for k in range(0,k_+1)}
    d={}
    a=x=0
    for c in B:
        f,g=c[5],c[6]; a+=g+1; x+=len(exact_2S(f,g))
    d['9']=x/a
    a=x=0
    for c in B:
        f,g=c[5],c[6]; a+=min(g,2*f+1)+1; x+=len(exact_2S(f,g))
    d["9'"]=x/a
    a=x=0
    for c in B:
        f,g=c[5],c[6]
        for S2 in range(0,g+1):
            a+=g-S2+1
            if S2 in exact_2S(f,g):
                x+=len([v for v in range(S2,g+1,2) if S2 in exact_2S(f,v)])
    d['10']=x/a
    a=x=0
    for c in B:
        l,k=c[1],c[2]; a+=ph[k]+1; x+=len(exact_2J(l,k))
    d['11']=x/a
    a=x=0
    for c in B:
        l,k,f=c[1],c[2],c[5]
        for j2 in range(0,ph[k]+1):
            a+=j2+2*f_+1
            if j2 in exact_2J(l,k):
                x+=len(range(abs(j2-2*f), j2+2*f+1, 2))
    d['12']=x/a
    a=x=0
    for c in B:
        l,k,f=c[1],c[2],c[5]
        for j2 in range(0,ph[k]+1):
            for K2 in range(0,j2+2*f_+1):
                adm=[J for J in range(max(0,K2-1),K2+2)]
                exa=[J for J in (K2-1,K2+1) if J>=0]
                a+=len(adm); x+=len(exa)
    d['13']=x/a
    return d