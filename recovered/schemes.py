import sys, itertools; sys.path.insert(0,'/home/claude/method')
from functools import lru_cache
from collections import Counter
from itertools import product
import method_tower as mt
CAPS=(3,3,1,3,1); nn,ee,ll,kk,ff=CAPS
@lru_cache(maxsize=None)
def terms(l,k):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (1,-1)]
    cnt=Counter()
    for combo in itertools.combinations(range(len(orbs)),k):
        ML=sum(orbs[i][0] for i in combo); MS2=sum(orbs[i][1] for i in combo)
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
def maxL2(l,k): 
    t=terms(l,k); return max((L for S,L in t), default=0)
@lru_cache(maxsize=None)
def max2J(l,k):
    js=set()
    for S2,L2 in terms(l,k):
        for j2 in range(abs(L2-S2),L2+S2+1,2): js.add(j2)
    return max(js) if js else 0
def phi(f,k):
    return max((f(l,kk2) for l in range(0,ll+1) for kk2 in range(1,min(4*l+2,k)+1)),default=0)
PHJ={k:phi(max2J,k) for k in range(0,kk+1)}
PHL={k:phi(maxL2,k) for k in range(0,kk+1)}
B=sorted(set(mt.base(CAPS)))
L9=[c+(s,) for c in B for s in range(0,c[6]+1)]
L10=[c+(v,) for c in L9 for v in range(c[8],c[6]+1)]
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            ph[(i,j)]=o
    tot=0; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d: tot+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>ph[(i,j)][cur[j]] or cur[j]>ph[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S)
SCHEMES={}
# jK (as built): 2Jc, 2K = Jc+f, 2J = K +- 1/2
A=[c+(j,) for c in L10 for j in range(0,PHJ[c[2]]+1)]
A2=[c+(K,) for c in A for K in range(0,c[10]+2*ff+1)]
A3=[c+(J,) for c in A2 for J in range(max(0,c[11]-1),c[11]+2)]
SCHEMES['jK  (as built)']=[A,A2,A3]
# LS throughout: 2Lc, 2Ltot = Lc+f, 2Stot = S +- 1/2, 2J = |L-S|..L+S  (loose)
Bv=[c+(L,) for c in L10 for L in range(0,PHL[c[2]]+1)]
B2=[c+(Lt,) for c in Bv for Lt in range(0,c[10]+2*ff+1)]
B3=[c+(J,) for c in B2 for J in range(0,c[11]+c[7]+2)]
SCHEMES['LS  (L then J)']=[Bv,B2,B3]
# jj: 2jc, 2jo in {2f-1,2f+1}, 2J = |jc-jo|..jc+jo  (loose)
Cv=[c+(jc,) for c in L10 for jc in range(0,PHJ[c[2]]+1)]
C2=[c+(jo,) for c in Cv for jo in range(max(0,2*c[5]-1),2*c[5]+2)]
C3=[c+(J,) for c in C2 for J in range(0,c[10]+c[11]+1)]
SCHEMES['jj  (j1 j2)']=[Cv,C2,C3]
# LK: 2Ltot, 2K = Ltot + Score, 2J = K +- 1/2
Dv=[c+(Lt,) for c in L10 for Lt in range(0,PHL[c[2]]+2*ff+1)]
D2=[c+(K,) for c in Dv for K in range(0,c[10]+c[7]+1)]
D3=[c+(J,) for c in D2 for J in range(max(0,c[11]-1),c[11]+2)]
SCHEMES['LK  (L then K)']=[Dv,D2,D3]
print('  LAMBDA UNDER FOUR COUPLING SCHEMES')
print('  shared base: Lambda_8 = %d, Lambda_9 = %d, Lambda_10 = %d  (E = %d, %d, %d)'
      % (len(set(B)),len(set(L9)),len(set(L10)),E(set(B),8),E(set(L9),9),E(set(L10),10)))
print()
print('  %-18s %10s %10s %10s   %6s %6s %6s' % ('scheme','L11','L12','L13','E11','E12','E13'))
for nm,(a,b,c) in SCHEMES.items():
    sa,sb,sc=set(a),set(b),set(c)
    print('  %-18s %10d %10d %10d   %6d %6d %6d'
          % (nm,len(sa),len(sb),len(sc),E(sa,11),E(sb,12),E(sc,13)))
print()
print('  WHY')
print('     every scheme is a chain of vector-coupling bounds |a-b| <= c <= a+b.')
print('     the LOOSE form 0 <= c <= a+b binds one coordinate by a monotone function')
print('     of one other, which is exactly the closure rule of 1.8.')
print('     the EXACT form needs two parents (a and b) and is ternary - which is 2.4.')
print()
print('  CONSEQUENCE')
print('     E = 0 is NOT scheme-contingent. Lambda closes in all four.')
print('     what IS scheme-contingent is what the letters MEAN:')
print('        2K in jK is Jc + l_outer ; in LK it is L_total + S_core ; jj has no K at all.')
print('     so the audit finding stands - the scheme is an unstated jurisdiction -')
print('     but it does not threaten the null case. Part II needs a caveat, not a demotion.')