from tower import base, exact_2S, exact_2J, phihat

def chains(caps):
    n_,e_,l_,k_,f_=caps
    B=base(caps)
    ph={k:phihat(k,l_) for k in range(0,k_+1)}
    A={'8':B}; P={'8':B}
    def ext(src,fn): return [c+(v,) for c in src for v in fn(c)]
    # 9
    A['9']=ext(A['8'],lambda c: range(0,c[6]+1))
    P['9']=ext(P['8'],lambda c: exact_2S(c[5],c[6]))
    # 9'
    A["9'"]=[c for c in A['9'] if c[8]<=2*c[5]+1]
    P["9'"]=[c for c in P['9'] if c[8]<=2*c[5]+1]
    # 10  seniority: v with 2S' <= v <= g ; exact v: same parity, term present in f^v
    A['10']=ext(A['9'],lambda c: range(c[8],c[6]+1))
    P['10']=ext(P['9'],lambda c: [v for v in range(c[8],c[6]+1,2) if c[8] in exact_2S(c[5],v)])
    # 11  core fine structure
    A['11']=ext(A['10'],lambda c: range(0,ph[c[2]]+1))
    P['11']=ext(P['10'],lambda c: exact_2J(c[1],c[2]))
    # 12  K, tree bound vs exact triangle with f
    A['12']=ext(A['11'],lambda c: range(0,c[10]+2*f_+1))
    P['12']=ext(P['11'],lambda c: range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2))
    # 13  J
    A['13']=ext(A['12'],lambda c: range(max(0,c[11]-1),c[11]+2))
    P['13']=ext(P['12'],lambda c: [j for j in (c[11]-1,c[11]+1) if j>=0])
    return A,P,ph

def report(caps):
    A,P,ph=chains(caps)
    out={}
    for k in ['8','9',"9'",'10','11','12','13']:
        out[k]=(len(A[k]),len(P[k]),len(P[k])/len(A[k]))
    return out,ph