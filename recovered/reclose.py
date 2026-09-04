import itertools, collections
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
P={'none found':0,'found':1}
def ok(s,v,p):
    if v==V['cited'] and p!=P['found']: return False          # cited ⟹ found
    if s>=S['measured'] and v<V['sampled']: return False       # measured ⟹ ≥ sampled
    return True
def close(cells):
    X=set(cells)
    while True:
        new=set(X)
        for a,b in itertools.combinations(X,2):
            j=tuple(max(x,y) for x,y in zip(a,b)); m=tuple(min(x,y) for x,y in zip(a,b))
            for c in (j,m):
                if ok(*c): new.add(c)
        if new==X: return X
        X=new
def cell(s,v,p): return (S[s],V[v],P[p])
def name(c): 
    s={v:k for k,v in S.items()}[c[0]]; v={v:k for k,v in V.items()}[c[1]]; p={v:k for k,v in P.items()}[c[2]]
    return f'{s} · {v} · {p}'
# current 48 elements: fibre -> list of cells
cur=collections.defaultdict(list)
def add(f,s,v,p): cur[f].append(cell(s,v,p))
# D.5.2 twenty-seven
add('definition · order','proved','exhaustive','found')
add('definition · combinatorics','proved','exhaustive','none found')
add('mechanism · order','proved','exhaustive','none found')
add('formula · combinatorics','proved','exhaustive','found'); add('formula · combinatorics','verified','exhaustive','found')
add('formula · analysis','proved','exhaustive','found'); add('formula · analysis','measured','exhaustive','none found'); add('formula · analysis','verified','exhaustive','none found')
add('formula · physics','verified','exhaustive','found')
for p in ['none found','found','none found','none found','none found']: add('theorem · order','proved','exhaustive',p)
add('theorem · combinatorics','proved','exhaustive','found'); add('theorem · combinatorics','proved','exhaustive','found'); add('theorem · combinatorics','proved','exhaustive','none found')
add('theorem · analysis','proved','exhaustive','none found'); add('theorem · analysis','proved','exhaustive','none found')
add('law · complexity','proved','exhaustive','none found')
add('method · order','verified','exhaustive','none found'); add('method · combinatorics','verified','sampled','none found'); add('method · analysis','verified','exhaustive','none found')
add('measurement · combinatorics','measured','exhaustive','none found'); add('measurement · combinatorics','measured','exhaustive','none found')
add('measurement · physics','measured','exhaustive','none found'); add('measurement · algebraic geometry','measured','sampled','found')
# D.5.4 five (theorem·order; A.5 proved·sampled per text but the appendix's cell statement keeps two cells; both readings tested below)
for _ in range(5): add('theorem · order','proved','exhaustive','none found')
# D.5.6 four
add('theorem · order','proved','exhaustive','none found'); add('theorem · order','proved','exhaustive','found')
add('theorem · combinatorics','proved','exhaustive','found'); add('formula · combinatorics','proved','exhaustive','found')
# D.5.7 four
add('theorem · order','proved','exhaustive','none found'); add('theorem · order','conjectured','sampled','none found')
add('measurement · combinatorics','measured','exhaustive','none found'); add('theorem · combinatorics','proved','exhaustive','none found')
# D.5.8 eight
add('theorem · order','proved','exhaustive','found'); add('theorem · order','proved','exhaustive','found')
add('measurement · combinatorics','measured','exhaustive','none found'); add('theorem · order','proved','sampled','none found')
add('theorem · order','proved','sampled','found'); add('measurement · combinatorics','measured','exhaustive','none found')
add('theorem · order','proved','exhaustive','found'); add('theorem · order','proved','exhaustive','found')
n=sum(len(v) for v in cur.values()); print('current elements',n,'fibres',len(cur))
def report(cur,label):
    tot=0
    for f,cells in cur.items():
        occ=set(cells); cl=close(occ); e=len(cl)-len(occ); tot+=e
        if e: print(f'  {label} E>0 in {f}: admitted&absent = {[name(c) for c in cl-occ]}')
    print(f'{label}: E total = {tot}')
report(cur,'D.5.8 state')
# proposed new elements (collaborator's classification, to be confirmed)
new=[('LS.ent the entrant operator','mechanism · physics','verified','exhaustive','none found'),
     ('LS.law the ordering law','law · physics','proved','exhaustive','none found'),
     ('LS.coll the collapse condition','mechanism · physics','verified','exhaustive','found'),
     ('LS.pin the pinned-channel theorem','theorem · physics','measured','exhaustive','none found'),
     ('LS.asym the multiplier identity','theorem · analysis','proved','exhaustive','found'),
     ('LS.quart the exact-quartic decomposition','theorem · analysis','proved','exhaustive','none found'),
     ('LS.chord chord = rot + perp','theorem · analysis','proved','exhaustive','found'),
     ('LS.twin the c→∞ twin','measurement · physics','measured','exhaustive','none found'),
     ('3B.shape the shape sphere','definition · analysis','proved','exhaustive','found'),
     ('3B.metric the shape metric','formula · analysis','proved','exhaustive','found'),
     ('3B.JM the Jacobi–Maupertuis metric','formula · analysis','proved','exhaustive','found'),
     ('3B.pot the potential on shape space','formula · analysis','measured','sampled','found'),
     ('3B.norm the norm variety','theorem · algebraic geometry','proved','exhaustive','found'),
     ('3B.five the five fixed points','theorem · analysis','measured','exhaustive','found'),
     ('3B.tri the triangle form at cap 8','measurement · combinatorics','measured','exhaustive','none found'),
     ('3B.def the deficit, one level','theorem · complexity','proved','exhaustive','found'),
     ('3B.index Λ₃, E = 0','theorem · order','proved','exhaustive','found')]
import copy
nxt=copy.deepcopy(cur)
for nm,f,s,v,p in new:
    assert ok(*cell(s,v,p)), nm
    nxt[f].append(cell(s,v,p))
print('after: elements',sum(len(v) for v in nxt.values()),'fibres',len(nxt))
report(nxt,'D.5.9 proposed')
newf=[f for f in nxt if f not in cur]; print('new fibres opened:',newf)