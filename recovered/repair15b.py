"""Reproduce the fifteen-letter repairs using the EXACT nine-letter conventions from data2.py."""
from itertools import product, permutations
from collections import defaultdict
RNG=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
     range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)
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
V={c for c in {close(x) for x in product(*RNG)} if c[Sf]==0}
V={c for c in V if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
base=E(V,15)
print('  baseline: %d cells, E = %d' % (len(V),base))
print()
print('  APPLYING THE NINE-LETTER CONVENTIONS VERBATIM')
print()
# --- merge by linearisation: collapse the two payer axes into one ordered axis
def lin():
    pairs=sorted({(c[Xe],c[Ug]) for c in V})
    paid=lambda p: 0 if (p[0]==0 and p[1]==0) else 1
    W=sorted(pairs,key=lambda p:(paid(p),p[0],p[1])); Wi={p:i for i,p in enumerate(W)}
    keep=[i for i in range(15) if i not in (Xe,Ug)]
    S={(Wi[(c[Xe],c[Ug])],)+tuple(c[i] for i in keep) for c in V}
    return E(S,14), len(S)
# --- slide within rows: on the minimal triple, compress the third to its rank in the row
def slide():
    T={(c[Xe],c[Ug],c[Np]) for c in V}
    rows=defaultdict(list)
    for a,b,n in T: rows[(a,b)].append(n)
    S={(a,b,sorted(rows[(a,b)]).index(n)) for a,b,n in T}
    return E(S,3), len(S)
# --- and the triple itself, for reference
def triple():
    T={(c[Xe],c[Ug],c[Np]) for c in V}
    return E(T,3), len(T)
for nm,f in [('merge by linearisation',lin),('slide within rows',slide),('the triple itself',triple)]:
    e,n=f(); print('     %-26s cells %6d   E = %d' % (nm,n,e))
print()
print('  AGAINST THE PAPER')
print('     paper: merge by linearisation 7,734   slide within rows 8,856')
e1,_=lin(); e2,_=slide()
print('     here : merge by linearisation %-7d slide within rows %d' % (e1,e2))
print()
print('  AND THE NINE-LETTER VALUES, FOR CALIBRATION')
print('     data.json: linearisation 414, slide 10')
print('     the slide operation acts on the TRIPLE (3 coordinates), so its E is small.')
print('     8,856 is far too large for a 3-coordinate object: the box there is at most')
print('     4 x 2 x 5 = 40, so E <= 40 - cells. the paper figure cannot be this operation.')