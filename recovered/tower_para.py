import itertools, sys
from functools import lru_cache
from collections import Counter
from itertools import product
@lru_cache(maxsize=None)
def terms_m(l,k,m):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (1,-1)]
    cnt=Counter()
    for combo in itertools.combinations_with_replacement(range(len(orbs)),k):
        c=Counter(combo)
        if any(v>m for v in c.values()): continue
        ML=sum(orbs[i][0]*n for i,n in c.items()); MS2=sum(orbs[i][1]*n for i,n in c.items())
        cnt[(2*ML,MS2)]+=1
    out=[]
    while cnt:
        L2=max(a for (a,b) in cnt); S2=max(b for (a,b) in cnt if a==L2)
        for a in range(-L2,L2+1,2):
            for b in range(-S2,S2+1,2):
                if (a,b) in cnt:
                    cnt[(a,b)]-=1
                    if cnt[(a,b)]==0: del cnt[(a,b)]
        out.append((S2,L2))
    return tuple(out)
@lru_cache(maxsize=None)
def ex2J(l,k,m):
    js=set()
    for S2,L2 in terms_m(l,k,m):
        for j2 in range(abs(L2-S2),L2+S2+1,2): js.add(j2)
    return tuple(sorted(js))
def max2J(l,k,m):
    e=ex2J(l,k,m); return max(e) if e else 0
def cap(l,m): return m*(4*l+2)
def phihat(k,lcap,m):
    best=0
    for kk in range(0,k+1):
        best=max(best,max((max2J(l,kkk,m) for l in range(0,lcap+1)
                           for kkk in range(1,min(cap(l,m),kk)+1)),default=0))
    return best
def base_m(caps,m):
    nn,ee,ll,kk,ff=caps; cells=[]
    for n in range(1,nn+1):
      for l in range(0,min(n-1,ll)+1):
        for k in range(1,min(cap(l,m),kk)+1):
          for q in range(0,k+1):
            for S2 in range(0,k+1):
              for e in range(1,ee+1):
                for f in range(0,min(e-1,ff)+1):
                  for g in range(0,min(cap(f,m),q)+1):
                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
def envelopes(X,d):
    vals=[sorted({c[i] for c in X}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            mx={}
            for c in X:
                if c[i]>mx.get(c[j],-99): mx[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(mx): b=max(b,mx[t]); o[t]=b
            phi[(i,j)]=o
    return vals,phi
def count_R(X,d):
    X=set(X); vals,phi=envelopes(X,d)
    total=0
    cur=[None]*d
    def rec(i):
        nonlocal total
        if i==d:
            total+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok:
                cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return total
CAPS=(3,3,1,3,1); n_,e_,l_,k_,f_=CAPS
print('  %s %8s %8s %8s %8s %8s %8s' % ('m','L8','L9','L10','L11','L12','L13'))
print('  %s %8s %8s %8s %8s %8s %8s' % (' ','E','E','E','E','E','E'))
for m in (1,2,3):
    B=base_m(CAPS,m); ph={k:phihat(k,l_,m) for k in range(0,k_+1)}
    L9=[c+(s,) for c in B for s in range(0,c[6]+1)]
    L10=[c+(v,) for c in L9 for v in range(c[8],c[6]+1)]
    L11=[c+(j,) for c in L10 for j in range(0,ph[c[2]]+1)]
    L12=[c+(K,) for c in L11 for K in range(0,c[10]+2*f_+1)]
    L13=[c+(J,) for c in L12 for J in range(max(0,c[11]-1),c[11]+2)]
    sizes=[len(set(x)) for x in (B,L9,L10,L11,L12,L13)]
    Es=[]
    for X,d in [(B,8),(L9,9),(L10,10),(L11,11),(L12,12),(L13,13)]:
        Xs=set(X); box=1
        vals,_=envelopes(Xs,d)
        for v in vals: box*=len(v)
        r=count_R(Xs,d)
        Es.append((r-len(Xs), box))
    print('  %d %8d %8d %8d %8d %8d %8d' % ((m,)+tuple(sizes)))
    print('    %8d %8d %8d %8d %8d %8d   <- E' % tuple(e for e,_ in Es))
    print('    boxes: %s' % ', '.join('%.3g'%b for _,b in Es))