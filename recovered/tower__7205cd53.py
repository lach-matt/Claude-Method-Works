import itertools
from functools import lru_cache

# ---- exact term structure of l^k by microstate enumeration ----
@lru_cache(maxsize=None)
def terms(l,k):
    """return set of (2S,2L) ... we need max 2J and the 2S set; do full LS decomposition."""
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (1,-1)]
    from collections import Counter
    cnt=Counter()
    for c in itertools.combinations(range(len(orbs)),k):
        ML=sum(orbs[i][0] for i in c); MS2=sum(orbs[i][1] for i in c)
        cnt[(2*ML,MS2)]+=1
    out=[]
    while cnt:
        ML2max=max(m for m,_ in cnt if cnt[(m,_)] if True) if False else max(m for (m,s) in cnt)
        cand=[(m,s) for (m,s) in cnt if m==ML2max]
        MS2max=max(s for (m,s) in cand)
        L2,S2=ML2max,MS2max
        for m in range(-L2,L2+1,2):
            for s in range(-S2,S2+1,2):
                cnt[(m,s)]-=1
                if cnt[(m,s)]==0: del cnt[(m,s)]
        out.append((S2,L2))
    return tuple(out)

@lru_cache(maxsize=None)
def exact_2S(l,k):
    return tuple(sorted({S2 for S2,L2 in terms(l,k)}))

@lru_cache(maxsize=None)
def exact_2J(l,k):
    js=set()
    for S2,L2 in terms(l,k):
        for j2 in range(abs(L2-S2), L2+S2+1, 2): js.add(j2)
    return tuple(sorted(js))

@lru_cache(maxsize=None)
def max2J(l,k):
    e=exact_2J(l,k); return max(e) if e else 0

def phihat(k,lcap):
    """monotone envelope of max2J over parent shells up to the caps"""
    best=0; out={}
    for kk in range(0,k+1):
        m=max(( max2J(l,kkk) for l in range(0,lcap+1) for kkk in range(1,min(4*l+2,kk)+1) ), default=0)
        best=max(best,m); out[kk]=best
    return out[k]

# ---- the base lattice ----
def base(caps):
    n_,e_,l_,k_,f_=caps
    cells=[]
    for n in range(1,n_+1):
      for l in range(0,min(n-1,l_)+1):
        for k in range(1,min(4*l+2,k_)+1):
          for q in range(0,k+1):
            for S2 in range(0,k+1):
              for e in range(1,e_+1):
                for f in range(0,min(e-1,f_)+1):
                  for g in range(0,min(4*f+2,q)+1):
                    cells.append((n,l,k,q,e,f,g,S2))
    return cells

def tower_counts(caps):
    n_,e_,l_,k_,f_=caps
    B=base(caps)
    r={'8':len(B)}
    # axis 9 : 2S' <= g
    L9=[c+(s,) for c in B for s in range(0,c[6]+1)]
    r['9']=len(L9)
    # axis 9' : + 2S' <= 2f+1
    L9p=[c for c in L9 if c[8]<=2*c[5]+1]
    r["9'"]=len(L9p)
    # axis 10 : 2S' <= v <= g
    L10=[c+(v,) for c in L9 for v in range(c[8],c[6]+1)]
    r['10']=len(L10)
    # axis 11 : 2Jc <= phihat(k)
    ph={k:phihat(k,l_) for k in range(0,k_+1)}
    L11=[c+(j,) for c in L10 for j in range(0,ph[c[2]]+1)]
    r['11']=len(L11)
    # axis 12 tree : 2K <= 2Jc + 2*f_max
    L12=[c+(K,) for c in L11 for K in range(0,c[10]+2*f_+1)]
    r['12']=len(L12)
    # axis 13 : |2J - 2K| <= 1
    L13=[c+(J,) for c in L12 for J in range(max(0,c[11]-1),c[11]+2)]
    r['13']=len(L13)
    return r,dict(ph)

def densities(caps):
    """fraction of each fibre that exact vector coupling realises"""
    n_,e_,l_,k_,f_=caps
    B=base(caps)
    d={}
    # axis 9: over (f,g) fibres of the base; admissible 0..g, exact = terms of f^g
    adm=ex=0
    for c in B:
        f,g=c[5],c[6]
        adm+=g+1
        ex+=len(exact_2S(f,g))
    d['9']=ex/adm
    # axis 9': admissible min(g,2f+1)+1
    adm=ex=0
    for c in B:
        f,g=c[5],c[6]
        adm+=min(g,2*f+1)+1
        ex+=len(exact_2S(f,g))
    d["9'"]=ex/adm
    # axis 10: v fibre, admissible 2S'<=v<=g ; exact seniority set for (f,g,2S')
    # exact v for a term of f^g with spin 2S': v in {g, g-2, ...} with term present in f^v
    adm=ex=0
    for c in B:
        f,g=c[5],c[6]
        for S2p in range(0,g+1):
            adm+=max(0,g-S2p+1)
            if S2p in exact_2S(f,g):
                ex+=len([v for v in range(S2p,g+1,2) if S2p in exact_2S(f,v)])
    d['10']=ex/adm
    # axis 11: 2Jc fibre; admissible 0..phihat(k); exact = exact_2J(l,k)
    ph={k:phihat(k,l_) for k in range(0,k_+1)}
    adm=ex=0
    for c in B:
        l,k=c[1],c[2]
        adm+=ph[k]+1
        ex+=len(exact_2J(l,k))
    d['11']=ex/adm
    # axis 12: K fibre; admissible 0..2Jc+2f_max ; exact triangle |2Jc-2f|..2Jc+2f step2
    adm=ex=0
    for c in B:
        l,k,f=c[1],c[2],c[5]
        for j2 in range(0,ph[k]+1):
            adm+=j2+2*f_+1
            if j2 in exact_2J(l,k):
                ex+=len(range(abs(j2-2*f), j2+2*f+1, 2))
    d['12']=ex/adm
    # axis 13: J fibre given K; admissible |2J-2K|<=1 -> up to 3 values (>=0); exact doublet/singlet
    adm=ex=0
    for K2 in range(0,40):
        pass
    return d,ph