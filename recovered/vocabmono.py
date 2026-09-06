from itertools import product
from collections import defaultdict
def RR(X,d):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def E(X,d): return len(RR(X,d))-len(set(X))
# --- 18-column main table ---
occ=set()
for g in (1,18): occ.add((1,g))
for p in (2,3):
    for g in [1,2,13,14,15,16,17,18]: occ.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): occ.add((p,g))
def block18(g):           # l as a function of group
    if g in (1,2): return 0
    if 3<=g<=12: return 2
    return 1
print('  IS l MONOTONE IN THE INDEX COORDINATE?')
seq18=[block18(g) for g in range(1,19)]
print('     18-column, l by group 1..18 :', seq18)
print('       monotone non-decreasing? %s   non-increasing? %s'
      % (seq18==sorted(seq18), seq18==sorted(seq18,reverse=True)))
# --- Janet: rows n+l, blocks ordered f,d,p,s ---
W=[2,2,8,8,18,18,32,32]
def janet_l(pos,width):
    # within a Janet row the blocks run f(14) d(10) p(6) s(2), trailing-aligned
    caps=[(3,14),(2,10),(1,6),(0,2)]
    tot=0; segs=[]
    for l,c in caps:
        if tot+c<=width: segs.append((l,c)); tot+=c
    # rows are shorter for small n+l: keep the LAST segments (s always present)
    segs=[]; rem=width
    for l,c in reversed(caps):
        if rem>=c: segs.insert(0,(l,c)); rem-=c
    out=[]
    for l,c in segs: out += [l]*c
    return out
print()
for w in W[:6]:
    seq=janet_l(0,w)
    print('     Janet row width %2d, l by position : %-34s monotone non-increasing? %s'
          % (w, str(seq)[:34], seq==sorted(seq,reverse=True)))
print()
print('  DOES MONOTONICITY PREDICT CLOSURE?')
print('  %-46s %6s %6s' % ('presentation','cells','E'))
print('  %-46s %6d %6d' % ('(period, group)  l non-monotone in group', len(occ), E(occ,2)))
byp=defaultdict(list)
for p,g in occ: byp[p].append(g)
contig={(p,i+1) for p,gs in byp.items() for i in range(len(gs))}
print('  %-46s %6d %6d' % ('(period, position) contiguous', len(contig), E(contig,2)))
janet={(r+1,i+1) for r,w in enumerate(W) for i in range(w)}
print('  %-46s %6d %6d' % ('Janet (n+l, position)  l monotone', len(janet), E(janet,2)))
# --- explicit test: add l as a third coordinate, in each ordering ---
X3a={(p,g,block18(g)) for p,g in occ}
print('  %-46s %6d %6d' % ('(period, group, l)  l as given', len(X3a), E(X3a,3)))
X3b={(p,g,3-block18(g)) for p,g in occ}
print('  %-46s %6d %6d' % ('(period, group, 3-l)  l reversed', len(X3b), E(X3b,3)))
print()
print('  THE POINT')
print('     l IS determined by group in the 18-column table, so the term is present.')
print('     But l(group) = 0,0,2,...,2,1,...,1 is NOT monotone, so no envelope can use it.')
print('     Janet orders blocks f,d,p,s so that l decreases monotonically with position.')
print('     Vocabulary containment is necessary but not sufficient: it must be MONOTONE.')